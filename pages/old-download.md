<!-- 
.. title: Download
.. slug: old-download
.. date: 2014-06-10 23:01:09 UTC
.. tags: Ubuntu,MATE,download
.. link: 
.. description: 
.. type: text
.. author: Martin Wimpress
-->

<div class="bs-component">
    <div class="jumbotron">
        <h1>Looking for the long term release??</h1>
        <p>Are you looking for the Ubuntu MATE 14.04 long term release that is supported until 2019?</p>
        <a href="/trusty/" class="btn btn-primary btn-lg">Download the LTS</a>
        </p>
    </div>
</div>

The Ubuntu MATE .iso image allows you to try Ubuntu MATE without 
changing your computer at all, and at your option to install it 
permanently later. You will need at least 512MiB of RAM to install 
from this image. The image can be burned to a DVD, mounted as an ISO 
file, or be directly written to a USB stick using a utility like `dd` 
or `ddrescue` (from the `gddrescue` package), for example:

    sudo ddrescue -d -D --force ISO_32_FILE /dev/sdx
    sudo ddrescue -d -D --force ISO_64_FILE /dev/sdx
    sudo ddrescue -d -D --force ISO_MAC_FILE /dev/sdx

If you want to make a bootable USB with Windows try [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/).

If you direct download the .iso image please make sure the appropriate
MD5 hash matches.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Grow your community</h1>
        <p>Become a full Ubuntu MATE community member by helping to grow and
        sustain it. Warm and fuzzy sensations guaranteed.</p>
        <a href="/donate/" class="btn btn-primary btn-lg">Donate</a>
        </p>
    </div>
</div>

## Download options

Ubuntu MATE is currently available for two architectures.

<div class="bs-component">
    <div class="alert alert-info">
        <strong>BitTorrent</strong> If you can spare the bytes, please
        download via BitTorrent and leave the client open after your
        download is finished, so you can seed it back to others. <i>A
        web-seed capable client is recommended for fastest download speeds.</i>
    </div>
</div>

<div class="row">
  <div class="col-lg-4">
    <div class="bs-component">
      <div class="list-group">
        <a class="list-group-item active">PC (Intel x86)</a>
        <p class="list-group-item">For almost all PCs. This includes most machines with Intel/AMD/etc type processors and almost all computers that run Microsoft Windows, as well as newer Apple Macintosh systems based on Intel processors. Choose this if you are at all unsure.</p>
        <p class="list-group-item">Size : ISO_32_SIZE MB</p>
        <p class="list-group-item">Hash : <code>ISO_32_MD5</code></p>
        <a class="list-group-item" href="https://ubuntu-mate.org/download/TOR_32_FILE"><strong>Torrent : <u>TOR_32_FILE</ul></strong></a>
      </div>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="bs-component">
      <div class="list-group">
        <a class="list-group-item active">64-bit PC (AMD64)</a>
        <p class="list-group-item">Choose this to take full advantage of computers based on the AMD64 or EM64T architecture (e.g., Athlon64, Opteron, EM64T Xeon, Core 2). If you have a non-64-bit processor made by AMD, or if you need full support for 32-bit code, use the Intel x86 images instead.</p>
        <p class="list-group-item">Size : ISO_64_SIZE MB</p>
        <p class="list-group-item">Hash : <code>ISO_64_MD5</code></p>
        <a class="list-group-item" href="https://ubuntu-mate.org/download/TOR_64_FILE"><strong>Torrent : <u>TOR_64_FILE</u></strong></a>
      </div>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="bs-component">
      <div class="list-group">
        <a class="list-group-item active">64-bit Mac (AMD64)</a>
        <p class="list-group-item">Choose this to take full advantage of computers based on the AMD64 or EM64T architecture (e.g., Athlon64, Opteron, EM64T Xeon, Core 2). If you have a non-64-bit processor made by AMD, or if you need full support for 32-bit code, use the Intel x86 images instead. <a href="http://askubuntu.com/questions/37999/what-is-different-about-the-mac-iso-image/40480#40480" target="_blank">This image is adjusted to work properly on Mac systems.</a></p>
        <p class="list-group-item">Size : ISO_MAC_SIZE MB</p>
        <p class="list-group-item">Hash : <code>ISO_MAC_MD5</code></p>
        <a class="list-group-item" href="https://ubuntu-mate.org/download/TOR_MAC_FILE"><strong>Torrent : <u>TOR_MAC_FILE</u></strong></a>
      </div>
    </div>
  </div>
</div>

<div class="bs-component">
    <div class="jumbotron">
        <h1>Release announcement</h1>
        <p>Find out what changed in ANN_TITLE</p>
        <a href="ANN_URL" class="btn btn-primary btn-lg">Release announcement</a>
        </p>
    </div>
</div>

## HTTP direct download

In addition to the recommended BitTorrent downloads above, the .iso
images can also be downloaded via HTTP.

### European CDN

Our European content distribution network (CDN) is kindly donated by
[First Colo](http://www.first-colo.com) and will automatically download from a
location closest to you.

  * [ISO_32_FILE](https://ubuntu-mate.r.worldssl.net/download/ISO_32_FILE)
  * [ISO_64_FILE](https://ubuntu-mate.r.worldssl.net/download/ISO_64_FILE)
  * [ISO_MAC_FILE](https://ubuntu-mate.r.worldssl.net/download/ISO_MAC_FILE)

### Germany

Our mirror in Germany is kindly donated by [First Colo](http://www.first-colo.com).

  * [ISO_32_FILE](http://pub.mate-desktop.org/iso/ubuntu-mate/release/i386/ISO_32_FILE)
  * [ISO_64_FILE](http://pub.mate-desktop.org/iso/ubuntu-mate/release/amd64/ISO_64_FILE)
  * [ISO_MAC_FILE](http://pub.mate-desktop.org/iso/ubuntu-mate/release/amd64+mac/ISO_MAC_FILE)

### Italy

Our mirror in Italy is kindly sponsored by [Prometeus](http://www.prometeus.net).

  * [ISO_32_FILE](https://ubuntu-mate.org/download/ISO_32_FILE)
  * [ISO_64_FILE](https://ubuntu-mate.org/download/ISO_64_FILE)
  * [ISO_MAC_FILE](https://ubuntu-mate.org/download/ISO_MAC_FILE)

### United States

Our mirror in the United States is provided by [Sourceforge](http://www.sourceforge.net).
Ubuntu MATE is [available from Sourceforge have mirror sites around the
world](http://sourceforge.net/projects/ubuntu-mate/files/).

  * [ISO_32_FILE](http://master.dl.sourceforge.net/project/ubuntu-mate/14.10/i386/ISO_32_FILE)
  * [ISO_64_FILE](http://master.dl.sourceforge.net/project/ubuntu-mate/14.10/amd64/ISO_64_FILE)
  * [ISO_MAC_FILE](http://master.dl.sourceforge.net/project/ubuntu-mate/14.10/amd64+mac/ISO_MAC_FILE)

## Sponsors

Many thanks to [First Colo](http://www.first-colo.com") and [Prometeus](http://www.prometeus.net)
for sponsoring the hosting and bandwith for the Ubuntu MATE download.

<div class="row">
  <div class="col-lg-6">
    <a href="http://www.first-colo.com"><img class="centered" src="/assets/img/banners/firstcolo_banner.png" width="320" height="90" alt="First Colo" /></a>
  </div>
  <div class="col-lg-6">
    <a href="http://www.prometeus.net"><img class="centered" src="/assets/img/banners/prometeus_banner.png" width="320" height="90" alt="Prometeus" /></a>
  </div>
</div>

<div class="bs-component">
    <div class="jumbotron">
        <h1>Hardware requirements?</h1>
        <p>Ubuntu MATE has modest hardware requirements.</p>
        <a href="/about/" class="btn btn-primary btn-lg">Learn more</a>
        </p>
    </div>
</div>

## Useful Information

You may find the following information useful, which is why we titled 
the section *Useful Information* since the information presented here
is mostly useful.

  * [Ubuntu MATE 14.10 and 15.04 Useful Information](https://ubuntu-mate.community/t/ubuntu-mate-14-10-and-15-04-useful-information/24)

## Reporting issues

Please report any issues you may find on the project's bug tracker. 

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Getting involved

Is there anything you can help with or want to be involved in? Maybe 
you just want to discuss your experiences or ask the maintainers some 
questions. Please [come and talk to us](/community/).

<script>
  // http://netnix.org/2014/04/27/tracking-downloads-with-google-analytics/
  window.onload = function() {
    var a = document.getElementsByTagName('a');
    for (i = 0; i < a.length; i++) {
      if (a[i].href.match(/^https?:\/\/.+\.(bz2|deb|gz|iso|pdf|torrent|xz|zip)$/i)) {
        a[i].setAttribute('target', '_blank');
        a[i].onclick = function() {
          ga('send', 'event', 'Downloads', 'Click', this.getAttribute('href'));
        };
      }
    }
  }
</script>
