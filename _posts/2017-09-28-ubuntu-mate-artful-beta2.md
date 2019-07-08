---
layout: blog-post
class: blog
title: Ubuntu MATE 17.10 Beta 2
permalink: /blog/ubuntu-mate-artful-beta2
description: Ubuntu MATE 17.10 (Artful Aardvark) Beta 2
category: dev
author: Martin Wimpress
lang: en

gallery:
    - image: /images/blog/layouts/00_mutiny.png
      caption: Mutiny Panel Layout
    - image: /images/blog/layouts/01_cupertino.png
      caption: Cupertino Panel Layout
    - image: /images/blog/layouts/02_redmond.png
      caption: Redmond Panel Layout
    - image: /images/blog/layouts/03_pantheon.png
      caption: Pantheon Panel Layout
    - image: /images/blog/layouts/04_contemporary.png
      caption: Contemporary Panel Layout
    - image: /images/blog/layouts/05_netbook.png
      caption: Netbook Panel Layout
    - image: /images/blog/layouts/06_traditional.png
      caption: Traditional Panel Layout
---

# *Join the Mutiny!*

We are sorry to announce that in this final beta of Ubuntu MATE 17.10
we've added new features to Caja, the MATE file manager. We realise
this is somewhat unconventional and would also like issue fair warning
to our community that we'll be adding more new features to Caja during
the the 18.04 development cycle. I know, we're a bit kooky like that.

  * **Feature rich file manager** - *Check!*
  * **Slick Greeter?** - *Check!*
  * **Global Menus?** - *Check!*
  * **Heads-up Display (HUD)?** - *Check!*
  * **Super key to active menu launchers?** - *Check!*
  * **Functional alternative to Unity 7 for those that want it and a traditional desktop for those that don't?** - *Check!*
  * *Read on to find out more...*

*We mean it, keep reading! Don't just go hunting for the download button
and skip over our most glorious release notes.*

We are preparing Ubuntu MATE 17.10 (Artful Aardvark) for distribution on
[October 19th, 2017](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseSchedule)
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

{:.center}
![Ubuntu MATE 17.10 Beta 2](/images/blog/1710-beta2-medium.png)

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

# What changed since the Ubuntu MATE 17.04 final release?

We've really been burning the midnight oil for the last four months.
This is what has been updated or added.

## Panel Layouts

We [surveyed our community about potentially changing the default UI](https://ubuntu-mate.community/t/poll-pantheon-to-become-the-default-layout-in-17-10/12817).
The feedback was mixed when factoring in the results from
[Twitter](https://twitter.com/ubuntu_mate/status/855704668097441793),
[Google+](https://plus.google.com/+MartinWimpress/posts/MtuF4edeSqi) and
[Straw Poll](http://www.strawpoll.me/12799961/r).

But it was the comments from our users that were most compelling. [We
decided to leave the default
alone](https://ubuntu-mate.community/t/ubuntu-mate-17-10-default-layout-decisions/12878?u=wimpy),
a personally difficult decision, and turned our attention to
rationalising the panel layouts and thoughtfully reconfiguring them.
Each panel layout is distinctive and now provides a different desktop
workflow:

  * **Mutiny** mimics the Unity 7 interface
  * **Cupertino** provides something similar to macOS
  * **Redmond** will be familiar to Windows users
  * **Pantheon** a hybrid for long time desktop Linux users who want some modern conveniences
  * **Contemporary** a blend of the best of the old and the sprinkle of the new
  * **Netbook** people still use them and this layout is for them
  * **Traditional** just like your Dad remembers it, and still the default

Here are a few screenshots to give you a feel for how things look.

{% include blog/gallery.html %}

## Global Menu

Global Menu support is now much improved, even compared to 17.10 Alpha
2, and available via the **Contemporary**, **Cupertino** and **Mutiny**
layouts which can be **activated via MATE Tweak**. Fully functional
with GTK, Qt, LibreOffice, Firefox/Thunderbird, Google Chrome, Electron
and others. You can now make more of your available screen space while
using Ubuntu MATE.

{:.center}
![Global Menu](/images/blog/layouts/global-menu.gif)

**NEW in 17.10 Beta 1** - Thanks to the excellent testing feedback
we've had since 17.10 Alpha 2 we've made the Global Menu far more
reliable and now operate correctly regardless of whether the
application was launched from the terminal, menu or launcher.

## Super key

{:.right}
![Super Key](/images/blog/layouts/superkey.png)

Complete Super key support is available from several of the panel
layouts. We're thrilled to welcome [Victor
Kareh](https://github.com/vkareh/) to the [team](/team/) who has been
busy patching [MATE Settings Daemon](https://github.com/mate-desktop/mate-settings-daemon),
[MATE Menu](https://github.com/ubuntu-mate/mate-menu),
[Brisk Menu](https://github.com/solus-project/brisk-menu) and
[MATE Dock Applet](https://github.com/robint99/mate-dock-applet) to
make the Super key work the way you'd all expect. This means <kbd>Super</kbd>
can be used to activate the menus/launchers and any other key-bindings
that include the <kbd>Super</kbd> key also continue to function correctly.

MATE Dock Applet, used in the Mutiny layout, also includes launching or
switching to docked items based on their position using in the dock
using <kbd>Super</kbd> + <kbd>1</kbd>, <kbd>Super</kbd> + <kbd>2</kbd> which will be familiar to Unity 7 users.
<kbd>Super</kbd> + <kbd>L</kbd> is also recognised as a screen lock key-binding along with the
usual <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd> that MATE Desktop users expect.

## Heads-Up Display

This is something we started during Ubuntu MATE 16.10 and never
perfected, but is now ready for prime time. A favourite of Unity 7
users is the Heads-Up Display (HUD) which provides a way to search for
and run menu-bar commands without your fingers ever leaving the
keyboard.

So if you're trying to find that single filter in Gimp but can't
remember which filter category it fits into or if you can't recall if
preferences sits under File, Edit or Tools on your favourite browser,
you can just search for it rather than hunting through the menus.

Just like Global Menus the HUD is currently only available via the
**Contemporary**, **Cupertino** and **Mutiny**.

### HUD improvements since 17.10 Alpha 2

We've improved the HUD significantly since Alpha 2 thank to all the
great testing feedback.

  * **NEW in 17.10 Beta 1** - The HUD is now **activated by just pressing** <kbd>Alt</kbd>, as you would expect in Unity 7.
  * The HUD is now reliably activated. In Alpha 2 is only responded to about one third of requests.
  * **NEW in 17.10 Beta 1** - The **HUD is now locally integrated**, so that it overlays on top of the activate application.

{:.center}
![The Locally integrated Heads-Up Display (HUD)](/images/blog/layouts/mate-hud-local.gif)

### Locally integrated rationale

The purpose of the HUD is to keep your fingers on the keyboard and
improve the efficiency in driving the menus for keyboard centric users.
We've locally integrated the HUD for similar reasons, if you're looking
at an application why move the HUD to the top of screen away from where
your eyes are already focused. Keeping the HUD within the context of
the active application eliminates refocusing your attention to a
different part of the screen, particularly helpful for users with high
resolution or multi-display workstations.

## Indicators

We've been improving Indicator support from release to release for some
time now. But with in Ubuntu MATE 17.10 many of the panel layouts offer
a complete line up of Indicators, all of which are fully compatible
with MATE. The default Indicators are:

  * Optimus (*only available if you have nvidia prime capable hardware and drivers*)
  * Bluetooth
  * Network
  * Power
  * Messages
  * Sound
  * Session

{:.center}
![Indicators](/images/blog/layouts/indicators.png)

## MATE Tweak

MATE Tweak is your gateway to activating different user interface
layouts and exploring the contrasting ways you can run Ubuntu MATE.
MATE Tweak has been given a coat of fresh paint and adds a couple of
much requested features.

  * Saving your own custom panel layout using a name of your choosing.
  * Prompts before executing operations that could wipe your custom, but unsaved, tweaks.
  * **NEW in 17.10 Beta 1** - You can also delete previously saved custom panel layouts.

{:.center}
![MATE Tweak, more than just a tweak tool.](/images/blog/layouts/mate-tweak.png)

When activating the Compton compositor you should now experience an
entirely tear free experience that is optimised for gaming. Thanks to
[Perdro Mateus](https://plus.google.com/+PedroMateus) from
[Linux Game Cast](https://linuxgamecast.com/) podcast for his help test
the various GPU, IGP and driver combinations. [`#LGCCares`](https://twitter.com/hashtag/LGCCares?src=hash)

While we were tuning compositors we gave some love to Compiz, which now
uses less RAM and fixes a number of niggles.

## Community Wallpaper

The Ubuntu MATE community participated in a [wallpaper competition](https://ubuntu-mate.community/tags/wallpaper-comp-17-10)
and have already [voted for their favourite](https://ubuntu-mate.community/t/vote-for-the-default-wallpaper-in-ubuntu-mate-17-10/14079?u=wimpy).
Congratulations to [Richard van Liessum](https://ubuntu-mate.community/u/richard)
for creating the winning entry! You have to install Ubuntu MATE 17.10
to see the full line up of new artwork though `;-)`

## Slick Greeter

**NEW in 17.10 Beta 1** - We've switched to Slick Greeter which still
uses LightDM under the hood but has a much nicer look and feel.

{:.center}
![Slick Greeter](/images/blog/layouts/slick-greeter.png)

## File manager

**NEW in 17.10 Beta 2** - We've added some new features to Caja, the
MATE file manager.

  * Added [Advanced bulk rename](https://tari.in/www/software/cajarename/).
  * Added [Hash checking](https://github.com/tristanheaven/gtkhash).
  * Replaced `caja-gksu` with `caja-admin`.
    * The obsolete `gksu` is being removed from Debian and we are aligning with that objective by replacing the use of `gksu` with PolicyKit.
  * Updated [Folder Color](http://foldercolor.tuxfamily.org/). Now supports custom emblems and properly integrates with the Ubuntu MATE default icon theme.

{:.center}
![Caja Rename](/images/blog/layouts/caja-rename.png)

### The bit no one reads but probably should

  * **Ubuntu MATE Welcome 17.10.14** has been stocked with even more new applications for you to discover and
    * The *all new* Software Boutique is not ready yet, so this is the Boutique you know and love. Just better stocked.
  * Upgraded to **MATE HUD** 17.10.9-0ubuntu1 which fixes broken event replay due to synchronous key grab.
  * Upgraded to **MATE Optimus** 17.10.1-1ubuntu0 which now features nvidia hardware detection, including external Thunderbolt connected devices.
  * The **Ubuntu MATE themes have been improved** via the release of `ubuntu-mate-artwork` 17.10.10
    * Several improvements Plymouth splash screens, both text and graphical varieties.
    * Add missing panel-grid to Radiant-MATE.
    * **Improve linked button styling for message dialogs**.
    * Add syntax for panel-grid image to support MATE 1.20.
    * Improve **clock-applet-button so it is consistent with other buttons**.
    * Add top `border-radius` for `.titlebar > headerbar` - *workaround for incorrect upstream use of the GTK API*
    * **Improved notebook (tab) styling**.
    * Updated GtkSourceView themes (used by text editors).
    * **Add bold style classes for Global Menu**.
    * Fix color of grey-out arrows in menus.
    * Fix padding of primary/secondary image in GtkEntry.
    * Improve menu items by adding slightly more padding.
    * Add a minimal padding to na-tray-applets.
    * Add the Ubuntu MATE logo as the distributor-logo.
    * Fix incorrect CSS syntax for Caja.
    * Fix world-map border color in clock-applet.
    * Fix GtkScale slider mouse-selection if slider is out of range.
    * Fix height of headerbar for `metacity-theme-viewer` - *workaround for incorrect upstream use of the GTK API*
    * Fix border color of scrollbars.
    * Remove obsolete chrom{e|ium} styling.
    * Remove unwanted backdrop states.
  * Many of the Ubuntu MATE defaults have been changed or updated
    * **Replaced `lightdm-gtk-greeter` with `slick-greeter`.**
    * Added keybindings for <kbd>Shift</kbd> + <kbd>Print Screen</kbd> to grab a screen area when taking a screenshot.
    * **Added defaults for Chromium**, which will show the [Ubuntu MATE Start](https://start.ubuntu-mate.org) page, *should you install it*.
    * Added sane defaults and tookit integration for `smplayer`, *should you install it*.
  * **New Ubiquity Slide Show**
    * Completely redesigned to introduce users to more of the features unique to Ubuntu MATE.
    * **Added Ubuntu MATE logo to Ubiquity**.
  * Migrated `gdebi` to PolicyKit - *Thanks Simon Quigley*
  * Experimental HiDPI support is a little less experimental.
  * ...and a whole lot of other little improvements and fixes.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 17.10"
    text = "We've even redesigned the download page so it's even easier to get started."
    button_text = "Download"
    button_url = "/download/"
%}

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * *Nothing critical.*

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * [The Ubiquity installer may auto select US keyboard layout](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1713664)
    * To work around this manually, select the correct regional keyboard layout for your computer.
  * [Ubiquity is uninstalling chosen locale language packs](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1713702)
    * After a successful installation, your computer may not have all the appropriate language packs installed.
    * To work around this issue, open **Language Support** in the Control Centre and follow the prompts to automatically install the required language packs.
  * [Ubiquity slide shows are missing for OEM installs of Ubuntu Budgie and Ubuntu MATE](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
