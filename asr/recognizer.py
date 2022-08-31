from stt import Model
from pathlib import Path
import wave, numpy, json, sys
from diarizer import toJson, FileError

RESOURCES_PATH = "/home/xander/deve/python/asr/resources/"
TMP_PATH = "/home/xander/deve/python/asr/tmp/"
MODEL_PATH = "/home/xander/deve/python/asr/resources/model.tflite"

def transcribe(data_path):
	model = Model(MODEL_PATH)
	sample_rate = model.sampleRate()

	try:
		with open(data_path) as dataFile:
			dataList = json.load(dataFile)

		if not dataList:
			raise FileError(data_path)
	except FileError:
		print("ERROR: Json file not found.")

	for clip in dataList[1:]:
		file = wave.open(clip["segment_path"], "rb")

		audioArray = numpy.frombuffer(file.readframes(file.getnframes()), numpy.int16)

		transcript = model.stt(audioArray)

		clip["transcript"] = transcript

	return dataList


def format():
	print("todo")


def main():
    try:
        dataPath = ""

        if sys.argv[1] == "-n": dataPath = TMP_PATH + sys.argv[2]
        if not Path(dataPath).is_file(): raise FileError(dataPath)

        dataList = transcribe(dataPath)

        toJson(dataList)

    except FileError:
        print("ERROR: Bad or no file name.")


if __name__ == "__main__": 
    main()
