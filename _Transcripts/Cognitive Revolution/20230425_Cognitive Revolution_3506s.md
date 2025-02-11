---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3506s
Video Keywords: []
Video Views: 2101
Video Rating: None
---

# How AI Agents Will Change How We Work with Matt Welsh of Fixie.ai
**Cognitive Revolution "How AI Changes Everything":** [April 25, 2023](https://www.youtube.com/watch?v=MHmd8hmpUMA)
*  And if you think of like a 2D plane, one axis is what you just described.
*  It's that idea of is it being used in line with a human versus being basically fire and forget.
*  You give it a task, you give it a job to do, and it goes off autonomously and executes.
*  I think the other axis here has to do with interpreting and synthesizing natural language
*  on one side and automating process on the other.
*  Let's address the elephant in the room, which is the, you know, there's a very real concern
*  amongst many people that AI based automation ends up putting people out of work.
*  I think that this is something that we're going to have to wrestle with as a field,
*  that things that we've been doing by hand are going to become obsolete.
*  You know, you don't have to look very far to see the black and white photograph of a room
*  full of accountants hunched over their ledgers and their, you know, mechanical calculators
*  doing things that a single spreadsheet could do today.
*  Hello and welcome to the cognitive revolution where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Before we dive into the cognitive revolution, I want to tell you about my new interview show
*  Upstream. Upstream is where I go deeper with some of the world's most interesting thinkers
*  to map the constellation of ideas that matter.
*  On the first season of Upstream, you'll hear from Mark Andreessen, David Sacks,
*  Balaji, Ezra Klein, Joe Lonsdale and more.
*  Make sure to subscribe and check out the first episode with A16Z's Mark Andreessen.
*  The link is in the description.
*  Hi everyone. Our guest today is Matt Welch.
*  He is the founder and CEO of Fixie.ai.
*  The automation platform for large language models that invites you to build natural language agents
*  that connect to your data, talk to APIs and solve complex problems.
*  While the technology world's attention has turned en masse to AI agents over just the last month,
*  Matt has been thinking about AI for much longer and building AI agents specifically for just over a
*  year. Citing as inspiration Google's early demonstration of LLM tool usage in its January
*  2022 Lambda paper, Matt, who is formerly a Harvard computer science professor and a 10-year
*  principal engineer at Google, has assembled an all-star team with the goal of driving process
*  automation for enterprise customers with AI agents.
*  You can see how they're going about this online at Fixie.ai.
*  The platform is currently in developer preview mode, which means that developers can build
*  whatever agents they want and end users can try any and all of the agents built by the community.
*  The chat style interface will by now be quite familiar and you can literally just tag agents
*  like you'd tag a teammate in Slack. Each agent is designed to do a different job for you.
*  While these agents in general are not super sophisticated just yet, and there are all sorts
*  of authentication, access, and security issues still to be worked out, if I had to bet right now
*  I'd say that agents will become one of the main ways that AI impacts and ultimately shapes the
*  world over the next few years. It's already clear that AI can do valuable cognitive work,
*  but as long as human users have to figure out how to route information to and from AI,
*  process automation in many contexts will be bottlenecked by implementation.
*  Agents hold the promise of handling not only the core cognitive work, but many of the messy
*  implementation details as well. The searching and finding, the sorting through and scanning,
*  the signing in and navigating of websites, the reading of documentation and using of APIs.
*  In short, all the ad hoc routing of information for which we today act as human plumbing.
*  I see no reason that this won't ultimately work. Both reinforcement learning and all sorts of
*  supporting tools and frameworks seem very well suited to overcoming the challenges at hand.
*  But while I'm quite sure that the agents are coming, likely with very visible progress by
*  the end of this year, I really don't know how this plays out. There are just so many ways that
*  the world will inevitably change in response to the introduction of agents, and agents will
*  interact not only with humans and existing software systems, but also with each other.
*  The dynamics here seem extremely hard to predict. So with all that in mind, I was really fascinated
*  by this conversation. Matt had extremely insightful thoughts on a 3D conceptual model
*  for understanding different modes of human AI interaction, as well as the challenges of
*  security and memory for AI agents. What sort of systems and infrastructure agents will really need
*  to go mainstream? Whether embeddings might create a privacy preserving communication medium for agents?
*  Why Matt believes in Apple's vision for inference on the edge? What sort of ambient interface
*  we're likely to use to interact with AI agents? And much more. Matt, as you might imagine, is
*  extremely busy. He had a client call that limited our time together to just an hour. But if you love
*  this episode as much as I did, we'd love to see your review on Apple podcasts, and maybe we'll
*  be able to convince Matt to come back in six months or so to check in on AI agents' progress.
*  Now, I hope you enjoy this conversation with Matt Welsh of Fixie.ai.
*  Matt Welsh, welcome to the Cognitive Revolution. Thanks for having me.
*  Really excited to have you here. The energy is at a peak right now, a fever pitch around this concept
*  of AI agents. And you, as the founder and CEO of Fixie AI, are right in the center of that.
*  Your company just announced the $17 million seed round, which has a little bit of a,
*  like, I don't know, 2021 sort of fundraising vibe to it. And then the world is kind of hitting
*  this moment of awareness, curiosity, fascination with obviously a lot of debate around AI agents
*  as well. So let's start off by just getting your perspective. What has it been like to be you
*  over the last couple months? Yeah, it's been bananas. The world is moving so fast here. And
*  the way I kind of think about it is, think of large language models like chat GPT as this alien
*  technology that just landed in our backyards. And everyone is now picking it apart and trying to
*  figure out what they can do with it. And they're finding that it's really remarkable in terms of
*  what's possible. And so chat GPT, you know, you mentioned the funding. The way I think about it
*  is chat GPT kind of chummed the water, as it were, to get so much interest from investors looking for
*  opportunities in the space. And we just happened to be in the right place at the right time,
*  I think, because we had been working in this space for a while before chat GPT came out. And
*  then all of a sudden, it just, you know, burst onto the scene and everybody's talking about it.
*  What were the models like when you started? I'm always kind of fascinated by this foresight that
*  certain people have seemed to demonstrate. I think it's, you know, really important and only
*  getting the the alpha on foresight is only getting higher and higher as the future comes at us faster
*  and faster. So, you know, going back even just a year, we're kind of in like early instruct GPT.
*  Was it like instruct GPT that you were seeing and saying, like, I can build a platform on this?
*  Yeah, not even I think, you know, we were in the kind of early days of GPT three. And at that time,
*  GPT three was not really fully a thing that people were building companies around. There were a few
*  Jasper dot AI being one of them, but it wasn't yet being used as a mechanism to drive automations or,
*  you know, access to custom data, access to external tools that that idea was kind of starting and
*  open source projects like Lang chain started building out some cool demos around that.
*  We were mainly inspired by the original Lambda paper from Google that showed that if you gave a
*  language model some the right kind of prompts and taught it how to call out to an external tool
*  to fetch external data that you could use that to drive interesting processes. And there just
*  weren't very many papers about that topic at the time. So that one was relatively new. And we
*  started building around that using GPT three. I think really what happened here was, you know,
*  chat GPT. Yes, there were certainly model improvements between GPT three and GPT three
*  point five. But it was popularizing that idea that changed everything. Right. It went from that
*  kind of clunky playground environment in behind open eyes, you know, developer website to a more
*  consumer focused user experience. And I think that speaks volumes of the power of just having that,
*  you know, end user experience dialed in just right that you could have done most of the things with
*  chat GPT with GPT freeze playground, but just nowhere near as elegantly and and usefully.
*  I'm really trying to figure out where I where I understand agents to be in this kind of
*  you know, fast evolving mix of usage patterns. So let me try on this theory for you. And I want to
*  hear, you know, how you would correct me. I've been kind of talking about AI usage as like
*  co-pilot mode on the one hand, and then what I have been calling delegation mode on the other hand,
*  where co-pilot mode is like you are doing stuff, you are driving and you are, you know,
*  pursuing tasks, you know, pursuing goals. And you've got this kind of helper that's there on the
*  side, you can kind of like, ask to like, you know, draft something for you or answer a question or
*  do a little analysis. But it's kind of, you know, at your like immediate beck and call. Whereas I
*  had been thinking of this delegation as like, more, I think maybe I, you know, should have a
*  more process automation kind of framing for it, because it's kind of has been like,
*  there's this AI that can do these cognitive tasks that previously required humans to do.
*  And now if we can just build the piping, then we can like start to automate and scale some of those
*  tasks in ways that were previously impossible. And you can see, you know, we can imagine a million
*  of those. And now agents have come onto the scene. And I kind of see it almost as like a bridge where
*  it's like, you can sort of stay in like, your own human pilot mode. But you have like access to this
*  delegation mode where you can say like, I want to kind of not just ask you questions, but carve off
*  distinct things and send them to you. And you need to be able to figure out the plumbing, right? I
*  guess that's kind of the key flip is like, I'm not going to sit there and architect a system. I want
*  you to figure out what buttons to push. I think that's right. So yeah, my view is, is that there's
*  two dimensions. And if you think of like a 2D plane, one axis is what you just described. It's
*  that idea of, is it being used in line with a human versus being basically fire and forget?
*  You give it a task, you give it a job to do, and it goes off autonomously and executes. I think the
*  other axis here has to do with interpreting and synthesizing natural language on one side.
*  And automating process on the other. And so, you know, the early generation of AI applications
*  were largely about taking in language, manipulating it, spitting out language. So Jasper being a good
*  example where you gave it a description of your product or the blog post or whatever marketing
*  copy you wanted. Jasper took that in and then synthesize something for you. On the automation
*  end of the spectrum, you start getting into things where you're using the language model kind of like
*  a computer that you program in English. And that computer is capable of doing extremely rich and
*  sophisticated kinds of symbolic manipulation, not just on natural language provided by humans,
*  but also on things like, you know, like a JSON object or contents of a spreadsheet or an XML
*  document or something else. And so if you think about that axis, I think you could pick almost
*  any point in that space and identify potential use cases and kind of existing systems that are
*  built up around that. So, you know, Jasper being very hard on the natural language processing side
*  and more in the kind of copilot quadrant that you're describing. With Fixie, where we're trying to go
*  is probably down in the opposite end of that spectrum, which is more about autonomy and
*  driving process automatically and also doing so in a way that doesn't need to be a live interaction
*  with a human. It can be, it doesn't have to be. So that's generally the way I've been thinking
*  about it, but I think that's a good framing. Yeah, I love it. Add a dimension is always a great way
*  to level up. So that's maybe one of the best questions and answers we've had on the show.
*  Honestly, I think that's really makes a ton of sense to me and I'm going to continue to
*  test some ideas against that, that 2D framework. You know, let's get into maybe a few of those
*  points. I am advising a company right now called Athena, which is in the executive assistant
*  services business. Their model is that they hire individuals in the Philippines.
*  They have, I believe a thousand active EAs working one-on-one with executive clients,
*  most in the U.S., but also elsewhere. Clients very widely, they have a lot of training and culture
*  and kind of stuff built up, but then each client is its own unique adventure. So it's extremely
*  kind of diverse, obviously a lot of commonalities, but a ton of long tail.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omnike so
*  much that I invested in it and I recommend you use it to use Cogrev to get a 10% discount.
*  So our goal is to become, and this is kind of, you know, my mission statement, right? Help us become
*  the EA company that is the best in the world at adopting AI tools. Please do my job for me,
*  and pick out some of these points in space perhaps and help us kind of like get more tangible about
*  how you envision work changing to delegate more of these things to the process agents that you're
*  creating. Yeah, I think there's a bunch of places in the space where this makes a lot of sense.
*  And I mean, first of all, let's address the elephant in the room, which is the, you know,
*  there's a very real concern amongst many people that AI based automation ends up putting people
*  out of work. I think that this is something that we're going to have to wrestle with as a field,
*  as an industry. In most cases, I don't think it's true. In some cases, it may well be true
*  that things that we've been doing by hand are going to become obsolete. You know, you don't have
*  to look very far to see the black and white photograph of a room full of accountants
*  hunched over their ledgers and their, you know, mechanical calculators doing things that a single
*  spreadsheet could do today, right? But anyway, coming back to the point about automating things
*  that an EA could do, I use a, I have an EA through a company called Double, and I can absolutely see
*  lots of opportunities for automating things. I think one side of it is, of course, generating
*  appropriate written content. Like that might be an email reply, or it might be a request to schedule
*  something, or it might be, you know, a newsletter that gets sent out to a group of individuals.
*  This is not always something that people have great training in being excellent community written
*  communicators. And especially if you get outside of, you know, countries where people are native
*  English speakers, they're not necessarily going to have the same level of skill there. And this is a
*  place where I think AI can help tremendously, right? On the other side, more on the process
*  automation, there's so many things that I know I do very mechanically and repeatedly that I believe
*  can and should be automated. And the only thing that we're kind of lacking today, I mean, the AI
*  models could automate it, but the AI models are lacking the appendages into your systems to make
*  this easy to do. So to give a very concrete example, you know, as a CEO, probably 70% of the
*  email that I get is people trying to sell me things that I don't need right now. And that might be,
*  you know, consulting services or, you know, recruiting services or, you know, some kind of
*  new bank account or whatever it is. A lot of my time has been spent drafting or sending out,
*  you know, polite replies to these people. And you could ignore the email completely. The problem is
*  then you get 5, 10, 20 emails from them and their automation flow and they keep bugging you and
*  following up. And so it's easier, I've found just to spend a minute or so to respond to them.
*  But the problem is that you can't tell whether or not an email is in that category until I kind
*  of sit down and read it. And it feels to me like that's another place where just categorizing
*  inbound email or other types of communication should be an automatable process. Now today,
*  my EA does that, right? He reads my email and puts it into different folders and often replies to
*  those things. But again, this is a very laborious process and it feels like something that we should
*  be able to use AI to automate. So that is a very top of mind example for us as well.
*  At Athenia, they call this pre-drafting and they've created significant training,
*  all this kind of stuff around it. And I think some, you know, the clients have to be pretty good at
*  systematizing for it to really lock in. And I personally, I actually started as a client.
*  So that's the way I got introduced to the company. The email drafting never quite got there for me.
*  There were definitely things that I was able to delegate that were like routine
*  calendaring and that kind of thing. But then there are some things where it's like, yeah,
*  nothing really wrong with what you're saying, but it's not quite how I would want to respond and
*  a bit of a hard time getting over that gap. And then I think AI is also going to have a bit of
*  a hard time getting over that gap, but it's maybe a different sort of hard time. So you kind of
*  mentioned the appendages and this gets to the deep dive that I kind of want to go on with you
*  around the different appendages that these systems are in need of and kind of what they're
*  going to look like. I'm thinking access is obviously just one real important one. It doesn't
*  seem to me that we're going to get to the point where few shot, here's two emails that this person
*  wrote in the past. Now you can kind of cover everything. You're going to need to be able to
*  go a little deeper than that. Access, you could also kind of tie to memory, although that's kind
*  of distinct too, because your memory may include your interactions with the system as well as kind
*  of the email database that existed before the system. But those both seem pretty hard and kind
*  of unsolved problems right now. So maybe let's just start with those. How do you guys think
*  about security? To me, it seemed just like an absolute hornet's nest of pain, but it is one of
*  your core selling proposition. So let's start there. I went on the Fixie platform, by the way,
*  and already, interesting bit of user feedback. I was comfortable giving the at Fixie slash
*  G calendar access to my calendar and playing with that. But then I saw the at busy executive hackathon
*  user who had the Gmail assistant. And I was not going to authorize that one. There's also an
*  interesting intersection with your marketplace concept. But I'm talking too much. Tell me,
*  security, how are you guys thinking about that? Yeah. So what you will see in Fixie today is we've
*  opened this up as a developer preview. And we've kind of intentionally said, hey, this is a free
*  for all. Let's just let people build things, bring them in, show them off, integrate them with other
*  people's agents and tools and workflows and see what happens. And we know that this is not really
*  the right model. This is not the model that makes the most sense for our enterprise customers. But
*  it does reveal a lot of interesting potential use cases. And so in a lot of ways, the throwing
*  caution to the wind and letting people build has been the first priority. Going into an enterprise
*  situation, though, you're certainly not going to want to just kick up a natural language agent
*  that some rando on the Internet put into the system. You're going to have to make some decision
*  about whether this is a good thing for me to integrate, whether I trust it and so forth.
*  And that, by the way, we're used to making those decisions. We make those decisions all day long.
*  We're using Riverside to record this podcast. I use Zoom. I use Google Meet. I use Google Calendar.
*  There's all kinds of trust relationships there that one has to have with their data when they're
*  doing those integrations. You know, I've plugged countless things into Slack that understand,
*  you know, my Google Drive contents and my calendar and so forth. So I feel reasonably confident that
*  there's a pattern for people to develop an intuition around where they want to place their trust.
*  Most enterprise customers, I think, are not going to be wanting to draw too much on these
*  third party integrations. They're largely going to be looking at building their own integrations
*  where they say, OK, we this is a natural language interface to our data, our tools, our APIs.
*  We built it in-house. We know where the data is flowing. We know what's happening with it
*  and we can build it into our own workflows. And so that's where we've been focusing most of the
*  work is on that developer experience. Coming back to the security question, though,
*  it's very clear that people don't yet have a good sense of how to think about where is the data
*  flowing when I'm using an AI powered application. Right. So let's imagine I build an agent that
*  slurps up my internal company notion website that has all of the information about everything
*  that's going on in the company, you know, proprietary stuff and confidential stuff and
*  so forth. Now I can take that agent and ask questions of it and I can say, you know,
*  what is the latest on this project? And it can go and pull out the relevant context from the
*  notion pages and answer that question for me. Well, what's going on here? Right. Well, first of all,
*  the query from the user has to route out to a language model. Where is that language model?
*  Which language model? Who's got access to it? Right. Secondly, the, you know, the query goes
*  into, you know, some kind of vector database or something that's pulling out the relevant snippets.
*  Again, who runs that? Where does that live? Where does the data live? You know, how can I delete
*  what's in there? Right. Third, what happens to the history of the query conversation? Where does that
*  live? The point being that there's a lot of pieces involved. And many of those pieces today are
*  third party things like we primarily use the open AI language models, although you can use other
*  things like entropics model and so forth. And, you know, if you're using an external vector database
*  like pine cone, then, you know, that's another part of the, you know, the software supply chain. So
*  we're going to have to solve this problem in a really, you know, explicit way for
*  enterprises that care so much about where the data is flowing and also have, of course, regulatory
*  compliance requirements around that. The good news is, though, I think that there's a good pattern
*  for doing that. Plenty of companies have built SAS products designed for enterprises that address
*  that kind of thing. And we just need to figure out how to do that as well. The biggest gap today for
*  us is the existence of language models that are really good that we can host in our infrastructure
*  and kind of put behind that firewall, if you will. Calling out to open AI is not ideal for a lot of
*  enterprise use cases, although there is the open AI service from Azure that addresses many of them.
*  So, you know, my expectation, though, is open source models are coming fast and furious. We've
*  seen even just this week, I think, two more exciting open source projects. There's the red
*  pajama thing and then Stability AI just announced one today. So my expectation is that we're going
*  to see an onslaught of these that give us that freedom to go and deploy our own models and not
*  have to rely on third-party providers. I want to think a little bit about, like, new threat
*  models as well, because there's the kind of data flowing from, you know, your server to open AI and,
*  like, their terms of service and whether you trust them to not leak the data somehow and not
*  get hacked on their side. All that stuff, yeah, I think mostly fairly conventional should be,
*  you know, I mean, we're a mess. So it's not like it's going that well today. I would say nobody I
*  know is like, you know, it's in a great state, is like web security. But yes, we get by. But there
*  is this kind of new paradigm as well that's like, is the model itself hackable or, like, subject to,
*  you know, misbehavior? And then what is it going to encounter in the wild as I send it on its way?
*  You know, we've seen these, like, super, like, foreshadowing, you know, kind of examples where
*  somebody puts a hidden message into the HTML website and then, you know, that actually does
*  have an effect on search that can be, like, quite a left turn. And, you know, people are very savvy
*  and very clever with this kind of thing, right? So the internet remains undefeated on that kind of,
*  you know, what can be exploited, like, you know, somebody will find and exploit. So I'm really
*  interested in just how you think about all that kind of stuff in general, too. And then specifically,
*  like, on the language model, Open AIs versus yours, I've had this theory that, like,
*  with 3.5 turbo getting extremely cheap and probably pretty good at, like, a lot of these
*  kind of core tasks and also, you know, the turbo reflects the speed that people might just kind of
*  start to see that as a standard and be willing to pay for the overall package of, like, convenience,
*  speed, quality, safety, like, they've got their whole red teaming infrastructure that is going to
*  be, you know, you can't possibly match that on, like, you know, whatever Stability just put out.
*  And I think they actually also do a pretty good job. I'm in their Discord and follow that. So,
*  you know, I think we're fortunate that Stability has put real thought into it as well. But, like,
*  hard for you to know exactly what, you know, the SLA, so to speak, you know, of safety for a
*  Stability, you know, open source releases. So how do you think about all those kind of unknown
*  unknowns and then, like, whose problem do you want those unknown unknowns to be?
*  I think that's a very good question. And it's something that it's such early days, I don't
*  think that the industry understands this very well at all. Right. You know, it wasn't that long ago
*  then that, you know, prompt injection attacks were all the rage and people were, you know,
*  digging into how does chat GPT work and what are the prompts that it, you know, that it uses and
*  then, you know, undermining those and getting chat GPT to adopt, you know, kind of evil persona
*  based on, you know, what somebody wants to get the thing to behave in a crazy way.
*  These are certainly going to be challenges, right? This is this is not at all a solved problem.
*  I have two takes on this. I think the first take is there's so much value to be brought today,
*  even in situations where confidence in the absolute safety of the model is low.
*  And many of those are coming out in situations where there's going to be a human in the loop
*  anyway. And so the amount of damage, so to speak, that an AI model that's misbehaving can perform is
*  fairly limited. So in the case of, you know, drafting an email, well, again, if it's a draft,
*  and the person who wants to send the email is going to be reading it first, then there's only
*  so much the draft could have gotten wrong, right? That there's a natural speed bump there,
*  if you will. So I think that there's a ton of value in use cases where there's already a kind
*  of built in check on that. But going forward, as we want to embed language models deeper and
*  deeper into our tech stack, we're certainly going to need to have appropriate safety mechanisms in
*  place. And this is a really active area of research. It's not obvious to me exactly how
*  we're going to achieve that goal. And some of it's certainly model fine tuning and red teaming it and
*  things like that. But I also have a feeling that we just need to put other software mechanisms in
*  place around and on top of these models to prevent them from taking actions that we don't expect.
*  There's an exciting project that I was just checking out a few days ago called Guardrails.
*  And this is from Shreyya Rajpal, who has worked at Apple. And this is a project that is effectively
*  allows you to write a spec that captures the semantic requirements of the response of a
*  language model in a certain situation. So to give an example, if I'm building an agent that is meant
*  to respond to questions about the weather, I can write a guardrail spec that says any response
*  from this use of the model needs to involve the weather in some way. It can't just be about any
*  arbitrary thing. And you can place other requirements on it. For example, the temperatures
*  that it responds with have to be within the range of what one would expect from this area of the
*  world. Or it can't report crazy kinds of numbers in terms of rainfall amounts that make no sense.
*  With those kinds of things in place now, when the model responds in a certain way,
*  guardrails can then interpret whether or not the model seems to be operating within its spec,
*  so to speak. And of course, there's problems with this. This is not a panacea. There's ways of
*  breaking that as well. I could have subtle ways of breaking the model so that it always
*  reports things in Fahrenheit instead of Celsius or whatever the thing is. But it feels like a very
*  good step in the right direction to building out software infrastructure to do this. The other
*  interesting thing there is I believe that there's a big opportunity to develop tailored models that
*  are explicitly designed only for the sake of validating responses from other models.
*  In other words, I don't need a full generative model that can spout a children's story or
*  something about Shakespearean literature in order to do this. I can have a much smaller, cheaper,
*  faster, and also heavily, heavily, heavily task-tuned model that's job is to basically take in
*  a set of requirements and give me a score, says, does this response match the set of requirements?
*  This was a weather agent. Did it answer about the weather, yes or no? And that seems like something
*  that language models will be very good at and we should be able to do.
*  Yeah. Okay. I think that all makes a ton of sense. I see shades of Eric Drexler's
*  comprehensive AI services and you also channel a little bit there, Imad, with his million small
*  models paradigm. And the guardrail thing sounds awesome too. I definitely will want to check that
*  out. That to me, I was thinking that sounds like a moderation endpoint. I've even speculated that
*  that could be a new technique that GPT-4 might be applying as some sort of semantically defined
*  loss as opposed to a pure next token loss and a semantically embedded style validation.
*  Constitutional AI, that was the other thing I was going to say. It's like a moderation endpoint
*  slash constitutional AI paradigm. So the ability to set something like that in a semantic way and
*  then have this kind of, yeah, guardrails, that sounds brilliant. Cool. Well, again, great,
*  great, great stuff there. I guess maybe next thing is memory. We're seeing, again, a wide range of
*  approaches where what I see on Fixie today is pretty episodic. Maybe there's a third dimension
*  also of our previously 2D space that's like, how long lived is the agent or interaction?
*  Because a search query can obviously be kind of often answered in just a quick generation and
*  you're done with the agents on Fixie. I'm having some conversation and going back and forth.
*  And then we're seeing towns of people having whole days of lives and reflective, synthetic memory.
*  So how are you guys thinking about that? That spectrum from the goldfish to, in theory, this
*  kind of knows you better than anyone, lifelong AI companion. Yeah, no, it's a very good question. So
*  in Fixie, there's a notion of what we call a session. And a session is just think of it as
*  the conversational record between some end user and some set of agents. And any number of agents
*  could be involved in a session. So I might use a session to, you know, fetch data from a database
*  and then massage it in some way and then call out to another agent to make a visualization or
*  something like that. So you can think of these sessions as kind of an append only
*  log of the conversational history. And of course, the content in a session itself provides context
*  to the agents when you're using it. So for example, if I said, you know, make a pie chart
*  showing me the top 10 contributors to this GitHub repo by number of commits. So we'll call out to an
*  agent, fetch the data from GitHub, call out to another agent to generate a pie chart.
*  Then if I just say, make a bar graph instead, I don't need to spell out the whole thing. I just
*  say make it a bar graph. Then because the context is there in the session object, that ends up
*  translating into make a bar graph of the top 10 contributors to this repo and so forth.
*  So the way we've been thinking about sessions to date has been that they're largely ephemeral
*  and they're largely meant to be used for, you know, the kind of few rounds of conversational,
*  you know, interaction between a human and the machine. But there's no reason they need to be
*  limited in that way. Right. And so one could imagine having kind of perm a session, if you will,
*  that is constantly going on for you and all interactions that you have with any aspect of
*  the system. Right. And so that forms the memory, if you will. And then, of course, we need mechanisms
*  to ensure that that memory is then fed into the downstream agents in the right way so that it can
*  be consulted as necessary. And that's roughly what things like auto GPT and baby AGI are doing.
*  So the short answer is this is pretty easy to do with fixie, but fixie isn't currently
*  focused on that. We do think that's going to be an important use case.
*  One of the biggest things that people are going to be concerned about there is privacy. Right.
*  And just like the problem that you have where, you know, you make a mistake and click on that shoe
*  advertisement on CNN one day, and now for the next three weeks, you're seeing nothing but shoe
*  advertisements all over the web. Right. You want to avoid a situation where someone
*  inadvertently poisons their memory with something that really is irrelevant to
*  whatever they're trying to use the system for. And that ends up kind of causing it to veer off
*  course or just become less relevant to them over time. And so I think there's going to be
*  an important need for some kind of semantic clustering of that history. You know, a
*  segmentation, if you will, so that if I'm interacting with the system in a work setting,
*  OK, I use one kind of kind of history. If I'm doing it in a personal setting,
*  I use another kind of history. You know, the way I solve that is I have two different
*  Chrome profiles, one for work, one for personal and never the twain shall meet. I never look at
*  personal stuff in my work profile and vice versa, because I want to avoid those two,
*  uh, you know, sessions effectively intermingling.
*  I guess I'm interested in whether you think for now the sort of long term version is just like
*  not what your target enterprise customers are looking for, because that could definitely
*  make a ton of sense to me. You know, you think of like trying to bring this kind of technology
*  to bear in customer service and it's like, let's just get a single call. Right. You know,
*  we can do that. We're winning and we can we can we can build on that. Right. Versus like we don't
*  need long term companions for our customers. That's really it. And most of the use cases
*  that we're seeing don't have a need for permanent history. There is an affordance in fixated day to
*  to record things for later consumption. So, for example, an agent could say I want to stash away
*  this piece of state or this text or this information about this particular user so I can
*  consult it later. And that ends up being used in a lot of places, but it's an explicit action as
*  opposed to implicit just, oh, through the nature of our conversation, I remembered this information.
*  The other thing that's important about it is that it has to be segmented by the end user,
*  that you do not want to be in a situation where an agent is, um, you know, answering questions
*  about someone else's order in the in the in the process of handling a single customer ticket.
*  So I think it's a combination of those. But we do think that there's going to be a need for this
*  kind of permanent history or maybe semi permanent history in the world of building agents that are
*  more autonomous. So if you look at the auto GPT stuff, effectively what it's doing is, you know,
*  using the history as a way of itself figuring out what to do next. And that doesn't need to be like
*  a permanent history that doesn't need to be full AGI with a permanent memory in order to be effective,
*  but it does provide a great deal more context for them to guide the model's operation. And that's
*  something that we want to make sure we do provide in fixie. So going back to my kind of assistant
*  use case in a in a world where we have like these very episodic, you know, kind of ephemeral session
*  style agents, presumably coming online and like working well first, then I can sort of see the
*  like human assistant plus AI assistant being a very natural paradigm. But it does seem like
*  that longer term memory, you know, starts to mature into form as well. So what do you kind of think is
*  the future of, you know, how what does a human assistant look like in a year, you know, or two
*  years as these kinds of tools start to come online and like, maybe even just more broadly than that.
*  I mean, I'm thinking hard about that. But I'm also just like, what does the individual just everyday,
*  you know, computer users experience start to look like? What do you think it's going to look like to
*  sit in front of a computer two years from now and do stuff? Or even six months from now, I think is
*  probably the more relevant question. I mean, you know, we're seeing all kinds of just incredible
*  things that people are starting to build. There's a product called Ember that acts as a kind of a
*  natural language agent that's embedded into my desktop environment on my laptop. There's one
*  called Multi on that's embedded into my web browser. And as soon as you have these things,
*  and they're not just responding to explicit queries by a user, you know, invoking the hot
*  key and typing, you know, show me a bar graph of this thing. But they're actually paying attention
*  to everything that's going on. Right. I often joke that, you know, my laptop here, my little MacBook
*  Air, this is the entire company fixie in this little tiny package. I mean, everything for the
*  company that I do is right here on this machine. And so that's all the email, all the zoom meetings,
*  all of the, you know, documents, all of the code, everything is here. So there's no reason that
*  an AI agent can't effectively have access to the full state of everything happening in my entire
*  work life. And probably most of my personal life too. Right. So the question then becomes,
*  what does that autonomy look like? I think because what you're speaking about is not just a person
*  asking for help with something and then kind of getting an answer. It's more of an autonomous or
*  a proactive process that's happening based on my, you know, the knowledge of what's going on in my
*  life. And so, you know, we've seen little bits and pieces of that. You know, my favorite example,
*  just in day to day use is things like, you know, using Siri to give me a reminder. You know, I
*  can't remember anything in my old age. So I'm constantly asking my phone to remind me of things
*  that I need to do in a couple of days or a week or whatever. That's such a trivial one though,
*  because it feels like in the future, the machine should just know that you've got to deal with this
*  thing or it's got to remind you that you need to take action here. And so the place where I think
*  it all needs to come together is first of all, a beautiful, streamlined and cohesive user experience,
*  just like my point earlier about chat GPT. Certainly there were ways of doing chat GPT before
*  chat GPT came along, but nobody did it because it was just, you know, too clunky. So the streamline
*  user experience is essential. One can make the same argument about the web, right? We had hypertext
*  before there was the web. It was called gopher and it was awful. It was terrible. But it, you know,
*  conceptually was the same thing. It just wasn't presented in the right ways. Right. So I think
*  we need to have that streamline user experience. I think the second is there really needs to be a way
*  to connect an AI system to all of the personal information that you're comfortable giving it,
*  that there needs to be a clearinghouse for that. Right now it's way too fragmented. And, you know,
*  what I am looking at in my web browser and what's on my calendar and what's in my email and,
*  you know, what's happening in my text messages and what's happening on Twitter are all different
*  places and they're all, you know, completely separate from each other. And for an AI to help
*  use any of that information, it needs to really have the same level of access to all that that I do.
*  And so that kind of comes back to your point about delegation.
*  Obviously that needs to be done in a way that is, you know, highly transparent, something that
*  users can really trust, they can control, they can revoke the access anytime they want. And by the
*  way, I think it needs to be personal. By personal, I mean ideally running on your own device.
*  I'm not sure that people are going to be comfortable with giving access to every single
*  thing that you're doing in your digital life to Google or Facebook. Now people might argue,
*  well, but we already do. Right. But we're doing so in a way that we're not necessarily aware of it.
*  And so, you know, I used to be on the Chrome team at Google and, you know, Chrome effectively
*  is able to keep tabs on everything you do on the web, every website you visit, every link you click.
*  And most people aren't aware that that's happening. You can turn it off, of course,
*  but that's just kind of the default behavior. And the reason they're not aware is that they don't
*  tend to surface that information in their own day-to-day lives. There's a history tab buried away
*  somewhere in Chrome that you can go see that stuff. But because it's not something I'm interacting
*  with, I can kind of just ignore the fact that it exists. So those, I think, are the three main
*  things that have to come together is the user interface, the clearinghouse for your data,
*  clearinghouse for your data, but also really the transparency and the control over it.
*  Once somebody builds that, and I don't think that's very hard to build,
*  I think we're going to be off to the races and enabling people to leverage AI in a really
*  meaningful way. Yeah. The sort of single sign-on or like, you know, log in with Facebook, log in
*  with Google, but be able to bring your sort of embedded content. A lot of things right now are
*  leading me to this idea. This is a very kind of immature idea. A critic might even say it's a
*  half-baked idea. But I keep coming back to this idea of like, bring your own embeddings
*  as maybe how a standard kind of gets set. It seems like the sort of abstraction and maybe some like
*  cryptographic layer on top of that as well could allow you to kind of never even share the raw
*  information, but still give like semantic access to applications in ways that could be really
*  useful. That's a fascinating idea. And it's not one that I've thought about. It bears some similarity
*  to some of the work that's been done in federated learning where you're able to train models that
*  operate on data from the collective, although it's a different approach, right? I like this idea a
*  lot that it, you know, effectively leveraging the embeddings is really almost a one-way function.
*  From something that you've done down into this vector space, but you can't really go the other
*  way. You can't necessarily go the other way. Although I'd guess you could probably reverse
*  pretty well. Today you can. Today you can. But the question is, could you effectively,
*  and I believe that there has been some research in the space of effectively, you know, taking the
*  embedding vector that can be generated through a language model and applying a one-way function to
*  it such that you can still perform nearest neighbor retrieval against that, but you can't go backwards
*  from that transformed vector into, you know, the original content of the original context.
*  And that seems, unless you, you know, grant access to do that, for example. I think it's a
*  fascinating idea. I do think that some of these techniques will be important. I think, I don't
*  think the world will be willing to wait for that. In other words, I think time and time again,
*  we've seen that, you know, new technologies take off well before the world is ready from a security
*  and a privacy perspective. I mean, look at the web. When the web started, there was no HTTPS. There
*  was no SSL, right? Everything was being done in clear text for many, many, many years. And it took,
*  and once SSL came along, look how long it took to actually get all these websites to start adopting
*  it. And so I think that we're going to end up in a place where people are happily granting the
*  Facebooks and the Googles of the future, the access to all of their sensitive data with the
*  belief that they're getting value from it, for sure. I did work at Apple for a time, and Apple has,
*  I think, a really interesting perspective on this, which is all else being equal. They want
*  everything with your personal data to only live on your device. They don't want access to your
*  personal data. And yes, there are things like iCloud backups and so forth, but they're not
*  trying to mine the personal data. They're actually trying to develop the power on the end user device
*  so that all the processing can happen there and all the storage can happen there. And I think that
*  it holds them back, certainly, the ad targeting and other things that one would like to do
*  is not going to be as good, but I think it's ultimately where the world will end up. And I'm
*  glad that they are focused on that. Yeah, it certainly might end up looking extremely
*  prescient, especially as bundled with the heavy investments in the chips that can actually make
*  it go on the edge. So on the question of the form factor, what do you think that might be?
*  And could it be like the Apple Glass? If the agents are good enough and then it's natural
*  language interface, you might even be able to just hum to it. Or it's not even too much of a stretch
*  to be like, probably not first released, but just kind of think and have the glass read directly
*  from the neurons into what it's supposed to do. I think it'll look more like the movie Her,
*  the Spike Jonze movie Her, where you're wearing an earpiece and you can talk to it.
*  That seems more likely to be the ambient interface going forward. At some point,
*  we may find that augmented reality glasses are a thing. When I was at Google, I was fortunate to
*  be one of the few people that was able to use Google Glass in the real world outside of the
*  Google offices and use them in a real life setting as a dog fooder. Of course, it never really caught
*  on, but I think in large part because it was not really socially acceptable to be wearing a camera
*  on your face. So if there wasn't a camera, maybe people would say, okay, well, that's a quirky
*  little screen or something. So it's more around the social acceptability. The nice thing about
*  the AirPods kind of UX is that it can be very kind of hidden. It's not something that's just
*  really obvious to other people that I have an AI here whispering in my ear, so to speak.
*  Imagining that, it obviously can talk back to you and then it can show you stuff on the phone.
*  Exactly. And everybody has a phone. You already have the screen. You already have the touch
*  interface. You already have the voice interface. You already have the speaker in your ear. And so
*  to me, that seems like the thing that will ultimately just really take off is that at any
*  time I'm able to ask this thing or even just get proactive help from it in the midst of doing
*  something. I do think that there's going to be a need for textual interfaces for things where you're
*  working on documents or on a screen, a larger screen. I don't think that just the audio
*  interface is the only thing, but if you are thinking about taking it out into the real world,
*  so to speak, that's really where I think it's going. The big zoom out kind of final question,
*  what are your biggest hopes for and fears for society as this AI wave crashes over us?
*  I think the big, there's so many risks in this space and it's kind of hard to know exactly
*  what the downsides are going to be. And I think we're just learning now about all of those risks.
*  In terms of the positives and the upsides, the thing that I'm extremely optimistic about and
*  hopeful for is that AI will enable anyone on the planet to take full advantage of computing.
*  Today, if you want to take advantage of computing, you need to be a member of an elite
*  priesthood that knows how to write code and write programs and or customize or tailor complex
*  pieces of software to do what you want. And much has been said about digital literacy and making
*  computers easier to use, but with AI, you end up with this natural language interface. And it's
*  not just an interface. I think it goes well beyond that to the reasoning abilities of these models
*  and the task execution abilities of these models as we've talked about. So if you think about
*  putting that in the hands of everyone on the planet, and no longer will we have a situation
*  where only the very privileged, only the very wealthy, only the people that have had the right
*  level of education will be able to take advantage of this. And I think that that's going to lead to
*  kind of a second information revolution, if you will. So I'm very excited about that.
*  As far as fears go, you know, I think about my kids, and I think about what they're going to
*  what kind of world they're going to be growing up in. And, you know, there is this fear that
*  the old ways of learning the old ways of gaining skills, the old ways in which you're
*  evaluated in things like school and so forth, are going to, you know, fall by the wayside,
*  and no longer are people going to be evaluated on how effective they are at writing an essay,
*  or how effective they are at coming up with a clever computer program to solve an assignment.
*  And so then it becomes a matter of, well, what are we evaluating for? What is the educational
*  curriculum of the future? And how do we decide who gets the A's and who gets the B's and who gets the
*  C's? And then frankly, how much does that matter? Right? Is that many of these structures have been
*  developed in a world where we needed to grade people according to some kind of in what we
*  believe to be an intellectual measure, but usually is not an intellectual measure. It's a measure of
*  some other properties that are usually not that important. But with AI in the mix, there is just
*  such a change in terms of how the world will be organized. And I don't know what that means
*  for the future. And it's kind of hard to know what the rules are going to be.
*  And so I'd say cautious optimism there, but also a bit of a fear around what that might end up
*  looking like. This has been a fantastic conversation. Matt Welch, thank you for being part of the
*  Cognitive Revolution. Thank you very much. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work, customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it,
*  and I recommend you use it too. Use Cogrev to get a 10% discount.
