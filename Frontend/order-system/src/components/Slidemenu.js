import React, { Component } from 'react';
import ReactDOM from "react-dom";
import { ScrollMenu, VisibilityContext } from "react-horizontal-scrolling-menu";
import Pizzaimg from '../images/pizza_logo.jpg'
import Drinkimg from '../images/drink_logo.PNG'
import Dessertimg from '../images/dessert_logo.jpeg'
import { LeftArrow, RightArrow } from "./arrows";
import { Card } from "./card";
import Header from './Header'
import { Button } from './Button';


// NOTE: embrace power of CSS flexbox!
// import "./arrowsOnBottomOrTop.css";
// import "./hideScrollbar.css";
// import "./firstItemMargin.css";

class Slidemenu extends Component {
    constructor(props) {
        super(props);
        this.state = {
  
          };
    }
    render() {
type scrollVisibilityApiType = React.ContextType<typeof VisibilityContext>;

const elemPrefix = "Slidemenu";
const getId = (index: number) => `${elemPrefix}${index}`;

  let items = [
      {
          id: 0,
          text: 'Pizza'
      },
      {
        id: 1,
        text: 'Pasta'
    },
    {
        id: 2,
        text: 'Sushi'
    },
    {
        id: 2,
        text: 'Sushi1'
    },
    {
        id: 2,
        text: 'Sushi2'
    },
    {
        id: 2,
        text: 'Sushi3'
    }
  ];

  return (

    <> 
      
        <div>
          <ScrollMenu
            LeftArrow={LeftArrow}
            RightArrow={RightArrow}
          >
            {items.map(item => (
              <Button
                Buttontext={item.text} // NOTE: itemId is required for track items
                key={item.id}
                itemId={item.id}
              />
            ))}
          </ScrollMenu>
        </div>
      
    </>
  );
}
    }
export default Slidemenu;
