<!--
.. title: Ubuntu MATE 15.04 Beta 2
.. slug: ubuntu-mate-vivid-beta2
.. date: 2015-03-26 17:30:37 UTC
.. tags: Ubuntu,MATE,Vivid,beta,draft
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->


Ubuntu MATE 15.04 Beta 2 is now available for official download. This
release builds on Ubuntu MATE Beta 1 by making a few changes and
addressing some bugs.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 15.04 Beta 1 release?

Here is what changed since Ubuntu MATE 15.04 Beta 1:

  * Fixed the "Notification Area" crashing on i386. [LP: #1425401](https://bugs.launchpad.net/ubuntu/+source/mate-panel/+bug/1425401)
  * Fixed [various glib compatibility issues](https://bugs.launchpad.net/ubuntu-mate/+bug/1426327). Many thanks to Vlad Orlov, Mike Gabriel and Stefano Karapetsas.
  * Fixed assorted bugs. All fixed Debian bugs below have been synced with Ubuntu.
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
    [#780226](https://bugs.debian.org/780226), [#780399](https://bugs.debian.org/780399)
    * Ubuntu [#1364111](https://launchpad.net/bugs/1364111), [#1422402](https://launchpad.net/bugs/1422402),
    [#1425499](https://launchpad.net/bugs/1425499), [#1425611](https://launchpad.net/bugs/1425611),
    [#1427704](https://launchpad.net/bugs/1427704), [#1428131](https://launchpad.net/bugs/1428131),
    [#1428275](https://launchpad.net/bugs/1428275), [#1430045](https://launchpad.net/bugs/1430045),
    [#1430204](https://launchpad.net/bugs/1430204), [#1430210](https://launchpad.net/bugs/1430210),
    [#1431349](https://launchpad.net/bugs/1431349), [#1432439](https://launchpad.net/bugs/1432439)
    [#1432235](https://launchpad.net/bugs/1432235)
  * Added some community contributed wallpapers from [Ghost Sixtyseven](https://ubuntu-mate.community/t/three-wallpapers-for-consideration/449).
  * Added MATE Menu to Ubuntu MATE and also uploaded it to the official Ubuntu archive.
  * Added MATE Tweak to Ubuntu MATE and also uploaded it to the official Ubuntu archive.
    * Compiz only presented as an option if the video device driver has the required features.
  * Enabled Qt accessibility modules when a MATE session is detected.
  * Enabled `systemd` as the default init system. [LP: #1427654](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/1427654).
  * Updated Yuyo, Ambiant-MATE, Radiant-MATE themes to override symbolic icons with full colour icons.
  * Updated MATE specific autostart files and configuration so they do not conflict with other desktop environments. (LP: #1426862)
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

It is not all good news however. Here are the known issues.

  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)
  * Virtualbox guests may only get a resolution of 640x480
    * [LP: #1368784](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/), see [comment #13](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/comments/13) for a work around.
  * Running an Ubuntu MATE live session as a Virtualbox guest may corrupt the video
  output of the guest.
    * You can correct the video display by pressing `Host+F1` to switch
    VT in the guest and then press `Host+F7` to switch back which will
    correct the video output.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

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
