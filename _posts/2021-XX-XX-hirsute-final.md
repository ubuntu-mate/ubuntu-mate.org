---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-21.04-release-candidate/
category: release                               
author: TBC
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 21.04 Release Notes
description: What's new in Ubuntu MATE 21.04 (Hirsute Hippo)

---

**Ubuntu MATE 21.04 has:...**
* Yaru MATE - theme, Suru icon, LIbreOffice, Metacity, GTKSourceView
* Yaru MATE snap (theme and icons) and how to use it. The snaps are shipped on the iso by default.
* Ayatana Indicators and the new settings
* Mutiny theme changes - dropped MATE Dock Applet    
* Removed RedShift.

{:.center}
![Ubuntu MATE 21.04](/images/blog/hirsute/hirsute-hippo-desktop.png)
**Tagline goes here.**




## What changed since the Ubuntu MATE 21.04?


### Linux Kernel

(Any relevant kernel updates will go here)


### MATE Desktop

(MATE Desktop updates will go here)


### Hardware Enablement

(Any relevant updates will go in this section. Otherwise, delete.)


## Raspberry Pi images

(The Raspberry Pi image will be developed and released shortly after the initial release. Do we want to say that this section will be edited once the Pi image is created and finalized??????)


## Major Applications

Accompanying **MATE Desktop X.XX.X* and **Linux X.X** are **Firefox
59.0.2**, **VLC 3.0.4**, **LibreOffice 6.1.2.1**


### (Applications of Note)

(Yaru discussion with mention of community Yaru theme wallpaper?)


{:.center}
![Major Applications](/images/blog/hirsute/versions.png)

See the [Ubuntu 21.04 Release Notes](https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 21.04"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}


## Upgrading from Ubuntu MATE 20.04 LTS or 20.10

You can upgrade to Ubuntu MATE 21.04 from Ubuntu MATE 20.04 LTS or 20.10. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

  * Open the "Software & Updates" from the Control Center.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" drop down menu to "For any new version".
  * Press <kbd>Alt</kbd>+<kbd>F2</kbd> and type in `update-manager -c -d` into the command box.
  * Update Manager should open up and tell you: New distribution release '21.04' is available.
    * If not, you can use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click "Upgrade" and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.


## Known Issues

Here are the known issues. (Should have a note about the screenreader on install, and how this is a priority for us to address ASAP with the next release)



{% include partials/known-issues.html filter="21.04" %}


## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
