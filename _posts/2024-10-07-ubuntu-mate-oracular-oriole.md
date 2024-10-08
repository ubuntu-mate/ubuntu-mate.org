---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-oracular-oriole-release-notes/
category: release
author: Martin Wimpress
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 24.10 Release Notes
description: What's new in Ubuntu MATE 24.10 LTS (Oracular Oriole)
---

Ubuntu MATE 24.10 is more of what you like, stable MATE Desktop on top of current Ubuntu. Read on to learn more 👓️

{:.center}
![Ubuntu MATE 24.10](/images/blog/oracular/screenshot.png)
**Ubuntu MATE 24.10**

## Thank you! 🙇

**My sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏
I'd like to acknowledge the close collaboration with the Ubuntu Foundations team and the Ubuntu flavour teams, in particular [Erich Eickmeyer](https://launchpad.net/~eeickmeyer) who pushed critical fixes while I was travelling.
Thank you!** 💚

## What changed since the Ubuntu MATE 24.04 LTS?

Here are the highlights of what's changed since the [release of Ubuntu MATE 24.04](https://ubuntu-mate.org/blog/ubuntu-mate-noble-numbat-release-notes/)

- Ships stable [MATE Desktop](https://mate-desktop.org) 1.26.2 with a handful of bug fixes 🐛
- Switched back to Slick Greeter (replacing Arctica Greeter) due to race-condition in the boot process which results the display manager failing to initialise.
  - Returning to Slick Greeter reintroduces the ability to easily configure the login screen via a graphical application, something users have been requesting be re-instated 👍

{:.center}
![Login Window Configuration](/images/blog/oracular/login-window.png)
**Login Window**

## What didn't change since the Ubuntu MATE 24.04 LTS?

If you follow upstream MATE Desktop development, then you'll have noticed that Ubuntu MATE 24.10 doesn't ship with the recently released MATE Desktop 1.28 🧉

I have prepared packaging for MATE Desktop 1.28, along with the associated components but encountered some bugs and regressions 🐞 I wasn't able to get things to a standard I'm happy to ship be default, so it is tried and true MATE 1.26.2 one last time 🪨

## Major Applications

Accompanying **MATE Desktop 1.26.2** 🧉 and **Linux 6.11** 🐧 are **Firefox 131** 🔥🦊,
**Celluloid 0.27** 🎥, **Evolution 3.54** 📧, **LibreOffice 24.8.2** 📚

See the [Ubuntu 24.10 Release Notes](https://discourse.ubuntu.com/t/oracular-oriole-release-notes/44878/1)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 24.10"
    text = "Ubuntu MATE 24.10 (Oracular Oriole) is available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading to Ubuntu MATE 24.10

The upgrade process to Ubuntu MATE 24.10 is the same as Ubuntu.

- [Ubuntu 24.10 Upgrade Process](https://help.ubuntu.com/community/OracularUpgrades)

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.
