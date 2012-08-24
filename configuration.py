import os

# Configurations File
class Configuration:
    # Url of the Planet's RSS Feed
    rssFeedURL = "http://planeta.debianbrasil.org/rss10.xml"

    # Bit.ly API Informations
    bitLyUser = ""
    bitLyApiKey = ""

    # Twitter application informations
    twitterConsumerKey = ""
    twitterConsumerSecret = ""

    # Twitter user/account tokens
    twitterAccessToken = ""
    twitterAccessTokenSecret = ""

    # Get the path of the tweetMyPlanet script
    __confFilename = os.path.realpath(__file__).split("/")[-1]
    __tweetMyPlanetDir = os.path.realpath(__file__).strip(__confFilename)

    # Path to Last-Tweeted-Entry file. File that stores the last tweeted entry
    lastTweetedEntryFilename = __tweetMyPlanetDir + "last-tweeted-entry"
