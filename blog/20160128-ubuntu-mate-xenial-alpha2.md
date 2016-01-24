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
    * The Control Contre and System menu categorisations are now consistent.
    * See the [MATE Desktop 1.12 release announcement](http://mate-desktop.org/blog/2015-11-05-mate-1-12-released/) for more details.
  * Updated to Ubuntu MATE Welcome 16.04.1
    * New Ambience theme for the navigation bar.
    * Added System Specifications page.
    * Added detection of graphics card (including VirtualBox)
    including one-click enablement of the graphics-drivers PPA.
    * Added one-click enablement of the LibreOffice Fresh PPA to continually
    track stable LibreOffice releases.
    * Added Firmware and Codecs one-click installers to Getting Started.
    * Added new page for live sessions and guest sessions and hides
    privileged features when launched in guest sessions.
    * Added category labels to the Software section.
    * Improved code re-use for footers (uses JavaScript)
    * Improved presentation to Introduction and Features.
    * Improve page transitions and added expandable/collapsible sub-sections.
    * Hints appear after opening utilities.
    * Updated Firefox, LibreOffice and Control Centre icons.
    * Removed links on software icons. Users were getting confused why
    this opened a web page.
    * Added miscellaneous tasks to update cache, fix an incomplete install
    and fix broken dependencies.
    * Added 0 A.D, Ambient Noise, Aptik, Audio Recorder, Bazaar Explorer,
    BtSync, Boot Repair, Caja Share, Chromium BSU, Dia, DVD Styler,
    EasyTAG, Emby, Enpass, Evolution, Extreme Tux Racer, FlightGear,
    FocusWriter, Frozen Bubble, GCompris, Git-Cola, Glade, Gobby,
    GParted, Hedgewars, HPLIP-GUI, KDE Connect Indicator, LibreOffice Base,
    LibreOffice Draw, LibreOffice Math, LibreOffice (fresh), Liferea,
    Minecraft Server, MySQL Workbench, My Paint, Neverball, Neverputt,
    Nexuiz, Opera, OpenSSH, Owncloud Client, Parcellite, PlayOnLinux,
    Poedit, Recent Notifications, RedNoteBook, ReText, Stellarium,
    Teeworlds, Tor Browser, Virt Manager, WarZone 2100, Wesnoth.
    * Updated Dropbox, VeraCrypt and X2Go.
    * Updated VirtualBox. Closes (LP: #1537395)
    * Installing Adobe Flash now uses `flashplugin-installer`.
  * Updated MATE Tweak to 3.5.5
    * Added support for Compton hardware compositing for Marco and Metacity.
    * Update window manager replacement to correctly migrate xcursor settings.
    * Updated process killing to be less invasive and a pure Python implementation.
    * Updated translations.
    * Removed Muffin support. It is not compatible with MATE.
  * Updated Ubuntu MATE Settings to 16.04.1
    * Added Mutiny panel layout. *(Requires `mate-dock-applet`)*
    * Updated custom menu entries to reduce clutter.
    * Updated gsettings override to improve default behaviour.
    * Corrected LibreOffice default icons to use Human.
  * Updated Ubuntu MATE Artwork to 16.04.1
    * Added MATE colourised icons for categories, devices and places.
    * Added community [contributed wallpaper from Luke Horwell](https://ubuntu-mate.community/t/wallpaper-the-materix/3107)
    * Added community [contributed wallpaper from Rick Lell](https://ubuntu-mate.community/t/wallpaper-ubuntu-mate-greyscaled-wood/3199)
    * Added community [contributed wallpaper from Noe Gonzales](https://ubuntu-mate.community/t/sky-high-wallpaper-photos-licensed-cc-by-sa/3433)
    * Added community [contributed wallpaper from Randall Lewis](https://ubuntu-mate.community/t/wallpaper-solar-systemate-4-flavors-1920x1080/3354)
    * Added community [contributed wallpaper from Sacha](https://ubuntu-mate.community/t/wallpaper-some-parrots-and-an-island/3450)
  * Update MATE Menu to 5.6.7.
    * Fixed 64-bit pointers for the C-Python interface. Thanks to György Balló from Arch Linux.
    * Fixed several calls to `Gdk.Color()`. Thanks to XRevan86 from OpenSUSE.
  * Updated Ubuntu MATE so DVD and BluRay libraries are pre-installed. *This
  doesn't mean DVD and BluRay will play out-of-the-box! But
  DVD playback can be fully enabled via Ubuntu MATE Welcome.*.
  * Updated the languages shipped on the DVD image. The full rationale
  on how we choose the languages and what we install is at <https://launchpad.net/bugs/1520278>.
  * Updated Shotwell to include online account plugins.
  * Improved support for braille displays.
  * Improved `xdg-utils` support.
  * Removed LibreOffice Math and LibreOffice Draw, they can now be added via Ubuntu MATE Welcome.

Thanks to everyone from the Ubuntu MATE community who contributed to
this release!

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 16.04</h1>
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
  * Shutdown/Restart of the live session does not work in Virtualbox and VMWave guests.
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
