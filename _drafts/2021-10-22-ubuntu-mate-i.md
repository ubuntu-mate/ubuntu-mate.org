---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-adjective-animal-final-release/
category: dev                                # Beta Only - change to 'release'
author: Martin Wimpress
lang: en
discourse_topic_id: # TBC

title: Ubuntu MATE 21.10 Release Notes
description: What's new in Ubuntu MATE 21.10 (Code Name)

---

<!--- Beta Only - Remove for final release --->

> We are preparing Ubuntu MATE 21.10 (Code Name) for distribution on
[October XXth, 2021](https://discourse.ubuntu.com/c/release/38).
With this **Beta** pre-release, you can see what we are trying out in
preparation for our next (stable) version.

<!--- End of Beta Only --->

Some words to summarise the release focus and say thanks. Read on to learn more...

{:.center}
![Ubuntu MATE 21.10 Beta](/images/blog/adjective/adjective-animal-desktop.png)
**Ubuntu MATE 21.10 (Code name).**

<!--- Beta Only - Remove for final release --->

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

Ubuntu MATE *Beta Releases* are *NOT* recommended for:

  * Regular users who are not aware of pre-release issues
  * Anyone who needs a stable system
  * Anyone uncomfortable running a possibly frequently broken system
  * Anyone in a production environment with data or workflows that need to be reliable

Ubuntu MATE *Beta Releases* are recommended for:

  * Regular users who want to help us test by finding, reporting, and/or fixing bugs
  * Ubuntu MATE, MATE, and GTK+ developers.

<!--- End of Beta Only --->


## What changed since the Ubuntu MATE 21.04?


### MATE Desktop

(MATE Desktop updates will go here)


### Hardware Enablement

(Any relevant updates will go in this section. Otherwise, delete.)


## Raspberry Pi images

(New Raspberry Pi images, or planned new images between now and the next
release, should go here. If no Raspberry Pi updates, delete.)


## Major Applications

Accompanying **MATE Desktop X.XX.X* and **Linux X.X** are **Firefox XX.X**,
**Celluloid 0.XX**, **LibreOffice X.X.X.X**

### (Applications of Note)

(Any significant additions or changes that merit more discussion can
go in their own subsection.)

{:.center}
![Major Applications](/images/blog/adjective/versions.png)

See the [Ubuntu 21.10 Release Notes](https://discourse.ubuntu.com/c/release/38)
for details of all the changes and improvements that Ubuntu MATE benefits from.

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 21.10"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading from Ubuntu MATE 21.04

You can upgrade to Ubuntu MATE 21.10 from Ubuntu MATE 21.04. Ensure that you
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

{% include partials/known-issues.html filter="21.10" %}

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
