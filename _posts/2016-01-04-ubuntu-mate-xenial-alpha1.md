---
layout: blog-post
class: blog
title: Ubuntu MATE 16.04 Alpha 1
permalink: /blog/ubuntu-mate-xenial-alpha1
description: Ubuntu MATE 16.04 (Xenial Xerus) LTS Alpha 1
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE Xenial Xerus (16.04) for distribution on
[April 21st, 2016](https://wiki.ubuntu.org/XenialXerus/ReleaseSchedule)
With this *Alpha 1* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Alpha Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who needs a stable system
  * Anyone uncomfortable running a possibly frequently broken system
  * Anyone in a production environment with data or workflows that need to be reliable

Ubuntu MATE *Alpha Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE, and GTK+ developers

## What changed since the Ubuntu MATE 15.10 release?

Here what changed in Ubuntu MATE 16.04 Alpha 1 since Ubuntu MATE 15.10.

  * Updated to Ubuntu MATE Welcome 16.04.0
    * Complete overhaul of the user interface.
    * Context menu removed. Closes [LP: #1480718](https://bugs.launchpad.net/bugs/1480718)
    * Detects if the Ubuntu repositories are available. Closes [LP: #1500533](https://bugs.launchpad.net/bugs/1500533)
    * Fixes re-install of Minecraft. Closes [LP: #1516338](https://bugs.launchpad.net/bugs/1516338)
    * Added Variety, Gnote, Planner, gnome-schedule, Redshift.
    * Updated Terminator, VirtualBox, Simple Screen Recorder, Minecraft.
  * Updated MATE Tweak to 3.5.3.
    * Added Keyboard LED Indicator.
    * Added capability to enable/disable animations.
    * Fixed non-translatable strings.
    * Updated translations.
  * Updated Ubuntu MATE Settings to 16.04.0
    * Enabled GTK styling for QT applications.
    * Enabled Marco animations.
    * Enabled Program List in launcher, accessed via `Alt + F2`.
    * Updated and sorted default application handlers.
    * Removed (temporarily) the System -> Preferences categorisation.
  * Updated Ubuntu MATE Artwork to 16.04.0
    * Added MATE colourised icons for devices and places.
    * Added community [contributed wallpaper from Aditya Singh](https://ubuntu-mate.community/t/mate-wallpapers/3048)
    * Added community [contributed wallpaper from Ryan Ride](https://ubuntu-mate.community/t/heres-my-first-all-original-wallpaper/597)
    * Added community [contributed wallpaper from Noe Gonzales](https://ubuntu-mate.community/t/wallpaper-city-chill/2899)
    * Added community [contributed wallpaper from Noe Gonzales](https://ubuntu-mate.community/t/wallpaper-beach-vibes/2900)
    * Added community [contributed wallpapers from Rohith Madhavan](https://ubuntu-mate.community/t/ubuntu-mate-wallpapers/965/8)
  * Updated MATE Menu to 5.6.6.
    * Fixed local code injection.

Thanks to everyone from the Ubuntu MATE community who contributed to
this release!

## Where is MATE 1.12?

It is coming really soon. In fact it should be available via updates in
a couple of days after this Alpha 1 release.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 16.04"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/xenial/"
%}

## Known Issues

Here are the known issues.

  * The cryptsetup password prompt is not shown.
    * [LP: #1359689](https://bugs.launchpad.net/bugs/1359689)
    * [LP: #1530548](https://bugs.launchpad.net/bugs/1530548)
  * Shutdown/Restart of the live session does not work in Virtualbox, VMWave and KVM guests.
    * [LP: #1447038](https://bugs.launchpad.net/bugs/1447038)
  * The input box for editing a Wired connection static IP address doesn't appear correctly.
    * [LP: #1530323](https://bugs.launchpad.net/bugs/1530323)
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
