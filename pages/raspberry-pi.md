<!--
.. title: Ubuntu MATE for the Raspberry Pi 2 and Raspberry Pi 3
.. slug: raspberry-pi
.. date: 2015-04-21 23:01:09 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,Raspberry Pi 2,Raspberry Pi 3,download,armhf,arm64,ARMv7,ARMv8
.. link:
.. description: Ubuntu MATE 16.04 for the Raspberry Pi 2 and Raspbery Pi 3
.. type: text
.. author: Martin Wimpress
-->

Martin Wimpress and Rohith Madhavan have made an Ubuntu MATE image for the 
Raspberry Pi 2 and Raspberry Pi 3 based on the regular Ubuntu `armhf` base, 
not the new [Ubuntu *"Snappy"* Core](https://www.ubuntu.com/core), which means 
that the installation procedure for applications uses the traditional tools, 
ie `apt-get`.

We have done what we can to optimise the build for the Raspberry Pi 2
and Raspberry Pi 3, you can comfortably use applications such as
LibreOffice and Firefox. But the microSDHC I/O throughput is a
bottleneck so **we *highly* recommend that you use a Class 6 or Class
10 microSDHC** card. **Ubuntu MATE 16.04 also fully supports the
built-in Bluetooth and Wifi on the Raspberry Pi 3** and **features
hardware accelerated video playback in VLC and hardware accelerated
decoding and encoding in `ffmpeg`**

You'll need a microSD card that is **6GB** or greater. The file system
will be automatically resized, on first boot, to occupy the unallocated
space of the microSD card.

**NOTE! There are no predefined user accounts**. The first time you
boot it will run through a setup wizard where you can create your own
user account and configure your regional settings. The first boot is
quite slow but, once the configuration is complete, subsequent boots
are much quicker.

<div align="center">
  <img src="/gallery/Screenshots/09_RASPBERRY.png" /></a><br />
  <b>Ubuntu MATE 16.04 running on the Raspberry Pi 3.</b>
</div>
<br />

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download</h1>
        <p>Run Ubuntu MATE on your Raspberry Pi 2 or 3 today.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download Ubuntu MATE</a>
        </p>
    </div>
</div>

## Making a microSDHC

The image can be directly written to a microSDHC using a utility like
`dd`, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue),
for example:

    sudo apt-get install gddrescue xz-utils
    unxz ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz
    sudo ddrescue -D --force ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img /dev/sdx

The microSDHC may be presented on any `/dev/sdX` so use the command
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

### Making a microSDHC with Windows

If you want to make a microSDHC using Windows we recommend:

  * [7-Zip](http://www.7-zip.org/) to extract the image.
  * [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) to write the image.

## Re-size file system

Since Ubuntu MATE 16.04.2 the root parition is automatically resized,
to fully utilise the all available space on the microSD card, on first
boot.

## SSH

Since Ubuntu MATE 16.04.2 the OpenSSH server is disabled by default. If
you want to enable SSH you can use `raspi-config` to created a file
call `ssh` in to `/boot` paritition and reboot.

When you enable SSH via either method explained above `sshguard` will
also be enabled.

## Enable and Disable X11

Since Ubuntu MATE 16.04.2 you can disable/enable the desktop
environment using `raspi-config`.

## Redirecting audio output

The sound will output to HDMI by default if both HDMI and the 3.5mm audio jack
are connected. You can, however, force the system to output to a particular
device using `raspi-config`.

For those of you who want to know how to do this without `raspi-config`:

### For HDMI

    sudo amixer cset numid=3 2

### For 3.5mm audio jack

    sudo amixer cset numid=3 1

## Hardware accelerated video with omxplayer

Most videos will play with hardware acceleration using `omxplayer` which
is pre-installed in Ubuntu MATE. However if you have MPEG-2 or VC-1 video
video files then **you will need MPEG-2 and/or VC-1 licenses from the
[Raspberry Pi Store](http://www.raspberrypi.com/license-keys/)**.

### omxplayer audio redirection

Should you want to manually select the output audio deive with `omxplayer`
it can be acieved as follows:

#### omxplayer over HDMI

    omxplayer -o hdmi video.mp4

#### omcplayer over 3.5mm audio jack

    omxplayer -o local video.mp4

## Hardware accelerated video with VLC and ffmpeg

Ubuntu MATE 16.04 added OpemMAX IL hardware accelerated video playback to VLC
and MMAL hardware accelerated video playback to ffmpeg.

  * To enable hardware accelerated video playback in VLC go to `Tools` -> `Preferences` -> `Video` and select `OpenMax IL`.
  * To use hardware accelerated video playback with `ffplay` you must specify the `h264_mmal` codec.

    `ffplay -vcodec h264_mmal video.mp4`

Hardware accelerated playback on the Raspberry Pi works by overlaying the
video directly to the screen. Therefore there are no onscreen controls for
playback control. You'll need to use the VLC and ffmpeg keyboard shortcuts.

  * [VLC keyboard control](https://wiki.videolan.org/Hotkeys_table/)
  * [ffplay keyboard controls](https://ffmpeg.org/ffplay.html#toc-While-playing)

## Hardware accelerate video encoding with ffmpeg

Since Ubuntu MATE 16.04.2 `ffmpeg` is shipped with hardware enabled video
encoding via the `h264_omx` encoder. Here is an example:

    `ffmpeg -f video4linux2 -i /dev/video0 -s 1280x720 -c:v h264_omx output.mp4`

## Recent Changes

### 2017-02-16 - 16.04.2 Release for Raspbery Pi 2 and Raspberry Pi 3

  * Performance optimised.
    * Added automated first boot partition resizing.
    * Optimised partition offset calculations
    * Optimised filesystem features.
    * Disabled unnecessary services to reduce CPU cycles and RAM requirements.
  * Forked and adapted `raspi-config` to Ubuntu.
    * Added [pi-top](https://www.pi-top.com/) brightness and power-off support.
  * Backported MATE Desktop 1.16.1.
  * Backported BlueZ 5.41.
  * Backported `ffmpeg` 3.2 including Raspberry Pi hardware acceleration for MMAL decoding and OMX encoding.
  * Backported `i2c-tools` and `python-smbus` 3.1.2.
  * Updated `raspberrypi-firmware` to 1.20161215-1.
  * Updated `pi-bluetooth` to 0.1.2 including failsafe systemd units.
  * Updated `gpiozero` to 1.3.1. A simple API for controlling devices attached to the GPIO pins.
  * Updated `omxplayer` to 0.3.7-git20160923-dfea8c9.
  * Updated `nuscratch` to 20160915+2.
  * Updated `picamera` to 1.12. Pure Python interface to the Raspberry Pi's camera module.
  * Updated `pigpio` to 1.130. Library for Raspberry Pi GPIO control.
  * Updated `python-sense-hat` to 2.2.0. Sense HAT python.
  * Updated `raspberrypi-sys-mods` to 20170208, which completely replaces `raspberrypi-general-mods`
  * Updated `raspi-gpio` to 0.20170105. Dump the state of the BCM270x GPIOs.
  * Updated `rpi.gpio` to 0.6.3-1. Python GPIO module for Raspberry Pi.
  * Updated `rtimulib` to 7.2.1-3. Versatile C++ and Python 9-dof, 10-dof and 11-dof IMU library.
  * Updated `sonic-pi` to 2.10.0.
  * Updated `xserver-xorg-video-fbturbo` to 1.20161111~122359.
  * Updated Xorg via the [LTS Enablement Stack](https://wiki.ubuntu.com/Kernel/LTSEnablementStack).
  * Added cap1xxx; A python library designed to drive various Microchip CAP1xxx touch ICs.
  * Added drumhat; A python library designed to control Drum HAT.
  * Added envirophat; A python library designed to control Enviro pHAT.
  * Added explorerhat; A python library designed to control the Explorer HAT and pHAT.
  * Added microdotphat; A python library designed to control Micro Dot pHAT.
  * Added mote; A python library designed to control Mote.
  * Added motephat; A python library designed to control Mote pHAT.
  * Added pantilthat; A python library designed to control Pan-Tilt HAT.
  * Added pianohat; A python library designed to control Piano HAT.
  * Added piglow; A python library designed to drive Piglow.
  * Added rainbowhat; A python library designed to control Rainbow HAT.
  * Added scrollphat; A python library designed to control Scroll pHAT.
  * Added sense-emu; A client library for the Raspberry Pi Sense HAT emulator.
  * Added sn3218; A python library to help control the SN3218 18-channel PWM LED driver.
  * Added st7036; A python library to help control the ST7036 LCD driver.
  * Fixed first boot configuration. Ubiquity now prompts to join available WiFi networks.
    * [#1572793](https://bugs.launchpad.net/bugs/1572793)
  * Disabled SSH by default.
    * SSH can be enabled via `raspi-config` or creating a file named `ssh` in the `/boot` partition.
    * `sshguard` is also automatically enabled when you enable SSH.
  * Reduced the image size to 5GB, down from 8GB.

### Previous Changes

  * [See what changed in earlier releases.](/raspberry-pi-change-log/)

## Known Issues

  * **Ubuntu MATE 16.04.2 for the Raspberry Pi is not snap compatible.**
    * We hope to have `snapd` compatibility in Ubuntu MATE 17.04 for the Raspberry Pi.
    * The 32-bit and 64-bit PC version of Ubuntu MATE 16.04, or newer, are `snapd` compatible.
  * Upon completion of the first boot setup WiFi doesn't work, at all. Reboot and WiFi will be available.
    * [#1572956](https://bugs.launchpad.net/bugs/1572956)

## Feedback and Improvements

Please post all feedback on the [dedicated community
forum](https://ubuntu-mate.community/c/support/raspberry-pi-2). If you
have any improvements then please submit a pull request to the [Ubuntu
Pi Flavour Maker project](https://ubuntu-pi-flavour-maker.org/).

This image is not an official Ubuntu image, it is community supported, so any
bugs filed on the Ubuntu MATE Launchpad bug tracker will be closed with a
comment directing the report to the Ubuntu MATE forums :-)
