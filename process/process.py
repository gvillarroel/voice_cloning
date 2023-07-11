# 1. visit hf.co/pyannote/speaker-diarization and accept user conditions
# 2. visit hf.co/pyannote/segmentation and accept user conditions
# 3. visit hf.co/settings/tokens to create an access token
# 4. instantiate pretrained speaker diarization pipeline

import sys
file_name = sys.argv[1]
import torch
import os

from pyannote.audio import Pipeline

output_file = f"rttm/{file_name}.rttm"
if not os.path.exists(output_file):

    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1.1",
                                        use_auth_token="").to(torch.device('cuda', 0))


    # apply the pipeline to an audio file
    diarization = pipeline(f"audio/{file_name}")

    # dump the diarization output to disk using RTTM format
    with open(output_file, "w") as rttm:
        diarization.write_rttm(rttm)
