var body = document.querySelector('body')
var button = document.querySelector('button')
function getRandomColor(){
  var letters = '0123456789ABCDEF';
  var color = '#'
  for (var i =0;i<6;i++){
    var r = Math.floor(Math.random()*16);
    color = color + letters[r]
  }
  return color
}
function changeColor(){
  var rc = getRandomColor()
  body.style.background = rc
  hr.style.background = rc
  button.style.background = rc
}
setInterval(changeColor,1000)
button.addEventListener('mouseover',changeColor)
