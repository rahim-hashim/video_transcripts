---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5938s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 7976
Video Rating: None
---

# BI 090 Chris Eliasmith: Building the Human Brain
**Brain Inspired:** [November 23, 2020](https://www.youtube.com/watch?v=rlvCFu7wx6o)
*  Our job as scientists and theorists is really often to unify these things and to say, you know,
*  what is some coherent description where I can use, you know, all the language from all the different
*  disciplines as we currently divide them up, right? The disciplines aren't reflective of nature,
*  they're, you know, historically accidents basically. Do we have that cognitive ontology correct? No. I
*  mean, there's almost pretty much no way that we're right. Is the simple way to say it that the goal
*  is to build a brain? I mean, just like the title of the book. Yeah, absolutely. How has that goal?
*  That's my shortest answer. Yeah, I love that answer. This is Brain Inspired.
*  Semantics. How does meaning get attached to processes? Syntax. How is structure encoded
*  and manipulated? Control. How is information flexibly controlled as needed in various
*  situations? And learning and memory. How are learning and memory instantiated? Hey everyone,
*  it's Paul. Those are the four questions that Chris Eliasmith spends his career at the University
*  of Waterloo pondering and trying to answer in the form of Spawn, his attempt to build a human brain.
*  If you've seen Chris's talks, you've seen the demonstrations of Spawn, receiving task instructions
*  into its one eye, processing the required computations in its spiking neural networks,
*  and performing the task using its arm to write an answer. Chris writes about all of this in his
*  book, How to Build a Brain, which I recommend and we talk about. The book summarizes his
*  philosophical approach as well as how he builds Spawn. He's also the co-founder and co-CEO of
*  Applied Brain Research, an AI applications company that spun out of his lab. I also got
*  some guest questions today from Brad Imany, Steve Potter, and Randy O'Reilly. So thanks to
*  those folks. Show notes are at braininspired.co slash podcast slash 90. If you find Brain Inspired
*  valuable, consider supporting it for just a few bucks a month through Patreon. Thank you as always
*  to the wonderful people who do that already and thank you for listening. All right, here's Chris.
*  All right, so I had Randy O'Reilly on a couple episodes ago and I started off by asking him this
*  question that I'm going to ask you to begin with as well. It was essentially how often do you allow
*  yourself to feel a sense of awe with regard to how far you've come personally and just how much
*  we know about brains and natural and artificial intelligence. Do you ever allow yourself to,
*  step back and just revere the amount that we've learned?
*  It's funny. Yeah, it's definitely tempting to do that and we hear about fantastic developments
*  in AI. Things like GPT-3 are really quite impressive, extremely large models that are
*  surprisingly coherent when you speak to them and so on. And we can see all the kinds of deep
*  insights that people are getting in neuroscience and the new kinds of techniques that let you
*  record from hundreds of thousands of neurons at the same time. Much of this is completely
*  unprecedented and super exciting but it never takes long for me to also quickly think of examples
*  that just seem so far away from what we can do. And the amount that we're missing, if we're looking
*  at a thousand neurons, this is like 0.00001% of what's going on inside a brain. So yeah,
*  the awe of how far we've come is often quickly replaced with the awe of how far we have left to go.
*  Do you feel that way in your own work with Spawn as well?
*  I do actually. I think that's not an unfair way to characterize it. I look at Spawn and I
*  can make it sound impressive. Six and a half million neurons, that's quite a few. Twenty
*  billion parameters, that's a lot of parameters. How did we figure out how to tweak them all such
*  that they did anything at all, let alone something kind of interesting? But very quickly, I also
*  realized we've got 20-ish brain areas and we definitely aren't fully modeling those and
*  out of a thousand or more brain areas, the model is 20,000 times smaller than the brain. Like,
*  20,000 times smaller is a lot smaller, right? So yeah, it's the same kind of experience that
*  I can definitely make myself feel good if I focus on the right aspects of the work.
*  But it doesn't usually take long for me to also just realize how miniscule it is in the
*  from the perspective of how far we'd like to go.
*  I feel like this is a cruel joke that is being played on us, that our reward systems can't just
*  accept, can't every once in a while just sit in awe of all of this stuff because we always have
*  to think, what's the next thing? The more we know, the more we don't know. I mean, there's this,
*  I don't know, it's a real conundrum. Well, we're going to talk about Spawn a lot, I hope,
*  during this episode as detailed in tons of your work, but most succinctly, I suppose,
*  in your book, How to Build a Brain, which is, what, eight years old now? Is that right?
*  Yeah. Yep. Making me feel old.
*  So it's a really nice book. I actually just tore through it and I wasn't able to do the,
*  I'm going to go through it again and do all the tutorials laid out in the book because,
*  so you begin by laying out your philosophy and your approach. And then, you know, it also details
*  how to implement these networks on software that you guys have built and is freely available.
*  And then you provide all these tutorials, which I'm going to go back through.
*  Yeah. I will let you know that actually the tutorials have all been updated to the latest
*  version of Nango, so you want to track those down online. The book is a little bit out of date in
*  that regard. I was wondering, like, how, yeah, how often that would be the case. I mean, you have,
*  do you have another book in the offing or what? No, we basically have just replicated all of those
*  tutorials and then new user interface. And it's a much nicer package than it used to be. And
*  it's much more closely connected to neuromorphic hardware, for instance, which is quite nice as
*  well. So. Okay, good. We're going to talk about that as well. Let's start with your approach a
*  little bit. So why is it important to build large scale models of the brain? Right. I think we sort
*  of touched on that with the very first question, right? Because the brain is very large and very
*  complicated and to expect explanations which are simple or uncomplicated is probably not
*  super realistic. I think, you know, we have some fairly compact explanations of physical phenomena
*  and people have often thought that maybe that's a good model for how we'll understand biology as
*  well. You know, so we have equations that seem to apply to huge numbers of motions, be it planets
*  or tiny little particles. But that kind of simplicity is not something I think we should
*  expect in biological explanations and biological systems. And so we really need to build models in
*  order to express our explanations in an appropriate manner and test them, test them in the same way
*  that we'd be testing any theory. So that's one important reason, right? It's just that we need
*  big complicated models because it's a big complicated system we're trying to understand.
*  And then another one is because it really forces us to specify our understanding, right? So I like
*  to quote Richard Feynman as I do in the book, that which I cannot create, I do not understand.
*  And so it seems to me that we need to build mathematical models as a way of expressing what
*  our understanding is. And in some ways, it's the only option, I think, when it comes to understanding
*  something like the brain. But mostly what is still being worked on are really smaller scale models of
*  particular functions, kind of in isolation, right? So you might have a working memory model. And
*  maybe you do it in a neural network. Maybe you do it in a box and arrow kind of higher cognitive
*  model. But then the large scale modeling has to bring all this stuff together and into a
*  coherent whole. So although I know that there's some balance in developing the model in bringing
*  in a new function and having to integrate it with the whole. So I mean, is it important to
*  have everything working together? Is that an important constraint? Yeah, I think that's a
*  little bit more of an idiosyncrasy on my part, building models which have a lot of parts and
*  putting them together. So there are models of similar sizes to Spawn like GPT-3, but it's
*  focused on language, right? That's all it does. And in fact, it's even larger than Spawn as far
*  as the number of parameters go. But it is more specific functionally, like you're saying.
*  I think the reason that in my work, we tend to focus on this kind of integration problem is
*  because part of my academic background is as a systems design engineer. And one of the things
*  that we focused on there was understanding systems, breaking them down and coming to realize that
*  it's the interaction between system parts that often is where our understanding fails or systems
*  fall apart or the real challenges arise. And so that's why it's important for me,
*  if we want to understand cognition and I think cognition comes about because of the interaction
*  of lots of different parts of the brain, then I want to build models that try to capture
*  my understanding of that integration. We have talked a lot on this podcast about levels,
*  levels of analysis and understanding. And the classic well-known version of that is David
*  Maher's levels. So you have the implementation level, which is the hardware and how it goes
*  about doing its thing, the algorithmic and representational level, which are sort of the
*  steps to perform the computation. And then you have this higher level computational level,
*  which is what computation, what function is actually being performed. And you talk about
*  that in the book as well. But in addition to that, you talk about levels of scale and you adhere to
*  what you call descriptive pragmatism with respect to levels of scale. What does that mean and why
*  is that important? Right. So yeah, that was definitely the philosopher coming out in me
*  there coming up with that funny sounding term. But it's very philosophical sounding. Yes, it is.
*  I was actually referring to something slightly different than Maher's levels. So in the
*  philosophical literature where people are wondering about levels, they're typically talking
*  about levels in nature. So Maher was talking specifically about levels in cognition or the
*  brain. But more broadly, if you think about levels in nature, there have been two prominent views.
*  One basically is a reduction kind of view, which is not that dissimilar from the way most people
*  interpret Maher, where you've got high level big phenomena and then you break it down into smaller
*  parts. So you take wood and you break it down to its chemical components, you break the chemical
*  components down into their atomic components and break those down and down and down. And everything
*  gets smaller and you give explanations for how wood behaves in terms of whatever level you want
*  to break it down to. So you're really focused on trying to implement this reductive relationship.
*  Putnam and Oppenheimer had that kind of view. And then when people started thinking about
*  psychology in particular, Jerry Fodor being one prominent example, they came to realize that that
*  kind of reduction doesn't seem to work very well. And so they came up with an anti-reductive stance
*  where they basically said that sciences like psychology stand independent of our ability to
*  reduce them. I should be able to give psychological level explanations and-
*  Stand alone.
*  Yeah. Stand alone. Yeah. Whenever I try to reduce them, something falls apart, right? That reductive
*  relation just doesn't exist. What I'm trying to do in speaking to that is to say, essentially,
*  these are ontological views. You're trying to say that in nature, there is a fact of the matter
*  about how levels relate to one another. And I'm instead taking an epistemic view, meaning that
*  it's really about what can we know, right? Or how is it useful for us to break up nature
*  in order for us to know it well, i.e. generate good explanations? And so descriptive pragmatism
*  is saying, well, the levels I'm picking out are really just descriptions, right? So it's an
*  expression via my knowledge. And it's one where I try to capture things like relations between parts
*  and holes. I try to talk about how lower level mechanisms give rise to higher level behaviors.
*  I can try to quantify the relationships. I'll write down some math to say exactly what those
*  relationships are. And ultimately, it comes down to specifying descriptions and levels
*  in service of an explanation of some kind. So I need to say, these are the questions I'm trying
*  to answer. And once I say that, then I'm like, okay, well, here is my level that I'm going to
*  talk about. So if I'm asking for a molecular answer to some neuroscience question and say,
*  okay, these are the levels I need to speak about. And do you speak about molecules and
*  receptors and some receptors and all that good stuff? But if somebody's asking a question about
*  reaction times, then I might have another level of description. And ideally, I interrelate these
*  descriptions, of course, and that's what makes them kind of levels. But it's not an imposition
*  in terms of saying, this is the way nature is carved, right? These are the joints of nature.
*  And so it doesn't have nearly the same, I think it's basically unlikely that we'll ever discover
*  what those are. So it's maybe a little bit more humble in that regard. It's really related to
*  what we know and how we know things. It's unlikely that we'll ever come up with a real
*  gritty corresponding mapping between levels, however many levels there are, let's just say
*  psychology and neuroscience for, you know, just to as an example, are we going to always just have
*  separate vocabularies and descriptions for the phenomenon we're talking about? Or are there
*  levels to be found in between that we will eventually have a new either vocabulary or
*  change our current vocabulary to map onto concepts that we're continuing to build on?
*  Yeah, exactly. And so I'm definitely in the latter camp where I believe that, you know,
*  our job as scientists and theorists is really often to unify these things. And to say, you know,
*  what is some coherent description where I can use, you know, all the language from all the different
*  disciplines as we currently divide them up, right? The disciplines aren't reflective of nature,
*  they're, you know, historically accidents, basically. So we can borrow whatever, you know,
*  language we want. Mathematics is really nice because it's often a way of being very specific
*  and precise about what relationships you're talking about. And so yeah, we want to tell that kind of
*  story where we still have levels show up, but we're not going to expect them to align to our
*  chosen disciplines like neuroscience and psychology, not at all. And I actually think,
*  so because you brought up Mara, I just jump on that for a second. A lot of people use Mara as
*  a way of kind of supporting that reductive view where they say, oh, you know, Mara had level one,
*  two and three, the ones that you specified, and they're independent. And that kind of independence
*  then makes you think, oh, well, I have to have some reductive relationship between the two.
*  If you read Mara, he doesn't think that, right? So he specifies these again as more of a practical
*  approach. Like if I'm going to come to give a model or an understanding, here's a useful way
*  to start to give descriptions that are helpful. And if you read his like 1980 book, the vision
*  book and so on, it really seems like he's much more integrative than people give him credit for.
*  And I've written a couple of papers on exactly that topic. Yeah, because I think it's kind of
*  the right view really to be integrative more than reductive. It's interesting. Tomaso Poggio,
*  with whom David wrote these levels things, you know, originally, and then he went on to
*  elaborate them. But he Poggio recently sort of updated his thoughts on the levels and added a
*  few like, I think learning was a new level and evolution was a new level. Anyway, I don't know
*  if you're familiar with that. So I haven't read the updated stuff. Okay, we I'll point you to it
*  maybe later, maybe later. So then I won't ask you about it. Let's talk about AI and intelligence
*  in general, then because in the book, and we're going to stick with a little philosophy here,
*  before we get down. I know you like this stuff. You like the philosophical stuff. Yeah.
*  You claim that it's not very opening paragraphs, I think in the book that in the last 50 years or so,
*  the real advances that we've made are not necessarily technological or knowledge based,
*  but instead about figuring out which questions are the right questions to ask. And that's a very
*  philosophical approach, because I think it's often the job of philosophy to figure out what is the
*  right question, right? So I don't could you elaborate on that a little bit? And, and I'm
*  wondering also, are we are we asking the right questions now? Or are we asking better questions
*  than the worst questions before? Yeah, I yeah, this is an excellent, excellent question. Right,
*  I don't think we're probably ever going to be the point where we're asking the right questions. I
*  mean, it's always difficult to answer that in so far as we can ask questions, which are so general,
*  they kind of have to be right, you know, like, how does the brain work? I mean, that's a question,
*  but and that's one we'll probably ask for a really, really long time. So maybe it's right in that
*  sense, because it will stay interesting. But I think the more specific you make your question,
*  right, then the less you're sure if it's the right one, right? It's, it's something that you're
*  looking for an answer to. But you don't know if that answer is going to lead you in the direction
*  of answering your higher level questions. And in the book, I actually specify four questions.
*  And I'm still asking those, I'm sure I'll be asking them for the rest of my career.
*  Yeah. I think they're better, as you're saying, than the ones that might have been asked before,
*  in some regards, so that, you know, they're organized differently than what people have,
*  the way people ask questions before, and I think usefully. And that's really the kind of thing
*  that I meant in starting the book with, you know, emphasizing how we've really improved the
*  questions we're asking, even if a lot of the answers haven't sort of caught up in some ways.
*  I think they're always getting better answers are definitely always getting better. I think we've
*  seen huge strides in recent years, in fact, largely because of computation and building
*  big complicated models and all the kinds of things that you're talking about earlier on.
*  So yeah, I would say if the questions are better, I wouldn't say that they're definitive and right.
*  But they'll definitely keep me entertained for the next 30 years or more.
*  I mean, one of the things that you lay out is our trajectory, our as in the human species from
*  the earliest AI, the go fi AI days of symbolic architectures on to connectionism and dynamicism,
*  and you even mentioned in parentheses, basically a Bayesian approach as another sort of major
*  approach. And what you desire to do, and I commend you for this is have the best of all of those
*  worlds sort of and unify them essentially and say we can have a little bit of this and a little bit
*  of that. And really, but the purpose is, or the right way is to use the right things from these
*  different approaches to build an integrated whole system, which is what you've tried to do.
*  Well, which is what you've done. Yeah, try to do.
*  Which is what you're, which is what you're continuing to do. Okay, fair enough.
*  One of the things that it seems like you do is you take a function based approach and to build
*  this thing and constrain it by the biological details. So it's in that sense, it's kind of a
*  top down approach, right? Instead of, you know, like the mark room sort of build all the details
*  and turn it on and see what happens sort of thing. You really, you approach it from a function,
*  functional aspect, and then build it with all of the biological details as a constraint.
*  Do you think that we have the right defined functions even, you know, something like working
*  memory, for instance, or, you know, attention and all of those fun words that have some psychological
*  meaning, maybe, maybe they do, maybe they don't. Do we have that cognitive ontology correct?
*  No, I mean, there's almost pretty much no way that we're right at this moment, I think, but we're,
*  you know, moving in the right direction. It's better than it used to be. We have a lot of ways
*  of testing the system, right? And like those tests are an attempt to figure out those functions,
*  but really, at least they're operationalizing what we mean by those words, right? So by that,
*  I mean, you know, we can say something like working memory, and we can have some theoretical
*  idea what that means. But what we do know is we've got a bunch of experiments we've done on animals
*  and humans, which we call working memory experiments. And we think there's some core to them. But at
*  least we, we can build a model that passes those tests or performs on those tests in the same way
*  as the biological system, we have a reason to believe that we've got something right about the
*  function, right? So it doesn't mean that we have, you know, exactly the right individuation of what
*  the relevant, you know, functions are in the brain. Michael Anderson's done some really nice work on
*  commenting how complicated and weird this seems to be sometimes, like, you know, part of the brain
*  that's for controlling your fingers also seems relevant for counting. So, you know, that's sort
*  of not one that we might have hypothesized if we hadn't collected a whole bunch of data, tried to
*  operationalize thing, then notice this weird overlap between brain areas that light up in these
*  two cases. So yeah, I definitely don't think we're done. But I do think that we have enough
*  information such that they can constrain our models, right? Exactly the way that you're saying.
*  I guess the maybe slight change I'd make to your characterization of what my lab does is top down,
*  is that it's really bidirectional, right? So we have low level constraints and high level constraints.
*  So high level constraints are function, low level constraints are biological information. And we try
*  to make the two meet, right? We've got all kinds of tools and techniques to try to make the meets.
*  And then after making the meet, go and test them in both directions. So are we getting functions
*  in the way that we wanted to, you know, we can test the functions in ways that we didn't take into
*  account when we first built the model. And we do exactly the same thing on the biological side,
*  you know, what kind of spike rates come out of these in this new functional example. And if we
*  collect data from the animal, does it look the same? Right? So yeah, I see it not as unidirectional,
*  I suppose. And because in all instances, we're really looking at constraints, then we also don't
*  have to worry too much about getting the right, a parcellation of function or the right exact
*  understanding of, you know, how neurons work and exactly what currents are doing what and when and
*  where we don't, we just instead need to build a model that captures as much data within a single
*  model as we can. And then we have some claim to saying, I have this pretty unified characterization
*  of psychological and neural function. Yeah, I mean, it doesn't as long as the psychological data,
*  the behavioral data is reproduced, at some level, you don't need to worry about what you call it,
*  of course. Right. The other side of this coin that this so this is the first question, I have like,
*  I could have had a lot more questions for you. But this is Brad Imany. And he's a previous guest
*  on the show. Alright, so here's his question about 30 seconds. Hey, Chris, this is Brad Imany. I got
*  a question for you. So the neural engineering framework seems quite effective if you have a
*  known function for a brain region that you'd like to translate into a neural algorithm.
*  But I guess the question is, how do you see it when looking at less understood brain regions?
*  Are there any examples of this approach in inferring novel functions that may be testable
*  for brain regions where kind of an explicit formal function is not well understood?
*  Right. Yeah. So Brad is asking specifically about the neural engineering framework, which is
*  maybe just as a bit of context is essentially a technique for taking a function of some kind
*  and building a spiking neural model to implement that function. And we generally like people to
*  specify the function as a dynamical system, meaning that you write down some differential
*  equations. And then, you know, off you go, and you can build spiking neural network models where you
*  have different degrees of neural detail and so on. So it's very general, it doesn't tell you,
*  how the brain works. It's kind of just a hypothesis about how for some high level,
*  low dimensional dynamics, you might be able to build a spiking neural network version
*  that approximates that. All right. So with that in mind, I think Brad's question definitely comes
*  from the way that we first presented this work. So me being myself and Charlie Anderson, we take
*  examples where we can write down the differential equations, right? So if we want to write down a
*  memory, we're like x dot equals zero, so nothing changes over time because we're keeping it in
*  memory. And then we can use the methods and off you go. And I think that has caused there to be
*  a bit of confusion about what the applicability of the methods are. So people often ask, do you
*  have to have this like closed form description of the function? And the simple answer is no, right?
*  So the neural engineering framework can learn. So you can do optimization methods on functions where
*  you just have a bunch of data points, excuse me, in the same way that you do for deep learning,
*  right? Or any other kind of optimization method that people use for neural networks.
*  In more recent work, we do that a lot more than we did in the original book. And, you know,
*  in some ways, it's a little less sort of theoretically clean, but the same relationships
*  and techniques and everything apply regardless of whether you can write down a closed form version
*  of your function or not. So that being said, I think another reason that we've emphasized the
*  ability to specify the function and have that constrain your neural model is because it opens
*  up that possibility for lots of other techniques. Like, again, standard neural network learning,
*  people often don't or can't write, like, even if I could specify the function, I still have to
*  generate a big data set and then do my sort of back propagation training, which can take a really
*  long time. Whereas in the neural engineering framework, we can, you know, we have methods for
*  very, very quickly, so much faster than trying to train up a system, find a solution, which will
*  actually replicate the dynamics of the system that you're interested in. So I think of the NEF as a
*  way of bringing together either a data-driven approach for generating your model or as a
*  sort of closed form, write down the function approach, and you can do both. But because
*  the latter is unique, that's one that we've often talked most about.
*  So do you imagine being able to infer a novel or new function based on,
*  you know, approaching it through the NEF? I mean, just through building various functions in,
*  I mean, part of SPAWN is that you don't have to add a whole lot to these parts
*  to implement a new task, for instance, right? There's like a slow build and you don't have
*  to add that much. But, I mean, have you had the experience of seeing a novel function arise?
*  I'm rolling my eyes just using arise or emerge, you know, whatever.
*  Right. Have you seen that happen or thought about the possibility of,
*  you know, finding a new function in that manner? Yeah, this is another question to which the
*  answer is probably uninterestingly subtle. So every time we implement a function that we specified
*  with math, it doesn't actually run that function, right? It's always some other function,
*  and it's approximating what we specified in math. So, but, you know, there's uninteresting
*  versions of that where it's like, yes, I'm out by 0.2 for, you know, whatever, over the range of
*  interest. There are more interesting versions of that, right? Where, you know, we have done built,
*  like the working memory actually is a really nice example where we built a working memory,
*  we wrote down the differential equations, we implemented it in neurons, and we actually have
*  really interesting normalization effects that are coming from the neurons, not from our methods of
*  replicating the function. And those normalization effects show up in the behavioral data and our
*  model matches the behavioral data better because we implemented it in neurons. So if we just run,
*  actually, I think there's examples in the book, if we just run the math, which of course we can
*  simulate the math directly, and then we look at how the model performs, it doesn't do nearly
*  as similarly as humans as when we implemented in neurons using the techniques and then
*  test it with the same data that we test humans with. So that's an example where, like, I don't
*  know if you want to call it a new function, but definitely the way the function was implemented
*  became much more like what actually happens in biology, it seems, given the neural data
*  and the biological data. So does that count as a discovery of a new function? I mean, maybe.
*  The word function is so generic, right? It's-
*  Well, yeah, that's true. Uninterestingly subtle. Is that how you characterize that?
*  Well, so the first part was supposed to be uninterestingly subtle. This part is
*  maybe a little bit more interestingly subtle. I think, and then the extreme version of that in my
*  estimation is something like GPT-3, I'll keep coming back to this example where I've just got
*  gigabytes of language data and I train up a bunch of parameters, and then I can go back and I can
*  look at the model and say, hey, where's the grammar and where's the syntax and where's the
*  semantics and what is the organization of the concepts in the model and on and on and on.
*  And so, again, you can do that kind of thing in the NEF, but we tend to shy away from it because
*  it's just a different, I don't know, methodology in lots of ways. But Spahn has got lots of deep
*  learning in it. I'm super happy to use those techniques. I think they're great. And then it
*  comes down to questions of explainability or how well you understand something. If you want
*  to go and intervene in the system, how have you built it can matter and all that kind of stuff.
*  So it's kind of a spectrum. Often when I ask people, so I mostly have people from
*  the biological sciences on the podcast, but sometimes there's, well, basically anyone I have
*  on the show is at least interested in both sides of AI and what I call neuroscience, which
*  encompasses all the natural sciences having to do with intelligence. Everyone seems to make,
*  well, I've heard it over and over this distinction between the goals of AI and the goals of
*  neuroscience. So the goal of neuroscience, understand the brain and minds and natural
*  intelligence, whereas the goal of AI is to build it. And that's more of an engineering problem.
*  But I'd like to know how you see this. I mean, you gave the famous Richard Feynman quote earlier
*  and that you also gave in the book, but engineering can be used to understand something,
*  which is what I take you to be doing with Spahn. Do you see these as two very separate things,
*  engineering AI versus the goal of neuroscience and how you should go about doing it?
*  Isn't engineering one method to understand something?
*  Yeah, absolutely. I definitely think these are highly connected. And I think a lot of,
*  there is recent work in neuroscience, which has borne this out. So there are a lot of neuroscientists,
*  especially in the vision sciences, where we have a lot of information and our understanding is
*  getting more and more detailed and the models we build are thus getting bigger and bigger.
*  A lot of them are using deep learning now, right? Let me build a deep learning recurrent
*  convolutional neural network and train it up using the same data I train my monkeys with and
*  then see if the tuning curves are similar. And if I add constraints into my model,
*  which are ones I observe in neocortex, does it do better on certain kinds of problems? And you say,
*  you can find cases where it does. And our best models of the visual system are now deep learned
*  neural network models, right? So I think that blurring, if you want to call it that, between
*  techniques in neuroscience and techniques in AI is going to continue 100%. And it's definitely
*  happening in our hands. We've recently come up with some networks which have gone in the
*  other direction where we were looking at how brains represent time and came up with a new
*  understanding of that that matched really nicely onto these time cells that recorded from
*  rodent-type of campus. These are the LMUs, right? Exactly. Yeah. The Legendre memory unit.
*  Cool. That's really neat stuff. Yeah. And then we took it over to the AI side and we're like,
*  look, it beats all of your time series techniques. That seems interesting, right? I mean,
*  the convolutional neural networks are the same thing. They beat all of the machine vision up
*  until they came out and they're based exactly on looking at how the brain has organized the
*  visual cortex. So yeah, this kind of swap back and forth, I think is going to continue if anything,
*  it's going to happen more. And the answer of, they just have different goals. I mean, goals are
*  things that are had by people, right? And so different people in those different disciplines
*  tend to have goals of the kind that you specify, but it doesn't mean the methods aren't perfectly
*  useful in either domain and doesn't mean you can't use deep networks to understand the brain. And
*  it doesn't mean you can't use brain understanding to do better in neural networks research as well.
*  If I had to hazard a guess, and I will, my guess is that people interested in how natural intelligence
*  works and understanding natural intelligence are much more prone to accepting inspiration and ideas
*  from the AI world, quote unquote, then vice versa, then AI is even very interested in how the brain
*  might perform some similar operations. Do you agree with that? And if so, why are the AI folks
*  less interested in brains than brain folks are interested in AI, let's say?
*  Yeah, it's an interesting question. I honestly, like I don't really hold that view. So like,
*  I can think of examples of people in AI who absolutely think neuroscience is a waste of time.
*  Michael I. Jordan is a perfect example. I had a long conversation with him about this.
*  But there are people of equal or greater stature who think that neuroscience is fantastic and
*  really like it. So, Joshua Benjio cares a lot about human psychological development. And Jeff Hinton
*  has always connected his work to neuroscience. He hasn't put a lot of weight on it. He doesn't
*  necessarily think it's a critical hypothesis, but he definitely goes out of his way to say,
*  these are reasonable things. And this might be a good interpretation of what's going on in the brain.
*  But that's different than taking inspiration from actual brain mechanisms to really constrain
*  your model. And you can slap the biological plausibility model on anything or label on
*  anything really. I mean, some do that with more good faith than others, right? And I'm not calling
*  out the big AI names here. Yeah. So, like convolutional neural networks, again, is one of
*  my favorites. So, Yann LeCun, of course, did take inspiration from biology directly. I think, yeah,
*  so the second part of my answer to your question, where I was about to agree with you, which is that,
*  you know, if you talk to people in AI, they don't spend a lot of time reading a ton of neuroscience
*  and trying to extract every principle from neuroscience and put it in their model.
*  That's more of a theoretical neuroscience kind of thing to do. And I think the reason there is
*  because function will trump biological plausibility, right? So, if I care more about something,
*  if I can get it to work, then that's going to be more important to me. And by work, it has to do
*  better than what the other guy did recently on whatever the benchmark is I care about.
*  And adding constraints is going to make that harder, not easier, typically, right? So, it's
*  very, it's not that common where I see a constraint or inspiration, if you want to call it that,
*  from neuroscience that including it makes my model better. But when it does happen, it can happen in
*  spades, right? So, it's really a question of being able to distill the relevant things you learn from
*  neuroscience into something that is functionally useful. And that's the hard part. It goes back
*  to goals, though, again, I guess, because the big goal in AI is AGI, whatever general means in AGI,
*  right? But what you're saying is, and at least in the part that you agree with me,
*  an AI researcher just wants to get the damn thing to work. And it doesn't really matter how
*  specialized it is, or how it actually works. So, there's really little reason to take inspiration
*  from some organ, the only known organ that we know that has this, you know, general capability
*  to slow yourself down, essentially, to build the whole thing, or to build something bulky,
*  so bulky that it does lots of other things besides this one function you want it to do.
*  Yeah. Does that track with you?
*  Well, so I wouldn't say there's little reason to do it. I would say that it's really hard to pick
*  the right inspiration, right? So, I think at the end of your comment there, you were like,
*  hitting the nail on the head where it's hard to know which of the constraints you could take from
*  biology are the ones that matter for function, right? And that's really what they care about.
*  And there definitely are some, and sometimes they have been discovered. But there's a lot of other
*  constraints which don't seem that important for function. We don't care about things that are,
*  you know, dealing with blood vessels or ion channels or like, and biology cares a lot about
*  those things. And so, distinguishing the constraints is really the challenge, right? And since it's so
*  hard to do, you're not going to spend your time, just like if you take them all, you know, 1% or
*  less are going to be the ones that were worth your time. And that's just, you got other things to do
*  with your time. Spikes are not worth anyone's time, are they? That's what we call a segue.
*  So, I want to talk about applied brain research and neuromorphics here before we get into Spawn,
*  because you helped start Applied Brain Research. I don't actually know what your role is with the
*  company now. So, this is a company offshoot from research done in your lab, is that right?
*  Yep. Yeah. I'm one of the founders.
*  So, are you a scientific advisor now?
*  I work like sort of more closely than that. I'm technically the co-CEO of the company.
*  Okay. Because things are still spinning out of your lab into the company as well, right?
*  Yeah, that's right. Yeah.
*  So, you guys develop, well, lots of things. I'll tell you what, let me,
*  this is a good time to pause and play you question number two. This is from Steve Potter, who was the
*  first person on the podcast. Cool. Hello, Chris. This is Steve Potter from Georgia Tech. I'm a
*  huge fan of your approach to modeling the brain. I think it's the right way to go. My question is,
*  how soon do you think models like yours will be implemented in neuromorphic spiking hardware to
*  solve actual problems for the average person? For example, I've watched fuzzy logic fade into
*  the background in camera auto-focusing systems. I've seen backprop nets fade into the background
*  of postal zip code recognition. And recently, deep learning models have faded into the background in
*  many ways as big companies use them for complex text and image understanding.
*  Neuromorphic spiking hardware has been around since the 90s, yet we still can't find it in
*  any consumer devices. So, I'm wondering when you think that will happen?
*  I bet you have an answer to this.
*  I don't know how precise my when answer will be. Yeah, I will comment that just because we had
*  stuff in the 90s doesn't mean the time is up. Large scale deep neural networks have been around
*  a lot longer than that. But it is an excellent question. It's one that's hard to answer.
*  From the company perspective, of course, we would love it to be sooner rather than later.
*  I think what we've learned on the company side is that launching new hardware actually commercially
*  is definitely a huge challenge. Even large companies like IBM and Intel who have developed
*  neuromorphic chips have not released them commercially, which is unfortunate and challenging.
*  I still think that the fundamental advantages of event-based computing and spike-based computing
*  and neuromorphics will be realized probably in the next couple of years. Then the question of how
*  long that will take to get into some products, hopefully sooner rather than later from the
*  perspective of all these companies that are doing this kind of thing. But I would be surprised if in
*  the next five years there isn't some application area which is dominated by a neuromorphic approach.
*  My understanding was that you guys are building neuromorphic chips. If that's right,
*  I'm wondering if that is the dominant thing that the company is doing.
*  We are not building neuromorphic chips. We are working with companies that build neuromorphic
*  chips. There are companies like Grey Matter and there's a company that's going to start up based
*  on the Spinnaker 2 project and Intel. We built a bunch of software and demos and everything for the
*  Intel chip. It's something that we have done, but we're not doing our own hardware. We are looking
*  at finding financing now, but we're basically profitable and going on our merry way and
*  perfectly content to keep doing what we're doing. One of the reasons why spiking is attractive is
*  simply power consumption, that it's a lot lower power. There's the classic notion that you can
*  run our brain with as many watts, 20 watts as it takes to run a low-powered light bulb. And yet,
*  the Googles and deep learning companies of the world are burning up our planet, consuming so
*  much energy. And so implementing neuromorphic chips would reduce that energy by orders and orders of
*  magnitude. Is spiking itself, because I know you don't have to run on spiking, is the advantage
*  simply power consumption or are there computational advantages that we should really
*  take to heart with spiking as well? I think the short answer is unfortunately the un-glamorous
*  one, which is that spiking is all about energy reduction. But it's also not un-glamorous. It is
*  absolutely an overriding reason why a brain survives or not, is if you can get enough energy
*  to keep it going. It's also critical for environmental reasons, like you said.
*  And if you could take your cell phone and put your laptop in it and it would run for years because
*  you're using different kinds of hardware, you would care a lot. It sort of sounds un-glamorous
*  to say, yeah, it's just about power, but you got to get excited about power. Everything is about
*  power. That's like saying all of our beautiful cognitive functions are built on this surviving
*  meat machine. And so you have to get excited about the survival aspect, but that's not what's
*  exciting to us. We want to talk about all of the higher cognitive functions, right? So yeah, you
*  need both, right? So we've actually done calculations. Like if we took spawn and we run it on GPUs now
*  and we know how many watts they take and spawn is really small, so we can just multiply the number
*  of watts the spawn takes to get us to the size of a human brain. And if we do that, it's over a gigawatt.
*  So if we had, using current techniques and hardware, something which was the size of the brain,
*  even if we figured out all the algorithmic challenges, which of course is a big hope,
*  the amount of power we'd be using, this is like three power plants just for one model.
*  Right? It's ridiculous. So it really is something that is absolutely a critical,
*  critical constraint. And it's a big reason that we care a lot about low power in the company.
*  I should say the company is actually using a lot of low power techniques on commodity hardware.
*  So we have realized that there's this challenge for getting commercially available
*  neuromorphic chips out there, which are fundamentally spiking. But we also,
*  because we're algorithmic focused, we can adapt those algorithms to current digital hardware and
*  still beat set world records and the amount of power we're using to get certain amount of accuracy
*  or whatever the metric is you want. So yeah, so even though the sort of commercial future might be
*  less certain on the hardware side, I think on the algorithmic side, you will probably see
*  sort of neuromorphic in quotes, I guess, because at this point, it's purely algorithmic
*  techniques that make the next generation of AI a lot more power efficient.
*  Is this your first foray into like being a company man?
*  It is. Yep.
*  That must be enlightening. And we could probably talk for hours just about that.
*  I had Dalip George on the show who founded Vicarious.
*  Yeah, I know.
*  They build robot arms. Well, I'm not going to say that like you guys do because they're very
*  different. And we'll get into the embodied cognition spawn in just a moment. But he said in
*  the past year or so, he's spent like 80% of his time doing sales and product stuff. And I guess
*  like survival, like power consumption, you have to be excited. He's still excited about it because
*  it's just another thing to optimize to him. But part of his point was that you like as in the
*  company, it's not just like you make these beautiful research products and then move them
*  into the company, you have customers and you have to actually listen to what the customers need,
*  specification wise and all that. That must be again, the power consumption efficiency must be
*  the number one thing that you guys are hearing from customers.
*  Actually, it's not the number one thing. So people want to be very careful about sacrificing
*  accuracy for power. So you don't want to be dropping your power and then have the model
*  not perform that well. That's just kind of unacceptable. So you're always trying to optimize
*  both of those things at the same time. I mean, I'm lucky insofar as being co-CEO means that there's
*  another co-CEO who's on the business marketing and sales side. And so I definitely don't have
*  that kind of challenge. So I am definitely more focused on building, helping them design the
*  products and figuring out what the next steps are and using the technologies that are from the
*  lab and integrating them and all that kind of stuff.
*  So you're what? 90% lab, 10%? I mean, I know that they're so overlapping.
*  80-20.
*  80-20. Okay. The Pareto principle. You want to talk Spahn?
*  Sure thing.
*  This is the main thing that you probably talk about. It's in all your presentations,
*  these beautiful animations, by the way, that are really fun. So Spahn is the unified network
*  of what's called a semantic pointer architecture that we'll get into in a minute. But eight years
*  ago, 2012-ish, when you published the paper in Science and then published a book on it,
*  you had two and a half million neurons. Now it's at 6.6 million neurons with, like you said earlier,
*  20 billion, what we'll call synapses, connections. Whereas before it did eight tasks,
*  a measly eight tasks, now it does 12 tasks. And I know that part of what you're doing and you have
*  these great demo videos, you're adding an adaptation. So we talked about how the different
*  functions map onto different brain areas. And I'm not sure if you don't include a cerebellum yet in
*  the animations, but maybe that's in the near future with this adaptation that you're adding in.
*  And some of the other latest things that it can do is instruction following. And maybe you can
*  talk about these things more as we go along. But now this is Spahn 2.0, I suppose. Is that right?
*  That's what we call it.
*  Was there a 1.2 or was it just...
*  No.
*  Okay.
*  One and two.
*  I like that. Big steps.
*  Yeah.
*  Is the simple way to say it that the goal is to build a brain? I mean, just like the title of the
*  book?
*  Yeah, absolutely.
*  How has that goal...
*  That's my shortest answer.
*  Yeah, I love that answer. Has that goal changed at all? Because I mean, of course, there are a
*  billion sub goals with that overarching larger goal.
*  Yeah, it really hasn't changed over time. Yeah. I mean, yeah, we want to build a brain and the way
*  we built the first one... So let me specify how it hasn't changed. So the way we built the first one
*  is essentially had several students working on different projects focused on functions of
*  different brain parts and then took all of those and integrated them together in one big model.
*  And after doing that, of course, I have more students and they have different projects.
*  And when you write a PhD thesis, it has to be your own work. And so to some extent, you want to have
*  the disintegrated model. So when people working on the different component parts,
*  right before you put it all together. And so, yeah, so that happened. And then basically all
*  the parts that were in Spahn were improved and new ones were added and extended and so on.
*  And then it was reintegrated as it were a second time, right? Which is what Spahn 2.0. And now we're
*  back more in the phase of improving our understanding of all those parts, as well as adding additional
*  components. And that is really driven by the students, right? Like the things they care about
*  are the things that tend to get time spent on them. And if it's an overlap with something that's in
*  Spahn, it will result in an improvement. And if it's something that's not in Spahn, it will result
*  in a new feature or functionality or task, if you will. I mean, I have a hundred questions just
*  the development of the original development of the thing. I mean, so someone was working on a
*  robot arm and someone was working on an eye, a fixated eye, and someone's working on working
*  memory and then you brought these together? Sort of. Yeah, I mean, really someone was working on
*  the motor system. So then a robot arm, like it's not supposed to be a robot arm, it's supposed to
*  be a biological arm, but whatever, very similar principles. So somebody was working on motor
*  control. Somebody else was working on vision and visual classification. So that was why that uses
*  deep learning methods is because that seems like one of the better ways to generate those sorts of
*  models is lots of people have now come to do. And somebody else was working on working memory. So
*  trying to just build a model, which replicates a lot of the different kinds of working memory
*  experiments that you see, both in humans and other animals. And yeah, and then off you go.
*  Critically, a postdoc of mine, Terry Stewart, was very focused and remains focused on the basal ganglia
*  as something which coordinates behavior across all of these different cortical areas. And of course,
*  that's one of the really key pieces to being able to do the integration and build a model like Spawn.
*  So it's sort of bringing all of that together is what resulted in Spawn 1.
*  That control system, do I have this right? That was one at the heart of the general problem solver
*  back in early AI days. Is that right? Like, Newell and Simon?
*  I don't think so.
*  I thought they had a central control, like a production system.
*  Yeah. So you can, yeah. So they would never have called it a basal ganglia. They did have a
*  production system and Act-R also has a production system and SOAR has a production system. But the
*  question is sort of how do you do the rule matching, right? That they do in production system. I don't
*  even think of it as rule matching, to be honest. But yeah, you can, if you have a controller,
*  I guess, then you could think of that as similar to what the basal ganglia is doing in Spawn.
*  Okay. So at the heart of Spawn, the unified network is the SPAW, the semantic pointer
*  architecture. First of all, I'm just curious, like, was this the heart of all of the individual
*  components before they were began to be integrated? Has that always been there at the beginning? Or
*  is this something that you had to build in when you tried to unify everything?
*  Yeah, it was more of the latter. So we had lots of work going on in the lab. And I had done lots of
*  previous models of different component parts. And it might not be too surprising to hear that
*  I did systems design engineering, which is like a very kind of high level integrative engineering.
*  And then I did philosophy, which is even sort of more high level and theoretical. And I got to
*  wondering, how can we bring all of these low level bits and pieces together? There seems to be
*  obviously a lot of coherence because we're using the same mathematical techniques to build all
*  these models and so on. And so that's really what gave inspiration for trying to come up with a
*  method of unifying all the different things that we had done all the way from motor control and
*  vision to cognitive control, intelligence, language processing, all these sort of things.
*  And it was the attempt to tell a coherent story that resulted in the SPA.
*  Okay. So what is the semantic pointer hypothesis in a nutshell?
*  Right. So that's a good question. So I guess I should maybe say that the semantic pointer
*  architecture itself is an architecture insofar as it's here's a set of component parts and some
*  methods for integrating new parts. And one of the things that's important to those methods is
*  semantic pointers. This is essentially a form of communication. And so the semantic pointer
*  hypothesis basically says that high level functions in a biological system, so cognitive functions,
*  are made possible by processing semantic pointers. So they're basically a kind of representation.
*  And in fact, they're specifically neural representations that carry some semantic
*  content and they can be put together into representational structures. So the structure
*  being really important for capturing cognitive phenomena and they're basically what underlies
*  complex cognition. So then that's the hypothesis itself. So that semantic pointers are compressed
*  representations that are used to build structured representations for complex cognition. And then
*  a lot of the rest of the book can be seen as filling in the details. So what do you mean by
*  structured representations? How do you construct those? Why are they neural representations? And
*  what role do they play? And how can you manipulate them? And how do they get generated by a vision
*  system or a motor control system? I mean, it's one way to that I just kind of noted to myself,
*  one way to view the brain as you have it with a semantic pointer architecture is like it's a big
*  autoencoder, right? Where you go from like this, you lay it all out really nicely in the book, but
*  super high dimensional, let's say visual input. And then you have these semantic pointers that
*  compress that data, compress that information as they represent various parts of it and transform
*  those representations into these really lower dimensional or higher abstract, you could say,
*  compressed entities. Then when you but then when you need to move your arm, for instance, then you
*  have to what you what you call dereference, that's very engineering. I imagine a very engineering
*  computer science as a computer science term. Yeah. So you have to dereference and in other words,
*  go from like this really low dimensional, highly abstract compressed form and then back into the
*  high dimensional space to enact some act. And it's not just perceptual motor. I mean, these things
*  happen from various cognitive processes as well. But in that sense, it's like a it's like it
*  squashes the function and then reproduces kind of like an autoencoder, then it comes back to a larger
*  high dimensional space. Maybe that's the only way it's like an autoencoder. Yeah, so the definitely
*  the high low high thing definitely is like an autoencoder. I think the difference is that you're
*  not auto. The auto part isn't working out. Yeah, because you're not really reproducing the input.
*  Instead, you're mapping it to some other space like the motor space is just not the same as the
*  visual space. But that's right. Yeah, I think it's it is important to have those concepts of
*  going from higher dimensions to lower dimensions and manipulating things in the low dimensional
*  spaces can be much more efficient than trying to manipulate stuff in the high dimensional space.
*  And then as you're saying, sort of dereference back out potentially to another high dimensional
*  space, right, which is what you might need for control. In the book, you really detail and,
*  you know, obviously, we're not going to get into all the details on how representations occur,
*  you know, and how they're transformed. One of the key features of a semantic pointer,
*  and the semantic pointer architecture is that they are composable, right? So you have you can
*  combine the semantic pointers through mathematical operations and compose higher order functions.
*  Maybe you could elaborate on that. Sure. Yeah. So I think the key part here is that this is mostly
*  focused on representation. So the representations are the things that you're constructing with your
*  composition. And then we have processes for, you know, performing the compositions, unperforming
*  a composition. So doing things like dereferencing and so on, as well as manipulating those
*  representations. So I think it's always helpful to distinguish between the representations and the
*  processes acting on them, basically. And it's a little bit more difficult to say that the sort of
*  processes are composable. They're sort of more like, I'm not sure what the right word would be,
*  but they're organisable. Like you can sort of put them in different orders. So you can apply
*  operations in different orders and things like that in order to get different effects. But yeah,
*  that's right. So in for the cognitive semantic pointers, we identify some specific mathematical
*  operators in the book. We've actually come up with other operators than the ones in the book
*  since then that have some nice properties and so on. And definitely in the book, I focus on cognition.
*  And that's why I talk a lot about circular convolution. You know, this idea that we're
*  basically borrowed from Tony Plait, who came up with circular convolution as a good way to
*  generate structured vector spaces. So yeah, we've run with that, implemented it in neurons,
*  extended in various ways and so on. And it ends up being really powerful way of constructing
*  things that look like sentences or things that look like lists or things that look like trees,
*  all these kind of standard computer science types of data structures that seem really useful for
*  getting our computers to do things, and seem to map on to notions like grammar, and so on in
*  cognition, and being able to represent those now in spiking neurons and manipulate them with
*  the basal ganglia type of controller and all that kind of thing.
*  You think of representations as being in a high dimensional vector space as vectors in a vector
*  space. That's, that's sort of how you define representation, right, which is a connectionist
*  way. Sort of. I'm not sure exactly how subtle you want me to be, but.
*  Oh, man, we like subtle. We can go down the rabbit hole a little bit on the show,
*  you know, without dragging out too much. But I like how none of your answers are yes or,
*  you had that one yes answer. I have one.
*  Yeah, that was good. I was still trying to build a brain.
*  That's more than most. Yeah. Yeah. So I guess the subtle answer is that,
*  you know, I typically distinguish between like a neural level representation and state
*  representation. Right. And that's why I wasn't sure if I should say yes.
*  Please. Yeah. Yeah.
*  The vector space you were talking about is the state level representation,
*  not necessarily what's going on in neurons. And that's right. Those tend to be low dimensional.
*  Neural spaces tend to be very high dimensional, much higher even than whatever state space you're
*  representing and working in. And this relates actually back to the earlier questions about,
*  you know, starting with functions and relating them to spiking neurons. We can also start with
*  vector spaces, which are kind of like abstract standard vector spaces,
*  Hilbert space or something. And then we can think about how to map that into a different
*  vector space, which is like a bunch of neurons that are spiking and can be, you know, have whatever
*  weird kinds of properties. But you can do a lot of thinking in the original vector space, the state
*  spaces, I like to call it, and, you know, specify hypotheses there and think about, you know, what
*  the right processes are to manipulate these representations, think about transformations
*  there, think about linearity, non-linearity happening in that space. And then, you know,
*  conveniently the NEF gives us these methods to map all of that into spiking neurons and this much
*  sort of more complicated in some regards space of neural activity.
*  Okay, so we're going to pause here then because, like I said, I had Randy O'Reilly on the show.
*  And we talked about his cognitive architecture, Libra, and I told him that you're going to be
*  coming on the show. And so he, I'm going to play you a three and a half minute clip here,
*  which with a question at the end to give context to what he said. And then we'll have one more
*  question from him after and then we can use that as jumping off points to talk about whatever we
*  need to. Sounds good. And I wanted you to kind of compare Libra and Spawn. Oh, yeah, for sure.
*  A lot of the, there's a lot of commonality and therefore, you know, a lot of opportunity to draw
*  kind of key contrasts. And, you know, Spawn, I think, you know, does have that advantage of being
*  something where you have a lot of control over what the system does. And a lot of what they've
*  done with their architecture is, is kind of configure really building on work that Tony
*  Plate did in the nineties, these holographic reduced representations to solve the binding
*  problem, to do kind of, you know, fairly complex, elaborate forms of cognitive information processing.
*  And so I think they're able to get a lot of functionality out of the system because
*  essentially they have a lot of control over what's happening. Whereas in Libra, we're more at the
*  mercy of like, what can we train the system to do? And what kind of dynamics are going to emerge
*  as we try to train these systems? And so we have a lot less control. And so I think we can't, you
*  know, they have like models of doing like Raven's progressive matrices and lots of complicated kinds
*  of tasks. On the other hand, those models also provide then kind of perhaps less insight into
*  how the brain really does it, because it's kind of reflecting more of an information processing
*  kind of prior assumption about how it could work. And one question I would ask about these models is
*  how much have you learned in making that model relative to what you kind of came in with it?
*  Like, how much did the model teach you in making the model? Because I feel like once you
*  have a framework where you can basically get the model to do what you want it to do,
*  that's nice, but it also means that the model has less opportunity to teach you something
*  that you didn't otherwise, you know, kind of know about the brain itself or about the functioning
*  of the brain, about how the how that cognition actually might work in the brain. You know,
*  I don't feel like the model of Raven's progressive matrices, for example, that they have gave me a
*  lot of insight into how like the brain might actually solve that problem. Likewise, with other
*  models that we've seen in AI, where they are now also taking on these Raven's progressive matrices
*  tasks, which are kind of the one of the classic tests of general intelligence. And that's why
*  they're very attractive to model with these kind of AI models. But the whole thing about it is that
*  it's a test of your on the fly ability to solve these kind of novel problems. And yet they're
*  training these models or hand configuring these models kind of in a special purpose way to solve
*  that task. And once you do that, it sort of negates the entire point of the of the task,
*  which is that it's supposed to be a transfer task, a novel task that you've never done before.
*  And so it's like, yeah, I can get a system to solve that task. That's not the problem.
*  The problem is, how do I get a system that's never done something like that before
*  to figure out how to solve the task on the fly on its own? You know, and that's the real problem.
*  And again, I think that's where, you know, having kind of introspective access to, okay, well,
*  gee, how am I going to solve this test? Well, I know there's these patterns, you know, just
*  that whole process we would introspectively go through in thinking about how you would
*  tackle a new task. That kind of flexibility, I think, is what is what's missing.
*  Okay, so he was kind of going on about his because we had talked about metacognition earlier and how
*  he thinks that's important. So what say you, Chris Elias Smith, to this charge? I'm just kidding.
*  Sorry, that was kind of long, but I thought for context.
*  No, no, not at all. It was actually good to get as much context as he provided to the question,
*  because I've had many conversations with Randy and they're often on many different topics.
*  Yeah, yeah.
*  But yeah, I think he's, you know, continuing to somewhat misunderstand how the model works in so
*  far as suggesting that whatever we want it to do, it will do regardless of it being brain like or
*  not brain like. I think like, yeah, I'm struggling, I guess, to know if I should talk specifically
*  about the Raven's progressive matrices or about spawn more generally. Let me start with the form
*  or the latter. So yeah, so, you know, he made the comment that spawn uses these circular
*  convolutions that we were talking about before that Tony plate suggested as a nice way of
*  generating structured vector spaces, and that a lot of the behavior of spawn is because of
*  that operator. That's actually not true. Like the that circular convolution operator is a very small
*  part of the model in sort of a computational respect. So it has nothing to do with the motor
*  system or the vision system or the basal ganglia. It's used in some of the models. So it's used in
*  the working memory model for constructing lists. And it's used in the, yeah, the Raven's progressive
*  matrix like stuff that the model does. But yeah, there's there's like so much more going on than
*  that, that you wouldn't be able to build a model like spawn if that was the only operator or the
*  only compression thing that you could do for sure. So that's the thing number one, maybe not that
*  significant in a way, like we do use it, we just don't, it's not like the whole model is it sort of
*  sounded like in some regards. And I think critically, I guess that, you know, the important
*  thing that does follow from that is that I think Randy seems to believe that because we can construct
*  representations using operators like that, that look like computer science representations of it,
*  like as I was just discussing, which is, you know, I think a strength of that operator,
*  it doesn't mean that we are writing down algorithms like computer science algorithms to
*  manipulate symbol like structures in a way that most people in AI would if they were trying to
*  solve Raven's progressive matrices. In fact, this is one of the big sort of emphases for us in
*  presenting that model was to say, hey, look, if you just like Randy was saying, actually, you know,
*  Raven's progressive matrices are supposed to be about coming to a problem that you haven't seen
*  before and solving it, not knowing what the right relationships are between all of these elements in
*  the matrix, right? You have to figure that out from square one. And our proposal about how that
*  worked was unique precisely because it didn't build in the rules that you needed to solve the
*  problem. So in essence, the thing that Randy was asking for is in our model, like that's one of
*  the special properties of that model. So do you think you think he's hung up on the approach,
*  just using computer science methods type approach to just because of the functions?
*  I think he's hung up on the fact that we call it the neural engineering framework and that engineers
*  build things to have specific functions, typically regardless of low level constraints. But,
*  you know, if you actually look at sort of how biologically plausible spawn is compared to Libra,
*  I think is a fairly strong argument to say that spawn is far more biologically plausible. So,
*  you know, we have everything in spiking neurons, we use all the time constants that you find in the
*  real synaptic connections. In the majority of Libra models, you know, they put in a max function,
*  which like, no neurons compute. And they make assumptions about it happening instantaneously,
*  which again, destroys the dynamics of the model being from being realistic. So, like, yeah, in
*  some ways, you know, I think, like that kind of debate is not irrelevant from the biological
*  realism perspective. But here, he's more concerned with the high level techniques, right, about
*  what assumptions do you or don't you build into the model in order to get it to work. And in the
*  case of our Raven's progressive matrices model, the model literally learns for each matrix,
*  how to do the inference, like it is learning exactly like he's asking. The difference is,
*  it's not changing the weights. And he, most of their models change weights. So, the learning
*  that happens in our Raven's progressive matrix model, as many others happens in the activities,
*  but in the brain learning happens in the activities, that's what working memory is,
*  and so on as well. So, yeah, I don't know, it's a, it's a bit of a criticism, which I think
*  misses the mark. In fact, it's kind of like one of the strengths of the model is precisely that it
*  learns and infers these new patterns that it's never seen before. Part of what you were, I have
*  one more question by him in just a second, part of what you were saying about spawn being
*  bi-directional, I think is one of its greatest strengths as well in that, I mean, it's not like
*  you're not trying to produce psychological functions, but this goes back to the conversation
*  earlier about levels of scale and descriptions of different levels. And you're at pains to remind
*  the reader throughout the book and other works of yours that, yeah, you do want psychological
*  function. That's the behavioral output is what it's all about eventually, but you also want the
*  implementation details to reflect how brains might be doing it. So, yeah. All right. So I'm
*  going to play one more question by him and, and then we'll move on. Sounds good.
*  The other question to ask Chris is, you know, do they clearly explain that the spiking
*  is added on after, like you program the model using dynamic equations, continuous dynamic partial
*  differential equations, and then they kind of add on the spiking afterwards. And when I learned that,
*  you know, I was kind of like, cause he, you know, in his talks, he makes a big deal about how it's
*  a spiking network, but it's kind of first a not spiking network, and then it becomes a spiking
*  network kind of after the fact. And so to me, that sort of was like, okay, well, how much is
*  really different between the spiking network and the original kind of, you know, differential
*  equation version of the model. So anyway, you could ask him that. All right. Shots fired. I like it.
*  So I should, we had also been talking, I'm sure you know this because you talk with Randy,
*  he's been, I don't know struggle is the right word, but he's been thinking about whether he
*  needs to add spiking to his connectionist networks in Libra. And so I either talked about that before
*  or after this, this comment. So you make a big deal. Yes, I do because it's true. It's all spiking.
*  I'm actually not quite sure what he means by added after. I think also interestingly, we've
*  already touched on this. You asked me a question earlier about like, you know, do you ever learn
*  anything or do you discover new functions? And my answer was basically, yeah, you put it into
*  spikes that you aren't actually computing the function you wrote down to start with. So, you
*  know, being in spikes is important and it's definitely not the case that you preserve your
*  original hypothesis about what the dynamics might be once you write down the real, or simulate the
*  real spiking neural system, right? So the dynamical system you simulate is not the one that you wrote
*  the equations down for. And it's the one you simulate that matters. So it quote unquote,
*  really is spiking. We never simulate the non-spiking system in the final spawn model,
*  right? It's really all spiking neurons. They're just neurons. They're just connected. Each neuron
*  has its own differential equation. That's all we simulate. None of the high level stuff plays any
*  role in the simulation at all. So I'm not quite sure. I imagine he's like equating that high level
*  state representation stuff we were talking about with the model, but ultimately it's not, right? So
*  it really is the thing that we simulate is the spiking neurons and the spiking. There's nothing,
*  no adding on spikes after. I'm not quite sure what that means to be honest.
*  Yeah. Well, thank you, Randy, for those questions. But now I'll ask you, Chris, and I already know
*  that I'm going to get a ton of emails about having you guys on together at some point. So
*  we'll see about that. But this is in some ways the pre-recorded questions are nicer because
*  no one can be interrupted, for instance. Fair enough. That's right. But how do you think of
*  spawn with respect to Libra? I mean, we've talked about this already a little bit, but I asked Randy
*  about spawn and I'll ask you about Libra, I suppose. Yeah, I struggle with this question because Libra
*  is not a model, right? So Libra is a learning method, kind of like a reinforcement learning
*  technique. And so there is no Libra model. Expand is one specific model. You can download it and run
*  it on your computer at home if you want. Right. Well, you can download Libra as well. And I
*  haven't done that either, but it's not a model. You can run simulations. You can simulate things
*  though, right? So maybe it depends on what you think of as a model. So it's, yeah, it's not a
*  model. It's a method, right? So like, you would want to compare Libra to the NEF, right? The
*  neural engineering framework. That's a technique for constructing and simulating models. Libra is
*  a technique for constructing and simulating models. Like they have their, you know, PDP plus plus,
*  or emergent now, I guess it's called, right? And so emergent is like mango. Libra is like the NEF
*  and spawn, like there is no spawn. And that I know, like they built a lot of really cool, big scale
*  models using Libra and lots of other techniques, but I don't know which of those to compare spawn
*  to. Right. Well, yeah. So I know he has plans to embody Libra, which would, that would be a step
*  toward a more spawn like, uh, that would be a model then, correct? Yeah. If he has a specific
*  instance in which, you know, here's the simulation and we're using Libra to learn stuff in that
*  particular simulation, I'm going to call, give that simulation a name. So whatever, Lisa, uh,
*  then, you know, that would be the thing that you would compare to spawn. Okay. Gotcha. Well,
*  okay. Maybe you, and you don't have to say anything more about this if you don't want to,
*  but maybe you can compare it to, to the neural engineering framework. Yeah. So, um, actually,
*  I think with some tweaks, which I'll try to give my comparison to, uh, other learning techniques
*  that I made before is not inappropriate here, right? Where, uh, yeah, for, you know, most kinds
*  of learning back prop and RL and all that kind of stuff that people use, typically they, um, have
*  a whole ton of data. You try to put the data through the model, get the model to update all
*  the connection weights, and then get it to perform the function that is somehow represented in the
*  data. Uh, and as I mentioned, we can do that in the NEF, but we also have these other methods where
*  we can be a little bit more explicit about what functions we'd like to compute. Um, and we can do
*  things much more efficiently, basically build models that we can get to work more easily and
*  that we can solve a lot faster on computers and stuff. Um, and that really lets us build models
*  of the scale of spawn that people, you know, typically cannot do. Like the only place you see
*  that happening is in things like language again, right? Where you've got so much data on that one
*  topic, IE, you know, speaking language and generating language that then you can finally
*  train a model of the scale that you need. Whereas for us, you know, you would never back prop
*  a spawn model. Like you couldn't build it originally from back prop. We can actually
*  back prop through spawn now. Like we can, you know, we can optimize, we can put Libra in spawn. You
*  can, you know, we've got all kinds of learning rules in spawn. We can do more of that. Uh, you
*  know, good. And it's a great way to understand learning. And I really think that the role for
*  techniques like Libra and, you know, we have like the PESPR rule and other stuff in spawn,
*  that is to explain online learning. Like once we have a system and it's functioning and we know
*  the system continues to learn and adapt and change itself. Um, and like our adaptive control
*  techniques, you know, that they do that, but that's a slightly different, uh, you know, part of the
*  answer to the question, how does the brain work, but slightly different role than constructing
*  the model to start with and constructing the model to start with, you know, if you really
*  want to understand development, then you might need a bunch of developmental processes and
*  everything. But we were always very explicit that we're writing down our starting big complicated
*  model as a hypothesis for where we think it's an approximation of what an adult is, has a tiny
*  little part of an adult's brain, right? It looks like spawn. And then from there, because we are,
*  now we have a big complicated, big complicated in the context of our models, not in the context of
*  the brain, a big complicated version, we can then introduce things like online learning and say,
*  you know, does that online learning rule keep things stable and can it add new functions
*  in useful ways and on and on and on. And we definitely have lots of research programs looking
*  at how do you learn a new cognitive function in spawn as opposed to specify one. And that this
*  is an important question for sure. Um, and I think that one that we care about, um, and one that I
*  think, uh, sort of people have in my humble estimation, sort of, uh, limited their options
*  for building these big models by starting with only, you know, kind of carte blanche learning
*  techniques, the tabula rasa network type. Exactly. And we know the brain doesn't do that either.
*  Right. So yeah, one of the, it's interesting because, um, on the one hand spawn and we haven't
*  even explicitly stated this is super impressive because, uh, it actually takes perceptual input
*  and a task, you know, and, uh, you know, you show like a number, which tells this, tells spawn what
*  task it's about to perform. You say, go, you give it, then you give it visual inputs and it has to
*  process that has to know which task it's being, um, input and it has to process and, and then output
*  via an arm, uh, output and answer whether that's drawing a, a number or letter and so on. On the
*  other hand, when you look at it, it looks so crude because it is this embodied system, but it's just
*  one I fixed and it's one, uh, robot arm with two degrees of freedoms to, yeah, two joints. Yeah.
*  And, and so in that sense, it's three joints, three joints. I'm sorry. I apologize. Six degrees
*  of freedom because there's six muscles. No, it's pathetic. I agree with everything you're saying.
*  Pathetic is the incorrect word, but it's just kind of humorous that like something so impressive
*  can look so crude in that, in that particular manner. And I'm wondering like what,
*  what the biggest, um, when you're adding in new functions, cause it's this big complex system now.
*  And when you're adding in a new function, what is typically the biggest hurdle or the most friction
*  in adding in, you know, some new function? It's a good question. So sometimes there's no,
*  almost no friction. I think like, you know, the ones we like to talk about is when we say things
*  like, ah, we added 200 neurons and we got an entire other task out of the thing, um, because
*  you're just leveraging all of the, you know, computation that can already do. But yeah, I mean,
*  so one of the purposes of specifying an architecture and a communication protocol and all
*  those, you know, fix semantic pointers and so on is because it actually makes adding new functions
*  reasonably painless most of the time, typically the thing that gets, so you can like hook things
*  up to one another easily and you have consistent ways of talking about what is being transferred
*  from one system to the other, right? That's the representational protocol part. The thing that
*  typically becomes hard is when you try to coordinate the whole system, right? So this is what the
*  Bazel Ganglia is doing. And it is definitely sensitive to, um, you know, making sure that when,
*  you know, one part of the model kind of wants attention or needs to like, wants to do processing
*  and take over the output, it's the right time for it to be doing that. And it's not trying to like,
*  interrupt some other thing that should be happening. And, you know, because we've identified
*  that as a challenge, you know, there are techniques for learning that and they're called reinforcement
*  learning. And that's exactly why we're looking at these techniques to basically auto tune the
*  model where, you know, it can learn through trial and error what the right order of operations is.
*  And when, you know, something needs to be brought online in order to solve a task and all that kind
*  of stuff. So, um, yeah, I think the, the fairest answer is that, yeah, the biggest challenge in
*  putting new parts in is making them work with the other parts in a coherent manner. It's not
*  typically the, you know, we can have like very complicated information processing going on in
*  the components. Um, and we can figure out ways of doing that, but then, you know, making those
*  outputs and inputs be coordinated with all the other outputs and inputs in the rest of the system.
*  That's where challenges rise. So is that, would you say, cause I was going to ask if, if the demand
*  that you put on the system for flexibility, uh, as part of that's something that you have to,
*  has to always be present and has to always remain flexible. And I was wondering if that would be my
*  guess, if that is what slowed progress the most is just having to always worry about how all the
*  systems interact together. Yeah, I think that's right. I mean, I think it's also why, you know,
*  things like, I don't know why I've talked about GPT-3 so much, but it's such an impressive model.
*  A lot of people's minds. Yeah. Yeah. It's quite something. Um, you know, one reason it doesn't
*  have to really worry about that. It doesn't explicitly worry about that. There's obviously
*  some pretty impressive things going on in the model as far as control and stuff goes on,
*  but yeah, you know, it, um, can just get more and more and more data and build a bigger and
*  bigger statistical model. Uh, and for us, that's right. We have to really worry about dynamics and
*  how things change over time and interactions between components and all these sorts of things.
*  I think it's worth it though. Like I think flexibility really, you know, when, if we think AI
*  interested in AGI, the G is about flexibility, right? And if we look at biological systems,
*  even something as simple as a cat, you know, which of course isn't simple, um, the flexibility and
*  the cat's, uh, you know, behavior is absolutely astounding, right? And that's exactly the kind
*  of thing we're missing from our models and from our understanding of the brain. So as much as it
*  is a challenge, it's also not the kind of thing I'm likely to want to get rid of anytime soon.
*  Why did you start with a human brain? Why not a cat? Why not something's a lower animal or whatever?
*  The reason really is actually coming back to, uh, trying to unify across all of those three
*  approaches that we were talking about before, or four approaches. Uh, so, you know,
*  symbolicism, dynamism, connectionism, and a Bayesian approach. So to convince people that
*  we were definitely doing something symbolic, right? So, you know, the challenge with symbolicism is
*  it's a good description of human cognition. It's not clear. It's a good description of anything else,
*  but it is describing important things about human cognition. So for us to convincingly
*  argue that, yeah, we're, you know, we're in the same camp, like we're doing some of the same stuff
*  that they're doing with those symbols. We really have to get something that looks like human
*  cognition off the ground. And so calling it a human brain is, is the reason we did that. And,
*  you know, picking things like Raven's progressive matrices and counting and all these very human
*  like, or human only kinds of cognitive phenomena seem, seem the right way to go for that.
*  You know, there's more of X Moravex paradox where in AI, where it's the, uh, the higher level,
*  logical, um, cognitive stuff is actually the easier stuff, uh, you know, on that symbolic level to,
*  to build, whereas manipulating a, uh, an arm to write a letter is the harder stuff in general.
*  So that's, that's what I'm wondering because that the higher level stuff is built presumably
*  on evolutionarily older functions and, and systems. So, um, it's, so that's why I was curious whether
*  cause you know, it's like you, you, uh, went for the gold from the start, but
*  we've got the bronze and silver in there too. Right. So we do have a visual system. We do have
*  a motor system and they, but they are definitely simplified and nowhere near as sophisticated,
*  but it's, that's true across the model, right? It's always simplified. And I think the point
*  for us is to try to say that, uh, yeah, you know, you need to do it all in some ways, right? You need
*  ultimately, that's what we're trying to explain is not sort of how a cat works. We're trying to
*  understand how a human works and go from there. What was the worst day in lab? What's the biggest
*  mistake that you've made with, with spawn or, or a, a mistake. Um, I don't think above most,
*  most of our dead ends, shall we call them as mistakes per se. Uh, they also don't tend to
*  stick around for very long, maybe unsurprisingly. Um, you know, I think one of the exciting things
*  about working in my lab and with all of the students I've had so many fantastic students is
*  that like days don't go by for very long where we're stuck. There's just so many other things
*  to try and really smart students coming up with all kinds of new, good ideas. And, you know,
*  it tends to be a very interdisciplinary place. So, you know, drawing from all kinds of different
*  approaches is something that people, um, sort of get used to. And that makes the mistakes fade into
*  the mist. I don't know. I don't know what to pick to be honest in, uh, trying to answer that
*  question. Yeah. You never tried to plug in some function and then just, it just broke everything.
*  No, that has not happened. I do not think one of the things that you're like, there's, there's
*  nothing that's that like, yeah, it's not like we tried to do emotion. It didn't work. And so we
*  left it out or we tried to add some legs and it didn't work. So we left them out. Yeah. No examples
*  like that. I tried to move the eye. The, um, yeah. In the book, I'm going to read you a quote from
*  your book, uh, quote, I will be shocked if major elements of the SPA turn out to be right end quote.
*  So it's okay. It's a very humbling, humble thing to say. What is your biggest worry about whether
*  spawn the overarching approach is, is the right path forward, or are you just super confident
*  that it is the right path? Uh, not sure what the it is. So the thing I would be confident in,
*  I suppose, is the more like the philosophical level, like, you know, the kinds of questions
*  that we're asking, um, the general mathematical approaches that we're taking. So using
*  vector spaces and dynamics and, uh, you know, embedding those into spiking neurons, like I would,
*  I, I, you know, I'm reasonably confident that that kind of those kinds of techniques, uh, going from
*  high dimensions to low dimensions, all those sorts of things are probably going to stick around
*  when we have a better brain model. Um, this, uh, like I said in the book, actually, I would be
*  surprised if any of it stuck around by the end, uh, where the it then is referring to things like
*  the specific vision model we've got or the specific motor control system, or, um, you know,
*  there might be principles in there which survive, but yeah, almost for sure there's going to be a
*  lot of changes and updates in our understandings as they exist now. I think the one I would be
*  least confident in, so that I guess this would only mean that it would maybe fail first,
*  is that, uh, the basal ganglia right now, we put way too much, uh, sort of weight on it for
*  taking care of the coordination and control. And I think there's lots of other processes that are
*  not well represented in the model for doing that. Yeah. So, you know, there's always, for, I think
*  most people, there's always a piece of data or two that really bother you and you have no idea how
*  they're consistent with your model. And for me, those show up in the basal ganglia. So there are,
*  unless the data is wrong, which is always a possibility, but I think there's pretty good
*  evidence that if you do a bilateral paladectomy, meaning that you like take out the outputs of the
*  basal ganglia, if you did that to spawn it breaks. It pretty much doesn't do anything. It's not going
*  to move its arm. Nothing interesting will happen. If you do that to a human, you know, they can still
*  function. They still do stuff. They seem to get a little bit more, uh, sort of driven by reflex
*  maybe and less flexible. Right. And so the fact that the basal ganglia is playing an important
*  role for flexibility seems to be right, but the fact that it plays a complete dominating role for
*  flexibility and basically performance of anything interesting, I think is probably putting too much
*  weight on that as a function that's sort of solely owned by the basal ganglia. I mean,
*  do you think redundancy is, uh, less appreciated than maybe it should be with respect to different
*  parts of the brain being able to perform different functions and, you know, overlapping in a
*  redundant manner in that same sort of vein? Yeah. I don't, I don't know if it's under appreciated.
*  I think lots of people, if you said that to anyone, they'd be like, yes, in fact, this is one of the
*  things that brains do amazingly that, uh, lots of our models aren't so great at. Um, so that kind of
*  robustness is definitely something I think people appreciate, but it's also, as I think your question
*  is highlighting something that is probably not well reflected in a lot of models, right? Especially
*  as they get bigger and more cognitive of the kind that we've been talking about. It's not the way
*  you'd think like, oh, I need to build in the same function in all 30 different parts of my model.
*  They all need to have like a little bit of the same function. Or yeah. And it's more also like,
*  when does one take over and the other doesn't? And it comes back to that coordination problem,
*  like as hard as the coordination problem is even with our simplified view, if you then start having
*  like little bits and pieces of the coordination happening in all these components and all that,
*  it gets even worse. And I, yeah, I'm hopeful that, you know, figuring out techniques for
*  self-tuning, basically letting the model have control over those parameters in the model is
*  going to be a pretty reasonable way forward. So you think that the, it'll settle into,
*  so you got spikes, right? Which reduce the energy. The brain's already like a low power
*  consumptive device, device. Um, I mean, a large part of that must be dedicated to control
*  because it is, you know, such a mess, so complicated. So do you think that, or do you think that it has
*  sort of settled into a low powered, um, where it's not difficult for the brain, where it doesn't
*  have to spend a lot of energy on control? No, I think it spends a ton of energy on control.
*  I think what it doesn't spend a ton of energy on is, uh, probably the tuning of the control. Like
*  that is, that is energy that you only spend when you need to. So if you find that you've got errors
*  in your control, something bad is happening in the world, right? That's when you start
*  giving a bunch of extra resources to try and fix that problem and, you know, retune things and all
*  that kind of stuff. But I think that, yeah, as far as the actual energy budget to control,
*  it's probably a lot, like, you know, definitely cerebellum is doing a bunch of that. Motor
*  control is doing a bunch of that. Basal anglia is doing a bunch of that. Vision system has like
*  attention, right? As a form of control through the vision system. Yeah, there's, there are layers
*  and layers and layers of control in the brain. So I wouldn't be surprised if most of what it does
*  in one way or another, we could relate back to control. Um, but yeah, it's the, the fixing of
*  the control or the retuning of it, the kinds of things we were talking about, um, you know,
*  when there's damage, right? And like, why doesn't it fall apart when I damage it? That's going to
*  be because of these other, um, sources of flexibility. So you're at 6.6 million. Um,
*  once you get to 86 billion, not that you, you know, I think it's around the corner, which is
*  half the interest from the corner. Once you get there, like, why not keep going? What, what,
*  why would you not build just a bigger, how to build a bigger brain? Why not? Sure. You could do
*  that. I think it depends on your goals at this point too. You know, maybe this brings us back
*  to the neurobiology AI kind of distinction where if we want to understand the human brain and help
*  medically, you know, understand what, how interventions work in humans and what it means
*  to apply a drug, then our constraint is going to be to replicate the system. We're trying to help
*  understand and that we want to help people fix and all those kinds of things. Um, and, uh, if
*  that's where interest stuff, that's where they stop. And if we're interested in building something
*  that's going to make better decisions or be faster, or, you know, all these sort of super
*  human intelligence kinds of, uh, functions we can imagine, then yeah, there's no reason that you
*  wouldn't be able to continue to build on the same principles and, and head in that direction. If you
*  want to me, there's this, um, well, I'm going to say fascinating, but extremely unlikely event,
*  but interesting nonetheless to think about that as you're putting these things together, that
*  you could develop novel functions by increasing some parameter or hooking to other adding some
*  other quote unquote brain area, and then having to interact with other brain areas. And all of a
*  sudden you see like a different, uh, sort of function. And we talked about the degrees of
*  what a new or novel function would be a question of a different degree or a different kind and
*  where that, where that balance is. Um, anyway, it's probably unlikely, but has building spawn,
*  has this undertaking changed the way that you yourself have thought about brains or, and,
*  or minds? Um, I tend not to distinguish brains and minds too much. Um, has it made me think
*  differently about, I mean, definitely, I think it's been kind of a slow process. Like we have,
*  especially in the second version, we've come up with new operators and new kinds of networks,
*  like the LMU and new understandings of, you know, representations that are likely in the brain,
*  which I definitely was not thinking about when we started the whole process. Uh, some of this stuff
*  hasn't made it into spine yet, frankly, some of the work in the lab that I think is kind of,
*  of that variety where it makes me rethink about the way functions are characterized in the original
*  version of spawn and so on, but it's very evolutionary. Um, so, uh, yeah, I can, I can
*  sort of point to those things. Uh, if I'm not sure if the construction of spawn itself had that kind
*  of impact. Uh, if anything, the biggest impact of that is just like, yeah, you can make it work.
*  Right. So I don't know how many people would have believed before we built it and it worked.
*  That we could build it and make it work. I mean, I remember sitting on the plane designing it and,
*  but when I was done, I was like, don't see why this wouldn't work. But then, you know,
*  the actual building, of course, was tons of effort. And, uh, yeah, Sean Chu is the guy who really
*  got it to work in the way I had hoped it would. Um, but it, yeah, you know, it did. Uh, so,
*  and maybe relieved is a better description than surprised, but yeah.
*  What's the most satisfying part of your day when you're working on something? Is it being,
*  for me, it would probably be the, using the tools to, uh, you know, build the, the actual
*  robotic arms and that sort of thing. I'm sure it's there. There are, um, fun things about all the
*  different aspects of your job. What gives you the most kicks?
*  That's a really hard one. Uh, and also varies from day to day. And it also varies depending
*  on my context. If I've been doing a lot of administration, which unfortunately is a lot
*  of my days these days, then any ability to get into the details of research gives me kicks,
*  as it were. Um, I have to say that mathematical elegance is something that really floats my boat,
*  as it were, especially as it applies to a real physical system. So, you know, not pure math in
*  that sense, but it's more like engineering math. Maybe that's unsurprising. Applied math, I guess.
*  Yeah. You see some like beautiful, simple description, which gives you a really deep
*  understanding. And then you can build something which follow those principles and you have a new
*  thing. Like, you know, this is a new way of putting physical substances together, or even if it's in
*  simulation, you know, you can move it into hardware and stuff like that. Um, to realize a behavior,
*  which yeah, you would not have come up with if you didn't have that sort of underlying mathematical
*  insight. That's definitely exciting, but it's also super exciting to just, you know, build a really
*  complicated engineering system and have it do what you were hoping it would. Uh, you know, if it's
*  flying a drone or moving a robot arm or building a model like Spawn, like these things are all also
*  very, uh, inspiring and make it easy to keep going back for more. Yeah. Yeah. It's, it's
*  super impressive. How would you, if you were going to start over, because one of the interesting
*  things about you and a strength is how varied and diverse your background is, your intellectual
*  background, computer science, engineering, philosophy, neuroscience, and how would you,
*  if you were going to start now, throw it all away, how would you begin again? Would you start the
*  company from day one? Yeah. Uh, so is, so what kind of starting over is this like, if I sent myself
*  back to where I was and I had to start over, if I was like right now, I became 20 years, 20 years
*  old and I'm like, okay. So that someone, someone, so it could be useful to someone in, in the
*  current position of 20 years old or, or so. I guess the, you know, I would pay a lot of attention
*  to the variety of techniques that are available and basically try to learn all of them. So like,
*  I would, you know, essentially I think what I'm saying is I would preserve the generality,
*  but the generality would now maybe be a little less broad in the sense that there's so much
*  more that has developed in the context of, you know, deep learning and reinforcement learning and
*  statistical methods, as well as the neuroscience and psychology and so on that, yeah, I, I wouldn't
*  sort of throw out the breadth, but maybe it just wouldn't be quite as broad, right? So I'm not sure
*  even exactly what that means per se. So what things would I sort of not pay attention to that I have
*  paid attention to? Yeah, that's, that's a, that was a good question is like, what, what is least
*  important? You know, what, what should people not be paying attention to? I think this is a really
*  difficult question because so many different fields have advanced, have advanced so far to the degree
*  that it actually takes quite a bit of time and effort to become anything more than a superficial,
*  than have a superficial level of knowledge about any of it. And, you know, part of like a PhD
*  program is like, generally a super deep dive in a very narrow topic. But I don't know. And it seems
*  like that's what people are these days is very specialized in a very narrow topic. And that was
*  constraining for me. And I'm sure for you that that was, you know, constraining because you do
*  have such a diverse base of knowledge. So I don't know, it's just difficult to know how to proceed.
*  It is. Yeah. And there aren't like programs in, I mean, yeah, you know, there are theoretical
*  neuroscience programs. And they will generally give you sort of deep on the neuroscience side
*  and pretty good on the technical side, but not as deep as you'd get if you were in an AI program.
*  But yeah, so trying to find the right, like basically you have to make a choice. And that
*  that would be the hard part, right? Is like, do you choose AI? Do you choose theoretical neuroscience?
*  Do you choose biological neuroscience, experimental neuroscience? Do you choose
*  philosophy? Do you choose psychology? Do you choose mathematical psychology? Like,
*  yeah, it's definitely a hard thing to do. Maybe I was lucky in that when I was making those choices,
*  you know, there weren't established AI programs that focused on neural networks and, you know,
*  that were related much to how the brain worked and so on. So, you know, philosophy was one of
*  the few places where understanding how the mind worked and thinking about connectionism and
*  symbolism all at the same time on equal footing could be done.
*  Would you say that philosophy is the most indispensable bodies of knowledge that you
*  carry? I'm pressing you, I know, but because philosophy is usually the thing that people
*  throw out first. Get rid of it. Who cares, right? Yeah, I think it's very important from a
*  sort of like high level perspective, like, as we were talking at the beginning, and as you mentioned,
*  asking the right questions, being sensitive to what the meanings of the words in those questions
*  really are, what people had thought about in the past along those questions. To me,
*  that's all very helpful. Philosophy does tend to sort of progress in a noticeable way much more
*  slowly than a lot of these other fields. And so doing it professionally and like writing lots of
*  philosophy papers and all that kind of thing often doesn't seem like it kind of advances as quickly,
*  unsurprisingly, because, you know, often wrestling with extremely complicated and difficult ideas.
*  So, yeah, not dispensable, but also not always easy to spend tons of time doing because you have
*  to be very patient because the progress is slow and so on. But yeah, I don't really think that's
*  an answer to how to specify the ideal course of study. Yeah, exactly. For getting into
*  biological cognition. I mean, maybe just the important thing is just to start and just move
*  forward no matter what. Right? Yeah. My strategy was do what I think seems cool at the time.
*  That was literally what drove me. So, yeah, building a brain would be neat. How do they work?
*  All right. Well, what's one way to ask that question? Oh, that's an interesting way to
*  ask the question and some interesting answers. Pretty much as much forethought as I gave it.
*  Well, it's brought you to a really cool place. So again, Chris, thank you so much for spending
*  so much time answering my silly questions and going down a long path with me today. I really
*  appreciate it and really good luck moving forward. Not that you need it. Thanks, Paul. It's been a
*  ton of fun. Brain Inspired is a production of me and you. I don't do advertisements. You can
*  support the show through Patreon for a trifling amount and get access to the full versions of all
*  the episodes, plus bonus episodes that focus more on the cultural side but still have science.
*  Go to braininspired.co and find the red Patreon button there. To get in touch with me, email
*  paul at braininspired.co. The music you hear is by The New Year. Find them at thenewyear.net.
*  Thank you for your support. See you next time.
