DATA_DIR = './data/'

USE_PBTXT = False

# If true, does not store messages in the inbox file, and redacts names in the web app
STRIP_PII = True

# Data import/export

FB_IMPORT_PATH = DATA_DIR + '/facebook-daylenyang-json/messages'

IMESSAGE_IMPORT_PATH = '/Users/daylenyang/Dropbox/chat.db'
CONTACTS_PATH = '/Users/daylenyang/Dropbox/contacts.csv'
SELF_NAME = 'Daylen Yang'

EXPORT_PATH = DATA_DIR + '/inbox'
EXPORT_PATH_FB = DATA_DIR + '/inbox_fb'
EXPORT_PATH_IMESSAGE = DATA_DIR + '/inbox_imessage'

# Web app

HOME_MAX_CONVERSATIONS = 25
APP_PATH = 'converscope-react/build'