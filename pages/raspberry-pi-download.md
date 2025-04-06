---
layout: sidebar
permalink: /raspberry-pi/download/
lang: en
sidebar: raspberry-pi

title: Raspberry Pi Images

---

## Is Ubuntu MATE still producing Raspberry Pi images?

Unlikely. The efforts from the Ubuntu MATE project has helped Ubuntu to become a first class release target
for the Raspberry Pi. You can download [Ubuntu for Raspberry Pi](https://ubuntu.com/download/raspberry-pi)
from Canonical for certified reliability and performance, with improved support for newer models.


## How can I install the MATE desktop on top of Ubuntu?

Unofficially, the Ubuntu MATE experience can be installed under regular Ubuntu using the terminal:

    sudo apt update
    sudo apt upgrade
    sudo apt install ubuntu-mate-desktop

Then reboot. On the login screen, select "MATE" as the session.


## Where can I find older images?

Our older images will continue to be available to download from our [archived releases server](https://releases.ubuntu-mate.org).
In some cases, the base system may still be supported. Check the support status using this command:

    ubuntu-security-status

for 20.04 and later. For 18.04 and older, instead use:

    ubuntu-support-status

See also: [Raspberry Pi Compatibility](/raspberry-pi/compatibility/)


## Which image should I use?

There are typically two images:

### arm64 (64-bit)

We recommend `arm64` for newer Pi models with more then 2 GB of RAM as the
hardware will benefit from CPU and memory pressure optimisations.
This will be our focus for future development.


### armhf (32-bit)

`armhf` has been the traditional target for Raspbian, and works best on
low RAM hardware like the Pi 2 and 3. Choose this one if you need to maximize
compatibility with software designed for Raspberry Pi OS.


## Can I build my own image?

Yes, check out this repository: <https://github.com/wimpysworld/ubuntu-pi-image>


## Where can I ask for help?

You're welcome to ask questions over in our [Raspberry Pi category](https://ubuntu-mate.community/c/support/raspberry-pi/19) on the Ubuntu MATE Community.
