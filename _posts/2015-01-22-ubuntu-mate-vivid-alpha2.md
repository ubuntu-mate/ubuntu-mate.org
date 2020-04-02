---
layout: blog-post
class: blog
title: Ubuntu MATE 15.04 Alpha 2
permalink: /blog/ubuntu-mate-vivid-alpha2/
description:
category: dev
author: Martin Wimpress
lang: en
---

Ubuntu MATE 15.04 Alpha 2 is now available for download. This release builds
on Ubuntu MATE 14.04 and 14.10 and introduces some new features. The observant
among you will notice that there was no Alpha 1 release because, reasons.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 14.10 release?

Here what changed in Ubuntu MATE 15.04 Alpha 2 since Ubuntu MATE 14.10. Some of
these fixes and improvements have already been back ported to 14.10 and made
available via updates.

  * Updated the Ambiant-MATE and Radiant-MATE icon themes with green icons. Thanks to [Michael Tunnell](http://michaeltunnell.com/).
  * Added community contributed wallpaper from [Gerard Aalders](https://plus.google.com/101077282481991372459/posts/RYALQj6Bc32).
  * Added some community contributed wallpapers from [Matt Kelley](https://ubuntu-mate.community/t/electragicians-wallpapers-with-svg-files-for-your-altering-pleasure/137).
  * Added some community contributed wallpapers from [Paolo Bravi](https://ubuntu-mate.community/t/ubuntu-mate-photo-wallpapers-feel-free-to-use/157).
  * Added some community contributed wallpapers from [Steve Cook](https://ubuntu-mate.community/t/desktop-wallpapers-for-anyone-who-wants-a-copy/135).
  * Added Yuyo and Yuyo-Dark themes with Yuyo-Dark being the default. Thanks to [Sam Hewitt](http://snwh.org).
  * Added missing `libnss-mdns` [LP #1380945](https://bugs.launchpad.net/ubuntu-mate/+bug/1380945).
  * Added missing faces pixmaps [LP #1385822](https://bugs.launchpad.net/ubuntu-mate/+bug/1385822).
  * Added [MATE Menu](https://github.com/ubuntu-mate/mate-menu), which is a fork of [MintMenu](https://github.com/linuxmint/mintmenu).
  * Added [MATE Tweak](https://github.com/ubuntu-mate/mate-tweak), which is a fork of [MintDesktop](https://github.com/linuxmint/mintdesktop).
  * Added Compiz support. MATE Tweak can be used to live switch between Compiz and Marco, no log out/in required.
  * Enabled X zapping via `Ctrl+Alt+Backspace`.
  * Enabled screen reader activation via LightDM indicators and LightDM key bindings.
  * Enabled touch to click by default for touchpads.
  * Enable Tilda pull-down terminal integration. Press `F12` to show/hide.
  * Fixed GRUB theme activation.
  * Fixed Calculator media keys [LP #1382781](https://bugs.launchpad.net/ubuntu-mate/+bug/1382781).
  * Fixed package conflicts with `gnome-applets` [LP #1378666](https://bugs.launchpad.net/ubuntu-mate/+bug/1378666).
  * Fixed sound themes. Thanks to [Sergio Schneider](https://plus.google.com/116549967007914384885/about) of the [Ubunt MATE Updated project](http://sourceforge.net/projects/uumate/)
  * Fixed auto-login on first boot if auto-login was selected during the install.
  * Replaced Totem with VLC as per the community [VLC poll](https://plus.google.com/103917631499285627130/posts/T97fZ7vbuUj).
  * Contributed patches to Ubiquity the provide better support for MATE.
  * All MATE package updates from Debian have been automatically synced to Ubuntu 15.04.
  * Ubuntu 15.04 has adopted multilib GObject introspection runtime (gir) which means Caja plugins now work *"out of the box"*.

{% include blog/jumbotron.html
    title = "Ubuntu MATE 15.04 Download"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/vivid/"
%}

## Known Issues

Here are the known issues.

  * Yuyo themes do not render some UI elements correctly, such as check boxes
  and radio buttons. This is why Ambiant-MATE is still used for the live session
  and the LightDM theme.
  * Live switching between Compiz and Marco is experimental and may result in an
  inconsistent Compiz configuration.
  * Running an Ubuntu MATE live session as a Virtualbox may corrupt the video
  output of the guest.
    * You can correct the video display by pressing `Host+F1` to switch
    VT in the guest and then press `Host+F7` to switch back which will
    correct the video output.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Useful Information

You may find the following information useful, which is why we titled
the section *Useful Information* since the information presented here
is mostly useful.

  * [Ubuntu MATE 15.04 Useful Information](https://ubuntu-mate.community/t/ubuntu-mate-14-10-and-15-04-useful-information/24)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
