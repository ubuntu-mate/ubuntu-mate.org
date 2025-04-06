# ubuntu-mate.org

![CI](https://github.com/ubuntu-mate/ubuntu-mate.org/workflows/CI/badge.svg)

The website for discovering and downloading the Ubuntu MATE operating system.

Powered by [Jekyll](https://jekyllrb.com/), a static site generator.

![Screenshot of website](.github/preview.png)


## Getting Started

See [EDITING.md](EDITING.md) for notes on adding/editing pages on this website.

**Translators,** please see the [Translations](#Translations) section instead.

### Using GitHub

Find the file you want on GitHub to edit, then click the pencil icon to start
editing. This is the easiest way to propose changes and create a pull request
for single files.

### Using a local copy

This has the advantage to preview your changes.

1. Install [Jekyll for Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/) (or other distro)

2. Install the dependencies for this website:

       bundle install

   Some additional packages are used to build the project:

       sudo apt install python3-requests python3-yaml transmission-cli python3-polib translate-toolkit webp

3. To build and preview changes locally:

       ./scripts/watch.sh

    The first build may take a while to complete, but will be substantially faster
    afterwards.

4. Preview the website on your computer at <http://localhost:4000>. Any changes you make will be live reloaded and include unpublished drafts.


## Testing

Continuous Integration will perform validation checks to ensure the website
maintains a high quality standard for visitors around the world. Before running
tests on your local machine, install the Ruby gem:

    gem install html-proofer

Then thereon after, you may run:

    ./scripts/test.sh

This will check internal links, images and page metadata for errors.

From time to time, you may wish to run the test with `--external` to check
links to other websites, blogs or people pages in case of [link rot](https://en.wikipedia.org/wiki/Link_rot).


## Translations

We are ready to speak multiple languages! Visit
[Transifex](https://www.transifex.com/ubuntu-mate/ubuntu-mate.org/)
to translate this website. The Ubuntu MATE team will pull in completed translations.

Please refer to the [guidelines](https://ubuntu-mate.community/t/22342) for
the best practices.

We use the [polyglot](https://github.com/untra/polyglot) gem to provide i18n support.

To add new locales, add the language code in:

* `_i18n/locales.txt`
* `_config.yml` (under `languages:`)
* `_data/lang.yml`

As part of the build process, markdown files for other languages are generated
via `scripts/manage-translations.py`. This can be ran manually too:

| Parameter             | Action                                            |
|-----------------------|---------------------------------------------------|
| `--generate`          | Will create POT files and updates PO files from pages.
| `--build`             | Will process translated PO files into Markdown files.

When pages change, run `--generate`. Before building the site, run `--build`.


If you're just testing locally and wish to preview at <http://localhost:4000>, all you need to run:

    ./scripts/watch.sh --locales



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
| `redirects`       | Meta redirects from legacy links.


## License

Refer to the [LICENSE.md](LICENSE.md) file for copyright and licensing notices
for this website.
