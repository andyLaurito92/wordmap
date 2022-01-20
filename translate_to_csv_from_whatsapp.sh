filename=$1
output=$2

echo "Going to transform file ${filename}"

tr -sc "a-zA-Záéíóúñ" "\n" < $filename | sort | uniq -c | sort -n -r | sed -r "s/(^ *)//g" | tr " " ";" >> output.csv
