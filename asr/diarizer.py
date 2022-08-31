from pyannote.audio import Pipeline
from pydub import AudioSegment
from pathlib import Path
import json, sys

RESOURCES_PATH = "/home/xander/deve/python/asr/resources/"
TMP_PATH = "/home/xander/deve/python/asr/tmp/"
CLIPS_PATH = TMP_PATH + "clips/"
MODEL_SAMPLE_RATE = 16000 # make this not hard coded, make these all not hardcoded? ^^^

class FileError(Exception):
    pass


def correctAudio(audio):
    if audio.frame_rate != MODEL_SAMPLE_RATE:
        audio = audio.set_frame_rate(MODEL_SAMPLE_RATE)

    if audio.channels != 1:
        audio = audio.set_channels(1)

    return audio


def diarize(sourcePath):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

    diarization = pipeline(sourcePath)

    segments = list()
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append((speaker, round(turn.start * 1000), round(turn.end * 1000))) # appends a tuple containing the segment's info

    return segments


def divide(sourcePath, segments):
    sourceName = sourcePath[sourcePath.rfind("/")+1:sourcePath.rfind(".")]
    sourceFormat = sourcePath[sourcePath.rfind(".")+1:]
    audio = correctAudio(AudioSegment.from_file(sourcePath))

    dataList = list()
    header = {
        "source_path": sourcePath,
        "source_name": sourceName,
        "source_format": sourceFormat,
        "segments": len(segments)
    }
    dataList.append(header)

    for i, segment in enumerate(segments):      # @TODO: maybe use uuid?
        segPath = CLIPS_PATH + str(i) + "_" + segment[0] + "_" + sourceName + "." + sourceFormat
        clipData = {
            "segment": i,
            "segment_path": segPath,
            "speaker": segment[0],
            "start": segment[1],
            "end": segment[2],
            "path": segPath,
            "transcript": ""
        }

        clip = audio[clipData["start"]:clipData["end"]]
        clip.export(segPath, format="wav")

        dataList.append(clipData)

    return dataList


def toJson(dataList):
    with open(TMP_PATH + dataList[0]["source_name"] + "-doc.json", "w") as file:
        json.dump(dataList, file, indent=4)


def main():
    try:
        sourcePath = ""

        if sys.argv[1] == "-n": sourcePath = RESOURCES_PATH + sys.argv[2]
        if not Path(sourcePath).is_file(): raise FileError(sourcePath)
    
        segments = diarize(sourcePath)

        dataList = divide(sourcePath, segments)

        toJson(dataList)

    except FileError:
        print("ERROR: Bad or no file name.")


if __name__ == "__main__": 
    main()
