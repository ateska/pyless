#!/bin/sh


cd $(dirname ${0})

exec python -m unittest discover $@
