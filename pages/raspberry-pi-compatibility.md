---
layout: sidebar
permalink: /raspberry-pi/compatibility/
lang: en
sidebar: raspberry-pi

title: Raspberry Pi Compatibility

---

## Supported Raspberry Pi Models

| Model                 | RAM   | Instruction Set | [armhf]  | [arm64]   |
| --------------------- | ----- | --------------- | -------- | --------- |
| Raspberry Pi 1 A+     | <512 MB | ARMv6         | No        | No        |
| Raspberry Pi 1 B+     | 512 MB| ARMv6           | No        | No        |
| Raspberry Pi Zero     | 512 MB| ARMv6           | No        | No        |
| Raspberry Pi Zero W   | 512 MB| ARMv6           | No        | No        |
| Raspberry Pi 2 B      | 1 GB  | ARMv7           | Yes       | No        |
| Raspberry Pi 3 B      | 1 GB  | ARMv8           | Yes       | Yes       |
| Raspberry Pi 3 B      | 1 GB  | ARMv8           | Yes       | Yes       |
| Raspberry Pi 3 B+     | 1 GB  | ARMv8           | Yes       | Yes       |
| Raspberry Pi 4 B      | 1 GB  | ARMv8           | Yes       | Yes       |
| Raspberry Pi 4 B      | 2 GB  | ARMv8           | Yes       | Yes       |
| Raspberry Pi 4 B      | 4 GB  | ARMv8           | Yes       | Yes       |
| Raspberry Pi 4 B      | 8 GB  | ARMv8           | Yes       | Yes       |
| Raspberry Pi 400      | 4 GB  | ARMv8           | Yes       | Yes       |

[armhf]: /download/armhf/
[arm64]: /download/arm64/

Note that the experience with models with 1 GB of RAM may be hampered by
memory pressure and increase wear on SD cards due to swapping.

### Raspberry Pi 2

This model fails to complete set up due to insufficient memory.

* If you have completed the setup on another Pi that card can be inserted in a Pi 3 Model A+ and it will work.
* Due to only having 512MB RAM, the system can be very tight on resources.

## armhf or arm64?

Good question! [This is answered on our Raspberry Pi Download page.](/raspberry-pi/download/)

## Memory and storage stats

Memory pressure is reasonable using the `armhf` images (~350MB at idle)
but quite tight on the `arm64` images (~490MB at idle). As always,
microSDHC I/O throughput is a bottleneck on the Raspberry PPi so don't
gimp your Raspberry Pi by cheaping out on poor performing microSDHC
cards. We used the [Samsung EVO Plus 32 GB microSDHC UHS-I U1](https://geni.us/AKAsg)
and [Kingston 64 GB microSDXC Canvas Go Plus](https://geni.us/Jelmu)
during the testing of these images and they significantly better
performance than most other microSDHC cards we've tried.
[But don't take our word for it](https://www.pidramble.com/wiki/benchmarks/microsd-cards).

You'll need a microSD card which is **8GB** or greater to fit the image.
The file system will automatically resize to occupy the unallocated
space of the microSD card. Here is our recommended kit lists on Amazon:
