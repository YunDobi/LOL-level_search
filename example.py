from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-668cb7b7-972a-4669-9e8c-864245d5f8b4')
my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'No candy for u')
print(me)