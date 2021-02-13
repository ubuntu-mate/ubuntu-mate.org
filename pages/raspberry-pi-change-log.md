---
layout: sidebar
permalink: /raspberry-pi/changelog/
lang: en
sidebar: raspberry-pi

title: Raspberry Pi Changes

---

# What's New for the Raspberry Pi?

{% include partials/toc.html %}

### 30 October 2020 - 20.04.1 & 20.10

  * Ubuntu MATE 20.10 is capable of USB boot.
  * Compute Module 4 support.
  * The `gpio`, `i2c`, `input` and `spi` groups are pre-created.
    * The user created using the first-boot wizard is automatically added to the groups above.
  * `cloud-init` is completely removed; file system expansion is handled by `cloud-initramfs-growroot` and the `x-systemd.growfs` mount option.
  * Snaps are initialized while the first-boot setup wizard runs.
  * Plymouth splash screen is displayed correctly during first-boot.
  * Serial console is disabled by default.
  * `gpu_mem` configured for 128MB by default.
  * `hdmi_drive` now defaults to DVI mode.

### 13 August 2020 - 20.04.1 Beta 2

  * Re-based on Ubuntu MATE 20.04.1.
  * Fixed WiFi on first boot during the initial setup wizard.
  * Dropped `gpu_mem` from `config.txt` as the defaults should be sensible.

### 12 July 2020 - 20.04 Beta 1

  * Re-based on Ubuntu MATE 20.04.
  * Added support for Raspberry Pi 4.
  * Enabled the VC4/V3D (fkms) driver by default.
  * Firefox uses Basic rendering by default.
    * Based on community feedback and our testing the OMTC (OpenGL) compositing video playback is choppy by comparison.
  * Added `rpi-eeprom`.
  * Minecraft: Pi Edition is still be packaged.
  * USB Booting is work in progress.
  * Dropped `raspi-config`; we have something else in the works...

### 06 April 2019 - 18.04.2 Beta 2

  * Added Raspberry Pi specific applications to the Software Boutique.
    * Minecraft: Pi Edition
    * Steam Link
  * Disabled WiFi Power Management.
  * `openssh-server` no longer pre-installed.

### 24 March 2019 - 18.04.2 Beta 1

  * Fixed EGL/GLES/OpenVG libraries for VideoCore IV.
  * Fixed Raspberry Pi features in Ubuntu MATE Welcome.
  * Added hardware accelerated VLC (`armhf` only).
  * Added hardware accelerated ffmpeg (`armhf` only).
  * Enabled piwheels.
  * Reduced boot time, after the initial first boot setup has been completed, by ~3 seconds.
  * Uploaded SteamLink (`armhf` only) to the archive, not pre-installed.
  * Uploaded Minecraft Pi Edition (`armhf` only) to the archive, not pre-installed.
  * Raspberry Pi 3 Model A+ confirmed working, *kind of*.

### 05 March 2019 - 18.04.2 Alpha 1

  * Fixed HDMI audio quality.
  * Fixed USB booting.
  * Fixed font caches.
  * Added pre-seeded snaps.
  * Added miscellaneous Raspberry Pi utilities.
  * Added EGL/GLES/OpenVG libraries for VideoCore IV.
  * Enabled splash screen.
  * Improved window manager responsiveness.
  * Reduced idle RAM consumption by ~30MB on arm64 and ~10MB on armhf.
  * Switched to the CFQ scheduler.

### 02 March 2019 - 18.04.2 Alpha 1

  * Initial Ubuntu MATE 18.04.2 images made available for private testing.

### 16 February 2017 - 16.04.2 Release for Raspbery Pi 2 and Raspberry Pi 3

  * Performance optimised.
    * Added automated first boot partition resizing.
    * Optimised partition offset calculations
    * Optimised filesystem features.
    * Disabled unnecessary services to reduce CPU cycles and RAM requirements.
  * Forked and adapted `raspi-config` to Ubuntu.
    * Added [pi-top](https://www.pi-top.com/) brightness and power-off support.
  * Backported MATE Desktop 1.16.1.
  * Backported BlueZ 5.41.
  * Backported `ffmpeg` 3.2 including Raspberry Pi hardware acceleration for MMAL decoding and OMX encoding.
  * Backported `i2c-tools` and `python-smbus` 3.1.2.
  * Updated `raspberrypi-firmware` to 1.20161215-1.
  * Updated `pi-bluetooth` to 0.1.2 including failsafe systemd units.
  * Updated `gpiozero` to 1.3.1. A simple API for controlling devices attached to the GPIO pins.
  * Updated `omxplayer` to 0.3.7-git20160923-dfea8c9.
  * Updated `nuscratch` to 20160915+2.
  * Updated `picamera` to 1.12. Pure Python interface to the Raspberry Pi's camera module.
  * Updated `pigpio` to 1.130. Library for Raspberry Pi GPIO control.
  * Updated `python-sense-hat` to 2.2.0. Sense HAT python.
  * Updated `raspberrypi-sys-mods` to 20170208, which completely replaces `raspberrypi-general-mods`
  * Updated `raspi-gpio` to 0.20170105. Dump the state of the BCM270x GPIOs.
  * Updated `rpi.gpio` to 0.6.3-1. Python GPIO module for Raspberry Pi.
  * Updated `rtimulib` to 7.2.1-3. Versatile C++ and Python 9-dof, 10-dof and 11-dof IMU library.
  * Updated `sonic-pi` to 2.10.0.
  * Updated `xserver-xorg-video-fbturbo` to 1.20161111~122359.
  * Updated Xorg via the [LTS Enablement Stack](https://wiki.ubuntu.com/Kernel/LTSEnablementStack).
  * Added cap1xxx; A python library designed to drive various Microchip CAP1xxx touch ICs.
  * Added drumhat; A python library designed to control Drum HAT.
  * Added envirophat; A python library designed to control Enviro pHAT.
  * Added explorerhat; A python library designed to control the Explorer HAT and pHAT.
  * Added microdotphat; A python library designed to control Micro Dot pHAT.
  * Added mote; A python library designed to control Mote.
  * Added motephat; A python library designed to control Mote pHAT.
  * Added pantilthat; A python library designed to control Pan-Tilt HAT.
  * Added pianohat; A python library designed to control Piano HAT.
  * Added piglow; A python library designed to drive Piglow.
  * Added rainbowhat; A python library designed to control Rainbow HAT.
  * Added scrollphat; A python library designed to control Scroll pHAT.
  * Added sense-emu; A client library for the Raspberry Pi Sense HAT emulator.
  * Added sn3218; A python library to help control the SN3218 18-channel PWM LED driver.
  * Added st7036; A python library to help control the ST7036 LCD driver.
  * Fixed first boot configuration. Ubiquity now prompts to join available WiFi networks.
    * [#1572793](https://bugs.launchpad.net/bugs/1572793)
  * Disabled SSH by default.
    * SSH can be enabled via `raspi-config` or creating a file named `ssh` in the `/boot` partition.
    * `sshguard` is also automatically enabled when you enable SSH.
  * Reduced the image size to 5GB, down from 8GB.

### 24 April 2016 - 16.04 Final Release for Raspbery Pi 2 and Raspberry Pi 3

  * Added OpemMAX IL hardware accelerated video playback to VLC.
    * To enable hardware accelerated video playback go to `Tools` -> `Preferences` -> `Video` and select `OpenMax IL`.
  * Added MMAL hardware accelerated video playback to ffmpeg.
    * To use hardware accelerated video playback with `ffplay` you must specify the `h264_mmal` codec - `ffplay -vcodec h264_mmal video.mp4`
  * Increased the minimum microSDHC card size to 8GB.
  * Removed tboplayer.

### 05 April 2016 - 16.04 Beta 2 for Raspberry Pi 2 and Raspberry Pi 3

  * Updated to Ubuntu MATE 16.04 including the new Welcome which comes with Raspberry Pi specific features.
  * Updated BlueZ 5.37 with patches to support the Raspberry Pi 3 integrated Bluetooth.
    * Ubuntu MATE 16.04 now supports the on-board Raspberry Pi 3 Bluetooth and Wifi.
  * Updated to Linux 4.1.19.
  * Updated to `raspberrypi-firmware` 1.20160315-1.
  * Updated to `omx-player` 0.3.7~git20160206~cb91001.
  * Updated to `wiringpi` 2.32.
  * Updated to `nuscratch` 20160115.
  * Updated to `sonic-pi` 2.9.0.
  * Migrated configuration tweaks to `raspberrypi-general-mods` and `raspberrypi-sys-mods`.
  * Experimental hardware accelerated OpenGL can be enabled, *if you know how* `;-)`

### 27 February 2016 - 15.10.3 for Raspberry Pi 2 and Raspberry Pi 3

  * Added support for Raspberry Pi 3 integrated Wifi.
  * Updated BlueZ 5.35 with patch to support the Raspberry Pi 3 integrated Bluetooth.
    * Support for the integrated Raspberry Pi 3 Bluetooth is not working but we hope to have an update that addresses this soon.

### 26 February 2016 - 15.10.2 for Raspberry Pi 2 and Raspberry Pi 3 (internal testing build)

  * Added support for Raspberry Pi 3 Model B.
    * No Raspberry Pi 3 integrated Wifi or Bluetooth support.
  * Updated to Linux 4.1.18.
  * Updated all packages to the current version in the Ubuntu 15.10 archive.
  * Fixed an issue where the SSH host keys were not correctly regenerated on first boot.

### 21 December 2015 - 15.10.1 for Raspberry Pi 2 Update

  * Migrated the build to [Ubuntu Pi Flavour Maker](https://ubuntu-pi-flavour-maker.org) project.
  * Images are now XZ compressed, to save bandwidth and make them compatible with GNOME Disks.
  * Added `python-gpiozero` and `python3-gpizero` 1.0.0 as packages.
  * Updated Scratch to 20151111.
  * Updated to Linux 4.1.15.
  * Reverted change to `/boot/config.txt` so audio is not forced to output over HDMI because this introduced more compatibility issues that it solved.

### 22 October 2015 - 15.10 for Raspberry Pi 2 Final Release

  * Added OMXPlayer GUI.
  * Added YouTube Downloader.
  * Added `fake-hwclock`.
  * Added `python-spidev` and `python3-spidev`.
  * Added `python-codebug-tether` and `python3-codebug-tether`.
  * Added `python-codebug-i2c-tether` and `python3-codebug-i2c-tether`.
  * Added file system integrity checking on first boot.
  * Optimised first run of MATE Menu.
  * Optimised LibreOffice icons.
  * Reinstated `oem-config`, which has been patched for the Raspberry Pi 2.
    * Now includes the Ubuntu MATE slideshow.
  * Fixed udev rules and groups for accessing `spi`.
  * Fixed Scratch, it now runs via a `sudo` wrapper.
    * Simliar to how Raspbian does it except *only* Scratch can be executed with elevated privileges, not everything.
  * Removed Compiz.

### 14 October 2015 - 15.10 for Raspberry Pi 2 Release Candidate

  * Fixed framebuffer so it now uses 32-bit colour depth.
  * Added Minecraft Pi Edition 0.1.1-4.
  * Added Scratch 20150916.
  * Added Sonic Pi 2.7.0-1.
  * Added essential Python 2.7.x and Python 3.4.x libraries.
  * Added `raspi-gpio`.
  * Added `python-rpi.gpio` and `python3-rpi.gpio`.
  * Added `python-serial` and `python3-serial`.
  * Added `python-picamera` and `python3-picamera`.
  * Added `python-sense-hat` and `python3-sense-hat`.
  * Added `python-astropi` and `python3-astropi`.
  * Added `python-pygame` and `python3-pygame`.
  * Added `udev` rules for `gpio`, `input`, `i2c`, `spi`, `vchiq`.
  * Added `/usr/local/sbin/adduser.local` hook to automatically add new users to the `adm`, `gpio`, `i2c`, `input`, `spi` and `video` groups.
  * Added `openssh-server` with first-boot host key regeneration.
  * Added `graphical` a utility to disable/enable the MATE desktop environment for easily creating a headless *"server"*.
  * Updated to Linux 4.1.10.
    * Now using the kernel, firmware and drivers from Raspberry Pi Foundation and includes `rpi-update` to easily update the kernel and firmware.
  * Updated `/boot/config.txt` so it is now fully documented.
  * Updated to `raspi-copies-and-fills` (high performance memcpy and memset) 0.5-1.
  * Updated to `xserver-xorg-video-fbturbo` (an accelerated x.org driver) 0~git.20151007.f9a6ed7.
  * Updated to `omx-player` 0.3.6~git20150912~d99bd86.
  * Updated `/boot/config.txt` so when HDMI is connected audio is sent over HDMI by default.
  * Enabled Plymouth to improve startup and shutdown performance.
  * Removed `oem-config`.

### 22 April 2015 - 15.04 for Raspberry Pi 2 Final Release

  * Enabled Ryan Finnie's PPA.
    * <https://launchpad.net/~fo0bar/+archive/ubuntu/rpi2>
    * Many thanks to Ryan for adding Vivid as a build target.
  * Changed from `cfq` to `deadline` I/O scheduler.
  * Added `xserver-xorg-video-fbturbo` (an accelerated x.org driver) 0~git.20150305.e094e3c-1.15.04.
    * Limited to hardware-accelerated window moving and scrolling.
  * Added `raspi-copies-and-fills` (high performance memcpy and memset) 0.4-1.
  * Added `oem-config` so first boot provides a setup wizard.
  * Added `rpi2-ubuntu-errata` for facilitating post-release updates/migrations.
  * Added sym-links to VideoCore utilties in `/opt/vc/` for 3rd party script compatibility.
  * Added `f2fs` support to the build script.
    * Pre-built images available for download use `ext4` because `f2fs` file systems can not be resized
    at present.
  * Updated to Linux 3.18.0-20.21.
  * Updated to `flash-kernel` 3.0~rc.4ubuntu54+rpi2.4.
  * Updated to `omxplayer` 0.3.6~git20150402~74aac37.
  * Updated to `raspberrypi-firmware-nokernel` 1.20150402.3ea439c-1.
  * Updated to `raspberrypi-vc` (VideoCore GPU libraries) 1.20150323.7650bcb-1.
  * Fixed `/etc/network/interfaces` so that the Ethernet device is now configurable via Network Manager.
  * Removed `openssh-server` until host key regeneration can be integrated.

### 22 April 2015 - 15.04 for Raspberry Pi 2 Beta 2

  * Enabled `systemd` as the init system.
  * Added `raspberrypi-vc` (VideoCore GPU libraries) 1.20150301.0de0b20-3.
  * Added `omxplayer` 0.3.6~git20150217~5337be8.
  * Added `linux-firmware`.
  * Added `openssh-server`.

### 07 March 2015

  * Initial Release.
