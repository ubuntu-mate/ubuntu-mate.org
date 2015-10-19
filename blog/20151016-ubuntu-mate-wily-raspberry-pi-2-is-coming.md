<!--
.. title: Ubuntu MATE 15.10 for Raspberry Pi 2 is coming
.. slug: ubuntu-mate-wily-for-raspberry-pi-2-is-coming
.. date: 2015-10-16 14:32:23 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,armhf
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

The Ubuntu MATE team have been working on a revised image for the
Raspberry Pi 2 based on Ubuntu MATE 15.10. It will be released on
October 22nd 2015.

The Raspberry Pi community have been generous with their donations to
Ubuntu MATE so we felt we really needed to improve Ubuntu MATE with
those people's requirements firmly in mind.

So we're sharing the feedback we've recieved about Ubuntu MATE 15.04
for the Raspberry Pi 2 and how we've (hopefully) improved the 15.10
release based on the that feedback.

<div align="center">
  <img src="/assets/img/logos/Raspi_Colour_R-207x250.png" /><br />
  <b>Ubuntu MATE 15.10 is coming to the Raspberry Pi 2 on October 22nd 2015</b>
</div>

## Makers

Talking to makers at Raspberry Jams, and online, it is clear they want
better *"out of the box"* GPIO support. Makers really like having access
to the extensive software repository that the Ubuntu base provides, but
miss some of the Raspberry Pi specific software.

The Ubuntu MATE desktop is popular with Makers as a full desktop
environment in which to develop and run graphical applications, but
sometimes the overhead of X11 and a full desktop is not desirable.

### Improvements for Makers

  * Added essential Python 2.7.x and Python 3.4.x libraries.
  * Added `raspi-gpio`.
  * Added `python-rpi.gpio` and `python3-rpi.gpio`.
  * Added `python-serial` and `python3-serial`.
  * Added `python-picamera` and `python3-picamera`.
  * Added `python-sense-hat` and `python3-sense-hat`.
  * Added `udev` rules for `gpio`, `input`, `i2c`, `spi2`, `vchiq`.
  * Added `/usr/local/sbin/adduser.local` hook to automatically add new users to the `adm`, `gpio`, `i2c`, `input`, `spi2` and `video` groups.
  * Added `openssh-server` with first-boot host key regeneration.
  * Added `graphical` a utility to disable/enable the MATE desktop environment for easily creating a headless *"server"*.

Most of the above has been ported and packaged in a PPA so updates can
be delivered automatically via the update manager. If we learn of new
Raspberry Pi specific software, that is in demand, we can port it and
add it to the PPA.

## Raspbian Tourists

Raspberry Pi users already familiar with Raspbian find the subtle
differences between Raspbian and Ubuntu MATE frustrating. For example,
being pinned to one kernel version, forever. For those who were able to
use `oem-config` (the first boot wizard) successfully, it was popular
but also very slow. Sadly for some, it was also extremely unreliable.
For others, they never got Ubuntu MATE to work at all `:-(`.

### Improvements for Raspbian Tourists

  * Removed `oem-config`.
    * First boot is much, much faster.
  * Included Ubuntu MATE Welcome.
    * Provides a Getting Started area for completing the initial system configuration, as a replacement for the `oem-config` wizard.
  * Updated to Linux 4.1.10.
    * The kernel, firmware and drivers are taken from the Raspberry Pi Foundation and `rpi-update` is included to easily update the kernel and firmware to the latest release.

## People new to Raspberry Pi

People entirely new to the Raspberry Pi community really like the
Ubuntu MATE desktop and how the interface can be changed to look
somewhat like Windows or Mac OS X. However, while Ubuntu MATE includes
a full office suite and many useful applications, users new to the
Raspberry Pi and Linux communities don't know how to install
applications to complete common tasks. They find the initial boot
screen *"scary"*. They mostly connect a screen via HDMI and are
frustrated that no audio is available via HDMI by default. We've heard
that last one from Makers too.

### Improvements for new Raspberry Pi users

  * Included Ubuntu MATE Welcome.
    * Provides Software area to easily find and install many best in class applications that intergrate well with Ubuntu MATE.
  * `/boot/config.txt` is now fully documented.
  * Fixed framebuffer so it now uses 32-bit colour depth.
  * When HDMI is connected audio is sent over HDMI by default.
  * Enabled Plymouth to improve startup and shutdown performance and make the initial boot screen less scary.

## Raspberry Pi for Children

Children really like the Ubuntu MATE desktop, but they have very sad
faces when they discover it doesn't include Scartch or Minecraft.

### Improvements for Children (and big children)

  * Added Minecraft Pi Edition 0.1.1-4 and its Python bindings.
  * Added Scratch 20150916 (nuscratch)
  * Added Sonic Pi 2.7.0-1.
  * Added `python-astropi` and `python3-astropi`.
  * Added `python-pygame`.

## Kodi users

We think it's great so many of you want to run [Kodi](http://kodi.tv/)
on Ubuntu MATE. But...

### Improvements for Kodi users

  * Use [OpenELEC](http://openelec.tv/) `;-)`
  * omxplayer is still included and we are hoping to include a GUI for it.

<small>We might, only with fair weather and following wind, make a Kodi build for Ubuntu MATE. But don't bet on it.</small>

## Thanks for sharing your thoughts

So there you have it, that's what you can expect in Ubuntu MATE 15.10
for the Raspberry Pi 2. Thank you all for talking to us at Raspberry
Jams and posting your feedback on the [Ubuntu MATE
community](https://ubuntu-mate.community). We really were listening.

A release candidate image has been sent off for final testing to our
crack team of, erm, testers. When Ubuntu MATE 15.10 for the Raspberry
Pi 2 is ready we'll update our [Ubuntu MATE for the Raspberry Pi
2](/raspberry-pi/) page. See you October 22nd `:-)`.
