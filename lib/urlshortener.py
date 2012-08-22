#-*- coding: utf-8 -*-

# URL Shortener Lib
#
# @author: Éverton Arruda <root@earruda.eti.br>
#
# Copyright (C) 2005 by Éverton Arruda
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import simplejson

class BitLy:
    """
    Bit.ly URL Shortener Class
    Uses the Bit.ly URL Shortening Service to
    shorten URLs

    shorten_url method based on:
    http://segfault.in/2010/10/shorten-urls-using-python-and-bit-ly/
    """
    __login = None
    __apiKey = None

    def __init__(self, login, apiKey):
        self.__login = login
        self.__apiKey = apiKey

    def shorten_url(self, url):
        """
        Shortens the given URL
        """
        try:
            params = {"longUrl": url,
                    "login": self.__login,
                    "apiKey": self.__apiKey,
                    "format": "json"}
            params = urllib.urlencode(params)

            encodedUrl = "http://api.bit.ly/v3/shorten?%s" % (params)
            request = urllib.urlopen(encodedUrl)
            response = request.read()
            request.close()
            response = simplejson.loads(response)

            if response["status_code"] == 200:
                return response["data"]["url"]
            return ""
        except:
            return ""
