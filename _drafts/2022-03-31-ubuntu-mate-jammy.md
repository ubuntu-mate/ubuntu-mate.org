---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-jammy-jellyfish-release-notes/
category: dev                                # Beta Only - change to 'release'
author: Martin Wimpress
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 22.04 Release Notes
description: What's new in Ubuntu MATE 22.04 (Jammy Jellyfish)

---

<!--- Beta Only - Remove for final release --->

> We are preparing Ubuntu MATE 22.04 (Jammy Jellyfish) for distribution on
April 21st, 2022](https://discourse.ubuntu.com/t/jammy-jellyfish-release-schedule/23906).
With this **Beta** pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<!--- End of Beta Only --->


Ubuntu MATE 22.04 is the culmination of 2 years of continual improvement 😅 to
Ubuntu and MATE Desktop. As is tradition, the development cycle for a LTS has a
keen focus on eliminating paper 🧻 cuts 🔪 but we've jammed in some new
features too and a fresh coat of paint 🖌 What follows is a summary of how
Ubuntu MATE has evolved since 20.04, so read on to learn 🧑‍🎓 more.

**I'd like to extend my sincere thanks to everyone who has played an active role
in improving Ubuntu MATE for this LTS release :clap: From reporting bugs,
submitting translations, providing patches, contributing to our crowd funding,
developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this
fabulous website. Thank you! Thank you all for getting out there and making a
difference!** :green_heart:

{:.center}
![Ubuntu MATE 22.04](/images/blog/jammy/jammy-jellyfish-desktop.png)
**Ubuntu MATE 22.04 (Jammy Jellyfish).**

<!--- Beta Only - Remove for final release --->

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Beta Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who needs a stable system
  * Anyone uncomfortable running a possibly frequently broken system
  * Anyone in a production environment with data or workflows that need to be reliable

Ubuntu MATE *Beta Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE, and GTK+ developers.

<!--- End of Beta Only --->


## What changed since the Ubuntu MATE 20.04 (Focal Fossa) LTS?

Here are the highlights of what's changed since the [release of 22.04](/blog/ubuntu-mate-focal-fossa-release-notes/)

### MATE Desktop 1.26.1 🧉

Ubuntu MATE 22.04 features MATE Desktop 1.26.1. MATE Desktop 1.126 was first
introduced in 21.10 and benefits from **significant effort 😅 in fixing bugs 🐛
in MATE Desktop, optimising performance ⚡ and plugging memory leaks**.

### Yaru 🎨

Ubuntu MATE 21.04 was the first release to ship with a MATE variant of Yaru. A
year later and we've been working hard with members of the Yaru and Ubuntu Desktop
teams to bring **full MATE compatibility to upstream Yaru, including all the
accent colour varieties.** All reported bugs 🐞 in the Yaru implementation for
MATE have been fixed 🩹

Ubuntu MATE 22.04 ships with all the Yaru themes, including our own chelsea
cucumber (MATE) version 🥒 The legacy Ambiant/Radiant themes are no longer
installed by default, neither are the MATE Desktop themes selection. We've
add an **automatic settings migration** to transition users who upgrade to an
appropriate Yaru MATE theme.

#### Cherry on top 🍒

In collaboration with Paul K from the Yaru team and Marco T from the Ubuntu Desktop
team, **we've added dark/light panel icons to Yaru for MATE Desktop and Unity.
So Ubuntu MATE 22.04 finally fully uses Yaru and Suru icons throughout.**

I updated the Metacity/Marco (the MATE Window Manager) themes in Yaru to make
sure they match GNOME/CSD/Handy windows for a consistent look and feel across
all window types.

I've added patches to Appearance Properties in Ubuntu MATE to **apply theme
changes to Plank (the dock), Pluma (text editor) and correctly toggle dark mode
preference for GNOME 42 apps**.

### 38% less fat 🍩

Ubuntu MATE, like it's lead developer, was starting to get a bit fat around the
mid section. **During the 22.04 cycle the image 📀 got to 4.1GB 😮** So, we've
removed the proprietary NVIDIA drivers from the local apt pool and thanks to
migrating fully to Yaru which features excellent de-duplication of icons and dropping
legacy themes/icons **the image is now a much more reasonable 28GB; 38% smaller.**

This is important to us, because **the majority of our users are in countries
where Internet bandwidth is not always plentiful**. Those of you with NVIDIA GPUs,
don't worry. If you tick the 3rd party software and drivers during the install
the appropriate driver for your GPU will be downloaded and installed 👍

#### But wait! There's more! 😲

These reductions in size are after **we added three new applications to the default
install on Ubuntu MATE: GNOME Clocks, Maps and Weather** My family and I have
found these three applications useful and use them regularly. Having these
available by default is one less reason to reach for my phone or tablet.

### Ayatana Indicators

Ubuntu MATE 20.10 transistion from Ubuntu Indicators to Ayatana Indicators. As a
quick refresher, Ayatana Indicators are a fork of Ubuntu Indicators that aims to be
cross-distro compatible and re-usable for any desktop environment 👌

Ubuntu MATE 22.04 ships the **latest versions of Ayatana Indicators and sees the
return Messages Indicator to the default install**. Ayatana Indicators now
provide improved backwards compatibility to Ubuntu Indicators and no longer
requires the installation of two sets of libraries, saving RAM, CPU styles while
improving battery endurance.

Other Ayatana Indicators available for install include:

  * Display Manager via `ayatana-indicator-display`
  * Webmail Notifier via `ayatana-webmail`

{:.center}
![Ayatana Indicator Settings](/images/blog/hirsute/ayatana-settings.png)
**Ayatana Indicators Settings**

To compliment BlueZ 5.64 protocol stack in Ubuntu, Ubuntu MATE ships
**Blueman 2.2.4 which offers comprehensive management of Bluetooth devices and
much improved pairing compatibility** 💙🦷

### Ubuntu MATE stuff 🧉

MATE Tweak & Layouts

- Layout switching and restoring
- picom
- Removed netbook. CSD bugs.
- Consistent shadows
- MATE HUD New `rofi`
- Plank default dock items is more comprehensive
I've also patched the MATE Window Manager so that
shadows are also consistent between client side decorated windows and 3rd party compositors like `picom`.

### Packages, packages, packages 📦

It doesn't matter how you like to consume your Linux 🐧 packages, Ubuntu MATE
has got you covered with **PPA, Snap, AppImage and FlatPak support baked in by
default.**

### Active Directory

The Ubuntu Desktop team added the option to enroll your computer into an
Active Directory domain 🔑 during install for 20.10. Ubuntu MATE has supported
the same capability since it was made available.

## Raspberry Pi images

(New Raspberry Pi images, or planned new images between now and the next
release, should go here. If no Raspberry Pi updates, delete.)

## Major Applications

Accompanying **MATE Desktop 1.26.1* and **Linux 5.15** are **Firefox 98.0.2**,
**Celluloid 0.20**, **Evolution 3.44** & **LibreOffice 7.3.2.1**

See the [Ubuntu 22.04 Release Notes](https://discourse.ubuntu.com/t/jammy-jellyfish-release-notes/24668)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 22.04"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 20.04 LTS and 21.10

You can upgrade to Ubuntu MATE 22.04 from Ubuntu MATE either 20.04 LTS or 21.10.
Ensure that you have all updates installed for your current version of Ubuntu
MATE before you upgrade.

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

{% include partials/known-issues.html filter="XX.XX" %}

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
