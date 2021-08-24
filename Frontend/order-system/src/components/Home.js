import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import Header from './Header'

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
            <Header/>
            <div className={classes.container}>
            <Link to="/Products">
            <button className={classes.test}>
                Test
            </button>
            </Link>
            </div>
            </div>
        );
    }
}
const styles = theme => ({
    test: {
        backgroundColor: "red"
    },
    container: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "200px",
    }
  });

  Home.propTypes = {
    classes: PropTypes.object,
}

export default withStyles(styles)(Home);