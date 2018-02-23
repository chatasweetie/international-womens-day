# International Women's Day 2018

Backend: [Flask](http://flask.pocoo.org/)
Frontend: [Bootstrap v4](http://getbootstrap.com/)
Hosting: [Google App Engine](https://cloud.google.com/appengine/)


## Table of Contents

- [Development](#development)
- [Build](#build)
- [Folder Structure](#folder-structure)

## Folder Structure

```
international-womens-day/
  README.md
  app.yaml (google app engine configuration)
  appengine_config.py (for google app engine)
  lib/ (for google app engine)
  requirements.txt
  main.py (server)
  static/
      css/
          styling.css
      imgs/
          assests/
          sponors/
          favicorn
  templates/
      base.html
      homepage.html
```

## Create Environment

Create and enter an isolated Python environment using virtualenv:
```
    virtualenv env
    source env/bin/activate
```

Install dependencies using pip:
```
    pip install -t lib -r requirements.txt
```


## Development
In the project directory, you can run:

```
FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run
```

## Build
To deploy to production simply follow these steps:

```
dev_appserver.py app.yaml
gcloud app deploy
```


Project site: [IWD site](www.iwd-sf.org)

## Contributors
[Jessica Dene Earley-Cha](https://www.linkedin.com/in/jessicaearley/), 
[Queenie Ho](https://www.linkedin.com/in/queenieho), 
[Andres Pineda](https://www.linkedin.com/in/humbamp123)

## License
MIT
