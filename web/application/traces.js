import React from 'react'

import { Panel } from '../components/panel'
import {Chart} from 'react-google-charts'
import * as API from '../api'

export class Show extends React.Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  componentWillMount() {
    API.getTrace(this.props.params.id).then(async json => {
      this.setState({trace: json});
    })
  }

  render() {

    let {trace} = this.state;

    if (!trace)
      return null

    let options = {
      hAxis: {
        format: 'HH:mm:ss',
      }
    }

    var columns = [
      {
          type: 'string',
          id: 'Service'
      },
      {
          type: 'date',
          id: 'Start'
      },
      {
          type: 'date',
          id: 'End'
      }
    ];

    let rows = trace.spans.map(function(span){
        return [ span.name, new Date(span.start/1000), new Date(span.stop/1000) ]
    });

    let height = window.innerHeight-200;

    return (
      <section>
        <h2>Trace <span>{trace.name}</span></h2>

        <h3>Spans:</h3>

        <Chart
          chartPackages={['timeline']}
          chartType = "Timeline"
          rows = {rows}
          columns={columns}
          options = {options}
          graph_id = "TimelineChart"
          width={"100%"}
          height={height} />

      </section>
    );
  }
}
