while IFS="" read -r n || [ -n "$n" ]
    while IFS="" read -r p || [ -n "$p" ]
        do
        printf '%s\n' "$p"
        youtube-dl.exe "$p"
        done < "$n"
done < links_keywords.txt

# while IFS="" read -r p || [ -n "$p" ]
# do
#   printf '%s\n' "$p"
#   youtube-dl.exe "$p"
# done < links_Koronawirus.txt