---
Date Generated: September 27, 2024
Transcription Model: whisper medium 20231117
Length: 3305s
Video Keywords: []
Video Views: 432
Video Rating: None
Video Description: Join Nathan for an insightful episode of The Cognitive Revolution with Wade Foster, co-founder and CEO of Zapier. Discover how this no-code pioneer is evolving into an AI-powered platform for the future of work. Learn about Zapier's ambitious vision, their integration of AI throughout their product, and how they're adapting as a company. From AI-driven lead qualification to innovative customer use cases, explore the cutting edge of automation at scale. Wade shares valuable insights on effective AI prompting, internal AI adoption strategies, and his perspective on recent AI advancements. Don't miss this fascinating look into the future of AI-powered automation with one of the industry's leading innovators.

Check out the ZapConnect 2024 event: https://zapier.com/zapconnect

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:
WorkOS: Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-Turpentine-Network

Weights & Biases Weave: Weights & Biases Weave is a lightweight AI developer toolkit designed to simplify your LLM app development. With Weave, you can trace and debug input, metadata and output with just 2 lines of code. Make real progress on your LLM development and visit the following link to get started with Weave today: https://wandb.me/cr

80,000 Hours: 80,000 Hours offers free one-on-one career advising for Cognitive Revolution listeners aiming to tackle global challenges, especially in AI. They connect high-potential individuals with experts, opportunities, and personalized career plans to maximize positive impact. Apply for a free call at https://80000hours.org/cognitiverevolution to accelerate your career and contribute to solving pressing AI-related issues.

Omneky: Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

RECOMMENDED PODCAST:
This Won't Last - Eavesdrop on Keith Rabois, Kevin Ryan, Logan Bartlett, and Zach Weinberg's monthly backchannel ft their hottest takes on the future of tech, business, and venture capital.
Spotify: https://open.spotify.com/show/2HwSNeVLL1MXy0RjFPyOSz

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsors: WorkOS
(00:01:22) About the Episode
(00:03:41) Introduction and Zapier's Competitive Edge
(00:07:20) AI as Knowledge Worker Companion
(00:10:27) Impressive AI Use Cases
(00:16:25) Sponsors: Weights & Biases Weave | 80,000 Hours
(00:19:05) AI Implementation Challenges
(00:19:13) LLM Performance and Prompting
(00:22:42) AI Adoption within Zapier
(00:31:00) Sponsors: Omneky
(00:31:23) AI-Assisted Workflow Creation
(00:36:07) AI Culture and Adoption at Zapier
(00:43:03) AI Impact on Zapier's Productivity
(00:48:06) Zapier's AI Integration Strategy
(00:54:43) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Zapier's AI Revolution From No-Code Pioneer to LLM Knowledge Worker
**Cognitive Revolution:** [September 26, 2024](https://www.youtube.com/watch?v=6JbKvVUjBy8)
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
*  Hello, and welcome back to the Cognitive Revolution. Today, my guest is Wade Foster,
*  co-founder and CEO of Zapier, the automation platform that's been a no-code pioneer since
*  its founding in 2011. Zapier has long been known as an easy way to connect apps and automate
*  workflows. But as Wade explains, they're now pursuing a much bigger vision to be, as Y Combinator
*  President Gary Tan recently put it, the AI-powered knowledge worker of the future. In this conversation,
*  Wade shares insights into how Zapier is embracing AI in their product and also adapting to AI as a
*  company. More than 400,000 customers have already delegated more than 100 million tasks to AI through
*  Zapier. And Wade highlights some of the most common and also some of the most original use cases,
*  from AI-powered lead qualification and SDR-style outreach to a voice memo to invoice system that
*  one customer built for his wife's small landscaping business. We also explore how Zapier, like so many
*  other companies right now, is evolving its own product strategy, moving from a DIY platform to
*  a done-for-you-by-AI platform with AI functionality woven throughout. While the AI functions that
*  design Zaps are still a work in progress, it's clear that Zapier hopes to lower the barriers to
*  entry by allowing anyone to design new workflows with a natural language interface. Along the way,
*  we also touch on the challenges of decomposing tasks that are intuitive for humans into the
*  sort of discrete steps that AI can handle effectively. Zapier's strategy for encouraging AI
*  adoption internally, including their very founder mode decision to stop work across the entire
*  company for a week-long AI hackathon after GPT-4 was released last year, Wade's tips for effective
*  prompting and pushing the boundaries of what's possible with current models, and his perspective
*  on the state of AI progress since GPT-4 and how that relates to his co-founder and previous guest
*  Mike Kanuk's perspective on progress toward AGI more generally. As always, if you're finding
*  value in the show, we'd appreciate it if you'd take a moment to share it with friends or write
*  us a review on Apple Podcasts or Spotify. And don't forget, you can always share your feedback
*  or suggestions via our website, cognitiverevolution.ai, or by DMing me on your favorite social network.
*  Now, I hope you enjoy this inside look at AI-powered automation at scale with Wade Foster,
*  CEO of Zapier. Wade Foster, CEO of Zapier. Welcome to the Cognitive Revolution.
*  Yeah. Thanks for having me, Nathan. I'm excited for this. You guys obviously have built a very
*  well-known company in the no-code space, one of the early category definers. And I wanted to start
*  off with just big picture stuff about the company, and then definitely we'll have a chance to go deep
*  on some of the AI products and features and cultural adaptations that I'm sure that you're
*  dealing with over the last couple of years. For starters, obviously the competition has grown up
*  around you as they've seen your success. How would you describe Zapier today in an increasingly
*  crowded market? What's the key competitive advantage? Why do people choose you? Why is
*  Zapier still leading in the space? You're right. There's a lot more options forever,
*  which I think is good for everybody to have that. But I think the thing that Zapier still does
*  better than everyone else is it's just so easy to get started with. It's not hard to come in and go,
*  you know what? I want to make a new payment from Stripe post into Slack. I want to take this
*  attachment I get in from Gmail and push this into Dropbox and just start with these real basic
*  integrations and just start to get your wheels turning. And then I think the thing that we have
*  increasingly been doing at Zapier is saying, hey, it's not just integrations. It's how do you really
*  build a full-blown automation platform out of this stuff? And so more and more folks get started with
*  Zapier on these easy things, but then find that the depth of the platform just keeps getting
*  bigger and bigger. And so they end up just being able to do more and more with Zapier.
*  And it's not necessary to go look for other things to solve an increasing amount of problems
*  at the end of the day. And so I think that easy to get started and just more depth for use just
*  keeps people in and around the ecosystem. When you talk about depth, is that number of other
*  things that you integrate with or how do you measure depth? Yeah, we've launched things like
*  tables and interfaces in the last couple of years. And so now it's not just simply an integration
*  you can do, but you can actually build on full-on applications. We had a customer earlier this year
*  that I met who had a wife that started a gardening business. She always wanted to start a gardening
*  business. And it turns out she liked the gardening part more than the business part and would never
*  send out invoices to customers, just wouldn't do it. And so husband was lovingly like, hey,
*  sweetie, I'm glad you're having fun with this, but it would be great if maybe we could get paid.
*  And he started thinking like, how could I make this easier for her to get paid? And turns his
*  after and says, I wonder if I can do something that makes it a lot easier to build these invoices.
*  Turns out he could. And he made what he calls voice to invoice. And what it is made a little
*  app on his phone and it's powered by JotForm, which has a field where you can just press record.
*  That's all the form does. You just press record and you just talk into it. And so when you talk
*  into it, he says, Hey, you know, met with this client today, Sally, we agreed on a budget of
*  150 bucks for tulips and $200 for daisies or whatever. And that then goes to Zapier,
*  sends it to the whisper API for transcription. Then that gets sent to a chat. GBT has a couple
*  of prompts, then extract out the actual terms of the invoice. And then that gets into a Google
*  spreadsheet that starts to enumerate, okay, a hundred bucks for this item, 200 bucks for that
*  item. And then eventually gets sent to quick voice to generate the invoice and gets in.
*  And now you can build these full on applications. 10 years ago, that would have been,
*  you know, you could raise a million bucks on an idea like that. Nowadays,
*  he's able to build that on Zapier in 30 minutes, an hour. That to me is what's increasingly awesome
*  about the combination of no code and AI is the types of experiences that just savvy people can
*  build, not necessarily engineers, just people who are using their brain a little bit can build
*  pretty impressive stuff. I think that's the thing that just gets me excited right now.
*  Yeah. One of the things that gets me excited is when I saw Gary Tan tweet about Zapier that
*  Zapier could be the AI knowledge worker of the future. And this is sort of one early example
*  of this in the wild. Is that how you think about the kind of big picture potential for the company
*  today? Do you want it to be something that feels like a knowledge worker companion, or is that
*  too out there for what you would define as your goal? Well, we've had this line on our about page
*  for a long time, which is we're just some humans who think computers should do more work. And I
*  think where that comes from is that certainly us as founders, but like the people we hang out,
*  the folks who are around, it was not uncommon for us to have ideas of, I'd like to build this,
*  or I'd like an app that does this thing. And to realize pretty quickly, it's harder than we
*  thought it would be. There's more hassle, the technology is not quite there. And the distance
*  it takes to go from idea to execution is pretty big still. And at the end of the day, what we're
*  just trying to do with Zapier is shrink that distance, make it so much quicker for a person
*  to just go from idea to living, breathing thing at the end of the day. So I do get pretty excited
*  about the potential of Zapier to be this just sidekick assistant. Insert whatever word, but
*  it's going to be this tool that just sits by you to help you solve a whole host of problems that
*  you might have. Generally at work is where we're spending most of our time thinking about this
*  stuff. Yeah, it's really interesting how over the last year, we've all been on quite a journey of
*  figuring out what more work can computers do broadly than they used to be able to do. And
*  we know that there's a pretty big answer to that, but the exact shape of it and the nooks and crannies
*  are often quite surprising. Obviously, you can do a lot more Zapier now than you could in a pre,
*  let's say GPT-4 world. Do you have kind of stats or ways of describing how much of the individual
*  task flows that are flowing through Zapier involve some AI element today? I guess you could just
*  measure that in terms of how often are people calling open AI or thought or whatever.
*  We're at about 400,000 customers that have delegated now over a hundred million tasks to AI.
*  And it's the fastest growing category on Zapier is AI related workflows. I'm very bullish on
*  the potential of this as a thing that's going to continue to solve problems for a lot of folks.
*  Yeah, that's fascinating. So 400,000 customers and a hundred million individual tasks. So that's a
*  hundred million trigger logic and output that had some language model call. Some AI was involved
*  somewhere. Yeah. Yeah. Okay. Interesting. So let's talk about the shape of that. I think this is one
*  of the hardest things for people who are new and not obsessed with it as I am. And I sometimes
*  think it took me thousands of hours to map out for myself and develop my intuition.
*  Maybe you can give us some shortcuts and you have the benefit of obviously all these customers.
*  Yeah. I guess for starters, what are some of the most impressive, hardest, highest stakes
*  successes that you've seen where people are able to get AI to do something that really moves the
*  needle for them? Yeah. Well, I mentioned the voice to invoice problem there. I think another example
*  that comes to mind is Sikyi Chen, who's the CEO at Runway. Runway sells this, you can almost think
*  of it like Notion needs like financial planning. It makes it really easy for people who aren't in
*  finance, like understand like the finances of the business and figure out how it works. Sikyi,
*  the Runway team, they are great at building products and as great as they are at that,
*  they might be even better at marketing products. And so when they announced like their new site,
*  it kind of went viral and they pretty instantly had dozens of people signing up for access to
*  the product in a minute. And it's a pretty small team and the engineers are all 100% focused on
*  building the actual product. And sales team is like two people, there's one person on success.
*  There's just not that many people here and they're getting dozens of folks coming in every single
*  minute. So, you know, what do they do? Sikyi says, Hey, I wonder if I can build something with
*  Dappier Chat GPT to help us better qualify these folks coming in and send out prospects for them.
*  And one of the things he builds is a quick zap that takes the lead that hits their database,
*  pops it over to Zapier. They then iterate through the latest batch that comes through.
*  And in doing that, you hit the chat GPT and filters out anything that's a free email domain.
*  And so instead of having to enumerate all the email domains, they can just tell chat GPT
*  anything that looks like free, just figure it out. So they can kind of vaguely tell it.
*  And then chat GPT figures out the rest. Then they have the leftover ones hit clear bit and say,
*  Hey, I want to go enrich all these because these feel like they could be actual legitimate prospects.
*  I think they then come back and hit chat GPT one more time and say, for the qualified folks,
*  we want you to write an email draft. And they have a very specific prompt they use in chat GPT that
*  like, it's like, Hey, make it witty, but not cringe and some guidance for like how they want
*  to send this. And then they have that land in Gmail as a draft. And so in the morning,
*  those sales reps can pop into their Gmail drafts and go like, send, send, send, send, send, send,
*  quickly review them. Cause you want to just double check it a little bit, but they can move
*  through these things in a way that if they were trying to do all that stuff manually,
*  you couldn't have done it with the headcount they have. And so when you ask Siki, like the impact of
*  that is I would have had to hire another 10, 20 people to get that job done. And instead this was
*  something he built in 30 minutes on Dabby or chat GPT, few other tools, et cetera. So I think you
*  see stories like that are pretty common. Honestly, the biggest hurdle I think folks have is
*  actually coming up with the ideas for them. The creativity is I think the hardest part. And
*  I certainly see this pretty, right. You probably come across this too. You like go on Twitter,
*  X, whatever. And you'll see folks that are like in the scene, the AI scene, and they'll be like,
*  what do you actually use AI for? What actually are you using it for? And I think we're in that
*  period where some of the novelty of the demos have worn off and folks are still sometimes searching
*  for, yeah, but where's the sticky use case? Where's the impact? Where's the repeatable stuff? And so
*  it's really useful to get Danny and Siki and all these other use cases out there for folks
*  because they can start to go, okay, I don't have that exact problem, but I have a version of that.
*  And now I can figure out maybe how do I go replicate it for myself?
*  To go a little bit deeper in the advice that you would give people, or what are the takeaways
*  from that? I think people, the creativity or having the ideas is definitely one limiting factor. I
*  think another is not having a good sense for what the AI is going to do, what it's not going to do.
*  Well, recently I've heard a number of people say that you only want to use the AI where it's
*  strictly required. Anything that can be done in a traditional code way should because it'll be
*  better, faster, cheaper. Then there's some things that are kind of in between where it's like
*  classification or like deciding on like a fork in the road. How sort of detailed do you recommend
*  people or do you find people need to be in terms of exactly how prescriptive they're going to be?
*  Another way to say that is like, how much do the AIs actually have any autonomy in deciding what to
*  do versus being told exactly like, this is your input, this is your task, and we want the output
*  in this format? I think at the stage we're at right now, you definitely have to be more prescriptive.
*  There is a very real last mile problem based on the state of the art that we have today.
*  And so I do think I would subscribe to the advice you gave there, which is if you have a job to
*  be done that can be done in a deterministic way with code, or you can use a no-code tool,
*  but at the end of the day, it's all code under the hood. You're probably going to want to have it
*  run that way because it's going to be more reliable. It's going to be cheaper. It's going to be faster.
*  You're going to have all those things that you get there. And then there are a handful of like things
*  that an AI or LLMs are quite good at, certain tasks that you actually can't do it the other way,
*  or maybe you could, but it's exceptionally difficult. And that is things like how do you extract
*  information from unstructured text? How do you categorization you mentioned? So if you've got
*  to go categorize a whole bunch of stuff, it's going to be better, faster, cheaper than a human.
*  If you want it to generate text or generate something novel, it's going to be better at those
*  types of things. So there's a whole host of use cases that we actually didn't have a way to do
*  those free LLMs, but you can inject an LLM in the middle of a deterministic workflow and now have a
*  whole new type of thing that you can build. And so today that is, I think, where we're seeing the
*  most success. And y'all be honest, we had to figure that out too. We launched a product
*  central that was inference everywhere. It was trying to use AI to delegate a whole bunch of tasks. And
*  it is having some success, but the place where a lot of that 400,000 users and 100 million tasks,
*  that's happening through our traditional workflow engine. And I think it's because in that
*  traditional workflow engine, you can pair, mix and match deterministic steps with an AI step. And you
*  can basically delegate exactly what you want to the spot that you need it. And that improves the
*  overall reliability of the end-to-end task at the end of the day. Hey, we'll continue our interview
*  in a moment after a word from our sponsors. Today's episode is brought to you in part by
*  Weave. As a developer, the journey from concept to production-ready large language model apps
*  is fraught with challenges. Dealing with unpredictable large language model outputs,
*  correctly handling PII and ballooning API costs can all be blockers to shipping your next AI-powered
*  feature. Weave is a lightweight AI developer toolkit designed to simplify your large language
*  model app development. With Weave, you can trace and debug input, metadata and output with just
*  two lines of code. Weave helps you run rigorous evaluations and securely manage all of your
*  datasets and system configurations. So you can focus on what matters most, iterating and improving
*  on your large language model powered applications. Plus, Weave integrates seamlessly with your
*  favorite APIs and libraries, including OpenAI, Anthropic, Mistral, Cohere, Langchain, Llama Index
*  and more. So make real progress on your large language model development. Visit wmb.me.cr
*  to get started with Weave today. That's wmb.me.cr. And thanks to Weights and Biases for sponsoring
*  this episode. I am really excited that our new sponsor, 80,000 Hours, is now offering free
*  one-on-one career advising sessions to cognitive revolution listeners. 80,000 Hours aims to be the
*  best source of advice for people who want to do the most good that they possibly can with their
*  careers. We typically work for about 40 years in our lifetime and we work about 2,000 hours per year.
*  That is the single biggest opportunity that most of us have to make a positive contribution and
*  it's worth being strategic about it. That's where 80,000 Hours can help. I actually used their career
*  advising service myself. Two years ago, I had just finished the GPT-4 Red Teaming project and I wanted
*  to do anything I could to nudge the AI future in a positive direction. But what could or should I do?
*  That was not clear. After my call with 80,000 Hours, I got a number of connections to outstanding
*  individuals in the space and over the course of the follow-on conversations, I developed confidence
*  that this podcast was one of the projects that I should pursue. Today, I'm thrilled to have built an
*  audience of thoughtful, high-potential people that 80,000 Hours wants to help. To request a free
*  one-on-one career advising session, follow the link in the show notes. It's 80,000hours.org
*  slash cognitive revolution. That's 80,000hours.org slash cognitive revolution. Sign up for a free
*  one-on-one career advising session. Figure out how you can make a positive impact on the AI future
*  and I think you'll be glad that you did. How often are you seeing your users need to really push
*  for LLM performance to get it to where they need it? Like for Siki, for example, is he able to do
*  this on just a good prompt? Does he need like few shot examples or does he have to go as far as
*  fine-tuning a model to do certain key tasks? Yeah, most of our folks are just doing it with
*  basic prompting. You probably want to spend a little bit of time on your prompting, but it's
*  not like you're having to spend hours crafting the perfect prompt at the end of the day. You can
*  usually prompt it, maybe add a few examples if you feel like it, but you don't even have to do that
*  in a lot of cases. That's where I think folks are seeing a lot of the success today. No one's
*  having to go train their own models or anything like that for the use cases we're seeing on Zap
*  here. Are there use cases that you've seen people kind of have many people want to do and try to do
*  and just for whatever reason not be able to achieve any sort of no-go or there be a dragon
*  sort of zones you would describe? I think we like to communicate much more like colloquially
*  and there's a delta between that and how computers work today. There's a real skill even still in
*  describing stuff to computers and so that's like what we just touched on with prompts. The best
*  prompts are pretty specific and so there's a real skill that comes with authoring prompts. I think
*  most folks they get tripped up because they haven't actually really worked on that skill set at the
*  end of the day and so their prompts end up kind of vague or especially vague that it's really hard
*  for the LLM to figure out what it's going to do, but if you actually step back and think about it
*  it's probably hard for a human to figure out what you want to do too if you're being that vague.
*  I think the real magic is going to come when these models can get to a point where they can handle
*  increasingly vague statements and where they're figuring out how to take a just like really messy
*  human statement and then actually transcribe that into a better prompt under the hood or at least
*  prompt the human back to say, hey did you want more like A or more like B? You know that's what
*  you would do if you're working with an assistant. You're like hey can you go get me lunch or whatever
*  and they'd be like sure do you want this or that and it's actually neither. Could you do that?
*  A great assistant kind of knows how to interact with you in that way and I think that's really
*  what we're waiting for these models is to get to where they can kind of learn from you a little
*  bit and extract your preferences and have a little bit more memory and context and use that to keep
*  getting better and better over time. Yeah Tyler Cowen says context is that which is scarce. I'm
*  working on a project right now to try to get, I assume it's going to ultimately be a fine-tuned
*  model. I'm not sure exactly which one will be best but try to get some model to write as me
*  and try to do that in a way that hopefully I will find compelling. So my strategy for this is to
*  combine a huge amount of context and I'm currently in the process of trying to extract my data out
*  of all these different places where it is locked up, Gmail, Twitter and whatever and then try to
*  summarize that into something where it's hopefully still going to be pretty long, pretty thorough,
*  pretty fact rich so that the AI has enough to go on and then also train it on my actual output
*  so that it hopefully can pick up my style and patterns and whatnot and then that's when I'm
*  going to start putting things through Zaps and being like, okay can you respond to this email
*  as me knowing that you have 50,000 words of context on me so that you don't have to
*  hallucinate things and I don't 100% yet know if that's going to work but some of the stuff
*  we've seen just in the last couple weeks with GPT-4.0 fine tuning on the software engineering
*  benchmark definitely suggests that there is a lot of juice still there. Yeah, you might be able to
*  do that without fine tuning. We did a similar version, my assistant and I, where we took a bunch
*  of my own emails, post side written internally, Slack messages, all that sort of stuff and fed it
*  into one of these things and said, hey the prompt was effectively like describe the writing style
*  here and then we just did a couple iterations of that to where now we actually have a pretty
*  consolidated prompt, it's not that long, that basically describes my own personal writing style
*  and we used that, we actually ran an internal test where we had a bunch of questions that were
*  submitted by employees and I went through myself and answered those questions then we had an AI
*  version of me answer those questions and then we posed back to the company which answer is Wade,
*  which answer is AI Wade and it wasn't that easy for the company to tell. I think folks still picked
*  up on me a little bit more often but it was still pretty clearly like that this prompt effectively
*  was doing a pretty darn good job of that. The CEO Turing test is maybe the next default.
*  It's pretty fascinating though to think about because how many folks would love to actually
*  get feedback from the CEO but are maybe a little scared for whatever reason and just being able
*  to talk to somebody it's like you can get the advice of Wade but maybe without the judgment
*  Wade, that might be a perk at the end of the day. That's funny. So just to make sure I have this
*  setup correct, it was purely using a prompt. You basically just go to ChatGPT or Claude or any of
*  these things and feed it a bunch of documents, data, etc. and then you just ask it, can you
*  generate a prompt for me that would cause you to write in the style of all this stuff? That's
*  effectively what you're trying to get it to do and then you might have to loop through it a handful
*  of times, ask it a couple different ways and then you'll get like a nice prompt that you can say and
*  you can make it your system prompt then if you want in ChatGPT and it works pretty good. I get
*  that process but do I understand correctly that you didn't include any actual samples?
*  No, we gave a bunch of samples. Well, no, no. So let me back up. We gave it a bunch of examples.
*  That generated the prompt but then that prompt itself stands alone.
*  No other examples. I've tried that a bit and I would say my current state of the art pre-fine
*  tuning for Write as Me is give it just a bunch of samples and ask it to write as me and I find
*  Claude does the best at that for me and it works pretty well also. One of the challenges that I've
*  had is I get a lot of hallucinations if it is just kind of working with all these samples and
*  it's like from the LLM's perspective, I feel like I appear to be making up facts, right? It has a
*  hard time separating fact from fiction. What I'm writing is like plausible enough and then it will
*  write plausible enough stuff but it'll be wrong. Do you think that there is a way in which perhaps
*  just the generally like well-known status of Zapier and you is trained into the model in such
*  a way where you're benefiting from base training perhaps? Because otherwise like it would need
*  context presumably. I don't know what questions you're answering here but like, you know, what's
*  the deal with the team retreat, right? It's not going to know how to answer that. So how do you
*  make sure that it is like grounded enough to be effective? Yeah, I do think that is where it falls
*  down today. If you're asking about something very specific to Zapier that would not be in the
*  training, like some internal knowledge, that's not going to be in the training data anywhere.
*  It's not going to be in the samples from at least the standalone prompt and so that's just not going
*  to do a good job at that kind of answers. It's going to do what all these AI models is going to
*  hallucinate. It's going to give you a very confident sounding answer that looks correct
*  and is just wildly not. Yeah, so going back to what people do on the platform and the sort of
*  the limitations you said, it's easy to get started, connect one thing to another thing.
*  It's presumably a lot harder for most people to think about how they take something that they
*  do intuitively and break it down into, I think, Siki's thing was 16 steps. We had him on the show
*  not too long ago. Oh, did he share the same thing? We didn't get into the SDR thing in depth. We
*  talked more about like how they're using AI in the runway product. He did mention it very briefly,
*  but anyway, that sort of decomposition and layering of structure onto something that
*  people do in a kind of muscle memory sort of way, I assume also must be like a real challenge for
*  a lot of people and I wonder how do you help them with that and to what degree can AI
*  help them with that? There is the product experience where you go in. You can either
*  just start with a blank canvas and start building steps one after the other or you can say,
*  here's what I want to build and have AI generate a draft for you. Are people really attracted to
*  that? How well is that experience working for folks today? Yeah, people are definitely attracted
*  to that and using it today. I think it is still fairly immature to be honest, but it is working.
*  Pretty much daily we'll get notes of folks that are like, holy cow, that actually worked.
*  I think the magic of it is as easy as we've made Zapier, if you're going to try and set something
*  up without an AI, there's a lot of configuration that you have to do. You have to think through
*  triggers and actions and connect apps and map fields and just a lot of buttons you got to click.
*  Now it's easy to click the buttons, but there's a lot of buttons, a lot of knobs to turn.
*  And so the idea of being able to describe in natural language what you want or to have a
*  little bit of a thought partner to say, hey, can I do something like this? How might I do this?
*  And it's a feedback ideas. It acts kind of like a better rubber duck for you on these things.
*  I do think there's two vectors of improvement that we're working on. One is the better coach,
*  better guide for these things. So you're still in control as the human, but you can ask it
*  questions and it can say, why don't you try this or why don't you go this way? Or would this,
*  might this work for you? And it's helping you come with ideas. It's helping you get your creative
*  juices flowing. So that's vector one. I think the second factor is then how do you actually
*  take over some or all of the building for you? Because that's another big hurdle where you can
*  say, hey, okay, you said you wanted this. I've already done it. Do you want me to go ahead and
*  insert that in for you? And that's a different sort of like lane of improvement to go on. I think
*  both are pretty necessary to help folks reach the fullest potential. I think if you're just doing
*  building, you're only going to be successful with folks that sort of show up with ideas.
*  And if you're just doing the ideas only, the building still is sophisticated enough that
*  folks get tripped up along the way. And so you have to improve on both dimensions to really reach its
*  fullest potential. Have you used gamma? Gamma.app? I haven't yet. No. I definitely recommend them.
*  I think gamma, which is another former guest, is great at providing a sort of guided experience
*  at the beginning. What do you want to say? Give you an outline. Okay. You can iterate on that a
*  little bit. It's a slide maker. So now we translate this thing to a series of slides. And then when
*  you get into the slide level, also, there's like the AIs also kind of at that level. Like,
*  do you want me to revise this one slide? And they also do a really nice job on accept or reject
*  changes. I think they've got a really tasteful UI on that front. So anyway, I recommend them.
*  Do you have others that you look to that you think are out in front right now in terms of their
*  maturity for AI guided experiences? I think what Claude is doing with artifacts is like pretty,
*  pretty impressive right now. Like that's, I think you're just going to see a lot more of that kind
*  of experience where you have AI on one side, builder motif on the other. And it would not
*  surprise me as the next generation of the application layer feels a lot like that,
*  where you almost have this idea of like disposable experiences where it's spin up a thing,
*  use it, and then that's it lasts for a moment in time. I think those experiences are just pretty
*  freaking incredible when they work. How often are you like on your phone looking for a mobile app to
*  do some utility thing? You're like, it would just be better if I could create it. And if the time it
*  took me to create it was, I don't know, what under 10 minutes under five minutes, I don't know, like
*  what's the timeframe of what you'd go like, this is actually better experience than going through
*  the app store and trying to figure out like what I would do. So that's the kind of thing I think
*  we're gunning for here. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omnike so
*  much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  Yeah, it's happening fast. I was just complaining earlier today that I don't have a good personal
*  search engine. Like I want to just search through all the stuff that I've previously seen effectively.
*  And that's still oddly difficult. I find somebody responded, maybe you should just build one. And I
*  was like, you know what, maybe I should. It does feel much more in reach. Yeah, there was the product.
*  I think they rebranded rewind. I was super excited for that, but they've pivoted away from
*  that vision and narrowed in a little bit more. I'm not sure exactly why, but
*  in my experience, I did have challenges with that thing, just like consuming a lot of resources on
*  my computer. It sort of would bog down the machine. That was a barrier. So you have a co-founder
*  who's out with a big prize who is saying that progress toward AGI has stalled. Cards on the
*  table. I don't quite share that perspective. I wonder how you would address that disagreement
*  from the standpoint of just what is happening within the Zapier platform by users. So if we
*  look back at GPT-4 18 months ago, first version, and then we fast forward to today, there's been
*  a lot of things that have launched, like longer context, windows, multimodality, fine tuning of
*  advanced models, just way cheaper for one thing. And from my perspective, it seems like those things
*  have unlocked a lot, but maybe for practical purposes, for most people, they haven't unlocked
*  so much. Have you seen the frontier of the sort of difficulty or the value of tasks move a lot over
*  the last 18 months? Or would you say it has been more like, of course, like it has diffused, I'm
*  sure like more users are doing stuff, but in terms of the most impressive examples, how much
*  more impressive are they than 18 months ago? They're hugely more impressive. Like the progress has
*  been unquestionably strong, I think. Mike points out, and I think sometimes gets misconveyed is,
*  he really focuses on that G in AGI. And the definition he would use of AGI, which is obviously,
*  depending on what you talk to, you're hearing a million different definitions, is its ability
*  to learn something new from scratch. It's like basically being able to top domains. And right
*  now, I think what he would say is what's happening in LLMs is that it's trained on a set of stuff,
*  and then it's effectively pattern matching on top of that. And I think there's some truth to that.
*  But the reality is bigger models, like cheaper, multimodal, the commercial value, the useful
*  utility of automation has grown immensely. And I think that's where Zapier is playing most right
*  now. It's like, how do we actually help people just build more useful automation inside their
*  workplace? And on that dimension, compared to where we were 18 months ago, it's like night and day
*  difference. Like working with unstructured data was nearly impossible. I remember we built an
*  email parser, it's been years ago, and that thing was like the bane of our existence. People wanted
*  that thing to do so much, but the current state of the art email parsing tech was just not good
*  enough. Now, you can just do a basic prompt, and it's better than any parsing engine that you would
*  use two, three years ago. So yeah, the progress is incredible here. Yeah, that's really interesting.
*  I was just thinking about email parsing project earlier. And yeah, especially HTML emails, like
*  for folks who don't know, it's the gnarliest thing in the entire world. Somehow we have ended up in
*  this state where it's like the worst vestiges of old technology have somehow been crowded into
*  HTML emails. And it is a real nightmare to try to code. One might say you might need to be AGI
*  complete to just deal with HTML emails. But I guess that's probably a little too permissive.
*  So what do you hope for next? Obviously, there's a lot of speculation around Strawberry, Q-Star,
*  whatever. Zapier strikes me as being in an interesting position where if I'm in the workflow
*  business as you are, and it's like, man, this is amazing because all these hard things that we just
*  used to not be able to program to do, now we can just drop a little AI into this otherwise structured
*  workflow, and now it works. Amazing. But a lot of people also have this vision that might not be too
*  far off where they're like, I just don't even want to think about that sort of structure. I just want
*  to hand the AI a project level thing and say, go do this, figure it out, come back and show me when
*  you're done. More like the classic intern who you just give something to and wait. How does that
*  play with Zapier, you think? Do you want something that can do mid-scale, longer time horizon tasks?
*  Do you want something that's just much more reliable in terms of very local things? Is there
*  a form of that sort of agent thing that becomes a competitive force vis-a-vis Zapier?
*  Yeah, I think what do I want? What do consumers want? We all want a world where we can increasingly
*  describe tasks to be done in simpler, vaguer language and have an assistant just go do those
*  things. That sounds like the dream, doesn't it? The question is then what type of product experience
*  do you need to deliver on that? And I still think under the hood, you're going to have some form of
*  workflow engine that's powering a lot of this stuff because you're going to have to route data
*  to different services. You're going to have it execute various tasks within that. It's going to
*  have to feed the output to some other service and you're going to have to deliver it back to the
*  user. I think you're also going to have different types of jobs to be done. There's some things that
*  you want super low latency and cost is going to be a real important concern. That's going to have
*  to work in one particular way. You have other areas where it's like accuracy is really, really,
*  really important and you're willing to spend a lot of money on it. So that experience is going
*  to look quite different too. I think you go into any business and it's full of workflows
*  that all have different shapes, sizes, contours, what have you. And so I think we're going to just
*  see an enormous different ways that these things can sort of be put together. I think the question
*  is, are we going to have one godlike AI that you can just interface with that just magically knows
*  behind the scenes, how to route and do all that sort of stuff? Maybe. I don't see a ton of evidence
*  that's what's coming next. And then of course, if we get there, like all of us who build this kind
*  of stuff or who knows what we're going to do at that point in time, you start to get the AGI
*  territory where it's hard to, your guess is as good as mine of what the world will look like then.
*  But in the meantime, I'm pretty bullish on how we at Zapier can take these smarter,
*  more flexible models and inject them into like your existing toolkits to help you solve bigger,
*  better problems for an easier to use interfaces. For your AI sort of builder experience, the sort
*  of what do you want to build? Okay, here's a somewhat vague description of the Zap that I
*  want to create. How far have you pushed that today? And how much farther do you think there
*  is to push it before you would be maxing out what current models can do and would only see benefit
*  from the next step up in reasoning capability or whatever? I think there's still quite a bit more
*  we can do with the existing models, but we're definitely starting to feel like the boundaries
*  of some of this stuff where it's like there's certain types of tasks that we can do pretty
*  predictably if they're simple enough and small enough. But when it breaks outside the bounds
*  of those things, it definitely feels like self-driving cars where it's like you can
*  get the demo sort of working, but that last mile stuff ends up being exceptionally difficult.
*  It's all the edge cases, the weird anomalies, the things like that where humans can spot those
*  things pretty easily, but the AI will just trip up on those things left and right. And that's where
*  I do think we're just waiting for the models to see, hey, are they going to have a step function
*  improvement and what it's capable of? And if so, great, that's going to unlock a whole new set of
*  tasks for ourselves. But even within the existing models, I still think there's more we can do to
*  make that experience just better across a whole number of workflows. My number one tip for people
*  generally is fine tune on chain of thought or reasoning traces they're sometimes called,
*  but basically demonstrate with not necessarily a huge number of examples exactly how you want to
*  approach the task, kind of all the stuff that happens in the internal monologue that typically
*  in work doesn't get captured, right? Because we just have often like a ticket definition and then
*  the result and the thought process that happened in between is usually not captured.
*  But getting some of that stuff down in explicit form and then fine tuning on that so that the
*  model is now imitating not just your outputs, but also the reasoning process to get there.
*  That's my number one thing usually for pushing product experiences like that.
*  What have you found to be the biggest step up in performance of all the things?
*  I think what you just described is pretty accurate. I think in some ways, it's almost
*  the opposite of what you want to do for Google search. In Google search, you're just so lazy,
*  it's the shortest little keyword or whatever snippet that you can get. When you're working
*  with these models, you want to describe it in its fullest version of itself. So that definitely
*  stands out for sure. More examples is good. I think narrowing the task is also really helpful
*  and then starting to chain those narrower sets of tasks. The more you try and do multiple sets of
*  things in one, you're going to see it trip over. So I think to the extent that you can say, hey,
*  I only need to extract X here. Then the next step is, okay, now I want you to do this next thing
*  here. That to me is the next thing that really has helped improve performance, especially within the
*  workflow engine is to really get hyper specific about that stuff, break it down to its most
*  granular bits that you can think of. Test decomposition definitely also really big.
*  Yeah. It's tricky. I mean, we don't walk around as humans usually thinking about the smallest bit
*  of the task. It's kind of a nerdy concept. Yeah. I just was joking to somebody. You want to pretend
*  you're Dickens and you're being paid by the word for your reasoning between the input and output.
*  Well, what's that old thing that they... I feel like everyone does this in elementary school where
*  it's there's two people, one person is going to make a peanut butter jelly sandwich and then
*  you have to give them instructions on how to make the peanut butter jelly sandwich and the person on
*  the other side is instructed to only do what the person tells you to do. And chaos always ensues
*  because it turns out it's a lot more complicated to describe how to make a peanut butter jelly
*  sandwich than we think it actually is. So it feels a little bit like that experience at the end of
*  the day. That's a good exercise that maybe schools should be doing more of because clear communication
*  certainly seems like it's always valuable, but yeah, only heading upward in importance and returns.
*  Yeah. It's not lost on me that I do think the people with the best communication skills might
*  end up being really exceptional managers. Like folks that are just really well equipped to doing
*  this might actually end up being some of the folks who have already developed some of the best skills
*  for working in this world because they're used to delegation. They're used to describing their
*  intent really well. And they might end up really thriving in like this next chapter of the economy
*  because they've already tuned this engine really well versus maybe the rest of us who are still
*  trying to figure exactly what delegation means might have some work to do.
*  Shifting focus a little bit to how you guys are working internally at Zapier. How would you
*  describe the productivity gains that you've seen within the company? Obviously, software development
*  is one seemingly very natural use case. Are you guys able to qualitatively or quantitatively say
*  we're producing more software in a given unit of time? Do you have tools, best practices? Is
*  everybody using cursor? What's it look like now within Zapier just on the development front?
*  The biggest step function change we saw was probably 15, 16 months ago where this would
*  have been probably around the time of G54 release. We stopped the company for a full week and said,
*  hey, we're going to do hands down, we're going to do AI hackathon. And it's for everybody,
*  not just engineers, everybody in the company. So if you're an engineer, we want you to go build
*  with this stuff. If you're a non-engineer, we want you to go use it, get used to these things,
*  figure out what it's doing, et cetera. And in the weeks and months after that, we saw the adoption
*  of AI go from probably 10% of the workforce to past 50. I think it got up to maybe 60, 70% of the
*  workforce using it as a day-to-day tool in their job. Qualitatively, it is like a very common tool
*  in people's tool chests. It's hard to measure exactly quantitatively where that's showing up.
*  Engineers are using copilots, there's a lot of buzz around cursor, cloud artifacts are a lot of
*  fun to play with. There's a lot of just people using it to write code. They're using it to write
*  integration code. They're using it to write just any sort of feature. So that's super common.
*  You are a data analyst. That's a team that if you said, hey, what if we took JAT-GPD away from you,
*  what would you do? And you're going to pry it from our cold dead hands. So there's huge step
*  function gains and functions like that. I think on the GTM side, seeing a lot on
*  various forms of content creation, I think you got to be careful there. A lot of companies I see
*  use it in ways that are borderline spam. It's not actually going to help them stand out and do
*  interesting things. But I think, again, if you're using it as an assistant, and if you're really
*  trying to make sure like, here's what your quality bar is, here's the types of things you want out of
*  this. If you have really good prompts, you can find a way to generate hyper personalized emails
*  at scale. You can find a way to generate really good templates around how your product works,
*  really good. If you're e-commerce, you can generate great product descriptions for the products you
*  have. There's these use cases that around the content generation side, they're really quite
*  good. But I find the degree of quality there to be quite wide right now. So there's a lot of folks
*  where I'm like, don't do that. You're going to give the industry a bad name if it doesn't already
*  have a bad name. But the people who are using it very deftly, I think are having a ton of success.
*  Our HR team has been huge adopters of this stuff. They're using it all throughout onboarding to
*  help guide folks into the company. We have chat bots for all of our handbooks, documentation,
*  things like that. It's super common experience probably in any company where you like drop into
*  a Slack channel, can anyone give me the answer to this? In the past, there's a fleet of humans
*  answering those questions, even though it's been answered before, it's in some document somewhere.
*  So our HR team has done a really good job of consolidating those into chat bots and setting
*  up Slack bots that answer that stuff on their behalf. Using it for like to, again, an assistant
*  for helping you write really good performance reviews. I think performance reviews in every
*  company is everybody's worst nightmare or headache to do. And so we've got little chat bots that help
*  people just, hey, toss their accomplishments, the things they got to work in, and it'll just write
*  it for you. And so it saves everybody time to just be like, do the sloppy version of it. And it
*  ends up actually being quite good versus wasting all this time on like polish and presentation and
*  all that stuff that doesn't matter. I think we've just seen across the company in every department,
*  people are going through the learning curve of figuring out where can we use these tools to
*  up-level the work we do. And not everything's a winner. There's certain stuff, like a lot of
*  companies are talking about how much success they're having, for example, in customer service.
*  I think for us, we're actually finding it harder to get gains in customer service than others are
*  finding. And I think maybe that is because the diversity of our support, the technical of our
*  support is pretty high. Now we're still having success there, but it's not like the Klarna example
*  that made the waves probably, what was it, six months ago, where it was like, we were able to
*  get rid of 700 jobs or whatever. And I looked at that and I was like, yeah, I think that's probably
*  because they weren't doing much with automation to begin with. And so they had just a lot more gains
*  to be had where I think we were already pretty sophisticated on this front. And so the gains that
*  we could eke out of it were just not as much. I don't know. We're still working on it. We still
*  think there's a lot of improvements that could be had. We just haven't quite cracked the nut yet.
*  Yeah. I think your mileage probably varies and it just requires a lot of experimentation is what
*  we're finding. Yeah. Certainly everything is extremely context dependent. You mentioned
*  stopping the company for a week. I love that anecdote. Beyond that, have you done anything
*  else? For example, I see companies with all kinds of different intuitions, right? Some are like,
*  we want to have a bottoms up experimental culture. We want to give prizes to the people that come up
*  with the best AI automations. Others are like, this is going to be, thou shalt not put anything
*  into chat GPT, but it's not officially sanctioned. How do you approach that? There's also management,
*  right? Do you set an expectation? Everybody's going to do something. You're going to be accountable
*  on a quarterly basis for some AI adoption milestone or whatever. How have you approached that from a
*  cultural standpoint? What would you recommend to others? Yeah. I think you got to feel it out. We
*  started in sort of like a little bit more of a bottoms up approach and around the chat GPT
*  launch, we just were like, yeah, hey, this is cool. Like you should check it out. Everybody should
*  try it. Just trying to soft influence to get folks doing it. When the GPT four launch came out, we
*  felt, okay, this needs to be a lot more of a tops down mandate. And so that's when we stopped the
*  company for the week and said, Hey, you got to go do this and we got to go figure this out. I think
*  now we have a bit more of a healthy mix where it's like in some places we're like, Hey, there is a
*  strategic imperative reason for us to go figure this out. So we are going to say this needs to
*  happen. And other areas of the company, it's more just like, Hey, you're smart. You know, tools,
*  you figure it out. You're going to figure it out. And we're just keeping tabs on that stuff.
*  In terms of things that have worked to keep the drum beat going, we've done a couple things. When
*  we ran the hackathon, we worked with both legal and our technical teams and data privacy and all
*  that sort of stuff to set up some rules of engagement, to make sure it was done in a way
*  that we felt, you know, took really good care of customer data and all that sort of stuff.
*  We felt like it was important to have guardrails around some of those things. I would not suggest
*  just going wild west without working with your teams to create the proper environment to do this.
*  That was a really important first step for us that we did in combination with legal engineering
*  teams, things like that. And then since we've gotten on from that, we do an all hands every
*  Thursday, once a week, every month or so, we usually will do like an AI showcase as part of those
*  all hands. We'll just curate maybe half a dozen use cases and folks will record little videos or
*  come in and show off things live. And it'll just be like showing off what they do. And so that pushes
*  some cool use cases, get people's minds churning. We have a fun AI channel inside of Slack where
*  people are showing off stuff that they're building, things that they're playing with. We have a
*  handful of both engineers and non-technical, but like very sophisticated AI builders that will do
*  weekly AI office hours that anyone can just show up and share stuff around. We just tried to
*  foster these forums, whether they're official forums, tops down, do it this way, or just
*  employees taking initiative and figuring these things out. We just generally tried to put more
*  behind any of these things because we think that there's just so much goodness that can come from
*  that. It does require a little bit of the company to encourage it and nudge it along.
*  I think the biggest thing that I would tell other leaders is don't be shy about saying this is
*  important. I think that's why you've seen a lot of the founder led businesses have probably done
*  better during this period is because we're able to just come in and say, let's go do it. I think
*  more companies have that ability than they realize to say, this is important. If we sleep on this
*  stuff, it's going to be a problem. Maybe it's not a problem today, but give it a year, give it five
*  years. I think for almost any business, it's going to be a problem. Five years is a long time in this
*  space. Oh, yeah. Super long time. Five years, everybody's stuff is going to look different.
*  When you referred to some areas being top down strategic mandate, is that like core product
*  experiences or anything else outside of that? And then I always ask of entrepreneurs, what would a
*  10x more expensive version of the product look like where you spared no expense on the AI?
*  You have also the Zap Connect event happening. So maybe tie all those together. What are the
*  sort of new strategic initiatives product wise? Where are you applying more AI than ever before?
*  And whether or not that translates into a higher price point?
*  Yeah. I think in terms of a 10x higher price point, generally for us, that's going to mean
*  moving from like a suite of tools to actually like solving bigger sets of solutions. And for us,
*  where that sort of intersects with AI is we've launched things like tables, interfaces, chat
*  bots, in addition to our workflow engine, we have one that's coming around code. And I think in all
*  of these cases, we're thinking through what does like an AI first interface look like in those
*  motifs? I think the world was captured by chat GPT and we all felt, oh, chat is the new user
*  experience. But the further I get from that, I actually think a lot of the more traditional
*  UIs we're used to interacting with are still great user experiences. A table is a really good way to
*  interact with stuff. A workflow is a really good way to interact with this stuff. But what if you
*  reinvented it with AI as a first order primitive in these experiences? So that's a thing that we're
*  paying a lot of attention to. And then on the enterprise side, we're trying to figure out how
*  do we package all these things together to solve a 10x, 100x type of problem for you so that you as
*  the end user don't have to walk in and figure out how to configure all this stuff from the ground
*  up. We can come in and say, hey, here's more of an end to end solution out of the box. Maybe you have
*  to tweak some things on the edges, but you're not having to build the whole dang thing from the
*  ground up, which right now is as a DIY or as Haven, like it's the best place to hang out. But I think
*  we can do a little bit better job of just packaging some of the best use cases up for folks
*  and saying, hey, this right here is going to change the way your marketing team works. So this is
*  going to change the way your HR team works. This is going to change the way your finance team works.
*  If you use Zapier in this specific way. Done for you by AI beats do it yourself. Services are one
*  of the best places for AI right now is that services are premium priced experiences that AI
*  can you can offload a good chunk of the work to an AI. So you can still solid a premium, but the
*  labor to use it, you just went way, way, way down. Does that collapse? It seems like that collapses.
*  That's capitalism in a nutshell, right? What's the Jeff Bezos saying? Your margin is my opportunity.
*  So eventually capitalism competes away all this stuff and who wins? Consumers. We all win.
*  Yeah. High consumer surplus is definitely one of my main predictions for the next few years.
*  Totally. It's going to be fun for the consumer. I think for us that are built in software,
*  it'll be fun too, but I'm sure there's going to be some stressful moments as well.
*  Yeah. Well, this is great. I appreciate the time. Anything else you want to
*  talk about in terms of event, new launches, or just anything else we didn't get to?
*  Come check out Zapier. We are not the same old product that you all have maybe remember is like
*  that simple integrations tool. You can build a lot of crazy stuff on the right now. We are a small
*  business enterprise, tables, interfaces, automation, full on across the board. It's
*  been a fun couple of years of shipping over here. Love it. Wade Foster, CEO of Zapier.
*  Thank you for being part of the cognitive revolution. Thanks Nathan.
*  It is both energizing and enlightening to hear why people listen and learn what they value about
*  the show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can
*  DM me on the social media platform of your choice.
