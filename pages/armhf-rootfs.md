<!--
.. title: Ubuntu MATE generic armhf rootfs
.. slug: armhf-rootfs
.. date: 2015-05-09 13:01:09 UTC
.. tags: Ubuntu,MATE,armhf,ARMv7,aarch32
.. link:
.. description: Ubuntu MATE 15.04 generic armhf root file system
.. type: text
.. author: Martin Wimpress
-->

The Ubuntu MATE team have made a generic Ubuntu MATE 15.04 root file system for
aarch32 (ARMv7) based devices. This root file system is intended for ARMv7
enthusiasts and board manufacturers who'd like to make an Ubuntu MATE image for
their device(s). In order to adapt the root file system for your device you'll
need to:

  * Add a boot loader
  * Add a kernel
  * Add X.org 1.17 drivers
  * Add any other hardware specific configuration

We'd love Ubuntu MATE images for more aarch32 (ARMv7) devices and we will gladly
host the images and catalogue what the community creates.

The root file system is based on the regular Ubuntu `armhf` base, and not the
new Snappy Core, which means that the installation procedure for applications is
the same as that for the regular desktop version, ie using `apt-get`.

**NOTE! There are no predefined user accounts**. The first time you boot the
Ubuntu MATE image it will run through a setup wizard where you can create your
own user account and configure your regional settings. The first boot is quite
slow, but once the first boot configuration is complete subsequent boots are
much quicker.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Release announcement</h1>
        <p>Find out what changed in Ubuntu MATE 15.04</p>
        <a href="/blog/ubuntu-mate-vivid-final-release/" class="btn btn-primary btn-lg">Release announcement</a>
        </p>
    </div>
</div>

## Making an Ubuntu MATE image for aarch32 (ARMv7) based devices

These instructions are brief but hopefully sufficient for ARM device hackers to
get started.

## Download

The generic Ubuntu MATE aarch32 (ARmv7) root filesystem tarball is available
via BitTorrent and direct download. If you can spare the bytes, please
download via BitTorrent and leave the client open after your download is
finished, so you can seed it back to others. <i>A web-seed capable client is
recommended for fastest download speeds.</i></p>

Many thanks to [First Colo](http://www.first-colo.com) for contributing the
hosting and bandwidth for the Ubuntu MATE downloads.

<div class="row">
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.org/armhf-rootfs/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz.torrent">
        <img src="/assets/img/misc/torrent.png" alt="Ubuntu MATE 15.04 aarch32 (ARMv7) Torrent" title="Ubuntu MATE 15.04 aarch32 (ARMv7) Torrent" />
      </a>
      <p>Ubuntu MATE 15.04 via BitTorrent</p><p><b> aarch32 (ARMv7)</b></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="https://ubuntu-mate.r.worldssl.net/armhf-rootfs/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz">
        <img src="/assets/img/flags/European-Union-Flag-128.png" alt="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" title="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" />
      </a>
      <p>Ubuntu MATE 15.04 from European CDN</p><p><b> aarch32 (ARMv7)</b></p>
    </div>
  </div>
  <div class="col-lg-2">
    <div class="well bs-component text-center">
      <a href="http://can.ubuntu-mate.net/armhf-rootfs/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz">
        <img src="/assets/img/flags/Canada-Flag-128.png" alt="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" title="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" />
      </a>
      <p>Ubuntu MATE 15.04 from Canadian mirror</p><p><b> aarch32 (ARMv7)</b></p>
    </div>
  </div>
  <div class="col-lg-2">
    <div class="well bs-component text-center">
      <a href="http://fra.ubuntu-mate.net/armhf-rootfs/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz">
        <img src="/assets/img/flags/France-Flag-128.png" alt="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" title="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" />
      </a>
      <p>Ubuntu MATE 15.04 from France mirror</p><p><b> aarch32 (ARMv7)</b></p>
    </div>
  </div>
  <div class="col-lg-2">
    <div class="well bs-component text-center">
      <a href="http://ita.ubuntu-mate.net/armhf-rootfs/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz">
        <img src="/assets/img/flags/Italy-Flag-128.png" alt="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" title="Ubuntu MATE 15.04 aarch32 (ARMv7) Download" />
      </a>
      <p>Ubuntu MATE 15.04 from Italian mirror</p><p><b> aarch32 (ARMv7)</b></p>
    </div>
  </div>
</div>

If you direct download the image please make sure the MD5 hash matches:

  * `dcbc6539d2260ddcc7bb13a963f35583`

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
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.04 armhf-rootfs Download Tip">
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
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.04 armhf-rootfs Download Tip">
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
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.04 armhf-rootfs Download Tip">
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
        <input type="hidden" name="item_name" value="Ubuntu MATE 15.04 armhf-rootfs Download Tip">
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

### Extract the root file system

The root filesystem tarball will require a minimum of 4GB to extract. Extract
the rootfs archive to the location the example build script uses.

    sudo mkdir -p /var/local/build/vivid/ubuntu-mate/mate
    cd /var/local/build/vivid/ubuntu-mate/mate
    tar xvf ~/Download/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz .

### Get the example build script

**NOTE!** Currently this script will only run on an `armhf` device.

The Ubuntu MATE team have created a very simple script that builds an Ubuntu
MATE armhf image. This is largely based on the image we made for the Raspberry
Pi 2 and will require some modification for other devices.

    cd ~
    git clone git@bitbucket.org:ubuntu-mate/ubuntu-mate-armhf.git

### Build an image

**NOTE!** Currently this script will only run on an `armhf` device.

In order to add support for a new aarch32 (ARMv7) device you will need to:

  * Create a `configure_device()` function. The `configure_raspi2()` can be used
  as a reference.
  * Modify the `armhf_image()` function so `${DEVICE_NAME}` can call your
  `configure_device()` function.
  * You may need to modify the `make_image()` function to correctly setup the
  `/boot` and `/` partitions for your device.
  * At the bottom of the script add a call to `armhf_image` that references your
  device.

Once the above changes have been made, execute the script from a shell.

    sudo ./build-image.sh

This will take a long time, so I suggest you start this running before you go
to bed.

**Tip!** Mount `/var/local/build/` on a NAS via NFS.

If you add support for a new device please submit a pull request.

  * <https://bitbucket.org/ubuntu-mate/ubuntu-mate-armhf>

### Write an image to flash

Once you've created an image it can be written to flash storage using `ddrescue`.

    sudo ddrescue -d -D --force ubuntu-mate-15.04-desktop-armhf-device.img /dev/sdX

The flash storage may be mounted on any `/dev/sdX` so use the command `lsblk` to
check.

## Feedback and Improvements

If you start working on, or create, an Ubuntu MATE image for an aarch32 (ARMv7) device then
please let us know in the [Ubuntu MATE Development Discussion](https://ubuntu-mate.community/c/development-discussion) forum.

If you have any improvements, or add support for a new device, then please submit
a pull request to our [BitBucket](https://bitbucket.org/ubuntu-mate/ubuntu-mate-armhf).

## References

The Ubuntu MATE team have created an image for the Raspberry Pi 2. It may be a
useful reference.

  * <https://bitbucket.org/ubuntu-mate/ubuntu-mate-rpi2>

## Changes

### 2015-05-09

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
