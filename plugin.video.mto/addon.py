import sys
import os
import urllib
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import logging
from operator import itemgetter

def show_tags():
  tag_handle = int(sys.argv[1])
  xbmcplugin.setContent(tag_handle, 'tags')

  for tag in tags:
    iconPath = os.path.join(home, 'logos', tag['icon'])
    li = xbmcgui.ListItem(tag['name'], iconImage=iconPath)
    url = sys.argv[0] + '?tag=' + str(tag['id'])
    xbmcplugin.addDirectoryItem(handle=tag_handle, url=url, listitem=li, isFolder=True)

  xbmcplugin.endOfDirectory(tag_handle)


def show_streams(tag):
  stream_handle = int(sys.argv[1])
  xbmcplugin.setContent(stream_handle, 'streams')
  logging.warning('TAG show_streams!!!! %s', tag)
  for stream in streams[str(tag)]:
    logging.debug('STREAM HERE!!! %s', stream['name'])
    iconPath = os.path.join(home, 'logos', stream['icon'])
    li = xbmcgui.ListItem(stream['name'], iconImage=iconPath)
    xbmcplugin.addDirectoryItem(handle=stream_handle, url=stream['url'], listitem=li)

  xbmcplugin.endOfDirectory(stream_handle)


def get_params():
  """
  Retrieves the current existing parameters from XBMC.
  """
  param = []
  paramstring = sys.argv[2]
  if len(paramstring) >= 2:
    params = sys.argv[2]
    cleanedparams = params.replace('?', '')
    if params[len(params) - 1] == '/':
      params = params[0:len(params) - 2]
    pairsofparams = cleanedparams.split('&')
    param = {}
    for i in range(len(pairsofparams)):
      splitparams = {}
      splitparams = pairsofparams[i].split('=')
      if (len(splitparams)) == 2:
        param[splitparams[0]] = splitparams[1]
  return param


def lower_getter(field):
  def _getter(obj):
    return obj[field].lower()

  return _getter


addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))

tags = [
  {
    'name': 'MTO UK - Thursday | 7pm local time', 
    'id': 'MTOUK',
    'icon': 'MTO-uk.png'
  }, {
    'name': 'MTO France - Friday| 7pm local time',
    'id': 'MTOFrance',
    'icon': 'MTO-France.png'
  }, {
    'name': 'MTO Germany - Sunday| 13.30pm local time',
    'id': 'MTOGermany',
    'icon': 'MTO-Germany.png'
  }
]


MTOUK = [{
  'name': 'Original language',
  'url': '',
  'icon': 'MTO-uk.png',
  'disabled': False
}, {
  'name': 'National Geographic',
  'url': '',
  'icon': 'National Geographic.png',
  'disabled': True
}, {
  'name': 'Food Network',
  'url': '',
  'icon': 'Food Network.png',
  'disabled': True
}, {
  'name': 'FX',
  'url': '',
  'icon': 'FX.png',
  'disabled': True
}
]


MTOFrance = [{
  'name': 'Original language',
  'url': 'http://media.iranproud.com/ipnx/media/series/episodes/Shahrzad_01.mp4',
  'icon': 'MTO-France.png',
  'disabled': False
}, {
  'name': 'French',
  'url': '',
  'icon': 'MTO-France.png',
  'disabled': False
}]

MTOGermany = [{
  'name': 'Original language',
  'url': 'http://media.iranproud.com/ipnx/media/series/episodes/Shahrzad_01.mp4',
  'icon': 'MTO-Germany.png',
  'disabled': False
}, {
  'name': 'German',
  'url': '',
  'icon': 'MTO-Germany.png',
  'disabled': False
}, {
  'name': 'English',
  'url': '',
  'icon': 'MTO-Germany.png',
  'disabled': False
}]

streams = {
  'MTOUK': sorted((i for i in MTOUK if not i.get('disabled', False)), key=lower_getter('name')),
  'MTOFrance': sorted((i for i in MTOFrance if not i.get('disabled', False)), key=lower_getter('name')),
  'MTOGermany': sorted((i for i in MTOGermany if not i.get('disabled', False)), key=lower_getter('name')),
  # 'MTOUK': sorted(MTOUK, key=lower_getter('name')),
  # 'MTOFrance': sorted(MTOFrance, key=lower_getter('name')),
  # 'MTOGermany': sorted(MTOGermany, key=lower_getter('name')),
}

PARAMS = get_params()
TAG = None
logging.warning('PARAMS!!!! %s', PARAMS)

try:
  TAG = PARAMS['tag']
except:
  pass

logging.warning('ARGS!!!! sys.argv %s', sys.argv)

if TAG == None:
  show_tags()
else:
  show_streams(TAG)
