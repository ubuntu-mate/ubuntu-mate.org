<!--
.. title: Ubuntu MATE 16.04 Alpha 2
.. slug: ubuntu-mate-xenial-alpha2
.. date: 2016-01-28 12:00:00 UTC
.. tags: Ubuntu,MATE,Xenial,alpha2,draft
.. link:
.. description: Ubuntu MATE 16.04 (Xenial Xerus) LTS Alpha 2
.. type: text
.. author: Martin Wimpress
-->

We are preparing Ubuntu MATE Xenial Xerus (16.04) for distribution on
[April 21st, 2016](https://wiki.ubuntu.org/XenialXerus/ReleaseSchedule)
With this *Alpha 2* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Alpha Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who needs a stable system
  * Anyone uncomfortable running a possibly frequently broken system
  * Anyone in a production environment with data or workflows that need to be reliable

Ubuntu MATE *Alpha Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE, and GTK+ developers

## What changed since the Ubuntu MATE 15.10 release?

Here what changed in Ubuntu MATE 16.04 Alpha 2 since Ubuntu MATE 16.04 Alpha 1.

  * Updated to MATE Desktop 1.12.1.
    * Fixes and improvements for GTK3 support across the entire MATE Desktop including GTK 3.18 support.
    * Touchpad support is significantly improved and now features multi touch and natural scrolling.
    * Multi monitor support has been improved so the display settings use output names and the revised UI lets you set the primary monitor.
    * The power applet now displays model and vendor information so you can distinguish between multiple battery powered devices.
    * Improved session management which now includes screensaver inhibition while playing media.
      * MATE now listens to the `org.gnome.SessionManager` namespace.
    * Extended systemd support.
    * Long standing bugs and many little usability paper-cuts were fixed.
      * For example, panel applets are no longer reordered when changing screen resolutions.
    * See the [MATE Desktop 1.12 release announcement](http://mate-desktop.org/blog/2015-11-05-mate-1-12-released/) for more details.
  * Updated to Ubuntu MATE Welcome 16.04.1
    * New Ambience theme for the navigation bar.
    * Improved code re-use for footers (uses JavaScript)
    * Welcome will detect the graphics card (including VirtualBox)
    including information about the NVIDIA drivers PPA.
    * Expandable/collapsible sub-sections.
    * Hints appear after opening utilities.
    * Fade in software categories and corrected minor visual quirks.
    * Updated Firefox, LibreOffice and Control Centre icons.
    * Removed links on software icons. Users were getting confused why
    this opened a web page.
    * Added miscellaneous tasks to update cache, fix an incomplete install
    and fix broken dependencies.
    * Added Bazaar and Git.
    * Installing Adobe Flash now uses `flashplugin-installer`.
    * Updated PPAs for Veracrypt and X2Go.
  * Updated Ubuntu MATE Settings to 16.04.1
    * Added Mutiny panel layout. (Requires `mate-dock-applet`)
    * Removed Kandiword menu entry.
  * Updated Ubuntu MATE Artwork to 16.04.1
    * Added MATE colourised icons for categories, devices and places.
    * Added community [contributed wallpaper from Luke Horwell](https://ubuntu-mate.community/t/wallpaper-the-materix/3107)
    * Added community [contributed wallpaper from Rick Lell](https://ubuntu-mate.community/t/wallpaper-ubuntu-mate-greyscaled-wood/3199)


Thanks to everyone from the Ubuntu MATE community who contributed to
this release!

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 16.04 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/xenial/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

Here are the known issues.

  * The cryptsetup password prompt is not shown.
    * [LP: #1359689](https://bugs.launchpad.net/bugs/1359689)
    * [LP: #1530548](https://bugs.launchpad.net/bugs/1530548)
  * Shutdown/Restart of the live session does not work in Virtualbox, VMWave and KVM guests.
    * [LP: #1447038](https://bugs.launchpad.net/bugs/1447038)
  * The input box for editing a Wired connection static IP address doesn't appear correctly.
    * [LP: #1530323](https://bugs.launchpad.net/bugs/1530323)
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
