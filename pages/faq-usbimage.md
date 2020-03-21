---
layout: sidebar
title: Preparing a USB Image
permalink: /faq/usb-image/
lang: en
class: faq
sidebar: faq
---

## What is 'bootable media'? 

So you want to try Ubuntu MATE from a USB drive or SD card? Great! If you're new to the process, however, you might be wondering why you just can't copy the Ubuntu MATE image on to your media and be good to go. To run an operating system, you need to install the image to the drive in a way that allows your computer to boot from it.

To install and try Ubuntu MATE from a USB drive or SD card, you'll need media with at least 4 GB of memory and an [Ubuntu MATE image](/faq/downloads/).


### On Windows

**To make a bootable USB using Windows:**


 Download the latest version of [balenaEtcher](https://www.balena.io/etcher/). Double-click on the downloaded file to install.

 Run the **balenaEtcher** application.

 Click on the **Select Image** button and choose the Ubuntu MATE .iso file you want to use.


 ![EtcherSelectWindows](/images/bootable/Etcher-Select-image.png)

 Next click the **Select Target** button and choose the appropriate USB device to write the .iso to.

 ![EtcherSelectTarget](/images/bootable/Etcher-Select-target.png)

 Finally, click the **Flash!** button to begin the process.

 ![EtcherFlashWindows](/images/bootable/Etcher-Flash.png)

 It will show a progress bar as it operates.

 ![EtcherRunning](/images/bootable/Etcher-running.png)

 Etcher will notify you when the process is complete.

 ![EtcherCompleteWindows](/images/bootable/Etcher-complete.png)

 Please remove the USB drive and plug it into the system where you want to install Ubuntu MATE. 






**To make a bootable microSD using Windows:**


  *  If the downloaded file has a   `.xz` extension, use [7-Zip](http://www.7-zip.org/) to extract the .img file.

Once you have a `.img` file please follow the steps listed in the *If you want to make a bootable USB using Windows* section to write your image to your microSD card. Once completed, please remove your microSD card and insert it into your RaspberryPi.


### On Mac

**To make a bootable USB using a Mac**

If you plan on writing *and* using your bootable USB on Mac hardware, you'll need to erase and reformat your memory stick using Apple's *Disk Utility*, which you can launch from Applications>Utilities or the search function.

* After launching *Disk Utility*, insert your USB stick, which will then appear (Enable View>Show All Devices if it does not).
* Select the USB stick, and select `Erase` from the tool bar or right-click menu.
* Select the `MS-DOS (FAT)` format and `GUID Partition Map` from the respective drop-down menus.
* Check (and double check - you can lose data if you select the wrong device or partition) that you've chosen the target USB stick and click `Erase`.

![DiskUtility](/images/bootable/disk-utility.png)

* Download and install [Etcher](https://www.balena.io/etcher/), an open source project that flashes ISOs to SD cards and USB drives. 
* If necessary, open the 'Security and Privacy' section in System Preferences and allow apps downloaded from 'App Store and identified developers.' If this still does not allow you to run Etcher, click 'Open Anyway.'

![OpenEtcher](/images/bootable/open-etcher.png)

* Select the previously downloaded Ubuntu MATE ISO (which, by default, is in your Downloads folder) using **Select Image**.
* Confirm **Select Target** is pointing to the intended USB drive, and if not, choose the appropriate device.
* Click **Flash!** to write the ISO to your USB drive. Etcher will prompt you for your password. Etcher will display its progress, and inform you when the process has successfully completed with the image below.
* If OSX informs you 'The disk you inserted is not readable by this computer,' select **Eject**, not **Initialise**

![EtcherSuccess](/images/bootable/Etcher-complete.png)

* To use your bootable media on a Mac device, insert the USB stick and restart or turn on the device while holding the option/alt key to launch Startup Manager. Click on the gold disk labeled 'EFI Boot,' which will bring you to the Ubuntu boot menu.

If you cannot boot from the USB drive on your Mac, try [burning a DVD](https://ubuntu.com/tutorials/tutorial-burn-a-dvd-on-windows).




### On GNU/Linux

*To make a bootable USB/SD card using GNU/Linux*

There are several apps and utilities for writing an ISO to a USB drive or a microSDHC in GNU/Linux, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue) package). 

The image can be directly written to a microSDHC or to a USB drive using an utility like
`dd`, but we prefer `ddrescue` (from the [gddrescue](apt://gddrescue) package).

* On a Debian-based system, like Ubuntu MATE, run `sudo apt update` and `sudo apt install gddrescue`. 
* To find the block device name of your USB or microSDHC device, enter `sudo fdisk -l` to see all connected devices. For example, in the image below, the USB drive is /dev/sdb1/. Checking the name of your device is a key step, as writing to the wrong device might corrupt or destroy your data. 

![fdisk-l](/images/bootable/fdisk-l.png)

* Once you've confirmed you have correct block device, enter `sudo ddrescue --force -D path/to/.iso /dev/sdx`, replacing 'path/to/.iso' and 'sdx' with the path to the iso file and block device name of your USB drive or microSDHC.

#### On Ubuntu/Ubuntu MATE

[GNOME Disks](apt://gnome-disk-utility), which comes pre-installed on Ubuntu 16.04 and
newer, is an easy way to create a bootable USB drive.

If **Disks** is not present on your system, you can install it from the terminal with `sudo apt-get install gnome-disk-utility`. 

* Download your chosen Ubuntu MATE image, keep note of the location, and insert your USB drive. Be sure it's visible in File Manager/Caja. Remember this process will format your USB drive and erase all existing data, so be sure you've backed it up.
* Right-click on the ISO file, and select "Open with Disk Image Writer."

![GNOME Disks Right Click](/images/bootable/gnome_disks_right_click.png)

* GNOME Disks will open a "Restore Disk Image" popup. Select your USB drive in the "Destination" drop-down menu.

![GNOME Disks Start Restoring](/images/bootable/gnome_disks_start_restoring.png)

* Click "Start Restoring." When it asks if you're sure you want to write the disk image to the device, click "Restore."

![GNOME Disks Are You Sure](/images/bootable/gnome_disks_are_you_sure.png)

* Gnome Disks will ask for your password for authentication. Enter it and click "Authenticate."

![GNOME Disks In Progress](/images/bootable/gnome_disks_in_progress.png)

* Gnome Disks will begin writing the image, and will show a progress bar. Eject the disk before removing.
