## Theory

## Structure 

scrapy.cfg
myproject/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...

The directory where the scrapy.cfg file resides is known as the "project root directory.  That file contains the name of the python module that defines the project settings. "

eg:
    [settings]
    default = myproject.settings

## USING THE SCRAPY TOOL

Scrapy X.Y - no active project (prints currently active project)

Usage:
  scrapy <command> [options] [args]

Available commands:
  crawl         Run a spider
  fetch         Fetch a URL using the Scrapy downloader
[...]

## Creating a project
scrapy startproject myproject [project_dir] ( If project_dir wasn’t specified, project_dir will be the same as myproject.)

## Controlling projects

> For example, to create a new spider (scrapy genspider mydomain mydomain.com)