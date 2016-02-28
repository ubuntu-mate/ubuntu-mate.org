<!--
.. title: Ubuntu MATE for the Raspberry Pi 2
.. slug: raspberry-pi
.. date: 2015-04-21 23:01:09 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,download,armhf
.. link: https://ubuntu-mate.community/t/ubuntu-mate-15-04-for-raspberry-pi-2/517
.. description: Ubuntu MATE 15.10 for the Raspberry Pi 2
.. type: text
.. author: Martin Wimpress
-->

Martin Wimpress and Rohith Madhavan have made an Ubuntu MATE image
for the Raspberry Pi 2 which you can download or build yourself.

The image is functional and based on the regular Ubuntu `armhf` base,
not the new Snappy Core, which means that the installation procedure for
applications is the same as that for the regular desktop version, ie using
`apt-get`.

We have done what we can to optimise the build for the Raspberry Pi 2
and one can comfortably use applications such as LibreOffice, which in
fact is a joy to use :-) But the microSDHC I/O throughput is a
bottleneck so **we recommend that you use a Class 6 or Class 10 microSDHC**
card. If you build the image yourself we recommend you use the `f2fs`
filesystem.

You'll need a microSD card which is 4GB or greater to fit the image.
The file system can be resized to occupy the unallocated space of the
microSD card, similar to Raspbian.

**NOTE! There are no predefined user accounts**. The first time you
boot the Ubuntu MATE image it will run through a setup wizard where you
can create your own user account and configure your regional settings.
The first boot is quite slow, but once the first boot configuration is
complete subsequent boots are much quicker.

<div align="center">
  <img src="/gallery/Screenshots/09_RASPBERRY.png" /></a><br />
  <b>Ubuntu MATE 15.10 running on the Raspberry Pi 2.</b>
</div>
<br />

<div class="bs-component">
    <div class="jumbotron">
        <h1>Release announcement</h1>
        <p>Find out what changed in Ubuntu MATE 15.10</p>
        <a href="/blog/ubuntu-mate-wily-final-release/" class="btn btn-primary btn-lg">Release announcement</a>
        </p>
    </div>
</div>

## Download

A pre-built image of Ubuntu MATE 15.10.1 for the Raspberry Pi 2 is
available via BitTorrent and direct download. If you can spare the
bytes, please download via BitTorrent and leave the client open after
your download is finished, so you can seed it back to others. <i>A
web-seed capable client is recommended for fastest download
speeds.</i></p>

Many thanks to [First Colo](http://www.first-colo.com) for contributing the
hosting and bandwidth for the Ubuntu MATE downloads.

<div class="row">
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.org/raspberry-pi/ubuntu-mate-15.10.1-desktop-armhf-raspberry-pi-2.img.xz.torrent">
        <img src="/assets/img/misc/torrent.png" alt="Ubuntu MATE 15.10.1 Raspberry Pi 2 Torrent" title="Ubuntu MATE 15.10.1 Raspberry Pi 2 Torrent" />
      </a>
      <p>Ubuntu MATE 15.10.1 via BitTorrent</p><p><b>Raspberry Pi 2</b></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.r.worldssl.net/raspberry-pi/ubuntu-mate-15.10.1-desktop-armhf-raspberry-pi-2.img.xz">
        <img src="/images/flags/European-Union-Flag-128.png" alt="Ubuntu MATE 15.10.1 Raspberry Pi 2 Download" title="Ubuntu MATE 15.10.1 Raspberry Pi 2 Download" />
      </a>
      <p>Ubuntu MATE 15.10.1 from European CDN</p><p><b>Raspberry Pi 2</b></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://can.ubuntu-mate.net/raspberry-pi/ubuntu-mate-15.10.1-desktop-armhf-raspberry-pi-2.img.xz">
        <img src="/images/flags/Canada-Flag-128.png" alt="Ubuntu MATE 15.10.1 Raspberry Pi 2 Download" title="Ubuntu MATE 15.10.1 Raspberry Pi 2 Download" />
      </a>
      <p>Ubuntu MATE 15.10.1 from Canadian mirror</p><p><b>Raspberry Pi 2</b></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://fra.ubuntu-mate.net/raspberry-pi/ubuntu-mate-15.10.1-desktop-armhf-raspberry-pi-2.img.xz">
        <img src="/images/flags/France-Flag-128.png" alt="Ubuntu MATE 15.10.1 Raspberry Pi 2 Download" title="Ubuntu MATE 15.10.1 Raspberry Pi 2 Download" />
      </a>
      <p>Ubuntu MATE 15.10.1 from French mirror</p><p><b>Raspberry Pi 2</b></p>
    </div>
  </div>
</div>

If you direct download the image please make sure the MD5 hash matches:

  * `61287c1881b166c05b89a8cdc39e12b5`

## Download tip

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">
If everyone who downloaded Ubuntu MATE donated **$2.50** it would
fund the full-time development of Ubuntu MATE *and* MATE
Desktop. <u>Please give us a tip and help both projects flourish!</u> If
you'd [like to donate more or become an Ubuntu MATE patron](/donate/)
please visit the [donate page](/donate/).</p>

<div class="row">
  <div class="col-lg-3">
    <div class="well bs-component" align="center">
      <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
        <fieldset>
          <button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button>
        </fieldset>
        <input type="hidden" name="cmd" value="_xclick">
        <input type="hidden" name="business" value="6282B4CZGVCB6">
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 Raspberry Pi 2 Download Tip">
        <input type="hidden" name="no_shipping" value="1">
        <input type="hidden" name="no_note" value="1">
        <input type="hidden" name="charset" value="UTF-8">
        <input type="hidden" name="amount" value="2.50">
        <input type="hidden" name="currency_code" value="USD">
        <input type="hidden" name="src" value="1">
        <input type="hidden" name="sra" value="1">
        <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">
        <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
      </form>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component" align="center">
      <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
        <fieldset>
            <button type="submit" class="btn btn-primary">Tip us <b>$5.00</b></button>
        </fieldset>
        <input type="hidden" name="cmd" value="_xclick">
        <input type="hidden" name="business" value="6282B4CZGVCB6">
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 Raspberry Pi 2 Download Tip">
        <input type="hidden" name="no_shipping" value="1">
        <input type="hidden" name="no_note" value="1">
        <input type="hidden" name="charset" value="UTF-8">
        <input type="hidden" name="amount" value="5.00">
        <input type="hidden" name="currency_code" value="USD">
        <input type="hidden" name="src" value="1">
        <input type="hidden" name="sra" value="1">
        <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">
        <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
      </form>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component" align="center">
      <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
        <fieldset>
          <button type="submit" class="btn btn-primary">Tip us <b>$10.00</b></button>
        </fieldset>
        <input type="hidden" name="cmd" value="_xclick">
        <input type="hidden" name="business" value="6282B4CZGVCB6">
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 Raspberry Pi 2 Download Tip">
        <input type="hidden" name="no_shipping" value="1">
        <input type="hidden" name="no_note" value="1">
        <input type="hidden" name="charset" value="UTF-8">
        <input type="hidden" name="amount" value="10.00">
        <input type="hidden" name="currency_code" value="USD">
        <input type="hidden" name="src" value="1">
        <input type="hidden" name="sra" value="1">
        <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">
        <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
      </form>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component" align="center">
      <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
        <fieldset>
          <button type="submit" class="btn btn-primary">Tip us <b>$20.00</b></button>
        </fieldset>
        <input type="hidden" name="cmd" value="_xclick">
        <input type="hidden" name="business" value="6282B4CZGVCB6">
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 Raspberry Pi 2 Download Tip">
        <input type="hidden" name="no_shipping" value="1">
        <input type="hidden" name="no_note" value="1">
        <input type="hidden" name="charset" value="UTF-8">
        <input type="hidden" name="amount" value="20.00">
        <input type="hidden" name="currency_code" value="USD">
        <input type="hidden" name="src" value="1">
        <input type="hidden" name="sra" value="1">
        <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">
        <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
      </form>
    </div>
  </div>
</div>

## Making a microSDHC

The image can be directly written to a microSDHC using a utility like
`dd`, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue), for example:

    sudo apt-get install gddrescue xz-utils
    unxz ubuntu-minimal-15.10.1-server-armhf-raspberry-pi-2.img.xz
    sudo ddrescue -D --force ubuntu-minimal-15.10.1-server-armhf-raspberry-pi-2.img /dev/sdx

The microSDHC may be presented on any `/dev/sdX` so use the command
`lsblk` to check.

<div align="center">
<script type="text/javascript" src="https://asciinema.org/a/34243.js" id="asciicast-34243" async></script>
</div>

If you prefer a graphical tool we recommend using [GNOME Disks](apt://gnome-disk-utility)
and the *Restore Disk Image...* option, **which natively supports XZ
compressed images**.

    sudo apt-get install gnome-disk-utility

<div align="center">
<iframe width="640" height="480" src="https://www.youtube.com/embed/V_6GNyL6Dac?html5=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>

### Making a microSDHC with Windows

If you want to make a microSDHC using Windows we recommend:

  * [7-Zip](http://www.7-zip.org/) to extract the image.
  * [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) to write the image.

## Re-size file system

There are no utilities included for automatic file system re-sizing. However,
it's not hard to do manually. Once booted:

    sudo fdisk /dev/mmcblk0

Delete the second partition (d, 2), then re-create it using the defaults
(n, p, 2, enter, enter), then write and exit (w). Reboot the system, then:

    sudo resize2fs /dev/mmcblk0p2

## Enable and Disable X11

We created a simple utility called `graphical` to disable/enable the
MATE desktop environment for easily creating a headless *"server"*.
Executing `graphical disable` will present a console login on the next
boot, with no X11 or associated services running. If you want to get
the full Ubuntu MATE desktop back, run `graphical enable` and reboot.

## Hardware accelerated video

Most videos will play with hardware acceleration using `omxplayer` which
is pre-installed in Ubuntu MATE. However if you have MPEG-2 or VC-1 video
video files then **you will need MPEG-2 and/or VC-1 licenses from the
[Raspberry Pi Store](http://www.raspberrypi.com/license-keys/)**.

### Redirecting audio output

You can select which audio device `omxplayer` should output audio to.

#### For HDMI

    omxplayer -o hdmi video.mp4

#### For 3.5mm audio jack

    omxplayer -o local video.mp4

The sound will output to HDMI by default if both HDMI and the 3.5mm audio jack
are connected. You can, however, force the system to output to a particular
device using `amixer`.

#### For HDMI

    sudo amixer cset numid=3 2

#### For 3.5mm audio jack

    sudo amixer cset numid=3 1

## Feedback and Improvements

Please post all feedback on the [dedicated community topic](https://ubuntu-mate.community/t/ubuntu-mate-15-10-for-the-raspberry-pi-2/2479).
If you have any improvements then please submit a pull request to our
BitBucket.

  * <https://bitbucket.org/ubuntu-mate/ubuntu-mate-rpi2>

## Credits

  * [Rohith Madhavan](http://rohithmadhavan.com) - Made the Ubuntu MATE 15.04 image.
  * [Martin Wimpress](https://flexion.org) - Added first boot setup wizard and architecture optimisations.
  * [Ryan Finnie](http://finnie.org) - Raspberry Pi 2 Kernel, Firmware and video driver packages.
  * [Sjoerd Simons](http://sjoerd.luon.net) - Made the initial Raspberry Pi 2 kernel patches for Debian Jessie.
  * [Sergio Conde](http://omxplayer.sconde.net/) - Maintains `omxplayer` for the Raspberry Pi.
  * [Spindle](https://github.com/RPi-Distro/spindle) - a tool to help spin distribution images

## Changes

### 2015-12-21 - Ubuntu MATE 15.10.1 for Raspbery Pi 2 Update

  * Migrated the build to [Ubuntu Pi Flavour Maker](https://ubuntu-pi-flavour-maker.org) project.
  * Images are now XZ compressed, to save bandwidth and make them compatible with GNOME Disks.
  * Added `python-gpiozero` and `python3-gpizero` 1.0.0 as packages.
  * Updated Scratch to 20151111.
  * Updated to Linux 4.1.15.
  * Reverted change to `/boot/config.txt` so audio is not forced to output over HDMI because this introduced more compatibility issues that it solved.

### 2015-10-22 - Ubuntu MATE 15.10 for Raspbery Pi 2 Final Release

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

### 2015-10-14 - Ubuntu MATE 15.10 for Raspbery Pi 2 Release Candidate

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

### 2015-04-22 - Ubuntu MATE 15.04 for Rapsberry Pi 2 Final Release

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

### 2015-04-22 - Ubuntu MATE 15.04 for Rapsberry Pi 2 Beta 2

  * Enabled `systemd` as the init system.
  * Added `raspberrypi-vc` (VideoCore GPU libraries) 1.20150301.0de0b20-3.
  * Added `omxplayer` 0.3.6~git20150217~5337be8.
  * Added `linux-firmware`.
  * Added `openssh-server`.

### 2015-03-07

  * Initial Release.

## TODO

  * Add `raspi-config` or equivilent.
  * Add automatic reszing of the root file system.

## Other ARMv7 based devices

We'd love to see Ubuntu MATE images other ARMv7 based devices. Please take
a look at our generic armhf Ubuntu MATE root file system and build scripts.

  * [Ubuntu MATE generic rootfs for aarch32 ARMv7 devices](https://ubuntu-mate.org/armhf-rootfs)
  * [Ubuntu MATE for Raspberry Pi 2 build scripts](https://bitbucket.org/ubuntu-mate/ubuntu-mate-armhf)

## Reporting issues

Please report any issues you may find on the project's bug tracker.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Getting involved

Is there anything you can help with or want to be involved in? Maybe
you just want to discuss your experiences or ask the maintainers some
questions. Please [come and talk to us](/community/).

## References

  * <https://wiki.ubuntu.com/ARM/RaspberryPi>
  * <http://omxplayer.sconde.net/>
  * <https://github.com/bavison/arm-mem/>
    * <https://www.raspberrypi.org/forums/viewtopic.php?t=47832&p=403191>
  * <https://www.raspberrypi.org/documentation/configuration/config-txt.md>
  * [Peter Chubb. "SD cards and filesystems for embedded systems". Linux.conf.au.](http://mirror.linux.org.au/pub/linux.conf.au/2015/Case_Room_2/Friday/SD_Cards_and_filesystems_for_Embedded_Systems.webm)

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
