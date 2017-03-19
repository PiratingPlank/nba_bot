import nba_stats_bot as nba

import datetime as dt
from sys import argv
from pprint import pprint


def main():
    stat_time = ['daily', 'season']
    stat_list = ['points', 'rebounds', 'assists', 'blocks', 'steals']
    stat_abbr = ['PTS', 'REB', 'AST', 'BLK', 'STL']
    stat_name = ['hole-filler', 'ball-grabber', 'assist-meister', 'block god', 'thief']

    if len(argv) == 2 and argv[1] == 'help':
        print('Allowed stat types:\n{}, {}, {}, {}, {}.\n'.format(
                        'points', 'rebounds', 'assist', 'blocks', 'steals'))
        print('Allowed stat lengths:\n{}, {}.\n'.format(
                        'daily', 'season'))
        return

    if len(argv) <= 2:
        raise Exception('Not enough cooks in the kitchen; pass \'help\' for allowed arguments.')
    if len(argv) > 3:
        raise Exception('Too many cooks in the kitchen; pick a stat and a time-frame only.')

    for i in range(1,3):
        if argv[i] in stat_list:
            stat_type = argv[i]
        elif argv[i] in stat_time:
            stat_length = argv[i]
        else:
            raise Exception("Unknown argument passed: {}".format(argv[i]))

    if stat_length == 'daily':
        url = 'http://stats.nba.com/js/data/widgets/home_daily.json'
        date = dt.datetime.today().strftime("%m/%d/%Y")
        storytemplate = '{} was the top {} with {} {} on ' + date + '.'
    else:
        url = 'http://stats.nba.com/js/data/widgets/players_landing_inner.json'
        storytemplate = '{} is the top {} with {} {} per game.'

    top_stats = nba.bot(url)
    stat_num = stat_list.index(stat_type)
    stat = top_stats[stat_num]
    stat_abbr = stat_abbr[stat_num]

    story = storytemplate.format(stat['PLAYER_NAME'], stat_name[stat_num], stat[stat_abbr], argv[1])

    print(story)

if __name__ == '__main__':
    main()
