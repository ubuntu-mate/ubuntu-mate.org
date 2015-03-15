<!-- 
.. title: Ubuntu MATE Remix sprint
.. slug: ubuntu-mate-remix-sprint
.. date: 2014-06-29 20:11:18 UTC
.. tags: Ubuntu,MATE
.. link: 
.. description: 
.. type: text
.. author: Martin Wimpress
-->

Earlier this week [popey](http://popey.com) and I met up for a one day 
development sprint to try and make some headway with Ubuntu MATE Remix.
We did manage to make a good deal of progress. So, what did we achieve?

## Achievements unlocked

  * Development is now hosted on Launchpad - <http://launchpad.net/ubuntu-mate/>
  * The Ubuntu MATE Remix .iso images are now built using seeds and germinate. 
  While this is currently only possible using a meta package in
  [our PPA](https://launchpad.net/~ubuntu-mate-dev/+archive/ppa), this
  technique is consistent with the official Ubuntu flavour builds.
  * Fixed the Ambiance and Radiance themes to work with MATE 1.8.1.
  * The Ubuntu MATE Remix package selection is pretty much complete and offers
  a *"pure"* MATE desktop environment on top of Ubuntu. The testing .iso images do
  not include anything of Unity, indicators or Comppiz by default. Wide hardware
  support, including VirtualBox, has been integrated.
  * The application selections are mostly consistent with the default applications
  that shipped in Ubuntu 14.04 LTS.
  * Created this super-amazing website. Yes, it needs work and will be improved in due course.

## Locked levels

These are the main issues we need to work on:

  * Get LightDM to auto login to the LiveCD session.
  * Fork the `livecd-rootfs`, merge the Ubuntu MATE Remix modifications,
  build a revised package in our PPA and modify the .iso image builder accordingly.
  * Release .iso images for testing.
  * Ubuntu MATE Remix Plymouth boot themes and Ubiquity slides.
  * Coordinate merging the Ubuntu MATE Remix seeds, tasks and `livecd-rootfs`
  changes upstream.
  * Testing, lots of testing. In particular hardware and printer compatibility.

Is there anything you can help with or want to be involved in? If so please
[get in touch](/community/).
