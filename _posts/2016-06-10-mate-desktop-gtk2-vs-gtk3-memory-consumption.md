---
layout: blog-post
class: blog
title: MATE Desktop GTK2 vs GTK3 memory consumption
permalink: /blog/mate-desktop-gtk2-vs-gtk3-memory-consumption/
description: How does MATE Desktop for GTK2 RAM use compare to MATE Desktop for GTK3?
category: news
author: Martin Wimpress
lang: en
---

The number two question in the Ubuntu MATE community right now is:

> Does MATE Desktop built against GTK3 require more memory than MATE Desktop built against GTK2?

The answer is **Yes, but No**. Read on for a full explanation.

![Computer RAM](/images/blog/RAM.png)

Let's also take this opportunity to deal with another claim that cropped up
recently, [that MATE Desktop 1.14.1 on Ubuntu MATE 16.04 uses significantly
more memory that MATE Desktop 1.12.1 on Ubuntu MATE
16.04](https://plus.google.com/+BhikkhuSubhuti/posts/Y8td54KiGsA).

## Test conditions

  * MATE Desktop 1.12.1 and MATE Desktop 1.14.1 for Ubuntu MATE 16.04 **are both built against GTK2 only**.
  * These RAM comparisons were generated using
  [ps_mem](https://github.com/pixelb/ps_mem), because this is the correct tool
  for accurately measuring memory consumption, *one does not simply measure RAM consumption using System Monitor*.

If you want to tinker with `ps_mem` yourself it can be installed as follows:

    sudo apt update
    sudo apt install python-pip
    sudo pip install ps_mem

### Method for 16.04

Ubuntu MATE 16.04 was installed in a VM and fully upgraded and Ubuntu MATE
Welcome autostart was disabled, but all other defaults were used in all tests.
Upon login, `CRTL + ALT + t` was pressed to start a terminal and the following
script was run:

```bash
#!/usr/bin/env bash

SLEEP=90

if [ $(id -u) != 0 ]; then
    echo "You're not root you peasant!"
    exit 0
fi

VER=$(mate-about -v | sed 's/ /_/g')
echo "Profiling ${VER}"
echo "Sleeping for ${SLEEP} secs"
sleep ${SLEEP}
ps_mem | tee -a ${VER}.txt
echo "Done"
```

After the results were collected for Ubuntu MATE 16.04 running MATE Desktop
1.12.1 the system was [upgraded to MATE Desktop
1.14.1](/blog/mate-desktop-114-for-xenial-xerus/) and rebooted twice. Upon
login the same script was executed in the same way.

### Method for 16.10

[Ubuntu MATE 16.10
daily](http://cdimage.ubuntu.com/ubuntu-mate/daily-live/current/) was
installed in a VM and fully upgraded and Ubuntu MATE Welcome autostart was
disabled, but all other defaults were used in all tests. Upon login, `CRTL +
ALT + t` was pressed to start a terminal and the same script, as described
above, was run.

## Results

Here are the results:

<table class="table table-striped table-hover">
  <thead>
    <tr>
      <th>OS</th>
      <th>Desktop</th>
      <th>Tool Kit</th>
      <th>RAM (MiB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ubuntu MATE 16.04</td>
      <td>MATE Desktop 1.12.1</td>
      <td>GTK2</td>
      <td><span class="btn btn-warning btn-xs">353.0</span></td>
    </tr>
    <tr>
      <td>Ubuntu MATE 16.04</td>
      <td>MATE Desktop 1.14.1</td>
      <td>GTK2</td>
      <td><span class="btn btn-danger btn-xs">358.4</span></td>
    </tr>
    <tr>
      <td>Ubuntu MATE 16.10 (pre-alpha)</td>
      <td>MATE Desktop 1.14.1</td>
      <td>*GTK3*</td>
      <td><span class="btn btn-success btn-xs">351.7</span></td>
    </tr>
    <tr>
    </tr>
  </tbody>
</table>
<br />

## Conclusions

Here are some quick conclusions:

  * **MATE Desktop 1.14.1 does not use significantly more RAM that MATE Desktop
  1.12.1**, when both are built again GTK2.
  * **Ubuntu MATE 16.10 (pre-alpha)** using MATE Desktop 1.14.1 built against GTK3
  **uses less RAM than either Ubuntu MATE 16.04 configuration** using GTK2.

That second point needs some explaination because the detailed `ps_mem` output
included at the end of this blog post clearly shows that all MATE applications
built against GTK3 use more RAM than their GTK2 counterparts.

**Ubuntu MATE 16.10 (pre-alpha) is using less RAM than Ubuntu MATE 16.04** for the
following reasons:

  * **Tilda is no longer executed by default in Ubuntu MATE 16.10**, it is now an option in MATE Tweak.
  * Network Manager uses `systemd-resolved` via `libnss-resolve` for DNS lookups in 16.10 as opposed to `dnsmasq` in 16.04. This makes **Network Manager ever so slightly less resource intensive in Ubuntu 16.10**.
  * **All the default applications and components started in the default Ubuntu MATE 16.10 configuration use GTK3 only**, none use GTK2. So **only one toolkit is resident in memory**, not two as in Ubuntu MATE 16.04.

## Full `ps_mem` output

For completeness here is the `ps_mem` output for each test.

### Ubuntu MATE 16.04 with MATE Desktop 1.12.1 built against GTK2.

```text
 Private  +   Shared  =  RAM used   Program

156.0 KiB +  43.0 KiB = 199.0 KiB   tee
160.0 KiB +  40.5 KiB = 200.5 KiB   gnome-pty-helper
152.0 KiB +  49.0 KiB = 201.0 KiB   avahi-dnsconfd
224.0 KiB +  32.0 KiB = 256.0 KiB   acpid
276.0 KiB +  46.5 KiB = 322.5 KiB   agetty
320.0 KiB +  51.5 KiB = 371.5 KiB   irqbalance
328.0 KiB +  88.5 KiB = 416.5 KiB   cron
400.0 KiB +  93.0 KiB = 493.0 KiB   rtkit-daemon
464.0 KiB +  95.5 KiB = 559.5 KiB   dbus-launch
564.0 KiB +  21.5 KiB = 585.5 KiB   ssh-agent
624.0 KiB + 108.0 KiB = 732.0 KiB   dconf-service
648.0 KiB + 149.5 KiB = 797.5 KiB   gvfs-mtp-volume-monitor
756.0 KiB + 127.0 KiB = 883.0 KiB   gvfs-goa-volume-monitor
776.0 KiB + 198.0 KiB = 974.0 KiB   at-spi2-registryd
836.0 KiB + 141.0 KiB = 977.0 KiB   dnsmasq
932.0 KiB +  72.5 KiB =   1.0 MiB   systemd-logind
784.0 KiB + 243.0 KiB =   1.0 MiB   gvfsd
396.0 KiB + 637.0 KiB =   1.0 MiB   avahi-daemon (2)
900.0 KiB + 187.0 KiB =   1.1 MiB   accounts-daemon
896.0 KiB + 199.0 KiB =   1.1 MiB   gvfs-gphoto2-volume-monitor
988.0 KiB + 153.0 KiB =   1.1 MiB   gvfsd-fuse
924.0 KiB + 296.0 KiB =   1.2 MiB   gvfsd-dnssd
992.0 KiB + 281.0 KiB =   1.2 MiB   gvfsd-trash
  1.0 MiB + 293.5 KiB =   1.3 MiB   gvfsd-network
  1.1 MiB + 248.0 KiB =   1.3 MiB   sudo
  1.4 MiB +  76.5 KiB =   1.5 MiB   rsyslogd
  1.3 MiB + 260.0 KiB =   1.6 MiB   deja-dup-monitor
  1.3 MiB + 320.5 KiB =   1.6 MiB   ntpd
  1.5 MiB +  71.5 KiB =   1.6 MiB   systemd-journald
  1.2 MiB + 472.0 KiB =   1.6 MiB   gvfs-afc-volume-monitor
  1.2 MiB + 546.0 KiB =   1.8 MiB   (sd-pam)
  2.0 MiB +  41.0 KiB =   2.0 MiB   dhclient
  1.6 MiB + 461.5 KiB =   2.0 MiB   cupsd
  1.6 MiB + 432.0 KiB =   2.1 MiB   gvfs-udisks2-volume-monitor
  1.9 MiB + 199.0 KiB =   2.1 MiB   gnome-keyring-daemon
  1.6 MiB + 547.5 KiB =   2.1 MiB   upowerd
  1.5 MiB + 768.0 KiB =   2.2 MiB   cups-browsed
  1.6 MiB + 753.0 KiB =   2.3 MiB   dbus (2)
  1.7 MiB + 724.0 KiB =   2.4 MiB   lightdm (2)
  2.4 MiB + 136.0 KiB =   2.5 MiB   systemd-udevd
  2.6 MiB + 194.0 KiB =   2.8 MiB   at-spi-bus-launcher
  2.1 MiB + 805.0 KiB =   2.9 MiB   polkit-mate-authentication-agent-1
  2.4 MiB + 841.5 KiB =   3.2 MiB   mate-session
  2.1 MiB +   1.2 MiB =   3.3 MiB   whoopsie
  2.8 MiB + 645.0 KiB =   3.4 MiB   dbus-daemon (3)
  2.5 MiB + 930.0 KiB =   3.4 MiB   mate-power-manager
  2.9 MiB + 935.0 KiB =   3.8 MiB   mate-maximus
  3.5 MiB + 362.0 KiB =   3.8 MiB   ModemManager
  3.3 MiB + 898.5 KiB =   4.2 MiB   notification-area-applet
  2.1 MiB +   2.2 MiB =   4.3 MiB   systemd (2)
  3.7 MiB + 633.0 KiB =   4.3 MiB   obexd
  4.4 MiB + 216.0 KiB =   4.6 MiB   polkitd
  3.5 MiB +   1.2 MiB =   4.7 MiB   bash (3)
  4.8 MiB + 377.0 KiB =   5.1 MiB   udisksd
  3.9 MiB +   1.2 MiB =   5.2 MiB   trashapplet
  5.2 MiB + 612.0 KiB =   5.8 MiB   pulseaudio
  4.7 MiB +   1.1 MiB =   5.9 MiB   marco
  4.7 MiB +   1.4 MiB =   6.1 MiB   clock-applet
  4.4 MiB +   2.0 MiB =   6.4 MiB   mate-volume-control-applet
  6.1 MiB + 824.5 KiB =   6.9 MiB   NetworkManager
  5.2 MiB +   1.8 MiB =   7.0 MiB   wnck-applet
  6.9 MiB +   1.7 MiB =   8.6 MiB   mate-settings-daemon
  6.8 MiB +   2.2 MiB =   9.0 MiB   mate-terminal
  8.1 MiB + 921.5 KiB =   9.0 MiB   gvfsd-smb-browse
  8.3 MiB + 923.5 KiB =   9.2 MiB   mate-screensaver
  8.7 MiB +   1.9 MiB =  10.6 MiB   mate-panel
  8.8 MiB +   7.6 MiB =  16.4 MiB   update-notifier
 10.9 MiB +   8.1 MiB =  18.9 MiB   nm-applet
 16.9 MiB +   2.9 MiB =  19.8 MiB   applet.py
 14.2 MiB +   8.1 MiB =  22.3 MiB   tilda
 21.7 MiB +   3.1 MiB =  24.8 MiB   caja
 21.9 MiB +   5.8 MiB =  27.8 MiB   blueman-applet
 25.2 MiB +   5.9 MiB =  31.1 MiB   Xorg
---------------------------------
                        353.0 MiB
=================================
```

## Ubuntu MATE 16.04 with MATE Desktop 1.14.1 built against GTK2.

```text
 Private  +   Shared  =  RAM used   Program

152.0 KiB +  48.0 KiB = 200.0 KiB   avahi-dnsconfd
156.0 KiB +  45.0 KiB = 201.0 KiB   tee
164.0 KiB +  43.5 KiB = 207.5 KiB   gnome-pty-helper
224.0 KiB +  33.0 KiB = 257.0 KiB   acpid
292.0 KiB +  46.5 KiB = 338.5 KiB   agetty
324.0 KiB +  49.5 KiB = 373.5 KiB   irqbalance
324.0 KiB +  85.5 KiB = 409.5 KiB   cron
396.0 KiB +  87.0 KiB = 483.0 KiB   rtkit-daemon
460.0 KiB +  94.5 KiB = 554.5 KiB   dbus-launch
584.0 KiB +  21.5 KiB = 605.5 KiB   ssh-agent
628.0 KiB + 112.0 KiB = 740.0 KiB   dconf-service
652.0 KiB + 150.5 KiB = 802.5 KiB   gvfs-mtp-volume-monitor
672.0 KiB + 191.0 KiB = 863.0 KiB   at-spi-bus-launcher
824.0 KiB + 131.0 KiB = 955.0 KiB   gvfs-goa-volume-monitor
780.0 KiB + 195.0 KiB = 975.0 KiB   at-spi2-registryd
844.0 KiB + 138.0 KiB = 982.0 KiB   dnsmasq
912.0 KiB +  75.5 KiB = 987.5 KiB   systemd-logind
400.0 KiB + 635.0 KiB =   1.0 MiB   avahi-daemon (2)
884.0 KiB + 198.0 KiB =   1.1 MiB   gvfs-gphoto2-volume-monitor
908.0 KiB + 178.0 KiB =   1.1 MiB   accounts-daemon
  1.0 MiB + 150.0 KiB =   1.1 MiB   gvfsd-fuse
956.0 KiB + 298.0 KiB =   1.2 MiB   gvfsd-dnssd
  1.0 MiB + 276.0 KiB =   1.3 MiB   gvfsd-trash
  1.0 MiB + 291.5 KiB =   1.3 MiB   gvfsd-network
  1.1 MiB + 244.0 KiB =   1.3 MiB   sudo
  1.4 MiB +  80.5 KiB =   1.5 MiB   rsyslogd
  1.3 MiB + 262.0 KiB =   1.6 MiB   deja-dup-monitor
  1.3 MiB + 323.5 KiB =   1.6 MiB   ntpd
  1.2 MiB + 451.0 KiB =   1.6 MiB   gvfs-afc-volume-monitor
  1.6 MiB +  70.5 KiB =   1.6 MiB   systemd-journald
  1.4 MiB + 588.0 KiB =   1.9 MiB   (sd-pam)
  1.6 MiB + 383.5 KiB =   2.0 MiB   cupsd
  1.9 MiB +  40.0 KiB =   2.0 MiB   dhclient
  1.8 MiB + 203.0 KiB =   2.0 MiB   gnome-keyring-daemon
  1.6 MiB + 416.0 KiB =   2.0 MiB   gvfs-udisks2-volume-monitor
  1.4 MiB + 756.0 KiB =   2.2 MiB   cups-browsed
  2.1 MiB + 135.0 KiB =   2.2 MiB   systemd-udevd
  1.7 MiB + 721.0 KiB =   2.4 MiB   lightdm (2)
  2.4 MiB + 230.0 KiB =   2.6 MiB   polkitd
  2.1 MiB + 767.0 KiB =   2.9 MiB   polkit-mate-authentication-agent-1
  2.8 MiB + 243.0 KiB =   3.0 MiB   gvfsd
  2.8 MiB + 373.0 KiB =   3.1 MiB   udisksd
  2.1 MiB +   1.2 MiB =   3.2 MiB   whoopsie
  2.4 MiB + 836.5 KiB =   3.2 MiB   mate-session
  2.8 MiB + 650.0 KiB =   3.4 MiB   dbus-daemon (3)
  2.6 MiB + 926.0 KiB =   3.5 MiB   mate-power-manager
  2.9 MiB + 917.0 KiB =   3.8 MiB   mate-maximus
  3.5 MiB + 374.0 KiB =   3.9 MiB   ModemManager
  3.6 MiB + 525.5 KiB =   4.1 MiB   upowerd
  3.3 MiB + 888.5 KiB =   4.1 MiB   notification-area-applet
  3.7 MiB + 612.0 KiB =   4.3 MiB   obexd
  2.2 MiB +   2.2 MiB =   4.4 MiB   systemd (2)
  3.1 MiB +   1.3 MiB =   4.4 MiB   dbus (4)
  3.6 MiB +   1.2 MiB =   4.7 MiB   bash (3)
  3.9 MiB +   1.2 MiB =   5.1 MiB   trashapplet
  4.3 MiB + 921.5 KiB =   5.2 MiB   mate-screensaver
  5.1 MiB + 662.0 KiB =   5.7 MiB   pulseaudio
  4.7 MiB +   1.1 MiB =   5.8 MiB   marco
  4.4 MiB +   2.0 MiB =   6.3 MiB   mate-volume-control-applet
  5.0 MiB +   1.6 MiB =   6.5 MiB   wnck-applet
  6.3 MiB + 791.5 KiB =   7.1 MiB   NetworkManager
  6.7 MiB +   1.5 MiB =   8.1 MiB   clock-applet
  6.9 MiB +   1.8 MiB =   8.7 MiB   mate-settings-daemon
  8.0 MiB + 896.5 KiB =   8.9 MiB   gvfsd-smb-browse
  6.7 MiB +   2.2 MiB =   8.9 MiB   mate-terminal
 10.6 MiB +   1.9 MiB =  12.4 MiB   mate-panel
 10.5 MiB +   7.4 MiB =  17.9 MiB   update-notifier
 11.5 MiB +   7.8 MiB =  19.3 MiB   nm-applet
 16.6 MiB +   2.9 MiB =  19.5 MiB   applet.py
 15.4 MiB +   7.5 MiB =  22.8 MiB   tilda
 21.9 MiB +   3.2 MiB =  25.1 MiB   caja
 24.0 MiB +   5.9 MiB =  29.9 MiB   blueman-applet
 27.1 MiB +   5.6 MiB =  32.7 MiB   Xorg
---------------------------------
                        358.4 MiB
=================================
```

## Ubuntu MATE 16.10 with MATE Desktop 1.14.1 built against GTK3.

```text
 Private  +   Shared  =  RAM used   Program

152.0 KiB +  53.0 KiB = 205.0 KiB   avahi-dnsconfd
156.0 KiB +  52.0 KiB = 208.0 KiB   tee
236.0 KiB +  34.0 KiB = 270.0 KiB   acpid
320.0 KiB +  51.5 KiB = 371.5 KiB   irqbalance
324.0 KiB +  50.5 KiB = 374.5 KiB   agetty
324.0 KiB +  91.5 KiB = 415.5 KiB   cron
408.0 KiB +  96.0 KiB = 504.0 KiB   rtkit-daemon
572.0 KiB +  19.5 KiB = 591.5 KiB   ssh-agent
616.0 KiB + 118.0 KiB = 734.0 KiB   dconf-service
676.0 KiB + 161.5 KiB = 837.5 KiB   gvfs-mtp-volume-monitor
768.0 KiB + 141.0 KiB = 909.0 KiB   gvfs-goa-volume-monitor
780.0 KiB + 208.0 KiB = 988.0 KiB   at-spi2-registryd
928.0 KiB +  75.5 KiB =   1.0 MiB   systemd-logind
932.0 KiB +  84.0 KiB =   1.0 MiB   systemd-resolved
388.0 KiB + 659.0 KiB =   1.0 MiB   avahi-daemon (2)
776.0 KiB + 309.0 KiB =   1.1 MiB   gvfsd
896.0 KiB + 211.0 KiB =   1.1 MiB   gvfs-gphoto2-volume-monitor
892.0 KiB + 218.0 KiB =   1.1 MiB   dbus-launch (2)
  1.1 MiB + 275.5 KiB =   1.4 MiB   accounts-daemon
  1.1 MiB + 260.0 KiB =   1.4 MiB   sudo
  1.2 MiB + 212.5 KiB =   1.4 MiB   gvfsd-fuse
  1.4 MiB +  79.5 KiB =   1.5 MiB   rsyslogd
  1.2 MiB + 419.5 KiB =   1.6 MiB   gvfsd-trash
  1.4 MiB + 296.5 KiB =   1.7 MiB   deja-dup-monitor
  1.2 MiB + 535.5 KiB =   1.7 MiB   gvfs-afc-volume-monitor
  1.6 MiB +  79.5 KiB =   1.7 MiB   systemd-journald
  1.4 MiB + 462.0 KiB =   1.9 MiB   ntpd
  2.0 MiB +  44.0 KiB =   2.0 MiB   dhclient
  1.5 MiB + 560.5 KiB =   2.1 MiB   cupsd
  1.6 MiB + 588.0 KiB =   2.2 MiB   upowerd
  1.8 MiB + 483.5 KiB =   2.3 MiB   gvfs-udisks2-volume-monitor
  1.5 MiB + 984.0 KiB =   2.5 MiB   cups-browsed
  2.1 MiB + 756.0 KiB =   2.8 MiB   lightdm (2)
  2.7 MiB + 131.0 KiB =   2.8 MiB   systemd-udevd
  2.1 MiB + 988.5 KiB =   3.1 MiB   bash (2)
  2.2 MiB + 950.0 KiB =   3.1 MiB   (sd-pam) (2)
  2.2 MiB + 952.0 KiB =   3.2 MiB   gnome-keyring-daemon (2)
  2.9 MiB + 281.0 KiB =   3.2 MiB   at-spi-bus-launcher
  2.9 MiB + 355.0 KiB =   3.2 MiB   polkitd
  2.9 MiB + 451.5 KiB =   3.4 MiB   udisksd
  2.1 MiB +   1.4 MiB =   3.5 MiB   whoopsie
  3.1 MiB + 798.5 KiB =   3.9 MiB   dbus-daemon (4)
  3.9 MiB + 578.0 KiB =   4.5 MiB   obexd
  3.6 MiB + 948.0 KiB =   4.5 MiB   polkit-mate-authentication-agent-1
  2.7 MiB +   2.4 MiB =   5.0 MiB   systemd (3)
  4.0 MiB +   1.1 MiB =   5.2 MiB   notification-area-applet
  4.4 MiB +   1.1 MiB =   5.5 MiB   mate-maximus
  4.4 MiB +   1.3 MiB =   5.7 MiB   mate-power-manager
  4.6 MiB +   1.1 MiB =   5.7 MiB   mate-session
  5.2 MiB + 595.0 KiB =   5.8 MiB   pulseaudio
  5.5 MiB + 357.0 KiB =   5.8 MiB   ModemManager
  4.7 MiB +   1.5 MiB =   6.3 MiB   update-notifier
  4.9 MiB +   1.6 MiB =   6.4 MiB   trashapplet
  5.8 MiB +   1.1 MiB =   6.9 MiB   mate-screensaver
  5.0 MiB +   2.0 MiB =   7.1 MiB   mate-volume-control-applet
  6.5 MiB + 926.5 KiB =   7.4 MiB   NetworkManager
  5.7 MiB +   1.7 MiB =   7.4 MiB   wnck-applet
  5.9 MiB +   1.8 MiB =   7.7 MiB   clock-applet
  6.5 MiB +   1.4 MiB =   7.9 MiB   marco
  7.0 MiB +   2.1 MiB =   9.1 MiB   nm-applet
  9.1 MiB +   2.2 MiB =  11.4 MiB   mate-settings-daemon
  9.9 MiB +   2.1 MiB =  11.9 MiB   mate-panel
 11.0 MiB +   2.4 MiB =  13.4 MiB   mate-terminal
 17.0 MiB +   3.2 MiB =  20.1 MiB   applet.py
 21.2 MiB +   4.8 MiB =  26.0 MiB   blueman-applet
 23.3 MiB +   5.1 MiB =  28.4 MiB   caja
 54.0 MiB +   2.8 MiB =  56.8 MiB   Xorg
---------------------------------
                        351.7 MiB
=================================
```
