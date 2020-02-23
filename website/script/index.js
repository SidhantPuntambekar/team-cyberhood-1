var addBtn = document.querySelector("#addbtn");
var scanBtn = document.querySelector("#scanbtn");
var anaBtn = document.querySelector("#anabtn");

addBtn.addEventListener("click", function () {
    alert("Device add button has been clicked!");
})

scanBtn.addEventListener("click", function () {
    alert("Scan button has been clicked!");
})

anaBtn.addEventListener("click", function () {
    alert("Analyze button has been clicked!");
})

function displayTable1() {
    var table1 = document.getElementById("table1");
    var table2 = document.getElementById("table2");
    //var table2 = document.getElementById("table2")
    //var table2 = document.getElementById("table2")
    table2.height = 0;
    table2.style.visibility = "hidden";
    table1.height = "480";
    table1.style.visibility = "visible";
    document.getElementById("table1").contentWindow.location.reload();
   
}

function displayTable2() {
    var table1 = document.getElementById("table1");
    var table2 = document.getElementById("table2");
    //var table2 = document.getElementById("table2")
    //var table2 = document.getElementById("table2")
    table1.height = 0;
    table1.style.visibility = "hidden";
    table2.height = "480";
    table2.style.visibility = "visible";
    document.getElementById("table2").contentWindow.location.reload();


}

function displayTable3() {

}

window.setInterval(function() {
            reloadIFrame()
        }, 3000);

 function reloadIFrame() {
            console.log('reloading..');
        }