#!/bin/sh
# Yeni bir oturumda bir kez çalıştır: python bağımlılıkları + whisper modeli
pip install -q faster-whisper numpy pillow
python3 -c "from faster_whisper import WhisperModel; WhisperModel('medium', device='cpu', compute_type='int8')"
command -v ffmpeg >/dev/null || (apt-get update -qq && apt-get install -y -qq ffmpeg fonts-dejavu-core)
