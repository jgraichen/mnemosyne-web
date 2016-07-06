import React from 'react'

import { TimeSeries, TimeRange } from "pondjs"
import { Charts, ChartContainer, ChartRow, YAxis, LineChart } from "react-timeseries-charts"

import { Panel } from '../components/panel'

import * as API from '../api'

import styles from './dashboard.sass'

export class Dashboard extends React.Component {
  render() {
    return <Panel>
      <div className={styles.dashboard}>
        <div>
          <ResponseTimePanel title="Xikolo/Web/Application" />
        </div>
        <div>
          <ErrorRatePanel title="Xikolo/Web/Application" />
        </div>
      </div>
    </Panel>
  }
}

export class ResponseTimePanel extends React.Component {
  render() {
    return <Panel raised={true}>
      <div className={styles.appOverview}>
        <h2>Response Times</h2>
        <ResponseTimeChart />
      </div>
    </Panel>
  }
}

export class ErrorRatePanel extends React.Component {
  render() {
    return <Panel raised={true}>
      <div className={styles.appOverview}>
        <h2>Error rate</h2>
      </div>
    </Panel>
  }
}

export class ResponseTimeChart extends React.Component {
  constructor(...args) {
    super(...args)

    let series = new TimeSeries({
      name: "axis1",
      columns: ["time", "value"],
      points: [
        [1400425947000, 5.2],
        [1400425948000, 1.8],
        [1400425949000, 2.6],
        [1400425950000, 9.3],
        [1400425951000, 9.3],
        [1400425952000, 9.3],
        [1400425953000, 9.3],
      ]
    })

    this.state = {
      series: series
    }
  }

  componentWillMount() {
    API.getTransactions().then(async json => {
      this._update(json)
    })
  }

  _update(json) {
    let data = []

    for(let t of json) {
      let point = [t.start / 1000, t.duration / 1000]
      data.push(point)
    }

    let series = {
      columns: ["time", "value"],
      points: data
    }

    this.setState({
      series: new TimeSeries(series)
    })
  }

  render() {
    let series = this.state.series



    return <section>
      <ChartContainer timeRange={series.timerange()}>
        <ChartRow height="160">
          <YAxis label="ms" id="resptime" min={0} max={1200} format=",.0f"/>
          <Charts>
            <LineChart axis="resptime" series={series} />
          </Charts>
        </ChartRow>
      </ChartContainer>
    </section>
  }
}
