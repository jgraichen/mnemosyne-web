import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, Link, browserHistory } from 'react-router'

import Application from './application'

window.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render((
    <Router history={browserHistory}>
      <Route path="/" component={Application}>
      </Route>
    </Router>
  ), document.querySelector('#container'))
})
