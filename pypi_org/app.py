"""Define demo Flask app."""
import os
import sys

import flask

# The following two line make this work if not installed as a module.
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from pypi_org.views import home_views
from pypi_org.views import package_views
from pypi_org.views import cms_views

app = flask.Flask('pypi_org')


def main():
    """Set up and run the web app."""
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    """Register blueprints for all of the views."""
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    main()
