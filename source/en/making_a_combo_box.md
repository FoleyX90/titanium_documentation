<summary>
	This tutorial explains how to emulate a combo-box (a field that accepts free text as input or selectable from a list) on iOs.
</summary>
#Before we start 

The below video shows what we will obtain at the end of this tutorial.


<object width="600" height="385"><param name="movie" value="http://www.youtube.com/v/2H-w_hUQtPw?fs=1&amp;hl=en_US&amp;rel=0"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/2H-w_hUQtPw?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="600" height="385"></embed></object>

#Ok, what do we need for this iPhone combo-box ?

First of all we need a **textField** to accept input from the user. Titanium lets you set the leftButton and rightButton for this textField while constructing it. So we will take advantage of this and create a textField as it follows:
~~~
var my_combo = Titanium.UI.createTextField({
	hintText:"write your name or select one",
	height:40,
	width:300,
	top:20,
	borderStyle:Titanium.UI.INPUT_BORDERSTYLE_ROUNDED
});
~~~
Nothing special, a regular **textField** with a hint for the user that will disappear when the textField has a value.

Now we need to create the rightButton for it.

We will use a system button provided by Apple (**Titanium.UI.iPhone.SystemButton.DISCLOSURE**) only that we will rotate it 90 degrees to server our purpose. This is the code that creates the rightButton and the transformation applied to it.

~~~
var tr = Titanium.UI.create2DMatrix();
tr = tr.rotate(90);
var drop_button =  Titanium.UI.createButton({
	style:Titanium.UI.iPhone.SystemButton.DISCLOSURE,
	transform:tr
});
~~~ 

Now that we have the rightButton as we need it, the textField constructor becomes:
~~~ 

var my_combo = Titanium.UI.createTextField({
	hintText:"write your name or select one",
	height:40,
	width:300,
	top:20,
	borderStyle:Titanium.UI.INPUT_BORDERSTYLE_ROUNDED,
	rightButton:drop_button,
	rightButtonMode:Titanium.UI.INPUT_BUTTONMODE_ALWAYS
});
~~~ 

Please note the **rightButtonMode:Titanium.UI.INPUT_BUTTONMODE_ALWAYS** declaration, it makes this button visible all the time.

This is how it looks:

![textField with right button](http://farm6.static.flickr.com/5042/5210992121_3569d52338.jpg "The textField with right button set")

Pretty sexy, isn’t it? Well we’re not done yet.

#Building the modal picker

When the user focuses on the **textField**, the keyboard appears – so we will have to build our picker to emulate the same behavior and to maximize the usability of our form. For this we will need a **Picker** and two **buttons: Done and Cancel**. These two buttons will be positioned in a **Toolbar**, again, to emulate as good as possible the keyboard behavior.

Let’s build everything:
~~~
var picker_view = Titanium.UI.createView({
	height:251,
	bottom:0
});
 
var cancel =  Titanium.UI.createButton({
	title:'Cancel',
	style:Titanium.UI.iPhone.SystemButtonStyle.BORDERED
});
 
var done =  Titanium.UI.createButton({
	title:'Done',
	style:Titanium.UI.iPhone.SystemButtonStyle.DONE
});
 
var spacer =  Titanium.UI.createButton({
	systemButton:Titanium.UI.iPhone.SystemButton.FLEXIBLE_SPACE
});
 
var toolbar =  Titanium.UI.createToolbar({
	top:0,
	items:[cancel,spacer,done]
});
 
var picker = Titanium.UI.createPicker({
	top:43
});
picker.selectionIndicator=true;
 
var picker_data = [
	Titanium.UI.createPickerRow({title:'John'}),
	Titanium.UI.createPickerRow({title:'Alex'}),
	Titanium.UI.createPickerRow({title:'Marie'}),
	Titanium.UI.createPickerRow({title:'Eva'}),
	Titanium.UI.createPickerRow({title:'James'})
];
 
picker.add(picker_data);
 
picker_view.add(toolbar);
picker_view.add(picker);
~~~

The code is a little long but is not rocket science. Some stuff to talk about though:

Everything is wrapped inside a view – **picker_view** – because we will have to animate like the keyboard does, so it’s faster to animate one element only.
The height of picker_view is the height of the toolbar (43px) + the height of the picker (208px). How do I know this? I just used a ruler 
The combo-box interface looks like this:

![Titanium combo-box](http://farm5.static.flickr.com/4153/5210992051_21fc6bebb6.jpg "Titanium combo-box")

#Creating the picker animation

We also need to create 2 animations: *slide_in* and *slide_out*. We will animate the bottom property of the picker_view. We will need to start with the picker_view off the screen, so we will build it with:
~~~
bottom:-251
~~~
instead of 0 as it was initially.
~~~
var slide_in =  Titanium.UI.createAnimation({bottom:0});
var slide_out =  Titanium.UI.createAnimation({bottom:-251});
~~~

The logic behind the animations is this:

The user focuses the textField – the keyboard appears ( it’s done by the OS , no worries here) and if the picker_view is visible we need to hide it.
The user clicks the rightButton – we need to hide the keyboard and show the picker_view.
Here is the code:

~~~
my_combo.addEventListener('focus', function() {
	picker_view.animate(slide_out);
});
 
drop_button.addEventListener('click',function() {
	picker_view.animate(slide_in);
	my_combo.blur();
});
 
cancel.addEventListener('click',function() {
	picker_view.animate(slide_out);
});
~~~
I also added the click event on the cancel button to hide the picker_view.

#Filling the textField with the picker’s value

The only thing we have left is to actually put the value of the picker in the my_combo textField when the user clicks the done button and hide the picker_view.
~~~
done.addEventListener('click',function() {
	my_combo.value =  picker.getSelectedRow(0).title;
	picker_view.animate(slide_out);
});
~~~

The **getSelectedRow** method of the picker is returning the selected row, and we use its title. The getSelectedRow argument is the index of the columns in the picker, and since we have only one, this is 0.

#Download the project

The Resource folder of the project can be [downloaded from here](http://cssgallery.info/wp-content/combobox_tutorial.zip).

