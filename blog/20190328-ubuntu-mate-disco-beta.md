<!--
.. title: Ubuntu MATE 19.04 Beta 1
.. slug: ubuntu-mate-disco-beta
.. date: 2019-03-29 00:15:00 UTC
.. tags: Ubuntu,MATE,Disco,beta
.. link:
.. description: Ubuntu MATE 19.04 (Disco Dingo) Beta
.. type: text
.. author: Martin Wimpress
-->

**Ubuntu MATE 19.04 is a modest upgrade over previous releases. If you want bug
fixes and improved hardware support then 19.04 is for you.**

We are preparing Ubuntu MATE 19.04 (Disco Dingo) for distribution on
[April 18th, 2018](https://wiki.ubuntu.com/DiscoDingo/ReleaseSchedule)
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<div align="center">
<img src="/gallery/blog/1904-beta.png" alt="Ubuntu MATE 19.04 Beta" /><br />
Ubuntu MATE 19.04 with the Mutiny layout
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

## What changed since the Ubuntu MATE 18.10 final release?

Those of you who follow the desktop Linux news will know that
upstream [MATE Desktop recently released version 1.22](https://mate-desktop.org/blog/2019-03-18-mate-1-22-released/).

Let's rip that band-aid off and get this over quickly. Ubuntu MATE 19.04
is shipping with MATE Desktop 1.20. Albeit, the latest maintaince release of
MATE Desktop 1.20 with some of the bug fixes and new features from MATE
Desktop 1.22 included. In fact, the version of MATE Desktop being shipped in
19.04 is derived from the same MATE packages that will feature in the upcoming
[Debian 10 (Buster)](https://wiki.debian.org/DebianBuster) release.

You maybe wondering why we're not shipping MATE Desktop 1.22?
The answer, stability. MATE Desktop 1.22 introduces some underlying API
changes in core components and while all first party MATE Desktop
applications are compatible with the changes and completely stable, some
third party applications are not. Some third party applications are big
crashers now and we've not been able to fix them in time.

So, we are playing it safe and sticking with MATE Desktop 1.20 and working
with upstreams so we can land MATE Desktop 1.22 early in the Ubuntu MATE
19.10 development cycle.

### MATE Dock Applet

[MATE Dock Applet](https://github.com/robint99/mate-dock-applet) has been
updated to 0.88 which introduces some new visual options, both based on
the look of the Unity desktop. As can be seen in the screenshot above these
can be used to make the Mutiny layout more closely mimic Unity 7.

### Remote Desktop Awareness

Our MATE Desktop 1.20 packages ship with patches to support
[Remote Desktop Awareness (RDA)](https://github.com/ArcticaProject/librda). RDA
makes MATE Desktop more aware of its execution context so that it behaves
differently when run inside a remote desktop session compared to when running
on local hardware. Different remote technology solutions support different
features and they can now be queried from within MATE components. The inclusion
of RDA offers the option to suspend your remote connection, supports folder
sharing in Caja, MIME type bindings for SSHFS shares and allows session suspension
via the MATE screensaver.

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