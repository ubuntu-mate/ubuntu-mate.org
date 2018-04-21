<!--
.. title: Ubuntu MATE 18.04 LTS Final Release
.. slug: ubuntu-mate-bionic-final-release
.. date: 2018-04-26 16:00:00 UTC
.. tags: Ubuntu,MATE,Bionic,Beaver,LTS,final,18.04,draft
.. link:
.. description: Ubuntu MATE 18.04 LTS (Bionic Beaver) Final Release
.. type: text
.. author: Martin Wimpress
-->

**Grand standing introduction and thanks to all involved to be added here.**

<div align="center">
<img src="/gallery/blog/1804-final.png" alt="Ubuntu MATE 18.04 LTS" /><br />
</div>

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 16.04 LTS release?

Just about everything. Ubuntu MATE 18.04 is rammed to the rafters with
new features and improvements compared to 16.04.

### MATE Desktop 1.20.1

The MATE Desktop has transitioned from the GTK 2.24 based MATE 1.12 to
the very latest the GTK 3.22 based MATE 1.20.1.

As [you may have seen, MATE Desktop 1.20 was released in February 2018](http://mate-desktop.org/blog/2018-02-07-mate-1-20-released/) and offers some significant improvements:

  * **MATE Desktop 1.20 supports HiDPI displays with dynamic detection and scaling.**
    * HiDPI hints for Qt applications are also pushed to the environment to improve cross toolkit integration.
    * Toggling HiDPI modes triggers dynamic resize and scale, no log out/in required.
  * Marco now supports **DRI3 and [Present](https://keithp.com/blogs/Present/)**, if available.
    * **Frame rates in games are significantly increased when using Marco.**
  * **Marco now supports drag to quadrant window tiling**, cursor keys can be used to navigate the Alt + Tab switcher and keyboard shortcuts to move windows to another monitor were added.

If your hardware/drivers support
[DRI3](https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure) then
Marco compositing is now hardware accelerated. This dramatically improves 3D
rendering performance, particularly in games. If your hardware doesn't support
DRI3 then Marco will fallback to a software compositor.

You can [read the release
announcement](http://mate-desktop.org/blog/2018-02-07-mate-1-20-released/) to
discover everything that improved in MATE Desktop 1.20. It is a significant
release that also includes a considerable number of bug fixes.

**We like to extend our thanks to our friends at
[Entroware](https://www.entroware.com) for rolling their sleeves up and
helping debug [an nvidia driver issue](https://pad.lv/1764005) that was
impacting all flavours of Ubuntu during the last days of the 18.04 development
cycle.**

<div align="center">
<iframe id="ytplayer" type="text/html" width="852" height="480" src="https://www.youtube.com/embed/V6kth-4M62o?html5=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>

### New and updated desktop layouts - *new since 18.04 beta 1*

I have decided to add a new layout to the collection available in Ubuntu MATE
18.04. It will be called **Familiar** and is based on the Traditional layout
with the menu-bar (Applications, Places, System) replaced by Brisk Menu. It
looks like this:

<div align="center">
<img src="/gallery/bionic/familiar.png" alt="Familiar" /><br />
</div>

Familiar is now the the default layout, Traditional will continue to be
shipped, unchanged, and will be available via MATE Tweak for those who prefer
it.

**Netbook layout has been updated** - Since 18.04 beta 1 the maximised windows
now maximise into the top panel like the Mutiny layout. Brisk Menu replaces
the custom-menu and `mate-dock-applet` is used for application pinning and
launching. When maximising a window this offers some decent space savings.

**Mutiny layout has been tweaked** - Since 18.04 beta 1 the launcher icon
is the same size of the docked application icons. We heard you, we understand.
It's the little things, right?

### Global Menu and MATE HUD

<div align="center">
<img src="/gallery/layouts/global-menu.gif" alt="Ubuntu MATE Global Menu" /><br />
</div>

The Global Menu integration is much improved. When the Global Menu is added to
a panel the **application menus are automatically removed from the application
window** and only presented globally, no additional configuration (as was the
case) is required. Likewise removing the Global Menu from a panel will restore
menus to their application windows.

<div align="center">
<img src="/gallery/layouts/mate-hud-local.gif" alt="Ubuntu MATE HUD" /><br />
</div>

The HUD now has a 250ms (default) timeout, holding `Alt` any longer won't
trigger the HUD. This is consistent with how the HUD in Unity 7 works. We've
fixed a number of issues reported by users of Ubuntu MATE 17.10 regarding the
HUD swallowing key presses. The HUD is also HiDPI aware now.

### Ubuntu MATE Welcome - *new since 18.04 beta 2*

Welcome and Boutique have been given some love.

  * The software listings in the Boutique have been refreshed, with some applications being removed, many updated and some new additions.
  * Welcome now has snappier animations and transitions
  * A **new Browser Selection screen** has been added so you can quickly install your preferred browser.

<div align="center">
<img src="/gallery/bionic/browser-selection.png" alt="Browser Selection" /><br />
</div>

### Indicators by default

Ubuntu MATE 18.04 uses Indicators by default in all layouts. These will be
familiar to anyone who has used Unity 7 and offer better accessibility support
and ease of use over notification area applets. The volume in Indicator Sound
can now be over driven, so it is consistent with the MATE sound preferences.
Notification area applets are still supported as a fallback.

<div align="center">
<img src="/gallery/layouts/indicators-small.png" alt="Ubuntu MATE HUD" /><br />
</div>

### MATE Dock Applet

[MATE Dock Applet](https://github.com/robint99/mate-dock-applet) is used in
the Mutiny layout, but anyone can add it to a panel to create custom panel
arrangements. The new version adds support for BAMF and icon scrolling.

  * MATE Dock Applet no longer uses its own method of matching icons to applications and instead uses BAMF. What this means for users is that from now on the applet will be a lot better at matching applications and windows to their dock icons.
  * Icon scrolling is useful when the dock has limited space on its panel and will prevent it from expanding over other applets. This addresses an issue reported by several users in Ubuntu MATE 17.10.

### Brisk Menu

<div align="center">
<img src="/gallery/bionic/brisk-menu-dash.png" alt="Brisk Menu Dash Launcher" /><br />
</div>

Many users commented that when using the Mutiny layout the *"traditional"*
menu felt out of place. The [Solus Project](https://solus-project.com/), the
maintainers of [Brisk Menu](https://github.com/solus-project/brisk-menu), have
add a dash-style launcher at our request. Ubuntu MATE 18.04 includes a patched
version of Brisk Menu that includes this new dash launcher. When MATE Tweak is
used to enable the Mutiny or Cupertino layout, it now switches on the dash
launcher which enables a full screen, searchable, application launcher.
Similarly, switching to the other panel layouts restores the more traditional
Brisk Menu.

**Since 18.04 beta 1 we tweaked the style of the session control buttons** in
Brisk Menu and those updates will be wait for you are you install Ubuntu MATE
18.04 Beta 2.

### MATE Window Applets

The **Mutiny and Netbook layouts now integrate the [mate-window-applets](https://github.com/ubuntu-mate/mate-window-applets)**.
You can see these in action alongside an updated Mutiny layout here:

<blockquote class="imgur-embed-pub" lang="en" data-id="LxJHgeF"><a href="//imgur.com/LxJHgeF">Mutiny undecorated maximised windows</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>

### Minimal Installation

If you follow the Ubuntu news closely you may have heard that 18.04 now has a
Minimal Install option. Ubuntu MATE was at the front of the queue to take
advantage of this new feature.

<div align="center">
<img src="/gallery/bionic/minimal-install.png" alt="Minimal Install" /><br />
</div>

The Minimal Install is a new option presented in the installer that will
install just the MATE Desktop, its utilities, its themes and Firefox. All the
other applications such as office suite, email client, video player, audio
manager, etc. are not installed. If you're interested, here is [the complete
list of software that will not be present on a minimal install of Ubuntu MATE
18.04](https://bazaar.launchpad.net/~ubuntu-mate-dev/ubuntu-seeds/ubuntu-mate.bionic/view/head:/desktop.minimal-remove)

So, who's this aimed at? There are users who like to uninstall the software
they do not need or want and build out their own desktop experience. So for
those users, a minimal install is a great platform to build on. For those of
you interested in creating "kiosk" style devices, such as home brew Steam
machines or Kodi boxes, then a minimal install is another useful starting
point.

### MATE Tweak

MATE Tweak can now toggle the HiDPI mode between auto detection, regular
scaling and forced scaling. HiDPI mode changes are dynamically applied. MATE
Tweak has a deeper understanding of Brisk Menu and Global Menu capabilities
and manages them transparently while switching layouts. Switching layouts is
far more reliable now too. We've removed the *Interface* section from MATE
Tweak. Sadly all the features the Interface section tweaked have been dropped
from GTK3 so are now redundant.

<div align="center">
<img src="/gallery/bionic/mate-tweak.png" alt="MATE Tweak" /><br />
</div>

**We've added the following changes since 18.04 Beta 1**

  * Added support for the modifications to the Netbook layout.
  * Added a button to launch the Font preferences so users with HiDPI displays can fine tune their font DPI.
  * When saving a panel layout the Dock status will be saved too.

### Caja

We've added some new features to the file manager (Caja).

  * Added **[Advanced bulk rename](https://tari.in/www/software/cajarename/)** - A batch renaming extension.
  * Added **[Encryption](https://github.com/darkshram/seahorse-caja)** - An extension which allows encryption and decryption of OpenPGP files using GnuPG
  * Added **[Hash checking](https://github.com/tristanheaven/gtkhash)** - An extension for computing and validating message digests or checksums.
  * Added **[Advanced ACL properties](https://github.com/darkshram/mate-eiciel)** - An extension to edit access control lists (ACLs) and extended attributes (xattr)
  * Updated **[Folder Color](http://foldercolor.tuxfamily.org/)** - An extension for applying custom colours and emblems to folders and files.
  * Replaced the deprecated `caja-gksu` with `caja-admin` which uses PolicyKit to elevate permissions in the file manager for adminstrative tasks.

The deprecated `gksu` is being removed from Debian and we are aligning
with that objective by replacing all use of `gksu` with PolicyKit.

<div align="center">
<img src="/gallery/layouts/caja-rename.png" alt="Caja Rename" /><br />
</div>

### Documentation - *new since 18.04 beta 2*

The Ubuntu MATE Guide is a comprehensive introduction to MATE Desktop and
Ubuntu MATE including **how to use everything we ship by default**, along with
detailed instruction on how to tailor, tweak and customise Ubuntu MATE to your
suit your preferences.

<div align="center">
<img src="/gallery/bionic/ubuntu-mate-guide.png" alt="Ubuntu MATE Guide" /><br />
</div>

<div class="bs-component">
    <div class="jumbotron">
        <h1>Buy the books</h1>
        <p>Print and ebook versions of the books <b>Ubuntu MATE: Upgrading from Windows or OSX</b> and <b>Using Ubuntu MATE and Its Applications</b> are available from our shop.</p>
        <a href="https://ubuntu-mate.boutique" class="btn btn-primary btn-lg">Shop</a>
        </p>
    </div>
</div>

### Slick Greeter

Ubuntu MATE switched to [Slick
Greeter](https://github.com/linuxmint/slick-greeter) during the 17.10
development cycle, which still uses LightDM under the hood but is far
more attractive and is also HiDPI aware.

<div align="center">
<img src="/gallery/layouts/slick-greeter.png" alt="Slick Greeter" /><br />
</div>

We worked with our friends at [Lubuntu](https://lubuntu.me/) and
[Ubuntu Budgie](https://ubuntubudgie.org/) to land **a configuration
utility for Slick Greeter** just moments before the final freeze window
closed for 18.04.

<div align="center">
<img src="/gallery/bionic/lightdm-settings.png" alt="Slick Greeter Settings" /><br />
</div>

### Artwork, Fonts & Emoji

<div align="center">
<img src="/gallery/bionic/emoji.png" alt="Emoji Picker" /><br />
</div>

We are no longer shipping `mate-backgrounds` by default. They have served us
well, but are looking a little stale now. We have created a new selection of
high quality wallpapers comprised of some abstract designs and high resolution
photos from [unsplash.com](unsplash.com). The Ubuntu MATE Plymouth theme (boot
logo) is now HiDPI aware. Our friends at [Ubuntu
Budgie](https://ubuntubudgie.org/) uploaded a new version of Slick
Greeter which now fades in smoothly, rather than the stuttering we saw in
Ubuntu MATE 17.10. We've switched to Noto Sans for users of Japanese, Chinese
and Korean fonts and glyphs. MATE Desktop 1.20 supports emoji input, so we've
added a colour emoji font too.

**New since 18.04 beta 1 the xcursor themes have been replaced** with new
cursors from MATE upstream, that also offer HiDPI support.

### Major Applications

Accompanying **MATE Desktop 1.20.1** and **Linux 4.15** are **Firefox
59.0.2**, **VLC 3.0.1**, **LibreOffice 6.0.3.2** and **Thunderbird 52.7.0**.

<div align="center">
<img src="/gallery/bionic/versions.png" alt="Major Applications" /><br />
</div>

See the [Ubuntu 18.04 Release
Notes](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) for details of all
the changes and improvements that Ubuntu MATE benefits from..

### Raspberry Pi images

We're planning on releasing **Ubuntu MATE images for the Raspberry Pi around
the time 18.04.1 is released, which should be sometime in July**. It takes
about a month to get the Raspberry Pi images built and tested and we simply
didn't have time to do it in time for the April release of 18.04.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 18.04 LTS</h1>
        <p>We've even redesigned the download page so it's even easier to get started.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Upgrading from Ubuntu MATE 16.04 or 17.10

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" dropdown menu to "Long-term support versions".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager` into the command box.
  * Update Manager should open up and tell you: New distribution release '18.04' is available.
  * Click "Upgrade" and follow the on-screen instructions.

### Get the Ubuntu MATE snaps

When the upgrade is complete and you're logged in, open a terminal and execute:

    snap install ubuntu-mate-welcome --classic
    snap install software-boutique --classic
    snap install puilsemixer

The snap packages above are installed when performing a clean install of
Ubuntu MATE 18.04, but are not automatically installed when upgrading from an
earlier release.

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * Anyone upgrading from Ubuntu MATE 16.04 or 17.10 may need to **use MATE Tweak to reset the panel layout to one of the bundled layouts post upgrade**.
    * Migrating panel layouts, particularly those without Indicator support, is hit and miss. Mostly miss.

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * [Ubiquity is uninstalling chosen locale language packs](https://pad.lv/1713702)
    * After a successful installation, your computer may not have all the appropriate language packs installed.
    * To work around this issue, open **Language Support** in the Control Centre and follow the prompts to automatically install the required language packs.
  * [Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
