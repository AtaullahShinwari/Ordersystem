import React, { Component } from 'react';
import './Header.css'
import {Link} from 'react-router-dom'
import logo from "../images/Mcdonalds-Logo-Transparent.png"
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import {withStyles, IconButton, Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions} from '@material-ui/core';
import PropTypes from 'prop-types'
import CloseIcon from '@material-ui/icons/Close';
class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showCart: false,
          };
    }


    showCart = () =>{
        this.setState({
            showCart: true,
        })
    }
    closeCart = () =>{
        this.setState({
            showCart: false,
        })
    }
    render() {
        const {classes} = this.props
        return (
            <div>
                {console.log(this.state.showCart)}
                <div class="header">
                <Link to="/" style={{ textDecoration: 'none' }}>
                <img src={logo} class="logoimg"></img>
                </Link>
                <Link to="/" style={{ textDecoration: 'none' }}>
                <h6 class= "HeaderText">{this.props.headline}</h6>
                </Link>
                <div class="Cart">
                    <IconButton onClick={this.showCart}>
                    <ShoppingCartIcon className={classes.carticon} ></ShoppingCartIcon>
                    </IconButton>
                </div>
                </div>
            <div>
                {this.state.showCart ?
                <Dialog className={classes.dialog} open={this.state.showCart} onClose={this.closeCart} maxWidth='xs'>
                    <DialogTitle>
                        Warenkorb
                        <IconButton onClick={this.closeCart}>
                            <CloseIcon></CloseIcon>
                        </IconButton>
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText>test test test</DialogContentText>
                    </DialogContent>
                </Dialog>
                :null}
            </div>
            </div>
        );
    }
}
const styles = theme => ({
    carticon: {
        width: "1.5em",
        height: "auto",
        color: "#FCC42F",
    },
    dialog: {
        backgroundColor: "transparent",
    boxShadow: "none",
    overflow: "hidden"
    }
  });

  Header.propTypes = {
    classes: PropTypes.object,
    headline: PropTypes.string,
}
export default withStyles(styles)(Header);