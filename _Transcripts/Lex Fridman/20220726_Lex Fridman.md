---
Date Generated: April 10, 2024
Transcription Model: whisper medium 20231117
Length: 7808s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'coding', 'deep learning', 'deepmind', 'gato', 'google', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'oriol vinyals', 'programming', 'robots', 'sentient', 'singularity']
Video Views: 246579
Video Rating: None
---

# Oriol Vinyals: Deep Learning and Artificial General Intelligence | Lex Fridman Podcast #306
**Lex Fridman:** [July 26, 2022](https://www.youtube.com/watch?v=aGBLRlLe7X8)
*  at which point is the neural network a being versus a tool?
*  The following is a conversation with Oriol Vinales, his second time in the podcast. Oriol is the
*  research director and deep learning lead at DeepMind and one of the most brilliant thinkers and
*  researchers in the history of artificial intelligence. This is the Lex Friedman podcast. To support it,
*  please check out our sponsors in the description. And now to your friends, here's Oriol Vinales.
*  You are one of the most brilliant researchers in the history of AI, working across all kinds
*  of modalities. Probably the one common theme is it's always sequences of data. So we're talking
*  about languages, images, even biology and games as we talked about last time. So you're a good
*  person to ask this. In your lifetime, will we be able to build an AI system that's able to replace
*  me as the interviewer in this conversation in terms of ability to ask questions that are compelling
*  to somebody listening? And then further question is, are we close? Will we be able to build a
*  system that replaces you as the interviewee in order to create a compelling conversation?
*  How far away are we do you think? It's a good question. I think partly I would say,
*  do we want that? I really like when we start now with very powerful models, interacting with them
*  and thinking of them more closer to us. The question is, if you remove the human side of
*  the conversation, is that an interesting artifact? And I would say probably not.
*  I've seen, for instance, last time we spoke, we were talking about StarCraft. Creating agents that
*  play games involves self-play, but ultimately what people care about was how does this agent behave
*  when the opposite side is a human? So without a doubt, we will probably be more empowered by AI.
*  Maybe you can source some questions from an AI system. That even today, I would say,
*  it's quite plausible that with your creativity, you might actually find very interesting questions
*  that you can filter. We call this cherry picking sometimes in the field of language.
*  And likewise, if I had now the tools on my side, I could say, look, you're asking this interesting
*  question. From this answer, I like the words chosen by this particular system that created a few words.
*  Completely replacing it feels not exactly exciting to me. Although in my lifetime, I think way,
*  given the trajectory, I think it's possible that perhaps there could be interesting maybe self-play
*  interviews, as you're suggesting, that would look or sound quite interesting and probably
*  would educate or you could learn a topic through listening to one of these interviews at a basic
*  level, at least. So you said it doesn't seem exciting to you, but what if exciting is part
*  of the objective function the thing is optimized over? So there's probably a huge amount of data
*  of humans, if you look correctly, of humans communicating online, and there's probably ways
*  to measure the degree of, as they talk about, engagement. So you can probably optimize the
*  question that's most created an engaging conversation in the past. So actually, if you
*  strictly use the word exciting, there is probably a way to create a optimally exciting conversations
*  that involve AI systems. At least one side is AI. Yeah, that makes sense. I think maybe looping back
*  a bit to games and the game industry, when you design algorithms, you're thinking about winning
*  as the objective, right, or the reward function. But in fact, when we discuss this with Blizzard,
*  the creators of StarCraft in this case, I think what's exciting, fun, if you could measure that
*  and optimize for that, that's probably why we play video games, or why we interact, or listen,
*  or look at cat videos, or whatever on the internet. So it's true that modeling reward beyond the
*  obvious reward functions we're used to in reinforcement learning is definitely very exciting.
*  And again, there is some progress actually into a particular aspect of AI, which is quite critical,
*  which is, for instance, is a conversation that or is the information truthful, right? So you could
*  start trying to evaluate these from accepts from the internet, right, that has lots of information.
*  And then if you can learn a function automated, ideally, so you can also optimize it more easily,
*  then you could actually have conversations that optimize for non-obvious things such as excitement.
*  So yeah, that's quite possible. And then I would say, in that case, it would definitely be fun,
*  a fun exercise and quite unique to have at least one side that is fully driven by
*  an excitement reward function. But obviously, there would be still quite a lot of humanity in
*  the system, both from who is building the system, of course, and also ultimately, if we think of
*  labeling for excitement, that those labels must come from us because it's just hard to
*  have a computational measure of excitement. As far as I understand, there's no such thing.
*  Well, you mentioned truth also, I would actually venture to say that excitement is easier to label
*  than truth, or is perhaps has lower consequences of failure. But there is perhaps this the
*  humaneness that you mentioned, that's perhaps part of a thing that could be labeled. And that could
*  mean an AI system that's doing dialogue, that's doing conversations should be flawed, for example.
*  Like that's the thing you optimize for, which is have inherent contradictions by design,
*  have flaws by design. Maybe it also needs to have a strong sense of identity.
*  So it has a backstory, it told itself that it sticks to it has memories, not in terms of the
*  how the system is designed, but it's able to tell stories about its past. It's able to have
*  a mortality and fear of mortality in the following way that it has an identity.
*  And if it says something stupid and gets canceled on Twitter, that's the end of that system. So it's
*  not like you get to rebrand yourself, that system is that's it. So maybe that the high stakes nature
*  of it, because you can't say anything stupid now, because you'd be canceled on Twitter. And that
*  there's there's stakes to that. And then I think part of the reason that makes it interesting.
*  And then you have a perspective like you've built up over time that you stick with,
*  and then people can disagree with you. So holding that perspective strongly,
*  holding sort of maybe a controversial at least a strong opinion, all of those elements, it feels
*  like they can be learned because it feels like there's a lot of data on the internet of people
*  having an opinion. And then combine that with a metric of excitement, you can start to create
*  something that as opposed to trying to optimize for sort of grammatical clarity and truthfulness,
*  the factual consistency over many sentences, you're optimized for the humanness. And there's
*  obviously data for humanness on the internet. So I wonder, I wonder if there's a future where
*  that's part or I mean, I sometimes wonder that about myself. I'm a huge fan of podcasts.
*  And I listened to some podcasts. And I think like, what is interesting about this? What is compelling?
*  The same way you watch other games, like you said, watch play Starcraft or
*  have Magnus Carlsen play chess. So I'm not a chess player. So but it's still interesting to
*  me. What is that? That's the stakes of it, maybe the end of a domination of a series of wins.
*  I don't know, there's all those elements somehow connect to a compelling conversation. And I wonder
*  how hard is that to replace? Because ultimately, all of that connects to the initial proposition
*  of how to test whether an AI is intelligent or not with the Turing test, which I guess,
*  my question comes from a place of the spirit of that test.
*  Yes, I actually recall I was just listening to our first podcast where we discussed Turing test.
*  So I would say from a neural network, AI builder perspective, there's usually you try to map
*  many of these interesting topics you discuss to benchmarks, and then also to actual architectures
*  on how these systems are currently built, how they learn, what data they learn from,
*  what are they learning, right? We're talking about weights of a mathematical function.
*  And then looking at the current state of the game, maybe what do we need leaps forward to get to the
*  ultimate stage of all these experiences, lifetime experience, fears, like words that currently,
*  barely we're seeing progress just because what's happening today is you take all these
*  human interactions, it's a large vast variety of human interactions online, and then you're
*  distilling these sequences, right? Going back to my passion, like sequences of words, letters,
*  images, sound, there's more modalities here to be at play. And then you're trying to just learn a
*  function that will be happy, that maximizes the likelihood of seeing all these through a neural
*  network. Now, I think there's a few places where the way currently we train these models would
*  clearly like to be able to develop the kinds of capabilities you save. I'll tell you maybe a couple.
*  One is the lifetime of an agent or a model. So you learn from this data offline, right? So you're
*  just passively observing and maximizing this, it's almost like a landscape of mountains.
*  And then everywhere there's data that humans interacted in this way, you're trying to make
*  that higher and then lower where there's no data. And then these models generally don't
*  then experience themselves, they just are observers, right? They're passive observers of the data.
*  And then we're putting them to then generate data when we interact with them. But that's very
*  limiting the experience they actually experience when they could maybe be optimizing or further
*  optimizing the weights. We're not even doing that. So to be clear, and again, mapping to
*  AlphaGo, AlphaStar, we train the model. And when we deploy it to play against humans, or in this
*  case, interact with humans, like language models, they don't even keep training, right? They're not
*  learning in the sense of the weights that you've learned from the data, they don't keep changing.
*  Now, there's something a bit more feels magical, but it's understandable if you're into neural net,
*  which is, well, they might not learn in the strict sense of the words, the weights changing, maybe
*  that's mapping to how neurons interconnect and how we learn over our lifetime. But it's true that
*  the context of the conversation that takes place with when you talk to these systems,
*  it's held in their working memory, right? It's almost like you start the computer,
*  it has a hard drive that has a lot of information, you have access to the internet, which has probably
*  all the information. But there's also a working memory where these agents, as we call them,
*  or start calling them, build upon. Now, these memories are very limited. I mean, right now,
*  we're talking, to be concrete, about 2000 words that we hold. And then beyond that, we start
*  forgetting what we've seen. So you can see that there's some short-term coherence already, right?
*  With when you said, I mean, it's a very interesting topic, mapping an agent to have consistency,
*  then if you say, oh, what's your name, it could remember that, but then it might forget
*  beyond 2000 words, which is not that long of context, if we think even of this podcast,
*  books are much longer. So technically speaking, there's a limitation there, super exciting from
*  people that work on deep learning to be working on. But I would say we lack maybe benchmarks and
*  the technology to have this lifetime-like experience of memory that keeps building up.
*  However, the way it learns offline is clearly very powerful, right? So you asked me three years ago,
*  I would say, oh, we're very far. I think we've seen the power of this imitation, again,
*  of the internet scale that has enabled this to feel like at least the knowledge, the basic
*  knowledge about the world now is incorporated into the weights. But then this experience is lacking.
*  And in fact, as I said, we don't even train them when we're talking to them, other than
*  their working memory, of course, is affected. So that's the dynamic part, but they don't learn in
*  the same way that you and I have learned from basically when we were born and probably before.
*  So lots of fascinating, interesting questions you asked there. I think the one I mentioned is this
*  idea of memory and experience versus just kind of observe the world and learn its knowledge,
*  which I think for that, I would argue lots of recent advancements that make me very excited
*  about the field. And then the second maybe issue that I see is all these models, we train them from
*  scratch. That's something I would have complained three years ago or six years ago or 10 years ago.
*  And it feels if we take inspiration from how we got here, how the universe evolved us,
*  and we keep evolving, it feels that is a missing piece, that we should not be training models from
*  scratch every few months, that there should be some sort of way in which we can grow models,
*  much like as a species and many other elements in the universe is building from the previous
*  sort of iterations. And that's from a just purely neural network perspective.
*  Even though we would like to make it work, it's proven very hard to not throw away the previous
*  weights, this landscape we learn from the data and refresh it with a brand new set of weights,
*  given maybe a recent snapshot of this data set we train on, etc., or even a new game we're learning.
*  So that feels like something is missing fundamentally. We might find it, but it's
*  not very clear how it will look like. There are many ideas and it's super exciting as well.
*  Yes, just for people who don't know, when you're approaching a new problem in machine learning,
*  you're going to come up with an architecture that has a bunch of weights and then you initialize
*  them somehow, which in most cases is some version of random. So that's what you mean by starting
*  from scratch. And it seems like it's a waste every time you solve the game of Go and chess,
*  Starcraft, protein folding. Surely there's some way to reuse the weights as we grow this giant
*  database of neural networks that have solved some of the toughest problems in the world.
*  And so some of that is, what is that? Methods, how to reuse weights, how to learn, extract,
*  what's generalizable, or at least has a chance to be and throw away the other stuff. And maybe
*  the neural network itself should be able to tell you that. What ideas do you have for better
*  initialization of weights? Maybe stepping back, if we look at the field of machine learning,
*  but especially deep learning, at the core of deep learning, there's this beautiful idea that is
*  a single algorithm can solve any task. So it's been proven over and over with more increasing
*  set of benchmarks and things that were thought impossible that are being cracked by this basic
*  principle that is you take a neural network of uninitialized weights, so like a blank
*  computational brain, then you give it, in the case of supervised learning, a lot,
*  ideally, of examples of, hey, here is what the input looks like, and the desired output should
*  look like this. Image classification is a very clear example. Images to maybe one of a thousand
*  categories, that's what ImageNet is like. But many, many, if not all problems can be mapped this way.
*  And then there's a generic recipe that you can use. And this recipe with very little change,
*  and I think that's the core of deep learning research, that what is the recipe that is universal,
*  that for any new given task, I'll be able to use without thinking, without having to work very hard
*  on the problem at stake. We have not found this recipe, but I think the field is excited to find
*  less tweaks or tricks that people find when they work on important problems specific to those,
*  and more of a general algorithm. So at an algorithmic level, I would say we have something
*  general already, which is this formula of training a very powerful model, a neural network,
*  on a lot of data. And in many cases, you need some specificity to the actual problem you're solving.
*  Protein folding being such an important problem has some basic recipe that is learned from
*  beyond before, like transformer models, graph neural networks, ideas coming from NLP, like
*  something called BERT that is a kind of loss that you can emplace to help the model.
*  Knowledge distillation is another technique. So this is the formula. We still had to find some
*  particular things that were specific to alpha fold. That's very important because protein
*  folding is such a high value problem that as humans, we should solve it no matter if we need
*  to be a bit specific. And it's possible that some of these learnings will apply then to the next
*  iteration of this recipe that deep learners are about. But it is true that so far, the recipe is
*  what's common, but the weights you generally throw away, which feels very sad. Although maybe
*  in the last, especially in the last two, three years, and when we last spoke, I mentioned this
*  area of meta-learning, which is the idea of learning to learn. That idea and some progress
*  has been had starting, I would say mostly from GPT-3 on the language domain only, in which
*  you could conceive a model that is trained once, and then this model is not narrow in that it only
*  knows how to translate a pair of languages or it only knows how to assign sentiment to a sentence.
*  You could teach it by a prompting, it's called. And this prompting is essentially just showing
*  it a few more examples, almost like you do show examples, input-output examples, algorithmically
*  speaking to the process of creating this model. But now you're doing it through language, which
*  is a very natural way for us to learn from one another. I tell you, hey, you should do this new
*  task. I'll tell you a bit more. Maybe you ask me some questions and now you know the task. You
*  didn't need to retrain it from scratch. And we've seen these magical moments almost in this way to
*  do a few-shot promptings through language on language-only domain. And then in the last
*  two years, we've seen these expanded to beyond language, adding vision, adding actions and games,
*  lots of progress to be had. But this is maybe, if you ask me about how are we going to crack
*  this problem, this is perhaps one way in which you have a single model. The problem of this model is
*  it's hard to grow in weights or capacity, but the model is certainly so powerful that you can teach
*  it some tasks in this way that I could teach you a new task now if we were all at a text-based task
*  or a classification, a vision-style task. But it still feels like more breakthroughs should be had,
*  but it's a great beginning. We have a good baseline. We have an idea that this maybe is
*  the way we want to benchmark progress towards AGI. And I think in my view, that's critical to always
*  have a way to benchmark the community sort of converging to this overall, which is good to see.
*  And then this is actually what excites me in terms of also next steps for deep learning is
*  how to make these models more powerful. How do you train them? How to grow them? If they must grow,
*  should they change their weights as you teach it the task or not? There's some interesting questions,
*  many to be answered. Yeah, you've opened the door to a bunch of questions I want to ask, but let's
*  first return to your tweet and read it like a Shakespeare. You wrote,
*  Gato is not the end, it's the beginning. And then you wrote meow and then an emoji of a cat.
*  So first, two questions. First, can you explain the meow and the cat emoji? And second,
*  can you explain what Gato is and how it works? Right. Indeed. I mean, thanks for reminding me
*  that we're all exposing on Twitter and permanently there. Yes, permanently. One of the greatest
*  AI researchers of all time, meow and cat emoji. Yes. There you go. Right. So can you imagine like
*  touring and tweeting meow and cat? Probably he would. Probably. So yeah, the tweet is important
*  actually. You know, I put thought on the tweets. I hope people which part you think. Okay. So there's
*  three sentences. Gato is not the end. Gato is the beginning. Meow cat emoji. Which is the important
*  part? The meow. No, no. Definitely that it is the beginning. I mean, I probably was just explaining
*  a bit where the field is going, but let me tell you about Gato. So first, the name Gato
*  comes from maybe a sequence of releases that the mind had that named, like used animal names to
*  name some of their models that are based on this idea of large sequence models. Initially,
*  they're only language, but we are expanding to other modalities. So we had Gopher, Chinchilla.
*  These were language only. And then more recently we released Flamingo, which adds vision to the
*  equation. And then Gato, which adds vision and then also actions in the mix. Right. As we discuss
*  actually actions, especially discrete actions like up, down, left, right. I just told you the
*  actions, but they're words. So you can kind of see how actions naturally map to sequence modeling of
*  words, which these models are very powerful. So Gato was named after, I believe I can only
*  from memory, right? These things always happen with an amazing team of researchers behind. So
*  before the release, we had a discussion about which animal would we pick. And I think because
*  of the word general agent, and this is a property quite unique to Gato, we kind of were playing with
*  the GA words and then Gato- Kind of rise of cat. Yes. And Gato is obviously a Spanish version of
*  cat. I had nothing to do with it, although I'm from Spain. Oh, how do you say cat in Spanish?
*  Gato. Oh, Gato. Okay. Now I see. I see. I see you. Now it all makes sense. Okay. How do you say
*  meow in Spanish? No, that's probably the same. I think you say it the same way, but you write it
*  as M-I-A-U. It's universal. Yeah. All right. So then how does the thing work? So you said
*  general is, so you said language, vision, and action. How does this, can you explain what kind
*  of neural networks are involved? What does the training look like? And maybe what do you,
*  or some beautiful ideas within the system? Yeah. So maybe the basics of Gato are not that dissimilar
*  from many, many work that comes. So here is where the sort of the recipe, I mean, hasn't changed too
*  much. There is a transformer model. That's the kind of recurrent neural network that essentially
*  takes a sequence of modalities, observations that could be words, could be vision, or could be
*  actions. And then its own objective that you train it to do when you train it is to predict
*  what the next anything is. And anything means what's the next action. If this sequence that
*  I'm showing you to train is a sequence of actions and observations, then you're predicting what's
*  the next action and the next observation. So you think of these really as a sequence of bytes. So
*  take any sequence of words, a sequence of interleaved words and images, a sequence of
*  maybe observations that are images and moves in Atari, up, down, left, right. And these,
*  you just think of them as bytes and you're modeling what's the next byte going to be like.
*  And you might interpret that as an action and then play it in a game, or you could interpret
*  it as a word and then write it down if you're chatting with the system and so on. So GATO
*  basically can be thought as inputs, images, text, video, actions. It also actually inputs some sort
*  of proprioception sensors from robotics because robotics is one of the tasks that it's been trained
*  to do. And then at the output, similarly, it outputs words, actions. It does not output images.
*  That's just by design, we decided not to go that way for now. That's also in part why it's the
*  beginning because there's more to do clearly. But that's kind of what the GATO is. It's this brain
*  that essentially you give it any sequence of these observations and modalities and it outputs the
*  next step. And then off you go, you feed the next step into and predict the next one and so on.
*  Now, it is more than a language model because even though you can chat with GATO, like you can chat
*  with Chinchilla or Flamingo, it also is an agent. So that's why we call it A of GATO, the letter A.
*  And also, it's general. It's not an agent that's been trained to be good at only StarCraft or only
*  Atari or only Go. It's been trained on a vast variety of datasets. What makes it an agent,
*  if I may interrupt? The fact that it can generate actions? Yes. It's a good question. When do we
*  call a model? Everything is a model, but what is an agent in my view is indeed the capacity to take
*  actions in an environment that you then send to it and then the environment might return with
*  a new observation and then you generate the next action. This actually reminds me of the question
*  from the side of biology, what is life? Which is actually a very difficult question as well.
*  What is living when you think about life here on this planet Earth? And a question interesting to
*  me about aliens, what is life when we visit another planet? Would we be able to recognize it? And this
*  feels like it sounds perhaps silly, but I don't think it is. At which point is the neural network
*  a being versus a tool? And it feels like action, ability to modify its environment,
*  is that fundamental leap? Yeah, I think it certainly feels like action is a necessary condition
*  to be more alive, but probably not sufficient either. So sadly- It's a whole consciousness
*  thing, whatever. Yeah, we can get back to that later. But anyways, going back to the meow and
*  the gato, right? So one of the leaps forward and what took the team a lot of effort and time was,
*  as you were asking, how has gato been trained? So I told you gato is this transformer neural
*  network, models, actions, sequences of actions, words, et cetera. And then the way we train it is
*  by essentially pulling datasets of observations. So it's a massive imitation learning algorithm
*  that it imitates obviously to what is the next word that comes next from the usual datasets we
*  use before. So these are these web scale style datasets of people writing on webs or chatting
*  or whatnot. So that's an obvious source that we use on all language work. But then we also took
*  a lot of agents that we have at DeepMind. I mean, as you know, DeepMind, we're quite interested in
*  reinforcement learning and learning agents that play in different environments. So we kind of
*  created a dataset of these trajectories, as we call them, or agent experiences. So in a way,
*  there are other agents we train for a single mind purpose to, let's say, control a 3D game
*  environment and navigate a maze. So we had all the experience that was created through the one
*  agent interacting with that environment. And we added this to the dataset. And as I said,
*  we just see all the data, all these sequences of words or sequences of these agent interacting with
*  that environment, or agents playing Atari and so on. We see it as the same kind of data. And so
*  we mix these datasets together and we train GATO. That's the G part, right? It's general because
*  it really has mixed, it doesn't have different brains for each modality or each narrow task.
*  It has a single brain. It's not that big of a brain compared to most of the neural networks
*  we see these days. It has one billion parameters. Some models we're seeing getting the trillions
*  these days, and certainly 100 billion feels like a size that is very common from when you train
*  these jobs. So the actual agent is relatively small, but it's been trained on a very challenging,
*  diverse dataset, not only containing all of internet, but containing all these agent
*  experience playing very different distinct environments. So this brings us to the part
*  of the tweet of this is not the end, it's the beginning. It feels very cool to see GATO in
*  principle is able to control any sort of environments that especially the ones that it's been trained to
*  do these 3D games, Atari games, all sorts of robotics tasks and so on. But obviously it's not
*  as proficient as the teachers it learned from on these environments.
*  It's not obvious that it wouldn't be more proficient. It's just the current beginning part
*  is that the performance is such that it's not as good as if it's specialized to that task.
*  Right. So it's not as good, although I would argue size matters here.
*  I would argue always size always matters. That's a different conversation.
*  But for neural networks, certainly size does matter. So it's the beginning because it's
*  relatively small. So obviously scaling this idea up might make the connections that exist between
*  text on the internet and playing Atari and so on more synergistic with one another.
*  And you might gain. And that moment we didn't quite see, but obviously that's why it's the
*  beginning. That synergy might emerge with scale.
*  Right. It might emerge with scale. And also I believe there's some new research or
*  ways in which you prepare the data that you might need to sort of make it more clear to the model
*  that you're not only playing Atari and you start from a screen and here is up and a screen and
*  down. Maybe you can think of playing Atari as there's some sort of context that is needed
*  for the agent before it starts seeing, oh, this is an Atari screen. I'm going to start playing.
*  You might require, for instance, to be told in words, hey, in this sequence that I'm showing,
*  you're going to be playing an Atari game. So text might actually be a good driver to enhance the
*  data. So then these connections might be made more easily. That's an idea that we start seeing
*  in language, but obviously beyond this is going to be effective. It's not like I don't show you
*  a screen and you from scratch, you're supposed to learn a game. There is a lot of context we
*  might set. So there might be some work needed as well to set that context. But anyways, there's a
*  lot of work. So that context puts all the different modalities on the same level ground. Exactly.
*  Provide the context best. So maybe on that point, so there's this task, which may not seem trivial,
*  of tokenizing the data, of converting the data into pieces, into basic atomic elements
*  that then could cross modalities somehow. So what's tokenization? How do you tokenize text?
*  How do you tokenize images? How do you tokenize games and actions and robotics tasks?
*  Yeah, that's a great question. So tokenization is the entry point to actually make all the data
*  look like a sequence because tokens then are just kind of these little puzzle pieces. We break down
*  anything into these puzzle pieces and then we just model what's this puzzle look like when you make
*  it lay down in a line, so to speak, in a sequence. So in GATO, the text, there's a lot of work.
*  You tokenize text usually by looking at commonly used substrings. So there's ING in English is a
*  very common substring, so that becomes a token. There's quite well-studied problem on tokenizing
*  text. And GATO just used the standard techniques that have been developed from many years, even
*  starting from Ngram models in the 1950s and so on. Just for context, how many tokens, what order,
*  magnitude, number of tokens is required for a word? What are we talking about?
*  Yeah, for a word in English, every language is very different. The current level or granularity
*  of tokenization generally means maybe two to five. I don't know the statistics exactly, but
*  to give you an idea, we don't tokenize at the level of letters, then it would probably be like,
*  I don't know what the average length of a word is in English, but that would be the minimum set
*  of tokens you could use. It's bigger than letters, smaller than words. Yes, yes. And you could think
*  of very, very common words like the, I mean, that would be a single token, but very quickly,
*  you're talking two, three, four tokens or so. Have you ever tried to tokenize emojis? Emojis are
*  actually just sequences of letters. So maybe to you, but to me, they mean so much more. Yeah,
*  you can render the emoji, but you might, if you actually just... Yeah, this is a philosophical
*  question. Is emojis an image or a text? The way we do these things is they're actually mapped to
*  small sequences of characters. So you can actually play with these models and input emojis. It will
*  output emojis back, which is actually quite a fun exercise. You probably can find other tweets
*  about these out there. But yeah, so anyway, text, it's very clear how this is done. And then in GATO,
*  what we did for images is we map images to essentially, we compress images, so to speak,
*  into something that looks more like every pixel with every intensity. That would mean we have a
*  very long sequence, right? Like if we were talking about 100 by 100 pixel images, that would make the
*  sequences far too long. So what was done there is you just use a technique that essentially compresses
*  an image into maybe 16 by 16 patches of pixels. And then that is mapped, again, tokenized. You just
*  essentially quantize this space into a special word that actually maps to these little sequence
*  of pixels. And then you put the pixels together in some raster order, and then that's how you get
*  out or in the image that you're processing. But there's no semantic aspect to that.
*  So you're doing some kind of... You don't need to understand anything about the image in order to
*  tokenize it currently. No, you're only using this notion of compression. So you're trying to
*  find common... It's like JPG or all these algorithms. It's actually very similar
*  at the tokenization level. All we're doing is finding common patterns and then making sure
*  in a lossy way we compress these images, given the statistics of the images that are contained in all
*  the data we deal with. Although you could probably argue that JPEG does have some understanding of
*  images. Because visual information, maybe color, compressing crudely based on color does capture
*  something important about an image, about its meaning, not just about some statistics.
*  Yeah, I mean, JPG, as I said, the algorithms look actually very similar. They use the
*  cosine transform in JPG. The approach we usually do in machine learning when we deal with images
*  and we do this quantization step is a bit more data-driven. So rather than have some sort of
*  Fourier basis for how frequencies appear in the natural world, we actually just use
*  the statistics of the images and then quantize them based on the statistics, much like you do
*  in words. So common substrings are allocated a token and images is very similar. But there's no
*  connection. The token space, if you think of the tokens are an integer at the end of the day. So
*  now we work on... Maybe we have about, let's say, I don't know the exact numbers, but let's say 10,000
*  tokens for text, certainly more than characters because we have groups of characters and so on.
*  So from 1 to 10,000, those are representing all the language and the words we'll see. And then
*  images occupy the next set of integers. So they're completely independent. So from 10,001 to 20,000,
*  those are the tokens that represent these other modality images. And that is an interesting
*  aspect that makes it orthogonal. So what connects these concepts is the data. Once you have a data
*  set, for instance, that captions images that tells you, oh, this is someone playing a frisbee on a
*  green field. Now the model will need to predict the tokens from the text green field to then the
*  pixels. And that will start making the connections between the tokens. So these connections happen
*  as the algorithm learns. And then the last, if we think of these integers, the first few are words,
*  the next few are images. In GATO, we also allocated the highest order of integers to actions,
*  which we discretize. And actions are very diverse. In Atari, there's, I don't know if 17, discrete
*  actions. In robotics, actions might be torques and forces that we apply. So we just use similar ideas
*  to compress these actions into tokens. And then we just, that's how we map now all the space to
*  these sequence of integers. But they occupy different space. And what connects them is then
*  the learning algorithm. That's where the magic happens. So the modalities are orthogonal to each
*  other in token space. So in the input, everything you add, you add extra tokens. And then you're
*  shoving all of that into one place. Yes, the transformer. And that transformer, that transformer
*  tries to look at this gigantic token space and tries to form some kind of representation,
*  some kind of unique wisdom about all of these different modalities. How's that possible? If you
*  were to sort of put your psychoanalysis hat on and try to psychoanalyze this neural network,
*  is it schizophrenic? Does it try to, given this very few weights, represent multiple disjoint
*  things and somehow have them not interfere with each other? Or is this a more building on the
*  joint strength, on whatever is common to all the different modalities? Like what,
*  if you were to ask a question, is it schizophrenic or is it of one mind?
*  I mean, it is one mind. And it's actually the simplest algorithm, which that's kind of in a
*  way how it feels like the field hasn't changed since backpropagation and gradient descent was
*  purpose for learning neural networks. So there is obviously details on the architecture. This
*  has evolved. The current iteration is still the transformer, which is a powerful sequence modeling
*  architecture. But then the goal of this, you know, setting these weights to predict the data is
*  essentially the same as basically I could describe. I mean, we described a few years ago, alpha star,
*  language modeling, and so on. We take, let's say, an Atari game, we map it to a string of numbers
*  that will all be probably image space and action space interleaved. And all we're going to do is
*  say, okay, given the numbers, you know, 1001, 1004, 1005, the next number that comes is 2006,
*  which is in the action space. And you're just optimizing these weights via very simple
*  gradients like, you know, mathematical is almost the most boring algorithm you could imagine.
*  We settle the weights so that given this particular instance, these weights are set to
*  maximize the probability of having seen this particular sequence of integers for this
*  particular game. And then the algorithm does this for many, many, many iterations, looking at
*  different modalities, different games, right? That's the mixture of the data set we discussed.
*  So in a way, it's a very simple algorithm and the weights, right, they're all shared, right? So in
*  terms of, is it focusing on one modality or not? The intermediate weights that are converting from
*  these input of integers to the target integer you're predicting next, those weights certainly
*  are common. And then the way the tokenization happens, there is a special place in the neural
*  network, which is we map this integer, like number 1001, to a vector of real numbers. Like real
*  numbers, we can optimize them with gradient descent, right? The functions we learn are actually
*  surprisingly differentiable. That's why we compute gradients. So this step is the only one that this
*  orthogonality you mentioned applies. So mapping a certain token for text or image or actions,
*  each of these tokens gets its own little vector of real numbers that represents this. If you look at
*  the field back many years ago, people were talking about word vectors or word embeddings.
*  These are the same. We have word vectors or embeddings. We have image vector or embeddings
*  and action vector of embeddings. And the beauty here is that as you train this model, if you
*  visualize these little vectors, it might be that they start aligning even though they're independent
*  parameters. There could be anything, but then it might be that you take the word gato or cat,
*  which maybe is common enough that it actually has its own token. And then you take pixels that have
*  a cat and you might start seeing that these vectors look like they align. So by learning from
*  this vast amount of data, the model is realizing the potential connections between these modalities.
*  Now I will say there would be another way, at least in part, to not have these different
*  vectors for each different modality. For instance, when I tell you about actions in certain space,
*  I'm defining actions by words. So you could imagine a world in which I'm not learning
*  that the action app in Atari is its own number. The action app in Atari maybe is literally
*  the word or the sentence app in Atari. And that would mean we now leverage much more from the
*  language. This is not what we did here, but certainly it might make these connections
*  much easier to learn and also to teach the model to correct its own actions and so on.
*  All this to say that gato is indeed the beginning, that it is a radical idea to do this way,
*  but there's probably a lot more to be done and the results to be more impressive,
*  not only through scale, but also through some new research that will come hopefully in the years to
*  come. So just to elaborate quickly, you mean one possible next step or one of the paths that you
*  might take next is doing the tokenization fundamentally as a kind of linguistic communication.
*  So like you convert even images into language. So doing something like a crude semantic segmentation,
*  trying to just assign a bunch of words to an image that have almost like a dumb entity explaining
*  as much as it can about the image. And so you convert that into words and then you convert
*  games into words and then you provide the context in words and all of it.
*  Eventually getting to a point where everybody agrees with Noam Chomsky that language is actually
*  at the core of everything. It's the base layer of intelligence and consciousness and all that
*  kind of stuff. You mentioned early on, it's hard to grow. What did you mean by that? Because we're
*  talking about scale might change. There might be, and we'll talk about this too, there's a
*  emergent, there's certain things about these neural networks that are emergent. So certain
*  performance we can see only with scale and there's some kind of threshold of scale.
*  So why is it hard to grow something like this Miao network?
*  So the Miao network is not hard to grow if you retrain it. What's hard is, well, we have now
*  one billion parameters. We train them for a while. We spend some amount of work towards building
*  these weights that are an amazing initial brain for doing this kind of task we care about.
*  Could we reuse the weights and expand to a larger brain? That is extraordinarily hard but also
*  exciting from a research perspective and a practical perspective point of view.
*  There's this notion of modularity in software engineering and we're starting to see some
*  examples and work that leverages modularity. In fact, if we go back one step from Gato to a
*  work that I would say train much larger, much more capable network called Flamingo. Flamingo did not
*  deal with actions but it definitely dealt with images in an interesting way, kind of akin to
*  what Gato did but slightly different technique for tokenizing. But we don't need to go into that
*  detail. But what Flamingo also did, which Gato didn't do, and that just happens because these
*  projects, it's a bit of the exploratory nature of research which is great.
*  The research behind these projects is also modular.
*  Yes, exactly. And it has to be. We need to have creativity and sometimes you need to protect
*  pockets of people, researchers and so on. By we you mean humans.
*  Yes. And also in particular researchers and maybe even further DeepMind or other such labs.
*  And then the active neural networks themselves. So it's modularity all the way down.
*  All the way down. So the way that we did modularity very beautifully in Flamingo is we took Chinchilla,
*  which is a language only model, not an agent if we think of actions being necessary for agency.
*  So we took Chinchilla, we took the weights of Chinchilla, and then we froze them. We said,
*  these don't change. We train them to be very good at predicting the next world.
*  It's a very good language model, state of the art at the time you release it, etc.
*  We're going to add a capability to see. We are going to add the ability to see to this language
*  model. So we're going to attach small pieces of neural networks at the right places in the model.
*  It's almost like injecting the network with some weights and some substructures
*  in a good way. So you need the research to say what is effective, how do you add this capability
*  without destroying others, etc. So we created a small sub network initialized not from random,
*  but actually from self-supervised learning, a model that understands vision in general.
*  And then we took datasets that connect the two modalities, vision and language. And then we froze
*  the main part, the largest portion of the network, which was Chinchilla, that is 70 billion parameters.
*  And then we added a few more parameters on top, trained from scratch, and then some others that
*  were pre-trained with the capacity to see. It was not tokenization in the way I describe for Gato,
*  but it's a similar idea. And then we trained the whole system. Parts of it were frozen,
*  parts of it were new. And all of a sudden, we developed Flamingo, which is an amazing model
*  that is essentially, I mean, describing it as a chatbot where you can also upload images and
*  start conversing about images. But it's also kind of a dialogue style chatbot.
*  So the input is images and text and the output is text.
*  Exactly. How many parameters? You said 70 billion for Chinchilla.
*  Yeah, Chinchilla is 70 billion. And then the ones we add on top, which is almost like
*  a way to overwrite its little activation so that when it sees vision, it does kind of a correct
*  computation of what it's seeing, mapping it back towards, so to speak. That adds an extra 10 billion
*  parameters. So it's total 80 billion, the largest one we released. And then you train it on a few
*  datasets that contain vision and language. And once you interact with the model, you start seeing
*  that you can upload an image and start sort of having a dialogue about the image, which is
*  actually not something... It's very similar and akin to what we saw in language only, these
*  prompting abilities that it has. You can teach it a new vision task. It does things beyond the
*  capabilities that in theory, the datasets provided in themselves, but because it leverages a lot of
*  the language knowledge acquired from Chinchilla, it actually has this few-shot learning ability
*  and these emerging abilities that we didn't even measure once we were developing the model.
*  But once developed, then as you play with the interface, you can start seeing, wow, okay,
*  yeah, it's cool. We can upload, I think one of the tweets talking about Twitter was this
*  image from Obama that is placing a weight and someone is kind of weighting themselves. And it's
*  kind of a joke style image. And it's notable because I think Andriy Karpaty a few years ago said,
*  no computer vision system can understand the subtlety of this joke in this image,
*  all the things that go on. And so what we try to do, and it's very anecdotally, I mean, this is not
*  a proof that we solved this issue, but it just shows that you can upload now this image and start
*  conversing with the model, trying to make out if it gets that there's a joke because the person
*  weighting themselves doesn't see that someone behind is making the weight higher and so on and
*  so forth. So it's a fascinating capability. And it comes from this key idea of modularity,
*  where we took a frozen brain and we just added a new capability. So the question is, should we,
*  so in a way you can see even from DeepMind, we have Flamingo that this modular approach
*  and thus could leverage the scale a bit more reasonably because we didn't need to retrain
*  a system from scratch. And on the other hand, we had Gato which used the same data sets,
*  but then it trained it from scratch. And so I guess big question for the community is,
*  should we train from scratch or should we embrace modularity? And this goes back to modularity
*  as a way to grow but reuse seems natural and it was very effective, certainly.
*  The next question is, if you go the way of modularity, is there a systematic way of
*  freezing weights and joining different modalities across, you know, not just two or three or four
*  networks, but hundreds of networks from all different kinds of places, maybe open source
*  network that looks at weather patterns. And you shove that in somehow and then you have networks
*  that, I don't know, do all kinds of the plague StarCraft and play all the other video games
*  you can keep adding them in without significant effort. Maybe the effort scales linearly or
*  something like that as opposed to like the more network you add, the more you have to worry about
*  the instabilities created. Yeah, so that vision is beautiful. I think there's still the question
*  about within single modalities like Chinchilla was reused, but now if we train
*  a next iteration of language models, are we going to use Chinchilla or not?
*  How do you swap out Chinchilla?
*  Right. So there's still big questions, but that idea is actually really akin to software
*  engineering, which we're not re-implementing, you know, libraries from scratch. We're reusing
*  and then building ever more amazing things, including neural networks with software that
*  we're reusing. So I think this idea of modularity, I like it. I think it's here to stay. And that's
*  also why I mentioned it's just the beginning, not the end.
*  You mentioned meta-learning. So given this promise of GATO, can we try to redefine this term
*  that's almost akin to consciousness because it means different things to different people
*  throughout the history of artificial intelligence? But what do you think meta-learning
*  is and looks like now in the five years, 10 years, will it look like the system like GATO but scaled?
*  What's your sense of what is what does meta-learning look like? Do you think with all
*  the wisdom we've learned so far? Yeah, great question. Maybe it's good to give
*  another data point looking backwards rather than forward. So when we talk in 2019, meta-learning
*  meant something that has changed mostly through the revolution of GPT-3 and beyond. So what
*  meta-learning meant at the time was driven by what benchmarks people care about in meta-learning.
*  And the benchmarks were about a capability to learn about object identities. So it was
*  very much overfitted to vision and object classification. And the part that was met
*  about that was that, oh, we're not just learning a thousand categories that ImageNet tells us to
*  learn. We're going to learn object categories that can be defined when we interact with the model.
*  So it's interesting to see the evolution. The way this started was we have a special language
*  that was a small data set that we prompted the model with saying, hey, here is a new
*  classification task. I'll give you one image and the name, which was an integer at the time of the
*  image and a different image and so on. So you have a small prompt in the form of a data set,
*  a machine learning data set. And then you got then a system that could then predict or classify
*  these objects that you just defined kind of on the fly. So fast forward, it was revealed that
*  language models are a few short learners. That's the title of the paper. So very good title.
*  Sometimes titles are really good. So this one is really, really good because that's the point of
*  GPT-3 that showed that, look, sure, we can focus on object classification and what meta-learning
*  means within the space of learning object categories. This goes beyond or before rather to
*  also Omniglot before ImageNet and so on. So there's a few benchmarks. To now, all of a sudden,
*  we're a bit unlocked from benchmarks and through language, we can define tasks. So we're literally
*  telling the model some logical task or little thing that we wanted to do. We prompt it much
*  like we did before, but now we prompt it through natural language. And then, not perfectly,
*  I mean, these models have failure modes and that's fine, but these models then are now
*  doing a new task. So they meta-learn this new capability. Now, that's where we are now.
*  Flamingo expanded this to visual and language, but it basically has the same abilities. You can
*  teach it, for instance, an emergent property was that you can take pictures of numbers and then do
*  arithmetic with the numbers just by teaching it, oh, that's, I mean, when I show you three plus
*  six, I want you to output nine and you show it a few examples and now it does that. So it went way
*  beyond this ImageNet sort of categorization of images that we were a bit stuck maybe before
*  this revelation moment that happened in 2000, I believe it was 19, but it was after we chat.
*  And that way it has solved meta-learning as was previously defined.
*  Yes, it expanded what it meant. So that's what you say. What does it mean? So it's an evolving term.
*  But here is maybe now looking forward, looking at what's happening, obviously in the community
*  with more modalities, what we can expect. And I would certainly hope to see the following.
*  And this is a pretty drastic hope, but in five years, maybe we chat again. And we have a system,
*  a set of weights that we can teach it to play StarCraft. Maybe not at the level of AlphaStar,
*  but play StarCraft, a complex game. We teach it through interactions to prompting. You can
*  certainly prompt a system. That's what Gato shows to play some simple Atari games. So imagine if you
*  start talking to a system, teaching it a new game, showing it examples of in this particular game,
*  this user did something good. Maybe the system can even play and ask you questions. Say,
*  hey, I played this game. I just played this game. Did I do well? Can you teach me more?
*  So five, maybe to 10 years, these capabilities, or what meta-learning means, will be much more
*  interactive, much more rich. And through domains that we were specializing, so you see the
*  difference. We built AlphaStar specialized to play StarCraft. The algorithms were general, but
*  the weights were specialized. And what we're hoping is that we can teach a network to play
*  games, to play any game, just using games as an example, through interacting with it, teaching it,
*  uploading the Wikipedia page of StarCraft. This is in the horizon, and obviously,
*  their details need to be filled and research needs to be done. But that's how I see meta-learning
*  above, which is going to be beyond prompting. It's going to be a bit more interactive.
*  The system might tell us to give it feedback after it maybe makes mistakes or it loses a game.
*  But it's nonetheless very exciting, because if you think about this this way, the benchmarks are
*  already there. We just repurposed the benchmarks. So in a way, I like to map the space of what
*  maybe AGI means to say, okay, we went 101% performance in Go, in chess, in StarCraft.
*  The next iteration might be 20% performance across, quote unquote, all tasks. And even if it's not as
*  good, it's fine. We actually have ways to also measure progress because we have those specialized
*  agents and so on. So this is, to me, very exciting. And these next iteration models are
*  definitely hinting at that direction of progress, which hopefully we can have. There are obviously
*  some things that could go wrong in terms of we might not have the tools, maybe transformers are
*  not enough, then we must, there's some breakthroughs to come, which makes the field more exciting to
*  people like me as well, of course. But that's, if you ask me five to 10 years, you might see
*  these models that start to look more like weights that are already trained, and then it's more about
*  teaching or they're meta-learn what you're trying to induce in terms of tasks and so on. Well beyond
*  the simple now tasks we're starting to see emerge, like, you know, small arithmetic tasks and so on.
*  So a few questions around that. This is fascinating. So that kind of teaching, interactive,
*  not so beyond prompting, interacting with the neural network, that's different than the training
*  process. So it's different than the optimization over differentiable functions. This is already
*  trained and now you're teaching, I mean, it's almost akin to the brain, the neurons are already
*  set with their connections. On top of that, you're now using that infrastructure to build up further
*  knowledge. Okay, so that's a really interesting distinction that's actually not obvious from a
*  software engineering perspective, that there's a line to be drawn. Because you always think for
*  neural network to learn it has to be retrained, trained and retrained. But maybe, and prompting
*  is a way of teaching, and neural network a little bit of context about whatever the heck you're
*  trying it to do. So you can maybe expand this prompting capability by making it interact.
*  That's really, really interesting. Yeah, by the way, this is not, if you look at way back at
*  different ways to tackle even classification tasks. So this comes from long standing literature
*  in machine learning. What I'm suggesting could sound to some like a bit like nearest neighbor.
*  So nearest neighbor is almost the simplest algorithm that does not require learning. So it has this
*  interesting, like you don't need to compute gradients. And what nearest neighbor does is
*  you quote unquote have a data set or upload a data set. And then all you need to do is a way
*  to measure distance between points. And then to classify a new point, you're just simply computing
*  what's the closest point in this massive amount of data. And that's my answer. So you can think of
*  prompting in a way as you're uploading not just simple points and the metric is not the distance
*  between the images or something simple. It's something that you compute that's much more
*  advanced. But in a way it's very similar. You simply are uploading some knowledge to this
*  pre-trained system in nearest neighbor. Maybe the metric is learned or not, but you don't need to
*  further train it. And then now you immediately get a classifier out of this. Now it's just an
*  evolution of that concept, very classical concept in machine learning, which is just learning
*  through what's the closest point, closest by some distance, and that's it. It's an evolution of
*  that. And I will say how I saw meta-learning when we worked on a few ideas in 2016 was precisely
*  through the lens of nearest neighbor, which is very common in computer vision community. There's a
*  very active area of research about how do you compute the distance between two images. But if
*  you have a good distance metric, you also have a good classifier. All I'm saying is now these
*  distances and the points are not just images. They're like words or sequences of words and
*  images and actions that teach you something new. But it might be that technique-wise those come
*  back. And I will say that it's not necessarily true that you might not ever train the weights a
*  bit further. Some aspects of meta-learning, some techniques in meta-learning do actually do a bit
*  of fine tuning, as it's called. They train the weights a little bit when they get a new task.
*  As I call the how or how we're going to achieve this, as a deep learner, I'm very skeptic. We're
*  going to try a few things, whether it's a bit of training, adding a few parameters, thinking of
*  these as nearest neighbor, or just simply thinking of there's a sequence of words, it's a prefix.
*  And that's the new classifier. We'll see. There's the beauty of research. But what's important is
*  that is a good goal in itself that I see as very worthwhile pursuing for the next stages of
*  not only meta-learning. I think this is basically what's exciting about machine learning, period,
*  to me. Well, the interactive aspect of that is also very interesting. The interactive version
*  of nearest neighbor to help you pull out the classifier from this giant thing. Okay. Is this
*  the way we can go in five, 10 plus years from any task, sorry, from many tasks to any task?
*  And what does that mean? What does it need to be actually trained on?
*  Which point is the network had enough? What does a network need to learn about this world in order
*  to be able to perform any task? Is it just as simple as language, image, and action? Or do you
*  need some set of representative images? Like if you only see land images, will you know anything
*  about underwater? Is that some fundamentally different? I don't know.
*  I mean, those are awkward questions, I would say. I mean, the way you put, let me maybe further
*  your example, right? If all you see is land images, but you're reading all about land and water
*  worlds, but in books, right? Imagine, would that be enough? Good question. We don't know, but I
*  guess maybe you can join us if you want in our quest to find this. That's precisely-
*  Water world, yeah.
*  Yes, that's precisely, I mean, the beauty of research and the research business we're in,
*  I guess, is to figure this out and ask the right questions and then iterate with the whole community
*  publishing findings and so on. But yeah, this is a question. It's not the only question,
*  but it's certainly, as you ask, is on my mind constantly, right? And so we'll need to wait for
*  maybe the, let's say, five years. Let's hope it's not 10 to see what are the answers.
*  Some people will largely believe in unsupervised or self-supervised learning of single modalities
*  and then crossing them. Some people might think end-to-end learning is the answer,
*  modularity is maybe the answer. So we don't know, but we're just definitely excited to find out.
*  But it feels like this is the right time and we're at the beginning of this.
*  We're finally ready to do these kind of general big models and agents. What do you sort of specific
*  technical thing about Gado, Flamingo, Chinchilla, Gopher, any of these that is especially beautiful,
*  that was surprising maybe? Is there something that just jumps out at you? Of course, there's
*  the general thing of like, you didn't think it was possible and then you realize it's possible
*  in terms of the generalizability across modalities and all that kind of stuff. Or maybe how small of
*  a network, relatively speaking, Gado is all that kind of stuff. But is there some weird
*  little things that were surprising? Look, I'll give you an answer that's very important because
*  maybe people don't quite realize this, but the teams behind these efforts, the actual humans,
*  that's maybe the surprising, in an obviously positive way. So anytime you see these breakthroughs,
*  I mean, it's easy to map it to a few people. There's people that are great at explaining
*  things and so on. That's very nice. But maybe the learnings or the meta learnings that I get as a
*  human about this is, sure, we can move forward. But the surprising bit is how important are all
*  the pieces of these projects? How do they come together? So I'll give you maybe some of the
*  ingredients of success that are common across these, but not the obvious ones and machine
*  learning. I can always also give you those. But basically, engineering is critical. So very good
*  engineering because ultimately we're collecting data sets, so the engineering of data and then
*  of deploying the models at scale into some compute cluster that cannot go understated, that is a huge
*  factor of success. And it's hard to believe that details matter so much. We would like to believe
*  that it's true that there is more and more of a standard formula, as I was saying, like this recipe
*  that works for everything. But then when you zoom in into each of these projects, then you realize
*  the devil is indeed in the details. And then the teams have to work together towards these goals.
*  So engineering of data and obviously clusters and large scale is very important. And then
*  one that is often not, maybe nowadays it is more clear, is benchmark progress. So we're talking
*  here about multiple months of tens of researchers and people that are trying to organize the research
*  and so on, working together. And you don't know that you can get there. This is the beauty. If
*  you're not risking trying to do something that feels impossible, you're not going to get there,
*  but you need the way to measure progress. So the benchmarks that you build are critical.
*  I've seen this beautifully pay out in many projects. Maybe the one I've seen it more
*  consistently, which means we established the metric, actually the community did, and then we
*  leverage that massively as an alpha fold. This is a project where the data, the metrics were all there
*  and all it took was, and it's easier said than done, an amazing team working not to try to find
*  some incremental improvement and publish, which is one way to do research that is valid, but
*  aim very high and work literally for years to iterate over that process. And working for years
*  with a team, I mean, it is tricky that also happened to happen partly during a pandemic and
*  so on. So I think my meta learning from all this is the teams are critical to the success.
*  And then if now going to the machine learning, the part that's surprising is,
*  so we like architectures like neural networks. And I would say this was a very rapidly evolving
*  field until the transformer came. So attention might indeed be all you need, which is the title,
*  also a good title, although in hindsight is good. I don't think at the time I thought this is a great
*  title for a paper, but that architecture is proving that the dream of modeling sequences of any bytes
*  there is something there that will stick. And I think these advance in architectures,
*  in kind of how neural networks are architecture to do what they do. It's been hard to find one
*  that has been so stable and relatively has changed very little since it was invented five or so years
*  ago. So that is a surprising, is a surprise that keeps recurring into other projects.
*  Try to, on a philosophical or technical level, introspect what is the magic of attention?
*  What is attention? That's attention in people that study cognition, so human attention. I think
*  there's giant wars over what attention means, how it works in the human mind. So there's very simple
*  looks at what attention is in your own network from the days of attention is all you need. But
*  do you think there's a general principle that's really powerful here?
*  Yeah. So a distinction between transformers and LSTMs, which were what came before. And
*  there was a transitional period where you could use both. In fact, when we talked about AlphaStat,
*  we used transformers and LSTMs. So it was still the beginning of transformers. They were very
*  powerful, but LSTMs were still also very powerful sequence models. So the power of the transformer
*  is that it has built in what we call an inductive bias of attention that makes the model. When you
*  think of a sequence of integers, like we discussed this before, this is a sequence of words.
*  When you have to do very hard tasks over these words, this could be, we're going to translate
*  a whole paragraph or we're going to predict the next paragraph given 10 paragraphs before.
*  There's some loose intuition from how we do it as a human that is very nicely mimicked and
*  replicated, structurally speaking, in the transformer, which is this idea of
*  you're looking for something. So you just read a piece of text, now you're thinking what comes next.
*  You might want to re-look at the text or look at it from scratch. I mean,
*  literally, because there's no recurrence, you're just thinking what comes next.
*  It's almost hypothesis driven. So if I'm thinking the next word that I'll write is cat or dog,
*  the way the transformer works almost philosophically is it has these two hypotheses.
*  Is it going to be cat or is it going to be dog? Then it says, okay, if it's cat,
*  I'm going to look for certain words, not necessarily cat, although cat is an obvious word,
*  you would look in the past to see whether it makes more sense to output cat or dog.
*  Then it does some very deep computation over the words and beyond. So it combines the words,
*  but it has the query, as we call it, that is cat. Then similarly for dog. So it's a very
*  computational way to think about, look, if I'm thinking deeply about text, I need to go back to
*  look at all of the text, attend over it, but it's not just attention. What is guiding the attention,
*  and that was the key insight from an earlier paper, is not how far away is it. I mean,
*  how far away is it is important. What did I just write about? That's critical, but what you wrote
*  about 10 pages ago might also be critical. So you're looking not positionally, but content wise,
*  right? Transformers have this beautiful way to query for certain content and pull it out
*  in a compressed way so then you can make a more informed decision. I mean, that's one way to
*  explain Transformers, but I think it's a very powerful inductive bias. There might be some
*  details that might change over time, but I think that is what makes Transformers so much more
*  powerful than the recurrent networks that were more recency bias based, which obviously works
*  in some tasks, but it has major flaws. Transformer itself has flaws, and I think the main one,
*  the main challenge is these prompts that we just were talking about, they can be a thousand words
*  long. But if I'm teaching you Starcraft, I mean, I'll have to show you videos, I'll have to point
*  you to whole Wikipedia articles about the game, we'll have to interact probably as you play,
*  you'll ask me questions. The context required for us to achieve me being a good teacher to you on
*  the game as you would want to do it with a model, I think goes well beyond the current capabilities.
*  So the question is, how do we benchmark this and then how do we change the structure of
*  the architectures? I think there's ideas on both sides, but we'll have to see empirically,
*  obviously what ends up working. And as you talked about, some of the ideas could be keeping the
*  constraint of that length in place, but then forming hierarchical representations to where
*  you can start being much clever in how you use those thousand tokens.
*  Yeah, that's really interesting, but it also is possible that this attentional mechanism where
*  you basically, you don't have a recency bias, but you look more generally, you make it learnable,
*  the mechanism in which way you look back into the past, you make that learnable. It's also possible
*  where at the very beginning of that, because that you might become smarter and smarter in the way
*  you query the past. So recent past and distant past and maybe very, very distant past. So
*  almost like the attention mechanism will have to improve and evolve as good as the
*  tokenization mechanism, so you can represent long-term memory somehow.
*  Yes. And hierarchies are very, I mean, it's a very nice word that sounds appealing. There's
*  lots of work adding hierarchy to the memories. In practice, it does seem like we keep coming back to
*  the main formula or main architecture. That sometimes tells us something. There's such a
*  sentence that a friend of mine told me, whether it wants to work or not. So Transformer was clearly
*  an idea that wanted to work. And then I think there's some principles we believe will be needed,
*  but finding the exact details, details matter so much, that's going to be tricky.
*  I love the idea that there's like you as a human being, you want some ideas to work. And then
*  there's the model that wants some ideas to work. And you get to have a conversation to see what,
*  more likely the model will win in the end. Because it's the one you don't have to do any work.
*  The model is the one that has to do the work. So you should listen to the model. And I really love
*  this idea that you talked about the humans in this picture. If I could just briefly ask,
*  one is you're saying the benchmarks about the modular humans working on this.
*  The benchmarks providing a sturdy ground of a wish to do these things that seem impossible.
*  They give you, in the darkest of times, give you hope. Because little signs of improvement.
*  Somehow you're not lost if you have metrics to measure your improvement. And then there's
*  other aspect you said elsewhere and here today, like titles matter. I wonder
*  how much humans matter in the evolution of all this, meaning individual humans.
*  Something about their interaction, something about their ideas, how much they
*  change the direction of all of this. If you change the humans in this picture,
*  is it that the model is sitting there and it wants some idea to work? Or maybe the model is
*  providing you 20 ideas that could work. And depending on the humans you pick, they're going
*  to be able to hear some of those ideas. Because you're now directing all of deep learning at Deep
*  Mind, you get to interact with a lot of projects, a lot of brilliant researchers.
*  How much variability is created by the humans in all of this?
*  Yeah, I do believe humans matter a lot, at the very least at the timescale of years
*  on when things are happening and what's the sequencing of it. So you get to interact with
*  people that, you mentioned this, some people really want some idea to work and they'll persist.
*  And then some other people might be more practical, like I don't care
*  what idea works. I care about cracking protein folding. And these, at least these two kind of
*  seem opposite sides. We need both. And we've clearly had both historically and that made
*  certain things happen earlier or later. So definitely humans involved in all of this endeavor
*  these endeavour have had, I would say, years of change or of ordering how things have happened,
*  which breakthroughs came before which other breakthroughs and so on. So certainly that
*  does happen. And so one other maybe one other axis of distinction is what I called and this is most
*  commonly used in reinforcement learning is the exploration exploitation trade-off as well. It's
*  not exactly what I meant, although quite related. So when you start trying to help others, right?
*  You become a bit more of a mentor to a large group of people, be it a project or the deep learning
*  team or something, or even in the community when you interact with people in conferences and so on,
*  you're identifying quickly some things that are explorative or exploitative and
*  tempting to try to guide people. Obviously, I mean, that's what makes our experience. We bring it and
*  we try to shape things sometimes wrongly. And there's many times that I've been wrong in the past.
*  That's great. But it would be wrong to dismiss any sort of of the research styles that I'm observing.
*  And I often get asked, well, you're in industry, right? So we do have access to large compute
*  scale and so on. So there's certain kinds of research. I almost feel like we need to do
*  responsibly and so on. But it is kind of we have the particle accelerator here, so to speak,
*  in physics. So we need to use it. We need to answer the questions that we should be answering
*  right now for the scientific progress. But then at the same time, I look at many advances,
*  including attention, which was discovered in Montreal initially because of lack of
*  compute. So we were working on sequence to sequence with my friends over at Google
*  Brain at the time. And we were using, I think, eight GPUs, which was somehow a lot at the time.
*  And then I think Montreal was a bit more limited in the scale. But then they discovered this
*  content-based attention concept that then has obviously triggered things like Transformer.
*  Not everything obviously starts with Transformer. There's always a history that is important to
*  recognize because then you can make sure that then those who might feel now, well, we don't
*  have so much compute, you need to then help them optimize that kind of research that might actually
*  produce amazing change. Perhaps it's not as short term as some of these advancements or perhaps it's
*  a different time scale. But the people and the diversity of the field is quite critical
*  that we maintain it. And at times, especially mixed a bit with hype or other things, it's a
*  bit tricky to be observing maybe too much of the same thinking across the board. But the humans
*  definitely are critical. And I can think of quite a few personal examples where also someone told
*  me something that had a huge effect onto some idea. And then that's why I'm saying at least
*  in terms of years, probably some things do happen.
*  Yeah, it's fascinating. It's also fascinating how constraints somehow are essential for innovation.
*  And the other thing you mentioned about engineering, I have a sneaking suspicion. Maybe
*  I over, you know, my love is with engineering. So I have a sneaking suspicion that all the genius,
*  large percentage of the genius is in the tiny details of engineering. So like I think
*  we like to think our genius, the genius is in the big ideas.
*  I have a sneaking suspicion that like, because I've seen the genius of details, of engineering
*  details make the night and day difference. And I wonder if those kind of have a ripple effect over
*  time. So that too, so that's sort of taking the engineering perspective that sometimes that quiet
*  innovation at the level of an individual engineer, or maybe at the small scale of a few engineers
*  can make all the difference that scales because we're doing, we're working on computers that are
*  scaled across large groups, that one engineering decision can lead to ripple effects.
*  Yes.
*  Which is interesting to think about.
*  Yeah, I mean, engineering, there's also kind of a historical, it might be a bit random,
*  because if you think of the history of how, especially deep learning and neural networks
*  took off, it feels like a bit random because GPUs happened to be there at the right time
*  for a different purpose, which was to play video games. So even the engineering that goes into the
*  hardware, and it might have a time, like the timeframe might be very different. I mean,
*  these, the GPUs were evolved throughout many years where we didn't even, we're looking at that,
*  so even at that level, that revolution, so to speak, the ripples are like,
*  we'll see when they stop. But in terms of thinking of why is this happening,
*  I think that when I try to categorize it in sort of things that might not be so obvious,
*  clearly there's a hardware revolution, we are surfing thanks to that. Data centers as well,
*  data centers are where, like, I mean, at Google, for instance, obviously they're serving Google,
*  but there's also now thanks to that and to have built such amazing data centers, we can train
*  these models. Software is an important one. I think if I look at the state of how I had to
*  implement things to implement my ideas, how I discarded ideas because they were too hard
*  to implement, yeah, clearly the times have changed and thankfully we are in a much better software
*  position as well. And then, I mean, obviously there's research that happens at scale and more
*  people enter the field. That's great to see, but it's almost enabled by these other things.
*  And last but not least is also data, right? Curating datasets, labeling datasets, these
*  benchmarks we think about, maybe we'll want to have all the benchmarks in one system, but it's
*  still very valuable that someone put the thought and the time and the vision to build certain
*  benchmarks we've seen progress thanks to, but we're going to repurpose the benchmarks.
*  That's the beauty of Atari is like we solved it in a way, but we use it in GATO. It was critical
*  and I'm sure there's still a lot more to do thanks to that amazing benchmark that someone
*  took the time to put, even though at the time maybe, oh, you have to think what's the next
*  iteration of architectures. That's what maybe the field recognizes, but we need to,
*  that's another thing we need to balance in terms of a human's behind. We need to recognize all
*  these aspects because they're all critical and we tend to think of the genius, the scientist,
*  and so on. But I'm glad you're, I know you have a strong engineering background.
*  So, but also I'm a lover of data and it gives a pushback on the engineering comment.
*  Ultimately could be the creatives of benchmarks who have the most impact.
*  Andre Capati, who you mentioned, has recently been talking a lot of trash about ImageNet,
*  which he has the right to do because of how critical he is about how essential he is to the
*  development and the success of deep learning around ImageNet. And you're saying that that's
*  actually that benchmark is holding back the field because I mean, especially in his context on Tesla
*  autopilot, that's looking at real world behavior of a system. It's, there's something fundamentally
*  missing about ImageNet that doesn't capture the real worldness of things that we need to have
*  data sets, benchmarks that have the unpredictability, the edge cases, the whatever the
*  heck it is that makes the real world so difficult to operate in. We need to have benchmarks with
*  that. So, but just to think about the impact of ImageNet as a benchmark and that really puts a
*  lot of emphasis on the importance of a benchmark, both sort of internally a deep mind and as a
*  community. So one is coming in from within like, how do I create a benchmark for me to mark and
*  make progress? And how do I make benchmark for the community to mark and push progress? You have this
*  amazing paper you co-authored, a survey paper called Emergent Abilities of Large Language Models.
*  It has again, the philosophy here that I'd love to ask you about.
*  What's the intuition about the phenomena of emergence in neural networks, transformers,
*  language models? Is there a magic threshold beyond which we start to see certain performance?
*  And is that different from task to task? Is that us humans just being poetic and romantic? Or is
*  there literally some level of which we start to see breakthrough performance? Yeah, I mean, this
*  is a property that we start seeing in systems that actually tend to be... So in machine learning,
*  traditionally, again, going to benchmarks, I mean, if you have some input-outputs, right, like that
*  is just a single input and a single output, you generally, when you train these systems, you see
*  reasonably smooth curves when you analyze how much the data set size affects the performance,
*  or how the model size affects the performance, or how long you train the system for affects the
*  performance, right? So, if we think of ImageNet, the training curves look fairly smooth and
*  predictable in a way. And I would say that's probably because of the... It's kind of a one
*  hop reasoning task, right? It's like, here is an input, and you think for a few milliseconds or
*  100 milliseconds, 300 as a human, and then you tell me, yeah, there's an alpaca in this image.
*  So, in language, we are seeing benchmarks that require more pondering and more thought in a way,
*  right? This is just kind of you need to look for some subtleties that it involves inputs that you
*  might think of, or even if the input is a sentence describing a mathematical problem,
*  there is a bit more processing required as a human and more introspection.
*  So, I think how these benchmarks work means that there is actually a threshold. Just going back to
*  how transformers work in this way of querying for the right questions to get the right answers,
*  that might mean that performance becomes random until the right question is asked by the querying
*  system of a transformer or of a language model like a transformer. And then, only then, you might
*  start seeing performance going from random to non-random. And this is more empirical. There's
*  no formalism or theory behind this yet, although it might be quite important. But we're seeing these
*  phase transitions of random performance until some, let's say, scale of a model, and then it goes
*  beyond that. And it might be that you need to fit a few low-order bits of thought before you can
*  make progress on the whole task. And if you could measure, actually, those breakdown of the task,
*  maybe you would see more smooth, like, yeah, once you get these and these and these and these and
*  these, then you start making progress in the task. But it's somehow a bit annoying because then
*  it means that certain questions we might ask about architectures possibly can only be done
*  at certain scale. And one thing that conversely I've seen great progress on in the last couple
*  years is this notion of science of deep learning and science of scale in particular. So,
*  on the negative is that there's some benchmarks for which progress might need to be measured at
*  minimum and at certain scale until you see then what details of the model matter to make that
*  performance better. So, that's a bit of a con. But what we've also seen is that you can sort of
*  empirically analyze behavior of models at scales that are smaller. So, let's say, to put an example,
*  we had this Tintilla paper that revised the so-called scaling laws of models. And that whole
*  study is done at a reasonably small scale, that may be hundreds of millions up to 1 billion
*  parameters. And then the cool thing is that you create some loss, some trends. You extract
*  trends from data that you see, okay, it looks like the amount of data required to train now a 10x
*  larger model would be this. And these laws so far, these extrapolations have helped us save,
*  compute, and just get to a better place in terms of the science of how should we run these models
*  at scale, how much data, how much depth, and all sorts of questions we start asking extrapolating
*  from small scale. But then this emergence is sadly that not everything can be extrapolated
*  from scale, depending on the benchmark. And maybe the harder benchmarks are not so good for
*  extracting these laws. But we have a variety of benchmarks at least.
*  So I wonder to which degree the threshold, the phase shift scale is a function of the benchmark.
*  Some of the science of scale might be engineering benchmarks where that threshold is low. Sort of
*  taking a main benchmark and reducing it somehow, where the essential difficulty is left,
*  but the scale of which the emergence happens is lower, just for the science aspect of it versus
*  the actual real world aspect. Yeah. So luckily we have quite a few benchmarks,
*  some of which are simpler or maybe they're more like, I think people might call these
*  systems one versus systems two style. So I think what we're not seeing, luckily, is that
*  extrapolations from maybe slightly more smooth or simpler benchmarks are translating to the
*  harder ones. But that is not to say that this extrapolation will hit its limits. And when it
*  does, then how much we scale or how we scale will sadly be a bit suboptimal until we find better
*  laws. And these laws, again, are very empirical laws. They're not like physical laws of models,
*  although I wish there would be better theory about these things as well. But so far, I would say
*  empirical theory, as I call it, is way ahead than actual theory of machine learning.
*  Let me ask you almost for fun. So this is not, Oriel, as a DeepMind person or anything to do
*  with DeepMind or Google, just as a human being, and looking at these news of a Google engineer who
*  claimed that, I guess, the Lambda language model was sentient. And you still need to look into the
*  details of this, but sort of making an official report and a claim that he believes there's
*  evidence that this system has achieved sentience. And I think this is a really interesting case
*  on a human level, on a psychological level, on a technical machine learning level of how language
*  models transform our world, and also just philosophical level of the role of AI systems
*  in a human world. So what do you find interesting? What's your take on all of this?
*  As a machine learning engineer and a researcher and also as a human being?
*  Yeah, I mean, a few reactions. Quite a few, actually.
*  Have you ever briefly thought, is this thing sentient?
*  Right. So never. Absolutely never.
*  Even with like AlphaStar? Wait a minute.
*  Sadly, I think, yeah, sadly, I have not. Yeah, I think any of the current models, although
*  very useful and very good, yeah, I think we're quite far from that. And there's kind of a
*  converse side story. So one of my passions is about science in general. And I think I feel I'm a bit
*  of a failed scientist. That's why I came to machine learning, because you always feel,
*  and you start seeing this, that machine learning is maybe the science that can help other sciences,
*  as we've seen. It's such a powerful tool. So thanks to that angle, that, OK, I love science,
*  I love astronomy, I love biology, but I'm not an expert. And I decided, well, the thing I can
*  do better at is computers. But having, especially when I was a bit more involved in AlphaFold,
*  learning a bit about proteins and about biology and about life, the complexity,
*  it feels like it really is. I mean, if you start looking at the things that are going on
*  at the atomic level, and also, I mean, there's obviously that we are maybe inclined to try to
*  think of neural networks as like the brain, but the complexities and the amount of magic that it
*  feels when, I mean, I'm not an expert, so it naturally feels more magic. But looking at
*  biological systems, as opposed to these computer computational brains, just makes me like, wow,
*  there's such level of complexity difference still, right? Like orders of magnitude complexity that,
*  sure, these weights, I mean, we train them and they do nice things, but they're not at the level
*  of biological entities, brains, cells. It just feels like it's just not possible to achieve the
*  same level of complexity behavior. And my belief when I talk to other beings is certainly shaped
*  by this amazement of biology that maybe because I know too much, I don't have about machine learning,
*  but I certainly feel it's very far-fetched and far in the future to be calling or to be thinking,
*  well, this mathematical function that is differentiable is in fact sentient and so on.
*  There's something on that point that is very interesting. So you know enough
*  about machines and enough about biology to know that there's many orders of magnitude of
*  difference and complexity, but you know how machine learning works. So the interesting
*  question for human beings that are interacting with a system that don't know about the underlying
*  complexity, and I've seen people, probably including myself, that have fallen in love
*  with things that are quite simple. And so maybe the complexity is one part of the picture,
*  but maybe that's not a necessary condition for sentience, for perception
*  or emulation of sentience. Right. So I guess the other side of this is that's how I feel personally.
*  I mean, you asked me about the person, right? Now it's very interesting to see how other
*  humans feel about things. Again, I'm not as amazed about things that I feel this is not as magical
*  as this other thing because of maybe how I got to learn about it and how I see the curve a bit more
*  smooth because I've just seen the progress of language models since Shannon in the 50s and
*  actually looking at that time scale, we're not that fast progress, right? I mean, what we were
*  thinking at the time, like almost 100 years ago, is not that dissimilar to what we're doing now.
*  But at the same time, yeah, obviously others, my experience, right, the personal experience,
*  I think no one should tell others how they should feel. I mean, the feelings are very personal,
*  right? So how others might feel about the models and so on. That's one part of the story that is
*  important to understand for me personally as a researcher. And then when I maybe disagree or I
*  don't understand or see that, yeah, maybe this is not something I think right now is reasonable,
*  knowing all that I know, one of the other things and perhaps partly why it's great to be talking
*  to you and reaching out to the world about machine learning is, hey, let's demystify a bit the magic
*  and try to see a bit more of the math and the fact that literally to create these models,
*  if we had the right software, it would be 10 lines of code and then just a dump of the internet.
*  So versus like then the complexity of like the creation of humans from their inception, right?
*  And also the complexity of evolution of the whole universe to where we are, that feels orders of
*  magnitude more complex and fascinating to me. So I think, yeah, maybe part of the only thing I'm
*  thinking about trying to tell you is, yeah, I think explaining a bit of the magic, there is a bit of
*  magic. It's good to be in love obviously with what you do at work. And I'm certainly fascinated and
*  surprised quite often as well. But I think hopefully as experts in biology, hopefully will tell me this
*  is not as magic. And I'm happy to learn that through interactions with the larger community,
*  we can also have a certain level of education that in practice also will matter because I mean,
*  one question is how you feel about this, but then the other very important is you starting to interact
*  with these in products and so on. It's good to understand a bit what's going on, what's not going
*  on, what's safe, what's not safe and so on, right? Otherwise the technology will not be used properly
*  for good, which is obviously the goal of all of us, I hope.
*  So let me then ask the next question. Do you think in order to solve intelligence
*  or to replace the leg spot that does interviews, as we started this conversation with, do you think
*  the system needs to be sentient? Do you think it needs to achieve something like consciousness?
*  And do you think about what consciousness is in the human mind that could be instructive for
*  creating AI systems? Yeah, honestly, I think probably not to the degree of intelligence that
*  there's this brain that can learn, can be extremely useful, can challenge you, can teach you,
*  conversely, you can teach it to do things. I'm not sure it's necessary, personally speaking,
*  but if consciousness or any other biological or evolutionary lesson can be repurposed to
*  influence our next set of algorithms, that is a great way to actually make progress, right?
*  And the same way I tried to explain Transformers a bit how it feels we operate when we look at
*  text specifically, these insights are very important, right? So there's a distinction
*  between details of how the brain might be doing computation. I think my understanding is, sure,
*  there's neurons and there's some resemblance to neural networks, but we don't quite understand
*  enough of the brain in detail, right, to be able to replicate it. But then, if you zoom out a bit,
*  our thought process, how memory works, maybe even how evolution got us here, what's exploration,
*  exploitation, how these things happen, I think these clearly can inform algorithmic level
*  research. And I've seen some examples of this being quite useful to then guide the research,
*  even it might be for the wrong reasons, right? So I think biology and what we know about ourselves
*  can help a whole lot to build essentially what we call AGI, the real gato, right, the last step of
*  the chain, hopefully. But consciousness in particular, I don't myself at least think too
*  hard about how to add that to the system. But maybe my understanding is also very personal about what
*  it means, right? I think even that in itself is a long debate that I know people have often,
*  and maybe I should learn more about this. Yeah, and I personally, I notice the magic often
*  on a personal level, especially with physical systems like robots. I have a lot of
*  legged robots now in Austin that I play with. And even when you program them, when they do things
*  you didn't expect, there's an immediate anthropomorphization. And you notice the
*  magic and you start to think about things like sentience that has to do more with effective
*  communication and less with any of these kind of dramatic things. It seems like a useful part of
*  communication. Having the perception of consciousness seems like useful for us humans.
*  We treat each other more seriously. We are able to do a nearest neighbor shoving of that entity
*  into your memory correctly, all that kind of stuff. It seems useful, at least to fake it,
*  even if you never make it. So maybe like, yeah, mirroring the question. And since you talk to a
*  few people, then you do think that we'll need to figure something out in order to achieve
*  intelligence in a grander sense of the word. Yeah, I personally believe yes, but I don't even think
*  it'll be like a separate island we'll have to travel to. I think it will emerge quite naturally.
*  Okay. That's easier for us then. Thank you. But the reason I think it's important to think about is
*  you will start, I believe, like with this Google engineer, you will start seeing this a lot more,
*  especially when you have AI systems that are actually interacting with human beings that
*  don't have an engineering background. And we have to prepare for that because there'll be,
*  I do believe there'll be a civil rights movement for robots as silly as it is to say. There's going
*  to be a large number of people that realize there's these intelligent entities with whom I have
*  deep relationship and I don't want to lose them. They've come to be a part of my life. They mean a
*  lot. They have a name, they have a story, they have a memory. And we start to ask questions about
*  ourselves. Well, what this thing sure seems like it's capable of suffering because it tells all
*  these stories of suffering. It doesn't want to die and all those kinds of things. And we have to
*  start to ask ourselves questions. What is the difference between a human being and this thing?
*  So when you engineer, I believe from an engineering perspective, from a deep mind
*  or anybody that builds systems, there might be laws in the future where you're not allowed to
*  engineer systems with displays of sentience, unless they're explicitly designed to be that,
*  unless it's a pet. So if you have a system that's just doing customer support, you're legally not
*  allowed to display sentience. We'll start to ask ourselves that question. And then so that's going
*  to be part of the software engineering process. Which features do we have? And one of them is
*  communications of sentience. But it's important to start thinking about that stuff, especially
*  how much it captivates public attention. Yeah, absolutely. It's definitely a topic that
*  is important we think about. And I think in a way, I always see not every movie is equally
*  on point with certain things, but certainly science fiction in this sense,
*  at least has prepared society to start thinking about certain topics that even if it's too early
*  to talk about, as long as we are reasonable, it's certainly going to prepare us for both
*  the research to come and how to... I mean, there's many important challenges and
*  topics that come with building an intelligent system, many of which you just mentioned.
*  We're never going to be fully ready unless we talk about this and we start also, as I said,
*  just kind of expanding the people we talk to, to not include only our own researchers and so on.
*  And in fact, places like DeepMind, but elsewhere, there's more interdisciplinary groups forming up
*  to start asking and really working with us on these questions. Because obviously, this is not
*  initially what your passion is when you do your PhD, but certainly it is coming. So it's fascinating
*  it's the thing that brings me to one of my passions that is learning. So in this sense,
*  this is kind of a new area that as a learning system myself, I want to keep exploring.
*  And I think it's great to see parts of the debate and even I see a level of maturity in
*  the conferences that deal with AI. If you look five years ago to now, just the amount of workshops
*  and so on has changed so much. It's impressive to see how much topics of safety, ethics and so on
*  come to the surface, which is great. And if we were too early, clearly it's fine. I mean,
*  it's a big field and there's lots of people with lots of interest that will do progress or make
*  progress. And obviously, I don't believe we're too late. So in that sense, I think it's great
*  that we're doing this already. It's better to be too early than too late when it comes to
*  superintelligent AI systems. Let me ask, speaking of sentient AIs, you gave props to your friend,
*  Ilias Eskever, for being elected the fellow of the Royal Society. So just as a shout out to a
*  fellow researcher and a friend, what's the secret to the genius of Ilias Eskever? And also, do you
*  believe that his tweets, as you've hypothesized and Andre Kapotty did as well, are generated by
*  a language model? Yeah. So I strongly believe Ilias is going to visit in a few weeks, actually. So
*  I'll ask him in person. Will he tell you the truth? Yes, of course. Ultimately, we all have
*  shared paths and there's friendships that go beyond obviously institutions and so on. So
*  hope he tells me the truth. Well, maybe the AI system is holding him hostage somehow. Maybe he
*  has some videos that he doesn't want to release. So maybe it has taken control over him. So he can't
*  tell the truth. Well, if I see him in person, then he will know. But I think Ilias' personality,
*  just knowing him for a while, everyone in Twitter, I guess, gets a different persona. And I think
*  Ilias one does not surprise me. So I think knowing Ilias from before social media and before AI was
*  so prevalent, I recognize a lot of his character. So that's something for me that I feel good about
*  a friend that hasn't changed or is still true to himself. Obviously, there is, though, a fact that
*  your field becomes more popular and he is obviously one of the main figures in the field,
*  having done a lot of advancement. So I think that the tricky bit here is how to balance
*  your true self with the responsibility that you're worse carrying. So in this sense, I think,
*  yeah, I appreciate the style and I understand it, but it created debates on some of his tweets,
*  right? That maybe it's good we have them early anyways, right? But yeah, then the reactions are
*  usually polarizing. I think we're just seeing kind of the reality of social media a bit there as
*  well, reflected on that particular topic or set of topics he's tweeting about.
*  Yeah, I mean, it's funny that he used to speak to this tension. He was one of the early
*  seminal figures in the field of deep learning. And so there's a responsibility with that. But
*  he's also, from having interacted with him quite a bit, he's just a brilliant thinker about ideas.
*  And which, as are you, and that there's a tension between becoming the manager versus
*  the actual thinking through very novel ideas. The, yeah, the scientist versus the manager.
*  And he's one of the great scientists of our time. This was quite interesting. And also,
*  people tell me quite silly, which I haven't quite detected yet, but in private, we'll have to see
*  about that. Yeah. Yeah. I mean, just on the point of, I mean, Ilya has been an inspiration.
*  I mean, quite a few colleagues, I can think, shaped the person you are. Ilya certainly
*  gets probably the top spot, if not close to the top. And if we go back to the question about
*  people in the field, like how the role would have changed the field or not, I think Ilya's case is
*  interesting because he really has a deep belief in the scaling up of neural networks. There was a
*  talk that is still famous to this day from the Sequence to Sequence paper where he was just
*  claiming, just give me supervised data and a large neural network and then you'll solve basically all
*  the problems. That vision was already there many years ago. So it's good to see someone who is,
*  in this case, very deeply into this style of research and clearly has had a tremendous
*  track record of successes and so on. The funny bit about that talk is that we rehearsed the talk
*  in a hotel room before and the original version of that talk would have been even more controversial.
*  So maybe I'm the only person that has seen the unfiltered version of the talk. And maybe when
*  the time comes, maybe we should revisit some of the skip slides from the talk from Ilya. But I
*  really think the deep belief into some certain style of research pays out. It's good to be
*  practical sometimes and I actually think Ilya and myself are practical, but it's also good.
*  There's some sort of long-term belief and trajectory. Obviously, there's a bit of
*  lacking both, but it might be that that's the right path. Then you clearly are ahead and hugely
*  influential to the field, as he has been. Do you agree with that intuition that maybe was
*  written about by Rich Sutton in The Bitter Lesson, that the biggest lesson that can be
*  read from 70 years of AI research is that general methods that leverage computation are ultimately
*  the most effective? Do you think that intuition is ultimately correct? General methods that
*  leverage computation, allowing the scaling of computation to do a lot of the work.
*  The basic task of us humans is to design methods that are more and more general
*  versus more and more specific to the tasks at hand.
*  I certainly think this essentially mimics a bit of the deep learning research,
*  almost like philosophy, that on the one hand, we want to be data agnostic. We don't want to
*  pre-process datasets. We want to see the bytes, the true data as it is, and then learn everything
*  on top. I very much agree with that. I think scaling up feels, at the very least, again,
*  necessary for building incredible complex systems. It's possibly not sufficient,
*  barring that we need a couple of breakthroughs. I think Rich Sutton mentioned search being part
*  of the equation of scale and search. I think search, I've seen it, that's been more mixed in
*  my experience. From that lesson in particular, search is a bit more tricky because it is very
*  appealing to search in domains like Go, where you have a clear reward function that you can then
*  discard some search traces. But then in some other tasks, it's not very clear how you would do that.
*  Although recently, one of our recent works, which actually was mostly mimicking or a continuation,
*  and even the team and the people involved were pretty much very intersecting with AlphaStar,
*  was AlphaCode, in which we actually saw the bitter lesson how scale of the models and then
*  a massive amount of search yielded this very interesting result of being able to have human
*  level code competition. I've seen examples of it being literally mapped to search and scale.
*  I'm not so convinced about the search bit, but certainly I'm convinced scale will be needed.
*  We need general methods. We need to test them and maybe we need to make sure that we can scale them
*  given the hardware that we have in practice. But then maybe we should also shape how the
*  hardware looks like based on which methods might be needed to scale. That's an interesting
*  contrast of this GPU comment that is we got it for free almost because games were using this. But
*  maybe now if sparsity is required, we don't have the hardware. Although in theory,
*  many people are building different kinds of hardware these days, but there's a bit of this
*  notion of hardware lottery for scale that might actually have an impact at least on the year,
*  again, scale of years on how fast we'll make progress to maybe a version of neural nets or
*  whatever comes next that might enable truly intelligent agents.
*  Do you think in your lifetime we will build an AGI system that would undeniably be a thing
*  that achieves human level intelligence and goes far beyond?
*  I definitely think it's possible that it will go far beyond, but I'm definitely convinced that
*  it will be human level intelligence. I'm hypothesizing about the beyond because
*  the beyond bit is a bit tricky to define, especially when we look at the current
*  formula of starting from this imitation learning standpoint. We can certainly imitate
*  humans at language and beyond. Getting at human level through imitation feels very possible.
*  Going beyond will require reinforcement learning and other things. I think in some areas
*  that certainly already has paid out. Go being an example that's my favorite so far in terms of
*  going beyond human capabilities. But in general, I'm not sure we can define reward functions
*  that from a seat of imitating human level intelligence that is general and then going
*  beyond. That bit is not so clear in my lifetime, but certainly human level, yes. That in itself is
*  already quite powerful. Going beyond, we're not going to not try that if then we get to
*  superhuman scientists and discovery and advancing the world. But at least human level
*  in general is also very, very powerful. Especially if human level or slightly beyond is
*  integrated deeply with human society and there's billions of agents like that,
*  do you think there's a singularity moment beyond which our world will be just very deeply transformed
*  by these kinds of systems? Because now you're talking about intelligence systems that are
*  just, I mean, this is no longer just going from horse and buggy to the car. It feels like a very
*  different kind of shift in what it means to be a living entity on earth. Are you afraid? Are you
*  excited of this world? I'm afraid if there's a lot more. I think maybe we'll need to think about
*  if we truly get there, just thinking of limited resources like humanity clearly hits some limits
*  and then there's some balance hopefully that biologically the planet is imposing and we should
*  actually try to get better at this. As we know, there's quite a few issues with having too many
*  people coexisting in a resource limited way. So for digital entities, it's an interesting question.
*  I think such a limit maybe should exist, but maybe it's going to be imposed by energy
*  availability because this also consumes energy. In fact, most systems are more inefficient than
*  we are in terms of energy required. But definitely, I think as a society, we'll need to
*  just work together to find what would be reasonable in terms of growth or how we
*  coexist if that is to happen. I am very excited about obviously the aspects of automation that
*  make people that obviously don't have access to certain resources or knowledge
*  for them to have that access. I think those are the applications in a way that I'm most exciting
*  to see and to personally work towards. Yeah, there's going to be significant
*  improvements in productivity and the quality of life across the whole population,
*  which is very interesting. But I'm looking even far beyond us becoming a multi-planetary species.
*  Just as a quick last question, do you think as humans become multi-planetary species,
*  go outside our solar system, all that kind of stuff, do you think there will be more humans
*  or more robots in that future world? Will humans be the quirky intelligent being of the past?
*  Or is there something deeply fundamental to human intelligence that's truly special,
*  where we will be part of those other planets, not just AI systems?
*  I think we're all excited to build AGI to empower or make us more powerful as human species. Not to
*  say there might be some hybridization. I mean, this is obviously speculation, but there are
*  companies also trying to, the same way medicine is making us better. Maybe there are other things
*  that are yet to happen on that. But if the ratio is not at most one-to-one, I would not be happy.
*  So I would hope that we are part of the equation, but maybe a one-to-one ratio feels like possible,
*  constructive and so on. But it would not be good to have a
*  misbalance, at least from my core beliefs and the why I'm doing what I'm doing when I go to work and
*  I research what I research. Well, this is how I know you're human, and this is how you've passed
*  the Turing test. And you are one of the special humans, Oriol. It's a huge honor that you would
*  talk with me, and I hope we get the chance to speak again, maybe once before the singularity,
*  once after, and see how our view of the world changes. Thank you again for talking today.
*  Thank you for the amazing work you do. You're a shining example of a research and a human being
*  in this community. Thanks a lot, Lex. Yeah. Looking forward to before the singularity, certainly.
*  And maybe after. Thanks for listening to this conversation with Oriol Vinales. To support this
*  podcast, please check out our sponsors in the description. And now let me leave you with some
*  words from Alan Turing. Those who can imagine anything can create the impossible. Thank you
*  for listening and hope to see you next time.
