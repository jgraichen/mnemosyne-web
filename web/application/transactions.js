import React from 'react'

import * as API from '../api'

export default class Transactions extends React.Component {
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
        {this.state.transactions.map(item => this.renderListItem(item))}
      </ul>
    </section>
  }

  renderListItem(item) {
    return <li key={item.uuid}>
      {item.name}
    </li>
  }
}
