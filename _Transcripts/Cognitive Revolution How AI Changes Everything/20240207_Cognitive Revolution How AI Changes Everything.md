---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 7123s
Video Keywords: []
Video Views: 5503
Video Rating: None
---

# A Brief History of Biological and Artificial Intelligence with Max Bennett
**Cognitive Revolution "How AI Changes Everything":** [February 07, 2024](https://www.youtube.com/watch?v=HTvaAvdUyBE)
*  Is there going to be an artificial general intelligence? Is there a single principle on
*  which intelligence in general will emerge? Or are we actually going to wake up in a decade or two
*  decades and realize that there really was no such thing as AGI? There's different degrees of
*  generalization that occurs across tasks. Sure. But all entities are specialized for a specific suite
*  of tasks that they're going to face. And the problem with fine tuning is you very quickly get
*  this overfitting issue where it ends up overfitting to the small fine tuning data
*  set and it loses its generalization. It's forgetting old tasks that it was able to do.
*  I don't think this is a nuanced edge case. I think this is a foundational problem with the
*  way these models work. And so how does the mammal brain decide when to incorporate new information
*  and how to add it to my model of the world without interfering with other information?
*  There's a huge outstanding area of research that I think is a key difference between how mammal
*  brains are sort of simulating and modeling the world and how existing AI systems are doing it.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how AI
*  technology will transform work, life, and society in the coming years. I'm Nathan LeBenz, joined by
*  my co-host Eric Thornburg. Hello and welcome back to the Cognitive Revolution. Today I'm speaking
*  with Max Bennett, co-founder of Bluecore and author of A Brief History of Intelligence, Evolution,
*  AI, and The Five Breakthroughs That Made Our Brains. I bought this book immediately upon seeing the
*  title because I've been asking myself for some time now, how many conceptual breakthroughs do
*  we still need before AI systems will achieve functional parity with humans?
*  The answer, of course, is that I really don't know. I would be surprised, but not totally shocked,
*  if it turned out that attention really is all we need and that hyperscaling resolves all practical
*  problems with no major architectural innovations. And on the other hand, I would again be very
*  surprised if the number of breakthroughs needed turns out to be more than five. My best guess
*  would be two or three, but that leaves major follow-up questions, like what are the critical
*  things that humans are doing which AI systems are not yet capable of? Are physical embodiment and
*  multimodal inputs necessary to our overall cognition, or are they just an artifact of our
*  evolutionary history? How is it that we represent memories so efficiently and so usefully such that
*  even a single experience can shape our behavior for life? How do we determine what new information
*  to incorporate into our world models, what to reject, and what to remain uncertain about?
*  Where does theory of mind come from, and is it necessary for adversarial robustness?
*  And is some sort of hierarchical self-modeling needed for effective planning, and perhaps more
*  importantly, for subjective conscious experience? These are huge questions, and as AI systems become
*  more powerful and behave on the surface at least in more human-like ways, I believe it's also
*  increasingly important to understand the key similarities and differences between humans and
*  AI cognition in the most literal, mechanistic terms possible. For that purpose, this conversation
*  and the book on which it's based are extremely valuable resources. I definitely find myself
*  referring back to the five breakthroughs that Max outlines as a lens through which to ponder
*  new developments in AI. Of course, biological systems are extremely messy and constrained in
*  ways that engineered systems are not. Whereas life has to be a place where we can all be
*  and where we can all be, whereas life has to maintain homeostasis continuously, AI models are
*  mostly decoupled from specific hardware, and humans maintain the data centers. And whereas
*  evolution can only select for incremental changes which improve inclusive genetic fitness,
*  human engineers can and sometimes do discover discontinuous step change advances. So much like
*  the flight of birds inspired and informed the Wright brothers' early airplane designs,
*  and the speed and power of today's jet planes, so the history of human cognition can inform our
*  understanding of new AI developments and our expectations for future systems. While in my
*  view, and I believe Max would agree, certainly not representing a limit to their overall development.
*  As always, if you're finding value in the show, we'd appreciate it if you'd take a moment to share
*  it with your friends. A review on Apple Podcasts or Spotify would be amazing, but a simple tweet
*  is also worth a lot. Now, without further ado, I hope you enjoyed this conversation about the
*  history of intelligence, biological and artificial, with entrepreneur and author, Max Bennett.
*  Max Bennett, co-founder of Bluecore and author of A Brief History of Intelligence, Evolution AI,
*  and the Five Breakthroughs that Made Our Brains, welcome to the Cognitive Revolution.
*  So excited to be here.
*  Excited to have you. So I've been on a journey recently that ultimately led me to your book and
*  to this discussion. And coming from my AI obsessive perspective, I've been finding myself
*  thinking more and more about what is it that the human brain is doing that the AIs lack?
*  That was the motivation for me to say, there's clearly some stuff here that we're doing that
*  the AIs are not doing. But I kind of lacked a schema, a way to organize that. And so I went
*  looking for who has done kind of a good taxonomy of the things that humans are doing that I could
*  kind of compare and contrast with. And it turns out that you've written at least a version of
*  that book, which takes us through evolutionary history from some of the simplest organisms all
*  the way through to today. And obviously, with your experience in AI, you can't help but get AI into
*  the title these days and certainly have some discussion of that as well. But I'd love to just
*  kind of maybe take this conversation in two parts. First, really flesh out the argument in the book,
*  and then second, kind of see what we can take from that to inform our worldview and our expectations
*  about AI as well. To get started, you want to give just a little bit of kind of maybe your
*  background generally, but also really interested in kind of how you've brought multiple different
*  lines of thinking and scholarship together into the analysis that you've offered in this book.
*  Sure. So my background is primarily in commercializing AI technology. So I spent
*  the bulk of my career building a company called Bluecore, where we commercialized a bunch of
*  deep learning models for large e-commerce companies. So recommender systems, we did
*  a bunch of work on segmentation as a sort of now pre-transformers AI. So, you know, like the old
*  fashion AI. And so that was a really wonderful experience and journey. But what always perplexed
*  me in taking these models and bringing them to real use cases where you're trying to add business
*  value is how perplexing the discrepancy has always been between what AI models or machine learning
*  models are really good at and what the human brain is really good at. So, you know, back in the day,
*  some very simple things that a human could do, like, you know, have common sense about how you
*  might put an outfit together were things that were astronomically difficult to get an AI model to
*  have common sense about. These things are getting a little bit better now, but back in the day,
*  that was like an incredibly big challenge. So I always had this sort of curiosity about what is
*  missing between the brain and modern AI systems. And that sort of led me to the side project where
*  I just started corresponding with neuroscientists via email. I started just reading textbooks,
*  sort of just self-learning. And that led me to a few interesting ideas that led me to publish a
*  few papers and collaborate with a few neuroscientists. And then they just started sort of snowballing into
*  me having this idea for a book. And then I was just like, all right, I'm just going to take a
*  year off and write it. The whole time I was collaborating with a bunch of mentors of mine,
*  Dalip George, Carl Friston, Joseph Ledoux, David Reddish. These are all people that have become
*  mentors of mine and have sort of guided me along the way and helped me realize ideas I had that were
*  stupid. So yeah, so that was a really wonderful journey. And then hence the book was created.
*  To me, the kernel of the idea that makes the book unique is it really brings together three different
*  fields of study that I think wouldn't have been done without sort of a outsider kind of coming in
*  with just trying to piece things together. So the three fields of study are first,
*  evolutionary neuroscience. So this is the idea of trying to piece together what is the story arc
*  by which brains came to be over the last 600 million years, even just the last decade has
*  seen huge new pieces of inner of knowledge emerge from this field. It's a relatively small field,
*  actually. But there's been some phenomenal studies and trying to actually piece together through
*  looking at different brains, the animal kingdom, gene analysis, all these things have helped us
*  really piece that story together. The second field is comparative psychology, where we're actually
*  analyzing what are the different cognitive and intellectual capacities of different species.
*  And that can be used, obviously, to try and back into paired with evolutionary neuroscience,
*  what were the cognitive intellectual capacity of our ancestors, which is not really something
*  that's been discussed. I wrote a few papers on that, which is how do we actually try to
*  infer what the first mammals were capable of doing from what existing mammals can do,
*  what non mammalian vertebrates can do, and what evolutionary neuroscience suggests exists in their
*  brain. And the third field is AI, which I think is really essential to this whole exploration,
*  because AI really grounds us in reality, where I think fields of cognitive neuroscience,
*  it's easy to get into sort of philosophizing on concepts on how the mind works, which I think is
*  great and fruitful and rich insight. But what I like about AI is it really grounds us in do we
*  understand what we mean by these concepts? If so, we should be able to implement a very basic form of
*  it and test how well it works. So I think AI is sort of a litmus test for how well we understand
*  what we're actually saying. And AI has really taught us a lot of our intuitions are wrong.
*  And that is, I think reinforcement learning is perhaps the sort of best form factor here where,
*  and we'll get into this, but there's been lots of intuitions about how animals learn by trial and
*  error. And it was only by actually trying to implement these things in machines that we learn,
*  well, that intuition can't work because we haven't. And then we learn, well, the way we actually get
*  to work machines, this other approach, which actually does seem to be how brains do it. So
*  there's a really beautiful feedback group. So in summary, the idea of the book is to take
*  comparative psychology, evolutionary neuroscience and AI, merge them together and try and craft a
*  first approximation of how the brain came to be and see if there's insights there for AI.
*  I think there are some insights. I don't think it's necessarily an explicit roadmap for how to
*  build AI, but I do think as a first approximation, it illuminates aspects on how the human brain
*  works and things that are at least are different than how existing AI systems today are functioning.
*  Cool. Okay. Well, I want to get into each of the five breakthroughs in just a second,
*  but one thing that did jump out to me in reading the book and also watching some of the other
*  interviews that you've done, which have some of them been great and definitely recommend folks
*  going deeper down the Max Bennett rabbit hole than we'll be able to do today.
*  But throughout the book, one thing that you might expect to find, which you don't find,
*  is a definition of intelligence. And I wonder, like that would seem like a good starting point.
*  You obviously skipped it. So why do you think we are maybe better off avoiding
*  trying to define this term at all? Yeah. So it's a good, I've gotten that question a lot.
*  So it's possible in retrospect, I should have spoken to it more. I'll give you my reasoning.
*  My reasoning was when I cataloged all the existing definitions of intelligence,
*  you know, some of the preeminent experts in the field define intelligence meaningfully differently,
*  but there are different definitions of intelligence. Don't lead them to approach
*  the research agenda any differently. And so what to me that means is intelligence is this concept
*  that we all have intuitive understanding for what we generally are interested in studying.
*  But once we try to pigeonhole into a specific thing, it doesn't the value of that. It's very
*  hard to pigeonhole into one definition. And then there's not much fruit from that because we're
*  still going to be studying the same sort of topic. So, you know, I had a great conversation with
*  Brit Cruz about this where he defines intelligence as learning. And I think that's a reasonable,
*  you know, if it's like intelligence is learning. And I think it's a reasonable
*  definition to go with. But I don't know if it changes anything if you go with that definition
*  versus, you know, Feifei's definition, which is a much broader one around some, an agent that can
*  deal with challenges and solve problems in a changing environment. You know, you could,
*  you could fathom an entity that could solve the latter without having any learning. And so
*  I kind of avoided it because I didn't think it would change the story much. But and I don't
*  think I have like a definition that I find satisfying. Interesting. Well, I do think that's
*  a you know, I do think there's a lot of time wasted, certainly debating definitions and debating
*  from definitions. So I can certainly see some possible wisdom in just kind of skipping
*  that step. And I do also think that one of the things I've learned from AI is just that there's
*  a lot of weird stuff out there, you know, so you can kind of blind yourself in some ways if you,
*  you know, we have these I see these debates all the time, like, you know, does it really does
*  it understand? Does it really understand? You know, so that seems to lead nowhere.
*  I do think it brings up something maybe deeper, where, you know, there's a little bit of a schism
*  where I think I would fall on one side of the schism where, you know, is there going to be
*  an artificial general intelligence? Is there a single principle on which intelligence in general
*  will emerge? Or are we actually going to wake up in a decade or two decades and realize that there
*  really was no such thing as a GI? There's different degrees of generalization that occurs across tasks,
*  sure. But all entities are specialized for specific suites of tasks that they're going to face.
*  And I kind of more fall in the latter category, which Jan Lakoon talks about. And so what I think
*  that kind of means is when we talk about intelligence, what we're talking about 80%
*  of the time is we want something that feels very human like, that sort of what we're pursuing.
*  And when we mean something human like what we're actually talking about is a suite of capacities.
*  It's not really one capacity that we're trying to recreate, not only because we think it can benefit
*  humanity, but because we're really interested in understanding ourselves. And so my hunch is that
*  we're going to end up realizing that there really is no one panacea AGI. There's some general
*  principles that we can probably apply, but we're going to have intelligences that are specialized
*  to certain domains. Well, let's get into the kind of main structure of the book itself. So as the
*  title promises, you've got five breakthroughs. I will just give the one word label for each one,
*  and then we can kind of unpack each in terms. So the five breakthroughs, number one, steering,
*  number two, reinforcing, number three, simulating, number four, mentalizing, and number five,
*  speaking. So let's get started with steering. We're going all the way back to the age of small worms
*  and they're figuring out some of the most basic stuff. So tell us that the story of that first
*  breakthrough. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans, collected
*  anonymously, of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up-to-date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer-first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data sourcing and more
*  human representative data sets. Try the Brave Search API for free for up to 2000 queries per
*  month at brave.com slash API. Real quick, what's the easiest choice you can make? Taking the window
*  instead of the middle seat, outsourcing business tasks that you absolutely hate. What about selling
*  with Shopify? Shopify is the global commerce platform that helps you sell at every stage of
*  your business. Shopify powers 10% of all e-commerce in the US, and Shopify is the global force behind
*  Allbirds, Rothy's, and Brooklyn and millions of other entrepreneurs of every size across 175
*  countries. Whether you're selling security systems or marketing memory modules, Shopify helps you
*  sell everywhere, from their all-in-one e-commerce platform to their in-person POS system. Wherever
*  and whatever you're selling, Shopify has got you covered. I've used it in the past at the companies
*  I've founded, and when we launch merch here at Turpentine, Shopify will be our go-to. Shopify
*  helps turn browsers into buyers with the internet's best converting checkout, up to 36% better compared
*  to other leading commerce platforms. And Shopify helps you sell more with less effort thanks to
*  Shopify Magic, your AI-powered all-star. With Shopify Magic, whip up captivating content that
*  converts from blog posts to product descriptions, generate instant FAQ answers, pick the perfect
*  email send time. Plus, Shopify Magic is free for every Shopify seller. Businesses that grow,
*  grow with Shopify. Sign up for a $1 per month trial period at Shopify.com slash Cognitive.
*  Go to Shopify.com slash Cognitive now to grow your business, no matter what stage you're in.
*  Shopify.com slash Cognitive.
*  Yeah, so 600 million years ago, the world was a really fascinating place if you woke up and
*  you were navigating around the world 600 million years ago, there was really no life on land. So
*  if you looked at earth from space, it wouldn't be green. There were no trees yet. And pretty much
*  all of life was in the oceans. And most life was single cellular, but there were some multicellular
*  organisms starting to emerge. And the three branches of life had sort of already, the three
*  branches of eukaryotic life, which is the life that we're made out of, these really complex cells,
*  had already sort of branched off. There was the fungi lineage, there was the animal lineage,
*  and there was the plant lineage. And so we don't really have a great understanding of what fungi
*  looked like back then. But there's some evidence that there are sort of mushroom like structures
*  under the ocean, probably quite small. There were some plants like structures in the ocean,
*  probably close most resembling like seaweed of today. And then there were animal structures.
*  And there's so much debate about what these early animals look like, we don't know for sure.
*  But most evidence suggests that these really early animals were most akin to today's nidarians,
*  which is a class of animals that includes sea anemones, jellyfish, coral polyps. And what's
*  interesting about all of these creatures, which some fossil evidence suggests early animals were
*  akin to is they have no brains. So they have nerve nets. So they have this web of neurons
*  that are largely implementing independent reflexes. And so if you take a coral polyp,
*  which is this like radially symmetric, if you look at a coral, if you zoom in, there are actually
*  all these independent little polyps, which have like little tentacles, and there's a little stomach,
*  and they're radially symmetric, meaning if you put a sort of their symmetric around a central axis.
*  And what is key about like a coral polyp is they're not navigating around to find food. So
*  they're not they're not pursuing food, they're not avoiding predators. What they're primarily
*  doing is they have their tentacles out in the water, and they're waiting for small clumps of
*  food to hit their tentacles. And then they grab the food in and they consume it. And what's
*  interesting about about them is they don't have a lot of cognitive capacities. Now there is
*  independent convergence. So there's some really interesting studies that suggest today after 600
*  million years of evolution, some nidarians may have like box jellyfish may have gotten a little
*  bit smarter and gotten the ability to do some lightweight navigation, etc. So so there that
*  might have happened. But I do think most would agree that these early nidarians didn't have these
*  capacities, we've tried to find things like associative learning in coral polyps, we have
*  not found them. So they can't even associate the presence of a light with a shock and then retract
*  to the presence of that light, that very basic association doesn't even occur. So the question
*  is, how do we go from this web of neurons to brains? And this is sort of the first the first
*  breakthrough, which is steering. And what's what's key about evolution, which makes evolution like
*  amazing, but then also so perplexing, is despite you getting this crazy complexity at the end of
*  600 million years, every every change needs to be selected for so evolution doesn't have forethought.
*  So I can't say, Oh, you know, would be really valuable as if we actually consolidated all these
*  neurons into this design. Because that would enable us to have all these capacities. So let's
*  just do that next generation. Now, it has to be small incremental changes that lead to a result,
*  every generation has to survive. So it's a very restraining process. So the first brain needed to
*  be simple enough to be something that could be selected upon. So it couldn't just jump from,
*  you know, coral polyp to human brain, obviously, and it needed to have adaptive value. So when we
*  look into, you know, around 600 million years ago, 550 million years ago, the first animals with
*  brains emerge. And there are some interesting features of them. One, they were little worm like
*  creatures, about the size of a grain of rice, fossil evidence suggests very, very small. And
*  unlike the animals that came before, like an I dare, and they had bilateral symmetry. And that
*  means symmetric across a central plane, which all humans are, arthropods are, all mammals are,
*  and a good organism that people use as a sort of proxy organism for the first
*  bilaterian, which is the class of animals with bilateral symmetry, which is the first class of
*  animals that have brains, are nematodes. They're very small, worm like animals. And so the most
*  classic nematodes, the elegans has 302 neurons. I mean, it has like, it's like a hopelessly simple
*  brain, but we've studied nematodes deeply, and they have a credible suite of cognitive capacities.
*  And so the question is, what did this first brain do? So why did this first brain emerge? Why do we
*  go from nerve nets to this consolidated sort of brain center or head of these animals? And if you
*  look at a nematode and compare it to sort of a coral polyp, there's a few things that would
*  obviously immediately emerge. First is it's moving around a lot. So the strategy of a coral polyp,
*  which is weight for food, is very different than a nematode strategy, which is I'm going to go
*  pursue food. And what's interesting about a nematode is it does a remarkably good job of finding food
*  and getting away from dangers, but it doesn't see anything. I mean, if you look at the sensory
*  apparatus of a nematode, it is hopelessly simple. It doesn't have eyes, lens-shaped eyes. It just has
*  a very basic suite of neurons for detecting certain smells. I mean, detecting the presence
*  of light and some very basic sensory neurons for detecting pressure and touch. And yet it does a
*  phenomenal job finding food. And so the way it does this is with a technical term is called
*  taxis navigation. I call it steering just for to be cute. But taxis navigation is this idea that
*  you don't actually need to understand the structure of the world to find things. If you have gradients
*  of sensory information that you can pursue. So smell is a good example. So if you place a little
*  morsel of food in a pastry dish, it creates a smell gradient around it, which is just a feature
*  of how the physics of chemicals diffuse within fluid, where the presence of the smell chemicals
*  will be in higher concentration the closer you go to the origin. And so these early bioterians
*  look at a nematode actually realize I can solve the navigation problem, how to find food without
*  this jump to a rich sensory apparatus. If all I do is implement a very basic algorithm, which is
*  when I make an action that detects an increasing concentration of food smell, just keep going in
*  that direction. When I take an action that detects a decreasing concentration of a food smell term.
*  And so this very simple algorithm of steering or taxes navigation enables them to turn away and
*  get away from dangerous predator smells and get towards food smells without understanding anything
*  about the structure of the world without understanding without any sensory apparatus that
*  enables me to detect objects and recognize objects or any of that. But in order to do this, you need
*  a brain. You need to get to the point where there's a consolidated nucleus of neurons because you need
*  to make trade-offs. Now you can't have distributed web of reflexes. For example, a nematode is going
*  to face competing inputs. So one of my favorite nematode studies is they put a bunch of nematodes
*  on a Petri dish where they put food on one side and they put a copper barrier in the middle and
*  nematodes hate copper. Now what they found is they will readily make trade-offs between do I cross
*  this dangerous copper barrier, which is toxic to them to get to the other side to get food.
*  And it depends on two things. One, the relative concentration of each of these, the higher the
*  concentration of the food, the more willing they are to cross into how hungry they are. So they
*  incorporate their internal signals. The more hungry they are, the more willing they are to cross the
*  copper barrier. So in order to do this, I need to integrate two different sensory neurons. One that
*  detects bad things that triggers turning and one that detects good things that triggers forward
*  momentum into some central nucleus. So I can make a single choice as to what is my movement. So yeah,
*  so the idea is, which is not really particularly novel, I think most people in the field,
*  would agree with the general idea that taxes navigation was probably the movement algorithm
*  implemented by the first biolaterians. And from taxes navigation came several principles of
*  intelligence on which the rest of the brain evolution ensued, which is why I think it's so
*  interesting. First and foremost is this notion of valence, which in the AI community, people would
*  just call it reward. I wouldn't call it reward yet and biolaterians, but the idea is you classify
*  things in the world into good and bad. So in order to implement the algorithm of taxes,
*  what you need to do is say there are certain stimuli that I deem good and there's certain
*  stimuli that I deem bad. They directly map to a certain movement repertoire, which is turn towards
*  or turn away from it. If you look at an ematode, what's so interesting is the sensory apparatus
*  directly signals valence, which is not like a human. So this is where you can start seeing
*  simplicity become more complex. When I show a human, a stimulus that neurons in your eye
*  do not directly encode the valence of that stimulus, whether or not you deem it good or bad
*  or rewarding happens deeper in the brain. But when you look into an ematode brain, that's not the
*  case. They have neurons that detect food smells. These neurons directly map to neurons that trigger
*  forward momentum. So the, the, the effectively it's evolutionary hard, evolutionarily hard coded
*  what things are good and what things are bad. It's not learned over the course of their, their life.
*  Now they can change the relative weights of good and bad things based on learning, but there's a
*  very strong bias that's implemented. So that's the idea of tax navigation from taxes navigation
*  comes valence and this notion of reward. There's also something called affect, which is sort of
*  the basic template of emotions that emerged with nematodes. This is part of the book that I find
*  really fun to learn about where if you also look at how a nematode navigates,
*  there's another complexity that emerges. So what I told you is actually not exactly correct. When I
*  said that you put a morsel of food and it creates the smell gradient, that's true in a Petri dish.
*  It's not true in the real world. If you actually look at smell gradients in the real world,
*  the problem is there's a lot of noise because there's a lot of other noisy smells that occur
*  and there's lots of currents. So if you actually look at a smell plume from a source, it's actually
*  very noisy. It dissipates not in a clean gradient. It's like sort of wifting around and that creates
*  a problem because if you actually implemented exactly the algorithm I suggested, it wouldn't be
*  very effective because it's very common that if a nematode passed an area rich with food,
*  it wouldn't get a consistent smell gradient leading them to the source of that food.
*  So what nematodes do is they actually have what people in the field would call behavioral states,
*  which I think maps very nicely to what people who study other types of animals would call
*  affective states, which is a behavioral repertoire triggered by a stimulus, but persisting beyond
*  the presence of that stimulus. So nematodes have dopamine neurons that unlike us actually have an
*  apparatus that sticks outside of the body of the animal. So our dopamine neurons don't have direct
*  access to the external world. They're deep within the midbrain of a human and they only get information
*  from other parts of the brain. The nematode, which perhaps is suggestive of how dopamine
*  evolved in early biolaterians actually detects things outside of the worm. And what dopamine
*  neurons detecting the presence of food. And so what happens is when a nematode passes a patch of
*  food, it floods the brain with dopamine, which triggers a persistent state of what people call
*  dwelling, which is local area restricted search. And so what this means is it's a clever, relatively
*  simple mechanism for saying, if I detect food, it is a feature of the world that it's probably
*  likely there's other food nearby. And that's, that's, that's evolution taking advantage of a
*  feature of how the structure of the, our world works. That's not necessarily the case, but in
*  our world that happens to be a case. So a clever algorithm is to say, if I detect food, a food smell,
*  I'm going to continue doing local area restricted search for some period of time until I find other
*  food. I mean, so dopamine is a mechanism for triggering this sort of state of dwelling or
*  exploitation or seeking, which we see dopamine doing in early biolaterians and then persisting
*  through a whole, our whole lineage, which is cool, I think. And there's serotonin neurons that detect
*  food in the throat of a nematode, which generates a state of rest and satiation. In other words,
*  after consuming food, it's the thing that makes the, the, the nematode pause and say, okay,
*  I've consumed enough food. So this basic dichotomy between dopamine and serotonin, obviously it's
*  been complexified over 600 million years of evolution, but we see that very basic template,
*  which is dopamine is the seeking pursuit chemical and serotonin is the satiation delayed gratification
*  chemical. So, so I guess one more analogy before we can jump to a breakthrough too, is you see this
*  algorithm also implemented in things like the Roomba, right? So Roomba, which is the sort of
*  robot that goes around and does vacuum cleaning around your house, I think has some cool analogy
*  as to the early biolaterians because Rodney Brooks did, who also kind of has an evolutionary
*  lens on building autonomous systems, built the simplest possible robot, which is, and it's akin
*  to the biolaterians since that it actually modern ones do build a map of your world of your home,
*  but early ones did not build any map. All it would do is detect if it hits something and then it would
*  turn randomly, which is akin to taxes navigation. But what they did is they realized that a problem
*  with the Roomba is it wasn't taking advantage of detecting dirty things and cleaning up the whole
*  area. So it was taking too long. So they implemented something called dirt detect, which is almost
*  exactly how dopamine works in biolaterians. If a Roomba detects dirt, it actually stops its normal
*  behavioral repertoire and starts turning in a local region. And the reason is because it's likely the
*  case if it runs into a patch of dirt on the floor, there's other patches of dirt nearby. So it's the
*  same exact basic principle on which sort of dopamine started. So this is what the sort of
*  the first brain did. And I'll pause there if there's anything. I know I just did a bunch of
*  talking at you. Is there anything? Yeah, you want to add or ask? Hey, we'll continue our interview
*  in a moment after a word from our sponsors. If you're a startup founder or executive running
*  a growing business, you know that as you scale your systems break down and the cracks start to
*  show. If this resonates with you, there are three numbers you need to know. 36,000, 25 and one.
*  36,000. That's the number of businesses which have upgraded to NetSuite by Oracle. NetSuite is the
*  number one cloud financial system, streamline accounting, financial management, inventory,
*  HR and more. 25. NetSuite turns 25 this year. That's 25 years of helping businesses do more with less,
*  close their books in days, not weeks and drive down costs. One, because your business is one of a kind,
*  so you get a customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins. Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free at netsuite.com slash cognitive. That's netsuite.com slash
*  cognitive to get your own KPI checklist. netsuite.com slash cognitive. Omniki uses generative AI to
*  enable you to launch hundreds of thousands of ad iterations that actually work customized across
*  all platforms with a click of a button. I believe in Omniki so much that I invested in it and I
*  recommend you use it too. Use Cogrev to get a 10% discount. Yeah, that's I mean, it's a great
*  foundational overview. Do I recall correctly that there are sort of neurons that encode these like
*  somewhat higher order concepts in the brain or is that not there yet? I'm kind of making an analogy
*  in my own mind to interpret ability work on AI systems where people will go in and try to identify
*  sort of higher order concepts, right? And I had thought that there were sort of internal neurons
*  that kind of fired for keep going or, you know. Totally. So there's the people in the nematode
*  community who call them inter neurons. But yes, so there's their sensory. So the sensory neurons
*  that detect sort of positive valence things, negative valence things in the nematode, which
*  all connect to downstream neurons in the brain, which then mutually inhibit each other. So there's
*  and I'm simplifying slightly, but there's neurons that in general code for forward momentum.
*  And there's other neurons that in general code for turning. And these through a somewhat complex
*  web end up mutually inhibiting each other. And those connects to downstream neurons that control
*  sort of the locomotion motor program and nematodes. So yes, there are sort of intermediary neurons,
*  which is important because what you need is to integrate inputs from multiple positive valence
*  neurons and multiple negative valence neurons and eventually get to the point where you're making a
*  single choice. So yes, there are intermediary neurons for sure. Yeah. OK, cool. So even there,
*  you can kind of see, you know, the beginning of an analogy to even a transformer, you know, which is
*  many, many more neurons, but the same kind of structure of like the input layer that sort of
*  works up into these higher order concepts in the middle layers and then cash out to some behavior
*  on the other end. It only takes 302 neurons in a brain to have like an early form of that, which is
*  pretty amazing. I would say let's keep going. So breakthrough number two is reinforcing.
*  Tell us that story. So OK, so if you fast forward around 50 million years from when the first
*  bilaterians were sort of swimming around the seafloor, you enter the Cambrian period. And
*  probably many listeners are familiar with the Cambrian explosion. And this is where you get
*  this massive diversification of life. And for the most part, it's bilaterian life. So the explosion
*  of life that occurred during the Cambrian period are the ancestors of our bilaterian ancestors,
*  or the ancestors, the explosion of life you get descend from our bilaterian ancestor. And most of
*  the dominant species during the Cambrian period are actually arthropods, which are the sort of
*  class of animals that include things like insects. Insects had not emerged yet, spiders,
*  crustaceans. And so vertebrates, these are the invertebrates, vertebrates, which we are,
*  the animals with a vertebral column, were sort of small in general, middle of the food chain creatures.
*  And they resemble most resemble the modern fish. And these were our ancestors. So within this sort
*  of explosion of huge arthropod predators, and some of them are massive, like the size of a human,
*  and there was a little fish like ancestor that was sort of swimming around. And this fish like
*  ancestor evolved the very basic template of the vertebrate brain. And what I found actually most
*  fascinating when I started going back and reading about all this is most studies on comparative
*  psychology, and really neuroscience in general are done on mammals. So there's, you know, rats are
*  sort of the mainstay of neuroscience research. And there's some work done on fish, but it's,
*  you know, a very small minority. But when you look at all vertebrate brains, if you want to know
*  about the human brain, the fish brain kind of gets to you 70% of the way there, because the fish
*  brain has the very basic templates of all vertebrate brands, they contain a forebrain,
*  a midbrain, a hindbrain, the very basic substructures that maybe listeners have heard about
*  for there's a cortex in a fish that gets sensory information and recognizes patterns it projects
*  to the thalamus and the basal ganglia, which work in largely the same way. There are midbrain
*  structures for dopamine, like all of the basic the basic template of how vertebrate brains work,
*  you find in a fish. And so what was going on in this very early brain, I think we can get insight
*  from by looking at non mammal vertebrate brains. Mammal brains have some very unique structures
*  to talk about in Breakthrough 3. So in the vertebrate brain sort of templates, some of the most
*  important structures that you see are something called the cortex and something called the basal
*  ganglia. And what is not as appreciated, I think, and sort of the neuroscience community writ large,
*  is that there is a cortex in fish brains. So a lot of people think about how the cortex evolved
*  only in mammals, but there is a cortex in fish that performs somewhat similar processes, it gets
*  similar types of projections back and forth between the basal ganglia and the cortex. And so what are
*  all these things doing? Well, if you look at what a fish is capable of doing, one of the most
*  obvious things that it can do is it can learn from trial and error way better than a nematode could.
*  So you can just go on YouTube and watch people train fish to do crazy things. You can train a
*  fish to jump through hoops, you can train a fish to navigate through a maze, and you cannot train
*  a nematode to do any of these types of tasks. And one of the interesting things about looking
*  into the very basic template of a vertebrate brain is you start seeing the reward signal,
*  which, you know, doesn't really exist in the same way a nematode, now becoming dopamine. So
*  I'm going to go back in time to the early 20th century, where we were really going, we're
*  starting to learn about learning theory in general, this is Guy Edward Thorndyke. And
*  he originally wanted to study human learning. And he couldn't get the school the his sort of
*  program to let him study human children. So he ended up studying chickens instead. It's a really
*  funny story. But he thought, you know, in general, he was a starch Darwinist, he was like, Okay, if
*  we can find the principles of how simple animals like cats and birds learn, then maybe it applies
*  to human children. And what he originally was looking for was, can we teach these animals
*  through imitation learning? So he wanted to find a notion of insights and imitation. So the way he
*  set this up is he created these puzzle boxes, which are these famous studies that he did.
*  And he would put like a cat in this cage, put some food outside of the cage that they were
*  obviously motivated to get to. And there would be some very basic contraption in the cage that if
*  the cat did the right thing, the cage would open, they get the food. So sometimes it'd be a latch
*  that if they pulled the cage would open, sometimes he would just sit there and watch and if they licked
*  a certain paw, he would open the cage. So effectively, there was a puzzle they had to solve.
*  And so he was expecting to find two things. The first was that when they figured out how to do it,
*  the time to get out would immediately go to zero. This was his notion of insight. In other words,
*  once you figure out the puzzle, then you never need to someone else to tell you how to do it again.
*  And the second thing he thought he would find was imitation learning. So if you put another animal
*  in front of them who had already figured out how to do it, they would become faster. And at least in
*  his studies, he didn't find either of those things. But what he did find is there was a progressive
*  decline, almost like steady curve of them figuring out how to get out of the cage. And so he thought
*  about this effect. He called this the law of effects, but really just trial and error learning,
*  which he realized when animals do is they just try a bunch of random things, and they become
*  on average, more likely to do the things that that worked, and less likely to do the things
*  that did not work. In other words, after I get out of the cage, it reinforces the prior behaviors that
*  I took, and makes them more likely to occur. So it's not insight in the sense of, oh, I figured out
*  the puzzle. But it's making me more likely to take behaviors I just did before. And over time,
*  eventually the time it takes to get out of the cage went to zero. So he came up with this idea
*  of like, man, I wonder what portion of learning is just trial and error learning. And then this guy,
*  BF Skinner ended up taking this to the extreme and tried to claim that all learning across all
*  animals was just trial and error learning, which has been proven to be false, which we'll get to
*  in breakthrough three. But the interesting insight is a surprising quantity of behavior,
*  intellectual behaviors is in fact trial and error learning. And so this is where the second
*  breakthrough with reinforcement learning comes around. Because if you look at fish,
*  the same sort of puzzle experiments can be done on fish and they learn in exactly the same way.
*  So Thornebeck actually did this because he did, he was interested in studying fish. You can put a fish
*  in a tank and you can put these, these sort of walls in the tank with certain areas where they
*  can swim through. So the only like certain sections they can get to, and then you make one area light,
*  which they don't like, and one area dark, they do like, and see how long it takes the fish to get
*  through the puzzle. The same exact thing will happen at first takes them a long time, then it
*  takes them slightly less. And eventually they do it immediately. If you take a nematode, you don't
*  see this happen. You cannot train a very basic biolaterian to learn through trial and error in
*  this way. So something happened in the jump from biolaterians to early vertebrates. And so this guy,
*  so this is where AI actually is a really fascinating part of the story. So we have tried
*  to implement algorithms the way that Thornebeck believed that reinforcement learning worked,
*  which is when a good thing happens to reinforce recent behaviors. So Marvin Minsky, I think it
*  was in the fifties, he creates something called SNARK, which I forget exactly what it stands for,
*  stochastic neural analog reinforcement calculator, I think, which is a very basic algorithm that was
*  trying to learn how to teach something to get out of a maze, a very basic little AI agent to get out
*  of a maze and just reinforce it whenever it succeeded. So the idea was, Hey, let's take the
*  idea that Edward Thornebeck had applied to an AI system and watch it learn through trial and error.
*  Does not work. And the reason that doesn't work is because of something called the temporal credit
*  assignment problem, which is most actions that lead to good rewards are not directly proximal
*  to the reward. And so a good analogy would be a game of chess. When you play chess with someone,
*  the things you took, the actions you took that led you to win are not necessarily the actions,
*  the very end of the game, the things that might've won you, the game might've been in the middle of
*  the game. And so when all you do is just reinforce the recent behaviors, you don't end up getting a
*  very intelligent smart agents. And if you try and reinforce all the behaviors, it takes way too long.
*  You need way too much data to actually get it to learn how to play a good game of chess.
*  So this was a huge problem for decades in AI where we could not figure out how to get trial
*  and error learning to work and which when it eventually was discovered, which I'll describe
*  in a second, it actually ends up illuminating how vertebrae branch work. As we can see very
*  similar algorithms being implemented. So this guy, Richard Sutton came up with this brilliant idea
*  where maybe the way that trial and error learning works is we don't reinforce ourselves when we get
*  the actual reward. The reinforcement signal comes from changes in predicted reward. And so it's this
*  idea that when you're playing a game of, of chess, there's actually two opponent processes
*  happening. There is one process that's trying to predict what's the best next move, but then there's
*  a separate process that's trying to predict how good is my current state? How likely am I to win
*  another way of just saying what's my expected future reward? And his idea was maybe the reward
*  signal that trains the system, the policy network, which is the network that's deciding what move to
*  take is not when you win. It's the expectancy of the move you just took increased the likelihood
*  of winning substantially. So we, there's some intuition here, which is when you're playing a
*  game of chess and when you make a move, we were like, Oh man, my position just dramatically improved
*  that feeling that rush. That's the reinforcement signal. And so, uh, his idea of temporal
*  difference learning, which is the idea of the reinforcement signals, temporal differences,
*  changes and expected future reward is actually what reinforces brains. This is the insight that
*  unlocks or the reinforcement learning revolution. So the first sort of practical application was
*  something called TD Gammon, where this principle is used to make backgammon games work really well.
*  It has since been applied to far more complicated games like chess and checkers, et cetera.
*  So this is this idea that man, the way to get reinforcement learning to work is you need to
*  have an ongoing prediction as to what the likely future award is. Okay. So now we go back to fish
*  brains, which are eminently capable of learning through trial and error. And we look at the
*  structure called the basal ganglia, which is one of, I think the coolest parts of the brain. I won't
*  bore people with the nuances of how it works, but if you're interested in like neuroanatomy,
*  I think learning about how the basal ganglia works is one of the most tantalizing structures
*  because for two reasons. One, it is a beautiful mosaic structure. So the way it works is like so
*  clear versus if you look at a place like the neocortex, it's a complete mess. It's very hard
*  to decode what's actually happening. And then two, it's incredibly conserved across animals.
*  The basal ganglia in a fish works almost exactly the same way as the basal ganglia in a human.
*  And so no one knows exactly what it's doing. But there's some pretty strong theories that
*  is implementing something quite akin to Sutton's TD learning algorithm, because what we see is this
*  mosaic in the basal ganglia between circuits that attach to the brain stem motor system,
*  that bias actions in one way or another on the basis of dopamine bursts. So when it gets dopamine,
*  it becomes more likely to do an action. And when it gets a decline in dopamine, it becomes less
*  likely to do an action. And we actually know the exact circuitry for how that happens.
*  There's a mosaic within the basal ganglia that projects back to dopamine neurons that seems to
*  trigger increases in dopamine and also pause dopamine signaling. In other words, reinforcing
*  and punishing itself based on its expectation of future award. So there's a lot of people that have
*  done some modeling and tried to map the neuroanatomy of basal ganglia to Sutton's idea of TD learning,
*  still open area of research, but there's a lot of evidence to suggest that what it's doing is
*  something quite similar to this. And when you record dopamine neurons, this is the best evidence
*  for this. And this hasn't been done in fish, but if you do it in monkeys or mice, dopamine neurons
*  seem to signal almost exactly the TD learning signal. So what you see is phasic dopamine. So
*  big bursts of dopamine excitement occurs not on reward delivery, but on changes in expected future
*  reward. So if you hook up the dopamine neurons within a monkey, when a cue appears that it
*  thinks is predictive of a future award, that's when it gets a big burst of dopamine, not when
*  you actually give it the reward. And that actually was a big perplexing finding in neuroscience until
*  people realized that Sutton's TD learning works in practice and they realized, well, this is a new
*  interpretation of what dopamine neurons are doing. So if you go into a fish brain, there is good
*  evidence. We haven't recorded to my knowledge, you haven't recorded dopamine neurons directly,
*  but you have recorded the surrounding structures that do show these sort of prediction error
*  signals. In other words, it's triggering excitement when something just changed that
*  suggests you're about to get a positive reward or a negative reward. So the evidence suggests that
*  fish brains are doing this sort of same TD learning algorithm to enable them to learn from trial error.
*  What I think is so cool about this sort of breakthrough too, is it's only possible if you
*  have breakthrough one, you cannot implement a TD learning algorithm without having a grounding
*  notion of valence at the bottom of it. In other words, a notion of what is good and bad in the
*  first place. That is the baseline on which expected future rewards are built on top of,
*  because you need the actual reward signal, which only existed with taxes, navigation,
*  and nematodes, because that's what classified true good or bad things. So from this idea of
*  reinforcement, you get all these other things that emerged in vertebrate brains, because now once you
*  can learn arbitrary behaviors through trial and error, all these other things become possible.
*  For example, now it's really useful to recognize more things in the world, because that enables
*  me to have more complex suites of actions I can take on the basis of way more things I could
*  recognize. So the cortex is one of the structures that evolved in early vertebrates that seems to
*  do things like pattern recognition. Some fish can recognize human faces. So they're very,
*  very good at pattern recognition. Another thing that emerges in early vertebrates is a map of
*  3D space. A simple study for this is if you have a grid of let's say 25 different containers,
*  the only cue for where you are in this map of space, let's say one side of the wall of this
*  tank maybe has like a blue dot. So you can you wherever you're placed, theoretically,
*  you have sufficient information to build a map of the space. And let's say you put a morsel of
*  food under one of these containers, an arbitrary place in this grid of 25. Eventually, a fish will
*  find that location. If you put a fish back in the tank without any food, it will go right back to
*  the same location, irrelevant of where you place it. And so this is not, and this is an interesting
*  biological tweak on standard reinforcement learning agents. It's not actually just learning
*  the suite of egocentric actions to take. In other words, what move do I turn right or left in
*  response to a cue? It has something a little more advanced, which is given my location in 3D space,
*  what is a homing vector to a another location that I would like to be? And so that's a much
*  more effective way to engage in trial error learning, because it's much more robust to
*  changing and changing starting locations and all that. So you can go into a fish brain,
*  you can see the homologous region of the cortex, which ended up evolving into our version of the
*  hippocampus, which seems to encode locations in 3D space, which is just a useful tool, which will
*  end up mattering for breakthrough three. So yeah, so with vertebrate brains, you get arbitrary trial
*  and error learning with the basal ganglia, you get the cortex, which can learn arbitrary patterns,
*  which enables the basal ganglia to learn more complex behaviors, because it can recognize more
*  things in the world. Any questions on that? So the questions I have following up on this
*  reinforcement, I guess one is just kind of an observation that we do see this dual model pattern
*  across a number of different places in AI specifically, right? Like the GAN
*  architecture is not exactly this, but it's a similar thing where you've got the generator
*  and the discriminator and they kind of bootstrap together to hire capability. More certainly to the
*  frontier models of today, the reinforcement learning from human feedback is predicated also
*  on a reward model that is going to score something with its estimate of what a human would score it
*  as. And then by applying that to outputs, now you can reward the better outputs from the core model.
*  So those are both interesting. Also, the rewarding incrementally along the way has become a big
*  trend that was key to, and I think it's probably used in many places, but one that stands out to
*  me is OpenAI's result from, I think like first, maybe second quarter of 2023, where by rewarding
*  reasoning incrementally through the process of mathematical problem solving, they're able to get
*  language models to do much better on math by just kind of giving a lot finer grained reward
*  signal step by step, rather than just saying like, did you get it right or wrong at the end
*  and rewarding that? I think that is kind of sparse reward problem or like just sparse,
*  you don't get many rights. So how do you kind of get it on the right track when basically it's
*  wrong all the time in the early days? They had this problem with web agents too, when they started
*  off trying to do a web agent some years ago, they basically just found like, we're not getting any
*  positives. So we have nothing to reward. And so it kind of didn't work, but rewarding
*  incrementally earlier definitely seems to be a big trend toward more reliable performance.
*  So those are just some reference points, triggers in my own mind that I think I can kind of
*  understand a little bit better in light of this history. The other big thing that I'm kind of
*  wondering, this is maybe a question we could ask across all five breakthroughs, but particularly
*  here, I'm thinking, okay, there seems to be like a cluster of breakthroughs, and there's a lot of
*  discussion right now in AI too about the notion of emergence, which is to say, you know, and there's
*  a lot of definitional questions about emergence as well. So without necessarily trying to provide
*  the proper definition of emergence, one candidate definition is that certain capabilities come
*  online suddenly. And so, you know, we can look at like loss curves and say, you know, the loss curve
*  is kind of dropping smoothly, but sometimes these individual capabilities seem to come up
*  comparatively much faster. And there's a lot of debate as to, you know, whether that's exactly
*  happening. And maybe if you look at it the right way, you can still find a smooth loss curve for
*  a lot of these things, et cetera. But I guess I wonder like, how sharp do you think these breakthroughs
*  are? Do you have a mental model for one thing happened and it unlocked these other things?
*  But, you know, because I could, you could also say, well, 3D spatial model modeling sounds like
*  a pretty good candidate for a breakthrough, right? So I think this was the task of, this is why I look
*  at the whole book as a first approximation, because it is clearly the case that all of these were
*  broken down into small incremental generation by generation changes. It was not the case, of course,
*  that a nematode, two nematodes had a baby and then a fish was born, right? So the goal is to,
*  which there is some almost some tastes that comes into this where other people could have
*  different tastes and look at the same story and say, I think I would look at this as seven
*  different steps as opposed to five, or I would look at this as three steps. And I think all could be
*  equally right. It's a trade-off between complexity and predictive power, right? And so I think 3D
*  spatial modeling may have emerged at a separate, at importantly separate time period. We are,
*  part of this taste is constrained by the evidence we have available today. So for example, we don't
*  have good existing animals that show the gradual developments between nematodes and vertebrates.
*  There's only a few chordates still alive, which are non-vertebrate, of course, in other words,
*  non-vertebrate animals that are not yet in not exactly invertebrates. So like in this middle
*  ground is very few of those animals alive. And there's not a lot of comparative psychology studies
*  on them. We don't have really good comparative psychology studies on the most primitive vertebrae,
*  which is the lamprey. So we don't, I have, I've tried tirelessly to find this. I don't think we
*  even know if they have map-based navigation. So it would be a fascinating finding if we found that
*  a lamprey is incapable of knowing the locations in space, but a teleosed fish is that would suggest
*  that there was an important milestone that occurred between the first vertebrates and the
*  first jawed vertebrates as an example. So the point is we're constrained a little bit on trying to
*  come up with the first approximation that gives us a basic understanding of the steps by which
*  things evolved without adding so much complexity that we lose the intuition. The goal is a first
*  approximation, not exact accuracy. And we're also constrained by the evidence we have available,
*  which is we don't have rich comparative psychology studies across all of these diverse species.
*  And many of the animals that would show us the gradual development of brains are died out. So we
*  don't even, we don't have modern animals that show what these intermediary steps would be,
*  but you're absolutely right. You know, the basal ganglia clearly evolved in steps. The cortex
*  evolved in steps. You know, these things probably did not all emerge all at once, 100%. But I do
*  think there's insight to be garnered by even looking at the clustering of within this 50 million
*  a year window, you get all of these things coming at similar times. And I think there is insight to
*  garner about how do these things actually relate to each other? And what I found so interesting
*  about writing the story in the book is made is often the case, not always, but often the case
*  that suites of new abilities that seem to emerge a given lineage tend to come from common and similar
*  underlying neural structures and algorithms. And that's really interesting because what seems like
*  very different things are actually different applications of the same sort of sort of a
*  technique. And I think this actually emerges far more with breakthroughs three and four,
*  where you see that a lot of the new abilities that emerge in mammals are in fact, or could be
*  conceived as different applications of really one new algorithm or new ability that emerged
*  invertebrates a little bit harder because it's like very differing types of ability,
*  like map-based navigation, pattern recognition, and trial and error learning. But those are all
*  very interrelated. For example, pattern recognition is not relevant unless you have trial error
*  learning. If you don't have the ability to learn that this arbitrary pattern is something I should
*  do this behavior to, then it's not going to be particularly useful to be able to recognize a
*  pattern unless I have some clever mechanism to map the recognition of this thing to what behavior
*  should I take in response to it. They are related. It's also not very useful to have arbitrary trial
*  and error learning unless I can recognize rich things in the world, because I'm constrained to
*  the tiny amount of sensory neurons and a nematode, this deep, very expensive brain to learn to take
*  arbitrary behaviors where I can't even recognize much about the world at all. It's probably not
*  that relevant. It's probably cheaper to just toss that away and stick with a simple low-energy brain
*  that can't do that. You can see why these things benefit from each other. But yeah, definitely
*  did not happen where one generation emerged and then all these abilities were there.
*  Yeah. Help me understand that just a little bit better. This may be a, probably is, I mean,
*  there's a lot, obviously, of major divergences between the biological intelligences and the
*  artificial intelligences. But I could imagine, especially taking a little bit more of an AI
*  lens on things for a second, if I go back to the worm, I could imagine bolting a convent detector
*  onto the side of it that would pattern match on a predator or something and feed that signal into
*  the rest of the system to say, get the hell out of here, because I just recognized the face of a
*  predator or something. Now that may just be implausible to develop. Obviously, these are
*  small things. They don't have a lot of luxury of carrying around extra weight. But it does seem
*  like you could have value in these detectors, higher order detectors still without the
*  reinforcement. But I might be missing something there. I suppose we did that. I think what you
*  would suffer from is the same problem that Minsky had with his snark. So if you don't have the
*  ability to reinforce yourself on the basis of changes and expected future reward, it's not so
*  clear that you're going to end up having intelligent behaviors emerge. Because if I can recognize
*  something and the only way I'm learning about it is whether something good or bad happened within
*  a small window of two seconds. I mean, the nematode, simple bilaterians, their associative
*  learning is constrained to effectively a two second window. So they can make associations between
*  a bright light and something bad happening. So they get a tap to their side or something painful.
*  And then they are more likely to recoil and turn away from that light in the future, but has to
*  happen within two seconds. So contingencies beyond that two seconds are not learned because they
*  don't have this arbitrary reinforcement trial and error system. So maybe it would be valuable, but
*  this is now we're into energy trade offs, which is how valuable is it to be able to have this
*  convent that maps to turn towards or away when all you can do is make a mapping within two seconds
*  of something occurring relative to the energy costs of that thing. So there's maybe one outcome
*  is it's not energetically worth and that's why it didn't evolve. The other outcome could simply be
*  that it's just not evolutionarily available where some other things had to happen that are just lost
*  to time to get the brain complex enough where this type of pattern matching is even possible.
*  In other words, the reason that didn't happen is not because it wouldn't have been useful because
*  of evolutionary constraints. You needed to have a bigger body. You needed to have a bigger base
*  brain with more complex motor behaviors. Who knows what very basic neurobiology had to be there for
*  that to be an available iteration to emerge. Because the thing that's really interesting
*  about evolution is each iteration needs to be adaptively valuable or at least not adaptively
*  bad. So it's possible to have things that emerge that are what's called a
*  spandrel where it's not adding adaptive value yet, but it evolved for some other reason.
*  And then later it'll have value. But for something really energetically costly,
*  it's unlikely to emerge unless each iteration adds value. So that puts a big constraint,
*  which is you need to conceive. This is why understanding how lens shaped eyes evolved is
*  still such a fascinating thing, which is this incredibly complex structure. But what is the
*  incremental steps by which every step of the way were either neutral or positive on adaptive value.
*  So, but yeah, I think that would be my thinking around why maybe the early
*  biotarianism just add a convolutional neural network. Cool. This certainly does have interesting
*  implications for the relative evolutions of AIs versus biological systems. It just,
*  it strikes me that the separation of hardware and software is so there's a
*  possibly a distinction to be made on the biological side there too. But certainly on the
*  AI side, it's like that distinction is so complete that these questions of like,
*  does something have to be energy justified? We don't have to maintain homeostasis in AI systems.
*  There's a lot more sort of degrees of freedom and ability to kind of remix without concern
*  for these practical constraints. Which is why an interesting reason why I think it's likely
*  in the near term, at least we're going to see meaningful divergence between the way that our
*  AI systems work and the way biological brains work. And this is where I think there is a very fair
*  critique of, you know, we need to have good tastes when we take inspiration from neuroscience
*  and apply an AI because neuroscience, the way brains work as magical as they are, is a process
*  that is constrained in ways we don't need in our AI systems. For example, we perhaps have access
*  to far more energy and we're willing to be way less energy efficient. And so that means that the
*  parts of the brain that are optimized for energy efficiency, perhaps at least in the near term,
*  don't matter to us. So we're, it's not worth the like tireless effort to try and figure out how
*  brains do that. Brains also have huge evolutionary constraints. So it's very likely that's not an
*  optimal design versus when we implement things in Silicon, maybe we can find an optimal design,
*  throw away a previous design from scratch. So I think it's likely that we're going to end up with
*  AI systems that work in very different ways because they don't have the same constraints
*  that brains do. And so the taste question, which is a hard one, I obviously don't have all the
*  answers to, I have thoughts on, is what are the aspects of how brains work that are relevant,
*  which is not obvious. The goal is clearly not to recreate the human brain wholesale, but what
*  exists in the neuroscience of what we know about brains or don't yet know that we think will be
*  useful and practically relevant to building smart AI systems. That's sort of the hard question.
*  Okay, cool. Well, let's do the next three breakthroughs still. And then I have some,
*  you know, some direction that I want to take us down on some of those future oriented questions
*  too. All right. So these will, I think go faster because they're actually in some ways algorithmically
*  more complicated, but conceptually much simpler. So in mammal brains, which evolves during the era
*  of dinosaurs. So there's a really interesting story, which I won't go into. I'm like how,
*  you know, the story of how we went from fish to little squirrel like mammals is a fascinating one,
*  the series of extinction events, making our way onto land, dinosaurs emerging,
*  this whole rich history with that. But eventually around 150 million years ago,
*  we find ourselves as little four inch long mammals in an ecosystem with gargantuan massive
*  dinosaurs. We are very close to the bottom of the food chain. We're hiding in burrows, only coming
*  out at night to hunt for insects and then run back inside. But what is fascinating is inside this tiny
*  little brain evolved a new structure, an area of the cortex of early vertebrates, which is a three
*  layered structure. So if you looked at a lamprey brain and you looked at the cortex, there's sort
*  of three layers of neurons wrapped around each other. But if you look into any mammal brain,
*  from human to monkey to rat, you see a structure of their cortex, which has six layers. And this
*  is called the neocortex, which actually on the edges goes back to the old structures, which three
*  layers. So the olfactory cortex of mammals still has three layers, just like early vertebrates.
*  And the hippocampus of mammals still has three layers like early vertebrates, but this neocortex
*  area in between got really, really much more complicated. And so the question is, what did
*  this new neocortex do? And so in human brains, this is where evolution, I think, is so interesting
*  and instructive, because if all we did is study human brains, we would say the neocortex does
*  practically everything. I mean, if you go into the brain of a human, pretty much everything that you
*  consciously experience seems to occur in the neocortex. For example, if you get a concussion
*  to the back of your head, which is the visual cortex, so the neocortex is this six layer sheet
*  around the whole brain, all the folds you see when you look at a picture of a brain, that's neocortex.
*  And there's different sub regions that seem to do different things. As an example, the back
*  regions called the visual cortex. And if you get damaged, the visual cortex, people report being
*  blind. So they will say, I cannot see anything. And if you weave, they will not respond. But we
*  know that their brain is still processing visual information. For example, if you throw something
*  at their face, they will blink. If you show up a scary picture in front of them, they will report
*  feeling fear or their heart rate goes up, even though they won't be able to tell you why.
*  We know exactly why this occurs. It's called blindsight. And we know this because the
*  optic nerve goes into different parts of the brain. There's one pathway that goes through the
*  thalamus to visual cortex, which seems to be the place where we consciously experience things,
*  recognize rich objects, et cetera. There's another path that goes directly to the amygdala,
*  which is an older structure. There's a homologous region invertebrates, which is sort of like a
*  basic pattern detector, which can trigger emotional responses. So the neocortex seems to be where
*  all the complex stuff is happening that you consciously experience. But there's still lots
*  of other older regions of the brain that are doing stuff. If you go to the front part of the
*  neocortex, there's areas, there's a ring called motor cortex. If that gets damaged and in a stroke,
*  you become paralyzed. You lose your fine motor skills. There's regions in the brain that at
*  least classically have been language areas. If you get those damage, you lose the ability to speak
*  or to understand language. There's auditory areas. So when you look at the human brain,
*  it's like, man, this one structure seems to do everything. It enables complex movement, planning,
*  object recognition, all that stuff. But if you go all the way back to early mammals, if you look at
*  a rat, it's not so clear how important their neocortex is to all those things. For example,
*  you can lesion a rat's motor cortex and it can still move around just fine. The paralysis
*  associated with motor cortex damage is actually unique to primates. And I think that's a
*  fascinating finding because what it suggests is when we think about the neocortex as being able
*  to do things like what's where we control movement, there might be something more complicated going on
*  because when we go back to early mammals, it wasn't the region that controlled movement. That
*  was actually an adjustment over evolutionary time. So when we go into a rat, what is the neocortex
*  doing? Well, if you damage the motor cortex of a rat, they become unable to learn new motor skills,
*  but they can execute well-learned motor skills and they become much worse at fine motor behaviors.
*  In other words, things that require in real time motor planning, a cat becomes much less able
*  to look out at a bunch of sort of small platforms and plan its steps of its pause throughout that.
*  And so I think this is a very interesting suggestion that really what motor cortex was
*  originally doing is enabling things like motor planning. In other words, simulating your actions
*  before you do them. And this also goes to another area of research around what the neocortex is doing
*  where people think about it as a generative model. In other words, it is a model that does two things.
*  It can both recognize things in the world, but it can also generate its own samples of things in the
*  world. And so the original intuition for this came from visual allusions that were identified
*  in the 19th century, where I'm sure everyone is familiar with this. Like you can show someone
*  something that is ambiguously a cat or a rabbit or a duck, and you can only see one or the other,
*  or you can show someone like a Dalmatian set of patterns that they don't recognize. But then you
*  say, actually, do you see the dog there? And then all of a sudden I can't not see the dog.
*  Or there's examples where you show arbitrary images that people can't help but see a sphere
*  or a triangle there, even though there's not in fact a triangle there. And so what all of these
*  suggested, there's this guy, Helmholtz, who came up with, he used different words, but his idea was
*  perception as inference, which is what happens when we're seeing things in the world. What we're
*  actually doing is we're trying to infer, we're trying to infer the true state. And then we use
*  that as our prior when we predict net new things. So in other words, when we see this ambiguous
*  picture of a triangle, if it were the case that there were in fact a triangle there, that would
*  well predict the observation I'm seeing. And the reason why this is so important is if you think
*  about an animal navigating in the dark, once I have a prior about, oh, I remember seeing the
*  branches over there, I think I now have the base understanding that the world contains these
*  branches. Even as I start moving, if the sensory stimuli doesn't prove to me that it's there, but
*  is consistent with my prior, then I'm happy with it. I'll keep going with my prior until new
*  information emerges. So this type of, this is the Bayesian brain hypothesis, this idea that we try
*  to infer a model of the world. We try to infer what's the state of the world in my head. And
*  then I'm going to hold that as a prior and compare predictions from this against what actually
*  happens. You know, there's a lot of evidence that's what the neocortex is doing. And so
*  a lot of people talk about this neocortical generative model in the, through the lens of
*  it being really good at things like object recognition, which, you know, clue the neocortex
*  is good at. But I think from an evolutionary lens, a sort of alternative way to look at it is perhaps
*  what's most useful about the neocortex is not the recognition mode, which is the mode where I'm
*  receiving sensory stimuli and comparing it to my prior about the world, but the generation mode,
*  which is I'm cutting myself off from the actual worlds and I'm exploring the representation of
*  the world and generating my own data. In other words, simulating possible things. And the reason
*  why I think from an evolutionary lens is this is really interesting. It's hard to argue. I think
*  it's hard to argue one could argue this, but I think it's hard to argue the neocortex evolved
*  for object recognition because without a neocortex and a lot of vertebrates that just have a three
*  layered cortex are unbelievably good at object recognition. And they can do it with 3d perturbations
*  and 3d rotation. Like they, all the things that we would think a good object recognition system
*  should do fish seem eminently able to do. So it's, unless you argue there's some energy efficiency
*  or there is some unique improvement in performance in your cortex offers, I think it's sort of hard
*  to argue that the driving adaptive value of neocortical evolution was superior recognition.
*  I think what's much more compelling and consistent would be it was the first time when animals could
*  actually render a simulation of a state of the world. That's not the current one. In other words,
*  building a model of the world based on experiencing and perception by inference, but then having the
*  ability to pause and play out possible futures before I act. And, and that is something that we
*  do see in across mammals. So if you take a rat and you put it in a maze, unlike fish, it's, you know,
*  we haven't found this yet in fish. It would be a fascinating observation if we did, this is where
*  a lack of comparative psychology studies, you know, creates challenges. But with mammals,
*  we know this happens if a rat navigating a maze and you'll see it, if there's a choice points,
*  you'll see a rat pause and actually look back and forth. And so this has been, I was called vicarious
*  trial and error as a hypothesis, this view that rats seem like they're thinking about their possible
*  actions before they make a choice. But it was a hypothesis. There's no way to verify that rats
*  are actually doing this until this guy, David Reddish came around and actually recorded parts
*  of the hippocampus, which if you remember from early vertebrates render maps of space. And there's,
*  there's certain neurons in the hippocampus called place cells. So as a rat navigates around a maze,
*  there are specific neurons that activate at each location in that maze. You can actually look into
*  a rat and see, oh, there's a neuron that's a text that no matter where, which direction they come
*  from, it's always going to activate at this location in the maze, same thing for this whole location,
*  et cetera. And so usually place cells are primarily active for the location that the rat is actually
*  at. So as it's navigating the maze, you can see the place cells just change for the locations.
*  But when it reaches these choice points and looks back and forth, you see something mind blowing.
*  The place cells cease to activate only the location they're at. You literally can watch it
*  playing out possible futures. You can see the place cells start playing out different paths down the
*  maze until it actually makes a decision. So you can watch rats imagine the future. And, and that's a
*  really fascinating finding. And when you look at other abilities that you see emerge with mammals,
*  it's consistent with this idea of being able to simulate states of the world. That's not the
*  current one. For example, counterfactual learning. So counterfactual learning is being able to learn
*  what would have happened had I taken a different action. There's a key limitation with trial and
*  error learning and trial and error learning. You can only learn from the actual actions taken.
*  So I think a very simple example of this is rock, paper, scissors. So if you have, if you teach a
*  monkey to play rock, paper, scissors, if the monkey plays rock against paper and loses with
*  trial and error learning, what you would expect is it's now going to punish the behavior of rock.
*  So the next time it's going to be equally more likely to do paper or scissors, because one of
*  the three actions has been punished. But if it has counterfactual learning, if it can look at paper
*  and say, well, if I had played scissors, I would have won the last round. In other words, if it's
*  able to simulate possible actions, you would expect it to be more likely to play scissors.
*  And if it was really, really smart, you would realize there's actually no relationship between
*  these. So it's all random, which is what humans can realize. But what monkeys do is they become
*  more likely to play scissors, which demonstrates an ability to consider what would have happened
*  if I had done something different. And in rats, you can do sort of a similar thing where you can,
*  David Redish did a study, I won't go into the details, but you can watch a rat actually play
*  out different past choices and then change its decisions on the basis. You can go into the brain
*  and watch its orbital frontal cortex rendering a different outcome had it actually made a different
*  choice. You can literally watch it happen on which an orbital frontal cortex, another region
*  of neocortex. The other thing that emerges is something called episodic memory. This is a loaded
*  terms. Some people call episodic like memory, but the idea to render past events, which we also see
*  in rats, which lots of recent studies have shown episodic memory. Remembering the past is actually
*  the same process as imagining the future, because all we're doing is we're rendering another state
*  of the world. That's not the current one. So this idea, and again, in this breakthrough model,
*  what I think is so cool is you cannot have simulation without reinforcing. It is not,
*  there is no way to benefit yourself from imagining possible futures, unless you have some mechanism
*  by which to change your behavior based on those outcomes for a rat to be able to say, let me
*  imagine possible futures and then reinforce the ones where I get the best outcome in my imagination.
*  You need the same apparatus that's learning through trial and error. And you see this when
*  you go into brains as they imagine possible futures, they're effectively reinforcing themselves
*  vicariously based on their imagination. And thus, then when they go back into acting,
*  they're playing out their imagined action sequence. So the hypothesis here is that the
*  neocortex evolved, it gave a new mechanism for perception, perception by inference,
*  but the core adaptive value is the ability to simulate a model of the world, which we see
*  across mammals. And this is why mammals are good at fine motor skills, because a cat can plan
*  where to place its paws before it does so. Versus a lizard, if you watch a lizard run,
*  there's lots of evidence just they're not actually planning their movements ahead of time.
*  That's why most non mammalian vertebrates with the exception of birds are quite clumsy because
*  they don't have this sort of ability. I'm sorry. So the neocortex seemed to enable simulation,
*  which was again bootstrapped on the trial and error learning, which we see emerge in neocortex.
*  Yeah. This is kind of where I guess the, I don't know if you would agree with this
*  characterization, but it seems like we have pretty good AI versions of the reinforcement learning
*  breakthrough at this point. That's to say there couldn't be further improvement and sample
*  efficiency and so on, but it like largely works on this one. And then on the next one, we're kind
*  of in the, in the realm of like frontier AI capability. We can sort of squint and see that
*  we can kind of get language models to do some of this simulating if we set it up and scaffold it
*  the right way. And you have like techniques like chain of thought, and then that gets elaborated
*  into tree of thought. And there's the kind of, well, you know, we go down this path and this
*  path will be about, you know, evaluate those paths. So there is something pretty analogous there,
*  although it's, it feels like kind of a hack by comparison. Maybe a broad question is like,
*  how would you compare and contrast the state of AI simulation, counterfactual ability versus
*  biology? And also specifically within the biological systems, where do, how much do we
*  know about like how you get into the sort of counterfactual mode? So it's almost like there
*  must be some sort of switch or gating mechanism and how did the inputs for the hypotheticals
*  get generated? I'm a little bit, you know, if I'm, if I'm, when I'm thinking about my like range
*  of possible futures, there's this like fundamental mystery of like, where did the starting points
*  even kind of arise from? And then I can kind of, I know what I think it feels like to follow those
*  down a simulated path, but like how I even got onto these various simulated paths,
*  you know, I don't really feel like I have access to that.
*  Scottie So lots of fun thoughts there. So, so planning in general, so the,
*  the notion of simulating possible futures is a very old idea. I mean, in the fifties,
*  we were building systems that would engage in some form of planning. It's not the existence
*  of planning that's missing. It's how do we do planning in a way that works in practice? And
*  we haven't really, that's, that's the nuance. And the question is, are we a few architectural
*  tweaks away from that? So we'll, you know, open AI is a tree of thought system actually get us
*  very far as possible, or is there some fundamental aspect of how mammalian brains do it that's
*  missing? And that's also possible that we're just missing some key insight. So I think one
*  thing that is clearly different and that's going on in mammal brains, I don't know the open question
*  on like how far away this is an AI, but in mammal brains, there's this, it's you're continually
*  active and you're switching between these behavioral modes, as you're saying. So in
*  mammal brains, you have this sort of what might be called model free, which means I'm not actually
*  simulating possible futures. I'm just directly responding to the stimuli I'm getting defaults,
*  which, you know, kind of Daniel kind of would say like fast thinking, this is like the immediate
*  response to stimuli and we are going through that process. And then sometimes for some reason,
*  we intelligently decide when to stop and think. So that's the first intellectual thing that
*  somehow mammal brains are cleverly deciding when is this a choice point that I'm going to think
*  about. I have a general thesis, which I don't think I'm sure that other people that have this
*  idea where it's some notion of uncertainty measurement that drives this pausing. And so
*  uncertainty could be measured in different ways. It could be measured in the basal ganglia, where
*  there's divergent predictions of model free actions. It could be measured in the neocortex,
*  which is uncertainty and a generative prediction about the next day of the world. We don't know
*  that yet, but uncertainty triggering pausing. I think there's some good evidence that that
*  is something that's going on in male brains. Then there's the question of how do I prune the search
*  space to select possible futures to evaluate, which is your question of like, when you pause
*  and think you're obviously not doing a comprehensive search of all the possible futures. That was
*  ridiculous. So how do mammal brains actually cleverly prune the search base in three dimensional,
*  three dimensional world? This is one of the leading problems in robotics, which is the
*  the dimensionality of controlling even a basic robot arm is gargantuan, right? The actuators and
*  all the locations of where you put all the fingers and the arms, it's just such a gargantuan search
*  space that people have not yet figured out how do you prune that thoughtfully so that it can plan
*  movements at a time. A lot of research going into that. And then the last question is how do you
*  decide which outcome you select? And so how do you evaluate possible outcomes after you're
*  simulating? It's not just the notion of planning, but there might be unique breakthroughs in each
*  of these steps or unique sort of technical insights that we need to find and then bring into
*  other systems. Now you could imagine, I mean, I could imagine chaining together an LLM to do
*  each of these things, right? You could imagine just giving an LLM, you know, a small model,
*  a set of stimuli and just say, should you simulate, should you simulate? Yes, no, yes, no, yes, no. If
*  yes, then you engage a tree of thought, LLM that then selects things. You have another LLM that's
*  evaluating the outcome, saying is it accurate? So you could imagine chaining together an LLM to
*  do these three steps. Question is how well will it work? I'm sure we'll find that out soon. But I
*  think, so I think for the way that simulating works in the mammal, in the million brain,
*  I think one of the key things I believe that we're going to have to figure out in the AI systems is
*  this notion of continual learning. This is where I think the big next insight, like if I were to
*  do more neuroscience research, this is where I would focus my time. Because what happens with
*  LLMs, and this goes to their lack of episodic memory too, is I can't talk to it and it just
*  remembers as I'm speaking to it versus, you know, I can explain a new concept to you and now you
*  just know it and you didn't forget all the things you knew before. This notion of catastrophic
*  forgetting has been a problem in deep neural networks for a very long time. I mean, this is
*  why we don't let weights get updated continuously with new information because we know it risks
*  catastrophically losing its abilities. We see this in fine tuning. You know, I've been doing a
*  lot of fine tuning experiments for a variety of different things I've been working on to the side.
*  And the problem with fine tuning is you very quickly get this overfitting issue where it ends
*  up overfitting to the small fine tuning data set and it loses its generalization. It's forgetting
*  old tasks that I was able to do. This is not like a, I don't think this is a nuanced edge case. I
*  think this is a foundational problem with the way these models work. And so how does the mammal
*  brain decide when to incorporate new information and how to add it to my model of the world without
*  interfering with other information is a huge outstanding area of research that I think will
*  is a key difference between how mammal brains are sort of simulating and modeling the world
*  and how existing AI systems are doing it. We have some unique ideas in neuroscience. For example,
*  it seems to be the case that it's possible that weights are only updated in times of surprise or
*  new information. So there's some suggestion that there are certain neuromodulators that get released
*  only in moments where you have failed predictions, which then sort of doused synapses and in a
*  neuromodulator that enables them to update their weights. So one way we reduce catastrophic
*  forgetting is we're not actually continually learning everything only in certain instances.
*  Do we update weights? Another thing that I think is unique that people haven't really figured out
*  is this like sort of eureka moment that happens with humans where if you teach me something
*  that's confusing, I don't just incorporate it into my model of the world, which happens with
*  a neural network. I can give a neural network a transformer, any fine tuning data set I want,
*  even if the data set makes no sense relative to its prior information. And it will just start
*  learning because I'm back propping through. If you tell me one plus one equals four, and you start
*  trying to explain that concept to me, I'm not just going to take that as fine tuning data. I'm going
*  to take my model of the world and then desperately try and grasp how the information you're telling
*  me fits into my model of the world. And until I get it, I'm going to reject the information.
*  It doesn't make sense in my model of the world. And so something nuanced is happening where we
*  have, this is where robustness is clearly occurring in mammalian brands. There's something where
*  I reject new information unless I can somehow fit it into my established, rich and robust existing
*  model of the world. And somehow this is enabling, I think, a more generalization across tasks.
*  And somehow this is enabling continual learning in a more robust way, because we're not just
*  arbitrarily letting new information update weights. But how that actually works,
*  I don't think we know yet. But yeah, that would be my sidebar on what I think is missing in AI
*  systems that exist somewhere in the brain of mammals. Yeah, that's very interesting. And that
*  does bring to mind the state space model moment for me as well, which in the interest of time,
*  I'll keep this brief, but I had a long monologue about it late last year. And basically,
*  I think it at least promises a partial answer to some of these challenges where basically the
*  addition of a state, which is long lived and propagates through time, creates kind of a third
*  aspect of the overall system, right? In the transformer, you've got the weights and you've
*  got the inputs and it's kind of input and output. But the addition of the state gives you kind of
*  this extra thing that can store information, can kind of evolve through time without having the
*  weights themselves have to change. You have this kind of additional degree of freedom in terms of
*  how you want to store information, how you want to represent it. And the Mamba paper, which kind of
*  triggered me to go down the rabbit hole on this for a little while, crossed the threshold of
*  basically being as expressive, achieving very similar high level loss metrics to transformers,
*  but doing it in a way that A is a lot more efficient computationally, but B also has this
*  additional thing where you can encode memories longer term, I think. We're still in the very,
*  very early phases of figuring out how we're going to use the state space models in the broader
*  architecture of AI systems. I don't think it's just like a replacement. If there's anything to learn
*  from this five, well, there's a lot of things to learn. I don't want to diminish it, but one
*  thing I definitely take away from the five breakthrough model is that we still have all
*  the earlier breakthroughs. When people say, is this going to be the thing that kills the transformer?
*  I think one thing you could take away from this history of the biological intelligence is probably
*  not. It's probably something that gets combined to and remixed with and hybridized with the
*  existing capabilities and adds something new. Then over time, that will evolve further and maybe
*  bleed together and become inseparable even maybe, but it doesn't feel like we are...
*  When you think about is this going to totally replace that, that seems like a very rare
*  and temporary strange time in the evolution of these things. More so now we have this new ability.
*  Another thing you said too is when to accept and when to reject information,
*  the mechanism of the Mamba paper they call the selective state space model. Earlier states based
*  models just had, I don't want to speak for all states based models, but broadly an explicit
*  encoding of the history. You're just compressing with a known engineered algorithm all history
*  into a state to the best of your ability. You can have different trade-offs there. Do you want to
*  remember recent stuff more? Do you want to wait all history the same or whatever? But the selective
*  mechanism now allows you to update the state depending on the overall dynamics. You're not
*  just explicitly accepting any new information in with a hard-coded encoding, but if stuff
*  doesn't jive or doesn't seem relevant, then you can just not update the state accordingly.
*  I think we're probably going to see a lot of little variations on the, first of all,
*  multi-state models and then a lot of little variations on the selective mechanisms to
*  figure out, do we need a bucket, a state to put all the outliers in or a state to whatever.
*  There'll be a lot of things there. But I do think this third breakthrough and some of your comments
*  about it definitely suggests to me that the, which I already believed coming in, but I see a lot of
*  parallels to what the state space models may unlock for AI systems as a whole. Number four is
*  mentalizing. Cool. All right. I'll try to make the fast-paced. So mentalizing. So when we look at
*  primates, this is an area where the comparative psychology gets more controversial. So I'll try
*  and caveat things where in general, most primatologists or comparative psychologists would
*  agree with this, but some would disagree because there's a lot of debates around what non-human
*  apes are capable of doing, et cetera. But there are three abilities that you see at least good
*  consensus around, or at least some evidence for within non-human primates that are consistently
*  not found in non-primate mammals and other animals. And so this is sort of a good way to try and back
*  into what evolves in early primates. So one is this idea of theory of mind. And so theory of mind
*  is this idea of I can try and infer what your intent is based on observing your actions or try
*  to infer what knowledge you have on the basis of what I can see you doing. And so there's lots of
*  really cool studies with non-human primates where you can see these types of things emerge. For
*  example, there are studies where if you let a chimpanzee play with two different goggles,
*  one goggle that you put on, you can't see through and one goggle you can see through.
*  And then you let two human experimenters put these goggles on and they both hold food. The
*  chimpanzee always goes up to the one and with the goggles they can see through. So somehow they're
*  inferring and there's no reason why you would expect any sort of sort of Pavlovian association
*  with one of them or the other. But clearly there's some association of this person can see me and
*  this other person can't. Another good example that you see in non-human primates is there's
*  a study of them inferring the difference between people intentionally doing something versus not.
*  So there's been studies where you teach a non-human primates that of the two boxes placed
*  in a room, the one with a red marker mark on it is the one with food in it. So you train them
*  about that fact. Then you have an experimenter come in and bend over and mark one of them and
*  then stand up and then pretend to accidentally mark the other one. In other words, drop the marker.
*  Stimulus is identical. They always go to the one that was intentionally marked.
*  So there's some notion of the humans are giving me this food and this is the one they meant to
*  mark. So I'm ignoring the one that was an accident, which is really hard to understand without some
*  notion of I understand what you're intending to do. There's been lots of experiments like this
*  where they, one of my favorite ones, which is a little bit less rigorous, more of an anecdote,
*  but I think it beautifully describes how rich the lives of non-human primates are.
*  This guy, Emil Menzel was doing studies, trying to just show the presence of map-based learning
*  in, I think it was chimpanzees. And so what he would do is there's a sort of one acre forest
*  these chimpanzees were living in and he would show one of the chimpanzees, hey, I'm going to
*  put food behind this little morsel of food under this bush and then just see if the chimpanzee
*  would go back to the same location. And okay, great. He learned that obviously they go back
*  to the same location, but then he started observing something that he did not expect,
*  which is when I think her name was Belle, that chimpanzee started sharing the food with the
*  other members of the group. There was another chimpanzee named Rock that ended up being really
*  mean and taking all the food from her. So she started trying to trick him. She would wait
*  till he looked away and then go and get the food. So then he started intentionally looking away.
*  So she would go to the food and then he would turn around and run after it. Then she started
*  trying to lead him in the wrong direction until he was far enough away. And then she'd run back.
*  There was a cycle of deception and counter deception that folks have found with their primates,
*  which is only really possible to conceive of if what's happening is I'm trying to trick you
*  by changing the knowledge in your head. I'm trying to give you information that's wrong. So you think
*  one thing so I can do something else. And this is incredibly hard to imagine how someone would,
*  an animal would do this without some notion of understanding the mind and intentions of others.
*  So that's one new ability we see with them. The other one is imitation learning. So non-human
*  primates are really good. Remember those studies with a really good imitation learning member,
*  the size Edward Thorndyke, where it's sort of hard to find imitation learning in the animal kingdom.
*  But with, with non-human primates, they do it exceptionally well. You can teach,
*  they've done studies where they take one member of a primate group and they teach it to do this
*  special trick with a rake to get food. And then they send the primate back out into the world.
*  And pretty soon all of the whole troop is using the same exact technique. So they're cool. It's
*  like very clear evidence that they're learning through observation. There's also some evidence.
*  This is more controversial that chimpanzees do actively cheat teach. So they have seen,
*  you know, there's been some new evidence that chimpanzees will literally correct the mistakes
*  of youngsters when they're trying to do things like termite fishing, which also clearly requires
*  an understanding of what someone else's knowledge is and how to modify the knowledge. And so, okay.
*  So we have theory of mind. We see this improved imitation learning emerge in primates. And then
*  the other one, which the least evidence for, but there is some evidence for that primates are
*  uniquely good at what's called anticipating future needs where they can, they can take an action today
*  for a need that they don't currently experience. Humans do this all the time. We go to the grocery
*  store, we buy food for the week, even though I'm not hungry at all right now. And as obvious as
*  that seems to us, it's actually quite challenging to understand how animals do that. And they,
*  one of my favorite studies on this was done comparing squirrel monkeys and rats. And what
*  they did is they said they're going to give each of these animals a choice between two options.
*  One option is a low treat option. So it was either dates or raisins, but if they go with that route,
*  they get water right afterwards. The other is a high treat option, but they don't get water for a
*  long period of time. And they baseline these between the two animals to make sure that they
*  are quantifying it to induce a similar amount of thirst. And so the point is, am I willing to give
*  for go the high treat option because I know in the future, I'm going to be thirsty, even though
*  I'm not thirsty right now. I mean, what they found is squirrel monkeys would do that. They would go
*  with the low treat option, but rats would not. So some suggestion that they're capable of anticipating
*  future needs. So, okay, you have these three seemingly totally distinct abilities. And if
*  you go into the brain of new primates, you don't see a very different brain from early mammals.
*  There's really two main things that change other than size. The brain obviously is meaningfully
*  bigger, but they got an area of frontal cortex called granular prefrontal cortex. And then they
*  have a few sub regions of posterior sensory cortex that's new, that are new. And if you look at the
*  connectivity, a reasonable first approximation is what these, these areas of a new cortex are
*  doing is they're, they get input from older areas of mammalian neocortex. In other words,
*  it seems to be building a model of the older model. It's a hierarchical layer above it.
*  For example, a granular prefrontal cortex that exists in early mammals, that exists in rats,
*  gets sensory input directly from areas like the hippocampus and the amygdala. And if you look at
*  granular prefrontal cortex, it gets none of it. It only gets information from a great prefrontal
*  cortex. So you can think about it as sort of a hierarchical layer above. And sort of the idea
*  here is if you, and there was actually a big mystery about what these structures even did,
*  because there was lots of early studies in the 20th century that showed people with damaged
*  prefront, granular prefrontal cortex didn't seem to be fine. In some cases they were like
*  mostly normal other than their personality being weird. But then people started realizing that one
*  of the main things they were really bad at is engaging with other people in a socially reasonable
*  way because they really struggle on these theory of mind tasks. So if you start giving them tasks
*  where they need to reason about the changing knowledge of other people, they become quite bad
*  at it. One of my favorite studies on this is they compared people with damage to granular prefrontal
*  cortex to baselines to damage to hippocampus. And they asked them to do something very simple.
*  They said, just, can you write a little story about some state of the world in the future?
*  People with hippocampal damage could describe themselves in these imagined stories, but the
*  richness of the world was very basic. They couldn't describe key features of their imagined world.
*  People with granular prefrontal damage were eminently capable of describing aspects of the
*  world in the future, but they were always absent. They really struggled to imagine themselves
*  in this imagined state of the world, which suggests that part of what's happening is
*  the granular prefrontal cortex enables you to model you. In other words, it's the source of
*  metacognition, thinking about thinking. And what's interesting is you see these three abilities emerge
*  along with granular prefrontal cortex. They can actually be understood as three applications of
*  the same thing. So modeling your own inner simulation is effectively creating a model of
*  one's mind, and able to simulate the simulation. Another way to think about this is being able to
*  simulate thinking about different things. And so what that enables one to do is I can put myself
*  in someone else's shoes, because I can now imagine myself in a different situation and try and predict
*  what would I know and what would I think. You can also much more easily learn through imitation,
*  because I can see someone doing a behavior and I can imagine myself doing the same behavior and
*  vicariously train myself doing it and figure out what their intention is. One of the key things
*  with imitation learning is you can't just wholesale copy. In the interest of time,
*  I won't go into this whole area, but there's a really fascinating area of imitation learning
*  in AI where we found is one of the key things to make annotation learning work is not direct
*  copying, but inferring the intent of the behavior in someone else. In other words, what are they
*  trying to do? And then vicariously reinforcing yourself to do what they're trying to do. That's
*  a key thing that makes imitation learning work, which would explain why primates able to simulate
*  someone else's intentions become very good at imitation learning and anticipating future needs.
*  You could conceive of this simply as for me to imagine myself being hungry, I need to be able
*  to simulate myself in a different mind state than my current one. In other words, I need to be able
*  to imagine just like I would try to figure out why is person A acting this way. They must be really
*  thirsty because when I do that, the reason is because I'm thirsty. I can also imagine, well,
*  what am I going to feel if I take this action? I know I'm going to be thirsty because I can
*  simulate that behavior and I know I'm going to regret and want this other thing. I'm going to
*  engage in counterfactual learning and be upset. So actually what I'm going to do is take a different
*  choice. So what I think is cool about sort of this breakthrough four ideas, you see one common suite
*  of things happen in the neocortex, which seems to model the self and you see three new abilities
*  emerge, which can be conceived of as a first approximation. It's just different applications
*  of the same thing, which is simulating your own inner simulation. Mechanistically, how does this
*  actually work? Can we, is what I'm describing rich enough in detail to create sort of algorithmic
*  blueprints, Bill is an AI, definitely not. But in principle, it suggests that modeling the simulation
*  itself might unlock some interesting things. It also suggests some interesting things in how we
*  relate to AI systems. If what I'm saying is correct, not the only one that conceived of this,
*  but if the general story I'm telling is correct, one of the key grounding constraints that enables
*  humans to engage and relate to each other is the fact that our brains are not that different
*  because there is a synergy between me imagining myself in your shoes, being a relatively good
*  proxy for how you actually will feel. And there's lots of cognitive biases that we see happen where
*  I project, I try to project things onto other people when they don't feel that way, just because
*  I would. And this is our differences do create problems with a certain mental projection.
*  But if we create an AI system with a brain that works woefully differently than humans,
*  then we're going to perhaps need very different mechanisms to ensure that they understand why
*  we're doing certain things and the intent of what we say. Because the way in which human brains pull
*  it off is at least in part, I think, based on the idea that we have similar reward structures and
*  similar mechanisms by which the brain works so that this sort of mental projection on average
*  tends to be relatively effective at predicting what's going on in the brains of others.
*  Yeah. Theory of mind is a fascinating topic in every dimension. I've done a little bit of a deep
*  dive at one point into just how good is the GBT-4's theory of mind for humans. And it's
*  still controversial, but I would say it's definitely off the zero line at this point,
*  quite clearly. And then our theory of mind of the AIs is also extremely, maybe even more difficult
*  in some ways because our instincts for understanding them are so often misled by our
*  instincts for understanding ourselves and one another. We'll keep then the fifth breakthrough,
*  which is speaking for the book. People can read, or I listened actually to the audiobook,
*  which I recommend. How about some just very kind of high-level conceptual questions? I guess
*  one that stands out to me is the architecture of biological brains is very messy, dense connections,
*  not differentiable, not linear. It's this sort of mess that has all these kind of feedback loops
*  that are kind of cyclical and all sorts of different geometries. AI, much more linear.
*  Everything has to be differentiable for back propagation, at least in today's paradigms.
*  We've got other kind of evolutionary paradigms, but they're not currently
*  advancing the state of the art nearly as much. Do you have an intuition for
*  how that will shape up over time? Do we need more complicated geometries to achieve some of the
*  advantages? I'm specifically thinking about robustness, adversarial robustness that the
*  biological systems seem to have at a much stronger level than the AIs today.
*  Backprop has been so incredibly successful. The thing that brains might be doing that
*  it's hard for us to argue that it's going to replace backprop, but it might add a modification
*  to how backprop is used, is brains seem to be doing clever about when weights are updated,
*  which enables it to do continual learning. I think one of the key things we're going to want
*  is continual learning in these AI agents, being able to have them continuously get a stream of
*  information and us be confident that they're not going to lose knowledge about prior things that
*  it had information about. In order to do this, the thing with back propagation is almost too perfect
*  because it updates all the weights to be the exact partial derivative relative to the gradient.
*  If you're doing stochastic or mini batch, fine, it's not exactly right, but it's a very accurate
*  computation. The human brain might be doing something less accurate, but with some other trick
*  that enables it to engage in continual learning. I would be surprised if the answer ended up being
*  a wholesale. We don't do backprop at all anymore. We use this clever mechanism that we've figured
*  out the brain work. But if we figure out the general principle on which how brains maintain
*  representations robustly while learning, my hunch would be, my intuition would be that we can apply
*  that and still use back propagation. For example, and this is definitely not the answer, but if it
*  were the case that it was as simple as there's some measure of uncertainty and when uncertainty
*  passes a threshold, there's some process of assimilation of this new information. So some
*  active learning process of take the uncertain new object and try and manipulate it to understand
*  until I feel like I've generated enough data that I understand the thing. And then I go on with my
*  life. In other words, there's an active learning process. You could conceive of doing that with
*  back propagation, but what you're doing is you have some other mechanism by which there's a pause,
*  a process activated where you're going to allow weights to be updated. Maybe there's a generative
*  replay component where maybe we're going to learn that these AI agents have to sleep. There needs
*  to be some mechanism just like the brains use to maintain representations robustly where we're
*  replaying things to make sure there's some consolidation. So it seems likely to me that
*  to make continual learning and robustness work, there's going to be something new. And it's not
*  clear to me whether it's going to come first from biology or first from AI, but my guess is there's
*  going to be a beautiful cross pollination. If it's discovered first in AI, it might end up
*  be another Richard Sutton story where we go back into brains and realize brains are doing something
*  quite similar to this. Or if someone goes first into brains and figures out something clever,
*  and then we go to AI and we try to apply it. My guess is probably the ideas are already in
*  neuroscience. There's so many ideas on how brains do this. It's going to take someone reading
*  through that literature and coming up with a good, taking the right things from those ideas
*  to implement them. So yeah, I would be very surprised if we end up in 10 years and it's like
*  we've come out with a completely new paradigm. We're not using back prop. It's not deep learning.
*  I think that's unlikely. I do think there's some interesting things that will go on with
*  macro structures. So what's already sort of happening where a lot of the work that's been
*  going on is on single models. And we scale up a single model, single input output. And we know
*  brains don't do this. It's not just a broad soup of neurons. There's specialized subsystems that
*  talk to each other in interesting ways. If I imagine a world where we all have autonomous
*  robots walking around our house, I think it's a reasonable prediction that that's not going to
*  be a single model. There's going to be subsystems. There'll be some ConvNet that does object
*  recognition. There'll be a language model. Maybe there'll be some separate world model system.
*  Maybe there'll be some other continual learning episodic memory system. And these things sort of
*  come together. I mean, a whole brain macro architecture that's not just one scaled up
*  foundation model. Yeah. So many interesting little parallels and connections I'm drawing there.
*  Very early language model things like the pause token. Think before you speak. I think that paper
*  was called and that the backspace seems to kind of relate where you're getting out of distribution.
*  Your confidence is getting low. We're not yet at the point where we're really figuring out how
*  to internalize that. But with the backspace, you're just kind of like, I think I've taken
*  the wrong step here. Let me back up and try a different path forward where I can hopefully stay
*  more in distribution. I was just thinking too very much along the lines of what you just said that
*  it seems like we lack the kind of robustness, the ability to move forward in the broadest sense
*  through the changing environment. That's kind of what the language models, despite all the scaffolding,
*  can't do. But I think about something like the open worm project or I think recently the whole
*  connectome for the fruit fly was mapped. And I start to think, geez, what if you took that
*  as a digital blueprint and started to Frankenstein it where you go in and maybe replace a neuron with
*  a module or kind of like we talked about with both the com that onto in place of a single
*  food smell detector. Could you put sophisticated object recognition there?
*  And you can almost imagine taking this high level architecture that sort of has the
*  right feedback loops already evolved, but then just like soup up a lot of the components.
*  And that could get extremely weird. Probably we're headed for a future of both powerful and
*  weird systems. Does that seem like a viable path or do you expect things like that to start to
*  happen? I still think it's going to take taste from the side of the modeler to take a connect of
*  a fly brain and then figure out how to model it for the following reasons. Even knowing the connect
*  dome of a brain still only gives you a small percentage of understanding of what is computing
*  because even if you want to do a whole brain model of it, one neurons have different base firing rates,
*  different thresholds for firing, different firing modes between phasic and tonic. So just knowing
*  that two neurons connect to each other doesn't tell you how it's going to translate information
*  to the learning rates of synapses are totally different. So if you're on one dendritic spine
*  versus another, if you're close to the soma that has different effects, I don't know. I don't know
*  specifically about the connective of the, of the fly brain, but if they don't have knowing what type
*  of neuron is each, I would imagine they do. But if you don't know whether it's an excitatory,
*  inhibitory or neuromodulatory neuron, then you're not going to know what it actually is signaled
*  across the connection. If you don't know what receptor expression is on the post and pre-synaptic
*  neurons, it's not going to be easy to model how the synapses will in fact change. So all of that
*  is to say that like knowing how things connect to each other doesn't actually give you enough
*  information to do a wholesale model of how it will process information. So that means one of two
*  things. One, we're eventually going to get to the point where we do have enough information to just
*  wholesale model brain, which will be amazing, but knowing connectivity is not sufficient.
*  Or it's going to take a model, which is probably going to end up happening first. It's going to
*  take someone really great taste to say, okay, well, I'm going to guess that this is what this
*  module is doing and that's what this module is doing. And this is broadly the information that's
*  being communicated between them. And so I'm going to take the basic idea of it and render a simulation
*  of that and see if it behaves in a similar way to a fly brain. And I think that is, that's an
*  interesting approach, but it's still going to take some good intuitions from the sake of the
*  model. Or given just knowing the connections is really not enough. Yeah. That reminds me of the
*  Wright brothers and their observations around the subtle movements of the bird wings as they were
*  soaring. They didn't obviously just go in and do surgery on birds, but they were able to create
*  something that was inspired by and captures some of the principles of, but obviously it's been a
*  lot more extensible in important ways for us as well. Okay. So last one, do you have a unified
*  theory of value or moral patient hood that you could apply to these five breakthroughs? Like how
*  much should I care about a worm versus a fish versus a ape? And then if you'd be so bold,
*  do you have any intuition for how that would extend to AI systems? I have an intuition, but I
*  don't want it to be used as a moral authority for how we should treat animals. So I'll describe
*  my intuition, but I'm not an ethicist. So I don't claim to have actually thought through all of the
*  philosophical implications, but my intuition is there is something important on the jump from
*  a model free reinforcement learning system to a model based reinforcement learning system. In other
*  words, mammals, which I think there's independent convergence with birds, by the way. So it seems
*  to be the case that birds independently evolve these different types of brain structures that
*  do the same type of thing. So, you know, I think birds seem to also have this. So this seems to be
*  something unique about an animal that can actually pause and think about things and create a model of
*  itself. Now how that maps to the notions of consciousness and Aqualia and all that unclear,
*  but it seems to be the case that Aqualia is rendered in the neocortex, which would be consistent
*  with this idea of, or at least neocortex is essential to rendering Aqualia, which would
*  suggest that rats are experiencing the same thing. There might be something unique also that emerges
*  with primates when you actually have an identity in a sense of self. My intuition, this is pure
*  speculation. My intuition would be that Aqualia, the experience of things is something that evolves
*  in mammals, which is separate from identity and thinking about who you are and your place in the
*  world. And I would put more moral weight on the experience of things than the identity of things.
*  So some basic speculative intuitions when one is meditating, I am not in fact, the joy of meditation
*  is removing myself from obsessing over my identity, who I am, how I, you know, where I sit in the
*  world and ruminating about ourself, which I would think is a very primate like activity and just
*  engaging in raw perception by inference and experiencing the present, which is just not
*  engaging in the simulation of other things, but only just rendering a simulation of the current
*  state. And so I think that the experience of things is where things can be, one can suffer,
*  right? So whether or not I have a sense of self, I can still experience suffering. And so again,
*  all speculation, but to me, my intuitions lie in, you know, a rat really should have very similar
*  moral weight to a human. If you believe that, you know, where things are, where moral weight is
*  applied is in the actual experience of things, it doesn't need to have a notion of its own identity
*  for it to feel pain and feel fear, et cetera. Whereas for a fish, yeah, I feel like the fish
*  psychologist won't love this. But if I look into a fish brain, I don't see it's hard to correlate
*  the same sorts of things because their brains look so different. But of course we could,
*  we could find out that what's happening in the fish brain does correlate to what's happening
*  in the mammal brain. And then we'll realize we're committing atrocities. So there's risks associated
*  with it. But if you're asking my speculative intuitions, I do think it's at least very hard
*  to argue that humans have strong moral weight over non-human primates. I think that's a very
*  hard argument to make. And I also, my intuitions would say also would apply to mammals. In terms
*  of AI systems, this is like the trillion dollar ethical question that people are, I think, not
*  talking about. There's the question of how they treat us, which is a problem. But the question of
*  how we treat them is usually problematic because we don't even know, I mean, we don't even have
*  philosophical grounding to infer that anyone other than oneself is conscious. You know what I mean?
*  We, the only argument we really have, which is not based on observable data, is mechanistic
*  similarity. I just say, it seems to be my consciousness emerges from this thing in my head.
*  And I look in your brain, it looks quite similar. That's problematic because we're
*  clearly not going to be able to apply that paradigm to AI systems. And I think most people in AI
*  and in philosophy would hold the materialism view, which is you don't need the biological
*  gooey stuff of neurons to implement the same process. So now we have this big, we have a
*  challenge of how do we know when an AI system is now garnering ethical and moral weight?
*  And I don't have good answers to that. But I do think that that is going to be
*  an emergent challenge of the 21st century. Well, that could be a possible challenge for you to take
*  up in the next book. But for now, the book is A Brief History of Intelligence, Max Bennett, author.
*  Thank you for being part of the cognitive revolution. My pleasure. Thanks for having me.
*  It is both energizing and enlightening to hear why people listen and learn what they value about
*  the show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me
*  on the social media platform of your choice. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it, and I recommend you
*  use it too. Use Cogrev to get a 10% discount.
