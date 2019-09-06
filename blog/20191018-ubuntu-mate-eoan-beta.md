<!--
.. title: Ubuntu MATE 19.10 Beta 1
.. slug: ubuntu-mate-eoan-beta
.. date: 2019-10-18 00:15:00 UTC
.. tags: Ubuntu,MATE,Eoan,beta,draft
.. link:
.. description: Ubuntu MATE 19.10 (Eoan Ermin) Beta
.. type: text
.. author: Martin Wimpress
-->

**Ubuntu MATE 19.10 is a signifcant upgrade over previous releases sporting bug
fixes and new features**

We are preparing Ubuntu MATE 19.10 (Eoan Ermin) for distribution on
[October 18th, 2018](https://wiki.ubuntu.com/EoanErmin/ReleaseSchedule)
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<div align="center">
<img src="/gallery/blog/1910-beta.png" alt="Ubuntu MATE 19.10 Beta" /><br />
Ubuntu MATE 19.10 with the Familiar layout
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

## What changed since the Ubuntu MATE 19.04 final release?

  * Added MATE Desktop 1.22.1
  * Fixed frequent crashers in Brisk Menu, MATE Dock Applet and MATE Panel.
  * Brisk scrollbar fixed. Brisk upstream.
  * Upstream of MATE Dock Applet.
  * Fixed oversized indicator icons.
    gallery/blog/indicators-after.png
    gallery/blog/indicators-before.png
  * Fixed indicator scaling when changing the panel size.
  * Fixed race condition that could result in two network status icons being displayed
  * Fixed XPresent support
  * Added `indicator-datetime` support
  * Switched from Thunderbird to Evolution as the default mail/calendar app
  * Dropped Brasero from the default installed applications.
  * MATE Tweak preserves user preferences when switching between custom layouts.
  * Start Applications hides system applications.
  * GNOME MPV
  * indicator-notifications and do not disturb.
  * Blueman 2.0.8
  * Reduced the .iso image size, then made it big again because nvidia-drivers.
  * Languages on iso optimised for where UBuntu MATE is more used.
  * Marco - invisble window corners. Alt + Tab. HiDPI gradients. No menu in window controls by default.
  * MATE Window Applets
  * Theme fixes
  * Caja Deja Dup 0.0.8
  * Caja Media Info extension.
  * Dropped Compton and Compiz from the default install
  * Ubuntu MATE Welcome layout switcher.
  * MATE Screensaver lock on resume.
  * Fix symbolic icons appearing where they should not. Control Center. Sound Preferences. Bluetooth.
  * Improved batter indicators so they showing a charging symbol while charging.
  * Fixed lock icons in the Network Indicator when establishing VPN connection

sudo apt install compiz compiz-core compiz-mate compiz-plugins compiz-plugins-default

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 19.04 Beta</h1>
        <p>We've even redesigned the download page so it's even easier to get started.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * The Software Boutique doesn't list any available software.
    * An update, due very soon, will re-stock the software library and add a few new applications too.

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * [Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
