#working
while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  youtube-dl.exe "$p"
done < links_billie_sparrow.txt

while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  youtube-dl.exe "$p" || :
done < links_7_metrów_pod_ziemią.txt

while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  youtube-dl.exe "$p" || :
done < links_Arlena_Witt.txt

while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  youtube-dl.exe "$p" || :
done < links_Kasia_Gandor.txt

while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  youtube-dl.exe "$p" || :
done < links_Natalia_Nishka_Tur.txt

while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  youtube-dl.exe "$p" || :
done < links_PsychoLoszka.txt







