import React from "react";
import './Button.css';
import './Home.css'
import { VisibilityContext } from "react-horizontal-scrolling-menu";
import {Link} from 'react-router-dom'
export function Button({ itemId, Buttontext }: { itemId: string; Buttontext: string }) {
  const visibility = React.useContext(VisibilityContext);

  const visible = visibility.isItemVisible(itemId);
  return (
    <div
      role="button"
      tabIndex={0}
      className="containerMenu"
    >
                <div class='containerSubmenu'>
                 <Link to="/Submenu" style={{ textDecoration: 'none' }}>
                    <div class='Submenutext'>{Buttontext}</div>
                </Link>
                </div>
    </div>
  );
}
