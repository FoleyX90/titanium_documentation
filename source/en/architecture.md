<summary>
This guide covers the basic architecture of Appcelerator Titanium&trade;. After reading it, you should be familiar with:

* The general idea of how Titanium works
* The basic principles of Titanium design (Model, Views, Events)
</summary>

# How does Titanium work?

Although each platform that Titanium supports is implemented differently it is conceptually similar in design. Titanium works by translating your JavaScript code into a native application code and then invokes the platform underlying tools to build the final package.

How this is completed depends on the platform implementation.  Titanium is conceptual build with three distinctive building blocks:

* Pre-compiler
* Front-end compiler
* Platform compiler & packager

<note>
    By using Titanium, you typically don't need to know about the internals of how Titanium builds your application. We attempt to shield you from all these messy details in the Titanium Developer tool and integrate all these complex steps for you.
</note>

## Pre-compiler

The Titanium pre-compilers role is to take your application's JavaScript code and optimize it (reduce whitespace, reduce the size of symbols, etc) and then create a dependency hierarchy of all the Titanium APIs used by your application.

## Front end compiler

The role of the front-end compiler is to generate the appropriate platform-specific native code, native project (if necessary) and build any specific code that is necessary to compile Titanium for a given platform compiler.

## Platform compiler & packager

Each native platform has a set of associated tools (for example, Xcode for iOS) that are used to compile the final native application.  After compilation, your application is packaged for 
running either on the native simulator, native device for testing or for final packaging for
distribution.

# Titanium Design Concepts

The Titanium design is structured in a way that should be familiar to JavaScript developers.
Titanium uses a typical MVC (model view controller) design concept for building your application.  

The Titanium UI (user interface) is native.  Although in Titanium you use JavaScript to author your application, unlike a web browser application, Titanium  UI is built with native components and does not rely on a web browser control to host your application and render it.  When Titanium compiles your application, it uses the underlying components of the native UI not the web browser.  This means your application performs and acts like a true native application.

In Titanium, you will use a standard set of APIs that are pre-built in to Titanium and that will provide you with the capabilities to build your application. These APIs are split into various namespaces such as [[Titanium.UI]] (for User Interface) or [[Titanium.Network]] (for networking).

In your application code, you can either use `Titanium` or `Ti` which are the same reference - `Ti` simply acts like a shortcut to `Titanium`.

The following are the major design components in Titanium:

* Windows - windows host one or most Views
* Views - views draw content on the screen
* Widgets - widgets are special types of views that perform specific actions like buttons

## Windows

Windows have a lifecycle and host one or more Views inside them.  A Window itself is a View. A Window can be opened and closed.  A Window can either be full-screen, modal or partial screen (meaning it takes up less than 100% of the full screen).

A Window can itself be self-contained or its contents be controlled by another JavaScript file.

### Self-contained Windows

For example, to create a simple Window, you could do the following:

<code class="javascript">
var win = Ti.UI.createWindow();
var view = Ti.UI.createView({backgroundColor:"red"});
win.add(view);
win.open();
</code>

In the above example, we create a self-contained Window and then create a View that is red.  We add the View to the Window and then open the Window.

In iOS, you should see the following:

![redwindow](http://img.skitch.com/20101024-tiaw9w7xqsr919ktqikss8f46q.png)

This code is platform independent, meaning it will render and function the same in all Titanium environments.

### URL-based Windows

Sometimes it's easier to structure your application where the logic for a given Window
comes from a separate JavaScript file.  The URL for a URL-based Window must be local - meaning that it must be included in your project `Resources` directory and compiled in to your application.

We could restructure the above code to use a URL-based design.

First, in your `app.js`, you would add:

<code class="javascript">
    var win = Ti.UI.createWindow({url:"view.js"});
    win.open();
</code>

Then, create a file named `view.js` and add the following code:

<code class="javascript">
    var win = Ti.UI.currentWindow;
    var view = Ti.UI.createView({backgroundColor:"red"});
    win.add(view);
</code>

Notice that the `win` variable points to `Ti.UI.currentWindow`.  Titanium defines a set of special variables in your JavaScript context automatically for you which allow you. `Ti.UI.currentWindow` defines the Window reference that owns (opened) the current Window so you can still reference it.

When you run this example, you should see the exact same result as above.

## Views

Views are user-interface components.  Views are hierarchal - they can contain children.  Views can have a z-order - meaning they can be stacked on top or below another view at the same position.  

In Titanium, a good number of the `Titanium.UI` classes are specialized versions of a View.
However, in Titanium, you can create a simple View which can be powerful all by itself.

For example, let's create a view that is simply an image from a PNG file.

<code class="javascript">
    var win = Ti.UI.createWindow();
    var view = Ti.UI.createView({backgroundImage:"myimage.png"});
    win.add(view);
    win.open();
</code>

When you run the following, you should see the following on the iOS simulator:

![window](http://img.skitch.com/20101024-ctd4eycbe1xd8au6kfcs2ermj3.png)

This looks ugly! Why?  In our code above, we didn't provide any dimensions, so the view applied the backgroundImage to stretch the contents of the View itself. Since we didn't provide any size for the view, it will automatically take up 100% of the parent (superview) container.  This could be good or bad depending on what you're trying to accomplish.

Titanium has a specialized View at `Titanium.UI.ImageView` that provides you with some additional capabilities. Let's use the ImageView API to add the image.

<code class="javascript">
    var win = Ti.UI.createWindow();
    var view = Ti.UI.createImageView({
        image:"myimage.png",
        width:24,
        height:24
    });
    win.add(view);
    win.open();
</code>

You should now see the following:

![imageview](http://img.skitch.com/20101024-e1wpb7i834fdaymqnbsybuqjys.png)

In the above code, we're explicitly loading the image into a view at a specific size (24x24).  The ImageView supports scaling to either larger or smaller sizes.  However, if you didn't specify a set of dimensions, the ImageView would also size itself to the parent View dimensions.

Also, because we didn't provide any positional properties (such as top, left, right, bottom), the view will automatically be centered inside the parent View.

#### Adding interactivity

Views can have interaction. Let's make the view change size based on a touch.  This will demonstrate the use of Events in Titanium.

<code class="javascript">
    view.addEventListener('click',function()
    {
    	view.animate({width:96,height:96,duration:1000});
    });
</code>

In the above code, when the user touches the icon, the image will grow four times its size over 1 second in duration.  

Of course, sometimes you might want something a little more sophisticated and you need to use transformations.

<code class="javascript">
    view.addEventListener('click',function()
    {
    	var t = Ti.UI.create2DMatrix();
    	t = t.rotate(-90).scale(4);
    	view.animate({transform:t,duration:1000});
    });
</code>

In the above code, we're going to create a [Titanium.UI.2DMatrix](http://developer.appcelerator.com/apidoc/mobile/latest/Titanium.UI.2DMatrix-object.html) and rotate it -90 degrees and scale the size of the image by four.
  

## Widgets

Widgets are simply special types of Views that have special functionality such as Buttons and Textfields.  Underneath the cover a Widget is a View.  However, unlike typical Views, Widgets cannot themselves have children.

In this example, let's add a button that will drive the animation instead.

<code class="javascript">
    var win = Ti.UI.createWindow();
    var view = Ti.UI.createImageView({
        image:"myimage.png",
        width:24,
        height:24
    });
    var button = Ti.UI.createButton({
        title:"Animate",
        width:80,
        height:40,
        bottom:10
    });
    button.addEventListener("click",function(){
        view.animate({top:0,duration:500});
    });
    win.add(view);
    win.add(button);
    win.open();
</code>

Upon clicking the button, the image should fly to the top of the screen by setting the `top` property to `0`.

