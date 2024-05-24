# Podcast Transcripts

Transcribe and capture additional information from any Youtube video and playlist.  

## Description

The scripts utilize [pytube](https://github.com/pytube/pytube) to download the audio from Youtube videos and OpenAI's [whisper](https://github.com/openai/whisper) to transcribe the downloaded videos, writing the text to Markdown. Notebooks built on top of the scraping allow for further analyses of the content of the videos. 

## Quickstart

This guide will show you the most basic usage of the library.

### Dependencies

### Using video_transcript from command line

Run the script by calling `python video_transcript.py --url "<INSERT/YOUTUBE/URL/HERE>"`. If the url is a playlist, the script will be able to recognize and transcribe all videos from the playlist. 

### Using video_transcript from a notebook

Open [video_transcript.ipynb](video_transcript.ipynb), making sure the correct kernel is set to run the environment with the above dependencies.

## Examples


#### The New York Times Daily Podcast ([link](https://www.youtube.com/playlist?list=PLdMrbgYfVl-s16D_iT2BJCJ90pWtTO1A4))
```
python video_transcript.py --url "https://www.youtube.com/playlist?list=PLdMrbgYfVl-s16D_iT2BJCJ90pWtTO1A4"
```

#### Bill Simmons NBA Podcast ([link](https://www.youtube.com/playlist?list=PLYHjB_Comy8RhgQ_JNUbVNEQ6gc4iolhN))
```
python vide-transcript.py --url "https://www.youtube.com/playlist?list=PLYHjB_Comy8RhgQ_JNUbVNEQ6gc4iolhN"
```

### Common Pytube Errors
1. AttributeError: 'NoneType' object has no attribute 'span'
> * Caused by an issue in cypher. Navigate to wherever pytube is installed, and on line 411 in update `transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)` to `transform_plan_raw = js`. For more information, see: https://github.com/pytube/pytube/issues/1498
2. pytube.exceptions.AgeRestrictedError
> * Some playlists may result in an error due to age restriction (even ones you wouldn't expect!). To solve, navigate to [video_transcript.py](video_transcript.py) and include
> ```from pytube.innertube import _default_clients
     _default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]. 
> For more information, see: https://github.com/pytube/pytube/issues/1712.