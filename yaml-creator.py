import yaml, os

config = {
    "model_name": "my_model",
    "target_phrase": ["hey ares"],
    "custom_negative_phrases": [],
    "n_samples": 10000,
    "n_samples_val": 2000,
    "tts_batch_size": 50,
    "augmentation_batch_size": 16,
    "piper_sample_generator_path": "./piper-sample-generator",
    "output_dir": "./my_custom_model",
    "rir_paths": ["./mit_rirs"],
    "background_paths": ["./background_clips"],
    "background_paths_duplication_rate": [1],
    "false_positive_validation_data_path": "./validation_set_features.npy",
    "augmentation_rounds": 1,
    "feature_data_files": {
        "ACAV100M_sample": "./openwakeword_features_ACAV100M_2000_hrs_16bit.npy",
    },
    "batch_n_per_class": {
        "ACAV100M_sample": 1024,
        "adversarial_negative": 50,
        "positive": 50,
    },
    "model_type": "dnn",
    "layer_size": 32,
    "steps": 50000,
    "max_negative_weight": 1500,
    "target_false_positives_per_hour": 0.2,
    "piper_voice_name": "en-US-libritts_r-medium",
    "piper_voice_dir": "/home/zytherion/Projects/Custom-WakeWord/piper-sample-generator/models"
}

with open('my_model.yaml','w') as f: yaml.dump(config,f)
print("wrote", os.path.abspath('my_model.yaml'))