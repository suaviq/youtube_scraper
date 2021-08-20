yt_polish =['https://www.youtube.com/user/vroobelekbillie/videos', 'https://www.youtube.com/c/7metrówpodziemią/videos', 'https://www.youtube.com/c/ArlenaWitt/videos','https://www.youtube.com/c/KasiaGandor/videos','https://www.youtube.com/c/NishkaMovie/videos','https://www.youtube.com/c/PsychoLoszka/videos']
yt_polish_authors = ['billie_sparrow', '7_metrów_pod_ziemią', 'Arlena_Witt', 'Kasia_Gandor', 'Natalia_Nishka_Tur', 'PsychoLoszka']

yt_japanese = ['https://www.youtube.com/c/AniMelody2/videos','https://www.youtube.com/channel/UCHJSUG4MRcFszyC5qj7s7Uw']

def generate_name_of_files():
    for n in range(0,6):
        links = "links_" +  yt_polish_authors[n]
        print(links)
    for x in range(0,6):   
        hashcodes = "hashcodes_" + yt_polish_authors[x]
        print(hashcodes)


generate_name_of_files()
