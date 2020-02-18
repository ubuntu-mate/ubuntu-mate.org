---
layout: blog-post
class: blog
title: Ubuntu MATE 15.10 Beta 1
permalink: /blog/ubuntu-mate-wily-beta1/
description:
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE Wily Werewolf (15.10) for distribution on
[October 22nd, 2015](https://wiki.ubuntu.org/WilyWerewolf/ReleaseSchedule)
With this *Beta 1* pre-release, you can see what we are trying out in
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

## What changed since the Ubuntu MATE 15.10 Alpha 2 release?

Here's what changed in Ubuntu MATE 15.10 since Alpha 2.

  * Updated to MATE 1.10 *(mostly)*.
    * Caja now has an extension manager so plugins can be enabled/disabled at run-time.
    * A new audio mixer library, `libmatemixer`, has been introduced.
      * Provides an abstract API allowing access to mixer functionality available in
      the PulseAudio, ALSA and OSS sound systems.
    * Improved multi-monitor support.
    * Theme support has been expanded including Client Side Decorations (CSD) and pop-overs.
    * Full help and documentation is now available.
    * Static code analysis has resulted in many memory leaks being plugged.
    * Lots of bugs fixes. Really, *lots*.
    * For more details see the [MATE 1.10 Release Notes](http://mate-desktop.org/blog/2015-06-11-mate-1-10-released/).
  * Updated [Ubuntu MATE Welcome](https://ubuntu-mate.community/t/ubuntu-mate-welcome-screen/1616) 1.0.3.
    * Renamed to Welcome.
    * Added splash animation and transitions. Thanks to Luke Horwell.
    * Added and updated the content for Introduction and Features. Thanks to Larry Bushey of [Going Linux](http://goinglinux.com/) podcast.
    * Added access to backup, firewall and user manager to Getting Started.
    * Added catgories to the Software page.
    * Added a proprietary software toggle to the Software page.
    * Added new applications to the Software page:
      * App Grid.
      * Chromium as an alternative to Google Chrome.
      * Disks.
      * Hardinfo.
      * SpiderOakONE.
      * Ubuntu Software Centre.
      * VeraCrypt.
    * Update buttons in Software to make them consistent.
    * Hide some elements when in a live session.
  * Updated MATE Tweak 3.5.2
    * Added support for Fedora and Mageia panel layouts.
    * Update xcursor icon-theme when switching Window Manager to
    preserve MATE xcursor preferences.
    * Ported to Python 3.
  * Added Deja Dup integration to Caja filemanager. Thanks to [Marcos Costales](https://wiki.ubuntu.com/costales).
    * Deja Dup now has full content menu control in the Caja file manager.
  * Fixed unlocking a locked screen.
    * [LP: #1471454](http://launchpad.net/bugs/1471454)

## How complete is MATE 1.10?

We're not quite there yet. Here is the list of MATE packages that
have not yet been updated to MATE 1.10.

  * atril
  * mate-panel
  * mate-control-center
  * mate-power-manager
  * engrampa
  * mate-applets
  * mate-icon-theme-faenza
  * mate-sensors-applet
  * mate-user-share

That's quite a list. As I've said before I conduct all MATE packaging
work in Debian, as part of the MATE Packaging team for Debian. What
with summer vacations, civic duty and [DebConf 2015](http://debconf15.debconf.org/)
we didn't quite get all of MATE 1.10 uploaded in time for Beta 1.
The packages above should receive their 1.10 updates in the coming days.

Until all the MATE components are updated to 1.10, things could be a
bit bumpy. Ubuntu MATE 15.10 Beta 1 might be the most unstable version
of Ubuntu MATE we've ever released. But everything should be hunky-dory
for the final beta next month.

{% include blog/jumbotron.html
    title = "Ubuntu MATE 15.10 Download"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/wily/"
%}

## Known Issues

Here are the known issues.

  * The mix of MATE 1.10 and MATE 1.8 components will cause some instability.
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
