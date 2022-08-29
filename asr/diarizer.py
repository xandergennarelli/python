from pyannote.audio import Pipeline
from pydub import AudioSegment
from pathlib import Path
import json, sys

RESOURCES_PATH = "/home/xander/deve/python/asr/resources/"
TMP_PATH = "/home/xander/deve/python/asr/tmp/"
CLIPS_PATH = TMP_PATH + "clips/"

class FileNameError(Exception):
    pass


def diarize(fileName):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

    diarization = pipeline(RESOURCES_PATH + fileName)

    segments = list()
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append((speaker, round(turn.start * 1000), round(turn.end * 1000))) # appends a tuple containing the segment's info

    return segments


def divide(fileName, segments):
    sourcePath = RESOURCES_PATH + fileName
    audio = AudioSegment.from_file(sourcePath)

    dataList = list()
    header = {
        "source_path": sourcePath,
        "source_name": sourcePath[sourcePath.rfind("/"):sourcePath.rfind(".")],
        "source_format": sourcePath[sourcePath.rfind(".")+1:],
        "segments": len(segments)
    }
    dataList.append(header)

    for i, segment in enumerate(segments):
        segPath = CLIPS_PATH + str(i) + "_" + segment[0] + "_" + fileName

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


def toJson(list):
    with open(TMP_PATH + list[0]["source_name"] + "-doc.json", "w") as file:
        json.dump(list, file, indent=4)


def main():
    try:
        fileName = ""

        if sys.argv[1] == "-n": fileName = sys.argv[2]
        if not Path(RESOURCES_PATH + fileName).is_file(): raise FileNameError(fileName)
    
        segments = diarize(fileName)

        dataList = divide(fileName, segments)

        toJson(dataList)

    except FileNameError:
        print("ERROR: Bad or no file name.")


if __name__ == "__main__": main()