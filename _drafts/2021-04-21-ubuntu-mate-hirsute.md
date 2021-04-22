---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-hirsute-hippo-final-release/
category: release
author: Martin Wimpress & Monica Ayhens-Madon
lang: en
discourse_topic_id: 23969

title: Ubuntu MATE 21.04 Release Notes
description: What's new in Ubuntu MATE 21.04 (Hirsute Hippo)

---

**Can you smell 👃 that? That's the smell of fresh paint 🖌 with just a hint of
cucumber 🥒**

Ubuntu MATE 21.04 is here and it has a new look thanks to the collaboration with
the [Yaru team](https://github.com/ubuntu/yaru). This release marks the start of a new visual direction for Ubuntu MATE, while
retaining the features you've come to love 💚 Read on to learn 🎓 what we've
been working on over the last 6 months and get some insight to what we'll be
working on next.

We would like to take this opportunity to extend our thanks 🙏 to everyone who
contributed to this release, including:

  * The Yaru team for welcoming us so warmly 🤗 into the Yaru project and for all their hard work during this development cycle
  * The Ayatana Indicator team who helped add new features and fix bugs that improved the indicator experience
  * Everyone who participated in the QA/testing and bug filing 🐛
  * Those of you who have been contributing to documentation and translations

Thank you! Thank you all very much indeed 🥰

{:.center}
![Ubuntu MATE 21.04](/images/blog/hirsute/hirsute-hippo-desktop.png)
**Ubuntu MATE 21.04 (Hirsute Hippo)**

# What changed since the Ubuntu MATE 20.10?

Here are the highlights of what's changed since the release of Groovy 🕶
Gorilla 🦍

## MATE Desktop 🧉

The [MATE Desktop](https://mate-desktop.org) team released **maintenance 🔧
updates for the current stable 1.24 release of MATE**. We've updated the
[MATE packaging in Debian](https://salsa.debian.org/debian-mate-team) to
incorporate all these **bug 🐛 fixes and translation updates** and synced those
packages to Ubuntu so they all feature in this 21.04 release. **There are no new
features, just fixes** 🩹

## Ayatana Indicators 🚥

A highlight of the [Ubuntu MATE 20.10 release](https://ubuntu-mate.org/blog/ubuntu-mate-groovy-gorilla-release-notes/)
was the transition to Ayatana Indicators. You can read 👓 the [20.10 release
notes](https://ubuntu-mate.org/blog/ubuntu-mate-groovy-gorilla-release-notes/) to
learn what Ayatana Indicators are and why this transition will be beneficial in the
long term.

We've added new versions of Ayatana Indicators including **'Indicators' settings
to the Control Center**, which can be used to configure the installed
indicators.

{:.center}
![Ayatana Indicator Settings](/images/blog/hirsute/ayatana-settings.png)
**Ayatana Indicators Settings**

Other indicator changes include:

  * **Added Printer Indicator** 🖨 which replaces the legacy printer applet
  * **Removed [RedShift](http://jonls.dk/redshift/)**
    * We ran into a show stopper 🛑 bug 🐞 that prevented it's inclusion in 21.04
    * We'll either re-introduce RedShift in a future release or adopt [a potential alternative solution from the Ayatana Indicator project](https://github.com/AyatanaIndicators/ayatana-indicator-display/issues/14)

Expect to see more Ayatana Indicators included in future releases of Ubuntu
MATE. Top candidates are:

  * Display Indicator - *needs uploading to Debian and Ubuntu*
  * Messages Indicator - *needs uploading to Debian and Ubuntu*
    * **`ayatana-webmail` is available for install in Ubuntu MATE 21.04**
  * Keyboard Indicator - *requires feature parity with MATE keyboard applet*
  * Bluetooth Indicator - *requires integration work with Blueman*

## Yaru MATE 🎨

This is where most of the work was invested 💦

**A new derivative of the Yaru theme, called Yaru MATE, has been created in
collaboration with the Yaru team.** During our discussions with the Yaru team we
decided to make one significant departure from how Yaru MATE is delivered;
**Yaru MATE is only providing a light and dark theme**, with the light theme
being default. This differs from Yaru in Ubuntu which features a mixed
light/dark by default.

**We've decided to offer only light and dark variants of Yaru MATE as it makes
maintaining the themes much easier**, the mixed light/dark Yaru theme does
require extra work to maintain due to the edge cases it surfaces. **Offering just
light and dark variants also ensures better application compatibility.**

This work touched on a number of projects, here's what Ubuntu MATE now enjoys as
a result of Yaru MATE:

  * **GTK 2.x, 3.x and 4.x Yaru MATE light and dark themes**
  * **Suru icons** along with a number of **new icons specifically made for MATE Desktop and Ubuntu MATE**
  * **LibreOffice Yaru MATE icon theme, which are enabled by default** on new installs
  * **Font contrast is much improved** throughout the desktop and applications
  * **Websites honour dark mode at the operating system level**
    * If you enable the Yaru MATE Dark theme, websites that provide a dark mode will automatically use their dark theme to match your preferences.

In return for the excellent theme and icons from the Yaru team, the Ubuntu MATE
team worked on the following which are now features of Yaru and Yaru MATE:

  * **Pixel perfect Marco/Metacity/Compiz window manager theme** that matches Yaru GNOME Shell window rendering
    * All icons in these themes are **SVG for improved HiDPI support**
  * **[GTKSourceView 2.x, 3.x and 4.x style](https://github.com/ubuntu/yaru/pull/2546)**
    * Based on [Vanilla colour palette](https://vanillaframework.io/docs/settings/color-settings)

As a result of our window manager and GTKSourceView contributions it is now
possible to use all three upstream Yaru themes from Ubuntu in Ubuntu MATE 💪

{:.center}
![Yaru MATE GTKSourceView](/images/blog/hirsute/yaru-mate-gtksourceview.png)
**Yaru MATE GTKSourceView, Tiled Windows and Plank theme**

### Going the extra mile 🎽

In order to make Yaru MATE shine we've also created:

  * **Plank themes that match Yaru MATE for side and bottom docks**
  * **Patched Marco window manager disable shadows on side-tiled windows**
    * The Yaru and Yaru MATE window manager themes feature clean edge styling for side tiled windows
  * **Multiple colour variants of Yaru MATE are available via Ubuntu MATE Welcome**
  * **[Published a Yaru MATE GTK theme snap in the Snap Store](https://snapcraft.io/gtk-theme-yaru-mate)**
  * **[Published a Yaru MATE icon theme snap in the Snap Store](https://snapcraft.io/icon-theme-yaru-mate)**
  * **[Published a Yaru MATE PPA for users of Ubuntu MATE 20.04 LTS](https://www.omgubuntu.co.uk/2021/04/install-yaru-mate-theme-20-04)**

#### Yaru MATE Snaps

`snapd` will soon be able to automatically install snaps of themes that match
your currently active theme. The snaps we've created are ready to integrate
with that capability when it is available.

The `gtk-theme-yaru-mate` and `icon-theme-yaru-mate` snaps are pre-installed in
Ubuntu MATE, but are not automatically connected to snapped applications.
Running the following commands in a terminal periodically, or after you install
a snapped GUI application, will connect the themes to compatible snaps until
such time `snapd` supports doing this automatically.

```
for PLUG in $(snap connections | grep gtk-common-themes:gtk-3-themes | awk '{print $2}'); do sudo snap connect ${PLUG} gtk-theme-yaru-mate:gtk-3-themes; done
for PLUG in $(snap connections | grep gtk-common-themes:gtk-2-themes | awk '{print $2}'); do sudo snap connect ${PLUG} gtk-theme-yaru-mate:gtk-2-themes; done
for PLUG in $(snap connections | grep gtk-common-themes:icon-themes | awk '{print $2}'); do sudo snap connect ${PLUG} icon-theme-yaru-mate:icon-themes; done
```

### What's next? 🔮

While we made lots of progress with Yaru MATE for 21.04, the work is on going.
Here's what we'll be working on next:

  * Some symbolic icons are being provided by a fallback to the Ambiant MATE and Radiant MATE icon themes, something we are keen to address for Ubuntu MATE 21.10.
  * Ubuntu MATE doesn't have a full compliment of Suru icons for MATE Desktop, yet.
  * Plymouth boot theme will be aligned with the EFI respecting theme shipped in Ubuntu.

## Mutiny 🏴‍☠️

The Mutiny layout, which provides a desktop layout that somewhat mimics Unity,
has been a source of bug reports and user frustration 😤 for sometime now.
Switching to/from Mutiny has often crashed resulting in a broken desktop
session 😭

We have **removed MATE Dock Applet from Ubuntu MATE** and **refactored the
Mutiny layout to use Plank** instead.

{:.center}
![Mutiny layout with Yaru MATE Dark](/images/blog/hirsute/yaru-mate-mutiny-dark.png)
**Mutiny layout with Yaru MATE Dark**

  * **Switching to the Mutiny layout via MATE Tweak will automatically theme Plank**
    * Light and dark Yaru themes for Plank are included
  * Mutiny **no longer enables Global Menus and also doesn't undecorate maximised
windows by default**
    * If you like those features you can **enable them via MATE Tweak**
  * **Window Buttons Applet is no longer integrated** in the Mutiny top panel by default.
    * You can manually add it to your custom panel configuration should you want it.
    * **Window Buttons Applet has been updated to automatically use window control buttons from the active theme**. HiDPI support is also improved.

As a result of these changes Mutiny is more reliable and retains much of the
Unity look and feel that many people like.

## Command line love 🧑‍💻

We've included a few popular utilities requested by command line warriors.
**`neofetch`, `htop` and `inxi` are all included in the default Ubuntu MATE
install.** `neofetch` also features an Ubuntu MATE ASCII logo.

## Raspberry Pi images

We will release Ubuntu MATE 21.04 images for the Raspberry Pi in the days
following the release for PC 🙂

## Major Applications

Accompanying **MATE Desktop 1.24.1** and **Linux 5.11** are **Firefox 87**, **LibreOffice 7.1.2.2**, **Evolution 3.40** & **Celluloid 0.20**.

{:.center}
![Major Applications](/images/blog/hirsute/versions.png)

See the [Ubuntu 21.04 Release Notes](https://discourse.ubuntu.com/t/hirsute-hippo-release-notes/19221)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 21.04"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

# Upgrading from Ubuntu MATE 20.10

You can upgrade to Ubuntu MATE 21.04 from Ubuntu MATE 20.10. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c` into the command box.
  * Update Manager should open up and tell you: New distribution release '21.04' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

# Known Issues

Here are the known issues.

{% include partials/known-issues.html filter="21.04" %}

# Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
