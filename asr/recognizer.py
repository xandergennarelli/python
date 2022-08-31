from stt import Model
import wave, numpy, json

MODEL_PATH = "/home/xander/deve/python/asr/resources/model.tflite"

def transcribe():
	model = Model(MODEL_PATH)

	sample_rate = model.sampleRate()

	# for clip in clips
		file = wave.open(clipPath, "rb")

		audio = numpy.frombuffer(file.readframes(file.getnframes()), numpy.int16)

		transcript = model.stt(audio)

		# add transcript to json file


if __name__ == "__main__": 
	main()
