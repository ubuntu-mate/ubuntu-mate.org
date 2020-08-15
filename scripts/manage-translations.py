#!/usr/bin/python3
#
# Run this script to generate PO/POT files from the original markdown files.
#
# This enables them to be translated via Transifex.
#
# Requires:
#   - txt2po (provided in 'translate-toolkit')
#   - po2txt (provided in 'translate-toolkit')
#   - polib (provided in "python3-polib")
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import argparse
import os
import glob
import shutil
import subprocess
import sys
import polib

MINIMUM_PERCENT = 50

def check_if_installed(cmd, package):
    if not shutil.which(cmd):
        print("Command for '{0}' missing. Please install '{1}'")
        exit(1)

check_if_installed("po2txt", "translate-toolkit")
check_if_installed("txt2po", "translate-toolkit")
check_if_installed("msgmerge", "translate-toolkit")
check_if_installed("po2yaml", "translate-toolkit")
check_if_installed("yaml2po", "translate-toolkit")

# Directories
os.chdir(os.path.join(os.path.dirname(__file__), "../"))
base_dir = os.path.join(os.path.dirname(__file__), "../")
page_dir = "pages"
post_dir = "_posts"
yaml_dir = "_data"
i18n_dir = "_i18n"
dest_dir = "pages/i18n"

# Ensure output directory exists
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

# Gather locale list
def read_file(path):
    with open(path, "r") as f:
        return "".join(f.readlines())
locale_list = read_file(os.path.join(i18n_dir, "locales.txt")).split("\n")

# Gather pages - exclude non-translatable 50x error pages.
page_list = []
for page in glob.glob(page_dir + "/*.md"):
    if os.path.basename(page).startswith("50"):
        continue
    page_list.append(page)

# Gather posts - exclude blog posts before 2019 and translated posts
post_list = []
i18n_posts = glob.glob(post_dir + "/*.*.md")

for post in glob.glob(post_dir + "/*.md"):
    if os.path.basename(post)[:4] in ["2018", "2017", "2016", "2015", "2014"]:
        continue
    post_list.append(post)

for post in i18n_posts:
    post_list.remove(post)

# Put together lists
file_list = page_list + post_list

# Ensure locale has a folder
for locale in locale_list:
    src_locale = os.path.join(i18n_dir, locale)
    if not os.path.exists(src_locale):
        os.mkdir(src_locale)

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

if not os.path.exists(os.path.join(i18n_dir, "pots")):
    os.mkdir(os.path.join(i18n_dir, "pots"))

# Run commands
def run(command):
    try:
        proc = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("ERROR: Failed to run " + command)

# Operations for arguments
def generate():
    page_no = 0

    # For each markdown page, generate new POT and merge with existing.
    print("Generating pots...")
    for path in file_list:
        page_no += 1
        page = path.replace(".md", "").split("/")[-1]

        print("  [{0}/{1}] {2}.pot".format(page_no, len(file_list), page))

        pot_path = "{0}/pots/{1}.pot".format(i18n_dir, page)

        # Generate POT file
        run("txt2po --pot {0} {1}".format(path, pot_path))

        # Strip out critical strings that should not be translated.
        #
        # Strings are separated by new lines. Placing a "#noi18n" inside a "string"
        # will omit it from the PO/POT files.
        #
        # Frontmatter (single "---" and "layout:" string blocks) are also ignored.
        pot = polib.pofile(pot_path)

        for entry in list(pot):
            remove = False

            # Exclude end of frontmatter
            if entry.msgid == "---":
                remove = True

            # Exclude start of frontmatter
            elif entry.msgid.find("layout: ") != -1:
                remove = True

            # Exclude items explictly commented with "noi18n"
            elif entry.msgid.find("noi18n") != -1:
                remove = True

            # Exclude all-in-one include tags
            elif entry.msgid.find("{%") != -1:
                remove = True

            elif entry.msgid.find("%}") != -1:
                remove = True

            if remove:
                pot.remove(entry)

        pot.save(pot_path)

    # Re-generate a POT for strings.yml (for translating _includes and _layouts)
    strings_yml = "{0}/strings.yml".format(yaml_dir)
    strings_pot = "{0}/pots/strings.pot".format(i18n_dir)
    run("yaml2po -i {0} -o {1}".format(strings_yml, strings_pot))

    print("Refreshing locale po files...")
    for locale_no, locale in enumerate(locale_list):
        locale_no += 1
        if not locale:
            continue

        locale = locale.strip()

        # For each markdown page, generate new POT and merge with existing.
        for page_no, path in enumerate(file_list):
            page_no += 1
            page = path.replace(".md", "").split("/")[-1]
            print("  [{0}/{1}] {2}: {3}".format(page_no, len(file_list), locale, page))

            pot_path = "{0}/pots/{1}.pot".format(i18n_dir, page)
            po_path = "{0}/{1}/{2}.po".format(i18n_dir, locale, page)

            # Update PO files (merging existing data if it exists)
            if os.path.exists(os.path.join(po_path)):
                run("msgmerge {0} {1} > new_po.tmp".format(po_path, pot_path))
                os.rename("new_po.tmp", po_path)
            else:
                shutil.copy(pot_path, po_path)

        # Update strings.po
        strings_yml_po = "{0}/{1}/strings.po".format(i18n_dir, locale)
        strings_yml_pot = "{0}/pots/strings.pot".format(i18n_dir)
        if os.path.exists(os.path.join(strings_yml_po)):
            run("msgmerge {0} {1} > new_po.tmp".format(strings_yml_po, strings_yml_pot))
            os.rename("new_po.tmp", strings_yml_po)
        else:
            shutil.copy(strings_yml_pot, strings_yml_po)


def build():
    print("Generating markdown files...")

    # Clear previously generated markdown files
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    for post in i18n_posts:
        os.remove(post)

    total = len(locale_list) * len(file_list)
    for locale_no, locale in enumerate(locale_list):
        if not locale:
            continue

        locale = locale.strip()

        # Create new markdown files from translated PO files.
        for page_no, path in enumerate(file_list):
            page = path.replace(".md", "").split("/")[-1]
            is_post = page.startswith("20")
            page_no += 1

            current = page_no + (len(file_list) * locale_no)
            print("  [{0}/{1}] {2}: {3}".format(current, total, locale, page))

            src = os.path.join(i18n_dir, locale, page + ".po")
            dst = os.path.join(dest_dir, page + "." + locale + ".md")
            if is_post:
                dst = os.path.join(post_dir, page + "." + locale + ".md")
            run("po2txt --fuzzy -t {path} {src} {dst}".format(path=path, src=src, dst=dst))

            # Ensure language code is definitely set.
            contents = ""
            with open(dst, "r") as f:
                contents = "".join(f.readlines())
            contents = contents.replace("lang: en", "lang: " + locale)
            with open(dst, "w") as f:
                f.writelines(contents)

        # Create new translated string.yml file.
        yaml_locale_dir = os.path.join(yaml_dir, locale)
        if not os.path.exists(yaml_locale_dir):
            os.mkdir(yaml_locale_dir)

        # Update an existing strings.po file if exists.
        strings_po = os.path.join(i18n_dir, locale, "strings.po")
        template_yml = os.path.join(yaml_dir, "strings.yml")
        strings_yml = os.path.join(yaml_dir, locale, "strings.yml")
        if os.path.exists(strings_po):
            run("po2yaml --fuzzy -i {0} -t {1} -o {2}".format(strings_po, template_yml, strings_yml))


def sync():
    print("Generating .tx/config file...")
    tx_file = base_dir + "/.tx/config"

    tx_data = []
    tx_data.append("[main]\n")
    tx_data.append("host = https://www.transifex.com\n")
    a_z_file_list = sorted(page_list) + sorted(post_list)

    def _add_to_tx(filename):
        tx_data.append("\n[ubuntu-mate-org.{0}]\n".format(filename))
        tx_data.append("file_filter = _i18n/<lang>/{0}.po\n".format(filename))
        tx_data.append("source_file = _i18n/pots/{0}.pot\n".format(filename))
        tx_data.append("source_lang = en\n")
        tx_data.append("type = PO\n")

    for page in a_z_file_list:
        filename = os.path.basename(page).replace(".md", "")
        _add_to_tx(filename)

    # strings.yml is in the _data directory
    _add_to_tx("strings")

    with open(tx_file, "w") as f:
        f.writelines(tx_data)

    print("Pulling translations from Transifex... (this may take a while)")
    check_if_installed("tx", "transifex-client")
    run("tx pull -a --minimum-perc=" + str(MINIMUM_PERCENT))

    print("Updating locale lists...")
    lang_paths = glob.glob(i18n_dir + "/*")
    langs = []
    for path in lang_paths:
        if path.find("locales.txt") != -1 or path.find("pots") != -1:
            continue
        langs.append(path.split("/")[-1])

    total_pots = len(glob.glob(i18n_dir + "/pots/*.pot"))
    completed_langs = []
    for lang in langs:
        lang = os.path.basename(lang)
        if lang == "pots" or lang == "locales.txt":
            continue

        # Only add locale if it meets the threshold
        lang_po = len(glob.glob(i18n_dir + "/" + lang + "/*"))
        percent = int((lang_po / total_pots) * 100)
        complete = percent >= MINIMUM_PERCENT

        if complete:
            print("|               | Will be published", end="\r")
            completed_langs.append(lang)
        print("|               |".format(percent),end="\r")
        print("|       | {0}%".format(percent),end="\r")
        print("| {0}".format(lang))

    # (1) _i18n/locales.txt for our scripts.
    with open(i18n_dir + "/locales.txt", "w") as f:
        f.writelines("\n".join(completed_langs))

    # (2) _config.yml for the jekyll-polyglot gem.
    with open("_config.yml", "r") as f:
        config = f.readlines()

    new_config = []
    for line in config:
        if line.startswith("languages:"):
            line = 'languages: ["en"'
            for lang in completed_langs:
                 line += ', "{0}"'.format(lang)
            line += ']\n'
        new_config.append(line)

    with open("_config.yml", "w") as f:
        f.writelines(new_config)

    # (3) Locale name for the interface
    with open("_data/lang.yml", "r") as f:
        lang_labels = f.readlines()

    f = open("_data/lang.yml", "a")

    missing_langs = []
    for lang in completed_langs:
        if " ".join(lang_labels).find(lang) == -1:
            missing_langs.append(lang)
            f.write('{0}: ""\n'.format(lang))
    f.close()

    if missing_langs:
        print("\nNew language(s):\n    {0}\n".format(", ".join(missing_langs)))

    generate()
    build()

    print("Pushing source translations to Transifex... (this may take a while)")
    run("tx push -s")

    print("\nSync complete.\n")
    print(" \033[5m[!]\033[0m Ready to test/commit the changes. Performing a website build is recommended.")
    if missing_langs:
        print(" \033[5m[!]\033[0m New languages added! Add the strings in: _data/lang.yaml")
    print("")

# Process arguments
try:
    arg = sys.argv[1]
except Exception:
    print("Usage:")
    print("    manage-translations.sh [--generate] [--build] [--sync]")
    print("")
    print("Sync is only possible for managers of Ubuntu MATE Transifex.")
    exit(0)

if arg == "--generate":
    generate()
elif arg == "--build":
    build()
elif arg == "--sync":
    sync()
else:
    print("Invalid parameter")
    exit(1)
