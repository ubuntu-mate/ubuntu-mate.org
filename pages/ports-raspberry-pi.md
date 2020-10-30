---
layout: page-category
permalink: /ports/raspberry-pi/
lang: en
category: ports

title: Raspberry Pi

---

# Ubuntu MATE for Raspberry Pi

Ubuntu MATE 20.04 is available for Raspberry Pi with separate images for
`armhf` (ARMv7 32-bit) and `arm64` (ARMv8 64-bit). We have done what we can to
optimise the builds for the Raspberry Pi without sacrificing the full desktop
environment Ubuntu MATE provides on PC.

Ubuntu MATE for the Raspberry Pi provides a complete, familiar, desktop environment
that can be used for basic desktop computing. It is also of interest to makers and
device hackers who want to target [Ubuntu](https://ubuntu.com) for their projects.
You can prototype homebrew ARMv7 or ARMv8 based IoT devices in a comfortable desktop
environment, including building and testing your apps as [snaps](https://snapcraft.io).
The full Ubuntu archive is available to you.

For hobbyist projects, you can stick with Ubuntu MATE for "deployment". But, if
you have something more professional in mind then the applications and snaps you've
prototyped with Ubuntu MATE can be used with [Ubuntu Server](https://ubuntu.com/download/raspberry-pi)
or [Ubuntu Core](https://www.ubuntu.com/core). You might want to check out the
[Ubuntu Appliance Portfolio](https://ubuntu.com/appliance) too.

## Features

High-level features of these images are:

  * Ubuntu kernel.
    * Performance optimised by the Ubuntu Kernel team.
    * Regularly security patches by the Ubuntu Security team.
  * VC4/V3D (fkms) driver is enabled by default.
    * `fbturbo` driver is available if you want it, but limited to 2D accelerated window moving/scrolling on Raspberry Pi (using the BCM2835 DMA Controller).
  * Automatic online filesystem expansion.
  * Ethernet & WiFi (*where available*)
  * Bluetooth (*where available*)
  * Audio out via 3.5mm analog audio jack or HDMI
  * Video out via Composite or HDMI
  * GPIO access via [GPIO Zero](https://gpiozero.readthedocs.io) and [WiringPi](http://wiringpi.com/).
  * Support for [USB Booting](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md) is available for Ubuntu MATE 20.10 or newer.
  * Automatic first-boot file system resizing.
  * First-boot setup wizard guides you through creating a user account and configuring WiFi.

<!--
  * Hardware acceleration:
    *  `ffmpeg` has hardware assisted video decoding and encoding.
    *  VLC has hardware assisted video decoding.
  * Additional software:
    * [Steam Link](https://support.steampowered.com/kb_article.php?ref=6153-IFGH-6589) is available for install.
    * [Minecraft: Pi Edition](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi) is available for install.
-->

{:.center .small}
![Ubuntu MATE running on the Raspberry Pi 4](/images/ports/09_raspberrypi.png)
**Ubuntu MATE running on the Raspberry Pi 4**

## Supported Raspberry Pi

  * These images work on:
    * [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) **(recommended)**
    * [Compute Module 4](https://www.raspberrypi.org/products/compute-module-4/?variant=raspberry-pi-cm4001000) in a [Compute Module 4 IO Board](https://www.raspberrypi.org/products/compute-module-4-io-board/) **(recommended)**
      * A **Raspberry Pi 4 and Compute Module 4 with 2GB RAM or more** offers the best experience.
    * [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) **(not recommended)**
      * With just 1GB of RAM, everything works but desktop use is hampered by memory pressure.

## Unsupported Raspberry Pi

  * These images *kind of* work on:
    * [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) **(not recommended)**
    * [Raspberry Pi 3 Model A+](https://www.raspberrypi.org/products/raspberry-pi-3-model-a-plus/) **(not recommended)**
    * [Raspberry Pi 2 Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/) **(not recommended)**
      * Fails to complete the first boot setup due to insufficient memory.
      * If you have completed the setup on another Pi that card can be inserted in a Pi 3 Model A+ and it will work.
      * Due to only having 512MB RAM the `arm64` is not recommended; even the `armhf` version can be very tight on resources.

  * These images **will not work on** any Raspberry Pi model using an ARMv6 instruction set:
    * [Raspberry Pi 1 Model A+](https://www.raspberrypi.org/products/raspberry-pi-1-model-a-plus/)
    * [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/raspberry-pi-1-model-b-plus/)
    * [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/)
    * [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)

Memory pressure is reasonable using the `armhf` images (~350MB at idle)
but quite tight on the `arm64` images (~490MB at idle). As always,
microSDHC I/O throughput is a bottleneck on the Raspberry PPi so don't
gimp your Raspberry Pi by cheaping out on poor performing microSDHC
cards. We used the [Samsung EVO Plus 32 GB microSDHC UHS-I U1](https://geni.us/AKAsg)
and [Kingston 64 GB microSDXC Canvas Go Plus](https://geni.us/Jelmu)
during the testing of these images and they significantly better
performance than most other microSDHC cards we've tried.
[But don't take our word for it](https://www.pidramble.com/wiki/benchmarks/microsd-cards).

You'll need a microSD card which is **8GB** or greater to fit the image.
The file system will automatically resize to occupy the unallocated
space of the microSD card. Here is our recommended kit lists on Amazon:

### Raspberry Pi 4 with 8GB RAM

{:.transparent .icons}
|Raspberry Pi 4 8GB RAM|Argon One Case|SanDisk Extreme 128 GB microSDXC|
|[![Raspberry Pi 4 8GB RAM](/images/ports/pi4-8GB.jpg)](https://geni.us/QjSiQA6)|[![Argon One Case](/images/ports/argon-one.webp)](https://geni.us/lvbbi8n)|[![SanDisk Extreme 128 GB microSDXC](/images/ports/SanDiskExtreme.jpg)](https://geni.us/oRQKPJ)|

### Raspberry Pi 4 with 4GB RAM

{:.transparent .icons}
|Raspberry Pi 4 4GB RAM|Argon NEO Case|Kingston 64 GB microSDXC Canvas Go Plus|
|[![Raspberry Pi 4 4GB RAM](/images/ports/pi4-4GB.webp)](https://geni.us/wKRpG)|[![Argon NEO Case](/images/ports/argon-neo.webp)](https://geni.us/DcxV)|[![Kingston 64 GB microSDXC Canvas Go Plus](/images/ports/KingstonCanvasGoPlus.webp)](https://geni.us/Jelmu)|

### Raspberry Pi 4 with 2GB RAM

{:.transparent .icons}
|Raspberry Pi 4 2GB RAM|Flirc Case|Samsung EVO Plus 32 GB microSDHC UHS-I U1|
|[![Raspberry Pi 4 2GB RAM](/images/ports/pi4-2GB.webp)](https://geni.us/GN70L)|[![Flirc Case](/images/ports/flirc.jpg)](https://geni.us/QvssBp)|[![Samsung EVO Plus 32 GB microSDHC UHS-I U1](/images/ports/SamsungEvoPlus.png)](https://geni.us/AKAsg)|

{% include blog/jumbotron.html
    title = "Download"
    text = "Run Ubuntu MATE on your Raspberry Pi today."
    button_text = "Download"
    button_url = "/download/"
%}

## Additional features

### USB Booting

Ubuntu MATE 20.10 and newer support USB booting, **but Ubuntu MATE 20.04 does not**.

### Compute Module 4

If you have a [Compute Module 4](https://www.raspberrypi.org/products/compute-module-4/?variant=raspberry-pi-cm4001000)
you can enable the USB2 outputs on the [Compute Module 4 IO Board](https://www.raspberrypi.org/products/compute-module-4-io-board/),
assuming your Compute Module is plugged into such a board, by un-commenting the following line in
`/boot/firmware/config.txt`.

    #dtoverlay=dwc2,dr_mode=host

#### Enable USB boot for Raspberry Pi 4

To enable USB mass storage boot on a Raspberry Pi 4 follow these steps:

  * [Enable optional USB boot on Raspberry Pi 4](https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4#4-optional-usb-boot)

### Enable USB boot for Raspberry Pi 2, 3 and 3+

The Raspberry Pi 3, 3+ and Pi 2 v1.2 with the same BCM2837 SoC as the Pi 3,
are capable of booting from a USB drive. For the Pi 2 and 3 you'll first
need to [program USB boot mode](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md),
this is unnecessary on the Pi 3+ as USB booting is enabled by default.

### Firmware

The GPU firmware partition is mounted at `/boot/firmware`. The files
`/boot/firmware/config.txt` and `/boot/firmware/cmdline.txt` contain
the system configuration and kernel command line options respectively.

### SSH

The OpenSSH server is not installed by default. Simply install it to
to enable SSH.

    sudo apt install openssh-server

If you install SSH then you might also want to install `sshguard`
which is highly optimised and well suited for use on the Raspberry Pi
to protect from brute force attacks against SSH.

    sudo apt install sshguard

<!--
### Steam Link for Raspberry Pi

The Steam Link app extends Steam Link functionality to the Raspberry Pi
Model B 3 and 3+ and uses the same streaming technology as Valve's
Steam Link, allowing you to play your favorite games and even spectate
VR games right from your Raspberry Pi.

Can be installed via `sudo apt install steamlink`

You can learn more about Steam Link for Raspberry Pi from Valve:

  * [Steam Link App for Raspberry Pi](https://support.steampowered.com/kb_article.php?ref=6153-IFGH-6589)

### Minecraft: Pi Edition

Minecraft: Pi Edition is a cut down version of Minecraft for the Raspberry Pi.
It is based on an old version of Minecraft Pocket Edition and offers language
bindings for Python.

Can be installed via `sudo apt install minecraft-pi`

You can learn more about how to control the player, manually build with blocks
and use the Python interface to manipulate the world around you from the Raspberry Pi Foundation.

  * [Getting Started with Minecraft Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi)
-->

### Redirecting audio output

If you have issues with audio, you may try un-commenting the following line in `/boot/firmware/config.txt`:

    #hdmi_drive=2

This forces the HDMI output into HDMI mode instead of DVI; which doesn't support
audio output. You can also configure the system to output to a particular audio
device.

#### For HDMI

    sudo amixer cset numid=3 2

#### For 3.5mm audio jack

    sudo amixer cset numid=3 1

<!--
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
-->

## Recent Changes

### Ubuntu MATE 20.04.1 & 20.10 - October 30th 2020

  * Ubuntu MATE 20.10 is capable of USB boot.
  * Compute Module 4 support.
  * The `gpio`, `i2c`, `input` and `spi` groups are pre-created.
    * The user created using the first-boot wizard is automatically added to the groups above.
  * `cloud-init` is completely removed; file system expansion is handled by `cloud-initramfs-growroot` and the `x-systemd.growfs` mount option.
  * Snaps are initialized while the first-boot setup wizard runs.
  * Plymouth splash screen is displayed correctly during first-boot.
  * Serial console is disabled by default.
  * `gpu_mem` configured for 128MB by default.
  * `hdmi_drive` now defaults to DVI mode.

### Ubuntu MATE 20.04.1 Beta 2 - 13 August 2020

  * Re-based on Ubuntu MATE 20.04.1.
  * Fixed WiFi on first boot during the initial setup wizard.
  * Dropped `gpu_mem` from `config.txt` as the defaults should be sensible.

### Ubuntu MATE 20.04 Beta 1 - 12 July 2020

  * Re-based on Ubuntu MATE 20.04.
  * Added support for Raspberry Pi 4.
  * Enabled the VC4/V3D (fkms) driver by default.
  * Firefox uses Basic rendering by default.
    * Based on community feedback and our testing the OMTC (OpenGL) compositing video playback is choppy by comparison.
  * Added `rpi-eeprom`.
  * Minecraft: Pi Edition is still be packaged.
  * USB Booting is work in progress.
  * Dropped `raspi-config`; we have something else in the works...

### Previous Changes

  * [See what changed in earlier releases.](/ports/raspberry-pi-change-log/)

## Feedback and Improvements

These images are not official Ubuntu products and are community
supported by the Ubuntu MATE team. Please post feedback and
issues on the [dedicated community forum](https://ubuntu-mate.community/c/support/raspberry-pi).
