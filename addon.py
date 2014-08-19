import sys
from threading import Thread

import xbmcgui
import xbmcplugin
from xbmc import Player

from touchandgo import watch

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

dialog = xbmcgui.Dialog()
input_data = dialog.input('Ingresar nombre, temporada y capitulo',
                         type=xbmcgui.INPUT_ALPHANUM)

input_data = input_data.split('/')
name, season, episode = input_data

args = {'name': name,
        'season': season,
        'episode': episode,
        'serve': True
        }
t = Thread(target=watch, kwargs=args)
t.start()


dialog = xbmcgui.Dialog()
dialog.notification('touchandgo', 'touchandgo is starting waith for it.',
                      xbmcgui.NOTIFICATION_INFO, 60000)

video_url = "http://localhost:8888/"

player = Player(xbmc.PLAYER_CORE_AUTO)
player.play(video_url)


