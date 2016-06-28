<!--
.. title: Ubuntu MATE 16.10 Alpha 1
.. slug: ubuntu-mate-yakkety-alpha1
.. date: 2016-06-28 13:00:00 UTC
.. tags: Ubuntu,MATE,Yakkety,alpha1
.. link:
.. description: Ubuntu MATE 16.10 (Yakkety Yak) Alpha 1
.. type: text
.. author: Martin Wimpress
-->

**Beaut, beauty! We're stoked to announce Ubuntu MATE 16.10 Alpha 1, the first 
distro to ship a fair dinkum MATE Desktop implementation built entirely 
against GTK3+. Some thought we'd let the kangaroos loose in the top paddock by 
being the first distro to switch to GTK3+ and it would all come a gutser. But 
we put in big mobs of effort to ensure it's not complete ball dust. Give it a 
burl!**

The above statement is for the benefit of our friends at 
[#systemau](https://systemau.net.au/) who lament the often predictable and 
dreary wording used in Linux distro release announcements. We hope we've help 
restore balance to the force `;-)`

# Ubuntu MATE 16.10 Alpha 1

We are preparing Ubuntu MATE 16.10 (Yakkety Yak) for distribution on
[October 13th, 2016](https://wiki.ubuntu.org/YakketyYak/ReleaseSchedule)
With this *Alpha* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<div align="center">
<img src="/gallery/blog/ubuntu-mate-1610-alpha1.png" alt="Ubuntu MATE 16.10 Alpha 1" /><br />
<b>As is now customary our release artwork was made by <a href="https://www.youtube.com/channel/UCglkWuyZDppWD2BVsyI4r3A" target="_blank"><i>Ghost Sixtyseven</i></a>.</b>
</div>

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

## What changed since the Ubuntu MATE 16.04 release?

First of all, Ubuntu MATE 16.10 Alpha 1 owes a debt of gratitude to:

  * **[Luke Horwell](https://ubuntu-mate.community/users/lah7/)** for developing Ubuntu MATE Welcome and Software Boutique.
  * **[Robin Thompson](https://github.com/robint99)** for migrating MATE Dock Applet to GTK3+
  * **[Alexei Sorokin](https://build.opensuse.org/user/show/XRevan86)** for migrating MATE Menu to GTK3+
  * **[Wolfgang Ulbrich](https://github.com/raveit65)** for adding GTK 3.18 theme support to Ambiant MATE and Radiant MATE.
  * **[Mike Gabriel](https://sunweavers.net/blog/)** for reviewing and sponsoring uploads of MATE 1.14 to Debian.
  * **[Vlad Orlov](https://github.com/monsta)** for migrating MATE components to GTK3+ and fixing Indicator support in MATE Desktop 1.14.

### What changed since Ubuntu MATE 16.04 was released?

Before we list what's been added and updated, lets go over what has been 
dropped (for good) and what is temporarily missing.

  * **GNOME Main Menu (as used in the openSUSE layout) has been dropped.**
    * No one in the MATE team believes this applet is good enough to port to GTK3+. As it is GTK2+ only and has nobody to port or maintain it, this applet will be dropped for good.
  * **The openSUSE layout is currently missing but will be re-instated in MATE Desktop 1.16.**
    * This will feature a different menu applet.
  * The **Mutiny layout is currently missing but will be re-instated** when the `topmenu-gtk` MATE applet has been rebuilt for GTK3+
  * **Pidgin will no longer installed by default**
    * Pidgin is now available in the Software Boutique.
  * *Cheese is not currently installed by default but will be re-instated* as a default application when [merge proposal 298171](https://code.launchpad.net/~ubuntu-mate-dev/cheese/caja-compatibility/+merge/298141) is merged and released.
    * Cheese is available in the Software Boutique.
  * *Indicator Session is not currently available in Ubiquity while installing Ubuntu MATE but will be re-instated* when [merge proposal 297183](https://code.launchpad.net/~ubuntu-mate-dev/indicator-session/mate-compatibility/+merge/297183) is merged and released.

This is what have been updated or added.

  * All the Ubuntu MATE seeds and meta-packages have been completely overhauled**.
    * Basically **we've started over, and completely rebuilt Ubuntu MATE 16.10 from the ground up**.
    * It is now possible to **safely uninstall all the default applications without the `ubuntu-mate-desktop` package also being removed**.
    * **[Memory consumption of Ubuntu MATE 16.10 Alpha 1 is lower](/blog/mate-desktop-gtk2-vs-gtk3-memory-consumption/)** than that of Ubuntu MATE 16.04.
  * **New community contributed wallpapers from:**
    * [Ghost Sixtyseven](https://www.youtube.com/channel/UCglkWuyZDppWD2BVsyI4r3A)    
    * [Jordyn](https://ubuntu-mate.community/t/animated-waves-wallpaper/6228)
    * [Okinawa](https://ubuntu-mate.community/t/ubuntu-16-04-lts-mustache-wallpaper/4443)
    * [Per Andersson](https://ubuntu-mate.community/t/wallpapers-rootmate-dragonmate-selassiemate-selassiegray/6662)
  * **Upgraded to MATE Desktop 1.14**, which is now built entirely against GTK 3.18.
    * **Indicator support** for MATE Desktop, when built against GTK3+, has been **significantly improved**.
    * **Ambiant-MATE and Radiant-MATE themes have been completely reworked** to support GTK 3.18.
    * **We have initial HiDPI support *(almost)* working.** Don't get too excited, this is an all or nothing implementation. When enabled **all GTK3+ applications (not just MATE) will be rendered using high quality pixel doubling**. If you have a [2160p](https://en.wikipedia.org/wiki/4K_resolution) display, it looks ace `:-D`
    * You can find out **[what changed in MATE Desktop 1.14 from the upstream release announcement](http://mate-desktop.org/blog/2016-04-08-mate-1-14-released/)**.
  * **Upgraded Ubuntu MATE Welcome** to *16.10.4*
    * Ported to WebKit2 4.0. **The transitions and animations are now hardware accelerated (where supported)** and it looks very smooth indeed.
    * Sports a **new look and many visual and usability enhancements**.
    * Getting Started section offers **much more assistance for a post install setup and configuration**. (Some elements back ported to 16.04)
    * Adds **driver installer for Logitech's Unifying Receiver peripherals**.
    * New builds are **[automatically tested](https://semaphoreci.com/lah7/ubuntu-mate-welcome)**.
      * Testers can **check out [this daily PPA](https://launchpad.net/~lah7/+archive/ubuntu/ubuntu-mate-welcome-dev),** including packages for Xenial users wanting to test this new version of Welcome.
    * Detailed **system specifications can now be copied to the clipboard**.
    * Assorted **performance optimisations**.
  * **Upgraded Software Boutique.**
    * **Adds News to inform you of additions/removals to the Software Boutique.** (Back ported to 16.04)
    * **Adds Search facility** so you can quickly find software by name, keyword and description. (Back ported to 16.04)
    * **Adds Bulk queue installs** so you can queue up multiple applications to install at once.
    * **Software Boutique now stocks ~160 applications**. (Back ported to 16.04)
    * Introduces a new feature to **display a complete list of all applications and the repositories they are sourced from**.
    * Support added for **installing software for `arm64` and `ppc64el` architectures**.
    * Software **install and removal notifications now use the application icons**.
  * **Upgraded [MATE Tweak](https://bitbucket.org/ubuntu-mate/mate-tweak/)**
    * Splits up the UI and introduces a new Panel section.
    * Can now **change icon sizes and menu item icon sizes in the panel**, exposing a new capability in MATE Desktop 1.14. This has two benefits, **bigger icons for high resolution displays** and, if you are so inclined, **large panels suitable for touch input but without changing the desktop metaphor**.
    * Supports **enabling new style GTK3+ indicators**.
    * **Supports `xcompmgr` compositor, the preferred compositor to use along side the Raspberry Pi hardware accelerated VC4 drivers**.
    * **Tilda is no longer enabled by default**. Tilda is still installed by default, but can now be optionally enabled via MATE Tweak.
  * **Upgraded [MATE Dock Applet](https://github.com/robint99/mate-dock-applet)** which now supports GTK3+
  * **Upgraded [MATE Menu](https://bitbucket.org/ubuntu-mate/mate-menu)** which now support GTK3+

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 16.10</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

Here are the known issues.

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * A thing, described.
    * [#xxxxxxx](https://bugs.launchpad.net/bugs/xxxxxxx)

This is our known list of bugs that affect just Ubuntu MATE.

  * Describe a thing.
    * [#yyyyyyy](https://bugs.launchpad.net/bugs/yyyyyyy)

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
