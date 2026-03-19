from google import genai
import glob
from dotenv import load_dotenv
import os

# get api key from .env and set GEMINI_API_KEY environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=api_key)

# read through transcript files and generate a summary, list of unique points/topics discused with start and stop timestamps.
transcripts = glob.glob("/Users/hussain/code/AIML/transcripts/*.txt")
# sort transcripts naturally
transcripts.sort(key=lambda x: int(x.split(".")[0]))

prompt = """Read through the transcript and generate a summary, list of unique points/topics discused with start and stop timestamps."""

for transcript in transcripts:
    with open(transcript, "r") as f:
        transcript_text = f.read()
    response = client.models.generate_content(
        model="gemini-3.1-pro-preview", contents=transcript_text + "\n\n" + prompt
    )
    with open(transcript + ".summary", "w") as f:
        f.write(response.text)  
    print(f"Generated summary for {transcript}")