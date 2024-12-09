## installation

> pip install Scrapy

## We strongly recommend that you install Scrapy in a dedicated virtualenv, to avoid conflicting with your system packages.

Things that are good to know
> Scrapy is written in pure Python and depends on a few key Python packages (among others):
. lxml - efficient xml and html parser
. parsel -an HTML/XML data extraction library written on top of lxml
. w3lib - a multi purpose helper for dealing with URLs and web page encodings
. twisted - an asynchronous networking framework
. cryptography and pyOpenSSL - to deal with various network-level security needs

In case of any trouble related to these dependencies, please refer to their respective installation instructions:

## Venv

Python packages can be installed either globally (a.k.a system wide), or in user-space. We do not recommend installing Scrapy system wide.

Instead, we recommend that you install Scrapy within a so-called “virtual environment” (venv). Virtual environments allow you to not conflict with already-installed Python system packages 