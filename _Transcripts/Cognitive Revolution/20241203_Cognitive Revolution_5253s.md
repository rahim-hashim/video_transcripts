---
Date Generated: December 14, 2024
Transcription Model: whisper medium 20231117
Length: 5253s
Video Keywords: []
Video Views: 1988
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, Nathan welcomes back Div Garg, Co-Founder and CEO of MultiOn, for his third appearance to discuss the evolving landscape of AI agents. We explore how agent development has shifted from open-ended frameworks to intelligent workflows, MultiOn's unique approach to agent development, and their journey toward achieving human-level performance. Dive into fascinating insights about data collection strategies, model fine-tuning techniques, and the future of agent authentication. Join us for an in-depth conversation about why 2025 might be the breakthrough year for AI agents.

Check out MultiOn: https://www.multion.ai/

Help shape our show by taking our quick listener survey at https://bit.ly/TurpentinePulse

SPONSORS:
Oracle Cloud Infrastructure (OCI): Oracle's next-generation cloud platform delivers blazing-fast AI and ML performance with 50% less for compute and 80% less for outbound networking compared to other cloud providers13. OCI powers industry leaders with secure infrastructure and application development capabilities. New U.S. customers can get their cloud bill cut in half by switching to OCI before December 31, 2024 at https://oracle.com/cognitive

SelectQuote: Finding the right life insurance shouldn't be another task you put off. SelectQuote compares top-rated policies to get you the best coverage at the right price. Even in our AI-driven world, protecting your family's future remains essential. Get your personalized quote at https://selectquote.com/cognitive

Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

RECOMMENDED PODCAST:
Unpack Pricing - Dive into the dark arts of SaaS pricing with Metronome CEO Scott Woody and tech leaders. Learn how strategic pricing drives explosive revenue growth in today's biggest companies like Snowflake, Cockroach Labs, Dropbox and more.
Apple: https://podcasts.apple.com/us/podcast/id1765716600
Spotify: https://open.spotify.com/show/38DK3W1Fq1xxQalhDSueFg

CHAPTERS:
(00:00:00) Teaser
(00:00:40) About the Episode
(00:04:10) The Rise of AI Agents
(00:06:33) Open-Ended vs On-Rails
(00:10:00) Agent Architecture
(00:12:01) AI Learning & Feedback
(00:14:01) Data Collection (Part 1)
(00:18:27) Sponsors: Oracle Cloud Infrastructure (OCI) | SelectQuote
(00:20:51) Data Collection (Part 2)
(00:22:25) Self-Play & Rewards
(00:25:04) Model Strategy & Agent Q
(00:33:28) Sponsors: Weights & Biases RAG++
(00:34:39) Understanding Agent Q
(00:43:16) Search & Learning
(00:45:39) Benchmarks vs Reality
(00:50:18) Positive Transfer & Scale
(00:51:47) Fine-Tuning Strategies
(00:55:16) Vision Strategy
(01:00:16) Authentication & Security
(01:03:48) Future of AI Agents
(01:16:14) Cost, Latency, Reliability
(01:19:30) Avoiding the Bitter Lesson
(01:25:58) Agent-Assisted Future
(01:27:11) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# The Evolution of AI Agents Lessons from 2024, with MultiOn CEO Div Garg
**Cognitive Revolution:** [December 03, 2024](https://www.youtube.com/watch?v=30Nf4xQ_Foo)
*  I think OpenAI has definitely lost a lot of the lead they used to have.
*  The GPD 4 where they were kind of the sole winner and no one could catch up with them.
*  At this point it does seem like a very homogeneous market where everyone is kind of close.
*  When anything is disruptive, I think that it takes a lot of time for that to catch on.
*  And I think we are at the start of the disruptive era where a lot of the
*  online communication and interaction will get disrupted by agents.
*  Humans are pretty good at navigating websites with UI.
*  So theoretically, AI can also become very, very good. Even better.
*  I would call it explosion applications, which I don't think has happened so far.
*  I think about agent applications. I think it's still very good.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, Div Gurg, founder and CEO of Multion, returns for his third appearance on the show.
*  A lot has changed in the AI agent landscape since I first spoke with Div in mid-2023.
*  As you might remember at that time, the AI community was abuzz about the potential for
*  AI agents. With projects like BabyAGI giving large language models access to tools and really only
*  very minimal guidance and then stepping back to watch and see what they could accomplish on their
*  own. Of course, as it turned out, they didn't accomplish all that much. While there were many
*  amazing moments, those were the outliers. On average, the step-by-step error rate,
*  including on very mundane microtasks, was too high for agent frameworks to successfully string
*  many step sequences together all that often. And we also learned that while large language models
*  can improve in many areas through self-critique, they have a tendency to get stuck on obstacles
*  that humans quickly find ways around. For that reason, much of the last 18
*  months of work on agents has gone into developing better and more prescriptive scaffolding,
*  with many companies ultimately delivering platforms for what I call intelligent workflows.
*  That is, workflows that a human has designed and where the AI is needed to do some important
*  sub-task which requires intelligence, but where the AI is not given freedom to choose its own
*  adventure. As of January this year, Div and the Multion team were still among the most bullish on
*  open-ended agents, and as you'll hear in this conversation, they have continued at least partially
*  to buck that trend. They have built some new scaffolding and they have developed interesting
*  techniques for domain-specific fine-tuning, but their agent continues to take arbitrary natural
*  language requests and gamely does its best to fulfill them. The progress I found in my testing
*  is pretty obvious, and in some contexts the company claims human-level performance,
*  but still the system as a whole is not a viable substitute for a human assistant.
*  With that in mind, I was excited to pepper-tip with questions about what he's learned from all
*  of this activity, and so in this conversation we unpack the latest in agent development,
*  including the company's data collection strategy, the seemingly missing market for human computer
*  use data, and the role of synthetic data in bridging that gap. The company's model strategy,
*  including what models they've chosen as base, what fine-tuning techniques they're using,
*  and how their computer vision approaches have evolved over time. Why benchmarks so often show
*  human-level performance while the real-world results are clearly not as strong. The future
*  of agent authentication, as well as which parts of the internet at large will compete to serve agents,
*  versus which parts will try to exclude them. And finally, what sorts of customers Multion is looking
*  to partner with now, as well as how they're thinking about competing with hyperscalers
*  in light of Claude's new computer use capability.
*  Overall, it's clear to me that while it's taken longer than I had expected, reliable agents that
*  can perform a very large percentage of routine computer use tasks are coming. It's only a matter
*  of time. And as you'll hear, Div agrees with recent suggestions from both OpenAI and Anthropic
*  that 2025 will be the year. That of course makes Div a very busy man, and so I very much appreciated
*  his time and how open he was willing to be about the path that Multion has taken and the lessons
*  they've learned along the way. As always, if you're finding value in the show, we'd appreciate it
*  if you'd share it online, write a review on your podcast app, or leave a comment on YouTube.
*  Of course, we welcome your feedback and suggestions via our website, cognitiverevolution.ai,
*  or by DMing me on your favorite social network. Now, here's my conversation with Div Gerg of
*  Multion, catching up on the last year in AI agents. Div Gerg, founder and CEO of Multion,
*  welcome back to the Cognitive Revolution. Yeah. Thank you, Nathan. I'm excited to be
*  back. So agents, agents everywhere. The last 18 months has been quite the saga when it comes to
*  AI agents, their promise and whether or not they fulfilled that promise. And obviously, you've been
*  right in the thick of it as the founder of this company. How would you tell the story of agents
*  over the last 18 months since like the launch of GPT-4? And where do you think we are now in the
*  grand saga of AI agents? Yeah, I think it's been interesting to see. I was still saving very early.
*  I would call it like it's similar to the internet explosion. So we are kind of seeing like the
*  first wave of the internet in a sense, where it's still like glitchy, it's slow. Most people have not
*  used it. But the next thing that's going to happen is like this will become like more mainstream,
*  like the quality and reliability will go really up. And over time, this will become like,
*  there are still a lot of like opportunities where a lot of like the things that happen
*  in the daily life will become more agent-taking over time. So I do think like agents are still
*  very early. I think it's a competitive for definitely, I think at that time, it was kind
*  of a promise that okay, these kind of things are going to happen, you'll have this kind of
*  autonomy capabilities. Now, I think we're starting to see the early versions of that,
*  where like maybe people have found some like use cases and like specific verticals from
*  business use cases. I think it's still is very early. Most people have not created
*  by the H&D product. So I think it's still like Amazon explored it fully. And I think that will
*  take more time. Tell me about your agent lifestyle today. In the past, you've posted some viral demos
*  on Twitter of like having an AI agent order your lunch or do these kind of various transactions for
*  you. I think you had one of the first demos of it booking a flight. How is your day to day experience
*  of agents? Like what are they doing for you right now?
*  Yeah, that's been pervasive. I think I'm still using agents a lot for like shopping has been
*  a big use case like Instacart, groceries, definitely calendar invites. And then maybe a bunch of stuff
*  on LinkedIn or Twitter or a bunch of these kind of places where like you want to
*  do some boss that can automate things. For me personally, I definitely have a lot of my scheduling
*  is not based on agents. A lot of my groceries and some of my online shopping and the app that I
*  sell to the sun agents on. So let's talk about kind of a few different approaches to building
*  agents. It seems like in the beginning, the first wave of things that were launched, often it's just
*  like open source, check this out and mess around with that kind of projects. I'm thinking here of
*  like baby AGI and that sort of early wave. We're very much just like, Hey, GPT four looks really
*  smart. Let's let it figure everything out and kind of give it very open ended environment, very
*  sort of open instructions and kind of hope for the best. It seemed like by and large,
*  with notable and kind of exciting demos as the exception rather than the rule, those approaches
*  led to disappointment when people found like, Oh, well, it doesn't really work most of the time,
*  it gets stuck in various ways and whatever. And so the counter narrative, I would say,
*  has been where the counter, the sort of compensating approach, maybe is a better term for it,
*  has been to put the agents on rails to give them much less sort of autonomous decision making
*  authority and instead build out like very prescribed workflows where the step by step is
*  kind of designed by the human workflow designer and the AI is kind of there for the key bits that
*  require intelligence, but is not like left to choose its own adventure. You shared a preview
*  version of the latest multi-on agent and I was messing around with that. It seems like you guys
*  are still more in the open ended frame of development, but I'm sure you've tried a bunch
*  of stuff and have perspectives on those two different approaches. So tell me everything
*  about the open ended versus the on rails approach. Yeah, I think that's a good question. I totally
*  agree. I think on rails is the right way to start from, especially if you know exactly what use case
*  you want to target. If you're doing anything like enterprise or B2B SaaS, whatever. I don't think
*  like this kind of like more linear constraint workflows, I think is the right paradigm to start
*  with. And I think over time, I think you can have more open ended use cases which allow for
*  more general purpose experiences. I think for us also, we're trying to take a road in the middle
*  where we don't want to be too constrained because I think we're still targeting a lot of everyday
*  use. And what happens we have several like, I don't know, like at this point, 3000 plus people
*  from like all the user data we have. And I think the consumer behavior is just very different for
*  everyone. So depending on your demographics and age groups and like where you live, a bunch of
*  things. I think consumer behavior changes a lot. So you can have very constrained linear workflows,
*  because then you have to build like millions of these and like that's not possible.
*  And then you also want to be fully open ended, right? Because like if you have fully managed
*  something like the computer use API that came out for Anthropic, it's very general purpose,
*  but like it's like, it's very hard to find a utility for that. And so I think we're trying
*  to take a road in the middle where like how can you build more constrained workflows for
*  like tasks that you can define. And then we are building a lot of like verifiers and like one
*  thing in the direction was the agent QT research we did, where like the agent can learn to improve
*  and like improve its behavior on new websites it has never seen. And so we're starting with like
*  more domain specific models. And the models like know how to like do like vertical workflows of
*  tasks to develop. Or this models can improve and like generalize over time. But we don't want to
*  start with models that are fully general. Because that seems to be like a really big effort and also
*  doesn't seem something that will I think for a startup like us will pay off in the next six
*  months. How does that look behind the scenes? I mean, in my experience of the product,
*  it does still present as a very open ended thing when talk about kind of having these linear or
*  closer to linear on rails workflows in the background. The Voyager project comes to mind
*  from Nvidia, I'm sure you're very familiar with that, where they would have the agent,
*  you know, like a virtual video game environment, it was Minecraft, go out and like figure out new
*  skills and then sort of cache those skills for future use. So it didn't have to constantly
*  reinvent the wheel. Obviously, that's like a pretty big open ended environment, not nearly as big and
*  as wide ranging as doing stuff broadly on the internet. But what have you found to be the right
*  architecture for or the right balance point between like what is prescribed versus what is
*  left to the agent to decide at runtime? Yeah, that's a good question. I think what
*  better time we have landed on is kind of like user choices. So it's like you don't want the
*  agent to be fully autonomous. I think an example I like to use a lot is kind of like fact booking.
*  So you don't want to have the agent go and book you like a random flight and waste thousands of
*  dollars without like sort of like checking in with you like do you actually, are you fine with this
*  time? So do you want to find the evening? Do you want non-stop or like this airline is still
*  okay? So preferences matter a lot. And I think the paradigm we have landed on is like choices
*  where like you might give some sort of potentially ambiguous user query to the agent like go book me
*  a flight this weekend for a trip to Paris and then you want the agent to kind of fill in the blanks
*  where like okay like that requires maybe like a lot of choices that have to be implicitly being made.
*  And then like we are building a lot of these workflows where like how do we cast things,
*  the preferences, how do we make like involve the human in the loop? And I think that becomes
*  complicated where like you do it, I'm not relying on just the actions but also maybe like
*  how to personalize, how to maybe like really get to know like what to do and then based on that
*  like build like a really sort of product experience. What are the experiences that I recall from an
*  earlier version of the product that I don't know if it's still there? Maybe I missed it this time
*  around in my testing was the opportunity to essentially correct the AI if it made a mistake
*  and if to sort of demonstrate or like teach I think was the word that you used in the past.
*  The AI how to do a particular skill, you know I think probably most people would find it reasonably
*  intuitive to imagine how that was supposed to work, right? You would have the agent go do stuff when
*  it makes mistakes, the human could teach it what to do, then of course it would learn what to do and
*  maybe fold that into your training data later. I wonder if like that has played out as you've
*  thought it would or are you now doing that in a more implicit way or do you just find that like
*  that human sort of teaching paradigm is just not so useful as anticipated and if that's not working
*  like what is the alternative in terms of how do you source data to you know to teach the models
*  what to do? I think we've had good success with that. I think we collected like some millions of
*  trajectories using that method. The problem with any sort of crowdsourcing is like you can't really
*  trust the quality of the data and I think like Tesla is a good example for that. I think Tesla
*  has been trying this for the most early week olds where they crowd source a lot of data but like
*  filtering like the quality of the data is like actually good data versus bad data. I think that
*  has been like a thing where like you build a lot of filtering pipelines and build a lot of like
*  AI's logic around that. So I don't think we have been doing a lot of that maybe we've seen some
*  pay-all but I think it's still like I think it's just like a very noisy so that makes it
*  like a hard problem. The second way is like basically just working with like high quality
*  annotation data where like I won't say like too much here but like if you have annotators or like
*  people who can like sort of like have to collect expert data and I think that seems to be like one
*  paradigm maybe that more frontier labs are pushing towards but like you can go and like train these
*  agents on a lot of these general purpose use cases and then like train different models that are
*  working with you. I hear you on things being noisy. I also imagine of course the counterpoint
*  would be like human annotators are expensive and limited in supply. One question I have is why is
*  nobody propositioning me to pay to watch me use my computer all the time? Like I feel like there
*  should be a market now in install a general observer that just kind of watches a person use
*  the computer maybe get up a couple different modes of it including one where you like talk
*  through what you're doing and explain yourself because obviously most of the time the chain of
*  thought is not actually said out loud and recorded. You know you'd have to clean up that data of course
*  people are doing random stuff you'd also have to anonymize that data. I would want to know who you
*  are and I'd want to make sure I trust you before I let you install that on my computer but I feel
*  like with the the cost of annotation as people get into like higher and higher end knowledge
*  workers or even like scientific experts in some cases for the sanitation stuff it feels like
*  that's pretty valuable and I feel like I should be getting like a thousand dollars a month at least
*  for somebody to watch me use my computer so why isn't that happening or if it is you know point
*  me to where I sign up. Yeah I totally agree I think the market is there now I think it wasn't
*  there maybe like even a month or two ago I think it's a new market. I just I think it depends like
*  who's willing to purchase the data because I think at the end of the day getting this kind of data
*  is not that expensive because I think there's enough people who are willing to donate this data
*  for very cheap most especially if you can like use other countries and like whatever like outsource a
*  lot of this kind of data collection. I started thinking a lot of this data can get very cheap it
*  does become like if the company is really interested in your personal data and then they may be going
*  to offer like more like a thousand dollars a month just to be able to like get access to be very
*  like more like personal okay like what makes Nate and what does it that look like when he's using
*  his computer. Yeah I mean it's an interesting paradigm it kind of reminds me of we did two
*  episodes they were separated by some number of months on MindEye and MindEye 2 and in the
*  first case and this was like reconstructing what somebody was looking at like what image they were
*  looking at by the fMRI data scanned from a scan of their brain at the time that they were looking
*  at this image. In the first version it was patient specific modeling that was being done
*  and you had to have something like I don't know 20 hours or whatever of of these scans with a person
*  looking at a new image every few seconds to then finally get to the point where you could train a
*  model on that person and then in the second edition they had figured out how to kind of
*  let's say map all of these different users each of which have like a different anatomy of their
*  brain literally like different brain sizes there's a lot of course difference between people
*  map that all into essentially a shared space train one model on all of those data points
*  and then from that base model it would only take like an hour of one individual's data to kind of
*  fine-tune it to their particular anatomy and activation patterns. So I can see that here too
*  where you might say you know there's vast bulk data to be collected out there and then we just
*  on the margin it's really about fine-tuning to each individual person. So I guess what you're
*  saying is like that market is international and it's just a it's a lower price point because
*  I guess people feel like they want to separate out like scientific expertise from just like
*  general routine computer use and it's better to buy those separately at different market prices.
*  Yeah because if you think what the generic computer uses it's not that expensive it's also
*  like I think like very common patterns so I started thinking you can just outsource a lot
*  of that get that very cheap. I do think there's value of personal data which is like if you're
*  willing to share all your personal data and exactly how you are doing things and you don't
*  care about privacy then I think people are willing to figure a lot where like if they can get access
*  to a lot of this private data and then they can like maybe use that fully and then maybe like I
*  do think like that is a market that doesn't exist but that could be like very valuable market where
*  people are willing to pay a lot of money if they can get access to this private data and then you're
*  willing to like sort of like live with that kind of like loss of privacy in a sense.
*  Hey we'll continue our interview in a moment after a word from our sponsors.
*  Even if you think it's a bit overhyped AI is suddenly everywhere from self-driving cars to
*  molecular medicine to business efficiency. If it's not in your industry yet it's coming and fast
*  but AI needs a lot of speed and computing power so how do you compete without costs spiraling out
*  of control? Time to upgrade to the next generation of the cloud Oracle Cloud Infrastructure or OCI.
*  OCI is a blazing fast and secure platform for your infrastructure database application development
*  plus all your AI and machine learning workloads. OCI costs 50% less for compute and 80% less for
*  networking so you're saving a pile of money. Thousands of businesses have already upgraded
*  to OCI including MGM resorts specialized bikes and fireworks AI. Right now Oracle is offering
*  to cut your current cloud bill in half if you move to OCI for new U.S. customers with minimum
*  financial commitment. Offer ends 12-31-24 so see if your company qualifies for this special offer
*  at oracle.com slash cognitive that's oracle.com slash cognitive.
*  There are so many things in life we just never get around to.
*  Taking up that hobby, cleaning out the garage, you know little things that don't really make
*  huge differences in our lives. Yet there's one thing that most of us have probably been
*  neglecting that can have a huge impact on our family's future. It's life insurance and with
*  select quote getting covered with the right policy for you is easier and more affordable than you
*  might think. As someone who tracks AI progress on a full-time basis and obsesses about its potential
*  impact non-stop, I know how tempting it can be to ignore more mundane familiar risks. There's
*  always another paper to read, podcast to listen to, or product to try. And yet the smartest people
*  that I know in the AI space continue to save and invest money for the future, carve out time for
*  their relationships, maintain their physical and mental health, and yes protect their family with
*  life insurance just in case anything should happen before the singularity. If nothing else,
*  it's one less thing to worry about in a time of unprecedented change. So get the right life
*  insurance for you for less at selectquote.com slash cognitive. Go to selectquote.com slash
*  cognitive today to get started. That's selectquote.com slash cognitive.
*  Do you know what those data, I assume you're not doing this directly yourselves to the degree that
*  you are sourcing this kind of data, I assume you're working with partners to do it. Are there like
*  marketplaces that exist or go to companies? And are there, I'm also curious as to what degree
*  people are sort of logging in and doing like discrete tasks, like here's your task, go do it
*  on the browser, tick, tick, tick, versus just kind of open-ended observation that would be more of
*  like an imitation learning paradigm. How would you describe the, you don't have to give us any
*  secret services unless you want to, but let's say I wanted to buy this data, what's out there
*  that I can buy and who do I buy from and how much should I expect to pay?
*  I would definitely say there's a lot of data that companies, a lot of them we are working with,
*  again I can't really like, we are working with just for more like confidentiality
*  purposes, but I would definitely say like you've tried a lot of things, like even if you use something
*  like mDir or whatever like online solutions, I don't think you can like create tasks, okay like
*  I want someone who's doing this particular whatever like a computer is, so collect a lot of data and
*  then get a lot of like data that you can train on. I'm pretty sure that's what like Anthroplica is
*  doing, which is what they're doing. We have definitely done that, but then we're also like
*  thinking about a lot of like smart tricks, where like how do we find data in like the regimes we
*  care about, so how can we incentivize people to give us like the data that we don't have
*  and then make sure that we can like keep improving, figure out like where is the agent
*  most efficient on and get the right quality of data and keep them making better and better.
*  Are we at the point of self-play? Another thing that I sort of expect we'll have to tip soon is
*  just object feedback from reality, right? I mean we've obviously seen that work in all these
*  game playing environments. It has worked, but hasn't quite maybe hit the critical tipping point
*  yet for code generation, but I would assume that there's some analogous version of feedback from
*  reality that you could do in a open-ended computer use context too, right?
*  The thing that's missing the most right now is just having a really great quality report
*  that you can use from the environment. So when you're in a game-based setting like Minecraft or
*  something, you get a good reward or like even like when you're playing chess like a zero, you have
*  like you know exactly like what are the rewards for any moves you make in the game space and then
*  it's easy to optimize the policy and make it like yeah this is what we want to do to win.
*  What happens though is like if you are in like a more of a real world scenario,
*  there's no environmental reward and then you basically, that makes it challenging because
*  you don't know what is the objective that you're optimizing and then you maybe need to obtain
*  another model that is the kind of like giving some sort of proxy reward that you can use to
*  like sort of like optimize the model and make it better and better. I think the coding, I think
*  it's easier because you can create like unit tasks or you can have some sort of like static checking
*  like so you can get a numeric score on the quality of the code and like does this code actually
*  function well and then you can do some sort of self play okay like based on this kind of like score
*  can we optimize the score to actually become better and better and optimize it. I don't think it's
*  possible like there will be like some sort like the thing with this kind of algorithms is like
*  this always works to cheat in a sense so whatever metric or score you come with like the algorithm
*  might find a way to cheat like it might find some sort of like I just find out like you can just
*  create a lot of like null strings or something and like that actually solves the problem and
*  like gets you like infinity score or something like that and people have seen that because
*  reinforcement learning a lot when you use that in game playing environments. So yeah so I think
*  it becomes a question of can you obtain like high quality rewards on the setting you are in
*  and I think computer users like a hard one there like maybe a human can give you like the right
*  proxy various if you're doing things like human feedback much of the things things I think that
*  then it's possible but I think it's a harder problem than just like doing self play on a game
*  based on. I always remember you know that visual of I think it was a deep mind video game player
*  from like 2017 where the little boat is circling around and around the same space and like picking
*  up infinite points but not actually advancing in the game in the way that it was meant to so
*  yeah lots of vivid examples of mode collapse or other strange solutions in the reinforcement
*  learning world. So what's your model strategy today? I read through the agent queue paper
*  that you guys put out a couple months back at that time you were reporting results on a llama 370B
*  which you were doing a number of things to enhance obviously from its base version you know is that
*  still the baseline for what you guys are using in production or how would you characterize the
*  available I guess you know commercial and non-commercial open source options that are
*  available to an agent developer today? Yeah at this point I think we've got a lot of different
*  models so close source open source commissioner book like llama 17b has been I think a good
*  compromise in terms of speed versus the model reasoning capabilities and I think right now I
*  think it's starting to go more towards maybe like GPT-4-01 style where can you do like
*  inference time compute and can you optimize the model to do a chain of thought doing inference and
*  like become a better reasoner so I do think like that seems to be the way to solve a lot of these
*  complex reasoning problems so that's also what we're going towards where like I think at this
*  point the base model doesn't matter that much because I think there's enough base models most
*  of them are forming like similar-ish the recipe and like the data they're trained on are also
*  like more or less the same so then the trick kind of becomes like okay like what is your application
*  and how do you optimize the model on that application and I think that's what we did
*  with Agent Q where like we care about this kind of web interface that's kind of like a shopping
*  environment how can we get the right environment like feedback how can we train on the feedback
*  how do we make sure that this base model can like optimize and become better and better there
*  and then can you combine that with some sort of like inference time compute tricks to make it
*  like a better reasoner so I don't think at this point architectures seems to start becoming
*  irrelevant where like I think we might see some sort of like at least at the current scale it's
*  possible like if you are able to like 10x that can emphasize the parameters of the model then a
*  different architecture might like start shining all right now I think like most architecture seems
*  to like level out at the same performance where like there's not too much diversity
*  in terms of the models out there whether it's close to sort of open source and like how much
*  difference you can get so even if you look at the leaderboards like everything seems to be very
*  tied up it's everything's starting to come very very close no one has I think Open has definitely
*  lost a lot of the lead they used to have the gpd4 where like they were kind of the sole winner and
*  could catch up with that at this point it does seem like a very homogeneous market where everyone
*  is kind of close and the more the base model architectures kind of seems to become like not
*  relevant as long as it can use it interesting oh one would seem to be a possible exception to that
*  or no I mean obviously oh one is like expensive if you're trying to do mouse by mouse click and I
*  guess there's also a question right now of what is available is a one preview which doesn't have
*  the vision aspects enabled yet but does that sort of does that summary of everything sort of being
*  on a roughly even level include a one or not include that one like I'll say Owen is interesting
*  I think I would say it's very good math people have found out like it's not very good outside
*  the method America domain but I think it's very highly specifically jnone so so I'll say to give
*  no one I think it's not too different from what you have right now maybe like at least for the
*  one preview maybe like the flow and more this much better and then it can shine and they call a lot
*  different regimes I do think like this kind of paradigm where you instead of like training then
*  compute well like like last year gpd4 everything was we just throw more compute training more
*  parameters more compute more data and they get a better model that's more better reasoner I don't
*  think you're starting to see this type of like instead of showing up during training you throw
*  computer during inference and then like the more change you do the better you get and so for all
*  when it's kind of like if I throw less compute maybe it's kind of like maybe even worse than
*  gpd4 but if I throw a lot more compute maybe it's much much better and then so it's kind of
*  becomes like like how much time and compute can I throw bringing inference depending on application
*  but I do think that becomes like a different class of how to think about these problems
*  especially if you think about this is kind of like how much latency can you tolerate
*  adding friends and like how much resources are you willing to like give to the model
*  yeah I'm interested maybe we'll come back in a little bit to talk about kind of user experience
*  and how much you think some of that stuff matters like I'm always unsure about you know how much
*  cost matters how much latency matters obviously depends on the user experience and depends what
*  the agent is trying to accomplish but let's circle back to that for a moment let's stay on the
*  agent q research that you did I've got a table here that I pulled up from the paper there's
*  basically two kind of environments right that are used in the paper one is a e-commerce benchmark
*  that was created by academics and put out there and it's sort of a self-contained you know amazon
*  like environment for shopping and then the other one is actually going and having the agent do
*  things on open table if I understand correctly in both cases you get to about 95 percent success
*  through a variety of techniques and I thought maybe you could just like walk us through this
*  graph which people can pull up from the paper but it's a nice sort of explanation of how you build
*  up to the success starting from a llama 3 70b instruct base model which for the graph is coming
*  in on the open table task at not even 20 success that compares to gpt 40 which is over 60 but still
*  leaves like six more bars on the graph where you're layering on these additional techniques
*  and showing what the contribution of each one is so you want to take us from again under 20 percent
*  on llama 3 70b to a little over 60 percent gpt 40 to through six you know alternatives all the way
*  to the 95 percent yeah I think this is what I'll say like is possible with vertical specialization
*  models because I think what happens is like most of these models are just trained on very
*  generic internet data and then and they're not like really really super great at one thing
*  and I think that's very obvious when you look at like llama like like llama's like this performance
*  like 20 percent because I think it's probably never been trained on this kind of like tasks
*  before but then you start looking gpt 40 I think gpt 40 maybe has more browsing kind of like
*  capabilities or I think they're opening each other browsing too so they maybe have more data
*  on these kind of interfaces and that makes it like a better reasoner and a better like better
*  accuracy on this kind of like action tasks but again I think what happens is like just because
*  this is very generic there's no like specific fine tuning towards a particular vertical I think we
*  see a lot of loss of accuracy and I think that's one thing we proved with regionq where we were
*  like like now suppose actually have a llama model that performs 20 percent but then based on like
*  a lot of the data that we collect and we actually boost the performance to make it like essentially
*  close out the environment almost all the time and and then we tied this experiment where like
*  let's use a lot of like techniques like dpo that we're doing reinforcement and using like human
*  feedback and let's combine that with maybe like stuff like uh monitoring out a pre-search where
*  it can be searched the space of the websites so we can figure out we can explore the websites
*  figure out like like if we go down this route or this link will it work or not and if you're like
*  this didn't work this one worked and then keep doing that until we can kind of like keep on
*  doing make it better and better and and then we over time we have like a very specific like vertical
*  agent capability where like now this agent just knows like really how to innovate this website
*  and and the great thing is like this thing just took us one day so it was very fast and it's it's
*  kind of a self-improvement cycle so that you can just keep doing it more and more and so there's
*  some limitation on like like how much can you improve the performance as long as you have a good
*  quality feedback so as long as your feedback signal is very very high quality i think you can
*  you can just like keep making this better and better um and i think that was like a very
*  interesting learning like we were actually also very surprised like okay like that's
*  almost like a 4.5x improvement close to that you were like okay like yeah that's kind of
*  crazy like just in one day we were able to like boost our model that's forced 20 percent to like
*  get us all the way to to where we were able to push it with tech is used and i think that's kind
*  of like the same print here where how do you explore these moments and then then how do you
*  have this capability where you can excel learn and optimize hey we'll continue our interview in a
*  moment after a word from our sponsors as a developer the journey from concept to production ready
*  large language model apps is fraught with challenges dealing with unpredictable language
*  model outputs hallucinations and ballooning api costs can all be blockers to shipping your next
*  ai-powered feature that's where advanced rag comes in with the new rag plus plus course from
*  weights and biases you can overcome these hurdles and build reliable production ready rag applications
*  go beyond proof of concept and learn how to evaluate systematically use hybrid search
*  correctly and give your rag system access to tool calling based on 21 months of running a customer
*  support bot in production industry experts at weights and biases cohere and weaviate show you
*  how to get to a deployment grade rag application this offer includes free credits from cohere to
*  get you started make real progress on your large language model development and visit
*  w and b dot me slash cr to get started with their rag plus plus course today that's w and b dot me
*  slash cr to get started with their rag plus plus course today
*  so let's go one by one i think it is worth just breaking it down the first one on the chart is
*  llama 370b instruct rft is that a reinforcement learning fine tuning or a different kind of
*  usually it's just simple like instruction fine tuning is like the first layer of post training
*  right but it wasn't clear to me what the rft stood for in that case yeah i think it's like a
*  older algorithm i think it's a research paper i do i do think it's a reinforcement fine tuning
*  i think it's a research paper like so one of the algorithms i can read that came out last year
*  so we used it as a baseline and then we compared to the bunch of the matter telling there's a couple
*  of work from like sales force other groups and then the interesting thing was like no one kind
*  of like thought about like the directions i thought about where like how can we do more efficient
*  search and like a minor pillar of this kind of like learning and then like how do you self optimize
*  so that's reinforcement learning dpo is next i know you're right in the heart of dpo country there
*  in palo alto as maybe an aside can you help me develop my intuition for the dpo algorithm
*  i feel like i'm on a quest you know i can look at the equation and that doesn't jump out you know
*  is like super intuitive to me how would you describe in a qualitative or intuitive sense
*  what dpo is doing and like how a set of preferences on different generations is ultimately
*  being translated back into like updates to the weights of the model yeah now i was like dpo is
*  it's a very intuitive algorithm at the end of the day so when you do like supervised fine tuning
*  what you usually do is like you have a bunch of expert data this is like kind of the optimal data
*  and then training the model to be like like here's my ground truth optimal data and then you want to
*  like sort of like make the model predict behavior that's similar to it and then you're doing this
*  learning where you're doing like gradient descent to like go more closer to imitate like what the
*  ground truth data looks like so the model's predictions are similar to the ground truth
*  i think dpo i think the thing they do is i will call it like they also use the negative data in
*  a sense so they do like this kind of contrastive learning where they're like like we have some
*  positive feedback data we have some negative feedback data and then you want to do gradient
*  descent towards the positive data so we want the model to like go closer to the behavior
*  in terms of its predictions towards the positive outputs but we want to do like gradient ascent
*  on the native data so we want it to go away from the negative like behavior nothing that actually
*  probably works better because like if you're just kind of like if you think about like maybe like
*  the positive behavior is kind of a circle and the model is kind of like trying to get close to it
*  it's possible like the model might be very widespread so it's like it can cover the circle
*  but might also be very widespread outside but now when you're doing dp you're saying like here's
*  a positive stuff there's some negative stuff outside and you're taking the model the model
*  has to kind of become close the circle so it will basically have all predictions will be here so it
*  can be widespread and so i think that's a good way to think about it like you're kind of like
*  giving it more what to do and what not to do and the what not to do i think that kind of like
*  thing becomes very useful especially when you're doing this kind of reinforcement learning where
*  you're like this plus one is minus and then so i think that at the end of the day it's a very
*  intuitive algorithm and i think just beautifully fully formulated using like a lot of reinforcement
*  learning like like algorithmic literature and like principles and and then overall things like kind
*  of like gradient descent towards the positive samples gradient descent away from the negative
*  samples and then you kind of like counterbalance that by summing the sum of like all the samples
*  and dividing that formalize the factor i think that's basically dp i know in like typical
*  instruction tuning much like the pre-training it's literally just token by token evaluation right of
*  the output and then for ppo i know there's like a reward model that is responsible for sort of
*  scoring all the tokens and that reward model ultimately gives a signal of like this token
*  is really good this token is not good whatever with the dpo i understand that there is no reward
*  model and yet if i understand correctly it's like it's not just training the model to predict like
*  exactly what the tokens were right because with the negative examples like you can't just say
*  don't do that token you have to say like okay well so what right so can you give a little
*  more intuition for how if i have whole generations that are scored positively and negatively
*  how is the model understanding or how is the algorithm translating a score that is like
*  not token by token into something that can be ultimately applied token wise to update
*  weights through backpropagation so so i would say first is the initial detail that was formulated
*  i think that's our token rights so the first of the originally people from rafael rafaelico
*  so i do think that that one's you're kind of giving a positive and negative feedback
*  for each generation on the model and and so it's it basically becomes a supervised fine tuning so
*  you're saying like okay like here's this generation this gets positive score here's this generation
*  this gets negative scope and then you can kind of like just directly put that in make a simple
*  loss equation and train on that so you don't have to think about trajectories in the original
*  dpu the one modification we did in our agent queue paper was kind of like come with a trajectory
*  level dpu so when you're like working on environment you're taking multiple steps so you are not like
*  to start putting like maybe a single token and like finishing that if like keep taking a lot of
*  stuff until you reach your end state and then and then you can kind of generate a lot of territories
*  and like once you get a lot of these trajectories some trajectories and also scores from a negative
*  score and that's more close to maybe what ppo does usually in the reinforcement side
*  and then for this to work then you have to like think about like how can we apply this dp algorithm
*  on a more like a trajectory level right like all the scores are for trajectories not for individual
*  stops and i think then we propose this like trajectory level dpo that you can find in the
*  agent queue paper where like like how can this work and like how can we balance so if you have
*  like different trajectory stops and i don't think that's so there's like uh yeah so the original dp
*  i think i was calling like very simple very like it's working like per token or per stop
*  this is so you don't have to actually think of trajectories so in the original version you're
*  saying basically my positive score or my negative score is just applied to all tokens equally and
*  then that signal is propagated and that's it can you give a little more intuition for how the next
*  generation works you know this is maybe more tedious than some more interested in but i really
*  do want to continue to develop my intuition for what exactly in this as as precisely as i can
*  understand it what is the signal that we are actually sending into the model because i feel
*  like that's really helpful for at least having some foundation on which to make like guesses
*  or i wish to interpret the downstream behavior that comes from that yeah no that makes sense also
*  so at the end of the day the signal is kind of like the positive or negative score per generation
*  so i suppose like you're applying dp to a large language model and then you say like maybe like
*  i want you to maybe like say like who's the current president of the united states or something
*  and i suppose like the model knows the right answer and you can give it like this was a
*  generation so you have a plus one score but if it comes with the wrong answer then you can be like
*  like this is not correct and then you can give it a negative one and then you can do this multiple
*  times where like you can ask here you can generate 10 generations and then you can have different
*  voters different people who are like giving the score it can be the one person listening this
*  one and once you have enough of this like this for all the positive generations here's all the
*  negative generations and you put that in dp and you're like like now the goal is to improve the
*  sort of like optimize the probability of outputting the positive generations and minimize the
*  probability of outputting the negative generations okay i still want to keep studying this a little
*  bit more but maybe that i'll leave the rest for another day returning to the techniques in the
*  paper can we first just talk about like what is the definition of agent q like the just to be sure
*  i'm clear on that and then i see you know jumps off the chart that enabling the montecarlo tree
*  search drives a big boost in performance but maybe you could sort of talk about what are the
*  in addition to that like what are the biggest drivers of improved performance but first just
*  give us like what is the bundle that constitutes agent q yeah like i would say each and few again
*  this simple idea i think it's kind of like it borrows from i think richard certain's bitter lesson
*  where like the only thing that seems to work is like search and learning and i think like we were
*  kind of very inspired by that okay like even if you look at like noam brown's work at like what
*  work he did on diplomacy at matter and then like the stuff is working on currently at opening up a
*  lot of that is like like like how do you combine search and like how do you make that like use that
*  learning process to make it more intelligent like algorithms and so we did a similar thing where
*  we're like like search just seems to be very underexposed like no one has really thought
*  about like how do you do search for agents where like that seems to be like an obvious thing
*  and we're like let's can we now like come on out of this like montecarlo tree search where like it's
*  easy for the agent to go explore the state of different environments and then once we can explore
*  these environments can we get a lot of like this kind of like a positive negative reward
*  we're like so the positive generations positive like trajectories which are actually the goal
*  is for the negative trajectories which will which fail to reach the goal and once we have that then
*  can we put that in a learning process and and then like keep optimizing so it's like like maximize
*  the probability of positive territories that actually use the code minimize the probability
*  of trajectories that don't use the code and how the mcts helps is it's like we could be kind of
*  giving like okay like explore as much as possible so we're kind of like adding a lot of entropy
*  where like it's possible if you're not exploring the environment maybe just like a very narrow
*  path that the model has learned and now you just things like this is just the one thing that you
*  do on the environment space and so it just doesn't know how to memory the environment but we try to
*  add a lot of entropy to the initial exploration process so like the model is trying to go and
*  like take as many routes as possible but then over time it's finding out okay like this route
*  for like data and okay this didn't actually reach the goal so let's avoid that in the future this
*  were the positive ones let's keep doing that and that's where we like train a model that has kind
*  of seen the whole environment spritz and has learned okay like exactly like how to reach the goal
*  and and then we keep doing that and again and again until we can make this model like self-optimized
*  and better and better to maximize the probability of success so by applying all these things and I
*  didn't realize until this conversation that this was a relatively quick project with like not a ton
*  of compute presumably put into it although maybe I mean you can you could spend a lot of compute
*  today but I assume you didn't spend that much compute in just a you know a quick sprint of a
*  project like this you gradually climb all the way up you get to 95-ish percent on the one benchmark
*  that is better than human performance and this sort of gets philosophical pretty quick but
*  we see this all over the place right where it's like oh it's the ai's be humans at this benchmark
*  and that benchmark and all these benchmarks and I do take that very seriously as a signal of
*  how far we've come and yet at the same time if you just looked at all the benchmarks you would
*  think like we definitely have some sort of a gi running around and yet somehow we don't quite yet
*  so I guess first of all how do you think about that divergence between the ai performance on
*  a benchmark versus a human performance on a benchmark like it's still I assume you would
*  agree and I would say candidly in my testing of the agent like it can go do stuff you know
*  it can accomplish some tasks but I'll bet on myself in a Paul Bunyan first machine style
*  competition between me and the multi-on agent still so why do we not why do we see these
*  benchmarks with the ai's winning when it you know obviously every you know people design them to
*  try to represent the real world and I actually did go look at the the webshop thing and it like it
*  it looks like I'm pretty a little bit bare bones but like a pretty normal ish e-commerce environment
*  are people not trying I don't know I've come out you know one idea that comes to mind is maybe
*  people aren't trying that hard on the benchmarks but I don't think that's probably usually the
*  case I don't know what's your theory of the apparent divergence between what the benchmarks
*  seem to be telling us and what we actually then see in practice yeah I'll get quite like a
*  difference between our shared world scenario versus a mock scenario there's like a benchmark is a more
*  like a narrow domain like a couple of uh like the web platform the virtual environment has like maybe
*  like five six different like environments and what we also do is we're training on each different
*  environment of each different site so we can optimize the model to be very good on that site
*  when we do more like general propositions and that's working the real world like
*  until we have a leeway to go and ask like optimize this agent on every single website
*  I think like the performance won't match right because like a benchmark is just a very narrow
*  domain so it seems to saturate the benchmark for us to saturate the entire internet that is just a
*  much more challenging problem I think it's possible I think about it but I think it's just much more
*  complex and like requires more resources I do think that's kind of like where this thing
*  started emerging where like a benchmark is a like a simple simplified version of what you will see
*  in the real world but if you think about it as a vertical like here's this one narrow domain that
*  I really care about and then we take a look at the average human accuracy on the domain
*  and then we take a look at like okay what can we do with agent que style matter and then the
*  surprising result is that you can like in this narrow domain we can actually be the human and
*  and that becomes like sort of like a very interesting learning okay like now it can be
*  like a human in a very narrow domain then okay like over time you can like keep generalizing
*  and generalizing this is that you can like start beating humans and like put an emotionalized domain
*  but the question then becomes like okay like how much data do you need how much feedback do you need
*  how much scale do you need how much resources you have to throw I think that's kind of like an
*  interesting skill problem they're like like I don't think we've kind of figured out like the
*  fundamental ways to solve the problem but then you have to apply scale to make this like actually
*  is that really shy are you to the point now I mean of course this is like the big
*  there's obviously multiple big stories but I feel like a good candidate for what's different about
*  the current era of AI versus previous eras of AI is that we see positive transfer across lots of
*  things right like it used to be the case that if you tried to train a model on two tasks it
*  wouldn't be as good as two models trained on one task each now you have with foundation models this
*  sort of like foundational ability that seems to be you know rather quick to generalize to other
*  things and training on a million tasks turns out to make the million and one easier to learn
*  do you have a sense for where you go from negative to positive transfer as you scale up
*  an agent like this like I presumably doesn't happen if you go from just open table to just open
*  table plus amazon but if you keep if you just kept adding and I'm sure you've you know explored this
*  sort of thing if you just kept adding different sites is there a point where you start to see
*  positive transfer like do you have a sense for where the the threshold or the tipping point is
*  there yeah I'll definitely say so like especially suppose you have like a lot of shopping domain
*  websites you can have this like amazon or target or best buy wall mount whatever
*  the most of these are actually look similar because it's kind of like a search bar product
*  catalog when you have some sort of like digital product view check out and and and there's a lot
*  of positive transfer but like even if you obtain on one website and then you are like trying to
*  generalize it to like similar domains I think you actually get a very good transfer so I think
*  within each category I think there's a really good positive transfer and overall too I think like the
*  internet is not I think it's made for humans to use it's not that diverse if you think about like
*  the different ui's and like elements that you encounter you basically see like a lot of like
*  drop downs or draws or like navigation bars and whatever like text fields but I don't think there's
*  a lot of commonality so the model can like learn how to work on like a lot of these interfaces I
*  think there's a lot of positive transfer where you can work on new websites and then like keep
*  improving and that's also like one direction that you're very bullish on in what we're doing with
*  that being keep making this page and sputtering butter and over time I think it I do think there's
*  a scaling lock here but like once you do hit enough scale in terms of like the number of websites
*  you've trained on then you can generalize to the remaining website serial power let's come back to
*  the the scale the question of scale and the scaling laws and the possibility of bitter lessons and for
*  whom the lessons will be bitter again in a minute as well just staying on your model strategy for a
*  minute longer I'm curious what you've learned about fine tuning I feel like there are you know
*  obviously lots of different strategies for fine tuning Laura seems to have kind of become the
*  default thing because it's efficient I was a big fan or at least I was like very excited to read
*  a paper called mora from not too long ago which was an alternative that was like similar number
*  of parameters but higher rank and the math on that escapes me a little bit but conceptually
*  they reported sort of a denser fine tuning denser use more intensive use of the available
*  parameters and they did report that it was better at learning facts which I thought was really
*  interesting so interested if you've experimented with that or if you're just biting the bullet
*  and doing like full weight training yeah I don't think we see it like a lot of improvement
*  improvement just with Laura I think Laura is like very efficient it's a very good way to
*  train these models and funding them on on your application I do think there's also like a lot
*  of variants for Laura I think there's like theft Laura and like there's much of like this kind of
*  like variations and like a lot of this work really well I don't think Laura works really well there's
*  definitely a lot of this new innovation that's happening where people are coming from more
*  alternatives so I don't think that's an interesting space to watch for I think full training can help
*  is about how much data you have so if you have like a crazy amount of tokens you have like billions
*  of tokens and definitely should be like fully fine training but if you have like
*  100,000 tokens or in that magnitude I think then Laura is actually like a better method because
*  you have less parameters to optimize and so if you have less tokens less data then I think that's
*  actually a better use of that data and then you actually get better performance and but if you
*  have like billions of tokens then I think like you should be optimizing more parameters yeah I think
*  the good way to also think about this is change your last few lots so like what's the optimal data
*  for optimum number like the size of a model and so if you have like this many parameter model this
*  is the amount of data you should be throwing at this moment and I think that's a good way to
*  think about like Laura versus not Laura I guess I would maybe expect you would have billions of
*  tokens it sounds like you're not it sounds like you're not using huge data sets obviously quality
*  is a super important dimension should I infer from this that you have been just trying to optimize
*  the quality of the data set that you're working with over quantity and it's just not that big
*  that the Laura approach still is enough obviously we've tried a couple of things one thing we
*  definitely care about is speed and then if you're training over like billions of tokens that is a
*  very long process and I think so that's made some experiments have been running but others
*  we care about like quick additions and so what can we do with like a less amount of data and how
*  can you make more sufficient use of models that begin to deploy in production and then like make
*  use of for our customers so in that scenario we have found like if you look at agent cube like
*  we did like a couple of days of training and we were able to get very good performance on this
*  like nano domains it's actually is a better thing if you want to build a product for like doing like
*  pure research then I think we should be just spending like six months trying like hundreds
*  of tens of tokens and like trying to change like the best general agent possible but yeah but the
*  learning so far for us sorry I also would say for the space is like it's much easier to build a
*  network and it's also very easy to much much easier to prioritize it unless you want to be like a
*  foundation in the model company yeah okay gotcha what is your vision strategy right now is that
*  all I mean of course and by vision I mean like interpreting what the agent encounters on the
*  computer screen in the early days we were seeing lots of examples where people were trying to
*  parse the dom of the website and figure out how to like strip all the crap out of the html so that
*  would fit into the context window and now of course we've got much more in the way of multimodality
*  that we can take advantage of I mean you know in my testing I did find a couple of weird places
*  where the agent sort of got stuck and like was saying that it couldn't find something that was
*  like just plainly on the screen it wasn't clear to me if that was like just you know I don't know I
*  don't know what was happening there like was the model not able to see well or was there some sort
*  of weird situation like an iframe that would could possibly be causing some visibility issues
*  so I guess two parts of that question like what's your overall strategy for
*  interpreting the visuals and maybe what are some examples of just
*  weird challenges that pose problems you know relative to kind of the happy path that people
*  would think of first yeah so I would say at this point uh like I think we're doing a lot of hybrid
*  pipelines but I think there's a lot of like useful stuff to be taking up from the top
*  there's a lot of like meta tags and audio labels which is kind of like optimized for bots and then
*  you have a lot of like the visual data which has a lot of layouts and starts and and we're
*  doing a combination of both so we try to be hybrid where like can we expect the best of both works
*  and then can we use to to attain the models and do things um one challenge we always I think
*  this is something that throws off a lot of people is because if you're a human you kind of expect
*  this thing's doing fully work like a human right but what's happening is like the representation
*  of the screen on the ui that the agent is saying it's different from what you're seeing
*  and then and that makes like the behavior of the agent could be like a bit weird where maybe
*  it's able to click on invisible elements so it's able to make like it doesn't need to scroll down
*  it can just like kind of like see the whole like if there's a website with 10 pages maybe just is
*  able to see like all the 10 pages without needing to scroll down like a human and I think that kind
*  of like throws off like people from our spam image where you have to artificially figure out how to
*  constrain it to be more like a human and then there's also this things where maybe like you
*  might have some sort of elements which are particularly detect or identify which maybe
*  like are very obvious for a human but like like maybe the agent is not able to see that maybe
*  it's some sort of like complex seven-step issue or some kind of itrm issue I think like right now
*  we don't see a lot of that I do think like in our new prototypes I think we're just like trying a
*  lot of different things so they're not they might have some deficiencies there but I do think like
*  a lot of the major parts we have I think like we have been able to solve a lot of these things
*  over the last couple of months where like now the our pipeline for processing like the information
*  on websites I think it's it's very focused interesting I realized too there's probably
*  somewhat of an adversarial situation happening because what I was trying when I observed that
*  was and just to give people a little bit of a sense for the field so you added me to a test
*  flight where I could go you know download the in development multi-on app and then basically open
*  the app tell the agent what you want it to do it then has kind of a dual interface where it's like
*  telling you what it's doing and allowing you to you know pause it or give it additional instructions
*  feedback whatever as it goes and then if you minimize that you're just watching the screen
*  and it can also talk out loud to you so you can basically hear it narrate its progress and you're
*  watching the you know the state of the browser evolve as it goes on and does its thing well I'm
*  in Detroit and it's the day before Thanksgiving as we're recording so we've got the lions playing
*  their annual Thanksgiving day game tomorrow and the Michigan Ohio State is also this Saturday so I
*  just asked it to go get me tickets for each of these games and tried both and it was it was
*  successful in terms of like understanding my query it was successful in terms of
*  doing like an initial search it actually did a couple different approaches and different trials
*  in some cases like went to Google and searched in other cases it went like direct to a ticket site
*  from just prior knowledge it was able to search successfully on the ticket sites and then there
*  were a couple of instances where it was like those tickets were now on the screen but it would say
*  I'm having a hard time finding the tickets and especially if you're saying that's rare overall
*  I suspect that possibly part of what's going on is you know obviously these ticket companies have
*  bot wars going on for for many years now at this point where they're trying to permit people from
*  buying up and reselling and whatever I don't know expert in the tick mark ticket market but I know
*  it's complicated I guess all that is to say what do you think is the how do you describe the dynamic
*  right now maybe I didn't I wasn't thinking about this at the time but as I am thinking about it now
*  I'm thinking you could imagine this cutting multiple different ways right you might imagine
*  new auth frameworks for agents coming online and by the way I also another test I didn't have to
*  log in for these ticket sites but another test where I did need to log in to create an account
*  I tried shopping for Thanksgiving dinner on Instacart as well to do that I had to you know
*  at some point I got to a you must create an account screen and I just kind of paused and like
*  I put in my email and then you know when it sent me the confirmation I had to go get that out of
*  my email and provide that to the agent so it could provide it it was able to fill that to do those
*  steps with me putting that stuff into the chat but you could imagine like different parts of the
*  world evolving very differently where Instacart might say we want to be an aggressive early
*  adopter of whatever sort of auth paradigm is coming for agents because we obviously want people to
*  shop however they want to shop and if they want to have an agent shop for them more power to them
*  whereas a ticket master or a stub hub might say we want to ban all agents effectively because in
*  some way or other they're eating into our margins and so whatever countermeasures they might put up
*  that's a long prompt but I'd love to hear your thoughts on if you see any good auth frameworks
*  starting to emerge if you are seeing like countermeasures in the wild that you feel are
*  kind of anticipating an AI agent wave and trying to resist proactively and I guess just kind of
*  generally you know where do you see that sort of thing shaking out so let's see first one
*  definitely authentication I think it's getting more mature from I think there's a lot of like
*  authentication providers I think like uh um and on is one I think that's been trying to build a lot
*  of agent identity for browsing kind of stuff I think as there was a new one that came out agent
*  author something for the apis and like plugins integrations so I think that's a good picture
*  about a lot and I don't think that's a major enough that everyone can go and like
*  work with like some sort of authentication provider and like play it in and like you're good to go
*  but the second question becomes like okay are the current services and websites going to be adversarial
*  or cooperative I think long term they will be cooperative because I think it's kind of a win
*  win over time a short time it's hard to say because it's possible if some people might just take the
*  um uh direction on a positioning more to this is kind of like maybe harmful behavior it's kind of
*  like a more expanding and then that kind of becomes like how do you build trust how do you
*  make sure that you're like you are actually helping the website owners and the services
*  and the merchants and I don't think there's a women's situation where like as I said to make
*  sure I think it's transforming a lot of the experiences but it's like if you're a merchant
*  you still care about like the care revenue on a number of users and I think that's something
*  that begins to help I just like the I think it's like and when anything's disruptive I think it
*  takes a lot of time for that to catch on and I think we are at the start of the disruptive
*  area where like a lot of the online communication and interaction will get disrupted by it
*  and I think like there might be a lot of like initial backlash where like like this is kind
*  of dangerous and this is not safe and this is causing whatever these issues and but I think
*  over time I think it's a bit mental because it's just a different paradigm and it's a tennis
*  but if I then end long so yeah let's look ahead a little bit to the future I've got kind of
*  multiple related questions I mean you guys have been one of the most you know quick to
*  put things out there and you try anything with this and see what happens and it's been very
*  open-ended as you've described in this conversation you know you've not bucked the trend when it comes
*  to getting somewhat more narrow and being like okay you know let's really nail some
*  dialed-in use cases so where are you today on that are you working with like businesses and
*  you know if so I'd be really interested to know what sort of use cases they are finding
*  agents to be valuable for I think that's probably like the the probably the most important question
*  for all of this stuff is like where are people finding value today and then and maybe that also
*  kind of answers like why the off stuff isn't so much of a focus at the moment if it's like well
*  we're if we're working with enterprises we're in their off environment and it's a whole we don't
*  have to worry about signing into stub hub or whatever so yeah I guess I'm really interested
*  in like where you see you know you mentioned like a six month time frame what bets are you making
*  right now to you know start to bring real value to the world in the not too distant future
*  so I'll definitely say like verticals I think like more like vertical use cases that's what
*  you've been also doing internally I think I think that's the direction I'm bullish on I think the
*  agent was kind of like our first trend and the direction okay can you have vertical agents that
*  you can like train and learn on so you don't want like something that's probably hard core
*  it you don't want like something like playwright script or like scripting language that's it because
*  it's really hard core it's very like brittle it will just break all the time but you don't want
*  like some sort of like like if you want the smaller to be able to adapt so that maybe like
*  the interface change is able to like recover it's able to like like improve and but like I still
*  wanted to be like narrow now and I think like agent queue was kind of like showing okay this is kind
*  of possible and that's one thing we've been working with a lot of our clients on where like like can we
*  now ship this kind of like more narrow agents for specific use cases which could be maybe I don't
*  think it's explored a lot from the sectors so I would say like a good example is maybe like
*  restaurant reservations or if you want to do like travel kind of things if you want to do like
*  scheduling and I think there's a lot of these kind of sectors and I can't say too much about
*  the batch we're making right now and we feel like it's like like how can you kind of build
*  this kind of like agent vertical where like this agent becomes very current this particular vertical
*  and then keep optimizing it and making it into like a solid product experience and then there's
*  a lot of you have to think about enough reliability and then like optimizing for the user attraction
*  and a human in the group and much other things I think people are saying the thing about it but
*  I think it's still very early and I think like building a product is just a complex thing because
*  it's just not the agent I think it is just like a 10 or 100 more things yeah I think when what I'm
*  kind of inferring from your comments is that you're kind of finding a a third space that I
*  hadn't really considered as much where one approach would be to say here's a here's you
*  know consumer here's the do whatever you want here's our open-ended agent another one would
*  be to say we want to kind of compete in like the business process space where it's like
*  back office not visible super structured and then open table kind of represents a
*  sort of a middle ground where you might say we want to and maybe instacart would be another
*  great example of this or kayak we want to be the partner that creates an agent for your site that
*  could still be consumer facing but because we can partner with you in a deeper way we can really
*  dial in that reliability and get that product experience to be exactly what you want it to be
*  for the kayak assistant agent or the instacart agent or the open table agent or obviously people
*  can fill out the list of your crm for themselves but am i headed the right direction there that's
*  that's not what i'm reading between the lines from the h&q paper yeah yeah I do think like this can
*  be applied even to business processes of the things too because they're there too I think like if you
*  look at the current issues people have with ui path or other automation software I think just
*  take it's very brittle things like a lot of like onboarding ramp that requires like special like
*  engineers so like just really good at building this kind of like automations
*  and I think if you can decrease the complexity that also knows a lot of use cases where like
*  if you can enable anyone to build this kind of like automation even for business processes
*  and this automation is resilient then I think that also is a big enough so I don't think it
*  can be applied there and then things like maybe like interesting use cases there that we also
*  we might look into but we do at the end of the day I think like we're just trying to build something
*  that's more like like every everyday purpose in a sense would you think about being that layer for
*  some of these complicated products you know like a kayak right there's a lot of ui if you were going
*  to do a partnership with a kayak or with an open table would it still make sense to work through
*  the ui or would you start to augment the ui action space with like a specific sort of more
*  api like you know or tool kind of modality because you can imagine the agent might want to you know
*  again thinking of kayak right all the little uis in that sidebar it seems like the ais would have
*  a better job if they know that they're the kayak agent and they don't have to you know generalize
*  beyond that it seems like they might not want to go like drag the sliders for the time interval
*  that the user requested but rather just like make a sort of declarative statement to the system that
*  like I want to narrow the search in this way more kind of function calling like I realize I'm kind
*  of a couple layers of maybe speculation deeper beyond what you've explicitly confirmed but
*  how do you think about the hybrid between the fully general ui path to you know taking the
*  next step and in some cases what would seem to me more reliable of making like a function call
*  yeah I think we've been thinking about that a lot I think we have some things you're working on
*  I don't think that's an interesting action but I think it just takes a lot of time
*  I would say a good analogy here is like the thing about self-driving cars right so it's you can
*  imagine like if I was to build like a self-driving car from like sketch today my I can just say like
*  let's why not just go and construct special roads on every hybrid and this is a special like there's
*  a special lane and that's the lane is for like the self-driving car and the self-driving car just
*  uses the lane and the lane has sensors and everything ready and the self-driving car just
*  has to follow the lane and that's it like you basically don't have to do any R&D you basically
*  and you kind of want to go it's a very simple problem in terms of engineering research
*  the thing is like when you want to do something like that it's just like very complex because if
*  you change a lot of behavior it's a bit beginning for such a project everyone is sort of this kind
*  of like new thing and that will cost like everything about this will take like 10 years and like a lot
*  of like politics and like convincing people and like getting there and only that thing can do that
*  and then like a lot of self-driving cars startups decided like okay like that's probably not going
*  to happen anytime soon let's just build a car that can like let's build an autonomous car that
*  drives like a human car on any lane and let's go solve this problem using the kind of R&D and
*  that can make that work and because that's how humans like to navigate the world i think we have
*  a similar analogy here because i think like over time you might have this kind of like a spatial
*  internet infrastructure that allows agents to communicate to websites and then like do more
*  reliable function calling but again that becomes like like who has incentives so people like move
*  over that i think that it just takes a lot of time and i think i do think like this is like a
*  multi-year thing if even if you were like someone were startups and i think we've actually
*  been looking at that so i do think that could be like what the future looks like
*  but in the meantime until like everyone agrees on like the here's this new protocol and like
*  or here's how we'll do this communication and like convince everyone to adopt that protocol i
*  think like like basically being able to use these websites no matter how humans use them
*  i think that's the right way to start from because like i think that's also the battery with ai the
*  battery with ai is like whatever a human can do like for the ai i think of data and learning
*  can be able to do that and so that's how you're trying to do where like like like humans are
*  pretty good at like navigating websites with ui and so like theoretically like ai can also become
*  very very good even better and so if we can have this kind of ai which is like as good as human
*  or better i think that's a good way to solve the problem immediately and this is like how fast can
*  we get there once you get there and then you're like okay now maybe it's time for something like
*  different rate which forms like change and flip the paradigm and then i think like that will help
*  but i think that becomes like a buying problem they're like it's just like a
*  massive change in behavior and nothing that takes up time
*  a lot of these sites though do have like i'm just pushing a little bit in the middle space i mean i
*  hear you on like the road you know the dedicated lane for the self-drivers i've been calling for
*  that since i was in school and maybe that'll be one of the pleasant surprises that we get from
*  a new trump administration although i'm not holding my breath but there's been at least a
*  little talk i totally get it when you map that onto an enterprise it's like hey guys who wants
*  to implement this new agent protocol you know no hands go up or maybe one does but you know the
*  boss doesn't like it whatever i get that complexity but a lot of these sites do have like an internal
*  api right i mean isn't there something in the middle in a lot of cases that does exist like
*  what the ui talks to in many cases is an api right so is there a does it make sense in some
*  cases to just be like okay kayak you've got a real bear of a ui but this data structure
*  that manipulates is easier and this is like an actual live question for myself too i mean i'm
*  i actually have an episode coming up that i'm still putting some final touches on for people
*  that want to do what i call building software that uses itself kind of trying to coach people
*  that are building apps to create like the you know the magic ai functions that that their users have
*  always wanted even if they didn't know to ask for and that's kind of my paradigm so i wonder how you
*  react to you know i sort of see this equivalence between ui and ai not everywhere but in like a
*  lot of places and encourage developers to take advantage of that to say like okay instead of
*  asking your user to use all this ui have one button ask them what they want and then have the ai
*  translate that to the structure data that sits behind that ui now that doesn't scale super well
*  right because it that wouldn't be something you could do for every website but if you did want to
*  do a kayak or an open table partnership it seems like it would be viable and it's certainly if i'm
*  like talking to developers that are working on their own app you know should be viable for them
*  so i don't know any other reactions to that that sort of attempt to find the goldilocks zone
*  i don't think like this is again something i've thought about yeah i've been thinking about it
*  actually proposing some sort of like open standard around this where you can have like
*  like some sort of like standardized way to communicate between like agents and
*  websites and i don't think that can make a lot of sense for like all of the websites have back in
*  api that you're like directly interface with i think the biggest issue becomes like security
*  and like okay like i was like how do you see place get used who's going to call these api's
*  identification where like how do you identify who's calling these api's and there becomes like
*  patterns of use because i think if you're a website like a nbnb or doordash i think they
*  have all the patterns of use where like they know like this is basically what the user will like
*  use the website and it's a problem as a website for that particular pattern of use and then the
*  what happens is like if you transform yourself into like a api first business i think that just
*  changes a lot of paradigm because now you have to kind of fight against the product teams and maybe
*  like a lot of your front end teams and i think like the back end in your house don't want this
*  like you're exposing a lot of like security loops you have to think about sock to a bunch of things
*  so it becomes very hard for enterprise to navigate that landscape but i don't think like if you think
*  about engineering wise yes it's possible but i think it's just like a very different business
*  so patterns and i think very different security and like identity patterns which just complicates
*  events give a lot yeah gotcha how about i put a pin earlier in just like cost and latency this is
*  very common question for kind of anyone building in this space what have you learned about what
*  really matters and you said you care about speed certainly in the context of like your own development
*  iteration how much do you think this matters for the end user you know for your customers if they're
*  partner businesses and the end users what's the sort of optimization problem look like cost
*  reliability and speed and it's make for our agents or i'm just curious exactly what it might not
*  yeah i mean you can contextualize it however you want but i mean in some sense it's the you know
*  the oldest question in software right you good fast cheap pick two some would say in ai the magic
*  you can maybe have all three but you're still obviously making some trade-offs and you know
*  you said kind of 70 b is like a good compromise is that because you like have users like sitting
*  there waiting and you want to return for them quickly is it yeah so i'm just kind of curious
*  as to how you're thinking about you know what you're willing to pay in terms of financial cost and
*  latency for you know marginal improvements to reliability yeah i think it comes under the use
*  case simply if it's a high-risk use case like you want to do some sort of purchase behavior and you
*  know like i really want to confirm and make sure that we buy the right thing you don't actually
*  make the wrong purchase or like like you're doing travel or something just make sure that everything's
*  correct so how much does that matter and then because like it's a is it a soft boundary versus
*  a hard boundary so a hard boundary something like if you do it it's irreversible and it's
*  very costly to the user and you want to be like very careful like like maybe you don't really care
*  about how much time it takes can be takes me like maybe like 20 minutes or something potentially
*  that maybe it can be like more costly if you have to do more reasoning to more compute but the job
*  gets done all the time then i think a lot of people will want to live with that world compared to just
*  like yeah maybe it's very fast but it's very low reliability for like higher like this kind of like
*  hard decision boundaries there's some things which are like more sharp decision boundaries like chat
*  is a good example where like if you're taking a chatbot it's very soft decision boundary
*  because there's something irreversible about it and there's like some patterns like that like
*  suppose maybe like you're like you're doing some scheduling kind of things maybe like you
*  occasionally have some small things that you can like fix but a lot of agentic behavior is like more
*  hard decision boundaries and then so you want to be careful about okay like before you fully actuate
*  the action and like complete the task for the user that the task is actually like correctly done
*  and like before you do something a diverse and detecting is something is reversible but that is
*  also something that i think we've spent a lot of time thinking about because like if something is
*  reversible we can just have like a week like a small model and stick toward it and then it's fine
*  but if something is reversible then you like you need to build a lot of verification you make sure
*  that everything is like as good as possible and there's no ash cases and then when we're done
*  take that to the actual action yeah that's makes sense to me okay one more big question and then
*  i'll invite any other comments on things we didn't get to you know and for i should have
*  probably said this toward the top but full disclosure i'm a you know very small investor
*  in the company and i mostly don't really invest for returns so much as to support things and people
*  that i think are cool and want to see come into existence so i've been fascinated by what you've
*  been building basically since the beginning i do wonder how you think about kind of positioning
*  yourself to avoid being a casualty of the bitter lesson here we see like clod of course now has
*  computer use out and it is still not super reliable when it comes to step by step advancing
*  through tasks on the web it does bring though some like really nice advantages in terms of being like
*  an outstanding writer you know there are some like qualities of clod that are really hard to get
*  anywhere else and then of course open ai is always rumored to have something coming soon and
*  right now the rumors and hints i would say are suggesting that there's an agent framework coming
*  soon too so what is an agent company to do that hasn't raised you know 10 billion dollars to
*  compete effectively when you know they're clearly coming for you with incredible scale on some
*  timeline like again i would say it's kind of like finding the niche that you are that you want to
*  focus on and then like going up to that really now i don't think that's how like if you look at a lot
*  of the successful air products perplexity is a good example and they just chose like like such
*  are the niche and they just take force and hallucination as the one problem they were trying
*  to solve it like yeah like this problem models have issues with hallucination that is for fix
*  hallucination and that's basically what they were focusing on fully more or less and then building a
*  product experience around that because there's a good example where they're like yeah like let's
*  uh build this coding id and like that's free force and not and then they it kind of becomes
*  similar thing with the agents because computer use and the end of the day it's capability to
*  turn the product and she will have this action as a capability but then it's kind of like what's
*  the one thing that you can really clearly do to default and then how do you optimize the loop how
*  to build a product experience and the thing is like most frontier air labs are actually not
*  interested in this because like if you have hundreds of billions of dollars so you don't want to go up
*  like narrow domains like you're like i just want to throw in a computer like sort of like
*  build a general thing and it is great because that's kind of like a foundation one but then
*  i think someone needs to take that general purpose thing and build like the right product experience
*  and that kind of becomes like that unlocks a lot of like market opportunities where like like there
*  will be like a lot of like different businesses and like different use cases that will be built
*  that satisfy actual user need or like product need that is missing right now using this as
*  like a building block and i do i do think that's something that will try to happen maybe like
*  2025 because i think like this year what i called you was too early uh i mean like we were probably
*  like one of the first companies that were providing again this kind of any kind of like agent
*  capability and no one was able to build an application unless we are there in terms of
*  the technology frontier i guess it's hard to build a product right it's kind of like if you want to
*  build a card you have to first invent the view but if you feel like okay like we don't know how
*  to build a view properly or like it's like uh it's just not there then it's like you can't really
*  like like build up the product experience on that and i think that's where we have been like the
*  technology has been like just very new and then that makes it hard to build a full experience which
*  is like obviously reliable but now i think that as the technology goes better and better i think
*  like early 2025 we've seen a make up like uh i would call it an explosion of applications which
*  i don't think has happened so far if you think about agent capability i think it's still very good
*  so does that suggest that you would be open to starting to use these like is the future of
*  multi-ion like potentially powered by clod computer use and you know with that being sort of
*  you know the core capability and you being the product around it yeah again i wouldn't say too
*  much here i think there's a lot of things that are possible we have a close relationship with an
*  anthropic team i know a lot of people there and the research team and the marketing teams
*  yes i think that will say another day we are a product company and then it's kind of like like
*  what gets you across and i think we are also very innovative like so if we look at agent q and those
*  are kind of things that we are able to come up with so i do think with how this had this like kind
*  of like a rng advantage but like we are able to come with a lot of new things and then like the
*  question for us becomes as the ecosystem matures how can we combine a lot of our expertise to
*  have like a like a strategic advantage and then use that as a way to like sort of like solve a lot
*  of specific problems and i like to call this a kind of product focused research which is like
*  like you have a different problem and then you bring the research to solve this problem because
*  what happens like most of research you do even a condition they have out there in maximum is kind
*  of like the research problem is to solve it research is not directed towards anything but if
*  you're like here's this one problem that you care about it's just like the there's a missing block
*  we just don't know how to fill the block and we're like let's go and do the required nd to build
*  that block so we can fit it in and like sort of like complete the pieces of the puzzle so we can
*  reach to where we want to go i don't think we that's how we think about it like we have a lot of this
*  capability we're like a lot of things are missing even you think about right now the models and even
*  the computer use there's a lot of things that are missing and that's like how do you solve the
*  problems cool well never a dull moment it's a fast evolving landscape i think that's all the
*  questions that i had for you is there anything else that you wanted to touch on before we break
*  great time to pitch if you're hiring for any particular roles or you know looking for any
*  kinds of customers or just anything else that any other wisdom you want to impart
*  for sure no i mean definitely obviously now open for hiring i think we always think for like
*  greater people who can like raise a bar of i don't know that's always open for researchers and
*  engineers and product folks who want to like sort of work in this kind of patient domain
*  and i think i'm just really excited about like how's like applications especially like a lot
*  of the things you're working internally i think like give access to to one of the prototypes that's
*  still like a very early prototype but i think i'm very excited about like what will the right user
*  interaction and the right ways to like use this product to look like because i think that's just
*  the next wave right we're like it's like now you have the agent tech product we're like okay things
*  are happening automatically and you don't have to watch or do things all the time but maybe you
*  sometimes you want to take control sometimes you want to like maybe do things manually sometimes
*  you want maybe like you want to like learn and improve and i think just let's just take a really
*  new paradigm and i think building a really solid product there i think that's a hard challenge
*  so i think that's something that we're very very um spending a lot of time on in a sense okay like
*  how do you actually solve this problem and like how do you make this into the best interaction and
*  like the best experience and like how do you fit everything together so much maybe one more question
*  where are we a year from now that could be a multi-annual specific answer it could be an agent's
*  generally answer you kind of teased that in a little bit by saying you know 25 is the year
*  but it's what it's the year for what you know can you paint a picture of my agent assisted
*  life a year from now yeah it's i was thinking much hard to see like something like i said like
*  talbis from other than kind of things but like okay now you have this assistant you started like
*  okay like look up my files or find me this document so maybe like book this like whatever
*  like a flight for me or like do this whatever boring job and disappointment i don't think like
*  people kind of trying this say even like last year people were very bullish on like trying this kind
*  of things but just again like the technology was not there but now if you fast forward to 2025 i
*  think a lot of these things might start working and and you might start seeing that actual
*  assistants that are like useful for you are helping you in a lot of your data cave and so i'm
*  starting to get mainstream products based around agents and a lot of like this kind of like
*  explosion of like vertical applications which has not happened to the guard founder and ceo
*  of multion thank you for being part of the cognitive revolution thanks it is both energizing
*  and enlightening to hear why people listen and learn what they value about the show so please
*  don't hesitate to reach out via email at tcr at turpentine.co or you can dm me on the social
*  media platform of your choice.
