import React, { Component } from 'react';
import './Footer.css'
import {Link} from 'react-router-dom'
import logo from "../images/Mcdonalds-Logo-Transparent.png"
import LocalBarSharpIcon from '@material-ui/icons/LocalBarSharp';
import {withStyles, Button} from '@material-ui/core';
import PropTypes from 'prop-types'
import LocalPizzaSharpIcon from '@material-ui/icons/LocalPizzaSharp';
import CakeSharpIcon from '@material-ui/icons/CakeSharp';

class Footer extends Component {
    
    render() {
        const {classes} = this.props
        return (
            <div>
                <div class="footer">
                <Link to="/" style={{ textDecoration: 'none' }}>
                </Link>

                <div class='SpeisenClass'>
                <Link to="/Speisen" style={{ textDecoration: 'none' }}>
                    <Button class='SpeisenIcon' src={LocalPizzaSharpIcon}></Button>
                </Link>
                </div>
                <div class='DrinksClass'>
                 <Link to="/Drinks" style={{ textDecoration: 'none' }}>
                    <Button class='DrinksIcon' src={LocalBarSharpIcon}></Button> 
                </Link>
                </div>

                <div class='DessertsClass'>
                 <Link to="/Desserts" style={{ textDecoration: 'none' }}>
                    <Button class='DessertsIcon' src={CakeSharpIcon} ></Button>
                </Link>
                </div>
            </div>
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

  Footer.propTypes = {
    classes: PropTypes.object,
}
export default withStyles(styles)(Footer);