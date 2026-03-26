#!/usr/bin/env python3
"""
Split audio into 5-minute chunks and transcribe each with Whisper.
Outputs a merged transcription text file.
"""

import os
import subprocess
import sys
import whisper

AUDIO_FILE = "reuniao-allyson-23-03-2026.m4a"
CHUNKS_DIR = "chunks"
TRANSCRIPTIONS_DIR = "transcricoes"
OUTPUT_MERGED = "transcricao_completa.txt"
CHUNK_DURATION = 300  # 5 minutes in seconds

os.makedirs(CHUNKS_DIR, exist_ok=True)
os.makedirs(TRANSCRIPTIONS_DIR, exist_ok=True)

# Step 1: Get total duration
print("[1/3] Obtendo duração do arquivo de áudio...")
result = subprocess.run(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
     "-of", "default=noprint_wrappers=1:nokey=1", AUDIO_FILE],
    capture_output=True, text=True
)
total_duration = float(result.stdout.strip())
print(f"    Duração total: {total_duration:.1f} segundos ({total_duration/60:.1f} minutos)")

# Step 2: Split into chunks
print(f"\n[2/3] Dividindo em pedaços de {CHUNK_DURATION//60} minutos...")
chunk_files = []
start = 0
idx = 1
while start < total_duration:
    chunk_name = os.path.join(CHUNKS_DIR, f"chunk_{idx:03d}.wav")
    cmd = [
        "ffmpeg", "-y", "-i", AUDIO_FILE,
        "-ss", str(start),
        "-t", str(CHUNK_DURATION),
        "-ar", "16000",  # 16kHz for Whisper
        "-ac", "1",      # mono
        chunk_name
    ]
    subprocess.run(cmd, capture_output=True)
    chunk_files.append(chunk_name)
    print(f"    Chunk {idx}: {start//60:.0f}min - {min(start+CHUNK_DURATION, total_duration)//60:.0f}min → {chunk_name}")
    start += CHUNK_DURATION
    idx += 1

# Step 3: Transcribe each chunk
print(f"\n[3/3] Transcrevendo {len(chunk_files)} pedaços com Whisper (modelo 'medium')...")
model = whisper.load_model("medium")

all_texts = []
for i, chunk_file in enumerate(chunk_files, 1):
    print(f"    Transcrevendo chunk {i}/{len(chunk_files)}: {chunk_file} ...")
    result = model.transcribe(chunk_file, language="pt", fp16=False)
    text = result["text"].strip()
    
    # Save individual transcription
    txt_name = os.path.join(TRANSCRIPTIONS_DIR, f"transcricao_{i:03d}.txt")
    with open(txt_name, "w", encoding="utf-8") as f:
        f.write(text)
    
    all_texts.append(text)
    print(f"    ✓ Chunk {i} transcrito ({len(text)} caracteres)")

# Step 4: Merge all transcriptions
print(f"\nUnindo transcrições em '{OUTPUT_MERGED}'...")
with open(OUTPUT_MERGED, "w", encoding="utf-8") as f:
    for i, text in enumerate(all_texts, 1):
        start_min = (i-1) * 5
        end_min = i * 5
        f.write(f"[{start_min:02d}:00 - {end_min:02d}:00]\n")
        f.write(text)
        f.write("\n\n")

print(f"\n✅ Transcrição completa salva em: {OUTPUT_MERGED}")
print(f"   Total de caracteres: {sum(len(t) for t in all_texts)}")
