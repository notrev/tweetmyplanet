TweetMyPlanet
===================

ABOUT:
-------------------
TweetMyPlanet is a python script that reads an RSS Feed and tweets
it's entries in a twitter account.

This script was intended to tweet Planeta Debian Brasil's[0] entries
into @PlanetaDebianBr[1] account. As is done in @PlanetDebian[2].

TweetMyPlanet uses Tweepy[3] and feedparser[4].

Developed by Éverton Arruda <root@earruda.eti.br>
WebSite: http://earruda.eti.br
License: GNU/GPLv3

USAGE
-------------------
First of all, you'll need a twitter account with permissions given
to TweetMyPlanet Application. There is still a page being developed
to automate this step. Check out the website to stay informed.

You'll also need a Bit.ly account in order to shrten the URLs.

After getting these infos, you'll have to add them in the configuration.py
file together with the URL to the RSS Feed and run the script:

$ python tweetmyplanet.py

If you want it to run automatically, just add it in the crontab.

LINKS
-------------------
[0] http://planeta.debianbrasil.org
[1] http://twitter.com/planetadebianbr
[2] http://twitter.com/planetdebian
[3] https://github.com/tweepy/tweepy
[4] http://code.google.com/p/feedparser/
