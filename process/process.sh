#cd videos && for file in Class*.mp4; do mv "$file" "c${file//Class /}"; done


for file in $(ls -d videos/*.mp4);
do
    echo "$file";
    fshort="${file#videos/}"
    ffmpeg -i $file -vn -ab 128k -ar 44100 -y audio/$fshort.mp3;
done

#ls audio/ | xargs -P 4 -I {} python process.py {}
#ls audio/ | xargs -P 4 -I {} python split.py {}

