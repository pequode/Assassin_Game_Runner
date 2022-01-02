var canv = document.getElementById("canvas");
canv.width = window.innerWidth*0.85;
canv.height = window.innerHeight*0.95;
ctx = canv.getContext("2d");
ctx.fillStyle="green";
ctx.fillRect(0,0,canv.width,canv.height)
var mydata = JSON.parse(ASS);
numberOfContestants = mydata.length
// spaccing parameters for drawing
var scaleD = 0.9;
divisions = Math.floor(Math.sqrt(numberOfContestants))+1

// determine each images size
var imH = (canv.height/divisions)
var imW = (canv.width/divisions)
var images = [];
var i = 0;

// pre-loads all images into objects
for(i=0;i<numberOfContestants;i++)
{
  var string = mydata[i].EMAIL;
  string = "./images/"+string.substring(0,string.indexOf("@"))+".jpg";
  console.log(string);
  img = new Image();
  img.src =string;
  console.log(img)
  images.push(img)
}

// draws in a loop to allow a future clickable interface. 
const interval = setInterval(function() {
   var dis = images.length
   var c = -1
   var j =0
   // loop through all contestants and draw names to a grid
   for (j=0;j<dis;j++){
     ind = j%divisions
     if(j%divisions==0){
       c += 1;
     }
     if(images[j].height <images[j].width) {// draw each image with the smallest dim
       var h2w = images[j].height/images[j].width
       // ctx.fillStyle = "black" // add a boader
       // ctx.fillRect(ind*imW,c*imH,imW,imH*h2w)
       ctx.drawImage(images[j],ind*imW+imW*0.1,c*imH+imH*0.1,imW*0.8,imH*0.8*h2w);
     }
     else{
       var h2w = images[j].width/images[j].height
       ctx.fillStyle = "black"
       // ctx.fillRect(ind*imW,c*imH,imW,imH*h2w)
       ctx.drawImage(images[j],ind*imW+imW*0.1,c*imH+imH*0.1,imW*0.8*h2w,imH*0.8);
     }


     ctx.fillStyle = "White";
     ctx.font = "18px Arial Bold";
     ctx.fillText(mydata[j].NAME,(ind)*imW,(c+1)*imH);


   }
 }, 1000);
