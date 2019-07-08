---
layout: blog-post
class: blog
title: Ubuntu MATE Remix Alpha 2
permalink: /blog/ubuntu-mate-alpha2
category: dev
author: Martin Wimpress
lang: en
---

We are delighted to announce the release of Ubuntu MATE Alpha 2.

{% include blog/jumbotron.html
    title = "Ubuntu MATE Remix Alpha 2 Download"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/utopic/"
%}

## What works?

Most things, more than in Alpha 1 at least.

The .iso image should boot (from DVD or USB), the Live session should
work, the installer should work and the installed system should also
work. Notice the heavy use of *"should*", YMMV.

## What changed since Alpha 1?

  * Added support for booting UEFI computers. [LP #1337604](https://bugs.launchpad.net/ubuntu-mate/+bug/1337604)
  * Added *"out of the box"* accessibility for blind or visually impaired individuals. [LP #1337824](https://bugs.launchpad.net/ubuntu-mate/+bug/1337824)
  * Added `language-selector-gnome` as per [community request](https://plus.google.com/104108115467526996500/posts/5gmt5y4893m).
  * Added `ubuntu-mate-settings` package to provide sane defaults.
  * Added an Ubuntu-like panel layout.
  * Added Ambiance and Radiance themes to Pluma.
  * Added Rhythmbox and Totem plugins.
  * Added Release Notes to Ubquity.
  * Added support for Marco to Ubiquity. [MERGE #226114](https://code.launchpad.net/~ubuntu-mate-dev/ubiquity/ubiquity-marco/+merge/226114)
  * Fixed Network Manager applet.
  * Fixed inconsistent theme in live session installer.
  * Fixed default icons in LibreOffice.
  * Created custom `livecd-rootfs` package that tracks upstream.
  * Improved the seeds and meta packages.
  * Improved Ambiance and Radiance themes.
  * Improved `mono-icons` to better integrate with MATE. [LP #1337577](https://bugs.launchpad.net/ubuntu-mate/+bug/1337577)
  * Improved font rendering.
  * Removed `remmina` as per community [Remmina poll](https://plus.google.com/103917631499285627130/posts/gFv4xRH16P8).
  * Removed `caja-image-converter`.
  * Removed `caja-share`. [LP #1342206](https://bugs.launchpad.net/ubuntu-mate/+bug/1342206).
  * Removed `mate-user-share`.

## Known Issues

Ubuntu MATE 14.10 is currently an alpha distribution and we are aware of the following issues:

  * Upgrading from Ubuntu MATE Alpha1 using `apt-get` is not supported.
    * We Recommend that you install a clean Alpha2.
  * Most Shotwell online publishing plugins do not work. [LP #1314904 ](https://bugs.launchpad.net/ubuntu/+source/shotwell/+bug/1314904)
    * This can be resolved by installing `unity-control-center-signon` but doing so installs a number of Unity packages which add duplicate functionality to the MATE Control Centre.

### Reporting issues

If you spot any other issues please report them on the project's bug tracker.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Testing

Ubuntu MATE is in alpha and therefore we need people installing and
using Ubuntu MATE and reporting any issues you may find on the
project's bug tracker.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

Is there anything you can help with or want to be involved in? Maybe
you just want to discuss your experiences or ask the maintainers some
questions. Please [come and talk to us](/community/).

