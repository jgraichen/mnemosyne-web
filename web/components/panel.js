import React from 'react'
import styles from './panel.sass'

export class Panel extends React.Component {
  constructor(...args) {
    super(...args)
  }

  render() {
    let cn = styles.default

    if (this.props.raised) {
      cn = styles.raised
    }

    return <div className={cn}>
      {this.props.children}
    </div>
  }
}
