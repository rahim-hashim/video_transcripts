---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3882s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 4275
Video Rating: None
---

# BI 030 Jay McClelland: Mathematical Reasoning and PDP
**Brain Inspired:** [March 27, 2019](https://www.youtube.com/watch?v=4Zfwsl7uyQM)
*  Yeah, it's a huge challenge.
*  It's certainly going to take at least another 10 years to meet.
*  I was going to say, you can't do this in five years?
*  Come on.
*  Luckily, I feel like at least the pool of excited people who are willing and interested
*  in helping me make progress on this is growing.
*  People went from saying things to me like, excuse me, but does this have something to
*  do with perceptrons?
*  This is Brain Inspired.
*  Welcome everyone.
*  This is Paul Middlebrooks.
*  And if I sound a little different, it's because I'm recording this introduction on my phone
*  because I'm traveling with the family currently in Flagstaff, Arizona.
*  And I forgot to bring my good microphone.
*  So I hope it sounds okay.
*  I'm also recording this intro while my family sits and silently stares at me, waiting to
*  go do quote, fun stuff.
*  Right guys?
*  I'm still just silently staring.
*  Okay, a few things before I introduce today's show.
*  First, thanks to all my new supporters on Patreon.
*  Daniel, Joe, Tim, Peter, Gabriella, Omri, Kulin, and Lindsay.
*  Thank you guys.
*  You really don't know how rewarding it is to know that you appreciate the show enough
*  to support it.
*  If you would like to support the show, go to brandinspired.co and find the Patreon button
*  there where you can give as little as $2 per month.
*  If this support continues to grow as it is, I will be able to start paying someone to
*  edit the show and do other sundries that will allow me to focus more fully on the content
*  itself.
*  And it will free up my time a bit more to start producing some supplemental content,
*  maybe a little mini course down the road.
*  And if you're supporting the show, then you will definitely have early beta access to
*  that when it happens.
*  So again, thank you for the support.
*  One other thing, I want to welcome you new listeners visiting from Ginger Campbell's
*  podcast Brain Science.
*  I hope you find something here useful, perhaps even inspirational.
*  Brain Science, Ginger's podcast, is a long-standing excellent resource if you're looking for broader
*  topics on neuroscience and the likes.
*  Ginger has an interest in consciousness and understanding how our brains give rise to
*  consciousness.
*  So she has a lot of guests that focus on that.
*  And those are some of my favorite episodes.
*  But she also covers basically everything under the sun that has to do with neuroscience,
*  with philosophy, psychology, and so on mixed in.
*  So you should check out her show at Brainsciencepodcast.com.
*  Like I said, she interviewed me most recently about my background and deep learning in general
*  to introduce that topic to her audience.
*  And we talked about my little show here.
*  And I was delighted to contribute a bit to her show.
*  But I recommend you check out her Trove of Past episodes where you'll recognize plenty
*  of names and discover lots of other great topics that you'll want to listen to.
*  Okay, today I bring you none other than James L. McClelland, whose name is inextricably
*  linked to the concept of parallel distributed processing, or PDP.
*  PDP is basically a synonym for what has been variously called neural networks, connectionism,
*  parallel distributed processing, and now deep learning.
*  Jay has been a champion of the idea that learning done in PDP networks, that is sub-symbolic
*  distributed processing over simple units, can underlie virtually all of our cognition.
*  So we talk about the history a bit, the passing of the torch from symbolic-based AI to the
*  PDP neural network approach.
*  And you get to hear how Jay experienced that rather prickly time.
*  You'll hear him reference a famous past tense debate that he and David Rumelhart had with
*  Steve Pinker and Alan Prince and later others about whether the past tense of verbs are
*  formed using a distributed neural network-like coding or a more grammar-specific rule-based
*  type of coding.
*  So you'll hear when he's talking about that.
*  His earlier work focused on lots of cognitive science, like language and reading, as you
*  just heard, semantic cognition, decision-making, and quite a bit more actually, all under
*  the PDP approach.
*  And much of that work was done with David Rumelhart, with whom Jay published the famous
*  and still thought of as a sort of Bible for neural network PDP approaches, the book Parallel
*  Distributed Processing from 1986.
*  That was then, and this is now, and his newest project is trying to tackle mathematical reasoning
*  in machines.
*  It's worth here describing this briefly before we talk about it in the show.
*  Jay has set himself the goal of producing an AI agent that can pass an official New
*  York State geometry exam and to do so in as human a way as possible.
*  That is, to learn through exploration and feedback and reinforcement and to be able
*  to explain how the agent came to a certain answer and for the agent to ask for explanation
*  of why a certain answer was the right one.
*  So a rather ambitious project, which as you'll hear Jay is well aware of, we talk about how
*  his approach differs from the kind of learning that DeepMind has successfully implemented,
*  which largely relies on reinforcement learning, but not as much on other aspects of learning.
*  Jay talks about how he's come to think that language itself might be important for accomplishing
*  the goal of passing that geometry test.
*  So that's pretty interesting.
*  We reference and discuss at some length some of the work that I talked about with Sam Gershman
*  from a couple episodes ago.
*  Jay talked about how our current deep learning approach leaves out important human skills
*  that we somehow need to include if we want machines to really emulate humans thinking-wise.
*  Jay talks a bit about how his approach differs in that he maintains we can do just that,
*  but without hardwiring in the human-like abilities, but again figuring out how to do it from a
*  lower level neural network-like approach.
*  So I recommend listening to episode 28 with Sam if you want a bit of the background on that.
*  I also recommend, if you want to learn more about Jay's mathematical reasoning project,
*  to watch his lecture in which he lays out the project well, and I'll link to that in
*  the show notes at braininspired.co.au, slash podcast, slash 30, along with many of the
*  other things that we've talked about in this episode.
*  Daphne, if you are listening, my apologies.
*  One of the topics I wanted to discuss with Jay is the learning theory that he developed
*  many years ago in 1995 and has recently updated.
*  It's called the complementary learning systems theory, but we just didn't get to it.
*  Jay had other pressing matters to attend to and I wanted to let our discussion take its
*  own course a little bit.
*  So it's possible and hopefully I'll have Jay back soon to talk exclusively about that,
*  but I do also have some other guests lined up to talk about learning as well.
*  So hang in there, Daphne.
*  We will get there by hook or by crook.
*  All right, my family's rolling their eyes now telling me to finish up.
*  So thank you for listening and here is Jay McClelland.
*  Jay, thank you for joining me and agreeing to teach me today how to do better math.
*  Okay, well, I'm willing to give it a try.
*  So I'm actually tempted to say that you need no introduction and therefore give you no
*  introduction.
*  Do people ever actually do that because of how well known you are?
*  Sometimes they say this man needs no introduction, but usually they say a few words.
*  Okay, well, I guess I'll say a few words here.
*  I will have given you a proper introduction before we've actually begun recording here,
*  but extremely briefly, you're the director of Stanford's Center for Mind, Brain and
*  Computation and you run the Stanford Parallel Distributing Processing Lab.
*  And I will have gone through many of your accomplishments and interests from your past.
*  But today we're going to talk a little bit about the history of parallel distributed
*  processing and AI.
*  We're going to talk about the complementary learning system theory that you've developed
*  and how it relates to brains and AI and your current big focus project on implementing
*  mathematical reasoning in machines.
*  And then if we get through all that, time willing, I'll ask you some broader questions.
*  Sounds good.
*  Before we begin though, I would like to extend a personal thank you for helping found the
*  Center for the Neural Basis of Cognition, the joint effort between the University of
*  Pittsburgh and Carnegie Mellon University where I earned my PhD.
*  So thank you, sir, for helping found that institution.
*  Oh, that was definitely my pleasure.
*  That was one of the most exciting opportunities I've ever had.
*  Very good.
*  So before we dive in, let's just play a little name that year quiz here.
*  Okay.
*  Okay.
*  So I'm going to name the event and you name the year that you think it happened.
*  Are you ready?
*  Okay.
*  All right.
*  So what year was the first PC virus called brain?
*  Did it come to be?
*  What year, I guess, did it infect PCs would be the correct question.
*  Oh, gosh.
*  Being a cognitive scientist, I have no idea.
*  Maybe 1982.
*  1982.
*  Okay.
*  What year did Chernobyl, the nuclear power station, explode?
*  Also in the 80s.
*  I want to say it was 40 years ago or something because it was recently in the news.
*  So it would be 80, what, 79?
*  79.
*  We'll go with 79.
*  How about the space shuttle Challenger exploding shortly after takeoff?
*  I just watched the movie about Armstrong.
*  So I'm going to have to say 66.
*  66.
*  Okay.
*  We just have two more here.
*  One is when did Peter Gabriel's sledgehammer explode onto the scene and top the charts?
*  If you know who that is.
*  Just barely.
*  Yep.
*  Yep.
*  I didn't say it'd be easy.
*  I'm going to take a pass on that one.
*  I have no idea.
*  And finally, when was the book Parallel Distributed Processing published by David Romelhart and
*  James McClelland?
*  1986.
*  Okay.
*  You got that one right.
*  And the answer to all of these was 1986.
*  So apparently you were focusing on your work at the time, which is a good thing.
*  So let's talk a little bit of history of parallel distributed processing or I'm just going to
*  say PDP now.
*  So from roughly the 1950s into the 1980s, good old fashioned AI ruled the AI world with
*  symbol manipulating systems.
*  And their argument was that this is how intelligence happens.
*  It happens by manipulating symbols.
*  And a symbol, when I say symbol here, I'm referring to a physical pattern that can get
*  combined into structures and then those structures can be manipulated.
*  Then along comes an alternative approach, a PDP approach, which argues that representations
*  occur over a spread of activity of relatively simple sub-symbolic units.
*  So they're not symbols, there's these sub-symbolic units.
*  In other words, it looks more like the way that brains look.
*  So this approach, this latter approach has gone by various names, parallel distributed
*  processing, connectionism, neural networks.
*  And these days it's kind of all called deep learning.
*  And I'm just wondering if you have a preference between those and what your thoughts are on
*  the current term, deep learning.
*  I like deep learning, but I think neural networks is a good summary term for everything in this
*  space because deep learning is a method for training multi-layer artificial neural networks
*  and PDP models were always essentially neural-inspired or neuron-like processing units networks.
*  Connectionist models is another name that was popular back in the 80s.
*  And I think the focus there was on the idea that the knowledge wasn't stored explicitly
*  in patterns, but was in the connections.
*  And I find that notion very important.
*  But I think the word connectionist somehow doesn't otherwise communicate too much to
*  the audience.
*  So I think neural networks sort of tells people basically that one is dealing with something
*  that might have some something to do with how the brain works and exactly how much to
*  what extent and how much we should care is always part of the discussion.
*  Yeah, see, I tend to agree with you.
*  For some reason, I think that the deep learning term is somehow misleading it because it's
*  come to encompass so many different variations of the neural networks.
*  So this is something to I'm just wondering how long the term deep learning will last.
*  You know, well, it has a nice ring to it.
*  It sounds like it must be profound.
*  Right.
*  So you say you're in deep learning and everybody nods, you know, like, oh, boy, he's deep.
*  Yeah.
*  Well, OK, so there was this passing of the torch wherein the PDP approach basically emerged
*  victorious.
*  This is chronicled actually in a book by Terry Sanofsky and Terry's been on the show and
*  he wrote The Deep Learning Revolution.
*  And in that book and in other chronicles of this time period, it seems like it was kind
*  of a tumultuous passing of the torch, I suppose.
*  So was this downfall, if you will, of symbolic AI and the uprising, if you will, of PDP,
*  was it as tumultuous as it seems now when people talk about it?
*  It was tumultuous to me.
*  It's partly because I engaged with some of our colleagues at MIT that I can say that
*  it was tumultuous.
*  But I'm sure Terry told his story of his trip to MIT in his book.
*  He did.
*  And my story wasn't all that different than Terry's story.
*  So I would say this.
*  I would say that my experience of the period from, well, in my case, it was 1982 to 1989
*  was of a period where it gradually became realized that there was this new game in town.
*  People went from saying things to me like, excuse me, but does this have something to
*  do with perceptrons to, you know, writing articles where they were trying to explain
*  why this whole approach would never really fly?
*  Right.
*  But by the time we got to 1988, I think there was my view would be that there was kind of
*  this entrenched recognition that, OK, this is sort of going to be here to stay.
*  But there was also very strong ongoing resistance.
*  And it wasn't by any means it might have been one of the strongest computational paradigms
*  in town, but it wasn't the only way people thought about cognition.
*  There were many people who, if you read the literature from the developmentalists from
*  the through the 90s and even up till five, six years ago, the papers are full of, you
*  know, such statements as when does the child discover the insight that leads them to answer
*  this question correctly?
*  And I'm like, well, why do we have to think that this is some sort of explicit cognitive
*  realization?
*  Right.
*  Right.
*  My my feeling is very much that a new paradigm was put on the table and a bunch of people
*  joined in and participated, but it was only one among many sort of competing viewpoints
*  throughout the, let's say, the 90s.
*  And then there was this very big lull of interest in these things in the late 90s, early 2000s,
*  when, you know, I turned away from trying to use backpropagation.
*  I was told when I got here to Stanford in 2006 that they'd stopped teaching backprop
*  in their core machine learning class in the computer science department because it wasn't
*  useful anymore.
*  Wow.
*  So that was interesting to me.
*  But it wasn't too many years later that that changed again.
*  Yeah.
*  Well, it's back in full force now, for sure.
*  Yeah.
*  So were you guys getting invited to MIT just so people could badger you and?
*  Oh, absolutely.
*  Yeah.
*  Oh, my gosh.
*  So there was this wonderful experience where I was invited to be the featured speaker at
*  an evening seminar.
*  And the way the evening seminar was supposed to work was that somebody from the MIT community,
*  there would be a paper that would be circulated and people would be expected to take a look
*  at it.
*  And then somebody from the MIT community would sort of introduce the issues in the paper.
*  And then this person who had written the paper would then get up and give a short overview
*  of their perspective on the paper.
*  And then there would be a general discussion.
*  But what actually happened was two people decided they needed to comment on my paper
*  and each of them took a full hour.
*  So before I got a chance to speak, two hours had gone by and, you know, there needed to
*  be a bathroom break and everybody left at the break.
*  And I was sitting there listening to these guys as they were, you know, the first one
*  was Steve Pinker.
*  And he was telling me that this was very important, everybody that this was important.
*  It's the first model that really took seriously looking at the data and modeling the phenomena
*  rather than just sort of talking in very general terms and so on.
*  And really like the work for that reason.
*  And then he would say, you know, but, you know, this is wrong and this is wrong and
*  that is wrong.
*  So it's great to see this thing out there.
*  But these are the reasons why it's wrong.
*  And then the next guy got up and he was basically like, don't even bother me with this
*  till such time as you show that this network
*  can actually achieve adult competence.
*  Well, a competence based critique, which says that
*  the core of the computational idea has to be
*  a structure that captures competence without
*  error. And then the errors are these sort of performance factors that get in the way,
*  you know, sort of there's some noise somewhere.
*  But if you took the noise out, you'd be able to show it would do it perfectly.
*  Don't even talk to me until you have that.
*  I guess you haven't talked to him yet.
*  Well, he's still alive and he's still, you know, a guy who's
*  willing to practice rhetorical techniques that not everyone appreciates.
*  But but it was also a perspective that, you know, sort of represented the Chomsky and
*  kind of core idea that competence and actual behavior had very little to do with each
*  other. And, you know, nobody ever collected a data set when any human adult correctly
*  inflected the past tense of every single word that was presented to them.
*  Yeah. So it's an ideal that it would even exist.
*  You know, some model that would do that.
*  But you're kind of referring to your famous debates with Steve Pinker about the past tense
*  and how how that can happen, which we won't get into.
*  But but OK, so that's pretty interesting.
*  It was at the heart of the whole debate.
*  Right. And Jerry, so I don't know if you know the book that Pinker edited, which had,
*  you know, essentially the two speeches that those two guys presented.
*  And then this other critique by the guy who asked me if this had anything to do with
*  perceptrons. And then finally, and most importantly, the critique by Fodor and
*  Polishin of the entire connectionist enterprise.
*  It wasn't just about a specific model.
*  It was about the whole nature of the enterprise.
*  Well, so I mean, so there's a lot of competition in science as you know.
*  Right. And a lot of the rivalries I've experienced them, you know, in the past,
*  rivalries I've experienced them can be ugly, even petty.
*  They can get petty.
*  On the other hand, they can also drive progress and innovation.
*  And I'm wondering if you know how your experience with that and moving on with
*  other experiences, how that's shaped, how you view, you know, what if you could set
*  up sort of a competitive rivalry, what would that optimal what would be the optimal setup
*  for it? You know, it wouldn't be bickering, obviously.
*  But but I mean, a little competition is probably good.
*  Right. Yeah.
*  Well, so I'm going to answer this question twice.
*  So first of all, what in terms of making a practical concrete progress towards,
*  you know, sort of achievable milestones, one of the things that I've done repeatedly
*  over my career is to find instances in the literature where somebody has made
*  a claim about the nature of cognitive abilities, which I think is perhaps a useful
*  first approximation, but actually not 100 percent accurate.
*  And this is very much related to the past tense debate.
*  It has to do with looking at the world through what in that instance I would call
*  rule tinted glasses.
*  But in other instances, I would call glasses that are tinted by your theoretical
*  perspective such that you see the facts in a certain kind of way and you characterize
*  them in that way.
*  And then you specify that in order to address the facts in this domain, you have to exhibit
*  properties X, Y and Z where properties X, Y and Z don't actually hold in the real
*  phenomenon in the way that they've been stated, at least in the way these ideas get
*  passed around.
*  And so what I do is I come to these debates and I to these aspects of the literature and I
*  revisit the data and I try to bring out the ways in which they don't actually fully
*  support the stated summary claims.
*  And then I use that as leverage to illustrate the benefits of the approach that I take,
*  because it tends to capture those ways in which the phenomenon differs from the way
*  it's been described previously in the literature.
*  This is almost a philosophical approach to revisit the almost the meanings of some of
*  the terms being used and the assumptions being made, right?
*  Yeah.
*  So when somebody says that children have a eureka moment where they discover the past
*  tense rule and they kind of argue for it in terms of a statement about the data, that's
*  when I go back and I look at the data in more detail.
*  So we completely reanalyzed the data that backed up a statement about how abrupt this
*  transition was.
*  And we showed that, in fact, if you looked at it carefully, there was no abrupt transition
*  at all.
*  And this then plays into the rationale for having an approach that doesn't sort of begin
*  with the stipulation that cognitive abilities are a matter of acquiring discreet rules or
*  principles that suddenly change the whole pattern of your behavior with respect to a
*  whole domain.
*  And puts us in a place where we can understand how a real wet biological system that kind of
*  has a certain amount of intrinsic inertia to it isn't necessarily going to suddenly
*  turn on a dime.
*  It's going to require a certain amount of practice and experience to acquire new skills
*  and abilities and things like that.
*  So anyway, so that's been a part of how I would do it.
*  I would identify these places where things have been I think misstated, re-examine the
*  phenomena and lay out the facts again from another perspective and then show how models,
*  neural network kinds of models could address those phenomena.
*  That was one of the two answers.
*  I would say that the second answer relates to the deeper question about a long-term choice
*  of research focus.
*  So in my case, I decided to focus on mathematical cognition because it seemed to me that
*  mathematical cognition was a perfect domain within which to try to achieve a real flip
*  in the way we think about things.
*  So I guess fundamentally what I feel like my goal is as a scientist is to get people
*  to think differently about things that they tend to think about in ways that may just
*  be sort of stamped in by history and habit.
*  In mathematical cognition, there's a huge amount of emphasis on symbolic systems and
*  the idea that math could be reduced to a completely logical system, a system of rewrite rules,
*  something like that.
*  I realized on the one hand that neural network models could often be seen as models that
*  would capture the intuitive or implicit aspects of human cognition, but not the sort of advanced
*  scientific aspects, the kinds of things that we get PhDs to study, like mathematics or
*  computer science or physics or something like that.
*  So you could easily have said, okay, so we share this sort of basic biological architecture for,
*  let's say, visual processing with many other animals that have to navigate in the sky and
*  on land and swing from tree to tree and precisely grasp objects as they're moving through space and
*  recognize things to distinguish food from poison and do all kinds of things like that and even
*  sort of learn intuitive concepts through immersion and exposure to discourse, like discussion about
*  things or language.
*  So implicit learning of linguistic knowledge through gradual connection adjustment, okay,
*  maybe that's all fine.
*  This is all the stuff that happens before we go to school.
*  We learn our language.
*  We learn how to recognize objects.
*  This is all natural cognition.
*  We learn how to move and walk and even carry out fairly intricate motor sequences to tie our shoes
*  and feed ourselves and so on.
*  But when we get to school, we suddenly start being this sort of formal systems come in and
*  you know, so the question could neural networks help us understand both on the one hand why the
*  acquisition of those systems is sometimes hard, but also on the other hand, how it is that we
*  somehow sometimes achieve brilliant sort of insights that don't seem to be, you know, just
*  building up connections by rote, but somehow learning to have intuitions that guide us to
*  imply these interesting symbolic frameworks to new domains and to find, you know, demonstrate that
*  it's true that some principle really does hold or something.
*  So it just seemed like an opportunity to turn the whole business on its head a little bit and ask
*  whether rather than thinking about symbolic cognition as the core characteristic of the
*  human mind, could we see it as something that the human mind could learn to master as a tool that
*  would give it additional power to exploit its intuitive and implicit knowledge abilities
*  together with the capabilities of symbolic processing?
*  Maybe what we can do is actually for now just move on and talk about that project since we're
*  already kind of getting into it. But before we go there, so there's this been a recent kind of
*  backlash to deep learning and you know, a lot of people are saying that it's just not enough to
*  get us to general AI and this has to do with what you're just talking about. You know, it's not
*  really thinking like humans think. I had Sam Gershman on the show recently and he co-authored
*  a paper with colleagues and they argued that we need to build in some human-like processes
*  like intuitive physics, you know, like these things that we seem to come in the world with,
*  right, ready, like causality, compositionality. And you guys actually commented on that paper
*  and you know, you acknowledge like, okay, this is going to take a long time to address here these
*  issues that you've raised, but building it into the building these human-like processes into the
*  system is actually a limiting sort of shortcut that isn't how humans learn. And I'm wondering
*  if this is a trend that you've seen since the early days and up till through, you know, all the
*  all your work up to now where you get to this point and people say, oh, well, now we need to
*  build in some symbolic structure to it. Now we need to build in something that's supra,
*  not sub-symbolic, something above sub-symbolic, right? Is this something that you have
*  experienced and, you know, resisted all along or what?
*  Yes, I do resist that. What you said is exactly what I would say. If you build it in, it's not
*  so surprising that your model doesn't require as much experience to learn something. What I find
*  really intriguing though, I mean, I read, of course, I'm very familiar with the article
*  that you mentioned. We did write a response to it and I assign it in my class and I discuss it.
*  And the points that are made in it are important points. They do a valuable service to the field
*  by articulating some of the ways in which contemporary models, you know, don't capture
*  aspects of human reasoning. And I'm always in favor of that, right? If you point out to me
*  where the shortcomings are, I'm glad to know it. Well, I already alluded to this a little
*  bit before, but what I really don't like is when you then go on and tell me what I have to do to
*  solve the problem. And that's always somewhat motivating to me, though. It's sort of like,
*  okay. Well, this gets to the competitive process here, right?
*  That's right. So these guys did a good job of sort of setting up some of the targets that we ought
*  to try to meet in order to address the set of issues that we'll need to address before
*  we do have anything like general intelligence. And so I don't have any objection to the
*  observation about how different, you know, a DQN is from Brendan Lake in terms of its ability to
*  learn how to play Frostbite. Right. But, you know, what's the diagnosis of the reason for
*  that difference? Right. And what's the right research approach to take to address that?
*  So, you know, if you want something that's going to work tomorrow, I think doing what Brendan Lake
*  did in his dissertation, which was to explicitly build in the specific constraints that describe
*  how the use of a writing implement would constrain the production of handwritten characters
*  into an explicit generative model. That does give you a tremendous amount of inductive leverage. And
*  that, you know, part of the argument in the article was that that's what you need in order
*  to account for the fact that humans are able to learn after they've just learned how to produce
*  one alphabet properly. They know how to judge whether something is a character in another
*  alphabet or, you know, whether two characters are the same character, different characters,
*  things like that. So this is a very concrete and explicit sort of challenge that Brendan laid before
*  us. Can we produce a general purpose learning system that acquires this
*  knowledge such that it can do the generalization from only one previous
*  or a couple of previous like, examples that it's learned? Yeah. So I do agree that this kind of
*  back and forth, laying the challenges on the table is, you know, very important. It's what drives Deep
*  Mind. They take up a challenge. Yeah. If you tell them humans can do something that their agents
*  can't do, that's a research program. Right. Got it. Yeah. We ought to do that because humans do it
*  and our machines don't. Right. Right. Everybody. And if you can quantify this, you can sort of give
*  a measurement with this much experience, humans could do this much generalization.
*  And here's our model. It needs a hundred times the experience to get anywhere near that kind of
*  generalization. Okay. That's a challenge we ought to address. Yeah. You've quantified a difference
*  between humans and current state of the art machines. And that's part of what, you know,
*  really makes Deep Mind go. There's something where humans are better than what's currently
*  achievable. And so to learn what the essence of the requirement of an artificially general agent
*  would be to address it, you need to, you know, address that phenomenon. Well, so far that's been
*  games. It's been games. Yeah. But I think you can quantify it not just in terms of eventual success,
*  but rate of uptake. How quickly can you master the new game? You know, it's been a little bit
*  of an uphill battle for me to sometimes convince people that that's a worthwhile challenge to take
*  on. But I have seen a certain amount of buy-in on that. And I think we'll see more, you know,
*  because we get introduced to new things all the time. We have to pick up on new ideas. We have to
*  start using them pretty quickly. And we can't, you know, always wait for 100 billion training
*  examples and the completely balanced data set and so on to make progress.
*  Actually, it's not my intention to fuel any competitive spirits here today. But
*  let's talk about your 10-year plan here to pass a math exam.
*  Okay. So I know that you have a passion for helping human students learn math better,
*  and trigonometry specifically. You also have a passion for helping machines learn mathematical
*  reasoning. And this is your main focus now, which is to teach a machine how to mathematically reason
*  and to do it within 10 years. Now, I know from experience that when I've estimated how long an
*  experiment will take to really be as accurate as possible, I then have to multiply my own estimate
*  by at least two to be nearly accurate. And you've mentioned, you've talked to Jeff Hinton about this
*  and he doesn't think you can do it in 10 years. Do you guys have a wager on this, by the way?
*  Oh, no. Okay. I gave myself a 10-year horizon, not because I thought it was necessarily achievable,
*  but because I felt that it would take at least that long at minimum.
*  And when I first had this idea, I figured 10 years was a reasonable expectation of,
*  you know, my possible future time available to pursue the challenge. Now that about five years
*  has passed, I know for sure that it's going to be another 10 years before it was successful.
*  But that just means it's beyond the foreseeable horizon of what's actually doable based on what
*  I currently understand. So maybe that's a better way of saying what I meant by this 10-year
*  research program. I will say this. I feel like, well, I don't want to overstate this, but
*  one of the things that's fascinated me over the years is the extended latent phase of learning
*  in deep neural networks. So when you train a deep neural network, there are these long plateaus.
*  Sometimes they're less visible than others, but oftentimes they're very visible and they show up
*  especially in reinforcement learning agents. A very, very long time goes by before it seems
*  like the agent is beginning to learn anything. And then all of a sudden,
*  there's this fairly rapid transition that occurs. Now, obviously, you know, there's some state of the
*  system that it's built up over that long latent period that's sort of made it ready to make that
*  more rapid transition. And I'm sure that there are many, many aspects or facets to that. But we now
*  actually are beginning to understand exactly why this occurs in what we call deep linear neural
*  networks. Anyway, this is a bit of a digression. But since I've seen this so often in so many
*  domains of modeling cognitive development, I kind of feel like, okay, well, it's sort of expected in
*  my foray into mathematical cognition that it'll be the same way. There'll be this long latent period
*  before anything comes out the other end of the pipeline. I was going to venture to say that I
*  think you'll start to see more coming out. But I shouldn't. I don't really think that it makes
*  sense for somebody to try to predict the future. I'm not a predictor of the future. I'm somebody
*  who tries to make a long term plan for what he might try to achieve in the future.
*  Hmm. Well, you have so on your website, and I'll link to this, you lay out you have three videos
*  where you lay out this project really nicely and clearly. So maybe we can just start with
*  the motivating questions that are driving you toward this project. One of these is,
*  can networks really think? And so it makes me wonder what is thinking? And you kind of argue
*  that mathematical reasoning can be taken as thought. Yeah, I think that's fair.
*  I guess we could debate it. But it's hard to imagine that anyone would claim that Einstein
*  didn't spend a hell of a lot of time thinking while he was developing the theory of relativity.
*  Well, he was a very visual thinker as well, which pertains to some of your other material here.
*  Yeah. So but also, you know, you think about Euclid and Archimedes and anybody who's trying
*  to solve a mathematical problem or do a mathematical derivation or I mean, obviously,
*  it's also true when you're trying to debug a computer program or write a computer program or,
*  you know, devise a solution to a problem where there seem to be constraints that
*  you're having trouble figuring out a meat all at once. You know, so I think of thinking as being
*  very much a process that is extended over a period of time from the time in which a problem
*  is originally sort of envisioned as one worth solving to the time in which it's been formulated
*  more specifically as a concrete and explicit sort of item to resolve and to the time in which it's
*  been, you know, a sketch of a solution has been worked out to the time when you've actually sort of
*  fully consolidated your own understanding of the nature of that solution. And I feel like I've
*  undergone this kind of series of, you know, stages of thinking myself. And I feel like Darwin went
*  through these kinds of stages of thinking over the very extended period of years when he was
*  you know, going from recognizing that none of the existing solutions to the problem of evolution
*  made any sense to getting really excited by an idea that he knew was somehow relevant, but he
*  couldn't exactly figure out why to then kind of like seeing how that idea worked and how it would
*  result in, you know, selection of traits that were more likely to lead to survival and then,
*  you know, then going through this extended period of like doubting that that could possibly be
*  sufficient and so on. And so there's beautiful books about this that I've read some of.
*  And in my own thinking, yeah, I went from thinking, you know, could I ever build a neural
*  network model that would capture aspects of human semantic cognitive development to
*  having a closed form mathematical formulation that actually helps me see how the
*  kinds of U-shaped developmental phenomena and stage-like transitions that occur in
*  semantic cognitions could actually be understood, you know, from a closed form mathematical point
*  of view. I mean, that's, but that's something I did over a more than 20 year period. I started
*  being interested in semantic cognition early in the days I was working on complementary
*  learning systems themselves. The complementary learning systems was maybe a starter. Maybe we
*  should come back to that. But anyway, 25 years and now I feel like, okay, I've at least got an
*  understanding of what was going on in all that work and why we were able to explain all those
*  phenomena and so on. It's not something I can do on my own. It requires a group of people.
*  It requires people whose mathematical skills are stronger than mine. And it sort of motivates me
*  to think more about helping other people learn mathematical ideas because I still struggle when
*  I have to learn the new mathematical ideas that then allow me to understand my own models.
*  Well, that's what that's another one of your motivating questions is why is math so hard?
*  And can neural networks help us understand how we do learn math, right? So to maybe make it easy.
*  It's easy to understand why they would explain why it's hard because they learn so damn slowly.
*  So Sam Gershman and colleagues would agree with me about that. Okay, yeah.
*  Neural networks explains why math is hard. But they push back and say, I'm not interested in
*  what's hard. I'm interested in what's easy. And I'm like, well, okay, but you kind of get to what's
*  easy after you've been through what's hard. So then the final motivating question here is
*  how to extend neural networks to capture this math condition. So what you're saying is,
*  essentially is that what we have right now won't work. And we have to extend it in some way. Now
*  that's not just building in symbolic math concepts, right? You want to do it on a
*  sub symbolic level. But it is it's an admission that, you know, we're gonna have to develop
*  different approaches to the networks, correct? Well, admissions, admissions, a strong word here.
*  But I think I think actually, my response to that might surprise you a little bit.
*  In that paper, and in the lecture, I hope it's certainly in the paper,
*  laying out this this project laying out this approach, I, I talked about
*  the role of culture and structure in experience might play. Yeah. And as I've continued to think
*  about these things, I've begun to feel more and more that the the fundamental limitations are not
*  as much in the architectures, but more in whether our neural networks are placed in the same
*  rich experiential context that human learning occurs in. So I can say three things about this
*  specifically. One of them is, and I think this is possibly the most important.
*  We use language to share ideas with each other and to allow things that have been discovered
*  gradually through experience to be transmitted quickly through a linguistic statement.
*  And the neural networks that play Atari games, or go or chess, have no language at all. They just
*  have a bitmap and a response. Yeah, a set of response options. And it's quite amazing that
*  very advanced skills within the context of these games can be achieved by these systems. But I
*  firmly believe that one of the things that we do achieve in the course of the first
*  two or three years of life is an ability to let language guide our behavior and our thought
*  processes and let ourselves even use language to gather additional information from others.
*  And this needs to be a part of the way any system that's going to acquire productive conceptual
*  knowledge learns. I think it's going to need to have this ability to utilize language input to
*  guide its behavior and utilize linguistic input to output to explain and ask for explanation
*  on the output side. So it may be that there is some missing architectural element that will be
*  required to allow that to happen. And I don't want to claim there aren't other architectural
*  innovations that are going to turn out to be relevant and important. And every year some
*  clever new innovation occurs in deep learning, which I think is useful.
*  Well, yeah, these are like the kind of the bells and whistles that even DeepMind uses,
*  that the DeepQ network uses, reinforcement learning plus experience replay, which we would
*  talk about if we talked about the complementary learning system theory too. Maybe before we move
*  on we should just talk about what the, so you set some concrete goals for the project. And I started
*  off by saying how to teach a machine to pass a math exam. But the goal, one of the concrete goals is
*  to teach a machine to pass the New York State Regents exam in geometry specifically. So that's
*  a nice concrete goal. And not only that, but to do it like a human so that, you know, can it learn
*  and function and explain its own actions in a human like way.
*  Right. So I think that last statement, explain its own actions in a human like way, really taps into
*  what I was just talking about, right? Yeah, exactly.
*  It turns out that the exam is written in English, right? There are sentences.
*  Yeah, yeah. And there are diagrams and there are formulas and there is graph paper. I mean,
*  it's interesting in that regard. So in order to solve, to take this exam, you need to be able to
*  read graphs and draw graphs and interpret diagrams and understand text and mathematical
*  expressions and manipulate mathematical expressions and even state the basis of your reasoning in
*  explanatory statements. There are questions that are graded by human graders that require
*  these kinds of explanatory answers. So, you know, there's only a few of them because
*  that's obviously a time consuming task for a human grader for each New York State
*  region exam taker. But it's also part of the challenge and it relates to what we're talking
*  about, which is that I need to have an integrated skill set that involves being able to see how the
*  same relationship can be expressed in a sentence, in a formula, in a diagram,
*  and connect those to each other, which is what I think people do. So it needs to take language in,
*  it needs to produce language out, it needs to look at diagrams presented to it in a visual input,
*  and it needs to manipulate them and construct new ones. So in some ways it's got visual,
*  motoric, and linguistic capabilities, as well as the ability to properly process symbolic
*  expressions, you know, according to structure sensitive rules, while also relating them to
*  the problem at hand and going from the problem statement to the correct formula and vice versa.
*  So yeah, it's a huge challenge. It's certainly going to take at least another 10 years to meet.
*  I was going to say you can't do this in five years. Come on.
*  Luckily, I feel like at least the pool of excited people who are really interested in helping me
*  make progress on this is growing. And maybe this podcast that you're producing will
*  recruit one or two more excited individuals. Or scare the hell out of them to run away, you know.
*  Well, at least it's a challenge that could potentially be met.
*  Yeah. So we have maybe eight more minutes here. So it's too bad because the complementary learning
*  systems theory stuff is fun. And it's neat that it's been updated from, you know, from 1995,
*  this really influential paper. That's really kind of minor updates, actually. It's still looking
*  good going strong here. So I might, okay, I'll just take that laugh as a confirmation. So
*  I might describe a little bit of it in the introduction and link to it in the show notes.
*  And if we need to, we can have you back on and talk about it more fully as well.
*  So let's talk about just some broad things. What's one instance where luck has played a role
*  in your career or work?
*  Meeting Dave Rumelhart. Being a colleague of David Rumelhart
*  was probably the best thing that ever happened to me in my life, my scientific life.
*  And you chalk that up to luck.
*  Well, the process of which academic job somebody happens to land is definitely a matter of
*  happenstance, at least. There were particular reasons why I was the candidate chosen for that
*  job and not somebody else. But, you know, it was luck that he was there, UCSD, you know,
*  it's part of the group that decided to hire me in some level. And, you know, I think it was
*  more broadly, I think Don Norman and Dave Rumelhart provided a context where being serious
*  about the cognitive psychology while also being really open to both mathematical and
*  artificial intelligence research was, you know, like really, you know, considered a cool thing to
*  do. And I really felt it gave me the opportunity that almost any other psych department job
*  anywhere in the world wouldn't have opened up to the same extent. Just the opportunity to sort of
*  think not just about the empirical phenomena, but also the deeper computational kinds of questions
*  about how you could actually build systems that implemented them. Maybe Carnegie Mellon would have
*  been about as good and I ended up there later, so that was fine. But for me as an assistant professor,
*  the opportunity to think with Rumelhart in particular was also just truly amazing.
*  I thought that was a very fertile bit of soil that I landed in as an assistant professor.
*  He was a well-liked individual as well. So I'm reading this book by Hasek Chang called
*  Inventing Temperature and he extols the virtue in having a long-term focus, kind of a singular,
*  kind of not singular necessarily, but a long-term focus and like you're talking about with Darwin
*  going back and thinking about it over and over. And I think kind of like you've done in your career
*  here and what you're setting yourself up to do within 10 years, of course, with this math project.
*  And I'm wondering what you think is the right balance between, you know, this singular kind of
*  focus and diving deep on one thing and keep scratching and clying or moving around and
*  exploring, you know, this exploration versus exploitation within your career sort of question,
*  you know. Yeah. Well, I could talk forever about this kind of question.
*  Well, you don't have forever, so. Right.
*  Right. I guess what I would say is I do find myself to be spread quite thin. I do have a
*  sense of myself as somebody who has moved from topic to topic. I would say that typically what
*  happens in my case is that I work on a topic until I reach the point of feeling that what I
*  wanted to learn from working on it is has been learned. And so that's when I move on from
*  one thing to something else. I guess the other thing I would say is that this sort of broad goal
*  of developing a simulated neural network agent that can pass the New York State Regents exam
*  is so extended that it has to be broken down into multiple sub goals. And so the lab has been,
*  I can't at least say this, you know, after a couple of years of not producing anything,
*  we've begun to produce, you know, some papers sort of making small dents in this problem in little
*  ways. And in each one of those cases, you know, we're biting off a little chunk of something that
*  you might see as kind of like part of this huge elephant or not, but at least I see it as part
*  of a huge elephant and part of working towards that broader goal. So there's definitely a diversity
*  of, you know, like sub domains like geometry, trigonometry, early acquisition of number,
*  understanding fractions. These are all domains in which people, you know, spend their entire career.
*  But nevertheless, there's so much common structure about, you know, what kinds of mistakes
*  people made, what's hard or easy to learn, what's why, you know, etc., that I just feel like
*  finding out more about any of them is sort of contributing to my deeper goal of understanding
*  how to make progress on all of them. So from that point of view, mathematical cognition is
*  very exciting and very, very diverse as a as a as a overall field to be dabbling in while still,
*  you know, giving me a sense of underlying sort of organization to my efforts.
*  So, yeah. Well, so, lastly, Jay, you know, if you were going to start over, if you were just getting
*  into AI and neuroscience, just now, what approach would you take? Oh, wow.
*  I what advice would you give to your niece who's who's interested in getting into this stuff?
*  I would tell her to do two things. I would tell her to
*  find a collaborator or at least a mentor to bounce ideas off of, and I would tell her to
*  bounce ideas off of, and I would tell her to
*  try to find a specific problem that exemplifies a larger issue. So a specific concrete solvable
*  problem that exemplifies a larger issue. I think that this is the interactive activation model,
*  which is the project that Dave and I collaborated on really fully as, you know, really, we were
*  just in each other's offices, like maybe 15 hours out of a week at that point in our in this work
*  and where we took on something that was tractable, but also instantiated something that we both felt
*  was sort of much broader than the specific limitations of, you know, context influencing
*  the perception of a letter in a four letter, a string of four letters. And I think it was a
*  tremendous choice in that it was possible to develop this model that was explicit, understandable,
*  analyzable, presentable to the whole field, while also resonating with a much wider range of issues
*  and, you know, selecting the problem for both its tractability and its generality is,
*  of course, that's easy to say, do the right thing. Yeah, but, okay, you know, look for that and look
*  for that mentor who has a certain amount of wisdom and judgment to help guide you as you as you
*  wade into this very exciting and interesting field.
*  It is exciting. Well, I know that you have to go. So, James McClellan, thank you very much. And as
*  per your request in your lectures online in the videos about the Mathematical Cognition Project,
*  good luck. Okay, thank you.
*  Brain Inspired is a production of me. You can support the show through Patreon for a trifling
*  two or four dollars per month. Go to patreon.com slash brain inspired or go to the website,
*  braininspired.co and find the red Patreon button there. Your contribution will help keep this show
*  going without any annoying advertisements like you hear on other shows. To get in touch with me,
*  email paul at braininspired.co. The music you hear is by The New Year. Find them at the newyear.net.
*  Thank you for your support. See you next time.
*  Take me
