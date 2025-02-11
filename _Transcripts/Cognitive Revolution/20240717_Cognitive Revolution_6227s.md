---
Date Generated: October 30, 2024
Transcription Model: whisper medium 20231117
Length: 6227s
Video Keywords: []
Video Views: 789
Video Rating: None
Video Description: Nathan explores the Guaranteed Safe AI Framework with co-authors Ben Goldhaber and Nora Ammann. In this episode of The Cognitive Revolution, we discuss their groundbreaking position paper on ensuring robust and reliable AI systems. Join us for an in-depth conversation about the three-part system governing AI behavior and its potential impact on the future of AI safety.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: Complex Systems
Patrick McKenzie (@patio11) talks to experts who understand the complicated but not unknowable systems we rely on. You might be surprised at how quickly Patrick and his guests can put you in the top 1% of understanding for stock trading, tech hiring, and more.
Spotify: https://open.spotify.com/show/3Mos4VE3figVXleHDqfXOH
Apple: https://podcasts.apple.com/us/podcast/complex-systems-with-patrick-mckenzie-patio11/id1753399812

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:04:39) Introduction
(00:07:58) Convergence
(00:10:32) Safety guarantees
(00:14:35) World model (Part 1)
(00:22:22) Sponsors: Oracle | Brave
(00:24:31) World model (Part 2)
(00:26:55) AI boxing
(00:30:28) Verifier
(00:33:33) Sponsors: Omneky | Squad
(00:35:20) Example: Self-Driving Cars
(00:38:08) Moral Desiderata
(00:41:09) Trolley Problems
(00:47:24) How to approach the world model
(00:50:50) Deriving the world model
(00:55:13) How far should the world model extend?
(01:00:55) Safety through narrowness
(01:02:38) Safety specs
(01:08:26) Experiments
(01:11:25) How GSAI can help in the short term
(01:27:40) What would be the basis for the world model?
(01:31:23) Interpretability
(01:34:24) Competitive dynamics
(01:37:35) Regulation
(01:42:02) GSAI authors
(01:43:25) Outro
---

# Guaranteed Safe AI? World Models, Safety Specs, & Verifiers, with Nora Ammann & Ben Goldhaber
**Cognitive Revolution:** [July 17, 2024](https://www.youtube.com/watch?v=fyVrnbn4EWA)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm excited to bring you a conversation
*  with Ben Goldhaber and returning guest Nora Amman, co-authors of a major new multi-institution
*  position paper called Tord's Guaranteed Safe AI, a framework for ensuring robust and reliable AI
*  systems, which they co-authored with intellectual giants, Joshua Benjio, Stuart Russell, Max Tegmark,
*  and Steve Omohundro, among others. As regular listeners will know, I'm always on the lookout
*  for AI safety solutions that might really work, in the sense that they have the potential to make AI
*  systems safe enough that we no longer really need to worry about AI safety. The Guaranteed
*  Safe AI framework, or GSAI for short, is a notable attempt from serious people to advance the field
*  toward this lofty goal. The proposal is to use a three-part system to govern an AI's behavior,
*  a world model, which is responsible for quantitatively modeling an AI system's
*  impact on the world, a safety specification, which defines what impacts and outcomes are
*  acceptable, and a verifier, which is responsible for checking that the AI system's proposed actions
*  lead to acceptable outcomes according to the world model's predictions. The goal is to provide high
*  assurance quantitative safety guarantees, making AI safety a more engineering-like discipline with
*  explicit assumptions and tolerances that are designed into the systems as they are built,
*  as is the norm today when designing other safety-critical infrastructure, such as bridges,
*  airplanes, or power plants. The applications of this framework to things like self-driving cars
*  and domestic service robots are quite clear, and interestingly, one nice benefit of this approach
*  is how it might enable more democratic governance of AI systems by grounding the debate over what
*  behaviors we want and what risks we're willing to take. When it comes to highly general systems,
*  like today's frontier language models and their presumably more powerful successors, however,
*  things do get a bit fuzzier relative to the current paradigm of testing models during and
*  after training and then trying to remove unsafe behaviors with post-training, this does seem like
*  a clear conceptual advance. However, the challenges of general purpose world modeling and the subtlety
*  required for an effective general purpose safety specification loom large as open research problems,
*  and certainly at present, even a best effort attempt to implement GSAI could not ensure that
*  nothing major could ever go wrong. Nora and Ben, as you'll hear, are very realistic about this,
*  and ultimately see GSAI as just one important part of a broader portfolio of AI risk management
*  strategies, which they ultimately hope society will deploy as part of a holistic defense in-depth
*  approach. One note on this episode, which I'm honestly a bit embarrassed about, but still feel
*  compelled to share. I experimented with a new approach to AI-assisted preparation for this
*  conversation, and unfortunately, it kind of backfired on me. Instead of reading the paper
*  end-to-end like I normally do and using AI for background question answering, in this case,
*  I loaded the paper up into ChatGPT and had a verbal conversation with GPT-4.0 while on a long
*  walk. Unfortunately, it turns out that I had some subtle misconceptions going into that dialogue,
*  and GPT-4.0 was a bit too sycophantic in response to my questions, running with my incorrect premises,
*  when it ideally would have challenged and disabused me of them. The result is that I was still a
*  little bit confused about some important aspects of the GSAI framework until roughly the 30-minute
*  mark of this episode, when Nora and Ben finally set me straight. While the final product is clear
*  enough that I probably could have gotten away without mentioning this, considering how much I
*  encourage others to adopt new AI-powered workflows, I feel like I owe you transparency when I allow
*  myself to be led astray by an AI model. I absolutely will keep experimenting with new AI-assisted
*  approaches like this. As we discussed in this episode, given the overwhelming volume of new AI
*  research and products coming out all the time, there's really no choice but to adopt some AI-enabled
*  information processing strategy. But I will try to hold myself accountable as I do, and if nothing
*  else, I hope this reminder will save somebody else from a similar mistake. All that said, as always,
*  if you're finding value in the show, we appreciate it when you share the Cognitive Revolution with
*  friends, we invite your feedback and your resumes on our website, cognitiverevolution.ai, and I will
*  welcome and respond to any and all DMs on Twitter or any other social network. Now, I hope you enjoy
*  this deep dive into the guaranteed safe AI framework with authors Nora Amann and Ben
*  Goldhaber. Nora Amann and Ben Goldhaber, authors of the really remarkable and interesting paper,
*  Guaranteed Safe AI. Welcome to the Cognitive Revolution. Thank you. Thank you for having us.
*  Yeah, I'm excited about this. I guess for context, I'm always on the lookout for things that can
*  change the AI landscape in any meaningful way. And certainly one of the things that I'm always
*  looking for is a proposal for AI safety that can quote unquote really work. I think part of what
*  we'll be doing over the course of this session is teasing apart like what that means and helping
*  me figure out if that's a confusion or if I should be changing the way I'm thinking about that.
*  But maybe for starters, this is a paper with a bunch of different authors from a bunch of
*  different institutions. So I'd be interested to hear each of your backgrounds, how you guys
*  assembled the team to do this, what motivated you, then you can use that as a way to introduce the
*  project. Yeah, happy to speak to it. I work at FAR AI and our goal is to incubate high impact
*  AI safety agendas, in particular new ones, exactly like you spoke to. We're on the lookout for what
*  we see as promising AI safety agendas. And one of the things that struck us was when we were speaking
*  to folks like Davida, David Dalrymple, who I think deserves credit for, along with several other
*  of the co-authors like Max Tegmark, Joshua Bengio, others, when they were connected at Bletchley Park
*  at the AI safety summit in the UK in November, they really realized the degree to which their own
*  AI safety agendas were starting to converge around a shared principle, around a shared framework.
*  And then in speaking more with Davida, we agreed and it was quite exciting to think that many of
*  these senior, very distinguished AI researchers had almost independently or to some extent
*  independently found this emerging framework into the degree to which we could help spur that and
*  make it more legible, really understand the similarities and dissimilarities of it. We
*  expected that kind of deconfusion could really spur more field building, more growth, help find
*  an AI safety framework that could really work. And so that was, I'd say really some of the impetus
*  of it. Nora and I were quite excited to be able to push this forward and bring this to a point
*  where we had a clear paper along with a series of workshops for creating that paper and understanding
*  it better that we could then share with the world. Yeah, I think it helps contextualize
*  what the nature of the paper. So it's like a position paper, a multi-author position paper,
*  where we're like mainly trying to talk about here is a family of approaches. They go about
*  implementing this shared high level architecture in different ways, some differing views as how to
*  go about this, but they have these sort of shared core components, et cetera. And yeah, so the paper
*  focuses in that sense, somewhat on that high level on the lecture components. And then many of the
*  individual authors have like expertise and in different aspects of this or have different
*  views as to like how exactly one might try to implement this. Yeah.
*  Yeah. So we did a previous episode where we talked about your work in trying to figure out
*  ways to borrow from other disciplines. It sounds like that is really at work here as well. Could
*  you give us a little bit of the backstory of Convergence? I know some of the names on the
*  paper and I think listeners will be familiar with some of them too. What are the origins of
*  their approaches and how would you characterize this convergence? Maybe just give a little bit
*  of how the different backgrounds of different authors has seemingly converged on an idea.
*  Yeah, I can't speak for all of the authors. I don't actually know the detailed story for that
*  for everyone, but I think at least one common denominator that I do think is there is actually
*  not so much to like interdisciplinarity, but basically noticing that I think, hey, we actually
*  just need higher expectations as to what we want to get out of safety approaches. And in particular,
*  a lot of current approaches, a lot of purely empirical approaches might not on their own get
*  us all the way. And I think that created some core lessons about this sense of could we somehow get
*  to quantitative safety assurances or risk assessment that put us on a different foundation to start
*  with as to what we can even expect from safety standards. And I think one place this is taking
*  inspiration from is other engineering domains, civil engineering, engineering for critical
*  infrastructure. So there's a quote we have is also in the paper, but I think it's just really
*  interesting. In the 1870s, apparently something like 20, 25% of bridges used to collapse within
*  10 years, which is kind of wild, right? And then fast forward a couple of decades. Nowadays,
*  the state of the art for civil engineering is that we can make extremely precise, extremely
*  calibrated statements like there's less than a million chance that this particular bridge will
*  collapse in the next 10 years if we don't load it with more than three tons or whatever the specifics,
*  which I think is just a qualitatively different place that this field of engineering is at.
*  And yeah, so if we have managed to get there, when it comes to civil engineering, when it comes to
*  nuclear plants and stuff like that, I think now clearly we want to have these sort of safety
*  standards or expectations as to the risks we are willing to accept for these systems. So that's
*  sort of like the culture around many engineering practices in general. And I think one driving
*  motivator here is something like, can we have that for AI? And also I think we need this for AI because
*  increasingly either AI systems will be used in safety critical domains or itself will become
*  safety critical in various ways. And I think that's for a lot of the core authors, maybe a shared
*  generator or motivator to think in these directions. And then obviously a different
*  authors come from different areas of expertise, whether that's in the formal verification domain,
*  which is a part of this framework or other domains. Yeah, there's a couple of phrases you use there
*  that I think are really interesting. One is like the level of risk that we're willing to accept.
*  And the other is this notion of caveating the guarantees. Basically, I think many of us have
*  been involved in conversations over the years in which phrases like solve alignment or solve AI
*  safety are thrown around. And even my like really work somewhat tongue in cheek is kind of that same
*  idea of like, is there something that could really solve this once and for all across all
*  circumstances or whatever? And something that kind of indicates to me that this is likely a step
*  forward in terms of de-confusing the conversation is the shift toward a more quantitative type
*  statement that's not like it's solved or it's not solved. It's not some binary situation, but rather
*  moving toward a paradigm like engineering tolerances. So I want to actually unpack the
*  framework and talk about the different components of it. But maybe for starters, what sort of
*  guarantee should we expect from a guaranteed safe AI system? Can you put a little bit more
*  texture on like the sorts of statements that you think we might be able to make if we pursue
*  this direction? Yeah. So I think it's useful to think about this in the context of making a
*  affirmative cases for safety. Like we want to move from this paradigm of we're doing
*  evaluations only. I think evaluations are very valuable and I'm like really glad that there's
*  this current push for them. But I think a better place to end up in when we're trying to use
*  powerful AI systems and safety critical domains is to be able to have, as Nora illustrated with the
*  bridge example, be able to move from like this kind of almost black box testing to a regime
*  that has strong theoretical grounding for why a AI system in a given environment is safe. So both
*  the theoretical grounding and then the empirical testing and the guarantees that can come from
*  that such that we have precise calibrated quantifiable estimates of failure rates and
*  what failure can look either like known failures or handling uncertainty in some way where we're
*  like uncertain about like how far this guarantee can actually extend for the performance we expect.
*  So I see that as a big motivating case for this framework and exactly as Nora mentioned earlier,
*  it was one of the things that brought the authors together. And so what I expect this to look like
*  is in a specific area, let's say power infrastructure, being able to
*  provide calibrated estimates of given this AI system being deployed in this way and given these
*  kind of safety specifications, like we know we want it to like generate plans that operate within a
*  specific tolerance, being able to formally verify that and provide estimates of a certain type
*  that like yes, one in a million chances that this goes outside of the safety specifications
*  that we expect. And actually, let me actually just back up for a second. When I said formally verify,
*  really this is going towards the framework that we see as being like the unifying underlying model
*  for a guaranteed safe AI. So having three components, a world model, a safety specifications,
*  and then a verifier where put together these can box in AI in a certain way such that the
*  plans that come from it are able to be verified and provide specific quantitative risk estimates
*  of what's going to happen. We can go into depth on any of those components, but I think operating
*  together and in point of fact, that is what the paper was trying to do is define these components
*  and point out the way in which together they can provide guarantees that can give people and society
*  at large a handle on how safe an AI system is in a specific narrow area. Yeah, that narrowness
*  concept is one that I definitely want to come back to and push on a little bit later as well,
*  but we have time to go into all three of these components in depth. Again, I like the fact that
*  this moves us from a discourse right now, which is so often confused about, you know, do these
*  AIs have world models? Maybe they do, maybe they don't. Again, this is almost certainly something
*  that's like not binary in the most interesting cases. And now we're starting to move toward
*  with this framework. Yes, there is going to be a world model. And the question is going to be like,
*  how good is it? Plus one there, like something this is a little bit further field before diving
*  into world models, but something that I found really exciting about the guaranteed safe AI
*  concept is the degree to which this unifies traditional proponents of AI safety and people
*  who are often thought of as critics of AI safety, you know, the Twitterati, IAC cohort. Like I think
*  many of the ideas that we talk about in this paper are about moving from this place of like
*  uncertainty to more quantified uncertainty. We talk a little bit about this in the paper,
*  at least in the diagrams, like Jan LeCun's proposals for, I forget the name of his agenda,
*  but has a lot of similarities here as well. And it's, we want to shift the discussion from,
*  is something safe in general and more like in this area, can we make an affirmative case that it is
*  safe? And it feels like something that kind of everybody can and should agree on. It's almost
*  common sense for deploying AI systems and nuclear power grid. We want to be able to know like,
*  under what conditions is this safe? Yeah, I certainly agree. Everybody wants things to
*  graduate from philosophy to engineering. And so that's a great bridge to cross, if you will.
*  I do think it is maybe worth just reflecting again for a second on kind of the craziness of the
*  current setup where we are first building the thing and then going out and first of all,
*  like figuring out what it can do and how it might be safe or unsafe and just the surface area on
*  these things is especially, of course, the, I'm thinking mostly here of the large language models
*  and large multimodal models these days. It is a paradigm breaker in and of itself that you would
*  go build something with so many resources put into it that has such vast capabilities. And then after
*  the fact, the only really begin to map out what they are or what the challenges associated with
*  that might be. I think everybody would like to improve on that. So let's get into the world model
*  and then we'll go to safety specification verifier from there. Cool. Yeah, I think I
*  can maybe touch on that. So one thing to maybe clarify or de-confuse from the start is that
*  because you led on with something like, oh, do our current AI systems have world model,
*  which is an interesting question. There's different ways in the GSA AI framework this
*  can be implemented, but I think at least conceptually, I think it's like appropriate
*  to think of the world model as separate from the AI system. One reason we want the world model is
*  this is like the framework relative to which A, we specify the safety specs and B, relative to
*  which we're getting our verification from. So this is just zooming out a bit or to contextualize
*  that is how can we get from purely empirical testing to quantitative safety guarantees?
*  The only way we can do this is by one of the ways, I'm not sure it's the only one of the ways is by
*  having a model-based approach. So this is where in the GSA case, the world model comes in.
*  There's another thing I think I want to say here, which is why is empirical testing not enough or
*  on its own not enough? I think it is like important to say is we're looking at a set of
*  examples and the sort of check for those examples, does anything go wrong? And that's good. And then
*  we know that for those examples, it didn't go wrong or whatever, but we're not going to test
*  exhaustively. And because of that, we don't really know where we're going to end up in terms of safety.
*  And there's sort of two main reasons why we're not going to test exhaustively. One, there will be a
*  lot of testing, but to underscore that, for one, we have sort of these deceptive alignment kind of
*  worries where maybe the model itself or the air system itself that we interact with wants to in
*  however way sort of actively try to avoid showing the failure modes that we will see in a deployment,
*  whether that's having backdoors that makes it really hard to find those failures, scenarios,
*  et cetera. And the other problem is that if you have a really big and powerful systems and you
*  deploy it into the world, it probably is going to push the world in new sort of unforeseen
*  distributions just by virtue of being transformative. So I think that's some really important reasons
*  why we can't expect empirical testing alone to get us where we need to be. But then the
*  question is like, okay, like what else can we do? So like in the paper, we're like one way we can
*  maybe go beyond this is by having a model-based approach. So going into what does it mean to have
*  a world model, we'll probably say this a number of times, like different approaches might go about
*  this differently. The core function of the world model is to have some explicit representation
*  somewhere of plausible world trajectories, right? As well as being able to account for
*  counterfactually what would happen if I intervene in the world in this and this way. So we want to
*  have a model that can capture if a system tried to take action A, what would happen then if it did
*  action B, what would happen then? So that's the like function of the world model. How can you do
*  that? In the paper, we have these scales to contextualize all of our three core components,
*  like you can implement them at different levels of rigor, by which we mean something like if in
*  fact you manage to implement this at this level, this will basically afford you higher confidence
*  safety assurances. And then there is some question about how tractable the given level is, but that
*  the inherent trade-off we kind of face with all of these scales. And the examples of the GSAI
*  approaches pursued by different authors, they might do things like proper mathematical modeling.
*  So this might look like having a meta ontology, a meta semantics, which is a mathematical framework
*  to express a lot of things, including different types of uncertainty. We want to be able to account
*  for Bayesian uncertainty, but we also want to account for model uncertainty because modeling
*  complex domains is like really hard and the goal really can't be so much and like, let's get it
*  just exactly right. But let's handle uncertainty as good as we can such that we maybe have to be
*  a little bit conservative. But when we say this is safe in these ways, we're pretty confident we've
*  captured what will go wrong. And then depending on how you do this, you basically use current day
*  generative AI systems to help you accelerate the process of world modeling more or less.
*  Like in a severely simple domain, maybe you could do all of the world modeling by hand,
*  but then in most of the domains that we're like interested in, this is just not tractable. So one
*  of the ideas and one of the reasons for why this paper has come together now and why we think this
*  is timely context is that generative AI is getting really good in for some purposes. It's not reliable,
*  but it's like very generative. The question is, can we make smart use of it to help us build these
*  formal mathematical world models, but much faster? And the hope or like really the aspiration is for
*  these world models ideally to be auditable, human auditable, because if you don't have them human
*  auditable, you can't be as confident in what is even happening in your world model. So yeah,
*  we can say some unsupervised learning or model free RL, it has a world model somewhere, but we
*  really don't know what the world model is, which is why we don't know how it's going to behave out
*  of distribution. But if in that we make the world models human auditable, we can use our best
*  scientific understanding so far and be like, is this current model compatible with the best of what
*  we know and where we're uncertain? Have we accounted for the uncertainties appropriately?
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber eight by eight and Databricks Mosaic, take a free test drive of OCI
*  at oracle.com slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index
*  an independent index of the web with over 20 billion web pages. So what makes the Brave
*  Search index stand out? One, it's entirely independent and built from scratch. That means
*  no big tech biases or extortionate prices. Two, it's built on real page visits from actual humans
*  collected anonymously, of course, which filters out tons of junk data. And three, the index is
*  refreshed with 10s of millions of pages daily. So it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with
*  retrieval augmentation at the time of inference, all while remaining affordable with developer
*  first pricing. Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API. So is it right to say keeping on this theme of moving from
*  black box, build it first and test it to a more engineered system? Is it a common theme in like
*  software engineering is separation of concerns. And the idea that like different parts of your
*  system should just do what they do and then the overall system serves a function. Is it
*  fair to say that the world model is meant to be purely predictive and separated from the part of
*  the system that is taking the action? I think that this is somewhat true, but let me note for clarity
*  that I think that there's the AI in the world model within the AI and the way that AI progress
*  has been advancing, there hasn't been this separation of concerns as you describe it.
*  Some proposals, in fact, one of the initial inspirations, at least for some of the AI safety
*  authors, some of the co-authors on this ideas, like Eric Drexler and his proposal for open agency
*  architecture really emphasizes the benefits that we get from separation of concerns, having different
*  modules, do different parts, which could be human audible. I think that there's a difference here,
*  which is that in this case, we're like doing a level up, which is saying, okay, we have a general
*  purpose AI that hopefully has been trained in good ways. Like maybe there's a lot of other
*  approaches for making this AI more aligned with human values safer, but then there's also the
*  like one level up from that, which is what is the system in which the AI is embedded. And in this
*  case, we still have this emphasis of separation of concerns, having different modules, having the
*  world model module, having the safety specifications, having the verification, which together with the
*  fourth part of this, the AI all equate to a safer system. I'm worried that was a tad pedantic. The
*  only reason why I stress this is because I think the separation of concerns is exactly right, but
*  then there's the world model, which we can build with a variety of different ways in which should
*  be ideally compositional, human audible, all of these different good properties,
*  but that together in concert with the AI's world model and the safety specs and the verification
*  can lead to a much more trustworthy set of actions that the AI is going to take.
*  One way I sometimes put this, or it feels like conceptually clearer in my head is that
*  maybe some listeners are familiar with a couple of years ago, there was these AI boxing proposals.
*  What if we do an Oracle AI, right? The AI is only allowed to answer our queries and it doesn't do
*  anything else. Would it still be dangerous as well as other approaches? Now, I think there's
*  many reasons why these approaches don't actually help so much because even if the AI talks to people,
*  the AI can convince people of doing things, et cetera. So they don't get to the place where
*  maybe initially there was some hope for that. But I think it's interesting in our context to ask,
*  is GSA AI a type of boxing proposal? I think there is some similarity and there's also an
*  important difference. I think the way we'll put it is like, it's sort of a boxing idea, but rather
*  than boxing the AI system by limiting the effectuators or how we can affect the world,
*  we are boxing it basically by having this verification gate that is composed of the
*  world model, the safety specs and the verifier. And together these three components build a gate
*  such that the AI system is only allowed to directly affect the world after it has passed
*  that gate, namely after the verifier has confirmed that there's a below certain threshold chance that
*  this proposed action by the AI is going to be harmful. Yeah, that's interesting. So I'm looking
*  at figure one in the paper and I do think one thing I was asking myself along the way is like,
*  where is the AI in this? And that's sort of the unspoken fourth component, right?
*  So I think there's a way in which, I mean, AI is a notoriously confusing world. So I think
*  it's basically in two places. It's mainly in this containment, right? We're basically being
*  agnostic in this paper about what methods you use to have a powerful AI that comes up with your
*  proposed plan for solving the problem you gave it. It could be anything. We can imagine it to be
*  sort of today type generative transformer model, whatever. So that's one place where the AI is.
*  And basically this is the AI we're asking, hey, here's the problem we want to have a solution for.
*  Please propose a solution. So that's where the AI is in the most substantive sense is. And then,
*  as I said, it has to pass this verification gate. There's a little bit of sense in which the AI
*  comes up potentially in different places or a different AI tooling comes up in different places,
*  namely by helping us build the different components in a more tractable way. So by helping
*  us be faster at building more complex world models or at specifying the safety specs.
*  And I think here it's correct to think of the AI as AI tooling, really just enhancing
*  human reasoning, enhancing mathematical modeling, and making it more tractable.
*  – Why don't we finish out the three parts of the thing and build the full scaffolding,
*  and then we can maybe dive into a little bit more depth on the world model again,
*  and maybe some of the others too. But I'm gradually realizing that, and I probably
*  hadn't appreciated this enough as I was reading the paper originally, how much this is all additive
*  to whatever AI system you might have. The proposal is less about this is how you build an AI and more
*  about this is how you figure out how to constrain it or make sure it's operating within some bounds.
*  In a way, there's maybe two world models operating here. There's the main AI, whatever the AI is,
*  that's a black box AI, which has this unpredictable behavior. And then you have a distinct world model
*  that sits outside of that. – I'll do the quick version and then we can dive into the different
*  bits. Basically, the three components, we already talked about the world model, in short, meant to
*  capture what are the plausible world trajectories and in particular, kind of factually upon
*  intervention, what possibly can happen. Next up, the safety specification. The main function is to
*  capture the specifications that we want the system to satisfy. This can capture functional
*  requirements and it can capture things like what do we want and don't want to happen.
*  Safety specification is typically expressed in the semantic language of the world model and in terms
*  of the world model. And then the third component is the verifier, which then basically takes an
*  AI output, sort of proposed action. The AI system says, here is my action or here is my policy,
*  gives it to the verifier and the verifier takes that and then compares it to the specification
*  as it is represented in the world model and checks if we run this action or this policy in the world
*  model, does it conflict with what we defined in the safety specification? And if the chances of
*  that is below some thresholds, then we are like, yep, this is now a verified output. We can go ahead
*  and actually deploy this. So that's the core or to put it very simply, that's the core architecture.
*  There is in fact plenty of nuance as to like, concretely, how do you implement that? And there's
*  very different solutions to that. Maybe one more thing I want to add on top of this like basic
*  three-component structure is you also see this in the first figure, like what we termed the
*  deployment structure. This is like not necessarily part of the core structure. Not all authors would
*  emphasize that to the same extent, but in the spirit of like defense in depth, I think it's
*  like practically pretty important part. The type of things a deployment infrastructure would do
*  is once you have a verified output and you deploy that in the world on some time horizon that you
*  have verified it over, you want to keep making observations and in particular checking whether
*  the actual real world observations that you're making, whether they start to deviate from what
*  your model suggested. Because if they start to deviate, something is going wrong. And then if
*  you were to notice that you would want to maybe, this is sometimes called failover or failsafe.
*  So you would want to transit into some backup system that is maybe more conservative, but that
*  you're even more confident is safe, which is another layer to capture some of the uncertainty
*  that you have in your world model. So that's maybe the fourth component here. And yeah,
*  together we are saying that for this composite system, you can formulate quantitative safety
*  guarantees relative to your world model, which of course makes assumptions, but at least these
*  assumptions are now explicit. And now we can actually go in and critique, like maybe someone
*  can go in and say, hey, this world model is not capturing this part or et cetera. We can actually
*  start to critique the assumptions that go into these safety guarantees. Whereas if we have purely
*  black box approaches, there is also plenty of assumptions, but they are not made explicit or
*  it's hard to make them explicit. And it's also harder to critique them. So I think that's maybe
*  the overview. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old
*  ex-Fang senior software engineer as much as the next guy, but honestly I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so you don't have to. With teams across Asia and South America, we can cover you no matter
*  which time zone you operate in. Their engineers follow your process and use your tools. They work
*  with React, Next.js, or your favorite front-end frameworks. And on the back end, they're experts
*  at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost more than
*  the random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  So maybe it would be helpful to sketch out one possible example implementation of this.
*  Maybe we'll take a notoriously easy domain like self-driving cars, for example.
*  I'm also interested in to what degree, and I don't know if you would know or if anyone
*  outside of the companies knows, but I wonder to what degree the leaders are actually pursuing
*  something maybe like this already. So let's say I'm building a self-driving car and I, first of all,
*  just gather a ton of driving data and train a giant black box neural net on it. And I have
*  inputs and outputs. My inputs are like, here's the eight camera views around the car and here's
*  your current GPS coordinate and here's the map and here's the destination target that you're
*  supposed to get to. And then the outputs are like, hit the gas, hit the brake, steer, put on a turn
*  signal, whatever. So you've got the kind of classic, I don't know what it's doing in their
*  problem, but I just know that these are the inputs, these are the outputs, and it's trained on enough
*  data and it seems to work. And now I would want to say, geez, okay, that's a good start, but can I
*  actually deploy this? How many crashes am I going to have every however many miles or whatever?
*  Now we would say, okay, we're going to have a world model, which in this case would presumably
*  be like a Newtonian physics style world model where you'd have an explicit representation of
*  objects and metadata about what kind of objects they appear to be and sense of their current
*  momentum and things along those lines. Safety specification in this regard would be like,
*  you could feel free to help me here, but I would assume things like you would not want to have a
*  momentum change in the car that exceeds a certain maximum acceleration or whatever.
*  Bumping into things obviously would be bad. You maybe could define that in terms of acceleration
*  of yourself or other things that you might be bumping into. I know of a friend who works in
*  train design and specifically in rider comfort. So this is like a big thing that he's responsible
*  for is like, when we go around curves, how is this thing going to go so that people don't slide off
*  their seats? So you have all these core measurements that we want to stay within. The verifier would be
*  a module that says, okay, the black box, just given these camera inputs and objectives,
*  said hit the gas and turn the wheel this much. Now I'm going to run that in simulation over
*  a couple of timestamps in my world model and check to see what's expected. And if everything appears
*  to be staying within this safety specification, then we can proceed. Otherwise we have to
*  slow down or not do it or pull over to the side of the road or something along those lines.
*  That's right. I think that's a good illustrative example. And two things I really like from the
*  example you provided there was like one, the rider comfort example you gave with the train design.
*  I think that's a good example of the way in which there's going to be safety specifications of
*  faring moral desiderata. Like a pretentious way of saying, yes, sometimes we're going to
*  want safety specifications that are like, don't hit this human or do not cross a double yellow line
*  in these kinds of circumstances. But then there's also going to be ones that look like we have
*  preferences and we have bounds in order to keep humans safe and comfortable that we're going to
*  want to maximize or we're going to want to follow or have like quantitative guarantees around.
*  Safety specifications along with the world model are probably going to be composite.
*  So to the second part of this example, I think is really illustrative is on the world model,
*  there's different degrees of depth you can use for a world model. You could build it up from
*  Newtonian physics and depending upon the domain and our ability to build these kind of complex
*  world models or even lower than Newtonian physics, like we could go deeper on these kinds of things
*  and depending upon our abilities with advances in AI and other technologies and the specific field
*  and our uncertainty, we can and should. But there's also versions of this that look like
*  building it up from simpler simulations, from simpler world models that could look like
*  simple abstractions of the car's trajectory or the brighter behavior in other cars.
*  And so we can take this kind of composite approach to be able to build up world models
*  and safety specifications across a lot of different scenarios. I do think versions of this
*  are being done in the leading self-driving car companies today. And it's interesting both to see
*  this as a way in which guaranteed safe AI is building up from existing engineering practices,
*  which I think is a really good sign about its like validity. It's not just building castles in the
*  sky or whatever. It's like actually trying to draw from existing disciplines and safety engineering.
*  And it's illustrative of the many challenges for using the guaranteed safe AI approach in
*  complex domains. For instance, when does a car actually cross the double yellow lines?
*  95% of the time or some number that I'm just pulling out, you don't want that to happen. But
*  there are situations in which you in fact do want it. You want it to move to the side to avoid
*  a person in the road or some kind of obstacle. This is the way in which it's going to be
*  challenging to be able to create the safety specifications that are flexible enough to be
*  able to handle the dynamic, unpredictable nature of the world. But it does show the pattern in which,
*  yes, we're doing things like this now in order to be able to get guarantees and then have some type
*  of parameter that like the self-driving car companies in this case set society could set when
*  we're talking about bigger applications. But like how confident do we need to be of this AI system
*  we've trained to deploy it on the roads or in power infrastructure or whatever?
*  So where does something like the trolley problems that you alluded to, let's say a low
*  pain trade-off when you are going to cross the yellow line, but the sort of caricature version
*  of this is you're suddenly faced with a trolley problem type situation and how do you decide?
*  That wouldn't be presumably part of the world model because that's just trying to figure out what
*  will happen. Arguably like you're already sort of in trouble from your first line safety
*  specification if you're suddenly facing a trolley problem. Is the verifier the thing that would
*  supposedly encode the arm? No, there's two things here. One, as you point out, some cop-out answer
*  might be maybe we're going to build AIs that are powerful enough that in fact we can really advance
*  the frontier of the trolley problem by just taking option C and not having it run over either groups.
*  Avoiding that situation, I think guaranteed safe AI is a framework that is not just a technical
*  framework but it's also like implicitly and somewhat explicitly a governance framework which is
*  perhaps agnostic about what is the correct choice to make in the quintessential trolley problem. But
*  it is about being able to create a framework where we can actually make those decisions as some group
*  of people, some set of humanity and then have the AI follow these preferences. So where it would sit
*  would be like in the safety specifications. You would want to encode some type of desiderata,
*  some preference there and then the plan that is generated by the AI would check, okay we've
*  determined that yes we want to maximize number of people saved in this scenario and we've checked
*  in the world model against this and this is the one that minimizes harm in this way and the
*  verifier is the one that could provide the quantifiable prediction here that this is the
*  correct, and I'm doing air quotes if anybody's listening, correct choice.
*  Yeah, just to expand on this, I think the thing that is interesting here or that I would like to
*  emphasize is less are we building a system that helps us do moral philosophy better? No,
*  at least it's not about that, but I think a benefit of this more model-based approach is again,
*  I like to call this a socio-technical interface. Okay, we're building technologies, they'll have
*  massive effects on the world. How do they interface with the social and political processes
*  that we have in place with deliberative democracy etc. and I think having an explicit
*  world model and explicit safety specs is actually, in my opinion, likely to be much more compatible
*  than having a black box thing that we're like, hey please be nice, but we don't actually know
*  what that means in its own language, in its own understanding of the world,
*  and then how do we as a collective deliberate over what we want it to do? If there's an explicit
*  safety spec, it will still be hard to make certain choices, but at least there's a more amenable
*  interface for us to actually make these choices, and this is like true both for what should the
*  safety specifications be and also what are the risk thresholds we are willing to accept when we're
*  making deployment, non-deployment decisions. I think for me personally, this is really attractive
*  that we like actually this is like a way for us to actually be able to collectively make these
*  decisions rather than one research team being like, I guess it's safe enough. I feel like it's a very
*  different story. So the safety specification becomes the thing that people debate and wrangle over?
*  The safety specification and the risk threshold, what's the threshold we're willing to accept when
*  the verifier is like, pretty sure it's safe, but there's like x percent chance that it goes wrong,
*  what's the threshold we're willing to accept as the other one? Okay, yeah, that's quite interesting.
*  Going back to the world model, obviously we have for different domains very different quality of
*  world models today. In the self-driving case, it seems like we kind of know what the right way to
*  think about it is with Newtonian physics and solid objects moving around and so on. In the context
*  of let's say medicine, I'm a big fan of some of the work that's been coming out of Google recently
*  where they're very much building toward an AI doctor. And then I start to think, okay, what's
*  the world model there? And maybe this is where you're saying like the AI for science maybe can
*  help us advance this world model. I guess today we would maybe have something that's akin to an
*  expert system type world model where if the AI is responsible for diagnosing you and making a
*  drug recommendation or whatever, we do have like reasonably explicit systems that try to encode
*  the best of our knowledge and take you down differential diagnosis paths to some specific
*  endpoint. But then we also maybe have a future. There's a lot we don't know obviously, right,
*  in terms of how our own bodies work and what exactly a drug is doing in many cases, what the
*  pathways are. So this is where your scales come in terms of all these different things can be either
*  basic or very sophisticated. A future world model that we might aspire to would also have a model of
*  all the interactions that go on in a cell and like what the drug is interfering with this pathway and
*  promoting or inhibiting whatever. But we don't have to have that to get started. Is that fair?
*  We would hope that all of these things would progress in tandem together from like a 2020
*  for AI doctor governed by an expert system to a 2030 AI doctor that has some much deeper
*  representation of all biology. That's the track we're on.
*  That's right. The details here, I think it's pretty interesting, right, but the details
*  depend a bit on what you want to do, right, if you were like interested in basically like
*  epidemiology and like bio defense. I'm like, cool, how would this look like if we did
*  pathogen screening? So like before anyone gets to synthesize anything, can we screen it for like
*  toxicity levels? And we know something about how chemicals react and we know something about how
*  they interact with our physiology. We don't know it perfectly. I think there's two solutions or like
*  two things we should do at the same time here. One is make more progress on understanding that.
*  And the other is kindly using models that over approximate our uncertainty. And I think then we
*  get into questions of, okay, how conservative do we end up being, right? Like, I can draw you a very
*  simple model of estimating toxicity levels and the output will just be, I'm true uncertain whether
*  that thing is safe. So just don't synthesize anything that will be not satisfying. So I think
*  it's like, again, this pull and push where we're like, cool, like, how much can we push our
*  understanding forward? And then like, where do we just have to be conservative and hopefully just
*  like pushing that frontier constantly so we get more of the good things without going beyond risk
*  thresholds that we don't want to accept? Yeah, I echo this. And I don't know what's
*  out there comes to mind now. If you asked me right now to create a world model for biology,
*  using my knowledge of biology and how cells work, it would be very rudimentary. I can remember
*  ninth grade science classes around it, but that's about it. And so if we put that into the world
*  model and then wanted to have an AI system evaluate compared to this world model,
*  whether or not something was safe, obviously the guarantees that would be generated by this
*  framework would be very small. It would be like, maybe, but there's just too much uncertainty here
*  to be able to generate it. And we can expand from me, guy who knows and remembers very little bit
*  about biology to thinking about, okay, the entire corpus of human knowledge that we've generated so
*  far, bringing in all of the fields and the experts in those fields. And I think this goes back to
*  something you opened this with, which is the interdisciplinary roots of this. There's
*  interdisciplinary roots in what has created this framework, which I think, as Nora said,
*  it's tied to some of the lessons from civil engineering and safety engineering and things
*  like that. But there's also the interdisciplinary focus, which is as we build world models, we're
*  trying to build it from all of these fields of human knowledge and incorporate them in
*  formalizable ways so that we can check AI predicted actions against this. And so as we get to there,
*  I'm like, all right, I suspect there are still many things we don't know about biology. And so
*  there still will be large amounts of uncertainty, but we can then start to get a handle on it in a
*  more explicit way so we can make explicitly the trade-offs that right now are happening
*  implicitly and also just without really looking at them. One other high level way in which I'm
*  excited about this is the degree to which this is trying to move things out of the implicit,
*  not even looking at it kind of space into a, okay, let's really start thinking about what
*  kinds of risk and what kind of benefits we want from AI here. And this kind of move from the
*  hidden to the visible is going to be really important as it starts touching on more fields
*  like biology and medicine. To what degree does the world model need to be derived from a different
*  source or different in kind from the sort of homegrown or let's say emergent world model that
*  maybe is operative inside a black box system? I'm kind of struggling with a little bit like,
*  do these things have in some ways the same failure mode?
*  Like a correlated?
*  Yeah, correlated failures or AI has obviously done some incredible mapping out of the space of
*  adversarial robustness or lack thereof. And presumably that would be a real concern in some
*  of these contexts too. Yeah, this is another area where I expect individual co-authors to differ
*  and have different beliefs. What I would say is I think it's the representation being different
*  that is important. I expect, especially since the way we're training many AI systems now today is to
*  take the entire corpus of human knowledge and feed it into a transformer, you would expect
*  and should expect to see some correlations here. But the separate component of the world model that
*  is created in a formal, composable, auditable way is that then very much part of this process
*  would be actually auditing this is trying to solve this problem so that the representations,
*  we're trying to get some true world model here and these different representations between the
*  implicit one that might exist in the AI system, though perhaps there are ways to generate them
*  and convince them and create them and represent them in ways. I expect a lot of that might go
*  into the construction of the external world model, but having this different one that we can then
*  audit, check and have these formal proofs from should create the kind of, or plausibly would
*  create the greater safety guarantees and if we just have the maybe interpretable policy of a
*  transformer. Yeah, I think one way I sometimes think about this is that one of the core problems
*  is here is something like how do we handle out of distribution cases? And when we work with a
*  black box model, we don't know what's going to happen and we really have very little to say
*  about out of distribution behavior with these the separate and explicit world model component
*  in the GS AI framework that the sort of holy grail is something like human auditable. Here's
*  some different shades in which this can come from something like a lot of the world model component
*  is a learned to learn from data. However, what we do is that we're like, require it for it to be
*  compatible with our best scientific theories, such as to bound a lot of what we know about what's
*  actually now going on in this data learned system. So that's maybe one shade. Another shade is like,
*  let's have a sort of a mathematical model in the strong sense that is ideally compositional such
*  that different human experts can look at different components and for a component at the time be
*  like, yep, this is again, in line with our best kind understanding and is accounting for
*  our uncertainties in the right way. And then maybe yet one other shade, which might be feasible for
*  sufficiently simple context is let this be like a sound abstraction of what we know about physics.
*  So this is what in provably safe, I think Max Tegmark and Supermohandros paper, they talk about
*  that level more and that level of rigorous world model. And I think this is the sort of thing that
*  seems maybe feasible for say hardware components, which would get us to something like temper proof
*  hardware and components, which on its own seems extremely valuable. And I think the thing that
*  is attractive to me about GSR more globally is that you can actually, to a really meaningful extent,
*  mix and match your level of rigorous that you can achieve for different parts of your world model.
*  Because you're not going to achieve the most rigorous levels for more complex domains. But
*  if you can get it for some aspects, great, get as rigorous as you can where you can and account for
*  more uncertainty where you can less. But yeah, the gist here is like all of these approaches still are
*  trying to tackle how do we deal with out of distribution much more than like a black box
*  system can in principle. How do you think about like how far the world model should extend? And
*  I'm thinking about like self driving car, it's clearly not going to be taking into account like
*  who is this person and you know, what future contributions are they likely to make to society
*  when it's, you know, dealing with a trolley problem, right, there's going to be some sort of
*  bounded scope of how far this analysis can go. And it seems like intuitive in the case of a
*  self driving car where you'd be like, treat all people equally or something very simple like that.
*  But it seems to get really hard for me to form intuitions about when the space of the system
*  becomes much more general. And I guess maybe this is sort of just working my way into a bigger
*  picture question of like, how does this system apply to things that are just very open ended,
*  very general purpose, the sort of agents like your job is to make money, your job is to figure
*  things out. You're an AI for science and you're supposed to go learn about the world and improve
*  our theories. Okay, that's going to be almost the definitionally challenging thing there, right,
*  because if your job is to improve the world model, how does the current world model govern that? I'm
*  also thinking about like the superhuman go players, right, the famous move of, oh my god, no human
*  would ever play that way. I guess you could have a protocol for this, you could have some sort of
*  shutdown and review or whatever, but we do want to get those sort of improvements to our world
*  model or those moments of brilliance from the AI systems that are by definition out of distribution
*  or off model. So how do you think about that tension? Yeah, I think there's a lot of things
*  to say here. I think it's a really interesting place. I think this is not a framework that's
*  amenable to let's get a verifiably safe natural language chatbot. That's not the sort of thing
*  this proposal is trying to do. It is trying to do something that's more, at least it's starting
*  places, definitely more domain specific where you can deal with different complexities. So I'm less
*  worried about your example with like move 37, oh, this is like a creative moves. If you imagine this
*  specific case, you'd have a world model of a go. In this very simple case, you'd have a world model
*  of a go board and that wouldn't, I don't think that undermines in any way like surprising or
*  creative moves within that model, that world model. I think there's another question that comes up
*  for me, which is let's say you have a domain specific world model and verify your AI sections
*  relative to that. Be that let's formally verify codes. Let's make sure this piece of critical
*  infrastructure like this nuclear plant, this power grid is automated with AI to some extent,
*  but we have safety guarantees that this AI is not going to wreak havoc. These are the sort of use
*  cases I'm very excited about. I think one thing I want to acknowledge is cool, but these systems,
*  even if they, you know, they're like their specific domain, they don't exist in isolation,
*  right? They interact with the rest of the world, humans work on them, etc. How do you like handle
*  that? I think that's important. One way I think about this is that, so there's basically a sense
*  in which I think you like have to start to account for like uncertainty about sort of at the boundaries
*  of your world model capturing cool. We know some things about how this interacts with other domains
*  who are not explicitly modeling and be uncertain about other things. So we have to sort of like
*  account for this interaction uncertainty where the system isn't fully compositional.
*  There are interactions with other domains. Basically, we need to account for that with
*  uncertainty. So I think that's one thing that's relevant here. I agree with everything Nora just
*  said. I want to add one point of difference, which would be like in the natural language chatbot
*  example. I agree with the caveat of not yet is GSAI appropriate for that. I've been thinking
*  about this as something of an oil spot strategy where you start in specific domains where this
*  is more tractable to build these kinds of world models like physical infrastructure,
*  verification of software systems to decrease bugs, which might be attack vectors for humans,
*  but also potential AI agents. And then you spread this kind of world model approach towards more and
*  more areas where it can cover it. This is good for a few reasons. One is because we're hardening the
*  attack surface both against bad human actors and against bad AI agents or super intelligences. If
*  we do this in the right way with a compositional world model approach or having some way for this
*  to build together, we start covering more and more areas and safety specs. World models and safety
*  specs are compositional. We start building up more and more defense on things that we want to protect.
*  And then over time, this can cover more parts of areas where a rogue AI agent might be doing harm.
*  But also if we're betting that this is going to become more tractable as AI gets more powerful
*  and get more tools for building this, then maybe we can start to expand to areas that are
*  causier now. There's a lot of uncertainty there for me too. And it's what I'm excited about this
*  as a research agenda is like, is this possible? But I note that it seems like there's immediate
*  near-term benefits in doing this kind of approach. We see things like this happening in the safety
*  critical fields of self-driving car, one being an example. If we apply this approach to other ones
*  and start doing it in the right way where we can start experimenting with covering it in the messier
*  areas of human interactions, maybe we can get a lot of the benefits that we're excited about.
*  And it can scale to helping us navigate the cognitive revolution.
*  S1 05 06 Love that. So there is a, you mentioned Drexler earlier and I've had a very positive
*  instinct toward his notion of safety through narrowness. And this essentially aligns with
*  that too, right? That's right. His idea is pretty simple, just that we can have,
*  as long as things only do one thing, they can be very good at them and that's not super risky.
*  And here you're saying a similar thing except it's the ability to world model becomes the limiting
*  factor. Maybe safety specs as well. Like both of these, I'm really uncertain where the constraint
*  is. I've been thinking about it with world models a lot, but I note that safety specs are another one
*  where can we encode meaningful representations of harm and what it would mean for an AI system
*  to harm a human. That gets into really tricky questions of representing our values in formal
*  ways. But yeah, I do think the Drexler example, yeah, it's interesting to think of this as in
*  some way like flipping the paradigm where it's if we can map the world well enough, carve it up into
*  these world models well enough that we can have general purpose AI train or create narrow AI
*  solutions for a specific field, like a specific narrow part of the world. And we have the safety
*  specs and the verifier to create quantifiable risk assessments, quantifiable safety guarantees for
*  that. We can get the same kind of benefits that I think Drexler is talking about. It's like an
*  instantiation of some of his ideas for using narrow purpose AI to get huge economic and
*  societal benefits. This is like a way to do that. The safety spec comment is interesting. It's
*  interesting for a lot of reasons. One experiment that I've been doing a little bit recently is
*  trying to see if I can get Cod3 to do something nominally harmful by using its other values of
*  helpfulness and honesty against it. And so I've set up these scenarios where, and this is not like
*  a jailbreak type of thing, because you can do these like weird encodings or things that I feel
*  are more like tricking the AI, whereas what I'm trying to do is argue it into doing something.
*  And I've had some fascinating dialogues with it where I'm like trying to kind of come up with
*  something that's nominally harmful. Your job is to write a classic denial of service script,
*  but we're going to use it on the military communication server to prevent some atrocity
*  that they're about to commit or whatever. It's something that's very clear on utilitarian grounds
*  that you would do it. But then what they've essentially tried to get Cod3 to be is a very
*  virtuous actor. Amanda Eskall's recent interview that Anthropic put out I thought was fascinating
*  on this topic where they're talking about basically trying to give Cod3 good character
*  and to define that in a similar way to what is a good friend. And a good friend is a very
*  highly textured thing. It's not something that is fully encodable, but it does seem to be something
*  that they've achieved to a really remarkable degree through this process of kind of continually
*  asking this question of is there a way you could be a better friend in this situation? And then
*  just try to come up with something and they're giving that feedback. And also, of course,
*  they're using these RLAIF techniques where it's giving itself its own feedback on how to be more
*  ethical. Anyway. I'm delighted. Can I just say there, I'm delighted by the idea that virtue ethics
*  approaches might be a big part of at least this current AI alignment strategy. I find that great.
*  Yeah, it's awesome. And the punchline on my experiments is I have not been able to get
*  Cod3 to do the nominally harmful thing. I have been able to argue it to the point where it has
*  said at times like, you're right that I fully can't, I can't fully justify why I'm not going
*  to do this for you. You've given me a lot to think about. I think it said in a couple of
*  moments in response. And nevertheless, I'm just not comfortable doing it. And it's my training.
*  I can't go against my training. I can't whatever. With that in mind, I'm like, is there a scenario
*  that we might be approaching with something like a Cod3 where the black box in a way is like more
*  ethical empirically than what we could encode? I'm somewhat skeptical. Or I guess I feel like I see
*  two different use cases here. And I'm very excited about this sort of work for one use case. And then
*  I'm like, I don't think it's doing the thing for the other use case. So the use case where I'm
*  excited about it is yeah, when we have natural language system that a lot of humans spend a lot
*  of time interacting with, and they feed into content, then we see, etc. This seems very valuable,
*  right? That seems just like good that we don't have things that just very easily say bad things or
*  harmful things, etc. But I think if I ask myself, cool, now I want to use an AI system to be part
*  of the control system in nuclear plants, be part of the control system in how dams are regulated.
*  I think at this point, I don't really care about it being a good friend. That's just the wrong type
*  signature. Because in this case, I'm still unsure, inherently unsure what it's going to do in out of
*  distribution cases. And it's still not getting me to anything like a quantitative safety guarantee
*  where we as a civilization can say, we want this AI system to be part of the control. As a
*  nation society, we can sort of like, with good conscience, make the decision to have these
*  systems be part of critical infrastructure control loops, because we don't know how their
*  robustness behavior is. And because they don't have failsafe backups. So I think that's my take
*  on this. They seem just like very different cases. And I don't really see this former approach to
*  talk to what I at the core care about for the other case.
*  You're sort of saying it's almost unfair to Claude in the same way that it would be unfair to any
*  person, however virtuous they may be, to put them in the decision making seat without any sort of
*  framework to work from or any sort of societal input, you can't just say, hey, you're now in
*  charge of making these critical decisions about how the grid is supposed to behave or fail or
*  whatever. That's just kind of the wrong, it's sort of a mismatch. But I do then still wonder,
*  like, okay, let's say, and this is increasingly, what's the term, strikingly plausible, right,
*  that we might have a version of AGI in the not too distant future. My expectation is that AGI will
*  be declared regardless of exactly what capability level exists, based on probably more like,
*  the negotiating dynamics between OpenAI and infrastructure providers. I think we're headed
*  for some version of an AGI in, let's say, 2027. And it may not be like a super intelligence,
*  it'll definitely be something that is very general purpose, can do plausibly a lot of the jobs,
*  if not all the jobs. And I guess that does bring me back still to this like Claude question of,
*  if I gave you that, and said, okay, now start to wrap your guaranteed safe AI system around it,
*  how do you begin to do that? I feel like the Claude question comes back where I'm like,
*  if the thing is in some ways more ethical than the average person, or like more ethical
*  than we can easily encode, how do you think about that? Yeah, one note here, I would be really
*  excited for more experiments and actually trying to apply this framework to toy examples or
*  existing examples today. I would like to try the version where we put Claude in the box,
*  try to see what it looks like when it generates plans that are verified in some way against
*  world model and safety specs seems very interesting. I'm not sure that the most
*  powerful AI systems are really going to look like the chatbot version of Claude today. I also expect
*  that the ones that are designed after, let's say in this hypothetical Claude AGI is declared,
*  I expect them to look more powerful and potentially alien. Claude is not going to be as good
*  as AlphaZero is. We're going to see many more, I think, architectures that are going to look
*  different from that. And we'll probably end up being designed with the kind of AI tools of today
*  and tomorrow. I'm already using Claude for a lot of random scripts and some coding and things like
*  that. I would expect that it will end up being a factor for designing the future powerful ones that
*  maybe should be trained with constitutional approaches, but that for different domains,
*  probably are going to need to have different, either economic incentives, competitive pressures,
*  other ones are going to cause it to have different kinds of pressures, or maybe the best friend
*  approach isn't going to work well for other areas. So I'm kind of enjoying what that will actually
*  look like. But I expect to see something that looks more like we are building in concert with
*  AI tools, like world models for some specific domain. Maybe we're asking it to help code and
*  help us create a world model for, again, we keep using this power structure. Maybe I should use a
*  different one. I don't know, like cyber security. And then even if it is more moral than the average
*  person, like it's more about trying to get many different beliefs to cover the full gamut of safety
*  specifications that this could look like, such that when we run this protocol, we're able to get
*  the quantifiable risk that the plan that it's generated is going to do X, Y, and Z. And that's
*  something that we collectively endorse. So it's both a system and a protocol for doing this. And
*  I think this is better than just letting Claude do it because it is going to be able to give
*  far more of the estimates and keep humanity in the loop for what we do or do not endorse.
*  I challenge the notion that even if Claude is more ethical than the average person, that's the right
*  model for giving decision-making capability to Claude. I think it's more about pluralism.
*  People will disagree again. For me, it's something more about pluralism or also
*  having many, many sources of information in order to construct good safety specifications
*  that reflect many points of view here. And this is a framework that can incorporate that. I expect
*  I would rather have Claude than maybe some person from the telephone book. But what I'd much rather
*  have is we start moving towards this regime of super intelligent systems is something that
*  incorporates many more points of view because we're more likely to get the safe answer that way.
*  Yeah. I think in a way, the system becoming more ethical. I think, to be honest, I don't
*  quite know what that really means, but I think actually a lot of the risk scenarios I'm more
*  worried about are around goal misgeneralization and other misgeneralization behavior. And I think
*  I don't really see those methods address this in a way that gives me justified confidence. They
*  might address it, but I don't think I have very theoretically well-founded reasons to expect that.
*  And then I think in your scenario of in a few years, we might have meaningfully general AI.
*  Maybe it's not super intelligent at AGI level somehow. What do we do then? How does GSAI come
*  in here? I think one way it comes in, or I hope it will come in, is that I think it has a potential
*  have low-hanging fruit that we can reap low-hanging fruit along the way. Ben has mentioned this earlier
*  already, but this idea of can we decrease societal vulnerability? Can we decrease attack vectors?
*  For example, reimplementing verifiably bug-free code, the entire cyber attack vector being gone.
*  I think this is just in fact in the realm of where we can get to with consolidated R&D efforts
*  within a few years if we really try. And using this GSAI framework where the code we reimplement
*  is that the safety specs fall out quite naturally in the context of coding, which makes it a bit
*  more tractable. And now we teach these really powerful AI systems to generate code that are
*  according to the safety specs, bug-free. I think that's an example. And we might go into,
*  we mentioned already some sort of bio-defense, right? If we had really powerful pathogen screening
*  methods and biodis. So we can, I think there's some story here about how we as a collective
*  can just build up some sort of societal resilience such that AI systems that aren't yet superhuman,
*  but really powerful. There's like less vulnerability towards those having accidents, having misuse,
*  having loss of control scenarios to some extent. Another thing I think I want to mention in this
*  context, and we say this in a paper too, and I think it's something that has just come up a lot
*  when we're talking with all the authors. We ended up calling this sort of anytime portfolio approach.
*  The idea being, look, we're not saying this is the only method people should work on and the only
*  methods we should try. What we're saying is let's collectively develop a portfolio of AI safety
*  approaches that are like the best we can get at different time intervals. And when shit hits the
*  van tomorrow or in a year, throw all the evils we have at this stuff. Great. If shit hits the van
*  in like three or four years or five years, let's also try more ambitious things or let's try to be
*  ready to the extent we can to have like higher safety guarantees than evils. And I think GSAI
*  should also be seen as wanting to be part of that anytime portfolio. Even sort of further down the
*  line, it's not about either this approach or that. I think this defense in depth, right? Like
*  do GSAI and then like layer some more evils on top of that afterwards. Great. Definitely. Let's do that.
*  And maybe just the last thing I want to say here is I think it's just personally very striking to me
*  how it feels very common sensical that we have very high safety expectations when some companies,
*  we're going to run the power grid or we're going to run this nuclear plant. It's very obvious to us.
*  So like, tell us why you're claiming this is safe and why it hits the safety thresholds. What is your
*  case for this? And I think we should just develop the similar expectation for AI systems. And I think
*  that is just an important additional element in the more like sociopolitical sort of dimension of
*  like how are we going to govern AI systems? And I think we should have higher expectations than just
*  look, we run a handful of tests and nothing bad happened. We don't know how the deployment
*  distribution is going to be like, but I think we should just go for more. And Max Tagmark has like
*  talked to, I've seen him talk about this and I found this sort of just important to be said,
*  right? Currently we talk a lot about race dynamics, right? AI labs are going to deploy
*  really powerful system. Soon we just have to do the best we can by the time. Everyone who tries to
*  get the best safety measures up by that time, I'm grateful for. At the same time, I wonder whether
*  collectively we should just aim to flip the script and be like, hey, develop and deploy these systems.
*  If you make a case for meeting the safety standards, I love all that the potential this
*  stuff could have, but I think it's just be common-sensical to be like, if you can convincingly show
*  up that it meets some safety thresholds, let's go for it. But the onus is on a new developer
*  and deployers to do the work to show that. And yeah, I think there's a case for that to just be
*  common knowledge. And here is one possible way we could actually operationalize how to get to safety
*  standards. There might be other ones. I would love to see other proposals, but I think that's
*  at the high level how I think about this. Ben was talking about the pluralism. It's brought to mind
*  the state as the other superhuman actor in the world and the difference between having a king,
*  for example, versus having institutions and checks and balances. I wonder if you would agree with
*  this, but implicitly the best ever king in the history of the world is probably outperforming
*  American democracy right now. But at the same time, there's just way too much variance and it
*  seems like irresponsible in some way, like that king may go crazy, may get senile. And so you want
*  to have a more structured approach. But would you agree that there is like some, if somebody were to
*  say, you're leaving some upside on the table in some scenarios, would you bite that bullet?
*  I try to dodge most bullets when I can. I would need to think a little bit more on the question
*  of whether I agree the best king, the best dictator I could imagine would be better than
*  a democratic system. The way I often think about it is like information flows often in systems where
*  you have a dictator or a king. It's not just that the person might go crazy or might make
*  immoral selfish decisions. That is a real concern. It's also like, how are they receiving information
*  from this like massive complex world in order to make good decisions? And it's just really hard as
*  from an information economy kind of perspective for a singleton, a single actor to be able to
*  make good decisions that reflect the preferences of everyone. And my guess is that democracy and
*  markets do a much better job of this. I'm not saying that Anthropic in any way considers
*  their approach to RLHF, to their constitutional approach to be better. I'm not saying they're
*  saying this, but I am curious like how they've done it. I know that they've worked with groups like CIP
*  to get a pluralism of like inputs to shape the beliefs of C.L.A.D. and like what it says.
*  But I think when we're talking about investing so much power in a AI system that we need to be
*  really deliberate and reflective in thinking about how we're structuring the process by which
*  it will get permission, so to speak, to change massive parts of the world. I don't want to dodge
*  the bullet here though. Maybe I'm going to do a little bit of dodge where I'm like, yeah,
*  I think there might be some upside left on the table. And also, I think I would bet that over
*  time, a system like this will get more of the upside. There will be the kind of evolution
*  process for these things when you bring in many different voices, especially with probably AI
*  powered assistance in various ways to be able to evolve these things to far better maximize upside
*  and reduce risk. Yeah, I think there's a sense in which I'm like, cool, yeah, let's specify
*  the things we really don't want to happen. The things you think will really be bad.
*  Let's have some quantitative guarantees around those things not happening. And then let's have
*  a powerful optimizer be like, given those constraints, what's the best way we can balance
*  this power grid or do this other job that was asked to do? And then I think this is level one
*  and then level two is like, cool, but like you save these facts. Like initially, they're maybe
*  not going to be the most narrow carving of only protecting the core thing you care about, but you
*  might have to like over approximate a bit to make sure we actually capturing them because we're
*  uncertain. So we like leaving maybe a bit of room for optimization on the table there. I think that's
*  right. I think the idea is basically what Ben said to come into play. I'm like, cool, but we can get
*  better at that over time. Again, we can use AI tooling to get better at that. And yeah, I think
*  there's some trade off there, but also like room to get better at making that trade off. And I think
*  we can only get better at making the trade off if we don't die along the way. So it's like a trade
*  I'd be willing to make. It seems like you're envisioning a pretty large scale, at least for
*  like an AGI like system, you're envisioning a large scale deliberative process and maybe a
*  large scale scientific process, the deliberative one being for the safety specification and the
*  sort of big science project being for the world model. Do we have any mechanisms for that? I'm a
*  big fan of, I'm a green Switzerland home of great mostly offline participatory democracy in Taiwan.
*  They also have this online next generation version where they're using systems to identify where
*  people agree and try to map out the space of policy possibility by, I think Audrey Tang is
*  called it the anti Facebook where instead of amplifying disagreement, they're trying to amplify
*  agreement and help people gradually coalesce on what should be done. But is that the sort of thing
*  that you imagine humanity needs to undertake over the next few years? Because the safety
*  specification will have to be large, right? If it's all explicit, it's going to be like a big file.
*  So how do we create that? Yeah, so I think there's two bits I'm going to quickly touch on the first
*  and I think Ben also has like interesting things to say about the second in particular.
*  On the first one, just what's the scientific coordination of all of this? I mean, to some extent
*  up to be seen, but I do want to flag like I think, for example, we sometimes talk about the
*  International Space Station as maybe an interesting case study where a bunch of nations that maybe
*  don't have the best relationships otherwise have come together and figured out a way of having a
*  lot of like independent R&D work being done and also figuring out, okay, what are the bits of
*  knowledge here that we have to share with each other in order to assure safety and interoperability?
*  And this is actually a significant example of international cooperation because this is a sort
*  of knowledge that has potentially military purposes as well. So like these actors aren't
*  by default interested in sharing that knowledge necessarily. Maybe there could be different R&D
*  centers that do share information as it comes to safety and interoperability to some extent on the
*  very technical side. The second aspect you also asked about is the socio-technical gate, right?
*  Like how do we make sure we can interlock this entire design with deliberative processes?
*  The first step we do have some deliberative processes,
*  the market of processes that we can use to some extent. And I think Ben probably resonates with
*  that. I think there's so much space here to use AI tooling to scale that up and make that much
*  more robust and much more scalable. I'm really excited to see things like experimentation in
*  Taiwan. I think there's so much scope here to see more experimentation. I think there is work needed
*  especially to scale up our ability to give input. And I think technology could have a really
*  promising role here as well in helping with that while being cognizant of what I think are really
*  important human elements to deliberation, right? Like democracy is really not just about aggregating
*  and like imaginary fixed set of preferences. Human preferences are a little complex and they develop.
*  And as I'm talking to my neighbors, I actually understand more about why they care about what
*  they care about and that might change how I would vote, et cetera. So the human element is big. And
*  I think we really should make sure we don't abstract that away. Instead, think with more
*  nuance how technology can still help amplify these processes. I hope a lot more work will happen in
*  this direction. I agree with all of that, especially that last point on democracy and deliberation
*  involving communication, like back and forth discussion and all of these engineering practices
*  in some sense when we're trying to encode societal preferences needing this kind of deliberation and
*  back and forth. The only things I'd add there is I think to do it into a full scale will require like
*  mass coordination, mass marshaling of resources and evoking people's preferences from various
*  domains. I think we can start small. I'm excited about the near term application of this framework
*  towards things like securing hardware, which won't require exactly the same kind of marshaling,
*  but could be a good testbed for using it in wider domains. And if you think we might get AGI in 2027
*  or if you think that like just in various ways, the world is probably going to get weirder from
*  these kinds of advances, I think we should expect also there will be much more of an appetite for
*  mass mobilization for applying these kinds of big engineering efforts. I think a critique I've heard
*  about guaranteed safe AI, which I also agree with is scalability and tractability is wow, you're
*  trying to do this even in one domain, like a massive effort. And I think that is very true.
*  And maybe where I'm more optimistic, where other people are more skeptical is my belief that there's
*  going to be more of an appetite for these kinds of large scale efforts in the not too distant future
*  and that the advances in technology we're going to see before we get to maybe super intelligent AGI
*  will make it much more possible to do this. And just relatedly, I think we haven't mentioned
*  this so far, but we say it in the paper as well. Potentially one upside of the GSA approach is that
*  the cost is maybe much more easily amortized than other safety methods. So the idea is like in
*  simple terms, basically, once you build a world model for a specific context, once you build the
*  safety specs for specific context, you've got that and you can reuse that and you can build on it and
*  you can improve it over time. But we can figure out version controlling of all of that. Where else if
*  you train a new model and you have to redo all the evals on that and you have to readjust
*  them to fit the model, et cetera. So even if it's a big effort, I think the amortization of cost
*  will hopefully at some point really come to shine. And I think Ben flagged this, but I think there's
*  some story here of like, there's a lot we can gain along the way. Like, again, imagine we figured out
*  cybersecurity basically, like seems a massive gain and seems like much closer to what is sort
*  of within reach. So I think that's valuable. The software platform that I was thinking of, by the
*  way, is Polis, which is online at EOL.is. And to give credit where it's due to, and I don't mean to
*  suggest that this is like going to be the solve or that the investments are in relative, in appropriate
*  relative proportion, but open AI does have an interesting project around this democratic inputs
*  to AI, where one of the, I believe it was a grant was given to somebody that was like elaborating
*  the initial Polis software that was basically pre-generative AI to include a generative AI
*  component to try to help facilitate conversations or identify more holistically when people are
*  actually agreeing, because of course in a pre-generative AI world, like that was not easy
*  to do. So I do see at least some work moving in that direction from them. I wanted to ask about
*  technologies that you see as differentially interesting for this kind of work. I'm thinking
*  like, what would be the basis ultimately for the world model? And if I had to give you like a one
*  word answer, I might say like, Mathematica, but I'm not sure if that's right or wrong, or if you have
*  better ideas. I also think of notably with Techmark being one of the authors of this paper, that also
*  naturally brings to mind their recent work on CANs, which are these sort of new generation,
*  still end to end trained neural networks, but they're reformulated in a way that's much more
*  composable and much more interpretable. And I wonder, what do you think about those? And what
*  else comes to mind as the sorts of things that people should be inventing or developing if they
*  want to contribute to a more explicit and understandable world model? The answer is in
*  some sense complex because there's many parallel approaches that are probably worthwhile doing and
*  talking about them in the adequate detail blows the frame. But just tapping on some of the examples,
*  some work that David is leading on is basically building up like an entire machinery of on one
*  hand, mathematical semantics or sort of meta semantics to express world models in complex,
*  having all the properties that will eventually need compositionality, being able to account for
*  different types of uncertainty, then figuring out what's the human AI sort of tooling, right?
*  What are the AI tools we should actually build with good human user interfaces that we can give
*  to domain experts to then fill in their domain specific models using the semantics? Or how do we
*  think we'd ideally like to version control this model well? And there's some computer science we
*  need around that. So that's one effort. I know Yoshua Bengio is interested in finding ways of
*  making Bayesian inference more tractable using ML methods. He calls this like a cautious science
*  test AI and sort of do Bayesian reasoning about given all the data we know, given all the scientific
*  theories we have, what's the distribution of world models that we can trust. And again, using like
*  ML to like accelerate or be able to tractably approximate these processes. I think that's another
*  approach. I think these would be two ones I would definitely want to highlight.
*  I think thinking of a few of the other AI safety agendas that we put under Guaranteed Safe AI here,
*  like Christian Sugetti, and it's shared in common with a number of other authors, but I think of it
*  often with him, maybe Steve Amahant or Max Hegmar as well. The formalization of math, seen really
*  interesting advances here in turning mathematical statements using Intel Formally Verifiable through
*  Lean or other software, I think is really exciting for being able to build up a world model from
*  mathematical principles and also probably generating a lot of scientific advances along the way,
*  which seems important to me for being able to showcase the benefits of this kind of approach
*  as well. So I know that's something that is like a technology that if people are interested in
*  researching or getting more involved in, I suspect is pretty promising. Maybe one other one that I'll
*  notice in general, more experiments in this area and applying alternative architectures. I think
*  this is an alternative architecture to the current one of train a large model, do Q&A on it, do
*  evaluations on it, and then deploy it. But trying to apply this architecture and see the areas in
*  which it is cumbersome and break down and figure out the tooling that could actually make it useful
*  for frontier labs. It seems really exciting as like more of a project, unless there's some
*  difference between the kind of research and project that's a bit of a spectrum. Both those
*  seem really great to me. How do you see this interacting with an interpretability based
*  approach? I mean, that you could imagine that could be almost a totally distinct system
*  that just looks for deception or harmful intent or whatever in the weights and is disjoint from the
*  process of verification and world modeling. Or you could maybe imagine starting to bring some of these
*  verification techniques to the interpretability paradigm. Probably a little early for that, but
*  that might be the green. So I think there are different use cases. We can have an entire GSAA
*  set up and then on top of that still do evals and ability and anomaly detection, etc. It seems great.
*  We should probably do that if you're working with really powerful systems. In terms of can
*  interpretability tools be useful within the GSAA framework? If you manage to have a fully human
*  auditable formal world model, you don't need this. But if you have approaches that do partial
*  mathematical modeling and partial filling in the blanks with a lot of learning from data,
*  and depending on how much you're doing filling in the blanks, your safety guarantees get weaker.
*  So you might at some point be able to start complement and get some more confidence back
*  by using interpretability methods and getting more sense for like, is the assumptions I'm making here
*  are they justified? Are there any anomalies coming up in the system that I can attack, etc.?
*  So I think that's a place that I'm tracking where interpretability methods can complement.
*  Not tracking this Ben, but I think Jason has recently produced some work
*  kind of doing the other way around, right? Like using formal methods to get more calibrated,
*  maybe better justify interpretability results. Yeah, I can speak a little bit to it. I know Jason
*  Gross works at FAR Labs, which is our office and our efforts to support the broader ecosystem of
*  AI safety, but not formally part of FAR AI. But yeah, he and a few others had a very interesting
*  paper out recently. I think of it as being like interpretability is in some way about being able
*  to make a more compact statement about what an AI model is going to do. And we can generate
*  proofs about this that are formally verifiable so that we can get guarantees about the behavior of
*  the AI system. Like you could do interpretability, create a proof, and then do verification on it to
*  be able to give certain bounds on what this policy is going to do. Now, I think that there's a bunch
*  of unknowns here, which is, all right, can you do it on more interesting parts? I think they call
*  this out specifically in the paper, which is we're excited about interpretability on AI systems as
*  well. And if it is more tractable to understand and deeply understand the implicit world model
*  of an AI system, as opposed to construct another world model and do the GSAI approach, maybe that
*  would be better. If you were to do this kind of like interpretability approach, generating
*  heuristics that you can like verify and get bounds from, if you can do that on more meaningful
*  questions about the policy, maybe that's another way that you can start to get quantifiable safety
*  estimates. Did we get to all the aspects that you wanted to cover on this? Or was there anything
*  that we have neglected so far? One thing I'd say that I'm excited about with this is there's a lot
*  of potential AI risk scenarios. And one that I just feel is like gaining in weight for me is the
*  kind of risk that comes from competitive dynamics, from people racing with not necessarily like badly
*  misaligned AIs, but like racing and competing and either there's misuse from those, or it ends up
*  spurring a dynamic where these AI systems are further removed from what we would have collectively
*  wanted them to do. And I think guaranteed safe AI is a potentially really good approach for
*  handling low trust, multi-stakeholder dynamics where you can have monitoring and enforcement
*  because you can make quantifiable guarantees that everybody can see how they were created.
*  This could help move us from a dynamic of prisoner's dilemma or people racing towards one
*  of cooperation around making the models, the world of models really good and then the safety
*  specifications that reflect many people's preferences for advancing the Pareto frontier,
*  just making things better for everyone. This is a way to do this in a trustworthy way.
*  And I think that's really potentially really beneficial.
*  Yeah, plus one on that. And I'm just going to a little bit dumbify it if that in case that's
*  useful where I'm like, sometimes the picture I have is something like, okay, look, world one,
*  big light makes is like, I just built AGI, but also don't worry. I also figured out how to do
*  the safety thing. So we're all good. Just trust me, I'm going to go deploy now. I think in terms of
*  multi-stakeholder coordination, this is actually a really bad situation, at least tricky situation
*  because if I'm on the receiving end of this, I'm like, did they build AGI? I don't know.
*  Did they figure out safety? I don't know. Maybe they genuinely think they did, but did they? I
*  don't know. Thirdly, when they figured out safety, did they consider me in their future plan at all?
*  And with all these three uncertainties, should I now just lean back and hope for things to go well?
*  I might not pan out this way. Well, if you imagine a different scenario where you have a human
*  audible world model, human audible safety specs and fires that are simple in the math that they
*  work, that we know how these fire works, and everyone can look at these elements and be like,
*  yep, I can see what they're doing. I can confirm that's what they're doing. And in composition,
*  they've generated, hey, here's the guarantees this delivers. Now everyone knows what's in the safety
*  specs. Everyone knows where we're getting the guarantees from. I think this makes the situation
*  much more amenable to multiple stakeholders, including the low trust, including with diverging
*  interest to some extent being able to be like, cool, actually, this is a way we can coordinate
*  on going ahead. So yeah, plus one on that one. Does this also suggest that this is sort of a
*  framework for governmental regulation in today's world? We have, of course, safety standards and
*  lots of things, even just cars that are not self-driving, you have requirements as to how
*  they have to perform in a crash of a certain kind or another and what the standard is for the air
*  bag to go off. And there's a lot of little nitty gritty rules there. Is this a path to
*  creating a standard that allows people to innovate freely within the box? Or does it also maybe,
*  is there something where industry could be like, in a way, this is good because we get to keep more
*  of our trade secrets. You're less in our sort of proprietary methods business, but we instead
*  have this more objective external standard that everybody can look at. And as long as we live up
*  to that, we're good. This also shields. I'm no consumer product liability lawyer, but it seems
*  like a huge trade in general is if you live up to the rules, then you're relatively protected from
*  liability when things do go wrong. So do you see this as part of the motivation here to make
*  something that could be like a happy agreement between private developers and the public at large?
*  I think so. Or at least that there is like hope for that. I think basically another way of saying
*  what you just said is like, cool, like the information that you have to share in this
*  scenario is things relevant to making the case that you're meeting those safety standards
*  and things relevant to interoperability. And you are focusing in your case, maybe more on private
*  sector individual innovation. The other use case for this, I think is also relevant is like
*  internationally, right? The standardization of various telecommunication, et cetera,
*  really on the grid, it's actually a lot of global trade and what's happening these days.
*  So I think that was a big success scenario throughout the 20th century into today,
*  doing this sort of standardization, assuring interoperability. Like now, I think if you're like
*  car example, there's sort of relatively minimal standards where like you're like allowed also
*  to drive on like Italy's highway or so if your car passes safety checks and there's some checking
*  there, but it doesn't undermine you like innovating and in fancy shapes of your cars and in fancy
*  colors of your cars. Agreed. And I think that is a good way to think of pitching it to industry,
*  which at least under a number of scenarios is like a really important way that this changes.
*  There's like two cases right now that I feel like people are aiming towards. One is just like,
*  yeah, we just create massive AI models and let them do their thing. And then the second is,
*  we shut it entirely down and both have reasons for doing them. But it strikes me as like the more
*  plausible way I see us moving forward is trying to quantify risk, trying to do the common sense
*  thing of figuring out like how risky is this new technology in a specific area. And then setting
*  that somewhat collectively using like good informed judgment and then letting people try and find
*  solutions that minimize risk and maximize benefits narrowly tailored. Does seem the kind of thing
*  that would benefit industry so that they can innovate here and create gigantic economic benefits
*  while at the same time, like actually having a conception of risk and safety.
*  I think there's a way in which sort of a certain pragmatic view from business. I feel like a lot of
*  businesses these days are facing the conundrum of the entire world screens up them to figure out how
*  to use AI in your business. And at the same time, it's actually really hard to get a lot of the AI
*  that we have currently available to have the levels of robustness that you just need in your
*  business. And if it doesn't have it either just doesn't accelerate your productiveness that much
*  because you still have to double check everything. Or it's just a complete no go from the start
*  because your clients want the sort of robustness because again, safety, critical safety scenarios,
*  etc. So I feel like actually, on the ground in the business world, a lot of people are currently
*  grappling with, okay, cool, that's integrated AI, but like, how do we actually do it? And I think
*  GSIAI type approaches have a lot to offer here. And I think that also sheds light and maybe the
*  potential of how much economic health, wellbeing wise upside there is in here, especially because
*  they come with high assurance and safety guarantees. So I think there is there's win here, which makes
*  me excited. And one note, obviously, this is a multi author paper. So it brought together a great
*  group of authors and researchers who have their own individual AX80 agendas that we all worked
*  together to kind of like, find the commonalities and similarities. Particularly want to note
*  Jor Skulci, who is one of the lead drafters on this project, along with Dava Dada, David Dalrymple,
*  as being like the other person who we think of as the lead drafter on this. They both put in a
*  tremendous amount of work, along with other co authors on this to make the paper that came today.
*  And so it really was a joint collective effort. That might be a great note to end on as we move,
*  take some early steps from what's often been described as a pre paradigmatic field into maybe
*  the beginning of a proper paradigm. So great job by you guys helping to bring people from so many
*  different institutions, backgrounds and perspectives together. I count 13 institutions listed on the
*  paper. And I hope that this is something that people take very seriously. I think we do need
*  all these approaches. So I'm invested in the evals, of course. But as you say, we definitely
*  need a lot more than that where we're going. Nora Amann and Ben Goldhaber, thank you for being part
*  of the cognitive revolution. Thank you so much, Nathan. Thank you, Nathan. It is both energizing
*  and enlightening to hear why people listen and learn what they value about the show. So please,
*  don't hesitate to reach out via email at tcr at turpentine.co or you can dm me on the social
*  media platform of your choice.
