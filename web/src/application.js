import React from 'react'
import Toolbar from './components/toolbar'
import './application.sass'

export default class Application extends React.Component {
    render() {
        return (
            <div>
                <Toolbar />
            </div>
        )
    }
}
