---
layout: blog-post
class: blog
title: Ubuntu MATE 19.10 Release Notes
permalink: /blog/ubuntu-mate-19-10-eoan-ermine-release/
description: Ubuntu MATE 19.10 (Eoan Ermine)
category: release
author: Martin Wimpress
lang: en
discourse_topic_id: 21343
---

**Ubuntu MATE 19.10 is a significant improvement over Ubuntu MATE 18.04 and 19.04.
The theme of this release is to address as many *"paper-cut"* issues as
possible. Every new feature in Ubuntu MATE 19.10 has been added to address
bugs or poor user experience. Many long standing paper-cuts are finally
resolved. Make yourself a cup of tea ☕ and get a slice of cake 🍰 before reading
on to find out what we've been working on for the last 25 weeks.**


{:.center}
![Ubuntu MATE 19.10 Beta](/images/blog/eoan/eoan-ermine-desktop.png)
**_Harder, Better, Faster, Stronger_**


# Ubuntu MATE 19.10 - paper 🧻 cut ️🔪 release

I have not been completely happy 😞 with the quality of recent Ubuntu MATE
releases. All the important stuff works but there have been niggly issues
that by themselves are not deal breakers, but in aggregate are frustrating 😠
and spoil the experience. I've been focused on resolving these issues during
the 19.10 development cycle and you'll see that every new feature in Ubuntu
MATE 19.10 addresses one of these paper-cuts. We've achieved this by expanding
our QA team significantly and Ubuntu MATE 19.10 has been subject to weekly
testing throughout this cycle. I can't thank our QA team enough for
highlighting the issues that need attention.

Most of **the paper-cut effort has been focused around the window manager,
the panel and the indicators** as these are the main touching points of the
desktop environment that users interact with.

## MATE Desktop 1.22.2

Upstream [MATE Desktop](https://mate-desktop.org) recently released 1.22.2.
All the updates are present in Ubuntu MATE 19.10 plus I've cherry 🍒 picked a
good deal of fixes from MATE Desktop development snapshots. In total, 67
additional patches have been applied to the MATE Desktop packages in Ubuntu
MATE 19.10 to finesse this release prior to launch day 🚀 Included in those
patches are fixes for **locking the screen on resume from suspend**, adding
a **Media Information extension to the file manager**, **performance
improvements for the window manager** and **cycling external displays using**
<kbd>Super</kbd> + <kbd>p</kbd>. All this work has also been submitted
to [Debian](https://www.debian.org/).

**Since the final beta we worked on the following**:

  * Added *experimental* ZFS 🗄 install option.
  * Fixed rendering window controls on HiDPI 🔍 displays.
  * Fixed irregular icon sizes 📏 in MATE Control Center and made them render nicely on HiDPI displays.
  * Fixed Caja 📂 extensions not loading.
  * Fixed `mate-power-manager` 🔌 so it uses upower-glib `get_devices2()`.
  * Fixed Pluma 🗒 plugins not loading.
  * Fixed a crasher 💣 in MATE Dock Applet due to an Attribute error in `adjust_minimise_pos()`.
  * Fixed a `gnome-keyring` timeout ⏱ in `mate-session-manager`.
  * Fixed Codec 🎞 updates in Software Boutique.
  * Updated Advanced MATE Menu ⚙ to use the `start-here` icon, so all menus are consistent.
  * Updated the Ubuntu MATE Guide ❓
  * Updated the Ubiquity Slideshow 🎭

### Window Manager improvements

Marco is the Window Manager for MATE Desktop and in Ubuntu MATE 19.10
it brings a number of new features and fixes.

**XPresent support is properly fixed** which means that **screen tearing is now
a thing of the past** and **invisible window corners are finally here!** Invisible
window corners mean that windows can be easily resized 📏 without having to
precisely grab the window corners. **HiDPI rendering improvements** fix a number
of rendering problems that were present in various themes and components,
**most notably windows controls are now HIDPI aware**.

| **Before** 😢 | **After** 😀 |
| ------------- | ------------ |
| ![Before](/images/blog/eoan/lo-windows-controls-clip.png) | ![After](/images/blog/eoan/hi-windows-controls-clip.png)

**Alt+Tab navigation** makes it possible to
traverse the application switcher via keyboard and mouse. We've also **cleaned
up the window controls** by removing the menu button. The menu is still
available either by right clicking the window title bar or pressing
<kbd>Alt</kbd> + <kbd>Space</kbd>.

### Compiz & Compton

The main reason we've been shipping shipping Compton and Compiz in Ubuntu MATE
was to offer a solution to screen tearing or improve game performance. Compiz
has invisible window borders and also has a great screen magnifier suitable
for visually impaired users. However, now that...

  * Magnus (see below) provides screen magnification
  * Marco supports invisible windows borders
  * Marco has improved Alt+Tab behaviour
  * Marco is free from screen tearing
  * Marco frame performance when gaming is further improved
  * Using Compton and Compiz with MATE Desktop introduces other bugs and integration issues

...it is **time to remove Compiz and Compton from the default Ubuntu MATE
install**. The fundamental reasons for including them no longer exist.

If you love 😍 Compiz, it can be installed by opening a terminal and running
the following command:

    sudo apt install compiz compiz-core compiz-mate compiz-plugins compiz-plugins-default

Only having one window manager to target means we can promptly deliver new
features and minimise development effort. Which brings us to...

### New Key-bindings

The key-bindings for window tiling have only worked on full keyboards ⌨️ with a
10-key pad. Few laptops 💻 have a 10-key pad and not all keyboards have a
10-key either. There are some well known key-bindings from other platforms that
were not recognised in Ubuntu MATE. So, we've had a think 🤔 and come up with this:

  * <b>Maximise Window:</b> <kbd>Super</kbd> + <kbd>Up</kbd>
  * <b>Restore Window:</b> <kbd>Super</kbd> + <kbd>Down</kbd>
  * <b>Title Window right:</b> <kbd>Super</kbd> + <kbd>Right</kbd>
  * <b>Title Window left:</b> <kbd>Super</kbd> + <kbd>Left</kbd>
  * <b>Center Window:</b> <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>c</kbd>
  * <b>Title Window to upper right corner:</b> <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Right</kbd>
  * <b>Title Window to upper left corner:</b> <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Left</kbd>
  * <b>Title Window to lower right corner:</b> <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Right</kbd>
  * <b>Title Window to lower left Corner:</b> <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Left</kbd>
  * <b>Shade Window:</b> <kbd>Control</kbd> + <kbd>Alt</kbd> + <kbd>s</kbd>

I'm happy 😀 with these key-bindings as it is now possible to tile a window to
all screen quadrants 📐 using any keyboard form factor.

We updated the application launcher key-bindings, some of these have existed
in Ubuntu MATE for a while:

  * <b>Cycle external displays:</b> <kbd>Super</kbd> + <kbd>p</kbd>
  * <b>Lock Screen:</b> <kbd>Super</kbd> + <kbd>L</kbd>
  * <b>Screenshot a rectangle:</b> <kbd>Shift</kbd> + <kbd>PrintScr</kbd>
  * <b>Open File Manager:</b> <kbd>Super</kbd> + <kbd>e</kbd>
  * <b>Open Terminal:</b> <kbd>Super</kbd> + <kbd>t</kbd>
  * <b>Open Control Center:</b> <kbd>Super</kbd> + <kbd>i</kbd>
  * <b>Open Search:</b> <kbd>Super</kbd> + <kbd>s</kbd>
  * <b>Open Task Manager:</b> <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>Escape</kbd>
  * <b>Open System Information:</b> <kbd>Super</kbd> + <kbd>Pause</kbd>

The key-bindings compliment existing well established alternatives. So if
<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>t</kbd> (Terminal) and
<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd> (Lock Screen) are ingrained in
your muscle 💪 memory 🧠 they are still available too. You can find all the
keyboard shortcuts documented in the **Getting Started section of Ubuntu MATE
Welcome**.

## Panel & Indicator improvements

This is where a good deal of effort has been invested. Let's break it down.

### Brisk Menu and MATE Dock Applet

[Brisk Menu](https://github.com/getsolus/brisk-menu) is under the Solus GitHub
organisation, but it's been a couple of years since it had a new release. The
Solus Project gave me administrative access 🔱 to the Brisk Menu repo and I've
made a new release. Thanks to the efforts of a couple of Ubuntu MATE
contributors several bug 🐞 fixes have landed too, which includes **resolving
frequent crashers in Brisk Menu, preventing a scrollbar always appearing
in the category column** of the menu and **silencing sounds firing as you
rollover menu entries**.

The previous maintainer of [MATE Dock Applet](https://github.com/ubuntu-mate/mate-dock-applet)
announced that he no longer had the time ⌛️ to develop the project. Ubuntu
MATE has taken on ownership and we've already published a couple of new
releases 🤘 which include fixes for frequent crashes.

### MATE Panel

MATE Panel has had a long standing bug fixed that caused it to crash 💥 when
the panel was reset or replaced. This was most noticeable when switching panel
layouts via MATE Tweak and could result in the panel layout being left
incomplete or entirely absent. This bug is now fixed! MATE Tweak has been
updated to neatly integrate with with fixed MATE Panel behaviour so that **layout
switching is now 100% reliable**.

### Indicators

A bug which resulted in **oversized icons in indicators is finally resolved**.


{:.center}
![Before](/images/blog/eoan/indicators-before.png)
**Before 😢**

{:.center}
![After](/images/blog/eoan/indicators-after.png)
**After 😀**


However, it turned out some of the bugs were due to the icons 🎨 themselves.
Over 💯 icons have been refactored 🖌️️ to correct their resolutions or aspect
ratio; as a result the panel and indicators both scale correctly.

A race condition that could result in **two network status icons being
displayed is fixed**, and **when connected via VPN, lock icons are now
overlayed on the Network Indicator**. The battery 🔋 indicator is improved
and now has a larger **charging symbol while charging**.

We've **added the Date/Time Indicator and integrated it with MATE Desktop
and it now replaces the MATE clock applet** which corrects the placement of
the clock and session indicators.

We've finally addressed a long standing issue which has been around since
Ubuntu MATE 14.10 🕸️ Some of the monochrome symbolic icons used in the
indicators were also used in applications. The presented a couple of issues:

  * In some cases you couldn't easily see the icons against the window base colour.
  * The mix of monochrome and full colour icons in applications looked inconsistent.

This issue is now resolved, **monochrome symbolic icons are only used for
indicators and full colour icons are used in the Control Center, Sound
Preferences, Bluetooth, OSD, etc**.

### MATE Window Applets

[MATE Window Applets](https://github.com/ubuntu-mate/mate-window-applets)
have received a number a bug fixes and new features from a community
contributor. Window control icons now dynamically load from the currently
selected theme, rather than requiring manual user configuration, and
**a number of bugs (including significant memory leaks) have also been
resolved**.

## Notification Center

Ubuntu MATE 19.10 includes a **new Indicator that provides a "notification
center"** 🔔 We worked with the [upstream developer to add new features
to indicator-notifications](https://github.com/trism/indicator-notifications)
and integrate it with MATE Notifications Daemon.

{:.center}
![Notification Settings](/images/blog/eoan/notification-settings.png)

We now have a **notification center which also offers a "do not disturb" 🛑
feature**. When do not disturb is enabled, notifications will not be displayed
but will be captured in the notification center for review. It's also
**possible to blacklist some notifications**, so they are never stored by the
notification center. I've created an icon theme for the notification center so
it fits the look and feel of the default Ubuntu MATE theme. **Notification hints
are also fixed** so any notifications supplying additional media, such as
sounds or icons, now work.

Personally, I love ❤️ this feature! No more will I have awkward messages from
my Mum flash up while I'm presenting 😜

## Evolution replaces Thunderbird

The Ubuntu MATE development team discussed the pros and cons of switching the
default mail ✉️ client in Ubuntu MATE to
[Evolution](https://wiki.gnome.org/Apps/Evolution). Here is a summary of our
assessment:

  * Thunderbird does not integrate as well with the desktop.
    * For example, theme integration, font integration, compatibility with HUD (which is increasingly difficult to support in Thunderbird), notifications with action buttons, locale and spell checking.
  * Thunderbird & Lightning occupies 171MB on the ISO image, while Evolution uses 46MB.
  * Evolution integrates well with MATE Desktop given that both use GTK3.
  * **Evolution includes interoperability with LibreOffice**, for which Ubuntu MATE is already shipping the required components.
  * Evolution has superior **integration with Google Mail and Exchange**, including calendar, contacts, tasks, and memos.

**Indicator Date/Time also integrates with Evolution**. It is fully functional,
all the features of creating new events or opening upcoming events from the
indicator work. Clicking on a day in the month displays the events for the
selected day etc.

{:.center}
![Indicator Date/Time](/images/blog/eoan/indicator-datetime.png)

For the many people who use web-mail exclusively this change will have no
impact, but for those who use desktop mail we feel these productivity 📈
improvements are significant.

For those of you who love 💕 Thunderbird and wish to continue using it: we will
continue to offer Thunderbird in the Software Boutique for a one-click install.
Likewise, Evolution is now in the Software Boutique so can be installed/removed
with one-click too.

## GNOME MPV replaces VLC

We have **switched from VLC to GNOME MPV**, soon be renamed to
[Celluloid](https://celluloid-player.github.io/), for the default media
player 🎬 The reasons for switching to GNOME MPV are similar to swapping out
Thunderbird for Evolution; **better desktop integration**.

{:.center}
![GNOME MPV](/images/blog/eoan/gnome-mpv.jpg)

We've changed GNOME MPV's default UI to better fit in with MATE Desktop by
not using client side decorations (CSD). GNOME MPV has an MPRIS implementation
that completely integrates with the Sound Indicator. GNOME MPV uses less space
on the ISO image compared to VLC and we'll get on to why that is important
later.

GNOME MPV doesn't offer the extensive array of preferences and options
to users that VLC does, and instead ships sane defaults; only surfacing
options where they make sense. GNOME MPV is a GTK3 application whereas VLC uses
Qt5. **GNOME MPV looks right at home in Ubuntu MATE which uses GTK3 throughout**.
While we've done our best to coerce VLC to take hints from the GTK theme, it
has never been perfect. Most importantly, **GNOME MPV is an excellent media
player with the same broad media format support that VLC offers**. Ubuntu MATE
20.04 will ship Celluloid 🎞️, the new name for GNOME MPV. VLC will remain in
the Software Boutique as a single click install for anyone who wants it.

## Magnus

Most desktop environments are lacking a screen magnifier, which is an essential
application for visually impaired 👓 computer users and also useful for accurate
graphical design or detail work. One of the reasons we ship Compiz in Ubuntu
MATE is because it has an excellent screen magnifier and was our solution for
people who need magnification 🔍

{:.center}
![Magnus](/images/blog/eoan/magnus.png)

I collaborated with my friend [Stuart Langridge](https://twitter.com/sil)
to create [Magnus](https://kryogenix.org/code/magnus/); **a very simple
desktop magnifier**, showing the area around the mouse pointer in a separate
window magnified two, three, four, or five times. Magnus is now shipped 🚢
by default in Ubuntu MATE 19.10, Ubuntu Budgie 19.10 and other distros are
already picking up it too 💪

## Ubuntu MATE Themes

Dozens of theme related bugs have been fixed and the Ubuntu MATE themes have
been added to the `gtk-common-themes` used by snaps, **so snapped applications
are themed correctly for Ubuntu MATE users now**. This change is already
available all the way back to Ubuntu MATE 16.04.

The most noticeable theme issues that have been resolved are **expanders in tree
view are now a sensible size** (they were so tiny) so you can easily click them,
**window controls are correctly proportioned on CSD windows** and we've add a
splash of Chelsea Cucumber 🥒 to the Ubuntu MATE logo on the menu. Everything
the QA team highlighted has been fixed 🔨

## MATE Tweak and Ubuntu MATE Welcome

MATE Tweak now **preserves user preferences when switching between custom
layouts** thanks to a community contribution.

If you're familiar with MATE Tweak you'll know it can switch panel layouts
to somewhat mimic other platforms and distros 🐧 We have now integrated a
graphical layout switcher in Ubuntu MATE Welcome to better promote the feature
and make it more accessible. We have actually had this feature since 18.04 but
the bugs in MATE Panel I mentioned earlier meant it didn't work. With all the
associated panel bugs fixed 🔧 we now have this:

{:.center}
![Desktop Layout Switcher](/images/blog/eoan/desktop-layout.png)

## NVIDIA drivers

If you've been following the news surrounding Ubuntu you'll know that
Ubuntu will be shipping 🚢 the NVIDIA proprietary drivers on the ISO images.
Anyone selecting the additional 3rd party hardware drivers during installation
without an Internet connection will have the drivers available in offline
scenarios.

This comes at the cost of increasing the ISO size by ~115MB, but I think this
trade-off is worth it. The drivers are not active by default, just present in
the apt repository provided on the ISO image to facilitate installation should
they be requested. But, if your computer has an NVIDIA GPU, you can now have
the drivers installed and operational immediately following install 🌟

Post-install, Ubuntu MATE users with computers that support hybrid graphics
will see the MATE Optimus hybrid graphics applet displaying the NVIDIA logo.

{:.center}
![MATE Optimus](/images/blog/eoan/mate-optimus-19.10.1.png)

Now the NVIDIA 435 drivers are in Ubuntu 19.10, I have given MATE Optimus an
update. MATE Optimus adds support for NVIDIA On-Demand and will now prompt
users to log out when switching the GPU's profile. MATE, XFCE, Budgie,
Cinnamon, GNOME, KDE and LXQt are all supported. Wrappers, called `offload-glx`
& `offload-vulkan` can be used to easily offload games/apps to the PRIME
renderer. **I'm also delighted to see Ubuntu Budgie 19.10 are shipping MATE
Optimus too!**

The **NVIDIA drivers are now going to receive updates via the official
Ubuntu software repository**. So no need to add a PPA to get updates and more
importantly, **the NVIDIA drivers are signed (which is not supported for
drivers distributed via PPA) so you can keep Secure Boot enabled.**

## ISO optimisations

In order to squeeze those ~115MB of NVIDIA drivers on the ISO while keeping
the ISO at ~2.0GB required some optimisation. Certainly switching to Evolution
helped a bit. We've also **dropped Brasero from the default installed
applications** because optical media burning is not a widespread use case
these days. Brasero is still in Software Boutique should you need it.

The main gains came from **analysing the data we have about our user distribution
across countries** and changing what language packs we make available on the ISO.
We get the data from [snap metrics](https://snapcraft.io/ubuntu-mate-welcome)
and the [Ubuntu Report](https://ubuntu.com/desktop/statistics).

We dropped Chinese, Japanese and Indic language packs from the ISO and added
Russian. This dropped the ISO size considerably and the savings gained were
just about equivalent to what the NVIDIA drivers require.

We are **currently shipping English, Spanish, Portuguese, German, French,
Italian and Russian language packs on the iso**, with each language including
all regional dialect variations. Anyone in other parts of the world will get
the language packs providing they have an Internet connection during the
install.

Other gains were made by:

  * Changing to format of the weather station database which saved 15MB 😱
  * Removing Qt4 components. [Qt4 is being removed from Debian and Ubuntu](https://wiki.debian.org/Qt4Removal).
  * Removing [fcitx](https://fcitx-im.org/wiki/Fcitx) from the Live environment.
  * Removing obsolete software from the ship-live seed.
  * Removed `usb-creator-gtk` from the default install. GNOME Disks provides image writing capabilities.
  * Reducing the size of Ubuntu MATE Welcome and Software Boutique snaps.
  * Using image optimisation tools on every graphic asset in the default themes, icon themes and wallpaper back-catalog.

**Had we not optimised the ISO image it would have been 2.5GB, but instead
it remains just a hair over 2.0GB while now hosting the NVIDIA drivers and 7
language packs**. So, while the Ubuntu MATE ISO image is larger than some,
a good chunk of that size is hosting drivers and language packs that will
probably never end up getting installed on your computer. The language
packs and drivers are there to best service our diverse community of users
from across the world 🗺️ running a variety of hardware 💻

## ZFS on root

{:.center}
![ZFS on Linux](/images/blog/eoan/zol-logo.png)

Support for ZFS as the root filesystem is added as an experimental feature in 19.10.
The ZFS file system and partitioning layout is handled automatically directly via the
installer.

You can read more details on Didier Roche's blogs:

  * [Part 1 - Ubuntu ZFS support in 19.10: introduction](https://didrocks.fr/2019/08/06/ubuntu-zfs-support-in-19.10-introduction/)
  * [Part 2 - Ubuntu ZFS support in 19.10: ZFS on root](https://didrocks.fr/2019/10/11/ubuntu-zfs-support-in-19.10-zfs-on-root/)

## GPD MicroPC & other UMPCs

Alongside the generic image for 64-bit Intel PCs, we're also releasing a
bespoke image for the [GPD MicroPC](https://www.gpd.hk/gpdmicropc) which
includes hardware specific tweaks to get this device working *"out of the box"*
without any faffing about. [See our UMPC page for more details](/ports/umpcs/).

{:.center}
![ZFS on Linux](/images/blog/eoan/zol-logo.png)

{% include embed/youtube.html
    embed = "https://www.youtube.com/embed/_-zm17qlLU4?html5=1&amp;rel=0&amp;showinfo=0"
%}

## Major Applications

Accompanying **MATE Desktop 1.22.2** and **Linux 5.3.0** are **Firefox 69.0.1**,
**GNOME MPV 0.16**, **LibreOffice 6.3.1.2** and **Evolution 3.34.0**.

{:.center}
![Major Applications](/images/blog/eoan/versions.png)

See the [Ubuntu 19.10 Release
Notes](https://wiki.ubuntu.com/EoanErmine/ReleaseNotes) for details of all
the changes and improvements in Ubuntu that Ubuntu MATE benefits from.


{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 19.10"
    text = "Our download page makes it easy to acquire the most suitable build for your hardware."
    button_text = "Download"
    button_url = "/download/"
%}



## Upgrading from Ubuntu MATE 19.04

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c` into the command box.
  * Update Manager should open up and tell you: New distribution release '19.10' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * [Caja dropbox does not start](https://bugs.launchpad.net/ubuntu/+source/caja-dropbox/+bug/1845876).
    * The `libdropbox_apex.so` shared object, as distributed by Dropbox, has the wrong file permissions.
    * See [How to fix `libdropbox_apex.so` problem with latest Dropbox?](https://askubuntu.com/questions/1177519/how-to-fix-libdropbox-apex-so-problem-with-latest-dropbox).
    * The workaround is to open a terminal and run the following command:

```
sudo chmod a+rx /var/lib/dropbox/.dropbox-dist/dropbox-lnx.x86_64-*/libdropbox_apex.so
```

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
