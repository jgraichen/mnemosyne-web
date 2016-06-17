import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, Link, browserHistory, hashHistory } from 'react-router'

import Main from './main'
import Traces from './application/traces'
import Applications from './application/applications'

window.addEventListener('DOMContentLoaded', () => {

  let router = <Router history={hashHistory}>
    <Route path="/" component={Main}>
      <Route path="/applications" component={Applications} />
      <Route path="/traces" component={Traces} />
    </Route>
  </Router>

  ReactDOM.render(router, document.querySelector('#container'))
})
