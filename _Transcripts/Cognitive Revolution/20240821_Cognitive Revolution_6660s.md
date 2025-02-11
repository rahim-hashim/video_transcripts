---
Date Generated: September 05, 2024
Transcription Model: whisper medium 20231117
Length: 6660s
Video Keywords: []
Video Views: 4646
Video Rating: None
Video Description: Nathan presents a comprehensive AI automation framework developed over three years, applicable to process automation and generative AI integration. This episode of The Cognitive Revolution, offers critical insights for businesses looking to leverage AI effectively. Learn about choosing AI tasks, understanding work deeply, and optimizing AI performance in the wake of GPT-4 fine-tuning launch.

"AI Automation: Making AI Work for You" - Slide Deck: https://docs.google.com/presentation/d/1HCtUNmzcIZvMK9OPkdveczyf8rxYNBcvkdm-Ocw_rn0/edit#slide=id.g252d9e67d86_0_16

Waymark's case study on GPT-3 fine-tuning: https://openai.com/index/waymark/

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: 1 to 100 | Hypergrowth Companies Worth Joining
Every week we sit down with the founder of a hyper-growth company you should consider joining. Our goal is to give you the inside story behind breakout, early stage companies potentially worth betting your career on. This season, discover how the founders of Modal Labs, Clay, Mercor, and more built their products, cultures, and companies.
Apple: https://podcasts.apple.com/podcast/id1762756034
Spotify:https://open.spotify.com/show/70NOWtWDY995C8qDqojxGw

RECOMMENDED PODCAST: History 102
Every week, creator of WhatifAltHist Rudyard Lynch and Erik Torenberg cover a major topic in history in depth -- in under an hour. This season will cover classical Greece, early America, the Vikings, medieval Islam, ancient China, the fall of the Roman Empire, and more.Subscribe on 
Spotify: https://open.spotify.com/show/36Kqo3BMMUBGTDo1IEYihm
Apple: https://podcasts.apple.com/us/podcast/history-102-with-whatifalthists-rudyard-lynch-and/id1730633913
YouTube: https://www.youtube.com/@History102-qg5oj


SPONSORS:
Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-Turpentine-Network

Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

80,000 Hours offers free one-on-one career advising for Cognitive Revolution listeners aiming to tackle global challenges, especially in AI. They connect high-potential individuals with experts, opportunities, and personalized career plans to maximize positive impact. Apply for a free call at  https://80000hours.org/speak to accelerate your career and contribute to solving pressing AI-related issues.


CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsor: WorkOS
(00:01:22) About the Episode
(00:04:20) Introduction to AI Automation
(00:08:00) Useful Concepts
(00:13:43) Current AI Capabilities
(00:17:24) Sponsors: Oracle | Brave
(00:19:28) 3 Ways to work with AI
(00:25:10) Choosing Work for AI to Do
(00:31:18) Sponsors: Omneky | 80000 hours
(00:33:20) What AI Can Do vs. Can't Do
(00:47:11) Understanding the Work
(00:52:58) Documenting the Work
(01:00:50) Optimising AI Performance
(01:02:14) Prompt Engineering Gold Standards
(01:07:05) Optimising Information: Retrieval Augmented Generation
(01:09:29) Optimising AI Behaviour: Fine-tuning AI Models
(01:20:55) Trade-offs in AI Automation
(01:38:05) No-code Platforms for AI
(01:39:54) Roles in AI Automation
(01:50:38) Outro


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

# AI Automation Making AI Work for You - now with GPT-4o Fine-Tuning!
**Cognitive Revolution:** [August 21, 2024](https://www.youtube.com/watch?v=mPGkObr6SeA)
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
*  Hello, and welcome back to the Cognitive Revolution. The big news in AI in the last 24 hours was the
*  launch of GPT-4.0 fine-tuning from OpenAI. And that makes today the perfect day to share a presentation
*  on AI automation that I recently gave at the Adapta Summit in São Paulo, Brazil. I want to
*  give a big shout out to Max Peters and the whole Adapta team for having me. It was an awesome event
*  and a great opportunity to speak to more than 4,000 Brazilian business owners. I also had a
*  number of excellent conversations with very sophisticated AI builders. The AI automation
*  framework that I'm presenting here today is one that I've developed over the last three years,
*  starting in the summer of 2021 when OpenAI first made GPT-3 fine-tuning available.
*  Importantly, this approach, which includes a methodology for choosing the right tasks for AI
*  to do, a process for ensuring that you understand the work deeply enough to teach AI how to do it
*  effectively, and a roadmap for optimizing AI performance, which includes fine-tuning,
*  is one of the very few things that I've found has really stood the test of time in the fast-evolving
*  AI landscape. And while I present this presentation in terms of process automation, my work at Waymark,
*  where we've built a genuinely delightful AI-powered video creation experience for small
*  businesses, has taught me that the same basic principles also work when you want to add a
*  done-for-you-by-AI experience to an existing software application. I am extremely proud that
*  Waymark still has a case study page on the OpenAI website, which we earned for making excellent use
*  of GPT-3 fine-tuning. And the biggest change I've noticed as generation after generation of new
*  models has come online is really how ambitious we can be about our AI automation goals. Now,
*  with GPT-4.0 fine-tuning coming online too, that AI glass ceiling has just been raised yet again.
*  My goal with this presentation is to give you all of the most critical knowledge that you need to
*  succeed with AI automation projects. And I am genuinely not holding anything back. But I am
*  also considering taking on one or two businesses as AI automation consulting clients. So if you're
*  intrigued by the possibilities outlined here and believe that I can help accelerate your success,
*  please send me a note, either via our website, cognitiverevolution.ai, or by DMing me on your
*  favorite social network. Now, two final notes before getting started. First, I am thrilled to
*  welcome 80,000 Hours as a new sponsor to the show. Stay tuned to hear about the free one-on-one
*  career advising sessions that 80,000 Hours is now offering to cognitive revolution listeners.
*  Next, please note that this episode is probably best watched on YouTube, as I will be using a
*  slide deck throughout. That said, I do think the audio version will be okay if you really
*  prefer it. And in any case, we'll place a link to the slides in the show notes for your reference.
*  Now, let's go deep on AI automation and get ready to revolutionize the way we work.
*  I am here to talk through my recent presentation on AI automation. This is a presentation that
*  I recently had the opportunity to give at the Adapta Summit in Sao Paulo, Brazil.
*  It was for an audience of Brazilian Portuguese-speaking business owners, which was
*  quite a fun time. It's a great occasion for me to try to take a step back and say,
*  what do people who are not obsessed with AI but really want to get practical utility out of it
*  today most need to know to actually realize some of the value that I and others who have
*  spent a lot of time working with AI are actually enjoying in our day-to-day work.
*  I think a lot of people will probably benefit from this if you are looking around at the
*  broader world and saying, geez, everybody else seems to be getting so much value from AI and
*  I'm really not. I think this will be at least one angle that you can potentially take to really
*  start to make AI work for you. Let's get into it. As I shared with the group there in Sao Paulo,
*  I had the chance to stop in Manaus along the way. Manaus is the capital of the Amazon region.
*  The reason it's worth mentioning here briefly is just that as far out as Manaus may sound as a
*  destination, it is still pretty much a big city with 2 million people living there, even though
*  it's a city in the middle of the jungle that for most of its history has only been accessible by
*  river. Now you can access it by plane and they have one highway, I believe now. So it's kind of
*  out there and yet it is a place where the internet works, where my cell phone worked, where I took a
*  food tour in the afternoon and went around with a guy who spoke perfect English and who was still
*  in school actually studying tourism and had recently done a project on how to use AI for
*  tourism purposes. Obviously, one of the most obvious things to do is to use AI for translation.
*  He spoke English but he couldn't speak other languages of guests that might want to come and
*  take a food tour with them. So translation mediated by AI could be super useful for him
*  and it was definitely super useful for me in any conversations I was trying to have with Portuguese
*  speakers. So the world is definitely getting pulled together by technology, of course, in general and
*  AI had both, let's say, excited users and very much practical use for me on the ground there over
*  the course of a couple days. So I just introduced myself to the audience in Sao Paulo. I don't think
*  anybody really needs that here so we'll keep it moving. I've used this term AI scouting many times.
*  I didn't want to have to explain to them what that meant so I just said that I study AI and noted that
*  I try to come at it from as many different angles as possible. Okay, so here is the outline for this
*  AI automation talk. I started off with a couple definitions, just some foundational information.
*  A couple of these slides folks may have seen before in some of my other AI scouting reports,
*  but I thought that these definitions that I came up with were useful for helping people develop
*  intuition. So I thought it was worth taking a couple minutes on that. Then the heart of this
*  presentation is really getting into the three core steps of AI automation. As I look back,
*  this is a method that I've been working on really for the last three years solid and my practice on
*  this definitely changed a bit when GPT-4 dropped into my lap and I moved into the red teaming work
*  there, but the same core concepts that worked for GPT-3 and 3.5 now work for GPT-4 as well. It's
*  really just the scope of what you can do that has changed. Toward the end, I have some extras
*  and those were mostly leaf behinds for the audience, but I'll probably spend a little bit of time
*  here since we have time to go into those in a little bit more detail. So let's start off with
*  motivational definitions. I first just asked the audience to consider what is work? This is
*  kind of a dumb question, but I wanted to give a very general answer, which again I think will be
*  helpful in developing intuition for where to apply AI. The definition that I offer is that work
*  is the transformation of inputs into outputs. You have some starting inputs, you do some work,
*  and you get outputs from those inputs as a result of that work. It's almost tautological,
*  but as you'll see it's a building block for figuring out how to make sense of AI automation.
*  The next question is definitely more philosophically challenging and I don't want to
*  get into many different philosophical angles on this, but again just thinking intuitively and
*  practically what is intelligence? Here I offer the definition that intelligence is the ability to do
*  work, that is to transform inputs to outputs, without precise instructions. Now both of those
*  parts are really important, but the without precise instructions is really what distinguishes
*  something that we would call intelligent from something that we would call a fully deterministic
*  machine. So here's an example. This is the MNEST data set. This is one of the oldest and most
*  classic data sets in machine learning. The challenge here is to take a small image of a
*  handwritten digit and identify what number that is. This is an easy task for humans as you scan
*  through these numbers. Almost all of them are immediately obvious. There are some issues that
*  could be a little bit weird like what's going on here or what's going on here, but most of these
*  are like super easy and people score very high on this task as you'd expect. Now in contrast if you
*  try to write a computer program in the traditional sense of just coding up a bunch of rules to
*  identify these numbers, you find that this is in fact extremely difficult. I called it impossible
*  here. It might not be fully impossible in the fullness of time, but it is definitely something
*  that people still don't really know how to do. I went to Claw 3.5 Sonnet. Now GPT-4-0 just came out
*  with a new version just in the last day or two, so I still need to test that a little bit more
*  extensively. That is topping some leaderboards. For me, 3.5 Sonnet is still my go-to for the moment
*  for most tasks. I asked it to do an exercise to code up a function to classify these images.
*  It first gave me an explanation starting with the caveat that this is not the way to do this. You
*  really should use machine learning, but then it went ahead and coded up an attempt. You can see
*  that what it came up with here is a number of rules. If there's a line across the top,
*  it might be a seven. If there's a line across the bottom, it might be a two, et cetera, et cetera.
*  It also wrote the code to help me test the function to see how accurate it was. We got
*  14% accuracy on this task. Obviously, that's not very accurate and certainly not something
*  that you could use in any sort of practical economically valuable setting. By the way,
*  people sometimes say, does this really matter? Is there economic value to recognizing numbers?
*  I would just say, for starters, think about delivering the mail. How many millions of pieces
*  of hand-addressed mail are delivered every single day in the United States alone? It's going to be
*  quite a lot and somebody has to recognize those numbers. They do in fact have computers doing that
*  today, but they're not doing it with this sort of traditional code method. There is a genuine
*  economic value in solving this problem. Just to double check myself too, I asked Perplexity
*  what the best ever attempt to code up a solution to digit recognition was. It found an approach
*  that involved compressing the images using zip type compression and then looking at the file
*  sizes and making a prediction based on that. I thought it was a pretty clever approach.
*  Perplexity said that got to 80% accuracy. That's a lot better, but still that's wrong one in five
*  times. That's apparently the best that Perplexity could find in terms of somebody doing this with
*  a fully engineered algorithm. It's obviously still not good enough to be used.
*  The punchline is that AI also can do this task and actually can do it relatively easy. Even very small,
*  very simple neural nets can learn this task and can learn it way better than any explicit code
*  technique. My online research suggests that this can get up to 99.7% correct and that's right at
*  human level. I've got other videos of the content that goes into how this works, how these networks
*  are trained, all the vocabulary about the parts of them and the concepts of forward passes and
*  backpropagations and finding gradients and gradient descent. I'm going to leave all that
*  to other things for now. For now, this is going to be a very practical talk and we're just talking
*  about getting AI to work for you. The first takeaway of this example is that you want to
*  use AI for work that genuinely requires intelligence. If you have work to be done
*  that can be done by a fully deterministic machine or by traditional fully explicit code,
*  then you probably will ultimately be better off going that way because AI has downsides.
*  It costs more, it is slower, and it is more prone to mistakes than those deterministic approaches.
*  You really want to make sure that you're using it where it is in fact required. You want to use it
*  where intelligence is really required. You want to use it for things that can't be solved with those
*  fully explicit methods. With that said, it's really important to also understand what can AI
*  do today. You might see that and say, okay, recognizing toy numbers, that's just obviously
*  a very simple example. In fact, in today's world, the best AIs are closing in on human expert
*  performance on a great many routine tasks. This has happened obviously quite quickly over the last
*  few years and the word routine there is really important. When we talk about routine work,
*  we're talking about something where we know what good looks like. That happens quite a bit
*  and that the AI has a reasonable chance to learn from examples, either examples that
*  the model developers have found in the wild or perhaps as we'll get into examples that we will
*  curate in the process of AI automation. But we are going to need examples and the AI really excels
*  when it has those examples to learn from. That does not mean though that these are low value tasks.
*  I would say one of the highest value tasks, both in terms of the amount of schooling that people
*  go through to learn how to do it well, the money that they're paid and certainly the value to the
*  customer. One of the highest value tasks in our society is medical diagnosis. This study out of
*  Google, which we did cover in a previous podcast, shows that when they developed a purpose built,
*  they started with a foundation model, one of their best language models, but then really
*  dialed in the performance with a mix of different techniques, including multiple rounds of fine
*  tuning. They were able to create a chat bot that outperformed human doctors on the task of diagnosis
*  as judged by other human doctors in a pretty substantial way. You can see that on the left,
*  the AI doctor performance is just higher across the board regardless of how many guesses the
*  system or the doctor gets, regardless of how accurate your threshold for counting its answers
*  correct is. It's just basically strictly better than the human doctor. That's not the last word
*  on this. Google hasn't brought this to market yet. They're obviously going to be very cautious
*  about that and make sure that they have everything very buttoned up before they would bring this out
*  to the public in a commercial way. But this is published research and this is something that I
*  think is very credible and a very strong sign of things to come. This is not just research either,
*  by the way. This is something that is already being commercialized and sometimes in a pretty
*  serious way. This story from earlier this year, this company Klarna announced that they had created
*  an AI assistant powered by OpenAI that had handled 2.3 million customer conversations,
*  two-thirds of all their customer service conversations in just its first month live.
*  Doing the work of 700 full-time people, getting their customers better and faster answers as
*  measured by lower return times, just faster time to resolution. In part, that's because it's
*  available 24-7 and it speaks 35 languages. Overall, they estimated that this was going to
*  make their company $40 million more profitable in just 2024. That's not to say that it's doing
*  everything. It's doing two-thirds of the customer service chat. One-third, it still wasn't doing
*  or they didn't necessarily trust it to do, but to do two-thirds of customer service chats for a
*  company that is operating at scale, saving tens of millions of dollars, this is a big deal.
*  The takeaway from these two examples is that AI can very likely do routine work for you. Whatever
*  business you're in, whatever processes you have, I would bet there is something that you can get AI
*  to do at a human level or above. Save yourself a ton of time and money, scale something that was
*  previously impossible to scale. What you need to do is follow the framework that I'm about to get
*  into and really get disciplined about your approach to AI automation and then you will
*  likely be able to achieve this. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. AI might be the most important new computer technology ever. It's storming every
*  industry and literally billions of dollars are being invested. So buckle up. The problem is that
*  AI needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing, and of course nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  slash cognitive. That's oracle.com slash cognitive. Oracle.com slash cognitive.
*  This episode of the Cognitive Revolution is sponsored by the Brave Search API. You may know
*  if Brave has an alternative to Chrome, but did you know that Brave has its own independent search
*  engine powered by its own 20 billion page index of the web? The Brave Search API gives developers
*  reliable and affordable access to programmable web search, auto suggest, spell check, and more
*  with flexible plans for all types of use cases from rag search to automated business intelligence.
*  On top of that, it's up to three times cheaper than Bing, all without compromising on quality,
*  speed, or reliability. Over 700 businesses including Cohere, Chegg, and Kagi rely on the
*  Brave Search API and a recent survey showed that 94% of customers would recommend it to their peers.
*  To start building apps with the power of the web, sign up at brave.com slash API and get up to 5,000
*  free monthly calls. I do have one note though that I want to contrast because I think this was very
*  true with the audience in Sao Paulo and it might be quite true for the podcast audience as well.
*  It is important to distinguish between different ways of working with AI. Today we are of course
*  most familiar with chatting with AIs and that in fact was the nature of the interaction in the last
*  two examples as well. Both the diagnosis result and the customer service result ultimately present
*  to the end user as a chatbot. So we're very familiar with this modality, chat GPT, etc, etc.
*  It is a real-time interaction. You can take it anything you want. That's what makes it so
*  magical. But you the human remain in control. You are the pilot, the AI is the co-pilot,
*  and it's up to you in real time to figure out is the AI actually helping me right now or would I be
*  better off doing this on my own? And I think almost everybody who's used chatbots in some
*  depth has certainly had notable experiences of both. What we're talking about with automation is
*  a bit of a different goal. Instead of having a real-time interaction where we're always evaluating
*  is this thing working or not, the goal of automation is to get to the point where you can actually
*  delegate a certain piece of work on a consistent basis to an AI system and have enough confidence
*  that it will do the job well that you no longer have to check every single one of its outputs.
*  That for me is the unrealized potential of AI automation. In my work with Athena,
*  the executive assistant company, we also call this AI delegation. And you better believe that
*  we will be using this same framework internally to train executive assistants in the art of AI
*  automation because I think this is actually something that a lot of people can do and
*  certainly something that a lot of clients can really benefit from. So this typically takes the
*  form of more structured workflows that could be zappier zaps or it could be automations through
*  any number of different no code platforms or even could be operated through custom code. But the key
*  point is that you're hopefully going to get to the point where you can put this into the background
*  of your life, not have to think about it all the time. Once you've designed it, set it up,
*  validated that it's actually working, then you can leave the execution on a day-to-day basis
*  to the AI. In the middle, of course, are agents. And I think of agents as trying to get the best
*  of both worlds. It's real-time on the fly delegation. So it's somewhere between the chat
*  bot where you're having this real-time interaction and constantly evaluating and the automation where
*  you have to actually set up the structure. The promise of agents is that you can say,
*  hey, on the fly, here's a little project that I have. Go do it. Come back when you're done.
*  And hopefully, you would get good results. You have to take a trust but verify
*  approach with that right now. And for the most part, in today's world, people are not having
*  great results with this. I think a ton of work is going into it. I expect that with so much scaffolding
*  and so much structure having been built already that when the next generation of models hits that
*  are better at reasoning and better at multi-step planning and potentially better reflection,
*  that we will start to see some of the agent systems work. But for now, we're all waiting for
*  that. And what we're hearing, by the way, from a lot of the agent companies is a version of this
*  notion of using AI only where intelligence is truly required. They are saying that anything they can
*  do with code, they should be done with code. And you really only want to use AI where it's strictly
*  necessary to understand the user's intent. And you can map that onto much more structured,
*  deterministic program. And that can still be a magical experience for users because it can
*  allow people to have natural language conversations over the phone and actually get things done,
*  for example, which is not a very good or pleasant experience with most phone tree systems today.
*  There's, I think, real value on the verge of being unlocked even with today's models and
*  today's agent structures. My sense, though, is that this is really going to take a leap.
*  It could happen essentially anytime. I think everybody sort of understands that the leading
*  AI developers have more advanced models than they've released. How much more advanced and
*  how are they scoring on these sorts of things internally? We don't know. But it would be a
*  pretty big surprise for me if we don't see a next generation of models come online that can really
*  make these agents work for all sorts of kind of small scale ad hoc delegation in the near future.
*  That's a prediction. You can hold me accountable to that if it doesn't happen, but I would be quite
*  surprised. Okay, here's the heart of it. AI automation in three easy steps. Break this down
*  into first, choosing the work for AI to do. Second, understanding and documenting that work.
*  And then third, optimizing AI performance. This kind of moves from social to technical,
*  but you need to understand at least what is possible with technology throughout this process.
*  Depending on your background, different aspects of this may be more or less valuable. One of my
*  goals for this presentation is to help AI engineer, AI obsessed folks in general,
*  have better conversations with people that they're trying to apply AI for who don't have
*  the depth of experience or the intuition for what makes a good AI project. I see a lot of
*  cross talk between folks where business owners, project owners, budget owners, people who are
*  trying to make their business work better, have questionable intuitions. And then sometimes the AI
*  service providers that are working with them kind of sent in the wrong direction. And I think it
*  can be dramatically more successful to embark on AI automation projects if there's clarity and good
*  meeting of the minds between the AI expert and the domain expert. And I hope that this framework
*  will facilitate a lot of those conversations. So let's get into it. Choosing work for AI to do.
*  Obviously, this is super basic, but just putting my earlier definitions together.
*  The general form of what we're looking for here is some inputs that need to be transformed to
*  some outputs where intelligence really is required to make that transformation. That is to say where
*  we can't code up a fully explicit rules-based approach that actually works. When we can't,
*  and of course, there are many things where we can't, right? That's why humans have jobs
*  in today's world. Then that's at least a candidate for AI. Now, this is just a rundown of what makes
*  a good target versus what makes a bad target. I've already hammered a couple of times the idea that
*  you want to pick something where intelligence is really required. And then if you could do something
*  purely procedurally or purely with code, then you probably would at least want to seriously consider
*  that because it's going to run faster, it's going to run cheaper, and it's going to run more
*  predictably with traditional code versus AI. The next big thing to know is that you want to be
*  looking for things that are task-sized as opposed to things that are job-sized. This is actually one
*  of the biggest mistakes that I see business owners making is they're just thinking a little too big
*  relative to what AI can do right now in many cases. AI can do tasks. These tasks can be minutes. They
*  can be tens of minutes. They can be a couple hours. The AI evaluation organization, METER,
*  recently just put out a new benchmark. I haven't dug into it fully yet, but one of the things that
*  I loved about just their initial presentation is that they were segmenting the tasks that they were
*  testing the AI on by how long it took people to accomplish those same tasks. And of course,
*  there's a spectrum, but what you'd see there is that these very small couple-minute tasks,
*  AI can very often do. Not always, because as we'll see, there's a weirdness here,
*  but very often can. As the tasks get bigger and start to get over a day, the success rate really
*  starts to drop off. So you want to be thinking about tasks and how things are broken down into
*  tasks. Next, you want to look for something that is slow and expensive because obviously that's
*  where the payoff is. If something's already fast and cheap for you to do, then you're not going to
*  find as much value in automating it. Sometimes people think about looking for things that seem
*  to them to be the most automatable and they have the intuition that something that's fast and cheap
*  would be the most automatable. There could be some truth to that, but it's really important to keep
*  the payoff in mind as you go here. And so I always look for things that are slow and expensive. Same
*  idea with looking for something that's repetitive versus looking for something that's a one-off.
*  If it's not repetitive, you're not going to get the payoff. And as you'll see, this is a process
*  that we're going to outline here. So to go through that process, you want to have some significant
*  end number of times that this thing is going to happen, or it's probably just not going to be
*  worth it. If it's a one-off, take it to a chat bot. You might get some good help, but you don't
*  necessarily need to set up all the structure and evaluation and put the rigor in that makes sense
*  if you're doing true automation. Next one is super important. You are going to need explicit context
*  for an AI to be able to do the job. What does context mean? It's everything that is specific
*  to the situation that a person would need to know in order to do the job that is not generally known
*  on the internet. The AIs know a lot of stuff, but they know nothing about your particular business.
*  They know nothing about your particular project. They know nothing about your team. They basically
*  know nothing that they would need to know. Think about a random person coming into the business.
*  What are all the things that they would need to know? The AI is going to need to know probably
*  at least that much, maybe even a little bit more to add on to their background knowledge to be able
*  to do your task. In many organizations, context is not explicit. It is often implicit. That means
*  it's not really documented. People don't really necessarily get trained in a super formal way,
*  but they just look around and see what other people are doing and talk to people and gradually
*  build up the context that they need to be effective. That works fine, at least up to a certain point
*  for humans, but it doesn't work for AIs because AIs don't have water cooler conversations. They
*  don't wander around the office and look over people's shoulders at what they're doing.
*  They just don't have the same ways of gathering information on an ongoing basis. They have to have
*  it explicitly provided to them. A lot of times, AI automation really involves a critical step of
*  taking what was implicit context and making it explicit so that the AI can work with it.
*  Next is gold standard examples. This is a subcategory of explicit context,
*  but what's really important is to be able to first agree on what good looks like for a particular
*  task. I've seen it happen multiple times where you go into an organization and you ask how
*  this work is being done and nobody really knows. There's not a specific standard. There might be
*  multiple people doing it. You dig in and you find out that actually they're doing it in a different
*  way. Maybe that's fine. It seems like everything is working, but there isn't in reality a consensus
*  on exactly what is supposed to be happening here. Maybe they still disagree. Even when this result
*  comes to light, maybe people are like, oh, I actually prefer this or I prefer that.
*  You want as much as possible to avoid these beauty in the eye of the beholder type problems
*  where the people involved don't even have a consensus on what makes something good.
*  And you want to focus wherever you can on things where we have a clear concept of what does a great
*  job look like here. That is the gold standard example. And you're going to need to be able to
*  collect those as part of the context to make the AI successful. Low risk versus high sensitivity
*  pretty much goes without saying, especially when you're new to this, mistakes will happen,
*  issues will pop up. So you will be better served to go with something that's low risk versus
*  something that's high sensitivity. You also similarly want to make sure you're working in
*  a domain where you will get fast feedback. If there are issues, you do not want to set up AI
*  in a place where you have major blind spots and might not find out about issues until they've
*  built up and become a real problem for you. Number nine is a nod to Brazil, but it's also just,
*  maybe it's just common sense, but you want to automate things that are not fun for you to do.
*  The things that are fun, the things that you enjoy about your work, I would recommend for now,
*  keep doing them and let the AI focus on the stuff that you do not enjoy.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey guys, I'm excited to share that 80,000 Hours is now offering free one-on-one career advising
*  sessions to cognitive revolution listeners. 80,000 Hours' mission is to be the best source of career
*  advice for people who want to help solve the world's most pressing problems. And their website and
*  podcast are some of the best resources for information and perspective on AI. I used 80,000
*  Hours' career advising service myself just two years ago at age 38, immediately after completing
*  my GPT-4 red teaming work. At the time, I was honestly not sure that I could make a meaningful
*  contribution to the AI space, but I came away with a bunch of high-value introductions that ultimately
*  helped me build the confidence I needed to, among other things, start this podcast. Today, I know
*  that the cognitive revolution audience is full of very thoughtful, deeply engaged, and highly
*  capable people. That is exactly the sort of person that 80,000 Hours can help by working with you to
*  create or refine a high-impact career plan and by connecting you with AI safety experts and career
*  opportunities. To request a call, which like everything 80,000 Hours offers, is completely
*  free, go to 80,000hours.org slash cognitiverevolution or click the link in the show notes.
*  The possibility of transformative AI is increasingly real, and society is definitely not ready. So I
*  encourage you to suspend any lingering disbelief in yourself and take a concrete step that could
*  both accelerate your career and maximize your positive impact at 80,000hours.org slash cognitive
*  revolution. Finally, then, you want to find something that AI can do as opposed to something
*  that AI can't do. Now, some of these prior things have informed that, but there's still a huge
*  amount of questions open at this point on what can AI do versus what AI cannot do. If you're a
*  business owner and you're hearing this and this is a primer that you're then going to use to go out
*  and figure out what sort of AI specialists help you want to bring on, this will help you build
*  some intuition. But unfortunately, this is not a question that I can answer. What can AI do is not
*  a question that I can answer in full in probably any amount of time, but certainly not in a
*  reasonable presentation amount of time. And the reason for that is really just that AIs are weird.
*  I often say they should be referred to as alien intelligence, as opposed to more simply
*  artificial intelligence because of that weirdness. Now, arguably, humans are the weird ones and the
*  AIs are more normal. I don't want to be overly speciesist or pejorative here, but certainly
*  AIs violate the intuitions that we've developed around performance that we have from observing
*  humans. So just take three tasks, for example, translation, programming, a computer, and common
*  sense spatial reasoning. What you'll see is that people in general are not very good at translation.
*  Some people can do it pretty well. And indeed there was simultaneous English to Portuguese and
*  Portuguese to English translation at this event where I originally gave this talk. So some people
*  are pretty impressive with it. Most people can't do it at all. And the performance is generally all
*  over the map. Similarly with programming, some people are excellent. Some people can't do it at
*  all. A lot of people are in the middle. And then when it comes to common sense spatial reasoning,
*  again, a high level of variance, but people overall are pretty good. AIs are totally different. They
*  are, I would say, pretty clearly in many ways superhuman at translation in today's world.
*  They're not only faster and cheaper, but can also translate from any major language to any other
*  major language. If you're trying to do a highly literary translation, you should still go with
*  a human. But for kind of day to day functional translation, honestly, at this point, AIs are
*  your better bet in almost all contexts. Programming is in the middle. The AIs are consistently pretty
*  good. They can do a lot of stuff. They can write code in all the languages. They can also translate
*  code between languages, which is interesting. And by the way, they even outperform humans on
*  some coding contests. There have been some really interesting results where the language model has
*  outperformed the median entrant into a coding contest. You think about what kind of person
*  enters a coding contest as a hobby, something that they do for fun. They've got to enjoy programming.
*  Still, you have the AIs outperforming a good chunk of those people. But when it comes to the hardest
*  problems, the frontier technology there, your human expert is definitely going to be a lot better.
*  And then finally, common sense spatial reasoning is actually something that is a huge weakness
*  for AIs. And that's probably a reflection of the training data that they have access to.
*  Yes, they've read all the internet. They've read all the code on GitHub. But there's actually not
*  that much on the internet that says what happens when you stack an apple on top of a book or a book
*  on top of an apple or whatever. And so they've been slower on the uptake with that sort of stuff.
*  I do think that will change. People are creating that data. There's all sorts of techniques,
*  looking at videos and multimodal is making a dent in that. Standby for robots that actually do have
*  common sense spatial reasoning. I don't think you'll have to wait too long. But this is at
*  least just one broad class of example where it's just obvious that people are pretty much strictly
*  better than the AIs. And these are just weird results, right? Superhuman in translation,
*  above average in programming, but usually not cutting edge. And then just, frankly,
*  laughable mistakes in common sense spatial reasoning. Now you have to think, geez,
*  there's a lot of skills out there in the world. There's a lot of tasks that one could perform.
*  There's a lot of taxonomies that you could put onto all these different tasks. How do we have
*  an intuition for what AI can do well and what it can't do? That is really a hard problem.
*  Malcolm Gladwell famously said that you need 10,000 hours to have real expertise in a given domain.
*  I would say what passes for experts today in language model performance are people that have
*  put a few thousand hours into this. I maybe have put, depending on exactly what you count,
*  somewhere between two and 6,000 hours over the last three years. And I would put myself definitely
*  in the expert category, although there are those that would have better, more well-rounded sense
*  than me. But that's just where we are. You could maybe even say that there are no true experts
*  at this point because nobody's had a chance to put their 10,000 hours in.
*  Still, the benefit of a few thousand hours is quite substantial. Ethan Malik also says, by the
*  way, that if you're just working with a new model and you already have that expertise and you want
*  to fine tune, if you will, your understanding of a new model's strengths and weaknesses, that you'll
*  probably need to spend 10 hours talking to it to get a solid understanding of its strengths and
*  weaknesses. And if I do say so myself, I think it's quite helpful Twitter thread about how to
*  take a new model and figure out what its capability levels are and a number of different
*  techniques for doing that. I like that rule of thumb. I definitely recommend, especially people
*  in business looking for practical application of AI. Ethan Malik would be my number one account
*  on Twitter to follow. He's got a good book out as well. And that 10-hour stat comes from him.
*  So I'm going to try, right in the next slide, heroically try to give some intuition for what
*  AIs can do and what they can't do, but just know that for any given thing, your intuition,
*  especially for new to this, may fail you. There's no substitute for testing and it can be extremely
*  valuable to have some expert opinion to weigh in as well. But here's my rundown. When it comes to
*  breadth of knowledge, AIs are genuinely superhuman. As we all know, they've read the whole internet.
*  This translates to a breadth of knowledge that no human expert can match, right? When you look at
*  the MMLU test, it's like the AIs are now scoring at expert level, but to like expert in domain,
*  no human is scoring 90 plus percent on these MMLU score, almost vanishingly. A few humans
*  would be scoring at 90% on MMLU across the whole range of domains that it encompasses.
*  So that's a huge strength of AI. Depth, on the other hand, human experts still know best.
*  In Brazil, I told the story of how I was planning that trip to Manaus. I actually had a conversation
*  with Claude at 3.5 about the trip. And I asked it, first of all, said I'd been to Rio de Janeiro
*  before. I was going to be in Sao Paulo for this event. I wanted to go to one other place in Brazil.
*  Where should I go? It gave me a number of suggestions, including to go to the Amazon region.
*  And when I dug into that further, it was even able to get down to the specific
*  river cruise operator that I ended up going with. And this was just a one boat company
*  owned by a single guy. Memorized enough of the internet to know about that company,
*  to have a little bit of a sense for what they are all about. When I got there, the guy, first of all,
*  could not believe that that information came out of an AI and that's how I ended up on his boat.
*  But then he was also a useful contrast to the AI in the sense that he is a real expert on the fish
*  of the Amazon and knows way, way more than any AI would. First of all, in terms of just
*  recognize different fish, what kind of habitats they live in, where you'd find things, how they
*  reproduce, what the temperature and acidity of the water is, all that sort of stuff. He was obviously
*  head and shoulders above what an AI would be able to do. So hopefully that little anecdote gives some
*  intuition for the AI depth is not bad, right? Getting me down to that one fish and it gave me
*  regional dishes that I should try and a lot of different things. But the human expert on the
*  ground there still knows the fish of the Amazon far better than the AI. Insight is really, I would say,
*  the biggest advantage for humans right now. Human experts have these eureka moments that somehow
*  look at the vast space of possibility and into it often in a way that we can't even fully verbalize
*  or explain how we're doing it. But we have this ability, certainly the experts do, to unlock a
*  problem, to find that solution, to have that sort of inspiration breakthrough moment, that eureka
*  moment. And AIs probably don't do this. We are seeing very few of these moments happening with
*  AIs and they are typically significantly brute forced, which can be an effective technique.
*  We just recently had a paper announcing a system that had achieved silver medal performance on the
*  International Math Olympiad. And that is high level performance. When humans do those problems,
*  there's real insight involved in figuring out how to solve those problems. The AI systems take a
*  more brute force approach. They'll try a ton of different things. This is also true in the state
*  of the art usage of language models for the Arc AGI challenge. Those approaches involve
*  generating a ton of Python programs and then trying to figure out which ones are actually good and
*  why they might be failing and so on and so forth. So they're much more brute forcey than the humans
*  and they just generally don't generate as many eureka moments. So this is one of the biggest
*  things that I watch for right now are what sort of eureka moments are we seeing? How many are we
*  seeing? What sort are we seeing? Where are they coming from? For now, still major edge for humans.
*  Major edges for AI again include speed, cost, availability and scalability. These are all just
*  very practical. In some ways, this is like really why AI is most exciting right now. It is better
*  in some ways than humans, worse in some ways than humans when it comes to capability. But if it can
*  do the job, it's probably going to do it 10 times faster or more. They can generate text faster than
*  we can read it. It's going to do it 10 times more efficiently or at 10% or less of the cost.
*  That estimate for me, by the way, includes the cost of setup. Obviously, it depends on your volume
*  and value of task and all that sort of thing. But typically, you're going to see at least an
*  order of magnitude cost reduction. You can create qualitatively new and better experiences for
*  customers as Klarna did because AIs are available 24-7. It's also pick up where you left off. It's
*  not just that it's available 24-7. It's that you can have a long running chat and come back to it
*  anytime. I think that's actually a dramatically underutilized feature, even if just like chat
*  GBT and Claude, that they have your full history there. You can go extend, ask one more question
*  about anything else that you've ever previously talked to it about. That's just super useful.
*  Similarly with scalability, if you get 1,000 jobs at once all of a sudden, with today's APIs
*  subject to your rate limit, you can run 1,000 instances of the AI to that job and just turn
*  through them in basically no time. That combination of availability and scalability is really valuable
*  in terms of actually spending resources to do work when work is available and not having to have
*  somebody sitting there all day waiting for the next job to come in, which is certainly a reality
*  in many businesses, particularly many small businesses. Context, as we've talked about a
*  little bit already, is definitely an advantage for the experts. The AIs know nothing about
*  your specific circumstance, your business, your project, what have you. They're going to need to
*  be told everything. Human experts certainly pick up a lot. I would say sometimes we miss important
*  context too, but we're definitely notably better on this than the AIs are. Then finally, memory.
*  If I've learned anything from my experience working with AIs over the last couple of years,
*  it is to appreciate the quality of my human memory. The fact that it can remember so many
*  different kinds of things, experiences, facts, even sensory data, new skills, muscle memory,
*  that happens pretty organically without a lot of effort on my part. It is just a rolling thing
*  that's constantly being updated and it's all integrated and it's all pretty accessible for me
*  on a moment to moment basis. That's amazing. It's not perfect, of course. I definitely do
*  frequently have the experience of what was that link? What was that paper call? How do I get back
*  to that? But compared to AIs, I've come to really appreciate how useful the human memory system is.
*  People are working on this a lot. Of course, if you listen to this podcast, you've heard
*  about things like Hippo-Rag where people are starting to take inspiration from the structure
*  of the human memory and trying to create AI systems that mimic those properties. AI memory
*  is getting a lot better and also the context windows are getting just dramatically better.
*  There is a lot of progress in human memory. In fact, you know what? I'm going to go ahead and add
*  one more plus here. The reason I go from one to three pluses there is that it seems ultimately
*  AI memory is destined to outperform human memory. Just the fact that there's functionally infinite
*  drive space that you can query against, that multiple AI systems can share that hard drive
*  space, the ability to query it at super fast time. That all seems just hugely, undeniably powerful.
*  What's missing right now is the right architectures for AI memory. But as those come online,
*  the fundamental hardware advantages and scalability advantages of AI memory, I do expect ultimately to
*  dominate. But definitely human memory is still much more useful and intuitive to deal with than AI
*  memory. Hopefully that gives you a good intuition of what AI can do, what AI cannot do. This is,
*  of course, critical to choosing what sort of task you are actually going to try to automate
*  with AI. I would also just sanity check anything you're hearing from an AI advisor,
*  anybody who's trying to sell you AI services against this list and make sure that what you're
*  hearing from them matches up with this. I'm pretty confident in this analysis and I would
*  definitely consider a bit of a red flag if somebody was coming at me with a very different
*  interpretation. Though, of course, we could debate things at the margin. So let's imagine now that
*  we have chosen a task to automate. And let's imagine that we are going to try to do something
*  along the lines of what Klarna did. And we're going to try to automate some aspect of customer
*  service. Now we enter the portion of the project that is understanding the work. And by the way,
*  that could be pretty quick. Choosing what work to do. If you have the expertise to know what AI can
*  do and not do it, you've thought through this a number of times, that could be something you
*  could do in just a couple of hours. Discussing the business, looking at pain points, getting a
*  number of ideas on the table. It doesn't have to take a long time. I always remember Tyler Cowan,
*  famous blogger, personal hero of mine, and well-known super prolific reader. When he's asked,
*  how long did it take you to read that book? He always answers with his age, because his idea is
*  that reading is a lifelong thing. And it's not about how fast I would get through that book.
*  It's about all the reading that I did in the past. So it'd be in position to get through that book
*  really fast. And the same is true with this initial step of choosing the work for the AI to do.
*  You can do it fast if you have the expertise. But where that time goes, however many thousand hours,
*  goes to getting to the point where you have the expertise to have the good judgment to actually
*  do that work fast. Again, this is where an advisor can be really valuable. And hopefully, this
*  presentation facilitates a lot of those relationships. Okay, so now we're imagining we have chosen
*  customer service as the target for automation. Now we have to really understand the work,
*  deeply understand how and why the work gets done. When you ask people how work gets done,
*  many times you're going to get a sort of superficial high-level answer. People don't
*  actually spend a lot of time thinking in a meta way about how they do what they do or why they
*  do what they do, especially people who are doing routine work. They learn how to do it. They show
*  up and do it. So hopefully they like their job. In many cases, they don't love their job, but they
*  don't put a lot of extra thought in many cases into the meta of the work. They're just executing.
*  Now, the problem with that for the purposes of trying to help automate aspects of their work
*  is that they don't tend to give very detailed answers of how that work gets done. You'll get
*  answers. Oh, it's pretty simple. All we do is we get a customer service ticket in our system.
*  We respond to that ticket. We close the ticket. How hard could it be? That's not that helpful,
*  though. Obviously, if you're going to really try and automate it, you need to dig deeper. This is
*  really a social skill set right now that we're talking about when it comes to understanding the
*  work more so than a technology skill set. You have to ask those follow up questions. Dig in.
*  Okay, really. But how do you do it? I really like to use this phrase. Let's break it down step by
*  step. Astute listeners will know, of course, that this is a famous prompt for language models that
*  improves their performance. It also really improves people's performance and the quality of
*  analysis that they can give you about their own work when they'll actually engage in this
*  breaking it down thought process. If you ask a question like that to that same person,
*  how do you handle a customer service ticket? You dig deeper and ask them to break it down
*  step by step. Then you'll typically get a more detailed answer. A person might say,
*  actually, you're right. There's a bit more to it. Maybe you get something like this. Okay,
*  we get a ticket in, then we have to go find that customer account in our system. Then we prioritize
*  the ticket because we can't respond to them all immediately. We want to make sure we're responding
*  to the important ones in a timely way. Then once we do that, that kicks off another process where
*  somebody takes the highest priority ticket and then they have to go find the right documentation.
*  Then if they can't find that documentation, then they'll send that to the product team.
*  If they can, then they'll write and send a response. Then we can close the ticket. Okay,
*  much better. Now we're getting somewhere. I really like to look at these diagrams and think,
*  where are the pieces here where intelligence is truly required? In this case, I
*  mark those as black boxes, the black boxes of intelligence. Now, it depends a little bit on
*  the circumstances, but just to give an intuition for what I have in mind, finding a customer account,
*  that is something that in theory, especially if you ensure that your ticket form gets the
*  customer's email or requires them to be logged in to submit one or whatever, then that can be
*  fully automated. You can take their customer ID or their email and you can run a database query
*  and you can get their account information back out of your system. You can do that in a way
*  that doesn't really require on the fly intelligence. You can specify the rules to do that in a fully
*  algorithmic way. Whereas prioritizing the ticket, that's about not only understanding who the
*  customer is, but also what the situation is. If we wanted to dig into that subtask a little bit more,
*  then I like to ask the question, how do you think about it?
*  Sometimes you might even just want to record people's answers to these questions so you can
*  capture everything. Oftentimes, what I find here is you get a data dump all at once. Sometimes it
*  starts off with people saying, oh yeah, actually, there's a lot that goes into that. Then you can
*  start to hear all the different considerations that they work with when they do something as
*  seemingly simple as prioritizing a ticket. Just some questions that people might be asking are
*  like, how many tickets do we have open right now? Does this customer have a particular contractual
*  guarantee from us? Are they a free plan? Are they a paid plan? Are they a VIP? What kind of information
*  did they give us? Did they give us useful information? Is it an issue we already know about
*  or are perhaps already working on? Or do we already have a solution? Just how upset is the customer?
*  I think in many businesses, the squeaky wheel, of course, gets the grease. Is this something that
*  to affect others? Do we need to take some additional action or is this just locally
*  contained to this user? Those are just some of the things that I came up with in thinking about
*  in a generic way what would go into prioritizing a customer service ticket. But it's going to be
*  different in every business. You really need to understand in this particular context what are
*  the questions that people are asking and how are they making these determinations. The next step is
*  to truly document that process. You need to get examples of what great work looks like in this case.
*  That means you will need to collect the inputs and the outputs and even more importantly, perhaps,
*  or most importantly of all, the reasoning that led from those inputs to those outputs.
*  You could also call this the chain of thought if you want to use an AI term, but it is all of those
*  considerations. What questions were people asking? What factors were most important? What was the
*  thought process that went into the transformation of the input to the output? In this case, we've
*  got the customer service ticket. We've got the prioritization level and we want to understand
*  as deeply and as much detail as we can the reasoning process that the person went through
*  to go from input to output. This typically does not exist. This is where we are making implicit
*  context and implicit know-how explicit because people generally are not writing this down.
*  They're taking that ticket. They're thinking about it themselves for a second. They're making a
*  classification and they're moving on. It takes too much time to write all this stuff down. Very few
*  businesses actually collect that reasoning information in any sort of native way. I would
*  submit, by the way, that this is one reason that AIs are not as good at reasoning because we just
*  don't have as much data exhaust, if you will, of all of our mental processes as we do of all these
*  other sorts of artifacts. It's critical to capture that so that the AI can learn from it.
*  As a general rule, I recommend 10 gold standard examples to start. The good news is you don't
*  actually need that many. It is a pain in the butt sometimes for people to actually sit there and
*  think about all the considerations. Sometimes it takes a couple sessions too because they might
*  write five things down and then they'll go back and do their job for a little while. Then as they
*  do that, they'll realize actually there are six, seven, eight, nine, 10 considerations that also
*  are in play sometimes. They're not always mentally available to people just the first time you ask.
*  Sometimes they actually have to go through examples to surface all of the considerations that really
*  matter. It doesn't take that long in most tasks to generate these 10 gold standard examples.
*  In some cases, it's really just a matter of backfilling the reasoning. You may have the
*  inputs and the outputs, but now we need to fill in that middle of reasoning. I cannot emphasize
*  enough that if you can't get 10 really high quality examples with reasoning, that you are
*  not going to be able to automate this work successfully. This can happen for all sorts
*  of reasons. People may not want to do the reasoning step. They may just other priorities, whatever,
*  but this is just central. This is one of the absolute most important checkpoints on your
*  path to AI automation that you have to hit. If you can't hit it, you are going to be in real trouble.
*  To cast this in terms of the business owner's perspective and the AI advisor perspective,
*  really you want to have an agreement that this is one of these milestones that you're going to
*  get to in a project. It's relatively early still in this overall process. We haven't even started
*  the AI implementation yet, but we have to get there. If we can't, we're not going to be successful.
*  Business owners should be looking for their AI service providers to put some work into this,
*  even though it's not always super glamorous. It's not always the most cutting edge feeling thing,
*  but that is something you should be looking for. AI advisors should be setting expectations with
*  their clients that we are going to need to do this. It's going to take a little legwork to set this
*  up and we have to have examples for the AI to learn from. Now, a couple of notes before we move
*  on to the actual AI implementation. This is basically it. If you have 10 gold standard
*  examples, you are in position to begin the implementation process. You may find in some
*  cases, and I would caution against being too aggressive about this again, especially early on,
*  if you're new to AI automation or you're new to providing AI services to a business, I would not
*  rush into redesigning processes. It is much easier. It is much lower risk and people are very happy in
*  most cases to get wins on just taking a piece of their process that they don't really enjoy
*  doing and getting AI to do it well. That is an eye-opener for most people. If you're the AI
*  service provider and you do that on the first go, you'll be invited back. I would generally
*  recommend starting modestly, working within the existing processes, but the next level,
*  and it sometimes might even be the first level, is to also think, what if we did it in a little bit
*  different way? In this case of the ticket prioritization, really the reason that we're
*  prioritizing tickets, I snuck this in my initial description, is that we can't respond to them all
*  right away. But if you think about the strengths that AI has relative to humans, in particular,
*  its speed and its availability and its parallelizability, then you could also realize that
*  this prioritization step is superfluous in an AI-powered way. If we could get the AI to actually
*  write the responses effectively, and AI could write all the responses, maybe we could even still have
*  a human review as part of that process, but we wouldn't really need an explicit classification
*  step at all. We would just need to make sure the system is running well and AI can scale as it
*  needs to. My recommendation, again, in general, is to make this a step two. It's often tempting
*  to jump to the very best thing, but just many businesses are not quite ready for it. If it
*  doesn't work or expectations aren't quite met, and the more you deviate from current process,
*  the more expectations can get out of whack. That's why your best attempt to manage them,
*  people can get quite frustrated. I think this is, in some ways, the bigger value, but people need
*  to climb that ramp for themselves typically to get to that big value. I think that's really
*  important for especially AI service providers to keep in mind. It's also helpful to think through
*  just how do you prioritize? Let's say we were considering multiple different things that we
*  might want to automate with AI. It's funny how sometimes what people want to automate is just
*  most personally painful for them. I just set up three different scenarios here just to illustrate
*  the contrast. One is that somebody might want to get AI to answer their investor questions,
*  and they may think, geez, that's quite high value. I value my time so much and I spend
*  every much time doing it. Volume isn't going to be as high. Maybe the total realizable value
*  could be higher even than some much larger number of service tickets that we have to answer just
*  the value of one unit is so high. I would just keep in mind there that going back to that
*  checklist of what's a good target versus what's a bad target, where you're probably going to fail on
*  some of these things or you're going to really struggle is what does a great job look like
*  in answering an investor question? That's probably a lot more variable and also a lot more contextual
*  than answering a customer service ticket. In a customer service ticket, you have a pretty
*  good sense we want to be consistent. This is how we want to show up. In answering an investor
*  question, you probably do it differently for different investors depending on the relationship.
*  It's always very up to the minute questions, typically what were last month's numbers or
*  whatever. The context for that may not always be readily available. There's just a lot more
*  difficulty in something like answering investor questions. I would say you want to both look at
*  the expected value of the task in terms of unit value, in terms of volume, but then also make
*  sure that you're effectively discounting by the percentage chance that this just won't work.
*  In general, I would say, again, with the theme of starting with relatively easy wins, you're going
*  to want to usually pick things that are a little lower value, a little higher volume with higher
*  chance of success. Businesses may vary on this, but at a minimum, if you're providing AI services,
*  you want to get this risk conversation on the table sooner rather than later.
*  Okay. That brings us to the portion on optimizing AI performance.
*  This is going to be obviously pretty superficial because there's a ton to be said about this topic,
*  but these are the things that I think are most important for people to know.
*  First, I borrowed this chart directly from OpenAI. I was excited to see that they have something
*  like this now, which they didn't until fairly recently. They break AI performance optimization
*  down into two different dimensions. I really like them, but I think I can offer better labels.
*  They call them context optimization, aka what the model needs to know, and then LLM optimization,
*  how the model needs to act. I'm going to call those optimizing the information that the AI has,
*  and then also optimizing the behavior that the AI exhibits.
*  Three core techniques that we're going to get into are prompt engineering,
*  retrieval augmented generation. This is when there's a lot of information. Can we, at runtime,
*  selectively retrieve certain information and use it? Then fine tuning is actually making a custom
*  model that is derivative from the base model that is trained specifically in the task that you want
*  it to do. Let's break all of these down. Of course, the payoff in many situations is that you might
*  need multiple or even all of these different techniques. Let's start with prompt engineering.
*  There are a ton of different prompt techniques. Of course, I'm going back to the situation here
*  where we are keeping the prioritization step. We're not redefining the whole process just yet,
*  but this is basically my blueprint best practice prompt that I use always when I'm starting
*  something like this. A lot more, many other tips and tricks out there, but this is the core stuff
*  that I use every single time. First of all, I tell the AI what its role is. Usually that's in the
*  context of automated work. That's a professional role. You are a customer service agent.
*  Then I tell it what its task or its job is going to be at this point in time. Your job is to assign
*  a priority level to a ticket. This is very clear. It's the brief. It's the context that they need
*  these things. Then comes the instructions. This is the clearest distillation that you can come up with
*  of all of the considerations that you gathered when you took the time to interview the people
*  that are actually doing the work today and understanding as deeply as possible how they
*  are doing it. This can amount to communication of vibes to the model. We want to show up like this.
*  We want to have this tone. We want to have this attitude. It can also just be explicit rules.
*  If a customer is VIP, then it's automatically high priority. This could be paragraphs long. It
*  could even be pages long in today's world. Genuinely, the better there for the most
*  advanced models. Then I like to tell the AI what format I want the response in. I'm always going
*  to ask for reasoning before answer. My mantra for this is for AAA results, analysis before answer
*  always. You've got to have, and I've seen people make this mistake so many times, if they put the
*  answer first and then the analysis, what you get there is just post hoc justification of the answer.
*  One of the most common ways that I see people getting way lower performance out of language
*  models than they really could or should. Always have the reasoning or the analysis coming before
*  the answer. You can tell it in detail what format you want it to answer in. I don't want to get too
*  gnarly, but some XML or JSON formatting should be fine. Then we get to these gold standard examples.
*  This is the examples that we want the thing to learn from. This is sometimes called few shot.
*  It's sometimes called K shot. That's what Riley Goodside called it on our recent episode.
*  This is the 10 gold standard examples that you chose with all of the inputs, the reasoning that
*  you captured about how those inputs were transformed into outputs, and finally the outputs that were
*  created. Here I actually have a response. This really should be just a prioritization. Cool.
*  Now, if you had 10 examples, then the most examples you can use for any one test is nine.
*  You can set up 10 different tests with your 10 examples by each time taking nine of the examples,
*  using them in the prompt. Then for the 10th one, only giving it the inputs and having the AI do
*  the job of reasoning through that 10th problem and giving you the output for the 10th instance.
*  10 examples gives you 10 tests, each of which have nine examples to learn from. That's actually
*  pretty good. At that stage, you can take a step back and say, okay, for all of these different
*  10 things with nine other examples to learn from, did I get good results? This is really the first
*  place where you want to have a serious check-in with yourself or with the client, as the case may
*  be, to assess, is this thing working? Are we getting there? Often in today's world, this can
*  be enough. This is not optimized necessarily for cost or efficiency yet, but this can be enough to
*  get you pretty good performance. If it is, you're in business. Downstream, additional
*  optimizations are really just refinement. If it's not, then you've got more work to do. Why isn't
*  it working? This is where some of the other techniques will come into play. Again, there are
*  tons of advanced prompting techniques. I'm not going to get into these here. We had a good episode
*  on this recently with Sandor Schulhoff, who's the author of The Prompt Report. It's an 80-page paper
*  that has over a thousand different prompting techniques to get to the point where they feel
*  like they have a comprehensive survey of everything that's happening in prompting.
*  These are some of the things that really jump out to me as most relevant. The number one thing that
*  I would look at is actually just working with a language model to help you refine your prompt.
*  If you go into the Claude console today from Anthropic, they have tools in there that help
*  you do this. They can really help you clarify language. They can help you expand on prompts.
*  Sometimes you may have to refine what it gives you, of course, because, again, they don't know
*  the context, but it, at a minimum, can give you a really good idea of the kinds of things that can
*  be useful to include. If you need more, go there. I would say most of the time, the basic blueprint
*  that I've given you here should be enough to get pretty good performance. If it's not even close,
*  you may have chosen a bad task. Now, optimizing information. In this scenario,
*  we've given it nine examples, but sometimes we may have to get additional information
*  at runtime to give the AI all the context that it needs. Retrieval, augmented generation is a huge
*  topic. We've definitely covered it in different episodes in different ways. The basic scheme here
*  is that when a user input comes in, the inputs to the task, there is going to be some process by
*  which additional inputs are gathered. Those can be fully deterministic. That doesn't necessarily
*  mean there's any intelligence required. That could just be the step of taking the user's email,
*  querying against the database, pulling in the account information. That's private data.
*  It could also be fully deterministic public APIs. Maybe you have a task where you need the weather
*  or you need the current stock market numbers or whatever. You can just go to some public data
*  sources and get the latest information. Then sometimes you'll need to use more advanced,
*  more AI-centric techniques to find the most relevant content out of unstructured data.
*  Most common example I see of this today is when people want to set up a bot to answer questions
*  about company policy. They'll put all this company policy into a big vector database in embedding
*  form. If you don't know what that is, there are other episodes for that. But then you can take
*  that question, map it to the same vector space, and pull out the most relevant information from
*  that vector database. Then work all that into the full prompt, have the AI do the intelligence piece,
*  and finally give you the outputs. This is definitely a complication, but it is often
*  a necessary complication. Because even though the language models now can take a lot of input data,
*  they can't take all the input data that you may have. Sometimes you have to have up-to-date
*  information. You may need to integrate something along these lines to get the information that you
*  need. That was optimizing the information that the AI has at runtime. Again, my biggest tip is to make
*  sure you include enough context and to err on the side of more context, more than is perhaps
*  necessary as opposed to not enough. Always remembering that the AI knows nothing about
*  your situation, nothing about your business. It has this general world knowledge, but it knows
*  nothing about you. So it cannot make good guesses there unless you give it the right information.
*  So more information rather than less is always the mistake to make first, and you can dial that back.
*  Finally, we get to optimizing the behavior of AIs. This is really probably the most complicated
*  process and certainly the most complicated slide in this presentation. But I think ultimately the
*  intuition here should be pretty straightforward. The good news is that the language model providers
*  these days make this really very easy to do. You don't really have to do any of the heavy technical
*  lifting. Your focus is going to be entirely on the examples that you've collected and evaluating
*  the model's performance. So how do you optimize the behavior? If you're not getting enough from
*  just putting a few examples into a prompt, as we discussed in the gold standard prompt format,
*  you can then move on to fine tuning. Fine tuning basically is actually making you a custom model,
*  adjusting the weights, adjusting the numbers that are inside the model that do the computations
*  so that they are tailored to your specific task. Fine tuning generally does come with one really
*  big trade-off, which is that you get better performance on the task that you're training for
*  or perhaps a few tasks. You definitely can do multi-task fine tuning, though it can be a little
*  complicated. Mostly I would say start with one task and work your way up. You'll get better
*  performance on that one task. The trade-off that you will face is that the model will become worse
*  at everything else. So the general rule of thumb is one fine-tuned model for one task or maybe one
*  fine-tuned model for a few tasks. How does it work? You start again with your gold standard examples.
*  You have to format them into a chat format. There are helper libraries out there now that can do
*  that for you. You can do it out of a spreadsheet. You can do it with just a tiny bit of code.
*  You can upload a CSV into some of the fine tuning platforms like OpenAI. These days OpenAI GPT-40
*  Mini is available for fine tuning. It really doesn't cost much. It's only $3 per 1 million
*  tokens to fine tune GPT-40 Mini. That is currently, I believe, still the third, certainly in the top
*  five, highest rated models on LMSYS, which is pretty impressive. $3 for 1 million tokens, that is
*  really unbelievably affordable. Then it's only 30 cents per 1 million tokens. That's double the normal
*  price, but only 30 cents per 1 million tokens input. So you can really go wild with this and
*  not have to spend a lot of money. Your first round with just 10 gold standard examples is going to
*  cost you almost nothing. What you do is upload those into the platform, let the platform do the
*  work, whether it's OpenAI with GPT-40 Mini or Google with their Gemini Flash model that is now
*  available for fine tuning or Claude. Haiku is also available for fine tuning. That's a little bit
*  harder to get access to because it's just in preview at the moment of this recording on Amazon
*  Bedrock. But all these are happening. And of course, the Llama 3s are out there now for fine
*  tuning as well. Pick a platform that allows you to just upload examples, let them do all the hard
*  work and give you back a custom model specific to your task. That won't even take long. In the case
*  of OpenAI, it's typically minutes. If you're just using a few examples, sometimes you can get caught
*  in a queue, but usually it's very fast. And then amazingly with OpenAI too, you have the same
*  rate limits and the same scalability with your fine tuned model as you do with their normal
*  publicly available models. And that is really incredible. That is not something that I've seen
*  open source providers make available yet. Typically, if you're fine tuning a Llama and
*  you want to deploy that, you have to rent dedicated capacity. So you pay by the hour that model is
*  available. OpenAI does not charge that way. So the big tech providers here do have some really
*  nice convenience advantages relative to open source. Obviously, I think they'll all work for
*  many use cases, but the question of convenience for me very often does come down on the side of
*  the big tech providers. Okay, you upload your examples, they do the actual hard work, then they
*  give you back a model. Now your question is, is it working? And basically you're going to have four
*  possible scenarios here that I'll work through in turn. One is that it might be not working.
*  This would typically mean that you have chosen too ambitious of a task. And if you're not even
*  close after 10 examples, then my recommendation would be to revisit the choice of task and probably
*  break it down further into smaller tasks and perhaps pick one of those smaller tasks to focus
*  in on. If you're asking the language model to do too much at once and it's just not getting
*  close, breaking it down into subtasks is almost always the next best way to go. So that unfortunately
*  would send you a little bit back to the drawing board. You might have to break your existing
*  examples up into different subcomponent examples. There could be some non-trivial work there that
*  you'd have to do, but then you would come back with a simpler task and try again. Hopefully you avoid
*  that. Certainly seen it happen, including to myself. Hopefully you don't have to do that. If you do have
*  to do that and you succeed, you get down to the scope of task that a language model can in fact
*  succeed on, then probably what you'll see is that it'll be close, but maybe not quite working as
*  well as you would like. This is very common. And what I typically recommend here is just going and
*  getting more examples. You're on the right track, but the AI hasn't learned enough. There are
*  typically some settings in the fine tuning process where you can say how many runs, how many epochs,
*  or how many passes through the examples you want to take. You can turn that up a little bit,
*  but I wouldn't turn it up too much because you'll start to run into what is known as overfitting,
*  where it will overlearn from just a few examples and you'll start to see weird behavior where it
*  parrots those examples. You don't want to do too many epochs through a small dataset. So what you
*  need to do is expand the dataset. Now you can go back to your team and say, hey, I need a bunch
*  more examples because we're on the right track, but it's still not quite working. The trouble is
*  that every time you want to increase the size of your dataset, you don't typically just need to
*  double it. Usually you need to 10x it to take that next step in quality. So if you started with 10
*  great examples, now you need to be thinking more on the order of 100 great examples. And that can
*  start to be a lot to ask people to do, especially if they're not accustomed to writing up their
*  reasoning and now you're asking for this painstaking process. People don't always love that. It
*  certainly at a minimum is going to take a significant amount of time. So what most people do in practice
*  is not actually write those next 90 examples from scratch, but instead they use the model that they
*  just created. If it is close, but not quite, they do a bunch of generations and then they filter and
*  sometimes correct those generations to build up their dataset. So let's say it's working
*  50% of the time really well and the other 50% of the time is falling short. You could just
*  generate 200 examples, run through them, identify the ones that are working well, take those 100
*  and make that the expansion of your dataset. That's the most efficient way from a human time
*  perspective to build up that 10x bigger dataset. Now it does still leave the problem that what about
*  those other half where it wasn't working? Is it going to learn from the half that was working to
*  do it the right way on the other half? Maybe, but you also would be well served if you have the time
*  to look at those failures and to start to correct some of those failures. You don't have to do that
*  in the first loop, but it certainly helps and what you'll see is that's coming next for us in any
*  case. So one way or another, you get up to that next scale of examples, you run that fine tuning
*  process again and again you get out another custom model and again you ask is it working.
*  You might have to go through that a couple times. Typically you don't have to go past a thousand
*  examples for a regular single task. I would say if you're at a thousand examples and it's still not
*  working, you might be back to a task decomposition sort of scenario. At a hundred, certainly at a
*  thousand, typically you'll find that yes it is working. For most cases it is working on par
*  with the examples that we gave it. It seems like it would be viable in our business. It's consistent
*  enough that we can mostly trust it and typically what remains is just a matter of edge cases.
*  This is the sort of uncommon scenarios that people don't encounter super often that maybe
*  they didn't think of when they were creating the examples and yet when they do pop up, people
*  because of the implicit context that they have know what to do, but the language models because
*  they lack context don't know what to do and can still get it wrong. So this is why it is really
*  important to have visibility into what's happening, especially in the early phases of deployment,
*  always setting things up such that you're going to get quick notice if things are going wrong.
*  As these edge cases pop up, maybe you have users alerting you, maybe you have a human review
*  process, it's obviously all going to depend on the risk and reward and the resources that you have
*  available, but they likely are going to pop up. Then what you'll need to do is just patch the
*  data set to address those edge cases. The good news here is you typically, once it's working pretty
*  well, and the difference between kind of not quite working and yes, except for edge cases is
*  how much more data you need. When it's not working that well, but you seem like you're on the path,
*  you need to 10x the data to get to that next level of performance. But if it's actually mostly
*  working and it's now just a matter of correcting certain edge cases, then you don't usually need a
*  huge amount of additional data. And I actually recommend just identifying five of those edge
*  case failures. They can be synthetic to some degree. Sometimes you'll see one edge case and
*  it will remind you of, oh, this can take a few different forms. So build that out, can be manually,
*  can be in a variety of different strategies for building it out, but make sure that you
*  correct the behavior and show exactly the chain of thought that you want it to use.
*  And that will typically be in stark contrast to the chain of thought it actually used when it was
*  doing the wrong thing in these unusual scenarios. Small number of examples to correct these edge
*  cases, really focusing on correcting the behavior, showing the model exactly how you want it to reason
*  in this scenario. Again, back to the fine tuning, rerun it, come back to the model. Is it working?
*  It should be working. It would be a very unusual situation if it was working before. And then you
*  added a few edge case examples and it went backwards. Not to say that can't happen because
*  these things are weird and weird things do happen, but typically it will continue to be at least yes,
*  but for edge cases. And you might have a couple of rounds of this. Different types of edge cases
*  may pop up as you go through this process. Eventually, hopefully, and probably for most
*  things, you will get to the point where, yes, it really is working. You've identified the most
*  common edge cases and you're up in the level of human performance or hopefully even better.
*  And then you can say, yes, we have some success. Generally do recommend, and this is really
*  important for the conversations between the AI advisor and the client, if that's the dynamic,
*  plan for three rounds of core fine tuning. That's like your 10 examples, 100 examples,
*  1000 examples, and then plan for a few more rounds of patching edge cases. That's really
*  just important for managing expectations. It's really important for allocating the time to look
*  at the results for just being out the calendar time for how long is this whole thing going to take.
*  This is almost always going to happen. Sometimes you can get away with just two rounds or even just
*  one round of fine tuning if the task is simple enough and if the examples are good enough. But
*  even then you're probably still going to have edge cases. So just go into it with the expectation
*  that this is what it's going to take and you won't be disappointed. In practice, a real expert
*  might bop around some of these different techniques and they'll use judgment to figure out
*  what should I do first? Maybe I want to do rag first. Maybe I want to do fine tuning first.
*  It really very much depends on the scenario. And this is really where this becomes a little bit
*  right now more of an art than a science. So if you're working with someone who's really good
*  and that you trust, I would say in many cases you have no choice but to trust their judgment
*  and they'll have to guide you on what will be the next step in that process. Even then,
*  it is more art than science I would say at this point and people are not always going to make the
*  exact right choice. And again, this is a diagram from OpenAI that shows how sometimes you're
*  bopping around in this space of possible optimizations. A few notes on optimization
*  best practices. First, I really always emphasize de-risking the entire process by doing the hard
*  part first. In the context of a broader workflow, what is the hardest part that we're trying to get
*  AI to do? Is that writing the response to the customer ticket? Is it still just prioritizing
*  the customer ticket? Whatever that hardest part is that black box intelligence, really dial in on
*  that first and get it working. If you can get it working, then all the easier parts typically
*  will fall into place and that includes all the automation scaffolding, your Zap, your Zaps,
*  your API calls, your webhooks, whatever. Whatever is actually going to integrate this into the
*  broader flow of the business. That stuff is typically deterministic software and definitely
*  can be built, but it's a waste often to build it first because if you later find out that,
*  oh, the hard part, I can't quite get to work or it's not working quite the way I thought,
*  then all that surrounding stuff ends up being wasted effort. So identify the hard parts,
*  and do them first to de-risk the overall project. I have never been sad that I did that. And if I
*  go the other way, oftentimes I do end up wasting effort. Next step is just maximize performance
*  first, then improve cost and speed. Again, the cost of fine tuning GPT-40 mini is $3 per 1 million
*  tokens. And the cost of running it is 30 cents per 1 million tokens input and $1.20 per 1 million
*  tokens output. In other words, it is extremely cheap to fine tune models and to run fine tuned
*  models in today's world. So I would not worry too much about the cost and speed while you're in the
*  early development process. I would work and focus entirely on making the performance hit the bar
*  that you need it to hit. If you can hit that bar and then you actually go measure the cost and speed,
*  you will almost certainly find it is a lot cheaper and a lot faster than the human alternative.
*  That doesn't mean there still won't be opportunity for refinement and savings,
*  but typically that'll be pretty marginal. And the main thing that causes these projects to fail,
*  if they fail, is that the performance just wasn't good enough. They almost never fail
*  for being too expensive or being too slow. Related to that, in terms of the performance
*  threshold, it's really important to compare the AI performance to human performance, not to
*  perfection. It is a shocking but almost invariably true observation about every business I've ever
*  worked with that the humans are not doing a perfect job. They may be doing a great job,
*  but they're almost never doing anything that really approaches perfect. There are mistakes,
*  there are oversights, there are typos, there are misclassifications, you name it. People have low
*  effort in some cases, bad days. It's definitely not perfect. The AI is not likely to be perfect
*  either, but I see a lot of examples ranging from self-driving cars, where the data seems to suggest
*  that the self-driving cars are already at least as safe and maybe significantly safer than a human
*  driver, and yet we're still nervous about it. Same thing happens in a lot of these AI automation
*  projects, where when the business owner or the stakeholders get together and they really
*  scrutinize the AI output, they find these little flaws in it. It's definitely worth,
*  maybe we're finding the data set, trying to address those flaws, but it is very much also
*  worth keeping in mind, what are the humans actually doing today? It's often quite eye-opening
*  and can be very well worth doing to say, okay, yes, let's really scrutinize these AI outputs,
*  but let's also really scrutinize the human performance that we might be shifting from
*  if we're going to move to AI, because I think people often have a notion in their heads that
*  it's great or it's perfect even, and it's almost always not. Again, remember too that each additional
*  nine of better performance typically takes 10 times more resources. When I refer to nines,
*  I'm talking like 90% correct is one nine, 99% correct is two nines, 99.9% is three nines, and so
*  on. A general rule of thumb, which of course will vary, is that you can get to 90% in many cases
*  with those 10 examples. To push higher into the high 90s, you're going to need those 100 examples.
*  To get past that, you might need 1,000 examples. That even might be a little bit optimistic. To
*  get to 99.9% right is pretty rare in today's world, even in those handwritten digits that we
*  covered at the top. The state of the art is 99.7. Partly that's because a lot of the data is weird.
*  Every so often you see this number and it's like, genuinely, we have no idea what that is. In that
*  data set, there is some answer, but perhaps there can be mistakes, there can be issues, there can
*  be all sorts of things. 99.9% is going to be very tough to achieve for most scenarios, but
*  you can get into high 90s very often. You can get to the point where your failures are minor,
*  and you just need to keep in mind that each time you want to take that step, it's going to require
*  10 times more work. That can lead you to some analysis where you're like, okay, this is
*  good enough. Do I really want to do 10 times more work, or is there some other way perhaps to address
*  any remaining shortcomings? It can be tempting. Sometimes we want to maximize. We certainly have
*  a maximizing culture, a maximizing mentality, but another thing to keep in mind is that the
*  technology landscape is moving very quickly. Rather than maximizing the current version
*  with 10 times more data, 10 times more effort, instead, I typically would recommend planning
*  for a next version and planning for some of the techniques that you're using to become obsolete.
*  It has actually happened to me multiple different times that I'm in the process of building out one
*  of these automations, and then some new technology becomes available that causes me to rethink how
*  I'm approaching it in the first place. That could be as simple as just a better model where, going
*  from GPT 3.5 fine tuning to GPT 4.0 mini fine tuning, for example, just expands the scope of
*  what the models can be fine tuned to do. That can actually allow the tasks that you're trying to
*  solve to get bigger. We talk about task decomposition to break tasks down to be small
*  enough that language models can handle them, but the other countervailing trend is that the models
*  themselves are getting better. They're able to handle bigger and bigger tasks all the time,
*  and so some of that breakdown, some of that refinement ultimately can become obsolete when
*  the next generation of model comes online. There's a lot of judgment, a lot of art to understanding
*  where are we now? How good is that? Is it good enough? How does it compare to humans?
*  How much more performance might we be able to squeeze out if we did put another 10x more
*  time and energy into it? How much value would that get? How long would it take? And what's the
*  background technology context here? Is that solution still going to be relevant after we
*  do all that work, or might we be better off taking what we have right now, banking the win,
*  and waiting for the next generation of model to come to us and unlock new possibilities?
*  There's no single or easy answer there, but I do think you want to keep all of these things in
*  your mind at the same time as you are making these decisions. The final tip, which has become a
*  mantra among AI builders, is always look at your data. Now, this is a bit of a contradiction
*  because I said that the goal of AI automation is to actually delegate the work to the AI
*  and to achieve enough confidence that you don't have to always look at the data. You don't have
*  to look at every single output. And that is true. So when I say always look at your data,
*  I don't mean you want to continue to look at every single output. That would defeat the purpose of AI
*  automation, but maybe this would be better said as never allow yourself to be disconnected from
*  your data or blind to your data. Always have some way of occasionally looking in and sampling
*  what's going on. This is especially important in the development process. When you're going
*  through this iteration of 10 examples and fine tune and look at the results, there you have to be
*  really dialed in on the data because that's all it has to learn from. And the quality of the data,
*  the nature of the examples you're giving, the nature of the mistakes that the model is making,
*  all those things are crucial to ultimately getting it to work. Even after it's working,
*  it is really wise to at least have some visibility into your data, though, depending on the level of
*  performance and confidence that you've achieved. And again, the risk context that you're operating
*  in, you do want to move on to other things and not have to look at every output, but just don't
*  allow yourself to be totally blind. Make sure that there's at least some system or some alert
*  that would sound if things were starting to go wrong. Okay. With that, congratulations. If you
*  follow all these steps, you are officially automating work with AI. And I can tell you,
*  it can be a real game changer for a business. In my case at Waymark, my kind of nearest and
*  dearest example, it used to be the case that people had to come to our site with an idea and
*  write that idea out themselves entirely into the video maker that we had. And people just struggled
*  with that. They were like, I don't have a lot of ideas. I don't like writing. It's hard to get the
*  words. We now automate that entire process end to end and people create 10 times more content
*  because we have taken so much of the work out. It can really be super transformative in work that
*  I've done with Athena. For example, similarly, we have an onboarding process where each new client
*  has a one hour phone call where we get to know them. We understand their life, their priorities,
*  what matters to them, how they spend their time, their family, their colleagues, all that sort of
*  stuff. That becomes a recorded video. And it used to be a four hour and about a hundred dollar budget
*  to take that video and convert it into a written document that we can hand off to the executive
*  assistant that was going to be assigned to work with that client. Today, we have an AI pipeline
*  that does that work. I would honestly say it does a better job than people were able to do
*  in that four hour time limit for that hundred dollar budget. And it does it for under a dollar.
*  We first transcribe the recording into a text transcript and then we feed that text transcript
*  into a prompt. And in this case, I don't even think we ever needed to find Tune. We were able
*  to get the prompt working well enough just using those basic things of all the prompting best
*  practices and a couple of examples and boom, here's your converted document. This costs now
*  well under a dollar because it was maybe upwards of a dollar earlier when the model prices were
*  higher as we've upgraded models to better and faster and cheaper models. It's now well under
*  a dollar. So over 99% savings relative to the old solution. We did have to put some legwork into
*  setting it up in the first place, but now we're here. We don't have to do that four hours,
*  a hundred dollars worth of work anymore. And we still get a better product. And the client
*  experience is exactly the same because the clients still have that one hour conversation with the
*  human. That's not going away. The EA still gets a great document that introduces the client to them.
*  That allows the EA to hit the ground running for the client. That process is exactly the same,
*  if not a bit better. And we're saving all this time and money. So it can really be transformative
*  for a business. As you get practice doing this, you'll also start to see more and more opportunities
*  to do it. Finally, just a few extras. You will face a lot of trade-offs in this process. Here are
*  some that are the most common. I just covered performance versus investment, right? How high
*  can we drive the performance? Keeping in mind that every tangible step up in performance is
*  probably going to require 10 times more invested resources. That's an important trade-off. And it's
*  not always about maximizing performance. Accuracy versus complexity is another thing. Again,
*  driving that accuracy as high as possible can sometimes be accomplished with more complicated
*  workflows. But is that always worth it? So for example, when we choose images at Weymark to
*  accompany a video, we used to do it in such a way where we would caption the image, we would perform
*  text recognition on the image. We used an aesthetic model to evaluate how beautiful the image is.
*  That was a very noisy and challenging process. And then we use all those inputs, fed those into a
*  language model, and had the language model choose. That's actually now become obsolete because now we
*  have multimodal models that can make much better understanding of images. But it was like, man,
*  we keep layering on all these different techniques. And they all helped our accuracy,
*  but they did come at real engineering costs to develop that solution. Similarly, with development
*  costs and inference costs, people are, especially engineers, right? Engineers have a, I find,
*  a very common bad habit of not including the cost of their own time in the cost analysis of what
*  something is going to take to build and run. They tend to think about mostly what it's going to cost
*  to run, which is the inference cost, right? That's how many API calls and how many tokens.
*  So I've seen engineers over and over again, be willing to put a ton of their own time,
*  which is quite expensive, into an effort to save on the margin what the application is going to cost
*  at runtime. And that is almost never a financially good trade. It sometimes can make sense to optimize
*  because you want to make it faster. And users don't like to wait. So depending on the nature
*  of your application, if it is super time sensitive, then it might be worth paying development costs
*  to bring a token countdown because it brings time down. But I generally would not recommend doing
*  that for purposes of saving money. Again, keeping in mind that models are getting cheaper. They're
*  already quite cheap, that there's obsolescence coming. The name of the game typically is
*  maximize performance. Don't worry too much about cost. Maybe worry a little bit about speed,
*  but build the thing as simply as you can to the point that it works as well as you can make it
*  work with reasonable effort. Launch it and launch it hopefully before something comes out and makes
*  it obsolete. This is a real issue. Another trade off, of course, is value and risk. I think this
*  one is pretty intuitive, but the more valuable tasks also tend to be riskier. So figuring out
*  where you want to operate, I typically, again, recommend low risk to start, even though that can
*  put a bit of a cap on value. There probably are some things that are very low risk that have enough
*  frequency that there is real value in your business, and I would start there. And then again,
*  false positives and false negatives are, this is the classic trade off in all sorts of systems.
*  Right? If you want to be sure that nothing ever sneaks through, then you're going to catch a lot
*  of things that you didn't need to catch. A good example of this that we see in the wild right now
*  that I actually just discussed on another episode is how the different foundation model
*  providers are calibrating themselves on risk. Gemini, for example, seems to be the most risk
*  averse. Not too surprising because it's coming from Google and they've got a big reputation and
*  a lot to lose. So they have decided that they will accept that the model will refuse to do a bunch of
*  things that it probably should do and really would be no problem because they want to make very sure
*  that it doesn't do things that they genuinely don't want it to do. Open AI seems to be, and I
*  would say also Anthropic, although Anthropic is a little bit weird, maybe doesn't fit so well into
*  this paradigm, but Open AI is on the other side where they will allow some things that the model
*  really shouldn't do because they really hate those inappropriate refusals. So how you're going to set
*  that threshold, depending on your task, what it really ties back to value and risk. So just keep
*  in mind all these trade-offs, you will face them, you will have to balance them. It is more art than
*  science and it's highly contextual. These are the kinds of things, again, that an AI advisor
*  and a client should absolutely be discussing early in the process because getting clarity on this is
*  going to help everybody understand how this is likely to play out, what the downsides might be,
*  and when they do pop up, you're expecting them, you're ready for them. I also just wanted to give
*  one note on no-code platforms. I think today, no-code platforms are really very often the way to go.
*  If you are accustomed to working with software engineers, they are typically accustomed to doing
*  original program development, app development, and that has its place, of course, especially if
*  you're building an actual application that you're going to sell as an application. But if you are
*  building something internal to your business, I would strongly recommend taking a hard look
*  at no-code before you start coding up custom applications. There are tons of them out there.
*  We've had good luck with many in my work. N8n is even open source and free to use if you want to
*  host it yourself. I don't necessarily recommend doing that because it could be a hassle. That
*  option is out there. And you'll notice that they even use a lot of the same language that we use.
*  I borrow these terms from no-code, but you notice obviously inputs are the same, outputs are the
*  same. They use logic in no-code oftentimes for exactly how the task is going to be performed.
*  But that logic can also be supplemented by intelligence now. And you can have right within
*  these workflows calls to foundation model APIs. And I think this is really becoming the norm.
*  So we're going to have an episode actually on the cognitive revolution with one of the founders,
*  I believe the current CEO of Zapier before too long and dig into that in a lot more detail.
*  It's a nice thing to say for now. If you can build no-code, I recommend building no-code.
*  It's faster, it's cheaper, it's a little less flexible, but it's a lot easier to maintain.
*  It's a lot easier to look at. It's a lot easier to have somebody who's not a software developer
*  go in there and make a tweak. Most of the time, I think people are much happier if they get these
*  things working in no-code versus just having an application developer go off and build something
*  from scratch. Next few things I'm just going to breeze through. These are leave behinds.
*  You can get this presentation. I'll publish the whole thing so you can go check it out. But
*  this is a recap. If you are a business owner and you are hiring someone to help you with AI
*  automation, I tend to see these break down into two different roles. Certainly the same person
*  can play both roles, but I see a lot of AI advisor and then I see a lot of AI engineer.
*  The AI advisor is more on that first half of the process, identifying what good targets are within
*  your business for AI automation, working through that process of deeply understanding the work,
*  not necessarily continuing through to the implementation. The AI engineer is typically
*  much more focused on implementation. But again, you can find one person that can play both of
*  these roles, but it might be helpful to understand that these different roles can exist because there
*  is a different skill set for going through the social part of working with business leaders,
*  working with team members to figure out what to do and how it's best done and what good looks like
*  and sourcing those examples. That's a human to human process. And then implementing is a human
*  with technology or human with AI process and does involve a notably different skill set.
*  But I would run down the skills in any sort of interviewing or hiring process
*  and just make sure that people are checking these boxes. A good AI engineer will at least be familiar
*  and have some minimal experience doing all of these different things, I would say. It doesn't
*  mean that they necessarily have to be an expert in every single one. Nobody can keep up with the full
*  literature. Even just prompt engineering techniques, there's so many popping up all the time.
*  It's not like a red flag if somebody hasn't heard about one specific prompt engineering technique
*  that just popped up. There are a ton of techniques in retrieval, augmented generation. There's
*  multiple different ways to do fine tuning, especially if you're running it off of the major
*  platforms. So I would not be too concerned if somebody doesn't check every single box,
*  but basically I think you want to be working with somebody who can check all the boxes on both sides
*  of or on either side of this ledger as appropriate. Similarly, habits of mind for an AI advisor,
*  the things that I look for, the things that I try to do when I'm helping somebody through an AI
*  automation project versus the things that I see leading to frustration mostly boils down to
*  having humility about understanding what the work is and what makes it hard and really just focusing
*  in on understanding that as deeply as possible and making sure that we can get that core hard
*  part to work and setting reasonable expectations about what it's going to take to get there,
*  including probably multiple rounds of review of outputs and ultimately iteration on the technology.
*  Opposite vibe is to come in and say, oh, this is going to be easy. It's going to be no problem
*  to start jumping to building Zapier Zaps before figuring out if that core part can be made to
*  work and how promising that it'll all happen quickly or will knock this out. The first thing
*  is going to work. That is typically not true. That reminds me of my dad's old saying that I grew up
*  on, which is the other guy's job is always easier. So often the AI advisor feels like they're really
*  smart and this person that's doing customer service tickets, that can't be that hard.
*  But remember, there is typically a lot more to it. And a big part of what this person needs to do
*  is work with the team to uncover that information because without doing that,
*  you can't teach it to the AI and you're not going to get good results. So humility,
*  focus on what's hard and empathy for what makes this job difficult and a reasonableness on how
*  this whole process is going to go. Seeing that is a green flag in an AI advisor. Seeing the opposite
*  for me would be a big red flag. A couple last notes on, first of all, enterprise. Of course,
*  everything is harder in the enterprise. If you work for a big company, you can't necessarily
*  take for granted that there's going to be access to all the data. You're going to have all sorts
*  of red tape around privacy and data security. You may have contracts with customers that may
*  be difficult to meet if you're bringing in an AI system that could be sort of unreliable, even just
*  in terms of outages. If you build something on the open AI platform and the open AI platform goes down
*  for an hour and you have a one hour service level agreement, then you have a problem. So those
*  complications are definitely very real. I don't deal with them too much, but I think the biggest
*  thing that they imply is that task selection is even more important. It's even more important
*  because there's just so much extra friction, so much extra work has to go into getting things
*  set up to work and people hope that the solutions are going to last. Of course, they're not going
*  to last that long, but the most important thing I think is to just even spend more time and energy
*  choosing the right targets and really deeply understanding the work. The de-risking becomes
*  even more important when there's all this additional baggage that you have to deal with.
*  The cost of choosing the wrong task and going down the wrong path is just much higher when there's
*  more friction on that path. So if you're at an enterprise, more reason to invest in somebody who
*  really can guide you and make good decisions at these early phases of the process. Finally,
*  I initially called this future proofing, but really it's just future planning. The big thing here is
*  just to keep in mind that this technology is evolving faster than almost any other technology
*  ever has. The electrification of the United States took 60 years, like three generations, depending
*  on how you count. And this is unfolding over a period of far fewer years. So the solutions
*  that you build are not necessarily going to last that long. And the good news is that the trends
*  are all in your favor. Everything is getting better, faster and cheaper. That is allowing you to
*  build things more simply. The options for fine tuning and really optimizing are improving all
*  the time. The infrastructure is getting better, is getting more robust, is getting higher and
*  higher level. The no-code solutions, as I mentioned, are really getting quite strong.
*  And all this kind of adds up to, don't overthink it. Create something that works now, get those
*  easy wins. If it can match human performance and it can do it faster and cheaper, that's awesome.
*  Cash those checks and cash them as soon as possible. And don't over invest. Don't let
*  perfectly the enemy of good, to use an obvious cliche. Don't obsess about that last tiny little
*  increment of performance, especially if you're able to demonstrate that you're at human level.
*  Better to go around doing this multiple times in different areas of your business and picking up
*  multiple different wins, all of which can get upgrades when the next model comes out or the
*  next paradigm, than to obsess on one little thing. Know that none of this stuff is going to last
*  that long of a time. At Waymark, we have been through multiple iterations, many iterations
*  of our AI video creation process. And definitely the trend is that our architecture is getting
*  simpler. The effort that we have to put into each upgrade is getting smaller. The models are getting
*  better, faster and cheaper. The overall customer experience is getting better. And allowing that
*  to come to you is a big part of how to plan effectively for the future. I would create,
*  rather than going obsessive on one problem and trying to maximize performance on that problem
*  today, I would recommend going five or 10 problems, getting them all too good enough that
*  they actually work for you. And then letting the world come to you and enjoying the benefits of
*  those rolling upgrades with bigger surface area for them to actually serve you. So that's it.
*  That's AI automation. The key points, again, if I just to recap the entire thing briefly,
*  you want to use artificial intelligence where intelligence is genuinely required.
*  That means if something can be done in a fully deterministic, fully explicit code based way,
*  then that way probably is better because it will be faster, cheaper and more reliable than an AI
*  powered solution. You want to use the AI where intelligence is genuinely required because there's
*  just no way to code up a solution that works. You want to identify targets that fit that
*  description. You want to identify targets that have the right profile in terms of
*  having enough volume to be valuable, but not being too risky, being something that is no fun to do,
*  being something that AI can do. And then you really want to understand that work deeply
*  to make sure that you can teach the AI not just what an input and an output look like,
*  the pattern of thought that goes into making that transformation, the reasoning that the person who
*  does that job today is actually doing. Typically it's implicit. So a lot of work is converting
*  implicit context or implicit reasoning to explicit, but taking your time to do that well, get those
*  gold standard examples. And then you can embark on this process of AI optimization with prompts,
*  with information retrieval, and ultimately if necessary with fine tuning. If you follow that
*  path and if you make good decisions upfront, I would say a large majority of routine tasks
*  can ultimately be automated in most businesses today. It may take a significant amount of work
*  in some cases. It definitely took Google a lot of work to get to the point where their medical chat
*  bot was beating human doctors at diagnosis. I'm sure it took Klarna a lot of work to get to the
*  point where their AI chat bot could handle millions of conversations a month and save the company
*  tens of millions of dollars. But the payoff can be really quite great. So be prepared to put some
*  elbow grease in, but also know that the payoff for this can be some of the highest ROI of any activity
*  that you can engage in your business. The savings can be incredible. The scalability can be
*  incredible. You don't ever want to get totally disconnected from your data, but the degree to
*  which this can free you up to do higher and better things can really be incredible. So this was a
*  leftover slide from the presentation where I gave it in person. This is just a link to the Cognitive
*  Revolution website where you can get all of our stuff. And this is the link specifically to the
*  slides, which are open and you're welcome to download and share. Alrighty, this has been AI
*  Automation 101. Thank you all for being part of the Cognitive Revolution. It is both energizing
*  and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the
*  social media platform of your choice.
