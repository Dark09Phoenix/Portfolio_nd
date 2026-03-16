const text = "Pentesting | Network Security | Cloud Security";

let index = 0;

function typing(){

document.querySelector(".typing").innerHTML =
text.slice(0,index++);

if(index <= text.length){

setTimeout(typing,80)

}

}

typing();