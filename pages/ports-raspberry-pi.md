---
layout: page-category
permalink: /ports/raspberry-pi/
lang: en
category: ports

title: Raspberry Pi

---

# Ubuntu MATE for Raspberry Pi

Ubuntu MATE 18.04.2 is available for Raspberry Pi Model B 2, 3 and 3+ with separate
images for  `armhf` (ARMv7 32-bit) and `arm64` (ARMv8 64-bit). We have done what
we can to optimise the builds for the Raspberry Pi without sacrificing the full
desktop environment Ubuntu MATE provides on PC.

Ubuntu MATE for the Raspberry Pi provides a complete, familiar, desktop environment
that can be used for basic desktop computing. It is also of interest to makers and
device hackers who want to target [Ubuntu](https://ubuntu.com) for their projects.
You can prototype homebrew ARMv7 or ARMv8 based IoT devices in a comfortable desktop
environment, including building and testing your apps as [snaps](https://snapcraft.io).
The full Ubuntu archive is available to you.

For hobbyist projects, you can stick with Ubuntu MATE for "deployment", even
with the option to disable the X11 display server if it not an application
requirement. But, if you have something more professional in mind then the
applications and snaps you've prototyped with Ubuntu MATE can be used with Ubuntu
server or Ubuntu Core (https://www.ubuntu.com/core) on one of the ARM-based
reference platforms.

## Features

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


{:.center .small}
![Ubuntu MATE running on the Raspberry Pi 3+](/images/ports/09_raspberrypi.png)
**Ubuntu MATE running on the Raspberry Pi 3+**

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

Memory pressure is reasonable using the `armhf` images (~350MB at idle)
but quite tight on the `arm64` images (~490MB at idle). As always,
microSDHC I/O throughput is a bottleneck on the Raspberry PPi so don't
gimp your Raspberry Pi by cheaping out on poor performing microSDHC
cards. We used the [Samsung 32GB 95MB/s Memory Evo Plus microSDHC cards](https://geni.us/AKAsg)
during the testing of these images and they significantly better
performance than most other microSDHC cards we've tried.
[But don't take our word for it](https://www.pidramble.com/wiki/benchmarks/microsd-cards).

{:.center .small}
[![Samsung 32GB 95MB/s Memory Evo Plus Micro SD Card with Adapter](/images/ports/SamsungEvoPlus.jpg)](https://geni.us/AKAsg)

You'll need a microSD card which is **8GB** or greater to fit the image.
The file system will automatically resize to occupy the unallocated
space of the microSD card.


{% include blog/jumbotron.html

    title = "Download"
    text = "Run Ubuntu MATE on your Raspberry Pi Model B 2, 3 or 3+ today."
    button_text = "Download"

    button_url = "/download/"
%}


## Additional features

### USB Booting

The Ubuntu MATE 18.04.2 images for the Raspberry Pi support USB booting.

The Raspberry Pi 3, 3+ and Pi 2 v1.2 with the same BCM2837 SoC as the Pi 3,
are capable of booting from a USB drive. For the Pi 2 and 3 you'll first
need to [program USB boot mode](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md),
this is unnecessary on the Pi 3+ as USB booting is enabled by default.

### Re-size file system

The root parition is automatically resized, on first boot, to fully utilise
all the available space on the microSD card or USB stick. No reboots required.

### First boot

**NOTE! There are no predefined user accounts**. The first time you
boot the Ubuntu MATE image it will run through a setup wizard where you
can create your own user account and configure your regional settings.
The first boot setup takes a few minutes to complete, but subsequent
boots are much quicker.

### Firmware

The GPU firmware partition is mounted at `/boot/firmware`. The files
`/boot/firmware/config.txt` and `/boot/firmware/cmdline.txt` contain
the system configuration and kernel command line options respectively.
Ubuntu MATE 18.04.2 includes a port of `raspi-config` that supports
this location. These configuration files are also symlinked to `/boot/`
to hopefully support 3rd party tools and applications.

### SSH

The OpenSSH server is not installed by default. Simply install it to
to enable SSH.

    sudo apt install openssh-server

If you install SSH then you might also want to install `sshguard`
which is highly optimised and well suited for use on the Raspberry Pi to
protect from brute force attacks against SSH.

    sudo apt install sshguard

### Steam Link for Raspberry Pi

The Steam Link app extends Steam Link functionality to the Raspberry Pi
Model B 3 and 3+ and uses the same streaming technology as Valve's
Steam Link, allowing you to play your favorite games and even spectate
VR games right from your Raspberry Pi.

Can be installed via `sudo apt install steamlink`

You can learn more about Steam Link for Raspberry Pi from Valve:

  * [Steam Link App for Raspberry Pi](https://support.steampowered.com/kb_article.php?ref=6153-IFGH-6589)

### Minecraft Pi Edition

Minecraft: Pi Edition is a cut down version of Minecraft for the Raspberry Pi.
It is based on an old version of Minecraft Pocket Edition and offers language
bindings for Python.

Can be installed via `sudo apt install minecraft-pi`

You can learn more about how to control the player, manually build with blocks
and use the Python interface to manipulate the world around you from the Raspberry Pi Foundation.

  * [Getting Started with Minecraft Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi)

### Enable and Disable X11

You can disable/enable the desktop environment using `raspi-config`.

If you only intended to run as a headless server then the official Ubuntu Server 18.04.2 images might be of interest:

  * <https://wiki.ubuntu.com/ARM/RaspberryPi>

### Redirecting audio output

The sound will output to HDMI by default if both HDMI and the 3.5mm audio jack
are connected. You can, however, force the system to output to a particular
device using `raspi-config`.

For those of you who want to know how to do this without `raspi-config`:

#### For HDMI

    sudo amixer cset numid=3 2

#### For 3.5mm audio jack

    sudo amixer cset numid=3 1

### Hardware accelerated video

Most videos will play with hardware acceleration using VLC which
is pre-installed in Ubuntu MATE. To use hardware accelerated video playback
with `ffplay` you must specify the `h264_mmal` codec.

    `ffplay -vcodec h264_mmal video.mp4`

Hardware accelerated playback on the Raspberry Pi works by overlaying the
video directly to the screen. Therefore there are no onscreen controls for
playback control. You'll need to use the ffmpeg keyboard shortcuts.

  * [ffplay keyboard controls](https://ffmpeg.org/ffplay.html#toc-While-playing)

`ffmpeg` also offer hardware enabled video encoding via the `h264_omx` encoder. Here is an example:

    `ffmpeg -f video4linux2 -i /dev/video0 -s 1280x720 -c:v h264_omx output.mp4`

However if you have MPEG-2 or VC-1 video video files then **you will need MPEG-2
and/or VC-1 licenses from the [Raspberry Pi Store](http://www.raspberrypi.com/license-keys/)**.


## Recent Changes

### Ubuntu MATE 18.04.2 Beta 2 - WIP

  * Added Raspberry Pi specific applications to the Software Boutique.
    * Minecraft: Pi Edition
    * Steam Link
  * Disabled WiFi Power Management.
  * `openssh-server` no longer pre-installed.

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

### Previous Changes

  * [See what changed in earlier releases.](/ports/raspberry-pi-change-log/)

## Known Issues

  * Empty panel on first boot. This is an intermittent issue with Ubuntu MATE when running on slower computers.
    * The workaround in to start a terminal with `Ctrl` + `Alt` + `t` and reset the default Familiar layout using `mate-tweak --layout familiar`
  * Kernel panic when shutting down after initial setup
    * The worksround is to disconnect the power and reconnect it again. Everything will be fine `:-)`

## TODO

  * Build and publish a Raspberry Pi optimised web browser.
  * Add more Python modules for popular HATs and peripherals to the archive.

## Feedback and Improvements

These images are not official Ubuntu products and are community
supported by the Ubuntu MATE team. Please post feedback and
issues on the [dedicated community forum](https://ubuntu-mate.community/c/support/raspberry-pi).
