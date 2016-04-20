# ubuntu-mate.org

The website to discover and download the Ubuntu MATE operating system.

Powered by [Nikola](https://getnikola.com/) - a static page generator.

----------
## Translations
The website is only in English at the moment. **There is currently no way for translators yet**, although Nikola has support for multilingual sites.

----------
## Setting up the Nikola Environment

First, install Nikola into an isolated Python environment, called a `virtualenv`.
This is independent from the system's installation of Python.

    source ~/Snakepit/nikola/bin/activate

You know when the Nikola environment is activated because `(nikola)` will
be added to the bash prompt.

### Clone the website

    mkdir ~/Websites
    cd ~/Websites
    git clone git@bitbucket.org:ubuntu-mate/ubuntu-mate.org.git

### Build Nikola

The first build will take a while. Subsequent builds are much faster.

    cd ~/Websites/ubuntu-mate.org
    nikola build

### Serving the site

Nikola has a built in webserver, the serves the currently built site on port 8000.

    cd ~/Websites/ubuntu-mate.org
    nikola serve

Now point you web browser at localhost:8000 to test. CTRL+C to
stop serving.

### Cleaning Nikola

If you need to clean the Nikola build of the site do this following.

    nikola clean

You'll need to build the site again now.

----------
## Dynamic Download Page
The download page is dynamic, but is statically generated. Download information is stored in `downloads.json`. The page itself is updated by executing `scripts/update-download-page.py` and passing arguments (see `--help`).

