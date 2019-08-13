<!--
.. title: How to Verify Downloads
.. slug: how-to-verify-downloads
.. date: 2016-04-07 21:00:00 UTC
.. tags: Verify,Download,Security,Checksum
.. link:
.. description: Methods to verify your downloads are immune from hackers.
.. type: text
.. author: Luke Horwell
-->

## Why verify your downloads?

While in most cases, downloads are free from corruption and tampering,
you may wish to verify the integrity of your download to ensure you
are getting a clean copy of Ubuntu MATE exactly how the developers intended.

Verifying downloads are particularly important when downloading directly from
a server. BitTorrent is secure too as it checks pieces as it downloads.


## Check the SHA256 Hash (quick)

### On Ubuntu MATE

On current Ubuntu MATE versions (18.04 LTS and newer), `caja-gtkhash` is pre-installed
and allows you to perform checksums from within the file browser.

 * Navigate to the file in the **Caja** file manager.
 * Open the file's properties.
   * Either via the menu bar: **File → Properties** 
   * Or right click the file → **Properties**.
 * Choose **Digests** tab
 * Copy the SHA256SUM checksum from the download page and paste into **Check** field

![](/gallery/quick-help-screenshots/Caja-hash-howto.png "GtkHash inside Caja")

**Note:** To make calculation faster, it's only necessary to check the checksums you have values for.

---

### On other GNU/Linux distributions

#### Using a graphical tool: GtkHash

If GtkHash isn't installed, you can install it via your distribution's software manager.

 * Launch **GtkHash**
 * Select ISO in _File_ chooser
 * Copy the SHA256SUM checksum from the download page and paste into **Check** field
 * Click **Hash**
 * Ensure you have green checkmark near one of the calculated checksums

![](/gallery/quick-help-screenshots/Gtk-hash-howto.png "Using GtkHash")

#### Using the command line

A majority of other distributions come with  `sha256sum` pre-installed.

1. Open the folder containing the download in the terminal.

![](/gallery/quick-help-screenshots/sha256-ubuntu-1.png "Opening the folder in the terminal.")


2. Type `sha256sum` followed by the file name of the image.

        sha256sum ubuntu-mate-15.10-desktop-amd64.iso


3. Compare the hash with the one provided on the [Download](/download/) page.

    ![](/gallery/quick-help-screenshots/sha256-ubuntu-2.png "Results from the hash")

-----------
### On Windows

Checksum utilities are available on the web, such as:

 * [MD5 & SHA Checksum Utility](https://raylin.wordpress.com/downloads/md5-sha-1-checksum-utility/)
 * [Hashtab](http://implbits.com/products/hashtab/)
 * [Microsoft File Checksum Integrity Verifier](https://support.microsoft.com/en-us/help/889768/how-to-compute-the-md5-or-sha-1-cryptographic-hash-values-for-a-file)


-----------
### On Mac OS X

`sha256` is pre-installed with most versions of OS X.

    shasum -a 256 ubuntu-mate-15.10-desktop-amd64.iso


Graphical utilities are also available:

 * [Hashtab](http://implbits.com/products/hashtab/)


-----------
## Check using Repository GPG Keys (secure)

This method verifies the hashes published by Canonical are
actually authenticate. Unlike performing a quick checksum,
the SHA256SUMS file is signed and only Ubuntu's key can unlock
the file to reveal the checksums exactly as Ubuntu published them.

### Ubuntu

1. Download a copy of the `SHA256SUMS` and `SHA256SUMS.gpg` files
from [Canonical's CD Images server](http://cdimage.ubuntu.com/ubuntu-mate/releases/) for that particular version.

    ![](/gallery/quick-help-screenshots/sha256sums-gpg.png "Finding the SHA256SUMS file")


2. Install the Ubuntu Keyring. This may already be present on your system.

        sudo apt-get install ubuntu-keyring


3. Verify the keyring.

        gpgv --keyring=/usr/share/keyrings/ubuntu-archive-keyring.gpg SHA256SUMS.gpg SHA256SUMS


4. Verify the checksum of the downloaded image.

        grep ubuntu-16.04-desktop-amd64.iso SHA256SUMS | sha256sum --check

5. If you see "OK", the image is in good condition.

        ubuntu-mate-15.10-desktop-amd64.iso: OK

