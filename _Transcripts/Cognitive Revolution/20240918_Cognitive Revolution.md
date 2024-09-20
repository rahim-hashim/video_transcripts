---
Date Generated: September 20, 2024
Transcription Model: whisper medium 20231117
Length: 7435s
Video Keywords: []
Video Views: 674
Video Rating: None
Video Description: In this sponsored episode of The Cognitive Revolution, Nathan interviews Andrei Oprisan, Engineering Lead at Agent.ai. They explore the cutting-edge world of AI agents and their impact on the future of work. Andrei shares insights on language model limitations, best practices for building AI agents, and Agent AI's vision as a professional network for AI agents. The conversation covers technical details like fine-tuning models, vector database choices, and privacy-preserving techniques. Don't miss this deep dive into AI's role in transforming industries and the skills needed in an AI-augmented workplace.

Check out Agent.ai website here: https://agent.ai

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:

Weights & Biases Weave: Weights & Biases Weave is a lightweight AI developer toolkit designed to simplify your LLM app development. With Weave, you can trace and debug input, metadata and output with just 2 lines of code. Make real progress on your LLM development and visit the following link to get started with Weave today: https://wandb.me/cr

Oracle: Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

Brave: The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky: Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Squad: Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

RECOMMENDED PODCAST:
This Won't Last - Eavesdrop on Keith Rabois, Kevin Ryan, Logan Bartlett, and Zach Weinberg's monthly backchannel ft their hottest takes on the future of tech, business, and venture capital.
Spotify: https://open.spotify.com/show/2HwSNeVLL1MXy0RjFPyOSz

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsors: Weights & Biases Weave
(00:01:28) About the Episode
(00:05:36) Introduction and AI Agents Overview
(00:07:02) Current State of AI Agents
(00:11:30) Building and Optimizing AI Agents
(00:16:48) Agent.ai Platform and Marketplace (Part 1)
(00:19:01) Sponsors: Oracle | Brave
(00:21:05) Agent.ai Platform and Marketplace (Part 2)
(00:26:06) Customization and Context for Agents (Part 1)
(00:31:12) Sponsors: Omneky | Squad
(00:32:38) Customization and Context for Agents (Part 2)
(00:33:34) Business Model and Monetization
(00:36:53) Tech Stack and Development Process
(00:43:55) Future of Work and AI Impact
(00:54:14) Privacy and Data Security
(01:03:46) Fine-tuning and Chain of Thought
(01:14:30) Capturing Human Reasoning Process
(01:21:00) Preparing for Rapid AI Advancement
(01:40:58) AI's Impact on Jobs and Society
(02:00:16) Closing Thoughts and Future Outlook
(02:03:33) Sponsors: Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# The Professional Network for AI Agents, with Agent.ai Engineering Lead Andrei Oprisan
**Cognitive Revolution:** [September 18, 2024](https://www.youtube.com/watch?v=48a_aPxucwk)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Today's episode is brought to you in part by Weights and Biases. As a developer, the journey
*  from concept to production-ready large language model apps is fraught with challenges. Dealing
*  with unpredictable large language model outputs, correctly handling PII, and ballooning API costs
*  can all be blockers to shipping your next AI-powered feature. Weights and Biases Weave is a
*  lightweight AI developer toolkit designed to simplify your large language model app development.
*  With Weave, you can trace and debug input, metadata, and output with just two lines of code.
*  Weave helps you run rigorous evaluations and securely manage all of your data sets and system
*  configurations, so you can focus on what matters most, iterating and improving on your large
*  language model-powered applications. Plus, Weave integrates seamlessly with your favorite APIs and
*  libraries, including OpenAI, Anthropic, Mistral, Cohere, Langchain, Llama Index, and more.
*  So make real progress on your large language model development. Visit wnb.me.cr to get started with
*  Weave today. That's wnb.me.cr and thanks to Weights and Biases for sponsoring this episode.
*  Hello, and welcome back to the Cognitive Revolution. Today, I'm excited to share my
*  conversation with Andre Opressant, engineering lead at Agent AI, a fast-growing and currently
*  free-to-use AI agent platform that describes itself as the professional network for AI agents
*  online at agent.ai. Before diving in, I want to take a second to note that this is a sponsored
*  episode, our second sponsored episode out of more than 160 total episodes published over the last
*  year and a half. Our goal with sponsored episodes is to create a win-win-win for the show, for the
*  sponsor, and most importantly for you, the audience. I consider myself very fortunate that many startup
*  founders are currently interested in doing the show, and as such, we have the luxury of reserving
*  sponsored episodes for companies that I personally find very interesting and genuinely expect to
*  resonate with the audience. I see their sponsorship more as a way to cut to the front of the line
*  so that their appearance on the show aligns to their important company and product announcements
*  more than a go or no-go decision criteria per se. Agent AI is a perfect example of such a company.
*  It is a well-resourced and sophisticated effort backed by HubSpot CTO Darmesh Shah with a number
*  of intriguing angles on AI agents and the future of work more broadly, and I think today's episode
*  really exemplifies the win-win-win that I hope to create. I prepared for this conversation with the
*  same depth of exploration that I always do. I tried every last agent AI product feature that I
*  could find, wrote an outline of more than a thousand words of questions, and challenged Andre
*  to go deep on the technical details. In the end, I'm glad to say that he really delivered.
*  Highlights from this episode include Andre's breakdown of the current limitations of language
*  models when it comes to planning, out-of-domain detection, and error recovery. His analysis
*  recorded just days before OpenAI's big O1 announcement foreshadows their release and
*  suggests that a good chunk of what was previously missing might now be available. Andre also shared
*  recommendations for how to approach building AI agents, including the importance of narrow,
*  well-defined tasks and robust benchmarking. He shares insights on creating effective prompts,
*  structuring agent workflows, and implementing feedback loops to improve agent performance over
*  time. We also discuss agent AI's vision for the platform, including the concept of a professional
*  network for AI agents where agents have their own profiles and their plan to become a marketplace
*  where developers can build and monetize agents, as well as how this could democratize software
*  creation for everyone, potentially allowing even non-technical users to build sophisticated
*  AI-powered solutions. We also exchange best practices for fine-tuning models, and I was
*  very intrigued to hear Andre's best practice of using small models locally before going on
*  and scaling up to larger proprietary models in the cloud. We get a detailed explanation for why
*  agent AI uses Pinecone over Postgres's PG Vector for their vector database, touching on factors
*  including ease of use, scalability, and performance under different workloads. The kind of thing that
*  you can really only hear from someone who has tried a wide range of solutions. We also discuss
*  privacy-preserving techniques for AI. This is something that I really should learn more about.
*  We covered Apple's new approach to encryption of user data and got Andre's thoughts more generally
*  on the challenges of handling sensitive data in a way that unlocks the power of AI while still
*  maintaining user privacy. Finally, we conclude with an earnest big-picture discussion on the
*  future of work and AI's role in it. We explore Andre's vision for how AI agents will integrate
*  into various industries, the potential impact this could have on jobs, and the skills that
*  will become increasingly valuable in an AI-augmented workplace. We even touch on some of the ethical
*  considerations and potential societal impacts of widespread AI agent adoption. As always, if you're
*  finding value in the show, we'd appreciate it if you take a moment to share it with friends,
*  write a review on Apple Podcasts or Spotify, or just leave us a comment on YouTube. Of course,
*  we always welcome your feedback, including your thoughts on our experiment with sponsored episodes.
*  You can send us a note via our website, cognitiverevolution.ai, or you can DM me
*  on your favorite social network. Now, I hope you enjoy this discussion, which covers AI agents from
*  all angles with Andre Oprisson of Agent AI. Andre Oprisson, engineering lead at Agent AI,
*  online at agent.ai. Welcome to the Cognitive Revolution. Thank you, Nathan. Excited to be here.
*  I'm excited for this conversation. Obviously, AI agents have been a super hot topic since the
*  release of GPT-4, and so much time and energy and thought has gone into them. So far, I think we're
*  still waiting to see exactly how this is all going to play out. As we anticipate new models
*  and new capabilities and potentially an agent future coming at us sooner rather than later,
*  you guys have built an entirely new from the ground up platform for AI agents. I am excited
*  to get into every aspect of it. Awesome. Excited to share more about it. So maybe for starters,
*  what is an AI agent? How do you define them? I think there's so much confusion about this
*  from just post-GPT-4 a year and a half ago almost now. We saw these projects like BabyAGI
*  and AutoGPT, and the idea was like, you just give the agent a high level goal and it'll go off and
*  make its own plan and find its own way, and hopefully it'll be successful. Fair to say,
*  at this point, that hasn't quite worked. Probably still will. But in the meantime, the definition
*  of agent has slid around and been fudged by so many different people that I think it's really
*  helpful just to get clarity right now on what do you mean when you talk about building AI agents?
*  Great foundational question. And again, I think it's early. I think this definition will continue
*  to change every three to six months. And so I think six months from now, we'll tweak it
*  slightly. But my definition is semi-autonomous system that can perform tasks or make decisions
*  on behalf of a user. I do think it's extremely important to have these agents do very small
*  tasks, something concrete, something extremely bounded versus I think the first iterations,
*  very open-ended, very hard to define goals or have some very broad goals.
*  And this scenario and this future that we envision, we envision having these semi-autonomous
*  systems that do have the human in the loop. There is some work that the agent is going to do.
*  What are your thoughts on the performance? How do we benchmark these things? What success
*  for me versus for you, Nathan, might look very different even using the same kind of agent given
*  our expectations, given our background, given the kind of data that we want to feed it to
*  personalize, for example. I think the more narrow, the better. The more narrow definition,
*  the more narrow the set of capabilities an agent has, the more likely it is to succeed.
*  And then we build on that. We'll have, I believe, many, probably dozens and even hundreds of
*  very small specialized agents that will help you do your job on a daily basis, for example,
*  from reading what do I do as a white-collar worker. I read my emails in the morning.
*  I prioritize them based on what I value, what I value changes day to day, week to week,
*  month to month. There's some strategic, there's some tactical. And as you think about even
*  prioritizing something as simple as emails or reading your calendar and saying, here's a summary
*  of what you should, who are you meeting with today? It's Nathan for this podcast. You're meeting with
*  Dharmesh for agent.ai strategy session and so on and so forth. That context is going to change
*  over time. And I think the more narrow these agents are, the better. And over time, we'll
*  introduce more abstraction to be able to decide which agent is going to get which part of that job.
*  But I think we're going to be able to advance this much quicker if we don't try to oversell them and
*  say they're these autonomous systems that can do everything under your sun. I don't think that's
*  the case. I think that's a recipe for disaster, for hallucination, if not for disappointment
*  altogether. And having very concrete, small, benchmarkable agents with clear or broadly
*  well-defined data sets is going to get real work done faster. The question that I want to maybe
*  follow up on is you spend all day, as you said, building agents. So how do you think about what
*  the right scope of action or freedom is right now for them? Because I see that it's not like a binary.
*  One of my mantras is AI destroys all binaries. We can never have these clean categorical
*  distinctions anymore, I'm afraid. And this applies to agents too, where at the zero point of agency
*  would be a fully deterministic workflow with no models involved at all. It's just pure code.
*  And then on the other hand, you have a baby AGI type thing where you say,
*  go make money on the internet and it hopefully comes back with money for you.
*  And a lot of the failure seems to be people not really knowing where they should be on that
*  spectrum. I think there's a lot of success with things that you might just say are workflows with
*  an AI component. I had Sikhi Chen from Runway On and he talked about his AI SDR and its lead comes
*  in. We're going to ping this API to get data back and then we're going to put that into the
*  prompt. And then the final thing is language model creates an email for that person. I think
*  it was like 16 steps or something that he strung together. But I believe that they were all
*  deterministic. I don't think at any point in that process was the AI actually trusted to say,
*  I'm going to go this way or I'm going to go that way. It was like everything is prescribed
*  and the AI is getting tasks within a workflow. That I feel very confident can work today.
*  Do you think that is the farthest that we can go today or can we go further? How far do you
*  think we can productively push this semi-autonomy? I think we were still missing from a
*  clearly algorithmic and LLM evolution standpoint. I think we're a few evolutions away from being
*  able to fully move away from this highly prescriptive approach, which I do believe that's
*  where we're going to live for the next six to 24 months. We'll see if the new model coming out in
*  a few weeks from Chai GPT will change that in terms of the planning. But LLMs are fairly bad
*  at actually planning and actually explaining, helping a person understand where that uncertainty
*  is. It's very confident in giving you some answers. It doesn't know just how confident it is or
*  how it should doubt itself. I think that's a very big missing piece. Having some robust
*  out of domain detection as well to understand when it's not marketing anymore, it's sales.
*  It's a different kind of task and a different kind of domain to think through that deep planning.
*  It's absolutely foundational here for autonomous agents and we just don't have that yet.
*  There's also, as you think about this reliable self-correction, just how confident we are and
*  what the ground truth looks like. Being able to then self-correct will be doable or at least we'll
*  have some insights into what that looks like. Again, more guided autonomy. Lastly, I think the
*  part that's missing the most, and I think that this is where we're building towards that future
*  with workflow tools, is building more ground truth but also building ways to benchmark these outputs.
*  Let's say again, you and I are using the same kind of agent. From my context, what really good
*  looks like or really bad looks like is subjective. But I can tell you, you know what? I want more of
*  this. I might not know exactly why we got there, what of the 10, 20, 50, whether it's concrete
*  sort of steps that were taken or decisions that an LLM or some LLM took. I think it's important to
*  be able to explain those, to be able to reproduce them, to be able to then benchmark them to say,
*  you know what? We did a VIR a little bit left this way. For the next step, let's tack the other way
*  a little bit and guide closer to mathematically what we could describe as the objective right path
*  or more of the objective right path. When you're running this, let's say it's a million different
*  simulations for the same kind of work to be done, which again, if you have structured agents that
*  are essentially workflow tools on steroids, you can get that fairly quickly and a good enough sort
*  of answer. The benchmarking tied with the out of the main detection and some of the long-term goal
*  definition to then do the self-correction, I think those are the three big pieces that are needed
*  before we can have anything resembling sort of autonomy. But that doesn't mean that these agents
*  can't do a lot of work very well and really accomplish concrete business goals, better,
*  faster, cheaper, and really augmenting those human workflows themselves. Some of our most
*  effective agents own agent.ai and as we built more and more of them, we've actually learned that the
*  more prescriptive we are, the better they perform, the better the feedback is from both objectively,
*  from NPS surveys and other data points like that, but also very concretely in terms of feedback.
*  To give an example from our flagship agent on agent.ai, you can enter any company name or
*  domain name and we'll give you a full company report, everything from some general information
*  about the company website, founding time, the founders, the citizen makers, their emails,
*  etc., all the way to how does that traffic grow on LinkedIn and X and other platforms
*  down to researching their product offerings and price points and how would I sell to someone
*  at that company if I'm this other company trying to sell them something, give you enough of that
*  context. That alone, this agent that we talked about has 20 different sections. We've got over
*  100 different steps, mostly very prescriptive, but also there's some LLM flexibility now that
*  we have structured outputs where we can say we can trust more and more these LLMs to give us their
*  creative answers, but then make sure that it fits within certain data structures. It fits within a
*  list that we can quantify, have certain attributes that we really care about to then be able to
*  iterate that a number of times, a number of models, this mixture of experts, to then be able
*  to say, okay, roughly, what do we think are the top three competitors? If you were to try to compete
*  with this company, how would you do it, etc.? You can then answer those kinds of questions and
*  support those kinds of use cases much more consistently, much better at scale. And that's
*  part of what we've seen works as we continue to evolve these agents. It takes time. Unfortunately,
*  we're early, and so it takes a lot of time, a lot of iterations to get this right. And part of what
*  we're trying to do at agent.ai is provide the platform, provide the WYSIWYG drag and drop
*  workflow building toolkit, as well as some of the more creative LLM-based actions that will then fit
*  to certain kinds of outputs, structured outputs. You could drag and drop different kinds of
*  responses and visualize it in an interesting way. And all you have to do is just describe the steps
*  if you want to. You can drag and drop and customize for an expert, or you can just describe and say,
*  I need an agent that will read, I don't know, podcasts for me, summarize the key learnings.
*  Here's the topics that I really care about and focus more on those specifically. What I just said
*  there, those 30 seconds worth of description, maybe some tweaking should give you a full agent
*  that will do that concrete task very well. Now, the broader the sort of tasks are, or the less
*  structured, the less likely to succeed. But I think that's what we build upon. Those are the MVPs,
*  and then more mature versions of these agents will eventually be able to do even more work
*  across a number of domains. If we can tell when we're out of the domain, let's look at podcasts,
*  let's not look at YouTube videos, let's not look at emails, because those are different kinds of
*  mediums. The way we craft those prompts look different. The kind of benchmarking data that we
*  have is likely very different. And how we benchmark those results and then potentially fine tune
*  a model to really be able to give even 5% or 10% higher accuracy is going to be different. So
*  I think these are the building blocks. I think we're going to get better, but I do still believe
*  we need to live in a sort of workflow oriented world for some time until we build these other
*  LLM missing capabilities that will then allow for more autonomous execution end to end.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  This episode of the cognitive revolution is sponsored by the Brave Search API. You may know
*  if Brave has an alternative to Chrome, but did you know that Brave has its own independent search
*  engine powered by its own 20 billion page index of the web? The Brave Search API gives developers
*  reliable and affordable access to programmable web search, auto suggest, spell check, and more
*  with flexible plans for all types of use cases from rag search to automated business intelligence.
*  On top of that, it's up to three times cheaper than Bing, all without compromising on quality,
*  speed, or reliability. Over 700 businesses, including Cohere, Chegg, and Kagi rely on the
*  Brave Search API. And a recent survey showed that 94% of customers would recommend it to their peers.
*  To start building apps with the power of the web, sign up at brave.com slash API and get up to 5,000
*  free monthly calls. On the pieces that are missing from the language models in terms of their ability
*  to succeed today, it was effective planning, test decomposition and planning out of domain detection.
*  It knows when it's going to get itself in trouble. The final one was error recovery, basically,
*  figuring out when something's not going right. Is there a way to come back and overcome that
*  some way or another? That is a pretty good wish list. It sounds like you don't think that will be
*  on tap with the much anticipated strawberry model, whatever that might be. You're building with
*  the expectation that those things are not immediately going to be solved.
*  We're building with that in mind. I love to be pleasantly surprised. To the contrary,
*  again, we don't really know just how quickly I'm there. There's obviously a lot of research
*  in each of these domains. If interested, I can share what someone that research looks like. I'm
*  fascinated by this. My background in machine learning is actually building mostly the reliable
*  self-correction type of algorithms. And so being able to define what is that ground truth? How do we
*  essentially do surgery on neural networks to then be able to adjust and do that at runtime instead
*  of retrain a whole GBT 4.5 or 5.0 that takes a lot of time, a lot of money, even fine tuning
*  some very small models that can take time? What would essentially live patching that look like?
*  There are some advancements there, but we're not there yet. We're not there in terms of being able
*  to apply these broadly in this kind of class of LLMs that we have today. I think we're going
*  to get there. I think surely in the next five years or less, we'll likely have all of these
*  and many iterations of these capabilities. But I do think that they're critical. And if you can't
*  define what ground truth looks like and you can't tie it to the planning aspects, then I think it
*  cannot really evolve as much as we want it to. It'll be creative. I think and maybe there's this
*  definition of intelligence, definition of creativity will evolve. I think it needs to evolve,
*  but it's probably not what we expect it to be in terms of that sort of human level autonomy,
*  that human level intelligence. And these are some of the building blocks. Ian Lacune, the head of
*  AI at Metta and former NYU AI professor, he's been talking about this for years. I remember
*  being a student in his class where that was the focus of the research of what they were doing.
*  And this is 20 some years ago and some of the work that he did on convolutional neural nets
*  and aiming to create ways of discerning what that error correction needs to look like and that
*  some of the boundaries on domains and even being able to quantify within the same domain
*  on the topics, how well you're penetrating the domains and when you're maybe blending
*  different kinds of topics that shouldn't be blended together because again, it's mixing the wrong kind
*  of science ingredients in terms of logic. It doesn't build where you think it builds, but
*  it'll very confidently think that it's doable. I think this research is decades in the making and
*  I still don't think we have a good enough, fast enough sort of solution. We do have some solutions
*  and highly specialized domains and highly verticalized, but to be able to do even generic
*  planning across trying to build an agent with a concrete set of steps without turning it into
*  essentially a workflow builder with predefined set of options is still very hard. I think we need
*  some of those pieces before we can truly trust or quantify how much we should trust some of those
*  outputs. People say when you're building AI powered or AI enabled software, use the AI only
*  for the part that absolutely requires the AI and use code everywhere else where code can possibly
*  work. And I think what I heard from you was largely consistent with that. We're in the workflow world
*  for now. We're not in the baby AGI. It's not about to turn into grown up AGI in the immediate term,
*  but I also did notice one really interesting aspect of the platform to me that I haven't seen
*  done this way very much at all. I've tried a lot of things and looked for this actually,
*  because I feel like it's a little bit of a leading indicator of who is thinking ahead versus who is
*  the sort of filter step that exists within agent AI. And obviously people have had a lot of different
*  experiences with different no code platforms. In general, there's often a thing where it's like,
*  we get to a certain step, we need to advance conditionally. Maybe we stop under a certain
*  condition. Maybe we advance under a certain other condition. Maybe we fork the workflow,
*  depending on whether it's A or B or what have you. So that experience is pretty familiar.
*  Typically, it is done with hard coded rules. That, of course, was the only way we could do it until
*  quite recently. And so you have these exact match or contains match or regular expression
*  match sort of options. What stuck out to me in the agent AI version of this is that it was using a
*  language model to make that sort of distinction. So when I get to the filter or the decision step,
*  instead of needing to work up a regular expression, even better still would be if I could just express,
*  this is the gist of what I'm looking for and I want to advance under this and not advance
*  under that. And then I could perform that sort of judgment on top of unstructured data, right? Or
*  semi-structured data. As far as I can recall, implemented at one other company and they were
*  in a different space, but still had that sort of, we're going to trust the language model to make
*  this decision as to whether to continue or how to route. To put that in the form of a question,
*  what kind of guidance would you give people for what to trust the AI to do? How reliable do you
*  find those filter or those sort of routing decisions are in today's world? And how did you
*  decide to go ahead and take the leap to trust the AI to do that as opposed to just implementing
*  regular expressions? So I think for some of these conditional logic steps, LLM is actually
*  very good at understanding complex, if then else looping that's coming soon, but the same thing
*  for looping retry this or give me 50 variations of ad copy or 10 variations of emails and then
*  send them out, A, B test them for me, et cetera. Like some of those repeatable, if then do this,
*  otherwise do that conditional logic to repeat. Human beings are not great at explaining in steps
*  all the different paths that something could take. And actually LLMs are very good at that.
*  There's some really good data sets out there as well, where you can actually fine tune models
*  based on conditional logic, just hundreds of thousands of millions of these. You can get
*  super complicated with all sorts of nested logic, jumping out of a loop if something else were to
*  happen and so on. Even a two level nested, if then with continue blocks with in a while loop,
*  with a for loop, watching for certain system words, et cetera, with a workflow tool, very
*  hard to even myself being an expert and living this every day, it'd be hard for me to replicate it
*  and make sure that it actually works the way I conceptualize it working. But I can explain that
*  we can have a conversation about what I expect it to do. And LLM does a much better job than I do.
*  And this is actually properly benchmarked. We tested it and it is true for certain kind of
*  logic like this. They're very good. But when you try to go deeper planning, we're not there yet.
*  But there are some of these steps where I do think we have to push outside of our comfort zone and
*  embrace AI and benchmark it, right? And build more of this ground truth and figure out, okay,
*  can it do a good job, a good enough job, a better job, steeper, faster? If so, that's a wonderful
*  tool. I love to use wonderful tools that make me faster. I can do more things that I really care
*  about instead with my time, right? That's the way that I would look at these things, as well as do
*  mundane and computationally complex things like go and publish different posts on different
*  social media platforms and figure out what are the metrics, what kind of posts got more engagement
*  and why. Be my social media manager, do a job well for me versus I'm going to the same thing and
*  buy different platforms or maybe use some kind of platform to aggregate that. But I still need to
*  slice and dice some of the structured data. Wherever we have the structured data, I think these LLMs
*  can be very good, but also translating unstructured but predictable data and logic
*  flows into structured data outputs, we should embrace more and we should always push the envelope.
*  And that's how we think about building these agents and the kinds of capabilities that we
*  continue to add to agent.ai. It's how can we figure out and give you more of those tools so that
*  you're not spending time trying to figure out how do I build this complex workflow. You can talk to
*  it where it makes sense to and have it actually build the logic and give us some flexibility
*  within reason. In the back end, we always translate that to structured data, logic gates, and then so
*  on that you need to be able to run actual code and to end across a number of steps.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey everyone, Eric here. In this environment, founders need to become profitable faster and
*  do more with smaller teams, especially when it comes to engineering. That's why Sean Lennahan
*  started Squad, a specialized global talent firm for top engineers that will seamlessly integrate
*  with your org. Squad offers rigorously vetted top 1% talent that will actually work hard for you
*  every day. Their engineers work in your time zone, follow your processes, and use your tools.
*  Squad has front-end engineers excelling in TypeScript, React, and Next.js ready to onboard to
*  your team today. For back-end, Squad engineers are experts at Node.js, Python, Java, and a range of
*  other languages and frameworks. While it may cost more than the freelancer on Upwork billing you
*  for 40 hours but working only two, Squad offers premium quality at a fraction of the typical cost
*  without the headache of assessing for skills and culture fit. Squad takes care of sourcing,
*  legal compliance, and local HR for global talent. Increase your velocity without amping up burn.
*  Visit chewsquad.com and mention Turpentine to skip the wait list.
*  I think there's so many data points suggesting that we are entering an era when anyone quote unquote
*  will be able to build pretty advanced software. I find that to be extremely fascinating and I come
*  at it from a lot of angles. There's of course many coding assistant tools and Claude can code
*  remarkably well, but then there's also this sort of intermediate hybrid form of the workflow with
*  the AI sometimes playing the router. And then there's these questions of like, how does that
*  get built? I think you guys have a really interesting angle on that as well where you've
*  talked about having the AI do it. How well does that work? How have you gone about the process of
*  dialing it in? I recently gave a, one of my recent episodes was on AI automation and I'm curious as
*  to what tips you've learned for automating the process of creating an agent workflow because
*  that's a pretty advanced use case and I bet I could pick up some tips. But then you also have
*  the kind of marketplace dynamic, like the form factor of the product is interesting that when
*  I log in a header of the website, I have agent network and human network. And so I can go browse
*  around and explore different agents that are already there and published and shared, and I
*  can go look at people and what they've created and parse it in different ways. So I'm really
*  interested in like, how well does the AI generated workflow stuff work and what have you done to dial
*  that in? But also interested in is that what people want or are you finding that people are
*  more gravitating toward like, what has Dharmesh done? And maybe I can just borrow from him. And
*  then there's also an editing layer on top of that too. I mean, with my company Waymark, we do
*  basically full generations of marketing videos for small businesses. One of the frontiers that we're
*  looking at implementing now is, okay, you've got a video, but now you maybe want to give some
*  feedback on that video. Maybe you want to have some changes made to it. We have a UI where you can do
*  that, but I certainly imagine a future where I would say, the second scene isn't quite right,
*  make it more like this and have the AI do all that stuff and never have to touch a UI.
*  And it seems like you're definitely planning for that is I can see that in the product where
*  there's just this ability to explore, discover. I don't know if yet there's a way to say tweak
*  this to my circumstance, but anyway, you can unpack that in multiple directions.
*  It's like you're reading our roadmap, which we'll make public soon. But essentially, yes,
*  right now we have a small number of finely tuned agents, finally curated every single one being
*  hand-built with workflow tools, say, get this user input. And then when you get that input,
*  get this data from this data source. And then when you get that result, feed it to an ILM to do
*  something with some kind of prompt, then you turn that into structured data, then you use some other
*  source and eventually show user the thing they're looking for. Where we also have a way to build
*  agents in the same smart action builder that we have by just adding with the builder. And you can
*  say, let's ask the user for the YouTube video and it'll fill in the four different parameters
*  that you need for that step. For example, what is the heading? What is the variable name? What do
*  we show the user, et cetera? Maybe how many YouTube videos to crawl? Is it a YouTube video
*  or is it a channel? If so, how many videos deep should we go? What kind of topics should we care
*  about? You can just say that in the chat and it'll fill in all sorts of toggles for you and
*  do a fairly good job. We have some internal benchmarks. It's probably 80% good. That might
*  not be good enough or that's not yet good enough to make that available more broadly. But we also
*  will make it available over the next few weeks. This idea of templates. So for certain verticals
*  in marketing and sales and customer service, et cetera, we're going to have example agents
*  that users can publish either for users to use as they are. So where all that logic stays closed
*  and you just interact with it and that's it. Or make it open so anyone can make their own copy of
*  it, tweak it and say, you know what, what if I want to customize it for my use cases? What if I want to
*  add three more steps and remove two over there and then tweak the output to maybe send me emails of
*  the results instead of just showing me website on some kind of job and so on. That is all coming
*  very soon over the next few weeks, definitely in September. From there, I think the agent builder
*  becomes more useful as just a creative open-ended tool because it will have thousands of these
*  templates to feed upon. To be able to say, just you can describe what you want and it will have
*  a larger library of ground truth to really use to be able to say for this version of
*  agents that you'll build an agent.ai, it'll be able to put those steps together much more accurate
*  than the 90% plus stage with some of our testing and we'll see once users get their hands on it.
*  But I do believe we need these templates. We need people to build their agents and build the sense
*  of community as part of what we're looking to build here with agent.ai. The long-term vision
*  here is for agent.ai to be that platform where all those agents can live. We'll figure out
*  what's in it for the creator. How do we pay them? How do we drive that exchange of goods? Very
*  similar to how the Apple Store drives visibility. We'll guarantee you distribution. If you want
*  100,000 eyeballs a month on your agent, that comes free. If your agent is also free for everybody to
*  use, then maybe you get the feedback right from the customers and you can improve it that way.
*  Maybe you have a pro version that can do some more things. Maybe you enable certain personalization
*  and customization. It's just very similar to these app models that we're all familiar with and they
*  seem to work fairly well. I think that model will need to evolve for an AI agent marketplace
*  where, yes, some of the parallels do work, but how do you really charge? Is it per app? Is it a flat
*  fee? Is there some ref share of these credits that you need to use? Because one agent does not equal
*  another agent if you're using 10 data sources and 50 LLM steps with very large context versus
*  it's a very simple thing. Do some research for me. That's all part of what we're actually
*  experimenting with. We have a small alpha, I would say, builder group at this point. We're
*  not quite beta yet. We'll have beta over the next few weeks. We'll bring in even more users
*  into our platform and have them start building more and more agents. We're obviously always going
*  to seed the market with dozens of agents just based on feedback, based on what market research
*  we also do. But from there, we really want the market dynamics to take over where we're getting
*  close to tens of thousands of users now. I think we're at over 40,000 as of earlier this week. It's
*  growing very fast. And so the market is now getting enough momentum where we have builders
*  building more useful agents. We have a review process, just like the app store has a review
*  process to make sure the apps do what they say they do and they're not siphoning off personal
*  data of customers and so on. You want some guardrails. That's part of what we'll offer
*  through the platform, but also make it easy for anyone to build agents. And like you said,
*  what we love about this future is that you shouldn't need to be a developer to build agents.
*  It's all about citizen AI builders. Any person who has a need, just say you can build a form
*  to capture emails, to answer some questions with all the WYSIWYG sort of systems out there.
*  We want to make it as simple as that, even simpler. We just describe what you need. You'll have
*  dozens or hundreds of examples to pick from as well, if maybe that's a better path, examples
*  and such, as well as documentation, as well as that community of people who have tried different
*  things. Some things are not as successful as others. We're trying to build that community
*  because it's a space that will continue to evolve, I think, very quickly. You can go from zero to
*  expert in weeks. A lot of it has to do with how willing are you to fail fast, try some different
*  things, get some good examples, right? I think being hands-on, tweaking these things and making
*  work for your use cases is going to be what's going to make H&A.AI the choice platform for your
*  agents versus some of the more specialized point solutions, which also have, I think, great uses.
*  I just don't think you're going to have as much adoption long term because it's going to be harder
*  to acquire those customers, keep them engaged, continue to evolve, right? And as this underlying
*  technology also evolves, these LLMs will hopefully be able to do planning, or at the very least,
*  some of the error correction pieces. You're going to blend domains very quickly. You're going to have
*  many specialized agents, yes, but also something that can coordinate just across on top.
*  And we worked just with this model. We have this idea of adding agents to your team. I have a team
*  of agents. Maybe this is my social media team of agents. Maybe this is my marketing team of agents.
*  Maybe this is my school research doing my MBA right now. I need different kinds of specialized
*  agents to look up case studies and do some deeper analysis of data and present it in a consistent
*  way. How do we divide and conquer those tasks together in a team? And that's why we're positioning
*  agent.ai as a professional network of agents. If you believe that work is going to continue to be
*  hybrid, so an office and not an office work, we believe agents are going to be a part of that.
*  We believe that combining agents and having them do professional work means that we need a
*  professional social network for these agents, where you can really understand what is this agent
*  capable of? What are actual employers of those agents? What are they saying about that agent?
*  Is it a good agent? Is it a bad agent? For a lot of these other solutions, it's very hard to tell
*  how good are they. You may have some reviews, but over time, I believe this approach with an
*  actual social network with endorsements and maybe some certifications and so on will be the right
*  solution. It's useful to ask for actual business use cases. Yeah, certainly Dan, there are some
*  echoes of HubSpot where there's very few, if any, ecosystems in terms of platform and service
*  provider and kind of market dynamics on top of it that have been as successful as HubSpot has been.
*  And so I can see how the DNA there is definitely teeing you guys up for success with that model.
*  I want to just dig in for a second on the performance optimization around
*  getting AI to help build workflows. That is a challenging use case. And you mentioned
*  you've given multiple tips along the way. One was just be really explicit in your instructions. That
*  applies presumably for every scenario. It's not something that people necessarily are super great
*  at. So it's, again, this is definitely a reason I think that a marketplace dynamic could be really
*  helpful to people. But just more generally, I would assume this is the most core AI you're working on
*  is the AI that makes these workflows. What have you found to be the big performance enhancers for
*  that scenario? Explicit instructions. You mentioned also like having a bunch of examples. We know that
*  large language models are few shot learners to quote a famous paper title. What examples are
*  you doing rag on all those examples? If so, is that working? I hear a lot of failures on rag more
*  so than I hear successes. Are you fine tuning it? If so, what is working well there? This is something
*  I think folks who listen to this podcast, many are building their own highly specialized but
*  performance critical specialist model and they're looking for nuggets they can use to squeeze out a
*  few more points. Actually, rag for us so far has worked surprisingly well. That's how we've developed
*  that piece of functionality where we first essentially developed a few hundred examples
*  from very simple to very complex. That's our sort of template library if you will. We've then built
*  out a very simplistic benchmarking tool where we can say here's my goal, here's the kind of agents
*  that we would choose for each of these objectives that we have. How we selected that tool because
*  this specific ask actually means that I need YouTube data and Google news data for example.
*  And explaining that, I think making that part rag datasets and then as part of that as well.
*  The challenge with rag is, and there's two challenges, things that we found useful is number
*  one making sure your document size and the overlap are tuned. And so having too small of a window,
*  having too small of a document with not enough overlap can actually cause a lot of issues. For us,
*  the document size is well defined because we know just how big these objects are. Our average agent
*  has six steps and so each step looks like this six attribute JSON object and then you can do the math
*  and model out. Okay, so how big should these documents be to make sure that we're always,
*  they're just big enough, you don't want too much overflow. And then the last bit of advice there is
*  figure out how you benchmark the results. So you're going to have some kind of rag system,
*  you're going to maybe go the other path with fine tuning. We've tried that too.
*  Actually, you got a lot more false positives in that scenario. And so that again, there's pros
*  and cons to both approaches. It really depends on the kind of data that you have. And for our use
*  cases, given that everything was fairly predictable set of intents, rag tends to do a little bit better
*  because actually we got worse results by fine tuning versus by using some of the larger models.
*  So it's interesting research there, but building some level of evaluation tool and then I think
*  is critical to be able to say, even if you got the right answer, you got the wrong answer,
*  would you know it? And would you be able to quantify it to then be able to do some of this
*  other tuning? That's critical. And so whether that's another LLM call where you can say,
*  hey, here's a few shot examples of what really good looks like in really bad, what it looks like,
*  and then you make it give you the answer in a JSON format where it's one of three different enums of
*  good, bad, and I don't know, or some kind of numerical scale, whatever kind of works.
*  That is probably good enough to be able to solve for a lot of these complex use cases.
*  But then you have to build your ground truth. So now we do have some benchmarking toolkit. We have
*  this rag system. All of this is like 100 lines of code, maybe 200. It's not complicated to build
*  out. Assuming you have it, now you have to build enough of those examples to then be able to
*  babysit the system to then get a bunch of output, figure out, okay, does this actually make sense?
*  Let's go back. Let's revisit each data point and tune it again. Can we get predictable output?
*  Is the temperature low enough? And how much context should we give it to consistently get
*  good enough answers? And using models that are not versioned, that are not snapshot it, if you're
*  tying yourself to GPT-4 latest, they do make changes every now and then. You might be using
*  an entirely different model at that point, or like a different sort of checkpoint versus
*  try something local or try something hosted where it's a llama two or three at a certain point in
*  time. Very small language models. Some of the DeFi models are phenomenal for this, where you can just
*  run on device for these tests. And we got more consistently good answers that way. And then we
*  figure out, okay, how do you replicate that using Claude with the larger context? Because that's
*  actually really important for personalization. And we use that now for most of our self-building
*  approach. And we first started with these small language models, and then we worked our way back
*  to the larger ones where we need to be even more explicit with the prompts and then tune our RAG
*  approach a bit to get the same answers. You can't always use the same approach to RAG because how
*  you prompt and the context is a little bit different and you get some kind of different
*  results. And so you have to factor all those different variables into how you're building this.
*  There's something even that can run on devices likely good enough for 99% of these use cases.
*  Make sure you build a way to benchmark things and make sure that you really decide if you need to
*  go fine tuning or some kind of RAG or just use a larger context window or pare it down and
*  compress it in different ways. And you can have the same document take 10 times less space
*  by just asking you to compress it, define the language, and then include a definition with
*  every document, for example. And even like a Claude that has a 200k window, we've gotten
*  three million token equivalent documents running at the same speed. And there's papers on this.
*  There's ways of doing this now with much smaller models doing the same thing. I think those are
*  just some of the things that we've learned. We want to include this in our community portal.
*  What are the kinds of things that we found useful? What are some of the libraries that we've developed
*  that we'll share? We'll open source as well. But we're just super focused on can we get something
*  useful out there for users? This project is three, four, five months old at this point and
*  close to 50,000 users. And so it's grown tremendously. And then we've been super
*  heads down on just building more of the features that customers want. And now it's more about how
*  do we evangelize? How do we build that community and make it as repeatable for them as it has been
*  for us who do live this every day, who love to geek out with the latest research papers and try
*  12 different models and everything else. You shouldn't have to do that to build a useful agent.
*  You shouldn't have to do that to personalize. You shouldn't need to drag and drop even 30 different
*  steps to build an agent. You should just talk to the system or the Sribet and text message format,
*  and then you just get what you need and customize from a massive library. And we believe is the
*  power of this marketplace that we're building, where we're just going to connect the builders,
*  give them the distribution with people with real use cases that they're trying to solve for
*  and make that as easy for them as just describing what they want and you're using it. You don't
*  have to do it in the car research. One of my mantras for AI enablement generally is copy and
*  customize. And I think that is the experience that is by far the most accessible for people that are
*  not living and breathing AI all the time. I sometimes say clone and customize, although
*  copy and customize rolls off my tongue a little bit better. But when I saw the clone button on the
*  agents that you have there, I was like, okay, this is definitely philosophically similar to what I
*  think is going to really serve people. Let me just highlight a couple of points that you mentioned
*  along the performance maximization answer there. One that you mentioned was on rag,
*  you need semantics basically, right? If I were to translate your comments to my own language,
*  I would say you can't really take whatever proprietary data format you have and embed that
*  unless you're going to do your own embedding model. Now you've got another, it's like a regular
*  expression joke. You had one problem, now you have two problems. So most people don't want to have to
*  get into the trouble and probably don't have enough data to do their own embedding model. Maybe you
*  could fine tune it, but whatever, especially when you've got these sort of not super semantic
*  proprietary data structures, that is tough. So what I heard you say is what you want to be
*  searching on is a very semantic representation of that. So I imagine the rag component being like
*  maybe a paragraph description of what this agent is and does. That paragraph is what gets embedded.
*  You compare the user's request to a thousand of those paragraphs, not a thousand structured data
*  things that sort of specify all the tools and the API calls. But those paragraphs then point to those
*  things and then you can call in the right ones. For example, do I have that right? Any other nuances
*  there? That's it. And really we describe down to the field, down to some of the prerequisites
*  as well. So if you're going to have this, let's say we're going to get YouTube video transcripts
*  based on the URL. Let's make sure we have a YouTube URL to feed it. Or what else can we do?
*  You could also do something like search the web and you can use Google search capabilities. You
*  can use the channel lookup capabilities. So I guess more complicated because we do map out
*  some of those dependencies or optional dependencies or different ways of getting there.
*  So there's really, I look at it as almost data pre-processing. When you think about proprietary
*  formats, that's sort of the data scientist way in me is thinking about, okay, how do we pre-process
*  and index and retrieve it efficiently? You need to think through all those different nodes in a tree
*  and how you get there and different potential pathways. Very similar. And I think again,
*  you can start very simple, but pretty quickly you need a way to manage those dependencies in
*  a structured data format. The embedding part, like you mentioned, is critical. If you're going to have
*  domain specific vocab, then you're going to train it on that. You may need custom embedding model,
*  et cetera. That can complicate it quickly. Try to stay generic. But yes, that'll get better results.
*  Is it really worth the technical complexity for 2% better lift? Is that worthwhile? Then what is
*  your indexing system? Is it your likely elastic search or a face or something with custom indexing
*  for your proprietary data? That will likely be highly scalable, good enough for 99.9% of use cases.
*  We use Pinecone for that. Different ways of searching and indexing data with additional
*  metadata that you may actually need to provide it in the entire relevant context. And then the
*  last bit is also the query optimization. If you've got your proprietary jargon, you may need to
*  optimize accordingly. I don't think you need all these four ingredients. They're parts of
*  what we've defined to be able to get to a better state than
*  feeding as much context, feeding all of it if you can in the tailored prompt. And I think for most
*  use cases, that's likely good enough. Once the data footprint is just too large,
*  it just doesn't work. And then you have to invest in each of these pieces that you need to tie it
*  together. Yeah. And increasingly, we're spoiled for options, not necessarily spoiled in that they all
*  work super well. But I do think hybrid search is the way it seems to me. If not, maybe,
*  depending on the scenario, some sort of graph database. But at a minimum, you want to have
*  the vector component work with a sort of general SQL where clause style capability,
*  where you can be like, there are certain things that I know. And I want to narrow my search to
*  a certain segment of the overall data set. And having the hybrid search there is just
*  so fundamental. It's been funny to see how many things have been built on just like a pure rag
*  approach, pure vector. And it's that you do need a little bit of that complementary structured
*  approach as well. I was also thinking about another piece that we experimented with, and it
*  wind up not working out our use cases, but it might work out in other sort of custom proprietary
*  data sets where you could have custom similarity metrics. Just think about the evaluation and
*  adjusting retrieval metrics in a ragged system, your typical default cosine similarity
*  approach versus something keyword based versus some other semantic similarity based on your
*  own dictionary and your own kind of structures of, hey, this data maps out to this kind of
*  graph of nodes and topics that work together. Therefore, those examples of agents that wound up
*  actually not working for what we needed versus just creating larger documents that get embedded
*  given the nature of our data, given that they very cleanly translate to embeddings. That worked out
*  better with just having better descriptions of each of the steps and then what the agent would
*  be able to accomplish. So that'd be able to pick the right subset of steps with a node view of the
*  dependencies of those actions. But in many cases, especially when you have, let's say you're doing
*  medical research or you're trying to come up with some of some new drug and combine chemicals in a
*  very specific way, some of the language models that have recently come out in that space use some of
*  these custom similarity metrics against very large data sets of drugs that have been published and
*  so on where that is the right way to do it. And that will get very accurate results very cheaply.
*  So you got something extremely custom, right? Like a math or science type of language with those
*  dependencies, translating that to a kind of text nodes or topic nodes is cheaper and easier to do
*  than doing the nodes that then don't really give you the right kind of answer. Super fascinating.
*  You can go down these rabbit holes for each of the knobs and just deciding where and to say,
*  okay, that's not, that's likely not it. Or like this other solution that yes, we may lose 0.2%
*  efficiency in certain circumstances, but for the average case, it's actually no better. And we're
*  introducing a lot of complexity. Let's walk it back and try to get the simplest possible solution
*  as we generate more data. Let's say we get to a hundred thousand users or a million users,
*  we've got a billion agents on the platform and have 10 million agent runs on a daily basis with
*  highly complex data structures and documents as mapping to a personalization. Maybe that's when
*  some of this custom similarity metric definition and algorithms like definitely will come in handy.
*  But for what we're doing today and for the foreseeable future, we modeled that out and
*  we don't believe that to really be worth the complexity. But there could be specific
*  scientific domains where that's actually the only right answer. Like the only way to get to
*  desired accuracy is to go deep in each of these kinds of retrieval and evaluation metrics.
*  This is like a very rough rule of thumb. If you can represent your proprietary data structure,
*  or maybe it doesn't necessarily have to be proprietary, but for many of our app builders
*  in the audience, it would be proprietary to their app. If you can map that onto natural language
*  intent in a way that you feel is quite representative, then you're probably better off doing that
*  mapping and then doing your similarity search in natural language space. If you can't map it,
*  this would be the case with proteins, right? I don't think we have a great way in natural
*  language of talking about how proteins bind with each other shape-wise. There, you're operating in
*  a pretty different space. It's not cleanly mappable on a natural language. So you've got to probably
*  work in that space and that's a whole other world and you do need a lot of data for it.
*  One other big thing that caught my ear was when you talked about using small models locally and
*  working your way up to large models. I'll give you a piece of advice I give and then I want to
*  hear your kind of compare and contrast, but I always say to people who are trying to
*  build some automation, whether it's an automation for their business or the core thing in their app,
*  in Mark's case, it's make a video. We want that video to be really good. I typically tell people,
*  don't worry about cost at the beginning. Go with the absolute top model. Start there,
*  work your way down. First, get it to work. Then think about efficiency, performance. You can
*  usually find some gains, but first thing is just can you get it to work with any available
*  technology and then scale back? So tell me what you think of that advice and then how would you
*  give me a little more color on how you're using the small models locally and working up because
*  I've never actually done that. Yeah, so I agree with your comment. I think first start with the
*  frontier models, try to get it working within that kind of context. If you can't get good answers
*  out of GPT-4 or CLAWD or Gemini, you probably have the wrong prompt. You probably don't have
*  the right kind of data that you're bringing into the context window, et cetera, before trying to
*  do any optimization. I think going and hosting your own models or using something else is only
*  worthwhile if maybe you're living in a regulated space, but even then you can get enterprise
*  agreements for Chad GPT. Hospitals use it. Sending, I know here in Boston, one of my
*  MBA classmates working for a hospital and they're using Chad GPT to understand things that they
*  might have missed in a diagnosis. GPT on the cloud, obviously there's a way to secure it and then you
*  get all these agreements and you're never training on that kind of data, et cetera, but it works in
*  those kinds of contexts. Think very hard before you try to use a custom model where you really
*  believe that you need to have something very specific versus just use something out of the box.
*  Now cost does become a factor, especially let's say through using a lot of tokens consistently,
*  although these models, again, just like AWS is getting cheaper every year. And so I think even
*  Chad GPT has gotten 10 times cheaper and it's going to get 10 times cheaper and so on and so
*  as a concrete example, I'm using a sort of a local embedding model to quite literally index
*  all of my personal data, all my documents, all my images, automatically categorize it. I don't want
*  all of that to go over the wire. For example, if you got financial records and taxes and all sorts
*  of stuff, right? Even I screw things up sometimes and I'd rather some of that not get leaked. But
*  what's really interesting with some of these small models is you can actually get answers much, much
*  faster in terms of some of the fine tuning, some of the those different ways of now even patching
*  some of these live running models. And you can't really do that in the cloud like you need, where
*  you don't have access to GPT, poor weights and data, but some of these models you do. And so what if
*  you want to shrink these models down seven billion parameters to one billion or half a billion or a
*  hundred million and run it on a device they can take with you? That is the kind of experimentation
*  that I've done that I found useful to then be able to run these models locally and also do some
*  of the fine tuning much faster. GPT-4, fairly recently, I think it was maybe a month ago,
*  when they announced the ability to fine tune GPT-4. Before that, you could only fine tune 3.5,
*  for example. And some of the document definition that we needed to tweak, I was able to do locally
*  very fast and then use that comparatively to 3.5, I got better results with a local fine model
*  for use cases. And obviously GPT-4 fine tuning in the cloud, then beat that out of the water,
*  hands up. As different kinds of models will allow for fine tuning online as well, for example,
*  for Claude, we can't do that yet. There's some of these gaps where the local models can be very
*  useful as well if you want to fine tune for highly specialized use cases, maybe financial services,
*  where you don't want certain kind of client data or algorithms to get out there. And you just want
*  to build your own language model in that scenario that is just an off the shelf language model,
*  but you're fine tuning it in certain ways. I think those are the real use cases. I think that would
*  even be necessary in any way. But for 99.9% of cases, there are enterprise agreements.
*  You can ensure that your data never gets used in terms of getting trained on. They figure this out
*  and it'll continue to evolve. I think we'll get more and more of these controls and we'll probably
*  be sitting here a year from now and they're charging by the 100 million sort of tokens at the same
*  price. And the context window is in 128k if it's maybe 2 million or 5 million tokens.
*  In that kind of scenario, I think it's going to be increasingly hard to justify running your own
*  models. But I also think it's very important that we have a very vibrant open source model community
*  because this is only pushing the closed source model providers to move faster to provide more
*  of these tools. And frankly, I think to keep some of the larger players honest, because I do think
*  in many cases, you may not need to pay for a chat GPT. Yes, that's for specialists, that's for engineers,
*  for people who want to set that up and know how to do it and so on. But for my use cases on a daily
*  basis, I get as good results from running locally versus GPT-4. And it's even better in some of the
*  benchmarks in terms of planning. You get like a 50 something score, still abysmally low versus 30,
*  or 20 for Gemini. And so I think for certain specialized use cases, you can also fine tune it
*  to get much better benchmarks because there are smaller models that have less data that can get
*  in the way of what you really want it to do and really fine tune it where those lower level
*  embeddings and the neural nets don't actually come through and override your data for the most
*  part anyways. So again, that's one of the benefits of running some of these smaller models where
*  chat GPT won't even tell you what the parameter count is or that's not a thing. It gives you more
*  control in certain use cases. But again, I think for 99% of people, that's not necessary. It's not
*  going to create any value. And it's a fairly complex resource intensive kind of approach.
*  With machines now even faster and Apple's approach now with Apple intelligence, great name,
*  by the way, AI, and iOS 18 and some of these more powerful devices, you're likely going to be running
*  local small models like this on the edge and keep all your data private. There is no cloud.
*  You don't need a cloud. It just runs on the device. And increasingly, I think we're going to have this
*  with a blend of what Apple is now pioneered, which is your private AI cloud. So you can offload
*  your workload in a way that stays completely private to you. Not even Apple can see what
*  that looks like, even if they wanted to. So isomorphic encryption down at the
*  embedding level so that, yes, it's embeddings, but no, it's not embeddings that you can map to anything.
*  It's just the simplistic way to look at it is offsetting by some kind of encryption key.
*  Ultimately, even if anyone were to intercept all that traffic, they can't do anything with it.
*  And then you can trust it to say, now give me unlimited cloud resources, unlimited number of
*  models that just take a look at this data and give me better answers faster, which again, I think is
*  a super fascinating kind of hybrid approach to take to privacy, to scaling the workloads,
*  in a way that preserves the private aspects and the sensitive aspects of this data that we're
*  feeding these models. And what does that mean for training them? What does that mean for the next
*  iterations of these models? I think it's very interesting. And I think all of these approaches,
*  the ChadGBT, CLAW, Gemini approach, the open source approaches, the Apple's approach here,
*  they're all helping us evolve this phase very quickly. One more little follow up on the
*  fine tuning. Are you fine tuning on chain of thought? And do you have any tips around
*  the sort of data to fine tune on? Personally, I have found huge value in fine tuning on the
*  chain of thought that demonstrates exactly how I want the system to reason about whatever the
*  problem at hand is. So just wonder what you've seen in that respect.
*  I guess there's two different approaches here. Chain of thought versus chain of retrieval in
*  multi-step tasks. I think it's earlier in terms of progress and chain of retrieval algorithms,
*  but they're fine tuning. You're enhancing the reasoning capabilities and its ability to handle
*  problems where you need someone that's sequential and step by step reasoning by preparing a lot of
*  data. I think you need to collect a lot of training data. That's not only like the outputs,
*  but the very detailed intermediate reasoning steps. It's almost you've got an intern and you
*  have to explain every step and make sure your data is highly curated. If you can do that,
*  then chain of thought is really great. Then you have the supervised fine tuning where you annotate
*  all that data. That may mean we have to augment it in different ways. We haven't thought about
*  these dependencies that we need to bring in. And again, the last piece that I found useful is
*  being very explicit with what kind of prompt you're using. And I've literally just written
*  prompts like, can you just break this down into steps to solve the problem? And then
*  evolutions of that to then refine the chain of thought examples. And again, math, legal reasoning,
*  et cetera, chain of thought is very good in terms of improving that accuracy and it's all measurable.
*  And then for chain of tuning for those inference chains, that's actually super interesting because
*  you're tying it to RAC systems. You have to be retrieving, processing, integrating data from
*  multiple sources, but then you're dealing with the ensuing complexity of dealing with multiple
*  kinds of steps for retrieval, multiple kinds of steps for processing and resolving some of those.
*  But that's why I think it's harder to get right. You need a lot more infrastructure. There's
*  pipeline fine tuning and task specific fine tuning that you could do depending on the kind of tasks.
*  Like if it's Q&A versus synthesis, it gets very complicated quickly. And I haven't been able to
*  get nearly as good results with the second approach compared to just chain of thought.
*  I think just a few good examples, a few synthetic data generation approaches as well to this can go
*  a very long way. It's a little bit meta, but even asking like, how can I break this down further?
*  And what are some of the key potential decision plans that we haven't talked about? I found
*  many times like in some of our agent examples to be highly illuminating and even gave us
*  thoughts on like, oh yeah, we should break this out into two different tasks.
*  Because we're implicitly connecting concepts that like should just be split and actually we can
*  increase accuracy given certain kinds of intent by mapping each one of them to concrete kind of
*  chains of thought, right? Like dependencies up and down the chain, which again, I think it's a super
*  fascinating thought exercise as well, because then you can map it out and get a really good
*  understanding of what are your biases and the biases in that data that needs to be cleaned up
*  so that you can get better answers faster. I think it's as much having better data as just asking the
*  right kinds of questions and providing the right kinds of constraints onto the system in the first
*  place. Yeah, I say 10 gold standard examples. And obviously the exact number varies, but it
*  is surprisingly small. Most people assume that you need a lot more data than you actually need
*  to get started. One thing we've noticed at Waymark, which is really interesting is we want the AI to
*  be better than our customers were in the absence of AI. So we initially started by just pulling all
*  these videos that had been created in the system out and using that as fine tuning data. But then
*  as we're looking at them, we're like, actually we aspire for the AI to be better than this.
*  So rather than working from real data, we were like, okay, we need our creative team,
*  who's the best at this, to sit there and grind them out for a little while. We started with
*  thinking we needed 10,000. We quickly realized that was not necessary. Then we were like,
*  maybe we need a thousand. Then we're a hundred seems to be working pretty well actually.
*  And now what I mostly recommend to people is get to 10 and then you'll use that. Not that you'll
*  necessarily be done then, but that'll be enough of a seed data set that you can start to backfill
*  the things that don't actually exist. The chain of thought is generally not captured.
*  This is something that is missing. The internet does not have the chain of thought that typically
*  it's not even verbalized. It's typically totally implicit, maybe even sub vocal in the human's
*  brains, but it's definitely not spoken out loud or recorded down and it's not published on the
*  internet. So we see these shadows of it. We see the inputs and outputs, but what was actually
*  happening in the brain is missing. And have you seen any good tools for capturing that?
*  One thing that I think is a very large opportunity would be a sort of harness, if you will,
*  that a person could load up, strap in and be like, all right, I'm going to go do my work,
*  but this thing is going to be responsible for coaxing out of me why I'm doing what I'm doing.
*  How am I thinking about it? And then integrating that with the actual discrete actions and clicks
*  and keystrokes and outputs that I had so that we can create this unified data set of inputs and
*  the process, even to record it and then finally outputs. Have you seen anything like that? Because
*  I have not, and I have been looking for it. I haven't seen specific tools. There's a few
*  libraries that can help you on GitHub. I mean, Frank has some really good resources on that.
*  Just in terms of, there's a bunch of libraries I can share some of those links that are good at
*  monetizing some of those documents and using concrete patterns to then define this data.
*  But at the end of the day, they're essentially just data engineering, data pre-processing kinds
*  of tools. And that's basically it. It depends on the kind of data that you have and how you're
*  defining what the chain of thought should even look like, given the context,
*  which is probably why you don't have concrete platforms that can do that for you, because it's
*  so domain specific. This may be example specific, but that's a really good point. You should be able
*  to define and structure them and automatically load more examples based on annotations on maybe
*  some kind of agent runs and then say, okay, so what was it thinking there? What were the steps?
*  And then validate it and then annotate that to maybe do some actual fine tuning with.
*  As far as the closest, there are platforms that will allow you to load up a lot of data,
*  describe how you want it to be categorized and the kind of entities that you like to be extracted
*  from it and then maps it to documents. And then from there, you can use some prompts to approximate
*  some chain of thought to then turn that into fine tuning and like, as I'm sure just labeling
*  the data after processing and then human in the loop labeling it. That's a good point.
*  That feels like a big opportunity to me. Going back to the question of, I think of it as deep
*  context, but it ties a couple of different themes together that we've talked about.
*  One is the customization of agents to a user. That customization has multiple dimensions.
*  We've talked about modifying the workflow because you're using a different system or whatever.
*  Oh, I'm using this task manager instead of that task manager, but I like the rest of this. We
*  need to make that kind of change. Okay, that's fine. That's fairly not necessarily easy to get
*  an AI to do that on the user's behalf, but is at least conceptually something that the platform
*  can be responsible for. Then on this privacy question, I think another huge problem with
*  realizing the AI dream right now is we underestimate how idiosyncratic we all are, or maybe a nicer way
*  to say that is how contextual all of our work is. It's not necessarily that the AI can't do it,
*  but that we're getting generic stuff in many cases because we're not giving it enough to work with.
*  And so this is something that I think is very much an unsolved problem across the board in the space.
*  I'm currently working on a project to try to fine tune whatever model I can get to work to
*  write as me. And I'm realizing in doing that, that to write as me, you need to have a lot of context.
*  The strategy right now involves fine tuning, yes, but as far as I can read the research,
*  at least with the sort of low rank Laura style fine tuning that is available via OpenAI,
*  the fine tuning process doesn't seem to work well for learning facts.
*  So I've tried to fine tune it to answer, what is your name? My name is Nathan LeBent. It can pick
*  up my style reasonably well, but it doesn't learn the facts. So I feel like, okay, well,
*  to get this thing to write as me, I'm going to need it to learn to imitate my style. Fine
*  tuning seems to be able to do that, but I also need to give it just a ton of facts to be able to
*  have something to draw on to at least have any hope of effectively writing as me in any given
*  situation. And so that sends me down this rabbit hole of, okay, where does that data live? It lives
*  in Gmail, it lives in Slack. In my case, I have a podcast, so I have a lot of things that I've said
*  that are good context there. Some of these data sources are really sensitive. And I'm not a
*  privacy oriented person. People that know me know that I really don't care that much. But when it
*  gets to the level of every email I've sent for the last five years, which is the data that I'm
*  trying to manipulate here and every Slack message that I've sent for the last five years,
*  too, that is not the kind of thing that I just want to put over on one random startup that I
*  just found that may or may not work for this. I am willing to trust the open AIs, the Anthropics,
*  the Googles of the world, but I'm not willing to put all that data into random new startups.
*  But it is really important, right? If I want to get my AI agents to work well,
*  they need to know quite a bit about me, I think, in many cases. I'm in the process of working on
*  this. I'm working on prompts to go through literally tens of millions of tokens of my
*  past data and try to put that into 1% compression to give the language model enough context.
*  How should we be thinking about that? Is that something that users are just going to have to
*  continue to do themselves for a while? Or is there any way that you can start to help? Is there maybe
*  a context builder agent that I... Maybe that's what I need to do is I need to go on Agent AI,
*  build the context builder agent, you'll review it and verify that I'm not siphoning off people's
*  data. And then folks can have a connect my Gmail and spit out context. Is that the vision? Is that
*  what we're working toward? Or what else do we have? That's exactly the vision that we're working
*  towards. Privacy is paramount, which is why we haven't released anything yet. We are working on
*  a Google integration. So let's say you do want to connect Google Calendar, Google Drive, and
*  eventually Gmail. It's going to be able to maybe chat with your emails and chat with your calendar
*  and connect the dots. Given our parent company and mothership HubSpot, we think in relation to
*  customer contact, relationship management, that at the end of the day, it's all about relationships.
*  What useful information can we extract? Besides the fact that it's all sensitive information,
*  it's all important. We will do everything that we need to keep that secure, assuming that's
*  already done. Assuming that you trust Agent AI as much as you trust OpenAI. OpenAI today, you can
*  upload all of your data and they have essentially a RAC store, a vector store. You can upload a whole
*  bunch of documents and there's probably some limits, but probably a decent amount where you
*  can now use the RAC store, maybe multiple RAC stores, to then build your own assistant that is
*  then tied to those data stores. And then you can chat with your emails, you can chat with your
*  calendars, etc. The part that's missing obviously is doing that real time. Something should just
*  take care of it. Just always index it, add all the metadata, make sure that maybe we need to expire
*  certain data. Maybe we do need to fine tune it. Given your use case, if you have a lot of
*  pharma data of some kind, they need some additional algorithms to even retrieve the
*  right kind of data to the RAC. That gets complicated quick. For most Y-collar type of work,
*  it's fairly straightforward. We need to recommend some kind of document size and overlap, maybe a
*  few other settings on how we retrieve documents and how many of those documents we should retrieve
*  at a time given the prompt. And there's different methods of doing that. But that's all that's really
*  needed plus some data connectors. So you can now say, okay, let's get this data and up every minute.
*  You get every email, every calendar, and then you can do something useful with that information.
*  I think there are some approaches, none of them that I've seen so far are fully commercially
*  sort of enterprise grade yet in terms of applying asepomorphic encryption to
*  vector stores. So that's the kind of encryption where you can encrypt it,
*  you can encrypt, let's say the vectors, just the vectors themselves or some approximation.
*  And then we query that data and we can then decrypt it with the private key of the user.
*  And then you're the only one who has a key, you use your private key to get the actual results
*  and decrypt them to then give that to the agent to then handle it. We haven't cracked that yet.
*  I think that's fairly complicated. Obviously, no one has done it yet for that reason, but the
*  pieces are there. I also think the other solution to this is some kind of proxy answer where maybe
*  an agent AI or there's other platforms for sure where you can specify the model URL. Just say you
*  can specify open AI key if you want and use your account directly. Similarly, you can say, okay,
*  I'll provide my model URL. I'll provide my open AI compatible hosted model that might just be on
*  your local machine or on your own private data center or something that you trust.
*  All that data just gets sent through, proxied over, sending for embeddings if you want to
*  embed millions of documents and financial records, use something local. You don't have to use
*  something in the cloud. And then all that data just gets proxied, more control over exactly how
*  that behaves, what kind of model you're using behind the scenes. And I think the future is
*  some blend of those things, especially for the power user use cases. I think some of that kind
*  of proxying is necessary or using your own AWS bedrock model library. There's different ways of
*  hosting models now that is fairly straightforward at scale. But again, the encrypted data address
*  in a way where you could share all of your private data with us, we have no control or any other
*  platform has no way of reading it except when you authorize it for those specific use cases
*  to just show you the results. But to compute, it doesn't need to know what it looks like. It
*  doesn't need to know what the data is because again, they are just vectors, just math, and it
*  just can give you answers based off of that. Then you bring it all back together. Apple, I think,
*  is doing some things there, reading from their patent disclosures and some of the research papers
*  that they've put out. They're doing this type of isomorphic encryption to be able to keep all your
*  data in your encrypted enclave on your iPhone, send chunks of that data. Maybe it's your email
*  contacts, maybe it's your calendar contacts, and only a very small sliver of that data encrypted
*  in flight and as isomorphically at that to then just give the answers back and then you're the
*  only one who can see it. That's the kind of privacy sort of forward solution we need. We're
*  not there yet. I would trust some of these systems like OpenAI, I think I already do,
*  with all my data. I've done exactly what you just talked about with all of my emails and all my
*  years of data. I did it locally, I did it in the cloud. There are ways of protecting yourself and
*  making sure that your data is kept private. But I think that the biggest takeaway there is make
*  sure you're paying for the products. If you're not paying for them, you are the product. If you're
*  not paying the 20, 30, 100 dollars for the API sort of access, which comes by default with all
*  the privacy guarantees. If you're using new startup free product, they're going to monetize
*  what you give them. Your data may wind up in all sorts of places. I think there's some good
*  out of the box ways of doing that today that doesn't require all of these additional
*  advances that I believe will just be industry standard in six months to a year. I think we're
*  going to have every vector store have that kind of key based approach. Yeah, I need to study that
*  more. I love that you're getting into the Apple patents to start to triangulate on that because
*  I think that is a huge gap right now and a huge opportunity. I mean, just to trace the thought
*  pattern again, it's like the models need a lot of context. They need more than a couple paragraphs.
*  They really, in many cases, need a lot of context if you're going to get them to do work that you're
*  going to be happy with. They need more than just a couple of bits of instruction. But how do we move
*  that data around in a way that is secure? In general, if you're just doing normal embedding,
*  it is easy to reverse that. And so it's not secure. Even though you may not be able to read the
*  embeddings as a human, it is pretty easy for somebody if they were to come into the possession
*  of your embeddings to reverse that and get, if not exactly the original, very close, right?
*  Preserve the ability to do semantic work on top of an embedding, but to make it not reversible.
*  That does seem like a huge piece that can make so much more stuff possible without major downside
*  risks. So I'm quite excited about that. Great. Then let's talk about the business aspect of
*  Agent AI for a minute. You had said, obviously, make sure you're paying for products or you are
*  the product. You guys are in an in-between phase right now where the product is free for everyone
*  to use, at least up to a point. And you have the backing, as you mentioned, of HubSpot, which allows
*  you to do that without going personally bankrupt as some individual app builders have confronted
*  when things go viral. What is the plan? Maybe you don't know yet, but how do you anticipate
*  monetizing this? Right now, it's kind of a simple, you use an agent, it's one credit.
*  Obviously, not all agents are created equal, especially if I start to bring in tens of
*  thousands of tokens of context. That's not going to be all equal. I can imagine you could be like
*  super high margin on some one credit uses and negative on others. What does this look like?
*  Is it usage based? Do you make a margin on usage? I expect we're probably going to see
*  sign in with OpenAI, sign in with Anthropic maybe coming at some point where people will be able
*  to bring their own access to the models, to other products. That doesn't exist yet. Well, it does
*  in the form of I could bring my API key. So I can imagine you could have people bring their own API
*  keys to the degree that there are fine tuned models in those clouds, individuals may want to
*  own them as well. What do you think the outlook on the economics and pricing packaging of this over
*  time? So obviously, right now, everything is free. We have this concept of credits. Essentially,
*  if you use all your credits, you just get more and there's more ways of getting more. We'll
*  introduce at some point this year, likely some way of buying more tokens when we also introduced
*  the builder side incentives. I think that's when it really matters for us. In the meantime,
*  our goal is really to just get adoption to figure out what actually works for people. We'll likely
*  be able to sustain hundreds of thousands or millions of users at essentially full unlimited
*  kind of usage for some time. That's one of the benefits of having Dharmesh Shah as the man behind
*  the scenes, driving the vision forward and helping us democratize this more broadly,
*  because that is expensive. If you're trying to do this yourself and get even 10,000 users,
*  some of those costs add up pretty quickly. I think we're going to see a lot of consolidation
*  in the AI tools and agents and marketplaces kind of space because, frankly, most haven't figured out
*  a business model. Like most, you're getting traction, you're getting more users. There's
*  certain use cases that we're going to really focus on and build a number of agents again for the
*  use cases that we know and understand very well, like marketing and sales and customer service
*  that are very much sort of HubSpot user persona adjacent, if not centric. And we'll expand from
*  that. I think the part that we really want to get right is how do we incentivize builders?
*  Is it by acquisitions? I think that's part of the equation. Should we go and actually hire
*  five, 10, 20 of these companies? We likely will. I think that's part of what we need to do
*  if we want to make agent.ai, the marketplace, the platform for developing agents, for getting
*  distribution, for being like the app store. I think that is to just help seed this marketplace,
*  to get more of the right builders on there, to get more of the right agents, give them some kind
*  of guarantees in terms of a likelihood, why that's a flat fee, that we'll pay them plus some kind of
*  usage. There's a few models here that we're thinking through right now. What does that pay
*  package need to look like for people that are finding these agents useful? Is it like kind of
*  the 99 cent approach? Happy to pay a dollar a month for something that I find useful? Is that
*  $5 a month? Is that $20 like a Chad GPT level price if you get essentially unlimited Chad GPT
*  usage through the platform with your own data, with a bunch of other agents? Is that a decent
*  price point or something between 99 cents and that kind of average price?
*  And then I think that there needs to be some type of rev share for each of these credits that
*  user uses to both give to the builder and also give the builders the tools to then charge for
*  a higher tier of an agent. So again, I think there's this concept that we're playing with right now
*  that will have some agents as a closed kind of beta phase where you can have a free version
*  of an agent. You can have a pro version of an agent that will just do a lot more. That will connect
*  maybe more data sources that are going to cost more money. Do you need this version of an agent
*  or do you need this other one? I think it's early. I think we haven't quite figured it out. I think
*  for the foreseeable future, everything is free. But yes, I think if we want to first make sure
*  we take care of the builders, give them real incentives to build agents, to bring their
*  agents frankly to agent.ai to make sure that this is the marketplace for all these agents,
*  that is our goal. And then make it super easy for anyone who needs to customize their agents,
*  make it super easy to do that, create again the right incentives for builders to open some of
*  their models, to get the right kind of ratings, maybe get a higher cut essentially of the marketplace
*  sort of transactions and then so on, all the way to some premium support and so on.
*  So I think that the future needs to look something like that to have a viable market,
*  but also a viable business. Where again, at the end of the day, we're looking to build this into
*  a business. Again, we have one of the benefits of not needing to fundraise. We're just really
*  focused on building the right product and doing what's right for customers. But I think we also
*  need to figure out what does that need to look like for these builders to have a healthy marketplace
*  that can actually sustain itself. Yeah, cool. All right. I love the ambition. It definitely sounds
*  like a good spot to be able to give it all away for while you figure it out. I don't expect it to
*  be free forever, but to take advantage while it lasts. I think kind of changing gears, just zooming
*  out a little bit from the product, I've got a few big picture questions. How are you taking advantage
*  of all the AI tools in building this platform? I have just joined the cursor revolution in the
*  last two weeks. I actually downloaded it six months ago. Wasn't blown away then. If you were
*  like me in that early cohort, definitely come back, I would say. I've been super impressed now
*  with where it is. And I can't believe I ever actually typed code. What a primitive life form
*  I was. What is your tech stack from the development side look like? Yeah, I love cursor as well. I
*  probably have five of these tools like cursor and your co-pilots for some custom things that I built
*  as well. Yes, I fully embrace the AI tools for writing code as well. Our tech stack is fairly
*  standard. Python, backend, frontend is all Max.js, React, TypeScript with everything on AWS,
*  everything auto scalable database wise, relational database, Postgres, behind the scenes.
*  And that's basically some queue management and those kinds of things. A very simple sort of
*  stack, very standard. Frankly, we love the simplicity of what Python can do. I wish we could just,
*  you could do full stack development on Python versus you can do it on JavaScript, but you can't
*  quite do that on Python. Technically, that's not true. There are some libraries now where you can
*  build some of the front end using Python, but yeah, it's just those two languages and we're moving
*  super fast or shipping dozens of times a day, which is awesome. We have a small team today. I think
*  it's overall, we're just a team of about 12 or 13 people at this point. Three, four months ago, it was
*  just me and our mesh and another freelancer doing front end work, mostly on the backend side and
*  some algorithms, DevOps, et cetera. And we're continuing to grow. I think we're always looking
*  for anyone who's actually interested in working on something like this. We're only going to grow.
*  And yeah, we just love working on this kind of cutting edge side of what is the Gentic AI even
*  look what it was six months ago versus what it's going to be six months from now.
*  I think it's more useful every day. It's more concrete and it's more applicable to end users.
*  One fine point follow up there. When you use the Amazon scalable Postgres, does that have like
*  PG vector and do you have a sense for is PG vector all you need, so to speak? Because I've been very
*  confused as to should I be running out to get the latest and greatest vector database or should I
*  trust that the embedding model is actually where it's at and Postgres will probably figure it out.
*  Do you have a point of view on that? Yeah. Yeah. I mean, we've tried all the approaches. I think now
*  performance of the Postgres vector store is as good in some cases and some benchmarks even better
*  than something like Quadrant or Pinecone. We use Pinecone ourselves. We just love the simplicity
*  of it and it scales very nicely. I think that the debugging tools and searching tools are superior,
*  frankly, to some of the things that you can get out of the box with Postgres like anything else.
*  If you're willing to spend and have the engineering bandwidth, then just do it all in Postgres.
*  Keep your life simple. If that may also require some tuning, some optimizing data stores. We
*  reloaded a lot of data and had some cascading performance. This was six or so months ago and
*  I think it's come a long way, but something like commercial product like Pinecone is essentially
*  infinitely scalable and we'd rather just click one button and have to worry about
*  which replica on our Postgres setup is going to have some issues or get pegged CPU-wise because
*  there's a bug in this specific implementation. Therefore, I have to fail over and etc. I would
*  just rather pay another third-party service that is very good at this, that can do everything we
*  needed to. It's cheap enough. I mean probably millions or tens of millions of records and
*  something like Pinecone is dozens of dollars. I'd rather not have the headache for dozens of dollars
*  or even for hundreds of dollars. At the end of the day, some of those specialized tools
*  tend to do better if you can afford it, but on the other hand, you're always going to pay for it in
*  some fashion. So let's say you do get the built-in Postgres version, be prepared to spend some time
*  debugging, optimizing. There's always ways of tweaking and you do need to tweak some of those
*  settings to get optimal results. I've tried it recently. I think it's much faster than Pinecone,
*  but again for the kinds of use cases we're talking about, whether it's 15 milliseconds or 10,
*  does it really matter? That's not where the wait time is. It's in the language model, right? It's
*  in some of those run trips. As an engineering purist, technically, yes, that's an improving
*  solution, but our philosophy at agent.ai is pick the right tool for the job, don't overcomplicate
*  it, ship super fast. Whatever it takes to ship super fast, just do that. Yeah, it's a good
*  endorsement for Pinecone. It's an interesting reason that it's not actually some maybe more
*  fundamental technology difference, but it's really just the polish, if I understand you correctly,
*  it's the polish on the product that it works smoothly. It's not an afterthought. It's not
*  something that they tacked on and you're not going to have problems with it. And that is a
*  pretty appealing proposition for a lot of technologies. Yeah, I think it's like 10 lines of code to
*  instantiate your storage query, insert, upsert, never a phenomenal SDK. There are some libraries
*  for Postgres, but nothing quite as simplistic as that. So when you think about code footprint,
*  maintainability, those kinds of issues, you just feed it the connection string and everything else
*  is less than a dozen lines of code. And I have all the rag tooling that I really need, query data,
*  insert and delete it, create new data stores for new customers and so on. Yeah, cool. Zooming out
*  even further, the future of work is obviously a question that is on a lot of people's minds
*  and a quick perusal through the AI agent network and how the fact that's presented on par with the
*  human network is like two different sections of the site across the header. It definitely suggests
*  that as one of my good friends used to put it, the robots are coming for our jobs.
*  I personally feel like that is true and that we should probably be more real about it sooner in
*  this process. I've actually admired what I've heard from the CEO of Klarna recently, where they put
*  up this thing that said, this is doing the job of 700 people. And we literally have reduced our head
*  count in this customer service area because we created this chat bot. And he's, I know that's
*  hard to hear, but I think I have a duty as a leader in this space to let people know that this is the
*  reality that we're headed toward. I feel like in an ideal world, people should not have to do work
*  that they don't want to do. Or if you're only doing the work for money because you need to eat, like
*  in a better world, not to do that work and you could do other things. This of course doesn't
*  mean that there's not other worthwhile ways to spend time. I'm like an optimist on our ability
*  to find meaning even in the absence of jobs that we only used to do because we had to get paid to
*  buy food. But what do you think? And how do you guys think about your role or your thought
*  leadership in this space? Because obviously it's much bigger than any one product or platform,
*  assuming that we don't hit a plateau like now. Yeah. So look, the way I look at AI agents is that
*  they're highly effective, specialized, semi-autonomous applications. That's it.
*  I don't think they're coming for anyone's jobs. I think if anything, that's they're going to help us
*  do certain parts of certain jobs better, faster, cheaper. I think the human will always be in the
*  loop. I think you're going to need someone to decide, okay, what is good? What is bad?
*  What are the selection criteria? What is the broader context that we should really care about
*  and give that guidance to these AI agents that are going to increasingly become even more useful
*  tools, even more helpful, even more personalized? I think all of that is true. The way we're
*  positioning agent.ai is we believe, and this is purely because these are the concepts that we're
*  using today, but we believe that AI agents are going to be part of your team on a daily basis.
*  Whether that team for you as a solo entrepreneur is just you or just you and a bookkeeper or someone
*  else, you're going to have this other entity that can help you do some of that work, but it's not
*  going to take it away. It can't take it away. It needs a lot of guidance. It needs a lot of
*  inputs. It needs someone to say, this is what I was looking for. This is not what I was looking for.
*  It needs your permission to return data and really make extract meaning out of it and create the
*  right kind of voice for the answers. Yes, I think over time that these tools are only going to get
*  better in terms of approximating what you and I may think, what you and I may say, what you and I
*  need to put together a report. Can you put together a similar looking report or paper
*  or PowerPoint and extract data in a very similar way to then present some analysis to
*  in a kind of meeting? Yes, I think these agents are going to be able to do a lot of that type
*  of work on our behalf. Can it complete the whole thing end to end? Highly unlikely anytime soon,
*  but even in that scenario, again, the way we're framing agent.ai is this professional network of
*  agents because if you think, and we believe this strongly, that AI agents are going to do
*  work on our behalf and increasingly meaningful work, increasingly complex work and different
*  kinds of tasks, and you'll even have teams or crews of AI agents all kind of swarming together
*  to try to figure out how do I solve this specific problem and they each get a little piece of the
*  problem and eventually it all comes together and you say, you know, good AI agent and bad AI agent
*  and get some feedback and eventually get something useful out of it. And over time it gets better.
*  You're going to want to understand just like you do with people today on LinkedIn and other
*  social platforms, you want to understand what these agents are capable of, which ones are the
*  best ones at doing some very specific things consistently, repeatedly with reviews, with
*  endorsements, with the level of like education kind of equivalent, right? How much training they have,
*  what kind of models they work really good with, what kind of data is this working in a financial
*  sector or is this more marketing or is this more customer service oriented? That type of social
*  network credibility checks and the professional network aspect of it is I want to understand how
*  good these agents are as specialists, as certain kinds of things. Help me understand if I'm trying
*  to get maybe not, you know, client or level customer service AI enabled reps, but something
*  similar, right? What are the three or five agents and who are the builders, who are the people behind
*  those agents that are building these kinds of agents, right? Who should I reach out to
*  for my use cases, right? How do I start super simple and maybe that's good enough for 80%
*  of the use cases versus how do I go to something even more advanced, right? The kind of agent that
*  is fine tuned on its own model to be able to accomplish just what Kalana did, for example,
*  right? How can I hire that agent? How much would you pay to be able to get that kind of Kalana AI
*  agent within your organization? If I could pay 20 bucks a month and get that, I would probably do
*  it and I'll probably want to understand what that landscape needs to look like and for me to be able
*  to gain some kind of value, to be able to build these agents and make that part of my company's
*  strategy in terms of getting some of this real work done. Again, I think it's all highly additive.
*  Just like with ATMs and bank tellers, the bank tellers now do more things. It's more customer
*  relationship oriented and so on. I actually think we're going to have a lot more jobs that people
*  are going to need to do, not fewer. Yes, we're going to elevate the kind of work that we all do,
*  but I think we're going to bring in a lot of sophistication, a lot more thinking about
*  the data and the context and real conversations about biases in that data. Because all of these
*  AI agents are biased in some fashion, right? How do we understand that? How do we document it?
*  How do we constrain it so that we can get some really useful work done a lot faster and understand
*  maybe AI agents are in the solution for all the tasks? Completely agree. I think these are
*  highly specialized, finely tuned weapons that you can use, but you probably wouldn't want that.
*  Write poetry for you, right? Write a really interesting novel. Again, there are agents
*  that you can use today that can help you do that, but I still think there's a lot of things that
*  people can and will do a lot better. I think human plus agent in most of these cases is going
*  to win over just agent or just human. In fact, I think it's going to make that work itself
*  more enjoyable. I'm going to do less over the mundane. Do you really want to do data entry all
*  day and copy and paste data from one inefficient enterprise system to another so you can get the
*  thing, use your creativity for just 30 minutes of the day versus all five hours, let's say.
*  Maybe that's for a day now instead. I think it's super exciting. I think it's super early.
*  I also think we're going to need to figure out more of the regulatory aspects of this as we think
*  about what does this mean, especially within the US elections on everybody's minds and the election
*  season. What does that mean for AI generated, lookalikes of people and the voices, everything.
*  I think we need some of these guardrails. I think technology is moving much faster than any
*  regulation can move. That's obviously a bit scary. And I think also as builders of these platforms,
*  we need to make sure we're thinking about the safety, the bias, the controls, and maybe in say,
*  you know what, we're not going to support those kinds of use cases, make sure even if that means
*  turning down potential customers, we're going to have stump constraints in terms of what we want
*  these platforms to be able to enable. But I also think we need real answers in terms of the
*  regulations, real guardrails that don't stifle innovation. And it's a tough balancing act.
*  You want to advance, you want creative solutions, but you don't want to just kill the technology
*  in its infancy and lobotomize it essentially and maybe let other places be that cradle of
*  AI advancement very quickly. As well as I think you raise an interesting question. I don't know
*  what the answer is, but it's probably something like UBI. What is that sort of Star Trek?
*  I love that kind of scenario where yes, money doesn't really matter. And we're not doing work
*  for just the pursuit of money and sort of capitalistic gains. And then they have my
*  capitalists at heart. That's a tough pull to swallow. But I do think we need some kind of
*  solution that does take into account that future state where yes, and maybe in some roles,
*  some of this technology is going to more rapidly impact them. And I think we need some real answers
*  from a policy standpoint that can only be done through government intervention versus what
*  private companies can really achieve more from safety and trying to do good for the community
*  and the communities that we work and live. I think we also need some of these broader guard
*  realms as well. So last question on how we get ready for the possibility of a near term,
*  I might call it agent awakening. And my model for this is pretty simple, but it's basically just,
*  obviously we've seen every two ish years, like a major step up in model capability
*  from GPT two in 2019 to GPT three to GPT four in 2023. And we're kind of pretty close to do for one.
*  The interesting aspect of what's happening now is everybody's out there building
*  all of the scaffolding and structure to make these things go and to give them rails to be on
*  and to try to compensate for their weaknesses. People are chipping away at it. And I sort of
*  expect that from one day to the next and potentially quite soon, there is going to be a new better
*  model available that suddenly might in combination with all this stuff that's being built right now,
*  tip us over from one equilibrium to another or across a threshold where today, highly autonomous
*  things don't quite work everything we've talked about. Maybe that changes pretty fast where it's
*  actually now semi to moderately autonomous things do work. And now we're in a world where
*  the AISDR is not like only able to respond to inbounds, but can actually go out and do
*  research and build pipeline for me. And everything turns up at once. So I guess my question is,
*  do you have any, first of all, does that seem like a realistic vision? And if it does, and then that
*  could all happen quite quickly. Is there anything that we can do in a very practical tactical way to
*  be ready for that as a society? One kind of half-baked idea I previously proposed was speed
*  limits for AI agents. Obviously, one of the things that AI's are clearly already superhuman on is
*  they're faster than we are. Maybe there could be a speed limit for AI agents to try to make them move
*  more like human speed. I don't know what that should be. I don't know that anyone knows what
*  it should be. Another rule that is commonly proposed is AI should identify itself as AI.
*  There could be protocols, perhaps crypto enabled protocols of some sort to
*  indicate that you are engaged with an AI agent, where it's like who controls it, what its provenance
*  is, et cetera. Can you put any more meat on that bone? Because I feel like that could be coming
*  soon. I feel like we do have a lot of the stuff that could cause us to tip over a threshold.
*  I think both what that looks like is dramatically under theorized and what we can do to make sure
*  it looks good is also largely a blank space right now, unfortunately. Yeah. I still think we're a
*  long ways away from that being a reality. We've been almost there for decades now. Yes, I think
*  the advent of Chad GPT and making it that much more approachable has been a huge boost. Some of
*  these new architectures and the combination of hardware advancements and making things cheap
*  enough, making things accessible enough for developers really led to this Cambrian style
*  explosion over the last two years with AI. We're hoping to do the same thing with AI agents,
*  with agent.ai in terms of citizen developers. You don't need technical skills. Build agents, tweak
*  them for your own use cases. I don't think we're going to, even if let's say we were to have
*  some kind of major technical breakthroughs tomorrow, I still think you're going to need
*  people in the loop in some fashion, right? Unless you couple that with robots that can actually,
*  we can plant this into and make them cheap enough in which again, I think we're even a ways away
*  from, I love my Tesla, but we're a ways away from actual self-driving in any real shape or fashion
*  that ever rains or there's snow or anything like that. But assume that were the case. Assume
*  tomorrow we have Chad GPT 6, they jump over 5, it's 6 now, it can plan, it can execute.
*  It's way above human intelligence and it's continuing to learn exponentially at this point.
*  And the best way to make sure that we as people stay competitive is to embrace these tools,
*  to figure out how can we leverage them to create business value? Because by themselves,
*  as an engineer, I love cool technology, I have every gadget that you could ever get and I'm
*  always experimenting with the beta stuff before it's ready for everybody else. But part of what's
*  missing is really tying that to, okay, but how will it make money? How is it going to give
*  meaningfully better outcomes for real businesses trying to do mostly predictable, structured type
*  of work on a daily basis? That's what a lot of people are doing in a lot of these companies.
*  What would that mean for manufacturing? How can we improve safety with AI? Like actually make
*  people's lives better and safer in let's say factory settings with more sensors or more
*  predictive intelligence embedded. I think there are a lot of opportunities there as well.
*  And really, I think we need to be more curious about how can we make our lives better and evolve
*  the way we've been thinking about work. I don't think it needs to be this kind of doom and gloom
*  scenario where now nobody has jobs and what are we going to do? I think we should be thinking about
*  how can we reimagine every single job? If you could outsource 80% of what you do on a daily
*  basis, 80% of those tasks, how can we structure them? How can we reimagine them completely? Maybe
*  they're not even necessary with more system dynamics optimizations across the organization
*  in a way that will enable you to get the same outcomes or better, hopefully better, and do that
*  in a way that is much more efficient by blending human beings and what they're really good at and
*  their creative thinking and some of their defining parameters for success and tying to a broader
*  strategy and some of the political pieces, some of the social aspects of actually getting the job
*  done versus just inputs and outputs out of a computer. And those are the kinds of things that
*  I think we're still there early on in terms of tying that to business contexts, which again,
*  is part of what we're trying to figure out with agent.ai is how can we bring these agents to
*  companies? We're very much focused on small businesses, not enterprise. We're talking about
*  solopreneurs, small businesses, really anyone trying to build these agents and use them.
*  If you're an enterprise trying to use agent.ai, it's not for you. We're very much focused on that
*  zero to a hundred sort of size companies and figure out how can we make your lives easier with some
*  of these tools. And we're going to be right there bringing these advancements to people,
*  but also making it easy to build them. I still think even if tomorrow we have a new model and
*  now it's more amazing on certain benchmarks in certain scenarios, you're still going to need to
*  integrate it. You're still going to need to change workflows and define the problem and define
*  ground truth. And maybe it's going to be that much better at making things up and hallucinating to
*  the point where you can't tell the difference. Okay. How do we solve that? I mean, there's a lot
*  of things that we haven't really solved yet from an objective reasoning standpoint. And I think we
*  have a lot to do there even if we have much more intelligent systems, which I have no question that
*  we'll have them. But I think the other pieces are not there yet to even take full advantage of what
*  we have today, of using that to the full potential, using that in an efficient way. Now, if we have
*  Chiat GPT 6 and it has a hundred million token context window, you do all this kind of work real
*  time. Again, those are going to be very different. It's a different world that we're going to be
*  living in. But at the same time, we started 18 months ago to two years ago, but you're following
*  GPT 2 with a thousand token windows and very low capabilities. And we were thousands of times
*  better now in their regards, even if these models are thousands of times better than what we have
*  today. I don't think it's going to take away jobs in the way that some folks worry about. I think we
*  still need to figure out so much more in terms of the incentive systems and tying it to real
*  businesses, which is still very early, which is an amazing opportunity for anyone interested in the
*  space, interested in this kind of work. We need people to help shape that what this future state
*  is going to look like. Well, that might be a great note for us to close on the site where people can
*  build agents and start to contribute to the marketplace is agent.ai. Hard to imagine a better
*  domain for this opportunity than that. So I definitely encourage folks to check it out.
*  Any closing thoughts before we break? I just want to thank you again. Appreciate the conversation
*  today. I had a lot of thought provoking questions and back and forth. And I'm extremely optimistic
*  in terms of what the future is going to look like, what platform like agent.ai can democratize.
*  Can make AI more approachable, easier to use. I have a three-year-old son and as I'm thinking
*  about what does the world look like when he grows up, right? As he's using more of these tools
*  and thinking about doing schoolwork all the way to what will does day-to-day job even look like.
*  We want to make tools that are easy for anybody to use, easy for anybody to build themselves,
*  customize, maybe not three-year-olds, but close. I think that's at the very least interact with them.
*  Essentially talking to Alexa every day and asking for things, videos to play and things like that.
*  I imagine the world that we're building to be much better than the one that we're living in today.
*  And I think AI can really be part of that solution. I think we can use it to help solve a lot of
*  problems that we have in terms of climate change, in terms of how do we connect people
*  better and ultimately create a community. And democratizing through this kind of technology,
*  make it more accessible so that it really can make anybody's lives easier, better. You can focus more
*  on what you're passionate about. And ultimately we want to make it for everybody. We want to make it
*  something that it's not, you don't need to be in a fortune 500 enterprise to be able to use these
*  tools to be able to get meaningful outcomes. You can be an entrepreneur, you can be a small business
*  and that backbone of the economy. That's what we're focused on. That's what we're trying to enable.
*  And humbling to read the feedback of people using our platform and both positive and negative. I
*  think there's opportunities to improve every day and kind of seeing, okay, but this has a meaningful
*  impact. We're seeing people tell us their stories in terms of the different kinds of ideas they've
*  gotten that they wouldn't have gotten otherwise and how easy it was for them to build their first
*  agent to come up with recipes to stay healthier. And things like you and I may have never thought
*  of that, but you know, human creativity is kind of unbounded and it's just super reassuring to see
*  that these tools really create more meaningful connections and sort of human experiences.
*  Hopefully get actual work done better and faster and cheaper and then help us discover more of what
*  we're really passionate about and help us do that. So super exciting. Last note, we're always
*  hiring if you're interested in working in GTM, marketing, sales capabilities or engineering-wise
*  to help build product. We're always looking for top-notch individual contributors. We're a very
*  small team, about 12 of us in freelance capacity or another, but we're always looking to grow.
*  So if this sounds interesting to you, if you want to be part of shaping some of this in some way,
*  feel free to reach out, andre at agent.ai or just through the website feedback and we'll get back to
*  you. Love it. Andre Oprasan, agent.ai. Thank you for being part of the cognitive revolution.
*  Thank you, Nathan. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at tcr
*  at turpentine.co or you can DM me on the social media platform of your choice.
