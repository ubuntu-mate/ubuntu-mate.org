<!--
.. title: Ubuntu MATE 17.04 Alpha 2
.. slug: ubuntu-mate-zesty-alpha2
.. date: 2017-01-27 20:30:00 UTC
.. tags: Ubuntu,MATE,Zesty,alpha2
.. link:
.. description: Ubuntu MATE 17.04 (Zesty Zapus) Alpha 2
.. type: text
.. author: Martin Wimpress
-->

We are preparing Ubuntu MATE 17.04 (Zesty Zapus) for distribution on
[April 13th, 2017](https://wiki.ubuntu.com/ZestyZapus/ReleaseSchedule)
With this *Alpha* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<div align="center">
<img src="/gallery/blog/ubuntu-mate-1704-alpha2.png" alt="Ubuntu MATE 17.04 Alpha 2" /><br />
</div>

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

## What changed since the Ubuntu MATE 16.10 final release?

This is what have been updated or added.

  * Upgraded to **MATE Desktop 1.17.2**
    * The MATE Desktop 1.17 development snapshots are what will become the next stable release of MATE Desktop.
      * **Caja and Eye of MATE are both still 1.16 in Alpha 2**, newer versions should land via updates soon.
    * All the legacy GTK2+ code has been completely removed from the entire project.
    * Features **full support for [libinput](https://www.freedesktop.org/wiki/Software/libinput/)**, a modern library to handle input devices such as mice, trackpads and touch screens for Wayland and X11.
    * `mate-panel` now **supports [desktop actions](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#extra-actions)**.
    * Eye of MATE and Pluma have been ported to `libpeas`, which means **all the plugins are back**!
    * Many, many, bug fixes.
    * Translation updates.
  * Upgraded to **Ubuntu MATE Artwork 17.04.1**
    * **New folder icons contributed by [Daniel Foré](http://danielfore.com/)** from [elementary](https://elementary.io)
    * Ambiant-MATE and Radiant-MATE fixes.
    * **New pixel doubled assets contributed by [Michael Tunnel](http://michaeltunnell.com/)** from [TuxDigitial](http://tuxdigital.com/)
  * Upgraded to **Ubuntu MATE Welcome 17.04.1**
    * Updated the Software Boutique for 17.04
    * Update the DVD playbackback install to support DVD and Blu-ray.
    * `dconf-editor` is no longer pre-installed but has been added to the Software Boutique.
    * Updated translations.
  * **Dropped PowerPC**
    * [Debian announced it is dropping PowerPC as a release architecture in October 2016](https://lists.debian.org/debian-devel-announce/2016/10/msg00008.html).
    * [Ubuntu Technical Board announced that Ubuntu is removing 32-bit powerpc architecture from future Ubuntu releases](https://lists.ubuntu.com/archives/ubuntu-devel-announce/2016-December/001199.html).
    * Consequently Ubuntu MATE will not be releasing PowerPC images anymore.
    * Ubuntu MATE **16.04 will continue to support PowerPC until 2019**.
  * The `.iso` images are **approximately 200MB smaller**.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 17.04</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

Here are the known issues.

### Ubuntu MATE

* **MATE Tweak**: [Custom panel layout doesn't show in the panel list tab.](ttps://bugs.launchpad.net/ubuntu-mate/+bug/1706810)

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * [grub fails to install bootloader for LVM with Encryption](https://bugs.launchpad.net/ubuntu/+source/grub-installer/+bug/1659448)

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).