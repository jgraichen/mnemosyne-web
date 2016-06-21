import React from 'react'
import styles from './grid.sass'

export default class Grid extends React.Component {
  constructor(...args) {
    super(...args)
  }

  render() {
    return <div className={styles.grid}>
      {this.props.children}
    </div>
  }
}
