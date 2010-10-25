<summary>
    This guide will help you obtain Continuous Builds built automatically from the Titanium open source repository.
</summary>

<warning>
    Builds from our continuous builds site can be very unstable and unpredictable. We provide NO SUPPORT (even for Customers) that encounter problems from a build from source.
</warning>

That being said, if you are looking to stay on the bleeding edge, or get a bug fix before the official release, this is probably your best bet.

# Obtaining the Build

You can download the latest continuous builds here:
[http://build.appcelerator.net](http://build.appcelerator.net)

# Installing the Build

* Extract the mobilesdk zip into your Titanium installation folder.
    - OSX : `/Library/Application Support/Titanium` or `~/Library/Application Support/Titanium`
    - Linux: `~/.titanium`
    - Windows: `C:\\ProgramData\\Titanium` (Vista, 7), or `C:\\Documents and Settings\\All Users\\Application Data\\Titanium` (XP)
* Navigate down to the versioned folder for the build you extracted. (e.g. `1.3.3`) rename it to `continuous-1.3.3` (for example) so that you will get the production release notice for the official version.  If you keep it named `1.3.3` and then the actual 1.3.3 version is released, Titanium Developer will not notify you to download the actual version.
* After extracting (re)start Titanium Developer, and go to your Project's `Edit` tab, and make sure to change the SDK to match the version of that you downloaded.

