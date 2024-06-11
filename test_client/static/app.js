"use strict";

const outPutDiv = document.getElementById("output");

outPutDiv.addEventListener("dblclick", function handleClick(e) {
  console.log(e.target);
  if (e.target.tagName === "SPAN") {
    console.log("span");
    e.target.style.backgroundColor = "yellow";
    e.target.className = "highlighted";
  }
});
