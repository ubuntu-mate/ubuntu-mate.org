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

To install gem dependencies for the website:

    bundle install

To preview locally:

    bundle exec jekyll serve --watch --livereload

You can preview the website on your computer at http://localhost:4000.

If you need to update the gems (dependencies) later:

    bundle update


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
| `_drafts`         | Blog posts (markdown) not ready for publishing yet.
| `images`          | Images used across the site.
| `pages`           | Page contents (markdown)
| `_posts`          | Blog entries (markdown)

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
| `i18n`            | Compiled translated files (.md) for building.
| `_i18n`           | Source files (.pot, .po) for translating.
| `redirects`       | Meta redirects from legacy website.


## License

Refer to the [LICENSE.md](LICENSE.md) file for copyright and licensing notices
for this website.
