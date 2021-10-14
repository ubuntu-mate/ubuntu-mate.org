---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-impish-indri-final-release/
category: release
author: Martin Wimpress
lang: en
discourse_topic_id: 24668

title: Ubuntu MATE 21.10 Release Notes
description: What's new in Ubuntu MATE 21.10 (Impish Indri)

---

The significant change in Ubuntu MATE 21.10 is the introduction of [MATE Desktop
1.26.0](https://mate-desktop.org/blog/2021-08-08-mate-1-26-released/) ✨ which was
18 months in the making. Thanks to the optimisations in MATE Desktop 1.26, Ubuntu
MATE 21.10 is faster and leaner 💪

{:.center}
![Ubuntu MATE 21.10](/images/blog/impish/impish-indri-desktop.png)
**Ubuntu MATE 21.10 (Impish Indri).**

## What changed since the Ubuntu MATE 21.04?

Here are the highlights of what's changed since the [release of Hirsute
Hippo 🦛](https://ubuntu-mate.org/blog/ubuntu-mate-hirsute-hippo-release-notes/)

### MATE Desktop 🧉

A **significant effort 😅 has been invested in fixing bugs 🐛 in MATE Desktop 1.26.0,
optimising performance ⚡ and plugging memory leaks**. MATE Desktop is faster and
leaner as a result and it's **underpinnings have been modernised and updated**. This
last point mostly benefits developers working on MATE, but is important to
highlight to users at it demonstrates **MATE Desktop is being maintained to ensure it's longevity**.

Here are some of the other **quality of life 💌 improvements in MATE Desktop 1.26**:

  * The Control Center features:
    * Improved Window Preferences dialog with a more **comprehensive window behaviour and placement options** presented.
    * Display preferences now has an option for **discrete display scaling**.
    * Power Manager has a new option to enable keyboard dimming.
    * Notifications now support for hyperlinks.
  * Caja can **format drives and has a new Bookmarks sidebar**.
  * **Caja Actions**, which allows you to add arbitrary programs to be launched through the context menu, is now part of the Desktop.
  * Calculator now uses GNU MPFR/MPC for **high precision, faster computation and additional functions**.
  * Pluma has a **new mini map instant overview**, a grid background to turn Pluma into a writing pad and the preferences have been redesigned.
  * Atril is much **faster scrolling through large documents and the memory footprint has been reduced**.
  * Engrampa, the archive manager, now **supports EPUB, ARC and encrypted RAR files**.
  * Marco, the windows manager:
    * Correctly restores minimised windows to their original position.
    * Thumbnail **window previews support HiDPI**.
  * Netspeed applet shows **more information about your network interfaces**.

While MATE Desktop is not completely ready for Wayland just yet, 1.26.0
represents a significant stepping stone towards that objective with **most of the
MATE Desktop being able to run on a Wayland compositor**. 👍

### Ubuntu MATE Enhancements

Ubuntu MATE has tweaked 🔧 the default desktop configuration slighty:

  * Image Extrapolation and Interpolation is disabled by default in Eye of MATE to make **image viewing faster and image quality sharper**.
  * The **Alt-Tab pop-up is now expanded** to fit long window titles.
  * If you use the **Mutiny layout, session loading is now faster**.

### Guest Session

Once in a while a friend, family member, or colleague may want to borrow your
computer 😱 The **Guest Session provides a convenient way, with a high level of
security, to lend your computer to someone else**. A guest session can be launched
either from the login screen or from within a regular session. If you are
currently logged in, click the icon at the far right of the menu bar and select
Guest Session. This will lock the screen for your own session and start the
guest session.

A **guest cannot view the home folders of other users, and by default any saved
data or changed settings will be removed/reset at logout**. It means that each
session starts with a fresh environment, unaffected by what previous guests did.

### RedShift

RedShift makes a return, after being temporarily removed in Ubuntu MATE 21.04.

## Raspberry Pi images

We will be refreshing our Ubuntu MATE images for Raspberry Pi in the coming
weeks.

## Major Applications

Accompanying **MATE Desktop 1.26.0** and **Linux 5.13** are **Firefox 93.0**,
**Celluloid 0.20**, **LibreOffice 7.2.1.2**

See the [Ubuntu 21.10 Release Notes](https://discourse.ubuntu.com/t/impish-indri-release-notes/21951)
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
