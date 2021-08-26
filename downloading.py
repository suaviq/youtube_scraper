from yt_libraries import *

# working

# downloads subtitles using YoutubeTranscriptApi and saves it to txt file
def download_subtitles(code):
    try:
        srt = YouTubeTranscriptApi.get_transcript(code, languages=["pl"])
        with open(f"{code}.txt", "w") as f:
            for i in srt:
                try:
                    f.write(f"{i}\n")
                except:
                    print('Error with downloading subtitles')
    except:
        print('No polish subtitles')

# working 
# given string is in format:
# {'text': 'Ale co w ogole to znaczy?', 'start': 209.9, 'duration': 1.9}
# changes it to:
# Ale co w ogole to znaczy?
def clean_text(file, file_code):
    text = []
    clean_text =[]
    with open(file) as file:
        for line in file:
            new_line = line.replace('\n', '')
            new_line = line
            print(new_line)
            text.append(new_line)

    pattern = ": '[\sa-za-zżźćńółęąśŻŹĆĄŚĘŁÓŃA-Z0-9,]*"
    for line in text:
        match = re.findall(pattern, line) 
        code = str(match)
        clean_line = code.replace(": '",'').replace('["','').replace('"]','')
        print(clean_line)
        clean_text.append(clean_line)

    with open(file_code, 'w') as f:
        for item in clean_text:
            f.write("%s\n" % item)

# clean_text('yYTes03bvgM.txt', 'clean_yYTes03bvgM.txt')
# read_hashcode('hashcodes_billie_sparrow.txt')


####################################################################################
#working

# checks the language of given txt file; when file is empty, returns None
def check_lanuguage(clean_file):
    list = []
    filesize = os.path.getsize(clean_file)
    if filesize == 0:
        print("The file is empty: " + str(filesize))
    else:
        print("The file is not empty: " + str(filesize))
        with open(clean_file) as f:
            for text in f:
                list.append(text.replace('\n',''))
        for n in range(len(list)):
            sentence = ''' " ''' + list[n] + ''' " '''
            try:
                print(detect_langs(sentence))
            except:
                print("No sentence here")

####################################################################################

def read_hashcode(filename):
    hashcodes_to_download = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                new_line = (f"{line}").replace('\n','')
                # print(new_line)
                hashcodes_to_download.append(new_line)
            except:
                print("Space")
    for hash in hashcodes_to_download:
        print(hash)
        download_subtitles(hash)
        clean_text(f'{hash}.txt', f'clean_{hash}.txt')
        check_lanuguage(f'clean_{hash}.txt')
        old_path_hash = os.path.join(PATH, f'{hash}.txt')
        old_path_clean_hash = os.path.join(PATH, f'clean_{hash}.txt')
        new_path = os.path.join(PATH, 'mp3+subtitles', hash)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        Path(old_path_hash).rename(os.path.join(new_path, f'{hash}.txt'))
        Path(old_path_clean_hash).rename(os.path.join(new_path,f'clean_{hash}.txt'))
            

# read_hashcode('hashcodes_billie_sparrow.txt')





####################################################################################

#!/usr/bin/python

#working
# starts downloading.sh file and runs it
# in downloading.sh file the txt files with links to videos are opened
# the program in shell script downloads it 

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


def change_directory_for_videos():
    pattern =r"-[A-Za-z0-9_.]*"
    for subdir, dirs, files in os.walk(PATH):
        for file in files:
            try:
                new_filename = deEmojify(file)
                Path(os.path.join(PATH, file)).rename(os.path.join(PATH, new_filename))
                match = re.findall(pattern, new_filename) 
                code = str(match)
                print(code)
                clear_code = code.replace('''['-''', '').replace('''.mp4']''','')
                print(clear_code)
                Path(os.path.join(PATH, new_filename)).rename(os.path.join(PATH, 'mp3+subtitles', clear_code, new_filename))
            except Exception as e:
                # print(f"Problem:{e}")
                continue

def download_working_specific(hashcode_name):
    os.system("sh downloading_specific.sh")
    read_hashcode(hashcode_name)
    change_directory_for_videos()

def download_working_keyword(hashcode_name):
    try:
        os.system("sh downloading_keyword.sh")
    except:
        print('No subtitles in polish -> could not download video')
    read_hashcode(hashcode_name)
    change_directory_for_videos

download_working_keyword('hashcodes_Koronawirus.txt')