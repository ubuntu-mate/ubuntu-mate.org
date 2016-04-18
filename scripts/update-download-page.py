#! /usr/bin/python3
#
#  Easy Configurable Download Page for ubuntu-mate.org
#
#  Licensed under Creative Commons Attribution-ShareAlike 4.0 International License
#  as with the rest of the website.
#
#  (C) 2016, Luke Horwell <lukehorwell37+code@gmail.com>
#

import os
import sys
import inspect
import json
import libtorrent   # Provided by package 'python3-libtorrent'
import wget         # Provided by package 'python3-wget'
import subprocess

#
# ===== Arguments =====
#   --update-all         =  Update everything for the page.
#   --update-page        =  Regenerate the page.
#   --update-magnet-uri  =  Update the magnet URIs saved to downloads.json.
#

class DownloadPageScript(object):
    def __init__(self):
        print('--------------------------------\nDownload Page Markdown Update\n--------------------------------')

        # Paths from where this script is located
        self.whereami = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.source_template_path    = self.whereami + "/../pages/templates/download.md"
        self.target_destination_path = self.whereami + "/../pages/download.md"
        self.downloads_json_path     = self.whereami + "/../downloads.json"
        self.temp_files = []

        # Process arguments.
        if not len(sys.argv) > 1:
            print("What would you like the script to do?\nIs this production or debugging?")
            print("See --help or try --update-all.")

        for arg in sys.argv:
            if arg == '--update-all':
                self.read_json()
                self.update_magnet_uri()
                self.clean_up_temp()
                self.save_json()
                self.manipulate_page()
                self.generate_paypal_links()
                self.write_download_page()
            elif arg == '--update-page':
                self.read_json()
                self.manipulate_page()
                self.generate_paypal_links()
                self.write_download_page()
            elif arg == '--update-magnet-uri':
                self.read_json()
                self.update_magnet_uri()
                self.clean_up_temp()
                self.save_json()
            elif arg == '--help':
                print("\nScript for updating the dynamic Ubuntu MATE download page.\n")
                print("--update-all         =  Update everything for the page.")
                print("--update-page        =  Regenerate the page.")
                print("--update-magnet-uri  =  Update the magnet URIs saved to downloads.json.")

    # Useful functions used later in the script.
    def download_file(self, url):
        url_name = url.split('/')[-1]
        print('\nDownloading file: ' + url_name)
        filename = wget.download(url)
        self.temp_files.append(filename)
        return filename

    def clean_up_temp(self):
        for name in self.temp_files:
            os.remove(name)

    def get_download_size(self, url):
        url_name = url.split('/')[-1]
        print('Downloading metadata: ' + url_name)
        response = str(subprocess.Popen(['wget','--spider', url], stderr=subprocess.PIPE).communicate()[1])
        response.split('\n')
        size = int(response.split('Length: ')[1].split(' ')[0])
        size_MB = size / 1000 / 1000
        size_GB = size / 1000 / 1000 / 1000
        if size_GB < 1:
            return str(round(size_MB)) + ' MB'
        else:
            return str(round(size_GB,1)) + ' GB'

    def generate_magnet_uri(self, url):
        # https://github.com/danfolkes/Magnet2Torrent/issues/6
        # http://stackoverflow.com/questions/12479570/given-a-torrent-file-how-do-i-generate-a-magnet-link-in-python

        session = libtorrent.session()
        filename = self.download_file(url)
        info = libtorrent.torrent_info(filename)
        return("magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name()))

    def do_replace(self, this, that):
        self.page_buffer = self.page_buffer.replace(this, that)

    # Main functions
    def update_magnet_uri(self):
        print("Updating Magnet URI...")
        for release_id in sorted(self.downloads['release'].keys()):
            if not self.downloads['release'][release_id]['visible']:
                continue
            for arch in self.downloads['release'][release_id]['arch']:
                try:
                    if arch == 'armhf':
                        url = self.downloads['release'][release_id]['rpi-mirrors']['torrent']
                    else:
                        distro_codename = self.downloads['release'][release_id]['codename']
                        distro_version = self.downloads['release'][release_id]['version']
                        distro_state = self.downloads['release'][release_id]['state']
                        distro_type = self.downloads['release'][release_id]['type']
                        url = self.downloads['global']['canonical-torrent'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
                    self.downloads['release'][release_id]['magnet-uri'][arch] = self.generate_magnet_uri(url)
                except Exception as e:
                    print(' *** ERROR: Exception: ' + str(e))

    def read_json(self):
        # Read download information.
        print('Reading downloads JSON...')
        try:
            with open(self.downloads_json_path) as data_file:
                self.downloads = json.load(data_file)
        except Exception as e:
            print('\nERROR: Invalid JSON!\n' + str(e) + '\n')
            exit()

        print('Reading downloads template...')
        f = open(self.source_template_path, 'r+')
        self.page_buffer = f.read()

    def save_json(self):
        # Write JSON in memory to disk.
        print("Saving updated downloads JSON...")
        try:
            with open(self.downloads_json_path, 'w') as outfile:
                json.dump(self.downloads, outfile, indent=4, sort_keys=True)
        except Exception as e:
            print('\nERROR: Unable to open file for writing!\n' + str(e) + '\n')
            exit()

    def manipulate_page(self):
        print('Manipulating contents...')
        all_releases = sorted(self.downloads['release'].keys())

        for release_id in all_releases:
            version = 'version-' + release_id

            if not self.downloads['release'][release_id]['visible']:
                self.do_replace('href="#' + version + '"', 'style="display:none"')
                continue

            distro_codename = self.downloads['release'][release_id]['codename']
            distro_version = self.downloads['release'][release_id]['version']
            distro_state = self.downloads['release'][release_id]['state']
            distro_type = self.downloads['release'][release_id]['type']

            print('\n-------- ' + distro_version + ' --------')

            # Release Name
            # --- version-[X]-FRIENDLY-NAME
            self.do_replace(version + '-FRIENDLY-NAME', self.downloads['release'][release_id]['name'])

            # Release Notes URL
            # --- version-[X]-RELEASE-URL
            self.do_replace(version + '-RELEASE-URL', self.downloads['release'][release_id]['release-notes'])

            # Torrent URL
            # --- version-[X]-TORRENT-URL-[arch]
            for arch in self.downloads['release'][release_id]['arch']:
                if arch == 'armhf':
                    url = self.downloads['release'][release_id]['rpi-mirrors']['torrent']
                    self.do_replace(version + '-TORRENT-URL-' + arch, url)
                else:
                    url = self.downloads['global']['canonical-torrent'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
                    self.do_replace(version + '-TORRENT-URL-' + arch, url)

                # Link text for torrent
                # --- version-[X]-TORRENT-NAME-[arch]
                url_file = url.split('/')[-1]
                self.do_replace(version + '-TORRENT-NAME-' + arch, url_file)

                # Magnet URI for torrent
                # --- version-[X]-MAGNET-URI-[arch]
                magnet_uri = self.downloads['release'][release_id]['magnet-uri'][arch]
                self.do_replace(version + '-MAGNET-URI-' + arch, magnet_uri)

            # Direct URL
            # --- version-[X]-DIRECT-URL-[arch]
            # --- version-[X]-DIRECT-URL-[arch]-[server]  (for Raspberry Pi downloads)
            #
            # Link text for direct download
            # --- version-[X]-DIRECT-NAME-[arch]
            # --- version-[X]-DIRECT-NAME-[arch]-[server]  (for Raspberry Pi downloads)
            for arch in self.downloads['release'][release_id]['arch']:
                if arch == 'armhf':
                    for server in self.downloads['global']['rpi_servers']:  # eu, ca, fr...
                        url = self.downloads['release'][release_id]['rpi-mirrors'][server]
                        self.do_replace(version + '-DIRECT-URL-' + arch + '-' + server, url)
                        url_file = url.split('/')[-1]
                        self.do_replace(version + '-DIRECT-NAME-' + arch + '-' + server, '<b>' + self.downloads['global'][server] + '</b> - ' + url_file )
                    size = self.get_download_size(url)
                    self.do_replace(version + '-SIZE-' + arch, size)

                else:
                    url = self.downloads['global']['canonical-iso'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
                    url_file = url.split('/')[-1]
                    self.do_replace(version + '-DIRECT-URL-' + arch, url)
                    self.do_replace(version + '-DIRECT-NAME-' + arch, url_file)
                    size = self.get_download_size(url)
                    self.do_replace(version + '-SIZE-' + arch, size)

            # SHA256 Checksum for ISO
            # --- version-[X]-SHA256-[arch]
            for arch in self.downloads['release'][release_id]['arch']:
                sha256sum = self.downloads['release'][release_id]['sha256sum'][arch]
                self.do_replace(version + '-SHA256-' + arch, sha256sum)

            # Show alert box about LTS status
            # "LTS-CODENAMES" => Replace with version that is an LTS. Only one currently supported to be at the moment.
            # //version-[X]-show-LTS    => Code inject, to show #LTS using jQuery.
            # LTS_END_DATE               => Replaced with LTS Date.
            if self.downloads['release'][release_id]['lts']:
                self.do_replace('LTS-CODENAMES', version)
                self.do_replace('LTS_END_DATE', self.downloads['release'][release_id]['lts-end-date'])
                self.do_replace('//' + version + '-show-LTS', "$('#LTS').show();")

            # Show a danger alert for specific versions, if applicable.
            # E.g. serve bug, inform of experimental, or reaching end of life.
            if self.downloads['release'][release_id]['show-warning']:
                classes = "alert alert-danger"
                self.do_replace('id="' + version + '-WARNING" hidden', 'class="' + version + ' ' + classes + '"')
                self.do_replace(version + '-WARNING-HEADER', self.downloads['release'][release_id]['warning-header'])
                self.do_replace(version + '-WARNING-TEXT', self.downloads['release'][release_id]['warning-text'])

            # Other Downloads Page
            # --- version-[X]-OTHER
            url = self.downloads['global']['canonical-other-folder'].replace('OSVERSION', distro_version).replace('STATE', distro_state).replace('TYPE', distro_type)
            self.do_replace(version + '-OTHER', url)

            # Now actually replace version ID with release's codename.
            # version-A             =>      xenial
            self.do_replace(version, distro_codename)

    def generate_paypal_links(self):
        print('Generating PayPal Download Tips...')
        # Replaces "PAYPAL-DOWNLOAD-TIPS" on page.
        tip_amounts = ['2.50','5','10','20']
        # Variables = CLASS / AMOUNT / VERSION / ARCH
        form_start = '<div class="CLASS col-xs-3"><form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" method="post">\n'
        form_field = '<fieldset><button type="submit" class="btn btn-primary">Tip us <b>$AMOUNT</b></button></fieldset>\n'
        form_input = '<input type="hidden" name="cmd" value="_xclick"> \
         <input type="hidden" name="business" value="6282B4CZGVCB6"> \
         <input type="hidden" name="item_name" value="Ubuntu MATE VERSION ARCH Download Tip"> \
         <input type="hidden" name="no_shipping" value="1"> \
         <input type="hidden" name="no_note" value="1"> \
         <input type="hidden" name="charset" value="UTF-8"> \
         <input type="hidden" name="amount" value="AMOUNT"> \
         <input type="hidden" name="currency_code" value="USD"> \
         <input type="hidden" name="src" value="1"><input type="hidden" name="sra" value="1"> \
          <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/"> \
          <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">\n'
        form_end = '</form></div>\n'

        paypal_buffer = ''
        all_releases = sorted(self.downloads['release'].keys())
        for release_id in all_releases:
            if not self.downloads['release'][release_id]['visible']:
                continue

            for arch in self.downloads['release'][release_id]['arch']:
                CLASS = self.downloads['release'][release_id]['codename'] + '-' + arch
                VERSION = self.downloads['release'][release_id]['version']

                # Rename any arch names:
                if arch == 'i386':
                    ARCH = 'for 32-bit machines'
                elif arch == 'amd64':
                    ARCH = 'for 64-bit machines'
                elif arch == 'powerpc':
                    ARCH = 'for PowerPC'
                elif arch == 'armhf':
                    ARCH = 'for Raspberry Pi 2 and 3'
                else:
                    ARCH = arch

                for AMOUNT in tip_amounts:
                    paypal_buffer = paypal_buffer + form_start.replace('CLASS',CLASS).replace('AMOUNT',AMOUNT).replace('VERSION',VERSION).replace('ARCH',ARCH)
                    paypal_buffer = paypal_buffer + form_field.replace('CLASS',CLASS).replace('AMOUNT',AMOUNT).replace('VERSION',VERSION).replace('ARCH',ARCH)
                    paypal_buffer = paypal_buffer + form_input.replace('CLASS',CLASS).replace('AMOUNT',AMOUNT).replace('VERSION',VERSION).replace('ARCH',ARCH)
                    paypal_buffer = paypal_buffer + form_end.replace('CLASS',CLASS).replace('AMOUNT',AMOUNT).replace('VERSION',VERSION).replace('ARCH',ARCH)

        self.page_buffer = self.page_buffer.replace('PAYPAL-DOWNLOAD-TIPS', paypal_buffer)

    def write_download_page(self):
        print('Writing new download page...')
        os.remove(self.target_destination_path)
        file = open(self.target_destination_path, "w")
        for line in self.page_buffer.split('\n'):
            file.write(line + '\n')
        file.close()

if __name__ == "__main__":
    run = DownloadPageScript()
