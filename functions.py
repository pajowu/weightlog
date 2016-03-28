import os
from simplecrypt import encrypt, decrypt
import json
import base64


def save_weights(weights, weightfilename, password):
	weights.sort(key=lambda x: x['time'])
	with open(weightfilename, "w") as weightfile:
		ciphertext = encrypt(password, json.dumps(weights))
		data = base64.b64encode(ciphertext).decode("utf-8")
		weightfile.write(data+"\n")


def load_weights(weightfilename, password):
	weights = []
	if os.path.isfile(weightfilename):
		with open(weightfilename, 'r') as weightfile:
			data = base64.b64decode(weightfile.read())
			weight = decrypt(password, data).decode("utf-8")
			weights = json.loads(weight)
	return weights


def old_load_weights(weightfilename, password):
	weights = []
	if os.path.isfile(weightfilename):
		with open(weightfilename, 'r') as weightfile:
			for line in weightfile:
				data = base64.b64decode(line)
				weight = decrypt(password, data).decode("utf-8")
				weight = json.loads(weight)
				weights.append(weight)
	return weights
