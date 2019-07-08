---
layout: blog-post
title: Ubuntu MATE 15.10 Beta 2
permalink: ubuntu-mate-wily-beta2
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE Wily Werewolf (15.10) for distribution on 
[October 22nd, 2015](https://wiki.ubuntu.org/WilyWerewolf/ReleaseSchedule)
With this *Beta 2* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Beta Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who needs a stable system
  * Anyone uncomfortable running a possibly frequently broken system
  * Anyone in a production environment with data or workflows that need to be reliable

Ubuntu MATE *Beta Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE, and GTK+ developers

## What changed since the Ubuntu MATE 15.10 Beta 1 release?

Here's what changed in Ubuntu MATE 15.10 since Beta 1. 

  * Migration MATE 1.10 is complete.
    * Atril now supports ePub.
    * MATE Sensors Applet now supports NVIDIA GPUs.
    * For more details see the [MATE 1.10 Release Notes](http://mate-desktop.org/blog/2015-06-11-mate-1-10-released/).
  * Added Lightning Calendar plugin to Thunderbird, including Google calendar support.
  * Added new community contributed ["Keep Calm" wallpaper](http://timapple.com/ubuntu-mate-wallpaper/) by [Tim Apple](http://timapple.com/).
  * Updated Blueman to 2.0 - Manys thanks to the [Xubuntu](http://xubuntu.org) team for helping with this.
    * Now uses BlueZ 5.34.
    * Brings many Bluetooth improvements and fixes.
  * Updated Plank to 0.10 - Now has icon zooming and improved window dodging.
  * Update Galculator to 2.14 - Fixes [LP: 1474571](https://bugs.launchpad.net/ubuntu-mate/+bug/1474571)
  * Updated [Ubuntu MATE Welcome](https://ubuntu-mate.community/t/ubuntu-mate-welcome-screen/1616) to 1.0.3.3
    * Correct the category Ubuntu MATE Welcome is listed under.
    * Highlight the Software button.
    * Added Asunder.
    * Added FileZilla.
    * Added Iced Tea (Java) browser plugin.
    * Added Pulse Audio Volume Control.
    * Added Rapid Photo Downloader.
    * Added SuperTuxKart.
    * Update text for GIMP to mention that CMYK plug-ins are included.
  * Workaround for [Marco crashing on some IGPs](https://bugs.launchpad.net/ubuntu-mate/+bug/1495313).
    * A proper fix is available upstream and will be made available as an update soon.
  * Fixed `python-caja`. Caja Plugins were completely broken.
    * [LP: 1496925](https://bugs.launchpad.net/ubuntu/+source/python-caja/+bug/1496925)

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 15.10 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/wily/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

Here are the known issues.

  * Upgrading from Ubuntu MATE 15.04 to 15.10 does not work reliably.
    * A patch for this is pending and will be included in the October
    15th release candiate.
    * [LP: 1499078](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/1499078)
  * Depending on your location Ubiquity may trigger an `ubi-timezone` error.
    * The work around is to install without an active network connection. This affects all flavours.
    * [LP: 1462688](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1462688)
  * The menu used in the openSUSE panel layout crashes.
    * This is fixed upstream and an update for GNOME Main Menu will be published soon.
  * Using CTRL-Z in Caja to undo file/folder deletion will cause Caja to crash.
    * This is fixed upstream and an update for Caja will be published soon.
    * [LP: 1490161](https://bugs.launchpad.net/ubuntu-mate/+bug/1490161)
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
