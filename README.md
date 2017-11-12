# International Women's Day

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
1. Create and enter an isolated Python environment using virtualenv:
    ``virtualenv env ``
    ``source env/bin/activate``
2. Install dependencies using pip:
    ``pip install -t lib -r requirements.txt``


## Development
In the project directory, you can run:

```
python main.py
```

## Build
To deploy to production simply follow these steps:

```
dev_appserver.py app.yaml
gcloud app deploy
```


Project site: [IWD site](https://watchful-force-155207.appspot.com)

## Contributors
[Jessica Dene Earley-Cha](https://www.linkedin.com/in/jessicaearley/)

## License
MIT