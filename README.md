# generate_python_videos_using_python

In this project, you’ll use Python modules to generate the summary of a YouTube video. A Jupyter Notebook has been provided in the /usercode directory. You can open the Solution.ipynb file from the directory tree of VS Code.

#Import Modules

In this task, you’ll import the necessary modules for this project. To begin generating a summary from a video, import the following modules:

pytube: This module will be used to interact with YouTube using the video’s URL.
youtube_transcript_api: This module will be used to get the transcript of the video.
spacy: This module will be used to build the NLP model.
heapq: This module will be used to generate a summary from the tokenized sentences.

#Get ID of Youtube Video

After importing all of the necessary modules, obtain the ID of the YouTube video.

Use the extract library available in the pytube module to get the ID of the YouTube video using its URL.

#Get a Transcript of the Video

After getting the video’s ID, obtain the transcript of the video. To complete this task, perform the following steps:

Get the transcript of the YouTube video using YouTubeTranscriptAPI. This will return a list of dictionary values containing a timeline and text.
Retrieve all the text into a new variable.

# Get All Available Sentences

After successfully converting the video to text, break all the text into all available sentences. To complete this task, perform the following steps:

Load the en_core_web_sm model from spaCy.
Get all sentences using natural language processing.

#Get All Tokens from Document

In this task, obtain all the available tokens in the document. To complete this task, use a loop to iterate through the document and add all the tokens to a list.

#Calculate the frequency of tokens 

After obtaining all the tokens from the document, calculate the frequency of each token available in the document. To complete this task, perform the following steps:

Create a dictionary containing the tokens as keys and frequencies as values against each key.
Use a loop to iterate through all the tokens from the document.
If the token is not a punctuation or stop word, then increase its frequency count.

#Normalize the frequency of tokens

After getting the frequency of each token, normalize the frequencies for better accuracy. To complete this task, perform the following steps:

Get the word with the maximum frequency in the document.
Divide each frequency with the maximum frequency to normalize the frequencies.

#Calculate the Score of Sentences

After normalizing the frequencies of each word, calculate the score of each sentence available in the document. To complete this task, perform the following steps:

Get all sentences from the document.
Create a dictionary to store the sentences as keys and scores as values.
Iterate through all of the sentences in the document and perform the following steps:
Iterate through all words of the sentence.
If the word is available in the word_frequencies, add the frequency of that word to the sentence.

#Generate the Summary

After obtaining the normalized score of each sentence, generate the summary of the actual document. To complete this task, perform the following steps:

Get the 30% sentences with the maximum score.
Use these 30% sentences to get the summary of the actual text.
Note: These will be the most important sentences in the document.

Combine all the sentences to get the summary of the document.



