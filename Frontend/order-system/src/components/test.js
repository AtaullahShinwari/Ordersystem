import React, { Component } from 'react';
import ReactDOM from "react-dom";
import { ScrollMenu, VisibilityContext } from "react-horizontal-scrolling-menu";
import Pizzaimg from '../images/pizza_logo.jpg'
import Drinkimg from '../images/drink_logo.PNG'
import Dessertimg from '../images/dessert_logo.jpeg'
import { LeftArrow, RightArrow } from "./arrows";
import { Card } from "./card";
import Header from './Header'


// NOTE: embrace power of CSS flexbox!
// import "./arrowsOnBottomOrTop.css";
// import "./hideScrollbar.css";
// import "./firstItemMargin.css";

class Tst extends Component {
  constructor(props) {
      super(props);
      this.state = {

        };
  }



  render() {
type scrollVisibilityApiType = React.ContextType<typeof VisibilityContext>;

const elemPrefix = "test";
const getId = (index: number) => `${elemPrefix}${index}`;
 let items = [
      {
          id: 0,
          image: Pizzaimg,
          text: 'Speisen'
      },
      {
        id: 1,
        image:Drinkimg,
        text: 'Getränke'
    },
    {
        id: 2,
        image: Dessertimg,
        text: 'Desserts'
    }
  ];

  return (

    <> <Header headline="McDonalds's"/>
      <div className="example" style={{ paddingTop: "100px" }}>
        <div>
          <ScrollMenu
            LeftArrow={LeftArrow}
            RightArrow={RightArrow}
          >
            {items.map(item => (
              <Card
                cardimage={item.image}
                cardtext={item.text} // NOTE: itemId is required for track items
                key={item.id}
                itemId={item.id}
              />
            ))}
          </ScrollMenu>
        </div>
      </div>
    </>
  );
}
}
export default Tst;
