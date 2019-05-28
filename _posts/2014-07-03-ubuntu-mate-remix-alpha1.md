<!-- 
.. title: Ubuntu MATE Remix Alpha1
.. slug: ubuntu-mate-remix-alpha1
.. date: 2014-07-03 16:25:00 UTC
.. tags: Ubuntu,MATE,alpha1
.. link: 
.. description: 
.. type: text
.. author: Martin Wimpress
-->

**Yes, it's here and it's *very* alpha. So, be nice. Please!**

<div class="bs-component">
    <div class="jumbotron">
        <h1>Ubuntu MATE Remix Alpha1 Download</h1>
        <p>Join the fun and experience a retrospective future.</p>
        <a href="/utopic/" class="btn btn-primary btn-lg">Download</a>
        </p>
    </div>
</div>

## What works?

Most things.

The .iso image should boot (from DVD or USB), the Live session should work,
the installer should work and the installed system should also work. Notice
the heavy use of *"should*", YMMV.

## Known Issues

The is an alpha project, running on an alpha distribution that was put together
by a novice [Debian](http://www.debian.org) and [Ubuntu](http://www.ubuntu.com)
contributor. *That's alpha squared!*

Some things are broken, we know that, and you will doubtless find plenty more
broken things we haven't discovered yet. The following is known to be broken:

  * Network Manager applet doesn't auto start. The can be worked around by removing
  the `AutostartCondition` line in `/etc/xdg/autostart/nm-applet.desktop`.
  * ISO does not boot on a UEFI computer. [LP #1337604](https://bugs.launchpad.net/ubuntu-mate/+bug/1337604)
  * Some applets don't use the mono icons. [LP #1337577](https://bugs.launchpad.net/ubuntu-mate/+bug/1337577)
  * Some theming in the Live session is not correct.
  * Probably a whole heap more.

If you spot any other issues please report them on the project's bug tracker. 

  * [Ubuntu MATE Remix Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

We are particularly interested in real computer hardware and printer compatibility.

Is there anything you can help with or want to be involved in? Maybe you
just want to discuss your experiences or ask the maintainers some questions.
Please [come and talk to us](/community/).
