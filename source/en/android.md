<summary>
    The following guide provides Android specific platform information.
</summary>


# Packaging for the Android Market

## Android Documentation

Google publishes several documents related to publishing and you should become familiar with them.

- [Signing your Application](http://developer.android.com/guide/publishing/app-signing.html)
- [Versioning your Application](http://developer.android.com/guide/publishing/versioning.html)
- [Preparing to Publish](http://developer.android.com/guide/publishing/preparing.html)
- [Publishing your Applications](http://developer.android.com/guide/publishing/publishing.html)

##Important Considerations

Android requires a signed .apk (installation file) before it will install on a device. In development, we take care of creating a debug certificate and signing the .apk to reduce the number of tasks required in development. When packaging for production, you will have to become more familiar with the signing process and the requirements that the Android market and Android OS have for installing your application.

While you have several strategies for using your certificates, **you must take care not to lose a certificate**. It is recommended that you store a copy in several places including one offsite location. You should also restrict access to your generated certificates, as anyone with your key can request to run in the same process as all other applications you signed with that certificate.

Unless your application needs to share implementation (i.e run in the same process) with your other installed applications, it is recommended to use a different certificate for each application. This will allow Android to prevent access to an application's process increasing security.

**Read [Securing Your Private Key](http://developer.android.com/guide/publishing/app-signing.html#secure-key)**

## Preparation

Creating certificates will be easier if the JDK `bin` folder is in your path. Consult one of the platform [HowTo](http://www.codestrong.com/timobile/howto/) guides if you're unsure on how to set up your PATH.

If your Android project was created with mobile SDK Version 0.5.0 or earlier, you will need to add a minSDKVersion to your AndroidManifest.xml. See ticket #[66](http://appcelerator.lighthouseapp.com/projects/32238-titanium-mobile/tickets/66).

![Screenshot of SDK Version](http://img.skitch.com/20090725-cq6eys86i7hh1s5wqcypuiu7b4.png)

The rest of the document is going to guide you through getting the data together such that you can successfully package from Titanium Developer.

![Screenshot of Titanium Developer Android Packaging Tab](http://img.skitch.com/20090725-r55skrhbfufp7ft3ek8fmr8tnc.png)

Obtaining a Suitable Private Key 
--------------------------------

*(Summarized from the Android Documentation)*

A suitable private key is one that:

- You control.
- Represents you or your entity.
- Has a validity period that exceeds 25 years.
- If targeting the market, validity period after 22 October 2033.
- Is not a debug key.

It is recommended that you store your production keystore files separately from your projects and tools. For this example, we will assume that you are storing them in a folder of your user directory.

On unix based systems (Linux and OS X)
~~~
~/keystores
~~~

On Windows based systems in My Documents. *(Forward slashed in path below should be backslashes, there is a bug in the documentation system that prevents using backslash)*
~~~
%USERPROFILE%/My Documents/keystores
~~~

Creating the Private Key
------------------------

- Open a command prompt and change into your **keystores** folder.
- Enter the following command. Replace **MYKEYSTORE** with the name of your keystore (e.g. android.keystore) more than one key may be stored in a single keystore. Replace **MYKEYALIAS** with a name that describes the key (e.g. myfirstapp) you will need this alias for packaging. You will be prompted for the keystore password and a key password. The key password **MUST** be the same as the keystore password so just hit **<ENTER>** when prompted.

~~~
    keytool -genkey -v -keystore MYKEYSTORE -alias MYKEYALIAS -keyalg RSA -validity 11000
~~~

### Example Key Generation Session

![Example Session](http://img.skitch.com/20090725-d6u9sbychrfb95qpaw44bic8we.png)

Use the following command to verify the generated key. You will want to check that the date is greater than 25 years or after 22 October 2033 if you are publishing in the market.

~~~
    keytool -list -v -keystore MYKEYSTORE
~~~

### Key List Output

![Example key list output](http://img.skitch.com/20090725-bydajc9iuu328q2q31sb4yw6ir.png)

Signing the Application
-----------------------

Titanium Developer will handle signing your application. Go to your application, select the packaging tab, and enter your information. For this example I'm going to generate the signed application into `/tmp`.

### Packaging Form With Data

![Packaging form with data](http://img.skitch.com/20090725-1kdumg3t19c1chbsx4u5ppa2xe.png)

Click Package and Titanium Developer will display the following message.

![packaging message](http://img.skitch.com/20090725-fc1cdartkdxgp12ktnh3imucpm.png)

Verifying The Signed Application
--------------------------------

Before you go to the effort to upload your application, you might want to verify that it has been signed correctly using the following command.

~~~
    jarsigner -verify -verbose MYAPPLICATION.apk
~~~

### Example Verbose Verification Output

![Example verbose verification output](http://img.skitch.com/20090725-mej7bjq7emw7871hi8285hw632.png)

ZIPALIGN Your Application
-----------------------------

Before an application can be submitted to the Android Market it may need to be zipaligned. The Android documentation [zipalign guide](http://developer.android.com/guide/developing/tools/zipalign.html) describes the process.  Starting in Titanium 1.4, this is automatically done for you.

Distributing Your Application
-----------------------------

The Android documentation [Publishing Your Application](http://developer.android.com/guide/publishing/publishing.html) walks you through publication. You can choose to distribute via the Market or from your own website.
