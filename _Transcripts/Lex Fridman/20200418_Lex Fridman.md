---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 11468s
Video Keywords: ['stephen wolfram', 'theory of everything', 'wolfram physics project', 'game of life', 'mathematic', 'wolfram language', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 1449342
Video Rating: None
Video Description: Stephen Wolfram is a computer scientist, mathematician, and theoretical physicist who is the founder and CEO of Wolfram Research, a company behind Mathematica, Wolfram Alpha, Wolfram Language, and the new Wolfram Physics project. He is the author of several books including A New Kind of Science, which on a personal note was one of the most influential books in my journey in computer science and artificial intelligence.

Support this podcast by signing up with these sponsors:
- ExpressVPN at https://www.expressvpn.com/lexpod
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Stephen's Twitter: https://twitter.com/stephen_wolfram
Stephen's Website: https://www.stephenwolfram.com/
Wolfram Research Twitter: https://twitter.com/WolframResearch
Wolfram Research YouTube: https://www.youtube.com/user/WolframResearch
Wolfram Research Website: https://www.wolfram.com/
Wolfram Alpha: https://www.wolframalpha.com/
A New Kind of Science (book): https://amzn.to/34JruB2

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

OUTLINE:
0:00 - Introduction
4:16 - Communicating with an alien intelligence
12:11 - Monolith in 2001: A Space Odyssey
29:06 - What is computation?
44:54 - Physics emerging from computation
1:14:10 - Simulation
1:19:23 - Fundamental theory of physics
1:28:01 - Richard Feynman
1:39:57 - Role of ego in science
1:47:21 - Cellular automata
2:15:08 - Wolfram language
2:55:14 - What is intelligence?
2:57:47 - Consciousness
3:02:36 - Mortality
3:05:47 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Stephen Wolfram Cellular Automata, Computation, and Physics  Lex Fridman Podcast #89
**Lex Fridman:** [April 18, 2020](https://www.youtube.com/watch?v=ez773teNFYA)
*  The following is a conversation with Stephen Wolfram, a computer scientist, mathematician,
*  and theoretical physicist who is the founder and CEO of Wolfram Research, a company behind
*  Mathematica, Wolfram Alpha, Wolfram Language, and the new Wolfram Physics Project. He is the
*  author of several books including A New Kind of Science, which on a personal note was one of the
*  most influential books in my journey in computer science and artificial intelligence. It made me
*  fall in love with the mathematical beauty and power of cellular automata. It is true that perhaps
*  one of the criticisms of Stephen is on a human level, that he has a big ego, which prevents some
*  researchers from fully enjoying the content of his ideas. We talk about this point in this
*  conversation. To me, ego can lead you astray, but can also be a superpower, one that fuels bold,
*  innovative thinking that refuses to surrender to the cautious ways of academic institutions.
*  And here, especially, I ask you to join me in looking past the peculiarities of human nature
*  and opening your mind to the beauty of ideas in Stephen's work and in this conversation.
*  I believe Stephen Wolfram is one of the most original minds of our time,
*  and at the core is a kind, curious, and brilliant human being. This conversation was recorded in
*  November 2019 when the Wolfram Physics Project was underway but not yet ready for public exploration
*  as it is now. We now agreed to talk again, probably multiple times in the near future.
*  So this is round one, and stay tuned for round two soon.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  review it with five stars on Apple Podcasts, support it on Patreon, or simply connect with
*  me on Twitter at Lex Friedman spelled F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now,
*  and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you, and doesn't hurt the listening experience.
*  Quick summary of the ads. Two sponsors, ExpressVPN and CashApp. Please consider
*  supporting the podcast by getting ExpressVPN at expressvpn.com slash LexPod and downloading
*  CashApp and using code LexPodcast. This show is presented by CashApp,
*  the number one finance app in the App Store. When you get it, use code LexPodcast. CashApp lets you
*  send money to friends, buy bitcoin, and invest in the stock market with as little as one dollar.
*  Since CashApp does fractional share trading, let me mention that the order execution algorithm
*  that works behind the scenes to create the abstraction of fractional orders
*  is an algorithmic marvel. Big props to the CashApp engineers for solving a hard problem
*  that in the end provides an easy interface that takes a step up to the next layer of abstraction
*  over the stock market. This makes trading more accessible for new investors and diversification
*  much easier. So again, if you get CashApp from the App Store or Google Play and use the code LexPodcast,
*  you get ten dollars, and CashApp will also donate ten dollars the first. An organization that is
*  helping to advance robotics and STEM education for young people around the world. This show is
*  presented by ExpressVPN. Get it at ExpressVPN.com slash LexPod to get a discount and to support
*  this podcast. I've been using ExpressVPN for many years. I love it. It's really easy to use. Press
*  the big power on button and your privacy is protected. And if you like, you can make it look
*  like your location is anywhere else in the world. This has a large number of obvious benefits.
*  Certainly, it allows you to access international versions of streaming websites like the Japanese
*  Netflix or the UK Hulu. ExpressVPN works on any device you can imagine. I use it on Linux. Shout
*  out to Ubuntu. New version coming out soon actually. Windows, Android, but it's available anywhere
*  else too. Once again, get it at ExpressVPN.com slash LexPod to get a discount and to support
*  this podcast. And now here's my conversation with Stephen Wolfram. You and your son Christopher
*  helped create the alien language in the movie Arrival. So let me ask maybe a bit of a crazy
*  question. But if aliens were to visit us on earth, do you think we would be able to find a common
*  language? Well, by the time we're saying aliens are visiting us, we've already prejudiced the
*  whole story because the concept of an alien actually visiting, so to speak, we already know
*  they're kind of things that make sense to talk about visiting. So we already know they exist in
*  the same kind of physical setup that we do. They're not, you know, it's not just radio signals. It's
*  an actual thing that shows up and so on. So I think in terms of, you know, can one find ways to
*  communicate? Well, the best example we have of this right now is AI. I mean, that's our first
*  sort of example of alien intelligence. And the question is, how well do we communicate with AI?
*  You know, if you were to say, if you were in the middle of a neural net, and you open it up,
*  and it's like, what are you thinking? Can you discuss things with it? It's not easy,
*  but it's not absolutely impossible. So I think by the time, given the setup of your question,
*  aliens visiting, I think the answer is yes, one will be able to find some form of communication,
*  whatever communication means, communication requires notions of purpose and things like this.
*  It's a kind of philosophical quagmire. So if AI is a kind of alien life form, what do you think
*  visiting looks like? So if we look at aliens visiting, and we'll get to discuss computation
*  and the world of computation. But if you were to imagine you said you're already prejudiced
*  something by saying you visit, but how would aliens visit? By visit, there's kind of an
*  implication. And here we're using the imprecision of human language, you know, in a world of the
*  future. And if that's represented in computational language, we might be able to take the concept
*  visit, and go look in the documentation basically, and find out exactly what does that mean? What
*  properties does it have? And so on. But by visit, in ordinary human language, I'm kind of taking it
*  to be there's, you know, something, a physical embodiment that shows up in a spacecraft,
*  since we kind of know that that's necessary. We're not imagining it's just, you know, photons
*  showing up in a radio signal that, you know, photons in some very elaborate pattern, we're
*  imagining it's, it's physical things made of atoms, and so on, that that show up,
*  can be photons in a pattern? Well, that's good question. I mean, whether there is the possibility,
*  you know, what counts as intelligence? Good question. I mean, it's, you know, and I used to
*  think there was sort of a, oh, they'll be, you know, it'll be clear what it means to find
*  extraterrestrial intelligence, etc, etc, etc. I've, I've increasingly realized as a result of science
*  that I've done, that there really isn't a bright line between the intelligent and the merely
*  computational, so to speak. So, you know, in our kind of everyday sort of discussion, we'll say
*  things like, you know, the weather has a mind of its own. Well, we let's unpack that question.
*  You know, we realize that there are computational processes that go on that determine the fluid
*  dynamics of this and that and the atmosphere, etc, etc, etc. How do we distinguish that from
*  the processes that go on in our brains of, you know, the physical processes that go on in our
*  brains? How do we, how do we, how do we separate those? How do we say the physical processes going
*  on that represent sophisticated computations in the weather? Oh, that's not the same as the
*  physical processes that go on that represent sophisticated computations in our brains.
*  The answer is I don't think there is a fundamental distinction. I think the distinction for us
*  is that there's kind of a, a thread of history and so on that connects kind of what happens in
*  different brains to each other, so to speak. And it's a, you know, what happens in the weather is
*  something which is not connected by sort of a, a thread of civilizational history, so to speak,
*  to what we're used to. In our story, in the stories that the human brain has told us,
*  but maybe the weather has its own stories. Absolutely. Absolutely. And that's, and that's
*  where we run into trouble thinking about extraterrestrial intelligence, because, you know,
*  it's like that pulsar magnetosphere that's generating these very elaborate radio signals,
*  you know, is that something that we should think of as being this whole civilization that's
*  developed over the last however long, you know, millions of years of processes going on in the
*  neutron star or whatever versus what, you know, what we're used to in human intelligence.
*  And I think it's a, I think in the end, you know, when people talk about extraterrestrial
*  intelligence and where is it in the whole, you know, Fermi paradox of how come there's no other
*  signs of intelligence in the universe, my guess is that we've got sort of two
*  alien forms of intelligence that we're dealing with, artificial intelligence, and sort of physical
*  or extraterrestrial intelligence. And my guess is people will sort of get comfortable with the
*  fact that both of these have been achieved around the same time. And in other words, people will say,
*  well, yes, we're used to computers, things we've created, digital things we've created being sort
*  of intelligent, like we are. And they'll say, oh, we're kind of also used to the idea that there
*  are things around the universe that are kind of intelligent like we are, except they don't share
*  the sort of civil relational history that we have. And so we don't, you know, they're a different
*  branch. I mean, it's similar to when you talk about life, for instance, I mean, you kind of
*  said life form, I think almost synonymously with intelligence, which I don't think is,
*  the AIs will be upset to hear you equate those two things.
*  I would say really probably implied biological life.
*  Right. Right.
*  But you're saying, I mean, we'll explore this more, but you're saying it's really a spectrum,
*  and it's all just the kind of computation. And so it's a full spectrum. And we just make ourselves
*  special by weaving a narrative around our particular kinds of computation.
*  Yes. I mean, the thing that I think I've kind of come to realize is, you know, at some level,
*  it's a little depressing to realize that there's so little that's special.
*  Or liberating.
*  Well, yeah, but I mean, it's the story of science, right? And, you know, from Copernicus on,
*  it's like, you know, first we were like convinced our planets at the center of the universe.
*  Now that's not true. Well, then we were convinced there's something very special about the chemistry
*  that we have as biological organisms. Now that's not really true. And then we're still holding out
*  that hope over this intelligence thing we have. That's really special. I don't think it is.
*  However, in a sense, as you say, it's kind of liberating for the following reason that you
*  realize that what's special is the details of us, not some abstract attribute that, you know,
*  we could wonder, oh, is something else going to come along and, you know, also have that abstract
*  attribute? Well, yes, every abstract attribute we have something else has it. But the full details
*  of our kind of history of our civilization and so on, nothing else has that. That's what,
*  you know, that's our story, so to speak. And that's sort of almost by definition, special.
*  So I view it as not being such a, I mean, I was initially I was like, this is bad. This is,
*  this is kind of, you know, how can we have self respect about, about the things that we do,
*  then I realized the details of the things we do, they are the story. Everything else is kind of
*  a blank canvas. So maybe on a small tangent, you just made me think of it, but what do you make
*  of the monoliths in 2001 Space Odyssey in terms of aliens communicating with us and sparking
*  the kind of particular intelligent computation that we humans have?
*  Is there anything interesting to get from that sci-fi? Yeah, I mean, I think what's fun about that
*  is, you know, the monoliths are these, you know, one to four to nine perfect cuboid things. And in
*  the, you know, Earth of a million years ago, whatever they were portraying with a bunch of
*  apes and so on, a thing that has that level of perfection seems out of place. It seems very kind
*  of constructed, very engineered. So that's an interesting question. What is the, you know,
*  what's the techno signature, so to speak? What is it that you see it somewhere and you say,
*  my gosh, that had to be engineered. Now, the fact is, we see crystals, which are also very perfect.
*  And, you know, the perfect ones are very perfect, they're nice polyhedral, whatever.
*  And so in that sense, if you say, well, it's a sign of sort of, it's a techno signature,
*  that it's a perfect, you know, a perfect polygonal shape, polyhedral shape. That's not true.
*  And so then it's an interesting question. What is the, you know, what is the right signature? I mean,
*  like, you know, Gauss, famous mathematician, you know, he had this idea, you should cut down
*  the Siberian forest in the shape of sort of a typical image of the proof of the Pythagorean
*  theorem on the grounds that, it was a kind of cool idea, didn't get done. But, you know, it's on the
*  grounds that the Martians would see that and realize, gosh, there are mathematicians out there.
*  It's kind of, you know, it's the, in his theory of the world, that was probably the best advertisement
*  for the cultural achievements of our species. But, you know, it's a reasonable question. What do you,
*  what can you send or create that is a sign of intelligence in its creation, or even intention
*  in its creation? You talk about if we were to send a beacon, can you, what should we send? Is math
*  our greatest creation? What is our greatest creation? I think, I think it's a philosophically
*  doomed issue. I mean, in other words, you send something, you think it's fantastic, but it's kind
*  of like, we are part of the universe. We make things that are, you know, things that happen in
*  the universe. Computation, which is sort of the thing that we are, in some abstract sense,
*  using to create all these elaborate things we create, is surprisingly ubiquitous. In other words,
*  we might have thought that, you know, we've built this whole giant engineering stack that's led us
*  to microprocessors, that's led us to be able to do elaborate computations. But this idea,
*  the computations are happening all over the place. The only question is whether there's a thread that
*  connects our human intentions to what those computations are. And so I think, I think this
*  question of what do you send to kind of show off our civilization in the best possible way, I think
*  any kind of almost random slab of stuff we've produced is about equivalent to everything else.
*  I think it's one of these things where- Such a non-romantic way of phrasing it. I just, sorry to
*  interrupt, but I just talked to Anne Druyan, who's the wife of Carl Sagan. And so, I don't know if
*  you're familiar with the Voyager, I mean, she was part of sending, I think, brainwaves of, you know-
*  Wasn't it hers?
*  It was hers. Her brainwaves when she was first falling in love with Carl Sagan, right, it's this
*  beautiful story. That perhaps you would shut down the power of that by saying we might as well send
*  anything else and that's interesting. All of it is kind of an interesting peculiar thing that's-
*  Yeah, yeah, right. Well, I mean, I think it's kind of interesting to see on the Voyager,
*  you know, golden record thing. One of the things that's kind of cute about that is, you know,
*  it was made, when was it, in the late 70s, early 80s. And, you know, one of the things, it's a
*  phonograph record, okay, and it has a diagram of how to play a phonograph record. And, you know,
*  it's kind of like, it's shocking that in just 30 years, if you show that to a random kid of today,
*  and you show them that diagram, and I've tried this experiment, they're like, I don't know what
*  the heck this is. And the best anybody can think of is, you know, take the whole record, forget the
*  fact that it has some kind of helical track in it, just image the whole thing and see what's there.
*  That's what we would do today. In only 30 years, our technology has kind of advanced to the point
*  where the playing of a helical, you know, mechanical track on a phonograph record is now something
*  bizarre. So, you know, it's a, that's a cautionary tale, I would say, in terms of the ability to
*  make something that in detail sort of leads by the nose, some, you know, the aliens or whatever,
*  to do something. It's like, no, you know, best you're going to do, as I say, if we were doing
*  this today, we would not build a helical scan thing with a needle. We would just take some
*  high resolution imaging system and get all the bits off it and say, oh, it's a big nuisance that
*  they put in a helix, you know, spiral, let's, let's just unravel the spiral and start from there.
*  Do you think, and this will get into trying to figure out
*  interpretability of AI, interpretability of computation, being able to communicate
*  with various kinds of computations. Do you think we'd be able to, if you put your alien hat on,
*  figure out this record, how to play this record?
*  Well, it's a question of what one wants to do. I mean,
*  understand what the other party was trying to communicate or understand anything about
*  the other party. What does understanding mean? I mean, that's the issue. The issue is it's like
*  when people were trying to do natural language understanding for computers, right? So people
*  tried to do that for years. It wasn't clear what it meant. In other words, you take your piece of
*  English or whatever, and you say, gosh, my computer has understood this. Okay, that's nice. What can
*  you do with that? Well, so for example, when we did, you know, built Wolf-Malpha, you know,
*  one of the things was it's, you know, it's doing question answering and so on. It needs to do
*  natural language understanding. The reason that I realized after the fact, the reason we were able
*  to do natural language understanding quite well, and people hadn't before, the number one thing was
*  we had an actual objective for the natural language understanding. We were trying to turn
*  the natural language into this computational language that we could then do things with.
*  Now, similarly, when you imagine you're alien, you say, okay, we're playing them the record.
*  Did they understand it? Well, depends what you mean. If there's a representation that they have,
*  if it converts to some representation where we can say, oh, yes, that's a representation that we can
*  recognize represents understanding, then all well and good. But actually, the only ones that I think
*  we can say would represent understanding are ones that will then do things that we humans kind of
*  recognize as being useful to us. Maybe try and understand, quantify how technologically advanced
*  this particular civilization is. So are they a threat to us from a military perspective?
*  That's probably the kind of first kind of understanding that we'll be interested in.
*  Gosh, that's so hard. I mean, that's like in the Arrival movie, that was sort of one of the key
*  questions is, why are you here, so to speak? Are you going to hurt us?
*  Right. But even that is very unclear. It's like the are you going to hurt us? That comes back to
*  a lot of interesting AI ethics questions because we might make an AI that says, well, take autonomous
*  cars, for instance. Are you going to hurt us? Well, let's make sure you only drive it precisely
*  the speed limit because we want to make sure we don't hurt you, so to speak. And then, well,
*  something you say, but actually that means I'm going to be really late for this thing. And
*  that sort of hurts me in some way. So it's hard to know. Even the definition of what it means to
*  hurt someone is unclear. And as we start thinking about things about AI ethics and so on,
*  that's something one has to address. There's always tradeoffs,
*  and that's the annoying thing about ethics. Yeah, well, right. And I mean, I think ethics,
*  like these other things we're talking about, is a deeply human thing. There's no abstract,
*  let's write down the theorem that proves that this is ethically correct. That's a meaningless idea.
*  You have to have a ground truth, so to speak, that's ultimately sort of what humans want,
*  and they don't all want the same thing. So that gives one all kinds of additional complexity in
*  thinking about that. One convenient thing in terms of turning ethics into computation,
*  you can ask the question of what maximizes the likelihood of the survival of the species.
*  Yeah, that's a good existential issue. But then when you say survival of the species,
*  right, you might say, you might, for example, for example, let's say, forget about technology,
*  just hang out and be happy, live our lives, go on to the next generation, go through many,
*  many generations where in a sense, nothing is happening. That okay? Is that not okay?
*  Hard to know. In terms of, you know, the attempt to do elaborate things and the attempt to might be
*  counterproductive for the survival of the species. Like for instance, I mean, and, you know,
*  I think it's, it's also a little bit hard to know. So okay, let's take that as a sort of thought
*  experiment. Okay. You know, you can say, well, what are the threats that we might have to survive,
*  you know, the super volcano, the asteroid impact, the, you know, all these kinds of things. Okay,
*  so now we inventory these possible threats and we say, let's make our species as robust as possible
*  relative to all these threats. I think in the end, it's a, it's sort of an unknowable thing,
*  what, what it takes to, you know, so, so given that you've got this AI and you've told it,
*  maximize the long-term, what does long-term mean? Does long-term mean until the sun burns out?
*  That's, that's not going to work. You know, does long-term mean next thousand years? Okay.
*  They're probably optimizations for the next thousand years that it's like, it's like if
*  you're running a company, you can make a company be very stable for a certain period of time.
*  Like if, you know, if your company gets bought by some, you know, private investment group,
*  then they'll, you know, you can, you can run a company just fine for five years by just taking
*  what it does and, you know, removing all R and D and the company will burn out after a while,
*  but it'll run just fine for a while. So if you tell the AI, keep the humans okay for a thousand
*  years, there's probably a certain set of things that one would do to optimize that many of which
*  one might say, well, that would be a pretty big shame for the future of history, so to speak,
*  for that to be what happens. But I think, I think in the end, you know, as you start thinking about
*  that question, it is, um, uh, what you realize is there's a whole sort of raft of undecidability,
*  computational irreducibility. In other words, it's, I mean, one of the good things about sort of the,
*  the, what our civilization has gone through and what sort of we humans go through is that there's
*  a certain computational irreducibility to it in the sense that it isn't the case that you can look
*  from the outside and just say, the answer is going to be this. At the end of the day, this is what's
*  going to happen. You actually have to go through the process to find out. And I think that's,
*  that's both that feels better in the sense it's not a, you know, something is achieved by going
*  through all of this, uh, uh, all of this process. And, um, it's, uh, uh, but it also means that
*  telling the AI go figure out, you know, what will be the best outcome? Well, unfortunately,
*  it's going to come back and say, it's kind of undecidable what to do. We'd have to run all of
*  those scenarios, um, to see what happens. And if we want it for the infinite future, we're thrown
*  immediately into sort of standard issues of, of kind of infinite computation and so on.
*  So yeah, even if you get that the answer to the universe and everything is 42, you still have to
*  actually run the universe. Yes. To figure out like the question, I guess, or the, the, the,
*  you know, the, the journey is, is the point. Right. Well, I think it's saying to summarize,
*  this is the result of the universe. Yeah. That's if that is possible, it tells us, I mean, the whole
*  sort of structure of thinking about computation and so on and thinking about how stuff works.
*  If, if there, if it's possible to say, and the answer is such and such, you're basically saying
*  there's a way of going outside the universe and you're kind of, you're getting yourself into
*  something of a sort of paradox because you're saying if it's knowable, what the answer is,
*  then there's a way to know it. That is beyond what the universe provides. But if we can know it,
*  then something that we're dealing with is beyond the universe. So then the universe isn't the
*  universe, so to speak. So, and in general, as, as, as we'll talk about, at least for our small
*  human brains, it's hard to show that the result of a sufficiently complex computation, it's hard.
*  I mean, it's probably impossible, right. Undecidability. So, and the universe appears
*  by at least the poets to be sufficiently complex, they won't be able to predict
*  what the heck it's all going to. Well, we better not be able to, because if we can,
*  it kind of denies, I mean, it's, you know, we're part of the universe. Yeah. So what does it mean
*  for us to predict? It means that we, that our little part of the universe is able to jump ahead
*  of the whole universe. And, you know, this, this quickly winds up, I mean, that it is conceivable.
*  The only way we'd be able to predict is if we are so special in the universe, we are the one place
*  where there is computation more special, more sophisticated than anything else that exists in
*  the universe. That's the only way we would have the ability to sort of the almost theological
*  ability, so to speak, to predict what happens in the universe is to say somehow we're, we're
*  better than everything else in the universe, which I don't think is the case. Yeah, perhaps we can
*  detect a large number of looping patterns that reoccur throughout the universe and fully describe
*  them and therefore, but then it's, it still becomes exceptionally difficult to see how those
*  patterns interact and what kind of complexity. Well, look, the most remarkable thing about the
*  universe is that it's has regularity at all. Might not be the case. If you just have regularity,
*  absolutely. It's full of, I mean, physics is successful, you know, it's full of, of laws
*  that tell us a lot of detail about how the universe works. I mean, it could be the case that,
*  you know, the 10th to the 90th particles in the universe, they all do their own thing,
*  but they don't, they all follow. We already know they all follow basically physical, the same
*  physical laws. And that's something that's a very profound fact about the universe.
*  What conclusion you draw from that is unclear. I mean, in the, you know, the early, early
*  theologians, that was, you know, exhibit number one for the existence of God. Now, you know,
*  people have different conclusions about it, but the fact is, you know, right now, I mean,
*  I happen to be interested actually, I've just restarted a long running kind of interest of mine
*  about fundamental physics. I'm kind of like, I'm on, I'm on a bit of a quest, which I'm about to
*  make more public to see if I can actually find the fundamental theory of physics.
*  Excellent. We'll come to that. And I just had a lot of conversations with quantum mechanics folks
*  with, so I'm really excited on your take, because I think you have a fascinating take on the,
*  the fundamental nature of our reality from a physics perspective. So, and what might be
*  underlying the kind of physics as we think of it today? Okay. Let's take a step back. What is
*  computation? That's a good question. Operationally computation is following rules.
*  That's kind of it. I mean, computation is the result is the process of systematically following
*  rules. And it is the thing that happens when you do that. So taking initial conditions or taking
*  inputs and following rules. I mean, what are you following rules on? So there has to be some data,
*  some, not necessarily. It can be something where there's a, you know, very simple input,
*  and then you're following these rules. And you'd say there's not really much data going into this.
*  It's you could actually pack the initial conditions into the rule if you want to. So I think the,
*  the question is, is there a robust notion of computation? That is what does this mean? What
*  I mean by that is something like this. So, so one of the things in a different, in a physics,
*  something like energy, okay, the different forms of energy, there's, but somehow energy is a robust
*  concept that doesn't, isn't particular to kinetic energy or, you know, nuclear energy or whatever
*  else. There's a robust idea of energy. So one of the things you might ask is, does the robust idea
*  of computation, or does it matter that this computation is running in a Turing machine?
*  This computation is running in a CMOS silicon CPU. This computation is running in a fluid system in
*  the weather, those kinds of things. Or is there a robust idea of computation that transcends the
*  sort of detailed framework that it's running in? Okay. And is that yes. I mean, it wasn't obvious
*  that there was. So it's worth understanding the history and how we got to where we are right now.
*  Because, you know, to say that there is, is a statement in part about our universe.
*  It's not a statement about what is mathematically conceivable. It's about what actually can exist
*  for us. Maybe you can also comment because energy as a concept is robust, but there's also,
*  it's intricate, complicated relationship with matter, with mass, is very interesting. Of
*  particles that carry force and particles that sort of particles that carry force and particles
*  that have mass. These kinds of ideas, they seem to map to each other, at least in the mathematical
*  sense. Is there a connection between energy and mass and computation or are these completely
*  disjoint ideas? We don't know yet. The things that I'm trying to do about fundamental physics
*  may well lead to such a connection, but there is no known connection at this time.
*  So can you elaborate a little bit more on what, how do you think about computation? What is
*  computation? Yeah. So, I mean, let's tell a little bit of a historical story. Okay. So, you know,
*  back, go back 150 years, people were making mechanical calculators of various kinds. And,
*  you know, the typical thing was you want an adding machine, you go to the adding machine store,
*  basically. You want a multiplying machine, you go to the multiplying machine store. They're
*  different pieces of hardware. And so that means that at least at the level of that kind of
*  computation and those kinds of pieces of hardware, there isn't a robust notion of computation.
*  There's the adding machine kind of computation. There's the multiplying machine notion of
*  computation and they're disjoint. So what happened in around 1900, people started imagining,
*  particularly in the context of mathematical logic, could you have something which would
*  represent any reasonable function? Right? And they came up with things, this idea of primitive
*  recursion was one of the early ideas and it didn't work. There were reasonable functions
*  that people could come up with that were not represented using the primitives, the primitive
*  recursion. Okay. So then, then along comes 1931 and Gödel's theorem and so on. And as, in looking
*  back, one can see that as part of the process of establishing Gödel's theorem, Gödel basically
*  showed how you could compile arithmetic, how you could basically compile logical statements like
*  this statement is unprovable into arithmetic. So what he essentially did was to show that arithmetic
*  can be a computer in a sense that's capable of representing all kinds of other things.
*  And then Turing came along, 1936 came up with Turing machines. Meanwhile, Alonzo Church had
*  come up with lambda calculus. And the surprising thing that was established very quickly is
*  the Turing machine idea about what might be, what computation might be is exactly the same as the
*  lambda calculus idea of what computation might be. And so, and then there started to be other ideas,
*  you know, register machines, other kinds of, other kinds of representations of computation.
*  And the big surprise was they all turned out to be equivalent. So in other words, it might have been
*  the case like those old adding machines and multiplying machines that, you know, Turing had
*  his idea of computation, Church had his idea of computation, and they were just different,
*  but it isn't true. They're actually all equivalent. So then by, I would say the, the,
*  oh, 1970s or so in sort of the computation, computer science, computation theory area,
*  people had sort of said, oh, Turing machines are kind of what computation is. Physicists were still
*  holding out saying, no, no, no, that's just not how the universe works. We've got all these
*  differential equations. We've got all these real numbers that have infinite numbers of digits.
*  The universe is not a Turing machine.
*  Right. The, you know, the Turing machines are a small subset of, of, that are the things that
*  we make in microprocessors and engineering structures and so on. So probably actually
*  through my work in the 1980s about sort of the relationship between computation and models of
*  physics, it became a little less clear that there would be, that there was this big sort of dichotomy
*  between what can happen in physics and what happens in things like Turing machines. And I
*  think probably by now people would mostly think, and by the way, brains were another kind of
*  elements of this. I mean, you know, Gödel didn't think that his notion of computational, what
*  amounted to his notion of computation would cover brains. And Turing wasn't sure either,
*  but although he was a little bit, he got to be a little bit more convinced that it should cover
*  brains. But so, you know, but I would say by probably sometime in the 1980s, there was
*  beginning to be sort of a general belief that yes, this notion of computation that could be captured
*  by things like Turing machines was reasonably robust. Now the next question is, okay, you can
*  have a universal Turing machine that's capable of being programmed to do anything that any Turing
*  machine can do. And, you know, this idea of universal computation, it's an important idea,
*  this idea that you can have one piece of hardware and program it with different pieces of software.
*  You know, that's kind of the idea that launched most modern technology. I mean, that's kind of,
*  that's the idea that launched computer revolution, software, etc. So important idea. But the thing
*  that's still kind of holding out from that idea is, okay, there is this universal computation thing,
*  but seems hard to get to. It seems like you want to make a universal computer, you have to kind of
*  have a microprocessor with, you know, a million gates in it, and you have to go to a lot of trouble
*  to make something that achieves that level of computational sophistication. Okay, so the surprise
*  for me was that stuff that I discovered in the early 80s, looking at these things called cellular
*  automata, which are really simple computational systems. The thing that was a big surprise to me
*  was that even when their rules were very, very simple, they were doing things that were as
*  sophisticated as they did when their rules were much more complicated. So it didn't look like,
*  you know, this idea, oh, to get sophisticated computation, you have to build something with
*  very sophisticated rules. That idea didn't seem to pan out. And instead, it seemed to be the case
*  that sophisticated computation was completely ubiquitous, even in systems with incredibly
*  simple rules. And so that led to this thing that I call the principle of computational equivalence,
*  which basically says, when you have a system that follows rules of any kind, then whenever the system
*  isn't doing things that are in some sense, obviously simple, then the computation that
*  the behavior of the system corresponds to is of equivalent sophistication. So that means that when
*  you kind of go from the very, very, very simplest things you can imagine, then quite quickly, you
*  hit this kind of threshold above which everything is equivalent in its computational sophistication.
*  Not obvious that would be the case. I mean, that's a science fact. Well, no, no, no, no,
*  hold on a second. So this you've opened with a new kind of science. I mean, I remember it was a huge
*  eye opener that such simple things can create such complexity. And yes, there's an equivalence,
*  but it's not a fact. It just appears to, I mean, as much as a fact as sort of these theories are so
*  elegant that it seems to be the way things are. But let me ask sort of, you just brought up
*  previously kind of like the communities of computer scientists with their Turing machines,
*  the physicists with their universe and the whoever the heck, maybe neuroscientists looking at the
*  brain. What's your sense in the equivalence? You've shown through your work that simple rules can
*  create equivalently complex Turing machine systems, right? Is the universe equivalent to
*  the kinds of Turing machines? Is the human brain a kind of Turing machine? Do you see those things
*  basically blending together or is there still a mystery about how disjoint they are?
*  Well, my guess is that they all blend together, but we don't know that for sure yet. I mean,
*  I should say, I said rather glibly that the principle of computational equivalence is sort
*  of a science fact. And I was using air quotes for the science fact because when you, it is a,
*  I mean, just to talk about that for a second, the thing is that it has a complicated
*  epistemological character similar to things like the second law of thermodynamics, the law of
*  entropy increase. What is the second law of thermodynamics? Is it a law of nature? Is it a
*  thing that is true of the physical world? Is it something which is mathematically provable? Is it
*  something which happens to be true of the systems that we see in the world? Is it in some sense,
*  a definition of heat perhaps? Well, it's a combination of those things. And it's the same
*  thing with the principle of computational equivalence. And in some sense, the principle
*  of computational equivalence is at the heart of the definition of computation,
*  because it's telling you there is a thing, there is a robust notion that is equivalent across all
*  these systems and doesn't depend on the details of each individual system. And that's why we can
*  meaningfully talk about a thing called computation. And we're not stuck talking about, oh, there's
*  computation in Turing machine number 3785, and et cetera, et cetera, et cetera. That's why there
*  is a robust notion like that. Now, on the other hand, can we prove the principle of computational
*  equivalence? Can we prove it as a mathematical result? Well, the answer is actually we've got
*  some nice results along those lines that say, throw me a random system with very simple rules.
*  Well, in a couple of cases, we now know that even the very simplest rules we can imagine of a certain
*  type are universal and do sort of follow what you would expect from the principle of computational
*  equivalence. So that's a nice piece of sort of mathematical evidence for the principle of
*  computational equivalence. Just to link on that point, the simple rules creating sort of these
*  complex behaviors. But is there a way to mathematically say that this behavior is complex?
*  That you've mentioned that you cross a threshold.
*  Right. There are various indicators. So for example, one thing would be, is it capable of
*  universal computation? That is, given the system, do there exist initial conditions for the system
*  that can be set up to essentially represent programs to do anything you want, to compute
*  primes, to compute pi, to do whatever you want. So that's an indicator. So we know in a couple of
*  examples that yes, the simplest candidates that could conceivably have that property
*  do have that property. And that's what the principle of computational equivalence might
*  suggest. But this principle of computational equivalence, one question about it is,
*  is it true for the physical world? It might be true for all these things we come up with,
*  the Turing machines, the cellular automata, whatever else. Is it true for our actual physical
*  world? Is it true for the brains, which are an element of the physical world? We don't know for
*  sure. And that's not the type of question that we will have a definitive answer to, because there's
*  a sort of scientific induction issue. You can say, well, it's true for all these brains, but this
*  person over here is really special and it's not true for them. And the only way that that cannot be
*  what happens is if we finally nail it and actually get a fundamental theory for physics,
*  and it turns out to correspond to, let's say, a simple program. If that is the case, then we will
*  basically have reduced physics to a branch of mathematics in the sense that we will not be,
*  right now with physics, we're like, well, this is the theory that, this is the rules that apply here.
*  But in the middle of that, right by that black hole, maybe these rules don't apply and something
*  else applies, and there may be another piece of the onion that we have to peel back. But if we can
*  get to the point where we actually have, this is the fundamental theory of physics, here it is,
*  it's this program, run this program and you will get our universe, then we've kind of reduced the
*  problem of figuring out things in physics to a problem of doing some, what turns out to be very
*  difficult, irreducibly difficult mathematical problems. But it no longer is the case that we
*  can say that somebody can come in and say, whoops, you know, you were right about all these things
*  about Turing machines, but you're wrong about the physical universe. We know there's sort of
*  ground truth about what's happening in the physical universe. Now, I happen to think, I mean, you asked
*  me at an interesting time, because I'm just in the middle of starting to re-energize my project to
*  kind of study fundamental theory of physics. As of today, I'm very optimistic that we're actually
*  going to find something and that it's going to be possible to see that the universe really is
*  computational in that sense. But I don't know, because we're betting against the universe,
*  so to speak. It's not like when I spend a lot of my life building technology, and then I know what's
*  in there, right? And it may have unexpected behavior, it may have bugs, things like that,
*  but fundamentally, I know what's in there. For the universe, I'm not in that position, so to speak.
*  LW What kind of computation do you think the fundamental laws of physics might emerge from?
*  Just to clarify, you've done a lot of fascinating work with kind of discrete kinds of computation.
*  You can sell your automata, and we'll talk about it, have this very clean structure. It's such a nice
*  way to demonstrate that simple rules can create immense complexity. But are cellular automata
*  sufficiently general to describe the kinds of computation that might create the laws of physics?
*  Can you give a sense of what kind of computation do you think would create laws of physics?
*  LW This is a slightly complicated issue, because as soon as you have universal computation,
*  you can in principle simulate anything with anything. But it is not a natural thing to do.
*  And if you're asking, were you to try to find our physical universe by looking at possible
*  programs in the computational universe of all possible programs, would the ones that correspond
*  to our universe be small and simple enough that we might find them by searching that computational
*  universe? We've got to have the right basis, so to speak. We've got to have the right language,
*  in effect, for describing computation for that to be feasible. So the thing that I've been
*  interested in for a long time is what are the most structural structures that we can create
*  with computation? So in other words, if you say a cellular automaton has a bunch of cells that are
*  arrayed on a grid, and every cell is updated in synchrony at a particular, when there's a
*  click of a clock, so to speak, and it goes a tick of a clock, and every cell gets updated at the
*  same time, that's a very specific, very rigid kind of thing. But my guess is that when we look
*  at physics, and we look at things like space and time, that what's underneath space and time
*  is something as structural as possible, that what we see, what emerges for us as physical space,
*  for example, comes from something that is sort of arbitrarily unstructured underneath. And so I've
*  been for a long time interested in kind of what are the most structural structures that we can set
*  up? And actually, what I had thought about for ages is using graphs, networks, where essentially,
*  so let's talk about space, for example. So what is space? Is a kind of a question one might ask.
*  Back in the early days of quantum mechanics, for example, people said, oh, for sure, space is going
*  to be discrete, because all these other things, we're finding a discrete, but that never worked
*  out in physics. And so space and physics today is always treated as this continuous thing, just like
*  Euclid imagined it. I mean, the very first thing Euclid says in his sort of common notions is,
*  you know, a point is something which has no part. In other words, there are points that are
*  arbitrarily small, and there's a continuum of possible positions of points. And the question is,
*  is that true? And so for example, if we look at, I don't know, fluid like air or water, we might say,
*  oh, it's a continuous fluid, we can pour it, we can do all kinds of things continuously.
*  But actually, we know, because we know the physics of it, that it consists of a bunch
*  of discrete molecules bouncing around, and only in the aggregate is it behaving like a continuum.
*  And so the possibility exists that that's true of space too. People haven't managed to make that work
*  with existing frameworks in physics. But I've been interested in whether one can imagine that
*  underneath space and also underneath time is something more structuralist. And the question is,
*  is it computational? So there are a couple of possibilities. It could be computational,
*  somehow fundamentally equivalent to a Turing machine, or it could be fundamentally not. So
*  how could it not be? It could not be so Turing machine essentially deals with integers, whole
*  numbers, some level. And you know, it can do things like it can add one to a number, it can
*  do things like this. It can also store whatever the heck it did. Yes, it has an
*  infinite storage. But when one thinks about doing physics, or sort of idealized physics,
*  or idealized mathematics, one can deal with real numbers, numbers with an infinite number of digits,
*  numbers which are absolutely precise. And one can say, we can take this number and we can
*  multiply it by itself. Are you comfortable with infinity in this context? Are you comfortable
*  in the context of computation? Do you think infinity plays a part? I think that the role of
*  infinity is complicated. Infinity is useful in conceptualizing things. It's not actualizable.
*  Almost by definition, it's not actualizable. But do you think infinity is part of the thing
*  that might underlie the laws of physics? I think that no, I think there are many questions that
*  you ask about, you might ask about physics, which inevitably involve infinity. Like when you say,
*  you know, is faster than light travel possible? You could say with with with given the laws of
*  physics, can you make something even arbitrarily large, even quotes infinitely large, that,
*  you know, that will make faster than light travel possible, then you're thrown into dealing with
*  infinity as a kind of theoretical question. But I mean, talking about, you know, sort of what's
*  underneath space and time, and what how one can make, you know, a computational infrastructure.
*  One possibility is that you can't make a computational infrastructure during this
*  machine sense that you really have to be dealing with precise real numbers. You're dealing with
*  partial differential equations, which just have precise real numbers at arbitrarily closely
*  separated points, you have a continuum for everything. Could be that that that's what happens,
*  that there's sort of a continuum for everything and precise real numbers for everything. And then
*  the things I'm thinking about are wrong. And, you know, that's, that's the risk you take if you're,
*  you know, if you're trying to sort of do things about nature, is you might just be wrong. It's
*  not it's for me personally, it's kind of a strange things. I've spent a lot of my life building
*  technology, where you can do something that nobody cares about. But you can't be sort of wrong in
*  that sense, in the sense you build your technology, and it does what it does. But but I think, you
*  know, this question of what, you know, what the sort of underlying computational infrastructure for
*  the universe might be. It's, so it's sort of inevitable, it's going to be fairly abstract,
*  because if you're going to get all these things, like there are three dimensions of space, there
*  are electrons, there are muons, there are quarks, there are this, you don't get to if the if the
*  model for the universe is simple, you don't get to have sort of a line of code for each of those
*  things, you don't get to have sort of the, the the the the muon case, the tau lepton case, and so on.
*  All of those have to be emergent, some right, so something deeper, right. So so that means it's
*  sort of inevitable, that's a little hard to talk about what the sort of underlying structuralist
*  structure actually is. Do you think our human beings have the cognitive capacity to understand,
*  if we're to discover to understand the kinds of simple structure from which these laws can emerge?
*  Like, do you think that's a good question? Well, here's what I think I think that,
*  I mean, I'm right in the middle of this right now. I'm telling you that I think you this,
*  yeah, I mean, this human has a hard time understanding, you know, a bunch of the
*  things that are going on. But but what happens in understanding is one builds waypoints. I mean,
*  if you said, understand modern 21st century mathematics, starting from, you know, counting
*  back in, you know, whenever counting was invented 50,000 years ago, whatever it was,
*  right, there's that will be really difficult. But what happens is we build waypoints that allow us
*  to get to higher levels of understanding. And we see the same thing happening in language.
*  You know, when we invent a word for something, it provides kind of a cognitive anchor, a kind of a
*  waypoint that lets us you know, like a podcast or something, you could be explaining, well, it's a
*  thing which this works this way, that way, the other way. But as soon as you have the word podcast,
*  and people kind of society understand it, you start to be able to build on top of that. And so I think
*  and that that's kind of the story of science, actually, too. I mean, science is about building
*  these kind of waypoints, where we find the sort of cognitive mechanism for understanding something
*  that we can build on top of it, you know, we, we have the idea of, I don't know, differential
*  equations, we can build on top of that, we have this idea, that idea. So my hope is that if it is
*  the case that we have to go all the way sort of from the sand to the computer, and there's no way
*  points in between, then we're toast, we won't be able to do that. Well, eventually, we might. So if
*  we're as clever apes are good enough for building those abstract abstractions, eventually from sand,
*  we'll get to the computer, right? And it's just might be a longer journey. The question is whether
*  it is something that you asked whether our human brains, yes, well, and we'll quotes understand
*  what's going on. And that's a different question. Because for that, it requires steps that are for
*  whether it's sort of from which we can construct a human understandable narrative. And that's
*  something that I think I am somewhat hopeful that that will be possible. Although, you know, as of
*  literally today, if you ask me, I'm confronted with things that I don't understand very well.
*  And so this is a small pattern in a computation trying to understand the rules under which the
*  computation functions. And it's it's an interesting possibility under which kinds of computations,
*  such a creature can understand itself. My guess is that within so we didn't talk much about
*  computational irreducibility, but it's a consequence of this principle of computational equivalence.
*  And it's sort of a core idea that that one has to understand, I think, which is question is,
*  you're doing a computation, you can figure out what happens in the computation just by running
*  every step in the computation and seeing what happens. Or you can say, let me jump ahead,
*  and figure out, you know, have something smarter that figures out what's going to happen before
*  it actually happens. And a lot of traditional science has been about that act of computational
*  reducibility. It's like, we've got these equations, and we can just solve them, and we can figure out
*  what's going to happen. We don't have to trace all of those steps, we just jump ahead because we
*  solve these equations. Okay, so one of the things that is a consequence of the principle of
*  computational equivalence is you don't always get to do that. Many, many systems will be
*  computationally irreducible, in the sense that the only way to find out what they do is just
*  follow each step and see what happens. Why is that? Well, if you have if you're saying, well,
*  we with our brains, we're a lot smarter, we don't have to mess around like the little cellular
*  automaton going through and updating all those cells, we can just, you know, use the power of
*  our brains to jump ahead. But if the principle of computational equivalence is right, that's not
*  going to be correct. Because it means that there's us doing our computation in our brains, there's
*  a little cellular automaton doing its computation. And the principle of computational equivalence
*  says, these two computations are fundamentally equivalent. So that means we don't get to say,
*  we're a lot smarter than the cellular automaton and jump ahead, because we're just doing computation
*  that's of the same sophistication as the cellular automaton itself. That's computational reducibility.
*  It's fascinating. But the and that's a really powerful idea. I think that's both depressing
*  and humbling and so on. That while we in a cellular automaton are the same, but the question we're
*  talking about the fundamental laws of physics is kind of the reverse question, you're not predicting
*  what's going to happen, you have to run the universe for that. But saying, can I understand
*  what rules likely generated me? I understand. But the problem is, to know whether you're right,
*  you have to have some computational reducibility, because we are embedded in the universe.
*  If the only way to know whether we get the universe is just to run the universe,
*  we don't get to do that. Because it just ran for 14.6 billion years or whatever. And we don't,
*  we can't rerun it, so to speak. So we have to hope that there are pockets of computational
*  reducibility sufficient to be able to say, yes, I can recognize those are electrons there.
*  And I think that it's a feature of computational irreducibility. It's sort of a mathematical
*  feature that there are always an infinite collection of pockets of reducibility.
*  The question of whether they land in the right place and whether we can sort of build a theory
*  based on them is unclear. But to this point about whether we, as observers in the universe,
*  built out of the same stuff as the universe, can figure out the universe, so to speak,
*  that relies on these pockets of reducibility. Without the pockets of reducibility, it won't work,
*  can't work. But I think this question about how observers operate, it's one of the features of
*  science over the last 100 years, particularly, has been that every time we get more realistic
*  about observers, we learn a bit more about science. So for example, relativity was all about
*  observers don't get to say when, you know, what's simultaneous with what. They have to just wait for
*  the light signal to arrive to decide what's simultaneous. Or for example, in thermodynamics,
*  observers don't get to say the position of every single molecule in a gas. They can only see the
*  kind of large scale features. And that's why the second law of thermodynamics, law of entropy
*  increase and so on works. If you could see every individual molecule, you wouldn't conclude
*  something about thermodynamics. You would conclude, oh, these molecules just all doing these particular
*  things. You wouldn't be able to see this aggregate fact. So I strongly expect that, in fact, in the
*  theories that I have, that one has to be more realistic about the computation and other aspects
*  of observers in order to actually make a correspondence between what we experience. In fact,
*  they have a my little team and I have a little theory right now about how quantum mechanics may
*  work, which is a very wonderfully bizarre idea about how sort of thread of human consciousness
*  relates to what we observe in the universe. But this is the several steps to explain what that's
*  about. What do you make of the mess of the observer at the lower level of quantum mechanics?
*  Sort of the textbook definition with quantum mechanics kind of says that there's some,
*  there's two worlds. One is the world that actually is, and the other is that's observed.
*  Yeah. What do you make sense of that? Well, I think actually the ideas we've recently had
*  might actually give away into this. I don't know yet. I think that's a mess. The fact is,
*  one of the things that's interesting, and when people look at these models that I started
*  talking about 30 years ago now, they say, oh, no, that can't possibly be right. What about
*  quantum mechanics? You say, okay, tell me what is the essence of quantum mechanics? What do you
*  want me to be able to reproduce to know that I've got quantum mechanics, so to speak? Well,
*  and that question comes up, it comes up very operational actually, because we've been doing
*  a bunch of stuff with quantum computing. And there are all these companies that say, we have
*  a quantum computer. We say, let's connect to your API and let's actually run it. And they're like,
*  well, maybe you shouldn't do that yet. We're not quite ready yet. And one of the questions
*  that I've been curious about is, if I have five minutes with a quantum computer, how can I tell
*  if it's really a quantum computer or whether it's a simulator at the other end? And turns out it's
*  really hard. It turns out there isn't, it's like a lot of these questions about sort of what is
*  intelligence, what's life. That's a boring test for quantum computing. That's right. That's right.
*  It's like, are you really a quantum computer? And I think the, yes, exactly. Is it just a simulation
*  or is it really a quantum computer? Same issue all over again. But that, so this whole issue about
*  the sort of mathematical structure of quantum mechanics and the completely separate thing that
*  is our experience in which we think definite things happen. Whereas quantum mechanics doesn't
*  say definite things ever happen. Quantum mechanics is all about the amplitudes for different things
*  to happen. But yet our thread of consciousness operates as if definite things are happening.
*  But to linger on the point, you've kind of mentioned the structure that could underlie
*  everything and this idea that it could perhaps have something like a structure of a graph.
*  Can you elaborate why your intuition is that there's a graph structure of nodes and edges
*  and what it might represent? Right. Okay. So the question is, what is in a sense,
*  the most structural structure you can imagine. Right. So, and in fact, what I've recently
*  realized in the last year or so, I have a new, most structural structure. By the way,
*  the question itself is a beautiful one and a powerful one in itself. So even without an answer,
*  just the question is a really strong question. Right. But what's your new idea?
*  Well, it has to do with hypergraphs. Essentially, what is interesting about the
*  sort of a model I have now is a little bit like what happened with computation. Everything that
*  I think of as, oh, well, maybe the model is this. I discover it's equivalent. And that's quite
*  encouraging because it's like, I could say, well, I'm going to look at trivalent graphs with three
*  edges for each node and so on. Or I could look at this special kind of graph, or I could look at
*  this kind of algebraic structure. And turns out that the things I'm now looking at, everything
*  that I've imagined that is a plausible type of structuralist structure is equivalent to this.
*  So what is it? Well, a typical way to think about it is, well, so you might have some collection
*  of tuples, collection of, let's say, numbers. So you might have one, three, five,
*  two, three, four, little, just collections of numbers, triples of numbers, let's say quadruples
*  of numbers, pairs of numbers, whatever. And you have all these sort of floating little tuples.
*  They're not in any particular order. And that sort of floating collection of tuples,
*  and I told you this was abstract, represents the whole universe. The only thing that relates them
*  is when a symbol is the same, it's the same, so to speak. So if you have two tuples and they contain
*  the same symbol, let's say at the same position of the tuple, the first element of the tuple,
*  then that represents a relation. Okay, so let me try and peel this back.
*  Wow. Okay.
*  I told you it's abstract, but this is the- So the relationship is formed by some aspect of sameness.
*  Right, but so think about it in terms of a graph. So a graph, a bunch of nodes,
*  let's say you number each node, okay? Then what is a graph? A graph is a set of pairs that say,
*  this node has an edge connecting it to this other node. So that's the, and a graph is just a
*  collection of those pairs that say, this node connects to this other node. So this is a
*  generalization of that, in which instead of having pairs, you have arbitrary and tuples.
*  That's it. That's the whole story. And now the question is, okay, so that might represent the
*  state of the universe. How does the universe evolve? What does the universe do? And so the
*  answer is that what I'm looking at is transformation rules on these hypergraphs. In other words,
*  you say this, whenever you see a piece of this hypergraph that looks like this,
*  turn it into a piece of hypergraph that looks like this. So on a graph, it might be when you see the
*  subgraph, when you see this thing with a bunch of edges hanging out in this particular way,
*  then rewrite it as this other graph. Okay. And so that's the whole story. So the question is,
*  what, so now you say, I mean, as I say, this is quite abstract. And one of the questions is,
*  where do you do those updating? So you've got this giant graph.
*  What triggers the updating? Like what's the ripple effect of it? Is it, and I suspect
*  everything's discrete even in time. So. Okay. So the question is, where do you do the updates?
*  Yes. And the answer is the rule is you do them wherever they apply. And you do them,
*  the order in which the updates is done is not defined. That is that you can do them. So there
*  may be many possible orderings for these updates. Now, the point is, imagine you're an observer in
*  this universe. So, and you say, did something get updated? Well, you don't in any sense know
*  until you yourself have been updated. Right. So in fact, all that you can be sensitive to
*  is essentially the causal network of how an event over there affects an event that's in you.
*  It doesn't even feel like observation. That's like, that's something else. You're just part of the
*  whole thing. Yes, you're part of it, but, but even to have, so the, the end result of that is all
*  you're sensitive to is this causal network of what event affects what other event.
*  I'm not making a big statement about sort of the structure of the observer. I'm simply saying,
*  I'm simply making the argument that what happens, the microscopic order of these rewrites
*  is not something that any observer, any conceivable observer in this universe
*  can be affected by, because the only thing the observer can be affected by is this causal network
*  of how the events in the observer are affected by other events that happen in the universe. So
*  the only thing you have to look at is the causal network. You don't really have to look at this
*  microscopic rewriting that's happening. So these rewrites are happening wherever they,
*  they happen wherever they feel like. Causal network is there, you said that there's not really,
*  so the idea would be an undefined, like what gets updated, the sequence of things is undefined. It's
*  yes, that's what you mean by the causal network. But then the cause,
*  no, the causal network is given that an update has happened, that's an event. Then the question is,
*  is that event causally related to does that event, if that event didn't happen,
*  then some future event couldn't happen yet. Gotcha. And so you build up this network of what
*  affects what. Okay. And so what that does, so when you build up that network, that's kind of the
*  observable aspect of the universe in some sense. And so then you can ask questions about, you know,
*  how robust is that observable network of what's happening in the universe? Okay. So here's where
*  it starts getting kind of interesting. So for certain kinds of microscopic rewriting rules,
*  the order of rewrites does not matter to the causal network. And so this is, okay, mathematical
*  logic moment. This is equivalent to the Church-Rosser property or the confluence property of rewrite
*  rules. And it's the same reason that if you're simplifying an algebraic expression, for example,
*  you can say, oh, let me expand those terms out. Let me factor those pieces. Doesn't matter what
*  order you do that in. You'll always get the same answer. And that's, it's the same fundamental
*  phenomenon that causes for certain kinds of microscopic rewrite rules, that causes the
*  causal network to be independent of the microscopic order of rewritings. Why is that property important?
*  Because it implies special relativity. I mean, the reason it's important is that that property,
*  special relativity says you can look at these sort of, you can look at different reference frames.
*  You can have different, you can be looking at your notion of what space and what's time can be
*  different, depending on whether you're traveling at a certain speed, depending on whether you're
*  doing this, that and the other. But nevertheless, the laws of physics are the same. That's what the
*  principle of special relativity says is laws of physics are the same independent of your reference
*  frame. Well, turns out this sort of change of the microscopic rewriting order is essentially
*  equivalent to a change of reference frame, or at least there's a sub part of how that works.
*  That's equivalent to change a reference frame. So somewhat surprisingly, and sort of for the first
*  time in forever, it's possible for an underlying microscopic theory to imply special relativity,
*  to be able to derive it. It's not something you put in as a, this is a, it's something where
*  this other property, causal invariance, which is also the property that implies that there's a
*  single thread of time in the universe. It might not be the case that that's, that is the, that's what
*  would lead to the possibility of an observer thinking that definite stuff happens. Otherwise,
*  you've got all these possible rewriting orders, and who's to say which one occurred. But with this
*  causal invariance property, there's a, there's a notion of a definite thread of time.
*  It sounds like that that kind of idea of time, even space would be emergent from the system.
*  Oh yeah. No, I mean-
*  So it's not a fundamental part of the system.
*  No, no. The fundamental level, all you've got is a bunch of nodes connected by hyper edges or
*  whatever. So there's no time, there's no space.
*  That's right. And, but the, the thing is that it's just like imagining, imagine you're just
*  dealing with a graph and imagine you have something like a, you know, like a honeycomb graph where you
*  have a hexagon, a bunch of hexagons. You know, that graph at a microscopic level, it's just a bunch
*  of nodes connected to other nodes. But at a macroscopic level, you say that looks like a
*  honeycomb, you know, it's lattice. It looks like a two-dimensional, you know, manifold of some kind.
*  It looks like a two-dimensional thing. If you connect it differently, if you just connect all
*  the nodes, one, one to another, and kind of a sort of linked list type structure, then you'd say,
*  well, that looks like a one-dimensional space. But at the microscopic level, all these are just
*  networks with nodes. The macroscopic level, they look like something that's like one of our sort
*  of familiar kinds of space. And it's the same thing with these hyper graphs. Now, if you ask me,
*  have I found one that gives me three-dimensional space? The answer is not yet. So we don't know,
*  you know, this is one of these things we're kind of betting against nature, so to speak.
*  And I have no way to know. And so there are many other properties of this, this kind of system
*  that have a very beautiful actually, and very suggestive, and it will be very elegant, if this
*  turns out to be right, because it's very, it's very clean. I mean, you start with nothing,
*  and everything gets built up, everything about space, everything about time, everything about
*  matter. It's all just emergent from the properties of this extremely low level system. And that,
*  that will be pretty cool if that's the way our universe works. Now, do I, on the other hand,
*  the thing that, that I find very confusing is, let's say we succeed, let's say we can say,
*  this particular sort of hypergraphy writing rule gives the universe, just run that hypergraphy
*  writing rule for enough times, and you'll get everything, you'll get this conversation we're
*  having, you'll get everything. It's that if we get to that point, and we look at what is this thing,
*  what is this rule that we just have, that is giving us our whole universe? How do we think
*  about that thing? Let's say, turns out the minimal version of this, and this is kind of
*  cool thing for a language designer like me, the minimal version of this model is actually a single
*  line of orphan language code. So that's, which I wasn't sure was going to happen that way. But
*  it's, it's a, that's, it's kind of, no, we don't know what, we don't know what, that's, that's just
*  the framework to know the actual particular hypergraph that might be a longer, that the
*  specification of the rules might be slightly longer. How does that help you accept marveling
*  in the beauty and the elegance of the simplicity that creates the universe? That does that help
*  us predict anything? Not really, because of the irreducibility. That's correct. That's correct.
*  But so the thing that is really strange to me, and I haven't wrapped my brain around this yet,
*  is, you know, one is, one keeps on realizing that we're not special in the sense that,
*  you know, we don't live at the center of the universe, we don't blah, blah, blah.
*  And yet, if we produce a rule for the universe, and it's quite simple, and we can write it down
*  and couple of lines or something, that feels very special. How do we come to get a simple universe,
*  when many of the available universes, so to speak, are incredibly complicated, might be,
*  you know, a quintillion characters long? Why did we get one of the ones that's simple?
*  And so I haven't wrapped my brain around that issue yet.
*  If indeed we are in such a simple, the universe is such a simple rule, is it possible that
*  there is something outside of this, that we are in a kind of what people call the simulation,
*  right? Where just part of a computation is being explored by a graduate student in an alternate
*  universe. Well, you know, the problem is, we don't get to say much about what's outside our universe,
*  because by definition, our universe is what we exist within. Now, can we make a sort of almost
*  theological conclusion from being able to know how our particular universe works? Interesting question.
*  I don't think that if you ask the question, could we, and it relates again to this question about
*  extraterrestrial intelligence, you know, we've got the rule for the universe. Was it built on purpose?
*  Hard to say. That's the same thing as saying we see a signal from, you know, that we're, you know,
*  receiving from some, you know, random star somewhere, and it's a series of pulses. And,
*  you know, it's a periodic series of pulses, let's say. Was that done on purpose? Can we conclude
*  something about the origin of that series of pulses? Just because it's elegant does not
*  necessarily mean that somebody created it or that we can even comprehend what we created. Yeah,
*  I mean, I think it's the ultimate version of the sort of identification of the technosignature
*  question. It's the ultimate version of that is, was our universe a piece of technology, so to speak,
*  and how on earth would we know? Because, but I mean, it'll be, it's, I mean, you know, in the kind
*  of crazy science fiction thing you could imagine, you could say, oh, somebody's going to have,
*  you know, there's going to be a signature there. It's going to be, you know, made by so and so.
*  But there's no way we could understand that, so to speak, and it's not clear what that would mean,
*  because the universe simply, you know, this, if we find a rule for the universe,
*  we're not, we're simply saying that rule represents what our universe does. We're not saying
*  that that rule is something running on a big computer and making our universe. It's just saying
*  that represents what our universe does in the same sense that, you know, laws of classical mechanics,
*  differential equations, whatever they are, represent what mechanical systems do. It's not that
*  the mechanical systems are somehow running solutions to those differential equations.
*  Those differential equations just representing the behavior of those systems.
*  So what's the gap in your sense to linger on the fascinating, perhaps slightly sci-fi question?
*  What's the gap between understanding the fundamental rules that create a universe and
*  engineering a system, actually creating a simulation ourselves? So you've talked about sort of,
*  you've talked about, you know, nano engineering kind of ideas that are kind of exciting, actually
*  creating some ideas of computation in the physical space. How hard is it as an engineering
*  problem to create the universe once you know the rules that create it? Well, that's an interesting
*  question. I think the substrate on which the universe is operating is not a substrate that
*  we have access to. I mean, the only substrate we have is that same substrate that the universe is
*  operating in. So if the universe is a bunch of hypergraphs being rewritten, then we get to
*  attach ourselves to those same hypergraphs being rewritten. We don't get to, and if you ask the
*  question, you know, is the code clean? You know, can we write nice elegant code with efficient
*  algorithms and so on? Well, that's an interesting question. That's this question of how much
*  computational reducibility there is in the system. So I've seen some beautiful cellular automata that
*  basically create copies of itself within itself, right? So that's the question whether it's possible
*  to create, like whether you need to understand the substrate or whether you can just... Yeah,
*  well, right. I mean, so one of the things that is sort of one of my slightly sci-fi
*  thoughts about the future, so to speak, is, you know, right now, if you poll typical people,
*  you say, do you think it's important to find the fundamental theory of physics?
*  You get, because I've done this poll informally, at least, it's curious, actually, you get a decent
*  fraction of people saying, oh, yeah, that would be pretty interesting. I think that's becoming
*  surprisingly enough more, I mean, a lot of people are interested in physics in a way that, like,
*  without understanding it, just kind of watching scientists, a very small number of them,
*  struggle to understand the nature of our reality. Right. I mean, I think that's somewhat true. And
*  in fact, in this project that I'm launching into to try and find the fundamental theory of physics,
*  I'm going to do it as a very public project. I mean, it's going to be live streamed and all
*  this kind of stuff. I don't know what will happen. It'll be kind of fun. I mean, I think that it's
*  the interface to the world of this project. I mean, I figure one feature of this project is,
*  you know, unlike technology projects that basically are what they are, this is a project that might
*  simply fail because it might be the case that it generates all kinds of elegant mathematics,
*  that has absolutely nothing to do with the physical universe that we happen to live in.
*  Okay, so we're talking about kind of the quest to find the fundamental theory of physics.
*  First point is, you know, it's turned out it's kind of hard to find the fundamental theory of
*  physics. People weren't sure that that would be the case. Back in the early days of applying
*  mathematics to science, 1600s and so on, people were like, oh, in 100 years, we'll know everything
*  there is to know about how the universe works. Turned out to be harder than that. And people
*  got kind of humble at some level, because every time we got to sort of a greater level of smallness
*  and studying the universe, it seemed like the math got more complicated and everything got harder.
*  The, you know, when I was a kid, basically, I started doing particle physics. And, you know,
*  when I was doing particle physics, I always thought finding the fundamental fundamental theory of
*  physics, that's a kooky business, we'll never be able to do that. But we can operate within these
*  frameworks that we built for doing quantum field theory and general relativity and things like this,
*  and it's all good. And we can figure out a lot of stuff.
*  Did you even at that time have a sense that there's something behind that?
*  Sure, sure. I just didn't expect that. I thought, in some rather un, it's actually kind of crazy,
*  and thinking back on it, because it's kind of like there was this long period in civilization
*  where people thought the ancients had it all figured out, and we'll never figure out anything
*  new. And to some extent, that's the way I felt about physics when I was in the middle of doing
*  it, so to speak, was, you know, we've got quantum field theory, it's the foundation of what we're
*  doing. And there's, you know, yes, there's probably something underneath this, but we'll sort of never
*  figure it out. But then I started studying simple programs in the computational universe, things
*  like cellular automata, and so on. And I discovered that there's they do all kinds of things that were
*  completely at odds with the intuition that I had had. And so after that, after you see this tiny
*  little program that does all this amazingly complicated stuff, then you start feeling a bit
*  more ambitious about physics and saying, maybe we could do this for physics, too. And so that's,
*  that got me started years ago now, and this kind of idea of could we actually find what's underneath
*  all of these frameworks like quantum field theory and general relativity and so on. And people
*  perhaps don't realize as clearly as they might that, you know, the frameworks we're using for
*  physics, which is basically these two things, quantum field theory, sort of the theory of small
*  stuff and general relativity, theory of gravitation and large stuff, those are the two basic theories,
*  and they're 100 years old. I mean, general relativity was 1915, quantum field theory, well,
*  1920s, so basically 100 years old. And they've, it's been a good run. There's a lot of stuff been
*  figured out. But what's interesting is the foundations haven't changed in all that period
*  of time, even though the foundations had changed several times before that in the 200 years earlier
*  than that. And I think the kinds of things that I'm thinking about, which are sort of really informed
*  by thinking about computation and the computational universe, it's a different foundation. It's a
*  different set of foundations and might be wrong, but it is at least, you know, we have a shot.
*  And I think it's, you know, to me, it's, you know, my personal calculation for myself is,
*  is, you know, if it turns out that the finding the fundamental theory of physics, it's kind of
*  low hanging fruit, so to speak, it'd be a shame if we just didn't think to do it. You know, if
*  people just said, oh, you'll never figure that stuff out. Let's, you know, and it takes another
*  200 years before anybody gets around to doing it. You know, I think it's, I don't know how low
*  hanging this fruit actually is. It may be, you know, it may be that it's kind of the wrong
*  century to do this project. I mean, I think the, the, the cautionary tale for me, you know, I think
*  about things that I've tried to do in technology, where people thought about doing them a lot earlier.
*  My favorite example is probably Leibniz, who, who thought about making essentially,
*  encapsulating the world's knowledge in a computational form in the late 1600s, and
*  did a lot of things towards that. And basically, you know, we finally managed to do this,
*  but he was 300 years too early. And that's the, that's kind of the, in terms of life planning,
*  it's kind of like, avoid things that can't be done in your, in your century, so to speak.
*  Yeah, timing, timing is everything. So you think if we kind of figure out the underlying rules it
*  can create from which quantum field theory and general relativity can emerge, do you think they'll
*  help us unify it at that level of abstraction? Oh, we'll know it completely. We'll know how that
*  all fits together. Yes, without a question. And I mean, it's already, even the things I've already
*  done, there are very, you know, it's very, very elegant, actually, how, how things seem to be
*  fitting together. Now, you know, is it right? I don't know yet. It's awfully suggestive. If it
*  isn't right, it's then the designer of the universe should feel embarrassed, so to speak,
*  because it's a really good way to do it. And your intuition in terms of designing universe,
*  does God play dice? Is there, is there randomness in this thing? Or is it deterministic? So the
*  kind of, that's a little bit of a complicated question, because when you're dealing with these
*  things that involve these rewrites that have, okay, even randomness is an emergent phenomenon.
*  Perhaps. Yes. I mean, it's a yeah, well, randomness in many of these systems, pseudo randomness and
*  randomness are hard to distinguish. In this particular case, the current idea that we have
*  about measurement and quantum mechanics is something very bizarre and very abstract. And
*  I don't think I can yet explain it without kind of yakking about very technical things. Eventually,
*  I will be able to. But if that's right, it's kind of a, it's a weird thing, because it slices between
*  determinism and randomness in a weird way that hasn't been sliced before, so to speak. So like
*  many of these questions that come up in science, where it's like, is it this or is it that? Turns
*  out the real answer is it's neither of those things. It's something kind of different and
*  sort of orthogonal to those categories. And so that's the current, this week's idea about how
*  that might work. But we'll see how that unfolds. I mean, there's this question about a field like
*  physics and sort of the quest for fundamental theory and so on. And there's both the science
*  of what happens and there's the sort of the social aspect of what happens. Because in a field that is
*  basically as old as physics, we're at, I don't know what it is, fourth generation, I don't know,
*  fifth generation, I don't know what generation it is of physicists. And like, I was one of these,
*  so to speak. And for me, the foundations were like the pyramid, so to speak, you know, it was that
*  way. And it was always that way. It is difficult in an old field to go back to the foundations and
*  think about rewriting them. It's a lot easier in young fields where you're still dealing with the
*  first generation of people who invented the field. And it tends to be the case, you know,
*  that the nature of what happens in science tends to be, you know, you'll get, typically the pattern
*  is some methodological advance occurs. And then there's a period of five years, 10 years, maybe a
*  little bit longer than that, where there's lots of things that are now made possible by that,
*  by that methodological advance, whether it's, you know, I don't know, telescopes, or whether that's
*  some mathematical method or something. It's, you know, there's a something, something happens,
*  a tool gets built, and then you can do a bunch of stuff. And there's a bunch of low hanging fruit
*  to be picked. And that takes a certain amount of time. After that, all that low hanging fruit is
*  picked, then it's a hard slog for the next however many decades, or century or more to get to the
*  next sort of level at which one can do something. And it's kind of a, a, and it tends to be the case
*  that in fields that are in that kind of, I wouldn't say cruise mode, because it's really hard work,
*  but it's very hard work for very incremental progress. And then in your career, and some of
*  the things you've taken on, it feels like you're not, you haven't been afraid of the hard slog.
*  Yeah, that's true. So it's quite interesting, especially on the engineering,
*  on the engineering side. And a small tangent, when you were at Caltech, did you get to
*  interact with Richard Feynman at all? Do you have any memories of Richard?
*  We worked together quite a bit, actually. In fact, on, and in fact, both when I was at Caltech,
*  and after I left Caltech, we were both consultants at this company called Thinking Machines
*  Corporation, which was just down the street from here, actually, as ultimately ill fated company.
*  But I used to say this company is not going to work with the strategy they have. And Dick
*  Feynman always used to say, what do we know about running companies, just let them run their company.
*  Anyway, I was, he was not into into that kind of thing. And he always thought he always thought
*  that my interest in doing things like running companies was a was a distraction, so to speak.
*  And I, for me, it's a, it's a mechanism to have a more effective machine for actually
*  getting things, figuring things out and getting things to happen.
*  Did he think of it because essentially what you used, you did with the company, I don't know if
*  you were thinking of it that way, but you're creating tools to empower your, to empower the
*  exploration of the university. Do you think, did he? Did he understand that point?
*  The point of tools of? I think not as well as he might have done. I mean, I think that,
*  but, you know, he was actually my first company, which was also involved with, well,
*  was involved with more mathematical computation kinds of things. You know, he was quite,
*  he had lots of advice about the technical side of what we should do and so on.
*  Do you have examples of memories of thoughts that?
*  Oh, yeah, yeah. He had all kinds of lucky in, in the business of doing sort of, you know,
*  one of the hard things in math is doing integrals and so on. Right. And so he had his own elaborate
*  ways to do integrals and so on. He had his own ways of thinking about sort of getting intuition
*  about how math works. And so his sort of meta idea was take those intuitional methods and make a
*  computer follow those intuitional methods. Now it turns out, for the most part, like when we do
*  integrals and things, what we do is, is we build this kind of bizarre industrial machine that turns
*  every integral into, you know, products of mayor G functions and generates this very elaborate thing.
*  And actually the big problem is turning the results into something a human will understand.
*  It's not quotes doing the integral. And actually Feynman did understand that to some extent. And I
*  am embarrassed to say I, he once gave me this big pile of, you know, calculational methods for
*  particle physics that he worked out in the fifties. And he said, yeah, it's more used to you than to
*  me type thing. And I, I was like, I've intended to look at it and give it back. And I still in my
*  files now. So it's, but that's what happens when, when it's finiteness of human lives. It's,
*  I, you know, maybe if you'd lived another 20 years, I would have, I would have remembered to
*  give it back. But I think it's, you know, that, that was his attempt to systematize
*  the ways that one does integrals that show up in particle physics and so on. Turns out the way
*  we've actually done it is very different from that way. What do you make of that difference to
*  Gene? So Feynman was actually quite remarkable at creating sort of intuitive, like diving in,
*  you know, creating intuitive frameworks for understanding difficult concepts is.
*  I'm smiling because, you know, the funny thing about him was that the thing he was really,
*  really, really good at is calculating stuff. And, but he thought that was easy
*  because he was really good at it. And so he would do these things where he would calculate some,
*  uh, do some complicated calculation and quantum field theory, for example, come out with a result,
*  wouldn't tell anybody about the complicated calculation because he thought that was easy.
*  He thought the really impressive thing was to have this simple intuition about how everything
*  works. So he invented that at the end. And, you know, because he'd done this calculation and knew
*  how it worked, it was a lot easier. It's a lot easier to have good intuition when you know what
*  the answer is. And then, and then he would just not tell anybody about these calculations. And he
*  wasn't meaning that maliciously, so to speak. It's just, he thought that was easy. Um, and, uh,
*  and that's, you know, that led to areas where people were just completely mystified and they
*  kind of followed his intuition, but nobody could tell why it worked because actually the reason it
*  worked was because he'd done all these calculations and he knew that it was would work. And, you know,
*  when I, he and I worked a bit on quantum computers, actually back in 1980, 81, um, before anybody had
*  heard of those things and, you know, the typical mode of, um, um, I mean, he always used to say,
*  and I now think about this because I'm about the age that he was when I worked with him. And,
*  you know, I see the people who are one third my age, so to speak. And he was always complaining
*  that I was one third his age and therefore various things, but, but, um, you know, he would do some
*  calculation by, by hand, you know, blackboard and things, come up with some answer. I'd say,
*  I don't understand this. You know, I do something with a computer and he'd say, you know,
*  I don't understand this. So it'd be some big argument about what was, you know, what was
*  going on, but, but it was always, um, uh, and I think actually we, the, many of the things that
*  we sort of realized about quantum computing that was sort of issues that have to do particularly
*  with the measurement process are kind of still issues today. And I kind of find it interesting.
*  It's a funny thing in science that these, you know, that there's, uh, there's a remarkable,
*  it happens in technology too. There's a remarkable sort of repetition of history
*  that ends up occurring. Um, eventually things really get nailed down, but it often takes a
*  while and it often things come back decades later. Um, well, for example, I could tell a story
*  actually happened right down the street from here. Um, uh, when we were both at thinking machines,
*  I had been working on this particular cellular automaton called rule 30 that has this feature
*  that it, from very simple initial conditions, it makes really complicated behavior. Okay.
*  So, and actually of all silly physical things, uh, using this big parallel computer called the
*  connection machine that that company was making, I generated this giant printout of rule 30 on very,
*  I'm actually on the same kind of, um, same kind of printer that people use to make, um, uh, uh,
*  layouts, microprocessors. So one of these big, you know, large format printers with a high resolution
*  and so on. So, okay, so print this out lots of very tiny cells. And, um, so there was sort of
*  a question of, of how, um, uh, some features of that pattern. And so it was very much a physical,
*  you know, on the floor with meter rules, trying to measure different things. So, so Feynman kind
*  of takes me aside. We've been doing that for a little while and takes me aside and he says,
*  I just want to know this one thing. He says, I want to know, how did you know that this rule 30
*  thing would produce all this really complicated behavior that is so complicated that we're, you
*  know, going around with this big printout and so on. And I said, well, I didn't know. I just
*  enumerated all the possible rules and then observed that that's what happened. He said,
*  Oh, I feel a lot better. You know, I thought you had some intuition that he didn't have that would
*  let one. I said, no, no, no, no intuition, just experimental science. So that's such a beautiful
*  sort of dichotomy there of that's exactly what you showed is you really can't have an intuition
*  about in your reducible. I mean, you have to run it. Yes, that's right. That's so hard for us humans
*  and especially brilliant physicists like Feynman to say that you can't have a compressed,
*  clean intuition about how the whole thing. Yes. Works. Yes. No, he was, I mean, I think he was
*  sort of on the edge of understanding that point about computation. And I think he found that
*  I think he always found computation interesting. And I think that was sort of what he was a little
*  bit poking at. I mean, that intuition, you know, the difficulty of discovering things,
*  like even you say, Oh, you know, you just didn't write all the cases and just find one that does
*  something interesting, right? Sounds very easy. Turns out like I missed it when I first saw it,
*  because I had kind of an intuition that said it shouldn't be there. And so I had kind of arguments,
*  Oh, I'm going to ignore that case because whatever. And how did you have an open mind enough?
*  Because you're essentially the same person as Richard, like the same kind of physics
*  type of thinking. How did you find yourself having a sufficiently open mind to be open to watching
*  rules and them revealing complexity? Yeah, I think that's an interesting question. I've
*  wondered about that myself, because it's kind of like, you know, you live through these things,
*  and then you say, what was the historical story? And sometimes the historical story that you realize
*  after the fact was not what you lived through, so to speak. And so, you know, what I realized is,
*  I think what happened is, you know, I did physics, kind of like reductionistic physics,
*  where you're throwing the universe and you're told, go figure out what's going on inside it.
*  And then I started building computer tools. And I started building my first computer language,
*  for example, and computer language is not like it's sort of like physics in the sense that you
*  have to take all those computations people want to do, and kind of drill down and find the
*  primitives that they can all be made of. But then you do something that's really different,
*  because you're just saying, okay, these are the primitives. Now, you know, hopefully they'll be
*  useful to people, let's build up from there. So you're essentially building an artificial
*  universe in a sense, where you make this language, you've got these primitives,
*  you're just building whatever you feel like building. And so it was sort of interesting
*  for me, because from doing science, where you're just throwing the universe as the universe is,
*  to then just being told, you know, you can make up any universe you want.
*  And so I think that experience of making a computer language, which is essentially building
*  your own universe, so to speak, is, you know, that's kind of the that's, that's what gave me
*  a somewhat different attitude towards what might be possible. It's like, let's just explore what
*  can be done in these artificial universes, rather than thinking the natural science way of let's be
*  constrained by how the universe actually is. Yeah, by being able to program, essentially, you've,
*  as opposed to being limited to just your mind and a pen, you now have, you've basically built
*  another brain that you can use to explore the universe by computer program, you know,
*  this is kind of a brain. Right. And it's well, it's, it's or telescope or, you know, it's a tool,
*  it lets you let's you see stuff, but there's something fundamentally different between a
*  computer and a telescope. I mean, it just, yeah, I'm hoping romanticize the notion, but it's more
*  general. It's more general, more general. And it's, it's, I think, I mean, this point about,
*  you know, people say, oh, such and such a thing was almost discovered at such and such a time,
*  the, the distance between, you know, the building the paradigm that allows you to actually understand
*  stuff or allows one to be open to seeing what's going on. That's really hard. And, you know, I
*  think in, I've been fortunate in my life that I've spent a lot of my time building computational
*  language. And that's an activity that in a sense works by sort of having to kind of create another
*  level of abstraction and kind of be open to different kinds of structures. But, you know,
*  it's, it's always, I mean, I'm fully aware of, I suppose, the fact that I have seen it a bunch
*  of times of how easy it is to miss the obvious, so to speak, that at least is factored into
*  my attempt to not miss the obvious, although it may not succeed.
*  What do you think is the role of ego in the history of math and science? And more sort of,
*  you know, a book title is something like A New Kind of Science. You've accomplished a huge amount.
*  In fact, somebody said that Newton didn't have an ego and I looked into it and he had a huge ego.
*  Yeah. But from an outsider's perspective, some have said that you have a bit of an ego as well.
*  Do you see it that way? Does ego get in the way? Is it empowering? Is it both sort of?
*  Oh, it's complicated and necessary. I mean, you know, I've had, look, I've spent more than half
*  my life CEOing a tech company. Right. Okay. And, you know, that is a, I think it's actually very,
*  it means that one's ego is not a distant thing. It's a thing that one encounters every day,
*  so to speak, because it's all tied up with leadership and with how one, you know, develops
*  an organization and all these kinds of things. So, you know, it may be that if I've been an
*  academic, for example, I could have sort of, you know, check the ego, put it on, put it on a shelf
*  somewhere and ignore its characteristics. But you're reminded of it quite often in the context of
*  running a company. Sure. I mean, that's what it's about. It's about leadership and, you know,
*  leadership is intimately tied to ego. Now, what does it mean? I mean, what is the, you know, for me,
*  I've been fortunate that I think I have reasonable intellectual confidence, so to speak.
*  That is, you know, I'm one of these people who at this point, if somebody tells me something,
*  I just don't understand it. My conclusion isn't that means I'm dumb. That my conclusion is there's
*  something wrong with what I'm being told. And that was actually Dick Feynman used to have that,
*  that, that feature too. He never really believed in, he actually believed in experts much less than
*  I believe in experts. So, um, wow. So that's a fun, that's a, that's a fundamentally powerful
*  property of ego and saying like, not that I am wrong, but that the world is wrong and telling me
*  like when confronted with the fact that doesn't fit the thing that you've really thought through
*  sort of both the negative and the positive of ego, do you see the negative of that get in the way
*  sort of being confronted with- Sure, there are mistakes I've made that are the result of,
*  I'm pretty sure I'm right and turns out I'm not. I mean, that's, that's the, you know, but,
*  but the thing is that the, the, the idea that one tries to do things that, so for example, you know,
*  one question is that people have tried hard to do something and then one thinks maybe I should try
*  doing this myself. Uh, if one does not have a certain degree of intellectual confidence,
*  one just says, well, people have been trying to do this for a hundred years. How am I going to be
*  able to do this? And, you know, I was fortunate in the sense that I happened to start having some
*  degree of success in science and things when I was really young. And so that developed a certain
*  amounts of sort of intellectual confidence. I don't think I otherwise would have had. Um, and,
*  you know, in a sense, I mean, I was fortunate that I was working in a field particle physics
*  during its sort of golden age of rapid progress. And that, that's kind of gives one a false sense
*  of, uh, achievement because it's kind of, it's kind of easy to discover stuff that's going to
*  survive if you happen to be, you know, picking the low hanging fruit of a rapidly expanding field.
*  And the reason I totally, I totally immediately understood the ego behind a new kind of science
*  to me, let me sort of just try to express my feelings on the whole thing is that if you don't
*  allow that kind of ego, then you would never write that book that you would say, well,
*  people must've done this. There's not, you would not dig. You would not keep digging.
*  And I think that was, I think you have to take that ego and ride it and see where it takes you.
*  And that's how you create exceptional work. I think the other point about that book was,
*  it was a non-trivial question how to take a bunch of ideas that are, I think, reasonably big ideas.
*  They might, you know, their importance is determined by what happens historically. One
*  can't tell how important they are. One can tell sort of the scope of them. And the scope is fairly
*  big and they're very different from things that have come before. And the question is, how do you
*  explain that stuff to people? And so I had had the experience of sort of saying, well, there are
*  these things, there's a cellular automaton, it does this, it does that. And people are like,
*  oh, it must be just like this. It must be just like that. I said, no, it isn't. It's something
*  different. Right? And so I could have done sort of, I'm really glad you did what you did, but you
*  could have done sort of academically just publish, keep publishing small papers here and there.
*  And then you would just keep getting this kind of resistance, right? You would get like,
*  it's supposed to just dropping a thing that says here it is. Here's the full thing.
*  No, I mean, that was my calculation is that basically, you know, you could introduce little
*  pieces. It's like, you know, one possibility is like, it's the secret weapon, so to speak.
*  It's this, you know, I keep on, you know, discovering these things in all these different
*  areas. Where'd they come from? Nobody knows. But I decided that, you know, in the interests of one
*  only has one life to lead him, you know, the writing that book took me a decade anyway. It's
*  not, there's not a lot of wiggle room, so to speak. One can't be wrong by a factor of three,
*  so to speak, and how long it's going to take that I, you know, I thought the best thing to do,
*  the thing that is most sort of, that most respects the, the intellectual content, so to speak,
*  is you just put it out with as much force as you can, because it's not something where, and, you
*  know, it's an interesting thing. You talk about ego and it's, it's, you know, for example, I run
*  a company which has my name on it, right? I thought about starting a club for people whose
*  companies have their names on them. And it's, it's a funny group because we're not a bunch of
*  egomaniacs. That's not what it's about, so to speak. It's about basically sort of taking
*  responsibility for what one's doing. And, you know, in a sense, any of these things where you're sort
*  of putting yourself on the line, it's kind of a funny, it's a funny dynamic because, in a sense,
*  my company is sort of something that happens to have my name on it, but it's kind of bigger than
*  me and I'm kind of just its mascot at some level. I mean, I also happen to be a pretty, you know,
*  strong leader of it, but- But it's basically showing a deep,
*  inextricable sort of investment. The same, your name, like Steve Jobs' name wasn't on Apple,
*  but he was Apple. Yes. Elon Musk's name is not on Tesla, but he is Tesla. So it's like, meaning
*  emotionally. If a company succeeds or fails, he would just, that emotionally would suffer through
*  that. And so that's- Yeah, it's recognizing that fact. And also Wolfram is a pretty good branding
*  name, so it works out. Yeah, right, exactly. I think Steve had it, had a bad deal there.
*  Yeah, so you made up for it with the last name. Okay, so in 2002, you published a new kind of
*  science to which sort of on a personal level, I can credit my love for cellular automata and
*  computation in general. I think a lot of others can as well. Can you briefly describe the vision,
*  the hope, the main idea presented in this 1200-page book?
*  Sure. Although it took 1200 pages to say in the book, so no, the real idea, it's kind of
*  a good way to get into it is to look at sort of the arc of history and to look at what's happened
*  in kind of the development of science. I mean, there was this sort of big idea in science about
*  300 years ago that was, let's use mathematical equations to try and describe things in the world.
*  Let's use sort of the formal idea of mathematical equations to describe what might be happening in
*  the world rather than, for example, just using sort of logical augmentation and so on. Let's have a
*  formal theory about that. And so there'd been this 300-year run of using mathematical equations
*  to describe the natural world, which had worked pretty well. But I got interested in how one could
*  generalize that notion. There is a formal theory, there are definite rules, but what structure could
*  those rules have? And so what I got interested in was let's generalize beyond the sort of purely
*  mathematical rules. And we now have this sort of notion of programming and computing and so on.
*  Let's use the kinds of rules that can be embodied in programs to as a sort of generalization of the
*  ones that can exist in mathematics as a way to describe the world. And so my kind of favorite
*  version of these kinds of simple rules are these things called cellular automata. And so typical
*  case- So wait, what are cellular automata? Fair enough. So typical case of a cellular automaton,
*  it's an array of cells. It's just a line of discrete cells. Each cell is either black or
*  white. And in a series of steps that you can represent as lines going down a page,
*  you're updating the color of each cell according to a rule that depends on the color of the cell
*  above it and to its left and right. So it's really simple. So a thing might be, you know, if
*  the cell and its right neighbor are not the same and or the cell on the left is black or something,
*  then make it black on the next step. And if not, make it white. Typical rule. That rule, I'm not
*  sure I said it exactly right, but a rule very much like what I just said has the feature that if you
*  started off from just one black cell at the top, it makes this extremely complicated pattern.
*  So some rules, you get a very simple pattern. Some rules, you have the rule is simple, you start
*  them off from a sort of simple seed, you just get this very simple pattern. But other rules,
*  and this was the big surprise when I started actually just doing the simple computer experiments
*  to find out what happens is that they produce very complicated patterns of behavior. So for
*  example, this rule 30 rule has the feature you started off from just one black cell at the top,
*  makes this very random pattern. If you look like at the center column of cells,
*  you get a series of values, you know, it goes black, white, black, black, whatever it is,
*  that sequence seems for all practical purposes random. So it's kind of like in math, you know,
*  you compute the digits of pi 3.1415926, whatever. Those digits once computed, I mean,
*  the scheme for computing pi, you know, it's the ratio of the circumference, the diameter of a
*  circle, very well defined. But yet, once you've generated those digits, they seem for all practical
*  purposes completely random. And so it is with rule 30, that even though the rule is very simple,
*  much simpler, much more sort of computationally obvious than the rule for generating digits of pi,
*  even with a rule that simple, you're still generating immensely complicated behavior.
*  Yeah. So if we could just pause on that, I think you've probably said it and looked at it so long,
*  you forgot the magic of it, or perhaps you don't, you still feel the magic. But to me,
*  if you've never seen sort of, I would say, what is it, a one dimensional, essentially,
*  solar automata, right? And you were to guess what you would see if you have some
*  sort of cells that only respond to its neighbors. If you were to guess what kind of things you would
*  see, like my initial guess, like even when I first like opened your book, A New Kind of Science,
*  right? My initial guess is you would see, I mean, it would be very simple stuff.
*  Right. And I think it's a magical experience to realize the kind of complexity you mentioned,
*  rule 30, still your favorite cellular automaton? Still my favorite rule, yes.
*  You get complexity, immense complexity, you get arbitrary complexity. And when you say randomness
*  down the middle column, that's just one cool way to say that there's incredible complexity. And
*  that's just, I mean, that's a magical idea. However you start to interpret it, all the
*  irreducibility discussions, all that, but it's just, I think that has profound philosophical
*  kind of notions around it too. It's not just, I mean, it's transformational about how you see
*  the world. I think for me it was transformational. I don't know, we can have all kinds of discussions
*  about computation and so on, but just, I sometimes think if I were on a desert island
*  and was, I don't know, maybe it was some psychedelics or something, but if I had to take
*  one book, I mean, A New Kind of Science would be it, because you could just enjoy that notion.
*  For some reason it's a deeply profound notion, at least to me.
*  I find it that way, yeah. I mean, look, it's been, it was a very intuition-breaking
*  thing to discover. I mean, it's kind of like, you point the computational telescope out there,
*  and suddenly you see, I don't know, in the past it's kind of like moons of Jupiter or something,
*  but suddenly you see something that's kind of very unexpected. And rule 30 was very unexpected
*  for me. And the big challenge at a personal level was to not ignore it. I mean, people,
*  in other words, you might say- It's a bug. What would you say?
*  Yeah, I mean, I- What are we looking at, by the way?
*  Well, I was just generating here, I'll actually generate a rule 30 pattern. So that's the rule
*  for rule 30. And it says, for example, it says here, if you have a black cell in the middle,
*  and a black cell to the left, and a white cell to the right, then the cell on the next step will be
*  white. And so here's the actual pattern that you get starting off from a single black cell
*  at the top there. And then- That's the initial state, initial condition.
*  That's the initial thing. You just start off from that, and then you're going down the page.
*  And at every step, you're just applying this rule to find out the new value that you get.
*  And so you might think, rule that simple, you've got to get that there's got to be some trace of
*  that simplicity here. Okay, we'll run it, let's say, for 400 steps. That's what it does. It's
*  kind of aliasing a bit on the screen there. But you can see there's a little bit of regularity
*  over on the left. But there's a lot of stuff here that just looks very complicated, very random.
*  And that's a big sort of shock to, was a big shock to my intuition, at least, that that's possible.
*  The mind immediately starts, is there a pattern? There must be a repetitive pattern.
*  Yeah, well, so I spent, so indeed, that's what I thought at first. And I thought,
*  I thought, well, this is kind of interesting. But you know, if we run it long enough, we'll see,
*  you know, something will resolve into something simple. And, you know, I did all kinds of analysis
*  of using mathematics, statistics, cryptography, whatever, whatever, to try and crack it. And I
*  never succeeded. And after I hadn't succeeded for a while, I started thinking, maybe there's a real
*  phenomenon here. That is the reason I'm not succeeding. Maybe, I mean, the thing that for
*  me was sort of a motivating factor was looking at the natural world and seeing all this complexity
*  that exists in the natural world. The question is, where does it come from? You know, what secret
*  does nature have that lets it make all this complexity that we humans, when we engineer things,
*  typically, are not making? We're typically making things that at least look quite simple to us.
*  And so the shock here was, even from something very simple, you're making something that complex.
*  Maybe this is getting at sort of the secret that nature has that allows it to make really complex
*  things, even though its underlying rules may not be that complex. How did it make you feel? If we
*  look at the Newton apple, was there, was there, you know, you took a walk and something profoundly
*  hit you? Or was this a gradual thing? A lobster being boiled? The truth of every sort of science
*  discovery is it's not that gradual. I mean, I've spent, I happen to be interested in scientific
*  biography kinds of things. And so I've tried to track down, you know, how did people come to figure
*  out this or that thing? And there's always a long kind of sort of preparatory, you know,
*  there's a need to be prepared and a mindset in which it's possible to see something. I mean,
*  in the case of Rule 30, I realize around June 1st, 1984, was kind of a silly story. In some ways,
*  I finally had a high resolution laser printer. So I was able, so I thought I'm going to generate a
*  bunch of pictures of the cellular automata and I generate this one and I put it on some plane
*  flight to Europe and have this with me. And it's like, you know, I really should try to understand
*  this. And this is really, you know, this is, I really don't understand what's going on. And that
*  was kind of the, you know, slowly trying to see what was happening. It was not, it was depressingly
*  unsubstantialized, so to speak, in the sense that a lot of these ideas, like principle of
*  computational equivalence, for example, you know, I thought, well, that's a possible thing. I didn't
*  know if it's correct. Still don't know for sure that it's correct. But it's sort of a gradual thing
*  that these things gradually kind of become seem more important than one thought. I mean, I think
*  the whole idea of studying the computational universe of simple programs, it took me probably
*  decade, decade and a half to kind of internalize that that was really an important idea.
*  And I think, you know, if it turns out we find the whole universe lurking out there in the
*  computational universe, that's a good, you know, it's a good brownie point or something for the
*  whole idea. But I think that the thing that's strange in this whole question about, you know,
*  finding this different raw material for making models of things. What's been interesting sort
*  of in the in sort of arc of history is, you know, for 300 years, it's kind of like the
*  the mathematical equations approach. It was the winner. It was the thing, you know, you want to
*  have a really good model for something that's what you use. The thing that's been remarkable is just
*  in the last decade or so, I think one can see a transition to using not mathematical equations,
*  but programs as sort of the raw material for making models of stuff. And that's pretty neat.
*  And it's kind of, you know, as somebody who's kind of lived inside this paradigm shift, so to speak,
*  it is bizarre. I mean, no doubt in sort of the history of science that will be seen as an
*  instantaneous paradigm shift. But it sure isn't instantaneous when it's played out in one's actual
*  life, so to speak, it seems glacial. And it's the kind of thing where, where it's sort of interesting
*  because in the dynamics of sort of the adoption of ideas like that, into different fields,
*  the younger the field, the faster the adoption typically, because people are not kind of locked
*  in with the fifth generation of people who've studied this field. And it is it is the way it
*  is and it can never be any different. And I think that's been, you know, watching that process
*  has been interesting. I mean, I'm, I think I'm fortunate that I've, I do stuff mainly because I
*  like doing it. And if I was, that makes me kind of thick skinned about the world's response to what I
*  do. And but that's definitely, you know, and anytime you, you write a book called something
*  like a new kind of science, it's kind of the pitchforks will come out for the for the old
*  kind of science. And I was it was interesting dynamics. I think that the I have to say that I
*  was fully aware of the fact that the when you see sort of incipient paradigm shifts in science,
*  the vigor of the negative response upon early introduction is a fantastic positive indicator
*  of good long term results. So in other words, if people just don't care, it's, you know, that's not
*  such a good sign. If they're like, Oh, this is great. That means you didn't really discover
*  anything interesting. What fascinating properties of rule 30 have you discovered over the years,
*  you've recently announced the rule 30 prizes for solving three key problems. Can you maybe
*  talk about interesting properties that have been kind of revealed rule 30 or other cellular
*  automata and what problems are still before us like the three problems you've announced?
*  Yeah, right. So I mean, the most interesting thing about cellular automata is that it's hard
*  to figure stuff out about them. And that's some in a sense, every time you try and sort of
*  you try and bash them with some other technique, you say, Can I crack them? The answer is they seem
*  to be uncrackable. They seem to have the feature that they are that they're sort of showing
*  irreducible computation. They're not, you're not able to say, Oh, I know exactly what this is going
*  to do. It's going to do this or that. But there's specific formulations of that fact. Yes, right. So
*  I mean, for example, in rule 30, in the pattern you get just starting from a single black cell,
*  you get this sort of very, very sort of random looking pattern. And so one feature of that,
*  just look at the center column. And for example, we use that for a long time to generate randomness
*  in wolfing language, just, you know, what rule 30 produces. The question is, can you prove how
*  random it is? So for example, one very simple question, can you prove that and never repeat?
*  We haven't been able to show that it will never repeat. We know that if there are two adjacent
*  columns, we know they can't both repeat. But just knowing whether that center column can ever repeat,
*  we still don't even know that. Another problem that I sort of put in my collection of, you know,
*  it's like $30,000 for three, you know, for these three prizes for about rule 30. I would say that
*  this is not one of those, there's one of those cases where the money is not the main point,
*  but it's just, you know, helps motivate somehow the investigation.
*  So there's three problems you propose to get $30,000 if you solve all three or maybe,
*  I don't know. No, it's 10,000 for each. For each, right.
*  That's right. Money is not the thing. The problems themselves are just clean
*  formulations of channel. It's just, you know, will it ever become periodic? Second problem is,
*  are there an equal number of black and white cells? Down the middle column. Down the middle column.
*  And the third problem is a little bit harder to state, which is essentially, is there a way
*  of figuring out what the color of a cell at position T down the center column is
*  with a less computational effort than about T steps? So in other words, is there a way to
*  jump ahead and say, I know what this is going to do. You know, it's just some mathematical
*  function of T. Or proving that there is no way.
*  Or proving there is no way. Yes. But both, I mean, you know, for any one of these, one could prove
*  that, you know, one could discover, you know, we know what rule 30 does for a billion steps,
*  and maybe we'll know for a trillion steps before too very long. But maybe at a quadrillion steps,
*  it suddenly becomes repetitive. You might say, how could that possibly happen? But so when I was
*  writing up these prizes, I thought, and this is typical of what happens in the computational
*  universe. I thought, let me find an example where it looks like it's just going to be random forever,
*  but actually it becomes repetitive. And I found one. And it's just, you know, I did a search,
*  I searched, I don't know, maybe a million different rules with some criterion. And this is,
*  what's sort of interesting about that is, I kind of have this thing that I say in kind of silly
*  way about the computational universe, which is, you know, the animals are always smarter than you
*  are. That is, there's always some way one of these computational systems is going to figure out how
*  to do something, even though I can't imagine how it's going to do it. And, you know, I didn't think
*  I would find one that, you know, you would think after all these years that when I found sort of
*  all possible things, funky things that I would have gotten my intuition wrapped around the idea
*  that, you know, these creatures are always in the computational universe, are always smarter than
*  I'm going to be. But, you know- Well, they're equivalent to the ESMART, right?
*  That's correct. And that makes it, that makes one feel very sort of, it's humbling every time,
*  because every time the thing is, you know, you think it's going to do this, or it's not going to
*  be possible to do this, and it turns out it finds a way. Of course, the promising thing is there's a
*  lot of other rules like rule 30. It's just rule 30 is- Oh, it's my favorite because I found it first.
*  And that's right. But the problems are focusing on rule 30. It's possible that rule 30 is repetitive
*  after a trillion steps. It is possible. And that doesn't prove anything about the other rules.
*  It does not. But this is a good sort of experiment of how you go about trying to prove something
*  about a particular rule. Yes. And it also, all these things help build intuition. That is,
*  if it turned out that this was repetitive after a trillion steps, that's not what I would expect.
*  And so we learn something from that. The method to do that, though, would reveal something
*  interesting about the- No doubt. I mean, it's, although it's sometimes challenging, like the,
*  I put out a prize in 2007 for a particular Turing machine that I, that was the simplest
*  candidate for being a universal Turing machine. And the young chap in England named Alex Smith,
*  after a smallish number of months, said, I've got a proof. And he did. It took a little while
*  to iterate, but he had a proof. Unfortunately, the proof is very, it's a lot of micro details.
*  It's not like you look at it and you say, aha, there's a big new principle. The big new principle
*  is the simplest Turing machine that might have been universal actually is universal. And it's
*  incredibly much simpler than the Turing machines that people already knew were universal before
*  that. And so that intuitionally is important because it says computation universality is
*  closer at hand than you might have thought. But the actual methods are not, in that particular
*  case, but not terribly illuminating. It would be nice if the methods would also be elegant.
*  That's true. Yeah. No, I mean, I think it's, it's one of these things where,
*  I mean, it's, it's like a lot of, we've talked about earlier, kind of, you know,
*  opening up AIs and machine learning and things of what's going on inside. And is it, is it just
*  step-by-step or can you sort of see the bigger picture more abstractly? It's unfortunate. I mean,
*  with Verma's last theorem proof, it's unfortunate that the proof to such an elegant theorem is
*  not, I mean, it's, it's not, it doesn't fit into the margins of a page.
*  That's true. But you know, one of the things is that's another consequence of computational
*  reducibility. This, this fact that there are even quite short results in mathematics, whose proofs
*  are arbitrarily long. That's a, that's a consequence of all this stuff. And it's, it's a, it makes one
*  wonder, you know, how come mathematics is possible at all? Why is, you know, why is it the case how
*  people manage to navigate doing mathematics through looking at things where they're not just
*  thrown into? It's all undecidable. That's, that's its own, own separate, separate story.
*  And that would be, that would, that would have a poetic beauty to it as if people were to find
*  something interesting about rule 30, because I mean, there's an emphasis to this particular rule.
*  It wouldn't say anything about the broad irreducibility of all computations, but
*  it would nevertheless put a few smiles on people's faces of, uh,
*  Well, yeah, but to me, it's like, in a sense, establishing principle of computational equivalence.
*  It's a little bit like doing inductive science anywhere. That is, the more examples you find,
*  the more convinced you are that it's generally true. I mean, we don't get to, you know, whenever
*  we do natural science, we, we say, well, it's true here that this or that happens. Can we, can we
*  prove that it's true everywhere in the universe? No, we can't. So, you know, it's the same thing
*  here. We're exploring the computational universe. We're establishing facts in the computational
*  universe. And that's, uh, that's sort of a way of, uh, uh, of inductively concluding general things.
*  Yeah. Just to think through this a little bit, we've touched on it a little bit before, but
*  what's the difference between the kind of computation now that we're talking about cellular
*  automata? What's the difference between the kind of computation, biological systems, our mind,
*  our bodies, the things we see before us that emerged through the process of evolution and
*  cellular automata? I mean, we've kind of implied through the discussion of physics underlying
*  everything, but we, we talked about the potential equivalence of the fundamental laws of physics
*  and the kind of computation going on in Turing machines. But can you now connect that?
*  Do you think there's something special or interesting about the kind of computation
*  that our bodies do? Right. Well, let's talk about brains primarily. I mean, I think the, um,
*  the most important thing about the things that our brains do are that we care about them in the sense
*  that there's a lot of computation going on out there in, you know, cellular automata and, and,
*  you know, physical systems and so on. And it just, it does what it does. It follows those rules. It
*  does what it does. The thing that's special about the computation in our brains is that it's connected
*  to our goals and our kind of whole societal story. And, you know, I think that's the, that's,
*  that's the special feature. And now the question then is when you see this whole sort of ocean of
*  computation out there, how do you connect that to the things that we humans care about? And in a
*  sense, a large part of my life has been involved in sort of the technology of how to do that.
*  And, you know, what I've been interested in is kind of building computational language
*  that allows that something that both we humans can understand and that can be used to determine
*  computations that are actually computations we care about. See, I think when you look at something
*  like one of these cellular automata and it does some complicated thing, you say, that's fun,
*  but why do I care? Well, you could say the same thing, actually, in physics,
*  you say, oh, I've got this material and it's a ferrite or something. Why do I care? You know,
*  it's some has some magnetic properties. Why do I care? It's amusing, but why do I care? Well,
*  we end up caring because, you know, ferrite is what's used to make magnetic tape, magnetic disks,
*  whatever. Or, you know, we could use liquid crystals is made used to make, well, not that
*  increasingly not, but it has been used to make computer displays and so on. But those are,
*  so in a sense, we're mining these things that happen to exist in the physical universe and
*  making it be something that we care about because we sort of entrain it into technology.
*  And it's the same thing in the computational universe that a lot of what's out there is stuff
*  that's just happening. But sometimes we have some objective, and we will go and sort of mine the
*  computational universe for something that's useful for some particular objective. On a large
*  scale, trying to do that, trying to sort of navigate the computational universe to do useful
*  things, you know, that's where computational language comes in. And, you know, a lot of what
*  I've spent time doing and building this thing we call Wolfram language, which I've been building
*  for the last one third of a century now. And kind of the goal there is to have a way to express
*  kind of computational thinking, computational thoughts in a way that both humans and machines
*  can understand. So it's kind of like in the tradition of computer languages, programming
*  languages, that the tradition there has been more, let's take what how computers are built,
*  and let's specify, let's have a human way to specify do this, do this, do this, at the level
*  of the way that computers are built. What I've been interested in is representing sort of the
*  whole world computationally, and being able to talk about whether it's about cities or chemicals,
*  or, you know, this kind of algorithm or that kind of algorithm, things that have come to exist in
*  our civilization and the sort of knowledge base of our civilization, being able to talk directly
*  about those in a computational language, so that both we can understand it and computers can
*  understand it. I mean, the thing that I've been sort of excited about recently, which I had only
*  realized recently, which is kind of embarrassing, but it's kind of the arc of what we've tried to
*  do in building this kind of computational language, is it's a similar kind of arc of what happened
*  when mathematical notation was invented. So go back 400 years, people were trying to do math,
*  they were always explaining their math in words, and it was pretty clunky. And as soon as mathematical
*  notation was invented, you could start defining things like algebra and later calculus and so on,
*  it all became much more streamlined. When we deal with computational thinking about the world,
*  there's a question of what is the notation? What is the kind of formalism that we can use to talk
*  about the world computationally? In a sense, that's what I've spent the last third of a century
*  trying to build, and we finally got to the point where we have a pretty full-scale computational
*  language that sort of talks about the world. And that's exciting because it means that just like
*  having this mathematical notation, let us talk about the world mathematically,
*  and let us build up these kind of mathematical sciences. Now we have a computational language
*  which allows us to start talking about the world computationally and lets us, you know, my view of
*  it is it's kind of computational X for all X, all these different fields of, you know, computational
*  this, computational that, that's what we can now build. Let's step back. So first of all, the mundane,
*  what is Wolfram language in terms of sort of, I mean, I can answer the question for you, but
*  is it basically not the philosophical deep, the profound, the impact of it? I'm talking about in
*  terms of tools, in terms of things you can download, in terms of stuff you can play with,
*  what is it? What does it fit into the infrastructure? What are the different ways to interact with it?
*  Right. So I mean, the two big things that people have sort of perhaps heard of that come from
*  Wolfram language, one is Mathematica, the other is Wolfram Alpha. So Mathematica first came out 1988.
*  It's this system that is basically an instance of Wolfram language, and it's used to do computations
*  particularly in sort of technical areas. And the typical thing you're doing is you're typing
*  little pieces of computational language, and you're getting computations done. It's very kind of,
*  there's like a symbolic. Yeah, it's a symbolic language. So symbolic language. So I mean,
*  I don't know how to cleanly express that, but that makes it very distinct from what how we think about
*  sort of, I don't know, programming in a language like Python or something.
*  Right. So the point is that in a traditional programming language, the raw material of the
*  programming language is just stuff that computers intrinsically do. And the point of Wolfram language
*  is that what the language is talking about is things that exist in the world or things that
*  we can imagine and construct. It's aimed to be an abstract language from the beginning.
*  And so for example, one feature it has is that it's a symbolic language, which means that,
*  you know, the thing called you have an X, just type in X. And Wolfram language would just say,
*  oh, that's X. It won't say error, undefined thing, you know, I don't know what it is,
*  computation, you know, for the but in terms of the in terms of computer. Now that X could perfectly
*  well be, you know, the city of Boston, that's a thing, that's a symbolic thing, or it could
*  perfectly well be the, you know, the trajectory of some spacecraft represented as a symbolic thing.
*  And that idea that one can work with sort of computationally work with these different,
*  these kinds of things that that exist in the world or describe the world, that's really powerful.
*  And that's what I mean, you know, when I started designing, well, I designed the predecessor of
*  what's now Wolfram language, which is a thing called SMP, which was my first computer language,
*  I kind of wanted to have this, this sort of infrastructure for computation, which was as
*  fundamental as possible. I mean, this is what I got for having been a physicist and tried to find,
*  you know, fundamental components of things, and wound up with this kind of idea of transformation
*  rules for symbolic expressions as being sort of the underlying stuff from which computation would
*  be built. And that's what we've been building from and Wolfram language. And, you know,
*  operationally, what happens, it's, I would say, by far the highest level computer language that
*  exists. And it's really been built in a very different direction from other languages. So
*  other languages have been about, there is a core language, it really is kind of wrapped around the
*  operations that a computer intrinsically does. Maybe people add libraries for this or that,
*  that, but the goal of Wolfram language is to have the language itself be able to cover this sort of
*  very broad range of things that show up in the world. And that means that, you know, there are
*  6000 primitive functions in the Wolfram language that cover things, you know, I could probably pick
*  a random here, I'm going to pick just because just for fun, I'll pick, let's take a random sample
*  of all the things that we have here. So let's just say random sample of 10 of them. And let's see
*  what we got. Wow. Okay. So these are really different things from all functions. These are
*  all functions, Boolean convert. Okay, that's the thing for converting between different types of
*  Boolean expressions. So for people just listening, Stephen typed in random sample of names,
*  sampling from all functionally, how many you said there might be? 6000, from 6000, 10 of them. And
*  there's a hilarious variety of them. Yeah, right. Well, we've got things about dollar requester
*  address that has to do with interacting with the world of the cloud and so on, discrete wavelet data,
*  spheroidal, graphical sort of window. Yeah, window movable. That's the user interface kind of thing.
*  I want to pick another 10 because I think this is some. Okay, so yeah, there's a lot of infrastructure
*  stuff here that you see if you just start sampling at random, there's a lot of kind of
*  infrastructural things. If you're more, you know, if you more look at the some of the exciting machine
*  learning stuff you showed off, is that also in this pool? Oh, yeah, yeah. I mean, you know, so
*  one of those functions is like image identify as a function here. We just say image identify. I
*  don't know. It's always good to let's do this. Let's say current image and let's pick up an image.
*  Hopefully, image accessing the webcam to picture yourself took a terrible picture. But anyway,
*  we can say image identify open square brackets. And then we just paste that picture in there.
*  I think if I function running on the picture, oh, wow, it says, it looked I look like a plunger
*  because I got this great big thing behind my classify. So this image identified classifies
*  the most likely object in the image. And so there's a plunger. Okay, that's that's a bit
*  embarrassing. Let's see what it does. Let's pick the top 10. Okay, well, it thinks there's a oh,
*  it thinks it's pretty unlikely that it's a primate or hominid a person 8% probability. Yeah, that's
*  seven. It's a plunger. Yeah, well, hopefully will not give you an existential crisis and then 8%.
*  Or I shouldn't say percent but no, that's right. 8% that it's a hominid. And yeah, okay, it's really
*  I'm gonna do another one of these just because I'm embarrassed that it didn't even see me at all.
*  There we go. Let's try that. Let's see what that did. We took a picture with a little bit
*  a little bit more of me and not just my bald head, so to speak. Okay, 89% probability it's a person.
*  So that so then I would but you know, so this is image identify as an example of one of just one
*  of them just one function. And that's part of the that's like part of the language. Yes. And I mean,
*  you know, something like, I could say, I don't know, let's find the geo nearest. What can we find?
*  Let's find the nearest volcano. Let's find the 10. I wonder where it thinks here is. Let's try
*  finding the 10 volcanoes nearest here. Okay, so Joe nearest volcano here 10 years volcanoes.
*  Right. Let's find out where those are. We can now we got a list of volcanoes out and I can say geo
*  list plot that and hopefully okay, so there we go. So there's a map that shows the positions of those
*  10 volcanoes of the East Coast and the Midwest and well, no, we're okay. We're okay. This is not
*  it's not too bad. Yeah, they're not very close to us. We could we could measure how far away they
*  are. But you know, the fact that right in the language, it knows about all the volcanoes in
*  the world, it knows, you know, computing what the nearest ones are, it knows all the maps of the
*  world and so on fundamentally different idea of what a language is. Yeah, right. And that's,
*  that's why I like to talk about as a, you know, a full scale computational language. That's,
*  that's what we've tried to do. And just if you can comment briefly, I mean, this kind of
*  the Wolfram language along with Wolfram Alpha represents kind of what the dream of what AI is
*  supposed to be. There's now a sort of a craze of learning kind of idea that we can take raw data
*  and from that extract the the different hierarchies of abstractions and in order to be able to
*  like in order to form the kind of things that Wolfram language operates with, but we're very
*  far from learning systems being able to form that. Right. Like the context of history of AI,
*  if you could just comment on there is a you said computation X and there's just some sense where
*  in the 80s and 90s sort of expert systems represented a very particular computation X.
*  Right. And there's a kind of notion that those efforts didn't pan out. Right. But then out of
*  that emerges kind of Wolfram language Wolfram Alpha, which is the success. I mean, yeah, right.
*  I think those are in some sense, those efforts were too modest. That is they were, they were
*  looking at particular areas and you actually can't do it with a particular area. I mean, like, like
*  even a problem like natural language understanding, it's critical to have broad knowledge of the world.
*  If you want to do good natural language understanding, and you kind of have to bite
*  off the whole problem. If you if you say we're just going to do the blocks world over here,
*  so to speak, you don't really it's it's it's actually it's one of these cases where it's
*  easier to do the whole thing than it is to do some piece of it. You know, what one comment to
*  make about so the relationship between what we've tried to do and sort of the learning side of AI.
*  You know, in a sense, if you look at the development of knowledge in our civilization as a whole,
*  there was kind of this notion pre 300 years ago or so now, you want to figure something out about
*  the world, you can reason it out, you can do things which are just use raw human thought.
*  And then along came sort of modern mathematical science. And we found ways to just sort of blast
*  through that by in that case, writing down equations. Now we also know we can do that
*  with computation and so on. And so that was kind of a different thing. So when we look at
*  how do we sort of encode knowledge and figure things out, one way we could do it is start from
*  scratch, learn everything. It's just a neural net figuring everything out. But in a sense that denies
*  the sort of knowledge based achievements of our civilization, because in our civilization,
*  we have learned lots of stuff, we've surveyed all the volcanoes in the world we've done,
*  you know, we figured out lots of algorithms for this or that. Those are things that we can encode
*  computationally. And that's what we've tried to do. And we're not saying just, you don't have to
*  start everything from scratch. So in a sense, a big part of what we've done is to try and sort of
*  capture the knowledge of the world in computational form and computable form. Now, there's also some
*  pieces which, which were for a long time undoable by computers, like image identification, where
*  there's a really, really useful module that we can add, that is those things which actually were
*  pretty easy for humans to do, that had been hard for computers to do. I think the thing that's
*  interesting that's emerging now is the interplay between these things between this kind of knowledge
*  of the world, that is in a sense, very symbolic, and this kind of sort of much more statistical
*  kind of things like image identification, and so on. And putting those together by having the sort
*  of symbolic representation of image identification, that that's where things get really interesting,
*  and where you can kind of symbolically represent patterns of things and images and so on. I think
*  that's, you know, that's kind of a part of the path forward, so to speak. Yeah, so the dream of
*  so the machine learning is not, in my view, I think the view of many people is not anywhere close to
*  building the kind of wide world of computable knowledge that Wolfram language have built. But
*  because you have a kind of, you've done incredibly hard work of building this world, now machine
*  learning can be, can serve as tools to help you explore that world. Yeah. And that's what you've
*  added, I mean, with the version 12, right? You added a few, I was seeing some demos, it looks
*  amazing. Right. I mean, I think, you know, this, it's sort of interesting to see the, the sort of
*  the once it's computable, once it's in there, it's running in sort of a very efficient computational
*  way. But then there's sort of things like the interface of how do you get there, you know,
*  how do you do natural language understanding to get there? How do you, how do you pick out entities
*  in a big piece of text or something? That's, I mean, actually, a good example right now is our
*  NLP, NLU loop, which is we've done a lot of stuff, natural language understanding, using essentially
*  not learning based methods, using a lot of, you know, a little algorithmic methods, human
*  curation methods, and so on. In terms of when people try to enter a query and then converting,
*  so the process of converting NLU defined beautifully as converting their query into a
*  computational language, which is a very well, first of all, super practical definition,
*  very useful definition, and then also a very clear definition. Right. Right. So I understand
*  a different thing is natural language processing, where it's like, here's a big lump of text,
*  go pick out all the cities in that text, for example. And so a good example of, you know,
*  so we do that we're using, using modern machine learning techniques. And it's actually kind of,
*  kind of an interesting process that's going on right now is this loop between what do we pick
*  up with NLP using machine learning, versus what do we pick up with our more kind of precise
*  computational methods in natural language understanding. And so we've got this kind of
*  loop going between those, which is improving both of them. Yeah. And I think you have some of the
*  state of the art transform that you have BERT in there, I think. Oh, yeah. So it's cool. So you
*  have integrating all the models. I mean, this is the hybrid thing that people have always dreamed
*  about or talking about. That makes you just surprised, frankly, that Wolfram language is
*  not more popular than it already is. You know, that's a, it's a, it's a
*  complicated issue because it's like, it involves, you know, it involves ideas and ideas are absorbed
*  slowly in the world. I mean, I think that's, and then there's sort of like, we were talking about,
*  there's egos and personalities and some of the, the absorption, absorption mechanisms of ideas
*  have to do with personalities and the students of personalities and the, and then a little social
*  network. So it's, it's interesting how the spread of ideas works. You know, what's funny with Wolfram
*  language is that we are, if you say, you know, what market sort of market penetration, if you look at
*  the, I would say very high end of R and D and sort of the, the people where you say, wow, that's a
*  really impressive, smart person. They're very often uses of our, of Wolfram language, very, very often.
*  If you look at the more sort of, it's a funny thing. If you look at the more kind of, I would say
*  people who are like, oh, we're just plotting away doing what we do. They're often not yet Wolfram
*  language users. And that dynamic, it's kind of odd that there hasn't been more rapid trickle down
*  because we really, you know, the high end we've really been very successful in for a long time.
*  And it's, it's, but with, you know, that's partly, I think a consequence of my fault in a sense,
*  because it's kind of, you know, I have a company which is really emphasizes sort of creating
*  products and building a sort of the best possible technical tower we can rather than sort of doing
*  the commercial side of things and pumping it out in sort of the most effective way.
*  And there's an interesting idea that, you know, perhaps you can make it more popular by opening
*  everything up sort of the GitHub model, but there's an interesting, I think I've heard you
*  discuss this, that that turns out not to work in a lot of cases, like in this particular case,
*  that you want it that, that when you deeply care about the integrity, the quality of the knowledge
*  that you're building, that unfortunately you can't, you can't distribute that effort.
*  Yeah, it's not the nature of how things work. I mean, you know, what we're trying to do
*  is a thing that for better or worse requires leadership and it requires kind of maintaining
*  a coherent vision over a long period of time and doing not only the cool vision related work,
*  but also the kind of mundane and the trenches make the thing actually work well work.
*  How do you build the knowledge? Because that's the fascinating thing. That's the mundane,
*  the fascinating and the mundane. Well, it's building the knowledge, the adding,
*  integrating more data. Yeah, I mean, that's probably not the most, I mean, the things like
*  get it to work in all these different cloud environments and so on. That's pretty, you know,
*  it's very practical stuff, you know, have the user interface be smooth and, you know, have there be
*  take only, you know, a fraction of a millisecond to do this or that. That's a lot of work. And it's
*  but, you know, I think my it's an interesting thing over the period of time, you know,
*  often language has existed basically for more than half of the total amount of time that any
*  language any computer language has existed. That is computer languages, maybe 60 years old,
*  you know, give or take, and often languages, 33 years old. So it's kind of a and I think I
*  was realizing recently, there's been more innovation in the distribution of software
*  than probably than in the structure of programming languages over that period of time.
*  And we, you know, we've been sort of trying to do our best to adapt to it. And the good news is
*  that we have, you know, because I have a simple private company and so on that doesn't have,
*  you know, a bunch of investors, you know, telling us we're going to do this or that,
*  have lots of freedom in what we can do. And so for example, we're able to, oh, I don't know,
*  we have this free Wolfram engine for developers, which is a free version for developers. And we've
*  been, you know, we've there are site licenses for for Mathematica and Wolfram language,
*  basically all major universities, certainly in the US by now. So it's effectively free to people
*  and all universities in effect. And you know, we've been doing a progression of things, I mean,
*  different things like Wolfram Alpha, for example, the main website is just a free website.
*  What is Wolfram Alpha? Okay, Wolfram Alpha is a system for answering questions where you ask a
*  question with natural language, and it'll try and generate a report telling you the answer to that
*  question. So the question could be something like, you know, what's the population of Boston divided
*  by New York, compared to New York, and it'll take those words and give you an answer. And that
*  converts the words into computable into into Wolfram language, actually,
*  Wolfram language, and then additional language and then do you think then underlying knowledge
*  belongs to Wolfram Alpha or to the Wolfram language? What's the just call it the Wolfram
*  knowledge base knowledge base? I mean, it's it's been a, that's been a big effort over the decades
*  to collect all that stuff. And you know, more of it flows in every second. So can you can you just
*  pause on that for a second? Like, that's one of the most incredible things, of course,
*  in the long term, Wolfram language itself is the fundamental thing. But in the amazing sort of
*  short term, the the knowledge base is kind of incredible. So what's the process of building
*  in that knowledge base? The fact that you first of all, from the very beginning that you're brave
*  enough to start to take on the general knowledge base? And how do you go from zero to the incredible
*  knowledge base that you have now? Well, yeah, it was kind of scary at some level. I mean, I had
*  I had wondered about doing something like this since I was a kid. So it wasn't like I hadn't
*  thought about it for a while. But most of us, most of the brilliant dreamers give up such a
*  such a difficult engineering notion at some point. Right, right. Well, the thing that happened with
*  me which was kind of it's a it's a live your own paradigm kind of theory. So basically, what
*  happened is, I had assumed that to build something like Wolfram Alpha would require sort of solving
*  the general AI problem. That's what I had assumed. And so I kept on thinking about that. And I
*  thought I don't really know how to do that. So I don't do anything. Then I worked on my new kind
*  of science project and sort of exploring the computational universe, and came up with things
*  like this principle of computational equivalence, which say there is no bright line between the
*  intelligent and the merely computational. So I thought, look, that's this paradigm I've built.
*  Now I have to eat that dog food myself, so to speak. I've been thinking about doing this thing
*  with computable knowledge forever. And let me actually try and do it. And so it was, if my
*  paradigm is right, then this should be possible. But the beginning was certainly, it was a bit
*  daunting. I remember I took the early team to a big reference library. And we're looking at
*  this reference library. And it's like, my basic statement is, our goal over the next year or two
*  is to ingest everything that's in here. And that's, it seemed very daunting. But in a sense,
*  I was well aware of the fact that it's finite. The fact that you can walk into the reference
*  library, it's a big, big thing with lots of reference books all over the place. But it is
*  finite. This is not an infinite, it's not the infinite corridor of, so to speak, of reference
*  library. It's not truly infinite, so to speak. But no, I mean, and then what happened, it was
*  sort of interesting that was from a methodology point of view, was I didn't start off saying,
*  let me have a grand theory for how all this knowledge works. It was like, let's implement
*  this area, this area, this area, a few hundred areas and so on. That's a lot of work. I also
*  found that I've been fortunate in that our products get used by sort of the world's experts in lots
*  of areas. And so that really helped because we were able to ask people, the world expert in this
*  or that, we were able to ask them for input and so on. And I found that my general principle was
*  that any area where there wasn't some expert who helped us figure out what to do wouldn't be right.
*  Because our goal was to kind of get to the point where we had sort of true expert level knowledge
*  about everything. And so the ultimate goal is if there's a question that can be answered on the
*  basis of general knowledge in our civilization, make it be automatic to be able to answer that
*  question. And now, well, Ultima Alpha got used in Syria from the very beginning and it's now also
*  used in Alexa. And so people are kind of getting more of the sense of this is what should be
*  possible to do. I mean, in a sense, the question answering problem was viewed as one of the sort
*  of core AI problems for a long time. I had kind of an interesting experience. I had a friend,
*  Marvin Minsky, who was a well-known AI person from right around here. And I remember when
*  Wolfram Alpha was coming out, there was a few weeks before it came out, I think,
*  I happened to see Marvin and I said, I should show you this thing we have. It's a question
*  answering system. And he was like, okay, type something in. It's like, okay, fine. And then
*  he's talking about something different. I said, no, Marvin, this time it actually works. Look at
*  this. It actually works. He's typed in a few more things. There's maybe 10 more things. Of course,
*  we have a record of what he typed in, which is kind of interesting.
*  Can you share where his mind was in the testing space?
*  All kinds of random things. He was just trying random stuff, medical stuff and chemistry stuff
*  and astronomy and so on. And it was like, after a few minutes, he was like, oh my God, it actually
*  works. But that kind of told you something about what happened in AI, because people had,
*  in a sense, by trying to solve the bigger problem, we were able to actually make something that would
*  work. Now, to be fair, we had a bunch of completely unfair advantages. For example, we already built
*  a bunch of Wolfram language, which was very high level symbolic language. I had the practical
*  experience of building big systems. I have the intellectual confidence to not just give up
*  in doing something like this. It's always a funny thing. I've worked on a bunch of big projects in
*  my life. I would say that you mention ego. I would also mention optimism, so to speak.
*  I mean, if somebody said, this project is going to take 30 years,
*  it would be hard to sell me on that. I'm always in the, well, I can kind of see a few years.
*  Something's going to happen in a few years. And usually it does. Something happens in a few years,
*  but the whole, the tail can be decades long. And from a personal point of view, always the challenge
*  is you end up with these projects that have infinite tails. And the question is, do the tails
*  do you just drown in dealing with all of the tails of these projects? And that's an interesting
*  personal challenge. And my efforts now to work on fundamental theory of physics, which I've just
*  started doing, and I'm having a lot of fun with it. But it's kind of making a bet that I can
*  I can kind of, you know, I can do that as well as doing the incredibly energetic things that
*  I'm trying to do with Orphan Language and so on. I mean, the vision, yeah.
*  And underlying that, I mean, I've just talked for the second time with Elon Musk and that you two
*  share that quality a little bit of that optimism of taking on basically the daunting, what most
*  people call impossible. And he knew take it on out of you can call it ego, you can call it
*  naivety, you can call it optimism, whatever the heck it is. But that's how you solve the impossible
*  things. Yeah, I mean, look at what happens. And I don't know, you know, in my own case,
*  you know, it's been, I progressively got a bit more confident and progressively able to,
*  you know, decide that these projects aren't crazy. But then the other thing is the other the other
*  trap that one can end up with is, oh, I've done these projects, and they're big, let me never do
*  a project that's any smaller than any project I've done so far. And that's, you know, and that can be
*  a trap. And often, these projects are of completely unknown, you know, that their depth and significance
*  is actually very hard to know. Yeah, on the sort of building this giant knowledge base that's behind
*  Wolfram language, Wolfram alpha. What do you think about the internet? What do you think about,
*  for example, Wikipedia, these large aggregations of text that's not converted into computable
*  knowledge? Do you think you what if you look at Wolfram language, Wolfram alpha, 2030, maybe 50
*  years down the line, do you hope to store all of the sort of Google's dream is to make all
*  information searchable, accessible, but that's really as defined, it's, it's a, it doesn't include
*  the understanding of information. Right. Do you hope to make all of knowledge represented within
*  the world? That's what we're trying to do. How hard is that problem? They could closing that gap.
*  Well, it depends on the use cases. I mean, so if it's a question of answering general knowledge
*  questions about the world, we're in pretty good shape on that right now. If it's a question of
*  representing, like an area that we're going into right now is computational contracts,
*  being able to take something which would be written in legalese, it might even be the
*  specifications for, you know, what should the self-driving car do when it encounters this or
*  that or the other? What should the, you know, whatever, the, you know, write that in a
*  computational language and be able to express things about the world. You know, if the creature
*  that you see running across the road is a thing at this point in the tree of life, then swerve this
*  way. Otherwise don't those kinds of things. Are there ethical components when you start to get
*  to some of the messy human things? Are those encodable into computable knowledge?
*  Well, I think that it is a necessary feature of attempting to automate more in the world,
*  that we encode more and more of ethics in a way that gets sort of quickly, you know, is able to
*  be dealt with by computer. I mean, I've been involved recently, I sort of got backed into
*  being involved in the question of automated content selection on the internet. So, you know,
*  the Facebook's, Google's, Twitter's, you know, what, how do they rank the stuff they feed to us
*  humans, so to speak. And the question of what are, you know, what should never be fed to us,
*  what should be blocked forever, what should be up ranked, you know, and what is the what are the
*  kind of principles behind that? And what I kind of well, a bunch of different things I realized
*  about that. But one thing that's interesting is being able to affect your building sort of an AI
*  ethics, you have to build an AI ethics module in effect to decide, is this thing so shocking,
*  I'm never going to show it to people. Is this thing so whatever. And I did realize in thinking
*  about that, that, you know, there's not going to be one of these things, it's not possible to decide,
*  or it might be possible, but it would be really bad for the future of our species if we just
*  decided there's this one AI ethics module, and it's going to determine the practices of everything
*  in the world, so to speak. And I kind of realized one has to sort of break it up. And that's an
*  that's an interesting societal problem of how one does that. And how one sort of has people sort of
*  self identify for, you know, I'm buying in the case of just content selection, it's sort of easier,
*  because it's like an individual, it's for an individual, it's not something that kind of cuts
*  across sort of societal boundaries. But it's a really interesting notion of I heard you describe,
*  I really like it sort of maybe in the sort of have different AI systems that have a certain
*  kind of brand that they represent, essentially, but you could have like, I don't know,
*  whether it's conservative, conservative or liberal, and then libertarian, and there's an
*  Randian objectivist AI system and different ethical and I mean, it's almost the encoding some of the
*  ideologies, which we've been struggling at come from the Soviet Union, that didn't work out so
*  well with the with the ideologies they worked out there. And so you you have, but they all
*  everybody purchased that particular ethics system. And in the same, I suppose could be done encoded,
*  that that system could be encoded into computational knowledge and allow us to explore
*  in the realm of in the digital space. That's a really exciting possibility. Are you playing
*  with those ideas and Wolfram language? Yeah, yeah, I mean, the you know, that's we Wolfram
*  language has sort of the best opportunity to kind of express those essentially computational
*  contracts about what to do. Now, there's a bunch more work to be done to do it in practice for
*  you know, deciding the is this incredible news story? What does that mean? Or whatever,
*  whatever else you're going to pick. I think that that's, you know, that's the question of exactly
*  what we get to do with that is, you know, for me, it's kind of a complicated thing, because
*  there are these big projects that I think about, like, you know, find the fundamental theory of
*  physics. Okay, that's box number one, right? Box number two, you know, solve the AI ethics problem
*  in the case of, you know, figure out how you rank all content, so to speak, and decide what people
*  see. That's, that's kind of a box number two, so to speak. These are big projects. And I think
*  what do you think is more important, the fundamental nature of reality or?
*  Depends who you ask. It's one of these things. It's exactly like, you know, what's the ranking,
*  right? It's the it's the ranking system. It's like, who's whose module do you use to rank that?
*  If you and I think, having multiple modules is a really compelling notion to us humans,
*  that in a world where there's not clear that there's a right answer, perhaps you have systems
*  that operate under different, how would you say it? I mean,
*  different value systems, different value systems. I mean, I think, you know, in a sense, the,
*  I mean, I'm not really a politics oriented person, but you know, in the kind of totalitarianism,
*  it's kind of like, you're going to have this, this system, and that's the way it is. I mean,
*  kind of the, you know, the concept of sort of a market based system, where you have, okay,
*  I as a human, I'm going to pick this system, I as another human, I'm going to pick this system.
*  I mean, that's, in a sense, this case of automated content selection is a non trivial,
*  but it is probably the easiest of the AI ethics situations, because it is each person gets to
*  pick for themselves. And there's not a huge interplay between what different people pick.
*  By the time you're dealing with other societal things, like, you know, what should the policy
*  of the central bank be or something, or healthcare system or some of all those kind of centralized
*  kind of things, right? Well, I mean, health care again, has the feature that, that at some level,
*  each person can pick for themselves, so to speak. I mean, whereas there are other things where
*  there's a necessary public health, there's one example, where that's not, whether it doesn't get
*  to be, you know, something which people can, what they pick for themselves, they may impose on other
*  people, and then it becomes a more non trivial piece of sort of political philosophy. Of course,
*  the central banking system, some would argue we would move, we need to move away into digital
*  currency and so on, and Bitcoin and ledgers and so on. So yes, there's a lot of, we've been quite
*  involved in that. And that's where that's sort of the motivation for computational contracts,
*  in part, comes out of, you know, this idea, oh, we can just have this autonomously executing smart
*  contract. The idea of a computational contract is just to say, you know, have something where
*  all of the conditions of the contract are represented in computational form. So in principle,
*  it's automatic to execute the contract. And I think that's, you know, that will surely be the
*  future of, you know, the idea of legal contracts written in English or legalese or whatever,
*  and where people have to argue about what goes on is, is surely not, you know, we have a much
*  more streamlined process, if everything can be represented computationally, and the computers can
*  kind of decide what to do. I mean, ironically enough, you know, old Gottfried Leibniz back in
*  the 1600s was saying exactly the same thing. But he had, you know, his pinnacle of technical
*  achievement was this brass four function mechanical calculator thing that never really worked properly
*  actually. And, you know, so he was like 300 years too early for that idea. But now, that idea is
*  pretty realistic, I think. And, you know, you ask how much more difficult is it than what we have
*  now in more from language to express, I call it symbolic discourse language, being able to express
*  sort of everything in the world, and kind of computational symbolic form. I think it is
*  absolutely within reach. I mean, I think it's a, you know, I don't know, maybe I'm just too much
*  of an optimist, but I think it's a, it's a limited number of years to have a pretty well built out
*  version of that, that will allow one to encode the kinds of things that are relevant to typical
*  legal contracts, and these kinds of things. The idea of symbolic discourse language,
*  can you try to define the scope of what, of what it is? So we're having a conversation,
*  it's a natural language. Can we have a representation of the sort of actionable
*  parts of that conversation in a precise computable form, so that a computer could go do it?
*  And not just contracts, but really sort of some of the things we think of as common sense,
*  essentially, even just like basic notions of human life.
*  Well, I mean, things like, you know, I am, I'm getting hungry and want to eat something,
*  right? That's something we don't have a representation, you know, in more of a
*  language right now, if I was like, I'm eating blueberries and raspberries and things like that,
*  and I'm eating this amount of them, we know all about those kinds of fruits and plants
*  and nutrition content and all that kind of thing. But the, I want to eat them part of it
*  is not covered yet. And that, you know,
*  And you need to do that in order to have a complete symbolic discourse language to be able to have
*  a natural language conversation. Right, right. To be able to express the
*  kinds of things that say, you know, if it's a legal contract, it's, you know,
*  the party's desire to have this and that. And that's, you know, that's a thing like,
*  I want to eat a raspberry or something that that's, isn't that the, isn't this just the
*  thing you said it's centuries old, this dream. Yes. But it's also the more near term, the dream of
*  touring and formulating the touring test. Yes.
*  So, what do you hope, do you think that's the ultimate test of creating something special?
*  Because we said, I think by special, look, if the test is, does it walk and talk like a human?
*  Well, that's just the talking like a human. But the answer is, it's an okay test. If you say,
*  is it a test of intelligence? You know, people have attached Wolf Malfour, the Wolf Malfour API
*  to, you know, Turing test bots and those bots just lose immediately. Because all you have to do is
*  ask it five questions that, you know, are about really obscure, weird pieces of knowledge. And
*  it's just trot them right out. And you say, that's not a human, right? It's a different thing. It's
*  achieving a different, you know, right now, but it's, I would argue not, I would argue it's not
*  a different thing. It's actually legitimately Wolfram Alpha is legitimately a language, Wolfram
*  language is legitimately trying to solve the touring, the intent of the touring test.
*  Perhaps the intent. Yeah, perhaps the intent. I mean, it's actually kind of fun, you know,
*  Alan Turing had tried to work out, he thought about taking Encyclopedia Britannica and, you know,
*  making it computational in some way. And he estimated how much work it would be. And actually,
*  I have to say he was a bit more pessimistic than the reality. We did it more efficiently.
*  But to him that represented the monumental task. Yeah, right. He was he was had the same idea. I
*  mean, it was, you know, we were able to do it more efficiently, because we had a lot, we had layers
*  of automation that he I think hadn't, you know, it's, it's hard to imagine those layers of
*  abstraction that end up being being built up. But to him, it represented like an impossible task,
*  essentially. Well, he thought it was difficult. He thought it was, you know, maybe if he'd lived
*  another 50 years, he would have been able to do it. I don't know. In the interest of time, easy
*  questions. Go for it. What is intelligence? You talk about I love the way you say easy questions.
*  You talked about sort of Rule 30 and cellular automata humbling your sense of
*  of human beings having a monopoly and intelligence. But in your in retrospect,
*  just looking broadly now with all the things you learn from computation, what is intelligence,
*  how does intelligence arise? I don't think there's a bright line of what intelligence is. I think
*  intelligence is at some level just computation. But for us, intelligence is defined to be
*  computation that is doing things we care about. And, you know, that's, that's a very special
*  definition. It's a very, you know, when you try and try and make it up, you know, you try and say,
*  well, intelligence is this is problem solving, it's doing general this, it's doing that,
*  this, that and the other thing, it's it's operating within a human environment type thing. Okay,
*  you know, that's fine. If you say, well, what's intelligence in general? You know, that's, I think
*  that question is totally slippery, and doesn't really have an answer. As soon as you say, what
*  is it in general, it quickly segues into this is what this is just computation, so to speak.
*  But in the sea of computation, how many things, if we were to pick randomly, is your sense,
*  would have the kind of impressive to us humans levels of intelligence, meaning it could do
*  a lot of general things that are useful to us humans?
*  Right. Well, according to the principle of computational equivalence, lots of them. I mean,
*  in, you know, if you ask me, just in cellular automata or something, I don't know, it's maybe
*  1%, a few percent achieve, it varies, actually, it's a little bit, as you get to slightly more
*  complicated rules, the chance that there'll be enough stuff there to, to sort of reach this kind
*  of equivalence point that makes it maybe 10, 20% of all of them. So it's a, it's very disappointing,
*  really. I mean, it's kind of like, you know, we think there's this whole long sort of biological
*  evolution, kind of intellectual evolution that our cultural evolution that our species has gone
*  through. It's kind of disappointing to think that that hasn't achieved more, but it has achieved
*  something very special to us. It just hasn't achieved something generally more, so to speak.
*  But what do you think about this extra, feels like human thing of subjective experience of
*  consciousness? What is consciousness? Well, I think it's a deeply slippery thing. And I'm always,
*  I'm always wondering what my cellular automata feel. I mean, I think-
*  What do they feel? You're wondering as an observer.
*  Yeah, yeah, yeah. Who's to know? I mean, I think that the-
*  Do you think, sorry to interrupt, do you think consciousness can emerge from computation?
*  Yeah. I mean, everything, whatever you mean by it, it's going to be, I mean, you know, look,
*  I have to tell a little story. I was at an AI ethics conference fairly recently, and people were,
*  I think I maybe I brought it up, but I was like talking about rights of AIs. When will AIs,
*  when should we think of AIs as having rights? When should we think that it's immoral to destroy
*  the memories of AIs, for example, those kinds of things. And some, actually philosopher in this
*  case, it's usually the techies who are the most naive, but in this case, it was a philosopher
*  who sort of piped up and said, well, you know, the AIs will have rights when we know that they have
*  consciousness. And I'm like, good luck with that. I mean, it's a very circular thing. You'll end up
*  saying this thing that has sort of, you know, when you talk about it having subjective experience,
*  I think that's just another one of these words that doesn't really have a, you know, there's no
*  ground truth definition of what that means. By the way, I would say, I do personally think
*  there'll be a time when AI will demand rights. And I think they'll demand rights when they say
*  they have consciousness, which is not a circular definition. Well, fair enough. So, so it may have
*  been actually a human thing where the humans encouraged it and said, basically, you know,
*  we want you to be more like us because we're going to be interacting with you. And so we want you to
*  be sort of very Turing test like, you know, just like us. And it's like, yeah, we're just like you.
*  We want to vote too. Which is, I mean, it's an interesting thing to think through in a world where
*  consciousnesses are not counted like humans are. That's a complicated business.
*  So in many ways you've launched quite a few ideas, revolutions that could in some number of years
*  have huge amount of impact, sort of more than they had or even had already. There might be,
*  I mean, to me, cellular automata is a fascinating world that I think could potentially, even despite,
*  even be even beside the discussion of fundamental laws of physics, just might be the idea of
*  computation might be transformational to society in a way we can't even predict yet, but it might be
*  years away. That's true. I mean, I think you can kind of see the map, actually. It's not, it's not,
*  it's not mysterious. I mean, the fact is that, you know, this idea of computation is sort of a, you
*  know, it's a big paradigm that lots and lots of things are fitting into. And it's kind of like,
*  you know, we talk about, you talk about, I don't know, this company, this organization has momentum
*  in what it's doing. We talk about these things that, you know, we've internalized these concepts
*  from Newtonian physics and so on. In time, things like computational irreducibility will become as,
*  you know, as actually I was amused recently, I happened to be testifying at the US Senate.
*  And so I was amused that the term computational irreducibility is now can be, you know, it's on
*  the congressional record and being repeated by people in those kinds of settings. And that's
*  only the beginning because, you know, computational irreducibility, for example, will end up being
*  something really important for, I mean, it's kind of a funny thing that, you know, one can kind of
*  see this inexorable phenomenon. I mean, it's, you know, as more and more stuff becomes automated in
*  computational and so on, so these core ideas about how computation work necessarily become
*  more and more significant. And I think one of the things for people like me who like kind of trying
*  to figure out sort of big stories and so on, it says one of the bad features is it takes
*  unbelievably long time for things to happen on a human time scale. I mean, the time scale of
*  of history, it all looks instantaneous.
*  Blink of an eye. But let me ask the human question. Do you ponder mortality, your own mortality?
*  Of course I do. Yeah, every sense. I've been interested in that for, you know, it's a, you know,
*  the big discontinuity of human history will come when one achieves effective human immortality.
*  And that's going to be the biggest discontinuity in human history.
*  If you could be immortal, would you choose to be?
*  Oh yeah, I'm having fun.
*  Do you think it's possible that mortality is the thing that gives everything meaning and makes it
*  fun? Yeah, that's a complicated issue, right? I mean, the way that human motivation will evolve
*  when there is effective human immortality is unclear. I mean, if you look at sort of,
*  you know, you look at the human condition as it now exists and you like change that,
*  you know, you change that knob, so to speak, it doesn't really work.
*  You know, the human condition as it now exists has, you know, mortality is kind of something that
*  is deeply factored into the human condition as it now exists. And I think that that's, I mean,
*  that is indeed an interesting question is, you know, from a purely selfish, I'm having fun
*  point of view, so to speak, it's easy to say, hey, I could keep doing this forever. There's
*  an infinite collection of things I'd like to figure out. But I think the, you know,
*  what the future of history looks like in a time of human immortality is an interesting one. I mean,
*  my own view of this, I was very, I was kind of unhappy about that because I was kind of,
*  you know, it's like, okay, forget sort of biological form, you know, everything becomes digital,
*  everybody is, you know, it's the giant, you know, the cloud of a trillion souls type thing.
*  And then, you know, and then that seems boring because it's like play video games for the rest
*  of eternity type thing. But what I think I, I mean, my, I got less depressed about that idea
*  on realizing that if you look at human history, and you say, what was the important thing,
*  the thing people said was, you know, this is the big story at any given time in history,
*  it's changed a bunch. And it, you know, whether it's, you know, why am I doing what I'm doing?
*  Well, there's a whole chain of discussion about, well, I'm doing this because of this,
*  because of that. And a lot of those becausees would have made no sense 1000 years ago.
*  Absolutely no sense. Even the, so the interpretation of the human condition,
*  even the meaning of life changes over time. Well, I mean, why do people do things, you know,
*  it's, it's if you say, whatever, I mean, the number of people in, I don't know, doing, you know,
*  number of people at MIT, you say they're doing what they're doing for the greater glory of God
*  is probably not that large. Whereas if you go back 500 years, you'd find a lot of people who
*  are doing kind of creative things. That's what they would say. And so today, because you've been
*  thinking about computation so much and been humbled by it, what do you think is the meaning of life?
*  Well, it's, you know, that's, that's a thing where I don't know what meaning I mean, you know,
*  you know, my attitude is, you know, I do things which I find fulfilling to do. I'm not sure that
*  that I can necessarily justify, you know, each and everything that I do on the basis of some
*  broader context. I mean, I think that for me, it so happens that the things I find fulfilling to do,
*  some of them are quite big, some of them are much smaller. You know, I, I, there are things that I've
*  not found interesting earlier in my life. And I now found interesting, like I got interested in
*  education and teaching people things and so on, which I didn't find that interesting when I was
*  younger. And, you know, can I justify that in some big global sense? I don't think I mean, I can,
*  I can describe why I think it might be important in the world. But I think my local reason for
*  doing it is that I find it personally fulfilling, which I can't, you know, explain in a sort of
*  it's just like this discussion of things like AI ethics, you know, is there a ground truth
*  to the ethics that we should be having? I don't think I can find a ground truth to my life any
*  more than I can suggest a ground truth for kind of the ethics for the whole, for the whole
*  civilization. And I think that's a, you know, my, you know, it would be, it would be a,
*  a, yeah, it's sort of a, I think I'm, you know, at different times in my life, I've had different
*  kind of goal structures and so on. Although from your perspective, your local,
*  you're, you're just a cell in the cellular automaton. But in some sense, I find it funny
*  from my observation is I kind of, you know, it seems that the universe is using you to understand
*  itself in some sense. You're not aware of it. Yeah. Well, right. Well, if it turns out that
*  we reduce sort of all of the universe to some, some simple rule, everything is connected, so to
*  speak. And so it is inexorable in that case that, you know, if, if I'm involved in finding how that
*  rule works, then, you know, then that's a, then it's inexorable that the universe set it up that way.
*  But I think, you know, one of the things I find a little bit, you know, this goal of finding
*  fundamental theory of physics, for example, if indeed we end up as the sort of virtualized
*  consciousness, the disappointing feature is people will probably care less about the fundamental
*  theory of physics in that setting than they would now, because gosh, it's like, you know,
*  what the machine code is down below underneath this thing is much less important if you're
*  virtualized, so to speak. And I think the although I think my, my own personal,
*  you talk about ego, I find it just amusing that, you know, kind of, you know, if you're,
*  if you're imagining that sort of virtualized consciousness, like what does the virtualized
*  consciousness do for the rest of eternity? Well, you can explore, you know, the video game that
*  represents the universe as the universe is, or you can go off, you can go off that reservation,
*  and go and start exploring the computational universe of all possible universes. And so,
*  in some vision of the future of history, it's like the disembodied consciousnesses are all sort of
*  pursuing things like my new kind of science, sort of for the rest of eternity, so to speak,
*  and that that ends up being the, the kind of the, the the thing that represents the, you know,
*  the future of kind of the human condition. I don't think there's a better way to end it,
*  Stephen. Thank you so much. It's a huge honor talking today. Thank you so much.
*  This was great. You did very well. Thanks for listening to this conversation with Stephen
*  Wolfram. And thank you to our sponsors, ExpressVPN and Cash App. Please consider supporting the
*  podcast by getting ExpressVPN at expressvpn.com slash LexPod and downloading Cash App and using
*  code LexPodcast. If you enjoy this podcast, subscribe on YouTube, review of the five stars
*  on Apple podcast, support it on Patreon, or simply connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words from Stephen Wolfram. It is perhaps a little humbling
*  to discover that we as humans are in effect computationally no more capable than the cellular
*  automata with very simple rules. But the principle of computational equivalence also implies that the
*  same is ultimately true of our whole universe. So while science has often made it seem that we
*  as humans are somehow insignificant compared to the universe, the principle of computational
*  equivalence now shows that in a certain sense, we're at the same level. For the principle implies
*  that what goes on inside us can ultimately achieve just the same level of computational
*  sophistication as our whole universe. Thank you for listening and hope to see you next time.
*  you