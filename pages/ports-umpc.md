---
layout: page-category
permalink: /ports/umpcs/
lang: en
category: ports

title: Ultra Mobile PCs

---

# Ubuntu MATE for Ultra Mobile PCs

The Ubuntu MATE team offers a bespoke images for the
[GPD Pocket](https://www.gpd.hk/gpdpocket),
[GPD Pocket 2](https://www.gpd.hk/gpdpocket2),
[GPD WIN 2](https://www.gpd.hk/gdpwin2),
[GPD MicroPC](https://www.gpd.hk/gpdmicropc) and
[Topjoy Falcon](https://www.kickstarter.com/projects/440069565/falcon-worlds-first-8-inch-2-in-1-laptop)
that include the hardware specific tweaks to get these devices working
*"out of the box"* without any faffing about. Some models of the OneMix
Yoga devices are also supported.

Ultra Mobile PCs (UMPC) have had something of a resurgence in recent years
thanks to very successfull crowd funding campaigns for netbook style laptops
featuring a high resolution touch displays housed in an aluminium alloy
body. These scripts for UMPC devices are based on the excellent work by
[Hans de Goede](https://hansdegoede.livejournal.com/), [nexus511](https://apt.nexus511.net/),
[stockmind](https://github.com/stockmind/gpd-pocket-ubuntu-respin) and many
others.


{:.center .small}
![Ubuntu MATE running on the GPD Pocket (left) and GPD Pocket 2 (right)](/images/blog/gpd-pockets.jpg)
**Ubuntu MATE running on the GPD Pocket (left) and GPD Pocket 2 (right)**


## What works

The Ubuntu MATE images for the UMPCs adds the following tweaks:

  * Enable **frame buffer and Xorg display rotation**.
    * Supports `modesetting` *and* `xorg-video-intel` display drivers.
  * Enable **TearFree rendering by default**.
  * Enable touch screen rotation for Xorg and Wayland.
  * Enable **scroll wheel emulation** for Xorg.
    * While holding down the **right track point button** on the Pocket, Pocket 2 & Topjoy Falcon.
    * While holding down the **centre track point button** on the MicroPC.
  * Enable double size console (tty) font resolution.
  * Enable **resolution scaling** for 1920x1200 displays. *(MATE Desktop only)*
    * Results in an effective resolution of 1280x800 to make the small display panels easily readable.
    * Simple to disable if you want to restore full resolution.
  * **GRUB is usable post-install**.
    * GPD Pocket, WIN 2, MicroPC & TopJoy Falcon GRUB is rotated 90 degress, but functional.
    * GPD Pocket 2 GRUB is correctly rotated and functional.
  * GPD Pocket BRMC4356 WiFi firmware enabled by default.
  * GPD Pocket fan control kernel module enable by default.

## Known Issues

### GPD Pocket, WIN 2, MicroPC and Topjoy Falcon

  * The GRUB2 menu is rotated 90 degress on the GPD Pocket, MicroPC and Topjoy Falcon.
    * The workaround is to tilt your head.
  * The built in speaker in the GPD Pocket is mono and doesn't play audio from the right channel.
    * The workaround is to use headphones connected the 3.5mm audio jack.

### GPD Pocket 2

  * The boot menu is not displayed in the GPD Pocket 2 live media.
    * The workaround is to wait and the system will boot after a few seconds or press <kbd>Enter</kbd> to boot immeditately.
    * However, **GRUB is fully functional and usable post-install**.

### GPD Pocket, Pocket 2 & MicroPC, Topjoy Falcon

  * The Plymouth splash screen is not rotated.
    * The workaround is to not care.


{% include blog/jumbotron.html

    title = "Download"
    text = "Run Ubuntu MATE on your GPD Pocket, GPD Pocket 2, GPD WIN 2, GPD MicroPC or Topjoy Falcon today!"
    button_text = "Download"
    button_url = "/download/"

%}


## Disable desktop session scaling

If you want to restore the full native resolution of display then open
*Startup Applications* from the *Control Center*. Find the entry called
*GPD Pocket Display Scaler* in the *Startup Programs* tab and untick it.
Log out and back in and the full 1920x1200 resolution is restored.


{:.center}
![Disabling the UMPC Pocket Display Scaler via Startup Applications Preferences](/images/blog/gpd-pocket-display-scaler.png)
**Disabling the UMPC Pocket Display Scaler via Startup Applications Preferences**


## How were these images created?

With a script called `umpc-ubuntu-respin.sh` which you can find in the
following GitHub repository:

  * <https://github.com/wimpysworld/umpc-ubuntu>

## Accessing UMPC boot menus

### GPD Pocket, GPD MicroPC, OneMix Yoga 2

Switch the device on, immediately hold the <kbd>Fn</kbd> key and tap the <kbd>F7</kbd> key until the Boot Manager screen appears.

### GPD Pocket 2 & Topjoy Falcon

Switch the device on, immediately hold the <kbd>Fn</kbd> key and tap the <kbd>F12</kbd> key until the Boot Manager screen appears.

## Accessing UMPC BIOS menus

### Topjoy Falcon

Switch the device on, immediately hold the <kbd>Fn</kbd> key and tap the <kbd>F2</kbd> key until the BIOS appears.

## Feedback

These images for the GPD and Topjoy devices are community supported,
please post all feedback via the [community forum](https://ubuntu-mate.community/).
