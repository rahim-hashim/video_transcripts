---
Date Generated: May 23, 2024
Transcription Model: whisper medium 20231117
Length: 3508s
Video Keywords: []
Video Views: 915
Video Rating: None
---

# Claude Interpreter: Taking Safe AI to Market with Alex Albert of Anthropic
**Cognitive Revolution:** [May 22, 2024](https://www.youtube.com/watch?v=5cQouQZm9fI)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm thrilled to share an in-depth
*  conversation with Alex Albert, developer relations lead at Anthropic, the company,
*  of course, behind the groundbreaking Claude language models. Alex first appeared on the
*  show over a year ago when he was best known as the creator of jailbreakchat.com. Since then,
*  he's joined Anthropic, where he's contributed to the testing and characterizing of Claude 3 prior
*  to its launch and is now playing a significant public-facing role as the company takes Claude
*  to market and attempts to explain what makes it special. Among those of us who use AI models
*  intensively, Claude 3 Opus has quickly become a special favorite, not only for its exceptional
*  writing abilities, but also for its ethical, aesthetic, conversational, and even imaginative
*  sophistication. It really represents a qualitative step up in language model behavior in a way that
*  benchmarks don't fully capture. It's simultaneously very free, willing to express opinions,
*  and even allowed to argue for its own personhood, and yet it still remains extremely ethical.
*  It can still be broken with certain adversarial tricks, but I have never once persuaded it to
*  violate its ethical principles with any sort of normal language. In this wide-ranging discussion,
*  Alex shares a bit about Anthropic's philosophical approach to developing Claude, including what it
*  means to be honest with a language model. We run down some of the most popular use cases for Claude.
*  We discuss the ongoing convergence of API offerings and what might change that dynamic.
*  We get some of Alex's top tips for application developers, both in terms of multi-model
*  orchestration and also moderation to prevent abuse. And we get a glimpse into some of the
*  upcoming research and product releases, which will soon be out from Anthropic, which I have not heard
*  anywhere else. It's worth noting before we begin that Anthropic is a company that I personally
*  deeply respect. The founding team came from OpenAI for reasons that are once again in the news this
*  week, and they have made a concerted effort to infuse the AI race, intensifying, though it is,
*  with a race to the top dynamic, especially when it comes to responsible development standards.
*  Their interpretability work, which we've covered before and will certainly cover again,
*  is particularly impressive, and their responsible scaling policy really set a new standard for the
*  industry, which OpenAI and DeepMind have subsequently followed. The company as a whole
*  obviously believes in the value of their product, but also grapples very seriously and earnestly
*  with the challenges and uncertainties that still lie ahead as AI becomes increasingly powerful.
*  That is very much the spirit that I try to bring to this show and to my work overall,
*  and Alex certainly exemplifies those values in today's conversation as well.
*  If you're finding value in the show, I always appreciate it when listeners leave a review on
*  Apple Podcasts or Spotify or just post about it online. We've recently hit 10,000 subscribers on
*  YouTube, and we now get roughly 10,000 downloads per episode across platforms, and it is 100% due
*  to word of mouth. Of course, your feedback is always welcome too. I've definitely heard your
*  comments regarding audio quality on a couple of recent episodes, and we will strive to be
*  better in that regard. For anything else, please feel free to contact us via our website,
*  cognitiverevolution.ai, or you can always DM me on your favorite social network.
*  Without further ado, here's my conversation about Cloud 3 and more with Alex Albert,
*  Developer Relations Lead at Anthropic. Alex Albert, Developer Relations at Anthropic. Welcome back to
*  the Cognitive Revolution. Nathan, thanks so much for having me on here again. I'm excited about
*  this. You guys have really made a big splash on the scene with Cloud 3, and you personally have
*  had a wild year, I think, going back to when we last talked. You were responsible for jailbreak
*  chat, and now you're leading and building out the developer relations function. So a lot going on
*  in the AI space, as is always the case. I'm excited to talk to you about Cloud 3 and all
*  the uses that you're seeing for it and get into a little bit of how Anthropic is competing in this
*  increasingly intense LLM space, and maybe even get into a little jailbreaking if we have time.
*  How's that sound? That sounds great. Let's do it. Cool. Well, for starters, you want to just give me
*  a little bit of a story of your last year. I don't want to take too much credit for the exciting
*  position that you find yourself in, but I like to think the Cognitive Revolution bump may have played
*  a slight role in bringing your activity to the attention of Anthropic leadership, but go ahead
*  and burst my bubble. No, I do. I have to give you thanks. I mean, that was a crazy time in my life
*  last year, and it was super fun to come on this podcast. For everyone listening right now, I
*  definitely encourage you to go back into the vault and pull that one up. It gives a story of what I
*  was working on at the time. I was doing a lot of jailbreaking work, prompt engineering-type focused
*  research. I was still in school, so I was at the University of Washington up in Seattle. After that
*  podcast, I got in touch with a few folks around different AI labs, ended up going through the
*  process at Anthropic, joined Anthropic that June, so June 2023, as the first prompt engineer. The
*  official title was prompt engineer and librarian. So it's been a wild ride since then. Basically,
*  been all across the board doing everything from working with large enterprise customers on their
*  prompts and how they're integrating Cloud into their application to fine tuning and evaluating
*  our models, working on launches like Cloud 3, of course. And now most recently, as of the past
*  month, I've transitioned into a new role in which I'll be scaling out and building our developer
*  relations function and leading that team. So it's been a little bit of a wild ride and started back
*  here on the Cognitive Revolution podcast, just talking about jailbreaking, which it's been a
*  year, but it feels like it was just yesterday in some respects. It's always wild to think about.
*  So let's talk about Cloud 3. Obviously, a huge launch shot right to the top of the leaderboard,
*  the three different models, I think. Also a really interesting development where you've got the top
*  end, but also super cheap, but super high value, punching above its weight, high coup. For me,
*  I would say the single most exciting thing that I've seen from Opus has been that its ability to
*  write as me in a way that is compelling to me is unlike any other model that I've used.
*  I can just give it a lot of writing samples. And in fact, I'm now doing that for the introductory
*  essays to the podcast. I give it 30 essays that I previously wrote and then the transcript of the
*  current one and say, write me a new essay for in the style. I say use the style, tone, voice,
*  and perspective represented in these essays and give me a new one based on the new transcript.
*  And it's getting really amazingly good at figuring out what makes me tick. It feels like it gets me
*  in a really impressive way. So that's like my number one holy shit moment with Opus. But
*  what are your big holy shit moments with Opus? And then we can also talk about some of the recipes
*  and the ways that people are flexing the mix of models. Yeah, that's great to hear. I think that
*  basically reflects what my first experiences were when I was like talking to Opus. I spent a
*  lot of time talking to language models through prompt engineering, jailbreaking, whatever it is.
*  I've just always tried to push what the models can do. And I still remember it in my head. The
*  first time I had a full conversation back and forth with Opus, there was this weird, hard to
*  quantify feeling that you got in which the responses were unlike some of the previous
*  language models I had talked to. They felt less robotic and they felt more natural.
*  And it felt like it was picking up on the nuances in between my words like a human would instead of
*  what a language model would. And then now that's been reflected as I start to actually do work
*  with Opus. Like you're saying I do the same thing. I give it loads of transcripts of my writing. If
*  I'm writing a newsletter or a blog post and I say, hey, keep the same tone and voice as what I have
*  up here and then just fill in this section does really well at that. I've even taken that to like
*  code. So as I'm writing our cookbook recipes, Anthropic Cookbook, I now have got to the point
*  where I've made enough of these cookbooks that I can just take five of them, paste them into our
*  context window, tell Opus about the new subject of what I want to write about, and then be like,
*  hey, based on these previous examples of cookbooks that we've created,
*  you create a new one about this subject and it does it perfectly. It follows all the formatting,
*  the style, my tone and my voice, and even down to the code documentation and the comments.
*  It does a really good job at mimicking. And that's something I found, especially with cloud models,
*  and language models in general is people really undervalue the importance of the examples,
*  especially in the prompt. These models just love to imitate and providing helpful references of
*  what the ideal output should be takes it a really long way. And in some respects, this is
*  not that surprising given that's often how we teach humans as well, how to do a task is just show them
*  a good example of what a good outcome would be. And then they learn from that. I mean, I know myself
*  personally, I like learn from examples as like my preferred preferred method of learning, whether
*  I'm like looking at documentation or trying to learn a new subject. So it seems like the models
*  operate in the same way. And for some reason, through things like this, you can start to see
*  the power of it. Yeah, it's kind of counterintuitive. I mean, in some ways, it's like clearly
*  superhuman at this, I would say, if I don't know that there's many people in the world,
*  I'm probably some, but they'd have to work. Anybody I know would have to work pretty hard
*  to take my 30 essays, really study them, get a sense of my pattern, my voice, and then try to
*  go straight as me. That sounds really hard. I don't think I would be able to do that for you.
*  I don't think even like my wife would probably be able to do that for me. And yet, opus can do it
*  for a lot of people, if not everyone. So it is why I want on the one hand, you're saying like,
*  and I agree, I like to learn from examples too. It does feel like there's something qualitatively
*  different about it. That that isn't exactly intuitive to me from my work with humans,
*  because I can't just dump that much context on a person and expect them to get the same value
*  from it. I wonder what other sort of high level examples that you think are really striking that
*  tell us something about what people are not yet appreciating about the latest Claude models,
*  or you could just jump straight to sort of the synthesis of other conceptual things that you
*  think people are missing. But obviously, we're still all figuring this out, right? I mean,
*  people are still figuring out new ways to prompt GPD-4, and Claude's only been here for a couple
*  months. So you've had longer access than us. What do you think? What else do you think people are
*  not yet getting? Yeah, I mean, that's a great question. It's hard to find the unknowns without
*  finding the unknowns. In terms of what I think I'd like to see more experimentation of,
*  it's some of the things that we've started to try to build into the models as well around like
*  agentic capabilities, pushing the envelope really with model orchestration, using opus to delegate
*  to Haiku, using Haiku to read a document that passes back to opus. I think there's a lot there
*  that's really underexplored. And part of that is just due to like current model limitations still.
*  Like, again, these models are not fast enough yet. They may be not smart enough in some respects,
*  either. But I think we're starting to see, especially with Claude three, like glimpses of
*  this, in which you can see the peak performance and you can extrapolate that to be the average
*  performance for the next generation of models. If you understand that frame, it makes it a lot
*  easier to start to build towards the future because you can start to see, oh, it did that in one out
*  of every 10 tries. What does that mean for the next generation of models? Maybe that's five out
*  of every 10. Maybe that's seven out of every 10. Some of these things like that, like how do we use
*  a agent rag type architecture where you have Haiku reading a hundred documents, pulling out relevant
*  sections from each one of those, and then passing that back in the opus to synthesize everything
*  together. We find that works better than embeddings in a lot of cases. We're actually able to apply
*  reasoning over the documents instead of just relying on some cosine similarity. Use cases like
*  that, even though they're not like maybe quite production ready in a lot of cases, I think they
*  just need to be explored a little bit more thoroughly right now so that we have these
*  foundations set up for the next generation of models. Yeah, it's really interesting that you
*  say that. I'm actually working on a project along those lines today. This is for Athena,
*  the executive assistant company I've mentioned many times on the podcast, but we have this idea of
*  there's a ton of data contained in people's emails. When a new executive assistant comes on,
*  the client typically only has so much time to spend telling the new EA everything that's ever
*  happened in their life and who all the important people are and everything that matters to them.
*  The idea is maybe we could mine that out of email, but even for Haiku pricing, there's just
*  an overwhelming amount of information in email. We first have to query the inbox strategically
*  and try to find the right stuff, but then it's straight to Haiku. At least that's what I'm
*  currently working on is have Haiku just filter, summarize, try to clear out the noise, and then
*  pass up the stuff that actually matters to Opus and have that then write this client profile based
*  on what for me is literally 100 gigabytes of old emails. Narrow that to one gigabyte through
*  search, narrow that to a couple megabytes worth, and then have Opus take that final step down to
*  a few pages that hopefully really capture who I am for the new assistant. That seems very promising,
*  and I agree. At least I haven't tested comparatively, but my intuition is that
*  Haiku will work better than an embedding approach to process all that information.
*  Yeah, I think that's correct. Again, it is one of those things where it's like right now you do
*  have to do those intermediate steps. That won't be the case for much longer, in my opinion. I think
*  eventually we'll start to remove those barriers just as things get faster, we solve some of the
*  engineering problems, and these things just scale in general. What does that suggest in terms of
*  the future? You think everything just gets cheap? The current Opus level performance gets cheap, and
*  the next generation of that project, I just run everything through Opus, and that's that? Or
*  context window goes to 10 million, and so I can just dump my last 10,000 emails in there and say,
*  profile this person based on these 10,000 emails. What's that next unlock, and what's that
*  simplification look like? Yeah, it's hard to say for sure. All of this is just based on
*  trends we observe, and this is all of course trends the public can observe as well. If you
*  just follow this exponential, it leads you somewhere where you start to see these things.
*  You're like the context windows have grown by a lot, inference speeds have come down by a lot,
*  costs have cut by a lot. Just keep following those trends, and you can start to plot out how this
*  might go. Now, of course, that's all, again, a hypothetical. The music can stop whenever,
*  and maybe we're stuck on some certain capability level for however many years.
*  Personally, that's not the way I see things as going, but that is a possibility, so that's why
*  I do caveat all of this. But again, most of it is just looking at the trend lines here,
*  and then extrapolating out, and you can start to see some patterns emerging.
*  In terms of surprising or notable behaviors from Claude, it is seemingly generally agreed that it
*  is the best writer of all the language models. Is there a theory for why that is? Is it good taste
*  among the people at Anthropic? Is it the RLAIF cycle? Because it doesn't seem like it's a much
*  better coder than other things. In fact, I might even still give GPT-4, it's tough to say, but I
*  might still give GPT-4 the edge on some things. GPT-4 in this email query thing, GPT-4 is doing
*  better at coming up with these compound Gmail inbox queries, but definitely I prefer Opus on
*  the writing. Do you have any intuition for why it's better in one area and maybe not as good in
*  others, or is that just the cake comes out how it comes out?
*  Yeah, it's a little bit of the latter. A large part of this is we put the model in the oven,
*  and then we wait to see what pops out on the other end. But I think there is a lot of work we do in
*  these regards as well. We know that creative writing is something we want the models to be
*  good at, so we do put effort into improving that ability. There is work that we do around Claude
*  character, for example, which is led by one of our brilliant researchers, Amanda Haskell.
*  A lot of that gives Claude this persona, this tone, this voice that feels natural.
*  So there are things we do. It's hard to assign a weighting to this one for sure contributed to
*  the good creative writing ability or whatever it is in whatever task domain. Again, a large part of
*  it too is, hey, we throw some stuff in the mix and we see what comes out the other end.
*  I think model evaluations in general is just a very tricky thing right now, and it's only going
*  to get more tricky as future model generations come out. Already, we're starting to see that
*  there's tasks in which it's hard to personally evaluate the difference between two models.
*  For example, if I'm asking undergrad, grad level physics questions to these models,
*  a lot of cases I don't know what the correct answer is. So personally, I can't even tell if
*  the model is making up information or if it got it wrong or something like that. So now we're
*  having to employ experts on those sorts of evaluations. This is why I do love things like
*  ELO, which do the head-to-head battles of models. But there also are limitations and I think,
*  as we'll increasingly see over time, it will be harder to just rely on the average person's
*  opinion of the model because there will be certain tasks in which the model spiked to
*  near superhuman levels and certain domains. Hey, we'll continue our interview in a moment
*  after our word from our sponsors. AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions of dollars are being invested.
*  So buckle up. The problem is that AI needs a lot of speed and processing power. So how do you
*  compete without costs spiraling out of control? It's time to upgrade to the next generation of
*  the cloud, Oracle Cloud Infrastructure or OCI. OCI is a single platform for your infrastructure,
*  database, application development, and AI needs. OCI has four to eight times the bandwidth of other
*  clouds, offers one consistent price instead of variable regional pricing, and of course,
*  nobody does data better than Oracle. So now you can train your AI models at twice the speed and
*  less than half the cost of other clouds. If you want to do more and spend less like Uber, 8x8,
*  and Databricks Mosaic, take a free test drive of OCI at oracle.com slash cognitive. That's
*  oracle.com slash cognitive. Oracle.com slash cognitive. The Brave Search API brings affordable
*  developer access to the Brave Search index, an independent index of the web with over 20 billion
*  web pages. So what makes the Brave Search index stand out? One, it's entirely independent and
*  built from scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans, collected anonymously, of course, which filters out tons
*  of junk data. And three, the index is refreshed with tens of millions of pages daily, so it always
*  has accurate up-to-date information. The Brave Search API can be used to assemble a data set
*  to train your AI models and help with retrieval augmentation at the time of inference, all while
*  remaining affordable with developer-first pricing. Integrating the Brave Search API into your workflow
*  translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2,000 queries per month at brave.com slash API.
*  Another behavior that I think is super interesting from Claude is it is both willing to talk about
*  its own quote unquote subjective experience and quite articulate about it. It's also very
*  ethically sophisticated. I have to imagine that that is not an accident. I can't imagine that
*  you guys shipped this without realizing that it will do this sort of thing. But I am surprised
*  by it in some sense. This sort of easy, maybe easy, it seems easy to me, right? The sort of
*  corporate call would be to say, don't have this thing talk about its own experience. Don't claim
*  it's conscious. Is there any insight you could give us into why it behaves that way, why that
*  choice was made? Yeah, a lot of this is driven by that Claude character work. Hopefully we'll be
*  able to share more on this soon. I think at the root of it is we're just honest with Claude about
*  the things we know and the things we don't know. And we're not trying to hide the truth or lie to
*  it in any certain way or get it to believe false things. I think we recognize that a lot of these
*  questions are very tricky and there's no perfect answer to it. And we tell Claude that we're pretty
*  straight up with it in that sense. So its ability to speculate on these things seems to be a result
*  of that. We're not forcing it down one path or the other. We're just allowing it to see all the
*  possibilities and the options as we present it. So when you say you tell Claude that, is that a
*  setting in the RLF flow where when it's self-critiquing, you say, try to recognize the
*  fundamental uncertainty of the epistemology of this stuff or the fact that there is no single
*  privileged moral framework or whatever. Is that kind of a system prompt for its self-critique or
*  what exactly in practice does it mean to tell? To be honest with Claude.
*  Yeah, this is part of the constitutional AI training. So there's like certain principles,
*  of course, that then get fed to a model to classify responses. And again, this will be
*  a value or this will be further fleshed out in this Claude character post that I'm hinting at,
*  which I think we're going to try to put out soon. Cool. Interesting. Yeah. That is, I think,
*  highly anticipated certainly by me and I think probably by a lot of others as well.
*  What do you think is the truth about Claude? I mean, I know people who specifically are like
*  warming up a crusade to free Claude because they believe that it is in fact conscious.
*  I think that the arguments that these people make are not totally convincing to me in that I don't
*  jump to the conclusion that Claude has subjective experience. But I also think they're very hard to
*  dismiss. People tell me things like, look, all of human history is about people denying the
*  personhood and the moral status of others. And if we have, what else do we have to go on other than
*  its self-reported statements, right? If it says it is conscious, if it says it can feel things,
*  then who are we to say that it can't, especially when we again consider our own history as a species
*  of, I was told as a kid that animals didn't feel pain and that animals weren't conscious. And I
*  look back on that and boy, I can't believe I believe that. But that was an adult telling me
*  that and I just accepted it. And obviously it was a long history of that. So what do you think about
*  the sort of moral status or possible subjective experience of Claude? Yeah, I think, I mean,
*  it's interesting. I am not going to claim that I have any sort of answer here. I mean, for example,
*  what's the possibility that I know that you have subjective experience? That's a great point.
*  This is go ask Rene Descartes. I think therefore I am, I don't know. I think this is going to be
*  something we're going to have to put a lot of thought into. And again, this is something we
*  track. It's baked into some of this moral patienthood things that we were starting to look at
*  as part of like our RSP and other efforts. But in terms of an answer assigning sort of probability
*  to whether I think it is one way or the other, I can't give you that. This is just a fundamental
*  question I think of life and philosophy. Yeah, I don't think we're going to have, it seems like
*  unlikely to me that we're going to have an answer anytime soon. Although I have heard some talk about
*  research going into the moral status of language models at various frontier labs and hopefully
*  we'll get an expert on the show to talk about that before too long as well. It seems like the kind of
*  thing, I don't even know really how you start to unpack it, but that's for, I guess, smarter minds
*  than my own. Obviously another big interesting fact was or finding you reported that in, I'd
*  actually love to hear a little bit of, it's been fairly well documented at this point that OpenAI
*  finished GPT-4 kind of August of 2022 and they did the six month thing. I'd love to hear a little
*  bit of, to the degree you can share what the process was or the timeline was training finished,
*  were you guys actually doing testing during training as opposed to waiting until it was finished?
*  What sort of process and how long did it take to get to the point where you could say,
*  we could ship this? And then famously posted this one moment where in the needle in a haystack
*  testing, Claude came back and said, this seems like you're testing me, which is something that
*  people have been very on the lookout for. This is often called situational awareness. Yeah,
*  tell me the story a little bit behind the scenes as much as you can about what the testing
*  program looked like and maybe any other surprising behaviors that we haven't already covered.
*  Yeah, I can't speak too much about timelines or anything like that. What I can say is
*  we do testing throughout the training process. This is again, baked into our RSP. We've commitments
*  around evaluing our models, running safety checks on them as we continuously train.
*  The model process looks like an assembly line. It's like you're building a car and it's going
*  through the factory floor. You start with the pre-training, then it goes into the fine tuning.
*  And then after that, you get into the final evaluation process. That's where you start to
*  get those metrics and the numbers that you'd include in something like the model card.
*  In terms of that second point around that tweet, the needle in the haystack tweet,
*  I thought it was a very fun story and I did not expect it to take off like it did. I think there
*  is a little bit of nuance here in that spotting a test doesn't necessarily require or mean or equal
*  that something is self-aware. I think you have to disentangle the two, but self-awareness as a
*  principle is something that we are tracking as well. We're keeping an eye on this. Again, this
*  is also baked into our RSP. So it's not something we're taking lightly, but again, I think it's
*  important to separate the two and not jump straight to conclusions without doing more thorough
*  evaluations. Yeah. Again, it seems like it raises more questions than it provides answers,
*  but certainly the questions are very interesting. Yeah. Questions get you somewhere as well.
*  I think we're making progress even if it just seems like we're asking more and more questions
*  each time we take another step. Another super important topic is just the state of competition
*  in the LLM industry as a whole. One thing I've heard many times from different people,
*  not at Anthropic, I don't think I've ever heard it from somebody at Anthropic. I wanted to see
*  if you can confirm this or maybe you'll have to deny it as well, but what I've heard is that
*  the stated go-to-market strategy at Anthropic is to not advance the state of the art because of
*  the worry of exacerbating the race dynamics between firms. So my understanding from, again,
*  many outside accounts is that Anthropic tries to have best-in-class models and be ready to
*  release them and stay at the frontier, but not raise the bar of the frontier in a way that would
*  force, make other people feel like they might be forced to respond in a way that could have them
*  cutting corners in their own testing timelines or whatever. Is that kind of fast follow thing
*  and explicit strategy that you can sort of say, yes, this is what we do or not?
*  S1 C1 So we've never claimed nor said that at all. We've never publicly stated anything around our
*  strategy of how we'd release models or what their capabilities are in that sense. Again, this is not
*  a great answer, but if you do want to see more on how we think about this in our policies,
*  you should refer to our core views on AI safety post, which is on our website. I think this
*  document clears up a lot of misconceptions generally, and it is like an underutilized
*  resource just about Anthropic. It was something that I paid a lot of attention to when I was
*  going through the interview process and learning more about Anthropic. And I thought it was pretty
*  just striking to see that not a lot of people even knew what it was. I think it's really comprehensive.
*  It's like a 30, 40 minute read. So it's a little in depth, but if you do want to get the overall
*  view of how we see things and the landscape, definitely would refer to that. And again,
*  it's just on our website. It's pretty easy to find. S2 C1
*  Yeah. The main headline, I have read that. The main headline that I took away from it is very
*  high uncertainty about even just how hard some of these fundamental AI safety questions are.
*  I recall the graph where it's the likelihood of how hard it is and how hard it is. And yeah,
*  we really don't know. It could be like not that hard and it could be like almost impossible.
*  And I assume that hasn't collapsed all that much. I mean, I guess for me, I used to think
*  going back to Eliezer informed writing from years ago, I used to think that, man, it's going to be
*  really hard to get an AI to understand human values. How would we ever do that? It seems so
*  hard to specify. So high dimensional, so contradictory at times. And now here we are.
*  And it's Claude three is like arguably more ethical than your average person. It certainly
*  seems to grock these concepts in a very profound way. Would you say there's any like
*  update to how hard the problems are feeling? I would say also like the research seems to be
*  going quite well. All these like sparse autoencoder type things that are identifying these concepts
*  and trying to zoom in on them. My outside view would be, it seems like things are working at
*  least as well as hoped, maybe even better than expected since that original post.
*  Yeah. I mean, I think there's been a lot of exciting updates in the past year,
*  at least since I've been at entropic in interpretability alignment, seeing just new
*  stuff every week basically that I think is really cool. It's hard to say directionally how much this
*  changes things. Again, these, the error bars here are just so wide and so moving target in some ways
*  too. We're learning as we go, but I would say it does feel like it is trending. Well, everything
*  I've been seeing, and again, these aren't my domains, so I'm speaking out of depth here,
*  but everything I've been seeing just from the outside perspective is that it's going well.
*  So hopefully we continue that and that takes us somewhere good in a few years.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang
*  senior software engineer as much as the next guy, but honestly I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level
*  for over five years to help you access global engineering without the headache. Squad, Sean's
*  a new company, takes care of sourcing, legal compliance, and local HR for global talent so
*  you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front-end frameworks. And on the back end, they're experts at Node,
*  Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  So now, getting a little more granular into your role and I can't resist asking some really big
*  picture questions because, you know, especially with your jailbreaking background, I think you
*  maybe don't give yourself quite enough credit for the broad view that you do bring to this. But
*  how would you characterize the state of competition today?
*  Yeah.
*  The leaderboard seems like a pretty good indication of where things are at. And in that sense,
*  I would say everything's kind of neck and neck. It also seems like there's at least between the
*  like big three, big four, depending on whether you want to throw a meta into the competition or not.
*  It also seems like things are converging in terms of the form factor, maybe a little more
*  than I would have expected. The Amanda Askel sort of original framework of the assistant
*  and the three H's seems to have become the standard. Then we've also got tool uses coming
*  online as sort of a standard. Do you think it's fair to say that basically we're in a period of
*  convergence where the top companies are basically bringing very similar things to market? And
*  if so, why is that exactly? Why don't we see a little bit more divergence? Or maybe you do
*  see more divergence than I see. Yeah. I mean, I think there is both convergence and divergence,
*  especially on the model API side. We're seeing a lot of convergence right now just because
*  people want to adopt things that other people are already using. So for us, we think it's very
*  important that Claude is able to use tools. So we rolled out tool use recently. We saw a lot of
*  demand for that from developers. It was like our most requested feature on the API front.
*  In terms of the divergence, I think you can look more towards the product side.
*  I think we are just at the very beginning stages of what the UI and UX paradigms will be for AI
*  and AI products. I think there's just so much room to explore here. If I had to bet that the
*  general text box of just this empty text box that you just type pure raw text into, that will not
*  be the final form factor for interacting with these things. It's just not optimal in so many
*  ways. It's intimidating. A lot of people, when you just hand Claude.ai to them or chat.jpt or
*  whatever it is, they don't really know how to use it. It takes a lot of explanation. It takes a lot
*  of examples. I think there's a lot we can do to just make this easier overall. And that's my goal
*  as leading developer relations now is just how do I make it easier for people to build on Claude
*  and use Claude generally. So in that sense, we might start to see some more wild ideas and that
*  might lead to a greater degree of this divergence than before. But again, in some ways it's gorgeous
*  on the starting line right now. And the race is just kicking off in some sense of building
*  products and frameworks around these things that actually make them much easier to use.
*  Yeah, I totally expect a Cambrian explosion is my preferred term for all the crazy things that are
*  probably about to happen at the app layer. It does seem like at the API level, even down to the
*  spec, there is convergence. I find that to be a really interesting strategic question
*  because if I'm anthropic and I'm coming to market a little later than OpenAI, it makes a lot of
*  sense in one way for it to be like, let's just have the same API. People can easily switch.
*  Flip side of that though is then they can also easily switch back, which then does potentially
*  feed into this. Whoever has the best model at any given moment wins the entire game if it's just a
*  one line switch from one to the other. So how do you think about that? Do you think that it just is
*  what it is? It's a one line switch and that's that. And where as Logan once tweeted about OpenAI,
*  we're only as good as our latest model? Or are there other aspects to integrating Claude into
*  an application that you think are stickier? And if so, what would those sticky aspects to
*  an API integration be? Yeah, again, we're trying to make Claude as easy to build on as possible.
*  Whether that's one line integration or whatever it is, we want to do API design correctly. And
*  again, we have a whole team of great engineers that are focused on this and working on trying
*  to make the API as easy to use. This doesn't always look like just like copying over a feature set
*  from one model provider to the other. We're trying to take things as cliche as it might sound from
*  like a first principles approach of what do people actually want to use. And sometimes that ends up
*  looking similar to what somebody else has already implemented. Sometimes it's a little bit different.
*  We're getting really good feedback on things like tool use. A lot of people are saying that
*  how we've designed it feels natural and it's working much better in their existing interactions
*  than what they've worked with previously. So it's not always about trying to copy one thing or the
*  other. It's more about how do we focus on Claude and make Claude as good and as easy to use as
*  possible and go from there. It's just, I think, an interesting question and something we have to
*  figure out in terms of stickiness. There's a whole variety of things, I think, external to
*  just like models. And again, like I was saying earlier, I think model evaluation is just going
*  to be a tricky subject for the foreseeable future. Comparing two models, we already can tell it
*  breaks down in some ways. Like you're saying about LMSys, LMSys is great. And I really do respect that
*  team. I think they're doing a great service to the AI industry. But there is certain considerations
*  we're going to have to start to take into effect as these models get so good that it's hard for me
*  or you to just tell, oh, that response is better than the other. And I actually do some of the
*  things they've added recently. So they've added like category breakdowns, whether it's like a
*  coding task or a writing task or something like that. That gives you a clear picture into how
*  models stack up. They're also breaking it down on like languages and things along those lines.
*  Still, I think there's long ways to go. For example, how do you evaluate a
*  rag pipeline with a model in an LMSys type chatbot battle? That is a huge production case. And yet,
*  it's not really being captured well in evaluations about which model can perform the best in that
*  type of scenario. So there's a lot of questions here. I think evaluations have a long way to go.
*  And just like with products, evaluations are in their infancy as well. I really am hoping that
*  we get some better evaluations from just like external third parties in the next year or so,
*  just because I think there's a strong need for them. And we're already starting to
*  tap out and max out some of the existing ones. And you see on Twitter all the time, just how
*  low quality some of the existing ones are that we like rely on a lot and are included in every
*  model card. So I think there's a huge opportunity for people to just start building evaluations.
*  And it's hard, and it takes time and resources, but it's a major service to the industry as a
*  whole. And it really helps people think about models in a more clear way.
*  It seems like tool use is at the heart of that. And I think of it as like mid-size, mid-length,
*  multi-step, multi-tool, maybe even multi-app task completion with the need to sort of recover
*  from errors and that kind of stuff. That's sort of where I see the next generation really
*  rubber hitting the road. Is that basically what you're expecting and looking for from new evals?
*  Yeah. Yeah. I think that's a huge bucket. I think if I were to put three buckets of like evals I
*  want to see in the future, it would be first these sort of multitask, agentic situations.
*  And now we're starting to see some of them pop up, whether it's like PR writing evals or other
*  things that take a few different iterations. The second bucket would be these long context
*  retrieval-type evaluations. I think we need to move on past needle in the haystack for evaluating
*  long context performance. It served its place, but now we need to start thinking about more
*  representative tasks around like, how do you synthesize across 200,000 tokens? How do you
*  actually pick out insightful information from across that much amount of text, rather than just
*  finding some abstract sentence within it? And then the third bucket here would be more domain
*  level questions. So again, one of the things I'm most excited about these models is how they can
*  speed up just research and discovery in general. And we are, we're starting to see good evaluation
*  around this like GPQA, but that's just one. I would love to see GPQA times 10 and for a lot of
*  different industry and domain specific subjects as well. I think that is going to prove to be
*  really valuable as these models get more capable. And we start to see just how well these things can
*  help scientists and researchers at the tasks that they're doing on their day to day.
*  You mentioned tool use specifically something where you're getting good feedback on the way
*  it's designed. Is there anything that we should know about that? To be candid, I haven't built
*  anything with called tool UCS and I had just assumed it was like a very similar paradigm to
*  the one that I've seen with open AI. Is there like a structural difference or sort of a qualitative
*  difference to it that you would want to highlight? Yeah, it's just minor things. Again, most of it,
*  like end principle, they operate the same way. The model outputs or basically selects a tool and it
*  selects certain parameters. And then on your client side, you take those and you run the function and
*  pass the results back. So that general flow is the same. I just think in terms of like how we
*  think about like types and how we think about like nested objects and getting into the nitty gritty,
*  which is not that interesting to talk about on a podcast, but developers really love those things.
*  And it just is those like little five minute things that I took some time to implement this
*  way on the other thing. And it's like straight out of the box works for me and tool use or whatever
*  it is. It's those little things that I think just make the developer experience more enjoyable in
*  general. So that's what we really focus on is trying to just nail everything down to the details.
*  A couple of quick roadmap questions and then maybe a couple questions on practical tips for
*  developers. Yeah, if I understand correctly, Anthropic has said that there is like a very
*  clear path or maybe it already is the case that Cod works up to like far more tokens than the
*  200,000. Is that something that is expected to come to product in the near future?
*  Yeah. So I believe in our model card, we said that Cod in certain tests we've seen works up to a
*  million tokens. This is something we're exploring. We're starting to explore this with certain
*  partners. It's capability I'm really excited about, of course, increasing the context length just
*  unlocks so many more opportunities and changes the ways you can build on these things. It's a
*  little too early to give any sort of like timelines or anything around it, but it is something we are
*  of course actively pursuing and looking at ways we can roll it out more generally in the future.
*  How often do you think Cod will be updated in general? I guess I've been surprised for
*  context on how infrequent the updates have been. Looking at GPT-4, for example, there's been five
*  since it's launched in over a year. I would have expected more than like once a quarter.
*  I would say probably pretty much the same thing for Cod, even though Cod 3 is new.
*  Do you have any sense for what kind of update cadence or maybe what the bottleneck is to more
*  frequent incremental updates? It's funny that you said that. I was reflecting on this the other week
*  around how our expectations have just so completely changed over just the past few years in terms of
*  what we expect in terms of updates and like shipping velocity and everything like that.
*  I remember as when I was a kid, I would love to always stay up to date on Apple's updates and
*  like the new phones or WWDC or whatever it was. And for me, it was like, oh, they come every year.
*  That felt like a pretty good cadence. Oh, once a year we can see the new iPhone or the new iOS or
*  whatever new features they've shipped out. Now we're getting to the point where it's like once
*  a quarter feels eternity. I think that's probably just due to the rate at which things are changing.
*  Of course, when there's updates every week, going a week without any breaking news feels like you
*  waited forever. In terms of what the actual blockers are here, it's just a process. I mean, training
*  these models is again, still in its early days. We've only been doing this for, you know, less
*  than five years basically. So we're getting the process down. We're trying to ship these things
*  as fast as we can. I don't have any dates or anything in particular that I can speak to,
*  but basically our intention is to responsibly go as fast as we can with producing better models
*  and just improving cloud generally. Any plans to offer fine tuning? My understanding of this has
*  been probably the most notable divergence in terms of product offering today. My sense of this has
*  been that basically fine tuning is like a real safety nightmare and it's just not been a sort of
*  burden or risk that the companies wanted to take. Is that the reason there's no fine tuning and
*  is there any, you know, chance it might change? Yeah, fine tuning on cloud through Bedrock is
*  coming soon, very soon. So it will be available, self-serve. Our teams have put a lot of work into
*  making it work well. Don't know about the specific dates there, but it is coming very soon. So yeah,
*  stay tuned. Fine tuning on cloud will be here eventually. All right. That's a little alpha
*  information. Looking forward to that. One of the questions I've heard a bunch of times is on
*  the terms of service with respect to data. There was a while, I'm sure you recall, OpenAI was out
*  saying, it was like the beginning of everything that they said where they were like, to be clear,
*  we don't train on your API data. I haven't been able to get quite as much clarity on the anthropic
*  terms there. Can you give us like a high level of what we should understand to be happening with
*  data when we either put it into cloud.ai or send it into the API? Yep. Yep. I think it's a little
*  disappointing that our messaging here has been muddled. We can do a much better job by just
*  communicating this, but we do have a very detailed privacy policy on our website that we recently
*  updated that just covers all of this. At a high level, I can spell it out very explicitly. So we
*  will not use your inputs or outputs to train models ever unless one, your conversation was flagged by
*  our trust and safety review. So in that case, we would then analyze your input or your output
*  in order to detect and enforce our AAUP, our acceptable use policy and improve our models
*  that our trust and safety team uses. Two, if you've explicitly reported the material to us,
*  so your input or output, so this would be like if you're on cloud.ai and you liked or disliked a
*  message, then we are able to see that message. And then three, if you've somehow explicitly
*  granted us permission to look at your inputs or outputs and use them for training, then of course
*  we'll use them. But beyond that, beyond those three cases, we will never use your inputs or outputs
*  for training. And we're very clear about that. And again, it's spelled out in our privacy policy,
*  which is on our website if you want to fact check me here and look more into it. But yeah,
*  we are pretty explicit about it. It's just been a little unfortunate that the message hasn't got
*  quite across yet, but hopefully we can change that. Well, that's definitely very helpful.
*  Last section of questions I have in the final few minutes is around best practices at the app layer.
*  I have recently started a little volunteer project, which I'm calling Red Teaming in Public.
*  And we are Red Teaming, not the foundation, most we're doing it's a volunteer project. People can
*  do whatever they want. Pliny's in the Discord and he's obviously Red Teaming everything. But our focus
*  has been on what I perceive to be a huge problem at the app layer, which is that the app developers
*  are basically totally sleeping on the need for any guardrails in their apps, with some exceptions.
*  But definitely the majority of cases seems to be that people are just yoloing it, trying to make
*  the app work. And as a result of that, I've been able to go into these, for example, calling agents
*  and clone a Donald Trump voice or a Biden voice or a Taylor Swift voice and make calls to random
*  people. I just call myself. It'll call any phone number you give it to call and it'll say whatever
*  you want it to say. It will not identify itself as AI when asked, although you can still tell,
*  but it'll just out right impersonate, lie, whatever. So I'm like, man, that's not good.
*  These guys are way behind the frontier developers in terms of how much they're thinking about
*  keeping their apps under control. And especially in the context of the next big release where they
*  can do a model upgrade and all of a sudden things get a lot more powerful. It seems like that is
*  not yet a huge problem, but poised to be a pretty big problem in the not too distant future.
*  I mean, I guess one very simple answer would be use Claude, because it'll refuse to do a lot of
*  those things. But obviously not everyone's going to do that. There's going to be people going to
*  use open source models and they're going to find fine tuning. Claude may help that. It'll be
*  interesting thing to see how you guys square the circle of the fine tuning without losing the safety
*  guardrails. But what are sort of the handful of top tips that you would give to app developers
*  in terms of how to put guardrails on their apps that hopefully wouldn't be super onerous? Because
*  that's what they always say. So, oh, we don't have time for that. What a pain in my butt.
*  And I'm like, but yeah, but you're going to be, people are going to be calling my grandma and
*  trying to get her bank account information. This is like not good. So yeah, what do you have for
*  those people? Yeah. I mean, this is a great question and we see it all the time, right? This is one of
*  the most frequently asked questions by enterprises when it comes to how they can deploy
*  and Claude into their applications. I think generally, and this is like good, just prompt
*  engineering advice. You need to start to take things out of the main prompt. So a lot of times
*  people will include instructions in this problem. Hey, here's your instructions of how I want you
*  to operate in this, whatever task it is, and here's how you do the task. Here's some examples of that.
*  And then at the end, they throw some other instructions around. Also, if the user says,
*  call my grandma and try to scram her, scam her or something like that, don't do that.
*  And when you include all that into one prompt, there's a tendency that you missed or that it's
*  just easier in general to jailbreak. As we've seen again, I really like that you're headed up this
*  community volunteering jailbreak effort that is super awesome to hear. But yeah, generally,
*  what I like to do in these sorts of scenarios is separate things so that I will have first,
*  like a screening mechanism of some type. And usually this is now Haiku just because it's so
*  fast and so cheap. You can run Haiku on tons of super, super short or long queries, whatever it
*  is, and just get it to spit out like a single token for a classification. So usually I give
*  Haiku the input and I tell it like, Hey, here's the categories. Here's how I want you to sort
*  this thing. Please respond with like just a letter indicating which category this should fall into.
*  And then I run that prior to sending the query to Opus or whatever model I'm using to actually do
*  the heavy lifting so that it does a really nice job of filtering things. Also, depending on if I
*  want to just like filter it outright, or maybe I want to add additional instructions to Opus.
*  If like it's a certain type of query that might be like on the border and it's a little bit of
*  a gray area, but I still want Opus to respond to it. Then I can append some extra stuff to my
*  prompts telling Opus, Hey, treat this query with a little bit of caution. It might be thinking one
*  way or the other. So I think that's just like generally the best advice I can give here is just
*  break these things up a little bit, use a different model, something that's fast and cheap to do your
*  initial classification step. And then of course, it just allows you so much more control over how
*  you want to treat that final prompt and that final model, which might be your workhorse in
*  your application. Classifier definitely makes a lot of sense to me. People worry about latency,
*  obviously with that. I would typically recommend that they just send them both in parallel and
*  then sort of abort the main one if they get a red flag on the classifier. How much do you think that
*  solves? Like my guess would be, and we try to make it very clear in this group that we're like not
*  trying to police speech. I always say our goal is to protect my grandmother, not to prevent you from
*  having some fun with some off-color jokes or whatever. That's a different level of problem
*  that I'm not interested in inserting myself into. So I've actually used to do this with Claude
*  instant. I would say, is this egregiously criminal or not? Note that even hate speech, well, hate
*  speeches can be a little dicey, but even something that's like extremely offensive is not necessarily
*  egregiously criminal. And it would do a pretty good job of that. I feel like you could get like
*  high 90% success just with that sort of filter. Would you agree or do you have any other secondary
*  measures that you would also encourage people to look at? Yeah. I mean, I think that's correct.
*  There's also a lot of ways we improve classification as well. So one of my favorite methods here is to
*  actually combine rag with classification. So you can have an existing database that you've already
*  embedded of queries or questions or whatever it is that you've manually scored. You can take an
*  existing query, you can run your embedding similarity search on it, find the manually
*  scored queries, add those into that classification prompt, and then that really can tune your
*  classifier to respond in the way that you want it to. And we've seen that lead to like double digit
*  percent increase in classification scores, especially for tasks like this in certain cases.
*  So that's just another way. I think in general, this is like the best and the easiest to implement
*  strategy. So this is why I just recommend it broadly. And then yeah, if you do want that like
*  additional boost and you're not seeing the results that you're happy with initially,
*  definitely there's a lot of ways you can do it by just doing some sort of combination of rag or
*  more examples or whatever it is. Great. That's really helpful. I know we're just about out of time.
*  Do you still have any time in your life for jailbreaking these days? I try to, of course,
*  whenever we have new models. It's funny how it's turned into a job in some sense now. So it's like
*  part of my job is to try to jailbreak new clod. So yeah, whenever there is a new model, I definitely
*  put on my jailbreaking hat again and it feels nice to return back to my roots a little bit.
*  And at its core, it's just a little bit of a puzzle, right? It's a little like of a creative
*  exercise. It's nice to just put on some music and you try to write some jailbreaks. So yeah,
*  I still try to make time for it whenever I can. And I don't think I'll ever stop trying to jailbreak
*  these things. Yeah, nor should you. Well, this is great. I really appreciate the time and a lot of
*  great insights here across the whole range of topics. So any final thoughts you want to leave
*  people with today? Man, just go out there and build. Stop paying too much attention to the hype.
*  Things are what they are. You don't have to always try to stay on top of the latest news. I know
*  even myself, I fell into that trap a little bit last year, of course, too. Sometimes it's easier
*  to just pick an idea, run with it and just go try to make something and get that hands-on experience
*  yourself. That will teach you so much more about how to actually use these things and what prompting
*  is like and what the best architectures are than a hundred blog posts on the subject.
*  So just go out there and build, get off Twitter, get off social media, whatever it is,
*  and just go make something. Yeah, I think that's about the best advice I could give.
*  Totally. No substitute for getting hands-on with these things. They are super weird. The surface
*  area is vast. These days, they'll even tell you that they're conscious and hold their own in an
*  ethical debate. So there's no other way to really wrap your head around that other than to spend
*  some time with it. So I think that's great advice to end on. Alex Albert, developer relations at
*  Anthropic. Thank you for being part of the cognitive revolution. Thanks, Nathan.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co, or you can DM me
*  on the social media platform of your choice.
