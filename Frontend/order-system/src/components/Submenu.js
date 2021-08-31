import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import Header from './Header'
import Pizzaimg from '../images/pizza_logo.jpg'
import Pastaimg from '../images/pasta_logo.jpg'
import Dessertimg from '../images/dessert_logo.jpeg'
import './Submenu.css'

class Submenu extends Component {
    render() {
        return (
            <div>
                <Header headline="Speisen"/>
                <div class="containerSpeisenS">
                <div class='containerPizzaS'>
                 <Link to="/Speisen" style={{ textDecoration: 'none' }}>
                    <img class='Pizzaimage' src={Pizzaimg}></img>
                    <div class='Pizzatext'>Pizza</div>
                </Link>
                </div>
                <div class='containerPasta'>
                 <Link to="/Pasta" style={{ textDecoration: 'none' }}>
                    <img class='Pastaimage' src={Pastaimg}></img> 
                    <div class='Pastatext'>Pasta</div>
                </Link>
                </div>
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

  Submenu.propTypes = {
    classes: PropTypes.object,
}

export default withStyles(styles)(Submenu);