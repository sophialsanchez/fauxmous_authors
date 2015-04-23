var cur_position = 0;
var typing_speed = 3;
window.addEventListener("keypress", showBook, false);
	
// shows the book text, displaying three characters with every keypress
function showBook(key){
	var br = new RegExp("\n", "g"); // creates regex for newline
	var quote = new RegExp("/&quot", "g"); // creates regex for quote
	var next_typing_slice = book.slice(0, cur_position + typing_speed).replace(br,"<br/>").replace(quote,"\"");
	document.getElementById("text-space").innerHTML = next_typing_slice;
	cur_position = cur_position + typing_speed;
	adjustScreen();
}
	
//  scrolls window to the bottom when text expands beyond the window
function adjustScreen(){
	if(document.getElementsByClassName('book-container')[0].clientHeight-24 > window.innerHeight){
		window.scrollTo(0,document.body.scrollHeight);
	}
}

// shows the Facebook like button
function Like(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.3";
  fjs.parentNode.insertBefore(js, fjs);
}

// shows the Twitter button
function Tweet(d,s,id){
	var js,fjs=d.getElementsByTagName(s)[0],t=window.twttr||{};
	if(d.getElementById(id))return t;
	js=d.createElement(s);
	js.id=id;
	js.src="https://platform.twitter.com/widgets.js";
	fjs.parentNode.insertBefore(js,fjs);
	t._e=[];
	t.ready=function(f){t._e.push(f);};
	return t;
}