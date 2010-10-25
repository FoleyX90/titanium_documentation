<summary>
This guide covers getting up and running with Appcelerator Titanium&trade;. After reading it, you should be familiar with:

* Installing Titanium, creating a new Titanium application, and running the application in the simulator
* The general structure of a Titanium application
* The basic principles of Titanium design (Model, Views, Events)
* How to quickly extend your application to add powerful capabilities
</summary>

# PDF Instructions

You can download a full PDF guide customized to each operating system:

* [Mac OSX](http://assets.appcelerator.com.s3.amazonaws.com/docs/GettingStartedTitanium_Mac.pdf)
* [Windows](http://assets.appcelerator.com.s3.amazonaws.com/docs/GettingStartedTitanium_Windows.pdf)
* [Linux](http://assets.appcelerator.com.s3.amazonaws.com/docs/GettingStartedTitanium_Linux.pdf)



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


# Installing Titanium

Appcelerator's Developer Web site contains information you'll need to configure your development system, and then begin development using the sample programs. Using your Web browser, navigate to [http://developer.appcelerator.com/get_started](http://developer.appcelerator.com/get_started).

Here's the Web page you'll see:

![webpage](../assets/images/guides/getting_started/webpage.png)

At the bottom of the page, you'll see several helpful getting started videos that you can watch. You can watch them now or later; when you're ready, continue on with these instructions.

In this section, you'll install the components on the right that you'll use to develop mobile applications with Titanium, using Mac OS X.

There are several API revision levels, and different versions of the SDK's that we'll be navigating through in this section. You'll want to follow these installation steps in order.


# Getting Started with the Titanium Blackberry Beta Preview

<warning>
    This guide below is only for customers that have signed up for the Titanium BlackBerry Beta Preview. 
</warning>

## Setting Up Your Development Environment

Currently, Blackberry applications can only be developed and tested on Windows machines, due to the fact that Research in Motion's Blackberry simulators are Windows EXEs.  Technically speaking, you can develop and build your Blackberry applications on any platform supported by Titanium (Windows, Mac OS X or Linux), but you will not be able to test them in the Blackberry simulator on any platform other than Windows.  For that reason, these instructions assume you will be setting up a Windows system for Blackberry development using Titanium.

Most of the requirements that we list here are based on Research In Motion's own list of requirements for using their [Blackberry Java Plug-In for Eclipse](http://na.blackberry.com/eng/developers/javaappdev/javaplugin.jsp), which is what Titanium uses to access the Blackberry Java APIs.

###Microsoft Windows

You'll need Microsoft Windows XP or higher.  If you have a 64-bit version of Windows, be sure to nevertheless download 32-bit versions of Java and Eclipse as per the instructions below.

###Java Development Kit (JDK) 6 (update 10 or higher)

You need to have a Java Development Kit with version 6 (a.k.a. 1.6), specifically JDK 6 update 10 or higher -- *not* anything lower than JDK 6 update 10, and *not* JDK 7 or higher (it must be JDK *6*.)  At the time of this writing, JDK 6 update 20 is the most current version of JDK 6 and can be downloaded using the following link:

[JDK 6](http://java.sun.com/javase/downloads/widget/jdk6.jsp)

(Note: Even if you are using a 64-bit version of Windows, please download a 32-bit version of Java.)

After installing JDK 6, create a JAVA_HOME environment variable to point to the folder into which you installed the JDK.  For example, if you installed JDK 1.6 update 20 into `c:\\java\\jdk1.6.0_20`, you would set an environment variable such as this:

![Add the JAVA_HOME environment variable](http://img.skitch.com/20100630-8uq949akr87qxg43w5s459nu1e.jpg)
 

Then add the JDK's "bin" folder and `jre\\bin` folders to your system path by appending `%JAVA_HOME%\\bin` and `%JAVA_HOME%\\jre\\bin` to your PATH environment variable:

![Add Java bin folders to PATH](http://img.skitch.com/20100630-fa94hk6fcyh65m2nhpsr21jy14.jpg)
 

###Eclipse Classic 3.5

Research in Motion exposes its Blackberry APIs via Java interfaces installed as a plugin to the Eclipse IDE.  Their documents indicate that Eclipse Classic 3.5 is required.  You can download Eclipse Classic 3.5 here:

[Eclipse 3.5 Classic](http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops/R-3.5.2-201002111343/eclipse-SDK-3.5.2-win32.zip)

Even if you are using using a 64-bit version of Windows, please download a 32-bit version of Eclipse, as per Research In Motion's instructions.  Also, please notice that Eclipse 3.5 is not the latest version of Eclipse; however, the installer for the Blackberry Java Plug-In will not work with any Eclipse version other than 3.5, so you must install 3.5 instead of the latest Eclipse.

###Blackberry Java Plug-In for Eclipse 1.1

After Eclipse is installed, download and install the Blackberry Java Plug-In for Eclipse 1.1 using this link:

[Blackberry Java Plug-In for Eclipse](http://na.blackberry.com/eng/developers/javaappdev/javaplugin.jsp)

The file that you download is a setup EXE file.  Run that file and select the proper location where your Eclipse installation resides.  The setup program will put the Blackberry plugin under the "plugins" directory in that Eclipse folder.

Titanium Developer Setup
-------------------------

###Install Titanium Developer

If you don't already have it, you should install the standard version of Titanium Developer, which is available here:

[Titanium Developer](http://www.appcelerator.com/products/download/)

After it is installed, you should modify its Resources folder using the `tidev-bb-resources.zip` file; a link to that file was provided to you inside the e-mail you received as part of the beta preview registration.  Put that ZIP file into the Titanium Developer program folder, meaning the folder which contains the "Titanium Developer.exe" file.  In both Windows 7 and Windows XP, this will typically be:

`C:\\Program Files\\Titanium Developer`

If you are running a 64-bit version of Windows 7, check for:

`C:\\Program Files (x86)\\Titanium Developer`

Unzip the `tidev-bb-resources.zip` folder in that directory.  The ZIP file contains the `Resources/...` folder structure, which will overwrite the existing Resources folder.  Make sure to copy over the items in existing Resources folder (i.e. do not delete and replace them), or Titanium Developer may attempt to re-install an older version of its self.

###Locate your Eclipse Folder

After you've unzipped the special Blackberry-specific Resources folder above, you can start Titanium Developer (if it's your first time, you'll need to login to or register for the Appcelerator network.)  

Next, tell Titanium Developer where Eclipse is installed so that it knows where to find the Blackberry Eclipse Plug-in.  Go to the User Profile Perspective and fill in the "Blackberry SDK" field with the location of your Eclipse installation.

![Locate your Eclipse folder](http://img.skitch.com/20100630-xgjecrfjjuh71nt4ifx155urfq.jpg)
 

###Download Blackberry Desktop

Blackberry Desktop is required for you to send your application to device. Download and install it from here:

[http://na.blackberry.com/eng/services/desktop/desktop_pc.jsp](http://na.blackberry.com/eng/services/desktop/desktop_pc.jsp)

###Mobile SDK Setup

In the e-mail you received as part of beta preview registration there is a link to download the Blackberry-specific version of the Titanium Mobile SDK.  Download that file -- mobilesdk-bb-1.3.0-win32.zip -- and then unzip it into the Titanium folder that contains the "mobilesdk" sub-folder.  The location of this folder will depend on which version of the Windows operating system you are running.  Under Windows 7, it will typically be:

`C:\\ProgramData\\Titanium`

Under Windows XP, it will typically be:

`C:\\Documents and Settings\\All Users\\Application Data\\Titanium`

(Note: those folders may be hidden by default.  Change your folder view settings [Tools - Folder Options] in Explorer to see them if necessary.) 

The ZIP contains the `mobilesdk...` folder structure, so be sure to unzip it inside the Titanium folder so that its files get laid out properly into the sub-folders.

After you've finished unzipping it, you'll notice the folder structure `mobilesdk\\win32\\bb-1.3.0`.  That "bb-1.3.0" is the Blackberry-specific version of the Titanium Mobile SDK; later, when using Titanium Developer to create mobile projects for Blackberry, you'll need to remember to select the "bb-1.3.0" SDK for those projects:

![Specify the bb-1.3.0 Titanium SDK](http://img.skitch.com/20100630-tnseufi6f3s6it6jn46wd9m1he.jpg)
 

If Titanium Developer was running while you performed the previous steps, you should close it and restart it so that it becomes aware of the new Blackberry-specific mobile SDK.

At this point you're ready to either create your own projects or import others.  We'll start by importing the Blackberry "Kitchen Sink" project in the next section.

Importing the Blackberry "Kitchen Sink"
---------------------------------

There is a Blackberry-specific version of the Titanium Kitchen Sink project, which is a reference application designed to show which features are available in the Titanium mobile sdk.  In the e-mail you received as part of the beta preview registration process you will find a link to download the Blackberry Kitchen Sink.  Go ahead and download that file -- bb-kitchensink.app -- and unzip it in a folder where you plan to keep your Titanium projects.  After unzipping it, you will see a folder named `BBKitchenSink`.

Open Titanium Developer, click the "Import Project" button, and locate and import the `BBKitchenSink` folder you just unzipped.  After importing, make sure the BBKitchenSink project's "Titanium SDK" property is set to "bb-1.3.0."  You will then be able to run the Blackberry Kitchen Sink in the Blackberry simulator per the "Running the Simulator" instructions later in this document.

Creating your own projects
----------------------------

In order to create a Titanium mobile project to run on the Blackberry platform, go through the same steps you would for any other platform (iPhone/iPad, Android): 

* Click "New Project";
* Select project type "Mobile"
* Fill-in project details
* Be sure to choose "bb-1.3.0" as the "Titanium SDK":

![Specify the bb-1.3.0 Titanium SDK](http://img.skitch.com/20100630-tnseufi6f3s6it6jn46wd9m1he.jpg)

* Then click "Create Project".  

You can then go and edit the app.js file that gets created in your project's Resources folder, just as you would with Titanium mobile projects for Android or iPhone/iPad.

Running the Simulator
-----------------------

* From your project, click on the "Test & Package" tab in Developer. The "Run Emulator" and "Blackberry" sub tabs should be pre-selected for you, but if they aren't make sure to have them selected

![Correct simulator tabs](http://img.skitch.com/20100630-jeduyjeie4x1m2qp7w6uc7um3a.jpg)
 
* This view contains 5 actions:

    * Simulator: This dropdown selects the simulator which will run your application. We've selected the 9550 simulator by default, as it has a touch interface, and is the easiest to drive with a mouse and keyboard
    * Filter: This filters the amount of log output in the developer window based on the level selected. Info is default, Debug shows more than Info, and Trace shows more than Debug. With Blackberry Debug is normally as low as you need to go, Trace will have a lot of simulator messages that won't be useful in normal circumstances.
    * Launch button: click this button to launch the selected Blackberry Simulator.
    * Stop: Force quit the Blackberry simulator (useful if it locks up)
    * Clear SDCard: Clear the sdcard on the next simulator launch. If you receive a "ControlledAccessException" while launching your app, you should stop the simulator, and click this on the next launch. 

###Starting the App

Once Developer has launched your application, you'll need to manually start it by locating it in the "Downloads" section of the main Blackberry menu. You can do this by hitting the Blackberry key on the simulator, selecting the "Downloads" folder, and selecting your application. If your application is already running when you hit "Launch" a second time, the simulator will close the app and automatically relaunch it (there's no need to launch it again manually unless you close the application)

![Simulator Launch 1](http://img.skitch.com/20100630-1e5g4ciq54u47etxn88kd5kxij.jpg) ![Simulator Launch 2](http://img.skitch.com/20100630-dec3yy4k6de9td12pgmttdu6yi.jpg)
  
![Simulator Launch 3](http://img.skitch.com/20100630-j96xyjb6epgpxs4ermcegkumpq.jpg)

Installing To Device
---------------------

RIM requires that all applications sent to a device must be signed with their 3 keys and the user's private key. RIM charges $20 for the keys, and provides them via email after you fill out this form:

[https://www.blackberry.com/SignedKeys/](https://www.blackberry.com/SignedKeys/)

Make sure to remember your PIN, as you'll need it the first time you generate the private key when you sign the application through Developer.

Once you have received the 3 keys from RIM, follow these steps to install on device:

1. Verify that you've downloaded or copied all 3 keys into the same folder. The filenames should look like ('xxx' is a number generated by RIM):
     * client-RBB-xxx.csi
     * client-RCR-xxx-.csi
     * client-RRT-xxx.csi
2. Click the "Run on Device" tab, and make sure the "Blackberry" sub-tab is selected
3. Click the folder next to the entry for "Blackberry Key Directory" to select the folder that has the 3 signing keys.
4. If this is your first time to install on device, SignatureTool will ask you to create a private key for signing. You can leave the "passphrase" entry empty for now. Skip ahead to Step #7
5. If you've already created your private key, you have two options:
    * Enter your passphrase in the "Passphrase" entry before you click "Install Now". Developer will send the passphrase to SignatureTool
    * Leave the "Passphrase" entry blank, and SignatureTool will prompt for your passphrase before signing the application
6. Hit "Install Now" with your device connected via USB to your computer.
7. If you haven't created a private key yet, SignatureTool will now ask you if you'd like to create a new private key. Click "Yes"

![Private Key Step 1](http://img.skitch.com/20100630-ptn6jnwbt6c3k9bf1swh62j959.jpg)
 
* The next screen will ask you to create a password (passphrase) for this private key. Make sure you save this somewhere safe.

![Private Key Step 2](http://img.skitch.com/20100630-n564hye132g884rwp8g8tu9a6x.jpg)
 
* The final screen will ask you to generate random mouse / keyboard movement for creating a randomized key

![Private Key Step 3](http://img.skitch.com/20100630-gcy7kj4s2usyrsy74t88tk2urx.jpg)
 
* After this, SignatureTool should proceed with requesting the signature of your application's COD file(s), and Developer should install the application onto your device

API Documentation
----------------
Please see the document "[Blackberry API List](http://developer.appcelerator.com/doc/blackberry/api)" for a list of the portions of the Titanium Mobile SDK's API which are currently available for Blackberry.

Known Issues
------------
* TableView rows currently only have leftImage, text/title, and rightImage. We are working on a way to embed images and text arbitrarily for the next release
* The Blackberry Simulator will from time to time throw a ControlledAccessException (this exception will be seen as an all-white screen). If you see this screen:
    * Stop the emulator from Developer
    * Check the "Clear SDCard" checkbox
    * Re-launch the simulator
    * Make sure to un-check "Clear SDCard" on the next launch
* In some cases of prolonged use, we've seen Developer crash and refuse to start. If this happens to you, follow these steps:
    * Uninstall Developer from the Control Panel
    * Delete the following folders:
        * `C:\\ProgramData\\Titanium`
        * `%AppData%\\Titanium`
    * Follow the installation instructions in this document to reinstall Titanium Developer.