//--------------------------------------
// Dropdown
// - Ensure only one is open at a time.
// - Close a dropdown if user clicks outside.
//--------------------------------------
var dropdowns = document.getElementsByClassName("dropdown-trigger");
function dropdown_modal(input) {
    var newCheckState = input.checked;
    for (i = 0; i < dropdowns.length; i++) {
        dropdowns[i].checked = false;
    };
    input.checked = newCheckState;
}

document.addEventListener("click", function(event) {
    for (i = 0; i < dropdowns.length; i++) {
        if (dropdowns[i].checked === true) {
            var labels = dropdowns[i].labels;
            for (l = 0; l < labels.length; l++) {
                var bounds = labels[l].getBoundingClientRect();
                if (bounds.height === 0) continue;
                if (event.clientY > bounds.bottom) {
                    dropdowns[i].checked = false;
                }
            }
        }
    };
});

//--------------------------------------
// Download Links
// - Navigates to the end page after click.
//--------------------------------------
function download_thanks() {
    setTimeout(function() {
        window.location.href = "thanks/";
    }, 500);
}
