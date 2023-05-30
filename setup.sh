#!/usr/bin/env bash

# requirements
pip install --upgrade pip
pip install -U pip setuptools wheel
python3 -m pip install -r requirements.txt
python -m spacy download da_core_news_sm