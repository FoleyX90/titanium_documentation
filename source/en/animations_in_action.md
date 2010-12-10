<summary>
In this guide, you will learn about how to work with animations and transformations.
By the end of this guide, you should understand:

* Point to point animations
* Animating an elements opacity
* The basics of working with transforms

</summary>
#Before we start

This tutorial assumes a basic understanding of animations.  For a general introduction to animations please review the [Animation section](ui_design.html#animation).

The below video shows what we will obtain at the end of this tutorial.

<iframe src="http://player.vimeo.com/video/17666446?title=0&amp;byline=0&amp;portrait=0&amp;color=9a0707&amp;autoplay=1" width="640" height="480" frameborder="0"></iframe>

#Setting up for Animations

First of all we need a UI element to animate.  In this tutorial we will demonstrate animating **labels** and **views**.  Lets start off by creating a couple labels.

~~~
openingLabel = Titanium.UI.createLabel({
    text:'Happy Festivus',
    top: Math.round(Titanium.Platform.displayCaps.platformHeight * 0.30),
	height: 'auto',
	width:'auto',	
    shadowColor:'#aaa',
    shadowOffset:{x:3,y:3},
    color:'#900',
    font:{fontSize:openingLabelFontsize},
    textAlign:'center'
});

closingLabel = Titanium.UI.createLabel({
    text:'The End',
    height:'auto',
    width:'auto',
    color:'#fff',
    font:{fontSize:closingLabelFontsize},
    textAlign:'center',
	opacity: 0
});
~~~
We'll use the **openingLabel** to demonstrate 3D matrix transforms and save the **closingLabel** for demonstrating [opacity animation](ui_design.html#opacity).  Lets take a closer look at **openingLabel** first.  We already have our label so lets go ahead and create a 3D matrix that we will use as part of the animation:

~~~
var olt = Titanium.UI.create3DMatrix();
olt = olt.rotate(200,0,1,1);
olt = olt.scale(2);
olt = olt.translate(20,50,170);
olt.m34 = 1.0/-3000;
~~~

[2D](ui_design.html#2d_matrix) & [3D](ui_design.html#3d_matrix) matrices provide a number of methods that allow us to operate on the newly created matrix.  Refer to the [Titanium.UI.2DMatrix](https://developer.appcelerator.com/apidoc/mobile/1.0/Titanium.UI.2DMatrix) & [Titanium.UI.3DMatrix](https://developer.appcelerator.com/apidoc/mobile/1.0/Titanium.UI.3DMatrix) API Docs for more information on these.

#Starting an Animation

To animate our label we call the **animate** method on our label passing it an object that contains a [transform](ui_design.html#transforms) and a duration.  The transform in this case is the 3D matrix we created previously and the duration is simply the number of milliseconds we would like this animation to last.  A callback function can also be provided which will allow for us to take some action after the animation has completed.

~~~
openingLabel.animate(
    {transform: olt, duration: 1500}, 
    function() {
	    //Tasks to perform after the animation has completed
    });
~~~

When applied to our **openingLabel** the result is a label that grows, spins, and eventually moves out of view.


#Using Animation Objects

The animation object is used for specifying lower-level animation properties and more low-level control of events during an animation. An animation object can be created via Titanium.UI.createAnimation.  We'll make use of this to animate the **closingLabel** in this example.  The **closingLabel** is initially hidden via opacity 0.  Lets look at how we can animate the opacity of this UI element and scale it at the same time.  This will enable us to create an appear/zoom effect for the closing credits of this example.

~~~
closingLabel.animate(Titanium.UI.createAnimation({
	opacity: 100,
	duration: 2500,
	transform: Titanium.UI.create2DMatrix({
		scale: 1.5
	})
}));
~~~

Over the course of 2500 milliseconds this label will grow 1.5x the size and fade in to become fully visible.

#Animating Views

![Snowflake](http://developer.appcelerator.com.s3.amazonaws.com/documentation-examples/animation_snowflake_example.jpg "Snowflake example")

Of course the most interesting part of this example is the falling snowflakes.  Lets review how such an effect might be created.  Snowflakes come in all shapes and sizes.  Their path to the ground is influenced by things like wind and other objects meet in flight.  To imitate such behavior we'll need to create **views** of varying shapes, sizes, angles, etc.  We'll also need to randomize the location the start their journey and their path to the ground.  We'll make use of the Animation object, 2D matrices, opacity, duration, etc.  Lets start by creating a few helper functions:

~~~
//Used to randomize a logo's initial left position
function getRandomLeftPostion() {
	var leftVal = 0;
	while (leftVal < 10) {
		leftVal = Math.floor(Math.random()*Titanium.Platform.displayCaps.platformWidth);
	}
	return leftVal;
}

//Used to build a transform with some randomized attributes
function getRandomTransform() {
	var rotateVal  = Math.floor(Math.random()*100),
		scalingVal = 0;
	
	while (scalingVal < 0.1) {
		scalingVal = Math.random().toFixed(1);
	}
	
	return Titanium.UI.create2DMatrix({
		rotate: rotateVal,
		scale: scalingVal
	});
}

//Used to create a uniquish looking logo that we'll use in animations
function getImageViewToAnimate() {
    //We'll alternate between two background images
	bImage = (viewBackgroundImage === 'appcelerator' ? 'snowflake' : 'appcelerator');
	viewBackgroundImage = bImage;
	
	return Titanium.UI.createView({
		backgroundImage:'images/' + bImage + '.png',
		top: Math.floor(Math.random()*200), //start anywhere from top 0 to 200
		left: getRandomLeftPostion(),
		height:95,
		width:83,
		opacity: 0.75,
		visible: false,
		transform: getRandomTransform()
	});
}
~~~

With our helper functions in place we'll build up a set of snowflakes (**views** with a background image) to play with:

~~~
//Build up an array of viewsToAnimate (views) and add them to the current window
for(var i=0; i<30; i++) {
	var viewToAnimate = getImageViewToAnimate();

	viewsToAnimate[viewsToAnimate.length] = viewToAnimate;
	tiWindow.add(viewToAnimate);
}
~~~

When we are ready for the snowfall to begin we iterate over our snowflake array and call the animate method on each view.

~~~
viewsToAnimate[a].animate(Titanium.UI.createAnimation({
	top: (Titanium.Platform.displayCaps.platformHeight - 65),
	left: getRandomLeftPostion(),
	opacity: 1,
	curve: Ti.UI.ANIMATION_CURVE_LINEAR,
	duration: 3000+(Math.random()*(6000-3000)),
	repeat: 3
}));
~~~

We are passing a custom animation object each time we call animate.  When we created the **viewsToAnimate** array earlier each view was given a random [top and left starting position](ui_design.html#common_ui_properties).  You'll notice we are also setting these properties again in our custom animation object, but with different values.  **Top** is being set to a value just shy of the bottom of the screen.  This is so that we can make the snowflakes appear to pile up at the bottom of the screen like snow.  We could have used some conditional logic to determine the platform and based on that knowledge hardcoded some screen dimensions to figure out the correct **top** value offset needed to achieve this effect.  However, as we can see in this example, there is another option.  **Titanium.Platform.displayCaps** provides us with platformHeight & platformWidth properties that we can use to do the same thing without the extra overhead.  Setting a new **left** value will cause our snowflake to move either left or right (depending on the original position) like the wind is blowing it.  To make that left to right movement a bit smoother we use the [**Ti.UI.ANIMATION_CURVE_LINEAR** curve constant](https://developer.appcelerator.com/apidoc/mobile/1.0/Titanium.UI).

We initially created 30 snowflakes, but we want the overall duration of the example to last a bit longer than the time it takes for 30 snowflakes to fall without dramatically slowing down each snowflake.  To help solve this we make use of the **repeat** property.  With repeat set at 3 each animation repeats 3 times and we end up with 90 falling snowflakes.

#Download the project

The full source for this tutorial is available for both iPhone & iPad.  Download it [here](https://github.com/appcelerator/Documentation-Examples/tree/master/animations).

