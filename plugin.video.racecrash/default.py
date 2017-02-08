# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/gsfvideos
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.racecrash'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
#icon = local.getAddonInfo('icon')
icon = local.getAddonInfo('icon')
icon2 = "https://i.ytimg.com/vi/a8SHzhcIP3s/hqdefault.jpg"
icon3 = "http://www.thetimes.co.uk/tto/multimedia/archive/00331/112387456_f1_331989b.jpg"
icon4 = "http://www.eliteracecars.com/wp-content/uploads/2013/10/Dani-Pedrosa-crash-at-motorLand-aragon-596x360.jpg"
icon5 = "http://www.dragzine.com/files/2010/12/HowNot-1.jpg"
icon6 = "http://static.nascar.com/content/dam/nascar/articles/2014/2/23/main/nascar-nscs14-day-high-ten-922x520.jpg/jcr:content/renditions/original"
addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
YOUTUBE_CHANNEL_ID = "channel/UCugquOddbE7nCGYmhSmni4A"
YOUTUBE_CHANNEL_ID2 = "channel/UCHx4Hx6CqzQ1NDBn1Mwj0Ow"
YOUTUBE_CHANNEL_ID3 = "channel/UCN0DgHQnQldjWJ2GNgQmfjg"
YOUTUBE_CHANNEL_ID4 = "channel/UCR5VdjpClw2-amJobJaDq0w"
YOUTUBE_CHANNEL_ID5 = "channel/UCQxkaxYlzzOcFclbIeWaIew"
# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player().play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("racecrash.main_list "+repr(params))
	
	plugintools.log("racecrash.run")
	
	#plugintools.direct_play(str(entryurl))

plugintools.add_item(
		title = "Sportcrash",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon2,
		folder = True )
		
plugintools.add_item(
		title = "Motorsports Crashes",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon3,
		folder = True )		
plugintools.add_item(
		title = "Racing Gone Wild",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon4,
		folder = True )	

plugintools.add_item(
		title = "Racing Fail",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon5,
		folder = True )			

plugintools.add_item(
		title = "Crash Racing",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon6,
		folder = True )			
		
run()