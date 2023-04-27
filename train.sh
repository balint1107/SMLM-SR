#!/usr/bin/bash

python realesrgan/train.py -opt options/train_realesrnet_x4plus_med.yml --auto_resume
python realesrgan/train.py -opt options/train_realesrgan_x4plus_med.yml --auto_resume
