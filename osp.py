from yahoofinancials import YahooFinancials
import json
import subprocess
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
def sp():
	yahoo_financials_tech = YahooFinancials("ORCL")
	x=(yahoo_financials_tech.get_stock_price_data())
	price=(x["ORCL"]["regularMarketPrice"])
	img=Image.new('RGB',(1600,1200),color='black')
	d=ImageDraw.Draw(img)
	font=ImageFont.truetype("Times.ttc",64,encoding="unic")
	date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	d.text((200,534),"Oracle's Stock Price on "+str(date),font=font,fill=(255,0,0))
	d.text((725,600),"$ "+str(price),font=font,fill=(255,0,0))
	img.save('osp.png')
	time.sleep(5)
	SCRIPT = """osascript -e 'tell application "System Events" to tell every desktop to set picture to "/Users/cmjohnst/Desktop/osp.png"'
	"""
	subprocess.Popen("killall Dock",shell=True)
	subprocess.Popen(SCRIPT,shell=True)
	time.sleep(295)
while True:
	try:
		sp()
	except:
		pass
