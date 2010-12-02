<summary>
	Whether you have already finished your app or are just getting started, the goal of this guide is to share various tips and tricks to help make the path to approval as smooth as possible.
</summary>

The tips and tricks below are from a mix of sources:
* Our own personal experience with submitting apps for review
* Apple's [approval guidelines](https://developer.apple.com/appstore/resources/approval/guidelines.html)
* The [Q&A forum](http://developer.appcelerator.com/questions/created)

# General
From Apple's own [approval guidelines](https://developer.apple.com/appstore/resources/approval/guidelines.html): "We have over 250,000 apps in the App Store. We don't need any more Fart apps. If your app doesn't do something useful or provide some form of lasting entertainment, it may not be accepted." Keep that in mind when thinking about what type of app you would like to make.

If the premise of your app or the content within could be considered offensive, your app may be rejected by Apple's reviewers.

iPhone apps must run unmodified on an iPad at iPhone 3GS resolution as well as 2x resolution.  This generally won't be a problem, but in the rare case you should encounter this please include the mobilesdk version and iOS SDK version you are using when asking for support.

# Ads
Consider ads in your free apps, but don't feel that you HAVE to include them.  Your users won't like ads any more than you do, so keep that in mind when deciding whether you want to include ads in your apps.

If you decide to use iAd, in your code be sure and handle the cases where no iAd is being served at that moment or your app will be rejected.

<warning>
    Apps that are primarily advertisements will likely be rejected.
</warning>

## DO NOT
Include ads in a paid app.  Technically you probably *could* use ads in a paid app, but it is considered bad form and your apps rating in the App Store will suffer for it.  Choose ads or paid, not both.

# App Name
Don't say that your app is a "beta", "demo", "trial", or "test" version or your app will be rejected.

If you have want to release a "trial" version of an app, consider calling it a "lite" version instead.

Let's say that you have a space shooter game you want to release called "Blaster" and you want to have a trial version and a full version.  You could call them "Blaster Lite" and "Blaster" respectively, or you could choose to name them "Blaster" and "Blaster Pro".  Adding "Pro" to an app name is a convention some developers follow to distinguish a paid from a free version of an app.

For iPad apps, another common naming convention is to use "HD" at the end of the app name to indicate that it is an iPad version.  So to carry on the previous example, an iPad version of "Blaster" would be called "Blaster HD".

# Audio and Video

## Audio
Audio streaming over a cellular network cannot transfer more than 5MB over a five minute period.

## Video
Live video streaming is supported, but streaming over 10 minutes must use HTTP Live Streaming and include a baseline 64 kbps audio-only HTTP Live stream.

# Data
It's okay to make use of data from other sites such as RSS feeds, response from API calls, etc. provided you are authorized to use this data.  Scraping websites or sources like iTunes Connect will likely lead to your app being rejected.

# Free Apps
There are plenty of very good free apps in the App Store, and if you want to release your app for free there is nothing wrong with that.  Maybe you want an app for your portfolio, maybe you have no interest in monetizing this one, or maybe you have some other reason.  It's totally your call, and there's nothing wrong with releasing a free app.

Some developers like to release a free version of an app and see how it does, and if it does well they will released a paid version with additional features.

<warning>
    If your app has the ability to make donations to recognized charitable organizations, your app must be free.
</warning>

## DO NOT
Submit an app to Apple that is feature limited with buttons, labels, etc. that simply tell the user to upgrade to the full version of the app, it will be rejected.

# Paid Apps
This is mentioned it the ads section but it is worth mentioning here too:  please do not include ads in a paid app.  It is bad form and will impact your apps rating in the App Store.  Choose ads or to make a paid app, not both.

## Pricing
A very common price point for many apps is 99 cents for a very good reason.  It's cheap enough to be an impulse buy but expensive enough to prevent people from downloading your free app, deleting it, and giving it a 1-star rating for no good reason.  If you do decide to price your app higher, know that it may impact your sales volume.

If you are not sure where to begin with pricing, try searching the App Store for other apps that are similar to yours and see what their price is.

## Sales
A good way to spike your number of downloads is to put your app on sale.  This temporary price reduction can give you a lot of downloads at once, and might lead to more reviews too.  Use [iTunes Connect](https://itunesconnect.apple.com/) to manage your apps pricing and sales.

# Push
Push notification is nice if used correctly, but using it to send advertising or direct marketing to users will likely result in the app either being rejected or removed from the App Store later when users complain about it.  Same thing if you charge users to receive push notifications from your app.

# Reviews and Star Ratings
Sooner or later your app will receive an unfavorable review.  Sometimes it will be for a very good reason, sometimes not.  Either way, just remember you're not the only one this has happened to and that even the best apps in the App Store sometimes receive 1-star ratings and/or poor reviews.  That's just part of life as a developer.

For some perspective, pick some of your favorite apps and browse the reviews and star ratings they have received.

# User Interface
The user interface of your app must comply with Apple's design guidelines:

* [Apple iPhone Human Interface Guidelines](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/Introduction/Introduction.html)
* [Apple iPad Human Interface Guidelines](https://developer.apple.com/library/ios/documentation/General/Conceptual/iPadHIG/Introduction/Introduction.html)

A good rule of thumb with interface design is if you follow the general conventions of other iPhone and iPad apps you have seen you'll probably be fine.  BUT, don't copy the look of an existing application or your app may be rejected.  This may sounds tricky but it's really not.  Follow the standards for how to use buttons, images, etc. and don't just clone iBooks, etc.

# Rejection
Sooner or later you are bound to write an app that gets rejected, it happens to everyone at some point.

If your app is rejected, Apple will email you explaining why your app was rejected.  Sometimes they'll even include a link to something on the Apple website that will tell you what you how to fix it.

Once you've fixed the problem they pointed out, resubmit your app and wait for them to take another look at it.  Know that it may be several days before your app is reviewed again so don't expect expedited service because you are resubmitting a previously rejected app.

## Appeal
If your app is rejected and you believe there is truly no reason for your app to have been rejected, there is an App Review Board you can appeal to.  For information about that process see the "App Review Board" section [here](http://developer.apple.com/appstore/guidelines.html)

Remember to be very specific about why the App Review Board should reconsider your app.