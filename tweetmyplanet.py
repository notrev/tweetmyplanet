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

import sys
import time
import pickle
import tweepy

from lib import feedparser
from lib import urlshortener
from configuration import Configuration as conf

print "[" + time.strftime("%d/%m/%Y:%H:%M:%S") + "]"

# Getting the feed and parsing it
print ">>> Getting the FEED and parsing entries..."
feed = feedparser.parse(conf.rssFeedURL)

# Load last tweeted feed entry from the file
print ">>> Reading the last tweeted entry..."
lastTweetedEntry = None
try:
    with open(conf.lastTweetedEntryFilename, 'r') as lastTweetedEntryFile:
        lastTweetedEntry = pickle.load(lastTweetedEntryFile)
except IOError:
    # If there's no file, continue normally
    print ">>> No last-tweeted-entry file. File will be created."
    pass

# Instantiating the BitLy url shortener
bitly = urlshortener.BitLy(conf.bitLyUser, conf.bitLyApiKey)

# Add untweeted entries to a list
print ">>> Processing entries..."
entriesToTweet = []
for entry in feed.entries:
    # If the entry is the last tweeted entry, stop the loop
    if lastTweetedEntry and entry.title == lastTweetedEntry:
        break

    # Title is limitted to 114 characters in order to add the link
    title = entry.title
    if len(title) > 113:
        title = title[:113] + "..."

    # Shortening the link
    shortenedUrl = bitly.shorten_url(entry.link)
    if shortenedUrl == "":
        shortenedUrl = entry.link

    # Adding entry to the entries-to-be-tweeted list
    entriesToTweet.append([title, shortenedUrl])

# If no new entries to be tweeted, exit.
if entriesToTweet == []:
    print ">>> No new entries to be tweeted."
    sys.exit(0)

print ">>> %d new entries." % (len(entriesToTweet))

# Preparing the connection with twitter
auth = tweepy.OAuthHandler(conf.twitterConsumerKey,
        conf.twitterConsumerSecret)
auth.set_access_token(conf.twitterAccessToken,
        conf.twitterAccessTokenSecret)

# Connect to twitter
print ">>> Connecting to twitter."
try:
    twitter = tweepy.API(auth)
except:
    print ">>> Error when trying to connect to Twitter."
    pass

# Reverse the list of entries to be tweeted in order to
# tweet the oldest first
print ">>> Tweeting new entries..."
entriesToTweet.reverse()
try:
    for entry in entriesToTweet:
        tweet = entry[0] + " | " + entry[1]
        print "### %s" % (tweet)
        twitter.update_status(tweet)
        lastTweetedEntry = entry[0]
except:
    # If any error occur in the update_status, continue to save
    # the last tweeted entry in the last-tweeted-entry file
    print ">>> Error when trying to tweet an entry."
    pass

# Writes the last tweeted entry to the last-tweeted-entry file
with open(conf.lastTweetedEntryFilename, "w") as lastTweetedEntryFile:
    print ">>> Writing the last tweeted entry to the file."
    pickle.dump(lastTweetedEntry, lastTweetedEntryFile)
