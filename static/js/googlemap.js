"use strict";
var image = 'http://www.googlemapsmarkers.com/v1/1CE9B6';
// var user = 'http://maps.google.com/mapfiles/dd-start.png';


// function init(){
//     var mapDiv = document.getElementById("map");
//     var mapOptions= {
//         center: new google.maps.LatLng(37.757189, -122.335684),
//         zoom: 10,
//         mapTypeId: google.maps.MapTypeId.ROADMAP
//     };
//     var map = new google.maps.Map(mapDiv, mapOptions);

//     var infoWindow = new google.maps.InfoWindow({map: map});

function initMap() {
        var center = {lat: 37.789527, lng: -122.394276};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: center,
          scrollwheel: false,
          mapTypeControl: false,
        });
        var marker = new google.maps.Marker({
          position: center,
          map: map,
          icon: image,
          title:"Google Launch Pad",
        });
      }








