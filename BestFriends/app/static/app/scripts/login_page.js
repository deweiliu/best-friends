var surname_text_field = document.getElementById("surname");
var firstname_text_field = document.getElementById("first_name");
var submit_username_button = document.getElementById("sub_username");
surname_text_field.onclick = function () {
	if (firstname_text_field.value == "") {
		alert("please enter your first name first!");
	}
}
submit_username_button.onclick = function () {
	if (firstname_text_field.value == "") {
		alert("please enter your first name!");
	} else if (surname_text_field.value == "") {
		alert("please enter your surname!");
	}
	else {
		alert("welcome " + firstname_text_field.value + "!");
	}
}
