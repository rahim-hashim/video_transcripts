---
Date Generated: June 24, 2024
Transcription Model: whisper medium 20231117
Length: 6108s
Video Keywords: []
Video Views: 451
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2024/06/24/280-francois-chollet-on-deep-learning-and-the-meaning-of-intelligence/

Which is more intelligent, ChatGPT or a 3-year old? Of course this depends on what we mean by "intelligence." A modern LLM is certainly able to answer all sorts of questions that require knowledge far past the capacity of a 3-year old, and even to perform synthetic tasks that seem remarkable to many human grown-ups. But is that really intelligence? François Chollet argues that it is not, and that LLMs are not ever going to be truly "intelligent" in the usual sense -- although other approaches to AI might get there.

François Chollet received his Diplôme d'Ingénieur from École Nationale Supérieure de Techniques Avancées, Paris. He is currently a Senior Staff Engineer at Google. He has been awarded the Global Swiss AI award for breakthroughs in artificial intelligence. He is the author of Deep Learning with Python, and developer of the Keras software library for neural networks. He is the creator of the ARC (Abstraction and Reasoning Corpus) Challenge.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 280 | François Chollet on Deep Learning and the Meaning of Intelligence
**Mindscape Podcast:** [June 24, 2024](https://www.youtube.com/watch?v=rTh3UcPj_7o)
*  Hello everyone and welcome to the Mindscape podcast. I'm your host Sean Carroll.
*  You know that artificial intelligence is in the news.
*  We've talked about AI in various different ways here on the podcast,
*  especially over the last couple years where chat GPT and other large language models have really become an enormous
*  study of interest to many people for financial reasons, for intellectual reasons. They're
*  becoming everywhere, right? Google has put them on the first page of its search results.
*  Lots of people are using large language models to write texts.
*  You can write programs using large language models. You can write the syllabus for your college course, etc.
*  It's clear that this technology is going to have an enormous impact on
*  how humans behave and live going forward.
*  But there are subtleties. One of the things that I've talked about is the idea that
*  large language models are
*  amazing because they are able to mimic
*  human speech and behavior, right? They are able to sound enormously human without
*  actually thinking in the same way that human beings do. Large language models in some sense
*  memorize lots of things. They know a lot of facts about the world and they're super good at
*  interpolating between things that they know.
*  That includes interpolating different kinds of things that have never been interpolated before so they can seem creative.
*  They can do things that have never been done based on the training data of things that have been done before.
*  They're less good at going outside of the range of that training data and
*  one can argue that the processes by which they come up with their outputs are very different than what a human being does in actually
*  thinking reasoning about the problem presented to it.
*  Many people, especially people who are experts in AI,
*  understand this attitude perfectly well. It's certainly not new with me.
*  It's well known to many people,
*  but it is denied by other people who are much more impressed with the progress in large language models and think that we're close to
*  AGI, artificial general intelligence.
*  So I thought it would be fun to talk to someone who is in the front lines of
*  developing deep learning models in AI more generally. So today's guest is Francois Chollet.
*  He's a relatively young guy, but just to give you a sense of his accomplishments, he's a deep learning
*  researcher at Google.
*  One thing he's done is to develop a software package called Keras,
*  Keras, which is a software library that can be used to interface
*  with deep learning techniques.
*  So you could download it onto your computer and play with Keras and develop your own large language model or
*  modify someone else's large language model if you want to. It's become incredibly popular, three million something users at last count.
*  So it's had an impact on the field.
*  Francois is also the author of a book called Deep Learning with Python. I think there's also
*  a version using R, capital R, the computer language.
*  So you could read that and learn about deep learning yourself.
*  And finally, Francois has thought deeply about what it means to say that something is intelligent.
*  And in particular, he strongly denies that modern large language models are
*  intelligent in the conventional sense.
*  He says that what they've done is they've memorized a bunch of things effectively and like we said can interpolate between them and that
*  it gives them a wonderful ability to score well on many
*  current measures of intelligence that we human beings use on each other.
*  Large language models are good at passing tests, right? The bar exam for law school or whatever.
*  Large language models are really good at that.
*  Francois makes the case that this is not because they're intelligent.
*  It's just because they've learned a lot of things. And to make that clear,
*  he wrote an influential paper called On the Measure of Intelligence where he makes the case
*  he will explain it better than I could. But he makes the case that the whole point of intelligence is to go beyond
*  what you've learned, right? To not merely master a skill,
*  which large language models can do. They can learn whatever the particular subject matter is and spit it back at you.
*  But to sort of abstract
*  skills that you're not being explicitly taught.
*  So as Francois says, he has a three-year-old kid who's very good at generalizing from just a few examples
*  to build things with Legos that he's never seen before in a way that modern
*  LLMs are not able to do. So this proposal from Francois has gone on to become a new competition.
*  The, what is it called? The ARC-a-thon. ARC stands for
*  Abstraction and Reasoning Corpus, ARC. And the idea is that rather than using
*  questions from typical IQ tests or standardized exams or whatever, they have developed a set of novel
*  logic puzzles.
*  Okay, if you believe that intelligence has something to do with solving logic puzzles,
*  at least here is a set of logic puzzles that are not already out there in the training data that many LLMs have already had
*  access to. And guess what? A human being can easily do very well on this ARC test that has been developed.
*  80% success rate, etc. Large language models don't do so well. Some of them as low as 0%, but you know, typically
*  20-30%, something like that.
*  Evidence for the fact that whatever they're doing, it's not quite intelligence yet, which is not to say we can't get there.
*  So the point of the ARC competition is to
*  incentivize people to go beyond large language models to develop AI systems that truly are intelligent.
*  So it's not just a sort of skeptical attitude. It is a
*  attempt to push us in better directions.
*  We don't know when and if AI is going to become generally intelligent. We know it's not there now,
*  but maybe it'll get there soon. It depends on how clever we human beings are at developing such things.
*  If you visit the show notes page for this episode of the podcast at
*  preposterousuniverse.com
*  slash podcast, we'll give you links to all these things, the paper, the books, the competition, and so forth.
*  Okay, occasional reminder that you can support the Mindscape podcast on Patreon. Go to patreon.com slash Sean M.
*  Carroll and kick in a buck or two for every episode of Mindscape. In return,
*  you get ad-free versions of the podcast as well as the ability to ask AMA questions once a month.
*  Very, very worthwhile rewards for such a minor contribution. And with that, let's go.
*  Cross-flawed Charolais, welcome to the Mindscape podcast. Thanks for having me.
*  So I've talked to
*  people doing AI before on the podcast, and I have this picture in my mind that I just want you to tell me whether I'm on the right track or not.
*  That back in the day, there were these arguments about symbolic approaches to AI
*  versus connectionist approaches. In the symbolic approaches, you would try to define variables that
*  directly correlated to the world in some way and then hope that the AI would figure out how they all fit together.
*  Whereas in the connectionist approaches, you just put a bunch of little processors in there hooked up in the right way and
*  hope it learns things. And in the early days, the symbolic approach ruled but didn't get very far.
*  And these days, we've had amazing progress with deep learning and large language models that are basically in the connectionist
*  tradition. Is that rough picture approximately correct?
*  On a very long time scale, yeah, that's approximately correct.
*  Symbolic methods. So the big dichotomy here is actually between
*  having programmers hard code a model, a symbolic program,
*  of the task that they want to do versus having a system that can actually learn from data how to perform the task.
*  And symbolic approaches, of course, are much more tractable if you don't have a lot of compute, because if you only have a
*  very small computer, but you have a good brain, you can just figure out the right way to describe a task and then the computer can perform a task like playing chess, for instance.
*  However, if you want to make learning work, that's where you need some amount of skill. And as computers got better, then machine learning started getting really popular.
*  And machine learning did not actually start getting popular with so-called connectionist approaches initially. So the one of the first big
*  after neural networks, one of the first big breakthroughs of machine learning were SVMs. That's a learning algorithm that can do classification, can do regression. After that,
*  random forests got very popular in the early 2010s.
*  Then gradient boosted trees got also very popular. And by the way, so random forests and gradient boosted trees are not
*  neural network based. They are not even curve fitting based. And after that, you had the great rebirth of neural networks with the rise of deep learning. So starting around
*  2011, 2012, some people started training deep neural nets, specifically deep confidence. So convolutional neural networks, which is the kind of neural nets that
*  does very well with images. It's basically a kind of neural net that knows
*  how to split an image into small patches and look at each patch separately, then merge the information that is seen. And progress is like this in a sort of modular, hierarchical fashion.
*  Not too differently from what the visual cortex is doing, by the way.
*  And so this new GPU based carbonates started winning machine learning competitions.
*  So Dan Searson in 2011 won the Carpool Minor Academy competitions with this technique. Then in 2012, we had the big breakthrough with the ImageNet,
*  large scale image classification challenge that was solved with GPU trained carbonate.
*  And then in the following years, we had this gradual but very, very fast and sort of unstoppable rise of deep learning. Every year there were more people doing deep learning and deep learning could do more and more things.
*  And one thing that has increased quite dramatically is the scale of these neural nets.
*  So around 2016, 2017, we had the arrival of a new kind of architecture that got very popular, which was the transformer architecture for sequence processing. Before that, sequence processing was done with
*  regular neural networks, specifically the LSTM architecture, which dates back from the early 90s.
*  In fact, it's usually often the case that neural net research is very much grounded in stuff that's from the 80s and 90s.
*  Which you make sound like ancient history, but I was alive then, so it's not that ancient.
*  Yeah.
*  You know, I feel like most people doing deep learning today have actually very little knowledge of anything that came before 2015, to be honest.
*  And everyone is pretty much using the transformer architecture at this time, which was developed in late 2016 and got public in 2017.
*  And it works really well. And it works for sequence data, but pretty much anything can be treated as sequence data. So it actually works for images, it can work for videos, it can work for pretty much whatever you want.
*  And finally, we had the rise of Gen.E.I. So even larger scale transformers trained on
*  as much data as we can cram into them to train on the entire internet. In fact, they're not just trained on the entire internet,
*  they're trained on the entire internet, plus a lot of manually annotated data that's collected specifically for these models.
*  Currently, there are thousands of people who are employed full time to create training data for these models.
*  And they're not paid very well, usually.
*  I think I read that in something you wrote, and it kind of did take me back a little bit. So maybe, can you elaborate on this?
*  We'll get back to the architectures and so forth. So there are people, what are they,
*  writing texts for large language models to be trained on, or are they interacting with the models to correct their mistakes?
*  So typically, the process, it's more the second one. They're interacting with the model to correct their mistakes.
*  So now they said interacting with the model, but basically, they are receiving a stream of queries
*  that the model does not seem to be very good at, and they write answers for these queries,
*  or the correct and existing generated answer.
*  And so this is called data annotation, or sometimes data rating.
*  It can also, by the way, take the form of actual ratings, meaning that you get a choice between multiple generated answers, and you pick the best one.
*  And every company out there that's training these foundation models is employing typically several thousands
*  of people just doing this full time. And this is, by the way, this is very much what makes these models
*  useful. It's the fact that not only they're trying to predict the next word across
*  pretty much all the texts you can find on the internet, but they're also trained to sort of like prefer the right answer across
*  millions of different manually annotated queries.
*  So as we're recording this in June 2024,
*  many listeners will be familiar with a
*  set of problems that Google was having, having put forward their AI assistant onto search, and
*  sometimes it would give very bad answers. And I guess the hope was
*  that, like you say, individual human beings could go in there and just stamp out the bad answers one by one, but that hope seems to
*  be a little bit gloomier than originally intended.
*  That's right. And it's one of the big challenges and big limitations of LLMs is that
*  you have to apply these pointwise fixes, which are very labor intensive, right?
*  And they only address one query at a time. It is virtually impossible to fix
*  a general category of issues at once. And the reason why is because
*  these models, they are basically big curves, like they're big differentiable parametric curves that are fit
*  to a data distribution. And so you cannot really input into them
*  symbolic programs, for instance, that would be valid for a very large category of problems.
*  You can only input into them data points and they will fit these individual data points and they will be able to interpolate across them.
*  So giving them some amounts of generalization power,
*  but not that much. And so if you want the LLM to perform well,
*  the only option you have is that you need to densely sample
*  the space of queries in which it's going to have to operate.
*  And this is kind of the problem that we saw with the weird
*  Google AI answers is that they tended to be unusual queries.
*  And of course, you know, these models, they don't actually understand the queries you're giving them.
*  They are just mapping the query on the curve. So you can sort of picture the curve as
*  a surface. It's many forms, right? So it's like, you can picture it, I guess, in 3D. You can imagine a 2D
*  surface inside a 3D space.
*  And it's exactly what it is,
*  like a napkin. It's exactly what it is,
*  except in a space that has thousands of dimensions.
*  And basically, you know, in that space, different dimensions encode different axes of meaning,
*  and they can sort of like interpolate across data points, but they cannot really
*  model, for instance, a situation described in a query, especially not in quantitative terms.
*  Which is why they are not reliable. And my advice in general, when people start using
*  financial models, is that they're very good at giving you answers that are
*  directionally accurate, that are a step in the right direction, but they're extremely valid,
*  giving you exactly correct answers. So you should pretty much never
*  ask a foundation model, especially if it's a quantitative problem, by the way,
*  to give you an exact answer and then just blindly use that answer.
*  It's typically better to use it as a sort of like stepping stone to get you something that's
*  in the right direction, and then you refine it yourself. Or perhaps you could also automate that
*  and add a sort of symbolic search system to automatically refine the answer. Because if
*  you have a symbolic search system and you have some way of telling whether your answer is correct or
*  not, then you can just search across a range of answers and verify them. So use the LLM to provide
*  you with a sort of initial smaller search space, and then use a symbolic system to find the exactly
*  correct answer within that space. But never basically blindly trust anything that's written
*  by one of these models. I have learned that myself. I'm sure that you have also. But so to put it back
*  in the original terms, I'm getting the impression that rather than thinking of things as symbolic
*  versus connectionist, maybe it's more helpful to think of models where the programmer tries to
*  build in a structure versus models where the model learns a structure just from an enormous
*  amount of data. That's right. That's right. And one thing that's interesting here is that
*  in the first case, there's no intelligence involved. The only intelligence in the picture
*  is the intelligence of the programmer that understands the task, understands the problem,
*  models it in their head, and then writes down exact instructions, a description of the task,
*  description of the task that is so precise that there is no uncertainty left. And when you actually
*  run the program, it will never have to deal with any kind of novelty, anything that it does not know
*  what to handle. Because the programmer did a good job. They anticipated everything, right? Every
*  edge case, everything. And what the program you get, people are going to call it an AI,
*  but there's actually no intelligence. It's just a crystallized static program. The intelligence here
*  is the mind of the programmer that developed that program, right? Intelligence is this ability to
*  look at a novel problem, something you've not seen before, and come up with a solution,
*  write the program, right? And when you look at learning systems, clearly they're capable of
*  learning, capable of learning how to solve problems on their own or almost. So clearly they must have
*  some intelligence. But the most popular methods for doing this today are just curve fitting.
*  And curve fitting, I mean, clearly it's a form of learning. A curve trained with gradient descent
*  has non-zero intelligence, right? Because it turns data into solutions at some rate,
*  according to some sort of conversion ratio, which is not a very good conversion ratio, by the way.
*  It's curve fitting, it's extremely inefficient. But it has very, very low intelligence for this reason.
*  A system that is very intelligent would not be limited to these sort of pointwise
*  mappings like LLMs. Instead, if you wanted to fix an issue in an actual intelligent system,
*  you would just explain it, why the answer they gave was wrong. And then they would automatically
*  apply the patch, apply the fix to the entire underlying category of issues, right? Instead,
*  you have to apply these pointwise fixes, right? And the reason why is really because curve fitting
*  is extremely data inefficient, right? It's a very, very low intelligence type of learning.
*  And from those descriptions, well, I'm sure we'll get to this more later in the podcast,
*  but you can see why it would be very hard for either approach to give rise to true creativity,
*  right? One where the programmer puts in all the structures, kind of limited in that way.
*  Curve fitting is kind of limited once you want to wander outside where the data already is.
*  Yeah. If you adopt a symbolic approach, you're entirely limited by the sort of search
*  space that the programmer hard coded into the system. You're limited by what the programmer
*  can anticipate and imagine. And if you employ curve fitting, then you are limited to basically
*  the convex hull of the latent space representations of your input data points. So basically,
*  you're limited to interpolations between data points in your trained data. And you cannot really
*  create anything new, anything that you did not expect if you had seen everything in the trained
*  data. And by the way, this is kind of like the reason why foundation models often give you the
*  impression that they're being creative. It's because you haven't seen everything they've been
*  trained on. It's impossible. They've been trained on so much data. So they can surprise you. But if
*  you had seen everything, they would not surprise you. And so that doesn't mean that creativity
*  is something that cannot be achieved by an algorithm. I think it can be. But you have to
*  employ the right set of methods. I think if you look at the history of computer science,
*  when we saw real invention, real creativity initiated by an algorithm, it's been in cases
*  where you had a very open-ended search process operating over a relatively unconstrained search
*  space. Because if the search space is fairly unconstrained, then no human can anticipate
*  everything it contains. And the search process might find really interesting and useful and novel
*  points in that space. So for instance, genetic algorithms, if implemented the right way,
*  have the potential of demonstrating true creativity and of inventing new things in a way that
*  LLMs cannot. LLMs cannot invent anything because they are limited to interpolations.
*  A genetic algorithm with the right search space and the right fitness function can actually invent
*  entirely new systems that no human could anticipate.
*  Maybe you should explain to the listeners what a genetic algorithm is.
*  Absolutely. So a genetic algorithm, it's basically a discrete search process. So it's inspired by
*  biological evolution. In biological evolution, individuals can't understand the whole thing.
*  In biological evolution, individuals have a genome and they pass on half of their genome to
*  offsprings. And this is driven by a natural selection in order to have offspring. Well,
*  you need to survive, you need to reproduce, and so on. And so you end up with individuals that are
*  increasingly good, increasingly fit at surviving and reproducing. So this sort of criterion
*  of survival and reproduction would be called the fitness function.
*  And you can try to implement a computer version of this, where you have
*  points that are described in some way. That's going to be the genome. And you're going to
*  apply, you're going to code up some sort of fitness function, a way to evaluate how good
*  certain genome is. And you're going to generate a bunch of genomes. You're going to apply a
*  fitness function, select the best ones, top 10% or something. And then you're going to modify them.
*  And that could be random mutations. That could be crossover. You take parts of one genome and
*  cross it over with another. Because you're not limited by sexual reproduction, you can actually
*  do whatever you want. You can do crossover between many individuals, for instance.
*  But you have basically some sort of discrete mechanism for generating new combinations or
*  compositions or mutations for existing individuals. And now you have the next generation and you apply
*  the fitness function again, the selection function again. And you repeat. And assuming that your
*  search space, which is basically the space of possible individuals that can be represented
*  using your genome, assuming that it's fairly unconstrained, you may end up with some very
*  interesting findings. The OG genetic algorithms guys, they came up, for instance, with a very
*  novel design for an antenna using this technique. And this is the kind of design you could never
*  have obtained with an LLM trained on every antenna design out there. Because it's actually novel.
*  In order to get novelty, you need search. LLMs cannot perform search. They can only perform
*  interpolation. Good. I did want to, at the risk of scaring some listeners off, I did want to spend
*  just a few minutes digging into how the LLMs work. The LLMs are the things that have gotten so much
*  experience, so much attention these days. And maybe this is the wrong place to begin, but I'm
*  trying to wrap my head around thinking of words as vectors, assigning values to words and saying
*  that they're near to each other or far to each other in a vector space and taking dot products.
*  Can you explain a little bit about how that works?
*  Sure, sure. So the big idea behind LLMs and behind deep learning in general is that
*  the relationship between things can be described in terms of distance between things, like a literal
*  distance. So you're going to take things and things could be pixels or image patches or they
*  could be words or tokens. So a token is, you can think of it as like a word. It could be a sub word
*  as well. A token is basically a word. And the idea is that you're going to map your things,
*  so your tokens for instance, into some vector space. So vector space is basically just a
*  geometric space, points of coordinates. And points are things, like points are tokens.
*  And you're going to try to organize these points so that the distance between points represents
*  how semantically similar they are. And by the way, this is very similar to heavy end learning.
*  In heavy end learning, neurons that fire together, wire together.
*  In the real brain.
*  In real brains, exactly. And how tightly wired two neurons are could be interpreted as a distance
*  between them. So you could say that it's more of a topological distance than an actual geometric
*  distance in this case. But the idea is that if neurons encode concepts, then concepts that tend
*  to co-occur together are going to end up closer in the network. So closer in terms of some distance
*  function. And it's exactly the same with transformers, actually. So the way transformers
*  work is basically, so you map these tokens to points in the vector space. And then you're going
*  to compute pairwise distances. And they are cosine distances. Basically dot products between
*  words and between tokens. And you're going to use that to figure out a new coordinates for your
*  points. So incrementally updated coordinates for your points. And you're going to do that
*  by taking into account the pairwise dot products between tokens in a certain window of text. And
*  what you're effectively doing is that when tokens already have fairly high dot products
*  between each other, they are going to be pulled closer together.
*  Yeah. So the new token representations for the next layer, they're basically obtained by
*  combining, by interpolating effectively between existing tokens. So one token is going to become,
*  the representation for one token is going to become an interpolation between the representations
*  of surrounding tokens. And that's basically weighted by how related to each other they already
*  are. They are close to each other. They already are in this space. So it's basically
*  a kind of headband learning. So there is some connection with the way the brain learns. But
*  what you end up with once you've done this across many layers in a very high dimensional space,
*  and across a lot of data, what you end up with is a high dimensional manifold, which is basically
*  just a surface. As I said, you can think of it as a kind of like 2D napkin in a 3D space.
*  And that's exactly what it is, because it must be smooth, and it must be continuous,
*  because it needs to be differentiable. It needs to be differentiable because the whole process is
*  trained via gradient descent. Gradient descent is basically the only really scalable way,
*  efficient and scalable way that we have to fit curves like this these days.
*  And on this manifold, your token, so your information is organized in a very semantically rich
*  fashion. And things that are semantically similar are going to be embedded very close together
*  and different axes, different dimensions along the manifold are going to encode interesting
*  transformations of the data, transformations that are semantically meaningful and so on.
*  And what you end up observing is that the way your tokens are organized on this manifold
*  ends up encoding a bunch of useful semantic programs. So basically,
*  patterns of data transformation that occurred frequently in the trained data, and that the model
*  found useful to encode in order to better compress the semantic relationships between your tokens.
*  And this compression is necessary because you need to cram all of these relationships on this
*  manifold, which has very high dimensionalities. We can cram a lot of things into it, but it's still
*  not infinite. You still have pretty tight constraints. So you actually need to compress
*  things. And because you need to compress things, you're going to find these useful reusable programs
*  that help compress the data, express it in a more concise fashion. And that's really, I think, the
*  most effective way of thinking about LLMs is that they are big stores of programs,
*  millions of programs. And they're not, when I say program, they're not like Python programs or C++
*  programs, which are symbolic programs. Instead, they are more like vector functions. And that
*  means that you can actually interpolate between different programs. So a vector function is
*  basically just, it's a mapping between a subset of vector space and another subset. And it
*  encodes a useful, interesting transformation. Like, for instance, transforming the style of a
*  paragraph from one style to poetry. And it's not obvious that there exists a vector space in which
*  you can embed words in such a way that you could define a vector function that does something like
*  this. It seems extremely hard to imagine. And in fact, before LLMs actually showed that it was
*  possible, I don't think many people would have believed it, but it works. And that's really the
*  magic of deep learning is that you express relationships between things as a distance
*  function in vector space. And you do it at scale and magic starts happening. It turns out that you
*  can fit curves to basically anything if you have a large enough space and enough data.
*  I mean, I'll confess, I would have been very surprised if you had told me 20 years ago.
*  Anyone would have been very surprised. I don't think anyone anticipated this to happen.
*  For example, an example that you've used that I've seen elsewhere, thinking of these tokens
*  as elements of a vector space, you can have equations like king minus man plus woman equals
*  queen. Yeah. So that's an example from where to back. And where to back is only distantly
*  related to LLMs. But I think where to back is sort of like a miniature world of the sort of
*  phenomena that you see in LLMs. And in particular, I think it's where to back is good to illustrate
*  what is a semantically meaningful vector function. So in this case, you have worlds represented as
*  points in the vector space, and you can actually add a certain vector to any point to get a new
*  point, which is a new word, of course, because a point equals a word. And I think this vector
*  will consistently transform your words in one way, like for instance, making the word plural,
*  or going from a male word to a female word, that sort of thing.
*  And you can see how once that starts to work, it's almost as if some understanding is creeping in
*  to the model, or at least the appearance of understanding.
*  That's right. So yeah, I guess it kind of depends how you want to define understanding. But what's
*  going on is that having to organize tokens in a constraint space like this kind of forces you
*  to arrange them in such a way that different dimensions in your space start representing
*  transformations that enable compression of your space. You know what I mean?
*  And you see that scale with LLMs. And because LLMs are actually nonlinear,
*  the vector transformations that you're going to be looking at are much more complex, much powerful,
*  understanding vectors that can be completely arbitrary, actually completely nonlinear.
*  And LLMs, there are collections of millions of very useful vector programs like this that enable
*  a more concise representation of this token space. And when you're prompting an LLM with some query,
*  what it's basically doing, what a human would do is try to understand the words and picture them
*  in their mind, basically create a model for what's being said. Then you can maybe run some
*  simulation in this model and so on. So basically, you have this understanding of what is being
*  described and what is being asked. And what the LLM actually does is that it will fetch
*  from its collection of programs. You fetch either a program it has memorized or maybe
*  an interpolation across different programs it has memorized. And by the way, LLMs are actually
*  pretty bad at compositionality. They're bad at composing different programs. They can interpolate
*  between programs. You cannot really chain many programs like this with LLMs. You're pretty much
*  limited to patterns that have been exactly memorized by the model in its trained data.
*  So it's fetching a program and it's reapplying the program to the input you're giving to the model.
*  And when it works, it works. So for anything that the model is familiar with, something that is seen
*  thousands of times in its trained data, it works. So it's great. And because they've seen so much
*  data, there are millions of possible queries where it will give you exactly what you want.
*  So it can be tremendously useful. But anything that is more unfamiliar, it will not be able to
*  make sense of it. It will fetch a program applied. It's going to give you the wrong results. And for
*  the LLM, there is absolutely no way of telling because it's doing the exact same thing in any
*  case. There's no difference for the LLM between generating something that's correct. There's
*  versus generating something that's completely off. And so unfamiliarity is one way to trip up LLMs.
*  LLMs really can only give you the right answer for something they've seen before,
*  which is why data annotation, manual data annotation is so important. But it's not the only
*  failure case of LLMs. You find also sort of like the opposite failure case where
*  when you have a model that is too familiar with a certain pattern, it will be unable to deviate
*  from it. And a common example is, for instance, the sort of like logic puzzle where it's heavier,
*  like one kilogram of steel or one kilogram of feathers, for instance. And this is a logic
*  puzzle that occurs tens of thousands of times on the internet. And for this reason,
*  with the earlier LLMs, like for instance, the original challenge before, if you asked it,
*  what's heavier, like one kilogram of steel or two kilograms of feathers? It would be, oh,
*  they weigh the same. I know the answer. They weigh the same. So it's not actually trying to
*  read and understand the query. It's just fetching the pattern and reapplying it. And so this has
*  been fixed since, of course. But the way they fixed it, again, it's these pointwise patches.
*  They just explicitly teach the LLM about this new pattern for solving this particular kind of query.
*  And if you teach the LLM the right way, then it will start paying attention to the numbers
*  you're providing. So that's one example. There are many other such examples. And even today,
*  you take any of these LLMs, like Gemini or GPT-4 or whatever, you can find common logic puzzles
*  like this, where if you provide a small variation, the LLM will break down. Basically, anything that
*  has not been patched by hand will still fail today. And in general, this is also the reason why
*  LLMs are very sensitive to the way you phrase things. They're very brittle in that way.
*  And this is kind of what gave the rise to the concept of prompt engineering. So prompt engineering
*  is this idea that if you just ask your query the right way, like there is a right way and there is
*  a wrong way, if you just ask the right way, you get the right result. And another way to interpret
*  it is any time you find a query where you're getting the right answer, it is most likely
*  possible to modify the query a little bit in a way that would be totally transparent to a human,
*  that would make total sense to a human, but it will cause the LLM to start failing. And this is
*  true for virtually any query. You can always rephrase in a way that doesn't actually change
*  the query, but it will make the LLM fail. And specifically, the way you find these variations,
*  you just try to make the query slightly more unfamiliar or unexpected compared to what's on
*  the web. So let me see if I understand because you mentioned before the idea of the convex hull.
*  So you and I know what that means, but the listeners out there should envision a set of points.
*  And we're saying that not only, I think what's being said is that not only can the
*  LLMs or deep learning models interpolate along the set of points, but also sort of the interior
*  that is defined by that set. So if I ask it for a Shakespearean sonnet that explains spontaneous
*  symmetry breaking in particle physics, maybe no one has ever written such a thing before,
*  but it knows a lot about Shakespearean sonnets. It knows a lot about particle physics and the
*  vocabulary words. So we can sort of interpolate its way into giving you a good example.
*  Yeah, that's right. For instance, you could ask an LLM to talk like a pirate, but you could also
*  ask it to talk like Shakespeare. But because these transformation vector programs are vector
*  programs, you can actually merge them. You can average them. You can interpolate between them.
*  And that means you can start talking like a Shakespearean pirate, for instance.
*  That works, which is something that you cannot do with explicit logic program, by the way.
*  Good. Okay, so then the question is, does the way that the LLM succeeds at sounding so reasonable
*  and smart happen through implicitly making an accurate symbolic model of the world? Or is it
*  just a set of correspondence between the frequencies of words? Or are those secretly the same thing?
*  So it's significantly more complex. The correct answer is basically somewhere in between.
*  In an LLM, you will not find a symbolic model of the world, but you will find a model of word space,
*  a model of semantic space. And that model has some overlap with the world model that you may have,
*  for instance, but they're different in nature. And the model that LLMs are working with is just
*  not nearly as generalizable as the one you have. In general, any sort of symbolic model that enables
*  simulation is going to be able to generalize much further away from what it has seen before. Because
*  it does not just know about specific situations, it knows about the rules. And it knows about the
*  generated situations. So it can imagine completely novel situations. At the LLM, it's more of a case
*  that it knows about specific situations and can also sort of average, interpolate across situations.
*  But it cannot really move outside of these interpolations and imagine something that would be
*  possible if you knew about the rules generating these situations. And of course,
*  the best way to really develop an intuition about what LLMs do is to extensively play with them
*  and in an adversarial fashion. Try to make them fail, try to start developing a feel for what
*  makes them fail. And many people actually never try that. They just stick as much as possible to
*  things that work. And whenever they find something doesn't work, they blame themselves. They're like,
*  oh, I used the wrong prompt. And as a result, they tend to have this bias that they're like,
*  hey, LLMs understand everything I'm saying. But of course, this is not quite true.
*  It's very difficult to develop correct intuitions about LLMs because they are so counterintuitive.
*  They are sheer scale. They have memorized more text than you were reading your entire life,
*  by like four orders of magnitude. It's kind of hard to imagine that.
*  Yeah. Okay. So are they intelligent?
*  Not really, but they have non-zero intelligence. The way we define intelligence is that
*  intelligence, most people define intelligence in terms of skills. They're like, if it can do x,
*  y, z, it is intelligence. And I'm like, yeah, not quite. This is skill. And being skilled at
*  many things is useful. Obviously, it's valuable. LLMs are valuable in that sense. But when you
*  talk about general intelligence, what makes it general, it's not the fact that you have many x,
*  y, z, that it scales too many tasks. The fact that it should be able to scale to an arbitrary task.
*  You can come up with a new task and teach it to your model. If you cannot do that,
*  then the model is not intelligent. So intelligence, according to me, is the ability to pick up new
*  skills, to adapt to new situations, to things you've not seen before. So for instance, going
*  back to this idea of symbolic AI, symbolic AI cannot adapt. It's a static program that does one
*  thing. It cannot adapt to any novelty. It cannot learn anything. It has zero intelligence. Like a
*  chess engine has zero intelligence. And if you do curve fitting, well, if you just fit your curve,
*  and then you have your static curve, and you do static inference with it, you also cannot adapt
*  to any sort of novelty. You can only be skillful when you are within your data distribution,
*  you're trained at a distribution. Because the curve is static. And this is how deep learning
*  works today. You fit a curve, then it's frozen, and you do inference with it. And such a system,
*  again, has no intelligence. And lots of people talk about, oh, like LLMs can do in-context learning.
*  But that's actually a total misconception. LLMs do no learning. What they can do is that, given
*  a new problem that is slightly novel, but still very similar to something they've seen before,
*  they can fetch the correct program or interpolate across different programs that they've learned,
*  and solve this new, slightly new task. But that's not learning. That's actually fetching.
*  It's not fetching of an answer. It's fetching of the rule set. So it's sort of like one level higher,
*  which is why it kind of seems like learning. It's not actual learning.
*  So that said, you can actually do active inference within the LLM. You can actually make the LLM
*  learn, genuinely learn new things. And you do so by actually adjusting the curve to new set of
*  variables. And when you do that, the main issue you run into is curve fitting is very data inefficient.
*  Even fine-tuning, doing something like Lora, fine-tuning of an LLM is very data inefficient,
*  compared to what humans can do. Humans can actually pick up a new task from a couple
*  demonstration examples. Like I have a 3D wall at home, and it's always fascinating just how quickly
*  it can pick up very, very new skills, like climbing a climbing wall, for instance, or
*  building a car out of Legos. It's seen like five different Lego cars in its life, but it can just
*  imagine its own Lego cars and build them from the pieces it has available. There's no AI system
*  today that can do anything close to this. And it's not like it can do it because it's seen
*  tens of thousands of Lego cars and tens of thousands of other Lego constructions,
*  and it has access to unlimited Lego pieces. No, it's seen a handful. It's assembled a total of
*  probably fewer than 1,000 Lego bricks in its entire life. But no, it can actually create new things,
*  very complex new things. So LLMs can definitely now do that. So they have non-zero intelligence
*  because they can actually adapt to some amount of novelty. They can generalize beyond the exact
*  train data points they've seen, which is what makes them useful, but they can only generalize
*  close to what they've already seen. If you go a little bit too far away, they break down.
*  And they can learn, they can actually do active inference, but in a way that's extremely data
*  inefficient. So they have non-zero intelligence, but it's extremely low. It's definitely not
*  comparable to the intelligence of a three-year-old. My three-year-old is vastly more intelligent than
*  any LLM out there. It just doesn't compare. And I feel sometimes that
*  I feel a deep disconnect with some folks in the AI community that claim that, hey, LLMs today,
*  they're like high school level. This is absurd. I've even met a human being before,
*  if they've interacted with an LLM before. These are completely absurd claims.
*  But they're good at certain kinds of test taking, which is what makes people think,
*  well, that's how we measure intelligence. That's right. And this is one of the cognitive
*  fallacies around LLMs is that the school system loves to test humans on memorization problems.
*  School is mostly about memorization. You typically don't even learn rules.
*  You learn factories. You learn point to point things. And LLMs are vastly superhuman
*  at memorization. They are memorization machines. They have very, very low intelligence, very,
*  very low generalization power, but extremely high memorization. And when it comes to showing skill
*  at something, at something familiar, then you can always trade off intelligence for memorization.
*  Let's say, for instance, you're giving your students a physics exam.
*  And the concepts are pretty challenging. Many students probably haven't fully understood them.
*  But what some students could do is just cram a lot of past exams. And they may not really
*  understand everything, but for each problem, they will memorize the pattern. And if you just give
*  them the same problem with different numbers, they just fetch the pattern. This is exactly what
*  LLMs do. And these students, they can end up scoring very high despite having no understanding
*  of the underlying concepts. And this is true for human beings that have a limited memory and a
*  limited amount of time to study. So they can only memorize 10 exams or something. But what if you
*  have an LLM that can actually memorize 10,000 exams? It can end up showing a very strong
*  difference of skill, difference of understanding with no actual understanding concepts. And how do
*  you tell that this is not true understanding? Because after all, you can do your exam, and your
*  exam is what you're using to judge your students. So how do you tell? Well, the way to tell is that
*  instead of just giving your students or the LLM a problem that's derivative, that's just
*  similar to something that you've given before, you come up with something novel,
*  something that's never been asked before. And in order to approach this, you actually need
*  to think from first principles. You actually need to understand the underlying physics concepts.
*  And if you give that to your students that don't understand the material, but have studied a lot,
*  they will fail. They will score zero. The LLM will score zero as well. But then the smart student
*  from the back of the class that understood everything but just doesn't care to actually
*  memorize anything, they will do extremely well because they're smart.
*  But as a professor, this sounds like hell if I need to come up with novel problems
*  every single time. If you are looking to test understanding and intelligence, then yes, do.
*  On the other hand, if you're fine with just memorization, then you're not. And the school
*  system as a whole is fine with memorization. And sometimes it's because memorization is the goal,
*  but a lot of the time it's out of laziness. It's using memorization as a proxy for understanding,
*  but memorization is not a good proxy for understanding because you can always
*  memorize your way into high school with no understanding.
*  No argument for me there. It's absolutely true.
*  Yeah. And by the way, so just to continue this topic a little bit,
*  on this idea that if you want to test actual intelligence, you need problems that are novel,
*  problems where the test-taking system or human being cannot have memorized the solution.
*  And I actually released a benchmark of machine intelligence a few years back
*  in 2019 that's all about this idea. So it's called ARC, ARC-AGI in the long form. So it's
*  the abstraction and reasoning corpus for artificial intelligence. And the idea is that, well,
*  deep learning does really well by just memorizing data points, but it has very low generalization
*  power. How can you tell that something actually has intelligence? Well, you come up with puzzles
*  that are all unique, all original, never seen before, not similar to anything you would find
*  on the internet. So not really similar to existing IQ test puzzles, for instance. And so ARC is
*  basically a collection of such puzzles and there are public ones, but there are also private ones,
*  which are not more difficult than the public ones, but they're hidden. And this is extremely
*  important, of course, because if they were public, then you could just train a model on them,
*  right? And then it would mean nothing anymore. And as it turns out, deep learning methods and
*  LLMs in particular have scored very poorly on ARC. So we ran a competition on the website
*  Kaggle in 2020 on ARC. And this was back when GPT-3 was available. GPT-3 got released around
*  the same time as we ran the competition. And so people tried GPT-3 and it scored zero, right?
*  And the methods that actually worked were discrete program search methods. So not curve fitting.
*  Curve fitting just doesn't work very well for these type of puzzles. In general, curve fitting
*  works very poorly to handle any kind of novelty. And so later we also ran two years of a new
*  edition of the competition, it was called the OrcaThon. And it remains extremely challenging.
*  It kind of looks like an IQ test and it's very easy for humans to do, but it's extremely difficult
*  for AI to do. And it's very difficult for AI to do. And we're actually about to launch a reboot
*  of the competition on a larger scale. So we are relaunching on Kaggle again. So we're back on
*  Kaggle after four years. And we're going to have over $1 million in prizes. And the goal is to
*  solve ARK to pretty much human level. So something like 85%. And because we know
*  RMs just don't do very well on ARK, the goal here is really to incentivize people to come up with
*  new ideas. To look at these tasks, recognize just how easy it is for them to solve them and how
*  difficult it is for Chad's GPT, for instance, to solve them. And try to nudge people into asking
*  themselves, so what's going on here? Why can I do this? And the machine cannot. And try to come up
*  with new ideas. Try to come up with ideas they would not have pursued otherwise. If they stand
*  under the impression that LMs can do anything, all they need is enough data. That's definitely
*  not true. Even after ingesting every IQ test in the world, they cannot do ARK, even though ARK
*  looks exactly like an IQ test. And fundamentally, the reason why is because each puzzle in ARK
*  is new. It's something that you cannot have memorized before. It was created for ARK.
*  And LMs have basically no ability to adapt to novelty in this way. And if you want to solve
*  ARK, if you want the million dollar, you're going to have to come up with something original,
*  something that's going to be on the path to AGI, as opposed to LLMs, which are more of an off-ramp
*  on the way to AGI. And sorry, just as a tiny technical detail. So when one enters the competition,
*  you, Francois, do not tell their LLMs the questions. They have to sort of let you
*  give the questions without letting the people who wrote the LLMs know what the questions were.
*  Right. So the way it works is that you submit a program in the form of a notebook and you have
*  access to some amount of compute, which is 12 hours with one P100 GPU and one multi-core CPU.
*  And within 12 hours, you need to solve 100 hidden tasks. And so you're just submitting the program.
*  You are never directly seeing the hidden tasks. It's only your program that you've uploaded
*  that's going to see them. And then what you get out of that is a score. How many tasks
*  did your program solve? And then you have to iterate and come up with a better problem.
*  How large are these programs?
*  Well, we'll see. But they're computationally constrained, as I mentioned. They can only
*  run for 12 hours and they only have access to one GPU. So we'll see.
*  But I mean, just as a complete outsider, when I have an LLM, I kind of, since I don't have an LLM,
*  I think of it as it must have a huge amount of data that it needs to call up to answer these
*  queries. Is that part of what they're sending you, the whole sort of compressed data set,
*  or is it just the weights of different neurons?
*  So if you do want to use LLMs in the competition, the way you would do it is you would make your
*  pre-trained LLM part of your program. So before submitting your program, you would fine tune
*  your LLM on ARC data. And by the way, so you're not going to be able to use an LLM API,
*  like the charge PTPI, for instance, because that would require, obviously, it would require
*  showing this third party service, the hidden tasks.
*  Which I mean, again, for non-experts, that means that your competitors are not allowed to call out
*  to the outside world. No, exactly. You actually don't have internet access at all. So anything
*  the program needs access to must be part of the program. So if you want to use an LLM, it has to
*  be an open source LLM and you include it in your program. So beforehand, you would fine tune it on
*  ARC data, presumably, and then you would actually use it as part of your program.
*  And so of course, it cannot be an LLM that's too large because you just have one P100 GPU.
*  So that's enough for if you're using a float 16, that's enough for models that have like
*  8 billion parameters, which is actually pretty good.
*  Okay. And going along with this claim that the LLMs are not really intelligent,
*  I've seen related claims probably from your Twitter account that they can't reason and they
*  can't plan either. Are these, is that a correct characterization?
*  Yeah, that's correct. And I could talk about it a little bit, but really, I think what you want is
*  more than just a vague summary. If you want precise scientific references, I can send you some.
*  So actually, let me pull up. There's this professor from
*  Arizona State University has a really good...
*  We can put up links once we publish the episode on preposterousuniverse.com. So people can get a link
*  to it. Do you have any way to send you links in here?
*  Okay. There's a chat on the right. Perfect.
*  You can check out this YouTube video. And the guy also has a bunch of papers,
*  but really, I could send you a reading list if you want. But if you actually,
*  regardless, investigate the ability of LLMs to plan or reason, you find that no, they cannot
*  plan or reason. But what they can do is memorize patterns, memorize programs, and they can reapply
*  them. And as long as you are looking at a familiar task where the program is applicable,
*  they will be able to show the appearance of reasoning by fetching the program and applying
*  it. But that's kind of different from actual planning and reasoning. And the way you can tell
*  it's different is that if you modify the task a little bit so that the existing program is
*  normally applicable, the LLM will fail. And intelligence would really be the ability to
*  adapt to these changes. So instead of fetching a program, an interpolated program, it will be
*  the ability to synthesize on the fly a new correct program that matches your novel problem. If you
*  have that and you can synthesize this program efficiently from just a few examples, then you
*  have AGR, then you have general intelligence. And if you have this ability, you should also be able
*  to solve ARC, by the way, because this is what ARC is all about. For each puzzle, you get a couple
*  demonstration examples, and then you get a test example. And if you were able to synthesize on the
*  fly a correct program that matches the demonstration examples, then you would be done. LLMs
*  fail at that because all they can do is fetch. And of course, each puzzle is something they've
*  never seen before. And I feel like people who claim that LLMs can reason, they're really stuck
*  at this first stage where they see examples of something that looks like reasoning and they
*  don't try to investigate it. They're like, oh, it's working. This is impossible if the LLMs was
*  not reasoning. But actually what it's doing is just fetching a program. And that's just memory.
*  That's just memory. The LLM is a program database. That's it. It's an interpolated program database.
*  Intelligence is not being an interpolated program database. Intelligence is being the programmer,
*  is having the ability to look at something new and come up with a new program to address it.
*  Well, you just hinted at this a little bit, but I am certainly hearing a lot of people who are
*  nominally experts in the field make noises about artificial general intelligence and how close we
*  are to it if we're not already there. Yeah, I mean, the claim that we're already there,
*  or LLMs are high school level intelligence are absurd. I can't even fathom how I can make such
*  claims. It makes zero sense to me. I don't even understand how I can be so deluded as to claim
*  that. But if you want to ask seriously, under my definition of intelligence, which is obviously
*  correct, my opinion is obviously correct. Of course. That's why you're on the podcast.
*  If you want to ask when is AGI coming, it's very difficult to answer because the situation we're
*  in is that we have no technology today that is on the path to AGI. There is nothing that if you
*  just scale it, it gives you intelligence. But that said, that does not necessarily mean that AGI is
*  very, very far away. Rather, what it means is that you cannot predict when it will arrive
*  because you need to invent something new. But maybe we'll invent it next year. Maybe the ARC
*  competition will actually trigger someone into inventing it. So maybe it arrives next year.
*  It's possible. It's possible, but it's unpredictable because it doesn't exist yet.
*  And the claims that people are making are basically that they're founded on the idea that
*  LLMs are on the path to AGI and that you can predict how their intelligence will scale
*  with compute and data. And the idea is that, well, GPT-3 was middle school level,
*  GPT-4 is high school level, GPT-5 is going to be postdoc level, GPT-6 is going to be a super genius,
*  and so on. None of it makes any sense, even with a very loose definition of intelligence.
*  And do we understand what is going on inside the large language models? I mean, how much of a black
*  box are they? Or are we still kind of doing the science needed to figure out what is inside the
*  box? We are still in the process of figuring out how to interpret what they're doing. But there's
*  already a lot of work that has been done along the lines of interpreting how LLMs work and
*  visualizing what they're doing. There was a paper from Anthropic a few days or weeks ago that was
*  actually really insightful on that topic. Okay. So that's not an intractable problem.
*  We will get there. No, it's not intractable. It's an active area of research and we are making
*  progress. And by the way, every time we get new results, they are along the line of showing that
*  LLMs are actually just pattern matching engines. They are not intelligent. They are interpolative
*  databases of programs. Again, the big difference between intelligence and a program database is
*  like the program database is like GitHub. Intelligence is like the programmer. The programmer
*  individually knows dramatically less than what's in the database. But the database
*  cannot adapt. It's only that fixed set of programs. You can maybe recombine some programs,
*  but you have limited ability to recombine programs. The programmer can actually
*  invent anything, adapt to anything, because it has general intelligence. That's really the
*  difference. And people are like, yeah, so if we just scale GitHub to like a thousand more programs,
*  then it's going to be AGI. But no, it's just a bigger GitHub. It's just a more general GitHub.
*  It is still not a programmer. There is no level, there's no amount of stored memorized programs
*  where you develop suddenly the ability to synthesize your own programs on the fly. It's
*  just not how it works. If it worked this way, we'd already know. Because we've already scaled
*  LLMs to literally all the trained data that's available out there. Which, by the way, is the
*  reason why LLMs have entered the plateau since last year. It's because we've been running out of data.
*  And sure, you can scale compute. You can always keep scaling compute. But it's becoming useless
*  because the curve needs to be fit to something. The curve is literally just a representation of
*  a trained data set. If you've run out of data, then how do you improve the model? Well, one way
*  is that you can try to better curate your trained data. So you don't want to increase the scale of
*  the trained data, but you can increase the quality. That's actually one very promising way of
*  improving LLMs. That's what is actually the way LLMs keep improving today. We've already run out
*  of data. So the next stage is that we better curate the data. We are not training the data
*  LLMs on more data. We're actually curating it. Technically, we're still collecting new data
*  from human raters. So there's a bit of an increase, but on balance actually decreasing.
*  But you're not going to magically find a thousand times more novel, non-redundant
*  data to train these models on. It just doesn't exist. You're not even going to find 2x.
*  And that's the cause of the plateau we've been seeing. And something like GPT-5 is going to be
*  released probably at the end of the year. It's going to be a big disappointment,
*  because it's not going to be meaningfully better than GPT-4.
*  It occurs to me slightly belatedly that we should tell people what GitHub is,
*  because not all of them will know. Right. It's basically just a website that's a collection
*  of many open source programs put there by organizations, by programmers across the world.
*  And that's not, I mean, so that's your analogy for what current generations of large language
*  models are. What we want in some sense is something that is more truly creative and has the ability to
*  learn outside the extrapolation. Yeah, that's right. And even if you take a first-year CS student,
*  their knowledge is extremely limited. They know so little. They've seen so few real-world programs.
*  But yet, they have a much higher ability to write programs that are appropriate for a novel problem
*  compared to a system that has seen every open source program out there,
*  but that has value to intelligence. Yeah. Okay. Very good. So I'm 100% on your side here.
*  I've tried to convince people that the amazing thing about LLMs is how well they can mimic
*  sounding like human intelligence rather than thinking in the same way that human beings do.
*  I think that's actually quite intuitive, because you also see it in humans. You also see it in
*  humans that there is this trade-off between memorization and intelligence, and that with
*  enough memorization, you can actually reproduce the same outcomes as intelligence. And the way
*  you can tell apart someone who's operating based on memorization and someone who's actually
*  intelligent and is operating based on understanding is by presenting them with something new.
*  Right. And so it's true for human beings as well. And the reason why our intuitions are off
*  with LLMs is because the scale of memorization is unlike anything that's possible for humans.
*  Well, and maybe also trying to give some credit to the other side, maybe more problems that we're
*  interested in than we think are solvable by memorizing lots of things rather than by thinking
*  originally and creatively. Sure. I mean, LLMs, memorization is precisely what makes LLMs useful,
*  is that they've stored lots of patterns for how to perform certain actions, solve certain problems,
*  and they can fetch these solutions and reply them. And you may not know about these solutions,
*  so they may actually teach you something new. Can an LLM or could AI in some broader sense
*  be functioning as a creative scientist? Not an LLM, at least not an LLM in isolation.
*  To actually make these systems capable of invention, capable of developing new theories
*  and so on. Well, either you can have a human in the loop, the human is actually in charge
*  of the intelligence bits, the LLM is in charge of memory. So you use the LLM as a sort of extension
*  of your own memory, sort of like brain add-on. So that's one way you can create a super scientist
*  network by just supercharging an existing scientist with access to all this memorized content.
*  And by the way, I'm not convinced this is actually super effective.
*  What we have seen is that LLMs are very good at turning people who have no skill into people who
*  are capable of an average mediocre outcome. They are extremely bad at helping someone who's
*  already extremely good getting better. It basically doesn't work. And there are many reasons why, but
*  empirically, this is what you see. So this is why I don't think LLMs are going to have much impact
*  in science. Science is not about more mediocre papers, it's actually about the top ones. This
*  is what's actually conducted to progress. And the other way that you could try to make
*  these systems capable of novel discoveries is to try to add a search component. Like we talked about
*  genetic algorithms as a way to mine a search space and find unexpected points,
*  unexpected inventions in it. I think you may be able to create sort of like hybrid LLM plus
*  symbolic search systems that would be capable of invention.
*  I definitely noticed when I ask physics questions of LLMs, if it's a fairly straightforward
*  question, they're pretty good. But as soon as it becomes subtle, they are no longer good. I mean,
*  exactly the places where you don't get a lot of coverage out there in the training data,
*  they can't figure it out. And as you say, why would we have ever expected them to?
*  Yeah. If they've seen many instances of the problem you're asking, they have memorized
*  the solution template. And they can just fetch that solution template, reapply it,
*  give you the right answer. If it's something that's slightly different or that's similar,
*  but with maybe one word that actually changes the meaning, something like that,
*  they will still fetch the same template, pretty much. But now it's going to be wrong.
*  And they have no way of doing it. They don't actually understand the words that you're
*  putting in. They don't understand your query. They're just directly mapping to the solution
*  that they think they know. So there's this famous thing where you ask an LLM a question,
*  it gives you the wrong answer. And then you say, no, that sounds wrong. And it corrects itself.
*  Is that because it actually is correcting itself? Or is it just trying another possible answer from
*  its storage of possibilities? It's adapting its solution based on
*  patterns of program modification that you've seen before. So if you propose a pattern and then you
*  add to it, oh, by the way, this is wrong. Here's the correct pattern. And you do this many, many
*  times. The model learns a sort of like modification function that goes from this incorrect solution to
*  fixed solution. And if you tell it, oh, by the way, there's an error, please give me the right answer.
*  What it's going to do is that it's going to apply this modification function to the
*  input it previously produced and going to give you a new answer. And you may be like, hey, so why
*  don't we do it preemptively? But the thing is that in the absence of human feedback, there is no
*  particular reason for the modified program to be more or less correct than the initial program.
*  Only the humans themselves. Yeah. So I think I know what your answer to this is going to be,
*  because we talked about intelligence before. But what about the oft-proclaimed dream of letting the
*  AI program a smarter AI and therefore bootstrapping our way up into greater and greater intelligence?
*  Well, right now, if you want to use an LLM to do programming, it's going to be
*  constrained by its training data. It can only give you things that are simple interpolations of
*  programs, code snippets that are seen before, which is why LLMs work great as a stack overflow
*  replacement, but they do not work great as actual software engineers. Give a lot of novel problems
*  solving. And the average senior software engineer is a tremendously capable novel problem solver,
*  but they're also completely unable to invent a GI. You're not going to get an LLM, which has no
*  novel problem-solving ability. You're not going to get it to invent a GI. I mean,
*  you cannot even invent the solution to an ARC problem, which is pretty trivial. Like a four-year
*  one can do it. So no, that's not going to work. But you could ask, hey, why just use LLMs? Why
*  couldn't we use something else like genetic program search? Since I mentioned that agent
*  algorithms could actually invent new things. Well, in practice, I think this is kind of a bad idea.
*  It is viable in theory, because if you think about it, humans were developed by an evolutionary
*  algorithm. Intelligence is the answer to a question posed by nature. Could we not just get the same
*  answer by asking the question again and just letting a certain algorithm run its course?
*  In theory, yes. In practice, bad idea, because the scale at which you need to run is excessive.
*  And I'll tell you, we already have general intelligence. We are general intelligence.
*  And general intelligence gives you an extremely effective ability to predict what next idea should
*  be tried. If you try to delegate this sort of ideation bit to an algorithm, you're wasting
*  resources. Because what's going to be computationally intensive is actually evaluating
*  the solution, trying to implement it, figure out whether it's actually on the path, which they are
*  not, and so on. The ideation bit is not expensive. And so what you're doing is you're effectively
*  outsourcing the things that you're really good at and that cost you very little to a machine that's
*  really bad at it. And meanwhile, the things that are actually automatable and very expensive
*  while the machine still has to do them. So it's just an extremely ineffective
*  idea, this idea that, hey, we can just brute force our way to the right EGR
*  architecture. It doesn't work. In fact, it doesn't even work on a much smaller scale.
*  And by the way, another issue that you're going to run with this brute force search idea is that
*  you can search is only going to find you points in your initial search space. You start as a human
*  programmer. You start by defining the space you want to search over. Like, open both possible
*  genomes for your search algorithm, for example, for genetic search algorithm, for instance. And
*  what if the correct solution was not in your search space? If you don't know what the correct
*  solution is in advance, you have nowhere to tell. So maybe you're going to be expanding like
*  an extraordinary amount of computer resources to mine a search space that does not even contain
*  the right solution. And this whole idea doesn't even work on a much smaller scale. Like, for
*  instance, neural architecture search for a long time was a thing in deep learning. The idea was
*  that, hey, researchers have come up with a number of architectures that perform really well. Like,
*  there was LSTM, there was Transformers, and so on. Could we not just make a machine that tries
*  a bunch of different architectures and find a better one? It has never worked. There's literally
*  nothing out there that's popular that was developed by an algorithm, despite tremendous
*  amounts of compute dedicated to this idea. And everything out there, like Transformers, for
*  instance, or even the more novel and recent architectures like Mamba or XLSTM and so on,
*  all of these were invented by humans because humans are really good at inventing.
*  You know, like AI is not idea constrained today. So trying to outsource ideation is just a bad idea.
*  But it's not because we're magical, right? I mean, it seems like we should, in principle,
*  be able to write computer programs that are as smart as us.
*  Yes. Yeah, in principle, sure. It's just not a straightforward problem. It's just not an easy
*  little riddle. The human brain is tremendously complex. And no one really understands how it
*  works today. So I guess that you're not going to assign a large probability to the existential
*  threat of AI taking over the world. No. So to start with, because EGR is not a technology
*  that exists today and that we have nothing today that would lead to it. We need to invent it.
*  We need new ideas. And this is the entire point of the Arc-EGI competition, is to get people to
*  connect with new ideas because currently we are stuck, right? We are on an off-ramp. So we need a
*  reset. But even if we had a promising avenue to create EGR, I think the whole idea that EGR is
*  going to end humanity, it's based on several deep misconceptions about intelligence. Like
*  intelligence is pretty much just a conversion ratio between the information you have
*  to the ability to operate in novel situations in the future. Your turning intelligence is you
*  turning your past experience and also the knowledge that you're born with because today you're born.
*  You're actually not born knowing nothing about the world. You know some things about the world.
*  Some things are hard-coded into your genes. And so you turn that, it's mostly your experience,
*  but you turn that into the ability to approach each new day in your life and actually
*  behave appropriately throughout your day, accomplish your goals and so on. And
*  this ability to sort of like chart a path through a situation space does not entail
*  that the system should have goals of its own or values of its own that we need to align with
*  human values. It is just an ability. It's just a path-finding ability. And in order to make
*  something like Skynet or Terminators, well, you need more than just intelligence. You need
*  intelligence plus goal setting, autonomous goal setting. But why would you want to give machines
*  potentially very capable machines with autonomous goals? Sounds like a bad idea. And of course,
*  if you have goal setting, these goals need to be grounded in some value system. You're going to want
*  to give machines their own values. And of course, you're going to want to give machines autonomy
*  because intelligence does not imply autonomy, by the way. So autonomy in the sense that the ability
*  to perceive the world and act in the world without mediation by humans. There is no machine out there
*  today that is unmediated from humans, if only because they need a power supply. There's no
*  machine out there that can just recharge itself and maintain itself in perpetuity.
*  No machine today has autonomy. So in order to create a danger, you would need to engineer the
*  danger very deliberately, like Skynet, to be honest. The whole thing with Skynet is like, hey,
*  we have this very intelligent thing and we've given it the ability to make its own autonomous
*  decisions based on its own value system. Hey, let's look it up to our nuclear arsenal.
*  It sounds like a bad plan. So to make something dangerous, you literally have to create an agent,
*  give it autonomous sensing, give it autonomous acting, give it its own value system, give it
*  its own autonomous black box ability to set goals with no human supervision.
*  And then you give it super intelligence. Well, to be honest, this whole thing already starts being
*  dangerous even before you add intelligence. And intelligence in itself is just a tool. It's just
*  a way to accomplish goals. If you don't hook it up to autonomous goal setting, then it is pretty much
*  harmless. It's not quite harmless because it's going to be in the hands of humans,
*  and humans are dangerous. So it's dangerous in that sense that people are going to potentially
*  use it for bad purposes. But it's not dangerous in the sense that we compete with the human species.
*  It's no more dangerous than any other tool that we have. It's like, you know,
*  efficient energy is not on its own dangerous. It's just a tool. You can use it to create clean power,
*  right? Or you can use it to make a bomb. But if it's going to be threatening, it needs to be
*  deliberately engineered to be threatening. And I think HGI is going to be this. If I imagine
*  something. I also think it's kind of pointless to try to plan for risks in something that is
*  completely unknown. Like we don't know what HGI really looks like. How are you going to plan
*  for how you're going to handle it? So I think how to handle HGI is something that we're going to
*  start making meaningful progress on when we start having it. And again, HGI on its own
*  is not a threat. It's just a tool. To make it threatening, you need to engineer it into
*  either something completely autonomous, which sounds really like a bad idea,
*  or just turn it into a weapon in the hands of humans.
*  Well, you've done a very good job of sort of deflating some of the misconceptions about
*  intelligence and large language models and so forth. But I want to maybe wind up with giving
*  you a chance to talk about your day job, because you work on these things. You actually have a lot
*  of positive things to say about deep learning models, etc. So let's open the door a little bit
*  on what it means to be developing these things. I mean, you have a very successful software
*  package that 3 million people use. Should more people out there be developing and training
*  their own large language models? Absolutely. Not just large language models, but any sort of deep
*  learning model. I think it would be a sad world if there were only a fixed set of companies training
*  models and just giving those models to other people to be consumers of those models. I think
*  we want this technology to be a tool in the hands of everyone. I would like every software
*  developer out there to be able to tackle their own problems using these tools, using deep learning,
*  using large language models, using Keras. And that's basically the reason why I tried to make
*  Keras as accessible as possible, as approachable as possible. So what is Keras? What does that mean?
*  So Keras is a deep learning library. So it's a software library for building and training
*  your own deep learning models on your own data. And it's not necessarily building models from
*  scratch. You can also adapt an existing model, like an existing large language model, for instance.
*  So could you take an existing large language model and then feed it all the transcripts of
*  the Mindscape podcast and sort of elevate their importance in the model so that it would mimic some
*  average scholarly Mindscape guest kind of point of view? That's right. So if you want, for instance,
*  to generate new episodes, that's something you can do. You can take the Gemma 8 billion model,
*  for instance, which is an open source LLM released by Google. It's available in Keras.
*  You fine tune it to predict the next word on your transcripts. You can use a technique called
*  LoRa fine tuning, which is basically compute efficient fine tuning. And now you can
*  generate new transcripts. It's probably not going to be very good, but it's probably going to sound
*  like your podcast. If you start listening, you're probably going to be raising your A-pros.
*  At first glance, it's going to sound like your podcast.
*  Have you done this with the equivalent? I have not, but people have done a
*  generative podcast like this. Yeah. Are you aware of the experiment that was done
*  with the works of Daniel Dennett, the philosopher? No. So Eric Schwitzgabel,
*  who's another philosopher, who was another guest on the podcast, he and some collaborators
*  trained in LLM on everything ever written by Daniel Dennett. And then they asked it some
*  questions and they asked Dan Dennett these questions. Dan passed away recently, but before
*  that happened. And then they asked some philosophers who are familiar with Dennett's work,
*  which of these answers was the real Dennett? And they did better than chance, but in some
*  cases not a lot better, it depended on the question. Yeah. Honestly, if you're just looking at
*  short text snippets in isolation, it's very hard to do. Right. Exactly. And especially, you know,
*  when you're reading the ad with the LLM, it's meaningful because you're interpreting it.
*  You know? Yeah. You're giving it more credit maybe than it deserves. Yes. I mean, LLMs are
*  all about mimicking humans. So they're very good at hacking your theory of mind. Because you have
*  this bias towards interpreting as being like you anything that superficially acts like you. Right?
*  Yep. The intentional stance. Dennett talked about this actually. Yes. So, I mean, how realistic is
*  it for the typical listener with, you know, a relatively late model MacBook Pro to, you know,
*  open up Python on their computer and download some of your libraries and start going to town?
*  It's very easy. So you're going to want a GPU. So if you have a MacBook Pro, one of the recent ones,
*  you actually do have a GPU. And if you're using the TensorFlow backend of Keras, you can actually
*  do GPU accelerated computation on your MacBook Pro. So you can do that. You could also use a free
*  GPU notebook service like Colab from Google, for instance. It's actually extremely easy to just
*  get started and do a Laura Funtune of the GMM model with Keras on your own data. If you already
*  know Python, it's really easy. You'll be done like now. And if you don't, you've written a book.
*  I have written a book. That's right. So the first edition was in 2017. Then there was a second
*  edition in 2021. Now I'm actually writing the third edition. Okay. And I have a lot more content on
*  giant API. I would guess. LLMs and image generation as well. And is there, I mean,
*  besides the fact that it sounds like a lot of fun and also educational to do this, are there
*  use cases for people training their own LLMs to do their own specific tasks? Absolutely. If you're
*  a business and you're having a specific business problem, like, hey, I have this spreadsheet with
*  this information. I want to turn that into a set of emails. For instance, you can just, you could
*  prompt the LLM into doing it. Maybe it will work. But if you want better results, you can just
*  actually adapt the LLM to your problem so that it can not just fetch the right program, but maybe
*  fit the right program from the data you provide. In fact, I would say if you're, if as a business,
*  you want to make extensive use of LLMs, you should be finding your own LLMs because this gives you
*  an advantage. Instead of just reusing the same program database as everyone, which is the
*  sort of public access set in, you are starting to develop your own repository of private programs,
*  trying to train on your own data specific to your needs. And that's very powerful.
*  Is there an app out there that will answer my emails for me?
*  There probably is. There are just so many Genitivi solves.
*  I hope that I don't end up starting Skydent by sending an email that was generated by an LLM.
*  But there are, we shouldn't leave people with the impression that there aren't many, many
*  transformative ways that even LLMs can affect our lives going forward.
*  Yeah. So, you know, many, many people try to do things with Gen.Eye that it may not necessarily
*  be suited for. My advice is in general, do not try to delegate any sort of decision making to the LLM.
*  The LLM is there to give you a shortcut towards the general area that you're looking for.
*  Do not delegate your decision making. Do not let the LLM generate your emails for you.
*  But maybe it can help you write emails faster, for instance. Or maybe you can fix typos in your
*  emails. Anything that would make me go faster is very good. So I'll take that as useful advice.
*  Francois, thank you very much for being on the Mindscape podcast. Thanks for having me.
