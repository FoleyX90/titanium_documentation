<summary>
This guide will assist you in leveraging the location services available on your device.  By the end of this
guide, you will understand:

* How to get the device's current location
* How to continually monitor the device's location
* How to convert location to addresses an vice versa
* How to use the device's compass
* How to leverage native maps

</summary>

# Location Services

Titanium provides a simple proxy layer wrapped around the location services of your device.
The application code can ask if the location service is enabled with the property `Ti.Geolocation.locationServicesEnabled`

# Geolocation

In [Titanium Geolocation module](http://developer.appcelerator.com/apidoc/mobile/latest/Ti.Geolocation-module) are grouped all features needed to explot the location services.

## Current position

`Ti.Geolocation.getCurrentPosition` method is used to know the current position of the device.

<code class="javascript">
	var window= Ti.UI.createWindow();
	Ti.Geolocation.purpose = "Sample";
	Ti.Geolocation.getCurrentPosition(function(e) {
				if (e.error) {
					Ti.API.error('geo - current position' + e.error);
					return;
				}
				 var latitude = e.coords.latitude; 
				 var longitude = e.coords.longitude; 
				 var altitude = e.coords.altitude; 
				 var accuracy = e.coords.accuracy; 
				 var altitudeAccuracy = e.coords.altitudeAccuracy; 
				 var heading = e.coords.heading; 
				 var speed = e.coords.speed; 
				 var timestamp = e.coords.timestamp;
	 
				 Ti.API.info('geo - current position');
				 Ti.API.info(' - latitude: ' + latitude); 
				 Ti.API.info(' - longitude: ' + longitude); 
				 Ti.API.info(' - altitude: ' + altitude); 
				 Ti.API.info(' - accuracy: ' + accuracy); 
				 Ti.API.info(' - altitudeAccuracy: ' + altitudeAccuracy); 
				 Ti.API.info(' - heading: ' + heading); 
				 Ti.API.info(' - speed: ' + speed); 
				 Ti.API.info(' - timestamp: ' + timestamp);
			});

	window.open();     
</code>

The response contains all location informations that the device retrieves.

## Monitor position
In quite similar way, it's possible register to be notified when the location changes:

<code class="javascript">
	var window= Ti.UI.createWindow();
	Ti.Geolocation.purpose = "Sample";
	Ti.Geolocation.addEventListener('location', function(e) {
				if (e.error) {
					Ti.API.error('geo - position' + e.error);
					return;
				}
				 var latitude = e.coords.latitude; 
				 var longitude = e.coords.longitude; 
				 var altitude = e.coords.altitude; 
				 var accuracy = e.coords.accuracy; 
				 var altitudeAccuracy = e.coords.altitudeAccuracy; 
				 var heading = e.coords.heading; 
				 var speed = e.coords.speed; 
				 var timestamp = e.coords.timestamp;
	 
				 Ti.API.info('geo - position');
				 Ti.API.info(' - latitude: ' + latitude); 
				 Ti.API.info(' - longitude: ' + longitude); 
				 Ti.API.info(' - altitude: ' + altitude); 
				 Ti.API.info(' - accuracy: ' + accuracy); 
				 Ti.API.info(' - altitudeAccuracy: ' + altitudeAccuracy); 
				 Ti.API.info(' - heading: ' + heading); 
				 Ti.API.info(' - speed: ' + speed); 
				 Ti.API.info(' - timestamp: ' + timestamp);
			});

	window.open();
</code>

## Forward and reverse geocoding

A couple of useful methods are provided to translate from address to coordinates (`Ti.Geolocation.forwardGeocoder`) and from coordinates to address (`Ti.Geolocation.reverseGeocoder`); both are asynchronous methods requiring a callback function to process the response as argument.
The following example shows a simple use of both of them.

<code class="javascript">
	var window= Ti.UI.createWindow();
	window.backgroundColor = '#fff';

	var addr = "2065 Hamilton Avenue San Jose California 95125";
	var forwardGeoLabel = Ti.UI.createLabel({
		text:'Forward Geo (Addr->Coords): ' + addr,
		font:{fontSize:12, fontWeight:'bold'},
		color:'#111',
		top:0,
		left:10,
		height:15,
		width:300
	});
	window.add(forwardGeoLabel);

	var forwardGeo = Ti.UI.createLabel({
		text:'',
		font:{fontSize:11},
		color:'#444',
		top:20,
		left:10,
		height:15,
		width:300
	});
	window.add(forwardGeo);

	var latitude = 37.294511;
	var longitude = -121.922107;
	var reverseGeoLabel = Ti.UI.createLabel({
		text:'Reverse Geo (Coords->Addr):' + latitude + ', ' + longitude,
		font:{fontSize:12, fontWeight:'bold'},
		color:'#111',
		top:50,
		left:10,
		height:15,
		width:300
	});
	window.add(reverseGeoLabel);

	var reverseGeo = Ti.UI.createLabel({
		text:'',
		font:{fontSize:11},
		color:'#444',
		top:70,
		left:10,
		height:15,
		width:300
	});
	window.add(reverseGeo);

	Ti.Geolocation.forwardGeocoder(addr,function(evt) {
		forwardGeo.text = "lat:"+evt.latitude+", long:"+evt.longitude;
	});

	Ti.Geolocation.reverseGeocoder(latitude,longitude,function(evt) {
		var places = evt.places;
		reverseGeo.text = places[0].address;
		Ti.API.debug("reverse geolocation result = "+JSON.stringify(evt));
	});

	window.open();            
</code>

This is how is shown on iPhone:
![Geolocation on iPhone](http://img.skitch.com/20101209-8uirkadjnmisnjakpwxxubc7x8.png)

and on Android
![Geolocation on Android](http://img.skitch.com/20101209-nnqa5d7bw4u476uf5nam1nk6u4.png)


# Compass

Following the location philosophy, the compass is handled through a couple of asynchronuous methods.
The `Ti.Geolocation.hasCompass` is used to know if the device has a compass or not.

## Current Heading

A `heading` event contais all the needed informations to know how the device is oriented.

<code class="javascript">
	var window= Ti.UI.createWindow();
	Ti.Geolocation.purpose = "Sample";
	if (Ti.Geolocation.hasCompass) {   
		Ti.Geolocation.getCurrentHeading(function(e) {
					if (e.error) {
						currentHeading.text = 'error: ' + e.error;
						return;
					}
					var x = e.heading.x;
					var y = e.heading.y;
					var z = e.heading.z;
					var magneticHeading = e.heading.magneticHeading;
					var accuracy = e.heading.accuracy;
					var trueHeading = e.heading.trueHeading;
					var timestamp = e.heading.timestamp;
		 
					Ti.API.info('geo - current heading: ' + trueHeading);
				});
		} else {
			Ti.API.info("No Compass on device");
		}

	window.open();            
</code>

## Monitor Heading

A `heading` event must be observed to follow the compass changes.

<code class="javascript">
	var window= Ti.UI.createWindow();
	Ti.Geolocation.purpose = "Sample";
	if (Ti.Geolocation.hasCompass) {   
		Ti.Geolocation.addEventListener('heading',function(e) {
				if (e.error) {
					Ti.API.info("error: " + e.error);
					return;
				}
	 
				var x = e.heading.x;
				var y = e.heading.y;
				var z = e.heading.z;
				var magneticHeading = e.heading.magneticHeading;
				var accuracy = e.heading.accuracy;
				var trueHeading = e.heading.trueHeading;
				var timestamp = e.heading.timestamp;
	 
				Ti.API.info('geo - heading updated: ' + trueHeading);
			});
	
   	} else {
			Ti.API.info("No Compass on device");
	}

	window.open();            
</code>

# Native Maps

<note>
	To run map applications on Android emulator, a `API` Sdk must be choose to avoid `requires unavailable shared library com.google.android.maps` error.

	Moreover a [Google Map key](http://developer.appcelerator.com/doc/mobile/android-maps) have to be added to `tiapp.xml`

<code class="xml">
	<property name="ti.android.google.map.api.key.development">0ZnKXkWA2dIAu2EM-OV4ZD2lJY3sEWE5TSgjJNg</property>
	<property name="ti.android.google.map.api.key.production">GET_ME_FROM_GOOGLE</property>
</code>
</note>

## Displaying a map
You can add a map to a window using the creator `Ti.Map.createView`.
A comprehnsive list of proterties and methods are documented in [Ti.Map](http://developer.appcelerator.com/apidoc/mobile/latest/Ti.Map-module);

<code class="javascript">
    var window = Ti.UI.createWindow();
	var mapView = Ti.Map.createView({
		mapType: Ti.Map.STANDARD_TYPE,
		region:{latitude:33.74511, longitude:-84.38993, latitudeDelta:0.5, longitudeDelta:0.5},
		animate:true,
		regionFit:true,
		userLocation:true
	});
     
    window.add(mapView);
    window.open();
</code>

The `mapType` attribute defines the rendering type; allowed values are:
* Ti.Map.STANDARD_TYPE
* Ti.Map.SATELLITE_TYPE
* Ti.Map.HYBRID_TYPE

The `region` attribute defines the center of viewport using latitude and longitude values and its size as delta of latitude and longitude (a latitude degree is about 111 Km, a longitude degree depends on the distance from equator.).

`userLocation` enable the representation of current position on map, as a blue bullet point.

The previous example as shown on iPhone:
![MapView on iPhone](http://img.skitch.com/20101209-81j4bg8upgr2ee3cr9dkmix94k.png)

and on Android:
![MapView on Android](http://img.skitch.com/20101209-dm93kp5ymm2faxmkgbtej7ye.png)

## Changing a map's viewable area

As shown before, a region attribute defines the viewport of a map at creation time; this area can be changed at runtime.
For instance, the following code add a button that changes the viewable area when pressed:

<code class="javascript">
    var window = Ti.UI.createWindow();
	var mapView = Ti.Map.createView({
		mapType: Ti.Map.STANDARD_TYPE,
		region:{latitude:33.74511, longitude:-84.38993, latitudeDelta:0.5, longitudeDelta:0.5},
		animate:true,
		regionFit:true,
		userLocation:true
	});

	var button = Ti.UI.createButton({
		title: "Change",
		width: 100,
		height: 40,
		bottom: 0
	});
	button.addEventListener('click', function() {
		mapView.setLocation(
		 {
		 	latitude:37.337681,
			longitude:-122.038193,
			animate:true,
			latitudeDelta:0.04, 
			longitudeDelta:0.04
		  }
		);
	});
     
    window.add(mapView);
    window.add(button);
    window.open();  
</code>

## Drawing annotations

An annotation is created with `Ti.Map.createAnnotation method`, and can be customized in every part, pin image, color, callout etc.
An annotation can be added at creation time with array attribute `annotations` in `MapView`, or at runtime calling `addAnnotation` method on `MapView`.

<code class="javascript">
    var window = Ti.UI.createWindow();
	var apple = Ti.Map.createAnnotation({
		latitude:37.33168900,
		longitude:-122.03073100,
		title:"Apple HQ",
		subtitle:'Cupertino, CA',
		pincolor:Ti.Map.ANNOTATION_GREEN,
		animate:true,
		rightButton: 'images/apple_logo.jpg'
	}); 
	var mapView = Ti.Map.createView({
		mapType: Ti.Map.STANDARD_TYPE,
		region:{latitude:33.74511, longitude:-84.38993, latitudeDelta:30, longitudeDelta:30},
		animate:true,
		regionFit:true,
		userLocation:true,
		annotations:[apple]
	}); 

    window.add(mapView);
    window.open();  
</code>   

As shown on iPhone:
![Annotation on iPhone](http://img.skitch.com/20101209-r7e82j9dp45kgj43dd4jiddxpi.png)

and on Android:
![Annotation on Android](http://img.skitch.com/20101209-ciickp43ykkt4qup55dcau79a7.png)

## Drawing routes
<note>
	Currently supported on iPhone only.
</note>

In order to draw a route an a `Mapview`, a set of points should be provided to build a `route` object, that can be added to a map view with `addRoute` method.

For example, given a csv file of points:

<code class="javascript">
	42.33677,-71.126046
	42.336845,-71.126239
	42.336953,-71.12639
	42.337103,-71.12654
	...
</code>   

and this code:
<code class="javascript">
	var window= Ti.UI.createWindow();

	var boston = {latitude:42.334537,longitude:-71.170101,latitudeDelta:0.010, longitudeDelta:0.018};
	var mapview = Ti.Map.createView({
		mapType: Ti.Map.STANDARD_TYPE,
		region: boston,
		animate:true,
		regionFit:true,
		userLocation:true
	});

	// read in our routes from a comma-separated file
	var f = Ti.Filesystem.getFile(Ti.Filesystem.resourcesDirectory,'','route.csv');
	var csv = f.read();
	var points = [];
	var lines = csv.toString().split("\n");
	for (var c=0;c<lines.length;c++) {
		var line = lines[c];
		var latlong = line.split(",");
		if (latlong.length > 1) {
			var lat = latlong[0];
			var lon = latlong[1];
			var entry = {latitude:lat,longitude:lon};
			points[c]=entry;
		}
	}

	var route = {
		name:"boston",
		points:points,
		color:"red",
		width:4
	};

	// add a route
	mapview.addRoute(route);
	window.add(mapview);

	window.open();
</code>   

A route will by drawn.
![Map with route](http://img.skitch.com/20101209-fe3ry5f6fuyai47fdikh66kb7n.png)

