<!--
.. title: Ubuntu MATE for Raspberry Pi 3
.. slug: ubuntu-mate-for-raspberry-pi-3
.. date: 2016-02-28 06:00:00 UTC
.. tags: Ubuntu,Raspberry Pi,Raspberry Pi 2,Raspberry Pi 3,Server,Ubuntu MATE,Lubuntu,Xubuntu,15.10,Released
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

The Raspberry Pi 3 Model B is here and we are delighted to announce the
**immediate availbility of Ubuntu MATE 15.10 for the Raspberry Pi
3 Model B**!

Many thanks to [Ben
Nuttall](https://twitter.com/ben_nuttall), Simon West, [Liz
Upton](https://twitter.com/liz_upton) and [Phil
Elwell](https://github.com/pelwell) from the [Raspberry Pi
Foundation](https://www.raspberrypi.org/) for providing [Martin
Wimpress](https://twitter.com/m_wimpress) with a Raspberry Pi 3 and
engineering assistance over the weekend.

<div align="center">
  <img src="/images/logos/ubuntu-mate-flavour-maker-pi3.png" alt="Ubuntu MATE for the Raspberry Pi 3" title="Ubuntu MATE for the Raspberry Pi 3" />
</div>

The Raspberry Pi 3 Model B is the same form factor as the Raspberry Pi
B+ and Raspberry Pi 2 Model B, the RAM remains 1GB and the USB and
wired Ethernet port arrangement and configuration are unchanged.

Here is what is new to the Raspberry Pi 3:

  * Improved performance thanks to a **64-bit ARMv8-A Quad Core 1.2GHz CPU**
  * **Integrated WiFi** (BCM43438 ) accessed via SDIO using the Arasan MMC controller.
    * This requires that the Broadcom MMC controller is used for the SD card using the relatively new and recently revamped `bcm2835-sdhost` driver.
  * **Integrated Bluetooth LE** (BCM43438 again) is presented as a modem via a serial UART (two-wire - no hardware flow control) with the BlueZ software stack running in H4 mode.
  * Improved power management.

The Ubuntu MATE image we've prepared supports the integrated Wifi on the
Raspberry Pi 3, *but support for the integrated Raspberry Pi 3 Bluetooth
is still in progress and we hope to enable full support via an update
very soon*.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download</h1>
        <p>Download Ubuntu MATE for the Raspberry Pi 2 Model B and Raspberry Pi 3 Model B</p>
        <a href="/raspberry-pi/" class="btn btn-primary btn-lg">Download</a>
    </div>
</div>

The image will fit on a 4GB (or larger) microSHDC card, is
pre-configured to enable access to Raspberry Pi 2 and Raspberry Pi 3
hardware devices such as GPIO, SPI, I2C, etc and include replacement
`memcpy` and `memset` functionality for the Raspberry Pi to optimise
performance. We have done what we can to optimise the builds for the
Raspberry Pi 2 and Raspberry Pi 3 but microSDHC I/O throughput can be a
bottleneck so we recommend that you **use a Class 6 or Class 10
microSDHC card**.

The image is built from the regular Ubuntu armhf base, not the new
[Snappy Ubuntu](https://developer.ubuntu.com/en/snappy/), which means
that the installation procedure for applications is the same as that for
the regular desktop versions, ie using `apt-get`. **The images will only
work in a Raspberry Pi 2 Model B and Raspberry Pi 3 Model B**

The first time you boot one of the desktop images it will run through a
setup wizard where you can create your own user account and configure
your regional settings. The first boot is quite slow, but once the first
boot configuration is complete subsequent boots are much quicker.

## Changes

These are the changes that we've made since the 15.10.1 release.

### 2016-02-27 - 15.10.3 for Raspbery Pi 2 and Raspberry Pi 3

  * Added support for Raspberry Pi 3 integrated Wifi.
  * Updated BlueZ 5.35 with patch to support the Raspberry Pi 3 integrated Bluetooth.
    * Support for the integrated Raspberry Pi 3 Bluetooth is not working, but we hope to have an update that addresses this soon.

### 2016-02-26 - 15.10.2 for Raspbery Pi 2 and Raspberry Pi 3 (internal testing build)

  * Added support for Raspberry Pi 3 Model B.
    * No Raspberry Pi 3 integrated Wifi or Bluetooth support.
  * Updated to Linux 4.1.18.
  * Updated all packages to the current version in the Ubuntu 15.10 archive.
  * Fixed an issue where the SSH host keys were correctly regenerated on first boot.