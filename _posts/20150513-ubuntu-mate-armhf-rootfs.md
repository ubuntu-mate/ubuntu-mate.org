<!--
.. title: Ubuntu MATE 15.04 generic ARMv7 root file system
.. slug: ubuntu-mate-vivid-armhf-rootfs
.. date: 2015-05-13 23:32:23 UTC
.. tags: Ubuntu,MATE,armhf
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

<img class="right" src="/assets/img/logos/arm-cpu.png" alt="ARM CPU"/>

The Ubuntu MATE team have made a generic Ubuntu MATE 15.04 root file system for 
ARMv7 devices. This root file system is intended for ARMv7 enthusiasts and 
board manufacturers who'd like to make an Ubuntu MATE image for their device(s). 
In order to adapt the root file system for your device you'll need to:

  * Add a boot loader
  * Add a kernel
  * Add X.org 1.17 drivers
  * Add any other hardware specific configuration

We've created some instructions and example build scripts based on the work we
did to make [Ubuntu MATE 15.04 for the Raspberry Pi 2](/raspberry-pi/). The
instructions are brief but hopefully sufficient for ARM device hackers to get
started.

  * [Ubuntu MATE for ARMv7 documentation and downloads](/armhf-rootfs/)
  * [Ubuntu MATE for ARMv7 build scripts](https://bitbucket.org/ubuntu-mate/ubuntu-mate-armhf)

We'd love to see Ubuntu MATE images for more ARMv7 devices. We will gladly host
the images and catalogue what the community creates on this website. If you start
working on, or create, an Ubuntu MATE image for an ARMv7 device then please let
us know in the [Ubuntu MATE Development Discussion](https://ubuntu-mate.community/c/development-discussion) forum.

If you have any improvements, or add support for a new device, then please submit
a pull request to our [BitBucket](https://bitbucket.org/ubuntu-mate/ubuntu-mate-armhf).
