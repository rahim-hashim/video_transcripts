---
Date Generated: October 03, 2024
Transcription Model: whisper medium 20231117
Length: 4149s
Video Keywords: []
Video Views: 341
Video Rating: None
Video Description: In this special crossover episode of The Cognitive Revolution, Nathan shares an insightful conversation from the Latent.Space podcast. Swyx and Alessio interview Alistair Pullen of Cosine, creators of Genie, showcasing the cutting edge of AI automation in software engineering. Learn how Cosine achieves state-of-the-art results on the SWE-bench benchmark by implementing advanced AI techniques. This episode complements Nathan's recent discussion on AI Automation, demonstrating how far these practices can be pushed in real-world applications. Don't miss this opportunity to explore the future of AI-driven software development and its implications for businesses across industries.

Check out the Latent.Space podcast here: https://www.latent.space

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:
WorkOS: Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-Turpentine-Network

Weights & Biases Weave: Weights & Biases Weave is a lightweight AI developer toolkit designed to simplify your LLM app development. With Weave, you can trace and debug input, metadata and output with just 2 lines of code. Make real progress on your LLM development and visit the following link to get started with Weave today: https://wandb.me/cr

80,000 Hours: 80,000 Hours offers free one-on-one career advising for Cognitive Revolution listeners aiming to tackle global challenges, especially in AI. They connect high-potential individuals with experts, opportunities, and personalized career plans to maximize positive impact. Apply for a free call at https://80000hours.org/cognitiverevolution to accelerate your career and contribute to solving pressing AI-related issues.

Omneky: Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsors: WorkOS
(00:01:22) About the Episode
(00:04:29) Alistair and Cosine intro
(00:13:50) Building the Code Retrieval Tool
(00:17:36) Sponsors: Weights & Biases Weave | 80,000 Hours
(00:20:15) Developing Genie and Fine-tuning Process
(00:27:41) Working with Customer Data
(00:30:53) Code Retrieval Challenges and Solutions (Part 1)
(00:36:39) Sponsors: Omneky
(00:37:02) Code Retrieval Challenges and Solutions (Part 2)
(00:39:04) Planning and Reasoning in AI Models
(00:45:55) Language Support and Generalization
(00:49:46) Fine-tuning Experience with OpenAI
(00:52:56) Synthetic Data and Self-improvement Loop
(00:55:57) Benchmarking and SWE-bench Results
(01:01:47) Future Plans for Genie
(01:03:02) Industry Trends and Cursor's Success
(01:05:23) Calls to Action and Ideal Customers
(01:08:43) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Automating Software Engineering Genie Tops SWE-Bench, w Alistair Pullen, from Latent.Space podcast
**Cognitive Revolution:** [October 02, 2024](https://www.youtube.com/watch?v=mij1OIVmVw0)
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
*  Hello, and welcome back to the Cognitive Revolution. Today, I'm excited to share a special
*  crossover episode from the Latent Space Podcast, co-hosted by Swix and Alessio. For any that don't
*  already know, Latent Space is the number one podcast for practical insights for AI engineers.
*  And while longtime listeners may remember that the Cognitive Revolution was voted number three in
*  the same poll, and I can at times be a bit competitive about these things, in this case,
*  I have to agree with the wisdom of the crowd. The Latent Space Podcast is a regular must-listen
*  for me, and I am grateful to Swix for allowing me to share this episode here. I wanted to cross
*  post Swix and Alessio's conversation with Alistair Pullen of Cosine, makers of Genie, in particular
*  because it serves as such an excellent complement to my recent episode on AI automation. In that
*  episode, I covered the core best practices needed to automate routine business processes, which,
*  by the way, are pretty much exactly the same as you'd use to evolve a software application from
*  DIY to done-for-you by AI. And this conversation really demonstrates just how far that paradigm
*  can be pushed. Alistair and his team are implementing almost exactly what I outlined.
*  They are very thoughtfully breaking complex work into smaller AI-manageable parts,
*  curating gold standard examples, using synthetic data generation to fill in critical reasoning
*  chains, and fine-tuning intensively to achieve the desired AI behavior. They just happen to be
*  doing it with an unusually high level of ambition, a significant budget for data curation, creation,
*  and fine-tuning, and one major additional step of weaving all of the individual optimized workflows
*  together into an AI coding agent. The key takeaway here is clear. If Cosine can achieve a new state
*  of the art on the popular software engineering benchmark, Swibench, with this approach,
*  there is no reason to doubt that you can apply these techniques in your own business if you buckle
*  down and do the work. With that in mind, as I recently mentioned, I'm exploring working with
*  a few companies as an AI automation advisor. I've recently started one project helping a company
*  evolve their application from DIY to done-for-you by AI, and I have bandwidth for maybe one or two
*  more projects right now. So if you're interested, please reach out and we'll see if it makes sense
*  to work together. As always, if you're finding value in the show, we appreciate it when folks
*  take a moment to share it with friends, and we always invite your feedback and suggestions
*  either via our website, cognitiverevolution.ai, or by DMing me on your favorite social network.
*  And I really do encourage you to subscribe to the Latent Space Podcast if you haven't already.
*  Another recent episode with Michelle Pokras of OpenAI, which includes a deep dive on the
*  structured outputs API and other underappreciated features of OpenAI's APIs, was particularly
*  valuable for me. I've been using some of the techniques that they discussed in just the last
*  two weeks since that episode aired, and I have no doubt that Latent Space will once again provide
*  some of the best and most comprehensive coverage of this week's OpenAI Dev Day, which will again
*  help me raise my game. Now, I hope you enjoy this glimpse into the cutting edge of AI automation
*  with Alistair Pollin of Cosine from the Latent Space Podcast.
*  Hey everyone, welcome to the Latent Space Podcast. This is Alessio,
*  partner and CTO in residence at Decibel Partners, and I'm joined by my co-host,
*  Wix, founder of SmallAI. Hey, and today we're back in the studio in person after about three
*  to four months in visa jail and travels and all other fun stuff that we talked about in
*  the previous episode. But today we have special guests, Ali Pollin from Cosine. Welcome. Hi,
*  thanks for having me. We're very lucky to have you because you're on a two-day trip to San Francisco.
*  I would not recommend it. Don't fly from London to San Francisco for two days.
*  And you launched Genie on a plane, on plane Wi-Fi, claiming state-of-the-art in Sweet Bench,
*  which we're all going to talk about. I'm excited to dive into your whole journey because it has
*  been a journey. I've been lucky to be a small angel in part of that journey. And it's exciting to see
*  that you're launching to such a claim and such results. So I'll go over your brief background
*  and then you can sort of fill in the blanks on what else people should know about you. You did
*  your bachelor's in computer science and exeter. And then you worked at a startup that got acquired
*  into GoPuff. And around about 2022, you started working on a stealth startup that became a YC
*  startup. What's that overall story? Yeah. So basically when I left university, I met my now
*  co-founder, Sam. At the time we were both mobile devs. He was an Android developer, I was an iOS
*  developer. And whilst at university, we built this sort of small consultancy sort of, we'd be
*  approached to build projects for people. And we would just take them up and start with, they were
*  student projects. They weren't anything crazy or anything big. We started with those. And over time,
*  we started doing larger and larger projects, more interesting things. And actually when we left
*  university, we just kept doing that. We didn't really get jobs, traditional jobs. It was also
*  like in the middle of COVID, middle of lockdown. So we were like, this is a pretty good gig. We'll
*  just keep writing code in our bedrooms. And we did that for a while. And then a friend of ours that we
*  went to Exeter with started a YC startup during COVID. And it was one of these fast grocery
*  delivery companies. At the time I was living in the deepest, darkest countryside in England,
*  where fast grocery companies are still not a thing. So he sort of pitched me this idea and was like,
*  listen, I need an iOS dev, do you fancy coming along? And I thought, absolutely. It was a chance
*  to get out my parents' house, chance to move to London, do interesting things. And at the time,
*  truthfully, I had no idea what YC was. I had no idea. I wasn't in the startup space. I knew I
*  liked coding and building apps and stuff, but I'd never really done anything in that area.
*  So I said, yes, absolutely. I moved to London just sort of as COVID was ending. And yeah,
*  worked at what was fancy for about a year and a half. Then we brought Sam along as well. So
*  Sam and I were the two engineers at Fancy for basically his entire life. And we built literally
*  everything. It's like the client mobile apps, the back ends, the internal stock management system,
*  the driver routing algorithms, all those things, literally everything. It was my first... Both of
*  us were super inexperienced. We didn't have proper engineering experience. There were definitely
*  decisions we'd do differently now. We'd definitely buy a lot of stuff off the shelf, stuff like that.
*  But it was the initial dip of the toe into the world of startups. And we were both hooked
*  immediately. We were like, this is so cool. This sounds so much better than all our friends who
*  were consultants and doing normal jobs. We did that and it ran its course. And after, I want to
*  say 18 months or so, GoPuff came and acquired us. And there was obviously a transitionary period and
*  integration period with all the acquisitions. And we did that. And as soon as we'd vested what we
*  wanted to vest, and as soon as we thought, okay, this chapter is sort of done in about 2022, we left
*  and we knew that we wanted to go it alone and try something. We'd had this taste. Now we knew,
*  we'd seen how a YC startup was managed up close and we knew that we wanted to do something similar
*  ourselves. We had no idea what it was at the time. We just knew we wanted to do something. So we
*  tried some small projects in various different areas. But then Sam talked to me about GPT-3.
*  He'd seen it on Reddit and I'm his source of our knowledge. Sam loves Reddit. I'd actually heard
*  of GPT-2 and obviously had loosely followed what OpenAI had done with what was the game they
*  trained a model to play. Dota? Was it Dota? Yeah. So I followed that and I knew loosely what GPT-2
*  was. I knew what Burt was. So I was like, okay, this GPT-3 thing sounds interesting. And he just
*  mentioned it to me on a walk. And I then went home and like Googled GPT-3 and there was the
*  playground. It was the, and the model was DaVinci 2 at the time. And it was just the old school
*  playground completions, nothing crazy, no chat, no nothing. I miss completions though. Yeah,
*  old completions. Honestly, I had this conversation in OpenAI office yesterday. I was like, I just
*  went, I don't know. But yeah, so we, I started playing around with the playground and the first
*  thing I ever wrote into it was like, hello world. And it gave me some sort of like fairly generic
*  response back. I was like, okay, that looks pretty cool. The next thing was I looked through the docs
*  or they had a lot of example prompts because I had no idea. I didn't know if the, if you could
*  put anything in, I didn't know if you had to structure in a certain way or whatever. And I
*  saw that it could start writing like tables and JSON and stuff like that. So I was like, okay,
*  can you write me something in JSON? And it did. And I was like, oh wow, this is pretty cool.
*  Can you just write arbitrary JSON for me? And immediately, as soon as I realized that my mind
*  was racing and I like got Sam in and we just started messing around in the playground, like
*  fairly innocently to start with. And then of course, both being mobile devs and also seeing
*  at that point, we'd learned about what the codex model was. It was like this thing's trained to
*  write code. Sounds awesome. And copilot was start, I think I can't actually remember if copilot had
*  come out later. Yeah. It might've done. It's around about the same time. Around about the same time.
*  Yeah. And we were like, okay, as mobile devs, let's see what we can do. So the initial thing
*  was like, okay, let's see if we can get this AI to build us a mobile app from scratch.
*  We eventually built the world's most flimsy system, which was back in the day, we're like
*  4,000 token context windows, like chaining prompts, trying to keep as much context from one to the
*  other, all these different things where essentially you'd put in an app idea in a box. And then we do
*  like very high level stuff, figuring out what the stack should be, figuring out
*  what the front end should be written in, back end should be written in, all these different things.
*  And then we'd go through like for each thing, more and more levels of detail until the point that you
*  actually got codex to write the code for each thing. And we didn't do any templating or anything.
*  Like, no, we're going to write all the code from scratch every time, which is basically why it
*  barely worked. But there were like occasions where you could put in something and it would
*  build something that did actually run the back end would run the database would work. And we were
*  like, oh my God, this is insane. This is so cool. And that's what we showed to our co-founder Yang.
*  I met my co-founder Yang through Fancy because his wife was their first employee.
*  And we showed him, he was like, you've discovered Fart. What is this? This is insane. He has a lot
*  more startup experience. Historically, he's had a few exits in the past and has been through all
*  different industries. He's like our dad. He's a bit older. He hates me saying that. He's your COO now.
*  He's our COO. Yeah. And we showed him and he was like, this is absolutely amazing. Let's just do
*  something. Cause he, he at the time was just about to have a child. So he didn't have anything going
*  on either. So we applied to YC, got an interview. The interview was as most YC interviews are
*  short cut and pretty brutal. They told us they hated the idea and they didn't think it would work.
*  And that's when we started brainstorming. It was almost like the interview was like an office house
*  kind of thing. And we were like, okay, given what you know about the space now and how to build
*  things with these LLMs, like what can you bring out of what you've learned in building that thing
*  into something that might be a bit more useful to people on the daily? And also YC obviously likes
*  B2B startups a little bit more, at least at the time they did back then. So we were like, okay,
*  maybe we could build something that helps you with existing code bases, like can sort of automate
*  development stuff with existing code bases, not knowing at all what that would look like or how
*  you would build it or any of these things. And they were like, yeah, that sounds interesting.
*  You should probably go ahead and do that. You're in, you've got two weeks to build this in MVP.
*  And we were like, okay, okay. We did our best. The MVP was absolutely horrendous. It was a CLI tool.
*  It sucked. And at the time we were like, we don't even know how to build what we want to build. And
*  we didn't really know what we wanted to build, to be honest. We knew we wanted to try to help
*  automate dev work, but back then we just didn't know enough about how LLM apps were built,
*  the intricacies and all those things. And also the LLMs themselves, like 4,000 tokens,
*  you're not going very far. They're extremely expensive. So we ended up building a code
*  based retrieval tool originally. Our thought process originally was we want to build something
*  that can do our jobs for us. That is like the gold star. We know that. We've seen there are
*  glimpses of it happening with our initial demo that we did, but we don't see the path of how to
*  do that at the moment. Like the tech just wasn't there. So we were like, well, there are going to
*  be some things that you need to build this when the tech does catch up. So retrieval being one of
*  the most important things, like the model is going to have to be able to pull code out of a code base
*  somehow. So we were like, well, let's just build the tooling around it. And eventually when the
*  tech comes, then we'll be able to just like plug it into our tooling and then it should work basically.
*  And to be fair, that's basically what we've done. And that's basically what's happened,
*  which is very fortunate. But in the meantime, whilst we were waiting for everything to sort
*  of become available, we built this code base retrieval tool. That was the first thing we
*  ever launched when we were in YC, like that, and it didn't work. It was really frustrating for us
*  because it was just me and Sam like working like all hours trying to get this thing to work.
*  It was quite a big task in of itself, trying to get like a good semantic search engine working
*  that could run locally on your machine. We were trying to avoid sending code to the cloud as much
*  as possible. And then for very large code bases, you're like, you know, millions of lines of code,
*  you're trying to do some sort of local H and S W thing that runs inside your VS code instance
*  that like eats all your RAM as you've seen in the past, all those different things.
*  Yep. Yeah. My first call with you, I think I had trouble opening it.
*  Yeah, it sucks, man. I was like, yeah, I know, I know, I know it sucks. I'm sorry. But building
*  all that stuff was essentially the first six to eight months of what at the time was built.
*  Which by the way, build it. Yeah. It's terrible. Terrible.
*  That was the worst part of trying to think about whether I would invest is whether or not people
*  could pronounce the name. No, when we said when we went on our first ever YC retreat,
*  no one got the name right. They were like, build it, build, build. Well, and then we actually
*  changed the names, cosign like, although some people would spell it as in like, as if you're
*  cosigning for an apartment or something like that. It's like, can't win. Yeah. That was what built
*  was back then. But the ambition, and I did a talk on this back in the end of 2022, the ambition to
*  build something that essentially automated our jobs was still very much like core to what we
*  were doing. But for a very long time, it was just never apparent to us, how would you go about doing
*  these things? Even when you had 3.5, 16K, 16K suddenly felt huge. Because you've gone from 4
*  to 16, but even then 16K is like a lot of Python files are longer than 16K. So you can't, before
*  you even start doing a completion. Even then we were like, yeah, yeah, it looks like we're still
*  waiting. And then like, towards the end of last year, you then start, you see 32K, 32K was really
*  smart. It was really expensive, but also like, you could fit a decent amount of stuff in it. 32K felt
*  enormous. And then finally 128K came along. We're like, right, this is like, this is what we can
*  actually deal with. Because fundamentally, to build a product like this, you need to get as much
*  information in front of the model as possible and make sure that everything ever writes in output
*  can be traced back to something in the context window. So it's not hallucinating it. As soon as
*  that model existed, I was like, okay, I know that this is now going to be feasible in some way.
*  We'd done early sort of dev work on Genie using 3.5, 16K. And that was a very, very crude way of
*  proving that this loop that we were after and the way we were generating the data actually
*  had signal and worked and could do something. But the model itself was not useful because you
*  couldn't ever fit enough information into it for it to be able to do the task competently. And also
*  the base intelligence of the model. I mean, 3.5, anyone who's used 3.5 knows the base intelligence
*  of the model is lacking, especially when you're asking it to like do software engineering,
*  it's just quite involved. So we saw the 128K context model. And at that point, we'd been in
*  touch with OpenAI about our ambitions and how we wanted to build it. We essentially just took a
*  punt and I was like, I'm just going to ask to see, can we train this thing? Because at the time,
*  Fortubo had just come out. And back then there was still a decent amount of lag time between
*  OpenAI releasing a model and then allowing you to fine tune it in some way. They've gotten much
*  better about that recently. 4.0 fine tuning came out either, I think, a day, 4.0 mini fine tuning
*  came out a day after the model did. And I know that's something they're definitely optimizing
*  for super heavily inside, which is great to see. Hey, we'll continue our interview in a moment
*  after a word from our sponsors. Today's episode is brought to you in part by Weights and Biases.
*  As a developer, the journey from concept to production ready large language model apps
*  is fraught with challenges. Dealing with unpredictable large language model outputs,
*  correctly handling PII and ballooning API costs can all be blockers to shipping your next AI
*  powered feature. Weights and Biases Weave is a lightweight AI developer toolkit designed
*  to simplify your large language model app development. With Weave, you can trace and
*  debug input, metadata, and output with just two lines of code. Weave helps you run rigorous
*  evaluations and securely manage all of your data sets and system configurations. So you can focus
*  on what matters most, iterating and improving on your large language model powered applications.
*  Plus, Weave integrates seamlessly with your favorite APIs and libraries, including OpenAI,
*  Anthropic, Mistral, Cohere, Langchain, Llama Index, and more. So make real progress on your
*  large language model development. Visit wnb.me.cr to get started with Weave today. That's wnb.me.cr
*  and thanks to Weights and Biases for sponsoring this episode. I am really excited that our new
*  sponsor, 80,000 Hours, is now offering free one-on-one career advising sessions to Cognitive
*  Revolution listeners. 80,000 Hours aims to be the best source of advice for people who want to do
*  the most good that they possibly can with their careers. We typically work for about 40 years in
*  our lifetime and we work about 2,000 hours per year. That is the single biggest opportunity that
*  most of us have to make a positive contribution and it's worth being strategic about it. That's
*  where 80,000 Hours can help. I actually used their career advising service myself. Two years ago,
*  I had just finished the GPT-4 Red Teaming project and I wanted to do anything I could to nudge the AI
*  future in a positive direction. But what could or should I do? That was not clear. After my call
*  with 80,000 Hours, I got a number of connections to outstanding individuals in the space and over
*  the course of the follow-on conversations, I developed confidence that this podcast was one
*  of the projects that I should pursue. Today, I'm thrilled to have built an audience of thoughtful,
*  high potential people that 80,000 Hours wants to help. To request a free one-on-one career
*  advising session, follow the link in the show notes. It's 80,000hours.org slash cognitive
*  revolution. That's 80,000hours.org slash cognitive revolution. Sign up for a free one-on-one career
*  advising session. Figure out how you can make a positive impact on the AI future and I think
*  you'll be glad that you did. Which is a little bit, you know, for a year or so,
*  YC companies had like a direct Slack channel to open AI. We still do. Yeah. Yeah. So it's a
*  little bit of a diminishing of the YC advantage there. Yeah. If they're releasing this fine
*  tuning ability like a day after. Yeah, no, no, absolutely. But like, you can't build a startup
*  on the YC advantage. It's obviously nice. It makes you feel warm and fuzzy inside. But like,
*  at the end of the day, it's not that that's going to make you win. But yeah, no. So like we'd spoken
*  to Shamil there, the DevRel guy. I'm sure you know him. He's the head of solutions or something. He
*  is in their applied team. Yeah. We'd been talking to him from the very beginning when we got into
*  YC and he's been absolutely fantastic throughout. I basically had pitched him this idea back when
*  we were doing it on 3.5, 16K. And I was like, this is my crazy thesis. I want to see if this can work.
*  And as soon as like that 128K model came out, I started like laying the groundwork. I was like,
*  I know this definitely isn't possible because you released it like yesterday, but know that I want
*  it. And in the interim, like GPT-4, like 8K fine tuning came out. We tried that. It's obviously
*  even fewer tokens, but the intelligence helped. And I was like, if we can marry the intelligence
*  and the context window length, then we're going to have something special. And eventually we were
*  able to get on the experimental access program and we got access to four turbo fine tuning.
*  As soon as we did that, because in the entire ramp to that, we'd built the data pipeline.
*  We already had the last set up. So we're like, right, we have the data. Now we have the model.
*  Let's put it through and, and literate essentially. And that's, that's where like
*  genie is. We know it today really was born. I won't pretend like the first version of gene
*  that we trained was good. It was disaster. That's where you realize all the implicit biases in your
*  data set. And you realize that, oh, actually this decision you made that was fairly arbitrary was
*  the wrong one. You have to do it a different way. Other subtle things like, you know, how you write
*  get diffs in using LLMs and how you can best optimize that to make sure they actually apply
*  and work and loads of different little edge cases. But as soon as we had access to the underlying
*  tool, we were like, right, we can actually do this. And I was, I breathe a sigh of relief because I
*  didn't know it was like, it wasn't a done deal, but I knew that you could build something useful.
*  And I knew that we could build something that would be measurably good on whatever eval at the
*  time that you wanted to use. Like at the time back then we weren't actually that familiar with
*  but once Devin came out and they announced their sweet bench, I was like, that's when my life took
*  a turn. Challenge accepted. Yeah, challenge accepted. And that's where like, yes, that's
*  where my friendships have gone. My sleep has gone, my weight, everything got into sweet bench. And
*  yeah, we, it was actually a very useful tool in building genie because beforehand it was like,
*  yes, vibe check this thing and see if it's useful. And then all of a sudden you have an actual measure
*  to see like, couldn't it do software engineering? Not the best measure, obviously, but like it's
*  the best that we've got now. We would just iterate it and build and eventually we got it to the point
*  where it is now and a little bit beyond since we actually like, we actually got that score a couple
*  of weeks ago. And yeah, it's been a hell of a journey from the beginning all the way now. That
*  was a very rambling answer to your question about how we got here, but that's essentially the potted
*  answer of how we got here. Got the full origin story. Yeah, no, totally. You mentioned bias in
*  the data and some of these things in your announcement video, you called genie the worst
*  first AI software engineering colleague, and you kind of highlighted how the data needed to train
*  it needs to show how human engineer works. I think maybe you're contrasting that to just putting code
*  in it. There's kind of like a lot more than code that goes into software engineering. How do you
*  think about the data mixture? You know, and like, there's this kind of known truth that code makes
*  models better when you put in the pre-training data, but since we put so much in the pre-training
*  data, what else do you add when you turn to genie? Yeah, I think that sort of boils down
*  fundamentally to the difference between a model writing code and a model doing software engineering,
*  because the software engineering sort of discipline goes wider because if you look at something like
*  a PR, that is obviously a artifact of some thought and some work that has happened and has eventually
*  been squashed into some diffs. What the very crudely, what the pre-trained models are reading
*  is they're reading those final diffs and they're emulating that and they're being able to output
*  it. But of course it's a super lossy thing, a PR. You have no idea why or how for the most part,
*  unless there are some comments, which anyone who's worked in a company realizes PR reviews can be a
*  bit dodgy at times, but you see that you lose so much information at the end and that's perfectly
*  fine because PRs aren't designed to be something that perfectly preserves everything that happened.
*  What we realized was if you want something that's a software engineer, and very crudely we started
*  with something that can do PRs for you essentially, you need to be able to figure out why those things
*  happened. Otherwise, you're just going to rely, essentially you just have a code writing model.
*  You have something that's good at human eval, but not very good at sweet bench essentially.
*  That realization was part of the kernel of the idea of the approach that we took to design the
*  agent that is Genie. The way that we decided we want to try to extract what happened in the past,
*  as forensically as possible, has been and is currently one of the main things that we focus
*  all our time on. Because getting as much signal out as possible and doing that as well as possible
*  is the biggest thing that we've seen that determines how well we do on that benchmark
*  at the end of the day. Once you've sorted things out like output structure, how to get it consistently
*  writing diffs and all the stuff that is sort of ancillary to the model actually figuring out how
*  to solve a problem, the core bit of solving the problem is how did the human solve this problem
*  and how can we best come up with how the human solved these problems. So all the effort went
*  in on that pipeline. The mix that we ended up with was, as you've probably seen in the technical
*  report and so on, all of those different languages and different combinations of different task types,
*  all of that has run through that pipeline and we've extracted all that information out.
*  How does that differ when you work with customers that are private
*  workflows? Is there usually a big delta between what you get in open source and maybe public data?
*  When you scrape enough of it, most of open source is updating readmes and docs. It's hilarious.
*  We had to filter out so much of that stuff because when we first did the 3.5 16k model,
*  the amount of readme updating that went in, we did no data cleaning, no real like,
*  we just sort of threw it in and saw what happened. It was really good at updating readmes,
*  really good at writing some comments, really good at complaining in PR reviews. Again,
*  we didn't clean the data, so you'd give it some feedback and it would just reply and
*  it would just be quite insubordinate when it was getting back to you. Like,
*  now I don't think you're right. They would just sort of argue with you.
*  The process of doing all that was super interesting because we realised from the
*  beginning that, okay, there's a huge amount of work that needs to go into cleaning this,
*  getting it aligned with what we want the model to do to be able to get the model to be useful
*  in some way. I'm curious, how do you think about the customer willingness to share all of this
*  historical data? I've done a lot of developer tools investing in my career and getting access
*  to the code base is always one of the hard things. Are people getting more cautious about sharing
*  this information? In the past, it was maybe like, you're using static analysis tool,
*  whatever else you need to plug into the code base, fine. Now you're building a model based on it.
*  What's the discussion going into these companies? Are most people comfortable with letting you see
*  how they work and sharing everything? It depends on the sector mostly. We've actually seen,
*  I'd say, people becoming more amenable to the idea over time, actually, rather than more skeptical,
*  because I think they can see the upside. If this thing does what they say it does, it's going to be
*  more help to us than it is a risk to our infosec. Of course, companies building in this space,
*  we're all going to end up complying with the same rules and there are going to be new rules that
*  come out to make sure that we're looking at your code, that everything is safe and so on.
*  From what we've seen so far, we've spoken to some very large companies that you've definitely
*  heard of and all of them obviously have stipulations and many of them want it to be sandboxed to start
*  with and all the very obvious things that I would say as well. But they're all super keen
*  to have a go and see because despite all those things, if we can genuinely make them go faster,
*  allow them to build more in a given time period and stuff, it's super worth it to them.
*  Okay. I'm going to dive in a little bit on the process that you have created. You showed the
*  demo on your video and by the time that we release this, you should be taking people off the waitlist
*  launching people so people can see this themselves. There's four main parts of the workflow,
*  which is finding files, planning action, writing code and running tests. And controversially,
*  you have set yourself apart from the devins of the world by saying that things like having access
*  to a browser is not that important for you. Is that an accurate reading of what you wrote?
*  I don't remember saying that, but at least with what we've seen, the browser is helpful,
*  but it's not as helpful as like ragging the correct files. If that makes sense. It is still
*  helpful, but obviously there are more fundamental things you have to get right before you get to
*  like, oh yeah, you can read some docs or you can read a Stack Overflow article and stuff like that.
*  Yeah. The phrase I was indexing on was the other software tools are wrappers around foundational
*  models with a few additional tools such as a web browser or code interpreter.
*  Oh, I see. No, I mean, no, I'm deriding the approach there, not the tools.
*  Exactly. So like I would say in my standard model of what a code agent should look like,
*  Devin has been very influential, obviously, because you could just add the docs of something.
*  When I'm installing a new library, I can just add docs and Cursor also does this. And then obviously
*  having a code interpreter does help. I guess you have that in the form of running tests.
*  Genie has both of those tools available to it as well. So we have a tool where you can like
*  put in URLs and it will just read the URLs and it also uses Potexity's API under the hood as well
*  to be able to actually ask questions if it wants to. So no, we use both of those tools as well.
*  Those tools are super important and super key. I think obviously the most important tools to
*  these agents are like being able to retrieve code from a code base, being able to read Stack Overflow
*  articles and what have you and just be able to essentially be able to Google like we do is
*  definitely super useful. Yeah. I thought maybe we could just kind of dive into each of those actions
*  code retrieval. One of the core problems you had at Indexer that you've worked on even as built.
*  What makes it hard? What approach you thought would work, didn't work, anything like that.
*  It's funny, I had a similar conversation to this when I was chatting to the guys from OpenAI
*  yesterday. The thing is that searching for code specifically semantically, at least to start with,
*  I mean like keyword search and stuff like that is a sole problem has been around for ages, but
*  at least being able to, the phrase we always used back in the day was searching for what code does
*  rather than what code is, like searching for functionality is really hard, really hard.
*  The way that we approached that problem was that obviously like a very basic and easy approach is
*  right, let's just embed the code base, we'll chunk it up in some arbitrary way, maybe using an AST,
*  maybe using a number of lines, maybe using whatever, like some overlapping, just chunk it up and embed
*  it. Once you've done that, I will write a query saying like find me some authentication code or
*  something, embed it and then do the cosine similarity and get the top K right. That doesn't work,
*  I wish it did work, don't get me wrong. It doesn't work well at all because fundamentally,
*  if you think about like semantically how code looks is very different to how English looks and
*  there's like not a huge amount of signal that's carried between the two. So what we ended up,
*  the first approach we took and that kind of did well enough for a long time was, okay, let's train
*  a model to be able to take in English code queries and then produce a hypothetical code snippet that
*  might look like the answer, embed that and then do the cosine similarity. And that process,
*  although very simple, gets you so much more performance out of the retrieval accuracy.
*  And that was kind of like the start of our engine, as we called it, which is essentially like the
*  aggregation of all these different heuristics, like semantic, keyword, LSP and so on. And then
*  we essentially had like a model that would, given an input, choose which ones it thought were most
*  appropriate, given the type of requests you had. So the whole code search thing was a really hard
*  problem. And actually what we ended up doing with Genie is we let the model through self-play figure
*  out how to retrieve code. So actually we don't use our engine for Genie. So instead of like a request
*  coming in and then like say GPT-4 with some JSON output being like, well, I think here we should
*  use a keyword with these inputs and then we should use semantic and then we should like pick these
*  results. It's actually like a question comes in and Genie has self-played in its training data to
*  be able to be like, okay, this is how I'm going to approach finding this information, much more
*  akin to how a developer would do it. Cause if I was like, Sean, go into this new code base you've
*  never seen before and find me the code that does this, you're gonna probably, you might do some
*  keywords, you're going to look over the file system, you're going to try to figure out from
*  the directories and the file names where it might be. You're going to like jump in one and then once
*  you're in there, you're probably going to be doing the, you know, go to definition stuff to like jump
*  from file to file and try to use the graph to like get closer and closer. And that is exactly
*  what Genie does. Starts on the file system, looks at the file system, picks some candidate files.
*  Is this what I'm looking for? Yes or no. If there's something that's interesting, like an import or
*  something, it can command click on that thing, go to definition, go to references and so on.
*  And it can traverse the code base that way. Are you using the VS code LSP or? No, that's no,
*  that we're not doing this in VS code, we're just using the language servers running. But we really
*  wanted to try to mimic the way we do it as best as possible. And we did that during the self play
*  process when we were generating the data set. So although we did all that work originally,
*  and although like Genie still has access to these tools, so it can do keyword searches and it can do
*  you know, basic semantic searches, and it can use the graph, it uses them through this process and
*  figures out, okay, I've learned from data how to find stuff in code bases. And I think in our
*  technical report, I can't remember the exact number, but I think it was around 65 or 66% retrieval
*  accuracy overall, measured on we know what lines we need for these tasks to find for the task to
*  actually be able to be completed. And we found about 66% of all those lines, which is one of
*  the biggest areas of free performance that we can get hold of. Because when we were building Genie
*  truthfully, like a lot more focus went on, assuming you found the right information, you've been able
*  to reproduce the issue, assuming that's true, how do you then go about solving it and the bulk of
*  the work we did was on the solving. But when you go higher up the funnel, obviously, like the funnel
*  looks like, have you found everything you need for the task? Are you able to reproduce the problem
*  that's seen in the issue? Are you then able to solve it and the funnel gets narrowed as you go
*  down? And at the top of the funnel, of course, is rank. So I'm actually quite happy with that
*  score. I think it's still pretty impressive considering the size of some of the code bases
*  we're doing, we're using for this. But as soon as that if that number becomes 80, think how many
*  more tasks we get right. That's one of the key areas we're going to focus on when we continue
*  working on Genie. It'd be interesting to break out a benchmark just for that.
*  Because I don't know what state of the art is. Yeah, I mean, like for a, it's super easy because
*  like for a given PR, you know what lines were edited. Oh, okay. Yeah. You can source it from
*  cbench actually. Yeah, you can do it super easily. And that's how we got that figure out at the other
*  end. For us being able to see it against our historic models were super useful so we could
*  see if we were, you know, actually helping ourselves or not. And initially, one of the
*  biggest performance gains that we saw when we were working, when we did work on the rag a bit was
*  giving it the ability to use the LSP to like go to definition and really try to get it to emulate
*  how we do that. Because I'm sure when you go into an editor without where like the LSP is not working
*  or whatever, you suddenly feel really like disarmed and naked. You're like, oh my God,
*  I didn't realize how much I actually use this to get about rather than just find stuff. So we really
*  tried to get it to do that. And that gave us a big jump in performance. So we went from like 54% up
*  to like the 60s. But just by adding focusing on that. Hey, we'll continue our interview in a moment
*  after a word from our sponsors. Omniki uses generative AI to enable you to launch hundreds
*  of thousands of ad iterations that actually work customized across all platforms with a click of a
*  button. I believe in Omniki so much that I invested in it. And I recommend you use it to use cog rev
*  to get a 10% discount. That's one weird trick. Yes. I'll briefly comment here. So this is the
*  standard approach I would say most code tooling startups are pursuing. The one company that's not
*  doing this is magic.dev. Yes. So would you do things differently if you have a 10 million token
*  context window? If I had a 10 million context window and hundreds of millions of dollars,
*  I wouldn't have gone and built a, it's an LTM. It's not a transformer, right? That they're using,
*  right? If I'm not mistaken, I believe it's not a transformer. Eric's going to come on at some
*  point. I'm just listening. They obviously know a lot more about their product than I do. I don't
*  know a great deal about how magic works. I'm not going to speculate. Would I do it the same way as
*  them? I like the way we've done it because fundamentally like we focus on the act of
*  software engineering and what that looks like and showing models how to do that.
*  Fundamentally, the underlying model that we use is kind of null to us. So long as it's the best one,
*  I don't mind. And the context windows, we've already seen how you can get transformers to
*  have like 1.5 million token context windows. And that works perfectly well. So as soon as you can
*  fine tune Gemini 1.5, then you best be sure that Genie will run on Gemini 1.5 and we'll probably
*  get very good performance out of that. I like our approach because we can be super agile and be
*  like, oh, well, Anthropic have just released whatever, you know, and it might have half a
*  million tokens and it might be really smart. And I can just immediately take my JSONL file and just
*  dump it in there. And suddenly Genie works on there and it can do all the new things.
*  Does Anthropic have the same fine tuning support as OpenAI?
*  I actually haven't heard any.
*  They are working on it. They are partnered with AWS and it's going to be in Bedrock.
*  As far as I know, I think that's true.
*  Cool. We have to keep moving on to the other segments. Planning. The second piece of your
*  four-step Grandmaster plan. That is the frontier right now. You know, a lot of people are talking
*  about Strawberry, Q-Star, whatever that is. Monte Carlo Tree Search. Is current state of the art
*  planning good enough? What prompts have worked? I don't even know what questions to ask. Like,
*  what is the state of planning?
*  I think it's fairly obvious that with the foundational models, like you can ask them
*  to think by step by step and ask them to plan stuff, but that isn't enough. Because if you
*  look at how those models score on these benchmarks and then they're not even close to state of the
*  art. Which ones are you referencing?
*  So like just like Sweet Bench and so on. And like even the things that get really good scores on
*  human Eval or agents as well, because they have these loops. Obviously these things can
*  reason quote unquote, but the reasoning is the model. It's constrained by the model's intelligence,
*  I'd say very crudely. And what we essentially wanted to do was we still thought obviously
*  reasoning is super important. We need it to get the performance we have, but we wanted the
*  reasoning to emulate how we think about problems when we're solving them, as opposed to how a
*  model thinks about a problem when we're solving it. And that was, that's obviously part of like
*  the derivation pipeline that we have when we design our data. But the reasoning that the models do
*  right now and who knows what Q star, whatever ends up being called looks like. But certainly what I'm
*  excited on a small tangent to that, like what I'm really excited about is when models like that come
*  out, obviously the signal in my data, when I regenerate it goes up and then I can then train
*  that model that's already better at reasoning with improved reasoning data. And just like I can keep
*  bootstrapping and keep leapfrogging every single time. And that is like super exciting to me,
*  because I welcome like new models so much because immediately it just floats me up without having to
*  do much work, which is always nice. But at the state of reasoning generally, I don't see it going
*  away anytime soon. I mean, that's like an autoregressive model doesn't think per se.
*  And in the absence of having any thought, maybe an energy based model or something like that,
*  maybe that's what Q star is, who knows some sort of like high level abstract space where thought
*  happens before tokens get produced. In the absence of that for the moment, I think it's all we have
*  and it's going to have to be the way it works for what happens in the future. We'll have to see,
*  but I think certainly it's never going to hinder performance to do it. And certainly the reasoning
*  that we see Genie do when you compare it to like, if you ask GPT-4 to break down step by step an
*  approach for the same problem, at least just on a vibe check alone looks far better.
*  Two elements that I like that I didn't see in your initial video, we'll see when you know,
*  Genie launches is a planner chat, which is I can modify the plan while it's executing. And then
*  the other thing is playbooks, which also from Devin, where here's how I like to do a thing and
*  I'll use Markdown to specify how I do it. I'm just curious if like, you know, those things help.
*  Yeah, no, absolutely. We're 100%. We want everything to be editable. Not least because
*  it's very frustrating when it's not. Like if you're ever in a situation where like,
*  there's the one thing I just wish I could, and you'd be right if that one thing was right and
*  you can't change it. So we're going to make everything as well, including the code it writes.
*  Like you can, if it makes a small error in a patch, you can just change it yourself and let
*  it continue and it will be fine. So yeah, like those things are super important. We'll be doing
*  those too. I'm curious once you get to writing code, is most of the job done? I feel like the
*  models are so good at writing code when they're like in small chunks that are like very well
*  instructed. What's kind of the drop off in the funnel? Like once you get to like, you got the
*  right files and you got the right plan. That's a great question because by the time this is out,
*  there'll be another blog post. Yeah. Which contains all the information, all the
*  learnings that I delivered to OpenEye's fine tuning team when we finally got the score.
*  Go for it. It's already out. Yeah. I don't have it on my phone, but basically I broke down
*  the log probes. I basically got the average log prob for a token at every token position in the
*  context window. So imagine an X axis from zero to 128 K and then the average log prob for each
*  index in there. As we discussed, like the way Genie works normally is, you know, at the beginning,
*  you do your rag and then you do your planning and then you do your coding and that sort of cycle
*  continues. The certainty of code writing is so much more certain than every other aspect of Genie's
*  loop. So whatever's going on under the hood, the model is really comfortable with writing code.
*  There is no doubt. And it's like in the token probabilities. One slightly different thing,
*  I think, to how most of these models work is at least for the most part, if you ask GPT-4
*  in TrackGPT to edit some code for you, it's going to rewrite the entire snippet for you with the
*  changes in place. We train Genie to write diffs and, you know, essentially patches, right? Because
*  it's more token efficient and that is also fundamentally, we don't write patches as humans,
*  but it's like the result of what we do is a patch, right? When Genie writes code, I don't
*  know how much it's leaning on the pre-training, like code writing corpus, because obviously it's
*  just read code files there. It's obviously probably read a lot of patches, but I would wager it's
*  probably read more code files than it has patches. So it's probably leaning on a different part of
*  its brain is my speculation. I have no proof for this. So I think the discipline of writing code
*  is slightly different, but certainly is its most comfortable state when it's writing code. So once
*  you get to that point, so long as you're not too deep into the context window, another thing that
*  I'll bring up in that blog post is performance of Genie over the length of the context window
*  degrades fairly linearly. So actually, I actually broke it down by probability of solving a
*  sui bench issue, given the number of tokens of the context window at 60k, it's basically 0.5.
*  So if you go over 60k in context length, you are more likely to fail than you are to succeed just
*  based on the amounts of tokens you have on the context window. And when I presented that to the
*  fine tuning team at OpenAI, that was super interesting to them as well. And that is more of a
*  foundational model attribute than it is an us attribute. However, the attention mechanism
*  works in GPT-4. However, they deal with the context window at that point is influencing how
*  Genie is able to form. Even though obviously all our training data is perfect, right? So even if
*  stuff is being solved in 110,000 tokens, sort of that area, the training data still shows it
*  being solved there. But it's just in practice, the model is finding it much harder to solve stuff
*  down that end of the context window. That's the scale with the context. So for a 200k context size
*  is 100k tokens like the 0.5? I don't know. Yeah, but I hope not. I hope you don't just take the
*  context length and halve it and then see, oh, this is the usable context length. But what's been
*  interesting is knowing that actually really digging into the data, looking at the log
*  probes, looking at how it performs over the entire window, it's influenced the short term
*  improvements we've made to Genie since we got that score. So we actually made some small optimizations
*  to try to make sure as best we can without overdoing it, trying to make sure that we can
*  artificially make sure stuff sits within that sort of range because we know that's our sort of
*  balazone. And if we go outside of that, we're starting to push the limits and we're more likely
*  to fail. So just doing that sort of analysis has been super useful without actually messing with
*  anything more structural and getting more performance out of it. What about different
*  languages? So in your technical report, the data makes us 21% JavaScript, 21% Python, 14% TypeScript,
*  14% TSX, which is JavaScript, JavaScript. Yes, it's like 49% JavaScript. That's true. Although
*  TypeScript is so much superior, but anyway. Do you see how good is it at just generalizing? If
*  you're writing Rust or C++ or whatever else, it's quite different. It's pretty good at generalizing.
*  Obviously, I think there's 15 languages in that technical report that we've covered. The ones that
*  we picked in the highest mix were the ones that selfishly we internally use the most and also
*  I'd argue some of the most popular ones. When we have more resource as a company and more time and
*  once all the craziness that has just happened sort of dies down a bit, we are going to work on that
*  mix. I'd love to see everything ideally be represented in a similar level as it is. If you
*  took GitHub as a data set, if you took like how are the languages broken down in terms of popularity,
*  that would be my ideal data mix to start. It's just that it's not cheap doing all this. So yeah,
*  trying to have an equal amount of Ruby and Rust and all these different things is just at our
*  current state is not really what we're looking for. There's a lot of good Ruby in my GitHub profile.
*  You can have it all. Well, okay, we'll just train on that. For running tests, it sounds easy, but it
*  isn't, especially when you're working in enterprise code bases that are kind of like very hard to spin
*  up. How do you set that up? It's like how do you make a model actually understand how to run a code
*  base, which is different than writing code for the code base? The model itself is not in charge of
*  setting up the code base and running it. So Genie sits on top of GitHub. And if you have CI running
*  GitHub, you have GitHub actions and stuff like that, then Genie essentially makes a call out to
*  that, runs your CI, sees the outputs, and then moves on. Making a model itself set up a repo
*  wasn't scoped in what we wanted Genie to be able to do because for the most part,
*  at least most enterprises have some sort of CI pipeline running. If you're doing some even
*  like a lot of hobbyist software development, it has some sort of basic CI running as well.
*  And that was the lowest hanging fruit approach that we took. So when Genie ships, the way it
*  will run its own code is it will basically run your CI and it will take the... I'm not in charge
*  of writing this, the rest of the team is, but I think it's the checks API on GitHub allows you to
*  grab that information and throw it in the context window. What's the handoff like with the person?
*  So Genie, you give it a task and then how long are you supposed to supervise it for? Or are you
*  just waiting for the checks to eventually run and then you see how it goes? What does it feel like?
*  There are a couple of modes that it can run in. Essentially, it can run in fully headless,
*  autonomous modes. So say you assign it a ticket in linear or something, then it won't ask you
*  for anything. It will just go ahead and try. Or if you're in the GUI on the website and you're
*  using it, then you can give it a task and it might choose to ask you a cloud-frying question.
*  If you ask it something super broad, it might just come back to you and say,
*  what does that actually mean? Or can you point me in the right direction for this? Because our
*  decision internally was it's going to piss people off way more if it just goes off and makes a
*  completely ruined attempt at it because it just from day one got the wrong idea. So it can ask
*  you follow-up questions. And once it's going much like a regular PR, you can leave review comments,
*  issue comments, all these different things. And it, because it's been trained to be a software
*  engineering colleague, responds in actually a better way than a real colleague because it's
*  less snarky and less high and mighty. And also the amount of filtering it has to do for LGTM.
*  When you train a model to be a software engineer, essentially it's like you can just do anything.
*  It's like, yeah, it looks good to me, bro. It's shipping.
*  I just wanted to dive in a little bit more on your experience with the fine-tuning team. John
*  Allard was publicly sort of very commentary supportive and was part of it. Was it working
*  with them? I also picked up that you initially started to fine-tune what was publicly available,
*  the 16 to 32k range. You got access to do more than that. You've also trained on billions of
*  tokens instead of the usual millions range. Just take us through that fine-tuning journey and any
*  advice that you may have. It's been so cool. And this will be public by the time this goes out.
*  OpenAI themselves have said we are pushing the boundaries of what is possible with fine-tuning.
*  We are right on the edge and we are genuinely working with them in figuring out how stuff works,
*  what works, what doesn't work, because no one else is doing what we're doing. They have found
*  what we've been working on super interesting, which is why they've allowed us to do so much
*  interesting stuff. Working with John, I had a really good conversation with John yesterday.
*  We had a little brainstorm after the video we shot. You mentioned the billions of tokens.
*  One of the things we've noticed, and it's actually a very interesting problem for them as well,
*  when you're building a self-serve fine-tuning API, they have to decide how big your PATH adapter,
*  your LoRa adapter is going to be in some way. Figuring that out is actually a really interesting
*  problem because if you make it too big, because they support data sets that are so small, you can
*  put 20 examples through it or something like that. If you had a really sparse large adapter,
*  you're not going to get any signal in that at all. They have to dynamically size these things.
*  There is an upper bound. Actually, we use models that are larger than what's publicly available.
*  We're not in publicly available yet, but when this goes out, it will be. We have larger
*  LoRa adapters available to us just because of the amount of data that we're pumping through it.
*  At that point, you start seeing really interesting other things like you have to change your learning
*  rate schedule and do all these different things that you don't have to do when you're on the
*  smaller end of things. Working with that team is such a privilege because obviously they're
*  at the top of their field in the fine-tuning space. As we learn stuff, they're learning stuff.
*  One of the things that I think really capitalizes this relationship is when we first started
*  working on Genie, I delivered them a presentation, which will eventually become the blog post that
*  you'll love to read soon. The information I gave them there, I think, is what showed them,
*  oh wow, okay, these guys are really pushing the boundaries of what we can do here.
*  Truthfully, our data set, we view our data set right now as very small. It's like the minimum
*  that we're able to afford, literally afford right now to be able to produce a product like this.
*  It's only going to get bigger. Yesterday, while I was in their offices, I was basically,
*  so we were planning, we were like, okay, how this is where we're going in the next six to 12 months.
*  We're putting our foot on the gas here because this clearly works. I've demonstrated this is
*  the best approach so far. I want to see where it can go. I want to see what the scaling law
*  is like for the data. At the moment, it's hard to figure that out because you don't know when
*  you're running into saturating a PEFT adapter as opposed to actually, is this the model's limit?
*  Where is that? Finding all that stuff out is the work we're actively doing with them.
*  It's going to get more and more collaborative over the next few weeks as we explore larger adapters,
*  pre-training extension, different things like that. Awesome. I also wanted to talk briefly about the
*  synthetic data process. One of your core insights was that the vast majority of the time, the code
*  that is published by a human is in a working state. Actually, you need to fine tune on non-working
*  code. Take us through that inspiration. How many rounds did you do? It might be generous to say
*  that the vast majority of code is in a working state. I don't know if I can be honest. That's
*  very nice of you to say that my code works. Certainly, it's not true for me. You're right,
*  it's an interesting problem. What we saw was when we didn't do that, obviously, we were just
*  having to one-shot the answer. After that, it's like, well, I've never seen iteration before. How
*  am I supposed to figure out how this works? What you're alluding to there is the self-improvement
*  loop that we started working on. That was in two parts. We synthetically generated runtime errors
*  where we would intentionally mess with the AST to make stuff not work or index out of bounds or
*  refer to a variable that doesn't exist or errors that the foundational models just make sometimes
*  that you can't really avoid. You can't expect it to be perfect. We threw some of those in with a
*  probability of happening. On the self-improvement side, I spoke about this in the blog post,
*  essentially the idea is that you generate your data in batches. First batch is perfect, like
*  here's the problem, here's the answer, go train the model on it. Then for the second batch,
*  you then take the model that you trained before that can look like one commit into the future,
*  and then you let it have the first attempt at solving the problem. Hopefully, it gets it wrong.
*  If it gets it wrong, then you have like, okay, now the code base is in this incorrect state,
*  but I know what the correct state is. I can do some diffing essentially to figure out how do I
*  get the state that it's in now to the state that I want it in. Then you can train the model to then
*  produce that diff next and so on and so on and so on. The model can then learn and also reason
*  as to why it needs to make these changes to be able to learn how to solve problems iteratively
*  and learn from its mistakes and stuff like that. You picked the size of the data set just based on
*  how much money you spent generating it. Maybe you think you could just make more and get better.
*  Multiple of my monthly burn. It was very much related to capital. With any luck,
*  that will be alleviated soon. Very soon. I like drawing references to other things that are
*  happening in the wild because we only get to release this podcast once a week. The
*  Lamma 3 paper also has some really interesting thoughts on synthetic data for code. I don't know
*  if you have reviewed that. I'll highlight the back translation section because one of your
*  data set focuses is updating documentation. I think that translation between natural language,
*  English versus code and back and forth, I think is actually a really ripe source of synthetic data.
*  Lamma 3 specifically called out that they trained on that. We should have gone more into that in
*  our podcast with them, but we didn't know. There's a lot of interesting work on synthetic data stuff.
*  We do have to wrap up soon, but I'm going to briefly touch on the submission process for
*  Sweetbench. You have a 30% state-of-the-art Sweetbench result, but it's not on the leader
*  board because of submission issues. I don't know if you want to comment on that stuff versus...
*  We also want to talk about Sweetbench verified. Anything on the benchmarking side.
*  The potted history of this is quite simple, actually. Sweetbench, up until, I want to say,
*  two weeks ago, but it might be less than that or more than that, but I think two weeks ago,
*  suddenly started mandating what they call trajectories when you submit. Prior to this,
*  essentially, when you run Sweetbench, you run it through their harness and out the other end,
*  you get a report.json which is like, here's how many I resolved, here's how many I didn't resolve,
*  these are the IDs, the ones I did, these ones are the IDs I didn't, and it gives you any ones
*  that might have errored or something like that. What you would submit would be all of your model
*  patches that you outputted and that report. Then you would PR that into the Sweetbench repo and
*  that would be it. That was still the case when we made our submission on whatever day it was. They
*  look at them every Monday. We submitted it at some point during the week. I want to say it was four
*  days before that. I sat back and waited. I assumed it would be fine. When it came to Monday,
*  they then said, actually, no, we want model trajectories. I was like, okay, let me see what
*  this is and so on. I dug into it. Model trajectories are essentially the context window
*  or the reasoning process of show you're working. How did you get here? If you do a math exam,
*  show me you're working. Whereas before, they were like, just give me the final answer. Now
*  they want to see the work. I completely understand why they want to see that.
*  Sweetbench fundamentally is an academic research project and they want all the stuff to be open
*  source and public so people can learn from each other and improve and so on. That's very good. I
*  completely agree. However, at least for us, and the reason that we're not on the leaderboard is that
*  obviously the model outputs that we generate are sort of a mirror of our training data set. You
*  train the model to do a certain thing and output a certain way, whatever you output looks like your
*  training data. For the moment, as a closed source company, like fighting for an edge, we've decided
*  not to publish that information for that exact reason. I don't want someone basically taking my
*  tradges and then taking a model that's suing me GA and just distilling it immediately and then having
*  genie for themselves. As a business owner, that's the decision I've had to make.
*  The patches are still public. So like the, dare I say, traditional Sweetbench submission,
*  you can go to a GitHub repo and see it and run them for yourself and verify that the numbers
*  come out correctly. Like that is all that is the pot of reason. That's the story.
*  Sweetbench verified. You have a score. I do have a school. I do have a school 43.8%.
*  It's one of those things where like there aren't that many people on the leaderboard yet. So you
*  don't know how good or bad it's a smaller data set, right? Oh, it's, it's great. So on a tangent,
*  Sweetbench, original Sweetbench was 2,294, which is expensive. It's like $8,000 to run.
*  Oh, that's cheap. I don't know. At least for us, I don't even want to say publicly.
*  How much it costs us to run that thing. Expensive, slow, really like crap for iteration because like,
*  you know, you make a change to your model. How does it do on Sweetbench? I guess that's why
*  Sweetbench Lite existed, but Sweetbench Lite was not a, it was, there was easy stuff, right? Wasn't
*  a comprehensive measure of the overall thing. So we actually had the idea a month ago to what we
*  were going to call Sweetbench Small, where we were going to try to map out across Sweetbench,
*  like what is the distribution of like problem difficulty and all these different things,
*  and try to come up with like 300 examples that sort of map that where given a score on Sweetbench
*  Small, you could then predict your Sweetbench large score and sort of go from there. Fortunately,
*  OpenAI did that for us and probably much better than we would have done. They use some human
*  labelers and as obviously we're working with OpenAI quite closely, they talked to us about it and
*  they, you know, were able to let us know what the instance IDs were that were in the new Sweetbench
*  version. And then as soon as I had that, I could just take the report from the one that I run and
*  just diff them. And I was like, oh, we got 219 out of 500, which is 43.8%, which is to my knowledge,
*  at least right now, state of the art also, which makes sense, but also GPT-4.0 gets, I believe,
*  33%, which is like, I double check that. But I believe-
*  The August one, the new one.
*  Yeah, it's in their blog post. I can't remember which one it was. I don't know what the model
*  version was, but GPT-4.0, I believe gets 33%, which is obviously like significantly better than
*  what it got on the original, like Sweetbench.
*  2%.
*  It's only ridiculously low.
*  But no, Sweetbench verified like, it's so good. It's like, it's smaller. We know that the problems
*  are solvable. It's not going to cost me a lot of money to run it. It keeps my iteration time
*  lower. And there are also some things that we're going to start to do internally when we run
*  Sweetbench to have more of an idea of how right our model is. So one of the things I was talking
*  to John about yesterday was Sweetbench is a pass or fail, right? Like you either have solved the
*  problem or you haven't. That is quite sparse. It doesn't give you a huge amount of information
*  because your model could have got a lot of it right. Like looking through when you do a math
*  paper, you could have got the reason that you're working right until like the penultimate step,
*  and then you get it wrong. So we're going to look into ways of measuring, okay, well,
*  your model got it right up to this line and then it diverged. And that's super easy to do
*  because obviously you know the correct state of all of those questions. So I think one of the ways
*  we're going to keep improving Genie is by going more in depth and saying, okay, for the ones that
*  failed, was it right at any point? Where did it go wrong? How did it go wrong? And then sort of
*  trying to triage those sorts of issues.
*  So future plans, you have mentioned context-istaining and open source model, but basically I think,
*  you know, what the Genie is, is basically this like proprietary fine-tune data set and process
*  and software that you can add onto any model. Is that the plan? That's the next year?
*  That is, we're going to get really, we're going to be the best in the world at doing that
*  and continue being the best in the world at doing that and throwing it as many models as we can,
*  seeing what the performance is like and seeing what things improve performance in what places
*  and also making the data set larger is like one of the biggest things we're going to be working on.
*  I think one of the decisions before you as a CEO is how much you have like the house model be like
*  the one true thing and then how much you spend time working on customer models.
*  That's the thing that really gets me so excited genuinely. Like we have a version of Genie that
*  we named after one of our employees. It's called the John. We have a version of Genie that is
*  fine-tuned on our code base. So we basically, it's the base Genie and then we run the same data
*  pipeline that we run on like all the stuff that we do to generate the main data set on our repo.
*  And then all of a sudden you have like something that is both very good at software engineering,
*  but is also extremely good at your repo. And that is phenomenal to use. Like it's really cool.
*  More broadly outside of Cosine, what are you seeing? What trends are you seeing that you're
*  really excited by? Who's doing great work that you want to call out?
*  One of the ones that, I mean, it's not an original choice, but Cursor are actually
*  killing it. All the employees at Cosine love using it. And it's a really, really good example
*  of like just getting like UX right basically. Like putting the LLM in the right place and letting
*  it allow you and getting out of the way when you don't want it there and making it familiar
*  because it's still VS code and all these things. They've done an amazing job and I think they just
*  raised around. So congrats on that to them. So like they're doing amazing work.
*  Decision to fork VS code, I think was controversial. You guys started as a VS code extension.
*  We did, yeah.
*  Many, many, many people did that and they did the one thing that no one wanted to do.
*  I commend the bravery, honestly. Like I commend the bravery because like in hindsight, obviously
*  it's paid off, but at least for me in the moment, I was one of those people being like,
*  is that going to, are people going to do that? Are people going to download that? And yes,
*  obviously they are like, sure. Doing the hard thing, which is having worked on G&E recently,
*  for the past eight months or whatever, as taxing as it's been on us, like one of the main things
*  I have learned from this is like, no matter how small you are, how much resource you have,
*  just like try to do the hard thing. Cause I think it has the biggest payoff.
*  More broadly, just like lessons that you've learned running your company.
*  Oh, it's been a two year journey.
*  Two year journey. I mean, it's better than any real job you can ever get.
*  I feel so lucky to be working in this area, especially, it was so validating to hear it
*  from the guys at OpenAI as well, telling us like we're on the cutting edge on the bat.
*  We're pushing the boundaries of what's possible with what we're doing because I get to do,
*  I get to be paid to do this. I have briefly, as you heard at the beginning, done real jobs
*  and normal stuff and like just being able to do this on the daily is so interesting and so cool.
*  It's like, I pinch myself a lot genuinely about the fact that I can do this and also that not
*  only I can do this, but fortunately being a co-founder of the company, I have a huge
*  amount of say as to where we go next. And that is a big responsibility, but it's also so exciting
*  to me because I'm like, you know, steering the ship is, has been really interesting so far.
*  And I like to think that we've got it right, you know, in the last, in the last sort of eight
*  months or so. And that this is like really the starting point of something massive to come.
*  Awesome. Calls to action. I assume you're hiring, I assume you're also looking for customers. What's
*  the ideal customer, ideal employee? On the customer side, honestly, people who are just
*  willing to try something new, like the Genie UX is different to a conventional IDE. Give it a chance
*  like that. We really do believe in this whole idea of like developers work is going to be abstracted,
*  you know, levels higher than just the code. We still let you touch the code. We still want you
*  to dive into the code if you need to. But fundamentally, we think that if you're trying
*  to offload the coding to a model, the model should do the coding and you should be in charge of
*  guiding the model. So people who are willing to give something new a chance. Size of company,
*  and honestly, well, preferably the languages that are the most represented in our, in our train
*  days. So like anyway, if you're like doing TypeScript, JavaScript, Python, Java, that sort of
*  thing. And in terms of size of company, like so long as you're willing to try it and there
*  aren't any massive like infosec things that get in the way, like it doesn't really matter.
*  Like code base size can be arbitrary for us. We can deal with any code base size. And essentially,
*  any language, but your mileage may vary. But for the most part, like anyone who's willing to give
*  it a try is the ideal customer. And on the employee, honestly, we just want people who,
*  we're going to be hiring both on like what we call like the traditional tech side. So like building
*  the product essentially, and also hiring really heavily on the AI machine learning data set side.
*  As well. And in both cases, essentially, what we just wanted like really passionate people
*  who are obsessed with something and are really passionate about something and
*  are willing to, it sounds so corny with like join us in what we're trying to do. Like we have a very
*  big ambition and we're biting off a very large problem here. And people who can look at what
*  we've done so far, I'm like, wow, that's really impressive. I want to do that kind of work. I
*  want to be pushing the boundaries. I want to be dealing with experimental stuff all the time.
*  And, but at the same time, you putting it in people's hands and shipping it to people and so
*  on. So if that sounds, you know, amenable to anyone, that's the kind of person we're looking
*  to apply. Excellent. Any last words? Any Trump impressions that you like the Trump impression?
*  Everyone loved the Trump impression. Yeah. I mean, it's funny because like, I have some bloopers.
*  I'll show you the bloopers after we finished recording. I'll probably tweet them at some point.
*  The initial cut of that video had me doing a Trump impression. I sort of sat down into the chair
*  and been like, cosine is the most tremendous air lab in the world. Unbelievable. I walked in here
*  and I said, wow, this is an amazing lab. And like we sent it to some of our friends and they were
*  like, nah, you can't cold open with Trump, man. You just can't like, no one knows who you are.
*  You can end with it. But you can end with it. Now that that has gone out, we can now,
*  we can now post the rest of the bloopers, which are essentially me just like
*  fluffing my lines the entire time and screaming at my co-founder out of frustration. So yeah.
*  It was very well executed. Actually, very few people do the launch video that you did. I'm
*  as a sort of developer relations person. I'm actually excited by that stuff, but
*  thank you for coming on. Very, very short notice. I hope you have a safe flight back and excited to
*  see the full launch. I think this is a super fruitful area and congrats on your launch.
*  Thank you so much for having me. Cheers.
*  It is both energizing and enlightening to hear why people listen and learn what they value about
*  the show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.
