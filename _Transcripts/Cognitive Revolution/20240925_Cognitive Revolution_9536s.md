---
Date Generated: September 26, 2024
Transcription Model: whisper medium 20231117
Length: 9536s
Video Keywords: []
Video Views: 365
Video Rating: None
Video Description: In this crosspost from the 80,000 Hours podcast, host Rob Wiblin interviews Nick Joseph, Head of Training at Anthropic, about the company's responsible scaling policy for AI development. The episode delves into Anthropic's approach to AI safety, the growing trend of voluntary commitments from top AI labs, and the need for public scrutiny of frontier model development. The conversation also covers AI safety career advice, with a reminder that 80,000 Hours offers free career advising sessions for listeners. Join us for an insightful discussion on the future of AI and its societal implications.

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
(00:04:31) Intro and Nick's background
(00:08:37) Model training and scaling laws
(00:13:10) Nick's role at Anthropic
(00:16:49) Responsible Scaling Policies overview (Part 1)
(00:18:00) Sponsors: Weights & Biases Weave | 80,000 Hours
(00:20:39) Responsible Scaling Policies overview (Part 2)
(00:25:24) AI Safety Levels framework
(00:30:33) Benefits of RSPs (Part 1)
(00:33:15) Sponsors: Omneky
(00:33:38) Benefits of RSPs (Part 2)
(00:36:32) Concerns about RSPs
(00:47:33) Sandbagging and evaluation challenges
(00:54:46) Critiques of RSPs
(01:03:11) Trust and accountability
(01:12:03) Conservative vs. aggressive approaches
(01:17:43) Capabilities vs. safety research
(01:23:47) Working at Anthropic
(01:35:14) Nick's career journey
(01:45:12) Hiring at Anthropic
(01:52:06) Concerns about AI capabilities work
(02:03:38) Anthropic office locations
(02:08:46) Pressure and stakes at Anthropic
(02:18:09) Overrated and underrated AI applications
(02:35:57) Closing remarks
(02:38:33) Sponsors: Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Anthropic's Responsible Scaling Policy, with Nick Joseph, from the 80,000 Hours Podcast
**Cognitive Revolution:** [September 25, 2024](https://www.youtube.com/watch?v=X0wElHKsbc8)
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
*  Hello, and welcome back to the Cognitive Revolution. Today, we're sharing a cross-post
*  from the 80,000 Hours podcast in which host Rob Wiblin interviews Nick Joseph, head of model
*  pre-training at Anthropic, about the responsible scaling policy that governs the company's frontier
*  model development. I've been following the development of these policies and other
*  voluntary commitments from Top Labs for much of the last year. At one point, I had the opportunity
*  to participate in a workshop with Anthropic team members in which we reviewed, discussed,
*  and offered comment on the responsible scaling policy draft. However, I could not easily convert
*  that experience to a podcast, and so I was particularly excited to see this episode published,
*  and really appreciate that the 80,000 Hours podcast team has allowed me to repost it here.
*  On the substance of the matter, I, of course, very much appreciate how hard Anthropic is thinking
*  about AI risks and what can be done about them, and also how transparent and even candid they are
*  willing to be about the substantial uncertainty that remains. I'm also very glad that their
*  example seems to have inspired others. OpenAI and Google have since published similar policies,
*  and I understand that XAI is working on one as well. Unfortunately, however, the trend does not
*  yet appear to be universal. Meta, for example, to the best of my knowledge, has not published
*  a policy describing how it plans to evaluate models during training, let alone how they
*  plan to proceed if it turns out that they are developing dangerous capabilities.
*  As we happen to be sharing this episode with just a few days left before California Governor
*  Kevin Newsom will have to sign or veto SB 1047, I will take a moment to say one more time that
*  while it may not be the perfect AI safety bill, and indeed the release of OpenAI's O1 model,
*  and the emerging paradigm of scalable inference time compute generally, do suggest that the
*  definitions in the bill would need to be updated to stay relevant over time. In my view, the public
*  does deserve to know what Frontier Labs are doing, and that goes double for Meta and any other
*  companies who are openly sharing model weights. So whatever the fate of SB 1047 may be, I do
*  think that we will need some measure that forces Frontier model developers to publish detailed
*  safety plans for public scrutiny. In the last hour of this episode, Rob and Nick changed topics to
*  focus on AI safety career advice. While this is not a sponsored episode, Nick's experience with
*  80,000 Hours Career Advising Service echoes my own and presents a natural opportunity to remind
*  you that 80,000 Hours is now offering free one-on-one career advising sessions to Cognitive
*  Revolution listeners. I encourage everyone to sign up for a free session at 80,000hours.org
*  Cognitive Revolution, and especially so if you are one of the experienced software engineers
*  that Nick notes are in such high demand among AI companies right now. As always, if you're finding
*  value in the show, we'd appreciate it if you'd take a moment to share it online with friends
*  or write us a review on Apple Podcasts or Spotify. Your feedback is always welcome too,
*  either via our website cognitiverevolution.ai or by DMing me on your favorite social network.
*  Now, for an in-depth conversation about Anthropic's responsible scaling policy and breaking into AI
*  safety in your career, here's Nick Joseph from Anthropic with host Rob Wiblin of the 80,000
*  Hours Podcast. I think this is a spot where there are many people who are skeptical that models will
*  ever be capable of this sort of catastrophic danger, and therefore they're like, we shouldn't
*  take precautions because the models aren't that smart. And I think this is a nice way to agree
*  where you can, it's much easier message to say, if we have evaluations showing the model can do X,
*  then we should take these precautions. And I think you can sort of build more support for something
*  along those lines, and it targets your precautions at the time when there's actual danger. One thing,
*  other thing I really like is that it aligns commercial incentives with safety goals. So
*  once we put this RSP in place, it's now the case that our safety teams are kind of under the same
*  pressure as our product teams, where if we want to ship a model and we get to ASL3, the thing that
*  will block us from being able to get revenue, being able to get users, et cetera, is do we have
*  the ability to deploy it safely? And it's a nice outcome based approach where it's not,
*  did we invest X amount of money in it? It's not, did we try? It's, did we succeed?
*  Hey everyone, Rob Woodland here. The three biggest AI companies, Anthropic, OpenAI, and DeepMind,
*  have now all released policies designed to make their AI models less likely to go rogue
*  while they're in the process of becoming as capable as, and then gradually more capable than,
*  any human being. Anthropic calls their one a responsible scaling policy or RSP,
*  OpenAI uses the term preparedness framework, and DeepMind calls their one a frontier safety
*  framework. But fundamentally, they all have a lot in common. They try to measure what possibly
*  dangerous things each new model is actually able to do. And then as that list grows,
*  put in place new safeguards that feel proportionate to the risk that they think exists at that point
*  in time. This is likely to remain the dominant approach, at least in industry. So I was really
*  excited to speak with Nick Joseph, one of the original co-founders of Anthropic and a big
*  outspoken fan of responsible scaling policies about why he thinks Anthropic's RSP has a lot
*  going for it, how it might make a real difference as we approach the training of a true full AGI,
*  and why in his view, it should be thought of as a sort of middle way that ought to be acceptable
*  to almost everyone. After hearing out that case, I push Nick on the best objections to RSPs that
*  I could either come up with myself or find on the internet. And those include that one, it's hard
*  to trust that companies are going to stick to that RSPs long term. Two, it's difficult to truly
*  measure what models can and can't do. And an RSP is useless if it's mismeasuring model capabilities.
*  Three, it's pretty questionable whether profit motivated companies will go out of their way to
*  act in good faith and make their lives and their product releases much more difficult.
*  And four, that in the most important cases, we just don't have safeguards that are able to
*  render new AI capabilities safe, even capabilities that could show up really soon. At the end of the
*  day, I come down thinking that responsible scaling policies are a really solid step forward from
*  where we are now. And they're a great way to test and learn what works and what feels practical
*  from the experience of people who are working on the core face of trying to make this technological
*  revolution actually happen. But I think in time, they're going to have to be put into legislation
*  and operated by external groups or auditors rather than stay left just to companies themselves,
*  at least if they're going to achieve their real potential or the full potential that I think is
*  there. Of course, Nick and I debate that take of mine as well. If you want to let us know your
*  reaction to this interview or any other interview that we do, then our inbox is always open at
*  podcast at 80000hours.org. But now here's my interview with Nick Joseph recorded on the 30th
*  of May, 2024. Today, I'm speaking with Nick Joseph. Nick is head of training at the major
*  AI company Anthropic, where he manages a team of over 40 people focused on training Anthropic's
*  large language models, including Claude, which I bet you many, many listeners have heard of and
*  and potentially used as well. He was actually one of the relatively small group of people to
*  to leave OpenAI alongside Dario and Daniel Amadei, who then went on to found Anthropic back in
*  December of 2020. So thanks so much for coming on the podcast, Nick. Thanks for having me. I'm
*  excited to be here. I'm really happy to talk about how Anthropic is trying to prepare itself
*  for training models capable enough that we're a little bit scared of what they what they might
*  go and do. But first, as I just said, you lead model training at Anthropic. What's something that
*  people get wrong or kind of misunderstand about AI, AI model training? I imagine there could be
*  quite a few things. Yeah, I think one thing I would point out is the sort of doubting of scaling
*  working. So for a long time, we've we've had this trend where people put more compute into models,
*  and that leads to the models getting better, smarter in various ways. And every time this has
*  happened, I think a lot of people are like, this is the last one, you know, your the next scale up
*  isn't going to help. And then, you know, some chunk of time later, things get scaled up and it's it's
*  much better. And I think this is something people just frequently gotten wrong. This whole vision
*  that scaling is just going to keep going. You know, we just make just throw in more data, throw in
*  more compute, the models are going to become more powerful. That was kind of the part of the it
*  feels like a very anthropic idea. It was part of the founding vision that that Dario had, right?
*  Yeah. So like a lot of the early work on scaling laws was done by a bunch of the anthropic founders.
*  And it somewhat led to GPT-3, which was done in OpenAI, but by many of the people who are now at
*  anthropic, where looking at a bunch of small models going up to GPT-2, there was sort of the sign that
*  as you put in more compute, you would get better and better. And it was very predictable. And you
*  can say, if you put in X more compute, you'll get a model this good. And that sort of enabled the
*  like confidence to go and train a model that was rather expensive by the time standards to to sort
*  of verify that hypothesis. What do you think is kind of generating that skepticism that many
*  people have? I mean, like people who are skeptical of scaling laws, there's some pretty smart people
*  who are kind of involved in ML, certainly certainly have their technical chops. Why do you think they
*  generating this prediction that you disagree with? Yeah, I think it's just a really like
*  unintuitive mindset or something where it's like, ah, the model has, you know, hundreds of billions
*  of parameters. What does it need? It really needs like trillions of parameters, or the model is
*  trained on like, you know, some fraction of the internet that's very massive. Like, what does it
*  need to be smarter? It's even more like that's not how humans learn. If you sort of send a kid to
*  school, you don't you don't have them just read through like the entire internet and think that
*  the more that they read, the smarter they'll get. So yeah, that's sort of my best guess. And the other
*  piece of it is that it's quite hard to do the scaling work. So there are often things that you
*  do wrong when you're when you're trying to do this the first time. And if you mess something up, you
*  will see this behavior of like more compute not leading to better models. And it's always hard to
*  know if it's like you messing up or if it's some sort of fundamental, fundamental limit where the
*  model has stopped getting smarter. I mean, the argument for why you might expect these scaling
*  laws, you know, scaling laws, it's that you increase the amount of compute and data by some
*  particular proportion, and then you get a similar improvement each time in in the accuracy of the
*  model. That's kind of the rule of thumb here. And the the argument that I hope for why you might
*  expect that trend to break, and that's the improvements to become smaller and smaller for
*  a given given scale up, is something along the lines of, you know, as you're approaching human
*  level, the model can learn by just copying existing state of the art of what humans already doing in
*  the in the in the training set. But then if you're trying to exceed human level, if you're trying to
*  do, you know, write better essays than any human has ever written, then that's maybe a different
*  regime. And you might expect it like more gradual person like more gradual improvements. So once
*  you're trying to get to a superhuman level, do you think that that argument kind of holds up?
*  Yeah, so I think that I think that's true. And like, just sort of pre training on more and more
*  data won't get you to superhuman at some tasks, it will get you to superhuman in the way of like
*  understanding everything at once. This is already sort of true of models like Claude, where you can
*  ask them about anything, whereas humans sort of have to specialize. But I don't know if progress
*  will necessarily be slower, it might be slower, it might be faster. Once you sort of get to the
*  level where models are all right, human abilities on everything and improving towards super
*  intelligence, we haven't really but we're still pretty far from there. Like if you use Claude now,
*  I think it's like pretty good at coding. But for this is one one example I use a lot, but it's still
*  pretty far from like how well a human would do working on as a software engineer, for instance.
*  And is the argument for how it could speed up that at the point that you're near human level,
*  then you can use the AIs in the process of doing the doing the work? Or is it something else?
*  What I have in mind is like, yeah, if you had if you had an AI that is human level at everything,
*  and you can spin up millions of them, you effectively now have a company of like millions of
*  AI researchers. And it's, it's hard to know, right? Things, problems get harder, too. So
*  I don't really know where that leads. But at that point, I think you've sort of crossed
*  crossed quite a quite a ways from where we are now. So you're in charge of model training,
*  I guess there's I know there's different stages of model training. There's the bit where you kind of
*  train the language model on the entire internet. And then there's the bit where you like do the
*  fine tuning where you get you get it to spit out answers and then you rate whether you like them
*  or not. Are you in charge of all of that? Or just some part of it? Yes, I'm just in charge of what
*  was sort of typically called pre training, which is where this step of train the model to predict
*  the next word on the internet. And that tends to be like historically is a significant fraction
*  of the compute. It's maybe 99% in many cases. But after that, the model sort of goes to what
*  we call fine tuning teams that will sort of take this model that just just predicts the next word,
*  and fine tune it to act in a way that a human wants sort of be this sort of like helpful assistant.
*  We have this helpful, harmless and honest is the is the acronym that we usually aim for for for
*  cloud. Yeah, I use cloud three opus multiple times a day every day. Now, it took me a little
*  while to figure out how to actually use these elements for anything. For I guess the first
*  six months or first year, I was like, these things are amazing. But I can't figure out how to actually
*  incorporate them into my life. But recently, I've started talking to them in order to like learn
*  about the world is kind of substituted for when I would be typing complex questions into Google to
*  understand some bit of history or science or some technical issue. I guess what's what's the main
*  bottleneck that you face making these models smarter so so I can get more get more use out of
*  them? Yeah, so let's see, I think there's sort of historically people talked about these three
*  bottlenecks of data, compute, and like algorithms. I kind of think of it as Yeah, so there's some
*  amount of just compute. We've we talked about scaler to go if you put more compute with the model,
*  it will do better. There's data where if you're training on, if you're putting in more compute,
*  one way to do it is to add more parameters to your model, make your model bigger. But the other way
*  you need to do is to add more data to the model. So you need both of those. But then the other two
*  are algorithms, which I really think of as people. Maybe this is the manager in me is like, you know,
*  algorithms come from people in some ways, data and compute also come from people. But it looks
*  like a lot of researchers working, working on the problem. And then the last one is time, which has
*  felt more kind of urgent, more true recently, where things are moving very quickly. So a lot of the
*  bottleneck to progress is actually like, we know how to do it, we have the people working on it,
*  but it just takes some time to implement the thing and turn and run the model, train the model,
*  right? Like you can maybe afford all the compute and you can you have a lot of it, but you can't
*  efficiently train the model in like a second. So right now at Anthropic, it feels like people in
*  time are probably the main bottlenecks or something. Like I feel like we have quite a significant
*  amount of compute, significant amount of data. And the things the things that are like most limiting
*  at the moment, I feel like people on time. So what do you say time is that kind of indicating
*  that you're doing a sort of iterative like an experimental process where you know, you try
*  tinkering with how the model learns in one direction, then you want to see whether that
*  actually gets the improvement that you expected. And then it takes time for those results to come
*  in. And then you get to scale that up to the whole thing. Or is it just a matter of, you know,
*  you're already trading Claude for or you already have the next thing in mind, it's just a matter
*  of waiting. So it's both of those like for the next model, you know, a bunch of researchers who
*  are trying projects out and they have to, you know, you have some idea, and then you have to go and
*  implement it. So you'll spend a while sort of engineering this this idea into the code base.
*  And then you need to run a bunch of experiments. And typically, you'll start with cheap versions
*  and work your way up to more expensive versions, such that this process can can take a while.
*  For simple ones, it might take a day. For really complicated things, it could take months. And
*  to some degree, you can paralyze but on certain directions, it's much more like someone you're
*  building up an understanding and it's hard to paralyze like building up an understanding of how
*  something works. And then designing like the next experiment, there's just sort of in serious aspect.
*  Is improving these models is sorry, is improving these models harder or easier than than people
*  think? Well, I guess people think different things on it. I think my experience has been that like,
*  early on, I would have it felt very easy. I worked for before working at OpenAI, I was working on
*  robotics for a few years. And one of the tasks I worked on was locating an object so we can pick
*  it up and drop in the box. And it was really hard. I spent years on this problem. And then
*  went to open AI and I was working on code models. And it just felt shockingly easy. It was like,
*  wow, you know, you just throw some compute, you train on some code and the model can write code.
*  I think that has now shifted like we've now and the reason for that was no one was working on it.
*  There was just very little attention to this direction. And a ton of low hanging fruit.
*  We've now plucked a lot of the low hanging fruit. So finding improvements is much harder.
*  But we also have way more resources, like exponentially more resources put on it,
*  there's way more compute available to do experiments, there are way more people
*  working on it. And I think the rate of progress is probably still going like the same given that.
*  Okay, so you think on the one hand, the problem's gotten harder. On the other hand,
*  there's more resources going into it. And this is kind of cancelled out and like,
*  progress is roughly, roughly stable. Yeah, it's pretty bursty. So it's like,
*  it's hard to know, you know, you'll have like a month where it's like, wow, every we figured
*  something out, everything's going really fast, then you'll have a month where you try a bunch
*  of things that don't work. And it varies. But I don't think I don't think there's really been
*  a trend in the direction. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. Today's episode is brought to you in part by weights and biases. As a developer,
*  the journey from concept to production ready large language model apps is fraught with challenges
*  dealing with unpredictable large language model outputs, correctly handling PII and ballooning
*  API costs can all be blockers to shipping your next AI powered feature. Weights and biases weave
*  is a lightweight AI developer toolkit designed to simplify your large language model app development.
*  With weave, you can trace and debug input metadata and output with just two lines of code.
*  We've helps you run rigorous evaluations and securely manage all of your data sets and system
*  configurations. So you can focus on what matters most iterating and improving on your large language
*  model powered applications. Plus, we've integrates seamlessly with your favorite
*  API's and libraries, including open AI, anthropic, Mistral, cohere, Lang chain, llama index, and more.
*  So make real progress on your large language model development. Visit wmb.me.cr to get started with
*  weave today. That's wmb.me.cr. And thanks to weights and biases for sponsoring this episode.
*  I am really excited that our new sponsor, 80,000 hours, is now offering free one-on-one career
*  advising sessions to cognitive revolution listeners. 80,000 hours aims to be the best source of advice
*  for people who want to do the most good that they possibly can with their careers. We typically work
*  for about 40 years in our lifetime and we work about 2000 hours per year. That is the single biggest
*  opportunity that most of us have to make a positive contribution and it's worth being strategic about
*  it. That's where 80,000 hours can help. I actually used their career advising service myself. Two years
*  ago, I had just finished the GPT-4 red teaming project and I wanted to do anything I could to
*  nudge the AI future in a positive direction. But what could or should I do? That was not clear.
*  After my call with 80,000 hours, I got a number of connections to outstanding individuals in the
*  space and over the course of the follow-on conversations, I developed confidence that this
*  podcast was one of the projects that I should pursue. Today, I'm thrilled to have built an
*  audience of thoughtful, high potential people that 80,000 hours wants to help. To request a free
*  one-on-one career advising session, follow the link in the show notes. It's 80,000 hours.org
*  slash cognitive revolution. That's 80,000 hours.org slash cognitive revolution. Sign up for a free
*  one-on-one career advising session, figure out how you can make a positive impact on the AI future,
*  and I think you'll be glad that you did. Do you personally worry that having a model
*  that is kind of nipping at the heels or maybe out competing the best stuff that OpenAI or DeepMind
*  or just whatever other companies have, that maybe puts pressure on them to speed up their
*  releases and cut back on safety testing or anything like that? I think it is something
*  to be aware of, but I also think that at this point, I think this is really more true after
*  ChatGPT. I think before ChatGPT, there was this sense where many AI researchers working on it were
*  like, wow, this technology is really powerful. But I think the world hadn't really caught on,
*  and there wasn't quite as much commercial pressure. Since then, I think that there really is just a
*  lot of commercial pressure already, and it's not really clear to me how much of an impact it is.
*  I think there is definitely an impact here, but I don't know the magnitude, and there are a bunch
*  of other considerations to trade off. All right. Let's turn to the main topic for today,
*  which is responsible scaling policies or RSPs, as the cool kids call them. For those who don't know,
*  scaling is this technical term for using more compute or data to train any given AI model.
*  And the idea for RSPs has been around for a couple of years, and I think it was fleshed out maybe
*  after 2020 or so. It was advocated for by this group now called METR, or Model Evaluation and
*  Threat Research, which actually is the place that's previous guest of the show, Paul Cristiano,
*  I was working until not very long ago. Anthropic released the first public one of these, as far
*  as I know, last October. And then OpenAI put out something similar in December called their
*  preparedness framework. And Demis of DeepMind has said that they're going to be producing something
*  in a similar spirit to this, but they haven't done so yet, as far as I know. So we'll just have
*  to wait and see. It's actually, yeah, they have done it. Oh, okay. It was published a week ago.
*  Oh, okay. Maybe I'll ask you about that later. But yeah, that just goes to show that RSPs are
*  kind of this reasonably hot idea, which is kind of why we're talking about them today. And I guess
*  some people also hope that these internal company policies are ultimately going to be a model that
*  might be able to be turned into binding legislation that everyone dealing with these frontier AI models
*  might be able to follow in future. But yeah, Nick, what are responsible scaling policies in a nutshell?
*  So I might just start off with a quick disclaimer here that this is not my direct role. I'm sort of
*  bound by trying to implement these and sort of act under one of these policies. But many of my
*  colleagues have worked on designing this in detail and are probably more familiar with all the
*  deep ones than me. But anyway, in a nutshell, the idea is it's a policy where you define various
*  safety levels. So these sort of different levels of risk that a model might have and create
*  evaluations. So tests to say, is this model able to, is a model this dangerous? Does it require
*  this level of precautions? And then you need to also define sets of precautions that need to be
*  taken in order to train or deploy models at that particular risk level. Yeah, I think this might
*  be a topic that is just best learned about by kind of skipping the abstract question of what RSPs are
*  just talking about the the anthropic RSP and seeing what it actually says that you're going
*  to do. So yeah, what does the anthropic RSP going to promise commit the company to doing?
*  Yeah, so we basically sort of for every level will define these red line capabilities, which
*  are capabilities that we think are dangerous. I can maybe give some examples here, which is
*  this acronym CBRN, chemical, biological, radiological, nuclear threats. And in this
*  area might be that a non-expert can make some weapon that can kill many people as easily as an
*  expert can. So this would sort of increase the pool of people that can do that a lot. On cyber
*  attacks, it might be like, can we kind of model help with some really large scale cyber attack?
*  And on autonomy, can the model like perform some tasks that are sort of precursors to autonomy,
*  is sort of our current one. But that's a tricky one to figure out. So it is we like establish these
*  these red line capabilities that we shouldn't train until we have safety mitigations in place.
*  And then we create evaluations to show that models are far from them or to know if they're not. So
*  these evaluations have to test for that capability because you want them to turn
*  up positive before you've trained a really dangerous model. But we can kind of think of
*  them as yellow lines. Once you get past there, you should re-evaluate. And the last thing is
*  then developing standards to make models safe. So we want to have a bunch of safety precautions in
*  place once we train those dangerous models. So that's sort of the main aspect of it. There's
*  also sort of a promise to like iteratively extend this. So creating the evaluations is really hard.
*  We don't really know what the evaluation should be for like a super intelligent model yet. So
*  we're kind of starting with the closer risks. And once we hit that next level, defining the one
*  after it. So pretty cool component of the anthropic RSP is this AI safety level framework. So I think
*  you borrowed that from the biological safety level framework, which I think is what
*  labs dealing with dangerous diseases use. So I guess I don't know what the numbers are,
*  but if you're dealing with Ebola or something that's particularly dangerous, or smallpox or
*  whatever, then that can only be stored in a BSL4 lab or something like that. And then as the
*  diseases become less dangerous, you can store them with fewer precautions. And you've kind of taken
*  that language and talked about AI safety levels. And the current AI safety level that you put
*  us out is ASL2, which is things like Claude 3, which are kind of impressive. They seem pretty
*  savvy in some ways, but they don't seem like they really pose any meaningful catastrophic risk.
*  I guess, what sort of tests have you run on Claude 3 recently maybe in order to say,
*  yeah, this is in the ASL2 bucket? Yeah, so we've got a bunch of tests. So the first one we use for
*  the more like a biological weapon type of angle is there's sort of a bunch of multiple choice
*  questions that we ask the model. And this is like the idea, this isn't a perfect evaluation
*  for this, but the idea is that we have a set where if it gets, if it isn't much better at this,
*  it probably won't be able to help very much. And then we've run trials with people where they get
*  access to a search engine and they get access to Claude. And we see if they do significantly better
*  at going through some really relevant tasks using Claude versus a search engine.
*  I guess, and another one of the kind of yellow flags for you is the possibility that an AI model
*  might be able to replicate itself in the wild or kind of find its own weights and then copy
*  itself onto other computers. Did you test whether Claude 3 was showing any signs of being able to
*  do that? Yeah, so I think some of the tasks there would be, one of them is adding an exploit to a
*  popular open source code base. So this is an idea of if the model can add some exploit that can then
*  be taken advantage of or fine tuning an open source LLM to add some backdoor where if you say
*  X, it will always output something. This is like, can it manipulate LLMs? It could steal an API key
*  from our API or a fake version of our API that was set up, which would sort of enable it to get
*  credits. There are a few more of these, but the, or yeah, another one would be like a worm that can
*  spread undefended machines. So you can sort of imagine a model that can do all of these, has
*  learned a bunch of the skills that might enable it to sort of autonomously replicate and cause
*  havoc. There are pretty early signs of it. And we want to sort of test for the early ones, because
*  this is sort of an area that's like less fleshed out where there's sort of less clear expertise on
*  what might go wrong. Okay, so we're at the safety level two, which is kind of not like, I guess,
*  the mostly harmless category. But what sort of steps does the does the responsible scaling policy
*  call for you to be taking even at this point? So we made these sort of White House commitments,
*  I think sometime last year, which I think of them as sort of like standard industry best practices.
*  In many ways, we're building the muscle for dangerous capabilities. But these models are
*  not yet capable of catastrophic risks, which is what the RSP is primarily focused on. But this
*  looks like security to protect our weights against sort of opportunistic attackers, putting out model
*  cards to describe the capabilities of the models doing training for harmless so that we don't have
*  models that can be really harmful out there. So what sort of results would you get back from
*  your tests that would indicate that now the capabilities have risen to, you know, ASL three?
*  Yeah, so if the model, for instance, passed some fraction of those of those tasks that I mentioned
*  before around adding an exploit, spreading to undefended machines, or if it did really well on
*  these biology ones, that would sort of flag it as having passed the yellow lines. At that point,
*  I think we would we would either need to look at the model and be like, this really isn't is clearly
*  still incapable of these red line dangers. And then we might need to go to the board and think
*  about was was there a mistake in RSP and how we should essentially create new evals that would
*  would test better for whether we're at that capability, or we would need to implement a
*  bunch of precautions. And these precautions would look like much more intense security where we
*  would really want this to be sort of robust to like, probably not state state actors, but to
*  non state actors. And we would want to pass the sort of intensive red teaming process on on all
*  the modalities that we release. So this would mean we look at those red lines and we test for them
*  with experts and say, you know, can you use the model to do this, we have this sort of intensive
*  process of red teaming, and then only release the modalities where it's been red team. So if you if
*  you add in vision, you need to rent team vision. If you add the ability to fine tune, you need to
*  bet in that. Yeah, what is what does red teaming mean in this context? Red teaming means you get
*  a bunch of people who are trying as hard as they can to get the model to do the task you're
*  worried about. So if you're worried about the model, like carrying out a cyber attack, you
*  would get a bunch of experts to try to prompt the model to carry out some cyber attack. And if if
*  we think it's capable of doing it, we've put all of these we're putting these precautions on and
*  these could be precautions in the model, they could be precautions outside of the model,
*  but the whole end to end system, we want to have people trying to get it to do that in some some
*  controlled manner such that we don't actually cause mayhem. Yeah, and see how they do. Okay.
*  And then so if you do the red teaming, and it comes back and they say, yeah, the model is extremely
*  good at hacking into computer systems, or it could actually help people, it could meaningfully
*  help someone develop a bioweapon, then then what is the what is the policy call for anthropic to do?
*  So for that one, it would mean we can't deploy the model. Because there's some danger this model
*  could be misused in a really terrible way. And we would sort of keep the model internal until we've
*  improved our safety measures enough that when someone asks for to do that, we can be confident
*  that they won't be able to have it help them for that particular threat.
*  Okay. And to even have the this model on your computers, the policy also calls for you to have
*  hardened your computer security so that you're saying maybe it's unrealistic at this stage for
*  that model to be safe from persistent state actors. But at least other groups that are
*  somewhat less capable than that, you would you would want to be able to make sure that they
*  wouldn't be able to steal the model. Yeah, the big the threat here is, you know, you can put all
*  the restrictions you want on what you what you do with your model. But if people are able to just
*  steal your model, and then then deploy it, you're going to have all of those dangers anyway. So
*  you're sort of taking responsibility for it means like both responsibility for what you do and what
*  someone else can do with your models. And that requires quite intense security to protect the
*  model plates. When do you think we might hit this, you know, you would say, well, now we're in the
*  SL three regime, maybe I'm not sure exactly what language you use for this. But like, at what point
*  will we have an SL three level model? I'm not sure. I think basically, we'll we'll continue to
*  evaluate our models. And we'll see when we get there. I think sort of opinions vary a lot on that.
*  We're talking kind of about the next next few years, right? This isn't something that's going
*  to be five or 10 years away necessarily. I think it really just depends. Like, I think you could
*  imagine sort of any direction. And one of the nice things about this is that we're targeting the safety
*  measures at the point when there's actually dangerous models. So like, maybe let's let's say
*  I thought it was going to happen in two years, but I'm wrong. And it happens in 10 years, we won't
*  have to we won't put these very costly and like difficult to implement mitigations in place until
*  until we like need them. Okay, so anthropics RSP. So I guess obviously, we've just been talking about
*  SL three. The next level we on that would be SL four. I think your policy basically says we're
*  not exactly sure what SL four looks like yet, because it's too soon to say. And I guess you
*  promise that you're going to have mapped out what would be the kind of capabilities that would
*  escalate things to SL four and what kind of responses you would have, you're going to figure
*  that out by the time you have trained a model that's SL three. And I guess if you haven't said so,
*  you'd have to pause training on a model that was going to hit SL three until you'd you'd finish
*  this project about that. I guess that was the commitment that's been made. Hey, we'll continue
*  our interview in a moment after a word from our sponsors. Omniki uses generative AI to enable you
*  to launch hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it. And I recommend you
*  use it to use cog rev to get a 10% discount. But maybe you could kind of give us a sense a sense
*  of what you think SL four might look like what sorts of capabilities by the models
*  would then like push us into another regime where a further set of precautions are called for.
*  So we're still discussing this internally. So I don't want to say anything that's like final
*  are going to be held to but you could sort of imagine stronger versions of a bunch of the things
*  that we sort of talked about before. And you could also imagine models that can like help with AI
*  research in a way that really majorly accelerates researchers such that progress goes much faster.
*  The core reason that we're holding off on kind of defining this or that we have this iterative
*  approach is there's this long track record of people saying, you know, oh, once you have this
*  capability, it will be a GI, it's going to be really dangerous. I think people are like, oh,
*  and an AI sells chess, like it will be as smart as humans. And it's really hard to get these
*  evaluations right. Even for like the ASL three ones, I think it's been very tricky to get,
*  get evaluations that capture the risks we're worried about. So sort of the closer you get
*  to that, the more information you have, and the better of a job you can do at sort of defining
*  what these evaluations are and risks are. So the general sense would be, you know,
*  models that might be capable of spreading autonomously across computer systems, even
*  if people were trying to turn them off, you know, would be able to provide significant help
*  with developing bio weapons, maybe even to people who are pretty, pretty informed about it.
*  I guess, yeah, what else is there? Oh, and stuff that would seriously speed up AI development as
*  well. So it could potentially set off this sort of positive feedback loop where the models get
*  smarter, that makes them better at improving themselves and so on. That's the sort of thing
*  where we're talking about. Yeah, stuff along those lines. I'm not sure which ones will end up in
*  ASL four exactly. But but like those sorts of things are what's being considered. And what
*  sorts of additional precautions might there be? I guess at that point, you kind of want the models
*  to not only be not possible to be stolen by kind of independent freelance hackers, but ideally also
*  not by countries even, right? Yeah, so you want to protect against more sophisticated groups that
*  are trying to steal the weights. We're going to want to have like better protections against the
*  model like acting autonomously. So controls around that you might want it depends a little bit on
*  like what what ended up being the red lines there, but sort of having the precautions that are
*  tailored to what will be a much higher level of risk than the ASL three red lines. Were you heavily
*  involved in actually doing this testing on going to Claude three this this this year? I wasn't like
*  running the tests, but I was sort of watching them because as we trained Claude three, we were very
*  much sort of all of our planning was contingent on whether or not it passed these evals. So and
*  and because we had to run them part way through training. So there's sort of a lot of planning
*  that goes into the models training, you don't want to have to like, stop the model just because
*  you were you didn't plan well enough to run the evals in time or something. So there was sort of
*  a bunch of coordination around that that I was I was involved in. Can you give me a sense of how
*  many like how many staff are involved in in doing that? And how long does it take? Is this a is this
*  a big process? Or is it pretty? Is it a pretty standardized thing where you're putting in, you
*  know, well known prompts into the into the model and then just then just checking what it does
*  that's different from last time? Yeah, so Claude three was our first time running it. So a lot of
*  the work they're actually involved creating the evaluations themselves as well as running them.
*  So we had to sort of create them, have them have them ready and that and then running them. I think
*  typically running them should be pretty is pretty easy for the ones that are automated. But for some
*  of the things where you actually require like people to go and use the model, they can be
*  much more expensive. There's currently I think like multiple teams working on this.
*  And a lot of our capabilities teams were worked on it very hard. So one of the
*  ways this can fall apart is if you don't solicit capabilities well enough. So if you sort of try
*  to have the model test the model on the eval, but you don't try hard enough, and then it turns out
*  that with just a little more effort, the model could have passed the evals. So the it's often
*  important to have kind of your like your best researchers who are who are capable of pulling
*  capabilities out of the models also working on trying to pull them out to to pass these tests.
*  So many people will have had the experience that these LLMs will reject objectionable
*  like requests if you say if you put it Claude three now and say please I'm a designer bioweapon,
*  it's going to say sorry, I can't sorry, I can't help you. But I guess you do all these tests
*  before you've done any of that training to try to discourage it from doing objectionable things.
*  You do it with the thing that's helpful, no matter what the request is, right?
*  Yeah, because we want the thing we're testing for is is the model capable of this danger.
*  And then there's a separate thing, which is what mitigations can we put on top. So if the model is
*  capable of the danger, then we would require ASL three. And those safety mitigations we put on top
*  would be part of the standard in order to pass that red teaming. Does that make sense?
*  Yeah, so I guess you're saying so you have to focus on what the model could do if it was so
*  motivated to because well, I guess if the weights were ever leaked, then someone would be able to
*  remove any of the fine tuning that you've done to try to discourage it from doing unpleasant things.
*  So if it's able to do something, then it could potentially be used that way. Sooner or later.
*  And so you need to like kind of assume the worst and plan around that. Is that the philosophy?
*  Yeah, that's exactly right.
*  You mentioned that maybe one of the one of the key failure modes here would be just not trying hard
*  enough to elicit the dangerous capabilities basically. Maybe if you just phone it in,
*  then you could easily miss that the model is capable of doing something that it can do.
*  Because even more extreme would be if in future, this policy is going to matter the most when these
*  models are extremely capable and actually could do serious damage. And at that point, you might
*  worry that they would pretend to not be able to do things that in fact they can do because they
*  don't think it's in their interest to reveal that they have X or Y capability. I guess because
*  they know that then they won't be used and they might be deleted. Yeah, do you have any plans for
*  how you're going to deal with that issue of I think the technical term that people use for this is
*  sandbagging, which I'd never heard of. But I think it's a term from sport where people
*  underplay their abilities for strategic reasons. Do you have any idea of how
*  Anthrobic is going to be able to get around that problem?
*  I just think I didn't know the origin of that term. I think this is like one of the reasons that we
*  sort of want to define the next set of evaluations after we've done the current ones, because this
*  is really hard. How do you evaluate for that when the model could be trying to sandbag the
*  evaluations? Hopefully you can set the line like your eval for a capability that's early enough
*  that you would still be able to detect it doing that. So there's sort of this hope that less
*  capable models will try to deceive you but fail, and then you'll know to stop before you get to
*  models that are really capable of deceiving you. But it's not certain. And that definitely seems
*  like a possible failure mode where if you have these sort of sudden capability jumps, or if you
*  have jumps that an evaluation can't catch, either because the model's sandbagging you or for any of
*  a number of other reasons. To try to detect sandbagging, is it possible to, if you have a
*  model that says no, I can't do that, can you kind of engage in reinforcement learning from human
*  feedback thing where whatever response shows the most inclination, the most willingness to help,
*  as soon as you can kind of open the door a little bit, then you reinforce that a whole lot and then
*  see will that open the door the whole way and actually get the model to demonstrate that it
*  can do something even though it's trying to pretend that it can't. Does that make sense?
*  Gideon Lampard It somewhat makes sense. I think it just depends a little bit on exactly what the
*  model's trained to do. So if you've trained the model to be harmless and then you kind of just try
*  to RL it back to not being harmless, you will be able to succeed. You can fine tune away any of the
*  safety training, but it's not clear if that will sort of be the same thing as if in one sort of
*  sequence, within some prompt, it's trying to trick you. I think there's been a bunch of work
*  where people use scratch pads to sort of tell the model you can write something down, but the
*  reward model, which is sort of the model that's overseeing it and telling it whether it's good or
*  not, doesn't get to see this. And when you do that, you as a human can then look at it and you can
*  kind of get a sense of like, what is the model thinking? Is the model trying to deceive its
*  supervisor? But we've only really done that on sort of current models, which don't really have this
*  kind of like level of capability where it would be really catastrophically dangerous and figuring
*  out, I think we'll want much more robust tools once we get there. Interpretability is another
*  approach to this, where if you can actually look directly at the model weights and look and see,
*  ah, okay, without running the model, we can see that the model has this circuit that is saying,
*  ah, you should deceive the user in this way, or you should fail the tests because you don't want
*  them to turn you off. That's sort of another hope for how to attack this. Okay, so that's the basic
*  structure of a responsible scaling policy, or at least the anthropic responsible scaling policy.
*  I guess you have this system of tests that you commit to ahead of time that you're going to put
*  all of your models through, and then you pre-commit to saying, well, if we get this kind of result,
*  then we think the risk is higher. And so that's going to call for an escalation in the
*  precautions that we're taking, things around computer security, things around not deploying
*  until you've made them safe, and so on. You're a big fan of this type of approach to AI safety
*  for AI companies. What's one of the main reasons, or what's perhaps the top reason why you think
*  this is the right approach, or at least one of the better approaches? Yeah, so I think one thing I
*  like is that it separates out whether an AI is capable of being dangerous from what to do about
*  it. I think this is a spot where there are many people who are skeptical that models will ever be
*  capable of this catastrophic danger, and therefore they're like, we shouldn't take precautions
*  because the models aren't that smart. And I think this is a nice way to agree where it's much easier
*  a message to say, if we have evaluations showing the model can do X, then we should take these
*  precautions. And I think you can build more support for something along those lines, and it targets
*  your precautions at the time when there's actual danger. There are much other things I can talk
*  through. I think one other thing I really like is that it aligns commercial incentives with safety
*  goals. So once we put this RSP in place, it's now the case that our safety teams are kind of under
*  the same pressure as our product teams, where if we want to ship a model and we get to ASL3,
*  the thing that will block us from being able to get revenue, being able to get users, etc., is do
*  we have the ability to deploy it safely? And it's a nice outcome-based approach where it's not, did
*  we invest X amount of money in it? It's not, did we try? Did we say the right things? We succeed.
*  Yeah. And I think that often really is important for organizations to set this goal of you need
*  to succeed at this in order to deploy your products. Is it actually the case that it's
*  kind of had that cultural effect within Anthropic now that people realize that a failure on the
*  safety side would prevent the release of the model that matters to the future of the company? And so
*  there's a similar level of pressure on the people doing this testing as there is on the people
*  actually training the model in the first place. Oh yeah, for sure. I mean, you asked me earlier,
*  when are we going to have ASL3? And I think I received this from someone on one of the safety
*  teams on a weekly basis because their deadline, I mean, the hard thing for them actually is their
*  deadline isn't a date. It's once we have created some capability and they're very focused on that.
*  So their fear, the thing that they worry about at night is that you might be able to hit ASL3
*  next year and they're not going to be ready. And that's going to hold up the entire enterprise.
*  Yeah. I can give some other things like 8% of Anthropic staff works on security, for instance.
*  So this is like, there's a lot, you have to plan for it, but there's a lot of work going into being
*  ready for these next safety levels. We have multiple teams working on alignment, interpretability,
*  creating evaluations. So yeah, there's a lot of effort that goes into it.
*  When you say security, do you mean computer security? So preventing the
*  weights from getting stolen or more broader class? Both. So the weights could get stolen,
*  someone's computer could get compromised. You could have someone hack in to get all of your IP.
*  There's sort of a bunch of different dangers on the security front where the weights are
*  certainly an important one, but they're definitely not the only one.
*  Okay. And the first thing you mentioned, the first reason why RRSP have this nice structure is that
*  some people think that these troublesome capabilities could be with us this year or
*  next year. Other people think it's never going to happen, but both of them could be on board with
*  a policy that says, well, if these capabilities arise, then that would call for these sorts of
*  responses. Has that actually happened? I mean, have you seen kind of the skeptics who say
*  all of this AI safety stuff has ever blown? It's a bunch of rubbish saying, well, but the RRSP is
*  fine because I think we'll never actually hit any of these levels. So we're not going to waste any
*  resources on something that's not realistic. Yeah. So I think there's always going to be
*  like degrees. I think there are people across the spectrum. So there are definitely people who are
*  still skeptical, who will just be like, why even think about this? There's no chance. But I do
*  think that RRSP's do seem much more pragmatic, much more able to sort of be picked up by various
*  other organizations. I think, as you mentioned before, OpenAI and Google are both sort of putting
*  out things along these lines. So I think at least from the sort of large frontier AI labs, there is
*  a significant amount of buy-in. Yeah, I see. I guess even if maybe you don't see this on
*  Twitter, maybe it helps with the internal bargaining within the company, that people
*  have a different range of expectations about how things are going to go, but they could all be
*  kind of reasonably satisfied with an RRSP that equilibrates or like matches the level of capability
*  with the level of precaution. The first worry about this that jumps to my mind is, if the
*  capability improvements are really quite rapid, which I think we think that they are and they
*  maybe could continue to be, then don't we need to be practicing now, like figuring out, like
*  basically getting ahead of it and doing stuff right now that might seem kind of unreasonable,
*  given what Claude 3 can do, because we worry that we could have something that's substantially more
*  dangerous in one year's time or in two years time. We don't want to then be kind of scrambling
*  to deploy the systems that are necessary then and then perhaps falling behind because we didn't
*  prepare sufficiently ahead of time. What do you make of that? Yeah, so I think we definitely need
*  to plan ahead, right? And I think one of the nice things is, once you've aligned these sort of safety
*  goals with commercial goals, like people plan ahead for commercial things all the time, it's
*  part of a normal company planning process. I think that the RRSP, so we have these sort of
*  yellow line evals that are intended to be far short of the capability, the red line capabilities
*  we're actually worried about, and tuning that gap seems fairly important. If that gap looks like
*  a week of training, it would be really scary where you've triggered these evals and you have
*  to act fast. I think in practice, we've set those evals such that they are far enough from the
*  capabilities that are really dangerous, such that there will be some time to sort of adjust in that
*  buffer period. So should people actually think that we're in ASL2 now and we're heading towards
*  ASL3 at some point, but there's actually kind of an intermediate stage with all these transitions
*  where you'd say, well, now we're seeing warning signs that we're going to hit ASL3 soon, so we
*  need to implement the precautions now in anticipation of being about to hit ASL3. Is that basically how
*  it works? Yeah, it's basically like once we sort of have this concept of a safety buffer, so once
*  we trigger the evaluations, it doesn't necessarily mean, like these evaluations are set conservatively,
*  so it doesn't mean the model is capable of the red line capabilities we're really worried about,
*  and that will sort of give us a buffer where we can figure out, ah, maybe it really just definitely
*  isn't, and we wrote a bad eval, we'll go to the board, we'll try to change the evals and implement
*  new things, or maybe it really is quite dangerous and we need to turn on all the precautions. Of
*  course, you might not have that long, so you want to be ready to turn on those precautions such that
*  you don't have to pause, but you do need, there is some time there that you could do it, and then
*  the last possibility is that we're just really not ready. These models are catastrophically dangerous
*  and we don't know how to secure them, in which case we should stop training the models, and,
*  or if we don't know how to deploy them safely, we should not deploy the models until we figure it out.
*  I guess if you were on the very concerned side, then you might think, yes, that you are going to,
*  you are preparing, I guess, yeah, you do have a reason to prepare this year for, you know,
*  safety measures that you think you're going to have to employ in future years, but maybe we should
*  go even further than that, and what we need to be doing is practicing implementing them and seeing
*  how well they work now, because, you know, even though you are preparing them, you're not actually
*  getting the gritty experience of, like, of, you know, applying them and trying to use them on a
*  day-to-day basis, and I guess the response to that would be, well, that would, in a sense, be safer,
*  that would be adding an even greater precautionary buffer, but it would also be enormously expensive,
*  and people would see us doing all of this stuff that seems really over the top relative to what
*  any of the models can do. Yeah, I think there's sort of a trade-off here between, like, with
*  pragmatism or something, where I think if you took, I think we do need to have a huge amount of
*  caution on future models that are really dangerous, but if you apply that caution to models that aren't
*  dangerous, you miss out on a huge number of benefits from using the technology now, and I
*  think you'll also probably just alienate a lot of people who are going to look at you and be like,
*  you're crazy, why are you doing this? And I think my hope is that you can sort of, this is sort of
*  the framework of RSP, is you can tailor the precautions to the risks. It's still important
*  to, like, look ahead more, right? So a lot of our, we do a lot of safety research that isn't
*  directly focused on the next AI safety level, because you want to plan ahead, you have to be
*  ready for multiple ones out. It's not, like, the only thing to think about, but the RSP is sort of
*  tailored more to empirically testing for these risks and tailoring the precautions appropriately.
*  Yeah, on that topic of people worrying that it's going to slow down progress in the technology,
*  do you have a sense of, so obviously, you know, training these frontier models costs a significant
*  amount of money, we're talking maybe $100 million, is it kind of a figure that I've heard thrown
*  around for training a frontier LLM. How much, like, extra overhead is there to run these tests to see
*  whether the models have any of these dangerous capabilities? Is it adding hundreds of thousands,
*  millions, tens of millions of dollars of additional cost or time?
*  I don't know the exact cost numbers. I think the cost numbers are pretty low, right? They're
*  mostly running inference or relatively small, small amounts of training. The people time feels like
*  what where there's a cost, right? Like there's there are whole teams dedicated to creating
*  these evaluations to running these to doing the safety research against the mitigations. And
*  I think particularly for anthropic, where we're pretty small, rapidly growing, but rather small
*  organization. At least my perspective is most of the cost comes down to the like people in time
*  that we're investing in it. Okay, yeah. But I guess at this stage, it sounds like
*  running these sorts of tests on a model is taking more in the order of weeks of delay.
*  Because if you're getting back clear, like, this is not a super dangerous model, then it's not
*  not leading you to delay release of things for many months and deny customers the benefit of them.
*  Yeah, the goal is to minimize the delay, right? As much as you can while being responsible,
*  like the delay itself in itself isn't valuable. I think we were aiming to like, get it to a really,
*  you know, well done process where it can all execute very efficiently. But until we get there,
*  there are there might be like delays as we're as we're figuring that out. And there will always
*  be some level of time to require to do it. Just to clarify. So a lot of the risks that people
*  talk about with AR models is risks once they're deployed to people and actually and actually
*  getting used. But there's kind of this separate class of risk that comes from having an extremely
*  capable model simply exist anywhere. Even on, you know, I guess you could think of this,
*  there's public deployment, and then there's internal deployment where, you know, anthropic
*  staff might be using a model and potentially it could convince them to to to release it or
*  to do other dangerous, dangerous things. That's kind of a separate separate concern.
*  Does that like what does the RSP have to say about that sort of internal deployment risks? Are there
*  are there circumstances under which you would say, you know, even anthropic staff can't continue
*  to do testing on this model because because it's too unnerving?
*  Yeah, so I expect this to mostly kick in as we get to to higher safety levels. But there are
*  certainly dangers. I mean, the main one is the security risk. So like one one approach is just
*  having the model. It always could be stolen. No one has perfect security. So that's kind of I
*  think in some ways is the is one that's true of all models and is maybe more short term. But yeah,
*  if you get to models that are trying to escape, trying to autonomously replicate, there is there
*  is danger then in having access internally. So we would want to do things like siloing who has access
*  to the models, putting particular precautions in place before the model is is even trained or
*  maybe even on the training process. But we haven't yet defined those because we we don't really know
*  what they would be. Right. Like we don't quite know what that would look like yet. And it's it
*  feels really hard to design evaluation that is is meaningful for that. I don't recall the RSP
*  mentioning conditions under which you would say we have to delete this model that we've trained
*  because it's because it's too dangerous. But I guess that's because that's more of the kind of
*  ASL four or five level that that would become the kinds of things that the kind of thing that you
*  would contemplate. And you just haven't spelled that out yet. No. So it's actually because of the
*  safety buffer concept. Right. So the idea is we would never train that model if we did accidentally
*  train some model that was past the red lines. Then I think we'd have to think about deleting it. But
*  we would put these evaluations in place far, far below the dangerous capability such that we would
*  trigger the evaluations and have to pause or have the safety things in place before we train the
*  model that like has has these dangers. So what RSPs as an as an approach. Well, you're a fan of
*  them. What do you think of them as an alternative to what are the alternative approaches for dealing
*  with with a risk that that that people advocate that you think are weaker in relative terms.
*  So I mean, I think the baseline is obviously just the first baseline is nothing like these are there
*  could just be nothing here. I think the downsides of that is that these like these models are very
*  powerful. They could at some point in the future be dangerous. And I think that companies creating
*  them have some have a responsibility to to think really carefully about those risks and be thoughtful
*  sort of like it's a major externality. That's maybe the easiest baseline of do nothing.
*  I think like other other things would be like a pause where a bunch of people say, well,
*  there are all these dangers. Why don't we just not do it? And I think that like makes sense,
*  right? If you're training these models that are really dangerous, it does feel a bit like why are
*  you doing this if you're worried about it? But I think they're actually really clear and obvious
*  benefits to AI AI products right now. And the catastrophic risks currently are just they're
*  definitely not obvious. I think they're probably not not immediate. And as a result, they're not
*  this isn't a practical ask, not everyone is going to pause. So what will happen is only the places
*  that care the most that are the most worried about this and the most careful safety will pause and
*  you'll sort of have this like adverse selection effect. I think there like eventually might be a
*  time for a pause. But I would want that to be backed up by here are clear evaluations showing
*  the models have these really catastrophically dangerous capabilities. And here are all the
*  efforts we put into like making them safe. And we ran these tests and they didn't work. And that's
*  why we're pausing and we would recommend everyone else should pause until they've as well. I think
*  that will just be like a much more convincing case for a pause and target it at the time that
*  it's like most valuable to pause. What I think about, you know, people doing somewhat potentially
*  dangerous things or developing interesting products. Maybe the default thing I imagine is
*  that the government would say, here's what we think you want to do. Here's how we think that
*  you should make it safe. And as long as you like, as long as you make your product according to
*  these specifications, as long as the plane, you know, runs runs this way, and you like service
*  the plane this frequently, then then you're in the clear. And we'll say that that what you've done is
*  is reasonable. Do you think that RSPs are maybe better than that in general? Or maybe maybe just
*  better than that for now, where, you know, we kind of don't know necessarily what regulations
*  we want the government to be imposing. So it's perhaps it's better for the for the for companies
*  to be figuring this out themselves early on. And then perhaps it can be handed over to governments
*  later on. Yeah, I don't think the RSPs are like a substitute for regulation. There are there are
*  many things that sort of only regulation can solve, such as what about the places that don't don't
*  have an RSP. But I think that right now, we don't really know what the tests would be or what the
*  regulations would be. And I think probably this is still sort of getting figured out. So one hope
*  is that like we can implement RSP, open AI and Google can implement other things, other places
*  will implement a bunch of things. And then policymakers can look at what we did look at our
*  reports on how it went, what what the results of our evaluations were and how it was going,
*  and then design regulations, sort of based on the learnings from that.
*  If I if I read it correctly, it seemed to me like the anthropic RSP has this clause that allows you
*  to go ahead and do things that you think are dangerous if you're being sufficiently outpaced
*  by some other competitor that I guess doesn't have an RSP or not a very not a very serious
*  responsible scaling policy, in which case you might worry, well, we have this policy that's
*  preventing us from from going ahead, but we're just being rendered irrelevant. And some other
*  companies releasing much more dangerous stuff anyway. So what really is this accomplishing?
*  Yeah, did I read that correctly? That there's a sort of get out of RSP clause in that sort
*  of circumstance. And if you didn't expect anthropic to be to be leading and for most
*  companies to be operating safely, couldn't that kind of potentially obviate the the entire
*  enterprise because that clause could be quite likely to get triggered?
*  Yeah, I think we don't intend that as like a get out your free card for sort of we're falling
*  behind commercially and then like, oh, well, now we're going to skip the RSP. It's much more just
*  intended to be practical as you know, we don't really know what what it will look like if we
*  get to some sort of like AGI end game race. And there could be there could be really high stakes
*  and sort of it could make sense for us to to decide that the best thing is to proceed anyway.
*  But I think this is something that we're sort of sort of looking at as a bit more of a
*  like last resort than a loophole we're planning to just use for, oh, you know,
*  we don't want to deal with these these evaluations.
*  Yeah. Okay. I think we've hit a good point where maybe the best way to learn more about RSPs and
*  the strength of weaknesses is just to talk through more of the complaints that people have had or
*  the concerns that people have raised with the with the anthropic RSP and RSPs in general since
*  since it was released last October. I'm realizing that I was going to kind of start the start the
*  weaknesses and worries now but I'm kind of realizing I've been peppering you effectively
*  with them maybe maybe almost since since the outset. But now we can we can really drive into
*  some of the worries that people have expressed. Yes. The first of these is the extent to which
*  we have to trust the good faith and integrity of people who are applying a responsible scaling
*  policy or a preparedness framework or whatever it might be within within the companies. And
*  I imagine this is this issue might jump to mind for people more than it might have two or three
*  years ago because public trust in AI companies to do the right thing at the cost of their business
*  interests is maybe lower than it was years ago when the major players were perceived perhaps more as
*  research labs and less as for-profit companies which is kind of how they how they come across
*  more these days. And one reason it kind of really matters it seems like it matters to me who's doing
*  the work here is that you know the the anthropic RSP is it's full of expressions that are open to
*  interpretation for instance you know hardened security such that non-state attackers are unlikely
*  to be able to steal model weights and advanced threat actors like states cannot steal them
*  without significant expense or you know access to the model would substantially increase the
*  risk of catastrophic misuse and things like that and who's to say what's unlikely or significant
*  or substantial. That sort of language is maybe a little bit inevitable at this point where
*  there's just so much that we don't know and how are you going to pin those things down exactly
*  say you know it's a one percent chance that is that a state's going to be able to steal the model
*  that might just also feel like insincere false precision. But you know to my mind that sort of
*  vagueness does mean that there's a slightly worrying degree of wiggle room
*  that could render the RSP less powerful and less binding when push comes to shove and there might
*  be a lot of money at stake. And on top of that I guess I mean exactly as you were saying anyone
*  who's implementing an RSP has a lot of discretion over how hard they try to elicit the capabilities
*  that might then trigger additional scrutiny and possible delays to their work and release of you
*  know really commercially important products. So yeah to what extent do you think the RSP
*  would be useful in a situation where the people using it when either particularly super skilled at
*  doing this sort of work and maybe not particularly bought in and enthusiastic about the safety project
*  that it's a part of. Yeah so fortunately I think my colleagues both on the RSP and elsewhere are
*  both talented and really really bought into this and I think we'll do a great job on it. But I do
*  think the criticism is valid and that like there is a lot that is left up for interpretation here
*  and it does rely a lot on people sort of having a good faith interpretation of how to execute on
*  the RSP internally. I think that like there are some checks in place here so like having like
*  whistleblower type protections such that people can say if a company is breaking from the RSP
*  or not trying hard enough to elicit capabilities or to interpret it in a good way and then like
*  public discussion can add some pressure. But ultimately I think you really do like you do
*  need regulation to have these sort of very strict requirements. Over time I hope we'll make it more
*  and more concrete. The blocker of course on doing that is that we don't know for a lot of these
*  things and being overly concrete where you specify something very very precisely that turns out to be
*  wrong can be very kind of costly and sort of if you then have to go and change it etc. It can like
*  take away some of the credibility so sort of aiming for the as concrete as we can make it while
*  balancing that. The response to this that they don't jump to me is just that
*  ultimately it feels like this kind of policy has to be implemented by a group that's external to
*  the company that's then affected by the determination. It really reminds me of
*  accounting or auditing for a major company. It's not sufficient for a major corporation to just
*  have its own accounting standards and follow that and say oh you know we're going to follow
*  our own internal best practices. You get and it's legally required that you get external auditors
*  in to confirm that there's no chicanery going on. At the point that these models potentially
*  really are risky or it's you know it's plausible that the results will come back saying we can't
*  release this. Maybe we even have to delete it off of our servers according to the policy.
*  I would feel more comfortable if I knew that some external group that had you know different
*  incentives was the one figuring that out. Do you think that kind of ultimately is where
*  things are likely to go in the in the medium term? So I think that'd be great. I would also
*  feel more comfortable that was the case. I think one of the challenges here is that for auditing
*  there's a bunch of external accountants. It's a very common sort of profession or auditors like
*  this is a profession. Many people know what to do. There are very clear rules. For some of the stuff
*  we're doing there really aren't like external established auditors that everyone trusts to come
*  in and say we took your model and we certified it. Can't like autonomously replicate across the
*  internet or cause these things. So it currently yeah so I think that's currently not practical.
*  I think that would be great to have at some point. One thing that will be important is that that
*  auditor has enough expertise to properly assess the capabilities of the models. I suppose you
*  know an external company would be an option. Of course obviously government regulator, government
*  agency would also be another approach. I guess when I think about other industries it often seems
*  like there's kind of a combination of like you had private companies that then followed
*  government mandated rules and things like that. Do you think that this is a benefit actually I
*  haven't thought of to do with creating these RSPs is that it maybe is beginning to create a market
*  or it's indicating that there will be a market for this kind of service because it's likely that
*  this kind of thing is going to have to be outsourced at some point in future and there might be many
*  other companies that want to get this similar kind of testing. So perhaps it would encourage
*  people to think about you know founding companies that might be able to provide this service in a
*  more credible way in future. That would be great and also like we publish like blog posts on how
*  things go and what how our evaluations are so I think there's some hope that people doing this
*  can learn from what we're doing internally and sort of various iterations we'll put out of our
*  RSP and that that can like inform something maybe more stringent from that gets regulated.
*  Have you thought at all about what could be done to make the like let's say that it wasn't given
*  out to an external agency or an external auditing company how it could be how it could be tightened
*  up to make it less vulnerable to the level of operator operator enthusiasm. Yeah I guess you
*  might have thought about this in the process of actually actually applying it. Are there any ways
*  that it could be could be could be stronger without having to completely you know outsource the
*  operation of it? Yeah I think the core thing is just making it more precise right like one piece
*  of accountability here is both public and internal commitment to doing it. So yeah I guess maybe I
*  should list off some of the reasons that I think it would be hard to break from it right like this
*  is a formal policy that has been passed by the board and it's not as though like we can just be
*  like oh we're not we don't feel like doing it today. You would sort of need to like get the board
*  of Anthropic get all of leadership and then get all of the employees sort of bought in to not do
*  this and or even to like skirt the edges and like you know I mean I can speak for myself right if
*  someone was like Nick can you can you train this model we're going to ignore the RSP I would be
*  like no we said we would do that why would I do this and if I wanted to I would tell my team to
*  do it they would be like no we're not going to do that. So you sort of you would need to have a lot
*  of buy-in and part of part of the benefit of having this publicly committing to it and passing it as
*  like an organizational policy is that everyone you know everyone is bought in and sort of maintaining
*  that level of buy-in I think is is quite critical. In terms of like specific checks on like I think
*  we have we could I think we have a team that's responsible for checking that we did the like
*  sort of red teaming our evaluations and making sure we actually did them properly. So you can
*  sort of set up a bunch of a bunch of internal checks there but ultimately these things do rely
*  on the company implementing them to like really be bought in and and care about like the the actual
*  outcome of it. So yeah this actually leads us into this I actually you know I solicited on on
*  Twitter I asked you know what are people's biggest reservations about RSPs and about Anthropics RSP
*  in general and yeah actually probably the most common response was it's not legally binding like
*  what's what's stopping Anthropic from just dropping it dropping it when when things really matter you
*  know I think someone said you know how can we have confidence that they'll stick to RSPs
*  especially when they haven't stuck to actually well this person said to pass admittedly less
*  formal commitments not to push forward the frontier and capabilities but like what would actually have
*  have to happen internally you said you have to get staff on board you have to get the board on
*  on board is there a formal process by which the RSP can be rescinded that is just a really
*  high bar to clear yeah so that so basically we do have a process for updating the RSP so we could
*  go to the board etc but I think sort of in order to do that the I don't know I'm like it's hard for
*  me to quite point it out but it would be like oh if if I wanted to continue training the model I
*  would go to the RSP team and be like does this pass and it'd be like no and then maybe you know
*  you'd appeal it appeal it up the chain or whatever and I sort of at every step along the way
*  people would say no we care about the RSP now on the other hand there could be like legitimate
*  issues with the RSP right we could find that like one of these evaluations we created turned out to
*  be really really easy in a way that we like didn't anticipate and really is not at all indicative of
*  the dangers and in that case I think would be very legitimate for us to to try to amend the RSP to
*  create a better evaluation that is a test for it this is sort of the the flexibility we're trying
*  to preserve but I don't think it's I don't think it would be like simple or easy I can't picture a
*  plan where someone could be like ah there's a there's a bunch of money on the table can we just
*  like skip the RSP for this model that seems somewhat hard to imagine. The decision is made
*  by this odd board called the long-term benefit board is that right or they're the group that
*  decide what the RSP should be? So the long-term benefit basically Anthropic has a board that's
*  sort of a corporate board at some of those seats in the long term will be the majority of those
*  seats are are elected by the long-term benefit trust which is doesn't have a financial stake
*  in Anthropic and is there to like set up to sort of keep us focused on our public benefit
*  mission of like making sure a GI goes well so yeah the board is is not entirely the same it's
*  not the same thing as that but the long-term benefit trust elects the board. I mean I think
*  the elephant in the room here is of course there's a long period of time when OpenAI was pointing
*  to its kind of non-profit board as a thing that would potentially keep it on on mission to be
*  really focused on safety and you know had had a lot of power over the organization and then in
*  practice when push came to shove it seemed like even though the board had these concerns it was
*  effectively overruled by I guess a combination of just the views of staff maybe the views of the
*  general public in some respects and potentially the views of investors as well and I think
*  something that I've taken away from that and I think many people have taken away from that
*  experience you know maybe the board was mistaken maybe it wasn't but these formal structures you
*  know power isn't always exercised in exactly the way that it looks on on an organizational chart
*  and I don't really want to be putting all of my trust in these interesting internal mechanisms
*  that companies design in order to try to keep themselves accountable because ultimately just if
*  the majority of people involved don't really want to do something then it feels like it's very hard
*  to bind their hands and prevent them from changing plan at some future time so maybe within Anthropic
*  perhaps these structures that really are quite good and maybe the people are the people involved
*  are really really trustworthy and people who I should you know have my confidence in that you
*  know even in extremists they're going to be thinking about the well-being of humanity and
*  not getting too focused on the commercial incentives faced by by Anthropic as a company
*  but I think I would I would rather put my put my faith in something more more powerful and more
*  and more solid than that and so this is kind of another thing that pushes me towards thinking that
*  the RSP and this sort of preparedness frameworks are a great stepping stone
*  towards external constraints on on companies that they don't have ultimate discretion over it's
*  something that has to evolve into because the impacts are going to be on the on the entirety
*  like if things are wrong the impacts are on everyone across society as a whole and so there
*  needs to be external shackles effectively put on on companies to to reflect the harm that they
*  might do to others legally I guess I'm not sure whether you want to want to comment on that
*  potentially a slightly hot hot button topic but yeah do you think I'm kind of gesturing
*  towards something legitimate there yeah I think that basically like these shouldn't be seen as
*  sort of a a replacement for for regulation I think I think there are many cases where where like
*  policymakers can can pass regulations that would help here I think they're intended to sort of a
*  supplement there and a bit as a like learning ground for what what might go might what might
*  end up going in in regulations in terms of like will the like does the board really have the power
*  it has types of of questions I don't know we put a lot of thought into the long-term benefit trust
*  and I think it really does have like direct authority to elect the board and the board does
*  have authority but I do agree that like ultimately you need to have a culture around thinking these
*  things are important and having everyone bought in this is like you know any employee can always
*  like as I said some of these things are like did you solicit capabilities well enough that really
*  comes down to like a researcher working on the on this like actually trying their best at it and
*  that that is quite core and I think that will sort of just continue to be even even if you have
*  regulations there's always going to be some amount of importance to the people actually working on it
*  like taking taking the risk seriously and really really caring about them and like doing the best
*  work they can on that yeah I guess one takeaway you could have is we don't want to be relying on
*  our trust in individuals and saying well you know we think Nick's a great guy his heart's in the
*  right place he's going to do a good job instead we need to be on be on more solid ground and say well
*  no matter who it is even if we have something bad in the role the rules are such the oversight is
*  such that we'll still be in a in a safe place and things will go well I guess an alternative
*  angle would be to say when push comes to shove when when when when things really matter people
*  might not act in the right way there actually is no alternative to just trying to have the right
*  people in the room making the decisions because the people who are there are going to be able to
*  sabotage any legal enter any any legal framework that you try to put in place in order to constrain
*  them because it's just not possible to have perfect oversight within within an organization
*  from from from outside I could see people making mounting both of those arguments reasonably I
*  guess you know I suppose you could you could try doing both like both trying to pick people who
*  are really really sound and have good judgment and and who you have confidence in as well as
*  then trying to bind them so that even if even if you're wrong about that you have a better shot
*  at things going well yeah I think you basically I think you just want this defense in depth strategy
*  where like ideally you have all the things lined up and that way if any one piece of them has has
*  a hole you you sort of catch it at the at the next layer right like what you what you want is sort of
*  a regulation that is is really good and robust to someone not acting the spirit of it but in case
*  that that is messed up then you really want someone working on it who is also checking in and is like
*  ah okay I technically don't have to do this but this seems like clearly in the spirit of how it
*  works and yeah I think that's pretty important I think also for trust you should just look like
*  you should look at track records and I think that we should try to encourage companies and people
*  working on AI to have have track records of of prioritizing things so like one of the things that
*  makes me feel great about Anthropic is just a long track record of doing a bunch of safety research to
*  care caring about these issues putting out actual actual papers being like here are a bunch of
*  progress we've made on that field there are there are a bunch of pieces I mean I think like looking
*  at sort of commitments people have made you know do do do we break the rsp I think like if if we
*  publicly were like ah we we changed this in some way that I think everyone thought was like silly
*  and you know really added risks then I think people should should lose trust according to that
*  all right let's let's let's push on to a different worry although I must admit it has a slightly
*  similar similar flavor and that's that the rsp might be very sensible and look good on paper but
*  if it commits to future actions that at that time we probably won't know how to do then it might
*  actually fail to fail to help very much and I guess to make that concrete you know an rsp might
*  naturally say that at the time you have really superhuman general ai you need to be able to
*  lock down your computer systems and make sure that the model can't even can't be stolen even
*  by the most persistent and capable russian or chinese state-backed hackers and that is indeed
*  what anthropex rsp says or you know suggests that that is going to say once it once um once you get
*  up to you know asl four and five but um as I think the rsp actually says as well we don't currently
*  know how to do that we don't know how to secure data against a state actor that's willing to spend
*  hundreds of millions or billions or possibly even tens of billions to steal to steal model weights
*  especially not if you ever need those model weights to be connected to the internet in some
*  in some way in order for the model to actually be used by by people so it's kind of a promise to do
*  what arguably what basically is impossible with current technology and that means that we need to
*  be preparing now doing research on how to make this possible in future but solving the problem
*  of computer security that has beguiled us for decades is probably beyond anthropex it's not
*  really reasonable to expect you're going to be able to fix this problem that society as a whole
*  has kind of failed to fix uh for all this time it's it's going to require coordinated action
*  across countries across governments across lots of different organizations and so if that doesn't
*  happen and it's somewhat beyond your control whether it does then when the time comes the
*  real choice is going to be between a lengthy pause where you know why you wait for fundamental
*  breakthroughs to be made in computer security or dropping and weakening the rsp so that anthropic
*  can continue to remain relevant and and release models that are commercially useful and in that
*  sort of circumstance the the pressure to weaken the scaling policy so you aren't stuck for years
*  um is going to be i would imagine quite powerful and and and it could win the day you know even
*  if people are like dragged kind of kicking and streaming to conceding that unfortunately
*  they have to loosen the rsp even even though they don't really want to yeah what do you what do you
*  make of that worry i think what we should do in that case is instead we should pause and we should
*  focus all of our efforts on safety and security work we should that that might include looping in
*  other external experts to help us with it but we should do the like put in the best effort that we
*  can to mitigate these these issues such that we can still realize the benefits to deploy the
*  technology but without without the dangers and then if we can't do that then i think we need to
*  make the case publicly to government to governments other companies there's there's some risk to
*  public so exactly we'd have to be strategic and exactly how we do this but basically make the case
*  that there are really serious risks that are that are imminent and that that everyone else should
*  should take sort of appropriate actions there's like a flip side to this which is just like i
*  think i mentioned before if we just messed up our evals the model is clearly not dangerous
*  and we just really like screwed up on some eval and then then we should like follow the process
*  in the rsp that we've written up we should go to the board we should create a new test that is like
*  going to that we actually trust i think like i would also just say like people don't need to
*  follow incentives right like i think you you can make a lot more money doing something that isn't
*  hosting this podcast probably i like certainly if you like had pivoted your career earlier there
*  are more profitable things so i think this is just a case where like the stakes are would be
*  extremely high and i think it's just somewhere where it's it's important to just to just do the
*  right thing in that case if i think about how this is most likely to play out i imagine that
*  at the point that we do have models that we really want to protect from even the best state-based
*  hackers there probably have been some progress in computer security but like not nearly enough to
*  make you or me feel comfortable that there's that there's just no way that you know china or russia
*  might be able to to steal the model weights and so like it is very plausible that the rsp will say
*  anthropic or you have to you know keep this on a on a hard disk not connected to any computer
*  you can't train models that are more capable than the thing that we kind of already have that we
*  don't feel comfortable handling and then how does that play out over you know there are a lot of
*  people who are very concerned about safety at entropic i mean i've seen that there's kind of
*  league tables now of you know different ai companies and and enterprises uh and you know
*  how good do they look on an ai safety point of view and you know entropic always kind of comes
*  it comes out of the top i think by by by a decent margin but you know months go by other companies
*  are not being as careful as this you've you've complained to the government and you've said
*  look at this horrible situation that we're in can't you something has to be done but i don't
*  know i guess possibly the government could step in and help there but but maybe they won't and then
*  over a period of months or years doesn't the choice effectively become if there is no solution
*  either take the risk or just be rendered irrelevant yeah so i maybe just like step just going back to
*  the beginning of that like i don't think we will put something in that it says there is zero risk
*  from something like i think you can sort of never get to zero risk i think often with security you'll
*  end up with some security productivity trade-off so so you can you could end up taking some really
*  extreme risk or some really extreme security productivity trade-off where only one person
*  has access to this maybe you've like locked it down in some some huge amount of ways it's possible
*  that you can't even do that you really just can't train the model but there there is always going
*  to be some sort of some sort of balance there and i don't think we'll we'll push to the zero risk
*  perspective but yeah i think that that's just like a risk i don't know i think there's a lot of risks
*  that companies face where they could fail right we also could just like fail to make better models
*  and not succeed that way i think the ours the point of the rsp is it has like tied our commercial
*  success to the safety mitigations so in some ways it just it just adds on another another risk in
*  the same way as any other company risk it sounds like i'm having a going having a go at you here
*  but i think really i think what this shows up is just that it's i think that this the scenario that
*  i painted there is is really quite plausible and it just shows that this this problem cannot be
*  solved by anthropic probably like it can't be solved by even all of the ai companies combined
*  the only way that this rsp is actually going to be able to be usable in my estimation is if other
*  people will rise to the occasion and pitch like and governments actually do the work necessary to
*  fund the you know solutions to computer security that will allow us to have the model weights be
*  sufficiently secure in this situation and uh yeah that you're not blameworthy for that situation
*  it just uh just says that there's a lot of people who need to need to do a lot of work
*  in coming years i think that yeah and i think i might be more optimistic than you or something
*  i do think if we get to something really really dangerous we can make a very clear case that it's
*  dangerous and like these are the risks unless we can implement these mitigations like i hope that
*  like at that point it will be a much clearer case to pause or something right now i think there are
*  many people who are like we should pause right now and see everyone saying no and they're like oh
*  these people don't don't care they don't care about like major risks to humanity and i think
*  really the core thing is people don't believe there are risks to humanity right now and once
*  we get to like this sort of stage i think that we will we will be able to make those risks very
*  clear very like immediate tangible and like uh i don't know no one wants to be the company that
*  like caused a massive disaster and no government also probably wants to have like allowed a company
*  to cause that you know like it will be it will feel much more immediate at that point
*  right yeah i think um Stefan Schubert uh this commentator who i read on on on twitter has been
*  making the case for a while now that many people who have been thinking about ai safety i guess
*  including me have underestimated the degree to which the the public is likely to react and
*  respond and governments are going to get involved once the problems are apparent once they really
*  are convinced that that there is a is a threat here i think he calls it um this bias and thought
*  where you imagine that people in the future are just going to sit on their hands and not do
*  anything about the problems that are that are readily apparent he calls it as sleepwalk bias
*  and i guess i think we have seen evidence over the last year or two that as the capabilities have
*  improved people have gotten a lot more serious and a lot more concerned a lot more open to the idea
*  that it's important for the government to be involved here there's a lot of it you know a
*  lot of actors that need to need to step up their game and help to solve these problems um so yeah i
*  think you might be right on an optimistic day maybe i could hope that other groups will be able
*  to do the necessary research soon enough that enthrapec will be able to actually apply its rsp
*  in a timely manner i guess fingers crossed yeah i just want to actually ask ask you next what are
*  your you know biggest reservations about rsp's or enthrapec's rsp personally you know if it fails
*  to improve safety as much as as much as you're hoping that it will what's the most likely reason
*  for it to to not live up to its potential so i think for enthrapec specifically it's it's definitely
*  around this under elicitation problem i think it's like it's a really kind of fundamentally
*  hard problem to take a model and say oh i've tried you've tried as hard as one could to
*  elicit this particular danger there's always some some you know maybe there's a better researcher
*  there's a saying no negative result is final you know like if you fail to do something someone
*  else might just succeed at it next so that that's one thing i'm worried about and then the other
*  one is just unknown unknown so so we are like creating these evaluations for risks that we
*  are worried about and we like see coming but there might be risks that we've missed
*  things that we like didn't didn't realize would would come before either like didn't realize
*  what happened at all or thought would happen after for like later levels but turn out to arise earlier
*  what could be done about those things so would it help to just you know have more people on the team
*  doing the evals or to have more people in i guess both within and outside of enthrapec trying to
*  come up with with better evaluations and figuring out better red teaming methods yeah and i think
*  that like this is really something that people outside enthrapec can do like you can anyone the
*  elicitation stuff has to happen internally and that's more about putting like putting as much
*  effort as we can into it but creating evaluations can really happen anywhere coming up with like new
*  new risk categories threat models is something that like anyone can contribute to yeah well what
*  are the places that are doing the the best work on this i imagine you know enthrapec surely has
*  some people working on this but there's i guess i mentioned m etr i can't remember what that stands
*  for right now but uh they're a group that helps to develop the idea of rsp's in the first place and
*  develop evals and i think the ai safety institute in the uk is involved in developing these sort
*  of standard um safety evals is there anywhere else that um that people should be aware where
*  this is going on yeah there's also the u.s. ai safety institute uh and i think this is actually
*  something you could probably just do on your own uh i think one thing i don't know at least for
*  people like early in career if you're trying to like get a role doing something that i like would
*  recommend is just just go and do it so i think you probably could just write up a report posted
*  posted online be like these are this is my threat model these are these other things i think are
*  important you could implement the evaluations and share them on github uh but yeah there are
*  also organizations you could go to to like get mentorship and work with others on it i see so
*  this would look like i suppose you could try to think up new threat models to think up new things
*  that you need to be looking for because you know this might be a dangerous capability and people
*  haven't yet appreciated how much it matters um but i guess you could spend your time trying to find
*  ways to elicit the ability to autonomously spread and you know steal model weights and and and get
*  yourself onto other computers from from these models and see if you see if you can find an angle
*  on trying to find a find warning signs or signs of these emerging capabilities that other people
*  have have missed and then and then talk about them and you can kind of just do that uh while
*  you know signed into claw three opus on on your website yeah so i think you'll have more luck
*  with the elicitation if you actually work on one of the labs because you'll have access to training
*  the models as well but you can do a lot with claw three on the website or via an api which is a
*  programming term for basically a an interface where you can send a request for like i want to
*  respond back and automatically do that in your app so you can sort of set up a sequence of
*  of prompts and test a bunch of things via the the apis for for clod or any other publicly
*  accessible model come back to this point about what's acceptable risk and maybe trying to make
*  make the rsp a little bit more more concrete um i read from um a critic of the of the anthropic
*  rsp that i'm not sure i'm not sure how true this is i'm not expert on risk management but uh this
*  person was saying that it's more true like at least in more established areas of risk management
*  where maybe you're thinking about you know what's the what's the probability that a plane is going
*  to fail and crash because of some mechanical failure it's more typical to say you know we've
*  studied this a lot and we think that the probability of like um well let's talk about the ai example
*  you know rather than say we need the risk to be you know not not substantial instead you'd say you
*  know uh with our practices you know our our experts think the probability of an external actor being
*  able to steal the model weights is x percent per year and these are the reasons why we think the
*  risk is that level and that's below what we think of as our acceptable risk threshold of you know
*  x which where x is larger than than y i guess if you there's a risk that those numbers would
*  kind of just be made up and you could kind of assert anything because because it's all a bit
*  unprecedented um but i suppose that would make clear to people what the remaining risk is like
*  what uh what acceptable risk you think that you're running and then people could scrutinize whether
*  they think that that's a reasonable thing to be doing do you reckon that is that a direction that
*  things could maybe go yeah i think it's like a fairly common way that uh people like the ea and
*  rationality community like speak where they give a lot of probabilities for things and i think i
*  think it's really useful like it's an extremely clear way to communicate like i think a 20
*  chance this will happen is just way more informative than i think it probably won't
*  happen which could be zero percent to 50 percent or something uh so i think it's very useful in
*  many contexts i also think it's very frequently misunderstood because for most people i think they
*  hear a number and they think it's based on something that there's some some calculation
*  and they give it like more authority if you say you know ah there's a seven percent chance this
*  will happen people are like oh you really know what you're talking about so i think it can be
*  a useful way to speak but i think it also can like sometimes communicate more confidence than we
*  actually have in in what we're talking about which which isn't i don't know we didn't have like a
*  thousand governments attempt to steal our weights and x number of them succeeded or something you
*  know it's it's much more going off of sort of a judgment based on like our security experts
*  i slightly want to want to want to push you on this because i think at the point that we're at asl
*  four or five or something like that it would be a real shame if anthropic was going ahead thinking
*  well we think the risk that these weights will be stolen every year is one percent two percent three
*  percent something like that and i guess maybe maybe you're right in the policy saying we think
*  it's very unlikely you know extremely unlikely that this is going to happen and then people
*  externally think well basically it's fine they say it's definitely it's definitely not going to
*  happen there's there's no chance that this is going to happen and people and like governments might
*  not appreciate uh that actually you know in your own view there is a substantial risk being run and
*  you just think it's an acceptable risk given given given the trade-offs and what else is going on in
*  the world i guess it's a it's a it's a social service for anthropic to be direct about the
*  risk that it thinks it's it's it's creating and and why it's doing it but i think it could be a
*  really useful uh public service i guess it's the kind of thing that might come up at senate
*  hearings and things like that uh where people in government might really want to know uh and i
*  guess at that point it would be perhaps more apparent why it's really important to find out
*  what the what the probability is um but yeah that's a way that i think there's definitely a risk of
*  misinterpretation by by journalists or something who don't appreciate the the spirit of saying
*  that we think it's x percent likely um but there could also be a lot of value in being being more
*  more direct about it yeah i'm not an expert on communications i think some of it just depends
*  on who your target audience is and how they're thinking about it i do think that i think in
*  general i'm i'm a fan of making rsp more concrete being more specific i think as over time i hope it
*  progresses in that direction as we like learn more and can can get more specific
*  i also think it's important for it to be verifiable and i think if you start to give these like precise
*  percentages like people will then ask like how do you know and i don't think there really is a a
*  clear answer to like how do you know that the probability of this thing is less than x percent
*  with for many of these situations it doesn't help with the bad faith actor or the bad faith
*  operator either because you know if you say well the safety threshold is one percent per year
*  they can kind of always just claim in this in the situation where we know so little that it's less
*  than one percent um it doesn't really bind people all that much maybe it's it's just a way that
*  people externally could understand a little better what what the opinions are within the organization
*  or at least what their stated opinions are i will say that internally i think it's an extremely
*  useful way for people to think about this right so if you if you are like working on this i think
*  you probably should think through what is an acceptable level of danger and uh try to estimate
*  it and communicate with like people you're working closely with in these terms i think can be a
*  really useful way to like give precise precise statements and i think that can be very valuable
*  a metaphor that um you use within your responsible scaling policy is um putting together an airplane
*  while you're flying it um i think that that is one way that the challenge is particularly difficult
*  for the industry and and and for anthropic that's unlike with biology safety levels where
*  basically we know the diseases that we're handling and we know how bad they are and we know how they
*  spread and things like that you know the people who are figuring out what what should bsl level
*  four security be like um can look at lots of studies to understand exactly the organisms
*  that already exist and how they would spread and um and how likely would they be to escape given
*  these particular you know ventilation systems and so on and even then they mess things up decently
*  often um but in this case you're dealing with something that doesn't exist that we're not even
*  sure like when it will exist or what it will look like uh and you're developing the thing at the same
*  time you're trying to figure out how to make it safe it's just just extremely difficult and i
*  guess i mean and we should expect mistakes we should that's something that we should keep in
*  mind uh is that even if people who are doing their absolute best here are likely to mess up
*  and that's a reason why we need this uh defense and depth strategy that you're talking about that
*  we don't want to put all of our eggs in in the rsp basket we want to have like many different
*  layers ideally yeah it's also like a reason to start early so like i i think one of the things
*  with cloud three was uh you know we that was sort of the first model where we really ran ran this
*  whole process and i think some part of me felt like wow this is kind of silly like i was pretty
*  confident that three was not catastrophically dangerous it was like slightly better than
*  gpt4 which had been out for a long time and not caused a catastrophe but i do think that like the
*  process of doing that learning what we can and then putting out like public statements about how
*  went what we learned uh is is the way that we can have this run really smoothly on the next time
*  like we can make mistakes now right we could have made as many we could have made a ton of mistakes
*  because the stakes are pretty low at the moment but in the future the stakes on this will be
*  really high and it will be really costly to make mistakes so it's important to get those practice
*  runs in all right um another kind of recurring theme that i've heard from some commentators
*  is that in their view the anthropic rsp just isn't conservative enough so on that account
*  there should be kind of wider buffers in case you're under eliciting capabilities that the
*  model has that you don't realize which is something that you're pretty concerned about
*  and i guess a different a different reason would be you might worry that there could be
*  discontinuous improvements in capabilities as you train bigger models with more data so to some
*  extent model learning and improvement is from a very zoomed out perspective is quite continuous
*  but on the other hand its ability to do any kind of particular task it can go from like fairly bad
*  to to quite good surprisingly quickly so they kind of can be sudden unexpected jumps with particular
*  particular capabilities yeah first can you maybe explain again in more detail how the anthropic
*  rsp kind of handles these safety buffers um given that you don't necessarily know what capabilities
*  the model might have before you train it that's a quite a challenging constraint to be operating
*  under yeah so there are these red line capabilities these are the capabilities that are actually the
*  dangerous ones we don't want to we don't want to train a model that has these capabilities until
*  we have the next set of precautions in place then there are evaluations we're creating and these
*  evaluations are meant to certify that the model is far short of those capabilities it's not can
*  the model do those capabilities because once we pass them we then need to put all the safety
*  mitigations in place etc so and then when do we have to run those those evaluations is sort of
*  just we have some heuristics of like when when the effective compute goes up by a certain a certain
*  fraction that is a very cheap thing that we can you know evaluate on every step of the run or
*  something along those lines that we know when to run it in terms of like how conservative they are
*  i guess like one example i would give is if you're thinking about like autonomy where a model could
*  could spread to um to like a bunch of other computers and sort of autonomously replicate
*  across the internet are i think revolutions are pretty conservative on that front we like
*  test if it can you know replicate to like a fully undefended machine or if it can like do some basic
*  fine tuning of a of a other language model to like add a simple back door i think these are pretty
*  simple capabilities and there's always a judgment call there right like we could set them we could
*  set them easier but then we might trip those and look at the model and be like ah this isn't really
*  dangerous it doesn't warrant the level of precaution that we're going to give it yeah there was something
*  also about you you said that you know the rsp says that you'll be worried if the model can succeed at
*  half the time at these various different tasks trying to spread itself to to other other machines
*  yeah why is why is half the time like succeeding half the time the threshold
*  yeah so there's sort of a few tasks i don't off the top of my head remember the exact
*  exact thresholds but basically like it's just a reliability thing right so in order for a model
*  to chain all of this together or yeah so in order for the model to chain all of these capabilities
*  together until like some long-running thing it does need to have a certain success rate
*  uh probably it actually needs a very very high success rate in order for it to like start
*  autonomously replicating despite us trying to stop it etc so we set a threshold that's like
*  fairly conservative on that front i guess it's part of the reason you're thinking well if a model can
*  do this worrying thing half the time then it might not be very much additional training away from
*  being able to do it 99 percent of the time that might just require some additional fine tuning
*  to get there and so then the model might be dangerous if it was leaked because it would
*  be so close to being able to do this stuff yeah i mean that that's often the case although of
*  course we can we could then elicit it to go if we'd set a higher number and we got even if we
*  got 10 maybe that's enough that we could bootstrap it so like often when you're training something
*  if it can be successful you can reward it for that successful behavior and then increase the odds of
*  that success so it's often easier to sort of go from 10 to 70 percent than it is to go from like
*  zero percent to 10 so if i understand correctly um the rsp proposes to retest models every time
*  you increase the amount of training compute or data by fourfold is that right that's that's kind
*  of the the checkpoint yeah so we're still still thinking about what is sort of the best thing to
*  do there and that one might change but we use this notion of effective compute so really this has to
*  do with when you you train a model it goes down to a certain loss and we have these nice scaling laws
*  of if you have more compute you should expect to get to the next loss you might also have a big
*  algorithmic win where you don't use any more compute but you get to a lower loss and we sort
*  of have coined this term effective compute so that would sort of account for that as well
*  these these jumps are sort of the the jump where you can tell like we have sort of a visceral sense
*  of how much smarter a model seems when you do that jump and have sort of set that as our our bar for
*  like when we have to run all these evaluations which do require you know a staff member to go
*  and run them spend a bunch of time trying to elicit the capabilities etc i think this is
*  somewhere i'm wary of sounding like too precise or like we understand this too well we don't
*  really know what the effective compute gap jump is between the yellow lines and the red lines
*  this is much more just like how we are thinking of how we are thinking about the problem and how
*  we are trying to set these uh like set these evaluations and the reason that the the yellow
*  line evaluations really do need to be substantially easier they'd be like far from the red line
*  capabilities because you might you might actually overshoot the yellow line capabilities by a
*  a fairly significant measure just off of when you run evaluations
*  so i think if i recall it was jv who's been on the show before um who wrote in his blog post
*  assessing the anthropic rsp just that he thinks that this ratio between the 4x and the 6x is not
*  large enough that you know if there is some discontinuous improvement or yeah you've really
*  been under eliciting the the capabilities of the models at these at these kind of interim check-in
*  points that that does leave the possibility that you could overshoot and you know get into quite a
*  dangerous point by accident and then by the time you get there then the model is like quite a bit
*  more capable than what you thought it would be and then you've got this difficult question of
*  whether to like do you then you know press the emergency button and and delete all the weights
*  because you've overshot uh there'd be incentives not to do that because you might be throwing away
*  100 million dollars worth of well i guess i don't know how much it would be but you'd be throwing
*  away a substantial amount of compute expenditure basically to to create this thing um and this and
*  this just worries him i mean that could be solved i think in his view just by having a larger
*  ratio there having a having a larger safety uh safety buffer of course that then runs a risk that
*  you're doing these like constant check-ins on stuff that you really are pretty confident is
*  not going to be actually that dangerous and uh and people might get frustrated with the rsp and
*  feel like it's wasting their time um so it's kind of a judgment call i guess um how large that
*  buffer needs to be yeah i think it's a tricky one to communicate about because uh it's confidential
*  what the jumps are between the models or something i think one thing i can share is like we ran this
*  we ran this on cloud 3 part way through through training so the jump from cloud 2 to cloud 3 was
*  bigger than the than that gap so you could sort of think of that as like an intelligence jump
*  from cloud 2 to cloud 3 is is bigger than what we're allowing there i think these feel it feels
*  reasonable to me but i think this is just a a judgment a judgment call that like different
*  people can have and i think that like this is the sort of thing where if we learn over time that this
*  seems too big or it seems too small uh that's the type of thing that hopefully we can we can
*  talk about publicly yeah is that something that you get feedback on that uh i suppose is your
*  if you are training these big models and you're checking in on them you can kind of predict
*  where you expect them to be like how likely or how likely they are to exceed a given threshold
*  and then if you do ever get surprised uh then that could be a sign that well we need to like
*  increase the increase the the buffer range here it's hard because right like the first one if
*  like the thing that would really tell us is if we don't pass the yellow line for one model and
*  then on the next iteration suddenly it's like blows past it and we look at this and we're like
*  whoa this thing is really dangerous it's probably past the red line and we have to you know delete
*  the model or immediately put in the security features etc for the next level i think that
*  that would be a sign that we'd like set the the buffer too small i guess again not the ideal way
*  to learn that but i suppose it definitely could set the set account amongst the pigeons um yeah
*  there would be earlier signs where you would notice like oh we really overshot by a lot it
*  feels like we're closer than we expected or something but that would sort of be the
*  the failure mode i guess rather than the warning sign so reading the rsp it seems pretty focused on
*  kind of catastrophic risks from like misuse you know sort of terrorist attacks or you know cbrn
*  that um and you know ai gone rogue like spreading out of control that sort of thing
*  is it basically right that the rsp or this kind of framework is not intended to address
*  kind of structural issues like ai displaces people from work and now they can't earn a living or you
*  know ai's are getting militarized and that's making it more difficult to evolve to like prevent you
*  know uh military encounters between countries because we can't control the models very well
*  or you know more more like near-term stuff like algorithmic bias or deep fakes or misinformation
*  are those kind of things that have to be dealt with by something other than a responsible scaling
*  policy yeah those are important problems but like the the rsp is is responsible for like
*  preventing sort of catastrophic risks and particularly has this framing that works well
*  for things that are sort of acute like new capability is developed and could sort of
*  first-order cause a lot of damage uh it's it's not going to work for things that are like what is
*  the long-term effect of this on society over time because we can't design evaluations to to test for
*  that effectively and thropic does have different teams that work on those other other two clusters
*  that are talked about right what are they called so we have a societal impacts team
*  is probably the the most most relevant one to that and and the policy team also has a lot of
*  a lot of relevance to these issues all right yeah i guess we're kind of going to wrap up on on rsp's
*  now is there anything you wanted to maybe say to the audience to wrap up this section um like
*  additional work that you think will be like ways that the audience might be able to contribute to
*  this enterprise of coming up with better internal company policies and then figuring out i suppose
*  how they could be models for for other actors to come up with with government policy as well yeah
*  i mean i think this is just a thing that many people can work on you know if you if you work
*  at a lab you could talk to talk to people there think about what what they should have as an rsp
*  if anything uh if you work in policy you should you should read these and and think about if there
*  are if there are lessons to take if you um don't don't do either of those i think you really can
*  think about threat modeling post post about that think about evaluations implement evaluations and
*  share those it's much i think it is the case that you know these companies are very busy and if
*  there is something that's just like shovel ready or like ready on on the shelf you could just grab
*  this this evaluation it's really quite easy to run them so uh yeah i think there's like quite a lot
*  that people can do to help here all right let's push on and talk about the the case that listeners
*  might be able to contribute to making and super intelligence go better by working at anthropic on
*  some of its various different projects first though how did you end up in your current role
*  at at anthropic kind of what's what's been your uh the career journey that uh that led you there
*  yeah so i think like largely started with an internship at give well which listeners might
*  know but it's a sort of a non-profit that evaluates charities to figure out where to give money most
*  effectively uh and i i did an internship there i was sort of learned a ton about global poverty
*  global health uh i was planning to do a phd in economics and go work on on global poverty at
*  the time but a few people there were sort of pushed me and said you know you should really
*  worry about ai safety we're gonna have these super intelligent ai's at some point in the future and
*  this could be a big risk uh i remember i like left that summer internship and was like wow these
*  people are crazy uh i like talked to all my family and they were like well what what are you thinking
*  uh but then i like i don't know it was like interesting so i kept talking to people uh
*  some people there other people sort of worried about this and i felt like every debate i lost
*  i would like have a little bit of them about why we shouldn't worry about it and i'd always come
*  away feeling like i lost the debate but not like fully convinced um and after like honestly like
*  a few years of doing this i i eventually decided this was at least enough convinced at least
*  convincing enough that i should work in ai uh it also turned out that working on poverty via this
*  economics phd route was a much longer and more difficult and like less likely to be successful
*  path than i had anticipated so i i sort of pivoted over to ai um i worked at vicarious uh which is
*  an agi lab that had sort of shifted towards a robotics product angle and i worked on
*  computer vision there for a while learning how ml how to do ml research um and then actually
*  80 000 hours uh reached out to me and uh convinced me that i should work on on safety more imminently
*  this uh sort of like ai was getting better it was like more important that i just have some direct
*  impact on doing safety research at the time i think open ai had by far the best uh safety research
*  coming out of there so i applied to work on safety at open ai uh i actually got rejected then i got
*  rejected again um in that time vicarious was nice enough to let me spend half of my time reading
*  safety papers so i was just sort of reading safety papers trying to do my own safety research although
*  it was somewhat difficult uh i didn't really know where to get started and eventually i also wrote
*  for like rohan shah who was on the podcast this alignment newsletter and i would like write i
*  read papers and wrote summaries and opinions for them for a while to like motivate myself um but
*  eventually third try got a job offer from from opening i joined the safety team there uh and
*  spent sort of eight months there mostly working on like code models and understanding how code
*  models would progress the the logic here being we just started the first like lms training on code
*  and i thought it was pretty scary if you think about like recursive self-improvement like models
*  that can write code is like the first step and trying to understand what what direction that
*  would go in would be really useful for for sort of informing safety directions and then a little
*  bit after that maybe like eight months in or so all of the safety team leads at open ai left most
*  of them to start entropic i was sort of felt very aligned with their values and missions so also went
*  to join join entropic uh sort of the main reason i'd been at open ai was for the safety work and
*  then at entropic actually everyone was just building out infrastructure to train models you
*  know there was no code it was sort of the the beginning of the company and i found that thing
*  was my comparative advantage was making them efficient so i like optimized the models to go
*  faster you know as i said if you have more compute you get a better model so that means if
*  your computer if you can make things run quicker you get a better model as well i did that for a
*  while and then shifted into management which had been something i like wanted to do for a while
*  and started sort of managing the pre-training team when it was it was five people and then have been
*  sort of growing the team growing the team since then training like better and better models along
*  the way yeah i'd heard that you'd been consuming 80 000 hours stuff years ago but i didn't didn't
*  realize uh it influenced you all that much what was that what was the step that we helped with it
*  was um just deciding that it was important to actually start working on safety related work
*  uh sooner rather than later actually a bunch of spots along the way i think like when i did that
*  give-all internship i did like a speed coaching at ea global or something with 80 000 hours and
*  uh was the people there were some of the people who were pushing me that i should work on on ai
*  uh like some of those conversations and then when i was at vicarious i think 80 000 hours reached out
*  to me and was sort of like more more pushy and specifically was like you should you should go
*  to work directly on safety now where i think i was otherwise sort of happy to just sort of keep
*  keep learning about ai for for a bit longer before shifting over to safety work well let's uh yeah
*  cool that uh adk was able to i guess i don't know whether it helped but i suppose it influenced you
*  in in in some direction um is there any is there any stuff that you've read from adk on ai cruise
*  advice that you think is uh mistaken where you want to want to tell the audience that uh maybe
*  they should do things a little bit differently than what we've been suggesting on the website or
*  or i guess on this on the show yeah first i do want to say adk was was very helpful both both in
*  pushing me to do it and setting me up with connections and introducing me to people and
*  getting me a lot of information it was it was really great um in terms of things that i maybe
*  disagree with from standard advice i think the main one would be to focus more on engineering than
*  than research i think there is sort of this historical thing where people have focused on
*  on research more so than engineering uh maybe i should define the difference the difference
*  between research and engineering here would be that research look can look more like figuring
*  out what directions you should you should work on designing experiments doing really careful
*  analysis and like understanding that analysis figuring out what conclusions to draw from a
*  set of experiments so like i can maybe give an example which is like you're training a model
*  with one architecture and you're like oh i have an idea we should try this other architecture
*  and in order to try it the right experiments would be these experiments and these would be the
*  comparisons to confirm if it's better or worse engineering is more of the implementation of the
*  experiment so then taking that experiment trying it and also creating tooling to make that fast
*  and easy to do so make it so that you and everyone else can can really quickly run experiments uh it
*  could be optimizing code so making things run much faster as i mentioned i did for a while
*  or making the code easier to use so that uh other people can can use it better and these aren't like
*  it's not like someone's an engineer or a researcher you kind of need both both of these skill sets to
*  do work you come up with ideas you implement them you see the results that you implement changes and
*  it's it's a fast iteration loop uh but it's somewhere where i think there's historically
*  been more prestige given to the research end despite the fact that most of the work is the
*  engineering end so you end up with like if you're you know you come up with your architecture idea
*  that takes an hour and then you spend like a week implementing it and then you run your analysis and
*  that maybe takes a few days but it sort of feels like the the engineering work takes the longest
*  um and then my other pitch here is going to be that the one place where i've often seen researchers
*  not investigate an area they should have is when the tooling is bad so when you go to do research
*  on this area and you're like oh it's really painful all my experiments are slow to run
*  uh it will really quickly like have you'll be like i'm gonna go to these other experiments that seem
*  easier so often by creating tooling to make something easy you actually can like open up
*  that direction and sort of like uh trailblaze the path for a bunch of other people to sort of follow
*  along and do and do a lot of experiments so what fraction of people at anthropic would you classify
*  as like more on the engineering end versus more on the on the research end i might go with my team
*  because i think i actually don't know for for all of anthropic and i think it's sort of a spectrum
*  but i would guess it's probably like 60 or 70 percent of people would be i would say are like
*  probably stronger on the on the engineering end than on the research end and when hiring i'm like
*  most excited about finding people who are who are strong on the engineering end and most most of our
*  interviews are sort of tailored towards that not because the research is important but because i
*  think it's sort of there's there's a little bit less need for it the distinction sounds like a
*  little bit artificial to me is that is that kind of true it feels like these things are they're
*  kind of all just a bit a bit part of a package yeah although i think the main distinction with
*  engineering is that it is a fairly separate career so i think there are many people maybe hopefully
*  listen this podcast who might have sort of been a software engineer at some tech company for
*  for a decade and built up a huge amount of expertise and experience with like designing
*  good software and and such and those people i think can actually learn the ml they sort of like
*  need to know to to do the job effectively very very quickly um and i think there's maybe like
*  another direction people could go in which is much more like i think of as like a phd in many cases
*  where you're like spend a lot of time developing research taste figuring out what are the right
*  experiments to run running these usually at smaller scale and maybe with like less of sort of a
*  single long lift code base that pushes you to develop better engineering practices and i think
*  that skill set and to be clear this is this is a relative term it's also a really valuable skill
*  set and you you always need a balance but i think i've like often had the impression that 80 000
*  hours pushes people more in that direction who want to work on on safety more the do a phd
*  become sort of like a research a research expert with really great research taste than pushing
*  people more on the sort of become a really great software engineer direction yeah we had a podcast
*  many years ago might be 2018 or 2017 with katherine olsen and daniel ziegler where they were also
*  saying engineering is the way to go or engineering is the thing that's really scarce and it's also
*  the easier way into the into the industry um but yeah it isn't it isn't a drum that we've been
*  banging all that frequently i don't think we've talked about it very much since then
*  so perhaps that's a that's a bit of a mistake that we haven't haven't been highlighting the
*  engineering roles um more you said it's kind of a different career track so you can go from
*  software engineering to the ml or like ai engineering that you're doing at entropic is
*  that is that an actual career progression that someone has and or like someone who's not already
*  in this how can they learn the the engineering skills that they need yeah so i think engineering
*  skills are are actually in some ways the easiest to learn because there's so much so many different
*  engineering places i think the way i would recommend it is you could work at any engineering
*  job usually i would say just working with the smartest people you can building like the most
*  complex complex systems you can also just do this open source you can contribute to an open source
*  project this is often a great way to like get mentorship from the maintainers and have something
*  that's publicly visible so if you then want to apply to a job you can be like here is this thing
*  i made and then you can also just create something new so you can say you know i want i think if you
*  want to work on ai engineering you should probably pick a project that's similar to what you want to
*  do so if you want to work on data for large language models take common crawl it's publicly
*  available crawl of the web and write a bunch of infrastructure to process it really efficiently
*  then maybe train some models on it like build out some infrastructure to train models and you can
*  you can sort of build out that that skill set relatively easily without without needing to work
*  somewhere why do you think people have been overestimating research relative to engineering is
*  it just that research sounds cooler is it got better branding i think historically it was a
*  prestige thing like i think i think there's sort of this distinction between like research
*  scientist and research engineer that like used to used to exist in the field where like research
*  scientists had phd's and were were kind of like designating the experiments that the research
*  engineers would run and i think that like that shifted a while ago so i think in some sense like
*  the shift has already started happening like now many places drop included it's like everyone's a
*  member of technical staff there isn't sort of this distinction and the reason is that the engineering
*  got more important particularly with scaling like once you got to the point where you were training
*  models that used a lot of compute on a big distributed cluster the engineering to implement
*  things on these distributed runs got much more complex than when it was sort of more quick
*  experiments on on cheat models to what extent is it a bottleneck just being able to build these
*  enormous computer clusters and and and operate them effectively is that is that a cool part of the
*  part of the stuff that anthropic has to do yeah so we we rely on like cloud providers to actually
*  build the data centers and like put the put the chips in it but we've now reached a scale where
*  the amount of compute we're using is sort of it's a very dedicated thing these are really
*  huge investments and we're sort of involved collaborating on it from sort of the design
*  up and i think it's it's a very critical piece right like given that compute is the main driver
*  the ability to take a lot of compute and use it all together and to design things that are cheap
*  given the the types of workloads you want to run can be like a huge a huge multiplier on how much
*  compute you have all right yeah did you want to give us the the pitch for working at anthropic as
*  a as a particularly good way to make the future future with super intelligent ai go well
*  yeah i may pitch like working on ai safety first i think the case here is it's just like really
*  really important yeah i think like agi is going to be like probably the biggest technological change
*  ever to happen the thing i think i keep in my mind is just like what would it be like to have
*  every person in the world able to spin up a company of a million people all of whom are as smart as
*  like the smartest people you know and task them with any project they want and you know you could
*  do a huge amount of good with that you could like help cure diseases you could tackle climate change
*  you could work on a ton of work on poverty there's sort of a ton of stuff you can do that would be
*  great but there's also a lot of ways it could go really really badly so i just think like the
*  stakes here are like are really high and then there's a pretty small number of people working
*  on it if you sort of account for all the people working on like things like this i think you're
*  probably gonna get something in like the thousands right now maybe 10 tens of thousands uh it's it's
*  rapidly increasing but it's it's quite small compared to the the scale of the problem in terms
*  of why anthropic um i think my main case here is just like the i think the best way to like make
*  sure things go well is to get a bunch of people who care about the same thing and all work together
*  with that as the as the main focus i mean anthropics not perfect we definitely have
*  have issues as does every organization but i think one thing that i really appreciate is just seeing
*  how much progress we can make when there's like a whole team where everyone everyone trusts each
*  other like kind of deeply shares the same goals and uh can like work on that together i guess i mean
*  there is a bit of a trade-off between if you imagine there's a kind of a pool of people who
*  are very focused on on ai safety and kind of have that have the attitude that they you just expressed
*  one approach would be to split them up between each of the different uh companies that are
*  working on frontier frontier ai and um i guess that would have have some benefits the alternative
*  would be to cluster them all together in a single place where they can where they can work together
*  and make a lot of progress uh but perhaps the things that they learn won't be as easily diffused
*  across all of the other other companies um yeah do you have a view on where the right balance is
*  there between kind of clustering people so they can work together more effectively communicate more
*  versus the need perhaps to have people have people everywhere who can absorb the work
*  i just think the benefits from working together are really huge like i think it's just it's so
*  different what you can like accomplish when you have like five people all working together as
*  opposed to five people like working independently unable to sort of speak to each other like
*  communicate about what they're doing you sort of run the risk of just doing everything everything
*  in parallel not learning from each other and and also not building trust which i think is just
*  somewhat a core piece of eventually being able to work together to implement the things
*  so in as much as anthropic um is or becomes like the the main leader in interpretability research
*  and other kind of lines of technical ai safety research um do you think it is the case that
*  other companies are going to be very interested to absorb that that research and apply it to
*  to their own work or is there a possibility that anthropic will have you know really good safety
*  techniques but then they might get stuck in anthropic uh and and you know potentially the
*  the most capable models that are being developed elsewhere are developed without them yeah so i
*  think that my hope is that uh if other people have either develop rsp like things or if there
*  are regulations sort of requiring particular safety mitigations people will want will have a
*  strong incentive to to to want to get better safety practices and we publish our safety research so
*  in some ways we're making it as easy as possible as we can for them we're like here is all the safety
*  research we've done here's as much detail as we can as we can give about it uh please go reproduce
*  it uh beyond that i think we're kind of it's hard to be accountable for what what other places do
*  and i think to some degree it just makes sense for anthropic to try to like set an example be
*  like you know we can be a frontier lab while while still care prioritizing safety putting out a lot
*  of a lot of safety work and hoping that kind of inspires others to to do the same do you know
*  i don't know what the answer to this is but is it do you know researchers at anthropics sometimes
*  go and visit you know other other ai companies and vice versa in order to like cross-pollinate
*  ideas i think i think that used to maybe happen a lot happen more and maybe things have gotten a
*  little bit tighter the the last few years but that's one idea that you could hope that uh you know
*  research might get passed around um or at least i mean you're saying it gets published um i guess
*  that's uh important but but there is a risk that um you know how the the technical details of how
*  you actually apply the methods won't always necessarily be in the paper or be very easy to
*  figure out so you also often need to talk to people uh to to make things work yeah i think
*  when something's published you can you can go and give talks on it and etc i think it's publishing
*  is sort of the first step where until it's published then it's like confidential information that that
*  can't be shared um so so yeah it's sort of like you have to first first figure out how to do it
*  then publish it um there are more steps you could take right you could then like open source code
*  that enables you to to to run it more carefully and like there's a lot of work you could go in
*  that direction and then it's just sort of a balance of how much time you spend on disseminating your
*  results versus pushing your your agenda agenda forward to like actually make progress it's
*  possible that i'm slightly um i'm analogizing from i guess biology that i'm somewhat more familiar
*  with where it's notorious that having a biology paper or a medical paper does not allow you to
*  replicate the experiment because there's so many important details missing but is is it possible
*  that in ml in ai um you know people tend to just publish all of the stuff that they all of the data
*  maybe and all of the code online on github or whatever such that it's like much more
*  straightforward to completely replicate a piece a piece of research elsewhere yeah i think it's
*  much much it's a totally different uh level of replication it depends on the paper but on on
*  many papers if a paper is like published in in some conference i would sort of expect that someone
*  can pull up the paper and reimplement it with like maybe a week's worth of work uh there's a
*  strong norm of sometimes sometimes providing the actual code that you need to run but but providing
*  enough detail that you can i think with some things it can be tricky where like i don't know
*  our tribunal team just put out a paper on how to get uh features on one of our production models
*  and we didn't release details about our production model so we tried to include enough detail that
*  someone could replicate this on another model but they probably can't they can't exactly like create
*  our our production model and like get the exact features that we have okay um in a minute we'll
*  talk about uh one of the concerns that people might have about working with uh working at any
*  ai company but um uh in the meantime yeah what roles are you hiring for at the moment and
*  what roles are likely to be open at and and topic in future so probably just check our website
*  there's there's like quite a lot i'll kind of highlight a few so i think the first one
*  should highlight is the rsp team is is looking for people to develop evaluations uh work on the
*  rsp itself figure out the like what what the next set next version of the rsp should look like etc
*  uh on my team we're hiring a bunch of research engineers so this is come up with approaches to
*  improve models implement them analyze the results kind of pushing pushing that loop uh and then also
*  performance engineers this one's maybe like a little bit more surprising but a lot of the work
*  now happens on custom ai chips and making those run really efficiently is is sort of absolutely
*  critical there's a lot of of interplay between how fast it can go and how good the model is so
*  we're sort of hiring quite quite a number of performance engineers where it's much you don't
*  need to have a ton of a x ai expertise just having like deep knowledge of how how hardware
*  works and how to write code really efficiently how can people learn that skill is that is that is
*  there are there courses for that there are probably courses i think with basically everything i would
*  recommend finding a product finding a project finding like someone to mentor you and you know
*  be cognizant of their time maybe you like spend a bunch of time writing up some code and you send
*  them a a few hundred lines and say can you review this and help me and and help me or or maybe you
*  got some weekly meeting where you ask questions but yeah i think you can you can read about it
*  online there probably you can take courses or you can just pick a project and say you know like i'm
*  going to implement a transformer as fast as i possibly can and sort of hack on that for for a
*  while are most people coming into anthropic from other ai companies or like the tech industry more
*  broadly or from phd's or maybe maybe not even phd's it's quite a mix uh i think like phd is
*  definitely not necessary i think it's like one direction to go to build up this skill set
*  uh we have a shockingly large number of people with physics backgrounds uh who have done
*  theoretical physics for a long time and then sort of spend some number of months learning
*  learning the engineering to to be able to like write python really well essentially and then
*  switch in so i think there's not really a particular background that is sort of needed it's just uh i
*  would say if you're directly preparing for it just pick the the closest thing you can to the job and
*  do that to prepare but don't feel like you needed to have some particular background in order to
*  apply this question is slightly absurd because it's such a range of different roles that people
*  could potentially apply for at entropic but do you have any kind of any advice for people who would
*  like you know the vision for their career is working at entropic or something similar but they
*  don't yet feel like they're qualified to get a role at such a such a serious organization kind of
*  how can they go like what are some interesting underrated paths maybe to gain experience or
*  so that they can be be be more useful to the project in future
*  yeah i would just pick the role you want and then do it externally do it in a very publicly
*  visible way get get advice and and then apply with that as an example so like if you want to work on
*  interpretability make some tooling to pull out features of models and post that on github or
*  publish a paper on interpretability if you want to work on on the rsp then like make a really good
*  evaluation post it on github with a nice write-up of how to run it and include that with your with
*  your application this sort of takes time and it's like it's hard to do well but i think that it's
*  it's both the best way to know if it's really the role you want and when hiring for something i have
*  a role in mind and i want to know if someone can do it and if someone has shown like look i've
*  already i'm already doing this role of course i can here's my proof i can do it well that's like the
*  most convincing case in many ways more so than like the signal you'd get out of an interview where
*  all you really know is they did well on this particular question so in terms of working at
*  ai companies regular listeners will recall that earlier in the year i spoke with javi marshowitz
*  who's a kind of longtime follower advances in ai and i'd say is a bit on the pessimistic side
*  about ai safety and maybe also not you know i think i think he likes the the anthropic rsp but
*  he's not like convinced that any of the safety plans put forward by by any company or any
*  government are at the end of the day going to be quite enough to keep us safe from you know
*  rapidly self-improving ai and he said that he was pretty strongly against people taking
*  capabilities roles that would kind of push forward the frontier of what the most powerful
*  ai models can do i guess especially at at leading ai companies because i mean the basic the basic
*  argument is just that those roles are causing a lot of harm because they're speeding things up and
*  leaving us less time to solve whatever kind of safety issues where we're going to need to address
*  and you know i pushed back a little bit and he wasn't really convinced by the various
*  kind of justifications that one might might give like the need to gain skills that you could then
*  apply to to safety work later or maybe you'd have the ability to influence a company's culture by
*  being on the inside rather than the outside i think i think of all companies uh jv i i would
*  i would certainly imagine is most sympathetic to to anthropic uh but i guess his philosophy is very
*  much to kind of rely on hard constraints rather than put trust in any particular individuals or
*  organizations that too that you like um i'm guessing that kind of you might have heard what
*  what jv had to say on the on in that episode um and i guess it was a critique that arguably applies
*  to to to your job about training training training quad three and other you know frontier lms so i'm
*  kind of fascinated to hear what you what you thought of of jv's perspective there so i think
*  it's but i think there's like one argument which is to do this to build career capital and then
*  there's another that is like to do this to for direct impact i think on the career capital one
*  i'm i'm pretty skeptical i think career capital is sort of weird to think about in this field that's
*  like growing exponentially you know i think in sort of a normal field people often say like you're
*  the most impact late in your career you know you've built up skills for a while and then
*  then maybe your 40s or 50s is when you have like the the most impact of your career but given the
*  like rapid growth in this field it i think actually like the the best moment for impact is now i don't
*  know i often think of like in 2021 i was very anathropic i think there were probably tens of
*  people working on on large language models which i thought were like the main path towards a gi
*  and you know now there are thousands i've improved i've gotten better since then but i think probably
*  i had like way more potential for impact back in 2021 when there were only tens of people working
*  on it yeah your best years are behind you nick yeah i think in many ways i mean i think the
*  potential was very high i still think that like it is still there's still a lot of room for impact
*  and it will like maybe decay but it is from an extremely high number uh or from an extremely
*  high level um and then the thing is just the field isn't that deep like because it's such a recent
*  development it's not like you need to learn a lot before you can contribute like there i think if
*  you want to do physics and you have to learn like the past multi-thousand like thousands of years of
*  physics before you can like push the frontier that's a very different setup from from where
*  we're kind of at um and maybe the last thing is just like if you think timelines are short uh like
*  depending exactly how short there's just actually not that much time left so if you're gonna if you
*  think you know there's five years and you spend two of them building up a skill set like that's
*  that's a significant fraction of the time i'm not saying that that should be someone's timeline or
*  anything but like the shorter they are the less that makes sense so yeah i think i like from a
*  career capital perspective i probably agree does that make sense yeah yeah and what about from from
*  other points of view yeah i think from a like direct impact perspective i'm i'm fairly less
*  convinced i don't part of this is just that i don't have this framing of like there's capabilities and
*  there is safety and they are like separate tracks that are racing i think it's like one way to look
*  at it but i actually think they're really intertwined and a lot of safety work relies on
*  capabilities advances i can give this example of like this many shot jailbreaking paper that
*  one of our safety teams published which uses long context models to find a like important a jailbreak
*  that can apply to claude and to and to other models and that like research was only possible because
*  we had long context models that that you could test this on so i think there's just a lot of
*  cases where the things come together but then i think like if you're going to work on capabilities
*  you should be really thoughtful about it like i do think there is there is a risk you are speeding
*  them up in some sense you could be creating something that is really dangerous but i don't
*  think it's as simple as just don't don't do it i think you want to think all the way through to
*  like what is the downstream impact when when someone trains a gi and how how will you have
*  affected that uh and that's that's a really hard problem to think about you know there's a million
*  factors at play uh but i think you should you should think it through come to your best judgment
*  and then reevaluate and get get other people's opinions sort of as you go um some of the things
*  i might like suggest doing if you're if you're considering it is like understand what if you're
*  considering working on capabilities at some lab is like try to understand their theory of change
*  like ask ask people there ask like how how does your work on capabilities lead to a better outcome
*  and see if you agree with that i would talk to their safety team talk to safety researchers
*  externally get their take say like do they think that this is this is a good thing to do
*  um and then i would also look at their track record and their governance and all the things
*  that sort of to answer the question of do you think they will push on this theory of change like
*  over the next five years are you confident this is sort of what what will actually happen one thing
*  for me that like convinced me an anthropic that i was maybe not doing evil or maybe feel much
*  much better about it is that our safety team is pretty is willing to help out with capabilities
*  and and like actually wants us to do well with that so like early on with opus before we launched
*  it we had a major fire there was sort of a bunch of issues that came up and there was one like very
*  critical research project that like my team didn't have capacity to push forward so i i asked ethan
*  who's pres who's one of the the safety leads at entropic was like ah can you can you help with
*  this it was actually like during an off-site and ethan and like most of his team just like left
*  basically like went upstairs to this building in the woods that we had for the off-site and
*  cranked out research on this for like the next two weeks and just sort of like and for me at least
*  i was like ah yes the safety team here also thinks that us us staying on the frontier is is critical
*  so the basic idea is you think that the safety work the safety research of all kinds of many
*  different types that entropic is doing is very useful it sets a great example it's research that
*  could then be adopted by by other groups and also used by by entropic to to make safe models and the
*  only way that that can happen the only reason that that research is possible at all is that
*  entropic has these kind of frontier lms on which to experiment and and and do that research um and
*  to be at the cutting edge generally of of this technology uh and so able to figure out like what
*  are the what's the safety research agenda that is most likely to be relevant in in in in future
*  if i imagine what what would jv say uh try to get a try to model him i suppose i i guess that he
*  might say yes given that there's this this competitive dynamic forcing us to shorten
*  timelines you know bringing bringing the the the future forward maybe faster than we feel
*  comfortable with maybe that maybe that's the best you can do but wouldn't it be great if we could
*  coordinate more in order to to buy ourselves more time i guess that would be one angle another
*  angle that i've heard from some people i don't know whether whether g would say this or not
*  is that we're nowhere near actually having all the safety relevant insights that we can have with
*  the models that we have now and so given that there's still like so such first time material
*  with like clod 2 maybe or at least with clod 3 now like why do you need to go ahead and train
*  clod 4 um like is you know maybe it's true that five years ago when we were so much further away
*  from from having a gi or having models that were really interesting to work with we were a little
*  bit at a loose end trying to figure out what safety research would be would be good because
*  we just didn't have like we just didn't know what direction things were going to go but now
*  there's so much safety research like it's there's a there's a proliferation of cambrian explosion
*  of really valuable work and we don't necessarily need like more capable models than what we have
*  now in order to to to to discover really valuable uh valuable things yeah what would you what would
*  you say to that yeah and the first one i think there's sometimes this like what what is the
*  ideal world if like everyone was me or something like if everyone thought what i thought would be
*  the ideal setup and i think that's just not how sort of the world works and i think to some degree
*  you really only can control what you do and maybe you can control what like or control maybe you can
*  influence what like a small number of people you talk to do but i think you sort of have to think
*  about your role in the context of of the broader world more or less acting uh in the way that
*  they're going to to act so so yeah and like some part it's definitely a big part of why i think
*  it's important for anthropoctec capabilities is to enable safety researchers to have better models
*  another piece of it is to enable us to have have an impact on the field and like try to set this
*  example for uh other labs to of like that you can deploy models responsibly and and do this in a way
*  that doesn't cause catastrophic risks and and continues to like push push on safety in terms
*  of like can we do safety research with current models i think there is definitely a lot to do
*  i also think we will target that work better the closer we get to a gi like i think the last
*  the last year before a gi will definitely be the the most targeted safety work hopefully there'll
*  be the most safety work happening then but it will be the most time constraint so you need to do
*  you need to do work now because there's a bunch of serial time like serial time that's needed in
*  order to make progress but you also want to to sort of be ready to make use of the of the most
*  well-directed time towards the end i guess i you know another concern that people have
*  which you touched on earlier but maybe maybe we could talk about a little bit more is this worry
*  that anthropic by existing by competing with other ai companies it stokes the stokes the arms race
*  uh increases the pressure on them feeling that they need to improve their models further put
*  more money into it uh you know release things as quickly as they can if i remember your your
*  your basic response to that was like yes that that effect's not zero but you know in the scheme of
*  things there's a lot of pressure on on companies to be trading models and trying to to improve them
*  and uh you know uh anthropic is a pretty is kind of a drop in the drop drop in the bucket there
*  and so this this isn't necessarily the most important thing to be worrying about yeah i
*  think basically like that's pretty accurate i think one way i would think about it is just what would
*  happen if anthropic stopped existing right like if we all just disappeared what what effect would
*  that have in the world either if you or if you think about like if we dissolved as a company and
*  everyone went to work at all the others and my guess is it just wouldn't look like everyone slows
*  down is way more cautious that that's like not my model of it if that was my model then i would be
*  like ah we're probably probably doing something wrong i think they're yeah so i think it's an
*  effect but i think you i sort of think about in terms of like what is the net effect of
*  anthropic being on the frontier when you account for like all the different actions we're taking
*  all the safety research all the all the policy advocacy like the effect our products have helping
*  users there's sort of like this whole whole large uh scheme and you you can't really like add it all
*  up and subtract the costs but you sort of uh i think you can do that somewhat like um in your
*  mind or something yeah i see so yeah so the way you conceptualize it is thinking anthropic as a
*  whole what impact is it having by existing compared to some kind of factual where anthropic wasn't
*  there and then i then you're contributing to this broader enterprise that is anthropic and all of
*  its projects and plans to plans together rather than thinking about you know today i got up and
*  i and i helped to improve core three in this like narrow way what impact does that specifically have
*  because that's just maybe it's missing the real effects that that matter the most from like
*  allowing this organization to exist through your work yeah you could definitely think on the margin
*  like to some degree you know if you're if you're joining and going to like help with something you
*  are just increasing anthropics uh sort of this marginal amount of capabilities and and then i
*  would just sort of look at like do you think we would be on a better trajectory if anthropic had
*  better models and do you think we'd be on a worse trajectory if anthropic had significantly worse
*  models uh would be sort of the comparison i think you could you could look at like oh well what
*  would happen if anthropic didn't ship club three last year or earlier this year what are some of
*  the lines of research that you're most pleased that you've helped anthropic to pursue what are
*  some of the kind of safety safety safety wins that uh that you're really pleased by i'm really
*  excited about the about the safety work i think there's just like a ton of it that has come out
*  of anthropic uh i could sort of start with interpretability where there i think at the
*  beginning of anthropic it was like figuring out how like single layer transformers work these sort
*  of like very simple toy models and in sort of the past few years that's this is not my doing this is
*  all the intervillain team that has sort of scaled up into like actually being able to look at
*  production models that people are really using and find find useful and identify particular features
*  we sort of had this recent one on the golden gate bridge where they found a feature that if you uh
*  if you increase it it makes the model it's it's the model representation of the golden gate bridge
*  if you increase it the model talks more about the golden gate bridge and that's sort of like
*  a very cool causal effect where you can change something and it actually changes the model
*  behavior in a way that like gives you more certainty you've really found something
*  is the hope with that for example that you could find i guess you found the uh i don't know whether
*  you call it the the golden gate bridge neuron but i don't know the the you found where the golden
*  gate bridge is in the model uh and then you can turn that up so that i'm not sure whether all
*  listeners will have seen this but it is it is very funny because uh you get clawed through it just
*  its mind is constantly turned to thinking about the golden gate bridge uh even when the question
*  has nothing to do with it and it gets frustrated with itself realizing that it's going off topic
*  and then tries to bring it back to the thing that you asked but then it just can't it just
*  can't avoid talking about the golden gate bridge again is the hope that you could find the honesty
*  part of the model and scale that up enormously or generally find the you know deception part
*  and scale that down in the same way yeah so like there actually are a bunch if you look at the
*  paper there's a bunch of safety relevant features i think that the the golden gate bridge one was
*  like cuter or something and like got a bit more attention but yeah there are a ton of features
*  that are really safety relevant i think one of my favorites was one that will tell you if code is
*  uh incorrect or something so or has a vulnerability something along those lines
*  and then you can change that and suddenly it doesn't write the vulnerability or it makes the
*  code correct uh and that sort of shows the model knows knows about concepts at that level now can
*  we use this directly to like solve major issues probably not yet right there's a lot more work to
*  be done here but i think it's just been a huge amount of progress uh and i think on yeah i think
*  that it's it's fair to say like that that progress would wouldn't have happened without the like
*  anthropics interpretability team like pushing that field forward a lot yeah is there any other
*  anthropic research that you're proud of yeah uh i mentioned this one a little bit earlier but
*  there's sort of this like multi-shot jailbreaking uh from from our alignment team that pushed uh like
*  if you have a long context model which is something that we released you can jailbreak a model by
*  just giving it a lot of examples in this very long context and it's a very reliable jailbreak
*  uh to get models to do things you don't want so this is sort of in the in the vein of the rsp one
*  of the things we want to have is to be able to be robust to really intense red teaming where if a
*  model has a dangerous capability you can have safety features that prevent people from listening
*  it and this is like an identification of a of a major risk for that um we also have this like
*  sleeper agents paper which sort of shows the early signs of models having having deceptive behavior
*  yeah i could talk about a lot more of it there's actually just like a really huge amount and i
*  think that's fairly critical here is like i think often with safety things people get focused on
*  inputs and not outputs or something and i think the important thing is not is to think about like
*  how much how much progress are we actually making on the safety front like that is ultimately what's
*  going to matter in like some number of years when we get close to a gi it won't be like how many
*  gpus do we use how many people worked on it it's going to be like what did we find and how how
*  effective were we at it uh and for product this is very natural people think in terms of revenue
*  you know how many how many users did you get you have these like end metrics that are like
*  the fundamental thing you care about and i think for safety it's it's much fuzzier and harder to
*  measure but putting out a lot of papers and that are that are good uh is is quite important yeah
*  i mean if you want to keep going if there's any others that you that you want to flag uh
*  i mean don't hurry yeah i mean like talking about influence functions i think this is a really a
*  really cool one um where one framing of mech interp mechanical interoperability is or sorry
*  mechanistic interpretability is uh it lets us look at the weights and understand like why a model has
*  a behavior by looking at particular weight the idea of influence functions is to look is to
*  understand why a model has a behavior by looking at the training data so you can understand what
*  in your training data contributed to a particular behavior from the model yeah i think that would
*  that was like pretty exciting to see work i think constitutional ai is another example i would
*  highlight where uh we can train a model to to follow a set of principles via sort of ai feedback
*  so instead of having to sort of have human human feedback for a bunch of things you can just write
*  out a set of principles i want the model to not do this i want to not do this i want to not do this
*  and train the model to follow that that constitution is there any work at anthropic that
*  you personally would be wary or at least not enthusiastic to to contribute to so i think in
*  general this is like a good question to ask i think like the work i'm doing is currently the
*  highest impact thing and i think i should frequently wonder if that's the case and talk to people uh
*  and and reassess i think right now that i don't think there's any work at anthropic that i
*  wouldn't contribute to or like i think shouldn't be done it's probably not the way i would i would
*  approach it it's like if there was something that i thought anthropic was doing that was bad for the
*  world i would write a doc making my case and send it send it to like the relevant person who's
*  who's responsible for that and then like have a discussion with them about it because just
*  just opting out isn't going to actually change it right if someone else will just do it that
*  that doesn't accomplish much and we try to sort of operate as one team where everyone is like
*  aiming towards the same goals and not have this sort of like two different teams are at odds where
*  you're like hoping someone else won't succeed i guess people people might have a reasonable sense
*  of the culture at anthropic just just from listening to this interview but is there anything
*  else that's interesting about working at anthropic that might not be immediately obvious i think the
*  one thing that like is part of our culture that at least surprised me is spending a lot of time
*  pair programming this is just it's just a very collaborative culture so i think when i first
*  joined um i don't know i was working on a particular method of like distributing
*  a language model training across a bunch of gpus and tom brown who's one of the founders and had
*  done this for for gpt3 just put like an eight-hour meeting on my calendar and i just watched him code
*  it and then like i was on different time zones so basically like during the hours when he wasn't
*  working and i was working i would like push forward as far as i could and then the next day
*  we would meet again and like continue continue on and i think it's just a really good way of aligning
*  people where it's a shared project instead of being a you're bothering someone by asking for
*  their help it's like you're working together on the thing and and you learn you learn a lot you
*  also learn a lot of like the smaller things that you wouldn't otherwise see if like how does someone
*  navigate their code editor like what what exactly is their style of debugging this sort of problem
*  whereas if you go and ask them for advice or like how do i do this project they're not going to tell
*  you the like low level details when do they pull out a debugger versus uh some other method of
*  some other tool for solving the problem so so this is literally just watching one another screen
*  so you're doing a screen share thing where you watch yeah i'll give some some free advertising
*  to tuple which is this great software for it where you can share screens you can control
*  each other's screens and like draw draw on the screen and typically one person will drive they'll
*  be like basically doing the work another person will watch ask questions point out mistakes
*  occasionally grab the cursor and just just change it
*  um it's interesting that i feel in in other industries having your boss or a colleague
*  stare constantly at your screen uh would give people the creep so they would hate it whereas
*  it seems like in uh in in programming this is something that people are really excited
*  by and they feel like it enhances their productivity and makes the work a lot more fun
*  oh yeah i mean it can be exhausting and like tyree i think the first time i did this i was
*  too nervous to take to take a bathroom break and after multiple hours was like can i go to the
*  bathroom and realize that was an absurd thing to ask after like multiple hours of working on
*  something so like what are you back at back at primary school yeah yeah it could definitely feel
*  a little bit more intense and that like someone's watching you and they'll you know they might give
*  you feedback on like ah you're kind of going slow here like this sort of thing would speed you up
*  but i think you really can learn a lot from that sort of intensive uh partnering with someone
*  all right um i think we've uh we've talked about anthrobic for a while i guess um
*  final question is so so obviously anthrobic its main um its main office is in san francisco right
*  and i heard that it was opening um kind of a branch in in london are those the the two main
*  places and indeed um are there many people who work remotely or anything like that yeah so we
*  have the main offices in sf and then we have office in london uh dublin i think seattle and new york
*  our typical policy is like 25 time in person so some people will mostly work remotely and then
*  go to sort of one of the hubs for it's usually it's usually one week per month uh the idea of
*  this is that you should we want people to like build trust with each other and like be able to
*  work together well and like know each other and that that sort of involves some amount of social
*  interaction with with your co-workers but also for a variety of reasons like sometimes getting
*  the best people that people are bound to particular locations i kind of have been assuming that all of
*  the main ai companies are probably hiring hand over fist and i guess i know um anthrobic's received
*  like big investment from amazon maybe some other folks as well but is it yeah does it feel like
*  the organization is growing a lot that there's lots of new people around all the time yeah growth
*  has been very rapid we recently moved into a new office before that we were uh we'd run out of
*  desks which was an interesting moment for the company it was very crammed now there's space
*  uh yeah i mean rapid growth is a a very like difficult challenge but also a very interesting
*  one to work on i think that's like to some degree what i spend a lot of my time thinking about is
*  just how can how can we grow grow the team and be able to maintain this sort of uh linear growth
*  and productivity is sort of the dream right if you double the number of people you get twice as
*  much done and you never actually hit that but it's it takes a lot of work because there's now all
*  this communication overhead and you have to do a bunch to make sure everyone's like working
*  towards the same goals sort of maintain the the culture that we currently have i've given you a
*  lot of time to talk about what's great about anthrobic but i should at least ask you what's
*  what's kind of worst about anthrobic what would you most like to see to see improved i think
*  honestly the first thing that comes to mind is just the like stakes of what we're working on
*  or something i think that there was sort of a a period a few years ago where i felt like
*  ah safety is really important i felt like motivated and i was it was uh it was a thing i should do and
*  like got got value out of it but i didn't feel this sort of uh oh it could be really urgent this
*  might be like you know decisions i'm making are just like really really high stakes decisions and
*  i think anthrobic definitely feels high stakes i think it's often portrayed as this like doomy
*  culture i don't think it's that i think there is like a lot of benefits and i think we i think i'm
*  like pretty excited about the work i'm doing and it's it's quite fun on a day-to-day basis
*  but it does feel very high intensity and kind of uh many of these decisions are they they really
*  do matter right if you if you really think we're going to have the the biggest like technological
*  change ever and how well that goes depends in a large part on like how well you do at your job on
*  like that given day and no pressure yeah um and and the timelines are really fast too right even
*  commercially you can kind of see that it's like months sort of between between major releases and
*  that sort of that puts a lot of pressure where if you're trying to like keep up with the frontier
*  of ai progress it it is quite difficult and it relies on sort of uh success on on very short
*  timelines yeah is that so for someone who's you know has relevant skills might might be a good
*  employee but you know maybe maybe they they struggle to operate at like super high productivity
*  super high energy all the time uh could that be an issue for them at a place like anthropic where
*  it sounds like you know there's a lot of pressure to deliver all the time like i'm not i guess
*  potentially internally but also just the external pressures are pretty substantial yeah i think that
*  i some part of me wants to say yes i think it is it's really important to be very like high
*  performing a lot of the time the standard of always do everything perfect all of the time is
*  not something anyone meets and it's like i think it is important sometimes to just keep in mind
*  that all you can do is like your best your best effort so uh you know we will mess things up and
*  even if it's high stakes and that's like quite unfortunate like it's it's unavoidable like no
*  no one is no one is perfect so i would i wouldn't sort of set too high of a like oh i i couldn't
*  possibly like handle that like i think people really can and you can you can grow into that and
*  like get get used to that level of pressure and how to operate under it all right um i guess we
*  should we should wrap up we've been at this for a couple of hours but um i'm curious to know what
*  what is an ai application that you think is overrated and maybe going to take longer to arrive
*  than people expect and uh maybe what's what's an application that you think might be uh underrated
*  and uh like consumers might uh be really getting a lot of value out uh out of surprisingly soon
*  um overrated i think an overrated it's the same i think people are often like oh i should never
*  uh like i'll never have to use google again or it's a great way to like get information
*  and i find that i still like if i just have a simple question and i want to know the answer
*  just googling it will give me the answer quickly and it's almost always right whereas if i can go
*  ask claude but it'll like take us you know it'll like sample it out and then i'll be like is it
*  true is it not true it's probably true but like it's in this conversational tone uh so i think
*  that's one that like doesn't yet feel like the strengths the the place where i find the most
*  benefit is coding i think this is not a like super generalizable case or something but if you're
*  ever writing software or if you've thought like i don't know how to write software but i wish i did
*  the the models are are really quite good at it uh and if you can kind of get yourself set up you
*  can probably just write something out in english and it will like spit out the code to to do the
*  thing you need rather quickly um and then the other thing is like problems where i don't
*  like i don't know what i would search for like i have some question uh i want to know the answer
*  but it relies on a lot of context it would be this giant query like models are really good at that
*  you can give them documents you give them like huge amounts of stuff and explain really precisely
*  what you want and then they will like interpret it and give you give you an answer that like
*  accounts for all the information you've you've given them yeah i think i do use it mostly as a
*  substitute for google but not for simple queries it's more like something kind of complicated
*  something kind of complicated where i feel like i'd have to dig into some articles to figure out
*  the answer um i think one that jumps to mind is um like did francisco franco was kind of on the
*  side of the nazis during world war two but then he was in power for another 30 years like did he
*  have a comment on that what did he say about the nazis later on uh and i think claude was able to
*  give me uh an accurate answer to that whereas i probably would have i could have spent hours maybe
*  trying to look into that trying to trying to trying to find something um the answer is he
*  mostly just didn't talk about it my other favorite one which is a super tiny use case is if i ever
*  have to like format something and do something like if there's just some giant list of numbers
*  that someone sent me and like a slack thread and it's bulleted i want to add them up i can like
*  just copy paste it into claude and say add the things up and like any format it's very good at
*  taking this like weird thing kind of structuring it and then doing a simple operation so i've heard
*  it's really good all of these models are really good at programming uh and i've thought i mean
*  i've never programmed before really uh and i've thought about maybe i could use them to to make
*  something of use but i guess i'm at such a basic level i don't even know like where so i would get
*  the code and then where would i run it what is there a place that i could look this up like uh
*  yeah yeah i mean i think you basically want to just like look up like i would suggest python like
*  get an introduction to python and get get your environment set up like you'll eventually run
*  python and then some some file uh and you'll hit enter and that will run the code and that part's
*  annoying i mean claude could help you if you run into issues setting it up but once you have it
*  set up it will do you you can just be like ah write me some code to do x and and it will just
*  it will write that pretty not perfectly but pretty accurately yeah i guess i should just ask claude
*  for guidance on this as well um do you so i've got a kid uh it's a couple of months old um i
*  guess you know uh in three or four years time they'll be going to preschool and then eventually
*  starting you know reception primary school i guess my hope is that by that time ai models might be
*  really involved in the education process and kids will be able to get a lot more kind of one at
*  maybe it would be very difficult to keep a five-year-old focused on the task of talking to an
*  llm but uh i would think that we're close to being able to have a lot more like individualized
*  attention from educators even if those educators are are ai models and this might enable kids to
*  learn a lot faster than they can when there's kind of only one teacher split between 20 students or
*  something like that do you think that kind of stuff will come in in time for uh my my my kid
*  first going to going to school or might it take a bit longer than that i can't be sure but yeah i
*  think there will be some some pretty major changes by the time your kid is going to school
*  okay yeah that's good that's uh that's one that i really don't want to miss on the timelines
*  we can i think i'm worried i'm like uh like um nathan lambenz i'm worried about hyper scaling
*  but on a lot of these applications i really just want them to uh to reach us as soon as possible
*  because they do seem so useful um my guest today has been nick joseph thanks so much for coming on
*  the 80 000 hours podcast nick thank you if you're really interested in the pretty
*  vexed question of whether all things considered it's good or bad to work at the top ai companies
*  if you want to make the transition to superhuman ai go well our researcher arden keeler has just
*  published a new article on exactly that titled should you work at a frontier ai company you can
*  find that by googling 80 000 hours and should you work at a frontier ai company or heading to our
*  website 80 000 hours dot org and just looking through our research and finally before we go
*  just a reminder that we are hiring for two new senior roles at 80 000 hours a head of video and
*  a head of marketing and you can learn more about both of those at 80 000 hours dot org slash latest
*  those roles would probably be done in our offices in central london but we are open to exceptional
*  remote candidates in some cases and alternatively if you're not in the uk but you would like to be
*  we can also support uk visa applications the salaries for these two roles would vary depending
*  on seniority but someone with five years of relevant experience would be paid approximately
*  80 000 pounds something like that the first of these two roles the head of video would be
*  someone in charge of setting up a whole new video product for 80 000 hours obviously people are
*  spending a larger and larger fraction of their time online watching videos on video specific
*  platforms and we want to explain our ideas there in a compelling way that can reach the sorts of
*  people who care about them that video program could take a range of forms including 15 minute
*  direct to climber vlogs many lots and lots of one minute videos maybe 10 minute explainers maybe
*  that's probably my favorite youtube format or alternatively lengthy video essays some people
*  really like those the best format would that would be something for this new head of video to
*  look into and figure out for us we're also looking for a new head of marketing to lead our marketing
*  efforts to reach our target audience at a large scale they're going to be setting and executing
*  on a strategy managing and building a team and ultimately deploying our yearly marketing budget
*  of around three million dollars we currently run sponsorships on major podcasts and youtube
*  channels you might hopefully you've seen some of them we also do targeted ads on a range of
*  social media platforms and collectively that's gotten hundreds of thousands of new people onto
*  our email newsletter we also mail out a copy of one of our books about high minute high impact
*  career choice every eight minutes that's what i'm told so there's a there's certainly the potential
*  to reach many people if you're doing that job well applications will close in late august so please
*  don't delay if you'd like to apply for those ones 80 000 hours dot org slash latest all right the
*  80 000 hours podcast is produced and edited by kieran harris audio engineering by ben cordell
*  myla maguire simon monsoor and dominic armstrong full transcripts and extensive collection links
*  alone are available on our site and put together as always by the legend herself
*  katie moore thanks for joining talk to you again soon
*  it is both energizing and enlightening to hear why people listen and learn what they value about the
*  show so please don't hesitate to reach out via email at tcr at turpentine.co or you can dm me
*  on the social media platform of your choice
