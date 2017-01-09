#!/usr/bin/env bash
source  venv/bin/activate
pip install -r requirements.txt -t lib
pip install -r requirements.txt
dart --out=game/static/dart.js game/dart/main.dart
compass compile
deactivate
