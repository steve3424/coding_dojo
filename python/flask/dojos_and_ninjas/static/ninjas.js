function ValidateNinjaForm() {
    if(!document.forms["ninja-form"]["dojo_id"].value) {
        alert("No dojos to add ninja to!");
        return false;
    }
    return true;
}