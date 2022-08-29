from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

diarization = pipeline("resources/sample.wav")

segments = list()
for turn, _, speaker in diarization.itertracks(yield_label=True):
    # print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
    segments.append((turn.start, turn.end, speaker))

# use segments to break up audio file