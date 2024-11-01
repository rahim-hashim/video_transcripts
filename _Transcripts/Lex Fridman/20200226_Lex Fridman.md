---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5995s
Video Keywords: ['marcus hutter', 'aixi', 'agi', 'Schmidhuber', 'deepmind', 'artificial intelligence', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 102581
Video Rating: None
Video Description: Marcus Hutter is a senior research scientist at DeepMind and professor at Australian National University. Throughout his career of research, including with Jürgen Schmidhuber and Shane Legg, he has proposed a lot of interesting ideas in and around the field of artificial general intelligence, including the development of the AIXI model which is a mathematical approach to AGI that incorporates ideas of Kolmogorov complexity, Solomonoff induction, and reinforcement learning.

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

EPISODE LINKS:
Hutter Prize: http://prize.hutter1.net
Marcus web: http://www.hutter1.net
Books mentioned:
- Universal AI: https://amzn.to/2waIAuw
- AI: A Modern Approach: https://amzn.to/3camxnY
- Reinforcement Learning: https://amzn.to/2PoANj9
- Theory of Knowledge: https://amzn.to/3a6Vp7x

OUTLINE:
0:00 - Introduction
3:32 - Universe as a computer
5:48 - Occam's razor
9:26 - Solomonoff induction
15:05 - Kolmogorov complexity
20:06 - Cellular automata
26:03 - What is intelligence?
35:26 - AIXI - Universal Artificial Intelligence
1:05:24 - Where do rewards come from?
1:12:14 - Reward function for human existence
1:13:32 - Bounded rationality
1:16:07 - Approximation in AIXI
1:18:01 - Godel machines
1:21:51 - Consciousness
1:27:15 - AGI community
1:32:36 - Book recommendations
1:36:07 - Two moments to relive (past and future)

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Marcus Hutter Universal Artificial Intelligence, AIXI, and AGI  Lex Fridman Podcast #75
**Lex Fridman:** [February 26, 2020](https://www.youtube.com/watch?v=E1AxVXt2Gv4)
*  The following is a conversation with Marcus Hutter, Senior Research Scientist at Google DeepMind.
*  Throughout his career of research, including with Jürgen Schmidt Huber and Shane Legge,
*  he has proposed a lot of interesting ideas in and around the field of artificial general intelligence,
*  including the development of IXI, spelled A-I-X-I, model, which is a mathematical approach to AGI
*  that incorporates ideas of Kolmogorov complexity, Solomonov induction, and reinforcement learning.
*  In 2006, Marcus launched the 50,000 euro Hutter prize for lossless compression of human knowledge.
*  The idea behind this prize is that the ability to compress well is closely related to intelligence.
*  This, to me, is a profound idea. Specifically, if you can compress the first 100 megabytes
*  or one gigabyte of Wikipedia better than your predecessors, your compressor likely has to also
*  be smarter. The intention of this prize is to encourage the development of intelligent
*  compressors as a path to AGI. In conjunction with his podcast release just a few days ago,
*  Marcus announced a 10x increase in several aspects of this prize, including the money,
*  to 500,000 euros. The better your compressor works relative to the previous winners,
*  the higher fraction of that prize money is awarded to you. You can learn more about it
*  if you google simply Hutter prize. I'm a big fan of benchmarks for developing AI systems,
*  and the Hutter prize may indeed be one that will spark some good ideas for approaches
*  that will make progress on the path of developing AGI systems.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  give it five stars on Apple Podcasts, support it on Patreon, or simply connect with me on Twitter
*  at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do one or two minutes of ads now,
*  and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by CashApp, the number one finance app in the App Store. When you get it,
*  use code LEXPODCAST. CashApp lets you send money to friends, buy bitcoin, and invest in the stock
*  market with as little as one dollar. Broker services are provided by CashApp Investing,
*  a subsidiary of Square, and member SIPC. Since CashApp allows you to send and receive
*  money digitally, peer-to-peer, and security in all digital transactions is very important,
*  let me mention the PCI Data Security Standard that CashApp is compliant with. I'm a big fan
*  of standards for safety and security. PCI DSS is a good example of that, where a bunch of
*  competitors got together and agreed that there needs to be a global standard around the security
*  of transactions. Now, we just need to do the same for autonomous vehicles and AI systems in general.
*  So again, if you get CashApp from the App Store or Google Play and use the code LEXPODCAST,
*  you'll get $10 and CashApp will also donate $10 to FIRST, one of my favorite organizations that
*  is helping to advance robotics and STEM education for young people around the world.
*  And now, here's my conversation with Marcus Hodder.
*  Do you think of the universe as a computer or maybe an information processing system?
*  Let's go with a big question first. Okay, with a big question first. I think it's a very interesting
*  hypothesis or idea. And I have a background in physics, so I know a little bit about
*  physical theories, the Standard Model of Particle Physics and General Relativity Theory,
*  and they are amazing and describe virtually everything in the universe. And they're all,
*  in a sense, computable theories. I mean, they're very hard to compute. And it's very elegant,
*  simple theories which describe virtually everything in the universe. So there's a strong
*  indication that somehow the universe is computable, but it's a plausible hypothesis.
*  So what do you think, just like you said, general relativity, quantum field theory,
*  what do you think that the laws of physics are so nice and beautiful and simple and compressible?
*  Do you think our universe was designed naturally this way? Are we just focusing on the parts that
*  are especially compressible? Are human minds just enjoy something about that simplicity? And
*  in fact, there's other things that are not so compressible.
*  No, I strongly believe and I'm pretty convinced that the universe is inherently
*  beautiful, elegant, and simple and described by these equations. And we're not just picking that.
*  I mean, if there were some phenomena which cannot be neatly described,
*  scientists would try that. And there's biology which is more messy, but we understand that it's
*  an emergent phenomena and it's complex systems, but they still follow the same rules of quantum
*  electrodynamics. All of chemistry follows that and we know that. I mean, we cannot compute
*  everything because we have limited computational resources. No, I think it's not a bias of the
*  humans, but it's objectively simple. I mean, of course, you never know. Maybe there's some
*  corners very far out in the universe or super, super tiny below the nucleus of atoms or,
*  well, parallel universes which are not nice and simple, but there's no evidence for that.
*  And we should apply Occam's razor and choose the simplest tree consistent with it. But also,
*  it's a little bit self-referential. So maybe a quick pause. What is Occam's razor?
*  So Occam's razor says that you should not multiply entities beyond necessity,
*  which sort of if you translate that into proper English means, and in the scientific context means
*  that if you have two theories or hypotheses or models which equally well describe the phenomenon,
*  your study or the data, you should choose the more simple one.
*  So that's just the principle?
*  Yes.
*  Sort of that's not like a provable law, perhaps. Perhaps we'll kind of discuss it and think about
*  it, but what's the intuition of why the simpler answer is the one that is likelier to be more
*  correct descriptor of whatever we're talking about?
*  I believe that Occam's razor is probably the most important principle in science. I mean,
*  of course, we lead logical deduction and we do experimental design, but science is about understanding
*  the world, finding models of the world. And we can come up with crazy complex models,
*  which explain everything but predict nothing. But the simple model seem to have predictive power,
*  and it's a valid question why. And there are two answers to that. You can just accept it. That is
*  the principle of science, and we use this principle and it seems to be successful.
*  We don't know why, but it just happens to be. Or you can try, you know, find another principle
*  which explains Occam's razor. And if we start with the assumption that the world is governed
*  by simple rules, then there's a bias towards simplicity. And applying Occam's razor
*  is the mechanism to finding these rules. And actually in a more quantitative sense,
*  and we come back to that later in case of somnolent deduction, you can rigorously prove that.
*  If you assume that the world is simple, then Occam's razor is the best you can do in a certain sense.
*  So I apologize for the romanticized question, but why do you think, outside of its effectiveness,
*  why do you think we find simplicity so appealing as human beings? Why does E equals MC squared
*  seem so beautiful to us humans? I guess mostly in general, many things can be explained
*  by an evolutionary argument. And you know, there's some artifacts in humans, which, you know,
*  are just artifacts and not evolutionary necessary. But with this beauty and simplicity, it's,
*  I believe, at least the core is about, like science, finding regularities in the world,
*  understanding the world, which is necessary for survival, right? You know, if I look
*  at a bush, right, and I just see noise, and there is a tiger, right, and eats me, then I'm dead.
*  But if I try to find a pattern, and we know that humans are prone to
*  find more patterns in data than they are, you know, like the Mars face and all these things,
*  but this bias towards finding patterns, even if they are none, but I mean, it's best, of course,
*  if they are, yeah, helps us for survival. Yeah, that's fascinating. I haven't thought
*  really about the, I thought I just loved science, but indeed from in terms of just
*  for survival purposes, there is an evolutionary argument for why we find the work of Einstein so
*  beautiful. Maybe a quick small tangent, could you describe what Solomonov induction is?
*  Yeah, so that's a theory, which I claim, and Mr. Solomonov sort of claimed a long time ago,
*  that this solves the big philosophical problem of the human race. And I think that's the
*  big philosophical problem of induction, and I believe the claim is essentially true.
*  And what it does is the following. So, okay, for the picky listener, induction can be interpreted
*  narrowly and widely. Narrow means inferring models from data, and widely means also then
*  using these models for doing predictions, so prediction is also part of the induction. So I'm
*  a little sloppy sort of with the terminology, and maybe that comes from
*  Ray Solomonov, you know, being sloppy, maybe I should say that. He can't complain anymore.
*  So let me explain a little bit this theory in simple terms. So assume we have a data sequence,
*  make it very simple, the simplest one, say one, one, one, one, one, and you see 100 ones.
*  What do you think comes next? The natural answer, I must speed up a little bit, the natural answer
*  is of course, you know, one. Okay. And the question is why? Okay. Well, we see a pattern there.
*  Yeah, okay, there's a one and we repeat it. And why should it suddenly after 100 ones be different?
*  So what we're looking for is simple explanations or models for the data we have. And now the
*  question is, a model has to be presented in a certain language. In which language do we use?
*  In science, we want formal languages, and we can use mathematics, or we can use
*  programs on a computer. So abstractly on a Turing machine, for instance, or it can be a general
*  purpose computer. So, and there are of course, lots of models of you can say maybe it's 100 ones and
*  then 100 zeros and 100 ones, that's a model, right? But they're simpler models. There's a model print
*  one loop. Now that also explains the data. And if you push it to the extreme, you are looking for
*  the shortest program, which if you run this program reproduces the data you have, it will
*  not stop, it will continue naturally. And this you take for your prediction. And on the sequence
*  of ones, it's very plausible, right? That print one loop is the shortest program. We can give some
*  more complex examples like one, two, three, four, five. What comes next? The short program is again,
*  you know, counter. And so that is roughly speaking how solenoid induction works.
*  The extra twist is that it can also deal with noisy data. So if you have, for instance, a coin
*  flip, say a biased coin, which comes up head with 60% probability, then it will predict,
*  it will learn and figure this out. And after a while it predicts, oh, the next coin flip will
*  be head with probability 60%. So it's the stochastic version of that. But the goal is, the dream is,
*  always the search for the short program. Yes. Yeah. Well, in solenoid induction, precisely what you do
*  is, so you combine, so looking for the shortest program is like applying OpExRazor, like looking
*  for the simplest theory. There's also Epicorus principle, which says, if you have multiple
*  hypotheses, which equally well describe your data, don't discard any of them. Keep all of them around,
*  you never know. And you can put that together and say, okay, I have a bias towards simplicity,
*  but it don't rule out the larger models. And technically what we do is we weigh the shorter
*  models higher and the longer models lower. And you use a Bayesian techniques, you have a prior
*  and which is precisely two to the minus the complexity of the program. And you weigh all
*  this hypothesis and take this mixture and then you get also this stochasticity in.
*  Yeah. Like many of your ideas, that's just a beautiful idea of weighing based on the simplicity
*  of the program. I love that. That seems to me, maybe very human-centric concept, seems to be a
*  very appealing way of discovering good programs in this world. You've used the term compression
*  quite a bit. I think it's a beautiful idea. Sort of, we just talked about simplicity and maybe
*  science or just all of our intellectual pursuits is basically the attempt to compress the complexity
*  all around us into something simple. So what does this word mean to you, compression?
*  I essentially have already explained it. So compression means for me, finding short programs
*  for the data or the phenomenon at hand. You could interpret it more widely as finding simple
*  theories, which can be mathematical theories or maybe even informal, just in words.
*  Compression means finding short descriptions, explanations, programs for the data.
*  Do you see science as a kind of our human attempt at compression? So we're speaking more generally
*  because when you say programs, you're kind of zooming in on a particular sort of almost like
*  a computer science, artificial intelligence focus. But do you see all of human endeavor as a kind of
*  compression? Well, at least all of science I see as an endeavor of compression, not all of
*  humanity maybe. And well, there are also some other aspects of science like experimental design.
*  Right? I mean, we create experiments specifically to get extra knowledge and this isn't part of the
*  decision-making process. But once we have the data to understand the data is essentially compression.
*  So I don't see any difference between compression, understanding and prediction.
*  So we're jumping around topics a little bit, but returning back to simplicity,
*  a fascinating concept of Kolmogorov complexity. So in your sense, do most objects in our mathematical
*  universe have high Kolmogorov complexity? And maybe what is, first of all, what is Kolmogorov
*  complexity? Okay, Kolmogorov complexity is a notion of simplicity or complexity. And
*  it takes the compression view to the extreme. So I explained before that if you have some data
*  sequence, just think about a file in a computer and best sort of, you know, just a string of bits.
*  And if you, and we have data compresses, like we compress big files into zip files with certain
*  compressors. And you can also produce self-extracting RKRFs. That means as an executable,
*  if you run it, it reproduces your original file without needing an extra decompressor. It's just a
*  decompressor plus the RKRF together in one. And now there are better and worse compressors. And
*  you can ask what is the ultimate compressor? So what is the shortest possible self-extracting
*  RKRF you could produce for a certain data set, yeah, which reproduces the data set. And the length
*  of this is called the Kolmogorov complexity. And arguably, that is the information content
*  in the data set. I mean, if the data set is very redundant or very boring, you can compress it very
*  well. So the information content should be low. And you know, it is low according to this definition.
*  So it's the length of the shortest program that summarizes the data.
*  Yes. Yeah.
*  And what's your sense of our sort of universe when we think about the different
*  objects in our universe that we try, concepts or whatever, at every level, do they have higher or
*  low Kolmogorov complexity? So what's the hope? Do we have a lot of hope in being able to summarize
*  much of our world? That's a tricky and difficult question. So
*  as I said before, I believe that the whole universe based on the evidence we have is very
*  simple. So it has a very short description. So to linger on that, the whole universe,
*  what does that mean? Do you mean at the very basic fundamental level in order to create the universe?
*  Yes. Yeah. So you need a very short program and you run it.
*  To get the thing going.
*  To get the thing going and then it will reproduce our universe. There's a problem with noise. We
*  can come back to that later, possibly. Is noise a problem or is it a bugger feature?
*  I would say it makes our life as a scientist really, really much harder. I mean, think about
*  without noise, we wouldn't need all of the statistics. But then maybe we wouldn't feel
*  like there's a free will. Maybe we need that for the... This is an illusion that noise can
*  give you free will. At least in that way, it's a feature. But also if you don't have noise,
*  you have chaotic phenomena which are effectively like noise. So we can't get away with statistics
*  even then. I mean, think about rolling a dice and forget about quantum mechanics and you know
*  exactly how you throw it. But I mean, it's still so hard to compute the trajectory that effectively
*  it is best to model it as coming out with a number, this probability one over six.
*  But from this set of philosophical, Kolmogorov complexity perspective, if we didn't have noise,
*  then arguably you could describe the whole universe as standard model plus generativity.
*  I mean, we don't have a theory of everything yet, but sort of assuming we are close to it or have
*  it here, plus the initial conditions, which may hopefully be simple. And then you just run it and
*  then you would reproduce the universe. But that's all by noise or by chaotic phenomena.
*  So now if we don't take the whole universe, we'll just a subset, just take planet Earth.
*  Planet Earth cannot be compressed into a couple of equations. This is a hugely complex system.
*  So interesting. So when you look at the window, like the whole thing might be simple, but when
*  you just take a small window, then it may become complex. And that may be counter-intuitive.
*  So you can't just take a whole universe and then you can take a whole universe and then
*  take a small window. Then it may become complex. And that may be counter-intuitive.
*  But there's a very nice analogy. The library of all books. So imagine you have a normal library
*  with interesting books and you go there. Great. Lots of information and quite complex. So now I
*  create a library which contains all possible books, say of 500 pages. So the first book just has AAAA
*  over all the pages. The next book AAAA and ends with B and so on. I create this library of all
*  books. I can write a super short program which creates this library. So this library which has
*  all books has zero information content. And you take a subset of this library and suddenly you
*  have a lot of information in there. So that's fascinating. I think one of the most beautiful
*  object, mathematical objects that at least today seems to be understudied or under talked about is
*  cellular automata. What lessons do you draw from the game of life for cellular automata
*  where you start with the simple rules just like you're describing with the universe and somehow
*  complexity emerges? Do you feel like you have an intuitive grasp on the fascinating behavior of
*  such systems where some, like you said, some chaotic behavior could happen, some complexity
*  could emerge, some it could die out and some very rigid structures? Do you have a sense about
*  cellular automata that somehow transfers maybe to the bigger questions of our universe?
*  Yeah, the cellular automata and especially the Conway's game of life is really great because
*  this rule is so simple. You can explain it to every child and even by hand you can simulate a
*  little bit and you see these beautiful patterns emerge and people have proven that it's even
*  Turing complete. You cannot just use a computer to simulate game of life, but you can also use game
*  of life to simulate any computer. That is truly amazing. And it's the prime example probably to
*  demonstrate that very simple rules can lead to very rich phenomena. And people sometimes,
*  how is chemistry and biology so rich? I mean, this can't be based on simple rules. But no,
*  we know quantum electrodynamics describes all of chemistry and we come later back to that. I claim
*  intelligence can be explained or described in one single equation, this very rich phenomenon.
*  You asked also about whether I understand this phenomenon and it's probably not.
*  And there's this saying, you never understand really things, you just get used to them.
*  And I think I'm pretty used to cellular automata. So you believe that you understand now why this
*  phenomenon happens. But I give you a different example. I didn't play too much this Conway's
*  game of life, but a little bit more with fractals and with the Mandelbrot set and these beautiful
*  patterns just look Mandelbrot set. And well, when the computers were really slow and I just had a
*  black and white monitor and programmed my own programs in Assembler too.
*  Assembler, wow. Wow, you're legit.
*  To get these fractals on the screen and it was mesmerized and much later. So I returned to this
*  every couple of years and then I tried to understand what is going on. And you can understand
*  a little bit. So I tried to derive the locations, they are these circles and the apple shape.
*  And then you have smaller Mandelbrot sets recursively in this set. And there's a way
*  to mathematically by solving high order polynomials to figure out where these
*  centers are and what size they are approximately. And by sort of mathematically approaching this
*  problem, you slowly get a feeling of why things are like they are. And that sort of isn't, you know,
*  the first step to understanding why this rich phenomena.
*  Do you think it's possible? What's your intuition? Do you think it's possible to reverse engineer
*  and find the short program that generated these fractals by looking at the fractals?
*  Well, in principle, yes. So, I mean, in principle, what you can do is you take any data set,
*  you take these fractals or you take whatever your data set, whatever you have,
*  say a picture of Conway's Game of Life, and you run through all programs. You take a program size
*  one, two, three, four, and all these programs, run them all in parallel in so-called dovetailing
*  fashion. Give them computational resources, first one 50%, second one half resources and so on,
*  and let them run. Wait until they hold, give an output, compare it to your data. And if some of
*  these programs produce the correct data, then you stop and then you have already some program.
*  It may be a long program because it's faster. And then you continue and you get shorter and
*  shorter programs until you eventually find the shortest program. The interesting thing,
*  you can never know whether it's the shortest program because there could be an even shorter
*  program, which is just even slower. And you just have to wait here, but asymptotically,
*  and actually after finite time, you have the shortest program. So this is a theoretical,
*  so this is a theoretical but completely impractical way of finding the underlying
*  structure in every data set. And that is what Solomov induction does and Kolmogorov complexity.
*  In practice, of course, we have to approach the problem more intelligently. And then
*  if you take resource limitations into account, there's once the field of pseudo random numbers,
*  and these are random numbers. So these are deterministic sequences, but no algorithm,
*  which is fast, fast means runs in polynomial time, can detect that it's actually deterministic.
*  So we can produce interesting, I mean, random numbers may be not that interesting,
*  but just an example. We can produce complex looking data and we can then
*  prove that no fast algorithm can detect the underlying pattern.
*  Which is unfortunately, that's a big challenge for our search for simple programs in the space
*  of artificial intelligence, perhaps. Yes, it definitely is for artificial
*  intelligence. And it's quite surprising that it's, I can't say easy, I mean, physicists worked really
*  hard to find these theories, but apparently it was possible for human minds to find these simple rules
*  in the universe. It could have been different, right? But it's not that easy.
*  It's all inspiring. So let me ask another absurdly big question. What is intelligence in your view?
*  So I have, of course, a definition. I wasn't sure what you're going to say,
*  because you could have just as easily said, I have no clue.
*  Which many people would say, but I'm not modest in this question.
*  So the informal version, which I worked out together with Shane Lack, who co-founded DeepMind,
*  is that intelligence measures an agent's ability to perform well in a wide range of environments.
*  So that doesn't sound very impressive. And these words have been very carefully chosen.
*  And there is a mathematical theory behind that. And we come back to that later. And if you look at
*  this definition by itself, it seems like, yeah, okay. But it seems a lot of things are missing.
*  But if you think it through, then you realize that most, and I claim all of the other traits,
*  at least of rational intelligence, which we usually associate with intelligence,
*  are emergent phenomena from this definition. Like, you know, creativity, memorization,
*  planning, knowledge. You all need that in order to perform well in a wide range of environments.
*  So you don't have to explicitly mention that in a definition.
*  Interesting. So yeah, so the consciousness, abstract reasoning, all these kinds of things
*  are just emergent phenomena that help you in towards, can you say the definition again?
*  Multiple environments. Did you mention the word goals?
*  No, but we have an alternative definition. Instead of performing well, you can just replace it by
*  goal. So intelligence measures an agent's ability to achieve goals in a wide range of environments.
*  That's more or less equal.
*  But it's interesting because in there, there's an injection of the word goals.
*  So we want to specify there should be a goal.
*  Yeah, but perform well is sort of what does it mean? It's the same problem.
*  Yeah. There's a little bit gray area, but it's much closer to something that could be
*  formalized. In your view, are humans, where do humans fit into that definition? Are they
*  general intelligence systems that are able to perform in, like how good are they at
*  fulfilling that definition, at performing well in multiple environments?
*  Yeah, that's a big question. I mean, the humans are performing best among all
*  species on earth.
*  Species we know of.
*  Yeah.
*  Depends. You could say that trees and plants are doing a better job. They'll probably outlast us.
*  Yeah, but they are in a much more narrow environment, right? I mean, you just have
*  a little bit of air pollution and these trees die, and we can adapt, right? We build houses,
*  we build filters, we do geoengineering.
*  So the multiple environment part.
*  Yeah, that is very important. So that distinguishes narrow intelligence from
*  wide intelligence, also in the AI research.
*  So let me ask the Alan Turing question. Can machines think? Can machines be intelligent?
*  So in your view, I have to kind of ask. The answer is probably yes, but I want to
*  kind of hear your thoughts on it. Can machines be made to fulfill this definition of intelligence,
*  to achieve intelligence?
*  Well, we are sort of getting there, and on a small scale, we are already there.
*  The wide range of environments are still missing, but we have self-driving cars, we have programs
*  which play Go and chess, we have speech recognition. So that's pretty amazing, but
*  you can, you know, these are narrow environments. But if you look at AlphaZero, that was also
*  developed by DeepMind. I mean, got famous with AlphaGo and then came AlphaZero a year later.
*  That was truly amazing. So reinforcement learning algorithm, which is able just by self-play
*  to play chess and then also Go. And I mean, yes, they're both games, but they're quite different
*  games. And you know, don't feed them the rules of the game. And the most remarkable thing,
*  which is still a mystery to me, that usually for any decent chess program, I don't know much about
*  Go, you need opening books and end game tables and so on, and nothing was put in there.
*  Especially with AlphaZero, the self-play mechanism was so good,
*  especially with AlphaZero, the self-play mechanism starting from scratch, being able to learn
*  actually new strategies is incredible.
*  Yeah, it's really discovered, you know, all these famous openings within four hours
*  by itself. What I was really happy about, I'm a terrible chess player, but I like Queen Gumby,
*  and AlphaZero figured out that this is the best opening.
*  Finally, somebody proved you correct.
*  So yes, to answer your question, yes, I believe that general intelligence is possible.
*  And it also depends how you define it. Do you say AGI, with general intelligence,
*  artificial intelligence, only refers to if you achieve human level or is sub-human level, but
*  quite broad, is it also general intelligence? So we have to distinguish or it's only super
*  human intelligence, general artificial intelligence.
*  Is there a test in your mind, like the Turing test in natural language or some other test
*  that would impress the heck out of you, that would kind of cross the line of
*  your sense of intelligence within the framework that you said?
*  Well, the Turing test has been criticized a lot, but I think it's not as bad as some people
*  think. And some people think it's too strong. So it tests not just for a system to be intelligent,
*  but it also has to fake human deception, which is much harder. And on the other hand,
*  they say it's too weak because it just maybe fakes emotions or intelligent behavior. It's not real.
*  But I don't think that's the problem or a big problem. So if you would pass the Turing test,
*  so a conversation over terminal with a bot for an hour or maybe a day or so, and you can fool a
*  human into not knowing whether this is a human or not, so that's the Turing test. I would be truly
*  impressed. And we have this annual competitions, the Lübner prize. And I mean, it started with
*  ELISA, that was the first conversational program. And what is it called? The Japanese Mitsuko or
*  so. That's the winner of the last couple of years. It's quite impressive.
*  Yeah, it's quite impressive. And then Google has developed Mina, right? Just recently. That's an
*  open domain conversational bot, just a couple of weeks ago, I think.
*  Yeah. I kind of like the metric that sort of the Alexa prize has proposed. I mean, maybe it's
*  obvious to you. It wasn't to me of setting sort of a length of a conversation. Like you want the bot
*  to be sufficiently interesting that you'd want to keep talking to it for like 20 minutes. And
*  that's a surprisingly effective in aggregate metric because you really like nobody has the patience
*  to be able to talk to a bot that's not interesting and intelligent and witty and is able to go on
*  the different tangents, jump domains, be able to say something interesting to maintain your attention.
*  Maybe many humans will also fail this test. Unfortunately, we set just like with autonomous
*  vehicles, with chat bots, we also set a bar that's way too high to reach.
*  I said the Turing test is not as bad as some people believe. But what is really
*  not useful about the Turing test, it gives us no guidance how to develop these systems in the first
*  place. Of course, we can develop them by trial and error and do whatever and then run the test
*  and see whether it works or not. But a mathematical definition of intelligence gives us
*  an objective which we can then analyze by theoretical tools or computational and maybe
*  even prove how close we are. And we will come back to that later with the ICSI model.
*  I mentioned the compression, right? So in natural language processing,
*  they achieved amazing results. And one way to test this, of course, you take the system,
*  you train it, and then you see how well it performs on the task. But a lot of performance
*  measurement is done by so-called perplexity, which is essentially the same as
*  complexity or compression length. So the NLP community develops new systems and then they
*  measure the compression length and then they have ranking and leaks because there's a strong
*  correlation between compressing well and then the systems performing well at the task at hand.
*  It's not perfect, but it's good enough for them as an intermediate aim.
*  So you mean a measure, so this is kind of almost returning to the Kolmogorov complexity. So you're
*  saying good compression usually means good intelligence. Yes.
*  So you mentioned you're one of the only people who dared boldly to try to formalize
*  the idea of artificial general intelligence, to have a mathematical framework for intelligence,
*  just like as we mentioned, termed ICSI, A-I-X-I. So let me ask the basic question. What is ICSI?
*  Okay. So let me first say what it stands for because...
*  What it stands for, actually, that's probably the more basic question.
*  Yeah. The first question is usually how it's pronounced, but finally I put it on the website
*  how it's pronounced, so you figured it out. The name comes from AI, artificial intelligence,
*  and the X-I is the Greek letter Xi, which are used for Solomanov's distribution for
*  for quite stupid reasons, which I'm not willing to repeat here in front of camera.
*  So it just happened to be more or less arbitrary, I chose Xi, but it also has nice other
*  interpretations. So there are actions and perceptions in this model, right? An agent
*  has actions and perceptions over time. So this is A-index I, X-index I, so there's an action at time
*  I and then followed by perception at time I. We'll go with that. I'll edit out the first part.
*  Yeah. I'm just kidding. I have some more interpretations. So at some point, maybe
*  five years ago or 10 years ago, I discovered in Barcelona, it was in a big church, there was
*  a stone engraved, some text, and the word ICSI appeared there a couple of times.
*  I was very surprised and happy about it, and I looked it up. So it is a Catalan language,
*  and it means with some interpretation, that's it, that's the right thing to do. Yeah, heurica.
*  Oh, so it's almost like destined somehow came to you in a dream.
*  And similar, there's a Chinese word, ICSI, also written like ICSI, if you transcribe that to
*  pinyin. And the final one is that it's AI crossed with induction, because that's going more to the
*  content now. So good old fashioned AI is more about planning and known the ternistic world,
*  and induction is more about often your IID data and inferring models. And essentially what this
*  ICSI model does is combining these two. And I actually also recently I think heard that in
*  Japanese AI means love. So if you can combine XI somehow with that, I think there might be some
*  interesting ideas there. So ICSI, let's then take the next step. Can you maybe talk at the big level
*  of what is this mathematical framework? Yeah, so it consists essentially of two parts.
*  One is the learning and induction and prediction part, and the other one is the planning part.
*  So let's come first to the learning induction prediction part, which essentially I explained
*  already before. So what we need for any agent to act well is that it can somehow predict what
*  happens. I mean, if you have no idea what your actions do, how can you decide which actions are
*  good or not? So you need to have some model of what your actions effect. So what you do is you
*  have some experience, you build models like scientists of your experience, then you hope
*  these models are roughly correct, and then you use these models for prediction. And the model is,
*  sorry to interrupt, and the model is based on your perception of the world,
*  how your actions will affect that world. That's not the important part. It is technically important,
*  but at this stage, we can just think about predicting, say, stock market data, whether data
*  or IQ sequences, one, two, three, four, five, what comes next. So of course, our actions
*  affect what we're doing, but I'll come back to that in a second.
*  So, and I'll keep just interrupting. So just to draw a line between prediction and planning,
*  what do you mean by prediction in this way? It's trying to predict the environment without your
*  long-term action in that environment. What is prediction?
*  Okay. If you want to put the actions in now, okay, then let's put in now.
*  Yeah. We don't have to put them now. Scratch it. Dumb question. Okay.
*  So the simplest form of prediction is that you just have data which you passively observe,
*  and you want to predict what happens without interfering. As I said, weather forecasting,
*  stock market, IQ sequences, or just anything. Okay. And Solomons theory of induction based
*  on compression. So you look for the shortest program, which describes your data sequence,
*  and then you take this program, run it, which reproduces your data sequence by definition,
*  and then you let it continue running, and then it will produce some predictions. And you can
*  rigorously prove that for any prediction task, this is essentially the best possible predictor.
*  Of course, if there's a prediction task or a task which is unpredictable, like fair coin flips,
*  yeah, I cannot predict the next fair coin flip. What Solomonov does is says, okay, next head is
*  probably 50%. It's the best you can do. So if something is unpredictable, Solomonov will also
*  not magically predict it. But if there is some pattern and predictability, then Solomonov
*  induction will figure that out eventually, and not just eventually, but rather quickly, and you can
*  have proof convergence rates, whatever your data is. So there's pure magic in a sense.
*  What's the catch? Well, the catch is that it's not computable, and we come back to that later.
*  You cannot just implement it, even with Google resources here, and run it, and predict the stock
*  market and become rich. I mean, Ray Solomonov already tried that at the time.
*  But the basic task is you're in the environment, and you're interacting with an environment to try
*  to learn a model of that environment. And the model is in the space of all these programs.
*  And your goal is to get a bunch of programs that are simple.
*  Let's go to the actions now. But actually, good that you asked. Usually I skip this part,
*  although there is also a minor contribution, which I did. So the action part, but they usually sort
*  of just jump to the decision part. So let me explain the action part now. Thanks for asking.
*  So you have to modify it a little bit by now not just predicting a sequence which just comes to you,
*  but you have an observation, then you act somehow. And then you want to predict the next observation
*  based on the past observation and your action. Then you take the next action. You don't care
*  about predicting it because you're doing it. And then you get the next observation. And you want,
*  well, before you get it, you want to predict it again based on your past action and observation
*  sequence. You just condition extra on your actions. There's an interesting alternative
*  that you also try to predict your own actions. If you want.
*  In the past or the future?
*  In your future actions.
*  That's interesting. Wait, let me wrap. I think my brain is broke.
*  We should maybe discuss that later after I've explained the IxC model. That's an interesting
*  variation.
*  But that is a really interesting variation. And a quick comment. I don't know if you want
*  to insert that in here, but you're looking at that in terms of observations, you're looking
*  at the entire big history, the long history of the observations.
*  Exactly. That's very important. The whole history from birth of the agent. And we can
*  come back to that also why this is important. Often in RL, you have MDPs,
*  macro decision processes, which are much more limiting. Okay. So now we can predict
*  conditioned on actions. So even if we influence environment, but prediction is
*  not all we want to do. We also want to act really in the world. And the question is how
*  to choose the actions. And we don't want to greedily choose the actions.
*  Just what is best in the next time step. And first I should say, how do we measure
*  performance? So we measure performance by giving the agent reward. That's the so-called
*  reinforcement learning framework. So every time step, you can give it a positive reward
*  or negative reward, or maybe no reward. It could be very scarce. Like if you play chess,
*  just at the end of the game, you give plus one for winning or minus one for losing.
*  So in the IXC framework, that's completely sufficient. So occasionally you give a reward
*  signal and you ask the agent to maximize reward, but not greedily sort of the next one,
*  next one, because that's very bad in the long run if you're greedy. But over the lifetime of
*  the agent. So let's assume the agent lives for M time step, or dies in sort of a hundred years,
*  sharp. That's just the simplest model to explain. So it looks at the future reward sum and ask,
*  what is my action sequence? Or actually more precisely my policy, which leads in expectation,
*  because I don't know the world, to the maximum reward sum. Let me give you an analogy. In chess,
*  for instance, we know how to play optimally in theory. It's just a mini max strategy. I play
*  the move, which seems best to me under the assumption that the opponent plays the move,
*  which is best for him. So worst for me under the assumption that I play again, the best move.
*  And then you have this expecting max three to the end of the game. And then you back propagate,
*  and then you get the best possible move. So that is the optimal strategy, which for Norman
*  already figured out a long time ago for playing adversarial games. Luckily, or maybe unluckily
*  for the theory, it becomes harder. The world is not always adversarial. So it can be,
*  if the other humans even cooperative, or nature is usually, I mean, the dead nature is stochastic.
*  Things just happen randomly or don't care about you. So what you have to take into account is the
*  noise and not necessarily adversariality. So you replace the minimum on the opponent's side
*  by an expectation, which is general enough to include also adversarial cases. So now instead
*  of a mini max strategy, you have an expected max strategy. So far so good. So that is well known.
*  It's called sequential decision theory. But the question is on which probability distribution
*  do you base that? If I have the true probability distribution, like say I play Begum and right,
*  there's dice and there's certain randomness involved. Yeah. I can calculate probabilities
*  and feed it in the expect the max or the sequential decision tree, come up with the
*  optimal decision if I have enough compute. But in the, for the real world, we don't know that,
*  what is the probability the driver in front of me breaks? I don't know. So depends on all kinds
*  of things and especially new situations. I don't know. So this is this unknown thing
*  about prediction and there's where Solomanov comes in. So what you do is in sequential decision tree,
*  you just replace the true distribution, which we don't know by this universal distribution.
*  I didn't explicitly talk about it, but this is used for universal prediction and plug it into
*  the sequential decision tree mechanism. And then you get the best of both worlds.
*  You have a long-term planning agent, but it doesn't need to know anything about the world
*  because the Solomanov induction part learns. Can you explicitly try to describe the universal
*  distribution and how Solomanov induction plays a role here? I'm trying to understand.
*  So what it does it, so in the simplest case, I said, take the shortest program describing
*  your data, run it, have a prediction which would be deterministic. But you should not just take the
*  shortest program, but also consider the longer ones, but keep it lower a priori probability.
*  So in the Bayesian framework, you say a priori any distribution, which is a model or a stochastic
*  program has a certain a priori probability, which is two to the minus and why two to the minus
*  length of this program. So longer programs are punished a priori. And then you multiply it with
*  the so-called likelihood function, which is as the name suggests is how likely is this model given
*  the data at hand. So if you have a very wrong model, it's very unlikely that this model is true.
*  And so it is very small number. So even if the model is simple, it gets penalized by that.
*  And what you do is then you take just the sum, or this is the average over it.
*  And this gives you a probability distribution, so it's universal distribution of the Lomanov
*  distribution. So it's weighed by the simplicity of the program and likelihood. Yes. It's kind of
*  a nice idea. Yeah. So, okay. And then you said there's you're playing N or M or forgot the
*  letter steps into the future. So how difficult is that problem? What's involved there?
*  Is it a basic optimization problem? What are we talking about?
*  Yeah. So you have a planning problem up to horizon M and that's exponential time in the horizon M,
*  which is, I mean, it's computable, but intractable. I mean, even for chess,
*  it's already intractable to do that exactly. And for Go.
*  But it could be also discounted kind of framework where...
*  Yeah. So having a hard horizon at a hundred years is just for simplicity of discussing the model.
*  And also sometimes the math is simple. But there are lots of variations. It's actually
*  quite interesting parameter. There's nothing really problematic about it, but it's very
*  interesting. So for instance, you think, no, let's let the parameter M tend to infinity, right? You
*  want an agent which lives forever, right? If you do it naively, you have two problems. First,
*  the mathematics breaks down because you have an infinite reward sum, which may give infinity.
*  And getting reward 0.1 in the time step is infinity and giving reward one every time
*  step is infinity. So equally good. Not really what we want. Other problem is that if you have
*  an infinite life, you can be lazy for as long as you want for 10 years and then catch up with the
*  same expected reward. And think about yourself or maybe some friends or so. If they knew they lived
*  forever, why work hard now? Just enjoy your life and then catch up later. So that's another
*  problem with the infinite horizon. And you mentioned, yes, we can go to discounting.
*  But then the standard discounting is so-called geometric discounting. So a dollar today is about
*  worth as much as $1.05 tomorrow. So if you do this so-called geometric discounting, you have
*  introduced an effective horizon. So the agent is now motivated to look ahead a certain amount of
*  time effectively. It's like a moving horizon. And for any fixed effective horizon, there is
*  a problem to solve which requires larger horizons. So if I look ahead five time steps, I'm a terrible
*  chess player, right? I need to look ahead longer. If I play go, I probably have to look ahead even
*  longer. So for every horizon, there is a problem which this horizon cannot solve. But I introduced
*  the so-called near harmonic horizon, which goes down with one over T rather than exponentially T,
*  which produces an agent which effectively looks into the future proportional to each age. So if
*  it's five years old, it plans for five years. If it's 100 years old, it then plans for 100 years.
*  And it's a little bit similar to humans too, right? I mean, children don't plan ahead very long,
*  but then we get adult, we play ahead more longer. Maybe when we get very old, I mean,
*  we know that we don't live forever. Maybe then our horizon shrinks again.
*  So that's really interesting. So adjusting the horizon, is there some mathematical benefit of
*  or is it just a nice, I mean, intuitively, empirically, it would probably be a good
*  idea to sort of push the horizon back, extend the horizon as you experience more of the world. But
*  is there some mathematical conclusions here that are beneficial?
*  With solomonic reductions or prediction part, we have extremely strong finite time,
*  finite data results. So you have so-and-so much data, then you lose so-and-so much. So
*  the theory is really great. With the ICSI model with the planning part,
*  many results are only asymptotic, which, well, this is-
*  What does asymptotic mean?
*  Asymptotic means you can prove, for instance, that in the long run, if the agent
*  acts long enough, then it performs optimal or some nice thing happens. But you don't know how fast
*  it converges. So it may converge fast, but we're just not able to prove it because of difficult
*  problem. Or maybe there's a bug in the model so that it's really that slow. So that is what
*  asymptotic means sort of eventually, but we don't know how fast. And if I give the agent a fixed
*  horizon M, then I cannot prove asymptotic results. So if it dies in 100 years,
*  then in 100 years it's over. I cannot say eventually. So this is the advantage of the
*  discounting that I can prove asymptotic results. So just to clarify, so I've built up a model
*  with now in the moment, I have this way of looking several steps ahead. How do I pick
*  what action I will take? It's like with a playing chess, right? You do this minimax. In this case,
*  here do you expect the max based on the Solomonov distribution. You propagate back and then,
*  well, an action falls out. The action which maximizes the future expected reward on the
*  Solomonov distribution. And then you just take this action and then repeat. And then you get a
*  new observation and you feed it in this action observation. Then you repeat and the reward so on.
*  Yeah. So you rewrote too. Yeah. And then maybe you can even predict your own action.
*  I love that idea. But okay, this big framework, what is it? I mean, it's kind of a beautiful
*  mathematical framework to think about artificial general intelligence. What can you, what does it
*  help you into it about how to build such systems? Or maybe from another perspective,
*  what does it help us in understanding AGI? So when I started in the field, I was always interested
*  in two things. One was AGI. The name didn't exist then. It's called General AI or Strong AI.
*  And the physics theory of everything. So I switched back and forth between computer science
*  and physics quite often. You said the theory of everything. The theory of everything.
*  Yeah. There's basically two biggest problems before all of humanity.
*  Yeah. I can explain if you wanted some later time, why I'm interested in these two questions.
*  Can I ask you, in a small tangent, if one to be, it was one to be solved, which one would you,
*  if one, if you were, if an apple fell in your head and there was a brilliant insight and you could
*  arrive at the solution to one, would it be AGI or the theory of everything?
*  Definitely AGI because once the AGI problem is solved, they can ask the AGI to solve the other
*  problem for me. Yeah. Brilliant. Okay. So as you were saying about it.
*  Okay. So, and the reason why I didn't settle, I mean, this thought about, you know,
*  once you have solved AGI, it solves all kinds of other, not just the theory of every problem,
*  but all kinds of use, more useful problems to humanity is very appealing to many people. And,
*  you know, I had this thought also, but I was quite disappointed with the state of the art
*  of the field of AI. There was some theory, you know, about logical reasoning, but I was never
*  convinced that this will fly. And then there was this more holistic approaches with neural networks
*  and I didn't like these heuristics. So, and also I didn't have any good idea myself.
*  So that's the reason why I toggled back and forth quite some while and even worked for four and a
*  half years in a company developing software or something completely unrelated. But then I had
*  this idea about the ICSI model. And so what it gives you, it gives you a gold standard. So I have
*  proven that this is the most intelligent agents which anybody could build in quotation mark,
*  because it's just mathematical and you need infinite compute. But this is the limit. And
*  this is completely specified. It's not just a framework. Every year, tens of frameworks
*  are developed, which are just skeletons and then pieces are missing. And usually these missing
*  pieces turn out to be really, really difficult. And so this is completely and uniquely defined.
*  And we can analyze that mathematically. And we've also developed some approximations. I can
*  talk about that a little bit later. That would be sort of the top down approach, like
*  say for Neumann's mini max theory, that's the theoretical optimal play of games. And now we
*  need to approximate it, put heuristics in, prune the tree, blah, blah, blah, and so on. So we can
*  do that also with the ICSI model, but for general AI. It can also inspire those, and most of
*  most researchers go bottom up, right? They have their systems, they try to make it more general,
*  more intelligent. It can inspire in which direction to go. What do you mean by that?
*  So if you have some choice to make, right? So how should I evaluate my system if I can't do cross
*  validation? How should I do my learning if my standard regularization doesn't work well? Yeah.
*  So the answer is always this. We have a system which does everything that's ICSI. It's just
*  completely in the ivory tower, completely useless from a practical point of view.
*  But you can look at it and see, ah, yeah, maybe I can take some aspects. And instead of Kolmogorov
*  complexity, they'll just take some compressors, which has been developed so far. And for the
*  planning, well, we have UCT, which has also been used in Go. And at least it's inspired me a lot
*  to have this formal definition. And if you look at other fields, you know, like, I always come back
*  to physics because I have a physics background. Think about the phenomenon of energy. That was
*  long time a mysterious concept. And at some point it was completely formalized. And that really
*  helped a lot. And you can point out a lot of these things, which were first mysterious and wake,
*  and then they have been rigorously formalized. Speed and acceleration has been confused, right,
*  until it was formally defined. There was a time like this. And people often, you know,
*  don't have any background, still confuse it. And this ICSI model or the intelligence definitions,
*  which is sort of the dual to it, we come back to that later, formalizes the notion of intelligence
*  uniquely and rigorously. So in a sense, it serves as kind of the light at the end of the tunnel.
*  Yes, yeah.
*  I mean, there's a million questions I could ask her. So maybe kind of, okay, let's feel around
*  in the dark a little bit. So there's been here a deep mind, but in general, been a lot of breakthrough
*  ideas, just like we've been saying around reinforcement learning. So how do you see the
*  progress in reinforcement learning is different? Like, which subset of ICSI does it occupy?
*  The current, like you said, maybe the Markov assumption is made quite often in reinforcement
*  learning. There's other assumptions made in order to make the system work. What do you see as the
*  difference, connection between reinforcement learning and ICSI?
*  So the major difference is that essentially all other approaches, they make stronger assumptions.
*  So in reinforcement learning, the Markov assumption is that the next state or next
*  observation only depends on the previous observation and not the whole history,
*  which makes, of course, the mathematics much easier rather than dealing with histories.
*  Of course, they profit from it also because then you have algorithms that run on current computers
*  and do something practically useful. But for general AI, all the assumptions which are made
*  by other approaches, we know already now they are limiting. So for instance, usually you need
*  an agodicity assumption in the MDP frameworks in order to learn. Agodicity essentially means that
*  you can recover from your mistakes and that there are no traps in the environment. And if you make
*  this assumption, then essentially you can go back to a previous state, go there a couple of times
*  and then learn what statistics and what the state is like, and then in the long run perform well in
*  this state. But there are no fundamental problems. But in real life, we know there can be one single
*  action, one second of being inattentive while driving a car fast can ruin the rest of my life.
*  I can become quadriplegic or whatever. And there's no recovery anymore. So the real world is not
*  ergodic, I always say. There are traps and there are situations where you are not recovered from.
*  And very little theory has been developed for this case.
*  What do you see in the context of AICC as the role of exploration?
*  You mentioned in the real world we can get into trouble and we make the wrong decisions and really
*  pay for it. But exploration seems to be fundamentally important for learning about this
*  world, for gaining new knowledge. So is exploration baked in? Another way to ask it, what are the
*  parameters of AICC that can be controlled? Yeah, I say the good thing is that there are no
*  parameters to control. Some other people track knobs to control and you can do that. I mean,
*  you can modify AICC so that you have some knobs to play with if you want to. But the exploration
*  is directly baked in and that comes from the Bayesian learning and the long-term planning.
*  So these together already imply exploration. You can nicely and explicitly prove that
*  for simple problems like so-called bandit problems where you say, to give a real world example, say,
*  you have two medical treatments, A and B. You don't know the effectiveness. You try A a little bit,
*  B a little bit, but you don't want to harm too many patients. So you have to sort of
*  trade off exploring. And at some point you want to explore and you can do the mathematics and
*  figure out the optimal strategy. There are also non-Bayesian agents, but it shows that
*  this Bayesian framework by taking a prior over possible worlds, doing the Bayesian mixture,
*  then the Bayes optimal decision with long-term planning that is important, automatically
*  implies exploration also to the proper extent, not too much exploration and not too little.
*  In these very simple settings, in the ICSI model, I was also able to prove that it is
*  a self-optimizing theorem or asymptotic optimality theorems, although they're only asymptotic,
*  not finite time bounds. So it seems like the long-term planning is really important,
*  but the long-term part of the planning is really important. And also, maybe a quick tangent,
*  how important do you think is removing the Markov assumption and looking at the full history?
*  Sort of intuitively, of course it's important, but is it like fundamentally transformative to
*  the entirety of the problem? What's your sense of it? Like, cause we all, we make that assumption
*  quite often, just throwing away the past. I think it's absolutely crucial. The question is
*  whether there's a way to deal with it in a more holistic and still sufficiently well way. So
*  I have to come up with an example and fly, but you have some key event in your life,
*  a long time ago in some city or something, you realized that's a really dangerous street or
*  whatever, right? And you want to remember that forever, right? In case you come back there.
*  Kind of a selective kind of memory. So you remember all the important events in the past,
*  but somehow selecting the importance is- That's very hard. And I'm not concerned
*  about just storing the whole history. You can calculate human life, 30 or 100 years,
*  doesn't matter, right? How much data comes in through the vision system and the auditory system,
*  you compress it a little bit, in this case lossily and store it. We are soon in the means of just
*  storing it, but you still need to the selection for the planning part and the compression for
*  the understanding part. The raw storage I'm really not concerned about. And I think we should just
*  store, if you develop an agent, preferably just store all the interaction history. And then
*  you build, of course, models on top of it and you compress it and you are selective,
*  but occasionally you go back to the old data and reanalyze it based on your new experience you have.
*  Sometimes you are in school, you learn all these things you think is totally useless,
*  and much later you realize, oh, they were not as useless as you thought.
*  I'm looking at you, linear algebra. Right. So maybe let me ask about objective functions,
*  because that rewards, it seems to be an important part. The rewards are kind of given to the system.
*  For a lot of people, the specification of the objective function is a key part of intelligence.
*  The agent itself figuring out what is important. What do you think about that? Is it possible
*  within the IAC framework to yourself discover the reward based on which you should operate?
*  That will be a long answer. And that is a very interesting question. And I'm asked a lot about
*  this question. Where do the rewards come from? And that depends. I give you now a couple of answers.
*  If we want to build agents, now let's start simple. Let's assume we want to build an agent
*  based on the IAC model, which performs a particular task. Let's start with something super simple,
*  like playing chess or go or something. Then the reward is winning the game is plus one,
*  losing the game is minus one. Done. You apply this agent. If you have enough compute, you let it
*  self play, and it will learn the rules of the game. It will play perfect chess after some while.
*  Problem solved. If you have more complicated problems, then you may believe that you have
*  the right reward, but it's not. A nice cute example is elevator control. That is also in Rich Sutton's
*  book, which is a great book, by the way. You control the elevator and you think, well, maybe
*  the reward is not worth it. But you can also control the elevator. You can control the elevator
*  and you think, well, maybe the reward should be coupled to how long people wait in front of the
*  elevator. Long wait is bad. You program it and you do it. What happens is the elevator eagerly picks
*  up all the people, but never drops them off. Then you realize, maybe the time in the elevator also
*  counts, so you minimize the sum. The elevator does that, but never picks up the people in the
*  10th floor, in the top floor, because in expectation it's not worth it. Just let them stay.
*  Even in apparently simple problems, you can make mistakes. That's what in more serious
*  contexts, say, AGI safety researchers consider. Now let's go back to general agents. Assume we
*  want to build an agent which is generally useful to humans. We have a household robot,
*  and it should do all kinds of tasks. In this case, the human should give the reward on the fly.
*  Maybe it's pre-trained in the factory and there's some sort of internal reward for the battery level
*  or whatever. It does the dishes badly. You punish the robot, it does it good, you reward the robot,
*  and then train it to do a new task like a child. You need the human in the loop if you want a system
*  which is useful to the human. As long as this agent stays sub-human level,
*  that should work reasonably well, apart from these examples. It becomes critical if they become
*  on a human level. It's the same with children, small children. You have reasonably well under
*  control. They become older. The reward technique doesn't work so well anymore. Then finally,
*  so these would be agents which are just, you could say, slaves to the humans. If you are more
*  ambitious and just say we want to build a new species of intelligent beings, we put them on a
*  new planet and we want them to develop this planet or whatever. We don't give them any reward.
*  What could we do? You could try to come up with some reward functions like it should maintain
*  itself the robot, it should maybe multiply, build more robots, and maybe all kinds of things
*  which you find useful. But that's pretty hard. What does self-maintenance mean? What does it mean
*  to build a copy? Should it be exact copy, an approximate copy? That's really hard. But
*  Laurent Assort, also at DeepMind, developed a beautiful model. He just took the ICSI model
*  and coupled the rewards to information gain. He said the reward is proportional to how much the
*  agent had learned about the world. You can rigorously, formally, uniquely define that in
*  terms of our catalog versions. If you put that in, you get a completely autonomous agent.
*  Actually, interestingly, for this agent, we can prove much stronger result than for the general
*  agent, which is also nice. If you let this agent lose, it will be, in a sense, the optimal scientist.
*  It is absolutely curious to learn as much as possible about the world. Of course, it will also
*  have a lot of instrumental goals. In order to learn, it needs to at least survive. That agent
*  is not good for anything. It needs to have self-preservation. If it builds small helpers
*  acquiring more information, it will do that. If space exploration or whatever is necessary
*  to gathering information and develop it. It has a lot of instrumental goals following on
*  this information gain. This agent is completely autonomous of us. No rewards necessary anymore.
*  Of course, it could find a way to gain the concept of information and get stuck in that
*  library that you mentioned beforehand with a very large number of books.
*  The first agent had this problem. It would get stuck in front of an old TV screen,
*  which has just had white noise. The second version can deal with at least stochasticity.
*  What about curiosity? This kind of word, curiosity, creativity.
*  Is that kind of the reward function being of getting new information? Is that similar to
*  idea of kind of injecting exploration for its own sake inside the reward function? Do you find
*  this at all appealing, interesting? I think that's a nice definition. Curiosity
*  is a reward. Sorry, curiosity is exploration for its own sake. Yeah, I would accept that.
*  But most curiosity, well, in humans and especially in children, yeah, it's not just for its own sake,
*  but for actually learning about the environment and for behaving better. I think most curiosity
*  is tied in the end to what's performing better. Well, okay. So if intelligence systems
*  need to have this reward function, let me, you're an intelligence system,
*  currently passing the Turing test quite effectively. What's the reward function
*  of our human intelligence existence? What's the reward function that Marcus Hodder is operating
*  under? Okay, to the first question, the biological reward function is to survive and to spread,
*  and very few humans sort of are able to overcome this biological reward function.
*  But we live in a very nice world where we have lots of spare time and can still survive and
*  spread, so we can develop arbitrary other interests, which is quite interesting.
*  On top of that. On top of that, yeah. But the survival and spreading sort of is, I would say,
*  the goal or the reward function of humans, the core one.
*  I like how you avoided answering the second question, which a good intelligence system would.
*  So my- Your own meaning of life and the reward function.
*  My own meaning of life and reward function is to find an AGI to build it.
*  Beautiful. Okay. Let's dissect Ixie even further. So one of the assumptions is
*  kind of infinity keeps creeping up everywhere.
*  What are your thoughts on kind of bounded rationality and the nature of our existence
*  and intelligence systems is that we're operating always under constraints, under
*  you know, limited time, limited resources. How do you think about that within the Ixie framework
*  within trying to create an AGI system that operates under these constraints?
*  Yeah, that is one of the criticisms about Ixie that it ignores computation completely, and some
*  people believe that intelligence is inherently tied to what's bounded resources.
*  What do you think on this one point? Do you think the
*  boundaries of resources are fundamental to intelligence?
*  I would say that an intelligence notion, which ignores computational limits is extremely useful.
*  A good intelligence notion, which includes these resources would be even more useful,
*  but we don't have that yet. And so look at other fields outside of computer science.
*  Computational aspects never play a fundamental role. You develop biological models for cells,
*  something in physics, these theories, I mean, become more and more crazy and hard and harder
*  to compute. Well, in the end, of course, we need to do something with this model, but this more
*  nuisance than a feature. And I'm sometimes wondering if artificial intelligence would not
*  sit in a computer science department, but in a philosophy department, then this computational
*  focus would be probably significantly less. I mean, think about the induction problem is more
*  in the philosophy department. There's virtually no paper who cares about how long it takes to
*  compute the answer. That is completely secondary. Of course, once we have figured out the first
*  problem, so intelligence without computational resources, then the next very good question is,
*  could we improve it by including computational resources, but nobody was able to do that so
*  far, even halfway satisfactory manner? I like that. That in the long run,
*  the right department to belong to is philosophy. That's actually quite a deep idea, or even to,
*  at least to think about big picture philosophical questions, big picture questions, even in the
*  computer science department. But you've mentioned approximation. There's a lot of infinity, a lot of
*  huge resources needed. Are there approximations to Ixc that within the Ixc framework that are useful?
*  Yeah, we have developed a couple of approximations. And what we do there is that the
*  Solomov induction part, which was, you know, find the shortest program describing your data,
*  we just replace it by standard data compressors, right? And the better compressors get, you know,
*  the better this part will become. We focused on a particular compressor called Context Tree
*  Weighting, which is pretty amazing, not so well known. It has beautiful theoretical properties,
*  also works reasonably well in practice. So we used that for the approximation of the induction
*  and the learning and the prediction part. And for the planning part, we essentially just took the
*  ideas from a computer go from 2006. It was Jabba Sipespare, also now a DeepMind, who developed the
*  so-called UCT algorithm, Upper Confidence Bound for Trees algorithm on top of the Monte Carlo Tree
*  Search. So we approximate this planning part by sampling. And it's successful on some small toy
*  problems. We don't want to lose the generality, right? And that's sort of the handicap, right?
*  If you want to be general, you have to give up something. So but this single agent was able to
*  play, you know, small games like Coon Poker and Tic Tac Toe and even Pac-Man. And it's the same
*  architecture, no change. The agent doesn't know the rules of the game, really nothing, all by
*  player with these environments. So Jürgen Schmidhuber proposed something called Gertl machines,
*  which is a self-improving program that rewrites its own code. Sort of mathematically or
*  philosophically, what's the relationship in your eyes, if you're familiar with it, between AICS
*  and the Gertl machines? Yeah, familiar with it. He developed it while I was in his lab.
*  Yeah, so the Gertl machine, to explain briefly, you give it a task. It could be a simple task,
*  as you know, finding prime factors in numbers, right? You can formally write it down. There's
*  a very slow algorithm to do that. Just try all the factors, yeah. Or play chess, right? Optimally,
*  you write the algorithm to minimax to the end of the game. So you write down what the Gertl
*  machine should do. Then it will take part of its resources to run this program and other
*  part of the resources to improve this program. And when it finds an improved version, which
*  provably computes the same answer. So that's the key part, yeah. It needs to prove by itself
*  that this change of program still satisfies the original specification. And if it does so,
*  then it replaces the original program by the improved program. And by definition,
*  it does the same job, but just faster. Okay. And then, you know, it proves over it and over it.
*  And it's developed in a way that all parts of this Gertl machine can self-improve,
*  but it stays provably consistent with the original specification. So from this perspective,
*  it has nothing to do with ICCSI. But if you would now put ICCSI as the starting axioms in,
*  it would run ICCSI, but you know, that takes forever. But then if it finds a provable
*  speed up of ICCSI, it would replace it by this and this and this. And maybe eventually it comes up
*  with a model, which is still the ICCSI model. It cannot be, I mean, just for the knowledgeable
*  reader, ICCSI is incomputable. And that can prove that therefore there cannot be a computable exact
*  algorithm. There needs to be some approximations and this is not dealt with the Gertl machine.
*  So you have to do something about it. But there's the ICCSI model, which is finitely
*  computable, which we could put in. Which part of ICCSI is non-computable?
*  The Solomonov induction part. The induction. Okay. So-
*  But there's ways of getting computable approximations of the ICCSI model. So then
*  it's at least computable. It is still way beyond any resources anybody will ever have. But then the
*  Gertl machine could sort of improve it further and further in an exact way.
*  So is this theoretically possible that the Gertl machine process could improve? Isn't
*  ICCSI already optimal? It is optimal in terms of the reward collected
*  over its interaction cycles, but it takes infinite time to produce one action. And the
*  world continues whether you want it or not. So the model is assuming you had an oracle,
*  which solved this problem and then in the next 100 milliseconds or the reaction time you need
*  gives the answer, then ICCSI is optimal. It's optimal in sense of data also from learning
*  efficiency and data efficiency, but not in terms of computation time.
*  And then the other Gertl machine in theory, but probably not provably could make it go faster.
*  Yes. Okay. Interesting. Those two components are super interesting. The perfect intelligence
*  combined with self-improvement. Sort of provable self-improvement since you're always getting the
*  correct answer and you're improving. Beautiful ideas. Okay. So you've also mentioned that
*  different kinds of things in the chase of solving this reward, sort of optimizing for the goal,
*  interesting human things could emerge. So is there a place for consciousness within ICCSI?
*  Where does, maybe you can comment because I suppose we humans are just another
*  instantiation of ICCSI agents and we seem to have consciousness.
*  You say humans are an instantiation of an ICCSI agent.
*  Yes.
*  Oh, that would be amazing. But I think that's not true even for the smartest and most rational humans.
*  Maybe we are very crude approximations.
*  Interesting. I mean, I tend to believe, again, I'm Russian, so I tend to believe our flaws
*  are part of the optimal. So we tend to laugh off and criticize our flaws. And I tend to
*  think that that's actually close to an optimal behavior.
*  Well, some flaws, if you think more carefully about it, are actually not flaws. But I think
*  there are still enough flaws. I don't know. It's unclear. As a student of history, I think all the
*  suffering that we've endured as a civilization, it's possible that that's the optimal amount
*  of suffering we need to endure to minimize long-term suffering. That's your Russian background.
*  That's the Russian. Whether humans are or not instantiations of an ICCSI agent,
*  do you think there's consciousness to something that could emerge
*  in a computational formal framework like ICCSI?
*  Let me also ask you a question. Do you think I'm conscious?
*  Yeah, that's a good question. That tie is confusing me, but I think so.
*  You think that makes me unconscious because it strangles me?
*  If an agent were to solve the imitation game posed by Turing, I think they would be dressed
*  similarly to you. Because there's a kind of flamboyant, interesting, complex behavior pattern
*  that sells that you're human and you're conscious. But why do you ask?
*  Was it a yes or was it a no?
*  Yes. I think you're conscious, yes.
*  And you explain somehow why. But you infer that from my behavior. You can never be sure about that.
*  I think the same thing will happen with any intelligent agent we develop if it behaves
*  in a way sufficiently close to humans. Or maybe even not humans. Maybe a dog is also
*  sometimes a little bit self-conscious. If it behaves in a way where we attribute typically
*  consciousness, we would attribute consciousness to these intelligent systems and probably in
*  particular. That of course doesn't answer the question whether it's really conscious.
*  And that's the big hard problem of consciousness. Maybe I'm a zombie. I mean, not the movie zombie,
*  but the philosophical zombie.
*  Is to you the display of consciousness close enough to consciousness from a perspective of
*  AGI that the distinction of the hard problem of consciousness is not an interesting one?
*  I think we don't have to worry about the consciousness problem, especially the hard
*  problem for developing AGI. I think we progress. At some point we have solved all the technical
*  problems and this system will behave intelligent and then super intelligent. And this consciousness
*  will emerge. I mean, definitely it will display behavior which we will interpret as conscious.
*  And then it's a philosophical question. Did this consciousness really emerge or is it a zombie
*  which just fakes everything? We still don't have to figure that out. Although it may be interesting,
*  at least from a philosophical point of view, it's very interesting, but it may also be
*  sort of practically interesting. There's some people saying if it's just faking consciousness
*  and feelings, then we don't need to be concerned about rights. But if it's real conscious and has
*  feelings, then we need to be concerned. I can't wait till the day where AI systems
*  exhibit consciousness because it'll truly be some of the hardest ethical questions
*  of what we do with that. It is rather easy to build systems which people ascribe consciousness.
*  And I give you an analogy. I mean, remember maybe it was before you were born, the Tamagotchi.
*  Yeah, how dare you, sir.
*  Why? That's the reason you're young, right?
*  Yes, that's good. Thank you. Thank you very much. But I was also in the Soviet Union. We didn't have
*  any of those fun things.
*  But you have heard about this Tamagotchi, which was really, really primitive. Actually, for the
*  time it was... And you could race this and kids got so attached to it and didn't want to let it die.
*  I would have probably... If we would have asked the children, do you think this Tamagotchi is
*  conscious? And they would have said yes. I think that's kind of a beautiful thing, actually,
*  because that consciousness, ascribing consciousness seems to create a deeper connection,
*  which is a powerful thing. But we have to be careful on the ethics side of that.
*  Well, let me ask about the AGI community broadly. You kind of represent
*  some of the most serious work on AGI, at least earlier. And DeepMind represents serious work on
*  AGI these days. But why, in your sense, is the AGI community so small or has been so small
*  until maybe DeepMind came along? Why aren't more people seriously working on
*  human level and superhuman level intelligence from a formal perspective?
*  Okay. From a formal perspective, that's sort of an extra point. So I think there are a couple
*  of reasons. I mean, AI came in waves, right? AI winters and AI summers, and then there were
*  big promises which were not fulfilled. And people got disappointed. But narrow AI,
*  solving particular problems which seem to require intelligence, was always to some extent
*  successful. And there were improvements, small steps. And if you build something which is
*  useful for society or industrial useful, then there's a lot of funding. So I guess it was in
*  parts the money which drives people to develop specific systems, solving specific tasks.
*  But you would think that, at least in university, you should be able to do ivory tower research.
*  And that was probably better a long time ago. But even nowadays, there's quite some pressure of
*  doing applied research or translational research. And it's harder to get grants as a theorist.
*  So that also drives people away. It's maybe also harder attacking the general intelligence
*  problem. So I think enough people, I mean, maybe a small number, were still interested in
*  formalizing intelligence and thinking of general intelligence. But
*  not much came up, right? Or not much great stuff came up.
*  RG So what do you think? We talked about the formal, big light at the end of the tunnel.
*  But from the engineering perspective, what do you think it takes to build an AGI system?
*  Is that and I don't know if that's a stupid question, or a distinct question from everything
*  we've been talking about, IAIC, but what do you see as the steps that are necessary to take
*  to start to try to build something?
*  MF So you want to blueprint now and then you go off and do it?
*  RG That's the whole point of this conversation, trying to squeeze that in there. Now, is there,
*  I mean, what's your intuition? Is it is in the robotic space or something that has a body and
*  tries to explore the world? Is in the reinforcement learning space, like the efforts of AlphaZero and
*  AlphaStar, they're kind of exploring how you can solve it through in the simulation in the gaming
*  world? Is there stuff in sort of the, all the transformer work in natural English processing,
*  sort of maybe attacking the open domain dialogue? Like what, where do you see the promising pathways?
*  MF Let me pick the embodiment maybe. So, embodiment is important, yes and no. I don't believe that we
*  need a physical robot walking or rolling around interacting with the real world in order to achieve
*  AGI. And I think it's more of a distraction probably than helpful. It's sort of confusing
*  the body with the mind. For industrial applications or near term applications,
*  of course, we need robots for all kinds of things, yeah, but for solving the big problem,
*  at least at this stage, I think it's not necessary. But the answer is also yes, that I think the most
*  promising approach is that you have an agent and that can be a virtual agent in a computer
*  interacting with an environment, possibly a 3D simulated environment like in many computer games
*  and you train and learn the agent. Even if you don't intend to later put it sort of this
*  algorithm in a robot brain and leave it forever in the virtual reality, getting experience in a,
*  although it's just simulated 3D world, is possibly, and I say possibly, important to
*  understand things on a similar level as humans do, especially if the agent or primarily if the agent
*  wants, needs to interact with the humans, right? If you talk about objects on top of each other
*  in space and flying in cars and so on, and the agent has no experience with even virtual 3D
*  worlds, it's probably hard to grasp. But if you develop an abstract agent, say we take the
*  mathematical path and we just want to build an agent which can prove theorems and becomes a better
*  and better mathematician, then this agent needs to be able to reason in very abstract spaces and then
*  maybe sort of putting it into 3D environments, simulated, is even harmful. It should sort of,
*  you put it in, I don't know, an environment which it creates itself or so.
*  It seems like you have an interesting, rich, complex trajectory through life in terms of
*  your journey of ideas. So it's interesting to ask what books, technical fiction, philosophical
*  books, ideas, people had a transformative effect. Books are most interesting because maybe people
*  could also read those books and see if they could be inspired as well.
*  Well, yeah, luckily I asked books and not singular book. It's very hard and I tried to
*  pin down one book and I can do that at the end. So the books which were most transformative for
*  me or which I can most highly recommend to people interested in AI-
*  Both perhaps.
*  Yeah, yeah, both here. I would always start with Russell and Norbic, Artificial Intelligence,
*  A Modern Approach. That's the AI Bible. It's an amazing book. It's very broad. It covers all
*  approaches to AI and even if you focus on one approach, I think that is the minimum you should
*  know about the other approaches out there. So that should be your first book.
*  The fourth edition should be coming out soon.
*  Oh, okay. Interesting.
*  There's a deep learning chapter now, so there must be. Written by Ian Goodfellow. Okay.
*  And then the next book I would recommend, the Reinforcement Learning Book by Sutton and Bartow.
*  That's a beautiful book. If there's any problem with the book, it makes RL
*  feel and look much easier than it actually is. It's a very gentle book. It's very nice to read,
*  the exercises to do. You can very quickly get some RL systems to run. You know, very toy problems,
*  but it's a lot of fun and in a couple of days you feel you know what RL is about,
*  but it's much harder than the book.
*  Yeah.
*  Come on now. It's an awesome book.
*  Yeah, it is. Yeah. And maybe, I mean, there's so many books out there. If you like the information
*  theoretic approach, then there's Kolmogorov Complexity by Alin Vitani, but probably some
*  short article is enough. You don't need to read the whole book, but it's a great book.
*  And if you have to mention one all-time favorite book, so different flavor, that's a book
*  which is used in the international baccalaureate for high school students in several countries.
*  That's from Nicholas Alchen, Theory of Knowledge.
*  Second edition or first, not the third, please. The third one, they took out all the fun.
*  Okay.
*  So this asks all the interesting or to me interesting philosophical questions about
*  how we acquire knowledge from all perspectives, you know, from math, from art, from physics,
*  and ask how can we know anything. And the book is called Theory of Knowledge.
*  Is this almost like a philosophical exploration of how we get knowledge from anything?
*  Yes. Yeah. I mean, can religion tell us, you know, about something about the world? Can science tell
*  us something about the world? Can mathematics or is it just playing with symbols? And, you know,
*  these open-ended questions. And I mean, it's for high school students, so they have resources from
*  Hitchhiker's Guide to the Galaxy and from Star Wars and The Chicken Across the Road. And it's
*  fun to read, but it's also quite deep. If you could live one day of your life over again,
*  because it made you truly happy, or maybe like we said with the books, it was truly transformative.
*  What day, what moment would you choose that something pop into your mind?
*  Does it need to be a day in the past or can it be a day in the future?
*  Well, space-time is an emergent phenomena, so it's all the same anyway.
*  Okay. Okay. From the past.
*  You're really going to say from the future. I love it.
*  No, I will tell you from the future. Okay. From the past.
*  From the past, I would say when I discovered my Axiomodel. I mean, it was not in one day,
*  but it was one moment where I realized Kolmogorov complexity and didn't even know
*  that it existed, but I discovered sort of this compression idea myself, but immediately I knew
*  I can't be the first one, but I had this idea. And then I knew about sequential decision-making,
*  and I knew if I put it together, this is the right thing. And yeah, still when I think back
*  about this moment, I'm super excited about it. Was there any more details and context
*  that moment? Did an apple fall on your head? If you look at Ian Goodfellow talking about
*  Gans, there was beer involved. Is there some more context of what sparked your thought,
*  or was it just- No, it was much more mundane. So I worked in this company. So in this sense,
*  the four and a half years was not completely wasted. And I worked on an image interpolation
*  problem, and I developed a quite neat new interpolation techniques, and they got patented.
*  Then, which happens quite often, I got sort of overboard and thought about, yeah, that's pretty
*  good, but it's not the best. So what is the best possible way of doing interpolation? And then I
*  thought, yeah, you want the simplest picture, which is if your coarse-grained recovers your
*  original picture. And then I thought about the simplicity concept more in quantitative terms,
*  and then everything developed. And somehow the full beautiful mix of also being a physicist
*  and thinking about the big picture of it, then led you to probably be big with Ix.
*  Yeah. So as a physicist, I was probably trained not to always think in computational terms,
*  just ignore that and think about the fundamental properties which you want to have.
*  So what about if you could really live one day in the future? What would that be?
*  When I solve the AGI problem. In practice, in theory, I've solved it with the Ix model,
*  practice. And then I asked the first question. What would be the first question?
*  What's the meaning of life? I don't think there's a better way to end it.
*  Thank you so much for talking to me. It is a huge honor to finally meet you.
*  Yeah, thank you too. It was a pleasure of mine too.
*  Thanks for listening to this conversation with Marcus Hutter, and thank you to our
*  presenting sponsor, Cash App. Download it, use code LEXPODCAST, you'll get $10, and $10 will go
*  to FIRST, an organization that inspires and educates young minds to become science and
*  technology innovators of tomorrow. If you enjoy this podcast, subscribe on YouTube,
*  give it five stars on Apple Podcasts, support on Patreon, or simply connect with me on Twitter
*  at Lex Friedman. And now let me leave you with some words of wisdom from Albert Einstein.
*  The measure of intelligence is the ability to change.
*  Thank you for listening, and hope to see you next time.
