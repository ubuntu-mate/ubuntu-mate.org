<!--
.. title: Ubuntu MATE for the GPD Pocket and GPD Pocket 2
.. slug: gpd-pocket
.. date: 2018-10-17 17:00:00 UTC
.. tags: Ubuntu,MATE,GPD Pocket,GPD Pocket 2,download
.. link:
.. description: Ubuntu MATE for the GPD Pocket and GPD Pocket 2
.. type: text
.. author: Martin Wimpress
-->

The Ubuntu MATE team offers a bespoke image for the
[GPD Pocket](https://gpd.hk/gpdpocket) and [GPD Pocket 2](https://gpd.hk/gpdpocket2)
that includes the hardware specific tweaks to get these devices working
*"out of the box"* without any faffing about.

The GPD Pockets were very successful crowd funded netbook style laptops 
featuring a high resolution 7" touch display housed in an aluminium alloy 
body. The original GPD Pocket (2017) offered an Ubuntu pre-load option while 
the GPD Pocket 2 (2018) is available with Windows 10 only. The pre-configured 
image of Ubuntu MATE for the GPD Pockets is a continuation of the excellent 
work by [Hans de Goede](https://hansdegoede.livejournal.com/), 
[nexus511](https://apt.nexus511.net/), 
[stockmind](https://github.com/stockmind/gpd-pocket-ubuntu-respin) and many 
others following the release of the original GPD Pocket.

<div align="center">
  <img src="/gallery/blog/gpd-pockets.jpg" /></a><br />
  <b>Ubuntu MATE 18.10 running on the GPD Pocket (left) and GPD Pocket 2 (right)</b>
</div>
<br />

The Ubuntu MATE 18.10 image for the GPD Pocket and GPD Pocket 2 adds the
following tweaks to the vanilla image:

  * Frame buffer rotation.
  * Internal display rotation for Xorg.
  * Touch screen rotation.
  * Double the console (tty) font resolution.
  * The display manager (Slick Greeter) configured to use HiDPI mode.
  * The display in the desktop session is scaled to produce an an effective resolution of 1280x800 which makes the 7" 1920x1200 panel readable.
    * This scaling can easily be disabled for anyone wanting the full native panel resolution.
  * The additional BRMC4356 configuration required for the original GPD Pocket is included so WiFi works.

<div class="bs-component">
  <div class="jumbotron">
    <h1>Download</h1>
      <p>Run Ubuntu MATE on your GPD Pocket or GPD Pocket 2 today!</p>
      <a href="/download/" class="btn btn-primary btn-lg">Download Ubuntu MATE</a>
      </p>
    </div>
</div>

## Disable desktop session scaling

If you want to restore the full native panel resolution of the GPD Pocket then
open *Startup Applications* from the *Control Center*. Find the entry called
*GPD Pocket Display Scaler* in the *Startup Programs* tab and untick it. Log
out and back in and the full 1920x1200 resolution is restored.

<div align="center">
  <img src="/gallery/blog/gpd-pocket-display-scaler.png" /></a><br />
  <b>Disable GPD Pocket Display Scaler via Startup Applications Preferences</b>
</div>
<br />

## Known Issues

  * The GRUB2 menu is not rotated on the GPD Pocket.
    * The workaround is to tilt your head.
  * The GRUB2 menu is not displayed at all on the GPD Pocket 2.
    * The workaround is to wait and the system will boot after a few seconds or press <kbd>Enter</kbd> to boot immeditately.
  * The Plymouth splash screen is not rotated on the GPD Pocket or GPD Pocket 2.
    * The workaround is to not care.

## Feedback

This image for the GPD Pocket is community supported, please post all feedback
via the [community forum](https://ubuntu-mate.community/).
