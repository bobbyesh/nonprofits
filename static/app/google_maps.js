/**
 * Created by bobby on 4/25/17.
 */

function initMap() {
    var latlng = {lat: 45, lng: -122}; // Portland coordinates
    var mapOptions = {
        zoom: 6,
        center: latlng
    };

    var map = new google.maps.Map(document.getElementById('map'), mapOptions);
    create_markers(map);
}

function create_markers(map) {
    for (var i = 0; i < organizationData.length - 1; i++) {
        const info = organizationData[i].info;
        const marker = new google.maps.Marker({
            map: map,
            position: organizationData[i].latLng,
        });
        const infowindow = new google.maps.InfoWindow({
            content: info
        });
        marker.addListener('click', function () {
            infowindow.open(map, marker);
        })
    }
}