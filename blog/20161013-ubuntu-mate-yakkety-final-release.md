<!--
.. title: Ubuntu MATE 16.10
.. slug: ubuntu-mate-yakkety-final-release
.. date: 2016-10-13 20:30:00 UTC
.. tags: Ubuntu,MATE,Yakkety,final,16.10,private
.. link:
.. description: Ubuntu MATE 16.10 (Yakkety Yak) Final Release
.. type: text
.. author: Martin Wimpress
-->

<div align="center">
<img src="/gallery/blog/ubuntu-mate-1610-final.png" alt="Ubuntu MATE 16.10 Final" /><br />
<b>As is now customary, our release artwork was made by <a href="https://www.youtube.com/channel/UCglkWuyZDppWD2BVsyI4r3A" target="_blank"><i>Ghost Sixtyseven</i></a>.</b>
</div>

# It's GTK3+ baby, all of it!

> **Ubuntu MATE 16.10 is, more or less, a from scratch re-working of Ubuntu
> MATE, not just to accomadate GTK3+ but to also make most packages
> shipped by default with Ubuntu MATE *"Recommeneded"*. This means most
> default applications can now be uninstalled without issue.**
>
> **The work to port MATE Desktop to GTK3+ has been ongoing for a couple
> of years and Ubuntu MATE is the first major distribution to ship a
> full GTK3+ implementation of the MATE Desktop. And the absolute latest
> release too, MATE Desktop 1.16! Firefox and LibreOffice are also GTK3+
> only in Yakkety.**
>
> **This has been no small undertaking, we've changed toolkits twice this
> cycle. First from GTK 2.24.x to GTK 3.18 and then to GTK 3.20. The
> themes have required two significant upgrades first to supprt GTK 3.18
> and again to support GTK 3.20. We've also upgraded through three MATE
> Desktop versions this cycle, 1.12 to 1.14, 1.14 to 1.15 and 1.15 to 1.16.**
>
> **We originally scheduled a complete migration to GTK3+ to conclude for
> the 17.04 release, but thanks to those of you who have generously
> supported the Ubuntu MATE crowd funding we've achieved that objective
> a full 6 months ahead of schedule!**
>
> **Ubuntu MATE have paid &euro;5653 to Open Source developers working
> on MATE Desktop and Ubuntu MATE projects during the six months of the
> Ubuntu MATE 16.10 development cycle. You, the Ubuntu MATE community,
> have made it possible to complete the migration to GTK3+ a full six
> months ahead of schedule!**
>
> **Thank you all for you continued support!**
> 
> *Martin Wimpress, Ubuntu MATE Project Leader.*

<div class="bs-component">
    <div class="jumbotron">
        <h1>Download Ubuntu MATE 16.10</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/download/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## What changed since the Ubuntu MATE 16.10 Beta 2 release?

This is what has been added, updated or removed.

  * **Upgraded to MATE Desktop 1.16.0**
    * The entire MATE Desktop suite has been upgraded to MATE Desktop 1.16.0
    * Many, many, bug fixes.
    * Translation updates.    
  * **Upgraded Ubuntu MATE Artwork 16.10.9**
    * Fix Firefox download progress bars. (LP: [#1630224](https://bugs.launchpad.net/bugs/1630224))
    * Fix Unlock button for Time and Date Settings. (LP: [#1630910](https://bugs.launchpad.net/bugs/1630910))
    * Fix Back/Forward navigation buttons in Yelp. (LP: [#1624574](https://bugs.launchpad.net/bugs/1624574))
    * Fix Firefox Search/Location entry box borders. (LP: [#1624738](https://bugs.launchpad.net/bugs/1624738))
    * Fix Firefox menu items.
    * Fix Advanced Menu themes to use flat elements. (LP: [#1630366](https://bugs.launchpad.net/bugs/1630366), [#1624755](https://bugs.launchpad.net/bugs/1624755))
    * Fix OSD colors. (LP: [#1630538](https://bugs.launchpad.net/bugs/1630538))
    * Fix LibreOffice toolbars and theme. (LP: [#1624571](https://bugs.launchpad.net/bugs/1624571), [#1550990](https://bugs.launchpad.net/bugs/1550990))
    * Fix symbolic icons for GtkExpander.
    * Fix Transmission progress bars. (LP: [#1624565](https://bugs.launchpad.net/bugs/1624565))
    * Fix Indicator Applet on transparent panels. (LP: [#1598159](https://bugs.launchpad.net/bugs/1598159))
  * **Upgraded to Ubuntu MATE Weclome 16.10.10**
    * Correct description for Adobe Flash. (LP: [#1630266](https://bugs.launchpad.net/bugs/1630266))
    * Add keyboard navigation support. (LP: [#1616203](https://bugs.launchpad.net/bugs/1616203))
    * Fix Getting Started sections not re-closing. (LP: [#1626909](https://bugs.launchpad.net/bugs/1626909))
    * Fix broken images in bulk queue. (LP: [#1626896](https://bugs.launchpad.net/bugs/1626896))
    * Fix notifications for bulk queue operations. (LP: [#1626899](https://bugs.launchpad.net/bugs/1626899))
    * Fix "Upgrade Installed Packages" button. (LP: [#1626907](https://bugs.launchpad.net/bugs/1626907))
    * Fix inoperable introduction links.
    * Fix Getting Started hints not appearing.
    * Hide "open at login" checkbox for live and guest sessions.
    * Remove ocenaudio. (LP: [#1613410](https://bugs.launchpad.net/bugs/1613410))
    * Remove duplicate navigation buttons.    
    * Many other minor fixes and finements.
  * **Upgraded to [MATE Dock Applet 0.75](https://github.com/robint99/mate-dock-applet/releases/tag/V0.75)**
    * Application actions now have their own popup window, which can be disabled if required.
    * Window list now appears in response to a click on an application icon when it has more than one window open.
    * Action lists and window list colours now match the panel.
    * Optional Compiz integration, to provide previews of an applications open windows.
    * Bug fixes.
  * Many other bug fixes including: 
    * Fixed booting PowerPC iso on PowerMac G5 7,3. (LP: [#1626332](https://bugs.launchpad.net/bugs/1626332))
    * Fixed LightDM Guest Session warning dialog. (LP: [#1627395](https://bugs.launchpad.net/bugs/1627395))
    * Fixed Display Preferences not working. (LP: [#1628209](https://bugs.launchpad.net/bugs/1628209))
    * Fixed changing the size of the MATE Terminal. (LP: [#1615443](https://bugs.launchpad.net/bugs/1615443))
    * Removed colour customisations (not supported in GTK3+) from Appearence Preferences. (LP: [#1626960](https://bugs.launchpad.net/bugs/1626960))
    * Removed background support (not supported in GTK3+) from Caja. (LP: [#1628180](https://bugs.launchpad.net/bugs/1628180))

## Known Issues

Here are the known issues.

### Ubuntu MATE issues

  * Nothing significant.

You'll also want to check the Ubuntu MATE bug tracker to see what has
already been reported.

  * [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

### Ubuntu family issues

This is our known list of bugs that affect all flavours.

  * Choosing an Entire Disk install on PowerPC may result in an unbootable system.
    * The work around is to manually partition your hard disk and create an `ext2` boot partition.
    * (LP: [#1606089](https://bugs.launchpad.net/bugs/1606089)),
    (LP: [#1607128](https://bugs.launchpad.net/bugs/1607128))

  * Ubiquity installer Slideshows and Ubuntu MATE Welcome display a blank window on PowerPC.
    * This is due to a bug in WebKit 2.
    * (LP: [#1561573](https://bugs.launchpad.net/bugs/1561573)),
    (LP: [#1597764](https://bugs.launchpad.net/bugs/1597764))  

  * R300 GPU accelerated graphics do not work on PowerPC
    * (LP: [#1432949](https://bugs.launchpad.net/bugs/1432949)),
    (LP: [#1575391](https://bugs.launchpad.net/bugs/1575391))

  * Running Linux on PowerPC can require some tinkering and the following are useful references.
    * [PowerPC Known Issues](https://wiki.ubuntu.com/PowerPCKnownIssues)
    * [PowerPC FAQ](https://wiki.ubuntu.com/PowerPCFAQ)

## Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).
