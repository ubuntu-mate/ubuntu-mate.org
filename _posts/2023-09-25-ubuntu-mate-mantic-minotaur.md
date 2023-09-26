---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-mantic-minotaur-release-notes/
category: pre-release
author: Martin Wimpress
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 23.10 Release Notes
description: What's new in Ubuntu MATE 23.10 (Mantic Minotaur)
gallery:
    - image: /images/blog/lunar/Lunar-Lobster-Explorer.jpg
      caption: null
---

Ubuntu MATE 23.10 is more of what you like, stable MATE Desktop on top of current Ubuntu.
This release rolls up a number of bugs fixes and updates that continues to build on recent releases, where the focus has been on improving stability 🪨

## Thank you! 🙇

**I'd like to extend my sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏 From reporting bugs, submitting translations, providing patches, contributing to [our crowd-funding](https://www.patreon.com/ubuntu_mate), developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this fabulous website. Thank you! 💚

## What changed since the Ubuntu MATE 23.04?

Here are the highlights of what's changed since the [release of Ubuntu MATE 23.04](https://ubuntu-mate.org/blog/ubuntu-mate-lunar-lobster-release-notes/)

### MATE Desktop

[MATE Desktop](https://mate-desktop.org) has been updated to 1.26.2 with a selection of bugs fixes 🐛 and minor improvements 🩹 to associated components.

- `caja-rename` 23.10.1-1 has been ported from Python to C.
- `libmatemixer` 1.26.0-2+deb12u1 resolves heap corruption and application crashes when removing USB audio devices.
- `mate-desktop` 1.26.2-1 improves portals support.
- `mate-notification-daemon` 1.26.1-1 fixes several memory leaks.
- `mate-system-monitor` 1.26.0-5 now picks up libexec files from `/usr/libexec`
- `mate-session-manager` 1.26.1-2 set `LIBEXECDIR` to `/usr/libexec/` for correct interaction with `mate-system-monitor` ☝️
- `mate-user-guide` 1.26.2-1 is a new upstream release.
- `mate-utils` 1.26.1-1 fixes several memory leaks.

<!--
#### AI Generated wallpapers (yet again!)

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of Research Platforms at Queen Mary University of London managing the Apocrita HPC cluster service. **Once again, Simon has created **some stunning **AI-generated** 🤖🧠 ** for Ubuntu MATE using bleeding edge diffusion models** 🖌 *The samples below are 1920x1080 but the versions included in Ubuntu MATE 23.04 are 3840x2160*.

{% include blog/gallery.html %}

Here's what Simon has to say about the process of creating these new wallpapers for Lunar Lobster:

> My usual workflow involves checking reddit, etc for the latest techniques, and then installing the latest open-source tools and checkpoints for unlimited experimentation (e.g. stable diffusion), plus some selective use of Dall-e and Midjourney, while trying not to exhaust my credits. I then experiment with lot of different prompts (including negative prompts to discourage certain features), settings, styles and ideas from each tool to see what sort of images I can get, then tweak and evolve my approach based on the results.

> Lobsters are fascinating creatures, but in real life, I find them a bit ugly, with all those antennae and legs akimbo. For the theme of "Lunar Lobster", rather precise anatomy, I explored ideas of stylised alien robotic space lobsters, lunar landers and other lobster-themed spacecraft. After a producing a shortlist of varied images, I then perform any necessary AI processing such as inpainting, outpainting (generating new parts of an image beyond the existing canvas - particularly useful for getting the correct aspect ratio) and AI upscaling to make them suitable for use as wallpaper.
-->

## Major Applications

Accompanying **MATE Desktop 1.26.2** 🧉 and **Linux 6.5** 🐧 are **Firefox 118** 🔥🦊,
**Celluloid 0.25** 🎥, **Evolution 3.50** 📧, **LibreOffice 7.6.1** 📚

See the [Ubuntu 23.10 Release Notes](https://discourse.ubuntu.com/t/mantic-minotaur-release-notes/35534)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 23.10"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 23.04

You can upgrade to Ubuntu MATE 23.10 from Ubuntu MATE 23.04. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" drop down menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c -d` into the command box.
  * Update Manager should open up and tell you: New distribution release '23.10' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

## Known Issues

Here are the known issues.

{% include partials/known-issues.html filter="23.10" %}

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
