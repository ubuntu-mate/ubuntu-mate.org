<!--
.. title: Ubuntu MATE for the Raspberry Pi 2 and Raspberry Pi 3
.. slug: raspberry-pi
.. date: 2015-04-21 23:01:09 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,Raspberry Pi 2,Raspberry Pi 3,download,armhf,arm64,ARMv7,ARMv8
.. link:
.. description: Ubuntu MATE 16.04 for the Raspberry Pi 2 and Raspbery Pi 3
.. type: text
.. author: Martin Wimpress
-->

Martin Wimpress and Rohith Madhavan have made an Ubuntu MATE image for
the Raspberry Pi 2 and Raspberry Pi 3 which you can download or build
yourself.

The image is based on the regular Ubuntu `armhf` base, not the new Snappy 
Core, which means that the installation procedure for applications is the same 
as that for the regular desktop version, ie using `apt-get`. However, since 
Ubuntu MATE 16.04 snap packages can be installed alongside classic deb 
packages.

We have done what we can to optimise the build for the Raspberry Pi 2 and 
Raspberry Pi 3, you can comfortably use applications such as LibreOffice, 
which in fact is a joy to use :-) But the microSDHC I/O throughput is a 
bottleneck so **we *highly* recommend that you use a Class 6 or Class 10 
microSDHC** card. **Ubuntu MATE 16.04 also has fully working Bluetooth and 
Wifi on the Raspberry Pi 3**

You'll need a microSD card which is **8GB** or greater to fit the image. The 
file system can be resized to occupy the unallocated space of the microSD 
card, **on Ubuntu MATE 16.04 this can be done via Ubuntu MATE Welcome**.

**NOTE! There are no predefined user accounts**. The first time you
boot one of the desktop images it will run through a setup wizard where
you can create your own user account and configure your regional
settings. The first boot is quite slow but, once the first boot
configuration is complete, subsequent boots are much quicker.

<div align="center">
  <img src="/gallery/Screenshots/09_RASPBERRY.png" /></a><br />
  <b>Ubuntu MATE 16.04 running on the Raspberry Pi 3.</b>
</div>
<br />

<div class="bs-component">
    <div class="jumbotron">
        <h1>Release announcement</h1>
        <p>Find out what changed in Ubuntu MATE 16.04</p>
        <a href="/blog/ubuntu-mate-xenial-final-release/" class="btn btn-primary btn-lg">Release announcement</a>
        </p>
    </div>
</div>

## Known Issues

  * During first boot configuration Ubiquity does not prompt to join available WiFi networks.
    * [#1572793](https://bugs.launchpad.net/bugs/1572793)
  * Upon completion of the first boot setup WiFi doesn't work, at all. Reboot and WiFi will be available.
    * [#1572956](https://bugs.launchpad.net/bugs/1572956)

Both these issues will be addressed in Ubuntu MATE 16.04.1 for Raspberry Pi 2 
and 3 which is due in late July.

## Download

Pre-built images of Ubuntu MATE 16.04 for the Raspberry Pi 2 and Raspberry Pi 
3 are available via BitTorrent and direct download. If you can spare the 
bytes, please download via BitTorrent and leave the client open after your 
download is finished, so you can seed it back to others. *A web-seed capable 
client is recommended for fastest download speeds.*

Many thanks to [First Colo](http://www.first-colo.com) for contributing the
hosting and bandwidth for the Ubuntu MATE downloads.

<div class="row">
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.org/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz.torrent">
        <img src="/assets/img/misc/torrent.png" alt="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Torrent" title="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Torrent" />
      </a>
      <p>Ubuntu MATE 16.04 via BitTorrent</p><p><b>Raspberry Pi 2 and Raspberry Pi 3</b></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.r.worldssl.net/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz">
        <img src="/images/flags/European-Union-Flag-128.png" alt="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download" title="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download" />
      </a>
      <p>Ubuntu MATE 16.04 from European CDN</p><p><b>Raspberry Pi 2 and Raspberry Pi 3</b></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://can.ubuntu-mate.net/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz">
        <img src="/images/flags/Canada-Flag-128.png" alt="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download" title="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download" />
      </a>
      <p>Ubuntu MATE 16.04 from Canadian mirror</p><p><b>Raspberry Pi 2 and Raspberry Pi 3</b></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://fra.ubuntu-mate.net/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz">
        <img src="/images/flags/France-Flag-128.png" alt="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download" title="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download" />
      </a>
      <p>Ubuntu MATE 16.04 from French mirror</p><p><b>Raspberry Pi 2 and Raspberry Pi 3</b></p>
    </div>
  </div>
</div>

If you direct download the image please make sure the SHA256 hash matches:

  * Ubuntu MATE 16.04: `bf7c85d0a25c8f27313a4bc47d4ceb32a9082390b18651af247d9757abebd21a`

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
        <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download Tip">
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
        <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download Tip">
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
        <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download Tip">
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
        <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 Raspberry Pi 2 and 3 Download Tip">
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
    unxz ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz
    sudo ddrescue -D --force ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img /dev/sdx

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

### Ubuntu MATE 16.04

You can use Ubuntu MATE Welcome to resize to automatically resize the
partitions to make full use of your microSHDC card capacity. Simply
click the large **Raspberry Pi Information** button on the Welcome
screen, click the **Resize** button and then restart the Raspberry Pi.

### Manual Method

It's not hard to do manually. Once booted:

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

## Hardware accelerated video with omxplayer

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

## Hardware accelerated video with VLC and ffmpeg

Ubuntu MATE 16.04 added OpemMAX IL hardware accelerated video playback to VLC 
and MMAL hardware accelerated video playback to ffmpeg.

  * To enable hardware accelerated video playback in VLC go to `Tools` -> `Preferences` -> `Video` and select `OpenMax IL`.
  * To use hardware accelerated video playback with `ffplay` you must specify the `h264_mmal` codec

    `ffplay -vcodec h264_mmal video.mp4`

Hardware accelerated playback on the Raspberry Pi works by overlaying the 
video directly to the screen. Therefore there are no onscreen controls for 
playback control. You'll need to use the VLC and ffmpeg keyboard shortcuts.

  * [VLC keyboard control](https://wiki.videolan.org/Hotkeys_table/)
  * [ffplay keyboard controls](https://ffmpeg.org/ffplay.html#toc-While-playing)

## Feedback and Improvements

Please post all feedback on the [dedicated community 
forum](https://ubuntu-mate.community/c/support/raspberry-pi-2). If you have 
any improvements then please submit a pull request to the [Ubuntu Pi Flavour 
Maker project](https://ubuntu-pi-flavour-maker.org/).

## Credits

  * [Rohith Madhavan](http://rohithmadhavan.com) - Made the Ubuntu MATE 15.04 image for the Raspberry Pi 2.
  * [Martin Wimpress](https://flexion.org) - Added first boot setup wizard and architecture optimisations.
  * [Ryan Finnie](http://finnie.org) - Raspberry Pi 2 Kernel, Firmware and video driver packages.
  * [Sjoerd Simons](http://sjoerd.luon.net) - Made the initial Raspberry Pi 2 kernel patches for Debian Jessie.
  * [Sergio Conde](http://omxplayer.sconde.net/) - Maintains `omxplayer` for the Raspberry Pi.
  * [Spindle](https://github.com/RPi-Distro/spindle) - a tool to help spin distribution images

## Changes

### 2016-04-24 - 16.04 Final Release for Raspbery Pi 2 and Raspberry Pi 3

  * Added OpemMAX IL hardware accelerated video playback to VLC.
    * To enable hardware accelerated video playback go to `Tools` -> `Preferences` -> `Video` and select `OpenMax IL`.
  * Added MMAL hardware accelerated video playback to ffmpeg.
    * To use hardware accelerated video playback with `ffplay` you must specify the `h264_mmal` codec - `ffplay -vcodec h264_mmal video.mp4`
  * Increased the minimum microSDHC card size to 8GB.
  * Removed `tboplayer`.

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

### Previous changes

  * [See what changed in earlier releases.](/raspberry-pi-change-log/)

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
