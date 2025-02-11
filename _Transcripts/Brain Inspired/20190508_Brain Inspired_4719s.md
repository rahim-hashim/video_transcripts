---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4719s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 6058
Video Rating: None
---

# BI 034 Tony Zador: How DNA and Evolution Can Inform AI
**Brain Inspired:** [May 08, 2019](https://www.youtube.com/watch?v=nN9uh04KKno)
*  The goal of the paper was really to point out to people who work in machine learning
*  that much of what they call learning would not, to a biologist, seem like learning.
*  If I'd come on the scene in the 1950s, there's no way I would have been suckered into working
*  on neurons because that was clearly going to be a long haul, right?
*  What is something that you used to believe that you consider naive now?
*  Oh, that's easy enough.
*  I mean, what I did my PhD thesis on, which was...
*  This is Brain Inspired.
*  Hello, highly evolved brains.
*  This is Paul Middlebrooks.
*  All right.
*  The only real thing I have to mention today before I introduce the guest is that I would
*  love to hear from you.
*  Of course, I always love to hear from you, but specifically, I'd love to hear your answers
*  to the following question.
*  If you could wave a magic wand and manifest proficiency in some skill or body of knowledge
*  that you feel like would help you move forward in your research or work, what would that
*  skill or body of knowledge be?
*  Send me an email to paul at braininspired.co or reach out on Twitter.
*  I'm at PGMID.
*  You will hear my guest's answer or non-answer later in the show.
*  That guest is Tony Zador.
*  Tony runs his lab at Cold Spring Harbor Laboratory.
*  Well here, Tony has taken his own twisting somewhat circuitous path to his modern station,
*  as we all do, I suppose.
*  The main thrusts of his research these days is twofold.
*  One, he studies the neuroscience of auditory decision making in rodents, and we talk about
*  why he's chosen rodents to study what traditionally, for whatever reason, has been thought of as
*  a higher cognitive process, decision making.
*  And two, he studies how we might go about mapping out the connectome, that is, the blueprints
*  for how all of our neurons connect up to solve some otherwise unsolvable problems.
*  And he's doing this by working on developing little unique DNA barcodes that we could insert
*  into every neuron to figure out exactly where that neuron projects and which other neurons
*  it connects to.
*  I'll leave it to you for now to learn more about his work through his website linked
*  in the show notes, because we don't really talk about any of those things today.
*  Today we focus on his recent manuscript suggesting the AI world might want to pay more attention
*  to the role DNA plays in providing a massively pre-trained network, essentially, to jumpstart
*  development as animals, an explanation for why we don't need a million examples of a
*  nipple, for instance, to latch onto one right after we pop out of the womb into this beautiful
*  mess we call life.
*  I know many human mothers may disagree with our human innate ability to latch onto nipples
*  because many do struggle, so it's not a perfect analogy.
*  Speaking of nipples, we talk a few minutes about the early days of the now coveted neural
*  information processing, or NIPS, conference, now called NURiPs, because of the existence
*  of nipples and the existence of childish men, and how Tony grew the well-respected COSIGN
*  conference out of that world.
*  We also talk some evolution, real neurons versus artificial network units, reductionism,
*  I even say Big Bang once, so it was a fun conversation for me, I think it'll be fun
*  for you.
*  You can find the show notes at BrainInspired.co slash podcast slash 34.
*  So many new Patreon supporters to thank, you can find out how to do that at BrainInspired.co.
*  Tony, welcome to the show and thanks for being here.
*  It's a pleasure to be on.
*  This is your 20th year at Cold Spring Harbor Laboratory, where you're the program chair
*  in neuroscience.
*  Is that right?
*  And if so, have you celebrated or will you celebrate?
*  Indeed, it is just about to be my 20th year here at Cold Spring Harbor Lab.
*  I did recently step down as program chair of neuroscience, but I was program chair for
*  quite a while.
*  They do have a celebration for those of us who make it to the 20th year.
*  I have been invited and I do hope to attend.
*  I'm in the rarefied company of my boss, Bruce Stillman, and a handful of others, including
*  Jim Watson.
*  Yeah, so you've been there since 1999, for those of you who are listening to this podcast
*  years and years from now.
*  It is 2019 now.
*  But Tony, your research really has run the gamut in terms of levels of inquiry, from
*  down to the level of molecules, to the synaptic level, to cells, to neural circuits, up to
*  behavior.
*  And you're also perfect for this show because you really entered your career.
*  You originally worked on the theory side of neuroscience and did work with neural networks.
*  And we'll talk about your early participation at the NIPS conferences, or the NURiPS conferences
*  now, and how you started COSIGN out of your involvement in those early NIPS days.
*  And through your career, you've incorporated more of the experimental side, working with
*  slice neurophysiology, studying decision making in primates, eventually pioneering the study
*  of decision making in rodents, and in your case, auditory decision making.
*  And I think, and we can talk more about this, I think some of those obstacles that you faced
*  in that work with the rodents has led you to your connectomics work, developing a DNA
*  barcoding method to figure out the wiring diagram of mouse brains.
*  So I know that's an embarrassingly incomplete list.
*  No, no, I was going to say that's a fantastic summary of my career.
*  And I think we can just call this entire conversation to an end because I don't know what's left
*  for me to say.
*  Well, I was going to fill in a couple of the details.
*  Okay.
*  Well, good.
*  I was going to ask you how you would characterize your journey thus far.
*  But if that's good enough, we can just proceed.
*  That's great.
*  I think the overarching theme is that I have a short attention span.
*  Yeah, well, so sometimes I ask this question toward the end of a show.
*  But in this case, I'd like to ask you now, because you've had sort of a definitive path
*  and everyone has a unique path, you know, if you were going to go back in the early
*  days of graduate school, now, let's say, let's say you're starting off graduate school or
*  somewhere around there, what pathway would you lay out for yourself or what would you
*  start off in?
*  That's an interesting question.
*  I'm pretty happy with the path that I took, even though I did a lot of wandering.
*  I mean, going back even further, I started off in physics, then wandered over to linguistics
*  and went to medical school and then started in theoretical neuroscience.
*  And all of those things in different ways contributed to what I ended up doing.
*  At each stage, I guess I was driven by this tension between these fundamental questions
*  that I was excited about answering, which are the big questions that many of us go into
*  neuroscience to answer.
*  What is consciousness?
*  How does our mind work?
*  Things like that.
*  Am I attraction to simple, rigorous answers?
*  And the problem is there's a real tension there that the bigger the question, often
*  the less satisfying the answer.
*  So, it's been a back and forth.
*  I loved physics for the beauty of a simple equation that explains everything that you
*  asked.
*  I loved calculating how fast that ball goes down the inclined plane.
*  But then in the end, I didn't care how fast the ball goes down an inclined plane.
*  And on the flip side, I would spend my evenings wondering, well, what is consciousness?
*  I don't think we're that much closer to understanding that than we were when I started
*  thinking about that.
*  So, it's that tension between interesting questions and satisfying answers.
*  Yeah.
*  I wonder if a better question is just how to approach the areas of study when you go
*  into it.
*  Because it kind of takes a craftsman's mindset, if you will, because you have to be...
*  Okay, so there are two ways to approach things, right?
*  One is you follow your passions and then see where that leads you.
*  And another is, you have an interesting question.
*  You might not necessarily be passionate about linguistics, like let's say, and maybe you
*  were, but you still approach it with the mindset of, okay, I'm going to figure this out.
*  And then you can kind of learn and become passionate along the way.
*  Is that a useful distinction at all for approaching?
*  It fascinates me the differences in how different...the many different paths there are to success,
*  to successfully addressing scientific problems.
*  What drives different people turns out, as far as I can tell, to be very different.
*  In my case, I'm not very good at doing things that I'm not passionate about.
*  I didn't always turn in my homework on time.
*  So if I don't understand why I'm doing something, I just can't do it.
*  If I don't understand why I'm memorizing something, I can't do it.
*  So in my case, I don't really have a choice.
*  I get super excited by a question and I dive into it.
*  And then if I get disillusioned by it, then I end up moving on.
*  But other people are much more disciplined.
*  And they say, here, I see that that mountain top that I'd like to be on, I understand that
*  to get there, I will need to do a bunch of things that I'm not that excited about doing,
*  but I will do them.
*  And many of those people end up getting to the tops of some very hard to climb mountains.
*  Yeah, that's true.
*  That's a good analogy.
*  Well, let's talk about history for a minute.
*  So I've had a few people on the show who have sort of lived through the early days of AI
*  and seen the transition from symbolic AI to statistical-based neural net type AI.
*  So Terry Sanofsky was on the show and he documented his experiences in his book, The
*  Deep Learning Revolution.
*  I've had Jay McClellan on the show and he shared some stories about the general antagonism
*  of the symbolic AI pioneers toward the statistical parallel distributed processing and neural
*  network folks.
*  And you are well traversed as well.
*  So you were in attendance and participated in the early NIPS conferences, Neural Information
*  Processing Conferences, which started in 87.
*  I think maybe your first abstract was in 90, 91.
*  Yeah, so actually, so yeah, so I'm a slightly younger academic generation than they are.
*  I was going to mention that.
*  You didn't have to chime in with that.
*  I would have mentioned it.
*  Yeah, so they were already established around the time that I started graduate school in
*  1986.
*  So the very first conference that I ever went to as a graduate student was actually the
*  precursor to what is now NeurIPS, which is the Snowbird Conference on Neural Networks
*  held at Snowbird.
*  I think the one that I went to.
*  So that started in the early to mid 80s from a bunch of neural network people at Bell
*  Labs, including John Hopfield and Terry was among those people.
*  And that was a small invitation only meeting.
*  And I was lucky that my PI was invited and I came along for the conference and the skiing.
*  And then I started going to the NIPS meetings.
*  That became my sort of go to conference even more than SFN, more than the Society for Neuroscience
*  meeting just because back then there were very few people doing what I was doing, which
*  is work at the interface between computational neuroscience and neural networks.
*  And in fact, those two fields hadn't even fully diverged at that time.
*  And so there was, that was, I think, well, to my mind, it was the best place to see computational
*  neuroscience.
*  It was the was the NIPS conference.
*  And that lasted for a few years, right?
*  Where the computational neuroscience and neural network work were really in a discourse.
*  But so, yeah, so can you give the flavor of like what it was like then and maybe how it's
*  changed since then?
*  And yeah, so to my mind back then, the question I was interested in then, and to some extent,
*  that's the question that has been sort of what has driven a lot of my work, is what
*  have the conventional neural network models failed to capture about how the brain works?
*  And so that question really has two flavors.
*  Can you use neural network like models to model the brain?
*  And can you look at the brain and use them to build better neural network type models
*  that compute more effectively?
*  And now it's easy to articulate those as two separate questions.
*  But at the time, I certainly didn't have quite as much clarity that those were two questions.
*  So and I think a lot of the people in the field sort of considered them to be similar
*  questions and many of the same people worked, including Terry.
*  I mean, Terry's lab is, I mean, his is one of the preeminent computational neuroscience
*  labs and he is one of the people who contributed in a lot of ways to basic neural network theory.
*  So, you know, those back then, those were not fully differentiated and it was only later
*  that the NIPS community started sort of pushing the argument that look, yes, birds, you know,
*  they start, everybody would trot out the birds analogy, right?
*  We're going to talk about that later too.
*  Yeah.
*  Yeah. So just, you know, for real listeners, you know, birds fly, but we don't necessarily
*  look to birds to build better airplanes.
*  And that became the sort of prevailing wisdom at NIPS.
*  And at that point, sort of the neuroscience community, the computational neuroscience
*  community at NIPS sort of shrank and shriveled up for the most part.
*  Well, let's just interject because I want to talk about this birds thing real quick
*  because I swear to you, this happened to me before I even read the paper that we're going
*  to talk about today because I've had multiple guests on the show use the birds analogy.
*  And I've kind of nodded my head, you know, yeah, that's a good analogy.
*  You're right.
*  And then I was on a run the other day and I was thinking it's a really a poor analogy
*  because sure, if you want to talk about how airplanes quote unquote fly, we build wings
*  and use propellers and it can fly.
*  That would even use jets sometimes.
*  Or turbine engines, jets, you know.
*  But if you compare that to the diversity of how flies, insects and other birds fly, it's
*  not even a comparison.
*  Right.
*  But anyway, I thought of this and then I read your paper and in the last paragraph of your
*  paper, you say that you articulate these same ideas.
*  And I thought, oh, that guy, he must be a genius because he thinks like me.
*  That's what I thought.
*  Exactly.
*  Yeah.
*  Yeah.
*  No, I mean, the birds analogy is flawed.
*  And actually, I think another one of your guests, Botvinnik, provided some history.
*  I didn't know that apparently some of the early aeronautics engineers actually did take
*  specific inspiration from birds beyond the fact that they provide an existence proof
*  for flight.
*  Right.
*  Yeah.
*  I don't really know the history of aviation well enough to comment on that, but I was
*  gratified to hear that the birds analogy is flawed in other ways as well.
*  That's right.
*  I mean, those early people who took inspiration probably did die.
*  But that's for another, that's for the history folks.
*  You mean while flying.
*  Yeah.
*  Well, attempting to fly.
*  Well, attempting to fly.
*  Yeah.
*  Okay.
*  Anyway, sorry for the diversion.
*  But so then through the bird analogy, the NIPS people shooed away all the computational
*  neuroscientists.
*  For the most part, yeah.
*  I mean, it wasn't, I don't think it was an explicit decision.
*  Right.
*  The community there began to shrink to the point where it was not.
*  I mean, there was, I think there was always a neuroscience track at NIPS, but it began
*  and honestly, there might have been people who continued to go there for that, but I
*  found it less appealing and so did most of the people I knew.
*  You found it so unappealing that you started your own conference, the Neural Information
*  Encoding or NICS conference.
*  That's right.
*  That was an invitee only affair as well.
*  Correct?
*  That's right.
*  That's right.
*  And then, I was hired actually by the Snowbird conferences.
*  I started a series of, when I was still a postdoc, I started a series of invitation
*  only conferences on computational neuroscience, but that sort of differed from some of the
*  other computational neuroscience meetings in that we really tried to always invite a
*  mix of theorists and experimentalists.
*  Those went on for, I guess the first one was 96 at Jackson Hole and then we started to
*  have a series of them at Snowbird and a few other.
*  Coincidentally, they were all ski resorts in the West, but they were typically held
*  in February, but that was just pure coincidence.
*  I think they were very, really influential meetings for me and sort of a group of people
*  who went back year after year and they continued until I stopped being the primary organizer
*  at some point.
*  Several other people organized it and they continued till I think around 2002.
*  And then at that point, we decided that the sort of demand in the community for these
*  meetings exceeded what you could do with a small invitation only meeting.
*  And then we rebooted as what is now the COSIGN meeting, which is not invitation only.
*  It's open to everyone and it has abstracted and it's modeled directly after NIPS.
*  And it's growing like NIPS, I think, right?
*  It's growing like NIPS was growing before the AI explosion, the modern machine learning
*  explosion.
*  Right.
*  We started off at around, I guess, 300 and this year we topped, I think, 1,100.
*  Our goal was not to grow, but we are growing and so we're figuring out how to handle that
*  exactly.
*  I mean, I guess that's a good problem to have in some respects.
*  Yeah, it changes the flavor of a meeting, but that's a whole other discussion.
*  It reflects the fact that there are a lot of people interested in computational and
*  systems neuroscience.
*  So that's what the COSIGN, CO as in computational, SY as in systems and E as in neuroscience.
*  Like you said, I know that the NIPS conferences these days because of the AI explosion sells
*  out in minutes, right?
*  Is that the...
*  Yeah, that's my understanding.
*  I haven't been to NIPS literally in 10 years.
*  So from what I understand, it's like hard to get tickets to that than to a very popular
*  concert.
*  Both of which I'd probably stay away from.
*  So okay, last question about some history and the current state of affairs.
*  So it's not NIPS anymore, it's NURIPS, right?
*  That's right.
*  And even in Terry's book, he refers to it as NIPS.
*  That's how recently the change happened, I guess.
*  Do you have...
*  Okay, so when I heard, oh, they're changing the, I guess, acronym to NURIPS, I honestly,
*  I'm so naive, I couldn't figure out why until I heard that it was because NIPS can be short
*  for nipples.
*  And that's the reason, right?
*  Do you have a take on the necessity of changing it?
*  Or was there like some chauvinistic culture that really shadowed it or what?
*  Do you know?
*  I mean, I only...
*  I read a couple articles about it, the same ones that are publicly available.
*  Yeah.
*  Yeah.
*  I think it's no secret that especially the tech world is prone to juvenile jokes and
*  is not always welcoming to a diverse group of people.
*  And so I think this was by popular demand in order to sort of help change the culture.
*  I have no idea whether it's successful, but it's certainly worth trying.
*  Yeah.
*  Well, and so we advance.
*  So let's talk about evolution here.
*  The paper we're going to talk about was sent to me via Twitter.
*  Tim on Twitter suggested that I cover this paper and have you on the show.
*  So thanks, Tim.
*  Thanks, Tim.
*  And actually, something actually useful came from Twitter.
*  Imagine that.
*  Okay.
*  So, a critique of pure learning, what artificial neural networks can learn from animal brains.
*  Is it bio archive?
*  Yeah, I put it on bio archive.
*  Bio archive.
*  For now.
*  So let me see if...
*  For now, it's under review.
*  So hopefully it'll be in a referee journal at some point.
*  Okay, great.
*  So let me see if I have the take home right and then you can correct me.
*  So over evolution, DNA provides a massive amount of inherent learning that manifests
*  as the wiring principles of our brains and thus sets up a massively pre-trained system
*  essentially that we can then learn on top of during our lifetimes.
*  Whereas any current deep learning or AI system, supervised or unsupervised, suffers from having
*  to learn everything from scratch.
*  So in broad strokes, is that accurate?
*  What am I missing there?
*  In broad strokes, that's right.
*  Part of the...
*  The goal of the paper was really to point out to people who work in machine learning
*  that much of what they call learning would not, to a biologist, seem like learning.
*  A lot of it came from miscommunications that seemed to arise because people in different
*  fields use words in different ways.
*  It was my attempt to lay out cleanly what I think most biologists would agree is happening,
*  most neuroscientists would agree is happening in real organisms, namely that most organisms
*  come with a great deal of innate capacity to perform well in the environment.
*  How much that's in contrast with how machine learning people see what the problem is,
*  the intellectual problem.
*  So usually the problem formulation, at least traditionally, starts with a tabula rasa network.
*  And from an evolutionary point of view, it would be insane to not build in structure
*  if it were possible to do so.
*  If you have two organisms, one of which comes out of the box, born with the capacity to
*  navigate the environment effectively, and the other has to learn everything from scratch
*  each time, if it were possible to build in stuff innately, that organism would be selected
*  for.
*  And in fact, I would argue that that is what happens.
*  So that's really the core idea behind the paper is trying to sort of clarify for both
*  communities how they formulate the problem and to recognize that a lot of what is called
*  learning in the machine learning community would not be considered learning in the neuroscience
*  community.
*  This is an ongoing issue, I think.
*  Even calling artificial units neurons is problematic just in a conversational way.
*  It's difficult.
*  Indeed.
*  Indeed.
*  In fact, my thesis, my PhD thesis was on trying to understand the ways in which actual biological
*  neurons differ from the summation units of neural networks.
*  My thesis was on dendritic processing in real neurons.
*  Yeah.
*  Well, okay.
*  There's a lot to sort out moving forward in both fields or the crosstalk between the fields.
*  Yeah.
*  Okay, so Tony, I mean this in the best way possible.
*  You're a rodent guy, meaning that you've studied auditory decision making in rodents and sensory
*  processes.
*  In the paper, you argue that if we figure out mouse-level AI that essentially will be
*  right super close to human-level AI.
*  How is that?
*  Do you want to just expound on that idea for a moment?
*  Why do I believe that?
*  Yeah.
*  You're asking why I believe that.
*  Why do I believe that if we could just get to mouse-level AI, we'd be a short step away
*  from human-level AI?
*  Is it for grant funding is my question.
*  No, no, no, no.
*  There's plenty of stuff that I do for grant funding, but this actually is a fundamental
*  belief that is why I study decision making in rodents and for example, not in spiders,
*  but on the other hand, not in people or monkeys.
*  It's why I chose rodents.
*  So basically, my argument is an evolutionary argument that animals have been on this planet
*  for of order 500 million years or so, depending on exactly where you draw the line for animals,
*  five, six, seven hundred million years.
*  Vertebrates have been around for 400, 500.
*  Mammals have been around for about a hundred million years and they represent, you know,
*  over that time, there have been something like Avogadro's number of individual animals
*  that evolution has operated on.
*  99.9% of which are gone.
*  99.9% of which are gone, but if you formulate the problem right, even the ones that didn't
*  make it have to be considered when you think about how the ones that did survive, what
*  they have extracted, like how much of the space has been sampled of the space of all
*  possible networks.
*  Really, there's been a tremendous amount of evolution to get to vertebrates and to
*  get to mammals.
*  And the reason I'm focusing on mammals is that mammals all share what I consider to
*  be the fundamental advance that enabled human intelligence, which is the neocortex.
*  So we've had the neocortex for about a hundred million years.
*  And you know, our cortex, as far as we can tell, the basic principles are not very different
*  between a mouse, a primate, and in particular, a human.
*  It took, you know, the difference between our primate ancestors and a modern rodent.
*  You know, probably we have to go back more than 10, 20 million years to see really big
*  differences.
*  And so, you know, the things that really make humans special in terms of their apparent
*  intellectual prowess, those things came in the last few million years.
*  And you know, I started off in linguistics, so I'm particularly impressed by our ability
*  to do language.
*  And that, you know, depending on whether you think Neanderthal had language or not, probably
*  emerged in the last couple of hundred thousand or million years.
*  We know that our closest primate relatives currently can't master language.
*  So whatever that evolutionary jump was really very recent.
*  And, you know, the primate population sizes were pretty small.
*  So we're talking not very much evolution to get us from a neocortex to a creature capable
*  of human type intellectual functioning.
*  And so that's why I believe that the hard step is to get to the general purpose cortical
*  operation that rodents are capable of.
*  I say rodents, I mean, we could could easily have done cats or dogs.
*  It's just that rodents are the common lab species, tractable lab species for studying
*  these things.
*  You saying that I can't wait if it is that recent of a step in that small of a step to
*  get from our symbolic like processing or to our symbolic like processing.
*  I can't wait to see what's what's next for us evolutionarily.
*  Right.
*  What our cortices are capable of.
*  Yeah.
*  Although it's not clear where these, you know, any particular strategy asymptotes.
*  Right.
*  Right.
*  So there's this, you know, those who believe in the singularity think that, aha, as soon
*  we get to to human level intelligence, we'll quickly surpass it.
*  Right.
*  But it's also possible that this kind of strategy tops out after something a little bit higher
*  than human intelligence.
*  You need a fundamentally different strategy that we can't get to using these types of
*  approaches.
*  Proof that we're at the tip of the evolutionary arrow, right?
*  We're the cream of the crop.
*  Supervised learning, the main type used in deep learning these days that's kind of associated
*  with what the A.I. explosion is not enough to explain how we learn from early childhood.
*  So for example, kids don't need a million examples to learn what a car is, for instance.
*  Right.
*  Exactly.
*  And one suggestion, as you note in the paper, has been maybe that kids are built in with
*  this powerful unsupervised learning system really early on.
*  And that can then give way to a supervised learning type system later on.
*  You suggest that an early unsupervised learning system in the early in the developmental process
*  is not enough to explain the behavioral skills of young animals and humans.
*  And you give a lot of examples about how many of our learning skills are innate.
*  Right.
*  There's a possibility that the maximum absence of evidence is not evidence of absence could
*  be in play in this case.
*  Or do you think that it's just too wide of a chasm to imagine an unsupervised learning
*  algorithm that is powerful enough that could get kids on the right track, you know, animal
*  kids and children kids on the right track early enough?
*  Well, so in some sense, if you divide learning into supervised and unsupervised, and we agree
*  that the learning that is required for a child to learn language is not supervised, then
*  that only leaves unsupervised.
*  So in some sense, it must be the case that unsupervised learning is responsible for learning
*  things like language or categories.
*  The question isn't whether it's unsupervised learning.
*  The question is whether to my mind is whether it's a general purpose unsupervised algorithm
*  that could learn anything in a comparable amount of time.
*  And my belief is that it's not a general purpose unsupervised algorithm.
*  It's some unsupervised learning on top of a great deal of innate structure that we are
*  born with because of evolutionary selection.
*  So the hardest place for us to see that at work, I think, is in humans, in children.
*  It's easy to see why one might believe that humans rely on a tabula rasa unsupervised
*  learning approach because humans are so helpless at birth and then they take years to get up
*  to speed.
*  But we are, I don't believe, because I'm a neuroscientist and a biologist who believes
*  that we are just an incremental step away from the creatures from which we evolve, I
*  think the idea is, my approach anyway, is to go back and look at these earlier creatures
*  and say, well, does that also, could that really explain what's going on with these other creatures
*  like rodents or spiders?
*  So if we go back to insects, insects are born basically ready to go.
*  And fish are born with a great deal of innate structure ready to go.
*  That's not to say they function absolutely perfectly.
*  No, there's a little fine tuning that needs to go on.
*  But for the most part, they're not spending three years getting up to speed with their
*  environment before they're ready to reproduce.
*  They've got hours, days, or usually at most weeks before they're let loose in the environment.
*  And so to my mind, that is the argument that there has to be a great deal of innate structure.
*  There's other arguments too.
*  There are some cases where creatures do things for which they have zero examples, not one
*  example, but zero examples.
*  So there are a great number of innate behaviors that are really innate, at least portions
*  Do I have this right from, did you use the squirrel jumping from branch to branch in the paper?
*  Squirrel jumping, you know, I haven't studied squirrel jumping, but I imagine that they
*  take small jumps and then larger jumps.
*  No, but for example, burrowing behavior.
*  Burrowing, yeah, there you go.
*  So burrowing behavior, there's this fantastic work by Hopi Hoxtra at Harvard who studies
*  different species of a rodent called Paramecius that depending on the exact species, they
*  build very different nests, very different burrows.
*  And some are long and complicated and have a bunch of side pockets and some are shorter.
*  And they all have characteristic shapes.
*  And these are built in to the hardware.
*  These are innate in the sense that if you take a pup from one strain that builds a complicated
*  burrow and let it be reared by a mom from the other one, that pup will grow up and build a complex,
*  not a simple burrow.
*  In other words, it builds the one that its genetics endowed it with, not the one that its mom would build.
*  And so how do you encode stuff like that in a genome?
*  Well, you can imagine how you might do that.
*  But that's just a potentially experimentally tractable example of a huge number of innate behaviors.
*  And so to my mind, if you believe that there are things that can be inscribed into your behavior by genetics,
*  then I think there's a strong argument to be made that evolution would select for as many of those as are useful.
*  And, you know, if you can build into my nervous system a way of learning languages more quickly than my competitors or more effectively than my competitors,
*  I will outperform.
*  There'll be selection pressure for my offspring to thrive.
*  And so really, the question to my mind isn't whether it's possible to put these things into the genome, but rather, why is it that in humans,
*  some of them, some of that innate stuff was left out or so much of that innate stuff was left out.
*  And I think the answer, of course, is that there's a trade-off.
*  The more innate behavior you have, the less flexibility you have to deal with new environmental situations, new environments.
*  And so we as humans have sort of are probably as far away from maxing out on what's innate as any creature in the animal kingdom.
*  But that said, we're still mostly innate.
*  That's an interesting dynamic and, you know, losing the innateness to grant other abilities.
*  But we'll hold off on that for now.
*  So you distinguish between supervised learning in the paper for artificial neural networks and what you call supervised evolution.
*  I mean, this is along the same lines of what you were just talking about.
*  So what do you mean by the term supervised evolution?
*  Yeah, so that was just an attempt to be a little bit provocative.
*  Yeah, worked.
*  To say that, to think about what goes on in a supervised learning network as supervised learning is no more accurate than it would be to call it supervised evolution.
*  This supervised process is a really useful way for us as people building technology to get the network to do what we want,
*  to find the network structure, the network weights that achieve some objective function.
*  And that's fantastic. It's way more efficient than what I would say is likely to be the dominant way that evolution comes across it, which is basically a random walk.
*  Right. So evolution has the advantage of being able to operate on Avogadro's number of organisms over many, many years.
*  Like a genetic algorithm.
*  Yeah, exactly. Like for the most part, people can quibble, but in most cases, genetic algorithms are not as efficient as gradient descent.
*  But apparently evolution, for a variety of reasons, evolution didn't use supervised learning.
*  The problem formulation is not well adapted to the real challenges to the problems that biological organisms face.
*  So it's fine that we use supervised learning.
*  It's fantastic that people have figured out how to accelerate the process of finding the right weights in a network to solve a problem.
*  That's fantastic. Right. But that doesn't correspond, in my opinion, to learning.
*  It's just a trick for finding interesting network structures that solve problems.
*  And so we could apply that same approach to, quote unquote, evolution.
*  And we could, you know, evolution in the lab and we could call that supervised evolution.
*  And, you know, had the history of the field been different, had it been evolutionary biologists who figured out how to do what we now call machine learning, we might very well call it supervised evolution.
*  I can't wait for the first supervised evolution lab. Exactly. By a future PI.
*  So, you know, could or should DNA through evolution then be considered a mechanism of information compression?
*  Exactly. You know, or like a bottleneck of information to accommodate such vast amounts of data?
*  What's going on is biological organisms have to.
*  Compress everything they know and where I use knowing quotes about the structure of the network that they're going to build into the genome, they have to pass network structure through what I would call a genomic bottleneck.
*  And that's just a fact.
*  You know, everything, you know, because every organism arises from a single cell with one genome, everything about that organism's network structure has to come out of that genome.
*  And so that genome encodes a series of rules for construct wiring up a network.
*  And, you know, those rules, which could, by the way, be use dependent, some of those rules can be used, dependent are the rules that provide us with the brains that we then walk around with.
*  So I think that that passing the network structure through a genomic bottleneck actually acts as what in machine learning might be called a regularizer.
*  It requires sort of boiling down the most useful network motifs into a relatively short description length.
*  And then that sort of rigor, that constraint actually requires that really it's the most interesting network motifs that get passed along.
*  And I think really it was, you know, it took it took a long time, but eventually the one of the most fruitful network motif.
*  Was the cortex.
*  So the neocortex is, I think, you know, the brilliant result of many, many hundreds of millions of years of evolution.
*  That's interesting. I had Federico Turcheimer on the show this past episode, which hadn't aired yet since I've talked to you.
*  But one of the points that he makes in his work is how the brain, both functionally and anatomically, is fractal in nature, right?
*  Looks the same on multiple scales.
*  And it just struck me that thinking about DNA as a bottleneck of information, I cannot remember the name, but there has been recent, fairly recent work on the on deep layered networks like the kind that are used to mimic layers in the brain, right?
*  And how these can be thought of mathematically as information bottlenecks from one layer to the other to the next in compressing the information.
*  And I wish it escapes me who that work was done by.
*  I'll look it up after the show.
*  Anyway, just an interesting side note that could the DNA algorithm toward cortex and all the layers in between be fractal in nature?
*  Whether it's fractal, yeah.
*  I mean, the there's the information bottleneck idea, right, which which goes back to Palletishby and Bilbiolik, I think, in a series of papers, probably starting around the late 90s.
*  And the idea that by compressing information down, it's sort of a generalization of the idea of the autoencoder that by compressing information down,
*  if you if you send it through a compressed layer, what comes out the other side if you if you play your cards right is only what's useful.
*  Yeah, it's forcing what's useful. Yeah, exactly.
*  A principle of the universe, perhaps.
*  Yes. No, I think it's I think that that's exactly the principle that evolution exploits as an interesting side point.
*  You know, you might think, well, given that you have to pack everything you're going to have about the brain network into a genome, you might want to pack more.
*  And the way to do that would be to expand your genome.
*  Yeah. And turns out there are organisms that have genomes that are 100 times larger than than the human genome.
*  And so there's no biological constraint that says we're limited by the actual size of our genome.
*  And so, interestingly, the fact I would say that the fact that our genome isn't 100 times larger than it is,
*  is an argument that it's advantageous to compress down the wiring diagram into even a tiny fraction of our existing genome.
*  Because if it were useful to use a bigger genome, that would apparently not be a fundamental problem to for biology to solve.
*  For biology. But but let's say that we're somehow able to decode the pre-trained information that is in the DNA in a way that gives,
*  you know, like deep learning the same sort of start that an animal has upon birth, right, in some sort of network.
*  I mean, could we actually be limiting ourselves and thus our AI systems by the constraints that are compressed, encoded into biological DNA and into the innate learning?
*  Does that make sense?
*  Well, I guess the way I would say it is this.
*  If we consider the set of all possible networks, right, that's a pretty big space to to wander through.
*  So in modern deep, you know, in the modern era of deep networks, we have already sort of constrained ourselves to a subset of all those.
*  So even if you take a deep network that has millions of parameters, they're not organized willy nilly.
*  They're organized in a particular structured way.
*  Right. I mean, hence the term deep networks, layer after layer, and the layers of characteristic property.
*  So we're already imposing some structure.
*  And, you know, there's, I think, a lot of theoretical work going on right now trying to understand why that particular structure is a useful one.
*  And, you know, people have some ideas and I think they don't fully understand why.
*  But it turns out that somehow those kinds of networks are well suited to learn the kinds of things that you might want a network to learn.
*  And they're particularly trainable in small numbers of or relatively small, smaller numbers of samples than networks of other structure.
*  So it's quite possible that there exists at least so far in the absence of theoretical results to the contrary,
*  it seems possible that there exists somewhere in the space of all possible networks, ones that are even better.
*  But I would argue that rather than looking through the space of all possible networks,
*  why don't we sort of take our inspiration from the networks that we already know can solve the problems of interest?
*  Spoken like a true neuroscientist.
*  Well, so as you note in the paper, transfer learning or the ability for a neural network to be trained on one task and then transfer its learned skills,
*  let's say, to a new task, that's an active area of work in artificial intelligence these days.
*  But this is very different from the way that DNA gets transferred from one generation to the next through time.
*  So can you just comment on that and talk about how?
*  Yeah, I think the big difference there is that in transfer learning, at least as I know the field,
*  the amount of information that one might use to transfer to the new network is not constrained.
*  So you can use as much information you can basically the sort of naive way to do transfer learning is you just take the weights that you trained it up,
*  strip off the last few layers and then you initialize the network to the weights of the first end layers of the network.
*  And that's a lot of information.
*  And so that I suspect that that will work for a smaller class of problems than the more general solution,
*  which is, again, to boil down the key aspects of that wiring diagram through something that is a bottleneck, the genome.
*  So I would say that sort of conceptually, they they share some inspec that you you might not want to relearn everything from scratch every generation.
*  But I think biology actually has turned what at first blush might seem to be a constraint into a feature,
*  which is that it has to abstract the key aspects of that wiring diagram and and and fit it into a small bit of a genome.
*  And in fact, it has to do so.
*  You know, what comes out of the genome, of course, at least in in creatures,
*  in most creatures is not a detailed wiring diagram of the form, you know, wire neuron one to neuron three, seven, nine and two billion, but rather a set of rules.
*  And so by forcing it through a genomic bottleneck, it it sort of asks us to to look at what kinds of wiring rules would be effective for that that wiring.
*  Right. Like like the the nematode, as you point out, has its connections are actually completely instructed by the DNA, whereas maybe humans and mammals.
*  This could be the DNA evolution's test on, you know, let's take it from a complete wiring diagram to just some rules and some algorithms,
*  suggestions. And so we're seeing how that test is coming along.
*  Yeah, so here I am again, Tony.
*  I've asked this question multiple times in the past to many guests here, but I've asked it with neuronal properties in mind and anatomy in mind and biophysical properties in mind.
*  And now I'm going to ask it with the DNA in mind.
*  How biophysically accurate, how biologically accurate in the details are we going to eventually need to be to build an AI that will,
*  you know, to make an AI that will work on the level of, in your case, let's say a mouse.
*  I so my day job is being a neuroscientist.
*  So, you know, as part of my day job, I care deeply about all those details.
*  Right. I, you know, as I mentioned, as a graduate student, I did I made models of processing and single neurons, dendritic processing.
*  As a postdoc, I looked at the nuances of synaptic transmission.
*  And and now as a PI, I study neural circuits.
*  So I care about those details intimately, but I don't believe that there's only one solution.
*  So I don't believe that the solution that will allow us to build an intelligent machine will necessarily involve single units that have dendrites and particular complements of calcium and sodium channels arrayed in just the right way.
*  The reason I study the details is so that eventually I can get to the underlying principles, abstract them away and then say, ah, what's important about all those details is X, Y and Z.
*  Right. And so my belief is that almost none of the biophysical details will be important.
*  The problem is that without at least the only way I know how to figure out which details are important is to understand in.
*  Actual neuroscience settings, how those details work together to enable behavior.
*  So once we understand what's going on in a biological system, then we can abstract that stuff away and say, no, no, no, no, no.
*  What's important is not the calcium channels, et cetera.
*  What's important is X, Y or Z.
*  So, you know, over the course of thinking about this, I've had different opinions about what really is important.
*  Right.
*  And, you know, as a graduate student, I thought what was most important was that the simple processing units that are used in artificial neural networks are too simple.
*  And by the end of my graduate work, although I had a lot of fun learning how individual neurons worked.
*  I concluded that, OK, really, it's not a qualitative difference.
*  Sure, an individual neuron does something more complicated than a processing unit.
*  But by that, you could really just replace one individual unit with or one individual neuron with maybe a dozen units and you're done.
*  So in that sense, there's there's no deep thing missing.
*  It's just maybe it'll take 10 times as many simple units as neurons.
*  OK, what I ended up concluding was that what is fundamentally different is that actual neural networks in the brain, real networks of real neurons have highly structured connectivity.
*  You know, it's it's sparse and the neurons are wired up in very specific ways.
*  And that really, it's just what endows a brain with its capacity is the wiring diagram.
*  And so that is how I got to from studying pure decision making to trying to understand at the level of the actual wiring diagram, how those decisions are made at the level of which neurons are connected to which other neurons to produce this neural activity.
*  So, man, there's so many different ways we can go from here because you're doing some really great work with connectomics and just what we're talking about.
*  Maybe before we get there and I can't take I can't take all of your time for the day, but just thinking about levels, these levels of understanding and what it takes.
*  I had John Crackauer on the show maybe a month or two ago, and I don't remember if we talked about it on the show or I had the opportunity to have beers with him beforehand.
*  And I don't know. I don't remember if it was over beers or on the show, but he made the point.
*  Sort of his outlook is that when you can use brain circuitry and brain activity, neural activity even sort of as a check on the validity of of our understanding of higher cognitive functions and like our hypotheses for how these higher cognitive functions work, let's say.
*  But you don't need to really understand these lower level phenomena. You don't really need to understand the circuitry, the wiring diagram, the spike rates of all the neurons, for instance, to understand the higher cognitive functions themselves.
*  So do you think the understanding the constraints imposed by DNA and then the connectomic, the connectome, the wiring diagram will improve our understanding of the mental or psychological higher cognitive, I'm doing air quotes right now, functions that we call our cognition?
*  Yeah, so so obviously I wouldn't be doing what I do if I didn't believe that.
*  But you could be doing it because it's interesting in its own right, you know.
*  You're right. I could be. So you're right. It's not obvious. In my case, I think if we went back to the starts of our careers, we would probably find that we were interested in understanding the same fundamental questions.
*  You know, how do humans think? Yes, I just concluded that the way to get there was to understand the circuits at a really low level, because those are tractable.
*  It's again the trade off between really interesting questions and what to my mind are satisfying answers. So I have there was just no question that you could get satisfying answers to questions about how one neuron drives another neuron to fire.
*  How do synapses work? And potentially, I can tell you what the form of the answer is for what a wiring diagram looks like.
*  Right. That's well, well defined. And I can tell you whether or not I got in principle, whether or not we got the right answer. Right. It's hard. I might not get there, but at least it's really well defined.
*  And so I would say that the the argument that we can just sort of look at the top level of cognition, I push back on that because there is a name for the field where people look at that sort of top level.
*  And traditionally, that is psychology. Right. The very top level where you look at human behavior or you look even at animal behavior without trying to pry open the black box.
*  That's psychology. And that is you. I believe you can only get so far without opening up the black box.
*  I don't think that people today are that much smarter than they were 50 or 100 years ago. Yeah, I don't think we're that much better at designing experiments so that we can expect without sort of something new to make progress on that.
*  And this actually so he wrote a very provocative and controversial piece. I think it was in Neuron John Cocker did a couple years ago, maybe two, three years ago.
*  This is what we talked about when he was on the show. Yeah. Yeah. And, you know, it made a lot of points. And I was sympathetic to some specifically that one can't forget about behavior.
*  But the idea that one can only look at behavior or maybe use neuroscience as a check afterwards makes no sense to me.
*  Yeah, that's not what they argued in the paper, really. So I'm speaking for him and I shouldn't be.
*  Okay.
*  But but I think their point was just that it needs more behavior to be more inclusive of behavior. But yeah, we don't need to realize as someone whose labs, you know, spent the first maybe five years along with my close colleagues, Zach Mayne and figuring out how to train rats to perform the kinds of tasks that previously people had only trained nonhuman primates to perform.
*  I'm very sympathetic to the idea that one has to study behavior very, very closely. Yeah. But my belief, which I think is actually at odds with at least how I read that paper, is that that's not nearly enough.
*  And that the way that in general science and biology in particular, and neuroscience even more in particular, move forward is with new technologies.
*  And so having a well controlled behavior provides an interesting object to study in the right way. But the tools with which we study it, those have to or or it would be it would be foolhardy to ignore the fact that we've made tremendous advances and how we can study single neurons populations of neurons, how we can manipulate them and channel red ops and the whole optogenetic revolution.
*  To not use those tools would be a mistake. And there's a whole other discussion. I'll just make an argument. I'll throw out this argument that actually the history of science is really the interaction between scientific questions and technologies.
*  So if you go back to almost every major discovery that I can think of in neuroscience, where I know the history pretty well, it was enabled by a technological advance that preceded it.
*  So my favorite paper in all of neuroscience, the Hodgkin-Huxley papers, right, involved the voltage clamp.
*  Yeah, the development of the voltage clamp, which was developed by Casey Cole and taught either Hodgkin or Huxley a few years after he developed it. And that in turn required the development of tubes that were capable of enabling a feedback amplifier, right?
*  So you can trace a direct line from something from electrical engineering and electronics to the Hodgkin-Huxley equations. You can do a similar thing with single channel recording, low noise amplifiers that were sufficiently low noise that you could resolve single channel.
*  And you can go on and on to photon, etc, etc. So all these advances that enabled us to study things we couldn't previously study came from technology. But that's a whole other.
*  Yeah, it is. I'll just have to have you back on the show. So, so in my experience, and you've talked a little bit about this, and I fought against this and my experience in science in academia, is that people often come in with the big questions, you know, what is consciousness and things, but then knowledge ruins it, you know, we learn that we don't even understand the processes that are underlying the processes that we think are associated with the big questions.
*  That's right.
*  So the idea that you develop in the paper, it's not exactly reductionist. So my point is you people in their careers tend to end up studying sort of lower level processes and then lower level. And that tends to be the trajectory.
*  Yeah, of what you know, and then you're interested in it too, because you think, oh, it undergirds the higher level processes. But then, you know, 20 years later, you're studying electrons or whatever, you know, that's right. Yeah.
*  So, so the idea that you espouse in the paper with DNA, it's not exactly reductionist, because it gives DNA essentially a higher order role in intelligence, right? But one could go off the deep end here and say that, well, DNA is made of nucleotides, and it's under the rule of, you know, principles of entropy and, you know, metabolism and so on.
*  We could look at that level and say, actually, you have to consider not just the whole of life before us, which evolution encompasses, but the whole of existence as the innate intelligence that we start off with, maybe from the Big Bang, you know, is that just too crazy of an idea? You know, why is DNA the right level to zero in on here?
*  I'm not saying that. Okay. So at one level, what you're saying is right. And, you know, you can sit there stoned in your dorm room wondering.
*  Is it okay if I light up real quick while we talk? Yeah, exactly.
*  You can sit there stoned in your dorm room wondering about the deep questions. And, you know, that can paralyze you or at least entertain you for as long as you like. But operationally, right, there is in my mind, to my mind, a reason for stopping at the level of DNA of recognizing that the genome
*  actually, conceptually plays an important role in this whole process by acting as a bottleneck to the transfer of information about the circuit from one generation to the next. To my mind, that's all we need to know sort of at the abstract level to sort of move forward on this as a theoretical question. Now, as a practical question, right,
*  there are developmental neuroscientists who study the process of going from DNA to a wiring diagram, right? Right. And I happen not to be one of them. I think it's an interesting field. Yeah. Right. Yet.
*  But sure, that is in the actual experimental science. That's what one would study, right? One would choose to study how you go from DNA to a wiring diagram. That's developmental neuroscience. But and there are certainly some insights from that that might guide ones thinking at the theoretical level for how to build a network through pass through some kind of a bottleneck.
*  But the way I look at this is you look to the biology for inspiration, and then you take your best shot. Right. And that that's actually what the field of neural networks did. Right. Like, if you look at what happened, right, as you made the the transition from symbolic AI to neural networks to the first
*  generation of neural networks, right, symbolic AI basically involve people thinking, introspecting and thinking about psychology without thinking about the all those nasty details that are inside that, that black box. I don't blame them, right? If I, if I'd come on the scene in the 1950s, there's no way I would have been suckered into working on neurons, because that was clearly going to be a long haul. Right. So if there was this promise that you could just, you know, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a computer, you've got a
*  brain, you've got a brain, I can look at your brain, you know what, I could, I can just figure it out and just write down a program. Sure, right? Why not that that's clearly, it was an obvious thing to try. And at least, you know, I suspect that had I been around back then, I would have kept trying it and retired after not having figured out how the brain work. But by the time I got to the scene, it seemed pretty clear to me that the symbolic approach wasn't going to work. And so there was this generation
*  of one simple level of abstraction of how the brain works that was built into sort of neural networks, right, a simple processing unit that takes inputs from a bunch of other neurons and produces an output. And I gotta say that that's, you know, given what people knew about how neurons work back then, it wasn't bad for sort of an abstract, abstract abstraction, it wasn't bad for an abstraction, but it missed some stuff, right?
*  And now, 50 years later, we're sort of talking about, well, out of all the many, many things that missed, which of those were important? Yeah, or or any of them important? Was that enough? Yeah. And so my my own belief is that you can keep, you should keep going back to the neuroscience and ask, okay, given what we know today, is there anything that we can we can use to sort of guide the next
*  generation? And there are some clear successes there, right? So convolutional neural networks were explicitly inspired by looking at Hubel and Weasel type receptive fields, right? Yann LeCun was like, inspired by that, right? And he he thought about it and then abstracted it really nicely. He didn't slavishly build center surround receptor, or, you know, edge detecting receptive fields. But he was inspired by that. Right? And if you look
*  at sort of the work in reinforcement learning, again, people were inspired by the biology of reinforcement learning. That's been a great example of a field. The people who study reinforcement learning in neuroscience are talking to the people who are exploiting reinforcement type learning ideas to build better algorithms. Those people are talking to each other all the time. In many cases, it's some of the same people.
*  Well, that's one of the examples where the biology and the artificial neural AI really map onto each other well.
*  That's right. Yeah. Yeah, that's been a huge success.
*  Any, any reactions that you've had to the manuscript that stand out that have, you know, been either really positive or have kept you up at night?
*  Well, I would say that I circulated that manuscript around to a bunch of friends and colleagues. And so the early drafts of the manuscript elicited some really strong negative, mostly negative responses. But from friends who that's kind. Yeah. Yeah, it was fantastic.
*  From a bunch of colleagues, mostly from the machine learning community, who thought I was saying things that I wasn't saying or didn't mean to say, and who also didn't necessarily share my intuitions. And a lot of what this paper was, was laying out the basis for where my intuitions come from.
*  I see examples of innate learning in animals, for example.
*  So I would say that a lot of the feedback that I might have gotten after I released the paper were sort of encountered earlier, anticipated, and then sort of cause major rewrite. So I've, I've rarely rewritten the paper as extensively as this one in light of feedback, just because I was really trying to reach out to a community.
*  And it was useful to figure out why they rejected what I was saying. So I don't think I convinced anyone, but at least I think they understand now what I'm saying.
*  That's called progress.
*  Yeah. So at least we're, we're, we're using words more or less the same way, or at least I'm explaining how I would like people to use words and explaining the differences between how I would say a neuroscientist uses some words and a person in machine learning uses those same words.
*  Well, I hope the result when it comes out in a journal isn't just doesn't lead to a battle of semantics or something, because the ideas in the paper are awesome.
*  It's just really fun to read. And of course, I'll link to it in the show notes, the bio archive version anyway.
*  So thanks for writing it. And thanks for making me think more deeply about about our genetic code as that sort of compressed information.
*  So I'll stop using words because I don't want to use the wrong words now.
*  You know, words are mean whatever people want them to mean. It's just that if you have a large community of people using words one way and a different community using that same word a different way, it's just a setup for misunderstanding.
*  Yeah. Well, so I know that you got to go pretty soon. And so we didn't really get into your fascinating work on DNA barcoding.
*  I will talk about it a little bit in the introduction and point people to it. And then, you know, maybe we'll have you on again at a later time to talk about it.
*  It's really cool work that you're doing. So just a few kind of general questions before you go then.
*  I heard you say in a talk that you had I believe was a graduate student who you you suggested he or she not pursue a certain path.
*  And then they eventually just didn't listen to you and pursued it. And it turned out to work. So do you recognize or do you recommend that advisees not listen to their advisors?
*  More or less. Yeah. So what that's not exactly for me the ideal interaction with anyone in my lab or anyone I work with is that we have conversations until we figure out what we're going to do.
*  And so there are a couple of reasons you can disagree. One is, you know, as simple as you're using words differently.
*  Of course, it's even possible that one of us is just plain wrong about a fact or maybe one of us has the logic wrong.
*  But the most interesting disagreements come from having intuitions that are different and intuitions that are different from what we're used to.
*  And so the most interesting disagreements come from having intuitions that are different and intuitions arise from sort of this nebulous cloud of some of all the experience you've had, you know, all the papers you've read, all the experiments you've done, etc.
*  And your sort of guess as to how an experiment might turn out. And so with so in particular, I was talking about my work with a brilliant former student in my lab, Peter Zemensky.
*  And we when he joined the lab, we agreed on the overall scope of the project. And we agreed that we would have to look at one output pathway of the auditory cortex.
*  And then the since these experiments were really hard, we had to pick which output pathway we have to commit to a pathway.
*  And I was advocating by analogy with work in the in the nonhuman primate that he look at some cortical cortical pathway, let's say from the auditory cortex to the prefrontal prefrontal posterior parietal.
*  And he kept suggesting that we look at the striatum. And I didn't know anything about the straight.
*  And other than that, it was a complicated place and I didn't know anything about it.
*  And he kept saying, So what do you think about the straight? Oh, no, don't do that.
*  And at some point, I think he recognized that I had no logical basis for rejecting it.
*  It was just complete naivete and ignorance.
*  And so he did exactly what he should have done, which is after having considered my arguments and rejected them as unfounded, did exactly what he thought was best.
*  And he came back six months later with fantastic results that subsequently transformed my lab's research program.
*  That is exactly the best interaction between a to my mind between a between two people who work together.
*  Right. He's the one doing the experiment. He's the one who's ultimately responsible for the success of his project.
*  And so, you know, I am somebody who I think could provide best, you know, at worst, the sounding board and perhaps even some insight.
*  But in the end, he's got to take responsibility for it. So he does what he thinks is best.
*  And this is a conversation I have with everybody who enters my lab that ultimately they are responsible for making their project work.
*  And I'll do my best to help them, advise them, discuss with them.
*  But in the end, it's their decision what they do.
*  You have a lot of expertise and a lot of different areas. If you could wave a magic wand right now and just poof, be an expert in something, what would it be?
*  Oh, wow. That's a great question.
*  You know, I'm not sure I even would. For me, the fun is learning something that I'm not an expert in.
*  So if I could just wave that wand, then I would lose interest in it.
*  So that's a really good answer.
*  Right now, I'm trying to learn developmental neuroscience, and it's super exciting because I don't know anything about it.
*  But it turns out it's really interesting and important.
*  So you figure it out. Sum it up and just tell me. I don't need to learn it.
*  Well, yeah. But that's what you think. That's what you think.
*  And that's what I thought, too. And the fact is, as you said, that anything you dive into, almost anything you dive into that smart people have studied is worth studying.
*  Otherwise, they wouldn't have studied it.
*  What is something that you used to believe that you consider naive now?
*  Oh, that's easy enough.
*  I mean, what I did my PhD thesis on, which was the idea that the key thing missing in artificial neural networks was single neuron complexity.
*  I think single neuron complexity is really interesting and important to biology, but I don't think it's the fundamental thing that's missing.
*  I think that what I'm studying now is the fundamental thing that's missing, namely circuits.
*  Of course, I'll probably look back in five years and think that was naive. But right now I'm convinced that that's true.
*  Tony, thank you so much for your time. I know that you have some fun to get to with your kids in the city, so I appreciate your time here and continue the good work, man.
*  Thanks a lot. This was really fun.
*  Go to braininspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements like you hear on other shows.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net.
*  Thanks for your support. See you next time.
*  I'm
*  Searching
*  The
*  For
*  Empty
*  I don't
*  Know
*  You
*  Trust
*  The
*  Like
*  Your
*  Lies
*  You
