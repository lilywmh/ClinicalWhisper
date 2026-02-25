#!/usr/bin/env python3
"""
Generate synthetic .wav files for testing the DAIC-WOZ analysis pipeline.

These files simulate speech-like acoustic patterns (tone + silence) without
containing any real clinical data. Run this script once before testing the
Colab notebooks.

Usage:
    python generate_dummy_audio.py
"""

import os
import numpy as np
from scipy.io import wavfile

SAMPLE_RATE = 16000  # 16 kHz — Whisper's expected sample rate
DURATION = 5.0       # seconds per file
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_tone(freq: float, duration: float, sr: int = SAMPLE_RATE) -> np.ndarray:
    """Generate a sine-wave tone."""
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * freq * t)


def generate_silence(duration: float, sr: int = SAMPLE_RATE) -> np.ndarray:
    """Generate silence."""
    return np.zeros(int(sr * duration))


def save_wav(filename: str, audio: np.ndarray, sr: int = SAMPLE_RATE):
    """Save audio array as a 16-bit WAV file."""
    filepath = os.path.join(OUTPUT_DIR, filename)
    # Normalize to int16 range
    audio_int16 = np.int16(audio / np.max(np.abs(audio) + 1e-9) * 32767 * 0.8)
    wavfile.write(filepath, sr, audio_int16)
    print(f"  ✓ Saved {filepath} ({len(audio) / sr:.1f}s)")


def main():
    print("Generating dummy audio files...\n")

    # --- Participant 001: Monotone speech (steady 200 Hz) ---
    # Simulates flat affect / low vocal variability
    segments = []
    for _ in range(5):
        segments.append(generate_tone(200, 0.8))
        segments.append(generate_silence(0.2))
    audio_001 = np.concatenate(segments)
    save_wav("participant_001.wav", audio_001)

    # --- Participant 002: Expressive speech (varied frequencies) ---
    # Simulates normal prosodic variation
    freqs = [180, 250, 300, 220, 280]
    segments = []
    for f in freqs:
        segments.append(generate_tone(f, 0.7))
        segments.append(generate_silence(0.3))
    audio_002 = np.concatenate(segments)
    save_wav("participant_002.wav", audio_002)

    # --- Participant 003: Hesitant speech (long pauses) ---
    # Simulates psychomotor retardation / response latency
    segments = []
    for freq in [190, 210, 200]:
        segments.append(generate_tone(freq, 0.5))
        segments.append(generate_silence(1.0))
    # Pad to ~5s
    remaining = DURATION - sum(len(s) for s in segments) / SAMPLE_RATE
    if remaining > 0:
        segments.append(generate_silence(remaining))
    audio_003 = np.concatenate(segments)
    save_wav("participant_003.wav", audio_003)

    print(f"\nDone! Generated 3 dummy WAV files in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
