<!--
.. title: Download Ubuntu MATE
.. slug: download
.. date: 2016-04-04 10:00:00 UTC
.. tags: Ubuntu,MATE,download
.. link:
.. description: Download Ubuntu MATE
.. type: text
.. author: Luke Horwell
-->

## Download
Download a copy of the .iso image to try Ubuntu MATE without changing your
computer at all, and optionally install permanently later.

<noscript>
  <div class="alert alert-danger">
    <h3>Please enable JavaScript to continue.</h3>
    <p>This download page uses JavaScript to populate the download links
    and relevant information, but it is disabled for this browser.</p>
    <p>Alternately, you can access most links from
    [Canonical's CD Image Server](http://cdimage.ubuntu.com/ubuntu-mate/releases/).</p>
  </div>
</noscript>

<style>
  #arch-list .well {
    margin: 0;
    padding: 16px;
    color: black;
    cursor: pointer;
  }

  #arch-list a:hover {
    text-decoration: none;
  }

  .well.active {
    border: 2px solid #9AB270;
    color: #fff !important;
    background-color: #87a556 !important;
  }
</style>

<div id="release-list">
  <p>Choose a Release:</p>
  <ul id="release" class="nav nav-pills" role="tablist">
    <li id="version-A" role="presentation"><a href="#version-A" aria-controls="home" role="tab" data-toggle="tab"><img src="/favicon-16.png"/> version-A-FRIENDLY-NAME</a></li>
    <li id="version-B" role="presentation"><a href="#version-B" aria-controls="profile" role="tab" data-toggle="tab"><img src="/favicon-16.png"/> version-B-FRIENDLY-NAME</a></li>
    <li id="version-C" role="presentation"><a href="#version-C" aria-controls="home" role="tab" data-toggle="tab"><img src="/favicon-16.png"/> version-C-FRIENDLY-NAME</a></li>
  </ul>
  <hr>
</div>

<div id="arch-list" class="row" hidden>
  <p>Choose your Architecture:</p>
  <a id="amd64" onclick="selected_amd64()">
    <div class="col-xs-3 well bs-component">
      <h3>64-bit</h3>
      <p>
        Ideal for computers with:
        <ul>
          <li>More than 3 GB of RAM.</li>
          <li>64-bit capable Intel and AMD processors</li>
          <li>UEFI PCs booting in CSM mode.</li>
          <li>Modern Intel-based Apple Macs</li>
        </ul>
      </p>
    </div>
  </a>
  <a id="i386" onclick="selected_i386()">
    <div class="col-xs-3 well bs-component">
      <h3>32-bit</h3>
      <p>
        Ideal for computers with:
        <ul>
          <li>Less than 2 GB of RAM.</li>
          <li>Intel and AMD processors.</li>
          <li>Ageing PCs with low-RAM resources.</li>
          <li>Older Intel-based Apple Macintosh systems.</li>
        </ul>
      </p>
    </div>
  </a>
  <a id="powerpc" onclick="selected_powerpc()">
    <div class="col-xs-3 well bs-component">
      <h3>PowerPC</h3>
      <p>
        Designed for old generation PowerPC-based hardware, like:
        <ul>
          <li>Apple Macintosh G3, G4 and G5</li>
          <li>Apple iBooks and PowerBooks</li>
          <li>IBM OpenPower 7xx Machines</li>
        </ul>
      </p>
    </div>
  </a>
  <a id="armhf" onclick="selected_armhf()">
    <div class="col-xs-3 well bs-component">
      <h3>Raspberry Pi</h3>
      <p>
        For aarch32 (ARMv7) computers, like:
        <ul>
          <li>Raspberry Pi 2</li>
          <li>Raspberry Pi 3</li>
        </ul>
      </p>
    </div>
  </a>
</div>
<hr>
</div>
<div id="download-links" class="row" hidden>
  <div id="release-notes" class="row">
    <div class="col-xs-3">
      <div class="text-center">
        <img src="/favicon-144.png" alt="Ubuntu MATE">
      </div>
    </div>
    <div class="col-xs-9">
      <h3>Ubuntu MATE <span id="present-version"></span> for <span id="present-arch"></span> systems.</h3>
      <p>See what's new and any other important information for this release.</p>
      <p><a class="version-A" href="version-A-RELEASE-URL"><span class="fa fa-file"></span> Release Announcement</a></p>
      <p><a class="version-B" href="version-B-RELEASE-URL"><span class="fa fa-file"></span> Release Announcement</a></p>
      <p><a class="version-C" href="version-C-RELEASE-URL"><span class="fa fa-file"></span> Release Announcement</a></p>
      <p><a class="rpi" href="/raspberry-pi/"><img src="/images/logos/raspberry-pi.png" width="16px" height="16px"> Learn More</a></p>
      <p><a class="rpi" href="/raspberry-pi-change-log/"><img src="/images/logos/raspberry-pi.png" width="16px" height="16px"> What's New?</a></p>
      <div id="version-A-WARNING" hidden>
        <h3><b><span class="fa fa-warning"></span> version-A-WARNING-HEADER</b></h3>
        <p>version-A-WARNING-TEXT</p>
      </div>
      <div id="version-B-WARNING" hidden>
        <h3><b><span class="fa fa-warning"></span> version-B-WARNING-HEADER</b></h3>
        <p>version-B-WARNING-TEXT</p>
      </div>
      <div id="version-C-WARNING" hidden>
        <h3><b><span class="fa fa-warning"></span> version-C-WARNING-HEADER</b></h3>
        <p>version-C-WARNING-TEXT</p>
      </div>
      <div id="LTS" class="alert alert-success LTS-CODENAMES">
        <p>
          <b><span class="fa fa-star"></span> This release has Long Term Support (LTS)</b><br>
          Recommended if you desire a stable system. Support ends <b>LTS_END_DATE</b>.
        </p>
      </div>
    </div>
  </div>
  <hr>
  <div id="getting-started" class="row" hidden>
    <div class="col-xs-3">
      <div class="text-center">
        <br><br><br><br><br>
        <img src="../assets/img/misc/getting-started.png" alt="Getting Started Resources">
      </div>
    </div>
    <div class="col-xs-9">
      <h2>Thank you for downloading.</h2>
      <hr>
      <h3>Getting Started</h3>
      <p>The following resources may be useful to help get you up and running.</p>
      <p>
        <ul>
          <li><a href="../how-to-create-bootable-usb-drive"><span class="fa fa-usb"></span> Creating a bootable USB on Windows, Mac and GNU/Linux</a></li>
          <li><a href="https://help.ubuntu.com/community/BurningIsoHowto"><span class="fa fa-dot-circle-o"></span> Burning a DVD on Windows, Mac and GNU/Linux</a></li>
          <li><a href="../about/#hardware_requirements"><span class="fa fa-laptop"></span> Check your System Requirements</a></li>
        </ul>
      </p>
      <hr>
      <h3>Get Involved</h3>
      <p>Stop by to share your experiences, ask questions and discuss topics
      with other users and developers in our growing community.</p>
      <p><a href="https://ubuntu-mate.community"><span class="fa fa-user"></span> Meet the Community</a></p>
      <hr>
      <h3>Squish the Bugs</h3>
      <p>Found a serious issue? Please report them to Launchpad so we can
      get the relevant developers on the job.</p>
      <p><a href="https://bugs.launchpad.net/ubuntu-mate"><span class="fa fa-bug"></span> View Bug Tracker</a></p>
    </div>
  </div>
  <hr class="getting-started-hr">
  <div id="bittorrent" class="row">
    <div class="col-xs-3">
      <div class="text-center">
        <img src="../assets/img/misc/torrent.png" alt="BitTorrent">
      </div>
    </div>
    <div class="col-xs-9">
      <h3>Via Torrent</h3>
      <p>If you can spare the bytes, a torrent is the recommended method to download Ubuntu MATE.</p>
      <p>
        <a class="version-A-i386" onclick="thanks()" href="version-A-TORRENT-URL-i386"><span class="fa fa-download"></span> version-A-TORRENT-NAME-i386</a>
        <a class="version-A-amd64" href="version-A-TORRENT-URL-amd64"><span class="fa fa-download"></span> version-A-TORRENT-NAME-amd64</a>
        <a class="version-A-powerpc" href="version-A-TORRENT-URL-powerpc"><span class="fa fa-download"></span> version-A-TORRENT-NAME-powerpc</a>
        <a class="version-A-armhf" href="version-A-TORRENT-URL-armhf"><span class="fa fa-download"></span> version-A-TORRENT-NAME-armhf</a>
        <a class="version-B-i386" href="version-B-TORRENT-URL-i386"><span class="fa fa-download"></span> version-B-TORRENT-NAME-i386</a>
        <a class="version-B-amd64" href="version-B-TORRENT-URL-amd64"><span class="fa fa-download"></span> version-B-TORRENT-NAME-amd64</a>
        <a class="version-B-powerpc" href="version-B-TORRENT-URL-powerpc"><span class="fa fa-download"></span> version-B-TORRENT-NAME-powerpc</a>
        <a class="version-B-armhf" href="version-B-TORRENT-URL-armhf"><span class="fa fa-download"></span> version-B-TORRENT-NAME-armhf</a>
        <a class="version-C-i386" href="version-C-TORRENT-URL-i386"><span class="fa fa-download"></span> version-C-TORRENT-NAME-i386</a>
        <a class="version-C-amd64" href="version-C-TORRENT-URL-amd64"><span class="fa fa-download"></span> version-C-TORRENT-NAME-amd64</a>
        <a class="version-C-powerpc" href="version-C-TORRENT-URL-powerpc"><span class="fa fa-download"></span> version-C-TORRENT-NAME-powerpc</a>
        <a class="version-C-armhf" href="version-C-TORRENT-URL-armhf"><span class="fa fa-download"></span> version-C-TORRENT-NAME-armhf</a>
      </p>
      <p>
        <a class="version-A-i386" href="version-A-MAGNET-URI-i386"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-A-amd64" href="version-A-MAGNET-URI-amd64"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-A-powerpc" href="version-A-MAGNET-URI-powerpc"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-A-armhf" href="version-A-MAGNET-URI-armhf"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-B-i386" href="version-B-MAGNET-URI-i386"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-B-amd64" href="version-B-MAGNET-URI-amd64"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-B-powerpc" href="version-B-MAGNET-URI-powerpc"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-B-armhf" href="version-B-MAGNET-URI-armhf"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-C-i386" href="version-C-MAGNET-URI-i386"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-C-amd64" href="version-C-MAGNET-URI-amd64"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-C-powerpc" href="version-C-MAGNET-URI-powerpc"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a class="version-C-armhf" href="version-C-MAGNET-URI-armhf"><span class="fa fa-magnet"></span> Magnet Link</a>
        <a title="Opens your BitTorrent client. This method is trackerless and doesn't utilize web seeds. The true peer to peer option.">
          <span class="fa fa-info-circle"></span>
        </a>
      </p>
    </div>
  </div>
  <hr>
  <div id="direct-download" class="row">
    <div class="col-xs-3">
      <div class="text-center">
        <br>
        <img src="../assets/img/misc/iso-dvd-cd-disc.png" alt="Direct Download">
      </div>
    </div>
    <div class="col-xs-9">
      <h3>Via Direct Download</h3>
      <p>If preferred, you can also download the images over HTTP.</p>
      <p>
        <a class="version-A-i386" href="version-A-DIRECT-URL-i386"><span class="fa fa-download"></span> version-A-DIRECT-NAME-i386</a>
        <a class="version-B-i386" href="version-B-DIRECT-URL-i386"><span class="fa fa-download"></span> version-B-DIRECT-NAME-i386</a>
        <a class="version-C-i386" href="version-C-DIRECT-URL-i386"><span class="fa fa-download"></span> version-C-DIRECT-NAME-i386</a>
        <a class="version-A-amd64" href="version-A-DIRECT-URL-amd64"><span class="fa fa-download"></span> version-A-DIRECT-NAME-amd64</a>
        <a class="version-B-amd64" href="version-B-DIRECT-URL-amd64"><span class="fa fa-download"></span> version-B-DIRECT-NAME-amd64</a>
        <a class="version-C-amd64" href="version-C-DIRECT-URL-amd64"><span class="fa fa-download"></span> version-C-DIRECT-NAME-amd64</a>
        <a class="version-A-powerpc" href="version-A-DIRECT-URL-powerpc"><span class="fa fa-download"></span> version-A-DIRECT-NAME-powerpc</a>
        <a class="version-B-powerpc" href="version-B-DIRECT-URL-powerpc"><span class="fa fa-download"></span> version-B-DIRECT-NAME-powerpc</a>
        <a class="version-C-powerpc" href="version-C-DIRECT-URL-powerpc"><span class="fa fa-download"></span> version-C-DIRECT-NAME-powerpc</a>
        <img class="rpi" src="../images/flags/European-Union-Flag-16.png" width="16px" height="16px"/>
        <a class="version-A-armhf" href="version-A-DIRECT-URL-armhf-eu"> version-A-DIRECT-NAME-armhf-eu</a>
        <a class="version-B-armhf" href="version-B-DIRECT-URL-armhf-eu"> version-B-DIRECT-NAME-armhf-eu</a>
        <a class="version-C-armhf" href="version-C-DIRECT-URL-armhf-eu"> version-C-DIRECT-NAME-armhf-eu</a>
        <br class="rpi">
        <img class="rpi" src="../images/flags/Canada-Flag-16.png" width="16px" height="16px"/>
        <a class="version-A-armhf" href="version-A-DIRECT-URL-armhf-ca"> version-A-DIRECT-NAME-armhf-ca</a>
        <a class="version-B-armhf" href="version-B-DIRECT-URL-armhf-ca"> version-B-DIRECT-NAME-armhf-ca</a>
        <a class="version-C-armhf" href="version-C-DIRECT-URL-armhf-ca"> version-C-DIRECT-NAME-armhf-ca</a>
        <br class="rpi">
        <img class="rpi" src="../images/flags/France-Flag-16.png" width="16px" height="16px"/>
        <a class="version-A-armhf" href="version-A-DIRECT-URL-armhf-fr"> version-A-DIRECT-NAME-armhf-fr</a>
        <a class="version-B-armhf" href="version-B-DIRECT-URL-armhf-fr"> version-B-DIRECT-NAME-armhf-fr</a>
        <a class="version-C-armhf" href="version-C-DIRECT-URL-armhf-fr"> version-C-DIRECT-NAME-armhf-fr</a>
      </p>
      <p>
        <b>SHA256 Checksum:</b>
        <code class="version-A-i386">version-A-SHA256-i386</code>
        <code class="version-A-amd64">version-A-SHA256-amd64</code>
        <code class="version-A-powerpc">version-A-SHA256-powerpc</code>
        <code class="version-A-armhf">version-A-SHA256-armhf</code>
        <code class="version-B-i386">version-B-SHA256-i386</code>
        <code class="version-B-amd64">version-B-SHA256-amd64</code>
        <code class="version-B-powerpc">version-B-SHA256-powerpc</code>
        <code class="version-B-armhf">version-B-SHA256-armhf</code>
        <code class="version-C-i386">version-C-SHA256-i386</code>
        <code class="version-C-amd64">version-C-SHA256-amd64</code>
        <code class="version-C-powerpc">version-C-SHA256-powerpc</code>
        <code class="version-C-armhf">version-C-SHA256-armhf</code>
      </p>
      <p>
        <b>Download Size:</b>
        <span class="version-A-i386">version-A-SIZE-i386</span>
        <span class="version-A-amd64">version-A-SIZE-amd64</span>
        <span class="version-A-powerpc">version-A-SIZE-powerpc</span>
        <span class="version-A-armhf">version-A-SIZE-armhf</span>
        <span class="version-B-i386">version-B-SIZE-i386</span>
        <span class="version-B-amd64">version-B-SIZE-amd64</span>
        <span class="version-B-powerpc">version-B-SIZE-powerpc</span>
        <span class="version-B-armhf">version-B-SIZE-armhf</span>
        <span class="version-C-i386">version-C-SIZE-i386</span>
        <span class="version-C-amd64">version-C-SIZE-amd64</span>
        <span class="version-C-powerpc">version-C-SIZE-powerpc</span>
        <span class="version-C-armhf">version-C-SIZE-armhf</span>
      </p>
      <p><a href="../how-to-verify-downloads"><span class="fa fa-question-circle"></span> How to verify downloads</a></p>
      <div class="rpi">
        <span class="fa fa-heart"></span>
        Many thanks to First Colo for contributing the hosting and bandwidth for the Ubuntu MATE downloads
        for the Raspberry Pi images.
      </div>
    </div>
  </div>
  <hr>
  <div id="download-tips" class="row">
    <div class="col-xs-3">
      <div class="text-center">
        <br>
        <img src="../assets/img/misc/download-tips.png" alt="Download Tip">
      </div>
    </div>
    <div class="col-xs-9">
      <h3>Download Tip</h3>
      <p>
        If everyone who downloaded Ubuntu MATE donated $2.50 it would fund the full-time development
        of Ubuntu MATE and MATE Desktop. Please give us a tip and help both projects flourish!
      </p>
      <div class="row">PAYPAL-DOWNLOAD-TIPS</div>
      <p><b>Powered by </b> <img src="../assets/img/logos/pp-logo-100px.png" height="24px"/></p>
      <p>
        To donate more or become an Ubuntu MATE patron
        <a href="https://ubuntu-mate.org/donate/">please visit the donate page</a>.
      </p>
    </div>
  </div>
  <hr>
  <div id="sponsor1" class="row">
    <div class="col-xs-3">
      <div class="text-center">
        <br><br>
        <img src="../images/sponsors/osdisc.png" alt="OSDisc.com">
      </div>
    </div>
    <div class="col-xs-9">
      <h3>Purchase DVDs and USBs</h3>
      <h4><b>OSDisc.com</b></h4>
      <p>OSDisc.com is a leading source for Linux DVDs and USBs. Purchase ready-to-use bootable
      DVDs and memory sticks that come pre-installed with Ubuntu MATE and have persistent storage.</p>
      <p>
        <a href="https://www.osdisc.com/products/ubuntumate?affiliate=ubuntumate">
          <span class="fa fa-shopping-cart"></span> Purchase
        </a>
      </p>
    </div>
  </div>
  <br>
  <div id="sponsor2" class="row">
    <div class="col-xs-3">
      <div class="text-center">
        <br>
        <img src="../images/merch/hellotux/flash-drive.png" alt="HelloTux Flash Drive">
      </div>
    </div>
    <div class="col-xs-9">
      <h4><b>HELLOTUX</b></h4>
      <p>HELLOTUX sell an Ubuntu MATE branded 8GB Metallic Unibody USB stick that is just 41 mm
      long and less than 5 mm thick. It’s the perfect flash drive for your key ring, always
      with you. HELLOTUX will also help you to upgrade your flash drive to the next version
      of Ubuntu MATE, absolutely free.</p>
      <p>
        <a href="https://www.hellotux.com/ubuntumate1510_flash_drive">
          <span class="fa fa-shopping-cart"></span> Purchase
        </a>
      </p>
    </div>
  </div>
  <hr>
  <div id="mirrors" class="row">
    <div class="col-xs-3">
      <div class="text-center">
        <br>
        <img src="../assets/img/logos/i18n-small.png" alt="Mirrors and Other Options">
      </div>
    </div>
    <div class="col-xs-9">
      <h3>Mirrors and Other Options</h3>
      <p>You might prefer to find a DVD image on a mirror server that is geographically
      close to you in order to achieve a faster download.</p>
      <p>
        <a target="_blank" href="https://launchpad.net/ubuntu/+cdmirrors">
          <span class="fa fa-globe"></span> List Official Mirrors
        </a>
      </p>
      <p>
        <a class="version-A" href="version-A-OTHER" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads</a>
        <a class="version-B" href="version-B-OTHER" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads</a>
        <a class="version-C" href="version-C-OTHER" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads</a>
      </p>
    </div>
  </div>
  <hr id="mirrors-hr">
  <br>
</div>

<script src="https://code.jquery.com/jquery-1.12.2.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-XdYbMnZ/QjLh6iI4ogqCTaIjrFk87ip+ekIjefZch0Y+PvJ8CDYtEs1ipDmPorQ+" crossorigin="anonymous">

<script>

<!-- JQuery -->
if (typeof jQuery == 'undefined') {
document.write(unescape("%3Cscript src='/assets/js/jquery-2.0.0.min.js' type='text/javascript'%3E%3C/script%3E"));
}

<!-- Bootstrap -->
if ( typeof($.fn.modal) === 'undefined') {
document.write('<script src="/assets/js/bootstrap.min.js"><\/script>')
}
$.fn.modal || document.write('<script src="">\x3C/script>')

</script>

<script>
  // # Set variables
  var version = {v1: "version-A", v2: "version-B", v3: "version-C"};
  var arch = {a1: "i386", v2: "amd64", v3: "powerpc", v4: "armhf"};
  //
  // # Set defaults
  var show_version = "x";
  var show_arch = "x";
  var present_version = "x"
  var present_arch = "x"
  //
  function updatePage() {
    var v1, a1, v2, a2;
    for (v1 in version) {
      v2 = version[v1];
      $('.' + v2).hide();
      for (a1 in arch) {
        a2 = arch[a1];
        $('.' + v2 + '-' + a2).hide();
        $('#' + a2 + ' .well').removeClass('active');
      }
    }
    $('.' + show_version).show();
    $('.' + show_version + '-' + show_arch).show();
    $('#' + show_arch + ' .well').addClass('active');
    $('#present-version').html(present_version)
    $('#present-arch').html(present_arch)
  }
  //
  function showDownloadLinks() {
    $('#arch-help').slideUp();
    $('#arch-help-tab').fadeIn();
    $('#download-links').slideDown();
    $('#mirrors').show();
    $('#mirrors-hr').show();
    $('.rpi').hide();
    $('#LTS').hide();
  }
  //
  // !!! // Hide on page load.
  // V1-Hide
  // V2-Hide
  // V3-Hide
  updatePage();
  //
  // Selecting a distro version
  $( "#version-A" ).click(function() {
    show_version = "version-A";
    present_version = "version-A-RELEASE";
    updatePage();
    $('#arch-list').slideDown();
    //version-A-show-LTS
  });
  //
  $( "#version-B" ).click(function() {
    show_version = "version-B";
    present_version = "version-B-RELEASE";
    updatePage();
    $('#arch-list').slideDown();
    //version-B-show-LTS
  });
  //
  $( "#version-C" ).click(function() {
    show_version = "version-C";
    present_version = "version-C-RELEASE";
    updatePage();
    $('#arch-list').slideDown();
    //version-C-show-LTS
  });
  //
  // Selecting a architecture
  function selected_i386() {
    show_arch = "i386";
    present_arch = "i386";
    showDownloadLinks();
    updatePage();
  }
  function selected_amd64() {
    show_arch = "amd64";
    present_arch = "amd64";
    showDownloadLinks();
    updatePage();
  }
  function selected_powerpc() {
    show_arch = "powerpc";
    present_arch = "PowerPC";
    showDownloadLinks();
    updatePage();
  }
  function selected_armhf() {
    show_arch = "armhf";
    present_arch = "Raspberry Pi 2 and 3";
    showDownloadLinks();
    updatePage();
    $('#mirrors').hide();
    $('#mirrors-hr').hide();
    $('.rpi').show();
  }
  function thanks() {
    $('#getting-started').slideDown('slow');
    $('#getting-started-hr').show();
  }
</script>
