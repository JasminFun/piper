python3 -m piper_train.preprocess \
  --language cmn \
  --input-dir /mnt/d/project/tts/piper/dataset \
  --output-dir /mnt/d/project/tts/piper/training \
  --dataset-format ljspeech \
  --single-speaker \
  --sample-rate 16000 \
  --audio-quality x-low \
  --max-workers 12

python3 -m piper_train \
  --dataset-dir /mnt/d/project/tts/piper/training/ \
  --accelerator 'gpu' \
  --devices 1 \
  --batch-size 32 \
  --validation-split 0.0 \
  --num-test-examples 0 \
  --max_epochs 10000 \
  --resume_from_checkpoint /mnt/d/project/tts/piper/pretrained_model/epoch=2329-step=558624.ckpt \
  --checkpoint-epochs 1 \
  --precision 32 \
  --log_every_n_steps 1\
  --reload_dataloaders_every_n_epochs 1 \
  --replace_sampler_ddp False \
  --detect_anomaly True