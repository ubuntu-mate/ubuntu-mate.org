<!--
.. title: Ubuntu MATE 17.04 Beta 2
.. slug: ubuntu-mate-zesty-beta2
.. date: 2017-03-23 21:30:00 UTC
.. tags: Ubuntu,MATE,Zesty,beta2
.. link:
.. description: Ubuntu MATE 17.04 (Zesty Zapus) Beta 2
.. type: text
.. author: Martin Wimpress
-->

**We're absolutely chuffed to bits to announce, what is quite possibly,
the best Ubuntu MATE beta we've ever released. We didn't participate
in the Beta 1 so we have quite the change log from Alpha 2 that was
released in January. We still have some fixes to land for the themes
but overall this release is shaping up to be really great.**

We are preparing Ubuntu MATE 17.04 (Zesty Zapus) for distribution on
[April 13th, 2017](https://wiki.ubuntu.com/ZestyZapus/ReleaseSchedule)
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<div align="center">
<img src="/gallery/blog/ubuntu-mate-1704-beta2.png" alt="Ubuntu MATE 17.04 Beta 2" /><br />
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

## What changed since the Ubuntu MATE 17.04 Alpha 2 release?

Here is a run down of what has been changed, updated or added.

  * Upgraded to **MATE Desktop 1.18.0**, you can read the [MATE 1.18 release announcement](http://mate-desktop.org/blog/2017-03-13-mate-1-18-released/) for the full details.
    * The entire MATE Desktop suite of applications and components is now GTK3+ only!
    * **Added full support for [libinput](https://www.freedesktop.org/wiki/Software/libinput/)**, a modern library to handle input devices such as mice, trackpads and touch screens for Wayland and X11.
    * Separate settings for handedness (left/right-handed) and motion acceleration/threshold.    
    * **Much improved accessibility support (particularly for visually impaired users)**, many thanks to our friends at [Hypra.fr](http://hypra.fr/-Home-17-.html?lang=en) for their contribution!
    * Lots of deprecated GTK+ methods have been replaced and many bugs have been fixed.
    * **Lock screen will load the users selected background** instead of the system defined default.    
    * Translations are updated. *Thank you to our team of translators!*
    * **Notifications now implement action icons support**, for example playback control icons used by media players.        
    * Reworked the font viewer to add font browsing mode, support for TTC fonts and the Font Viewer is now exposed in the menus.    
    * A number of **memory leaks have been plugged**.
  * **Caja adds several new features** including:
    * Added a copy queue and copy pausing.
    * Support for back/forward mouse buttons for directory navigation.
    * Notification when ejected drives are safe to unplug.
  * MATE Panel gets several improvements, including:
    * **Added [desktop actions](https://standards.freedesktop.org/desktop-entry-spec/latest/ar01s10.html) support for additional launch options**.
    * Added StatusNotifier support.
    * **Added support for [Menulibre](https://smdavis.us/projects/menulibre/) menu editor**, if installed it is preferred over Mozo.
  * Engrampa, the archive manager, includes a number of improvements:
    * Added `ear` and `war` to the supported types list.
    * Check the rar/unrar version to the correct date is shown.
    * Fixed compressing `rar` and `7z` when split into volumes.
  * MATE Terminal includes a couple of new features:
    * **Attempting to close a terminal that has an active process will request confirmation before proceeding**.
    * Terminal tabs can be closed with a middle mouse button click.
  * **Atril, the document viewer, has much improved page load times** and adds support for `unarchiver` used by some comics.    
  * The Eye of MATE and Pluma plugin systems have been refactored:
    * **All the Eye of MATE and Pluma plugins are back** as a result of all C and Python plugins having been ported to `libpeas`.
  * Upgraded to **Brisk Menu 0.3.0**
    * Brisk is a new efficient menu for the MATE Desktop developed by the [Solus Project](https://solus-project.com/).
    * **Integrated in the new Pantheon layout** available via MATE Tweak.
    * The Brisk Menu default hotkey is currently `Ctrl+F10`
  * Upgraded to **Ubuntu MATE Artwork 17.04.7**
    * Scrollbars have been simplified, offer improved compatibility and compliment the updated icon theme we added earlier in the year.
    * **Notebooks (tabs to you and me) have had a complete redesign**.
    * Headerbars (as used by some GNOME3 applications) are now fully supported in all Ubuntu MATE themes.
    * **Added a new fully dark theme, called Ubuntu MATE Dark** - *Many thanks to the YouTuber [Linux &amp; Other Stuff](https://www.youtube.com/channel/UCQpkMe-SLNg0HwWCP3eeTxw) for the contribution!*
    * When navigating via keyboard, using tab and cursors, active items now provide a visual hint.
    * **Brisk Menu is fully styled to match the look and feel of the Ubuntu MATE themes**.
    * Many fixes and improvements, big and small, throughout.
  * Upgraded to **Ubuntu MATE Settings 17.04.5**
    * Added theme integration for kdenlive.
    * **Added a new panel layout called Pantheon.**
    * Integrated Qt4 and Qt5 theming with GTK+
  * Upgraded to **Ubuntu MATE Welcome 17.04.8**
    * Updated several applications and added, the much requested, kdenline.
    * **Enabled the Bulk Queue by default**, the Software Boutique can now add multiple applications to the install/remove queue and process them via a single operation. 
  * Upgraded to **MATE Tweak 17.04.2**
    * Added support for the **new Pantheon layout that uses Brisk Menu**.
  * Upgraded to **MATE Menu 17.04.2**
    * **Added support for [Menulibre](https://smdavis.us/projects/menulibre/) menu editor**, if installed it is preferred over Mozo.
  * Upgraded to **MATE Dock Applet 0.76**
    * Added support for startup notification when launching apps.
    * The applet gets a new look - a new type of indicator and a new type of active icon background have been added.
  * **Dropped 32-bit PowerPC support, completely!**
    * The [32-bit PowerPC architecture has been removed from the 17.04 archive](https://lists.ubuntu.com/archives/ubuntu-devel-announce/2017-March/001206.html).
    * Consequently Ubuntu MATE will not be releasing PowerPC images anymore.
    * Ubuntu MATE **16.04 will continue to support 32-bit PowerPC until 2019 and Ubuntu will offser security updates until 2021.**
  * *A-n-d most exciting of all...* **MATE Calculator is back, ported to GTK3+ and replaces Galculator** `:-D`

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

### Ubuntu family issues

This is our known list of significant bugs that affect all flavours.

  * [No remove media and hit enter to continue dialogue](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1672441)
    * May only affect computers with secure boot enabled.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).