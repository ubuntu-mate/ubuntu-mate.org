---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-for-gpd-pocket3/
description: Ubuntu MATE 21.10 for GPD Pocket 3
category: release
author: Martin Wimpress
lang: en
title: Ubuntu MATE 21.10 for GPD Pocket 3
discourse_topic_id: 25056

---

In what has become something of a tradition, the Ubuntu MATE team have released
images for the [GPD Pocket 3](https://www.gpd.hk/gpdpocket3) modular handheld PC.
**Many thanks to the team at GPD for providing sample hardware for us to work with!**

{:.center}
![Ubuntu MATE 21.10 running on the GPD Pocket 3](/images/blog/gpd-pocket3-laptop.jpg)
**Ubuntu MATE 21.10 running on the GPD Pocket 3**

{% include blog/jumbotron.html

    title = "GPD Pocket 3 Download"
    text = "The Ubuntu MATE 21.10 image for GPD Pocket 3 is available for download now"
    button_text = "Downloads"
    button_url = "/download/"

%}

## Tweaks for the GPD Pocket 3:

All the hardware in the GPD Pocket 3 works with a modern Linux OS, but some
configuration tweaking is required to deliver an optimised *"out of box"*
experience. Here's what we did:

  * Enable frame buffer and Xorg display rotation.
  * **Accelerometer support for automatic screen rotation.**
    * Also automatically rotates touch screen and stylus (draw and erase)
  * Enable **fractional scaling by default**
    * Results in an effective resolution of ~1280x800 to make the display panels easily readable.
    * Simple to toggle on/off via the *Display Scaler* app if you want to restore full resolution.
  * Enable audio via the HDaudio legacy driver.
  * Suspend is implemented via `s2idle`
    * A temporary workaround until S3 sleep state is supported.
  * Enable scroll wheel emulation while holding down the centre trackpad button.
  * Enable Tear-Free rendering by default.
  * Enable double size console (tty) font resolution.

Sadly, no support for the fingerprint reader. AFAIK only USB fingerprint readers
are supported in Linux.

{:.center}
![Ubuntu MATE 21.10 running on the GPD Pocket 3 in Tablet mode](/images/blog/gpd-pocket3-tablet.jpg)
**Ubuntu MATE 21.10 running on the GPD Pocket 3 in Tablet mode**

{% include blog/jumbotron.html

    title = "More Details & Downloads"
    text = "Find out more about Ubuntu MATE for the GPD Pocket 3. Get the downloads!"
    button_text = "Details & Downloads"
    button_url = "/ports/umpcs/"

%}
