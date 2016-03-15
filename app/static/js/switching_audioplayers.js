var width = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

// create js script for circular/bar playar
var head = document.getElementsByTagName('head')[0];
var js = document.createElement("script");
js.type = "text/javascript";
// js.src = "/static/js/audioplayer.js";
head.appendChild(js);


// get the source for the audio and TI_box (in 'audioplayer_source_mp3' and 'audioplayer_TI_box', which is hidden),
// build html for the players by concatenating the different sections
// pass it in the correct div (id="switching_audioplayers")
var audiodoc_audio = document.getElementById("audioplayer_source_mp3");
var switch_audioplayers = document.getElementById("switching_audioplayers");
var bar_player1 = '<audio controls id="author"><source src="';
var bar_player2 = '"type="audio/mpeg">Your browser does not support the audio element.</audio>';
var bar_player = bar_player1.concat(audiodoc_audio.innerHTML).concat(bar_player2);

var audiodoc_TI_box = document.getElementById("audioplayer_TI_box");
var cir_player1 = '<div id="circular_container"><canvas id="circular_progress" width="320" height="320"></canvas><div id="circular_player"><audio id="circular_audio"><source src="';
var cir_player2 = '" type="audio/mpeg" codecs="mp3"></source></audio><img src="';
var cir_player3 = '""><div class="circular_cover"><div class="circular_controls"><button id="play-pause" title="Play" onclick="togglePlayPause()"><i class="fa fa-play"></i></button><div id="remaining"></div></div></div></div></div>';
var cir_player = cir_player1.concat(audiodoc_audio.innerHTML).concat(cir_player2).concat(audiodoc_TI_box.innerHTML).concat(cir_player3);

// check width of screen and pass the correct player into the html
if (width < 768)
{
  switch_audioplayers.innerHTML = cir_player;
  js.src = "/static/js/circular_player.js";
}
else{
  switch_audioplayers.innerHTML = bar_player;
  js.src = "/static/js/audioplayer.min.js";
}
