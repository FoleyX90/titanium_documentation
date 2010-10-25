<summary>
    The following guide provides iOS specific platform information.
</summary>



# Distributing your App to Beta testers

With the 1.3.0 release, it should be possible to use Apple's tooling to do an ad hoc distribution of your application with the generated Xcode project (look in `build/iphone`). If you'd like to avoid Apple's tooling and use Titanium Developer, then read on for more information.

In lieu of doing an ad hoc distribution for iPhone, you can distribute the binary deployed to your local device for testing to your beta testers. The process for doing this is as follows:

## Provisioning Profile

Create a development provisioning profile which contains the device IDs of all the individuals you would like to be able to test your application. Install your application to a device for testing to create the binary.

## Zip up the binary

Zip up the binary from your application's `build/iphone/build` directory:

![dir](http://img.skitch.com/20100526-8idhej948myb6jnn3mc88krahj.png)


## E-Mail the .zip file and the `.mobileprovision` file to beta testers

Beta testers should now be able to drag the `.mobileprovision` file (the provisioning profile you created) to the iTunes icon to install it. Next, they should be able to similarly drag and drop the `.app` file into iTunes to install the app. Once they synch their phone through iTunes, your beta app should be installed on their device.

