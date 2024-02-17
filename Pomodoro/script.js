var crsr = document.querySelector(".cursor");
var title = document.querySelector('#heading');
const timerText = document.getElementById('timer-text');
const startButton = document.getElementById('start-button');

function mousefollower() {
  document.addEventListener("mousemove", function(dets){
    // crsr.style.left = dets.x - (parseInt(crsr.style.width) / 2) + "px";
    crsr.style.left = dets.x - 25 + "px";
    // crsr.style.top = dets.y - (parseInt(crsr.style.height) / 2) + "px"; 
    crsr.style.top = dets.y - 25 + "px"; 
  });
}

// function cursorenlarge(){
//   title.addEventListener('mouseover', function() {
//     crsr.style.width = "100px";
//     crsr.style.height = "100px";

//     setTimeout(function() {
//       crsr.style.width = "30px";
//       crsr.style.height = "30px";
//     }, 1000);
//   });
// }

let timer;
let timeInSeconds = 25 * 60;

// Function to update the timer text
function updateTimerText() {
  const minutes = Math.floor(timeInSeconds / 60).toString().padStart(2, '0');
  const seconds = (timeInSeconds % 60).toString().padStart(2, '0');
  timerText.textContent = `${minutes}:${seconds}`;
}

function updateSessionCountText() {
  sessionCountDisplay.textContent = sessionCount;
}

function startTimer() {
  timer = setInterval(function() {
    timeInSeconds--;
    if (timeInSeconds <= 0) {
      timeInSeconds = 5 * 60;
      timer = null;
      incrementSessionCount();
    }
    updateTimerText();
  }, 1000);
  updateStartButtonText(true);
}

function pauseTimer() {
  clearInterval(timer);
  timer = null;
  updateStartButtonText(false);
}

function toggleTimer() {
  if (!timer) {
    startTimer();
  } else {
    pauseTimer();
  }
}

function updateStartButtonText(running) {
  startButton.textContent = running ? 'Resume' : 'Start';
}

function incrementSessionCount() {
  sessionCount++;
  updateSessionCountText();
}

startButton.addEventListener('click', function() {
  toggleTimer();
  incrementSessionCount();
});

document.getElementById('reset-button').addEventListener('click', function() {
  clearInterval(timer);
  timer = null;
  timeInSeconds = 25 * 60;
  updateTimerText();
  updateStartButtonText(false);
});


mousefollower();
cursorenlarge();
startrestart();
