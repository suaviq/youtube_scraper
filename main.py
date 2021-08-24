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

# main_specific()
find_links(yt_polish[1], yt_polish_authors[1])
hashcode(f"links_{yt_polish_authors[1]}.txt", yt_polish_authors[1])
####################################################################################
# FOR KEYWORDS IN YOUTUBE SEARCH