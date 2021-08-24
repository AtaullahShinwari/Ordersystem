import React, { Component } from 'react';
import './Header.css'
import logo from "../images/McDonald's_Golden_Arches.svg.png"
class Header extends Component {
    render() {
        return (
            <div>
                <div class="LogoText">
                <img src={logo} class="logoimg"></img>
                <h6 class= "HeaderText">McDonalds</h6>
                </div>
            </div>
        );
    }
}

export default Header;