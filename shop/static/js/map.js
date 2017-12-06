function initMap() {
        var uluru = {lat: 52.230266, lng: 21.0026791};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: uluru
        });
        var contentString = '<strong>.Buy</strong><br>Warszawa, Złote Tarasy<br>';

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

