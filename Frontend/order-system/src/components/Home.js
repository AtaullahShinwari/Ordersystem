import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import Header from './Header'
import Pizzaimg from '../images/pizza_logo.jpg'
import Drinkimg from '../images/drink_logo.PNG'
import Dessertimg from '../images/dessert_logo.jpeg'
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
             <Header headline="McDonalds's"/>
              <div class="containerMenu">
                <div class='containerSpeisen'>

                 <Link to="/Submenu" style={{ textDecoration: 'none' }}>
                    <img class='Pizzaimage' src={Pizzaimg}></img>
                    <div class='Speisentext'>Speisen</div>
                </Link>
                </div>
                <div class='containerGetränk'>
                 <Link to="/Drinks" style={{ textDecoration: 'none' }}>
                    <img class='Drinkimage' src={Drinkimg}></img> 
                    <div class='Drinktext'>Getränke</div>
                </Link>
                </div>
                <div class='containerDessert'>
                 <Link to="/Desserts" style={{ textDecoration: 'none' }}>
                    <img class='Dessertimage' src={Dessertimg} ></img>
                    <div class='Desserttext'>Desserts</div>
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

  Home.propTypes = {
    classes: PropTypes.object,
}

export default withStyles(styles)(Home);