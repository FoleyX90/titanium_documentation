<summary>
	This document looks to provide tips and best practices when creating mobile applications.
</summary>

Whether you are designing an app for the iPhone/iPod touch, iPad, or Android, many of the same principles apply.

Two important things to keep in mind when developing for a mobile device is:

* The screen is smaller
* The input method is touch-based

At first glance these seem rather obvious and hardly worth mentioning, but they can't be stressed enough.  It's very easy to make an app that has displays too much data at once in a font tiny font, or that crams too many buttons or links into a tight space.  The difficult part is making a simple, easy to use interface.  Hopefully the information presented below will help.

# Getting Started
Some developers start with a sketch on paper, or maybe a mockup in Photoshop or Illustrator, of what they're after.  Others dive head first into the code and let interface evolve as they go.  The right approach is whatever works best for you and lets you create the app you see in your head.

If you're just getting started and aren't really sure where to start, start with getting the basics of your UI mocked up before getting into the code so you have a better idea of what to start building in Titanium.

If you plan on using Photoshop to mockup your interface, consider using one of these to help with the relative size of the different parts of your app:

* [iPhone GUI PSD](http://www.teehanlax.com/blog/2010/06/14/iphone-gui-psd-v4/)
* [iPad GUI PSD](http://www.teehanlax.com/blog/2010/02/01/ipad-gui-psd/)
* [Android GUI PSD](http://www.matcheck.cz/androidguipsd/) (the UI elements are from Android 1.5 but it should still be close enough to help with laying things out)

Another choice would be to create black and white wireframes in Illustrator.

# Busy Indicators
At different times while using your app, a user may do something that will trigger an action that will take several seconds to complete (a complex database query, a remote XHR call, etc.).  Never give your user the feeling that the app has hung or is broken; if something will take a second or more, show the user a busy indicator so they know something is happening.

# Native Look and Feel
The look and feel of the different platforms are similar, but they each have their own way of doing things.  For example, iOS and Android each have a way of showing a busy indicator and they each convey the same message, but the way the native control looks is quite different from one platform to another.  The same is true with tabs, menus, and all sorts of other UI elements.

Users of the different platforms expect a busy indicator to look a certain way on that device, and a menu to open a certain way, and so on.  Don't take an app designed for one platform and force it to look and feel the same way on another platform, to those users the app will feel unnatural and awkward.  

If you use native controls on one platform, give users on the other platform(s) the same courtesy and use native controls there too.

It's okay to take chance with your design, but do so in a way that complements the look and feel of the platform you are developing for.

# Orientation
If you plan on supporting both landscape and portrait modes with your application, don't just assume that because it works well in portrait that your app will also be fine in landscape because that's not necessarily the case.

In portrait mode your user will have 50% more vertical space than when they are in landscape mode, so you might design something that looks great with all that vertical space, but when the phone rotates to landscape mode the app is practically unusable.

Remember, you can use an orientation change event listener to detect when the device's orientation changes in case you need to have the layout change slightly depending on what the current orientation is.

If you find that your app is just not giving the user experience you want in either of the modes, consider only allowing your app to work in the one where it does work the way you intended.

# Page Titles
As users move through your app, some screens may look similar to others.  Choose your page titles well to prevent confusion.

# Scrolling
Vertical scrolling within an app is fairly common, but horizontal scrolling is best avoided unless your app really needs it.

If your app includes an image or map view, sometimes it's just unavoidable to have things off the screen to the left and right.  In most apps, though, this is not required and is best avoided.

For example, an app that shows the user a long Tweet or email message could either have the text wrap, or require the user to scroll side-to-side to read the entire thing.  Having the text wrap gives the user the best experience, while making them scroll horizontally will feel awkward and clumsy.

# Tabs
On iOS, when more than 5 tabs are created in an app, the OS automatically creates a tab labeled "More..." so the tabs don't become too narrow to use.  Android does not, however.

On Android, your tabs will keep getting narrower the more you add and their labels will overlap, so keep this in mind if you are designing for Android.  You can handle lots of tabs any way you want to, you will just have to design and code it yourself.

# Use of Colors
Using different colors in your app can be a good thing, but overusing color will make your app look too busy and cluttered. For example, using a background color in a tableview to indicate when something is new, expiring soon, etc., is a good idea.  This simple visual queue will tell users that something in your app where the color changed needs their attention.

Using a different row in your table for each row will make your app feel clumsy and less approachable.

When choosing which colors to use where, keep in mind that some colors already have a meaning to users.  If you intend to use a color to tell your user something, choose one that they already associate with what you are trying to convey.

# White Space / Negative Space
In page layout, "white space", or "negative space", is the space between the elements on the page.  Good use of white space on a page means the content is easier to read, and the same is true in an app.  The space doesn't literally have to be white of course, it just refers to the gap or padding between, say, a graphic and a label describing it.

Having this space means your content is easier to read and to understand, this translates into your app being simpler to use, but more isn't better.

Too little space and things will be difficult to read, too much and it will look like something in the UI is missing or didn't load.

![Example of too little white space](http://img.skitch.com/20101202-baf957e7ertdfh8megk59wk799.jpg)

![Example of too much white space](http://img.skitch.com/20101202-x1rwraeg9ab2yqketh4giyh4wi.jpg)

![Example of good use of white space](http://img.skitch.com/20101202-qyiqh8w3j47mrjyau7ajt55aqi.jpg)

Another benefit to good use of white space is that the user will have room to easily tap on things such as labels with click event listeners, buttons, tableview rows, etc.  Not all fingers are created equal--your app needs to accommodate fingers of different sizes and dexterity levels.