---
Date Generated: September 06, 2024
Transcription Model: whisper medium 20231117
Length: 2807s
Video Keywords: []
Video Views: 500
Video Rating: None
Video Description: Nathan interviews Andrew Mason, CEO of Descript, about their AI-powered video editing platform. Learn how Descript is transforming content creation with features like AI transcription, custom voice overdubbing, and eye contact models. Discover the future of video editing and how AI is making it accessible to everyone in this insightful episode of The Cognitive Revolution.

Looking for podcast production? 
Our production team, led by Adi and Sai from AI Podcasting (https://aipodcast.ing), is now open to taking on additional clients for podcast production and AI-driven workflows; if you need help with your podcast, you can contact them directly through their website (https://aipodcast.ing/contact/) or reach out to me for more information.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: Second Opinion
A new podcast for health-tech insiders from Christina Farr of the Second Opinion newsletter. Join Christina Farr, Luba Greenwood, and Ash Zenooz every week as they challenge industry experts with tough questions about the best bets in health-tech.
Apple Podcasts: https://podcasts.apple.com/us/podcast/id1759267211
Spotify: https://open.spotify.com/show/0A8NwQE976s32zdBbZw6bv


SPONSORS:
Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-TCR

Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsor: WorkOS
(00:01:22) About the Episode
(00:04:23) Introduction
(00:05:18) Creating Descript
(00:06:53) Favorite Features
(00:10:41) Descript Workflow
(00:14:10) Product Strategy (Part 1)
(00:16:45) Sponsors: Oracle | Brave
(00:18:49) Product Strategy (Part 2)
(00:18:49) API Access
(00:23:50) OpenAI Partnership
(00:27:01) Expensive Product Version
(00:29:20) Multimodal AI
(00:31:12) User Fine-Tuning (Part 1)
(00:32:24) Sponsors: Omneky | Squad
(00:34:10) User Fine-Tuning (Part 2)
(00:34:54) Content Creators
(00:35:54) Monetization Challenges
(00:37:20) AI Avatars
(00:42:20) Small Businesses and AI
(00:43:42) Hiring AI Engineers
(00:46:25) Outro

---
SOCIAL LINKS:
Website : https://www.cognitiverevolution.ai
Twitter (Podcast) : https://x.com/cogrev_podcast
Twitter (Nathan) : https://x.com/labenz
LinkedIn : https://www.linkedin.com/in/nathanlabenz/
Youtube : https://www.youtube.com/@CognitiveRevolutionPodcast
Apple : https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify : https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Underlord Descript’s AI Video Editor, with CEO Andrew Mason
**Cognitive Revolution:** [August 03, 2024](https://www.youtube.com/watch?v=oTf5qAAJ9H8)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  This episode is brought to you by Work OS. If you're building a B2B SaaS application,
*  at some point your customers will start asking for enterprise features like SAML authentication,
*  SCIM provisioning, role-based access control, and audit trails. That's where Work OS comes in,
*  with easy to use and flexible APIs that help you ship enterprise features on day one without
*  slowing down your core product development. Today, some of the hottest startups in the
*  world are already powered by Work OS, including ones you probably know like Proplexity,
*  Vercell, Jasper, and Webflow. Work OS also provides a generous free tier of up to 1 million
*  monthly active users for user management, making it the perfect authentication and
*  authorization solution for growing companies. It comes standard with rich features like bot
*  protection, MFA, roles and permissions, and more. If you're currently looking to build SSO for your
*  first enterprise customer, you should consider using Work OS. Integrate in minutes and start
*  shipping enterprise plans today.
*  Hello, and welcome back to the Cognitive Revolution. Today, my guest is Andrew Mason,
*  CEO of Descript, the AI-powered video editing platform that's revolutionizing content creation
*  by making it as easy to edit video as it is to edit a text document. As you'll hear, we at the
*  Cognitive Revolution are longtime users of Descript. It's an integral part of our production process,
*  and we can sincerely attest to its radical ease of use. In this conversation, we get into the
*  details of how Descript is using AI to reimagine the content creation and editing process. This is
*  a journey that began with a novel editing interface built on top of AI transcription technology and
*  has since expanded to include a variety of post-production techniques, including AI custom
*  voice overdubbing, the AI eye contact model that makes it appear as if I'm looking directly into
*  the camera right now while in fact I'm reading from a document, as well as a number of editing
*  shortcuts that remove pauses, filler words, retakes, and more. Collectively, Descript calls
*  this suite of AI features underlord, a clever bit of branding that's obviously meant to imply that
*  Andrew and team want to keep humans at the helm of the content creation process. Along the way,
*  we also touch on Descript's partnership with OpenAI and Andrew's perspective on AI-generated
*  content, and I also share some details about how we're using AI workflows at the Cognitive Revolution.
*  For those, I have to give the bulk of the credit to our production team, led by Addy and Sai from
*  AI Podcasting. I've been working with these guys for the last six months, and they have both worked
*  really hard to not only produce the eight or more episodes that we publish each month, but also to
*  build AI workflows that streamline the process and create distribution leverage. The short clips
*  that I post on Twitter, for example, are the outputs of an AI workflow. AI creates six to eight
*  of them for each episode, and then I choose and post my favorite one or two. You can go ahead and
*  read my full testimonial on their website, AIPodcast.ing. To be clear, I do not have any
*  stake in the business, but I do sincerely recommend them, and they are now open to taking on additional
*  clients. So if you need podcast production help, you can feel free to ping me for more information
*  or contact them directly. In other news, I've received roughly 40 resumes from listeners who
*  are interested in new AI engineering or AI advising roles over the last month. This week,
*  I finally have the chance to catch up and review everything that I received, and I'm now starting
*  to circulate lists of relevant resumes to friendly companies. Those include Athena,
*  the executive assistant company that I've mentioned many times on the show, and also Elicit,
*  the two-time past guest that's building a market-leading AI research assistant, among others.
*  I believe I've now responded to everyone, but if you did submit something and haven't heard back
*  from me, please do ping me again to let me know. As always, if you're finding value in the show,
*  we'd appreciate it if you'd take a moment to share it with friends, and we always appreciate
*  your reviews on Apple or Spotify. Now, without further ado, here's my conversation about building
*  an AI-powered software product that changes how a great many people work with Andrew Mason, CEO
*  of Descript. Andrew Mason, CEO of Descript. Welcome to the Cognitive Revolution.
*  Yeah. Thanks for having me. My pleasure. I'm excited about this. I think you guys have a great
*  product. We at the Cognitive Revolution are regular users of it and got some interesting
*  questions, hopefully, that get at where this is all going in the big picture, as well as some of
*  the stuff around how it works today. For starters, I'd love to just hear your big picture long-term
*  vision for Descript. Obviously, you guys just recently launched the Underlord feature, which
*  I thought was inspired branding in the standpoint of not threatening the users too much, but I always
*  feel like there's a really interesting tension for tool companies where it's like you're enabling
*  service providers in many cases, but with the AI features, does this converge on becoming more of a
*  service itself? I'm very interested in your thoughts on that.
*  Yeah, totally. I think we created Descript because creating audio and video content,
*  increasingly, was feeling as fundamental as creating text content as the platforms got
*  better for distributing that stuff, but it was getting no easier to make. About, I don't know,
*  eight years or so ago when we started thinking about this as transcription quality was getting
*  better, we saw the potential to reimagine what a editor looks like for audio and video, where
*  instead of being this timeline, which not only has quite the learning curve, it's just irreducibly
*  slow to work in, you could make something that felt like the one tool that everybody understands
*  how to use a doc. By doing that, our hope was that we could put video and audio in everyone's
*  communication toolkit and complete this journey that creation has gone on from only being in the
*  hand of creative professionals to now also being something that creators use to something that
*  every knowledge worker and communicator can use. This whole thing has been enabled from AI from the
*  start, and now in our generative AI world, we see it as this incredible companion that can
*  just take even more of the tedium out of the process. In theory, making this kind of content
*  should be easy. It's the easiest thing in the world to just open your mouth and speak, but
*  looking and sounding good is the hard part, and that's where we think AI can really help.
*  So maybe run down some of the favorite features that you guys have launched. I mean,
*  I'm a big user of the pause removal and the filler word removal. Those are like two
*  first ballot hall of fame features for me. I've recently seen also the retake removal.
*  What are your favorite tools? What are the most popular tools of users?
*  Well, you name some of the really popular ones. Another one is a feature we have called Studio
*  Sound. A lot of people, especially guests on podcasts, don't have access to a great recording
*  environment. They might have a mic, but still be in an echoey room. That's one of the hardest
*  things because if you're not a trained producer, you might not even have the ear to realize.
*  You know that it doesn't sound like the stuff you hear on the radio, but you couldn't begin to say
*  why or how to fix it. Studio Sound is this AI effect that will, it's not just noise reduction,
*  it's like literally trained to take something that sounds like it was recorded on a computer mic,
*  whether there's background or whatever, and make it sound like it was recorded in a studio with a
*  professional mic. So people really love that. A couple others that have really been transformative
*  for my workflow. I make a lot of scripted, like how-to kind of videos or explainers where I'm
*  talking to the camera. The process of reading a script is really tedious. The workflows I used
*  to see creators do would be that they would have their script off camera and they would read a
*  sentence or two at a time and then memorize it and look at the camera and then pause and pause.
*  It's just an editing nightmare. Or you can get a teleprompter, but it's like a whole setup
*  that most people aren't going to bother with. A teleprompter is like, I don't know if you've
*  ever tried, it's like hard to read off. It's like a skill to read off a teleprompter.
*  So we have this feature called eye contact, which is creepy, but it's so cool. It lets you read off
*  of your screen, just like out of a Google doc or whatever. And then you turn on eye contact and
*  it looks like you're talking to the camera. So that's been like super transformative. I'll write
*  like a really rough draft of a script and I'll hit record and I'll like stop and rewrite parts of it
*  as I'm reading and feeling it out in the way that I'm speaking. And then at the end, we have
*  this remove retakes feature that is powered by Underlord where it is smart enough to be able to
*  tell, oh, it looks like they're just saying the same thing multiple times here. So I'm going to
*  edit out everything except for the last take and clean that up. So that's a favorite feature I have.
*  Another feature I really love is the ability to record over AI speech. So sometimes I will
*  write a script directly in Descript and add visuals as I'm going, kind of like storyboarding it out
*  and using an AI speech version of myself or just like a stock speaker. And in order to have like
*  a rough draft, because normally when you're making videos, like the normal process for people is you
*  kind of have to compartmentalize your writing your script and have another doc or like you've
*  set up a table or something where you're doing your storyboarding and talking about what the
*  visuals are. But the really cool thing about Descript is we kind of break all the traditional
*  barriers between pre-production, production and post-production. You can do post-production and do
*  your visual layout as you're writing and then have a scratch visual. And then at the end,
*  you can record your camera on top of that and it'll transcribe what you just said and light it up
*  and position all of the layout changes properly. We don't do a good job at like making that feature
*  super obvious in the app, which is why one of the reasons I like to mention it because it's another
*  super transformative workflow thing. Yeah, I want to understand it a little bit better actually,
*  because the way I do my intros, including the one I'll do for this episode is I take the
*  transcript of the podcast and I take 30 intros that I wrote for previous episodes,
*  put that into Clawed 3.5 sonnet now, I have it write a new intro for this episode.
*  Then it's quite good. It needs that 30 examples of my previous writing, but it really kind of,
*  I feel like it gets me and it's pretty cool. What does it get wrong if you don't give it the 30
*  examples? It doesn't, I mean, it can summarize reasonably well, but it doesn't match style. I
*  have a certain cadence where I sort of say the same things a lot of times in the same order.
*  I always say, welcome back to the cognitive revolution. I always kind of close out with
*  a couple of notes and then say, now here's my conversation with the guest. I also sort of have
*  a little bit of a, it won't be such an issue for this episode, but in some of these episodes where
*  it's like, how should we feel about this? Should we be excited about AI doctors or should we be
*  fearful of AI doctors? Should we be fearful of AI in general? I sort of have a very both sidesy
*  vibe, which is sincere, but I always kind of try to channel both my enthusiasm and my,
*  what I would describe as healthier.
*  It's kind of nuanced.
*  Quite good at school and stuff, yeah. If I have like a particular point of view on
*  a particular episode where I'm like, I want to communicate this exactly, then I have to add that
*  to my standard prompt. But if it's like, for an episode where it's a pretty down the fairway,
*  here's a founder or a researcher and we kind of go through their work, it does a really nice job
*  of just matching my general format, pulling out the key points. But then I read it and I typically
*  do a couple of takes beginning to end. So how do I do that in the Descript workflow that you just
*  described?
*  We have a write feature in Descript that will just do your standard issue generative text based on a
*  prompt. The cool thing, what we should build for you is what you've described, which is we use your
*  historical podcast episodes to be able to write an intro for you that sounds like the intros that
*  you've done. And then it can just spit that out at the top of your transcript. And then what you
*  would do in Descript is you would just select it and record over it. I don't know that it adds that
*  much value versus just leaving it in a separate doc in your use case, because where it's really
*  cool is when you've added visuals up front. If you had an intro that was a couple minute intro,
*  you knew you were switching to some different layouts where you wanted to show a visual overlay
*  or some B-roll or something like that, you could do all that when you're writing and then record
*  over it and it would preserve those visuals. But if it's just a straight one-shot intro recording,
*  then there's not much we can do to improve on that other than making the writing process
*  easier. Yeah, interesting. Maybe I should do more. Usually, I think most people listen to this in
*  pure audio. We do put it on YouTube, but I always say if you are getting it on YouTube, you should
*  put the phone in your pocket because it's not healthy to look. They spend that much time looking
*  at my face. So it'd be better to have something other than just my ugly mug sitting here staring
*  back at people. We do use the eye contact feature for that most of the time at least. And I do think
*  that is quite nice and mostly comes out in a way where I wouldn't feel like I know the difference.
*  I would say on the studio sound, this is a window into a bigger picture question maybe in terms of
*  product strategy. We've recently been really enamored with the new 11 Labs model that is
*  an audio cleanup. And I would say at least of all the things that we've tried, it's probably the
*  market leader. So we now, if necessary, we'll take the audio to that, run it through, and then
*  bring it back into Descript for the editing. I wonder how you think about being a hub or a place
*  that people can tap into all these other tools, even if you didn't necessarily create them versus
*  wanting to build and create? Because my understanding is the studio sound seems like something
*  that you had created internally. Maybe that's wrong, but is there a future where I could plug
*  into these external purpose-built models from other providers within the core editing experience?
*  Yeah, we don't have any religion about building our own stuff. Frankly, we would rather not.
*  You'll notice when we do build our own stuff, we're not releasing APIs for it in general. That just
*  hasn't been a part of the strategy. We see ourselves as building the best creation tool out there for
*  people. And our goal is to offer the best integrations that let people use whatever the
*  state of the art is that's out there. So we'll be adding more text-to-speech voices from other
*  providers very soon, more generative media libraries pretty soon, and want to do more and more.
*  And yeah, if something comes around that's better than studio sound, that sounds great for us, like
*  less time spent on building those things. We build them because they're useful to customers
*  and people don't have them. So there's stuff like on text-to-speech where text-to-speech
*  shows up in two ways in Descript. One is in this thing that we've branded as regenerator or overdub
*  where you can go in and select a word that you spoke and then change the word in the middle of
*  a sentence. And that is unique to Descript. Nobody else has built something like that. And there's
*  some really specific stuff that we do around blending the generated speech into the same
*  prosody and sound quality of the audio that's on either side. So it sounds very natural.
*  On the other hand, for general long-form text-to-speech complete sentences, there's now
*  stuff that's every bit as good as Descript. And we want to give people more options there,
*  more voices. And so we'll be integrating that. Yeah. Cool.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure,
*  or OCI. OCI is a single platform for your infrastructure, database, application development,
*  and AI needs. OCI has four to eight times the bandwidth of other clouds, offers one consistent
*  price instead of variable regional pricing. And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8, and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. This episode of the cognitive revolution is sponsored by the Brave
*  search API. You may know Brave as an alternative to Chrome. But did you know that Brave has its
*  own independent search engine powered by its own 20 billion page index of the web? The Brave search
*  API gives developers reliable and affordable access to programmable web search, auto suggest,
*  spell check, and more with flexible plans for all types of use cases from rag search to automated
*  business intelligence. On top of that, it's up to three times cheaper than Bing, all without
*  compromising on quality, speed, or reliability. Over 700 businesses, including Coheer, Chegg,
*  and Kagi rely on the Brave search API. And a recent survey showed that 94% of customers
*  would recommend it to their peers. To start building apps with the power of the web,
*  sign up at brave.com slash API and get up to 5,000 free monthly calls.
*  The API point that you mentioned was actually one. So I work with a couple of guys who are
*  basically a small podcast production agency. They call themselves AI podcasting. I was drawn to them
*  because they're very committed to using the latest and greatest AI tools. And in addition to
*  doing a good job for me, they also bring me lots of ideas and we trade ideas and so on.
*  So one of the things they wanted me to ask you is about API access. They would love, and this may be
*  very rare, but they would love to be able to build their own sort of external workflows and then hit
*  the ignore endpoint because most of what we're doing is cutting and ignore all these things based
*  on the heuristics that we've developed. But then we still love and I kind of feel like we sort of
*  have to have the ability to go in and see in a visual way what was cut. And that's why I think
*  the ignore thing is like a really good format because it's so easy to see and it's so easy to
*  restore. It sounds like you're going to break their hearts though. No API.
*  Not necessarily. It's not that we're, yeah, maybe that's true. Is that not coming soon?
*  We're not against it. It's just a priorities question. That sounds like a cool workflow.
*  So it sounds like what they want to do is they've built their own kind of version of some of the
*  script editing AI actions. I'd be curious to learn more about what it is. But another way to do that
*  would be to have kind of extensions or presets inside of Descript that let you use different
*  models or type in different prompts or whatever and then save those so that you don't need the
*  API access. Is that something that would be cool? Yeah, I think it would probably work similarly.
*  It probably doesn't matter in the end too much if it's posting in the edit changes or calling out
*  to get them and implementing once they're returned is probably just two reps to the same place.
*  I think we've experimented with a lot of things. They do fine tune models for specific clients
*  to really edit in the way that that client wants to have things edited. They also do this for clips
*  and this is where the editing gets even more intensive, right? Because we'll try to figure
*  out what is the right viral clip for us to zero in on and then how do we kind of get that under
*  60 seconds ideally, right, to fit under certain thresholds for different platforms. And now you're
*  talking like economizing on the level of one second here, one second there. And so we've created
*  examples of that, a few shot, many shot even, and even fine tuning to try to zero in on what are
*  the clips that we feel are working for us or that sort of satisfy my idiosyncrasies in some cases,
*  right? Because each client wants to kind of present themselves in a different way.
*  So we have some, for example, where it's like my theory is, and I don't necessarily have data for
*  this, but I feel like when we post a clip, people who follow me know my face. They don't necessarily
*  know the guest face, but of course the guest is like the real star. So we try to do a real quick,
*  and as you can tell, I talk too much on my own podcast. So my questions are usually too long.
*  So we try to shrink my question down into like their first couple of seconds
*  and then get the guest on to let them shine. So these are the heuristics that we're kind of
*  trying to encode. And it's like a little bit more than we can prompt within the, and I got to start
*  saying it the way you're saying it, which is de-script. Am I saying it that way? I try to mix
*  it up. So say it however you want to say it. I've put the emphasis on the script, but we've kind of
*  gotten into this, right? So there's a little bit more that we're trying to do than we can just
*  prompt into that system. But we do ultimately want to bring it back there because we want to see it.
*  We want the visuals, and it's that last, often there's like a tweak, right? So we could pipeline
*  this out. And we've tried doing that where we actually, okay, we get all these suggested edits,
*  and now we could programmatically make them with FFMPEG type tooling. But that sucks at the end,
*  because if you don't love it, you have a really hard time going back, right? So the dream would
*  be the de-script output based on those workflows. So we can still do that last tweak. I would love
*  to actually talk to those guys and brainstorm a little bit what we can do. Also, this is the
*  weirdest podcast. I just feel like we're doing a customer call, but I love it. It's great if this
*  works for you. Yeah, I get into the weeds of how things work. And most people that listen are,
*  you know, another standard joke is it's not entertainment. So, you know, it's for people
*  that are like building a lot of times and then also in research, but really trying to...
*  No, I'll talk about this all day. The better than like telling you the three things I learned from
*  Groupon. That was going to be one of my... I have that down at the bottom of the outline. So,
*  okay, I should cut that. But hopefully I'll make it more relevant than most.
*  Okay. So this is cool. I wanted to get into also a little bit of OpenAI partnership. That's
*  obviously something you guys have taken investment from them, a pretty significant amount, right? As
*  I recall. And obviously they're like selling frontier intelligence. And if you have a couple
*  million bucks to put down custom models, I was interested in sort of, are you working with them
*  on custom models, trying to really push the possibilities of what language models can do
*  in the editing workflows? Yeah. I think like they saw how generative AI was exciting across audio,
*  visual and text mediums. And Descript is interesting because it sits at the intersection
*  of those things. So Sam was just a big believer that this was going to be a space where you could
*  have a lot of fun and do some really interesting stuff using the sorts of things that they were
*  building. And also that even as this stuff got better and better, having a tool with human shaped
*  controls where the human can get in there and practice their craft alongside the alien wasn't
*  going away anytime soon. What the relationship has looked like has been more or less like a standard
*  early investor. But then we get to have conversations with these people who are
*  working on the cutting edge of what's going on, help us understand where things are going,
*  get early access to some stuff, but that's it. It's pretty standard, pretty basic stuff.
*  So that sounds like a no on a custom model. If so, that's, or is it a no comment?
*  I can't even comment on that because I'm not even sure what the research teams right now are
*  working on with them. So it's a no comment from a place of ignorance.
*  My gut says that could be really compelling. They have an interesting talk out with,
*  it's actually a member of the OpenAI team talking about their partnership with Harvey. And they
*  claim to have, through continued pre-training on legal data, have gotten to the point where
*  they had a 97% preference ratio of their legal specific model versus the original GPT-4 base
*  that they were working from. And it does feel like something similar is probably on the cusp of
*  possible for editing, where I would imagine what we see certainly in our own without nearly as much
*  data as you would have potentially access to and not nearly as many hours to put into it.
*  We see there is a lot of value in even just fine tuning. And so I could imagine if you have
*  a billion hours of intensively edited content that you could work from, that seems like it could
*  create just a qualitatively different experience. For sure. We've seen that as well, and we're
*  moving to largely fine tuned models for most of our actions at this point.
*  This is one of my new favorite questions for entrepreneurs. I think you'll have an
*  interesting take on it. What would a 10 times more expensive version of the product look like
*  if we said we're going to push performance to the limit no matter how much the inference,
*  how many tokens that may take? What do you think are the frontiers?
*  Well, the obvious answer to that right now for us is in generative video, which is still quite
*  expensive and cost prohibitive for a lot of the use cases that would be interesting, which are like,
*  I mean, the way we think of video is that most videos are mostly window dressing with brief
*  glimpses of actual content appearing on frames, like information appearing on frames. If you
*  think about it, this video is a great example. The visuals are just us, our heads are just like
*  about engagement, but it's not adding very much at all to the substance. Maybe at some point,
*  we could throw up a chart or something like that, and that might be some actual information.
*  I think generative video has a lot of potential for solving that window dressing problem that
*  creating videos have. If you think about turning a doc into a video, there's the speech part,
*  which you can use AI speech, which has gotten quite good and is pretty affordable.
*  You can also record it, which isn't that hard, but creating the visuals is the hard part.
*  We've started to see some experiments in generative window dressing, the most prominent of which is
*  synthetic avatars, but I think that's just the most obvious possibility of what someone could do,
*  and there's a lot you could do with animation and other forms of generative video that I think
*  are pretty interesting. SORA, in a word, would be where some of those... SORA, like Runway,
*  why haven't we integrated Runway? I think it's just because it's like 10 bucks, something like
*  that per minute of video, just really limits what you can do with it for our customers,
*  especially for stuff like this where you think about the way you use a tool like Mid-Journey
*  or something. There's a lot of back and forth experimentation. Those tools work because they're
*  not zero shot. Yeah, it's certainly a skill unto itself. One thing I thought you might say,
*  too, is, or maybe this is already happening under the hood. It's not totally obvious to me. I assume
*  the original version was, as you said, toward the top, transcribed first, now processed transcripts,
*  multimodality is obviously coming online in a very powerful way. I assume you've had some
*  early access to the voice mode and one imagines that the ability to put in raw audio along with
*  perhaps a transcript or perhaps even raw video could be quite a game changer in terms of the
*  quality of manipulation that you could get back from the AIs. What do you think the next...
*  That's allegedly coming soon to all of us. What do you think that is going to mean for
*  descriptive content creation broadly? Specifically, multimodality and AI that can see and hear.
*  Yes, we're excited about all that stuff. I don't think that gets us to the 10x more expensive
*  threshold. At least we haven't envisioned a way to make it that expensive for ourselves or our
*  customers yet. But in short, I think what it does is it lets our editing assistant get smarter.
*  Right now, all Underlord can do is read your script and make a bunch of guesses on what's
*  happening on the screen or what's happening in the audio in order to make suggestions.
*  I think when it's actually looking at the frames and listening to intonation and things like that,
*  then the possibilities just get richer in terms of the different styles that it can take on and
*  it gets more accurate. Yeah, it seems like that's going to be a big, big deal. I'm looking forward
*  to the voice mode just so I can go read research papers while walking around my neighborhood
*  instead of having to actually be planted in front of my computer. So it seems like that's
*  going to be a huge unlock. You mentioned fine tuning. You're trending toward fine tuning for
*  more and more tasks on this 10x more expensive theme. What about fine tuning to the user? Is
*  that something that you see in the scope of possibility? Yeah, it's something that's
*  definitely on our radar. I can't say too much about it yet. But you just earlier started this
*  podcast with a great example of how powerful something like that could potentially be.
*  So it's certainly something that we're thinking about. Yeah, my clod prompt is 10 cents basically
*  with the full transcript and the 30 examples. And so that's in the zone where, especially if
*  you do have a couple iterations or a couple back and forth, you could get up to 30, 50 cents.
*  That starts to feel like the kind of thing where you have to take it into account to some extent,
*  especially if I'm making a number of, which I make, we're doing eight a month. So it starts to be
*  into the dollars for you if you built in something along those lines. But at the same time, there's
*  still plenty of room. If you imagine, we put that under the 10x more expensive heading,
*  it still gives you like a ton of room to run. Yeah. Yeah. No, that's not too bad. Hey,
*  we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy, is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent,
*  so you don't have to. With teams across Asia and South America, we can cover you no matter
*  which time zone you operate in. Their engineers follow your process and use your tools. They work
*  with React, Next.js, or your favorite front-end frameworks. And on the back end, they're experts
*  at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the waitlist.
*  What about bringing, this is like maybe crazy, but I've been starting to think about having GPT-4-0
*  voice mode co-host with me in some way, shape, or form. Maybe it coaches me in the background,
*  maybe it actually pops in, maybe it has my outline and sort of says, you know, this would be the time
*  to ask that question so you don't have the awkward pause like I just had. I don't really love
*  fully AI-generated content in most cases, but I wonder if you have a vision for a more hybrid
*  approach where you have this real-time co-host potentially.
*  LWK Yeah, I mean, we think that's another really interesting idea. It's something that we've talked
*  about a little bit internally, but can't say too much more about it at the moment other than say
*  that sounds cool.
*  JG Okay. Maybe just zoom out for a second. What is the breakdown of who creates content with
*  Descript? Is it mostly podcasters or how often do you see people doing different,
*  what's the sort of customer profile breakdown?
*  LWK It's a mix between podcasters and creators,
*  video content creators, a lot of people that are making educational content, explainers and how-to's,
*  tutorials. Descript has a built-in screen recorder that you can either use loom style to just fire
*  off a quick video message, but it's also really great for recording overlays on top of a narrated
*  screencast kind of thing that you're making. In businesses, we see marketing teams use it.
*  We see it being used for internal training materials. So that's a pretty good overview
*  of the types of people that are using it, and they're using it to create, in addition to just
*  straight up podcasts and video content, they're using it to repurpose that stuff into clips and
*  promo content. JG So what else do you think those folks need? One idea that occurred to me,
*  and this is kind of my own AI video background speaking, but it seems like monetization for
*  these folks is typically quite a challenge. I've been fortunate to be part of this turpentine
*  network and they handle almost all of the sponsorship sales, so that takes a real load
*  off of me. But in general, I feel like people both have a hard time selling and then also
*  creating the high quality sponsorship content that they would want to integrate seems like a real
*  challenge. Thoughts on that and thoughts on other things that you think people are really missing
*  as we imagine a world of lots more creators thriving independently?
*  Yeah, so we hear that all the time, like monetization, finding an audience is one
*  of the top pain points that you'll ever hear from creators. At least for now, it's kind of outside
*  of our sweet spot and we've got our hands full, just trying to make it easier for them to make
*  their content. We also hear like once creators get past their initial list, just continuing to
*  keep things fresh and come up with ideas for content can be a struggle. So those are the
*  buckets, the ideation, obviously like making it easier to make more content faster and then
*  audience and monetization. We mentioned synthetic voices. Do you see people using things like
*  HeyGen or Synthesia, these sort of AI avatars? I wonder if you have a take on the future of
*  that form factor. Yeah, we talk about it a lot. What's your take?
*  Very hard to say. I would say right now it is actually just did an episode with HeyGen and
*  created my intro for that episode with my HeyGen avatar. And then we also had a weird recording
*  issue where like his video was kind of corrupted. And so we actually decided, well, let's go for it
*  and recreated this whole thing with his HeyGen avatar. So we're like, you know, just spent a lot
*  of time with the avatars. I would say it's like late uncanny valley and still it's again quite
*  good. Certainly for a couple minutes at the top, it seems serviceable. In general, I'm not excited
*  to listen to long form stuff with it yet, but it seems like it is, you know, potentially not much
*  longer before it could exit the uncanny valley. And then it becomes like very hard to say where
*  it goes as far as I can tell. And once it exits the uncanny valley, like do you think that's the
*  thing that's standing in the way? Do you see yourself watching a long form video of your
*  favorite podcaster as an avatar? I think it depends on just how good the ideas are. You know, I'm open
*  to weirdness for sure. Yeah. What has let me down the most, I think in AI generated podcasts to date
*  has been less the quality of the voice that synthesize or the avatar and more just that like,
*  I have not usually felt like there's really any alpha to it. In the episode we just did with Josh
*  from Joshua, I should say from Hey Jen, he actually said all those things and then we kind of
*  recreated it. So we felt like it was, you know, it wasn't like we were just taking LLM slop and
*  putting it into his voice. It was actually his words kind of recreated. So it was a little bit
*  different, but yeah, I think at the heart of why I haven't been enthused so far has been just the
*  quality of ideas even more so than the form factor in which it's delivered. Yeah, you know,
*  we have a kind of like brand value here about staying clear eyed, being really careful not
*  to believe our own bullshit on anything. It's so easy when you're building a tech company
*  to get swept up in it all. And we just like, don't want to do that life is too short. And I think
*  like AI avatars is interesting. It's so hard to predict the future. And I think AI avatars are
*  emblematic of that. There's some companies that have gotten quite large building AI avatars,
*  and like these hyper realistic avatars, and I totally missed it. When I saw that I was like,
*  this is dystopian. Even if you get to the point like out of the uncanny valley, it's irredeusably
*  cheap. Like it's all the value is for making it scalable for the creator. There's no value is
*  executed for the audience. But I expect like you're saying that this is just the first phase of
*  something that gets really interesting. And probably where it gets really interesting is not
*  just in like, trying to recreate the previous version of what we had, but using this technology
*  to create something new that we haven't seen before. And that's maybe where this stuff really
*  becomes something else and something special that's not quite as creepy. Yeah, they have
*  interesting ideas around. I think for me right now, the number one killer use of that kind of
*  thing would be translation. Just to think like, if I could translate this whole thing into Spanish,
*  that could open up a whole new opportunity. And even if it is slightly weird, it still feels
*  genuine. They've got certainly much farther out ideas around personalization and choose your own
*  adventure and all kinds of dynamic possibilities that start to get into that realm of like,
*  it becomes a meaningfully different thing. And maybe that just ultimately feels different.
*  But yeah, I think today, we're still kind of poking around to figure out exactly
*  what that might look like. Yeah. All right. Here's the Groupon question.
*  Okay. You know, small businesses really well. Yeah. What do you think they are sleeping on
*  in terms of how they should be using AI that they're not? I mean, I'm trying to think about
*  that from a Groupon lens. Like I have no idea how like restaurants or, you know, nail salons
*  are using AI. The most obvious thing is it feels like we're in this window of time where AI can
*  really like bring the cost of creating like 80th percentile quality online presence from
*  videos to your website and stuff like that, really high quality. And so I don't know. I assume that
*  a lot of small businesses are sleeping on that, but I'm not really like, I'm too busy building this,
*  you know, little video app to haven't been staying in touch with the massage places and stuff that
*  we used to feature on Groupon. I think it's still pretty safe to say that they are mostly sleeping
*  on it entirely. Yeah. Handling routine stuff is kind of where my head goes. Just like soon,
*  if not already, there are going to be good appointment taking phone agents. And that in
*  and of itself, I think could be a huge unlock for many businesses. Yeah. I'll say that the kinds of
*  businesses that we deal with at Descript, which are a little bit different than like you don't
*  have restaurants buying like there were these brick and mortar places buying a lot of like SAS
*  tools necessarily. They do, but it's just like, it doesn't come to the scale that we're talking to
*  them as much as more of a self-service thing. What we see from the slightly larger SMBs and enterprises
*  is that they do have a mandate to go out and integrate AI tools and find AI tools. And they
*  have trouble a lot of times finding something that's actually adding meaningful value for the
*  org. So there's like a lot of stuff that's come out that has this like magical AI promise, but it
*  might be good at like a very one specific type of thing. But when you actually try to integrate it
*  into the org and get people to use it, it kind of breaks down. So that's not like to say that AI is
*  some kind of a fad for this thing from that. I think it's more just like we're still in the process
*  of building all the tools that are going to work really well for businesses.
*  Perfect transition to what have you learned about hiring AI engineers and how the discipline or
*  skill set of applying AI to product experiences differs a little bit from a more traditional
*  software engineering challenge. Yeah. So it's a little bit different if you're having people
*  that are working with LLMs and like kind of wrangling LLMs compared to the people that are
*  building models like we did with Studio Sound or Overdub, especially when we were building those
*  models. One of the interesting things was that like normally when you're building product,
*  you can just like define your requirements, design something, work with engineering and have a pretty
*  good sense of like you can build a product around known engineering constraints. And
*  the constraints on these AI tools end up shifting kind of as the research unfolds.
*  So the user experience that you're building for AI speech model that can be trained instantly
*  is very different from the one that can be trained in 15 minutes is very different from the one
*  that can be trained in a day. And we've gone through all of those different cycles and
*  we've been working on stuff where relatively late in the development process, something happens where
*  you have a new model that's much higher quality, but instead of taking 15 minutes, it takes three
*  hours. And then you have to make those kinds of trade-offs that maybe completely shift the nature
*  of the product. So that's like the big new thing is that level of uncertainty and figuring out how
*  to work that into the development process. The other thing is just how when you're building
*  when you're doing AI research, you're making a bunch of bets. Some of them are going to pan out,
*  some of them aren't. The ones that don't, you might hit like an absolute dead end and just need to
*  start from scratch on a different idea. And you just have to factor that into the way that you
*  build and run the team is that that's like par for the course. Yeah, that's very apt, I think. I
*  always say with AI engineering, we don't know what's going to work in advance. Derisking is
*  critical. Do the hard part first. And I think you basically said something very similar there. So
*  that's good reassurance for me and for anybody who's listened to me say those things in the past.
*  I know we're just about out of time. Anything else you wanted to touch on before we break?
*  No, thanks for having me. This was fun. Cool. I appreciate it. It's been short but sweet. Andrew
*  Mason, CEO of Descript. Thank you for being part of the cognitive revolution. You bet. Thanks for
*  having me. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co
*  or you can DM me on the social media platform of your choice.
