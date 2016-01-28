var audio = document.getElementById('circular-audio');
var progress = document.getElementById('circular-progress');
var playpause = document.getElementById("play-pause");
var volume = document.getElementById("volume");

audio.controls = false;

audio.addEventListener('timeupdate', function() {
  	updateProgress();
}, false);

function togglePlayPause() {
   if (audio.paused || audio.ended) {
      playpause.title = "Pause";
      playpause.innerHTML = '<i class="fa fa-pause fa-3x"></i>';
      audio.play();
   } else {
      playpause.title = "Play";
      playpause.innerHTML = '<i class="fa fa-play fa-3x"></i>';
      audio.pause();
   }
}

function setVolume() {
   audio.volume = volume.value;
}

function updateProgress() {
	var percent = Math.floor((100 / audio.duration) * audio.currentTime);
	progress.value = percent;
	var canvas = document.getElementById('circular-progress');
	var context = canvas.getContext('2d');
	var centerX = canvas.width / 2;
	var centerY = canvas.height / 2;
	var radius = 150;
	var circ = Math.PI * 2;
	var quart = Math.PI / 2;
	var cpercent = percent / 100; /* current percent */
	context.beginPath();
	context.arc(centerX, centerY, radius, 0, ((circ) * cpercent), false);
	context.lineWidth = 10;
	context.strokeStyle = '#ffc21c';
	context.stroke();
	if (audio.ended) resetPlayer();
}

function resetPlayer() {
	  audio.currentTime = 0; context.clearRect(0,0,canvas.width,canvas.height);
  playpause.title = "Play";
	  playpause.innerHTML = '<i class="fa fa-play fa-3x"></i>';
}

// thx to: http://www.adobe.com/devnet/html5/articles/html5-multimedia-pt3.html

// Circular rotating music player with menu on back with html5 javascript and css3 is  MIT licensed:  http://opensource.org/licenses/MIT
// modified for Knowitwall 2016


function setLocation(){
    var percentage = 0.80;
    audio.currentTime = audio.duration * percentage;
}


// Circular rotating music player with menu on back with html5 javascript and css3 is  MIT licensed:  http://opensource.org/licenses/MIT
// modified for Knowitwall 2016


function setLocation(){
    var percentage = 0.80;
    audio.currentTime = audio.duration * percentage;
}
