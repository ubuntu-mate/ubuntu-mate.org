<!--
.. title: Ubuntu MATE 14.10 Release Candidate
.. slug: ubuntu-mate-utopic-release-candidate
.. date: 2014-10-15 21:00:00 UTC
.. tags: Ubuntu,MATE,Utopic,release candidate
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

Ubuntu MATE 14.10 release candidate is now available for download.
This is the last release prior to the final 14.10 release and fixes
a few issues that were present in Beta2 please **make sure you read
the  release notes below** because there are still unresolved issues
you'll need to be aware of.

## What works?

Most things, more than in Beta2 at least. People tell us that Ubuntu
MATE is stable. You may, or may not, agree.

## What changed since Beta2?

This release candidate has been focused on fixing broken things and
improving what was already present in Beta2.

  * Fixed full disk encryption, or rather entering your pass phrase into Plymouth.
    * [LP #1382791](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1382791)
    * [LP #1359689](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1359689)
    * [LP #1362333](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1362333)
  * Fixed Plymouth not displaying boot up splash screens.
    * [LP #1376090](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1376090)
    * [LP #1372802](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1372802)
    * [LP #1370707](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1370707)
    * [LP #1368414](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1368414)
    * [LP #1356513](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1356513)
    * [LP #1343841](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1343841)
  * Fixed [missing Sticky Notes applet](https://bugs.launchpad.net/ubuntu-mate/+bug/1370048).
  * Merged xzoom menu entry upstream. [LP #1368188](https://bugs.launchpad.net/ubuntu/+source/xzoom/+bug/1368188)
  * Synced [mate-screensaver 1.8.1-1 from Debian](https://bugs.launchpad.net/ubuntu/+source/mate-screensaver/+bug/1378430)
  * Synced [marco 1.8.2 from Debian](https://bugs.launchpad.net/ubuntu/+source/marco/+bug/1378429)
  * Synced [mate-applets 1.8.1 from Debian](https://bugs.launchpad.net/ubuntu/+source/mate-applets/+bug/1378427)
  * Synced [atril 1.8.1 from Debian](https://bugs.launchpad.net/ubuntu/+source/atril/+bug/1378426)
  * Synced [caja 1.8.2 from Debian](https://bugs.launchpad.net/ubuntu/+source/caja/+bug/1378425)
  * Synced [mate-panel 1.8.1 from Debian](https://bugs.launchpad.net/ubuntu/+source/mate-panel/+bug/1378421)
  * Added caja-dropbox 1.8.0 to the PPAs.
  * Added mate-control-center to 1.8.3 to the PPAs.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 14.10 Release Candidate Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/utopic/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Upgrading from Beta2

If you have Beta2 installed, here is how to upgrade to the release
candidate.

Start a shell and update.

    sudo apt-get update
    
Complete the upgrade.    
    
    sudo apt-get dist-upgrade

Reboot, login, start a shell and clean up.

    sudo apt-get autoremove
    sudo apt-get autoclean

## Known Issues

Although Ubuntu MATE includes fixes for Plymouth (full disk encryption
and boot logo display) these are not official Ubuntu patches and
currently specific to Ubuntu MATE. If Ubuntu update the Plymouth packages
without fixing these issues then you may experience regressions in
Ubuntu MATE which, if you're using full disk encryption, could *"brick"*
your system.

So, while we've *"fixed"* full disk encryption we still don't recommend
you use it. Enabling home directory encryption is fully supported and
completely safe to use.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported:

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Testing

Ubuntu MATE 14.10 will be released on October 23rd and we need
people installing, using Ubuntu MATE and reporting any issues you may
find on the project's bug tracker.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

Is there anything you can help with or want to be involved in? Maybe
you just want to discuss your experiences or ask the maintainers some
questions. Please [come and talk to us](/community/).

