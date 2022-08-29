from pyannote.audio import Pipeline
from pydub import AudioSegment
from pathlib import Path
import json

RESOURCE_PATH = "resources/"

def diarize(fileName):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

    diarization = pipeline(RESOURCE_PATH + fileName)

    segments = list()
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append((speaker, round(turn.start * 1000), round(turn.end * 1000))) # appends a tuple containing the segment's info

    return segments

def splitAudioFile(fileName, segments):
    sourcePath = RESOURCE_PATH + fileName
    audio = AudioSegment.from_file(sourcePath)

    with open(sourcepath[:sourcePath.rfind(".")] + ".json", "w") as file:
        for i, segment in enumerated(segments):
            segPath = RESOURCE_PATH + str(i) + "_" + segment[0] + "_" + fileName

            clipInfo = {
                "sourcename": fileName,
                "speaker": segment[0],
                "start": segment[1],
                "end": segment[2],
                "path": segPath
            }

            clip = audio[clipInfo["start"]:clipInfo["end"]]
            clip.export(segPath)

            clipInfo_json = json.dumps(clipInfo, indent=4)
            file.write(clipInfo_json)

    # is this done?

def main():
    fileName = ""
    try:
        if sys.args[1] == "-n": fileName = sys.args[2]

        if not Path(RESOURCE_PATH + fileName).is_file(): raise NameError(fileName)
    except NameError:
        print("ERROR: Bad or no file name.")

    segments = diarize(fileName)

    splitAudioFile(fileName, segments)



if __name__ == "__main__": main()
# use segments to break up audio file