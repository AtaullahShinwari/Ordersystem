import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import Pizzaimg from '../images/pizza_logo.jpg'
import Drinkimg from '../images/drink_logo.jpg'
import Dessertimg from '../images/dessert_logo.jpeg'
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
                </Link>
                <div class='containerSpeisenP'>
                 <Link to="/Speisen" style={{ textDecoration: 'none' }}>
                    <img class='PizzaimageP' src={Pizzaimg}></img>
                    <div class='SpeisentextP'>Speisen</div>
                </Link>
                </div>
                <div class='containerGetränkP'>
                 <Link to="/Drinks" style={{ textDecoration: 'none' }}>
                    <img class='DrinkimageP' src={Drinkimg}></img> 
                    <div class='DrinktextP'>Getränke</div>
                </Link>
                </div>
                <div class='containerDessertP'>
                 <Link to="/Desserts" style={{ textDecoration: 'none' }}>
                    <img class='DessertimageP' src={Dessertimg} ></img>
                    <div class='DesserttextP'>Desserts</div>
                </Link>
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

  Speisen.propTypes = {
    classes: PropTypes.object,
}
export default withStyles(styles)(Speisen);