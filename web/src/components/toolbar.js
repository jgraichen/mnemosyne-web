import React from 'react'
import styles from './toolbar.sass'

export default class Toolbar extends React.Component {
    constructor(...args) {
        super(...args)
    }

    render() {
        return (
            <nav className={styles.toolbar}>
                <h1>Mnemosyne</h1>
            </nav>
        )
    }
}
