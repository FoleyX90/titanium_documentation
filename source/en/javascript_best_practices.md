<summary>
This guide covers a variety of best practices when developing JavaScript applications in Titanium.
</summary>

# JavaScript Best Practices

There are any number of very good books and tutorials on JavaScript best practices out there today, but for
developers coming to Titanium with a limited background in JavaScript, we'd like to shared a few general best
practices to be aware of when developing JavaScript applications.

## Don't pollute the global scope!

In an execution context, by default all variables are global.  The only means of scoping variables in JavaScript
is to place them inside of a function.  A much better approach than global variables/functions is to enclose all
your application's API functions and properties into a single variable (namespace).  This will minimize the chances
of your code colliding with other code or libraries you include in the context later.

	//app.js
	//------
	
	// BAD - we put five variables in the global scope which could be clobbered
	var key = 'value',
		foo = 'bar',
		charlie = 'horse';
	
	function helper() {
		//help out
	}
	
	function info(msg) {
		helper(msg);
		Ti.API.info(msg);
	}
	
	//Better - enclose everything but your public namespace inside a self-calling
	//function... now we only have 1 variable in the global scope
	
	// Now, 'myapp' is the only global variable, which is good
	var myapp = {
		key: 'value',
		foo: 'bar',
		charlie: 'horse'
	};
	
	(function() {
		function helper() {
			//help out
		}
		
		myapp.info = function(msg) {
			helper(msg);
			Ti.API.info(msg)
		};
	})();

## Use `===` and `!==` instead of `==` and `!=`

Called by some the "Compare, damn it!" operator, `===` performs what a `==` operator might in other languages.
If the two operands are equal in type and value, `===` will return true and `!==` will return false which is almost
always what you mean.  This is a common gotcha and fits nicely in the category of JavaScript language quirks.

## Lots of variables?  Use a comma.

You don't need to put `var` in front of every variable - you can use commas to replace:

	var foo = true;
	var me = 'awesome';

with:

	var foo = true, me = awesome;

## Efficient loops
In some situations, checking the length of an array during every iteration can be slow.  So rather than writing:

	var names = ['Jeff','Nolan','Marshall','Don'];
	for(var i=0;i<names.length;i++){
		process(names[i]);
	}
	
It is better to only get the length of the array only once, as in:

	var names = ['Jeff','Nolan','Marshall','Don'];
	for(var i=0,j=names.length;i<j;i++){
	  	process(names[i]);
	}
	
## Wrap self-calling functions in parens

As you start to realize the utility of self-calling functions, you may be tempted to write a self-calling function as:

	var myValue = function() {
		//do stuff
		return someValue;
	}();
	
While syntactically correct, someone reading this code (missing the () at the end of the function declaration) might
think you are assigning a function to `myValue`, rather than the return value of the function.  A better way to write
this is with wrapping parentheses:

	var myValue = (function() {
		//do stuff
		return someValue;
	})();
	
In this case it is clear that myValue is not a function, but the return value of the function.
	
## Avoid deep nesting

On Android, Rhino will occasionally cause your app to run out of memory if you have several levels of recursion or iteration
in a function.  If you run into a "recursion to deep" error, try and flatten out your code in areas where
you have several levels of nested loops or recursive code.

# Other resources and articles

Obviously, this is not an exhaustive list.  If you're really interested in learning about JavaScript best practices,
I strongly recommend picking up a copy of Douglas Crockford's [JavaScript - The Good Parts](http://oreilly.com/catalog/9780596517748).
Some other online resources, for which you mileage may vary:

* [Opera's JavaScript Best Practices](http://dev.opera.com/articles/view/javascript-best-practices/) (editorial opinion: Hungarian notation in JavaScript is dumb)
* [Presentation: JavaScript Best Practices](http://www.slideshare.net/cheilmann/javascript-best-practices-1041724)
* [Hacker News thread on JS best practices](http://news.ycombinator.com/item?id=835991)
* [JavaScript in Ten Minutes](https://github.com/spencertipping/js-in-ten-minutes)