import React from "react";
import ArrowBackIosIcon from '@material-ui/icons/ArrowBackIos';
import { VisibilityContext } from "react-horizontal-scrolling-menu";
import ArrowForwardIosIcon from '@material-ui/icons/ArrowForwardIos';

function Arrow({
  children,
  disabled,
  onClick
}: {
  children: React.ReactNode;
  disabled: boolean;
  onClick: VoidFunction;
}) {
  return (
    <button
      disabled={disabled}
      onClick={onClick}
      style={{
        cursor: "pointer",
        textDecoration: "none",
        userSelect: "none"
      }}
    >
      {children}
    </button>
  );
}

export function LeftArrow() {
  const {
    isFirstItemVisible,
    scrollPrev,
    visibleItemsWithoutSeparators
  } = React.useContext(VisibilityContext);


  return (
    <Arrow  onClick={() => scrollPrev()}>
      <ArrowBackIosIcon></ArrowBackIosIcon>
    </Arrow>
  );
}

export function RightArrow() {
  const {
    isLastItemVisible,
    scrollNext,
    visibleItemsWithoutSeparators
  } = React.useContext(VisibilityContext);



  return (
    <Arrow onClick={() => scrollNext()}>
      <ArrowForwardIosIcon></ArrowForwardIosIcon>
    </Arrow>
  );
}
