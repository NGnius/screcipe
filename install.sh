#!/bin/bash
# setup in case this is the first run
pip3 install -q --user -r ./lib/recipe_scrapers/requirements.txt
pip3 install -q --user ./lib/recipe_scrapers
pip3 install -q --user -r requirements.txt

# run
# python3 main.py
