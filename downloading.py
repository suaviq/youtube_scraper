from yt_libraries import *

# working

# downloads subtitles using YoutubeTranscriptApi and saves it to txt file
def download_subtitles(code):
    srt = YouTubeTranscriptApi.get_transcript(code, languages=["pl"])
    with open(f"{code}.txt", "w") as f:
        for i in srt:
            try:
                f.write(f"{i}\n")
            except:
                print('Error with downloading subtitles')
# working 
hashcodes_to_download = []
def read_hashcode(filename):
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


# read_hashcode('hashcodes_billie_sparrow.txt')
    # download_subtitles(hash)




# download_subtitles('UKl6DMzrD1U')
####################################################################################

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


for hash in hashcodes_to_download:
        try:
            line = (f"{hash}").replace('\n','')
            print(line)
            clean_text(f"'{line}.txt'", f"'clean_{line}.txt'")
        except:
            print("Space")

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

# check_lanuguage('clean_yYTes03bvgM.txt')

# test1.txt is empty and it's working
# check_lanuguage('test1.txt')



####################################################################################

#!/usr/bin/python

#working
# starts downloading.sh file and runs it
# in downloading.sh file the txt files with links to videos are opened
# the program in shell script downloads it 

# os.system("sh downloading.sh")