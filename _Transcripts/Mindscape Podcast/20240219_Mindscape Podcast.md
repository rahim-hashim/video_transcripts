---
Date Generated: June 07, 2024
Transcription Model: whisper medium 20231117
Length: 4820s
Video Keywords: []
Video Views: 12095
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2024/02/19/266-christoph-adami-on-how-information-makes-sense-of-biology/

Evolution is sometimes described -- not precisely, but with some justification -- as being about the "survival of the fittest." But that idea doesn't work unless there is some way for one generation to pass down information about how best to survive. We now know that such information is passed down in a variety of ways: through our inherited genome, through epigenetic factors, and of course through cultural transmission. Chris Adami suggests that we update Dobzhansky's maxim "Nothing in biology makes sense except in the light of evolution" to "... except in the light of information." We talk about information theory as a subject in its own right, and how it helps us to understand organisms, evolution, and the origin of life.

Christoph Adami received his Ph.D. in physics from Stony Brook University. He is currently professor of Microbiology and Molecular Genetics as well as Physics and Astronomy at Michigan State University. Among his awards are the NASA Exceptional Achievement Medal and the Lifetime Achievement Award from the International Society for Artificial Life. His new book is The Evolution of Biological Information: How Evolution Creates Complexity, from Viruses to Brains.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 266 | Christoph Adami on How Information Makes Sense of Biology
**Mindscape Podcast:** [February 19, 2024](https://www.youtube.com/watch?v=4PCHelnFKGc)
*  Hello everyone, welcome to the Mindscape podcast. I'm your host, Sean Carroll.
*  Longtime listeners will know that I've long been a fan of Las Vegas. I like to
*  go to Vegas, play poker, eat, shop, whatever, just relax and have a good time.
*  Haven't been able to do it quite as much now that we're on the East Coast. That's
*  okay, there's always pluses and minuses. Now we can go to New York. It's like the
*  Las Vegas of the East. But anyway, one of the reasons why I like Las Vegas is in
*  addition to the stereotypes. So the stereotypes are absolutely there, right?
*  There are long rows of slot machines with dull-eyed people mindlessly
*  pressing buttons hoping to get rich someday. It's kind of depressing, that
*  part. But there's a lot of weird stuff in Vegas if you look closely enough. So by
*  Vegas standards, one of the weird things that I really like is there's an outpost
*  of Bauman Rare Books. This is a well-known rare book store with headquarters
*  in New York, but they have a Vegas store in the Palazzo Hotel Casino where I used
*  to stay sometimes. And it's just weird among all the glitz and glamour, here's
*  rare books, and they actually have a lot of first editions of things, but also
*  some weird science-y books. They have a signed Albert Einstein, for example. And I
*  was very amused to see in Bauman's rare books in Vegas a copy of Claude Shannon's
*  master's thesis. Claude Shannon, famous 20th century scientist for many reasons,
*  and his master's thesis, I didn't actually know this before I saw it in the
*  bookstore, is very famous. It's been called by Howard Gardner the most
*  influential master's thesis of all 20th century science. This is a master's
*  thesis that has its own Wikipedia page, okay, and it's about basically using
*  Boolean analysis to model and improve the efficiency of circuits and things
*  like that. Pretty awesome for a master's thesis kind of thing, but for my purposes
*  today I'm just using this as a somewhat strained segue into, of course, Claude
*  Shannon's big contribution, even bigger than the master's thesis, came ten years
*  after when he essentially invented information theory. He wrote a paper
*  called the mathematical theory of communication, and like many great
*  scientific breakthroughs, theoretical breakthroughs, this was driven by a
*  down-to-earth technological practical need. Shannon was interested in sending
*  signals across the Atlantic Ocean in wires, and you want to send a signal in a
*  way that is efficient, right, that is least likely to be garbled or to lose
*  the information, and to do that, to figure out how to do that, you need to have a
*  mathematical way of characterizing what you mean by information, and it turns out
*  as he discovered by doing the math that it's very very similar to the formula
*  for entropy in statistical mechanics. So there was clearly some interesting
*  hidden relationship here between information and communication on the
*  one side and statistical mechanics and thermodynamics on the other side, and of
*  course, so this is the middle of the century, 1948, this idea has blossomed
*  quite a bit. You hear about information all the time, you hear about it in the
*  political arena, right, misinformation, disinformation, you hear about it in
*  technology, remember the information superhighway, that was a big thing, and
*  you must have heard that information as a concept is useful in biology, in
*  neuroscience, quantum mechanics, quantum information, and so on. So today on the
*  podcast, we have Christophe Adami, who is, like many Mindscape guests, he started
*  out his career as a relatively traditional physicist doing nuclear and
*  particle physics, and now he's a professor at Michigan State, not only in
*  physics, but also in, I think, molecular biology department, but he studies
*  evolution and life, including artificial life, and he has a new book out called
*  The Evolution of Biological Information, How Evolution Creates Complexity from
*  Viruses to Brains. So I'm gonna use this as an excuse to really get clear on what
*  is this information theory stuff. I mean, by the way, the book is a little
*  technical, I'm not gonna advocate it for people who don't like equations, there
*  are some equations there, but the equations are quite mild, you know, if
*  you're the kind of person who doesn't read equations every day, but doesn't
*  blanch when you see one, it might be a good book to pick up. And we're gonna
*  talk about what information theory is in general, and specifically how
*  biologists, or people who care about biology, even if they're physicists, are
*  gonna use information theory to better understand things like evolution and
*  even the origin of life. I would say that 75 years later, the idea of information
*  theory we got from Claude Shannon is still not settled in, you know, we're
*  still working through the basic implications of it, so it's very exciting,
*  it's fun, it's a new lens with which to look at the world in a detailed way. And
*  you know, that's all we like to do here at the Mindscape Podcast, so let's go.
*  Chris Adami, welcome to the Mindscape Podcast. Glad to be here. You know, let's
*  start with this idea of information theory. It's always gonna be a challenge
*  when you have an idea like information theory that uses a natural language word
*  that people are familiar with, right? Information, they think they know what
*  information is, but now we have math behind it. We've talked about information
*  theory a lot on the podcast without ever just taking a breath and saying what it
*  is. So do you have a best way, favorite way of explaining information theory to
*  the person on the street? I do. It's actually strange that in this case, the
*  mathematical understanding of the word information is actually very similar or
*  very close to our understanding, generally speaking, in our normal, you
*  know, everyday usage. So to really define information mathematically or even in
*  words, we can just say that information is that which allows someone who has
*  that information to make predictions with accuracy better than chance, right?
*  So there's a system that I know something about it, and then that means I
*  can actually predict some of its states. For example, you know, where I can find
*  coffee with accuracy better than chance. If I would just randomly go somewhere,
*  well, I would most likely not end up in a coffee place. But if I have information,
*  that means I can actually say, hey, I have to go to this particular place. And
*  that's how we understand it normally in our everyday language. And it is also
*  exactly how it is defined mathematically. Mathematically, information is that which
*  is used to make predictions, but it has to be better than chance to be information.
*  Otherwise, it's just a guess. Right. And so because making predictions with
*  accuracy better than chance is really powerful, that means it's also powerful
*  in biology. But of course, it's also powerful, let's say, in the stock market.
*  If I have inside information, I can get rich using information because I can make
*  predictions about, for example, the stock price with accuracy better than chance.
*  Right. And Shannon, when he defined this concept in 1948, he defined it precisely
*  that way, even though he didn't use exactly those words. And as a consequence,
*  there's a lot of misunderstanding about what information really is. It's often
*  confounded with entropy, which is in a sense the absolute opposite of information,
*  namely, it is about what we don't know. Right. And so if you then confound
*  information and entropy, then you're going to get a lot of misunderstandings.
*  But didn't I completely agree with you, by the way, but didn't Shannon himself do that?
*  I mean, didn't didn't he use the word information like maximal information for him
*  in a code or an alphabet is maximum entropy, right? When every symbol is equally likely.
*  You are right. He has done that. I should say not so much in his original article, but you know,
*  there was a book written or co-written by I forget, it's Shannon and McMillan or something,
*  Shannon and Weaver, in particular in the book Shannon and Weaver, the words entropy and
*  information get mixed up and I have a suspicion that this was mostly Weaver doing that. I would
*  have to actually look at the original article if Shannon himself does that, because in a sense,
*  you know, he should know better. You know, I just because I saw so much of the confounding between
*  entropy information, I felt compelled to just simply write an article called What is information,
*  which is main purpose was to say, hey, guys, you know, you have to be careful. One is not the other.
*  Now, that's great. And I do sometimes wonder, you know, I agree with everything you just said,
*  and I wonder if it's just my physics training, because to me, thinking like Boltzmann would have
*  thought a low entropy state, if you tell me that you're in a low entry macrostate, all the molecules
*  are in one corner of the room, you've given me a lot of information, right? Low entropy is a lot
*  of information. And that makes perfect sense to me. That's right. Low entropy is a lot of information.
*  You can think of information as simply a difference between two entropies, namely the
*  maximum entropy in the actual entropy. Okay, good. So that's why when your actual entropy is low,
*  then your information is high because it's this difference. And the fact that it's a difference,
*  by the way, is a fundamentally important thing, namely, entropy itself, in a sense, has no real
*  meaning or existence, just like energy doesn't have in physics, only differences of entropy have
*  a meaning, just like in physics, only differences between energies have any real-life effect.
*  And so the fact that it's a difference is important, but it's important that the first term
*  is a maximum entropy, like how much there is to know about the system. And if you forget about that,
*  then your information is just minus entropy, or what a bunch of people have called negentropy,
*  right? Which is nonsense. It's forgetting the first term, which is the maximum entropy,
*  so that this thing, which is information, is always positive. So basically, in this way of
*  talking, you would say, when I have some configuration and I have some statistical
*  knowledge about it, I can divide the state into sort of the entropy part, which I don't understand
*  very well, and the information part, which specifies something. Right. Or very simply speaking,
*  the, you can, for every system, write down or understand what is the maximum uncertainty
*  that you have. It's just really counting the number of degrees of freedom that there are,
*  and then taking the log of that. Right. And then you ask yourself, well, how much entropy do I
*  actually have? In other words, do I have a probability distribution that is different
*  than the maximum entropy distribution? And if the answer is yes, then that means already you know
*  something. That means that the actual distribution has a lower entropy, and then you have some
*  information. However, you may not know at that point exactly what this information is about.
*  Okay. In a gas, of course, very often you do, just like you said, when you have a bunch of
*  molecules in a corner, well, then you have information about where these molecules are.
*  Of course, if you allow the molecules to disappear or to sort of like do their thing,
*  what happens is that your knowledge about the positions of the molecule starts decreasing.
*  And at the same time, of course, your end, the actual entropy starts increasing. Right. That is
*  what we call the second law of thermodynamics. It's literally just the loss of information
*  that you have. And of course, during that equilibration phase, the system is returning
*  to its equilibrium, but it's actually at disequilibrium. So in other words, whenever you
*  have information, it gives you a hint that the system is not at equilibrium. It is away from
*  equilibrium. And the amount of information is in fact characterizing how far away from equilibrium
*  you are. So when I'm speaking to you right now, you're actually in an ordered state, a very ordered
*  state as far as the molecules are concerned. And I can tell you in a sense how much ordered state
*  there is. It's about half a million bits. Okay. Why? Because in fact, that is the amount of
*  information that's actually stored in your genome. Ah, okay. This is probably going to be
*  leaping ahead. But what about like the particular configuration of my body? Certainly that is more
*  than half a million bits. That's a good question. But since in fact, that organization is done by
*  the half a million bits, my suspicion is that in fact, that must be the same because how else would
*  you achieve this ordered state? So this is actually an interesting question. I would have
*  to sit down and think a little bit. My intuition is that even though it seems that, you know,
*  that would be more than half a million bits, that in fact it is not. However, it's such a good
*  question that I cannot actually tell you right now why. Good final exam question for the next time
*  you teach a course based on your book. Yeah, that's actually a good point. I mean, if I,
*  you know, after this interview, I'll try to sit down and figure this out. Okay, that's a good one.
*  And it's simply because the information cannot be anywhere else. You know, the fact that you
*  ordered, the only thing that makes that possible is the information in your genome. And as a
*  consequence, in a sense, mathematically, it has to be like that, even though, just like you said,
*  that seems low. It does seem low. I like to think I convey more information there. I mean, certainly
*  in my brain, there are neurons with certain weights and things like that. And
*  there's probably more than half a million. Right. Okay. So now you're making another point. Of
*  course, there's information that you have acquired during your lifetime that is not being counted.
*  That is definitely there. Good. However, if you take, let's say a brain,
*  let's say a baby brain, physically speaking, of course, there are differences. Yeah, but I mean,
*  like the information is stored in the weights of the neurons in the brain in some way. So definitely
*  that is in addition, right? However, that of course does not give you your physical appearance.
*  It doesn't change the organization of the rest of your body. It's an interesting train of thought.
*  Either a final exam question or a paper to be written here, I think, about this. How many bits
*  am I? But okay, something very interesting and important happened just now in your discussion of
*  information, because I think that if you asked people on the street, do you have information
*  about where your car keys are? They would think about that as a yes-no question. I know where they
*  are or I don't. And you've sneaked in the information that you have, and you've got the
*  question, I know where they are or I don't. And you've sneaked in the idea of a probability
*  distribution, which is kind of central here. Right. So how does that come in? Like, how central is
*  probability to information theory? Well, actually, it is the central aspect of it. So before you can
*  really understand information theory, you should have a very basic course in probability and
*  statistics. Now, to tell you the truth, not everybody who's working in the field did have
*  that. And that shows. But simply because the concept of probability actually, to fully understand it,
*  is it's not as simple as just writing down, you know, P sub i or some distribution, you know,
*  what a probability is. And I know you're familiar with this, because you've thought about this in
*  context of quantum mechanics for a long time, is, you know, not immediately trivial. Some people
*  think, oh, a probability exists by itself. Other people say, no, a probability is just simply
*  something that you can estimate, but that in itself, in a sense, really doesn't exist.
*  But the idea of prediction, of course, is central to that. So when you're asking yourself,
*  can I predict with accuracy better than chance? Then you have to, in a sense, have an idea of,
*  well, what is chance, the chance prediction here? And for that, in a sense, you need a prior,
*  you need an assumption about what is expected, right? And so if you're going to talk about
*  a probability distribution, then you're really talking about what am I expecting? So let's go
*  to the example of the car keys, right? So generally speaking, we could say, okay, here's a person who's
*  looking for their car keys. They know with 90% of the chance from past experience, right, we're
*  setting up the priors now, from past experience, 90% of the time, it's in my pocket. Right. But
*  if it's not in my pocket, it could be in 10 different places. Yeah. Right. If that is the case,
*  you can set up, just set up the probability distribution for you. Because that means that
*  there are 11 possible places that the keys could be in. Right. And the chance to find it in your
*  pocket is 10%. Sorry, 90%. And then in each of the 10 other places, the chance to find it is one out
*  of 100. Right. Yeah. So now I've set the expectation before I've done any experiment, right? Now I'm
*  doing an experiment. And of course, what experiment are you going to be doing? You're going to check
*  your pocket first. Yes. Right. Right. And now what happens is that this measurement is going to give
*  you information. Right. And in fact, we call this, you know, this outcome of this measurement, it's
*  called a specific information. Okay. It's specific information, because I can do I can do 11
*  measurements. And the average of the outcomes of that, that's actually the information gained from,
*  from the measurement of the locations. The interesting thing here is that if I don't find
*  the key in my pocket, then I have a problem. Now it could be in 10 different places. So it turns out
*  that the specific information of this measurement, namely that the key is not in your pocket is
*  negative. Yeah, it's a negative specific information, even though the average information
*  gained from the car keys searching measurement is still positive, because you're now less sure of
*  where the keys are than exactly exactly. So it's intuitive declares it's like, oh my god, it's like,
*  I thought I knew, see, that's the thing I thought I knew means that's the priors from the priors,
*  you had a pretty good idea, then you make your measurement and you go like, oh my god, now I
*  don't know anything. And this is mathematically in fact, it's an exercise in my book in chapter
*  three. Very good. And let me just raise again, I'm super on your side, but it's my job to, you know,
*  play the devil's advocate sometimes. People worry about this way of thinking about information,
*  because it sounds a little subjective. It's not out there in the world, you're talking about
*  information as an ability for some agent to make predictions, right? Is it truly objective? Or is
*  it only relative to the capacities of some thinking being? So, so you're asking, of course, the most
*  important question about information. And the answer is information is contextual, always,
*  it is never absolute. And now I'm going to give you a great example that will get you, you know,
*  to think about this. Suppose you are a virus, and you are in fact reaching wreaking havoc inside of
*  a patient, right? You are replicating fast, everything is going good for you. Right? Let's
*  imagine your mutation rate is actually kind of low. So you don't change much while so the information
*  that you have about doing your job is doing its job. Right? Now the patient takes an antiviral,
*  right? It takes the patient takes an antiviral, and suddenly this virus goes like, man,
*  you know, this replicating thing is now really, really, really hard. Right? And what you can now
*  do is you can calculate the information about how to do this job. And it has changed dramatically.
*  In fact, now the virus does not have this amount of information about doing its job anymore.
*  And you're going to have but the sequence is the same. How can a sequence is the same?
*  Earlier have lots of information, and then have very little information. The answer is because
*  the context changed, because that what you have information about has changed. So what was the
*  environment yesterday isn't the environment today, you have information about yesterday's world,
*  not about today's world. And that is the important thing. Information is completely
*  contextual, the same sequence evaluated in different environments will have different
*  information and therefore different meaning. A lot of time people think that, oh, information
*  theory can't deal with meaning. It's absolutely untrue. My molecular sequence means something
*  here on earth, actually, you know, above the surface of the water, for example, you put me
*  underwater and my sequence is making wrong predictions, right? Namely about how to breathe.
*  No underwater, that thing doesn't work. Your fitness is zero. I will have zero offspring
*  underwater unless I actually, you know, am in a submarine or something like that where I'm taking
*  the environment with me. Right. Then I could still have information. So very, you know,
*  very nearly so in biology, information and fitness are exchangeable. You have high information about
*  how to do something, how to survive in the environment means having high fitness. They are
*  related. In fact, they are mathematically related and we don't have to talk about what that
*  relationship is, but you can read about it in my book. So in other words, what happened in evolution
*  is that fitness and information are essentially intertwined. They are almost the same thing.
*  The way you are increasing your fitness is you're increasing the information about how to live in
*  that environment. I guess I was trying to make a similar point to what you just said in my book,
*  The Big Picture. I mentioned the Voynich manuscript, right? This wonderful old book full of symbols and
*  nobody knows whether it's nonsense or whether it refers to something. And so I asked the question,
*  how much information is there in the Voynich manuscript? How would you answer this?
*  Manuscript. How would you answer that question?
*  The answer is unless we know what the information is about, this is entropy for us.
*  So if you have text or any data, that is not information. In fact, it is literally just
*  entropy in the sense that you are talking about, oh, it represents an example out of another
*  similar set of things. And so you're setting up your hypothetical ensemble so that you can talk
*  about entropy. The moment that you know what things you can predict with it, then it becomes
*  information. If you do not know this, the same piece of information or the same text, should I
*  say, the same symbolic sequence would just be entropy to you. In other words, just to repeat
*  it, because information is that which allows you to make predictions about a particular system with
*  accuracy better than chance. If you don't know what this is, it's not information. Another example
*  is somebody hands you a subway chart, and he goes, well, that's fantastic, except I don't know
*  which city this is. Well, then it's useless to you. So in other words, useless information is entropy.
*  Got it. The other idea at the technical level that I have found super important in my tiny
*  little forays in information theory is mutual information. I love this concept, and it never
*  gets explained in a popular level. So maybe you can give us a shot. Right. So first of all,
*  information is really a mutual entropy. It's a shared entropy. So in other words, the reason
*  why me, if I have information, can make predictions about another system is because
*  in a sense, we have certain correlations. We know something about each other. Right. And so information,
*  even though I showed you earlier that it's really a difference of entropies, you can also think of
*  it as a shared entropy. The mathematics to show that this is one and the same thing,
*  we're not going to go into. But just trust me here that, you know, if you think about a Venn diagram
*  about a system and the one who's trying to measure the system, the intersection of that Venn diagram,
*  that's the information that the measurement device has about the system. Right. That's a shared
*  entropy. That shared entropy is, of course, the information. So when people say mutual information,
*  they meaning mutual, mutual entropy. In fact, nobody should be using that word. Okay. Like in
*  my book, for example, when, you know, I have like an index where it says mutual information, I say
*  C information. Because, you know, they are enough, you know, but it's just for the reason that we
*  talked about earlier that people are using information and entropies anonymously. They have
*  taken mutual entropy, which is an information and call that mutual information. Right. But in
*  principle, they're one and the same thing. We just should call it information. It is that,
*  you know, that correlates the two systems. Because remember, we always have to talk about two systems
*  when we are talking about information, one that makes the prediction and one that is being
*  predicted. Right. Right. And what is shared, the shared correlation between them, you know,
*  in other words, what's not random between them. That is information. Good. So now we have a
*  pretty firm grounding on information theory. We can move on to applying it to biology, which is
*  what your book is all about. But let me, let me just first ask the background question.
*  How popular in biology is this task of thinking about things in terms of information theory? Is
*  it, is it everyone does it or no one does it, or it is the new hotness and it's sweeping the field?
*  Let me put it this way. If this was something that everybody does, I wouldn't have had to write this
*  book. Okay, good. This book really came out of a frustration that I have this tool, I see how
*  valuable it is to understand essentially anything in biology and nobody's using it. When I say
*  nobody, that's not quite true. There are a few people who do. Bill Bialik in Princeton, for example,
*  has certainly done this and he does know how to do this. There's a few people, often in fact,
*  in Bialik's orbit, who have looked at information transmission in cells, for example, in gene
*  regulation and calculated the channel capacity of a cellular communication channel and did this
*  very well. And I in fact have these examples in my book, but it is woefully underrepresented.
*  There is something about information theory that presents a barrier, a hurdle to, in a sense, to
*  acceptance. I only have a vague memory of when I first learned about information theory. It was,
*  in fact, at Caltech when a postdoc that was placed into my office actually first started explaining
*  classical information theory to me because we were actually working in quantum information.
*  And it was like, well, let's do the classical theory first. And I remember when he was first
*  writing these formulas on the board, which has these vertical bars and colons and semi-colons,
*  thinking like, what is this? This is not my mathematics. My mathematics, there's integrals,
*  there's differentials, there are matrices. And now I'm seeing these weird symbols and my brain
*  doesn't really understand them. In a sense, from the cognitive science perspective, is you don't
*  have these representations that allow you to recognize these things and they have to build
*  over time. And I think this barrier that I felt at the time and was like, oh, there's all these
*  different entropies. There's a mutual, there's a shared, the conditional. And you're like, how am
*  I going to keep them apart? And you're going to have to get used to them just like you got used
*  to integrals and differentials and things like that. If I ask anyone who had algebra and calculus,
*  would you ever confound differentials with integrals? And it goes like, of course not.
*  Yes, because you got used to this stuff. So there seems to be this barrier. And in particular,
*  very often information theory is perceived as being an engineering discipline. And they go like,
*  well, the engineers, they want to do error correcting codes. What does this have to do
*  with biology? In fact, I've seen this in print saying the engineering discipline of information
*  theory has nothing to say about biology because these are very different things. It's like saying,
*  well, information theory can't apply to physics when in fact, we do know very well that it does.
*  In fact, I just explained the second law of thermodynamics in terms of information theory.
*  Right. And so this barrier is very palpable. So if somebody is an established scientist
*  and you tell them, well, you know what, you should really be using information theory,
*  they're not going to do it. They're entrenched in their ways and they usually are not receptive
*  to learning in a sense, a whole new bag of tricks. It is not that different from what happened in
*  black hole physics where they constantly talk about information loss in black holes and not a
*  single paper is trying to calculate the capacity of the black hole channel, except of course me.
*  But that's because I know information theory. But these people have been working in this area for
*  30 years and not picked up a single book or article on information theory. Again, there's
*  this barrier. They're saying like this concept is different from the concept I need. And the answer
*  is no, it is the same concept. I'm a little bit sympathetic because I know when I read papers
*  in economics, they have this habit of denoting variables in equations by words rather than by
*  single letters. And it's so trivial and silly, but it truly rubs me the wrong way. And I have
*  trouble wrapping my brain around it. No, I fully agree with you because that is not how we write
*  equations. I still almost vividly remember this aversion where I'm like, this is not my thing.
*  But you have to power through this. In my lab, everybody gets the basic introduction to
*  information theory. And then once you've sort of internalized it, you cannot see the world except
*  through that lens of information theory. It's like the hammer that makes everything look like a nail.
*  And in my book, in fact, I sort of co-opt the famous saying, which we all know in biology,
*  which says nothing in biology makes sense except in the light of evolution, which certainly is true.
*  But I basically have changed it around to say nothing in biology makes sense except in the light
*  of information. Then of course, information is that which evolves. Really, I mean, people would
*  say organisms involve. No, what evolves actually is information. The information is what is essential
*  in an organism. The organism itself isn't really that essential in a sense. It's replaceable.
*  If we have offspring, they carry most of the information with them, but only the encoded
*  information. Of course, what we think is specific to ourselves is of course the stuff in our brain
*  that we have talked about about 25 minutes earlier. The information that we acquired over a lifetime
*  is of course making us special. The information in your genome does not make you special,
*  but it is what makes you alive. So is it fair to think of Charles Darwin as an early information
*  theorist? Well, I would say no, simply because he didn't really, and he had no way of understanding
*  that the basis of inheritance was really the replication of information. He didn't even know
*  how any of this stuff was encoded because all that was discovered in 1958. Or we should say that
*  John von Neumann kind of figured it out a little bit earlier when he came up with this theory of
*  self-replicating machines, which essentially could have told Watson and Crick where to look for
*  the information. Darwin did not know that, but he had, via his sleuthing, in a sense,
*  going on boats and looking at stuff, figured out, hey, there's variation going on, there's selection
*  going on, and there's inheritance going on. The fact that these three things are properties of
*  information, so inheritance being the replication of information, variance being the mutation
*  of information, the changing of information, and selection is the meaning of information.
*  In other words, those pieces of information that have a lot of information are fitter,
*  and therefore will have more offspring. And therefore, in fact, because I told you about
*  the relationship between information and fitness, then the meaning of information is selection.
*  We can think of the entire evolutionary process in terms of what happens to information,
*  and we should, in fact. But Darwin did not think that way, even though, of course, I haven't read
*  all of his works, even though many of them are in my little natural history collection in my bookshelf,
*  but they are big, big tomes. One of the things that is so astonishing to me is that Darwin had in his
*  head essentially 12 book treaties, and then was forced to publish the abstract of it as the first
*  book, which is now the origin of species. But he had so much more to say, and then over the rest of
*  his life, in fact, said many of these things. And of course, most of those things, like about
*  worms and about plants and things like that, we don't usually read. But in there, if you study
*  those volumes maybe with more attention to the concept of information, in the idea that
*  what makes these plants how they are, in fact, is making predictions. But he's, in fact, a good
*  example. Darwin himself at some point noticed a particular orchid which had a very, very long neck,
*  which he knew had to be pollinated. And it was about 30 centimeters,
*  what is that in, it's about a foot, or even longer, in fact. But basically he said,
*  now I will make a prediction. I will predict that there is a pollinator exists with a proboscis or
*  a nose, which is about that length. And even though he didn't live to see that prediction come
*  true, in fact, his competitor in the evolutionary field that almost scooped him, he in fact,
*  basically said, oh, and I'm going to tell you that this must be a sphinx moth. And in fact,
*  they later found it after Darwin died. And that was exactly as he had predicted it. So to some
*  extent, he knew that evolution, this idea, the theory of evolution is a predictive theory,
*  even though he didn't think of it in terms of information theoretical terms.
*  So yeah, a typical evolutionary biologist would try to explain things in terms of there's a
*  population with certain traits, and there's a fitness landscape, and they move towards peaks
*  of the fitness landscape. And so you're not undermining that, you're just saying that a useful
*  way of thinking about fitness is having the information to successfully predict what's
*  going to happen in your environment and therefore survive. That's right. I don't undermine any of
*  the standard population genetics is really just a very different way of understanding what fitness
*  is. You know, after all, fitness, the way you know, it is not the same word as we talk about
*  physical fitness, of course, right? fitness in biology means fitting your environment well.
*  Right? It means being adapted to your environment, which means corresponding to right and see we're
*  seeing aha, that means in a sense that your body structure, you know, is predictive about what world
*  you live in. Right? So for example, equal i bacteria, they grow best at 37 degrees Celsius.
*  Well, that's weird, isn't it? Well, no, it's not weird. That's the temperature of our stomach.
*  So basically, their molecular biology makes a prediction about what environment they're in,
*  namely one that 37 degrees Celsius, if their prediction is off, well, that means in fact,
*  you know, they don't have as much information as they think, and they're actually not going to
*  grow as fast. Right? So this correlation between the genome and the environment gives you the
*  fitness because it tells you you're fitting this environment. Well, you're well adapted to it.
*  And that concept information is precisely that this correlation. And this is a very important
*  point because it reminds us that just so people don't get the wrong idea, information isn't
*  necessarily conscious, right? It's not something that you might say, you know, the information in
*  your genome is very well adapted to your environment, even though you personally might have no idea with
*  the arrangement of nucleotides in your DNA is. That's right. So obviously, you know,
*  when we're talking about the fact that cells make predictions about their environment, which they
*  do all the time, because cells have to make decisions. It's not like they have a brain.
*  Yeah. But to some extent, we also know that because once you understand that information is
*  just a correlation, which is a non random correlation, because sometimes you get correlation
*  by chance. But no, we're looking for correlations that are not by chance and that are on top of that
*  being maintained. Right. Because in thermodynamics, you might have correlations by chance,
*  but they are going to disappear very soon. Right. The genome is making sure that these correlations
*  are being maintained so that we can continue using, you know, what we have to make predictions about
*  the environment. If you would be loosening this continuous maintenance, then information would go
*  away and we call that death. Is that what we call death? Good. Now that we know. But I this does
*  bring us to a very fun point you make in the book is that we can think of evolution as a kind of
*  Maxwell's demon and maybe be fun to explain what Maxwell's demon is. Not everyone knows. And what
*  this has to do with evolution? Right. So that's a good point. And thank you for leading me into
*  that, because it's one of my favorite parts of the book, actually. So Maxwell's demon. Let's not talk
*  about why this devil was invented. But let's focus on what he does. So the Maxwell's demon basically
*  is sitting at the intersection of two, let's say boxes, and there's a little window inside of the
*  box. And now both boxes are have gas in them, gas molecules who have different speeds, you know, by
*  in fact described by the Maxwell distribution, right? Turns out. And now imagine that this demon
*  who sits there, he operates sort of the door between the two, the two boxes. And he also has
*  a measurement device that he uses in order to measure the speed of a molecule, for example,
*  one that is about to go through the door. And then he goes like, okay, if this is a fast molecule,
*  I'm going to let it go through. But if it's a slow molecule, I'm going to shut the door. And so that
*  it is in fact going to be reflected. If he does that a lot, he's going to have one half of the
*  two boxes, I mean, or I should say the left box as opposed to the right box with lots of fast molecules.
*  And the other one will be, you know, stuck with all the slow molecules. That is in violation in
*  apparent violation, I should say, of the second law of thermodynamics, which basically says no,
*  that can't happen. Namely, a the formation of a non equilibrium situation from equilibrium. So
*  mathematically, it looks like what the demon has achieved is in fact creating order or violating
*  the second law of thermodynamics. The fact that he didn't do such a thing was in fact proven
*  mathematically and fully correctly later by by what's his name? Landauer. A Landauer,
*  a Rudolf Landauer, a German American physicist. And we're not going to go into how that proof goes.
*  But it is not a violation of the second law of thermodynamics. But this idea that via measurement,
*  you can actually reduce entropy is, of course, a very common one, because measurements give you
*  information and information is sort of the opposite of entropy. So yeah, if you, for example,
*  look into a room of molecules, and then essentially measure the speed and position of all the
*  molecules you're looking at, you could in principle achieve a lot of order, because you could punch
*  them, so to speak, with a laser and then all go them into one corner. So in other words,
*  measurements do allow you to decrease entropy. Now that we have described the Maxwell demon.
*  Now let's think about the Darwin demon. So in order to understand this, let's imagine that instead of
*  these measurements that the demon does, we're basically doing mutate. So the molecules are now
*  mutations. Okay, so you have a genome and a mutation happens, the mutation happens is completely random.
*  It could actually increase your fitness, or it could decrease your fitness. And now, the demon
*  basically says, look, I'm actually closing the door and not allowing the decreasing fitness mutations
*  to persist, but I'm going to keep those that actually are increasing my fitness. So in a sense,
*  the organism now performs a measurement, but it turns out, of course, that the mechanism of
*  evolution is precisely that way, namely, the deleterious mutation will make it such that the
*  organism carrying it doesn't have as many offspring, right, it's less fit. And as a consequence,
*  its frequency in the population will go down or else even if it's a lethal mutation will disappear,
*  whereas the beneficial mutations will in fact be enhanced. So because the beneficial mutations
*  create order because like there's now a type that increases in frequency, maybe even very fast
*  at the at the detriment of all of the other sequences, well, that creates order in the
*  population. And it's essentially because you learn something about the about the environment,
*  you've extracted information about the environment by having this measurement of the environment.
*  So in other words, these mutations that are being kept, they are measurements of the environment,
*  just like 37 degrees Celsius. Okay, so let's adjust our genome in such a way that we grow well,
*  you know, at 37 degrees Celsius. Whereas the deleterious mutations, of course, are misinformation,
*  right? And they reduce your fitness. And as a consequence, are thrown out of the window,
*  right? That's the the the the Maxwell demon closing the door on them. Right? And what that means is
*  that, well, if this is a continuous process, then it should lead to a constant increase about the
*  of information inside of an organism over time as evolution proceeds. And therefore, we can actually
*  formulate this as a law, namely the law of increasing information in evolution, that actually
*  predicts that if you start out with a low information beginning sequence, that over time,
*  the information must increase, but not all the time. For example, if the environment changes,
*  well, we already discussed that, then your information drops, right? And you have to sort
*  of relearn things, right? There are other ways in which information can get lost. For example,
*  recombination can actually destroy information, right? It can also lead to a good thing. So this
*  this natural demon, this this Darwin demon is not perfect. In a sense, it's leaky. It sometimes
*  makes wrong decisions, where information can actually go down instead of up, right? But overall,
*  on average, this theory of evolution predicts that the amount of information that is stored in a
*  population of genomes has to be going up. And that is very interesting, because we've been searching
*  for a way to understand the biocomplexity that we are seeing around us, and asking how on earth is
*  all of this possible? And can I understand if one organism is more complex than another? And this
*  idea of complexity, of course, is difficult to put in mathematics. But in fact, it turns out that
*  complexity is literally just information. In other words, information or complexity is just
*  a proxy for information. Why? Complexity essentially is stuff that is complicated,
*  but helps you do something interesting, right? We don't associate complexity with something that
*  is just structurally interesting, but actually doesn't do anything, right? What was called a
*  spandrel by Gould and Lewington in biology, right? Something that looks very complicated. Once you
*  understand it's actually just, let's say, an icicle, they are not really that complex. But there
*  are really complex things, for example, our brains, right? But that is, in fact, reflected
*  by the information necessary to make it, right? So it turns out, therefore, that information is
*  really the correct way of measuring complexity. And therefore, the question of is complexity
*  increasing in evolution is simply answered as a yes, as long as you understand that complexity is
*  really information, and the natural demon is responsible for that law of increasing information.
*  Good, because naively, we might look at an organism and try to figure out, oh, that looks
*  complicated, that looks pretty simple. And we wonder why all this complexity has grown. But
*  you're saying that that's just a pale reflection of what's really going on underneath the hood.
*  That's right. But it's almost like saying, like, if I look at a sequence,
*  right, somebody's genome or some animal's genome or a bacterial genome, I can't immediately see,
*  well, this is information, this is not information, here's some information, is it like, like,
*  they look the same, right? So we need to figure out how they're making predictions, or in other
*  words, how are they functioning in the world. So if you have something that looks complex,
*  then you have to ask yourself, let's observe this thing and see whether what looks such as
*  an intricate mechanism is in fact necessary for survival, or whether it is just something that is
*  a consequence of something else, right? We see sometimes like these complex display behaviors
*  in animals, and they are obviously important in mating. And if you would remove them, in fact,
*  your fitness drops to zero, because you don't get to mate zero offspring zero. Right. But then
*  there are other things that are in a sense just not they're not important for the actual survival,
*  you would take them away. And it doesn't change the fitness. It's like saying you're removing a
*  section of the genomic code. But if that is not predictive of anything, if it does not carry any
*  information, it is not important for fitness, you can take it away. And we don't have said to get,
*  if I understood what you said correctly, we don't right now have a clear cut way of looking
*  at a genome and saying this part contains information, this part doesn't. We actually
*  do, but only if we're looking at many of them, not a single one. Right. If I have 100 versions
*  of a gene, there are regions in it that are unimportant for survival. If I then make an
*  alignment of them, then I can recognize, oh, look, this changes all the time at this position.
*  Clearly, that doesn't mean anything because you can just really nearly change it. But then you go
*  like, oh, but look at this section. It's the same everywhere the same for every organism. I bet you
*  it is because when you change it, you die. And that's why I haven't seen it. Right. If you would
*  make it, it would simply die. And therefore, you it doesn't enter your database. So you have to do
*  these multiple sequence alignment, as they're called in bioinformatics. And then you're looking
*  across, you know, column by column, and you see some columns being completely conserved by
*  evolution, even though evolution constantly tries to change them, right, through the mutational
*  process. And then you see columns which are really nearly like on the nucleotide level,
*  you see A, C, G, and T with 25% frequency. And you go like clearly not information. Right. And so
*  that is, in fact, the basis of the algorithm that I described in the book that allows you to measure
*  the amount of information in a sequence. But if you do not have a multiple sequence alignment,
*  in other words, a bunch of examples, then you cannot understand what is information because
*  everything looks the same. And this reminds me that you, of course, have collaborated with your
*  colleague, Richard Lensky on his long term, who was the boss of the long term evolution experiments.
*  You've actually seen data like this. That's right. In fact, you know, we constantly see this, we see
*  this more easily in digital life experiments, where we have self replicating computer programs
*  that live inside of a computer, just like the one I'm staring at right now, and that you're staring
*  at right now. And there we can extract these sequences, and we can look precisely where the
*  information is. And in fact, we can measure the information and see as the fitness increases,
*  the information increases. It's literally if you would be taking the log of the fitness
*  and superimpose it with the calculated information, they're almost on top of each other.
*  Right? Because it's the log fitness, which is basically the growth rate,
*  which is, in a sense, mathematically equivalent to information. So if information is zero,
*  your growth rate is zero. Right? So my biological knowledge is not very big, but I do recall
*  understanding that the human genome is not the longest out there in the ecosystem. Right?
*  Is that something we understand? So this is an important question. And it's in biological
*  literature is called the C value paradox. If you just look at the length of genomes,
*  there is an amoeba out there, which has 200 times more DNA than we have. It's called amoeba w,
*  actually. So it's almost like the W in a former president. So, you know, you can think of that as
*  you may. So clearly, genomic content isn't information. Right? But if you would take
*  the genome of let's say, 1000 of these amoeba, and then align it, then you would see that most
*  of the stuff is completely meaningless. Or else, in fact, it might not be haploid. So in other words,
*  you have 100 copies of the same small piece of information. And here's another thing that you
*  need to understand about information. If I have one book, okay, that let's say, is predictive about
*  certain things, and then you have a copy of the book, that's not twice as much information. It is
*  exactly one time as much information. So if you have 100 copies, because you have 100 copies of
*  your genome, like we, for example, have two copies, we are deployed, there's many other
*  organisms like in particular in plants, which are terraploid, you know, they have 16 copies and so
*  on. So this amoeba probably has over 100 copies of its own genome. So in other words, clearly,
*  this amount of DNA, you have to divide it by 100, that still wouldn't get us to the 3 billion that
*  we have 3 billion per chromosome. Right? So yeah, and it's not 6 billion in a 6 billion base pairs.
*  But in fact, out of the 3 billion nucleotides, which in a sense, give you a
*  entropy or potential information of 6 billion bits. But it's potential information, which is
*  the same thing as entropy, right? Only a small fraction of this actually encodes information.
*  And from the encode project, it is probably about 8%. And that's how you're getting to that number
*  of 500 million bits, which is about 8%, I think, of the 3.1 billion or so. Right? And so there are
*  some plant genomes that are enormous because of this explosion. But if you have several copies,
*  and if you have in plants, for example, there's lots and lots of intergenic regions, which are
*  meaningless. In other words, there's no information in there. Plants are sort of
*  spectacular for that. They have far more intergenic stuff than humans, for example.
*  Some of them have up to 70% intergenic stuff. And this intergenic stuff is probably also riddled
*  with transposons. So literally, if you would be taking it out or mutating it, it would not change
*  what the plant does at all. So there is no information encoded there. So if you really
*  want to plot just information content, in fact, Eugene Kuhnen, who works at the NIH, he has done
*  that. In fact, his plot is in my book. And you find out that bacteria are sort of very low there.
*  And humans, as far as we can measure, in fact, have the most information. Mammals generally,
*  but humans the most. So this idea that humans are, in a sense, the apex of complexity that some
*  people think is sort of very self-serving, that might not be wrong. Certainly, if you take a look
*  at it through the lens of information theory. Yeah, I believe that. That number went by pretty
*  quickly, so I want to get it right. 8% of the human genome is information-bearing?
*  It's coding. Yeah. And the rest is intergenic stuff or repetitive stuff. In other words,
*  it's uninformative. It seems a little inefficient. I don't know.
*  Well, I mean, it's because there is so much for example, if you have a gene, there are regions
*  that are called introns, which just have junk in it. And they're being excised before the stuff
*  is being translated into proteins. And so there's a vast amount of that. And then inside of
*  chromosomes, there's vast regions of repetitive stuff. Some of it might even serve structural
*  features so that molecules can attach to it, but it does not actually provide information about
*  surviving. So obviously, it is difficult to measure the information content because we would have to
*  have thousands of human genomes that you can align. Now we have, in fact, now thousands of human
*  genomes, but nobody's actually tried to do that. And I should say that in order for a good ensemble
*  to really be reflective of the information, we needed to have a good amount of variation.
*  In other words, those nucleotides that are mutatable, they should have had a chance to mutate.
*  But because we humans have a relatively common recent ancestor, there's a lot of conservation
*  in the genome that is common through common descent. Right. And it looks like it might be
*  information if I'm making such an alignment of a thousand genomes, but in fact might not be.
*  So one of the things you might want to do is you want to take a lot of African genomes for this
*  alignment, because there's much more variation in the African genomes because they have in a sense
*  been evolving longer and their common ancestors much, much, much earlier, which is why there is
*  so much more variation. Right. And that would be a much better estimate is if you take European
*  genomes and make that alignment, because really, you know, we're looking at like a hundred thousand
*  years of variation, which given the population sizes might not be enough to really reveal the
*  information content. So if you have a population that has a fairly common recent ancestor, then
*  even this alignment is not going to do a very good job of giving you the information. But very often
*  in proteins, single proteins, for example, or viral proteins, which are evolving very quickly,
*  you can actually measure this information. And I've done this, for example, for the HIV protease,
*  which is a 99 amino acid sequence. And then see, for example, like the example with drugs that I
*  gave you, but when you introduce, you know, anti HIV drugs in the population, you see the information
*  dropping very rapidly. And then because we have data over time, you can see how as the virus
*  evolves drug resistance, it really learns about this new world that is being cast into. And you
*  see the information over 10 years really approaching the preintroduction levels. Right. So for certain
*  proteins and molecules, it's much easier to actually do this analysis and measuring information
*  than, for example, to do it for a whole genome. In principle, it can be done. But ideally, you would
*  do essays where you're trying to mutate every nucleotide, right, and see how it reacts. And
*  that's, of course, not feasible right now. So it would be unethical, by the way, also, by the way.
*  Yeah, that happens in other podcasts I do. It'd be fun to do certain experiments, you just can't
*  really do it. But one way of saying what you just said a little while ago is that the human genome
*  has not had time to equilibrate in some sense. That is exactly what I say. Good. So there's plenty
*  of unexplored variation in it. Because I was going to ask, you know, are there sections of the human
*  genome or, for that matter, other advanced genomes where there is some continuity over time? So
*  clearly, this section of the DNA is carrying information, but we don't know what it does.
*  Absolutely. One of my favorite examples is that there are untranslated regions in the genome
*  that seem to be completely conserved. And it looks like it's untranslated, which means no
*  protein is being made. Well, an RNA is actually being made. Right. So in fact, these are long
*  stretches of RNA. And what they do is they can form molecules called ribozymes. And it is a fairly
*  recent discovery that these, in fact, are actually very important in understanding brain function.
*  So there are these long non-coding RNAs. And remember, DNA has this neutrality in the third
*  position of a codon. So for many of the amino acids, when you mutate the third codon, because
*  every amino acid is encoded by a triplet, you can change it willy-nilly. It doesn't change the amino
*  acid. So there should be neutrality in that position. And you see this throughout the genome.
*  Right. But then you have these non-coding regions where there's no neutrality whatsoever. Well, yes,
*  because if you translate it into an RNA, the ribozyme, there's no codon translation. It's not
*  made from amino acids. So in fact, every nucleotide is important. And that's how it comes that these
*  vast long non-coding RNA regions are completely conserved, which means that they carry 100%
*  information or close to that. They're not 100% conserved. But that's because sometimes in these
*  ribozymes, because they are folding into structures, you can make a mutation on one
*  nucleotide as long as you're making the complementary mutation at the corresponding one.
*  Right. But this is a fundamental discovery, because it means that these ribozymes that are
*  super important in the survival of the organism. And in fact, May explained, so they did this study
*  for in brains of flies, that they are super important in controlling mating behavior of the
*  fly, which was previously not understood. And you can't find a protein that does it. Well,
*  because done by these RNA sequences. That's actually super interesting. And I'm pretty sure
*  I didn't know this. So the central dogma in molecular biology is that the DNA contains
*  information that gets transcribed into RNA that tells the ribozyme which proteins to make. And
*  what you're saying is that that's not all the DNA does. There's a separate function where parts of
*  it get transcribed into RNA and then don't make proteins, they make ribozymes instead. And those
*  also play a crucial role. That's absolutely right. So whenever you hear the word dogma,
*  then you're always going like, well, okay, so I'm sure it's not really a dogma. So let's actually
*  look for the violations of it. And that's always a fruitful avenue of investigation. So yeah,
*  in fact, the role that RNAs play in the molecular biology of the cell cannot be underestimated. I
*  mean, these are highly functional molecules, they modify DNA. If you didn't know that, there's a
*  whole bunch of gene editing going on. Certainly in single celled eukaryotes, and I talk a little
*  bit about that in my book about the trypanosomes, a fantastic, absolutely stunning story of how these
*  RNAs are ensuring in a sense, the survival of genetic information that should have died 100
*  million years ago, in a sense. And so these molecules, they're also regulators. So the RNA
*  molecules, the ribozymes, which are untranslated are so functionally important that we cannot
*  understand really the molecular biology of the cell without their action.
*  Interesting. And that's actually a great segue into the sort of the final topic that I wanted
*  to hit here. It would be a shame if we didn't talk about the origin of life. And of course,
*  you know that there's a lot of people who put RNA front and center in that story, but we don't know
*  what the right story is for the origin of life. So how can information theory help us here?
*  Right. So that's a great segue because in fact, the current thinking is that prior to DNA, we know
*  that DNA and proteins cannot have been at the very origin of life because you need proteins to, in a
*  sense, understand how DNA is acting. And you cannot understand one without the other. So it cannot be,
*  you cannot have this separation between storage material, which is DNA, and machine, which is
*  the proteins, as in the origin. Now, it turns out that RNAs, they can store information because
*  they're really the RNA nucleotides are cousins of DNA. They just basically have an oxygen
*  compound more. That's why the RNAs are called ribonucleotides and the DNA is called deoxy,
*  namely removed ribonucleotides with an oxygen removed. That difference is actually very important
*  because it affects the stability of the molecule. And of course, if you're going to do information
*  storage, you want to have a stable one, and that's the DNA. However, the RNA molecule, which
*  it's almost like a DNA, but can actually conform in all kinds of different ways,
*  they can play the role of a machine, the ribozymes that we just talked about.
*  So according to the RNA world framework, you're going like, hey, how do you have something where
*  information and machine is one and the same? And that would be the RNA world. So in other words,
*  self replicating RNA molecules, like where they store information and are folding into the
*  machinery that replicates the information. We, as you correctly pointed out, we don't know if that is
*  the ancestor because the biochemists tell me that there are some fundamental problems of,
*  you know, how this whole stuff could have worked out. And that's a problem in biochemistry,
*  which I only lightly touch upon in the book because I'm certainly not an expert on that.
*  But the important thing to understand the origin of life is to first understand what life is.
*  And what life is, is basically information, a string of information, or a string that contains
*  information about how to make copies of that information. You might think, oh, but that's not
*  so difficult. I make copies of information all the time. I have a copy machine. It's like, yes,
*  but who built the copy machine? The copy machine isn't some random thing. If you just throw a bunch
*  of piles of metal together, it's not going to form a copy machine. In fact, it takes an
*  inordinately complex set of instructions to make that copy machine. So yes, it makes copies and
*  it's great at doing that. And you could, in fact, make copies of the blueprint of a copy machine.
*  But that copy machine isn't going to make the copy machine from that blueprint. It's not. It
*  makes copies. That's it. But if you had a machine that is, in fact, built from information,
*  and therefore then once it's crumpled up, in a sense, into this ribozyme, then makes copies
*  of the actual information, well, that's life. So life is information that copies itself.
*  But if you just have a little bit of information, it is not going to do that because, like I said,
*  to create a machine that can make copies of information, you need a minimum amount.
*  Five bits is not going to do it. Maybe 100 bits is not going to do it. In fact, we don't know
*  what the smallest amount of information is that has a capacity to replicate. You know why? Because
*  we also don't know what the environment is within which this replication happened because I told you
*  that the information is really information about the environment. So a string of 100 bits
*  is 100 potential information. But depending on the environment, it could be a lot and it could be a
*  little. And so we don't know a whole lot about the very early Earth, but there could be very
*  many different environments. But what we do know, and I can say that unequivocally, is that there is
*  a minimum amount of information and that amount of information cannot be obtained by chance
*  by chance. Under no circumstance. Okay. Right. Well, I should say, mathematically speaking,
*  if the likelihood of finding any of these molecules would be chance, right. However,
*  there are in fact mechanisms that could make an avenue where information can actually gradually
*  accumulate without a Darwinian process. This is speculation. Sure. But think of it this way.
*  We can imagine a process where a molecule that carries no information but is in fact a
*  sequence of in some alphabet. Let's imagine even it to be an RNA. Right. We can imagine that there
*  is a process by which it can be replicated, but in a sense passively. Right. For example,
*  it could be laying on a clay surface and then you can basically have a process that will make sure
*  that only complementary bases are being added. Right. Then basically it becomes copied. But
*  there's no information in it. Right. So this copying of information or of a sequence, you're
*  copying entropy really. Right. But now because the copying machinery is actually in the hardware,
*  not in the software. Right. It's this clay and it's the process of complementation.
*  Now imagine that if in fact the rate of making errors in the complementarity
*  can sort of vary. So it turns out that the speed of this operation of copying varies depending on
*  how many errors you are making in that complement complementarity. So if for some reason you have
*  something that makes this faster, well, that's actually a good thing. And you're going to make
*  more of these copies, even though you might think there's no information. But now imagine that what
*  makes this faster, which means makes it more accurate because they are the same thing,
*  is actually something that is part of that information that sort of like helps and binds.
*  Like something breaks off and then sort of goes like, hey, I'm using that broken off piece to
*  actually make that process more error free and therefore faster. What just happened then is that
*  information just seeped into the genome. Because remember that piece that broke off is actually
*  one of your own. And you can imagine, but so a process like that, that slowly but surely
*  information about how to do the replication moves from the hardware into the software.
*  It's a non-equilibrium process, but it is at least imaginable. Right. Because you have to reach
*  this limit until there's enough information in the sequence that it autonomously replicates without
*  the support of the hardware. That is my sort of imaginary view of the origin of life. But it is
*  a hard thing because you have to reach this limit. Let's say the limit is 200 bits, right? Only after
*  200 bits can evolution take hold, which then means I can have the evolutionary process increase this
*  amount of information to infinity, right? Theoretically. But before you have achieved
*  Darwinian evolution, any information that is in the sequence is now highly fragile.
*  It is basically prone to deteriorating due to the second law of thermodynamics, right? So you
*  basically have to have a process where you are constantly working against this law. But it is
*  because information from the replicative machinery that the hardware is seeping into your sequence.
*  If this happens fast enough, you might actually get to this point where Darwinian evolution can
*  take place and therefore you separated yourself from the second law of thermodynamics.
*  Okay, good. I actually think I understand that. Let me try to run it by you again and see if I
*  got the right idea. We talked about Maxwell's demon and evolution, and that was pretty clear to me.
*  If you just had a set of genomes and you just acted randomly on them, they would randomly walk
*  through the space of all possible genomes and the entropy of that distribution would go up.
*  That is the second law of thermodynamics. But you are saying that selection kicks in,
*  in the case of evolution, and that basically acts like Maxwell's demon to lower the entropy by sort
*  of nudging all of the genomes towards areas of higher fitness. That is pretty darn efficient.
*  You are suggesting that maybe the origin of life was a similar mechanism, not quite the same and
*  not quite as efficient, but something that was a little Maxwell's demon-y to allow the distribution
*  to become lower entropy until Darwin could kick in. That is exactly right. If you think about this
*  idea that if you are making fewer mistakes in the copying process, that the copying goes faster and
*  you are therefore making more copies, that means that there is a Darwin-y mechanism at work, even
*  though there is no self-replication. But there is replication. But it is replication of non-informative
*  things which, by this mechanism, some of this stuff by chance happens to increase your speed
*  of replication. Those are being maintained. Yes, the information about to replicate is in the
*  hardware, not in the software, but it slowly starts seeping in. Slowly or fast, it really depends on
*  the environment that you are in. Of course, we have no glimpse of any of that because if you imagine
*  that let's say it is actually a process that is not that difficult to achieve, wherever it
*  constantly keeps occurring, it would be dwarfed by any form of life that is actually there, that has
*  perfected this for four billion years. There are these dark smokers and these underground
*  what are they called? These pure hydrogen basically. Yes, these alkaline vents. Volcanoes almost.
*  And there is all kinds of interesting bacterial life going on and who knows what else goes on there.
*  There are some theorists that claim that yes, these type of environments are perfect for the origin
*  of life, but even if it would be constantly reoccurring there, we wouldn't see it because
*  bacteria have already colonized them. Okay, that is great. That is a very interesting
*  set of ideas. I hope that it is followed up on. But we are near the end of the podcast, so we are
*  allowed to think big now and it does lead into I guess the last question, which is human beings
*  have developed capacities for manipulating information that didn't exist before human beings
*  came along. We can not only think, but we can learn, we can teach in ways that other species
*  don't. We can store information and replicate it in books and on computers and so forth. Is this
*  analogous to the origin of life? Is this another way that information is reproducing itself? Are we
*  seeing a phase transition to a new kind of information phase? I think you are right about
*  that. I mean just imagine the advance of being able to write down what you are going to do.
*  Being able to write down what you have learned so that other people can build upon that.
*  That obviously in a sense, I am saying obviously, but maybe that is not obvious to everyone.
*  Obviously that is the magic power that we have acquired as a human species that no other species
*  has. The best that other species can do is to somehow teach young generations about certain
*  behaviors, hunting behaviors or maybe even tricks that you can use with rocks and sticks and things
*  like that. But to actually figure out mathematics and write it down into a book and then teach that
*  to other people so that they can for example predict the orbit of a planet 100 million years
*  from now. I mean if that is not mind boggling, then I don't know what. Now if you think about it,
*  what we call our ability to make predictions over long distances as far as humans are concerned,
*  in a sense we call that intelligence. We are making intelligent decisions so that we in a sense can
*  survive better. But in fact clearly making predictions about what the environment is tomorrow
*  is going to be an important element in my survival. It was an important element for survival for any
*  hunting species that goes like, oh I predict that this prey is going to be at this location
*  in about 10 seconds and if I can make that prediction very accurate, I will catch that prey.
*  Now if you think about intelligence as the temporal radius at which you can make predictions with
*  accuracy to better than chance, well then you realize well bacteria make predictions all the
*  time, but they make predictions about the next second because they're making predictions about
*  where the nutrient is, but that could change very quickly. But for example this behavior of
*  finding food, chemotaxis, well that's clearly in a sense an intelligent behavior in the sense that
*  it makes certain predictions that are going to come true or not within a second or so.
*  But other animals for example, let's say chipmunks, they make predictions about well
*  the next season will be such that there will be winter so I may have to actually store some food.
*  But we as humans by having developed writing systems, by having developed mathematics,
*  can now make predictions in time over a far, far longer period that are accurate better than
*  chance. The fact that we are talking about global warming and how that could affect us as a species
*  is an obvious intelligent concept because we have understood that if we don't do anything
*  then we might be in big, big trouble. That is making predictions in a time scale far removed
*  of our day-to-day activity. And our brain does that, but our brain of course has been doing this
*  before we had figured out writing systems. But now the conjunction of our brain where information
*  during a lifetime is stored and then we can make it permanent in books, that is the real secret
*  sauce to the success of this species as far as I'm concerned. Well we'll see whether or not we have
*  the collective strength of will to actually act on these predictions that we're making or not.
*  Yeah that's right of course that's the big political question. Unfortunately it is a political one and
*  not a mathematical one. The mathematical one is very obvious. Good, that helps us a little bit.
*  Chris Adami, thanks so much for being on the Mindscape Podcast.
*  It was really my pleasure. Thank you, Sean.
