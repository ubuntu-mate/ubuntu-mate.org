---
layout: blog-post
title: Ubuntu MATE 19.10 Beta 1
permalink: ubuntu-mate-eoan-beta
category: release
author: Martin Wimpress
lang: en
---

**Ubuntu MATE 19.10 is a signifcant upgrade over previous releases sporting bug
fixes and new features**

We are preparing Ubuntu MATE 19.10 (Eoan Ermin) for distribution on
[October 18th, 2018](https://wiki.ubuntu.com/EoanErmin/ReleaseSchedule)
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

{:.center}
![Ubuntu MATE 19.10 Beta](/images/blog/1910-beta.png)
**Ubuntu MATE 19.10 with the Familiar layout**

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

## What changed since the Ubuntu MATE 19.04 final release?

  * Added MATE Desktop 1.22.1
  * Fixed frequent crashers in Brisk Menu and MATE Dock Applet
  * Fixed oversized indicator icons
  * Fixed race condition that could result in two network status icons being displayed
  * Fixed XPresent support
  * Fixed lock icons in the Network Indicator when establishing VPN connection
  * Added `indicator-datetime` support
  * Switched from Thunderbird to Evolution as the default mail/calendar app
  * Dropped Brasero from the default installed applications.
  * Reduce the .iso image size.
  * MATE Tweak preserves user preferences when switching between custom layouts.
  * Start Applications hides system applications.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 19.04 Beta"
    text = "Our download page makes it easy to acquire the most suitable build for your hardware."
    button_text = "Download"
    button_url = "/download/"
%}

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * The Software Boutique doesn't list any available software.
    * An update, due very soon, will re-stock the software library and add a few new applications too.

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * [Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
