---
layout: blog-post
class: blog
title: Ubuntu MATE server upgrades
permalink: /blog/ubuntu-mate-server-upgrades/
description:
category: news
author: Martin Wimpress
lang: en
---

The Ubuntu MATE website is now load-balanced across multiple countries. This
is in additional using [CloudFlare](https://www.cloudflare.com) for caching
at the network edge.

Twice last week ubuntu-mate.org experienced
[DDoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) attacks. Over
the weekend the new server infrastructure was deployed so that ubuntu-mate.org
is now load balanced across four servers in different countries. We also have
more DDoS counter measures in place and continue to make use of the European
CDN kindly sponsored by [First-Colo](https://www.first-colo.com/).

{:.center}
![First-Colo](/images/blog/sponsors/firstcolo.png)

We used this as an opportunity to add BitTorrent downloads for the [Raspberry
Pi 2 images](https://ubuntu-mate.org/raspberry-pi/) and updated the Ubuntu
MATE 14.04 torrents. Both now have 5 web-seeds in addition to those of you
generously seeding Ubuntu MATE.

Another benefit of this transition is that we no longer rely on Sourceforge
for serving downloads. Sourceforge also experienced an extended outage
recently and this impacted our ability to serve downloads for the Raspberry Pi
2 images. Given some of the recent actions by Sourceforge, we were
uncomfortable using them for file hosting.

Lastly all the embedded video on the site now uses HTML5 and the download
pages have been simplified and the Torrents are more prominently located.

None of this would have been possible without the kind donations from the
[Ubuntu MATE Patrons](https://www.patreon.com/ubuntu_mate) and the
generous contributions many of the Ubuntu MATE community have made via PayPal.

**Thank you!**

If you haven't donated to the Ubuntu MATE project and you get value from our
work please consider becoming a Patron or making a donation.

{% include blog/jumbotron.html
    title = "Support Ubuntu MATE"
    text = "Become a monthly supporter on **Patreon** or make a donation to help grow the Ubuntu MATE community."
    button_text = "Support Ubuntu MATE"
    button_url = "/donate/"
%}
