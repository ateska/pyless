#!/bin/sh

cd $(dirname ${0}) && java -jar antlr-3.1.3.jar lesscss.g -o ../pyless
