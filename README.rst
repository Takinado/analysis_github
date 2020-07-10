.. raw:: html
    <h1>GitHub repository analysis</h1>
    <p>The script analyzes the repository using the GitHub REST API. Analysis results output to stdout.</p>
    <p align="center">
      <a href="https://travis-ci.org/Takinado/analysis_github">
        <img src="https://travis-ci.org/Takinado/analysis_github.svg?branch=master" alt="Build Status">
      </a>
    </p>


Usage
=============

usage: analysis.py [-h] [-s SINCE] [-u UNTIL] [-b BRANCH] [-t TOKEN] repository

positional arguments:
  repository            Full path to repository (https://github.com/...)

optional arguments:
  -h, --help            show this help message and exit
  -s SINCE, --since SINCE
                        Only data after this date will be analyze. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
  -u UNTIL, --until UNTIL
                        Only data before this date will be analyze. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
  -b BRANCH, --branch BRANCH
                        Repository branch. Default: master
  -t TOKEN, --token TOKEN
                        GitHub OAuth2 token (use to increase rate limit)



CI/CD
======================
GitHub, Travis-CI, Heroku
On Heroku deploy Django (for example).
Run script by django-cron, django-chroniker, or Celery.
Write results to the database.

If we need we can create a simple form to run the script with different parameters.


How to run
=======================

.. code-block:: bash

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ python analysis_git/analysis.py <repository>
