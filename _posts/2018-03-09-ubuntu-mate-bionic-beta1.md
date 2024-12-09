---
layout: blog-post
class: blog
title: Ubuntu MATE 18.04 Beta 1
permalink: /blog/ubuntu-mate-bionic-beta1/
description: Ubuntu MATE 18.04 (Bionic Beaver) Beta 1
category: dev
author: Martin Wimpress
lang: en
discourse_topic_id: 21333
---

We are preparing Ubuntu MATE 18.04 (Bionic Beaver) for distribution on
[April 26th, 2018](https://wiki.ubuntu.com/BionicBeaver/ReleaseSchedule)
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

{:.center}
![Ubuntu MATE 18.04 Beta 1](/images/blog/1804-beta1.png)

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

## What changed since the Ubuntu MATE 17.10 final release?

We've been refining Ubuntu MATE since the 17.10 release and making improvements to ensure that Ubuntu MATE offers what our users want today and what they'll need over the life of this LTS release. This is what's changed since 17.10.

### MATE Desktop 1.20

As [you may have seen, MATE Desktop 1.20 was released in February 2018](http://mate-desktop.org/blog/2018-02-07-mate-1-20-released/) and offers some significant improvements:

  * **MATE Desktop 1.20 supports HiDPI displays with dynamic detection and scaling.**
    * HiDPI hints for Qt applications are also pushed to the environment to improve cross toolkit integration.
    * Toggling HiDPI modes triggers dynamic resize and scale, no log out/in required.
  * Marco now supports **DRI3 and [Present](https://keithp.com/blogs/Present/)**, if available.
    * **Frame rates in games are significantly increased when using Marco.**
  * **Marco now supports drag to quadrant window tiling**, cursor keys can be used to navigate the Alt + Tab switcher and keyboard shortcuts to move windows to another monitor were added.

If your hardware/drivers support [DRI3](https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure) then Marco compositing is now hardware accelerated. This dramatically improves 3D rendering performance, particularly in games. If your hardware doesn't support DRI3 then Marco will fallback to a software compositor.

You can [read the release announcement](http://mate-desktop.org/blog/2018-02-07-mate-1-20-released/) to discover everything that improved in MATE Desktop 1.20. It is a significant release that also includes a considerable number of bug fixes.

### Global Menu and MATE HUD

{:.center}
![Ubuntu MATE Global Menu](/images/blog/layouts/global-menu.gif)

The Global Menu integration is much improved. When the Global Menu is added to a panel the **application menus are automatically removed from the application window** and only presented globally, no additional configuration (as was the case) is required. Likewise removing the Global Menu from a panel will restore menus to their application windows.

{:.center}
![Ubuntu MATE HUD](/images/blog/layouts/mate-hud-local.gif)

The HUD now has a 250ms (default) timeout, holding `Alt` any longer won't trigger the HUD. This is consistent with how the HUD in Unity 7 works. We've fixed a number of issues reported by users of Ubuntu MATE 17.10 regarding the HUD swallowing key presses. The HUD is also HiDPI aware now.

### Indicators by default

Ubuntu MATE 18.04 uses Indicators by default in all layouts. These will be familiar to anyone who has used Unity 7 and offer better accessibility support and ease of use over notification area applets. The volume in Indicator Sound can now be over driven, so it is consistent with the MATE sound preferences. Notification area applets are still supported as a fallback.

{:.center}
![Ubuntu MATE HUD](/images/blog/layouts/indicators-small.png)

### MATE Dock Applet

[MATE Dock Applet](https://github.com/robint99/mate-dock-applet) is used in the Mutiny layout, but anyone can add it to a panel to create custom panel arrangements. The new version adds support for BAMF and icon scrolling.

  * MATE Dock Applet no longer uses its own method of matching icons to applications and instead uses BAMF. What this means for users is that from now on the applet will be a lot better at matching applications and windows to their dock icons.
  * Icon scrolling is useful when the dock has limited space on its panel and will prevent it from expanding over other applets. This addresses an issue reported by several users in Ubuntu MATE 17.10.

### Brisk Menu

{:.center}
![Brisk Menu Dash Launcher](/images/blog/bionic/brisk-menu-dash.png)

Many users commented that when using the Mutiny layout the *"traditional"* menu felt out of place. The [Solus Project](https://getsol.us), the maintainers of [Brisk Menu](https://github.com/solus-project/brisk-menu), have add a dash-style launcher at our request. Ubuntu MATE 18.04 includes a patched version of Brisk Menu that includes this new dash launcher. When MATE Tweak is used to enable the Mutiny or Cupertino layout, it now switches on the dash launcher which enables a full screen, searchable, application launcher. Similarly, switching to the other panel layouts restores the more traditional Brisk Menu.

### MATE Window Applets

The Mutiny layout now integrates the [mate-window-applets](https://github.com/ubuntu-mate/mate-window-applets). You can see these in action alongside an updated Mutiny layout here:

<blockquote class="imgur-embed-pub" lang="en" data-id="LxJHgeF"><a href="https://imgur.com/LxJHgeF">Mutiny undecorated maximised windows</a></blockquote><script async src="https://s.imgur.com/min/embed.js" charset="utf-8"></script>

### Minimal Installation

If you follow the Ubuntu news closely you may have heard that 18.04 now has a Minimal Install option. Ubuntu MATE was at the front of the queue to take advantage of this new feature.

{:.center}
![Brisk Menu Dash Launcher](/images/blog/bionic/minimal-install.png)

The Minimal Install is a new option presented in the installer that will install just the MATE Desktop, its utilities, its themes and Firefox. All the other applications such as office suite, email client, video player, audio manager, etc. are not installed. If you're interested, here is [the complete list of software that will not be present on a minimal install of Ubuntu MATE 18.04](https://bazaar.launchpad.net/~ubuntu-mate-dev/ubuntu-seeds/ubuntu-mate.bionic/view/head:/desktop.minimal-remove)

So, who's this aimed at? There are users who like to uninstall the software they do not need or want and build out their own desktop experience. So for those users, a minimal install is a great platform to build on. For those of you interested in creating "kiosk" style devices, such as home brew Steam machines or Kodi boxes, then a minimal install is another useful starting point.

### MATE Tweak

MATE Tweak can now toggle the HiDPI mode between auto detection, regular scaling and forced scaling. HiDPI mode changes are dynamically applied. MATE Tweak has a deeper understanding of Brisk Menu and Global Menu capabilities and manages them transparently while switching layouts. Switching layouts is far more reliable now too. We've removed the *Interface* section from MATE Tweak. Sadly all the features the Interface section tweaked have been dropped from GTK3 so are now redundant.

### Caja

We've landed [caja-eiciel](https://github.com/darkshram/mate-eiciel) and [caja-seahorse](https://github.com/darkshram/seahorse-caja).

  * **caja-eiciel** - An extension for Caja to edit access control lists (ACLs) and extended attributes (xattr)
  * **caja-seahorse** - An extension for Caja which allows encryption and decryption of OpenPGP files using GnuPG

### Artwork, Fonts & Emoji

{:.center}
![Emoji Picker](/images/blog/bionic/emoji.png)

We are no longer shipping `mate-backgrounds` by default. They have served us well, but are looking a little stale now. We have created a new selection of high quality wallpapers comprised of some abstract designs and high resolution photos from [unsplash.com](https://unsplash.com). The Ubuntu MATE Plymouth theme (boot logo) is now HiDPI aware. Our friends at [Ubuntu Budgie](https://ubuntubudgie.org/) have uploaded a new version of Slick Greeter which now fades in smoothly, rather than the stuttering we saw in Ubuntu MATE 17.10. We've switched to Noto Sans for users of Japanese, Chinese and Korean fonts and glyphs. MATE Desktop 1.20 supports emoji input, so we've added a colour emoji font too.

### Raspberry Pi images

We're am planning on releasing **Ubuntu MATE images for the Raspberry Pi around the time 18.04.1 is released, which should be sometime in July**. It takes about a month to get the Raspberry Pi images built and tested and we simply don't have time to do this in time for the April release of 18.04.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 18.04 Beta 1"
    text = "We've even redesigned the download page so it's even easier to get started."
    button_text = "Download"
    button_url = "/download/"
%}

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * Anyone upgrading from Ubuntu 16.04 or newer may need to use MATE Tweak to reset the panel layout to one of the bundled layouts post upgrade.
    * Migrating panel layouts, particularly those without Indicator support, is hit and miss. Mostly miss.

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * [The Ubiquity installer may auto select US keyboard layout](https://pad.lv/1706859)
    * To work around this manually, select the correct regional keyboard layout for your computer.
  * [Ubiquity is uninstalling chosen locale language packs](https://pad.lv/1713702)
    * After a successful installation, your computer may not have all the appropriate language packs installed.
    * To work around this issue, open **Language Support** in the Control Centre and follow the prompts to automatically install the required language packs.
  * [Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.
  * [System fails to start encrypted swap on boot on an encrypted home installation](https://pad.lv/1670336).
    * To work around this either:
      * do not select "Encrypt my home directory" during installation.
      * after install edit `/etc/crypttab` and replace `UUID=XXX` with `/swapfile`.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
