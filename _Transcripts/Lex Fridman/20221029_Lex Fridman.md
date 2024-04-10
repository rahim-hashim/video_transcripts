---
Date Generated: April 10, 2024
Transcription Model: whisper medium 20231117
Length: 12527s
Video Keywords: ['agi', 'ai', 'ai podcast', 'andrej karpathy', 'artificial intelligence', 'artificial intelligence podcast', 'autonomous driving', 'autopilot', 'computer science', 'deep learning', 'elon musk', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'optimus', 'radar', 'tesla']
Video Views: 2825824
Video Rating: None
---

# Andrej Karpathy: Tesla AI, Self-Driving, Optimus, Aliens, and AGI | Lex Fridman Podcast #333
**Lex Fridman:** [October 29, 2022](https://www.youtube.com/watch?v=cdiD-9MMpb0)
*  I think it's possible that physics has exploits and we should be trying to find them, arranging
*  some kind of a crazy quantum mechanical system that somehow gives you buffer overflow, somehow
*  gives you a rounding error in the floating point.
*  Synthetic intelligences are kind of like the next stage of development.
*  And I don't know where it leads to.
*  Like, at some point, I suspect the universe is some kind of a puzzle.
*  These synthetic AIs will uncover that puzzle and solve it.
*  The following is a conversation with Andrei Kapathy, previously the director of AI at
*  Tesla and before that at OpenAI and Stanford.
*  He is one of the greatest scientists, engineers and educators in the history of artificial
*  intelligence.
*  This is the Lex Friedman podcast.
*  To support it, please check out our sponsors.
*  And now, dear friends, here's Andrei Kapathy.
*  What is a neural network and why does it seem to do such a surprisingly good job of learning?
*  What is a neural network?
*  It's a mathematical abstraction of the brain.
*  I would say that's how it was originally developed.
*  At the end of the day, it's a mathematical expression and it's a fairly simple mathematical
*  expression when you get down to it.
*  It's basically a sequence of matrix multiplies, which are really dot products mathematically,
*  and some non-linearity is thrown in.
*  It's a very simple mathematical expression and it's got knobs in it.
*  Many knobs.
*  Many knobs.
*  These knobs are loosely related to basically the synapses in your brain.
*  They're trainable, they're modifiable.
*  The idea is we need to find the setting of the knobs that makes the neural net do whatever
*  you want it to do, like classify images and so on.
*  There's not too much mystery, I would say, in it.
*  You might think that basically you don't want to endow it with too much meaning with respect
*  to the brain and how it works.
*  It's really just a complicated mathematical expression with knobs and those knobs need
*  a proper setting for it to do something desirable.
*  Yeah, but poetry is just a collection of letters with spaces, but it can make us feel a certain
*  way.
*  In that same way, when you get a large number of knobs together, whether it's inside the
*  brain or inside a computer, they seem to surprise us with their power.
*  I think that's fair.
*  I'm underselling it by a lot because you definitely do get very surprising emergent behaviors
*  out of these neural nets when they're large enough and trained on complicated enough problems.
*  Like, say, for example, the next word prediction in a massive data set from the internet.
*  These neural nets take on pretty surprising magical properties.
*  Yeah, I think it's interesting how much you can get out of even very simple mathematical
*  formalism.
*  When your brain right now is talking, is it doing next word prediction?
*  Or is it doing something more interesting?
*  Well, it's definitely some kind of a generative model that's a GPT-like and prompted by you.
*  So, you're giving me a prompt and I'm kind of responding to it in a generative way.
*  And by yourself, perhaps a little bit?
*  Are you adding extra prompts from your own memory inside your head?
*  Well, it definitely feels like you're referencing some kind of a declarative structure of memory
*  and so on.
*  And then you're putting that together with your prompt and giving away some answer.
*  How much of what you just said has been said by you before?
*  Nothing, basically, right?
*  No, but if you actually look at all the words you've ever said in your life and you do a search,
*  you've probably said a lot of the same words in the same order before.
*  Yeah, could be.
*  I mean, I'm using phrases that are common, etc., but I'm remixing it into a pretty sort
*  of unique sentence at the end of the day.
*  But you're right, definitely there's a ton of remixing.
*  It's like Magnus Carlsen said, I'm rated 2900 whatever, which is pretty decent.
*  I think you're talking very, you're not giving enough credit to your own nuts here.
*  What's your best intuition about this emergent behavior?
*  I mean, it's kind of interesting because I'm simultaneously underselling them.
*  But I also feel like there's an element to which I'm over, like, it's actually kind of incredible
*  that you can get so much emergent magical behavior out of them despite them being so
*  simple mathematically.
*  So I think those are kind of like two surprising statements that are kind of juxtaposed together.
*  And I think basically what it is, is we are actually fairly good at optimizing these neural
*  nets.
*  And when you give them a hard enough problem, they are forced to learn very interesting
*  solutions in the optimization.
*  And those solutions basically have these emergent properties that are very interesting.
*  There's wisdom and knowledge in the knobs.
*  And so this representation that's in the knobs, does it make sense to you intuitively that a
*  large number of knobs can hold the representation that captures some deep wisdom about the data
*  it has looked at?
*  It's a lot of knobs.
*  It's a lot of knobs.
*  And somehow, you know, so speaking concretely, one of the neural nets that people are very
*  excited about right now are GPTs, which are basically just next word prediction networks.
*  So you consume a sequence of words from the internet and you try to predict the next word.
*  And once you train these on a large enough data set, you can basically prompt these neural
*  nets in arbitrary ways and you can ask them to solve problems.
*  And they will.
*  So you can just tell them, you can make it look like you're trying to solve some kind
*  of a mathematical problem and they will continue what they think is the solution based on what
*  they've seen on the internet.
*  And very often those solutions look very remarkably consistent, look correct potentially.
*  Do you still think about the brain side of it?
*  So as neural nets is an abstraction or mathematical abstraction of the brain,
*  you still draw wisdom from the biological neural networks or even the bigger question.
*  So you're a big fan of biology and biological computation.
*  What impressive thing is biology doing to you that computers are not yet that gap?
*  I would say I'm definitely on, I'm much more hesitant with the analogies to the brain than
*  I think you would see potentially in the field.
*  And I kind of feel like certainly the way neural networks started is everything
*  stemmed from inspiration by the brain.
*  But at the end of the day, the artifacts that you get after training, they are arrived at
*  by a very different optimization process than the optimization process that gave rise to
*  the brain.
*  And so I think I kind of think of it as a very complicated alien artifact.
*  It's something different.
*  The neural nets that we're training.
*  They are complicated alien artifact.
*  I do not make analogies to the brain because I think the optimization process that gave
*  rise to it is very different from the brain.
*  So there was no multi-agent self-play kind of setup and evolution.
*  It was an optimization that is basically what amounts to a compression objective
*  on a massive amount of data.
*  Okay.
*  So artificial neural networks are doing compression and biological neural networks
*  are not to survive and are not really doing anything.
*  They're an agent in a multi-agent self-play system that's been running for a very, very long time.
*  That said, evolution has found that it is very useful to predict and have a predictive
*  model in the brain.
*  And so I think our brain utilizes something that looks like that as a part of it, but
*  it has a lot more, you know, catches and gizmos and value functions and ancient nuclei that
*  are all trying to like make a survivor reproduce and everything else.
*  And the whole thing through embryo genesis is built from a single cell.
*  I mean, it's just the code is inside the DNA and it just builds it up like the entire
*  organism with arms and the head and legs.
*  Yes.
*  And like it does it pretty well.
*  It should not be possible.
*  So there's some learning going on.
*  There's some, there's some, there's some kind of computation going through that building
*  process.
*  I mean, I don't know where, if you were just to look at the entirety of history of life
*  on earth, where do you think is the most interesting invention?
*  Is it the origin of life itself?
*  Is it just jumping to eukaryotes?
*  Is it mammals?
*  Is it humans themselves?
*  Almost sapiens?
*  The origin of intelligence or highly complex intelligence?
*  Or is it all just a continuation of the same kind of process?
*  Certainly, I would say it's an extremely remarkable story that I'm
*  only like briefly learning about recently all the way from actually like you almost
*  have to start at the formation of earth and all of its conditions and the entire solar
*  system and how everything is arranged with Jupiter and moon and the habitable zone and
*  everything.
*  And then you have an active earth that's turning over material.
*  And then you start with abiogenesis and everything.
*  So it's all like a pretty remarkable story.
*  I'm not sure that I can pick like a single unique piece of it that I find most
*  interesting.
*  I guess for me as an artificial intelligence researcher, it's probably the last piece.
*  We have lots of animals that are not building technological society, but we do.
*  And it seems to have happened very quickly.
*  It seems to have happened very recently.
*  And something very interesting happened there that I don't fully understand.
*  I almost understand everything else.
*  I think intuitively, but I don't understand exactly that part and how quick it was.
*  Both explanations would be interesting.
*  One is that this is just a continuation of the same kind of process.
*  There's nothing special about humans.
*  That would be deeply understanding.
*  That would be very interesting that we think of ourselves as special.
*  But it was obvious.
*  It was already written in the code that you would have greater and greater intelligence
*  emerging.
*  And then the other explanation, which is something truly special happened,
*  something like a rare event, whether it's like crazy rare event like a space odyssey.
*  What would it be?
*  If you say like the invention of fire or as Richard Wrangham says, the beta males
*  deciding a clever way to kill the alpha males by collaborating.
*  So just optimizing the collaboration, the multi-agent aspect of the multi-agent.
*  And that really being constrained on resources and trying to survive the collaboration aspect
*  is what created the complex intelligence.
*  But it seems like it's a natural outgrowth of the evolution process.
*  What could possibly be a magical thing that happened, like a rare thing that would say
*  that humans are actually human level intelligence is actually a really rare thing in the universe?
*  Yeah, I'm hesitant to say that it is rare, by the way, but it definitely seems like
*  it's kind of like a punctuated equilibrium where you have lots of exploration and then
*  you have certain leaps, sparse leaps in between.
*  So of course, like origin of life would be one.
*  DNA, sex, eukaryotic life, the endosymbiosis event where the archaeon ate little bacteria,
*  just the whole thing.
*  And then of course, emergence of consciousness and so on.
*  So it seems like definitely there are sparse events where a massive amount of progress
*  was made, but yeah, it's kind of hard to pick one.
*  So you don't think humans are unique?
*  Got to ask you, how many intelligent alien civilizations do you think are out there?
*  And is their intelligence different or similar to ours?
*  Yeah, I've been preoccupied with this question quite a bit recently,
*  basically the Fermi paradox and just thinking through.
*  And the reason actually that I am very interested in the origin of life is fundamentally trying to
*  understand how common it is that there are technological societies out there in space.
*  And the more I study it, the more I think that there should be quite a lot.
*  Why haven't we heard from them?
*  Because I agree with you.
*  It feels like I just don't see why what we did here on Earth is so difficult to do.
*  Yeah, and especially when you get into the details of it.
*  I used to think origin of life was very, it was this magical rare event,
*  but then you read books like, for example, Nic Lane,
*  The Vital Question, Life Ascending, etc.
*  And he really gets in and he really makes you believe that this is not that rare.
*  Basic chemistry.
*  You have an active Earth and you have your alkaline vents and you have lots of alkaline
*  waters mixing with the ocean and you have your proton gradients and you have the little
*  porous pockets of these alkaline vents that concentrate chemistry.
*  And basically, as you step through all of these little pieces, you start to understand that
*  actually, this is not that crazy.
*  You could see this happen on other systems.
*  And he really takes you from just a geology to primitive life.
*  And he makes it feel like it's actually pretty plausible.
*  And also, like the origin of life was actually fairly fast after formation of Earth.
*  If I remember correctly, just a few hundred million years or something like that after
*  basically when it was possible, life actually arose.
*  So that makes me feel like that is not the constraint.
*  That is not the limiting variable and that life should actually be fairly common.
*  And then where the drop-offs are is very interesting to think about.
*  I currently think that there's no major drop-offs basically.
*  And so there should be quite a lot of life.
*  And basically, where that brings me to then is the only way to reconcile the fact that
*  we haven't found anyone and so on is that we just can't see them.
*  We can't observe them.
*  Just a quick brief comment.
*  Nick Lane and a lot of biologists I talked to,
*  they really seem to think that the jump from bacteria to more complex organisms is the
*  hardest jump.
*  Mm-hmm.
*  The eukaryotic life, basically.
*  Yeah.
*  Which I don't, I get it.
*  They're much more knowledgeable than me about the intricacies of biology.
*  But that seems like crazy because how many single-cell organisms are there?
*  And how much time you have?
*  Surely it's not that difficult.
*  And a billion years is not even that long of a time, really.
*  Just all these bacteria under constrained resources battling it out.
*  I'm sure they can invent more complex.
*  I don't understand.
*  It's like how to move from a Hello World program to like invent a function or something like that.
*  I don't...
*  Yeah.
*  Yeah.
*  So I'm with you.
*  I just feel like I don't see any...
*  If the origin of life, that would be my intuition, that's the hardest thing.
*  But if that's not the hardest thing because it happens so quickly,
*  then it's got to be everywhere.
*  And yeah, maybe we're just too dumb to see it.
*  Well, it's just we don't have really good mechanisms for seeing this life.
*  I mean, by what...
*  How?
*  So I'm not an expert just to preface this, but just from what I've been looking at it.
*  I want to meet an expert on alien intelligence and how to communicate.
*  I'm very suspicious of our ability to find these intelligences out there and to find these
*  earths like radio waves, for example, are terrible.
*  Their power drops off as basically one over R square.
*  So I remember reading that our current radio waves would not be...
*  The ones that we are broadcasting would not be measurable by our devices today.
*  Only like...
*  Was it like one-tenth of a light year away?
*  Basically, tiny distance because you really need a targeted transmission
*  of massive power directed somewhere for this to be picked up on long distances.
*  And so I just think that our ability to measure is not amazing.
*  I think there's probably other civilizations out there.
*  And then the big question is why don't they build one-man probes and why don't they
*  interstellar travel across the entire galaxy?
*  And my current answer is it's probably interstellar travel is like really hard.
*  You have the interstellar medium.
*  If you want to move at close to the speed of light,
*  you're going to be encountering bullets along the way because even like tiny hydrogen atoms
*  and little particles of dust are basically have massive kinetic energy at those speeds.
*  And so basically you need some kind of shielding.
*  You have all the cosmic radiation.
*  It's just like brutal out there.
*  It's really hard.
*  And so my thinking is maybe interstellar travel is just extremely hard.
*  And you have to go very slow.
*  Billions of years to build hard?
*  It feels like we're not a billion years away from doing that.
*  It just might be that you have to go very slowly potentially as an example through space.
*  Right.
*  As opposed to close to the speed of light.
*  So I'm suspicious basically of our ability to measure life and I'm suspicious of the ability
*  to just permeate all of space in the galaxy or across galaxies.
*  And that's the only way that I can currently see a way around it.
*  Yeah. It's kind of mind blowing to think that there's
*  trillions of intelligent alien civilizations out there kind of slowly traveling through space
*  to meet each other.
*  And some of them meet, some of them go to war, some of them collaborate.
*  Or they're all just independent.
*  Just like little pockets.
*  Well, statistically, if there's trillions of them, surely some of the pockets are close enough to
*  get them.
*  Some of them happen to be close.
*  Yeah.
*  And close enough to see each other.
*  And then once you see something that is definitely complex life, like if we see something,
*  we're probably going to be severe, like intensely aggressively motivated to figure out what the
*  hell that is and try to meet them.
*  What would be your first instinct to try to like at a generational level, meet them or
*  defend against them?
*  Or what would be your instinct as a president of the United States and the scientists?
*  I don't know which hat you prefer in this question.
*  Yeah, I think the question, it's really hard.
*  I will say, like, for example, for us, we have lots of primitive life forms on Earth.
*  Next to us, we have all kinds of ants and everything else, and we share space with them.
*  And we are hesitant to impact on them and we're trying to protect them by default,
*  because they are amazing, interesting, dynamical systems that took a long time to evolve.
*  And they are interesting and special.
*  And I don't know that you want to destroy that by default.
*  And so I like complex dynamical systems that took a lot of time to evolve.
*  I think I'd like to preserve it if I can afford to.
*  And I'd like to think that the same would be true about the galactic resources and that
*  they would think that we're kind of incredible, interesting story that took time.
*  It took a few billion years to unravel and you don't want to just destroy it.
*  I could see two aliens talking about Earth right now and saying,
*  I'm a big fan of complex dynamical systems.
*  So I think it was a value to preserve these and who basically are a video game.
*  Or show a TV show that they watch.
*  Yeah, I think you wouldn't need a very good reason, I think, to destroy it.
*  Why don't we destroy these ant farms and so on?
*  It's because we're not actually really in direct competition with them right now.
*  We do it accidentally and so on.
*  But there's plenty of resources.
*  And so why would you destroy something that is so interesting and precious?
*  Well, from a scientific perspective, you might probe it.
*  You might interact with it lightly.
*  You might want to learn something from it.
*  So I wonder, there could be certain physical phenomena that we think is a physical phenomena,
*  but it's actually interacting with us to poke the finger and see what happens.
*  I think it should be very interesting to other alien scientists what happened here.
*  What we're seeing today is a snapshot.
*  Basically, it's a result of a huge amount of computation over like billion years or something
*  like that.
*  It could have been initiated by aliens.
*  This could be a computer running a program.
*  Okay, if you had the power to do this, for sure, at least I would.
*  I would pick an Earth-like planet that has the conditions based on my understanding of
*  the chemistry prerequisites for life.
*  And I would seed it with life and run it.
*  Wouldn't you 100% do that and observe it and then protect?
*  That's not just a hell of a good TV show.
*  It's a good scientific experiment.
*  It's physical simulation.
*  Maybe the evolution is the most like actually running it is the most efficient way to
*  understand computation or to compute stuff.
*  Or to understand life or what life looks like and what branches it can take.
*  It does make me kind of feel weird that we're part of a science experiment, but maybe everything's
*  a science experiment.
*  Does that change anything for us?
*  If we're a science experiment?
*  I don't know.
*  Two descendants of apes talking about being inside of a science experiment.
*  I'm suspicious of this idea of like a deliberate panspermia as you described it, Surtis.
*  I don't see a divine intervention in some way in the historical record right now.
*  I do feel like the story in these books like Nick Lane's books and so on sort of makes
*  sense.
*  And it makes sense how life arose on Earth uniquely.
*  And yeah, I don't need to reach for more exotic explanations right now.
*  Sure, but NPCs inside a video game don't observe any divine intervention either.
*  We might just be all NPCs running a kind of code.
*  Maybe eventually they will.
*  Currently, NPCs are really dumb, but once they're running GPTs, maybe they will be like,
*  hey, this is really suspicious.
*  What the hell?
*  So you famously tweeted, it looks like if you bombard Earth with photons for a while,
*  you can emit a roadster.
*  So if like in Hitchhiker's Guide to the Galaxy, we would summarize the story of Earth.
*  So in that book, it's mostly harmless.
*  What do you think is all the possible stories like a paragraph long or sentence long that
*  Earth could be summarized as once it's done its computation?
*  So like all the possible full if Earth is a book, right?
*  Yeah.
*  Probably there has to be an ending.
*  There's going to be an end to Earth and it could end in all kinds of ways.
*  It can end soon, it can end later.
*  What do you think are the possible stories?
*  Well, definitely there seems to be...
*  It's pretty incredible that these self-replicating systems will
*  basically arise from the dynamics and then they perpetuate themselves and become more
*  complex and eventually become conscious and build a society.
*  And I kind of feel like in some sense, it's kind of like a deterministic wave
*  that kind of just happens on any sufficiently well-arranged system like Earth.
*  And so I kind of feel like there's a certain sense of inevitability in it.
*  And it's really beautiful.
*  And it ends somehow, right?
*  So it's a chemically diverse environment where complex dynamical systems can
*  evolve and become more and further complex.
*  But then there's a certain...
*  What is it?
*  There's certain terminating conditions.
*  Yeah, I don't know what the terminating conditions are,
*  but definitely there's a trend line of something and we're part of that story.
*  And where does it go?
*  So we're famously described often as a biological bootloader for AIs.
*  And that's because humans...
*  I mean, we're an incredible biological system and we're capable of computation and love and so on.
*  But we're extremely inefficient as well.
*  We're talking to each other through audio.
*  It's just kind of embarrassing, honestly, that we're manipulating seven symbols serially.
*  We're using vocal cords.
*  It's all happening over multiple seconds.
*  It's just kind of embarrassing when you step down to the
*  frequencies at which computers operate or are able to cooperate on.
*  And so basically, it does seem like synthetic
*  intelligences are kind of like the next stage of development.
*  And I don't know where it leads to.
*  At some point, I suspect the universe is some kind of a puzzle.
*  And these synthetic AIs will uncover that puzzle and solve it.
*  And then what happens after, right?
*  Because if you just fast forward Earth many billions of years, it's quiet.
*  And then it's like, to turmoil, you see city lights and stuff like that.
*  And then what happens at the end?
*  Is it like a poof?
*  Or is it like a calming?
*  Is it explosion?
*  Is it like Earth like a giant?
*  Because you said emit roasters.
*  Will it start emitting like a giant number of satellites?
*  It's some kind of a crazy explosion.
*  And we're living, we're like, we're stepping through an explosion.
*  And we're living day to day and it doesn't look like it.
*  But it's actually, I saw a very cool animation of Earth and life on Earth.
*  And basically, nothing happens for a long time.
*  And then the last two seconds, basically cities and everything,
*  and the lower orbit just gets cluttered.
*  And just the whole thing happens in the last two seconds.
*  And you're like, this is exploding.
*  This is a state of explosion.
*  If you play it at normal speed, it'll just look like an explosion.
*  It's a firecracker.
*  We're living in a firecracker.
*  Where it's going to start emitting all kinds of interesting things.
*  So explosion doesn't, it might actually look like a little explosion
*  with lights and fire and energy emitted, all that kind of stuff.
*  But when you look inside the details of the explosion, there's actual complexity happening
*  where there's like, yeah, human life or some kind of life.
*  We hope it's not a destructive firecracker.
*  It's kind of like a constructive firecracker.
*  All right.
*  So given that, I think hilarious discussion.
*  It is really interesting to think about what the puzzle of the universe is.
*  Did the creator of the universe give us a message?
*  Like for example, in the book Contact, Carl Sagan, there's a message for any civilization
*  in digits in the expansion of pi in base 11 eventually, which is kind of interesting thought.
*  Maybe we're supposed to be giving a message to our creator.
*  Maybe we're supposed to somehow create some kind of a quantum mechanical system that alerts them to
*  our intelligent presence here.
*  Because if you think about it from their perspective, it's just say like quantum field
*  theory, massive like cellular ton of a ton like thing.
*  And like, how do you even notice that we exist?
*  You might not even be able to pick us up in that simulation.
*  And so how do you prove that you exist, that you're intelligent and that you're part of the universe?
*  So this is like a touring test for intelligence from Earth.
*  Like the creator is, I mean, maybe this is like trying to complete the next word in a
*  sentence.
*  This is a complicated way of that.
*  Like Earth is just is basically sending a message back.
*  Yeah, the puzzle is basically like alerting the creator that we exist.
*  Or maybe the puzzle is just to just break out of the system and just stick it to the creator in
*  some way.
*  Basically, like if you're playing a video game, you can somehow find an exploit and find a way
*  to execute on the host machine in arbitrary code.
*  There's some, for example, I believe someone got a game of Mario to play Pong just by exploiting
*  it and then creating a basically writing code and being able to execute arbitrary code in the
*  game.
*  And so maybe we should be maybe that's the puzzle is that we should be find a way to exploit it.
*  So I think like some of these synthetic AI's will eventually find the universe to be some kind of a
*  puzzle and then solve it in some way.
*  And that's kind of like the end game somehow.
*  Do you often think about it as a simulation?
*  So as the universe being a kind of computation that might have bugs and exploits?
*  Yes.
*  Yeah, I think so.
*  I think physics is essentially.
*  I think it's possible that physics has exploits and we should be trying to find them,
*  arranging some kind of a crazy quantum mechanical system that somehow gives you buffer overflow,
*  somehow gives you a rounding error in the floating point.
*  Yeah, that's right.
*  And like more and more sophisticated exploits.
*  Those are jokes, but that could be actually very close.
*  Yeah, we'll find some way to extract infinite energy.
*  For example, when you train reinforcement learning agents in physical simulations and you ask them
*  to say run quickly on the flat ground, they'll end up doing all kinds of like weird things
*  in part of that optimization, right?
*  They'll get on their back leg and they'll slide across the floor.
*  And it's because the optimization, the enforcement learning optimization on that agent has figured
*  out a way to extract infinite energy from the friction forces and basically their poor
*  implementation and they found a way to generate infinite energy and just slide across the surface.
*  And it's not what you expected.
*  It's just sort of like a perverse solution.
*  And so maybe we can find something like that.
*  Maybe we can be that little dog in this physical simulation.
*  The cracks or escapes the intended consequences of the physics that the universe came up with.
*  Yeah.
*  We'll figure out some kind of shortcut to some weirdness.
*  Yeah.
*  And then, man, but see the problem with that weirdness is the first person to discover
*  the weirdness like sliding in the back legs.
*  That's all we're going to do.
*  Yeah.
*  It's very quickly because everybody does that thing.
*  So the paperclip maximizer is a ridiculous idea, but that very well could be what then we'll just
*  all switch that because it's so fun.
*  Well, no person will discover it, I think, by the way.
*  I think it's going to have to be some kind of a super intelligent AGI of a third generation.
*  Like we're building the first generation AGI.
*  Third generation.
*  Yeah.
*  So the bootloader for an AI, that AI will be a bootloader for another AI.
*  Better AI.
*  Yeah.
*  And then there's no way for us to introspect like what that might even...
*  I think it's very likely that these things, for example, like say you have these AGI's,
*  it's very likely, for example, they will be completely inert.
*  I like these kinds of sci-fi books sometimes where these things are just completely inert.
*  They don't interact with anything.
*  And I find that kind of beautiful because they've probably figured out the meta game
*  of the universe in some way, potentially.
*  They're doing something completely beyond our imagination.
*  And they don't interact with simple chemical life forms.
*  Why would you do that?
*  So I find those kinds of ideas compelling.
*  What's their source of fun?
*  What are they doing?
*  Well, probably puzzle solving in the universe.
*  But inert, so can you define what it means inert so they escape the interaction?
*  Peer inert to us as in they will behave in some very strange way to us because they're
*  beyond...
*  They're playing the meta game.
*  And the meta game is probably say arranging quantum mechanical systems in some very weird
*  ways to extract infinite energy, solve the digital expansion of pi to whatever amount.
*  They will build their own like little fusion reactors or something crazy.
*  They're doing something beyond comprehension and not understandable to us.
*  And actually brilliant under the hood.
*  What if quantum mechanics itself is the system and we're just thinking it's physics,
*  but we're really parasites on...
*  Not parasite, we're not really hurting physics.
*  We're just living on this organism.
*  This organism and we're like trying to understand it, but really it is an organism.
*  And with a deep, deep intelligence, maybe physics itself is...
*  The organism that's doing the super interesting thing and we're just like one little thing,
*  yeah, and sitting on top of it trying to get energy from it.
*  We're just kind of like these particles in the wave that I feel like is mostly deterministic
*  and takes a universe from some kind of a big bang to some kind of a super intelligent replicator,
*  some kind of a stable point in the universe given these laws of physics.
*  You don't think as Einstein said, God doesn't play dice?
*  You think it's mostly deterministic?
*  There's no randomness in the thing?
*  I think it's deterministic.
*  Oh, there's tons of...
*  Well, I want to be careful with randomness.
*  Pseudo-random?
*  Yeah, I don't like random.
*  I think maybe the laws of physics are deterministic.
*  I think they're deterministic.
*  You just got really uncomfortable with this question.
*  Do you have anxiety about whether the universe is random or not?
*  Is this a sort of...
*  There's no randomness.
*  You said you like Good Will Hunter.
*  I don't know.
*  Randomness.
*  You said you like Good Will Hunting.
*  It's not your fault, Andre.
*  It's not your fault, man.
*  You don't like randomness?
*  Yeah, I think it's unsettling.
*  I think it's a deterministic system.
*  I think that things that look random, like say the collapse of the wave function, etc.,
*  I think they're actually deterministic, just entanglement and so on,
*  and some kind of a multiverse theory, something, something.
*  Okay, so why does it feel like we have a free will?
*  Like if I raise this hand, I chose to do this now.
*  That doesn't feel like a deterministic thing.
*  It feels like I'm making a choice.
*  It feels like it.
*  Okay, so it's all feelings.
*  It's just feelings.
*  Yeah.
*  So when an RL agent is making a choice, is that...
*  It's not really making a choice.
*  The choice is already there.
*  Yeah, you're interpreting the choice and you're creating a narrative for having made it.
*  And now we're talking about the narrative.
*  It's very meta.
*  Looking back, what is the most beautiful or surprising idea in deep learning or AI
*  in general that you've come across?
*  You've seen this field explode and grow in interesting ways.
*  Just what cool ideas?
*  Like what made you sit back and go, hmm, small, big or small?
*  Well, the one that I've been thinking about recently,
*  the most probably is the transformer architecture.
*  So basically, neural networks have...
*  A lot of architectures that were trendy have come and gone for different sensory modalities,
*  like for vision, audio, text.
*  You would process them with different looking neural nets.
*  And recently we've seen this convergence towards one architecture, the transformer.
*  And you can feed it video or you can feed it images or speech or text,
*  and it just gobbles it up.
*  And it's kind of like a bit of a general purpose computer
*  that is also trainable and very efficient to run on our hardware.
*  And so this paper came out in 2016, I want to say.
*  Attention is all you need.
*  You criticized the paper title in retrospect that it didn't foresee
*  the bigness of the impact that it was going to have.
*  Yeah, I'm not sure if the authors were aware of the impact that that paper would go on to have.
*  Probably they weren't.
*  But I think they were aware of some of the motivations and design decisions
*  behind the transformer, and they chose not to, I think, expand on it in that way in the paper.
*  And so I think they had an idea that there was more than just the surface of just like,
*  oh, we're just doing translation and here's a better architecture.
*  You're not just doing translation.
*  This is like a really cool, differentiable, optimizable, efficient computer that you've proposed.
*  And maybe they didn't have all of that foresight, but I think it's really interesting.
*  Isn't it funny, sorry to interrupt, that that title is memeable,
*  that they went for such a profound idea.
*  I don't think anyone used that kind of title before, right?
*  Attention is all you need.
*  Yeah, it's like a meme or something.
*  Yeah.
*  Isn't that funny?
*  Maybe if it was a more serious title, it wouldn't have the impact.
*  Honestly, there is an element of me that honestly agrees with you and prefers it this way.
*  Yes.
*  If it was too grand, it would over-promise and then under-deliver potentially.
*  So you want to just meme your way to greatness.
*  That should be a t-shirt.
*  You tweeted, the Transformer is a magnificent neural network architecture
*  because it is a general purpose differentiable computer.
*  It is simultaneously expressive in the forward pass,
*  optimizable via back propagation, gradient descent, and efficient high parallelism compute graph.
*  Can you discuss some of those details?
*  Expressive, optimizable, efficient for memory or in general, whatever comes to your heart?
*  You want to have a general purpose computer that you can train on arbitrary problems.
*  Like say the task of next work prediction or detecting if there's a cat in an image
*  or something like that.
*  You want to train this computer so you want to set its weights.
*  I think there's a number of design criteria that overlap in the Transformer simultaneously
*  that made it very successful.
*  I think the authors were deliberately trying to make this really powerful architecture.
*  Basically, it's very powerful in the forward pass because it's able to express
*  very general computation as something that looks like message passing.
*  You have nodes and they all store vectors.
*  These nodes get to basically look at each other and it's each other's vectors.
*  They get to communicate and basically nodes get to broadcast,
*  hey, I'm looking for certain things.
*  Then other nodes get to broadcast, hey, these are the things I have.
*  Those are the keys and the values.
*  So it's not just attention.
*  Yeah, exactly.
*  Transformer is much more than just the attention component.
*  It's got many pieces architectural that went into it.
*  The residual connections, the way it's arranged, there's a multi-layer perceptron
*  and there the way it's stacked and so on.
*  But basically, there's a message passing scheme where nodes get to look at each other,
*  decide what's interesting and then update each other.
*  When you get to the details of it, I think it's a very expressive function.
*  So it can express lots of different types of algorithms in forward pass.
*  Not only that, but the way it's designed with the residual connections,
*  layer normalizations, the softmax attention and everything, it's also optimizable.
*  This is a really big deal.
*  Because there's lots of computers that are powerful that you can't optimize,
*  or they're not easy to optimize using the techniques that we have,
*  which is back-proplication and gradient descent.
*  These are first-order methods, very simple optimizers, really.
*  You also need it to be optimizable.
*  Then lastly, you want it to run efficiently in our hardware.
*  Our hardware is a massive throughput machine like GPUs.
*  They prefer lots of parallelism.
*  So you don't want to do lots of sequential operations.
*  You want to do a lot of operations serially.
*  And the transformer is designed with that in mind as well.
*  And so it's designed for our hardware and it's designed to both be very expressive
*  in the forward pass, but also very optimizable in the backward pass.
*  And you said that the residual connections support a kind of ability to learn short
*  algorithms fast and first, and then gradually extend them longer during training.
*  What's the idea of learning short algorithms?
*  Right.
*  So basically, a transformer is a series of blocks.
*  And these blocks have attention and a little multilayer perceptual.
*  And so you go off into a block and you come back to this residual pathway.
*  And then you go off and you come back.
*  And then you have a number of layers arranged sequentially.
*  And so the way to look at it, I think, is because of the residual pathway
*  in the backward pass, the gradients sort of flow along it uninterrupted
*  because addition distributes the gradient equally to all of its branches.
*  So the gradient from the supervision at the top just floats directly to the first layer.
*  And all the residual connections are arranged so that in the beginning during initialization,
*  they contribute nothing to the residual pathway.
*  So what it kind of looks like is imagine the transformer is kind of like a Python
*  function, like a DEV.
*  And you get to do various kinds of lines of code.
*  Say you have a hundred layers deep transformer.
*  Typically, they would be much shorter, say 20.
*  So you have 20 lines of code and you can do something in them.
*  And so think of during the optimization, basically, what it looks like is first,
*  you optimize the first line of code and then the second line of code can kick in.
*  And the third line of code can kick in.
*  And I kind of feel like because of the residual pathway and the dynamics of the optimization,
*  you can sort of learn a very short algorithm that gets the approximate answer.
*  But then the other layers can sort of kick in and start to create a contribution.
*  And at the end of it, you're optimizing over an algorithm that is 20 lines of code.
*  Except these lines of code are very complex because it's an entire block of a transformer.
*  You can do a lot in there.
*  What's really interesting is that this transformer architecture actually
*  has been remarkably resilient.
*  Basically, the transformer that came out in 2016 is the transformer you would use today,
*  except you reshuffle some of the layer norms.
*  The layer normalizations have been reshuffled to a pre-norm formulation.
*  And so it's been remarkably stable, but there's a lot of bells and whistles
*  that people have attached on it and tried to improve it.
*  I do think that basically it's a big step in simultaneously optimizing for lots of
*  properties of a desirable neural network architecture.
*  And I think people have been trying to change it, but it's proven remarkably resilient.
*  But I do think that there should be even better architectures potentially.
*  But you admire the resilience here.
*  There's something profound about this architecture that's at least resilient.
*  Maybe everything can be turned into a problem that transformers can solve.
*  Currently, it definitely looks like the transformer is taking over AI,
*  and you can feed basically arbitrary problems into it.
*  And it's a general, differentiable computer, and it's extremely powerful.
*  And this convergence in AI has been really interesting to watch for me personally.
*  What else do you think could be discovered here about transformers?
*  What's the surprising thing?
*  Or is it a stable...
*  I want a stable place.
*  Is there something interesting we might discover about transformers?
*  Like aha moments maybe has to do with memory,
*  maybe knowledge representation, that kind of stuff?
*  Definitely the zeitgeist today is just pushing...
*  Basically, right now the zeitgeist is do not touch the transformer, touch everything else.
*  So people are scaling up the data sets, making them much, much bigger.
*  They're working on the evaluation, making the evaluation much, much bigger.
*  And they're basically keeping the architecture unchanged.
*  And that's the last five years of progress in AI, kind of.
*  What do you think about one flavor of it, which is language models?
*  Have you been surprised?
*  Has your sort of imagination been captivated by...
*  You mentioned DPT and all the bigger and bigger and bigger language models.
*  And what are the limits?
*  Of those models, do you think?
*  So just the task of natural language.
*  Basically, the way GPT is trained, right, is you just download a massive amount of
*  text data from the internet and you try to predict the next word in the sequence, roughly speaking.
*  You're predicting little word chunks, but roughly speaking, that's it.
*  And what's been really interesting to watch is...
*  Basically, it's a language model.
*  Language models have actually existed for a very long time.
*  There's papers on language modeling from 2003, even earlier.
*  Can you explain in that case what a language model is?
*  Yeah. So language model, just basically the rough idea is just predicting the next word
*  in a sequence, roughly speaking.
*  So there's a paper from, for example, Benjio and the team from 2003, where for the first time,
*  they were using a neural network to take, say, like three or five words and predict the next word.
*  And they're doing this on much smaller data sets.
*  And the neural net is not a transformer.
*  It's a multilayer perceptron.
*  But it's the first time that a neural network has been applied in that setting.
*  But even before neural networks, there were language models, except they were using n-gram models.
*  So n-gram models are just count-based models.
*  So if you start to take two words and predict the third one, you just count up how many times
*  you've seen any two-word combinations and what came next.
*  And what you predict as coming next is just what you've seen the most of in the training set.
*  And so language modeling has been around for a long time.
*  Neural networks have done language modeling for a long time.
*  So really what's new or interesting or exciting is just realizing that when you scale it up
*  with a powerful enough neural net, a transformer, you have all these emergent properties where
*  basically what happens is if you have a large enough data set of text,
*  you are in the task of predicting the next word.
*  You are multitasking a huge amount of different kinds of problems.
*  You are multitasking understanding of chemistry, physics, human nature.
*  Lots of things are sort of clustered in that objective.
*  It's a very simple objective, but actually you have to understand a lot about the world
*  to make that prediction.
*  You just said the U-word understanding.
*  In terms of chemistry and physics and so on, what do you feel like it's doing?
*  Is it searching for the right context?
*  What is the actual process happening here?
*  Yeah. So basically it gets a thousand words and it's trying to predict the thousandth and first.
*  And in order to do that very, very well over the entire data set available on the internet,
*  you actually have to basically kind of understand the context of what's going on in there.
*  It's a sufficiently hard problem that if you have a powerful enough computer,
*  like a transformer, you end up with interesting solutions.
*  You can ask it to do all kinds of things and it shows a lot of emergent properties,
*  like in-context learning.
*  That was the big deal with GPT and the original paper when they published it,
*  is that you can just sort of prompt it in various ways and ask it to do various things.
*  And it will just kind of complete the sentence.
*  But in the process of just completing the sentence,
*  it's actually solving all kinds of really interesting problems that we care about.
*  Do you think it's doing something like understanding?
*  Like when we use the word understanding for us humans.
*  I think it's doing some understanding in its weights.
*  It understands, I think, a lot about the world and it has to in order to predict the next word
*  in a sequence.
*  So it's trained on the data from the internet.
*  What do you think about this approach in terms of data sets, of using data from the internet?
*  Do you think the internet has enough structured data to teach AI about human civilization?
*  Yes, I think the internet has a huge amount of data.
*  I'm not sure if it's a complete enough set.
*  I don't know that text is enough for having a sufficiently powerful AGI as an outcome.
*  Of course, there is audio and video and images and all that kind of stuff.
*  Yeah, so text by itself, I'm a little bit suspicious about.
*  There's a ton of things we don't put in text in writing,
*  just because they're obvious to us about how the world works and the physics of it,
*  and that things fall.
*  We don't put that stuff in text because why would you?
*  We share that understanding.
*  And so text is a communication medium between humans.
*  It's not an all-encompassing medium of knowledge about the world.
*  But as you pointed out, we do have video and we have images and we have audio.
*  And so I think that definitely helps a lot.
*  But we haven't trained models sufficiently across all those modalities yet.
*  So I think that's what a lot of people are interested in.
*  But I wonder what that shared understanding of what we might call common sense
*  has to be learned, inferred in order to complete the sentence correctly.
*  So maybe the fact that it's implied on the internet,
*  the model is going to have to learn that, not by reading about it,
*  by inferring it in the representation.
*  So like common sense, just like we, I don't think we learn common sense.
*  Like nobody says, tells us explicitly.
*  We just figure it all out by interacting with the world.
*  Right.
*  And so here's a model reading about the way people interact with the world.
*  It might have to infer that.
*  I wonder.
*  Yeah.
*  You briefly worked on a project called World of Bits,
*  training an RL system to take actions on the internet
*  versus just consuming the internet like we talked about.
*  Do you think there's a future for that kind of system,
*  interacting with the internet to help the learning?
*  Yes, I think that's probably the final frontier for a lot of these models.
*  So as you mentioned, when I was at OpenAI, I was working on this project, World of Bits.
*  And basically it was the idea of giving neural networks access to a keyboard and a mouse.
*  And the idea is that...
*  What could possibly go wrong?
*  So basically you perceive the input of the screen pixels and basically the state of the
*  computer is sort of visualized for human consumption in images of the web browser
*  and stuff like that.
*  And then you give the neural network the ability to press keyboards and use the mouse.
*  And we're trying to get it to, for example, complete bookings and interact with user interfaces.
*  And...
*  What did you learn from that experience?
*  Like what was some fun stuff?
*  This is a super cool idea.
*  I mean, the step between observer to actor is a super fascinating step.
*  Yeah. Well, it's the universal interface in the digital realm, I would say.
*  And there's a universal interface in the physical realm, which in my mind is a humanoid form factor
*  kind of thing.
*  We can later talk about optimists and so on.
*  But I feel like there's a similar philosophy in some way, where the human world,
*  the physical world is designed for the human form.
*  And the digital world is designed for the human form of seeing the screen and using
*  keyboard and mouse.
*  And so it's the universal interface that can basically command the digital infrastructure
*  we've built up for ourselves.
*  And so it feels like a very powerful interface to command and to build on top of.
*  Now, to your question as to what I learned from that, it's interesting because the world
*  of bits was basically too early, I think, at OpenAI at the time.
*  This is around 2015 or so.
*  And the Zeitgeist at that time was very different in AI from the Zeitgeist today.
*  At the time, everyone was super excited about reinforcement learning from scratch.
*  This is the time of the Atari paper, where neural networks were playing Atari games and
*  beating humans in some cases, AlphaGo and so on.
*  So everyone's very excited about training neural networks from scratch using reinforcement
*  learning directly.
*  It turns out that reinforcement learning is an extremely inefficient way of training neural
*  networks because you're taking all these actions and all these observations and you get some
*  sparse rewards once in a while.
*  So you do all this stuff based on all these inputs.
*  And once in a while, you're told you did a good thing, you did a bad thing.
*  And it's just an extremely hard problem.
*  You can't learn from that.
*  You can burn a forest and you can sort of brute force through it.
*  And we saw that, I think, with Go and Dota and so on.
*  And it does work.
*  But it's extremely inefficient and not how you want to approach problems, practically
*  speaking.
*  And so that's the approach that at the time we also took to World of Bits.
*  We would have an agent initialize randomly.
*  So with keyboard mash and mouse mash and try to make a booking.
*  And it's just like revealed the insanity of that approach very quickly, where you have
*  to stumble by the correct booking in order to get a reward of you did it correctly.
*  And you're never going to stumble by it by chance at random.
*  So even with a simple web interface, there's too many options.
*  There's just too many options.
*  And it's too sparse of a reward signal.
*  And you're starting from scratch at the time.
*  And so you don't know how to read.
*  You don't understand pictures, images, buttons.
*  You don't understand what it means to make a booking.
*  But now what's happened is it is time to revisit that.
*  And OpenAI is interested in this.
*  Companies like Adept are interested in this and so on.
*  And the idea is coming back because the interface is very powerful.
*  But now you're not training an agent from scratch.
*  You are taking the GPT as initialization.
*  So GPT is pre-trained on all of text.
*  And it understands what's a booking.
*  It understands what's a submit.
*  It understands quite a bit more.
*  And so it already has those representations.
*  They are very powerful.
*  And that makes all the training significantly more efficient.
*  And makes the problem tractable.
*  Should the interaction be with like the way humans see it with the buttons and the language?
*  Or should be with the HTML, JavaScript and the CSS?
*  What do you think is the better?
*  So today all of this interaction is mostly on the level of HTML, CSS and so on.
*  That's done because of computational constraints.
*  But I think ultimately everything is designed for human visual consumption.
*  And so at the end of the day, there's all the additional information as in
*  the layout of the web page and what's next to you.
*  And what's a red background and all this kind of stuff and what it looks like visually.
*  So I think that's the final frontier as we are taking in pixels and we're giving out
*  keyboard mouse commands.
*  But I think it's impractical still today.
*  Do you worry about bots on the internet?
*  Given these ideas, given how exciting they are, do you worry about bots on Twitter being
*  not the stupid bots that we see now with the crypto bots, but the bots that might be out
*  there actually that we don't see that they're interacting in interesting ways?
*  So this kind of system feels like it should be able to pass the,
*  I'm not a robot click button, whatever.
*  Which do you actually understand how that test works?
*  I don't quite like there's a checkbox or whatever that you click.
*  It's presumably tracking like mouse movement and the timing and so on.
*  Exactly this kind of system we're talking about should be able to pass that.
*  So what do you feel about bots that are language models plus have some interactability and
*  are able to tweet and reply and so on?
*  Do you worry about that world?
*  Yeah, I think it's always been a bit of an arms race between sort of the attack and the
*  defense. So the attack will get stronger, but the defense will get stronger as well,
*  our ability to detect that.
*  How do you defend? How do you detect? How do you know that your Carpati account on Twitter
*  is human? How would you approach that? Like if people were claimed, you know,
*  how would you defend yourself in the court of law that I'm a human?
*  This account is here.
*  At some point, I think it might be, I think the society will evolve a little bit. Like
*  we might start signing, digitally signing some of our correspondence or things that we create.
*  Right now, it's not necessary, but maybe in the future it might be.
*  I do think that we are going towards a world where we share the digital space with AIs.
*  Synthetic beings.
*  Yeah. And they will get much better and they will share our digital realm and they'll
*  eventually share our physical realm as well. It's much harder, but that's kind of like the
*  world we're going towards and most of them will be benign and awful and some of them will be
*  malicious and it's going to be an arms race trying to detect them.
*  So, I mean, the worst isn't the AIs. The worst is the AIs pretending to be human.
*  So I don't know if it's always malicious. There's obviously a lot of malicious applications, but
*  yeah, it could also be, you know, if I was an AI, I would try very hard to pretend to be human
*  because we're in a human world. I wouldn't get any respect as an AI. I want to get some love and
*  respect on Twitter.
*  I don't think the problem is intractable. People are thinking about the proof of personhood
*  and we might start digitally signing our stuff and we might all end up having like,
*  yeah, basically some solution for proof of personhood. It doesn't seem to me intractable.
*  It's just something that we haven't had to do until now, but I think once the need like
*  really starts to emerge, which is soon, I think people will think about it much more.
*  So, but that too will be a race because obviously you can probably spoof or fake
*  the proof of personhood. So you have to try to figure out how to...
*  Probably.
*  I mean, it's weird that we have like social security numbers and like passports and stuff.
*  It seems like it's harder to fake stuff in the physical space. But in the digital space,
*  it just feels like it's going to be very tricky, very tricky to out.
*  Because it seems to be pretty low cost to fake stuff. What are you going to put an AI in jail
*  for like trying to use a fake personhood proof? I mean, okay, fine. You'll put a lot of AIs in
*  jail, but there'll be more AIs, like exponentially more. The cost of creating a bot is very low.
*  So, unless there's some kind of way to track accurately, like you're not allowed to create
*  any program without showing, tying yourself to that program. Like any program that runs on the
*  internet, you'll be able to trace every single human program that was involved with that program.
*  Right. Yeah. Maybe you have to start declaring when, you know, we have to start drawing those
*  boundaries and keeping track of, okay, what are digital entities versus human entities? And what
*  is the ownership of human entities and digital entities? And something like that. I don't know,
*  but I think I'm optimistic that this is possible. And in some sense, we're currently in like the
*  worst time of it because all these bots suddenly have become very capable. But we don't have the
*  fences yet built up as a society. But I think that doesn't seem to me intractable. It's just
*  something that we have to deal with. It seems weird that the Twitter bot, like really crappy
*  Twitter bots are so numerous. So, I presume that the engineers at Twitter are very good. So,
*  it seems like what I would infer from that is it seems like a hard problem. They're probably
*  catching, all right, if I were to sort of steel man the case, it's a hard problem and there's a
*  huge cost to false positive to removing a post by somebody that's not a bot. That creates a very bad
*  user experience. So, they're very cautious about removing. So, maybe it's, and maybe the bots are
*  really good at learning what gets removed and not such that they can stay ahead of the removal
*  process very quickly. My impression of it, honestly, is there's a lot of loaning for it.
*  I mean, just that's what I... It's not subtle. That's my impression of it. It's not subtle.
*  But you have to... Yeah, that's my impression as well. But it feels like maybe you're seeing
*  the tip of the iceberg. Maybe the number of bots isn't like the trillions and you have to like...
*  Just it's a constant assault of bots. I don't know. You have to steel man the case because the bots
*  I'm seeing are pretty obvious. I could write a few lines of code that catch these bots.
*  I mean, definitely there's a lot of loaning fruit, but I will say I agree that if you are a
*  sophisticated actor, you could probably create a pretty good bot right now using tools like GPTs
*  because it's a language model. You can generate faces that look quite good now. And you can do
*  this at scale. And so I think it's quite plausible and it's going to be hard to defend.
*  There was a Google engineer that claimed that the Lambda was sentient. Do you think there's any
*  inkling of truth to what he felt? And more importantly, to me at least, do you think
*  language models will achieve sentience or the illusion of sentience soonish?
*  Yeah. To me, it's a little bit of a canary in a coal mine kind of moment,
*  honestly, a little bit. So this engineer spoke to a chatbot at Google and became convinced that
*  this bot is sentient. He asked us some existential philosophical questions.
*  And he gave reasonable answers and looked real and so on. So to me, he wasn't sufficiently trying
*  to stress the system, I think, and exposing the truth of it as it is today. But I think this will
*  be increasingly harder over time. So yeah, I think more and more people will basically become...
*  Yeah, I think there will be more people like that over time as this gets better.
*  Like form an emotional connection to an AI chatbot.
*  Perfectly plausible in my mind. I think these AIs are actually quite good at human connection,
*  human emotion. A ton of text on the internet is about humans and connection and love and so on.
*  So I think they have a very good understanding in some sense of how people speak to each other
*  about this. And they're very capable of creating a lot of that kind of text. There's a lot of
*  sci-fi from 50s and 60s that imagined AIs in a very different way. They are calculating cold
*  Vulcan-like machines. That's not what we're getting today. We're getting pretty emotional
*  AIs that actually are very competent and capable of generating plausible sounding
*  text with respect to all of these topics. See, I'm really hopeful about AI systems that
*  are like companions that help you grow, develop as a human being, help you maximize long-term
*  happiness. But I'm also very worried about AI systems that figure out from the internet
*  that humans get attracted to drama. So these would just be like shit-talking AIs.
*  They just constantly, did you hear? They'll do gossip. They'll try to plant seeds of suspicion
*  to other humans that you love and trust and just kind of mess with people. Because that's
*  going to get a lot of attention. So drama, maximize drama on the path to maximizing engagement. And
*  us humans will feed into that machine and get, it'll be a giant drama shitstorm. So I'm worried
*  about that. So it's the objective function really defines the way that human civilization progresses
*  with AIs in it. I think right now, at least today, they are not sort of, it's not correct to really
*  think of them as goal-seeking agents that want to do something. They have no long-term memory or
*  anything. It's literally, a good approximation of it is you get a thousand words and you're trying
*  to predict a thousand at first, and then you continue feeding it in. And you are free to
*  prompt it in whatever way you want. So in text, so you say, okay, you are a psychologist and you are
*  very good and you love humans. And here's a conversation between you and another human,
*  human colon something, you something. And then it just continues the pattern. And suddenly you're
*  having a conversation with a fake psychologist who's like trying to help you. And so it's still
*  in the realm of a tool is people can prompt it in arbitrary ways and it can create really incredible
*  text, but it doesn't have long-term goals over long periods of time. It doesn't try to,
*  so it doesn't look that way right now. Yeah. But you can do short-term goals that have
*  long-term effects. So if my prompting short-term goal is to get Andrei Kapas to respond to me on
*  Twitter, when I, I think AI might, that's the goal, but it might figure out that talking shit to you,
*  it'll be the best in a highly sophisticated, interesting way. And then you build up a
*  relationship when you respond once and then it like over time, it gets to not be sophisticated
*  and just like just talk shit. And okay, maybe you won't get to Andrei, but it might get to
*  another celebrity. It might get into other big accounts and then it'll just, so with just that
*  simple goal, get them to respond. Maximize the probability of actual response. Yeah. I mean,
*  you could prompt a powerful model like this with their, its opinion about how to do any possible
*  thing you're interested in. So they will just, they're kind of on track to become these oracles.
*  I could sort of think of it that way. They are oracles. Currently it's just text, but they will
*  have calculators. They will have access to Google search. They will have all kinds of gadgets and
*  gizmos. They will be able to operate the internet and find different information. And
*  yeah, in some sense, that's kind of like currently what it looks like in terms of the development.
*  Do you think it'll be an improvement eventually over what Google is for access to human knowledge?
*  Like it'll be a more effective search engine to access human knowledge?
*  I think there's definite scope in building a better search engine today. And I think Google,
*  they have all the tools, all the people, they have everything they need, they have all the
*  puzzle pieces, they have people training transformers at scale. They have all the data.
*  It's just not obvious if they are capable as an organization to innovate on their search engine
*  right now. And if they don't, someone else will. There's absolute scope for building a significantly
*  better search engine built on these tools. It's so interesting. A large company where the search,
*  there's already an infrastructure, it works as brings out a lot of money. So where structurally
*  inside a company is their motivation to pivot to say, we're going to build a new search engine.
*  Yeah, that's hard. So it's usually going to come from a startup, right?
*  That would be, yeah. Or some other more competent organization. So currently, for example,
*  maybe Bing has another shot at it. Here we go, Microsoft Edge, as we're talking offline.
*  It's really interesting because search engines used to be about, okay, here's some query,
*  here's web pages that look like the stuff that you have. But you could just directly go to answer
*  and then have supporting evidence. And these models, basically, they've read all the texts
*  and they've read all the web pages. And so sometimes when you see yourself going over to
*  search results and sort of getting a sense of the average answer to whatever you're interested in,
*  that just directly comes out. You don't have to do that work. So they're kind of like,
*  uh, yeah, I think they have a way to this of distilling all that knowledge into
*  like some level of insight, basically. Do you think of prompting as a kind of teaching and learning
*  like this whole process, like another layer, you know, because maybe that's what humans are.
*  We already have that background model and then you're, the world is prompting you.
*  Yeah, exactly. I think the way we are programming these computers now, like GPTs,
*  is converging to how you program humans. I mean, how do I program humans via prompt? I go to people
*  and I prompt them to do things. I prompt them from information. And so natural language prompt is how
*  we program humans and we're starting to program computers directly in that interface. It's like
*  pretty remarkable, honestly. So you've spoken a lot about the idea of software 2.0. All good ideas
*  become like cliches so quickly. Like the terms, it's kind of hilarious. Um, it's like, I think
*  Eminem once said that like, if he gets annoyed by a song he's written very quickly, that means
*  it's going to be a big hit because it's too catchy. But, uh, can you describe this idea and how
*  you're thinking about it has evolved over the months and years since, since you coined it?
*  Yeah. Yes. I had a blog post on software 2.0, I think several years ago now. Um, and the reason
*  I wrote that post is because I kept, I kind of saw something remarkable happening in like software
*  development and how a lot of code was being transitioned to be written not in sort of like
*  C++ and so on, but it's written in the weights of a neural net. Basically just saying that neural
*  nets are taking over software, the realm of software and, um, taking more and more tasks.
*  And at the time, I think not many people understood this deeply enough that this is a big deal. It's
*  a big transition. Neural networks were seen as one of multiple classification algorithms you might
*  use for your data set problem on Kaggle. Like this is not that, this is a change in how we program
*  computers. And I saw neural nets as, uh, this is going to take over. Uh, the way we program
*  computers is going to change. It's not going to be people writing a software in C++ or something
*  like that and directly programming the software. It's going to be accumulating training sets and
*  data sets and crafting these objectives by which you train these neural nets. And at some point,
*  there's going to be a compilation process from the data sets and the objective and the architecture
*  specification into the binary, which is really just, uh, the neural net, uh, you know, weights
*  and the forward pass of the neural net. And then you can deploy that binary. And so I was talking
*  about that sort of transition and, uh, that's what the post is about. And I saw this sort of
*  play out in a lot of fields, uh, you know, autopilot being one of them, but also just a simple
*  image classification. People thought originally, you know, in the eighties and so on that they
*  would write the algorithm for detecting a dog in an image. And they had all these ideas about how
*  the brain does it. And first we detect corners and then we detect lines and then we stitched them up.
*  And they were like really going at it. They were like thinking about how they're going to write
*  the algorithm. And this is not the way you build it. Um, and there was a smooth transition where,
*  okay, uh, first we thought we were going to build everything. Then we were building the features,
*  so like hog features and things like that, uh, that detect these little statistical patterns
*  from image patches. And then there was a little bit of, uh, learning on top of it,
*  like a support vector machine or binary classifier, uh, for cat versus dog and images on top of the
*  features. So we wrote the features, but we trained the last layer, sort of the classifier. And then
*  people are like, actually, let's not even design the features because we can't honestly, we're not
*  very good at it. So let's also learn the features. And then you end up with basically a convolutional
*  neural net where you're learning most of it. You're just specifying the architecture and
*  the architecture has tons of filling the blanks, which is all the knobs, and you let the optimization
*  write most of it. And so this transition is happening across the industry everywhere. And,
*  suddenly we end up with a ton of code that is written in neural net weights. And I was just
*  pointing out that the analogy is actually pretty strong and we have a lot of developer environments
*  for software 1.0. Like we have IDEs, um, how you work with code, how you debug code, how do you run
*  code, uh, how do you maintain code? We have GitHub. So I was trying to make those analogies in the
*  new realm. Like what is the GitHub of software 2.0? Turns out it's something that looks like
*  hugging face right now. Uh, you know, and so I think some people took it seriously and built
*  cool companies and, uh, many people originally attacked the post. It actually was not well
*  received when I wrote it. And I think maybe it has something to do with the title, but the post was
*  not well received. And I think more people sort of have been coming around to it over time.
*  Yeah. So you were the director of AI at Tesla where I think this idea was really implemented at scale,
*  which is how you have engineering teams doing software 2.0. So can you sort of linger on that
*  idea of, I think we're in the really early stages of everything you just said, which is like
*  GitHub IDEs, like how, how do we build engineering teams that, that work in software 2.0 systems and
*  the data collection and the data annotation, which is all part of that software 2.0. Like
*  what do you think is the task of programming a software 2.0? Is it debugging in the space of
*  hyperparameters or is it also debugging in the space of data? Yeah. The way by which you program
*  the computer and influence its algorithm is not by writing the commands yourself. You're changing
*  mostly the dataset. You're changing the loss functions of like what the neural net is trying
*  to do, how it's trying to predict things, but basically the datasets and the architecture. So
*  the neural net. And so in the case of the autopilot, a lot of the datasets had to do with, for example,
*  detection of objects and lane line markings and traffic lights and so on. So you accumulate massive
*  datasets of here's an example, here's the desired label, and then here's roughly how the architect,
*  here's roughly what the algorithm should look like. And that's a convolutional neural net.
*  So the specification of the architecture is like a hint as to what the algorithm should roughly
*  look like. And then the fill in the blanks process of optimization is the training process.
*  And then you take your neural net that was trained, it gives all the right answers on
*  your dataset and you deploy it. So there's in that case, perhaps at all,
*  machine learning cases, there's a lot of tasks. So is coming up, formulating a task
*  like a, for a multi-headed neural network is formulating a task part of the programming?
*  Yeah. How you break down a problem into a set of tasks.
*  Yeah. I'm on a high level. I would say if you look at the software running in the autopilot,
*  I gave a number of talks on this topic. I would say originally a lot of it was written in software
*  1.0. There's imagine lots of C++, right? And then gradually there was a tiny neural net that was,
*  for example, predicting given a single image, is there like a traffic light or not, or is there a
*  landline marking or not? And this neural net didn't have too much to do in the scope of the software.
*  It was making tiny predictions on individual little image. And then the rest of the system
*  stitched it up. So, okay, we're actually, we don't have just a single camera, we have eight cameras.
*  We actually have eight cameras over time. And so what do you do with these predictions? How do you
*  put them together? How do you do the fusion of all that information and how do you act on it?
*  All of that was written by humans in C++. And then we decided, okay, we don't actually want
*  to do all of that fusion in C++ code because we're actually not good enough to write that
*  algorithm. We want the neural nets to write the algorithm and we want to port all of that software
*  into the 2.0 stack. And so then we actually had neural nets that now take all the eight camera
*  images simultaneously and make predictions for all of that. And actually they don't make predictions
*  in the space of images. They now make predictions directly in 3D. And actually they don't in three
*  dimensions around the car. And now actually we don't manually fuse the predictions in 3D over time.
*  We don't trust ourselves to write that tracker. So actually we give the neural net the information
*  over time. So it takes these videos now and makes those predictions. And so you're sort of
*  just like putting more and more power into the neural net, more and more processing. And at the
*  end of it, the eventual goal is to have most of the software potentially be in the 2.0 land
*  because it works significantly better. Humans are just not very good at writing software basically.
*  So the prediction is happening in this 4D land with three-dimensional world over time. How do you
*  do annotation in that world? What have you as a data annotation, whether it's self-supervised
*  or manual by humans is a big part of the software 2.0 world. Right. I would say by far in the
*  industry, if you're talking about the industry and what is the technology of what we have available,
*  everything is supervised learning. So you need data sets of input, desired output, and you need
*  lots of it. And there are three properties of it that you need. You need it to be very large.
*  You need it to be accurate, no mistakes, and you need it to be diverse. You don't want to
*  just have a lot of correct examples of one thing. You need to really cover the space of
*  possibility as much as you can. And the more you can cover the space of possible inputs,
*  the better the algorithm will work at the end. Now, once you have really good data sets that you're
*  collecting, curating, and cleaning, you can train your neural net on top of that.
*  A lot of the work goes into cleaning those data sets. Now, as you pointed out, it could be... The
*  question is, how do you achieve a ton of... If you want to basically predict in 3D, you need data in
*  3D to back that up. So in this video, we have eight videos coming from all the cameras of the system.
*  And this is what they saw. And this is the truth of what actually was around. There was this car,
*  there was this car, this car. These are the lane line markings. This is the geometry of the road.
*  There was traffic light in this three-dimensional position. You need the ground truth. And so the
*  big question that the team was solving, of course, is how do you arrive at that ground truth?
*  Because once you have a million of it, and it's large, clean, and diverse, then training your
*  neural net on it works extremely well, and you can ship that into the car. And so there's many
*  mechanisms by which we collected that training data. You can always go for human annotation.
*  You can go for simulation as a source of ground truth. You can also go for what we call the
*  offline tracker that we've spoken about at the AI day and so on, which is basically an automatic
*  reconstruction process for taking those videos and recovering the three-dimensional
*  reality of what was around that car. So basically think of doing a three-dimensional reconstruction
*  as an offline thing, and then understanding that, okay, there's 10 seconds of video. This is what
*  we saw. And therefore, here's all the lane lines, cars, and so on. And then once you have that
*  annotation, you can train your neural nets to imitate it. And how difficult is the three
*  reconstruction? It's difficult, but it can be done. So there's overlap between the cameras,
*  and you do the reconstruction, and there's perhaps if there's any inaccuracy, so that's
*  caught in the annotation step. Yes. The nice thing about the annotation is that it is fully offline.
*  You have infinite time. You have a chunk of one minute, and you're trying to just offline in a
*  supercomputer somewhere, figure out where were the positions of all the cars, all the people,
*  and you have your full one-minute video from all the angles. And you can run all the neural nets
*  you want, and they can be very efficient, massive neural nets. There can be neural nets that can't
*  even run in the car later at test time. So they can be even more powerful neural nets than what
*  you can eventually deploy. So you can do anything you want, three-dimensional reconstruction,
*  neural nets, anything you want just to recover that truth, and then you supervise that truth.
*  What have you learned? You said no mistakes about humans doing annotation, because I assume humans
*  are, there's like a range of things they're good at in terms of clicking stuff on screen. Isn't that,
*  how interesting is that to you of a problem of designing an annotator where humans are accurate,
*  enjoy it? Like what are the even the metrics are efficient or productive, all that kind of stuff?
*  Yeah. So I grew the annotation team at Tesla from basically zero to a thousand while I was there.
*  That was really interesting. You know, my background is a PhD student researcher. So growing
*  that kind of an organization was pretty crazy. But yeah, I think it's extremely interesting and
*  part of the design process very much behind the autopilot as to where you use humans. Humans are
*  very good at certain kinds of annotations. They're very good, for example, at two-dimensional
*  annotations of images. They're not good at annotating cars over time in three-dimensional space,
*  very, very hard. And so that's why we were very careful to design the tasks that are easy to do
*  for humans versus things that should be left to the offline tracker. Like maybe the computer
*  will do all the triangulation and three-degree construction, but the human will say exactly
*  these pixels of the image are car, exactly these pixels are human. And so co-designing the data
*  annotation pipeline was very much bread and butter was what I was doing daily. Do you think there's
*  still a lot of open problems in that space? Just in general, annotation where the stuff the machines
*  are good at, machines do and the humans do what they're good at. And there's maybe some
*  iterative process. Right. I think to a very large extent, we went through a number of iterations
*  and we learned a ton about how to create these datasets. I'm not seeing big open problems.
*  Originally when I joined, I was really not sure how this would turn out. But by the time I left,
*  I was much more secure and actually we sort of understand the philosophy of how to create these
*  datasets. And I was pretty comfortable with where that was at the time. So what are strengths and
*  limitations of cameras for the driving task in your understanding when you formulate the driving
*  task as a vision task with eight cameras? You've seen that the entire, most of the history of the
*  computer vision field when it has to do with neural networks, just if you step back, what are the
*  strengths and limitations of pixels, of using pixels to drive? Yeah. Pixels I think are a beautiful
*  sensory, beautiful sensor I would say. The thing is like cameras are very, very cheap and they
*  provide a ton of information, ton of bits. So it's an extremely cheap sensor for a ton of bits.
*  And each one of these bits is a constraint on the state of the world. And so you get lots of megapixel
*  images, very cheap. And it just gives you all these constraints for understanding what's actually out
*  there in the world. So vision is probably the highest bandwidth sensor. It's a very high bandwidth
*  sensor. And I love that pixels is a constraint on the world. It's this highly complex,
*  high bandwidth constraint on the state of the world. And it's not just that, but again,
*  this real importance of it's the sensor that humans use. Therefore, everything is designed
*  for that sensor. The text, the writing, the flashing signs, everything is designed for vision.
*  And so you just find it everywhere. And so that's why that is the interface you want to be in,
*  talking again about these universal interfaces. And that's where we actually want to measure the
*  world as well and then develop software for that sensor. But there's other constraints on the state
*  of the world that humans use to understand the world. I mean, vision ultimately is the main one,
*  but we're like referencing our understanding of human behavior in some common sense.
*  Physics, that could be inferred from vision from a perception perspective, but it feels like we're
*  using some kind of reasoning to predict the world, not just the pixels. I mean, you have a powerful
*  prior service for how the world evolves over time, et cetera. So it's not just about the likelihood
*  term coming up from the data itself telling you about what you are observing, but also the prior
*  term of where are the likely things to see and how do they likely move and so on. And the question
*  is how complex is the range of possibilities that might happen in the driving task?
*  Is that to you still an open problem of how difficult is driving, philosophically speaking?
*  All the time you worked on driving, do you understand how hard driving is?
*  Yeah, driving is really hard because it has to do with the predictions of all these other agents
*  and the theory of mind and what they're going to do and are they looking at you? Where are they
*  looking? Where are they thinking? There's a lot that goes there at the full tail of the expansion
*  of the knives that we have to be comfortable with. Eventually, the final problems are of that form.
*  I don't think those are the problems that are very common. I think eventually they're important,
*  but it's really in the tail end. In the tail end, the rare edge cases.
*  From the vision perspective, what are the toughest parts of the vision problem of driving?
*  Well, basically, the sensor is extremely powerful, but you still need to process that information.
*  And so going from brightnesses of these pixel values to, hey, here are the three-dimensional
*  world is extremely hard. And that's what the neural networks are fundamentally doing.
*  And so the difficulty really is in just doing an extremely good job of engineering the entire
*  pipeline, the entire data engine, having the capacity to train these neural nets,
*  having the ability to evaluate the system and iterate on it. So I would say just doing this
*  in production at scale is like the hard part. It's an execution problem. So the data engine,
*  but also the deployment of the system such that it has low latency performance. So it has to do
*  all these steps. Yeah, for the neural net specifically, just making sure everything
*  fits into the chip on the car. And you have a finite budget of flops that you can perform
*  and memory bandwidth and other constraints. And you have to make sure it flies and you can squeeze
*  in as much computer as you can into the tiny. What have you learned from that process? Because
*  maybe that's one of the bigger new things coming from a research background, where there's a system
*  that has to run under heavily constrained resources, has to run really fast. What kind
*  of insights have you learned from that? Yeah, I'm not sure if there's too many insights. You're
*  trying to create a neural net that will fit in what you have available and you're always trying
*  to optimize it. And we talked a lot about it on the AI day and basically the triple backflips
*  that the team is doing to make sure it all fits and utilizes the engine. So I think it's extremely
*  good engineering. And then there's all kinds of little insights peppered in on how to do it
*  properly. Let's actually zoom out because I don't think we talked about the data engine, the entirety
*  of the layouts of this idea that I think is just beautiful with humans in the loop.
*  Can you describe the data engine? Yeah, the data engine is what I call the almost biological feeling
*  like process by which you perfect the training sets for these neural networks. So because most
*  of the programming now is in the level of these data sets and make sure they're large, diverse,
*  and clean, basically you have a data set that you think is good. You train your neural net,
*  you deploy it, and then you observe how well it's performing. And you're trying to always increase
*  the quality of your data set. So you're trying to catch scenarios that are basically rare.
*  And it is in these scenarios that neural nets will typically struggle in because they weren't told
*  what to do in those rare cases in the data set. But now you can close the loop because if you can
*  now collect all those at scale, you can then feed them back into the reconstruction process I
*  described and reconstruct the truth in those cases and add it to the data set. And so the whole
*  thing ends up being like a staircase of improvement of perfecting your training set. And you have to
*  go through deployments so that you can mine the parts that are not yet represented well in the
*  data set. So your data set is basically imperfect. It needs to be diverse. It has pockets that are
*  missing and you need to pad out the pockets. You can sort of think of it that way in the data.
*  What role do humans play in this? So what's this biological system like a human body is made up
*  of cells? What role, like how do you optimize the human system? The multiple engineers collaborating,
*  figuring out what to focus on, what to contribute, which task to optimize in this neural network?
*  Who is in charge of figuring out which task needs more data? Can you speak to the hyperparameters,
*  the human system? It really just comes down to extremely good execution from an engineering
*  team who knows what they're doing. They understand intuitively the philosophical
*  insights underlying the data engine and the process by which the system improves
*  and how to again, delegate the strategy of the data collection and how that works.
*  And then just making sure it's all extremely well executed. And that's where most of the work is,
*  is not even the philosophizing or the research or the ideas of it. It's just extremely good execution.
*  It's so hard when you're dealing with data at that scale. So your role in the data engine
*  executing well on it is difficult and extremely important. Is there a priority of like,
*  a vision board of saying like, we really need to get better at stoplights?
*  Yeah. Like the prioritization of tasks. Is that essentially, and that comes from the data?
*  That comes to a very large extent to what we are trying to achieve in the product for a map.
*  The release we're trying to get out in the feedback from the QA team where the system
*  is struggling or not, the things we're trying to improve.
*  And the QA team gives some signal, some information in aggregate about the performance of the system
*  in various conditions. That's right. And then of course, all of us drive it and we can also see it.
*  It's really nice to work with a system that you can also experience yourself and you know,
*  it drives you home. Is there some insight you can draw from your individual experience that
*  you just can't quite get from an aggregate statistical analysis of data? Yeah.
*  It's so weird, right? Yes. It's not scientific in a sense because you're just one anecdotal sample.
*  Yeah. I think there's a ton of, it's a source of truth. It's your interaction with the system
*  and you can see it, you can play with it, you can perturb it, you can get a sense of it,
*  you have an intuition for it. I think numbers just like have a way of,
*  numbers and plots and graphs are much harder. It hides a lot of-
*  If you train a language model, it's a really powerful way is by you interacting with it.
*  Yeah. 100%.
*  Try to build up an intuition. Yeah. I think like Ilan also,
*  he always wanted to drive the system himself. He drives a lot and I want to say almost daily.
*  So he also sees this as a source of truth, you driving the system and it performing.
*  And yeah. So what do you think? Tough questions here. So Tesla last year removed radar from
*  the sensor suite and now just announced that it's going to remove ultrasonic sensors
*  relying solely on vision, so camera only. Does that make the perception problem harder or easier?
*  I would almost reframe the question in some way. So the thing is basically,
*  you would think that additional sensors- By the way, can I just interrupt?
*  Go ahead. I wonder if a language
*  model will ever do that if you prompt it. Let me reframe your question. That would be epic.
*  That's the wrong prompt. Sorry. It's like a little bit of a wrong question because
*  basically you would think that these sensors are an asset to you, but if you fully consider
*  the entire product in its entirety, these sensors are actually potentially liability
*  because these sensors aren't free. They don't just appear on your car. You need
*  have an entire supply chain. You have people procuring it. There can be problems with them.
*  They may need replacement. They are part of the manufacturing process. They can hold back the line
*  in production. You need to source them. You need to maintain them. You have to have teams that
*  write the firmware, all of it. And then you also have to incorporate and fuse them into the system
*  in some way. And so it actually like bloats a lot of it. And I think Elon is really good at
*  simplify, simplify. Best part is no part. And he always tries to throw away things that are not
*  essential because he understands the entropy in organizations and in the approach. And I think
*  in this case, the cost is high and you're not potentially seeing it if you're just a computer
*  vision engineer. And I'm just trying to improve my network and is it more useful or less useful? How
*  useful is it? And the thing is, once you consider the full cost of a sensor, it actually is
*  potentially a liability. And you need to be really sure that it's giving you extremely
*  useful information. In this case, we looked at using it or not using it and the delta was not
*  massive. And so it's not useful. Is it also bloat in the data engine? Like having more sensors?
*  Is it a distraction? And these sensors, they can change over time, for example. You can have one
*  type of say radar. You can have other type of radar. They change over time. Now you suddenly
*  need to worry about it. Now suddenly you have a column in your SQLite telling you, oh, what
*  sensor type was it? And they all have different distributions. And then they contribute noise and
*  entropy into everything. And they bloat stuff. And also organizationally, it's been really
*  fascinating to me that it can be very distracting. If you only want to get to work as vision,
*  all the resources are on it and you're building out a data engine and you're actually making
*  forward progress because that is the sensor with the most bandwidth, the most constraints in the
*  world. And you're investing fully into that and you can make that extremely good. If you're
*  only a finite amount of sort of spend of focus across different facets of the system.
*  And this kind of reminds me of Rich Sutton's The Bitter Lesson. It just seems like simplifying the
*  system in the long run. Now, of course, you don't know what the long run is. It seems to be always
*  the right solution. Yeah. Yes. In that case, it was for RL, but it seems to apply generally across
*  all systems that do computation. So what do you think about the LiDAR as a crutch debate?
*  The battle between point clouds and pixels. Yeah. I think this debate is always slightly
*  confusing to me because it seems like the actual debate should be about like,
*  do you have the fleet or not? That's like the really important thing about whether you can achieve
*  really good functioning of an AI system at that scale. So data collection systems. Yeah. Do you
*  have a fleet or not is significantly more important whether you have LiDAR or not. It's just another
*  sensor. And yeah, I think similar to the radar discussion, basically, I don't think it basically
*  doesn't offer extra information. It's extremely costly. It has all kinds of problems. You have to
*  worry about it. You have to calibrate it, et cetera. It creates bloat and entropy. You have to be really
*  sure that you need this sensor. In this case, I basically don't think you need it. And I think,
*  honestly, I will make a stronger statement. I think the others, some of the other companies who
*  are using it are probably going to drop it. Yeah. So you have to consider the sensor in the full,
*  in considering, can you build a big fleet that collects a lot of data? And can you integrate
*  that sensor with it, that data and that sensor into a data engine that's able to quickly find
*  different parts of the data that then continuously improves whatever the model that you're using?
*  Yeah. Another way to look at it is like vision is necessary in the sense that
*  the drive, the world is designed for human visual consumption. So you need vision.
*  It's necessary. And then also it is sufficient because it has all the information that you need
*  for driving and humans obviously has vision to drive. So it's both necessary and sufficient.
*  So you want to focus resources and you have to be really sure if you're going to bring in other
*  sensors, you could add sensors to infinity. At some point you need to draw the line. And I think,
*  in this case, you have to really consider the full cost of any one sensor that you're adopting. And
*  do you really need it? And I think the answer in this case is no.
*  So what do you think about the idea that the other companies are forming high resolution maps
*  and constraining heavily the geographic regions in which they operate? Is that approach not,
*  in your view, not going to scale over time to the entirety of the United States?
*  I think, as you mentioned, they pre-map all the environments and they need to refresh the map.
*  And they have a perfect centimeter level accuracy map of everywhere they're going to drive. It's
*  crazy. When we're talking about autonomy actually changing the world, we're talking about the
*  deployment on a global scale of autonomous systems for transportation. And if you need to maintain
*  a centimeter accurate map for Earth or for many cities and keep them updated, it's a huge dependency
*  that you're taking on. Huge dependency. It's a massive, massive dependency. And now you need to
*  ask yourself, do you really need it? And humans don't need it. So it's very useful to have a
*  low level map of the connectivity of your road. You know that there's a fork coming up. When you
*  drive an environment, you have that high level understanding. It's like a small Google map.
*  And Tesla uses Google map, similar kind of resolution information in the system. But it
*  will not pre-map environments to send me a level of accuracy. It's a crutch. It's a distraction.
*  It costs entropy and it diffuses the team. It dilutes the team. And you're not focusing
*  on what's actually necessary, which is the computer vision problem.
*  What did you learn about machine learning, about engineering, about life, about yourself as one
*  human being from working with Elon Musk? I think the most I've learned is about how to sort of
*  run organizations efficiently and how to create efficient organizations and how to fight entropy
*  in an organization. So human engineering in the fight against entropy. Yeah. I think Elon is a
*  very efficient warrior in the fight against entropy in organizations. What does entropy
*  in an organization look like exactly? It's process. It's process. And inefficiencies in
*  the form of meetings and that kind of stuff. Yeah. Meetings. He hates meetings. He keeps telling
*  people to skip meetings if they're not useful. He basically runs the world's biggest startups,
*  I would say. Tesla, SpaceX are the world's biggest startups. Tesla actually has multiple startups.
*  I think it's better to look at it that way. And so I think he's extremely good at that.
*  And yeah, he has a very good intuition for streamlining processes, making everything efficient.
*  Best part is no part, simplifying, focusing, and just kind of removing barriers, moving very
*  quickly, making big moves. All of this is very startupy, sort of seeming things, but at scale.
*  So strong drive to simplify. From your perspective, I mean, that also probably applies to just
*  designing systems and machine learning and otherwise, like simplify, simplify.
*  Yes. What do you think is the secret to maintaining the startup culture in a company that grows?
*  Can you introspect that? I do think you need someone in a powerful position with a big hammer
*  like Elon, who's like the cheerleader for that idea and ruthlessly pursues it. If no one has
*  a big enough hammer, everything turns into committees, democracy within the company,
*  process, talking to stakeholders, decision making, just everything just crumbles.
*  If you have a big person who is also really smart and has a big hammer, things move quickly.
*  So you said your favorite scene in Interstellar is the intense docking scene with the AI and
*  Cooper talking, saying, Cooper, what are you doing docking? It's not possible. No, it's necessary.
*  Such a good line. By the way, just so many questions there. Why an AI in that scene,
*  presumably is supposed to be able to compute a lot more than the human. It's saying it's not
*  optimal. Why the human? I mean, that's a movie, but shouldn't the AI know much better than the human?
*  Anyway, what do you think is the value of setting seemingly impossible goals?
*  Our initial intuition, which seems like something that you have taken on that Elon espouses,
*  where the initial intuition of the community might say this is very difficult, and then you take it
*  on anyway with a crazy deadline. You just, from a human engineering perspective, have you seen the
*  value of that? I wouldn't say that setting impossible goals exactly is a good idea,
*  but I think setting very ambitious goals is a good idea. I think there's what I call sublinear
*  scaling of difficulty, which means that 10x problems are not 10x hard. Usually 10x harder
*  problem is like two or three x harder to execute on. Because if you want to improve the system by
*  10%, it costs some amount of work. And if you want to 10x improve the system, it doesn't cost
*  100x amount of work. And it's because you fundamentally change the approach. And if you
*  start with that constraint, then some approaches are obviously dumb and not going to work. And it
*  forces you to reevaluate. And I think it's a very interesting way of approaching problem solving.
*  It requires a weird kind of thinking. Going back to your PhD days, how do you think which ideas
*  in the machine learning community are solvable? It requires, what is that? I mean, there's a
*  cliche of first principles thinking, but it requires to basically ignore what the community
*  is saying. Because doesn't a community in science usually draw lines of what is and isn't possible?
*  And it's very hard to break out of that without going crazy.
*  Yeah. I think a good example here is the deep learning revolution in some sense,
*  because you could be in computer vision at that time during the deep learning revolution of 2012
*  and so on. You could be improving a computer vision stack by 10%. Or we can just be saying,
*  actually, all of this is useless. And how do I do 10x better computer vision? Well,
*  it's not probably by tuning a hog feature detector. I need a different approach. I need something that
*  is scalable. Going back to Richard Sutton's understanding the philosophy of the bitter lesson,
*  and then being like, actually, I need much more scalable system like a neural network
*  that in principle works. And then having some deep believers that can actually
*  execute on that mission and make it work. So that's the 10x solution.
*  What do you think is the timeline to solve the problem of autonomous driving?
*  That's still in part an open question. Yeah. I think the tough thing with timelines
*  of self-driving obviously is that no one has created self-driving. Yeah. So it's not like
*  what do you think is the timeline to build this bridge? Well, we've built million bridges before.
*  Here's how long that takes. No one has built autonomy. It's not obvious. Some parts
*  turn out to be much easier than others. So it's really hard to forecast. You do your best based on
*  trend lines and so on and based on intuition. But that's why fundamentally it's just really
*  hard to forecast this. No one has built it. So even still being inside of it is hard to do?
*  Yes. Some things turn out to be much harder and some things turn out to be much easier.
*  Do you try to avoid making forecasts? Because Elon doesn't avoid them, right?
*  And heads of car companies in the past have not avoided it either. Ford and other places
*  have made predictions that we're going to solve at level four driving by 2020, 2021, whatever.
*  And now they're all kind of backtracking that prediction. As an AI person,
*  do you for yourself privately make predictions or do they get in the way of your actual ability
*  to think about a thing? Yeah, I would say what's easy to say is that this problem is tractable
*  and that's an easy prediction to make. It's tractable. It's going to work. Yes, it's just
*  really hard. Some things turn out to be harder and some things turn out to be easier. But it
*  definitely feels tractable and it feels like at least the team at Tesla, which is what I saw
*  internally, is definitely on track to that. How do you form a strong representation that allows
*  you to make a prediction about tractability? So like you're the leader of a lot of humans,
*  you have to kind of say this is actually possible. How do you build up that intuition?
*  It doesn't have to be even driving. It could be other tasks. What difficult tasks did you
*  work on in your life? I mean classification, achieving certain, just an image net, certain
*  level of superhuman level performance. Yeah, expert intuition. It's just intuition. It's belief.
*  So just like thinking about it long enough, like studying, looking at sample data, like you said,
*  driving. My intuition is really flawed on this. I don't have a good intuition about tractability.
*  It could be anything. It could be solvable. The driving task could be simplified into something
*  quite trivial. The solution to the problem would be quite trivial. And at scale, more and more cars
*  driving perfectly might make the problem much easier. The more cars you have driving, people
*  learn how to drive correctly, not correctly, but in a way that's more optimal for a heterogeneous
*  system of autonomous and semi-autonomous and manually driven cars that could change stuff.
*  Then again, also I've spent a ridiculous number of hours just staring at pedestrians crossing
*  streets thinking about humans. And it feels like the way we use our eye contact, it sends really
*  strong signals and there's certain quirks and edge cases of behavior. And of course, a lot of
*  the fatalities that happen have to do with drunk driving and both on the pedestrian side and the
*  driver side. So there's that problem of driving at night and all that kind of. So I wonder, it's like
*  the space of possible solutions to autonomous driving includes so many human factor issues
*  that it's almost impossible to predict. There could be super clean, nice solutions.
*  I would say definitely to use a game analogy, there's some fog of war, but you definitely also
*  see the frontier of improvement and you can measure historically how much you've made progress.
*  And I think, for example, at least what I've seen in roughly five years at Tesla, when I joined,
*  it barely kept lane on the highway. I think going up from Palo Alto to SF was like three or four
*  interventions. Anytime the road would do anything geometrically or turn too much, it would just not
*  work. And so going from that to like a pretty competent system in five years and seeing what
*  happens also under the hood and what the scale of which the team is operating now with respect to
*  data and compute and everything else is just massive progress. So. So you're climbing a mountain
*  and there's fog, but you're making a lot of progress. Fog. You're making progress and you
*  see what the next directions are and you're looking at some of the remaining challenges and they're
*  not like, they're not perturbing you and they're not changing your philosophy and you're not
*  contorting yourself. You're like, actually, these are the things that we still need to do.
*  Yeah. The fundamental components of solving the problem seem to be there from the data engine to
*  the compute, to the compute on the car, to the compute for the training, all that kind of stuff.
*  So you've done over the years, you've been at Tesla, you've done a lot of amazing
*  breakthrough ideas and engineering, all of it from the data engine to the human side, all of it.
*  Can you speak to why you chose to leave Tesla? Basically, as I described that, Ren, I think over
*  time during those five years, I've kind of gotten myself into a bit of a managerial position. Most
*  of my days were meetings and growing the organization and making decisions about a sort
*  of high level strategic decisions about the team and what it should be working on and so on.
*  It's kind of like a corporate executive role and I can do it. I think I'm okay at it,
*  but it's not fundamentally what I enjoy. I think when I joined, there was no computer vision team
*  because Tesla was just going from the transition of using Mobileye, a third party vendor for all
*  of its computer vision, to having to build its computer vision system. So when I showed up,
*  there were two people training deep neural networks and they were training them at a computer
*  at their legs. Yeah. They're doing some kind of basic classification task.
*  Yeah. I kind of grew that into what I think is a fairly respectable deep learning team.
*  A massive computer cluster, a very good data annotation organization.
*  I was very happy with where that was. It became quite autonomous and so I kind of stepped away.
*  I'm very excited to do much more technical things again. Yeah. And kind of like we focus on AGI.
*  What was that soul searching like? Because you took a little time off and think like,
*  how many mushrooms did you take? No, I'm just kidding. I mean, what was going through your mind?
*  The human lifetime is finite. Yeah. You did a few incredible things. You're one of the best
*  teachers of AI in the world. You're one of the best, and I don't mean that, I mean that in the
*  best possible way, you're one of the best tinkerers in the AI world. Meaning like understanding the
*  fundamentals of how something works by building it from scratch and playing with the basic
*  intuitions. It's like Einstein, Feynman, we're all really good at this kind of stuff. Small example
*  of a thing to play with it, to try to understand it. So that, and obviously now with Tessa, you
*  helped build a team of machine learning, like engineers and a system that actually accomplishes
*  something in the real world. So given all that, what was the soul searching like?
*  Well, it was hard because obviously I love the company a lot and I love Elon, I love Tesla.
*  I want, it was always hard to leave. I love the team basically. But yeah, I think actually,
*  I will be potentially interested in revisiting it. Maybe coming back at some point,
*  working in Optimus, working in AGI at Tesla. I think Tesla is going to do incredible things.
*  It's basically like, it's a massive large scale robotics kind of company with a ton of in-house
*  talent for doing really incredible things. And I think human robots are going to be amazing.
*  I think autonomous transportation is going to be amazing. All this is happening at Tesla. So I
*  think it's just a really amazing organization. So being part of it and helping it along, I think
*  was very, basically I enjoyed that a lot. Yeah, it was basically difficult for those reasons because
*  I love the company. But I'm happy to potentially at some point come back for Act 2. But I felt
*  like at this stage, I built the team, it felt autonomous and I became a manager and I wanted
*  to do a lot more technical stuff. I wanted to learn stuff. I wanted to teach stuff. And I just
*  kind of felt like it was a good time for a change of pace a little bit. What do you think is the best
*  movie sequel of all time, speaking of part two? Because most of them suck. Movie sequels?
*  Movie sequels, yeah. And you tweeted about movies. So just in a tiny tangent, what's like a favorite
*  movie sequel? Godfather Part 2. Are you a fan of Godfather? Because you didn't even tweet or
*  mention the Godfather. Yeah, I don't love that movie. I know it has a huge follow-up. We're
*  going to edit out the hate towards the Godfather. How dare you disrespect- I think I will make a
*  strong statement. I don't know why. I don't know why, but I basically don't like any movie before
*  1995, something like that. Didn't you mention Terminator 2? Okay, okay. Terminator 2 was a little
*  bit later, 1990. No, I think Terminator 2 was in the 80s. And I like Terminator 1 as well. So,
*  okay, so like few exceptions, but by and large, for some reason, I don't like movies before 1995
*  or something. They feel very slow. The camera is like zoomed out. It's boring. It's kind of naive.
*  It's kind of weird. And also Terminator was very much ahead of its time. Yes. And the Godfather,
*  there's like no AGI. So- I mean, but you have Good Will Hunting was one of the movies you
*  mentioned and that doesn't have any AGI either. I guess that's mathematics. Yeah. I guess occasionally
*  I do enjoy movies that don't feature- Or like Anchorman. That's- Anchorman is so good.
*  I don't understand, speaking of AGI, because I don't understand why Will Ferrell is so funny.
*  It doesn't make sense. It doesn't compute. There's just something about him. And he's a singular human
*  because you don't get that many comedies these days. And I wonder if it has to do about the
*  culture or the machine of Hollywood or does it have to do with just we got lucky with certain
*  people in comedy. It came together because he is a singular human. Yeah. Yeah. I like his movies.
*  That was a ridiculous tangent. I apologize. But you mentioned humanoid robots. So what do you
*  think about Optimus, about TeslaBot? Do you think we'll have robots in the factory and in the home
*  in 10, 20, 30, 40, 50 years? Yeah. I think it's a very hard project. I think it's going to take a
*  while. Who else is going to build human robots at scale? And I think it is a very good form factor
*  to go after because like I mentioned, the world is designed for humanoid form factor. These things
*  would be able to operate our machines. They would be able to sit down in chairs, potentially even
*  drive cars. Basically, the world is designed for humans. That's the form factor you want to invest
*  into and make work over time. I think there's another school of thought, which is, okay,
*  pick a problem and design a robot to it. But actually designing a robot and getting a whole
*  data engine and everything behind it to work is actually an incredibly hard problem. So it makes
*  sense to go after general interfaces that, okay, they are not perfect for any one given task,
*  but they actually have the generality of just with a prompt with English able to do something
*  across. And so I think it makes a lot of sense to go after a general interface in the physical
*  world. And I think it's a very difficult project. I think it's going to take time.
*  But I see no other company that can execute on that vision. I think it's going to be amazing.
*  Like basically physical labor. Like if you think transportation is a large market,
*  try physical labor. It's insane. But it's not just physical labor. To me, the thing that's also
*  exciting is social robotics. So the relationship we'll have on different levels with those robots.
*  That's why I was really excited to see Optimus. People have criticized me for the excitement,
*  but I've worked with a lot of research labs that do humanoid, legged robots,
*  Boston Dynamics, Unitree. There's a lot of companies that do legged robots,
*  but that's the elegance of the movement is a tiny, tiny part of the big picture.
*  So integrating the two big exciting things to me about Tesla doing humanoid or any legged robots
*  is clearly integrating into the data engine. So the data engine aspect, so the actual intelligence
*  for the perception and the control and the planning and all that kind of stuff,
*  integrating into the fleet that you mentioned. And then speaking of fleet, the second thing is
*  the mass manufacturers, just knowing culturally driving towards a simple robot that's cheap to
*  produce at scale and doing that well, having experience to do that well. That changes
*  everything. That's a very different culture and style than Boston Dynamics, who by the way,
*  those robots are just the way they move. It'll be a very long time before Tesla could achieve
*  the smoothness of movement, but that's not what it's about. It's about the entirety of the system,
*  like we talked about the data engine and the fleet. That's super exciting. Even the initial
*  models, but that too was really surprising that in a few months you can get a prototype.
*  Yeah. And the reason that happened very quickly is as you alluded to, there's a ton of copy paste
*  from what's happening on the autopilot, a lot. The amount of expertise that came out of the
*  woodworks at Tesla for building the human robot was incredible to see. Basically, Elon said at one
*  point, we're doing this. And then next day, basically, all these CAD models started to appear.
*  People talk about the supply chain and manufacturing, and people showed up with
*  screwdrivers and everything the other day and started to put together the body. And I was like,
*  whoa, all these people exist at Tesla. And fundamentally, building a car is actually
*  not that different from building a robot. And that is true, not just for the hardware pieces,
*  and also, let's not forget hardware, not just for a demo, but manufacturing of that hardware at
*  scale. It is a whole different thing. But for software as well, basically, this robot currently
*  thinks it's a car. It's going to have a midlife crisis at some point. It thinks it's a car.
*  Some of the earlier demos, actually, we were talking about potentially doing them outside in
*  the parking lot because that's where all of the computer vision was working out of the box
*  instead of inside. But all the operating system, everything just copy pastes. Computer vision,
*  mostly copy pastes. You have to retrain the neural nets, but the approach and everything,
*  and data engine and offline trackers and the way we go about the occupancy tracker and so on,
*  everything copy pastes. You just need to retrain the neural nets. And then the planning control,
*  of course, has to change quite a bit. But there's a ton of copy paste from what's happening at Tesla.
*  And so if you were to go with the goal of, okay, let's build a million human robots and you're not
*  Tesla, that's a lot to ask. If you're Tesla, it's actually like, it's not that crazy.
*  And then the follow-up question is then how difficult, just like with driving,
*  how difficult is the manipulation task such that it can have an impact at scale? I think
*  depending on the context, the really nice thing about robotics is that unless you do a
*  manufacturer and that kind of stuff, is there is more room for error. Driving is so safety critical
*  and so that, and also time critical. A robot is allowed to move slower, which is nice.
*  Yes. I think it's going to take a long time, but the way you want to structure the development is
*  you need to say, okay, it's going to take a long time. How can I set up the product development
*  roadmap so that I'm making revenue along the way? I'm not setting myself up for a zero one
*  loss function where it doesn't work until it works. You don't want to be in that position.
*  You want to make it useful almost immediately, and then you want to slowly deploy it
*  and at scale. And you want to set up your data engine, your improvement loops,
*  the telemetry, the evaluation, the harness and everything. And you want to improve the product
*  over time incrementally and you're making revenue along the way. That's extremely important because
*  otherwise you cannot build these large undertakings just like don't make sense economically. And also
*  from the point of view of the team working on it, they need the dopamine along the way. They're not
*  just going to make a promise about this being useful. This is going to change the world in 10
*  years when it works. This is not where you want to be. You want to be in a place like I think
*  autopilot is today where it's offering increased safety and convenience of driving today. People
*  pay for it. People like it. People purchase it. And then you also have the greater mission that
*  you're working towards. And you see that. So the dopamine for the team, that was a source of
*  happiness and satisfaction. Yes, 100%. You're deploying this. People like it. People drive it.
*  People pay for it. They care about it. There's all these YouTube videos. Your grandma drives it. She
*  gives you feedback. People like it. People engage with it. You engage with it. Huge.
*  Do people that drive Teslas recognize you and give you love? Like, hey, thanks for this nice
*  feature that it's doing. Yeah, I think the tricky thing is some people really love you. Some people,
*  unfortunately, you're working on something that you think is extremely valuable, useful, etc.
*  Some people do hate you. There's a lot of people who hate me and the team and the whole project.
*  Are they Tesla drivers?
*  In many cases, they're not, actually.
*  Yeah, that actually makes me sad about humans or the current ways that humans interact. I think
*  that's actually fixable. I think humans want to be good to each other. I think Twitter and social
*  media is part of the mechanism that actually somehow makes the negativity more viral,
*  that it doesn't deserve disproportionately add a viral boost to the negativity.
*  I wish people would just get excited about, so suppress some of the jealousy, some of the ego,
*  and just get excited for others. Then there's a karma aspect to that. You get excited for others,
*  they'll get excited for you. Same thing in academia. If you're not careful, there is a
*  dynamical system there. If you think of in silos and get jealous of somebody else being successful,
*  that actually, perhaps counterintuitively, leads to less productivity of you as a community and
*  you individually. I feel like if you keep celebrating others, that actually makes you
*  more successful. I think people, depending on the industry, haven't quite learned that yet.
*  Some people are also very negative and very vocal, so they're very prominently featured.
*  Actually, there's a ton of people who are cheerleaders, but they're silent cheerleaders.
*  When you talk to people just in the world, they will tell you, it's amazing, it's great.
*  Especially people who understand how difficult it is to get this stuff working. People who have
*  built products and makers and entrepreneurs. Making this work and changing something
*  is incredibly hard. Those people are more likely to cheerlead you.
*  One of the things that makes me sad is some folks in the robotics community don't do the
*  cheerleading and they should because they know how difficult it is. Well, they actually sometimes
*  don't know how difficult it is to create a product that's scale. They actually deploy it in the real
*  world. A lot of the development of robots and AI systems is done on very specific small benchmarks
*  and as opposed to real world conditions. Yeah, I think it's really hard to work on robotics
*  in an academic setting. Or AI systems that apply in the real world. You've criticized,
*  you flourished and loved for time the image net, the famed image net data set.
*  And I've recently had some words of criticism that the academic research ML community gives
*  a little too much love still to the image net or those kinds of benchmarks. Can you speak to
*  the strengths and weaknesses of data sets used in machine learning research? Actually, I don't know
*  that I recall a specific instance where I was unhappy or criticizing image net. I think image
*  net has been extremely valuable. It was basically a benchmark that allowed the deep learning
*  community to demonstrate that deep neural networks actually work. There's a massive value in that.
*  So I think image net was useful, but basically it's become a bit of an MNIST at this point.
*  So MNIST is like little 228 by 28 grayscale digits. There's kind of a joke data set that
*  everyone just crushes. There's still papers written on MNIST though, right? Maybe there's
*  strong papers, like papers that focus on how do we learn with a small amount of data, that kind
*  of stuff. Yeah, I could see that being helpful, but not in sort of mainline computer vision
*  research anymore, of course. I think the way I've heard you somewhere, maybe I'm just imagining
*  things, but I think you said image net was a huge contribution to the community for a long time,
*  and now it's time to move past those kinds of... Well, image net has been crushed. I mean,
*  the error rates are... Yeah, we're getting like 90% accuracy in 1000 classification way.
*  Prediction. And I've seen those images and it's like really high. That's really good. If I remember
*  correctly, the top five error rate is now like 1% or something. Given your experience with a
*  gigantic real world data set, would you like to see benchmarks move in a certain directions
*  that the research community uses? Unfortunately, I don't think academics currently have the next
*  image net. We've obviously, I think we've crushed MNIST. We've basically kind of crushed image net,
*  and there's no next sort of big benchmark that the entire community rallies behind and uses
*  for further development of these networks. Yeah. What are what it takes for a data set to
*  captivate the imagination of everybody, like where they all get behind it? That could also need like
*  a leader, right? Yeah. Somebody with popularity. I mean, why did image net take off? Is it just
*  the accident of history? It was the right amount of difficult. It was the right amount of difficult
*  and simple and interesting enough. It just kind of like it was the right time for that kind of a
*  data set. Question from Reddit. What are your thoughts on the role that synthetic data and
*  game engines will play in the future of neural net model development? I think as neural nets
*  converge to humans, the value of simulation to neural nets will be similar to value of simulation
*  to humans. So people use simulation because they can learn something in that kind of a system
*  and without having to actually experience it. But are you referring to the simulation we do in our
*  head? No, sorry, simulation. I mean like video games or other forms of simulation for various
*  professionals. So let me push back on that because maybe there's simulation that we do in our heads
*  like simulate if I do this, what do I think will happen? Okay. That's like internal simulation.
*  Yeah. Internal. Isn't that what we're doing? Assuming before we act. Oh yeah, but that's
*  independent from like the use of simulation in the sense of like computer games or using simulation
*  for training set creation or- Is it independent or is it just loosely correlated? Because like,
*  isn't that useful to do like counterfactual or like edge case simulation to like,
*  you know, what happens if there's a nuclear war? What happens if there's, you know, like those kinds
*  of things? Yeah, that's a different simulation from like Unreal Engine. That's how I interpreted
*  the question. Ah, so like simulation of the average case. What's Unreal Engine? What do you
*  mean by Unreal Engine? So simulating a world, the physics of that world, why is that different?
*  Like, because you also can add behavior to that world and you could try all kinds of stuff, right?
*  You could throw all kinds of weird things into it. Unreal Engine is not just about simulating. I mean,
*  I guess it is about simulating the physics of the world. It's also doing something with that.
*  Yeah, the graphics, the physics and the agents that you put into the environment and stuff like
*  that. Yeah. See, I think you, I feel like you said that it's not that important, I guess,
*  for the future of AI development. Is that correct to interpret it that way? I think humans use
*  simulators for, humans use simulators and they find them useful. And so computers will use
*  simulators and find them useful. Okay. So you're saying it's not that I don't use simulators very
*  often. I play a video game every once in a while, but I don't think I derive any wisdom about my own
*  existence from those video games. It's a momentary escape from reality versus a source of wisdom
*  about reality. So I think that's a very polite way of saying simulation is not that useful.
*  Yeah, maybe not. I don't see it as like a fundamental, really important part of like
*  training neural nets currently. But I think as neural nets become more and more powerful,
*  I think you will need fewer examples to train additional behaviors. And simulation is, of course,
*  there's a domain gap in a simulation that is not the real world, that's slightly something different.
*  But with a powerful enough neural net, you need, the domain gap can be bigger, I think,
*  because neural net will sort of understand that even though it's not the real world, it has all
*  this high level structure that I'm supposed to be able to learn from. So the neural net will actually,
*  yeah, it will be able to leverage the synthetic data better by closing the gap, by understanding
*  in which ways this is not real data. Exactly.
*  Right, I do better questions next time. That was a question, but I'm just kidding. All right.
*  So is it possible, do you think, speaking of MNIST, to construct neural nets and training
*  processes that require very little data? So we've been talking about huge data sets like the internet
*  for training. I mean, one way to say that is, like you said, like the querying itself is another level
*  of training, I guess, and that requires a little data. But do you see any value in doing research
*  and kind of going down the direction of, can we use very little data to train, to construct
*  a knowledge base? 100%. I just think like at some point you need a massive data set. And then when
*  you pre-train your massive neural net and get something that is like a GPT or something, then
*  you're able to be very efficient at training any arbitrary new task. So a lot of these GPTs,
*  you can do tasks like sentiment analysis or translation or so on just by being prompted
*  with very few examples. Here's the kind of thing I want you to do. Here's an input sentence,
*  here's the translation into German. Input sentence, translation to German. Input sentence, blank,
*  and the neural net will complete the translation to German just by looking at the example you've
*  provided. And so that's an example of a very few shot learning in the activations of the neural
*  net instead of the weights of the neural net. And so I think basically just like humans, neural
*  nets will become very data efficient at learning any other new task. But at some point you need a
*  massive data set to pre-train your network. To get that. And probably we humans have something
*  like that. Do we have something like that? Do we have a passive in the background model constructing
*  thing that just runs all the time in a self-supervised way? We're not conscious
*  of it. I think humans definitely, I mean, obviously we learn a lot during our lifespan,
*  but also we have a ton of hardware that helps us at initialization coming from sort of evolution.
*  And so I think that's also a really big component. A lot of people in the field,
*  I think they just talk about the amounts of seconds that a person has lived pretending that
*  this is a WLRRSA, sort of like a zero initialization of a neural net. And it's not.
*  You can look at a lot of animals, like for example, zebras. Zebras get born and they see and they can
*  run. There's zero training data in their lifespan. They can just do that. So somehow I have no idea
*  how evolution has found a way to encode these algorithms and these neural net initializations
*  that are extremely good into ATCGs. And I have no idea how this works, but apparently it's possible
*  because here's a proof by existence. There's something magical about going from a single cell
*  to an organism that is born to the first few years of life. I kind of like the idea that the reason
*  we don't remember anything about the first few years of our life is that it's a really painful
*  process. Like it's a very difficult, challenging training process. Like intellectually. Like,
*  and maybe, yeah, I mean, I don't, why don't we remember any of that? There might be some crazy
*  training going on and that maybe that's the background model training that is very painful.
*  And so it's best for the system once it's trained not to remember how it's constructed.
*  I think it's just like the hardware for long-term memory is just not fully developed.
*  Sure. I kind of feel like the first few years of infants is not actually like learning. It's
*  brain maturing. We're born premature. There's a theory along those lines because of the birth
*  canal and the swallowing of the brain. And so we're born premature. And then the first few years,
*  we're just, the brain is maturing and then there's some learning eventually.
*  That's my current view on it. What do you think, do you think neural nets can have long-term memory?
*  Like that approach is something like humans. Do you think they need to be another meta
*  architecture on top of it to add something like a knowledge base that learns facts about the world
*  and all that kind of stuff? Yes, but I don't know to what extent it will be explicitly constructed.
*  It might take unintuitive forms where you are telling the GPT, like, hey, you have a declarative
*  memory bank to which you can store and retrieve data from. And whenever you encounter some
*  information that you find useful, just save it to your memory bank. And here's an example of
*  something you have retrieved and how you say it. And here's how you load from it. You just say,
*  load whatever you teach it in text in English, and then it might learn to use a memory bank from that.
*  Oh, so the neural net is the architecture for the background model, the base thing. And then
*  everything else is just on top of it. That's pretty easy to use.
*  It's not just text, right? You're giving it gadgets and gizmos. So you're teaching some
*  kind of a special language by which it can save arbitrary information and retrieve it at a later
*  time. And you're telling it about these special tokens and how to arrange them to use these
*  interfaces. It's like, hey, you can use a calculator. Here's how you use it. Just do 5, 3, plus 4,
*  1 equals. And when equals is there, a calculator will actually read out the answer and you don't
*  have to calculate it yourself. And you just tell it in English, this might actually work.
*  Do you think in that sense, Godot is interesting, the DeepMind system, that it's not just a language,
*  but actually throws it all in the same pile. Images, actions, all that kind of stuff. That's
*  basically what we're moving towards. Yeah, I think so. So Godot is very much a kitchen sink
*  of approach to reinforcement learning in lots of different environments with a single fixed
*  transformer model, right? I think it's a very early result in that realm. But I think, yeah,
*  it's along the lines of what I think things will eventually look like.
*  Right. So this is the early days of a system that eventually will look like this, like from a
*  rich, sudden perspective. Yeah, I'm not super huge fan of, I think, all these interfaces that
*  look very different. I would want everything to be normalized into the same API. So for example,
*  screen pixels, very same API, instead of having different world environments that have very
*  different physics and joint configurations and appearances and whatever, and you're having some
*  kind of special tokens for different games that you can plug. I'd rather just normalize everything
*  to a single interface. So it looks the same to the neural net, if that makes sense.
*  So it's all going to be pixel-based pong in the end.
*  I think so. Okay. Let me ask you about your own personal life. A lot of people want to know you're
*  one of the most productive and brilliant people in the history of AI. What does a productive day
*  in the life of Andrej Kapati look like? What time do you wake up usually? Because imagine
*  some kind of dance between the average productive day and a perfect productive day. So the perfect
*  productive day is the thing we strive towards, and the average is what it converges to,
*  given all the mistakes and human eventualities and so on. So what time do you wake up? Are you a
*  morning person? I'm not a morning person. I'm a night owl, for sure. Is it stable or not?
*  It's semi-stable, like eight or nine or something like that. During my PhD, it was even later. I
*  used to go to sleep usually at 3 a.m. I think the a.m. hours are precious and very interesting time
*  to work because everyone is asleep. At 8 a.m. or 7 a.m., the East Coast is awake. So there's
*  already activity. There's already some text messages, whatever. There's stuff happening.
*  You can go on some news website and there's stuff happening. It's distracting. At 3 a.m.,
*  everything is totally quiet. And so you're not going to be bothered, and you have solid chunks
*  of time to do work. So I like those periods, night owl by default. And then I think productive
*  time, basically, what I like to do is you need to build some momentum on the problem without too
*  much distraction. And you need to load your RAM, your working memory, with that problem.
*  And then you need to be obsessed with it when you're taking a shower, when you're falling
*  asleep. You need to be obsessed with the problem, and it's fully in your memory, and you're ready
*  to wake up and work on it right there. So is this in a scale, temporal scale,
*  of a single day or a couple of days, a week, a month? So I can't talk about one day basically
*  in isolation because it's a whole process. When I want to get productive in the problem,
*  I feel like I need a span of a few days where I can really get in on that problem.
*  And I don't want to be interrupted. And I'm going to just be completely obsessed with that problem.
*  And that's where I do most of my good workouts. You've done a bunch of cool little projects in a
*  very short amount of time, very quickly. So that requires you just focusing on it.
*  Yeah. Basically, I need to load my working memory with the problem, and I need to be productive,
*  because there's always a huge fixed cost to approaching any problem. I was struggling with
*  this, for example, at Tesla because I want to work on a small side project. But, okay, you first need
*  to figure out, oh, okay, I need to SSH into my cluster. I need to bring up a VS code editor so
*  I can work on this. I run into some stupid error because of some reason. You're not at a point
*  where you can be just productive right away. You are facing barriers. And so it's about really
*  removing all of that barrier, and you're able to go into the problem, and you have the full
*  problem loaded in your memory. And somehow avoiding distractions of all different forms,
*  like news stories, emails, but also distractions from other interesting projects that you
*  previously worked on or currently working on and so on. You just want to really focus your mind.
*  I can take some time off for distractions and in between, but I think it can't be too much.
*  Most of your day is spent on that problem. And then I drink coffee, I have my morning routine,
*  I look at some news, Twitter, Hacker News, Wall Street Journal, et cetera.
*  So basically, you wake up, you have some coffee. Are you trying to get to work as quickly as
*  possible? Do you take in this diet of what the hell is happening in the world first?
*  I do find it interesting to know about the world. I don't know that it's useful or good,
*  but it is part of my routine right now. So I do read through a bunch of news articles,
*  and I want to be informed. And I'm suspicious of it. I'm suspicious of the practice,
*  but currently that's where I am. Oh, you mean suspicious about the
*  positive effect of that practice on your productivity and your well-being?
*  My well-being psychologically, yeah. And also on your ability to deeply understand the world,
*  because there's a bunch of sources of information, you're not really focused
*  on deeply integrating it. Yeah, it's a little bit distracting.
*  In terms of a perfectly productive day, for how long of a stretch of time in one session do you
*  try to work and focus on a thing? A couple hours, is it one hour, is it 30 minutes, is it 10 minutes?
*  I can probably go a small few hours, and then I need some breaks in between for food and stuff.
*  And yeah, but I think it's still really hard to accumulate hours. I was using a tracker that told
*  me exactly how much time I spent coding any one day. And even on a very productive day,
*  I still spent only like six or eight hours. And it's just because there's so much padding,
*  commute, talking to people, food, et cetera. There's a cost of life, just living and sustaining
*  and homeostasis and just maintaining yourself as a human is very high.
*  And that there seems to be a desire within the human mind to participate in society that creates
*  that padding. Yeah. Because the most productive days I've ever had is just completely from start
*  to finish, just tuning out everything and just sitting there. And then you could do more than
*  six and eight hours. Is there some wisdom about what gives you strength to do tough days of long
*  focus? Yeah, just like whenever I get obsessed about a problem, something just needs to work,
*  something just needs to exist. It needs to exist. So you're able to deal with bugs and programming
*  issues and technical issues and design decisions that turn out to be the wrong ones. You're able
*  to think through all of that given that you want to think to exist. Yeah, it needs to exist. And
*  then I think to me also a big factor is, are other humans are going to appreciate it? Are they going
*  to like it? That's a big part of my motivation. If I'm helping humans and they seem happy,
*  they say nice things, they tweet about it or whatever, that gives me pleasure because I'm
*  doing something useful. So like you do see yourself sharing it with the world. Like what
*  it's on GitHub or through blog posts or through videos. Yeah, I was thinking about it. Like suppose
*  I did all these things, but did not share them. I don't think I would have the same amount of
*  motivation that I can build up. You enjoy the feeling of other people gaining value and happiness
*  from the stuff you've created. Yeah. What about diet? I saw you played with intermittent fast,
*  you fast. Does that help? With everything. With the things you played, what's been
*  most beneficial to your ability to mentally focus on a thing and just mental productivity and
*  happiness? You still fast? Yeah, I still fast, but I do intermittent fasting. But really what it means
*  at the end of the day is I skip breakfast. So I do 18, six roughly by default when I'm in my steady
*  state. If I'm traveling or doing something else, I will break the rules, but in my steady state,
*  I do 18, six. So I eat only from 12 to six. Not a hard rule and I break it often, but that's my
*  default. And then, yeah, I've done a bunch of random experiments. For the most part right now,
*  where I've been for the last year and a half, I want to say, is I'm plant-based or plant-forward.
*  I heard plant-forward. It sounds better. What does that mean exactly? I don't actually know
*  what the difference is, but it sounds better in my mind. But it just means I prefer plant-based food.
*  Raw or cooked? I prefer cooked and plant-based. So plant-based, forgive me, I don't actually know
*  how wide the category of plant entails. Well, plant-based just means that you're not
*  about it and you can flex. And you just prefer to eat plants and you're not trying to influence
*  other people. And if you come to someone's house party and they serve you a steak that they're
*  really proud of, you will eat it. Yes. Right. So you're not judging my... Oh, that's beautiful.
*  I mean, I'm on the flip side of that, but I'm very sort of flexible. Have you tried doing one meal a
*  day? I have accidentally, not consistently, but I've accidentally had that. I don't like it. I
*  think it makes me feel not good. It's too much of a hit. Yeah. And so currently I have about two
*  meals a day, 12 and six. I do that nonstop. I'm doing it now. I do it one meal a day. It's
*  interesting. It's an interesting feeling. Have you ever fasted longer than a day?
*  Yeah. I've done a bunch of water fasts because I was curious what happens.
*  What happens? Anything interesting? Yeah, I would say so. I mean, what's interesting is that you're
*  hungry for two days and then starting day three or so, you're not hungry. It's such a weird feeling
*  because you haven't eaten in a few days and you're not hungry. Isn't that weird? It's really weird.
*  One of the many weird things about human biology is figure something out. It finds another source
*  of energy or something like that or relaxes the system. I don't know how that works.
*  Yeah. The body is like, you're hungry, you're hungry. And then it just gives up. It's like,
*  okay, I guess we're fasting now. There's nothing. And then it just kind of focuses on trying to make
*  you not hungry and not feel the damage of that and trying to give you some space to figure out
*  the food situation. So are you still to this day most productive at night?
*  I would say I am, but it is really hard to maintain my PhD schedule, especially when I
*  was, say, working at Tesla and so on. It's a non-starter. But even now, people want to meet for
*  various events. Society lives in a certain period of time and you sort of have to work.
*  So it's hard to do a social thing and then after that return and do work.
*  Yeah, it's just really hard. That's why I try when I do social things,
*  that's right, not to do too much drinking so I can return and continue doing work.
*  But at Tesla, is there conversions? Tesla, but any company, is there a convergence towards a schedule
*  or is there more? Is that how humans behave when they collaborate? I need to learn about this.
*  Do they try to keep a consistent schedule where you're all awake at the same time?
*  I do try to create a routine and I try to create a steady state in which I'm
*  comfortable. So I have a morning routine, I have a day routine, I try to keep things to a steady
*  state and things are predictable and then your body just sort of sticks to that. And if you
*  try to stress that a little too much, it will create, when you're traveling and you're dealing
*  with jet lag, you're not able to really ascend to where you need to go.
*  Yeah, that's what you do about humans with the habits and stuff. What are your thoughts on work
*  life balance throughout a human lifetime? So Tesla in part was known for pushing people to
*  their limits in terms of what they're able to do, in terms of what they're trying to do,
*  in terms of how much they work, all that kind of stuff.
*  Yeah. I mean, I will say Tesla gets all too much bad rep for this because what's happening is Tesla,
*  it's a bursty environment. So I would say the baseline, my only point of reference is Google,
*  where I've interned three times and I saw what it's like inside Google and DeepMind. I would say
*  the baseline is higher than that, but then there's a punctuated equilibrium where once in a while,
*  there's a fire and people work really hard. And so it's spiky and bursty and then all the stories
*  get collected. How about the bursts? And then it gives the appearance of total insanity,
*  but actually it's just a bit more intense environment and there are fires and sprints.
*  And so I think definitely though, I would say it's a more intense environment than something
*  you would get. But in your person, forget all of that, just in your own personal life,
*  what do you think about the happiness of a human being, a brilliant person like yourself,
*  about finding a balance between work and life or is it such a thing, not a good thought experiment?
*  Yeah, I think balance is good, but I also love to have sprints that are out of distribution.
*  And that's when I think I've been pretty creative as well.
*  So sprints out of distribution means that most of the time you have a quote unquote balance.
*  I have balance most of the time. I like being obsessed with something once in a while.
*  Once in a while is what? Once a week, once a month, once a year?
*  Yeah, probably like say once a month or something.
*  Yeah. And that's when we get a new GitHub repo for monitoring?
*  Yeah, that's when you really care about a problem. It must exist. This will be awesome.
*  You're obsessed with it. And now you can't just do it on that day. You need to pay the fixed cost
*  of getting into the groove and then you need to stay there for a while. And then society will
*  come and they will try to mess with you and they will try to distract you. Yeah. The worst thing is
*  like a person who's like, I just need five minutes of your time. The cost of that is not five minutes
*  and society needs to change how it thinks about just five minutes of your time.
*  Right. It's never just one minute. It's just 30 seconds. Just a quick.
*  What's the big deal? Why are you being so? Yeah, no. What's your computer setup? What's
*  like the perfect? Are you somebody that's flexible to no matter what? Laptop, four screens?
*  Or do you prefer a certain setup that you're most productive?
*  I guess the one that I'm familiar with is one large screen, a 27 inch and my laptop on the side.
*  What operating system? I do max. That's my primary.
*  For all tasks. I would say OS X. But when you're working on deep learning, everything is Linux,
*  you're SSH into a cluster and you're working remotely. But what about the actual development
*  like they're using the ID? You would use, I think a good way is you just run VS code.
*  My favorite editor right now on your Mac, but you are actually, you have a remote folder
*  through SSH. So the actual files that you're manipulating are in the cluster somewhere else.
*  So what's the best ID? VS code. What else do people use? So I use EMAX still.
*  It may be cool. I don't know if it's maximum productivity. So what do you recommend in terms
*  of editors? You worked a lot of software engineers, editors for Python, C++ machine learning
*  applications. I think the current answer is VS code. Currently, I believe that's the best
*  IDE. It's got a huge amount of extensions. It has a GitHub copilot integration,
*  which I think is very valuable. What do you think about the copilot integration? I was actually,
*  I got to talk a bunch with Guido Narrazam, who's a creative Python and he loves copilot. He like,
*  he programs a lot with it. Yeah. Do you? Yeah, I use copilot. I love it. And it's free for me,
*  but I would pay for it. Yeah, I think it's very good. And the utility that I found with it was,
*  I would say there is a learning curve and you need to figure out when it's helpful and when
*  to pay attention to its outputs and when it's not going to be helpful, where you should not
*  pay attention to it. Because if you're just reading at suggestions all the time, it's not
*  a good way of interacting with it. But I think I was able to sort of mold myself to it. I find
*  it's very helpful, number one, in copy, paste and replace some parts. So when the pattern is clear,
*  it's really good at completing the pattern. And number two, sometimes it suggests APIs that I'm
*  not aware of. So it tells you about something that you didn't know. So- And that's an opportunity
*  to discover and you- It's an opportunity to, so I would never take copilot code as given. I almost
*  always copy a copy paste into a Google search and you see what this function is doing. And then
*  you're like, oh, it's actually exactly what I need. Thank you copilot. So you learn something.
*  So it's in part a search engine, part maybe getting the exact syntax correctly that once you see it-
*  It's that NP-hard thing. Once you see it, you know it's correct. But you yourself struggle.
*  You can verify efficiently, but you can't generate efficiently. And copilot really,
*  I mean, it's autopilot for programming. And currently it's doing the lane following,
*  which is like the simple copy paste and sometimes suggest. But over time it's going to become more
*  and more autonomous. And so the same thing will play out in not just coding, but actually across
*  many, many different things probably. But coding is an important one, right? Like writing programs.
*  How do you see the future of that developing the program synthesis? Like being able to write
*  programs that are more and more complicated. Because right now it's human supervised in
*  interesting ways. It feels like the transition will be very painful.
*  My mental model for it is the same thing will happen as with the autopilot. So currently
*  it's doing lane following, it's doing some simple stuff. And eventually we'll be doing autonomy and
*  people will have to intervene less and less. And those could be like testing mechanisms.
*  Like if it writes a function and that function looks pretty damn correct. But how do you know
*  it's correct? Because you're like getting lazier and lazier as a programmer. Like your ability to,
*  because like little bugs, but I guess it won't make little mistakes. No, it will.
*  Copilot will make off by one subtle bugs. It has done that to me. But do you think future systems
*  will? Or is it really the off by one is actually a fundamental challenge of programming?
*  In that case, it wasn't fundamental and I think things can improve. But
*  yeah, I think humans have to supervise. I am nervous about people not supervising what comes
*  out and what happens to, for example, the proliferation of bugs in all of our systems.
*  I'm nervous about that, but I think there will probably be some other copilots for bug finding
*  and stuff like that at some point. There'll be like a lot more automation for...
*  Oh man. It's like a program, a copilot that generates a compiler, one that does a linter,
*  one that does like a type checker. It's a committee of like a GPT sort of like...
*  And then there'll be like a manager for the committee. And then there'll be somebody that
*  says a new version of this is needed. We need to regenerate it. There were 10 GPTs, they were
*  forwarded and gave 50 suggestions. Another one looked at it and picked a few that they like.
*  A bug one looked at it and it was like, it's probably a bug. They got re-ranked by some other
*  thing. And then a final ensemble GPT comes in and is like, okay, given everything you guys have told
*  me, this is probably the next token. The feeling is the number of programmers in the world has been
*  growing and growing very quickly. Do you think it's possible that it'll actually level out and drop
*  to like a very low number with this kind of world? Because then you'll be doing software 2.0 programming
*  and you'll be doing this kind of generation of copoly type systems programming, but you won't
*  be doing the old school software 1.0 programming. I don't currently think that they're just going to
*  replace human programmers. I'm so hesitant saying stuff like this, right? Because this is going to
*  be replaced in five years. I know it's going to show that like this is where we thought,
*  because I agree with you, but I think we might be very surprised.
*  What's your sense of where we stand with language models? Does it feel like the beginning or the
*  middle or the end? The beginning, 100%. I think the big question in my mind is for sure GPT will
*  be able to program quite well, competently and so on. How do you steer the system? You still have
*  to provide some guidance to what you actually are looking for. And so how do you steer it? And how
*  do you talk to it? How do you audit it and verify that what is done is correct? And how do you work
*  with this? And it's as much not just an AI problem, but a UI UX problem. So beautiful, fertile ground
*  for so much interesting work for VS Code++ where it's not just human programming anymore. It's
*  amazing. Yeah. So you're interacting with the system. So not just one prompt, but it's iterative
*  prompting. You're trying to figure out having a conversation with the system. To me, that's
*  super exciting to have a conversation with the program I'm writing. Yeah. Maybe at some point,
*  you're just conversing with it. It's like, okay, here's what I want to do. Actually this variable,
*  maybe it's not even that low level as variable, but- You can also imagine,
*  can you translate this to C++ and back to Python and back to- Yeah, it already exists in some way.
*  But just doing it as part of the program experience, I think I'd like to write this
*  function in C++. Or you just keep changing for different programs because of different
*  syntax. Maybe I want to convert this into a functional language. And so you get to become
*  multilingual as a programmer and dance back and forth efficiently. Yeah. I mean, I think the UI
*  UX of it though is still very hard to think through because it's not just about writing code
*  on a page. You have an entire developer environment. You have a bunch of hardware on it. You have some
*  environmental variables. You have some scripts that are running in a Chrome job. There's a lot
*  going on to working with computers and how do these systems set up environment flags and work
*  across multiple machines and set up screen sessions and automate different processes. How all that
*  works and is auditable by humans and so on is a massive question at the moment. You've built
*  Archive Sanity. What is Archive and what is the future of academic research publishing that you
*  would like to see? Archive is this preprint server. If you have a paper, you can submit it
*  for publication to journals or conferences and then wait six months and then maybe get a decision,
*  pass or fail, or you can just upload it to Archive. And then people can tweet about it three minutes
*  later and then everyone sees it, everyone reads it, and everyone can profit from it in their own
*  own ways. You can cite it and it has an official look to it. It feels like a publication process.
*  It feels different than if you just put in a blog post.
*  Yeah. It's a paper and usually the bar is higher for something that you would expect on
*  Archive as opposed to something you would see in a blog post.
*  Well, the culture created the bar because you could probably host a pretty crappy
*  paper in Archive. What does that make you feel like? What does that make you feel about peer
*  review? Rigorous peer review by two, three experts versus the peer review of the community
*  right as it's written. Yeah. Basically, I think the community is very
*  well able to peer review things very quickly on Twitter. And I think maybe it just has to
*  do something with AI machine learning field specifically though. I feel like things are
*  more easily auditable and the verification is easier potentially than the verification somewhere
*  else. So it's kind of like you can think of these scientific publications as like little
*  blockchains where everyone's building on each other's work and citing each other.
*  And you sort of have AI, which is kind of like this much faster and loose blockchain.
*  But then you have any one individual entry is like very cheap to make. And then you have other
*  fields where maybe that model doesn't make as much sense. And so I think in AI at least,
*  things are pretty easily verifiable. And so that's why when people upload papers,
*  they're a really good idea and so on. People can try it out the next day and they can be the final
*  arbiter of whether it works or not on their problem. And the whole thing just moves significantly
*  faster. So I kind of feel like academia still has a place. So this like conference journal
*  process still has a place, but it's sort of like it lags behind, I think. And it's a bit more maybe
*  higher quality process, but it's not sort of the place where you will discover cutting edge work
*  anymore. It used to be the case when I was starting my PhD that you go to conferences and journals
*  and you discuss all the latest research. Now when you go to a conference or journal, like no one
*  discusses anything that's there because it's already like three generations ago irrelevant.
*  Which makes me sad about like DeepMind, for example, where they still publish in nature
*  and these big prestigious... I mean, there's still value, I suppose, to the prestige that comes with
*  these big venues, but the result is that they'll announce some breakthrough performance and it'll
*  take like a year to actually publish the details. And those details, if they were published
*  immediately, would inspire the community to move in certain directions with that.
*  Yeah, it would speed up the rest of the community, but I don't know to what extent
*  that's part of their objective function also. That's true. So it's not just the prestige,
*  a little bit of the delay is part of it. Yeah, they certainly, DeepMind specifically has been
*  working in the regime of having slightly higher quality basically process and latency
*  and publishing those papers that way. Another question from Reddit. Do you or have you suffered
*  from imposter syndrome? Being the director of AI at Tesla, being this person when you're at
*  Stanford where the world looks at you as the expert in AI to teach the world about machine learning.
*  When I was leaving Tesla after five years, I spent a ton of time in meeting rooms
*  and I would read papers. In the beginning when I joined Tesla, I was writing code and then I was
*  writing less and less code and I was reading code and then I was reading less and less code.
*  This is just a natural progression that happens, I think. Definitely, I would say near the tail end,
*  that's when it starts to hit you a bit more that you're supposed to be an expert, but actually
*  the source of truth is the code that people are writing, the GitHub and the actual code itself.
*  You're not as familiar with that as you used to be. I would say maybe there's some insecurity there.
*  Yeah, that's actually pretty profound that a lot of the insecurity has to do with not writing the
*  code in the computer science space because that is the truth. That right there.
*  Code is the source of truth, the papers and everything else. It's a high-level summary.
*  Just a high-level summary, but at the end of the day, you have to read code. It's impossible
*  to translate all that code into actual paper form. When things come out, especially when
*  they have a source code available, that's my favorite place to go.
*  Like I said, you're one of the greatest teachers of machine learning, AI ever. From CS231N to today,
*  what advice would you give to beginners interested in getting into machine learning?
*  Beginners are often focused on what to do. I think the focus should be more like how much you do.
*  I am a believer on a high level in this 10,000 hours concept where
*  you just have to pick the things where you can spend time and you care about and you're
*  interested in. You literally have to put in 10,000 hours of work. It doesn't even matter as much
*  where you put it. You'll iterate and you'll improve and you'll waste some time. I don't know
*  if there's a better way. You need to put in 10,000 hours. I think it's actually really nice because
*  I feel like there's some sense of determinism about being an expert at a thing if you spend
*  10,000 hours. You can literally pick an arbitrary thing. I think if you spend 10,000 hours of
*  deliberate effort and work, you actually will become an expert at it. I think that's a nice
*  thought. Basically, I would focus more on are you spending 10,000 hours? That's what I would focus
*  on. Then thinking about what kind of mechanisms maximize your likelihood of getting to 10,000
*  hours, which for us silly humans means probably forming a daily habit of every single day actually
*  doing the thing. Whatever helps you. I do think to a large extent, it's a psychological problem
*  for yourself. One other thing that I think is helpful for the psychology of it is many times
*  people compare themselves to others in the area. I think this is very harmful. Only compare yourself
*  to you from some time ago, say a year ago. Are you better than you a year ago? This is the only way
*  to think. I think then you can see your progress and it's very motivating.
*  RG That's so interesting that focus on the quantity of hours. I think a lot of people
*  in the beginner stage, but actually throughout, get paralyzed by the choice. Which one do I pick? This
*  path or this path? They'll literally get paralyzed by which ID to use.
*  Well, they're worried about all these things, but the thing is, you will waste time doing something
*  wrong. You will eventually figure out it's not right. You will accumulate scar tissue and next
*  time you'll grow stronger because next time you'll have the scar tissue and next time you'll learn
*  from it. Now, next time you come to a similar situation, you'll be like, oh, I messed up.
*  I've spent a lot of time working on things that never materialize into anything. I have all that
*  scar tissue and I have some intuitions about what was useful, what wasn't useful, how things turned
*  out. All those mistakes were not dead work. I just think you should just focus on working.
*  What have you done? What have you done last week?
*  RG That's a good question actually to ask for a lot of things, not just machine learning.
*  It's a good way to cut the, I forgot what the term we used, but the fluff, the blubber, whatever,
*  the inefficiencies in life. What do you love about teaching? You seem to find yourself
*  often drawn to teaching. You're very good at it, but you're also drawn to it.
*  RG I don't think I love teaching. I love happy humans and happy humans like when I teach.
*  I wouldn't say I hate teaching. I tolerate teaching, but it's not like the act of teaching
*  that I like. It's that I have something, I'm actually okay at it. I'm okay at teaching and
*  people appreciate it a lot. I'm just happy to try to be helpful and teaching itself is
*  not like the most, I mean, it can be really annoying, frustrating. I was working on a bunch
*  of lectures just now. I was reminded back to my days of 231 and just how much work it is to create
*  some of these materials and make them good. The amount of iteration and thought and you go down
*  blind alleys and just how much you change it. So creating something good in terms of educational
*  value is really hard and it's not fun. RG It's difficult. So for people who definitely
*  go watch your new stuff, there are lectures where you're actually building the thing from,
*  like you said, the code is truth. So discussing backpropagation by building it, by looking
*  through it and just the whole thing. So how difficult is that to prepare for? I think that's
*  a really powerful way to teach. Did you have to prepare for that or are you just live thinking
*  through it? RG I will typically do like say three takes and then I take like the better take. So I
*  do multiple takes and then I take some of the better takes and then I just build out a lecture
*  that way. Sometimes I have to delete 30 minutes of content because it just went down the alley that
*  I didn't like too much. So there's a bunch of iteration and it probably takes me somewhere
*  around 10 hours to create one hour of content. RG To get one hour. It's interesting. I mean,
*  is it difficult to go back to the basics? Do you draw a lot of wisdom from going back to the basics?
*  RG Yeah. Going back to backpropagation, loss functions, where they come from.
*  And one thing I like about teaching a lot honestly is it definitely strengthens your understanding.
*  So it's not a purely altruistic activity. It's a way to learn. If you have to explain something
*  to someone, you realize you have gaps in knowledge. And so I even surprised myself in those lectures.
*  The result will obviously look at this and then the result doesn't look like it. And I'm like,
*  okay, I thought I understood this. RG That's why it's really cool. Literally code,
*  you run it in a notebook and it gives you a result and you're like, oh, wow. And like actual numbers,
*  actual input, actual code. RG Yeah, it's not mathematical symbols,
*  etc. The source of truth is the code. It's not slides. It's just like, let's build it.
*  RG It's beautiful. You're a rare human in that sense. What advice would you give to researchers
*  trying to develop and publish idea that have a big impact in the world of AI? So maybe
*  undergrads, maybe early graduate students? RG Yeah. I mean, I would say like they definitely
*  have to be a little bit more strategic than I had to be as a PhD student because of the way AI is
*  evolving. It's going the way of physics where in physics you used to be able to do experiments
*  on your bench top and everything was great and you could make progress. And now you have to work in
*  like LHC or like CERN. And so AI is going in that direction as well. So there's certain kinds of
*  things that's just not possible to do on the bench top anymore. And I think that didn't use
*  to be the case at the time. RG Do you still think that there's like
*  GAN type papers to be written? Where like, very simple idea that requires just one computer to
*  illustrate a simple example? RG I mean, one example that's been very influential recently
*  is diffusion models. Diffusion models are amazing. Diffusion models are six years old. For the longest
*  time, people were kind of ignoring them, as far as I can tell. And they're an amazing generative model,
*  especially in images. And so stable diffusion and so on. It's all diffusion based. Diffusion is new.
*  It was not there and came from, well, it came from Google, but a researcher could have come up with
*  it. In fact, some of the first actually, no, those came from Google as well. But a researcher could
*  come up with that in an academic institution. RG Yeah, what do you find most fascinating about
*  diffusion models? So from the societal impact of the technical architecture? RG What I like
*  about diffusion is it works so well. DG Was that surprising to you? The amount of the variety,
*  almost the novelty of the synthetic data is generating. RG Yeah, so the stable diffusion
*  images are incredible. It's the speed of improvement in generating images has been insane.
*  We went very quickly from generating like tiny digits to tiny faces, and it all looked messed up.
*  And now we were stable diffusion. And that happened very quickly. There's a lot that academia
*  can still contribute. You know, for example, flash attention is a very efficient kernel for
*  running the attention operation inside the transformer that came from academic environment.
*  It's a very clever way to structure the kernel that does the calculation. So it doesn't materialize
*  the attention matrix. And so there's I think there's still like lots of things to contribute,
*  but you have to be just more strategic. RG Do you think neural networks can be made to reason?
*  DG Yes. RG Do you think they already reason? DG Yes.
*  RG What's your definition of reasoning? DG Information processing.
*  RG So in the way that humans think through a problem and come up with novel ideas,
*  it feels like reasoning. So the novelty, I don't want to say but out of distribution ideas,
*  you think it's possible? DG Yes. And I think we're seeing that already in the current neural nets.
*  You're able to remix the training set information into true generalization in some sense.
*  RG That doesn't appear in a fundamental way in the training set.
*  DG Like you're doing something interesting algorithmically, you're manipulating
*  some symbols and you're coming up with some correct unique answer in a new setting.
*  RG What would illustrate to you, holy shit, this thing is definitely thinking?
*  DG To me, thinking or reasoning is just information processing and generalization.
*  And I think the neural nets already do that today. RG So being able to perceive the world
*  or perceive whatever the inputs are and to make predictions based on that or actions based on that,
*  that's reasoning. DG Yeah, you're giving correct answers in novel settings
*  by manipulating information. You've learned the correct algorithm. You're not doing just some kind
*  of a lookup table on the Earth's neighbor search, something like that.
*  RG Let me ask you about AGI. What are some moonshot ideas you think might make significant
*  progress towards AGI? Or maybe in other ways, what are the big blockers that we're missing now?
*  DG So basically, I am fairly bullish on our ability to build AGI's. Basically, automated
*  systems that we can interact with and are very human-like, and we can interact with them in a
*  digital realm or physical realm. Currently, it seems most of the models that do these magical
*  tasks are in a text realm. I think, as I mentioned, I'm suspicious that the text realm is not enough
*  to actually build full understanding of the world. I do actually think you need to go into pixels
*  and understand the physical world and how it works. So I do think that we need to extend these models
*  to consume images and videos and train on a lot more data that is multimodal in that way.
*  RG Do you think you need to touch the world to understand it also?
*  DG Well, that's the big open question I would say in my mind is if you also require the embodiment
*  and the ability to interact with the world, run experiments, and have data of that form,
*  then you need to go to Optimus or something like that. I would say Optimus in some way is like a
*  hedge in AGI because it seems to me that it's possible that just having data from the internet
*  is not enough. If that is the case, then Optimus may lead to AGI because to me, there's nothing
*  beyond Optimus. You have this humanoid form factor that can actually do stuff in the world.
*  You can have millions of them interacting with humans and so on. If that doesn't give rise to
*  AGI at some point, I'm not sure what will. From a completeness perspective, I think that's a really
*  good platform, but it's a much harder platform because you are dealing with atoms and you need
*  to actually build these things and integrate them into society. I think that path takes longer,
*  but it's much more certain. Then there's a path of the internet and just training these compression
*  models effectively on trying to compress all the internet. That might also give these agents as
*  well. RG Compress the internet, but also interact with the internet. It's not obvious to me
*  in fact, I suspect you can reach AGI without ever entering the physical world,
*  which is a little bit more concerning because that results in it happening faster.
*  It just feels like we're in boiling water. We won't know as it's happening.
*  I'm not afraid of AGI. I'm excited about it. There's always concerns, but I would like to know
*  when it happens and have hints about when it happens. A year from now, it will happen,
*  that kind of thing. I just feel like in the digital realm, it just might happen.
*  I think all we have available to us because no one has built AGI again. All we have available to us
*  is, is there enough fertile ground on the periphery? I would say yes. We have the progress
*  so far, which has been very rapid. There are next steps that are available. I would say,
*  yeah, it's quite likely that we'll be interacting with digital entities.
*  How will you know that somebody has built AGI? I think it's going to be a slow incremental
*  transition. It's going to be product-based and focused. It's going to be GitHub copilot
*  getting better and then GPT is helping you write. Then these oracles that you can go to with
*  mathematical problems, I think we're on the verge of being able to ask very complex questions in
*  chemistry, physics, math of these oracles and have them complete solutions.
*  AGI to use primarily focused on intelligence, so consciousness doesn't enter into it.
*  In my mind, consciousness is not a special thing you will figure out and bolt on. I think it's an
*  emerging phenomenon of a large enough and complex enough generative model. If you have a complex
*  enough world model that understands the world, then it also understands its predicament in the
*  world as being a language model, which to me is a form of consciousness or self-awareness.
*  In order to understand the world deeply, you probably have to integrate yourself into the
*  world. In order to interact with humans and other living beings,
*  consciousness is a very useful tool. I think consciousness is like a modeling insight.
*  Modeling insight. Yeah, you have a powerful enough model of understanding the world that
*  you actually understand that you are an entity in it. Yeah, but there's also this,
*  perhaps just a narrative we tell ourselves. It feels like something to experience the world,
*  the hard problem of consciousness, but that could be just a narrative that we tell ourselves.
*  Yeah, I think it will emerge. I think it's going to be something very boring. We'll be talking to
*  these digital AIs. They will claim they're conscious. They will appear conscious. They
*  will do all the things that you would expect of other humans, and it's going to just be a stalemate.
*  I think there will be a lot of actual fascinating ethical questions, like Supreme Court level
*  questions of whether you're allowed to turn off a conscious AI. If you're allowed to build a
*  conscious AI, maybe there would have to be the same kind of debates that you have around,
*  sorry to bring up a political topic, but abortion, which is the deeper question with abortion,
*  is what is life? The deep question with AI is also what is life and what is conscious? I think
*  that will be very fascinating to bring up. It might become illegal to build systems that are
*  capable of such level of intelligence that consciousness would emerge and therefore the
*  capacity to suffer would emerge, and a system that says, no, please don't kill me. Well, that's what
*  the Lambda Chatbot already told this Google engineer. It was talking about not wanting to die
*  or so on. That might become illegal to do that. Right. Because otherwise you might have a lot of
*  creatures that don't want to die. You can just spawn infinity of them in a cluster.
*  And then that might lead to horrible consequences because then there might be a lot of people that
*  secretly love murder and they'll start practicing murder in those systems. To me, all of this stuff
*  just brings a beautiful mirror to the human condition and human nature. We'll get to explore
*  it. And that's what the best of the Supreme Court, of all the different debates we have about ideas
*  of what it means to be human. We get to ask those deep questions that we've been asking throughout
*  human history. There has always been the other in human history. We're the good guys and that's the
*  bad guys. And we're going to, throughout human history, let's murder the bad guys.
*  And the same will probably happen with robots. There'll be the other at first, and then we'll
*  get to ask questions. What does it mean to be alive? What does it mean to be conscious?
*  Yeah. And I think there's some canary in the coal mines, even with what we have today.
*  For example, there's these waifus that you work with and some people are trying to,
*  this company is going to shut down, but this person really loved their waifu and is trying
*  port it somewhere else and it's not possible. I think definitely people will have feelings
*  towards these systems because in some sense, they are like a mirror of humanity
*  because they are sort of like a big average of humanity in the way that it's trained.
*  That average, we can actually watch. It's nice to be able to interact with the big average of
*  humanity and do a search query on it. Yeah. Yeah, it's very fascinating.
*  And we can of course also shape it. It's not just a pure average. We can mess with the training data,
*  we can mess with the objective, we can fine tune them in various ways. So we have some impact on
*  what those systems look like. Once we achieve AGI and you could have a conversation with her
*  and talk about anything, maybe ask her a question, what kind of stuff would you ask?
*  I would have some practical questions in my mind like,
*  do I or my loved ones really have to die? What can we do about that?
*  Do you think it will answer clearly or would it answer poetically?
*  I would expect it to give solutions. I would expect it to be like, well, I've read all of
*  these textbooks and I know all these things that you've produced and it seems to me like,
*  here are the experiments that I think it would be useful to run next and here are some gene
*  therapies that I think would be helpful and here are the kinds of experiments that you should run.
*  Okay, let's go with this thought experiment. Imagine that mortality is actually
*  like a prerequisite for happiness. So if we become immortal, we'll actually become deeply unhappy
*  and the model is able to know that. So what is this supposed to tell you, stupid human, about it?
*  Yes, you can become immortal, but you will become deeply unhappy. If the AGI system is trying to
*  empathize with you human, what is this supposed to tell you? That yes, you don't have to die,
*  but you're really not going to like it? Is it going to be deeply honest? There's an interstellar,
*  what is it? The AI says humans want 90% honesty. So you have to pick how honest do I want to answer
*  these practical questions. Yeah. I love the AI interstellar by the way. I think it's such a side
*  kick to the entire story, but at the same time, it's really interesting. It's kind of limited
*  in certain ways, right? Yeah, it's limited and I think that's totally fine by the way. I think
*  it's fine and plausible to have limited and imperfect AGI's. Is that the feature almost?
*  As an example, it has a fixed amount of compute on its physical body and it might just be that
*  even though you can have a super amazing mega brain, super intelligent AI, you also can have
*  less intelligent AIs that you can deploy in a power efficient way and then they're not perfect,
*  they might make mistakes. No, I meant more like say you had infinite compute and it's still good
*  to make mistakes sometimes. In order to integrate yourself, what is it? Going back to Good Will
*  Hunting, Robin Williams' character says the human imperfections, that's the good stuff, right?
*  Isn't that like we don't want perfect, we want flaws in part to form connections with each other
*  because it feels like something you can attach your feelings to, the flaws. In that same way,
*  you want AI that's flawed. I don't know. I feel like perfection is cool. But then you're saying,
*  okay, yeah. But that's not AGI. But see, AGI would need to be intelligent enough to give answers to
*  humans that humans don't understand. And I think perfect isn't something humans can't understand
*  because even science doesn't give perfect answers. There's always gaps and mysteries and
*  I don't know. I don't know if humans want perfect.
*  Yeah, I could imagine just having a conversation with this kind of oracle entity
*  as you'd imagine them. And yeah, maybe it can tell you about based on my analysis of human condition,
*  you might not want this and hear some of the things that might.
*  But every dumb human will say, yeah, yeah, yeah, yeah, trust me. Give me the truth. I can handle it.
*  But that's the beauty. People can choose.
*  But then the old marshmallow test with the kids and so on, I feel like too many people
*  can't handle the truth, probably including myself. The deep truth of the human condition,
*  I don't know if I can handle it. What if there's some dark stuff? What if we are an alien science
*  experiment and it realizes that? What if it had... Yeah. This is the matrix all over again.
*  I don't know. What would I talk about? I don't even, yeah. Probably I'll go with the safer
*  scientific questions at first that have nothing to do with my own personal life and mortality.
*  And mortality, just like about physics and so on. To build up, let's see where it's at,
*  or maybe see if it has a sense of humor. That's another question. Would it be able to,
*  presumably in order to, if it understands humans deeply, would be able to generate humor.
*  Yeah. I think that's actually a wonderful benchmark almost. I think that's a really
*  good point basically. To make you laugh.
*  Yeah. If it's able to be a very effective standup comedian, then it's doing something very
*  interesting computationally. I think being funny is extremely hard.
*  Yeah. Because it's hard in a way, like a Turing test, the original intent of the Turing test is
*  hard because you have to convince humans. And there's nothing... That's why comedians talk
*  about this. This is deeply honest because if people can't help but laugh, and if they don't laugh,
*  that means you're not funny. If they laugh, it's funny.
*  And you're showing you need a lot of knowledge to create humor about like the
*  documentation, human condition and so on. And then you need to be clever with it.
*  You mentioned a few movies. You tweeted, movies that I've seen five plus times, but
*  I'm ready and willing to keep watching. Interstellar, Gladiator, Contact, Good Will,
*  Hunting, The Matrix, Lord of the Rings, all three, Avatar, Fifth Element, so on. It goes on.
*  Terminator 2. Mean Girls, I'm not going to ask about that one.
*  I think. I think her man...
*  Mean Girls is great.
*  What are some of the jump onto your memory that you love and why? You mentioned The Matrix.
*  As a computer person, why do you love The Matrix?
*  There's so many properties that make it beautiful and interesting. So there's all
*  these philosophical questions, but then there's also AGI's and there's simulation and it's cool.
*  And there's the black...
*  The look of it, the feel of it.
*  The look of it, the feel of it, the action, the bullet time. It was just innovating in so many ways.
*  And then Good Will Hunting, why do you like that one?
*  Yeah, I really like this tortured genius sort of character who's grappling with whether or not
*  he has any responsibility or what to do with this gift that he was given or how to think about the
*  whole thing. But there's also a dance between the
*  genius and the personal, what it means to love another human being.
*  There's a lot of themes there. It's just a beautiful movie.
*  And then the fatherly figure, the mentor and the psychiatrist.
*  And it really messes with you. There's some movies that just really mess with you on a deep level.
*  Do you relate to that movie at all?
*  No.
*  It's not your fault, Andre, as I said. Lord of the Rings, that's self-explanatory.
*  Terminator 2, which is interesting.
*  You rewatch that a lot. Is that better than Terminator 1?
*  You like Arnold?
*  I do like Terminator 1 as well. I like Terminator 2 a little bit more,
*  but in terms of surface properties.
*  Do you think Skynet is at all a possibility?
*  Yes.
*  Like the actual sort of autonomous weapon system kind of thing?
*  Do you worry about that stuff?
*  I do worry about it.
*  AI being useful war?
*  I 100% worry about it.
*  Some of these fears of AGI's and how this will plan out,
*  these will be very powerful entities probably at some point.
*  For a long time, they're going to be tools in the hands of humans.
*  People talk about alignment of AGI's and how to make...
*  The problem is even humans are not aligned.
*  How this will be used and what this is going to look like is troubling.
*  Do you think it'll happen slowly enough that we'll be able to,
*  as a human civilization, think through the problems?
*  Yes. That's my hope is that it happens slowly enough and in an open enough way
*  where a lot of people can see and participate in it.
*  Just figure out how to deal with this transition, I think, which is going to be interesting.
*  I draw a lot of inspiration from nuclear weapons because I sure thought it would be fucked
*  once they developed nuclear weapons.
*  It's almost like when the systems are not so dangerous, they destroy human civilization,
*  we deploy them and learn the lessons.
*  If it's too dangerous, we might still deploy it, but you very quickly learn not to use them.
*  There'll be this balance achieved.
*  Humans are very clever as a species.
*  It's interesting.
*  We exploit the resources as much as we can, but we avoid destroying ourselves, it seems like.
*  Well, I don't know about that, actually.
*  I hope it continues.
*  I'm definitely concerned about nuclear weapons and so on, not just as a result of the recent
*  conflict even before that. That's probably my number one concern for humanity.
*  If humanity destroys itself or destroys 90% of people, that would be because of nukes?
*  I think so. It's not even about full destruction. To me, it's bad enough if we reset society.
*  That would be terrible. It would be really bad. I can't believe we're so close to it.
*  It's so crazy to me.
*  It feels like we might be a few tweets away from something like that.
*  Yep. Basically, it's extremely unnerving and has been for me for a long time.
*  It seems unstable that world leaders just having a bad mood can take one step towards a bad
*  direction and it escalates. Because of a collection of bad moods, it can escalate
*  without being able to stop.
*  It's a huge amount of power. Then also with the proliferation, basically, I don't actually
*  really see... I don't actually know what the good outcomes are here. I'm definitely worried about
*  it a lot. Then AGI is not currently there, but I think at some point will more and more become
*  something like it. The danger with AGI even is that I think it's even slightly worse in the sense
*  that there are good outcomes of AGI. Then the bad outcomes are like an epsilon away, like a tiny
*  one away. I think capitalism and humanity and so on will drive for the positive ways of using that
*  technology. But then if bad outcomes are just like a tiny flip of minus sign away, that's a really
*  bad position to be in.
*  A tiny perturbation of the system results in the destruction of the human species. It's a weird
*  line to walk.
*  I think in general, what's really weird about the dynamics of humanity and this explosion we've
*  talked about is just like the insane coupling afforded by technology and just the instability
*  of the whole dynamical system. I think it just doesn't look good, honestly.
*  That explosion could be destructive and constructive and the probabilities are non-zero in both.
*  Yeah, I do feel like I have to try to be optimistic and so on. I think even in this case,
*  I still am predominantly optimistic, but there's definitely...
*  Me too. Do you think we'll become a multi-planetary species?
*  Probably yes, but I don't know if it's a dominant feature of future humanity. There might be some
*  people on some planets and so on, but I'm not sure if it's like a major player in our culture and so
*  on.
*  We still have to solve the drivers of self-destruction here on Earth. Just having a
*  backup on Mars is not going to solve the problem.
*  By the way, I love the backup on Mars. I think that's amazing. We should absolutely do that.
*  And I'm so thankful for anyone who...
*  Would you go to Mars?
*  Personally, no. I do like Earth quite a lot.
*  I'll go to Mars. I'll go for you. I'll tweet at you from there.
*  Maybe eventually I would once it's safe enough, but I don't actually know if it's
*  on my lifetime scale unless I can extend it by a lot.
*  I do think that, for example, a lot of people might disappear into
*  virtual realities and stuff like that. I think that could be the major thrust of
*  the cultural development of humanity if it survives.
*  It's just really hard to work in physical realm and go out there.
*  I think ultimately all your experiences are in your brain.
*  It's much easier to disappear into digital realm.
*  I think people will find them more compelling, easier, safer, more interesting.
*  So you're a little bit captivated by virtual reality, by the possible worlds,
*  whether it's the metaverse or some other manifestation of that.
*  Yeah.
*  Yeah, it's really interesting. I'm interested, just talking a lot to Carmack,
*  where's the thing that's currently preventing that?
*  Yeah. To be clear, I think what's interesting about the future is
*  it's not that... I feel like the variance in the human condition grows.
*  That's the primary thing that's changing. It's not as much the mean of the distribution,
*  it's the variance of it. So there will probably be people on Mars and there will be people in VR
*  and there will be people here on earth. It's just like there will be so many more ways of being.
*  So I feel like I see it as a spreading out of a human experience.
*  There's something about the internet that allows you to discover those little groups and then
*  gravitate to something about your biology, likes that kind of world that you find each other.
*  Yeah. And we'll have transhumanists and then we'll have the Amish and everything is just
*  going to coexist. Yeah. The cool thing about it,
*  because I've interacted with a bunch of internet communities, is they don't know about each other.
*  Like you can have a very happy existence, just like having a very close-knit community and not
*  knowing about each other. I mean, you even sense this, just having traveled to Ukraine,
*  there's, they don't know so many things about America. When you travel across the world,
*  they think you experience this too. There are certain cultures that are like, they have their
*  own thing going on. So you can see that happening more and more and more and more in the future.
*  We have little communities. Yeah. Yeah, I think so. That seems to be
*  the, that seems to be how it's going right now. And I don't see that trend really reversing.
*  I think people are diverse and they're able to choose their own path and existence. And I
*  celebrate that. And so- Will you spend so much time in the metaverse,
*  in the virtual reality? Which community are you? Are you the physicalist, the physical reality
*  enjoyer or do you see drawing a lot of pleasure and fulfillment in the digital world?
*  Yeah, I think currently the virtual reality is not that compelling. I do think it can improve a lot,
*  but I don't really know to what extent. Maybe there's actually even more exotic things you
*  can think about with Neuralynx or stuff like that. So currently I see myself as mostly a team
*  human person. I love nature. I love harmony. I love people. I love humanity. I love emotions
*  of humanity. And I just want to be in this solar punk little utopia. That's my happy place.
*  My happy place is people I love thinking about cool problems surrounded by a lush,
*  beautiful, dynamic nature and secretly high tech in places that count.
*  Places that count. So you use technology to empower that love for other humans and nature.
*  Yeah, I think technology is used very sparingly. I don't love when it gets in the way of humanity
*  in many ways. I like just people being humans in a way we slightly evolved and prefer, I think,
*  just by default. People kept asking me because they know you love reading. Are there particular
*  books that you enjoyed that had an impact on you for silly or for profound reasons that you
*  recommend? You mentioned the Vital Question. Many, of course. I think in biology as an example,
*  the Vital Question is a good one. Anything by Nic Lane, really life ascending, I would say,
*  is a bit more potentially representative as a summary of a lot of the things he's been talking
*  about. I was very impacted by The Selfish Gene. I thought that was a really good book that helped me
*  understand altruism as an example and where it comes from and just realizing that the selection
*  is on the level of genes was a huge insight for me at the time. And it cleared up a lot of things
*  for me. What do you think about the idea that ideas are the organisms, the means?
*  Love it. 100%.
*  Are you able to walk around with that notion for a while that there is an evolutionary kind of
*  process with ideas as well? There absolutely is. There's memes just like genes and they compete
*  and they live in our brains. It's beautiful. Are we silly humans thinking that we're the
*  organisms? Is it possible that the primary organisms are the ideas?
*  Yeah, I would say the ideas kind of live in the software of our civilization in the minds and so
*  on. We think as humans that the hardware is the fundamental thing. I, human, is a hardware entity,
*  but it could be the software, right? Yeah. I would say there needs to be some grounding
*  at some point to a physical reality. Yeah, but if we clone an Andre,
*  the software is the thing that makes that thing special, right?
*  Yeah, I guess you're right. But then cloning might be exceptionally difficult. There might
*  be a deep integration between the software and the hardware in ways we don't quite understand.
*  Well, from the evolutionary point of view, what makes me special is more like the gang of genes
*  that are writing in my chromosomes, I suppose. They're the replicating unit, I suppose.
*  No, but that's just the thing that makes you special. Sure. Well, the reality is,
*  what makes you special is your ability to survive based on the software that runs on the hardware
*  that was built by the genes. So the software is the thing that makes you survive, not the hardware.
*  It's a little bit of both. It's just like a second layer. It's a new second layer that hasn't been
*  there before the brain. They both coexist. But there's also layers of the software.
*  So abstraction on top of abstractions. Okay, so Selfish Gene and Nick Lane. I would say sometimes
*  books are not sufficient. I like to reach for textbooks sometimes. I feel like books are for
*  too much of a general consumption sometime, and they're too high up in the level of abstraction,
*  and it's not good enough. So I like textbooks. I like The Cell. I think The Cell was pretty cool.
*  That's why also I like the writing of Nick Lane is because he's pretty willing to step one level
*  down, and he's willing to go there. But he's also willing to be throughout the stack. So he'll go
*  down to a lot of detail, but then he will come back up. And I think he has a... Yeah, basically,
*  I really appreciate that. That's why I love college, early college, even high school.
*  Just textbooks on the basics of computer science, of mathematics, of biology, of chemistry.
*  They condense down. It's sufficiently general that you can understand both the philosophy
*  and the details, but also you get homework problems, and you get to play with it as much
*  as you would if you were in programming stuff. Yeah. And then I'm also suspicious of textbooks,
*  honestly, because as an example in deep learning, there's no amazing textbooks,
*  and the field is changing very quickly. I imagine the same is true in, say, synthetic biology and
*  so on. These books like The Cell are kind of outdated. They're still high level. What is the
*  actual real source of truth? It's people in wet labs working with cells, sequencing genomes, and
*  actually working with it. And I don't have that much exposure to that or what that looks like.
*  So I still don't fully... I'm reading through The Cell, and it's kind of interesting, and I'm
*  learning, but it's still not sufficient, I would say, in terms of understanding.
*  Well, it's a clean summarization of the mainstream narrative.
*  But you have to learn that before you break out towards the cutting edge.
*  Yeah. What is the actual process of working with these cells and growing them and incubating them?
*  And it's kind of like a massive cooking recipe, so making sure your cells live and proliferate,
*  and then you're sequencing them, running experiments, and just how that works, I think,
*  is kind of like the source of truth of, at the end of the day, what's really useful in terms of
*  creating therapies and so on. Yeah. I wonder what in the future AI textbooks will be,
*  because there's artificial intelligence, the modern approach. I actually haven't read,
*  if it's come out, the recent version, there's been a recent edition. I also saw there's a
*  Science of Deep Learning book. I'm waiting for textbooks that are worth recommending, worth
*  reading. It's tricky, because it's like papers and code, code, code. Honestly, I find papers
*  are quite good. I especially like the appendix of any paper as well. It's like the most detailed
*  you can have. It doesn't have to be cohesive connected to anything else. You just described
*  me a very specific way you saw the particular thing. Yeah. Many times, papers can be actually
*  quite readable, not always, but sometimes the introduction and the abstract is readable,
*  even for someone outside of the field. This is not always true. And sometimes, I think,
*  unfortunately, scientists use complex terms, even when it's not necessary. I think that's harmful.
*  I think there's no reason for that. And papers sometimes are longer than they need to be in the
*  parts that don't matter. Appendix would be long, but then the papers, look at Einstein, make it
*  simple. Yeah. But certainly, I've come across papers, I would say, in synthetic biology or
*  something that I thought were quite readable for the abstract and the introduction. And then you're
*  reading the rest of it, and you don't fully understand, but you are getting a gist, and I
*  think it's cool. What advice, you give advice to folks interested in machine learning and research,
*  but in general, life advice to a young person, high school, early college, about how to have a
*  career they can be proud of or a life they can be proud of. Yeah, I think I'm very hesitant to give
*  general advice. I think it's really hard. I've mentioned, like some of the stuff I've mentioned
*  is fairly general, I think, like focus on just the amount of work you're spending on a thing.
*  Compare yourself only to yourself, not to others. That's good. I think those are fairly general.
*  How do you pick the thing? You just have a deep interest in something.
*  Try to find the argmax over the things that you're interested in.
*  Argmax at that moment and stick with it. How do you not get distracted and switch to another thing?
*  You can, if you like.
*  Well, if you do an argmax repeatedly every week, every month.
*  It doesn't converge.
*  It's a problem.
*  Yeah, you can low pass filter yourself in terms of what has consistently been true for you.
*  But yeah, I definitely see how it can be hard, but I would say you're going to work the hardest on
*  the thing that you care about the most. So low pass filter yourself and really introspect.
*  In your past, what are the things that gave you energy and what are the things that took
*  energy away from you? Concrete examples. Usually from those concrete examples,
*  sometimes patterns can emerge. I like it when things look like this when I'm in these positions.
*  That's not necessarily the field, but the kind of stuff you're doing in a particular field. So for
*  you, it seems like you were energized by implementing stuff, building actual things.
*  Being low level learning and then also communicating so that others can go through
*  the same realizations and shortening that gap. Because I usually have to do way too much work
*  to understand a thing. And then I'm like, okay, this is actually like, okay, I think I get it.
*  And why was it so much work? It should have been much less work. And that gives me a lot
*  of frustration. And that's why I sometimes go teach. So aside from the teaching you're doing
*  now, putting out videos, aside from a potential Godfather part two, with the AGI at Tesla and
*  beyond, what does the future of Ranjha Kapothi hold? Have you figured that out yet or no?
*  I mean, as you see through the fog of war, that is all of our future. Do you start seeing silhouettes
*  of what that possible future could look like? The consistent thing I've been always interested in,
*  for me at least, is AI. And that's probably what I'm spending the rest of my life on,
*  because I just care about it a lot. And I actually care about many other problems as well,
*  like say aging, which I basically view as disease. And I care about that as well, but I don't think
*  it's a good idea to go after it specifically. I don't actually think that humans will be able to
*  come up with the answer. I think the correct thing to do is to ignore those problems and you solve
*  AI and then use that to solve everything else. And I think there's a chance that this will work.
*  I think it's a very high chance. And that's kind of like the way I'm betting at least.
*  So when you think about AI, are you interested in all kinds of applications, all kinds of domains,
*  and any domain you focus on will allow you to get insights to the big problem of AGI?
*  Yeah, for me, it's the ultimate meta problem. I don't want to work on any one specific problem.
*  There's too many problems. So how can you work on all problems simultaneously? You solve the meta
*  problem, which to me is just intelligence and how do you automate it?
*  Is there cool small projects like Archive Sanity and so on that you're thinking about,
*  that the world, the ML world can anticipate?
*  There's always some fun side projects. Archive Sanity is one. Basically, there's way too many
*  archive papers. How can I organize it and recommend papers and so on? I transcribed all of your
*  podcasts. What did you learn from that experience, from transcribing the process of like you like
*  consuming audio books and podcasts and so on? Here's the process that achieves closer to human
*  level performance and annotation. Yeah. Well, I definitely was surprised that transcription
*  with OpenEye's Whisper was working so well compared to what I'm familiar with from Siri and
*  a few other systems, I guess. It works so well. And that's what gave me some energy to try it
*  out. And I thought it could be fun to run on podcasts. It's kind of not obvious to me why
*  Whisper is so much better compared to anything else, because I feel like there should be a lot
*  of incentive for a lot of companies to produce transcription systems and that they've done so
*  over a long time. Whisper is not a super exotic model. It's a transformer. It takes smell
*  spectrograms and just outputs tokens of text. It's not crazy. The model and everything has
*  been around for a long time. I'm not actually 100% sure why this game model works.
*  It's not obvious to me either. It makes me feel like I'm missing something.
*  I'm missing something. Yeah. Because there is a huge, even at Google and so on, YouTube
*  transcription. Yeah. Yeah, it's unclear. But some of it is also integrating into a bigger system
*  that is so the user interface, how it's deployed and all that kind of stuff. Maybe
*  running it as an independent thing is much easier, like an order of magnitude easier than deploying
*  to a large integrated system like YouTube transcription or anything like meetings.
*  Zoom has transcription that's kind of crappy, but creating an interface where it detects the
*  different individual speakers, it's able to display it in compelling ways, run it in real time,
*  all that kind of stuff. Maybe that's difficult. That's the only explanation I have because
*  I'm currently paying quite a bit for human transcription and human caption annotation.
*  It seems like there's a huge incentive to automate that. Yeah. It's very confusing.
*  I think, I mean, I don't know if you looked at some of the whisper transcripts, but they're
*  quite good. They're good. And especially in tricky cases. I've seen whisper's performance on super
*  tricky cases and it does incredibly well. So I don't know. A podcast is pretty simple. It's like
*  high quality audio and you're speaking usually pretty clearly. And so I don't know what OpenAI's
*  plans are either. But yeah, there's always fun projects basically. And stable diffusion also
*  is opening up a huge amount of experimentation, I would say in the visual realm and generating
*  images and videos and movies. Yeah, videos now. And so that's going to be pretty crazy.
*  That's going to almost certainly work and is going to be really interesting when the
*  cost of content creation is going to fall to zero. You used to need a painter for a few months to
*  paint a thing and now it's going to be speak to your phone to get your video. So Hollywood will
*  start using that to generate scenes, which completely opens up. Yeah. So you can make a
*  movie like Avatar eventually for under a million dollars. Much less. Maybe just by talking to your
*  phone. I mean, I know it sounds kind of crazy. And then there'd be some voting mechanism. Like
*  how do you have a net? Would there be a show on Netflix that's generated completely
*  automatically? Yeah, potentially. Yeah. And what does it look like also when you can just generate
*  it on demand and there's infinity of it. Yeah. Oh man. All the synthetic content. I mean, it's
*  humbling because we treat ourselves as special for being able to generate art and ideas and all
*  that kind of stuff. If that can be done in an automated way by AI. Yeah. I think it's fascinating
*  to me how these, the predictions of AI and what it's going to look like and what it's going to be
*  capable of are completely inverted and wrong. And a sci-fi of 50s and 60s was just like totally
*  not right. They imagined AI as like super calculating theory approvers and we're getting
*  things that can talk to you about emotions. They can do art. It's just like weird. Are you
*  excited about that future? Just AI's like hybrid systems, heterogeneous systems of humans and AI's
*  talking about emotions, Netflix and children and AI system. Where the Netflix thing you watch is
*  also generated by AI. I think it's going to be interesting for sure. And I think I'm cautiously
*  optimistic, but it's not obvious. Well, the sad thing is your brain and mine developed in a time
*  where before Twitter, before the internet. So I wonder people that are born inside of it might
*  have a different experience. Like I, maybe you can still resist it and the people born now will not.
*  Well, I do feel like humans are extremely malleable. Yeah. And you're probably right.
*  What is the meaning of life, Andre? We talked about sort of the universe having a conversation
*  with us humans or with the systems we create to try to answer for the universe, for the creator
*  of the universe to notice us. We're trying to create systems that are loud enough to answer back.
*  I don't know if that's the meaning of life. That's like meaning of life for some people.
*  The first level answer I would say is anyone can choose their own meaning of life because we are
*  conscious entity and it's beautiful, number one. But I do think that a deeper meaning of life as
*  someone is interested is along the lines of what the hell is all this and why? And if you look at
*  the inter-fundamental physics and the quantum field theory and the standard model, they're very
*  complicated. And there's this 19 free parameters of our universe and what's going on with all this
*  stuff. And why is it here? And can I hack it? Can I work with it? Is there a message for me? Am
*  I supposed to create a message? And so I think there's some fundamental answers there. But I
*  think there's actually even like, you can't actually really make dent in those without more time.
*  And so to me also, there's a big question around just getting more time, honestly.
*  Yeah, that's kind of like what I think about quite a bit as well.
*  So kind of the ultimate, or at least first way to sneak up to the why question is to try to escape
*  the system, the universe. And then for that, you sort of backtrack and say, okay, for that,
*  that's going to take a very long time. So the why question boils down from an engineering perspective
*  to how do we extend? Yeah, I think that's the question number one, practically speaking,
*  because you can't, you're not going to calculate the answer to the deeper questions in time you
*  have. And that could be extending your own lifetime or extending just the lifetime of human
*  civilization. Of whoever wants to not many people might not want that. But I think people who do
*  want that, I think, I think it's probably possible. And I don't think I don't know that people
*  fully realize this, I kind of feel like people think of death as an inevitability. But at the
*  end of the day, this is a physical system, some things go wrong. It makes sense why things like
*  this happen, evolutionary speaking. And there's most certainly interventions that that mitigate
*  it. That'd be interesting if death is eventually looked at as, as a fascinating thing that used to
*  happen to humans. I don't think it's unlikely. I think it's I think it's likely. And it's up to
*  our imagination to try to predict what the world without death looks like. Yeah, it's hard to,
*  I think the values will completely change. Could be. I don't I don't really buy all these ideas
*  that, oh, without death, there's no meaning, there's nothing as I don't intuitively buy all
*  those arguments. I think there's plenty of meaning, plenty of things to learn. They're interesting,
*  exciting. I want to know I want to calculate. I want to improve the condition of all the humans
*  and organisms that are alive. Yeah, the way we find meaning might change. We there is a lot of
*  humans probably including myself that finds meaning in the finiteness of things. But that doesn't mean
*  that's the only source of meaning. Yeah, I do think many people will will go with that, which
*  I think is great. I love the idea that people can just choose their own adventure. Like you
*  you are born as a conscious free entity, by default, I'd like to think and you have your
*  unalienable rights for life in the pursuit of happiness. I don't know if you have that
*  in the nature, the landscape of happiness, you can choose your own adventure mostly.
*  And that's not fully true. But I still am pretty sure I'm an NPC. But an NPC can't know it's an NPC.
*  There could be different degrees and levels of consciousness. I don't think there's a more
*  beautiful way to end it. Andre, you're an incredible person. I'm really honored you
*  would talk with me. Everything you've done for the machine learning world, for the AI world,
*  just to inspire people to educate millions of people has been it's been great. And I can't wait
*  to see what you do next. It's been an honor, man. Thank you so much for talking today. Awesome.
*  Thank you. Thanks for listening to this conversation with Andre Karpathy. To support this podcast,
*  please check out our sponsors in the description. And now let me leave you with some words from
*  Samuel Carlin. The purpose of models is not to fit the data, but to sharpen the questions.
*  Thanks for listening and hope to see you next time.
