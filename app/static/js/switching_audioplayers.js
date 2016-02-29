var width = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var height = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;

// get the source for the audio (in 'audio_source_mp3', which is hidden),
// concatenate the bar player divs into one (with the audio source in the middle)
// pass it in the audio
var audiodoc_audio = document.getElementById("audio_source_mp3")
var switch_audioplayers = document.getElementById("switching_audioplayers");
var bar_player1 = '<audio controls id="author"><source src="';
var bar_player2 = '"type="audio/mpeg">Your browser does not support the audio element.</audio>';
var bar_player = bar_player1.concat(audiodoc_audio.innerHTML).concat(bar_player2);
switch_audioplayers.innerHTML = bar_player;
