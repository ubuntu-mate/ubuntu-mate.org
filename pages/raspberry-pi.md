<!-- 
.. title: Ubuntu MATE for the Raspberry Pi 2
.. slug: raspberry-pi
.. date: 2015-04-21 23:01:09 UTC
.. tags: Ubuntu,MATE,Raspberry Pi,download,armhf
.. link: https://ubuntu-mate.community/t/ubuntu-mate-15-04-for-raspberry-pi-2/517
.. description: Ubuntu MATE 15.04 for the Raspberry Pi 2
.. type: text
.. author: Martin Wimpress
-->

Rohith Madhavan and Martin Wimpress have made an Ubuntu MATE 15.04 image
for the Raspberry Pi 2 which you can download or build yourself.

The image is functional and based on the regular Ubuntu `armhf` base, and
not the new Snappy Core, which means that the installation procedure for
applications is the same as that for the regular desktop version, ie using
`apt-get`. 

We have done what we can to optimise the build for the Raspberry Pi 2 and 
one can comfortably use applications such as LibreOffice, which in fact is
a joy to use :-) But the microSDHC I/O throughput is a bottleneck so we
recommend that you use a Class 6 or Class 10 microSDHC card. If you build
the image yourself we recommend you use the `f2fs` filesystem.

You'll need a microSD card which is 4GB or greater to fit the image. The file
system can be resized to occupy the unallocated space of the microSD card,
similar to Raspbian.

**NOTE! There are no predefined user accounts**. The first time you boot the
Ubuntu MATE image it will run through a setup wizard where you can create your
own user account and configure your regional settings. The first boot is quite 
slow, but once the first boot configuration is complete subsequent boots are
much quicker.

<div align="center">
  <img src="/gallery/Screenshots/ubuntu-mate-1504-raspberry-pi-2-screenshot.png" /></a><br />
  <b>Ubuntu MATE 15.04 running on the Raspberry Pi 2.</b>
</div>
<br />

## Download

A pre-built image is also available.

<div class="row">
  <div class="col-lg-6">
    <div class="bs-component">
      <div class="list-group">
        <a class="list-group-item active">Raspberry Pi 2 (ARMv7)</a>
        <p class="list-group-item">For the Raspberry Pi 2, but not the original Raspberry Pi models based on ARMv6.</p>
        <p class="list-group-item">Size : 903 MB</p>
        <p class="list-group-item">MD5 : <code>ea74db696bb50907a12ffbc2f2eeb4b5</code></p>
        <a class="list-group-item" href="https://ubuntu-mate.r.worldssl.net/raspberry-pi/ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2"><strong>File: <u>ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2</u></strong></a>
      </div>
    </div>
  </div>
  <div class="col-lg-6">
    <div class="well bs-component">
      <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
        <fieldset>
          <legend>Download tip</legend>
          <p>If everyone who downloaded Ubuntu MATE donated $2.50 it would
          fund the full-time development of Ubuntu MATE <i>and</i> MATE
          Desktop. Please give us a tip and help the projects flourish!</p>
          <p>If you'd <a href="/donate/">like to donate more or become an Ubuntu MATE patron</a>
          please visit the <a href="/donate/">donate</a> page.</p>
          <img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">
          <div class="form-group">
            <div class="col-lg-6">
              <button type="submit" class="btn btn-primary">Tip us $2.50</button>
            </div>
          </div>
        </fieldset>
        <input type="hidden" name="cmd" value="_xclick">
        <input type="hidden" name="business" value="6282B4CZGVCB6">
        <input type="hidden" name="item_name" value="Ubuntu MATE for Raspberry Pi 15.04 Download Tip">
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
</div>

### HTTP direct download

In addition to the recommended BitTorrent downloads above, the image
can also be downloaded via HTTP.

<div class="row">
  <div class="col-lg-4">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.r.worldssl.net/raspberry-pi/ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2">
        <img src="/assets/img/flags/European Union Flag.png" alt="Ubuntu MATE 15.04 Raspberry Pi 2 Download" title="Ubuntu MATE 15.04 Raspberry Pi 2 Download" />
      </a>
      <p>Ubuntu MATE 15.04 from European CDN</p><p><b>Raspberry Pi 2</b></p>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="well bs-component text-center">
      <a href="http://pub.mate-desktop.org/iso/ubuntu-mate/vivid/armhf/ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2">
        <img src="/assets/img/flags/Germany Flag.png" alt="Ubuntu MATE 15.04 Raspberry Pi 2 Download" title="Ubuntu MATE 15.04 Raspberry Pi 2 Download" />
      </a>
      <p>Ubuntu MATE 15.04 from German mirror</p><p><b>Raspberry Pi 2</b></p>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.org/raspberry-pi/ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2">
        <img src="/assets/img/flags/Italy Flag.png" alt="Ubuntu MATE 15.04 Raspberry Pi 2 Download" title="Ubuntu MATE 15.04 Raspberry Pi 2 Download" />
      </a>
      <p>Ubuntu MATE 15.04 from Italian mirror</p><p><b>Raspberry Pi 2</b></p>
    </div>
  </div>
</div>

If you direct download the .iso image please make sure the MD5 hash matches:

    ea74db696bb50907a12ffbc2f2eeb4b5

### Sponsors

Many thanks to [First Colo](http://www.first-colo.com") and [Prometeus](http://www.prometeus.net)
for sponsoring the hosting and bandwidth for the Ubuntu MATE download.

<div class="row">
  <div class="col-lg-6">
    <div class="well bs-component">
    <a href="http://www.first-colo.com"><img class="centered" src="/assets/img/sponsors/firstcolo.png" alt="First Colo" /></a>
    </div>
  </div>
  <div class="col-lg-6">
    <div class="well bs-component">
    <a href="https://www.prometeus.net/billing/aff.php?aff=239"><img class="centered" src="/assets/img/sponsors/prometeus.png" alt="Prometeus" /></a>
    </div>
  </div>
</div>

## Putting the image on microSDHC

Download the image and then:

  1. Extract the `.img.bz2` archive to get the image file.

    bunzip2 ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2

  2. Write the image file to the microSD card as root.

    sudo ddrescue -d -D --force ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img /dev/sdX

The drive may be mounted on any `/dev/sdX` so use the command `lsblk` to
check.

## Build

**NOTE!** Currently these scripts will only run on an `armhf` device.

  * <https://bitbucket.org/ubuntu-mate/ubuntu-mate-rpi2>

Edit `build-image.sh` and change `BASEDIR`. Then run the build.

    sudo ./build-image.sh

This will take a long time, so I suggest you start this running before you go
to bed.

## Re-size file system

There are no utilities included for automatic file system re-sizing. However,
it's not hard to do manually. Once booted:

    sudo fdisk /dev/mmcblk0

Delete the second partition (d, 2), then re-create it using the defaults 
(n, p, 2, enter, enter), then write and exit (w). Reboot the system, then:

    sudo resize2fs /dev/mmcblk0p2

## Hardware accelerated video

To play videos using **hardware accelerated decoding you will need MPEG-2 and/or VC-1 
licenses from the [Raspberry Pi Store](http://www.raspberrypi.com/license-keys/)**.
You can then use `omxplayer`, which uses the Raspberry Pi VideoCore libraries, to
provide hardware accelerated video playback.

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

Please post all feedback on the [dedicated community topic](https://ubuntu-mate.community/t/ubuntu-mate-15-04-for-raspberry-pi-2/517).
If you have any improvements then please submit a pull request to our
BitBucket.

  * <https://bitbucket.org/ubuntu-mate/ubuntu-mate-rpi2>

## Credits

  * [Rohith Madhavan](http://rohithmadhavan.com) - Made the Ubuntu MATE 15.04 image.
  * [Martin Wimpress](https://flexion.org) - Added first boot setup wizard and architecture optimisations.
  * [Ryan Finnie](http://finnie.org) - Raspberry Pi 2 Kernel, Firmware and video driver packages.
  * [Sjoerd Simons](http://sjoerd.luon.net) - Made the initial Raspberry Pi 2 kernel patches for Debian Jessie.
  * [Sergio Conde](http://omxplayer.sconde.net/) - Maintains `omxplayer` for the Raspberry Pi.

## Changes

### 2015-04-22

  * Enabled Ryan Finnie's PPA.
    * <https://launchpad.net/~fo0bar/+archive/ubuntu/rpi2>
    * Many thanks to Ryan for adding Vivid as a build target.
  * Changed from `cfq` to `deadline` I/O scheduler.
  * Added `xserver-xorg-video-fbturbo` (an accelerated x.org driver) 0~git.20150305.e094e3c-1.15.04.
    * Limited to hardware accelerated window moving and scrolling.
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

### 2015-03-14

  * Enabled `systemd` as the init system.
  * Added `raspberrypi-vc` (VideoCore GPU libraries) 1.20150301.0de0b20-3.
  * Added `omxplayer` 0.3.6~git20150217~5337be8.
  * Added `linux-firmware`.
  * Added `openssh-server`.
  
### 2015-03-07

  * Initial Release.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Release announcement</h1>
        <p>Find out what changed in Ubuntu MATE 15.04</p>
        <a href="/blog/ubuntu-mate-vivid-final-release/" class="btn btn-primary btn-lg">Release announcement</a>
        </p>
    </div>
</div>

## TODO

  * Add OpenSSH with host key regeneration on first boot.
  * Add `raspi-config` or equivilent.
  * Add automatic reszing of the root file system.

## Useful Information

You may find the following information useful, which is why we titled 
the section *Useful Information* since the information presented here
is mostly useful.

  * [Ubuntu MATE 15.04 Useful Information](https://ubuntu-mate.community/t/ubuntu-mate-14-10-and-15-04-useful-information/24)

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

## Other ARMv7 based devices

We'd love to see Ubuntu MATE images other ARMv7 based devices. Please take
a look at our generic armhf Ubuntu MATE root file system and build scripts.

  * <https://ubuntu-mate.org/armhf-rootfs/>
  * <https://bitbucket.org/ubuntu-mate/ubuntu-mate-armhf>

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
