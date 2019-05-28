<!--
.. title: Ubuntu MATE Beta1
.. slug: ubuntu-mate-beta1
.. date: 2014-08-28 19:04:11 UTC
.. tags: Ubuntu,MATE,beta1
.. link:
.. description:
.. type: text
.. author: Martin Wimpress
-->

Ubuntu MATE Beta1 is released and represents a big step forward 
compared to Alpha2, not least because Ubuntu MATE is now sporting new 
themes and artwork to give it a distinctive look. A number of bugs have 
also been fixed along the way and a few new ones have been introduced, 
**so make sure you read the release notes below**.

## What changed since Alpha2?

Mostly Beta1 has been focused on adding artwork to give Ubuntu MATE its
own identity but improvements have been made and some bugs have been
fixed too.

  * Added community contributed wallpapers from [Goce Mitevski](https://github.com/gocemitevski/ubuntu-mate-wallpapers/) and [Ivan Pejić](https://github.com/nadrimajstor/ubuntu-mate-theme).
  * Added community contributed Plymouth theme from [Jack Mohegan](https://plus.google.com/101312215214323407176/posts/2dyVkArfx49).
  * Added community contributed SYSLINUX theme contributed from [Ivan Pejić](https://github.com/nadrimajstor/syslinux-themes-ubuntu-mate).
  * Added community contributed Ubiquity slides from [Jack Mohegan](https://plus.google.com/101312215214323407176/posts/2dyVkArfx49).
  * Added Ambiant-MATE and Radiant-MATE desktop and icon themes.
  * Added Ubuntu MATE LightDM theme.
  * Added [OpenDyslexic](http://opendyslexic.org/) a font created to increase readability for readers with dyslexia.
  * Added a screen magnifier for individuals with low vision.
  * Added patent-free S3TC compatible implementation that provides texture compression to Mesa.
  * Added service discovery on a local network via the mDNS/DNS-SD protocol suite.
  * Added `colord` to manage, install and generate accurate colour profiles.
  * Added `ntp` time synchronisation daemon.
  * Added `policykit-desktop-privileges` which fixes, among other things, auto mounting of disks without requiring a password.
  * Added a PAM module that will automatically unlock the keyrings using your login password, making gnome-keyring usage transparent without losing its security benefits.
  * Added GVFS backend (FTP, SSH, WebDAV, Samba) to Déjà Dup.
  * Added GStreamer backend to LibreOffice.
  * Fixed hiding the `im-config` icon from MATE.
  * Improved support for 3G/4G USB dongles.
  * Improved support for iPods and MTP devices.
  * Improved on-demand codec installation.
  * Improved hardware detection and support.
  * Improved .iso image mastering to ensure consistency with official Ubuntu flavours.
  * Improved meta packages and added `ubuntu-mate-live` for handling packages that are only required in the Live CD.
  * Updated the default Qt4 style to match the Ambiant-MATE theme.
  * Updated the language packs in the Live CD based on the Top 10 countries that visit <https://ubuntu-mate.org>.
  * Updated ubuntu-mate.org website content and improved the screenshot slideshow.
  * Updated ubuntu-mate.org webserver to deliver all content over SSL/TLS using [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security), [PFS](https://www.eff.org/deeplinks/2013/08/pushing-perfect-forward-secrecy-important-web-privacy-protection) and (when possible) [SPDY](http://en.wikipedia.org/wiki/SPDY).
  * Removed `ffmpegthumbnailer`, `light-themes` and `ubuntu-artwork`.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE Beta1 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/utopic/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## Upgrading from Alpha2

Some of the package selections and default settings have changed since 
Alpha2. If you have Alpha2 installed, here is how to upgrade to Beta1.

Start a shell and upgrade.

    sudo apt-get update
    sudo apt-get dist-upgrade

Remove some obsolete packages.

    sudo apt-get remove adium-theme-ubuntu light-themes ubuntu-wallpapers

Overlay some Ubuntu MATE configuration files.

    rsync -av /etc/skel/.config/ ~/.config/
    rsync -av /etc/skel/.local/ ~/.local/

Reboot, login, start a shell and clean up.

    sudo apt-get autoremove
    sudo apt-get autoclean

Finally set up the default Ubuntu MATE appearance.

  * Go to `System -> Preferences -> Appearance` and select the 
  'Ambiant-MATE' theme. Click the `Backgrounds` tab and select the
  'Ubuntu MATE Cold' wallpaper.

## Known Issues

Ubuntu MATE 14.10 is currently in beta and we are aware of the 
following issues.

  * Full disk encryption *may* not work. This is an [upstream bug in Plymouth](https://bugs.freedesktop.org/show_bug.cgi?id=80553)
  that can prevent your passphrase from being accepted.
    * Home directory encryption does work.
  * Plymouth does not display the boot time splash screens. This is an upstream bug. [LP #1343841 ](https://bugs.launchpad.net/ubuntu/+source/plymouth/+bug/1343841)
  * Currently the `Try Ubuntu MATE without installing` option does not work due to an upstream bug. [LP #1355966](https://bugs.launchpad.net/ubuntu/+source/systemd-shim/+bug/1355966)
  * EFI computers may encounter a black screen during boot up and the system will not be usable. This is an upstream bug. [LP #1353989 ](https://bugs.launchpad.net/ubuntu/+source/systemd-shim/+bug/1353989)
  * You may experience some video corruption when running in a VirtualBox guest.
    * See below for a workaround.

### Reporting issues

If you spot any other issues please report them on the project's bug 
tracker. 

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Testing

Ubuntu MATE Beta2 will be released at the end of September therefore we
need people installing, using Ubuntu MATE and reporting any issues you
may find on the project's bug tracker.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

Is there anything you can help with or want to be involved in? Maybe
you just want to discuss your experiences or ask the maintainers some
questions. Please [come and talk to us](/community/).
