# Podcast Transcripts

## Based on Andrei Karpathy's [LexiCap](https://karpathy.ai/lexicap/)

1. First we get all the episodes in the [playlist](https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4) (ty [youtubesearchpython](https://pypi.org/project/youtube-search-python/)), see their docs.
2. Then we download the audio for all of them (ty [yt-dlp](https://github.com/yt-dlp/yt-dlp)): `yt-dlp -x --audio-format mp3 -o {mp3_file} -- {youtube_video_id}`
3. Then we transcribe them (ty [OpenAI Whisper](https://github.com/openai/whisper)): `whisper --language en --model large -o {out_dir} -- {mp3_file}`
4. Download the raw captions data as a zip file [here](https://karpathy.ai/lexicap/data.zip).