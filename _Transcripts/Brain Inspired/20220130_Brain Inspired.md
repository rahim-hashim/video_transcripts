---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4267s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 14455
Video Rating: None
---

# BI 125 Doris Tsao, Tony Zador, Blake Richards: NAISys
**Brain Inspired:** [January 30, 2022](https://www.youtube.com/watch?v=orn7hMTOP_k)
*  The goal of the conference is to bring machine learning and computational neuroscience back
*  together again.
*  A lot of the major insights in deep learning and artificial intelligence came from neuroscience.
*  In fact, you could basically say that almost all of them.
*  There has been a lot of interest in the computational neuroscience community in bringing machine
*  learning and AI back on board.
*  But the other direction has yet to be fully recouped.
*  So that direction of taking inspiration from the brain to build better AI systems is precisely
*  the gap that I think we wanted to fill with this conference and which is arguably still
*  a gap.
*  I mean, I feel like this neuro-AI is as fundamental as physics or chemistry.
*  It's the study of intelligence perception.
*  All of these, there's certainly fads in how you analyze data using neural networks and
*  so on.
*  That's all true.
*  But the fundamental quest to understand intelligence, I don't see how that can be called a fad.
*  This is Brain Inspired.
*  Step right up, folks, and get your tickets.
*  That's right, get your tickets to the NYSIS conference this year.
*  Hello, everyone.
*  It's Paul.
*  This is a conference held at Cold Spring Harbor where the goal, as you'll hear Tony Zador
*  say, is to bring together the machine learning world and the neuroscience world with a particular
*  focus on how neuroscience can help inform machine learning and artificial intelligence.
*  So I had noticed that the deadline to submit abstracts and to get your tickets to join
*  the conference is coming up.
*  Actually, it's January 21st, right after the release of this podcast.
*  So I thought it would be fun to have the three organizers of the conference this year on
*  the podcast just to have a broad conversation about their interests and topics related to
*  the conference and neuro-AI in general.
*  Dora Sau is a new voice on the podcast.
*  She runs her lab at UC Berkeley, and she's interested in how our brains form invariant
*  representations of objects.
*  You could say she's well known already for her work studying face patch areas in the
*  cortex in non-human primates and in humans.
*  Blake Richards is at McGill University.
*  The last time he was on the podcast, we talked about largely his work figuring out how back
*  propagation or something like back propagation might be implemented in brains.
*  And in this discussion, we talked about his more recent interests, for example, figuring
*  out how multiple streams of representations can be combined to help us generalize better.
*  And Tony Zador is at Cold Spring Harbor.
*  And the last time he was on the podcast, we focused on his paper, A Critique of Pure Learning,
*  in which he makes the case that we need to pay more attention to evolution and the innate
*  structures and abilities that organisms come into the world with.
*  And during our discussion, we revisit the ideas from Tony's paper and use it as a
*  springboard to talk about development and learning and how these processes could be
*  considered one kind of continuous optimization process.
*  And in general, we have kind of a wide ranging discussion about many of the issues that are
*  relevant to the NISIS conference.
*  So I encourage you to go to the NISIS website, which you can find in the show notes at braininspired.co
*  podcast slash 125 and consider whether it may be of interest of you to attend this year
*  or another year.
*  Thank you for listening and enjoy.
*  So I thought we would just start not so much by giving an introduction of yourselves, but
*  maybe you guys can talk each about something that kept you up last night that you're thinking
*  about scientifically.
*  I know that there are many things that keep people up these nights, but in the science
*  something that you're working on that's just at the edge of your knowledge.
*  Tony, would you want to lead us off?
*  Sure.
*  Well, so my life is pretty diverse.
*  So what keeps me up one night isn't necessarily what keeps me up the second night.
*  I don't get a lot of sleep at all.
*  But most recently, what has been keeping me up is we've been working on applying some
*  ideas about the genomic bottleneck to reinforcement learning.
*  And we've been trying to figure out how we can compress the networks that we use for
*  reinforcement learning by a couple orders of magnitude and see if that can give us better
*  generalization, better transfer learning.
*  And so there's a lot of a lot of exciting stuff going on there.
*  But that's sort of at the edge of what we can do with that.
*  It seems to be working, but there are some things that aren't quite there yet.
*  So we're pretty excited about that.
*  We're going to come back to that as well.
*  I have questions about that.
*  All right, great.
*  Doris, what kept you up last night?
*  Yeah, I don't know about last night.
*  But the question that I've been obsessed about for a long time now is how the brain
*  solves segmentation.
*  We see our vision is really based on objects.
*  And there must be some way that the brain manages to bind all the parts of an object
*  together and track those parts as they move around.
*  And whatever the code is, it should be fundamentally different from anything that we understand
*  right now, because it has to be a dynamic code.
*  The object becomes twice as big.
*  That code has to expand somehow.
*  Computer vision people use colors.
*  What is the analog of this color label in the brain?
*  So I would give everything to know the answer.
*  And that's one of the big problems we're working on right now.
*  So you're sort of famous for faces, right?
*  Face patch areas in brains.
*  But that wasn't your original interest?
*  Your original interest was objects, and now you've returned to that?
*  Oh, yeah.
*  I got into faces.
*  I joke that it was like this 20-year detour.
*  And now I'm doing back to what I want to do originally.
*  My first experiment when I was a grad student, I set up a monkey from Rye and I showed monkeys
*  pictures of stereograms because I wanted to understand how they represent 3D objects.
*  And then I read this paper from Nancy Kamasher about faces.
*  And it seemed like a fun project that might not work to show monkeys' faces.
*  And that sort of took its own life.
*  A 20-year diversion then, huh?
*  I guess that's how science players work.
*  I hope that they'll come together.
*  When we're discovering this face patch system, it's not really about faces for me.
*  I could care less about faces.
*  There's like one part of the brain that I could have lesion.
*  It would probably be my face area.
*  So I wouldn't be so shy.
*  The face patch system is beautiful.
*  We call this turtle's underbelly.
*  It lets us get at the mechanisms for how the brain represents high-level objects and gives us
*  an experimental handle to all kinds of questions related to high-level object representation,
*  including one of the questions I assume we're going to be talking about, unsupervised learning.
*  How does the brain learn to recognize a face just from a few observations?
*  And I think that's also going to connect to this tracking and segmentation problem I talked about.
*  So yeah, the face patch system is a lot more than just about how the brain represents faces.
*  Is it a solved issue?
*  I mean, there was controversy over whether this particular brain area,
*  speaking of Nancy Kenwisher's work, really is representing faces.
*  Is that solved?
*  Are we done with that?
*  No, it's not solved.
*  I think we do have a lot more insight into it.
*  And one of the insights has actually come from deep networks that came on the scene,
*  I don't know, five or 10 years ago.
*  So for the longest time, Nancy's lab and others had discovered these little islands of cortex
*  selected for faces, bodies, and colored objects and other things.
*  And we had replicated this in monkeys.
*  And it was a total mystery if there was any principle governing how all of these regions
*  are organized.
*  And there was also islands of surrounding cortex that no one had any idea what they're really doing.
*  And so it was this kind of, yeah, it was a big question mark.
*  And there's some sense maybe there is no principle at all.
*  All right, this is what you get.
*  And you get some islands of cortex that represent things that are understandable
*  and other islands that don't.
*  And then deep networks came on the scene.
*  And my postdoc, King-Lei Bao, I'm not going to go through the whole story,
*  but he basically, he did a very simple analysis.
*  He passed a large number of objects through AlexNet.
*  And just did principle components analysis on activations in layer FC6.
*  And then you can just look at the first few principle components and they span an object space.
*  And the amazing thing is that if you look at what's in those different quadrants of that object space,
*  one quadrant turns out to be faces.
*  Another quadrant turns out to be things that look like bodies.
*  And so something clicked.
*  And it's like, whoa, what if all of IT cortex is actually laid out
*  according to these two axes of object space that you discovered with the deep network?
*  And that made a new prediction about a new network that we should find and turn out to exist.
*  So yeah, to first approximation, it seems like IT cortex is actually laid out
*  like an object space and base patches are one quadrant of that.
*  So it's starting to make sense, but I think base patches are also,
*  they also are specialized for bases in a very strong way, right?
*  You just invert the contrast of a base, the cell's response goes way down.
*  And a lot of those things can't be explained by just projection onto this generic object space.
*  So it's still an open question, but we have a lot more insight now.
*  Blake, have you figured out, were you up last night thinking about how face patches get learned
*  in brains?
*  Not specifically, but the thing that's been keeping me up is
*  related to some of this stuff. So one of my big worries right now is the question of how to
*  develop artificial intelligence that can engage in what we call systematic generalization.
*  So that is not just generalization to unseen data points or even data points that might come from
*  a different distribution, but specifically generalization that
*  obeys some systematicity or some rules, as it were.
*  And humans are pretty good at this, right? So you can look at some puzzle,
*  like I can give you some kind of shape-based analogy where say I show you a square,
*  a triangle and a square, and then I show you a circle, a diamond,
*  and you have to fill in the last one and you'll immediately kind of detect the rule above.
*  You say okay, it goes one shape, two shape, back to the first shape. So then you apply it again,
*  and immediately you can get the answer. You don't have to see any data points. It just,
*  the rule makes sense to you right away. And this is actually surprisingly hard to
*  get in vanilla artificial neural networks. They don't show this kind of systematic
*  generalization. And the old school answer to what you needed for that was symbol systems.
*  And that's still the answer some people give. But for a variety of reasons, which we can discuss
*  if we wish, I've come to the conclusion that I think that systematic generalization doesn't
*  depend on the existence of a symbol system or anything like that. It just depends on the
*  existence of separate representations for static object features in the environment.
*  And on the other hand, relations between objects, be it dynamic movement-based relations or just
*  spatial relations or any other kind of relation, you need this distinction between the objects
*  you represent and the relationships between them. And those have to be represented by different
*  systems. And if you have these separated representations, there's some data coming out
*  of a few labs and some preliminary stuff from my lab as well, showing that then if you have these
*  separate representations, you do get systematic generalization. And so then the interesting
*  question for me is how could those separate representations possibly emerge? And this is
*  where we published a recent study showing that if you optimize a deep neural network that has
*  two different anatomically segregated streams and you optimize it with an unsupervised loss to do
*  prediction, you'll actually get kind of segregated representations for static object features and
*  movement or relation features. And so this is a kind of broader interest now for me that ties
*  back into the unsupervised learning question, because basically I'm starting to think more and
*  more that maybe the way we get to systematic generalization in the brain is by having systems
*  that through evolution or learning in the lifetime have been optimized in such a way that you get
*  separate representations for the relationships between objects and the objects themselves.
*  And I think that once you have those separate representations, now you can get systematic
*  generalization. And the reason is actually pretty simple. It's because systematic generalization
*  depends on you having a sense of there being relations that can be applied to anything,
*  no matter what the object is. And so once you have those separated representations for your
*  relations, that becomes possible. Is hierarchy involved here? Or because the way you described
*  it, it sounds like a single level, right? So two representations, and then there's some
*  generalization. But is there a hierarchical structure that you're thinking about as well?
*  I mean, you definitely need hierarchy if you're dealing with any kind of complex high-dimensional
*  input. In principle, I think this same rule that you need separate representations for your
*  relations and your objects in order to get systematic generalization could even apply
*  in situations where you already have simplified representations that don't require any additional
*  hierarchy to get you what you need. But in 99% of the tasks that we would ever want an AI to do,
*  and certainly for everything the brain does, yes, you need hierarchy. Because you don't
*  care about, say, pixel-lover relationships, right? You don't care really about what this
*  and this retinal ganglion cell's relationship are to each other. What you care about is the relationship
*  of, say, where is my face relative to this other person's face, or something like that. These are
*  the sorts of high-level relationships that you care about. And so that requires hierarchy.
*  So I was just reading about induction and deduction and abduction and how
*  humans are so great because we are great abductors, right? We perform abductive inference.
*  Is this related at all to that? Forgive me for the naive question.
*  No, I mean, it's definitely related to this stuff. Because what you could say to some extent
*  is that standard deep neural networks are really good at induction.
*  And I think there's a lot of evidence for that at this point in time. And so both deductive and
*  abductive reasoning are arguably still missing. And indeed, when we talk about systematic
*  generalization, that is precisely related to these questions.
*  So Tony, I know that you hate learning. The last time you were on the podcast,
*  we talked about your paper, A Critique of Pure Learning.
*  You mean me personally.
*  Right. Yeah. You seem incapable. No.
*  No, I gave up. Too hard.
*  So let's talk about the conference that's coming up. Actually, the deadline to
*  apply and submit abstracts is just January 21, I believe. And so this podcast-
*  I believe so. It's coming right up.
*  Yeah. From neuroscience to artificially intelligent systems, NISIS.
*  Got it. Well done.
*  So it's kind of interesting because I mentioned Tony's paper because it is,
*  in some sense, the antithesis of learning. That's not true, obviously. But the rage these
*  days is using these learning systems, artificial neural networks, deep learning networks.
*  And Doris has already mentioned her work with the unsupervised learning. And Blake
*  just mentioned the same. First of all, what's the conference and what's the goal of the
*  conference? And then how did someone who is so anti-deep learning networks come to be one of
*  the organizers? And are you the dissenting voice among the attendees, et cetera?
*  Well, I'll start by saying what the conference is. The goal of the conference is to, in some sense,
*  bring machine learning and computational neuroscience back together again. So a lot of
*  the major insights in deep learning and artificial intelligence came from neuroscience. In fact,
*  you could basically say that almost all of them, all of the major advances in artificial
*  intelligence came from looking at neuroscience. So the very idea of formulating the question of
*  artificial intelligence as the interactions between collections of simple units, which we might be
*  tempted to call neurons, suggests its deep roots. And in fact, interestingly, even the von Neumann
*  architecture, which is in some sense the opposite of neural network type architectures,
*  even that architecture was an attempt by von Neumann, an explicit attempt by von Neumann
*  to model a certain aspect or at least capture certain essential features of how the nervous
*  system works. So if you go back to the technical report from, I think, around 47 or something
*  on the first von Neumann computer, he devotes an entire chapter to comparing how the architecture
*  that they propose relates to that of the brain. And so, you know, convolutional neural networks
*  and the ideas of reinforcement learning, all of these come from tapping into neuroscience.
*  And in fact, in the early days, NeurIPS, which was back then called NIP, was a meeting that
*  drew together both people from machine learning and neural networks and people in computational
*  neuroscience. In fact, they were the same people. I mean, that was the meeting that was like my go-to
*  meeting when I was a graduate student. It was the only place, the only sort of substantial meeting
*  where you could present computational neuroscience. But by the mid-90s, those two fields had sort of
*  diverged to the point where it wasn't really sort of useful to have them as one meeting.
*  And nowadays, I think, most many, at least many people who work in artificial intelligence,
*  have sort of lost sight of the fact that any knowledge from neuroscience was perhaps anything
*  but, if you like, an inspiration or an existence proof. So, you know, to hear a lot of modern AI
*  people talk, the role of neuroscience in AI is comparable to the, let's say, role of birds in
*  aeronautics engineering. Yes, in the beginning, man looked up at flying birds and said,
*  if only we could fly too. But that's where the connection stops. But of course, that's not really
*  true. So the goal of NISIS is to bring these two communities back together and have sort of,
*  get a conversation going again. So that, you know, in the event that the current technologies,
*  the current approaches sort of asymptote at some point, which, you know, incredible though
*  the advances are, I think we still will need new ideas, will sort of provide the foundation
*  for those new ideas in this meeting. If I can add to that too, I think one of the
*  interesting things about the way that it's evolved in recent years is that
*  there has been a lot of interest in the computational neuroscience community in
*  bringing machine learning and AI back on board to kind of do our explorations of the brain.
*  But the other direction has yet to be fully recouped. And so that direction of taking
*  inspiration from the brain to build better AI systems is precisely the gap that I think we
*  wanted to fill with this conference and which is arguably still a gap. Because, you know, if you go
*  to cosine or whatever, you see a lot of deep neural networks, a lot of AI stuff, but they're all
*  addressed at answering questions about the brain. Whereas at NeurIPS, I would say, though there's a
*  growing neuroscience contingent, it's still a very small part of it. And it's by no means
*  the mainstream of the conference. Doris, do you agree with all of that? So you,
*  you know, you were just talking about using unsupervised learning models to inform the
*  neuroscience, which like Blake was just saying, is the general trend of the direction of the
*  arrow these days. But, you know, just from the title of the conference, from neuroscience to
*  artificial intelligence systems, you know, speaks to the arrow that Blake was talking about.
*  Do you agree that, that there, well, first of all, there's lots of things. So what Tony was
*  talking about, the original inspiration, you know, trying to bring that back, do you agree
*  that it went away, that it's that the AI community doesn't appreciate neuroscience? And then also,
*  in your own work, you seem to be, you know, going the normal way, the modern normal way from
*  AI to neuroscience. Do you have aspirations to go to reverse that arrow? Sorry, that's like seven
*  questions. That's a lot of questions. Yeah. So first, I should say, I've never attended this
*  nicest conference before. So I'm super excited. I'm not totally sure what to expect, except that
*  I'll meet some incredibly smart people thinking about this question of, you know, how brains
*  can inspire machines and vice versa. Machines can inform our understanding of brains.
*  I can't, I don't know that the history, you know, people in AI have been thinking the last 10 years.
*  I think some of them have been deeply interested in the brain throughout, right? I think Jeff Hinton
*  has always like, saw himself first as someone who, his goal is to understand the brain. Is that right?
*  Well, 100%. And let me say there, there has always been the remaining core community in the AI world
*  that believes in the need for taking inspiration from neuroscience. The misfits?
*  The misfits and robes? I think actually some of the most influential people,
*  I think it's precisely the most influential people are the ones who do keep paying attention
*  to neuroscience. I mean, clearly, clearly, clearly, clearly cares. I think, you know, so,
*  so the people who have made many of the major advances actually were paying attention.
*  I think that what is lost is for the younger generation. I mean, sort of modern AI has become
*  such a large field on its own that it sort of feels like it's self-contained. I think that's,
*  that's really the issue. It's almost as if one were to, you know, try to make it fundamental
*  advances, let's say in electrical engineering without quite understanding the underlying physics.
*  Yeah. I can, I also, I want to add to that because I think there's a funny dynamic that has come about
*  because of the fact that, as Tony said, the most influential people are the ones who still
*  fundamentally both seek and believe in the need for inspiration from the brain. And that is that
*  there's a large contingent, I feel like, of AI researchers who see themselves almost as like
*  rebels or something like that for articulating the idea that we never need to look at brains.
*  And this is the sort of like the cool thing to say, as it were, for some people,
*  precisely because they see someone like Jeff Hinton or Yoshua Bengio say, oh, brains are
*  critical inspiration for AI. And they're like, no, no, no, that, you know, I'm going to show
*  that's nonsense. These old guys don't know what they're talking about. And so I have many
*  interactions with young researchers. And on some level, their skepticism, I think, is good. It's
*  healthy to be skeptical of what the older generation tells you. But it's always funny
*  for me when I have conversations with some really young people in the tech world. And they say to
*  me, wow, you know, none of this really has anything to do with brains. It's all just matrix
*  multiplication and stuff. Meanwhile, you know, a part of me wants to sit down and say, well,
*  listen up, Sonny Jim, let's let's do a history lesson here and go through the entire process
*  with them. So what's funny is that I think that many AI people have left the neuroscience stuff
*  to the side. And some of them see that as a sort of like bold rebellion against the old guard.
*  Oh, I was just gonna say, Tony, I mean, this also relates very much to your famous essay, right? I
*  mean, you know, we shouldn't ignore these hundreds of millions of years of evolution. Like the brain
*  has figured out so much structure and we should, you know, get a huge leap. We can figure out what
*  those structures are. What are those fundamental structures that enable intelligence? Like it just
*  seems ridiculous to ignore that. Like why? Yeah, absolutely. I mean, like that's what that's what
*  to me. That's what really keeps me up at night. It's the idea that, you know, it's like if we want
*  to achieve faster than light travel, and some aliens plunk down a spaceship capable of faster
*  than light travel, right? We would sit there trying to reverse engineer that spaceship to figure it
*  out, right? So we have that we are surrounded by creatures that have solved the problems that we're
*  trying to solve, not just humans, but animals, simple animals, who are outperforming us, worms,
*  flies, bees, spiders, my dog, rats. They're all outperforming many, many, many things that we wish,
*  we only wish we could, we could build machines to do. And some of them are so simple, and we still
*  don't understand them. It's embarrassing, right? We, there's this, you know, this great cartoon of
*  a bunch of Lego pieces, right? And it's just an empty box and like, ah, okay, we, we have everything,
*  we just need to figure out how to put them together. We know so much and yet we don't quite know how to
*  put them together and in the appropriate, meaningful way. So that's what that's what, you know,
*  it's just such an obvious source of not just inspiration, but specific guidance.
*  Exactly.
*  When I was in graduate school, actually, like, I think it was one of the first, it was a summer
*  course at MDL that I was at, you know, people were staying up late and drinking and, you know, one
*  very senior neuroscientist, respected neuroscientist was talking about how, you know,
*  we were on the brink of understanding how the brain works. And he started prophesying the coming
*  of the, he basically started prophesying the coming of the Messiah of neuroscience, who would,
*  who would, you know, sort of reveal the truth to us. And, you know, maybe he had a,
*  he was, he had a little bit too much alcohol on board. And so he was, you know, personifying it.
*  But I think many of us feel like we're just on the brink. Like, if only somebody could explain to us
*  what we're missing, right? And some of us maybe even would have hoped to discover that missing
*  thing. It's just so frustrating that we know so much and we don't quite know what we don't,
*  what, you know, that missing piece. Yeah, I mean, yeah, Blake was talking about this factorization
*  between relations and, you know, what the object properties, right? And so that reminded me, I
*  didn't know this, how you think about Blake, but, you know, when you try to generate invariant
*  representation, you kind of, you know, on the one hand, you're saying that this thing that's
*  transformed is the same. So you're extracting those invariant features at the same time. You
*  want to know what that transformation is, right? Did it rotate? Did it expand? And so I think that,
*  I, you know, I think a lot of the structure that's somehow built in through these, you know,
*  this genome that's specifying the wire diagram is to extract the 3D world, right? That the geometric
*  aspects, like how things transform, like being able to deal with that. Because once you have that,
*  then you can, you know, do unsupervised learning, all of that, right? Because you can track this
*  object and you have like suddenly, you know, millions, billions of training samples for free.
*  So that's my hunch is like a lot of it, like if we can understand that,
*  we'll go a long way. So I really resonate with Blake there. And, you know.
*  One thing I'd say about that, though, and I think this gets at where Tony's essay has influenced my
*  thinking a bit more. And I think is really an important thing to remember when we're talking
*  about inspiring AI with the brain is precisely as Doris kind of gestured out there, these systems,
*  if we think about the visual system for a moment, you know, it has surely been optimized over the
*  course of evolution to engage in exactly that kind of invariant representation for the object.
*  And then you have your representations of the spatial relations and stuff. So the object
*  can rotate and it doesn't look different to you. And this is all built into our genomes. But,
*  you know, because I suspect that there's some of that in animals, the instant they're born.
*  But then on top of that, there's some, a whole layer of supervised unsupervised learning, sorry,
*  unsupervised learning throughout the early life that takes those underlying inductive biases that
*  help us to segregate out kind of constant objects and relations between objects and stuff, and then
*  can do a lot more learning on top of that, so that we can learn really particular features of
*  particular objects. And, you know, this is how a cat moves. This is how a ball moves. This is the
*  nature of, you know, playing with spinning top, etc. And all of those particular relations and
*  properties that hold for the unique objects that evolution couldn't necessarily have known about
*  in advance are what we learn through unsupervised learning. But that's all done on the base of
*  a fundamental, very strong inductive bias to have these invariant representations of constant
*  objects and relations between them in a 3D world. Since you mentioned Tony's paper, we don't need to
*  make the whole conversation focused on this. But so I recently had Robin Heesinger on the podcast,
*  I think it may have been last episode, actually. He's the author of The Self-Assembling
*  Brain. And the way that it's sort of pitted generally is there's evolution, there's innateness,
*  right? So we come into the world and there's the structure, which is encoded in the DNA somehow,
*  right? And then there's learning on top of it. But his argument is that what we are forgetting,
*  which is a impossibly complex myriad of information unfolding, is what he calls it,
*  is that from genes to the connectome, that developmental process is a crucial missing aspect.
*  And he kind of considers it an algorithm from the DNA to the connectome, because our DNA can't
*  specify the entire connectome, right? But then on top of that, there's learning. So do we need to
*  consider development? Or can we really just figure out the right structure and build that
*  innate structure in the connectome, or in the case of artificial networks?
*  I mean, I think it's clear that the way you get... I mean, it's not that clear. It's the
*  sort of way that biologists think about it, that the way you get from a genome to
*  any physical structure is via development. And the observation that the amount of information
*  in the genome is orders of magnitude lower than the amount of information in the connectome
*  implies that there have to be actually relatively simple rules for going from
*  genome to connectome. And those are developmental rules. Now, on top... So some of those rules are
*  going to be like activity dependent. And it's those activity dependent rules,
*  probably, that over the course of evolution, got sort of co-opted and formed the basis for
*  activity dependent learning. In fact, from a neuroscientist point of view, at least from a
*  synaptic neuroscientist point of view, it's sometimes pretty hard to distinguish mechanisms
*  for development from mechanisms for learning. LTP, long-term potentiation, is the leading
*  candidate synaptic mechanism for learning and memory. But in fact, some of the earliest results
*  in LTP were in development. So it's really... There is no sharp distinction from an organism's
*  point of view between mechanisms of development and mechanisms of learning. Some of the very
*  earliest mechanisms of development are clearly distinct. Neurogenesis and things like that,
*  probably, are... And also laying out the basic wiring diagram of a neural circuit don't
*  necessarily depend on activity. But for the most part, learning and development, they go hand in
*  hand in biology and the distinction between them is kind of artificial.
*  Yeah, I would 100% agree with that. And I think that Tony made another really interesting point
*  there, which is that what we call learning is probably a series of other mechanisms related to
*  general developmental properties of the nervous system that got co-opted over the course of
*  evolution and which somehow in mammals and some birds and stuff got linked into specifically
*  things like error reduction mechanisms. And that was what then transitioned us towards what we
*  might call learning and the proper sense of it. The proper sense. So there's a bias right there,
*  right? Well, okay. So here's, I guess, what I would say about where I distinguish learning from
*  other activity dependent properties. And this goes back to work I did in my PhD,
*  where I was doing a lot of work on synaptic plasticity and tadpoles. And whenever we would show
*  changes in the tadpoles visual system as a result of activity dependent processes, people would
*  always ask, well, how do we know that that's not just some program that the genome has built in it,
*  but which needs some activity to unroll? And the answer was always, well, we're going to have to
*  unroll. And the answer was always, well, we look for specifically stimulus-instructed changes.
*  So if you can show that the nature of the changes depend not just on their being activity,
*  but on specifically the stimulus you show the animal. And so if you show different stimuli,
*  you get different results in terms of how the brain develops, then you've got something that's
*  arguably learning, because it's actually reflecting the animal's experiences rather than
*  it being simply a gate that opens to allow for the developmental program to unroll.
*  Blake, I was going to ask you about this anyway. So going off of what you just said,
*  I was curious, and Tony, you brought up LTP and synaptic mechanisms of learning.
*  What your take is on the new dynamical fad where you're looking at manifolds changing and
*  neural activity progressing through a manifold low dimensional space and that learning can take
*  place in the dynamics of the network, that it's not all plasticity based. Are you on board with
*  this story? Well, I'm certainly on board with it. And I mean, I think we've known that for a long
*  time because there are certain types of tasks that you don't need long-term potentiation for.
*  And so therefore it has to be something other than synaptic plasticity on some level. Right.
*  And the dynamics is a reasonable place to start. I think that my favorite demonstration of that
*  was actually a paper from Jane Wang and Matt Botvinick, where they do meta learning in a
*  neural network and a deep neural network. But the meta learning quote unquote is interesting
*  because the inner loop was actually just dynamics of activity. And they show that if you train the
*  network such that the dynamics of activity represent your sort of plasticity in the inner
*  loop, and then you've got your outer loop where you actually change your synaptic connections,
*  you can end up recapitulating a lot of really fascinating experimental evidence related to
*  how animals and people use their prefrontal cortex to solve a whole host of problems.
*  So that's just one example paper and there's been a few around for a while. So I think that trend is
*  gaining steam precisely because on some level there's something really real there.
*  Well, I was up too late the other night and I had the thought that maybe the quote unquote learning,
*  you talked about what proper learning, that the learning that's taking place in the dynamics
*  may not be considered learning per se, but just movement among an inductive bias that's
*  already built in. Right. And that inductive bias is built in through the synaptic connection
*  weights. Right. So it's like we have these capabilities of moving along the dynamical
*  manifold landscape to throw some jargon out there, but we can only move into spaces that
*  already exist. It's not like true quote unquote learning that's happening because
*  we're already set up. We already have those available spaces to visit.
*  Well, what makes that less learning life than any other kind of learning?
*  I think pretty much we can only learn things that we can learn.
*  A quintessential example of things that we can learn, of a thing we can learn is language.
*  And yet, I believe that we have circuits that predispose us to learn language. Now,
*  the details of the specific language we learn depend on the language that we're exposed to.
*  And it's hard to articulate exactly what it is that is common among all languages. But still,
*  I think it's pretty clear we have some, if you like, innate circuitry that enables us to acquire
*  a language very quickly. And there are some slots there, some free parameters that get filled
*  pretty quickly over the course of the first few years of life that allow us to acquire sounds
*  and words and basic syntax and grammar. Also, I would say from the experimental side,
*  there's some amazing experiments being done with BMIs to see the capacity for the brain to learn.
*  I think it's like really, for me at least, it was kind of shocking that you can set up a BMI
*  so like a mouse can learn to control a cursor based on the activity of pretty much like any neuron.
*  An arbitrary chosen set of neurons in some arbitrary piece of brain, they can control
*  a cursor by controlling that activity. That they could learn to do that was pretty shocking to me.
*  And it goes against this idea that you're only able to learn very specific things.
*  But in that case, so just continuing on my late night thought experiment, in that case,
*  couldn't you argue that the mouse already had the ability to make those movements? So it can't
*  explore some completely novel way of mapping. So in my thought experiment, it would require
*  actual changes in the synaptic structure, in the connections between the units. Because you could
*  say that, well, the mouse already had the ability to visit those spaces and already had visited those
*  spaces probably throughout time. So it's not that challenging to remap the population dynamics
*  to that space. Does that make sense? I don't know why I'm arguing about this. This is about you,
*  not me, about you guys, not me. So I'm sorry. To me, it's still pretty stunning. Like you choose
*  like an arbitrary set of neurons, like they, who knows what they're actually coding.
*  And you can just get the mouse to use those the activity in those neurons to control this thing.
*  It suggests something about incredible flexibility, right? You mentioned remapping,
*  there has to be some kind of remapping, and whatever the mechanism is, this has been incredibly
*  flexible. I guess this is a question of how does the brain do this dynamic routing?
*  I tell you, Paul, if you see me at NICES, give me a hug. And if you remember that,
*  you've suddenly made a connection from your face cell representing me to your cells representing
*  hugging. And it's a dynamic connection. That connection has never happened before. How on earth
*  do you do that? But I've not hugged many people, Doris, but I have hugged people. So that's within
*  the realm of my current capabilities, right? Yeah, but to wire it so specific for me,
*  it's like the magic part. And I just want to say something that I think gets at what you're trying
*  to push at Paul, which is, and this ties back to Tony's first answer to you as well. All learning
*  systems are constrained on what they can learn. There is no such thing as a learning system that's
*  not constrained on what it can learn. And in fact, this has been proven mathematically with
*  the no free lunch theorem. If a learning system truly has no prior on what it can learn, it
*  basically just learns everything poorly. So to get good learning, you necessarily have to
*  constrain your system to learn well in certain areas. And in this way, if we show that say brains
*  have certain restrictions placed on the sorts of things they can learn, that's unsurprising.
*  That would almost, it would be more surprising if that didn't exist. And that's where I agree with
*  Doris's point, which is that sometimes it's shocking the things that brains apparently can learn,
*  in my opinion, when it seems like it shouldn't necessarily be something that's learnable,
*  that like, why would we not be constrained to learn that? And, you know, I suppose I think
*  different species have different degrees of this. And so for me, I think humans are remarkably
*  adept at learning a surprisingly large number of arbitrary things. And, but that doesn't mean that
*  we're not constrained. We're very much so still constrained. It's just that it's surprising how
*  arbitrary it can be. Yeah. Just to circle back to the question that you asked a while ago about,
*  do I hate learning? And how much do I hate learning? You love to be this guy, though. I know.
*  Obviously, I personally hate learning things. But, but I think that the point that I was trying to
*  make in that essay was not that learning isn't a thing that exists, but that a great deal of what
*  non neuroscientists sometimes imagine depends on learning, probably doesn't depend on learning by
*  an individual over the course of his or her lifetime. And that we are biased by paying
*  attention to humans who probably learn way more than almost any other animal, probably more than
*  any other animal. But even we don't learn as much as we think we do. But animals, most animals,
*  don't actually require a great deal of learning to function properly. So they're capable of learning.
*  But if you look at most insects, they can't afford to spend their first couple months figuring out
*  how the world works, right? They come out of whatever it is that insects come out of. And
*  they're they're pretty much ready to roll, right? Or fly or fight or crawl or do whatever they're
*  going to do. Yeah, I mean, you know, I have colleagues who study learning in Drosophila.
*  And so, you know, flies are capable of learning. And that certainly is adaptive. But many of the
*  things that we're impressed at, that insects and frankly, even mammals do, probably doesn't require
*  a great deal of learning, probably maybe just a bit of fine tuning to the environment. So,
*  you know, you watch a squirrel jumping from tree to tree, that squirrel didn't like figure out
*  de novo how to jump from tree to tree. Like all squirrels learn to do it pretty well.
*  And I think I just want to note something, because I think there's this
*  misperception that there's a big divide on this question. Tony has actually convinced me of this
*  point. And and I really don't think that it's incorrect to say that for the vast majority of
*  species, a lot of the learning that has occurred, quote unquote, was actually optimization over the
*  course of evolution. I think that what is maybe sometimes misunderstood about this argument,
*  though, and Tony or Doris, you can disagree with me if you do on this point, is that that doesn't
*  mean that then for AI, the message is hardwired human engineered features. Because the problem,
*  they agree that the mental jump that people are making there is they're saying, okay,
*  animals have a lot of innate machinery, therefore, we should give AI innate machinery.
*  But they're forgetting that animals innate machinery was delivered courtesy of an optimization
*  routine, rather than a human engineer. And this is the problem because human engineers suck at
*  delivering the kind of things that you need for AI. That's what we discovered over the course,
*  50 years of failed AI research. So, you know, although everything that is Tony saying is true,
*  animals have all this innate machinery, and you know, a squirrel probably doesn't,
*  they tweak whatever existing programming is there in order to learn how to jump from tree to tree.
*  That doesn't then mean that the solution to AI is for us to sit down and try to be like,
*  okay, let's think through it. Absolutely. No, I think I think that's absolutely right.
*  Like we have this innate machinery. And if we're going to try to engineer it, the solution isn't.
*  So, so far, we were we were given two choices, right? One choice is to hand engineer those
*  features either by using your imagination or possibly by looking at the engineered features
*  from animals. That's choice one. And choice two is to learn them de novo each time you train a
*  system. And I'm arguing there's a third route, which is you lay a foundation of the sort of useful
*  prior, right? And maybe you get them through an optimization algorithm. And frankly, you know,
*  just because evolution got them through an evolutionary algorithm doesn't mean that that's
*  exactly the algorithm we need to use. So in fact, you know, evolution is a lousy algorithm, right?
*  Because it doesn't use a gradient. Evolution worked because it operated over, I'm going to try
*  to do a back of the envelope calculation on this, like 10 to the 10 to the 30 individuals have
*  contributed to our our genome, even with really fast GPUs, it's going to be a while before we can
*  sort of simulate 10 to the 30 organisms and use the outcome of that as the basis of
*  of our of our system. So no, I mean, the the insight that we have was that gradients are
*  really useful for finding your way around the high dimensional space. Right. So if we're going
*  to engineer if we're going to recapitulate evolution, right, we're probably going to have
*  to do it using gradient. And the idea is that we shouldn't have to redo that each and every time
*  we train a network, we should sort of figure out some kind of collection of foundational structures.
*  Right. Each time we train a network, usually, and you know, there's been some recent work on,
*  on, you know, not starting from scratch each time, especially with language networks, because
*  there are basically we have no choice, right? Because, you know, training one of these causes
*  the lights to dim in Boston for a couple days requires that much energy and compute. So it,
*  it seems like at some point, you can't keep retraining from scratch each time. But I think
*  that that the lesson there is far more general, and we have to sort of figure out how to reuse
*  the training that we've done over and over again, in a useful way. So, you know, when I was a kid,
*  we used to stump each other by asking, Do you walk to school or carry your lunch?
*  And I, it's a false dichotomy, right? The choice between learning and exploiting innate structures
*  is a false dichotomy. The answer is we should do both. Do you think though, we're anywhere near
*  understanding the capacity. So thinking about the high dimensional structure, right? Of, you know,
*  86 billion neurons. But do you think that we are near anywhere near appreciating the actual
*  heavy heavy lifting that evolution has done to create that a particular high dimensional space,
*  right? Where are these amazing general learning things, and it's amazing, the different types of
*  things that we can learn and recombine. But on the other hand, constraint, like Blake was saying,
*  is super important. And do we do we appreciate that high dimensional structure enough? Or do we
*  think, okay, it's so high dimensional, it can just do anything. I think most people would recognize
*  the importance of the high dimensional structures that have been optimized by evolution for the
*  unique properties of human thought. And certainly anyone who's tried optimizing neural networks
*  for any lengthy period of time will appreciate just how amazing the product that evolution has
*  produced is. Because you can get a lot of really cool, funky, amazing behaviors with gradient
*  descent. But getting the unique mix that you see in animals in general, not just people,
*  is turning out to be remarkably difficult. And so I think anyone who has spent some time with
*  and with these optimization procedures will respect evolution's contribution quite a bit.
*  Yeah, and you guys have been talking about how you can build, use evolution to build the most
*  powerful machines. As a neuroscientist, my interest is really to understand the brain. And there's
*  different ways of understanding, right? There's this fad right now of regressing activity of
*  neurons to units in deep networks. That's one type of understanding. I think the deep understanding
*  is going to require understanding the structures, right? It's sort of like, if you take a simpler
*  example, you know, what is the probability of getting two heads and a tail if you flip a coin
*  three times, right? So you could figure that out by doing a Monte Carlo simulation. You could figure
*  that out by writing out all the outcomes, right? H, H, T, H, T, T, so on. Or you could figure that
*  out by actually understanding the structure of the binomial distribution. I think all of us would
*  agree that the last form of understanding is this, you know, real understanding. And so similarly,
*  like just taking a neural network, like that's not going to, and then regressing and saying it
*  explains whatever percent variance, like that, that's not totally satisfying, right?
*  I agree with that. And I just want to say, I think sometimes there is an unfortunate tendency
*  for people to think of the contribution that machine learning can make to neuroscience
*  as being fully encapsulated by that approach that just regresses neural activity against
*  deep neural networks. And I think that provides us a bit of understanding, as Doris said, but in my
*  mind, that is only really effective as a tool for gaining understanding if you're using it to answer
*  other questions with the neural network. So simply showing that you have a network that you can
*  regress well against the data is itself not necessarily that informative. It doesn't tell
*  you nothing, but it's not necessarily that informative. But instead, what you want to do
*  is you then want to use those models to, as it were, understand the distribution and to try to
*  think about the principles by which you can get models that are better fits to brains.
*  And it's only by taking that principled approach and using these models as normative guides
*  that we get to something like real understanding. Simply doing the regressing itself is not
*  I agree with Doris, sufficient for understanding. And it's also not, and this is ultimately my point,
*  the entirety of the program that neural networks and machine learning and neuroscience have to
*  offer neuroscientists. Exactly. And I think Tony's essay also for me personally introduced another
*  dimension of understanding, right? Understanding how this genome encodes these structures that
*  enable learning. And it's sort of always like festered in the back of my mind. And I heard this
*  statistic that the genome, you can put it on a CD-ROM or something, and it seemed kind of incredible.
*  But I never, like Tony, really worked out the implications of that. You have to specify all of
*  these learning rules in that CD. So that's, yeah. I feel like if we're going to understand the brain,
*  we have to understand that question too. Like Mara had the famous three levels that this is,
*  I feel like a fourth level. How does this computational structure, how do you actually
*  wire it up with the small amount of information? In some sense, I consider it good news because
*  it means that the, like there was one concern that I've always had is that the brain is just
*  infinitely complicated. You know, there's this bag of tricks idea that basically it's just a
*  collection of kludges. And although there's clearly some of that going on, right? Clearly a lot of
*  specialized adaptations that you'll only understand if you really, really dig, dig, dig,
*  very deep. The overall description length of the entire circuit is just not that long.
*  And, you know, there's an upper limit, which is the size of the genome, but it's not being optimally
*  used in some sense. And not all of the genome is used to specify the brain. So, you know,
*  the difference between, actually I did another calculation, the difference between
*  a human brain and a macaque brain actually does fit on an old school floppy disk. So it's, you know,
*  of order one megabyte. Doris doesn't know what you're talking about, but okay.
*  So, you know, I think it's good news that the things that make us special as humans,
*  it's really not that much, right? Now, you know, one megabyte of stuff could actually have a huge
*  impact, but to figure out what that, to write it down, it turns out probably not to be so hard.
*  Well, this is why I brought up development earlier. And I mean, I'm just unbiased because
*  of my recent conversation with people like Robin Heisinger and well, other people I've had on the
*  podcast recently, Kevin Mitchell, for instance, that the, their argument is that we're actually
*  missing, like what is actually specified in the genome isn't the rules for connections,
*  it is the rules for development. And that through the developmental process, that algorithm actually
*  changes. That's the same thing. Yeah, six and one half doesn't know the other. Yeah, that's
*  implicit. And say, it's not so it's clear that we will not like dig into the genome and suddenly
*  find the part where you can unpack the matrix that reflects the cut, you know, the conductive,
*  I don't know, not the recent movie, but the connectivity matrix
*  among among neurons, right? Like, we're not going to, ah, there, you know, let's just do
*  gzip on this. No, it's not. It's not simply a bunch of synaptic weights, even probably
*  in C elegans, where you could actually just lift all the weight C elegans being a worm,
*  there's 302 neurons and 7000 synapses, right? Even though the C elegans genome is a little
*  smaller than ours. That connectivity matrix for the circuit, the entire brain circuit of the
*  worm C elegans would fit comfortably into the genome, but that's still not how it's done.
*  Right. So developmental rules are, you know, interesting and complicated, but they're rules,
*  right? So at no point would you expect to find a list of connections within
*  within a genome. So I think we're all in agreement that the way you get from
*  genomes to circuits is via interesting developmental rules. Whether that whether
*  understand, like I think understanding those rules is fascinating in its own right, whether
*  that will be the path to understanding, you know, the computational roles of neural circuits.
*  I don't know, I'm, I am getting increasingly interested in development in the hopes that maybe
*  it will provide insight. But, you know, there are possibly many ways of figuring out how to make a
*  brain that that compute or how computation in the brain is, is sort of instantiated into the circuit.
*  Tony, how's your paper aged? I had you on, it was like two years ago or something. I don't remember.
*  It was forever ago. But yeah, it was a long time ago. Yeah. Would you do, would you have
*  written anything differently in the paper at this point? Or do you still stand by the original
*  message? And I, I still stand by it, it sort of laid down the, certainly the path that my lab is
*  going to be taking in this, in this domain. So, you know, that was, you know, it was an essay,
*  it was full of ideas and observations, but not actual work. But for me, like the research program
*  that is suggested by it is to figure out how to actually compress an artificial neural network
*  wiring diagram into a quote unquote genome. And that when you ask, you know, what am I thinking
*  about? That's on a day to day basis, what I'm thinking about. And, you know, that's, that's the
*  nitty gritty of it. And it's been, it's been a lot of fun, it is a lot of fun to see how we can do
*  that. So, but I think, I think there's, you know, if I were to add, I've been talking to actually
*  Blake about this recently, is to think a little bit harder about the role of evolution in all this.
*  I think, you know, how to actually fit that in is like, I don't have a clear idea yet. But in terms
*  of a path forward, that's something that I've certainly been thinking a lot about.
*  Do we understand evolution itself well enough to think about those things?
*  I feel like we understand the principles of evolution pretty well. You know, it's for me,
*  the biological equivalent to Newtonian mechanics, it is the core insight that allowed us to build
*  all the rest of the conceptual scaffolding and general approach to doing the science. And so,
*  you know, I'm sure there are still tons of things that people are learning about evolutionary
*  processes every day, but the fundamental mechanism is very clear and we can simulate it,
*  we can show that you get all sorts of interesting things that, you know, explain a variety of
*  facets of biological life. And so, though there's more to discover, I think if we don't admit to
*  knowing, to understanding something about evolution, then I'm not sure what we do understand.
*  Yeah, I'm with you there.
*  All right. As organizers of the NYSYS conference this year, I will just put your feet to the fire.
*  Where do you guys think, complete speculation, of course, where do you think we are on the
*  FAD curve of what is sometimes called neuro AI? That is, well, go ahead.
*  Hardly a FAD. I would say that it's just the opposite. It's after a neuro AI winter,
*  we are experiencing the neuro AI spring. So, we're returning to, you know, we're returning
*  to our roots. So, I think that it deserves, I think neuroscience deserves to be a part of AI
*  and vice versa. And we're just hopefully going to kind of catalyze that return.
*  Yeah, I agree with that. And I think the only caveat I'd add, and this is why sometimes you
*  can talk about FADs, and I say this with all due respect to anyone in California listening or here
*  on the call, sometimes the FAD machine that people are picking up on is not what's going on in
*  academia or even industrial research, but the FAD machine that is what comes out of Silicon Valley,
*  venture capital, culture, and stuff like that. And there, I think we probably have passed an
*  inflection point. If you just look at the number of searches online for deep learning, it's down
*  from a few years ago. If you look at the extent to which people are throwing money at anyone who
*  says they have a company that does deep learning, that's down from a few years ago. So, there's
*  some business cycle FAD that maybe is slightly on the wane. But I think the long-term business
*  trend, and certainly as Tony articulated, the long-term scientific endeavor is not a FAD,
*  has never been a FAD, and will continue to pick up pace as we start to figure more and more out.
*  Agree Doris? I completely agree. I mean, I feel like this
*  neuro-AI is as fundamental as physics or chemistry. It's the study of intelligence,
*  perception, all of these things that some of us, that's what we care about. It's so fundamental.
*  There's certainly FADs in how you analyze data using neural networks and so on. That's all true.
*  But yeah, the fundamental quest to understand intelligence, I don't see how that can be called
*  a FAD. All right. One last question. I know you guys have to go for each of you. Do the problems
*  that you are working on, do they feel bigger or do they feel smaller than when you began working
*  on them or as you continue to work on them? For me, they definitely feel that they're so much
*  bigger. When I first started recording from face cells, the question was like, what drives this
*  face cell? Even as the eyes, the shape of the face, and so on. We've pretty much figured that out.
*  The cells are driven by shape and appearance features. So now we're asking questions like,
*  how does the brain generate a conscious percept of a face? Or can the brain, how do you imagine a face?
*  How do you learn a face in an unsupervised way? It's a whole new realm of questions.
*  When I started graduate school, I had this fear that I wouldn't train up fast enough
*  and that by the time I understood enough to do useful work, all the problems would be
*  solved. That turned out not to be quite as big a problem as I thought.
*  In that sense, the problem seemed constantly to get bigger. I thought the problem was pretty small
*  when I started. I thought that it was like training up as a physicist in the mid-20s,
*  because there was this sudden moment where everything got figured out in quantum mechanics.
*  And if you got your degree in 1929, you'd missed the boat. I figured that that was going to be.
*  Turns out we haven't quite hit that inflection point yet.
*  The problems remain as big or bigger than when I started graduate school.
*  Blake, I'd love to hear a dissenting voice here, that all the problems seem tiny now.
*  I'm afraid I can't give you that kind of dissent. What I'll say though is,
*  I think that as the field matures, what's interesting is that you get to the point where
*  though the problems can seem bigger and are bigger, you feel, at least me, I feel a little
*  bit more like I have some of the conceptual tools to tackle them. And so, though it seems
*  like there's more work to do and the problems are bigger, I don't feel the same sense of like,
*  well, how the hell are we going to do this at all? That I felt maybe like 15 years ago when I was
*  starting my graduate school. That's a radically different scenario that way, to feel like we
*  actually have some of the conceptual and experimental tools necessary to tackle these
*  problems that do indeed seem bigger to me now. Well, considering that 99.999% of the organisms
*  couldn't be with us today because of that bastardly evolutionary optimization algorithm,
*  I really appreciate this little sliver of humanity being with me. Thanks guys for joining me.
*  Thank you so much.
*  Braininspired.co. The music you hear is by The New Year. Find them at thenewyear.net.
*  Thank you for your support. See you next time.
