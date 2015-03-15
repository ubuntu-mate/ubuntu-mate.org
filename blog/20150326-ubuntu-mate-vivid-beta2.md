<!--
.. title: Ubuntu MATE 15.04 Beta 2
.. slug: ubuntu-mate-vivid-beta2
.. date: 2015-03-26 17:30:37 UTC
.. tags: Ubuntu,MATE,Vivid,beta,draft
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->


Ubuntu MATE 15.04 Beta 2 is now available for official download. This
release builds on Ubuntu MATE Beta 1 by making a few changes and
addressing some bugs.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 15.04 Beta 1 release?

Here is what changed since Ubuntu MATE 15.04 Beta 1:

  * Fixed the "Notification Area" crashing on i386. [LP: #1425401](https://bugs.launchpad.net/ubuntu/+source/mate-panel/+bug/1425401)
  * Added some community contributed wallpapers from [Ghost Sixtyseven](https://ubuntu-mate.community/t/three-wallpapers-for-consideration/449).
  * Added MATE Menu to Ubuntu MATE and also uploaded it to the official Ubuntu archive.
    * This release also includes many new translations.
  * Added MATE Tweak to Ubuntu MATE and also uploaded it to the official Ubuntu archive.
    * This release also includes many new translations.
  * Enabled Qt accessibility modules when a MATE session is detected.
  * Enabled `systemd` as the default init system. [LP: #1427654](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/1427654).
  * Updated Yuyo, Ambiant-MATE, Radiant-MATE themes to override symbolic icons with full colour icons.
  * Updated MATE specific autostart files and configuration so they do not conflict with other desktop environments. (LP: #1426862)
  * Updated available languages.
    * `en` `es` `pt` are available on all architectures
    * `bn` `fr` `hi` `ja` `zh-hans` are available on all except PowerPC.
  * Replaced Cheese with guvcview.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 15.04 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/vivid/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Known Issues

It is not all good news however. Here are the known issues.

  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)
  * MATE 1.8x is not fully compatible with `glibc` >= 2.43.1 which now features
  in Ubuntu 15.04. The MATE team have been working on patches but they have not yet
  made there way into the official Ubuntu archive. Therefore the following
  PPA should be enabled to get the fixes. You *really* want to do this:

    sudo apt-add-repository ppa:ubuntu-mate-dev/vivid-mate
    sudo apt-get update
    sudo apt-get dist-upgrade

  * Live switching between Compiz and Marco is somewhat experimental and may result in
  no window decorations on some older GPUs.
  * Virtualbox guests may only get a resolution of 640x480
    * [LP: #1368784](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/), see [comment #13](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/comments/13) for a work around.
  * Running an Ubuntu MATE live session as a Virtualbox guest may corrupt the video
  output of the guest.
    * You can correct the video display by pressing `Host+F1` to switch
    VT in the guest and then press `Host+F7` to switch back which will
    correct the video output.

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Useful Information

You may find the following information useful, which is why we titled 
the section *Useful Information* since the information presented here
is mostly useful.

  * [Ubuntu MATE 15.04 Useful Information](https://ubuntu-mate.community/t/ubuntu-mate-14-10-and-15-04-useful-information/24)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
