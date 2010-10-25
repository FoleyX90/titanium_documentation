# Appcelerator Documentation Guides Project

Welcome to the Appcelerator Documentation Guides project. 

The goal of this project is to provide open and transparent product documentation for the Appcelerator Titanium open source project.  

## Goals of this project

The following are the main goals for this project:

* Open source and easy to fork - these guides should be open and transparent and available for anyone to obtain and modify
* Easy to author - these guides should be _easy_ to author to encourage _participation_ and _accuracy_
* Easy to build and run locally - these guides should be _easy_ to build and read _locally_ without the need for complex web server setup
* Easy to localize - these guides should be _easy_ to localize into other languages given that size of the Appcelerator community globally

## How to build

To build the guides, you'll need the following third-party components:

* Python 2.5+ - you'll need to obtain Python. If you're on OSX or Linux, Python is already installed.
* You'll need the following Python modules: json, mako and markdown

You can install the Python modules:

    > easy_install Mako
    > easy_install markdown

Once you have the required dependencies, simply run the `gen.py` script.  This will generate the documentation into the `output` folder.  To get the root webpage, open `output/en/index.html` in your favorite web browser.

## How to contribute

Contribution should be rather easy. After generation the documentation page, navigate to the `Contribute` page in the navigation bar.

## Why not a wiki?

We often get asked "why not just make all the documentation wiki-style content?"  That's a reasonable request and, in the past, we did.  What we found was that the content was rarely updated and when it was, quality often suffered, or worse, it was incomplete.  We have decided to make the guides easy to obtain, easy to author, easy to peer review and publish as opposed to providing a wiki-interface to them.  Much like open source software, we find that once users take the time to checkout, build and contribute along with the peer review from checkins on GitHub, it ends up producing content which has much higher quality and contributions which have much greater completeness.  We think this is a good balance at this point in the project's lifecycle.

## Copyright & Credits

(c) 2010 by Appcelerator, Inc. All Rights Reserved. The guides and associated scripts are licensed under the Apache Public License (version 2).  

The documentation template was adapted from the Rail Guides which is licensed under the 
[Creative Commons Attribution-Share Alike](http://creativecommons.org/licenses/by-sa/3.0/). We relicense all those files under the same license.

Appcelerator is a registered trademark of Appcelerator, Inc.  Appcelerator Titanium is a trademark of Appcelerator, Inc.

