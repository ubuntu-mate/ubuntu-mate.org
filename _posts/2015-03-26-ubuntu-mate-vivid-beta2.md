---
layout: blog-post
title: Ubuntu MATE 15.04 Beta 2
permalink: ubuntu-mate-vivid-beta2
category: dev
author: Martin Wimpress
lang: en
---

Ubuntu MATE 15.04 Beta 2 is now available for official download. This
release builds on Ubuntu MATE Beta 1, makes a few changes and fixes
a lot of bugs.

As usual preparing this release of Ubuntu MATE has been a team effort.
Special thanks to [Mike Gabriel](https://alioth.debian.org/users/sunweaver/),
[Vlad Orlov](https://github.com/monsta) and [Stefano Karapetsas](https://github.com/stefano-k)
for putting in a great deal of effort triaging bugs, doing code reviews and
creating new upstream MATE Desktop 1.8.x point releases. Thanks guys!

Thanks also to [Mathieu Trudel-Lapierre](https://launchpad.net/~mathieu-tl),
[Colin Watson](https://launchpad.net/~cjwatson), [Adam Conrad](https://launchpad.net/~adconrad)
and [Daniel Holbach](https://launchpad.net/~dholbach) for their patience and 
guidance that has helped fix and improve Ubuntu MATE.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 15.04 Beta 1 release?

Here is what changed since Ubuntu MATE 15.04 Beta 1:

  * Fixed the Notification Area crashing on i386. [LP: #1425401](https://bugs.launchpad.net/ubuntu/+source/mate-panel/+bug/1425401)
  * Fixed [various glib compatibility issues](https://bugs.launchpad.net/ubuntu-mate/+bug/1426327).
  * Fixed assorted bugs. All bugs fixed in Debian have been synced with Ubuntu.
    * Debian [#774546](https://bugs.debian.org/774546), [#775212](https://bugs.debian.org/775212),
    [#775261](https://bugs.debian.org/775261), [#776689](https://bugs.debian.org/776689),
    [#776698](https://bugs.debian.org/776698), [#777311](https://bugs.debian.org/777311),
    [#778278](https://bugs.debian.org/778278), [#778816](https://bugs.debian.org/778816),
    [#778817](https://bugs.debian.org/778817), [#778824](https://bugs.debian.org/778824),
    [#778826](https://bugs.debian.org/778826), [#778835](https://bugs.debian.org/778835),
    [#776698](https://bugs.debian.org/776698), [#779719](https://bugs.debian.org/779719),
    [#779821](https://bugs.debian.org/779821), [#779848](https://bugs.debian.org/779848),
    [#779856](https://bugs.debian.org/779856), [#779916](https://bugs.debian.org/779916),
    [#780104](https://bugs.debian.org/780104), [#780210](https://bugs.debian.org/780210),
    [#780226](https://bugs.debian.org/780226), [#780399](https://bugs.debian.org/780399),
    [#780731](https://bugs.debian.org/780731)
    * Ubuntu [#1364111](https://launchpad.net/bugs/1364111), [#1377967](https://launchpad.net/bugs/1377967),
    [#1422402](https://launchpad.net/bugs/1422402), [#1425499](https://launchpad.net/bugs/1425499),
    [#1425611](https://launchpad.net/bugs/1425611), [#1427704](https://launchpad.net/bugs/1427704), [#1428131](https://launchpad.net/bugs/1428131),
    [#1428275](https://launchpad.net/bugs/1428275), [#1430045](https://launchpad.net/bugs/1430045),
    [#1430204](https://launchpad.net/bugs/1430204), [#1430210](https://launchpad.net/bugs/1430210),
    [#1431349](https://launchpad.net/bugs/1431349), [#1432439](https://launchpad.net/bugs/1432439),
    [#1432235](https://launchpad.net/bugs/1432235), [#1419321](https://launchpad.net/bugs/1419321),
    [#1426664](https://launchpad.net/bugs/1426664), [#1428273](https://launchpad.net/bugs/1428273),
    [#1426436](https://launchpad.net/bugs/1426436)
  * Added some community contributed wallpapers from [Ghost Sixtyseven](https://ubuntu-mate.community/t/three-wallpapers-for-consideration/449).
  * Added MATE Menu and also uploaded it to the official Ubuntu archive.
  * Added MATE Tweak and also uploaded it to the official Ubuntu archive.
    * Compiz is now only presented as an option if the video device driver has the required capabilities.
  * Enabled Qt accessibility modules when a MATE session is detected.
  * Enabled `systemd` as the default init system. [LP: #1427654](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/1427654).
  * Updated [Folder Color](http://foldercolor.tuxfamily.org/) to 0.0.60 and Folder Color Caja to 0.0.62.
    * Now allows folder colours to be set globally.
  * Updated Yuyo, Ambiant-MATE, Radiant-MATE themes to override symbolic icons with full colour icons.
  * Updated MATE specific autostart files and configuration so they do not conflict with other desktop environments. [LP: #1426862](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/1426862).
  * Updated available languages.
    * `en` `es` `pt` are available on all architectures
    * `bn` `fr` `hi` `ja` `zh-hans` are available on all except PowerPC.
  * Updated `mate-themes` with improved support for GTK3 Client Side Decorations and pop-overs.
  * Updated MATE profile for Compiz to enhance the effects slightly.
  * Replaced Cheese with guvcview.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 15.04 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/vivid/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

It is not all good news however. Here are the known issues. All of which
affect every Ubuntu flavour.

  * Once installation has finished, and the final Restart button is pressed, the screen freezes and becomes unresponsive. Pressing Enter which would normally do the reboot does nothing.
    * The computer will require a manual power off or reset after the disc has been ejected.
    * [LP: 1436816](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1436816)
  * Virtualbox guests will only get a resolution of 640x480
    * [LP: #1368784](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/), see [comment #13](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/comments/13) for a work around.
  * It is not possible to install the Virtualbox drivers via the Additional Hardware application.
    * [LP: #1434579](https://bugs.launchpad.net/ubuntu/+source/software-properties/+bug/1434579)
    * The workaround is to open a shell and `sudo apt-get install virtualbox-guest-x11`.
  * You may not be able to enter your pass phrase if you use full disk encryption.
    * [LP: #1386005](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1386005)
  * OEM Config is broken.
    * [LP :#1436937](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1436937)
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Useful Information

You may find the following information useful, which is why we titled 
the section *Useful Information* since the information presented here
is mostly useful.

  * [Ubuntu MATE 15.04 Useful Information](https://ubuntu-mate.community/t/ubuntu-mate-14-10-and-15-04-useful-information/24)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
