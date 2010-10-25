<summary>
This guide covers getting up and running with Appcelerator Titanium&trade;. After reading it, you should be familiar with:

* Installing Titanium, creating a new Titanium application, and running the application in the simulator
* The general structure of a Titanium application
* The basic principles of Titanium design (Model, Views, Events)
* How to quickly extend your application to add powerful capabilities
</summary>

# Downloading Titanium

To download Titanium, navigate to the [Titanium Download Page](http://www.appcelerator.com/download) and download Titanium. Depending on your operating system, this will download the Titanium installer. 

## Development environment requirements

You're ready to go – you've got your computer all set up, and ready to start working with Titanium. These are the development environments that are supported. You may find that slightly down-rev operating systems work fine as well, but these are the versions that we've tested.

<info>
The following are the supported environments:

* Mac OS X 10.6.4 (Snow Leopard)
* Windows 7, XP and Vista
* Ubuntu 9.10 (Karmic Koala)
</info>


### Mac OS X

Using Mac OS X, you can build mobile apps for iPhone, iPad and Android.
We've tested Mac OS X version 10.6.4, but earlier versions of 10.6 (Snow Leopard) should work as well. (Please let us know if you have any trouble.)

<note>If you're developing for iPhone or iPad, you must use Mac OS X for your development. Note that the current iOS (iPhone and iPad) SDK will not run on Mac OS X systems earlier than Snow Leopard.</note>


### Windows

We have tested these procedures with Windows 7. You may be able to use earlier versions of Windows, but we haven't fully tested them, and they aren't supported.

### Linux

We've tested Titanium mobile development with Ubuntu 9.10 (Karmic Koala).
You can try using other Linux distributions to develop with Titanium, but this Ubuntu distribution is the one that we test with and support. If you have trouble or success with another distribution, please let us know.


## Installing Titanium

Appcelerator's Developer Web site contains information you'll need to configure your development system, and then begin development using the sample programs. Using your Web browser, navigate to [http://developer.appcelerator.com/get_started](http://developer.appcelerator.com/get_started).

Here's the Web page you'll see:

![webpage](../assets/images/guides/getting_started/webpage.png)

At the bottom of the page, you'll see several helpful getting started videos that you can watch. You can watch them now or later; when you're ready, continue on with these instructions.

In this section, you'll install the components on the right that you'll use to develop mobile applications with Titanium, using Mac OS X.

There are several API revision levels, and different versions of the SDK's that we'll be navigating through in this section. You'll want to follow these installation steps in order.


### Mac OSX

This section is for development using a Macintosh. You can also develop using Windows or Linux, which are covered in related sections.

For downloaded files, the filenames given here are current as of when we created this guide. In general, it should be ok to use a later update of the listed files.

#### Install Titanium and mobile SDK's (Mac OS X)

#### Install iOS (iPhone and iPad) SDK

There are several steps along the way to installing the iOS SDK. To get started, go to:

[http://developer.apple.com/](http://developer.apple.com/)

Here are the steps you'll need to complete.

* Register as an Apple Developer, if you are not one already
* Agree to the Apple iPhone developer license
* Download and install XCode with the iOS SDK

Once you've agreed to the iOS developer license, there is an approval process before you go to the next step. This approval generally takes only a few hours for individual developers, but can sometimes take several days for a corporate account. Additionally, you'll need a paid membership in the iPhone Developer Program when it comes time for you to publish your app.
The above steps are done with Apple through Apple's Web site, and don't involve Appcelerator or Titanium.

It's important to allow the SDK to install in the default location on your Mac. This is inside the "Developer" directory at the top level of your startup drive. (This will be a sibling directory to "Users".) Once installed, it's important to avoid moving that directory – XCode will expect to see the various components in their default locations. The SDK will take up about 6 GB, so be sure you have enough space on your startup drive for it.


#### Install Android SDK

There is no login or approval process for Android development. However, there are numerous steps that you have to follow to download and install the Android SDK, and then register it for use in Titanium. In preparation, it's helpful to read about the Android SDK here:
[http://developer.android.com/sdk/installing.html](http://developer.android.com/sdk/installing.html).

When you're ready, go to the [Android SDK download page](http://developer.android.com/sdk/index.html).

In the following steps, we'll show you how to: 

* Download the Android SDK
* Install the Android SDK to the root drive
* Start the Android SDK and AVD Manager GUI 
* Download and install the proper Android APIs

For development on the Mac, download android-sdk_r06-mac_86.zip, which should end up being automatically unzipped into your Downloads folder. The Android SDK folder will be called "android-sdk-mac_86", and will take up about 1 GB.

Using the Finder, drag the "android-sdk-mac_86" from your Downloads directory to your root (startup) drive – this is often called "Macintosh HD". Rename the Android SDK folder to "android-sdk". Our examples expect this configuration, but you can actually put the Android SDK folder anywhere you like.

Although not essential, you may want to use the Terminal application on your Mac to work with the Android tools. Here are the commands in Terminal that you could use to start up the Android SDK and AVD Manager GUI.

<code class="bash">
    cd /android-sdk
    ./tools/android
</code>

