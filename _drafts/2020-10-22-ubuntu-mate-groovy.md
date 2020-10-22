---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-groovy-gorilla-release-notes/
category: release
author: Monica Madon & Martin Wimpress
lang: en
discourse_topic_id: 22888

title: Ubuntu MATE 20.10 Release Notes
description: What's new in Ubuntu MATE 20.10 (Groovy Gorilla)

---

The releases following an LTS are always a good time ⌚ to make changes the set
the future direction 🗺️ of the distribution with an eye on where we want to be for
the next LTS release. Therefore, Ubuntu MATE 20.10 ships with that latest MATE
Desktop 1.24.1, keeps paces with other developments within Ubuntu (such as
Active Directory authentication) and migrated to the Ayatana Indicators project.

If you want bug fixes :bug:, kernel updates :corn:, a new web camera control :movie_camera:,
and a new indicator :point_right: experience, then 20.10 is for you :tada:. Ubuntu MATE 20.10
will be supported for 9 months until July 2021. If you need Long Term
Support, we recommend you use [Ubuntu MATE 20.04 LTS](website!)

Read on to learn more... :point_down:

{:.center}
![Ubuntu MATE 20.10 (Groovy Gorilla)](/images/blog/groovy/groovy-gorilla-desktop.png)
**Ubuntu MATE 20.10 (Groovy Gorilla)**

## What's changed since Ubuntu MATE 20.04?

### MATE Desktop

If you follow the [Ubuntu MATE twitter account](https://twitter.com/ubuntu_mate) 🐦
you'll know that MATE Desktop 1.24.1 was recently released. Naturally Ubuntu
MATE 20.10 features that maintenance release of MATE Desktop. In addition, [we
have prepared updated MATE Desktop 1.24.1 packages for Ubuntu MATE 20.04](https://pad.lv/1891891)
that are currently in the SRU process. Given the number of MATE packages being
updated in 20.04, it might take some time ⏳ for all the updates to land, but
we're hopeful that the fixes and improvements from MATE Desktop 1.24.1 will
soon be available for those of you running 20.04 LTS 👍

### Active Directory

The Ubuntu Desktop team added the option to enroll your computer into an
Active Directory domain 🔑 during install. We've been tracking that work and the
same capability is available in Ubuntu MATE too.

{:.center}
![Active Directory Enrollment](/images/blog/groovy/active-directory.png)
**Enroll your computer into an Active Directory domain**

### Ayatana Indicators

There is a significant under the hood change 🔧 in Ubuntu MATE 20.10 that you
might not even notice 👀 at a surface level; we've replaced Ubuntu Indicators
with [Ayatana Indicators](https://github.com/AyatanaIndicators).

We'll explain some of the background, why we've made this change, the short
term impact and the long term benefits.

#### What are Ayatana Indicators?

In short, Ayatana Indicators is a fork of Ubuntu Indicators that aims to be
cross-distro compatible and re-usable for any desktop environment 👌 Indicators
were developed by Canonical some years ago, initially for the GNOME2
implementation in Ubuntu and then refined for use in the Unity desktop. Ubuntu
MATE has supported the Ubuntu Indicators for some years now and we've contributed
patches to integrate MATE support into the suite of Ubuntu Indicators. Existing
indicators are compatible with Ayatana Indicators.

We have migrated Ubuntu MATE 20.10 to Ayatana Indicators and Arctica Greeter. I
live streamed 📡 the development work to switch from Ubuntu Indicators to
Ayatana Indicators which you can find below if you're interested in some of the
technical details 🤓

{% include embed/youtube.html
    embed = "https://www.youtube.com/embed/4ICRjjjMbEE?html5=1&amp;rel=0&amp;showinfo=0"
%}

#### The benefits of Ayatana Indicators

Ubuntu MATE 20.10 is our first release to feature Ayatana Indicators and as
such there are a couple of drawbacks; there is no messages indicator and no
graphical tool to configure the display manager greeter (login window) 😞

Both will return in a future release and the greeter can be configured
using `dconf-editor` in the meantime.

{:.center}
![Arctica Greeter dconf configuration](/images/blog/groovy/arctica-greeter-dconf.png)
**Configuring Arctica Greeter with `dconf-editor`**

That said, there are significant benefits that result from migrating to Ayatana
Indicators:

  * Debian and Ubuntu MATE are now aligned with regards to Indicator support; patches are no longer required in Ubuntu MATE which reduces the maintenance overhead.
  * [MATE Tweak](https://github.com/ubuntu-mate/mate-tweak) is now a cross-distro application, without the need for distro specific patches.
  * We've switched from [Slick Greeter](https://github.com/linuxmint/slick-greeter) to [Arctica Greeter](https://github.com/ArcticaProject/arctica-greeter) (both forks of Unity Greeter)
    * Arctica Greeter integrates completely with Ayatana Indicators; so there is now a consistent Indicator experience in the greeter and desktop environment.
  * Multiple projects are now using Ayatana Indicators, including desktop environments, distros and even mobile phone projects such as [UBports](https://ubports.com/). With more developers collaborating in one place we are seeing the collection of available indicators grow 📈
  * Through UBports contributions to Ayatana Indicators we will soon have a Bluetooth indicator that can replace Blueman, providing a much simpler way to connect and manage Bluetooth devices. UBports have also been working on a network indicator and we hope to consolidate that to provide improved network management as well.
  * Other indicators that are being worked on include printers, accessibility, keyboard (long absent from Ubuntu MATE), webmail and display.

So, that is the backstory about how developers from different projects come together to collaborate on a shared interest and improve software for their users 💪

### Webcamoid

We've replaced Cheese :cheese: with Webcamoid :movie_camera: as the default webcam tool for
several reasons.

  * Webcamoid is a full webcam/capture configuration tool with recording, overlays and more, unlike Cheese. While there were initial concerns :pensive:, since
Webcamoid is a Qt5 app, nearly all the requirements in the image are pulled in via YouTube-DL :tada:.
  * We've disabled notifications :bell: for Webcamoid updates if installed from universe pocket as a deb-version, since this would cause errors in the  user's system and force them to download a non-deb version. This only affects users who don't have an existing Webcamoid configuration.

### Linux Kernel

Ubuntu MATE 20.10 includes the 5.8 Linux kernel. This includes numerous
updates and added support since the 5.4 Linux kernel released in
Ubuntu 20.04 LTS. Some notable examples include:

* Airtime Queue limits for better WiFi connection quality
* Btrfs RAID1 with 3 and 4 copies and more checksum alternatives
* USB 4 (Thunderbolt 3 protocol) support added
* X86 Enable 5-level paging support by default
* Intel Gen11 (Ice Lake) and Gen12 (Tiger Lake) graphics support
* Initial support for AMD Family 19h (Zen 3)
* Thermal pressure tracking for systems for better task placement wrt CPU core
* XFS online repair
* OverlayFS pairing with VirtIO-FS
* General Notification Queue for key/keyring notification, mount changes, etc.
* Active State Power Management (ASPM) for improved power savings of PCIe-to-PCI devices
* Initial support for POWER10

## Raspberry Pi images

We have been preparing Ubuntu MATE 20.04 images for the Raspberry Pi and
we will be release final image for 20.04 and 20.10 in the coming days 🙂

## Major Applications

Accompanying **MATE Desktop 1.24.1** and **Linux 5.8** are **Firefox
81**, **LibreOffice 7.0.2**, **Evolution 3.38** & **Celluloid 0.18**.

{:.center}
![Major Applications](/images/blog/groovy/versions.png)

See the [Ubuntu 20.10 Release Notes](https://discourse.ubuntu.com/t/groovy-gorilla-release-notes/15533)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 20.10"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 20.04 LTS

You can upgrade to Ubuntu MATE 20.10 from Ubuntu MATE 20.04 LTS. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" drop down menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c -d` into the command box.
  * Update Manager should open up and tell you: New distribution release 'XX.XX' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.


## Known Issues

Here are the known issues.

{% include partials/known-issues.html filter="20.10" %}


## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
