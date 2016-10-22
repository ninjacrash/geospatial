#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:54:22 2016

@author: clesiemo3
"""
import requests

if __name__ == '__main__':
    
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=700 Clark Street St. Louis 63102')

    resp_json_payload = response.json()

    print(resp_json_payload['results'][0]['geometry']['location'])