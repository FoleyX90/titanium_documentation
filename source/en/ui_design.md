<summary>
This guide covers how User Interfaces are designed and developed using Ti. After reading it, you should be familiar with the following concepts:
    
* How to layout your UI in Titanium
* Advanced application layout techniques
* Platform specific UI capabilities

</summary>

<note>
    You should be familiar with the basic [Titanium architecture](architecture.html) before continuing with this guide.
</note>

# Positioning and Coordinate system

Titanium uses a left, top coordinate system.  The 0,0 position is the top, left position of the View or Window.  In Titanium, you can also use negative coordinates.  For example, the following View as a child of the main Window would put the view offscreen:

<code class="javascript">
    var window = Ti.UI.createWindow();
    var view = Ti.UI.createView({
        top:-20,
        width:10,
        height:10,
        backgroundColor:"red"
    });
    window.add(view);
    window.open();
</code>

In Titanium, we could move it on screen with a shake with the following example:

<code class="javascript">
    var window = Ti.UI.createWindow();
    var view = Ti.UI.createView({
        top:-20,
        width:10,
        height:10,
        backgroundColor:"red"
    });
    window.add(view);
    window.open();
    Ti.Gesture.addEventListener('shake',function()
    {
        view.animate({top:view.top + 40, duration:500});
    });
</code>

In the above code, each Titanium the device receives a `shake` gesture event, the view will animate by sliding down 40 pixels over a 1/2 second duration.

## Default position

When no specific position is specified, the View will be placed in the center of the parent View.

## Default size

When no specific size is specified, the View will attempt to take up 100% of the parent View's size.

## Default color

When no color for a View is specified, the View will be transparent.

# Common UI Properties

The following properties are common when dealing with positioning and dimensions.

## top

The `top` property specifies how many pixels from the superview's (the parent View) top position the view should be placed.

## right

The `right` property specifies how many pixels from the superview's (the parent View) right position the view should be placed.

## bottom

The `bottom` property specifies how many pixels from the superview's (the parent View) bottom position the view should be placed.

## left

The `left` property specifies how many pixels from the superview's (the parent View) left position the view should be placed.

## width

The `width` property specifies the size from left to right of the view.  

## height

The `height` property specifies the size from top to bottom of the view.

The `width` and `height` property can be expressed as a number, a string designator (such as `20px` as in 20 pixels) or a string designator (such as '50%' as in 50% of the parent View).  When values are expressed as numbers, they are assumed to be pixels.


# Animation

An important part of designing a great UI is making the interface interactive and smooth.

Titanium provides built-in Animation capabilities that are optimized for each device.  For example, on iOS devices, animations perform on the GPU and provide high performance capabilities.

## Basic Animation

Any Window, View or Widget in Titanium can be animated with the `animate` method. The `animate` method will perform a set of animation against the view and animation events can be handled to perform complex timelines.

Let's start with a basic animation.  In the below example, we want to cause the view to pop out in nice animation effect when the button is clicked.

<code class="javascript">
    var window = Ti.UI.createWindow();
    var button = Ti.UI.createButton({
        title:"Animate",
        width:100,
        height:40
    });
    window.add(button);
    window.open();
    button.addEventListener("click",function()
    {
        // initially scale the window to 0, meaning invisible
        var t = Ti.UI.create2DMatrix().scale(0);
        var w = Ti.UI.createWindow({
        	backgroundColor:'#336699',
        	borderWidth:8,
        	borderColor:'#999',
        	height:400,
        	width:300,
        	borderRadius:10,
        	opacity:0.92,
        	transform:t
        });
        // create first transform to go beyond normal size
        var t1 = Ti.UI.create2DMatrix().scale(1.1);
        var a = Ti.UI.createAnimation();
        a.transform = t1;
        a.duration = 200;
        // when this animation completes, scale to normal size
        // this gives it a nice pop
        a.addEventListener('complete', function()
        {
        	var t2 = Ti.UI.create2DMatrix().scale(1.0);
        	w.animate({transform:t2, duration:200});
        });
        // create a button to close window
        var b = Ti.UI.createButton({
        	title:'Close',
        	height:30,
        	width:150
        });
        w.add(b);
        b.addEventListener('click', function()
        {
        	var t3 = Ti.UI.create2DMatrix().scale(0);
        	w.close({transform:t3,duration:300});
        });
        // open the window with the initial animation
        w.open(a);
    });
</code>

In the above example, you'll note that we're using animation events to control the animation timeline.  We initially scale the view from zero (meaning, no size) to be bigger than the final size and then immediately scale it back to normal size. This will give the window a nice pop effect.

This example also shows how you can animate a window `open` with an animation object.  The animation object is also similar to passing the properties via the `animate` method.  However, the animate object provides more fine grain listeners and also provides an easier ability to reuse animations.

## 2D Matrix

Titanium provides a [2D Matrix](http://developer.appcelerator.com/apidoc/mobile/latest/Titanium.UI.2DMatrix-object) class for holding values for an affine transformation matrix. A 2D matrix is used to rotate, scale, translate, or skew the objects in a two-dimensional space. A 2D matrix is represented by a 3 by 3 matrix. Because the third column is always (0,0,1), the data structure contains values for only the first two columns.

To create a 2D matrix, you simply call the factory method:

<code class="javascript">
    var m = Ti.UI.create2DMatrix();
</code>

The [initial matrix](http://en.wikipedia.org/wiki/Identity_matrix) is always the "identity matrix" which is the simplest nontrivial diagonal matrix. 

You can apply methods against the resulting matrix object to create a new representation. You must use the returned object. 

<code class="javascript">
    var m = Ti.UI.create2DMatrix();
    m = m.scale(2);
</code>

You can also chain multiple function calls together since the return value is another 2D Matrix object.

<code class="javascript">
    var m = Ti.UI.create2DMatrix();
    m = m.scale(2).rotate(-90);
</code>

## 3D Matrix

Titanium provides a [3D Matrix](http://developer.appcelerator.com/apidoc/mobile/latest/Titanium.UI.3DMatrix-object) class for holding values for an affine transformation matrix. A 3D matrix is used to rotate, scale, translate, or skew the objects in a three-dimensional space. A 3D matrix is represented by a 4 by 4 matrix. Because the forth column is always (0,0,1), the data structure contains values for only the first three columns.

The 2D Matrix and 3D Matrix are similar in usage.

## Transforms

To use the matrix, you simply call the `transform` property on a View.  By setting the `transform` property, the change takes effect immediately.

<code class="javascript">
    var m = Ti.UI.create2DMatrix().scale(2);
    view.transform = m;
</code>

If you'd like to animate the transform, you should either set the `transform` property of an Animation object or the `transform` property of the `animate` function.

For example, using as a `transform` property of the `animate` function:

<code class="javascript">
    var m = Ti.UI.create2DMatrix().scale(2);
    view.animate({transform:m,duration:400});
</code>

For example, using as a `transform` property of the Animate object:

<code class="javascript">
    var m = Ti.UI.create2DMatrix().scale(2);
    var a = Ti.UI.createAnimation();
    a.duration = 400;
    a.transform = m;
    view.animate(a);
</code>


## Window animation

You can apply an animation to the following functions of a Window:

* open - apply an animation while opening the Window
* close - apply an animation while opening the Window
* animate - apply an animation immediately on the Window


## Window transitions

You can also apply a Window transition using the `transition` property.  Transitions provide a transition animation between two windows.

<warning>
    Currently, this is only supported in iOS.
</warning>

For example:

<code class="javascript">
    window.open({
	    transition:Titanium.UI.iPhone.AnimationStyle.FLIP_FROM_LEFT
    });
</code>

The `transition` property also applies to an Animation object and the `animate` function.

The following styles are supported on [Titanium.UI.iPhone.AnimationStyle](http://developer.appcelerator.com/apidoc/mobile/latest/Titanium.UI.iPhone.AnimationStyle-object):

* CURL_DOWN: Curl downwards during a transition animation
* CURL_UP: Curl upwards during a transition animation
* FLIP_FROM_LEFT: Flip from left to right during a transition animation
* FLIP_FROM_RIGHT: Flip from right to left during a transition animation
* NONE: No Animation


## Opacity

When performing an animation, you will want to spend time on the aesthetics to make the animation seem more life-like.  The `opacity` property is a good property to keep in mind when performing animations where you're changing the visual state between one or more Views.

The `opacity` property controls the transparency (or opacity) of the View. Typically, you'll bring the opacity from `0.0` to some end state, such as `1.0` during the animation.  This will provide a "fade in" effect and make the View seem to "appear" on the screen.

In this example, the view is initially set to `0` - effectively making it fully transparent, or invisible.  When the button is clicked, the view simply animates it's `opacity` property from `0.0` to `1.0`, making it appear to fade in.

<code class="javascript">
    view.opacity = 0;
    button.addEventListener("click",function(){
        view.animate({
            opacity:1.0,
            duration:500
        });
    });
</code>


# Advanced Layout 

Sometimes when you're building a more complicated UI you'll need more advanced layout techniques that help will you construct the UI.

## Using zIndex

The `zIndex` property of a View specifies the stack order of the View relative to other Views at the same position.

For example, assume we had 3 overlapping Views:

<code class="javascript">
    var window = Ti.UI.createWindow();
    var view1 = Ti.UI.createView({
    	backgroundColor:'pink',
    	zIndex:10,
    	width:200,
    	height:30,
    	top:10,
    	left:10
    });
    var view2 = Ti.UI.createView({
    	backgroundColor:'blue',
    	zIndex:11,
    	width:200,
    	height:30,
    	top:15,
    	left:15
    });
    var view3 = Ti.UI.createView({
    	backgroundColor:'red',
    	zIndex:12,
    	width:200,
    	height:30,
    	top:20,
    	left:20
    });
    window.add(view3);
    window.add(view2);
    window.add(view1);
    window.open();
</code>

In the above example, you should see the following screen:

![zindex](http://img.skitch.com/20101025-k2s9hu1ax3pb143pr626fdb1fd.png)

You'll note from the above code that the pink view (view1) has a higher `zIndex` value and thus is stacked on top of the blue (view2) and red (view3) views near the same position even though it is added last. 

## Using Background Images

You can use an background image on a View.  The background image is specified with the `backgroundImage` property and the image will automatically be stretched (if smaller) to the entire size of the View.

<code class="javascript">
    var window = Ti.UI.createWindow({
        backgroundImage:"my_background.png"
    });
    window.open();
</code>


## Using Gradients

Background gradients can be created dynamically on a View by specifying the `backgroundGradient` property.

<warning>
    Currently, this is only supported in iOS.
</warning>

For example, to create a linear gradient, you could use the following example:

<code class="javascript">
    var window = Ti.UI.createWindow();
    var view = Ti.UI.createView({
        backgroundGradient:{
    		type:'linear',
            colors:[
                {color:'#d4d4d4',position:0.0},
                {color:'#666666',position:0.50},
                {color:'#b4b4b4',position:1.0}
            ]
        }
    });
    window.add(view);
    window.open();
</code>

This code should look like the following:

![gradient](http://img.skitch.com/20101025-x9ckm8s5ptw84phdmhd86ijgrb.png)

Notice that the stops can be controlled with the `colors` property of the `backgroundGradient` object.  

## Using Rounded Borders

You can round the borders of a View by using the `borderRadius` property.  When using the `borderRadius` property you must also use the `borderColor`. Optionally, you can set the width of the border with the property `borderWidth` (defaults to 1 pixel).

For example:

<code class="javascript">
    var window = Ti.UI.createWindow();
    var view = Ti.UI.createView({
    	backgroundColor:"#999",
    	borderRadius:20,
    	borderWidth:10,
    	borderColor:'#336699'
    });
    window.add(view);
    window.open();
</code>

This should appear as the following:

![border](http://img.skitch.com/20101025-gd6g4y8tci5pg4tckwms42ebhi.png)

# Cross-platform layout using JSS

One of the challenges with creating cross platform layouts is that each type of platform might require some level of tweaking if you want to have unique interfaces. 

Titanium offers a capability called "JSS" which standards for JavaScript Stylesheets. It is modeled directly from CSS (Cascading Stylesheets) and supports almost identical properties. 

To use JSS, you'll need to create a file with the extension `.jss` and the same name as the URL-based Window.

<warning>
    The JSS functionality is introduced in 1.5. If you are using a version prior to 1.5, this will not work.
</warning>

For example, suppose you wanted to create a set of styles for `app.js`. You would create a file named `app.jss`.

JSS support ID-based styles, class-based styles and type-based styles.

In the following example, we'll setup the application logic.

<code class="javascript">
    var window = Ti.UI.createWindow({
        id:"w"
    });
    var button = Ti.UI.createButton({
        id:"b",
        title:"Hello"
    });
    window.add(button);
    window.open();
</code>

Now, we can specify the user interface styles separately using JSS:

<code class="css">
    #w {
        background-color:"red";
    }
    button {
        width:100px;
        height:40px;
    }
</code>

In the above JSS, we're using both an ID selector and a class-based selector. Also notice that we're specifying both properties inline (the `title` property of the button) in addition to the JSS.  Properties that are specified in the object constructor override any properties specified in JSS.

## Specifying Global Styles

You can specify global styles by specifying a JSS file named `global.jss`.  All styles provided in this file take effect on all Windows.  Any properties provided in a Window-specific JSS file, however, take precedence over global properties.


# Platform specific UI details

Titanium attempts to reduce as much of the differences between each platform but this is an ever increasing task and something that can be a work in progress.  Sometimes platforms provide unique UI capabilities and we need to support them.

## iOS Retina display

The iOS platform starting in 4.0 supports a high-resolution, ["Retina" display](http://www.apple.com/iphone/features/retina-display.html). The iPhone device with Retina display has a 640x960 pixels instead of 320x480.

To specify images that take advantage of the Retina display, you must specify images that take advantage of the larger pixel dimensions. You can read more about the technical details in the [iOS Application Programming Guide](http://developer.apple.com/library/ios/#documentation/iphone/conceptual/iphoneosprogrammingguide/SupportingResolutionIndependence/SupportingResolutionIndependence.html).

To use the Retina display image, you'll need to name the image with the `@2x.png` suffix.  For example, `foo@2x.png`.  If you'd like to provide a low resolution image, you'd specify an additional file named `foo.png`.  Titanium will transparently use the appropriate image file based on the appropriate display pixels.  

## iOS Custom Fonts

The iOS platform supports custom fonts which must be embedded in your application `Resources` folder.

To specify one or more custom fonts, you must use a custom `Info.plist` file. To use a custom `Info.plist`, copy the `Info.plist` from the `build/iphone` folder. If this folder does not exist, run your application in the simulator once and it should be created automatically. You'll want to copy the `Info.plist` file into the root directory of your project (at the same level as `tiapp.xml`).

Add the following XML at the end of the `Info.plist` file. You should edit the file in a text editor. The `<string>` value should contain the name of the font file you copied into your `Resources` directory.  

<warning>
    Be careful when editing. If the changes are not valid XML, your application will fail to compile.
</warning>

<code class="xml">
    <key>UIAppFonts</key>
	<array>
		<string>comic_zine_ot.otf</string>
	</array>
</code>

To reference your font, you use the `fontFamily` property of the `font` property object.

<warning>
    You must use the name of the font as display in Font Book - which likely will be different than the name of the file.
</warning>

For example:

<code class="javascript">
    var window = Ti.UI.createWindow({
    	backgroundColor:"white"
    });
    var label = Ti.UI.createLabel({
    	text:"Appcelerator\nFTW!",
    	font:{fontSize:54,fontFamily:"Comic Zine OT"},
    	width:"auto",
    	textAlign:"center"
    });
    window.add(label);
    window.open();
</code>

You should see the following:

![customfont](http://img.skitch.com/20101025-xnf6wihhdaksx4s944x9yqj9gq.png)

<warning>
    Be careful about the licensing of your custom font.  You must use a license that provides you with the ability to redistribute the font in your application.
</warning>

