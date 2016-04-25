<!--
.. title: Ubuntu MATE for the Raspberry Pi 2 and Raspberry Pi 3
.. slug: raspberry-pi-change-log
.. date: 2016-04-07 19:09:27 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,Raspberry Pi 2,Raspberry Pi 3,download,armhf,arm64,ARMv7,ARMv8
.. link:
.. description: Ubuntu MATE 16.04 for the Raspberry Pi 2 and Raspbery Pi 3
.. type: text
.. author: Martin Wimpress
-->

# What's New for the Raspberry Pi 2 and 3?

[Back to Raspberry Pi page](/raspberry-pi/)

### 2016-04-24 - 16.04 Final Release for Raspbery Pi 2 and Raspberry Pi 3

  * Added OpemMAX IL hardware accelerated video playback to VLC.
    * To enable hardware accelerated video playback go to `Tools` -> `Preferences` -> `Video` and select `OpenMax IL`.
  * Added MMAL hardware accelerated video playback to ffmpeg.
    * To use hardware accelerated video playback with `ffplay` you must specify the `h264_mmal` codec - `ffplay -vcodec h264_mmal video.mp4`
  * Increased the minimum microSDHC card size to 8GB.
  * Removed tboplayer.

### 2016-04-05 - 16.04 Beta 2 for Raspberry Pi 2 and Raspberry Pi 3

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

### 2016-02-27 - 15.10.3 for Raspberry Pi 2 and Raspberry Pi 3

  * Added support for Raspberry Pi 3 integrated Wifi.
  * Updated BlueZ 5.35 with patch to support the Raspberry Pi 3 integrated Bluetooth.
    * Support for the integrated Raspberry Pi 3 Bluetooth is not working but we hope to have an update that addresses this soon.

### 2016-02-26 - 15.10.2 for Raspberry Pi 2 and Raspberry Pi 3 (internal testing build)

  * Added support for Raspberry Pi 3 Model B.
    * No Raspberry Pi 3 integrated Wifi or Bluetooth support.
  * Updated to Linux 4.1.18.
  * Updated all packages to the current version in the Ubuntu 15.10 archive.
  * Fixed an issue where the SSH host keys were not correctly regenerated on first boot.

### 2015-12-21 - 15.10.1 for Raspberry Pi 2 Update

  * Migrated the build to [Ubuntu Pi Flavour Maker](https://ubuntu-pi-flavour-maker.org) project.
  * Images are now XZ compressed, to save bandwidth and make them compatible with GNOME Disks.
  * Added `python-gpiozero` and `python3-gpizero` 1.0.0 as packages.
  * Updated Scratch to 20151111.
  * Updated to Linux 4.1.15.
  * Reverted change to `/boot/config.txt` so audio is not forced to output over HDMI because this introduced more compatibility issues that it solved.

### 2015-10-22 - 15.10 for Raspberry Pi 2 Final Release

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

### 2015-10-14 - 15.10 for Raspberry Pi 2 Release Candidate

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

### 2015-04-22 - 15.04 for Raspberry Pi 2 Final Release

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

### 2015-04-22 - 15.04 for Raspberry Pi 2 Beta 2

  * Enabled `systemd` as the init system.
  * Added `raspberrypi-vc` (VideoCore GPU libraries) 1.20150301.0de0b20-3.
  * Added `omxplayer` 0.3.6~git20150217~5337be8.
  * Added `linux-firmware`.
  * Added `openssh-server`.

### 2015-03-07

  * Initial Release.

<script>
  // http://netnix.org/2014/04/27/tracking-downloads-with-google-analytics/
  window.onload = function() {
    var a = document.getElementsByTagName('a');
    for (i = 0; i < a.length; i++) {
      if (a[i].href.match(/^https?:\/\/.+\.(bz2|deb|gz|iso|pdf|torrent|xz|zip)$/i)) {
        a[i].setAttribute('target', '_blank');
        a[i].onclick = function() {
          ga('send', 'event', 'Downloads', 'Click', this.getAttribute('href'));
        };
      }
    }
  }
</script>
