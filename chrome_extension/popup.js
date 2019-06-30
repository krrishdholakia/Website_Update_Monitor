let hitBtn = document.getElementById('hitBtn');
console.log("button clicked!");
hitBtn.onclick = function(element) {
  const socket = io("http://localhost:8080");
  console.log("button clicked!");
    socket.emit("message", "HELLO WORLD from extension");
    socket.on("message", function(data) {
    console.log(data);
    });
  setInterval(function() {
    console.log("button clicked!");
    socket.emit("message", "HELLO WORLD from extension");
    socket.on("message", function(data) {
    console.log(data);
    });
  }, 70000)
  
};
