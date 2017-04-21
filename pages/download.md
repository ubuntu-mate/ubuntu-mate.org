<!--
.. title: Download Ubuntu MATE
.. slug: download
.. date: 2016-04-04 10:00:00 UTC
.. tags: Ubuntu,MATE,download
.. link:
.. description: Download Ubuntu MATE
.. type: text
.. author: Luke Horwell
-->

## Download
The Ubuntu MATE .iso image allows you to try Ubuntu MATE without changing your 
computer at all, with an option to install it permanently later. You will need 
at least 512MB of RAM to install from this image.
<hr />

<noscript>
<div class="alert alert-danger">
<h3>Please enable JavaScript to continue.</h3>
<p>This download page uses JavaScript to populate the download links
and relevant information, but it is disabled for this browser.</p>
<p>Alternately, you can access most links from
[Canonical's CD Image Server](http://cdimage.ubuntu.com/ubuntu-mate/releases/).</p>
</div>
</noscript>

<style>
#arch-list .well {
margin: 0;
padding: 16px;
color: black;
cursor: pointer;
}

#arch-list a:hover {
text-decoration: none;
}

.well.active {
border: 2px solid #9AB270;
color: #fff !important;
background-color: #87a556 !important;
}
</style>

<div id="release-list">
<p><b>Choose a Release:</b></p>
<ul id="release" class="nav nav-pills" role="tablist"><li id="xenial" role="presentation"><a href="#xenial" role="tab" data-toggle="tab"><big><img src="/favicon-32.png"/> Ubuntu MATE 16.04.2 LTS</big></a></li>
<li id="yakkety" role="presentation"><a href="#yakkety" role="tab" data-toggle="tab"><big><img src="/favicon-32.png"/> Ubuntu MATE 16.10</big></a></li>
<li id="zesty" role="presentation"><a href="#zesty" role="tab" data-toggle="tab"><big><img src="/favicon-32.png"/> Ubuntu MATE 17.04</big></a></li>
</ul>
</div>

<div id="arch-list" class="row" hidden>
<hr>
<p><b>Choose your Architecture:</b></p>
<a id="amd64" onclick="selected_amd64()">
<div class="col-xs-3 well bs-component">
<h3>64-bit</h3>
<p>
Ideal for computers with:
<ul>
<li>More than 3 GB of RAM.</li>
<li>64-bit capable Intel and AMD processors</li>
<li>UEFI PCs booting in CSM mode.</li>
<li>Modern Intel-based Apple Macs</li>
</ul>
</p>
</div>
</a>
<a id="i386" onclick="selected_i386()">
<div class="col-xs-3 well bs-component">
<h3>32-bit</h3>
<p>
Ideal for computers with:
<ul>
<li>Less than 2 GB of RAM.</li>
<li>Intel and AMD processors.</li>
<li>Ageing PCs with low-RAM resources.</li>
<li>Older Intel-based Apple Macintosh systems.</li>
</ul>
</p>
</div>
</a>
<a id="powerpc" class="xenial yakkety " onclick="selected_powerpc()">
<div class="col-xs-3 well bs-component">
<h3>PowerPC</h3>
<p>
Designed for old generation PowerPC-based hardware, like:
<ul>
<li>Apple Macintosh G3, G4 and G5</li>
<li>Apple iBooks and PowerBooks</li>
<li>IBM OpenPower 7xx Machines</li>
</ul>
</p>
</div>
</a>
<a id="armhf" class="xenial " onclick="selected_armhf()">
<div class="col-xs-3 well bs-component">
<h3>Raspberry Pi</h3>
<p>
For aarch32 (ARMv7) computers, like:
<ul>
<li>Raspberry Pi 2</li>
<li>Raspberry Pi 3</li>
</ul>
</p>
</div>
</a>
</div>
<hr />

<div id="download-links" class="row" hidden>
<div id="release-notes" class="row">
<div class="col-xs-3">
<div class="text-center">
<img src="/favicon-144.png" alt="Ubuntu MATE">
</div>
</div>
<div class="col-xs-9">
<h3><span id="present-version"></span> for <span id="present-arch"></span> systems.</h3>
<p>See what's new and any other important information for this release.</p>
<p><a class="xenial" href="https://ubuntu-mate.org/blog/ubuntu-mate-xenial-final-release/"><span class="fa fa-file"></span> Release Announcement</a></p>
<p><a class="yakkety" href="/blog/ubuntu-mate-yakkety-final-release/"><span class="fa fa-file"></span> Release Announcement</a></p>
<p><a class="zesty" href="/blog/ubuntu-mate-zesty-final/"><span class="fa fa-file"></span> Release Announcement</a></p>

<p><a class="rpi" href="/raspberry-pi/"><img src="/images/logos/raspberry-pi.png" width="16px" height="16px"> Learn More</a></p>
<p><a class="rpi" href="/raspberry-pi-change-log/"><img src="/images/logos/raspberry-pi.png" width="16px" height="16px"> What's New?</a></p>
<div class="alert alert-success xenial-amd64 xenial-i386 xenial-powerpc " hidden><p><b><span class="fa fa-info-circle"></span> This release has Long Term Support (LTS)</b></p><p>Recommended if you desire a stable system. Support ends <b>April 2019</b>.</p></div>
<div class="alert alert-info yakkety-amd64 yakkety-i386 yakkety-powerpc yakkety-armhf " hidden><p><b><span class="fa fa-info-circle"></span> This is an intermediate release</b></p><p>Suitable for people who want to keep up with the latest developments in Ubuntu MATE and Open Source. Support ends <b>July 2017</b>.</p></div>
<div class="alert alert-info zesty-amd64 zesty-i386 zesty-powerpc zesty-armhf " hidden><p><b><span class="fa fa-info-circle"></span> This is an intermediate release</b></p><p>Suitable for people who want to keep up with the latest developments in Ubuntu MATE and Open Source. Support ends <b>January 2018</b>.</p></div>

</div>
</div>
<hr />

<div id="bittorrent" class="row">
<div class="col-xs-3">
<div class="text-center">
<img src="../assets/img/downloads/torrent.png" alt="BitTorrent">
</div>
</div>
<div class="col-xs-9">
<h3>Via Torrent</h3>
<p>If you can spare the bytes, a torrent is the recommended method to download Ubuntu MATE.</p>
<p>
<a class="xenial-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04.2/release/ubuntu-mate-16.04.2-desktop-amd64.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04.2-desktop-amd64.iso.torrent</a>
<a class="xenial-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04.2/release/ubuntu-mate-16.04.2-desktop-i386.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04.2-desktop-i386.iso.torrent</a>
<a class="xenial-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04.1-desktop-powerpc.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04.1-desktop-powerpc.iso.torrent</a>
<a class="xenial-armhf" href="https://ubuntu-mate.org/raspberry-pi/ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz.torrent</a>
<a class="yakkety-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/release/ubuntu-mate-16.10-desktop-amd64.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.10-desktop-amd64.iso.torrent</a>
<a class="yakkety-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/release/ubuntu-mate-16.10-desktop-i386.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.10-desktop-i386.iso.torrent</a>
<a class="yakkety-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/release/ubuntu-mate-16.10-desktop-powerpc.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.10-desktop-powerpc.iso.torrent</a>
<a class="zesty-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/17.04/release/ubuntu-mate-17.04-desktop-amd64.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-17.04-desktop-amd64.iso.torrent</a>
<a class="zesty-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/17.04/release/ubuntu-mate-17.04-desktop-i386.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-17.04-desktop-i386.iso.torrent</a>

</p>
<p>
<a class="xenial-amd64" href="magnet:?xt=urn:btih:405b66f2130e504c0d9bae20dd7c5d53a74f2c0b&dn=ubuntu-mate-16.04.2-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="xenial-i386" href="magnet:?xt=urn:btih:f3ae641b8297ef79cab706a4b760a487eae2af8a&dn=ubuntu-mate-16.04.2-desktop-i386.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="xenial-powerpc" href="magnet:?xt=urn:btih:f29b7235363d0456f52aaf8eb8b748e980837305&dn=ubuntu-mate-16.04.1-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="xenial-armhf" href="magnet:?xt=urn:btih:d0f23c109d8662a3fe9338f75839af8d57e5d4a9&dn=ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="yakkety-amd64" href="magnet:?xt=urn:btih:e249fe4dc957be4b4ce3ecaac280fdf1c71bc5bb&dn=ubuntu-mate-16.10-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="yakkety-i386" href="magnet:?xt=urn:btih:bee8a636e86ad0270d27a91d183c8912e1176ae1&dn=ubuntu-mate-16.10-desktop-i386.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="yakkety-powerpc" href="magnet:?xt=urn:btih:5c8427c3ad8c0a84f7d09f266ffb73cb58bf9625&dn=ubuntu-mate-16.10-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="zesty-amd64" href="magnet:?xt=urn:btih:17e03ce12145d3cd308a203c53731f9845929239&dn=ubuntu-mate-17.04-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="zesty-i386" href="magnet:?xt=urn:btih:c822889553580c896f73da3fdc48610af48e50dc&dn=ubuntu-mate-17.04-desktop-i386.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a title="Opens your BitTorrent client. This method is trackerless and doesn't utilize web seeds. The true peer to peer option.">
<span class="fa fa-info-circle"></span>
</a>
</p>
</div>
</div>
<hr />

<div class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../assets/img/downloads/download-tips.png" alt="Download Tip">
</div>
</div>
<div class="col-xs-9">
<br>
<h3>Download Tip</h3>
<p>
<b>A little bit can go a long way.</b> If everyone who downloaded Ubuntu MATE donated <b>$2.50</b>
it would fund the full-time development of Ubuntu MATE and MATE Desktop.
<u>Please help both projects flourish by showing your support with a tip.</u>
</p>
<div class="row"><div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.1 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.1 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.1 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.1 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04.2 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="yakkety-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="zesty-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 17.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
</div>
<p><b>Powered by </b> <img src="../assets/img/logos/pp-logo-100px.png" height="24px"/></p>
<p>
<b>To donate more, donate with BitCoin or become an Ubuntu MATE Patron
<a href="https://ubuntu-mate.org/donate/">please visit the donate page</a>.</b>
</p>
</div>
</div>
<hr />

<div id="direct-download" class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../assets/img/downloads/direct-download.png" alt="Direct Download">
</div>
</div>
<div class="col-xs-9">
<h3>Via Direct Download</h3>
<p>If preferred, you can also download the images over HTTP.</p>
<p>
<a class="xenial-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04.2/release/ubuntu-mate-16.04.2-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04.2-desktop-amd64.iso</a>
<a class="xenial-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04.2/release/ubuntu-mate-16.04.2-desktop-i386.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04.2-desktop-i386.iso</a>
<a class="xenial-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04.1-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04.1-desktop-powerpc.iso</a>
<a class="yakkety-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/release/ubuntu-mate-16.10-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.10-desktop-amd64.iso</a>
<a class="yakkety-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/release/ubuntu-mate-16.10-desktop-i386.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.10-desktop-i386.iso</a>
<a class="yakkety-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/release/ubuntu-mate-16.10-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.10-desktop-powerpc.iso</a>
<a class="zesty-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/17.04/release/ubuntu-mate-17.04-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-17.04-desktop-amd64.iso</a>
<a class="zesty-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/17.04/release/ubuntu-mate-17.04-desktop-i386.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-17.04-desktop-i386.iso</a>

<img class="rpi" src="../images/flags/bytemark-16.png" width="16px" height="16px"/>&nbsp;
<a class="xenial-armhf" href="https://ubuntu-mate.org/raspberry-pi/ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz" onclick="thanks()"><b>Bytemark</b> - ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz</a>

<br class="rpi" />
</p>
<p>
<b>Download Size:</b>
<span class="xenial-amd64">1.7 GB</span>
<span class="xenial-i386">1.7 GB</span>
<span class="xenial-powerpc">1.7 GB</span>
<span class="xenial-armhf">1.2 GB</span>
<span class="yakkety-amd64">1.7 GB</span>
<span class="yakkety-i386">1.7 GB</span>
<span class="yakkety-powerpc">1.7 GB</span>
<span class="zesty-amd64">1.7 GB</span>
<span class="zesty-i386">1.7 GB</span>

</p>
<p>
<b>SHA256 Checksum:</b>
<code class="xenial-amd64">39cb4d4069dd79a9104b8c1c5d0d4a5b009779eec55fafeceafcf43c7ebcaba4</code>
<code class="xenial-i386">4bfe56e59e565088264590ad930130c4e872b1806c34fd6a7202752852961355</code>
<code class="xenial-powerpc">59ee1a0bfd9995aa71edeb8c011536c815b6980392b527ae243c2a5835b8d43d</code>
<code class="xenial-armhf">dc3afcad68a5de3ba683dc30d2093a3b5b3cd6b2c16c0b5de8d50fede78f75c2</code>
<code class="yakkety-amd64">6d64b911a2bda877ad7e8131bc88abe8e49c69842d69f5818d1b54f01849e451</code>
<code class="yakkety-i386">d99cfac02954d5ac23f2e9e78e1a50695a49efeb2e0dd336d653c1ec4191ce10</code>
<code class="yakkety-powerpc">a0518aa8f03dc3c3a1e0ec4a4d89af489419b21c400d0dd7fe87afa9d17346ac</code>
<code class="yakkety-armhf"></code>
<code class="zesty-amd64">acfcf1ab54946c67e99e0503c23385e697046fae45e393661d501100844d9a5d</code>
<code class="zesty-i386">8415711f8085f2c25341261e9503355be53a6871f8ffc96ada62884b1ee4d00b</code>
<code class="zesty-powerpc"></code>
<code class="zesty-armhf"></code>

</p>
<p><a href="../how-to-verify-downloads"><span class="fa fa-question-circle"></span> How to verify downloads</a></p>
<div class="rpi">
<span class="fa fa-heart"></span>
Many thanks to <a href="https://www.bytemark.co.uk/r/ubuntu-mate/"><b>Bytemark</b></a> for sponsoring all the hosting and bandwidth costs for the Ubuntu MATE downloads of the Raspberry Pi images.
<div class="row">
<div class="col-lg-3">&nbsp;</div>
<div class="col-lg-6">
<div class="well bs-component">
<a href="http://www.bytemark.co.uk/r/ubuntu-mate"><img class="centered" src="/images/sponsors/bytemark.png" alt="Bytemark" /></a>
</div>
</div>
<div class="col-lg-3">&nbsp;</div>
</div>        
</div>      
</div>
</div>
<hr />

<div id="sponsor1" class="row">
<div class="col-xs-3">
<div class="text-center">
<br><br>
<img src="../images/sponsors/osdisc.png" alt="OSDisc.com">
</div>
</div>
<div class="col-xs-9">
<h3>Purchase DVDs and USBs</h3>
<h4><b>OSDisc.com</b></h4>
<p>OSDisc.com is a leading source for Linux DVDs and USBs. Purchase ready-to-use bootable
DVDs and memory sticks that come pre-installed with Ubuntu MATE and have persistent storage.</p>
<p>
<a href="https://www.osdisc.com/products/ubuntumate?affiliate=ubuntumate">
<span class="fa fa-shopping-cart"></span> Purchase
</a>
</p>
</div>
</div>
<br />

<div id="sponsor2" class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../images/merch/hellotux/flash-drive.png" alt="HelloTux Flash Drive">
</div>
</div>
<div class="col-xs-9">
<h4><b>HELLOTUX</b></h4>
<p>HELLOTUX sell an Ubuntu MATE branded 8GB Metallic Unibody USB stick that is just 41 mm
long and less than 5 mm thick. It’s the perfect flash drive for your key ring, always
with you. HELLOTUX will also help you to upgrade your flash drive to the next version
of Ubuntu MATE, absolutely free.</p>
<p>
<a href="https://www.hellotux.com/ubuntumate1510_flash_drive">
<span class="fa fa-shopping-cart"></span> Purchase
</a>
</p>
</div>
</div>
<hr/>

<div id="getting-started" class="row">
<div class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../assets/img/downloads/getting-started.png" alt="Getting Started">
</div>
</div>
<div class="col-xs-9">
<br>
<h3>Getting Started</h3>
<p>The following resources may be useful to help get you up and running.</p>
<p>
<ul>
<li><a href="../how-to-create-bootable-usb-drive"><span class="fa fa-usb"></span> Creating a bootable USB on Windows, Mac and GNU/Linux</a></li>
<li><a href="https://help.ubuntu.com/community/BurningIsoHowto"><span class="fa fa-dot-circle-o"></span> Burning a DVD on Windows, Mac and GNU/Linux</a></li>
<li><a href="../about/#hardware_requirements"><span class="fa fa-laptop"></span> Check your System Requirements</a></li>
</ul>
</p>
</div>
</div>
</div>
<hr />

<div id="mirrors" class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../assets/img/logos/i18n-small.png" alt="Mirrors and Other Options">
</div>
</div>
<div class="col-xs-9">
<h3>Mirrors and Other Options</h3>
<p>You might prefer to find a DVD image on a mirror server that is geographically
close to you in order to achieve a faster download.</p>
<p>
<a target="_blank" href="https://launchpad.net/ubuntu/+cdmirrors">
<span class="fa fa-globe"></span> List Official Mirrors
</a>
</p>
<p><a class="xenial" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04.2/release/" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads for 16.04.2</a>
<a class="yakkety" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/release/" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads for 16.10</a>
<a class="zesty" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/17.04/release/" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads for 17.04</a>
</p>
</div>
</div>
<hr id="mirrors-hr" />
</div>

<script src="https://code.jquery.com/jquery-1.12.2.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-XdYbMnZ/QjLh6iI4ogqCTaIjrFk87ip+ekIjefZch0Y+PvJ8CDYtEs1ipDmPorQ+" crossorigin="anonymous">

<script>
<!-- JQuery -->
if (typeof jQuery == 'undefined') {
document.write(unescape("%3Cscript src='/assets/js/jquery-2.0.0.min.js' type='text/javascript'%3E%3C/script%3E"));
}

<!-- Bootstrap -->
if ( typeof($.fn.modal) === 'undefined') {
document.write('<script src="/assets/js/bootstrap.min.js"><\/script>')
}
$.fn.modal || document.write('<script src="">\x3C/script>')
</script>

<script>
// # Set variables
var version = {xenial: "xenial", yakkety: "yakkety", zesty: "zesty"};
var arch = {amd64: "amd64", i386: "i386", powerpc: "powerpc", armhf: "armhf"};


// # Set defaults
var show_version = "x";
var show_arch = "x";
var present_version = "x"
var present_arch = "x"

function updatePage() {
var v1, a1, v2, a2;
for (v1 in version) {
v2 = version[v1];
$('.' + v2).hide();
for (a1 in arch) {
a2 = arch[a1];
$('.' + v2 + '-' + a2).hide();
$('#' + a2 + ' .well').removeClass('active');
}
}
$('.' + show_version).show();
$('.' + show_version + '-' + show_arch).show();
$('#' + show_arch + ' .well').addClass('active');
$('#present-version').html(present_version)
$('#present-arch').html(present_arch)
$('#download-links').slideUp('fast');
}

// Run this when page loads.
updatePage();

function showDownloadLinks() {
$('#download-links').slideDown();
$('#mirrors').show();
$('#mirrors-hr').show();
$('.rpi').hide();
}

function thanks() {
$('#getting-started').slideDown('slow');
$('#getting-started-hr').show();
}

// Selecting a distro version
$( "#xenial" ).click(function() {show_version = "xenial";present_version = "Ubuntu MATE 16.04.2 LTS";updatePage();$('#arch-list').slideDown();});
$( "#yakkety" ).click(function() {show_version = "yakkety";present_version = "Ubuntu MATE 16.10";updatePage();$('#arch-list').slideDown();});
$( "#zesty" ).click(function() {show_version = "zesty";present_version = "Ubuntu MATE 17.04";updatePage();$('#arch-list').slideDown();});


// Selecting an architecture
function selected_i386() {
show_arch = "i386";
present_arch = "32-bit";
updatePage();
showDownloadLinks();
}

function selected_amd64() {
show_arch = "amd64";
present_arch = "64-bit";
updatePage();
showDownloadLinks();
}

function selected_powerpc() {
show_arch = "powerpc";
present_arch = "PowerPC";
updatePage();
showDownloadLinks();
}

function selected_armhf() {
show_arch = "armhf";
present_arch = "Raspberry Pi 2 and 3";
updatePage();
showDownloadLinks();
$('#mirrors').hide();
$('#mirrors-hr').hide();
$('.rpi').show();
}

</script>

<script>
// http://netnix.org/2014/04/27/tracking-downloads-with-google-analytics/
window.onload = function() {
var a = document.getElementsByTagName('a');
for (i = 0; i < a.length; i++) {
if (a[i].href.match(/^https?:\/\/.+\.(bz2|deb|gz|iso|pdf|torrent|xz|zip)$/i)) {
a[i].setAttribute('target', '_blank');
a[i].onclick = function() {
ga('send', 'event', 'Downloads', 'Click', this.getAttribute('href'));
};
}
}
}
</script>


