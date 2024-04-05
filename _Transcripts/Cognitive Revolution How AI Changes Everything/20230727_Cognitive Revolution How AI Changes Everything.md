---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 7987s
Video Keywords: []
Video Views: 945
Video Rating: None
---

# Demystifying LLMs with Mechanistic Interpretability Researcher Arthur Conmy
**Cognitive Revolution "How AI Changes Everything":** [July 27, 2023](https://www.youtube.com/watch?v=Y5Pzch7_8MQ)
*  a really ambitious goal of interpretability where the whole architecture of the forward
*  pass can be understood to a human, or at least these high-level concepts like the whole
*  routing to a particular expert has some meaning to humans. And I think it's possible that we can
*  get to this stage with mechanistic interpretability. But I think it's worth noting that even if this
*  fails pretty badly, it's still possible for the interpretability of narrow tasks, like an
*  understanding of the dangerous capabilities, so we can at least remove those dangerous capabilities,
*  even if we don't have an understanding of all capabilities of the model.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas, and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Thornburg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm excited to take a deep dive into
*  mechanistic interpretability with Arthur Konmy. Looking back on the show over the last few months,
*  I realized that I'd mentioned the topic of mechanistic interpretability many times,
*  repeatedly highlighted it as one of the most promising paths to long-term safety,
*  and shared a few of the canonical results that most inform my AI worldview. But we've never
*  really got into much detail about how mechanistic interpretability work is actually performed.
*  Today we're getting into those details. Now, this is an advanced topic, so while we definitely take
*  our time to explain the key concepts in the simplest possible terms, we do assume throughout
*  that you understand the differences between related concepts like parameters and activations,
*  or attention heads and MLP blocks. If those distinctions aren't already clear, I might suggest
*  watching part one of my AI scouting report first, as the fundamentals that I present there
*  really are meant as a foundation for a conversation like this one. Beyond that foundation,
*  Arthur really is the perfect person to guide us, as he's just published a new paper and software
*  library that aimed to accelerate mechanistic interpretability work by automating the most
*  cumbersome and tedious parts of the typical research workflow. Beginning with the core
*  questions that mechanistic interpretability seeks to answer, and describing the conceptual basis and
*  experimental setups that are most commonly used, Arthur does a great job, both in the paper and in
*  this conversation, of providing clear, even intuitive, explanations for how researchers
*  are starting to pry open the black box that our large language models. It's really fascinating
*  to learn how sub-circuits are discovered within transformers, and to see the effective, but often
*  quite alien, problem-solving strategies that models learn. I'm also really excited by Arthur's
*  vision for how mechanistic interpretability work could one day allow us to inspect powerful AI
*  systems for the emergence of concerning capabilities, even during the training process.
*  While we're a super long way from being able to do that reliably today,
*  such mastery of how AI systems work would be an outstanding development for safety, reliability,
*  and performance. This is an unusually accessible introduction to mechanistic interpretability
*  from a practitioner who is among the best in the field. I learned a ton, and I think you will too,
*  so I hope you enjoy my conversation with Arthur Convy. Arthur Convy, welcome to the Cognitive
*  Revolution. Thanks, Nathan. Good to see you. Yeah, I'm super excited about this. So,
*  boy, folks who've listened to this show for a little bit have heard me certainly mention the
*  concept of mechanistic interpretability a few times, and I have mentioned that I'm excited about
*  it as a research direction, and it seems like one of the most promising paths to long-term safety
*  with AI systems is to understand them in a deeper way, in a more penetrating way than we do
*  right now. But we've not really got into the details too much, other than looking at a few
*  headline results of grokking and a few seminal things that give people a sense that progress
*  is happening here. This, for many, I think will still be their first real deep dive into
*  mechanistic interpretability, so I'm excited to get into all that with you.
*  Maybe for starters, could you just tell us how you think about mechanistic interpretability?
*  What is it? What are the goals? What attracts you to it, perhaps, as well?
*  So, mechanistic interpretability is the reverse engineering of the learned algorithms that
*  neural networks implement into human understandable concepts. So, the idea here is that neural
*  networks, like machine learning models, are an algorithm which turns inputs into outputs,
*  but it's very opaque how exactly that model is turning inputs into outputs.
*  In mechanistic interpretability, we aim to explain how that happens in terms of the internal
*  components of that model in a human understandable way. So, not nearly that this matrix is multiplied
*  by this matrix and produces the outputs, but no, here are the high-level variables the model's
*  using internally to produce outputs from inputs. So, I see my research goal as is to improve the
*  world understanding of how neural networks operate by, for example, explaining more of the
*  behaviors of neural network models in terms of their internal components.
*  I think my background, which got me into mechanistic interpretability, was probably studying
*  mathematics in my undergraduate degree, where almost the whole subject is about actually
*  understanding how things happen. I was drawn to this area in machine learning because machine
*  learning is, in general, not a field where the understanding of how algorithms are operating
*  is the way that further techniques are made. It's just like a blind optimization procedure,
*  but it doesn't have to be that way. My motivation is to continue to make machine learning and the
*  algorithms learned by neural networks more understandable in terms of human concepts.
*  There's a few levels to this, I suppose, in terms of how much we could achieve. I think we'll
*  different results get to different stages of this depth of understanding, let's say.
*  The way I think about it, and tell me if you would present this a little differently, is
*  first, you might just ask, how is it that the models are doing what they do? Can we even just
*  describe how information is being processed in any way that's more enlightening than just everything
*  kind of connects to everything and we don't really know? If I then went up a level, I could say,
*  okay, well, I could just describe that and we're going to get into the work that you've done to
*  help kind of zero in on the part of the network that seems to be most important for a given task.
*  But then I could go beyond that and I could say, well, okay, I can see that these are the parts
*  that are lighting up, but why does that work? What is it actually doing? Is there a way for me to
*  understand that in any sort of intuitive way? Then I guess maybe a third level would be like,
*  to what degree can we understand or determine if the things that it has learned, the strategies
*  that it has learned are in fact general and constitute some meaningful understanding?
*  Or are they sort of still in the stochastic paradigm of, yeah, you may get decent results
*  on things that look like the training data, but there's not really a deeper understanding here.
*  And I guess further too, you might say, well, is there anything we can do to encourage actual
*  understanding or maybe discourage, I guess, depending on exactly what you're looking for
*  from your systems? How do you think about those layers? Would you adjust that
*  mental organization of this? Yeah, definitely. I agree with the first two layers, Nathan,
*  you proposed that. And think about those two a lot. But to me, mechanistic interpretability
*  has just two steps, essentially. That firstly, you find what the important subcomponents
*  of this huge neural network are that matter. And then having established this subset that is
*  important, you can then ask, well, what is the meaning of that subset? Which I think maps onto
*  your two levels very well. And I think describes a bunch of research that has already been done.
*  I'm sure we'll get into that further. And yeah, I think that then the third level is one of many
*  sort of potential use cases, essentially, of mechanistic interpretability, where this could
*  enable us to answer the questions of are these models doing reasoning or modeling humans that
*  they're interacting with? Or is it just a wad of heuristics and statistics that is not doing
*  anything intelligent beneath just a ton of rote-based rules? And we don't know the answer to
*  that question at this point in time. Yeah, the stochastic parrot's hypothesis is still a hypothesis
*  that models are just parroting nonsense, but it looks correct to us because we haven't probed
*  deep enough. No one does probe deep enough with their evaluations. And if we can actually understand
*  the algorithm these models are implementing, we can have a yes or no answer to the question of
*  whether they're just in general surface-level heuristics or they're actual algorithms which go
*  beyond just normal heuristics. In my general sense, Kirk, if you would just agree with this,
*  but my general sense is that it's kind of always both and we just don't really know
*  which is the case for any given task and model that we might want to consider. It seems to me
*  that, even not always both, but certainly you get to a certain level of scale, there seems to be some
*  generality that starts to appear, which even if we haven't proven it yet, we've seen enough
*  examples of meaningful grokking to believe that more is happening. But we just don't know for any
*  particular task under consideration at the start, has this been understood or is it still
*  just statistical correlation that kind of appears to be making sense? Is that your understanding too?
*  Yeah, I think that it's pretty clear that there are cases when models are reasoning or performing
*  the correct algorithm to produce certain completions to problems. You can think of
*  basic math problems or basic reasoning problems that have been turned into benchmarks and then
*  destroyed by various large language models as affirmative tests. There are some cases of
*  reasoning going on. But after the frontier of capabilities where you suddenly have the next
*  size of model that can do something that previous models couldn't do, such as GPT-4 surprising many
*  people with its coding abilities, it's unclear whether this is at that scale when the ability
*  first emerges, actually just pattern matching that's worked in enough cases to convince humans,
*  or there's something deeper going on where at some level you reach some understanding of code.
*  I think this is quite an important distinction, whether frontier capabilities are incredibly
*  surface level when they first emerge or whether they can be learned in generality straight away.
*  Because the emergence of capabilities and the unpredictability of new things that models can do
*  is quite important for the future risks of systems. Because if we can't predict what's going to come,
*  then we would at least like to know that there's hopefully a surface level heuristic maybe,
*  than like a completely general solution to something that we thought was very difficult.
*  Because this could cause quite a lot of instability and unpredictability when we
*  talk deploy systems. So like what a really getting quite into like the high level motivation for why
*  like these issues are quite serious. But yes, I agree that there's a both surface level heuristics
*  and general like general reasoning ability in these models. And I think that the problem is
*  like distinguishing the two particularly at the frontier, if that makes sense.
*  Totally. I've said, probably in a few episodes at this point that for me, the most important
*  sentence in the GPT-4 technical report is the it's quite a short one, certain capabilities
*  remain hard to predict. And there they show the reversal of what had been an inverse scaling law
*  where I'm sure you're familiar with this bigger models had been more susceptible to hindsight
*  neglect or hindsight bias sort of reasoning fallacies until GPT-4 when suddenly sure looks
*  like that has been grok. I don't think it's been certain hasn't been proven in public.
*  I don't know what they know internally. But to go from everything's getting worse as the
*  models get bigger to all of a sudden GPT-4 is perfect, definitely suggests that there are some
*  kind of phase changes that happen on the frontier and the fact that even OpenAI for all the smooth
*  curves that they can plot can't really predict on any given task whether it's going to be
*  understood or not. That definitely creates a lot of unpredictability as you said. So
*  let's get back a little later to what we might do to encourage things to be more understandable
*  from the start. And for now, just dive into what you have done to help us make sense of the models
*  that we do have at present. So I love the way that you approach this paper and I also enjoy the
*  clever name the ACDC, which you give to the algorithm. I think first, it's really useful
*  just to describe the general process that one takes to mechanistic interpretability. I think
*  you do a beautiful job of that in the paper. And this will be the first time that folks have heard
*  this level of detail. So for starters, how about just kind of giving us this overview of the
*  workflow that mechanistic interpretability researchers tend to pursue? We'll get into each
*  of the three parts in more detail. And then of course, get into especially the part that
*  you've automated. Cool. Yeah, that sounds great. Hey, we'll continue our interview in a moment
*  after a word from our sponsors. Hey everybody, if you're a business owner or founder like me,
*  you'll want to know more about our sponsor NetSuite. NetSuite provides financial software
*  for all your businesses. Whether you're looking for an ERP tool or accounting software, NetSuite
*  gives you the visibility and control you need to make better decisions faster. And for the first
*  time in NetSuite's 25 years as the number one cloud financial system, you can defer payments of a full
*  NetSuite implementation for six months. That's no payment and no interest for six months. And you
*  can take advantage of the special financing offered today. NetSuite is number one because
*  they give your business everything you need in real time, all in one place to reduce manual
*  processes, boost efficiency, build forecasts, and increase productivity across every department.
*  More than 36,000 companies have already upgraded to NetSuite, gaining visibility and control over
*  their financials, inventory, HR, e-commerce, and more. If you've been checking out NetSuite
*  already, then you know this deal is unprecedented. No interest, no payments. So take advantage of
*  the special financing offer with our promo code at netsuite.com slash cognitive. netsuite.com slash
*  cognitive to get the visibility and control your business needs to weather any storm. That is
*  netsuite.com slash cognitive. Omniki uses generative AI to enable you to launch hundreds of thousands of
*  ad iterations that actually work, customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it too. Use Cogrev to get
*  a 10% discount. So the way we set up the three steps of the mechanistic interpretability workflow
*  just to prepare advance are firstly choosing a behavior or a task that a neural network can
*  perform, such as we discussed, the ability to predict modular addition in language model
*  trains to get the correct answer to modular addition sounds. And then secondly, after picking
*  this behavior, we then define the scope of the interpretation that we're aiming to explain.
*  So this means that sometimes it's possible to explain the whole computation that the model
*  performs in terms of individual neurons, for example, which communicate between different
*  layers of your model. But this is in general pretty difficult since there are a huge number of neurons
*  and computation is not often localized to individual neurons. So other researchers
*  in projects I've worked on have instead looked at the attention heads and MLPs of transformers.
*  So an MLP consists of many neurons, but you can consider it as just one component.
*  And so a researcher who might maybe thinks it's a bit too ambitious to explain how a task is
*  performed in terms of the individual neurons may wish to explain the task in terms of the MLPs,
*  the whole MLPs that are important in the model. Maybe it's just a subset of them.
*  So then that's the first two steps. And then the third step is to perform a bunch of intervention
*  experiments that find those exact attention heads, MLPs or neurons that are important for
*  that task at hand. And this is generally the most laborious from the human side part of the process.
*  And hence why we thought it was a good fit for trying to automate in terms of the circuit
*  discovery process. So yeah, those are the three steps. It's a high level overview.
*  I'm happy to get into that if you'd like, Nathan, or if there are any questions
*  that seem to stick out to you. Happy to discuss.
*  Yeah, I definitely want to get into each one in more detail. So, but just to kind of echo it back
*  to you. First is identifying a behavior of interest. I mean, let me just get into the details now. So
*  I'm struck by, there's a lot of trade-offs here, right? You've got, first of all, what models do
*  you have access to? What models can you kind of actually manage to scale your approach up to
*  handling? What are those models capable of? So those are kind of some very practical constraints.
*  In general, people seem to be doing this work at this stage on relatively small models. And those
*  models are only capable of relatively modest tasks, certainly compared to the likes of GPT-4 and
*  CLAWD-2. So maybe just give us a little bit more insight into how you choose what models you're
*  working with and how you identify behaviors that you think are actually particularly worth this
*  depth of investigation. Yeah, sure. That's a good question about the first step of what do you mean
*  by picking a task or the criteria to choose here. And I think that some of the criteria which feel
*  important to me are localization of a task, such as something which can be thought about on its own
*  is distinct from the rest of the natural language computation. So one of the tasks we considered
*  was a task where a model's able to predict a future year in a given century from a previous
*  year in that century. And in this case, this is quite localized to individual token completions
*  that are about particular years that have been incremented from the previous year.
*  Whereas tasks that are somewhat more vaguely defined, such as the model produced a non-toxic
*  response or a non-harmful response, are often really open-ended and difficult to pin down.
*  And so it's generally harder to interpret tasks that have quite a vague definition and can be
*  completed with a huge number of different tokens, for example, because this is just going to be
*  distributed all through the network and be quite difficult to pin down. So that's one consideration
*  on task choice. That's mostly a question of tractability, like how tractable is it to actually
*  be able to complete this interpretability project. And you could often narrow down wide concepts into
*  smaller ones to get around that issue. And then the second consideration would be something like,
*  is this task relevant to something that bigger models can do and is confusing from the relevance
*  of the actual capabilities of these models? So as examples of this, a lot of people are interested
*  in models' ability to recall facts, for example, to produce completions to sentences that require
*  knowing something about the objects in that sentence. And this is important because we'd
*  like to know if we train our language models on this much data and this person has mentioned this
*  many times, for example, will the model be able to store that information? Will it know that information
*  and stuff like that? And so this turns out to be quite an interesting problem because it certainly
*  matters for models we deploy later. And there are lots of things that natural language models do
*  because just the training data distribution is extremely diverse. And so selecting something
*  which is useful as models get bigger is another important consideration. So yeah, that's the two
*  considerations for choosing a task. That's really interesting. So just on the first point about
*  kind of locality, it strikes me that there's probably at least a rough mapping onto or maybe
*  from tasks that we ourselves sort of have some ability to describe how we're doing and tasks
*  that we might hope would be tractable. For example, a toxic or nontoxic response. If I look at my own
*  behavior, I'm like, not always that super clear as to why I generated a toxic or nontoxic response.
*  Whereas, I think I have a clearer sense of how I'm thinking about something like, for this example
*  you gave about the years, a sample prompt from the paper, the war lasted from 1517 to 15. And then
*  it's up to the language model to complete that. Introspectively, it feels like I have a better
*  sense for what I'm doing. How much does that kind of introspective decomposition of tasks
*  feed into your task selection? Not to say it should or shouldn't, but I'm curious.
*  I think that we always would be choosing tasks that involve something that humans know how to
*  do, because then we can put metrics and measures of how much the model does them, since we can
*  figure out how we do them. But I think the interesting point here is that models often
*  do things in very different ways to humans. We found several examples of this in the circuits
*  we discovered, where when models are choosing the correct name to put on the end of a sentence,
*  they often aggregate all the names together and then remove the deleted names, which is not how
*  humans reason about names at all. So I think it's the case that we always choose tasks that, as
*  humans, we can understand how we perform them, at least at this point in time. But we don't
*  always observe that the language models perform these tasks in the same way as humans at all.
*  Yeah, certainly it's always important to keep in mind the profound differences between the way that
*  we do things and the way that the models are often, seemingly in fact, learning to do them.
*  Okay, well, there'll be more opportunity, I think, to unpack some of these examples
*  and see how this plays out. When you're putting together a data set, I also understand that it's
*  important to have contrasting examples where you want to set up a situation where you can look at
*  the difference between a sample that's doing or an example completion that's doing what you want it
*  to do and one that's not doing it. Can you give us a little bit more intuition for that? Is it like,
*  for the year example, would the contrasting be like doing it right and doing it wrong,
*  like getting the wrong answer from 1517 to 1515, something nonsensical? Is that the kind of like
*  super sharp contrast? Or is it just like other tasks that are kind of not this task?
*  Cool. Yeah, that's a great question. So when we define these tasks, as we can sort of explore in
*  our paper, a crucial component of this is the selection of like two data sets. And the first
*  one is unsurprisingly, a bunch of like prompts or inputs to it like a model, which have the behavior
*  identified. But you also do need like a contrasting set, as Nathan you've just mentioned, that are
*  crucial to find the components of the model that actually do your original task. And why do we do
*  this? Why do we need like comparison of two different parts? This is to do with how in the
*  language model computation, it's not possible to just find the like subsets of the model,
*  which does your one task, and just completely ignore the rest of the model. Because that is
*  still going to need to do some computation in the forward pass when you're running the model
*  to be able to produce the correct completion. Like you can't just like, take your model in
*  your like programming language and just say like, no, I don't want that component. Like just like
*  remove that. You have to be like somewhat more clever. And so the default path that's taken in
*  most machine learning research is pruning. And what like pruning does is set certain weights in
*  the network to zero to like remove like the effect of that component of the model. So if it's like a
*  neuron, it will now never fire if it's like weighted zero. But this is actually quite problematic,
*  because the model in like training and normal like runs is not used to seeing just zeros from like a
*  huge number of components in its like forward pass. It's used to seeing like different values
*  which fall on some distribution. And then sometimes like something fires like slightly more than usual,
*  let's say, and that will then cause the model to produce like the completion it does in the current
*  setting. And so this is a quite like long like point. But then the crucial like finishing touch
*  here is that if you have a contrasting set of examples, you're able to just set the like models
*  internal activations to the activations on the like corrupted like data set. And this doesn't
*  have the problem that a lot of machine learning research has, that it just sets to zero and the
*  model is now like essentially confused as to what it's like doing, because it's never seen zeros
*  before. Instead, the model is just like counterfactually seen different outputs from
*  like earlier components. So that's like the intuition for needing this like contrasting
*  set of examples. And in the case of the like years, I think where we're like predicting it,
*  the war lasted from 1517 to 15. And this war example is from a great paper by Michael Hanna
*  and fellow authors, where they find how GPT-2 can do greater than if you're interested. This then
*  has a like a baseline example that those authors chose, where I believe it says just the war lasted
*  from 1500 to and here like literally any completion can work like 1500 to 1500, 1500 to 1500 and one
*  1500 to 1599. And so the model doesn't like need to do this like greater than operation to find out
*  the future years. And so this serves as a perfect like baseline, because now when you compare your
*  two like data sets, the model components that are important on the like greater than 1517 to some
*  future year data sets, but aren't important on the baseline data set 1500 to literally any like year
*  in the 1500s, then are like actually the model components doing that greater than computation.
*  So I guess the key point here is that greater than is implicitly an operation which is not just the
*  super general algorithm of like just a year. So our technique like this like formalism of the
*  mechanistic interpretability workflow is able to like specifically zoom into like the task at hand,
*  which is about predicting a greater year rather than just like any year at all. So yeah, I hope
*  that provides like a bit of a longer story for why like the baseline for like mechanistic interpretability
*  is quite important. And it's not sufficient to just have like zeros as a baseline.
*  Yeah, cool. Okay. So then that's in anticipation. So just to, you know, kind of send some of that
*  back to you, hopefully to make sure everybody listening along is with us. What I'm understanding
*  is that in anticipation of the part three, where you're going to be, you know, systematically
*  eliminating parts of the network to figure out which parts matter most,
*  it has been found, and you have an intuition for it, but I assume to start it as an empirical finding,
*  as most do, that just a hard elimination of different parts of the network where we literally
*  take them straight to zero is in fact, kind of too far outside of what the network has learned to
*  expect and learn to process. And so it creates these other problems. And then you actually can get
*  better results by replacing instead of actually deleting outright, you are replacing whatever
*  values with something that's like representative and kind of, you know, normal in some sense for
*  the model. But to do that, that's where you need these kind of baseline examples to have a sense
*  for what that normal would be in this case. Yeah, that's exactly right. So I think, yeah, key,
*  like intuition pump that like I have for why this, why we'd like to avoid setting things to zeros
*  is that possibly the models components have like an implicit bias term, essentially in machine
*  learning, that is not present in the literal bias parameters. But the weight matrix just on average,
*  for example, is like outputting a value in some particular range. And it's unlikely that this
*  range will be zeros overall. And so it's super useful to like use a baseline rather than use
*  just the zeros. And this was like, yeah, it's not my primary research contribution. But when I was
*  at a Redwood research, who did like mechanistic interpretability research, some of their research
*  output provided evidence for this claim that it's not a great idea to set to like zero activations,
*  but instead, like, yeah, corrupting your model with activations from a different data set example,
*  maybe more representative of like the models computation. I'm as I think I mentioned always
*  kind of very careful about analogies. But again, just for intuition sake, if you're trying to do
*  something like this on a human, and you literally just removed part of their brain entirely, then
*  you might imagine that like other parts of the brain would be quite disturbed by that and be
*  like, hey, wait a second, we're expecting signal from here, and we're not getting it. And the whole
*  system can kind of, you know, go haywire. So instead of literally, I mean, that's where you
*  get into like literal lobotomies, I suppose, instead of like actually, you know, totally disabling
*  a part of a network, you kind of say, let me just return this to sort of baseline activity,
*  so that other parts of the network aren't like, you know, disturbed, and they get something,
*  you know, along the lines of what they're, you know, accustomed to seeing.
*  Yeah, that sounds exactly right. And I definitely do think in terms of like similar analogies to
*  like interventions you'd do on humans, like sometimes because it is helpful to like,
*  choose between different like interventions you could do on models. And I agree that like the
*  zeroing intervention often is like equivalent to just like removing something in like a human body
*  or something, if we were giving an analogy to like medical interventions. And in general, this
*  like wouldn't be the way you would like treat someone, you'd rather go for like a placebo
*  of like the hormone or something they're being treated for, rather than just like removing
*  their body's ability to produce that hormone. That would be the default strategy to like treating
*  something. Okay, cool. So we're in, you know, getting close to the end of part one and
*  definitely anticipating part three, again, part one is identify behavior of interest, a data set
*  that demonstrates it and a metric to evaluate it. So let's then talk about the metric to evaluate.
*  This was one of the areas of the paper where I was a little bit confused because
*  my intuition out of the gate was just like, if I'm trying to figure out what parts of a
*  network are important to doing a certain thing, then the intuitive metric to me that I would want
*  to look at first would be like, can I, you know, do some of this neutralization or, you know,
*  patching as it's called, and basically get the same output. But you take a few different approaches,
*  where it seems like sometimes you are just kind of trying to make sure that outputs are minimally
*  changed. But other times you're looking at other kinds of metrics. So give us a little bit more
*  about how you think about identifying metrics and why there are different metrics here in the first
*  place. Sure. Yeah, I think that metrics are mostly like a question of the practitioners'
*  choice in selecting a task. So to give an example, in the case of the war sentences, so again,
*  the language models complete sentences like the war lasted from 1517 to 15, yada yada.
*  The language model, we deem to be correct when it answers like 1518 or 1519 or some future year
*  and like incorrect in when it like completes a sentence with lasted from 1517 to 1516.
*  And so there is some like human judgment call here that like some completion the model chooses,
*  1718, 19 are like the correct ones. And we want to measure that. And some completion of the model
*  probably places some probability on because these models like usually output like a distribution
*  over each completion they could like create that we deem incorrect. So the like practitioners in
*  this case decided to like measure how good the model was in this task by like summing the
*  probabilities on the like correct completions like the future years and subtracting the contributions
*  from years that were less than that. And so it like wasn't sufficient for those researchers
*  to just find like the subsets of models that were like similar to the original model, because the
*  original model was wrong in some ways, it would sometimes predict like the wrong earlier years.
*  And so the like metric allows you to be a little bit more like fine grained and measure an exact
*  behavior that the model has, rather than just hoping that the models like distribution,
*  which includes some incorrect parts is correct. So yeah, I guess the like the high level thing here
*  is that language models can be wrong and are often wrong. But you can like select for that,
*  if you know what like the right answer is, and put this into a metric. Does that make sense?
*  Yeah, it's interesting. I mean, I guess we'll get into this a little bit in the upshot,
*  you know, for kind of the findings portion as well. But it does still feel a little bit to me like,
*  I don't know, confusing just in as much as, you know, if this model has been trained to do this
*  thing, or maybe it's not trained to do specifically this thing, but it's been trained, and this is
*  like one of the things that it seems to be able to do. If we then go in and start cutting out parts
*  of the network or, you know, patching them with, you know, kind of neutral, it doesn't seem like
*  it would, it should get better. I guess in some cases, it could, but that would, you know, be kind
*  of a weird, you know, random result, or seemingly random. And you can, if you have intuitions for
*  that, I definitely want to hear them. But so then I kind of wonder, like, why not just stick to the
*  simplest thing of like, keeping the same original behavior, as opposed to kind of looking at this,
*  you know, this kind of task specific measure that's, you know, that's kind of cooked up,
*  seemingly kind of ad hoc. Yeah, I think I want to push back slightly on the like intuition there
*  of like how language models produce their completions. Because often when we're like
*  using like the like the GPT-4 and Claw 2 chatbots that are a state of the art, it feels like they're
*  like perfect in some completions, like it all looks correct. And there's very few errors. But
*  the like pre-training task for models that is like most of the computation procedure to produce that
*  great model at the end, involves predicting text from like across all the internet. So across all
*  books and all forums, and all like just general sites on the internet. And the model like probably
*  always has some like uncertainty over like what exactly the like locate like the location on the
*  internet essentially of the prompt is that it needs to use to produce better completions that are like
*  more likely to be correct. And so in some sense, it's like juggling a lot of different heuristics,
*  but some include just producing what to humans seems correct, like a year that's in future.
*  But there's some balancing of like ironic completions or jokes or something where it has to
*  like balance some probability that there's just like a dumb mistake here essentially. And then
*  there's also some uncertainty that maybe this like web page on the internet got like transcribed
*  poorly, so that like the document will just cut off at this point. And when you think about just
*  like how diverse the like internet of like different text pages is, it's then like less obvious that the
*  model like should be completing what to us humans seems like the correct response, just because there
*  are so many contexts in which any particular sentence could arise. And this introduces just
*  so much complexity that I guess my intuition for having like metrics for behaviors and
*  mechanistic interpretability is you can control for this like what long tail essentially of possible
*  reasons why completion would arise by specifically choosing like completions that are correct in the
*  sense of a year that's larger rather than smaller. So yeah, I think that a language model training
*  produces like a very wide diversity of like outputs, some which seem correct to humans and
*  some that don't at all. And we can control for this. To try to synthesize that for myself,
*  I guess what you're saying is because the models in general have not been trained super specifically
*  on this task, and they have not been trained on a super clean data set, you know, that's probably
*  another reason that the frontier models are performing so much better is they probably have
*  a lot cleaner data set than some of the earlier open source stuff that is accessible for this
*  kind of work. But because they have such a mess, you know, kind of going into training, they've
*  learned all these different things and they're all, you know, there's all these kind of sub circuits
*  running in superposition on top of each other. And so actually, there are, when you zero in on
*  this task, it is actually reasonable to expect that there is some sub circuit that in isolation
*  could do a better job than the model itself is doing. And your goal with defining a task specific
*  metric is to zero in on that perhaps even better than baseline model performance by stripping away
*  this other stuff that in fact might be hurting overall performance on this task. Yeah, exactly.
*  I agree entirely. Yeah. And just to put it in perspective, like the number of tokens these
*  models are trained on is just mind blowing. And you imagine, or rather you look at the statistics
*  of how long a human would need to spend reading like just text monotonously. It's like orders of
*  magnitude longer than a human lifetime to consume the amount of text that like these models consume.
*  And therefore, like as the individual humans, we like actually cannot model the full diversity
*  of the distributions that like we're training these models on. So to me, it's like actually
*  not surprising that like there's just substantially more complexity than there is to human text
*  completion inside of like these like language models. That's all my questions on part one. So
*  we have identified a behavior of interest. We have put together a data set that demonstrates it and
*  has some contrasting examples that are similar but don't have exactly that same critical behavior.
*  And we've got a metric to evaluate it, which could be by default just minimal change to the
*  model's output. But we do have some reason to expect that we might even be able to get
*  better performance if we're savvy about defining a more intentional metric for evaluation. That's a
*  big theme I kind of keep trying to reinforce for folks in general, just at the base level of
*  model creation in the first place, that like clever formulation of a loss function has been
*  one of the big unlocks in the last few years, really. Just moving to this next word prediction
*  or next token prediction in the first place was kind of a stroke of genius that allowed for
*  all the data to be used. But that's just one loss function and there's certainly a lot more work to
*  be done there to come up with better optimization targets. So that brings us to part two. And
*  this part again, I'm tempted, again, I don't want to be like overly reliant on analogies, but here
*  it does seem like in a lot of different areas of science, one of the kind of core decisions
*  that you have to make is at what sort of level of zoom or what level of abstraction
*  am I going to study this problem on? So in biology, you've got ecology and you've got,
*  on the other end, like genetics, and you've got a lot of layers in between. You can study cells,
*  you can study systems within the body, you can study an individual organism, you can study a
*  species, you can study all these different kind of layers. So it seems like there is a reasonable
*  analogy here that you kind of have to do the same thing. You could look at every single activation,
*  but for multiple reasons, that becomes either computationally intractable or just like too
*  much of a mess. And so you have to kind of pick how zoomed in do we want to get
*  for the purposes of this particular analysis. So how can you develop our intuitions a little
*  bit more there for how you think about this decision? Yeah, the analogy to biology,
*  while it's important to be like guarded around giving like analogies to like different fields,
*  I think that like, broadly speaking, I expect that like the development of this like mechanistic
*  interpretability field to progress more like biology than like different fields such as physics,
*  because there are like a number of parallels between the like development process of the
*  complex systems inside neural networks that are neural networks, essentially, and the like
*  evolution process that also like training on a very like stupid, like goal function,
*  but then also gave rise to like incredibly complex behaviors along the way. And so beginning with an
*  agreement with the analogy here, yeah, in terms of what is the choice and how the choice is made
*  in mechanistic interpretability research, I think it's mostly a question of like how ambitious the
*  researcher is essentially in terms of how they're like pushing this like frontier of the best
*  explanations that we currently have of certain behaviors and certain like behaviors of different
*  complexity with sufficient like depth and zoom in zoom into that like explanation of a behavior.
*  And so it's a young field and there are really not many researchers doing research on
*  mechanistic interpretability, but we already have like neuron level explanations of how like toy
*  transformers complete the correct completion to like modular addition, which is work by like
*  Neil Nanda and collaborators. And we have much worse understanding, but still some understanding
*  of how GVD2 small like completes its predictions, the solely in terms of like
*  attention heads and MLPs. And then to give like a third example down the line, other researchers,
*  the paper is called Rome or like the Eiffel Tower is in Rome, have looked into like the factual
*  recall models and then edit that recall models by looking at where facts are stored in terms of
*  whole like attention layers, which include each a bunch of like attention heads, like in parallel
*  and their work groups together whole layers of the like model to then say, well, the factual recall
*  is isolated to these layers. And so really, it's a question of like, how ambitious like is your
*  project? And the answer to how ambitious are you is the correct answer rather is not always like
*  more like a if you try and like explain things at like a really low level, and this is just
*  extremely difficult, that is unlikely that like projects will be successful. And so just I think
*  as a research community, people in mechanistic, it's absolutely research, you're just trying to
*  like improve this frontier of getting better and better explaining harder behaviors, but in a more
*  zoomed in way, and giving their contribution to the field that way. And so it's mostly comes down
*  to like a judgment call on the researchers like parts for like where they're aiming at. And so
*  yeah, that's an example of three different levels, the neuron level in modular edition work,
*  the attention head level in GPT-2 small work covered in our work, but then the attention layer
*  or like several layers level that's explored in different factual recall work. And I think all of
*  these are like pretty good contributions at different parts of like the frontier.
*  And again, it just seems like there is intuition here around things like, you know, the best way
*  to explain the flight of a fly ball is not to go to the quantum mechanical level. So you want to
*  use a level of description that is actually meaningful to the, you know, to the person who's
*  absorbing the output. So in some sense, it's like you're optimizing for the human audience's ability
*  to understand the results as much as anything else. Yeah. And like also as a quantum mechanic
*  to actually be able to finish your project to explain flight there. Like I wish you luck if
*  you're a quantum mechanic trying to do that, but I also don't expect it to be successful. So that's
*  like the trade off that is being made here. Yeah. So how in practice, you know, at a conversational
*  level, this sounds sort of, I don't want to say easy, but it sounds like, you know, there's a few
*  levels that you could zoom into that seem pretty natural. And, you know, if we're chatting about
*  this over lunch, we can easily say, Oh, why don't we try looking at the, you know, attention heads
*  as kind of the, you know, the level of zoom for this particular project. But then obviously if
*  you go back and actually code this and make it sort of, you know, something that can feed into
*  the third step of actually automating the process of isolating these sub graphs. So how hard is that
*  from a coding standpoint or a notation standpoint? That's how it sounds kind of hard to me. I'm not
*  the world's greatest coder, but I feel like I would have a hard time going from, okay,
*  we've decided we want to zoom in on the attention head level or, you know, an ML individual MLP
*  blocks will be our kind of unit of consideration to then actually figuring out how do I express
*  that in code as a, you know, causal acyclic graph. That's where it starts to sound a little more
*  challenging. How hard is it in practice to do that? Yeah, I would say this was definitely one of the
*  more fiddly parts of the ACDC project to translate these high level intuitions into something which
*  is like able to be modified inside code. I do think that there are like pretty good libraries.
*  This is mostly a coding question at this point to be able to like extract and edit the internal
*  states of machine learning models. So yeah, with any like, once a researcher has some familiarity
*  with how like language model forward passes work, it's not so difficult to then add like attachments
*  into your code base to extract those like activations because generally they are
*  represented cleanly. And in our work, we've like made a library for researchers to be able to more
*  cleanly edit the impact of like one particular model component specifically on one like later
*  downstream components, because that's the part which is somewhat harder from the like implementation
*  perspective, editing the specific effect one earlier model component has on one later model
*  component. Because by default, just your like code just runs from end to end and one model component
*  affects all downstream components. But to do interpretability, you'd like to be somewhat
*  more fine grained and look at the impact that an earlier upstream component has on each individual
*  downstream component. So that's the part that's difficult, though it is pretty easy to get at
*  least started with like isolating individual attention heads. And there's now a lot of
*  educational material, like trying to get more people to do mechanistic interpretability and
*  to like have fun doing these sorts of experiments. The difference here is that if you are trying to
*  just execute procedurally the transformations of the transformer, you sort of take in data,
*  you apply some mechanisms, you know, that ultimately cashes out to linear algebra,
*  you take the results and you just kind of keep going, right. But once you're kind of past a
*  certain layer, you can like leave that stuff aside. You don't have to, you know, by default,
*  that inference time, right, you don't necessarily keep track of how layer one interacts with layer
*  eight or whatever. You don't even necessarily think of it that way in the implementation,
*  because you're just kind of doing one thing at a time. It feels like this happens, then this
*  happens, and this happens, and it feels very linear. But there is this kind of conceptual finding,
*  empirical conceptual finding that because of the residual stream, if I understand correctly,
*  actually you can have critical interactions that do not proceed layer to layer, but actually skip
*  layers or you have these kind of, if layer, obviously I'm just making up fake examples,
*  but if this happens in layer one of this particular network, then layer five also like lights up.
*  That's not the kind of thing that the naive kind of forward pass implementation really looks at.
*  So the hard part is kind of, maybe not the hard part, but certainly a conceptual leap that one
*  needs to make here is understanding that like this causal graph is a bit more complicated than just
*  the direct like procedural implementation. Yeah, that's exactly right. So this was a really
*  beautiful like finding from the anthropic interpretability team. So the AI lab that make
*  Claude that as Nathan, as you mentioned, there's a residual stream, which in like normal machine
*  learning is usually just referred to as like the hidden state of the network, which is transformed
*  from each layer incrementally. But the researchers at Anthropic realized that if you're implementing
*  a model with residual connections, which just means that once you apply some transformation
*  to this hidden state, you then add the original hidden state back to the transformation. So you
*  incrementally update by adding a transformation of the current state at each step. And this gives you
*  like a whole way to view like the forward pass of transformers and many other models as a continual
*  stream of information, which the model components read from and then write back to. And this is like
*  a really useful finding for like all of the sort of mechanistic interpretability research field
*  that has like this key consequence that we can model the impact that one very early layer component
*  has on like a specific downstream component that is like a really non-trivial finding,
*  but it's really like beautiful once it like makes sense from the Anthropic paper,
*  a mathematical framework for transformer circuits that was a substantial like inspiration for our
*  work that we like added to. I do have, I think the graphical representation that they use in that paper,
*  which presents the residual stream as kind of the central object. And then all of these other
*  things as kind of side, you know, the attention heads and the MLPs as kind of side loops that are
*  like making a contribution as opposed to centering those and having this kind of random line that
*  kind of goes around them, which is how they're, you know, so many of the transformers are designed.
*  That was definitely an eye-opening and kind of clarifying reframing for me. And that is in the
*  early slides of the AI scouting report. So definitely, you know, another good reminder
*  to check that out to get a little bit more grounding on some of these earlier results.
*  So this ultimately does still sound kind of hard to me because, you know, you have kind of a clean
*  forward pass implementation, but now you do have a many more kind of paths, causal graph that that
*  ultimately turns into for the purposes of this type of sub-circuit isolation work. Come back to
*  that in just a second. One thing that jumped out to me also is kind of a footnote, but, and this is
*  the kind of thing that may be really obvious to all the practitioners like you who do this every
*  day, but is not necessarily so obvious to people who, you know, are kind of trying to catch up to
*  you, is the idea that all of these circuits are acyclic, meaning there can never be a loop
*  in the design of the circuit. It all has to be one way. It all has to be, you know, the kind of
*  language of forward pass and back propagation sort of suggest that. But I'm interested in your
*  thoughts a little bit on this kind of cyclicality. I guess for one thing, you know, do anything more
*  to add. And then on the other hand, like, I wonder if that kind of represents some sort of frontier
*  in model development where if we could figure out how to have some sort of cyclical loop,
*  you know, certainly that's something that we have, right? We have some sort of ongoing kind
*  of feedback mechanism where our current state, you know, interacts with our future state and
*  our past states in ways that are not, you know, we're not just like, you know, waking up and
*  executing a single forward pass in isolation each time. So yeah, do you have any thoughts on this
*  cyclicality as like, it's a little bit of a digression from the main topic, but does it
*  feel like that is something that will never come online because our techniques just don't support
*  it? Or do you feel like that is maybe, you know, one of a candidate for kind of another future
*  capabilities unlock? Yeah, I really like this observation that I think is one that like
*  researchers like me who spend like their days trying to like understand these models forget
*  is like a design choice, which is informed all the things that I look at that these models are
*  just like ends to ends rather than like cyclic at all. And so I think it's a great observation
*  because it's just one that I just wouldn't have noticed because I spend all my time working with
*  the like the end to end models. And yeah, like the constraints of back propagation and requiring to
*  have like gradients for each individual component as aggregated end to end does enforce the like the
*  forward pass of the model then just computes like a purely linear process, which goes through like
*  different edges, but then is always like going forward in some sense. And yeah, like the like
*  mechanistic adaptability research community has mostly focused or is mostly focused at the moment
*  on these transformed language models, which all like operate under this like, like a cyclic paradigm.
*  And yeah, it's certainly just essentially a whole another dimension, which there's no current work on
*  to be able to like unlock some interpretation of which definitely like could be something which
*  would really like advance our understanding, particularly because a lot of the current use
*  cases of like language models are maybe not quite like ace, like not quite cyclic, but certainly more
*  recurrent, which means like leading back into themselves, which like in general, mechanistic
*  adaptability hasn't managed to like get a great handle on yet. So while we can talk a lot about the
*  sort of like ability to understand how models produce one token completion, and how this is like
*  really exciting open research direction, we don't have much understanding of like how models produce
*  helpful like rollouts of completions. So whole like poems or prompts that go on and do some like
*  chain of thought reasoning, for example, we just don't really know the mechanics of how the models
*  like using its computed new like first token to then produce computed next token. And we also
*  don't have a great understanding of how like these more common like agents deployed on like the internet
*  such like auto GPT models, how they or if they are meaningfully different from the models that just
*  compute like one forward pass, but instead like these models are continually produced more and
*  more actions that the model then like tries to like do and then like observe some like a consequence
*  on that action and then acts on that further. So yeah, like all this sort of discussion is premised
*  on like just really like individual single forward pass completions. And there are ways it could be
*  extended, but we certainly haven't done them. And I'd like love for like future work and future
*  mechanistic adaptability research to hopefully grapple with like these like harder problems
*  of like recurrence. And then plausibly even like cyclic models, if people find ways to like make
*  this work with back propagation. Yeah, I kind of see two more little follow-ups in this digression
*  and then we'll get to the core of your contribution. What I was kind of, if I understand correctly,
*  the core kind of constraint here and the reason for having this no cycle, no loops, acyclic
*  constraint is basically that we just want to have easy computation for back propagation, right?
*  Whereas if you, so you can kind of work your way back and you're only each at each time,
*  you can sort of say, well, we know how all the other stuff already plays out. So we're kind of,
*  you know, using the chain rule and it's all at each step. It's like an easy calculation.
*  Whereas I guess if you had a loop that would seem to suggest something more like a differential
*  equation type of math dynamic, and then you would have just a lot harder math on your hands. Is that
*  basically the issue there? Yeah, that seems correct that we like have found this easy way
*  to train models under back propagation. And it's certainly not like the optimal way, but it's like
*  a common lesson in like machine learning, essentially, that a lot of progress is generally
*  gained from pushing simple techniques super far compared to creating incredibly intricate
*  and complex techniques over like long periods of time. And so yeah, my like the article by
*  Rich Sutton, like a famous like a machine learning researcher calls this the like bitter lesson
*  that generally are smart methods in machine learning. If they can't like absorb large amounts
*  of computation power, lose to much simpler methods, if the simpler method can scale a lot.
*  So I think this like forward pass and non cyclic like paradigm of models is probably a consequence
*  of like this simple backdrop setup for like language models. In fact, being very scalable to
*  like large amounts of compute, whereas cleverer architectures may like bake in better assumptions,
*  and in theory have like more useful properties, but aren't as easy to like, just scale with a lot
*  of like compute. And so I think that's the focus of like my research, I'd say overall, like focusing
*  on the simple and principle like techniques that actually scale to like quite formidable consequences.
*  All makes sense, the bitter lesson, we learn it over and over again. What about a change to the
*  loss function on the other hand? So I'm thinking of a recent paper, I'm hoping to interview the
*  authors of this one as well. I believe it was out of Stanford, where it kind of made the rounds for
*  having a backspace token. That was kind of the headline, like we introduced a backspace token,
*  now the model can kind of course correct. I've only read the paper sort of superficially so far,
*  but it also seemed to involve a different loss function that they kind of talked about re-casting
*  the process as an imitation learning challenge, as opposed to just next token prediction. And
*  therefore, the optimization seems to be over like a longer, you know, set of tokens, and then that
*  can kind of feed into this ability to do the backspace action when the results seem to be
*  getting too far outside of, you know, normal distribution. What do you think about, does that,
*  how does that kind of loss function switch potentially relate to this kind of mechanistic
*  interpretability work? Yeah, I don't think as much as a researcher about the like sort of the loss
*  function these like models are trained on, like what's the optimal choice loss function there,
*  but I certainly think it's like a really exciting direction for interpretability to try and like
*  choose loss functions that are like more interpretable by default. And I think I was
*  excited to hear that you spoke with Ziming Liu, who's done some stuff on changing the loss function
*  of models to make them more modular. And I think that this work is exciting. Yeah, it's
*  not something which I personally worked on, but I always enjoy seeing changes to the default setup,
*  which can hopefully incentivize like models to be more easily amenable to like our explanation
*  techniques. And yeah, I think that one lesson here, which is quite useful, is that it's exciting to
*  have interpretability and mechanistic interpretability techniques that can hopefully
*  work no matter what sort of like training setup is, or how models change. So we'd like to have
*  like approaches which will work even if the sort of like game changes slightly, and people do
*  things differently in future. And so this was like a substantial motivation for like the work on
*  just pinning down models computational graph in full generality, because this wasn't tied to like
*  having the particular transformer architecture that's basically ripped off of the like GPT-2
*  and GPT-3 papers, but could potentially be used on any sort of model. So yeah, I think that I'm,
*  I think it's a good idea, particularly because machine learning moves so fast, to be open to
*  approaches that will still work if the like board game changes as like machine learning progress
*  continues. So that brings us, you know, and I appreciate all your time and willing to go
*  down some of these rabbit holes with me. But I think that brings us finally to your core
*  contribution, which just zooming out for a second, this three step process of identify a task,
*  have a data set that can demonstrate the task, have an optimization goal to evaluate how a sub
*  network is doing against that task. That's all part one, get set up to figure out how to represent
*  your network as this causal graph. And now three, what you have created is a piece of software
*  that can automate the otherwise extremely tedious process of just systematically working its way
*  through all the branches of this graph and figuring out which of these actually do anything and which
*  can we cut as we look to zero in on what's actually doing the core part of this work. So
*  tell us about how that works. Yeah, cool. That sounds great. We got so into just like explaining
*  the sort of like side tangents of why mechanistic interpretability research done all these things,
*  that that was far longer than a necessary introduction to like what like the contribution
*  of ACDC, so automatic circuit discovery is, since ACDC is really just like a three step algorithm
*  that like imitates the human process for trying to interpret neural networks, but does this just via
*  like a software rather than requiring a human in the loop. And so given all the like extensive
*  description of the setup that we went through, the three steps are firstly selecting this
*  computational graph at some level of abstraction and then add like a given node in that like out
*  like that graph, looking at all the like input edges to the node in that graph and one by one
*  like removing them by setting their like activation to the activation on the baseline data set
*  and then measuring whether setting the activation along this particular edge to the baseline data
*  set decreases the like model's performance on the downstream metric by a given like amount.
*  And if this is a like a large decrease in model performance, then we keep this edge in the graph,
*  but if it didn't seem to matter at all, we can remove this edge. And that's like the step two,
*  which we then just recurse in the third step through all the nodes. So that's like the high
*  level overview or all of ACDC, but it really is just like three steps to find a sub graph of the
*  model's whole computational graph. So you've got this process for kind of neutralizing
*  components of the graph, asking how does performance compare on the output metric? And then
*  if the performance is sufficiently degraded, then we decide, okay, that's one we need to keep.
*  Whereas if it's not sufficiently degraded, then okay, we can throw that away. So I guess
*  two questions there. One is like just procedurally, you have all these different kind of
*  length connections, right? Like if I'm starting at the end, my last MLP block or whatever,
*  it's influenced by all previous layers, but those are mediated through the residual stream.
*  So what does it actually mean to say, if I'm looking at, okay, the connection between
*  the eighth and final, let's say MLP block and the first attention layer, that's all kind of
*  the direct connection there being mediated through the residual stream where all this
*  other information is also flowing. What does it mean to knock that part out? Like you can't take
*  the whole residual stream out, right? So what does that actually look like to cut that kind of
*  connection? Sure. So in the example of a very early layer attention head, for example, that might be
*  just one of the things that are the inputs to one late layer MLP. We would generally write the
*  inputs to that MLP as the sum of all the previous components, because as mentioned in the residual
*  stream, the inputs to the MLP is just the sum of all the previous components that have added to
*  the residual stream. So if we want to corrupt the effect that this singular attention head in the
*  early part of the model has on this far downstream components, like an MLP, what we can do is we can
*  take the inputs into this attention, sorry, this MLP at the end, we can then subtract this clean
*  contribution from the earlier attention head and then add in the corrupted output of this attention
*  head. And then this will preserve all the other clean activations, which are the inputs to this
*  MLP, and we'll just corrupt the contribution which comes from that one early attention head.
*  And so yeah, that's the process that we use to edit just this singular connection from,
*  in this example, an attention head to an MLP. Let's go back to the years example. So you're
*  looking at the greater than task, the war went from 1517 to 15 blank,
*  and you've got your contrasting example, which might be the war went from 1500 to 15 blank, such
*  that you don't necessarily need to do the greater than because it's going to be some,
*  any two digit number there would work. So you then have a situation where you're like,
*  all right, I've got all my activations for the actual greater than task, I've got all my activations
*  for the kind of very comparable, but not requiring the actual greater than operation task,
*  I hear you, I get the idea that okay, I can express all the inputs to a late layer as the sum of all
*  the outputs from the earlier layer. If I switch, you're only doing one adjustment to the sum at a
*  time. So like, if you're just looking at this one layer, I'm a little confused still about,
*  if I were to change the outputs, those would also change how each middle layer of the input
*  of computation actually works. Right. But you're not doing that. So like, if I'm,
*  if I'm looking at the connection between layer one and layer eight, I'm not necessarily changing
*  the sum for the purposes of looking at layer seven. Is that right?
*  Yes, you're totally correct that we do not edit the effects that in the example, the
*  early attention head has on all the middle components. And to provide an implementation
*  detail, which might help to understand the process here, we actually simply cache the
*  corrupted value and the clean value of this early attention head. And the benefits of caching are
*  that we can run the forward pass up to this final MLP without having done any changes to that early
*  attention head. But then once we're at this MLP, we have the cached clean and corrupted value.
*  So now that we can like force this MLP to have like essentially seen the corrupted value,
*  even when in the whole forward pass so far, we just had the like the early attention head,
*  for example, on the like clean input. So it's a matter of caching those two, like saving them
*  as in your like piping code, nothing more complicated than that. So that then once we're
*  at the downstream node, then we can do the editing. And this ensures separation of the effects of the
*  early attention head on the middle components separate from the effect of the early attention
*  head on this particular MLP. So again, what I understand you need to be doing for starters to be
*  make sure I have this straight is defining how much degradation in performance on our optimization
*  metric will we tolerate. And if it's if the degradation is below that level of tolerance,
*  then we'll cut that portion of the graph. But I was kind of confused because I was kind of
*  thinking, you know, different tasks, different graphs, everything might be so different.
*  Does it make sense to make that kind of the the free parameter? Or would it make
*  more sense? If it were tractable? I'm not, you know, this is where my abstract math isn't quite
*  strong enough always to know what's going to work or not. But I kind of felt myself wanting
*  to reframe the question a little bit and say, how sparse can I make this graph? How much can I cut it
*  while still maintaining some overall level of performance? So why do I set that kind of
*  individual kind of operation, you know, bit by bit threshold as opposed to some kind of global
*  notion of how sparse can we go while still like succeeding at the task?
*  Yeah, this is a fantastic question, because I would much rather have an algorithm which chooses
*  the sparsity of the graph and then gives you back a subgraph that has that sort of sparsity.
*  And the reason that instead, we just have like a threshold, which measures like the amount that a
*  single edge matters is purely like a tractability question that we don't know how to design an
*  algorithm, which like at the end, or at least I don't know at this point in time,
*  that like at the end will give me like this graph that's sufficiently sparse, let's say,
*  but in the process aims robustly towards that conclusion. Because in advance, you just don't
*  know which of the huge number of subgraphs will be the one that is the best at explaining how a
*  model does a task. And I think this is like a general machine learning iterative optimization
*  problem that really we would like to specify what we want in the end, but this doesn't really
*  give us like a tractable way of getting there. Are you just asking for like a
*  x or y sparse graph, this amount of sparsity in your end graph. But like if you just immediately
*  select a graph with that sparsity, it just will be like, in general, like absolutely hopeless at
*  the task. And so we need like an iterative way to get there. And this could be gradient descent,
*  or this could be the sort of ACDC algorithm, which goes node by node. But it just is like a
*  pretty hard problem to like, have that like end goal be a useful target through the optimization
*  process. So your intuition is completely correct that we would rather have like a
*  this level of sparsity graph. But instead, what we've got is this like, a proxy measure of the
*  like local corruption amount that's allowed. But it certainly can give you some indication of how
*  sparse the end graph will be. Because the ACDC iterative process first will process the output
*  node. So once you've run with a particular threshold, you'll be able to see like how many
*  nodes is added to the output connection. And this will provide some guide to then how many nodes
*  will be upstream, because you're likely you have like one half of the nodes outputting to the end
*  connection, then it seems like you're going to have a pretty dense graph overall, it's going to
*  include most of those connections. Whereas if it's including just like two of the nodes,
*  and you like, for example, wanted a substantially more like that was not enough for you, and you
*  thought there are more components that mattered, you could increase it. So while sadly, we don't
*  have a like a hyper parameter, which can give us the exact sparsity of the end results, the early
*  like performance of the algorithm does give you some indication of how sparse the end result will
*  be. But yeah, it's a great concern. I hope people in the future can make a version which gives graphs
*  of like a specified sparsity. But for now, we like don't have a method of doing this.
*  So for now, you're kind of sweeping through the parameter space for what that threshold should be,
*  and then kind of eyeballing initial results and kind of saying, well, when I set the threshold
*  such that it tolerates a lot of degradation, like everything got cut, and it looks like this has
*  kind of gone too far. Versus if I set it, you know, to only tolerate a tiny bit, then you might see
*  something that looks still super dense and be like, doesn't feel like it's gone far enough.
*  And as you're kind of using a certain amount of taste to kind of figure out where in that
*  trade-off you want to be. Yeah, I think there's a good distinction here between
*  two ways in which we like tested the ACDC algorithm that involved like validation tests,
*  which swept over a huge number of parameters to see what the like best performance was for like
*  this algorithm in different regimes, like in the very sparse regime to the like pretty dense regime
*  was like one thing that happened. But then we also tested like at least a use case where this was
*  used in practice by like researchers who were trying to find like a particular behavior of a
*  model and where it was computed in the graph. And in this case, you're not so worried about
*  sweeping over all possible parameters. You're looking for like a revealing subgraph, which
*  helps you like begin your like research into like how the model is doing a particular task.
*  So I think there's like two modes there that like in the work, in machine learning work, you need to
*  like validate that like actually your technique is helpful for recovering circuits. But then in
*  practice, you can do like early stopping essentially, once you found something which
*  is revealing how models do certain tasks. Yeah, I think the two ways that you validated
*  the results are super interesting to me as well. The I was a little bit surprised by the order of
*  presentation, not that that's like the most important. But when I think about how would I,
*  you know, I've come up with this technique, like how would I demonstrate that it actually works?
*  To me, the obvious thing is like, show that it can continue to do the original thing, you know,
*  as well or not so much worse, or maybe even in certain circumstances better than the fully
*  dense graph. That part makes total intuitive sense to me. But you, is there a reason that
*  you kind of prioritize the other one for discussion earlier, the other one being looking at what folks
*  like Neil Nanda have actually found through their own, you know, non-automated painstaking approaches
*  and kind of comparing what the algorithm, the ACDC algorithm isolates to what they isolated by hand?
*  Why was that like the first place to go for validation? Yeah, that's a good question. So
*  just to clarify the experiments that was performed, it was a experiment to see how well the ACDC
*  technique, as well as differing techniques that we like repurposed from like the literature,
*  were able to like find the circuits that previous work found. I don't think it actually included an
*  example from like the Neil Nanda's line of work, but it did include, for example, the greater than
*  year example that we've discussed a lot. And I think we chose this measure of the measure of how
*  much our technique reproduced the other work that practitioners had done was that our motivation was
*  to like make something which is helpful for a mechanistic interpretability research that is like
*  the first step in the process of like actually giving semantic meaning to the different components
*  in models and like what these components are doing. And so I think that it is helpful to get
*  some indication of how performance your like subgraph is that you mentioned as the second
*  evaluation that we chose. But the purpose of the ACDC algorithm was certainly something that we
*  hoped practitioners would use to like explain models rather than like get models that are just
*  like really good at predicting years, because this is not something which like is actually
*  useful to people. Like how good is your model at predicting years? So our priority was like the
*  first step on the path to understanding the semantic meaning of components. And high
*  performances may be correlated with that, but it's not exactly as direct as just finding the
*  important components that like researchers had like in practice found were like the
*  semantically meaningful components. So I hope that makes sense as like the two different evaluations
*  and why we were excited about reproducing previous work, though it is certainly flawed.
*  We can get into that if need be. If I understand clearly, it's kind of an audience driven thing
*  where your goal is to create a tool that will be adopted by interpretability researchers
*  and to convince them that this is actually meaningful, you wanted to show that you could
*  recreate earlier results that they all know about and you know, hold in high regard.
*  Yeah, I'd say it's true that it's an audience problem, but I want to clarify that I'm not like
*  overselling this approach in terms of an approach for finding like the best sub circuits that do
*  different like behaviors like correct years. This wouldn't probably not be a very competitive
*  approach because we're doing these interventions on like the edges that involve like a substantial
*  amount of caching and recomputation that would be inefficient compared to other ways you could
*  have like elicit model capabilities because it's just like a substantially larger amount of compute.
*  So that's just like not really the like the area that we're like competing for to make a good
*  technique. We're competing for something different, which is like the discovery of the semantically
*  meaningful components. So I'm not overselling my work. I do think it would be a very good algorithm
*  for getting very good sub graphs at particular tasks, but it wasn't the goal ever either.
*  So that would contrast to like the zooming Lou from the Techmark group work that we talked about
*  earlier where they are taking a different approach, modifying the loss function during
*  the training process to kind of create sparse networks by design. Is that kind of what you're
*  contrasting against? Like that would be the approach to finding the sparseness network
*  that can do a task and you are instead trying to create a tool that can kind of also do that,
*  but is doing that already downstream of like this very messy training process.
*  So it's not really optimized for the best possible circuit, but it's optimized for finding what
*  circuits do in practice exist given current techniques. Yeah, I think this is a useful
*  distinction between post hoc interpretability, which our work is like an example of and like
*  training process interpretability or like selecting for interpretability that I think that the zooming
*  Lou work is a great example of. So here we're assuming we have some fixed model and it's a
*  black box. We want to like open up the black box to understand what's happening within it. That's
*  just like the premise of the work, but like complementary work, a different direction you
*  could take is yeah, like designing training processes that incentivize like interpretability
*  through like modular structure in that example. And I just think these two approaches complement
*  each other because on one hand, if the architectures that like we were studying were more comprehensible
*  and then this would just make our job or more modular rather. This would make
*  mechanistic interpretability much easier, but at the same time work that's building into the
*  loss function, some hopeful notion of interpretability does need to be validated to actually be
*  interpretable down the line because models can learn like strange solutions which appear
*  interpretable, but are not in reality as interpretable and some work by Anthropic on
*  a technique called solo as an activation function instead of relu or galu is actually an example
*  where the researchers try to like choose a training process, which led to a more interpretable model,
*  but found that the model was like hiding its like superposition in this case fire,
*  like a confusing routes that they had created by like introducing that new technique.
*  So I think that to reiterate the two paradigms of like post hoc interpretability and designing
*  training processes for interpretability are like complementary and different in terms of like
*  approaches that you would take to like try and reach both of those goals.
*  It's just important to keep in mind that like sparsity does not necessarily mean
*  it's superinterpretable and certainly doesn't mean that it's like generalized in a way that
*  we would consider to be like rocking or sort of representative of some like more fundamental
*  non-stochastic pair of understanding. You could have sparsity and still have all those other
*  problems at the same time. Cool. Well, then let's talk a little bit. You kind of alluded to it for
*  a second about like the compute that goes into this. How much compute did this take? Like what
*  kind of resources do you need? How accessible is this kind of stuff? You know, do the techniques
*  that you have today scale up to large scale models if you just have enough compute or is there not
*  enough compute in the world to apply something like this to a GPT-3? Tell me about just kind of
*  all the compute considerations with this line of work. Sure. So this work was done
*  with computes that was mostly from just like a FAR AI, so like a research group that one of the
*  collaborators, Adria Grigora Alonso, works with. And so this was not like a super cluster of like
*  one of the huge labs that we were working with. And we could see practitioners get results on
*  like the GPT-2 small large language model in like half an hour or like an hour of like runs
*  when they worked super well and were like pretty sparse. Though there are definitely cases where
*  compute is somewhat of a bottleneck to ACDC and particular scaling kits. So the two cases that
*  come to mind are that when you like don't select the threshold appropriately and you include lots
*  of edges, then you tend to have to search through every single node of the computational graph.
*  And since your like computation is like roughly linear in the number of like nodes that are present,
*  this becomes extremely expensive as your technique includes and searches through each node. So the
*  first case is when like yeah you don't choose like the correct threshold and this sometimes
*  can be frustrating and then leads to slow runs and slow feedback loops that we hope that like
*  future work will be able to work on. GPT-2 small is how many parameters? Like 10 million?
*  Yeah so that's the second sort of worry about the like compute that GPT-2 small is a 100 million
*  parameter model. So this is like large given like statistical models or things that people used
*  10 years ago but it's incredibly small compared to like hundreds of billions of GPT-3 larger models.
*  And because our technique is like iterative over all the edges in fact which scale almost like
*  with the square of the number of nodes involved, currently this is not feasible at all for like the
*  GPT-3 size model and isn't really even very efficient for models that are like at the billions
*  of parameters. So we're not able really to scale up an order of magnitude beyond GPT-2 small at
*  current. I at least am excited for further interpretability research to hopefully scale
*  to those sizes and already people have done some interpretability work on the like outpacker model
*  so like a seven billion parameter model and I think that I know a number of like follow-up
*  works to this like work that could plausibly be able to scale up to that size while automatically
*  finding circuits. So an open problem essentially I would like to see more work on it.
*  Yeah interesting. So even with GPT-2 small though I assume we're not using the individual neurons as
*  the as the nodes right? So it's there's still some zoom out so how could you give an intuition for
*  how that kind of number of nodes scales with model size? It seems like there's a almost a different
*  scaling law you know or different scaling intuition that one needs to develop here right? Because
*  it seems like more layers would definitely have a big difference. So even like with a certain number
*  of parameters you know kind of depending on the the width and the number of layers you could maybe
*  set things up where the the number of edges to consider actually could vary potentially quite a bit.
*  Yeah that's a good point. I hadn't even considered that in the discussion that in fact almost all of
*  our research in the like the main text of our paper focused on the abstraction level of the important
*  attention heads and the important MLPs in these like large language models rather than being
*  more specific or to the individual neurons of these large language models or the like attention
*  layers that would be less specific. I was solely talking about the abstraction level of the
*  individual attention heads and MLPs and connections between them including in fact the individual
*  query and key and value paths that are like the inputs to attention heads for example.
*  We were able to isolate those and I think that this is roughly mirroring the pace of progress
*  of people's interpretability projects because after all it is just like last year that I was
*  fortunate to work with collaborators on the the IOI or interpretability in the wild paper
*  which was the first work that was able to reverse engineer a circuit inside GPT-2 small and then
*  this year we now have the greater than circuits in GPT-2 small for example. So yeah and these works
*  are both at this attention head and MLP level which is like the only like the point at which
*  we can do experiments on GPT-2 small with ACDC. I think it would still be too slow because there
*  would be too many connections if you were looking at individual neurons but the existing interpretability
*  research hasn't really been able to understand these GPT-2 models on neuron level. So yeah some
*  it's sort of a bad news and good news there I suppose for like understanding GPT-2 neurons
*  with ACDC. Even keeping that level of abstraction you know where the focus is on the attention heads
*  and the and the MLP blocks if you were to do try to take the leap you know a thousand x parameters
*  right from whatever order of magnitude 100 million on GPT-2 small to order of magnitude 100 billion on
*  WAMA-2 or GPT-3 or what have you. How does the compute requirement of this process scale? Does it
*  go as like the square of the increase? Like does a thousand fold increase in parameters end up being
*  like a million fold increase in compute or? Yeah I think it's on average slightly worse than like
*  scaling with the square of the number of like nodes or parameters you're introducing. Obviously
*  nodes and parameters not the same but this is because as you increase like the number of nodes
*  by a factor of two say you're roughly increasing the number of edges in the graph by a factor of
*  four because these networks are highly connected. Like it turns out that your layer zero heads have
*  an impact on almost all downstream layer heads and so as you increase the like yeah the number of
*  nodes by a factor of two you roughly increase the number of edges by a factor of four and because
*  this algorithm is iterative over each of the edges this leads to like yeah like the quadratic
*  increase and then like your whole forward pass is now more expensive as well because you're dealing
*  with a bigger model which accounts for something on top of the quadratic cost of more iterations.
*  But I don't think would give you I mean like yeah it turns out that the process of just iterating
*  over each edge is the slow part of this network like the bottleneck rather than forward pass cost
*  so that turns out to be the biggest bottleneck. In practice how easy have you guys made this today?
*  You know for somebody who obviously has an interest in the subject but you know I have I
*  definitely feel like I have some weaknesses when it comes to notation and you know I'm not the
*  greatest at managing like a ton of indexes you know there's a lot of indexes to manage
*  when you're doing this kind of work. Is the work that you've put out like developed enough
*  where somebody like me can actually get in there and do it or like how how much of a burden still
*  remains for you know the kind of casual investigator to get in and start to figure some stuff out?
*  Yeah we try to make our library like well written for like all practitioners by like building it on
*  top of Regrate's mechanistic interpretability library called a transformer lens. So a transformer
*  lens which you can like find on github is a library which makes mechanistic interpretability
*  of generative language models far easier than the default implementations in like hugging face for
*  example or in online tutorials and so it was originally developed by Neil Nanda who again has
*  like helped a lot with making this mechanistic interpretability field easy to skill up in and
*  have a bunch of like tractable research directions so it's thanks to him for this sort of resource
*  but now the ACDC library can load any of the models that are in the transformer lens library
*  as a computational graph with all the connections between the like nodes as different edges.
*  So this includes like the whole GPT-2 line of models as well as a bunch of the like smaller
*  toy language models that have been found by like illuthor AI and the Pythia models for example
*  and some of a bunch of toy models that have different activation functions such as the like
*  the Gelu and Solu activation function. So out of the box you can use this thing with a ton of
*  language models that are available for mechanistic interpretability researchers in the like transformer
*  lens library and this includes like models like the Lama models but we think that probably ACDC
*  will be a little bit too slow on these larger models for now and so like you're excited to
*  future work and scale it up. If all goes according to plan we're going to presumably see people
*  starting to isolate a lot of subgraphs. What would you say then is the state of our ability to
*  actually make sense of these subgraphs? Is that my understanding is that remains like a very
*  artisanal sort of process and kind of has its own workflow of like trying to figure out
*  what algorithm this you know really instantiates and you know is it something that constitutes
*  understanding all that is kind of in the eye of the beholder there's these various techniques
*  around like editing and looking for behavioral change there's like probes you know to kind of
*  try to figure out what internal states you know actually map on to to real world states that maybe
*  the model didn't even necessarily see in its training data but how like in general are these
*  things like do we get to a satisfying conclusion for most of these subgraphs that we identify or
*  not so much? Yeah I think this is mostly like an open question and I'm excited to see work that
*  provides evidence either way for hopefully the interpretability of just these like just raw
*  subgraphs of huge numbers of attention heads and MLPs all that like they would be somehow misleading
*  or confusing and not useful this would be a useful piece of evidence that like mechanistic
*  interpretability is hard and like so far the use case that we found with like a practitioner who
*  used this to find out whether like the GPT-2 small model was able to produce completions that were
*  like the correct gender of different like names in the sentence or expected gender so it would turn
*  like ordinary names of women into like the she pronoun so this was just like the bias essentially
*  of the model to expect that as a completion and ordinary male pronouns or male names rather into
*  he so again like a bias of the model to produce that completion then like reveal this structure
*  the model was like aggregating information about this like name on like this surprising next tokens
*  the name so the model would just like take the name information and then move that to like the
*  next token in the residual streams or a different residual stream and then that would be what would
*  be like would be like funnels downstream into like the like normal like a gender completion
*  of like the he or she completion that was expected based on the like the biases and the training data
*  and so this was a case where the like the azdc algorithm could have gave like a confusing mess
*  as to like how the model did this particular pronoun completion but actually was like fairly
*  interpretable oh it was aggregating information on this like position that was the like the
*  token after the name and the researcher could clearly see that through like a bunch of the MLPs
*  and then could like make that conclusion which was certainly like a non-trivial conclusion
*  and would have taken a long time to find by like hands since it's like a computation which occurs
*  like in the internals of the model like it's not a function the input and it's not like something
*  which is a function of the output it's just this internal position which matters a ton and so in
*  the limited examples we have so far it turned out to be a pretty easy process but i expect there
*  are definitely cases where it's much harder and i'd like to see like further evidence whether it's
*  in general a lot easier or in general still quite hard fascinating i'm trying to kind of envision
*  that and i certainly appreciate the importance of these internal states which you know some might
*  be bold enough to call emergent properties or emergent behaviors do you have a take on the
*  i guess i'll just call it the emergence discourse yeah on emergence it's definitely a concept which
*  is attractive to talk about because of its like connection to unpredictability and the
*  longer-term worries that different AI or new AI systems will be qualitatively like different
*  from current AI systems and i do think that it is however often a question of which metric you
*  choose to measure your property under so abilities of large language models often seem emergent when
*  we look at token completions that our like billion parameter model for example can suddenly do three
*  digit addition like we give it three addition three digit addition sums and it can now like suddenly
*  be able to like generally produce the correct answer whereas like the hundred million parameter
*  models can produce just like rubbish on the same outputs and this feels to us like something that's
*  emergent because like suddenly the models created this and previously it was like absolutely hopeless
*  but often when you like hear these statistics or read these papers about the emergent capabilities
*  of models they're solely looking at a particular metric like in this case the probability that the
*  model gives the correct like addition completion and actually language models and models generally
*  are trained on the logarithm of the probability that the model gives to certain completions
*  and so often follow-up research has found like and it's been called like a mirage in one paper
*  that once you're looking at like the logarithm of the probability that the model gets the correct
*  three digit addition sum correct for example then progress looks really smooth and it just increases
*  like gradually in like the log of the number of parameters of the model but it just happens to be
*  that like exponential growth is extremely fast and so at one moment you're at like one percent
*  likelihood of producing the correct addition sum and then suddenly you're like timesing by like
*  50 or whatever and we're at 50 percent and this looked like it was a qualitative change
*  and came out of nowhere but really you were just staring at like the wrong metric and so my broad
*  take is that for now we are not very good at like finding the right metrics to measure models under
*  and so we resort to just looking at their outputs and sampling what happens even though like best
*  evaluations that exist the like team from the alignment research center who found a bunch of
*  like somewhat dangerous capabilities of g54 still in general used a technique of just looking at
*  what the model's outputs were and we should expect that these like probabilities on completions are
*  growing like exponentially uh in the sort of like scaling curve because we train on like logarithm of
*  the probability of the completions and so i think that currently we're likely to see more
*  emergence but it's mostly because we're looking at the wrong metrics and i'm certainly excited
*  about digging deeper into the internals of models through interpretability or other methods because
*  of the fact that by default i expect we'll see emergence but we could do so much better yeah
*  that's a fascinating i've been kicking this question of emergence around from a bunch of
*  different angles as well and trying to just figure out first of all like what matters and i guess
*  one way to maybe think about what matters tell me if you see this differently is just asking like
*  how practical is it to zoom in on these things in in the process of training because i guess
*  my intuition is that you know what really matters for like users society companies you know is at
*  the end of a training process what can a model do or not do and how general is that capability and
*  you know is it grok in some way that reflects a meaningful understanding or is it still stochastic
*  parrot that seems like the key thing that like matters most it does seem to be true that you
*  know per that mirage paper that if you find one of these kind of surprises and then rewind and say
*  well okay let me actually measure that performance at every every you know increment of the training
*  process then you can plot like a smoother curve and it seems like there's this kind of
*  phase change that is often happening between like a correlation paradigm and a more algorithmic
*  paradigm and those are kind of you know one is is dropping while the other is rising and that does
*  from what i've seen often take like like an order of magnitude more training to to make that phase
*  change or sometimes even more perhaps but it seems like it's still going to be really hard
*  you know if you're training a system like gbt4 first of all you don't know what list of as you're
*  training it you don't know what things will like emerge that you could then later come back and
*  plot a smooth curve on so you're going to have a hard time knowing what things to even look at
*  you know incrementally along the way and then just like the compute tax of that you know if you were
*  to say every batch i want to like run a million diagnostics and you know kind of benchmark a
*  thousand you know a million things whatever at every step like that becomes like massive overhead
*  so i kind of look at that mirage paper and i'm like you definitely found something that is
*  quite helpful to understanding what's going on in the training process
*  but from the standpoint of like society or even model developers it doesn't feel like that allows
*  us to get around this problem of we don't know what's going to come out of the model at the end
*  of a big training run or at least not without like a significant overhead imposed on the training
*  process would you challenge anything there or correct me on anything no i definitely agree that
*  it seems an extremely difficult problem to predict what are essentially like unknown unknown
*  capabilities that we don't like we don't just don't know how far training on predicting next
*  words and then maybe being rlhf fine-tuned on top of that gets us in the limit like how many
*  capabilities does this actually get us will this solve like will this be like competitive with the
*  best humans at maths for example will it never reach anywhere close to like a like a graduate
*  math student i don't know what the answer is here and so therefore i agree that and there's like so
*  many other tasks in this like a ballpark like that that plausibly could emerge or plausibly can't we
*  just don't know where they'll come from but i think that i am more concerned about mostly known unknowns
*  in the like evaluation space of different evaluations of things models can do as like an
*  example a lot of ai safety research has established like that there are often like
*  convergent instrumental goals that models will have so if the end training targets involves
*  one of a huge number of objectives it is useful for the models to gain like power or resources
*  to achieve those goals because power and resources are just like very helpful for a huge number of
*  things that the model could want to do such as like convincing people to send certain messages
*  on the internet or acquiring certain like like objects on the internet or something you would
*  like to have more money and more influence to get those things and so my take here is that we don't
*  just we don't need to look for the unknown unknown capabilities to have helpful evaluations and
*  predictions of different model capabilities we can sort of think about these known unknowns of like
*  concepts which theoretically are likely to emerge through sufficient training because of the like
*  instrumental convergence arguments but then current models don't do very much like seek power
*  essentially so once we restrict to a certain number of capabilities that seem could be like
*  quite dangerous if we have future powerful ai's then i hope that we can develop better evaluations
*  to figure out how close or how far our current models are from doing these like certain dangerous
*  like gaining these certain dangerous capabilities that are like known purely from the theoretical
*  angle for now this this debate kind of always comes up around interpretability or maybe not
*  always but i think it's first and personally just fascinating work that you know i'm very curious
*  about kind of independent of its consequences you know for me it just passes the uh you know it's
*  interesting on its own merits test but you know as i mentioned at the top to me it feels like it's a
*  pretty promising path to safety it seems like you're kind of sketching out like a vision of
*  sort of the holy grail of mechanistic interpretability at least for safety purposes would be to figure out
*  how models might implement some of these most concerning behaviors and then be able to
*  detect that the formation of those sub graphs in the training process that would be like you know
*  the the dream scenario right any anything to add to that yeah this sounds like exactly what i think
*  of is like a speculative but like incredibly beneficial application of like the mechanistic
*  interpretability techniques that like i and a number of other researchers and my collaborators
*  have worked on so i agree with this characterization and i will just like point out that i'm well aware
*  that this like problem that's been sketched out where there are no theoretical dangerous capabilities
*  that powerful ai systems could have can definitely be approached with like other approaches to safety
*  we don't need to have a mechanistic understanding of ai's to be able to like hopefully steer them
*  like away from dangerous capabilities or at least know when the dangerous capabilities are present
*  but it's certainly the case that mechanistic interpretability has like a very strong
*  ability to like isolate and understand those capabilities because it would hopefully be able
*  to explain those capabilities in terms of the exact like location and models and the exact reasons
*  why this capability emerged rather than just like a litmus test that goes like positive or negative
*  but whether this capability is there so that's like the the wider dream of interpretability
*  with regard to like applications and safety what do you make of the argument that i that i do
*  sometimes hear that it's like yeah but everything's kind of dual use and yeah we can understand this
*  stuff better but also that's just going to feed into accelerating the increasing power of systems
*  in general and so you know maybe it's not so good i don't find that super compelling i don't really
*  have a great knockdown reason for it other than just i don't know what else to do but try because
*  it certainly seems like everything is progressing regardless right so i wouldn't pin you know the
*  sort of potential for a runaway kind of loss of control scenario on mechanistic interpretability
*  by any means yeah i want to be careful because i guess we both have a similar opinion here that
*  i also like don't find the arguments or the danger of mechanistic interpretability research
*  uh extremely compelling and since we both sort of perhaps have this opinion i don't want to
*  misrepresent the opposite view but to me it seems like the vast majority of capability gains
*  in machine learning that have been relevant to the development of the most powerful systems
*  have not come from advances in transparency or insights about how models work there's a great
*  discussion of this exact question in like a alignment forum research post on pragmatic
*  ai safety which discusses that uh like you can just survey where capability gains to vision
*  models in machine learning and to language models in machine learning have come from and the vast
*  majority have come from basically engineering hacking to find something which works slightly
*  better than the alternatives while no one really understands why this works slightly better than
*  the alternatives such as picking a loss function that's just predicting the next token that turns
*  out to work really well at absorbing capabilities or in the like rlhf process to pick a reward
*  which just uses between zero and one it's just like a preference between one and the other thing
*  to me these things didn't like arise from a deep understanding of how to model language or how to
*  model human preference but as far as i understand it arose from trying a number of alternatives
*  and then eventually selection pressure leading to these being the best of the bunch and so under
*  this world view of progress in machine learning i think that currently mechanistic interpretability
*  is very unlikely to contribute to like the bulk of further performance improvements in like machine
*  learning models i guess that's my first um disagreement with the perspective that
*  mechanistic interpretability could be dangerous for its dual use to making ever more powerful like ai
*  systems and then my second like disagreements with the perspective that mechanistic interpretability
*  could be like harmful overall is that i think that mechanistic interpretability if it works like this
*  is all premised under it like being useful because currently we haven't found like a stellar
*  application to the models that matter but we hope we can get there this second reason that i think
*  it has like a greater positive side to a negative side is that it plausibly gives us a way of like
*  designing and understanding ai systems in a different way to the current understanding of systems
*  such that we could develop maybe more powerful ai systems like this is the the worry but they
*  would actually be understandable to us we would understand how these ai's are like computing the
*  outputs that they're like processing from inputs and to me this may involve more powerful ai's
*  but would substantially reduce the like risks of deploying these systems because a lot of the risks
*  from like the alignments of ai systems come from being able to specify your objective and trying
*  to get something from an ai system but not understanding the process through which the ai
*  system achieves that end goal and this essentially is like the alignment problem that are specifying
*  the end state isn't enough because it either is really hard to specify that end state like as an
*  outer alignment problem in the jargon or the ai system learns a solution which was just totally
*  unintended and maybe internally optimizes uh that is like this inner alignment problem even if you
*  chose the right goal but to me interpretability and mechanistic interpretability could be like a
*  way if it can work to develop ai systems where we understand that middle like process between our
*  like specification of the goal like the goal of the system and the ai system being able to like
*  actually execute and like achieve that goal so that's my like two reasons for being optimistic
*  about the impact of like mechanistic interpretability research what i try to
*  envision what that might look like you know a a future that sort of combines better understanding
*  hopefully better control but also you know increasing power and you know maybe power per
*  unit compute or whatever first thing that comes to mind is kind of a
*  mixture of experts mixture of sparse experts sort of architecture i'm kind of imagining something
*  where you take like the zooming loop paper we've talked about a couple times that are
*  you know creating these very small but like very sparse and kind of crystalline almost looking
*  subgraphs and you know scaling that up where there's some sort of mechanism where you've got
*  a lot of those and you only use you know a certain number at a time and so you can kind of see like
*  what was what modules were loaded in to handle this particular case what do those things do
*  it seems like that is like potentially pretty promising to me is that how does that relate to
*  your kind of obviously still somewhat vague vision for what might eventually come online
*  yeah i think this is an example a nicely concrete example of like a really like ambitious goal of
*  interpretability where like the whole architecture of like the forward pass can be understood to a
*  human or at least yeah like these high level concepts like the whole routing to a particular
*  expert has some like meaning to humans and i think it's possible that we can get to this stage with
*  mechanistic interpretability but i think it's worth noting that even if this like fails pretty badly
*  it's still possible for the interpretability of narrow tasks like the mentioned power seeking in
*  certain scenarios can be achieved like through like mechanistic interpretability like there could
*  plausibly be a circuit which does this particular power seeking task and having like just understood
*  that circuit in a network we can like understand why the training process got to this solution
*  or we can just remove that circuit entirely before we deploy a system and i don't think this is like
*  ideally what like my future looks like as in oh man we have like this like misaligned system
*  but we'll just like remove that part and deploy it anyway but i think that there are ways which this
*  is like a graceful degradation of the like ambitious goals having a whole architecture
*  which makes sense like an understanding of the dangerous capabilities so we can at least remove
*  those dangerous capabilities even if we don't have an understanding of all capabilities of the model
*  well you've been extremely gracious with your time i have maybe one more question i'll give
*  you a chance too if you want to touch on anything else we haven't but what are you looking at you
*  know i kind of try to keep my eye on the horizon in my you know self uh proclaimed role as ai scout
*  you know i'm kind of always looking for what is happening that maybe isn't being talked about a
*  ton yet but seems like it has kind of transformative potential are there things that you see
*  right now or you know are or keep or maybe haven't seen but are keeping an eye out that you think
*  could kind of change the game so to speak either to make things a lot easier perhaps you know so
*  that you know maybe something like the zooming strategy becomes mainstream and things become much
*  more easy to interpret or on the flip side you mentioned like recurrence you know makes things
*  harder there was just this paper in the last few days i've lived out of microsoft research around
*  retention they propose a somewhat different mechanism which i don't really understand yet
*  but they are bold enough to call it a possible successor to the transformer um seems like you
*  know there's potential here for paths of and this may be an indication too that the history
*  in its particulars could end up really mattering if you can imagine like there may be and it seems
*  to me very likely that there is or there are multiple very viable architectures to be found
*  just starting with the fact that we have the human brain that works pretty well we have the
*  transformer that works pretty well probably other things that work pretty well it seems like some
*  of those things may be much more or much less amenable to being understood so i wonder what
*  you're kind of you know keeping your eye out for in terms of things that could you know kind of
*  you know kind of shake the snow globe or you know kind of rearrange the game board in a substantial
*  way yeah that's a really good question about like looking forward what are like the things that
*  uh like i'm thinking about looking for and i think that um like it's worth others having on their
*  radar and in terms of like yeah mechanistic interpretability and interpretability research
*  i think a common theme which i would expect to be part of a lot of the
*  like the next generation of um contributions to the field will involve more higher level motifs
*  in language models so we spoke a lot of today about the circuit framework we break up uh like a large
*  subgraph into these like individual components like attention heads and mlps that are given to
*  you by the architecture you read what a transformer is and then you learn okay it has attention heads
*  and mlps but both myself and current work and i've heard of a number of other groups are working on
*  trying to go beyond these abstractions of just the heads in the model and the mlps in the model
*  to look for higher level motifs in models so to be concrete uh like you can find as like i think
*  in current work i've been working on that like certain behaviors such as suppressing these like
*  negativity heads in gbd2 small generalized to the whole distribution of training text
*  and you can find this motif that we call copy suppression in upcoming work that works across
*  all the like train distribution rather than just on these narrow tasks and it's also distributed
*  across like several different heads rather than in like singular heads and i know of a number of
*  other groups who are also going beyond the sort of circuit paradigm where you explain uh like
*  different model behaviors in terms of these uh given components like attention heads and mlps
*  but aggregate different components and weight them in clever ways to build like higher level
*  motifs that like at this point in time there are like very few examples of in the literature
*  and i expect that this is like the next big uh phase of mechanistic interpretability research
*  going beyond like narrow circuits and low level details to high level motifs about like how
*  these large language models are doing computation so yeah i'd stay at stay on the lookout for uh
*  higher level motifs that occur across different model components or like between different model
*  components that's uh my personal current direction and what i'm excited to see other groups do work
*  on cool i love it we will certainly keep an eye out for that you've got the motifs notion that's
*  kind of a different sort of thing that you're looking for is there also a frontier on the
*  automation of that or just better automation that you think will be a a driver of a lot of value
*  yeah i think that the uh automation to find motifs or explain motifs is probably like
*  quite a lot harder than the default path of uh just narrow circuits but i think that
*  there are a number of efforts which could be scaled up to either work with acdc or would like
*  go off on their own if they worked out particularly well to be able to like explain motifs so the
*  example would be the like open ai research where gbt4 can be used to explain the neurons in gbt2
*  and here this is a useful complementary technique to like this automatic circuit discovery where
*  we're like just finding structure because it's like by default assigning semantic meaning to
*  different components and i think that what using these like language models in particular to try
*  and explain what different components or even different subsets of different models are doing
*  is like an approach which would be super exciting for understanding how these uh like motifs are
*  present in different models that plausibly is somewhat more difficult with just the pure
*  circuit discovery approach i love it there's so much for us to continue to explore and learn about
*  and you've given us a great tour of one corner of the world but we've got a lot more work to do so
*  arthur conmey thank you for being part of the cognitive revolution thanks so much nathan thank
*  you for having me on it's been a pleasure omnike uses generative ai to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button i believe in omnike so much that i invested in it and i recommend you
*  use it too use cog rev to get a 10 discount
