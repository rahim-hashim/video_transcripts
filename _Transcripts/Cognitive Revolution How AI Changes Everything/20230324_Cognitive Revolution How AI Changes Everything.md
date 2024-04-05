---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4855s
Video Keywords: []
Video Views: 416
Video Rating: None
---

# The AI Voice Revolution with Mahmoud Felfel of Play.ht
**Cognitive Revolution "How AI Changes Everything":** [March 24, 2023](https://www.youtube.com/watch?v=9YtxBnj52Wc)
*  We're working with like the South Park good use, like they're making like a new episode
*  and like they'll be using one of our voices also for one of the characters.
*  That's super exciting. Like, oh my God, like this voice is now being used in production,
*  actual show. We started with additional text-to-speech use cases. The main
*  driver for us to do that investment because it was like very risky. So we did all like that
*  investment because we wanted to get into that market of like the human voice, like all voice
*  over actors and the opportunities this can open because this was the first time ever
*  you're automating the human voice. Hello and welcome to the cognitive revolution
*  where we interview visionary researchers, entrepreneurs and builders working on the
*  frontier of artificial intelligence. Each week we'll explore their revolutionary ideas and
*  together we'll build a picture of how AI technology will transform work, life and society in the coming
*  years. I'm Nathan LeBenz joined by my co-host Eric Torenberg. Before we dive into the cognitive
*  revolution, I want to tell you about my new interview show Upstream. Upstream is where I
*  go deeper with some of the world's most interesting thinkers to map the constellation of ideas that
*  matter. On the first season of Upstream, you'll hear from Mark Andreessen, David Sachs, Balaji,
*  Ezra Klein, Joe Lonsdale and more. Make sure to subscribe and check out the first episode with
*  A16Z's Mark Andreessen. The link is in the description. Omniki uses generative AI to enable
*  you to launch hundreds of thousands of ad iterations that actually work customized across
*  all platforms with a click of a button. I believe in Omniki so much that I invested in it and I
*  recommend you use it too. Use Cogrev to get a 10% discount. Mahmoud Falful is the CEO of PlayHT,
*  the AI power text to voice generator. We've told you episode after episode that transformers
*  are working for everything and that includes generating what PlayHT calls ultra realistic
*  human voices. When Mahmoud started PlayHT just three years ago, serviceable but obviously robotic
*  texts to speech services were the standard and neural voices were just getting started.
*  Just two years ago, a custom voice with a leading provider required hours of audio and cost $10,000.
*  Today, I can clone my voice with just 10 minutes of audio at minimal cost in less than an hour.
*  I can hear myself reading content just like this and just as in other subfields of AI,
*  progress is not slowing down. Mahmoud talks about the next generation of text to voice models working
*  more like image generators do today with a rich prompt space that allows you to effectively direct
*  the quality of voice output. If there's one AI development society has predicted and which is
*  very intuitively dual use, it's deep fakes but somehow they are already here and we are
*  definitely not prepared. Already on TikTok, I'm seeing creators say that their families have been
*  scammed and starting to recommend family passwords that impersonators wouldn't know.
*  Now, I was genuinely impressed with Mahmoud's approach to user safety and preventing abuse.
*  To his credit, he does have a multi-pronged approach but it seems like there's only so
*  much builders like Mahmoud can do to protect us from the downsides of AI and we're likely going
*  to have to figure out how to deal with the world of convincing deep fakes quickly. As much as that
*  does worry me, I also share Mahmoud's amazement and delight over the technology and the products
*  that he's able to build with it. Making this was easy, quick and genuinely fun and I hope you enjoy
*  my conversation with Mahmoud Felfel. Mahmoud Felfel, welcome to the Cognitive Revolution.
*  Thank you. Thanks for having me.
*  Yeah, my pleasure. I'm really looking forward to this conversation but you obviously are the
*  founder and CEO of PlayHT and you guys are in what would be traditionally called the text-to-speech
*  business. You might also call it the voice generation business as we'll get into a little
*  bit later. You might even call it at least the audio side of the deep fake revolution that's
*  coming our way. I'm really excited to talk to you. I've been personally a customer and I would say
*  pretty demanding exacting customer in the space of the technology that you're building
*  because at my company Waymark, we make TV commercials for local and small advertisers.
*  It's really appealing that we want to use technology to do that. It gives speed,
*  it gives cost effectiveness which is hard to match with any sort of service.
*  But no matter how small the business, no matter how small the budget, folks want to sound good.
*  They do not want it to sound like it was made by a robot. I've personally spent quite a few hours
*  going around and shopping for all the products, testing all the APIs. What you guys are doing
*  with the ultra realistic voices is really among the very best products out there today in terms of
*  how it sounds, how easy it is to use. I'm really interested to get into all of that technology and
*  start to pull apart how it works. But first, I just wanted to ask you a question about the
*  start of the business because I think there's maybe something pretty interesting here.
*  When I was first shopping around and used PlayHT, it wasn't quite clear to me but I got the sense
*  from using the product that the first thing that you had launched was essentially an API wrapper
*  around text-to-speech services that were already offered by the big tech companies,
*  your Googles, Amazons, maybe even an IBM or a Microsoft. I don't know who all had offerings
*  that you guys were making available. I'd love to hear the back story of that. That seemed like a
*  really smart strategy to me because obviously those things are reliable and they were pretty
*  close to the state of the art, if not state of the art, and they were fast. Also, by reselling them,
*  you have an unbelievable window into how customers like or don't like those services and where
*  they're falling short. Tell me about that kind of origin story. You're right about what you said.
*  And we started by using these third-party APIs from AWS, Google Cloud, IBM. IBM was the first
*  one. IBM Watson. Even before AWS released, Poly and Azure also released text-to-speech voices.
*  The reason we started with this product is that me and my co-founder were working together,
*  software engineers. We were always tinkering with different things, trying to solve different
*  problems. And we started maybe over a couple of years, 10 ideas all failed. And then at the end,
*  literally taking a break of working on anything. I like listening to audio books. I have two
*  subscriptions to audio books or something. So I didn't find the same with articles. At the time,
*  that was maybe four years ago. Media was pretty big and there were many writers coming to media.
*  So I found this one place where all writers there and I'm reading a lot of medium articles every day.
*  I started to think, okay, I need to listen to this when I'm running or doing anything.
*  How do I do with audio books? But there was no way to do that. And then I started to look into,
*  okay, what's available? Can this be automated? And then I found IBM Voices. And they were actually
*  pretty good. Most of the voices in the market at that point was very robotic. They were like,
*  you cannot consume. They're not consumable for people. And I wouldn't stand listening to that
*  for an hour or something. But the IBM Voices were actually pretty good. And they're still robotic.
*  Alexa-like voices or Siri. But you can tolerate listening to them for some time. And so we built,
*  I suggested that idea to my co-founder and we started building it. We built it with a Chrome
*  extension for medium. Basically, we're building it for myself. And we put it on product hunt.
*  Actually, we didn't put it on product hunt. Someone found it and put it in the Chrome store
*  and put it there. And we got so many people using it. Asked for mobile apps. We built mobile apps.
*  And there was a lot of traction on that, listening to audio articles. We started to think about,
*  okay, this is becoming maybe a little bit big. Let's just focus on this and make it business.
*  We started to think about monetizing it. And then we started to see it was very hard to ask people
*  to pay for this. They want to, like consumers, they want to consume more and pay way less.
*  And if you go the route of audio ads, that also wasn't very appealing to us to try to source ads
*  and services to users. I mean, it's annoying even for us to have audio ads. So we didn't
*  want to add this to the product. But at the same time, we noticed something that,
*  like many of the users of our application and the Chrome extension,
*  were actually people who have already publications and have blogs or are actually using mediums
*  themselves as writers. And they have big audiences. And they're asking us, okay, this is very useful.
*  I love it. I want my readers to be able to listen to my content. So we saw opportunities there for
*  having this as like a B2B product or like a SaaS product where we offer this like audio articles
*  product where writers and or publications in general can add this. And now like there are many
*  publications now. I mean, after that time, many publications have this now you can listen to the
*  article when you go there. So that was our target at that point. Yeah. And we, so we did this product.
*  We started getting some growth there. It wasn't like as big as what we hoped for, but we started
*  to get a feeling of like building a B2B product, SaaS business and what people are expecting.
*  And the problem there is that we started to found like this is like the audio articles product was
*  more of, you know, like this thing of like vitamins versus like painkillers. It was like a good to have.
*  It was like most people wasn't like searching or trying to find a solution for an audio article
*  problem. It's a good to have. Like if you have a publication, I mean, writing itself, generating
*  the actual articles, that's a problem. But then once you have that adding audio articles on top
*  of this seemed like it's a good to have thing. And we, so we didn't get like a huge, huge growth there.
*  And at that time COVID hit and we have built this on top of these like APIs. We have built that
*  editor that has, you know, basically all the capabilities of these APIs, you know,
*  customizing the SSML and like, like everything there and like just taking this and making it
*  visual where people can, you know, easily create content using these like text to speech engines.
*  And we found that there are many customers coming using this for other use cases.
*  And when COVID hit that like some of these use cases were in like learning and development and
*  like other so we can get into this more and actually why we started investing
*  in our own like in-house model. It's related actually to the point that you just mentioned that
*  people like regardless if it's a small or big company, they want the best quality, right?
*  And we started to see this in our users. That was the main reason we started to invest in
*  training our own models because we found, okay, these like generic APIs from AWS or Azure,
*  they are good, but they are not built for like the use cases we're trying to serve. And they are
*  still very robotic. So we saw if we want this business to really grow, we have to, I mean,
*  we either sell it and do something else or we have to solve that quality issue. We have to make this
*  voice like human-like voice. And, you know, we started investing in training our model. We can
*  get into this more. Yeah, that's really interesting. You're one of a couple of different entrepreneurs
*  now that we've talked to who actually started a company that was not originally an AI company and
*  has become an AI company. You guys started with kind of a problem, an observation, you know, and
*  it sounds like above all, kind of creating an accessible product experience that, you know,
*  people preferred to having to go to AWS Poly and figure that out directly. And then, you know,
*  kind of you're midway and all of a sudden what is possible with AI changes dramatically. So
*  did you run into any challenges, you know, in kind of reselling those things? Like were the platform,
*  you know, companies nice to you as you went about doing that? And how much of that is still like
*  the usage that you see in the product today versus all the new stuff that we'll talk about next?
*  Yeah, actually. So we built, like, I think a very good business. We're growing very fast on these
*  APIs because we're mostly solving problems. I mean, like end of the day, I mean, we are like
*  in this like tech bubble, so we're really interested in tech and like fancy stuff. But end of the day,
*  consumers don't care about like what's happening in the background. Like is it your model? Is it
*  an API? Is it whatever? They want, they have a problem and they want it solved and solved with,
*  like, you know, like this like jobs to be done, like approach where the job here is to create
*  good quality audio out of this. And like these were like good enough and fast enough to solve
*  that problem and like to a point. And that point was the quality. Whenever we started to look into
*  the high end use cases, like, as you said, with audio ads, with gaming, like gaming companies,
*  like most of gaming companies today, they don't use text to speech in production. They use it
*  only for like, like scratch audio, like when they're developing the game, they just fill in
*  like some, you know, like characters with voices. But when they go to production, they get actual
*  voiceover actors to get like, you know, that feeling and like suppression and all of that.
*  The same for like media production, like in general, like in all, like in different,
*  like all the high end use cases, even in audio articles, like when we, whenever we try to reach
*  to like New York Times or like any like big publication, they who care about their brand,
*  they would complain about quality. Okay. This is not good enough for our users. So that was the,
*  we found this is the biggest hurdle. Like if we manage to solve that problem, this will be a huge,
*  because then we moved from the traditional text to speech market to, which is like learning and
*  development, IVR, like, like, you know, these things to the human voice market. And that's like
*  a huge market. Like, like the use cases are like huge there and the potential also like these
*  platforms, there was no problem at all. They provide an API. We were able to scale very well
*  and we're still using them until today. We launched our own model. I mean, we started working
*  on it like more than a year ago, but we launched it around five months ago. And over these five
*  months, now our models are serving around 60% of our usage. And we have like millions of like
*  conversions every month. And now, now 60%, I mean, it didn't actually drop like the old, the old
*  model usage didn't drop. It has been like growing, but also our models came up and now it took over
*  that. And the reason like these people are still using the old models, like all of these like APIs,
*  mainly because of languages. Like our model now is still only in English and these other models,
*  they have like, like a much bigger, like maybe I think 130 something like languages and accents
*  inside each language and everything. So that also has like a lot of usage.
*  I'm reminded of the very first episode we did, which was with Suhail Doshi from Playground.
*  He told us a fascinating, couple of fascinating stats. One was that a full 10% of their users make
*  more than a thousand images a day, which I still kind of, you know, shake my head at and try to
*  imagine what that really means. But then also he said at one time they found a latency bottleneck
*  in their system, fixed it and generation got twice as fast. And he said they immediately saw,
*  essentially a doubling of usage with that change, you know, kind of a step change.
*  Like people were just, you know, ready to use all of the generation that they would give them.
*  So your story is kind of similar in a sense that you had this kind of breakthrough of quality with
*  the new ultra realistic voices and it just unlocks more use cases, more market opportunity.
*  And it's really fascinating to know that the, you know, kind of big tech, you know,
*  last generation stuff not only continues to play a significant role, but even, you know,
*  continues to grow. So that is very, very interesting.
*  Well, I mean, we have something similar also. I think that like people are starting really to
*  like use this and change their content creation flows completely because of these technologies,
*  what Playground is doing and like we're doing on others. Like we have some users that told me,
*  like on calls, we are spending 12 hours per day in our editor. I was so surprised. Like I am not
*  spending 12 hours a day in our editor. They're creating like complete audio books, podcasts,
*  and they're very careful, like choosing characters and like, you know, editing everything.
*  They're really designing the experience. Initially we thought that people would use this just to
*  replace, to be like a quick thing, you know, to get something out. But people are very
*  like deliberate about these things and trying to have, like, think about like the listener,
*  how they will listen and like have conversations with different voices and like the voices we do
*  and how the conversation will flow from one character to another and all of these things.
*  And that's just so inspiring to see like how people are using this tool.
*  So tell me about the process of, I guess, first of all, becoming an AI company.
*  I'm sure you had to, you know, learn a lot yourself. I'm sure you had to go hire new people
*  that brought critical skills to the team. And then it sounds like you spent more than half a year
*  working on your first in-house model before you were able to launch it. So tell me about the
*  process, but then also the technology itself that you've built. Actually, from the beginning,
*  we have been very involved, like me and Microphone, they're both software engineers. So like the most
*  natural thing was not to use the APIs from these platforms like AWS and others, but to just go and
*  do our own, deploy our own models. But the problem there, and like actually many other companies in
*  the market, they did exactly that. They just went and trained their own models. But what we found,
*  the maximum quality we're able to get, like whenever we take these models, you know,
*  FastSpeed, Staccatron, like this, like the ones available in the market, and we train them,
*  the best results you can get is similar to what you get from the API. So it just didn't
*  make sense. Like you will invest and you'll have like a machine learning team in-house and like
*  doing a lot of research and training and stuff like this, and at the end, getting the same quality
*  and the same value you're getting from these APIs. At the beginning, that didn't make sense. And we
*  continuously, like, I mean, almost every open source project or research paper came out about
*  text-to-speech in those two years. We were in touch with the person who did it, and we had a call with
*  them, like we, and like whoever open sourced something, we have to try it. But we never found
*  something that's really a breakthrough. But at that time, like beginning of 2022, we started to
*  see that shift in the architectures, like Dali was there, GPT-3 was there for some time, and
*  diffusion models, and there was that shift. Okay, so now, because the problem with text-to-speech,
*  like standard text-to-speech models, that they are not self-supervised. They're like supervised
*  learning where you have, say, 20 hours of Nassan's voice recorded in a studio, and then you take that
*  and you train a model on these 20 hours. So the model will generalize on how to speak like your
*  voice, like this, like Nassan's voice, and that's it, not how to speak like a human. And that's why
*  the voice that's generated in a studio from one person, it is really hard to make the model
*  generalize from this to be able to speak like so many other voices and be very emotional. And
*  like basically, if you want the model to speak a different accent, you will have to get someone
*  speaking that accent and train the model in that accent. If you want the model to speak in like
*  specific emotion, you will have to go and get someone speaking that some data set, and you
*  label it like this and you do some conditioning to the model to be able to generate that emotion,
*  which is a very hard process to do, especially if you want to scale to so many voices. And then if
*  you want to go into voice cloning, that's almost impossible. What we found at that time that now
*  with self-supervised learning where, okay, now you can train this actually on a huge data set or like
*  hundreds of thousands of voices, maybe, and there are already some, like the good thing is there are
*  really like very large data sets available, like Common Voice from Mozilla and like many other
*  like books, Bookslib, like some UTI books, you know, public domain UTI books available. And I
*  mean, you have the internet, right? Like you can also use like a lot of data available in the
*  internet where, and now with like self-supervised, you don't need that data to be like the best
*  quality. You basically training the model how to speak like humans. And then after training this
*  large language model, it's actually not very large, just like,
*  like around like, I think almost like 300 million parameters. So it's actually very
*  medium model. Right now we have one, we have another one now that's actually large.
*  I can't tell you why we trained another model and everything, but that one, the first one was
*  actually wasn't that large. And, but the reason it got very good is that because the data set is big
*  and then we started to see some stuff that we didn't expect to happen. Like the model started
*  to have these representations about emotions and you know, if there is a sad thing and just like
*  this, that stuff was mind blowing to us. Like you have the same voice, everything, and you have the
*  same text that's very sad tone, like, Oh no, like I do stuff like this. And another thing is that's
*  like, Oh my God, wow. And the voice would be completely changing between those two just by
*  changing the text. It was just like, the model has started to have these representations of like,
*  what is a sad voice sounds like and what is like a happy voice sounds like, what's an excited voice.
*  And because in all the pairs of text and clips we trained it on, like it has, it must have seen
*  when someone is saying, Oh no, it's usually very sad voice. So it started to have like, to attach
*  these to, you know, that type of text. And now it can just from text extract these emotions and
*  this style. So when we saw that like change in architecture, like transformers and large
*  language models, that was the reason we started to like invest in this. And it took us like,
*  actually we had the model like very early, like we had some good results, but it was very small,
*  like degenerate to talk like maybe 20 minutes to generate like, like a minute 40, which like
*  impossible to use. And we spent like, we spent maybe six months until now actually we're still
*  like optimizing the performance of the model actually probably in the next couple of weeks,
*  we'll have like a real time streaming API. That's like something that we have been,
*  you know, like to think about how it was very slow at the beginning. And now we're coming to real
*  time streaming. It's like, it's just, it's so exciting. Yeah. I love your enthusiasm for this
*  too. It's, and I feel the same way, you know, it's crazy just how much things have improved in such
*  a short time. Like we're seeing multiple orders of magnitude improvement, you know, in like a year
*  or two years on some of these things, just, just really incredible to see. What can you tell us
*  kind of about the architecture? It sounds like from what you're saying that it's a, you know,
*  transformer based approach as, you know, kind of increasingly everything is these days. Do you use
*  like any sort of off the shelf language model as kind of a base to get started? Do you have like a,
*  you know, for all the different voices that you have, is that kind of a single core model with
*  like different decoders, you know, at the end that it kind of creates ultimately, you know,
*  different sounding voices, you know, you can go as much detail on this show, you can go into as
*  much detail as you want to share. Yeah, it is like a transformer based model. And honestly,
*  that's not like a secret. Like you can see now, I mean, I will get into like a lot of details about,
*  because it's not like one model. It's like a pipeline of things that the engine rates,
*  the audio, because all the models like you that works like in text to speech, you usually don't
*  use waveforms. You don't use audio like training or like using the model itself, but you use like
*  male spectrograms, which is like a representation of audio, like that can be compressed and used
*  much, much more efficiently. But, and then at the end you turn this, you use vocoders to turn that
*  into like high quality audio and vocoders have been something there like for a very long time.
*  But the main model we're using, you've seen, I'm sure you've seen like some of these papers like
*  Valley and like audio LM and like this model. I think people are starting to come up with
*  with like similar ideas, like using transformers, training on like a large data set. I think like
*  the Valley was trained in like 40,000 hours and I'm not sure about audio LM. Like I don't think
*  they released like a lot of details, but like I think these models will start to come up and like
*  they're basically very similar ideas. Like there will be, there are a lot of details inside the
*  model, inside this pipeline to make it, because like one problem with large language models that
*  it's maybe good for images, but it is terrible for something like voice is that these models are like
*  non-deterministic, right? Like this large language transformer model is like, but with something like
*  voice, you want it to be deterministic. You want something like a specific word to be almost
*  pronounced like the same way, right? Or a specific acronym, for example. So this also introduced a
*  lot of challenges that we have been solving and like working around. But yeah, like so it is like,
*  as you say, like transformer based model, like large language model. And I think the trick mostly
*  is also in the data set, like what type of data and how to load this data. And like another problem
*  we face to training the model, because there is no infrastructure out there for training
*  large language voice models. So we had to literally build in our entire infrastructure from scratch,
*  like how to process this data and how to load them into like multiple GPUs for training.
*  And like the data set also part and the diversity in that data set, what voices, what accent,
*  like how long are like, you know, the data pieces or clips you're training the model on.
*  Like there's so many details there that also that are important in generating something that's
*  high quality. You said like different voices, how does this work? So like the way it works now is
*  that you can sample from the model itself. The model have 10 talk in like basically like 100,000
*  voices or something. So you can't sample almost any voice from the model. But what we did to make
*  sure we have the highest quality, we actually went and we got some voiceover actors who we know
*  because they have like specific accent or like something like specific we need to have on our
*  platform. And we got like four or five hours of each one. And then we fine tune the model on these
*  voices. So now the model like, and then there is like a copy of the model that can speak like that
*  person. So and it needs only like one hour to four hours, something like this. And yeah, we were able
*  to, these other voices we have now on the platform, their own like voiceover actors that we worked with
*  and we got them to record their audio for us and in different styles. And then we fine tune the
*  model on that and we make that available to you. But everything is built on the same base model.
*  When you mentioned the spectrogram, some folks might have seen a recent like text to music
*  project that kind of circulated quite a bit, where you would see the spectrogram that would then be
*  translated to the music. But that's quite a fascinating pipeline that it ultimately kind
*  of ends up going through this like visual representation that then gets translated to
*  the audio. I found that fascinating. It's cool to know that you're doing something similar there.
*  Amazing project to see. Yeah. So what are the big use cases that you're now tapping into with the
*  ultra realistic voices? I got to give a plug for the podcast that you're helping to produce with
*  Reid Hoffman. I think he calls it Chats with GPT, where he's literally like sitting, you know,
*  virtually metaphorically, whatever, you know, alongside Chats GPT and having a conversation
*  with it that turns into a podcast, play HD powering the audio of that. Is that like a
*  very random far out use case? Or are you seeing more and more of that kind of stuff? Like,
*  what are people doing with it now? Yeah, actually, we see a lot of like people using that for
*  podcasting also. Another thing interesting also that probably when this episode is aired,
*  it will be already live. We're working with the South Park studios. They're making a new episode
*  and they'll be using one of our voices also for one of the characters. That's super exciting.
*  Oh my God, this voice is now being used in production, actual shows and HBO.
*  So this is just another example of these use cases. And I think this is exactly what we wanted to do.
*  We started with the use cases for L&D and IVR and the traditional
*  next-to-speech use cases. The main driver for us to do that investment, because it was like very
*  risky. We didn't know if that would even work. No one did something like this before. And when
*  the model was like 20 minutes, generating 20 minutes, that's not usable. We didn't know if
*  that's even doable to reduce it to something usable by users. And so we did all that investment
*  because we wanted to get into that market of the human voice, all voice over actors,
*  and the opportunities this can open. Because this was the first time ever you're automating
*  the human voice. Anything that can be done by a human, it now can be automated. And you can think
*  about gaming, production use cases for gaming. Right now we're working with multiple gaming
*  studios where they want to create fully dynamic experiences. Usually you get in games, some
*  characters, they would have voices. And all the NPCs in the game will have like bubbles.
*  It doesn't make economic sense for them to get like a hundred voice over actors
*  like recording all the characters. And now the other layer on top of this, they want players
*  to have a conversation with the NPC in the game. And that's something that's just not doable. Even
*  if you have all the resources, you can't make this work. And the same with another streaming
*  streaming service now. They create podcasts and they want to use this to create also dynamic
*  experiences for people listening to the podcast. Hi, Nathan. In today's episode, you'll see what
*  these things are just like these markets. It's not like something that's already existing and
*  we are plugging, like replacing it with voice and just opening complete new markets. So we're
*  very excited to see these new use cases coming up. And so since we launched this, we have been
*  seeing also a lot of creators. We're getting a lot of YouTube creators now coming and using these
*  voices every day. And they usually, we've seen like two use cases there. These are, they are
*  that a non-English channel or like the creators of the channel, not English speakers. And now they
*  are telling us it's like we have hired a couple of British and American accent people in the team.
*  They can now create videos for us. It's so empowering. And like the other use case where
*  creators are loaning their voices and they're starting to create more content. So instead of
*  you have to go to the studio a couple of times a week with one interview or like to record a video
*  or like a product review or something like this, now you can just have the video create, like write
*  the text and then have that on top of the video in minutes that used something that used to take
*  like a long time to do. And like we are very interested in the use cases around voice loaning
*  as well. That's like one of the things that we have been investing in. And yeah, we're very excited
*  to see like what people are coming up with. I just want to talk a little bit about the challenges
*  that you guys are still facing. Obviously this technology is maturing rapidly and the fact that
*  you're doing stuff with South Park and HBO and all that, that's incredible. I'm just kind of
*  understand like what some of the trade-offs are that you are facing and what kind of some of the
*  challenges are as you go toward this more ultra realistic approach. The reason like these other
*  models like they have all these features like this is a mill and you can control styles and that stuff
*  because they are very mature. Like they have been in the market for a very long time and people have
*  been working with this for a very long time to add all these capabilities. But on the contrary,
*  with like the large language model approach, we literally like just did this like five months ago,
*  right? And we have been so focused on performance and optimizing it to actually work like in almost
*  real time or as close to the existing models as possible. So it will be usable for users because
*  when I tell you like someone is like paying for like 12 hours a day working on this, if that takes
*  each generation takes like one minute more, that's where he will be taking like another like
*  like like be like a long like way longer process for him, right? And the iterative process,
*  the feedback loop is very important that you create something, you listen to it, you see how
*  it sounds, you try different voice, different characters. We wanted to make that feedback loop
*  as fast as possible and I think we did it. But right now and the reason that I told you we trained
*  another model that's actually much bigger and solving many of the problems the first model had,
*  one of these problems are actually these like pronunciations and the control of on the voices.
*  Right now, we have a lot more control on like adding things like emphasis like the specific
*  word or adding like pauses or make the voice speak in a specific style like like, for example,
*  like an audio book, like a narrative style or a commercial style or a training like like
*  instructional style like these things where it's still the same voice, the same everything, but then
*  it will not be as dramatic if it's instructional, for example, or as emotional.
*  And then there was some styles like meditation or these things where it was actually very hard
*  to get the voice completely changed. It's like wave speaking. But so this new model will
*  is solving like most of these problems. And over time, we're adding more and more of this control
*  because if you're thinking about this model for the users, if you now think of like for the job
*  to be done, it's this model for the user is like a human voice over actor. And the user needs to
*  tell him, no, like, you know, speaking like say the same in a different international, like be
*  more excited, like increase your voice here. Or like this pronunciation needs to be a little bit
*  different. You know, it's like how would you actually tell an actual human voice over actor,
*  right? And we are seeing that feedback from users now. And we were surprised at the beginning. I
*  mean, that's like way better than the other voices. Why people are complaining about these things?
*  Because now they are not comparing it with sticks to speech. They are comparing it with humans.
*  And that was like a complete shift in like the mentality that, okay, actually this needs to be
*  directable. Like you need to be able to direct that voice exactly what you want. Like what you're
*  saying, like all that stuff with this email. And now we are so we are actively working on these
*  things. And I think in the next few months, all of that will be out and it will be almost like
*  on par with like the existing voices. So what do I have to do to be a beta tester is my first
*  question. Kind of hear from what you're saying there that your vision for this next generation
*  is maybe less about like an SSML, which makes sense given what you've told me about the
*  the market, right? You don't see the big opportunity in terms of like taking share
*  from systems that are still in production that are, that do support SSML, but rather,
*  it sounds more like we're headed for kind of prompt engineering for voices. And so I'm
*  imagining myself kind of being like the moment that, you know, a grandfather first saw his,
*  you know, grandbaby and like getting the voice to come out with the appropriate emotion from those
*  kinds of like qualitative scenario narrative type descriptions, which, you know, is I think what a
*  director on set would say to an actor, right? They certainly don't give them SSML notation.
*  So am I getting where you're going there? Like, are we all about to become prompt engineers slash
*  directors? Exactly. I think like our goal in this, like eventually that we have something that
*  people can totally control the voice. And I think that you spoke earlier about that, the transition
*  from like a text to speech company to an AI company and that now in text to speech, you have like a
*  specific set of voices that turn any text into that voice speech, right? But now you want to have
*  like a lot more control on that designing the speakers, like the actual voices, like that you
*  can, okay, I want this voice to because this actually what happens, like I want a voice that
*  sounds like, you know, optimus prime voice, like, you know, the deep voice was like, but you know,
*  like it will be a little bit like slower. So this is how people actually think about it, like content
*  creation. And if you think about the future of content creation, it would be something like this.
*  People are just becoming narrators or they just describe what they want. And then, you know, it
*  will be generated and they start using it. Like instead of them actually sitting and doing the
*  work themselves, they would become just, they're describing like, like what's happening with images
*  now, right? You're just describing what they want, what you want and you generate it. Then you iterate
*  over it again and again, until you have the exact things that you had in mind. The things that used
*  to take days from like artists or designers right now, it can be done in minutes. If someone has the
*  right ideas and how to iterate over this and help like to guide this like machine or this model
*  into the right direction of generating what you want. And I think the same is happening with voice
*  where you will be able to design these speakers and create voices of exactly what you want and
*  then start using them. So I totally agree with you. I think this is where it's going.
*  You mentioned briefly earlier, the fact that these models are in some sense, non-deterministic.
*  And there is some level of just like GPU indeterminacy, which is basically irresolvable
*  at like the software level right now, or at least would be extremely difficult to avoid.
*  But I also understand that that's like pretty rare and only kind of comes up when, you know,
*  values are very close to kind of rounding points anyway. So is that what you mean by like you,
*  you can't make them determinate? Okay, there's two points there. The first thing I'm comparing
*  this with the previous generation of models where it is very deterministic. Like if you put the same
*  text with the same voice generated 10 times, they will be identical. There'll be no difference.
*  But then with this thing, if you put the same voice and generate in samples, it will be different,
*  like one sample from the other. There might be a very slight difference. Sometimes it's a little
*  bit more like more than what you want, like like big difference in the way specific words be
*  said or something. And that with text to speech, that determinism that means that the user doesn't
*  can't just come drop in an audio book and click convert and just, you know, get and forget about
*  it. Right. He needs to sit and make sure like it is actually exactly as he wants, like what he wants.
*  And that's that introduces a problem based on the use case. Some use cases, people actually want to
*  do this. They want to come with a big document, drop it there and have some something that's 100%
*  words, like say things exactly like what they want in the same specific style. But in some other use
*  cases, that's actually is a feature where you want to generate again and again and see which,
*  which actually which intonation like it's like, like compared with images, like where you generate
*  10 images and you can maybe choose the third one because it's exactly like what you had in mind.
*  And then you iterate more over this. And so exactly the same case here. So we allow users to
*  generate like multiple samples and they listen to them and they choose the right one. And the
*  good thing about this, that this data also is very valuable for actually writing the model,
*  like what people prefer to use in like, in like different scenarios. So like this is like the
*  point of like undeterminism there where another point with especially things like, like acronyms
*  or something like where sometimes when you generate, like generate again, the model might
*  pronounce like, because there's some words that the model never heard about before. It's like a
*  company name or like some weird acronym or something like this. Like it might be hard for it like to
*  get it like right every time. Now we have people in the team who have like a long experience in
*  speech processing. And now we started doing some stuff that the traditional models that used to
*  do to make sure we have this like kinetic representation of like words and pronunciations
*  and try to like freeze that stuff in the model where it can't, it will always like generate
*  these words in that way while still keeping the undeterminism for the other stuff like going on.
*  And the good thing about also voice, if you again compare it with humans, I mean, if you ask the
*  same person to read the same sentence 10 times, there will be actually difference. It will be
*  the same all 10 times. There might be slight difference, but there is a difference. So,
*  and people are okay with that. But then it comes the issues when like with pronunciations or
*  or with if this undetermined or like this random like generations are for specific words are not
*  carrying the right emotions or styles they want. And that stuff we need to give them the control
*  to do this when they want. And but by default it should be, users should be able to discover
*  like these different styles in like this like randomness and be able to select the one that
*  matches what they think is the right way of saying this again, matching exactly how humans speak.
*  Unlike a technical level, is there sort of a setting that you could also think about exposing
*  that could be like the equivalent of a temperature? Actually, yes, like and this new model that we
*  were creating, there are actually a lot more than just temperature and like specific state you want
*  the model to use or something. There are like things like how like the voice guidance, like
*  when you try especially to clone a voice, for example, you want it to be identical, how much
*  resemblance you want it to be the original voice versus to be like a little bit like it. Like you
*  wanted to preserve the same accent. You want it to be exactly like that voice or no. So like
*  there are a lot more when it comes to voice like and some stuff like a lot related to like some
*  attributes of the voice itself, like its style, it's like gender, it's for example, like you can
*  add the voice, you can add it to make it like a female, but if the main voice is male, it will
*  become a little bit feminine, but like it will be still like a male voice. But there are a lot of
*  like good stuff that you people can start using and tweaking exactly how they want the voice to
*  sound and then start using this. So that's stuff that we're actually starting to expose the users
*  and be able to have more control on designing these speakers that they'll be using.
*  This conversation and just the way you're speaking about your product does actually remind me a lot
*  of talking to Sue Hales for the first episode, just because control, control, control, control.
*  We've got this amazing technology now it's blowing people's minds. And now how do we rein it in and
*  really make it work for us? You guys obviously have different versions of that challenge,
*  but it's fascinating to hear, you know, conceptually how much commonality there is.
*  Let's talk about languages just for a second. Is it just a matter of lack of training data that is,
*  maybe also market, but you know, from a technical standpoint, is it just like training data that
*  prevents you from expanding the ultra realistic voices to other languages?
*  Actually, not just the training data. I mean, you don't need the same amount of data for other
*  languages. I mean, we have created internally some Japanese and Portuguese voices and the
*  result was actually better than what's available in AWS and these APIs only from maybe like 10
*  hours of audio, because the base model knows how to speak very well like humans. Now you just need
*  to train it how to speak like a Portuguese accent, for example. And the other challenge there,
*  because our model wasn't trained on phonemes, so sometimes like these other languages will have
*  specific types of characters, especially with the non-English, not like the voices are not,
*  what's it called, like they don't have like the Roman scripting. They will have like just Japanese
*  like, or like, you know, these languages that you need to train, like what's called like a G2P or
*  like you need to train like a phoneme encoder to be able to understand like that script when you
*  give it to the model to translate. And once you do that and the model can just understand phonemes,
*  it doesn't matter. You can just train it on any language or fine tune it in any language.
*  Another thing we're doing now is just we are actually going to train like a large language
*  model that just from scratch that has like multi-lingual. The reason for this that we think
*  that we will start to see some capabilities of like cross-language like speaking where
*  right now actually we have it for English that if you upload like a voice, if you try to clone a
*  voice in that speaking in for example French and you if you go there like you clone the voice it's
*  available in your like studio, you can then start using it, you will get like an English voice with
*  a French accent. I honestly didn't expect that this will work like and it was like mind blowing
*  when I saw it but it works so well and we tried many voices across like and it works like even
*  a lot better with the new model we're training even with like few short training. You show it
*  literally like a 30 seconds of like a Japanese accent and you will get an English person talking
*  but with the same accent basically the same voice but speaking English but with it's like as
*  if like a Japanese person starts to speak English and he has the accent it just it is like amazing
*  and you can think about the capabilities of this with something like dubbing for example you can
*  have the same actor like across languages same talking in the same voice but in in that different
*  language and then so one of the reasons we're thinking of training that like multi-lingual
*  model that to start seeing this like not only from any language to English like what you have
*  now but just across languages you can have the same voice so you design the voice for your game
*  or your audio book or whatever and you love this voice in the way it talks and tune or everything
*  and then you want to just take this and make it available in every language in the same voice but
*  then speaking that language so this is what we're trying to do. Does the compute itself come with a
*  huge price tag for you guys and how do you manage that? Do you do it just on your own in the cloud
*  or do you work with like a mosaic or some sort of like specialist large model training company?
*  Currently we're doing everything on our own but it's usually inference is not expensive
*  like inference is like I mean and users are paying for inference so it's not like a problem
*  and right now the model is very optimized is that even for voice clones are built like so that like
*  infrastructure that can load and load like all models on the fly in the GPU memory and handle
*  like hundreds of models per GPU so we did a lot of work on optimization on that infrastructure side
*  so it can scale really well now so there's no problem with that usage side when users are using
*  and scaling that but the problem more is or the cost comes more with training like this model
*  we're training now like we're finishing it actually it cost us like hundreds of thousands of dollars
*  to I mean it's not like millions like you know these other like large language models but still
*  for a startup that's like a lot of money and the good thing is that we have been in this market
*  for a very long time like for like three years now we have a lot of customers and we have like
*  very like decent revenues that's covering everything so far so I think that's not a
*  challenge for us now the challenge would be if we really want to scale this a lot more in training
*  and experimentation and also most of the cost what we found is not only in training this one
*  large model but actually it's a lot more in experimentation training like a very like
*  much smaller models to for example when we did this like language like Japanese and Portuguese
*  wanted to know is that actually doable is that like can you just fine-tune this on another language
*  and it works if you train this on phonemes so this took like a couple of weeks not months to train
*  but then like so this like this experimentation and we do a lot of these experiments to to improve
*  the models to do these things like what we have been talking about is like control and phonemes
*  and pronunciations and languages so this continuous experimentation is actually it's like an R&D
*  department yeah like it costs a lot of money and I think that's that's that sort of it's still
*  like working fine with us like but over time I think these models will reach will reach a point
*  where we'll exactly have what we want and hopefully we don't need to do the same investment again in
*  to get like the same the same feature because right now it's lacking on a lot of features in
*  the existing models and we're trying to get there in all these features so one of the reasons for
*  that also is that we are trying to train our own models we're not using like you know like an API
*  or something from from another company or something that's already open source so that also comes with
*  that cost you're just sort of trying to to build the operating system and the applications at the
*  same time right so yeah I think this is like where the cost most of the cost is just kind of thinking
*  out long term one of the things you said there triggered a thought for me which is just like
*  voice unlike other things seems to hit just even conceptually a certain kind of plateau
*  when it achieves like human voice actor level I don't know necessarily what it would mean you
*  know I do know what it would mean to be superhuman at you know many tasks but when it comes to
*  producing human voice like you know almost definitionally like you can only be
*  so good and then you're beyond like what is superhuman right in that in that domain so
*  do you think do you see things kind of leveling off at a point where like the models are so good
*  that they can kind of do what you want them to do and you can kind of stage direct them
*  and you know they're they're like easy to use do you see that the core technology at some point
*  becomes like commoditized and even like open source and just kind of generally accessible
*  there are two questions there like one on the model itself like what will happen is will this
*  become a commodity and another thing on if this became a commodity what will happen to the
*  application right so like for the model itself I think eventually like the improvements you're
*  trying to make on the base model will be will start to give you like diminishing returns where
*  like yeah you know like speech recognition for example like they reached a point where
*  okay right now every speech recognition system is like 95 percent good just I mean to move from
*  95 percent to 98 percent it needs a lot of work but based on the use case almost all of them are
*  like 95 percent like you know accurate or something so I actually don't know but like I think they're
*  all pretty good now so I think the same will happen with voice but then the difference we're
*  seeing here will be this that yes there might be some open source or an API available in like a
*  year or two from now that's that has similar quality to what we have today but then for the
*  specific use cases to be able to generate voices and have like this specific workflows for gamers
*  for example or or like people are working on animation movies or this thing I think mostly
*  we will need to train like some specialized models or fine-tune bit like on their data like
*  something that is specialized that can give them exactly what they need and that wouldn't make
*  sense for for example open AI if they're if they have like a model that's available and very cheap
*  or or stability if they have like a model that's available you know and open source
*  because they are trying to build something that's generic that everyone is using right
*  but we we are interested in specific verticals specific use cases where we can go and build like
*  these specialized modules for these use cases that works really well in what they want and
*  the other thing is if you think about we are now talking about also the use cases that have data
*  sets available like publicly right but if you think about things like customer support or like
*  sales calls or like these things you cannot go anywhere and find 10,000 50,000 hours of
*  customer support goals right I mean like now we're working with some like some partners who have
*  this data like that's available but and private data from like you know their customers and then
*  we can train that model and provide them a solution that replaces customer support for example but
*  no one will be able to compete with this because like this data is not available for anyone to
*  train and have a variation and it would make sense for everyone to have 100 modules for all
*  different use cases so I think this is where we can start having some something that's different
*  from the market and the other thing is you know for example like copilot has been in the market
*  for like two years now like one half years and I'm not sure if you know that like almost all
*  FANG like like all the large companies they're not no one is using copilot even though it's like
*  so good like it saves you a lot of time but why they're not using it because they are afraid if
*  they use it that like their data will be like you know leaked or like I don't know open AI or like
*  whatever for like privacy reason so that's another thing that like these companies who want to create
*  like right now we're talking with some like big production studios who are very careful about the
*  voices like that they have actual actors like they're you know like that and they want us to
*  learn their voices to use in post-production in these use cases and they're very careful about
*  this and we would have mostly to just give them like some you know in-house deployment of the
*  model trained on their voices on their actors because if something like that like that leaked
*  that's a big problem for them right so I think these things were for enterprises and these
*  big production companies where you will have to have like a solution that's specialized and
*  deployed internally to give the privacy and and you know like these things for them I think I think
*  that will be some things that can like protect the business from just like you know opening this for
*  everyone but I agree with you that the individual use case over time will become very competitive
*  when opening eyes for example like opens an API for this everyone will start building applications
*  like and so many startups will start building something similar right to what we're doing
*  and the individual use case will become very competitive but then the companies like production
*  or gaming or like the enterprise use cases they will still need something like specialized for
*  them and the other thing on the application side this is where the difference between like
*  building the operating system and you know the applications right now we are doing both but
*  eventually going deep into these verticals and building more tools for them around what we're
*  doing this also will be something that that will be special to like what like our offering for them
*  like to give you an example I mean even not with this model with the old models we had
*  we had a team from Amazon using us and they have AWS volume but the reason for that they didn't
*  want to go hire a developer and build their own solution right like they just wanted something
*  really they can use and start you know getting their job done and the same will happen here if
*  OpenAI has an API tomorrow or like anyone else like the same will happen like companies will start
*  will continue to use the applications that has a UI as they can just use and get their job done
*  quickly it's one of the best rundowns of long-term motes that I've heard and you know really echoes
*  also what OpenAI is doing and kind of you know the new market reality that they're creating right
*  now in the language model space you know it is striking to see that that is now at two dollars
*  per million tokens functionally free for a lot of use cases but at the same time they're doing
*  exactly what you're alluding to which is they're going and selling seven figure deals to you know
*  major companies that have data that you know I don't know if they're doing any on-prem
*  offerings at this point or not but certainly walling things off from other people's data you
*  know all that is going to be a huge concern for them and for their customers especially driving
*  it so it makes total sense that you would feel some of those same you know tubs and be moving in
*  in some of those same directions everyone is asking this question like like will this be all
*  these foundational motives would that be monetized and does everyone will will have it and there will
*  be no value in that but I think what what this question misses is that like this is just like an
*  operating system that then there's like two things there like this like specialized things that you
*  can build for enterprises and for specific use cases and then the applications that can be built
*  on top of this because of different layers of this right like exactly like in cloud for example
*  right there's like AWS and Azure but then there's so many application layers on top of that that
*  still make a lot of money on like make like huge businesses was that so let's go back to cloning
*  then for a second I think this is going to be you know one of the most powerful features or use cases
*  that you offer it's certainly in time if not already will become one of the more controversial
*  as well at this point you can go into playht and upload 10 minutes of audio of you speaking and
*  then and I was able to send you the first question from my list of questions in my voice
*  generated on playht it was honestly all very easy very smooth and it was as much as I have
*  shopped for this product I confess it was the first time I cloned my own voice and it was kind of a
*  wow moment you know again as much as I've shopped for this like hearing myself come out of the
*  machine and it you know it really does have a obviously a very high resemblance to my voice I
*  thought that was you know kind of eye-opening so what are people doing with cloned voices how much
*  of the usage is that and then obviously you know we got to talk a little bit about kind of the
*  societal impact and the potential for abuse so I'm curious to know if you're already starting to see
*  some of that as well you can get like almost 100% resemblance I have multiple that times where
*  users will send us say I sent this to my wife and she didn't know it's an AI voice like and like
*  like one of the things we are experimenting with just about like voice cloning so you know we had
*  this idea of what if we make phone calls to sell our product you know it made this like I mean
*  sales like we have like SDRs and our team that are hiring them like to make phone calls reach
*  out to people who are outbound and like you know still our product companies they say okay you know
*  what like when I listen to these calls they seem very basic hey are you interested in this product
*  yes no okay let's have a call so we did like you know we we hooked up chatgbt with our with our
*  voices and we we started making these calls and I mean we were very surprised that no one no one
*  figured out it's an AI voice on the call like it's very surprising because like we're saying
*  actually maybe people will like feel like it's an AI voice and they will you know like hang up or
*  something like no it's like just normal conversations it's like actually we're like just thinking to
*  share some samples and voice or something but now this technology is becoming like very very good
*  in this that as you said it's also dangerous so right now like about the abuse issue and
*  that's something that we thought about a lot and actually one of the reasons we spent a lot of time
*  I mean that's available from day one the model can clone any voice right actually all the voices
*  we have now available these are just voice clones voice over actors that we got and cloned their
*  voices and now making them available for everyone to use so but we were very careful about like
*  releasing this that we started by just you know like asking people to sign up have a call with
*  us try to understand what they want to use this for what is the what are the use cases well we
*  didn't know I mean that's a new market for us for like voice cloning and we wanted to know what
*  people would be using that for and we had like we spent probably a couple of months just having a
*  lot of call to these customers trying to understand their use cases and out of this came a lot of like
*  youtubers and podcasters and you know these use cases talking to understand them more and
*  then when we launched it at the beginning it was very strict process that a lot of like manual
*  reviews and wasn't scalable at all because we have been very careful about up use here until we built
*  we managed to we only opened it up like as well like the thing that you used now when we did two
*  things when we added moderation when we managed to add moderation to our studio where right now
*  everything going through the API is going through like a very strict like moderation policy that if
*  you try to like you can try to try to go and put something like you know I know something very
*  offensive or racist and it's really hard to you know make this right I'm sure everybody knows that
*  but we're trying to be it's it's okay to have some you know like false positives there like
*  we might end up like looking some users by mistake or like stuff like this compared to having someone
*  you know like being harmed through this technology so we did this like we added this moderation in
*  our through our APIs our platform and we tested it well and the other thing we added is that we
*  built this classifier and this is like very hard problem to solve that building that discriminator
*  and I know openly I actually trying also to build this for gpt for chat that can tell if a content
*  is actually human generated or AI generated and we built that classifier and it's available publicly
*  on our website for free that anyone can go drop like an AI generated like audio and be able to tell
*  if it's AI generated or human generated and I know this doesn't look up use in itself but we're
*  hoping that this will start to advance and hopefully like more and more people can you know like win
*  this classifier like being advanced and being able to detect a lot more of these cases of like AI
*  content it will like maybe be integrated in like social media or like with banks or like we know
*  with this like entities that depend on like voice as like a way of like you know logging into your
*  account of like your biometrics or with or like with that stuff like that on youtube or other
*  you know places where you have some maybe fake news or something and hopefully these platforms
*  can have you know some message to inform the user okay you know like what twitter has now with
*  community what was it called community signals or something like where
*  yeah notes where where they have this message okay you know this content actually this actually
*  this is wrong this not like there it's a real thing that's what's real and maybe if they have
*  something integrated like this they can start to tell people this is actually wrong right now
*  some people are using other services to create fake ads on on tiktok from like joe rogen voice and
*  these things like he's recommending some product it's it's very dangerous right like and so and
*  like some people are reading an article a couple of days ago someone used like a service like this
*  to defer all the family and to like you know thinking that their son is in jail and they
*  need to send them money or something like this so it's very like that stuff is very dangerous to
*  to do so we're trying to i think like what like sam altman was saying that like he is hoping like
*  this technology like a gi like will will take a little bit of time until like you know like that
*  society i'm like paraphrasing it like until the safety like it's used to you know like gets adapted
*  to that technology so i think it is even more like so for voice because for images the society is
*  already sort of ready for um you know like generated images like you already doubt anything you see in
*  social media now it might be photoshopped like something have been there for like 10 years
*  but for voice if you hear a voice saying something if you get a call from your brother saying
*  telling you something you don't like i mean the first impression is not like are you you know the
*  real person or that's that's not right that's not right like you just because that's not yet like
*  very common in society that they these things are so real but this will happen over time they will
*  have a doubt like for everything like any media you see you the first thing you will you will have
*  is that actually real is or is that a deep faith because right now this will become so real that
*  you cannot tell the difference and it will become worse over time so i think it is like a matter of
*  like you know like responsible companies who try to like have the tools and like in place and have
*  the things as much as possible to look like the abusers and at the same time like you know like
*  the society is over time getting used to the the fact that now voice cloning and deep fakes and
*  the same will happen soon with like videos right now lip syncing is becoming very good that there
*  are some like videos you know like you can see with just like some like lip syncing voice of like
*  jorgen or like other or like why they're like other people like saying something they didn't say
*  and that's very dangerous but the society like over time will get used to that like it will not
*  trust like you see something like on any source i don't know what's the solution for this or the
*  society but i mean we're trying to be in the middle where we mitigate the abuse as much as we can
*  through these tools and the operation and at the same time offer a service to users that they will
*  find it useful and easy to use yeah that all makes sense it's a tough it's a tough challenge and you're
*  not by any means alone in in facing it two really quick follow-ups there one on your discriminator
*  is that something that works like across audio generated by other text-to-speech products as well
*  or does it depend on like a signal that you're embedding in or you know or maybe just naturally
*  occurs in the audio that you create it depends so it catches some stuff what we noticed from like
*  testing it from our models and from other other stuff in the market but it's less from the other
*  stuff on the market and it can get a lot better i think i think this is just like the first version
*  of it like this can get a lot better in detecting because these voices generated through transformers
*  for coders and like you know these models they have specific they leave behind some specific things
*  that you can detect and you can over time if you really invest in this across different types of
*  coders and like approaches or generating like decoding the audio to create like waveforms and
*  that stuff you can start like you can start to reach a point where it will be very very accurate
*  but again i say it's a very hard problem to solve like to have something that's very you know like
*  a discriminator that's like very good in detecting any ai generated content that's a very hard problem
*  to solve and but having something that's accurate enough i think it can at least mitigate a lot of
*  abuse if it if it's deployed in the right places and you know like like the same it's the same idea
*  was like fake news and like these things so i think it can like the idea here is to make it you can if
*  you can mitigate that like 100 at least make it like 90 so most of the abuse is is mitigated and
*  you know trying to do you know like as much as you can is there any way to detect like commonly abused
*  voices i mean i'm sure there would be a way if you had a small enough set if it was just Joe
*  Rogan and Joe Biden you could probably you know solve that relatively easily but is there a way
*  to kind of extend that do you think it would be realistic to extend that to the hundred thousand
*  you know most well-known people that that folks might want to clone and abuse a voice of yeah
*  we actually thought about this so there are some data sits there for celebrities for example
*  but the problem there and you can build the classifiers to detect these voices and lag
*  like if the user tries to clone like a celebrity voice but the reason we didn't invest in this
*  because we found actually learning celebrity voices maybe it's not the most dangerous thing
*  but the most dangerous thing is calling maybe like politicians or voices of common people and
*  defrauding them right because like when you're running a scam trying to get into someone's bank
*  account with his voice i mean we will never be able to find that person's voice and put it in the
*  classifier right that actually is the most dangerous thing and that's why we went with the
*  approach of okay when someone clones a voice what will they do with it they will try to write use
*  our api or or editor and write some text and generate audio in that voice and then so then
*  we thought like having this moderation layer and then flagging these users and blocking them this
*  can be a lot more effective than just having like like you know a database of like voices that we
*  can detect i've done a little bit of this kind of red teaming work on language models and in that
*  context yeah it makes total sense right like what is the content you know people asking for
*  somebody's you know mother's maiden name is probably a pretty good red flag you know that
*  they're uh they're up to no good if you imagine so if we started to have like some like humans like
*  moderating this these use cases and i think we have like a large language module or something
*  that we can fine tune on this data and be able to tell with some probability if someone is because
*  sometimes if someone's trying to get into someone's bank account the classifier might not detect it for
*  moderation but if over time you start to detect these use cases that's like going you know like
*  going through like these cracks of the the class of the moderation detection and then you add these
*  things there over time i think it will get better and better in that a lot more than just if you try
*  to detect the voices and and and block users based on this really enjoyed learning a lot about
*  how you're thinking about the business how you're thinking about the technology i'm you know very
*  excited to see the next generation larger model and all of the you know prompt engineering or
*  stage direction type of use cases and modes that it's going to unlock it sounds like you're really
*  on the verge of another big step forward so i'm excited to see that i've got three kind of quick
*  hit closing questions for you first one is what are the ai tools that you are using in your
*  day-to-day life right now that you would recommend that others check out i think definitely chat gbt
*  like i mean i'm using it now for like summarizing things if i have like a like a very long email i
*  was just like a little bit there ask it to summarize it or more also for i mean for writing any code
*  now which i just is just like it doesn't make sense to do something else i just i use it and
*  you know keep asking it okay like you know changes from python to just script or like whatever and
*  like you know like do like all the things that you want to do so it is really good at this i do use
*  grammarly also so i think i think it is they have actually i think they are like one of the biggest
*  like maybe ai tools like more touchy bit is grammarly but like no one sort of like knows about it but i
*  use it also like a lot it gives like a lot of good suggestions now when you're writing emails or
*  or these things based on the context you're doing yeah chat gpt certainly the number one answer
*  there you're actually not the first to mention grammarly as well do i infer that like chat gpt
*  has kind of crowded out copilot like you you are finding that you just want to go to the the better
*  ai to do kind of longer code generations i i think like i mean i'm still using copilot but like
*  mostly when i'm starting something like writing something new and they won't just like like
*  judge it feels like um not like an auto completion like like uh like how like you might get from
*  copilot but it is just it's like you're you're having another developer next to you and you're
*  thinking about different things okay you know what like let's let's change this from you know
*  this like let's add some like rate limiting here how would this work and then you write this and
*  send it as a code and wait for the response okay you know what like let's change this from
*  this language to that language like that's like very quickly you know these iterations until you
*  reach something that you want to use and then you take this into your editor and then you can use
*  like copilot there so i'm seeing like i feel like that chat based like coding i've never expected
*  this like i mean if you describe this to me like a year ago i would say this one i would never use
*  this but it is actually it is actually pretty good it reminds me as you know like my career
*  sometimes i would have interns working with me and it is very similar to that it's like you're
*  working with an intern and asking him to do something and then he would go do it and then
*  comes back with it and then you can like think with him like another iteration and then he would do
*  the same it feels very similar to that yeah i think that's very apt i use that metaphor
*  pretty often these days too and it it works on you know kind of a couple different levels right
*  like it needs a lot of context you know it's uh it really benefits from a couple examples of what
*  good looks like you know aka few shot learning so there are i think a couple of um you know pretty
*  profound parallels there to the the intern that that does make that a useful way to help people
*  especially if they're new to the technology to understand how they can get the most out of it
*  hypothetical situation i'm sure you're familiar with the company neuralink
*  let's imagine sometime from now i don't know how far into the future this will be that a million
*  people already have a neuralink implant so you're not going to be the first but the question is
*  would you want to be the one millionth and first if getting the neuralink implant would allow you to
*  basically have thought to speech like you could type as fast as you could uh as fast as you can
*  think your words can just be you know your thoughts can be translated to words and stored in the
*  computer would you be interested in getting that implant for that capability i think i might try
*  before a million for a million even it's yeah like i mean it is it's just like it's it's amazing like
*  so exciting thing to see i mean if this works because like the main things there is that like
*  the bandwidth for humans like you think about something then you have to write it and
*  and you know do this like thing yourself your manual you know physical thing but then when
*  if you're able to change your thoughts maybe to like a machine directly and have it like interact
*  with it like the bandwidth would be like a lot more like like a lot like bigger and wider than
*  if you're just using your own you know like hands to describe something and and and stuff like this
*  i think it would be so powerful and people who will have this they will start to advance really
*  quickly into like what they can do and like their capabilities and uh yeah i mean it has to be safe
*  of course but like yeah i would try for sure just zooming out entirely you know kind of biggest
*  picture what are your biggest hopes for and also fears for the the ai era that we are entering
*  you know kind of as you think about how things will play out over the rest of the decade
*  i've been thinking a lot about like this like ai safety stuff and i i don't know i will not like
*  comment on this but like from because there's so many opinions there and so many people like
*  say you know like different things about like try to predict what will happen in the future but like
*  i think like what i hope like will be that you know the community like the society will get the
*  chance to adapt to these changes and this will be very empowering and these tools will help us to
*  be like a lot more productive in and there'll be like a lot more progress for the for humans in
*  in the next like what like 10 years or like like i hope that would be like a lot more positive and
*  what i hope doesn't happen is that like the legal side of the legalization of this technology now
*  like like we're seeing now with the stability getting sued because of like what they're trying
*  to do like you know and like there might be i hope that doesn't introduce another winter to
*  the technology and like delay it a lot because if this happens in like this market like they're
*  trying to be responsible it will still like other markets who are not as responsible we still keep
*  it open and they will be able to advance a lot faster and so it is very important that
*  like that the legalization of that can be you know like when you think about something like
*  with the internet like we know with like platforms like facebook and twitter and these things
*  not being like responsible for like that user are posting on their platform you can you can
*  argue the benefits and you know like the like the disadvantages of something like this but you can
*  not argue that that is one of the reasons that made this platform huge and really big and impactful
*  and useful for a lot of people and if that was wasn't the case that like everyone who posts
*  something that you can just go and sue like facebook for it like they would have died like
*  long time ago right so i think i hope that the society overall will be able to adapt help like
*  progressing that technology into the benefit of humans and because i think it can be really useful
*  and people can become a lot more efficient and productive and like the overall gain for like
*  like the society can be huge from from a technology like this again this has been a fantastic
*  conversation Mahmoud Felfel thank you for being part of the cognitive revolution thanks Nathan
*  i enjoyed it thank you so much Omniki uses generative ai to enable you to launch hundreds
*  of thousands of ad iterations that actually work customized across all platforms with a click of a
*  button i believe in Omniki so much that i invested in it and i recommend you use it too use cog rev
*  to get a 10 discount
