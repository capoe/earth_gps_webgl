

## Modify the code to load your own GPS data

Edit index.html and look for the following XML HTTP request:

```javascript
requestLoadData(
    'data/cook_journey_1772-1775.json',
    setupLocations,
    { tag: 'gps-cook', color_0: 0x0066ff, color_1: 0xffffff },
    null);
```

Simply substitue 'data/...json' with your own GPS trajectories (make sure to match the file format).

## Data sources

Earth elevation data from earthobservatory.nasa.gov
The KML raw data is taken from "Digital Archives and Pacific Cultures" (pacific.obdurodon.org)
