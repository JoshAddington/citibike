
d3.json("/api/map_json", function(collection) {


    var feature = g.selectAll('path')
        .data(collection.features)
        .enter().append('path');

    map.on('viewreset', reset);
    reset();

    // fit the SVG element to leaflet's map layer
    function reset() {

        bounds = path.bounds(collection);

        var topLeft = bounds[0],
        bottomRight = bounds[1];

        svg .attr("width", bottomRight[0] - topLeft[0])
            .attr("height", bottomRight[1] - topLeft[1])
            .style("left", topLeft[0] + "px")
            .style("top", topLeft[1] + "px");

        g .attr("transform", "translate(" + -topLeft[0] + ","
                                     + -topLeft[1] + ")");

        // initialize the path data
        feature.attr("d", path)
            .attr('stroke', 'grey')
            .attr('fill','none');
  }

    // Use Leaflet to implement a D3 geometric transformation.
  var projectPoint = function(x, y) {
    var point = map.latLngToLayerPoint(new L.LatLng(y, x));
    this.stream.point(point.x, point.y);
  }
});
