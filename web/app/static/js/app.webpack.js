var $ = require('jquery');
var React = require('react');
var ReactDOM = require('react-dom');

var TestApp = React.createClass({
  render: function() {
    return (
      <div>
        <h2>React works!</h2>
      </div>
    );
  }
});

ReactDOM.render(
  React.createElement(TestApp, null),
  document.getElementById('content')
);