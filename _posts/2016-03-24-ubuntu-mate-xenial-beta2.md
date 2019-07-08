---
layout: blog-post
class: blog
title: Ubuntu MATE 16.04 Beta 2
permalink: /blog/ubuntu-mate-xenial-beta2
description: Ubuntu MATE 16.04 (Xenial Xerus) LTS Final Beta
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE Xenial Xerus (16.04) for distribution on
[April 21st, 2016](https://wiki.ubuntu.org/XenialXerus/ReleaseSchedule)
With this *Final Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

{% include blog/alert.html
    style = "warning"
    title = "Do Not Upgrade from 14.04!"
    text = "There is an issue **affecting all Ubuntu flavours** that will
            cause an upgrade from 14.04 to 16.04 to fail, hard! See bug
            [#1555237](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/1555237)
            for details. **Upgrades from 15.10 to 16.04 work just fine.**"
%}

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

## What changed since the Ubuntu MATE 16.04 Beta 1 release?

First of all, I'd like to extend my thanks to:

  * **[Luke Horwell](https://ubuntu-mate.community/users/lah7/)** and **[Robin Thompson](https://github.com/robint99)** for for their work on Ubuntu MATE Welcome and Software Boutique.
  * **[Gunnar Hjalmarsson](https://launchpad.net/~gunnarhj)** for his help making `im-config` and `gnome-language-selector` compatible with Ubuntu MATE.
  * **[Rico Tzschichholz](https://launchpad.net/~ricotz)** for his help completing MATE integration for Synapse.
  * **[Alexei Sorokin](https://build.opensuse.org/user/show/XRevan86)** and **[Alberts Muktupāvels](https://launchpad.net/~albertsmuktupavels)** for their help improving MATE integration in Compiz.
  * **[Timo Jyrinki](https://launchpad.net/~timo-jyrinki)**, **[Daniel Holbach](https://launchpad.net/~dholbach)** and **[Artur Rona](https://launchpad.net/~ari-tczew)** for sponsoring package updates for Ubuntu MATE.

Also, thank you to everyone who has been testing Ubuntu MATE 16.04 Beta
1 and filing bug reports. It has really helped identify lots of little
issues that we've worked hard to fix.

{:.center}
![Ubuntu MATE 16.04 Beta 2](/images/blog/ubuntu-mate-1604-beta2.png)

### Here is what changed Ubuntu MATE 16.04 Beta 2 since Beta 1.

  * Added Synapse 0.2.99.2-1
    * **Synapse now features complete MATE integration**. Synapse is
    installed but not active by default. It can be enabled
    using MATE Tweak.
  * Updated to MATE Tweak 3.5.8
    * Adds **Enable Launcher** to the *Interface* section which
    activates/deactives Synapse.
    * Displays a **confirmation after changing Window Manager** to Compton or Compiz.
    * Also fixed [#1548011](https://bugs.launchpad.net/bugs/1548011),
    [#1549081](https://bugs.launchpad.net/bugs/1549081),
    [#1557203](https://bugs.launchpad.net/bugs/1557203),
    [#1558013](https://bugs.launchpad.net/bugs/1558013),
    [#1549076](https://bugs.launchpad.net/bugs/1549076)
  * Updated to Compiz 0.9.12.2+16.04.20160318-0ubuntu1
    * **Improved MATE Compiz integration**, `gtk-window-decorator` will now
    use settings from Marco when Compiz detects it is running in a MATE
    session.
    * Google Chrome and Chromium windows are now considered Compiz
    windows in fullscreen to avoid tearing.
    * Refined the Compiz profile for MATE to correct some minor issues.
    * Update `mate-settings-daemon` to use `xsettings` for **improved xcursor theme support**.
  * Updated to Plank 0.11
    * Adds Docklets and also **includes a new theme for Ubuntu MATE**
    contributed by [Holger Rueckershaeuser](http://holgerrpl.tk/).
  * Updated to MATE Menu 5.6.9
    * While searching for an application, the **top match will be launched
    when Enter is pressed**. [#1552363](https://bugs.launchpad.net/bugs/1552363)
  * Updated to Ubuntu MATE Welcome 16.04.6
    * Fix splash screen flicker. [#1549072](https://bugs.launchpad.net/bugs/1549072)
    * Fix Codec installation. [#1558986](https://bugs.launchpad.net/bugs/1558986)
    * Fix system information.
    * Fix subscription updates.
    * Fix Abobe Flash, Dropbox and RednoteBook installs.
    * Fix Google Chrome repsoitory, i386 is no longer available.
    * Fix LibreOffice upgrades.
    * Add Ardour, ConvertAll, Corebird, FreeCiv, Gajim, GNOME Software,
    Gpick, Kodi, MuseScore, Nuvola Player, OBS Studio, Pinta,
    Simple Screen Recorder, Subsurface, SparkleShare, Time Tracker,
    Vivaldi, Wireshark and Zenmap to Software Boutique.
    * Add English, Chinese, French, Spanish and German translations.
  * Updated to Ubuntu MATE Artwork 16.04.5
    * **Icon rendering in menus is faster** and icon inheritance is fixed.
    * Corrected rendering of Mozo (menu editor).
    * **Update buttons and scrollbars** so GTK2 and GTK3 themes are more
    closely aligned.
    * **Add resize area and shadows for CSD windows**.
    * **Add minimal style for CSD windows running without a compositor**.
    * Add community contributed wallpaper [Blissful Sky](https://ubuntu-mate.community/t/i-made-a-new-wallpaper-blissful-sky/4277) by Jordyn.
    * Fixes [#1552363](https://bugs.launchpad.net/bugs/1552363),
    [#1556618](https://bugs.launchpad.net/bugs/1556618),
    [#1549079](https://bugs.launchpad.net/bugs/1549079),
    [#1541929](https://bugs.launchpad.net/bugs/1541929),
    [#1551029](https://bugs.launchpad.net/bugs/1551029),
    [#1499521](https://bugs.launchpad.net/bugs/1499521),
    [#1442738](https://bugs.launchpad.net/bugs/1442738),
    [#1364073](https://bugs.launchpad.net/bugs/1364073)
  * Updated to Ubuntu MATE Settings 16.04.4
    * Auto-corrects pre-existing MATE incompatible input methods.
    * Add modified `mate-panel.desktop`, specific to Ubuntu MATE, to cater
    for the all supported  compositors and disk encryption strategies.
    [#1553070](https://bugs.launchpad.net/bugs/1553070)
    * Add all optical video mime types and enable autoplay.
    * Updated default settings for new version of Plank.
    * Correct the GNOME Main Menu entry for `network-config-tool`.
  * Updated to `mate-dock-applet` 0.70.
    * Several bug fixes [#1557180](https://bugs.launchpad.net/bugs/1557180),
    [#1555324](https://bugs.launchpad.net/bugs/1555324),
    [#1550392](https://bugs.launchpad.net/bugs/1550392),
    [#1554128](https://bugs.launchpad.net/bugs/1554128),
  * Updated Ubuntu MATE Ubiquity Slideshow artwork.
  * Fixed Python plug-ins for Caja
    * **Folder Color, Deja Dup Caja, Insync Caja and others now work again**.
  * Fixed `im-config` and `gnome-language-selector`.
    *  Ensures a MATE compatible input method is selected by default.
    [#1550325](https://bugs.launchpad.net/bugs/1550325)
  * Replaced guvcview with Cheese.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 16.04"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/xenial/"
%}

## Known Issues

Here are the known issues.

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * Shutdown/Restart of the live session does not work in Virtualbox and VMWare guests.
    * [#1447038](https://bugs.launchpad.net/bugs/1447038)
  * Swap partition *may* fail to be created when installing on a disk with existing partitions.
    * [#990744](https://bugs.launchpad.net/bugs/990744)

This is our known list of bugs that affect just Ubuntu MATE and Xubuntu.

  * The Blueman applet may crash on login on computer without Bluetooth
  or has Bluetooth disabled.
    * [#1533206](https://bugs.launchpad.net/bugs/1533206)

The issues outlined above will be resolved via updates.

### PowerPC

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
