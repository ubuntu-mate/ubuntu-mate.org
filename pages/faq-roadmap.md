---
layout: sidebar
permalink: /faq/roadmap/
lang: en
class: faq
sidebar: faq

title: Roadmap

---

# Outstanding Objectives

This page outlines some of the activities the Ubuntu MATE team will research,
and possibly implement, in future development cycles to improve and refine our
operating system.

{% include partials/toc.html %}

## Grow community participation and engagement

Ubuntu MATE and MATE Desktop are created by very small teams. We’ll improve our
documentation so that new contributors can find tasks they can work on and
material to help them get started.

## Developer tooling and collaboration

Ubuntu MATE and MATE Desktop will expand their use of continuous integration
and automated testing in an effort to save the small development teams burning
valuable time on activities best left to a bot.

Additionally, we will review the development platforms and communication/
collaboration tools used by the MATE Desktop team to improve team communication
and simplfy the project infrastructure where possible.

## Modern display server support

Wayland is set to become the defacto next generation display server. While Xorg
has some years of usefulness remaining, now is the time to start planning for
how MATE Desktop, and therefore Ubuntu MATE, implement support for Wayland.

## Voice command

Smart speakers are growing in popularity and commanding mobile devices by voice
is already common place. We will research how effectively voice commands can be
integrated into Ubuntu MATE.

## Accessibility

Making an accessible operating system was a key priority when the Ubuntu MATE
founders initially set out the goals of the project.

While Ubuntu MATE is never going to be able to offer the comprehensive
integration of assistive technologies that Sonar GNU/Linux provides, we will
continue to follow their lead so that Ubuntu MATE is a viable desktop solution
where computer access is shared within a household or business where individual
needs differ.

The upstream MATE Desktop team are actively engaged with visually impaired users
from the Linux community to ensure their needs are met. This effort will likely
never be complete, as it requires constant refinement.

## Translation

Translation of Ubuntu and MATE desktop is handled upstream thanks to the tireless
efforts of many translators, therefore the Ubuntu MATE operating system is
available in many languages. However, this website is currently available in
English only and we will work with the community to make it available in other
languages.

---

# Completed Objectives

While these initiatives are considered "complete" they will of course
be maintained and improved.

## Artwork

Overhaul the Ubuntu MATE design language and make is consistent for web
and desktop. Create a new wallpaper collection based on abstract
designs and high quality photos.

 :heavy_check_mark: *Implemented since Ubuntu MATE 18.04*

## User experience

I am reliably informed that everything is a *user experience* these
days. User interfaces are, apparently, passé.

The MATE desktop offers a traditional desktop metaphor but it is also
extremely customisable. When combined with some 3rd party applications
Ubuntu MATE can be augmented to provide an "*experience*" similar to
what other contemporary desktop environments offer while retaining its
classic desktop paradigm.

 :heavy_check_mark: *Implemented since Ubuntu MATE 16.04*

## HiDPI support

High pixel density laptops and displays are becoming increasingly common
and Ubuntu MATE needs to provide a first class HiDPI experience.

 :heavy_check_mark: *Implemented since Ubuntu MATE 18.04*

## Launchers and Docks

We will evaluate 3rd party launchers, such as Slingscold,
[Synapse](http://mhr3.blogspot.com/2010/11/introducing-synapse-acetylcholine.html),
[The Duck Launcher](https://github.com/the-duck/launcher) and 3rd party docks,
such as [Plank](https://launchpad.net/plank), to
see how they can be integrated with Ubuntu MATE to make user interaction
with the desktop more efficient.

Launchers and docks are not to everyone's tastes so we will conduct
community polls (just as we have done in the past) to determine if the
selected 3rd party tools should be integrated as defaults or optional
extras.

 :heavy_check_mark: *Implemented since Ubuntu MATE 17.10 via Brisk Menu, MATE Menu and Super key support throughout MATE Desktop*

## Compiz

There are some hardcore Compiz addicts in the MATE community. That said
Compiz will never be enabled by default in Ubuntu MATE, but we do want
to cater for those people who want it. Compiz does include some
features that are of real benefit, such as the Enhanced Zoom plug-in
which is useful for individuals with low vision.

The Ubuntu MATE team will create a simple way for Compiz to be
installed and enabled for those users who want it.

 :heavy_check_mark: *Implemented since Ubuntu MATE 15.04*

## Ubuntu MATE Tweak

There are a plethora of options behind MATE that are not yet exposed
via control centre applets. The Ubuntu MATE team have already provided
a simple tool to tweak your MATE configuration called MATE Tweak and
over time that tool be be enhanced and improved.

A number of different panel layouts are already available in Ubuntu MATE.
Panel layouts that offer a pure MATE desktop will continue to be made
available and others added that may also rely on 3rd party launchers,
docks or even Compiz. We will provide a tool to switch between these
different desktop layouts that also enables/disables the appropriate
launchers and docks where required.

  :heavy_check_mark: *Implemented since Ubuntu MATE 15.04 via **MATE Tweak***

## Complex input methods

We've received feedback that complex input method support in Ubuntu
MATE could be better.

MATE does have support for complex input methods right now, but having
spoken to some users in China and Japan, we now better understand their
requirements. To that end we've documented how to install and enable
IBus and fcitx on the [download page](/download/). That was just the
first step in ensuring everyone is catered for and in the future we
will integrate either [IBus](https://code.google.com/p/ibus/) or
[fcitx](https://fcitx-im.org/) into Ubuntu MATE to address this short
coming.

 :heavy_check_mark: *Implemented since Ubuntu MATE 15.10*
