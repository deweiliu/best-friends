window.onload = function () {
    var surname_text_field = document.getElementById("surname");
    var firstname_text_field = document.getElementById("first_name");
    var submit_username_button = document.getElementById("sub_username");
    //$(".bubble").hide();
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
            document.getElementById("show_bubble").innerHTML = "<span>welcome " + firstname_text_field.value + " ! </span>";
            //$(".bubble").show();
        }
    }
}



    
    

