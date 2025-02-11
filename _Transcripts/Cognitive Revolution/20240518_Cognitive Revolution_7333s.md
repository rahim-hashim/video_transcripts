---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 7333s
Video Keywords: []
Video Views: 5969
Video Rating: None
Video Description: Dive into a critical analysis of AI's rapidly evolving realm with Zvi Mowshowitz. Discover our take on Google's I-O event highlights, OpenAI's spring event, the big tech and startup AI dynamics, and the significant shifts in OpenAI's safety team. Gain insights into the competitive landscape, technological advancements, and strategic challenges that shape today's AI industry, as we explore the future's uncertainties and the potential for change.

Part 2 is here : https://www.youtube.com/watch?v=lvjs-1SpX6U

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

CHAPTERS:
(00:00:00) Introduction
(00:03:01) Welcome to the Cognitive Revolution
(00:06:35) The Reality of AI Demos: Hype vs. Practicality
(00:09:30) Integrations and Universal Assistants: The Future of AI
(00:15:39) Sponsors: Oracle | Brave
(00:17:47) The Ethical and Social Implications of AI
(00:31:53) AI's Role in Addressing Loneliness and Social Engagement
(00:33:24) Sponsors: Squad | Omneky
(00:35:12) The Future of AI: Subscription Models and Ethical Considerations
(00:44:13) Exploring AI's Ethical Balancing Act
(00:46:14) The Ethics of Personal AI Relationships
(00:52:13) The Future of AI: Customization and Personalization
(00:56:02) The Role of Multiple AI Friends in a Diverse Ecosystem
(01:00:23) The Impact of AI on Market Dynamics and Competition
(01:11:22) Big Tech's Dominance and Startup Ecosystem Challenges
(01:22:54) Navigating the Tech Landscape: Opportunities and Challenges
(01:25:47) The Importance of Future-Proofing in AI Development
(01:28:26) Legal and Compliance Challenges in AI Implementation
(01:30:43) Venture Capital and AI: Navigating the Investment Landscape
(01:40:56) The Future of Employment in the Age of AI
(01:50:15) The Departures from OpenAI's Safety Team: Implications and Insights
---

# OpenAI and Google Race to Her - Is the Big Tech Singularity Near? Part 1 with Zvi Mowshowitz
**Cognitive Revolution:** [May 18, 2024](https://www.youtube.com/watch?v=8fYtGCP6gos)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today, after traveling to California for Google's
*  I.O. event and taking some time to process what has been, in all honesty, quite a confusing week,
*  I'm back home and excited to share a timely conversation with Svi Moshewicz.
*  While many excellent news roundups have been published over the last few days,
*  including by Svi on his blog, here we aim to provide a higher level of analysis.
*  We start by discussing the new capabilities that excite us most from a mundane utility perspective,
*  including the native multimodality, lower latency, lower prices, and deeper integrations into
*  platforms that were all previewed this week. And then we reflect on the fact that while the
*  technical advances are indeed very impressive, most of the products aren't actually available
*  for us to use and even many of the demos seem quite rushed, and we consider what that might imply.
*  From there, we attempt to get a handle on the competitive and strategic dynamics at play,
*  as the big tech incumbents compete not only with one another, but also with younger,
*  scrappier, and less constrained startups. We assess whether the apparent convergence
*  of the frontier developers' retail and API products may create a winner-take-all arms race
*  dynamic, and we analyze whether more friend-like AI products could mitigate that concern.
*  We also debate whether the returns to scale and foundation model development
*  mean that the so-called big tech singularity may be near.
*  Where I tend to emphasize the big tech companies' structural advantages and find myself,
*  frankly, bearish on the majority of startups right now, is Svi tends to place more emphasis
*  on the cultural, bureaucratic, and regulatory barriers to big tech growth and is more bullish
*  on the challengers. I think the contrast between our perspectives here is quite interesting,
*  and I hope you find it useful. Finally, we address arguably the biggest news of the week,
*  the string of departures from OpenAI's safety team, including what it almost certainly does
*  not imply, what it in fact might, and what the departed safety researchers and safety community
*  should do now. We recorded this on a Friday morning, and it was actually during our recording
*  that Jan Lejka posted a thread explaining his reasons for leaving OpenAI, and while we didn't
*  have a chance to discuss his post specifically, I do think our overall analysis holds up in light
*  of his statement. At a high level, the only thing that's crystal clear at this point is that the
*  situation is increasingly complicated and moving so quickly that we should all be really honest
*  about our fundamental uncertainty and remain open to changing our minds on key questions.
*  I, for one, certainly am. As always, if you're finding value in the show, we'd appreciate it if
*  you'd take a moment to share it with friends, and if you think we missed anything important or got
*  anything wrong, we invite you to share your feedback via our website, cognitiverevolution.ai,
*  or by DMing me on your favorite social network. Now, I hope you enjoy this timely analysis of
*  another intense week in AI with Zvi Maschowitz. Zvi Maschowitz, welcome back to The Cognitive
*  Revolution. It's always a busy week when you're here, and I don't think that's a coincidence.
*  We've got a lot to cover. I'm very confident it's not a coincidence. I thought we would maybe
*  organize this sort of as you do your blog posts, start with kind of the mundane utility
*  and what we're excited about, and then get into maybe what we're not so excited about,
*  and then maybe get into what we're worried about. I think we've got some
*  good topics for each of those sections this week. How's that sound?
*  Oh, yeah. Yeah, that's definitely the right things to do, and there's definitely coverage all around.
*  Cool. Oh, or not cool, depending on the section we're talking about.
*  It's not so cool. Let's start off with then obviously a busy week with OpenAI making some
*  launches, Google making some launches slash announcements. I guess both of them really making
*  launches slash announcements, which is one of the bits of analysis that I want to get into. But I
*  guess for starters, what stood out to you as the new capabilities that are most exciting to you
*  as somebody in search of an incrementally better life? Yeah, so there's always the difference
*  between what they're promising you're going to be able to do in the future
*  and what you can actually touch now. We can use now. So we can use now is GPT-4.0.
*  That is fast. That is half the price if you're using the API. And that is multimodal in various
*  ways. It seems like a great product. It has its weaknesses that are becoming apparent as
*  I use it. But it's already pretty exciting. And then when it becomes fully multimodal,
*  it starts to play into the modalities that they're talking about where you talk to the AI and talk
*  back and it hears your tone of voice and it hears the cadence of your expressions and it sees your
*  face and all that stuff. That looks pretty exciting in the relatively near term. They said a few weeks
*  for that. But I do think this is bearing the lead compared to all of the integrations that both
*  companies are promising. That to me is the big exciting thing if they can be delivered. What about
*  these universal assistants? Because the demos they actually gave us were lame as hell on these
*  capabilities. Can you recognize what I'm seeing in this picture? Can, okay. Yeah, I already know
*  you know how to do that. Why is this exciting? You remember what was happening a minute ago. Yeah,
*  you can. Okay, yeah, again. I knew that. And was that over and over again, these demos of
*  educational videos with trivial exercises where the kid is being intentionally dense and already
*  knows the answers and then is doing a good job of play acting being actually lost and then the AI
*  doesn't pick up on it and just tends to bubble through. You have a bunch of translations of very
*  trivial statements that, you know, I'm not saying I could translate them without knowing the languages,
*  but it's close. So on. And those are some open AI demos, but Google's demos were similar, basically,
*  in these areas. But then we're talking about the things where it's okay, search my inbox for all of
*  my receipts, put them into a spreadsheet, organize all of my expenses and all of the things that have
*  been done by category. So do all this automatically forever, like I told you to on a background
*  continuous basis. Now I'm more interested, right? The context of integrating all of this information,
*  right? Open AI thinking it's going to live on your phone, Google thinking it's going to live on your
*  phone. And it's shaping up potentially to be another Android versus iPhone battle, right?
*  Because if Google is going to own Android, right, it falls and it's looking at the big deal of Apple.
*  Yeah, it does. I feel like there's a really interesting point there on the demos and just how
*  sort of slapdash some of them were. The open AI ones, I think they're trying to make a point
*  on some level of this is you can tell it's very real and like definitely not prerecorded and
*  staged. Although you could always still fake it, but I believe that their demos were real in real
*  time. And there were a couple of things there that the AI came back with where it was like,
*  yeah, I didn't think that was maybe exactly what they were hoping it was going to say,
*  but they're at least showing off that this is real now and we have the confidence to do it live on
*  stage for you. But across both companies, it did feel like the demos were a little bit of an
*  afterthought. And I wonder what you make of that. Is that like a, I mean, it'd be like,
*  it's a reflection of the sort of ideological motivation behind the development in a sense,
*  where they're like pushing the capabilities and then figuring, we'll figure out what to do with
*  it after, which has obviously been something Sam Mullen has said explicitly in various ways over
*  time. But it's still a little striking to me that they were so, okay, we just made this thing now.
*  Can anybody come up with something to do with it on stage? We got to be on stage in 10 minutes.
*  It felt, oh yeah, well, Mira speaks Italian. Let's translate. That is cool, but it did feel
*  rushed. And I guess the other answer would just be like, they're rushing, they're racing. And so
*  they're taking these things out of the oven and putting them right on stage without much time to
*  really figure out what to do. It suggests that these capabilities are new. They haven't had them
*  for very long. It also suggests to their credit that they're not optimizing the demo. They're not
*  putting lots and lots of effort into putting forward the best demo possible. If these were
*  startups, these were scrappy little companies trying to use this to raise money, you would have
*  seen dramatically different demos that would have looked dramatically more impressive from both
*  companies, but they deliberately chose not to put in that effort. So you don't have the same effect
*  of, I am very confident this is the best possible thing you could have shown me. I am very confident
*  that if Google or Urban AI had tasked a bunch of people with, okay, take the day, take the week,
*  figure out something much more impressive, try it 20 times, confirm that it always works,
*  get it ready. I think they would have gotten something that would have wowed us a lot more.
*  I have to assume these were hastily assembled, not well thought out, like not robustly tested,
*  demoed. These were closer to real than you would normally see, but it still speaks to, they didn't
*  try to make this interesting in some important senses. But also that could be a lot of like,
*  who are you talking to? Like you're talking to the person who doesn't even know what
*  GPD4 is. They're used to three and a half as like what it is, and they barely even
*  spend five minutes on it, and they have no idea what's going on. And then the horse can talk at
*  all. And that's actually really impressive because until a year or two ago, the horses didn't talk.
*  Yeah, I have a few candidates for the things that excite me most. You hit on one already, which is
*  the integration into the whole platform. For Google, that's obviously always been where they're
*  going. And with OpenAI, it's kind of more suddenly, it seems where they're going, although I'm sure
*  they've been planning for that for some time as well. But all of a sudden you get the desktop app,
*  now you can connect your Google Drive, or at least again, that's coming soon or in some phase of
*  rollout. That does seem super exciting as our friend or let's say inspirational figure, Tyler
*  Cowen says context is that which is scarce. And that has definitely been a feeling I've had with
*  language models all the time. It's both traditionally that earlier language models that
*  might've meant you just only have so many tokens in the context window. Obviously that problem has
*  been largely solved with Google going from now one to two million tokens that they're bringing online.
*  That's a lot of tokens and fit a lot in that. But now you still have to figure out, well,
*  how am I going to get those tokens? What tokens am I going to get? If you're copying and pasting
*  a million tokens around to do a single use case, now you've got a lot of friction there as well.
*  So plugging into these different sources, whether it's your Google Drive or your Gmail or whatever,
*  that seems like it is going to be a tremendous driver of value.
*  Yeah. They've always talked about these giant context windows and they're very, very useful
*  when you know you need them. And you're sitting down to analyze a big bunch of data or search
*  for a big bunch of data, but it is much slower. It is substantially more expensive for token to do it.
*  And what we're seeing is Gemini Flash. We're seeing things that are optimized for speed,
*  things that are optimized for cheap and things that are optimized to
*  run locally and just do all of these things in a way that the customer wants. And Google is also
*  giving us two million context window, which is very useful. But how do you combine these things?
*  And a lot of the key is going to be like, how do you go through all that context, figure out what
*  the right context is? I always thought that Tyler Cowen saying context is that which is scarce,
*  is sort of saying two things at once. It's saying the whole, like, you don't have enough context,
*  right? But you're always short on context, but also sort of a definitional thing, sort of whatever
*  it is that is scarce is the context. And so in some sense, once these details of your situation
*  become background common knowledge, that's not context anymore. In that sense, that's just
*  your life. Like, I don't think about that as context when making my decision. So I don't think,
*  well, in context, we like French toast, like, no, we just like French toast.
*  It's just a fact about me that currently, these companies don't know. But presumably,
*  these companies would know when I'm just storing absolutely everything and they're taking an input.
*  So other things that I think are candidates for the most impactful aspects of these launches,
*  one is the kind of freeness of it all. Opening, I'm moving to make the latest model free for everybody
*  is a big deal. And Google seems to be doing something similar. It's not entirely clear
*  exactly what they're going to be rolling out at what price point in what product. They have the
*  Google Advanced, which is not free, which has been required to get you the most advanced models to
*  date. But it's unclear if that will be required as a subscription to get the Gmail Assistant that's
*  coming or whatever. So we've got some clarification questions, I think, still for them. But this does
*  seem like a moment where, obviously, OpenAI has almost the sort of Kleenex brand in AI thus far.
*  And most people who have tried something and weren't super impressed with it tried chat GPT
*  with a 3.5 default. Now they are going to get a major step up. How do you think that will change
*  the landscape, the world of work in the immediate term, just on the basis of like,
*  now everybody can use the best model? Yeah, trivial inconveniences like you have to pay a
*  bit of money, definitely hold back a lot of people. And it's clear that from all sides,
*  they're realizing that owning the customer is so much more important than the trivial cost to
*  compute for the lightweight customers using a bit of it. Chat GPT is pure profit for a user like me.
*  I'm not actually requiring that many tokens per month. I'm paying $20 a month to have it.
*  Goodness, that's part of my job. And I want to make sure that I have a variety of different
*  things to try and get each other. But in practice, of course, they hit a dollar in
*  inference in a month, right? 5% cost to provide the goods. On the margin, that's shockingly high.
*  So it's not very expensive to give these people the free version, except in some
*  of our people cancel those subscriptions because they no longer need anything but the free version.
*  I do think it's going to be an issue for something that they count on that revenue,
*  but I don't think they count on that revenue particularly. And of course, they get the data
*  every time someone puts something into there. And that's incredibly valuable. So that's another way
*  you own the customer. So yeah, the future, I think Google clearly is indicating that in the same way
*  that you've used Bing the entire time, you get access to GPT-4, but nobody bothered because it
*  was a weird different interface and people didn't notice. Google, I think, has realized that for
*  most purposes Pro 1.5 is in fact the appropriate model for most use cases that people want to do.
*  They don't need what Gemini Advanced is offering, but they will offer the upgrade to Gemini Advanced
*  if you want to pay it. And most people won't pay for it and most people won't need it.
*  But the Pro 1.5 is for most purposes, plenty good enough. When you're trying to compare Pro 1.5 to
*  Gemini Advanced, it's not entirely obvious that it advances all that in some sense,
*  much better than it in practical purposes for many of the things you want to do. Pro 1.5 is very good
*  at searching documents, for example, which is the main thing that I still want Gemini for,
*  exclusive to other things, but I'm not integrating with other Google services.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  A.I. might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that
*  A.I. needs a lot of speed and processing power, so how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and A.I. needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead
*  of variable regional pricing, and of course, nobody does data better than Oracle. So now you
*  can train your A.I. models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive
*  of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive. Oracle.com slash
*  cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave
*  Search index stand out? One, it's entirely independent and built from scratch. That means
*  no big tech biases or extortionate prices. Two, it's built on real page visits from actual humans,
*  collected anonymously, of course, which filters out tons of junk data. And three, the index is
*  refreshed with tens of millions of pages daily, so it always has accurate up-to-date information.
*  The Brave Search API can be used to assemble a data set to train your A.I. models and help with
*  retrieval augmentation at the time of inference, all while remaining affordable with developer
*  first pricing. Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API. I feel like the voice and the real-time vision also
*  definitely, this is where the demos were kind of flat. I thought this was true, really, in both
*  cases. I mean, the OpenI ones were maybe a little bit better. At Google, I went out to the Google
*  I.O. event and they had a, you know, it's quite a production, right? They have the amphitheater,
*  which they don't actually own, I learned, but it felt like they owned it for the couple days
*  that we were there because they had set up basically a whole little city on this plot of
*  land with massive, like almost permanent, but still temporary structures for all their different
*  sections, web and Android and AI. There's a whole AI building and you go in there and they've got
*  all these different AI demos. And the one was Project Astra and you go into a little booth
*  and they have a camera mounted and it's looking down at a table and then it's like, okay, here's
*  a another sort of bin, another table full of junk. Now you can like pick a couple pieces of junk,
*  put them under the camera and talk to the AI about it. So you've got like a toy dinosaur
*  and you're like, what's this? And it says, it looks like a toy dinosaur. And you're like, okay.
*  And it was, again, it's kind of going back to this, like, I'm not sure that they really
*  took this anywhere near how useful it could be. And it does feel like the sort of thing where
*  it's like, yeah, we made this. Now we've got to show it off somehow. And we're leaving the rest of
*  the work to the community to do, which I have mixed feelings on that. I don't mind it in some
*  sense. It's an enabling technology. And so fine. I do feel like those things should have been a
*  little bit better thought through or certainly could have been a little bit better thought
*  through. It does feel a little ideological in some ways. And I guess I just also want them to have a
*  bigger, better idea for like, where are they trying to take us? We're all kind of, everybody is,
*  at least everybody in technology, right? Is like, looking forward to these announcements,
*  trying to figure out what are they going to do and how's it going to impact me and what can I build
*  on it? Or is it a threat to me? And then they just give you this stuff and it's like, the homework
*  isn't really done. I've been saying recently that the scarcest resource is a positive vision for the
*  future. And I just, I feel like I want more of the tangible vision for where they are taking us
*  than just sort of, here's a table full of junk. Like you can put it under the camera and like the
*  thing will recognize it and you can talk about it. Even though it was impressive, they had another
*  like, Pictionary mode too, which was an impressive demonstration. You saw some of these things in the
*  Google, in the Gemini 1.5 Pro original announcement where they showed like a hand drawing of a thing
*  and said, where did this happen in the movie? And it was able to cross-reference this to a scene.
*  That similar experience was on display. People were like drawing little line drawings and saying,
*  what movie does this represent? Somebody drew in the little demo group that I was in a Wilson
*  volleyball with the handprint on it and asked what movie this was. And it didn't get it at first.
*  And then they drew an island around it and a tree and it put a couple of waves and it was like,
*  oh, I get it. It's Castaway. And so it definitely is a very impressive and quite capable
*  technology, but it does feel like sort of the electrical wiring has been created before we
*  have any idea what we're going to plug into it. And that is just a very strange dynamic to me.
*  I should go back and read more. I wonder how much of a vision folks like Edison had for
*  what electricity was going to do. I mean, in that era, merely lighting the room at night was a
*  revolution. So probably didn't need to have too much more than that. But I don't know. How do you
*  feel about this sort of building? They will come. Everybody else can figure it out.
*  I'm a parent. And so what this reminds me of more than anything else is the kind of thing you do as
*  your kid. You're like, do you know what this is? It's a toy dinosaur. What's that? The window. You
*  ask the basic questions. You check their knowledge. You fill in gaps. You see why they're strong and
*  weak. You're building up muscle memory. You're building up components. You know, they'll need
*  those components to then do things that are more impressive to synthesize them. The idea is, well,
*  if you know what everything in the world is, if you can recognize what people are gesturing at
*  in various ways and do other things, this then allows you to do things that actually matter later.
*  And it's also just evidence of intelligence, evidence of comprehension. And that's all they're
*  trying to demonstrate there in some sense. Like it's not the final exam. It's not like
*  the job. The job comes later. But yeah, these are not use cases. These are not things you would
*  actually do. They're a fun little game to have a play fictionary and try to get the thing. It's okay.
*  But man, like pretty big man. Like what is the vision of the future? The vision of the future
*  seems to be the universal assistant. The idea is that you tell it what you want it to do or
*  what information you want it to tell you or anything like that. And it does what you want
*  informed by all of this context. The same way they're really smart, like knowledgeable assistants
*  who's gotten a lot of experience if you would do. And the thought is, well, go from there. What do
*  you do for a person? Well, whatever you want, right? Like as far as they got.
*  So how do you, yeah, it feels, I mean, there was so much talk of her this week and leading up to
*  the events that I found that very striking. I haven't gone back and watched that movie in a
*  while. I don't know if you have or how fresh that story is in your mind, but would you read that
*  movie as a positive vision of the future? Would you, I've heard kind of seen takes across the
*  spectrum from people being very excited about it to people saying it's a dystopia. And then others
*  were like, well, it seems like it's more in the middle. How would you read that story first of
*  all? And then I'm interested too, to hear, do you think this is where you personally are going to
*  go? Are we all going to be walking around with her in our ears? Meta's got their, we just heard
*  they've got an earbud that has a camera in it in development. So that seems like an interesting
*  form factor for the her future. Anyway, how do you start off with, how do you read that story?
*  So from what I can tell, right? Like it's not, it's good in the sense that it's not a dystopia
*  and it's not a utopia, right? It's not pretending that this is all one thing or another thing. It's
*  saying here's a scenario, here are some things that might happen here from speculations as to
*  how some aspects of that might go. And it's up to you, the viewer, determine is Phoenix better off
*  in these ways or worse off in these ways? Is this a healthy or unhealthy way to go about doing things?
*  Is it good or bad for his personal growth? What is the salient alternative? What does this do to
*  society? And then ignoring the ending, because as usual, the actual big picture, like ASI safety
*  takes are terrible. But if you just look at the concrete mundane questions it's raising,
*  I think it does it from what I can tell it does a good job of not judging in every sense. It's
*  saying like, here are some things that we expect to happen. And my reading is something like,
*  if you're treating the AI, like it's a person, developing a relationship with it and getting
*  emotionally invested in it. And especially if you're treating it like you might treat Scarlett
*  Johansson in some sense. And this is not practice. This is not reps. This is not training. This is
*  not experiments. This is like real for you. In that sense, it's not good. That's not good for you.
*  And it's not good for society. If everyone else is doing it too, it's going to make it much harder
*  to get real connections with other people. In that sense, if you're using it as certain different
*  things, if you're using it as like a source of advice, a source of information, a coach,
*  a sounding board, like there are testing grounds, there are ways you can use this that are good,
*  be good. They're obviously good using it as like a tutor to teach you new things. It's obviously
*  just great. But like, why, how could you possibly think that it's bad? But there are obvious ways
*  that you should go, wait a minute, this is not healthy. This is like taking our evolutionary
*  instincts and then putting something on there that was not, that is mimicking the thing that's not
*  supposed to be the thing. And it's bad in the way that like pornography is bad. It's not that you
*  would never ever use it necessarily, you would want to ban this, but like too much of this is bad.
*  Like you have to touch grass. And like the warning of her, right? Again, if you just don't worry
*  about the ending too much, like you get the concreteness, the warning is that this can substitute
*  for other things. And then if you let that go too far, that can be bad for you. And the promise is
*  this is actually really cool and exciting in other ways and has a lot of a negativity.
*  And the question is how do you balance that? And this is not a new problem to AI. We've had to deal
*  with this with a lot of new technologies like mobile phones, social media, or the latest ones.
*  The one that I keep coming back to more and more is television, actually. Partly because like with
*  social media and phones, we have this pretty big debate as to what's happening right now and it
*  hasn't played itself out. We haven't made the full adjustment. With TV, we're at the end of the road,
*  but we moved on to the next thing. We've seen what it did. We've gone through generations.
*  We can look back and ask ourselves what happened? How did we deal with it? What did this do to us?
*  And the more I think about it, I think that that situation where it's not like they made
*  all these warnings about how horrible this was going to be. It turns out everybody was being dumb.
*  Situation in which everyone made these dire warnings about how horrible this was going to be
*  and they were just correct. And it didn't destroy our civilization. We're still here.
*  But the things all just happened. The impact on people that we were worried about, they just
*  happened. And we now live in the world that resulted from that. And it turns out that was
*  eminently survivable. And we've gotten richer enough and better enough in other ways that it's
*  okay, mostly. But one thing you notice is that basically everywhere that got ubiquitous television
*  is now below our place, but level of fertility. So these things can be extremely unhealthy.
*  What do we do about that? So how would you characterize the
*  impact of TV? Obviously heard the fertility point. I guess my general sense would be that
*  it has just given us such a ready solution for our boredom that there's like just
*  fewer passion projects, fewer people developing new quirky hobbies, fewer people just chasing
*  random stuff because it's just easy to kind of go there for a bit of entertainment. Is that your
*  mainline narrative as well? I think it ate massive numbers of hours in the day. And yeah,
*  it made activation energy so much more expensive to get. It made gumption much harder to have.
*  It substituted for a lot of other things that led to good places that built up and had increasing
*  marginal returns to devoting your time and energy. And it taught us to be hard potatoes, right?
*  Passive consumers of information just sit there. We consumed massive amount of advertising.
*  We forget now in the internet age where we're pissed off that our 30-minute show has three
*  minutes of highly skippable advertising on our podcast. It used to be that your 30-minute show
*  was 22 minutes a day. It was a horrible ratio, like 25% ads. And nowadays I watch a sporting event.
*  I make sure to start late if it's not a huge event because I can't bear the idea that there are
*  commercial breaks. This is so bad. But that's the correct reaction if you have the option.
*  Why would you want to endure that when you can just be slightly delayed? It's not the
*  super bowl, is it? If it is, then you're stuck. And also the ads are great. But most of the time,
*  the ads are terrible. And it also, people built their lives around this. They built their
*  schedules around this. And they stopped planning things with people. The whole Bowling Alone
*  phenomenon, I think people underestimate how much it was just television. It was just,
*  there's a show I can watch. There's a thing I can do. And so I think it sounds like a lot of work
*  and requires coordination and requires an activation energy. And I don't have to. I can just think,
*  now it's Netflix, of course, and chill or whatever any number of similar things are.
*  And I watch still today, at least on television. People think it's over, but it's not over. And
*  am I better off for it? I think so. But I'm not at all convinced. The other thing is just,
*  you used to sit alone with your thoughts and just be willing to be bored. You used to like
*  do all these things. And now we have so many different things. It's not just the television,
*  it's not the phone. It's now, you know, you can listen to a podcast, you can listen to
*  music anytime, anywhere. You can do all these other things. You can just scroll endlessly.
*  And so it's been supercharged. And all these things matter. And all these things change us.
*  And having an AI at our fingertips all the time, again, even in this big sort of mundane
*  utility world, right? It's not particularly dangerous, doesn't really transform everything.
*  It's going to change a ton of things. And it doesn't necessarily mean we're going to
*  choose to do smart, high level things with it. One thing that's striking about all the
*  character AI style things out there is they're freaking dumb. They don't, they spend a ton of
*  time customizing the experience so that you get the type of interaction you want. The kind of
*  thing that's satisfying to people, but they keep not investing in highly capable models to power
*  those interactions. They're ridiculously stupid. So often, if you look at what people are reporting
*  back, or you try them out in my experience, like you'll be lucky. I mean, you're not just not
*  getting 3d4. You're often getting like below three and a half. You're getting something that's like
*  abysmal. Yeah, that was really striking in my testing of replica. And it's gotten significantly
*  better. But it is amazing how I'll never forget the line from Eugenia, the CEO there, she said,
*  going back even before language models, they started this project with the idea of addressing
*  loneliness. And she said, we knew we couldn't make a bot that could talk. But we thought maybe we
*  could make one that would listen or could listen and could make you feel heard. And she was pretty
*  open about the fact that they use like pretty simple tricks. And she used the term, not my term,
*  her term, parlor tricks in the early days to just make people feel heard. I'm mixed on that. I feel
*  like that's another one of these things where it's good for some, but it potentially becomes a big
*  problem when it gets to be too broadly too good or too broadly adopted, because they have research
*  out that shows that, and again, this is like done over a year ago, before the current generation
*  of language models, which they haven't even fully implemented. Last I checked. But already,
*  their product was helping people reduce suicidal ideation, helping people who need reps, get reps.
*  People by and large did report that they were more socially engaged as a result of having this
*  outlet or kind of practice ground, training ground, whatever, however you want to conceptualize it.
*  So it seems like it's like, even in that limited form, it's good for this sort of pocket of people
*  who are really struggling. But then I do wonder, similarly to what you're saying, like, how does
*  that change life if it becomes really good and compelling to people who are not really struggling,
*  but could do other things and maybe now don't do other things so much. Hey, we'll continue our
*  interview in a moment after a word from our sponsors. Hey, all Eric Torenberg here. I'm hearing more
*  and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30 year old ex-fang senior software engineer as much as the next guy,
*  but honestly, I can't afford them anymore. Founders everywhere are trying to turn to global talent,
*  but boy is it a hassle to do at scale from sourcing to interviewing to on the ground operations and
*  management. That's why I teamed up with Sean Lanahan, who's been building engineering teams
*  in Vietnam at a very high level for over five years to help you access global engineering without
*  the headache. Squaw, Sean's new company, takes care of sourcing, legal compliance, and local HR
*  for global talent so you don't have to. With teams across Asia and South America, we can cover you
*  no matter which time zone you operate in. Their engineers follow your process and use your tools.
*  They work with React, Next.js, or your favorite front end frameworks. And on the back end,
*  they're experts at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost
*  more than the random person you found on Upwork that's doing two hours of work per week, but
*  billing you for 40. But you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squaw.com and mention Turpentine
*  to skip the wait list. Omniki uses generative AI to enable you to launch hundreds of thousands of
*  ad iterations that actually work, customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it too. Use Cogrev to get
*  a 10% discount. I wonder how you think about the... So if TV just happened, then maybe this is just
*  going to happen too, right? We're all going to be walking around with this thing in our ear, and
*  it'll be... I mean, it was striking how responsive the voice interface was. They talk about between
*  2 and 300 milliseconds latency to respond, and that is normal conversational interactive response
*  time. When we go edit our podcast into script, the normal break between words, if you have a long
*  silence, they'll take it down to 300 milliseconds as their default for... You had a gap, but you
*  want to just shrink that gap to make it sound like it never happened. 300 milliseconds is what they
*  have. So if it can respond in less than that, it's definitely going to be in this similar zone to
*  normal interactive conversation. I do wonder what forces are going to shape this. It does seem like
*  it probably matters a lot what the business model is behind it or who's doing it and what they're
*  trying to do for us, to us, with us. An advertising model is very different perhaps from a subscription
*  model. People obviously have also got sucked into social media. There was a time, which I think it's
*  honestly still there to a significant degree, although maybe it's kind of receded somewhere,
*  everybody was optimizing for time on site and you had this like, what can we do to
*  make this person come back? What is the most engaging thing? And it became probably
*  harmfully engaging, not just to individuals, but to society. I do think Zuckerberg, to his credit,
*  has tried to back off of that. I'm not sure if other platforms have, but certainly they've
*  taken some public steps to not reward anger emojis, for example, which I think is a nice,
*  clean, low-hanging fruit win, but still got to give credit where it's due for taking that.
*  Do you have any sort of tree in your mind? What do you see as maybe the forks in the road for
*  how this new kind of ubiquitous technology could develop depending on what our relationship
*  is to it? And you can imagine, I always used to say too, and I think I might have to stop saying
*  this, but ChatGPT, I always appreciated that the branding was not trying to be your buddy.
*  ChatGPT, a name, it doesn't sound like a friend. And the way it talked to you also was not like a
*  friend. It never sends you proactive notifications, which some of these virtual friend things do.
*  Replica will send you notifications on your phone and say it misses you and it wants to talk.
*  ChatGPT, it's just like, here's your answer. Let me know if there's more I can do to help.
*  But it's not baiting you into further interaction. Claude, interestingly, does a little more of that
*  where it'll ask you, what do you think at the end of its responses in a lot of cases, especially if
*  it's more philosophical or open-ended? So I guess there's related questions there around,
*  how do you expect this to develop in terms of how much the technology will try to pull us in and try
*  to captivate us versus maybe try to push us out into the world? And how do you think that will
*  depend on who's developing it and with what business models? Yeah, so these are not the
*  branching parts of the universe that I worry about the most. Obviously, I'm worried about
*  bigger things, but the stuff matters too, especially if the bigger things don't materialize.
*  And I think you get a lot of the nails on the head, especially the subscription versus advertising
*  versus time on site optimizations. So what metrics they're aiming for, I think, are a gigantic
*  question. And then the question of will people be able to differentiate and select based on what is
*  good for them? Or will they be largely falling into these traps where they fall path to least
*  resistance, they get checked into entering skinner boxes, they develop these kind of
*  fake emotional attachments, they use it as an excuse not to engage with the world instead of
*  using it as a tool with which to learn how to engage with the world or to better engage with
*  the world. Every time I write a new post, I'm constantly filled with ideas either that other
*  people have had or that I have myself, or often both where I'm like playing off of them and they're
*  playing off of other people. How could we use this as a tool to make our lives better,
*  not through interacting with it constantly, but for using it to enhance our choices and our actions
*  and solve our trivial inconveniences, solve our knowledge gaps, skill gaps, again, give us the
*  reps in the ways that are relevant, let us practice, let us do all the boring coordination,
*  let us not get interrupted is I think one that's going to become a bigger deal, let us track all
*  of these logistics and all this paperwork and all this stuff that's expensive to us, where humans
*  effectively can only do so many things, even though the amount of actual stuff going on inside those
*  things is often small. AI can solve a lot of these problems for us, but we have to want it to, we
*  have to care about that and it has to be something we prioritize. I'm really hoping for a subscription
*  model that I think one of the best things that OpenAI did was go completely advertising free,
*  completely steer the customer free as far as I can tell. There's this huge amount of revenue
*  and ability that they've just given up entirely and instead all they're trying to do is answer my
*  query, charge a flat rate or charge an API for marginal cost providing it is, and that's it.
*  And as a result of that, that has become for many top people a standard, right? Like you've learned,
*  oh you can't just become a miserable person. The difference between a AAA by once carefully crafted
*  experience game that's trying to do something good for you, which I think is a wonderful thing and
*  people should do more of it than they do with anything, and the gotcha games and the mobile
*  experiences and the free to play is, which are designed to hook you and trick you and trap you
*  and exploit the whales that can be exploited and makes everyone else's life miserable to make sure
*  they can exploit the whales and that stuff you just don't want to touch for the most part.
*  You can occasionally, they happen to create an experience that's good enough that if you are
*  bold enough, you might be confident enough in your own self-restraint, you can go into the
*  lines, but mostly, see these mechanics, you should run, right? You should run as fast as you can.
*  And it's the same thing, right? You have, JetGPT is inherently a very healthy product.
*  They're not worried that people are going to do something bad for them on a personal level because
*  they use too much JetGPT. I just, I haven't even heard a single story. Same thing with Quad, same
*  thing with General. These companies are being very responsible in the ordinary sense. Character AI,
*  with replica, they're not. Replica is very obviously the predatory free to play,
*  trick you into coming back, like message you when you're away, give you your daily reward or
*  various types. Like every time, oh, you can get more free messages by waiting and then come back
*  for them. I know where this comes from, right? I know about delayed variable rewards. I know daily
*  login bonuses. I know all the tricks. I was in the gaming industry. I know how this stuff works.
*  And when you see that stuff, you've got to run. And so the other question is if we don't regulate,
*  if we don't mandate, because the free society, we really shouldn't be regulating and mandating
*  this stuff, right? This bad incentive drive out good or just good drive out bad, who wins this fight?
*  And if the bad guys win in this sense, it's going to be a pretty miserable time for people
*  who get trapped. But my hope is that people with the best models are presenting good experiences.
*  And that can continue and we can scale that. And the other question is what happens with the
*  advertising model and where is the advertising, right? Because like,
*  right now, advertising is clearly delineated. It's clearly distinct from the experience. But
*  with the large language model, it seems very easy to say, well, we're going to give you a
*  free experience where you can ask about various different products that you might want to compare.
*  But if you just want a little bit of priority in what's discussed and which creatures are
*  highlighted, and whether we talk about Coke or Pepsi, or we talk about Tide or one of the
*  competitors, you're welcome to pay us. What happens in that future where suddenly this
*  thing is suddenly pushing stuff on you and you can't necessarily tell the difference,
*  and the labels are increasingly convoluted. If you aren't paying, you're the product,
*  right? In that sense. And we can reach one of those worlds, and then maybe you even have to
*  get your second AI to watch what the first AI is doing. If you're smart, you can notice when
*  this thing is happening. You can double check what they're saying. I don't want to get too far away
*  from news that we can get so much to get through. I do think this is really interesting. The analysis,
*  many people have covered the news. So I think where we hopefully can add value is with a little more
*  synthetic analysis. I do have one word of defense for replica in that having gotten to know Eugenia
*  a little bit, I do think she is really trying. And they do have a subscription model, although
*  they do have these add-on by a new outfit for your replica type things going to. I think that research,
*  which I do take as reasonably credible, it came out of a group at Stanford and they weren't directly
*  involved in it other than handing over data, as I understand it, is pretty compelling. I do think
*  they're headed into a very challenging balancing act of a future. One thing she said to me that
*  was really interesting, and I do see that this is like another dynamic I'm going to ask you to analyze.
*  On the one hand, they started with relationships and basically no mundane utility. And then with
*  Chet GBT, we have pure, isolated, episodic help on whatever you're looking for help with,
*  but no relationship. And I was struck that I heard from her actually a couple months ago,
*  last episode we did, that she is moving replica toward more of an assistant.
*  And she said something I thought was really interesting, which was maybe the moat in AI
*  is relationship. That you don't swap out your friends because I knew better friend,
*  potential friend came along. You have some sort of loyalty to your friends, like the history matters
*  what you've been through together matters. And she was, we're going to become more of an assistant,
*  but we still want to have this notion of relationship. And maybe that is where the moats
*  in AI come from. That's why maybe people don't switch at the drop of a hat long-term. Chet GBT,
*  on the other hand, is headed that direction a little bit too, now it seems, where you've got
*  certainly the voice is like much more given to relationship and it's like developing memory and
*  it's obviously going to have longer context and all these sorts of things. So these maybe seem to
*  be converging. I wonder how you think about the ethics of Chet GBT, like going more in the buddy
*  direction. If this is something that you think, and we have like wave of departures from open AI
*  to talk about too, I wonder to what degree you might speculate as to how this move toward the
*  like more engaging personal relationship possibly could have been one of the things that the safety
*  team might have objected to. Certainly I would have been like, Hey, do we really want to go this
*  far, this fast? Can't we keep the voice just a little flatter? Okay, cool. It's responsive,
*  but does it also have to be so thirsty? Like in our first release? But then there's another dynamic
*  too that I think I would, if I'm reading into what they're doing correctly, Altman's now saying,
*  well, we want to get into not safe for work content. We want to be able to do some of this
*  stuff, even gore, even like erotica, whatever. But we don't want to be making deep fakes.
*  And I'm like, on the one hand, you might say, well, why would they be doing that? That seems just,
*  why would they even want to touch it? On the other hand, you might think, well,
*  maybe they think they can do it more ethically than other people can. Or maybe if they do
*  90% of the stuff that people want, it'll take the air out of the sails of the sort of totally
*  unscrupulous actors that would be doing your, if you can get NSFW AI from open AI, that's like,
*  R rated. Maybe you don't need like Taylor Swift deep fake porn that's X rated or something.
*  And maybe they think, hey, we can be like the good guys that do this racy stuff, but stay on
*  the right side of the worst ethical lines. There's a lot there. Convergence to buddies.
*  And how do you think they're maybe thinking about like how they play against like other
*  actors that they may consider to be worse actors? So I'll start with the last part.
*  I wrote out my model specs analysis for open AI, but it kind of seemed to everyone at Open AI is
*  going to be hella distracted this week and everyone else as well. I'm going to hold it for another
*  week or two and refine it and adjust it and then post it later. But one of the things I have in it
*  in fact, an endorsement of NSFW. Right. I think you have to ask, is this actually harming anyone?
*  Is this bad for people who are not the user or is this so obviously just terrible for the user
*  every damn time? That as a free society, we need to say no. And as far as erotica or gore,
*  the answer is just obviously not. Right. People have this desire to be thirsty, right? They have
*  this desire to be horny on vain. They have this desire to be like playing in these ways and getting
*  these experiences. And if you don't let them get it at home, they'll get it on the street.
*  You can't shut this stuff down. It's just part of the human experience. And yeah, I think absolutely
*  if somebody wants to create pornographic images, they're not deep fakes of individuals who have
*  not given their permission, then why shouldn't we do that for you? Given we have verified you're an
*  adult, maybe we've charged you extra because why not? Maybe. But why shouldn't you be able to do
*  that? If you want to create a picture with a bunch of blood and gore, why shouldn't you do that? They
*  recognize with Sora that you can't do sex, you can't do gore, you can't make most of the interesting
*  things that people do with video. You can draw the line at PG-13, a lot of them are just out the
*  window, especially every individual element has to be very carefully curated and gate-kipped and
*  so on. It's just not going to work. And so yeah, I think that you draw the line specifically at
*  inappropriate portrayals of actual individuals, but you don't want to make an obscene,
*  Taylor's-like thing. That's a problem. You should catch that. You should stop that from happening.
*  And there's a certain level of difficulty you need to impose on that before someone can be
*  allowed to do that, but you have various different tricks to defend yourself against it.
*  But I think if you want to either create a pornographic beat thing of no specific person
*  that just plays to whatever it is you want to see an image of, or if you want to create a picture
*  of Taylor Swift wearing a different colored outfit singing in a different venue that she never visited
*  for her errors tour, as long as it's got a watermark, what's the problem? You want to
*  take a picture of her singing at your son's birthday party and have fun pretending that she
*  was at your son's birthday party and play her music, right? Because you can just record that
*  and hit play. That's kind of the service. What's so bad about that? Why is that a problem? And
*  obviously different people have different opinions and maybe each celebrity should decide what level
*  reproduction is okay and not okay. But certainly the situation where Barack Obama can't be generated
*  by an image model, like giving a speech at the wrong college, it's just like, done to me. And
*  again, is going to force me to use a different image model for those purposes. And how long is
*  it going to be before those free image models are just trivial to set up and trivial to use and
*  everyone starts using them? I keep waiting. I have to be able to vision on my computer and I tried
*  it out for a bunch of stuff. One thing that's very good for is you tell it to create a hundred
*  copies of something and then you come back 30 minutes later and then you check this thing,
*  scroll quickly through them and see if any of them have what you wanted. Maybe you go image
*  damage on that one and maybe you figure out what, maybe you just use this to diagnose,
*  okay, here's what's wrong with my prompt and try a different prompt. And you can't do that if you're
*  using the free internet services because that would cost them an arm and a leg. Now I'm using
*  my own GPU, so it's fine. Or alternatively, use that to create stuff that they wouldn't let you
*  create because you want to see what you can do and you want to create it and maybe you want to enjoy
*  it. So I moved on to a basically, it's become especially obsolete that I just use the online
*  ones now, but I've been waiting for Stable Fusion 3 to be easy to deploy and now to go back to,
*  okay, see what the data is. In general, yeah, I think they should offer the services that you want.
*  I don't think it should be this thirsty by default. I think this idea that suddenly you have
*  Star Wars Johansson acting all 30 with you, like when you just asked what the weather was outside
*  with no indication you wanted thirstiness, that's weird. I don't think that's ideal.
*  I think that we went too far. But if you put in your user preferences, you dial up the thirstiness
*  tone, right, you need select, you want the Star Wars Johansson style voice, I don't think shame,
*  like it's fine. Enjoy yourself if that's the statement you enjoy. And again, you should be
*  very careful with consent and very careful with permission when there are real people involved.
*  But I think a lot of real people will be very happy to give their consent either for free
*  or for a very nominal charge. You ask me if someone wants to use my voice for some ungodly
*  unknown reason on Sketch EPT, if it's just a handful of people I'd say go ahead, if it's like
*  100,000 people, I'm like I should be paid. But it's about reasonable compensation here. And I'm sure
*  a lot of people feel the same way, including people whose voices someone might want to hear.
*  Are you telling me I shouldn't just pay an extra dollar and get the Morgan Freeman voice for all
*  of my narrations and my explanations? That's cool. Why shouldn't I do that? Or maybe I want to
*  start with Johansson. Again, she gets paid. That's fine too. And then like you were there's some other
*  stuff that you were asking about that I've almost forgotten at this point, just because it's such a
*  complex question. So you just have to remind me what we were talking about.
*  What I am thinking about is, and it is there's a lot of issues that are intertwined here,
*  but there's a couple dimensions of convergence. Actually, there's like the convergence to the
*  buddy form factor. And then I also see at a lower level, and we're gonna have an episode,
*  I'm gonna have Alex Albert, he was a prompt engineer and I was leading the developer relations
*  function at Anthropic. And I was asking him about how all the APIs are converging too,
*  and how they think about that in the sense that it may create a winner take all dynamic.
*  So on the one hand, I'm like, man, I don't feel great about sort of the trend toward relationship
*  first in general. I do feel pretty good about Replica for the people that are really struggling
*  with loneliness. Not sure how I feel about it when it gets to like a super broad based thing.
*  I'm not sure how I feel about OpenAI being so thirsty with their voice. But then if I go down
*  one level and I look at the API and I see convergence there, and it's a one line switch,
*  possibly with a little bit of prompt engineering, definitely with a little bit of prompt
*  engineering, but it's like close to a one line switch just to go from GPT-4 turbo to Cloud 3
*  Opus to back to GPT-4. Oh, to Gemini 1.5 Pro, whatever's next. That to me is worrying dynamic
*  in that if all of the integration points have converged to essentially the same service provided
*  in the same way with a down to a one line change, then it becomes a winner take all dynamic in the
*  like whoever has the best model in theory can win all the business very quickly. Like why don't we
*  switch to the new one? But then maybe one reason that could not be so a winner take all with one
*  release to the next would be this relationship dynamic. So I'm like, not sure I like what it does
*  to society if we're all like in these parasocial relationships, but maybe I do. What it does
*  to soften the super intense borderline winner take all dynamics. I'm not even sure to what
*  degree those exactly overlap because one is the app layer and the other is the API layer
*  that powers the app layer. But what do you think? I see the opposite. I think you're thinking about
*  this all wrong. So first of all, you have more than one friend and I have a lot more than one friend
*  and I choose which friend to call based on what we want to talk about and what we might want to
*  go do. And sometimes I have a group of friends, sometimes I have one, sometimes I have a different
*  one. And I would get bored if I was hanging out, my best friend's name is Seth. And if we hung out
*  every day all day and try to talk about everything, I'd be like, this is not it. I don't just want to
*  just hang out with Seth all day. But so I hang out with other people too. And the switching, this
*  means that you are not locked in, right? You're not stuck. So quite the opposite of winner take
*  all, right? It lets you move around and even character AI and replica understand this. You can
*  talk to 10 different bots, right? For different purposes. And of course, you, at minimum, you want
*  to figure out, you have this one for when you want to talk about engineering, this one for when you're
*  thirsty, this one for when you just want to talk about restaurants in the area, blah, blah, blah,
*  which makes perfect sense. And chat GPT has his GPTs and now Jim and I is going to have his gems
*  and so on. And then you have this thing where you can plug into a different LLM. And so for me,
*  I have changed my primary LLM reasonably recently from GPT-4 turbo to Gemini to Claude,
*  and now back to GPT-4. And in many cases on a dime, it doesn't mean you don't use the other ones. It
*  means that like, when I want a variety of answers, I'll call all three of my friends and I'll ask them
*  in some sense, and I'll ask them, Hey, what do you think? What do you think? What do you think?
*  I'll compare notes. And then I know what I know who's good for this, right? I want to know the
*  PDF. I want an image. I didn't create this kind of image. And so I put portfolio and then as
*  people advance, you weren't okay. So then you just captured more of my portfolio for now, but then
*  that switches back and I want this variety. I want these optionality. I don't necessarily even want
*  these things to know all about me, certain aspects of me. Then I do different things. Also data
*  portability is probably going to be a huge thing. If you're at replica, you build up this relationship,
*  but are they going to allow you access to your records and data? And that's like a pretty toxic
*  thing for them to do. I assume they won't. What happens when you download the chat log,
*  upload the chat log into into Gemini three or whatever it is and say, you're this guy.
*  Here's everything that you've said to me. And here's everything I've said to you.
*  And it learns all about you now. And now you have your new assistant that knows what your old
*  assistant often you don't switch employees because you don't want to have to train them to explain
*  all the context with them. But now that context is just copy paste. That's like a huge, I don't
*  expect winner take all from this unless the winner deserves it. So like GBD five is out and everyone
*  else is still at four level. Well, of course I'm just going to 90% of the time plus be using chat
*  GBT, got GBD five. But if it's a marginal change, like it's been recently, where it's just like one
*  of these things is a little bit better, that's completely different. It's particularly the lock
*  ins and the relationships that I think are the places where you're likely to get a picture with
*  a take all scenario. So if Gemini knows the contents of my Gmail, those are the contents of
*  my sheets, there's the contents of my docs is creating workflows where it generates new documents
*  and new memories, sees my photos and all my photos, I start taking pictures of all my food, so it knows
*  what I eat every day, where I've been, etc, etc. It has all of this new context, it'd be very
*  difficult to transfer this context. Now, suddenly, I have this huge thing where every time anything
*  is remotely personal, I want to use Gemini, right? And that becomes a thing. But I don't think that
*  in general, I've been seeing this lock in, unless of course, the people develop this kind of emotional
*  attachment, right? This may be romantic, maybe it's something else. I'm basically saying that's not
*  like that going too far is not particularly healthy. Right? I think that's bad. I think people should
*  strive to avoid that. And different or pretty special circumstances, like beyond what it takes
*  to get like reputation, reps and practice and stuff like that. But I'm optimistic this is this
*  is the conversion seems like a friendly thing, right? Like, why wouldn't you? Like, how amazing
*  would it be if you could transfer your stuff and your connections and your knowledge between social
*  networks, between Android and iPhone, between all these other things that are like converts,
*  but are seemingly incompatible, like compatibility is just almost always good.
*  Yeah, it seems good for the consumer. I do wonder about how in a world where Google have their data
*  on the calendar, and then OpenAI does their launch one day in advance, it does seem like
*  there is a potential for exacerbating the general one of the biggest worries in AI is that
*  the and I know I'm not telling you anything you don't know as well, or probably better than I do,
*  but the arms race dynamic between either countries or even just leading companies within
*  the United States, where, hey, we got to get this out, we got to beat them, you have x time to do
*  your testing, and we're launching and that's the time you have. And so corners start to get cut,
*  perhaps. This feels like the liquidity with which people can move about the market would enable that
*  dynamic or encourage that dynamic because if OpenAI is like about to launch, one party is going to
*  beat us, we got to get ahead of them. Now you have this and that sort of depends on the idea that
*  if they're out ahead of us, then everybody's going to switch to them and we're going to be
*  screwed for a while. And that could be screwed in revenue, it could be screwed in data, it could be
*  even just pride and reputation, which certainly seems to be a big part of what's happening at the
*  moment. You don't worry about that. To me, I'm convinced by your multiple friends argument that
*  as long as there are different things in the same ballpark and they have different characters, you
*  go to different things. I do personally find that as well. I still, if only because chat GPT has the
*  native coding environment, even if Opus is a little bit better on coding, like the fact that
*  it can execute the code on chat GPT side, it keeps me there for coding. Now it actually with O probably
*  is notably better on coding as well, but Opus is a better writer. So I go to it for help with
*  writing. So I do have my different AI friends for different purposes at the retail consumer level,
*  but in my app building, it is more of a, I'm going to make a choice, right? If it's Weimark
*  and I'm going to have a language model or a vision language model process all the images of a small
*  business that's just uploaded their library, we're probably pretty much going to just do it with one
*  model. And in practice, like you can switch really easily. That dynamic doesn't seem like a big
*  concern to you still. It can go both ways, right? If switching costs are low, then me announcing a
*  day before you doesn't really matter. So what you get my customers for a day and then I switch back,
*  like who cares? If it's incredibly expensive, well, then if you can get ahead enough to convince me
*  to switch, I'm stuck. And so maybe you get incentivized to try and capture that market
*  a lot more, or maybe you're trying to outdo each other continuously or try and say just a step ahead
*  because we don't take a lot. But my guess is there'll be enough differentiation between what
*  features these different tools have and in what details you want to use and in how you customize
*  them. I've got to put a decent amount of work at this point to customizing my instructions for
*  Chat GPT because they have custom instructions and I haven't done that for Gemini or Cod yet,
*  but when they offer that and I decide to do the time, I will almost certainly do that. And they
*  might look very different because I'm trying to specialize, right? They might be like, okay, so
*  when I go here, this is what I want. So it's a different set of instructions. But as an app
*  maker, you're not going to want to switch every time there's a little incremental improvement,
*  right? So it's just not the same thing. Look, winner take all in some sense from a safety
*  perspective is ideal. If OpenAI or Anthropic or Google was out there two years ahead of everyone
*  else and their model was just better. And so for all dangerous purposes, they were the only ones
*  that mattered, then there are advantages to that. But I don't think that the interoperability is
*  going to change whether or not that turns out to be true in an important sense. I don't get
*  substantially changes necessarily, the pressure we're putting on people in that way. But also,
*  one of the things about this last week that was like why I really enjoyed this week on the release
*  side, even though there's other things that I didn't like as much, obviously, was that everybody
*  is now seems to be focused on things that help people have a better experience and improve the
*  world, but they don't advance the core intelligence underlying system. So to me,
*  that's just win. I want CHAP GPT to be better for its users without becoming more intelligent
*  in the ways that they get more existential dangerous. It's not that it stays in its
*  current state and just gets all these new cool features. That's just the best of the world.
*  Love this world. And so I was really heartened to see the direction people were taking it,
*  see these new developments, and I can wish everybody a great success. Obviously, it built
*  a certain amount of revenue and hype and pressure, but I think mostly that's already built in. And
*  I accepted that's just the world we have to live in. So why begrudge? Why not just have a good...
*  Don't throw me a good time. Just keep going. Yeah, I'm with you on that. My standard line with the
*  GPT-4 class models is we're in this sweet spot where it's powerful enough to be really useful,
*  but not so powerful as to be a real concern. And I do think that's great. And I do think all these
*  integration points are great. The enhancements of just, as you, of course, famously call it,
*  mundane utility are great. It doesn't feel... And I hear the argument too about, yeah, if somebody's
*  way out ahead, then they have the luxury of doing it right, taking their time. It doesn't seem like
*  we're in that world to me. I do expect OpenAI is probably still about half a generation ahead
*  internally. My guess is that they don't make the best model free if they don't have a significantly
*  better one coming before too long that's going to get everybody paying again. That could be wrong,
*  but that would be based on all kinds of rumors and Intel and just how much time has elapsed
*  and public comments from Sam Altman. It does seem like they probably still have one additional turn
*  that Google may not have made yet. But overall, it does feel like they're close enough where
*  they're running, generally speaking, neck and neck. And that part does concern me. And Meta is
*  not far behind either. They just put out a paper yesterday where they had trained a new model called
*  Chameleon, which is very natively multimodal. They call it early fusion, meaning text and image
*  tokens are encoded in the same way, basically share all the same weights, trained with 10 trillion
*  tokens, which is not a small amount. And unclear if they're going to open source that yet, but same
*  as all these other natively multimodal things that they're answering and definitely just showing
*  that you're not going to stay in front of open source for too long, even if you are ahead by
*  a full generation, generation and a half, you're going to have to keep going. I'm still not convinced
*  the other direction either that I shouldn't be worried about the liquidity at the API layer,
*  the ease of switching and the sense that may create where we got to one up these guys.
*  I do see that dynamic kind of developing and it does seem problematic.
*  It is. I don't think these things that basically what I'm saying is I'm not sure these things
*  intersect that heavily in terms of the correlation is close to zero, not that it's like going the
*  other way or anything. These things seem to me to roughly cancel out in the sense that like
*  that same pressure is always going to be there. Open AI and Google are going to try and one up
*  each other. They're going to try and advance them all as fast as possible. They're running into a
*  lot of the same constraints. My assumption is indeed that open AI has somewhat of a lead here,
*  but the fact that open AI seems to be quite responsibly taking their time to build the
*  next thing, whether or not they have a choice, we'll see what happens. But it's really hard to
*  tell who's out in front. I think Google has a history of essentially being far out ahead of
*  what Google actually releases. Google has had a significant number of pretty earth shattering for
*  the time capabilities in the past, and it decided that their lawyers should carry the day and they
*  should not release the products. And so it's not obvious to me that Google has to be behind it all.
*  It's very opaque from the outside. You can't tell. Like it falls as dead open AI is six months to a
*  year ahead or something like that. If open AI is not six months to a year ahead, it would seem to be
*  more likely because Google also has another half or full generation more than they've shown,
*  not that open AI doesn't. My assumption is that open AI, I mean, things don't take that long to train
*  as such necessarily. Yeah, it's more like you get into a position where you're ready to do that,
*  but you have the resources to do that. You have all the data streamlined and you're ready to go.
*  And it's really hard to know, obviously, any of this for sure. It's also possible that there's a
*  big gap between when you have it internally in the base model form and when you're ready to actually
*  release a product. I speculate it also that it's possible that there's a GPT-5 style model. They
*  either could train or have trained, but the inference is so expensive that they think it
*  would degrade the user experience to rush it into market. So they'd rather do this instead,
*  because for most purposes, that's not actually what people want in some form, or they need to
*  scale up their infrastructure. Because they have to choose. They have to either serve GPT-5 to a
*  small number of people or serve GPT-4-0 to a very large number of people. And maybe they think that
*  it's better for them if they serve the second one. I don't know. It's a hard time. In the long run,
*  who has the advantage? Who has the better infrastructure? Who has the better teams?
*  Who has the better capabilities? Again, there are people who know much better than we do,
*  and we'll find out. Yes, in an important sense, I wish it wasn't close. I wish I knew who it was,
*  who was in front, and that they could, in some sense, just take their time. Much more so,
*  and I definitely see the pressure that seems to be building of throwing caution into the wind
*  and just doing some stuff. But again, shouldn't caution be thrown through the wind outside of
*  some certain key moments? When are the moments when you should be cautious? So like GPT-2,
*  we saw some caution for OpenAI, even if that wasn't enough for Dario. GPT-3,
*  again, we saw some caution. We got some dispute over how much caution was warranted. GPT-4,
*  we saw a lot of caution with the release. It seems pretty reasonable to not particularly be that
*  cautious about 4.0. If you've looked at it, you're like, no, these extra modalities don't really do
*  anything of that interest. We know that because we've tried a lot of stuff with GPT-4, and it's
*  not like it's close. It's basically fine. And then here, you're in an over-commercial situation, and
*  they were up against any number of deadlines. You've got the Google I.O. thing coming the next day.
*  You're potentially asking Ilya and maybe John Leike to stay on until after this presentation,
*  so that doesn't distract. So you've got potentially a bunch of things coming up.
*  I want to talk a little bit also about broader market competition. Our mutual friend, Andrew
*  Kritch, coined this term, the big tech singularity, or I think he calls it the tech company singularity.
*  But the notion here, I think, is an interesting one where he basically says, at some point,
*  we may hit a point where the big tech companies, in virtue of their superior
*  AI and compute capabilities, could reach such a position of dominance where they could effectively
*  enter into any industry that they want to compete in and come to dominate it in relatively short
*  order. And I do start to feel like we may be getting close to that, and I think you have a
*  different point of view on it. But my simple thinking is, man, Google has $100 billion cash on
*  hand. So one fork in the road there would be like, are they allowed to buy in or not to these
*  industries? But it's crazy. They got $100 billion cash on the balance sheet. I looked up just some
*  of the big hospital companies in the country. One of the biggest ones, not the biggest, but a big one
*  that I'm familiar with is called Tenet, and they have 58 hospitals. They're worth $13 billion
*  market cap. For one eighth of the cash that Google has on hand, they could buy one of the biggest
*  hospital companies in the country. And then you can imagine them just plumbing
*  med-gemini into kind of everything, ripping out the sort of nightmarish electronic health records
*  that currently exist, putting something in that would hopefully be a lot better, tapping into all
*  this data. They've been able to do these med-gemini things, I would assume, with huge barriers to data.
*  This would dramatically reduce their barriers to data, would allow them to... I'm sure, of course,
*  they'd still have to handle compliance in some ways, but they could dramatically streamline
*  their access to data, train the next generation of medical models, provide med GPT as kind of
*  frontline service. And it would seem to me like they would pretty quickly be the best hospital
*  system in the country if they did that. And then I imagine replicating that across other
*  verticals, education, as we've discussed. Obviously, these things hold tremendous promise for
*  education. The key thing seems to be actually building it in a sort of first-class way, which
*  I'm not sure current institutions are going to do very well. And Google may struggle with it in some
*  ways too. Again, they could buy any number of private education companies for a pittance from
*  their perspective and just run a loss leader experiment to see what they could do in a new
*  vertical like this. Why do you think that's not the case? Do you think that's not true?
*  Dr. Michael O'Neill Because I think they're not culturally
*  capable of doing the things you'd have to do to make that work. I think that their
*  reputational and legal and regulatory barriers to doing that are very serious. And I think that
*  they're not going to be able to deploy technology in those situations that is that far ahead of
*  what people who are simply paying them to use big tech technologies could get in their place.
*  Open AI is not going to be able to use GPT-5 for its hospital system substantially before
*  GPT-5 is released. That's not really a thing. The version of, I forget what the med, their
*  Alphamette or whatever it is that they're calling it. The version that Google is going to put out
*  there is going to be the same version that they have internally, but it's also going to be available
*  to everybody else if the people want it. Yes, it gives them better data to do this, but they
*  could also get that through licensing agreement through a sort of cooperative deal. And there's
*  a reason why basically companies like Google do not put themselves into every dig and cranny,
*  try to do everything and every feature. There's a reason why we see these demos and we're like,
*  do you have no idea what your products can do? Are you not trying to do anything with your product?
*  Are you just leaving that for the rest of us? And the answer is yes, they really are in some
*  important sense. And they are trying to develop their core systems of products, make their thing
*  available, let someone else build off of it, let someone else take the baton, let someone else
*  handle these things. I saw a few weeks ago a story about AI private equity. So the idea is this thing
*  but without being Google. So you go out there, you find a company that's obviously in an AI business,
*  doesn't know it's supposed to be an AI business. You buy the company, you then tell all the
*  employees to use AI, you deploy the AI systems, everyone gets much more productive, the company
*  goes up in value, the company makes a lot more money, you win. You then use the profits to keep
*  doing this. And that seems like a much better model to me. So does being a startup whose job
*  is to raise a lot of money in order to launch this hospital thing. Either we're going to send hospitals
*  or maybe use a private equity thing and buy them out. I don't know, maybe do both. But these models
*  strike me as more what these people are capable of. But Google is terribly scurristic in so many
*  different ways. My understanding is so is Microsoft, so are the other big tech companies in their own
*  ways. You can't simply have them launch an entirely new thing and do an entirely different thing
*  and expect that to just work in this sense. Now, obviously at some point, if you have GPT-9,
*  you can tell GPT-9, go out and buy a hospital system and deploy your technology to help the
*  patients do better and make more money. And GPT-9 just handles all of it because it's GPT-9.
*  But that's not the most important thing that's going on with the fact that you have GPT-9.
*  You bury the lead if you can do that. It's very important census. So as long as we're still dealing
*  with these mundane levels of AI, my expectation is that the big tech companies just, they only have
*  so many Imperial focus points. They only have so much different things they can do at once.
*  And it's not in their interest to do this. There's a reason why Google is constantly buying startups.
*  And I don't think that's going to change. Let's talk about the startup side for a second as well.
*  I feel like I am hearing less about startup acquisitions lately from the big tech guys.
*  Obviously, we had the Microsoft aqua hire inflection. But compared to a number of years
*  ago, it does seem like there's a lot less aqua hiring going on. And certainly, there is bureaucracy
*  at these companies. It does seem like they've managed to clear some of that out in the Gemini
*  department, at least. There has been an interesting discussion on that just in the last
*  24, 48 hours on Twitter where, among other people, Shultow, who is locally famous for his
*  appearance on the Dorakesh podcast said, yeah, basically nobody cares about levels at Gemini.
*  Elsewhere in Google, yes. But in the Gemini thing, it's a very flat, we're all one team trying to
*  make things happen vibe. If you are a startup, I was going down my list of previous cognitive
*  revolution guests and just asking, who is feeling enabled by all these new things and who's feeling
*  threatened by all these new things? And I'm like, I think there's a significant majority of them
*  that seem like they are more likely to be threatened by it, if we're honest.
*  And I do think in the short term, probably still everybody grows because, and this is for some of
*  the reasons that you're saying, that Google is not going to productize everything immediately.
*  They're not going to go to market with the same sort of intensity or focus that startups will.
*  So I'm bullish on everybody's next couple to few quarters still. But I do look at the economies of
*  scale that I see developing in the big tech companies vis-a-vis the startups that are building
*  on the platform. And I'm like, man, I don't like the beyond two to four quarters position for
*  a good chunk of them because they're always going to be a little bit behind on the models,
*  of course, that inside they're going to know what they have inside. They're going to be picking off
*  of what are the biggest opportunities for us. The outside, of course, you're waiting inside.
*  You can also do it for free. Exactly how this is going to be positioned and what you have to pay
*  for is to shake out. But one thing that's definitely clear right now is GPT 4.0 is free for all in chat
*  GPT. It's not free. They've lowered the cost, but it's not free via the API. So right off the bat,
*  you have as a startup, you're like, how do I exactly compete with that? I have to pay for it,
*  which means I have to charge for it, which means I just have all this additional friction
*  compared to somebody can just go to chat GPT and use the thing directly there. And again,
*  just the economies of scale, just man, who can really compete with these guys? We've had folks
*  on the show who specialize in text to speech, who specialize in image generation, and just GPT 4.0
*  once its full capabilities come online over the next couple of weeks, seems like it's likely to be
*  best in class at both of those potentially. You make of like the position of the companies that
*  are building on the platforms right now. So Altman, I think, had very wise things to say
*  about this, right? The idea that if you're building your model, you're of your company,
*  you're building your company and you're building its tag, because GPT N isn't smart enough,
*  isn't good enough, and you're going to build a substitute that's going to for now do a better
*  job, then we're going to steamroll. We're going to curb stop you. It's here to die. But if you're
*  planning here's an apparatus to use intelligence such that when GPT 5 comes in, you switch the 4
*  to a 5 in the function call. And now suddenly your product just works way better. And you're
*  not directly trying to do the thing that the base model can just do. Now you're in a manning shape.
*  And in fact, you have a great company that's going to be happy when OpenAI makes progress.
*  So the question is, can you plan for something where you're happy when OpenAI comes up with
*  a new model and not sad? Or without loss of generality, obviously. So if you're 11 Labs,
*  and you have amazing text to speech right now, then yeah, you have to worry a lot about whether
*  OpenAI is going to curb stop you, because you are fundamentally competing directly with them to
*  offer a technological service that they are going to want. And either you find a niche,
*  say you're willing to replicate Scarwood Johansson's real voice and OpenAI isn't,
*  or something like that. But otherwise, yeah, they're actually going to have things better,
*  and you're going to have to somehow keep up with them. That then requires being big.
*  That's because that's a generic ability that OpenAI is going to develop anyway,
*  because it needs it for its core products. But if you are trying to be a private equity company
*  that buys out hospitals in order to streamline their medical records, well, now you're like,
*  okay, cool, you have the latest AI to just feed into these things to be better. You're like, cool,
*  hand it over, Google. Hand it over, OpenAI. And you plug it in, and your product works better.
*  And you're that much better than competition than you were last month when they didn't have an AI
*  at all. And you had GPT-4, and now you have GPT-5. It's amazing. You're just that much
*  far ahead. And so also, there's no conflict between there are going to be a lot of amazing
*  companies. There are going to be some, we're going to all die before that, because there are going to be some really cool companies.
*  And the current companies are often not going to be the cool companies. It's very possible that
*  every two years, half the existing companies die in this realm, because they got curb stomped,
*  because the thing they're trying to do no longer differentiates them from the core model. The core
*  model was not able to do that. But the other half do well. It's the tech bubble in 1999, right? Where,
*  yeah, a lot of these companies turned out to be doing something that had no underlying value as
*  the internet developed. And it didn't differentiate them. But also, do a portfolio of them. Part of that
*  was Amazon. So you made money anyway. So who do you, could you point to specific companies that
*  you think are like, well positioned? Because I honestly struggle to list too many that I think
*  are going to be like, oh yeah, this is playing to our advantage, how we hoped and puts us in a
*  long-term winning position. I don't find a very long list, honestly. Yeah. The problem with,
*  I think you mentioned this before, is that AI is this huge beat. And so you have to choose
*  where you're going to specialize. And I've made a deliberate choice, mostly not to follow
*  the details of various startup projects. And it's one project that are offering within utility in this way,
*  because they're not that important to the bigger picture. And it's very hard without investigating
*  carefully to have value add things to say about them. Right? So it's okay. I'll see what happens.
*  So I can't say which ones I think have great market prospects necessarily. But I also can't
*  say which ones are necessarily going to get curbsome either. And I would rather them be internals.
*  Right? How do we, I have no idea what the complexity is actually doing to the hood.
*  I don't know to what extent they're training their own model. I don't know to what extent
*  they are working off of GPT-4 or Claw or whatever it is right now, but then adding custom
*  instructions and then scaffolding to try and allow it to much, much better analyze the web and come
*  out with very rapid good answers. And in a sense, there's like a version of Rebuxity that gets
*  curbsomped and a version of Rebuxity that's potentially going to do very well. Right? All
*  depends on a lot of details. But when I look at what are the companies whose tabs I have opened,
*  what are the companies whose stuff I use? And I do not use those things because what I want is
*  what the base model is offering. I don't use Character AI either. Right? But think about that
*  as an example, right? If you're a Character AI, well, if you're just counting on the fact that
*  OpenAI is not going to be thirsty, right? It's not really a great long-term plan. If you're
*  counting on we're going to give them a bunch of tricks that make this thing feel like human
*  interaction because you're a replica, because the models aren't good enough to simulate real human
*  interaction on their own, that's not going to be sustainable either. Right? But if you're building
*  your AI bot such that when you make it smarter, it provides a better experience, but you know all
*  these things about how to build relationships that OpenAI doesn't know and is never going to find
*  that. You could be in a great spot. There's nothing stopping you. Right? And in theory,
*  that stuff should get much, much better. And it should especially get much better when you start
*  adding video generation and virtual reality, which is where I assume is the future of that sort of
*  thing a few years from now in the line. And if you're ready for that, great. So it just depends
*  on, again, are you trying to be future-proof? Are you getting where the fuck is going?
*  Or are you fixing the fact that right now there are some flaws that you can better address and
*  you can go to market. But there's also room for people who sign brightly for a year or two and
*  make a bunch of money and then fade away because they're tech- That is honestly, when I've considered
*  any sort of new entrepreneurial endeavor right now, I'm like, I think you're right to cite
*  Sam Altman and I think that analysis is right. But I'm like, man, that's pretty tough. I can't
*  identify too many things where I'm like, oh yeah, if I do this, then I'll be like much enabled by
*  the next model, but I won't be threatened by it. The majority do seem like right now, like they're
*  in this kind of compensating for weaknesses, trying to go to market, and they have to, right?
*  Because if they don't compensate for the weaknesses, they can't really go to market successfully.
*  If they don't go to market successfully, for most of them, aside from a few that can maybe raise
*  enough money to really make a long-term play and not feel rushed to market, but that's obviously
*  not a super common position to be in, it feels tough. So when I've considered- Ashwin,
*  I don't think I'm going to start a company in the short term, but when I have considered that,
*  I've felt more drawn to this. What would be like a flash in a pan that meets a need right now
*  that could grow really fast that maybe doesn't make sense 18 months, two years from now,
*  but which could be like a good winning short-term sprint that, sure, inevitably gets burned up in
*  the supernova of the animation models? Right. Even if your original tech gets
*  burned up in the supernova, right, by learning a lot about the business and your customers
*  and the golden relationship with your customers, you might be able to entirely turn this over
*  into something that still makes sense. And there's a lot of places where getting it right,
*  making it easy on the user. We talk about all these custom instructions, all this looking
*  between different models and different companies, and all of these sophisticated power user things
*  that we're doing. And we got to remember that most people aren't even using these models at all.
*  And people are using them at all. Most of them are incredibly unsophisticated, right? They're
*  mostly complete civilians. And most people will never touch a settings button in their life on
*  any of the apps they use. No matter what option you give them, no matter how valuable they are,
*  they will never learn what they are. This is not how people work. So if you can just do some basic
*  good customizations and set up good defaults and handle some regulatory issues
*  and just make life easier for people in a way that slots in the technology, right? And then you
*  have a bunch of scaffolding to actually have it be better in various ways. And that's where we
*  promise it. I was talking to one of my friends, he's a lawyer, right? And his firm is encouraging
*  them to use their own internal customized, but very lightly customized, it's like some basic service,
*  lawyer GPT that they can use internally, but they can't just use the basic thing because of compliance
*  concerns, but also because they wouldn't necessarily know exactly what to do. But there's
*  enough annoying individual steps on it that he ends up just not bothering because by the time he
*  actually imported the proper case law and hooked up the proper documents, he could have just done it
*  by hand. So to offer the time, so he loses most of the utility from it. Most of the time he ends up
*  skipping it. It seems you personally could probably within a month code up something that would
*  supercharge this capability and probably increase the entire firm's production by 10%, maybe 50%.
*  Certainly if you have a small team. So, and then again, if you built it properly,
*  when GPT-5 comes out, you just switch the four to a five and the reference call back and your
*  product just gets better. So there's the alternative, but he can't use the, still can't use the
*  alternative and still doesn't know enough to like properly do the alternative. And then yeah, when
*  it properly integrates into your entire workflow and Google's buddy has fully automated into,
*  okay, now it has access to every document in the world automatically. You're still going to want
*  this kind of specialization and you're going to use the profits you made early on to do the
*  specialization thing. If you buy the hospital, you're going to be able to integrate into the
*  hospital's workflow. You're going to gain the trust and ability and education of these doctors.
*  You're going to make it easy on them because they are not tech people and they do not want to have
*  to think about it. And they want something that like feels right and safe and good to them. And
*  the regulators are breathing down your neck. And there are so many things like this where professionals
*  time is so incredibly valuable and getting the answers right a little bit more is so incredibly
*  valuable. But you don't have to be that much better in certain ways. Again, you can be 10
*  times better in the interface. You can be 10 times better in just the ease of onboarding and usage
*  and regulatory compliance. And then you have some scaffolding, but yeah, sure. You just
*  are doing whatever the last bottle is. That seems fine. I think there's plenty of things that like,
*  they're not future proofs you don't think you're pro, but like they're future proofs in terms of
*  if you're planning ahead to make it work. So you said you like the business model of the private
*  equity AI reboot for companies that don't realize they should be AI powered yet. Do you like venture
*  capital right now? Would you go, would you want to be an LP in a generic Silicon Valley venture
*  fund at the moment? Venture is a weird situation because your compensation as an LP in a venture
*  capital firm is not tied to your expected returns that highly. It's a question of,
*  look, if you offered me a big enough fund to go invest in companies and we set aside ethical
*  concerns for the moment with potentially advancing AI in the wrong ways, or we were confident we could
*  only choose companies we were confident were neutral or better or whatever it is,
*  and you gave me a big enough portfolio to work with and enough of a share of the profits,
*  then of course I'm excited. Do I expect VC to make money like above market returns?
*  I think that's a completely different question. And that is a, now we're talking price, right?
*  We're talking about whether or not there's too much money raising into AI, where there's not
*  enough money rising into AI. And then also the question of course of how much are the insiders
*  and the high reputation and well connected people just getting differential access and
*  positive selection and you're missing out on all the deals that are worth it. And so you just
*  left the drugs and unless you're like really good at picking up from the drugs, even if the industry
*  does well, you're going to lose. I'm currently advising Lionheart Ventures. We're trying to do a
*  safety positive fund for AI. And I think they're taking LP money if you want to invest in their
*  next fund. But that's more than talking about the industry, learn about the startups, learn about
*  what's going on. And partly you have to try and encourage the company to think we'll be better
*  in the world. It's not going to be about money. I don't have a very good share of it. But sure,
*  of course, if you have a bunch of money and it comes down to you get the good deals and is your
*  expected return high enough if you're considering investing or not. And that's very hard to tell
*  from the outside. My guess and are the valuations the same? Or maybe the valuations have an extra
*  zero on them they're not supposed to have at this point. Or maybe everyone's sleeping and they
*  should have an extra zero they don't have. And now those things are completely crazy.
*  My guess is if I get a portfolio that said I get to buy shares in SV on the stock exchange,
*  and SVUS was just a equal share of all venture capital investments made by anybody at Silicon
*  Valley. And it was trading at cost investment plus interest rate or something. I would put
*  a portion of my savings into SVUS. But that's not the question.
*  Well, that's a pretty good approximation of what I'm trying to ask. I think I would
*  probably put more into Big Tech than that. If you had $1 to put in SV, hypothetical SVUS,
*  and $1 to put in Big Tech US, which is whatever your companies.
*  Yeah, it is trading at cost of investment plus interest. And the existence of SVUS
*  didn't radically alter the valuation of all the companies, which it would.
*  If this traded, then all the valuation would probably go up 10x or something crazy.
*  We have various reasons to suspect this. But at current valuations in relative terms,
*  I think I'd be pretty excited for this small stock. And I think that the market would reflect
*  that if other people had similar market opportunities. That you'd be able to turn
*  around and sell it at a profit if it's good, but actual people wouldn't pay. And they would
*  have a both sides returns if you didn't have that. And you just got to hold to maturity as it were.
*  But I'm very happy with my portfolio of companies essentially is Big Tech investments that have
*  made me a ton of money. And everything else, which is like a wash. I made some money in
*  Versolar and I lost some money in Hasbro. It's all the emerging market stuff is all wash.
*  It's vaguely even except for a significant number of Big Tech companies that have just gotten
*  returns have been very good. And the Big Tech companies are increasing percent of my portfolio
*  because they don't rebalance. I guess I expect that trend to continue to summarize our
*  somewhat contrasting viewpoints. I'm seeing it being pretty hard to outrun the Big Tech
*  companies because they seem to be moving pretty fast and the returns to scale seem to be super
*  high. And it seems like a large majority from what I see seem to be playing this sort of
*  compensating for current weaknesses game and trying to get to market. And meanwhile,
*  the next generation of model is cooking if it's not already cooked. And the current one is free
*  in retail and not free at the API layer. And it seems like you more see friction and bureaucracy,
*  friction in the market, bureaucracy at the Big Tech companies, regulatory barriers such that you
*  think that while maybe everything I'm saying, I don't hear you like disputing any of it, but
*  you're more saying, yeah, that's maybe all true, but it probably still gets contained by these
*  other forces and leaves like a lot of opportunity for other smaller companies. I basically think
*  that the Big Tech companies just only have so much bandwidth that attention has to be focused
*  and critical for any given company of whatever size. And that leaves treasure everywhere.
*  There's just think about all the things you could do with current technology. If you had somebody
*  built the app for that, somebody built a really good, not just a GPT, but like a much broader
*  true context has gathered all the data is coordinating a bunch of stuff is a lot out,
*  like actually sat down with users, figured out what they actually cared about and so on. And it's
*  certainly something Google could have built. It's something that I mean, I know people couldn't
*  build, but they did because they're not doing so. They didn't even try and fail. They didn't even
*  try. Right. They did review that virtual employee in their keynote. What's your expectation for the
*  AI powered virtual employee? The first thing I noticed right away was like, is this thing in
*  all of the chats and reading all of the messages and the DMs and like all of your emails, like for
*  everyone on the team, they're talking to other people on the team. It looks like it is. And that
*  doesn't seem great for me. I don't necessarily want all of that stuff to be viewable by an AI
*  that people can query. That seems bizarre. People can start using Signal at work just separately
*  on their second phone. What's going to happen here? But to the extent that if that problem gets
*  solved, it seems really exciting to me that essentially you have this virtual employee.
*  Really what it is, it's just, it's a bot that scoops up all of the information from all of the
*  contacts in which you're okay with everybody having that contact ideally. And then it can
*  answer questions. It can help communicate. It can help mediate. It can pass things along.
*  It can, I'm especially excited for just things like you ask it, what has happened regarding X or
*  can you keep me posted if something happens with respect to Y or can you contact Cheryl in marketing
*  and have her evaluate which of these three things she wants, she places what priority on and get
*  back to me because I don't want to have to talk to her directly because she's really rude.
*  Or any number of things. It seems like it's the sky's limit on just you have this extra tool in
*  your toolbox that in practice is going to be incredibly valuable because it just knows all
*  the things and can do all the things and continuously monitor all the places. And just
*  not having to monitor as many feeds on a continuous basis by itself needs like a concept.
*  Do you have a sense for what the hourly rate should be for an employee like that?
*  They may or may not charge for it that way.
*  So it's always the question as a consultant, which hours are people paying? Which parts of
*  your experience are being built and which parts are not being built? But if you assume that when
*  we talk about what you're billing while it's being queried by a human, while it is performing a
*  specific task, but not while it's hovering up all the information in the background,
*  I assume a lot if it's good. But it's always the if it's good. If it's reliable, if you can count.
*  There's always that threshold effect to be in these situations. Is it good enough
*  that I trust it to do this task? Because if I wanted to check the marketing room and see
*  if marketing has any requests or proposals or craziness that I might have to respond to,
*  right? And the marketing channels are massive, my company, right? They're like 40 pages of stuff.
*  And I don't want to read that. So I have the area that junk. Now, can the I reliably alert me
*  when I actually have to pay attention such that I trust not to read the stuff? If it doesn't,
*  it's worth it. Right? But if it's good enough that I actually don't read it,
*  then suddenly, it's a godsend, even if it has to spam you with four pages out of the 40 per day,
*  just to make sure there's no false negatives. So the question is, can you get it reliable enough?
*  If I ask it to have to talk to share on marketing, would actually give an interface of share on
*  marketing and would fail briefly when it fails such that I can take over from it. It fails silently.
*  If it hallucinates weird stuff, gets me in trouble, that happens even a little bit,
*  I can't do it. But if we can get there, suddenly, it's incredibly valuable. I think it's a lot of
*  stuff like that, right? Or if it's just easy to use, right? It's like with my friend, the lawyer
*  and the case files, right? Like, if I can get it such that it's easier to have this thing checked,
*  and it's reliable enough, suddenly I win. But until then, I have nothing. But I think you see
*  a lot of this stuff where you have nothing until you have everything. And then once you have
*  everything, you have to learn to have it. And you have to get people to actually use it. So you've
*  got three things you have to do. So these things are hard. But it's Google. We'll get there. The
*  question is, how long will it take and which ways will we get there? But we'll get there.
*  Yeah. I think you're absolutely right to emphasize the importance of threshold effects.
*  It does seem like we're pretty close to tipping over a couple of big ones. And
*  it will be very interesting to see how that affects the broader world of employment.
*  What's your expectation for employment over, say, the next year? Do you think we hit a point where
*  we do start to see a real impact on either the positive side, like measurable productivity,
*  or on the potentially negative side? You could imagine a world in which people that are entering
*  the labor market are really struggling because entry-level developers just can't really beat
*  Devon or entry-level general purpose knowledge workers can't really compete super effectively
*  on an ROI basis with these AI assistant, AI virtual employees from the likes of Google.
*  What's your short-term expectation for that? So you have to obviously separate what's going
*  to happen in specific areas of employment, what's going to happen with employment more broadly,
*  either the sector of information, knowledge workers, or this overall employment. Overall
*  employment is just a question of how big the positive number is. Because as you make people
*  more productive, as you enable people to do more things, we are nowhere near the point where the
*  AI just starts doing the next marginal task that a human wasn't bothered to do before. And to me,
*  that's the question. If the AI takes 10% of the tasks in the world, or even 25% of the tasks,
*  well, every time that the new task that we were going to do, except for the time the human put
*  are off doing it from the AI. So we're wealthier. We have more productivity. We are richer than we
*  thought we were. We are able to commission more things and people will be in more demand, not
*  less demand. So that's great overall. Question of knowledge work. Specifically, I don't expect that
*  much diffusion that quickly. And that's why the private equity stuff, for example, is so important
*  slash potentially profitable. So specifically, we're starting to see a few industries where
*  people are hurting. Illustrators, translators, to some extent, junior coders, junior engineers.
*  Oh, I think the junior engineers are actually mostly a non-zero interest rate phenomenon
*  combined with a flaw in the tax bill. So I think we're seeing this problem where engineers can't
*  get work and everyone like, but it's not about AI. It's about the fact that you can no longer deduct
*  those expenses properly. And so every company doesn't have a huge cash set is just getting
*  boiled away by this and interest rates are higher. So you can't invest in the future as profitably.
*  And the combination of these two things is just hitting the market really hard because they're
*  happening at once. And hopefully we fix the stupid tax loophole reasonably soon and the anti-loophole
*  where you just get slammed for no good reason. And then the situation gets a lot better.
*  Because with programming, if you double the effectiveness of every programmer, or if you
*  double the effectiveness of every really good programmer, or plus 50% of every bad programmer
*  and made every person you can't put at all as good as really terrible programmers or something,
*  I think you just get a lot more programming. I think you just get a lot more demand. I'm
*  now much more capable of programming, which has taken me from definitely not doing any programming
*  to might want to do some programming, but it's not going to take someone else's job away.
*  It's just going to mean that we code more things. So I'm pretty optimistic about that aspect of
*  things because I've literally never been at a company where I would have thought where we
*  had engineers. And I was like, what will we even do if another engineer? We have all the engineers
*  we need. That is not a thing. It's always like we need more engineers. We need better engineers.
*  We need to prioritize. We're constantly triaging what has to be done today versus next week versus
*  next month because good coding is always incredibly valuable to any real company.
*  And I don't think we're anywhere near that changing.
*  So do you think we'll see on the positive side, like measurable productivity improvements in the
*  short term? So they say that the internet showed up everywhere, but the productivity is realistic.
*  Right? Like that. And we know that's bullshit, right? We know that the world is a much richer
*  place. People are much more productive in important senses because of the internet or because of
*  computers and technology. But the stats don't seem to say that. So I wouldn't be surprised
*  if the stats just act dumb. I don't know how else to put this and don't reflect the reality of
*  the situation. And also like coding is not that big a percentage of the economy, right? So like,
*  we know that certain even knowledge works of certain types broadly construed not the
*  big percentage of the economy. So I would say I don't expect that much in the shape of like
*  measurable productivity or economic growth to be apparent in 2024 or even 2025 necessarily
*  at current pace because I expect so low adoption even among the places where people could be
*  productive and people not adopting it properly and not getting the most out of what the systems can
*  do for a while while they come down. And also for a lot of the actual productivity not showing up
*  in statistics, including employees just hiding the fact that they're probably just productive,
*  like just searching off a lot because they can. Or alternatively, like doing better jobs
*  the same thing, but looking the same or like just various other techniques. We just have this long
*  history of statistics just not being good at this. But that's compared to like, what I expect to
*  happen in the immediate term, right? Like my five year, 10 year projection is for this to be very
*  noticeable, even in the relatively not interesting worlds. You talk to economists, they're like,
*  well, you know, it might add 1.5% to our total productivity over the next 10 years. If we have
*  a really optimistic scenario, people are in a crack. People just like, what are you smoking?
*  This is make no sense. That's just not a possible thing that could happen unless you like,
*  maybe if Oz AI, like, boomers got their daily to roll back, would you be three and a half?
*  Which I think would be the same. There are a few people are even, you know, almost no one ever
*  is the opposite. Yeah, no, we just use the current things we have, we just extend them in a way. And
*  I wonder how many of those economists would watch the presentations from this week,
*  and see those demos, rethink what they're saying, because what's always happened is they are always
*  trying to evaluate, okay, if we have exactly the things that we currently have, and nothing else
*  ever, what happens to the productivity stats? I think they're still off in order to, they're still
*  crazy. But they do have to notice when other things become actually possible, right? Like,
*  what would be the productivity boost just from a universal translator that actually works?
*  Be very concrete. Everybody have a phone now can get full real time continuous translation,
*  including tone of voice, including affects and associations, really good translation,
*  and boost the start of the translator, right? It's being said as if it was being spoken to you,
*  its original form, with only the minor part of the equivalent. And what does that do to productivity?
*  It's own, right? There's so many different things you could put in that slot. They're just huge,
*  on their own. So I'm very optimistic. Over time, I just don't want to get too ahead of ourselves.
*  So maybe another time we can talk about the possibility of a biotech revolution,
*  because that's another one where I see an interesting dynamic where it seems like
*  things could be about to get pretty crazy. But much in the way that these this new class of
*  weight loss drugs, maybe doesn't makes everybody a lot better off, or makes those people that are
*  taking it a lot better off may end up actually shrinking GDP in some ways, because there's like
*  a lot of expensive things that don't have to happen downstream. I could be very interested
*  to hear your take at some point on how that might play. Zero for a while, because of bureaucratic
*  and regulatory issues. And then 10 years from now, watch out. Is it to the point where you like,
*  change how you live or change like your risk, your personal cost benefit or risk analysis at all,
*  because you think there might be genuinely revolutionary advances in biomedicine for you?
*  I've already baked in that kind of thing, mostly. And I think mostly there's very little you can do
*  that you shouldn't be doing anyway. If you're a healthy person, you should try to stay healthy.
*  You should invest a lot in your health. And I don't think this changes that. And I don't think that
*  the flip side of that, of course, is the world could end in some sense, right? I'm 45 years old.
*  If I think that we're going to hit escape velocity and like all these designer drivers that make
*  everything great, but by the time I hit 60, like half the time, right, and like half the rest of
*  the time, obviously dead, like I'm not saying this is my model or anything. I'm just saying,
*  if you didn't believe that, then maybe you just don't care much about your long-term health,
*  because the death rate in that range is actually not that large. There's a lot of different ways
*  you can approach it. And humans are completely irrational about these things. But the actual
*  observed, or real preference for me is your health is valuable. You get good returns from being
*  healthy immediately, effectively. You don't need to add the longevity to it. And there are basically
*  no clashes between longevity and current health. They're actually like, well, I have to trade one
*  off the other. It's like, no, what's good is good for the most part. As far as we can tell,
*  as far as we can't tell, we just don't know anything. There's probably ways that you do
*  trade off, but like we just don't smart enough to know about that stuff. So yeah, I'm putting
*  reasonable amounts of investment into me, my health. I do think that it would be dumb with this kind
*  of revolution potentially on the horizon to skydive, like to take known like large risks of being
*  literal. But like clearly, like you will not be safe. Right. Like you're if you roll a natural one,
*  like we can't help you. Okay. Well, we can dig deeper into that on another occasion.
*  Got to address the departures from the safety team at OpenAI this week. I think everybody
*  probably has heard the news. Daniel Catalto, I'm not sure if I'm saying that quite right, but he
*  left a couple weeks ago now and has been posting some cryptic stuff online saying that he declined,
*  like left his equity on the table, which would have been a large majority of his personal net
*  worth because he wants to retain the right to criticize the company. But we haven't actually
*  heard what those criticisms are. Now, obviously we've got Ilya is out with a pretty conciliatory
*  message saying he thinks everything's in good hands and they're going to build safe HGI.
*  And then Jan, who was his co-lead on the super alignment team without such a message, simply
*  saying I resigned and leaving us guessing. It's obviously not good. What more can you
*  say about it beyond its obvious not goodness? I've been writing up the article this morning
*  for this that I'll probably post next week. I have eight safety researchers in the last six months
*  who have left one way or the other. In addition to Ilya and Jan and Daniel, we have Leopold and
*  Pavel who were fired for leaking confidential information supposedly. What little we know about
*  this, it's hard to tell because when you leave confidential information, the last thing they want
*  to do is tell everybody about all the confidential information. You just leaked through the serious
*  because like obviously that's self-defeating, but it looked a lot like they technically leave
*  confidential information that was used to fire them. But like from the outside, we can't tell.
*  We also lost William Saunders, Colin O'Keefe and Ryan Lowe. So that is, I don't know exactly how
*  many people would count as line that are safety researchers under this criteria, but it feels
*  like a lot, right? We also did lose Diane Yoon, Chris Clark, and then Morkawa. We don't aren't
*  obviously safety related, but I don't know what's going on guys. Sherry Lachman, head of social
*  impact has gone. It doesn't feel like the kind of pattern of people you were losing when you're
*  like being a socially responsible safety first company, right? It feels like a company loses
*  these people when a lot of people were very dismayed in some fashion. And yeah, obviously
*  we have the messages that are being sent and not sent. We have the fact that people are
*  almost certainly universally under NDA. We have the fact that like Daniel gives us very strong
*  evidence that non-discouragement clauses are in place basically everywhere, unless you are going
*  to pay an extreme financial price to not do so. And even then you're still under NDA. So it's
*  probably going to Daniel is that he's reserving the right to prioritize them in the future,
*  but the NDA probably severely constrains his ability to reveal the information that would be
*  useful right now. And he's made a very reasonable decision not to break the NDA.
*  So he did say one thing, which was his reason for resigning was loss of confidence that
*  the company OpenAI would act responsibly around the time of AGI. That's almost a verbatim quote,
*  probably not quite exact. How would you, the NDA thing seems weird to me, to be honest. I'm like,
*  if you really believe that and you are willing to leave that much money on the table to be able to
*  make some criticisms, what's the NDA doing here? It doesn't seem like they could really sue you
*  super effectively. They maybe could, but like the Streisand effect, you're talking about
*  self-defeating, right? Like suing your safety, departed safety person only increases the attention,
*  the media circus, whatever to what they're saying. You might not want to appropriate certain
*  technology or certain technological information. There might be a throw-hazard involved.
*  Yeah, it seems like you can kind of separate that, right? It wouldn't be like the mere existence or
*  the discovery of something that would lead to a loss of confidence. There's got to be something
*  social about that, right? The public is primed for it when it comes to, Sam Maltman was just the
*  subject of a lot of drama. There's definitely smoke here. It seems like-
*  I think that's the obvious. My experience with this type of thing is that if they were to reveal
*  some esoteric detailed reasons why they were concerned and it was technically leaking
*  confidential information that you were indicted for, probably you don't necessarily get sued for
*  that, although you might, but also like it could make your life pretty miserable and it could take
*  away your flexibility to do other things in the future. But the baseline scenario here is there's
*  simply a toxic environment inside open AI for people who care about safety and safety, right?
*  That it's now transformed into a move fast and bring things, startup fatality and that they are
*  inherently vicious after everything that happened of anybody with associations with like that's
*  wrong or the alignment form or the A or safety of any kind and that they're making their lives
*  miserable in various ways and that politically Altman wants all those people gone. And so it's
*  steadily taking every incremental opportunity to get those people gone and that as those people
*  leave, more of them are now more isolated and under more pressure to leave. And if you were to
*  spell all this out, you'd be breaking your NDA and potentially making yourself vulnerable.
*  And in general, these are like Sam Altman is representing reasonably well that you can be a
*  negative person, right? That he might come after you if you personally, if these are personal
*  issues and political internal issues that you like spread their dirty laundry and you launch
*  these kinds of attacks. I don't think it's unrealistic that you get sued for it. Like,
*  start-end effect be damned. I think that I've dealt with these people and a lot of these people
*  absolutely sacrifice the start-end effect in the short term to credibly be the type of agent that
*  will retaliate. It's rational. It's highly rational, highly correct from a decision theory standpoint
*  to be willing to come down very hard on somebody in this situation who attacks you,
*  right? The counterpuncher. If you are trying to be a modern leader of a company in these situations
*  where there's a lot of secrets, there's a lot of dirty laundry, because there have to be, even if
*  you're doing everything right, even if no one's doing anything malicious and everyone's trying
*  their best and everything's basically fine, there's still a bunch of stuff that you wouldn't want aired
*  to the public. And yeah, you credibly threaten that you are going to enforce these things.
*  The equal extent of the law, you're going to make people's lives miserable. You're probably going to
*  do other things to make their lives socially worse in various ways. Try to blackball them in their
*  future jobs and opportunities and blah, blah, blah. And Sam Altman knows a lot of the VCs. He knows a
*  lot of the people who determine whether or not your startup goes well or badly, whether you can
*  get various different spots. I don't think being worried about these things is unreasonable. I do
*  think that we can be confident that there isn't an imminent, the world is about to end because of
*  opening-eyed technology that's motivating these partners, because then they wouldn't be talking.
*  If it was like, no, seriously, they broke Q-Star and they hooked it up with GVD-5 and now this
*  thing is clearly on the verge of breaking out on the internet, we're very worried about it,
*  or some crazy scenario that's clearly not happening, what's very clearly not happening,
*  then I think these people would be willing to talk if only to whistleblowers to a government
*  committee or something. They'd be talking. And I think potentially they're talking to people
*  who are not public. If you had serious problems with really deep wrongdoing, would you go public
*  with your concerns or would you call the government? It's not obvious to me that one approach has been
*  on the other. But again, the default explanation for all of this is that the environment at OpenAI
*  became toxic as a result of the events that happened, regardless of the extent to which
*  Sam Altman directly caused that to happen or intentionally wanted that to happen.
*  And as a result of that, and also a lot of people were effectively his political enemies and now
*  they're gone. And if you see someone doing that, systematically getting rid of very people in the
*  safety departments, maybe you leave. Daniel lost faith in OpenAI's ability to navigate the future
*  AGI role responsibly and left. It wasn't too long after they fired Lee Abolt and Cavell.
*  One obvious explanation is that he knew that he thought those firings were bullshit and that he
*  saw that they were cleaning houses, taking people and shoving safety people inside and working
*  away from them. And therefore he lost faith in their ability to be responsible. It doesn't require
*  there to be a big mystery here. Right? But the obvious explanation is that OpenAI is just not
*  a place that is currently very receptive to something that I think will be very vital to
*  making sure the future goes well. And that's deeply troubling.
*  So any parting advice for either the departed folks from OpenAI or there's been talk also of
*  compensating folks like Daniel for leaving his stock on the table to try to encourage others
*  to do that or to set some sort of a precedent. I guess any like, what should we want in the short
*  term? I would agree with you. There's probably not like a super emergency or they probably would
*  just be throwing all caution to the wind. But what do you think they should be wanting and
*  what should they be doing to get it? And what can others be helping that?
*  Obviously it depends on what the underlying situation is. Obviously they should take their
*  concerns forward no matter what else they've done. And if they can't do that, then that's like
*  horrible. They should be, if there are things that justify whistleblowing to governments behind the
*  scenes in ways that they're protecting the support, they should do that. I think the
*  difference between disparagement and breaking your NDA, obviously you think about these things
*  very differently. I do think it would be good to consider compensating Daniel or others who have
*  given up their equity in order to not find non-disparagement clauses. But I do worry
*  especially about paying for NDA breaches, about the secondary incentive problem.
*  If you know that people who are working on safety will feel free to violate their NDAs because this
*  ecosystem will compensate them for doing so, then maybe you just can't hire anybody in the ecosystem
*  at all. Maybe you can't hire anybody who cares about safety because you're worried they will
*  steal your secrets and giving you economically valuable secrets and therefore you can't do it.
*  I think you should think very carefully about what you are and aren't going to compensate to what
*  extent and not just blow your one card. I believe in freedom of contract. These people knew what
*  they were signing and they knew what they were agreeing to. It doesn't mean that it's
*  sacrosanct. It doesn't mean it's fully sacrosanct. It doesn't mean that there aren't circumstances
*  where you should break the NDA and there aren't circumstances where you should go to
*  protect the people who do break the NDA. But I think those bars are high. Also, obviously,
*  I am a journalist now as are you to some extent. Anyone wants to break news,
*  if any level of confidentiality and privacy, my DMs are open.
*  Well, that might be a good note to leave it on. I'll look forward to your full analysis on this
*  topic next week. It's always great to break it down with you. Any other closing thoughts?
*  We don't know much about this in particular and about many of the demos and other things
*  that we've learned about in general. We're speculating. We're trying to process a lot
*  of information very quickly. I don't think we know what's going on. To be clear, this could all
*  be as simple as events like the vacation people's mouths. They want us to fresh start.
*  The environment is somewhat hostile philosophically to what they're doing and they're
*  just not having fun anymore in some sense. And then that fact makes people lose confidence.
*  Maybe it's that simple. Maybe it's all kind of coincidence. We don't know. It's just,
*  yeah, I don't believe coincidence.
*  Cool. Well, we'll keep following it in our respective formats. So thank you for taking
*  the time today. Enjoy the conversation as always. And Sv Moshvitz, thank you for being part of the
*  cognitive revolution. Absolutely. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.
