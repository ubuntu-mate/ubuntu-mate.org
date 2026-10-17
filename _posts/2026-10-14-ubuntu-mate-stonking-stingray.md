---
layout: blog-post
class: blog
permalink: /blog/ubuntu-mate-stonking-stingray-release-notes/
category: release
author: SuiVue
lang: en
discourse_topic_id: # TBC
title: Ubuntu MATE 26.10 Release Notes
description: What's new in Ubuntu MATE 26.10 (Stonking Stingray)
---

Lo and behold 👐, **Ubuntu MATE 26.10 (Stonking Stingray)** is here! 🎊 We are back 🦾 after a hiatus where the project skipped the 26.04 LTS release 🌥️ earlier this year.

This is the first official release from the [new circle of friends](https://discourse.ubuntu.com/t/hello-from-the-new-ubuntu-mate-maintainers-team/84246) 💚. I thank them all for their love and grit 🏋️ in seeing UM revive and thrive. Sincere thanks also to members of the larger Ubuntu community for their guidance ➡️ , patience 🧘 and support ⚓. Thanks also to our users 👥; their testing, feedback and good wishes played a part in shaping the release. And we intend to continue the 'Tenacious' efforts into the future.🦖

Ubuntu MATE 26.10 is a **standard release** (non-LTS) and will be **supported for 9 months, until July 2027**.

## What changed in Ubuntu MATE 26.10?

The team! 😇😉

Joking apart, in terms of new features, we must admit we could not complete upgrade of all of MATE packages to their latest released version even with our best efforts. The urgency with which we gathered and worked, the high standard of Debian packaging, overall quality process involved in a release and not to forget the challenges of balancing personal life, all weighed in.

On a positive note though, the available packages are stable 🏛️. Many bugs 🦟 were fixed by upstream. Some of those fixes 🛠️ have made it to the release and we are planning to backport others after the release.

As Ubuntu MATE builds on top of Ubuntu, please see the [Ubuntu 26.10 Release Notes](https://documentation.ubuntu.com/release-notes/26.10/) for details of all the changes and improvements.

## Known Issues:

- On the login screen, if we click on the password box, the password reveal/conceal (👁️) icon is broken ([LP 2169382](https://bugs.launchpad.net/ubuntu-mate/+bug/2169382)).

- During installation, if you choose manual installation, the installer creates the EFI partition automatically (and forcefully), even when you have created one manually. However, there is no issue when manually creating other partitions like /boot, /, /home etc. Workaround is to leave creation of EFI partition to the installer itself and only create other partitions. ([1572](https://github.com/canonical/ubuntu-desktop-provision/issues/1572))

- If you are a visually challenged user, the screen-reader installation has a quirk. On ‘Select your timezone’ slide, you cannot come out of ‘Timezone’ box with a ‘Tab’. It keeps looping and reads timezone info. As a workaround, press ‘Shift+Tab’ twice, to reach ‘Next’ button in reverse direction. From there the installation continues without issue. This affects all flavors using ‘subiquity’ installer ([1571](https://github.com/canonical/ubuntu-desktop-provision/issues/1571)).

- If you are testing on virtual machine, you may see an error pop-up saying, “Sorry, Ubuntu XX.YY has experienced an internal error.”, and if you click on ‘Show details’, it will (mostly) be /usr/bin/blueman-applet. There is no issue on bare-metal installs with bluetooth support.

- In live-session, ‘redshift’ application *may not* work. This is because, the location service has either not started or failed to start. There is no issue on an installed system (vm or bare-metal) as tested.

- In the installer, the links shown in 'Join the community' slide needs updating ([LP 2170678](https://bugs.launchpad.net/ubuntu/+source/ubuntu-mate-settings/+bug/2170678)).

## Other Changes:

There are some changes that may affect some UM users who rely on scripting and automation 🧙. If you are using any of the following packages, please check and adjust accordingly.

- We have migrated to `dracut` from `initramfs-tools`. While the `update-initramfs -u` command still works, specific options that you used may not be available any more.

- We have dropped `ifupdown` and embraced `netplan` fully. This had to be done because `ifupdown` was failing to bring ethernet devices in live-session (due to deprecated `dhclient` being hard-coded). This also means, there will be no `pppoeconf` package which pulls-in `ifupdown`.

- Latest version of `gdebi` is broken. It fails when we click on ‘Install’ and enter password. Instead of shipping it in non-functional state, we decided to drop it from the iso. We will work to fix the bug ([LP 2151797](https://bugs.launchpad.net/ubuntu/+source/gdebi/+bug/2151797)).

## Download Ubuntu MATE 26.10

{% include blog/jumbotron.html
    title = "Download Ubuntu MATE 26.10"
    text = "Available for 64-bit desktop computers!"
    button_text = "Download"
    button_url = "/download/"
%}

## Upgrading to Ubuntu MATE 26.10

For upgrading information, refer to the discourse topic "[Upgrading to Ubuntu MATE 26.10](https://discourse.ubuntu.com/t/upgrading-to-ubuntu-mate-26-10/89421)".

**NOTE:** There are no offline upgrade options for Ubuntu MATE. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

**P.S.**: The Ubuntu MATE flavoured stonking stingray mascot on the
download page was contributed by our community user (Thank you *@indigo*).
It is easier to participate and contribute to Ubuntu MATE than you probably
think. *Your* contribution could be part of next Ubuntu MATE release!
See [get-involved](https://ubuntu-mate.org/get-involved/) page to know more.
