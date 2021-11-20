var count = 3;
var countElement = document.querySelector("#count");

console.log(countElement);

function add1() {
    count++;
    countElement.innerText = "hey";
}