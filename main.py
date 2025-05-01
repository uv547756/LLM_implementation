import os
import urllib.request
import re

class tokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

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

tokenize = tokenizer(vocab)
text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenize.encode(text)
print(ids)

print(tokenize.decode(ids))
