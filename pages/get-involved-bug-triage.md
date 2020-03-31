---
layout: sidebar
title: Bug Reporting and Triage
permalink: /get-involved/bug-triage/
lang: en
class: get-involved
sidebar: get-involved
---


## Bug Reporting

### First Steps

If you don't already have a Launchpad account, [set one up](https://help.launchpad.net/YourAccount/NewAccount) 
before you get started. Ubuntu uses Launchpad to track bugs and their fixes.

### Is Your Bug a Bug

No, this isn't a weird philosophical question. Be sure to check the [community 
forum](https://ubuntu-mate.community) to see if your bug might just be a
configuration issue. Make sure you also check the [release notes](/blog/) for
your particular version of Ubuntu MATE, and also check [Launchpad](https://bugs.launchpad.net/ubuntu-mate) for
any duplicate reports of your issue.

### Reporting Bugs in Ubuntu MATE

If your issue is indeed a bug, [this tutorial](https://ubuntu-mate.community/t/how-to-report-problems-in-ubuntu-mate/17943) 
is extremely helpful in showing the individual steps to file a 
report. Many thanks to APolihron, one of our QA testers, for making this!


## Bug Triage

Once bug reports are filed, the next step is to triage the bug. Much like 
medical staff prioritize patients based on the severity of their condition, bug
triagers help teams determine which bugs are critical, and which are less 
urgent.

Some bug triage tasks require special privileges granted by project owners or
administrators, but others simply require a [Launchpad](https://code.launchpad.net/ubuntu/+login) account.
The key things you can do to help us prioritise bugs are as follows:

* Can you reproduce a reported bug? If you can, write up the steps you followed
to confirm the issue also exists for you.
* If you confirmed the bug, could you also replicate the issue in stock Ubuntu
or other flavours? Be sure your report indicates other affected flavours, or if
the issue was limited to Ubuntu MATE.
* However, if you can't reproduce the bug, can you get more information from the
original bug reporter?
* Did you determine the bug was a duplicate? If so, mark one bug as a duplicate
of the other.
* Did you determine the bug was filed with the wrong project? If so, re-open the 
bug with the right project and leave a note in the initial location.

The initial work can help us realise where an error is, especially if the error
is upstream. Bug triagers help make sure things are flowing as they should 
between upstream and downstream, and help bug fixers know where they need to
focus their efforts.

The video below shows bug triaging (and Martin!) in action:

{% include blog/youtube.html embed = "https://www.youtube.com/embed/kWojaWHl3U4?t=3732&rel=0" %}

