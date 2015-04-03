<!--
.. title: Ubuntu MATE 15.04 Final Release
.. slug: ubuntu-mate-vivid-final-release
.. date: 2015-04-23 23:23:23 UTC
.. tags: Ubuntu,MATE,Vivid,draft
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

Ubuntu MATE 15.04 is now available for official download. This
release builds on Ubuntu MATE Beta 2 and fixes some bugs.

As usual preparing this release of Ubuntu MATE has been a team effort.
Special thanks to [Mike Gabriel](https://alioth.debian.org/users/sunweaver/),
[Vlad Orlov](https://github.com/monsta) and [Stefano Karapetsas](https://github.com/stefano-k)
for putting in a great deal of effort triaging bugs, doing code reviews and
creating new upstream MATE Desktop 1.8.x point releases. Thanks guys!

Thanks also to [Mathieu Trudel-Lapierre](https://launchpad.net/~mathieu-tl),
[Colin Watson](https://launchpad.net/~cjwatson), [Adam Conrad](https://launchpad.net/~adconrad)
and [Daniel Holbach](https://launchpad.net/~dholbach) for their patience and 
guidance that has helped fix and improve Ubuntu MATE.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 15.04 Beta 2 release?

Here is what changed since Ubuntu MATE 15.04 Beta 2:

  * Fixed Virtualbox guests only getting a resolution of 640x480
    * [LP: #1368784](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/).
  * Fixed corrupt Korean fonts in Ubiquity.
    * [LP: #1437961](https://bugs.launchpad.net/ubuntu-mate/+bug/1437961).
  * Fixed OEM Config.
    * [LP :#1436937](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1436937)

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

  * Once installation has finished, and the final Restart button is pressed, the screen freezes and becomes unresponsive. Pressing Enter which would normally do the reboot does nothing.
    * The computer will require a manual power off or reset after the disc has been ejected.
    * [LP: 1436816](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1436816)
  * It is not possible to install the Virtualbox drivers via the Additional Hardware application.
    * [LP: #1434579](https://bugs.launchpad.net/ubuntu/+source/software-properties/+bug/1434579)
    * The workaround is to open a shell and `sudo apt-get install virtualbox-guest-x11`.
  * You may not be able to enter your pass phrase if you use full disk encryption.
    * [LP: #1386005](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1386005)
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has already been reported. These issues will be addressed in due course.

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
