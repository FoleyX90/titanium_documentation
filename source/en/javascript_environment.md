<summary>
In this guide, you will learn about the JavaScript runtime environment in which your application code executes.
By the end of this guide, you should understand:

* The basics of the JavaScript engine used by Titanium
* Single versus multiple execution contexts
* How to include external JavaScript files/libraries
* What built-in functionality exists in the global namespace

</summary>

# The Titanium JavaScript Environment

In a Titanium Mobile application, your source code is packaged into a binary file and then interpreted at runtime by a JavaScript
engine bundled in by the Titanium build process.  In this guide, you will learn more about the JavaScript runtime environment that
your code runs in.

# The JavaScript Engine

Titanium runs your application's JavaScript using one of two JavaScript interpreters - [JavaScriptCore](http://webkit.org/projects/javascript/) 
on iOS (the interpreter used by Webkit), [Mozilla Rhino](http://www.mozilla.org/rhino/) on Android, and the Browser Field object on BlackBerry.
These engines provide a standard JavaScript interpreter with most of the functionality you would be used to in the web browser, with a few
notable exceptions (mainly the DOM APIs and other browser-specific trappings).  However, Titanium has supplemented the global namespace 
with some global functions JavaScript developers would be accustomed to.

## Built-In Functions

There are a number of functions built into the global namespace in your mobile JavaScript application.  They are formally addressed
in the [official API documentation](http://developer.appcelerator.com/apidoc/mobile/latest), but we'll enumerate several of these
functions here to make you aware of them.

* `setTimeout` - schedule a function to be called once after a certain number of milliseconds
* `setInterval` - schedule a function to be called on a regular interval, specified in milliseconds
* `clearInterval` - remove a function executing on interval
* `alert` - display a simple native alert dialog with text (for quick and dirty visual debugging, in lieu of logging)
* `JSON` - Titanium provides a standard JSON serialization/deserialization mechanism via the JSON namespace (`JSON.parse` and `JSON.stringify`)

## The Titanium Namespace

In addition to the above built-in functions, Titanium-specific APIs are found in the `Titanium` namespace.  `Titanium` is also
aliased to `Ti` to save you some keystrokes, but they are equivalent.  The Titanium namespace provides many functions, properties,
and events that you can use to create a native mobile application - 
[check out the reference documentation for more](http://developer.appcelerator.com/apidoc/mobile/latest) on what is available in the
`Ti` namespace.

# Execution Contexts

By default, a Titanium Mobile application has a single "execution context" in which an application runs.  In our case, an 
"execution context" is similar to the single JavaScript thread provided to JavaScript applications in the web browser.  Your 
application's `app.js` file bootstraps your application and serves as the root application context.  All variables declared in a context 
are available globally.  

## Including external JavaScript files

It is possible to include files in the current execution context, much like using a `&lt;script&gt;` tag in an HTML page.

	Ti.include('myscript.js');
	
Scripts included into the current context via `include` are executed globally for the context, and are not affected by functional
scope.  Let's say `somescript.js` contains a single variable declaration:

	var something = true;
	
The following code in app.js:

	Ti.include('somescript.js');
	
	if (something) {
		Ti.API.info('something is true');
	}

And this code are equivalent - notice that includes are always global, regardless of the scope they are called in:

	(function() {
		Ti.include('somescript.js');
	})();
	
	if (something) {
		Ti.API.info('something is true');
	}


## Multiple execution contexts

Your application can have multiple execution contexts.  New execution contexts are typically created by opening a new window
that points to an external URL in its `url` property:

	Ti.UI.createWindow({
		url:'window.js'
	}).open();
	
When the window is opened, the script `window.js` is immediately run in a new execution context. If the preceding code were 
run in `app.js`, any variables or function declarations made in app.js would be unavailable:

![figure](http://img.skitch.com/20101130-kr7b3bqhd5e3suepfiag38991k.png)

## Passing data between contexts

It is possible to communicate across execution contexts using application-level events.  Using Titanium's custom event
API, arbitrary JavaScript data structures can be sent and received in different execution contexts.  Note that the
'payload' of your event must be JSON serializable, so business objects will not preserve any instance methods associated
with them.  The APIs used to fire and receive events are in the `Ti.App` namespace:

	//to fire...
	
	Ti.App.fireEvent('customEvent', {
		myData:true,
		someStuff:[
			'foo',
			'bar'
		]
	});
	
	//to receive...
	
	Ti.App.addEventListener('customEvent', function(eventData) {
		alert(eventData.someStuff[0]); //will alert 'foo'
	});

The following illustrates how this might look in a very simple Titanium Mobile application:

![sample](http://img.skitch.com/20101130-kcryuu56sbk5uryfstjd9bf2n2.png)

## Should I use a single context or multiple contexts?

As is often the case in software development, the answer is "that depends".  Most of the time, it is probably advisable to use a
single execution context, for a couple of reasons:

* You can pass complex objects in custom events
* You only include your libraries/dependencies only once, since there's only one context

In most of the projects done by Appcelerator's own Professional Services team on Titanium Mobile, a single execution context with
multiple `include`-ed external files is used.  However, there are instances where having multiple execution contexts is useful.  For
example, in our [Kitchen Sink](http://github.com/appcelerator/KitchenSink) application, it is advantageous to have a 'clean slate'
for every API usage example, so we don't have to worry about polluting the global scope and can keep the examples easy.  It could be 
there are other reasons to want or need this 'clean slate' in your own application.  In fact, that brings up a good point...

## Don't pollute the global scope!

This is more of a general JavaScript best practice, since it is important in the web browser as well.  Declaring a lot of global
variables and functions in an execution context leaves your code at risk of colliding with its self or other included libraries.
To avoid this, use closures and self-calling functions to encapsulate your code.  A rational include file would look something
like this:

	var myAPI = {}; // This is a variable I intend to be 
					// global, since I want
					// people who inculde my file to 
					// have visibility to it
	
	(function() {
		// put my implementation inside a self-calling function,
		// so I can go crazy with local functions and variables
		
		function helper() {
			//do stuff
		}
		
		var state_variable = true;
		
		//then, create a controlled public API...
		
		myAPI.doSomething = function() {
			//do something
		};
	})();
	
These and other best practices are covered in [JavaScript Best Practices](javascript_best_practices.html).