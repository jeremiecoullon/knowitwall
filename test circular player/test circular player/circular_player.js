
var audio = document.getElementById('audio');
var progress = document.getElementById('progress');
var playpause = document.getElementById("play-pause");
var volume = document.getElementById("volume");
var timeRemaining = document.getElementById("remaining");

//how far from 3 o'clock the progress bar starts, 0 - 2*pi
var progressOffsetRadians = 147 * (Math.PI / 180);
//the distance from the centre of the player to the middle of the progress bar
var progressRadius = 150;
//the thickness of the progress bar
var progressWidth = 10;
//how far from the middle of the progress bar a click 'on' the progress bar can be, and still control the progress - should be at least progressWidth
var progressClickWidth = 20;

audio.controls = false;

audio.addEventListener('timeupdate', function() {
  	updateProgress();
}, false);

document.getElementById('container').addEventListener('click', function(e){
	var player = document.getElementById('player'),
		//playerBounds is the rectangle encompassing the player
		playerBounds = player.getBoundingClientRect(),
		//xDistance is the distance on the x-axis of the click relative to the centre
		xDistance = e.x - (playerBounds.left + (player.offsetWidth / 2)),
		//yDistance is the same, but for the y-axis
		yDistance = e.y - (playerBounds.top + (player.offsetHeight / 2)),
		//distanceFromCentre is how far the click was from the centre of the player
		distanceFromCentre = Math.sqrt((xDistance * xDistance) + (yDistance * yDistance)),
		//we might use these later to work out the new progress percentage
		clickAngle,
		newProgressPercentage,
		//and here's a handy constant
		twoPi = 2 * Math.PI;
			
	//use distanceFromCentre to work out whether the progress bar was clicked - does it fall within the radius range?
	if(distanceFromCentre >= progressRadius - progressClickWidth && distanceFromCentre <= progressRadius + progressClickWidth){
		//note that although Math.atan2 is undefined for (0, 0) arguments, in practice the check above avoids that case given reasonable values
		clickAngle = Math.atan2(yDistance, xDistance);
		//account for the offset and make clickAngle positive - it currently ranges from -pi to pi, and progressOffsetRadians is at most twoPi, so we need to add twoPi twice before getting the remainder
		clickAngle = (clickAngle + twoPi + twoPi - progressOffsetRadians) % twoPi;
		//work out the percentage (0 to 1)
		newProgressPercentage = clickAngle / twoPi
		//probably over-cautious, but let's guard against rounding errors
		if(newProgressPercentage < 0) newProgressPercentage = 0;
		if(newProgressPercentage > 1) newProgressPercentage = 1;
		//and set the new progress
		audio.currentTime = audio.duration * newProgressPercentage;
	}		
});

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
	var canvas = document.getElementById('progress');
	var context = canvas.getContext('2d');
	var centerX = canvas.width / 2;
	var centerY = canvas.height / 2;
	var circ = Math.PI * 2;
	var quart = Math.PI / 2;
	var cpercent = percent / 100; /* current percent */
	var secondsLeft = audio.duration - audio.currentTime;
	
	//draw the clickable part of the progress bar
	context.beginPath();
	context.arc(centerX, centerY, progressRadius, 0, circ, false);
	context.lineWidth = progressClickWidth;
	context.strokeStyle = '#f60';
	context.stroke();
	
	//and draw the current progress
	context.beginPath();
	context.arc(centerX, centerY, progressRadius, progressOffsetRadians, progressOffsetRadians + ((circ) * cpercent), false);
	context.lineWidth = progressWidth;
	context.strokeStyle = '#ffc21c';
	context.stroke();
	
	//also update the time remaining (mm:ss)
	timeRemaining.innerHTML = NumString(Math.floor(secondsLeft/60), 2) + ':' + NumString(Math.floor(secondsLeft % 60), 2);
	
	if (audio.ended) resetPlayer();
}

//returns the provided number, padded with leading zeroes if necessary to make the required length
function NumString(num, minLength){
	var str = num + '';
	while(str.length < minLength){
		str = '0' + str;
	}
	return str;
}

function resetPlayer() {
	  audio.currentTime = 0; context.clearRect(0,0,canvas.width,canvas.height);
  playpause.title = "Play";
	  playpause.innerHTML = '<i class="fa fa-play fa-3x"></i>';
}

// thx to: http://www.adobe.com/devnet/html5/articles/html5-multimedia-pt3.html

// Circular rotating music player with menu on back with html5 javascript and css3 is  MIT licensed:  http://opensource.org/licenses/MIT

// modified for Knowitwall 2016