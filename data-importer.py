import os, numpy as np, scipy.io.wavfile, datasets
from tqdm import tqdm
outdir = "./mit_rirs"
os.makedirs(outdir, exist_ok=True)
rir = datasets.load_dataset("davidscripka/MIT_environmental_impulse_responses",
                            split="train", streaming=True)
for row in tqdm(rir):
    name = row['audio']['path'].split('/')[-1]
    arr = (row['audio']['array'] * 32767).astype('int16')
    scipy.io.wavfile.write(os.path.join(outdir, name), 16000, arr)


outdir = "./background_clips"
os.makedirs(outdir, exist_ok=True)

# 1) Download locally (no streaming)
fma = datasets.load_dataset("rudraml/fma", name="small", split="train")

# 2) Resample to 16 kHz on the fly
fma = fma.cast_column("audio", datasets.Audio(sampling_rate=16000))

# 3) Save ~1 hour of 30s clips (adjust n if you want more)
n = 3600 // 30
for i, row in zip(range(n), fma):
    wav_path = os.path.join(outdir, os.path.basename(row["audio"]["path"]).replace(".mp3", ".wav"))
    arr16 = (row["audio"]["array"] * 32767).astype("int16")
    scipy.io.wavfile.write(wav_path, 16000, arr16)