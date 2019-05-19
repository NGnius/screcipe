#!/bin/bash
# install required dependencies available from pip repos
pip3 install -q -r requirements.txt
# install dependencies for GCP App Engine deployment not available from pip repos
# pip3 install -q -t libs ./lib/recipe_scrapers
