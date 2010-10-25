<summary>
    This guide will explain the Appcelerator project structure and set of files and directories.
</summary>
 
# The Project Folder

There are a number of files and important folders in your mobile project. Here's the main files:

* **LICENSE** - this file just describes the Appcelerator license. This is for your reference and not included in your application.
* **LICENSE.txt** - this is your end-user application license. This is not currently used for mobile project but will be used in the future.
* **README**- this file just describes the project and is not included in your application.
* **tiapp.xml** - this is the main application descriptor file and describes details about your application and is used by the packager and the runtime.
* **build** - this directory is where phone-specific project files and resources are kept. This folder is used by the packager and by developer for building, compiling and creating your native distributions. Generally, files in this folder should not be modified as this files are changed on demand by Titanium as your application changes. Use caution when touching any files or folders in these directories as it may render your application unusable.
* **Resources** - this folder is very important and contains all your application files such as your JavaScript, HTML, images, etc. This is the main folder you will use to include resources for your application. All files included in this folder are packaged and available to your application.
* **i18n** - this folder (optional) contains the localization resources for each language supported. This folder must be created as it's not created by default.

## Special resources per platform

There are a few specific folders under `Resources` that are special based on the final application package. Underneath the `Resources` folder is an `iphone` and `android` folder (dependent on which platforms you're using). All files placed under these folders will only be available on the platform by name. The files in these folders will take precedence (and will be merged) over files in the root `Resources` directory.

For example:

If you have a file named `foo.png` in the root folder and a file named `foo.png` under `Resources/iphone` - when Titanium compiles the application for iphone, you will have one file named `foo.png` which will be the file under the `Resources/iphone` directory. Directories are preserved during merging. This capability gives you more fine grain control over resources per platform in cases where you need to override or provide specific resources for a given platform. When you reference a file from your application, you should not include the platform in the name. For example, you would reference `foo.png` instead of `iphone/foo.png` since the files are merged into the base directory when packaged.

# Default splash screen

To specify a default splash screen that is displayed as your application is loading, you need to replace the file named `Default.png`. For iPhone, you should take care to design a splash screen that will allow the spinner indicator to display near the center of the screen while loading.

# Application icon

The application icon (what's shown on the phone screen) is controlled by the `<icon>` entry in the `tiapp.xml` file. The file is relative to the `Resources` directory. You can specify a different icon for Android and iPhone by naming the file the same but including a different version in the respective platform folder under `Resources`.

# Application Configuration

Most of the application configuration can be configured through Titanium Developer. However, there are a few application specific settings you'll need to edit directly in `tiapp.xml`.

## Custom iOS Configurations

The following is specific to iOS configurations.

### iOS specific configuration

There are a few additional iPhone specific configurations that control features or capabilities only available on iPhone.

* persistent-wifi - this tag at the root level named `<persistent-wifi>` will tell iPhone that your application requires a persistent wifi connection and to not turn off the wifi after a brief period of inactivity. This defaults to false.
* prerendered-icon - this tag at the root level named `<prerendered-icon>` will tell iPhone not to apply an additional gloss over your application icon. This is useful if you have a pre-rendered gloss that has been applied. This defaults to false.

#### Retina Display based splash screen

To specify a Splash screen that supports the Retina display, specify a file named `Default@2x.png` in the `Resources/iphone` folder along with `Default.png`. For more information on Retina display configuration, please read the [UI guide section](ui_design.html#ios_retina_display).

#### Custom Info.plist

To use a custom `Info.plist`, copy the `Info.plist` from the `build/iphone` folder. If this folder does not exist, run your application in the simulator once and it should be created automatically. You'll want to copy the `Info.plist` file into the root directory of your project (at the same level as `tiapp.xml`).  Whatever values are placed in your custom `Info.plist` will be used as-is by the Titanium compiler.

#### Custom Fonts

You can specify custom fonts. See the [instructions](ui_design.html#ios_custom_fonts) in the UI Design guide.

## Custom Android Configurations

The following is specific to Android configurations.

#### Custom AndroidManifest.xml

To use a custom `AndroidManifest.xml`, copy the `AndroidManifest.xml` from the `build/android` folder. If this folder does not exist, run your application in the simulator once and it should be created automatically. You'll want to copy the `AndroidManifest.xml` file into the root directory of your project (at the same level as `tiapp.xml`).  Whatever values are placed in your custom `AndroidManifest.xml` will be used as-is by the Titanium compiler.


# Excluding files from source control

If you'd like to exclude certain files from source code control that change dynamically or that are generated locally, you should exclude the files and folders from the following two directories: `build/iphone` and `build/android`.

