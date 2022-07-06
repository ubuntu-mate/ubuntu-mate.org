---
layout: sidebar
permalink: /raspberry-pi/compatibility/
lang: en
sidebar: raspberry-pi

title: Raspberry Pi Compatibility

---

## Supported Raspberry Pi Models

{% include partials/pi-compatibility-table.html %}

Note that the experience with models with 1 GB of RAM may be hampered by
memory pressure and increase wear on SD cards due to swapping.


## armhf or arm64?

Good question! [This is answered on our Raspberry Pi Download page.](/raspberry-pi/download/)


## Storage Tips

As always, microSDHC I/O throughput is a bottleneck on the Raspberry Pi so don't
gimp your Raspberry Pi by cheaping out on poor performing microSDHC
cards. We used the [Samsung EVO Plus 32 GB microSDHC UHS-I U1](https://geni.us/AKAsg)
and [Kingston 64 GB microSDXC Canvas Go Plus](https://geni.us/Jelmu)
during the testing of these images and they significantly better
performance than most other microSDHC cards we've tried.
[But don't take our word for it](https://www.pidramble.com/wiki/benchmarks/microsd-cards).

You'll need a microSD card which is **8GB** or greater to fit the image.
The file system will automatically resize to occupy the unallocated
space of the microSD card.
