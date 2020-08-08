---
layout: sidebar
permalink: /faq/verify-download-secure/
lang: en
class: faq
sidebar: faq

title: Verifying Downloads

---

## Verify for Tampering

This method will verify the signature on the `SHA256SUMS` checksum file. By
proving that this file's digital signature belongs to Ubuntu, you can be
confident using these checksums to verify the downloaded files haven't been
tampered or corrupted.

{% include partials/toc.html %}


## Preperations

### Windows

We recommend using the [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/faq),
which allows you to run Ubuntu within Windows. This will provide a GNU/Linux
environment for running GPG and checksum commands.

For help setting up this environment, please see:

* <https://ubuntu.com/tutorials/tutorial-ubuntu-on-windows>

Once installed, jump to the [steps](#steps) section.


### macOS

You'll need to install GnuPG (utility for verifying the signature) and
`sha256sum` (for verifying the checksum). We recommend installing this via
[Homebrew](https://brew.sh/), a command line package manager for macOS.

1. Install: <https://brew.sh/>
2. Run:

       brew install gnupg
       brew install coreutils

Once installed, jump to the [steps](#steps) section.


### GNU/Linux

Most, if not all, distros (including Ubuntu MATE) comes preloaded with packages
that provide `gnupg` and `sha256sum`. If yours doesn't, you can install these
via your distro's package manager.

In Ubuntu, `sha256sum` is provided in `coreutils`.


## Steps

### 1. Obtain the checksums and signature

For downloads provided by Canonical:

* <http://cdimages.ubuntu.com/ubuntu-mate/releases/>
* Download the `SHA256SUM` and `SHA256SUM.gpg` files.

>
> **Canonical's download server is HTTP! Is this secure?**
>
> This is a question that commonly asked. We use Canonical's infrastructure
> being an official Ubuntu flavour. Many archive mirrors do not use
> SSL to reduce the overhead of HTTPS.
>
> The GPG fingerprint is validated against the Ubuntu keyserver.
> So, regardless of where you obtained the file, if the signature matches,
> you can trust the file.
>

Or for device ports provided by us:

* <https://releases.ubuntu-mate.org>
* Download the `.sha256` and `.sha256.sign` files.

First, let's find out if you have the signature key:

    gpg --keyid-format long --verify SHA256SUMS.gpg SHA256SUMS

Or:

    gpg --keyid-format long --verify *.sha256.sign *.sha256

If this says:

>
> gpg: Signature made Thursday, October 17, 2019 PM03:13:47 BST
>
> gpg:                using DSA key 46181433FBB75451
>
> **gpg: Can't check signature: No public key**
>
> gpg: Signature made Thursday, October 17, 2019 PM03:13:47 BST
>
> gpg:                using RSA key D94AA3F0EFE21092
>
> **gpg: Can't check signature: No public key**
>

If you don't have the public key, see **step 2**, otherwise skip to **step 3**.


### 2. Retrieve the key (if applicable)

Here's how to securely download the signature key from the keyserver. This only
needs to be performed once, except in the rare situation the keys were updated.

In this instance, the two keys are `46181433FBB75451` and `D94AA3F0EFE21092`.
Run this command, but add `0x` to the start of both these keys, like so:

    gpg --keyid-format long --keyserver hkp://keyserver.ubuntu.com --recv-keys 0x46181433FBB75451 0xD94AA3F0EFE21092

You should get an output like this:

>
> gpg: key D94AA3F0EFE21092: public key "Ubuntu CD Image Automatic Signing Key (2012) <cdimage@ubuntu.com>" imported
>
> gpg: key 46181433FBB75451: 110 signatures not checked due to missing keys
>
> gpg: key 46181433FBB75451: public key "Ubuntu CD Image Automatic Signing Key <cdimage@ubuntu.com>" imported
>
> gpg: no ultimately trusted keys found
>
> gpg: Total number processed: 2
>
> gpg:               imported: 2
>

Or:

> gpg: key 7454357CFFEE1E5C: public key "Martin Wimpress <martin@wimpress.org>" imported
> gpg: Total number processed: 1
> gpg:               imported: 1


Suspicions should arise if the public key belongs to a random stranger, or looks
forged.


### 3. Is it a match?

Run this command:

    gpg --keyid-format long --verify SHA256SUMS.gpg SHA256SUMS

And the output:

>
> gpg: Signature made Thursday, October 17, 2019 PM03:13:47 BST
>
> gpg:                using DSA key 46181433FBB75451
>
> **gpg: Good signature from "Ubuntu CD Image Automatic Signing Key <cdimage@ubuntu.com>" [unknown]**
>
> gpg: WARNING: This key is not certified with a trusted signature!
>
> gpg:          There is no indication that the signature belongs to the owner.
>
> Primary key fingerprint: C598 6B4F 1257 FFA8 6632  CBA7 4618 1433 FBB7 5451
>
> gpg: Signature made Thursday, October 17, 2019 PM03:13:47 BST
>
> gpg:                using RSA key D94AA3F0EFE21092
>
> **gpg: Good signature from "Ubuntu CD Image Automatic Signing Key (2012) <cdimage@ubuntu.com>" [unknown]**
>
> gpg: WARNING: This key is not certified with a trusted signature!
>
> gpg:          There is no indication that the signature belongs to the owner.
>
> Primary key fingerprint: 8439 38DF 228D 22F7 B374  2BC0 D94A A3F0 EFE2 1092
>

Note the **bold** lines which confirm the file was signed by the team
over at Ubuntu. If this wasn't genuine, the result would be **BAD signature**.

The "key is not certified" message is simply because you haven't explictly told
GnuPG to trust this key. This is optional. You can
[learn more about GnuPG on the wiki page](https://help.ubuntu.com/community/GnuPrivacyGuardHowto).


### 4. Verify the ISOs

Now we know the checksum file is untampered with, you can proceed to verify
for corruption as normal.

    sha256sum -c SHA256SUMS 2>&1 | grep OK

You should see "OK" in its output:

    ubuntu-mate-20.04-desktop-amd64.iso: OK

An empty output would indicate the file is corrupt and should re-downloaded
again.

There are other ways to perform checksum checks that don't require a Terminal,
take a look at our [Verify for corruption](/faq/verify-download-quick/) for details.


---

_This page is an adaptation of [Ubuntu's verification tutorial](https://discourse.ubuntu.com/t/14010)._
