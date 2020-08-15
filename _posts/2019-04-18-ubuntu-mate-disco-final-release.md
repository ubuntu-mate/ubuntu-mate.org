---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-disco-final-release/
description: Ubuntu MATE 19.04 (Disco Dingo) Final Release
category: release
author: Martin Wimpress
lang: en
discourse_topic_id: 21342

title: Ubuntu MATE 19.04 Final Release

---

**Ubuntu MATE 19.04 is a modest upgrade over previous releases. If you want bug
fixes and improved hardware support, *particularly for NVIDIA GPU owners*, then
19.04 is for you. Oh yeah, we've also made [bespoke Ubuntu MATE 19.04 images for
the GPD Pocket and GPD Pocket 2](/ports/umpcs/). Read on to learn more...**


{:.center}
![Ubuntu MATE 19.04](/images/blog/1904-final.png)
**Ubuntu MATE 19.04 with the Mutiny layout**

## What changed since the Ubuntu MATE 18.10 final release?

Those of you who follow the desktop Linux news will know that
upstream [MATE Desktop recently released version 1.22](https://mate-desktop.org/blog/2019-03-18-mate-1-22-released/).

Let's rip that band-aid off and get this over quickly. Ubuntu MATE 19.04
is shipping with MATE Desktop 1.20. Albeit, the latest maintenance release of
MATE Desktop 1.20 with some of the bug fixes and new features from MATE
Desktop 1.22 included. In fact, the version of MATE Desktop being shipped in
19.04 is derived from the same MATE packages that will feature in the upcoming
[Debian 10 (Buster)](https://wiki.debian.org/DebianBuster) release.

You may be wondering why we're not shipping MATE Desktop 1.22?
The answer, stability. MATE Desktop 1.22 introduces some underlying API
changes in core components and while all first party MATE Desktop
applications are compatible with the changes and completely stable, some
third party applications are not. Some third party applications are big
crashers now and we've not been able to fix them in time.

So, we are playing it safe and sticking with MATE Desktop 1.20 and working
with upstreams so we can land MATE Desktop 1.22 early in the Ubuntu MATE
19.10 development cycle.

### NVIDIA Drivers

During the Ubuntu 18.10 development cycle the Linux kernel, firmware,
Mesa and Vulkan were all updated to ensure we offered the best possible
support for sipping AMD GPUs. During the 19.04 cycle AMD support has
been uplifted again but we have also improved the *"out of box"* experience
for NVIDIA GPU owners too.

If you have an NVIDIA GPU connected to your computer and select
*Install third-party software for graphics and Wi-Fi hardware* during
installation, the NVIDIA proprietary drivers will be installed.

{:.center}
![Third party drivers](/images/blog/disco/select-third-party-drivers.png)

Post install, the proprietary NVIDIA drivers are installed and configured. To
confirm this, open a terminal and run `nvidia-smi`. Ubuntu MATE users with
laptops that support hybrid graphics will see the MATE Optimus hybrid graphics
applet displaying the NVIDIA logo.

{:.center}
![MATE Optimus - hybrid graphics switcher](/images/blog/disco/mate-optimus-indicator.png)


### MATE Dock Applet

[MATE Dock Applet](https://github.com/robint99/mate-dock-applet) has been
updated to 0.88 which introduces some new visual options, based on
the look of the Unity desktop. As seen in the screenshot at the start of this
post, this has been used in the Mutiny layout to further mimic Unity 7.

### Remote Desktop Awareness

Our MATE Desktop 1.20 packages ship with patches to support
[Remote Desktop Awareness (RDA)](https://github.com/ArcticaProject/librda). RDA
makes MATE Desktop more aware of its execution context so that it behaves
differently when run inside a remote desktop session compared to when running
on local hardware. Different remote technology solutions support different
features and they can now be queried from within MATE components. The inclusion
of RDA offers the option to suspend your remote connection; supports folder
sharing in Caja; MIME type bindings for SSHFS shares and allows session suspension
via the MATE screensaver.

### GPD Pocket

Alongside the generic image for 64-bit Intel PCs, we're also releasing bespoke
images for the [GPD Pocket](https://www.gpd.hk/gpdpocket) and
[GPD Pocket 2](https://www.gpd.hk/gpdpocket2). These include hardware
specific tweaks to get these devices working *"out of the box"*
without any faffing about. [See our GPD Pocket page for more details](/ports/umpcs/).

## Major Applications

Accompanying **MATE Desktop 1.20.4** and **Linux 5.0.0** are **Firefox
66.0.3**, **VLC 3.0.6**, **LibreOffice 6.2.2.2** and **Thunderbird 60.6.1**.

{:.center}
![Major Applications](/images/blog/disco/versions.png)

See the [Ubuntu 19.04 Release
Notes](https://wiki.ubuntu.com/DiscoDingo/ReleaseNotes) for details of all
the changes and improvements in Ubuntu that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 19.04"
    text = "Our download page makes it easy to acquire the most suitable build for your hardware."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 18.04 or 18.10

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c` into the command box.
  * Update Manager should open up and tell you: New distribution release '19.04' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

## Known Issues

Here are the known issues.

### Ubuntu MATE

  * Nothing significant.

### Ubuntu family issues

This is our known list of bugs that affects all flavours.

  * When [selecting third-party drivers during install causes a long pause before the install proceeds](https://pad.lv/1824905).
    * This is the `ubuntu-drivers` tool refreshing it's cache. Please wait a couple of minutes and the install will continue normally.
  * [Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)
    * To work around this, run `apt install oem-config-slideshow-ubuntu-mate` in the OEM prepare session.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
