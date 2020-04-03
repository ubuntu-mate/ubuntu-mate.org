---
layout: blog-post
class: blog
title: Ubuntu MATE 20.04 Release Notes
permalink: /blog/ubuntu-mate-focal-fossa-release-notes/
description: Ubuntu MATE 20.04 (Focal Fossa)
category: dev                                   # release
author: Martin Wimpress & franksmcb
lang: en
discourse_topic_id: 21380
---

We are preparing Ubuntu MATE 20.04 (Focal Fossa) for distribution on
[April 23rd, 2020](https://wiki.ubuntu.com/FocalFossa/ReleaseSchedule).
With this *Beta* pre-release, you can see what we are trying out in
preparation for our next (stable) version.


{:.center}
![Ubuntu MATE 20.04 Desktop](/images/blog/focal/focal-fossa-desktop.png)
**Ubuntu MATE 20.04 - Welcome now offers a few buckets of paint!**


## Ubuntu Testing Week

{:.center}
![Ubuntu MATE with its family of flavours](/images/history/join-family.svg)


The **Ubuntu MATE** team is proud to be a part of **Ubuntu Testing Week** which
starts today (2 April) **until 8 April** along with the other flavours of the
Ubuntu family. Please join us in testing the beta of Ubuntu MATE 20.04
(Focal Fossa) as well sharing the :green_heart: by testing out some of the other flavours.

Unsure of how to test? [Alan Pope](http://popey.com/), the co-founder of Ubuntu
MATE, has made an outstanding video showing how easy it is to do.

{% include embed/youtube.html
    embed = "https://www.youtube.com/embed/hXLiqjOkSmg"
%}

If you need some help, [join us in our beta testing thread](https://ubuntu-mate.community/t/ubuntu-mate-20-04-beta-testing/21369/).
Did you find a :bug:? We've got a
[helpful guide](https://ubuntu-mate.community/t/how-to-report-problems-in-ubuntu-mate/17943)
on how to report it.

There are many way ways of testing. A spare machine, a secondary hard drive,
a live USB, or using a VM (Virtual Machine). If you are planning on using a VM,
you may be interested in trying [quickemu](https://github.com/wimpysworld/quickemu)
which allows you to easily manage QEMU VM's with a shell script.

We hope you will join in and help us make Ubuntu MATE 20.04 and all of it's
family a success :tada:


## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Beta Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who requires a stable system
  * Anyone uncomfortable running a system that can often be broken
  * Anyone in a production environment with data or workflows that need reliability

Ubuntu MATE *Beta Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE, and GTK+ developers



## What changed since the Ubuntu MATE 18.04 LTS and 19.10?

Those of you who follow the desktop Linux news will know that
upstream [MATE Desktop recently released version 1.24](https://mate-desktop.org/blog/2020-02-10-mate-1-24-released/).

Ubuntu MATE 20.04 is shipping with MATE Desktop 1.24.

Thus, all of the improvements in MATE Desktop 1.24 will be present in Ubuntu
MATE 20.04.

**Since the last LTS we worked on the following**:

  * Added *experimental* ZFS :file_folder: install option.
  * Fixed rendering window controls on HiDPI :mag: displays.
  * Fixed irregular icon sizes :straight_ruler: in MATE Control Center and made them render nicely on HiDPI displays.
  * Fixed unresponsive Caja :file_folder: extensions.
  * Fixed `mate-power-manager` :electric_plug: to use upower-glib `get_devices2()`.
  * Fixed unresponsive Pluma :notebook: plugins.
  * Fixed a crasher :bomb: in MATE Dock Applet due to an Attribute error in `adjust_minimise_pos()`.
  * Fixed auto-start errors in `mate-session-manager`.
  * Gave Ubuntu MATE Welcome a fresh coat of :paintbrush:.
  * Updated the Ubuntu MATE Guide  :question:
  * Updated the Ubiquity Slideshow :performing_arts:

## Firmware updater

We've add a GTK front end for `fwupd` This application can:

  * Upgrade, Downgrade, & Reinstall firmware on devices supported by `fwupd`.
  * Unlock locked fwupd devices
  * Verify firmware on supported devices
  * Display all releases for a `fwupd` device

{:.center}
![Firmware](/images/blog/focal/firmware.png)
**Ubuntu MATE 20.04 - Features an LVFS compatible Firmware management utility**

### Window Manager improvements

Marco is the Window Manager for MATE Desktop and in Ubuntu MATE 20.04
it brings a number of new features and fixes.

**XPresent support is properly fixed**, which means that **screen tearing is now
a thing of the past** and **invisible window corners are finally here!** Invisible
window corners mean that windows can be easily resized :straight_ruler: without having to
precisely grab the window corners. **HiDPI rendering improvements** fix a number
of rendering problems that were present in various themes and components.
**Most notably, windows controls are now HIDPI aware**.

  * Magnus (see below) provides screen magnification
  * Marco supports invisible windows borders
  * Marco has improved Alt+Tab behaviour
  * Marco is free from screen tearing
  * Marco frame performance when gaming is further improved

**Minimized Application Preview**

Minimized applications in the window list now present a thumbnail preview.

{:.center}
![Minimized Preview](/images/blog/focal/taskbar-preview.png)

**Alt+Tab navigation** makes it possible to
traverse the application switcher via keyboard and mouse.
<kbd>Alt</kbd> + <kbd>Tab</kbd>.

{:.center}
![Alt-Tab Switcher](/images/blog/focal/alt-tab.png)

**Workspace Switcher** allows you to switch between workspaces using a the keyboard and mouse.
<kbd>Alt</kbd> + <kbd>Tab</kbd> + <kbd>Ctrl</kbd>.

{:.center}
![Workspace Switcher](/images/blog/focal/workspace-switcher.png)

**Compiz and Compton have been removed from the default Ubuntu MATE
install**. The fundamental reasons for including them no longer exist.

Only having one window manager to target means we can promptly deliver new
features and minimise development effort. Which brings us to...

### New Key-bindings

The key-bindings for window tiling have only worked on full keyboards :keyboard: with a
10-key pad. Few laptops :computer: have a 10-key pad and not all keyboards have a
10-key either. There are some well known key-bindings from other platforms that
were not recognised in Ubuntu MATE. So, we've had a think :think: and have come up with this:

  * **Maximise Window:** <kbd>Super</kbd> + <kbd>Up</kbd>
  * **Restore Window:** <kbd>Super</kbd> + <kbd>Down</kbd>
  * **Title Window right:** <kbd>Super</kbd> + <kbd>Right</kbd>
  * **Title Window left:** <kbd>Super</kbd> + <kbd>Left</kbd>
  * **Center Window:** <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>c</kbd>
  * **Title Window to upper right corner:** <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Right</kbd>
  * **Title Window to upper left corner:** <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Left</kbd>
  * **Title Window to lower right corner:** <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Right</kbd>
  * **Title Window to lower left Corner:** <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>Super</kbd> + <kbd>Left</kbd>
  * **Shade Window:** <kbd>Control</kbd> + <kbd>Alt</kbd> + <kbd>s</kbd>

It is now possible to tile a window to
all screen quadrants :triangular_ruler: using any keyboard form factor.

We updated the application launcher key-bindings, some of these have existed
in Ubuntu MATE for a while:

  * **Cycle external displays:** <kbd>Super</kbd> + <kbd>P</kbd>
  * **Lock Screen:** <kbd>Super</kbd> + <kbd>L</kbd>
  * **Screenshot a rectangle:** <kbd>Shift</kbd> + <kbd>PrintScr</kbd>
  * **Open File Manager:** <kbd>Super</kbd> + <kbd>e</kbd>
  * **Open Terminal:** <kbd>Super</kbd> + <kbd>T</kbd>
  * **Open Control Center:** <kbd>Super</kbd> + <kbd>I</kbd>
  * **Open Search:** <kbd>Super</kbd> + <kbd>S</kbd>
  * **Open Task Manager:** <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>Escape</kbd>
  * **Open System Information:** <kbd>Super</kbd> + <kbd>Pause</kbd>

The key-bindings compliment existing well established alternatives. So if
<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> (Terminal) and
<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd> (Lock Screen) are ingrained in
your muscle :muscle: memory 🧠 they are still available too. You can find all the
keyboard shortcuts documented in the **Getting Started section of Ubuntu MATE
Welcome**.

### Brisk Menu

[Brisk Menu](https://github.com/getsolus/brisk-menu) is under the Solus GitHub
organisation, but it's been a couple of years since it had a new release. The
Solus Project gave me administrative access :trident: to the Brisk Menu repo and I've
made a new release. Thanks to the efforts of a couple of Ubuntu MATE
contributors, several bug :bug: fixes have landed too, which includes **resolving
frequent crashers in Brisk Menu, preventing a scrollbar always appearing
in the category column** of the menu and **silencing sounds firing as you
rollover menu entries**.

### MATE Panel

MATE Panel has had a long-standing bug fixed that caused it to crash :boom: when
the panel was reset or replaced. This was most noticeable when switching panel
layouts via MATE Tweak and could result in the panel layout being left
incomplete or entirely absent. This bug is now fixed! MATE Tweak has been
updated to neatly integrate with with fixed MATE Panel behaviour so that **layout
switching is now 100% reliable**.

### Indicators

A bug which resulted in **oversized icons in indicators is finally resolved**.

{:.center .transparent}
| ![Before](/images/blog/eoan/indicators-before.png) | ![After](/images/blog/eoan/indicators-after.png)
| **Before** :poop: | **After** :heart_eyes:

However, it turned out some of the bugs were due to the icons :art: themselves.
Over :100: icons have been refactored :paintbrush:️ to correct their resolutions or aspect
ratio; as a result the panel and indicators both scale correctly.

A race condition that could result in **two network status icons being
displayed is fixed**, and **when connected via VPN, lock icons are now
overlayed on the Network Indicator**. The battery :battery: indicator is improved
and now has a larger **charging symbol while charging**.

We've **added the Date/Time Indicator and integrated it with MATE Desktop
and it now replaces the MATE clock applet** which corrects the placement of
the clock and session indicators.

We've finally addressed a long standing issue which has been around since
Ubuntu MATE 14.10 🕸️: some of the monochrome symbolic icons used in the
indicators were also used in applications. The presented a couple of issues:

  * In certain cases, you couldn't easily see the icons against the window base colour.
  * The mix of monochrome and full colour icons in applications looked inconsistent.

This issue is now resolved; **monochrome symbolic icons are only used for
indicators and full colour icons are used in the Control Center, Sound
Preferences, Bluetooth, OSD, etc**.

### MATE Window Applets

[MATE Window Applets](https://github.com/ubuntu-mate/mate-window-applets)
have received a number of bug fixes and new features from a community
contributor. Window control icons now dynamically load from the currently
selected theme, rather than requiring manual user configuration.
**A number of bugs (including significant memory leaks) have also been
resolved**.

## Notification Center

Ubuntu MATE 20.04 includes a **new Indicator that provides a "notification
center"** :bell: We worked with the [upstream developer to add new features
to indicator-notifications](https://github.com/trism/indicator-notifications)
and integrate it with MATE Notifications Daemon.

{:.center}
![Notification Settings](/images/blog/eoan/notification-settings.png)

We now have a **notification center that also offers a "do not disturb" :red_circle:
feature**. When do not disturb is enabled, notifications will be muted and captured in the notification center for review. It's also
**possible to blacklist some notifications**, so they are never stored by the
notification center. I've created an icon theme for the notification center so
it fits the look and feel of the default Ubuntu MATE theme. **Notification hints
are also fixed** so any notifications supplying additional media, such as
sounds or icons, now work.

## Evolution replaces Thunderbird

The Ubuntu MATE development team discussed the pros and cons of switching the
default mail :email: client in Ubuntu MATE to
[Evolution](https://wiki.gnome.org/Apps/Evolution). Here is a summary of our
assessment:

  * Thunderbird does not integrate as well with the desktop.
    * For example, theme integration, font integration, compatibility with HUD (which is increasingly difficult to support in Thunderbird), notifications with action buttons, locale and spell checking.
  * Evolution integrates well with MATE Desktop given that both use GTK3.
  * **Evolution includes interoperability with LibreOffice**, for which Ubuntu MATE is already shipping the required components.
  * Evolution has superior **integration with Google Mail and Exchange**, including calendar, contacts, tasks, and memos.

**Indicator Date/Time also integrates with Evolution**. It is fully functional,
including all the features of creating new events or opening upcoming events from the
indicator. Clicking on an individual day in the month displays the events for that day, etc.

{:.center}
![Indicator Date Time](/images/blog/eoan/indicator-datetime.png)

For the many people who use web-mail exclusively, this change will have no
impact, but for those who use desktop mail we feel these productivity :chart_with_upwards_trend:
improvements are significant.

For those of you who love :two_hearts: Thunderbird and wish to continue using it, we will
continue to offer Thunderbird in the Software Boutique for a one-click install.
Likewise, Evolution is now in the Software Boutique, and can be installed/removed
with one click.

## Magnus

Most desktop environments are lacking a screen magnifier, which is an essential
application for visually impaired :eyeglasses: computer users, as well as accurate
graphical design or detail work. One of the reasons we ship Compiz in Ubuntu
MATE is because it has an excellent screen magnifier and was our solution for
people who need magnification :mag:

{:.center}
![Magnus for zooming into the screen](/images/blog/eoan/magnus.png)

Martin and [Stuart Langridge](https://twitter.com/sil) collaborated
to create [Magnus](https://kryogenix.org/code/magnus/); **a very simple
desktop magnifier**, showing the area around the mouse pointer in a separate
window magnified two, three, four, or five times. Magnus is now shipped :ship:
by default in Ubuntu MATE 20.04.

## Ubuntu MATE Themes

Dozens of theme-related bugs have been fixed. The Ubuntu MATE themes have
been added to the `gtk-common-themes` used by snaps, **so snapped applications
are now themed correctly for Ubuntu MATE users**. This change is already
available all the way back to Ubuntu MATE 16.04.

The most noticeable resolved theme issues are **sensibly sized expanders in tree
view** (they were so tiny) that are easily clickable,
**window controls are correctly proportioned on CSD windows** and we've add a
splash of Chelsea Cucumber :bug: to the Ubuntu MATE logo on the menu. Everything
the QA team highlighted has been fixed :hammer:

## MATE Tweak and Ubuntu MATE Welcome

MATE Tweak now **preserves user preferences when switching between custom
layouts** thanks to a community contribution.

If you're familiar with MATE Tweak, you'll know it can switch panel layouts
to somewhat mimic other platforms and distros 🐧 We have now integrated a
graphical layout switcher in Ubuntu MATE Welcome to better promote the feature
and make it more accessible. We have actually had this feature since 18.04, but
the bugs in MATE Panel I mentioned earlier meant it didn't work. With all the
associated panel bugs fixed :wrench: we now have this:

{:.center}
![Desktop Layout Switcher](/images/blog/eoan/desktop-layout.png)

## NVIDIA drivers

If you've been following the news surrounding Ubuntu you'll know that
Ubuntu will be shipping :ship: the NVIDIA proprietary drivers on the ISO images.
Anyone selecting the additional 3rd party hardware drivers during installation
without an Internet connection will have the drivers available in offline
scenarios.

Post-install, Ubuntu MATE users with computers that support hybrid graphics
will see the MATE Optimus hybrid graphics applet displaying the NVIDIA logo.

{:.center}
![MATE Optimus](/images/blog/eoan/mate-optimus-19.10.1.png)

We have given MATE Optimus an update. MATE Optimus adds support for NVIDIA On-Demand
and will now prompt users to log out when switching the GPU's profile. MATE, XFCE, Budgie,
Cinnamon, GNOME, KDE and LXQt are all supported. Wrappers, called `offload-glx`
& `offload-vulkan`, can be used to easily offload games/apps to the PRIME
renderer. **I'm also delighted to see Ubuntu Budgie 20.04 are shipping MATE
Optimus too!**

The **NVIDIA drivers are now going to receive updates via the official
Ubuntu software repository**. So no need to add a PPA to get updates and more
importantly, **the NVIDIA drivers are signed (which is not supported for
drivers distributed via PPA) so you can keep Secure Boot enabled.**


### Remote Desktop Awareness

Our MATE Desktop 1.24 packages ship support for
[Remote Desktop Awareness (RDA)](https://github.com/ArcticaProject/librda). RDA
makes MATE Desktop more aware of its execution context, so it behaves
differently when run inside a remote desktop session compared to when running
on local hardware. Different remote technology solutions support different
features and they can now be queried from within MATE components. The inclusion
of RDA offers the option to suspend your remote connection, supports folder
sharing in Caja and MIME type bindings for SSHFS shares, and allows session suspension
via the MATE screensaver.

## ZFS on root

{:.center}
![ZFS on Linux](/images/blog/eoan/zol-logo.png)

Support for ZFS as the root filesystem is added as an experimental feature in 20.04.
The ZFS file system and partitioning layout is handled automatically directly via the
installer.

You can read more details on Didier Roche's blogs:

  * [Part 1 - Ubuntu ZFS support in 19.10: introduction](https://didrocks.fr/2019/08/06/ubuntu-zfs-support-in-19.10-introduction/)
  * [Part 2 - Ubuntu ZFS support in 19.10: ZFS on root](https://didrocks.fr/2019/10/11/ubuntu-zfs-support-in-19.10-zfs-on-root/)


{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 20.04 Beta"
    text = "Notice anything different? We've overhauled the website to make things easier to discover!"
    button_text = "Download"
    button_url = "/download/amd64/focal/"
%}


## Known Issues

Here are the known issues.

### Ubuntu MATE

 * [Xorg crashes to Login prompt in VirtualMachines](https://bugs.launchpad.net/ubuntu/+source/xorg-server/+bug/1745345)
     * `gstreamer-vaapi` when installed, will cause xorg to crash and bring the user back to the login prompt when running certain applications.
     * See [Workaround for Xorg crashes to Login prompt in VirtualMachines 20.04](https://ubuntu-mate.community/t/workaround-for-xorg-crashes-to-login-prompt-in-virtualmachines-20-04/21368/2)

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
