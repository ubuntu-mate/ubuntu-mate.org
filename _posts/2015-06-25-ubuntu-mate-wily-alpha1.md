---
layout: blog-post
class: blog
title: Ubuntu MATE 15.10 Alpha 1
permalink: /blog/ubuntu-mate-wily-alpha1/
description:
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE Wily Werewolf (15.10) for distribution on
[October 22nd, 2015](https://wiki.ubuntu.org/WilyWerewolf/ReleaseSchedule)
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

## What changed since the Ubuntu MATE 15.04 release?

Here what changed in Ubuntu MATE 15.10 Alpha 1 since Ubuntu MATE 15.04.

  * Added community contributed wallpapers by [David Chadderton](https://ubuntu-mate.community/users/webspresso/activity) from [Webspresso](http://webspresso.co.uk/).
  * Added a community contributed wallpaper by [Rohith Madhavan](https://ubuntu-mate.community/t/ubuntu-mate-wallpapers/965).
  * Added [TLP](http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html) for improved laptop battery endurance.
  * Added [inxi](https://code.google.com/p/inxi/)
  * Added MATE specific defaults for Plank. *(Only activated if a Plank configuration is not already present)*
  * Added custom menu entries for LibreOffice Draw/Math, Tilda and some control center applets to correct categorisation and reduce clutter.
  * Added `gvfs-fuse` to fix media playback over Samba networks using VLC.
  * Added `pulseaudio-module-bluetooth` to help improve Bluetooth A2DP support.
  * Added MATE support to `xdg-utils`. [LP: #1001902](https://bugs.launchpad.net/xdg-utils/+bug/1001902).
  * Updated MATE Tweak to 3.4.9.
    * Added button to save panel layouts.
    * Added button to reset Compiz settings to *"factory"* defaults.
    * Added support for Metacity and Mutter window managers.
    * Added support Maximus.
    * Added support for Netbook layouts.
    * Added notifications for window manager switching and layout saving.
    * Improved layout and window manager switching. No longer exit when switching between window managers.
    * Updated UI to remove/replace deprecated methods.
    * Updated translations.
    * Renamed Eleven layouts to Cupertino.
  * Updated the Ambiant-MATE and Radiant-MATE themes so that GTK3 application that use Header Bars now have traditional window decorations.
  * Updated key bindings for MATE, Marco and Compiz so they are broadly consistent and mostly the same as Unity.
  * Updated the `ubuntu-mate-core` and `ubuntu-mate-desktop` tasks/meta-packages so a *basic* Ubuntu MATE system can be installed from the `mini.iso` using just the `ubuntu-mate-core` package.
    * [Ubuntu 15.10 daily i386 mini.iso](http://archive.ubuntu.com/ubuntu/dists/wily/main/installer-i386/current/images/netboot/mini.iso)
    * [Ubuntu 15.10 daily amd64 mini.iso](http://archive.ubuntu.com/ubuntu/dists/wily/main/installer-amd64/current/images/netboot/mini.iso)
  * Updated default application handlers.
    + `.deb` files are now handled by `gdebi`.
    + `apt://` URLs are now handled by `apturl`.
    + DVD, VideoCD and SuperVCD discs are handled by VLC.
  * Updated `apt-xapian-index` to only install on i386 and amd64 due to performance and I/O overhead for ARM and PowerPC.
  * Updated Compiz profile for MATE to prevent Tilda appearing in application switchers.
  * Updated the default settings so that Ambiant-MATE is once again the default theme.
  * Updated `ubuntu-mate-lightdm-themes` to support the new version LightDM GTK Greeter.
  * Replaced `packagekit` with `python3-aptdaemon.pkcompat` to reduce memory foot print.
  * Improved support for iOS devices.
  * Fixed tool tips in Wine when running Compiz. [LP: #957879](https://bugs.launchpad.net/ubuntu/+source/compiz/+bug/957879)
  * Fixed incorrect colours in Ambiant-MATE and Radiant-MATE for some GTK3 applications. [LP: #1437690](https://bugs.launchpad.net/ubuntu-mate/+bug/1437690)
  * Fixed Compiz thumbnails. [LP: #1437611](https://bugs.launchpad.net/ubuntu-mate/+bug/1437611)
  * Fixed Trash in the live session. [LP: #1445622](https://bugs.launchpad.net/ubuntu/+source/gvfs/+bug/1445622)

{% include blog/jumbotron.html
    title = "Ubuntu MATE 15.10 Download"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/wily/"
%}

## Known Issues

Here are the known issues.

  * The `cryptsetup` password prompt may not be shown.
    * [LP: #1359689](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1359689)
  * Shutdown/Restart of the live session does not work in Virtualbox guest.
    * [LP: #1447038](https://bugs.launchpad.net/bugs/1447038)
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
