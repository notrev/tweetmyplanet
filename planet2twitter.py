#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Script that parses the Planeta Debian Brasil's RSS Feed
# and tweets the new entries in the Planeta Debian Brasil's
# twitter account
#
# Copyright (C) 2012 by Éverton Arruda <root@earruda.eti.br>
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

from lib import feedparser
from lib import urlshortener

rssFeedURL = "http://planeta.debianbrasil.org/rss10.xml"
bitLyUser = ""
bitLyApiKey = ""

feed = feedparser.parse(rssFeedURL)
bitly = urlshortener.BitLy(bitLyUser, bitLyApiKey)

for count in range(1):
    title = feed.entries[count].title
    if len(title) > 114:
        title = title[:114] + "..."
        
    shortenedUrl = bitly.shorten_url(feed.entries[count].link)
    if shortenedUrl == "":
        shortenedUrl = feed.entries[count].link

    print "%s | %s" %(title, shortenedUrl)
