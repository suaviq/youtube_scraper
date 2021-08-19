import os
import shutil
import time

import pandas as pd
# import requests
# from bs4 import BeautifulSoup
from requests.models import parse_header_links
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from youtube_transcript_api import YouTubeTranscriptApi
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
# from pathlib import Path
# from urllib.parse import urljoin
# from urllib.request import Request, urlopen
