# Intro
Personal website with blog and portfolio

# Framework
Django for the admin interface that allows easy posting

# Front End
- Built using Bootstrap 3 native for the built-in responsive features
- Jinja2 templates

# Javascript
- map.js loads leaflet map using ES6 features
- turnsignal.min.js is mostly auto generated geometry description for webgl 
model
- Three.js used to create interactive 3d models
- leaflet.js is used to create interactive map

# Media
- Konsole_icon.svg is LGPL 2.1 or later licensed retrieved from wikimedia
- GEARS.svg is CC0 1.0 licensed retrieved from wikimedia
- Github, Linkedin and OpenStreetMap logos used within respective guidelines
- all other images are personal and CC BY-SA 4.0 licensed

# Hosting
- Running on shared host with apache proxy setup to serve static files
- Gunicorn with async workers handles serverside rendering
