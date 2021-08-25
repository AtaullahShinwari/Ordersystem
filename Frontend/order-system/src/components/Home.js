import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import Header from './Header'
import speisen from '../images/speisen.jpg'
import './Home.css'

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {

          };
    }
    render() {
        const {classes} = this.props
        return (
            <div>
                <Header headline="McDonald's"/>
                    <div class="menuContainer">
                    <Link to="/Submenu">
                        <div class="speisen">
                            <img class="menuimg"src={speisen}></img>
                            <div class="menuname"></div>
                        </div>
                    </Link>
                    </div>
                </div>
        );
    }
}
const styles = theme => ({
    test: {
        backgroundColor: "red"
    }
  });

  Home.propTypes = {
    classes: PropTypes.object,
}

export default withStyles(styles)(Home);