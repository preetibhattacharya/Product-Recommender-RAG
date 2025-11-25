#!/usr/bin/env bash

# Upgrade pip, setuptools, and wheel first
python -m pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt
