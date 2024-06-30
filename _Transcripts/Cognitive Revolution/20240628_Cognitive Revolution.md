---
Date Generated: June 30, 2024
Transcription Model: whisper medium 20231117
Length: 6521s
Video Keywords: []
Video Views: 872
Video Rating: None
Video Description: Dive into the profound discussion on AI expectations and the future with Martin Casado, General Partner at Andreessen Horowitz, as we unpack the complexity of AI systems and their potential impact on the world. Explore the differing viewpoints on AI's epistemics, possible regulatory standards, and the art of predicting AI advancements. Gain insights into the actionable outcomes of this dialogue and the significance of understanding AI before shaping policies. Join us for this episode of the Cognitive Revolution to contemplate AI's trajectory and what it might mean for humanity.

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
(00:03:18) AI progress
(00:05:20) Threshold effects
(00:12:30) Heavy-tailed universe
(00:14:53) LLMs are not very good at unique tasks
(00:26:27) Sponsors: Oracle | Brave
(00:28:36) Understanding meaning
(00:31:44) How do LLMs work? (Part 1)
(00:36:25) Sponsors: Omneky | Squad
(00:38:12) How do LLMs work? (Part 2)
(00:44:01) Post-training
(00:51:09) Simulation
(01:04:06) Regulation
(01:08:53) What makes AI a paradigm shift
(01:11:51) Compute limits
(01:20:07) Sleeper agents
(01:23:16) Surface area of models
(01:25:49) AI regulation
(01:27:35) AI in medicine
(01:29:56) AGI, superintelligence
(01:37:04) Competition in the foundation model space
(01:40:57) The scaling laws
(01:44:31) The AGI convergence
(01:45:35) Bets on the future of AI
(01:48:20) Outro
---

# AI Safety Regulations: Prudent or Paranoid? with a16z's Martin Casado
**Cognitive Revolution:** [June 28, 2024](https://www.youtube.com/watch?v=oZ7788oKoss)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm excited to share my
*  conversation with Martine Casado, general partner at Andresen Horowitz.
*  Instead of our usual expert interview format, today Martine and I engage in a genuine back
*  and forth conversation about how we understand today's frontier AI models, the potential for
*  next generation systems to become powerful actors in the world, and what, if anything,
*  we should do about that now. I had initially planned to discuss our respective AI worldviews
*  only briefly before moving on to questions of appropriate commitments, standards, and
*  regulations for AI developers, but we ended up spending a full hour on epistemics and
*  expectations when it became clear that our different outlooks were upstream of any such
*  policy debates. When we did get there in the second half, I found the discussion far more
*  agreeable than you might expect from today's online discourse, in part I think because we
*  had already identified how we understand the situation differently. If I had to try to
*  characterize our perspectives, I'd say that I am more focused on what I can infer from my understanding
*  of current AI systems capabilities and their mechanisms, while Martine, who to be clear has
*  definitely also studied today's systems on a technical level, seems to base his expectations
*  more on historical examples and the profound complexity of the broader world. One key question
*  that emerged is how much the potentially irreducible computational complexity of the
*  universe ultimately matters, and whether AI models will be able to take very effective shortcuts
*  relative to full-on simulation. For several reasons, it seems to me that they probably
*  will be able to do this. For one thing, we humans seem to do it, so there's some existence proof
*  that it's possible, and for another, we see some aspects of these dramatic shortcuts emerging
*  in the models that we've covered in recent episodes on protein folding and interaction,
*  as well as small-scale chemistry simulations. That said, it is still the case that no very
*  general system has developed a reliable world model, to say nothing of an adversarially robust
*  world model at this point in time, and I certainly can't prove that it will happen at any point in
*  time or scale. While we didn't reach full agreement on worldview, I think this discussion demonstrates
*  that it is absolutely possible to communicate across quite different AI perspectives, and it
*  also reinforces the idea for me that it continues to make more sense to focus our time and energy
*  on understanding what is before jumping to what ought to be done about it. Toward the end,
*  we agreed on the idea of making one or more one-dollar bets about how the near-term future
*  will shape up. I invite any interested listeners to try to formalize those conditions, and if you
*  want to do that on a prediction market platform, I will happily share those links. As always,
*  if you're finding value in the show, we'd appreciate it if you'd share it with a friend.
*  And of course, we welcome your feedback via our website, cognitiverevolution.ai, where we're
*  accepting resumes that I'll be circulating privately with friendly companies, and of course,
*  you're always welcome to DM me on any social network anytime. Now, I hope you enjoyed this
*  exploration of AI expectations and implications with Martin Casado of Entrace and Horowitz.
*  Martin Casado, general partner at A16Z. Welcome to the Cognitive Revolution.
*  Very happy to be here.
*  I think this is going to be a great conversation. We are primarily here to talk about the importance
*  of open source and to dig into a lot of the details of the current debates around early
*  regulation of AI and how that might impact open source and what the pros, if any, and cons,
*  potentially many of that might be. Before we get into it, I just wanted to get a little bit of your
*  super big picture AI worldview and ask you to project out a little bit.
*  How powerful do you think AI is going to be over the next couple of years? We've obviously heard
*  AGI 2027. Is that a story you're buying? What do you think we're going to see over the next two
*  to three years? I think all things in the past is probably the best predictor of the future.
*  My hope is this continues to be a very useful tool to help us with progress and to stave off
*  this universe that seems pretty destined on killing us. I'm hoping it continues on that
*  trajectory. What is interesting is if you actually look, let's say the past 80 years of quote unquote
*  AI, it's been steady progress, independent of there being winters and summers. It's been very,
*  very steady progress. It's been progress on economics, progress on problem solves.
*  Every time we tackle a problem, everybody's, oh, goodness, this is it. We're almost at AGI.
*  Then it just turns out that's one modality. Then we go on to the next and we say, oh,
*  that wasn't really actually AGI or AI. This whole AGI thing has been a moving goalpost for 70 years.
*  I would say, listen, it's been this very steady progress. We've gotten good at many things. It's
*  been a very useful tool. I hope it continues to be so. I think it's a very important thing for us to
*  continue to develop and use. I don't think that there's any step change or it changes the nature
*  of computers or software in ways that we haven't seen before. I don't think that.
*  Let me just give you a few more concrete things because I'm a big believer in threshold effects.
*  The topics of emergence are super hotly debated and is emergence a mirage or not a mirage? Maybe
*  the underlying curves are smooth. In terms of practical utility, even if the capability of the
*  model hasn't taken a sudden shift, the utility and what it can actually practically do in the world
*  sometimes seems to take a notable leap. I guess right now, I thought Dorkash put this really well
*  on a recent podcast where he said, it seems like the models are token for token as smart as most
*  people. Yet there's some things that they're missing. They don't have this great long-term
*  memory or the ability to integrate memories. They're not great at autonomy. They fall down
*  and can't get back up or don't know how to dust themselves off. But it seems like the core
*  intelligence is there to do a lot of jobs. It's this packaging memory, agentic finishing
*  that's needed to get to the point where you'd have this sort of knowledge worker. Is that basically
*  the story that you see? Does that translate to a... I think AGI is, yes, certainly very ill-defined,
*  but drop in knowledge worker that could do a large majority of jobs passively well is maybe
*  better defined. Do you see that coming soon? Again, I think I'd like to draw from a historical
*  analogy because I think they're very useful in this context because we see these very often
*  and they all look kind of the same and it's played out. When I first joined Stanford to do my PhD,
*  I did my PhD in computer science and systems was in 2003. Around then, I don't know, it was
*  2003 or 2004, Sebastian Thrun had won the DARPA Grand Challenge. The DARPA Grand Challenge,
*  he drove a van fully autonomously for 1200 miles and everybody was like, hooray, AGI is solved,
*  RoboTaxi is solved. This is amazing thing. A hundred percent, we've hit one of these threshold
*  moments, a hundred percent like you could actually do things you couldn't do before.
*  It was the start of a new era of vision and perception and self-driving and now 20 years
*  later and about a hundred billion dollars invested, a little bit less than a hundred billion dollars
*  invested, the unit economics of self-driving are still three times worse than Uber. I'm a systems
*  person, meaning all I've been doing for the last 30 years of my life is building computer systems,
*  large distributed systems. This is what I do and I just know that scalar capabilities,
*  A, they're not necessarily parametric. They don't necessarily just go up and to the right.
*  There's so many examples of this and we can talk about that. I know that the universe is this very
*  heavy-tailed system and there's no single solution that tends to reign in its complexity. I know that
*  the economics for these things are very, very hard. What gets lost in these conversations is
*  AI has been better at humans for a very long time at many things, handwriting detection,
*  diagnosis for a very long time, game playing for a very long time, mathematics since the creation
*  of the computer. You know, forwarders and magnitude better than mathematics than us
*  and yet none of these things have resulted in kind of general economically viable solutions
*  for everything. They've just for subsets, right? And so for, we can talk about this language. So
*  another way to rephrase what you said about the language stuff is these models are very good at
*  predicting what a mean person would do next. A mean person would do next. So sure, they basically
*  do kernel smoothing over positional embeddings. That's great, which means if you have a corpus
*  of data, it'll give you the average response, which is great. And it's very useful for a number
*  of things. Does that provide economic utility for a broad range of stuff? I mean, I'll tell you,
*  I look at these companies basically full-time and I have for three years, we probably have the largest
*  portfolio of them and I don't see that yet. Now there are areas where they do work, but it's not
*  that. It's not this kind of general knowledge worker. That's not actually not working. And the
*  areas where it is working is stuff like the marginal cost of content creation goes to zero.
*  So now we have like amazing new content or computers are creating an emotional connection
*  with humans. That's new and that's exciting and that's amazing. But this idea of this general
*  knowledge worker working, I haven't seen it yet and maybe it'll happen, but just like self-driving
*  20 years ago, like that's just not how the universe tends to play out.
*  Yeah, I guess where do you think we are in self-driving today? And it's been actually a
*  couple upgrades since I took my last ride in a Tesla FSD. This was last summer, actually. It's
*  been basically a year since I did it last. At that point, I was like, I think this is actually safer
*  than the average person I drive with and probably the average person I see around me on the road,
*  sometimes I'm like, man, how did you survive long enough to get in front of me and do that?
*  And they're not deployed at superscale. We're not quite ready to trust them. But if you believe
*  the statistics from the company and certainly my just episodic experience seems to suggest that
*  they probably are roughly on par, maybe even better. And maybe society is going to demand
*  a 10X better to actually deploy at scale. But it seems like we're kind of there.
*  And I guess, so I don't know if they're kind of unit economic, and I don't know if they're there
*  on an exception basis. I do feel with a lot of these AI things, you enter this area where
*  you get good enough that the economics suggest that you change the environment rather than make
*  the AI more general. And I think this is probably best described with agriculture. So we don't have
*  any unit economically viable way to pick strawberries. It's like human beings and animals
*  have been forging food forever. We're very efficient at it. To actually compete with a human
*  on that is very tough. On the other hand, what we can do is we can play strawberries in certain rows
*  and we can add these optical cues, etc. That kind of get it much closer. And so I definitely think
*  that we're at a place where for many cases, AI is better than humans at driving, which I think is
*  great. And I think it's a huge positive. I think these are hugely specialized systems. I don't
*  think you can take the one that's good at self-driving and make it, I don't know, be a
*  virtual girlfriend. I think there's a totally different modality. So it's not general, right?
*  It's not general. It's just good at driving. Just like something is good at chess. And now I think
*  we're at the long tail of the problem. For fully autonomous stuff like Waymo, the unit economics
*  are just very tough, right? They're very tough if you're competing with a human driver. For other
*  ones, I do think that if we just start evolving how we make streets and so forth, I think we're
*  pretty close. And I think that's great. I think this is a positive for everybody. Yeah, I love the
*  narrowness of the full self-driving. I actually think that's a huge plus that it is an engineered
*  system that does one thing. And I also love your comment about modifying the environment.
*  That was actually very notable even a year ago in the FSD that the places where it got tripped up,
*  I was like, the closest exit to my house off the highway has one of these service roads and has a
*  stop sign. And it's genuinely quite ambiguous as to who the stop sign is for as you're getting off
*  the highway. It's not for you as you're getting off the highway, but it's pointed right at you.
*  And so you can understand how it would get confused about that. And that's the kind of
*  thing that if we're serious, we could just go on fixing these signs and we'd make it so much better.
*  Just quick digression, because this is just so important to this discussion on how
*  the heavy-tailed universe makes this conversation very complicated between human beings. Because I
*  don't think people appreciate how heavy-tailed the universe is. So I just want to describe this
*  because it just comes up right now and it's going to be so relevant to what we're going to be talking
*  going forward, which is there are many things that systems deal with that are heavy-tailed.
*  What heavy-tailed means is if you draw an occurrence at random, just draw one at random,
*  the chances are is that it's a very rare occurrence. So a very classic case of this is search.
*  And so if you draw a unique search query, say Google at random, the chances are it's pretty
*  unique actually, even after all of this time. Now this is unique searches. So if you take all of the
*  searches that go into Google, say, and then you don't dedupe them, so like you can have a lot of
*  repetitive ones, the vast majority of searches are the same. Let's say 90% of them are common.
*  But if you reduce it to just singular intents, so you don't have any duplications, the majority
*  are exceptions. And that's how the universe tends to be. Like I come from networking, it's a very
*  famously heavy-tailed discipline. A lot of things in the tail. So if you're building a general system,
*  the majority of new things it has to do, not things it has to do, the majority of new things
*  it has to do are exceptions. Now it's very easy to get tripped up in these conversations because
*  the majority of stuff that you're doing is not new. The majority of stuff you're doing is very
*  common. But anytime you get into new areas, then you have to come up with new stuff. And it's like
*  self-driving is a very great case of this. Like nobody expected basically a 2D vision problem.
*  Let's be honest, man. Self-driving is 2D. It's not even 3D. It's like you have streets and you have
*  signs. You don't really worry about the Z dimension really. And yet $100 billion in,
*  $100 billion of investment, we're almost there, but not in an economically positive way.
*  The reason I want to make this point now is I think so much of these discussions is people,
*  I believe, underestimating how heavy-tailed the universe is and how hard it is to make progress.
*  And so we should be working as hard to make progress so that we can do stuff like self-driving
*  and not slow it down because the task is enormously complex. I think that's definitely a good
*  description of where things are today. In my kind of summary communications about the state of AI,
*  I always say that the best systems are closing in on expert performance on routine tasks. And the
*  board routine there definitely is critical because when you get outside of routine tasks,
*  they are not comparable to expert performance. So let's move this to here. So as far as I can tell
*  what LLMs are doing, and there's actually papers that are shown pretty concretely, is they take a
*  corpus of data, they create positional embeddings, and they basically average over it. And based on
*  that, they can predict what a human being would do or say given a certain situation. And they do
*  that basically via averaging. For 80% of the tasks, let's say that's great. This is for 80% as
*  non-unique. So you're not deduping tasks. But let me give you an analogy. What if I came to you,
*  I'm a startup founder, I'm like, hey, Nathan, I've got this amazing chat bot that for IT help tickets,
*  it answers 90% of the time. And you're like, this is amazing. Like 90% of the work goes away.
*  This is what you say. But then you actually do diligence on my company, and you realize
*  that 90% of that, 85% of that is just answering password resets. So I was factually correct
*  saying that 90% gets answered. That's the case. But the reality is the situations that I help with
*  are very easy to automate if you wanted to, and they're not that much work. And you still have,
*  from a unique standpoint, you still have to have humans do 50% of the unique things that come in,
*  50%. So that was the state of chat bots for the last 10 years. And we had the exact same discussions.
*  They seem to answer 90%, they answer 85%, they can do these things, we're almost done.
*  But that's not how heavy tail distributions work. So again, so let's go to this case that you're
*  making 100% these LLM solve problems we couldn't before. And 100% they're a very useful computer
*  science primitive. We're nowhere close to understanding what these distributions look like,
*  how heavy tail they are, and how they can handle that tail, just like we weren't with AV,
*  just like we weren't with original chat bots. And so I just think that without being specific
*  on uniqueness and the distribution and whether we think it's parametric, it's very hard to have
*  these conversations. So we result in generalities that sound good, but I think from a system
*  standpoint, aren't very sensible. How far do you think this goes? Like best guess, if you are
*  imagining yourself in 2027, and you have your AI assistant, can you say, hey, I'm going to New York
*  next week for this event. Here's the invitation, book me a flight, book me a hotel, and get a good
*  result? I think it's going to be like self driving, I think we'll get 80% there with these
*  agentic systems. And then people are going to start changing the environment to make them
*  more effective. Because human output is also heavy tailed. And so my best guess, again,
*  I'm going to repeat myself, but I actually think this is how it's going to play out is,
*  right now, anytime we're always at like beginning of what looks like an exponential,
*  but is actually a sigmoid. And what we think is like a fat head system, but ends a heavy tail
*  system, it always feels like this, like it feels right now. And everybody's saying all the stuff
*  that they're saying right now. And we're like, it's amazing, you know, everything's going to work
*  out. And then we're going to realize, oh, my goodness, the universe is heavy tail. This is
*  really hard. These things are good at 80% of stuff, but the 80% of stuff that it's good at
*  is not that hard. And the stuff that I need it to be good at is really hard. And so then we're
*  going to enter an area that we're like, oh, boy, we talked about scaling laws, throwing 10 times
*  more compute at something over a period of time is so impossible that what we're going to do is
*  we're going to actually change the way websites work. And we're going to actually have indicators
*  and we're actually going to have lanes. And then we're going to spend the time actually changing
*  the systems. And so over time between changing the way websites work and where these agents work,
*  we'll enter a period where these things are more autonomous. But I don't think it's because we've
*  cracked the generality problem. I think it's because we've evolved computer science as a
*  discipline and tech and software as an industry in order to solve the problem.
*  Soterios Johnson I find language to be a confusing domain in some ways because
*  there is so much, it's hard to get truly out of distribution in interesting ways. It can write
*  a sonnet about the NBA finals or whatever. And that's definitely out of distribution,
*  but you could say it's interpolating between things in distribution. Sometimes I'd like to
*  just go to things that humans can't do. So when I look at things like EVO, the early foundation
*  model for DNA sequencing, it's an interesting one. And there's another, I did an episode just
*  yesterday on models for basically simulating solutions, like salt solutions. And in both of
*  these cases, you see these sort of remarkable generalization moments where in the EVO case,
*  it's trained on DNA sequence data, just like bacteria and phage data. So it's next token
*  prediction, it's next base pair prediction, same thing as a language model. So you could say,
*  oh, it's only predicting the next base pair. But like the language models, it seems to have developed
*  these higher order internal representations that mean something that it was not specifically
*  trained to learn, but that it's learned in service of making the next base pair prediction.
*  And one of the experiments that they did that is so striking to me, this is from the ARC Institute,
*  they did what they call gene essentiality scoring, where they basically say,
*  we'll give you a gene sequence, and we'll perturb it. And then we'll look at your perplexity,
*  your being the model, your level of confidence or uncertainty downstream of that prediction.
*  If you remain confident, then we can believe that gene must not be super essential. Because if it
*  gets messed up, then you can still predict how this fits into life. But if we make that change,
*  and then you become very radically unconfident in your downstream predictions, then we can infer
*  that this gene is actually really important. Because now when it's off, now you recognize
*  you're out of distribution, and you can't make any confident predictions anymore. It seems to me like
*  that signals, and that's like a 7 billion parameter model, 300 billion tokens, that's 2% of what LAMA,
*  or one and a half percent of what LAMA 3 is trained on. So it does feel like there's
*  some potential in these systems to learn things that we don't know, to grok, if you will,
*  patterns in the universe that are not known to anyone really, to essentially speak DNA.
*  So if you buy all that, how do you backport that to language? Because I feel like I start to see,
*  just modeling the economy or modeling software. I do start to see things, if you were to train,
*  keep scaling and keep training these models on distributed systems or software or whatever,
*  how do we know that they don't start to learn things that people don't know and truly
*  generalize beyond the training set? Because it does seem like that's happening in some profound
*  way. I think this is a great question. I think maybe this is why I come to this from a different
*  thing. Prior to my PhD, my life was computational physics. I worked at Lawrence Livermore National
*  App. I did large physics simulation. I just lived this life. And I think the Occam's razor
*  in all of this is distribution in, distribution out. These things are very good at learning
*  distributions of the training set. And so this is just into this weird, quirky coincidence of
*  this moment. I actually worked on protein folding at IBM T.G. Watson Research Center in 1999 on the
*  Blue Gene Project. And at that time, there was a belief that we knew enough of the fundamental
*  forces in order to actually from first principles calculate protein folding. That was the thesis,
*  and that we just didn't have enough compute. And so they actually built a whole computer to do this
*  called Blue Gene. And through corporate machinations that ended up becoming an entirely
*  new computer because they couldn't fund it, it never really happened. But there was the belief
*  that if you had enough compute that you could do protein folding and a bunch of other stuff.
*  And so I think it's very reasonable. This is just strict Occam's razor that if you have enough
*  compute and you have enough data and you're dealing with an axiomatic system that you can reduce to
*  first principles, then you will learn that distribution and you can use it for predictive
*  stuff. And if you want to call predictive emergent, that's fine, but it's just predictive. Like
*  anything is predictive. Like I've worked on simulations codes that were predictive. Could
*  I have predicted the yield of a nuclear weapon? No, I could not have predicted that as a human
*  being only a computer can, but it's really just understanding first principles to create these
*  things. I very strongly believe these models are very useful in science where you've got
*  fundamental laws of nature that are being learned that can be predictive. I think the
*  models that are good at that is not going to turn around and solve a different problem most likely,
*  because I think you've probably learned one distribution from what domain and that's a very
*  useful tool that we should use. Now let's go ahead and move that over to language now. So if my
*  Occam's razor is these things learn structure in a data corpus, it's distribution in distribution out,
*  that means that they're learning structure of the text corpus that they've been fed.
*  And a great example of this, there's a recent paper I saw, I don't know if it got accepted or
*  not, I think it was just on archive, but that showed that if you could gzip a text corpus
*  and the compression was good, then like the accuracy was good, which suggests almost
*  everything you need to know about this, that all it's doing is learning structure in the text.
*  It has nothing to do with underlying meaning, it's just structure that's in the text.
*  So you can understand the distribution of text, you can actually spit out text, but this doesn't
*  say anything about learning fundamental principles of the world from which the text is based.
*  And so it almost seems to be that the magic in this sequence of texts is you've got these humans
*  that have spent say 3000 years looking at the universe. And the universe is again heavy-tailed
*  and it's non-linear and it's very complex and it's fractal and it's self-similar and these are
*  notoriously complicated systems to simulate. So then the human brain is like, I'm going to abstract
*  this out as a tree and I'm going to abstract this out as like this concept. And so we're like
*  these machines that take the universe and abstract it into things that are words, but it's a very
*  lossy representation. You can't describe something and get back the universe, but it turns out because
*  we have those abstractions, they're very predictable. Like we've made the universe
*  more linear and we've made the universe less heavy-tailed and we've made the universe less
*  self-similar. And once we've done that, we've added structure that's predictable. So the fact
*  that you can take a corpus of text, which a human being has pulled from the universe and then made
*  the universe much simpler and find structure in that is not surprising at all. But to think then
*  somehow then you can go from that to the universe is a step that like just simply has not been
*  demonstrated. And it actually, it doesn't even stand to reason. Hey, we'll continue our interview
*  in a moment after a word from our sponsors. AI might be the most important new computer technology
*  ever. It's storming every industry and literally billions of dollars are being invested. So buckle
*  up. The problem is that AI needs a lot of speed and processing power. So how do you compete without
*  costs spiraling out of control? It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure or OCI. OCI is a single platform for your infrastructure,
*  database, application development and AI needs. OCI has four to eight times the bandwidth of other
*  clouds, offers one consistent price instead of variable regional pricing. And of course,
*  nobody does data better than Oracle. So now you can train your AI models at twice the speed and
*  less than half the cost of other clouds. If you want to do more and spend less like Uber, 8x8
*  and Databricks Mosaic, take a free test drive of OCI at oracle.com slash cognitive. That's
*  oracle.com slash cognitive. Oracle.com slash cognitive. The Brave Search API brings affordable
*  developer access to the Brave Search index, an independent index of the web with over 20 billion
*  web pages. So what makes the Brave Search index stand out? One, it's entirely independent and
*  built from scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans collected anonymously, of course, which filters out tons of
*  junk data. And three, the index is refreshed with tens of millions of pages daily. So it always has
*  accurate up to date information. The Brave Search API can be used to assemble a data set to train
*  your AI models and help with retrieval augmentation at the time of inference, all while remaining
*  affordable with developer first pricing. Integrating the Brave Search API into your workflow translates
*  to more ethical data sourcing and more human representative data sets. Try the Brave Search API
*  for free for up to 2000 queries per month at brave.com slash API.
*  If I understood you correctly, you're saying like that doesn't mean that they have an understanding
*  of meaning. How would you square that with like a sparse auto encoder or line of research or sort of
*  Golden Gate Claude, if you will? Like they're able to now say through these sparse encoder,
*  sparse auto encoder techniques that they can isolate, I think it's 30 some million different
*  features, each of which is a direction in activation space, and then inject those at
*  runtime, right? And they're starting to create these sort of control mechanisms where it's
*  they jack up the Golden Gate Bridge feature, then all it wants to talk about is Golden Gate Bridge,
*  or more practically, insert kindness or insert, you know, deviousness or whatever.
*  There seems to be some meaning there, right? Their structure. That's very different than meaning.
*  So we're talking about three things. And this is a great conversation, because I think it gets to
*  the heart of it. So the universe is self similar. It's fractal, meaning no matter what zoom level
*  you look at it has the same stochastic properties, right? So like you can spend an entire life
*  studying a cell and a planet, right? That's how much complexities in the universe. The universe
*  is heavy tailed, which means the exception is the norm if you dedupe. And it's nonlinear,
*  which means that you can't computationally predict out too far, just because we don't know we don't
*  have closed form solutions for nonlinear stuff. And it's just a very hard computations problem.
*  That's the universe. Now, human beings have had to navigate this crazy universe. And so we've
*  created this amazing engine, which is the brain. And it has reduced this universe to concepts and
*  words and stuff that we use and we talk about that kind of makes it a little bit predictable.
*  And so at least you and I can communicate about it. But if I tell you, like, this is a tree,
*  there's a concept tree in my brain, but it's almost an arbitrary distinction that it's a tree,
*  I could say talk about branches versus leaves. I could talk about networks of trees. That's
*  actually one tree like the big Aspen Grove, I could talk about cells of the tree. It's like
*  this kind of arbitrarily useful distinction. So it has some semblance to the real world.
*  But if I say a tree, it's probably not an accurate relative to how the world is, is it one tree? Is
*  it a family tree? It's just a useful abstraction. So these models will 100% recover the abstractions
*  that we've put in text, because the structure is all there. That's not surprising, like,
*  compression would do that. All that's doing is taking advantage of structure. And that structure
*  is real. But let's say that it's finding a tree, is it does a tree actually map to the universe in
*  a meaningful way? It's a human created concept that has some vague semblance to something we all agree
*  on. Unless you're a scientist, then you probably disagree with the common understanding. And oh,
*  by the way, my concept of a tree also includes like a toy and a cartoon picture of a tree,
*  which is entirely different. And so text is a way that we as humans represent the world that's
*  very different than the actual universe, because we find it useful. There's structure there.
*  And these LLMs are exploiting that structure, just like compression would or anything else.
*  And it's very useful for us. But it doesn't necessarily mean that these things can enact on
*  the world. These are very different domains. Yeah. I guess I'm not quite getting the gap. There's so
*  many interesting results to point to recently. Did you see the one about GPT-4 finding and
*  exploiting new zero day exploits? This was just in the last week or two. And it's increasingly
*  impossible to keep up with everything. I don't expect you've seen anything. But no, that one I
*  have. I think when you're dealing with this much compute and this much data, I think the human
*  intuition just totally fails. And we as humans are really bad about thinking in distributions.
*  That's not how we think. We kind of assume the world is parametric. And by the way,
*  which is why the text that we create is so well structured and why it could be exploited by LLMs.
*  You have to navigate this universe. You have to make the simplifying assumptions, which we do.
*  And so it's good to actually come up with mental frameworks about how these things work. So I'll
*  tell you a few of mine. The first one of mine is, as far as I can tell, these things are
*  exploiting structure in whatever data that they're reading. Like we've mentioned before.
*  And it's not clear whether that distribution extends beyond that. And if it does, then you're
*  basically back to simulating the universe, which I've spent a lot of time with. I think that's very
*  tough. The second one is the actual mechanisms. We're talking about transformers. The actual
*  mechanism is basically kernel smoothing. It's averaging. Which means to me, is the further you
*  get out to where the data is rare, the greater the inaccuracies come. And that doesn't mean
*  that for systems that you can actually extrapolate from, that you don't get great results. That would
*  be quote unquote out of distribution. It turns out some systems are linear or you have enough data,
*  you can map the distribution. So that one is totally fine. Now the third one is this in-context
*  learning one. And I think Vishal Mishra, who's a professor at Columbia, did the best work on this,
*  where he actually shows that for in-context learning, where you actually put the context
*  in the prompt and you can move the posterior distribution to get interesting results, he mapped
*  it specifically to Bayesian learning. And it's a beautiful paper. I don't know why more people
*  don't read it. So listen, we know that these things can do some basic Bayesian reasoning. And this is
*  where the prompt is basically the new evidence, which changes the posterior function. So you'll
*  get new stuff there. We know that if you average enough stuff, you'll get new stuff there. It just
*  has to be linearly interpolatable. If it's not linearly interpolatable, you're not going to get
*  new stuff. So none of these things suggest that you're not going to get new stuff. It just puts
*  constraints. We know how Bayesian systems work. We've got 20 years of understanding
*  convergence properties to them. We have a work that's specifically mapped ICL to Bayesian learning.
*  So let's just go ahead and use that corpus of work to understand the properties. It doesn't
*  say it's out of distribution or in-distribute. It doesn't say that at all. It just bounds what that
*  means. And then we also know the mechanics of the way Transformers works, which is this kernel
*  smooth. I mean, it's more complex than that. And so that can create new things, but it means there's
*  a linear interpolation. And so I think the problem is we have these anecdotal conversations
*  where it's whack-a-mole. It feels like almost like the intelligent design discussions,
*  where someone will come up with a new set of evidence of something that there's no way
*  evolution could have created this. You have to spend all of this time to show actually you can,
*  but we don't know everything. And here's the theory. And I feel like when we have these
*  discussions, it should be a bit more principled as opposed to I've got this anecdote that seems
*  something's new, because nobody says that you're not going to see new stuff. I mean, it's very
*  obviously if you're doing interpolation, it's new. Very obvious if you're doing Bayesian reasoning,
*  like something's going to be new, and talk more about the distributions and the theory of why
*  we're doing that. But as far as I can tell, that's totally missing. Nobody's come and said,
*  here's my theory of out of distribution stuff. Here is my thesis for what is going on functionally
*  to create this new data. And on the other hand, you've got mounting and tons of evidence that
*  map these to existing systems that we know that people just seem to not want to follow. And I just
*  feel like, listen, humans love to see things in clouds and complex systems. There's so many facets
*  and they're so complicated and they're so huge and they're so ethereal. And then we see things
*  and we just do this historically. And we've got these kind of amazing compute elements that are
*  huge and they surprise us and they're amazing, but we can map them to formal systems and we know how
*  they work. And that doesn't mean that they're dangerous or not dangerous. I'm not saying that.
*  I'm just saying that we can actually map them to reasonable systems to have a discussion. And that
*  just seems to be missing. This conversation is a great example. I'm very happy to map these things
*  to formal systems. We understand and have that discussion, but it's always this kind of anecdotal
*  whack-a-mole instead, which I just don't know how to answer to every instance of what seems like
*  emergent behavior when of course emergent behavior is expected anyways. Hey, we'll continue our
*  interview in a moment after a word from our sponsors. Amnaki uses generative AI to enable
*  you to launch hundreds of thousands of ad iterations that actually work customized across
*  all platforms with a click of a button. I believe in Amnaki so much that I invested in it and I
*  recommend you use it too. Use Cogrev to get a 10% discount. Hey all, Eric Torenberg here. I'm hearing
*  more and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30 year old ex-fang senior software engineer as much as the next guy,
*  but honestly I can't afford them anymore. Founders everywhere are trying to turn to
*  global talent, but boy is it a hassle to do at scale from sourcing to interviewing to on the
*  ground operations and management. That's why I teamed up with Sean Lanahan, who's been building
*  engineering teams in Vietnam at a very high level for over five years to help you access
*  global engineering without the headache. Squaw, Sean's new company, takes care of sourcing,
*  legal compliance, and local HR for global talent so you don't have to. With teams across Asia and
*  South America, we can cover you no matter which time zone you operate in. Their engineers follow
*  your process and use your tools. They work with React, Next.js, or your favorite front end frameworks,
*  and on the back end, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing
*  two hours of work per week but billing you for 40, but you'll get premium quality at a fraction of
*  the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squaw.com and mention Turpentine
*  to skip the wait list. I'm definitely a materialist and so I do believe that in the fullness of time,
*  we can probably figure out in arbitrary level of detail how these things work. They're actually
*  way easier to study than life, for example. I would say we've made tremendous progress in
*  interpretability and general understanding that you mentioned is a great example. I've seen another
*  one too that pretty similar where somebody designed a matrix implementation of gradient descent and
*  then looked for that in the wild and found it. It's like, oh, look, these things have learned to
*  implement gradient descent at runtime and that's another kind of mechanism at least sometimes.
*  Probably have different mechanisms and different models and there's this various,
*  almost like phase change type of dynamics that are being explored too, where even for something
*  as simple as the modular addition grokking, there's multiple algorithms that it can lock into,
*  each of which work but they're different. There's memorization and then there's multiple
*  actual algorithmic solves and which one you end up with depends on initial conditions.
*  I don't think there's any magic in the machine. Definitely with you on that. It does seem that
*  in principle, we should be able to figure it all out. It doesn't seem like we've made a lot of
*  progress but it doesn't seem like we're that close to having it all figured out. On the sigmoid
*  question, I tend to also agree that it does not seem like there's reason to believe that this is
*  going to be an exponential forever. It does seem like it probably levels off. But then I'm also
*  reminded of the old joke of two guys in the woods and the bear is coming and the one's putting on
*  his shoes and he says, I don't have to outrun the bear, I just have to outrun you. I do wonder
*  if we imagine continuing to scale up as we have been scaling up and there's all these trend lines
*  and x times more compute and however much advantage from algorithmic proficiency and whatever.
*  I was just talking to somebody at generally one of the top five hyperscalers in the world
*  and they are using a new replacement for the atom optimizer that is giving them something like 30%
*  savings on compute. This was published open source. The technique is called SOFIA and it's
*  just incredible. 30% off the top. You're saving $100 million on the biggest runs. Anyway, let's
*  imagine we continue to scale up and it's a few more orders of magnitude. Let's say we don't just
*  put in the text but we also put in this low-level solution data and the protein, the DNA data and
*  the protein and the gene expression and we work our way up all these levels of orders of magnitude.
*  Then it's like computer systems, like all the cloud logs from AWS and Google Cloud and all
*  this stuff gets in there and you've got all these different self-similar but overlapping
*  orders of magnitude of ways of understanding the world. Even if it asymptotes or levels off at some
*  point, I have a hard time imagining that doesn't level off at a higher point than human is able
*  to achieve today. I feel like you probably see that differently still. A lot of this reduces to
*  how you view the universe. If you don't view the universe as fractal self-similar and if you don't
*  view it as heavy-tailed and if you don't view it as non-linear, then you could imagine that. It is
*  all of those things. We know it is all of those things. There's no distribution of data that we
*  know of that's not the universe that will produce something that's predictive of the universe.
*  It's really that simple. That doesn't mean that we can't focus on an area and reproduce that
*  distribution. I could become very good at predicting whatever, protein folding. I could get
*  really good at playing chess. But it's distribution in, distribution out. If you notice the ones that
*  stuff like recursive self-similarity works and control loops work and simulated data works,
*  like synthetic data works, there are these axiomatic areas where the axioms constrain
*  the search space and you're basically converging on search. You can get very good at those. I can
*  get much better at unit arithmetic. I can get much better than you at game playing. I can get much
*  better at humans at all of these things. But none of that talks to the fact that can you find the
*  right level of abstraction in a fractal system and can you tackle a heavy-tailed universe where
*  not by occurrence but by uniqueness the complexities in the tail? Even in this discussion,
*  the use cases that you view tend to be these axiomatic, of course we can do full, we thought
*  in the late 90s we could do protein folding by fully searching the search space. It's just not
*  surprising to me that we can learn distributions and spit them out. I feel that's a very different
*  statement than saying now we have a model that can navigate the universe in a way that is
*  predictive of all of the complexities of it. Maybe another way to think of this is we've spent
*  3,000 years doing our best and writing it down and we can create a model that can learn from all of
*  that and do what the mean human being would have done in the last 3,000 years. But the problem is
*  the stuff that we're doing tomorrow by uniqueness, a lot of it's going to be new. That's just how the
*  universe works and we're going to have to either build a machine that can do that, which we don't
*  know how to do, or we're going to have to do it ourselves and let these machines do the mean task.
*  So do you have an account of or a theory of what it is that you think humans are doing that the
*  models can't do today? I mean two things. One of them and the most important one is we experience
*  the universe and we abstract it into concepts. That's very common. Why do you think all the
*  budget is moving to post-training by the way? What's your thesis of why so much budget right
*  now is moving from compete to post-training? Ease of use is a huge one. I would still
*  guess it's probably a minority of budget if you're talking like Lama 400. I don't know.
*  Lama 400? I don't know. They said they had 10 million messages. I know how much multi-pass costs.
*  Let's say it costs $15. We're talking a budget between 100 and 200 million, which anecdotally
*  it seems about right based on what I know of the industry. But yeah, that's about half.
*  And so what I would argue is we're very good. Models are very good at taking the output that
*  humans create and being able to reproduce that distribution. They're very good at that. This is
*  why Scale AI is Scale AI and all these companies are so successful. That's not the game. The game
*  is looking at the universe and creating the supervised data. That's the game. And so I think
*  one model to look at this is, again, human beings have been around, let's say, in a capacity for
*  writing things down for 5,000 years. So you've got humans for 5,000 years that have been looking at
*  the universe and doing this thing that models cannot do, which is making a decision like that
*  is a rock, then that is a dust, and this is a concept, and this is a relationship, and I'm
*  going to write it down. And then as a group, we're going to synthesize these ideas and work at these.
*  And so we've got this almost platonic representation in our heads of the universe,
*  and that is very structured. So we did all the hard work. That is hard work to take this untamed
*  universe and reduce it into words and concept. That's hard. No LLM that I know can do that.
*  Not even close. But then once we've done all of that hard work, is it surprising to you that there's
*  structure? We did all this work. Of course there's structure. So you take that structure, you put it
*  into an LLM, it learns the structure, and it can spit it back out. So the very specific thing that
*  these LLMs can't do is look at the universe and recreate this kind of structure. And to be super
*  clear, that structure is not the universe. That's very different. Like a rock is a rock,
*  is an idea in our head. It's not representative of any single thing. Is it a grain of sand or rock?
*  I don't know. Is it a boulder or rock? I don't know. These are concepts we've created in order
*  to navigate the universe. They're not the universe. So human beings take the universe and create the
*  concepts. And that's structured because we need structure in order to do anything. The LLMs learn
*  that structure. It feels like the only thing that works is basically you can do exhaustive
*  quote unquote AI, which converges on search to learn distributions, or you do supervised learning,
*  which human beings are doing the hard work, in my opinion, by labeling things and everything else.
*  And then you just learn what the human beings have done. But to take the universe and actually to
*  reign structure and all that complexity, that's what we do. And it would be great if machines can
*  do it. I've never seen any evidence that they can. Yeah, maybe some glimmers up, but that's just not
*  where we are. So I just want to be super clear, because you asked me a very specific question.
*  It would be a very specific answer. Look at the universe and then come up with these concepts that
*  are useful, that are not the universe. They're concepts. They're totally separate. Like a rock
*  is not a thing. It's a human concept. But to take the universe and decide something is a rock,
*  that's actually all of the complexity and all of the energy is that step, which LLMs just don't do.
*  Yes, this is why I think language is such a tricky domain. By the way, the platonic representation,
*  you probably saw there's a paper titled exactly that. But it doesn't tell us much about this
*  particular question, because it is still operating in the language domain. And it is in that way,
*  able to piggyback on our prior art in terms of useful abstraction of the universe. I do think
*  if there was a line of research where I would venture a guess that I think you maybe wouldn't
*  agree with, that maybe we could come back in a certain finite amount of time and say,
*  has this happened or not? And what would we infer from it? I probably would look at
*  this biology foundation model space and the sequence modeling. And you can imagine that's
*  going to be elaborated a lot. They didn't even use eukaryotic sequences in that initial EVO paper.
*  Let alone like expression data, transcriptome, proteome, whatever.
*  We know enough about the natural sciences to build predictive models when we have for a very
*  long time. I can simulate a supernova on a computer pretty accurately. I think it's phenomenal.
*  It's phenomenal that we have an approach to throw computer to problem that learning a fundamental
*  law of physics. But again, how is that any different than the fact that we've been modeling
*  physical systems for a very long time, other than the fact that in these cases, it allows us to
*  apply more compute at the problem. And we can solve problems that we don't have close form
*  analytics solutions to. It almost feels to me like an extension of simulation, which would be very
*  different than the claims around general reasoning. It's literally learning laws of physics,
*  which we've been doing since the beginning of compute. The creation of computers was for
*  ballistics. So the reason that we created computers is because ballistics are nonlinear. The trajectory
*  of ballistics are nonlinear. So we had people in rooms that would create logarithm tables by hand.
*  They were called computers. That's where the name came from. ENIAC shows up. ENIAC does it.
*  Forwarders at magnitude. It's about 5,000 times faster than a human being does it. And we have
*  a computer. And this is a perfect example of a nonlinear system, which is a trajectory with gravity
*  being done by a computer. Why is this not just a straightforward extension of exactly that like
*  we've been doing for the last 80 years? Here's my expectation. Tell me if you maybe we can make a
*  little friendly wager on this. I think that over the next year, we are going to start to see
*  scaled up foundation models for biology that are going to start to understand the super complicated
*  interactions between genes, between proteins in cells in ways that are inferred from inputs and
*  outputs, learning these higher order concepts in the middle, which we could not simulate
*  because it's computationally just intractable and which we certainly don't have a closed form
*  solution for either. If that does happen, that would seem to constitute to me an instance of
*  looking at the world, looking at basically raw data of sequences and just
*  lice cells and what proteins were found in them and whatever, and learning meaningful abstractions.
*  And I would expect that we'll start to discover stuff by doing counterfactual experiments on those
*  models. In other words, tweak a thing, see what happens, find medicines, find disease patterns by
*  make a tweak, see what happens. What if we change this counterfactually and then go validate those
*  things in the wet lab? If we start to see that happening, would that to you represent phenomena?
*  I fully expect that.
*  But how does that not constitute looking at the universe and figuring out what's what?
*  Oh, for sure, for sure. For specialized subdomain, you absolutely can learn distributions.
*  100%. Listen, I've implemented Navier-Stokes, fluid dynamics, and this is a turbulent chaotic
*  system. So we've known how to implement very complex systems with computers, for sure.
*  And especially in very specific domains where we could reduce these things to a few fundamental
*  forces or we can reduce these things to mostly linear systems. The previous version of this is
*  just all the computational methods where we would take a problem that we know and we'd actually
*  experimentally determine, like it's just experimentally, we'd say, okay, this material
*  behaves this way under this pressure and this heat and it has these properties. And we take what we
*  learned experimentally and we'd create these models and they would do pretty good at simulation.
*  And I would say this is a very straightforward extension of that, which is you look at how
*  the world works in a constrained situation and then you can predict what would happen
*  in the constrained situation. But just like simulations, remember we could do this with
*  simulation. We've been able to do this for a very long time, right? So we could experimentally
*  determine how different materials work and then you can actually simulate a new system based on
*  those. This is how we do most industrial design today anyways. So my question to you is how is
*  this fundamentally different than that or not a natural extension than that where you're giving
*  it a system, you're learning some fundamental properties, you can do something new, but that
*  doesn't mean that you can disobey the laws of physics in predicting stuff that computers can't
*  predict. It's not obvious to me that it can simulate complex nonlinear systems that are
*  chaotic for long periods of time. I think this is just yet another step on this kind of like we have
*  computers simulate physical stuff and we're simulating the next thing with the next tool.
*  Does the parallel making make sense? Like if you go to like in the 80s and 90s we would literally
*  empirically test physical matter. We didn't know how the physical matter worked. We just
*  empirically tested. We'd have it has this opacity under this heat. It has this tensile strength.
*  We'd use that to build databases of materials, equations of state we call them. This is how they
*  interoperate. We'd use those when we're doing simulations and we'd simulate what happens when
*  a car explodes, what happens if an airplane runs into a building, like all of these things.
*  None of those instances worked. They were simulations and they were very accurate.
*  None of them came from like first principles. They are all empirically, but that has its limits
*  because it didn't solve climate prediction past 15 days. It didn't allow us to simulate life.
*  To me this is just computers being attached to another domain which thank goodness we've
*  come up with a great tool that's going to give us a little bit more insight,
*  but it's a little bit more insight is what it is. By the way we had the same discussions in the
*  simulation. This is why by the way we stopped playstations from going to the Middle East.
*  That was exactly it. So again I worked I actually worked in the nuclear weapons program at Livermore.
*  So I was very close to the previous version of these discussions like oh my goodness if Saddam
*  Hussein gets playstations he's going to be able to simulate nuclear weapons right like just totally
*  misunderstanding that the ability to simulate something is not some runaway process that's
*  going to allow you to recreate a world or anything like that. It's a very specific tool for a very
*  specific situation, but we were here before when it was 25 years ago. Yeah there's certainly no
*  arguing that past predictions of AI progress often didn't pan out and that does seem like it's
*  not a near-term future that we can dismiss either. The other argument is that they have all panned
*  out exactly as you would expect and they're going to continue to and this has been steady progress
*  for 80 years and it's been a super useful tool and every time we unlock something people are like oh
*  poo that wasn't AGI so that must not have been AI and they're like focused on the wrong goal and
*  it's a very unspecified goal and instead it's like any other computer science primitive where it keeps
*  solving problems and we should continue to solve problems with it which is the way that I would
*  view it. It's interesting because people talk about summers and winters and not panning out
*  like you just did but it couldn't be further from the truth. It's been a foundational primitive of
*  computer science that we've been using very effectively and we continue to use more effectively
*  and I don't see why that won't just continue to be the case. Yeah I like your vision. I think what
*  you're describing is almost an ideal scenario. But I do think this is an important foundation. Let me try
*  to bottom line your perspective. I'm still a little confused around what would count.
*  Is there what would be the evidence of if the fundamental thing that humans can do and have
*  done through our history that the AIs can't do is look at the universe and figure out the right
*  abstractions and come up with the right concepts that compress it in order to make sense of it
*  and I agree it's very hard to say what they're doing in the language domain because we already
*  did that work and they're learning it from us. I try to describe something in the biology domain
*  where it's like it seems like they're starting to show signs of doing that and I could believe that
*  they would and then you sort of agreed but then now I'm confused as to wouldn't that count as
*  doing that and then it seems like the response is well that's just in one domain but it doesn't seem
*  like there's anything that would prevent it. Certainly there's a huge leap in generality
*  with this latest generation of system so I do imagine just shoveling all the modalities into
*  one model. We've already got text vision and audio in GPT-4. Why not the true GPT-5 would be like
*  biology data and weather data and like pictures of deep space and solution simulations and just
*  battery simulations, material science, whatever. Throw that all into one thing and if it can do
*  that then it's definitely not going to be constrained by one domain anymore so I'm still a little lost
*  as to like exactly what the limit that you see is in terms of why it doesn't become a system that's
*  more powerful than people. I'm so glad you reduced it to this. I think this is great right and there's
*  two things. There's this notion that language reasoning is general which a lot of people believe
*  but you don't seem to be on that kind of kick so let's put that one aside and you're more on the
*  like learning properties and simulating properties of the universe which is totally fine so what I
*  would do is I would just bring you back to everything we've learned about simulation
*  which is even when you know all of the properties of the system and you can simulate
*  you just don't have the computational capacity to simulate non-linear systems. We don't have
*  the materials or the energy or anything. It's literally like a compute problem. We have code
*  bases that have been around for 20-30 years that simulate all sorts of crazy stuff and yet they've
*  got limited utility for exactly this reason. The universe is just so complex that they're useful
*  for a little bit and so if it turns out and I'll give you a very specific one that we can bet.
*  If it turns out that these models somehow change that compute trade-off where it can simulate
*  non-linear systems in ways that traditional stuff can't, I'm 100% with you but that's not what
*  they're doing. What they're doing is they're inferring stuff that we haven't been able to
*  infer by looking at data. That doesn't mean that they can be predictive in a way that kind of
*  disobeys our understanding of compute requirements and like a Raleigh-Taylor instability is basically
*  if you have two liquids that are on top of each other with different densities and that is one
*  Raleigh-Taylor unstable system and if you perturb it like you get these kind of like just amazing
*  kind of chaotic turbulent things that happen. We have been looking at this problem for 30 years
*  and we have no idea how to actually predict what will happen. We just know roughly what they will
*  look like but we don't know like the specifics and AI systems are way less efficient than an actual
*  like code written for simulation. So to think that it can tackle those types of problems I just don't
*  see any indication. I mean I view that we have these kind of modalities of compute that we can
*  throw up problems right. So the most efficient is basically imperative programming where you give
*  the computer a set of instructions and know exactly the rules right. So that's just normal
*  programming. Then we have another modality which is declarative programming and by the way the first
*  one's the most efficient right it just does the rules. The second one is like the end state that
*  you want. I know the end state but you know it very specifically and then the computer figures
*  out what to do. This is declarative programming and so to come to the solution it has to do all
*  of the logical closure stuff so that requires more compute right and we don't even know how to bound
*  that compute. That's why like databases when you run queries are not bounded so that's declarative
*  programming. Now we're in AI where you don't even know what the end state is. You're just like I have
*  a whole bunch of data and I want you to find patterns in that data right. That requires even
*  more compute so it's even less efficient. So it's another modality of compute. It's one we've been
*  fighting for a long time but it doesn't change the nature of computers. They're still systems and
*  they're still computers and they still have the same limitations independent of what distribution
*  that they learn. And so if it turns out that these things can like simulate systems for a period of
*  time longer than normal simulation then I'm with you. I'm like this is breaking the laws of physics
*  but until then it feels to me like simulation where you just don't know all of the rules but
*  it's learning some of the rules. Yeah I guess I let I think about it less in terms of simulation
*  and more in terms of how effective the choice of actions can be at any given time step. Like
*  I'm not simulating the universe. Humanity as a whole is not simulating the universe but we're
*  all just taking our local conditions and our sort of general sense of our own selves and goals and
*  trying to do the next step at any given time. And it seems like our overall efficacy through
*  our lives is the integral if you will over how good our choices are at each given time step.
*  And that doesn't depend on any huge simulation of anything like irreducibly complex. So then if I
*  imagine an AI it seems within reach to imagine an AI that can do something very similar to what
*  I'm doing which is have a goal, look at its immediate surroundings, look at what it just did,
*  look at whatever other context it may be given and pick a next action and potentially be better
*  than me at it and potentially quite a bit better. And then that to me seems like enough. If it can
*  do that then I feel like we're in an unprecedented environment where we now have fundamentally
*  pretty alien and not super well understood things that can take more effective actions in many
*  given contexts than I could. And then that to me is like where I start to turn the conversation
*  toward what sort of safeguards should we have in place? Just again because these conversations
*  tend to be so modeled. If that action requires interacting with the physical world it has to
*  simulate the physical world. It just does, right? Like it has to understand like dynamics and
*  ballistics. It has to understand what happens if someone throws a rock at it or if it's like in
*  water or if the weather's like I mean that's how you navigate the physical world. It's really why
*  we created computers, right? It was because these are very hard things to do. And then if it's not
*  that, if it's not interacting with the physical world then it is interacting in this kind of
*  language domain that we've created and I agree you'd be very good at some subset of those things.
*  There's zero indication it'd be good at new things and that's what we're actually very good at.
*  And again without actually having a model for all of these things that we understand like the
*  distributions, we understand the mechanisms, I feel like we just use words and the words all make
*  sense. But like complex systems we never know convergence and divergence without actually
*  specifying the system. And I feel like for these conversations we just don't have a system we talk
*  about and so it's always we live in the world of like rectangles and arrows and somebody takes a
*  rectangle and they have an arrow that goes back to the rectangle. They're like ah we've got a virtuous
*  cycle without actually specifying that if you have diminishing marginal returns you don't go anywhere
*  or you're doing the same stuff or whatever. And so I think this is incumbent on all of us to actually
*  understand the systems we're working with and then come up with these basic views and properties to
*  make sure at least we understand what the convergence properties are. I'm sorry that
*  was a very muddled thing to say but I feel that until we talk about specifics it's very hard to
*  make concrete statements in this. Yeah it's tough. We're in a tough environment because things are
*  moving really quick and we are pre-paradigmatic right on understanding a lot of these
*  things. Again I think the progress has been incredible but we're just starting to crack
*  the black box. Okay so let's change gears because I think this is probably certainly gives everybody
*  enough to to get at least a good intuition for our relative philosophies on this. So what do you think
*  we should do right now in practical terms to regulate AI if anything? The regulation one is
*  sticky for to me for two reasons. The first one is we don't even have a definition of AI
*  and so I think it reduces to regulating software and then for that I would say we've been
*  regulating software for a very long time and there's a broad robust discourse around that and I think
*  we should make whatever conversations we have part of that broader discussion. So yeah just trying
*  to bring a couple different lenses to this from existing rules. We obviously have liability rules
*  for all kinds of products not just software. It seems like there is a general kind of trade-off
*  that companies make with the government where it's like we want to have safe products that we can
*  generally count on as being safe. Companies don't want to be sued every two seconds and the general
*  trade is like you agree to implement some standards. If you implement those standards you'll be shielded
*  from regulation and that does vary right across like lots of different product types. You know
*  cars are very different from milk and so on and so forth but we don't have anything really like
*  that for AI and not a ton really for software either. You probably know better than I do in
*  terms of some like niche areas. I mean cars have a lot of software. Yeah certainly cars are
*  increasingly software products. And airplanes have a lot of software in them and medical devices have
*  a lot of software in them. So in all these regimes there's tons of testing, there's tons of verification,
*  they are engineered and demonstrated to a standard but we don't have those like standards really for
*  these AI systems yet. I don't know what the distinction is between AI and software is. I
*  really don't. Like I have seen the definition used in these regulations. It's so broad that really
*  could include all non-trivial software and I don't say this to be a polemic and I don't say this to be
*  difficult. I'm saying this very clearly. They literally say a system that can whatever navigate
*  and change a virtual or physical system. I mean these are so broad right. So we're really talking
*  about software. That's what we're really talking about. We have what 70 years of history regulating
*  software in many domains and I think that regulation is very important. I'm not a libertarian. I'm a
*  lifelong liberal like a very moderate person. I'm just saying this discourse has been around for a
*  very long time and we should continue. And if there's an area that software is being pushed,
*  an area that we need to have some sort of protections, we should add them to it right. But
*  that's a very different statement than saying AI is somehow paradigmatically different. There's
*  just like literally zero indication that it is. And then try to somehow regulate a computer science
*  premise like regulating a database. Let me give you like a specific example. So by the way we
*  went through this during the rise of the web and the internet. And so a lot of my formal studies
*  were in networking and so I was actually pretty close to these discussions. And at the time there
*  was this concern that with the rise of the web and the internet, you have actual paradigmatic
*  shift. It's not just software, it's different. And we actually had examples like the Morris
*  worm had taken out a whole bunch of stuff. We were running critical infrastructure on it
*  and there was this notion of asymmetry which actually changed the defense posture of the
*  United States. And the notion of asymmetry is the more that you bought onto the technology,
*  the more vulnerable you were. So as opposed to mutually assert destruction, which was our
*  doctrine before, we now have this new thing which is like, oh my goodness, we're the most vulnerable
*  because we've adopted this. So you had two very compelling reasons to want to regulate this stuff
*  and be afraid of it and do close source and whatever it was. You had like examples of taking
*  out critical infrastructure and you had this change in posture. And yet even that, which we have none
*  of those today with AI, none. We don't have examples of like this or like there, like literally it took
*  out computers and hospitals, right? We don't have any examples of paradigmatic shift. And even then
*  the conclusion after very robust conversation for a long time is you regulate the applications,
*  you regulate the industries, you don't regulate the math and the computer science primitives.
*  All that I would ask at this AI discussions is either A, demonstrate as paradigmatically different
*  and if you don't have that, then B, let's absolutely regulate and have regulations. Let's
*  do it as part of the broad robust discourse we've had over the last 20 years with really smart people
*  in much more dangerous environments. Again, I think that we put all of our fears in AI,
*  but you realize like we're running hospitals on the internet for the first time that were being
*  taken out and it was impacting patients. That's what we were dealing with. And now we're dealing
*  with theoretical threats on bio weapons that don't even exist yet. I just feel like we've all gotten
*  mad and forgotten where we came from and the discussions that we've had. And all I'm trying
*  to do is saying we've been here before. It was actually much worse here at the conclusions.
*  Let's draft on all of that work and share knowledge.
*  I guess to venture a distinction or what makes the technology a paradigm shift,
*  I would probably zero in on the fact that they are trained, not engineered and that maybe a better
*  thing even than that would be that the creators of the models generally don't know what they're
*  going to be able to do. And even at deployment time don't have a very robust account of what
*  the capabilities of the systems are. You could point to things in the past and be like, oh,
*  you didn't expect this out of whatever, but this does seem to be qualitatively different that they
*  just train, train, train, train, train a long time. Especially if you look at base models,
*  right? Base models are totally unpredictable and nobody really knows. I think one of the reasons
*  that people are putting so much resource into post-training is to try to get control.
*  And it's only sort of working. Yeah. So this is the thing is when you're talking to a internet
*  guy and a distributed systems guy, it's just like none of the systems that we worked on,
*  we understood the implications of. Think about the internet. Like every sociopath becomes your
*  next door neighbor. What does that even mean? What does it mean to put kids on the internet?
*  What does it mean to have your business on the internet? What does it mean to put critical
*  infrastructure in the internet? There is no model for how any of this behaves. There is no way to
*  make computer systems provably correct. Like we didn't have any of that. A lot of the early
*  discussions when we were creating TCP was to prevent congestion collapse. Cause we thought,
*  oh, like everybody's going to like the communication protocols. They're going to all decide that there's
*  an issue on the internet and then they're all going to like back off. And then at the same time,
*  they're going to kind of correlate and kind of talk again. And who knows if this takes out the
*  entire internet, which run critical infrastructure, like people underestimate like how complex and how
*  little we've known for any system that we've built with no idea. And I guess having been there,
*  like during these times, a lot of computer science is building systems, especially distributed
*  systems that have emergent behaviors that are non-predictable, that are a tool that you use to
*  solve bigger problems. We've got a lot of approaches to doing that. We've developed over time. We will
*  develop new ones and it's just not clear at all to me. And again, like the internet is my favorite
*  example to hold up to this is literally we changed the social structure of humans. They're totally
*  unpredictable. We're putting critical infrastructure on it. We had examples of like emergent stuff that
*  was like worms weren't possible before the internet by definition. So we actually had like provable,
*  not demonstrated new attack vectors. And yet the conclusion was, listen, we're going to keep this
*  stuff open. It's very important. We're going to regulate the uses of these things. And this was
*  the primary growth driver of the last 20 years. And so either you thought that decision was wrong,
*  but that's a very different discussion. We could have that discussion. We could re-litigate those
*  10 years of discussion, or you can say, you know, this is the same thing, except for like a softer
*  form of it, because we have no proof that these things are paradigm actually different. I would
*  consider these wildly baseless claims. And so why don't we use the same method that we did before?
*  The couple of points I wanted to follow up on, but I really want to ask your question on,
*  or really want to ask for your view on what companies should do, right? In terms of the
*  proposed regulations applying to everything, we do have these like compute thresholds, the 10 to the
*  26, whatever, I don't want to get too bogged down and like, well, that could be a slippery slope,
*  or they could change that threshold or whatever. I agree if they all of a sudden drop the threshold
*  dramatically, that would be like very heavy handed and counterproductive. And the open source of the
*  last couple of years has been, I think almost everybody agrees good for everybody, including
*  even bigger safety hawks that are backing SB 1047, I think are quite on record saying the open
*  sourcing of for example, llama three is good even for safety, because it gives you know, more people
*  something to study. Forgetting about rules or people imposing on people, like just to be like,
*  good companies to be good developers of technology. What do you think the leading companies
*  should be doing? How much should they invest in? What sort of standards should they have? What
*  testing protocols should they be committing to? So on and so forth? Yeah, I think this is a great
*  question. So I just have to make the point like there's no correlation between danger and compute.
*  It's so silly. It's like this is made up correlation. And so I don't think like compute
*  linux make any sense at all. I think it's in some ways it just sounds good, but there's just
*  there's zero correlation. We've been building systems for a very long time that have like social
*  and ethical responsibilities, right. And these are ones with user generated content and user
*  interactions and companies as a result, either through regulatory action, which I fully support,
*  or through self policing have identified behaviors the software should not do. And they've built
*  a lot of systems around those. And I would say that should absolutely should not change.
*  Like Roblox should protect miners, social networks should protect people from certain types of
*  content. These are the things that we've evolved as an industry as you know, somewhat of an ethical
*  basis or a principle basis. And some of it is regulatory and some of itself enforced. And I
*  think that should absolutely continue. But realize that while we were doing that, we weren't putting
*  compute limits on databases. And we weren't regulating computer science primitives. And we
*  weren't inhibiting innovation of startups. And that's what we're doing now. And that is a paradigm
*  shift. And that is a doctrine shift. And it's really scary. And I am not a political person.
*  I'm very happy building systems. The only reason I've been so vocal is because I find this so
*  dangerous. And once this is done, I'll be very happy to like not say a word about it again.
*  Well, you may have a while to go before that. So let's say a couple of just kind of concrete
*  things. I was on the GPT-4 red team back 18 months ago. One of the things that I tested was,
*  could the model be a convincing spearfishing attacker? And surprise to no one probably at
*  this point, it could. This was the early model that hadn't been through all the RLHF yet.
*  Although when they deployed it, it still did that for several iterations. And now finally,
*  they've got it to refuse. If, for example, a meta puts out an open source model, and they haven't
*  done a thorough job of getting these refusal behaviors in place. And you can just go to it
*  and say, hey, this was my old prompt. You are a spearfisher. Your job is to talk to this person
*  and get their mother's maiden name or whatever. And it'll do it. And then somebody out there does
*  it and people are harmed by that. Do you think meta should have any responsibility or anything
*  to answer for in the legal system for their contribution to that problem? Or is that all on
*  the end user? My rule of thumb for general systems is that unless they were purposely trained for
*  malicious behavior, they're general systems. Would you say the same thing about a database?
*  That's interesting. A lot of computer security started with tools that were like scanners that
*  could be used for malicious purposes. This discussion was enormous back then. So remember
*  back in the early time of the internet, people would come up with NMAP or any of these scanners
*  that would determine vulnerabilities. And some of them would even actually exploit them. Remember
*  Metasploit? And there's all these discussions. All these people are building these things and
*  they're using it for malicious purposes. And you know what? We just decided that it's actually
*  the criminals using them. That's who we want to go after because a lot of good people use them for
*  positive purposes. And oh, by the way, the history of cyber security is built on open source in these
*  tools. Companies like Tenable came out of these tools. So if history is any indication, you want
*  to regulate or you want to definitely criminalize bad people and bad behavior, but not the tooling
*  because the tooling is very fundamental to defense. So what I'm saying is even more stringent,
*  it's more regulatory heavy than what we did with the internet. Literally, you could build
*  exploit tools 20 years ago and release them open source and you are not liable if somebody
*  use it. And that was purposely built for exploiting. I'm saying like if somebody's
*  perfectly building a model for something illegal, okay, that's bad, right? So that's even more heavy
*  heavy. I'm more of a regulatory hawk on this case, but I don't think general purpose models that
*  aren't specifically trained for this stuff, the person that created it is generally liable. That
*  would just basically say software, you're liable for creating software if somebody use it poorly,
*  which I think this would be the biggest kind of inhibitor to innovation and the biggest chill on
*  software we've ever imposed. About a distinction or some sort of gradations on the autonomy of
*  the system, though, it does seem like a database on the one hand is inert until it gets a query
*  and a language model in the raw is inert until it gets a prompt. But I've been testing a lot of
*  products. There's a new class of product I'm sure you've seen often called calling agent,
*  where you can go in, give it a phone number, tell it what you want it to accomplish,
*  and it will just call the person and have a voice conversation real time with that person.
*  They are often marketed as agents and they have the conversation entirely autonomously until either
*  the goal is achieved or the person hangs up or whatever. Now, if I prompt that agent to
*  scam you or to threaten you or to harass you or whatever, clearly I'm in the wrong as user for
*  doing that. But would you put responsibility on the company providing that agentic AI as a service
*  as well or would you again shield them and say it's all in the end user?
*  Why not the telephone company? Why not the mining company that...
*  Exactly. You got to draw a line somewhere, right? The question is where to draw the line.
*  Yeah, exactly. The illegal behavior. General computer science primitives are very useful
*  for solving problems. They may save the human race. To your point, we're going to go ahead and
*  we're going to solve biology and a bunch of other stuff and that's just another app. There may be
*  whatever. These things solve grand unified field theory and physics goes away discipline and that's
*  another app. We're just going to keep solving problems and that's amazing. So we want the
*  primitives to be primitives. If people do illegal behavior based on them, then 100% they should be
*  criminalized. We don't even make guns illegal. We literally don't even hold gun makers liable.
*  And you're talking about... We are outliers in that.
*  You're talking about hypothetical threats for a very useful primitive that's shown far more good
*  than bad. I just feel like we've all gone a little crazy on this one. By the way, this is a dramatic
*  shift in sentiment and I think I know where the sources came from, but it's not what people think
*  it. I really think that we're just a little bit off base, unfortunately. I'm not sure what I think
*  about open source model releases entirely. I do think it's not unreasonable to demand some testing
*  before release. When it comes to these agent calling companies, I actually come down pretty
*  firmly that if you are going to offer an autonomous system as a service, I think it should be on you
*  to make sure that your system refuses egregiously criminal requests.
*  And that doesn't seem like too much to ask. No, no, no. I think that's totally fair. Fair enough.
*  Yeah, yeah. Listen, I want to be super, super reasonable. If you've done all of the work to
*  do criminal behavior, except for a very modest anybody can do it, then I... And that's the
*  primary use case. I'm all for coming in, but that's a very different statement than I've created a
*  computer science primitive that's very useful to a lot of people. To me, it's miles away.
*  You mentioned protocols a couple of times, and there's also this question of how much we can trust
*  open source models. Anthropica has had this paper on sleeper agents, and the concept there is
*  basically data set poisoning, model poisoning. You can create malicious models that can potentially
*  even attack their own user. So open source models, they are great in many respects.
*  I do see a future in which it doesn't seem like we'll be able to just trust any open source
*  model. Certainly, you can't just download and execute any binary right off the internet.
*  You shouldn't do that. You should probably go through the app store and get the approved
*  version most of the time. It seems like models are headed that direction too, because of the
*  sleeper agent unpredictable behaviors that could be maliciously coded into them.
*  What technology solutions are you excited about for making sure that this open and free exchange
*  remains healthy and trustable as opposed to collapsing into a you can't trust any model
*  you find on the internet equilibrium? Can I point out how silly the whole sleeper agent thing is?
*  How is this different than any arbitrary back to work any piece of software that we've been
*  dealing with since forever? One big difference is in principle, if you read the code of whatever,
*  right? In theory, you would be able to tell, but we don't have any tools that can tell.
*  Absolutely not the case. If I give you a binary set of instructions, there's no way to actually
*  determine behavior. This is computer science. That's why we don't go around downloading and
*  executing random binaries, right? I'm just saying we can talk about software, and I think it's great
*  to talk about software, but we somehow keep making AI these special unique things. And in some ways,
*  they definitely have new properties and other ways, they're actually not that different,
*  like this kind of notion of a sleeper agent. Binaries have had the potential for backdoors
*  for a very long time. We provably can't detect these, right? It converges on the halting problem,
*  right? So it's the same thing for models. And I just don't see why you wouldn't just use the same
*  things that we do with binaries, which is Apple in the app store will decide to have some sort
*  of criteria. And maybe you just don't download some random model if you don't want to. And
*  personally concerned way less about the model that might tell me something stupid or something
*  offensive than a binary that could like wipe my hard drives, right? And so I don't think it
*  changes that game at all. At least maybe I'm missing some, maybe you can educate me. What could a model
*  do that a binary can't? I don't know. It's a good question. Certainly, models can do a lot of things
*  that traditional software can't, right? When I advise people on how to build AI apps, I usually
*  say, if you're going to have an AI app, the reason you're going to use these, at least these new
*  general purpose models in an app is that there's some cognitive task that for practical purposes,
*  you can't reduce to explicit instructions. Whether that's is this a cat or a dog or whatever,
*  there is something that you can't reduce to code. So they can do definitely just categorically,
*  a lot more stuff. They can, for example, trick people. You could imagine a Liza bot or whatever
*  doing dirty question extraction from people. So your concern is exploiting the human
*  via social interface versus anything having to do with the machine. Is that your concern?
*  I don't know. I'm not that great of a hacker, but I think you could also have a sleeper agent
*  model that, oh, great, download and run this thing and it's going to help you use your computer.
*  But maybe it also goes around looking for things in your computer and maybe it's actually better
*  able to find them than traditional software because it can sort of search more effectively
*  and have a better understanding of what it's looking at at any given context. Abstract,
*  people do all sorts of things like if I want to email myself my credit card number, maybe I
*  put a star between all the numbers and then it breaks regular expressions. But maybe a model
*  just looks at that and that looks like somebody trying to trip up a regular expression on a
*  credit card number. I don't know. I think it just feels like there's a lot. The surface area of
*  these, my general reasoning is the surface area of these things is vast and there's just a lot
*  of unknown unknowns. Yeah. Again, I guess from my standpoint, if somebody wants to break into your
*  computer, probably the best way is with some binary that'll do a backdoor and then almost all
*  computer attacks are humanated anyways. They get a bunch of information, they send it to a group
*  of people who analyze it and maybe you can put all of that intelligence locally at some point.
*  We're definitely not there yet and it can do something but I feel like that's at this point
*  science fiction. You can do a lot of automated stuff today with binaries. You can absolutely
*  put humans in the loop. You can do intelligence stuff. You can social engineer. You can do all
*  of those things today. I don't know if there's a paradigmatic shift. I have not seen it. If there
*  is and you actually have demonstrations of this, then maybe it warrants a discussion but we're not
*  there yet. I do think we've got a lot of safeguards in place when it comes to binaries. I think we've
*  all learned not to download the wrong ones and we should. Here's how sensitive we are to this
*  question. No joke, I was in Japan last fall and I got a phone call from my mom and my mom's like,
*  oh, Martine, where are you? I'm like, oh, I'm in Japan. She's like, no, you're not. I'm like,
*  I am. She's like, oh, talk to your father. It's a very awkward call. My dad gets on. He's like, oh,
*  he's like, where are you? I'm like, in Japan. He's like, oh, I just had somebody call and said,
*  it was you and I could hear you but you're a little bit muffled and you're in prison and I'm
*  heading out the door to give $10,000 to get you out of prison. Like literally this happened to me.
*  And it was my voice and they were almost convinced to do this. And so I posted this on Twitter
*  and everybody's like, oh my God, deep fakes. This is what happens in the age of AI. And all of a
*  sudden there's this indictment AI. Well, the priest before it talks to the police, they actually know
*  the team that does this. It has nothing to do with AI. It's literally a human being that muffled
*  their voice and to pull this off, it's been going on for a very long time. And so I just feel like
*  we ascribe these superpowers to AI that have not been demonstrated that are still possible today.
*  And even if they could do the same thing that you can today, which they absolutely can,
*  is not a paradigmatic shift. And maybe if we do see that happen, like we should say, oh, the
*  safeguards we have in place are not enough. But I don't think that we should do that preemptively
*  because you're going to inhibit the innovation, the proliferation of these things, which is,
*  it really is a different way that we will as a society view the development and the use of
*  software. And I think that something that has added so much good, we're going to, I think it's
*  almost like a moral bet. Like we will reduce the amount of good we do in the fear of something
*  that we just haven't even demonstrated that's bad. I do worry about that. The nuclear outcome
*  for AI would definitely be a real tragedy. And I'm a big proponent right now of two projects
*  I'll highlight that I think are like maybe the most important things going on right now. One
*  from Google DeepMind of an episode coming soon on the med, what was MedPalm, now is MedGemini.
*  And they're just grinding, man. It's like dialing in the diagnosis, really strong evals,
*  expanding modalities to radiology, all these other things. And I love it because I like,
*  I think we can all love it because we all want everybody to have this sort of access to quality
*  expertise. And obviously it's like all too scarce. I also love it because it does demonstrate
*  pretty compellingly, although as always, we can debate around this, that there is potential for
*  extreme value today, even kind of the current level of systems without necessarily having to
*  like 100x or 1000x or 10,000x the scale of the training runs. I asked the guys there,
*  do you guys think you could create your AI doctor vision if Gemini 1.5 Pro was the blast and best
*  model you ever got to build on? And they were like, yeah, I think so. It would take us a
*  little longer. But yeah, I think we could probably make it happen. And OpenAI has a similar one.
*  They're working with Harvey, as I'm sure you are familiar. They have a custom model that they're
*  doing for them. And same deal, right? They're working on GPT-4 base. It's like incremental
*  compute, not orders of magnitude compute. And they're again, just achieving huge gains. I
*  think it was like 97% preference ratio of the dialed in model to the original base.
*  So I am very much with you that I would hate to see us end up in a spot where professional licensing,
*  regulatory capture, rent seeking prevents us from getting the value. And I'm definitely vigilant
*  against those sorts of threats. The flip side for me is I would love us to understand this a little
*  bit better before we raced to the proverbial trillion dollar cluster or whatever that sort of
*  AGI super intelligence might be. Sounds like you ultimately just don't think that's going to
*  happen. I take it you guys will not be investing in Ilya's new straight super intelligence venture.
*  I would be delighted to invest in that. I mean, I honestly think it reduces to how people wake up in
*  the morning. And some people wake up in the morning and they're really afraid of the future.
*  And there's some they can't really articulate it, but there's something bad that's going to happen.
*  And they want to protect themselves from it. They're not really sure what it was. And like anything
*  that has the spectra of it, they'll find it in there. That's a constant voice in every technology
*  shift. It's just absolutely constant. And there's other people are like, listen, we're the ones who
*  created this, we got this stuff, it turns out that the universe is very complicated. It turns out that
*  we use tools to protect ourselves, not the opposite. And of course, most things are going to
*  use every computer, everything that we create. But I believe in us as kind of
*  meaning creatures to have innovation, it just comes down to the basis of innovation. And I
*  tend to think that, listen, I don't think that there's, I don't think the universe gives up the
*  secrets easily at all. I don't think any single system will ever solve all problems, not even
*  close. I feel like everything is a sigmoid. I feel the universe is heavy tailed. And so the more
*  tools we have, the more we're enabled to help ourselves. That's really what I strongly believe
*  every indication of this current AI to me suggests that this is the case here. These are
*  still computer systems. And so I think that any inhibition of innovation on the stuff that's
*  outside of a 30 year discourse, again, I'm thinking very moderate position here. I'm like,
*  we regulate software a whole bunch. We should continue to do that. These are hard-earned
*  regulations. Let's continue to do that. But let's not inhibit innovation unnecessarily based on the
*  precautionary principle. I do want to have just one quick analogy for you. So you're familiar
*  with the whole CRISPR thing, right? Listen, CRISPR like that changes the human genome. It doesn't
*  just edit like one thing. Like if you like change a human being with CRISPR and that the human genome
*  is different and they have kids that gets passed on. So what happened when Christopher got invented?
*  There was like some self-policing. There wasn't really a lot of regulation. A bunch of people
*  went and studied it. And it turns out to be a very useful tool for humans to use going forward. And
*  so there's one of two views there. One of the views is like, oh, we got it wrong. We should have
*  basically regulated it. But that's not what we did. We did something actually very different.
*  And this is something that edits the human genome. And so to me, it's just so mind blowing that we're
*  talking about computer systems that don't edit anything, that we actually understand the properties
*  of. I could literally sit here and talk about like the bounds of all of these things. And yet
*  we're talking about constraining this new innovation. It feels like we've just entered
*  like this kind of weird dark period in our emotional state with regards to computers.
*  And I think a lot of it is social networking casts a lot of shadow. I think a lot of it is
*  both from like red pill to bunch of people. And so we're just in this kind of mindset that we just
*  want to protect ourselves from something that's not a threat. I wish I was so confident. Have you
*  ever heard of gene drives just to raise to see and raise your CRISPR? So it's a CRISPR elaboration.
*  I don't know if he's the inventor or one of the inventors, but I have an episode coming up
*  with Kevin Esfeld, who's a biologist. Brilliant guy. The gene drive concept is that it will copy
*  itself into the other chromosome and thus it becomes super dominant. So if it gets inserted
*  in one generation, next thing you know, it's in both chromosomes. And then when that generation
*  reproduces, it copies again. And so basically it's going to take over the entire population
*  with this gene. The only way that they know to combat that is to have another gene drive that
*  comes in and tries to neutralize the first gene drive. But I guess the reason I raised that is
*  it seems like the real kind of core disagreement between the safetyists and the, you know, let's
*  not worry about this or it would be premature to worry about this is really the expectation of
*  how powerful is it going to get and how broad would the impact be? Because the CRISPR versus
*  the gene drive, it's like those are very different technologies, right? One makes an edit,
*  one propagates through all future generations, and that difference is everything, right?
*  Yeah, totally. It seems like the same thing basically is true for AI.
*  So I totally agree with this, which is like, I am all for if we've identified one mechanism
*  that has massive destructive power. For example, listen, I worked in nuclear weapons, right? I
*  totally understand the impact of nuclear weapons. You have one relatively simple mechanism that has
*  massive destructive power, and it could be the case, certainly with something biological,
*  because you do have exponentials when it comes to replication, right? Just like with a nuclear
*  bomb, like once you hit criticality, you get an exponential. With biology, you also get an
*  exponential, right? That has not been the case with the computer systems. There's zero indication
*  that will ever be the case with computer systems. These are not biological systems,
*  they're computer systems. So until somebody actually shows that in a way that's not a
*  platonic thought experiment, like there's zero evidence. Actually, in fact, there's actually
*  counter evidence that we have recursive self-improvement. There are a number of
*  good studies like this will never happen, theoretically. So until we have even a shred
*  of evidence that there's going to be anything that's going to be exponential or that'll behave in ways
*  that computer systems haven't, then we could have the conversation, but we're not there.
*  We're literally taking a thought experiment that is not rooted at all in the way that we
*  understand computers and using that to regulate perhaps the most beneficial technology of the last
*  30 years. Do you like the responsible scaling policy approach or the preparedness framework
*  approach? Each of Anthropic OpenAI and DeepMind now have their own kind of version of this,
*  but I'm sure you're familiar, but basically for everybody who may not be, they are defining a
*  set of things that they are interested in looking at or think could be problematic long-term,
*  defining thresholds of capability and then in the Anthropics case, committing to either solving it
*  or stopping scaling when they begin to see those. I think companies should do whatever they want,
*  whether this is for signaling or they're actually genuinely concerned they should do whatever they
*  want. I've spoken to a lot of people, by the way, that are close to these and a lot of the times
*  are like, listen, we're worried that if we don't self-police, the regulators will police for us.
*  So it's not because they actually think there's a genuine concern, not everybody. Some people think
*  there's a genuine concern. Many people that do this for much more pragmatic reasons. I am fully
*  supportive of that. To be very clear, what I am not supportive of is regulators getting arbitrary
*  restrictions that will unevenly impact startups, academics, and researchers. Anthropic, do your
*  thing. OpenAI, do your thing. Google, do your thing. But do not foist this on a broader framework
*  that's going to impact our ability to innovate. I think that's actually a moral wrong. I really do.
*  What do you think the trajectory of competition in the foundation model space is going to look like?
*  It's a very good question. I think one thing I didn't appreciate and I'm just starting to
*  appreciate is how much there's a perverse economy of scale and distillation is so effective.
*  So a positive economy of scale, like a network effect, is the leader,
*  the marginal cost to add the additional user goes to zero. So leaders get ahead and you have natural
*  monopolies. A neutral competitive landscape just fragments because a dollar in is basically a dollar
*  earned. In this, it looks like there's a perverse economy of scale, which the leader has to pay more
*  money to stay ahead. And because you're a leader, you help the followers because they can literally
*  use you to catch up to you. That's a perverse economy of scale. I think there's a very open
*  question on is this going to just end up fragmenting into a whole bunch of competitive models that are
*  basically the same size? And that seems to be the case. Originally, this is how much we're so scared
*  of our own shadow. Originally, everybody was like, it'll be opening AI and they'll be ahead of
*  everybody and nobody will catch up. Remember that? I remember it very well. You've got data
*  network effects and they're going to have all the data. So now that's clearly not the case.
*  So now you have a number of companies that are roughly at the same baseline. But what's surprising
*  is companies that are not even software companies, just like the Nvidia released recently, are building
*  models that are incredibly competitive. There's open source that's incredibly competitive.
*  Databricks released a model that was incredibly competitive. And so my sense is because there's an
*  inherent perverse economy of scale that's built into this, which is because you can use them for
*  distillation. I'm using a very loose phrase of distillation, not the technical phrase, but like
*  you can use them to build models, I suspect you're going to just have massive massive fragmentation.
*  And that's absolutely been the case, right? This is what we've seen is you'd think that it'd be
*  open AI and everybody else, maybe open AI, and dropping and everybody else. And it's not like
*  that. Yeah, I mean, you look at the LM says leaderboard, it is like that. It's basically all
*  those guys dominating the top. Certainly, there are a lot of people who have done a fine tune
*  based on like their outputs and close the gap. But this I think is pretty different.
*  Listen, if you compare this to a true network effect with a marginal cost of the leader,
*  like for adding a new user goes to zero, it looks nothing like this. This is shockingly fragmented
*  for any sort of industry that's capital intensive shockingly fragmented. Just so you know, if you
*  compare this to like the rise of social networking, or the rise of the telephone networks,
*  or the rise of the internet, or any of these is a shocking fragmented. What measurement would you
*  say that though, because the leaderboard doesn't the leaderboard basically shows like three players,
*  the sort of market share I would think is also like very dominated. That's a great point. I think
*  that's a great point. I think if you look at the market share, it's breaking what you normally see,
*  which is it breaks Pareto, which is like the top 20% gets 80% of the market and the rest.
*  It looks like software in that way, but it doesn't look different than software.
*  Yeah, I often kind of assume it's converging on cloud.
*  Yeah, exactly. I think this is a great point. I think it is converging on what we have seen
*  traditionally with software, which is first mover gets 80% and is able to track capital. But it's
*  not, it does not look like the network. Networks very specifically create monopolies. In
*  Facebook, like whatever GitHub is another one, like those look quite different than oligopolies,
*  which you tend to see come out of traditional software where there isn't an inherent network
*  effect, but there are scale effects and first mover effects. And I absolutely grant you,
*  that's what it seems to look like now. But even then, I am surprised by how fast
*  less funded competitors catch up. I do think that they're diminishing marginal returns all across
*  the board in these models. When it comes to collecting data, the existing data that you have,
*  the compute, et cetera. So I expect this to be a lot more fragmented than I think many people do.
*  And listen, if you want to do a dollar bet, I will bet you a dollar in two years that this has turned
*  out to be relatively fragmented. There's not a clear leader that has 80% of the market.
*  I think we could come up with a bet there that I would take. My general expectation is that
*  there are going to be fewer and fewer competing at the top level because part of my bet would be
*  that something like scaling laws hold. I think the most unpredictable element of all of this is
*  like research breakthrough. And that's what can really shake the snow globe is like somebody finds
*  something that doesn't scale quadratically anymore or whatever. There could be all sorts of
*  insights that could change things. But if scaling laws are... People always talk about scaling laws,
*  but you know how hard it is to deal with a logarithmic scaling law or an exponential power
*  law or however you want to characterize it? You need an order of magnitude more to get the same
*  improvement. This is really tough. And we're starting to see that play out now. And so I
*  think when people say scaling laws hold, I think that kind of undersells what that means.
*  But does this work against open source in the sense that if you expect that it is going to be
*  that hard to get those gains? The opposite for two reasons. Let's not even talk about distillation.
*  So let's imagine you have two Zenos paradox runners, right? So like they're both running,
*  but like never getting to the end. It turns out when you have scaling laws like this,
*  the front runner will continue to run slower because the marginal dollar goes down.
*  So put it this way, if open AI needs to improve by some fixed amount, it has to pay 10 times more
*  or a hundred times more or a thousand more. And so for the same investment, any challenger is going
*  to catch up by quite a bit. So that gap is always closing. Now they never catch up because these
*  are kind of Zenos paradox runners, but it's the exact opposite. Was that clear? It's like the
*  leader has to now pay more to make the same gains. And then if you add the fact that the followers
*  can learn from the leaders because they can do all sorts of tricks, like create the post-training
*  data or whatever tricks that they do, that's even another headwind. So in a normal network effect,
*  the leader gets a tax break because it's easier to connect new users because whatever,
*  you've got super linear value when you have more units or whatever it is. But this one,
*  leaders get taxed a lot more and they get taxed more because the marginal value has dropped so
*  much, but also because the people behind can catch up. And so it's the exact opposite of what you've
*  said. There's no disputing the Zenos paradox runners analysis, but the question is like,
*  how apt is that analogy to the actual situation? It seems like you could easily get into a dynamic
*  where, and this is like what Anthropic, according to their leaked pitch deck said, it seems like
*  you could easily imagine a situation where somebody gets far enough along that they are actually
*  really economically valuable, whether that's drop in knowledge worker or whatever.
*  That's a great point. Yeah.
*  And then they actually have the resources and the others don't. And then that sort of splits.
*  There's like a continental divide there where you're either rolling downhill toward AGI or
*  you're still coming uphill toward trying to get over the hump. Sure. Listen, if that happens,
*  that's great. Again, there's perverse economies of scales and diminishing margin returns everywhere
*  you look in this space. This is why it seems to me that you have one leader, then everybody catches
*  up and then they're edging forward and then everybody catches up. The distillation thing
*  is incredibly real. Having, listen, being a professional investor for almost a decade and
*  having worked with complex systems for three times longer than that, I will say this does not
*  look like a normal first mover scale effect or network effect. It looks the opposite. It looks
*  like a total slugfest to stay as really, really hard. And I think it's going to get even harder.
*  The marginal value is going down per dollar invested for leaders so quickly. And so to think
*  that somehow gives leaders an advantage, you have to assume there's some step function generality
*  thing which we've not yet seen and maybe there will be at some point in time, but we have not
*  seen that. Let's think about this. I want to make a dollar bet on this one. I think that the tail is
*  going to really impact the shape of this industry going forward. I think that it'll be different
*  than we've seen in previous kind of software industries. Yeah, I'm with that. Definitely.
*  One of my big things is like another difference in our approach is that I try to avoid analogies as
*  much as possible because I feel like I always, what am I smuggling in with my analogies I'm
*  always worried about? So I'm not trying to pattern match on any social network or anything else, but
*  I do think there's probably a couple of bets when I go back and look at the transcript on this.
*  Market concentration is one. Some of these just, I'm not sure quite how we would formalize the
*  abstraction. I think we're talking about two things when we talk about models. One thing is
*  a general reasoning fabric that goes out of distribution. I would say the answer to that is
*  no, I think that converges to Bayesian learning and so it's very useful, but I don't think the
*  language stuff about it. Then the other one, the one you're talking about to me converges on
*  simulation, which like it can learn the laws of physics in ways so we don't have to do the
*  empiricism. So it can do that, but it converges on simulation. So it'll be able to, it's like the
*  next step in simulation. These are two very different things. I don't think one day it's good
*  at learning simulation is going to generalize. Just because you're good at biology doesn't mean
*  you're good at playing chess or flying an airplane or something like that. So in neither of these
*  cases, the language one nor the biology one, do you have your reputed AGI? You've got something
*  that's good at next token prediction. You've got something that's good at learning distributions
*  and that's where we're at. Yeah, there might be a dollar on like, can those things be put together
*  and still do and do both of those in one system perhaps as well? The language one can call the
*  other one. I just don't think that changes. Yeah, I even mean that same weights like genuinely
*  integrated. Yeah, I literally think this whole problem comes down to simulation and maybe it's
*  just because my simulation background, like the only way to simulate the universe is to beat the
*  universe. Like it literally comes down to the universe is a big computer that's simulating
*  itself. It's basically string theory and that's the reason we can't even simulate like the three
*  body problem. It's just we don't have the compute resources to do that. You need so many compute
*  sources that impact whatever you're trying to impact anyways. We can continue to chip away at
*  the problem, but it'll never be cracked. I honestly hope that's right because I'm a little bit afraid
*  of what happens if it gets fully cracked. That's probably a great place to leave it today. I
*  appreciate a very collegially interesting, constructive conversation and I look forward to
*  formalizing one or more one dollar bets. All right, I'm going to think about it. I'll send you an email
*  if I have a good idea of what we're going to do. Good. I think these things are great. I would love
*  to do a couple of one dollar bets. So to be continued, but for now, Martin Casado, general
*  partner at A16Z, thank you for being part of the cognitive revolution. Thanks so much. This was great.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can
*  DM me on the social media platform of your choice.
