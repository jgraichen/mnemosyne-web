import React from 'react'

import { Panel } from '../components/panel'
import * as API from '../api'

export class Traces extends React.Component {
  state = {traces: []}

  constructor(...args) {
    super(...args)
  }

  componentWillMount() {
    API.getTraces().then(async json => {
      this.setState({traces: json})
    })
  }

  render() {
    return <section>
      <ul>
        {this.state.traces.map(item => this.renderListItem(item))}
      </ul>
    </section>
  }

  renderListItem(item) {
    return <li key={item.uuid}>
      {item.name}
    </li>
  }
}
