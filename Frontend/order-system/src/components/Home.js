import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import Header from './Header'
import Pizzaimg from '../images/pizza_logo.jpg'
import Drinkimg from '../images/drink_logo.jpg'
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
            <Header/>
            <div className={classes.container}>
             </div>
             
            <div class='containerSpeisen'>
             <Link to="/Warenkorb">
                </Link>
                 <button> <img class='Pizzaimage' src={Pizzaimg}></img></button>
                  <div class='Speisentext'>Speisen</div>
                </div>


            <div class='containerGetränk'>
                 <img class='Drinkimage' src={Drinkimg} ></img>
                 <div class='Getränke'>Getränke</div>
             </div>
            <div class='containerDessert'>
                 <img class='Dessertimage' src={Dessertimg} ></img>
                 <div class='Desserts'>Desserts</div>
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