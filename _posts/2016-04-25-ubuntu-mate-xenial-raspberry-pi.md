---
layout: blog-post
class: blog
title: Ubuntu MATE 16.04 for Raspberry Pi 2 and Raspberry Pi 3
permalink: /blog/ubuntu-mate-xenial-raspberry-pi/
description: Ubuntu MATE 16.04 LTS (Xenial Xerus) for Raspbery Pi 2 and Raspberry Pi 3.
category: release
author: Martin Wimpress
lang: en
discourse_topic_id: 21310
---

Ubuntu MATE 16.04 images for the Raspberry Pi 2 and Raspberry Pi 3 are
now available for download.

{% include blog/jumbotron.html
    title = "Download"
    text = "Download Ubuntu MATE for the Raspberry Pi 2 Model B and Raspberry Pi 3 Model B."
    button_text = "Download"
    button_url = "/ports/raspberry-pi/"
%}

The image is built from the regular Ubuntu `armhf` base, not the new
[Snappy Ubuntu](https://ubuntu.com/core), which means
that the installation procedure for applications is the same as that for
the regular desktop versions ie using `apt-get`. However, since
Ubuntu MATE 16.04 snap packages can be installed alongside classic deb
packages.

We have done what we can to optimise the build for the Raspberry Pi 2 and
Raspberry Pi 3, you can comfortably use applications such as LibreOffice and
Firefox. Ubuntu MATE 16.04 also has **fully working Bluetooth and Wifi on the
Raspberry Pi 3**. You'll need a microSD card which is **8GB** or greater, the
file system can be automatically resized to use the unallocated space of the
microSD card via Ubuntu MATE Welcome. But the microSDHC I/O throughput is a
bottleneck so **we *highly* recommend that you use a Class 6 or Class 10
microSDHC** card. The 16.04 release is also the first to feature **hardware
accelerated video playback in VLC and ffmpeg**.

{:.center}
![Ubuntu MATE 16.04 running on the Raspberry Pi 3](/images/blog/Screenshots/09_raspberrypi.png)
**Ubuntu MATE 16.04 running on the Raspberry Pi 3.**

## Changes

### 2016-04-24 - 16.04 Final Release for Raspbery Pi 2 and Raspberry Pi 3

  * Added **OpemMAX IL hardware accelerated video playback to VLC**.
    * To enable hardware accelerated video playback go to `Tools` -> `Preferences` -> `Video` and select `OpenMax IL`.
  * Added **MMAL hardware accelerated video playback to ffmpeg**.
    * To use hardware accelerated video playback with `ffplay` you must specify the `h264_mmal` codec - `ffplay -vcodec h264_mmal video.mp4`
  * Increased the **minimum microSDHC card size to 8GB**.
  * Removed `tboplayer`.

### 2016-04-05 - 16.04 Beta 2 for Raspberry Pi 2 and Raspberry Pi 3

  * Updated to Ubuntu MATE 16.04 including the new Welcome which comes with Raspberry Pi specific features.
  * Updated BlueZ 5.37 with patches to support the Raspberry Pi 3 integrated Bluetooth.
    * Ubuntu MATE 16.04 now supports the on-board Raspberry Pi 3 Bluetooth and Wifi.
  * Updated to Linux 4.1.19.
  * Updated to `raspberrypi-firmware` 1.20160315-1.
  * Updated to `omx-player` 0.3.7~git20160206~cb91001.
  * Updated to `wiringpi` 2.32.
  * Updated to `nuscratch` 20160115.
  * Updated to `sonic-pi` 2.9.0.
  * Migrated configuration tweaks to `raspberrypi-general-mods` and `raspberrypi-sys-mods`.
  * Experimental hardware accelerated OpenGL can be enabled, *if you know how* `;-)`

## Known Issues

  * During first boot configuration Ubiquity does not prompt to join available WiFi networks.
    * [#1572793](https://bugs.launchpad.net/bugs/1572793)
  * Upon completion of the first boot setup WiFi doesn't work, at all. Reboot and WiFi will be available.
    * [#1572956](https://bugs.launchpad.net/bugs/1572956)

Both these issues will be addressed in Ubuntu MATE 16.04.1 for Raspberry Pi 2
and 3 which is due in late July.
