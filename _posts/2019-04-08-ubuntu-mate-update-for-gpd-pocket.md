---
layout: blog-post
class: blog
title: Ubuntu MATE 18.04 and 19.04 for GPD Pocket & Pocket 2
permalink: /blog/ubuntu-mate-update-for-gpd-pocket
description: Ubuntu MATE 18.04 and 19.04 for GPD Pocket & Pocket 2
category: release
author: Martin Wimpress
lang: en
---

Back in October 2018 the Ubuntu MATE team released bespoke images of Ubuntu
MATE 18.10 for the [GPD Pocket](https://gpd.hk/gpdpocket) and
[GPD Pocket 2](https://gpd.hk/gpdpocket2) that included hardware specific
tweaks to get these devices working *"out of the box"* without any faffing
about. **Today we are releasing Ubuntu MATE 18.04.2 and Ubuntu MATE 19.04
images for both devices**. Read on to find out more...

{:.center}
[Ubuntu MATE 18.04.2 running on the GPD Pocket (left) and 19.04 on the GPD Pocket 2 (right)](/gallery/blog/gpd-pockets-news.jpg)

{:.caption}
**Ubuntu MATE 18.04.2 running on the GPD Pocket (left) and 19.04 on the GPD Pocket 2 (right)**

# What's new?

## Ubuntu MATE 18.04.2

Thanks to the recent hardware enablement stack upgrade in Ubuntu it is now
possible to create images based on Ubuntu MATE 18.04.2 for the GPD Pocket and
GPD Pocket 2. [These images are final and available to download now!](https://ubuntu-mate.org/download/)

## Ubuntu MATE 19.04

The Ubuntu MATE 19.04 release is just days away, so we have also prepared
Ubuntu MATE 19.04 Beta images for both devices. [Also availble for download now](https://ubuntu-mate.org/download/)
and you can simply collect updates to get from the beta to final release on
April 18th 2019.

## Improvements

Thanks to the feedback and contributions from the community, these are the
improvement we've made since the Ubuntu MATE 18.10 images were created:

  * Frame buffer and Xorg display rotation now works with `modesetting` and `xorg-video-intel` display drivers.
  * Enabled **TearFree rendering by default**.
  * Updated touch screen rotation to support Xorg and Wayland.
  * Enabled an **emulated mouse scroll wheel**, activated by holding down the right track point button and moving the trackpoint up/down.
  * **GRUB is now usable post-install** for both devices!

{% include blog/jumbotron.html
    title = "More Details & Downloads"
    text = "Find out more about Ubuntu MATE for the GPD Pocket and Pocket 2. Get the downloads!"
    button_text = "/gpd-pocket/"
    button_url = "Details & Downloads"
%}
