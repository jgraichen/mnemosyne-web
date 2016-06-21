import React from 'react'
import { Link } from 'react-router'
import styles from './toolbar.sass'

export default class Toolbar extends React.Component {
    constructor(...args) {
        super(...args)
    }

    render() {
        return (
            <nav className={styles.toolbar}>
                <h1>
                    <Link to="/">Mnemosyne</Link>
                </h1>
                <ul>
                    <li><Link to="/applications">Applications</Link></li>
                    <li><Link to="/transactions">Transactions</Link></li>
                    <li><Link to="/traces">Traces</Link></li>
                </ul>
            </nav>
        )
    }
}
