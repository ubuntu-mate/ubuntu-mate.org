---
layout: blog-post
class: blog
title: Ubuntu MATE 16.10 progress update
permalink: /blog/ubuntu-mate-yakkety-progress-update/
description: Ubuntu MATE 16.10 progress update on the migration to GTK3+ and Snappy package research and development
category: news
author: Martin Wimpress
lang: en
---

The [Ubuntu MATE Patrons](https://www.patreon.com/ubuntu_mate) have already
received some updates explaining most of this, but here's an update for
everyone.

With a solid 16.04 release behind us it is time to focus on our
*"retrospective future"* and not just languish as a retrospective only
project. Ubuntu MATE 16.10 is the experimental playground to adopt, and
experiment with, new technologies so that our traditional desktop environment
can continue to flourish and remain relevant.

**TL;DR Ubuntu MATE 16.10 is switching to GTK3+, Ubuntu MATE Welcome and
Software Boutique are improving all the time, MATE Tweak has been tweaked and
Ubuntu MATE is involved in the early prototyping of using Snap packages to
package the MATE Desktop.**

Read on to find out what that all means.

## Snap!

Snap is a new package format that was introduced to desktop Ubuntu, and
flavours, in 16.04. Naturally Ubuntu MATE 16.04 has built-in `snapd` support.
The general idea of a Snappy system is that all snaps are self contained,
protected and isolated pieces of code that perform a well defined set of
functions.

The Ubuntu MATE team are being supported by Ubuntu developers to create Snaps
of various MATE desktop components in order to discover what works and what
doesn't. This is an iterative process to improve the snap platform and package
more MATE components until running a full desktop environment on a Snappy
system is possible.

We're delighted to be involved with Snappy and are looking forward to the road
ahead and the role Snaps will play in Ubuntu MATE's *"retrospective future"*.

### What! You're dropping .deb? *R-A-G-E!&nbsp; Q-U-I-T!* Alt+F4

{% include blog/jumbotron.html
    title = "We are not dropping the classic Debian package based distribution model."
    text = "We want to make this point as clear as we can. The classic Debian based package distribution model is not being dropped."
    button_text = "Snappy"
    button_url = "https://developer.ubuntu.com/en/snappy/"
%}

**OK, got that? .deb packages are not being dropped. Good `:-)`**

### Snap progress

Right now we've got one snap package for Galculator, which is part of the MATE
Desktop suite of applications, and our first attempt looked liked this:

{:.center}
![Snappy Galculator](/images/blog/Progress-201605/Snappy_Galculator.png)

Oh dear! As you can see it's *very* early days `;-)` Fortunately, after some advice from
Ubuntu developers, it now looks like this:

{:.center}
![Snappy Galculator Day 2](/images/blog/Progress-201605/Snappy_Galculator_2nd_Day.png)

Better! On the second day of experimenting with Snappy things improved. There
is still an issue with rendering some images, the .png images that surround
the buttons in this case, but fonts and themes are working.

Work has now started on Snapping more complex MATE applications such as Pluma (the
text editor) and Caja (the filemanager).

### Why are Snaps important to me?

Insightful question `;-)`

The number one question in the Ubuntu MATE community right now is:

> When can I get MATE 1.14 for Ubuntu MATE 16.04?

Snaps will make that problem a snap to solve.

## GTK3+

Ubuntu MATE 16.10 will be a GTK3+ build only. This is both good and bad, here's why.

{:.center}
![MATE 1.14 GTK3](/images/blog/Progress-201605/MATE114_GTK318.png)

The screenshot above shows an early development build of Ubuntu MATE 16.10
running MATE 1.14 built against GTK 3.18. Many improvements have been made
since that screenshot was taken.

### The Good

  * The **MATE 1.14 package transition to GTK3+ was committed to Debian git** a month ago
  * A PPA has been created for Ubuntu MATE 16.10 to test MATE 1.14 built against GTK3+
  * **Ubuntu MATE themes have been adapted** to work with GTK3+
  * Debian developers are **currently reviewing and sponsoring the uploads MATE 1.14** into Debian unstable
  * We will be doing the work to support GTK 3.20 and upstream MATE are already working on GTK 3.21/3.22 support
  * **MATE 1.14 built against GTK3+ works**
  * **Ubuntu MATE 16.10 Alpha 1 will feature MATE 1.14 built against GTK3+**
  * During May 2016 **Ubuntu MATE has transfered €1997 to 7 independant Open Source developers to accelerate the completion of the GTK3+ migration**
    * Full details will be published in the Ubuntu MATE May 2016 financial summary that is due in the second week of June 2016.

MATE 1.14 also introduces the **facility to change the size of Panel menu
icons (the menus for Applications, Places, System) and Panel icons (anything
in a panel)**, the supported resolutions are 16px to 48px. This will soon be
exposed via MATE Tweak and has a few benefits:

  * Bigger icons **for high resolution displays**
  * **Big icons for the visually impaired**
  * And if you are so inclined, **large panels suitable for touch input but without changing the desktop metaphor**

### The Bad

  * MATE Menu (the Advanced Menu option in MATE Tweak) is not compatible with GTK3+. However the porting project has started and is well advanced.
  * MATE Indicator Applet is a bit broken under GTK3+ but investigations are underway.
  * MATE Dock Applet is not compatible with GTK3+, the porting project has not yet started.
  * Topmenu Applet is not compatible with GTK3+, the porting project has not yet started.

### The Ugly

  * GNOME Main Menu (the menu in the openSUSE panel layout) is GTK2+ only and
  unmaintained. None of the MATE developers are interested in migrating it to
  GTK3+. **GNOME Main Menu will be dropped from the Debian and Ubuntu archives.**

### Why is GTK3+ important to me?

Good question, glad you asked `;-)`

Some of the old libraries that MATE GTK2+ depends on are unmaintained,
deprecated and being removed from many distributions. **In order for MATE to
remain relevant, the move the GTK3+ is essential.**

HiDPI, is going to be a thing. Really, it is. **With MATE 1.14 built against
GTK3+ we have initial HiDPI support working.** Don't get too excited, this is
an all or nothing implementation. It can be enabled via an environment
variable and a session restart, but once done, all GTK3 applications (not just
MATE) will be rendered using high quality pixel doubling. If you have a 4K
display, it looks ace `:-D`

## MATE Tweak

In other developments **Tilda is no longer auto-started by default**, it is
now an option in MATE Tweak. MATE Tweak has a slight UI re-organise and now
supports Xcompmgr as one of the compositor options. **Xcompmgr support has
been added because it is the preferred compositor to use on the Raspberry
Pi**. MATE Tweak has also separated the Interface section into Interface and
Panels.

## Welcome and Software Boutique

Ubuntu MATE Welcome has been ported to WebKit2 4.0, **the animations and
transitions are now much more fluid**. Welcome has also been given a slight
design refresh.

### Boutique News

The Software Boutique now features News, to **inform you of package additions,
modifications and removals**.

{:.center}
![Boutique News](/images/blog/Progress-201605/Boutique_News.png)

### Boutique Search

**A search facility has also been added** and the Ubuntu MATE community has
contributed some new applications, including [Atom](https://atom.io/),
[Clementine](https://www.clementine-player.org/) and [Lutris](https://lutris.net/).

{:.center}
![Boutique Search](/images/blog/Progress-201605/Boutique_Search.png)

## What of Ubuntu MATE 16.04?

The Boutique News, Boutique Search and new Boutique software listings have
**already been back ported to Ubuntu MATE Welcome in 16.04. Subscribe Welcome to
updates and you can have them today!**

Some of the theme updates to support MATE built against GTK3+ have highlighted
some bugs and **those fixes will be back ported to 16.04 as well**. This is in
addition to a number of other Ubuntu MATE bug fixes that have already landed
in 16.04.

## What else?

Well, that's all for now. But we have some other goals planned for 16.10 and
if we're able to deliver on them we'll let you know here.
