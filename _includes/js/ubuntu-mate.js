//--------------------------------------
// Header Dropdown
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
function download_thanks(method) {
    setTimeout(function() {
        window.location.href = "thanks/?method=" + method;
    }, 500);
}

//--------------------------------------
// Carousel "Gallery"
//--------------------------------------
$(window).ready(function() {
    if ($(".gallery").length > 0) {
        $(".gallery").slick({
            infinite: true,
            dots: true,
            nextArrow: '<button type="button" class="slick-next">→</button>',
            prevArrow: '<button type="button" class="slick-prev">←</button>'
        });
    }
});

//--------------------------------------
// Search page
//--------------------------------------
$(window).ready(function() {
    var locale = $("html").attr("lang");
    var json_path = "/search/search.json";
    if (locale != "en") {
        json_path = "/" + locale + "/search/search.json";
    }

    if ($("#search-input").length > 0) {
        var sjs = SimpleJekyllSearch({
            searchInput: document.getElementById("search-input"),
            resultsContainer: document.getElementById("results-container"),
            json: json_path
        });

        // Execute search again if using back button.
        var value = $("#search-input").val();
        if (value.length > 0) {
            setTimeout(function() {
                sjs.search(value);
            }, 750);
        }
    }
});

//--------------------------------------
// Dark mode toggle (for browsers that can't switch automatically)
//--------------------------------------
function toggle_dark() {
    if (localStorage.getItem("dark") === "true") {
        localStorage.setItem("dark", "false");
        document.getElementById("dark-sheet").media = "(prefers-color-scheme: dark)";
    } else {
        localStorage.setItem("dark", "true");
        document.getElementById("dark-sheet").media = "";
    }
}

if (matchMedia("(prefers-color-scheme: dark)").matches === true) {
    document.getElementById("dark-toggle").remove();
}

//--------------------------------------
// i18n: /en/ link does not work
//--------------------------------------
if ($("html").attr("lang") != "en") {
    var path = window.location.pathname.split("/");
    path.shift()
    path.shift();
    $("#en-nav-btn").attr("href", "/" + path.join("/"));
}

//--------------------------------------
// Blog index - hide older posts
//--------------------------------------
function show_all_posts() {
    $(".post-card.old").removeClass("old");
    $("#show-old-posts").remove();
    return false;
}

//--------------------------------------
// Features - filter dropdowns
//--------------------------------------
function refresh_feature_filters() {
    var filter_distro = document.getElementById("filter-distro");
    var filter_minimal = document.getElementById("filter-min-only");

    var class_name = filter_distro.options[filter_distro.selectedIndex].attributes.name.value;
    var min_only = filter_minimal.checked;

    $(".feature").removeClass("filtered");
    $(".filter-" + class_name).addClass("filtered");
    if (min_only === true) {
        $(".filter-min-only").addClass("filtered");
    }
    filter_distro.disabled = filter_minimal.checked;
}

if ($(".feature-filter").length > 0) {
    refresh_feature_filters();
}
