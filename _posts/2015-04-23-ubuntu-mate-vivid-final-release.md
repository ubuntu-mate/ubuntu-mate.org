<!--
.. title: Ubuntu MATE 15.04 Final Release
.. slug: ubuntu-mate-vivid-final-release
.. date: 2015-04-23 15:23:23 UTC
.. tags: Ubuntu,MATE,Vivid,Press Kit
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

<div class="bs-component">
    <div class="jumbotron">
        <h1>Achievement Unlocked!</h1>
        <p>If you didn't already know, Ubuntu MATE is now an official member of the Ubuntu family.</p>
        <p><img class="centered" src="/Ubuntu-MATE-Remix.png" alt="Ubuntu MATE" /></p>
    </div>
</div>

Ubuntu MATE 15.04 is now available for download. This release builds
on Ubuntu MATE Beta 2 and mostly fixes bugs.

As usual preparing this release of Ubuntu MATE has been a team effort.
Thanks to [Mike Gabriel](https://alioth.debian.org/users/sunweaver/),
[Vlad Orlov](https://github.com/monsta), [Mathieu Trudel-Lapierre](https://launchpad.net/~mathieu-tl),
[Martin Pitt](https://launchpad.net/~pitti), [Adam Conrad](https://launchpad.net/~adconrad)
and [Daniel Holbach](https://launchpad.net/~dholbach) for helping get the Ubuntu
MATE 15.04 release out the door. Thanks guys!

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## Ubuntu MATE 15.04 new features

Here is a run down of some of the new features in Ubuntu MATE 15.04
compared to Ubuntu MATE 14.10:

  * Ubuntu MATE 15.04 is an official Ubuntu flavour.
  * Established a hardware partnership with [Entroware](https://www.entroware.com).
  * Added PowerPC and [Raspberry Pi 2](/raspberry-pi/) as supported hardware architectures.
  * Added a new default theme called [Yuyo](https://github.com/snwh/yuyo-gtk-theme).
  * Added [user interface switching](https://youtu.be/YI4IWO_SpiI) to MATE Tweak.
  * Added [fully integrated Compiz support](https://youtu.be/k_nk02XELi4).
  * Added [Tilda pull-down terminal](https://youtu.be/_woWvmHl3Rc).
  * Added [Folder Color](https://youtu.be/ZrSVepoNuJk).
  * Added [LightDM GTK Greeter Settings](https://launchpad.net/lightdm-gtk-greeter-settings)
  * Added categories to the system menus.
  * Added new community contributed desktop backgrounds.
  * Updated to Linux 3.19
  * Updated to MATE Desktop 1.8.2.
  * Updated to Firefox 37.
  * Updated to LibreOffice 4.4.
  * Updated GTK 3.x themes to use full colour icons, like their GTK 2.x counter parts.
  * Updated all themes to offer improved Client Side Decoration (CSD) support.
  * Replaced Totem with VLC.
  * Replaced Cheese with guvcview.
  * Replaced `upstart` with `systemd`.
  * ...and many other minor improvements and bug fixes.

You can find the official Ubuntu release note here:

  * https://wiki.ubuntu.com/VividVervet/ReleaseNotes

## What changed since the Ubuntu MATE 15.04 Beta 2 release?

Here is what changed since Ubuntu MATE 15.04 Beta 2:

  * Updated Rhythmbox to 3.1
  * Updated Plank to 0.9.0
  * Updated `ubuntu-mate-artwork` to 0.4.7 which adds improved Client Side Decoration (CSD) support.
  * Fixed OEM install mode.
    * [LP :#1436937](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1436937)
  * Fixed Virtualbox guests only getting a resolution of 640x480.
    * [LP: #1368784](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/).
  * Fixed restarting the computer from the live session and upon completion of an install.
    * [LP: 1436816](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1436816)
    * Virtualbox guests still require a manual power off. [LP: #1447038](https://bugs.launchpad.net/bugs/1447038).
  * Fixed installing the Virtualbox X.org drivers via the Additional Hardware utility.
    * [LP: #1434579](https://bugs.launchpad.net/ubuntu/+source/software-properties/+bug/1434579)
  * Fixed corrupt Korean fonts in Ubiquity.
    * [LP: #1437961](https://bugs.launchpad.net/ubuntu-mate/+bug/1437961).
  * Fixed missing translations and incorrect window decorations when enabling Compiz in MATE Tweak.
    * [LP: #1433562](https://bugs.launchpad.net/ubuntu-mate/+bug/1433562).
    * [LP: #1441072](https://bugs.launchpad.net/ubuntu-mate/+bug/1441072).
  * Fixed auto-mounting devices formatted with exFat and connected via USB.
    * [LP: #1441728](https://bugs.launchpad.net/ubuntu-mate/+bug/1441728).
  * Fixed missing swap when using home directory encryption.
    * [LP: #953875](https://bugs.launchpad.net/ubuntu/+source/ecryptfs-utils/+bug/953875)
  * Fixed `mate-terminal.wrapper` so that home directory encryption passphrase can be recovered.
    * [LP: #1445198](https://bugs.launchpad.net/ubuntu-mate/+bug/1445198)
  * Fixed assorted MATE bugs in Debian that have been synced with Ubuntu.
    * [#781951](https://bugs.debian.org/781951).
    * [#780580](https://bugs.debian.org/780580).
    * [#781303](https://bugs.debian.org/781303).
    * [#781247](https://bugs.debian.org/781247).
    * [#781246](https://bugs.debian.org/781246).
    * [#780844](https://bugs.debian.org/780844).
    * [#782194](https://bugs.debian.org/782194).
    * [#782189](https://bugs.debian.org/782189).

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 15.04 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/vivid/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

It is not all good news however. Here are the known issues. All of which
affect every Ubuntu flavour.

  * You may not be able to enter your pass phrase if you use full disk encryption.
    * [LP: #1386005](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1386005)
  * Shutdown/Restart of the live session does not work in Virtualbox guest.
    * [LP: #1447038](https://bugs.launchpad.net/bugs/1447038)
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has already been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Useful Information

You may find the following information useful, which is why we titled the section
*Useful Information* since the information presented here is mostly useful.

  * [Ubuntu MATE 15.04 Useful Information](https://ubuntu-mate.community/t/ubuntu-mate-14-10-and-15-04-useful-information/24)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 15.04 Press Kit</h1>
        <p>If you are a publisher, blogger, Podcaster or Youtuber then you might find our press kit useful.</p>
        <a href="/ubuntu-mate-1504-presskit/" class="btn btn-primary btn-lg">Press Kit</a>
        </p>
    </div>
</div>
