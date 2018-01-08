"use strict";
var image = 'http://www.googlemapsmarkers.com/v1/1CE9B6';

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








