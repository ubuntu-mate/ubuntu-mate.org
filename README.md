# ubuntu-mate.org

The website for discovering and downloading the Ubuntu MATE operating system.

Powered by [Nikola](https://getnikola.com/) - a static page generator.

[![Build Status](https://travis-ci.org/ubuntu-mate/ubuntu-mate.org.svg?branch=master)](https://travis-ci.org/ubuntu-mate/ubuntu-mate.org)

----------
## Translations

The website is only in English at the moment. **There is currently no way for 
translators yet**, although Nikola has support for multilingual sites.

----------
## Setting up the Nikola Environment

First, install Nikola into an isolated Python environment, called a 
`virtualenv`. This is independent from the system's installation of Python.

    source ~/Snakepit/nikola/bin/activate

You know when the Nikola environment is activated because `(nikola)` will be 
added to the bash prompt.

### Clone the website

    mkdir ~/Websites
    cd ~/Websites
    git clone git@bitbucket.org:ubuntu-mate/ubuntu-mate.org.git

### Build Nikola

The first build will take a while. Subsequent builds are much faster.

    cd ~/Websites/ubuntu-mate.org
    nikola build

### Serving the site

Nikola has a built in webserver, the serves the currently built site on port 
8000.

    cd ~/Websites/ubuntu-mate.org
    nikola serve

Now point you web browser at localhost:8000 to test. CTRL+C to stop serving.

### Cleaning Nikola

If you need to clean the Nikola build of the site do this following.

    nikola clean

You'll need to build the site again now.

----------
## Deploying the site

The site is re-deployed on every commit via Travis CI. However, it a new 
Ubuntu MATE release is happening then the download page needs updating too.

### Updating the dynamic download page

The download page is dynamic client-side, but is statically generated using these resouces.

  * Download information is stored in `files/assets/downloads.json`
  * The main presentation is taken from `/pages/download.md` and will need Alpha, Beta labels etc updating.
  * The LESS and CSS configuration is stored in `/themes/United/less/download.less`
  * The Javascript logic is in `/files/assets/js/downloads.js`

When the torrents are published as part of the iso release run `generate-magnet-urls.sh`
for each release architecture, for instance:

    ./scripts/helpers/generate-magnet-urls.sh http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04.3/release/ubuntu-mate-16.04.3-desktop-i386.iso.torrent

Copy and paste the output to `files/assets/downloads.json` under the respective `magnet-uri` key.

