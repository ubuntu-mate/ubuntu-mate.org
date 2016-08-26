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

        # Consistant Variables
        self.archs = ['amd64', 'i386', 'powerpc', 'armhf']

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
                self.strip_starting_spaces()
                self.write_download_page()
            elif arg == '--update-page':
                self.read_json()
                self.manipulate_page()
                self.generate_paypal_links()
                self.strip_starting_spaces()
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
        try:
            response = str(subprocess.Popen(['wget','--spider', url], stderr=subprocess.PIPE).communicate()[1])
            response.split('\n')
            size = int(response.split('Length: ')[1].split(' ')[0])
            size_MB = size / 1000 / 1000
            size_GB = size / 1000 / 1000 / 1000
            if size_GB < 1:
                return str(round(size_MB)) + ' MB'
            else:
                return str(round(size_GB,1)) + ' GB'
        except:
            print(' ** Failed to download metadata for: ' + url_name)
            print(' ** Does this file exist on the server?')
            return 'Unknown'

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
            for arch in self.archs:
                try:
                    if arch == 'armhf':
                        url = self.downloads['release'][release_id]['rpi-mirrors']['torrent']
                    else:
                        distro_codename = self.downloads['release'][release_id]['codename']
                        distro_version = self.downloads['release'][release_id]['version']
                        distro_state = self.downloads['release'][release_id]['state']
                        distro_shortstate = self.downloads['release'][release_id]['shortstate']
                        distro_type = self.downloads['release'][release_id]['type']
                        if distro_state.startswith('alpha'):
                            url = self.downloads['global']['canonical-alpha-iso'].replace('CODENAME', distro_codename).replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type) + '.torrent'
                        elif distro_state.startswith('beta'):
                            url = self.downloads['global']['canonical-alpha-iso'].replace('CODENAME', distro_codename).replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('SHORT', distro_shortstate).replace('TYPE', distro_type) + '.torrent'
                        else:
                            url = self.downloads['global']['canonical-iso'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type) + '.torrent'

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

        # Prepare the data to append into.
        buffer_release_list = ""
        buffer_rpi_class = ""
        buffer_release_notes = ""
        buffer_torrent_links = ""
        buffer_magnet_links = ""
        buffer_direct_links = ""
        buffer_direct_uk_links = ""
        buffer_download_sizes = ""
        buffer_checksums = ""
        buffer_alerts = ""
        buffer_other_links = ""
        buffer_javascript = ""
        buffer_variables = ""

        # Iterate through the database.
        for release_id in all_releases:
            version = 'version-' + release_id
            distro_name = self.downloads['release'][release_id]['name']
            distro_codename = self.downloads['release'][release_id]['codename']
            distro_version = self.downloads['release'][release_id]['version']
            distro_state = self.downloads['release'][release_id]['state']
            distro_shortstate = self.downloads['release'][release_id]['shortstate']
            distro_type = self.downloads['release'][release_id]['type']
            distro_release_url = self.downloads['release'][release_id]['release-notes']

            print('\n-------- ' + distro_version + ' --------')

            ## Releases
            template = '<li id="' + distro_codename + '" role="presentation"><a href="#' + distro_codename + '" role="tab" data-toggle="tab"><big><img src="/favicon-32.png"/> ' + distro_name + '</big></a></li>'
            buffer_release_list = buffer_release_list + template + '\n'

            # Raspberry Pi Downloads Available?
            rpi_visible = self.downloads['release'][release_id]['rpi-visible']
            if rpi_visible:
                buffer_rpi_class = buffer_rpi_class + distro_codename + ' '

            ## Release Notes URL
            template = '<p><a class="' + distro_codename + '" href="' + distro_release_url + '"><span class="fa fa-file"></span> Release Announcement</a></p>'
            buffer_release_notes = buffer_release_notes + template + '\n'

            ## Torrent URL
            for arch in self.archs:
                if arch == 'armhf':
                    url = self.downloads['release'][release_id]['rpi-mirrors']['torrent']
                    url_file = url.split('/')[-1]
                else:
                    if distro_state.startswith('alpha'):
                        url = self.downloads['global']['canonical-alpha-torrent'].replace('CODENAME', distro_codename).replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
                        url_file = url.split('/')[-1]
                    elif distro_state.startswith('beta'):
                        url = self.downloads['global']['canonical-beta-torrent'].replace('CODENAME', distro_codename).replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('SHORT', distro_shortstate).replace('TYPE', distro_type)
                        url_file = url.split('/')[-1]
                    else:
                        url = self.downloads['global']['canonical-torrent'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
                        url_file = url.split('/')[-1]

                template = '<a class="' + distro_codename + '-' + arch + '" href="' + url + '" onclick="thanks()"><span class="fa fa-download"></span> ' + url_file + '</a>'
                buffer_torrent_links = buffer_torrent_links + template + '\n'

                # Magnet URI for torrent
                magnet_uri = self.downloads['release'][release_id]['magnet-uri'][arch]
                template = '<a class="' + distro_codename + '-' + arch + '" href="' + magnet_uri + '" onclick="thanks()"><span class="fa fa-magnet"></span> Magnet Link</a>'
                buffer_magnet_links = buffer_magnet_links + template + '\n'

            ## Direct URL
            for arch in self.archs:
                if arch == 'armhf':
                    # UK Server
                    url = self.downloads['release'][release_id]['rpi-mirrors']['uk']
                    url_file = url.split('/')[-1]
                    template = '<a class="' + distro_codename + '-' + arch + '" href="' + url + '" onclick="thanks()"><b>' + self.downloads['global']['name-uk'] + '</b> - ' + url_file + '</a>'
                    buffer_direct_uk_links = buffer_direct_uk_links + template + '\n'

                else:
                    if distro_state.startswith('alpha'):
                        url = self.downloads['global']['canonical-alpha-iso'].replace('CODENAME', distro_codename).replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
                        url_file = url.split('/')[-1]
                    elif distro_state.startswith('beta'):
                        url = self.downloads['global']['canonical-beta-iso'].replace('CODENAME', distro_codename).replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('SHORT', distro_shortstate).replace('TYPE', distro_type)
                        url_file = url.split('/')[-1]
                    else:
                        url = self.downloads['global']['canonical-iso'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
                        url_file = url.split('/')[-1]

                    template = '<a class="' + distro_codename + '-' + arch + '" href="' + url +'" onclick="thanks()"><span class="fa fa-download"></span> ' + url_file + '</a>'
                    buffer_direct_links = buffer_direct_links + template + '\n'

                # Download Size
                size = self.get_download_size(url)
                template = '<span class="' + distro_codename + '-' + arch + '">' + size + '</span>'
                buffer_download_sizes = buffer_download_sizes + template + '\n'

            # SHA256 Checksums for ISOs
            for arch in self.archs:
                sha256sum = self.downloads['release'][release_id]['sha256sum'][arch]
                template = '<code class="' + distro_codename + '-' + arch + '">' + sha256sum + '</code>'
                buffer_checksums = buffer_checksums + template + '\n'

            # Alert Box for LTS Status
            if self.downloads['release'][release_id]['end-date']:
                end_date = self.downloads['release'][release_id]['end-date']
                if self.downloads['release'][release_id]['lts']:
                    alert_title = "This release has Long Term Support (LTS)"
                    alert_text  = "Recommended if you desire a stable system. Support ends <b>END_DATE</b>.".replace('END_DATE', end_date)
                    template = '<div class="alert alert-success '
                    for arch in self.archs:
                        # Raspberry Pi releases are not long term supported.
                        if not arch == 'armhf':
                            template = template + distro_codename + '-' + arch + ' '

                    template = template + '" hidden>' + \
                                '<p><b><span class="fa fa-info-circle"></span> ' + alert_title + '</b></p>' + \
                                '<p>' + alert_text + '</p>' + \
                            '</div>'
                elif distro_state.startswith('alpha') or distro_state.startswith('beta'):
                    alert_title = "This is a development pre-release"
                    alert_text  = "Suitable for developers and tester who want to help with Ubuntu MATE QA, or to provide testing feedback and file issue reports."
                    template = '<div class="alert alert-warning '
                    # Raspberry Pi releases are not long term supported.
                    for arch in self.archs:
                        template = template + distro_codename + '-' + arch + ' '

                    template = template + '" hidden>' + \
                                '<p><b><span class="fa fa-info-circle"></span> ' + alert_title + '</b></p>' + \
                                '<p>' + alert_text + '</p>' + \
                            '</div>'
                else:
                    alert_title = "This is an intermediate release"
                    alert_text  = "Suitable for people who want to keep up with the latest developments in Ubuntu MATE and Open Source. Support ends <b>END_DATE</b>.".replace('END_DATE', end_date)
                    template = '<div class="alert alert-info '
                    # Raspberry Pi releases are not long term supported.
                    for arch in self.archs:
                        template = template + distro_codename + '-' + arch + ' '

                    template = template + '" hidden>' + \
                                '<p><b><span class="fa fa-info-circle"></span> ' + alert_title + '</b></p>' + \
                                '<p>' + alert_text + '</p>' + \
                            '</div>'
                buffer_alerts = buffer_alerts + template + '\n'

            # Alert Box for Important Issues  (e.g. serve bug, inform of experimental, or end of life.)
            if self.downloads['release'][release_id]['show-warning']:
                warning_title = self.downloads['release'][release_id]['warning-header']
                warning_text  = self.downloads['release'][release_id]['warning-text']
                template = '<div class="alert alert-danger ' + distro_codename + '" hidden>' + \
                             '<p><b><span class="fa fa-warning"></span> ' + warning_title + '</b></p>' + \
                             '<p>' + warning_text + '</p>' + \
                           '</div>'
                buffer_alerts = buffer_alerts + template + '\n'

            # Other Downloads Page
            url = self.downloads['global']['canonical-other-folder'].replace('OSVERSION', distro_version).replace('STATE', distro_state).replace('TYPE', distro_type)
            template = '<a class="' + distro_codename + '" href="' + url + '" target="_blank"><span class="fa fa-bookmark"></span> Other Downloads for ' + distro_version + '</a>'
            buffer_other_links = buffer_other_links + template + '\n'

            # JavaScript Functions
            template = '$( "#' + distro_codename + '" ).click(function() {' + \
                            'show_version = "' + distro_codename + '";' + \
                            'present_version = "' + distro_name + '";' + \
                            'updatePage();' + \
                            '$(\'#arch-list\').slideDown();' + \
                        '});'
            buffer_javascript = buffer_javascript + template + '\n'

        # JavaScript Variables
        buffer_variables = 'var version = {'
        for release_id in all_releases:
            codename = self.downloads['release'][release_id]['codename']
            buffer_variables = buffer_variables + codename + ': "' + codename + '", '
        buffer_variables = buffer_variables[:-2] + '};\nvar arch = {'
        for arch in self.archs:
            buffer_variables = buffer_variables + arch + ': "' + arch + '", '
        buffer_variables = buffer_variables[:-2] + '};\n'

        # Now replace place holders on page.
        self.do_replace('RELEASE-LIST', buffer_release_list)
        self.do_replace('RPI-VISIBLE', buffer_rpi_class)
        self.do_replace('RELEASE-URL', buffer_release_notes)
        self.do_replace('TORRENT-LINKS', buffer_torrent_links)
        self.do_replace('MAGNET-LINKS', buffer_magnet_links)
        self.do_replace('DIRECT-LINKS', buffer_direct_links)
        self.do_replace('DIRECT-UK-LINKS', buffer_direct_uk_links)
        self.do_replace('DOWNLOAD-SIZES', buffer_download_sizes)
        self.do_replace('CHECKSUMS', buffer_checksums)
        self.do_replace('ALERT-PLACEHOLDERS', buffer_alerts)
        self.do_replace('OTHER-DOWNLOAD-LINKS', buffer_other_links)
        self.do_replace('// JAVASCRIPT-FUNCTIONS', buffer_javascript)
        self.do_replace('// JAVASCRIPT-VARIABLES', buffer_variables)

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

            for arch in self.archs:
                CLASS = self.downloads['release'][release_id]['codename'] + '-' + arch
                VERSION = self.downloads['release'][release_id]['version']

                # Rename any arch names:
                if arch == 'i386':
                    ARCH = 'i386'
                elif arch == 'amd64':
                    ARCH = 'amd64'
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

    def strip_starting_spaces(self):
        print('Stripping whitespace...')
        page_buffer_original = self.page_buffer
        page_buffer_new = ""
        for line in page_buffer_original.split('\n'):
            page_buffer_new = page_buffer_new + line.lstrip() + '\n'
        self.page_buffer = page_buffer_new

    def write_download_page(self):
        print('Writing new download page...')
        os.remove(self.target_destination_path)
        file = open(self.target_destination_path, "w")
        for line in self.page_buffer.split('\n'):
            file.write(line + '\n')
        file.close()

if __name__ == "__main__":
    run = DownloadPageScript()
