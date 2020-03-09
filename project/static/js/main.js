// toggle menu
let mainNav = document.getElementById('js-menu');
let navBarToggle = document.getElementById('js-navbar-toggle');

navBarToggle.addEventListener('click', function () {
	mainNav.classList.toggle('active');
});


// placeholders
if(document.getElementsByName("username")[0] !== undefined) {
	document.getElementsByName("username")[0].placeholder = "Username"
}
if(document.getElementsByName("name")[0] !== undefined) {
	document.getElementsByName("name")[0].placeholder = "Name"
}
if(document.getElementsByName("surname")[0] !== undefined) {
	document.getElementsByName("surname")[0].placeholder = "Surname"
}
if(document.getElementsByName("password")[0] !== undefined) {
	document.getElementsByName("password")[0].placeholder = "Password"
}
if(document.getElementsByName("confirm")[0] !== undefined) {
	document.getElementsByName("confirm")[0].placeholder = "Confirm Password"
}
if(document.getElementsByName("key")[0] !== undefined) {
	document.getElementsByName("key")[0].placeholder = "Activation Key"
}
if(document.getElementsByName("phone_number")[0] !== undefined) {
	document.getElementsByName("phone_number")[0].placeholder = "Phone Number"
}
if(document.getElementsByName("position")[0] !== undefined) {
	document.getElementsByName("position")[0].placeholder = "Position"
}


// passcode buttons
let passcode = 0;

document.getElementById("delete").onclick = function() {
	passcode = 0;
	document.getElementById("passcode").value = passcode;
}

buttons = document.getElementsByClassName("button");
for(let i = 0; i < buttons.length; i++) {
	document.getElementById("_" + i).onclick = function() {
		passcode = passcode * 10 + i;
		document.getElementById("passcode").value = passcode;
	}
}