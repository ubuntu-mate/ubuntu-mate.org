#!/usr/bin/python3
#
# A simple test that verifies pages and blogs for ALL locales
# have the required keys.
#
import os
import glob

repo_root = os.path.dirname(os.path.realpath(__file__) + "../../")
error = False

pages = []

for regex in ["pages/*.md", "pages/i18n/*.md", "_posts/*.md", "_drafts/*.md"]:
    paths = glob.glob(regex)
    for path in paths:
        pages.append(path)

print("\nValidating {0} pages for consistency...\n".format(len(pages)))
for path in pages:
    with open(path, "r") as f:
        content = " ".join(f.readlines())
    for key in ["layout:", "title:", "permalink:", "lang"]:
        if content.find(key) == -1:
            print("Missing '{0}' in {1}".format(key, path))
            error = True

if error:
    print("\nErrors found.\n")
    exit(1)
else:
    print("\nNo errors found.")
    exit(0)
