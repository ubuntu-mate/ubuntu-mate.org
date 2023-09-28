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
    - image: /images/blog/mantic/minotaur-king.jpg
      caption: null
---

Ubuntu MATE 23.10 is more of what you like, stable MATE Desktop on top of current Ubuntu.
This release rolls up a number of bugs fixes and updates that continues to build on recent releases, where the focus has been on improving stability 🪨

{:.center}
![Ubuntu MATE 23.10](/images/blog/mantic/screenshot.png)
**Ubuntu MATE 23.10**

## Thank you! 🙇

**I'd like to extend my sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏 From reporting bugs, submitting translations, providing patches, contributing to [our crowd-funding](https://www.patreon.com/ubuntu_mate), developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this fabulous website. Thank you!** 💚

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

#### Yet more AI Generated wallpaper

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of Research Platforms at Queen Mary University of London managing the Apocrita HPC cluster service. **Once again, Simon has created a stunning AI-generated 🤖🧠 wallpaper for Ubuntu MATE using bleeding edge diffusion models** 🖌 *The sample below is 1920x1080 but the version included in Ubuntu MATE 23.10 are 3840x2160*.

{% include blog/gallery.html %}

Here's what Simon has to say about the process of creating this new wallpaper for Mantic Minotaur:

> Since Minotaurs are imaginary creatures, interpretations tend to vary widely. I wanted to produce an image of a powerful creature in a graphic novel style, although not gruesome like many depictions. The latest open source Stable Diffusion XL base model was trained at a higher resolution and the difference in quality has been noticeable, particularly at better overall consistency and detail, while reducing anatomical irregularities in images. The image was produced locally using Linux and an NVIDIA A100 80GB GPU, starting from an initial text prompt and refined using img2img, inpainting and upscaling features.

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
