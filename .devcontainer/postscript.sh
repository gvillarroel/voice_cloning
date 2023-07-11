apt update && apt upgrade -y && apt install ffmpeg -y

pip install -r ../requirements.txt
pip install -qq https://github.com/pyannote/pyannote-audio/archive/refs/heads/develop.zip
#pip uninstall pytorch-lightning
#pip install lightning
#pip install -U protobuf

#pip install pyannote.audio
