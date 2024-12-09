/*!
 *  Ubuntu MATE Website Theme
 *
 * This JS file is licensed under the GNU Affero General Public License v3.0.
 * https://www.gnu.org/licenses/agpl-3.0.html
 *
 *  Copyright (C) 2019-2020, 2024 Luke Horwell (@lah7)
*/
//--------------------------------------
// Header Dropdown
// - Ensure only one is open at a time.
// - Close a dropdown if user clicks outside.
//--------------------------------------
const dropdowns = document.getElementsByClassName("dropdown-trigger");
function dropdownModal(input) {
    const newCheckState = input.checked;
    for (i = 0; i < dropdowns.length; i++) {
        dropdowns[i].checked = false;
    };
    input.checked = newCheckState;
}

document.addEventListener("click", function(event) {
    for (i = 0; i < dropdowns.length; i++) {
        if (dropdowns[i].checked) {
            const labels = dropdowns[i].labels;
            for (l = 0; l < labels.length; l++) {
                const bounds = labels[l].getBoundingClientRect();
                if (bounds.height === 0)
                    continue;
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
function downloadThanks(method) {
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
    const locale = $("html").attr("lang");
    const json_path = locale == "en" ? "/search/search.json" : `/${locale}/search/search.json`;

    if ($("#search-input").length > 0) {
        const sjs = SimpleJekyllSearch({
            searchInput: document.getElementById("search-input"),
            resultsContainer: document.getElementById("results-container"),
            json: json_path
        });

        // Execute search again if using back button.
        const value = $("#search-input").val();
        if (value.length > 0) {
            setTimeout(function() {
                sjs.search(value);
            }, 750);
        }
    }
});

//--------------------------------------
// Blog index - hide older posts
//--------------------------------------
function showAllPosts() {
    $(".post-card.old").removeClass("old");
    $("#show-old-posts").remove();
    return false;
}

//--------------------------------------
// Features - filter dropdowns
//--------------------------------------
function refreshFeatureFilters() {
    const filterDistro = document.getElementById("filter-distro");
    const filterMinimal = document.getElementById("filter-min-only");

    const className = filterDistro.options[filterDistro.selectedIndex].attributes.name.value;
    const minOnly = filterMinimal.checked;

    $(".feature").removeClass("filtered");
    $(".filter-" + className).addClass("filtered");
    if (minOnly) {
        $(".filter-min-only").addClass("filtered");
    }
    filterDistro.disabled = filterMinimal.checked;
}

if ($(".feature-filter").length > 0) {
    refreshFeatureFilters();
}
