import os
import urllib.request
import re

if not os.path.exists("the-verdict.txt"):
  url = ("https://raw.githubusercontent.com/rasbt/"
           "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
           "the-verdict.txt")
  file_path = "the-verdict.txt"
  urllib.request.urlretrieve(url, file_path)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

#print(f"Total Number of characters: {len(raw_text)}") #20479
preprocessed = re.split(r'([,.;:?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
# print(preprocessed[:30])
# print(len(preprocessed)) #4690

all_words = sorted(set(preprocessed)) #remove duplicates and sort
vocab_size = len(all_words)
#print(vocab_size) 1130

vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

