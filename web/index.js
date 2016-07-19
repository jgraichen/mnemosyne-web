import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, IndexRoute, Link, browserHistory, hashHistory } from 'react-router'

import { Main } from './main'
import { Dashboard } from './application/dashboard'
import { Applications } from './application/applications'
import * as Transaction from './application/transactions'
import * as Trace from './application/traces'

window.addEventListener('DOMContentLoaded', () => {

  let router = <Router history={hashHistory}>
    <Route path="/" component={Main}>
      <IndexRoute component={Dashboard} />
      <Route path="transactions" component={Transaction.List} />
      <Route path="transactions/:id" component={Transaction.Show} />
      <Route path="applications" component={Applications} />
      <Route path="traces/:id" component={Trace.Show} />
    </Route>
  </Router>

  ReactDOM.render(router, document.querySelector('#container'))
})
