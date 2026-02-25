# Dummy Audio Data

This directory contains **synthetic `.wav` files** for testing the analysis notebooks.

These files are **NOT** real DAIC-WOZ interview recordings. They are generated
by `generate_dummy_audio.py` and contain simple sine-wave tones and silence to
simulate speech-like patterns.

## Generate Dummy Audio

```bash
python generate_dummy_audio.py
```

This creates 3 files:
- `participant_001.wav` — steady tone (simulates monotone speech)
- `participant_002.wav` — varied tones (simulates expressive speech)
- `participant_003.wav` — tone with long pauses (simulates hesitant speech)
