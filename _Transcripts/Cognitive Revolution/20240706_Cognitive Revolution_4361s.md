---
Date Generated: July 07, 2024
Transcription Model: whisper medium 20231117
Length: 4361s
Video Keywords: []
Video Views: 609
Video Rating: None
Video Description: Nathan interviews Siqi Chen, CEO of Runway, about revolutionizing business finance through AI. In this episode of The Cognitive Revolution, we explore how Runway is creating an intelligent business operating system that generates financial scenarios and explains complex metrics. Siqi shares insights on AI's future impact on finance, business, and society at large.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST:
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.

Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:02:45) Runway
(00:06:11) AI features
(00:12:10) Defining the syntax
(00:14:48) How AI has been expressed since GPT-3
(00:18:32) When did it become clear that the models were getting good enough?
(00:24:29) Sponsors: Oracle | Brave
(00:26:38) How the model is being asked to generate a scenario
(00:26:38) What will drive the most improvement?
(00:28:50) How Runway can help you make decisions
(00:37:47) Sponsors: Omneky | Squad
(00:39:34) Runway as a business operating system
(00:39:51) How does the product work?
(00:44:31) What does the future hold?
(00:47:34) The frontier model has passed the average person
(00:51:18) AI tools for operations
(00:55:21) How to get the best out of AI models
(01:00:39) How AI models can write as you
(01:02:43) AGI, work, and the future
(01:08:33) AI safety, regulation, and the future
(01:11:26) Closing thoughts
(01:12:20) Outro
---

# Building an Intelligent Business OS, with Runway CEO Siqi Chen
**Cognitive Revolution:** [July 06, 2024](https://www.youtube.com/watch?v=KIvlDHuYK6g)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm speaking with Sikyi Chen,
*  prolific Twitter commenter, active angel investor, and founder and CEO of Runway,
*  a finance platform that's revolutionizing how businesses understand and interact with
*  their financial data through a combination of traditional software and AI.
*  Sikyi's journey from math major to game developer to four-time CEO, including a stint at Sandbox
*  VR during the onset of COVID, has given him a deep appreciation for the pain points of traditional
*  methods of financial planning. With Runway, he's not just building another spreadsheet replacement,
*  he's crafting an intelligent business operating system that can generate complex financial
*  scenarios, explain intricate metrics, and ultimately help all employees understand how their work
*  contributes to the business's bottom line success. In this discussion, we explore how Runway is
*  layering AI onto their product, how they are using AI operationally, how far Sikyi expects
*  AIs to progress in the near future, and what all that implies for the world at large.
*  Sikyi describes Runway's ambient intelligence product strategy, which aims to surface AI-powered
*  insights without users needing to explicitly query a chatbot, the prompt engineering strategies that
*  they're using to present financial and other structured data to LLMs in a usable way,
*  and the reasons that Runway has integrated more than 680 different data sources to date.
*  After that, we get Sikyi's perspective on the possibility of self-improving AI systems,
*  how his AI worldview informs his approach to company building, investing, and even parenting,
*  his expectation that relative status and things provably made by humans will increase in importance
*  and value, and how he thinks at a meta level about which AI scenarios are worth thinking about and
*  planning for, and which are, even if not entirely implausible, simply too crazy to spend time
*  worrying about. If you're finding value in the show, we'd appreciate it if you'd take a moment
*  to share the Cognitive Revolution with friends, or leave us a review on Apple Podcasts or Spotify.
*  Meanwhile, we invite your feedback and your resumes for our experimental private job board
*  via our website, cognitiverevolution.ai, and I always welcome your DMs, whether by email or
*  your favorite social network. Now, I hope you enjoyed this conversation on the application of
*  AI to finance and much more with Sikyi Chen of Runway. Sikyi Chen, founder and CEO of Runway.
*  Welcome to the Cognitive Revolution. Thanks for having me. It's great to be here.
*  I'm excited about this. You are building a company that I think is at a very interesting
*  intersection of problem space that's really important that people have to get right. And
*  you're also building a lot of AI features into that product. I think that's a really interesting
*  place to be right now. So I'm really excited to get into that, get into some of the weeds of
*  what you're building and how you're thinking about that. And then hopefully at the end,
*  zoom out and talk about some of your big picture views. For starters, you want to just tell us a
*  little bit about what Runway is. There's an interesting backstory as to why you decided
*  to start this company and maybe you can start to tee up some of the AI integration points.
*  Sure. Yeah. So at a high level, Runway is a finance platform for the finance team. The main
*  goal is to make the business understandable to not just people inside of finance, but outside of
*  finance too. This seems like a very dry and boring problem, but it's probably the most interesting
*  one I've worked on in my career. The backstory is I've been a four-time CEO and a three-time founder
*  now. My background is in math. I majored in math and I have a technical background. I was never
*  comfortable with business and finance. I never thought of myself as any kind of business person.
*  As my career progressed over all of these companies, I felt increasingly insecure about
*  that identity. And this came to a head when I was appointed CEO of a company called Sandbox VR
*  shortly before COVID hit. And when it did hit, we had to do all kinds of scenario planning on
*  these spreadsheets. What these spreadsheets do is, you know, probably heard of the term of financial
*  model before. And not only is that used by investment bankers on Wall Street, but it's also
*  more importantly used by CFOs and founders who run companies. And what these things do is they
*  are a simulation of a business. It basically lets you time travel in the future and understand the
*  implications of the decisions you make today about how much money to raise, how to change pricing,
*  how much to spend on marketing, how many people to hire. And so when COVID came to a head,
*  we had to scenario plan for how long COVID is going to last. Is it going to last three months,
*  six months, 12 months? And we're doing them on these spreadsheets. And long story short, we had
*  to lay myself off and most of the company went from 400 some employees to basically around 10 or so.
*  And the founder hibernated the company over COVID. Shortly after that happened, literally half an
*  hour, I was talking to both our CFO and then the Andreessen team who invested in Sandbox.
*  And I asked them, like, surely there's something better we could have used for this problem to,
*  like, scenario plan and see what's going to happen with COVID. Because Figma exists and Notion and
*  we have all of these great products, surely there's something that is intuitive, understandable
*  for the business itself. And I was surprised to learn that actually wasn't anything better
*  than just simply using a spreadsheet, which is amazing, but also like it can do everything.
*  So it's not really good at any particular thing. And that's how Runway got started. The more we
*  work on this problem, the more we realize that this is actually a really interesting and deep
*  problem. And impact could be really large, right? As employees, we work in these companies and we're
*  just used to not understanding finance and not understanding business. It's supposed to be
*  mysterious. But if we can understand it at a deeper level, we can make better decisions and we can
*  align and collaborate better. And there's a lot of interesting ideas and AI plays a big role in
*  making that a lot more accessible. So listeners will know, and you're probably getting the sense
*  that I always really try to do my homework and get a very hands-on sense of the products and
*  services and technologies and models and research that our guests have worked on.
*  In this case, I am not yet a Runway customer, but certainly the pain point resonates with me a lot.
*  Having a founder CEO, I can recall scenario planning late night before the board meeting.
*  Like I was already supposed to have this done, but yeah, there was more. I always had the attitude
*  that I got to actually run the business more so than I need to polish this stuff up for the board.
*  They didn't always necessarily agree with that or love that attitude on my part. But I can remember
*  quite a few late nights tinkering with spreadsheets, either for historicals or more often for
*  forward-looking scenarios. So I definitely identify with that pain point. And then I did take the
*  demo last week to get a hands-on look at it. A couple of things definitely jump out. One is that
*  it does have this somewhat of a pattern of people identifying things that are done in
*  spreadsheets and then saying, can we build a better dedicated product for that specific problem?
*  This definitely feels like that. I think the way that it connects historical data to present and
*  future views is really nice and definitely feels like the future relative to what I used to be
*  doing. Also, the design is really great. The design is really strong and the branding-
*  Does this pop-up sound like a runway ad?
*  Yeah, it's not. But I was impressed. I was genuinely impressed. And I did actually send it over to
*  the Weimar CEO, took over for me after I got the AI bug so bad that I couldn't think about anything
*  else. And so we are officially in your pipeline. Anyway, all that said, not a paid endorsement. I'm
*  just enthusiastic. Let's get into some of these AI features. And folks who hear any number of other
*  podcasts and conversations that you've had to get other angles on what you're doing,
*  we'll focus on the AI angle. The feature that I saw that I thought was like, whoa, this really is a
*  shifting moment for how I would think about finance and think about how, not just how,
*  but also how much of this sort of forward-looking financial scenario planning I might do was when
*  we just did a text prompt to scenario. And we just asked the AI that's built right into the runway
*  product to create a scenario where we ramp up our marketing spend enough to 3X our revenue over the
*  next 12 months. And just with that kind of high level thing, it spits out a scenario for us that
*  we're now looking at. And I'd love to go into the hood there and understand what is happening that
*  is leading to that scenario popping out. Yeah. So there's a few ways to look at it. So
*  if you think about what a CFO would typically do, the CEO would have a question like, how do we
*  triple revenue next year? And the CEO would talk to the CFO or whoever owns the model. And then
*  what a CFO would do is go to this model that has all of these simulations, these relationships
*  around how different things affect revenue and growth two years down the line. And they'll
*  literally try some numbers out. What happens if we hire more salespeople? What happens if we
*  increase the marketing budget? What happens if we increase conversion and say, if we do roughly
*  these things, we'll need to raise more money, we'll need to increase prices, we'll need to
*  hire more salespeople. And we get there. And here's how it affects all of the other metrics
*  that you care about. And it's a very iterative sort of manual process. And if you think about
*  what's going on in a CFO's head, you have some kind of intuition about what are the likely
*  drivers that most realistically impact those constraints that you're looking for. So if you
*  think about revenue, then you think, okay, sales, marketing, pricing, and that kind of thing,
*  conversion rates. And then you go to this spreadsheet and change those numbers. And then
*  you visually look to see if the output matches the constraints that you're asked. And so when
*  you think about it from a technical perspective and how you can use an LLM to make that
*  better and faster, what are LLMs good and not good at? It's good at making a guess. It's good
*  at common sense of reasoning about what are things that are probably related to revenue.
*  What is it bad at? It's really bad at doing math, right? It's not super intelligent yet. It can't
*  just do math in your head, which is an interesting observation because humans also generally aren't
*  that good at that. We're good at language, but you would have to be, there's like Rayman, like
*  Savant's out there, but most people can't do very complicated math in their head, which is why
*  spreadsheets exist that helps us do these calculations. And so one way to think about
*  how this works is we're effectively giving this LLM a calculator and having the LLM do what it's
*  good at. It can understand a constraint. It can look at the constraint and understand what are the
*  drivers in this model that most likely are going to impact a constraint. It can evaluate whether
*  the output of changing those constraints and match the constraints that you want.
*  But actual calculation is done by the model engine. So that's like one very high level way
*  of thinking about this. But to make this work, the reason why it's actually essentially more
*  difficult to solve that same workflow in a spreadsheet is the context doesn't necessarily
*  exist in a spreadsheet. You need to have semantic labeling of the drivers and sure, you can look at
*  the roads, but you also need a lot more context. You need to know what is a product roadmap? What
*  is a hiring plan? What is a fundraising plan? What is a marketing plan? And plans usually actually
*  don't exist in that spreadsheet. It lives in places like Notion and Google Docs. And so in order for
*  to make this work, we have to invent new abstractions and primitives that can contain business intent
*  context, like a product roadmap, like a fundraising plan and a marketing plan. And with all of that
*  context, plus the logic of the driver, then you have enough context for an LLM to do something
*  reasonable to answer that question. Yeah. Okay. That's really interesting in multiple ways.
*  The sort of definition of a syntax for something like this is that's a challenge that I've been
*  through a couple of times with our company, Waymark. We create videos for small businesses.
*  And in some ways, there's like a similar problem where we have the sort of form that we want the
*  AI to write a script for and select the assets for and ultimately create the voiceover for and
*  all these different things. But we need to make sure that it respects the right format in its
*  generation. A lot of time actually, especially in the early days, went into defining what that
*  syntax would be so that it would be as lightweight on the AI as possible so that it could actually
*  do it. Also, of course, it had to be something that we could rehydrate deterministically with
*  code on the backend of the generation. We started relatively early. I'd be interested to hear
*  where you started and how that syntax has evolved. I imagine in our case, it started out really
*  simple because it was all that the models at the time could handle. And if anything, I think now
*  we're trending toward a more rich representation because the models are getting better at handling
*  those. So I'd love to hear what your journey has looked like to figure out how to represent this
*  in a form that the AIs can work with. Yeah. It was somewhat of a technical challenge in that
*  on the backend, these drivers are represented by UUIDs, right? So even hydrating the UUIDs into
*  semantic descriptions of what these things do was some amount of work to just get stored on the
*  backend. But we go beyond that because the way a model works isn't just about a single row or a
*  single formula, right? You can say runway goes cash flow via burn and that represents that row.
*  There is an entire dependency tree on how runway is calculated through burn and then burn is affected
*  by expenses and revenue, all these different things. And so one of the things we've done
*  that we use is actually we proactively use AI to describe parts of the sub model. So we say,
*  this is runway and this is how it's calculated. This is burn and in this particular model is
*  calculated. And so what we found is that the more context we give the LLM, the better it's going to
*  be able to figuring out what are the right guesses on what to perturb first. And you can generate
*  that context also through AI, which is a really interesting thing. And that's what we do. And we
*  find that that is like a really interesting direction in terms of how AI is expressed in
*  our products. And so the way I think about this, and I know like leaving a little bit from your
*  more technical question, but the opportunity we've seen in the product is if you look at how AI has
*  been expressed since GPT-3 has come out, initially people had did a bunch of experiments and were
*  cool demos. You call the API, but nothing really broke out until chat GPT, right? That was a moment
*  where, okay, this is like a very interesting interface that people can understand and get a
*  lot of value out of immediately. And what's happened since then is everyone has basically
*  added a co-pilot to their product. There's chat with whatever and this is like a side pain on the
*  side. And then now we're in a world of like agents, except like the models aren't capable
*  enough to self-reflect. And so agents by and large, like it's hard to get real productive
*  work done with them. I think the next range of models, when it's able to self-reflect a lot
*  better and plan a lot better, I think we'll see a lot more economic value. But that's like how
*  things have evolved. And some observations about that is one, like the thing about a chat interface
*  is that it's really accessible, but the two biggest opportunities for improvement is one,
*  it doesn't have a lot of context in most cases, right? Chat GPT has some memory now.
*  It doesn't really know a lot of business context about who you are and personalization and like
*  all the meetings that you have in your calendar. And so a bunch of companies are working on that
*  problem. The more context, the more helpful and proactive it can be. And the second thing is it's
*  proactiveness, right? What I've found really surprising is despite how many people use chat
*  GPT, how few of them really understand what you can even ask it to do. People are generally
*  underutilizing what chat GPT can do. And so the way we think about how those two things connect is
*  where we are with models today, I think the best use of AI is not through necessarily just a chat
*  interface or through agents, but we call it ambient intelligence. It just does the work in the
*  background without you having to ask. And the way it's expressed is through the interface itself.
*  So a real example is when you look at a driver in runway, like a row, and you can see the details of
*  it and trace through it, there isn't just a description there. You didn't have to ask it for
*  a description, right? It just told you and it just looks like text. It doesn't look like AI.
*  And I think the way Apple has thought about how you express AI is very similar to how we think
*  about it. In the course of your normal workflow, you can serve it as text, you can serve it as
*  suggestions without someone having to have a conversation with a message window. And I think
*  that is the best way to create value from AI today. And that's a lot of how we think about it.
*  Soterios Johnson I really like the idea of using AI in the background to synthesize metadata.
*  That to me is definitely a strong emerging pattern. And we do that a little bit at
*  Waymark too, in our case. I'd be interested to hear how much you had anticipated building
*  models into the product when you started with the product. In our case, we really didn't.
*  I was always interested in AI, but it seemed like at the time that we were building the product that
*  anything that could actually help our users create content was a long way off. And then it
*  showed up a lot faster than we anticipated. So we created this template system. And initially,
*  users would fill it out. And then we learned later that there's an opportunity for the AI to
*  fill it out, but they weren't yet multimodal. So it was like, we need to represent this in text,
*  but how do we represent it in text? And there became this whole kind of elaborate pipeline
*  for figuring out what exactly is on screen. We know what our wonky JSON backend representation
*  is, but what does this actually look like to a person? And that was a whole process.
*  When did it become clear to you that the models were getting good enough that it was actually
*  going to be able to help with a finance use case? We started a runway maybe just right before GBD3
*  came out, I think maybe a few months before. And Naval Ravikant was our first check. And he
*  actually named the company Runway. There's a funny story about this because when I was talking to
*  him about this idea for Runway, I asked him what he thought about the name CFO.AI, which is a domain
*  we still own and we don't use. And his feedback was, no, don't call it.AI. This is back in 2020.
*  Right. And he said, the reason why you shouldn't call it.AI is because it's going to be
*  dated really quickly. Everything is going to be AI. And so the company without AI as a name,
*  it's not going to be a sustainable name. And I thought that was in retrospect, that is such a
*  prescient observation because the way we think about AI today is you don't talk about your product
*  as powered by JavaScript, right? Or AWS. It's just how it works. And that's the right way I think
*  about AI. It's not like a separate thing. It's just part of the capabilities of the product.
*  And one of the many avenues that you can use to create value, that was part of our thinking
*  in the beginning. The mission of Runway has never changed. The mission has always been
*  to make business accessible and understandable to everyone. And when you think about AI in relation
*  to mission, it's not just a thing we added in later when it became hot. What large language
*  models are really good at today are precisely those two things. Making things more understandable
*  by taking something that is maybe complicated and explaining them in plain English, right?
*  And also making things accessible by short-cutting these complicated workflows so it can ask you to
*  do something in plain English. That's something that it is really good at. In fact, I thought
*  it was so good. I currently have the number one GPT in the chat GPD store under the education
*  category called Universal Primer. And the entire thesis is that is something that elements are good
*  at. It can take something very complicated and explain it to you like you're five and also
*  filling up links of any prerequisite concepts you're missing. And so that's how we thought about
*  elements from the very beginning of Runway is how can we make this very complicated business
*  understandable to everyone.
*  Cool. I missed that in my scouting report on you. So that's cool that you have the number one GPT.
*  You cashing any checks from that yet? Still waiting on our mailbox money from our GPTs, right?
*  I am. I can't disclose how much or the method under NDA, but I can at least confirm that yes,
*  I have.
*  I haven't even heard that they're actually paying out. So that's also a little-
*  Yeah, they said specifically don't talk about the method or the amount, but they didn't say
*  nothing about that when Candice says we're not getting paid. We are getting paid.
*  Cool. Interesting. So a couple of great little tidbits there.
*  Going back to how it works when you are generating a scenario, I am interested in
*  what the language model is being asked to generate. Are you using a tool
*  use or function calling paradigm? And then you said you're giving the model a calculator. So
*  in this case, Runway is the calculator, right? But I'm interested to hear a little bit more
*  about what that interface looks like between the model and the more deterministic explicitly
*  coded product. Is that like an iterative goal finding sort of thing? If I say I want to
*  get to 3X revenue, is it cycling until it kind of hones in on that end state?
*  Yeah, exactly. The great thing about LLM is you can have some intuition about how it should work
*  based on what humans do. So a CFO understands what are the- has some intuition about what is
*  going to drive revenue. And with a model, we can do better than that. We can provide the entire
*  dependency tree of a model to the LLM and say, here is roughly how the model works and here's
*  the different drivers. Take some guesses on what you think are going to perturb revenue or whatever
*  constraint you want the most. And once you selected that, take some guesses as to when.
*  So if the constraint is like 3X revenue next year, then reasonably, you're probably not going to try
*  to do it five years from now. We're probably going to do it like three months from now, six months
*  from now. You're going to try a few different things, right? And when you try a few different
*  things, we run it through this calculator that is a model. And then we look at, okay, what was the
*  constraint that you asked to optimize against? It was revenue, right? So we said, okay, which one is
*  that? It's going to be the one that says revenue. And then we compare the outputs before and after
*  and say, is this 3X? Right? That's a calculation. We can trivially feed it.
*  And so the way this workflow works is exactly what a CFO does, right? We're not asking it to do the
*  math. We hand it basically this black box calculator and we ask it to basically figure out,
*  what are the most likely levers to pull and try pulling some levers and what's going to tell you
*  what happened. And then you're going to look at that. It was a higher, lower, how much was off by,
*  and then you're going to try some other things and you iteratively get closed.
*  It doesn't work all the time, but that is definitely something that as the model capabilities
*  get better, it will get better at. And the way we orchestrate it, as that gets better, it will also
*  get better. That sounds very much like the assistance API. I don't know if you want to
*  comment on what underlying technology you are using, but if I was going to
*  point to a single technology that maps onto that most closely, it would probably be that.
*  Yeah, we don't use that. It is a very unique use case in that we have a custom model that's
*  different from company to company. And so we built a lot of very custom orchestration
*  systems to make that work. But yeah, that is a pretty good analogy.
*  Hey, we'll continue our interview in a moment after our word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead
*  of variable regional pricing. And of course, nobody does data better than Oracle. So now you
*  can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive
*  of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive. Oracle.com slash
*  The Brave Search API brings affordable developer access to the Brave Search index, an independent
*  index of the web with over 20 billion web pages. So what makes the Brave Search index stand out?
*  One, it's entirely independent and built from scratch. That means no big tech biases or
*  extortionate prices. Two, it's built on real page visits from actual humans, collected anonymously,
*  of course, which filters out tons of junk data. And three, the index is refreshed with tens of
*  millions of pages daily. So it always has accurate up to date information. The Brave Search API can
*  be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up
*  to 2000 queries per month at brave.com slash API. In terms of the improvement, what do you think is
*  maybe what has and what do you expect to drive the most improvement in the overall value to users?
*  How much is coming from scaffolding, orchestration, and how much is coming from just
*  raw scaling and more fundamentally capable general models?
*  I think generally for most problems, including ours, the answer is both. So what I mean by that
*  is obviously as the models get better, intuition, reasoning, planning, self-reflection, all of that
*  has incredibly high leverage. And it also drives the architecture of the orchestration.
*  Orchestration will need to change as it's able to self-reflect better. But for our uses in
*  particular, orchestration is particularly interesting and useful. And I'll say it goes beyond
*  orchestration. It's like, what is the substrate that you're orchestrating on top of? And what I
*  mean by that is it will be very difficult to create that workflow on top of the substrate of simply a
*  spreadsheet. And that's because the abstractions that exist in a spreadsheet are cells and rows.
*  And they are not well suited to contain business intent contexts like a product roadmap or
*  fundraising plan or marketing plan. And so job one was actually creating the right substrate so that
*  you can connect that context with the business model and the plans together and pass it to an
*  LLM. Once you have the right substrate that can contain that context, then orchestration is important
*  in order to feed the relevant context to the LLM. And at that point, larger context windows help,
*  better understanding helps. But a substrate is not something that an LLM is going to handle for you
*  outside of the box. And this is where I'm a big believer in this idea that you can't just jump
*  straight to an LLM, at least for the next year or two. What you can get an unfair advantage of
*  is building a tool for thought that has the right abstractions to contain more and more context
*  that people already use. And that's a much better starting point to feed to an LLM because you can
*  feed it more context. I'm looking in my notes to see if I have the number of integrations that the
*  product supports, but I believe it's in the hundreds, right? It's about 680 today. 680.
*  So I assume that is also something that kind of started for non-AI related reasons, but turned
*  out to be a perfect Swiss army knife to pull in context. And I'm assuming that this is where
*  the marketing plan comes from or the product roadmap, right? People aren't entering that stuff
*  directly into runway in most cases, right? Actually, a good number of customers are.
*  So we integrate with just about everything because finance is not about really just finance.
*  I think the right way to think about it, the way we think about this is that it is a simulation of
*  the entire company. And so on some level, everything that happens in the company,
*  every person, every department falls down to the bottom line eventually somewhere.
*  And so it's all kind of part of the finance model. It's just that today the tools that we have make
*  it so that the finance model is really isolated. And as a result, if you're a sales person, the
*  sales team has a model, the product team has a model, the growth team has a model, the marketing
*  team has a model. All these are in different spreadsheets everywhere. And they really ought
*  to connect to each other, right? So that you have one view of how the marketing plan affects
*  the sales plan, affects your overall financial health of the company. And that doesn't happen
*  today. And so we integrate with a large number of data sources because everything that happens in a
*  company is eventually part of that financial model. And you want to be able to track progress against
*  all of those things. I think the most interesting thing that we've seen is that we have companies
*  integrating JIRA into Runway, which for a finance platform, that's unheard of, right? Like finance
*  people barely use existing finance platforms because they're all really difficult to use and
*  quite slow and un-flexible. But the reason why is because we have an abstraction called plans that
*  actually can encapsulate business intent context. So you integrate JIRA so you can attribute a ticket
*  or a project to financial outcomes, how it affects conversion rates, how it affects growth,
*  and then see how it affects margin. And so all of that context is useful for an LLM and it will
*  only increase in utility over time because it's hard to make decisions off of just the financial
*  point of view, right? It's a lot easier to make decisions if you have a holistic understanding of
*  what is a product team's intent in roadmap, what is a sales team intent in roadmap and growth and
*  marketing, all these things. And then as the LLMs get more capable, it can create richer plans that
*  reflect that business intent as opposed to just changing the numbers. So the vision that I'm
*  starting to see through the fog for myself would be like, if I've integrated my task management
*  platform into Runway, I might be able to go in and ask something like, what's the financial impact if
*  we do the ticket that's on the onboarding funnel and it improves signup rate by X, Y, or Z percent?
*  What's that look like? And how does that compare to if we handle a long standing pain point,
*  which might improve retention by A, B, or C increments? And then the idea would be like,
*  I can see the range of these two things and start to prioritize my
*  actual work with this kind of visibility into long-term financial results.
*  I think a nuance there is that's something that you can do today in Runway and you don't even need
*  AI to do it. So if you can say this Jira ticket is going to increase conversion by 5%, right?
*  You can just do that and look at instantly the impact on Runway revenue margin burn by just
*  clicking on the thing. There is no AI required there. I think what's more interesting though
*  is for example, when you have a bunch of possible potential tickets that you can work on and you
*  want to know on which one each should you work on first and there's a hundred of them, then we don't
*  actually do this today to be clear, but in theory an LLM can look at that, all of those things and
*  look at what is the most impactful based on ROI ticket you can work on. What we do today is
*  something interesting though, which is for example, if you have something like budget versus actual,
*  as your time progresses, where you thought you were going to be in July a year ago is different
*  from where you are actually are, right? There is a variance there. Let's say your revenue is off by
*  20%. What you can do if you have all of your data integrated through your model is drill in and
*  figure out, okay, why was it off by 20%? Was it the pricing that we got wrong? Was it a number of
*  leads? Was it a conversion rate? We have all of this information because we integrate with
*  analytic systems and your data warehouse, all these different things. Through that, we can just
*  tell you. Traditionally, the way you would have to do is you would have to trace through your model
*  by hand in a spreadsheet, which is really annoying and slow, but we can just automate all of that,
*  which is pretty handy. Yeah, that's cool. I can definitely see, going back to the theme of
*  automatically AI doing stuff in the background for you, creating context, or in this case,
*  it'd be maybe more creating connections or even helping manage. So many companies struggle with,
*  are we doing things that actually advance our stated goals at any given point in time?
*  I can imagine a really interesting background process that could look at all the tickets
*  and say, first of all, we hypothesize this might connect to, and then also, I don't know,
*  I'm assuming there's okay, our ability among those 680 integrations as well. Do these things seem to be
*  connected to the top level goals that we have set, which I think soberingly enough for many
*  leaders in many companies would be like, they don't always. Sometimes a surprisingly low
*  percentage of them do. Yeah. So it almost sounds like this is your sort of angling,
*  not for a finance platform, but really for an overall business management platform. How big
*  does this vision get in your mind? So LinkedIn, I describe it as disrupting the $70 trillion
*  industry. I think about it one, another way I do think about it, and Stripe's mission and vision
*  is to increase the GDP of the internet. I think in a real way, our mission is increasing GDP of
*  the world because there is so much impact in having everyone in the company understand how
*  the business works, what the plans are, what is the impact of their own decisions. So that we want
*  to live in a world where imagine a designer, a PM engineer could say, if we work on an X instead
*  of Y, here's how it affects margin and growth two years down the line. You can't imagine having that
*  conversation today. And that's really interesting. Why is that? Everyone works in a business for the
*  most part, and yet we accept this reality that it's okay for very few people to understand that you
*  can just be heads down and focus on your own thing. And we think that the evolution of information
*  technologies, especially like since computers has been making like very complicated things more and
*  more accessible and understandable. That's what a spreadsheet did. And also that's what Figma did
*  for design through components, right? And we think in a very real way, what we're doing is
*  if inventing new information technology to make one of the most complicated businesses
*  understandable. And we think that has a really big impact. People, and you're right, like the outcome
*  of this, we don't actually think of it as a finance platform. We market it today because that's the
*  most understandable way to think about it. But the way we do think about this is a business operating
*  system. And an operating system maybe sounds more dry, but like the way I think about it is like,
*  what is the video game view of a business? My background is on video games, right? It was Zynga
*  and sandbox. Because like if you ever play civilization or a little coaster tycoon or
*  like pizza tycoon or whatever, all these games, they're fun games where you run a business.
*  So what makes that fun? What makes it fun is it's understandable. It's visual.
*  It's interactive. You get responses immediately. You feel like you're building up a mental model
*  of how things work and you can have some agency control over it. Businesses don't work that way
*  today. And it totally can if we have better tools for thought that map to how people think about
*  their businesses. And we would argue a spreadsheet is not the best form of that. Hey, we'll continue
*  our interview in a moment after a word from our sponsors. Omniki uses generative AI to enable you
*  to launch hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it. And I recommend you
*  use it to use cog rev to get a 10% discount. Hey, all Eric Torenberg here. I'm hearing more
*  and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30 year old ex Fang senior software engineer as much as the next guy,
*  but honestly, I can't afford them anymore. Founders everywhere are trying to turn to
*  global talent, but boy is it a hassle to do at scale from sourcing to interviewing to on the
*  ground operations and management. That's why I teamed up with Sean Lanahan, who's been building
*  engineering teams in Vietnam at a very high level for over five years to help you access
*  global engineering without the headache. Squad, Sean's new company, takes care of sourcing,
*  legal compliance and local HR for global talent so you don't have to. With teams across Asia and
*  South America, we can cover you no matter which time zone you operate in. Their engineers follow
*  your process and use your tools. They work with react, next JS or your favorite front end frameworks.
*  And on the back end, they're experts at node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two
*  hours of work per week, but billing you for 40, but you'll get premium quality at a fraction of
*  the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the wait list.
*  Yeah, it's really interesting comment on video games and how the sort of business intelligence
*  in video games is always 10 out of 10 in contrast to real life where it's so often far from it.
*  So I love the hugeness of the vision. If we reel back to today, I was just the AI engineer
*  World's Fair last week and the big topic that I'm going to talk about is the AI. So I'm going to
*  and the big topic there is like demos are really easy. Making stuff that's actually reliable in
*  production is hard. That's the chasm that so many businesses are trying to cross.
*  Where are you guys in that journey today? Like when I generate a scenario, does that come along
*  with a like a you better fact check this sort of warning or do you feel like you have it
*  under control enough that you can be confident that it's like pulling the right levers or things
*  are like executing properly. You said earlier like it doesn't always work. I don't know if
*  that means like there are errors or just like sometimes it can't converge on your goal,
*  which would be two different ways in which it might not always work.
*  But to what degree have you tamed the unwieldiness of language models in this product?
*  I would say we have not tamed it very well at all. This is early and I think the models
*  capabilities aren't quite there yet. It hallucinates, it will misunderstand, it will get things wrong.
*  I generally would not trust it out of the box at all to be very clear on that particular use case.
*  And so that is like our version of the shiny AI demo and like it will get good as model
*  capabilities increase and orchestration gets better. But I think like what people and what
*  we're focused on now is like how do you get value out of it today?
*  And do we think about this is there's so much that you can do that leverages what LLMs are good at
*  immediately. And so we have a few ideas. So we have this thing called explain mode.
*  And what that does is when you hold down the control button and you mouse over any part of
*  the product, it will just tell you what you're looking at and explain it.
*  And so that idea comes from this idea that you shouldn't have to like type and have a chat
*  with the system to get value out of it because most of the time you don't even know what question
*  to ask. And so there is these ambient, we refer it internally as ambient intelligence.
*  There's this ambient things that just exist without requiring any user interaction that takes
*  advantage of known context where you can make things more understandable, explainable.
*  Another example is we have pull requests between models. Like when you look at that,
*  it should just explain and it does what's different, what changed. That's something
*  that's good at today. Right. And so where we are seeing value and it's like fairly reliable is just
*  making things understandable and accessible to people who aren't familiar with the product,
*  unfamiliar with the business. It's quite good at that today.
*  Sgt. Mike Allen Yeah, that's interesting. I read a lot of
*  ML literature and these days my reading workflow is to take the paper, put it into both Chai GPT and
*  Claude and ask for a summary in each one for starters and then just go back and forth with
*  kind of tinkering back and forth between the two models and just asking lots of follow-up questions.
*  And I would say it is getting extremely good. And what's notable about this ML literature is for
*  one thing, it's moving super fast. So like a lot has happened since the knowledge cut off date at
*  any point in time. It's like by definition, not in the training data, but even just the overall
*  gestalt or whatever of the field is shifting on like a month to month basis. And yet I would say I
*  see precious few outright hallucinations or errors when I'm working with something that is this is
*  the document that we need to focus on. So for finance, there certainly are these intricacies
*  where I could see it being a challenge with formulas, drivers, exactly how things are calculated.
*  But it checks out to me that it would be very good at explaining these sorts of things in the
*  world today, given that at least among those in the know, like those concepts are pretty well
*  established. I'm curious to see how my GPT reform with that workflow. If you upload a PDF to universal
*  primer and see what it does, I'm curious to get your reaction to that. Yeah, because the prompts
*  that I have by default for explain are very complicated technical problem. Like explain to
*  me how transformers work in the context of LLMs or explain how Navier-Stokes is derived and things
*  like that. So yeah, I think that would be a pretty good use case. I'd love for you to try.
*  Okay, cool. I'll check it out. When you're in discussion with Sam Altman as one is from time
*  to time and they ask you, what do you want GPT-5 to do that the current models can't do? I'm being
*  somewhat silly with my premise there. I don't know how often you're in discussion with Sam Altman,
*  but they talk about not much at all. Abstracting away from that. I was just joking.
*  They've said in public forum a few times that one of the ways that they evaluate companies that
*  they're interested in is the companies that are like, we need GPT-5 because we needed to do X that
*  your current model can't do. So with my silly premise aside, what are those things for you?
*  It sounds like it's this scenario planning, but can you be more precise or detailed in terms of
*  where it's failing now that you think GPT-5 quote unquote might do for you?
*  Yeah. What is known about orchestration is that one of the biggest lifts that you can get
*  through better orchestration is reflection. Look at it. How do you feel about it? Is it good? Is
*  it accurate? How would you change it? And then come up with a better prompt. That I think is
*  the most important thing to get better in a new model. And I think it's probably likely to be the
*  highest leverage thing. And actually it crosses into my personal definition of what AGI is.
*  As the models get more capable, it should be able to look at existing outputs and figure out why it
*  was broken and how to make it better. And below a certain threshold, you just get nowhere, right?
*  It just devolves, it hallucinates, it loses track. I personally think that is the biggest thing I want
*  to see. And that reflection capability, I think once it crosses a certain threshold,
*  is basically the barrier towards AGI. If it crosses a critical threshold where it can continuously
*  look at its own orchestration, look at its prompt and just get better, then you approach
*  it self-boost trapping, right? The separation between an LLM and AI system today is basically,
*  it's already, I think, smarter than many humans. You ask those questions and probably half the
*  human population kind of come up with as good of an answer for any given problem that you ask
*  how to BT. I think it's more capable than people give it credit for. But I think what we really
*  want to look at is on the extreme end of capability for a human being. And I think one of the more
*  extreme ones are the human beings incapable of improving the LLMs themselves. And once an LLM
*  or properly orchestrated, some kind of eugenic loop can get to that point, then we're there.
*  And I think that's basically the downstream of better reflection capabilities, which in turn
*  is driven by planning capabilities, recent capabilities, and things like that.
*  Yeah. It doesn't seem like we're too far off. I definitely agree that all things considered.
*  One of my kind of standard talking points is that it was actually, in my view, as of summer of 2022
*  with the Palm paper that the frontier model passed the average person on the average task.
*  I've evaluated that with Palm on Big Bench. And now I would say that the models are closing in on
*  expert performance on routine tasks. But the word routine is doing a lot of work there because
*  obviously the models really excel where they have lots of examples to learn from.
*  And comparatively, they struggle when they have to figure out entirely new things. So that's exactly
*  the shortcoming that you're speaking about. Before we return to that and project into the future a
*  little bit farther, the UI that you mentioned around just mousing over and hitting control
*  within the product, I think is a really interesting one and one that maybe a lot more
*  products should adopt. That also seems like the kind of thing that might not be
*  secret sauce that you might be able to tell us a little bit more about how that works.
*  I'm curious, is that like a, did you have to go through and take a ton of screenshots of your
*  product and just like manually label them and throw those into a big prompt or like any lessons
*  learned there? Because I think a lot of people would actually do well to implement something
*  like that if they could figure out how. Yeah, it's mostly a design problem, right?
*  And I think like when you look at the way Apple implemented intelligence in the iPhone,
*  they never said AI or something like that. So like Apple intelligence in general,
*  it is very similar to how we think been thinking about internally for a while now.
*  The it's not a very complicated multi-mobile science fiction thing. We just literally trace
*  through the dome of what the object tree of whatever your mouse is looking at. And we say,
*  what does this thing is a driver? It is a report. If you're looking at a mole around a poll request,
*  we just, we know you're looking at it. It's already pre-generated. And so we define the
*  key entities in the product, whether that's a page or reports, a poll requests, a driver.
*  And we say, okay, let's generate some explanations and just show it to people.
*  So it's fairly uncomplicated, but you know, people have, I think, systematically under value design,
*  right? What Apple did was interesting, but it was not a whole lot of new foundational
*  model capabilities there. It was just a very well considered design. And that's what made the iPhone
*  work. And in general, that's one of the bigger opportunities in applied AI today. Everyone's
*  like looking for a more capable model, the better fine tuning orchestration system or whatever it is.
*  And reality is you'll have a few AI labs and they all have the most capable models.
*  And there needs to be a lot more work in figuring out how you can use these new AI capabilities and
*  express them to customers in useful ways. And we barely scratched the surface of that. And
*  right now, the bulk of that is chat with a bot. It's a profound point that if the surface area
*  isn't that big, a lot of times things don't have to be nearly as complicated. That's my take away
*  from your comment there that like just work harder on defining your problem and mapping out
*  the internals of it. And in many cases, like you can be pretty comprehensive about that. And then
*  you've made life a lot simpler on whatever, whether it's a user or a language model,
*  just do that hard work. It's finite and it can like really pay off with that without having to
*  invoke any science fiction. That's a good upshot from that. How about just to sneak in a couple
*  more practical things before we do the big picture questions. I've seen you comment in a
*  couple other contexts, like very aggressive early adopters of chat, GPT and other AI tools
*  for operations within your own business. What are your favorite products, your favorite use cases?
*  Where are you getting the most value from applying language model or language model
*  workflows in your business today? Yeah. The good news is there's a lot more
*  ready to use tools out there than it was a year ago, even two years ago. But we've always thought
*  about AI as an incredible tool to increase the leverage of our company. And so we have this
*  internal goal of never having more than a hundred employees run away. And it's possible today because
*  you can scale with increasing capabilities in AI, right? As you mentioned, like we're maybe not
*  that far off. If that's the case, you have a very small company where everyone is like just so
*  empowered, has so much leverage and so much freedom and ownership over what they do that they can
*  create so much more impact than at a large company. Because the biggest factor in making
*  like work less enjoyable is just like more people, I think, more people, more problems.
*  So we've always thought about and been excited about it. Two particular use cases, like we've
*  talked extensively, I think is generally about the AI SDR that we built when our website went
*  viral and we have so many leads coming in, we had to qualify them. So it's a very simple automation.
*  You have a new signup, we enrich it through ClearBit. And then we have a prompt to qualify
*  this lead, whether they're using a free email address or work one, what kind of work do they do,
*  how big is the company, how is it growing, what's the role, are you key decision maker,
*  all these different things. And the wonderful thing is we can describe our qualification
*  criteria the same way I would describe it to SDRs. Roughly we want like companies that are
*  growing and passing millionaires, we want them to be a key decision maker or in finance. They
*  should be largely based in the US and ideally more than 50 people. And it'll do that. It's a
*  pretty simple thing for an alum to understand. And it does a great job of filtering. And then once
*  they're qualified, then we, and this is where it took a bit more time, we developed this prompt
*  that where we gave them context about what we do and our value proposition. And what we know about
*  their company through their website and all the other context that we have and say, please draft
*  a email responding to this customer and make it very clever. Don't make it cringy. Don't make it
*  mid. Just connect what we do and what they do in a really clever novel way. And it took a lot of
*  tweaking to make it sound reasonable. And the outcome is that when our sales team wakes up in
*  the morning, we automatically post that draft in the Gmail draft folder. And so they wake up and
*  in the draft folder is a bunch of pre-written emails, all pre-qualified, all pre-customized,
*  and they just press send. So that's one of them that's interesting. More recently,
*  I do cultural interviews with candidates and I was taking a lot of notes as I'm looking for
*  certain traits in candidates. And I was thinking about, okay, I don't really want to take these
*  notes anymore because I want to pay attention to the candidate and have more of a connection
*  instead of typing. And I know brain records the video. And so what I did is I just made a GPT
*  that's internal and I downloaded a transcript, paste it in and just gives me the notes in exactly
*  the format I want, pulling out exactly the things I'm looking for. It doesn't do a very good job of
*  making the hiring decision and evaluating it, but it's really good at taking the content and
*  extracting out like the key things that I was looking for and the angles I was looking for
*  around motivation and values and things like that. That's been like incredibly convenient for us.
*  Do you use no code tools to build those things? I feel like a lot of software companies
*  are reluctant to use platforms like that, but maybe your example will inspire people to
*  build more on existing platforms and do less kind of code at all from scratch.
*  Yeah, we do both. So for the two things I mentioned, one's just chat GPT, the other is Zapier plus
*  Zapier automation. But we also build other tools like that's written in code, depending on
*  capabilities, right? I wanted to build a thing that will leave feedback on documents in whatever
*  persona that people wanted to. So I want Jeff Bezos or CJAS to critique this thing, my notion
*  document, and that required code. I wrote most of the code with chat GPT and understood how the
*  notion API worked. And I said, I want you to monitor all of its entire workspace and look for
*  mentions of you, this bot. And when it says like, the way it works is you call app jam session with
*  Steve Jobs, right? You just leave that as a comment on any document. And then the bot will come back
*  in the voice of Steve Jobs and excerpt out the critical parts of whatever document and leave
*  feedback critiquing it, however you like. So it really depends on the use case. We're pretty
*  pragmatic. If it's possible to do and quick to do with a no code tool, we'll do that. If we need to
*  write code, we'll do that too. Do you find that those personas are best delivered by any model?
*  In particular, I've recently been experimenting with the RLHF models versus the purely pre-trained
*  models. And the pre-trained ones we have access to are not as powerful, but they do seem to capture
*  the stylistic elements, at least, of a lot of different personalities a lot more closely.
*  What have you found there in terms of how do you actually get the real value of the
*  Bezos or the Jobs perspective? I find the prompt has so much impact on the quality of it.
*  The prompt that I think we share publicly is really long and you have to work really hard. You have
*  to put every trick in the book for it to get some interesting insight out of it. We say,
*  do not say anything generic. Make it the most interesting novel insight, even to an expert.
*  And talk in their persona, but not in their media persona, but look at their internal persona
*  on how they actually speak. And so the more specific detail we add and the more stringent
*  we are on the quality and insight requirements, the slightly better it gets. Interesting. I'm
*  really very interested to see what Lama 3 400B does in that regard, especially if they do release
*  the purely pre-trained version. They may or may not in the end, but if they do, things will start
*  to get a little weird, I think, in the impersonation game. Yeah, I think Jimmy Apple said that's not
*  going to happen. And I think strategically, I would probably bet on it not happening.
*  How about getting any models to write as you? You're obviously a prolific tweeter and I've
*  heard that's good for lead gen for your business. Folks internally want more tweets from your
*  account. Have you gotten anything to write as you in a way that's compelling to you?
*  No, I don't think we're quite there yet. And I think this does speak to maybe a cutting edge
*  limitation on models. I think maybe it speaks to probably more a lack of context than anything else.
*  The problem with having a LLM generate interesting content or just in general, a good piece of
*  writing is that good writing isn't about the writing, it's about the ideas. And the most
*  interesting ideas tend to be novel a lot of the times or phrased in some kind of novel, interesting
*  contextual way. And that gets at the tail end of the distribution in terms of trading data.
*  I think more data, more reason is going to help, but I think more context and some way of continuous
*  learning and interacting with the world so they can form these experiences is all going to help.
*  And I find working with a ghost writer, so I actually have a ghost writer in LinkedIn because
*  it's a very different style. And it took a long time. And the main challenge is it's not the
*  writing. It's imparting the lived experiences, the stories, everything I've seen, and then expressing
*  that in a style that's very difficult to get to. And when working with a ghost writer, you're
*  basically offloading a lot of context. And you probably will need to do the same thing with LLMs.
*  But the great thing about LLMs is that you can build a lot of context just by connecting it with
*  a bunch of existing data, which will be much harder for a human being to do. It will take longer.
*  And so as we have more context and better capabilities, I think that'll get better.
*  But today, it's not there. I would not. My content, if I want it to work, and you've seen this,
*  right? You can tell when someone posts something with ChadDBT, it's very recognizable. It's very
*  mid. And that's probably not going to work. I think that's mostly been my experience, too.
*  The one exception that I've had with that is when I write the short intro essay that I put at the
*  top of each episode of the podcast, I now take 30 of those that I originally wrote by hand before
*  Clawed 3 existed, and then provide also the transcript of the current episode and ask it
*  to write a new intro in the style of the 30 that I've provided using, of course, the new content.
*  I would say for three out of four episodes, I could probably just use that. One out of four,
*  I have more of a strong opinion or a take or perspective. If we're talking about regulation,
*  we're talking about something where I want to weigh in in the intro, then it doesn't get that
*  right. Although I can still write it pretty well if I instruct it upfront of here's what take I
*  want to infuse. But if it's a more standard episode where we're talking through research
*  results or we're talking through a product, it actually does a pretty good job. And it is uncanny
*  in picking up on my written mannerisms, which is a bit of a funny experience to be reading what
*  really does feel like my own voice coming back at me out of an LLM. Yeah, that actually totally
*  tracks. It's probably if you can give it enough context. And what we're saying is you give it a
*  bunch of examples and it has a context over your current episode. Can it write something
*  reasonable most of the time? That makes sense. And that's probably close enough to good for
*  something like a LinkedIn. I think Twitter is really different because what context do you give
*  it for any given shitpost that is it going to be a banger? Right? That's timely, it's new,
*  it's kind of clever, it's surprising. And so I would say that works pretty differently.
*  But generally, yeah, you have context and you prompt that it can do a pretty good job.
*  So last couple of minutes, zooming out big picture, you're on record with an expectation that AI
*  capabilities increases are not at their end and expecting seems like pretty powerful
*  AIs to come online in the not too distant future. I don't want to get bogged down in like specific
*  timelines or whatever, because obviously that's always got a confidence interval on it. But I am
*  interested in how you think about making your investments in light of possible AGI soon, how
*  you think about raising your kids in light of AGI soon and how you think about your company in light
*  of AGI soon. All these sort of most fundamental activities in life seem to be under the specter
*  of possibly radical change that I think about this basically nonstop. And I still am more at a loss
*  than not as to how I should adjust my approach to life. So what if any changes have you made to your
*  approaches given your outlook? Yeah, for investing, I talk my book in a sense that I think the biggest
*  opportunities in AI is productivity and context. So I'm looking for companies that take those
*  two pillars and drive it forward in new product expressions. So things like an AI Chief of Staff,
*  things like AI SDR platform. So I invested in Automatica, which does that. I invested in
*  Maestro, which is the Chief of Staff. I think those are still very interesting opportunities.
*  So mostly it's on the application layer today, although I was a small investor in Letham Labs
*  and some other companies. But I think there's going to be relatively few new foundational
*  model companies and most of those implied. And so that's one angle I think about.
*  How does AGI affect that? I have the same answer for investments as I do for the company.
*  So how does AGI affect the company? And I think on some level, all bets are off,
*  right? Once you get the AGI, it may be a very short shot to ASI. And I actually don't think
*  about it that much. The reason why I don't think about it that much is in that world,
*  my company, in terms of just absolute impact, the impact on me is probably way smaller than the
*  impact on Microsoft or Amazon or literally every large company. Because what we're talking about
*  is, okay, it can do all forms of productive work. What is then the work that people do? What is the
*  nature of work? What happens to my specific company is almost irrelevant when you have very much
*  larger societal level questions. That's going to raise. The one thing I do think about is in
*  AGI world where you have agents running the world, can there be a runway agent and what
*  does the wrong agent do? And I think there's an opportunity to have effectively a CEO agent
*  who understands the entire business context because that's a really interesting,
*  unique source of data. There's very few companies that have a holistic view of everything that
*  happens in the company. I think that's one interesting direction. But by and large,
*  I think the societal effects are just going to be unpredictable. So I don't think about it all that
*  much. In terms of the family bit, I think maybe that does connect to the company bit, which is
*  I advise my kids to be makers. And this is what I would do before AI anyway,
*  learn to code, learn how to make things with their hands, learn how to create games.
*  And it's wonderful. Over Christmas, we were traveling with a friend's family and
*  I have a nine-year-old and with another nine-year-old, they wanted to create a
*  game that's a cross between Transformers and Gundam and they asked how do you have to do it.
*  Chucky B generated art, they generated the rules, they asked them how would you make it? Get Unity,
*  they download Unity, nine-year-olds, right? And they have this thing that will guide them step
*  by step on how to do things and they'll respond to their questions at their level. It's wonderful.
*  So they can learn how to make things. But the question then is what is the value of making things
*  if AI can just make it from scratch, from start to finish instantly, right, in the future?
*  And my point of view on this is basically things that are provably made by humans
*  will still be valuable because I think what Charlie Munger observed about the world is
*  something I think about a lot, which is people think that greed drives human progress,
*  but it's not greed, it's actually envy. Like social competition, sexual competition in society
*  is something that has existed since people or animals have existed. And so we are going to be
*  endlessly creative at finding new status gains to compete against, right? Even in a world, in a
*  post-singularity world, it's still going to be about like how can I demonstrate I am the most
*  interesting, fit, creative, smart person out there and we're going to figure out new rules.
*  The rules might be the thing that's going to be most valuable is like whoever can paint the best
*  painting by hand, right? Like that's what art does. The software that's going to be valuable
*  is the software that is not created by AI, but the one that was provably coded by hand without AI
*  assistance. We see that today in the sense that if you watch chess, you don't watch AlphaGo playing
*  against AlphaGo. No one can play better chess than that. You still watch Magnus Farson because
*  that's interesting as a human. And I think that will, dynamics will play out on a broad scale.
*  And so there's always going to be something interesting for humans to do unless AI kills us
*  first. On that note, that's a very common answer. Actually, it's basically the same answer that I
*  have, which is my version of it is just like playing toward the range of outcomes that I feel
*  like I have some ability to influence. If there's like AGI, ASI soon, like,
*  yikes, I don't really know what I can do. I don't think about it that much either.
*  Do you think though that means that governments should start to be thinking about this and start
*  to be working on international treaties or whatever, or would you cast your lot with just
*  technology taking us where it might? How much do you think we should try to be intentional in
*  shaping or controlling versus just letting it happen as it happens?
*  I'm like generally skeptical of government intervention. I don't know that we know what
*  the right move is. The thing that's already happening is regulating compute. I don't know
*  how I feel about that. Like, how do we know this is good? How do we know that's the right thing
*  to focus on? How do we know that like with the current amount of compute and right architecture,
*  we can't just get the ASI anyway. So I think there's a lot we don't know. I generally think
*  the, I'm bullish on the kind of mechanistic interpretability. And I think really the things
*  are going to solve it is just better understanding through technology of how this works more so than
*  government regulation. Cause there is no doubt that to me that regulation will happen. I just
*  don't know that the right thing is to get ahead of it when we don't know a whole lot
*  about how the world's actually going to change. Yeah. I'm pretty uncertain about all that too.
*  I'm also very generally speaking, skeptical of government regulation. In this case, I feel like
*  I might rather go down trying than not trying, but it does seem also at the same time, like we
*  very well could have a lot of unintended consequences or even negative consequences.
*  And I definitely share your enthusiasm for it.
*  One worry I have is if we believe this is going to be powerful as we think it is,
*  regulation then puts you at a disadvantage against like less favorable actors. Right.
*  And that's true on a nation state level as well as a company level. So if open AI decides to be super
*  safe, then like some other research like group is going to like not worry about that and just go
*  faster. And they may have maybe less than benevolent thing with nation states, right? If America
*  regulates compute and AI research, another nation state will not. And what happens at the critical
*  crossing of capabilities when it gets able to sell bootstrap. So it's a very difficult problem
*  and the implication of regulation is like, may not play out the way people want it to.
*  Yeah. Again, my instinct there is if we're going to go down, I'd rather go down trying to cooperate
*  with China than racing China to create godlike AI. But it doesn't mean you're wrong. It very well
*  could go down that way. I know we're just about out of time. Any other either big picture questions
*  or any other items you wanted to touch on that we didn't or anything you want to plug before we
*  break? I know. I think we covered a lot, but anyway, yeah, if you're a mid-size company,
*  pay for runway. I was really impressed with the demo. We're in the pipeline. So I am plus one,
*  at least in the lead column. Let's see what our key stakeholders have to say about that. But very
*  cool product, really interesting application of AI in a high importance area. And I think definitely
*  sign of things to come. So Sikhi Chen, founder and CEO of Runway, thank you for being part of
*  the cognitive revolution. Thank you, Nathan. It's been great. It is both energizing and
*  enlightening to hear why people listen and learn what they value about the show. So please don't
*  hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform
*  of your choice.
