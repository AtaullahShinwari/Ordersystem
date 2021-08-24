import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'

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
            <Link to="/Products">
            <button className={classes.test}>
                Test
            </button>
            </Link>
            </div>
        );
    }
}
const styles = theme => ({
    test: {
      width: '100%',
      backgroundColor: 'red'
    }
  });

  Home.propTypes = {
    classes: PropTypes.object,
}

export default withStyles(styles)(Home);