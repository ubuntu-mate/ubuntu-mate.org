---
layout: blog-post
class: blog
title: MATE Desktop 1.16 for Ubuntu MATE 16.04
permalink: /blog/mate-desktop-116-for-xenial-xerus
description: How to upgrade Ubuntu MATE 16.04 to MATE Desktop 1.16
category: release
author: Martin Wimpress
lang: en
---

The [Ubuntu MATE Patrons](https://www.patreon.com/ubuntu_mate) have
already received this information, but here's an update for everyone.

A popular question in the Ubuntu MATE community among the 16.04 users is:

> When can I get MATE Desktop 1.16 for Ubuntu MATE 16.04?

The answer is, **now**. *Right now*.

{:.center}
![About MATE Desktop 1.16](/images/blog/MATE116.png)

We've published a [PPA containing MATE 1.16 that is
designed to work with Ubuntu MATE 16.04](https://launchpad.net/~ubuntu-mate-dev/+archive/ubuntu/xenial-mate).
You can find out [what changed in MATE Desktop 1.16 from the upstream release announcement](http://mate-desktop.org/blog/2016-09-21-mate-1-16-released/).

You might be wondering why it has taken several months to release this PPA?
Here's why; **they've been well tested**.

The packages in this PPA are derived from the MATE Desktop 1.16
packages that have been prepared for the upcoming Debian 9 (Stretch)
release. Issues encountered in Debian have been fixed and we also waited
for the all the MATE Desktop bugfix releases, so **what you are getting
today is actually MATE Desktop 1.16.1**.

## Upgrade to MATE Desktop 1.16.x

To upgrade Ubuntu MATE 16.04 to MATE Desktop 1.16.x do the following:

Open a terminal using `CRTL + ALT + t`.

    sudo apt-add-repository ppa:ubuntu-mate-dev/xenial-mate
    sudo apt update
    sudo apt full-upgrade

Now restart your computer and you're running MATE Desktop 1.16.x `:-)`

## Notes

Upgrading to MATE Desktop 1.16 will remove the `mate-netspeed` packages, but
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

The version of MATE Desktop 1.16 in [this PPA](https://launchpad.net/~ubuntu-mate-dev/+archive/ubuntu/xenial-mate)
is **mostly built against GTK2+ to ensure compatibility with Ubuntu MATE
16.04 and all the 3rd party MATE applets, plugins and extensions**.

That said some applications have been transitioned to GTK3+ such as:

  * Engrampa
  * MATE Notification Daemon
  * MATE PolKit
  * MATE Session Manager
  * MATE Terminal

We hope you enjoy using MATE Desktop 1.16 on Ubuntu MATE 16.04!
