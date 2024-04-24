---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5605s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 175
Video Rating: None
---

# BI 053 Jon Brennan: Linguistics in Minds and Machines
**Brain Inspired:** [November 18, 2019](https://www.youtube.com/watch?v=1dko1tVzS20)
*  I mean, how can you not be impressed?
*  This is phenomenal what our natural language processing systems are doing these days, what
*  you can do in your phone.
*  So I'm very impressed.
*  What I get skeptical about is when the advances, the engineering advances are put forward as
*  scientific insights into cognition.
*  When are we comfortable saying that meaning has been captured in this neural network?
*  And even if we say that, are we saying it's the same type of meaning as captured in, say,
*  a human brain?
*  This is Brain Inspired.
*  You guys are amazing.
*  I mean, you guys are amazing.
*  But I'm quoting John Brennan there because that is what he tells his class before he
*  He teaches them just how amazing their brains are to be able to use language so seemingly
*  effortlessly.
*  John is a linguist at the University of Michigan studying how words and sentences are combined
*  and structured in our minds and brains and the algorithms by which to process those words
*  and sentences.
*  He uses his linguistic expertise and collaborates with others to create and test neurocomputational
*  models that strive to process natural language like the story Alice in Wonderland and output
*  something that matches various brain signals that humans produce when reading the same
*  story.
*  John and I talk about why language is so hard to study.
*  I get his take on the current state of natural language processing and other language-related
*  AI, how he thinks linguistics can contribute to AI.
*  And we discuss some of his work to test whether when we process language, we're always using
*  our full resources to process any potentially complicated structures and patterns in the
*  syntax and semantics of the language or if we can get by whenever possible by using a
*  simpler style of processing.
*  I'll let the answer to that mystery gnaw at you for now.
*  I appreciate the recent feedback.
*  Sounds like many of you are looking forward to what I guess I'll call for now the Brain
*  Inspired Course, which is slowly taking shape and which aims to eventually cover the whole
*  neuroscience and AI interface landscape, past, present, and future.
*  So you know, just a tiny little project.
*  I haven't figured out yet exactly how I'll roll it out, but it'll have to be a living
*  sort of course.
*  By that I mean I will release some version of it with the promise that it will continue
*  to grow as I build more.
*  All I know for sure is that if you support the show on Patreon, you will have access
*  to all of the early versions that I make and most likely much more than that.
*  If you just want to stay informed about when I plan to release stuff, you can sign up for
*  the email list at braininspired.co slash course.
*  Also dear Patreon supporters like Brandon and Theo, thank you guys.
*  I'm planning at some point to start putting out a little extra audio content like maybe
*  primers and summaries of things that we talk about on the show so that you can get more
*  out of the episodes going forward.
*  All right, go to the show notes to learn more about John and what he does at braininspired.co
*  slash podcast slash 53.
*  Either you are using all of your glorious hierarchical processing abilities or just
*  making ends meet with some sequential techniques.
*  That'd be fine too.
*  I wish you all happy word and sentence processing until next time.
*  Here is the exceptional John Brennan.
*  Beware the Jabberwock, my son.
*  The jaws that bite, the claws that catch.
*  Beware the jubjub bird and shun.
*  The frumious bandersnatch.
*  John, you did not write this, but why do you hate this Lewis Carroll poem so much?
*  What a way to start.
*  I love that Lewis Carroll poem.
*  I love Alice in Wonderland.
*  I actually just read it to my kids a couple of months ago, both Alice in Wonderland and
*  Through the Looking Glass.
*  They are weird stories.
*  They're weird stories for children.
*  I do have an opinion about this poem as it comes to researching language in the brain.
*  Yeah, so that's the Jabberwock poem.
*  That's just one of the ways that people try to tease out semantics from syntax, which
*  is called Jabberwocky, that style of having very little meaning in the words but having
*  some sort of syntax still in the structure.
*  So we'll get to that.
*  I just wanted to try to throw you off there at the beginning.
*  I do want to add though that Alice herself immediately after hearing that poem says,
*  says, I don't know what, but it does mean something.
*  It does mean something.
*  So Alice is getting meaning from that sentence and she knows someone killed something at
*  the end.
*  Oh yeah.
*  If you want to circle back to that, we can.
*  Oh gosh, yeah, that's a big topic.
*  All of these are such big topics.
*  I hope this will be fun.
*  Okay, so John, welcome to the show.
*  Thanks for having me.
*  This is going to be fun, Paul.
*  So you are, what do you call yourself, a computational neurolinguist?
*  What do you call yourself?
*  I'm a linguist.
*  Linguist, okay.
*  You are interested in how words and sentences are mentally represented in our minds and
*  processed in our brains.
*  You use computational models to test this along with EEG, MEG and fMRI to try to figure
*  all this out.
*  Yes.
*  So, all right, let's jump into it.
*  So, originally I had David Popple on the show who, among other things, tries to figure out
*  how the sounds that we hear get processed into meanings in our brains and our minds.
*  I also had Liz Spelke on the show who believes that language is this special sauce that allows
*  us humans to dominate and rule the planet and soon the universe and so on.
*  Language is hard to study.
*  I was definitely too scared to study it.
*  So why is it hard?
*  What are the challenges to understanding language versus other cognitive processes like perception
*  and action and even some of the things in between, classically thought to be between
*  perception and action like decision making?
*  Why is language special and hard?
*  Great, great.
*  Yeah, I kind of wish I was a little more scared or a little more skeptical when I got started.
*  Now looking back from what I know now, but language, I mean, there's two answers that
*  I think are pretty commonly given to that sort of question of, well, what are the special
*  challenges facing the study of language as a cognitive science and a neuroscience?
*  One of them is that we only have one model, the human model.
*  So there's not a really adequate animal model for language.
*  There are some animal models that have been studied in terms of speech.
*  So vocal communication in particular.
*  Bird song has been useful amongst others.
*  Speech and language are distinct phenomena.
*  So language is not solely an aspect of vocal communication.
*  So sign languages are as rich as spoken languages amongst other things.
*  So language is really a distinct phenomena from what we see elsewhere in the animal kingdom.
*  And that's just going to be challenging.
*  We can't stick single electrodes into neurons willy nilly until we find the neuron that
*  represents nouns with people.
*  And we can do that for cats or mice or macaque.
*  The other challenge that I think it's commonly mentioned is that actually all the things
*  that you mentioned, action, decision making, memory, these all get used when we use language.
*  And so language is a system that depends on many other cognitive systems.
*  It draws on them.
*  That doesn't mean it's not distinct.
*  That doesn't mean it doesn't have its own special sauce.
*  But it's hard to study something that is so intertwined with other systems that we also
*  don't really fully understand.
*  And so you end up being in a position that I think is kind of familiar.
*  Well, it's a very familiar feeling to me.
*  I think to others, which is you're sort of trying to understand something that you don't
*  yet understand with other things that you don't quite understand.
*  And this is challenging.
*  This is challenging.
*  And then there's the whole issue of meaning and what is meaning and how to encode it as
*  well.
*  So we'll get more to that.
*  Yeah, good.
*  Good.
*  I guess the study of language in non-human primates like cocoa, that sort of fell apart,
*  right?
*  I don't know if it fell apart.
*  It's certainly not hot these days, at least in terms of what I'm seeing.
*  But I think we learned some interesting things.
*  So there's a set of research programs that were basically designed to ask nature versus
*  nurture.
*  So is human language special because it has a special kind of communicative and thought-building
*  characteristics because human children are embedded in a language-using environment that's
*  very different from the environment that other young animals find themselves in?
*  Or do children bring something special to the table such that they are going to learn
*  language from their environment and other animals are not?
*  So that's a way to put the question.
*  And so one way people tried to answer this was literally bringing in animals into their
*  environment.
*  So famously, Herb Terrace at Columbia University tried to raise a chimpanzee named Nim Chimski
*  in a human environment.
*  And there are all sorts of scientifically challenging things in that research program.
*  There are some non-scientifically challenging things in that research program.
*  But the idea was sort of built on this question of if you give a chimp language input, is
*  it going to learn language?
*  And despite the challenges, I think the answer we learned was no, not quite.
*  Well, that was his big conclusion, right?
*  And then there's this big sort of fight between he and Coco's owner, sort of, which we don't
*  need to get into.
*  But even before that, wasn't there an attempt to try to teach, I don't know if those apes,
*  to actually vocalize, to say the words?
*  I mean, this is how naive we are, of course.
*  There was.
*  So the first attempts, yeah, were, and the couple's name escapes me, but a couple brought
*  a chimpanzee, I think I want to say it's a chimpanzee, into their house.
*  And this is the late 50s, early 60s, and just raised it along with their infant.
*  And you and I were just talking about raising infants.
*  It's a challenge.
*  And I imagine it's a little more challenging when there's an ape involved.
*  And this was spoken language, and that didn't work.
*  And part of the reason that didn't work is because the chimpanzee is not going to vocalize
*  in the way humans can vocalize.
*  It's not going to have the same physical apparatus.
*  And so a lot of the more successful challenges, for instance, the program that Herb Terrace
*  ran with Niemczewski was using sign, a kind of form of sign language.
*  Now, one of the scientific issues is that none of the researchers in that program were
*  native signers.
*  So these are non-native signers trying to, so that's already going to pose a challenge.
*  So you put children in an environment when they're surrounded by non-native signers,
*  and they're going to learn, they're going to develop a fully formed sign language.
*  This has been documented now many times, most famously in Nicaragua.
*  So even from that very flawed experimentation, we already, I think, see interesting differences
*  between what human infants do, given a very impoverished input for non-human, in this
*  case, primates.
*  So I don't know how you're raising your kids, but I tried to get my wife to agree with me
*  to just go with silence and non-signing and only give them food pellets when they said
*  anything that made sense.
*  It hasn't worked out.
*  I know.
*  I know.
*  The water feeding, too.
*  I periodically considered the idea of, there's certain kinds of sentences that linguists
*  have studied now for decades that seem to violate the rules, not of a particular language,
*  but of any language that's been documented, these languages that seem to be sort of, they're
*  just un-human language.
*  And so the question is, what do children do when they're presented with this as input?
*  They're never going to get it as input, but they also never make a mistake that has that
*  shape.
*  So children make lots of linguistic mistakes, but there are certain mistakes they never
*  make and there's actually interesting patterning to those mistakes.
*  The question is, what happens when you give them an input that violates what seem to be
*  the rules of any language?
*  And I have not, I haven't had the wherewithal to really test this out in even a non-scientific
*  way.
*  Yeah.
*  So you're going to test what you do test.
*  Okay.
*  Well, so let's back up here.
*  I want to start sort of with the AI side of things here and then we'll switch to the neuroscience
*  and your work in that area.
*  My understanding is that, and I'm not sure exactly how familiar you are with a lot of
*  the AI side of things, but my understanding is that many or most of the advances in natural
*  language processing are basically reduced to a language model at its core.
*  A language model being basically there's a sequence of words, it takes a sequence of
*  words and just tries to predict the next word.
*  Yeah.
*  Yeah.
*  And there's lots of advances going on.
*  It's very rapid right now in natural language processing and other language fronts in AI.
*  What is your, do you have a thought, do you have a broad assessment from the neuro linguistics
*  point of view of, or the linguistics point of view of natural language processing and
*  other language models and technology in AI?
*  I mean, I have opinions.
*  That's what we want here, man.
*  I'm not an AI person.
*  I'm not an NLP person.
*  I'm not a computational linguist.
*  So all of my opinions are from an outsider's perspective.
*  So a language model, I think of a language model as a task, right?
*  It's a task we can give an artificial system.
*  It's a task we can give a person.
*  I give it to a person we call it a closed task.
*  Predict the next word.
*  And there are many ways.
*  It's incredibly powerful when you train.
*  So what you see a lot of success is what I see a lot of success as being as building
*  an algorithm and then you train that algorithm, you teach that algorithm, you set its parameters
*  by asking it to predict the next word on some corpus of text.
*  And it's going to adjust its parameters when it does that wrong until it does that a little
*  bit less wrong.
*  And the models that are trained in this way do well.
*  They do well at that task.
*  And then it seems to me one of the big breakthroughs of the last year or two, just how rapidly
*  this field blows my mind, is getting models trained in a way similar to that to do well
*  on other tasks.
*  So another task might be say translation or inference or question answer.
*  So the transfer learning is kind of what it's called in that.
*  I'm not sure if that applies to such different sorts of tasks, but I'll call it transfer
*  learning.
*  Right, right.
*  Sure.
*  Yeah.
*  And people predict too.
*  Right.
*  So one of the sort of guiding principles when I think of how we approach the challenges
*  we face in my work, which is what the brain is doing when it's building meaning in terms
*  of like words and sentences, is we have to understand the brain's doing that in a predictive
*  way.
*  It's working with it, with what it has to do as much work ahead of time as it can to
*  make its job easier.
*  But prediction is not the end all be all of what the brain is doing.
*  And the way I see it presented in the NLP literature, at least the literature I understand
*  and as much as I understand any of it, is the task is to predict the next word.
*  That's what you're doing.
*  That's the job of the model, to predict the next word.
*  And that's not the job of people.
*  Their job is not to predict the next word.
*  Their job is to understand.
*  Or perhaps something else.
*  Perhaps their job is maybe a kind of understanding, but understand just enough to like get their
*  bagel and coffee and get out of there.
*  Or to understand just enough of a lecture that they can do on, you know, or something
*  else, right?
*  So, but it's, I don't think it's often the job of the language user to predict the next
*  word.
*  I think prediction is a tool that the brain is using to make whatever its job is a little
*  bit easier, if that makes sense.
*  And so it's a fundamental part, thinking about prediction and what the brain is doing is
*  a fundamental part of how we approach the problem in our lab.
*  But it's just that.
*  It's sort of, it's a context we place on the job the brain is doing.
*  Whatever it's doing, it's doing it.
*  Prediction is going to be part of that.
*  So you don't, you know, when the latest model comes out, latest instantiation of some transformer
*  model or whatever comes out, you don't project forward and think, oh man, this is eventually
*  going to start understanding what it's predicting.
*  You know, you don't see that magically happening.
*  You know, do we need to know how brains process language for meaning to, you know, to build
*  it in AI or are we just going to get there by brute force?
*  Right, right, right.
*  So do we need to understand how brains process meaning to do it in AI?
*  No, no, I don't see why we would need to do that.
*  So we don't need to understand.
*  A favorite example of a colleague of mine is we don't need to understand how birds fly
*  to build airplanes.
*  The rebuttal to that would be that airplanes don't fly anything like birds and can't fly
*  anything like birds.
*  But I digress.
*  No, I don't think you do.
*  That's right.
*  That's right.
*  But that's not to say that airplanes and birds don't sort of embody something about aerodynamics
*  and the physics of flight.
*  They both interact with the same physical principles of our world, right?
*  They just do so in very different ways to achieve an end which we call flight.
*  We call both of those flight.
*  And so maybe we should be worried about that word.
*  Maybe flight we want to call one thing flight and the other thing flight prime or something
*  else.
*  And I suspect we're going to run into the same challenge with artificial and human intelligence.
*  We already call them neural networks.
*  We call them neural networks in the brain and we call them neural networks in a digital
*  computer which is frustrating for people like me, I guess.
*  I think we try to be careful about artificial neural network, make sure we call that artificial
*  neural.
*  But you're right.
*  And I think the word meaning is going to give us the same challenge.
*  So when are we comfortable saying that meaning has been captured in this neural network?
*  Even if we say that, are we saying it's the same type of meaning as captured in say a
*  human brain?
*  Or frankly, is that meaning in the human brain the same meaning that's going to be captured
*  in my cat's brain?
*  I mean, my cat is representing very complex relationships between things at the same time
*  as my kids are.
*  And meaning becomes a very slippery, very difficult term here to ascribe to sort of
*  to say that something has the same or something has different meaning.
*  So that's not to say that the artificial neural network can do something very powerful,
*  not doing something that is going to represent meaning.
*  But you want to be careful, I guess, when the debate becomes, is it human-like enough?
*  And I'm not sure I answer that.
*  I'm happy just taking different terms.
*  Yeah, right.
*  Yeah.
*  So, okay.
*  Well, then are you impressed with the capabilities in artificial networks?
*  I mean, how can you not be impressed?
*  This is phenomenal what our natural language processing systems are doing these days, what
*  you can do in your phone.
*  So I'm very impressed.
*  What I get skeptical about is when the advances, the engineering advances are put forward as
*  scientific insights into cognition.
*  Ah, yes.
*  And so now I'm guilty of this.
*  I want to take the newest, fanciest tool from Google Research and see what insights it might
*  offer for how humans solve the problem of language understanding or the problem, the
*  subpart of that that we already talked about, about predicting the next word.
*  I think that's a subpart of the human language understanding problem.
*  But to say that solving the problem in one domain is going to therefore give us the answer
*  in the other domain, it's just, it's not going to be that simple.
*  The part where I'm optimistic, and I know I have colleagues who disagree with me on this,
*  is I think that I can look at one for insights, but possible insights into the other.
*  So like, oh, how did you solve that problem when faced with it at Google Research?
*  Let me think about that now and ask if there are ways that can help me think about how
*  the brain might have solved that problem.
*  Yeah, but the problem is if you ask someone there today, then you go back to your lab
*  and you think about it for a week and you think, oh, I might now have like somewhere to,
*  I might be able to apply it.
*  And then you ask them again and they say, oh, no, no, no, that was a week ago.
*  Now we have a completely new and different model.
*  So you were at CCN this year.
*  This is where we met, Cognitive Computational Neuroscience.
*  And I went to your breakout, which was very nicely done.
*  Anyway, we can talk about that later.
*  But one topic that kept coming up, that I kept hearing at the conference was just the
*  problem of the pace of AI.
*  So people in science were kind of like down about how fast AI was going because like,
*  how can we possibly keep up?
*  So you're excited, but do you see this as a problem at all that the models keep changing
*  so fast relative to what, because in science, you have to, in AI, your task is to solve a problem.
*  And in science, your task is to understand.
*  And if you do something where you think that might lead to some insight and understanding,
*  then you have to go back and do six more experiments to rule out all other possibilities.
*  And so it's so slow.
*  Is this a problem, you think?
*  Well, it's certainly a problem for me.
*  I don't know if it's a problem for the field.
*  Like I certainly cannot read enough.
*  I can't keep up.
*  And part of that is like I offload that job onto colleagues or computational colleagues who are a
*  little more embedded in those literatures.
*  And I ask, you know, I kind of trust them or ask them or rely on them to help me understand
*  what do I need to understand now compared to what I learned a year ago or five years ago
*  or 10 years ago.
*  Is it, there are a couple of, so then there's, we've certainly been victim of this.
*  So we were emailing before this chat and you'd mentioned a paper that our group wrote earlier
*  this year.
*  And that paper that we were earlier this year was eclipsed by ourselves six months before
*  that paper came out because of the different pace of work in different domains.
*  So one paper came out in a computational venue, the Association for Computational Linguistics.
*  And that is just a bit, that paper, you know, was written and submitted and revised and came out in
*  six or eight months versus a paper that we pushed through a regular journal that took,
*  you know, two years.
*  Well, this is a problem with journals as well, but.
*  And me, you know, at some point I'm going to, you know, there are certain deadlines I'm going to
*  be a little slower on because I know that I have more.
*  So yes, it's a problem.
*  I don't know if it's a problem for the science.
*  I can't tell.
*  I'm not, I'm not, I'm not.
*  But is it a problem for, because you, you know, you say you can take inspiration from some model,
*  right?
*  But then the model changes so quickly.
*  Is that a problem with taking the inspiration and actually using it?
*  Yeah, yeah.
*  I mean, one question, and I just, I literally don't have the answer is when we change a model,
*  what aspects are we changing?
*  So, so the analogy I think of is actually an analogy from linguistics.
*  So linguistics gets criticized sometimes, especially the syntactic theory in linguistics
*  gets criticized sometimes by outsiders because the theory has changed.
*  And now it's on a much slower pace.
*  So it's changed from like the early seventies to the late seventies to the eighties to the
*  mid nineties to the two thousand.
*  So on kind of a decade level, but people Chris, I was like, well, this is not
*  which theory is right?
*  What am I supposed to do?
*  How am I supposed to use your theory of syntax to understand, say, a psychological
*  phenomena or neuroscience phenomenon?
*  So linguistics gets criticized for this pace of change, but that pace of change on the surface,
*  which seems sort of like prohibitively costly to understand what's changed has masks some,
*  some constants, some things that have been the same in the theory from,
*  from the sixties to now, or at least from the early eighties to now.
*  And I wondered the same about about some of these AI tools.
*  So to what extent we've we've tweaked the parameters, we've added another LSTM or we've
*  we've taken a transformation network or and we take our attention network and now we've
*  glommed them together in a new way.
*  But there's interesting.
*  I mean, I would like to know to what extent some formal properties of the system have been
*  qualitatively different.
*  Yeah.
*  And I don't know.
*  I have no clue.
*  And maybe I'm just wrong.
*  And you're right.
*  And the pace of change is such that things are qualitatively changing such that the model,
*  the insights from a model right now is going to are going to be totally different from
*  insights from six months ago.
*  And if that's true, then yeah, I'm not in great shape.
*  Well, so it's you could say that there's a somewhat close connection between
*  deep learning models and some some processes like sensory processing.
*  In fact, there's a really good fit between some neural activity in these deep model networks
*  and what you see in the brain.
*  So for instance, convolutional neural networks, which I know are also used in language,
*  but they've provided like vision and other sensory neuroscience with tools to compare
*  with brain computations.
*  And those the convolutional neural nets, conva nets, CNNs were inspired by what directly by
*  what we learned in the 60s, Hubel and Weasel about how visual processing works in brains
*  by recording these single neuron responses.
*  But we don't have such a direct mapping from, like you said, from action potentials to
*  language.
*  Do you see the you know, are you jealous?
*  Do you see the relationship between like AI and neuroscience more disconnected for language
*  versus other cognitive domains?
*  Is that something that you're aware of?
*  Yeah, I mean, I maybe I am jealous.
*  I mean, this goes back to what I said, I'm not sure if there are challenges in this in
*  the particular path that I'm pursuing, but I didn't know when I knew.
*  I know less now than I knew five or 10 years ago as I learned.
*  I better understand more what I don't know.
*  And the sort of tools we have to under from to connect from basic neuroscience to
*  some aspects of higher level cognition.
*  Those tools are a little I think they're a little harder to use in language.
*  So we've we've posed with this problem the way we we've been tackling it, at least in
*  my little group, is by thinking carefully about sort of what level of abstraction are we
*  are we tackling some problems, some problem in this case in language comprehension and
*  building meaning.
*  And so we use deep artificial deep neural networks that that parse linguistic input
*  and we use aspects of these networks to help us understand brain signals.
*  But I at least don't look at this at what we're doing as asking.
*  We're not looking at what are the unit level activations in the deep neural network
*  and how are those mapping to unit or cortical circuit activations in the brain?
*  That's not a granular level that we're looking at.
*  So rather, I think that the we there are certain neural network architectures out there
*  that I'm excited about because they compute functions, they approximate functions that I
*  think capture something deep about the kind of functions human humans carry out as their
*  processing language.
*  And so the neural network is as it is, it's a function approximator, it's a function,
*  in this case, doer.
*  And it's doing it in a way I think is useful to understand what people are doing.
*  And then we ask whether the actions the neural network has taken at a at a pretty large level,
*  what decisions the neural network has made, to what extent do those decisions help give us
*  insight into what kinds of decisions the human neural network, the human brain is doing at some
*  larger, emergent, do we want to say emergent or?
*  Oh, I don't know.
*  No, no.
*  Maybe I don't just I'm not a native speaker of that term, but
*  Well, should we say psychological level or, you know, at the level?
*  It's definitely a higher level.
*  I mean, the level firm that gets used is algorithmic.
*  Okay.
*  Yeah.
*  David Maher.
*  So for instance, we might build a neural network whose job is to predict the next word,
*  so language model, and then ask, so what's its uncertainty about the next word?
*  And, and humans certainly make predictions in the service of understanding.
*  And we know that behavioral signals, but also brain signals are very sensitive to aspects of
*  how certain they are, or how unexpected an input might be.
*  And then we can ask, well, let's tweak the neural network and change what it's using,
*  what the information is using to derive that certainty about what's coming up next to make
*  that prediction. So we change the information that's available to network, the network to
*  make a prediction. And then we have now, we can do that multiple times, and we can develop kind
*  of a set or a space of possible sort of prediction paths the network can take.
*  And we can ask, well, which of these paths is the best match to what the human signal is doing?
*  And that's more or less what we've been doing for five or six years now.
*  And the level of abstraction is high.
*  So we're not looking at what the individual unit level activations of the network are doing.
*  We're looking at the outcome of those activations. And we can tweak sort of macro parameters and let
*  the beauty of deep learning sort of handle, I mean, that's what we use deep learning for,
*  to handle all the micro parameters to get it to work.
*  Right. So you're somewhat agnostic about the mechanism that gives rise. Actually,
*  let me rephrase that. So you don't give a damn about brains.
*  Yeah, I mean, maybe. I certainly, I think that's fair. That's fair. I mean, I'm a linguist. I'm
*  not a neuroscientist. The end game of my own little parochial research program is not to figure out
*  what's going on in a particular brain region or particular neural circuit or how it works,
*  is to understand what a phrase is.
*  Well, see, but I'm lumping it. So in this little world of this podcast,
*  everything natural, I lump into the term neuroscience because it would take hours to
*  just list off all the different fields that studies natural intelligence. Right. So I'm
*  lumping you in as a neuroscience in this regard.
*  Okay. Can I disagree with that?
*  Sure.
*  Right. So neuroscientists sort of implies that what I want to understand
*  are neurons and their interactions.
*  Okay. I'm just disregarding. Yes, in general, I agree with you. And I'm not going to
*  hold you to a neuroscientist in any other conversation. Okay. I'm going to have to,
*  like, I don't know, somehow I'm going to have to communicate this better, I think.
*  So, but okay, what do you think that, like, linguistics can contribute to AI progress?
*  Yeah. I think quite a lot. And I think there are lots of people advocating for this. And
*  sometimes this message is being heard. But the thing that linguists has long contributed to
*  the cognitive scientists more generally is a problem, a particularly sticky problem.
*  And this was what put linguistics on, it didn't put it on the map, but it put it on a new map,
*  it put in a new position on the map in the 50s and 60s. This is what Noam Chomsky made his career
*  out of, which was saying that there are problems in cognition that can't be explained by the,
*  at that point, the dominant theory of psychology, that is behaviorism. And I think, yeah,
*  artificial intelligence can hear that again, these days. I was at a workshop a little over
*  a year ago on, yeah, the intersections between cognitive science and artificial intelligence,
*  and sort of the mutual trade-offs between them. And the very last talk put forward a very
*  remarkable study. It was a mouse, one of these mouse and a maze studies from the 30s. And it
*  is absolutely amazing, the way the mice are navigating, they're given a certain reward,
*  and then what you do is you change the maze on them and you ask, well, how do they solve this
*  new problem, given that they've never seen exactly this problem before? And the way they solve it is
*  phenomenal. And of course, the piece to resistance of the talk was, of course, now we can show an
*  artificial network with remarkably well-understood properties solving the same problem in a very
*  similar way. And so it's amazing. But what stood out to me listening to that talk was the date of
*  the original finding, which was 19, it was in 30, I think it was 38 or 36. So it was at the peak of
*  behaviorism in psychology. And the success in behaviorism were brought short by language,
*  by recognizing Chomsky wrote in the late 50s, that when this exact paradigm was applied to language,
*  and it was seen as a verbal thing, though the language is not verbal, that paradigm could not
*  work. And so there are dependencies and aspects of the rules of language, of linguistic structures,
*  that could not be learned by the dominant behaviorist paradigm, and can't be learned by
*  the artificial intelligence networks that are now kind of reproducing some of those remarkable
*  behaviorist findings. And so language, I think furnishes a really, really interesting deep problem
*  space. And some colleagues are, you know, one of the things they're doing is looking at some of
*  the challenges that in this case, like people who do NLP are developing for themselves. So commonly,
*  you build a new neural network that is a language model, say, and you confront it with a large set
*  of text. And you ask, well, how well does it for instance, predict the next word or answer the
*  question, right, or produce a useful search result or something, you know, given some set of annotated
*  data, and then you ask, you ask how it can do on data that hasn't seen before. And so one of the
*  problems with that, the challenges that there that are often used, is that they rely on natural text.
*  You know that I love natural text. You can come back to that. Yeah, we will. But natural text,
*  makes use of a lot of very common, very simple, say, aspects of syntactic structure,
*  its kinds of sentence types. And it doesn't, there are lots of kinds of sentences, syntactic
*  structures that aren't used very often in natural text. So, but what's remarkable is that people,
*  even very young people, aren't that much bothered when they come across a syntactic structure that
*  they hear very rarely, or sometimes even not at all. So there are well documented cases of children
*  navigating challenging dependencies between words. I think we can get into some weedy details if you
*  want. But where if you look at a corpus of text, sorry, a corpus of speech that children of that
*  type would have heard, it's vanishingly small. It doesn't come out in an EEG, in the like ERPs.
*  What do you mean? If they hear something that's off, that's like a surprise syntactically?
*  So something that's, so that's what I'm saying is that there are certain types of syntactic
*  structures that don't come across as surprises, even though they've never been heard before. So
*  frequency of input is not predictive of surprise of the listener. I see. Yeah, so going back to sort
*  of what we can challenge our AI systems with. So there are, and these phenomena, these kind of
*  linguistic edge cases, they, I mean, they occupy 2% of a large corpus of English text,
*  but like 90% of the syntax literature, because that's those are the edge cases people want to
*  understand, like what is going on in these sentences? How do they work? What are their
*  internal bits? Why do they work the way they do and not some other way? And I, one thing that
*  I'm excited by are cases where computational linguists, computational linguists are using
*  these sorts of examples as challenge cases for AI systems, asking like, okay, now let's see stuff
*  that kids are really good at, even though they're really infrequent in the input and use those to
*  start tuning our neural networks. So again, linguistics, that's just one example where I
*  think linguistics offers an interesting problem space for AI. Cool. All right, you guys, you heard
*  it. There's a new challenge for you to go and implement in your networks. All right, well,
*  let's talk about people. Okay. So I don't know how compelled you feel to keep up with the
*  you know, NLP advances research because it's only about what, 1050 papers every day,
*  new papers every day. You're probably at least compelled to keep up somewhat with the
*  linguistics research. Yeah. So what is your broad take? What's the broad picture of where we are in
*  understanding how language works in even at the algorithmic level, let's say, in brains, in minds?
*  Yeah, we're just beginning. I mean, that's the thing that so my PhD advisor, Lena Polkinen,
*  will constantly remind, you know, I get reminded by her, but she'll give it mentioned in talks and
*  stuff is that we are just beginning this task of trying to understand how the brain understands
*  language. So it's okay to not know much. And we are really and what we do know we are wrong about,
*  right? We are wrong. Why is it? Why are you so comfortable saying that? Because I completely
*  agree. But I think that that applies to almost everything that we're studying. Yes, I agree with
*  you. I agree with you. I mean, that I don't know any other way to beat. Yeah, right. You can't
*  approach the problem and think, Oh, yeah, we've got it. Because then you're gonna, that's just not
*  true. And you're if you're just, if you start if you're starting from a place that's like just so
*  divergent from reality, I don't know what you're going to do next. So, so what the challenge,
*  what are we going to do when we know we're wrong? And part of me, like I get satisfaction by
*  thinking I'm not the only one. And it's not that like linguistics or or neuro linguistics, we're
*  not the only ones that you go to the physicists, and the leading theories of, you know, the universe
*  don't explain like 90% of the mass in the universe. My seven year old was just asking me what's
*  smaller than an atom and then I had to go into the whole, you know, well, quarks and then all the
*  others, I started to explain string theory to her, you know, yeah, no, we've had that conversation
*  around the dinner table, too. Yeah. And, and so like, if this is are happy with like, I don't
*  know what the cutting edge on like dark energy is. But if it's still more or less poorly understood,
*  I understand it. I don't know if anyone else does. Okay, good. That's your next paper. But,
*  but then we're all in the same boat. We're trying, you know, we, we try to make do with what we what
*  we build models. And we ask what characteristics do these models have? How do they match up with
*  the world? And where they go wrong? Let's let's dig into that. And, you know, in our lab, at least
*  the stuff that doesn't work is certainly the stuff that leads to the most exciting advances. Why
*  didn't that experiment work? Why didn't that model that model should have? Or why didn't that model
*  fit the data in a certain way? And that's what that's what leads us to the next step where we
*  get a little incrementally better with not just predicting new data, but with with building models
*  that have some sort of sense to them with understanding. So this is so is this the best
*  time to be alive in linguistics or what? I mean, we're doing okay. I mean, linguistics is
*  linguistics exciting, right? So it's a discipline that sits at the center of so many other
*  disciplines. And that for me has always been the attraction, right? A discipline where I can see so
*  linguistics at the University of Michigan where I am right now, sitting is has long been in the
*  humanities. I'm running an ERP lab. We actually just switched over the summer to the social
*  sciences division. But we continue to you know, we are neither here nor there, right? We are
*  talking to anthropologists, to psychologists and neuroscientists, to mathematicians and philosophers.
*  I mean, at some level, these are just labels though, too. Right, right, right, right. But
*  they're labels that have some value to us, right? They delineate certain kinds of questions, certain
*  kinds of methods and linguistics as a estuary in which these things connect, these different methods
*  kind of connect with each other. These kinds of questions crash into each other. We have to ask,
*  well, how do we reconcile questions about sort of people and communities and how people build
*  communities and situate themselves in those communities with language to like, well, what's
*  going on in the left anterior temporal lobe when you're listening to a word? And you know, I'm
*  sitting in a department where these two kinds of things are happening at the same time and in
*  offices right next to each other. And that for me is exciting. It poses a set of challenges which I
*  find, I find fun. That's great. You're young in your career, so this should be a lot of fun for
*  many years for you. I hope so. So John, you study a lot of what you study is semantics, which is
*  the meaning in language, which we have already talked about a little bit. Is the capacity for
*  language? Yeah. Is it the key or a necessary bottleneck or a key for deriving meaning
*  in the world? Yeah. This kind of goes back to, you know, we touched on earlier, which is like,
*  this word meaning is pretty slippery, right? And it's hard to get to know exactly what we mean. I
*  mean, the aspect of meaning that I've got, spend most of my attention on is combinatorial meaning.
*  So given that say words have meaning, that's going to be a big challenge to figure out. But
*  let's say we figure that out. Or let's say we just accept that they have meaning, then how do we
*  put them together to derive systematically the meanings of phrases and sentences? And so it's that
*  systematic combination of meanings that occupies a lot of my attention. And I do think that the
*  way in which language allows us to combine meanings in an infinite way. Infinite. Well,
*  that's another special thing about language that is unique among other cognitive. I mean,
*  I guess you could you could create an infinite number of paintings or, you know, different
*  types of paintings. It's different compositionally. It's definitely it's definitely seen as very unique
*  to language, the sort of infinite combinatorics of it. And I have become interested in better testing
*  that view. So we have other domains of cognition that show combinatorial recombinations of an
*  action planning is one of them. Right. So we can plan and execute and understand very complex
*  interwoven actions. And in fact, these complex actions are organized in a way that's hierarchical
*  in the way that language is organized hierarchically. So that, you know, grasping a cup involves
*  planning to move fingers and wrists and arms and torsos in the same way that I don't know in the
*  same way, but in a way that so we also talk about hierarchy when we talk about expressing a sentence,
*  which has in it nouns and noun phrases and and verb phrases and sentences. OK, so so one question
*  is whether the formal properties of these systems are similar or different. And that's a question
*  that as far as I can tell, has not actually been put to the test in the way I'd like to see it.
*  So one of the things that I really like about language and the combinatorial properties of
*  language are that we actually have a very good understanding, a mathematical understanding of
*  the formal properties of a system that generates the kind of common recombinations that language
*  has. So it fits a mathematically well understood domain of what kind of system has the properties
*  that human language has. It's a domain that Chomsky had some early contributions to. But people
*  like R. Van Josie at Penn kind of identified or a consensus view that was coming across of many,
*  many researchers in the 80s that language has a particular sits in a particular kind of formal
*  spot. It's called mildly context sensitive. So so that's a description of the kind of system,
*  kind of formal system that human language seems to be the best match to. And so so we can identify
*  this with like human language seems to be mildly context and has that formal property. And so
*  an interesting question is, well, are there other systems, cognitive systems that are also themselves
*  mildly context sensitive? And I don't know if that's been answered. If it has been, I would love to
*  hear it. That's interesting. But there are other hierarchical systems. So action planning, you can
*  see is hierarchical, but that doesn't make it in fact, mildly context. There are other kinds of
*  hierarchical formal systems that don't have that level of expressivity. Right. So I mean, I know
*  that like Chomsky came up with context free. Yeah. So these are formal systems that can be
*  tested out and yeah, these are yeah, the properties of these systems can you can ask does it does a
*  particular set of behaviors say conform to a system that has, you know, this level of expressivity or
*  maybe more expressivity. And of course, the challenge is, you can go all the way up to a Turing
*  machine, which is is as much as you can give a system. And the challenge there is that, well,
*  how do you learn that system? And so so linguistics has long as you know, since the cognitive
*  revolution being confronted with sort of what is the level of complexity of the system, and how do I
*  balance that or against like, well, how do kids kids have to learn this system, and they're not
*  being taught it, they are figuring it out. And I don't know about your kids, but my kids can't
*  figure out how to take a bath. Oh, my God, I don't want to talk about it. Exactly. But they can figure
*  out complex relative clauses and asking complicated questions between dependency between and
*  understanding how how words in one sentence relate to words is said, you know, not just five
*  minutes ago, but months ago. So they figure out these linguistic dependencies without being taught.
*  And and that is that's remarkable. And that is intention with the complexity of the system
*  they have to master. So the system has to be simple enough, or they have to have enough
*  kind of built in biases to know how to how to make sense of this system, whatever its properties are.
*  Yeah, well, this is we could really go, go deep in this stuff, you know, with the Chomsky's view,
*  and then the rebuttals and yeah, yeah, yeah, yeah. But the core thing about language is,
*  is this idea of the complexity of linguistic system does seem to be at least I haven't seen
*  any evidence that language has the kind of other cognitive systems have the kind of complexity
*  language does. And that's an interesting puzzle to sort of nail down. So the embodied cognition world
*  or was all tied up with the study of language as well. Yeah. Yeah. Is embodiment necessary for
*  language? As we understand it? Do we need bodies? I mean, is it you know, because there are parts of
*  language, like you said, is tied into everything. Yeah. And it's tied into our motor responses and
*  ours. Yeah. I mean, what do you mean by embodiment? And what do you mean by embodiment? I don't know.
*  Yeah, but but in the sense of, let's say humans, not not machine, but humans, right? So,
*  you know, an example is if I'm telling you a story about two people having a conversation,
*  as I'm telling you what person A says, I kind of step over and face one way. And then I shift to
*  person B who's responding and I step to the other side and as if I'm talking that I'm mimicking the
*  two people, right? And that's all tied up in the words that I'm producing and spinning out. Yeah,
*  I mean, I think no, the answer is no, I don't think language is embodied. I don't think we need
*  embody we need to embody words or to understand language. I think that, you know, the way we
*  learn about the world around us and words is indeed embedded in our sense, our sense perceptions and
*  our actions. But we don't need to use so the theory of embodiment I'm thinking of is a theory
*  that says that we use our perception action systems not only for sort of perceiving and for
*  acting, but also they are necessary for the act of understanding itself. So if I'm going to understand
*  you talk about cats that I am and making use of my sense, my sensory system, such in the way that it
*  responds when I see my cat, for instance, in order to understand what you're saying, I absolutely do
*  not think that's the case. So you don't so language is independent is it is meaning embodied in that
*  sense then? So the way we understand the way that we derive meaning from things is that an
*  environment a necessary component? I don't think so. I don't think so. So so there are some
*  remarkable studies where you know, you can you either look at individuals who who have experienced
*  lesions in say, their motor system, and their ability to understand action words, say,
*  words like kick or throw, it are no are not detectively different from words of individuals
*  who who have experienced those lesions. Where you can look at work David Kemmerer has done some
*  remarkable work with Parkinson's patients who have you know, neurodegenerative diseases targeted so
*  their broad versus they can perform a wide variety of actions. But if you probe their semantic
*  knowledge of those actions seems no different from people who have not experienced that different.
*  The other side of this is you can ask well those people, they develop those representations with a
*  healthy neural system. So maybe that that's it. But then you can look at children who have lifelong
*  cerebral palsy. And you can probe their speech perception, which people consider to be possibly
*  embodied. And you can also probe their semantic understanding. And I think there's a lot of work
*  to be done with this in those sorts of studies. But my read of them that I understand is that
*  these children have no not detectively different capacity for speech. So complicated because you
*  have a lot of comorbid deficits in these individuals. But you can certainly see individuals
*  that have very severe like lifelong action performing capacity, maybe speech production
*  capacity, but their difficulty with speech comprehension or word comprehension is relatively
*  mild compared to deficits with production. So those sorts of asymmetries, production perception
*  asymmetries are are difficult to capture with a fully embodied theory either of speech perception
*  or of meaning. Well your specialty is words and sentences, sentences and then
*  sub sentences, which is very broadly what does it take to process a sentence? Yeah, yeah. So yeah,
*  okay, let me let me think about this. Try to try to draw a semantic tree structure in words. No,
*  I'm just kidding. Yeah. Well, I mean, so, so when we're understanding a sentence, we have to
*  understand two things, right? We have to understand the words and the word meanings, and we have to
*  understand the structures, the way the words are fit together, the syntax, in order to derive how
*  the word means combined to form the meanings of phrases and the meanings of sentences. So this is
*  compositionality. We understand the meaning of a sentence because we understand the meaning of the
*  parts and the way those parts are put together. So the job of the understander, the job your job
*  right now, or my job when you're speaking, or anyone, if there would be anyone listening,
*  is, yeah, is they have to figure out from the sequence of, I mean, I'm going to say a sequence
*  of words, but that's, of course, not what you're hearing. You're not hearing words. You're hearing,
*  you're hearing air hitting your ear drum. Right, right. So there's already this sort of radical
*  complexity and abstractness of what we mean by word. Let's just ignore that and say we have a
*  sequence of words, but now we need to understand the structure that those words belong to. So the
*  phrases, like the fact that an adjective is, you know, if I'm talking about the red boat, then you
*  know that that red is telling you something about boat. I can, of course, say the boat is red. Now,
*  red is in a totally different part of the sentence, but it's also telling us something about boat.
*  Again, I painted the boat red. So now red is in, I've reconfigured that sentence yet again,
*  but it's still the boat that's becoming red. And I'm now telling you something about how that event
*  happened. So you are able to sort of to take these individual words and identify the dependencies
*  between them such that you can start to understand the way their meanings influence each other.
*  And do it so seamlessly. We do it so seamlessly. I mean, it's just, like, I would love, it's just
*  wild. Like, it's just, it gives me the stop and just sort of be amazed. And so this is, I mean,
*  this is where I start with my classes, my undergraduates, is just being like, you guys are
*  amazing. This is phenomenal. And we can't, I mean, we can build, we've been talking for much of this
*  conversation so far about how amazing AI is. But in fact, if you compare it to a four and a half year
*  old, it's awful. Like, let alone, I mean, there's like most recent advances at Google, but just try
*  having a conversation with like the Verizon helpline. It's terrifying. And so, but we do this
*  remarkably well. And we do it under adverse conditions of noisy environments. We do it with
*  speakers who are, who we've never heard before. Like, try to get Siri to recognize a voice that's
*  never heard before and the accent it's never heard. I mean, it's going to be a disaster.
*  But Siri doesn't wake you up at 6 a.m. and just start chattering immediately, you know.
*  Okay. So kids pose their own challenges, but we can wake up at 6 a.m. and be like, wow,
*  you use that relative clause. So beautiful. That's how you feel. You wake up and you say,
*  you're amazing. That's not how I feel. That's not how I feel. But so, so, so what do brains have to do?
*  They have to understand these structures and have to do so incredibly rapidly. And I think prediction
*  plays a role in how we do it incredibly rapidly because we can do some of the work ahead of time.
*  We can basically say, based on what I know about who I'm listening, who I'm talking to, based on
*  what's been said so far or other experiences I have, I can make a guess about what's coming up
*  next. And now my job in the moment is not taking a word and figuring out its meaning and then
*  figuring out the syntactic structure and then figuring out what that means. That's not the
*  job I'm doing in a quarter of a second. The job I'm doing is, is this word a match? And if it is,
*  then I can carry on. If it's not, then I can start doing some revision operations. But the
*  idea is that by kind of offloading the work that is demanded of you by every time you get a word
*  into sort of what can you do ahead of time, you've made this task a little more efficient and kind of
*  better suited to the speed that we communicate. We talk two to four to six words a second. And
*  that's a serious task. Yeah. And it's effortless. So in natural language processing, the way that
*  a network is trained is you take Wikipedia, some sort of big text, right? And just throw it at it.
*  But in the lab, you can't really throw Wikipedia at a poor undergrad and say,
*  you know, process this and tell me what you predict. So classically experiments done using,
*  are done using constrained language tools like lists and phrases and stuff. But like much
*  other current efforts in science, trying to go toward more ecologically valid types of studies,
*  you find it important to use natural language in the lab to study. For example, sentences in brains,
*  right? So why is that? Why do you find it important to use natural language? Yeah. Yeah. I
*  mean, I think there are two reasons that have really been driving me. One of these reasons
*  is generalizability is asking to what extent, you're asking questions about how the brain
*  processes language that I think generalized to the way the brain is processing language when we're
*  not in the lab. And so if you're confronted with a set of sentences, each of which may or may not
*  end with a word that's very unexpected over and over again, and these sentences are all unrelated
*  to each other, that's just not, I don't know about your life experience, but that's not,
*  that tends not to be the kind of language I hear on a day to day basis. So there are questions about
*  generalizability from those sorts of very carefully, thoughtfully constructed experiments. Yeah. But
*  related to that question of generalizability is, well, what is the human or maybe the human's brain?
*  What are they doing when they're confronted with those sentences? So what is the theory of the task
*  that the participant in the experiment is doing? And my read is that there are kind of a number of
*  experiments that are typically used in, say, neuro linguistics, these isolated sentence type
*  experiments, where the theory of the task has not been specified, maybe quite as fully as you might
*  like. Right? So it's not, it's not specified. So for instance, it's not specified exactly what
*  are the processes that are required to understand this word when it's out of context, such that I
*  can take that data and ask, okay, now I'm going to look at more natural language and see, well,
*  how is that same process being used in this more natural context? Like that level of detail of
*  theory development isn't necessarily widespread. So it's the second concern that has drawn me to
*  natural language, because in fact, that is a domain where I think we have some pretty well
*  developed theories. That's because the theories that have been developed in places like psycho
*  linguistics and fields like NLP, as we've already been talking about, are aiming to be theories of
*  well, what are people under how are people understanding language in their environment?
*  So when I'm going looking for what are theory, what are tasks that we have reasonable theories of
*  listening to a story for understanding is a theory is a task that I think we have some actually kind
*  of useful, partial theories of. And so that's a it's a complex task. But but but these useful
*  partial theories are, I think, useful scientifically. You want to talk a little
*  bit of science like an example of what you've done? Okay. So this is a very recent paper. I'm
*  not sure if this is the one that is now a year old that you've had is just outstripped now.
*  But this is your 2019 PLOS paper hierarchical structure guides rapid linguistic predictions
*  during naturalistic listening. So yeah. So most NLP uses sequential language models to process
*  text and language. Yeah. But language, grammar and syntax is a hierarchical structure. Yeah.
*  So it's a question whether our brains process language hierarchically isn't that strange that
*  that's a question, but it is a question. Well, let me can I jump in? Yeah, please. So there
*  are lots of ways to phrase this question. So so do our brains process language hierarchically?
*  That I don't think is a question on the table that you cannot capture the pattern seen in the
*  world's languages without accepting that the brain processes language hierarchically. Right. So so
*  just because we can't see the hierarchy doesn't mean it's not there. Right. We didn't have to see
*  genes to know how to develop gene theory. You didn't have to see electrons to know that they
*  explain properties of the atoms. But you could it couldn't it be a question that mechanistically,
*  the brain doesn't have to process it hierarchically that it could be done at an algorithmic or some
*  higher level. And this is a ridiculous question. I mean, no, I'm not sure. I mean, I think. So what
*  are you saying when you say the brain processes language hierarchically? So let me see if I can
*  put this at all cogently. And I might totally fail. But folks, he's been up all night with his
*  child, by the way. He let me in on the secret before we started. So yeah. So yeah, that's a
*  lame excuse. But hierarchy, you need to appeal to the fact that the brain represents hierarchies
*  to capture the patterns in the world's languages. The question, the more narrow question that I think
*  is live in the literature is I guess there are two ways to put it. One is like, well, how rapidly
*  do we kind of derive or make use of those hierarchies during language processing? Because
*  that generalization from linguistics is a generalization divorced from time. So these
*  are linguistic patterns that you develop from asking someone about patterns of sentences that
*  are or are not acceptable in their in their language without really worrying about like,
*  well, how rapidly did you process it? Or anything like that. So these are offline tasks where you
*  ask judgments about sentences or sentence meanings and make assessments about the grammar
*  underlying those sentences. So one question we can ask is like, well, is the brain sort of
*  recognizing these hierarchical structures rapidly or is it sort of more of an offline thing?
*  Gotcha. A second sort of dimension of open debate goes back to task, which is something that has
*  come up a couple of times in our conversation. So what are you asking people to do such that they
*  might make use of hierarchies in the brain? And one, I think interesting research domain
*  developed by people like Fernando Ferreira has been, are there certain kinds of tasks in which
*  we use language but don't necessarily make use of some of the more abstract aspects of linguistic
*  representations in order to serve that task? So when I'm giving this in a lecture, like I can very
*  easily, my students can easily kind of understand that they might not be listening with their whole
*  brain. So yeah, so we're not using the entirety of our computational capacity to sort out all of
*  the hierarchy in things that aren't necessarily hierarchical. Is that the...? Right. I think
*  that's a live theory. And this is what your paper is kind of testing. That's what we're testing. And
*  that's where naturalistic comes into it. So we give people a very simple, in this case,
*  naturalistic, kind of natural-like task of listening to an audiobook. And as you already
*  previewed, they're listening to the first chapter of Alice in Wonderland. And it's important to be
*  clear, like the first chapter is not as weird as the rest. So the first chapter, Alice is sitting
*  with her sister, a rabbit comes by, it talks, it jumps down a hole, she jumps down the hole,
*  she has some marmalade while she's falling, she lands at the bottom, she's lost. You know the story
*  very well. Yeah. I've listened to it a few hundred times. But it's not this weird Jabberwocky poem,
*  it's just plain sort of late 1800s prose aimed at children. But we can ask, they're sitting in the
*  lab, they know they're going to be answering a couple questions at the end of the experiment
*  about what happened. But it's just like what happened in the story. It's not like detailed
*  questions about syntactic structure, about individual sentences even. It's just about plot
*  points. So there's a real question, are they making use of this abstract, maybe computationally
*  expensive mental representations to achieve this task? And that's sort of how I think of the
*  question we were targeting in that paper. So are we making use of these abstract,
*  hierarchical representations in the service of this naturalistic task? And the answer we come
*  up with in that paper is yes. Well, yes. But okay, so well, you tested three different models out to
*  see. Okay, first of all, let's just back up. So what you're looking at is neurocomputational
*  models. Yeah. Maybe just describe what a neurocomputational model is broadly. Okay,
*  yeah. So we I mean, this is a term that is definitely a term you use to get grant money.
*  That's the key. That's the start where you use the term neurocomputational model to get grant money
*  and different people mean different things by it. So what I mean is a model who's going to produce
*  outputs, those outputs, which I'd like to ask, like whether they align better or worse with some
*  neural signal. Yeah. Others are going to use it. We actually alluded to this earlier,
*  asking more like are the internal states of the model, like unit level activations,
*  approximating things I can measure from the brain. And we're not using it in that way. We're asking
*  about outputs of the model being, you know, suitable for fitting against outputs of some
*  brain measurement I've taken from humans. So that's how I use neurocomputational. Okay. So
*  in these models that you used, you tested three, you input some language, and then it spits out
*  what you call a mental state. And then you transform that mental state into a prediction
*  of the brain signal and then match that prediction to the actual, in this case, EEG signal
*  that you were recording. So you tested three models. Two of these models were, well,
*  the Ngram is the most traditional language model out there, I guess, which is the first model.
*  So these were sequential models. Actually, maybe you can just take us quickly through the three
*  models. So we're looking at three models. So one of these models, a model called the Ngram model,
*  is these are all language models, by the way, which you already kind of introduced us to. So
*  they're all, they have the job of predicting the next word. And the Ngram model is going to predict
*  the next word based on the previous two words it's encountered, a third order Ngram model.
*  So that's a very limited little sequential window. I know the two words I just heard,
*  what word is coming up next. And if you're looking at a sentence like about like my sister,
*  who was visiting last week, is about to, it's like, now you have about to, is all that the Ngram
*  model sees when it's about to predict the next word, all the other stuff it's ignoring.
*  Gotcha. The second model that we look at is a simple recurrent network. This is a very classic
*  artificial neural network that has three layers. The middle or hidden layer is recurrently connected
*  back to itself. So that means that the output at any given word is going to reflect the input
*  and also the previous state of this hidden layer. And that, that hidden, that recurrent connection
*  allows it to represent the context that the words it's seen before, but that context is going to be
*  represented in a sequential way. These were, I think they were called context elements originally
*  in the vanilla recurrent neural networks. Anyway. Yeah. I mean, if you look at Elman's papers from
*  the late nineties, so these are also called Elman nets. You know, you basically have the hidden
*  layer and you, you, you, the way you talk about it, you copy the hidden layer to a context layer,
*  and then that serves as the, that context layer plus the input is the input to the hidden layer.
*  Next, but you know, it's the same mathematically as just drawing a circle from the hidden layer
*  back to itself. Very good. And so, so one property of these context networks, these, these simple
*  recurrent networks is that the output at any given state is going to be, you know, a mixture
*  of the input it's seeing and the, and the hidden layer. So that hidden layer and sort of what it
*  previously saw. And now you go on to the next word and you have just one previous state,
*  which is self influenced by its state before, and you have the input and now you go to the next
*  and you have that again, the new input and you have the previous state and then the previous
*  state before that, that that's been influenced by the previous day. But at each point, you're sort
*  of more and more distal you get from the current word, the less and less that context has an effect,
*  efficacy on, on updating your new output. But it's still sequential, still in order.
*  In this way, it's sequential, right? So there's a strong proximity bias. So the immediate context
*  has a strong effect and more distal context is going to have a less strong effect. So this is
*  the second kind of model we use as a, as a model that can accommodate sort of arbitrary length
*  previous input, not just the first, the previous two words, but with a strong sequential bias to it.
*  And then the third network we, we, or the third language model we test is of a different kind of
*  flavor, right? Is it, is a context free, a probabilistic context free language model.
*  So in this case, you're going to ask, what's the probability of the next word by querying,
*  by looking at the grammar, the syntactic structure of everything you've seen so far.
*  So if you have a sentence, I don't know what the sentence I gave a moment ago, but my sister who
*  was visiting last week is about to, you have something like you have a prepositional phrase,
*  you have this auxiliary verb phrase is, is about to, and then you have my sister who was visiting
*  last week. So that's like a subject noun phrase with a relative clause in it. So all of these
*  little syntactic nodes are, are available for the language model to then ask, well, what's the
*  probability of, you know, my vocabulary of all my vocabulary, what's the, what's the distribution
*  of probabilities of that vocabulary given this, this syntactic information. Does that kind of
*  get us where we need to be? Yeah, it does. And you said, well, who wins? Well, so, so we're asking
*  about, in that paper, EEG brain signals record what people are listening to the story. And we see
*  evidence that there are, are sort of rapid within about 200, 250 milliseconds, EEG signal that's
*  sensitive to the probability of a word. And this is like old news, right? So the one reason I like
*  using EEG for these studies is that EEG is exquisitely sensitive to brain signals reflecting
*  unexpectedness, reflecting surprise. Surprising, I guess, is the surprise. Surprising is this term
*  from information theory about how much information a word is giving us. And a word that is unexpected
*  is giving us a lot of information. And in your case, you're actually looking at the
*  surprise all due to parts of speech. In that paper, that's right. So the language models are all about,
*  is the next word going to be a preposition or a verb or a noun or an adjective? We have other work,
*  which I want to circle to in a moment where we are looking at the probability of word as an
*  electrical item. This paper, yeah, it's part of speech. Okay. And the brain, the EEG signal is
*  exquisitely sensitive to these sorts of surprising inputs, both surprising parts of speech and
*  surprising words themselves. Sorry, surprising relative to the probability distribution of
*  expected other parts of speech and other words, right? That's how we model it. That's how we
*  model it. But the literature tells us that, you know, when you measure, so the classic way to
*  measure surprising is you ask 100 undergraduates, fill in the blank. And a surprising word is a word
*  that never gets filled in. And so we know a lot about the brain signal from those sorts of studies.
*  So what we see is that the probabilities, when those probabilities, like what's unexpected,
*  are estimated based on these hierarchical information, those probabilities are sort of
*  better lined up with the ups and downs in the brain signal versus those probabilities when you just
*  take into account the sequential information. But that's important to say that it's not
*  either or, right? So, and we see this supported by the data, though we're far from the only one
*  showing this sort of evidence that the brain is also exquisitely sensitive to this sort of
*  sequential information. So a word that's unexpected based on the immediately preceding two words
*  is going to drive certain brain signals pretty robustly. A word that's unexpected based on the
*  sequential context that goes back a little farther is also going to show a very clear
*  statistically reliable effect in our data. What we see is that the hierarchical information
*  predicts certain brain responses above and beyond those other models. And so that's for me,
*  the little scientific little tiny step up from where the literature was at prior to the paper.
*  It's not either or. It's not we're right, somebody else is wrong. Okay, maybe we're a little bit
*  right. But it's that this information has this hierarchical information is doing some work
*  for the comprehender in terms of making predictions about upcoming words, in addition to whatever
*  variety of other information they're using. And that's interesting, especially in this naturalistic
*  task, where there's live theories on the table saying people can just ignore that computationally
*  expensive, abstract, chomsky representations in this sort of simple task. And we think this is a
*  little bit of data, so you can't ignore those kinds of representations people are using them,
*  because they're valuable. They have valuable information in them.
*  So now when you're giving a lecture and you're looking out into the student's eyes, can you
*  point and say, you're sequentially processing, you're hierarchically processing?
*  Yeah, yeah, yeah, I can see the trees just emerging from their heads. Like, okay,
*  there's exactly the dead eyes, you are only sequentially processed. No,
*  because they're all amazing, of course. But yeah, well, it all gets filtered through
*  attention. So if you're not attending, yet, you're not going to do processing.
*  Okay, there you go. So this idea of hierarchy in has been interesting to me for a long time,
*  in part because it's live in terms of like how, how quickly we're recognizing hierarchy,
*  and, and whether we're doing it in sort of a range of tasks. And it's sort of an important
*  building block for me of getting back to some of these questions of linguistic representations
*  that I started my career on, and I'm still very interested in. Because we, you know,
*  it's sort of establishing where in the brain, where in the brain signals that I'm able to record,
*  can I go looking for, for evidence that's going to connect with maybe some question about,
*  about phrase structure, or question about sort of how verbs are represented, or how nouns are
*  represented. And so these sorts of theoretical debates in syntax, about the nuance of sort of
*  what a verb is, or what a prepositional phrase is, to get at those debates, we need to kind of have
*  a brain signal that's going to connect with those hierarchies. And so the first question is, well,
*  what are those sorts of brain signals? So that's sort of, so this is work that for me has been
*  important in building a bridge. We're still just building that bridge, but it's been built that
*  bridge. The way we've been tackling that more recently, though the paper came out before the
*  2019 paper that you're talking about, is making use of deep neural networks. So circling back
*  to stuff we've already talked about. So using deep neural networks at this algorithmic kind
*  of level of abstraction, where the network is carrying out a task of identifying phrase structure
*  that I think is analogous and interesting ways to the task that humans are carrying out. And I can
*  ignore the internal workings of the network, or at least I have done so so far. Yeah. Successfully.
*  Yeah, exactly. Hey, you have a job. Yeah, thankfully. And so these networks are nice
*  because we can train them on, I mean, what are these networks great at? They're great at training
*  on giant reams of data. So therefore, we can build these networks to predict sort of individual
*  words, not just parts of speech where we're training. We can make use of a lot less data
*  when we're predicting just parts of speech. And so this is with work with colleagues like Chris
*  Dyer and Adi Concoro and John Hale, who are Google DeepMind. And what we've been using a deep
*  neural network tool that Chris Dyer developed called a recurrent neural network grammar.
*  So this is a deep neural network that's built, in particular to represent the kinds of abstract
*  hierarchical structures that we know that language makes use of. So it learns and operates over these
*  sorts of structures. And so now we've been using this as a tool to see sort of what extent can we
*  again see evidence for these sorts of structures in the human brain data. So we confront the
*  neural network with Alice in Wonderland in this case. Of course. And then we can derive various
*  measures from the network. We can derive how likely it thinks the next word is. We can also
*  drive other measures like how many kind of states did the network explore as it was confronted with
*  a new word and before it got ready to go on to the next word, something about the complexity of the
*  representation that it's operating over each word. So this is a different kind of complexity
*  than what we could get from the language models that we were talking about a moment ago.
*  That's exciting.
*  And so we have these two measures we can compute from the recurrent neural network. And then we can
*  take advantage of some beautiful work by Adi Konkoro, co-author on the paper, where we
*  essentially ablate the network. So we remove aspects, a component of the network. And what
*  we remove in this case is the component whose job is to look at a particular structure that it's
*  identified based on the sequence of words and reconfigure its internal representation to compose
*  those words into a single memory representation. So this is composition. We've talked about this
*  before. So it's identified a structure and the internals of the network, once it's identified,
*  in this case a phrase, it basically recomputes the internal representation of that phrase as a whole.
*  And we can now take out that component, that internal component of the network,
*  and we replace it with a sort of a standard which just adds a new symbol to the memory
*  representation. It's like, okay, phrase over. It doesn't recompute that phrase representation,
*  it just says phrase over.
*  Consolidates.
*  Yeah, it doesn't reconsolidate. So we could have a version that composes,
*  consolidates in your terms, and a version that doesn't. And then we can also use now
*  as a baseline sequence model, a state-of-the-art recurrent neural network, not this simple
*  recurrent neural network that has just three layers and has this very strong bias towards more
*  recent information. But in this case, we use a long short-term memory network, LSTM. So that
*  is a network that can dynamically reweight aspects of its context, its history, in order to take
*  advantage of information that it encountered many, many words ago in as much as that information
*  might have utility for predicting the next word. So it can learn, depending on the way in which
*  words, both distal and proximal, have utility in particular next word, it can in principle learn
*  those relationships. So this is a pretty strong baseline when you're considering, well, we
*  consider a pretty strong baseline when evaluating the role of this explicit encoding of hierarchy
*  compared to the LSTM that can implicitly recover long distance dependencies, but it's not built in.
*  Does that make sense?
*  Yep. It's exciting.
*  So we have these networks, and we take the exact same Alice in Wonderland EEG data set that we were
*  talking about a moment ago from the PLOS ONE paper, and we ask to what extent can we capture
*  dynamics in the EEG data from both the probabilities of the next word and also these estimates of how
*  many states did the model explore as it moves from word to word. And under both measures,
*  we can see evidence that the hierarchical encoding, and particularly the explicit
*  composition available by this recurrent neural network grammar is improving our ability to
*  characterize, to predict the EEG data, and just again predicting the EEG data word by word,
*  and in terms of individual lexical items, not say parts of speech. So in this way, this paper that
*  came out now a little over a year ago, it fills in some gaps that are left over from our PLOS
*  paper, but it's tackling it from a slightly different perspective too. I think one thing that
*  I'm slowly learning, way too slowly, is things that I used to think were either-or propositions
*  aren't. So we just said this a moment ago when it came to sequence versus hierarchy, and the thing
*  that I'm now confronting is part of speech versus individual lexical items. So two years ago,
*  I would have thought that, yeah, we're building a set of models predicting EEG data for parts of
*  speech because that's doable. I could do that with the tools that I have in front of me,
*  and I'd really like to be doing words. And then I got new tools and new collaborators, and we were
*  able to do this work that for me has been really exciting, and we can predict individual words.
*  And now, in fact, asked by a reviewer on a kind of a follow-up work to the paper I was just talking
*  about, a reviewer said, well, what's going on in this new model, and how does it compare to some
*  of the other models? And I really want to see the full story together. And I was like, oh, more work.
*  But as happens way too often, is that that was work that was well worth doing because
*  looking at these different models that were developed at different times with slightly
*  different goals and without really communication between those two model building efforts,
*  they communicate with each other in that they're answering similar questions, but
*  they're developed with a slight different, you know, for different agendas, right? But the models
*  are doing similar things, but they're also doing different things. And in fact, both these differences
*  are matter for the brain data. So it's not the case that one family model is just bar none better
*  than the others. So in some aspects of the data, one model does better. Some aspects of the data,
*  both models are contributing or the models are indistinguishable from each other.
*  So one thing that we're, you know, I'm kind of excited to think about, there are lots of things
*  I'm excited to think about. One thing is, is to what extent do we want to think about these sorts of
*  activities of these models, in this case, part of speech versus individual Alexa, as capturing
*  different kind of streams of processing that indeed are going on in people. And this is not
*  unfamiliar from psycholinguistics, right? That people are going to be making predictions
*  at different levels of representation, different aspects of what we might be seeing or using these
*  different levels of representation simultaneously in their competition. So this is familiar.
*  I needed a reminder, I guess that's my way to put it.
*  This is great, John. So we're, you know, we're coming up on time. And actually,
*  I just got an email, Paul, before you talk to John, I just developed a new model that
*  will fit his data better. No, I'm just kidding. Well, I mean, I should, if I can just advertise,
*  like all of our data is online. So we, and I kind of try to try to say this whenever I give a talk,
*  is like download the data. Yeah, we have our annotations are online, the data, the EEG data
*  is online, we have an FMR data set that's going to be released, I think at the end of the month.
*  So the point of this, the other thing about the great thing about the naturalistic data,
*  I mean, this is pure sales right here. But is that it's once you put it out there, like,
*  you can develop your own model. And we and you can either ask your own questions with your own model,
*  or if your model is trying to do similar stuff as our model, then we can pick these models against
*  each other. And that model comparison is for me, so exciting, because we have sort of a ground that
*  we can agree on a particular data set challenge data set. And when we build our models, our
*  assumptions are just out there in front of us, like, this is what we think is going on, or this
*  is what I'm committed to right now. I know it's wrong, but it's the best I got right now. And now
*  we can have a very kind of concrete discussion. So we've been following a lot of kind of
*  groundbreaking work from others trying to get our data out there. So that we not only do we know
*  we're wrong, but you can help us understand like, well, how are we wrong? And how can we be less
*  wrong? There's the challenge from from john guys. Hey, so in our in our remaining just a few minutes,
*  can I ask you some just broad kind of I get a lot of emails actually wanting advice from people.
*  Okay, you're ready to help some people out here? I will see. Well, so I mean, the main thing, you
*  know, is how would you if you were going to do it over and, you know, start a new, how would you
*  begin the study of, let's say, linguistics or neuro linguistics? I don't know. I mean, there's
*  so many things that was so lucky for me, including the my my PhD advisor, my other students who began
*  their PhD, I did the people who I ended up talking to at colloquia or at conferences. I mean, I just
*  got lucky. Well, was it fortune is the is for a prepared mind. I don't remember the exact fortune
*  favors the prepared mind. I don't know about prepared mind. But I do think that one thing that
*  I was encouraged to do and and I was given support in doing and really paid off is is just going out
*  and talking to people. So go to conferences, go to I mean, we met at the CCN conference computational
*  or cognitive computational neuroscience. And that is that's not a community that I I mean,
*  I'm a linguist, right? I'm not a computational neuroscientist at the end of the day, but just
*  going to a conference, encountering new ideas and new people has been so valuable for me
*  to learn new things for myself, but also to talk to people who can help me do what I want to do,
*  understand what I can't understand myself. Right. And so when I look back at what's worked, it's
*  it's these sorts of personal connections and being supported and going out and finding those
*  connections. So I don't know what I would do differently. But that I mean, I couldn't imagine
*  doing what I'm doing now without the connections I have, the colleagues I have, the students I have,
*  and the opportunities that I had as a graduate student and postdoc,
*  junior faculty in getting out and talking to people. What's something that that you maybe
*  invested some time in that you think back now you wish you'd skipped? Oh, um, what was a complete
*  waste of your time? Besides doing podcasts? Not that there's not a lot. I mean, I wish I invested
*  more time in programming. I have no computer science background. And I mean, there are two
*  ways that that would be paying off better now. One is that we do a lot of programming just in
*  the service of doing our science, programming our experiments, program our analyses. And the more
*  I talk about to computer scientists and computational linguists about theory building, the more I kind
*  of wish I had some foundation. So I would have had to given up something in order to spend more time
*  learning computer science. I don't I don't know what I would have given up. I actually don't have
*  a solid answer for that. You mentioned that children will invent their own languages if they
*  needed. Will future AIs invent new languages or even use language as we know it?
*  I don't I don't see why not. I mean, I think I mean, in as much as we want to build AIs that
*  operate like children, I don't see why that's not something that could potentially happen. But also
*  in as much as AIs are going to do something that's totally different from what humans do
*  and develop their own. I mean, I guess, OK, I'm a believer in the singularity, I guess. Can we say
*  that? But I'm not worried about it. And I'm not worried about it anytime soon. Yeah, OK.
*  So so if it's like, yes, one day, sure. But is it going to happen at Google Research in the next two
*  years? No, I'm really but but OK, so there's the singularity. There's this concept of the
*  superintelligence, right? Yeah, quote unquote. And it's very scary, very scary to very rich,
*  loud people. It made me think like, OK, so I can you can kind of understand what what
*  superintelligence looks like in terms of figuring out how to construct paperclips or whatever,
*  whatever analogy or story that you've heard. It's another thing to think of what is super
*  entailed. So what is superintelligence in the realm of language? Like what would a superintelligent
*  language look like? Oh, I don't. Yeah, I don't know. I've never thought about that.
*  I wouldn't recognize it because I'm way down on the spectrum, I think, with language. But
*  like it's going to it's going to take over language. What what does that mean? I don't know.
*  I don't know if that has. Yeah, I don't know if that's well, well framed. I mean,
*  that's what this whole podcast is about is framing things poorly. So I feel like that's a good summary
*  of my career. But it's framing things in a way that are like helpful for someone else to say
*  what you've done wrong. But yeah, I mean, we don't. Yeah, I don't know. I guess I mean, one thing that
*  I get worried about, again, is this idea that like even like language like language as a useful
*  term. Right. So we're talking about really like meaning as a useful term. It's like human language
*  is a totally useful term for me because like I think I understand. Well, if that's a phenomenon
*  I want to understand, I can delineate that pretty clearly. There are going to be edge cases, but
*  but most I can do it. But if you want to say, well, language, if you want to back off from human
*  language, say, well, language, and maybe you're going to talk about languages, artificial
*  intelligence could develop or maybe you want to include in their language, like things that people
*  call language, like they might call, you know, the way bees communicate kind of bee language,
*  or they might talk about music as a kind of language. So people use the word language
*  in this bigger sense than human language. And again, it's like, well, you that might be a very
*  useful way to talk casually. I'm not sure that's, I don't know what it means when you want to put
*  confront me with like scientifically, what is that? You know, it's common to all those embodied,
*  they're all embodied. All right. I think you just got the last word and I'm not totally
*  I'll edit it out. Exactly. No, but I think this is a great place to to end up is,
*  you're not happy with the word language. I like that. That's it. Yeah, no, I'm yeah, I'm generally
*  not happy with with terms. I find terms to be kind of limiting. And it's frustrating. Right. It's
*  like, well, what are you studying? It's like, well, I'm studying language. Well, what do you mean by
*  that? Okay, I can't like linguists can't define the word word. Right. This is great. Well, we can't
*  define anything. So let's just give up. Right. No, no, but we can we can be less bad. I mean,
*  this is this is I don't I have to do it. I mean, this is like constantly what my students and I
*  are talking about is, you know, you come up with a difficult challenge. And if we actually if we
*  can end on this, I'd be a little happier. But you come up with a difficult challenge, and you're
*  not quite sure it's like what this is wrong. And that's wrong. And so I think it's definitely
*  wrong. You're like, and yeah, that's just all true. And is it like, is there something that's a little
*  bit less wrong? And is this term is bad? But is there a little a way you can tweak that term or
*  a way you can define it? That's going to be like a little less bad. It's going to help you
*  understand a little bit more and that being a little bit less bad. If I can do that, I'm happy.
*  John, I wish you plenty of future less wrongness. And hey, I really appreciate your time here. And
*  I will point people to is your website, the computational neuro linguistics lab website,
*  the best place to find out more? Okay. Computational neuro linguistic lab at
*  University of Michigan. Yeah, really appreciate it, man. Thank you.
*  Oh, this has been a blast. Thank you so much.
*  Brain inspired is a production of me and you. You can support the show through Patreon for a
*  microscopic two or $4 per month. Go to brain inspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying
*  advertisements like you hear on other shows. To get in touch with me, email paul at brain inspired
*  dot co. The music you hear is by the new year. Find them at the new year dot net. Thanks for
*  your support. See you next time.
