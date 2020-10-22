---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-groovy-final-release/
category: dev                                # Beta Only - change to 'release'
author: Monica Madon 
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 20.10 Release Notes
description: What's new in Ubuntu MATE 20.10 (Groovy Gorilla)

---

Ubuntu MATE 20.10 is a modest :relaxed:, yet strategic :chart_with_upwards_trend:, upgrade over our 20.04
release. If you want bug fixes :bug:, kernel updates :corn:, a new web camera control :movie_camera:,
and a new indicator :point_right: experience, then 20.10 is for you :tada:. Ubuntu MATE 20.10 
will be supported for 9 months until July 2021. If you need Long Term
Support, we recommend you use [Ubuntu MATE 20.04 LTS](website!)

Read on to learn more... :point_down:

{:.center}
![Ubuntu MATE 20.10](/images/blog/eoan/eoan-ermine-desktop.png)
**Tagline goes here.**

## What's changed since Ubuntu MATE 20.04?


### Linux Kernel

Ubuntu MATE 20.10 includes the 5.8 Linux kernel. This includes numerous 
updates and added support since the 5.4 Linux kernel released in 
Ubuntu 20.04 LTS. Some notable examples include:

* Airtime Queue limits for better WiFi connection quality
* Btrfs RAID1 with 3 and 4 copies and more checksum alternatives
* USB 4 (Thunderbolt 3 protocol) support added
* X86 Enable 5-level paging support by default
* Intel Gen11 (Ice Lake) and Gen12 (Tiger Lake) graphics support
* Initial support for AMD Family 19h (Zen 3)
* Thermal pressure tracking for systems for better task placement wrt CPU core
* XFS online repair
* OverlayFS pairing with VirtIO-FS
* General Notification Queue for key/keyring notification, mount changes, etc.
* Active State Power Management (ASPM) for improved power savings of PCIe-to-PCI devices
* Initial support for POWER10



### MATE Desktop

(MATE Desktop updates will go here)


### Hardware Enablement

(Any relevant updates will go in this section. Otherwise, delete.)


## Raspberry Pi images

(New Raspberry Pi images, or planned new images between now and the next
release, should go here. If no Raspberry Pi updates, delete.)


## Major Applications

Accompanying **MATE Desktop 1.24.X* and **Linux 5.8** are **Firefox
81** and **LibreOffice 7.0.2**


### Webcamoid

* We've replaced Cheese :cheese: with Webcamoid :movie_camera: as the default webcam tool for 
several reasons.
* Webcamoid is a full webcam/capture configuration tool with recording, 
overlays and more, unlike Cheese. While there were initial concerns :pensive:, since 
Webcamoid is a Qt5 app, nearly all the requirements in the image are 
pulled in via YouTube-DL :tada:.
* We've disabled notifications :bell: for Webcamoid updates if installed from 
universe pocket as a deb-version, since this would cause errors in the 
user's system and force them to download a non-deb version. This only 
affects users who don't have an existing Webcamoid configuration.



{:.center}
![Major Applications](/images/blog/cosmic/versions.png)

See the [Ubuntu 20.10 Release Notes](https://wiki.ubuntu.com/GroovyGorilla/ReleaseNotes)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 20.10"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}


## Upgrading from Ubuntu MATE 20.04 LTS

You can upgrade to Ubuntu MATE 20.10 from Ubuntu MATE 20.04 LTS. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" drop down menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c -d` into the command box.
  * Update Manager should open up and tell you: New distribution release 'XX.XX' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.


## Known Issues

Here are the known issues.

{% include partials/known-issues.html filter="20.10" %}


## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
