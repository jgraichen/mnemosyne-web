import React from 'react'
import { Link } from 'react-router'
import {Table, Column, Cell} from 'fixed-data-table-2';

require('fixed-data-table-2/dist/fixed-data-table.css');

import * as API from '../api';


const TextCell = ({rowIndex, data, col, ...props}) => (
  <Cell {...props}>
    {data[rowIndex][col]}
  </Cell>
);

const TimeCell = ({rowIndex, data, col, ...props}) => {
  var date = new Date( data[rowIndex][col]/1000); // start is in microseconds
  return (
    <Cell {...props}>
      {date.toUTCString()}
    </Cell>
  );
};

const MetaCell = ({rowIndex, data, col, ...props}) => {
  let stringValue = JSON.stringify(data[rowIndex][col]);
  return (
    <Cell {...props}>
      {stringValue}
    </Cell>
  );
};

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
    let {transactions} = this.state;

    function onRowSelect(event, rowId){
      let uuid = transactions[rowId]["uuid"];
      // TODO: Do this with router
      window.location.href= "/#/transactions/"+uuid;
    }



    // TODO: find a better way to scale the table. Also: re-render on window resize
    let width = window.innerWidth;
    let height = window.innerHeight-60; // window hight - navbar

    return <Table
      rowHeight={50}
      rowsCount={transactions.length}
      width={width}
      height={height}
      headerHeight={50}
      onRowClick={onRowSelect}>
      <Column
        header={<Cell>Transaction ID</Cell>}
        cell={<TextCell data={transactions} col="uuid" />}
        flexGrow={1}
        width={200}
      />
      <Column
        header={<Cell>Start</Cell>}
        cell={<TimeCell data={transactions} col="start" />}
        fixed={true}
        width={400}
      />
      <Column
        header={<Cell>Duration (in ms)</Cell>}
        cell={<TextCell data={transactions} col="duration" />}
        fixed={true}
        width={200}
      />
    </Table>
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
    let {transaction} = this.state;

    if (!transaction)
      return null

    function onRowSelect(event, rowId){
      let uuid = transaction.traces[rowId]["uuid"];
      // TODO: Do this with router
      window.location.href= "/#/traces/"+uuid;
    }

    // TODO: find a better way to scale the table. Also: re-render on window resize
    let width = window.innerWidth;
    let height = window.innerHeight-200; // window hight - navbar

    return (
      <section>
        <h2>Transaction <span>{transaction.uuid}</span></h2>

        <h3>Traces:</h3>
        <Table
        rowHeight={50}
        rowsCount={transaction.traces.length}
        width={width}
        height={height}
        headerHeight={50}
        onRowClick={onRowSelect}>
          <Column
            header={<Cell>Trace ID</Cell>}
            cell={<TextCell data={transaction.traces} col="uuid" />}
            flexGrow={1}
            width={200}
          />
          <Column
            header={<Cell>Name</Cell>}
            cell={<TextCell data={transaction.traces} col="name" />}
            fixed={true}
            width={200}
          />
          <Column
            header={<Cell>Start</Cell>}
            cell={<TimeCell data={transaction.traces} col="start" />}
            fixed={true}
            width={400}
          />
          <Column
            header={<Cell>Duration (in ms)</Cell>}
            cell={<TextCell data={transaction.traces} col="duration" />}
            fixed={true}
            width={200}
          />
          <Column
            header={<Cell>Meta</Cell>}
            cell={<MetaCell data={transaction.traces} col="meta" />}
            flexGrow={2}
            width={200}
          />
        </Table>
      </section>
    );
  }
}
