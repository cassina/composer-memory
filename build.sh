#!/usr/bin/env bash
source  venv/bin/activate
pip install -r requirements.txt -t lib
pip install -r requirements.txt
bower install
compass compile
deactivate
bash devserver.sh
