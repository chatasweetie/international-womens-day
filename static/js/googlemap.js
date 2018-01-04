"use strict";
var image = 'http://maps.google.com/mapfiles/marker_purple.png';
var user = 'http://maps.google.com/mapfiles/dd-start.png';


function init(){
    var mapDiv = document.getElementById("map");
    var mapOptions= {
        center: new google.maps.LatLng(37.757189, -122.335684),
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(mapDiv, mapOptions);

    var infoWindow = new google.maps.InfoWindow({map: map});