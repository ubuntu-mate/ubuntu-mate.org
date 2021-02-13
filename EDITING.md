# Editing content on ubuntu-mate.org

The source language of the website is primarily **British English**. :gb:

## Markdown

The usual Markdown syntax is used primarily throughout the website. Liquid is also used
which can be identified by the double curly brackets: `{{ text }}` or `{% text %}`.

**No HTML snipits please.** Create an `include` and reference this on the page instead.
This is because translators will be exposed to all of the content in a Markdown file.

To aid translators, please leave gaps between large sections of text and headings with a
clear single line gap.

In addition, one or more classes may be applied to some Markdown elements, for example,
to support images:

```
{:.center .small}
![alt text](/images/example.png)
```

Tables are supported, like as used on GitHub:

```
| Title Header          | Column 2          |
| --------------------- | ----------------- |
| Apple                 | Banana
| Cat                   | Dog
```

One or more classes can be added before the table, such as:

* `.transparent` to drop the borders and colours.
* `.icons` to center align contents, designed for 2 rows and columns of icons.

Both of them together would be `{:.transparent .icons}` just above the table syntax.

## Creating a Page

In order for the i18n process to work, all pages **must** be placed in a flat structure
in `pages/`, meaning no subdirectories.

The frontmatter are the lines between `---` at the top of the file.

```
---
layout: page
title: New Page
permalink: /untitled/
lang: en
class: about
---
```

See [Layouts](#Layouts) below for descriptions and parameters of layouts you may use.
Some layouts and includes require YAML data in the frontmatter.

On all pages, `class` is used to indicate the current page on the header.
See [`_data/navigation.yml`](_data/navigation.yml) for the correct value.

## Downloads

The data is stored in `_data/downloads.yml`:

* The **`releases`** key lists the versions currently available.
* The **`arch`** key is a list of architectures. When adding/removing here, make changes in `pages/download.md` too.
* The **`downloads`** key lists the downloads (releases) for each `arch`.

Architectures may include ports to other devices, such as `gpd_pocket`.

The URL, torrent and magnet URI is required. To obtain the magnet
link automagically, set the `magnet-uri` key to `autogen` like so:

```
- release: bionic
  ~~snip~~
  magnet-uri: autogen
```

Then pass `--magnet-uri` to the `build` or `watch` script, which will overwrite
`autogen` with the actual URI. This requires `transmission-show` to be installed.

    ./scripts/watch.sh --magnet-uri


## Layouts (`_layouts`)

Here is the YAML data to place in the page's frontmatter when the layout is in use.

#### `page`

The most basic kind of page, just the header, footer and page title are displayed.

#### `page-category`

Requires `category` to point to a class specified in
[`_data/categories.yml`](_data/categories.yml). This is so the correct subnavigation
items appear.

#### `blog-post`
```
category: `dev` or `release` or `news`
```

#### `catalogue`
**Inherits:** [page-category](#page-category)

```
  - group: Name of Group
    items:
      - name: "Name of Item"
        price: "Appears in green text"
        img: /path/to/image
        url: https://example.com
        description: >-

            Description goes here.

      - name: "Next item", etc
        price:
        ...
```

#### `error-serious`
```
error: 500
error_name: Internal Server Error
```

#### `feature-page`
**Inherits:** [page-category](#page-category)

Filenames are an exception on this page, they just need to be the filename (without file
extension) and be placed in `images/features/` and `images/features/2x/`.

```
# Whether to place the image on the left or right.
swap_position: false

main_image_filename: placeholder
main_image_alt:
main_title: Make the desktop unique to you.
main_subtitle: Set up the panels to resemble your familiar workflow.
main_text: >-

    Main body of text.

left_image_filename: placeholder
left_image_alt:
left_title: Cupertino
left_subtitle: A dock and menu bar, similar to the aesthetic of macOS.

middle_image_filename: placeholder
middle_image_alt:
middle_title: Redmond
middle_subtitle: Most familiar to Windows users.

right_image_filename: placeholder
right_image_alt:
right_title: Mutiny
right_subtitle: The lightweight alternate recognised by Ubuntu Unity users.
```

#### `history`
**Inherits:** [page-category](#page-category)

The Markdown for this page should be structured like so:

* **h2** - date/release, appears in sidebar.
* **h3** - the title
* an optional image with the class `milestone-image`
* Markdown content as usual

```
## Pre-2014
### The Ubuntu MATE backstory

{:.milestone-image}
![MATE is a fork of GNOME 2](/images/history/gnome-mate-fork.svg)
```

#### `page-banner`
```
banner_bg: /images/ubuntu-mate/404.jpg
banner_fg: /images/ubuntu-mate/logo.svg (Optional)
banner_title: Text goes here
banner_subtitle: Text goes here
banner_label: null  (Optional)
banner_url: (Optional)
```

#### `sidebar`

Requires `sidebar` to point to a valid key specified in
[`_data/sidebar.yml`](_data/categories.yml). This is so the sidebar is populated
with the correct items.

There are no strings in `sidebar.yml`, so please add new ones to `strings.yml` as
appropriate.


#### `team`

The Markdown on this page appears at the bottom, which is for Special Thanks and
Contributors.

The data for the circle and their icons can be found at `_data/team.yml`.


#### `testimonals`
```
testimonials:

    - who: "Author Name"
      handler: "@example1"
      url: "http://example.com"
      avatar: null
      quote: "We love Ubuntu MATE!"

    - who: "Author Name"
      handler: "@example2"
      url: "http://example.com"
      avatar: null
      quote: "For a retrospective future."

youtube:
    - embed_url: "https://www.youtube.com/embed/XXXXXXXXXXX?start=510&rel=0"
      who: "Name from Example Organisation"
      quote: "This is a sample sentence."
      subject: "Software Boutique in Ubuntu MATE 15.10"
```

### Pre-determined

These are pre-determined for special purposes and shouldn't be used for new pages.

* `blog-index`
* `download`
* `feature-grid`
* `post-download`
* `search`

## Adding Blog Posts

When _watching_ the site, the posts in `_drafts` will be visible in your local copy.
These are drafts and won't be published, making it useful for copying templates.

The `description` and `author` fields may be used by blog posts.

## Includes (`_includes`)

#### Alerts
```
{% include blog/alert.html
    title = "Something went wrong."
    text = "Some text goes here."
    style = "warning" or "error"
%}
```

#### Gallery
Add `{% include blog/gallery.html %}` to the page, and add YAML to the front matter:

```
gallery:
    - image: /images/homepage/01_familiar.png
      caption: null
    - image: /images/homepage/02_contemporary.png
      caption: null
```

Only one gallery is supported per page.

#### Jumbotron
Usually to present call to actions, commonly used on the blog.
```
{% include blog/jumbotron.html

    title = "Download Ubuntu MATE today"
    text = "This new release will be first available for PC/Mac users."
    button_text = "Download"
    button_url = "/download/"

%}

```

#### Known Issues
Shows a table of currently known issues with the distro. This data is stored
at `_data/known-issues.yml`. A `filter` can be optionally specified.
```
{% include partials/known-issues.html filter="20.10" %}
```

#### YouTube Embed
When using the "Share" functionality on YouTube, extract the URL and place it
inside this `include` on the page:
```
{% include embed/youtube.html
    embed = "https://www.youtube.com/embed/XXXXXXXXXXX"
%}
```

#### Other Embeds

* `embed/download-tip-paypal.html` - used on post download page.
* `embed/paypal.html` - used on funding pages.
* `embed/twitter.html` (with parameter `handler`) - used on blog page.

These are re-used across page layouts and shouldn't be used in Markdown files:

* `partials/banner.html`
* `partials/blog-metadata.html`
* `partials/blog-sidebar.html`
* `partials/categories.html`

#### Raspberry Pi Compatibilty Table

The data files are at:

* `_data/raspberry_pi_models.yml` - for architecture compatibilty
* `_data/raspberry_pi_releases.yml` - for release compatibilty

Adding new releases to `raspberry_pi_releases.yml` will require some table
tweaks to the HTML at `partials/pi-compatibility-table.html` (the heading
and conditional check)

## Images

All images are to be kept in this folder. Reference them on any page or blog post via
Markdown:

```
![alt text](/images/folder/image.png)
````

**HiDPI Displays**

* Currently, only the **Features** page supports @2x images for HiDPI displays.

**WebP Support**

* The published website will automatically optimise the image's compression
efficency by creating a WebP version of the image. The server is configured to
serve this asset in-place of existing image files were available.
* Some templates in the code use the `<picture>` tag to reference the WebP.

SVGs that are used on buttons and styling may be placed in `_includes/images/` instead,
which appends SVG directly into the page for manipulation through styling.

## Adding Redirects

Create a new file and amend as necessary:
```
---
layout: redirect
permalink: /vivid/
destination: /old-release/
---
```

Redirects for old URLs are essential to maintain strong links for websites linking to
legacy pages once used on this website.

