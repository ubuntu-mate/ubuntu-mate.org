<!--
.. title: Ubuntu MATE 14.04.2 Release
.. slug: ubuntu-mate-trusty-14.04.2-release
.. date: 2015-03-23 21:54:37 UTC
.. tags: Ubuntu,MATE,Trusty,final
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

Ubuntu MATE 14.04.2 is available for download. This release fixes a few
issues that were present in 14.04.1, adds some new features and
updates some packages.

It is important to state quite clearly **Ubuntu MATE 14.04.2 is not an
official Ubuntu flavour!** Although we now have official status for 15.04,
it is not retroactive. Ubuntu MATE 14.04 will always be an unofficial build.

We would have preferred that this release was made on Februaty 20th when the
official flavours shipped 14.04.2. However, we were in the middle of some time
critical activities to ensure Ubuntu MATE 15.04 official status, so decided to
let 14.04.2 slip until we had time to finish it. We hope you understand.

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 14.04.1 release?

There are advantages and disadvantages to maintaining an unofficial Ubuntu 
derivative. The downside is that we have not been able to integrate all of
the hardware enablement stack in Ubuntu MATE 14.04.2. We have only integrated
the Linux 3.16 kernel, but not the updated Xorg stack. During our testing
we found many issues with the Xorg HWE stack, such as Virtualbox Guest Additions
and the Ubuntu SDK not being compatible. These issues are not specific to Ubuntu
MATE.

The upside of maintaining an unofficial Ubuntu deriative is that we can roll
out new features and package updates. So we did, most notably LibreOffice
4.4.1.2.

The advantage of the newer Linux kernel is that it resolves most
of the screen tearing issues some people experienced in Ubuntu MATE
14.04.1. The surprise inclusion of Compiz (although it is not enabled
by default) is also to help provide tear free video for those with
graphics hardware capable of running Compiz. The MATE profile for Compiz
also comes with the Enhanced Zoom plugin enabled in order to satisfy
visually impaired individuals who require a high quality screen
magnifier. The screen zooming keybindings are `<Super>m` to zoom in
and `<Super>n` to zoom out.

He is what we've changed.

  * Updated to Linux 3.16.0-33
  * Updated to Firefox 36
  * Updated to LibreOffice 4.4.1.2
  * Updated to [LightDM GTK Greeter](http://smdavis.us/projects/lightdm-gtk-greeter/) 2.0.0 which now includes a MATE logo in the session switcher.
  * Updated MATE specific autostart files and configuration so they do not conflict with other desktop environments.
  * Updated the built-in languages.
    * `en` `es` `pt` `bn` `fr` `hi` `ja` `zh-hans`
  * Added [LightDM GTK Greeter Settings](https://launchpad.net/lightdm-gtk-greeter-settings) 1.10. Thanks to [Sean M. Davis](http://smdavis.us)
  * Fixed sound themes. Thanks to [Sergio Schneider](https://plus.google.com/116549967007914384885/about) of the [Ubunt MATE Updated project](http://sourceforge.net/projects/uumate/)
  * Fixed auto-login on first boot if auto-login was selected during the install.
  * Enabled X zapping via `Ctrl+Alt+Backspace`. 
  * Enabled touch to click by default for touchpads.
  * Enabled Qt accessibility modules when a MATE session is detected.
  * Backported GTK 2.24.27.
  * Backported Ubiquity compatibility features for MATE from 15.04.
  * Backported Compiz compatibility features for MATE from 15.04.
    * MATE Tweak can be used to live switch between Compiz and Marco, no log out/in required.
  * Backported MATE Tweak from 15.04.
  * Backported MATE Menu from 15.04.
  * Backported the `cloudtop` meta package from 15.04 which is suitable for remote terminal deployment.
  * All MATE package updates from Debian 8.0 have been synced to Ubuntu MATE 14.04 and 14.10.
    * [#774546](https://bugs.debian.org/774546), [#775212](https://bugs.debian.org/775212),
    [#775261](https://bugs.debian.org/775261), [#776689](https://bugs.debian.org/776689),
    [#776698](https://bugs.debian.org/776698), [#777311](https://bugs.debian.org/777311),
    [#778278](https://bugs.debian.org/778278), [#778816](https://bugs.debian.org/778816),
    [#778817](https://bugs.debian.org/778817), [#778824](https://bugs.debian.org/778824),
    [#778826](https://bugs.debian.org/778826), [#778835](https://bugs.debian.org/778835),
    [#776698](https://bugs.debian.org/776698), [#779719](https://bugs.debian.org/779719),
    [#779821](https://bugs.debian.org/779821), [#779848](https://bugs.debian.org/779848),
    [#779856](https://bugs.debian.org/779856), [#779916](https://bugs.debian.org/779916),
    [#780104](https://bugs.debian.org/780104), [#780210](https://bugs.debian.org/780210),
    [#780226](https://bugs.debian.org/780226), [#780399](https://bugs.debian.org/780399)

Excluding the Kernel and LibreOffice updates, these updates have been rolled out 
to existing Ubuntu MATE 14.04.1 installs.

You may also want to review the changes that were made in stock Ubuntu 14.04.2.

  * [14.04.2 Update Packages](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes#Updated_Packages)
  * [14.04.2 Change Summary](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/ChangeSummary/14.04.2)

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE 14.04 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/trusty/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Useful Information

You may find the following information useful, which is why we titled 
the section *Useful Information* since the information presented here
is mostly useful.

  * [Ubuntu MATE 14.04 LTS Useful Information](https://ubuntu-mate.community/t/ubuntu-mate-14-04-lts-useful-information/25)

## Known Issues

  * Virtualbox guests may only get a resolution of 640x480
    * [LP: #1368784](https://bugs.launchpad.net/ubuntu/+source/virtualbox/+bug/1368784/), see [comment #13](https://b$
    * Use `System -> Preferences -> Additional Drivers` to install the
    Virtualbox drivers that will correct the resolution.

You'll also want to check the Ubuntu MATE bug tracker to see what
has already been reported. These issues will be addressed in future
development cycles.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

Please report any issues you may find on the project's bug tracker
so we can improve future releases.

## Feedback

Is there anything you can help with or want to be involved in? Maybe
you just want to discuss your experiences or ask the maintainers some
questions. Please [come and talk to us](/community/).
