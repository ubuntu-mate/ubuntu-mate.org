<!--
.. title: Ubuntu MATE 14.10 Release
.. slug: ubuntu-mate-utopic-final-release
.. date: 2014-10-23 19:13:37 UTC
.. tags: Ubuntu,MATE,Utopic,final
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

The Ubuntu MATE 14.10 final release is now available for download.
This release fixes a few issues that were present in the release
candidate but **make sure you read the release notes below**.

## Thank you

I'd just like to take this opportunity to thank the following people
for helping create this inaugural release of Ubuntu MATE. These are the
shoulders upon which I stand:

**Stefano Karapetsas, Alan Pope, Sam Hewitt, Sander Sweers, Mike Gabriel,
Abel McClendon, Steve Zesch, John Paul Adrian Glaubitz, Goce Mitevski,
Ivan Pejić, Jack Mohegan, Riccardo Pecchioli, Brett Wiley, Caleb Howland,
Jonathan Nadeau, Daniel Holbach, Colin Watson, Iain Lain, Luke Velvich,
Kendell Clark, Kyle Brouhard, Erich Eickmeyer, James Pellerano,
Steve Radonich IV and Stephen Morrish.**

And, thanks to the community. Thanks for showing an interest in Ubuntu
MATE. Thanks for using Ubuntu MATE. Thanks for filing bug reports. Thanks
for your suggestions. Thanks for testing. And most importantly, thanks
for your contributions and creating a solid community on which we
can build.

Thank you!

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the release candidate?

This release has fixed a few minor issues and tweaked a couple
things.

  * Full disk encryption, or rather entering your pass phrase into Plymouth,
  was properly fixed by the Ubuntu team. 
  * Fixed missing configuration options in the workspace switcher applet [LP #1382682](https://bugs.launchpad.net/ubuntu-mate/+bug/1382682)
  * Fixed the live session not auto logging into the MATE desktop.
  * Added a background wall paper to Ubiquity.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 14.10 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/utopic/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Upgrading from the release candidate

If you have the release candidate installed, here is how to upgrade
to the final release.

Start a shell and update.

    sudo apt-get update
    
Complete the upgrade.    
    
    sudo apt-get dist-upgrade

Upgrade Plymouth.

    sudo apt-get install \
    plymouth=0.9.0-0ubuntu7 \
    plymouth-label=0.9.0-0ubuntu7 \
    plymouth-theme-ubuntu-text=0.9.0-0ubuntu7

Reinstall Plymouth themes.

    sudo apt-get --reinstall install plymouth-theme-ubuntu-mate-text
    sudo apt-get --reinstall install plymouth-theme-ubuntu-mate-logo

Reboot, login, start a shell and clean up.

    sudo apt-get autoremove
    sudo apt-get autoclean

## Known Issues

  * Plymouth not displaying boot up splash screens.
    * [LP #1376090](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1376090)
    * [LP #1372802](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1372802)
    * [LP #1370707](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1370707)
    * [LP #1368414](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1368414)
    * [LP #1356513](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1356513)
    * [LP #1343841](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1343841)

You'll also want to check the Ubuntu MATE bug tracker to see what
has already been reported. These issues will be addressed in future
development cycles.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Please report any issues you may find on the project's bug tracker
so we can improve future releases.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

Is there anything you can help with or want to be involved in? Maybe
you just want to discuss your experiences or ask the maintainers some
questions. Please [come and talk to us](/community/).
