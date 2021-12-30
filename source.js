var canv = document.getElementById("canvas");
canv.width = window.innerWidth*0.85;
canv.height = window.innerHeight*0.95;
ctx = canv.getContext("2d");
ctx.fillStyle="green";
ctx.fillRect(0,0,canv.width,canv.height)
var mydata = JSON.parse(ASS);
numberOfContestants = mydata.length

var scaleD = 0.9;
divisions = Math.floor(Math.sqrt(numberOfContestants))+1
// console.log(divisions,mydata[0].PROFILE PICTURE:,mydata)
console.log(mydata[0].PROFILEPICTURE)
var srt = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Chrome_icon_%28September_2014%29.svg/1200px-Google_Chrome_icon_%28September_2014%29.svg.png";

var imH = (canv.height/divisions)
var imW = (canv.width/divisions)
var images = [];
var i = 0;
// function grey(input) {
//             cnx.drawImage(myimage, 0 , 0);
//             var width = input.width;
//             var height = input.height;
//             var imgPixels = cnx.getImageData(0, 0, width, height);
//
//             for(var y = 0; y < height; y++){
//                 for(var x = 0; x < width; x++){
//                     var i = (y * 4) * width + x * 4;
//                     var avg = (imgPixels.data[i] + imgPixels.data[i + 1] + imgPixels.data[i + 2]) / 3;
//                     imgPixels.data[i] = avg;
//                     imgPixels.data[i + 1] = avg;
//                     imgPixels.data[i + 2] = avg;
//                 }
//             }
//
//             cnx.putImageData(imgPixels, 0, 0, 0, 0, imgPixels.width, imgPixels.height);
//         }
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


const interval = setInterval(function() {
   var dis = images.length
   var c = -1
   var j =0
   for (j=0;j<dis;j++){
     ind = j%divisions
     if(j%divisions==0){
       c += 1;
     }
     if(images[j].height <images[j].width) {
       var h2w = images[j].height/images[j].width
       // ctx.fillStyle = "black"
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
// img.src = '.png';
// for (i=0;i<numberOfContestants;i++){
//   num = numberOfContestants%divisions
//
// }
