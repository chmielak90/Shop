function initMap() {
        var uluru = {lat: 52.2308984, lng: 20.98838909999995};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: uluru
        });
        var contentString = '<strong>CodersLab</strong><br>warszawa, prosta 51<br>';

        var infowindow = new google.maps.InfoWindow({
          content: contentString
        });

        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
        marker.addListener('click', function() {
          infowindow.open(map, marker);
        });
        infowindow.open(map,marker);

      }

