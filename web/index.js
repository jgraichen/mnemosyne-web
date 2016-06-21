import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, IndexRoute, Link, browserHistory, hashHistory } from 'react-router'

import Main from './main'
import Traces from './application/traces'
import Dashboard from './application/dashboard'
import Applications from './application/applications'
import Transactions from './application/transactions'

window.addEventListener('DOMContentLoaded', () => {

  let router = <Router history={hashHistory}>
    <Route path="/" component={Main}>
      <IndexRoute component={Dashboard} />
      <Route path="transactions" component={Transactions} />
      <Route path="applications" component={Applications} />
      <Route path="traces" component={Traces} />
    </Route>
  </Router>

  ReactDOM.render(router, document.querySelector('#container'))
})
