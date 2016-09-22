<!--
.. title: Ubuntu MATE 16.10 Beta 2
.. slug: ubuntu-mate-yakkety-beta2
.. date: 2016-09-23 00:00:00 UTC
.. tags: Ubuntu,MATE,Yakkety,beta2,draft
.. link:
.. description: Ubuntu MATE 16.10 (Yakkety Yak) Beta 2
.. type: text
.. author: Martin Wimpress
-->

We are preparing Ubuntu MATE 16.10 (Yakkety Yak) for distribution on
[October 13th, 2016](https://wiki.ubuntu.org/YakketyYak/ReleaseSchedule) With this
*Final Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<div align="center">
<img src="/gallery/blog/ubuntu-mate-1610-beta2.png" alt="Ubuntu MATE 16.10 Beta 2" /><br />
<b>As is now customary, our release artwork was made by <a href="https://www.youtube.com/channel/UCglkWuyZDppWD2BVsyI4r3A" target="_blank"><i>Ghost Sixtyseven</i></a>.</b>
</div>

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

## What changed since the Ubuntu MATE 16.10 Beta 1 release?

This is what has been added, updated or removed.

  * **Upgraded to MATE Desktop 1.15.1**
    * The entire MATE Desktop suite has been upgraded to MATE Desktop
    1.15.x
    * These are the final development snapshots and bring many bug fixes
    and GTK3+ compatibility improvements.
    * **MATE Desktop 1.16 will be available via updates soon!**
  * Updated Ubuntu MATE themes which **significantly improves GTK 3.20 compatibility**.
  * Upgraded to **Linux 4.8**.
  * **Ubuntu MATE 16.10.8 will be available via updates** shortly after release.
  * Fixed MATE Tweak segfault when switching to Compiz due to a `gsettings` schema change in Metacity.
  * Fixed Weather reports and forecasts.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 16.10</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

Here are the known issues.

### Ubuntu MATE issues

  * Nothing significant.

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * LibreOffice 5.2.1 has bugs in it's GTK3+ implementation that results white borders being shown around the toolbars in dark themes.

  * Choosing an Entire Disk install on PowerPC may result in an unbootable system.
    * The work around is to manually partition your hard disk and create an `ext2` boot partition.
    * [#1606089](https://bugs.launchpad.net/bugs/1606089),
    [#1607128](https://bugs.launchpad.net/bugs/1607128)

  * PowerPC iso fails to boot with linux-image-4.8.0-11-generic on PowerMac G5 7,3
    * It does work on PowerBook G4 5,6 and 5,8.
    * [#1626332](https://bugs.launchpad.net/bugs/1626332)

  * Ubiquity installer Slideshows and Ubuntu MATE Welcome display a blank window on PowerPC.
    * This is due to a bug in WebKit 2.
    * [#1561573](https://bugs.launchpad.net/bugs/1561573),
    [#1597764](https://bugs.launchpad.net/bugs/1597764)

  * R300 GPU accelerated graphics do not work on PowerPC
    * [#1432949](https://bugs.launchpad.net/bugs/1432949),
    [#1575391](https://bugs.launchpad.net/bugs/1575391)

  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).