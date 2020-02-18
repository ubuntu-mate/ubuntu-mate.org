---
layout: blog-post
class: blog
title: MATE Desktop 1.14 for Ubuntu MATE 16.04
permalink: /blog/mate-desktop-114-for-xenial-xerus/
description: How to upgrade Ubuntu MATE 16.04 to MATE Desktop 1.14
category: release
author: Martin Wimpress
lang: en
---

The [Ubuntu MATE Patrons](https://www.patreon.com/ubuntu_mate) have already
received this information, but here's an update for everyone.

The number one question in the Ubuntu MATE community right now is:

> When can I get MATE Desktop 1.14 for Ubuntu MATE 16.04?

The answer is, **now**. *Right now*.

{:.center}
![About MATE Desktop 1.14](/images/blog/MATE114.png)

We've published a [PPA containing MATE 1.14 that is
designed to work with Ubuntu MATE 16.04](https://launchpad.net/~ubuntu-mate-dev/+archive/ubuntu/xenial-mate).
You can find out [what changed in MATE Desktop 1.14 from the upstream release announcement](http://mate-desktop.org/blog/2016-04-08-mate-1-14-released/).

You might be wondering why it has taken 2 months to release this PPA? Here's
why; **they've been well tested**.

The packages in this PPA are derived from the MATE Desktop 1.14 packages that
were recently uploaded to Debian unstable. The upgrade issues encountered in
Debian unstable have been fixed and all the packages have transitioned to
Debian testing. All the upgrade fixes are included in this PPA to ensure a
smooth transition. We also waited for the first MATE Desktop bugfix release, so
**what you are getting today is actually MATE Desktop 1.14.1**.

## Upgrade to MATE Desktop 1.14.x

To upgrade Ubuntu MATE 16.04 to MATE Desktop 1.14.x do the following:

Open a terminal using `CRTL + ALT + t`.

    sudo apt-add-repository ppa:ubuntu-mate-dev/xenial-mate
    sudo apt update
    sudo apt dist-upgrade

Now restart your computer and you're running MATE Desktop 1.14.x `:-)`

## Notes

Upgrading to MATE Desktop 1.14 will remove the `mate-netspeed` packages, but
don't be alarmed, the NetSpeed applet is now included in the `mate-applets`
package. You won't loose any functionality.

If you see the following prompt during the upgrade, then **press Enter to accept `[default=N]`**:

    Configuration file '/etc/xdg/autostart/mate-volume-control-applet.desktop'
     ==> Deleted (by you or by a script) since installation.
     ==> Package distributor has shipped an updated version.
       What would you like to do about it ?  Your options are:
        Y or I  : install the package maintainer's version
        N or O  : keep your currently-installed version
          D     : show the differences between the versions
          Z     : start a shell to examine the situation
     The default action is to keep your current version.
    *** mate-volume-control-applet.desktop (Y/I/N/O/D/Z) [default=N] ?

The version of MATE Desktop 1.14 in [this PPA](https://launchpad.net/~ubuntu-mate-dev/+archive/ubuntu/xenial-mate)
is  **built against GTK2+ to ensure compatibility with Ubuntu MATE 16.04
and all the 3rd party MATE applets, plugins and extensions**.


We hope you enjoy using MATE Desktop 1.14 on Ubuntu MATE 16.04!
