#!/bin/sh


cd $(dirname ${0})

#PYTHONPATH=$(shell cwd)
#export PYTHONPATH

#python -m unittest discover
exec python -m unittest tests.test_css
