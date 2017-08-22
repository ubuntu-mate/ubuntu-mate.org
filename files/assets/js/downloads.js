download_ani_speed = 500;
var arch;
var downloads = {};

function getFilename(url) {
    var tokens = url.split("/");
    return tokens[tokens.length - 1];
}

$.ajax({
  type: "GET",
  url: "/assets/downloads.json",
  dataType: "json",
  success: function(data) { downloads = data; },
  async: true
});

function setArch(a, friendly_name) {
    arch = a;
    $(".arch-option").removeClass("selected");
    $("#" + arch).addClass("selected");
    $("#arch-list").addClass("exit");
    $(".arch-choice").html(friendly_name);
    setTimeout(function() {
        $("#arch-list").hide().removeClass("exit");
        $("#arch-selected").fadeIn(download_ani_speed);
        $("#release-list").addClass("entry").show();
    }, download_ani_speed);

    // Only show releases that support this architecture.
    var releases = Object.keys(downloads);
    releases.forEach(function(release) {
        if (downloads[release].hasOwnProperty(arch) === true) {
            $("#" + release).show();
        } else {
            $("#" + release).hide();
            return;
        }

        var elementSelector = "#" + release + " > .details > ";

        // Show warning colour if a pre-release
        $(elementSelector + ".support").removeClass("support-ends").removeClass("support-preview");
        if (downloads[release]["pre-release"] === true) {
            $(elementSelector + ".support").addClass("support-preview");
        } else {
            $(elementSelector + ".support").addClass("support-ends");
        }

        // Get details about distro, including alternates.
        $(elementSelector + ".name").html(downloads[release]["name"]);
        $(elementSelector + ".description").html(downloads[release]["description"]);
        $(elementSelector + ".support").html(downloads[release]["support"]);

        if (downloads[release][arch].hasOwnProperty("alt-name")) {
            $(elementSelector + ".name").html(downloads[release][arch]["alt-name"]);
        }

        if (downloads[release][arch].hasOwnProperty("alt-description")) {
            $(elementSelector + ".description").html(downloads[release][arch]["alt-description"]);
        }

        if (downloads[release][arch].hasOwnProperty("alt-support")) {
            $(elementSelector + ".support").html(downloads[release][arch]["alt-support"]);
        }
    });
}

function goBackToArch() {
    $(".arch-option").removeClass("selected");
    $("#arch-list").addClass("entry");
    $("#release-list").addClass("exit");
    setTimeout(function() {
        $("#release-list").hide().removeClass("exit");
        $("#arch-list").addClass("entry").show();
    }, download_ani_speed);
}

function setRelease(codename) {
    $(".release-option").removeClass("selected");
    $("#" + codename).addClass("selected");
    $("#release-list").addClass("exit");
    setTimeout(function() {
        $("#release-list").hide().removeClass("exit");
        $("#release-selected").fadeIn(download_ani_speed);
        $("#details-list").addClass("entry").show();
    }, download_ani_speed);

    var release = downloads[codename];
    var links = downloads[codename][arch];

    var name = $("#" + codename + " .details h4").html();
    var description = $("#" + codename + " .details p").html();
    var support = $("#" + codename + " .details div").html();
    $("#selected-release").html(name);

    // Update artwork
    $("#artwork-background").attr("style", "background-image:url(" + release["background-url"] + ")");

    // Update links and text on the page
    $("#release-notes").attr("href", release["release-notes"]);
    $("#torrent-download").attr("href", links["torrent"]);
    $("#magnet-download").attr("href", links["magnet-uri"]);
    $("#direct-download").attr("href", links["direct"]);
    $("#other-downloads").attr("href", release["other-downloads"]);
    $("#sha256sum").html(links["sha256sum"]);
    $("#download-size").html(links["download-size"]);
    $("#torrent-download var").html(getFilename(links["torrent"]));
    $("#direct-download var").html(getFilename(links["direct"]));

    // Special considerations for Raspberry Pi
    if (arch == "armhf") {
        $("#mirrors").hide();
        $("#getting-started").hide();
    } else {
        $("#mirrors").show();
        $("#getting-started").show();
    }

    // Update PayPal buttons
    $(".tip-name").attr("value", "Ubuntu MATE " + name + " " + arch + " Download Tip");

    // Experimental can be dangerous.
    if (release["pre-release"] === true) {
        $("#pre-release-warning").show();
    } else {
        $("#pre-release-warning").hide();
    }
}

function goBackToRelease() {
    $(".release-option").removeClass("selected");
    $("#release-list").addClass("entry");
    $("#details-list").addClass("exit");
    setTimeout(function() {
        $("#details-list").hide().removeClass("exit");
        $("#release-list").addClass("entry").show();
    }, download_ani_speed);
}
