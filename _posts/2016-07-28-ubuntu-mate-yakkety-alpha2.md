---
layout: blog-post
class: blog
title: Ubuntu MATE 16.10 Alpha 2
permalink: /blog/ubuntu-mate-yakkety-alpha2
description: Ubuntu MATE 16.10 (Yakkety Yak) Alpha 2
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE 16.10 (Yakkety Yak) for distribution on
[October 13th, 2016](https://wiki.ubuntu.org/YakketyYak/ReleaseSchedule)
With this *Alpha* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

{:.center}
![Ubuntu MATE 16.10 Alpha 2](/images/blog/ubuntu-mate-1610-alpha2.png)

**As is now customary, our release artwork was made by [Ghost Sixtyseven](https://www.youtube.com/channel/UCglkWuyZDppWD2BVsyI4r3A).**

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

## What changed since the Ubuntu MATE 16.10 Alpha 1 release?

First of all, Ubuntu MATE 16.10 Alpha 2 owes a debt of gratitude to:

  * **[Luke Horwell](https://ubuntu-mate.community/users/lah7/)** for developing Ubuntu MATE Welcome and the new [Ubuntu MATE Start Page](https://start.ubuntu-mate.org).
  * **[Robin Thompson](https://github.com/robint99)** for improving MATE Dock Applet and adding new UI features built on GTK3+
  * **[Wolfgang Ulbrich](https://github.com/raveit65)** for adding GTK 3.18 theme support to Ambiant MATE and Radiant MATE.
  * **[Vlad Orlov](https://github.com/monsta)** for migrating MATE components to GTK3+ and helping improve Indicator support in MATE Desktop 1.14.

This is what have been updated or added.

  * Added **MATE Heads-Up Display (HUD)**
    * Runs menubar commands, **much like the Unity 7 HUD**. Disabled by default, but can be enabled via MATE Tweak.
    * Once activated the HUD can be invoked via `CTRL + ALT + Space`.
  * Upgraded to **MATE Tweak 16.10.4**
    * Improved Indicator support with the **introduction of the Message Menu.**
    * Added option to **enable the MATE Heads-Up Display (HUD)**
  * Upgraded to **MATE Dock Applet 0.73**
    * **Drag and drop rearranging of dock icons**.
    * **Redesigned the window list** which appears when the mouse is hovered over a dock icon.
    * Window titles are ellipsized if they are too long.
    * Additional actions that the application supports are now shown at the top of the window list.
    * Pinning and Unpinning is now always shown at the bottom of the window list.
  * Upgraded to **Ubuntu MATE Welcome 16.10.7**
    * Auto focus the search text entry.
    * Updated translations.
  * Firefox now has a **[customised Ubuntu MATE Start Page](https://start.ubuntu-mate.org)**.
  * *Cheese has been re-instated* as a default application.
  * **Indicator Session has been re-instated in Ubiquity** while installing Ubuntu MATE.
  * The `.iso` image is **approximately 150MB smaller**.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 16.10"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/download/"
%}

## Known Issues

Here are the known issues.

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * Choosing an Entire Disk install on PowerPC may result in an unbootable system.
    * The work around is to manually partition your hard disk.
    * [#1606089](https://bugs.launchpad.net/bugs/1606089),
    [#1607128](https://bugs.launchpad.net/bugs/1607128)

  * R300 GPU accelerated graphics do not work on PowerPC
    * [#1432949](https://bugs.launchpad.net/bugs/1432949),
    [#1575391](https://bugs.launchpad.net/bugs/1575391)

  * Ubiquity installer Slideshows and Ubuntu MATE Welcome display a blank window on PowerPC. This is due to a bug in WebKit 2.
    * [#1561573](https://bugs.launchpad.net/bugs/1561573),
    [#1597764](https://bugs.launchpad.net/bugs/1597764)

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
