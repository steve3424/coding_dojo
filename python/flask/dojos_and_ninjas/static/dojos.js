function ValidateDojoForm() {
    if(!document.forms["dojo-form"]["dojo_name"].value) {
        alert("Must specify dojo name");
        return false;
    }
    return true;
}