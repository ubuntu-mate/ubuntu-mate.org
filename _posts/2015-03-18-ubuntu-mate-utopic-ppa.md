---
layout: blog-post
title: Ubuntu MATE 14.10 PPA Change
permalink: ubuntu-mate-utopic-ppa
description: Ubuntu MATE 14.10 has a new PPA, you must enable it.
category: news
author: Martin Wimpress
lang: en
---

## No action required

Since this blog post was first made there have been some complaints about
having to enable a new PPA. Therefore the original PPA that is embedded in
the Ubuntu MATE 14.10 iso images has been populated with updated packages
that were shipped on the Ubuntu MATE 14.10 iso images.

This PPA now includes the current MATE 1.8 packages and all the bugs that have
been fixed by the MATE package maintainer for Debian. In order to get your
updates, no further action is required.

### Ubuntu MATE 14.10 - Optional

If you are running Ubuntu MATE 14.10 you should consider adding this following 
PPA to get access to optional MATE packages that were not included in the iso
images.

    sudo apt-add-repository ppa:ubuntu-mate-dev/utopic-mate
    sudo apt-get update
    sudo apt-get upgrade
