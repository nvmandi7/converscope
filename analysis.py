from constants import *
import chat_pb2
from metric_pb2 import *
from collections import Counter, defaultdict
import sys
import numpy as np
import datetime
import time
from enum import Enum
from emoji import UNICODE_EMOJI


class InboxAnalyzer:

    def __init__(self):
        f = open(EXPORT_PATH + ('.pbtxt' if USE_PBTXT else '.pb'),
                 'r' if USE_PBTXT else 'rb')
        inbox = chat_pb2.Inbox()
        inbox.ParseFromString(f.read())
        f.close()

        self.inbox = inbox
        self.id_conversation_map = {c.id: c for c in inbox.conversation}
        assert len(self.id_conversation_map) == len(inbox.conversation)
        self.oldest_ts = sys.maxsize
        self.newest_ts = -1
        for c_id in self.id_conversation_map.keys():
            old, new = self.__get_extreme_ts(c_id)
            self.oldest_ts = min(self.oldest_ts, old)
            self.newest_ts = max(self.newest_ts, new)
        print('InboxAnalyzer initialized,', len(self.id_conversation_map),
              'conversations')

    def get_conversations(self):
        """
		Return all conversation metadata stripped of messages.
		Returns: [Conversation]
		"""
        c_metadatas = []
        for c in self.id_conversation_map.values():
            c_metadata = chat_pb2.Conversation()
            c_metadata.id = c.id
            c_metadata.participant.extend(c.participant)
            c_metadata.group_name = c.group_name
            c_metadatas.append(c_metadata)
        return c_metadatas

    def get_message_counts(self, start_ts=0, end_ts=sys.maxsize):
        return {
            c.id: len(
                list(
                    filter(
                        lambda m: m.timestamp > start_ts and m.timestamp <
                        end_ts, c.message))) for c in self.inbox.conversation
        }

    def exists(self, c_id):
        return c_id in self.id_conversation_map

    def get_conversation(self, c_id):
        return self.id_conversation_map[c_id]

    def get_conversation_by_group_name(self, group_name):
        for c in self.inbox.conversation:
            if c.group_name == group_name:
                return c
        return None

    def get_oldest_ts(self):
        return self.oldest_ts

    def get_newest_ts(self):
        return self.newest_ts

    def __get_extreme_ts(self, c_id):
        c = self.id_conversation_map[c_id]
        if len(c.message) == 0:
            return sys.maxsize, -1
        # TODO hack: there appear to be some corrupted timestamps from ~2003. Filter to be >2007.
        return min(
            filter(lambda x: x > 1167638400,
                   map(lambda x: x.timestamp,
                       c.message))), max(map(lambda x: x.timestamp, c.message))

    def get_count_timeline(self, c_id):
        """
		If start_ts is -1, uses the oldest ts in the inbox as the start_ts.
		Bin granularity is by day.
		End ts is today.
		"""
        c = self.id_conversation_map[c_id]
        hist = defaultdict(int)
        for m in c.message:
            date_str = datetime.date.fromtimestamp(m.timestamp).isoformat()
            hist[date_str] += 1
        counts = [hist[x] if x in hist else 0 for x in self.get_date_range()]
        return counts

    def get_date_range(self):
        date_range = (datetime.date.fromtimestamp(self.oldest_ts),
                      datetime.date.fromtimestamp(self.newest_ts))
        dates = [date_range[0]]
        while dates[-1] != date_range[1]:
            dates.append(dates[-1] + datetime.timedelta(days=1))
        dates = list(map(lambda x: x.isoformat(), dates))
        return dates

    def longest_streak_days(self, c_id):
        hist = zip(self.get_count_timeline(c_id), self.get_date_range())
        best = 0
        best_end_date = ''
        curr = 0
        for count, date in hist:
            if count == 0:
                curr = 0
            else:
                curr += 1
            if curr > best:
                best = curr
                best_end_date = date
        return best, best_end_date

    def all_names(self):
        names = set()
        for c in self.inbox.conversation:
            names.update(c.participant)
        return names


def print_messages(conv, start_ts=0, end_ts=sys.maxsize):
    i = 0
    for message in sorted(conv.message, key=lambda m: m.timestamp):
        if message.timestamp > start_ts and message.timestamp < end_ts:
            print(
                i,
                datetime.datetime.fromtimestamp(message.timestamp).isoformat(),
                message.sender_name, ':', message.content)
            i += 1


class CountGranularity(Enum):
    MESSAGE = 1
    CHARACTER = 2


def get_counts_by_sender(conv, count_granularity):
    if count_granularity == CountGranularity.MESSAGE:
        return Counter(map(lambda x: x.sender_name, conv.message))
    elif count_granularity == CountGranularity.CHARACTER:
        c = defaultdict(int)
        for m in conv.message:
            c[m.sender_name] += len(m.content)
        return c


def main():
    ia = InboxAnalyzer()
    conv = ia.get_conversation('')
    print_messages(conv, 1467529200, 1469170800)


def emoji_counts(conv):
    emoji_list_by_name = defaultdict(list)
    for msg in conv.message:
        for char in msg.content:
            if char in UNICODE_EMOJI:
                emoji_list_by_name[msg.sender_name].append(char)
    return emoji_list_by_name


if __name__ == '__main__':
    main()
