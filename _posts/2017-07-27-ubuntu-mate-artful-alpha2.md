---
layout: blog-post
class: blog
title: Ubuntu MATE 17.10 Alpha 2
permalink: /blog/ubuntu-mate-artful-alpha2/
description: Ubuntu MATE 17.10 (Artful Aardvark) Alpha 2
category: dev
author: Martin Wimpress
lang: en
old_comments_topic_id: 21325

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

# Welcome Unity 7 refugees! *This* is the Ubuntu flavour you've been searching for

**We're not happy, proud, pleased or ambivalent to announce this alpha.
No, not us. The is our most "*Super*" alpha ever and we're ecstatic
to present this fine release for your distro delectation. Ubuntu MATE
17.10 is brimming with new toys to play with. Read on to find out more...**

*We mean it, keep reading! Don't just go hunting for the download button
and skip over our most glorious release notes.*

We are preparing Ubuntu MATE 17.10 (Artful Aardvark) for distribution on
[October 19th, 2017](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseSchedule)
With this *Alpha* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

{:.center}
![Ubuntu MATE 17.10 Alpha 2](/images/blog/1710-alpha2-medium.png)

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

# What changed since the Ubuntu MATE 17.04 final release?

We've really been burning the midnight oil for the last three months.
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

Global Menu support is now much improved, and available via the
**Contemporary**, **Cupertino** and **Mutiny** layouts which can be
**activated via MATE Tweak**. Fully functional with GTK, Qt,
LibreOffice, Firefox/Thunderbird, Google Chrome, Electron and others.
You can now make more of your available screen space while using Ubuntu
MATE.

{:.center}
![Global Menu](/images/blog/layouts/global-menu.gif)

## Super key

{.right}
![Super Key](/images/blog/layouts/superkey.png)

Complete Super key support is available from several of the panel
layouts. We're thrilled to welcome [Victor
Kareh](https://github.com/vkareh/) to the [team](/team/) who has been
busy patching [MATE Settings Daemon](https://github.com/mate-desktop/mate-settings-daemon),
[MATE Menu](https://github.com/ubuntu-mate/mate-menu),
[Brisk Menu](https://github.com/solus-project/brisk-menu) and
[MATE Dock Applet](https://github.com/robint99/mate-dock-applet) to
make the Super key work the way you'd all expect. This means Super can
be used to activate the menus and other key-bindings that include the
Super key also continue to function correctly.

MATE Dock Applet, used in the Mutiny layout, also includes launching or
switching to  docked items based on their position using in the dock
using `Super+1`, `Super+2` which will be familiar to Unity 7 users.
`Super+L` is also recognised as a screen lock key-binding along with the
usual `Ctrl+Alt+L` that MATE Desktop users expect.

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

{:.center}
![The MATE Heads-Up Display (HUD)](/images/blog/layouts/mate-hud.gif)

Just like Global Menus the HUD is currently only available via the
**Contemporary**, **Cupertino** and **Mutiny** layouts and is activated
via `Super+Alt`.

## Indicators

We've been improving Indicator support from release to release for some
time now. But with this release many of the panel layouts offers a
complete line up of Indicators, all of which are fully compatible with
MATE. The default Indicators are:

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

{:.center}
![MATE Tweak, more than just a tweak tool.](/images/blog/layouts/mate-tweak.png)

When activating the Compton compositor you should now experience an
entirely tear free experience that is optimised for gaming. Thanks to
[Perdro Mateus](https://plus.google.com/+PedroMateus) from
[Linux Game Cast](https://linuxgamecast.com/) podcast for his help testing
various GPU, IGP and driver combinations. [#LGCCares](https://twitter.com/hashtag/LGCCares?src=hash)

While we were tuning compositors we gave some love to Compiz, which now
uses less RAM and fixes a number of niggles.

## Community Wallpaper

The Ubuntu MATE community participated in a [wallpaper competition](https://ubuntu-mate.community/tags/wallpaper-comp-17-10)
and have already [voted for their favourite](https://ubuntu-mate.community/t/vote-for-the-default-wallpaper-in-ubuntu-mate-17-10/14079?u=wimpy).
Congratulations to [Richard van Liessum](https://ubuntu-mate.community/u/richard)
for creating the winning entry! You have to install Ubuntu MATE 17.10
to see the full line up of new artwork though `;-)`

### The bit no one reads but probably should

  * **Ubuntu MATE Welcome 17.10.7** has been stocked with some new applications for you to discover.
    * The new Software Boutique is not ready yet, so this is the Boutique you know and love. Just better stocked.
  * **Brisk Menu 0.4.5** has improved Super key support and numerous fixes, plus a few settings that MATE Tweak can manipulate to augment how Brisk is presented in different layouts.
  * **MATE Menu 17.10.7** now has better relevance of launcher search results, can now optionally search Duck Duck Go, has numerous fixes and that all important Super key was improved.
  * **MATE Dock Applet 0.79** has improved Super key support and several bug fixes.
  * [Redshift](http://jonls.dk/redshift/), which adjusts the colour temperature of your screen according to your surroundings, is installed by default but not enabled by default.
  * Synapse is removed from the default install.
  * MATE Desktop 1.18 has seen many updates, with lots of bugs fixes. Nothing new, just be more stability.
    * mate-session-manager 1.18.1
    * mate-panel 1.18.4
    * mate-control-center 1.18.2
    * mate-media 1.18.1
    * mate-panel 1.18.3
    * libmateweather 1.18.1
    * engrampa 1.18.2
    * mate-netbook 1.18.1
    * mate-sensors-applet 1.18.2
    * mate-panel 1.18.2
    * caja 1.18.3
    * marco 1.18.1
    * mate-polkit 1.18.1
    * eom 1.18.2
    * mate-utils 1.18.2
    * pluma 1.18.2
    * mate-icon-theme-faenza 1.18.1
    * mate-terminal 1.18.1
    * mate-icon-theme 1.18.2
  * Caja now includes the [GtkHash](https://github.com/tristanheaven/gtkhash) extension *(will be installed with your next update)*
  * Experimental HiDPI support is a little less experimental.
    * If you kept reading that ^ is for you. Also see that massive image of the Indicators above. Not an accident `;-)`
  * ...and a whole lot of other little improvements and fixes.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 17.10"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/download/"
%}

## Known Issues

Here are the known issues.

### Ubuntu MATE

* **MATE Tweak**: [Custom panel layout doesn't show in the panel list tab.](https://bugs.launchpad.net/ubuntu-mate/+bug/1706810)

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * *tbc*

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
