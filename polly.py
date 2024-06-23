"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

session = Session(profile_name="adminuser")
polly = session.client("polly")

phonemes = [
    "b",
    "d",
    "f",
    "ɣ",
    "ɦ",
    "j",
    "k",
    "l",
    "m",
    "n",
    "ŋ",
    "p",
    "r",
    "s",
    "t",
    "v",
    "ʋ",
    "x",
    "z",
    "t͡ɕ",
    "ɡ",
    "d͡ʑ",
    "ɱ",
    "ɲ",
    "ɕ",
    "ʑ",
    "ʔ",
    "ɑ",
    "ɛ",
    "ɪ",
    "ɔ",
    "ʏ",
    "aː",
    "eː",
    "ə",
    "i",
    "oː",
    "y",
    "øː",
    "u",
    "ɑi",
    "aːi",
    "ʌu",
    "ɛi",
    "eːu",
    "iu",
    "ɔi",
    "oːi",
    "œy",
    "ui",
    "yu",
    "ɛː",
    "iː",
    "ɔː",
    "œː",
    "uː",
    "yː",
    "ɑ̃ː",
    "ɛ̃ː",
    "ɔ̃ː"
]

for phoneme in phonemes:
    try:
        response = polly.synthesize_speech(TextType="ssml", Text=f'<speak><phoneme alphabet="ipa" ph="{phoneme}"></phoneme></speak>', OutputFormat="mp3", VoiceId="Lotte")
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join("outputs", f'{phoneme}.mp3')

            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)

    else:
        print("Could not stream audio")
        sys.exit(-1)
