### Modify the code to load your own GPS data

Edit index.html and look for the following XML HTTP request.

```javascript
requestLoadData(
    'data/cook_journey_1772-1775.json',
    setupLocations,
    { tag: 'gps-cook', color_0: 0x0066ff, color_1: 0xffffff },
    null);
```

Simply substitue 'data/...json' with your own GPS trajectories (but make sure to match the file format).

### Requirements

Note that these scripts will run only on machines with graphics cards that support WebGL
(this probably excludes most Android devices unfortunately).

### Data sources

* Earth elevation data from earthobservatory.nasa.gov

* The KML raw data for James Cook's travels are taken from "Digital Archives and Pacific Cultures" (pacific.obdurodon.org)

* The orbital controls and some other three.js convenience functions are (minor modifications aside) taken from the three.js website.
