// The delete / save btns get swapped so the btn
// to be swapped in is stored here
var temp_btn = document.createElement("input");
temp_btn.id = "save-btn";
temp_btn.type = "submit";
temp_btn.value = "Save";
temp_btn.classList.add("button");
temp_btn.classList.add("button--inverted");

var prev_values = {};
function BeginEdit() {
    // Make all editable fields editable
    var form_inputs = document.querySelectorAll(".user-card__input--editable");
    for(var i = 0; i < form_inputs.length; ++i) {
        form_inputs[i].style.backgroundColor = "white";
        form_inputs[i].disabled = false;
        // Need to cache the previous values in case user wants
        // to discard changes
        prev_values[form_inputs[i].id] = form_inputs[i].value;
    }

    // Change edit and delete buttons
    var edit_btn = document.querySelector("#edit-btn");
    edit_btn.innerHTML = "Discard";
    edit_btn.onclick = EndEdit;

    // Swap delete w/ save btn
    var delete_btn = document.querySelector("#delete-btn");
    delete_btn.parentNode.replaceChild(temp_btn, delete_btn);
    temp_btn = delete_btn;
}

function EndEdit() {
    // Make editable inputs un-editable again
    var form_inputs = document.querySelectorAll(".user-card__input--editable");
    for(var i = 0; i < form_inputs.length; ++i) {
        form_inputs[i].style.backgroundColor = "#009879";
        form_inputs[i].disabled = true;
        // Restore prev values from dictionary cache
        form_inputs[i].value = prev_values[form_inputs[i].id];
    }

    // Change discard back to edit
    var edit_btn = document.querySelector("#edit-btn");
    edit_btn.innerHTML = "Edit";
    edit_btn.onclick = BeginEdit;

    // Swap save w/ delete btn
    var save_btn = document.querySelector("#save-btn");
    save_btn.parentNode.replaceChild(temp_btn, save_btn);
    temp_btn = save_btn;
}
