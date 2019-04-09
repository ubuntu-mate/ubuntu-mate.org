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

The Ubuntu MATE team offers a bespoke images for the
[GPD Pocket](https://gpd.hk/gpdpocket) and [GPD Pocket 2](https://gpd.hk/gpdpocket2)
that includes the hardware specific tweaks to get these devices working
*"out of the box"* without any faffing about.

The GPD Pockets were very successful crowd funded netbook style laptops 
featuring a high resolution 7" touch display housed in an aluminium alloy 
body. The original GPD Pocket (2017) offered an Ubuntu pre-load option while 
the GPD Pocket 2 (2018) is available with Windows 10 only. The pre-configured 
images of Ubuntu MATE for the GPD Pockets is a continuation of the excellent 
work by [Hans de Goede](https://hansdegoede.livejournal.com/), 
[nexus511](https://apt.nexus511.net/), 
[stockmind](https://github.com/stockmind/gpd-pocket-ubuntu-respin) and many 
others.

<div align="center">
  <img src="/gallery/blog/gpd-pockets.jpg" /></a><br />
  <b>Ubuntu MATE 18.10 running on the GPD Pocket (left) and GPD Pocket 2 (right)</b>
</div>
<br />

## What works

The [Ubuntu MATE images](https://ubuntu-mate.org/gpd-pocket) for the GPD
Pocket and GPD Pocket 2 adds the following tweaks:

  * Enable **frame buffer and Xorg display rotation**.
    * Supports `modesetting` *and* `xorg-video-intel` display drivers.
  * Enable **TearFree rendering by default**.
  * Enable touch screen rotation for Xorg and Wayland.  
  * Enabled an **emulated mouse scroll wheel**.
    * Activated by holding down the right trackpoint button and moving the trackpoint up/down.
  * Enable double size console (tty) font resolution.
  * Enable **resolution scaling** for 1920x1200 displays. *(MATE Desktop only)*
    * Results in an effective resolution of 1280x800 to make the 7" panel easily readable.
    * Simple to disable if you want to full resolution.
  * **GRUB is usable post-install**.
    * GPD Pocket GRUB is rotated 90 degress, but functional.
    * GPD Pocket 2 GRUB is correctly rotated and functional.
  * GPD Pocket BRMC4356 WiFi firmware enabled by default.
  * GPD Pocket fan control kernel module enable by default.

## Known Issues

### GPD Pocket

  * The GRUB2 menu is rotated 90 degress on the GPD Pocket.
    * The workaround is to tilt your head.
  * The built in speaker in the GPD Pocket is mono and doesn't play audio from the right channel.
    * The workaround is two use headphones connected the 3.5mm audio jack.

### GPD Pocket 2

  * The boot menu is not displayed in the GPD Pocket 2 live media.
    * The workaround is to wait and the system will boot after a few seconds or press <kbd>Enter</kbd> to boot immeditately.
    * However, **GRUB is fully functional and usable post-install**.

### GPD Pocket & GPD Pocket 2

  * The Plymouth splash screen is not rotated on the GPD Pocket or GPD Pocket 2.
    * The workaround is to not care.

<div class="bs-component">
  <div class="jumbotron">
    <h1>Download</h1>
      <p>Run Ubuntu MATE on your GPD Pocket or GPD Pocket 2 today!</p>
      <a href="/download/" class="btn btn-primary btn-lg">Download Ubuntu MATE</a>
      </p>
    </div>
</div>

## Disable desktop session scaling

If you want to restore the full native resolution of display then open
*Startup Applications* from the *Control Center*. Find the entry called
*GPD Pocket Display Scaler* in the *Startup Programs* tab and untick it.
Log out and back in and the full 1920x1200 resolution is restored.

<div align="center">
  <img src="/gallery/blog/gpd-pocket-display-scaler.png" /></a><br />
  <b>Disable GPD Pocket Display Scaler via Startup Applications Preferences</b>
</div>
<br />

## How were these images created?

With a script called `gpd-pocket-ubuntu-respin.sh` which you can find in the 
following GitHub repository:

  * <https://github.com/wimpysworld/gpd-pocket2-ubuntu>

## Accessing GPD boot menus

### GPD Pocket

Switch the GPD Pocket on, immediately hold the <kbd>Fn</kbd> key and tapping the <kbd>F7</kbd> key until the Boot Manager screen appears.

### GPD Pocket 2

Switch the GPD Pocket 2 on, immediately hold the <kbd>Fn</kbd> key and tapping the <kbd>F12</kbd> key until the Boot Manager screen appears.

## Feedback

These images for the GPD Pocket and GPD Pocket 2 are community supported,
please post all feedback via the [community forum](https://ubuntu-mate.community/).