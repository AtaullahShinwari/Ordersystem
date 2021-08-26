import React from "react";

import './Home.css'
import { VisibilityContext } from "react-horizontal-scrolling-menu";
import {Link} from 'react-router-dom'
export function Card({ itemId, cardimage, cardtext }: { itemId: string; cardimage: string; cardtext: string }) {
  const visibility = React.useContext(VisibilityContext);

  const visible = visibility.isItemVisible(itemId);
  return (
    <div
      role="button"
      tabIndex={0}
      className="containerMenu"
    >
                <div class='containerSpeisen'>
                 <Link to="/Submenu" style={{ textDecoration: 'none' }}>
                    <img class='Pizzaimage' src={cardimage}></img>
                    <div class='Speisentext'>{cardtext}</div>
                </Link>
                </div>
                {console.log(cardimage)}

    </div>
  );
}
