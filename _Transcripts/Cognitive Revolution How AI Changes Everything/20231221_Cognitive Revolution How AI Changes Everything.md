---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 9006s
Video Keywords: []
Video Views: 8759
Video Rating: None
---

# Emergency Pod: Mamba, Memory, and the SSM Moment
**Cognitive Revolution "How AI Changes Everything":** [December 21, 2023](https://www.youtube.com/watch?v=X5F2X4tF9iM)
*  My sense is that neither the human brain nor the transformer are the end of history.
*  The purpose of this episode today is to really sound an alarm and say that I think we now
*  have that new architecture.
*  We're going to see more effective agents, more compelling long-term assistance, more
*  compelling long-term AI friends and companions.
*  All of this, if I had to guess, I would say it probably happens several times as fast
*  as the transformer era.
*  Hello, and welcome to the cognitive revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture
*  of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  One of the most important big questions that I get asked is what are the chances that somebody
*  invents something better than the transformer?
*  Since 2017, with the introduction of the transformer, attention is all you need.
*  Transformers have dominated the field.
*  One of the big realizations that I had as a relatively recent entrant to the field a
*  couple of years ago from my multimodal perspective at Weymark was, oh my God, it's a transformer
*  solving all of these different problems.
*  As I'm watching art creation come online, as I'm watching language models get dramatically
*  better, as I'm watching all sorts of niche tasks advanced rapidly, image captioning,
*  image matching, video captioning, all these different things, so many things, everything,
*  everywhere all at once, but all the transformer.
*  So I think I've been pretty clear in recent months on a bunch of different episodes that
*  this is hard to predict.
*  I sometimes call it the hundred trillion dollar question, which is the size of the global
*  economy today.
*  But my sense is that neither the human brain nor the transformer are the end of history.
*  If you watch my AI scouting report, I go through the history of expectations and predictions
*  about how far AI might make it given raw compute guesses.
*  These date decades back, most notably in the 90s with Kurzweil publishing his Singularity
*  is Near drawing these exponential curves and saying, hey, right around 2020-ish, 2020,
*  2025, that's when you're going to have enough compute to match the power of one human.
*  And then later you're matching all of humanity and becoming truly superhuman.
*  Well, the human level AI has shown up roughly on schedule.
*  It is, as we've covered in many different ways, human level, but not human like.
*  In many ways, it is very alien.
*  And yet this power, which now is in most domains ahead of the average human and in many domains,
*  really closing in on expert performance, this has basically all been driven by the transformer.
*  The attention mechanism is doing everything for us.
*  So I've been really interested in this question.
*  How likely is it that somebody will invent something better than the transformer?
*  And I've been watching out for it.
*  And there have been a few plausible candidates this year, which I've mentioned a number of times.
*  Those include most notably RetNet, which is a publication out of Microsoft collaborating
*  with Singularity University in China.
*  We also had Lily Yu from Meta on to talk about the Megabyte architecture.
*  Which was still fundamentally transformer, but the hierarchical approach that was different
*  and in meaningful ways.
*  And of course, there have been a ton of improvements, but there have been a few candidates
*  for things that, hey, this might start to look like something that could be even better than
*  a transformer.
*  The purpose of this episode today is to really sound an alarm and say that I think we now have
*  that new architecture.
*  And it is called the Selective State Space Model, aka Mamba, published in just the last
*  couple of weeks.
*  I saw this paper pretty much as soon as it came out.
*  Saw some of the claims and have gone really deep into not just trying to understand it.
*  That was about the first week since it came out, but then also really begin to project
*  into the future.
*  What is this going to mean?
*  I think if my AI scouting paradigm is good for anything, it should be good for identifying
*  new research that really matters and at least giving a pretty good guess about what that
*  new research, what that new capability is likely to unlock in practical terms.
*  So that's what I'm going to try to take you through here today.
*  It is going to be hopefully accessible throughout.
*  I always try to use vocabulary words and then the most plain spoken terminology that I can.
*  So I'll try to make it as accessible as possible throughout.
*  So I'll try to make it as accessible as possible throughout.
*  It will also definitely be technical.
*  I will be getting into the weeds for sure deeply, but actually to start off with something
*  a little bit different today.
*  So if you'll indulge me, I think it may prove instructive to begin with a little examination
*  of our own human cognition.
*  So what comes to mind when I say the word rainbow?
*  There are a lot of different ways to think about the concept of a rainbow and I'm sure
*  everybody had a slightly different experience in just those couple seconds that I let you
*  think without further prompting.
*  Some may have conjured up an image immediately.
*  Obviously, we have highly visual things that we can't see.
*  We have highly visual thinkers among us.
*  So you may have gone straight to a colorful vivid image.
*  Others may have gone to smells.
*  I'm not a big smell person, but I do find that the rainbow associated always with after
*  the rain, there's a very distinct smell and a very consistent smell to that.
*  And somehow that is conjured for me very quickly.
*  You can also get a lot more conceptual.
*  Think about it through the lens of, for example, science.
*  What is happening?
*  How is it that light interacting with water in the air is bent differently such that the
*  colors normally perceived as just normal white light are split and we can perceive them
*  individually.
*  You may think of just the history of science as well and what an achievement that was.
*  But you also might think about going deeper into history, thinking about how
*  ancient humans understood the rainbow, thinking about how
*  in various traditions it represents a promise from God, a sense of protection,
*  a sense of rebirth, renewal, obviously associated with spring as well.
*  You might think about just the pure colors.
*  If you're an artist or a creative or even just a kid who remembers that Roy G.
*  Biv mnemonic, which was never that great of a mnemonic, but that's what we were taught.
*  Roy G.
*  Biv, the colors all in order, how they blend together, how there really is no exact
*  distinction, but it is a spectrum, a sort of continuous space of color,
*  profound in its own way.
*  You might even think of just contemporary identity politics.
*  You might think of the rainbow as a way to express self-love.
*  You might think of the rainbow as a way to make a statement about who should be included in what
*  spaces in society and on what terms.
*  You probably have personal memories of rainbows as well.
*  Of course, everybody's personal memories will be different.
*  These are many different lenses on just a very simple concept.
*  I want to use that experience and all those different lenses to unpack
*  some of the strengths and weaknesses of current AI systems.
*  And also look at how this new AI architecture, the selective state space model,
*  Mamba, state space models more generally compare not only to the AI that we currently have,
*  but to us.
*  I've done the cognitive tale of the tape in the past comparing humans to transformers.
*  A lot of what we're going to do here is talk about the humans, transformers, and now state space.
*  And who knows what comes next future that I think we can start to get a reasonably decent read on.
*  So let's talk about some of the functions that go into that cognition that we just experienced
*  around the concept of the rainbow.
*  Capabilities that we have and we take for granted include the ability to accept multimodal inputs.
*  The main ones for a rainbow in particular that we can take in, we can take in the site.
*  We can actually see the thing itself and we could also see the text which represents the word rainbow.
*  We can hear the word, right?
*  That's how you heard it from me just a moment ago.
*  You heard the word rainbow and even with touch you could, if you're a braille reader,
*  you could have your fingertip interact with an encoding of the language of rainbow
*  and have that rise up to some higher level understanding.
*  So this concept can be loaded in through all these different modalities.
*  Now I think what's also really interesting is that at a high level once this concept is loaded into
*  our brains and becomes the focus of our cognition, it doesn't exist in the same way in which it
*  entered. It exists in a higher dimensional more associative space.
*  All of the different notions that come to mind, that information is not encoded in the word
*  rainbow itself, right?
*  That is just seven letters in the English language.
*  It's just seven bytes of information and yet we can load up such rich understandings.
*  That information is encoded in our brains.
*  It already exists there to be tapped into by this given stimulus.
*  And so we're not just working strictly with tokens.
*  We are working on some higher order concepts, which are not super obvious even today.
*  Like what exactly is the nature of those concepts and how does our cognition work?
*  Obviously that's not a fully solved problem, but it is clear that the cycle of accepting a stimulus
*  in working it up through layers of the neural architecture to the most abstract, the most
*  high level concepts, thinking about it, and then often working back down toward,
*  okay, now what do I want to express, right?
*  That thinking of what happens next seems to happen at this high level beyond words.
*  But then to take action in the world or communicate with others, we have to then translate that down
*  into some lower level thing that could be motor commands.
*  But for the purposes of today, let's think mostly about generating language, right?
*  And we also generate from the studies I've seen just a couple tokens at a time.
*  We have this higher level understanding of what's going on, but our actual words
*  are really rolling off of our, from our brains into our mouths and into the sound with just a
*  couple tokens of buffer.
*  You can think about, you can just understand that yourself by just thinking like you just
*  don't know what you're going to say in the future and where the exact words come from
*  is not super clear or intuitive, right?
*  There is some not fully conscious mechanism by which these high level thoughts that we
*  experience as conscious states get translated into words that can actually be articulated.
*  We also, and this is super critical, this is going to be one of the key concepts to understand
*  for the Mamba architecture and what makes it new and different from its immediate ancestors.
*  But also something that we can do is that we can treat a given input differently
*  depending on its context.
*  Okay, that's super important.
*  So again, we can treat a given input differently depending on its context.
*  So each of those angles that I gave you before, whether it's the mythological or the scientific
*  or the personal memory or a story or a person who loves rainbows, all these different
*  prompts that I can give you, I use that word definitely advisedly, they change the way that
*  you think about rainbow.
*  The rainbow is not loaded in the same way every time.
*  It is loaded in with the awareness of this other information, this other part of the input.
*  And so the high level states that arise as a result are significantly different.
*  And again, you can just understand this through basic examination of your own cognition, I think.
*  Certainly it is pretty obvious to me when I take the moment to reflect on it.
*  And then finally, again, think about this memory, right?
*  I just, I gave short shrift so far to the personal memory.
*  But this is something that, again, we have the ability to somehow reach
*  deep into our own personal history and recall things that we may not have recalled
*  for years, may not have experienced for decades.
*  And so that gives us this sort of long term individual coherence and identity
*  that is in many ways made up of the fact that we can tap into these long term memories.
*  So that's human cognition.
*  Okay, contrast now to the current AI paradigm.
*  On the multimodal front, we now have multimodal AIs that can take in
*  all these different kinds of inputs.
*  The most profound ones, I think, are just the ability to integrate vision and language.
*  That's, if nothing else were happening, that would be a huge deal.
*  But there's a lot more besides.
*  We're going to see AIs that have senses that we couldn't dream of having, right?
*  Talk about just seeing additional colors through additional wavelengths.
*  Just as kind of one very early example of what that might look like.
*  But there's no reason to think that AIs are not going to be able to take in all sorts
*  of signals that we just don't have either the receptors for or the ability,
*  the native ability to parse.
*  And they're going to be able to learn how to take in lots more modalities.
*  This is already well underway with transformers.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Real quick, what's the easiest choice you can make?
*  Taking the window instead of the middle seat, outsourcing business tasks that you absolutely hate.
*  What about selling with Shopify?
*  Shopify is the global commerce platform that helps you sell at every stage of your business.
*  Shopify powers 10% of all e-commerce in the US.
*  And Shopify is the global force behind Allbirds, Rothies, and Brooklynen,
*  and millions of other entrepreneurs of every size across 175 countries.
*  Whether you're selling security systems or marketing memory modules,
*  Shopify helps you sell everywhere, from their all-in-one e-commerce platform
*  to their in-person POS system.
*  Wherever and whatever you're selling, Shopify has got you covered.
*  I've used it in the past at the companies I've founded.
*  And when we launch merch here at Turpentine, Shopify will be our go-to.
*  Shopify helps turn browsers into buyers with the internet's best converting checkout,
*  up to 36% better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort thanks to Shopify Magic, your AI-powered all-star.
*  With Shopify Magic, whip up captivating content that converts from blog posts
*  to product descriptions. Generate instant FAQ answers.
*  Pick the perfect email send time.
*  Plus, Shopify Magic is free for every Shopify seller.
*  Businesses that grow, grow with Shopify.
*  Sign up for a $1 per month trial period at Shopify.com slash Cognitive.
*  Go to Shopify.com slash Cognitive now to grow your business, no matter what stage you're in.
*  Shopify.com slash Cognitive.
*  So what about that higher order, more associative form of processing that I described?
*  It turns out that the transformer is also doing something very similar to the loop that I described.
*  You're taking in an input, working it up to higher order concepts,
*  and then kind of working it down to make a specific prediction.
*  The transformer is actually doing something very, very similar.
*  It is starting from the embeddings, moving through the layers.
*  Starting from the embeddings, moving through the layers.
*  And remember, and especially in the big transformers, there are many layers,
*  dozens of layers that successively process the data step by step until finally it reaches the end.
*  And there is a pretty systematic study now of how the different layers work.
*  And it's quite clear, I would say, from a bunch of different research results at this point,
*  that it is in the middle layers that the highest order concepts are the focus of the model's
*  cognition. Just three results that I'll mention to kind of ground that and you can go check into
*  them more. I've covered a couple of these in the recent AI research podcast. One is the
*  Influence Functions research from Anthropic. They looked at training data and said, how can we tell
*  what training data is most important to a particular output from the model?
*  What they show is that in the small models, with relatively few layers, you have apparent stochastic
*  peritory where the things that are most relevant are those that have the same keywords. So you can
*  see that the understanding is relatively shallow and you can infer that even if the text that is
*  generated passes as correct in some sense, that at least from this analysis, the small models
*  don't seem to have a very sophisticated high level understanding. But the big models do.
*  When you get up to real scale, and we're talking here like tens of billions of parameters, I think
*  Anthropic was working with something in the sort of 50, 60 billion parameter range. By that time,
*  you see now really sophisticated relationships between the inputs that are determined to matter
*  most and the actual work and the outputs at hand. So that's really interesting and they
*  specifically locate that in the middle layers. Another concept is editing and changing the
*  fact patterns that the language models have learned. This is a technique, there are a couple
*  different papers on this. One is called Roam and that one really started to scale up this concept
*  editing work and develop metrics for the robustness of the concept editing, the reliability.
*  And you can do now tens of thousands of concept edits where you, for example, say,
*  Michael Jordan played baseball, right? You want to edit the worldview, the history as the model
*  understands it so that Michael Jordan played baseball, but you want that to be consistent
*  so that it answers that way regardless of what kinds of questions it is asked. You want it to
*  be robust, simple rephrasing and you want other things to stay right, right? You don't just want
*  to replace the concept of basketball wholesale, you still want Larry Bird and LeBron James to have
*  played basketball and they can do all of those things by editing concepts within a transformer.
*  And again, that editing is mostly happening at the middle layers.
*  And then most recently, the representation engineering paper, which was from Dan Hendricks
*  and collaborators, where they start to look at the activations again in the middle layers
*  and ask questions about them, like what kinds of concepts can we identify in this information? And
*  indeed, they find that they can both classify and even start to control model behavior with
*  this growing library of high level concepts, which are represented as a vector direction
*  in activation space in these middle layers of the transformer. So we have pretty good
*  evidence, I think now to say that when it comes to this aspect of cognition, this loop of
*  taking in this compressed input language, you gradually work your way up through the layers,
*  whether in the human, it's through the visual system or through the auditory system, or even
*  through the touch system and gradually get up to these higher level concepts where you have all
*  these associations, you have all this valence and everything is there. And then after chewing on
*  that for a little bit in a way that we don't have certainly perfect self-awareness of, we can then
*  translate that back down into concrete next to a contractions and make language and transformers
*  are doing something very similar. It is weird though, that the transformer does that with a
*  homogeneous architecture. You have the embedding at the beginning of the transformer where you
*  convert your inputs into numbers. Then you basically have the same exact block over and over again. And
*  of course, there's a lot of little variations, but the core concept is really the same every time
*  through every layer that is a multi-headed attention block where the tokens are all
*  computed relationally to each other. And you can figure out what to pay attention to based on the
*  overall inputs. Then you have the multi-layer perceptron, which is dense information processing,
*  but notably that works on a token by token level. Then you also have some non-linearity,
*  some way of filtering out noisy information. And then you have the skip connections and you just
*  layer that block over and over and over again until you hit the scale of the model that you're trying
*  to build. And then at the end, you have some de-embedding reduction to specific prediction
*  as well. The middle is really the same thing over and over again. So I do think that is like
*  remarkably weird that we have created something that doesn't have much specialization of internal
*  architecture. And it's just that the layers themselves end up taking on these different
*  aspects of the cognitive process. There's a division of labor between the layers, even though
*  there's not a difference in form. So I think that's a pretty striking observation. Turning now to that
*  third point, what about the ability to process the same inputs differently? This too is something that
*  transformers can do via the attention mechanism. And it is broadly understood to be a very important
*  part of why they work so well. So how does this work? In the abstract, you can imagine two classes
*  of machine learning architecture, two classes of model. One would be where you have the weights,
*  and the weights again, the weights are the numbers that are learned in the training process.
*  And they are the numbers that are used to transform the inputs through whatever
*  layers or process until outputs are reached. So one traditional, typical, normal AI architecture,
*  machine learning architecture, would just have the weights fixed and just apply the weights
*  in the same way, regardless of what the inputs are. So you feed in some inputs, you convert them to
*  numbers, and then they're just going to be crunched through layer one in a certain way,
*  and they're crunched through layer two in a certain way, and they're crunched through all
*  the layers in a certain way. And the way that those numbers are crunched can just be the same
*  every time, regardless of what the input is. Most machine learning architectures historically
*  have worked that way. If you go watch the three blue, one brown 2017 introduction to
*  neural networks, which is a classic and has some great visualization, I still recommend that all
*  the time, because of just how fundamental and how elegant his explanation is. He does not talk
*  about attention at all. And the types of architectures that he's describing are basically this way. You
*  feed some inputs in, the weights are all there, and the weights just do their thing. Each layer
*  crunches the same way, and that's just how it works. So what's different about the attention block
*  is that inputs have two routes by which they affect the overall process. The inputs are
*  the inputs that get fed in layer to layer through the model, but they also have this other path,
*  the ability to shape what the attention block is going to do. So you may be aware that the
*  attention matrix is different every time, depending on the inputs. That's why we have these different
*  K, Q, and V portions. And first, their nature is determined, and that again depends on the inputs.
*  And then they are crunched against each other. So again, there's two paths by which the inputs
*  affect the number crunching that ultimately happens. They just are the inputs, and then they
*  also affect part of the way the inputs are crunched. That is why the attention matrix is different
*  every time and can't just be totally pre-computed. And this is understood to be a huge reason
*  that the transformers are so powerful. Thinking back again to our experience and the way that we
*  consider the concept of rainbow differently, depending on these compressed supplemental inputs,
*  the different lenses of historical and mythological and scientific and so on,
*  chat GPT can do the same thing. The language models can do the same thing. If you say,
*  explain to me a rainbow through the lens of mythology, you will get a totally different
*  answer from if you say through the lens of optics or the lens of childhood or whatever.
*  This is something that the simpler models can't do. If you have an image classifier,
*  it may have a rainbow class, but it's just applying the same standard computation to
*  every single image and hopefully it lands on the rainbow. It's not loading in all these other
*  associations. And this is what this secondary path of influence from the inputs to the computation
*  ultimately allows for. It's a huge reason. I think this is pretty well established in
*  the literature from a bunch of different angles. It's a huge reason that the attention-based
*  transformer architecture is so powerful. It's that forking path. It's that two ways of the input
*  determining how the information processing happens. It's a big deal because this is what
*  the Mamba architecture unlocks for a totally different class of model. And we're going to
*  get into that in a lot more detail, but before we do, let's talk about the big weakness of the
*  transformer. The big weakness, the information passing that unlocks so much power is also slow.
*  It transformers are quadratic in nature is because every additional token has to
*  have a relationship computed with all the tokens that came before it. And that's a fundamentally
*  quadratic computation process. So obviously lots of optimizations and also approximations have been
*  used to try to work around that. And certainly we have scaled context window up a lot, but
*  basically the state of play is that the full dense, non-approximated attention is still
*  quadratic and all the approximations largely seem a little worse. Often they can work quite well,
*  but they don't seem to work as well as the full dense, no compromises attention. So the weakness
*  of attention there is that it's slow and also that the context window itself, because it is
*  quadratic in the context length, the context windows are fundamentally very limited.
*  Now we've seen that they have grown a lot, right? And at a hundred thousand tokens,
*  you can fit the great Gatsby in. Claude 2.1 is now on the market with up to 200,000 tokens of context.
*  And that is definitely not nothing. It's a lot more than it used to be. Just a couple years ago,
*  we were talking about 2000 token windows and not long before that Bert, I think is 512. So
*  there has been definitely rapid growth in the computing power, obviously that underlies all
*  this. And with that, the ability to extend out these context windows longer and longer.
*  But that's still not that long. A hundred thousand tokens. That's just one book,
*  right? And if you're reading that entire, if you read the great Gatsby,
*  that is the entirety basically of what a transformer can work with at any given time.
*  That also would translate into like a three hour podcast. If I take the transcript of this entire
*  thing, it's going to be most of a hundred thousand tokens. And that's not that much,
*  right? I don't know what my effective token intake rate is per day, but it's a lot higher than that.
*  I hear a lot of audio. I have a lot of conversations. I read a lot of things as well.
*  I have a ton of imagery coming into my cognition. So a hundred thousand tokens,
*  is not much in the grand scheme of things. And for transformers, there is nothing but that context
*  and the weights themselves. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. If you're a startup founder or executive running a growing business, you know that as you
*  scale, your systems break down and the cracks start to show. If this resonates with you,
*  there are three numbers you need to know. 36,000, 25,000 and one. 36,000. That's the
*  number of businesses which have upgraded to NetSuite by Oracle. NetSuite is the number one cloud
*  financial system, streamline accounting, financial management, inventory, HR, and more. 25. NetSuite
*  turns 25 this year. That's 25 years of helping businesses do more with less, close their books
*  in days, not weeks, and drive down costs. One, because your business is one of a kind, so you
*  get a customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts, and improve margins. Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free, and netsuite.com slash cognitive. That's netsuite.com
*  slash cognitive to get your own KPI checklist. Netsuite.com slash cognitive. Omniki uses
*  generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button. I believe in Omniki so much that I invested
*  in it, and I recommend you use it too. Use CogRev to get a 10% discount. You have the weights. They
*  have a ton of information encoded in them, but then they just take their input. They're always waking
*  up, if you will, with total amnesia, and they have a world, to the degree they have a world model,
*  they're waking up with their world model ready to go. But then they're confronting some input
*  that is totally novel. And they have no memory of confronting that input before, and they just have
*  to crunch what they're given to crunch. And they can do it in the super richly expressive way
*  because of the forking path and the multiple ways in which the input can ultimately influence the
*  information processing. But at the end of each episode, when the context window runs out,
*  there really isn't anywhere for that to go. That information typically is just discarded.
*  And then we come back and we use the LLM powered assistant again, another time with a totally new
*  context. So we've got right now a lot of hacks to try to get around that. This is why we have a
*  system prompt from OpenAI. We're custom instructions, as they call it in Chat GPT,
*  because you want to have more consistent behavior. You want to have it sort of know you, but it can't
*  know you. It doesn't have any mechanism to know you. It doesn't have any way to take that
*  context that it crunched in the context of one interaction, one episode, and turn that into any
*  longer term durable memory that it can later use. That mechanism just doesn't exist. So it's
*  fundamentally an episodic technology. And then we have, of course, retrieval, augmented generation,
*  the database, where we can save our logs and start to query back into our logs.
*  But from the standpoint of the model, loading those logs in, that's also still just one episode.
*  It doesn't have a real memory of that earlier episode. It can only just load in a part of it.
*  And however much it loads in, that's context. And you can get into these more elaborate
*  constructions where we save all the logs and then we come through and process them periodically and
*  try to summarize them or synthesize something more useful out of them. That was one of the
*  techniques from the AI town paper that I thought was most interesting. It wasn't so much just the
*  fact that they had all these guys running around and talking, but they were periodically sweeping
*  through all their recorded memories and synthesizing higher order memories, more compressed
*  representations of what those little bots had experienced so that later that could be loaded
*  into context more usefully. But again, it's still kind of just a hack, right? Because it's like a
*  language model, which is purely episodic, processing some memories and creating new language.
*  And then that language kind of getting loaded into a model, it's lossy, right? Language,
*  because it's compression, it's also lossy and it's not necessarily lossy in super principled ways.
*  And this is why the transformer AIs that we have today don't make great companions and don't make
*  great long-term assistance and are not super effective as agents because 100,000 tokens is
*  not that many tokens. If you want to go out and browse the web and do comparison shopping and
*  navigate tricky situations, there's no way for it to learn your preferences, right? To have an
*  instinct and intuition for your preferences, it's not going to have that. What it can have is
*  explicitly declared preferences at the system prompt or accessible through some database that
*  it can query and load in. But it's never going to really know you. It's never going to have an
*  intuition that is inbuilt to understand you or even just itself, its own history. It's just,
*  there is no mechanism. There's nothing but the context window currently under consideration
*  and the weights themselves. You might say that the memory is missing. I think there are paths,
*  by the way, to fixing this within the transformer architecture. And in an episode a few back where I
*  sketched out the future of the transformer. So you can go listen to that one if you want the
*  full deep dive on that. That's outside the scope for today. But briefly, we've started to see these
*  additional tokens built into the transformer vocabulary and then into the training process
*  with some pretty interesting results. There has been the backspace token where with a modification
*  to the loss function, the model can recognize that it's getting out of distribution and add
*  a backspace token and then carry on from where it was before with still the information that like it
*  knows that it took this step and then encountered the backspace. So it can really help with avoiding
*  going off the rails. That's not yet super commonplace from what I understand, but very
*  interesting result. Another super interesting result is the paper, Think Before You Speak. This
*  was the pause token, the thinking token. The idea was that, hey, if we just give it some extra
*  tokens without necessarily having to do anything, but just allow it to crunch a thinking token,
*  train it when it's appropriate to do that, then maybe that can bring about better performance.
*  And sure enough, it does. And so from that, I imagine, geez, maybe a memory token could also
*  make sense. How exactly does that memory token get created is not super clear, but you can start to
*  imagine that you might load in tokens, especially because we've seen this in the multimodal context
*  so often, right? The ability to bridge from one space to another means that you can take an image
*  and convert it into language space. And even with the frozen vision model, frozen language model,
*  you can just train a small adapter such that the language model natively knows how to interpret
*  the output of that small adapter because you've literally transformed image into language space
*  and to the model it is understood as language. Even if no vocabulary could get there, you have
*  that ability to shape information into language space so that the language model can work with it.
*  I think there's something very similar to be done with memories to compress some of the history
*  into maybe just one token, how much memory you can fit into one token, who knows, but clearly
*  you can fit in a lot more than just one word. We know that from the image work. So exactly what
*  the nature of this memory compression is likely to be is unclear. I can see the beginning of a solution
*  on the transformer mainline AI development path right now, just based on these other kind of
*  behavioral tokens, I can see a memory token also really starting to work. I haven't seen that yet
*  in the research, but I do think it is conceptually possible. But in the meantime,
*  somebody has invented a better way. And this is now bringing us to the real subject of today's
*  episode. So the paper that announces all this is called Mamba, linear time sequence modeling
*  with selective state spaces. This is just two authors, Albert Gu and Shri Dao. You may recognize
*  those names. And it is a real tour force. I mean, what two individuals have done here,
*  I think, has pretty good chance of rising to the level of that canonical attention is all you need
*  work, which remember did not invent the attention mechanism. But in fact, abstracted away a lot of
*  previously complicated detail and demonstrated that the attention mechanism itself in just this
*  very basic form was enough to do basically all the tasks that people were trying to do.
*  It turns out it was not all you need for all tasks you might want to do, but it was all you need for
*  the measurements and the ability to examine or characterize the language model that they had
*  available at the time. This is a big deal. Let me first just talk about who the two authors are a
*  little bit. They are both professors. Albert Gu is an assistant professor at Carnegie Mellon.
*  He's also the chief scientist at a company called Cartesia AI. And his Twitter bio simply says,
*  leading the SSM, that is the state space model revolution. The other author is
*  Shri Dao. And he is also an incoming professor at Princeton. He is also a founding chief scientist
*  at an AI startup called Together AI, which has raised $102.5 million Series A. And his expertise
*  is really in performance, super close to the metal, highly optimized algorithms for really making the
*  most of your GPUs. If you know his name, Shri Dao, you probably know it from Flash attention. And
*  Flash attention was a major advance in how attention could be computed without any sort
*  of approximations, really doing the full computation, but doing it in a way that worked
*  much better just based on how the data is shuffled around and what moves to different parts of the
*  overall GPU physical hardware. Finding a better way to do that made it just dramatically more
*  efficient and has been a huge unlock and major, major compute savings. So these are the two guys.
*  It's the leader of the state space model revolution, and it's a really accomplished
*  hardware expert. And that's Albert Gu and Shri Dao. So what's the big difference here?
*  It all starts with the concept of the state. The thing about state space models that is so different
*  from what we have now come to understand as a norm in the transformer is that it has an internal state,
*  a state that evolves through time and also propagates through time. Okay. So one way to
*  think about it is that it is something that outlasts the single interaction between the weights
*  and an input. So if a transformer has all these weights and it takes an input and they interact,
*  and yes, there's that fork, but there's not really anything else, right? What the state space model
*  adds to this at a conceptual level is the idea that, okay, yes, you have your weights and you
*  have your input, but you also have an internal state. And the nature of the calculation now becomes,
*  I'm going to process both the last state and the new input by the weights to get not just an output,
*  yes, an output, but not just an output, also a new updated state. And so this state becomes a long
*  lived thing that can go on and on through time. With all this motivation, it should appeal to you
*  as something that's like, hmm, this state can go through step after step and it propagates through
*  time. It's not the output, but it is a modified state that is used to calculate the output at
*  each step. Like immediately, I think, hmm, this sounds like there might be something there that
*  could help solve the memory problem. And indeed these state space models, they have some real
*  strengths. People have been working on this for the last couple of years. There've been a whole
*  bunch of papers about it, bunch of results. It does have real strength when it comes to extended
*  memory. There are specific benchmarks that try to test this where you have long strengths.
*  And these often have been historically programmatically generated. And there are tasks
*  like, here's some sort of expression, which may have tons of parentheses in it and brackets and
*  curly brackets. Code is like this. In arithmetic, you can just write out infinite arithmetic with
*  whatever sort of open bracket, open parentheses notation. And then in coding, you have to close
*  those things. So the challenge then becomes for the AI, can I give you this giant long sequence of
*  all of this stuff with all these order of operations, open parentheses, open square brackets,
*  and can you close it? Can you close that in an effective way? The state space models have
*  dominated this category. This is one of the few things where the transformer is not supreme. And
*  the big reason is that these things can get arbitrarily long. And it's really hard for the
*  transformer to keep up with these arbitrarily long things like some of them just can't do it.
*  There's literally no way. So the state space models have already shown even prior to this
*  state space moment that there is a role for them, that they do have some really desirable
*  memory properties that the transformer does not have. Now, how this works is actually pretty
*  complicated, but also principled. I followed references back to an earlier Albuquerque and
*  Tridau collaboration in that case with other authors as well. And the original HIPPO paper
*  HIPPO H I P P O it's called describes how long sequences can be compressed into really small
*  state representations using a process of projection onto a basis of polynomial functions. Now that's
*  complicated math, but the way they evaluate memory back in this original paper is for its
*  ability to memorize and arbitrary noisy input sequence. And there are different ways of doing
*  it where you wait more recent data more heavily or wait all data the same. But what they show is that
*  you can create a slightly lossy yes, but still extremely useful representation of a sequence
*  extremely efficiently by representing them in this way. And by the way, they have some pretty nice
*  scaling properties too. So there's motivation to work on this because the structure of the computation
*  is actually in many ways a lot more favorable than the transformer. Each inference step takes the same
*  amount of time constant time inference. Why is it constant time? Because you have a state and the
*  state is of a fixed size. Okay, that's important. The state is of a fixed size. It changes through
*  time, but it doesn't grow through time. So the state because it's of a fixed size and a new token
*  of input, those two can be considered to the inputs. They are processed by the weights,
*  an output token is generated and the next state is also generated. And that takes the same amount of
*  time, regardless of how long the sequence historically has been, because the state itself
*  doesn't grow. That's in contrast to transformers, whereas the context grows, you have this
*  quadratic nature of the computation. There are caching strategies that help. You're just able to
*  cache the parts that you already did. So you don't have to redo it with every single token. But
*  fundamentally, you still have that quadratic calculation. The state space model though,
*  it's constant time inference because the state itself does not grow. It evolves, it changes
*  from step to step, but it does not grow. So constant time inference, that's great. And then
*  that also means linear scaling with the sequence length for the purposes of training. So this is
*  awesome, right? Like this is much better. If each step takes the same amount of time, then you're
*  at a fundamentally different regime than if each step is starting to take a little bit longer than
*  the last step. Huge difference. Okay. So what's the problem? Well, historically, the problem is
*  they just don't work as well. You've got these few areas, these kind of oddball parentheses,
*  closing tasks that the state space models do really well on. But for most language modeling tasks,
*  that is to say like all the stuff that Chess GPT can do for us that we find so much value in the
*  transformers for, the state space models just haven't been as good. Interestingly, I think that
*  the authors of this paper do really give you a pretty good sense for their motivations for this
*  work in conceptual terms. It's not as accessible as what I'm presenting here, but this is such a
*  true or false because it begins with such high level conceptual insight. And then they go so deep
*  all the way down to this super low level code, which is by the way open source to actually make
*  the implementation of it work. But just starting at the very high level, they're like, you know,
*  all these state space models that we've been using so far, you have been of the simpler class, where
*  the actual layer by layer transformations are fixed. And the information just flows through it.
*  They don't have that property like the transformer has. And like the brain obviously has
*  where the nature of the computation that is by what numbers will the inputs be transformed.
*  The states based models have not had that ability to do that dynamically. So that really limits
*  what is sometimes called expressivity, just how rich, dynamic, powerful can they be.
*  Their motivating observation is that the states based models have probably been limited by that,
*  that they can't match the transformer because they just don't have the same
*  multi-path means for the inputs to affect the information processing that unlocks the power
*  in the transformer. So you might wonder, well, why is that? You know, why were they designed that way?
*  And historically, as I understand it, the reason has been that that was the only way to make the
*  feasible, you know, in reasonable with reasonable resources and time. The math of this can get
*  pretty abstract in terms of the notation. But basically, the states based models that have
*  come before have been designed so that they can be represented and computed in parallel, and also so
*  that they can be represented and computed in a recurrent fashion. The parallel form is called
*  the convolution. And that's less important for non-technical folks than the idea that there is a
*  way with the traditional states based models to do the calculation that is highly parallelizable.
*  And that's obviously super desirable to transformers also highly parallelizable,
*  which is a big part of why it's been able to scale with GPU infrastructure.
*  So the states based models, people want to do the same thing. Can we make this highly parallelizable
*  so that we can hopefully scale it? And yes, you need to have the convolutional form. And then you
*  can do this calculation in a highly parallelized way. And that's by the way, you use mostly for
*  training because you have these like large established batches of what the text is. You
*  want to process that in batch. You don't want to have to do literally just one token at a time.
*  That's pretty annoying. So you have to have this convolutional form, which allows for this high
*  level of parallelization. But then when you switch to inference, then it does become a recurrent
*  process. Inference, next token prediction, you're just predicting one token at a time. This is
*  called auto regressing, where you're taking your token, feeding it back in as input and running the
*  same process over and over again. The loop is feeding the output right back into itself as input,
*  but it is still only just doing one token at a time. And you really can't parallelize beyond that.
*  So you'll see the training and also if there's a long prompt, then the initial mode could be
*  convolutional in structure and parallel in computation. So that can happen quickly.
*  And then when you're actually like generating new stuff, you have to go one token at a time anyway.
*  So that's the recurrent form. So all these state space models had this dual nature. They wanted to
*  have the parallelizability. But then of course, at runtime, you're going to generate one token at a
*  time. So here's the key dual breakthrough for the Mamba paper. They said, okay, is there any way
*  that we can broaden what a state space model can be so that the calculation that is done
*  is influenced by the inputs in kind of a similar way to what the transformer does.
*  We want the inputs not just to flow down a assembly line, so to speak, where they get
*  transformed by exactly the same numeric machinery each time. But we want the nature of the
*  transformations as we go down the line to also depend on what the inputs happen to be.
*  How can we make that possible? Keep in mind, these state space models are a little bit different.
*  You have the state as it currently exists, and then you have a new input. And then those get
*  processed by some parameters such that an output gets generated and also a new state.
*  You can look at the diagram in the paper. Ultimately, if you are just generating content
*  with this, then you're again feeding each output back in as input. But you're also feeding the new
*  state in as input. And the old state, you let go of, right? It just goes away. The state has evolved.
*  The state has changed. So what they decided to do is say, okay, what if we let all these parameters
*  and what if we let the transformations that we're going to do to the state and the input
*  depend on the input itself? That's like, on some level, a conceptually simple thing to do.
*  This is like a relatively small change in the equations that define the architecture. But
*  the key problem with it is that now you truly can no longer have a convolutional form. And so the
*  computation is no longer in the way that it was. So you're now really constrained to the recurrent
*  form. And so you might think, well, geez, that's just like not going to ever work. We have to be
*  able to parallelize in order to really make this scalable. And this is where Tree Dow, one of the
*  leading experts in the development of these super efficient low level algorithms comes in. So
*  what they do here is they call hardware aware algorithm design. Parts of it will be beyond
*  the scope, but I want to at least take a little bit of a dive into this to give you some intuition
*  for what it is. And then there's plenty of room for greater depth of study beyond this as well.
*  The hardware that they use is the Nvidia A100. And that is a state of the art machine until
*  recently. It's been superseded now by the H100, but the A100 is no slouch. It's just one generation
*  behind the latest H100. And it's been the standard, you know, it's what GBT4 was trained on, for
*  instance. So it's a big machine. It costs thousands of dollars. It runs at 400 watts, which is not
*  nothing. That's only half an electric teapot when it's boiling your water, but it's like
*  20 light bulbs in today's world. So it's not nothing, but it's also not like a huge machine,
*  thousands of dollars, you know, 20 light bulbs worth of energy. And what they really try to do
*  is figure out how can we organize this computation so that it can work fast on this machine,
*  knowing all the specs and knowing that we have a world-class expert in tree doubt in terms of
*  writing the CUDA code that is going to manage how this information moves around
*  in a very strategic and ultimately effective way. What they do is, first of all, they look at the
*  nature of the chip. They note that there are two kinds of memory that are available on the GPU.
*  And this might even be a little bit of a simplification because there could be some
*  even in between from diagrams I've looked at. But the two that they really call out are the SRAM,
*  which is also called the SM or the shared memory. And then they have the HBM, which is the high
*  bandwidth memory. And these are two different kinds of memory that serve very different
*  purposes. Actually on the A100, there are 6,912 CUDA cores. Those are the actual processing unit
*  that do the math, right? That do the multiplication and addition that ultimately
*  constitutes the matrix multiplication that ultimately constitutes all this stuff. There's
*  6,912 of those on a single A100 chip. The shared memory or the SRAM, this is the memory that is
*  absolutely closest to those cores where the actual number crunching takes place at the very lowest
*  level. There is this SRAM shared memory right next to that, highly integrated with it.
*  And amazingly, not that much of it. The amount of SRAM on an A100 is just 164 kilobytes. 164
*  kilobytes. That is with one letter being a byte, that's actually less than the context window on
*  the leading LLMs. But that is the memory, limited as it is, that the cores communicate with most
*  directly. And that's the absolute fastest access memory that they have. The next level of memory
*  out, the high bandwidth memory, that is the much bigger memory pool. On the A100, it's 40 gigabytes
*  of memory. Okay, so that's obviously qualitatively different, like five orders of magnitude-ish
*  greater. So totally qualitatively different thing. This is where the parameters get stored.
*  When you have these giant models, however many billion parameters you're talking about,
*  you multiply that by a sort of integer factor. It depends on the quantization, like how big the
*  numbers are in terms of how many decimal points they have. But basically, if you think of a number
*  as a couple of bytes, how many billion parameters do you have? And that's going to tell you how many
*  gigabytes of space it's going to take up. So 40 gigabyte A100, actually not even enough to run.
*  That wouldn't be enough to store the entirety of GPT-3 weights. 175 billion parameters is going to
*  be bigger than 40 gigabytes of memory. So that used to get into arrays. And again, there's a
*  lot of intelligence to how do those parameters get loaded in? How do they move? We don't want
*  to be waiting on them. There are bottlenecks everywhere in this process. So you've got the
*  course where the actual number crunching happens. You've got the SRAM, which is the memory that is
*  small, that is most closely integrated with that. And then you've got the high bandwidth
*  memory outside. That's where the parameters are. You're going back to flash attention.
*  The advance there was figuring out how to manage, how to better manage the movement of the parameters
*  from the high bandwidth memory into the SRAM and back and exactly what order that movement
*  and that calculation should be done to really get the most from the hardware. The naive interpretation
*  it turns out way less good than flash attention. And you really have to understand the design of
*  the chips. You really have to understand CUDA at a deep level to be able to write this level of
*  optimized code and treat out how many people in the world can do it, but he is one and certainly
*  one of the best. Okay. So what is the hardware aware algorithm as it exists today? Well, the big
*  thing seems to be that the state, the model state never comes off of the SRAM. It is only dealt with
*  in that highest speed, closest to the core memory. So the parameters of the model, those will sit in
*  your high bandwidth memory. The inputs can then be used to interact with those parameters so that
*  they are different each time, right? So that it's not just this super consistent assembly line type
*  of thing, but where the individual stations or the layers, as you go down that assembly line,
*  actually do different things depending on the input that process inevitably, because there's
*  a lot of parameters involves accessing those parameters on the high bandwidth memory, but the
*  state itself, this thing that propagates from one inference step to the next holding its size
*  constant, right? Evolving its value, evolving its content, evolving what information it contains,
*  but holding its size content that stays in the SRAM all the time and is not, unless you intervene
*  and say, okay, we want to extract this information. It's never exported off of the SRAM from state to
*  state at all. And that seems to be the big unlock that allows the Mamba architecture specifically
*  to run fast. Okay. So this hardware aware algorithm, this hardware aware management of the state is
*  super key and it's super technical. Without it, if you had just been a naive implementation,
*  this thing would be too slow to run. It would not be effective, would not be scalable because it just
*  can't run fast enough. So again, the code for this is all open source. They have a repository out
*  there, but I am not a CUDA code expert by any means. I did copy some of it into chat GPT and
*  start to orient myself to it a little bit that way, but it's out there and it's super, super
*  detailed, hyper optimized code, super, super technical. A core idea, again, just keeping the
*  states on the SRAM so that doesn't have to come on and off all the time using up the bandwidth
*  between the high bandwidth memory and the SRAM to give you just a little bit of a sense of
*  additional techniques. They highlight a few, one called kernel fusion, which is basically when you
*  have multiple different transformations, depending on the nature of the linear algebra and how the
*  transformations relate to each other. Instead of taking an input, multiplying by matrix A,
*  then getting the result and multiplying by matrix B, you can often reorder the computation. So you
*  do the matrix A and B interaction first, and then you have one net thing that you can apply to each
*  of the inputs, right? That's obviously highly simplified, but that kernel fusion concept is
*  taking multiple transformations and collapsing them into a single transformation that can only
*  happen under certain conditions. It can be really complicated to do, but again, if you want to
*  maximize the performance, then this is like a pretty core and well-established technique.
*  Another big one that they do is called re-computation. So this is in training,
*  because you're trying to minimize the traffic between the high bandwidth memory and the
*  SRAM to make things as fast as they can be. You don't really have the ability to save all of the
*  activations or save all of the gradients along the way. So they use a different technique,
*  which is called re-computation, where they basically compute the activations and the gradients as they
*  do the backward back propagation step, which again, takes more compute, but less moving of data around.
*  And it turns out that the moving of data around is the more pressing bottleneck. So actually
*  re-computing certain things in these instances can be much faster. You want more on that? You're
*  going to have to dig in yourself and get deeper. But zooming out again, the upshot is with a
*  hardware-aware algorithm, they've made such a dramatic performance improvement on the way that
*  state space model calculations can be performed, that they're able to support this greater
*  generalization, this multiple paths for the inputs to impact the nature of the information
*  processing much more transformer-like. Also, again, human brain is clearly doing something like this.
*  They're able to support that despite the fact that it means no convolutional form can exist,
*  and therefore your parallelization is greatly limited. They're able to support that because of
*  this super hardware-aware, super sophisticated, low-level algorithm design. And with that all
*  sorted out, it actually allows them to begin to scale. So they have trained a bunch of different
*  models to a couple of different modalities. And for language modeling, they're doing this on a
*  couple of relatively small models, a one and a half billion parameter model and a three billion
*  parameter model. And they go up to 300 billion tokens trained. That's a pretty decent number.
*  It's a long way from state of the art. GPT-4 was generally thought to be trained to like 10
*  trillion tokens, which would be 30 times the 300 billion that they did here. Lama 2 was trained
*  to like 2 trillion tokens. So this is also still like an order of magnitude lower than the Lama
*  models, even the small ones. But it's also not trivial, right? To train up to 300 billion tokens,
*  that shows that there is some scalability, but it also gets you far enough down the loss curve
*  that you can start to get a decent sense for, okay, just how good is this thing?
*  And this is the thing that made the headlines, right? These are the curves now that we can say,
*  huh, this seems like a really big deal because they are beating transformers on language modeling.
*  To say that's a big deal would be definitely an understatement, right? Again, going back to
*  the very beginning, one of the most common, super big, super high impact questions that I'm asked is,
*  are we going to see something better than the transformer? And here we are seeing something
*  that is marginally better than the transformer. They look at this in terms of flops, training
*  different architectures with the same number of flops and comparing the loss curve. They show that
*  basically, if you have a short sequence length, the Mamba architecture just slightly seems to
*  outperform the best transformer version that they use. But again, one of the authors here is somebody
*  who created flash attention, so they should have a pretty authoritative take. If you had a
*  naive implementation of any of these things, you could cook the books. But they have a vanilla
*  transformer in this paper and then also a transformer plus plus, which they describe as
*  the best transformer training recipe that they know. And basically the Mamba on the 2000
*  token sequence length just basically exactly matches it. And then they look a little beyond that,
*  now start to look at an 8,000 plus token sequence length. And you can see there's actually a little
*  space now between the Mamba and the transformer where the Mamba is lower, has lower loss, lower
*  perplexity. So this is right off the bat, a big deal. This is like, wow, on these core measurements
*  of just broad pre-training, as far as it's been scaled so far, and this is out to like 10 to the
*  20 flops, they are beating the transformer. This is like still five orders of magnitude from GPT-4
*  in terms of flops. But if you've studied the scaling laws, you know that one of the big
*  findings over the last couple of years that has guided so much of where the big investments have
*  gone has been this observation that scaling laws do kind of work. I would say that there is a lot
*  more scaling to be done, obviously, from 300 billion tokens to 10 trillion and beyond. There's
*  a lot more parameters that you may want to have in the model eventually over time. There's a lot
*  more to be explored in really all different dimensions of this. Like you can't predict the
*  exact behavior of an AI based on pure flops, but with a reasonably high level of confidence,
*  you can predict the aggregate loss. Those curves are actually pretty smooth and pretty predictable.
*  So if you see something that is beating the best architecture, even in a somewhat low flop regime,
*  and you can see that it holds from 10 to 18, 10 to the 19, into the 10 to the 20
*  flop range, then you have a pretty good chance that it's going to extend into higher orders of
*  magnitude as well. Given how solid scaling laws have been and how these curves look where they
*  have a very similar shape, it seems to me quite likely that we will again see a pretty predictable
*  scaling law that can be developed for the state space models as well, and that it probably will
*  carry on a few more orders of magnitude. They also do, and I'm going to get into this in too
*  much detail, but they also do other modalities in the paper. The one that I think is the most
*  interesting is DNA because naturally there are long sequences. Why am I harping on sequence length,
*  just as a reminder, because this whole thing is about solving memory. So you can compare
*  2000 sequence to the transformer 2000 sequence, but the transformer does well at 2000 sequence.
*  You can do that again at eight. And these days the transformer does well at eight,
*  but the transformer can't go to a million very easily. So why did they not test language
*  on longer sequences? My guess is because there aren't super readily available longer sequences
*  of language just ready to go for training. This is something that perhaps they could clear up for
*  us a little bit, but then they did go on to do training with super long sequences on DNA up to
*  a million tokens. And what is so striking about their result with the million tokens on DNA is
*  that they don't see performance loss even as they go up to a million tokens and basically no other
*  architecture has that quality. Every other architecture that they study as the sequence
*  length gets longer, they see a significant drop in performance. But with the Mamba architecture,
*  even up to a million tokens, they see improving performance. This is a huge deal, right? Again,
*  the whole point of this or the whole motivation, the whole reason I think this is such a game
*  changer is because I think this unlocks the ability for models to start to develop longer
*  term memory. I think a lot will flow from that too. A million tokens is a lot, right? It's five
*  times longer than the state of the art transformer. And this is just the very first paper on the Mamba
*  architecture. So there's some other stuff in there as well. They work on audio. They have some kind
*  of toy problems that are interesting to look at that kind of show how the previous state space
*  models just couldn't do certain things at all. But the new design that they have does work.
*  And this is where they also, by the way, introduced the concept of selectivity. The state space models
*  in the past were what the authors call linear time invariant, which is a fancy way of saying that
*  the inputs proceed down an assembly line and they get transformed in exactly the same way,
*  regardless of what they are. Whereas in contrast to that, the new thing with the selectivity
*  mechanism that they introduce, that's where you now have different transformations happening
*  as the data gets processed, again, depending on the input all within a single inference step.
*  So key points, it's beating the transformer on these kind of familiar comparisons where you can
*  say, Hey, what does it do at 2000 sequence? And what does it do at 8,000? And let's take that up
*  to at least 10 to the 20 flops. And then they're also seeing these really remarkable demonstrations
*  on both the toy problems and on these DNA tasks where the longer the sequence gets, the more the
*  model improves. I think that's just a really, really interesting phenomenon from which we can
*  start to see through the fog a little bit and hopefully figure things out.
*  One of the really interesting aspect of all this is the inference throughput on the A100.
*  They show that the batch size that you use influences tremendously how much throughput you
*  get. The GPU is built for extreme parallelization. If you're just running one autoregressive sequence
*  through an A100 80 gigabyte chip, you are not getting the max out of it. And that's true across
*  any of these architectures because it can parallelize more than just a single autoregressive
*  unrolling can parallelize. So they show that with their Mamba 1.4 billion parameters that you can
*  just run a bunch of individual autoregression inference processes at the same time. And it
*  looks like an A100 can handle essentially 64 concurrent inferences really without any trouble.
*  And that's where it seems to max out its parallelization. But these are all better than
*  the transformer. It's all higher throughput than a transformer of similar size. So a big deal. Now,
*  again, the transformer a little bit more parallelizable. You can have a bigger
*  transformer that sits on multiple different devices. And it's not clear exactly how that's
*  going to work as people try to scale up Mamba, right? Because you have this state and it's in
*  the SRAM and you're minimizing this input and output. So I think there's definitely more
*  work to do there on exactly how it might scale beyond say 7 billion parameters. But 7 billion
*  parameters is already quite a lot. A lot of models are working at that scale and doing
*  important things. And the throughput is just much, much higher on this single A100 with the Mamba
*  architecture as compared to the transformer. We've got a lot going for us here, right? We've got
*  something that is demonstrated even before this work to have much better long-term memory properties,
*  but just wasn't generally powerful enough to be competitive with transformers.
*  Now we've got a conceptual generalization of the state space model that puts it into transformer
*  territory and perhaps even a little bit better on these core language modeling tasks. Huge deal.
*  It does come at this cost of not being as parallelizable. You have to do it in recurrent
*  form, but hardware aware algorithm design makes this feasible in a way where it is actually faster
*  than the transformer, at least up to the scale of the devices that we have. And it's again
*  demonstrated that the longer sequences, the better it works. With DNA, we're talking up to a million
*  with these toy problems, again, up to a million tokens. That is a big, big deal. There's one more
*  thing in the paper that I think is interesting as well. They also try just your very first thing in
*  terms of integrating the state space model and the attention model. What does that look like?
*  They basically show that if they interweave the Mamba and the multi-headed attention
*  architecture together, then it further improves the performance a little bit. Not that much,
*  but it does in fact improve the performance. And you can just see clearly that the loss curve is
*  just a bit lower. And they say the Mamba multi-headed attention architecture is only
*  slightly better, which to me is like, okay, yeah, maybe it wasn't that much better, but like it is
*  visibly better. The loss curve is lower and you've only tried one basic interweaving approach and
*  already it was better. So I think there's a lot more where that came from. Okay. So what else do
*  we know? Right? Well, the paper was published. There's also the code repository that is published.
*  There's also the model that is published that is trained up to the 300 billion tokens. Your 2.8
*  billion parameter model is something like six gigabytes and now people are starting to work on
*  it. So an obvious question would be what other techniques that kind of already exist work with
*  this model? Interesting data point on that is that there have been already a couple of people who have
*  gone out and fine tuned it. One that I've spent the most time with is a project called Mamba Chat.
*  Haven HQ is the company behind this. Haven is all about helping you fine tune models for
*  specialized tasks. Justice Maddern is the individual. So they dive into this and basically take
*  a pretty simple approach to doing the fine tuning. It seems like the core
*  libraries there mostly work with a fine tune on 16,000 chats out of a data set called Ultra Chat
*  200K. You get a Mamba Chat model and in your browser, in a Google collab notebook, you can run
*  this Mamba Chat. So I've spent a little bit of time doing that sitting and just looking at the
*  performance of the Mamba Chat. Basically the chat works and it can chat with you very normally.
*  It seems to know stuff. It can be induced to hallucinate. It summarized very effectively for
*  me at 500 tokens, no problem. At 1500 tokens, no problem. At about 3000 tokens, it seemed to lose
*  coherence. And I was quite interested in both. This thing is built for long-term memory. Why doesn't
*  it seem to handle long sequences well in text? And basically what I came to trying this in an
*  reading all the papers is that it has been trained on long-term text. The magic of the
*  state space model, which we do see demonstrated in these other modalities like the DNA and the toy
*  problems, is that it can carry information forward via the state indefinitely, but that doesn't mean
*  it will. And in fact, the average length of chat in this Ultra Chat paper is 1,467 tokens to under
*  1500 tokens. That is super small compared to today's even just context windows. We do see that
*  the model is able to go beyond that length, but not dramatically beyond that length. And I think
*  if there's one thing that should keep us all grounded, this is the thing that is least well
*  proven as of now and where there is a little bit of a leap required. So that is definitely worth
*  keeping in mind as a possible reason that some of my downstream inferences and speculations
*  may not actually work. My experience also in terms of using this on Cloud was that it was like
*  sometimes fast, sometimes slow. I wasn't able to get an A100, which is the hardware
*  that is used in the development. Instead, what Google Cloud gave me, even with my paid account,
*  was a V100. That is one generation before the A100. So it's not like a slouchy machine, but it's not
*  on par with the A100 either. So not exactly sure how to interpret the speed. Sometimes it seems
*  quite fast and other times it seemed quite slow. Just for like objective comparison, the V100 has
*  96 kilobytes of shared memory as compared to the A100's 164 kilobytes. So it's a little more than
*  half. In any event, it is clear that the recurrence is a fundamental limitation on like just how fast
*  this thing can work. And even from the paper with a single A100, they expect that you will get
*  58 tokens per second if you're just running a single line of inference. 58 tokens per second
*  is faster than you can read. So it's fine. We speak at 150 words per minute. Most people can read
*  a couple hundred words a minute. Speed reading, you get until three, four, five, 600 words
*  a minute. So it's comfortably faster than you can read with the 7 billion parameter scale.
*  If you imagine a 20 billion parameter scale, it's not exactly clear how much that will slow down,
*  but let's just say you get down to 20 tokens a second. Now, maybe you're actually kind of
*  waiting for it as an individual user. And certainly if you're doing like background processing,
*  the latency does start to become a factor. At Weymark, for example, when we generate a
*  video script for somebody, we may be generating a thousand tokens. And this might be the kind of
*  thing that could take the better part of a minute. So it isn't trivial. The latency is still an issue,
*  even with this like hardware aware design. And I wasn't fully able to characterize that
*  in my own experimentation on Collab, but fine tuning basically works. The libraries, the data
*  sets, the ability to like get it to be a chat assistant, really no obvious problem there.
*  Summarization seemed to be limited by not having been trained on super long context
*  and speed was hard to assess. But again, I want to zoom out a little bit and just consider the fact
*  that maybe these head to head comparisons are kind of missing the point or at a minimum,
*  they're just scratching the surface of what we should be thinking about. Because the way these
*  results are reported is that, okay, this Mamba architecture outperforms the transformer. When we
*  train it on 2000 or 8,000 sequence. And again, the 8,000 is more outperformance than the 2000,
*  which is almost indistinguishable. So as we go to long context, we are seeing advantage, but these
*  are pretty standard transformer measurements. And you're not necessarily playing to the Mamba
*  architecture's strengths. If the whole point of this is that it can have long-term memory
*  in a way that the transformer just can't, because it has this state that has long lived going
*  through time. I would just emphasize that none of the tests are really meant to test that. All of
*  these benchmarks are things that like transformers can do. None of them really are things that are
*  fundamentally different from what the transformer can do. And so there may be whole areas where
*  this Mamba architecture, especially as you start to think about long-term memory,
*  there are probably all sorts of things that the Mamba architecture can do that the transformer
*  just can't do at all. And this is where I want to start to get into somewhat more speculative
*  scouting work, but hopefully you'll agree pretty well grounded and likely enough, I think, to happen
*  that this is something we should start to take seriously and plan for.
*  What can we do with this state space architecture that is now as expressive, as powerful at the unit
*  level as the attention powered transformer, but which has potentially a lot of different surprises
*  and nuances and idiosyncrasies left to be discovered? Remember just how many things we have seen
*  that are just plain weird about the transformer AIs. I suspect that we may see similar amounts of
*  surprises from state space models, but it seems quite clear that we can take this architecture
*  and start to think about breaking out of context windows, that we can think about new training
*  strategies that are designed, engineered data sets that are designed to encourage long-term
*  coherence, to encourage adversarial robustness, to make the model behavior more predictable,
*  because you have this ability now with the state to encode long-term context.
*  We've really only barely scratched the surface of that kind of data set creation. Again, the chats,
*  used to do the fine tuning, 1,400 tokens. That's nothing. That's a handful of back and forth total.
*  A book, the Great Gatsby, is almost 100,000 tokens. That's nothing in the scheme of what a human
*  process is. These architectures have been demonstrated up to a million, but the loss
*  curves were still going down at a million. There's a pretty good prospect, I think,
*  that we could start to think of millions, maybe even tens of millions.
*  And then again, I think maybe all this is missing the point if we try to frame it as
*  state space models versus transformer. Is Mamba the transformer killer? The answer there is almost
*  certainly no. These different architectures, as I hope now is starting to become more intuitive,
*  they are fundamentally different things. They do things in fundamentally different ways.
*  From that, it seems very likely that they will have fundamentally different strengths and weaknesses.
*  All of this analysis so far is largely conducted on what you might think of as the transformer's
*  home turf. It's all on short sequences. It's all on familiar benchmarks. These are the things that
*  we test because these are the things where transformers have traction. We don't go to these
*  super long sequence things because the transformers don't really work on them. We don't even really
*  have the data sets. There are a couple, but there are not all that many. So when you see that the
*  Mamba architecture is outperforming the corresponding transformer almost across the
*  board on all these benchmarks that are fairly standard in the field, then I think you have to
*  also keep in mind that we're not yet even really playing to this new architecture's strength.
*  There is, as we broaden our thinking about how we might use this thing, we are likely to see
*  that there are areas where its outperformance is even bigger. And we might also see, by the way,
*  some areas where its performance is inherently less. So in challenging myself to, well, what is
*  probably worse about this state space model paradigm compared to the transformer? I think the most
*  fundamental thing is that the state carries all the information from the context or the episode
*  into each inference step. If important information was let go in a previous inference step,
*  then it will no longer be available in the state for the next inference step.
*  So that's a pretty important one, right? It's like you have a long term memory,
*  but once you let go of something, it's gone. That's going to create some pretty different
*  dynamics, I suspect. I would guess that a state space model, for example, might be more likely to
*  just simply miss some things or appear blind to certain details. And attention mechanisms are not
*  always great at this either, but because they do compute every token in relation to every other
*  token, if you are looking for like a diamond in the rough, or if you load in the great Gatsby
*  into Claude and you put one weird sentence in there and you say, spot the weird sentence,
*  at a minimum, you can say that the attention mechanism is computing the relationship between
*  those tokens and all the other tokens. And it's likely to pop something up weird when it does that
*  such that it can probably identify the right thing. I don't think that comes for free. I think they
*  train on that stuff. They train on increasingly long sequences to create that long-term coherence
*  in the transformer, but you do have that every token to every token. So to spot a diamond in
*  the rough, you have the opportunity to make sure you are looking at every token as the challenge
*  arises. In contrast, if you're using a state space model and you've processed a bunch of information,
*  gone through a bunch of history, and at each step along the way, the state is evolving,
*  and that means incorporating new information and encoding it into the compressed form that is
*  safe, but it also means letting go of information over time. Then once it's gone, it's gone. You may
*  not be able to say, oh, hey, sometime back in this episode or in this context, there was something
*  weird. Can you now tell me what's weird? It may have just identified that as an anomaly at the time
*  and let it go such that you may not be able to retrieve that. So I'm starting to get a little
*  bit speculative here, but I think this brings us to the question of what's next. And I think there
*  are two big things that are really going to be next. There is going to be the sculpting of memory
*  and there is also going to be the remixing and the recombining of architectures. And again,
*  remember, even in the Mamba paper, the Mamba interwoven with multi-headed attention is the
*  best performing version. The Mamba version beats the vanilla transformer, but the hybrid already
*  beats the Mamba. And again, this is the attention is all you need paper for the selective state space
*  model, right? This is the one where they're saying, hey, look, we have a new thing here
*  that is as powerful and is in fact beating the transformer on its home turf, right? On all the
*  familiar benchmarks that you know and love transformers for, the new thing is beating
*  the transformer on that stuff. And then, hey, look, if we just do the most naive recombination
*  of the two, it works a little bit better yet. Now to me, that suggests that we're going to see a lot
*  of remixing. So let's talk about sculpting memory and remixing. Sculpting memory. First and foremost,
*  this is going to be a data question, I think. More than ever before, we are going to need
*  intentionally designed training data. We are going to have to be really careful and thoughtful
*  about putting together long sequences and what we want models to learn from those sequences,
*  what we want to encourage them to retain, what we want to encourage them to let go of. And this kind
*  of work, this data creation work is a slog, but definitely can be resource intensive. It can be
*  a grind and it's not always considered super glamorous, but I think that it actually may be
*  the most important work that is going to be needed to unlock the power of the state space models and
*  the long-term memory function. Because at least from this fine tuning that we've seen, it's not
*  happening automatically, right? If you just go train it on short sequences, does it handle long
*  sequences? It seems that not by default. And that shouldn't really shock you, right? If you are
*  optimizing something and you only ever optimize for retaining information for a certain length,
*  then what happens when you give it a ton more information? It may kind of gum up the works,
*  right? When you see these models going off the rails, it's not exactly clear what's happening
*  there. Certainly there's a lot more work to be done to understand the internals of these models.
*  You might think that like the state is getting clogged up with like too much information and
*  just becoming too overloaded and not working well. Maybe it's not letting go of things as it
*  should. You can also imagine having the other problem, as I already sketched out, where maybe
*  in certain situations it has let go of things that you wish it didn't. So we're going to have to
*  create datasets with, I think, a high level of intention to really shape how we want the
*  memory to work. If we want to have needle in a haystack type behavior, we can probably incentivize
*  that quite directly, even with synthetic data, right? To create situations where there's an
*  anomaly and you need to be able to identify the anomaly much later on. That would really
*  incentivize a certain kind of information retention that is like anything that is kind
*  of contrastive or out of step with the current state is super important, must be maintained.
*  On the other side, again, you could train in such a way where if that never comes up in the training
*  data, if that diamond in the rough type thing never comes up, then it probably won't happen by
*  default, right? The state will not retain that information if it is not incentivized to retain
*  that information in the training process. And the training process largely is defined by the data
*  that it is learning from. So how do you want to shape? If you wanted to do some of this data work,
*  you could think to yourself, how do I want to shape the way that AI long-term memory is ultimately
*  going to work? What behaviors do we want it to have? What qualities do we want it to have?
*  Let's start to think about data sets that can teach those qualities and behaviors. So again,
*  I think this may prove to be the most enduring because everything else that's going to happen
*  is going to remix. But the data sets actually seem to last longer than almost anything else.
*  Certainly in MLU, the math benchmark, these are one of the few things in machine learning right
*  now that's like three years old, but continues to be state of the art relevance. I think there
*  is something similar to be done in terms of data set building for the state space architecture era.
*  By the way, a lot of that probably private when you think about long episodes and you think about
*  how much investment companies make in training their people and how long that process is,
*  how many tokens are represented in an employee onboarding and training process. It's a lot.
*  So you would expect, I think that private companies would be well positioned to create a lot of this
*  data. So that's data. The data I think is going to prove to be super important.
*  Architectures. Again, I think when people ask, is this the end of transformers or is it now like
*  Mamba or state spaces are all we need. I think that is kind of the wrong framing on the question.
*  The way I see this unlock is we used to have one mechanism that is the attention block
*  that was so powerful, so much better at almost all tasks than almost everything else that we
*  literally just used it and only it. Even knowing that, hey, we see that these layers are doing
*  different things. Going back to taking in a stimulus and working it up to higher order concepts
*  and processing it in the middle layers before then working your way back down to a tangible
*  next prediction. That's all done by the same thing. It's kind of crazy.
*  Now we have the existence proof that, okay, with a state space model, you can achieve similar,
*  even slightly better power, the transformers own home turf tests, flop for flop parity,
*  better scaling properties, faster, more throughput. Amazing. But I think the real way to think about
*  it is that we now have these two blocks, these two units, and that they each have different
*  strengths and weaknesses. And the real question is going to be, how do we combine them? And we
*  are starting to see some developments from just the last couple of weeks where this kind of thing
*  is starting to happen. So one from Together, which is the company where Tree Dow is one of the
*  co-founders and the chief scientist, we have this new model called Striped Hyena 7B. And this is a
*  combination architecture of on the one hand, the attention mechanism, and on the other hand,
*  the state space model. This is not yet from what I can tell, and I don't believe they've published a
*  full paper on this. This seems to be a more commercial release, this Striped Hyena 7B.
*  But they describe it as offering a glimpse into a world beyond transformers. It is notably not a
*  world beyond attention, but it is a hybrid structure that includes a state space model.
*  As I understand it, not yet a selective state space model, which is a traditional
*  state space structure combined with the attention mechanism. And it is a globally competitive
*  7 billion parameter model that you can already get access to through the Together AI API.
*  So that happened quickly, and we can assume that the selective state space one may soon be coming
*  as well. There is also another paper recently called Block State Transformer. And this one
*  even gets more into the weeds. It is a deeper integration of state space and attention mechanisms.
*  It is again, not yet with the selective state space model, but a global state that can get fed
*  into an attention mechanism. So in this Block State Transformer unit, they now have still the
*  self-attention of text to itself. Then they also have a cross-attention of the text to the context
*  that is evolving through time. And this is again, very competitive. I won't get into the
*  the details on this one as much, but suffice it to say, it's doing its fair share of winning.
*  And again, this is without even having the selective state space model. The selective
*  state space model was just published two weeks ago. The Block State Transformer came just a
*  little bit after that. The Striped Hyena came just a few days after that as well. They've already
*  announced that they're at least taking the architecture now up to 600 billion tokens of
*  training. Again, with the recurrence there, it seems like it's not as easy to parallelize as other
*  things, but they're going to continue to push that, I'm sure. And there's just so much room
*  for remixing that I think we're nowhere near done. We've gone from one core building block to two,
*  and we've only begun to think about how we might remix them. I think we're also going to see
*  probably a lot of evolution just of the state space model itself, right? The transformer has
*  gotten all the attention because it was working. The transformer has been optimized like crazy
*  because it is working. The state space models didn't attract that kind of attention because
*  they weren't really broadly competitive. But now that we've seen this demonstration that they can
*  be, how about moving from say a single state to a multi-state model? We see this already with
*  attention, right? There's not just one attention head, there's multi-headed attention. And I think
*  you can certainly see an analogy where multiple states might make a lot of sense. You might have
*  different states which are responsible for different things. One great unlock that the state provides
*  is it's another thing that you can make a target for an optimization process.
*  So what I mean by that is with the transformer, and as far as I can tell so far also with even
*  this most advanced selective state space model, all of the optimization is just on the language
*  prediction. We're just talking about pre-training perplexity measure. It's just how well is the
*  model able to predict the next token in whatever text it happens to be being trained on at the time.
*  But with the state space models, you also get out a state. And that state can have various properties.
*  And you might even think about optimizing multiple things. You want to optimize the
*  prediction, but you might also want to optimize some properties of a state or multiple different
*  states. One really natural way to do this would be to have some sort of contrastive objective between
*  the different states just to push them in different directions, right? We might have multiple states.
*  We might want to optimize all the states when it comes to making a good prediction, but we also
*  might want to try to create an incentive within the training regime to make the states look
*  different, a richer and more robust overall representation. Perhaps you might also have some
*  states that are dedicated to specific purposes. I think one of the really interesting things is
*  going to be to what degree do people take another conceptual elaboration here? You might imagine,
*  for example, a built-in classifier. Again, in the transformer, you have this forward pass layer by
*  layer. You get a prediction out. That's all you get out. And we can try to go into the middle layers
*  and use techniques like representation engineering or whatever to see based on the activations,
*  does this appear to have a certain concept loaded in and active or not? That's starting to work,
*  but it's definitely kind of messy. You can also have classifiers that sit outside and try to
*  filter inputs or try to filter outputs or identify when things are problematic, but you don't really
*  have classifiers built in. You try to do that with RLHF and you have a hell of a time doing it. Lots
*  of false positives, lots of false negatives. You could imagine though having multiple states within
*  a state space model where again, they're all working together perhaps to make a good prediction,
*  but maybe one of the states is specifically optimized as a classifier such that they may
*  fire off in a different way as well in a way that can be aware of the full history that can have all
*  these beneficial long-term memory properties of the state space models. But because the state is
*  also something that you can optimize, you might be able to turn different states into effective
*  classifiers. So maybe you're getting both an output in terms of the next token, but also getting
*  classifier values out at the same time as well. Very interesting potential I think for things
*  like that. You may also see different kind of wearings. Maybe you feel like this long-term
*  memory is great, but I can't necessarily fully trust it. Maybe I need to look at the current
*  state, but also some historical states. I can't say every state because keeping in mind the only
*  reason this is scalable in the first place is that the traffic from the high bandwidth memory
*  to the SRAM that is closest to the cores has been designed in such a way that the traffic there is
*  minimized. We can't just take every internal state and remove it and save it, but we could do some.
*  We could accept some performance hit to have some historical states. And maybe we would find that
*  if we have my last state, but also some selection of historical states to work from as the current
*  input, perhaps that could work even better. There could be hierarchies of states. There could be
*  mixtures of experts built into this kind of architecture as well. There is a whole host of
*  opportunity for innovation and elaboration, I think, in this new architecture, just in the same way
*  that there was with transformers. But again, even more so because now we have two fundamental
*  building blocks that seem to work comparably well and have these different strengths and weaknesses.
*  What other kind of things might we see? New wiring diagrams, new ways to branch,
*  perhaps some way to recover the parallel form for training, perhaps through an approximation.
*  It does seem like fundamentally this selective mechanism is by definition recurrent. But if we
*  were to accept some imprecision, could we create a convolutional version that would be close enough
*  to load in a bunch of context to get something off the ground fast or to facilitate training?
*  I would not be surprised if something like that is possible. We might see regularization
*  techniques that are really interesting with memory. Just thinking about the human cognitive
*  experience, we can remember what we had for breakfast this morning. Many of us, most of the time,
*  we can remember maybe the best breakfast we've ever had. And we can remember what we normally
*  have for breakfast. But we certainly can't remember every breakfast we've ever had. So there's some
*  sort of abstraction happening, some sort of compression happening where things that are not
*  outliers that fit patterns, we get rid of the details of those individual episodes of our memory,
*  and we compress them into the general memory of what I typically eat for breakfast as opposed to
*  a bunch of super specific individual breakfasts. So I think you're probably likely to see some sort
*  of weight decay. You might call it state decay. Weight decay, you basically say by default
*  throughout the training process, all the weights are going to get lower. They're going to get
*  smaller every step. And then the only way that they're not going to get smaller is if they
*  specifically get turned up through optimization. This has been shown to be pretty key to the
*  grokking phenomenon where the generalization that happens seems to depend on the fact that
*  the model's first solution, which is just to memorize, gets gradually weaker due to the weight
*  decay. But the actual algorithm that solves the problem continually gets turned up and
*  overcomes weight decay. And when that gets turned up enough that it is the dominant mode, then you
*  have the grokking. Some version of this also certainly happening in the human memory where
*  clearly a lot of details are pruned from our memories. There's work there to be done. But my
*  term there is state decay from weight decay to state decay. Not to say we won't have weight decay
*  as well in these state space models, but state decay is something that has just been there for
*  a while that doesn't appear to be useful. Can we just gradually let go of that stuff and maybe have
*  multiple states so that they do it in different ways where some try to retain and others try to
*  let go so that we have a robust multi-state representation that maybe can do a little bit
*  more than any individual state with a single training objective could do on its own. Finally,
*  before moving on from the architecture bit, here's a quote from the Together AI blog post
*  about the Stripe-Taina model. They say, early in our scaling experiments, we noticed a consistent
*  trend. Given a compute budget, architectures built out of mixtures of different key layers
*  always outperform homogenous architectures. This was a conclusion that I came to in my own reading
*  and just thinking about this. Then eventually I came across this quote. I don't want you to think
*  that I'm taking too much from this one quote. On the contrary, I thought it was a perfect
*  representation of what I had inferred was likely to be the case. We're headed for a future here
*  where we're not going to see the same attention block as every single layer. We're also not going
*  to see that the selective state space block is the only thing that matters. Instead, we're going to
*  see that these architectures built out of mixtures of different key layers are going to be the way,
*  and that they'll probably blend together. That's what the block state transformer is all about as
*  well. What else can we begin to expect if all this analysis is right? On the hardware dimension,
*  the state itself is another dimension for scaling. We have the parameters. That's been the main way
*  that we've talked about models and their scale. We also have the context window, which we've been
*  scaling in the transformer. Here we have something new. We have this state, which is itself of finite
*  size. It is where the information from the current episode, from the current context,
*  has been compressed. How big that state can be is a pretty important question. You are fundamentally
*  limited by the size of the state, how much information you can actually bring forward.
*  I think this doesn't seem to be explored at all in this current paper, but how big the state is
*  is definitely something that you will want to push. I would expect that just like we saw a rush for
*  bigger parameter counts and longer context windows, bigger states is something that is going to
*  ultimately get scaled. Is the current hardware optimized for that?
*  Probably not. If you just consider the fact that the algorithm here was developed in a hardware
*  aware way, that sort of implies that the hardware was not designed for this algorithm. Well, we've
*  certainly seen hardware designed for transformers. It will certainly take a while if we are going to
*  see hardware designed for states based models, but I wouldn't be shocked to see something like
*  that happen. I'm not exactly sure what that would look like, but perhaps it would look like a
*  different ratio between the SRAM or the shared memory and the high bandwidth memory. Right now,
*  from what I've seen over the last couple of generations, V100, A100, H100, those memory
*  sizes are roughly growing at the same pace. Whatever has determined that ratio, the ratio
*  hasn't really changed over the last couple of generations. If I'm right about all this, we may
*  see higher ratios of shared memory to high bandwidth memory, because maybe the models
*  don't necessarily need to get all that much bigger, but the states need to get bigger.
*  And so the hardware may have to adjust to allow for that. Beyond that, how much more can we get
*  out of SRAM and into some longer term storage? It's kind of crazy, right? The state is the
*  important thing here, or at least it's the big new innovation that gives us this possibility of
*  longer term memory, more coherent in all likelihood, more agentic sort of behavior. And yet the state
*  itself doesn't exist anywhere except in this very small amount of the high speed memory. And by
*  default, it's not exported from that. So it's not saved anywhere. So all the states by default are
*  lost. If we were to try to get all the states, literally every timestamp, off of the SRAM,
*  then it would probably be prohibitively slow. But how much more might we be able to sneak off
*  the SRAM? Or could a different chip have a somewhat different design where information could flow out
*  of the SRAM into some sort of storage without clogging the critical input channel? I don't know,
*  but it does seem like a question is going to be what more can we get out of SRAM and at what
*  performance cost? And eventually, is there any hardware modification that could ease that?
*  Because I do think we're going to want to look at historical states, for sure. And just to get one
*  historical state off, that shouldn't be too big of a problem. But to get like lots to get every 10
*  states or every 100 states or every thousand, that's going to be a lot more, especially if
*  you're talking millions of steps in an inference. If you wanted every thousand, you're looking at
*  a thousand states. How much does that slow things down? I don't know today, but I think that's
*  another area where there's going to be some interesting scaling laws and analysis on current
*  hardware. How much can we save out of these internal states without tanking performance?
*  They really do think that's likely to matter. Then you might think about application development.
*  So let's imagine these things start to realize the potential that I'm talking about. And we start to
*  have models that whatever exactly their internal wiring, they have this long-term memory, that they
*  start to have something that the transformers lack, that they have the ability to evolve
*  meaningfully over time. That they can, because they have this longer-term coherence, that they
*  can start to be more predictable in their behavior, fundamentally less stochastic,
*  fundamentally more shaped by all interactions that they've had. Something that can evolve with you,
*  something that can really, in a much deeper, longer-term holistic way, actually start to get
*  to know you. And again, all that's going to take a lot of work. The data part, I think in particular,
*  we have to go create the data that incentivizes that. And that doesn't really exist much today.
*  I would not be surprised if we start to see it come online relatively quickly, but it doesn't
*  exist yet today. So we are going to have to go and create that. But as that starts to come online,
*  then what sort of things are going to be possible in terms of applications?
*  I think one thing is we'll see a shift probably from context management to something that you
*  might call context selection. Or another way to say that is maybe you go from
*  RAG to something more like state search. So what do I mean by that? It's like really long contexts.
*  You aren't going to want to have to recompute every time. If you're looking at reading a whole
*  body of literature in order to load up the latest and greatest knowledge into the context. Or if
*  you're talking about reading somebody's whole email history to really get a sense for who they are,
*  you're not going to want to have to redo that for every single inference. It's not going to
*  be practical. So we're going to have some states which get arrived at, exported off the SRAM at
*  whatever performance cost. Again, it'll definitely be acceptable to do this from time to time to
*  cache a state, which is how many you can do will be interesting to find out. But you can definitely
*  do one here or there. So if you want to run through a million or millions of tokens and build up this
*  state that has evolved through that entire history, you definitely will be able to take that
*  state and save it. And then you might have a lot of those running around. So instead of having to
*  be very careful about what specific text do I put into context. Maybe the idea is more that we have
*  a big library of pre-computed contexts, which we can then select from. Today, I'll often give a few
*  shot examples, but maybe in the future, I can go to a library of existing contexts that have done
*  hundreds or thousands or a million of those problems, right? Or read the whole textbook
*  and then did a thousand problems that are now ready to solve my particular problem. It seems like
*  that is going to be a potentially big, big deal. And again, going through a database and retrieving
*  some text and putting that into the prompt, that feels kind of clunky by comparison to saying,
*  do I have any states that have what I need? This also suggests, why would you want multi-state
*  architectures? Well, maybe you want one state that's kind of your core state, but then you want
*  auxiliary states that have information. Again, we sort of work this way, right? We have, I'm Nathan,
*  I'm me, I'm like going through my day, I know what's going on. And then I like get into a mode
*  where I have all this working knowledge that it's really the front and center in my mind. And then
*  I might go switch to a totally different context and go play with my kids. And I have kind of a
*  different, seemingly quite disjoint set of mental states that are associated with those two things.
*  But in some sense, I'm still me, right? I'm not suggesting that I work like these states-based
*  models work or that they are going to work like I work, but I just see that behaviorally, I have
*  this kind of flexibility and I can imagine an architecture now with, again, perhaps a core
*  state or a couple of core states and then like swappable states. Another way that I've been
*  saying this is from mixture of experts to mixture of states. Can we take these
*  states and combine them, recombine them in interesting ways? Almost for sure. It seems
*  like that's almost for sure possible, right? We see that in representation engineering, even within
*  the transformer mid-layer activations, it seems almost for sure that you would be able to take
*  states and combine them perhaps with weird unexpected consequences in some instances,
*  but like functionally almost for sure that should work. There's also like disposable paths
*  or self-delegation could potentially get a lot more interesting. I was trying to use an agent
*  platform the other day and the agents still don't quite work. So I'm trying to use this agent
*  platform to do something. It involves like searching through my email. My email has a
*  ton of stuff in it. The search returned a ton of things and then it kind of broke. Like it was too
*  much. Couldn't page through it effectively or whatever. And I was looking at it and I was like,
*  I can see why this is a pretty big challenge because even if you're using GPT-4,
*  turbo or quad 2.1 and you've got north of a hundred thousand tokens, like an email search
*  out of my email, I need to delete more stuff. But man, a lot of people have a lot of email,
*  right? We have gigabytes of email. So the search results go pretty deep and then you need to scan
*  through them and figure out what's relevant and you can self-delegate that. But the transformers
*  just don't handle it super well. Whereas you might imagine a state space model scanning through
*  these long search results much more effectively. And this is actually an area where you could also
*  imagine the state space model parallelizing really well. You might say, okay, I've come as
*  far as I've come. I'm at this state and now it is the time to search through the email.
*  Well, maybe I can just take 20 of myself and divide that work 20 different ways and each go
*  through a page. And for each email, I'll be asking, does this seem relevant? And if so,
*  I'll indicate as much. And then that way I can really quickly scan through all the stuff with
*  a ton of context to determine what's relevant and not relevant. Then once I find all the stuff that's
*  relevant, then I pop up a level in my recursion depth and now I can just discard all those
*  versions of me. And me here is the selective state hybrid architecture of the future.
*  We can just discard all those versions that actually ran through all the
*  annoying irrelevant email results. And we can just pop up and say, okay, here's all the relevant
*  stuff. Maybe you have some notation that we performed a search or whatever, but you don't
*  need all that. You don't need to recall. You don't need to clog up your context. You don't need to
*  clog up your state with all the random emails that were not relevant. So instead you just
*  run that process, discard, and then pick up back where you left off with all the stuff that actually
*  is relevant. I think we are likely to see far, far more agentic behavior and far more robustness,
*  far more apparent sense of direction or purpose or kind of unity toward goals based on the fact
*  that we can build up these really long contexts. You might even think of things like developing
*  sort of a immune system, a runtime immune system as a state, right? This gets a little bit beyond
*  what we typically think of as the cognitive, but the human immune system has memory. It knows what
*  it has seen in the past. Sometimes these memories fade. Other times they last a lifetime. Obviously,
*  it's all super complicated, but the human immune system is in a very fundamental way built on a
*  memory system. So what would the equivalent of that be in one of these state space models?
*  What if it was just a log of all the attacks that are known, right? We maybe can't train into the
*  core weights that there's all these attacks. Who knows what the training mix is going to look like?
*  Fine tuning in general has not proven, at least for transformers, to be a great way to teach facts.
*  So new kinds of attacks, new things to watch out for, those are tough, right? OpenAI has their
*  system prompt and a lot of debate that happens around when they get embarrassed by some failure
*  of chat GPT and then later people report it being fixed. People accuse OpenAI of changing the system
*  prompt. At this point, it's pretty well established that they're not changing the model that frequently,
*  but they can change the system prompt. And so maybe they can just go in there and be like,
*  hey, watch out for this and have it watch out for that. And hopefully the storm will blow over and
*  we can include it in the next data set, but we can at least patch the behavior and stop the
*  embarrassment for the moment. I don't know how much they do have that. I suspect not all that much
*  because clogging up your system prompt with that kind of crap just doesn't seem like the kind of
*  trade-off that they would want to make unless it's a pretty serious vulnerability. The fact that my
*  spearfishing thing like always worked, they could have easily said like, do not spearfish
*  in the system prompt. And that probably would have stopped it from working or at least would
*  have helped quite a bit. So I don't think they're doing a ton of that, but with the
*  state space paradigm, you can imagine doing a lot of it. You can imagine a dedicated state within a
*  multi-state model. You can imagine keeping much more up to date on recent reports. These are the
*  things that you really need to be watching out for now. And potentially those things could be
*  passed around in a far more lightweight and rapid way. And if it is a dedicated state within a
*  multi-state model, you potentially could get significant robustness out of that. I mean,
*  that's how we do it, right? The old shame on you for fooling me once, but shame on me if you fooled
*  me twice. That's because I have memory, right? I'm supposed to remember it and I'm supposed to
*  recognize it and I'm supposed to know better the next time. And the transformer just doesn't have
*  that mechanism, but the state space models definitely do. And the question is, can we
*  shape it and can we get the performance to where we need it to be, to where we can really trust it?
*  I strongly suspect we can. I strongly suspect we are going to see much more agentic, much more
*  goal-directed, much more consistent, much more predictable behavior, much less weird going off
*  the rails, less apparent stochastic randomness. And I think all of that is probably going to be
*  unlocked with mostly data sets. If I had to guess, I would say it's like two-thirds data sets
*  and one-third architectures. You're going to have to have the data sets to train into
*  various architectures and the architectures will co-evolve. If you're thinking about data sets
*  and you want to build one, by the way, I would really emphasize this would be true at any company
*  as well. I've said before many times, AIs can handle tasks really well, but jobs are too big for them.
*  If this changes that, then the way it's probably going to happen is that people are really going
*  to start to record jobs. Instead of just having these more manageable bite-sized units of tasks,
*  we're going to have to start thinking about data sets and super long episodes as ways to record
*  jobs. And I think it's also going to be really important to the degree that we want to automate
*  whole jobs and we want to do that in kind of a robust way. It's going to be important to
*  make reasoning explicit and to really capture reasoning. This is important already on
*  Transformers. I've covered a few different times how, when I tried to fine-tune GPT 3.5
*  for the way Mark script writing task, it didn't really work. At first, it didn't seem better,
*  even a little worse. And then when we started using reasoning steps in the data set to make
*  clear, this is how we want you to think about it. This first go through the reasoning, the strategy,
*  and then write the script teaching it. This is how we want you to approach it. And we want you to
*  spell it out and then do it dramatically improves performance. I think that there is this kind of
*  analogous reasoning or identity or narrative level that people have that seem to guide our
*  actions over time and make us legible and predictable to one another and help us stay on task
*  that probably gets built in here too. It's not just about this is the task. This is how I break
*  down. This is how I approach it. But if you were really thinking, how can I get an AI to do a job?
*  One of the things I think is missing that you don't really find this on the internet, right?
*  It's the higher level narrative of who am I? What is my job? What are my goals? What am I doing right
*  now? And that's in pursuit of that, right? That's all always somewhat in mind. And then it can fade
*  a little bit as you're really getting into the task, but you'll select your task. You decide what
*  to do based on this stuff, right? And you decide when it's worth pushing through difficulty versus
*  when it's worth giving up and going and doing something else. Instead, these decisions are
*  guided by this high level narrative. And we don't really have that in the training data. It's not
*  on the web. So I think we're really going to have to work hard to capture it. And it probably just
*  starts off by like having people monologue more and just force people to take the moment to really
*  spell out who are you? What is your job? What are you doing? And to weave that in to all the activity
*  I think that is likely to be a big part of how we can get the AIs to imitate human behavior.
*  And again, that data doesn't really exist yet. Certainly not at the scale that it's going to need
*  to exist if we're really going to see the sort of performance that I'm expecting from all this new
*  technology. Okay. What about interpretability and safety? This is a really interesting topic.
*  And I've seen different takes on it. One simple take, which I think definitely has something to
*  be said for it is maybe this is a huge win for safety work and mechanistic interpretability work
*  because the state itself is such an obvious thing to focus on. It's like, wow, with the transformer,
*  we have all these internal activations and circuits, but what's happening? It's also alien
*  here because we have this state that is the long-lived state and you kind of compare the
*  last state to the current state and to the next state. It does seem like that is a very natural
*  object of study. And to look at what concepts are activated, to look at concepts like intent,
*  is there deceptive intent? Is there helpful intent? Is there harmful intent? It would seem that you
*  can really zero in on this particular thing and study it super intensively. Techniques like
*  representation engineering that we have mentioned a couple of times are seemingly likely to be pretty
*  adaptable to this circuit type approaches, perhaps as well. You have a ton of weights still,
*  right? Like you still have billions of parameters that are involved in this information processing.
*  So studying the circuits that develop within those, that's definitely also a thing.
*  But the existence of the state as something to focus on does seem like it could be a huge
*  advantage for interpretability and safety. At the same time, at least as it's currently set up,
*  the fact that the states are never actually taken off the SRAM at all and you don't have access to
*  them and that's somewhat necessary for performance reasons does suggest that you can study these
*  states. But if you actually want to monitor states at runtime, right now we don't have a great way
*  to do that. If you're tinkering and you're studying, you're doing interpretability work,
*  then yes, you have a natural place to focus your energy. But there's not a practical way to say,
*  in fact, it would kind of violate the whole premise of the hardware aware algorithm to say,
*  I want to export every state so I can study it later. You maybe could fit in some sort of checks
*  that could happen purely on the SRAM and that could be another output. But definitely some
*  innovation would have to happen there to have a state of the art state monitoring applied at
*  runtime without a major performance hit. Again, maybe we see hardware changes there where there's
*  more SRAM and it makes it easier to do, but very hard to say right now. Just behaviorally,
*  I would guess there will be as many surprises and weirdnesses with these as there are with
*  transformers. Maybe with the hybrid mechanisms, you start to get somewhat less behavioral
*  weirdness because they hopefully get the best of the strengths and the weaknesses are compensated
*  for. But if I were just thinking pure state space models, I would expect a lot of weirdness.
*  And even with the hybrids, it certainly should be open-minded to behavioral weirdness. And so
*  I do think we're set back a bit in terms of just understanding AIs generally. What can they do?
*  What can't they do? What do they trip over? We have answered that to a decent degree
*  for transformers, but we have not even really begun to answer it for state space models.
*  We can only begin to answer it now. Zooming out, bigger picture still yet, considering
*  philosophical questions and questions of human AI interaction dynamics. I think if everything I
*  said about the agent capabilities is true, if because of these long context, we can start to
*  see more coherent, consistent, predictable, legible behavior. If these things can evolve over time and
*  get to know us in some sort of more intuitive, deeper way, then I think we're going to have a
*  totally different relationship with them. It's going to be much easier to project value onto them.
*  We already see this happening, of course, go back to our second episode with replica,
*  people falling in love with like pretty primitive chatbots. Now we are seeing character AI, people
*  are spending hours today, all sorts of new sex bot chat app type things are coming at us.
*  All of these things still don't have long-term memory. We still don't have a mutual evolution
*  with them. This could really change that. And if it does, we are going to be much more inclined
*  to see these things as real value. And the loss of a state with all the context that it represents
*  could be like a real loss. You may not even be able to recreate it. Because again, that log is not
*  there by default, or you could log every input, but by default, most people are not going to be
*  logging every input and intermediate states are lost. So losing a prized state or a valued state,
*  that could be a real loss. Not the kind of thing that's easy to get back. Not like with
*  transforming, just reprompt or whatever. It might not be like that anymore. These things might have
*  more durability and they might even merit more moral weight. Right? I don't really know why I'm
*  conscious. I certainly don't claim to have the mystery of consciousness solved, but I hope to
*  do an episode on this. One paradigm for understanding consciousness relates to
*  just the fact that we can have this kind of long time horizon awareness. And that to some extent,
*  that that comes about by us modeling ourselves. We definitely have an ability to predict
*  how we're going to feel in the future. We may be right or wrong, but we do have a kind of running
*  prediction that helps us when things are changing from our expectation. We realize that in part
*  because we do have this, at least a little bit ahead planning for what am I likely to be
*  experiencing next. When that expectation is violated, it definitely brings things to
*  our attention. You can definitely imagine these state space models, self modeling, right? What
*  if you had a dedicated state whose job it is to model what the likely state is going to be
*  50 states from now? That's a bit of a trick to pull off, but it does seem like there's nothing
*  fundamentally blocking that. And that's getting close to at least one definition
*  of consciousness. Will there be subjective experience? I have no idea, but it's much
*  easier for me to imagine caring about an AI that is powered by a state space model with a long
*  running super high context state. And to be right about caring about it as compared to caring about
*  a character that's coming out of a transformer model today. I'm radically agnostic about these
*  things, but certainly it seems like this is a significant step in that direction.
*  If you've ever heard of the age of M by Robin Hansen, I would say a classic that is more classic
*  now as a result of this, he postulates a AI that essentially simulates a human brain or emulates a
*  human brain. And so he calls them M's and they're supposed to be very human like, because they're
*  to a high enough degree of precision, emulating what a human brain would do.
*  But they have all these different properties because they are digital. They can be paused
*  and put into long-term storage and then woken up. And when they're woken up, time has passed, but
*  their state isn't changed because we have this durable digital storage. And so he envisions
*  a world where that plays out. And these things are easy to clone, right? You can spin up a bunch.
*  I alluded to that in terms of application design and in terms of self-delegation to go scan through
*  a ton of emails. A lot of the analysis in the age of M is way more apt in a future where long
*  running states are a key component of what AIs are. We're not headed immediately for real high
*  fidelity emulations, but we may be headed for enough of the core capabilities such that a lot
*  of that analysis is going to, I think, start to become more and more relevant. You look at the
*  transformer and you look at the M's and you're like, ah, these are just so different that I don't
*  really think the analysis of the M's and how that's likely to play out in terms of economics, society,
*  whatever. I don't think that follows from transformers, but much more so. It seems like it could follow
*  from the state space architectures. So hopefully maybe we can get Robin on to go through that
*  because I think it's only looking more and more relevant. Now, zooming out again a little bit
*  further, just kind of talking big picture. If you are looking for investments to make, if you are
*  looking for companies to watch, I would definitely look at both of the companies that the two authors
*  of the Mamba paper are affiliated with. That's Albert Gu. He's the chief scientist at Cartesia
*  and Tree Dow. He's the chief scientist at Together AI. Cartesia specifically says that they are
*  training models with sub-quadratic scaling properties. And this certainly fits that bill.
*  Together AI seems to be even more focused on just as you'd expect from Tree Dow's hardware aware,
*  super close to the metal programming. They seem to focus on infrastructure, managing compute,
*  getting the most out of compute, et cetera, et cetera. Given that both of these guys are involved
*  with startups, it is a little curious that they published this research. We are in a moment of
*  general closing and I would be fascinated to talk to them about why they chose to publish this work.
*  I think this is the kind of thing you could keep secret, especially given how it's not just a high
*  level conceptual thing, but it's also the low level implementation details that are so important to
*  making the thing work. That's the kind of thing you can keep secret. You can keep CUDA code in a
*  highly specific implementation. That you could keep secret. So they chose not to. It's out there.
*  They may, maybe they even have more secrets that haven't been shared with the public, but this is a
*  pretty big paper and the code base that I am kind of surprised is published in today's day and age.
*  Just as a thought experiment, if they had taken it to Microsoft and tried to sell it, I would
*  expect that they would have been able to get a lot of money for it, but they didn't. So it's out there.
*  Unless I'm way wrong about what this can enable, that definitely just means acceleration will
*  continue. Open AI is well known for pouncing on stuff like this. When I've shopped this idea around
*  to different people and said, what do you think? Why might this not be as transformative as it
*  seems like it would be to me? And one of the interesting speculations I got back was, well,
*  maybe the leading labs already have something like this. And so therefore it's baked in already to
*  the very best stuff that we're seeing. Maybe GPT-4 has an element of this. I don't think that's true.
*  Certainly the way that they are presented seems to be like you have a context window. You can't go
*  past it. So I don't see anything to suggest yet that there is something like this. The leaders
*  like Open AI. They didn't invent the transformer either. Obviously what they have done is they have
*  pounced on the advances. They have really tried to push the performance and maximize it. They've
*  really tried to figure out what is this good for. They are obviously highly invested in data creation
*  and collection of all sorts. They're doing licensing deals now with all sorts of different
*  data providers. I would guess that they already have somebody internally, maybe even a team
*  working on characterizing this. I would guess Anthropic is probably already doing the same.
*  If it is working, they will make it work. And interestingly with Open AI in particular,
*  their new assistance API would be dramatically improved with an architecture like this.
*  The assistance API, which is basically the GPT's API version, allows you to have arbitrary length
*  threads and also documents, you know, rag style knowledge base that's attached.
*  But this arbitrary length thread, you think, well, how do you have an arbitrary length thread if you
*  have a finite attention window? The answer that we've got so far is that the assistant
*  basically queries its own history as part of your subsequent call and fetches history that's
*  relevant and loads that into context. And then you are charged for, and this has not been totally
*  clarified yet, you are charged for the new inputs and outputs, but also whatever was
*  fetched out of history. That's a little bit messy. It doesn't sound that awesome.
*  It would be totally smooth with an architecture like this, right? You have now an arbitrary length.
*  You have that history. Yeah, you can query it perhaps if you need to, but you have this state
*  that is propagating through time. And this would also lend itself to, again, if used in pure form,
*  and I don't think it's going to be pure form. I think there's going to be hybrid with attention,
*  but if used in kind of pure form, then you could also imagine, hey, you only get billed for the
*  additional inputs and outputs at any given extension of the thread. That could be a huge deal.
*  So I think OpenAI is advantaged by this, probably relative to other things, which is again why it is
*  kind of confusing as to why it was published. Their ability to pounce on things, to drive scale,
*  to really get relentless on the question of what is going to make this product work well,
*  is going to be a huge advantage here because this is something that is just new and totally
*  uncharacterized. And I do think their assistance API, if there was anything that, broadly, I think
*  they don't have this in their production stack yet, but they might have something like it in the
*  pipeline. And if I decide one piece of evidence that would make me think, yeah, maybe they do,
*  it would be the nature, just the structure of the assistance API. The assistance API looks like
*  something that was built a little bit more with this kind of architecture in mind, honestly,
*  than with the transformer. Maybe you could think of it as like a bridge from a pure transformer
*  structure to a future structure that they anticipate. Time will tell. Agents, we're behind.
*  I've been thinking a little bit about coming to the end of the year. What have I been right on?
*  What have I been wrong on? I definitely expected more progress on the agents than we've got.
*  One of the big reasons I think that we haven't got as much as I expected is that GPT-4V has only
*  recently come available. It was demoed in March. We had expected to see at that time that it would
*  be launched soon and that multimodal inputs would quickly become the norm. And I definitely think
*  that vision is super important for effectively navigating even just the digital world, right?
*  Even just doing stuff in a browser. The browser is meant to be interpreted visually
*  and only recently has that really become possible. So now we have the application development agent
*  work to be done on top of that. I think there is a big unlock there. And I think we're going to get to
*  effective agents regardless, even if we do have to brute force it through purely transformers
*  between the vision, between doing things like rewarding reasoning. I had a result earlier this
*  year where they achieved a state of the art on the math benchmark by giving a reward signal at
*  every intermediate step of reasoning as opposed to just the final result. I think that is going to
*  work for agents. If I had to guess what GPT-4.5 would look like, if you interpret the TikTok of
*  the last generation, if GPT-3 was a certain scale, a certain kind of latent power, and then 3.5 was
*  when they really applied the RLHF and made it behave, then GPT-4 is another bigger level of
*  power. But it was released before this paper came about the rewarding intermediate reasoning.
*  And so maybe GPT-4.5 is still the same raw power, but just like way more reliable reasoning. That's
*  kind of what I expect from GPT-4.5. Context windows continue to go up as well. We've also got
*  new scaffolding. Obviously we've got RAG. We've also got skilled libraries.
*  There's a lot of reasons to think that agents will work, but this seems like a qualitatively
*  different reason to think that agents will work. That with the long-term memory, with the big enough
*  states, with perhaps multiple states, it seems like there is a path to a level of coherence,
*  robustness, legibility, predictability that will make these agents both far more effective
*  and also just far more familiar in the way that they proceed. And finally,
*  I think all of this does suggest that things are getting a bit out of control. You've heard me say
*  that, that things are perhaps out of control many times. I would like to emphasize that I think
*  right now we are hitting a moment where there may be a qualitative shift in just how out of control
*  things are getting. A totally different line of research, but just again in the last week or two,
*  DeepMind put out a paper in Nature about a technique called FunSearch, searching the
*  function space where they used a frozen language model. That means again, the language model weights
*  are not changing. They're not even fine tuning it, but nevertheless they were able to use it
*  to advance the state of the art in a number of problems, including a couple of mathematical
*  problems that have been open for decades. You know, this is pretty remarkable the way that they do it.
*  They have to have things where the solution is scorable. This relates to the PNP problem division
*  where certain kinds of problems are very hard to find the answer to, but are very easy to
*  verify the answer to. A classic example of that would be factoring the product of two large prime
*  numbers. I give you some giant number and even if I tell you like, hey, this is the product of two
*  large primes, you're going to be at it for a while before you can figure out what those primes are.
*  Cryptography is largely based on the extreme challenge of this problem. However, if you have
*  the private key, if you have one of the prime numbers that was used, then you can just do the
*  division and there it is. So it's very time consuming to find the answer, but it's very easy
*  to verify the answer. This DeepMind paper is for problems like that. This almost bears its own
*  episode, but the way that they do it is they use the language model. They generate ideas. They give
*  it like its best recent attempts, you know, functions that have scored the highest and say,
*  here's a function. Here's how it's scored. Here's another function. Here's how it's scored.
*  Your job is to come up with a new function that will score even better. And it took a lot of
*  generations, but not that many. I think they reported a million generations in this paper,
*  but a million generations, we're talking low tens of thousands of dollars at retail API price
*  with GPT-4 pricing to run a million generations. So not that much. And with a little bit of
*  additional clever structure to make sure that they were trying novel strategies and whatever,
*  and the fact that they could quickly score the results, they're able to advance the state of the
*  art on multiple open math problems that again, have people been working on and have been open for
*  decades. That paradigm seems to extend extremely naturally to exploring the architectural space
*  in machine learning. And particularly now that we have not one, but two different fundamental blocks
*  that are like equally expressive and have these likely quite complimentary strengths and weaknesses
*  where the attention is really good at dense analysis and every token relates to every token.
*  And we can see everything that's under consideration clearly in one view versus the
*  state space where you have this long-term memory and the ability to learn from lots of examples,
*  but also have to let go of certain information over time. This architectural space is
*  barely explored at all. And AI could probably do it. GPT-4.5 even, even four, right? I mean,
*  this was Cody that they used, which was a Palm two generation fine tuning on this deep mind paper.
*  So that's not even as good as GPT-4, but you take GPT-4, you apply a similar structure. You say,
*  here are the two blocks that you can really play with that are like your fundamental units.
*  You can reorder them. You can remix them. You can have different sizes at different layers. You can
*  have different interleaving patterns. You can have different kinds of skip connections. You
*  can potentially even define new ways that kind of bleed the blocks together. And each time you do
*  that, we will actually do some training. We'll actually instantiate that model. We'll run it
*  through some training and we'll compare it to other models that were trained on exactly the same
*  initial data. That can be pretty fast. In previous episodes, we've done analysis of like,
*  how big does your cluster have to be to train GPT-4 and how many days or whatever? Well,
*  the biggest model, the 3 billion parameter model is still like five orders of magnitude less compute
*  than GPT-4. And you don't even need that. Maybe you can get by with one millionth. Maybe you can
*  even do seven orders of magnitude less. If you see something that, hey, in early training,
*  it's beating things that are currently our best, then those are the things that you want to look at.
*  Right. So to take a language model and have it do a million different versions. Now the score
*  is not so easy to calculate for each of those million. If each test takes one millionth of
*  GPT-4 compute to evaluate, then when you do a million, then you've basically consumed all
*  of GPT-4 compute. So this would be a big undertaking still for a significant lab with significant
*  compute resources. But might you expect that GPT-4 with a million attempts could beat the state of
*  the art? I would bet it could. And what about the possibility also that as the state of the art
*  improves, it's not GPT-4 doing it, but it is in fact some state space attention hybrid doing it.
*  I'm assuming that one of the biggest challenges in the DeepMind paper is that, hey, we need to avoid
*  the same generations over and over again. Right. If you have the language model do the same task a
*  million times, you're going to have to take care to get it to vary what it's doing. But if it has a
*  long-term memory of its own, then perhaps it can be incentivized to explore different kinds of spaces
*  within the architectural space without having to be tortured so much into doing it. And again,
*  you need the training data to create that kind of behavior if that's indeed the kind of behavior
*  that you want to create. But it certainly seems far more possible than it ever has before that
*  highly agentic, highly goal-oriented, highly on task, well, the specialized agents might soon be
*  doing the machine learning architecture R&D, or at least a significant share of it
*  for us in an automated way. And if that is beginning to happen, then we're really starting
*  to close some fundamental feedback loops that begin to look like some sort of takeoff, some sort
*  of intelligence explosion. So with the big caveat that maybe I have this all wrong, maybe it's just
*  not going to work. Maybe it just won't scale past the 300 billion. I don't know why that would be.
*  The scaling laws so far have been pretty predictive, but yeah, maybe I have it wrong.
*  Maybe it just won't work. But if I'm right, I think we are looking at not the end of transformers,
*  but the end of the transformers era, the end of the time when the same exact block repeated over
*  and over again would give you the very best performance. And instead, we would be heading
*  into the beginning of a new multi-architecture era where we will likely have even faster recombining
*  of these elements to create ever better and also ever more specialized architectures,
*  where we will have proliferation and evolution so quick that it's going to become increasingly hard
*  to analyze and make sense of. This is already pretty hard. I spent the last two weeks trying
*  to understand this from every angle and try to figure out what's going on. There's a lot more
*  to come. I think it's going to be very hard to keep up with this stuff, particularly if we start
*  to see the loop close where the models can do the exploration of architectural space to build
*  even better models. I think we're going to see all that and more effective agents, more compelling
*  long-term assistance, more compelling long-term AI friends and companions. All of this, if I had
*  to guess, I would say it probably happens several times as fast as the transformer era has already
*  unfolded. From 2017 here to late 2023, a six-year period of transformers invented to today.
*  I would say this new architecture gets validated, assuming it does, and gets elaborated
*  in a similar way in probably a third or maybe a quarter of the time, in part because
*  so many more people have piled into the space because the hardware has ramped up, because the
*  data sets are there, because the benchmarks are there, because the models are increasingly able
*  to help all of these factors feeding into the same dynamic. The cycle is turning tighter and tighter.
*  If you thought that the cognitive revolution was
*  going to give you any rest, I am sad to say that I don't think that is the case.
*  If anything, it just seems like the intensity is turning up and up and up.
*  The cycle time is getting shorter and shorter.
*  And all I can say is buckle up.
*  It is both energizing and enlightening to hear why people listen and learn what they value about
*  the show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM
*  me on the social media platform of your choice. Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omnike so much that I invested in it
*  and I recommend you use it too. Use Cogrev to get a 10% discount.
