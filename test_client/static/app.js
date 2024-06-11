"use strict";

const outPutDiv = document.getElementById("output");

outPutDiv.addEventListener("dblclick", function handleClick(e) {
  console.log(e.target);
});
