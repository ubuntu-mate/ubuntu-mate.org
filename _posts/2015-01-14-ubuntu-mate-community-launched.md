---
layout: blog-post
title: Ubuntu MATE Community launched
permalink: ubuntu-mate-community-launched
category: news
author: Martin Wimpress
lang: en
---

Some months ago [we asked if the Ubuntu MATE community was interested in expanding without using social networks](/blog/alternative-community-forum-poll/).
The answer was clear. Yes, you do. Then we asked [if the community would fund the required infrastructure and hosting](/blog/ubuntu-mate-community-donations/).
And you did! Thank you to everyone who became a monthly sponsor or
donated.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Join the Ubuntu MATE Community</h1>
        <p>The communications hub for Ubuntu MATE is now open.</p>
        <a href="https://ubuntu-mate.community" class="btn btn-primary btn-lg">Join the Community</a>
        </p>
    </div>
</div>

The Ubuntu MATE team decided to use [Discourse](http://www.discourse.org/)
to provide a community space. You can sign up for an account on the
our server or you can sign in with your social profiles if you want to.
Discourse has a responsive design so anyone can access the community
from any device, no apps required.

The Ubuntu MATE community will act as forum, wiki and also replaces
traditional mailing lists. When you sign up you'll receive a message
that explains how to get around Discourse and use its most common
features. Our hope is that the new Ubuntu MATE community site will
become the hub through which all Ubuntu MATE communication can flow.

## The server

A new quad core server with 4GB of RAM, 800GB RAID-6 Disk and 6TB
bandwidth has been deployed. It is running Ubuntu Server 14.04 LTS and
[Docker](https://www.docker.com) is running in a container.
[Mandrill](https://mandrillapp.com/) is integrated for email
notifications and [CloudFlare](https://www.cloudflare.com) provide
an edge caching CDN, application firewall and adds an additional layer
of spam prevention. The site is only available via https using TLS 1.0
(or higher), has [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
enabled and uses perfect forward secrecy (PFS). The webserver also has
[SPDY](https://developers.google.com/speed/spdy) enabled and
[StatusCake](https://www.statuscake.com) is used to monitor the site
availability and response times. At the time of writing the Ubuntu MATE
community site gets an [A+](https://www.ssllabs.com/ssltest/analyze.html?d=ubuntu%2dmate.community&s=104.28.25.88&latest)
rating from [SSL Labs](https://www.ssllabs.com).

We hope you enjoy the new Ubuntu MATE community. See you on the other side!
