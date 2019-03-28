<!--
.. title: Ubuntu MATE for the Raspberry Pi Model B 2, 3 and  3+
.. slug: raspberry-pi
.. date: 2015-04-21 23:01:09 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,Model B,Raspberry Pi 2,Raspberry Pi 3,Raspberry Pi 3+,download,armhf,arm64,ARMv7,ARMv8
.. link:
.. description: Ubuntu MATE 18.04 for the Raspberry Pi 2 and Raspbery Pi 3
.. type: text
.. author: Martin Wimpress
-->

The images are functional and based on Ubuntu 18.04.2 for `armhf` (ARMv7 32-bit)
and `amd64` (ARMv8 64-bit). We have done what we can to optimise the build for
the Raspberry Pi without sacrificing the full desktop environment Ubuntu MATE
provides on PC. High-level features of these images are:

  * Ubuntu kernel, fully maintained by the Ubuntu Kernel and Security teams.
  * Automatic online filesystem expansion.
  * Ethernet
  * WiFi (*where available*)
  * Bluetooth (*where available*)
  * GPIO
  * Audio
  * HDMI
  * USB Booting
  * Hardware acceleration:
    * `fbturbo` driver is pre-installed but limited to 2D accelerated window moving/scrolling on Raspberry Pi (using the BCM2835 DMA Controller).
    *  VLC
    *  `ffmpeg`
    * The *experimental* VC4 driver can be enabled via `raspi-config`.
    * Please note, the `arm64` images do not feature any VideoCore IV hardware acceleration.
  * Additional software:
    * A port of `raspi-config` for Ubuntu is pre-installed.
    * Steam Link is available for install.
    * Minecraft Pi Edition is available for install.

<div align="center">
  <img src="/assets/img/misc/raspberry-pi-screenshot.jpg" /></a><br />
  <b>Ubuntu MATE running on the Raspberry Pi 3+</b>
</div>
<br />

## Supported Raspberry Pi

  * These images will work on:
    * [Raspberry Pi 2 Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)
    * [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
    * [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) **(recommended)**

  * These images *kind of* work on:
    * [Raspberry Pi 3 Model A+](https://www.raspberrypi.org/products/raspberry-pi-3-model-a-plus/) **(not recommended)**
      * Fails to complete the first boot setup due to insufficnent memory.
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

<div align="center"><a href="https://geni.us/AKAsg" target="_blank"><img src="/assets/img/misc/SamsungEvoPlus.jpg" alt="Samsung 32GB 95MB/s Memory Evo Plus Micro SD Card with Adapter" style="width:200px;"/></a></div>

You'll need a microSD card which is **8GB** or greater to fit the image.
The file system will automatically resize to occupy the unallocated
space of the microSD card.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download</h1>
        <p>Run Ubuntu MATE on your Raspberry Pi Model B 2, 3 or 3+ today.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download Ubuntu MATE</a>
        </p>
    </div>
</div>

## Making a microSDHC or USB

The image can be directly written to a microSDHC or USB stick using a utility like
`dd`, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue),
for example:

    sudo apt-get install gddrescue xz-utils
    unxz ubuntu-mate-18.04.2-beta1-desktop-armhf+raspi-ext4.img.xz
    sudo ddrescue -D --force ubuntu-mate-18.04.2-beta1-desktop-armhf+raspi-ext4.img.xz /dev/sdx

The microSDHC or USB stick may be presented on any `/dev/sdX` so use the command
`lsblk` to check.

<div align="center">
<script type="text/javascript" src="https://asciinema.org/a/34243.js" id="asciicast-34243" async></script>
</div>

If you prefer a graphical tool we recommend using [GNOME
Disks](apt://gnome-disk-utility) and the *Restore Disk Image...*
option, **which natively supports XZ compressed images**.

    sudo apt-get install gnome-disk-utility

<div align="center">
<iframe width="640" height="480" src="https://www.youtube.com/embed/V_6GNyL6Dac?html5=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>

### Making a microSDHC or USB stick with Windows

If you want to make a microSDHC using Windows we recommend:

  * [7-Zip](http://www.7-zip.org/) to extract the image.
  * [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) to write the image.

## Additional features

### USB Booting

The Ubuntu MATE 18.04.2 images for the Raspberry Pi support USB booting.

The Raspberry Pi 3, 3+ and Pi 2 v1.2 with the same BCM2837 SoC as the Pi 3,
are capable of booting from a USB drive. For the Pi 2 and 3 you'll first
need to [program USB boot mode](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md),
this is unnecessary on the Pi 3+ as USB booting is enabled by default.

### Re-size file system

The root parition is automatically resized, on first boot, to fully utilise
the all available space on the microSD card or USB stick. No reboots required.

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

The OpenSSH server is disabled by default. If you want to enable SSH you can
use `raspi-config` to created a file call `ssh` in to `/boot` paritition and
reboot.

When you enable SSH via either method explained above `sshguard` will
also be enabled.

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
It is based on an old version of Minecraft Pocket Edition and offer language
bindings for Python.

Can be installed via `sudo apt install minecraft-pi`

You can learn more about how to control the player, manually build with blocks
and use the Python interface to manipulate the world around you from the Raspberry Pi Foundation.

  * [Getting Started with Minecraft Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi)

### Enable and Disable X11

You can disable/enable the desktop environment using `raspi-config`.

If you only intended to run as a headless server then the official Ubuntu Server 18.04.2 images mightt be of interest:

  * https://wiki.ubuntu.com/ARM/RaspberryPi

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

### Ubunttu MATE 18.04.2  - March 5th, 2019

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

### Ubunttu MATE 18.04.2 Alpha 1 - March 2nd, 2019

  * Initial Ubuntu MATE 18.04.2 images made available for private testing.

### Previous Changes

  * [See what changed in earlier releases.](/raspberry-pi-change-log/)

## Known Issues

  * Empty panel on first boot. This is an intermittent issue with Ubuntu MATE when running on slower computers.
    * The workaround in to start a terminal with `Ctrl` + `Alt` + `t` abd reset the default Familiar layout using `mate-tweak --layout familiar`
  * Kernel panic when shutting down after initial setup
    * The worksround is to disconnect the power and reconnect it again. Everything will be fine `:-)`

## TODO

  * Build and publish a Raspberry Pi optimised web browser.
  * Add Python modules for popular HATs and peripherals to the archive.

## Feedback and Improvements

Thse images are not an official Ubuntu products and are community supported.
Please post all feedback and issues on the [dedicated community
forum](https://ubuntu-mate.community/c/support/raspberry-pi-2).