The stats bot is something that I’ve been considering for a little while. It is
 pretty easy to get hold of this kind of information, but only if you go to
 stats.nba.com on a regular basis. But if you don’t use your desktop, this can
 make the looking a little easier.

I like adding a little flair to the bot as well. I haven’t seen anything like
this and searching just from the command line makes it simpler. Admittedly,
creativity is the issue for something like this, as changing the actual
information requires a LOT more scraping, and when the data is available
already for the searcher.

Being cute might be a problem for a lot of these bots, but for me, someone
with very little programming ability still, that little bit of flair is one
of the only things available to me that can differentiate the bot from someone
else’s creation.

To the actual bot: bot itself is simple, pulls the information needed to go
through the command line. As it should be done.

For the main; the issue is to find the data source needed for the information.
Season and daily are the important ones for people interested in this, and for
casual fans knowing the average versus the season is the change between average
and integer highs.

The data finding was helped with Dan getting the first .json file, and I found
the other without a huge amount of pain. I was able to get hold of the
information because it was readily available, but the real issue is that the
 data is a massive pain to look at. It’s a super deep file, thick with
 information and stacks and stacks of dictionaries and lists. But once you get
 past understanding the information then it’s alright to deal with, as the main
 function shows with a fairly simple for-loop that pulls the information from
 the data space that it resides.

The main issue is that the information changes every time a player does
something. For daily, as soon as games begin, the numbers are set to 0,
which means that the information is changing up until all games are over.
But, it does have some use in those changes; who did what when? What’s going
on now? So the sudden changes might shift how a person watches a game, or
switches to other games. Not the worst problem, but certainly an issue for the
bot and one that might make it only useful from like 2AM Eastern time to about
7PM Eastern Time. A problem, but one that is more based on the data shift than
what the bot is doing.

Overall, I think that the main strength of the bot is it’s ability to find the
 best of each statistical category for seasonal or daily statistics. Its
 weakness is that those best of’s are always in flux. So those changes are
 not great, but they certainly do add some volatility to the bot’s work.
