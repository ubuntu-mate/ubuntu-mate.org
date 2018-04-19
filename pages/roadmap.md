<!--
.. title: Roadmap
.. slug: roadmap
.. date: 2014-09-19 23:01:09 UTC
.. tags: Ubuntu,MATE,Roadmap
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

This page outlines roadmap items we've completed and some of the
activities the Ubuntu MATE team will research, and possibly implement,
in future development cycles to improve and refine our operating
system.

# In progress roadmap objectives

## Grow community participation and engagement

Ubuntu MATE and MATE Desktop are created by very small teams. We'll
improve our documentation so that new contributors can find tasks they
can work on and material to help them get started.

## Reboot Ubuntu MATE Welcome and Software Boutique

We will decouple Ubuntu MATE Welcome and the Software Boutique so they
can be interated on independently. The code for both will be refactor
and simplified so that other projects wanting to build on either can
easily do so.

Both applications will be delivered as snaps to break the development
cycle relationship with the distribution, giving us the freedom to
develop both without the usual constraints of distribution release
management. This will also benefit Ubuntu MATE who will automatically
get new features, application listings and other improvements.

## Developer tooling and collaboration

Ubuntu MATE and MATE Desktop will expand their use of continuous
integration and automated testing in an effort to save the small
development teams burning valuable time on activities best left to a
bot.

Review the development platforms and communication/collaboration tools
used by the MATE Desktop team to improve team communication and simplfy
the project infrastructure where possible.

Review the static site building tools using by Ubuntu MATE and MATE
Desktop so that the websites can be more easily maintained.

## Modern display server support

Wayland is set to become the defacto next generation display server.
While Xorg has some years or usefulness ahead of it, now is the time to
start planning for how MATE Desktop, and thefore Ubuntu MATE, implement
support for Wayland.

## Voice command

Smart speakers are growing in popularity and commanding mobile devices
by voice is already common place. We will research how effectively
voice commands can be integrated into Ubuntu MATE.

## Accessibility

<img class="right" src="/assets/img/logos/a11y-small.png" alt="Accessibility" width="150" height="150" />

Making an accessible operating system was a key priority when the
Ubuntu MATE founders initially set out the goals of the project.

Ubuntu MATE is never going to be able to offer the comprehensive
integration of assistive technologies that [Sonar GNU/Linux](http://sonargnulinux.com/)
provides. But we will continue to follow their lead so that Ubuntu MATE
is a viable desktop solution where computer access is shared within a
household or business where individual needs differ.

The upstream MATE Desktop team are actively engaged with visually
impaired users from the Linux community to ret and ensure their needs
are met. This effort will like never be complete, it requires constant
refinement.

## Translation

<img class="right" src="/assets/img/logos/i18n-small.png" alt="Internationalisation" width="150" height="150" />

Translation of Ubuntu and MATE desktop is handled upstream thanks to
the tireless efforts of many translators, therefore the Ubuntu MATE
operating system is available in many languages. However, this website
is currently available in English only and we will work with the
community to make it available other languages too.

# Completed Roadmap Objectives

While these initiatives are considered "complete" they will of course
be maintained and improved.

## Artwork

Overhaul the Ubuntu MATE design language and make is consistent for web
and desktop. Create a new wallpaper collection based on abstract
designs and high quality photos.

 * *Implemented since Ubuntu MATE 18.04*

## User experience

I am reliably informed that everything is a *user experience* these
days. User interfaces are, apparently, passé.

The MATE desktop offers a traditional desktop metaphor but it is also
extremely customisable. When combined with some 3rd party applications
Ubuntu MATE can be augmented to provide an "*experience*" similar to
what other contemporary desktop environments offer while retaining its
classic desktop paradigm.

 * *Implemented since Ubuntu MATE 16.04*

## HiDPI support

High pixel density laptops and displays are becoming increasingly common
and Ubuntu MATE needs to provide a first class HiDPI experience.

 * *Implemented since Ubuntu MATE 18.04*

## Launchers and Docks

We will evaluate 3rd party launchers, such as Slingscold,
[Synapse](http://synapse.zeitgeist-project.com/wiki/index.php?title=Main_Page),
[The Duck Launcher](https://the-duck.github.io/) and 3rd party docks,
such as [Plank](http://wiki.go-docky.com/?title=Plank:Introduction), to
see how they can be integrated with Ubuntu MATE to make user interaction
with the desktop more efficient.

Launchers and docks are not to everyone's tastes so we will conduct
community polls (just as we have done in the past) to determine if the
selected 3rd party tools should be integrated as defaults or optional
extras.

 * *Implemented since Ubuntu MATE 17.10 via Brisk Menu, MATE Menu and Super key support throughout MATE Desktop*

## Compiz

There are some hardcore Compiz addicts in the MATE community. That said
Compiz will never be enabled by default in Ubuntu MATE, but we do want
to cater for those people who want it. Compiz does include some
features that are of real benefit, such as the Enhanced Zoom plug-in
which is useful for individuals with low vision.

The Ubuntu MATE team will create a simple way for Compiz to be
installed and enabled for those users who want it.

 * *Implemented since Ubuntu MATE 15.04*

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

  * *Implemented since Ubuntu MATE 15.04 via **MATE Tweak***

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

 * *Implemented since Ubuntu MATE 15.10*

## Application install

Users new to Linux are often overwhelmed by the vast choice of software
on offer. The Ubuntu MATE team will create a curated selection of
applications suitable for use with Ubuntu MATE that can be installed
via one click.

The Ubuntu MATE community will select one application that is more
suitable for a given task or activity so that new users can quickly
turn their Ubuntu MATE workstation into a productive tool.

  * *Implemented since Ubuntu MATE 15.10 via **Ubuntu MATE Welcome***

## Media casting and streaming

<img class="right" src="/assets/img/misc/phone-small.png" alt="Phone" width="124" height="240" />

Seamless integration with home media server content and media casting
devices is essential in order for Ubuntu MATE to remain relevant
for many home users. We will try to deliver on that.

Similarly being able to access popular subscription-based streaming
services such as Netflix, Amazon Instant Video and Spotify is also an
expectation for many users. While the Ubuntu MATE team can do little
to deliver the technologies to make this happen, we can provide simple
installation options to enable access to these services, and where
possible, ship the required software by default.

  * *Implemented since Ubuntu MATE 15.10 by using Software Boutique to install Google Chrome, Spotify or Pithos*

## Mobile device integration

Currently Ubuntu MATE has the essential mobile device support you'd
expect. You can plug in a phone or a media player and the device is
automatically detected and mounted, you can then access the files on it.

  * *Implemented since Ubuntu MATE 15.10*

Mobile device notifications can be wirelessly mirrored to your Ubuntu
MATE desktop and for you to be able to send files or links wirelessly
between your mobile devices and Ubuntu MATE.

  * *Implemented since Ubuntu MATE 16.04 by using the Software Boutique to install KDE Connect Indicator"