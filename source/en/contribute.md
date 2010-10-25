<summary>
    The Appcelerator Titanium SDK is open source and licensed under the [Apache Public License (version 2)](http://www.apache.org/licenses/LICENSE-2.0.html).  We host the source code to Titanium on [GitHub](http://www.github.com/appcelerator) and we welcome your generous contributions to the project.
</summary>


# How to find the Appcelerator Code

Titanium is hosted and actively developed on [GitHub](http://www.github.com/appcelerator). 

Appcelerator hosts a number of open source projects on GitHub.  In order to build Titanium, you will need a few tools:

* Git
* Python 2.6+ 
* SCons
* Platform SDKs such as Android, iOS (if building on OSX), etc.

# Before you can contribute

Since Appcelerator itself is both an open source project and also a Company that is in charge of its long-term development, we require that you sign a standard Open Source Contributors License Agreement (CLA). As with most open source projects, legal issues regarding intellectual property rights require us to protect ourselves, our contributors and our users from any future ownership claims to the software, documentation or other materials contribute to Appcelerator.

You must first electronically sign the [CLA](http://bit.ly/app_cla) before you can contribute code, documentation, etc. to the Appcelerator open source project.


# How to contribute to Documentation

This website is available in GitHub and can be forked if you'd like to help contribute content.

First, you'll need to fork the code.

<code>
    git clone git@github.com:appcelerator/titanium_documentation.git
    cd titanium_documentation
</code>

Next, you'll want to build the site and make sure that works fine.  

<code>
    ./gen.py
</code>

This will generate the full website into the `output` directory.  You'll want to open up the following webpage in a browser `output/en/index.html`.

## The documentation structure

The source files for each guide is under the language folder (such as `en`) and the documentation is written in [Markdown](http://daringfireball.net/projects/markdown/) format.

The documentation structure is specified in the `doc.json` file in the root directory. The file is a JSON formatted file which contains the information that the generator script uses to build the entire website.

Each documentation page uses a template under the `templates` folder. The template is in a format that the [[Mako]](http://www.makotemplates.org/docs/syntax.html) templating system for Python. Generally, you will use the existing `guide.html` template already provided.

## Localization of the guides

To localize for a specific language, you must add the language to the `doc.json` file.

For each `language` entry in the `languages` array, the generator will attempt to build a localized version of the documentation:

<code>
"languages":
[
	{
		"directory":"en",
		"title":"English",
		"code":"en"
	}
]
</code>

To add a new language, add a new entry under the `languages` key. The value for the `title` key should be in the specific language.  For example, for Japanese the key should be: 日本. The code should be the ISO language code.


