import fpclib
import re
# You can put other imports here, but the standalone only supports importing the following other libraries (Other imports require python to be installed on the host machine and the script to be run directly):

# os, sys, time, re, json,
# bs4, argparse, codecs, datetime, glob,
# sqlite3, threading, traceback, webbrowser, zipfile,
# urllib, difflib, googletrans, qfile, and Levenshtein.

TITLE = re.compile("(.*?) - Play online at GameMonetize.co Game")

# This is the regex that will be used to match the site url. It is required!
regex = 'gamemonetize.co'

# Priority that the site has when matching regexes. Higher priorities will be checked first. If left out, it is assumed to be 0.
priority = 0

# "WebsiteName" should be the exact same as the name in <WebsiteName>.py, otherwise fpcurator will complain.
class GameMonetize(fpclib.Curation):
    def parse(self, osoup):
        # "self" is a curation generated from a given matched url (see fpclib.Curation in the fpclib documentation), while osoup is a beautifulsoup object generated from the html downloaded from the given matched url.
        # You'll want to use self.set_meta to set the metadata of the curation based upon the osoup object.
        pass
         # Get Logo
        try: self.logo = fpclib.normalize(soup.find("meta", property="og:image")["content"], keep_prot=True)
        except: pass
      # Get Description
      # Get Release Date
      
      # Get Developer and set Publisher
        self.dev = [dev.text.strip() for dev in soup.select(".game_dev_list > li")]
        self.pub = "GameMonetize"
# Only HTML5 is supported      
        self.platform = "HTML5"
        self.app = fpclib.BASILISK
       def save_image(self, url, file_name):
        try:
            fpclib.download_image(url, name=file_name)
        except: pass
	# You can also overwrite any other methods of fpclib.Curation here to add custom functionality, including but not limited to:
    # get_files(self) - This method is called after parse() called to get the files specified by the launch commands of the curation and additional apps (by default). Overwrite it if you want to download other files into the curation (like for html files).
    # soupify(self) - called to get osoup for the parse method. Overwrite it if you need to provide specific information (like login info or a captcha token) to a webpage in order to access the page properly.
    # save_image(self, url, file_name) - called both to save the logo and screenshot of the curation based on self.logo and self.ss (only if they are set). This by default does NO error checking, so if you want error checking you'll have to overwrite this function.
