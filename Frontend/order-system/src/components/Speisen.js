import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import  './Speisen.css';
import Header from './Header';

class Speisen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            submenu: 'Pizza',
          };
    }



    render() {
        const {classes} = this.props
        return (
            <div>
                <Header headline={this.state.submenu}/>
                <Link to="/Warenkorb">
                    <button className={classes.test} >
                        test
                    </button>
                </Link>

            </div>
        );
    }
}
const styles = theme => ({
    test: {
      width: '100%',
      backgroundColor: 'blue'
    }
  });

  Speisen.propTypes = {
    classes: PropTypes.object,
}
export default withStyles(styles)(Speisen);