# Youtube Video Transcripts

Transcribe and capture additional information from any Youtube video and playlist, which includes many of your favorite podcasts!  

## Description

The scripts utilize [pytube](https://github.com/pytube/pytube) to download the audio from Youtube videos and OpenAI's [whisper](https://github.com/openai/whisper) to transcribe the downloaded videos, writing the text to Markdown files. Notebooks built on top of the scraping allow for further analyses of the content of the videos. 

## Quickstart

This guide will show you the most basic usage of the library.

### Dependencies

1. To start, make sure you open up a Terminal (Mac) or Command Prompt (Windows) window and [create a fresh Anaconda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) (i.e. `conda create env transcripts`). 
2. Activate the new environment with: `conda activate transcripts`
3. Install the following dependencies
> * [pytube](https://github.com/pytube/pytube): 
>   * `python -m pip install pytube`
> * [whisper](https://pypi.org/project/openai-whisper/): 
>   * `pip install openai-whisper`

### Using video_transcript from command line

Run the script by calling `python video_transcript.py --url "<INSERT/YOUTUBE/URL/HERE>"`. If the url is a playlist, the script will be able to recognize and transcribe all videos from the playlist. 

### Using video_transcript from a notebook

Open [video_transcript.ipynb](video_transcript.ipynb), making sure the correct kernel is set to run the environment with the above dependencies.

## Examples

### Single Video

**1961: Aldous Huxley on the power of TECHNOLOGY! ([link](https://www.youtube.com/watch?v=ZCOGFSwrGNc))**

To transcribe the historic 1961 speech by Aldous Huxley on the increasing use and influence of technology on society:

```
conda activate <your/environment/name>
python video_transcript.py --url "https://www.youtube.com/watch?v=ZCOGFSwrGNc"
```

The output is as follows:
```
Loading Whisper Model: medium
  Model Loaded.
Number of Videos to Transcribe: 1
  0%|                                                                                                  | 0/1 [00:00<?, ?it/s]Creating directory: _Transcripts\BBC Archive
Downloading video from: https://www.youtube.com/watch?v=ZCOGFSwrGNc
  Video downloaded to youtube_20240523_234743.mp4
Video Title: 1961: Aldous Huxley on the power of TECHNOLOGY! | In Conversation | Classic Interviews | BBC Archive
  Author: BBC Archive
  Date:   June 23, 2023
  Length: 7.88m
  Views:  50143
Transcribing Video
  Transcription Time: 1.33 min
  Segments Transcribed: 77
Writing transcript to file
Video file deleted: youtube_20240523_234743.mp4
100%|██████████████████████████████████████████████████████████████████████████████████████████| 1/1 [01:25<00:00, 85.53s/it]
Transcription Complete
  Number of Videos Transcribed: 1
```

Within [_Transcripts](_Transcripts), you'll find a folder within the newly-created BBC Archive folder containing the following transcript captured in the markdown:
> *  In your Brave New World Revisited, which was published about two years ago,
> *  you did claim that much of what you forecast had come true.
> *  I mean, for example, the use of drugs and this instance of people having their thoughts directed
> *  while they were asleep through music being played or messages being played through their pillows and so on.
> *  In which societies do you think that most of what you forecast has mostly come true?
> *  I mean, is it in America, Britain, Russia, China?
> *  Well, it seems to me this is not so much...
> *  You can't say that it's a question of national peculiarities or even entirely of political peculiarities.
> *  I mean, I think when the technological and applied scientific means are developed, they just tend to be used.
> ...  

### Playlists

**The New York Times Daily Podcast ([link](https://www.youtube.com/playlist?list=PLdMrbgYfVl-s16D_iT2BJCJ90pWtTO1A4))**

```
python video_transcript.py --url "https://www.youtube.com/playlist?list=PLdMrbgYfVl-s16D_iT2BJCJ90pWtTO1A4"
```

**Bill Simmons NBA Podcast ([link](https://www.youtube.com/playlist?list=PLYHjB_Comy8RhgQ_JNUbVNEQ6gc4iolhN))**
```
python vide-transcript.py --url "https://www.youtube.com/playlist?list=PLYHjB_Comy8RhgQ_JNUbVNEQ6gc4iolhN"
```

### Common Pytube Errors
#### AttributeError: 'NoneType' object has no attribute 'span'
Caused by an issue in cypher. Navigate to wherever pytube is installed, and on line 411 in update `transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)` to `transform_plan_raw = js`. 

For more information, see: https://github.com/pytube/pytube/issues/1498
#### pytube.exceptions.AgeRestrictedError
Some playlists may result in an error due to age restriction (even ones you wouldn't expect!). To solve, navigate to [video_transcript.py](video_transcript.py) and include:
```
  from pytube.innertube import _default_clients
  _default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"].
```
For more information, see: https://github.com/pytube/pytube/issues/1712.