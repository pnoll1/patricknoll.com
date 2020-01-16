# Intro
Personal website with blog, portfolio, members only section and stripe checkout for payment.

# Django
- Used for the admin interface that allows easy posting
- home and downloads are seperate apps to increase reusability
- ORM used for portability and ease of use
- django-markdownx used to parse markdown for blog posts
  
# Front End
- Built using Bootstrap 3 native for the built-in responsive features
- Jinja2 templates
  - template inheritance used to implement DRY

# Maps
- Leaflet.js with Mapbox tiles and geojson data loaded using fetch
- Visualizing OpenStreetMap Edits post uses mapbox streets style for a traditional map appearance
- downloads-ad uses light style to give enough info to orient user without getting in the way of the data
  - county data downloaded using overpass, processed using osmium then converted to geojson using ogr2ogr

# 3D Model
- Three.js used to render interactive 3d model
- turnsignal.min.js is mostly auto generated from a Freecad 3d model

# Media
- Konsole_icon.svg is LGPL 2.1 or later licensed retrieved from wikimedia
- GEARS.svg is CC0 1.0 licensed retrieved from wikimedia
- Github, Linkedin and OpenStreetMap logos used within respective guidelines
- all other images are personal and CC BY-SA 4.0 licensed

# Ops
- Running on Debian VPS
- postgresql database
- apache proxy setup to serve static files that don't need auth
- mod_wsgi runs python
- tls setup using certbot
