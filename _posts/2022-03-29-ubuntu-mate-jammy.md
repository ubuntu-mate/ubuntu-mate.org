---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-jammy-jellyfish-release-notes/
category: dev                                # Beta Only - change to 'release'
author: Martin Wimpress
lang: en
discourse_topic_id: 25318

title: Ubuntu MATE 22.04 LTS Release Notes
description: What's new in Ubuntu MATE 22.04 LTS (Jammy Jellyfish)
gallery:
    - image: /images/blog/jammy/jelly3.jpg
      caption: null
    - image: /images/blog/jammy/jelly4.jpg
      caption: null
    - image: /images/blog/jammy/jelly6.jpg
      caption: null
---

Ubuntu MATE 22.04 LTS is the culmination of 2 years of continual improvement 😅
to Ubuntu and MATE Desktop. As is tradition, the LTS development cycle has a
> We are preparing Ubuntu MATE 22.04 (Jammy Jellyfish) for distribution on
[April 21st, 2022](https://discourse.ubuntu.com/t/jammy-jellyfish-release-schedule/23906).
With this **Beta** pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<!--- End of Beta Only --->

Ubuntu MATE 22.04 is the culmination of 2 years of continual improvement 😅 to
Ubuntu and MATE Desktop. As is tradition, the LTS development cycle has a
keen focus on eliminating paper 🧻 cuts 🔪 but we've *jammed* in some new
features and a fresh coat of paint too 🖌 The following is a summary of what's
new [since Ubuntu MATE 21.10](/blog/ubuntu-mate-impish-indri-final-release/) and
some reminders of how we got here from 20.04. Read on to learn more 🧑‍🎓

## Thank you! 🙇

**I'd like to extend my sincere thanks to everyone who has played an active role
in improving Ubuntu MATE for this LTS release 👏 From reporting bugs,
submitting translations, providing patches, contributing to our crowd funding,
developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this
fabulous website. Thank you! Thank you all for getting out there and making a
difference!** 💚

{:.center}
![Ubuntu MATE 22.04 LTS](/images/blog/jammy/ubuntu-mate-mutiny-dark.png)
**Ubuntu MATE 22.04 LTS (Jammy Jellyfish) - Mutiny layout with Yark-MATE-dark**

<!--- Beta Only - Remove for final release --->

## What works? 🤔

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Beta Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who needs a stable system
  * Anyone uncomfortable running a possibly frequently broken system
  * Anyone in a production environment with data or workflows that need to be reliable

Ubuntu MATE *Beta Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE Desktop, Yaru and GTK+ developers.

<!--- End of Beta Only --->

## What's changed?

Here are the highlights of what's changed recently.

### MATE Desktop 1.26.1 🧉

Ubuntu MATE 22.04 features MATE Desktop 1.26.1. MATE Desktop 1.26.0 was introduced
in 21.10 and benefits from **significant effort 😅 in fixing bugs 🐛
in MATE Desktop, optimising performance ⚡ and plugging memory leaks**. MATE
Desktop 1.26.1 addresses the bugs we discovered following the initial 1.26.0
release. Our community also fixed some bugs in Plank and Brisk Menu 👍 and also
fixed the screen reader during installs for visually impaired users 🥰 In all
over 500 bugs have been addressed in this release 🩹

### Yaru 🎨

Ubuntu MATE 21.04 was the first release to ship with a MATE variant of the
[Yaru theme](https://github.com/ubuntu/yaru). A year later and we've been working
hard with members of the Yaru and Ubuntu Desktop teams to bring **full MATE
compatibility to upstream Yaru, including all the accent colour varieties.**
All reported bugs 🐞 in the Yaru implementation for MATE have also been fixed 🛠

{:.center}
![Yaru Themes](/images/blog/jammy/yaru-themes.png)
**Yaru Themes in Ubuntu MATE 22.04 LTS**

Ubuntu MATE 22.04 LTS ships with all the Yaru themes, including our own *"chelsea
cucumber"* version 🥒 The legacy Ambiant/Radiant themes are no longer
installed by default and neither are the stock MATE Desktop themes. We've added
an **automatic settings migration** to transition users who upgrade to an
appropriate Yaru MATE theme.

#### Cherries on top 🍒

In collaboration with [Paul Kepinski](https://github.com/Jupi007) 🇫🇷 (Yaru team)
and [Marco Trevisan](https://twitter.com/3v1n0) 🇮🇹 (Ubuntu Desktop
team) **we've added dark/light panels and panel icons to Yaru for MATE Desktop
and Unity**. I've added a collection of new dark/light panel icons to Yaru for
popular apps with indicators such as Steam, Dropbox, [uLauncher](https://ulauncher.io/),
[RedShift](http://jonls.dk/redshift/), [Transmission](https://transmissionbt.com/),
Variety, etc.

{:.center}
![Light Panel](/images/blog/jammy/panel-light.png)
![Dark Panel](/images/blog/jammy/panel-dark.png)
**Light and Dark panels**

I've added patches 🩹 to the Appearance Control Center that **applies theme
changes to Plank (the dock), Pluma (text editor) and correctly toggles the
colour scheme preference for GNOME 42 apps**. When you choose a dark theme,
everything will go dark in unison 🥷 and vice versa.

So, **Ubuntu MATE 22.04 LTS is now using everything Yaru/Suru has to offer.** 🎉

#### AI Generated wallpapers

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of
Research Platforms at Queen Mary University of London managing the Apocrita HPC
cluster service. He's been creating AI 🤖 generated art using bleeding edge
CLIP guided diffusion models 🖌 The results are pretty incredible and we've
[included the 3 top voted "Jammy Jellyfish" in our wallpaper selection](https://twitter.com/m_wimpress/status/1504030749451862026)
as their vivid and vibrant styles compliment the Yaru accent colour theme options
very nicely indeed 😎

{% include blog/gallery.html %}

If you want the complete set, here's a tarball  of all 8 wallpapers at 3840x2160:

  * [AI Generated *"Jammy Jelly"* by Simon Butcher](https://people.ubuntu.com/~flexiondotorg/Jammy_Jellyfish_AI_Wallpapers.tar.xz) 🎁 (22MB)

### Ubuntu MATE stuff 🧉

Ubuntu MATE has a few distinctive apps and integrations of it's own, here's a
run down of what's new and shiny ✨

#### MATE Tweak

Switching layouts with MATE Tweak is its most celebrated feature. We've improved
the reliability of desktop layout switching and restoring custom layouts is now 100%
accurate 💯

{:.center}
![Ubuntu MATE Desktop Layouts](/images/blog/jammy/panel-layouts.png)
**Having your desktop your way in Ubuntu MATE**

We've removed `mate-netbook` from the default installation of Ubuntu MATE and
as a result the Netbook layout is no longer available. We did this because
`mate-maximus`, a component of `mate-netbook`, is the cause of some
compatibility issues with client side decorated (CSD) windows. There are still
several panel layouts that offer efficient resolution use 📐 for those who need
it.

**MATE Tweak has refreshed its supported for 3rd party compositors.** Support for
Compton has been dropped, as it is no longer actively maintained and
**comprehensive support for [picom](https://github.com/yshui/picom) has been added**.
`picom` has three compositor options: Xrender, GLX and Hybrid. All three are
can be selected via MATE Tweak as the performance and compatibility of each
varies depending on your hardware. **Some people choose to use `picom` because
they get better gaming performance or screen tearing is reduced. Some just
like subtle animation effects `picom` adds** 💖

#### MATE HUD

Recent versions of `rofi`, the tool used by MATE HUD to visualise menu
searches, has a new theme system. **MATE HUD has been updated to support this
new theme engine and comes with two MATE specific themes (`mate-hud` and
`mate-hud-rounded`) that automatically adapt to match the currently selected
GTK theme**.

You can add your own `rofi` themes to `~/.local/share/rofi/themes`. Should you
want to, you can use any `rofi` theme in MATE HUD. Use <kbd>Alt</kbd> + <kbd>F2</kbd>
to run `rofi-theme-selector` to try out the different themes, and if there is
one you prefer you can set it as default by using running the following in a terminal:

```bash
gsettings set org.mate.hud rofi-theme <theme name>
```

{:.center}
![MATE HUD](/images/blog/jammy/mate-hud.png)
**MATE HUD uses the new rofi theme engine**

#### Windows & Shadows

I've updated the Metacity/Marco (the MATE Window Manager) themes in Yaru to make
sure they match GNOME/CSD/Handy windows for a consistent look and feel across
all window types 🪟 and 3rd party compositors like `picom`. I even patched how
Marco and `picom` render shadows so windows they look cohesive regardless of
toolkit or compositor being used.

#### Ubuntu MATE Welcome & Boutique

The Software Boutqiue has been restocked with software for 22.04 and
**Firefox 🔥🦊 ESR (`.deb`) has been added to the Browser Ballot in Ubuntu MATE Welcome.**

{:.center}
![Ubuntu MATE Welcome Browser Ballot](/images/blog/jammy/firefox-esr.png)
**Comprehensive browser options just a click away**

### 41% less fat 🍩

Ubuntu MATE, like it's lead developer, was starting to get get a bit large
around the mid section 😊 **During the development of 22.04, the image 📀 got
to 4.1GB 😮**

So, we put Ubuntu MATE on a strict diet 🥗  We've removed the proprietary NVIDIA
drivers from the local apt pool on the install media and thanks to migrating
fully to Yaru (which now features excellent de-duplication of icons) and also
removing our legacy themes/icons. And now the Yaru-MATE themes/icons are
completely in upstream Yaru, we were able to remove 3 snaps from the default
install and **the image is now a much more reasonable 2.7GB; 41% smaller.** 🗜

This is important to us, because **the majority of our users are in countries
where Internet bandwidth is not always plentiful**. Those of you with NVIDIA GPUs,
don't worry. If you tick the 3rd party software and drivers during the install
the appropriate driver for your GPU will be downloaded and installed 👍

{:.center}
![Install 3rd party drivers](/images/blog/jammy/install-3rd-party.png)
**NVIDIA GPU owners should tick *Install 3rd party software and drivers* during install**

While investigating 🕵 [a bug in Xorg Server that caused Marco (the MATE window manager)
to crash](https://pad.lv/1959995) **we discovered that Marco has lower frame time
latency ⏱ when using Xrender with the NVIDIA proprietary drivers**. **We've
published a PPA where NVIDIA GPU users can install a version of Marco that uses
Xpresent for optimal performance** ⚡

```bash
sudo apt-add-repository ppa:ubuntu-mate-dev/marco
sudo apt upgrade
```

Should you want to revert this change you install `ppa-purge` and run the
following from a terminal: `sudo ppa-purge -o ubuntu-mate-dev -p marco`.

#### But wait! There's more! 😲

These reductions in size are after **we added three new applications to the default
install on Ubuntu MATE: GNOME Clocks, Maps and Weather** My family and I 👨‍👩‍👧 have
found these applications particularly useful and use them regularly on our
laptops without having to reach for a phone or tablet.

{:.center}
![GNOME Clocks, Maps & Weather](/images/blog/jammy/gnome-clocks-maps-weather.png)
**New additions to the default desktop application in Ubuntu MATE 22.04 LTS**

For those of you who like a minimal base platform, then **the minimal install
option is still available which delivers just the essential Ubuntu MATE Desktop
and Firefox browser.** You can then build up from there 👷

#### Packages, packages, packages 📦

It doesn't matter how you like to consume your Linux 🐧 packages, Ubuntu MATE
has got you covered with **PPA, Snap, AppImage and FlatPak support baked in
by default.** You'll find `flatpak`, `snapd` and `xdg-desktop-portal-gtk` to
support Snap and FlatPak and the (ageing) `libfuse2` to support AppImage are all
pre-installed.

Although `flatpak` is installed, [FlatHub](https://flathub.org/home) is not
enabled by default. To enable FlatHub run the following in a terminal:

```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

**We've also included `snapd-desktop-integration` which provides a bridge
between the user's session and `snapd` to integrate theme preferences 🎨 with
snapped apps** and can also automatically install snapped themes 👔
**All the Yaru themes shipped in Ubuntu MATE are fully snap aware**.

### Ayatana Indicators

Ubuntu MATE 20.10 transitioned to [Ayatana Indicators](https://github.com/AyatanaIndicators) 🚥
As a quick refresher, Ayatana Indicators are a fork of Ubuntu Indicators that
aim to be cross-distro compatible and re-usable for any desktop environment 👌

**Ubuntu MATE 22.04 LTS comes with Ayatana Indicators 22.2.0 and sees the
return of Messages Indicator 📬 to the default install**. Ayatana Indicators now
provide improved backwards compatibility to Ubuntu Indicators and no longer
requires the installation of two sets of libraries, saving RAM, CPU cycles and
improving battery endurance 🔋

{:.center}
![Ayatana Indicator Settings](/images/blog/jammy/ayatana-settings.png)
**Ayatana Indicators Settings**

To compliment the BlueZ 5.64 protocol stack in Ubuntu, Ubuntu MATE ships
**Blueman 2.2.4 which offers comprehensive management of Bluetooth devices and
much improved pairing compatibility** 💙🦷

I also patched `mate-power-manager`, `ayatana-indicator-power` and Yaru to **add
support for battery powered gaming input devices, such as controllers 🎮 and joysticks 🕹**

### Active Directory

And in case you missed it, the Ubuntu Desktop team added the option to enroll
your computer into an Active Directory domain 🔑 during install. Ubuntu MATE
has supported the same capability since it was first made available in the
20.10 release.

### Raspberry Pi image 🥧

  * Should be available very shortly after the release of 22.04.

### Major Applications

Accompanying **MATE Desktop 1.26.1** and **Linux 5.15** are **Firefox 99.0**,
**Celluloid 0.20**, **Evolution 3.44** & **LibreOffice 7.3.2.1**

See the [Ubuntu 22.04 Release Notes](https://discourse.ubuntu.com/t/jammy-jellyfish-release-notes/24668)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 22.04 Beta"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 20.04 LTS and 21.10

You can upgrade to Ubuntu MATE 22.04 LTS from Ubuntu MATE either 20.04 LTS or
21.10. Ensure that you have all updates installed for your current version of
Ubuntu MATE before you upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" drop down menu to "For long-term support versions" if you are using 20.04 LTS; set it to "For any new version" if you are using 21.10.
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c -d` into the command box.
  * Update Manager should open up and tell you: New distribution release 'XX.XX' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

## Known Issues

Here are the known issues.

{% include partials/known-issues.html filter="22.04" %}

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
