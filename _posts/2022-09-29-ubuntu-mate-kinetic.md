---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-kinetic-kudu-release-notes/
category: dev                                # Beta Only - change to 'release'
author: Martin Wimpress
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 22.10 Release Notes
description: What's new in Ubuntu MATE 22.10 (Kinetic Kudu)
gallery:
    - image: /images/blog/kinetic/kudu-field.jpg
      caption: null
    - image: /images/blog/kinetic/kudu-foresty.jpg
      caption: null
    - image: /images/blog/kinetic/kudu-grass.jpg
      caption: null
    - image: /images/blog/kinetic/kudu-standalone.jpg
      caption: null
    - image: /images/blog/kinetic/kudu-verdant.jpg
      caption: null
---

Ubuntu MATE 22.10 is a modest update by recent standards and focused on *"quality
of life improvements"*. And there is good reason why this release of Ubuntu MATE
doesn't feature the usual bucket 🪣 list of changes you'd typically expect, and
that's because I've been helping bring the full Ubuntu MATE experience to Debian
MATE 🧉

This may raise some questions for Ubuntu MATE users, so let's try and address them:

 - **I'm not stepping away from Ubuntu or Ubuntu MATE**. I will continue to use and develop Ubuntu MATE 👍
 - I've closely collaborated with the MATE packaging team for Debian for over 8 years 👴
 - Making the MATE experience in Debian and Ubuntu consistent **makes maintenance easier for all involved** 🛠
 - Ubuntu MATE offers some modernisation of MATE via home-grown apps such as MATE Tweak and Ayatana Indicators. **We want Debian users to benefit from those improvements too** 💖
 - We're hopeful the MATE spin in Debian 12 will offer the same (or extremely similar) experience Ubuntu MATE users have enjoyed for some time 🎁

## Thank you! 🙇

**I'd like to extend my sincere thanks to everyone who has played an active role
in improving Ubuntu MATE for this release 👏 From reporting bugs,
submitting translations, providing patches, contributing to
[our crowd funding](https://www.patreon.com/ubuntu_mate),
developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this
fabulous website. Thank you! Thank you all for getting out there and making a
difference!** 💚

{:.center}
![Ubuntu MATE 22.10](/images/blog/kinetic/kinetic-kudu-desktop.jpg)
**Ubuntu MATE 22.10 using the Pantheon layout and new centered panel applets and HUD**

## What changed since the Ubuntu MATE 22.04?

Here are the highlights of what's changed since the [release of Ubuntu MATE 22.04](https://ubuntu-mate.org/blog/ubuntu-mate-jammy-jellyfish-release-notes/)

### MATE Desktop

The usual point release updates to [MATE Desktop](https://mate-desktop.org) and
[Ayatana Indicators](https://github.com/AyatanaIndicators) have been included
that fix 🩹 an assortment on minor bugs 🐛 **The main change in MATE Desktop
is to MATE Panel**, where we've included an early snapshot release of `mate-panel`
1.27.0 along with a patch set that **adds centre alignment of panel applets**.

This much requested feature comes from Ubuntu MATE community contributor
[Gordon N. Squash](https://github.com/thesquash) 🇺🇸 and allows panel applets to
be centre aligned, as well as the usual left and right alignment. I'm sure
you'll all join me in thanking 🙇 Gordon for working on this feature.

**Centre aligning of applet icons will ship with MATE Desktop 1.28, but we're
including it early 🐓 for Ubuntu MATE users**. We've updated MATE Tweak to
correctly save/restore custom layouts that use centre aligned applets and all
the panel layouts shipped with Ubuntu MATE 22.10 have been updated so they're
compatible with center alignment of applets ✅

#### AI Generated wallpapers (again!)

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of
Research Platforms at Queen Mary University of London managing the Apocrita HPC
cluster service. **Once again, Simon has created some stunning AI generated 🤖🧠
wallpapers for Ubuntu MATE using bleeding edge diffusion models** 🖌 *The samples
below are 1920x1080 but the versions include in Ubuntu MATE 22.10 are 3840x2160*.

{% include blog/gallery.html %}

Here's what Simon has to say about about some of the challenges he faced
creating these new wallpapers for Kinetic Kudu:

> AI image generation is continuing to improve at a mind-boggling rate. Yet, until recently, coherent human faces, hands and anatomically correct animals have proved rather tricky. Fortunately human faces are getting particular attention in the open source community after the release of Stable Diffusion. However, while an anthropomorphic portrait of a Kudu wearing a rather dapper suit will be stylishly rendered, getting consistent results for kudu in their natural habitat proved particularly tricky, exacerbated by their elegant horn structure. Often you will get rather wild interpretations of the horns, 5 legged creatures, or nightmarish output akin to the Pushmi-Pullyu from the Dr Doolittle stories.

<div align="center"><blockquote class="twitter-tweet"><p lang="en" dir="ltr">AI-generated kudu are hard. They are happy posing for their portrait in a suit, but as soon as you want them to act normal, you get abominations like this double-headed beastie <a href="https://twitter.com/hashtag/stablediffusion?src=hash&amp;ref_src=twsrc%5Etfw">#stablediffusion</a> <a href="https://t.co/BgPR3QBqru">https://t.co/BgPR3QBqru</a> <a href="https://t.co/RVCbgMsOAh">pic.twitter.com/RVCbgMsOAh</a></p>&mdash; Simon Butcher (@simonjbutcher) <a href="https://twitter.com/simonjbutcher/status/1572574722612920322?ref_src=twsrc%5Etfw">September 21, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></div>

> Jellyfish, on the other hand, are a mass of tentacles and perhaps benefit aesthetically from the randomness induced by AI-generated images, in the same way that forests, mountains and hobbit villages generated by AI can be produced en-masse to a very satisfying extent. So while 1000 stunning unique images of jellyfish can be produced in a few minutes with a powerful GPU, the kudu was quite a challenge, and I had to experiment a lot with various prompts and styles, and a lot of cherry-picking - throwing away about 99% of the results that weren't quite right. For the next release, I'm hoping we'll see further AI innovation in time for the next release, or...maybe the next code name will be a lionfish?

### PipeWire

**PulseAudio has been replaced with PipeWire** and Bluetooth audio codec support
has been expanded with the addition of AAC, LDAC, aptX and aptX HD.

As a [podcaster](https://linuxdowntime.com/) and [streamer](https://twitch.tv/WimpysWorld)
I'm delighted to have PipeWire installed by default in Ubuntu MATE 22.10. The
migration to PipeWire has resolved some longstanding minor annoyances I've had
with audio in that past and all the tools 🧰 I use for audio and video
production continue to function correctly.

#### PipeWire on Ubuntu MATE 22.04

If you like to ride the LTS train 🚆 but want to use PipeWire in Ubuntu MATE
22.04 (*as I have been doing for some months*) then this is how to make the
change:

```bash
sudo apt-get install gstreamer1.0-pipewire pipewire-audio-client-libraries wireplumber
sudo apt-get remove pulseaudio-module-bluetooth
sudo apt-get install libfdk-aac2 libldacbt-abr2 libldacbt-enc2 libopenaptx0 libspa-0.2-bluetooth libspa-0.2-jack
```

Once the installs/removals are complete restart your computer.

### Ubuntu MATE Stuff

The *"MATE HUD"* has seen some significant work from community contributor
[twa022](https://github.com/twa022) 🌎. The **HUD now supports MATE, XFCE
and Budgie**, has improved accuracy for HUD placement (taking into account various
panel offsets/struts), **is highly configurable and includes a new HUD settings app** ✨

{:.center}
![HUD Settings](/images/blog/kinetic/hud-settings.png)
**HUD Settings**

#### MATE User Manager

**A new utility, User Manager, has been added to complement the suite of MATE
tools.** User Manager replaces the aging `gnome-system-tools` which was
removed from Ubuntu MATE in the 22.04 release and allows you to add/modify/remove
user accounts. It also includes the ability to define which users are Administrators,
enable/disable auto-login, set profile images and manage group memberships.

{:.center}
![MATE User Manager](/images/blog/kinetic/mate-user-manager.png)
**MATE User Manager**

#### Yaru

And last but not least, the Ubuntu MATE Artwork package has been updated to
**include all the refinements and improvements in the suite of
[Yaru](https://github.com/ubuntu/yaru) themes** 🎨

## Major Applications

Accompanying **MATE Desktop 1.26.1** 🧉 and **Linux 5.19** 🐧 are **Firefox 105** 🔥🦊,
**Celluloid 0.20** 🎥, **Evolution 3.46** 📧, **LibreOffice 7.4** 📚

See the [Ubuntu 22.10 Release Notes](https://discourse.ubuntu.com/t/kinetic-kudu-release-notes/27976)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 22.10"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 22.04

You can upgrade to Ubuntu MATE 22.10 from Ubuntu MATE 22.04. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" drop down menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c -d` into the command box.
  * Update Manager should open up and tell you: New distribution release '22.10' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

## Known Issues

Here are the known issues.

{% include partials/known-issues.html filter="22.10" %}

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
