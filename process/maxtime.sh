#!/bin/bash

input="processed/SPEAKER_07.mp3"
output="output.mp3"
max_size=10000  # Tamaño máximo en kilobytes

# Obtén la duración total (en segundos) del archivo de entrada
total_duration=1200

for (( duration = total_duration; duration > 0; duration-- )); do
    ffmpeg -y -i "$input" -t "$duration" -c copy "$output"  # Recorta el audio
    size=$(du -k "$output" | cut -f1)  # Obtén el tamaño del archivo de salida en kilobytes
    if (( size <= max_size )); then
        echo "El tamaño final del archivo es ${size}K, la duración es ${duration} segundos"
        break
    fi
done
