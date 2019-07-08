---
layout: blog-post
class: blog
title: Ubuntu MATE 16.04.1 LTS
permalink: /blog/ubuntu-mate-xenial-point-one
description: Ubuntu MATE 16.04.1 (Xenial Xerus) LTS Final Release
category: release
author: Martin Wimpress
lang: en
---

{:.center}
![Ubuntu MATE 16.04.1 LTS Final Release](/gallery/blog/ubuntu-mate-1604-final.png)

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 16.04.1"
    text = "Join the other 400,000 people who downloaded Ubuntu MATE 16.04 between April 21st 2016 and July 21st 2016 and experience a retrospective future."
    button_text = "Download"
    button_url = "/download/"
%}

## What changed since the Ubuntu MATE 16.04 release?

Here are the changes specific to Ubuntu MATE 16.04.1:

  * Ubuntu MATE Welcome fixes.
    * Fix Raspberry Pi partition resizer.
    * Remove obsolete `linux-firmware-nonfree` from the install options.
    * Correct some strings so translations are exposed.
  * Ubuntu MATE Artwork fixes.
    * Fix Calendar styling.
    * Fix progress bars so they are one colour.
    * Make GTK2 and GTK3 scrollbars consistent.
  * Ubuntu MATE Settings fixes.
    * Fix switching keyboard layouts using `Alt` + `Shift`.
  * Ubiquity fixes.
    * Now prompts to join available WiFi networks during the install.
  * Fixed shutdown/restart of the live session in Virtualbox and VMWare guests.

Here are the general Ubuntu family changes since 16.04

  * https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/ChangeSummary/16.04.1

## MATE Desktop 1.14

We've published a [PPA containing MATE 1.14 that is
designed to work with Ubuntu MATE 16.04](https://launchpad.net/~ubuntu-mate-dev/+archive/ubuntu/xenial-mate).
You can find out [what changed in MATE Desktop 1.14 from the upstream release announcement](http://mate-desktop.org/blog/2016-04-08-mate-1-14-released/).

{% include blog/jumbotron.html
    title = "MATE Desktop 1.14 for Ubuntu MATE 16.04"
    text = "If you want the latest MATE Desktop for Ubuntu MATE 16.04 than add our PPA and upgrade."
    button_text = "Get MATE Desktop 1.14"
    button_url = "/blog/mate-desktop-114-for-xenial-xerus/"
%}

## Known Issues

Here are the known issues.

### PowerPC

  * No slides are displayed in Ubiquity Slideshow while installing Ubuntu MATE on PowerPC.
    * [#1561573](https://bugs.launchpad.net/bugs/1561573)
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
