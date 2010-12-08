<summary>
    The following tutorial will show how to create a tooltip on the iOs environment.
</summary>

#Introduction

In our applications we have to try to make the user's experience as smooth as possible. 

In some cases, due the space restrictions we cannot add enough visual information to transmit our intentions. 

One case could be a button with an icon only that might be hard for the user to understand what it's supposed to do. In this case we could use a tooltip to signal the user the button's function.

Below is an example on how this could look:

![tooltip titanium example ](http://farm6.static.flickr.com/5085/5244120022_6a390dc44b.jpg "The tooltip example")


#Building the tooltip

To simplify the code we will consider we already have the interface elements (we need a window named **index_view** and a button named **tipButton**).

The tooltip is a simple view with the tip image set as background:

![tooltip background](http://cssgallery.info/wp-content/uploads/2010/04/bubble.png "The tooltip view background")

And it's created using the code below:

~~~
var tipView =  Titanium.UI.createView({
	width:205,
	height:57,
	backgroundImage:"bubble.png",
	top:0,
	right:3
});
~~~


The “Continue reading” is a simple label added to this view

~~~
var tipLabel =  Titanium.UI.createLabel({
	text:'Continue reading',
	color:'#fff',
	width:205,
	height:34,
	top:16,
	font:{
	fontFamily:'Helvetica Neue',
		fontSize:13,
		fontWeight:'bold'
	},
	textAlign:'center'
});
 
tipView.add(tipLabel);
~~~

And finally we add the tooltip to the **index_win**:

~~~
index_win.add(tipView);
~~~

Now when we open the **index_win** the tooltip will be there and the user will have a visual clue on what the **tipButton** does.


#More on user experience

If the tooltip stays there permanently will obstruct the below views or at least will become annoying so we need to find a way to hide it. 

We can do this when the user clicks the **tipButton** by using a smooth fadeout.

The code below creates an animation that operates on the **opacity** property of the **tipView** (so the whole tooltip) and that is triggered on the click event of the **tipButton**.

~~~
var anim_out = Titanium.UI.createAnimation();
	anim_out.opacity=0;
	anim_out.duration = 250;
});
 
tipButton.addEventListener('click', function() {
	tipView.animate(anim_out);
});
~~~



