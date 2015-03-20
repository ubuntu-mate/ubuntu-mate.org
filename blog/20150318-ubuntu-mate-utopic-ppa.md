<!--
.. title: Ubuntu MATE 14.10 PPA Change
.. slug: ubuntu-mate-utopic-ppa
.. date: 2015-03-18 21:45:13 UTC
.. tags: Ubuntu,MATE,Utopic
.. link: 
.. description: Ubuntu MATE 14.10 has a new PPA, you must enable it.
.. type: text
.. author: Martin Wimpress
-->

### Ubuntu MATE 14.10 - Action Required

Since the release of the Ubuntu MATE 14.10 images the software update
PPAs have been re-organised. If you are running Ubuntu MATE 14.10 you
**must** do the following to ensure you get all the package updates.

    sudo apt-add-repository ppa:ubuntu-mate-dev/utopic-mate
    sudo apt-get update
    sudo apt-get dist-upgrade

This PPA was recently updated and now includes the current MATE 1.8 packages
and all the bugs that have been fixed by the MATE package maintainer for
Debian.
