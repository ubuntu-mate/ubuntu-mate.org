<!--
.. title: Ubuntu MATE 17.10
.. slug: ubuntu-mate-artful-final-release
.. date: 2017-10-19 14:00:00 BST
.. tags: Ubuntu,MATE,Artful,final,17.10
.. link:
.. description: Ubuntu MATE 17.10 (Artful Aardvark) Final Release
.. type: text
.. author: Martin Wimpress
-->

# *Join the Mutiny!*

After six months of tireless work we present Ubuntu MATE 17.10, by far
the best release we've ever produced. I'd like to extended my sincere
thanks to everyone who has contributed to this fine release. The
development theme for Ubuntu MATE 17.10 has been delivering several
different desktop layouts each providing a distictive workflow.
**Checkout MATE Tweak to access to these layouts and join the Mutiny!**

  * **Shipping snaps by default** - *Check!*
  * **Feature rich file manager** - *Check!*
  * **Slick Greeter?** - *Check!*
  * **Global Menus?** - *Check!*
  * **Heads-up Display (HUD)?** - *Check!*
  * **Super key to active menu launchers?** - *Check!*
  * **Functional alternative to Unity 7 for those that want it and a traditional desktop for those that don't?** - *Check!*
  * *Read on to find out more...*

*We mean it, keep reading! Don't just go hunting for the download button
and skip over our most glorious release notes.*

<div align="center">
<img src="/gallery/blog/1710-final-medium.png" alt="Ubuntu MATE 17.10 Final" /><br />
</div>

# What changed since the Ubuntu MATE 17.04 final release?

We've really been burning the midnight oil for the last six months.
This is what has been updated or added.

## Panel Layouts

We [surveyed our community about potentially changing the default UI](https://ubuntu-mate.community/t/poll-pantheon-to-become-the-default-layout-in-17-10/12817).
The feedback was mixed when factoring in the results from
[Twitter](https://twitter.com/ubuntu_mate/status/855704668097441793),
[Google+](https://plus.google.com/+MartinWimpress/posts/MtuF4edeSqi) and
[Straw Poll](http://www.strawpoll.me/12799961/r).

But it was the comments from our users that were most compelling. [We
decided to leave the default
alone](https://ubuntu-mate.community/t/ubuntu-mate-17-10-default-layout-decisions/12878?u=wimpy),
a personally difficult decision, and turned our attention to
rationalising the panel layouts and thoughtfully reconfiguring them.
Each panel layout is distinctive and now provides a different desktop
workflow:

  * **Mutiny** mimics the Unity 7 interface
  * **Cupertino** provides something similar to macOS
  * **Redmond** will be familiar to Windows users
  * **Pantheon** a hybrid for long time desktop Linux users who want some modern conveniences
  * **Contemporary** a blend of the best of the old and the sprinkle of the new
  * **Netbook** people still use them and this layout is for them
  * **Traditional** just like your Dad remembers it, and still the default

Here are a few screenshots to give you a feel for how things look.

<!-- Outer wrapper for presentation only, this can be anything you like -->
<div align="center">
<div id="banner-fade">
  <!-- start Basic Jquery Slider -->
  <ul class="bjqs">
    <li><a class="image-reference" href="/gallery/layouts/00_mutiny.png"><img src="/gallery/layouts/00_mutiny.png" title="Mutiny Panel Layout"></a></li>
    <li><a class="image-reference" href="/gallery/layouts/01_cupertino.png"><img src="/gallery/layouts/01_cupertino.png" title="Cupertino Panel Layout"></a></li>
    <li><a class="image-reference" href="/gallery/layouts/02_redmond.png"><img src="/gallery/layouts/02_redmond.png" title="Redmond Panel Layout"></a></li>
    <li><a class="image-reference" href="/gallery/layouts/03_pantheon.png"><img src="/gallery/layouts/03_pantheon.png" title="Pantheon Panel Layout"></a></li>
    <li><a class="image-reference" href="/gallery/layouts/04_contemporary.png"><img src="/gallery/layouts/04_contemporary.png" title="Contemporary Panel Layout"></a></li>
    <li><a class="image-reference" href="/gallery/layouts/05_netbook.png"><img src="/gallery/layouts/05_netbook.png" title="Netbook Panel Layout"></a></li>
    <li><a class="image-reference" href="/gallery/layouts/06_traditional.png"><img src="/gallery/layouts/06_traditional.png" title="Traditional Panel Layout"></a></li>
  </ul>
  <!-- end Basic jQuery Slider -->
</div>
<!-- End outer wrapper -->
</div>
<script src="/assets/js/jquery.min.js"></script>
<script src="/assets/js/bjqs-1.3.min.js"></script>
<script>
    jQuery(document).ready(function($) {
    $('#banner-fade').bjqs({
        width : 960,
        height : 540,
        responsive : true,
        usecaptions : true
    });
});
</script>

## Global Menu

Global Menu support is now much improved, even compared to 17.10 Alpha
2, and available via the **Contemporary**, **Cupertino** and **Mutiny**
layouts which can be **activated via MATE Tweak**. Fully functional
with GTK, Qt, LibreOffice, Firefox/Thunderbird, Google Chrome, Electron
and others. You can now make more of your available screen space while
using Ubuntu MATE.

<div align="center">
<img src="/gallery/layouts/global-menu.gif" alt="Global Menu" /><br />
</div>

**NEW in 17.10 Beta 1** - Thanks to the excellent testing feedback
we've had since 17.10 Alpha 2 we've made the Global Menu far more
reliable and now operate correctly regardless of whether the
application was launched from the terminal, menu or launcher.

## Super key

<img class="right" src="/gallery/layouts/superkey.png" alt="Super Key">

Complete Super key support is available from several of the panel
layouts. We're thrilled to welcome [Victor
Kareh](https://github.com/vkareh/) to the [team](/team/) who has been
busy patching [MATE Settings Daemon](https://github.com/mate-desktop/mate-settings-daemon),
[MATE Menu](https://github.com/ubuntu-mate/mate-menu),
[Brisk Menu](https://github.com/solus-project/brisk-menu) and
[MATE Dock Applet](https://github.com/robint99/mate-dock-applet) to
make the Super key work the way you'd all expect. This means <kbd>Super</kbd>
can be used to activate the menus/launchers and any other key-bindings
that include the <kbd>Super</kbd> key also continue to function correctly.

MATE Dock Applet, used in the Mutiny layout, also includes launching or
switching to docked items based on their position using in the dock
using <kbd>Super</kbd> + <kbd>1</kbd>, <kbd>Super</kbd> + <kbd>2</kbd> which will be familiar to Unity 7 users.
<kbd>Super</kbd> + <kbd>L</kbd> is also recognised as a screen lock key-binding along with the
usual <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd> that MATE Desktop users expect.

## Heads-Up Display

This is something we started during Ubuntu MATE 16.10 and never
perfected, but is now ready for prime time. A favourite of Unity 7
users is the Heads-Up Display (HUD) which provides a way to search for
and run menu-bar commands without your fingers ever leaving the
keyboard.

So if you're trying to find that single filter in Gimp but can't
remember which filter category it fits into or if you can't recall if
preferences sits under File, Edit or Tools on your favourite browser,
you can just search for it rather than hunting through the menus.

Just like Global Menus the HUD is currently only available via the
**Contemporary**, **Cupertino** and **Mutiny**.

### HUD improvements since 17.10 Alpha 2

We've improved the HUD significantly since Alpha 2 thank to all the
great testing feedback.

  * **NEW in 17.10 Beta 1** - The HUD is now **activated by just pressing** <kbd>Alt</kbd>, as you would expect in Unity 7.
  * The HUD is now reliably activated. In Alpha 2 is only responded to about one third of requests.
  * **NEW in 17.10 Beta 1** - The **HUD is now locally integrated**, so that it overlays on top of the activate application.

<div align="center">
<img src="/gallery/layouts/mate-hud-local.gif" alt="The Locally integrated Heads-Up Display (HUD)" /><br />
</div>

### Locally integrated rationale

The purpose of the HUD is to keep your fingers on the keyboard and
improve the efficiency in driving the menus for keyboard centric users.
We've locally integrated the HUD for similar reasons, if you're looking
at an application why move the HUD to the top of screen away from where
your eyes are already focused. Keeping the HUD within the context of
the active application eliminates refocusing your attention to a
different part of the screen, particularly helpful for users with high
resolution or multi-display workstations.

## Indicators

We've been improving Indicator support from release to release for some
time now. But with in Ubuntu MATE 17.10 many of the panel layouts offer
a complete line up of Indicators, all of which are fully compatible
with MATE. The default Indicators are:

  * Optimus (*only available if you have nvidia prime capable hardware and drivers*)
  * Bluetooth
  * Network
  * Power
  * Messages
  * Sound
  * Session

<div align="center">
<img src="/gallery/layouts/indicators.png" alt="Indicators" /><br />
</div>

## MATE Tweak

MATE Tweak is your gateway to activating different user interface
layouts and exploring the contrasting ways you can run Ubuntu MATE.
MATE Tweak has been given a coat of fresh paint and adds a couple of
much requested features.

  * Saving your own custom panel layout using a name of your choosing.
  * Prompts before executing operations that could wipe your custom, but unsaved, tweaks.
  * **NEW in 17.10 Beta 1** - You can also delete previously saved custom panel layouts.

<div align="center">
<img src="/gallery/layouts/mate-tweak.png" alt="MATE Tweak, more than just a tweak tool." /><br />
</div>

When activating the Compton compositor you should now experience an
entirely tear free experience that is optimised for gaming. Thanks to
[Perdro Mateus](https://plus.google.com/+PedroMateus) from
[Linux Game Cast](https://linuxgamecast.com/) podcast for his help test
the various GPU, IGP and driver combinations. [`#LGCCares`](https://twitter.com/hashtag/LGCCares?src=hash)

While we were tuning compositors we gave some love to Compiz, which now
uses less RAM and fixes a number of niggles.

## Community Wallpaper

The Ubuntu MATE community participated in a [wallpaper competition](https://ubuntu-mate.community/tags/wallpaper-comp-17-10)
and have already [voted for their favourite](https://ubuntu-mate.community/t/vote-for-the-default-wallpaper-in-ubuntu-mate-17-10/14079?u=wimpy).
Congratulations to [Richard van Liessum](https://ubuntu-mate.community/u/richard)
for creating the winning entry! You have to install Ubuntu MATE 17.10
to see the full line up of new artwork though `;-)`

## Slick Greeter

**NEW in 17.10 Beta 1** - We've switched to Slick Greeter which still
uses LightDM under the hood but has a much nicer look and feel.

<div align="center">
<img src="/gallery/layouts/slick-greeter.png" alt="Slick Greeter" /><br />
</div>

## File manager

**NEW in 17.10 Beta 2** - We've added some new features to Caja, the
MATE file manager.

  * Added [Advanced bulk rename](https://tari.in/www/software/cajarename/).
  * Added [Hash checking](https://github.com/tristanheaven/gtkhash).
  * Replaced `caja-gksu` with `caja-admin`.
    * The obsolete `gksu` is being removed from Debian and we are aligning with that objective by replacing the use of `gksu` with PolicyKit.
  * Updated [Folder Color](http://foldercolor.tuxfamily.org/). Now supports custom emblems and properly integrates with the Ubuntu MATE default icon theme.

<div align="center">
<img src="/gallery/layouts/caja-rename.png" alt="Caja Rename" /><br />
</div>

## Snaps installed by default

**NEW in 17.10 Final** - Ubuntu MATE is pioneering pre-installed snap
support by being the first distro to ship a snap by default. For the
Ubuntu MATE 17.10 release the `pulsemixer` snap, [a console based mixer for
PulseAudio](https://github.com/GeorgeFilipkin/pulsemixer), is installed
by default.

<div align="center">
<img src="/gallery/layouts/pulsemixer.png" alt="pulsemixer" /><br />
</div>

Pre-installing snaps by default in the desktop images was an outcome of
the [Ubuntu Rally that took place in New York](https://insights.ubuntu.com/2017/09/01/ubuntu-rally-in-nyc/).
Installing the `pulsemixer` snap by default in Ubuntu MATE 17.10 is
being used as a pilot and what we learn will help the Ubuntu Desktop
team with their efforts to ship snaps by default in Ubuntu 18.04.

Adding `pulsemixer` to the default Ubuntu MATE 17.10 has not
significantly affected the size of the iso image. We chose `pulsemixer`
because it is a small, useful application, that has never been
available in the Debian or Ubuntu archives.

### The bit no one reads but probably should

Here's the full run down of what changed since Ubuntu MATE 17.04:

  * Ubuntu MATE now features a Global Menu implementation provided ia [vala-panel-appmenu](https://github.com/rilian-la-te/vala-panel-appmenu) and most of the UBuntu idicators are now available with MATE compatibility.
  * Upgraded to **MATE HUD** 17.10.9-0ubuntu1 which fixes broken event replay due to synchronous key grab.
  * Upgraded to **MATE Optimus** 17.10.1-1ubuntu0 which now features nvidia hardware detection, including external Thunderbolt connected devices.
  * Upgraded to **Brisk Menu** 0.4.5 has improved Super key support and numerous fixes, plus a few settings that MATE Tweak can manipulate to augment how Brisk is presented in different layouts.
  * Upgraded to **MATE Menu** 17.10.8-0ubuntu1 now has better relevance of launcher search results, can now optionally search Duck Duck Go, has numerous fixes and that all important Super key was improved.
  * Upgraded to **MATE Dock Applet** 0.79 has improved Super key support and several bug fixes.
  * Upgraded to **Ubuntu MATE Welcome** 17.10.15 has been stocked with even more new applications for you to discover and
    * The *all new* Software Boutique is not ready yet, so this is the Boutique you know and love. Just better stocked.
  * **Added [PulseMixer](https://github.com/GeorgeFilipkin/pulsemixer) snap to the default install.**
  * Removed Synapse and HexChat from the default install.
  * **Added [Redshift](http://jonls.dk/redshift/)**, which adjusts the colour temperature of your screen according to your surroundings, is installed by default but not enabled by default.
  * Dropped `caja-gksu` and migrated `gdebi` to PolicyKit - *Thanks Simon Quigley*
    * `caja-admin` has replaced `caja-gksu`
    * `gksu` is being removed from Debian so we are aligning with that objective by removing `gksu` from Ubuntu MATE.
  * **Caja now includes the [GtkHash](https://github.com/tristanheaven/gtkhash) and [Caja Rename](https://tari.in/www/software/cajarename/) extensions**.
  * **New Ubiquity Slide Show**
    * Completely redesigned to introduce users to more of the features unique to Ubuntu MATE.
    * **Added Ubuntu MATE logo to Ubiquity**.
  * Patched `unity-gtk-module` to fix ghosting artefacts when dragging and dropping icons.
  * Many of the Ubuntu MATE defaults have been changed or updated
    * **Replaced `lightdm-gtk-greeter` with `slick-greeter`.**
    * Added keybindings for <kbd>Shift</kbd> + <kbd>Print Screen</kbd> to grab a screen area when taking a screenshot.
    * **Added defaults for Chromium**, which will show the [Ubuntu MATE Start](https://start.ubuntu-mate.org) page, *should you install it*.
    * Added sane defaults and tookit integration for `smplayer`, *should you install it*.
  * **New Ubiquity Slide Show**
    * Completely redesigned to introduce users to more of the features unique to Ubuntu MATE.
    * **Added Ubuntu MATE logo to Ubiquity**.
  * MATE Desktop 1.18 has seen many updates, with lots of bugs fixes. Nothing new, just be more stability.
    * Some long standing bugs with `systemd` integration and DBus session activation have been fixed.
  * The **Ubuntu MATE themes have been improved** via the release of `ubuntu-mate-artwork` 17.10.10
    * Several improvements Plymouth splash screens, both text and graphical varieties.
    * Add missing panel-grid to Radiant-MATE.
    * **Improve linked button styling for message dialogs**.
    * Add syntax for panel-grid image to support MATE 1.20.
    * Improve **clock-applet-button so it is consistent with other buttons**.
    * Add top `border-radius` for `.titlebar > headerbar` - *workaround for incorrect upstream use of the GTK API*
    * **Improved notebook (tab) styling**.
    * Updated GtkSourceView themes (used by text editors).
    * **Add bold style classes for Global Menu**.
    * Fix color of grey-out arrows in menus.
    * Fix padding of primary/secondary image in GtkEntry.
    * Improve menu items by adding slightly more padding.
    * Add a minimal padding to na-tray-applets.
    * Add the Ubuntu MATE logo as the distributor-logo.
    * Fix incorrect CSS syntax for Caja.
    * Fix world-map border color in clock-applet.
    * Fix GtkScale slider mouse-selection if slider is out of range.
    * Fix height of headerbar for `metacity-theme-viewer` - *workaround for incorrect upstream use of the GTK API*
    * Fix border color of scrollbars.
    * Remove obsolete chrom{e|ium} styling.
    * Remove unwanted backdrop states.
  * Experimental HiDPI support is a little less experimental.
  * ...and a whole lot of other little improvements and fixes.

The above in addition to the [general changes that Ubuntu 17.10 introduced](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes).

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 17.10</h1>
        <p>We've even redesigned the download page so it's even easier to get started.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Upgrading from 17.04

To upgrade on a desktop system:

  * Open *Software & Updates* from the Control Centre
  * Select the 3rd Tab called *Updates*.
  * Set the *Notify me of a new Ubuntu version* dropdown menu to *For any new version*.
  * Press <kbd>Alt</kbd> + <kbd>F2</kbd> and type in `update-manager -c` into the command box.
  * Update Manager should open up and tell you: New distribution release '17.10' is available.
  * If not you can also use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click *Upgrade* and follow the on-screen instructions.

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * *Nothing critical.*

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * [The Ubiquity installer may auto select US keyboard layout](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1713664)
    * To work around this manually, select the correct regional keyboard layout for your computer.
  * [Ubiquity is uninstalling chosen locale language packs](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1713702)
    * After a successful installation, your computer may not have all the appropriate language packs installed.
    * To work around this issue, open **Language Support** in the Control Centre and follow the prompts to automatically install the required language packs.
  * [Ubiquity slide shows are missing for OEM installs of Ubuntu Budgie and Ubuntu MATE](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
