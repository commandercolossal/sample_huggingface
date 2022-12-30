from transformers import pipeline

import torch
import torch.nn.functional as F


classifier = pipeline("sentiment-analysis")
results = classifier("We are very happy to show you this library")
print(res)

print('Hello')