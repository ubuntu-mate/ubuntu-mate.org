---
layout: blog-post
class: blog
title: Ubuntu MATE 15.10 Alpha 2
permalink: /blog/ubuntu-mate-wily-alpha2
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE Wily Werewolf (15.10) for distribution on
[October 22nd, 2015](https://wiki.ubuntu.org/WilyWerewolf/ReleaseSchedule)
With this *Alpha 2* pre-release, you can see what we are trying out in
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

## What changed since the Ubuntu MATE 15.10 Alpha 1 release?

Here what changed in Ubuntu MATE 15.10 Alpha 2 since Alpha 1.

  * Added a community contributed wallpaper by [David Chadderton](https://ubuntu-mate.community/t/wallpaper-take-back-your-desktop/1708) from [Webspresso](http://webspresso.co.uk/).
  * Added a community contributed wallpaper by [quidsup](http://quidsup.net/wallpaper/show.php?i=Neon-UbuntuMATE).
  * Updated [Ubuntu MATE Plymouth boot animation](https://www.youtube.com/watch?v=fANsyzPcXyM) by Jack Mohegan.
  * Added [Ubuntu MATE Welcome](https://ubuntu-mate.community/t/ubuntu-mate-welcome-screen/1616) 1.0.1
    * Welcome is new utility unique to Ubuntu MATE.
    * Welcome helps orientate users with their new operating system.
    * Welcome guides users through post-install configuration such as installing drivers and adding language support.
    * Welcome provides a one-click installation from a highly curated list of best-in-class software to *"get stuff done"* or have some fun.
      * The installation options include Steam, Google Chrome, Dropbox, Spotify, Syncthing, Telegram, uGet, Minecraft,
      Gimp (with CMYK support), InSync, Skype, Google Music Manager, Ubuntu SDK, Codecs, libdvdcss2,
      VirtualBox 5.0 and many others.
  * Updated MATE Tweak 3.5.0
    * Fixed saving/restoring of custom panel layouts.
    * Simplifies the interface for selecting alternative panel layouts.
  * [Removed the Ubuntu Software Center](/blog/ubuntu-mate-and-ubuntu-software-center/).
  * Fixed shutdown/restart of the live session in Virtualbox guests.
    * [LP: #1447038](https://bugs.launchpad.net/bugs/1447038)

## Where is MATE 1.10?

It is coming soon, here's why.

I am an upstream MATE developer, which means I know stuff. There are good
reasons why MATE 1.10 is not in Ubuntu MATE 15.10 or other PPAs right now.
Here are some of them:

  * The upstream MATE team planned for MATE 1.10 bug fix point releases.
  Those are now all released, as of a few days ago, and include significant
  improvements to the help documentation and many bug fixes.
  * I have elected to sync MATE packages from Debian into Ubuntu without
  any modifications. I do this because I am a MATE maintainer for Debian.
  * The Debian MATE team have uploaded most of the MATE 1.10 packages to
  Debian experimental about two months ago. Bugs have been found and fixed.
  * [This bug is being crushed](https://bugs.launchpad.net/ubuntu-mate/+bug/1392502)
  and means that most packages need significant modification, it takes time.

In short, I don't want to release stuff when I know significant changes are coming.
But as you can see, lots of work on MATE 1.10 has been going behind the scenes.

{% include blog/jumbotron.html
    title = "Ubuntu MATE 15.10 Download"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/wily/"
%}

## Known Issues

Here are the known issues.

  * Can't unlock the lock screen.
    * The work around is to use Switch User and authenticate. This will *"log you in"*
    and preserve your desktop session. This bug is fixed in MATE 1.10 which will land in
    Ubuntu MATE 15.10 soon.
    * [LP: #1471454](http://launchpad.net/bugs/1471454)
  * The `cryptsetup` password prompt may not be shown.
    * [LP: #1359689](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1359689)
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
