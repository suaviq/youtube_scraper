import os
import re
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd
from langdetect import detect, detect_langs
from requests.models import parse_header_links
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from youtube_transcript_api import YouTubeTranscriptApi
import pathlib

PATH = pathlib.Path.cwd()
