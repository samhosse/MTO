tags = [
  {
    'name': 'Live TV',
    'id': 'LiveTV',
    'icon': 'livetv.png'
  }, {
    'name': 'Movies',
    'id': 'Movies',
    'icon': 'movies.png'
  }
]


LiveTV = [{
  'name': 'Vevo Tv',
  'url': '',
  'icon': 'Vevo Tv.png',
  'disabled': False
}, {
  'name': 'National Geographic',
  'url': '',
  'icon': 'National Geographic.png',
  'disabled': False
}, {
  'name': 'Food Network',
  'url': '',
  'icon': 'Food Network.png',
  'disabled': False
}, {
  'name': 'FX',
  'url': '',
  'icon': 'FX.png',
  'disabled': False
}]


Movies = [{
  'name': 'Despicable Me 2',
  'url': 'http://media.iranproud.com/ipnx/media/series/episodes/Shahrzad_01.mp4',
  'icon': 'Despicable Me 2.png',
  'disabled': False
}]


streams = {
  'LiveTV': sorted((i for i in LiveTV if not i.get('disabled', False)), key=lower_getter('name')),
  'Movies': sorted((i for i in Movies if not i.get('disabled', False)), key=lower_getter('name')),
  # 'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  # 'Movies': sorted(Movies, key=lower_getter('name')),
}
