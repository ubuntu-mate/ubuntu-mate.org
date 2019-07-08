---
layout: blog-post
class: blog
title: Ubuntu MATE 15.10 Final Release
permalink: /blog/ubuntu-mate-wily-final-release
category: release
author: Martin Wimpress
lang: en
---

{% include blog/youtube.html
    embed = "https://www.youtube.com/embed/KEHxHr-Ih9w?html5=1&#amp;rel=0&amp;showinfo=0"
%}

## What works?

People tell us that Ubuntu MATE is stable. You may, or may not, agree.

## What changed since the Ubuntu MATE 15.10 Beta 2 release?

Here's what changed in Ubuntu MATE 15.10 since Beta 2.

  * Fixed `update-manager` and `do-release-upgrade` to upgrade from Ubuntu MATE 15.04 to Ubuntu MATE 15.10.
    * Although this is not supported on the Raspberry Pi 2 images.
  * Fixed the openSUSE panel layout, GNOME Main Menu no longer crashes.
  * Fixed `ubi-timezone` error in Ubiquity.
  * Fixed Caja undelete, which was causing Caja to crash or fail to undelete.
  * Updated MATE Tweak to 3.5.2a
    * Remove all deprecated GTK properties.
    * Make irrelevant UI elements insensitive rather than being hidden.
    * Fix retaining the current theme settings when switching to Metacity.
    * Fix Plank not being left running when saving a custom theme.
    * Fix leaving multiple volume applets enabled when switching panel layouts.
    * Fix CTRL+C not closing MATE Tweak.
  * Updated Ubuntu MATE Welcome to 1.0.3.5
    * Removed Simple Screen Recorder, it is not compatible with Ubuntu MATE 15.10 or any 15.10 flavour.
    * Remove Synapse, it has an intermitent issue resulting in segmentation fault on Ubuntu MATE 15.10.
  * Updated the boot screen artwork in the ISO image. Bigger, more consistent, and higher contrast for visually impaired users.
  * Updated Plank to 0.10.1.
  * Prepared Ubuntu MATE 15.10 for the Raspberry Pi 2.

{% include blog/jumbotron.html
    title = "Ubuntu MATE 15.10 Download"
    text = "Join the fun and experience a retrospective future."
    button_text = "Download"
    button_url = "/wily/"
%}

## Raspberry Pi 2

We are delighted to release Ubuntu MTE 15.10 for the Raspberry Pi 2 on
release day along side the other supported architectures.
You can find out more and download the image from the [Ubuntu MATE Raspberry Pi page](/raspberry-pi/).

{:.center}
![Raspberry Pi logo](/images/blog/Logos/raspberry-pi.png)
**Ubuntu MATE 15.10 is also available for the Raspberry Pi 2**

## Thanks

Thanks to everyone who contributed to Ubuntu MATE 15.10. A side from
the [core team](/team/) there are few people who deserve a public
*"Thank you!"*

### Community

Many thanks to [David Chadderton](https://ubuntu-mate.community/users/webspresso/activity)
from [Webspresso](http://webspresso.co.uk/), [Rohith Madhavan](https://ubuntu-mate.community/t/ubuntu-mate-wallpapers/965),
[quidsup](http://quidsup.net/wallpaper/show.php?i=Neon-UbuntuMATE),
[Tim Apple](http://timapple.com/), Jack Mohegan and
[Linux Scoop](http://linuxscoop.com/) for the new community contributed artwork and videos.

Thank you to Luke Horwell for adding the animations, transitions and
categorisation to Ubuntu MATE Welcome. Thanks to Larry Bushey, from
[Going Linux](http://goinglinux.com/) podcast, for adding and updating
the content for Introduction and Features in Ubuntu MATE Welcome. Thanks
also to [Matt Hartley](http://www.matthartley.com/), from
[Freedom Penguin](http://freedompenguin.com/), for helping with the
Ubuntu MATE Welcome Software selection.

Thanks to [Joe Ressington](http://joeress.com/about),
[Isaac Carter](http://twitter.com/stupidcoder) and
[Albert Hickey](http://plus.google.com/+Winkleink), from
[The Pi Podcast](http://thepipodcast.com/), for testing Ubuntu MATE
15.10 for the Raspberry Pi 2. You really helped ironout some kinks and
improved the release quality for everyone.

Lastly, thanks to everyone who has reported issues, provided feedback or
donated to Ubuntu MATE. Your feedback has been vital to understanding
what improvements people most want to see. We do listen, so keep the
feedback coming.

### Canonical

In addition to the efforts of the Ubuntu MATE team and the Ubuntu MATE
community, we are also grateful for the help and support we've recieved
from the following Canonical employees:

  * [Adam Conrad](https://launchpad.net/~adconrad)
  * [Adam Stokes](https://launchpad.net/~adam-stokes)
  * [Alan Pope](https://launchpad.net/~popey)
  * [Colin Watson](https://launchpad.net/~cjwatson)
  * [Daniel Holbach](https://launchpad.net/~dholbach)
  * [Didier Roche](https://launchpad.net/~didrocks)
  * [Iain Lane](https://launchpad.net/~laney)
  * [Łukasz Zemczak](https://launchpad.net/~sil2100)
  * [Martin Pitt](https://launchpad.net/~pitti)
  * [Mathieu Trudel-Lapierre](https://launchpad.net/~mathieu-tl)
  * [Michael Hall](https://launchpad.net/~mhall119)
  * [Oliver Grawert](https://launchpad.net/~ogra)
  * [Sebastien Bacher](https://launchpad.net/~seb128)
  * [Stephen M. Webb](https://launchpad.net/~bregma)

## Known Issues

Here are the known issues.

  * These are the [Known Issue for Ubuntu MATE 15.10](https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuMATE#Known_issues).
  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

You'll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

{% include blog/jumbotron.html
    title = "Ubuntu MATE 15.10 Press Kit"
    text = "If you are a publisher, blogger, Podcaster or Youtuber then you might find our press kit useful."
    button_text = "Press Kit"
    button_url = "/ubuntu-mate-1510-presskit/"
%}
