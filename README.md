# TweetMyPlanet #

## ABOUT: ##

TweetMyPlanet is a python script that reads an RSS Feed and tweets
it's entries in a twitter account.

This script was intended to tweet [Planeta Debian Brasil](http://planeta.debianbrasil.org)'s
entries into [@PlanetaDebianBr](http://twitter.com/planetadebianbr) account.
As it is done in [@PlanetDebian](http://twitter.com/planetdebian).

TweetMyPlanet uses [Tweepy](https://github.com/tweepy/tweepy) and [feedparser](http://code.google.com/p/feedparser/).

Developed by Éverton Arruda <root AT earruda.eti.br>

WebSite: http://earruda.eti.br

License: GNU/GPLv2

## USAGE ##

You will need 4 informations in order for the plugin to be able to publish to
Twitter: API Consumer Key, API Consumer Secret, OAuth Access Token, OAuth Access Token Secret.

To get these informations, you will need to create an app in Twitter. To do so, you
can follow the steps in this link:

http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/

You'll also need a Bit.ly account in order to shorten the URLs.

After getting these infos, you'll have to add them in the `configuration.py`
file together with the URL to the RSS Feed and run the script:

```
$ python tweetmyplanet.py
```

If you want it to run automatically, just add it in the crontab.
