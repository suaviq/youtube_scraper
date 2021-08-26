from link_generator import *
from data_structures import *
from downloading import *
####################################################################################
# FOR SPECIFIC YT CHANNELS
# 1. Generate links
def main_specific():
    for n in range(0,6):
        find_links(yt_polish[n], yt_polish_authors[n])
        hashcode(f"links_{yt_polish_authors[n]}.txt", yt_polish_authors[n])
        download_working_specific(f'hashcodes_{yt_polish_authors[n]}.txt')

####################################################################################
# FOR KEYWORDS IN YOUTUBE SEARCH
# musze linki zapistwac do listy najlepiej txt i po tym iterowac 
def main_keyword():
    keywords = []
    with open(f'keywords.txt', 'r') as f:
        for item in f:
            keywords.append(item)
    for key in keywords:
        hashcode(f"links_{keywords[key]}.txt", keywords[key])
        download_working_keyword(f'hashcodes_{keywords[key]}.txt')

