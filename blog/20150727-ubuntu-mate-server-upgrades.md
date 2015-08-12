<!-- 
.. title: Ubuntu MATE server upgrades
.. slug: ubuntu-mate-server-upgrades
.. date: 2015-07-27 06:01:09 UTC
.. tags: Ubuntu,MATE,infrastructure
.. link: 
.. description: 
.. type: text
-->

The Ubuntu MATE website is now load-balanced across multiple countries. This
is in additional using [CloudFlare](https://www.cloudflare.com) for caching
at the network edge.

Twice last week ubuntu-mate.org experienced 
[DDoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) attacks. Over 
the weekend the new server infrastructure was deployed so that ubuntu-mate.org 
is now load balanced across four servers in different countries. We also have 
more DDoS counter measures in place and continue to make use of the European
CDN kindly sponsored by [First-Colo](https://www.first-colo.com/).

<div class="row">
  <div class="col-lg-12">
    <div class="well bs-component">
    <a href="https://www.first-colo.com/"><img class="centered" src="/assets/img/sponsors/firstcolo.png" alt="First-Colo" /></a>
    </div>
  </div>
</div>

We used this as an opportunity to add BitTorrent downloads for the [Raspberry 
Pi 2 images](https://ubuntu-mate.org/raspberry-pi/) and updated the Ubuntu 
MATE 14.04 torrents. Both now have 5 web-seeds in addition to those of you 
generously seeding Ubuntu MATE.

<div class="row">
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://can.ubuntu-mate.net/">
        <img src="/assets/img/flags/Canada-Flag-128.png" alt="Canada" title="Canada" />
      </a>
      <p>Canadian mirror</p></p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://fra.ubuntu-mate.net/">
        <img src="/assets/img/flags/France-Flag-128.png" alt="Frane" title="France" />
      </a>
      <p>French mirror</p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://ger.ubuntu-mate.net/">
        <img src="/assets/img/flags/Germany-Flag-128.png" alt="Germany" title="Germany" />
      </a>
      <p>German mirror</p>
    </div>
  </div>
  <div class="col-lg-3">
    <div class="well bs-component text-center">
      <a href="http://ita.ubuntu-mate.net/">
        <img src="/assets/img/flags/Italy-Flag-128.png" alt="Italy" title="Italy" />
      </a>
      <p>Italian mirror</p>
    </div>
  </div>
</div>

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

<div class="bs-component">
    <div class="jumbotron">
        <h1></h1>
        <p>Become a monthly supporter at <a href="http://www.patreon.com/ubuntu_mate">Patreon</a>
        or make a donation to help grow the Ubuntu MATE community.</p>
        <a href="donate/" class="btn btn-primary btn-lg">Support Ubuntu MATE</a>
        </p>
    </div>
</div>
