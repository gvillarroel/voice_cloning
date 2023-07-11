import pandas as pd
from pydub import AudioSegment
import os
import sys
file_name = sys.argv[1]

fin = f'rttm/{file_name}.rttm'
import os 

if os.path.exists(fin):
    # Leer el archivo CSV
    df = pd.read_csv(fin, sep=' ', header=None)
    # Cargar el archivo de audio original
    audio = AudioSegment.from_mp3(f"audio/{file_name}")

    # Recorre los valores únicos en la octava columna (los diferentes altavoces)
    for speaker in df[7].unique():
        # Crea un nuevo segmento de audio vacío para cada altavoz
        new_audio = AudioSegment.empty()

        # Filtra el DataFrame para solo los registros que corresponden al altavoz actual
        speaker_df = df[df[7] == speaker]

        # Para cada fila en el DataFrame del altavoz
        for index, row in speaker_df.iterrows():
            # Extraer el inicio y la duración del segmento
            start_time = row[3] * 1000  # pydub trabaja en milisegundos
            duration = row[4] * 1000

            # Extraer el segmento del audio original
            segment = audio[start_time:start_time + duration]

            # Añadir el segmento al nuevo audio
            new_audio += segment

        # Exporta el nuevo archivo de audio
        new_audio.export(f"processed/{file_name}_{speaker}.mp3", format="mp3")

    print("Archivos de audio generados.")
