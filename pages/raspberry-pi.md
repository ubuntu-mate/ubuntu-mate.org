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

The image is functional and based on the regular Ubuntu `armhf` base,
not the new Snappy Core, which means that the installation procedure
for applications is the same as that for the regular desktop version,
ie using `apt-get`.

We have done what we can to optimise the build for the Raspberry Pi 2
and Raspberry Pi 3, you can comfortably use applications such as
LibreOffice, which in fact is a joy to use :-) But the microSDHC I/O
throughput is a bottleneck so **we recommend that you use a Class 6 or
Class 10 microSDHC** card.

You'll need a microSD card which is 4GB or greater to fit the image.
The file system can be resized to occupy the unallocated space of the
microSD card, **on Ubuntu MATE 16.04 this can be done via Ubuntu MATE
Welcome**.

**Ubuntu MATE 16.04 has working Bluetooth and Wifi work on the Raspberry
Pi 3**

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
        <h1>Download</h1>
        <p>Run Ubuntu MATE on your Raspberry Pi 2 or 3 today.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download Ubuntu MATE</a>
        </p>
    </div>
</div>


## Making a microSDHC

The image can be directly written to a microSDHC using a utility like
`dd`, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue), for example:

    sudo apt-get install gddrescue xz-utils
    unxz ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz
    sudo ddrescue -D --force ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img /dev/sdx

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
screen, clicking the **Resize** button and then restarting the Raspberry Pi.

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

  * [Rohith Madhavan](http://rohithmadhavan.com) - Made the Ubuntu MATE 15.04 image for the Raspberry Pi 2.
  * [Martin Wimpress](https://flexion.org) - Added first boot setup wizard and architecture optimisations.
  * [Ryan Finnie](http://finnie.org) - Raspberry Pi 2 Kernel, Firmware and video driver packages.
  * [Sjoerd Simons](http://sjoerd.luon.net) - Made the initial Raspberry Pi 2 kernel patches for Debian Jessie.
  * [Sergio Conde](http://omxplayer.sconde.net/) - Maintains `omxplayer` for the Raspberry Pi.
  * [Spindle](https://github.com/RPi-Distro/spindle) - a tool to help spin distribution images

## Changes

    [See what's new and changed.](/raspberry-pi-change-log/)

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
