<summary>
This guide will explain the Titanium Mobile project structure.  After reading this guide, you should understand:

* The contents of your Titanium project
* How to use platform- and density-specific resources
* The configuration options available for your Titanium project

</summary>

# The Project Folder

<img src="http://img.skitch.com/20101129-puqysnxcu5widbr9um7x5mw1xk.png" style="float:right;margin:0 0 20px 20px;"></img>
When your project is created by Titanium Developer, a number of files are generated for you.  Here are the highlights
of what you can expect to find in a Titanium Mobile project:

* **LICENSE** - this file just describes the Appcelerator license. This is for your reference and not included in your application.
* **LICENSE.txt** - this is your end-user application license. This is not currently used for mobile project but will be used in the future.
* **README**- this file just describes the project and is not included in your application.
* **tiapp.xml** - this is the main application descriptor file and describes details about your application and is used by the packager and the runtime.
* **build** - this directory is where phone-specific project files and resources are kept. This folder is used by the packager and by developer for building, compiling and creating your native distributions. Generally, files in this folder should not be modified as this files are changed on demand by Titanium as your application changes. Use caution when touching any files or folders in these directories as it may render your application unusable.
* **Resources** - this folder is very important and contains all your application files such as your JavaScript, HTML, images, etc. This is the main folder you will use to include resources for your application. All files included in this folder are packaged and available to your application.
* **i18n** - this folder (optional) contains the localization resources for each language supported. This folder must be created as it's not created by default.

## app.js

In the Resources folder, `app.js` serves as the entry point for your application, and your application's
[root execution context](javascript_environment.html).  You could, in theory, implement your entire application in this file,
but more likely you will break up your application into multiple files and
[include them in the current context](javascript_environment.html#including_external_javascript_files) - in that case, app.js
serves as more of a 'bootstrap' file.  In any case, this is where the coding starts for your mobile application.

## Platform-specific Resources

There are a few specific folders under `Resources` that are special based on the final application package. Underneath the `Resources` 
folder are `iphone` and `android` folders - any resources placed in one of these folders will supersede the contents of the top-level 
Resources directory for a given platform.

For example, let's say you have a file named `foo.png` in the root Resources folder and a file named `foo.png` under `Resources/iphone`.
When Titanium compiles the application for iPhone, you will have one file named `foo.png` which will be the file under the 
`Resources/iphone` directory. Directories are preserved during merging. This capability gives you more fine grain control over 
resources per platform in cases where you need to override or provide specific resources for a given platform. When you reference a 
file from your application, you should not include the platform in the name. For example, you would reference `foo.png` instead of 
`iphone/foo.png` since the files are merged into the base directory when packaged.

![example](http://img.skitch.com/20101129-enru76mrb5ppsspdye18cq5963.png)

## Density-specific Resources

Not all devices have the same screen density or resolution.  An iPhone 3GS has a much lower density display than a iPhone 4.
Android devices come in all shapes, sizes, and screen resolutions.  However, you don't have to specify the right image assets
for every situation in code if you follow a few conventions when packaging resources with your application.

## Using density-specific resources on iOS

While on iPhone you can always size and position components using a 320x480 point system, you won't always be running on a 
high-density ("Retina") display.  You can transparently provide different visual assets per screen density by providing a
standard low-res image and a high-res image side by side in your project using file naming conventions.

<img src="http://img.skitch.com/20101129-cuktta51j4929hnksabe81u3jm.png" style="float:right;margin:0 0 20px 20px"></img>
Let's say you have an image that you use to skin a Button called `myButton.png`.  On the iPhone 3GS it looks fine, but it seems a bit
pixelated on iPhone 4.  To transparently use a different image on iPhone 4's retina display, simply create a high-res version of the
graphic and save it in your project, adding `@2x` to the filename.  So the high-res version becomes `myButton@2x.png`, but the code
remains:

	var myButton = Ti.UI.createButton({
		backgroundImage:'myButton.png'
	});

## Using density-specific resources on Android

The Android OS [divides the available screen densities into three groups](http://developer.android.com/guide/practices/screens_support.html),
high, medium, and low.  You can specify image resources to use per density by placing them in an `android/images/[density]` folder,
as in:

![images](http://img.skitch.com/20101129-r3w6xk6i4tip9im3emgkfe86qp.png)

Similarly to the iOS example, if we were creating a button in code (or referencing the image in a configuration file), we would just 
use `myButton.png`:

	var myButton = Ti.UI.createButton({
		backgroundImage:'myButton.png'
	});

# Special Resources

There are a number of special application resources that can be packaged along with your application - here are a few of the most
common:

## Splash screen

To specify a default splash screen that is displayed as your application is loading, you need to replace the file named `Default.png`. 
For iPhone, you should take care to design a splash screen that will allow the spinner indicator to display near the center of the 
screen while loading.

## Application icon

The application icon (what's shown on the phone screen) is controlled by the `<icon>` entry in the `tiapp.xml` file. The file is 
relative to the `Resources` directory. You can specify a different icon for Android and iPhone by naming the file the same but 
including a different version in the respective platform folder under `Resources`.

# Application Configuration

Most of the application configuration can be configured through Titanium Developer. However, there are a few application-specific 
settings you'll need to edit directly in `tiapp.xml`.

## iOS specific configuration

There are a few additional iPhone specific configurations that control features or capabilities only available on iPhone.

* persistent-wifi - this tag at the root level named `<persistent-wifi>` will tell iPhone that your application requires a persistent wifi connection and to not turn off the wifi after a brief period of inactivity. This defaults to false.
* prerendered-icon - this tag at the root level named `<prerendered-icon>` will tell iPhone not to apply an additional gloss over your application icon. This is useful if you have a pre-rendered gloss that has been applied. This defaults to false.

## Custom Info.plist

To use a custom `Info.plist`, copy the `Info.plist` from the `build/iphone` folder. If this folder does not exist, run your 
application in the simulator once and it should be created automatically. You'll want to copy the `Info.plist` file into the 
root directory of your project (at the same level as `tiapp.xml`).  Whatever values are placed in your custom `Info.plist` will 
be used as-is by the Titanium compiler.

## Custom Fonts

You can specify custom fonts. See the [instructions](ui_design.html#ios_custom_fonts) in the UI Design guide.

## Custom AndroidManifest.xml

To use a custom `AndroidManifest.xml`, copy the `AndroidManifest.xml` from the `build/android` folder. If this folder does not 
exist, run your application in the simulator once and it should be created automatically. You'll want to copy the 
`AndroidManifest.xml` file into the root directory of your project (at the same level as `tiapp.xml`).  Whatever values are 
placed in your custom `AndroidManifest.xml` will be used as-is by the Titanium compiler.


# Excluding files from source control

If you'd like to exclude certain files from source code control that change dynamically or that are generated locally, you 
should exclude the files and folders from the following two directories: `build/iphone` and `build/android`.

