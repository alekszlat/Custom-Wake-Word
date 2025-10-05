# 🧰 Custom Wake-Word Training — Environment & Commands

## 1) Clone this repo
```bash
git clone --recursive https://github.com/alekszlat/Custom-Wake-Word 
```

## 2) Tools & audio libs
```bash
sudo apt-get update
sudo apt-get install -y software-properties-common build-essential git wget curl \
    ffmpeg sox libsndfile1 espeak-ng espeak-ng-data libespeak-ng1
```

## 3) Add the Deadsnakes PPA (trusted source for alternate Python versions)
```bash
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
```

## 4) Install 3.10 + venv + headers and set up venv
```bash
sudo apt-get install -y python3.10 python3.10-venv python3.10-dev
python3.10 -m venv venv
source venv/bin/activate
```

## 5) Install dependencies
```bash
# PyTorch (CPU trio) – avoids CUDA mismatch errors
pip install -r requirements.txt
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
