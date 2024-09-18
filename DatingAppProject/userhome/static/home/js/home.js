//story section
let currentScrollPosition = 0;
let scrollAmount = 320;
const sCont = document.querySelector(".story-container");
const hScroll = document.querySelector(".horizontal-scroll");
const btnScrollLeft = document.querySelector("#btn-scroll-left");
const btnScrollRight = document.querySelector("#btn-scroll-right");
btnScrollLeft.style.opacity = 0;
// alert("sCont.offsetWidth:=",sCont.offsetWidth);
// alert("hScroll.offsetWidth:=",hScroll.offsetWidth);
let maxScroll = -sCont.offsetWidth + hScroll.offsetWidth; //-612

function scrollHorizontally(val){
  currentScrollPosition += (val * scrollAmount);
  
  sCont.style.left = currentScrollPosition + "px";//-320
  // alert(currentScrollPosition);
  // alert(sCont.style.left );//-612
  // alert(maxScroll);

  if(currentScrollPosition >= 0){
    currentScrollPosition = 0;
    btnScrollLeft.style.opacity = 0;
  }else{
    btnScrollLeft.style.opacity = 1;
  }

  if(currentScrollPosition <= maxScroll){
    currentScrollPosition = maxScroll;
    btnScrollRight.style.opacity = 0;
  }else{
    btnScrollRight.style.opacity = 1;
  }
}