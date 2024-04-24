---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-lunar-lobster-release-notes/
category: release
author: Martin Wimpress
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 23.04 Release Notes
description: What's new in Ubuntu MATE 23.04 (Lunar Lobster)
gallery:
    - image: /images/blog/lunar/Lunar-Lobster-Explorer.jpg
      caption: null
    - image: /images/blog/lunar/Lunar-Lobster-Landing.jpg
      caption: null
    - image: /images/blog/lunar/Lunar-Lobster-Steampunk.jpg
      caption: null
    - image: /images/blog/lunar/Lunar-Lobster.jpg
      caption: null
---

Ubuntu MATE 23.04 is the least exciting Ubuntu MATE release ever. The good news is, if you liked Ubuntu MATE 22.10 then it is more of the same; just with better artwork! 🖌️🖼️ I entered this development cycle full of energy and enthusiasm off the back of the [Ubuntu Summit in Prague](https://ubuntu.com/blog/ubuntu-summit-2022-reflections), but then I was seriously ill 🤒 and had a long stay in hospital. I'm recovering well and should be 100% in a couple of months. This setback and also changing jobs a couple of months ago has meant that I've not been able to invest the usual time and effort into Ubuntu MATE. I'm happy to say that I've been able to deliver another solid 🪨 release with the help of the Ubuntu community.

## Thank you! 🙇

**I'd like to extend my sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏 From reporting bugs, submitting translations, providing patches, contributing to [our crowd-funding](https://www.patreon.com/ubuntu_mate), developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this fabulous website. Thank you! 💚

## What changed since the Ubuntu MATE 22.10?

Here are the highlights of what's changed since the [release of Ubuntu MATE 22.10](https://ubuntu-mate.org/blog/ubuntu-mate-kinetic-kudu-release-notes/)

### MATE Desktop

Both [MATE Desktop](https://mate-desktop.org) and
[Ayatana Indicators](https://github.com/AyatanaIndicators) have seen some version bumps that fix 🩹 an assortment of minor bugs 🐛

#### AI Generated wallpapers (yet again!)

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of Research Platforms at Queen Mary University of London managing the Apocrita HPC cluster service. **Once again, Simon has created **some stunning **AI-generated** 🤖🧠 ** for Ubuntu MATE using bleeding edge diffusion models** 🖌 *The samples below are 1920x1080 but the versions included in Ubuntu MATE 23.04 are 3840x2160*.

{% include blog/gallery.html %}

Here's what Simon has to say about the process of creating these new wallpapers for Lunar Lobster:

> My usual workflow involves checking reddit, etc for the latest techniques, and then installing the latest open-source tools and checkpoints for unlimited experimentation (e.g. stable diffusion), plus some selective use of Dall-e and Midjourney, while trying not to exhaust my credits. I then experiment with lot of different prompts (including negative prompts to discourage certain features), settings, styles and ideas from each tool to see what sort of images I can get, then tweak and evolve my approach based on the results.

> Lobsters are fascinating creatures, but in real life, I find them a bit ugly, with all those antennae and legs akimbo. For the theme of "Lunar Lobster", rather precise anatomy, I explored ideas of stylised alien robotic space lobsters, lunar landers and other lobster-themed spacecraft. After a producing a shortlist of varied images, I then perform any necessary AI processing such as inpainting, outpainting (generating new parts of an image beyond the existing canvas - particularly useful for getting the correct aspect ratio) and AI upscaling to make them suitable for use as wallpaper.

### Flatpak

[Flatpak is no longer installed by default](https://discourse.ubuntu.com/t/ubuntu-flavor-packaging-defaults/34061), but can still be installed should you want to use it.

### PipeWire

As a [podcaster](https://linuxdowntime.com/) and [streamer](https://twitch.tv/WimpysWorld) I'm delighted to have PipeWire installed by default since Ubuntu MATE 22.10. The Ubuntu MATE meta packages have been updated to correctly install the revised pipewire packages in Ubuntu. Special thanks to Erich Eickmeyer, from the Ubuntu Studio project, for his work on this.

## Major Applications

Accompanying **MATE Desktop 1.26.1** 🧉 and **Linux 6.20** 🐧 are **Firefox 111** 🔥🦊,
**Celluloid 0.20** 🎥, **Evolution 3.48** 📧, **LibreOffice 7.5.2** 📚

See the [Ubuntu 23.04 Release Notes](https://discourse.ubuntu.com/t/lunar-lobster-release-notes/31910)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 23.04"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 22.10

You can upgrade to Ubuntu MATE 23.04 from Ubuntu MATE 22.10. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" drop down menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c -d` into the command box.
  * Update Manager should open up and tell you: New distribution release '23.04' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
