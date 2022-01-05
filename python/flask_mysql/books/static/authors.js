function ValidateAuthor() {
    if(!document.forms["author-form"]["first_name"].value) {
        alert("Must have first name!")
        return false;
    }

    if(!document.forms["author-form"]["last_name"].value) {
        alert("Must have last name!")
        return false;
    }

    return true;
}