#!/usr/bin/env python3

from election import Election

FILE_PATH = './data/2017-01-09_dickson.json'

dickson = Election.from_json(FILE_PATH)
dickson.calculate()
dickson.print_results()
