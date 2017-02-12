import React from 'react';
import ReactDOM from 'react-dom';

import Event from './components/event'

ReactDOM.render(
  <Event url="http://localhost:8000/events/1/" />,
  document.getElementById('root')
);
