import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import Header from './Header'

class Submenu extends Component {
    render() {
        return (
            <div>
                <Header headline="Speisen"/>
                <Link to="/Products" style={{ textDecoration: 'none' }}>
                    test
                </Link>
            </div>
        );
    }
}

export default Submenu;