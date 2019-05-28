<!--
.. title: Ubuntu MATE 18.04 Beta 1 for Raspberry Pi
.. slug: ubuntu-mate-bionic-beta1-raspberry-pi
.. date: 2019-03-29 14:25:00 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,Model B,Raspberry Pi 2,Raspberry Pi 3,Raspberry Pi 3+,download,armhf,arm64,ARMv7,ARMv8,beta1
.. link: https://ubuntu-mate.org/raspberry-pi/
.. description: Ubuntu MATE 18.04 Beta-1 for the Raspberry Pi Model B 2, 3 and  3+
.. type: text
.. author: Martin Wimpress
-->

We are preparing **Ubuntu MATE 18.04 (Bionic Beaver) for the Raspberry Pi**.
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<div align="center">
  <img src="/gallery/Screenshots/09_raspberrypi.png" /></a><br />
  <b>Ubuntu MATE running on the Raspberry Pi 3+</b>
</div>
<br />

Ubuntu MATE 18.04 Beta 1 is available for Raspberry Pi Model B 2, 3 and 3+,
with separate images for  `armhf` (ARMv7 32-bit) and `arm64` (ARMv8 64-bit).
We have done what we can to optimise the builds for the Raspberry Pi without
sacrificing the full desktop environment Ubuntu MATE provides on PC.
High-level features of these images are:

  * Ubuntu kernel, fully maintained by the Ubuntu Kernel and Security teams.
  * Automatic online filesystem expansion.
  * Ethernet & WiFi (*where available*)
  * Bluetooth (*where available*)
  * Audio out via 3.5mm analog audio jack or HDMI
  * Video out via Composite or HDMI
  * GPIO access via [GPIO Zero](https://gpiozero.readthedocs.io), [pigpio](http://abyz.me.uk/rpi/pigpio/) and [WiringPi](http://wiringpi.com/).
  * Support for [Python Wheels for the Raspberry Pi](https://www.piwheels.org/).
  * Support for [USB Booting](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md).
  * Hardware acceleration:
    * `fbturbo` driver is pre-installed but limited to 2D accelerated window moving/scrolling on Raspberry Pi (using the BCM2835 DMA Controller).
    *  VLC has hardware assisted video decoding.
    *  `ffmpeg` has hardware assisted video decoding and encoding.
    * The *experimental* VC4 driver can be enabled via `raspi-config`.
    * Please note, the `arm64` images do not feature any VideoCore IV hardware acceleration.
  * Additional software:
    * A port of [`raspi-config` for Ubuntu](https://github.com/flexiondotorg/raspi-config/) is pre-installed.
    * [Steam Link](https://support.steampowered.com/kb_article.php?ref=6153-IFGH-6589) is available for install.
    * [Minecraft: Pi Edition](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi) is available for install.

<div class="bs-component">
    <div class="jumbotron">
        <h1>More Information</h1>
        <p>Find out more about Ubuntu MATE for Raspberry Pi Model B 2, 3, and 3+</p>
        <a href="/raspberry-pi/" class="btn btn-primary btn-lg">Read more</a>
    </div>
</div>

## Supported Raspberry Pi

  * These images will work on:
    * [Raspberry Pi 2 Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)
    * [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
    * [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) **(recommended)**

  * These images *kind of* work on:
    * [Raspberry Pi 3 Model A+](https://www.raspberrypi.org/products/raspberry-pi-3-model-a-plus/) **(not recommended)**
      * Fails to complete the first boot setup due to insufficient memory.
      * If you have completed the setup on another Pi that card can be inserted in a Pi 3 Model A+ and it will work.
      * Due to only having 512MB RAM the `arm64` is not recommended. The `armhf` version can be very tight on resources.

## Unsupported Raspberry Pi

  * These images **will not work on** any Raspberry Pi model using an ARMv6 instruction set:
    * [Raspberry Pi 1 Model A+](https://www.raspberrypi.org/products/raspberry-pi-1-model-a-plus/)
    * [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/raspberry-pi-1-model-b-plus/)
    * [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/)
    * [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)

## Recent Changes

### Ubuntu MATE 18.04.2 Beta 1 - March 24th, 2019

  * Fixed EGL/GLES/OpenVG libraries for VideoCore IV.
  * Fixed Raspberry Pi features in Ubuntu MATE Welcome.
  * Added hardware accelerated VLC (`armhf` only).
  * Added hardware accelerated ffmpeg (`armhf` only).
  * Enabled piwheels.
  * Reduced boot time, after the initial first boot setup has been completed, by ~3 seconds.
  * Uploaded SteamLink (`armhf` only) to the archive, not pre-installed.
  * Uploaded Minecraft Pi Edition (`armhf` only) to the archive, not pre-installed.
  * Raspberry Pi 3 Model A+ confirmed working, *kind of*.

### Ubuntu MATE 18.04.2 - March 5th, 2019

  * Fixed HDMI audio quality.
  * Fixed USB booting.
  * Fixed font caches.
  * Added pre-seeded snaps.
  * Added miscellaneous Raspberry Pi utilities.
  * Added EGL/GLES/OpenVG libraries for VideoCore IV.
  * Enabled splash screen.
  * Improved window manager responsiveness.
  * Reduced idle RAM consumption by ~30MB on arm64 and ~10MB on armhf.
  * Switched to the CFQ scheduler.

### Ubuntu MATE 18.04.2 Alpha 1 - March 2nd, 2019

  * Initial Ubuntu MATE 18.04.2 images made available for private testing.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download</h1>
        <p>Run Ubuntu MATE on your Raspberry Pi Model B 2, 3 or 3+ today.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download Ubuntu MATE for the Pi</a>
        </p>
    </div>
</div>

## Feedback and Improvements

Thse images are not official Ubuntu products and are community
supported by the Ubuntu MATE team. Please post feedback and
issues on the [dedicated community forum](https://ubuntu-mate.community/c/support/raspberry-pi-2).