(function() {
    // Build the container and animate in the triangles.
    var container = $("#ubuntu-mate-triangles");

    function generate_triangle(orientation) {
        var brightness = Math.random() + 1;
        var fade_class = "";
        if (Math.random() > 0.6) {
            fade_class = "fade-even";
        } else {
            fade_class = "fade-odd";
        }
        return "<img class='triangle " + orientation + " " + fade_class + "' src='/assets/img/ubuntu-mate-triangle.svg' style='filter:grayscale(1) brightness(" + brightness + ")' />";
    }

    function generate_square() {
        return("<div class='square'>" +
                    generate_triangle("left") +
                    generate_triangle("top") +
                    generate_triangle("right") +
                    generate_triangle("bottom") +
                "</div>");
    }

    var htmlBuffer = "";
    var maxToGenerate = 25;
    if (window.innerWidth > 1250) {
        maxToGenerate = 50;
    }
    for (x = 0; x < maxToGenerate; x++) {
        htmlBuffer += generate_square();
    }
    container.append(htmlBuffer);

})();
