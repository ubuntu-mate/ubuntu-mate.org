---
layout: blog-post
title: Ubuntu MATE 18.10 Beta
permalink: ubuntu-mate-cosmic-beta
description: Ubuntu MATE 18.10 (Cosmic Cuttlefish) Beta
category: dev
author: Martin Wimpress
lang: en
---

**Ubuntu MATE 18.10 is a modest, yet strategic, upgrade over our 18.04
release. If you want bug fixes and improved hardware support then 18.10 is for
you. For those who prefer staying on the LTS then everything in this 18.10
release is also important for the upcoming 18.04.2 release. Read on to learn
more...**

We are preparing Ubuntu MATE 18.10 (Cosmic Cuttlefish) for distribution on
[October 18th, 2018](https://wiki.ubuntu.com/CosmicCuttlefish/ReleaseSchedule)
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<p align="center">
[Ubuntu MATE 18.10 Beta](/gallery/blog/1810-beta.jpg) Superposition on the Intel Core i7-8809G Radeon RX Vega M powered Hades Canyon NUC

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Beta Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who needs a stable system
  * Anyone uncomfortable running a possibly frequently broken system
  * Anyone in a production environment with data or workflows that need to be reliable

Ubuntu MATE *Beta Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE, and GTK+ developers

## What changed since the Ubuntu MATE 18.04 final release?

Curiously, the work during this Ubuntu MATE 18.10 release has really been
focused on what will become Ubuntu MATE 18.04.2. Let me explain.

### MATE Desktop

The upstream MATE Desktop team have been working on many bug fixes for MATE
Desktop 1.20.x, that has resulted in a lot of maintenance updates in the
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

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 18.10 Beta</h1>
        <p>We've even redesigned the download page so it's even easier to get started.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * The Software Boutique doesn't list any available software.
    * An update, due very soon, will re-stock the software library and add a few new applications too.

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * The [ISO may not boot on VirtualBox](https://pad.lv/1792932).
    * This appears to impact Ubuntu (proper) more than Ubuntu MATE. It is an intermitent problem on Ubuntu MATE and simply resetting the VM may work on the next boot. If not, press a key when the initial boot prompt (Man and Keyboard) is displayed, then press F6 and select `nomodeset` and press ENTER to boot.

  * The ISO boots fine and installation works as expected on On QEMU/Libvirt, but it sometimes fails to boot post-install.
    * This [may be due to Plymouth crashing](https://pad.lv/1794280), investigations are underway.

  * [Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
