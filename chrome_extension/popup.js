let hitBtn = document.getElementById('hitBtn');
console.log("button clicked!");

var port = chrome.extension.connect({
  name: "Sample Communication"
});
port.postMessage("Hi BackGround");
port.onMessage.addListener(function(msg) {
  // for (let value in Object.keys(msg)) {
  //   console.log("counting: " + value);
  // }
  console.log(msg[0]);
  chrome.browserAction.setBadgeText({text: "1+"});
  var today = new Date();
  var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
  document.getElementById("hitBtn").innerHTML = msg
  document.getElementById("further_information").innerHTML = "value last updated at: " + time; 

});

// hitBtn.onclick = function(element) {
//   const socket = io("http://localhost:8080");
//   console.log("button clicked!");
//   initial_run = true
//   while (initial_run) {
//     socket.emit("message", "HELLO WORLD from extension");
//     socket.on("message", function(data) {
//     var today = new Date();
//     var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
//     console.log(data);
//     document.getElementById("hitBtn").innerHTML = data
//     document.getElementById("further_information").innerHTML = "value last updated at: " + time; 
//     chrome.browserAction.setBadgeText({text: "10+"});
//     });
//     initial_run = false
//   }
  
// };
