---
layout: sidebar
permalink: /faq/usb-image/
lang: en
class: faq
sidebar: faq

title: Preparing a USB Image

---

## What is bootable media?

**So you want to try Ubuntu MATE from a USB drive or SD card?** Great! If you're
new to the process, you might be wondering why you just can't copy the Ubuntu MATE
image on to your media and be good to go. To run an operating system, you need
to write the image to the drive in a way that allows your computer to boot from it.

To install and try Ubuntu MATE from a USB drive or SD card, you'll need media
with at least 4 GB of memory and have
[downloaded a compatible copy of Ubuntu MATE](/faq/downloads/) for your system.

{% include partials/toc.html %}


## Instructions

This applies to both USB and microSD cards.

If the downloaded file has a `.xz` extension, use [7-Zip](http://www.7-zip.org/)
to extract the `.img` file first.

---

### Windows

1. Download the latest version of [balenaEtcher](https://www.balena.io/etcher/).
Double-click on the downloaded file to install.

2. Run the **balenaEtcher** application.

3. Click on the **Select Image** button and choose the Ubuntu MATE `.iso` file
you want to use.

    ![Screenshot of Etcher](/images/faq/bootable/Etcher-Select-Image.png)

4. Click the **Select Target** button and choose the appropriate USB device to
write the .iso to.

    ![Screenshot of Etcher](/images/faq/bootable/Etcher-Select-target.png)

5. Finally, click the **Flash!** button to begin the process.

    ![Screenshot of Etcher](/images/faq/bootable/Etcher-Flash.png)

* It will show a progress bar as it operates.

    ![Screenshot of Etcher](/images/faq/bootable/Etcher-running.png)

* Etcher will notify you when the process is complete.

    ![Screenshot of Etcher](/images/faq/bootable/Etcher-complete.png)

* Please remove the USB drive and plug it into the system where you want to
install Ubuntu MATE.


---

### macOS

If you plan on writing *and* using your bootable USB on Mac hardware, you'll
need to erase and reformat your memory stick using Apple's *Disk Utility*,
which you can launch from **Applications > Utilities** or the search function.

1. After launching *Disk Utility*, insert your USB stick, which will then appear.
  * If it does not, check **View > Show All Devices** from the menu bar.
1. Select the USB stick, and select `Erase` from the tool bar or right-click menu.
1. Select the `MS-DOS (FAT)` format and `GUID Partition Map` from the respective
drop-down menus.
1. Check (and double check - you **can lose data if you select the wrong device
or partition**) that you've chosen the target USB stick and click `Erase`.

    ![Screenshot of Disk Utility](/images/faq/bootable/disk-utility.png)

1. Download and install [Etcher](https://www.balena.io/etcher/), an open source
project that flashes ISOs to SD cards and USB drives.
1. If necessary, open the 'Security and Privacy' section in System Preferences
and allow apps downloaded from 'App Store and identified developers.' If this
still does not allow you to run Etcher, click 'Open Anyway.'

    ![Screenshot of Etcher](/images/faq/bootable/open-etcher.png)

1. Select the previously downloaded Ubuntu MATE ISO (which, by default, is in
your Downloads folder) using **Select Image**.
1. Confirm **Select Target** is pointing to the intended USB drive, and if not,
choose the appropriate device.
1. Click **Flash!** to write the ISO to your USB drive. Etcher will prompt you
for your password. Etcher will display its progress, and inform you when the
process has successfully completed with the image below.
1. If macOS informs you 'The disk you inserted is not readable by this computer,'
 select **Eject**, not **Initialise**

    ![Screenshot of Mac's unreadable disk message](/images/faq/bootable/disk-not-readable.png)

1. To use your bootable media on a Mac device, insert the USB stick and restart
or turn on the device while holding the option/alt key to launch Startup
Manager. Click on the gold disk labeled 'EFI Boot,' which will bring you to
the Ubuntu boot menu.

If you cannot boot from the USB drive on your Mac, try [burning a DVD](https://ubuntu.com/tutorials/tutorial-burn-a-dvd-on-windows).


---

### GNU/Linux

There are several apps and utilities for writing an ISO to a USB drive or a
microSDHC in GNU/Linux, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue) package).

The image can be directly written to a microSDHC or to a USB drive using an
utility like `dd`, but we prefer `ddrescue` (from the
[gddrescue](apt://gddrescue) package).

On a Debian-based system, like Ubuntu MATE, run:

    sudo apt update
    sudo apt install gddrescue

To find the block device name of your USB or microSDHC device, to see all your
connected devices:

    sudo fdisk -l

For example, in the image below, the USB drive is `/dev/sdb` (third entry) and
the first and only partition is `/dev/sdb1` (last entry). Checking the name of
your device is a key step, as **writing to the wrong device might corrupt or
destroy your data**.

![Screenshot of fdisk command in terminal](/images/faq/bootable/fdisk-l.png)

Once you've confirmed you have the correct block device, enter the following
command replacing `path/to/iso` and `sdx` with the path to the iso file and
block device name of your USB drive or microSDHC.

    sudo ddrescue --force -D path/to/iso /dev/sdx


---

### Ubuntu/Ubuntu MATE

[GNOME Disks](apt://gnome-disk-utility) comes pre-installed on Ubuntu 16.04 and
later. This is an easy way to create a bootable USB drive.

If **Disks** is not present on your system, you can install it from the terminal:

    sudo apt-get install gnome-disk-utility

1. Download your chosen Ubuntu MATE image, keep note of the location, and insert
your USB drive. Be sure it's visible in File Manager/Caja. Remember this process
will format your USB drive and **erase all existing data**, so be sure you've
backed it up.

1. Right-click on the ISO file, and select "Open with Disk Image Writer."

    ![Right clicking an ISO file](/images/faq/bootable/gnome_disks_right_click.png)

1. Select your USB drive in the "Destination" drop-down menu.

    ![Screenshot of restore disk image prompt](/images/faq/bootable/gnome_disks_start_restoring.png)

1. Click "Start Restoring." When it asks if you're sure you want to write the
disk image to the device, click "Restore."

    ![Screenshot of GNOME Disks confirming action](/images/faq/bootable/gnome_disks_are_you_sure.png)

1. You may be asked for your password for authentication. Enter it and click "Authenticate."

1. GNOME Disks will begin writing the image, showing its progress and an
estimated time.

    ![Screenshot of GNOME Disks writing data](/images/faq/bootable/gnome_disks_in_progress.png)

When complete, eject (or power off) the disk before removing.
