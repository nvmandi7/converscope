import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';
import * as constants from './constants.js';
import Button from 'react-bootstrap/Button';
import MessageCountHistogram from './histogram.js';

function metric_pretty_name(metric_short_name) {
  return metric_short_name.replace(/_/g, ' ');
}

function MetricRow(props) {
  return (
    <div>
    <hr />
    <h5 className="small-caps">{metric_pretty_name(props.metric_name)}</h5>
    <div class="row">{props.values.map((arr) =>
      <div className="statistic col-sm-4">
      <div className="big-number" dangerouslySetInnerHTML={{__html: isNaN(arr[1]) ? arr[1] + '&#xfe0f;' : arr[1].toLocaleString()}} />
      <div className="small">{arr[0]}</div>
      </div>)}</div>
    </div>
  )
}

class DetailPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      groupName: '',
      metrics: {},
      x_axis: [],
      counts: [],
      random_message: {},
      tfidf: {},
      participants: [],
    };
  }

  fetchData = () => {
    let url = constants.URL_PREFIX + "/api/conversation?id=" + this.props.c_id;
    console.log(url);
    fetch(url)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            groupName: result.groupName,
            metrics: result.metrics,
            x_axis: result.dates,
            counts: result.count_by_day,
            random_message: 'randomMessage' in result ? result.randomMessage : {},
            tfidf: 'tfidf' in result ? result.tfidf : {},
            participants: result.participant,
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error: error,
          });
        }
      )
  }

  componentDidMount() {
    this.fetchData();
  }

  render() {
    if (this.state.error) {
      return <div>Error: {this.state.error.message}</div>;
    } else {
      return (
        <div>
          {this.state.isLoaded ? 
            <div>
              <div className="text-danger clip">{this.props.c_id}</div>
              <h4>{this.state.groupName}</h4>
              <div className="text-muted small">
                <ul className="participants">{this.state.participants.length > 0 ? this.state.participants.map((name) => <li key={this.state.c_id + name}>{name}</li>) : ""}</ul>
              </div>
              <hr />
              <h5 className="small-caps">messages by day</h5>
              <MessageCountHistogram x_axis={this.state.x_axis} counts={this.state.counts} />
              <div>
              {'content' in this.state.random_message ? 
              <div><hr /><h5 className="small-caps">blast from the past</h5>
              <blockquote class="blockquote text-center">
                <p class="mb-0">{this.state.random_message.content}</p>
                <footer class="blockquote-footer">{this.state.random_message.sender_name + ' on ' + (new Date(this.state.random_message.timestamp * 1000)).toLocaleDateString()}</footer>
              </blockquote>
              <div class="text-center"><Button variant="warning" onClick={() => this.fetchData()}>another one</Button></div>
              </div> : ''}
              {'tokens' in this.state.tfidf ?
              <div><hr /><h5 className="small-caps">tf-idf top tokens</h5>
              <div>
                {this.state.tfidf.tokens.map((token, index) => <div className="tfidf-token" style={{fontSize: this.state.tfidf.scores[index]*200 + 'pt'}}>{token}</div>)}
              </div>
              </div> : ''}
              {Object.entries(this.state.metrics).map(([key, value]) => <MetricRow metric_name={key} values={value} />)}
              </div>
            </div>
          : <div className="text-center">
              <div className="spinner-border" role="status">
                <span className="sr-only">Loading...</span>
              </div>
            </div>}
        </div>
      );
    }
  }
}

export default DetailPage;