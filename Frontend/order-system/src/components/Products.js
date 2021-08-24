import React, { Component } from 'react';
import {Link} from 'react-router-dom'
import {withStyles} from '@material-ui/core';
import PropTypes from 'prop-types'
import  './Products.css';

class Products extends Component {
    constructor(props) {
        super(props);
        this.state = {
            testStatus: false,
          };
    }

test = () => {
console.log('Erfolgreich')
}

    render() {
        const {classes} = this.props
        return (
            <div>
                {console.log(this.state.testStatus)}
                <Link to="/Warenkorb">
                    <button className={classes.test} onClick={this.test()}>
                        test
                    </button>
                </Link>
                <div class="body">
                    sadsad
                </div>
            </div>
        );
    }
}
const styles = theme => ({
    test: {
      width: '100%',
      backgroundColor: 'blue'
    },
    test2: {
        backgroundColor: 'red'
    }
  });

  Products.propTypes = {
    classes: PropTypes.object,
}
export default withStyles(styles)(Products);