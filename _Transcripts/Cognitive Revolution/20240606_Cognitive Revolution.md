---
Date Generated: June 06, 2024
Transcription Model: whisper medium 20231117
Length: 4207s
Video Keywords: []
Video Views: 148
Video Rating: None
Video Description: Join us for an engaging chat with Logan Kilpatrick where we discuss the latest AI developments and Google's strategy in pushing the boundaries of artificial intelligence. Learn about the competitive state of AI, the groundbreaking Gemini 1.5 Flash model, and get a glimpse into the future of AI fine-tuning. Gain insights on Google DeepMind's research and its impact, the differences between various Google AI products, and debunking AI rumors. Whether you're an AI enthusiast or a professional in the field, this conversation with an AI industry insider offers valuable perspectives on applying AI in business and understanding the rapid advancements in this dynamic sector.

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Recommended Podcast - The Riff with Byrne Hobart
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

CHAPTERS:
(00:00:00) Introduction
(00:07:29) Google culture
(00:11:01) DeepMind and Google
(00:15:49) Native multimodality
(00:18:17) Sponsors: Oracle | Brave
(00:20:24) What to focus on
(00:23:40) LMSYS leaderboard
(00:27:46) Rumors
(00:36:32) AI is too cheap to meter
(00:39:17) Open AI Assistant
(00:40:14) Sponsors: Squad | Omneky
(00:41:59) Dogfooding
(00:48:58) AI Studio
(00:52:28) Native Multimodal
(00:55:57) VideoFX
(01:01:09) Competition
(01:04:07) What to do with AGI
(01:09:19) Closing
---

# Inside Google’s AI Studio with Logan Kilpatrick
**Cognitive Revolution:** [June 06, 2024](https://www.youtube.com/watch?v=CD1ku-YnoIE)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm excited to once again be speaking with
*  Logan Kilpatrick, former lead developer relations lead at OpenAI and currently product manager at
*  Google, where he's responsible for Google's playground-like AI Studio product.
*  Logan has become one of my favorite people in the AI space. He is extremely hardworking,
*  very earnest, and always inclined to be helpful. After what was very clearly a super intense period
*  for him leading up to Google I.O., he managed to fit this recording in before dinner with his family,
*  which I very much appreciated. We covered a lot of ground in just over an hour, including Logan's
*  first impressions of Google's culture, how hard the team at Google is working from top to bottom,
*  and how Google is balancing the need to share information across teams internally while also
*  protecting its most valuable intellectual property. We discussed how quickly Google DeepMind is
*  producing research advances, how much of a challenge it is for Google product teams to keep up,
*  and how important that makes application developers to Google's overall AI deployment strategy.
*  We also got into the incredible capabilities of Google's Gemini 1.5 Flash model, which significantly
*  outperforms the original GPT-4 on head-to-head user comparisons while offering 100x longer context
*  window at just 1 to 2 percent of the price per token. Really an incredible advance in just a year.
*  The distinction between the AI Studio, Gemini API, and Google's Vertex products, and a look at the
*  roadmap, including fine-tuning for Flash, which, depending on what else happens between now and
*  then, would make Flash the most powerful model available for fine-tuning anywhere in the world.
*  Logan also gave me a pointer on how few of the AI rumors that circulate online are actually true.
*  And finally, we discussed the state of competition in AI, both between frontier labs
*  and between platforms like Google and the startups building on their APIs.
*  I always appreciate Logan's candid insider perspective, and I think this conversation
*  is really self-recommending for anyone who's building AI-powered applications,
*  or simply interested in the state of play at the world's most important AI companies.
*  As a quick reminder, I am considering starting a super-niche cognitive revolution jobs board.
*  When I mentioned this in the recent scouting report episode, I got a half a dozen resumes in,
*  which was awesome. Now I'm wondering if I skimmed everything off the top, or if there's still a lot
*  more interest out there. If you'd be interested in an AI engineer or an AI advisor role,
*  responsible for helping medium-sized businesses apply AI in very practical, but often very
*  idiosyncratic ways, please do be in touch. And if you're part of a business that needs that sort
*  of help, feel free to ping me about that as well. As always, we appreciate it when you share the
*  show with friends, and once again, we humbly ask for your reviews on Apple, podcasts, or Spotify,
*  or just a comment on YouTube. One of the most common comments that we get on our YouTube
*  channel actually is simply that we deserve more subscribers and views. So thank you in advance
*  for helping us to spread the word. With that, I hope you enjoy my conversation with Google's
*  Logan Kilpatrick. Logan Kilpatrick, now of Google, welcome back to the cognitive revolution.
*  Thank you. I appreciate it.
*  Lots of cover. I was just out at Google I.O. at your invitation. Thank you for that. I think
*  the race is officially on, that's safe to say. I wanted to just take you through a little bit
*  of your experience with Google. Obviously, you've had one of the few people on planet Earth that
*  has seen both of the 1A or 1A and 1B AI leaders from the inside, so just to get your perspective
*  on that. And then honestly, I just want to do a pretty down-the-fair way run through of all the
*  stuff that was launched at I.O., all the stuff that you're excited about, help developers get
*  oriented toward the platform. As you well know, there's some complexity issues there historically
*  that I think you're working to help overcome. And then I hear there's some cool stuff, maybe more
*  stuff coming soon too. So maybe we can preview that a little bit at the end if we can time it
*  just right. I love it. I'm super excited. Let's dive in. All right, cool. So first of all, you were
*  not on the beach for long. It was a pretty short timeframe between your departure from OpenAI and
*  taking up at Google. Is there an inside story of how that happened? I got the sense that this was
*  not like a normal Google hiring process, which from what I've understood can often stretch on
*  for months, but certainly didn't seem to be the case for you. Yeah. When I left OpenAI, a bunch of
*  folks from Google had reached out and I started having conversations with Matt Velasso, who's now
*  my manager, and Josh Woodward, who leads the Google Labs team and gave a bunch of the awesome
*  I.O. keynotes. And it's funny that you say process being quick. Honestly for me, it felt slow. I was
*  like, I'm ready to move. I'm burning daylight here. The race is happening. But ultimately,
*  to Google's credit, and it's not clear to me that much of this is visible in the world
*  today, but I think the team is really making the order of magnitude of bet on everything that's
*  happening in AI right now that you would want to see. And I think hopefully that was clear from the
*  releases at I.O. And I felt that in my hiring process. I felt that level of urgency, just
*  in the way in conversations with people. It's exactly what I wanted to see. That's just who I
*  am as a person is like, I would like to do things and I would like to do them as soon as they can
*  be done. So it was exciting to see that from Google. Yeah. I've got a little minor story that
*  supports that myself actually, when Gemini 1.5 was initially announced and put into preview mode for
*  early testers, I was not initially on that list, but I sent Jeff Dean a DM on Twitter on a Saturday
*  morning, my time, Eastern time, it was like 1130. I think I sent the message and within an hour,
*  he had responded to me, said that he would get it done, sent an email, copied Josh Woodward actually,
*  who then in turn copied someone else. And within 24 hours from a Saturday morning to a Sunday
*  morning, I had the access and was testing the million tokens. So I definitely took away from
*  that, that there is no level of seniority at Google at this point, that people are not really
*  locked in and willing to roll up their sleeves and make things happen. And I'm under no delusions
*  about my own level of importance to see that kind of responsiveness and just engagement from folks
*  who've been there a long time, particularly in the case of Jeff Dean. I actually don't know how long
*  Josh has been there, but I know they're both senior folks and Jeff certainly could be excused
*  for not responding to fan mail like that. But I was pretty impressed with his engagement and how
*  quickly that was turned around. Yeah, Josh has been at Google for 15 years. He actually started as an
*  intern and now leads the Google labs team as the VP and is like an incredible journey, but exactly
*  what you would expect from somebody who's gone through that. And I think in many ways, like his
*  team, again, for folks who don't have contacts, his team is actually the team that built the Gemini
*  API and AI Studio. And it's now Matt Filosso's team, who I'm a part of at Google, who's sort of
*  inheriting these products as we scale it beyond a million developers. So it's been hard to match
*  Josh and his team's sense of urgency around this stuff, but it is also incredibly inspiring.
*  Interested in what else has stood out to you about Google culture so far, one tweet that you put out
*  in your first few weeks there that I thought was remarkable was a comment that it was something to
*  the effect of one thing that's nice about Google's culture is that there's a lot of visibility into
*  what's coming and that makes your job easier. Obviously, there's some hint of implied contrast
*  there. To whatever degree you want to go to that, you can go into it. And if not, then just tell me
*  how the culture has landed for you as you've ramped up at Google. Yeah, I think at a really
*  high level, the practical reality at OpenAI, and I think maybe you can get Sam on and he can
*  give his perspective. And I think for very real reasons, the separation between research at OpenAI
*  and everyone else at OpenAI is a very strong force. When I joined OpenAI, that wasn't the case. I
*  think this is actually one of the pieces of the culture that a lot of folks appreciate, which is
*  you can just drop into a research meeting and hear about what was happening and learn about
*  how the technology itself was progressing right around post-GPT4, even with chatGPT and all that
*  stuff. That very quickly started to change and there was a bunch of legitimate organizational
*  infrastructure, etc, etc, things that changed to put very strong divisions in place between these
*  teams. And I'm not delusional in the sense of Google obviously has a strong vested interest
*  in protecting its intellectual property. So it's not even that there are mitigations and protections
*  in place and there are clear boundaries and roadblocks put in place, but it still feels,
*  at least for me at Google, in spite of that, people are still very willing to collaborate.
*  And I actually think a lot of it has to do with the DeepMind team itself, just cares about
*  developers. They want to see, and part of this from their perspective, developers are one of
*  the primary surface areas for them to bring this technology to the world. I know partially some of
*  it comes available through the first party product. I think the first party product,
*  the Gemini product, which is incredible and a bunch of folks are using, just has a different
*  feeling about it comparatively against how, at least in my experience, teams felt about chatGPT.
*  I think a lot of people at OpenAI was like, well, chatGPT is so successful, let's just
*  essentially put our eggs in that basket. And we want to work closely with those teams to the point
*  yeah, wanting to collaborate really deeply with the chatGPT teams. And not always, at least from
*  my perspective, wanting the deep collaboration with the API and the developer teams. And obviously,
*  there was still a collaboration. So it's hard to say that it didn't exist, but it really does feel
*  like the DeepMind team is like, developers are incredibly important. They're on the ground
*  giving us the feedback about how to make the developer product better. Just this weekend,
*  got a bunch of pings from an incredibly well-written doc from Susan on the DeepMind
*  team. And it was about all the things, the challenges of getting started with Flash and
*  what we need to do to improve that. And it was like, clearly this person and also broadly this
*  team and people really care about making this technology accessible to the world. And it was
*  awesome to see that. And then we literally turned around in 24 hours and made a bunch of changes and
*  hopefully improved that experience. So all that's to say, at least where I am right now feels like
*  a culture that is going to help me as somebody who's tried to make products for developers,
*  be more effective at my job. And ultimately, that's what it comes down to. I think there's
*  very real realities of why you would want to have things either way. But I feel like I'm able to
*  build the right things for developers because I have a collaboration with the DeepMind team,
*  which is important to me. Cool. Yeah. It's been an interesting trajectory to watch
*  DeepMind finally really consummate the merger with Google. And of course, I've been on the outside of
*  that. But the commentary, even from Demis, I thought was quite revealing where he was just like,
*  look, we're getting from the point where this has been primarily a research problem to now where
*  it's still a research problem, but also very much an engineering problem. And it certainly seemed
*  like they came to this moment with a very realistic understanding that for this to go to the next
*  level, it was something that was going to have to work with the broader strength of Google beyond
*  the sort of research focus that DeepMind had obviously built in such strength over time.
*  I think this is one of the tension points now actually for us is like the DeepMind team is
*  doing such incredible work. It's like we're not rate limited on how much innovation is coming out
*  of DeepMind and like how important the new directions they're making from a modeling
*  standpoint are. It's really rate limited by can we build the right products around these things?
*  How do we thoughtfully put this technology in the hands of developers and also consumers through
*  all the one piece surface areas? And I think the DeepMind team is like chomping at the bit to get
*  this technology out to people. It is like now our job to actually do that work and stay in tandem
*  with them. And it's hard. Like they just have so many incredibly smart people doing incredibly
*  interesting things that yeah, I think we have our work cut out for us.
*  Yeah. Let the record show that I for one never doubted Google's strength, at least in the areas
*  where it counts most. If the inputs to AI are, which they are data, compute and algorithms,
*  then it always seemed to me quite clear that Google DeepMind had all three of those at the
*  highest size level. And certainly now we are seeing that. So it was at the conclusion of
*  the keynote, whatever the first day of IO, the count of the number of times that AI was said
*  revealed, and I believe it topped out at 121. A lot of different announcements there, both on
*  the developer facing side and the sort of integration across the entire horizontal suite
*  of Google products. For starters, what are the things that jump out to you most? I assume you
*  guys have some early use of the first party tool. So if there's anything there that you've had a
*  chance to go a little bit deeper, farther on, then the rest of us are interested to hear what you
*  think we should be excited about. And then obviously the API side is your bread and butter.
*  I think on the workspace side, the thing that continues to be the most valuable Gemini use
*  case for me, and it just works out of the box is there's a Gemini meeting note taker built directly
*  into Google Meet, and you just turn it on at the beginning of the call. It basically takes notes
*  of the whole conversation and summarizes everything for you. And then also specifically does a bunch
*  of action items and tags people. It's like one of the best workflows. I just do a single button
*  click. I get an email afterwards with the entire thing put together. I think this had already been
*  released prior to IO, but I'm sure it's going to get better with the new models that are not
*  powering that experience. So that's been on the actual Google workspace slash all the different
*  tools that are available. The most useful thing I've also been experimenting with the travel
*  planning piece on the consumer side of I'm going to the Azores with my girlfriend and we were
*  trying to figure out like, what are we going to do? And what are all the different things? So again,
*  incredibly well designed and thoughtful. I just put in how long I was there, the dates,
*  found a bunch of stuff, gave me a travel itinerary. There was a button to export it to a Google Doc
*  that you could email it to someone. I was like, this is awesome. And again, that's what for me,
*  as a consumer, what I'm expecting from when I engage with Google's AI surface areas of like,
*  give me this full experience, like I'm integrated into this world, let me benefit from it. And I
*  think the email, the Google Docs, all those things is a great example of those integrations coming
*  together and actually providing a bunch of value. On the developer side, like Flash, we can talk
*  about Flash and Pro and more in a bit, but like those were the two most important things. And then
*  I'll give a special honorary mention for Gemini in Google Chrome. That seems incredibly interesting.
*  Again, there's billions of people who use Google Chrome. If you want to think about what the impact
*  of this technology is on the world, a lion's share of the impact is going to be had as by like those
*  types of distributions, which are super interesting to see Google pushing on. Yeah. Okay. So a couple
*  threads I'll put it in to come back to later. One is the meeting thing and just some of the
*  competitive dynamics that I see shaping up there. And then similarly for the travel planning,
*  although that one I think is more AI versus human competition as opposed to platform versus startup.
*  But let's just talk about the models a little bit first. For one thing, I am not entirely clear.
*  Maybe this is out there somewhere, but obviously a bit of a deluge of information. I wasn't quite
*  able to get total clarity on it. When Google speaks about natively multimodal models with the
*  current generation, the 1.5 generation of Gemini, can you give us a little bit more detail on what
*  natively multimodal means? Obviously we've seen OpenAI say, okay, this is all basically tokens in,
*  tokens out, regardless of whether it's text audio or image video token, whatever. I'm not even sure
*  on the video piece exactly how to be thinking about that for the OpenAI side either, but I'm
*  less clear on the Google side. Like, is this a single transformer that takes and generates all
*  these inputs or how native is this native multimodality now? Yeah, that's a good question.
*  I think the TLDR of this is you can put in whatever type of content you want and you can get
*  an output today only in text and not pay the cost from a developer perspective of having to route
*  things between multiple models. And I think that's the ethos of what it means from me on the
*  developer side of what it means to be natively multimodal is historically you would have to like
*  chain together a bunch of these requests. You'd have to pay the round trip compute or the round
*  trip latency time for every single call. You would have to like string those together. And essentially
*  it meant any multimodal use case was not feasible to do in a production setting because the latency
*  of doing many different calls strung together, whether it be audio, video, image combined with
*  some text was just not feasible. And now you take all of those things that you previously needed
*  four different models for and you can just do them with flash and do them with an incredible
*  amount of speed. I'll refer folks to the Gemini 1.5 technical report, which actually just got
*  released slightly after IO. It's like 150 pages. I don't think that it's talked about in depth,
*  like what it means to be natively multimodal, but we can ping Jeff Dean after this and see if maybe
*  we get a blog post from the DeepMind team about what it means to be natively multimodal. I'm not
*  sure, but I think it's a good question. I've heard other folks asking it. It's not clear if it's one
*  of those details that like, so we should really push to show the world how it works or if it's
*  like more of an implementation detail that the team is intentionally not revealing because there's
*  some secret sauce happening there. It's not clear to me personally which of those it is right now.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber eight by eight and Databricks Mosaic, take a free test drive of OCI
*  at oracle.com slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index.
*  An independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans collected
*  anonymously of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up to date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API. Yeah, I guess we'll be able to tell maybe a little bit
*  more over time just with things like does it pick up on intonation of audio? If there's like a
*  pipeline and it's transcribing audio and then feeding the text into the same kind of format
*  as regular text, then presumably like it wouldn't notice these things like the intonation in voices.
*  Whereas if we can get a different response or if it seems to understand the intonation,
*  then that would seem to imply sort of an early fusion type of strategy, which and I borrow that
*  term from a recent meta paper that just came out. It was like a lost in the shuffle of the big week
*  of OpenAI and Google's big announcements, but not to be entirely slept on because they're showing
*  that they're definitely not too far behind either and they are very much on the mindset to show their
*  work obviously. Nathan, I think this question about can the model understand variances in
*  people's voice and emotion and tone and stuff, I think it's actually a really good question.
*  I'll follow up. This had also come up a couple of times and I think this is an important thing to
*  make clear for developers because the actual use cases that you build depend on that on whether or
*  not the model understands that piece. So I'll follow up. My understanding is that it might and
*  it maybe is limited to certain contexts or certain aspects of that, but I'll follow up.
*  Okay, cool. Just in the interest of pruning the space of things that people need to keep track of
*  as well, is there anything that we should be thinking about like anything earlier than Gemini
*  1.5 on at this point or is Gemini 1 basically superseded? Yeah, almost. It is fully superseded
*  now with these new models. That was actually part of the Gemini 1.5 technical report is that
*  the Gemini 1.5 Pro model is now better across pretty much every axis that Gemini 1.0 Ultra was,
*  which was never made widely available to folks, I think partially because the team saw it was coming
*  with Gemini 1.5 Pro. So I would move my mental model to focus almost entirely on the 1.5 family.
*  So that's Flash and Pro right now. And those models seem to be pretty much better at everything
*  comparatively against any of the models we put out before. Yeah. And also it should be noted
*  pretty much the same is almost true across the entire universe of language models. The
*  LMSYS leaderboard just got updated today finally with Flash appearing on it for the first time.
*  And the new Pro models are now basically within the margin of error, maybe just a couple points
*  outside of the margin error of GPT-4.0 per the LMSYS leaderboard. And there are two 1.5 Pro models
*  there. One is called Gemini Advanced. Is that also available in the API like an online version?
*  That's only in the like Gemini Advanced UI experience. Is that right? Yeah, I think it's
*  mostly just there from a showcasing perspective of what that model is capable of. But yeah,
*  you definitely cannot access that via the API today. I'm interested to see if there ends up
*  being some use cases that folks come up with that make it seem like it is something that we would
*  maybe want to open up to people. But right now it is not accessible outside of the Gemini first
*  party product. Reading all of the docs and knowing with a little more clarity exactly what's going on
*  out of the millions of tokens of documentation would be the first place I would go. Honestly,
*  I think it's a fair question. I actually think this is my point of feedback that I've given to
*  the LMSYS team before, which is I do think they should make it more clear, like exactly what those
*  models are. Like having a model page, kind of like what Hugging Face does, honestly, where you can
*  give details, provide a model card. Right now when you click on the leaderboard, it just goes off to
*  some other thing. But I feel like it's in people's best interest to more fully document what
*  these things actually are on LMSYS. Yeah. Okay. Nevertheless, the two at the top are the same
*  model. One has a knowledge cutoff that's available via the API. The other one is online.
*  That's not available via the API, but is what you get when you go to use the Gemini advanced
*  product. And then it's not too many spots down the leaderboard and notably above Claude 3 Sonnet,
*  where Flash has just landed. And that is pretty impressive given the price point and also the
*  fact that both of these, both the Flash and the Pro model have the million token context window
*  with two million coming soon and talk of from 15 of infinite context. I wonder if you have any
*  perspective on this that's new. This is a bit of an aside, but obviously intellectual property is
*  like super valuable. We're in this general period of closing. I'm hearing multiple reports of
*  kind of less information sharing even within companies, which you sort of alluded to happening
*  in various ways. And then I see a paper like Infini Attention, if that's how they're pronouncing it,
*  that was out of DeepMind recently where they show a really elegant, it looks more like a state space
*  or a state space kind of equivalent where there's this like fixed size element that is still like
*  referred back to with attention, but is like constantly updated and can handle in theory,
*  like up to infinite attention. And then there's like the more recent sort of sliding window.
*  I'm surprised that something like that gets published. And I wonder if you have any
*  insight or perspective on why some things that still seem like they're like top notch IP are
*  coming out despite this sort of broader closing of sharing. It's an interesting question.
*  A couple of reactions. One, I have no specific knowledge about this individual paper broadly.
*  I would assume part of it is theater. I would assume part of it is wanting to give folks the
*  credit that they deserve for doing some of this work, which is like an important part of the
*  scientific process. I think part of it is again, on the scientific process side, like folks wanting
*  to get these ideas out. And again, I don't know for this specific paper if it's like, this thing
*  is verified and is like the clear path towards scaling to infinite context, or if it's more of
*  like, hey, here's an idea that might work. And it's intended to like foster conversation with
*  people in the ecosystem. I think there's a lot of reasons to publish stuff like that. And
*  strategically for DeepMind, like, again, they need to attract the world's talent. There's a lot of
*  academic talent that's out there that care about the stuff that's being published from a paper
*  perspective. So I think there is an economic reason why it might make sense to publish,
*  even if in some sense, you have to give up some discovery, and it's no longer a trade secret or
*  what have you. I think all of those things are at play. I would also not underestimate the value of
*  or the reality of like, what is actually new versus like, someone has already figured out and
*  like, they know someone else has figured this thing out based on what someone said or specifically
*  didn't say in another paper. So like, the calculated calculus on this could be that it's clear to the
*  DeepMind team that someone has already figured something else out that's very similar to this.
*  And even though they haven't said it in this very specific way, it's not actually brand new, or it
*  could be completely brand new. And they're like, this is the most incredible thing ever. We need
*  to share it with the world. I honestly don't know. But I think those are the things that I would
*  think through if I was in that position. Yeah, a lot of considerations, to say the least. I try not
*  to put too much stock into the rumor mill, but I had heard that the DeepMind team had some impressive
*  results with state space model type work internally and hadn't published it. And then
*  Mamba happened at the end of last year. And then maybe it was like, we might as well bring this
*  out. And I can also very well imagine that's not the best thing that Google has up its sleeve at
*  this point as well. Nathan, if I can impart anything on you, it's that the number of the
*  rumors that are true is so small that it rounds down to zero. Most of the rumors that you read are
*  totally nowhere close to reality. I don't know in this specific instance, but when I had some
*  specific knowledge that people were rumoring about online at OpenAI, and it was never true.
*  So I guess before returning back to Flash, which is definitely something I do want to dig in on a
*  bit, because it is super impressive, how would you advise developers who are obviously trying to
*  figure out what to build and where to go? And they're trying to gauge, am I going to get enabled
*  by or steamrolled by the next generation of things coming out from the frontier developers?
*  Should they be trying to zoom out and take a higher level perspective? Or are there trusted
*  sources you would recommend? People are not going to stop asking these questions, right?
*  It's the absence of something. We're back to the rumor mill, right?
*  Yeah. It is important that folks continue to ask the questions. I think it's just worth considering
*  and having a very skeptical take on all the different rumors, really thinking about it from
*  first principles. I think on the comment of what should developers be thinking about,
*  what makes me excited about Gemini 1.5 Flash? To give a little bit of context, OpenAI released
*  GBT4 March of 2023. I was sitting with Greg in the weeks leading up to that launch and going over
*  the demo that ultimately became him drawing on the napkin and doing that whole experience.
*  I think when I first saw that happen and when I was playing around with the technology,
*  I was like, oh, this is here and this is going to have an impact right now. I think the very
*  real reality is, until Flash came out, the natively multimodal whole echelon of vision use cases was
*  not actually possible. I gave a talk at the AI Engineering Summit the middle of last year,
*  and I said that 2024 was going to be the year of multimodal models. I think that's actually turning
*  out to be 100% true. Again, the thing that gets me excited about this particular moment is the
*  vision use cases were literally not possible before across a couple of different axes, cost,
*  latency. Most vision use cases actually turn out to be people putting in a picture and saying,
*  like, tell me about what's happening in this specific location or where this specific object
*  is or et cetera, et cetera. Those are most vision use cases in production today. And again,
*  those weren't possible before. Flash outputs actually, you can get the model to output a
*  bounding box or multiple bounding boxes. You can say, hey, where is this thing in this image? Tell
*  me where it is. And that makes this whole, like there's so many custom image segmentation models
*  that are out there, all this stuff around automating, clicking through UIs and stuff
*  like that, that were literally not possible before. The vision models that were out there,
*  the state of the art vision models, had no understanding of the spatial relationship
*  and how that act and the coordinate plane of where things were. And that's now possible.
*  And also as somebody who invests in AI startups and looks at this whole space very holistically,
*  there's just so many new things that are going to be created because of the flash models.
*  Just as a fan of the technology, not even as, again, it's hard to de-bias myself now being at
*  Google. But I really do think that it's this very special moment that it's not actually super clear
*  to me that widely the developer community sees this opportunity, partially because I think there
*  was these huge expectations for all the vision use cases and none of them have really panned out to
*  any interesting degree. And I think that's again, finally just starting to change.
*  Yeah, it is pretty amazing. The first thing that I've done with it that really impressed me,
*  and I did go head to head on this with other frontier model developers offerings, was to the
*  degree I could actually, because I couldn't entirely do this. As listeners well know,
*  I'm the AI advisor to this company, Athena, that's in the executive assistance space.
*  We've talked many times about how we have worked on this onboarding process where they used to have
*  a hour long onboarding call and then somebody would spend four hours, was the budgeted time,
*  to write up a profile of the person so that they could then hand that off to the assigned assistant
*  that would work with this client and try to give them a good running start to understand who the
*  client is. That process has been largely AI-ified. We still do the human to human call because that's
*  good for eliciting the information, but then to actually transcribe, turn that into a profile,
*  that's now all done with language models. But now we're thinking, well, what more could we do?
*  There's a ton of information, of course, that's locked up in people's Gmail. Gmail is almost for
*  sure, and probably by a lot, the number one most adopted platform across all of our clients.
*  They all have just an unbelievable amount of data in there. Our assistants get access to it as well
*  because that's a big part of how they're going to help is managing your inbox, managing your calendar.
*  So I just tried pulling the most recent 250 emails that I personally had sent and just
*  dumped them into a single context window with Flash and asked it to write a character sketch
*  about me. Basically, no prompt engineering, nothing like I didn't really even iterate on this much.
*  I was really impressed with what it was able to do. This was, it turned out with my email
*  patterns, whatever idiosyncrasies I may have, 250 emails with the content replied to and forwarded
*  or whatever the case may be, it was about a thousand tokens per email. So with this 250,
*  I'm looking at like a quarter million tokens. That obviously exceeds the context window that
*  are available from other providers. I could chunk it or whatever potentially as well, but
*  I don't want to have to do that. That sounds like work. So just dump the whole thing into Flash and
*  got a really pretty impressive two page character sketch of me and my interest and what I'm involved
*  with and covered the podcast and it covered Athena and it covered various other AI related
*  things that I'm sending emails about. Overall, a really impressive experience and that cost,
*  it actually took longer to get the emails out of the Gmail API than it took to run it through Flash.
*  The whole thing took like a three to four minute timeframe, but like 45 seconds of that was Flash
*  and the cost of it, if I understand the pricing correctly, I believe comes in under 20 cents
*  at a quarter million tokens times the 70 cents. So that was definitely an eye opener where I was
*  like, man, for a couple bucks, we can like really understand a client's whole like,
*  you know, many different facets of their life, right? We're thinking about things like
*  can we go find every gift that they've ever given in their email history and pull out all
*  the people that they should be thinking about giving gifts to and the assistant could be
*  proactive perhaps about that. Or can we get all of your travel habits, you know, and every loyalty
*  program number that you have and put that into a spreadsheet form. And it looks like this stuff is
*  very possible and honestly not even that hard to do. It's crazy to think that even with GPT-4
*  original with the 8,000 tokens, I've joked that context window inflation is the best type of
*  inflation that would handle eight emails of my thousand tokens, right? And that's before generating
*  anything. So I could maybe get seven in there or six or five, depending on how long they were,
*  whatever. And you think about the time and the cost and every once in a while would fail and
*  the complexity of that. And life has just gotten so, so much easier for developers to get like a
*  really good output back. Interestingly, that is not something that the Gmail integration will do
*  yet. I asked it to do the same thing and just said into Gemini in Gmail, like, could you read my
*  recent emails and write a character sketch of me? It said it couldn't help with that. That's my
*  story of Flash. Tell me a story of yours or somebody else's that you think is worth highlighting.
*  A couple of reactions to this. One, as an Athena customer, I'm glad that you're doing this work
*  because it actually sounds incredibly useful for the assistants or just anyone trying to help
*  someone with anything. The nuance and the very specific context matter so much. And I was using
*  AI Studio and the Gemini API to do drafts and just taking different passes at the Gemini 1.5
*  technical reports and doing exactly this of like, Hey, pull out interesting insights from here.
*  We should actually do a live demo of asking some of the questions that you asked about like,
*  what makes this natively multimodal? You can just upload the PDF and ask. I probably have it sitting
*  in my setup still. So I'm curious if we can do that and see what happens. The other thread that
*  came to my mind around this is I'm pretty sure that Flash just passed GPT-4, the original GPT-4
*  on the LM Sys leaderboard. And I'm curious if you can fact check me on that to see if that's true.
*  The 0314 version, which I think was the original, that model was $30 per million input tokens and
*  1.5 Flash version is now 35 cents for under 128K tokens and then 70 cents after that for a model
*  that's just as intelligent for a model that is more capable. And I say all that not to compare
*  these two, but also just like back to the thread of the conversation of how should developers be
*  thinking about this technology? Like that trend is not going to stop that trend of the models
*  becoming faster, smarter, cheaper, more capable, being able to infuse even more AI into the products
*  and services that people are building is going to be the path that we are very clearly on. And I was
*  in another call earlier today and was talking about the tools and how people are using AI as a tool
*  and how in many ways people are taking AI today and being like, oh, I'm going to put AI here and
*  I'm going to put AI here and I'm going to put AI here. And the actual future outcome of this
*  technology is like, the AI is going to be everywhere. Your product is going to have AI infused
*  and AI is going to be one of the primary interfaces of interaction with your product.
*  And not enough people, I think, are thinking to that order of magnitude and that level. And
*  partially it's because the technology is not actually there yet. So I have empathy for that.
*  But I think having that in the back of your mind of what that world is going to look like
*  and what is your specific product or services perspective in a world in which AI is everywhere.
*  And it is, as the saying goes, too cheap to meter. Intelligence, it'll be too cheap to meter because
*  there's so many things that are being built with it. It's useful to think about. I think the really
*  quick comment about what I've seen people building with Flash, I would be really interested to see.
*  And I think I've seen some demos actually from folks who we were at IO with around like,
*  what does an open Astra look like? Like the demo that Google did and the DeepMind team did with
*  putting on the glasses and being able to ask questions. I think you could probably recreate
*  a lion's share of that demo just using the 1.5 Flash API. And people were all talking about,
*  Oh, is Google Glass back? You can go buy that similar hardware like that, just like off the
*  shelf for probably a few hundred bucks and either connected to one of the open Gemma models or
*  connected directly to the Gemini API and make that workflow work for yourself.
*  So it'll be really interesting to see how that actually plays out. It's on my ever growing to-do
*  list to buy a pair of glasses like that and try it out and see if I can recreate the demo myself,
*  like just using the API. And again, my instinct is yes.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior
*  software engineer as much as the next guy, but honestly I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management.
*  That's why I teamed up with Sean Lanahan, who's been building engineering teams in Vietnam at a
*  very high level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance,
*  and local HR for global talent so you don't have to.
*  With teams across Asia and South America, we can cover you no matter which time zone you operate in.
*  Their engineers follow your process and use your tools. They work with React,
*  Next.js, or your favorite front-end frameworks. And on the back end,
*  they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's
*  doing two hours of work per week but billing you for 40. But you'll get premium quality at
*  a fraction of the typical cost. Our engineers are vetted top 1% talent and actually working
*  hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work, customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Yeah, it seems like if in the immediate wake of GPT-4 was the agent's craze and then it was
*  sort of, OK, well, maybe not quite yet, but we can see where this is going. Now it seems like
*  with the ability to watch the screen and for things to be cheap and low enough latency,
*  it seems like the proactive coworker is the new thing where I'm seeing a ton of that popping up,
*  whether it's the, obviously we've got the chat GPT desktop app in limited rollout and Astra and
*  Pietro made a demo at the airport, a simple version obviously, but it was impressive to see
*  how quickly he was able to put even a simple version of that together. What did the specs
*  look like on that for? I haven't benchmarked this extensively myself yet, but for Flash,
*  how should people think about time to first token and token per second type of metrics?
*  Because with the thing that I did with the 250 emails, 250,000 tokens, and it generated
*  2000-ish tokens in response and that took like about 45 seconds. So that's on the one hand,
*  extremely fast, but on the other hand, probably I shouldn't put that much context into my,
*  like, it wouldn't be fast enough to do it like on a sort of proactive suggestive basis. Are there
*  any like rules of thumb or just guidelines for how fast we should think about these things as
*  being given varying amounts of context? Yeah, that's a good question. Latency continues to be a
*  challenging thing to articulate to an external audience because there's so many confounding
*  factors of like, what does latency actually mean? Like the current load that the server is under
*  affects latency and time to first token, like it varies by day. There's historically across usage
*  patterns, different times of the day have different peak loads, which then impacts latency. There are
*  all these like weird effects back to the comment that I made earlier. I think this is actually
*  something that I'm hopeful that LMSys and in absence of LMSys, I think somebody else should
*  do this. Like, how can we make a benchmark that is actually representative of all of these trade
*  offs? Like as me as a developer, as you as a developer, you're thinking about how to use this
*  technology. How can we actually calculate into these benchmarks, not just the human preference
*  scores, but also like what the cost is for a million tokens and what the latency looks like
*  coming up with a scientific way to do that. Or even just a simple interface where like I,
*  as a developer can say, here you have three little sliders and the two things I care the most about
*  are latency and cost. And you know what? Actually intelligence doesn't matter that much to me or
*  vice versa, whatever the different axes are, letting you tweak those and getting some sort
*  of output of like, here's the model that I should be choosing based on those things. I think would
*  actually be incredibly interesting to developers. And again, I'm biased, but I don't think that the
*  ELO scores for flash are actually representative of how transformative it's going to be for
*  developers because it's tied for like ninth or something like that. But it's also 10 times
*  cheaper than a bunch of similarly capable models and also multimodal and also et cetera, et cetera.
*  So it's really interesting to think about that. That's the thing that keeps ringing in my head.
*  I do think we probably need to put out a little bit more guidance around latency. My instinct is
*  it's three times ish faster in a bunch of use cases that I've tried than pro, but I've almost
*  like fully moved over a bunch of my daily AI use to flash. And it seems to be like just as capable
*  in a lot of the use cases that I'm messing around with it on. Yeah, that's interesting. The fact
*  that you're doing that as a first go to is definitely pretty telling the numbers for what
*  it's worth are the ELO score for flash right now is 1232. And that is just under 50 points ahead of
*  GPT-4-0314, the original. And it's funny, the least popular GPT-4 continues to be the June
*  of last year version. So it's like a full 70 points ahead of that. And it's only like 15 points behind
*  the January version of GPT-4, which is, as you noted, more than 10 times more expensive, either
*  30 times more expensive or 12 times more expensive, depending on whether you're above or below the
*  128. And just to be clear on how that works too, is it basically like it's a hard cutoff, right? If I
*  send in 127,999, I'm built at the one rate and I tip over, I'm at that other rate, that sort of
*  suggests I'm using more hardware, I guess is probably what's going on under the hood. Otherwise,
*  I don't know why there would be a breakpoint. It is a hard cutoff. I think the intent is actually
*  more so to like the cost of doing compute on higher numbers of tokens is not linear. Broadly,
*  that's true. So I think this is more so trying to embody the reality of the costs associated with
*  running these models, which is that it's a much higher cost to do some of those larger token
*  requests. It just requires a lot more compute. Yeah. Take that for what it's worth. And on your
*  comment about the 0613 model, yeah, well, a couple of years, we'll get a blog post or another podcast
*  about why that model is slightly worse than all the other GPT-4 models. Interesting. Well, the world
*  might be a very different place by the time you're able to tell that story in full, but I look
*  forward to it nonetheless. When you guys are building internally at Google, and I know you're
*  not exactly doing this, but the things that we saw Astra, for example, out of the Labs group,
*  are they basically building on the same thing that we as developers either are now able to build on
*  or soon will be able to build on? Is that basically a dogfooding exercise? Yeah. Labs didn't build,
*  just to clarify, the DeepMind team has built the Astra project. Labs built a bunch of the cool stuff.
*  I think there's very specific circumstances where they might be running their own stuff,
*  but actually most, there's many thousands of internal teams that build directly on the Gemini
*  API. The same API that we make available to developers is the same API that teams use. I
*  think the only delta, the reason why teams might not use those models out of the box is they need
*  some custom post-training data that's not represented in the existing models that are
*  available through the API. Again, if that team has the muscle and the resources to go and do
*  custom post-training, then they might go and do that to make, this is just a made up example,
*  but the Maps team, if the model doesn't have enough Maps data and for some reason there's a
*  bunch of use cases that would require that, if they had the resources, they might go and build
*  off of the base model and go and post-train their own version for some specific use case.
*  Gotcha. Okay, cool. I'm interested to hear, you're stepping into a position here where
*  competition is obviously fierce for the developer accounts and there's multiple dimensions to it,
*  the models being certainly the primary one and what actual capabilities you can get at for what
*  price, but the friction and the developer experience also definitely matters. I will
*  confess to having been confused certainly at times in terms of where do I go for what with
*  cloud versus Vertex versus AI Studio. If you actually have the Gemini 1.5 technical report
*  loaded up and you want to just do the walkthrough in the AI Studio, that would be, I think, a useful
*  exercise. Let me switch over to my Gmail account and then I'll do it from there.
*  Okay, cool. I can see your screen and maybe just give us a little bit of context for what this is
*  and how it relates to other flagship Google properties. I'm not clear on
*  is this a sort of playground type of environment, but when I actually want to go to production,
*  I need to switch over to Vertex still, or what is the sort of overall developer journey that folks
*  are supposed to go on and how does this fit into that? Yeah, this is a great question. I'm glad that
*  you asked that. It is top of mind for me to simplify this and make sure that it's abundantly
*  clear to developers. I think having to talk about it is a great reminder that we have a lot of work
*  to do in this space. Broadly, if you are somebody who knows that you need an enterprise cloud
*  solution, that is what Vertex is for. For whatever the constraint is, whether it's a legal, regulatory,
*  privacy, you need some specific SOs, you need whatever, you need to have some legal agreement
*  signed because of the context of your business, all of those things are traditional things that
*  an enterprise cloud provider would do. You can get all of those things from Vertex. I think it's
*  the right place to go if you need those things. If you're just a developer who's like, I need to
*  build AI into my startup, I want to use Flash, I want to use 1.5 Pro, there's two things that
*  you need to be aware of. One, AI Studio is sort of the interface to get started with this technology.
*  You can do a bunch of prompting, which we'll do here in this UI. It's essentially just a playground.
*  You can get your API key, you can do a couple of other things like make a tuned model, which
*  you can also do through the API. This is where you would get started with the technology.
*  You can also just go to ai.google.dev where our developer documentation lives. Again, you'll still
*  need to use AI Studio to grab an API key for the API. But you can go to production, you can scale
*  in production. We support, again, similar... The mental model that I give to people is like,
*  there was OpenAI and there was Azure OpenAI for us. We have the Gemini API and then we also have
*  the Gemini API available in Vertex, which is our enterprise cloud solution. You can choose either
*  of those. There's very real reasons you would want to use either. For most developers using
*  enterprise cloud solutions, there's a bunch of friction involved for good reason. They tend to
*  go with the less friction option, which is in our case, AI Studio and the Gemini API.
*  Got you. Cool. For most people, if you don't have a special requirement,
*  you don't even have to concern yourself with Vertex.
*  Correct. Yeah. Again, unless you have a specific need for an enterprise cloud solution, I don't
*  think that you can get pretty much everything you need directly out of the box with AI Studio and
*  the Gemini API. Gotcha. Okay. Yeah. Cool.
*  Yeah. We're in AI Studio. Again, simple prompt interface. I put in the Gemini 1.5 technical
*  report, 115,000 tokens, and we were talking before about natively multimodal. Can you tell me
*  what makes Gemini 1.5 natively multimodal? What does that even mean?
*  And we can go and find out and we'll see what happens in a couple of seconds. The document
*  you provide doesn't explicitly state what makes Gemini 1.5 natively multimodal. Interesting.
*  And this is exactly what I would have expected. Yeah. I think that it doesn't talk about the
*  architecture. While this is not really intended to be like a place that people come for regular
*  use of the models, I actually have found it to be useful in a couple scenarios. I find it to be
*  remarkable that it's not easier to set up a template with a long doc just loaded fully into
*  context. When the GBTs first launched, it was like, okay, great. Now I can put my whole codebase in
*  there. But then I would do that and then it would try to search through it, not load enough stuff in
*  and then miss things. And I was like, okay, but I actually just want you to read the whole
*  codebase. And because I know you can't, you have enough room for that, but it wasn't really designed
*  for that. Claude, I still doesn't have that as like a template setting. And actually, this is
*  like one of the few places where you can come and just have a preset prompt that has a few docs.
*  I have a couple template prompts in my own studio. One of them is like 20 different
*  mixture of experts papers. I was trying to get a handle on what is up with a mixture of experts.
*  Notably, I think it is stated that this is a mixture of experts architecture that we're
*  working with here. And that's obviously become standard frontier at this point.
*  So just trying to get a handle on that, I was like, I'm going to have probably however many
*  rounds of back and forth on this to try to educate myself and just loading in those 20 papers. And
*  it's funny, like that's a pain in the butt, but the ability to just save that here as a preset is
*  actually pretty useful and has me coming back to it occasionally as like a retail customer,
*  even though that's not something I'm like trying to productize.
*  Yeah, it is interesting. I think part of the context is that the AI studio product has like
*  the DNA and the roots actually in the consumer is originally called mobile or maker suite. And it
*  was about like building automation flows and things like that. And it ultimately got transformed into
*  AI studio, which is this sort of playground product. But I think a lot of the initial DNA was
*  more of a consumer product, which is interesting. And I think very clearly the direction that we're
*  pushing in is like towards a developer product. But I do think that part of the magic of this is
*  like, and actually to your comment about email is like something that we've thought about, about
*  like, you know, ultimately, we want people to be able to see that this technology is useful. So
*  being able to import a bunch of your emails and use Gemini directly through this interface has a
*  potential to be really useful to people. I think the balance to strike is like, we don't want to
*  make this too much of a consumer product. Like ultimately, what matters is developers building
*  stuff with the API. So we don't want to over incentivize people to come to AI studio and do
*  all their AI workflows directly inside AI studio. It would be quite the accident of history if that
*  to continue to be the thing. Let's do a couple of rapid fire ones. Let's do it. Okay, just road map
*  then. The VO, should we expect that to be kind of a slow rollout a la Sora? Or is that something
*  folks will actually be able to build into products in the like, not distant future?
*  It's a really good question. And I honestly don't have the answer. My expectation is that the
*  tooling is actually pretty robust that part of video effects that the labs team and other
*  contributors have built. So I'm not 100% sure on what the rollout looks like. But it seems like a
*  very distinctly different product slash world out strategy than Sora from my understanding. And I'm
*  hearing Josh talk about it. Okay, cool. I'm on the wait list. If you could put in a good word for me,
*  that one is definitely a priority at Weimark. How about on the rounding out the suite of tools a
*  little bit? Obviously, as you well know, OpenAIRE has the assistance API that kind of brings an
*  integrated rag component as well as like a tool use thing into a single product. As far as I know,
*  there's not like a rag element. There is tool use, but it doesn't seem like it's been emphasized
*  very much. So what's the future of those things? Will there be like a packaged up version?
*  Yeah, we have function calling right now. We have a bunch of improvements that we need to make on
*  function calling. So you can imagine like a function calling V2 coming. Yeah, I say V2 just
*  to emphasize that we'll make updates to it's not clear like what how substantial those changes will
*  be if it's just like improving the accuracy of the model like function calling or what that will
*  look like. We actually do have in the Gemini API today, a semantic retrieval API that's been built
*  in, which took a bunch of work. So you can upload a bunch of documents into a corpus and then do
*  semantic retrieval on top of that. I think we're still early in our thinking about what that product
*  will look like. It's not clear that the current design and what we've built is like the thing
*  that we'll keep running with long term. But I think it's been useful to look at that. On the
*  Vertex side, they have an agent builder flow, which allows you to do a few more of these use
*  cases a little bit more robustly. And we don't offer that yet, but I think it's possible we might
*  take what they learn on the Vertex side and bring some of that over into the Gemini API as well.
*  Okay, cool. That's interesting. What about fine tuning? I know there are like some things that
*  can be fine tuned. Like what can be fine tuned? I can't fine tune like 1.5 Pro. Can I?
*  You can't fine tune 1.5 Pro, but on Thursday we'll announce or coming on May 30th. So maybe after this
*  video is released, 1.5 Flash fine tuning will be available. And I think we have such an interesting
*  value proposition with Flash and that you don't pay more cost for inference and you don't pay
*  to train. So it makes it this very unique value proposition that actually again, nobody else is
*  offering right now, which is really exciting to me. So no pro tuning yet, but Flash tuning will
*  be announced, not fully rolled out, but announced on Thursday. Wow. Okay. That's interesting. Should
*  we think of that as the same? I think fine tuning is like very much a point of confusion, right?
*  For I tried at one point trying to fine tune open AI models to write as me. That turned out to be
*  not viable. Currently the best write as me solutions, one I would say is probably Claude Opus.
*  And I should try again with the latest date stamp of Gemini 1.5 Pro because that was the thing up
*  until Opus. But how should we think about fine tuning? My general rule of thumb is if you're
*  narrowing in on a task, you can use fine tuning to dial in exactly how you want it to behave
*  for a specific task. But then you have to make sure that you're controlling inputs and outputs
*  effectively. You lose the generality. If you want to do something sort of ad hoc, like write as me,
*  summarize all these documents or whatever, there you're probably just better context stuffing. How
*  would you refine my understanding of that? Yeah. I think this, when I was between Google and open AI,
*  give a serious thought into making a startup around this problem, this write as me problem.
*  Because I think the real challenge is you can get pretty far with fine tuning. The problem is it's
*  like a traditional machine learning problem to actually make sure that you have a representative
*  data set that's balanced and focused on the right things. And it's like, you're probably actually
*  capable of doing this. But I think broadly the market of people who are going to figure out,
*  do the right experiments, figure out how to actually make this work is like a very small
*  subsection of people. So my guess on- What rank fine tuning, I'm not sure it's even really
*  super possible. It seems like facts are just really hard. So it seems like you need some sort of
*  retrieval help, probably anyway. I think it's both of those things. And I also think it's like
*  synthetic data magnification, stuff like that. Like a lot of people just don't have enough content to
*  actually like, you need more examples to make the model really good at what it is. And like being
*  really thoughtful about what you're doing with fine tuning versus what you're doing with RAC.
*  Yeah. Okay. That was definitely tricky. I'm not sure if I'm capable of it or not. I maybe gave up
*  too soon, but I didn't succeed. So time will tell. Okay. You had said a while back, this was back in
*  the open AI era, open AI is only as good as its latest model. And that has stuck with me because
*  it really suggests that the competition has a potential for a winner take all dynamic because
*  it is like pretty easy to switch between models. In many cases, you got a reprompt engineer,
*  but it's a pretty simple swap in a lot of cases. How would you characterize the state of competition
*  amongst the frontier developers today? And like, how much are you guys thinking about each other
*  and trying to time your announcements to scoop each other? What's the real
*  vibe as you guys are competing in this world that is our last model situation?
*  I have an enormous amount of respect for Sam. I'm not sure that I agree with the,
*  I never think about competition piece of it. I think people are like very aware of how much
*  competition there is. So it wasn't, yeah, I was not aligned with that. I think to me,
*  something that has become abundantly clear is that we're not going to end up in a winner take
*  all situation. I think the players in the market understand how much of an opportunity there is
*  with this technology, how transformative it is. If anything, I think that has pushed even more
*  people who normally wouldn't compete in this space to compete in this space, which I think is a net
*  benefit for everyone, especially with where open sources and how many people are pushing from a
*  frontier lab perspective. It's super exciting to be a part of. And I would actually expect that
*  even more people are going to end up competing as they finally wrap their head around how big of an
*  opportunity there is here. Interesting. That's quite contrary actually to my expectation. I feel
*  like we're seeing the second tier of foundation model developers getting thinned out right around
*  now. And I expect there will be a couple of Chinese champions. There might be like an Indian
*  champion, like Mistral might be like the champion of Europe. But I think we're headed for 10,
*  maybe, companies that could make a credible case that they're at or near the frontier.
*  You think it'll be more than that? I think it's hard to know the specific number, but my guess is
*  just because of how much value could be accrued that a lot of people, anyone with any amount of
*  technical understanding and sufficient resources is going to go and do this. And there's a lot of
*  people who don't have enough sufficient resources and they'll go do open source and that will
*  continue to push open source even closer to the frontier. So I'm hopeful that we'll end up in some
*  really nice symbiosis. And I think for like people betting on taking the entire market to be
*  successful, I think it's not likely to be the best outcome for those companies. And I think there's
*  a lot of businesses where they just need to make a great model for it to be an incredibly
*  valuable thing for their business. I think that's actually positive.
*  Okay. Another recent tweet that really caught my attention was your tweet saying that if
*  AGI were here today, people wouldn't know what to do with it. And I'd love to hear more about what
*  you mean by that. Because I feel like I would know what to do with it, or at least I think I would.
*  If it's an AGI that is literally like, if we're talking, you know, can outperform humans at most
*  economic work and is highly autonomous, what are people not going to get about that? Or am I using
*  the wrong definition? Or please explain. No, I think you of all people would know
*  what to do with it because I think you're positioned in this ecosystem in a very particular
*  way. I think that the commentary was more that like, again, continuing to hit on this story of
*  most people still have never even used GBT four, most people have never used Gemini 1.5.
*  Most people haven't used this technology. So everyone thinks that there's going to be the
*  singularity. If someone gave me AGI right now on my computer and I can access it through an API or
*  an interface, time in which it'll take for the world to change is very long. The world is a big
*  place. There's a lot of things that are going to happen. But also the sort of conversation with
*  Connor, who was also at IO, and I don't know if you got a chance to chat with him, but he's incredible.
*  I love Connor so much. And he gets to spend his time thinking about how can we empower people who
*  don't have any technical background to really leverage this technology and understand how to
*  build with it. And I think it's such a powerful message because again, most of the world is not
*  technical. Most of the world doesn't really care about this technology. It's more about how they
*  can use it as a tool. So that maybe suggests sort of where you would direct people on the developer
*  side in terms of opportunity. Going back to earlier in the conversation, you said one of the great
*  workflows is just turning on meeting assistant in Google Meet and it will take notes and assign
*  to-dos and whatever. Of course, there are like a dozen startups that are competing for that niche
*  as well. I came away honestly from IO feeling like, man, the platforms have such incredible
*  economies of scale. They've got the distribution. They can afford to build a lot of things in for
*  free. Obviously, Meta's put everything free. GPT-4.0 is free. I pay for Google advance. I'm not sure
*  what I'm getting for free or not. But certainly there's ability to put stuff in for free.
*  How do you think developers should be strategizing for what opportunities
*  they can pursue that Google won't pursue or can they out-execute? It seems like distribution is
*  going to be a really hard uphill battle for any of these meeting note-takers going forward, right?
*  But it wasn't that long ago that would have been considered a frontier like, oh my God, Google's
*  not going to do this anytime soon. But I'm old enough to remember those days and they weren't
*  that long ago. So how do I stay ahead of that wave and not get crashed over by that wave?
*  I think the distribution piece is definitely one of the advantages that larger companies
*  have over startups. I think the real reality for startups, and I've felt this myself now having
*  sat in many different seats in my life, is there are so many inherent advantages to startups, which
*  now being in a large company, again, I would beg to have those things as advantages. Again,
*  the fact that you can have a very small focused group of people who are just going to go and
*  execute and build and do that, and you don't need to, you know, every additional, however many
*  people you have introduces an again, additional amount of coordination overhead. And if I was
*  sitting in a startup today, I would be smiling with my grin, extremely wide thinking about how
*  I can go and compete against some of the large companies that are out there because there's just
*  so much opportunity in the ecosystem. There's so much to be built. There's so many new things that
*  were not possible before that are now possible with LLMs. I think the important thing is again,
*  it's very possible that all the meeting notes takers are going to do really well. I think
*  they're actually incredibly well positioned to become one of the first agents slash assistants
*  that like actually help you go and do work. Like they're in the meeting, they have the context,
*  like having the context is like half the battle. I'm not only in Google Meets, but I think there's
*  a lot of people who are across many different platforms across Teams and Zoom and Meet and
*  other things and being able to have a tool that maybe does all those things is incredibly useful.
*  So there's a lot of different edges. And again, the value isn't in just doing the integration and
*  taking the notes, but like also in what you do after that and how much you can automate away.
*  Like if for some reason I had a system that was able to draft up a bunch of emails after a meeting
*  and say, here, let me go and ping these people for you and I can just go and check, check and
*  send those emails off. That's a distinctly different competitive advantage than what's
*  being provided today. So there's always more that can be done. And I think again, as I've said this
*  many times in different places, there's never been a better time to be a startup building in this
*  space than right now. Like this technology, like everything is up for grabs. Well, I think
*  that's a great concluding note. You want to share anything else that we didn't get to? Yeah, I'm on
*  Twitter. Folks can get ahold of me there and see all the things that I'm thinking and sharing. And
*  I'm appreciative of you having me on for a second time, Nathan. This was fun. Hopefully I'll see you
*  sooner than Google IOT next year. Looking forward to it. Logan Kilpatrick, thank you for being part
*  of the cognitive revolution. I love it. Thanks for having me. It is both energizing and enlightening
*  to hear why people listen and learn what they value about the show. So please don't hesitate
*  to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your
*  choice.
