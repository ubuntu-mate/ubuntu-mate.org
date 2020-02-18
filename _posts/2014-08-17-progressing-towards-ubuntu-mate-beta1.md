---
layout: blog-post
class: blog
title: Progressing towards Ubuntu MATE Beta1
permalink: /blog/progressing-towards-ubuntu-mate-beta1/
description:
category: news
author: Martin Wimpress
lang: en
---

A few days ago I was asked [what is the current status of Ubuntu MATE,
what is outstanding and what help do we require](https://plus.google.com/101312215214323407176/posts/4WefGfx765p)
via [our Ubuntu MATE Google+ community](https://plus.google.com/communities/108331279007926658904).
I thought it best to reply here to reach a wide audience.

# Ubuntu MATE as an official Ubuntu flavor

Towards the end of July the Ubuntu MATE team contacted the
[Ubuntu Technical Board](https://wiki.ubuntu.com/TechnicalBoard)
to request official flavor status.

  * [Ubuntu MATE Remix is seeking official flavor status](https://lists.ubuntu.com/archives/technical-board/2014-July/001979.html)

The Ubuntu MATE team made an Ubuntu 14.04 PPA for MATE 1.8.1 as a
result of our initial communication with the Ubuntu Technical Board.

  * [MATE for Trusty](https://launchpad.net/~ubuntu-mate-dev/+archive/ubuntu/trusty-mate)

popey attended an Ubuntu Technical Board meeting in early August to find
out what our next steps should be. During this meeting it was established
that the Ubuntu Technical Board are supportive of Ubuntu MATE and the
[Ubuntu MATE team needs to complete some formalities](https://lists.ubuntu.com/archives/technical-board/2014-August/001989.html)
before we can progress our request. The Ubuntu MATE team will complete
the outstanding actions requested by the Ubuntu Technical Board in the
coming days and I am confident Ubuntu MATE will achieve official status
in due course.

# Ubuntu MATE Beta1 progress

Ubuntu MATE Beta1 is progressing nicely and is mainly focused on tweaking
the themes and adding Ubuntu MATE specific artwork. The Ubuntu MATE
community have been brilliant in this regard and contributed Ubuntu
MATE wallpapers, LightDM theme, Plymouth theme and new desktop themes.
A [SYSLINUX theme](http://imgur.com/jTEEdGV) is currently in the works.

Some general improvements have also been made during the Beta1 cycle,
such as desktop policy privilege fixes, meta package improvements and
aligning the core packages with the other Ubuntu flavors.

I needed a few evenings break from for Ubuntu MATE, so I gave the bot
in the [Ubuntu MATE IRC channel](/irc/) a personality and modified the
Ubuntu MATE webserver to only deliver content over HTTPS using
[HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security),
[PFS](https://www.eff.org/deeplinks/2013/08/pushing-perfect-forward-secrecy-important-web-privacy-protection)
(perfect forward secrecy) and [SPDY](http://en.wikipedia.org/wiki/SPDY).

Consequently the [Ubuntu MATE website has an A+ rating](https://www.ssllabs.com/ssltest/analyze.html?d=ubuntu-mate.org)
from SSL Labs and we are doing our bit to [Reset the Net](https://www.resetthenet.org/).

# Assistance required?

These are the areas where we could use some help.

## Bugs

There are a couple of bugs, not show stoppers, that we could you some
help with.

### Plymouth

We've got a lovely Ubuntu MATE Plymouth theme but due to a recent
`plymouth` update no Plymouth themes are displayed at boot. This is an
upstream Ubuntu bug. If you have a Launchpad account please visit the
bug reports below, mark them as affecting you and provide any additional
information to assist in their resolution.

  * [plymouth 0.9.0 can not use framebuffer for terminal: none](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1356513)
  * [boot animation did not appear](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1343841)

### Minimizing Chrome or Chromium

Do you have an nVidia graphics card and dual screens? If so, could you
please install Ubuntu MATE, install the proprietary nVidia driver,
install Chrome or Chromium and see if you can reproduce the issue reported below.

  * [minimize chrome or chromium](https://bugs.launchpad.net/ubuntu-mate/+bug/1354826)

If you can, please add as much information to the bug report as possible
because right now we not sure if this is a MATE, Chrom(e|ium) or
nVidia issue.

## Ubiquity slides

When you install Ubuntu, or one of the flavours, a series of slides
are shown during the installation. We need some Ubuntu MATE specific
slides creating because we are currently using the official Ubuntu
slides. [If this is something you could help with, then please let us know](/community/).

## Folder icons

Ubuntu MATE will come with two new themes, Ambiant-MATE (derived from Ambiance)
and Radiant-MATE (derived from Radiance). I am considering replacing the
folder icons in these new themes with ones that use MATE green (`#87A752`)
as the base colour for the folders. I have reached out to the
[RAVEfinity](http://www.ravefinity.com/) project and they are willing to
help the Ubuntu MATE team. I would like to off-load the task of
collaborating with RAVEfinity to someone in the Ubuntu MATE community.
[If you are interested, then please let us know](/community/).

## Test and report issues

This is where you can really make a difference to the quality of the
Ubuntu MATE final release. We need people actually using Ubuntu MATE in
order to uncover potential problems so we can fix them *before* the
final release.

Please install Ubuntu MATE, either in a Virtual Machine (VM) or on real hardware and use
it as much as possible. If you spot any issues please report them on the
Ubuntu MATE bug tracker.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Artwork Team

We'd like to establish an Ubuntu MATE artwork team who can drive the
artwork and design efforts. There are clearly several members of the
Ubuntu MATE community who are already interested in this area. If you
would like to join them then [please let us know](/communty/) so we can
formalise the team structure.

# No show stoppers

At this point in the Beta1 cycle there are no show stoppers and we
continue to get daily reports from new users saying how impressed they
are with the stability of Ubuntu MATE, even at this early stage.

As of right now, we are on track for an August 28th release of Ubuntu
MATE Beta1.

Is there anything you can help with or want to be involved in? Maybe you
just want to discuss your experiences or ask the maintainers some questions.
Please [come and talk to us](/community/).
