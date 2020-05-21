#!/usr/bin/python3
#
# Run this script to generate PO/POT files from the original markdown files.
#
# This enables them to be translated via Transifex.
#
# Requires:
#   - txt2po (provided in 'translate-toolkit')
#   - po2txt (provided in 'translate-toolkit')
#

import argparse
import os
import glob
import shutil
import subprocess
import sys
import polib

def check_if_installed(cmd, package):
    if not shutil.which(cmd):
        print("Command for '{0}' missing. Please install '{1}'")
        exit(1)

check_if_installed("po2txt", "translate-toolkit")
check_if_installed("txt2po", "translate-toolkit")
check_if_installed("msgmerge", "translate-toolkit")

# Directories
os.chdir(os.path.join(os.path.dirname(__file__), "../"))
base_dir = os.path.join(os.path.dirname(__file__), "../")
page_dir = "pages"
post_dir = "_posts"
yaml_dir = "_data"
i18n_dir = "_i18n"
dest_dir = "pages/i18n"

# External helper scripts
yaml2po = os.path.join(base_dir, "scripts/helpers/yaml2po")
po2yaml = os.path.join(base_dir, "scripts/helpers/po2yaml")

# Ensure output directory exists
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

# Gather file list
def read_file(path):
    with open(path, "r") as f:
        return "".join(f.readlines())

file_list = glob.glob(page_dir + "/*.md") + glob.glob(post_dir + "/*.md")
locale_list = read_file(os.path.join(i18n_dir, "locales.txt")).split("\n")

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
    strings_yml_pot = "{0}/pots/strings.pot".format(i18n_dir)
    run("{0} -P {1} {2}".format(yaml2po, strings_yml, strings_yml_pot))

    print("Regenerating locale po files...")
    locale_no = 0
    page_no = 0
    for locale in locale_list:
        locale_no += 1
        if not locale:
            continue

        locale = locale.strip()

        # For each markdown page, generate new POT and merge with existing.
        for path in file_list:
            page_no += 1
            page = path.replace(".md", "").split("/")[-1]
            print("  [{0}/{1}] {2}: {3}".format(page_no, len(file_list) * (len(locale_list) - 1), locale, page))

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
        if os.path.exists(os.path.join(strings_yml_po)):
            run("msgmerge {0} {1} > new_po.tmp".format(strings_yml_po, strings_yml_pot))
            os.rename("new_po.tmp", strings_yml_po)
        else:
            shutil.copy(strings_yml_pot, strings_yml_po)


def build():
    locale_no = 0
    page_no = 0
    print("Generating markdown files...")

    # Clear previously generated markdown files
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    for locale in locale_list:
        locale_no += 1
        if not locale:
            continue

        locale = locale.strip()

        # Create new markdown files from translated PO files.
        for path in file_list:
            page_no += 1
            page = path.replace(".md", "").split("/")[-1]
            print("  [{0}/{1}] {2}: {3}".format(page_no, len(file_list) * (len(locale_list) - 1), locale, page))

            src = os.path.join(i18n_dir, locale, page + ".po")
            dst = os.path.join(dest_dir, page + "." + locale + ".md")
            run("po2txt --template {path} {src} {dst}".format(path=path, src=src, dst=dst))

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
        yaml_src = os.path.join(i18n_dir, locale, "strings.po")
        yaml_dst = os.path.join(yaml_dir, locale, "strings.yml")
        if os.path.exists(yaml_src):
            run("{0} {1} {2}".format(po2yaml, yaml_src, yaml_dst))


# Process arguments
try:
    arg = sys.argv[1]
except Exception:
    print("Usage:")
    print("    manage-translations.sh [--generate] [--build]")
    exit(0)

if arg == "--generate":
    generate()
elif arg == "--build":
    build()
else:
    print("Invalid parameter")
    exit(1)
