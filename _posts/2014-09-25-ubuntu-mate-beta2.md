---
layout: blog-post
class: blog
title: Ubuntu MATE 14.10 Beta 2
permalink: /blog/ubuntu-mate-utopic-beta2/
description:
category: dev
author: Martin Wimpress
lang: en
---

Ubuntu MATE 14.10 Beta 2 is now available for download. This second beta
fixes a number of issues that were present in Beta 1, adds a few new
features and includes some more original artwork. We've managed to not
introduce any new bugs this time but please **make sure you read the
release notes below** because there are still unresolved issues you'll
need to be aware of.

## What works?

Most things, more than in Beta 1 at least. People tell us that Ubuntu
MATE is stable. You may, or may not, agree.

## What changed since Beta 1?

Beta 2 has been focused on fixing broken things and improving what was
already present in Beta 1.

  * Released community contributed [Ubuntu MATE Identity graphics from Goce Mitevski](https://github.com/gocemitevski/ubuntu-mate-identity-graphics).
  * Added community contributed [GRUB2 theme from Ivan Pejić](https://github.com/nadrimajstor/grub2-themes-ubuntu-mate).
  * Added `gnome-system-tools` due to community feedback requesting user and time management facilities. [LP #1367772](https://bugs.launchpad.net/ubuntu-mate/+bug/1367772)
  * Added indicators to Ubiquity that enable access to assistive features and basic system configuration.
  * Added assistive features to LightDM.
  * Added keybindings, compatible with Sonar GNU/Linux, for toggling assistive features.
  * Added a MATE panel layout that is similar in appearance to Windows XP classic mode (see below for activation instructions).
  * Updated the default Ubuntu MATE panel layout to better reflect how Ubuntu 10.04 and 10.10 were arranged.
  * Updated some icon assets in Ambiant-MATE and Radiant-MATE. Thanks to [Jack Mohegan](https://plus.google.com/101312215214323407176/posts/2dyVkArfx49).
  * Updated some of the Ubiquity slides used in the installer slide show. Thanks to [Ivan Pejić](https://plus.google.com/113587242852192152625/).
  * Updated font configuration to be consistent across applications.
  * Fixed installation failures when there is no active Internet connection. Really, *it is* fixed this time. [LP #1363267](https://bugs.launchpad.net/ubuntu-mate/+bug/1363267)
  * Fixed LightDM crashes that prevented the Live desktop session from working. [LP #1369952](https://bugs.launchpad.net/ubuntu/+source/lightdm/+bug/1369952)
  * Fixed EFI computers displaying a black screen rendering the system unusable. [LP #1353989 ](https://bugs.launchpad.net/ubuntu/+source/systemd-shim/+bug/1353989)
  * Fixed default application associations. [LP #1364127](https://bugs.launchpad.net/ubuntu-mate/+bug/1364127)
  * Fixed erroneous apt configuration that prevented recommended packages being installed.
  * Fixed video corruption in the Ubiquity installer.
  * Fixed activation of the default sound theme.
  * Fixed speaker test sounds in the Sound preferences.
  * Merged Ubuntu MATE specific PolicyKit desktop privileges upstream.
  * Removed `virtualbox-guest-x11` from the Live session.
  * Removed [wubi](https://wiki.ubuntu.com/WubiGuide) from the Ubuntu MATE .iso image.

{% include blog/jumbotron.html
    title = "Ubuntu MATE 14.10 Beta 2 Download"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/utopic/"
%}

## Upgrading from Beta 1

Some of the meta packages have changed since Beta 1. If you have Beta 1
installed, here is how to upgrade to Beta 2.

Start a shell and update.

    sudo apt-get update

If you were tracking development packages between Beta 1 and Beta 2 you
will want to remove `grub-theme-ubuntu-mate` since it has a new name now.

    sudo apt-get remove grub-theme-ubuntu-mate

Complete the upgrade.

    sudo apt-get dist-upgrade

Remove some obsolete packages.

    sudo apt-get remove ubuntu-mate-desktop-policy-privileges

Remove an erroneous apt configuration that has existed since Alpha 1.

    sudo rm /etc/apt/apt.conf.d/00recommends

If you were tracking development packages between Beta 1 and Beta 2 you
may want to remove IBus.

    sudo apt-get purge ibus ibus-anthy ibus-gtk ibus-gtk3 ibus-qt4

Reboot, login, start a shell and clean up.

    sudo apt-get autoremove
    sudo apt-get autoclean

## Known Issues

Ubuntu MATE 14.10 is currently in beta and we are aware of the following
issues.

  * Full disk encryption, or rather entering your pass phrase into Plymouth, *may not* work. **Home directory encryption does work**.
    * [LP #1359689](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1359689)
  * Plymouth does not display boot up splash screens.
    * [LP #1370707](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1370707)
    * [LP #1368414](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1368414)
    * [LP #1356513](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1356513)
    * [LP #1343841](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1343841)

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported:

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Testing

The Ubuntu MATE release candidate will be released mid-October we need
people installing, using Ubuntu MATE and reporting any issues you may
find on the project's bug tracker.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

Is there anything you can help with or want to be involved in? Maybe
you just want to discuss your experiences or ask the maintainers some
questions. Please [come and talk to us](/community/).

