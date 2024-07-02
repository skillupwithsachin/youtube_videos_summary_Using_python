#Import Libraries

from pytube import extract
from heapq import nlargest
from youtube_transcript_api import YouTubeTranscriptApi
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# Get ID Of Youtube Video

url = 'https://www.youtube.com/watch?v=DhkjfTTp_e0&t=1395s'
video_id = extract.video_id(url)
video_id

# Get Transcript of Video

transcript = YouTubeTranscriptApi.get_transcript(video_id)
text = ""
for elem in transcript:
    text = text + " " + elem["text"]
text

#Get All Available Sentences

nlp = spacy.load('en_core_web_sm')
document = nlp(text)
for sentence in document.sents:
    print(sentence.text)

#Get All Tokens from Document

tokens = [token.text for token in document]
tokens

#Calculate the frequency of tokens

word_frequencies = {}
for word in document:
    text = word.text.lower()
    if text not in list(STOP_WORDS) and text not in punctuation:
        if word.text not in word_frequencies.keys():
            word_frequencies[word.text] = 1
        else:
            word_frequencies[word.text] += 1
word_frequencies

#Normalize the frequency of tokens

max_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency
word_frequencies

#Calculate the Score of Sentences

sentence_tokens = [sentence for sentence in document.sents]
sentence_score = {}
for sentence in sentence_tokens:
    for word in sentence:
        if word.text.lower() in word_frequencies.keys():
            if sentence not in sentence_score.keys():
                sentence_score[sentence] = word_frequencies[word.text.lower()]
            else:
                sentence_score[sentence] += word_frequencies[word.text.lower()]
sentence_score

#Generate the Summmary

select_length = int(len(sentence_tokens) * 0.3)
summary = nlargest(select_length, sentence_score, key = sentence_score.get)
final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
summary
