# Custom Wake-Word Training — Environment & Commands

## 1) Tools & audio libs
```bash
sudo apt-get update
sudo apt-get install -y software-properties-common build-essential git wget curl \
    ffmpeg sox libsndfile1 espeak-ng espeak-ng-data libespeak-ng1
```

## 2) Add the Deadsnakes PPA (trusted source for alternate Python versions)
```bash
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
```

## 3) Install 3.10 + venv + headers and set up venv
```bash
sudo apt-get install -y python3.10 python3.10-venv python3.10-dev
python3.10 -m venv venv
source venv/bin/activate
```

## 4) Install dependencies
```bash
# PyTorch (CPU trio) – avoids CUDA mismatch errors
pip install --index-url https://download.pytorch.org/whl/cpu \
  "torch==2.5.1" "torchaudio==2.5.1" "torchvision==0.20.1"

# HF Datasets + Arrow (avoid pyarrow API errors)
pip install "datasets>=2.18,<3.0" "pyarrow>=12,<18"

# Audio & augmentation
pip install soundfile scipy numpy tqdm audiomentations==0.33.0 torch-audiomentations==0.11.0 acoustics==0.2.6

# Metrics & helpers
pip install torchmetrics==1.2.0 torchinfo==1.8.0 mutagen==1.47.0 pronouncing==0.2.0

# Piper + phonemizers (TTS synth for data generation)
pip install piper-tts espeak-phonemizer deep-phonemizer==0.0.19 speechbrain==0.5.14
```

## 5)Clone repos
```bash
git clone https://github.com/dscripka/openWakeWord.git
git clone https://github.com/dscripka/piper-sample-generator.git
```

## 6) Download OpenWakeWord models
```bash
mkdir -p ./openWakeWord/openwakeword/openwakeword/resources/models
cd ./openWakeWord

wget -O openwakeword/resources/models/embedding_model.onnx \
  https://github.com/dscripka/openWakeWord/releases/download/v0.5.1/embedding_model.onnx
wget -O openwakeword/resources/models/embedding_model.tflite \
  https://github.com/dscripka/openWakeWord/releases/download/v0.5.1/embedding_model.tflite
wget -O openwakeword/resources/models/melspectrogram.onnx \
  https://github.com/dscripka/openWakeWord/releases/download/v0.5.1/melspectrogram.onnx
wget -O openwakeword/resources/models/melspectrogram.tflite \
  https://github.com/dscripka/openWakeWord/releases/download/v0.5.1/melspectrogram.tflite

cd ..
```

## 7) Piper generator checkpoint (the .pt)
```bash
mkdir -p ./piper-sample-generator/models
# Save the official generator checkpoint under the expected name:
wget -O ./piper-sample-generator/models/en-us-libritts-high.pt \
  'https://github.com/rhasspy/piper-sample-generator/releases/download/v2.0.0/en_US-libritts_r-medium.pt'

## 8) Download feature datasets (for training)
wget -O ./openwakeword_features_ACAV100M_2000_hrs_16bit.npy \
  https://huggingface.co/datasets/davidscripka/openwakeword_features/resolve/main/openwakeword_features_ACAV100M_2000_hrs_16bit.npy
wget -O ./validation_set_features.npy \
  https://huggingface.co/datasets/davidscripka/openwakeword_features/resolve/main/validation_set_features.npy
```

## 9)Run helping scripts to set up training data
```bash
python data-creator.py
python yaml-creator.py
```

## 10) Train your model
```bash
python openwakeword/openwakeword/train.py --training_config my_model.yaml --generate_clips
python openwakeword/openwakeword/train.py --training_config my_model.yaml --augment_clips
python openwakeword/openwakeword/train.py --training_config my_model.yaml --train_model
```
