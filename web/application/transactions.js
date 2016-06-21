import React from 'react'
import { Link } from 'react-router'

import * as API from '../api'

export class List extends React.Component {
  state = {transactions: []}

  constructor(...args) {
    super(...args)
  }

  componentWillMount() {
    API.getTransactions().then(async json => {
      this.setState({transactions: json})
    })
  }

  render() {
    return <section>
      <ul>
        {this.state.transactions.slice(0, 20).map(item => this.renderListItem(item))}
      </ul>
    </section>
  }

  renderListItem(item) {
    return <li key={item.uuid}>
      <Link to={`/transactions/${item.uuid}`}>{item.uuid}</Link>
    </li>
  }
}

export class Show extends React.Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  componentWillMount() {
    API.getTransaction(this.props.params.id).then(async json => {
      console.log(json)
    })
  }

  render() {
    let t = this.state.transaction

    if (!t)
      return null

    return <section>
      <h2><span>{t.uuid}</span>: <span>{t.name}</span></h2>
    </section>
  }
}
