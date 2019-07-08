---
layout: blog-post
title: Ubuntu MATE 17.04
permalink: ubuntu-mate-zesty-final-release
description: Ubuntu MATE 17.04 (Zesty Zapus) Final Release
category: release
author: Martin Wimpress
lang: en
---

**We're totally over the bloody moon to announce Ubuntu MATE 17.04.
This is our favourite release of Ubuntu MATE so far and, we believe, a
real return to form. Ubuntu MATE 16.10 was a transitional release, in
every sense, and 17.04 concludes the upheaval of migrating to GTK3+.
This has been a release focused on refining the distro and sweating the
details. As always, we're never finished and eager to start work on
17.10 to bring you futher improvements and refinement. But for now, we
hope you enjoy Ubuntu MATE 17.04 as much as we've enjoyed making it
for you.**

<p align="center">
[Ubuntu MATE 17.04 Beta 2](/gallery/blog/ubuntu-mate-1704-beta2.png)

# What's New in Ubuntu MATE 17.04?

We've put a great deal of effort into refining Ubuntu MATE 17.04 in the
following ways:

  * The [MATE Desktop team](https://github.com/orgs/mate-desktop/teams)
  did an amazing job releasing [MATE Desktop 1.18.0](http://mate-desktop.org/blog/2017-03-13-mate-1-18-released/)
  which completes the transition to GTK3+, fixes countless bugs and
  introduces some much needed new features and modernisations.

  * [Daniel Foré](http://danielfore.com/) from [elementary](https://elementary.io)
  contributed new icons to Ubuntu MATE which deliver style and panache.

  * [Ikey Doherty](https://plus.google.com/+IkeyDoherty) from [Solus](https://solus-project.com/)
  created [Brisk Menu](https://github.com/solus-project/brisk-menu) in
  collaboration with Ubuntu MATE. This efficient menu is integrated in
  the new Pantheon layout available via MATE Tweak.

  * Dave from [Linux & Other Stuff](https://www.youtube.com/channel/UCQpkMe-SLNg0HwWCP3eeTxw)
  contributed a new dark theme, called Ambiant-MATE Dark. We love it!

  * [Wolfgang Ulbrich](https://github.com/raveit65) from [MATE Desktop](https://mate-desktop.org)
  worked tirelessly on all the Ubuntu MATE themes making them all fully 
  compatible with GTK 3.22 add ensuring every pixel is placed exactly
  where it should be.

  * [Michael Tunnel](http://michaeltunnell.com/) from [TuxDigitial](http://tuxdigital.com/)
  contributed retouched art assets for the Ubuntu MATE themes including
  scaled variants for when we are ready to go HiDPI.

  * [Luke Horwell](https://ubuntu-mate.community/users/lah7) from [Ubuntu MATE](https://ubuntu-mate.org)
  updated the Bulk Queue in Ubuntu MATE Welcome and the Software Boutique
  so you can now queue up multiple application install/remove and execute
  them in one operation.

  * [Martin Wimpress](https://flexion.org) from [Ubuntu MATE](https://ubuntu-mate.org)
  did some stuff but no one remembers what.

**We extend our sincere thanks to everyone who contributed to this
Ubuntu MATE release. Thank you!**

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 17.04</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## What changed since the Ubuntu MATE 17.04 Beta 2 release?

This is what has been added, updated or removed.

  * **Upgraded several MATE Desktop 1.18 components**, fixing numerous bugs and some memory leaks.
    * libmatekbd 1.18.2
    * MATE Applets 1.18.1
    * MATE Control Center 1.18.1
    * MATE Panel 1.18.1
    * Eye of MATE 1.18.1
    * Engrampa 1.18.1
    * MATE Sensors Applet 1.18.1
    * MATE Settings Daemon 1.18.1
    * Pluma 1.18.1
    * Caja 1.18.1
    * MATE Utils 1.18.1
    * MATE Icon Theme 1.18.1
    * MATE Themes 3.22.10
  * Upgraded to **Brisk Menu 0.3.5**
    * Add category roll-overs.
    * Add standardised CSS style classes.
    * Assorted bug fixes.
  * Upgraded to **MATE Dock Applet 0.77**
    * Add drag and drop to add applications to the dock.
    * Add drag and drop of data between running applications.
    * Add key bindings to activate and select applications in the dock.
      * `<Super> 1 - 0` for the first 10 applications in the dock.
      * `<Super><Alt> 1 - 0` for applications 10 to 20 in the dock.
    * Bug fixes.
  * Upgraded **Ubuntu MATE Artwork 17.04.11**
    * Completed the Ambiant-MATE Dark theme.
    * Fix keyboard layout view.
    * Fix Brisk Menu button styling to match the other menu applets.
    * Fix scale troughs for inactive windows for Ambiant-MATE Dark.
    * Fix GTK2+ radio and checkbox assets to match GTK3+. (LP: [#1046129](http://pad.lv/1046129))
    * Fix GTK2+ Notebooks, Progress bars and Sliders so they match GTK3+.
    * Fix GTK2+ Ambiant-MATE so that Qt4/Qt5 applications are styled correctly.
    * Fix GTK2+ runtime warnings.
    * Fix GTK2+ and GTK3+ Notebook background and font colours.  
    * Fix GTK3+ switches, particularly in headerbars.
    * Fix GTK3+ button hover focus.
    * Fix background and colours for MATE Terminal and GNOME Terminal.
    * Fix box-shadow on desktop windows.
    * Fix styling for Brisk Menu and MATE Menu.
    * Fix pop-over modelbuttons.
    * Fix solid-csd border colors.
    * Fix border images for Ambiant-MATE Dark.
    * Add missing gtkstyle-fallback settings.
    * Add missing GtkSourceView styles for Ambiant-MATE-Dark.
    * Add Ubuntu MATE community contributed wallpaper, Ubuntu MATE Wet.
    * Remove obsolete GTK2+ styling.    
  * Upgraded to **Ubuntu MATE Welcome 17.04.11**
    * Fix incorrect quoting of URIs which prevent some locales from installing software. (LP: [#1679280](http://pad.lv/1679280))
    * Fix the removal of Adobe Flash if installed via Ubiquity. (LP: [#1676052](http://pad.lv/1676052))    
    * Disable the Install button if Ubiquity is not avaliable. (LP: [#1678582](http://pad.lv/1678582))
    * Add Simple Screen Recorder.
    * Update translations.
  * Upgraded to **Ubuntu MATE Settings 17.04.7**
    * Fix to allow users to change the Firefox homepage. (LP: [#1605887](http://pad.lv/1605887))
    * Fix dynamic placement of Brisk Menu search entry. (LP: [#1677517](http://pad.lv/1677517))
    * Activate Brisk Menu category rollover by default. (LP: [#1677520](http://pad.lv/1677520))

## Known Issues

Here are the known issues.

### Ubuntu MATE issues

  * After completing an OEM install two network icons are present in the panel. (LP: [#1674796](http://pad.lv/1674796))
    * This only happens when the OEM configuration is completed. On subsequent boots only one network icon is shown.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * `dnsmasq-base` is not installed which means Network COnnection sharing doesn't work. (LP: [#1681912](http://pad.lv/1681912))
    * The workaround is to `sudo apt install dnsmasq-base`.

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
