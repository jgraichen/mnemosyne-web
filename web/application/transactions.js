import React from 'react'
import { Link } from 'react-router'
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table';

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

    function onRowSelect(row, isSelected){
      // TODO: Do this with router
      window.location.href= "/#/transactions/"+row.uuid;
    }

    var selectRowProp = {
      mode: "radio",
      clickToSelect: true,
      hideSelectColumn: true,
      onSelect: onRowSelect
    };

    function dateFormatter(value, row, formatExtraData){
      var date = new Date(value/1000); // start is in microseconds
      return date.toUTCString();
    }

    return <BootstrapTable data={this.state.transactions} striped={true} hover={true} pagination={true} search={true} selectRow={selectRowProp}>
        <TableHeaderColumn dataField="uuid" isKey={true} dataAlign="left" dataSort={true}>Transaction ID</TableHeaderColumn>
        <TableHeaderColumn dataField="start" dataAlign="left" dataSort={true} dataFormat={dateFormatter}>Start</TableHeaderColumn>
        <TableHeaderColumn dataField="duration" dataAlign="left" dataSort={true}>Duration</TableHeaderColumn>
    </BootstrapTable>
  }
}

export class Show extends React.Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  componentWillMount() {
    API.getTransaction(this.props.params.id).then(async json => {
      this.setState({transaction: json});
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
