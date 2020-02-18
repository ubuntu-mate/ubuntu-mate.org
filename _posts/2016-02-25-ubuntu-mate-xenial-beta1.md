---
layout: blog-post
class: blog
title: Ubuntu MATE 16.04 Beta 1
permalink: /blog/ubuntu-mate-xenial-beta1/
description: Ubuntu MATE 16.04 (Xenial Xerus) LTS Beta 1
category: dev
author: Martin Wimpress
lang: en
---

We are preparing Ubuntu MATE Xenial Xerus (16.04) for distribution on
[April 21st, 2016](https://wiki.ubuntu.org/XenialXerus/ReleaseSchedule)
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

## What changed since the Ubuntu MATE 16.04 Alpha 2 release?

First of all, I'd like to extend my thanks to:

  * **[Luke Horwell](https://ubuntu-mate.community/users/lah7/)** for introducing dynamic generation of the Software Boutique in Ubuntu MATE Welcome and generally improving the design and function of Ubuntu MATE Welcome.
  * **[Robin Thompson](https://github.com/robint99)** for adding a translation framework to Ubuntu MATE Welcome. We are finalsing the translation tooling and will be asking for translators to help us from next week.
  * **[Mike Gabriel](https://sunweavers.net/blog/)** for packaging `mate-dock-applet`, `topmenu-gtk` and re-instating `gir1.2-wnck-1.0` (required by `mate-dock-applet`) into the `libwnck` packages for Debian.
  * **[Iain Lane](https://launchpad.net/~laney)** for mentoring Martin Wimpress so the `libwnck` package updates in Debian could be synced to Ubuntu.
  * **[Timo Jyrinki](https://launchpad.net/~timo-jyrinki)** and **[Daniel Holbach](https://launchpad.net/~dholbach)** for sponsoring critical package updates for Ubuntu MATE.
  * **[Ghost Sixtyseven](https://www.youtube.com/channel/UCglkWuyZDppWD2BVsyI4r3A)** for creating a fantastic new Ubuntu MATE desktop wallpaper called *"A Dawn Gift"*.

{:.center}
![Ubuntu MATE 16.04 Beta 1](/images/blog/ubuntu-mate-1604-beta1.png)

Thanks to everyone else from the Ubuntu MATE community who contributed to this release!

### Here is what changed in Ubuntu MATE 16.04 Beta 1 since Alpha 2.

  * Ubuntu MATE Welcome 16.04.3
    * Added the **Software Boutique** which now contains ~120 applications.
    * Added the ability to **launch applications from the Software Boutique**.
    * Added **category filtering to the Software Boutique**.
    * Added **expandable/collapsible More Details for each application** listed in the Software Boutqiue.
    * Added **screenshots for applications listed in the Software Boutique**.
    * Added **subscribe to updates for Ubuntu MATE Welcome** to ensure you always have the latest version of Ubuntu MATE Welcome and Software Boutique, including new application listings and translations.
    * Added **highlighting of installed applications** listed in the Software Boutique.
    * Added a **spinner while applications are being installed** using the Software Boutique.
    * Added **Raspberry Pi 2** specific features and documentation, including **automatic partition resizing**.
    * Fixed the **toggling of Proprietary software in the Software Boutique**.
    * Improved the Software Boutique **by always showing software categories** at the top of the window.
    * Assorted bug fixes and improvements.
  * Updated MATE Desktop 1.12.1
    * MATE Desktop **CPU resource requirements have been reduced across the board**.
    * **Updated Caja to 1.12.4**
      * Fixes a segfault on start-up.
      * Fixes a segfault when the `python-caja` extension is enabled.
      * Fixes a segfault when restoring files that have special characters in their name from the Trash.
      * Fixes a some memory leaks.
    * **Updated Pluma to 1.12.2**
      * Fix missing icon in the Python console plugin list.
      * Fix possible `use-after-free` in incremental searches.
    * **Updated Eye of MATE to 1.12.2**
      * Fixes a integer overflow when allocating a large block of memory during a Print Preview.
      * Assorted minor fixes and optimisations.
  * Added MATE Dock Applet 0.67 developed by [Robin Thompson](https://github.com/robint99).
    * A **configurable dock applet that can be placed on any panel, in any orientation**.
  * Added Topmenu Applet 0.2.1 developed by [Javier S. Pedro](https://javispedro.com/me.html)
    * A **Gtk+ module that allows placing a global menu in MATE panel applets**.
    * The **Ubuntu MATE team also added `lxpanel-plugin-topmenu` and `xfce4-topmenu-plugin` to the Debian and Ubuntu archives** so those desktops can benefit too.
  * Ubuntu MATE Settings 16.04.2
    * Added **Mutiny panel layout which showcases `mate-dock-applet` and `topmenu-gtk`**.
      * **The traditional GNOME2 style two panel layout is, and will continue to be, the default**.
  * Updated Ubuntu MATE Artwork to 16.04.2
    * Added community [contributed wallpaper from Ghost Sixtyseven](https://ubuntu-mate.community/t/wallpaper-a-dawn-gift-xenial-xerus/3925)

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

  * Cryptsetup password prompt is not shown.
    * [LP: #1359689](https://bugs.launchpad.net/bugs/1359689)
    * [LP: #1530548](https://bugs.launchpad.net/bugs/1530548)
  * Plymouth does not display the graphical boot splash.
    * [LP: #1370707](https://bugs.launchpad.net/bugs/1370707).
  * Shutdown/Restart of the live session does not work in Virtualbox and VMWare guests.
    * [LP: #1447038](https://bugs.launchpad.net/bugs/1447038)
  * The input box for editing a Wired connection static IP address doesn't appear correctly.
    * [LP: #1530323](https://bugs.launchpad.net/bugs/1530323)
  * Swap partition *may* fail to be created when installing on a disk with existing partitions.
    * [LP: #990744](https://bugs.launchpad.net/bugs/990744)

### Ubuntu MATE issues

This is our known list of bugs that jut affect Ubuntu MATE.

  * System Information in Ubuntu MATE Welcome displays "No Information Available".
  * Activating a Compton composited Window Manager in Virtualbox, without installing Guest Additions drivers, will lock up the desktop.
    * **VirtualBox drivers can be installed via Ubuntu MATE Welcome in the Getting Started section**.

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
