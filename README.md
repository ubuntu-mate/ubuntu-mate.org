# ubuntu-mate.org

[![Build Status](https://travis-ci.org/ubuntu-mate/ubuntu-mate.org.svg?branch=master)](https://travis-ci.org/ubuntu-mate/ubuntu-mate.org)

The website for discovering and downloading the Ubuntu MATE operating system.

Powered by [Jekyll](https://jekyllrb.com/), a static site generator.


## Getting Started

### Edit on GitHub

The easiest way to edit ubuntu-mate.org is to use GitHub to edit the page.
Simply find the page you want and create a pull request!

**Translators,** please see the [Translations](#Translations) section instead.

### Setup

Install [Jekyll](https://jekyllrb.com) as follows:

    sudo apt install ruby ruby-dev make gcc
    sudo gem install jekyll bundler

To install gem dependencies for the project;

    bundle install

Some additional packages are needed to build the project:

    sudo apt install python3-yaml transmission-cli

This website has a few programmatically generated files, so be sure to run:

    ./scripts/build.sh

To watch for changes locally:

    ./scripts/watch.sh

You can preview the website on your computer at http://localhost:4000.


## Translations

We are ready to speak multiple languages! Visit
[Transifex](https://www.transifex.com/ubuntu-mate/ubuntu-mate.org/)
to translate this website. The Ubuntu MATE team will pull in completed translations.

We use the [polyglot](https://github.com/untra/polyglot) gem to provide i18n support.

When building the website, use `scripts/generate-translations.sh` to generate
the necessary files.

| Parameter             | Action                                            |
|-----------------------|---------------------------------------------------|
| `--generate`          | Creates POT and updates PO files from pages.
| `--build`             | Process translated PO files for use with Jekyll.

When pages change, run `--generate`. Before building the site, run `--build`.


## File Structure

### Content Editor

| Folder            | Purpose
|-------------------|-------------------------------------------------------|
| `_data`           | Structured YAML data used for things like download lists.
| `_drafts`         | Blog posts (markdown) not ready to publish. Use `--drafts` parameter to preview.
| `images`          | Images used across the site.
| `pages`           | Page contents (markdown)
| `_posts`          | Blog posts (markdown)

### Development

| Folder            | Purpose
|-------------------|-------------------------------------------------------|
| `_includes`       | HTML to build up sections of the website.
| `_layouts`        | HTML base layouts.
| `_sass`           | Ubuntu MATE theme
| `assets`          | Global website resources, like favicons and libraries.
| `scripts`         | For building and deployment.

### Other

| Folder            | Purpose
|-------------------|------------------------------------------------------|
| `_i18n`           | Source files (.pot, .po) for translating.
| `redirects`       | Meta redirects from legacy website.


## License

Refer to the [LICENSE.md](LICENSE.md) file for copyright and licensing notices
for this website.
