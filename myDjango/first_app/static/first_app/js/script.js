
var header = document.querySelector("h1")


header.style.color = 'red'


function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];
  }
  return color
}

 function bick(){
	colorInput=getRandomColor()
	header.style.color=colorInput
}

setInterval("bick()",500);

//Triggering an event
var para=document.querySelector("#duy")
var para1=document.querySelector("#duyy")
var para2=document.querySelector("#duyyy")


para.addEventListener("mouseover",function(){
	para.textContent="OOOOPSSS! I forgot to include Dalgona!!";
	para.style.color="red";
})

para.addEventListener("mouseout",function(){
	para.textContent="Welcome to my Bootstrap Project: Coffee Lover";
	para.style.color="black";
})


para1.addEventListener("click",function(){
	para1.textContent="Next Time I will choose Jilipee!! YUMMMMMMMMMYYYYYYYYYYYY!!!!!"
	para1.style.color="blue"
})
para2.addEventListener("dblclick",function(){
	para2.textContent="Just Kidding DUHH!!"
	para2.style.color="magenta"
})