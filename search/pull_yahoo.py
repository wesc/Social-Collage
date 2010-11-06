"""
Messing around script...
"""

import json
import urllib


# filename, headers = urllib.urlretrieve("http://boss.yahooapis.com/ysearch/images/v1/%22Nikola%20Tesla%22?appid=fOwNVoHV34FaT7MH5A6Jzl2.DTD1A2NQ6tz1i2.f1zxxxSmVkO2M1RM1267Qx80-")

#print open(filename, "r").read()



s = json.load(open("tesla_dump.json"))

print s['ysearchresponse']['resultset_images'][0]['thumbnail_width']
print s['ysearchresponse']['resultset_images'][0]['thumbnail_height']
print s['ysearchresponse']['resultset_images'][0]['thumbnail_url']

print s['ysearchresponse']['count']
