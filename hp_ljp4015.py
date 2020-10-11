# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#		  							    #
# This is a script to print the ink level of an HP LaserJet P4015 printer.  #
#									    #
# Author: Tyler Hooks							    #
#									    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

# IP address of printer. 
address = ""

# Ignore invalid SSL certificate.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
	with urlopen(address, context = ctx) as url:
		soup = BeautifulSoup(url, 'html.parser')
		# HTML block containing cartridge information. 
		ink_block = soup.find('div', attrs = {'class':'hpGasGaugeBlock'}).span.text
		# Get the ink level. 
		ink_level = re.findall('\d+%', ink_block)[0]
		# Print value as proof-of-concept. 
		print(ink_level)
	
except Exception as e:
	print(e)
