---
layout: page-category
permalink: /umpcs/
lang: en

title: Ultra Mobile PCs

---

# Ubuntu MATE for Ultra Mobile PCs

The Ubuntu MATE team offers a bespoke images for the
[GPD Pocket](https://gpd.hk/gpdpocket),
[GPD Pocket 2](https://gpd.hk/gpdpocket2),
[GPD Pocket 3](https://gpd.hk/gpdpocket3),
[GPD WIN 2](https://gpd.hk/gdpwin2),
[GPD MicroPC](https://gpd.hk/gpdmicropc),
[GPD P2 Max](https://www.gpd.hk/gpdp2max),
[GPD WIN Max](https://gpd.hk/gpdwinmax) and
[Topjoy Falcon](https://www.kickstarter.com/projects/440069565/falcon-worlds-first-8-inch-2-in-1-laptop)
that include the hardware specific tweaks to get these devices working
*"out of the box"* without any faffing about. Some models of the OneMix
Yoga devices are also supported.

Ultra Mobile PCs (UMPC) have had something of a resurgence in recent years
thanks to very successful crowd funding campaigns for netbook style laptops
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
    * While holding down the **centre track point button** on the MicroPC & Pocket 3.
  * Enable double size console (tty) font resolution for high resolution devices.
  * Enable **fractional scaling** for 1920x1200 displays.
    * Results in an effective resolution of 1280x800 to make the display panels easily readable.
    * Simple to toggle on/off if you want to restore full resolution.
  * **GRUB is usable post-install**.
    * GPD Pocket, WIN 2, MicroPC & TopJoy Falcon GRUB is rotated 90 degrees, but functional.
    * GPD Pocket 2 and GPD P2 Max GRUB is correctly rotated and functional.
  * GPD Pocket BRMC4356 WiFi firmware enabled by default.
  * GPD Pocket fan control kernel module enabled by default.
  * GPD Pocket 3 & TopJoy Falcon **accelerometer support for automatic screen rotation**.
  * GPD WIN Max features a custom, persistent, EDID.

## Known Issues

### GPD Pocket, GPD Pocket 3, WIN 2, MicroPC, WIN Max and Topjoy Falcon

  * The GRUB menu is rotated 90 degrees on the GPD Pocket, MicroPC and Topjoy Falcon.
    * The workaround is to tilt your head.
  * The built in speaker in the GPD Pocket is mono and doesn't play audio from the right channel.
    * The workaround is to use headphones connected the 3.5mm audio jack.

### GPD Pocket 2

  * The boot menu is not displayed in the GPD Pocket 2 live media.
    * The workaround is to wait and the system will boot after a few seconds or press <kbd>Enter</kbd> to boot immediately.
    * However, **GRUB is fully functional and usable post-install**.

### GPD Pocket 3

  * When a HDMI display is connected, the touch coordinates on the internal display are incorrect.

### GPD Pocket 3, GPD WIN 2, GPD WIN Max & Topjoy Falcon

  * The Plymouth splash screen is not correctly orientated; and for the GPD WIN Max incorrectly coloured.
    * The workaround is to not care.

{% include blog/jumbotron.html

    title = "Download"
    text = "Run Ubuntu MATE on your GPD hardware or Topjoy Falcon today!"
    button_text = "Download"
    button_url = "/download/"

%}

## How were these images created?

With a script called `umpc-ubuntu-respin.sh` which you can find in the
following GitHub repository:

  * <https://github.com/wimpysworld/umpc-ubuntu>

## Accessing boot menus & BIOS

Switch the device on, immediately hold/tap the corresponding key(s).

|      Device      |      BIOS    |  Boot  Menu  |
|   -------------  | ------------ | ------------ |
| GPD Pocket       | `Fn` + `F7`  | `Fn` + `F7`  |
| GPD Pocket 2     | `Fn` + `F12` | `Fn` + `F12` |
| GPD Pocket 3     | `Fn` + `F7`  | `Fn` + `F7`  |
| GPD WIN 2(!)     |    `Del`     |    `Del`     |
| GPD MicroPC      | `Fn` + `F7`  | `Fn` + `F7`  |
| GPD P2 Max       | `Fn` + `F7`  | `Fn` + `F7`  |
| GPD WIN Max      |     `F7`     |     `F7`     |
| OneMix Yoga 2    | `Fn` + `F7`  | `Fn` + `F7`  |
| TopJoy Falcon    | `Fn` + `F2`  | `Fn` + `F12` |

  * **GPD WIN 2(!)**: Navigate to *Save & Exit* and choose the storage device you want to boot from under *Boot Override*

## Feedback

These images for the GPD and Topjoy devices are community supported,
please post all feedback via the [community forum](https://ubuntu-mate.community/).
