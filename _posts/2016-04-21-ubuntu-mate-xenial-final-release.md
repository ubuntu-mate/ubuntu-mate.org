---
layout: blog-post
class: blog
title: Ubuntu MATE 16.04 LTS
permalink: /blog/ubuntu-mate-xenial-final-release/
description: Ubuntu MATE 16.04 (Xenial Xerus) LTS Final Release
category: release
author: Martin Wimpress
lang: en
---

{:.center}
![Ubuntu MATE 16.04 LTS Final Release](/images/blog/ubuntu-mate-1604-final.png)

# Thank You!

> **Ubuntu MATE 16.04 LTS has not just been in development for 6 months. Ubuntu
> MATE 16.04 LTS has been in development for nearly 2 years. Since the project
> started in June 2014 this release, this our first official LTS, is what we've
> been working towards. This was the goal we had firmly in our sights every step
> of the way.**
>
> **I extend my sincere thanks to everyone who has contributed to Ubuntu MATE over
> the last 22 months. None of this would have been possible without the
> countless contributions from the amazing Ubuntu MATE community. I can't thank
> you all enough for what you've helped create. I only hope this release makes
> you all proud.**
>
> *Martin Wimpress, Ubuntu MATE Project Leader.*

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 16.04"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/download/"
%}

## What changed since the Ubuntu MATE 16.04 Beta 2 release?

Here is what changed Ubuntu MATE 16.04 LTS Final Release since Beta 2:

  * Added `ubuntu-snappy-cli` to the default install.
  * Updated Ubuntu MATE Welcome to 16.04.9.
    * Updated translations and assorted bugs fixes. [#1566837](https://bugs.launchpad.net/bugs/1566837)
    * Updated to install Telegram from a PPA maintained by Martin Wimpress that has fixes Indicator icons.
    * Updated Vivaldi to the stable release.
    * Improved partition resizing for the Raspberry Pi.
  * Update MATE Menu 5.7.1
    * Fixed the menu being offset from the panel when using Compiz. [#1559371](https://bugs.launchpad.net/bugs/1559371)
    * Fixed configuring a custom heading colour. [#1560332](https://bugs.launchpad.net/bugs/1560332)
    - Fixed displaying the Software Boutique as package manager if it is available. [#1568170](https://bugs.launchpad.net/bugs/1568170)
    - Fixed drawing the menu over existing windows. [#1569563](https://bugs.launchpad.net/bugs/1569563)
  * Updated MATE Tweak to 3.5.10
    * Fixed aggressive setting of the xcursor theme. [#1563087](https://bugs.launchpad.net/bugs/1563087)
    * Fixed `psutil.AccessDenied` crash. [#1562843](https://bugs.launchpad.net/bugs/1562843)
    * Fixed handling of "unknown" window managers. [#1563037](https://bugs.launchpad.net/bugs/1563037)
    * Fixed ordering of notebook entries. [#1564957](https://bugs.launchpad.net/bugs/1564957)
    * Fixed toggling of menu bar features. [#1564959](https://bugs.launchpad.net/bugs/1564959)
    * Modified composited window managers to use a phase delayed startup. [#1553070](https://bugs.launchpad.net/bugs/1553070)
  * Updated Caja Dropbox to 1.12.0-3
    * Fixed the missing tray icon by executing via `dbus-launch` to ensure. [#1559249](https://bugs.launchpad.net/bugs/1559249)
  * Updated Blueman to 2.0.4-1ubuntu2
    * Fixed `blueman-applet` crashing on startup. [#1533206](https://bugs.launchpad.net/bugs/1533206)
  * Updated Ubuntu MATE Artwork to 16.04.6
    * Assorted bug fixes and refinements 1563971 [#1563971](https://bugs.launchpad.net/bugs/1563971)
  * Updated to Ubuntu MATE Settings 16.04.5
    * Modified composited window managers to use a phase delayed startup. [#1553070](https://bugs.launchpad.net/bugs/1553070)
  * Updated MATE Control Center to 1.12.1.
    * Fixes configuration of all Windows focus modes. [#1382992](https://bugs.launchpad.net/bugs/1382992)
  * Updated MATE Session Manager to 1.12.2.
    * Minor bugs fixes.
  * Prepared the Ubuntu MATE 16.04 image for the Raspberry Pi 2 and Raspberry Pi 3.

### Community contributors

Here are just a few of the people who contributed to Ubuntu MATE during the
16.04 development cycle that deserve a special mention:

A very special *Thank you* to **[Luke
Horwell](https://ubuntu-mate.community/users/lah7/)** for taking Ubuntu
MATE Welcome to the next level. Ubuntu MATE Welcome and the Software
Boutique have become a central part of the Ubuntu MATE experience and
it is Luke we need to thank for really making them standout features.
Also thanks to **[Robin Thompson](https://github.com/robint99)**,
author of MATE Dock Applet, who did the lions share of adding a
translation framework to Ubuntu MATE Welcome which is now available in
20 languages.

Thanks to **[Mike Gabriel](https://sunweavers.net/blog/)** the Debian
Developer heading up the Debian MATE Packaging team. The vast majority
of Ubuntu MATE development actually happens in Debian and we owe a huge
debt of gratitude to Mike for his tireless efforts.

Thanks to **[Joe Ressington](http://joeress.com/about)**, **Isaac
Carter** and **[Albert
Hickey](http://plus.google.com/+Winkleink)**, from **[The Pi
Podcast](http://thepipodcast.com/)**, for testing Ubuntu MATE 16.04 for
the Raspberry Pi 2 and Raspberry Pi 3. You really helped ironout some
kinks and improved the release quality for everyone.

Thank you to **[Alexei
Sorokin](https://build.opensuse.org/user/show/XRevan86)** and **Alberts
Muktupāvels** for their help
improving MATE integration in Compiz.

Thanks **[Gunnar Hjalmarsson](https://launchpad.net/~gunnarhj)** for
his help making `im-config` and `gnome-language-selector` compatible
with Ubuntu MATE and **[Rico
Tzschichholz](https://launchpad.net/~ricotz)** for his help completing
MATE integration for Synapse and the new version of Plank.

Thank you to the following people for creating the new wallpaper
backgrounds for Ubuntu MATE 16.04:

**[Ghost Sixtyseven](https://www.youtube.com/channel/UCglkWuyZDppWD2BVsyI4r3A)**,
**[Luke Horwell](https://ubuntu-mate.community/t/wallpaper-the-materix/3107)**,
**[Rick Lell](https://ubuntu-mate.community/t/wallpaper-ubuntu-mate-greyscaled-wood/3199)**,
**[Noe Gonzales](https://ubuntu-mate.community/t/sky-high-wallpaper-photos-licensed-cc-by-sa/3433)**,
**[Randall Lewis](https://ubuntu-mate.community/t/wallpaper-solar-systemate-4-flavors-1920x1080/3354)**,
**[Sacha](https://ubuntu-mate.community/t/wallpaper-some-parrots-and-an-island/3450)**,
**[Aditya Singh](https://ubuntu-mate.community/t/mate-wallpapers/3048)**,
**[Ryan Ride](https://ubuntu-mate.community/t/heres-my-first-all-original-wallpaper/597)**,
**[Noe Gonzales](https://ubuntu-mate.community/t/wallpaper-city-chill/2899)** (again),
**[Noe Gonzales](https://ubuntu-mate.community/t/wallpaper-beach-vibes/2900)** (yet again) and
**[Rohith Madhavan](https://ubuntu-mate.community/t/ubuntu-mate-wallpapers/965/8)**.

Finally, thanks to everyone who installed the alphas and betas, reported issues,
provided feedback or donated to Ubuntu MATE. Your feedback has been vital to
understanding what improvements people most want to see. We do listen, so keep the
feedback coming.

### Canonical

In addition to the efforts of the Ubuntu MATE team and the Ubuntu MATE
community, we are also extremely grateful for the help and support we've
recieved from the following Canonical employees:

  * **[Adam Conrad](https://launchpad.net/~adconrad)**,
 **[Adam Stokes](https://launchpad.net/~adam-stokes)**,
 **[Alan Pope](https://launchpad.net/~popey)**,
 **[Colin Watson](https://launchpad.net/~cjwatson)**,
 **[Daniel Holbach](https://launchpad.net/~dholbach)**,
 **[Didier Roche](https://launchpad.net/~didrocks)**,
 **[Iain Lane](https://launchpad.net/~laney)**,
 **[Łukasz Zemczak](https://launchpad.net/~sil2100)**,
 **[Marco Trevisan](https://launchpad.net/~3v1n0)**,
 **[Martin Pitt](https://launchpad.net/~pitti)**,
 **[Mathieu Trudel-Lapierre](https://launchpad.net/~mathieu-tl)**,
 **[Michael Hall](https://launchpad.net/~mhall119)**,
 **[Oliver Grawert](https://launchpad.net/~ogra)**,
 **[Sebastien Bacher](https://launchpad.net/~seb128)**,
 **[Stephen M. Webb](https://launchpad.net/~bregma)**,
 **[Timo Jyrinki](https://launchpad.net/~timo-jyrinki)** and
 **[Will Cooke](https://launchpad.net/~willcooke)**.

## Known Issues

Here are the known issues.

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * Ubiquity does not prompt to join available WiFi networks.
    * [#1572793](https://bugs.launchpad.net/bugs/1572793)
  * Shutdown/Restart of the live session does not work in Virtualbox and VMWare guests.
    * [#1447038](https://bugs.launchpad.net/bugs/1447038)

### PowerPC

  * No slides are displayed in Ubiquity Slideshow while installing Ubuntu MATE on PowerPC.
    * [#1561573](https://bugs.launchpad.net/bugs/1561573)
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
