document.getElementById('map').classList.add('map');
var baselayers, ways, nodes, controls_layers, mymap, overlays, mapbox, featureCount;

var mapbox = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    tileSize: 512,
    minZoom: 8,
    maxZoom: 18,
    zoomOffset: -1,
    id: 'mapbox/streets-v11',
    accessToken: 'pk.eyJ1IjoicG5vbGwiLCJhIjoiY2pkNDNyNmtzMHRtOTMzcWZ0Y2szdzh3eCJ9.g8tszbsYH0bVCcj7v8RAEQ'
});
var baselayers = {
    "Mapbox": mapbox
}
var mymap = L.map('map', {
    center: [47.810, -122.384],
    zoom: 9,
    layers: [mapbox]
});

fetch('edits')
.then( res => res.json())
.then(data => {
  var ways = L.geoJSON(data,{
  style: function (feature) {
      return {};
  }
  ,
  pointToLayer: function (feature) {
    return false;
  }
  });
  var nodes = L.geoJSON(data,{
  style: function (feature) {
      return {stroke:false,fill:false};
  }
  });
  ways.addTo(mymap);
  var markers = L.markerClusterGroup({disableClusteringAtZoom: 17});
  markers.addLayer(nodes);
  mymap.addLayer(markers);

  var overlays = {
  "markers": markers,
  "ways": ways,
  };
  featureCount = data.features.length.toString();
  var controls_layers = L.control.layers(baselayers, overlays);
  controls_layers.addTo(mymap);
  legend.addTo(mymap);
  counter.addTo(mymap);
})
.catch();

var legend = L.control({position: 'bottomright'});
legend.onAdd = function (mymap) {
    var div = L.DomUtil.create('div', 'legend');
    div.innerHTML = 'OSM Last Touched Edits';
    return div;
};

var counter = L.control({position: 'bottomright'});
counter.onAdd = function(mymap) {
    var divCounter = L.DomUtil.create('div', 'counter');
    divCounter.innerHTML = 'Features: '+featureCount;
    return divCounter;
};
