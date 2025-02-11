---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 6289s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 282
Video Rating: None
---

# BI 031 Francisco de Sousa Webber: Natural Language Understanding
**Brain Inspired:** [April 12, 2019](https://www.youtube.com/watch?v=0X74YObr4lw)
*  That was the moment when I had a shift of understanding and I realized that it's not
*  so important to look at the algorithm first, it's first important to look at the representation.
*  You wouldn't think this in the beginning, at least I didn't, you actually have to expose
*  yourself because although it costs energy to constantly argue and come up with arguments,
*  that is in the end the best way of refining the structural change that you might have discovered.
*  This is Brain Inspired.
*  Hey everyone, this is Paul Middlebrooks back in my home studio. Today I speak with Francisco
*  de Salsa Weber. He is the founder of Cortical I.O., which is a natural language processing
*  startup out of Vienna, Austria. They process text in a novel way to do all sorts of things with it.
*  I say novel because Francisco developed his technology based on what he believes to be the
*  most reasonable theory on how the cortex processes information. That is essentially the theory of
*  Jeff Hawkins from episode 17 of this podcast. I'll refer you to that episode to learn the
*  ins and outs of Jeff's ideas about cortical information processing. Jeff's hierarchical
*  temporal memory technology takes in and does calculations on long vectors of binary data,
*  made up of mostly zeros and a handful of ones. This is known as a sparse distributed representation.
*  You'll hear Francisco talk in depth about how the text processing works via his semantic folding
*  theory. As a quick primer here, his system that does this called Retina takes in a corpus of text
*  about a subject that you're interested in and it breaks down the text and ends up with words in
*  the form of these long binary sparsely populated vectors, which Francisco calls semantic fingerprints.
*  Words that have similar meanings or are associated with similar concepts have similar semantic
*  fingerprints in that they physically look similar when you visualize them on little
*  semantic fingerprint plots. For example, if you were me in my late high school slash early
*  college days, you might feed it a large body of classic Russian literature. The Retina system
*  would create a Russian literature semantic universe filled with the words from those books,
*  and you could enter your most beautiful sentence and find out whether you're the next Dostoevsky
*  or the next Tolstoy or something along those lines. Francisco shares how he came to this
*  current solution for his version of natural language processing and how he was inspired
*  by Jeff Hawkins' work, especially using sparse distributed representations, to represent how
*  brains code information. We talk about language as an extension of our own brains or really like an
*  extended growth of our brains and how the codes in our heads get externalized by us and internalized
*  by someone else and then coded back into essentially the same code in their brains. He lays out a bit
*  of the history of how people have tried to process language all the way up to our modern
*  big data deluge, why the deep learning approach isn't ideal for many of the applications that
*  are needed to work with language, and we walk through his semantic folding theory and how his
*  system actually processes language data to make it useful for all sorts of tasks and how this kind
*  of processing could compare with how brains do it. And Francisco shares ideas on how you, dear
*  listener, could start your own business using the principles of semantic folding theory. You can
*  learn more about his business at cortical.io where you can also play with some of the tools
*  that he's made and that we talked about. I have to apologize for the audio quality in this episode
*  because of technical issues I wasn't able to record with my normal setup so we had to use some
*  lesser third-party software with lower quality audio. So the sound itself isn't great. Plus,
*  I was working with editing one track between me and him and given the delay between me in the US
*  and Francisco in Austria, we ended up talking over each other plenty and there just isn't anything
*  I could do to fix it. Hopefully you can still enjoy our conversation despite that limitation
*  and my invariant limitation as myself. You can find the show notes at braininspired.co
*  slash podcast slash 31. Thank you to Felix, Michael, Sharika, Yu and Lee for contributing
*  to the show via Patreon. When our paths cross, I will buy you a coffee or a beer and we can
*  talk about reins and machines and how awesome you are for helping me run this show. And thanks
*  for listening guys. You are a wonderful and curious audience and I love bringing you excellent people
*  like Francisco to your ears wherever they may be. And here is Francisco de Salsa Weber.
*  Francisco, thanks for joining me and agreeing to teach me how our brains understand the language
*  today. Well, hello. Thanks for having me and I hope I can actually teach you something. So you're
*  the founder of a startup called Cortical.io. Cortical.io and this is actually your third
*  startup company that you founded. Is that right? Yes, absolutely. So I've entered the computer
*  science market if you want in the year 2000 after having worked in the Vienna General Hospital on
*  natural science. And since then, I have tried to innovate certain sectors that seems to be just
*  my way of looking at problems is to try and find a different solution. And I've worked in the in the
*  context of open source software. So this whole concept of collaboratively creating useful stuff
*  was sort of key for me at the time that moved over into what at the time was information retrieval.
*  I had a second company working on patent analytics and patent search as a specific topic. And that's
*  where I basically learned about the limitation of today's state of the art when it comes to properly
*  interpreting language. And yeah, that led me to Cortical.io.
*  Yeah, well, so this is interesting. And hopefully later, we'll have a few minutes just to talk about
*  founding startups in general, because usually here, you know, I'm talking to neuroscience
*  researchers. And so, so this will be a different interesting perspective. So let me see if I can
*  just summarize what Cortical.io does, and then you can take it from there and correct me. So
*  you guys have an approach to natural language processing that stems from the theories of Jeff
*  Hawkins about how our cortex in the brain processes information. And the goal is to be able to
*  process massive amounts of text that's being generated all the time, and to process it like
*  numbers are processed. So to be able to do computations with it. And we'll talk about how all
*  that happens in a few minutes. But then to be able to then you can feed the processed
*  information into the systems called hierarchical temporal memory systems made by Jeff
*  Hawkins team at Numenta. Is that an accurate kind of big picture description? And what would
*  you add?
*  Yes, absolutely. So the whole thing started, as I've mentioned before, by learning about the
*  limitations of our current way of handling text. And the one thing I've really learned is that
*  improvement happens in fraction of percentage steps in terms of precision for very specific
*  evaluation. So we are basically so far away from what we humans can do, that I said, okay, this
*  doesn't look like a continuous improvement kind of problem. I think that there is a much more
*  fundamental trick that works here. So the first observation is that to some degree, all current
*  methods and there are plenty because whenever you reach a ceiling, in a certain domain, you start
*  up trying a lot of different ways of doing things. But none of these actually came really beyond
*  the ceiling, that fictional ceiling. And so I said, okay, what other reference do we have? There
*  is only one reference implementation for that algorithm, let me call it like this, which is
*  actually the human brain. So anything that basically explains how the human brain works, should
*  give a good hint on what we should do in terms of language. And then the first impression is that
*  there is enormous amounts of explanations or concepts of what certain parts of the brain are
*  doing under certain conditions. But if you're not a super specialist yourself, it's just so much
*  light that you can't see anything. And so to me, the key moment was actually to first listen to
*  explanation of his approach. And the beauty of his approach is it gives you a conceptually
*  manageable system that allows you to zoom in and out depending on how well you do know the details.
*  But you can zoom in and out in the model and it stays down. And that was extremely impressive to
*  me because it allowed me to find, let's say the right level of resolution that I can cover. And
*  it allowed me to play through a certain number of things. And I just realized, okay, there are
*  many of the problems that I know from statistical modeling of language that could roughly be sort
*  of mapped to that kind of structure that Jeff describes. There was one key moment when I started
*  studying Jeff's materials, I was still not clear on what does it really mean. I mean, it was just
*  this gut feeling, if you want that, okay, that's the direction I should for some time follow to see
*  if something pops up. And then there was this moment when Jeff started to talk about sparse
*  distributed representations and how key they are to allow that whole simple, on the quotes, way of
*  explaining the computation of information. And he said that every information seems to be encoded
*  in such a sparse distributed representation, which we can detail out shortly. But that was the
*  moment when I had a shift of understanding. And I realized that it's not so important to look at the
*  algorithm first, it's first important to look at the representation. And that sort of change of
*  perspective changed everything. And from that, all the initials for our current approach started.
*  I feel like I've heard you mentioned that you had this sort of aha moment while you're in the shower,
*  is that right?
*  Yeah, I mean, it sounds pit a rest literally. But the key question at that point to me was, how can I
*  make two words that mean similar things look similar? Because you have when you think of neural
*  networks as being weight machines, to some degree, which they are not in the HM model, but that sort
*  of this basic intuition that people have today about that. And it's easily understandable if I have
*  100 degrees Celsius or 101 degrees Celsius, they are numerically close, and they are also similar in
*  how they behave. So there you have a sort of a natural proximity of similarity. But I don't know the
*  word car and truck, they don't show by any means similarity at the encoding level. We have to
*  convert this into something that makes sure that a truck looks similar like a car, because a truck
*  looks much similar to a car than it does to a tree, for example. So how do we do this in the first
*  place? And once we know how we do this, how can we automate this? Because I cannot start writing the
*  dictionary about everything in order to have this correct representation. And the third aspect to
*  this was the famous semantic grounding. So where does the link between the pointer or the label of
*  something and the actual representation of something? Where does that happen? And how does that
*  look like? These were the three starting questions.
*  Yeah, very good. I was talking to a friend just a few years ago, and he had gone from academia to
*  industry and had studied becoming a data scientist and had gone to one of these kind of boot camps or
*  whatever for becoming a data scientist, where they place you in a job afterwards. And he was telling
*  me, you know, there's been so much progress on so many facets in data science, but if natural
*  language processing is still lagging, and if you can solve that, then you're really on to something.
*  So this is, you know, exciting work that you're doing here. So I was actually my daughter was
*  talking to me the other day. And, well, first, she told me how much she loved me and what a great dad
*  I am, of course. But then she literally she said to me, like, learning how to read is hard. And, and
*  I thought, Oh, yeah, you know, I wish that I remember learning how to read as a young kid. And I
*  thought, Oh, yeah, language is hard. But then I sort of thought, Well, yeah, language is hard. But
*  you can also think of it as, you know, our easiest solution to communication, given our brain
*  constraints, you know, given that we likely process just about all the information coming in, we
*  likely process it in a similar way. And this is one of the insights that Jeff Hawkins had that, you
*  know, there are these repeating motifs across the cortex, which is severely limiting, actually. So in
*  a way, you can kind of think of language as maybe the easiest and dumbest solution for us to
*  communicate with each other. I don't know if you want to evolutionarily speak anyway, I don't know
*  if you want to
*  No, I absolutely agree. I mean, to me, it was an a high tech, when I realized, okay, there was some
*  point in time where evolution came up with a micro circuit that had a certain number of
*  characteristics, input and output. And the way how this micro circuit works, and it tried it out in
*  the mammalian brain for the first time, to basically lead to a situation that this would be one of the
*  most characteristic, if you want for a mammalian to some degree, to have this new cortex that sits
*  on top of all the older sort of parts of the brain. And the genius if you want is to find a small
*  circuit. So maybe in computer science, you could call it a flip flop, that does some basic
*  information processing within the realm of digital computing or within the realm of neuro
*  computing. And the algorithm was such that you get more processing power by just adding up those
*  modules. And then you just try to develop a body that can sustain as much as possible in the brain.
*  And then there is this sudden limitation, and it works well, because there is this one species that
*  has this super quick sort of growth period, and it works even out that you can get the babies to
*  come to basically give birth very early. So that the brain can even grow for some period after
*  birth. But then there is this limitation, the famous birth canal. So you cannot grow the head
*  endlessly for obvious reasons. So the only remaining way for getting more neuro tissue
*  surface in order to increase the computation is to basically do what we do today with the
*  processors, taking several processors and linking them up. And that link, in my understanding, is
*  language, because when I start thinking about the problem I have, I can also borrow the real state of
*  my neighbor's brain tissue for a moment by communicating my state of the brain, and having him
*  sort of use his brain with my state to hopefully deliver an aspect of the problem that is helpful
*  for me. And I think that this is the mechanism by which the whole social framework as being an
*  evolutionary advantage really got his, if you want, substrate or material manifestation in the first
*  place. I think that there is a direct link on that level.
*  Yeah.
*  That's such a, I mean, language is really such a beautiful thing when you really zoom out. And we
*  could just talk about that all day, I suppose. But, you know, but so we still don't really know. So I'm
*  not super up to speed on the current state of language in neuroscience. But I know we know areas in the
*  brain where language is processed. But we still don't know exactly how it's processed. So this is a
*  remaining question. And this is this is what you're essentially working on, even though you're not a
*  neuroscientist researcher.
*  Yeah. So, so in fact, language as such is in fact, externalization of the actual scene that's
*  happening. And the actual topic is more of a concept kind of topic here. So language is in fact,
*  just the Morse code we use to encode certain brain states. Yeah, that's the reason why we can afford
*  as a human society to have hundreds of languages, if not 1000, and still sort of work very similar
*  and even have more and more similar cultures. That shows that we might not share the same
*  externalization. So whenever we sort of get information out of our brain, it depends on where
*  we are and what our culture is. But what we are sending the payload is the same. I can speak to
*  someone in Australia. And by for example, pointing at the photo, we could both say yet these are, I
*  don't know, kangaroos. Yeah, and we have a not the same but a similar sort of conceptual model of the
*  kangaroos. And that allows us to exchange information on kangaroos. Yeah, if our brains would be fully
*  different, and a different language would mean a different representation of qualities, then we
*  could never ever communicate with someone across the language. And this is by the way, there is a
*  quite a lot of neuroscience that points in this direction, also indicating that the semantic part,
*  at least, so that the grounding of language uses the whole brain. It there are these quite famous
*  studies that the MIT from Hark as Al and in Carnegie Mellon from lots of course, that's okay. I give
*  it a point shortly, where they made fMRI pictures of humans who got a concept triggered. So they
*  either saw the word, a cat or they saw the image of a cat or they could hear the sound of a cat. In
*  the moment, when sort of the concept cat appeared, they make a photo basically of the brain activity.
*  And they found out that whenever the concept appears, they get photos that match to a very high
*  degree. So even such a high degree that they could train an algorithm to learn that correlation, and
*  to later on give it an unseen fMRI picture. And the system was properly predicting what concept
*  actually triggered it. And as if that would not be already scary to some degree. They could even
*  show that they could train the machine learning of the correlation of the concept with the picture
*  with one individual, and it could still pretty well predict the proper interpretation of another
*  individual. So this seems even to be similar over individuals. So this inner representation,
*  and that is basically the mechanism, I think, by which the brain works with information,
*  is that it basically makes snapshots situational data, it makes snapshots of experiences that we
*  have. And every snapshot just contains all the information that we get from all the sensors.
*  And that's how we learn about the world. But that's exactly the same way as we learn the language.
*  So it's based on a sufficient large, but still astonishing small number of examples,
*  we are capable of storing information about the language by the example. And if you do this,
*  what became then the semantic holding mechanism, namely by training the semantic space as a map,
*  and to use it to encode everything that you learn. That's the way how you make this link
*  between reality and the label, namely by snapshotting the overall experience that you had
*  with something that relates to this label. And that is sort of the origin of the distributed
*  representation. A cat is just the sum of all my encounters with cats with all senses. And
*  because that contains many interactions, if you look at two different individuals,
*  the two averages of a cat become more and more similar by default, because you have seen them in
*  all sorts of situations and contexts. And after 20 years, you have, I don't know, 250,000 experiences
*  of cat. And just by pure statistic, that is very similar to in average, of course, to the 250,000
*  cats that the boy in the neighbor buildings saw. And that's why we agree on what cats are,
*  because these averages have enough overlap between them.
*  So actually, let's, if we can, let's just back up and then and then we'll really get into the
*  semantic folding theory. And, and from now on, let's stop talking about cats, shall we? Why is
*  it always cats? I'm just kidding. We can stick with cats. That's a cultural, cultural tradition.
*  In Vienna as well? Or what? This is worldwide. Yeah. Oh, gosh. Although my example was even worse
*  because Australia and cats is a bad mixture anyway. They are not so much into cats over there,
*  because they don't use to have any. Yeah. That's right. We'll do kangaroos from now on. So,
*  but let's, let's talk just a little bit broadly about natural language processing. So, or NLP,
*  I could say. So the, I mean, the basic goal of NLP is, is to program computers to process
*  natural language data. Yeah. But I've heard you use the term natural language processing, but I've
*  also heard you use the term natural language understanding with respect to what you do. But
*  what can you kind of hash out the difference between natural language understanding and
*  processing? Yeah. So it's a, it's a quite a blurry line. Okay. Of course, I would say intuitively
*  natural language processing is a much more mechanistic procedure. Yeah. This starts with
*  things like taking some text out of a document and finding out or cutting out every single word.
*  So whenever there is a blank, you collect the word and you look for the next word. So that is
*  sort of one of the basic tasks that you do in terms of parsing a text before you don't parse
*  the text, you cannot do anything because you don't know what the text actually looks like. Yeah. Then
*  after parsing it, you might do things like finding out where are the nouns, where are the verbs.
*  You might want to reduce words from their polymorphism. You know, a verb can have many
*  different forms. A noun can be singular plural and so on. And you do stemming. Yeah. Interestingly,
*  these seemingly simple things, if you want to do them seriously, they end up being pretty hard.
*  So even something simple like sort of cutting out words of a text, you happen to find a word
*  like New York. You don't want this to be the word new and the word York. You want this to be the
*  word New York. The president of the national committee should be the president of the national
*  committee and so on. And if you try to do this fully automated, you will just realize that there
*  is a billion of variants out there for what could be parsed and what could be considered and so on.
*  So these parsers, even although they are doing a fundamental and simple thing, they reach a point
*  where there is no simple statistical rule that they can apply, but they have to bring in special
*  information. And that's traditionally, so people try to do this over the 80s and 90s and try to do
*  this with expert systems by having linguists type in all sorts of metadata and so on. But this was a
*  sisyphus work. I mean, it was never ending. And so it's found on the very specific solutions that
*  could be implemented like this. Most of the possible solutions were just not economic enough
*  to be practically built. So people then started to use statistical methods and they started to build
*  statistical language models. So a mathematical creature that for certain parameters behaves
*  like a language expert system. And so then they started to build parsers of all sorts that use
*  those language models to make educated guesses of the word fire in this position. Is this a verb or
*  is this a noun? And that again improved things. And then at some point, there was again this ceiling
*  and nobody could come up with a language model that really improved things. And that is what is
*  an indicator to me that we are just missing out an essential aspect here, or that the whole strategy
*  of doing a mechanistic language modeling will not help us. And then in the latest years, there was
*  this explosion of text so that even the statistical approaches could not be applied in such an easy way
*  to the text anymore. So there was this race between how efficient is my algorithm while being
*  of a certain quality and how much data can I process in a second. And so we have today situations
*  that if you would say I want to collect all the global tweets about mobile phones,
*  not even Twitter themselves could solve this because it's just not economic doing this.
*  I know that there are, I mean so deep learning is all the rage right now. And I know that there are
*  plenty of deep learning systems using recurrent neural networks and stuff to approach NLP. And
*  what you do is not deep learning. And I'm not sure if it's the right time now to compare the deep
*  learning approach with what you do without having already spoken about what you do. But maybe you
*  could just talk for a second about maybe why deep learning approaches are insufficient for NLP. And
*  then we can really get into semantic folding theory. Yeah, so basically the immediate
*  limitation for let me say commercial purposes is the fact that the sheer amount of data
*  that you need to train a deep learning system is not always available. And this is a very
*  optimistic view of the things. I would say that the more interesting a case comes, the less data
*  you have that allows you to train it, especially in the language domain. Because that companies
*  like Google and Facebook, they have an easy life doing deep learning because first of all, they do
*  that on their own data and they have endless amounts of this data. But this is only very,
*  while the companies are very big and impressive and everything, but they only cover a tiny
*  slice of reality. Yeah, I mean, yeah, that's, that's another thing. So I'm, of course,
*  not entitled to talk about the relevance of the data, but I'm just scientifically talk about the
*  amount of data here. Nevertheless, I mean, if you want to use deep learning to find out about some
*  inside deal communicated via email, and you tell the compliance officer, yeah, if you give me 10,000
*  of those emails to train, I find you every inside deal, there would be no bank having,
*  having 10,000 of these emails that will still be alive. So there will never be, even if
*  computers become super efficient, and there is only one bank, one big bank left, even that big
*  bank will not have enough data to train this. And the problem is that deep learning trains models
*  on the actual payload data. So if you want to filter emails, where you need to have special
*  attention for some reason, you have to train the system on, I don't know, 1000s and 1000s
*  of these emails. And each of the emails for training purposes has to have a marker saying
*  if that is an interesting or non interesting email. And if you have enough of this, and of course,
*  first of all, you need the emails. And secondly, you have to annotate them, as we say, for what
*  they stand. And only then you can train a classifier. That's probably if you have enough data,
*  and if the class that you want to filter out is really a useful class, big chances are that you
*  will do a good job. But if you now say I want to have also all emails where people complain about
*  something, you have to start all over, you have to find your 50,000 complaint emails, you have to
*  annotate them again, and you have to train another model. And that's what I strategy that I call the
*  billion model universe. Because this tries to map 100,000 objects, and ends up with a billion of
*  models that model that represent those 100,000 objects. And this is simply not efficient. And
*  if we have learned something is that evolution doesn't tolerate anything that is not efficient,
*  this gets immediately eliminated. Yeah. Yeah. So that was the reason why we said we have to find
*  a different way. And this different way was precisely to find out that the representation
*  was actually the key. And once you've got the right representation, the algorithm
*  literally becomes trivial to some degree. It has to be trivial because computation wise, neurons
*  are trivial. So anything that contains cosine and integrals, and I don't know what is definitely
*  far beyond what a neuron could ever process. The neuron can in the end of the day fire or not fire,
*  most of the time. So the representation has to be able and supportive.
*  Well, yeah. So let's talk about how we get to that representation. So you have a paper online
*  available that describes and walks through a bunch of all the details and examples of your
*  semantic folding theory. So I had Jeff Hawkins on the show a while back, actually. And we talked a
*  little bit about the hierarchical temporal memory that he has developed. But we mostly actually
*  talked about his more recent theory about how each cortical column encodes essentially an entire
*  object. But anyway, one of the principles of his approach to how the cortex works, like we already
*  said, is that these repeating cortical columns are all performing the same computation on data that's
*  coming in and making predictions. I wonder if you could just talk about what else might be useful
*  background information on HTM, hierarchical temporal memory, for us to proceed then with
*  semantic folding theory. And if you need to get in the shower to do this, that's okay.
*  No, I've done this once. This usually should be enough. Yeah, so that's precisely the point. So
*  every cortical column stands for an object or for some real world information. This could be,
*  let's say, the pixel in your retina in a given context. This can be, I don't know,
*  for a certain shape of a nose and so on, depending on where in the hierarchy you are. But what is
*  common to all these columns is they have a link to something real in the sense that it is data that
*  originates from the senses. There is no other source of data. Even if it's data that comes from
*  other regions, if you trace back the initial sort of trigger of these region jump was definitely
*  somewhere in the senses. And this is what I call the special case information that I have.
*  A given moment, basically. And this is also very different from all sorts of statistical representations
*  where one feature is the weight of the neuron branch 300,058 to the neuron 8,370. But nobody has
*  a clue what this figure that is stored in there as a weight, how that relates to anything. And that
*  is one of the big problems why you cannot really debug a deep learning network. You can just try
*  out playing around with parameters. But if you happen to have even just 15 parameters, you could
*  easily last the rest of the universe a lifetime to actually find the optimum configuration.
*  So this is again, although it might be mathematically correct that at some point
*  the system will converge. But if that is after the next big bang, then that's not valuable or
*  useful information. And especially what actually you need to do is to flee a sawtooth tiger that is
*  coming after you. You have to have a strategy that allows you to say whatever the answer to my question
*  will be, it needs to be here in, I don't know, 30 milliseconds. Otherwise, it's not worth it.
*  And in Stone Age, if you want, that was a key feature of the algorithm. I mean, there were just
*  nearly everything outside of yourself was dangerous to some degree. And how can you do this?
*  How can you arrange information in that way? And the way how semantic folding is doing this
*  is by having a two separate processes. One is a process where the sensorial input is projected
*  onto a map in a way that sensors triggering in the same time, start aggregating on the map,
*  they start building clusters. And, and I think that there is a lot of parallel findings that we have
*  neuroscience, for example, this famous big pruning could precisely be a mechanism where after an
*  influence, an inflational link up between the neurons starts by default, which would be a
*  pretty simple mechanism that could be something that is triggered by some gene or something.
*  And then only the ones that have, let's say the lowest, the lowest trigger levels to fire
*  are the ones that remain because they have been used sufficiently enough. And all the synapses
*  that have not been used. And if a neuron has no useful synapse, then the whole neuron might just
*  get eliminated. Are you talking about pruning as in when we late in our teenage years?
*  The two year, the year old pruning. Yeah. So this is a literal organic pruning mechanism.
*  And the point is that if you allow the environment to change the morphology of how the feature bits
*  of your sensors are arranged, what happens is that you end up with an arrangement of your sensor bits
*  that somehow capture the semantics of the world plus the semantics of your sensors.
*  Because that's the baby doesn't get a lot of information in the beginning from the world
*  because everything is blurry. But that's the moment when the basic organic map is drawn,
*  because the auricular nerve looks in a certain way in a human and the optical nerve looks in
*  a certain way. And the system has to be initialized with this topological setup of all these nerve
*  ending. And then it's by exposing the sensors to actual data that there is sort of a refinement
*  of that map until bits that contain similar information, because they are triggered in
*  similar moments, they get close together. And it's very obvious for that reason that,
*  for example, the optical nerve creates a close to one to one projection in the first optical layer,
*  because by default, a sort of bitwise organized retina, two bits that are next to each other
*  typically get triggered at the same time with the same color, because they come from the same
*  object in the external world. And therefore, that's the reason why the optical system,
*  you can literally map what the person sees. But with the acoustic system that is more
*  sophisticated by splitting up the frequencies and so on, it looks more chaotic. If you want,
*  if you look at the first projection layer in the brain, but still the principle, I think,
*  is the same, that you encode the actual perception based on a topology that stems from all the sum
*  of all the previous experiences. And that's adoption of morphology seems to slow down,
*  because sometimes you reach your stable semantic understanding of the world. And then only the
*  pattern remains interesting. Whereas in a younger brain, if the pattern is extraordinary enough,
*  it might still influence the way how you capture information. So to me, this fits quite well with
*  what we experience. And the practical way how we implemented this, and that's where you see why
*  computer science is so nice, is because you can literally always simplify pragmatically everything.
*  It is that we take some text, and we declare this text to be the reference about a specific language.
*  So if I want to create a system that understands medical records, in reading medical records,
*  I have to teach the semantic system the language of medicine, because all the
*  existing knowledge that we have of the world about medicine is encoded using the language of medicine.
*  So I have to first do the same as I would do with the human. I teach you the language. So you go to
*  school, you go to high school, you go to university, and after a number of years, you understand,
*  let's say, 70% of the typical language that doctors use when they talk to each other.
*  And once you have reached that point, although you might have never seen a medical record,
*  but you will be able to look at it and make some sense out of it. And that is the difference.
*  A deep learning approach would have been to collect 500,000 medical records and to train
*  my model on those. That is, if you want, the big difference, because with our language model,
*  I can then take diagnostic records and I can do the same. I can understand them and I can
*  differentiate them because I know the language in which they are formulated. And the basic unit
*  that your system works on is a word, right? Yeah. So these words get coded as a sparse distributed
*  representation. And maybe you can just talk about what a sparse distributed representation is
*  in the context of a word. And then we can just kind of walk through the way your system processes
*  the data. Yeah. Yeah. So the sparse distributed representation is basically a binary vector,
*  very large in size. So we, for example, work with a vector that has 16,300-something
*  bits behind each other, but this is ridiculously small of what you would expect in the brain.
*  We probably speak of millions and hundreds of millions or whatever of one representation.
*  And the way it works is that every bit in this representation stands for a fact in the world,
*  in the end, coming in from the census. So it is traceable by default, what it means.
*  And you have a sparsity, which means only a very small number of the possible positions have ones
*  and most of it has zeros. And the interesting thing is that there is a mathematical proof
*  saying that these sparse vectors have certain properties. And as it turned out for us,
*  one of the most important properties is that you can aggregate them, which basically means you can
*  add them together. So you can take 10 different strings, each 16,000 bits long, with a small
*  number of ones scattered along this string. And if you now scatter, so whenever one of them has a one
*  in a position, you make a one in the target. The interesting thing is that with the resulting
*  representation, you cannot calculate back how the original 10 strings have looked like,
*  but you can calculate the degree in which an arbitrary string could be member. So you can
*  interpret the viability of the match between a string with a given pattern. And interestingly,
*  you can close to endlessly aggregate those sparse representations without actually losing
*  information. What happens in language, for example, is that you get a more and more higher level
*  view on the thing. So if I make, we call the sparse distributed representations, we call them
*  semantic fingerprints, because it's easier to pronounce. So I can add the semantic fingerprints
*  of a sentence together. I can add the fingerprints of all the words in a paragraph, in a document,
*  even in a book or even in a library. The point is that the representation will be always correct
*  in terms of topics of how important certain topics are, but it will be more and more
*  large scale view of the thing. And making a fingerprint of a library would allow me to say
*  for an unseen book, how well it fits in this kind of library. And what I now want to explain is
*  how we actually sort of compute the fingerprints. So as I said, we train from reference material. So
*  in order to stick with our virtual medical students, let's say we bring together all the
*  textbooks and reference books that a human would need to become, let's say, a medical doctor.
*  So you might end up, let's say with some hundred books that you have to read and learn as a human.
*  And I extract the text from there. And then I slice the text down to sentence level. And with
*  every sentence, I also remember the paragraph it was in. I remember the last title, the super title,
*  and even the book title if you want, that because all of those titles are with textbooks,
*  typically, and with reference materials, they are structured in a way to give you the, if you want,
*  ontology reference to this specific concept that is captured in a specific sentence.
*  And you now take all these words that you have in this hierarchy of titles plus the sentence
*  in the end. And that becomes a special case experience of a basic unit of language.
*  So the basic unit that has meaning, that can have meaning is a word. And of course,
*  there's, again, it's a blurry line, but in general, a word is, let me say,
*  sort of the smallest entity that means something. Yeah. And then those words are taken
*  to formulate specific claims or information units. And that's the reason why we have structure in the
*  language, why we have sentences, why we have paragraphs, and so on. And that, in fact,
*  the implicit or the explicit representation of the implicit order that that information has in the
*  author's brain. And when he wants someone else to properly understand this, he has, of course,
*  not only to carry the information as such, but also, to some degree, the structure. And that's
*  why we read out the reference information in that way. So let's say we started with 100 books,
*  and we now have a million of these small snippets containing the words of it. And now we simulate
*  what in the biological brain happens by sort of moving the order of the sensory bits around.
*  In biology, this might happen either while the nerve grows or while the nerve operates
*  in early stages, is that we arrange the snippets and then we use machine learning. And that's the
*  only actual machine learning step that is in semantic coding is to arrange the snippets on a
*  given space. So we define the space as being a metric space of 128 times 128. Could be anything
*  else? Yeah, I was going to ask why. So the semantic fingerprint is a little over 16,000
*  binary units, and that is 128 by 128. So I'm just curious how you settled on that number.
*  First of all, the obvious is it should be a power of two to be efficiently
*  implementable. And the specific size, so why isn't it 64 times 64 versus why isn't it 256 times 256,
*  is purely the ratio of how useful is the given resolution, how well can I separate
*  two things that are separate while making sure that things that are similar still overlap.
*  So it's basically like when you have a light microscope, you have to know what lenses you
*  use to know what color the light has to be that goes through it. If you send the wrong
*  spectrum of the light to the light microscope, you might see a blurry
*  picture. So you have to match those two parameters. And here in the semantics,
*  it's also I have to make sure that I can discriminate two sentences in the sense of,
*  yes, they are both diagnosis sentences of a medical record, but this is one diagnosis,
*  and that is another. And if I have too low semantic resolution, I could just say that both
*  are diagnosis, but I cannot say if they are similar or not as diagnosis. And we have,
*  I have to say we have done this basically by trial and error. And that has proven to be sort of the
*  zero degrees Celsius if you want. It doesn't have anything to do with a theory about
*  how the brain might encode the information. It's more of a computational issue.
*  Yeah, this is a computational issue. The fact that this is a two dimensional extent,
*  of course, has to do with the fact that the brain or the neocortex is a two dimensional structure,
*  and something that feeds into a two dimensional structure transmitting a topology has to be
*  two dimensional at least. It could be three dimensional, but that again would be,
*  you wouldn't become better. Things would just get more complicated to compute. So again,
*  efficiencies, kink, that is the smallest dimensionality where you can work with a
*  two dimensional pattern of computer inputs that you have at the neocortex level.
*  Well, sorry, sorry, I interrupted you there. So you had the text, you break it up into these snippets,
*  and then the snippets get broken down. Arrange the snippets on my space of 128,
*  so 16,000 positions in a way that snippets containing similar words stay proportionally
*  close to each other. And snippets with fewer similar words stay proportionally far apart.
*  And that's the machine learning step, right?
*  Exactly. Because that's an optimization thing. You correct the error a little, you re-compute it,
*  you correct the error a little until the improvement is so small that you say,
*  okay, that's good enough for my purpose. Practically, it takes us about two hours
*  to compute that mapping thing. So it's a reasonable amount of time, not five days,
*  because that could already change how you do real world stuff. If every time you need to compute this
*  takes five days, you have other problems. Yeah. So once we have computed that map, that distribution,
*  which is a total projection of the set of examples that you chose for reference. So that,
*  again, the same as for humans, depending on who the teachers are, and what you have written into
*  the school books, that's what the kids will internalize. Yeah. So if it's medicine, it will
*  be the medicine understanding. If it's a law text, it will be legal understanding and so on.
*  It even is true for different languages. So you can do this in German, French, English.
*  We have done it for Chinese, Arabic, Russian. So even if the whole writing logic is different,
*  this still works. In fact, the only thing that you need is the notion of there is a grammar
*  behind the use of the word string. Even if I don't know the grammar, that just needs to be a grammar,
*  which means the strings depend on each other. So in Chinese, you have the whole word, basically,
*  or sign that depends on the other signs. In English, this word depends on all the other words
*  in the sentence, because there is a grammar structure that says how to build sentences.
*  And that interdependence, so that every word depends on all the other words in all ways,
*  in the way how the declination works, in the way how the polymorphism works,
*  in the way how you make it plural. All of that is influenced by all the other parts of the same
*  language. And this is, per definition, a semantic universe. And if I now take a smart set of examples,
*  and our schooling of kids is basically exposing them to the world, but making a simulation that
*  is much smarter, that allows them in quite short time, understand stuff that it took us
*  maybe 1000 years to understand. So there is this sort of improvement of this teaching.
*  And the same strategy is basically when we have what we typically call the subject matter experts,
*  who choose the reference material for the domain. And I keep telling them, choose the books that you
*  would want a new employee to read first. Those are the books that are key to capturing the essence
*  of your domain. And what we do as a next step, this is sort of the first step was the building
*  of the semantic map. And the second step is that we make a word list. So we make a long list of
*  all the words that occur in my reference, and I take every word only once. So let's say I end up
*  with 100,000 distinct words. And for each word, I can now say in what snippet is this word appearing.
*  And because I have a coordinate position associated with each snippet, due to the map,
*  I have now the set of all snippets that contain the word, give me this distributed pattern of bits
*  that go on. Sorry, I should say that, you know, it's hard in an audio podcast,
*  you can visualize and you show this in talks and in your papers that, you know, this 128 by 128
*  square pattern, where a word is then represented, if it appears in 12 snippets, you flip those 12
*  bits on if I'm not mistaken, and then it gives this colored pattern of what a word, how a word
*  is represented in this space. So exactly what this characteristic is that this bit pattern is very
*  sparse. So the vast majority is white, and only in our case, we take about 2% as the upper limit
*  is used. And the incredible thing is, although we have this tiny little space of 16,000 positions,
*  we can encode enormous amounts of information without needing more space. And that is,
*  from a biological point of view, exactly what we need, because the one thing that we can be sure of
*  is that we cannot grow the brain. So if we want to have memory space for 50, 60, 80 years of life,
*  there is a lot of information to store. So the representation has to be done in a way that it
*  stays relevant. So recent information has to be sort of more important to some degree
*  as ancient information. But we still have to sort of feel the ancient information because otherwise,
*  our predictions will be bad. Yeah. And so that is a big problem. Yeah, because we in computer science,
*  when you run out of memory, you go and buy new chips, or you put the new computer next to it,
*  or whatever. But that's not the way nature could do this. Yeah. So I find it quite impressive how
*  the biological constraints sort of pointed into a completely different way of doing things. So
*  by introducing a pattern, a topology, and we find a lot of topologies in the neocortex, the whole
*  concept of having the regions of stuff is in the end topological. So topology seems to be one of the
*  principles to the neocortex, I would even say. In my own research even, I recorded neurons in a brain
*  region called the frontal eye field. It's partly responsible for making our eyes move, making eye
*  movements. And in this region, just another topology, as you move your electrode down through
*  the region across the cortex, essentially, you can stimulate, microstimulate it and induce eye
*  movements. And there is a topology because as you go down a little bit further, the eye movement
*  changes direction smoothly and changes, changes, changes direction and changes the distance. So
*  yeah, there are these topologies all over the place. And so what you're talking about then is
*  a semantic topology, essentially. Yeah. To be honest, I think that language is just a
*  nicely interpretable set of, or aspect. But I think one thing that is key to Jeff's theory
*  is that every part of the neocortex does fundamentally the same thing. So if that is the
*  way how we assimilate and handle language, basically everything else is supposed to work in
*  a similar way. Because there is precisely not a module A that does this kind of computation and
*  the module B that does some other kind of computation. They have slight differences,
*  but I've been told that it's even hard to discriminate the neocortex of a mouse versus
*  the one of a human. So similar they are. Humans is a little bit larger, actually.
*  Yeah. So you have these semantic fingerprints is what you end up with. Each word has a semantic
*  fingerprint. And then as you say, because they're so sparsely populated, you can then do all sorts
*  of computations with other words to form sentences as you were talking about earlier. Exactly.
*  And the main computation that you do on these is a similarity computation. I don't know if you want
*  to discuss that a little bit. Yeah. So there are two things. There is one thing is that they can
*  literally apply Boolean operators to these fingerprint representations. And the Boolean
*  operators on the bit directly correspond to a semantic function in the sense of the representation.
*  So if I take the fingerprint of Jaguar, so I assume that I have learned, I forgot to say this,
*  I assume that I have learned the language space with Wikipedia, which is some sort of college
*  student knows everything sort of reality. And you now convert the word Jaguar into a fingerprint,
*  and you convert the word Porsche into a fingerprint. The first thing you will see is that
*  they are at least in certain regions very similar, precisely in the region where the bit
*  stands in context that has to do to cars, for example, or even to sport cars, let's say.
*  So if you take now the Jaguar fingerprint and you subtract all the bits that are in common
*  between Porsche and Jaguar, so the overlap between Porsche and Jaguar, and you take away
*  wherever they actually overlap, what you get is a fingerprint where the closest word to it is the
*  word tiger. And it is the word tiger because a Jaguar could be either a car or it could be a big
*  cat. If you take away every hint that points to a big car, what remains is a fingerprint that
*  looks similar like the fingerprint of the word tiger. That is this mechanism that, for example,
*  an example I usually give is the word organ that in English is ambiguous again. And if I use it
*  in the sentence, organs and pianos are musical instruments, the region about organ being a
*  biological structure will not be strengthened when I add them up by any other word because the
*  word musical and piano, they are all not ambiguous with that part. Only the word organ has this
*  ambiguity. So if I do my aggregation, and then of course I have to sparsify the results back to the
*  2%, all the bits relating to organ like liver and lung will be eliminated because they haven't been
*  strong enough in the aggregation. And what happens here is basically with probably the
*  computationally most simple mechanism by sort of anding and oring together binary structures,
*  I can computationally disambiguate the word organ because no human will ever have a problem in
*  right away perfectly understanding what the sentence means without even thinking on
*  liver or lung. And this used to be in the traditional NLP space, this used to be one of
*  the big holy problems on how to computationally without using lookup, of course, in a dictionary,
*  how could I ever computationally disambiguate anything? On the other hand, so why this is so
*  effortless for humans, I think becomes perfectly clear if you see that the sheer aggregation,
*  so the sheer representation of a sentence already implicitly disambiguate all the contained words
*  without needing any extra computation. So again, it's all about efficiency. And why would there be
*  ambiguity in the first place, of course, in order to allow you to reuse the same word
*  for several things? Because it's more efficient to only need 10,000 words as an adult part of the
*  society than meeting, I don't know, a million words in all the flavors. And in order to sort of be
*  memory efficient, and by again, using this very little space of 128 times 128, you can even pack
*  multiple meanings per word without losing anything. If you make the math of so 2% that we typically
*  use for a fingerprint are about 320 or so bits that we use at the given point out of the 16,300.
*  If you make the math on in how many ways can I select 300 out of 16,000 bits,
*  you get it's a factorial number. So you end up with atoms in the known universe or something
*  of that order. I mean, probably I exaggerate, but it's a huge combinatorial space just on this little
*  tiny patch of 16,000 bits. And the computations that you do, just the simple subtraction, addition,
*  and comparison, it's so beautiful and clean. Something a new one can actually make.
*  Right, right, right. I don't know how you actually came to the semantic fingerprint,
*  but I'm imagining a time where you realized what you had and then I'm wondering what that felt
*  like to you. Yeah, I mean, to be honest, I read the first time about neural networks
*  when I was in school in the in the late 90s. And I don't know, I was fascinated by having a
*  programmable process, find out something I mean, this whole, I mean, that the computer could add
*  to numbers or multiply to numbers, this was trivial, even then, but to get something complex,
*  where you just do a little bit of sampling, and then the system would find out something that you
*  could never find out because it's too complicated. That was fascinating me. But one of the first
*  stopping points I saw is precisely language. So if and then I had a very naive approach to this. But
*  if you would encode characters into ASCII codes, and you would feed your ASCII codes into a neural
*  network, it would take forever to even even understand what Peter Pan is. Yeah. So this is
*  really so I said, okay, this is impossible. A human kid, he hears a word one time, maybe two times,
*  and then you hear him already using this word properly. Yeah. So that cannot be the right way.
*  And so for me, already then was the question, okay, all of that is nice, but how do I feed
*  text into this? I mean, numbers is obvious. If two numbers are close, they tend to represent
*  something that relates or that is similar. So but how is an A similar to a B? Yeah. What is?
*  And then I did not know about things like representation. Interestingly, in retrospective,
*  when searching for an answer myself, I found myself in papers of the 80s and the early 90s.
*  And those were more philosophical ideas about things like data representation and so on,
*  which I found extremely useful. I mean, there is this book from Douglas Hospital that talks about
*  the whole thinking process is just making analogies between things. Yeah. And it's very
*  sound how he explains this also, when he says things like the word cat again, is not in reality,
*  it's not a word, but it's a label of a class. It's the class of all experiences that are sort of
*  catty. Yeah, that becomes the word cat. And he basically does a pure
*  semantic explanation of it. And I wonder what he would say about our way of representing of
*  capturing this. So yeah, maybe one day, I managed to have a conversation with him on that. But I
*  think it beautifully matches this whole conceptual framework he built where thinking is a computation
*  analogies. And interestingly, you can explain a lot of human capabilities and particularities
*  also that are founded basically on this analogy making approach. I'll have to have them on the
*  show. And maybe both at the same time. Yeah. That would be an honor. Okay, so I mean, you run a
*  business, right? So we've been talking about all the technology and how cool it is. But what do you
*  use this stuff for? Yeah, so it's a very basic functionality. So by nature of things, you can
*  apply it to many different things, which is a is fantastic, but it's a pain also, because it's,
*  it's, I mean, if you have a Swiss knife in your pocket, you have this tendency of taking care of
*  every problem that crosses your, your way. Because yeah, I can do this, and they can do that. And so
*  it at some point, it actually needs a lot of discipline in kind of keeping a business focus.
*  The point that I would make in general is our strength is not even that, how would you say,
*  our results would be sort of have a higher precision or so I mean, all this machine learning
*  induced a lot of discussions about precision. And if people know it even a bit better, they might
*  even talk about recall and things like that. But in my experience, you create business value, if you
*  are more efficient. And that is the same parameter that evolution uses. So we have won a number of
*  competitions, not necessarily because we had a 0.1% higher precision, but because we could
*  demonstrate maybe in three weeks, that we could reasonably well address and maybe indicate the
*  solution of a problem where others have not even started training the models properly.
*  And this turns out to be the key factor. Because from my perspective, and I meet a lot of
*  large enterprises in Europe, in the US, they all have, I mean, I wouldn't call it, but I showed
*  trivial problems to some degree. I mean, problems like I'm getting 500,000 emails a day. And I know
*  that 60% of them don't need to be addressed. But they cannot filter them out. So a lot of people
*  have to read these emails every day to make sure that we don't miss anything important.
*  And I mean, you have companies out there talking about self-driving cars of, I don't know,
*  automated DNA insertion in cells. And I don't know what, but we have not yet made a system
*  that is capable of doing what a 10-year-old probably could do. And again, not because there
*  are not methods of doing this. There are plenty of existing NLP approaches that could help you.
*  But you will simply not be able in a real world context to build such a system with a reasonable
*  efficiency. So you will not find anyone paying you the money it would cost to implement this
*  properly. That is the big problem. So how's business?
*  Yeah, so there is the other part. Being small, I would say even very small, and successful,
*  is also complicated, if you want. You don't need to answer the question,
*  if you don't want to. No, no, it's in fact business is good. It took a while because
*  Will teaches you that selling the first car that runs on water is just a hard sell.
*  As you might not think, but it's a hard sell. And we had a certain lucky strike in the sense that
*  because AI is booming, big companies are making efforts in sort of being part of that AI thingy.
*  So it's much easier, I would say, for a small company out of Austria to get the attention of
*  some of the big players than it would have been 10 years ago, where probably we would not have
*  tens of the number of customers to even talk to. Because they would say,
*  I have a fax machine, what do you want? So business is good, but especially if things are moving
*  and moving so fast, you just have to be careful to make the real good business decisions, basically,
*  within this. I should also say that you guys, if you go to cortical.io, you guys make available
*  toys to play with, to try out the technology. Absolutely. So I'll point people there in the
*  show notes, of course, and then you can also see examples of these. You probably think they're
*  beautiful. I think they're beautiful, these semantic fingerprints, right? I know you've
*  looked at a lot of them. Yeah, I mean, it's fascinating. I remember in the early days,
*  some five years ago, I happened to talk once to an investor and he saw this fingerprint and he said,
*  do your users need to look at this in order to use your software? And I said, no, no, no,
*  this is just a rendering so that you have some sort of feeling on what this would be or so.
*  And funny enough, it turns out that one of our applications that we created is a search engine,
*  by the way. And it turned out that people love to see the fingerprint of your query and the
*  fingerprint of a result that you have found and see where do they actually overlap, which is,
*  why has this document be actually selected? And it turned out that this fingerprint
*  representation is a super intuitive one, especially as you can move your mouse over the dots.
*  And for each dot, you have a pop up with the local keywords that you have in this area. So you can
*  literally take a magnifying glass and try to figure out why has this document been selected.
*  That's so cool. I just realized you could probably teach yourself to read
*  looking at these fingerprints, right? Yeah. Yeah. Yeah. And if you like me,
*  stare a lot into this, I think I have already adapted certain circuits in my brain that can
*  sort of in depth, more in depth, at least decipher what the fingerprint represents.
*  So it's really, and it shows how well this matches with the way how the brain wants to
*  process. So I think that, yeah. I have dreams. So I used to work at a grocery store and check
*  out groceries. And to this day, I still have dreams where I'll see like a banana floating across,
*  and then the number 11 will show up because bananas, the code for bananas was 11. So do you
*  see these fingerprints in your dreams? Absolutely. And it's not just as the fingerprint, but
*  I literally sit with a customer talking on a maybe new use case that I haven't thought through yet.
*  And I can literally by mentally arranging those fingerprints, figure out what would be the right
*  strategy in sort of solving that. And what is so scary is that very often, this first naive
*  thought, yeah, so like, like I said before, the Jaguar minus Porsche equals tiger, yeah.
*  This was initially, this was sort of a joke, wouldn't it be funny if you could do this?
*  And then I tried it out with a fingerprint, and it worked literally. And that is the fascinating
*  aspect is that you don't need some obscure complex algebra, basically, that doesn't tell
*  you anything. And you just hope by the end of the computation that you get something useful.
*  Here, you can literally try out every single step, you can read it, you can see what would that
*  give if I overlapped an example of an animal with an example of a car, I would see, I don't know,
*  30% of the cars having a strong overlap because the marketing department of the cars keep making
*  links to some animals between the car and the animal. And you can sort of verify these kinds of
*  things within seconds, if you're interested. It's really cool work. And it's really exciting. And
*  like I said, I'll point people who want to learn more to your paper. And there's a you give a video
*  lecture online that I can on YouTube that I can point to. So like I said, I had Jeff Hawkins on
*  the show. And he's, you know, obviously, I know you agree with this, that he's done some really
*  nice work, theoretical work. But he's, he's actually a little controversial in the neuroscience
*  community. You know, he's really also lauded by a lot of the nurse community. So it's not really
*  that much controversy. But I'm wondering if you've had any reactions or, you know, back and forth
*  with any people in the neuroscience community about what they think to about your approach and,
*  and just the AI community as well, like how how people are reacting to your work here?
*  Yeah, I mean, I have not that much contact to the real neuro community. I, from time to time,
*  I like to join some conferences. But I can say that the effect that Jeff sees in the neuroscience
*  community, I do see that in the machine learning slash AI community, really is that there is always
*  a majority. And this majority, if that majority not happens not to have the sort of best approach,
*  it's incredibly sort of hard to keep up with the world that basically doesn't want to be changed.
*  It's literally as you have to demonstrate a certain amount of persistence until the
*  world decides to sort of give you a chance. This is a very interesting phenomenon. Because it makes
*  sense. It also makes sense because you don't want to have a captain who with every wave
*  rushes in one extreme direction. I mean, everybody will get seasick. So I perfectly understand that
*  there needs to be a fundamental conservativism in order to allow this whole incremental improvement.
*  But if you see this from the personal perspective on what it takes, and how much you need to
*  do sort of endless repetitions of what you say you have to allow enough discussions with people who
*  have a different opinion. Yeah, so I can really relate. And I think that Jeff had some of these
*  experiences also in his domain. And that's just what it takes to do some structural changes. I
*  think this is characteristic to more structural changes. Yeah, so Sam Gershman, his advice to
*  people getting started in their careers was that you have to be willing to swim upstream and go
*  against the grain and keep your head down. And even though the majority maybe doesn't agree with
*  you, you have to forge ahead. So I think that this is the same lesson that you're communicating.
*  You wouldn't think this in the beginning, at least I didn't. You actually have to expose yourself.
*  Because although it costs energy to constantly argue and come up with arguments, but that is in
*  the end, the best way of refining the structural change that you might have discovered. I mean,
*  the way how I looked at semantic fingerprints four years ago, today, I look back and think,
*  my God, was I my ease. By exposing or allowing a certain degree of sustainable discussion,
*  it also matured myself. So it helped me as thinking and refining things and also abolishing
*  certain aspects. I mean, for example, in the beginning, I thought that we might want now to
*  apply a lot of the visual computation. So there are a lot of algorithms
*  in working with images and so on. And my first intuition was, we can use all of these
*  different visual filters and stuff until I find out they are not applicable. You really want to
*  stick with Boolean operators. So yeah, it has always two sides.
*  Well, yeah, I mean, in my own experience, of course, I like to use coding as an example,
*  because you're starting to learn how to code like computers in whatever language. And then
*  you code for about a year and then you look back and think, oh, man, I was awful. But now I'm good.
*  And then the next year, you look back and think, oh, it never ends.
*  Absolutely. Yeah, yeah, yeah. I can perfectly relate to this.
*  Do you think that deep learning, which is all the rage right now, do you think that it's overblown?
*  Yes and no. I think that it was good to have something like deep learning, because it allowed
*  to, for example, give data it's right. I mean, 15 years ago, nobody was talking or philosophizing
*  about data. Everybody was talking about processing. So this whole aspect that processing also has a
*  lot to do with data. The whole fact that there is now job description like data scientists,
*  data scientists in the 80s would have been someone who types in some paper records or so.
*  It has been data scientists. So I do think that there is a social reason, a good social reason,
*  why this is there. On the other hand, you have especially the more advanced people in the domain.
*  But I hear more and more criticisms or descriptions of limitations of the approach,
*  which I think is good also because it's not only good to learn of a problem, but it's also to
*  start a more sort of continuous process. On the other hand, I don't expect deep learning
*  to ever solve some of the real problems. So I mean, it might sound extreme, but I
*  don't think that current deep learning will be the method for getting self-driving cars.
*  It will be good for getting very, very intelligent, smart cars that know much earlier than I do
*  that there is an object or a person approaching. All of that, I believe, I think we could,
*  if we wanted, we could already do this today. We might have a computational issue that we cannot
*  create this cheap enough, but this is just a matter of time. But to literally have a car
*  to decide how to move from point A to point B, I think that we need to find a different approach.
*  And my belief is that probably the most efficient will be the way how evolution
*  taught the mouse to do this. In fact, we don't even need human intelligence to drive a car.
*  A proper mouse brain, I'm sure, would give a pretty good driver.
*  That's funny to imagine.
*  But it's damn hard to create something that is equivalent to a mouse. So just to give a sort of
*  an outlook there, if you consider all of these IoT stuff, so in the end, you notice driving a car
*  automatically means that you have to work with sensor data and that has to be in a model and
*  that model has to tell how you use the steering wheel and the gas and things like that. And
*  although we have this ambition, there is not even a standard way of creating the representation of
*  the status of a car. I mean, it could well be that I missed something, but when you ask the operating
*  system of a car today, what is your status, you get probably 500 pages of floating point values
*  of all sorts of sensors. But that's not a status. And if you ask biologically, if you ask a
*  biologist or someone who has a natural science view on things, they will exactly know what's
*  meant by the status. It's this sort of compound, semantic situation that could even have a name,
*  like driving slowly uphill on a curvy street. That would be a status in the heat, to use an
*  adjective. And if you imagine the temperature of your engine, your sensor tells you the temperature
*  is, let's say, 100 degrees Celsius. So what can this mean? This can mean that either you're driving
*  fast in the plane or you're driving slow uphill or you're driving in a hot ambient temperature.
*  And you will always get the same measurements, namely 100 degrees Celsius, but it will mean
*  many different cases. But if you happen to drive downhill in the winter and the engine has 100
*  degrees Celsius, then you know that's an anomaly. Something's going wrong. And again, it's the same
*  measurement. So it's not by collecting all the measurements that we are going to understand
*  what's happening to the car. We will understand it if we have a way of capturing the semantic
*  space of the car and using it to interpret any measurement that we do on this car. And we've done
*  experiments and we could demonstrate that you could apply semantic folding to these kinds of
*  sensor data. I was going to ask you if you had a recommendation for a similar type business to
*  cortical I.O. that you think would be good to start based on these same principles.
*  So that would be IOT in general. Internet of Things, IOT? Absolutely. Absolutely. All the things
*  closer to your domain, for example, is you could interpret medical records.
*  With every blood sample, you can get up to 50 or more parameters. And one thing, and if you remember,
*  I said the only thing that's needed for semantic folding to work is a grammar. But you can be sure
*  that all the parameters that you can read out of a blood sample, they relate to each other
*  grammatically because they're coming from the same system, which is the human body. So if one
*  parameter is high, that will influence all other parameters, even if I don't exactly know how and
*  where. But I can assume that all the parameters sampled at the very same moment for the very same
*  individual will have a deep interaction and the link between them. And in the same way, you could
*  create a fingerprint of the calcium level in the blood of a patient. And given on the fingerprint,
*  you could possibly say that he is very close with his pattern to someone who just had a heart attack
*  or he's very close to someone who does a lot of endurance sport. That's what is to be sort of
*  refined. I just want to say that I think that this whole semantic folding could be sort of a
*  universal concept. That of course, the way how we see today is of course naive, but it might be
*  something that comes closer to what nature has converged to in order to make sense of the world.
*  It certainly has that potential. So you guys heard it. Francisco just gave multiple ideas
*  that you could apply this to. So go start your own business here. So what is something that you wish
*  you knew starting a sort of AI-based, neuroscience-based startup or a tech startup? What is something that you
*  wish you knew going in or maybe like a valuable one of the more valuable lessons that you've
*  learned through the because you've been you've been doing this for what 20 plus years?
*  In the meantime, yes, it has been a while. Yes, that's correct. In several configurations. So I
*  did this more with the service-oriented approach, but I also did this now with a technology approach.
*  And first of all, there is a big difference. For some reason, I don't know why exactly, but
*  service-oriented products are at least nowadays a much easier sell, for example, to investors and so
*  on than a technology because when it comes to technology, first of all, it's much harder to
*  innovate technology, which is already a not easy way to do because it's not just doing the little
*  improvement potentially, but it might need some more fundamental approach. And today, this is
*  mostly done at the level of business models. So there is a lot of creativity in creating new
*  functional bundles and finding new ways of selling them. That's basically, I think, what carries the
*  internet boom and the whole digitization, basically. But we have still we are still lacking some
*  quite fundamental components. And one of those is definitely the way how we process data according
*  to the in the meantime already old von Neumann approach. And it's interesting to see how hard
*  it is today to think out of the von Neumann box. It reminds me a bit with Darwin's times when he
*  tried to tell people that you can explain a lot by applying the concepts of evolution.
*  But there were, of course, a lot of situations that he couldn't answer yet because he has also to
*  study and think through things. But having found a principle that is somehow counterintuitive
*  and matches nicely to questions that have not that were not touched simply because
*  there was more creationist approach then. It took quite an amount of effort to do this,
*  but it also created a lot of space for a whole new generation of science. So I think even the
*  physicists in the end had improved their way of researching because someone like Darwin came along
*  at some point. Yeah. Yeah. And yeah, so yeah, one has simply to stick to this guideline of
*  trying to be more efficient. As soon as you see that you do something more efficient than it used
*  to be done, you can assume that you have a business there. You just need to maybe forge it
*  to find out how you implement it. But before you don't see that you improve efficiency in any
*  any sort of dimension, usually it will be hard to run a business on that.
*  Do you do you recommend starting a business? Absolutely. I think it's the most adequate
*  time nowadays to innovate. It might not be so much the academic world, maybe for certain topics.
*  There might be topics that just need the real reality. I mean, the scientific reality has
*  always some sort of optimized clean room situation with the exception of specifically problematic
*  sciences like the most sociology or to some degree philosophy even I would say that have been blurry.
*  But I think that in the future, those might become the leading sciences if you want,
*  leading, let's say in a commercial undercodes way or with the commercial impact they have.
*  Because once we manage to compute with semantics, then we can approach something like sociology
*  in a much more realistic manner. Just imagine if you make the proper fingerprint of the message of
*  a politician and you make the fingerprint of the opinion of a voter, you have a completely new way
*  of looking at these things, not as percentage values, but as differentiated detailed partial
*  overlaps and the non-overlaps. I think that there is a whole, once we master semantics
*  programmatically, we can overcome statistics. So statistics is the best tool for us currently
*  to explain the world and make it useful. But it has this fundamental limitation that it's
*  just a model and it's just more or less like reality. But with the semantic folding approach,
*  you can compute with the literal data that reality provides. I'm pretty sure that this
*  will open up a lot of new perspectives. That's exciting. What I really meant was
*  just because it's a scary thing to just go on your own and start a business because
*  businesses fail. Yeah, so what? Yeah, I know. Well, see, that's the thing is you have that attitude,
*  but maybe you're just that special type of person to forge ahead.
*  And the point is, even if it fails, it can sort of bring you forward. It depends
*  if you have been sincere with yourself in doing this try. If you have been, then it will improve
*  yourself. I'm convinced of that. But this is also a very specific difference, for example, between
*  the US community, let's say in the tech scene and the European, you're not so much allowed to fail,
*  if at all, in Europe. So you rather chew your product a very long time until it's perfect.
*  And then you hit the market and you become a star. What happens often, unfortunately, is that
*  people have just moved on and the market where you wanted to offer your product doesn't exist
*  anymore by the time it takes to actually get there. On the other hand, if you have the strategy of
*  building up 100 businesses to actually have one, you burn a lot of money. That's money that also
*  needs to be generated. So both the limits. What I saw to be the rare thing is, so it's not even so
*  much the startup people, it's the investors. They are the sort of the motor for the whole system.
*  Interestingly, so one caveat, if you want, that I would give is don't expect a purely strategic play
*  to happen because strategies are very complicated and especially when involved with money and so on,
*  this becomes a very complicated situation. So in the beginning, it's mostly a tactical play. So you
*  have to be smart in your day-to-day decisions while keeping the strategic view a little down
*  the road but still keeping it in sight. But at least that was something that I struggled with,
*  is to find the right amount of strategy thinking in this whole thing.
*  Well, Francisco, this has been, I really appreciate you taking so much time and sharing
*  so much knowledge with us today. I really think what you're doing is great work and I just wish
*  you the best of luck moving forward and thanks for being with us today.
*  Thanks a lot. It was a pleasure.
