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
Download a copy of the .iso image to try Ubuntu MATE without changing your
computer at all, and optionally install permanently later.
<hr>

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
<ul id="release" class="nav nav-pills" role="tablist"><li id="xenial" role="presentation"><a href="#xenial" role="tab" data-toggle="tab"><big><img src="/favicon-32.png"/> Ubuntu MATE 16.04 LTS</big></a></li>
<li id="wily" role="presentation"><a href="#wily" role="tab" data-toggle="tab"><big><img src="/favicon-32.png"/> Ubuntu MATE 15.10</big></a></li>
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
<a id="powerpc" onclick="selected_powerpc()">
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
<a id="armhf" onclick="selected_armhf()">
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
<hr>

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
<p><a class="wily" href="/blog/ubuntu-mate-wily-final-release/"><span class="fa fa-file"></span> Release Announcement</a></p>

<p><a class="rpi" href="/raspberry-pi/"><img src="/images/logos/raspberry-pi.png" width="16px" height="16px"> Learn More</a></p>
<p><a class="rpi" href="/raspberry-pi-change-log/"><img src="/images/logos/raspberry-pi.png" width="16px" height="16px"> What's New?</a></p>
<div class="alert alert-success xenial-amd64 xenial-i386 xenial-powerpc " hidden><p><b><span class="fa fa-info-circle"></span> This release has Long Term Support (LTS)</b></p><p>Recommended if you desire a stable system. Support ends <b>in 2019</b>.</p></div>

</div>
</div>
<hr>

<div id="getting-started" class="row" hidden>
<div class="row">
<div class="col-xs-3"></div>
<div class="col-xs-9"><h2>Thank you for downloading.</h2></div>
</div>

<div class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../assets/img/downloads/getting-started.png" alt="Getting Started Resources">
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
<hr id="getting-started-hr" hidden>

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
<a class="xenial-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04-desktop-amd64.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04-desktop-amd64.iso.torrent</a>
<a class="xenial-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04-desktop-i386.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04-desktop-i386.iso.torrent</a>
<a class="xenial-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04-desktop-powerpc.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04-desktop-powerpc.iso.torrent</a>
<a class="xenial-armhf" href="https://ubuntu-mate.org/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz.torrent</a>
<a class="wily-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/ubuntu-mate-15.10-desktop-amd64.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-15.10-desktop-amd64.iso.torrent</a>
<a class="wily-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/ubuntu-mate-15.10-desktop-i386.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-15.10-desktop-i386.iso.torrent</a>
<a class="wily-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/ubuntu-mate-15.10-desktop-powerpc.iso.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-15.10-desktop-powerpc.iso.torrent</a>
<a class="wily-armhf" href="https://ubuntu-mate.org/raspberry-pi/ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz.torrent" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz.torrent</a>

</p>
<p>
<a class="xenial-amd64" href="magnet:?xt=urn:btih:56b88ad5991641a48890fcdd04f068b3f6c0ba66&dn=ubuntu-mate-16.04-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="xenial-i386" href="magnet:?xt=urn:btih:c070b72287790164236c9e80134391b7e864261a&dn=ubuntu-mate-16.04-desktop-i386.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="xenial-powerpc" href="magnet:?xt=urn:btih:d64ca895d6778f6d50503d6229f276f101920cb4&dn=ubuntu-mate-16.04-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="xenial-armhf" href="magnet:?xt=urn:btih:92c9b38d58124e7771de2113227e05003b7144d0&dn=ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="wily-amd64" href="magnet:?xt=urn:btih:cd45dbf7e17267362dab3adc76320038abc710b9&dn=ubuntu-mate-15.10-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="wily-i386" href="magnet:?xt=urn:btih:78eca987c4fa1941c84895740565a8d99ce85e92&dn=ubuntu-mate-15.10-desktop-i386.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="wily-powerpc" href="magnet:?xt=urn:btih:4dba4714d94f7818d9a5d7bca84a754ce11eb53e&dn=ubuntu-mate-15.10-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a class="wily-armhf" href="magnet:?xt=urn:btih:01fa02661144c6a26ff09cb7a9bceb1c48716972&dn=ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>
<a title="Opens your BitTorrent client. This method is trackerless and doesn't utilize web seeds. The true peer to peer option.">
<span class="fa fa-info-circle"></span>
</a>
</p>
</div>
</div>
<hr>

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
<b>A little bit can go a long way.</b> If everyone who downloaded Ubuntu MATE donated $2.50
it would fund the full-time development of Ubuntu MATE and MATE Desktop.
Please help both projects flourish by showing your support with a tip.
</p>
<div class="row"><div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="xenial-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 16.04 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-amd64 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 amd64 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-i386 col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 i386 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-powerpc col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for PowerPC Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$2.50</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="2.50">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$5</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="5">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$10</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="10">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
<div class="wily-armhf col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$20</b></button></fieldset>
<input type="hidden" name="cmd" value="_xclick">          <input type="hidden" name="business" value="6282B4CZGVCB6">          <input type="hidden" name="item_name" value="Ubuntu MATE 15.10 for Raspberry Pi 2 and 3 Download Tip">          <input type="hidden" name="no_shipping" value="1">          <input type="hidden" name="no_note" value="1">          <input type="hidden" name="charset" value="UTF-8">          <input type="hidden" name="amount" value="20">          <input type="hidden" name="currency_code" value="USD">          <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1">           <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">           <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
</form></div>
</div>
<p><b>Powered by </b> <img src="../assets/img/logos/pp-logo-100px.png" height="24px"/></p>
<p>
To donate more or become an Ubuntu MATE patron
<a href="https://ubuntu-mate.org/donate/">please visit the donate page</a>.
</p>
</div>
</div>
<hr>

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
<a class="xenial-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04-desktop-amd64.iso</a>
<a class="xenial-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04-desktop-i386.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04-desktop-i386.iso</a>
<a class="xenial-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/ubuntu-mate-16.04-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-16.04-desktop-powerpc.iso</a>
<a class="wily-amd64" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/ubuntu-mate-15.10-desktop-amd64.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-15.10-desktop-amd64.iso</a>
<a class="wily-i386" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/ubuntu-mate-15.10-desktop-i386.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-15.10-desktop-i386.iso</a>
<a class="wily-powerpc" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/ubuntu-mate-15.10-desktop-powerpc.iso" onclick="thanks()"><span class="fa fa-download"></span> ubuntu-mate-15.10-desktop-powerpc.iso</a>

<img class="rpi" src="../images/flags/European-Union-Flag-16.png" width="16px" height="16px"/>&nbsp;
<a class="xenial-armhf" href="https://ubuntu-mate.r.worldssl.net/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz" onclick="thanks()"><b>European CDN</b> - ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz</a>
<a class="wily-armhf" href="https://ubuntu-mate.r.worldssl.net/raspberry-pi/ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz" onclick="thanks()"><b>European CDN</b> - ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz</a>

<br class="rpi">
<img class="rpi" src="../images/flags/Canada-Flag-16.png" width="16px" height="16px"/>&nbsp;
<a class="xenial-armhf"  href="http://can.ubuntu-mate.net/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz" onclick="thanks()"><b>Canadian Mirror</b> - ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz</a>
<a class="wily-armhf"  href="http://can.ubuntu-mate.net/raspberry-pi/ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz" onclick="thanks()"><b>Canadian Mirror</b> - ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz</a>

<br class="rpi">
<img class="rpi" src="../images/flags/France-Flag-16.png" width="16px" height="16px"/>&nbsp;
<a class="xenial-armhf" href="http://fra.ubuntu-mate.net/raspberry-pi/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz" onclick="thanks()"><b>French Mirror</b> - ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz</a>
<a class="wily-armhf" href="http://fra.ubuntu-mate.net/raspberry-pi/ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz" onclick="thanks()"><b>French Mirror</b> - ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz</a>

</p>
<p>
<b>Download Size:</b>
<span class="xenial-amd64">1.6 GB</span>
<span class="xenial-i386">1.6 GB</span>
<span class="xenial-powerpc">1.7 GB</span>
<span class="xenial-armhf">1.1 GB</span>
<span class="wily-amd64">1.2 GB</span>
<span class="wily-i386">1.2 GB</span>
<span class="wily-powerpc">1.2 GB</span>
<span class="wily-armhf">994 MB</span>

</p>
<p>
<b>SHA256 Checksum:</b>
<code class="xenial-amd64">ec19ba1280e5a05b78a863f3844864a8b0a3b4336028bcfbf143ad4fda44f2c3</code>
<code class="xenial-i386">549bdf46fb959f0374e5e3de6b85b350226d930f50decba7c4aad64804a8e750</code>
<code class="xenial-powerpc">a2c24cd68f2cbaf320f048cd3e3b22eddc0b721fdfde8defe626d92a313cebca</code>
<code class="xenial-armhf">bf7c85d0a25c8f27313a4bc47d4ceb32a9082390b18651af247d9757abebd21a</code>
<code class="wily-amd64">caf12e840f33eae535332b98d4491ce3f36e2c32cb4196a2e08209f39d626dec</code>
<code class="wily-i386">6a5f118dff0539779693a9d0560a503e3e90a7352099a86bf84afcca3c342f95</code>
<code class="wily-powerpc">56fa37086e950a3055e638fdef2fb58de78b45c917bc7adb7e577c602e324463</code>
<code class="wily-armhf">49ac8dfb73c203fe698a1a3c139b5cbec023c0d567253998e942d1fa236bbb94</code>

</p>
<p><a href="../how-to-verify-downloads"><span class="fa fa-question-circle"></span> How to verify downloads</a></p>
<div class="rpi">
<span class="fa fa-heart"></span>
Many thanks to First Colo for contributing the hosting and bandwidth for the Ubuntu MATE downloads
for the Raspberry Pi images.
</div>
</div>
</div>
<hr>

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
<br>

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
<hr>

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
<p><a class="xenial" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04/release/" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads for 16.04</a>
<a class="wily" href="http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads for 15.10</a>
</p>
</div>
</div>
<hr id="mirrors-hr">
</div>

<div class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../assets/img/downloads/community.png" alt="Community">
</div>
</div>
<div class="col-xs-9">
<br>
<h3>Get Involved</h3>
<p>Stop by to share your experiences, ask questions and discuss topics
with other users and developers in our growing community.</p>
<p><a href="https://ubuntu-mate.community"><span class="fa fa-comments"></span> Meet the Community</a></p>
</div>
</div>
<hr>

<div class="row">
<div class="col-xs-3">
<div class="text-center">
<br>
<img src="../assets/img/downloads/bugs.png" alt="Bug Tracker">
</div>
</div>
<div class="col-xs-9">
<br>
<h3>Found a bug?</h3>
<p>Please submit your detailed and reproducable bug reports to Launchpad
so that the relevant developers can fix them in future updates.</p>
<p><a href="https://bugs.launchpad.net/ubuntu-mate"><span class="fa fa-bug"></span> View Bug Tracker</a></p>
</div>
</div>
<br>

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
var version = {xenial: "xenial", wily: "wily"};
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
$('#getting-started').slideUp('fast');
$('#getting-started-hr').hide();
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
$( "#xenial" ).click(function() {show_version = "xenial";present_version = "Ubuntu MATE 16.04 LTS";updatePage();$('#arch-list').slideDown();});
$( "#wily" ).click(function() {show_version = "wily";present_version = "Ubuntu MATE 15.10";updatePage();$('#arch-list').slideDown();});


// Selecting an architecture
function selected_i386() {
show_arch = "i386";
present_arch = "i386";
showDownloadLinks();
updatePage();
}

function selected_amd64() {
show_arch = "amd64";
present_arch = "amd64";
showDownloadLinks();
updatePage();
}

function selected_powerpc() {
show_arch = "powerpc";
present_arch = "PowerPC";
showDownloadLinks();
updatePage();
}

function selected_armhf() {
show_arch = "armhf";
present_arch = "Raspberry Pi 2 and 3";
showDownloadLinks();
updatePage();
$('#mirrors').hide();
$('#mirrors-hr').hide();
$('.rpi').show();
}

</script>


