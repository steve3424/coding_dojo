function ValidateBook() {
    if(!document.forms["book-form"]["title"].value) {
        alert("Must have title!")
        return false;
    }
    if(!document.forms["book-form"]["num_pages"].value) {
        alert("Must have number of pages!")
        return false;
    }
    return true;
}