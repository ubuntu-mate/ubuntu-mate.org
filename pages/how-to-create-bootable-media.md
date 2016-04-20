<!--
.. title: How to create a bootable USB Drive.
.. slug: how-to-create-bootable-usb-drive
.. date: 2016-04-07 21:55:10 UTC
.. tags: How-to,Help,Boot,USB,DVD,Quick,Getting Started
.. link:
.. description: How to create a bootable USB drive for Ubuntu MATE.
.. type: text
.. author: Martin Wimpress & Luke Horwell
-->

## Creating a Bootable USB Drive

### On Ubuntu and Ubuntu MATE

[GNOME Disks](apt://gnome-disk-utility) is pre-installed on Ubuntu 16.04 and
newer. Use the *Restore Disk Image...* option, **which natively supports XZ
compressed images**.

If **Disks** is not present on your system, you can install it from the terminal:

    sudo apt-get install gnome-disk-utility

<div align="center">
    <iframe width="640" height="480" src="https://www.youtube.com/embed/V_6GNyL6Dac?html5=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>


### On GNU/Linux

The image can be directly written to a microSDHC using a utility like
`dd`, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue) package).

For example, for Debian-based systems:

    sudo apt-get install gddrescue xz-utils
    unxz ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz
    sudo ddrescue -D --force ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img /dev/sdx

Replace `/dev/sdX` with your actual device. Use the `lsblk` command to check.

<div align="center">
    <script type="text/javascript" src="https://asciinema.org/a/34243.js" id="asciicast-34243" async></script>
</div>


### On Windows

If you want to make a microSDHC using Windows we recommend:

  * [7-Zip](http://www.7-zip.org/) to extract the image.
  * [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) to write the image.


### On Mac OS X

[Official instructions are provided by Ubuntu.](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx)
