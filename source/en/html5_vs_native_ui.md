<summary>
    The following guide tries to show the difference between building applications using HTML5 ( embedded or not in a webview) and Appcelerator Titanium&trade; native framework.
</summary>

#First thing you need to know

Despite the fact that Titanium uses JavaScript as programming language, it has nothing in common with HTML. Every single JS instruction you write is converted in pure ObjectiveC.
In Titanium Mobile it doesn't exist DOM, so the usual frameworks (MooTools, jQuery, etc) won't work (maybe a server version of the framework will do, but there is no point in deploying 100k of javascript just to have some syntax sugar).

There are community contributions that bring to Titanium the familiar look and functionality of this frameworks and is more indicated to use one of this as being dedicated to extend Titanium.

Even if the syntax,properties and methods are similar to the DOM model, this is only to facilitate the learning/usage by a user that comes from the web development world.


#HTML5 vs Native UI

When we are developing an application for mobile platforms we have to think all the time on performance. The mobile devices have limited resources. There are may devices with Android with slow CPUs, the first generations of iOs devices or older BlackBerries. Not even the most advanced mobile device on the market can compete with a computer, so we really need to make our application as slim as possible.

The below example of a simple black text "Hello Titanium!" on white background build using both HTML and Native will show the big difference in resources consumption using both techniques.

**The embedded webview with the html code:**

~~~
var win = Titanium.UI.createWindow({
	backgroundColor:'#fff'
});

var web_view = Titanium.UI.createWebView({
	html:'<html><head></head><body>Hello Titanium</body></html>'
})

win.add(web_view);
win.open();
~~~

**The Native code:**

~~~
var win = Titanium.UI.createWindow({
	backgroundColor:'#fff'
});

var text_label = Titanium.UI.createLabel({
	text:'Hello Titanium'
})

win.add(text_label);
win.open();
~~~
 
Both examples looks to be the same from the coder point of view - the number of elements it's the same and we have almost the same amount of code to be written.
From the device point of view, the above examples will behave as it follows:

Let's start with the **Native** code:
The OS creates a window then a label (that is a view specialized in rendering simple text), it attaches the label to the window, then opens the window. 

Now the **HTML** code:

The OS creates a window.
Then create a webView. A webview is nothing else then a mobile safari that you can embed in your app, without the interface (chromeless). 

It means it loads 

* a DOM parser, 
* a JavaScript interpreter, 
* a CSS parser, 
* an HTML renderer, 
* a SVG renderer, 
* a Canvas renderer, 
* a history manager (to go back and forward ), 
* a SQLLite engine (for cookies and local storage),
* all the methods you might need to manipulate all of the above
* the events you might need to capture (load, etc).

After all this resources are loaded the html property we set in the constructor is parsed, checked for javascript/css and rendered.
After this the OS opens the window.

This is a very simple case scenario.
If we want to make a more complex application things gets complicated - in HTML we need to replicate the interface elements, to use some javascript (more or less heavy) to copy the behavior of the UI elements ( a table scroll for example), etc. Using the Native code we have this by default, optimized and working at a lower level with the OS.

#When not to use HTML

HTML should be avoided as much as possible.Almost everything you need it can be done using native code. The app will load faster and will react faster to the user's actions leading to a better user experience.

#When to use HTML

There are cases when the webview cannot be avoided.
* If you need to render formatted text, it doesn't exist yet a native control that is able to do this. But stick with rendering the content only.
* When you need to open external urls. If you do this is better to open a new window that get closed when the user returns to your app and so resources are freed.






