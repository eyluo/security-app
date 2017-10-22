# -*- coding: utf-8 -*-

import urllib.request

from geolite2 import geolite2

def get_location_dict():
    data = urllib.request.urlopen('https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt')

    ip_dict = dict()

    for line in data:
        current_ip = line.decode('utf-8').strip('\n')
        current_ip_dict = dict()

        if current_ip[0] == '#': continue
        else:
            location_info = geolite2.reader().get(current_ip)
            # print(current_ip)

            if type(location_info) == dict:
                current_ip_dict['continent'] = location_info['continent']['names']['en']
                current_ip_dict['country'] = location_info['country']['names']['en']
                current_ip_dict['coordinates'] = (location_info['location']['latitude'], location_info['location']['longitude'])
                ip_dict[current_ip] = current_ip_dict
                # print("coordinates: ", (location_info['location']['latitude'], location_info['location']['longitude']))
                # print('\n')
            # else: 
                # print("No location info!")
                # print('\n')

            

    return ip_dict

def get_country_list(location_dict):
    country_list = list()
    for ip in location_dict:
        print(ip)
        print(location_dict[ip]['country'])
        if location_dict[ip]['country'] not in country_list:
            country_list.append(location_dict[ip]['country'])
    return country_list

def get_coord_list(location_dict):
    coord_list = list()
    for ip in location_dict:
        if location_dict[ip]['coordinates'] not in coord_list:
            coord_list.append(location_dict[ip]['coordinates'])
    return coord_list