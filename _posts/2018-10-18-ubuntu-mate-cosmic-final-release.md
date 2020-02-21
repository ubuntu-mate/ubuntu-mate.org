---
layout: blog-post
class: blog
title: Ubuntu MATE 18.10 Final Release
permalink: /blog/ubuntu-mate-cosmic-final-release/
description: Ubuntu MATE 18.10 (Cosmic Cuttlefish) Final Release
category: release
author: Martin Wimpress
lang: en
---

**Ubuntu MATE 18.10 is a modest, yet strategic, upgrade over our 18.04
release. If you want bug fixes and improved hardware support then 18.10 is for
you. For those who prefer staying on the LTS then everything in this 18.10
release is also important for the upcoming 18.04.2 release. Oh yeah, we've
also made a [bespoke Ubuntu MATE 18.10 image for the GPD Pocket and GPD Pocket
2](/ports/umpcs/). Read on to learn more...**

{:.center}
![Ubuntu MATE 18.10](/images/blog/1810-final.jpg) Superposition on the Intel Core i7-8809G Radeon RX Vega M powered Hades Canyon NUC

## What changed since the Ubuntu MATE 18.04 final release?

Curiously, the work during this Ubuntu MATE 18.10 release has really been
focused on what will become Ubuntu MATE 18.04.2. Let me explain.

### MATE Desktop

The upstream MATE Desktop team have been working on many bug fixes for **MATE
Desktop 1.20.3**, that has resulted in a lot of maintenance updates in the
upstream releases of MATE Desktop. The Debian packaging team for MATE Desktop,
of which I am member, has been updating all the MATE packages to track these
upstream bug fixes and new releases. Just about all MATE Desktop packages and
associated components, such as AppMenu and MATE Dock Applet have been updated.
Now that all these fixes exist in the 18.10 release, we will start the process
of SRU'ing (backporting) them to 18.04 so that they will feature in the Ubuntu
MATE 18.04.2 release due in February 2019. The fixes should start landing in
Ubuntu MATE 18.04 very soon, well before the February deadline.

### Hardware Enablement

Ubuntu MATE 18.04.2 will include a hardware enablement stack (HWE) based on
what is shipped in Ubuntu 18.10. Ubuntu users are increasingly adopting the
current generation of AMD RX Vega GPUs, both discrete and integrated solutions
such as the Intel Core i7-8809G Radeon RX Vega M found in the Hades Canyon NUC
and some laptops. I have been lobbying people within the Ubuntu project to
upgrade to newer versions of the Linux kernel, firmware, Mesa and Vulkan that
offer the best possible "out of box" support for AMD GPUs. Consequently,
Ubuntu 18.10 (of any flavour) is great for owners of AMD graphics solutions
and these improvements will soon be available in Ubuntu 18.04.2 too.

### GPD Pocket

Alongside the generic image for 64-bit Intel PCs we're also releasing a
bespoke image for the [GPD Pocket](https://www.gpd.hk/gpdpocket) and
[GPD Pocket 2](https://www.gpd.hk/gpdpocket2) that includes the hardware
specific tweaks to get these devices working *"out of the box"*
without any faffing about. [See our GPD Pocket page for more details](/ports/umpcs/).

{:.center}
![Ubuntu MATE 18.10 running on the GPD Pocket (left) and GPD Pocket 2 (right)](/images/blog/gpd-pockets.jpg)

{:.caption}
**Ubuntu MATE 18.10 running on the GPD Pocket (left) and GPD Pocket 2 (right)**

## Raspberry Pi images

We're planning on releasing **Ubuntu MATE images for the Raspberry Pi after
that 18.10 release is out, in October 2018**. It takes usually takes about a
month to get the Raspberry Pi images built and tested, but we've encountered
some challenges with the 18.04 based images which has delayed their release.
Hopefully we'll have something in time for Christmas 2018 `:-)`

## Major Applications

Accompanying **MATE Desktop 1.20.3** and **Linux 4.18** are **Firefox
59.0.2**, **VLC 3.0.4**, **LibreOffice 6.1.2.1** and **Thunderbird 60.2.1**.

{:.center}
![Major Applications](/images/blog/cosmic/versions.png)

See the [Ubuntu 18.10 Release
Notes](https://wiki.ubuntu.com/CosmicCuttlefish/ReleaseNotes) for details of all
the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 18.10"
    text = "We've even redesigned the download page so it's even easier to get started."
    button_text = "Download"
    button_url = "/download/"
%}

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * Nothing significant.

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * [After installing an Ubuntu 18.10 flavour alongside an existing Ubuntu 18.10 install, the resized filesystem is corrupted](https://pad.lv/1798562).
    * It has not been reported to happen if the original operating system is something other than Cosmic.
  * [When installing while preserving existing data, an error message is displayed](https://pad.lv/1798369), which is due to `Could not get lock /target/var/cache/apt/archives/lock`
    * The packages installed originally are not reinstalled and must be reinstalled manually. Although the user data is preserved.
  * [The screen reader is not auto-enabled on first login even if it's been enabled during installation](https://pad.lv/1796275).
  * [In an OEM installation, during user setup, the language selected is not taken into account](https://pad.lv/1798554).
  * [When disconnecting from VPNs, DNS resolution may become broken](https://pad.lv/1797415) requiring a restart of systemd-resolved`.
    * `sudo systemctl restart systemd-resolved.service`
  * [Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
