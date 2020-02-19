---
layout: blog-post
class: blog
title: Ubuntu MATE 16.04.2 for Raspberry Pi 2 and Raspberry Pi 3
peramlink: /blog/ubuntu-mate-xenial-point-2-raspberry-pi/
description: Ubuntu MATE 16.04.2 LTS (Xenial Xerus) for Raspbery Pi 2 and Raspberry Pi 3.
category: release
author: Martin Wimpress
lang: en
---

An Ubuntu MATE 16.04.2 image for the Raspberry Pi 2 and Raspberry Pi 3 is now
available for download.

{% include blog/jumbotron.html
    title = "Download"
    text = "Download Ubuntu MATE for the Raspberry Pi 2 Model B and Raspberry Pi 3 Model B."
    button_text = "Download"
    button_url = "/download/"
%}
The image for the Raspberry Pi 2 and Raspberry Pi 3 based on the regular
Ubuntu `armhf` base, not the new [Ubuntu *"Snappy"*
Core](https://www.ubuntu.com/core), which means that the installation
procedure for applications uses the traditional tools, ie `apt-get`.

We have done what we can to optimise the build for the Raspberry Pi 2 and
Raspberry Pi 3, you can comfortably use applications such as LibreOffice,
which in fact is a joy to use :-) But the microSDHC I/O throughput is a
bottleneck so **we *highly* recommend that you use a Class 6 or Class 10
microSDHC** card. **Ubuntu MATE 16.04 also fully support the built-in
Bluetooth and Wifi on the Raspberry Pi 3** and also **feature **hardware
accelerated video playback in VLC and hardware accelerated decoding and
encoding in ffmpeg**

{:.center}
![Ubuntu MATE 16.04.2 running on the Raspberry Pi 3](/images/blog/Screenshots/09_raspberrypi.png)
**Ubuntu MATE 16.04.2 running on the Raspberry Pi 3**

## Changes

These are the changes since Ubuntu MATE 16.04 for the Raspberry Pi was release.

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
    * SSH can be enabled via `raspbi-config` or creating a file named `ssh` in the `/boot` partition.
    * `sshguard` is also automatically enabled when you enable SSH.
  * Reduced the image size to 5GB, down from 8GB.

## Known Issues

  * **Ubuntu MATE 16.04.2 for the Raspberry Pi is not snap compatible.**
    * We hope to have `snapd` compatibility in Ubuntu MATE 17.04 for the Raspberry Pi.
    * The 32-bit and 64-bit PC version of Ubuntu MATE 16.04, or newer, are `snapd` compatible.
  * Upon completion of the first boot setup WiFi doesn't work, at all. Reboot and WiFi will be available.
    * [#1572956](https://bugs.launchpad.net/bugs/1572956)

{% include blog/jumbotron.html
    title = "More Information"
    text = "Find out more about Ubuntu MATE for Raspberry Pi 2 Model B and Raspberry Pi 3 Model B."
    button_text = "Read more"
    button_url = "/raspberry-pi/"
%}
