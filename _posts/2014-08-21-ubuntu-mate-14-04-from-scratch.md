---
layout: blog-post
class: blog
title: Ubuntu MATE 14.04 from Scratch
permalink: /blog/2014-08-ubuntu-mate-14-04-from-scratch
description: Installing Ubuntu MATE 14.04 from scratch
category: dev
author: Martin Wimpress
lang: en
---

We are getting a lot of requests for Ubuntu MATE 14.04 .iso images but we
won't be in a position to make them until after Ubuntu MATE 14.10 is
released. So, as an interim measure here are some instructions for creating
your own Ubuntu MATE 14.04 from scratch.

The basic steps are:

  * Install Ubuntu from a netboot .iso
  * Add the Ubuntu MATE PPAs
  * Install the required packages
  * Tweak the configuration

## Download Ubuntu 14.04 netboot .iso image

Visit the URL below and download either the i386 or amd64 `mini.iso`.

  * <http://cdimage.ubuntu.com/netboot/14.04/>

Burn the .iso to CD or `dd` it to a USB stick.

{% include blog/alert.html
    style = "warning"
    title = "UEFI and Wireless!"
    text = "While the `mini.iso` is handy, there are some limitations."
%}

  * It can't boot or install UEFI computers that you want to run in UEFI mode because it lacks the required files for booting the computer in UEFI
mode. Therefore, if you have a UEFI computer you need to enable *"Legacy BIOS Mode"*.
  * If you have a wireless card that requires firmware or a proprietary driver then you will have to connect via ethernet cable to complete the initial installation.

## Install a minimal Ubuntu 14.04

Installing from `mini.iso` is straight forward, here is an overview of what
to do.

  * When `mini.iso` boots select `Install` by pressing **ENTER**.
  * Select your language.
  * Select your location.
  * Configure your keyboard layout.
  * Enter the hostname for the computer.
  * Choose a mirror location for the Ubuntu archive.
  * Configure the HTTP proxy to use (if required).
  * Create your user account.
  * Decide if you want your home directory encrypted or not.
  * Select your time zone.
  * Partition the disk(s).

The base system packages will now be downloaded and installed, this is a good
time for a cup of tea. Or, if your Internet connection is like mine, then it
is time for a pot of tea while you bake a cake.

  * Select your preferred update management policy.
  * When the 'Software selection' menu is displayed make sure nothing is selected
  then choose `<Continue>`.
  * Install the GRUB boot loader.

{% include blog/alert.html
    style = "warning"
    title = "USB and GRUB"
    text = "Using the netboot .iso from the USB may need special attention."
%}

As Jon notes in the comments, when using `mini.iso` from a USB stick the installer often sees the
USB as `/dev/sda` and the disk you are installing to as `/dev/sdb`. This is apparent during the
partitioning.

When it's time for the installer to write the bootloader to a drive, it defaults to `/dev/sda`.
Since `/dev/sda` is the USB stick, bad things will happen. So, select the **No** option that's offered
at that point and manually identify where the bootloader should actually go, very likely `/dev/sdb`.

  * Set the system time to UTC or local time.

The minimal Ubuntu installation is complete, choose `<Continue>` to reboot.

## Configure Ubuntu

Login using the user account you created earlier. A few packages need to be installed so that the Ubuntu MATE PPAs can be added easily.

    sudo apt-get install python-software-properties software-properties-common

## Add the Ubuntu MATE PPAs

Now add the Ubuntu MATE PPAs.

    sudo apt-add-repository ppa:ubuntu-mate-dev/ppa
    sudo apt-add-repository ppa:ubuntu-mate-dev/trusty-mate
    sudo apt-get update

## Install Ubuntu MATE

Execute the following to install Ubuntu MATE.

    sudo apt-get install --no-install-recommends ubuntu-mate-core ubuntu-mate-desktop linux-firmware-nonfree

Remember that cake you baked earlier? Now is a good time to eat it.

### Post-install configuration

When the install is complete some post-install configuration is *required*.

During the `mini.iso` install a user account was created, which is
missing a couple of files that make Network Manager work and
correct the default icons for LibreOffice. Therefore these Ubuntu MATE
configuration files need to be manually overlayed.

    rsync -av /etc/skel/.config/ ~/.config/
    rsync -av /etc/skel/.local/ ~/.local/

This last tweak is required to get NetworkManager fully working. Edit
`/etc/network/interfaces` to remove any extra lines so that it looks
*exactly* like this:

    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).

    # The loopback network interface
    auto lo
    iface lo inet loopback

### Audio and Video Codecs?

If you'd like some additional audio/video codecs and Adobe Flash then install
the following package.

    sudo apt-get install ubuntu-restricted-addons

### Virtualbox?

If you are doing this in a Virtualbox guest then you'll want to install these
additional packages.

    sudo apt-get install virtualbox-guest-x11 virtualbox-guest-dkms

## All done!

You can now reboot into your shiny new Ubuntu MATE 14.04.

#### References

  * <https://help.ubuntu.com/community/Installation/MinimalCD>
