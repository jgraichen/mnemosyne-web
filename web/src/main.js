import React from 'react'

import Toolbar from './components/toolbar'

import './main.sass'

export default class Main extends React.Component {
    render() {
        return (
            <div>
                <Toolbar />
                {this.props.children}
            </div>
        )
    }
}
