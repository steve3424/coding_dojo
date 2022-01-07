function ValidateFavorite() {
    if(!document.forms["fav-form"]["book_id"].value) {
        alert("No book to favorite!")
        return false;
    }

    return true;
}