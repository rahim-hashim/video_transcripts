---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 7189s
Video Keywords: []
Video Views: 167579
Video Rating: None
Video Description: 
---

# François Chollet Keras, Deep Learning, and the Progress of AI  Lex Fridman Podcast #38
**Lex Fridman:** [September 14, 2019](https://www.youtube.com/watch?v=Bo8MY4JpiXE)
*  The following is a conversation with Francois Chalet.
*  He's the creator of Keras, which is an open source deep learning library
*  that is designed to enable fast, user-friendly experimentation with deep neural networks.
*  It serves as an interface to several deep learning libraries, most popular of which is
*  TensorFlow, and it was integrated into the TensorFlow main code base a while ago.
*  Meaning, if you want to create, train, and use neural networks, probably the easiest and most
*  popular option is to use Keras inside TensorFlow. Aside from creating an exceptionally useful and
*  popular library, Francois is also a world-class AI researcher and software engineer at Google.
*  And he's definitely an outspoken, if not controversial, personality in the AI world,
*  especially in the realm of ideas around the future of artificial intelligence.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  give us five stars on iTunes, support it on Patreon, or simply connect with me on Twitter
*  at Lex Friedman, spelled F-R-I-D-M-A-N. And now, here's my conversation with Francois Chalet.
*  You're known for not sugarcoating your opinions and speaking your mind about ideas in AI,
*  especially on Twitter. It's one of my favorite Twitter accounts. So, what's one of the more
*  controversial ideas you've expressed online and gotten some heat for? How do you pick?
*  Yeah, no, I think if you go through the trouble of maintaining a Twitter account,
*  you might as well speak your mind, you know? Otherwise, what's even the point of having a
*  Twitter account? It's like having a nice car and just leave it in the garage.
*  Yeah, so what's one thing for which I got a lot of pushback? Perhaps, you know,
*  that time I wrote something about the idea of intelligence explosion, and I was questioning
*  the idea and the reasoning behind this idea. And I got a lot of pushback on that. I got a lot of
*  flak for it. So, yeah, so intelligence explosion, I'm sure you're familiar with the idea, but it's
*  the idea that if you were to build general AI problem-solving algorithms, well, the problem
*  of building such an AI, that itself is a problem that could be solved by your AI, and maybe it
*  could be solved better than what humans can do. So, your AI could start tweaking its own algorithm,
*  could start making a better version of itself, and so on iteratively in a recursive fashion.
*  And so you would end up with an AI with exponentially increasing intelligence.
*  That's right.
*  And I was basically questioning this idea, first of all, because the notion of intelligence
*  explosion uses an implicit definition of intelligence that doesn't sound quite right to me. It
*  considers intelligence as a property of a brain that you can consider in isolation,
*  like the height of a building, for instance. But that's not really what intelligence is.
*  Intelligence emerges from the interaction between a brain, a body, like embodied intelligence,
*  and an environment. And if you're missing one of these pieces, then you cannot really define
*  intelligence anymore. So just tweaking a brain to make it smarter and smarter doesn't actually
*  make any sense to me.
*  So first of all, you're crushing the dreams of many people, right? So there's a, let's look at
*  like Sam Harris, actually a lot of physicists, Max Tegmark, people who think, you know, the universe
*  is an information processing system. Our brain is kind of an information processing system.
*  So what's the theoretical limit? Like it doesn't make sense that there should be some,
*  it seems naive to think that our own brain is somehow the limit of the capabilities and
*  this information is just, I'm playing devil's advocate here, this information processing
*  system. And then if you just scale it, if you're able to build something that's on par with the
*  brain, you just, the process that builds it just continues and it will improve exponentially.
*  So that's the logic that's used actually by almost everybody that is worried about superhuman
*  intelligence. So you're trying to make, so most people who are skeptical of that are kind of like,
*  this doesn't, their thought process, this doesn't feel right. Like that's for me as well. So I'm
*  more like, it doesn't, the whole thing is shrouded in mystery where you can't really say anything
*  concrete, but you could say this doesn't feel right. It doesn't feel like that's how the brain
*  works. And you're trying to with your blog posts and now making a little more explicit.
*  So one idea is that the brain isn't, exists alone. It exists within the environment.
*  So you can't exponentially, you would have to somehow exponentially improve the environment
*  and the brain together almost yet in order to create something that's much smarter in some kind
*  of, of course we don't have a definition of intelligence. That's correct. That's correct.
*  I don't think you should look at very smart people today, even humans, not even talking about AIs.
*  I don't think their brain and the performance of their brain is the bottleneck to their
*  expressed intelligence to their achievements. You cannot just tweak one part of the system,
*  like of this brain, body, environment system, and expect capabilities like what emerges out of this
*  system to just explode exponentially. Because anytime you improve one part of a system with
*  many interdependencies like this, there's a new bottleneck that arises. And I don't think even
*  today for very smart people, their brain is not the bottleneck to the sort of problems they can
*  solve. In fact, many very smart people today, they're not actually solving any big scientific
*  problems. They're not Einstein. They're like Einstein, but the patent clerk days.
*  Einstein became Einstein because this was a meeting of a genius with a big problem
*  at the right time. But maybe this meeting could have never happened, and then Einstein would have
*  just been a patent clerk. In fact, many people today are probably like genius level smart,
*  but you wouldn't know because they're not really expressing any of that.
*  Wow, that's brilliant. So we can think of the world, Earth, but also the universe as just
*  as a space of problems. So all these problems and tasks are roaming it of various difficulty.
*  And there's agents, creatures like ourselves and animals and so on that are also roaming it.
*  And then you get coupled with a problem and then you solve it. But without that coupling,
*  you can't demonstrate your quote unquote intelligence.
*  Exactly. Intelligence is the meaning of great problem solving capabilities with a great problem.
*  And if you don't have the problem, you don't really express an intelligence. All you're left
*  with is potential intelligence, like the performance of your brain or how high your IQ is,
*  which in itself is just a number. So you mentioned problem solving capacity.
*  What do you think of as problem solving? Can you try to define intelligence?
*  What does it mean to be more or less intelligent? Is it completely coupled to a particular problem?
*  Or is there something a little bit more universal?
*  Yeah, I do believe all intelligence is specialized intelligence. Even human intelligence
*  has some degree of generality. Well, all intelligence systems have some degree of generality,
*  but they're always specialized in one category of problems. So the human intelligence is specialized
*  in the human experience. And that shows at various levels, that shows in some prior knowledge,
*  that's innate, that we have at birth. Knowledge about things like agents, goal-driven behavior,
*  visual priors about what makes an object, priors about time, and so on. That shows also in the way
*  we learn, for instance, it's very, very easy for us to pick up language. It's very, very easy for
*  us to learn certain things because we are basically hard-coded to learn them. And we are specialized
*  in solving certain kinds of problems, and we are quite useless when it comes to other kinds of
*  problems. For instance, we are not really designed to handle very long-term problems. We have no
*  capability of seeing the very long-term. We don't have very much working memory.
*  So how do you think about long-term? Do you think long-term planning, we're talking about
*  scale of years, millennia, what do you mean by long-term, we're not very good?
*  Well, human intelligence is specialized in the human experience. And human experience is very
*  short. One lifetime is short. Even within one lifetime, we have a very hard time envisioning
*  things on a scale of years. It's very difficult to project yourself at a scale of five years,
*  a scale of 10 years, and so on. We can solve only fairly narrowly scoped problems. So when it comes
*  to solving bigger problems, larger scale problems, we are not actually doing it on an individual
*  level. So it's not actually our brain doing it. We have this thing called civilization, which is
*  itself a problem-solving system, a artificial intelligence system. And it's not running on
*  one brain, it's running on a network of brains. In fact, it's running on much more than a network
*  of brains. It's running on a lot of infrastructure, like books and computers and the internet and
*  human institutions and so on. And that is capable of handling problems on a much greater scale than
*  any individual human. If you look at computer science, for instance, that's an institution
*  that solves problems and it is superhuman. It operates on a greater scale. It can solve
*  much bigger problems than an individual human could. And science itself, science as a system,
*  as an institution, is a kind of artificially intelligent problem-solving algorithm that is
*  superhuman. Yeah, it's a, well, at least computer science is like a theorem prover
*  at a scale of thousands, maybe hundreds of thousands of human beings.
*  At that scale, what do you think is an intelligent agent? So there's us humans at the individual
*  level. There is millions, maybe billions of bacteria on our skin. That's at the smaller
*  scale. You can even go to the particle level as systems that behave, you can say intelligently
*  in some ways. And then you can look at Earth as a single organism. You can look at our galaxy,
*  and even the universe as a single organism. Do you think, how do you think about scale and
*  defining intelligent systems? And we're here at Google, there is millions of devices doing
*  computation in a distributed way. How do you think about intelligence versus scale?
*  You can always characterize anything as a system. I think people who talk about things like
*  intelligence explosion tend to focus on one agent is basically one brain, like one brain
*  considered in isolation, like a brain, a jar that's controlling a body in a very like top to bottom
*  kind of fashion. And that body is pursuing goals into an environment. So it's a very hierarchical
*  view. You have the brain at the top of the pyramid, then you have the body just plainly receiving
*  orders, and then the body is manipulating objects in the environment and so on. So everything is
*  subordinate to this one thing, this epicenter, which is the brain. But in real life, intelligent
*  agents don't really work like this, right? There is no strong delimitation between the brain and
*  the body to start with. You have to look not just at the brain, but at the nervous system.
*  But then the nervous system and the body are naturally two separate entities. So you have to
*  look at an entire animal as one agent. But then you start realizing as you observe an animal over
*  any length of time, that a lot of the intelligence of an animal is actually externalized. That's
*  especially true for humans. A lot of our intelligence is externalized. When you write down some notes,
*  there is externalized intelligence. When you write a computer program, you are externalizing
*  cognition. So it's externalizing books, it's externalized in computers, the internet, in other
*  humans. It's externalizing language and so on. So there is no hard delimitation of what makes an
*  intelligent agent. It's all about context. Okay, but AlphaGo is better at Go than the best human
*  player. There's levels of skill here. So do you think there's such a concept
*  as an intelligence explosion in a specific task? Do you think it's possible to have a category of
*  tasks on which you do have something like an exponential growth of ability to solve that
*  particular problem? I think if you consider a specific vertical, it's probably possible to
*  some extent. I also don't think we have to speculate about it because we have real world
*  examples of recursively self-improving intelligence systems. For instance, science
*  is a problem-solving system, a knowledge generation system, like a system that
*  experiences the world in some sense and then gradually understands it and can act on it.
*  That system is superhuman and it is clearly recursively self-improving because science
*  feeds into technology. Technology can be used to build better tools, better computers, better
*  instrumentation and so on, which in turn can make science faster. So science is probably the closest
*  thing we have today to a recursively self-improving superhuman AI. You can just observe, is scientific
*  progress to the exploding, which itself is an interesting question. You can use that as a basis
*  to try to understand what will happen with a superhuman AI that has a science-like behavior.
*  Let me linger on it a little bit more. What is your intuition why an intelligence explosion
*  is not possible? Taking all the scientific revolutions, why can't we slightly accelerate
*  that process? You can absolutely accelerate any problem-solving process. Recursive
*  self-improvement is absolutely a real thing. But what happens with a recursively self-improving system
*  is typically not explosion because no system exists in isolation. Tweaking one part of the system
*  means that suddenly another part of the system becomes a bottleneck. If you look at science,
*  which is clearly a recursively self-improving, clearly a problem-solving system,
*  scientific progress is not actually exploding. If you look at science, what you see is the picture
*  of a system that is consuming an exponentially increasing amount of resources, but it's having
*  a linear output in terms of scientific progress. Maybe that will seem like a very strong claim.
*  Many people are actually saying that scientific progress is exponential, but when they're claiming
*  this, they're actually looking at indicators of resource consumption by science. For instance,
*  the number of papers being published, the number of patents being filed and so on, which are just
*  completely correlated with how many people are working on science today. So it's actually an
*  indicator of resource consumption. But what you should look at is the output, is progress in terms
*  of the knowledge that science generates, in terms of the scope and significance of the problems that
*  we solve. And some people have actually been trying to measure that. Like Michael Nielsen,
*  Michael Nielsen, for instance, he had a very nice paper, I think that was last year, about it.
*  So his approach to measure scientific progress was to look at the timeline of scientific discoveries
*  over the past 100, 150 years. And for each major discovery, ask a panel of experts to rate the
*  significance of the discovery. And if the output of science as an institution were exponential,
*  you would expect the temporal density of significance to go up exponentially, maybe because
*  there's a faster rate of discoveries, maybe because the discoveries are increasingly more important.
*  And what actually happens if you plot this temporal density of significance measured in this way,
*  is that you see very much a flat graph. You see a flat graph across all disciplines, across physics,
*  biology, medicine, and so on. And it actually makes a lot of sense if you think about it,
*  because think about the progress of physics 110 years ago, right? It was a time of crazy change.
*  Think about the progress of technology 170 years ago, when we started replacing horses with cars,
*  when we started having electricity and so on. It was a time of incredible change. And today is also
*  a time of very, very fast change. But it would be an unfair characterization to say that today,
*  technology and science are moving way faster than they did 50 years ago or 100 years ago.
*  And if you do try to rigorously plot the temporal density of the significance,
*  you do see very flat curves. And you can check out the paper that Michael Nielsen had about this idea.
*  And so the way I interpret it is, as you make progress in a given field or in a given subfield
*  of science, it becomes exponentially more difficult to make further progress. Like the very first
*  person to work on information theory. If you enter a new field, and it's still the very early years,
*  there's a lot of low hanging fruit you can pick. But the next generation of researchers is going to
*  have to dig much harder, actually, to make smaller discoveries, probably larger numbers,
*  smaller discoveries. And to achieve the same amount of impact, you're going to need a much
*  greater headcount. And that's exactly the picture you're seeing with science, is that the number of
*  scientists and engineers is in fact increasing exponentially. The amount of computational
*  resources that are available to science is increasing exponentially and so on. So the
*  resource consumption of science is exponential, but the output in terms of progress, in terms of
*  significance, is linear. And the reason why is because, and even though science is recursively
*  self-improving, meaning that scientific progress turns into technological progress, which in turn
*  helps science. If you look at computers, for instance, our products of science and computers
*  are tremendously useful in speeding up science. The internet, same thing, the internet is a
*  technology that's made possible by very recent scientific advances. And itself, because it
*  enables scientists to network, to communicate, to exchange papers and ideas much faster,
*  it is a way to speed up scientific progress. So even though you're looking at a recursively
*  self-improving system, it is consuming exponentially more resources to produce the same amount of
*  problem solving. So that's a fascinating way to paint it. And certainly that holds for the
*  deep learning community, right? If you look at the temporal, what did you call it? The temporal
*  density of significant ideas. If you look at in deep learning, I think I'd have to think about
*  that. But if you really look at significant ideas in deep learning, that might even be decreasing.
*  So I do believe the per paper significance is decreasing, but the amount of papers is still
*  today exponentially increasing. So I think if you look at an aggregate, my guess is that you would
*  see linear progress. If you were to sum the significance of all papers,
*  you would see roughly linear progress. And in my opinion, it is not a coincidence that you're
*  seeing linear progress in science despite exponential resource conception. I think the
*  resource conception is dynamically adjusting itself to maintain linear progress because we,
*  as a community, expect linear progress, meaning that if we start investing less and seeing less
*  progress, it means that suddenly there are some lower hanging fruits that become available and
*  someone's going to step up and pick them. So it's very much like a market for discoveries and ideas.
*  But there's another fundamental part which you're highlighting, which as a hypothesis,
*  science or the space of ideas, any one path you travel down, it gets exponentially more difficult
*  to get new ideas, to develop new ideas. And your sense is that's going to hold across
*  our mysterious universe. Yes. Well, exponential progress triggers exponential friction.
*  So that if you tweak one part of the system, suddenly some other part becomes a bottleneck.
*  For instance, let's say you develop some device that measures its own acceleration,
*  and then it has some engine and it outputs even more acceleration in proportion of its own
*  acceleration and you drop it somewhere. It's not going to reach infinite speed because it exists in
*  a certain context. So the air around it is going to generate friction and it's going to block it at
*  some top speed. And even if you were to consider the broader context and lift the bottleneck there,
*  like the bottleneck of friction, then some other part of the system would start stepping in and
*  creating exponential friction, maybe the speed of light or whatever. And this definitely holds
*  true when you look at the problem-solving algorithm that is being run by science as an
*  institution, science as a system. As you make more and more progress, despite having this recursive
*  self-improvement component, you are encountering exponential friction. The more researchers you
*  have working on different ideas, the more overhead you have in terms of communication
*  across researchers. If you look at, you were mentioning quantum mechanics, right? Well,
*  if you want to start making significant discoveries today, significant progress in
*  quantum mechanics, there is an amount of knowledge you have to ingest, which is huge.
*  So there's a very large overhead to even start to contribute. There's a large amount of overheads to
*  synchronize across researchers and so on. And of course, the significant practical experiments
*  are going to require exponentially expensive equipment because the easier ones have already
*  been run. Right. So in your sense, there's no way of escaping this kind of friction with artificial
*  intelligence systems? Yeah. I think science is a very good way to model what would happen with
*  a superhuman recursive system proving error. That's your sense. That's my intuition. It's not
*  a mathematical proof of anything. That's not my point. I'm not trying to prove anything. I'm
*  just trying to make an argument to question the narrative of intelligence explosion, which is
*  quite a dominant narrative. And you do get a lot of pushback if you go against it. So for many people,
*  AI is not just a subfield of computer science. It's more like a belief system, like this belief that
*  the world is headed towards an event, the singularity, past which AI will go exponential very much,
*  and the world will be transformed and humans will become obsolete. And if you go against this
*  narrative, because it is not really a scientific argument, but more of a belief system, it is part
*  of the identity of many people. If you go against this narrative, it's like you're attacking the
*  identity of people who believe in it. It's almost like saying God doesn't exist or something. So you
*  do get a lot of pushback if you try to question these ideas. First of all, I believe most people,
*  they might not be as eloquent or explicit as you're being, but most people in computer science
*  are most people who actually have built anything that you could call AI, quote unquote, would agree
*  with you. They might not be describing it in the same kind of way. It's more, so the pretty
*  more, so the pushback you're getting is from people who get attached to the narrative from,
*  not from a place of science, but from a place of imagination. That's correct. So why do you think
*  that's so appealing? Because the usual dreams that people have when you create a super intelligent
*  system, past the singularity, that what people imagine is somehow always destructive. Do you
*  put on your psychology hat? Why is it so appealing to imagine the ways that all of human civilization
*  will be destroyed? I think it's a good story. It's a good story. And very interestingly, it mirrors
*  religious stories, right? Religious mythology. If you look at the mythology of most civilizations,
*  it's about the world being headed towards some final events in which the world will be destroyed
*  and some new world order will arise that will be mostly spiritual, like the apocalypse followed by
*  paradise probably. It's a very appealing story on a fundamental level. And we all need stories. We
*  all need stories to structure the way we see the world, especially at timescales that are beyond
*  our ability to make predictions. So on a more serious non-exponential explosion
*  question, do you think there will be a time when we'll create something like human-level intelligence
*  or intelligent systems that will make you sit back and be just surprised and damn how smart this
*  thing is? That doesn't require exponential growth or exponential improvement, but what's your sense
*  in a timeline and so on that you'll be really surprised at certain capabilities? And we'll
*  talk about limitations and deep learning and so on. Do you think in your lifetime you'll be really
*  damn surprised? Around 2013, 2014, I was many times surprised by the capabilities of deep learning,
*  that was before we had assessed exactly what deep learning could do and could not do. And it felt
*  like a time of immense potential. And then we started narrowing it down, but I was very surprised.
*  So we'd say it has already happened. Was there a moment, there must have been a day in there,
*  where your surprise was almost bordering on the belief of the narrative that we just discussed.
*  Was there a moment, because you've written quite eloquently about the limits of deep learning,
*  was there a moment that you thought that maybe deep learning is limitless?
*  No, I don't think I've ever believed this. What was really shocking is that it worked.
*  It worked at all. Yeah.
*  But there's a big jump between being able to do really good computer vision and human-level
*  intelligence. So I don't think at any point I wasn't an impression that the results we got
*  in computer vision meant that we were very close to human-level intelligence. I don't think we're
*  very close to human-level intelligence. I do believe that there's no reason why we won't achieve it at
*  some point. I also believe that the problem with talking about human-level intelligence is that
*  implicitly you're considering an axis of intelligence with different levels.
*  But that's not really how intelligence works. Intelligence is very multi-dimensional.
*  There's the question of capabilities, but there's also the question of being human-like.
*  And it's two very different things. You can build potentially very advanced intelligent
*  agents that are not human-like at all. And you can also build very human-like agents. And these are
*  two very different things. Right. Let's go from the philosophical to the practical.
*  Can you give me a history of Keras and all the major deep learning frameworks that you kind of
*  remember in relation to Keras and in general, TensorFlow, Theano, the old days? Can you give
*  a brief overview Wikipedia style history and your role in it before we return to AGI discussions?
*  Yeah, that's a broad topic. So I started working on Keras. It was named Keras at the time.
*  I actually picked the name just the day I was going to release it. So I started working on it
*  in February 2015. And so at the time, there weren't too many people working on deep learning,
*  maybe fewer than 10,000. The software tooling was not really developed.
*  So the main deep learning library was CAFE, which was mostly C++.
*  Why do you say CAFE was the main one?
*  CAFE was vastly more popular than Theano in late 2014, early 2015. CAFE was the one library that
*  everyone was using for computer vision. And computer vision was the most popular problem.
*  Absolutely. Like, ConvNets was like the subfield of deep learning that everyone was working on.
*  So in late 2014, I was actually interested in RNNs, in Recurrent Neural Networks, which was
*  a very niche topic at the time. It really took off around 2016. And so I was looking for good tools.
*  I'd used Torch 7. I'd used Theano a lot in Kaggle competitions. I'd used CAFE. And
*  there was no good solution for RNNs at the time. There was no reusable open source
*  implementation for LSTM, for instance. So I decided to build my own. And at first,
*  the pitch for that was it was going to be mostly around LSTM, Recurrent Neural Networks. It was
*  going to be in Python. An important decision at the time that was kind of non-ambitious is that
*  the models would be defined via Python code, which was kind of like going against the mainstream at
*  the time because CAFE, Python 2 and so on, like all the big libraries were actually going with
*  the approach of having static configuration files in YAML to define models. So some libraries were
*  using code to define models like Torch 7, obviously, but that was not Python. Lasagne was like
*  a Theano-based very early library that was, I think, developed, I don't remember exactly,
*  probably late 2014. It's Python as well. It's Python as well. It was like on top of Theano.
*  And so I started working on something. And the value proposition at the time was that
*  not only what I think was the first reusable open source implementation of LSTM,
*  you could combine RNNs and covenants with the same library, which is not really possible before.
*  Like CAFE was only doing covenants. And it was kind of easy to use because before I was using
*  Theano, I was actually using scikit-learn and I loved scikit-learn for its usability. So I drew
*  a lot of inspiration from scikit-learn when I met Karas. It's almost like scikit-learn for neural
*  networks. The fit function. Exactly. The fit function, like reducing a complex train loop to
*  a single function call. And of course, some people will say this is hiding a lot of details, but that's
*  exactly the point. The magic is the point. So it's magical, but in a good way, it's magical in the
*  sense that it's delightful. I'm actually quite surprised. I didn't know that it was born out of
*  desire to implement RNNs and LSTMs. It was. That's fascinating. So you were actually one of the first
*  people to really try to attempt to get the major architectures together. And it's also interesting,
*  you made me realize that that was a design decision at all, is defining the model and code.
*  Just I'm putting myself in your shoes, whether the YAML, especially if Cafe was the most popular.
*  It was the most popular by far. If I was, if I were, yeah, I don't, I didn't like the YAML thing,
*  but it makes more sense that you will put in a configuration file the definition of a model.
*  That's an interesting gutsy move to stick with defining it in code. Just if you look back.
*  Other libraries were doing it as well, but it was definitely the more niche option.
*  Yeah. Okay. Keras and then...
*  Keras. So I released Keras in March 2015 and it got users pretty much from the start.
*  So the deep learning community was very, very small at the time. Lots of people were starting
*  to be interested in LSTM. So it was kind of released at the right time because it was offering an
*  easy to use LSTM implementation. Exactly at the time where lots of people started to be intrigued
*  by the capabilities of RNN. RNN is one LP. So it grew from there.
*  Then I joined Google about six months later, and that was actually completely unrelated to
*  Keras. I actually joined a research team working on image classification, mostly like computer
*  vision. So I was doing computer vision research at Google initially. And immediately when I joined
*  Google, I was exposed to the early internal version of TensorFlow. And the way it appeared
*  to me at the time, and that was definitely the way it was at the time, is that this was
*  an improved version of Theano. So I immediately knew I had to port Keras to this new TensorFlow
*  thing. And I was actually very busy as a new Googler. So I had not time to work on that.
*  But then in November, I think it was November 2015, TensorFlow got released. And it was kind
*  of like my wake-up call that, hey, I had to actually go and make it happen. So in December,
*  I ported Keras to run onto a TensorFlow. But it was not exactly port. It was more like a refactoring
*  where I was abstracting away all the backend functionality into one module so that the same
*  code base could run on top of multiple backends, on top of TensorFlow or Theano. And for the next
*  year, Theano stayed as the default option. It was easier to use, somewhat less buggy.
*  It was much faster, especially when it came to ordinance. But eventually, TensorFlow overtook it.
*  Right. And TensorFlow, the early TensorFlow, a similar architectural decisions as Theano.
*  Yeah. So it was a natural transition. Yeah, absolutely.
*  So what, I mean, that still Keras is a side, almost fun project, right?
*  Yeah. So it was not my job assignment. It was not. I was doing it on the side. And even though it
*  grew to have a lot of users for a deep learning library at the time, like Stroud 2016, but I
*  wasn't doing it as my main job. So things started changing in, I think it must have been maybe
*  October 2016. So one year later, so Rajat, who was the lead on TensorFlow, basically showed up one day
*  in our building where I was doing research and things like, so I did a lot of computer
*  vision research, also collaborations with Christian Zugeding and deep learning for
*  theorem proving. It was a really interesting research topic. And so Rajat was saying, hey,
*  we saw Keras, we like it, we saw that you're at Google. Why don't you come over for like a quarter
*  and work with us? And I was like, yeah, that sounds like a great opportunity. Let's do it.
*  And so I started working on integrating the Keras API into TensorFlow more tightly.
*  So what followed up is a sort of like temporary TensorFlow only version of Keras that was in
*  TensorFlow.contrib for a while and finally moved to TensorFlow Core. And, you know, I've never
*  actually gotten back to my old team doing research. Well, it's kind of funny that
*  somebody like you who dreams of, or at least sees the power of AI systems that reason and
*  theorem proving we'll talk about has also created a system that makes the most basic kind of
*  Lego building that is deep learning super accessible, super easy. So beautifully so.
*  It's a funny irony that you're both responsible for both things. So TensorFlow 2.0,
*  there's a sprint. I don't know how long it'll take, but there's a sprint towards the finish.
*  What are you looking at? What are you working on these days? What are you excited about? What
*  are you excited about in 2.0? I mean, eager execution. There's so many things that just
*  make it a lot easier to work. What are you excited about? And what's also really hard?
*  What are the problems you have to kind of solve? So I've spent the past year and a half
*  working on TensorFlow 2.0. It's been a long journey. I'm actually extremely excited about it.
*  I think it's a great product. It's a delightful product compared to TensorFlow 1. We've made
*  huge progress. So on the Keras side, what I'm really excited about is that, so,
*  you know, previously Keras has been this very easy to use high level interface to do deep learning.
*  But if you wanted to, you know, if you wanted a lot of flexibility, the Keras framework, you know,
*  was probably not the optimal way to do things compared to just writing everything from scratch.
*  So in some way, the framework was getting in the way. And in TensorFlow 2.0, you don't have this
*  at all. Actually, you have the usability of the high level interface, but you have the flexibility
*  of this lower level interface. And you have this spectrum of workflows where you can get
*  more or less usability and flexibility trade-offs depending on your needs.
*  Right. You can write everything from scratch and you get a lot of help doing so by, you know,
*  subclassing models and writing some train loops using eager execution. It's very flexible. It's
*  very easy to debug. It's very powerful. But all of this integrates seamlessly with higher level
*  features up to, you know, the classic Keras workflows, which are very psychic and like,
*  and, you know, are ideal for a data scientist, machine learning engineer type of profile.
*  So now you can have the same framework offering the same set of APIs that enable a spectrum of
*  workflows that are more or less low level, more or less high level that are suitable for profiles
*  ranging from researchers to data scientists and everything in between. Yeah. So that's super
*  exciting. I mean, it's not just that it's connected to all kinds of tooling. You can go on mobile,
*  you can go with TensorFlow Lite, you can go in the cloud or serving and so on. It all is
*  connected together. Now, some of the best software written ever is often done by one person,
*  sometimes two. So with a Google, you're now seeing sort of Keras having to be integrated in
*  TensorFlow. I'm sure it's a ton of engineers working on. So, and there's, I'm sure, a lot of
*  tricky design decisions to be made. How does that process usually happen from at least your
*  perspective? What are the, what are the debates like? What, is there a lot of
*  thinking, considering different options and so on? Yes. So a lot of the time
*  I spent at Google is actually discussing design discussions, right? Writing design docs,
*  participating in design review meetings and so on. This is, you know, as important as actually
*  writing the code. Right. What's the- There's a lot of thoughts. There's a lot of thought and a lot
*  of care that is taken in coming up with these decisions and taking into account all of our
*  users because TensorFlow has this extremely diverse user base, right? It's not like just
*  one user segment where everyone has the same needs. We have small scale production users,
*  large scale production users. We have startups, we have researchers. You know, it's all over the
*  place and we have to cater to all of their needs. If I just look at the standard debates of C++ or
*  Python, there's some heated debates. Do you have those at Google? I mean, they're not heated in
*  terms of emotionally, but there's probably multiple ways to do it, right? So how do you arrive
*  through those design meetings at the best way to do it, especially in deep learning where
*  the field is evolving as you're doing it? Is there some magic to it? There's some magic to the process?
*  I don't know if there's magic to the process, but there definitely is a process. So making design
*  decisions is about satisfying a set of constraints, but also trying to do so in the simplest way
*  possible because this is what can be maintained. This is what can be expanded in the future.
*  So you don't want to naively satisfy the constraints by just, you know, for each capability
*  you need available, you're going to come up with one argument, new API and so on. You want to design
*  APIs that are modular and hierarchical so that they have an API surface that is as small as possible,
*  right? And you want this modular hierarchical architecture to reflect the way that domain
*  experts think about the problem. Because as a domain expert, when you're reading about a new
*  API, you're reading a tutorial or some docs pages, you already have a way that you're thinking about
*  the problem. You already have certain concepts in mind and you're thinking about how they relate
*  together. And when you're reading docs, you're trying to build as quickly as possible a mapping
*  between the concepts featured in your API and the concepts in your mind. So you're trying to
*  map your mental model as a domain expert to the way things work in the API. So you need an API
*  and an underlying implementation that are reflecting the way people think about these things.
*  So in minimizing the time it takes to do the mapping.
*  Yes. Minimizing the time, the cognitive load there is in ingesting this new knowledge about your API.
*  An API should not be self-referential or referring to implementation details. It should only be
*  referring to domain specific concepts that people already understand.
*  Brilliant. So what's the future of Keras and TensorFlow look like? What does TensorFlow 3.0
*  look like? So that's kind of too far in the future for me to answer, especially
*  since I'm not even the one making these decisions. But so from my perspective,
*  which is just one perspective among many different perspectives on the TensorFlow team,
*  I'm really excited by developing even higher level APIs, higher level than Keras. I'm really
*  excited by hyperparameter tuning, by automated machine learning, AutoML.
*  I think the future is not just defining a model like you were assembling Lego blocks and then
*  collect fit on it. It's more like an automagical model that would just look at your data
*  and optimize the objective you're after. So that's what I'm looking into.
*  So you put the baby into a room with the problem and come back a few hours later
*  with a fully solved problem. Exactly. It's not like a box of Legos. It's more like the combination of
*  a kid that's really good at Legos and a box of Legos and just building the thing on his own.
*  Very nice. So that's an exciting feature. I think there's a huge amount of applications and
*  revolutions to be had under the constraints of the discussion we previously had. But what do you think
*  of the current limits of deep learning? If we look specifically at these function approximators
*  that try to generalize from data. You've talked about local versus extreme generalization.
*  You mentioned that neural networks don't generalize well and humans do. So there's this gap.
*  And you've also mentioned that it's generalization is not always easy.
*  So and you've also mentioned that extreme generalization requires something like
*  reasoning to fill those gaps. So how can we start trying to build systems like that?
*  Right. Yeah. So this is by design. Deep learning models are like huge parametric models
*  differentiable, so continuous, that go from an input space to an output space. And they're
*  trained with gradient descent. So they're trained pretty much point by point. They're learning a
*  continuous geometric morphing from an input vector space to an output vector space. And
*  because this is done point by point, a deep neural network can only make sense of points in
*  experience space that are very close to things that it has already seen in string data. At best,
*  it can do interpolation across points. But that means, you know, it means in order to train your
*  network, you need a dense sampling of the input cross output space, almost a point by point sampling,
*  which can be very expensive if you're dealing with complex real world problems like autonomous
*  driving, for instance, or robotics. It's doable if you're looking at the subset of the visual space,
*  but even then it's still fairly expensive. You still need millions of examples.
*  And it's only going to be able to make sense of things that are very close to what it has seen
*  before. And in contrast to that, well, of course, you have human intelligence. But even if you're
*  not looking at human intelligence, you can look at very simple rules, algorithms. If you have a
*  symbolic rule, it can actually apply to a very, very large set of inputs because it is abstract.
*  It is not obtained by doing a point by point mapping, right? For instance, if you try to learn
*  a sorting algorithm using a deep neural network, well, you're very much limited to learning point
*  by point what the sorted representation of this specific list is like. But instead, you could
*  have a very, very simple sorting algorithm written in a few lines. Maybe it's just, you know,
*  two nested loops. And it can process any list at all because it is abstract, because it is a set
*  of rules. So deep learning is really like point by point geometric morphings,
*  morphings, trying to understand. And meanwhile, abstract rules can generalize much better.
*  And I think the future is really to combine the two.
*  So how do we, do you think, combine the two? How do we combine good point by point functions
*  with programs, which is what the symbolic AI type systems, at which levels the combination happen?
*  Obviously, we're jumping into the realm of where there's no good answers.
*  It's just kind of ideas and intuitions and so on.
*  Well, if you look at the really successful AI systems today, I think they're already hybrid
*  systems that are combining symbolic AI with deep learning. For instance, successful robotics
*  systems are already mostly model-based, rule-based things like planning algorithms and so on.
*  At the same time, they're using deep learning as perception modules.
*  Sometimes they're using deep learning as a way to inject fuzzy intuition into a rule-based process.
*  If you look at a system like a self-driving car, it's not just one big end-to-end neural network
*  that wouldn't work at all, precisely because in order to train that, you would need a dense sampling
*  of experience space when it comes to driving, which is completely unrealistic, obviously.
*  Instead, the self-driving car is mostly symbolic. Its software is programmed by hand. So it's mostly
*  based on explicit models, in this case, mostly 3D models of the environment around the car,
*  but it's interfacing with the real world using deep learning modules.
*  The deep learning there serves as a way to convert the raw sensory information
*  to something usable by symbolic systems.
*  Let's linger on that a little more. Dense sampling from input to output.
*  You said it's obviously very difficult. Is it possible?
*  In the case of self-driving, you mean?
*  Let's say self-driving. For many people,
*  let's not even talk about self-driving. Let's talk about steering, staying inside the lane.
*  Lane following, yeah, it's definitely a problem you can solve with an end-to-end deep learning model,
*  but that's like one small subset.
*  Hold on a second. I don't know why you're jumping from the extreme so easily,
*  because I disagree with you on that. It's not obvious to me that you can solve lane following.
*  No, it's not obvious. I think it's doable. I think in general, there are no hard limitations
*  to what you can learn with a deep neural network, as long as the search space is rich enough,
*  is flexible enough, and as long as you have this dense sampling of the input cross output space.
*  The problem is that this dense sampling could mean anything from
*  10,000 examples to trillions and trillions.
*  So that's my question. What's your intuition?
*  If you could just give it a chance and think what kind of problems can be solved by getting
*  a huge amount of data and thereby creating a dense mapping. Let's think about
*  natural language dialogue, the Turing test. Do you think the Turing test can be solved
*  with a neural network alone?
*  Well, the Turing test is all about tricking people into believing they're talking to a human.
*  And I don't think that's actually very difficult because it's more about exploiting
*  human perception and not so much about intelligence. There's a big difference between
*  mimicking intelligent behavior and actual intelligent behavior.
*  So, okay, let's look at maybe the Alexa Prize and so on. The different formulations of the
*  natural language conversation that are less about mimicking and more about maintaining a fun
*  conversation that lasts for 20 minutes. That's a little less about mimicking and that's more about,
*  I mean, it's still mimicking, but it's more about being able to carry forward a conversation with
*  all the tangents that happen in dialogue and so on. Do you think that problem is learning
*  learnable with this kind of neural network that does the point-to-point mapping?
*  So I think it would be very, very challenging to do this with deep learning.
*  I don't think it's out of the question either. I wouldn't rule it out.
*  The space of problems that can be solved with a large neural network,
*  what's your sense about the space of those problems? Useful problems for us.
*  In theory, it's infinite. You can solve any problem. In practice, well, deep learning is
*  a great fit for perception problems. In general, any problem which is not really amenable to
*  explicit and crafted rules or rules that you can generate by exhaustive search over some program
*  space. So perception, artificial intuition, as long as you have a sufficient training data set.
*  And that's the question. I mean, perception, there's interpretation and understanding of the
*  scene, which seems to be outside the reach of current perception systems. So do you think
*  larger networks will be able to start to understand the physics and the physics of the scene,
*  the three dimensional structure and relationships of the visors in the scene and so on,
*  or really that's where symbolic AI has to step in?
*  Well, it's always possible to solve these problems with deep learning. It's just extremely
*  inefficient. An explicit rule-based abstract model would be a far better, more compressed
*  representation of physics than learning just this mapping between in this situation,
*  this thing happens. If you change the situation slightly, then this other thing happens and so on.
*  Do you think it's possible to automatically generate the programs that would require that
*  kind of reasoning or does it have to? So the way expert systems fail, there's so many facts about
*  the world had to be hand coded in. I think it's possible to learn those logical statements that
*  are true about the world and their relationships. I mean, that's kind of what they're improving at
*  a basic level is trying to do. Right? Yeah. Except it's much harder to formulate statements
*  about the world compared to formulating mathematical statements. Statements about the world tend to be
*  subjective. So can you learn rule-based models? Yes, definitely. That's the field of program
*  synthesis. However, today we just don't really know how to do it. So it's very much a grass search
*  or tree search problem. And so we are limited to the sort of tree search and grass search algorithms
*  that we have today. Personally, I think genetic algorithms are very promising.
*  So almost like genetic programming. Genetic programming, exactly.
*  Can you discuss the field of program synthesis? Like how many people are working and thinking
*  about it? Where we are in the history of program synthesis and what are your hopes for it?
*  Well, if it were deep learning, this is like the nineties. So meaning that we already have existing
*  solutions. We are starting to have some basic understanding of what this is about, but it's
*  still a field that is in its infancy. There are very few people working on it. There are very few
*  real-world applications. So the one real-world application I'm aware of is Flash Fill in Excel.
*  It's a way to automatically learn very simple programs to format cells in an Excel spreadsheet
*  from a few examples. For instance, learning a way to format a date, things like that.
*  Oh, that's fascinating. Yeah. Okay, that's a fascinating topic. I always wonder when I provide
*  a few samples to Excel, what it's able to figure out. Like just giving it a few dates.
*  What are you able to figure out from the pattern I just gave you? That's a fascinating question.
*  It's fascinating whether that's learnable patterns. And you're saying they're working on that.
*  How big is the toolbox currently? Are we completely in the dark? So if you said
*  in terms of programs, I would say maybe 90s is even too optimistic because by the 90s,
*  we already understood backprop. We already understood the engine of deep learning even
*  though we couldn't really see its potential quite. Today, I don't think we've found the engine of
*  program synthesis. So we're in the winter before backprop. Yeah, in a way, yes. So I do believe
*  program synthesis in general, discrete search over rule-based models is going to be a cornerstone
*  of AI research in the next century. And that doesn't mean we're going to drop deep learning.
*  Deep learning is immensely useful. Being able to learn is a very flexible, adaptable,
*  parametric model. So it's got to understand that's actually immensely useful. All it's doing
*  is pattern recognition, but being good at pattern recognition, given lots of data,
*  is just extremely powerful. So we are still going to be working on deep learning. We're going to be
*  working on program synthesis. We're going to be combining the two in increasingly automated ways.
*  So let's talk a little about data. You've tweeted
*  about 10,000 deep learning papers have been written about hard coding priors about a specific task
*  in a neural network architecture. It works better than a lack of a prior. Basically summarizing all
*  these efforts, they put a name to an architecture, but really what they're doing is hard coding some
*  priors that improve the performance of the system. But it gets straight to the point,
*  it's probably true. So you say that you can always buy performance by in quotes,
*  performance by either training on more data, better data, or by injecting task information
*  to the architecture of the pre-processing. However, this isn't informative about the
*  generalization power of the techniques used, the fundamental ability to generalize. Do you think
*  we can go far by coming up with better methods for this kind of cheating, for better methods of
*  large scale annotation of data? So building better priors. If you made it, it's not cheating anymore.
*  Right. I'm joking about the cheating, but large scale. So basically I'm asking about
*  something that hasn't, from my perspective, been researched too much is exponential improvement
*  in annotation of data. Do you often think about... I think it's actually been researched quite a bit.
*  You just don't see publications about it because people who publish papers are going to publish
*  about known benchmarks. Sometimes they're going to read a new benchmark. People who actually have
*  real world large scale deep learning problems, they're going to spend a lot of resources into
*  data annotation and good data annotation pipelines, but you don't see any papers about it.
*  That's interesting. So do you think there's certainly resources, but do you think there's
*  innovation happening? Oh yeah, definitely. To clarify the point in the tweet. So machine
*  learning in general is the science of generalization. You want to generate knowledge that can be reused
*  across different datasets, across different tasks. And if instead you're looking at one dataset,
*  and then you are hard coding knowledge about this task into your architecture, this is
*  no more useful than training a network and then saying, oh, I found these weight values perform
*  well. Right. So David Ha, I don't know if you know David, he had a paper the other day
*  about weight agnostic neural networks. And this is a very interesting paper because it really
*  illustrates the fact that an architecture, even without weights, an architecture is
*  knowledge about a task. It encodes knowledge. And when it comes to architectures that are
*  uncrafted by researchers, in some cases it is very, very clear that all they are doing is
*  artificially re-encoding the template that corresponds to the proper way to solve
*  task encoding given dataset. For instance, I know if you've looked at the baby dataset,
*  which is about natural language question answering, it is generated by an algorithm. So this is a
*  question and answer pairs that are generated by an algorithm. The algorithm is so long as
*  a template. Turns out if you craft a network that literally encodes this template,
*  you can solve this dataset with nearly 100% accuracy. But that doesn't actually tell you
*  anything about how to solve question answering in general, which is the point.
*  Right. The question is just to linger on it, whether it's from the data side or from the
*  size of the network. I don't know if you've read the blog post by Ray Sutton, The Bitter Lesson,
*  where he says the biggest lesson that we can read from 70 years of AI research is that general
*  methods that leverage computation are ultimately the most effective. So as opposed to figuring out
*  methods that can generalize effectively, do you think we can get pretty far by just having
*  something that leverages computation and the improvement of computation?
*  Yeah. So I think Rich is making a very good point, which is that a lot of these papers,
*  which are actually all about manually hard coding prior knowledge about a task into some system,
*  doesn't have to be deep learning architecture, but into some system, right? These papers are
*  not actually making any impact. Instead, what's making really long-term impact is very simple,
*  very general systems that are really agnostic to all these tricks, because these tricks do not
*  generalize. And of course, the one general and simple thing that you should focus on is that
*  which leverages computation, because computation, the availability of large-scale computation has
*  been increasing exponentially, following Moore's law. So if your algorithm is all about exploiting
*  this, the new algorithm is suddenly exponentially improving. So I think Rich is definitely right.
*  However, he's right about the past 70 years. He's assessing the past 70 years. I am not sure that
*  this assessment will still hold true for the next 70 years. It might, to some extent. I suspect it
*  will not, because the truth of his assessment is a function of the context in which this research
*  took place. And the context is changing. Moore's law might not be applicable anymore, for instance,
*  in the future. And I do believe that when you tweak one aspect of a system, when you exploit
*  one aspect of a system, some other aspect starts becoming the bottleneck. Let's say you have
*  unlimited computation. Well, then data is the bottleneck. And I think we are already starting
*  to be in a regime where our systems are so large in scale and so data-engraved. The data today and
*  the quality of data and the scale of data is the bottleneck. And in this environment,
*  the bitter lesson from Rich is not going to be true anymore. So I think we are going to move
*  from a focus on a scale of a competition scale to focus on data efficiency.
*  Data efficiency. So that's getting to the question of symbolic AI. But to linger on the deep learning
*  approaches, do you have hope for either unsupervised learning or reinforcement learning,
*  which are ways of being more data efficient in terms of the amount of data they need
*  that require human annotation? So unsupervised learning and reinforcement learning are frameworks
*  for learning, but they're not like any specific technique. So usually when people say reinforcement
*  learning, what they really mean is deep reinforcement learning, which is like one
*  approach, which is actually very questionable. The question I was asking was unsupervised learning
*  with deep neural networks and deep reinforcement learning. Well, these are not really data efficient
*  because you're still leveraging these huge parametric models, train point by point with
*  gradient descent. It is more efficient in terms of the number of annotations, the density of
*  annotations you need. So the idea being to learn the latent space around which the data is organized
*  and then map the sparse annotations into it. And sure, I mean, that's clearly a very good idea.
*  It's not really a topic I would be working on, but it's clearly a good idea.
*  So it would get us to solve some problems that...
*  It will get us to incremental improvements in labeled data efficiency.
*  Do you have concerns about short term or long term threats from AI, from artificial intelligence?
*  Yes, definitely to some extent.
*  And what's the shape of those concerns?
*  This is actually something I've briefly written about, but the capabilities of
*  deep learning technology can be used in many ways that are concerning from mass surveillance
*  with things like facial recognition, in general, tracking lots of data about everyone and then
*  being able to making sense of this data, to do identification, to do prediction.
*  That's concerning. That's something that's being very aggressively pursued by total Italian states
*  like China. One thing I am very much concerned about is that our lives are
*  increasingly online, are increasingly digital, made of information consumption and information
*  production, our digital footprint, I would say. And if you absorb all of this data and you are
*  in control of where you consume information, social networks and so on, recommendation engines,
*  then you can build a sort of reinforcement loop for human behavior. You can observe
*  the state of your mind at time T. You can predict how you would react to different pieces of content,
*  how to get you to move your mind in a certain direction. And then you can feed you
*  a specific piece of content that would move you in a specific direction. And you can do this at scale,
*  at scale in terms of doing it continuously in real time. You can also do it at scale in terms of
*  scaling this to many, many people, to entire populations. So potentially artificial intelligence,
*  even in its current state, if you combine it with the internet, with the fact that we have
*  all of our lives are moving to digital devices and digital information consumption and creation,
*  what you get is the possibility to achieve mass manipulation of behavior and mass
*  psychological control. And this is a very real possibility.
*  Yeah. So you're talking about any kind of recommender system.
*  Let's look at the YouTube algorithm, Facebook, anything that recommends content you should watch
*  next. And it's fascinating to think that there's some aspects of human behavior that you can
*  say a problem of, is this person hold Republican beliefs or Democratic beliefs? And it's just
*  a trivial, that's an objective function. And you can optimize and you can measure and you can turn
*  everybody into Republican. Everybody into a Democrat. Absolutely. Yeah. I do believe it's true.
*  So the human mind is very, if you look at the human mind as a kind of computer program,
*  it has a very large exploit surface, right? It has many, many vulnerabilities. Exploit surfaces,
*  ways you can control it. For instance, when it comes to your political beliefs, this is very much
*  tied to your identity. So for instance, if I'm in control of your newsfeed on your favorite social
*  media platforms, this is actually where you're getting your news from. And of course, I can
*  choose to only show you news that will make you see the world in a specific way, right? But I can also
*  create incentives for you to post about some political beliefs. And then when I get you to
*  express a statement, if it's a statement that me as the controller, I want to reinforce, I can just
*  show it to people who will agree and they will like it. And that will reinforce the statement in
*  your mind. If this is a statement I want you to, this is a belief I want you to abandon, I can,
*  on the other hand, show it to opponents, right? Will attack you. And then because they attack you,
*  at the very least, next time you will think twice about posting it. But maybe you will even
*  stop believing this because you got pushback, right? So there are many ways in which
*  social media platforms can potentially control your opinions. And today,
*  the, so all of these things are already being controlled by AI algorithms. These algorithms
*  do not have any explicit political goal today. While potentially they could, like if some
*  totalitarian government takes over social media platforms and decides that now we're going to use
*  this not just for mass surveillance, but also for mass opinion control and behavior control,
*  very bad things could happen. But what's really fascinating and actually quite concerning is that
*  even without an explicit intent to manipulate, you're already seeing very dangerous dynamics
*  in terms of how these content recommendation algorithms behave. Because right now, the goal,
*  the objective function of these algorithms is to maximize engagement, right? Which seems fairly
*  innocuous at first, right? However, it is not because content that will maximally engage people,
*  get people to react in an emotional way, get people to click on something, it is very often
*  an
*  content that is not healthy to the public discourse. For instance, fake news are far more likely
*  to get you to click on them than real news simply because they are not constrained to reality. So
*  they can be as outrageous, as surprising, as good stories as you want because they're artificial,
*  to me that's an exciting world because so much good can come. So there's an opportunity to
*  educate people. You can balance people's worldview with other ideas. So there's so many objective
*  functions, the space of objective functions that create better civilizations is large,
*  arguably infinite. But there's also a large space that creates division and
*  destruction, civil war, a lot of bad stuff. And the worry is naturally probably that space is bigger,
*  first of all. And if we don't explicitly think about what kind of effects are going to be observed
*  from different objective functions, then we're going to get into trouble. But the question is,
*  how do we get into rooms and have discussions? So inside Google, inside Facebook, inside Twitter,
*  and think about, okay, how can we drive up engagement and at the same time create a good
*  society? Is it even possible to have that kind of philosophical discussion?
*  I think you can definitely try. So from my perspective, I would feel rather uncomfortable
*  with companies that are in control of these new algorithms, with them making explicit decisions
*  to manipulate people's opinions or behaviors, even if the intent is good, because that's a very
*  totalitarian mindset. So instead, what I would like to see is probably never going to happen,
*  because it's not very realistic, but that's actually something I really care about. I would
*  like all these algorithms to present configuration settings to their users, so that the users can
*  actually make the decision about how they want to be impacted by these information recommendation,
*  content recommendation algorithms. For instance, as a user of something like YouTube or Twitter,
*  maybe I want to maximize learning about a specific topic. So I want the algorithm
*  to feed my curiosity, which is in itself a very interesting problem. So instead of
*  maximizing my engagement, it will maximize how fast and how much I'm learning, and it will also
*  take into account the accuracy, hopefully, of the information I'm learning. So yeah, the user should
*  be able to determine exactly how these algorithms are affecting their lives. I don't want actually
*  any entity making decisions about in which direction they're going to try to manipulate me.
*  Right? I want technology. So AI, these algorithms are increasingly going to be our interface to a
*  world that is increasingly made of information. And I want everyone to be in control of this
*  interface, to interface with the world on their own terms. So if someone wants these algorithms
*  to serve their own personal growth goals, they should be able to configure these algorithms in
*  such a way. Yeah, but so I know it's painful to have explicit decisions, but there is underlying
*  explicit decisions, which is some of the most beautiful fundamental philosophy that we have
*  before us, which is personal growth. If I want to watch videos from which I can learn, what does
*  that mean? So if I have a checkbox that wants to emphasize learning, there's still an algorithm
*  with explicit decisions in it that would promote learning. What does that mean for me? Like for
*  example, I've watched a documentary on flat earth theory, I guess. It was very like that. I learned
*  a lot. I'm really glad I watched it. It was a friend recommended it to me, not because I don't have
*  such an allergic reaction to crazy people as my fellow colleagues do, but it was very eye opening.
*  And for others it might not be. From others, they might just get turned off for that. Same with
*  Republican and Democrat. It's a non-trivial problem. And first of all, if it's done well,
*  I don't think it's something that wouldn't happen, that YouTube wouldn't be promoting,
*  or Twitter wouldn't be. It's just a really difficult problem. How do we give people control?
*  Well, it's mostly an interface design problem. The way I see it, you want to create technology
*  that's like a mentor or a coach or an assistant so that it's not your boss. You are in control of it.
*  You are telling it what to do for you. And if you feel like it's manipulating you, it's not actually
*  doing what you want. You should be able to switch to a different algorithm.
*  So that fine-tune control, you kind of learn. You're trusting the human collaboration. I mean,
*  that's how I see Atanos vehicles too, is giving as much information as possible and you learn that
*  dance yourself. Adobe, I don't know if you use Adobe product for like Photoshop. Yeah, they are
*  trying to see if they can inject YouTube into their interface, but basically allow you to
*  show you all these videos because everybody's confused about what to do with features. So
*  basically teach people by linking to, in that way it's an assistant that uses videos as a basic
*  element of information. Okay, so what practically should people do to try to fight against abuses of
*  these algorithms or algorithms that manipulate us? Honestly, it's a very, very difficult problem
*  because to start with, there is very little public awareness of these issues. Very few people would
*  think there's anything wrong with their new algorithm, even though there is actually something
*  wrong already, which is that it's trying to maximize engagement most of the time, which
*  has very negative side effects. Ideally, the very first thing is to stop trying to
*  purely maximize engagement, try to propagate content based on popularity. Instead, take into account
*  the goals and the profiles of each user. One example is, for instance, when I look at
*  topic recommendations on Twitter, like they have this news tab with switch recommendations,
*  it's always the worst garbage because it's content that appeals to the
*  smallest common denominator to all Twitter users because they're trying to optimize,
*  they're purely trying to optimize popularity, they're purely trying to optimize engagement,
*  but that's not what I want. They should put me in control of some setting so that I define what's
*  the objective function that Twitter is going to be following to show me this content. Honestly,
*  this is all about interface design. It's not realistic to give users control of a bunch of
*  knobs that define an algorithm. Instead, we should purely put them in charge of defining
*  the objective function. Let the user tell us what they want to achieve, how they want this algorithm
*  to impact their lives. Do you think it is that or do they provide individual article by article
*  reward structure where you give a signal, I'm glad I saw this or I'm glad I didn't?
*  Like a Spotify type feedback mechanism, it works to some extent. I'm kind of skeptical about it
*  because the only way the algorithm will attempt to relate your choices with the choices of everyone
*  else, which might, if you have an average profile that works fine, I'm sure Spotify accommodations
*  work fine if you just like mainstream stuff. If you don't, it's not optimal at all actually.
*  It'll be an inefficient search for the part of the Spotify world that represents you.
*  So it's a tough problem, but do note that even a feedback system like what Spotify has does not
*  give me control over what the algorithm is trying to optimize for. Well, public awareness,
*  which is what we're doing now, is a good place to start. Do you have concerns about long-term
*  existential threats of artificial intelligence? Well, as I was saying, our world is increasingly
*  made of information. AI algorithms are increasingly going to be our interface to this world of
*  information and somebody will be in control of these algorithms. And that puts us in any kind
*  of bad situation. It has risks. It has risks coming from potentially large companies wanting
*  to optimize their own goals, maybe profit, maybe something else. Also from governments
*  who might want to use these algorithms as a means of control of the population.
*  Do you think there's existential threat that could arise from that?
*  So existential threats. So maybe you're referring to the singularity narrative where robots
*  just take over. Well, I don't not terminate a robot and I don't believe it has to be a singularity.
*  We're just talking to, just like you said, the algorithm controlling masses of populations.
*  The existential threat being hurt ourselves much like a nuclear war would hurt ourselves.
*  That kind of thing. I don't think that requires a singularity. That requires a loss of control over
*  AI algorithms. Yes. So I do agree there are concerning trends. Honestly, I wouldn't want
*  to make any long-term predictions. I don't think today we really have the capability to see
*  what the dangers of AI are going to be in 50 years, in 100 years. I do see that we are already faced
*  with a concrete and present dangerous surrounding the negative side effects of content
*  recommendation systems of new algorithms concerning algorithmic bias as well. So we are
*  delegating more and more decision processes to algorithms. Some of these algorithms are
*  uncrafted, some are learned from data, but we are delegating control. Sometimes it's a good thing.
*  Sometimes not so much. There is in general very little supervision of this process.
*  We are still in this period of very fast change, even chaos, where society is restructuring itself,
*  turning into an information society, which itself is turning into an increasingly
*  automated information processing society. Well, I think the best we can do today is try to
*  raise awareness around some of these issues. And I think we're actually making good progress. If you
*  look at algorithmic bias, for instance, three years ago, even two years ago, very, very few
*  people were talking about it. And now all the big companies are talking about it. They are often
*  not in a very serious way, but at least it is part of the public discourse. You see people in Congress
*  talking about it. And it all started from raising awareness.
*  Right. So in terms of alignment problem, trying to teach as we allow algorithms,
*  just even recommender systems on Twitter,
*  encoding human values and morals, decisions that touch on ethics. How hard do you think that problem
*  is? How do we have loss functions in neural networks that have some fuzzy components of human morals?
*  Well, I think this is really all about objective function engineering, which is probably going to
*  be increasingly a topic of concern in the future. For now, we are just using very naive loss functions
*  because the hard part is not actually what you're trying to minimize. It's everything else. But as
*  the everything else is going to be increasingly automated, we're going to be focusing our human
*  attention on increasingly high level components, like what's actually driving the whole learning
*  system, like the objective function. So loss function engineering is going to be, loss function
*  engineer is probably going to be a job title in the future. And then the tooling you're creating
*  with Keras essentially takes care of all the details underneath. And basically, the human
*  expert is needed for exactly that. That's the idea. Keras is the interface between the data you're
*  collecting and the business goals. And your job as an engineer is going to be to express
*  your business goals and your understanding of your business or your product, your system,
*  as a kind of loss function or a kind of set of constraints.
*  Does the possibility of creating an AGI system excite you or scare you or bore you?
*  So intelligence can never really be general. At best, it can have some degree of generality,
*  like human intelligence. It also always has some specialization in the same way that human
*  intelligence is specialized in a certain carrier of problems, it's specialized in the human
*  experience. And when people talk about AGI, I'm never quite sure if they're talking about
*  very, very smart AI, so smart that it's even smarter than humans, or they're talking about
*  human-like intelligence, because these are different things. Let's say, presumably,
*  I'm impressing you today with my humanness. So imagine that I was in fact a robot. So what does
*  that mean? I'm impressing you with natural language processing. Maybe if you weren't able to see me,
*  maybe this is a phone call. So that kind of system, companion.
*  That's very much about building human-like AI. And you're asking me, is this an exciting perspective?
*  Yes. I think so, yes. Not so much because of what artificial human-like intelligence could do, but
*  from an intellectual perspective, I think if you could build truly human-like intelligence,
*  that means you could actually understand human intelligence, which is fascinating.
*  Human-like intelligence is going to require emotions. It's going to require consciousness,
*  which is not things that would normally be required by an intelligent system. If you look at,
*  we were mentioning earlier, science as a superhuman problem-solving agent or system,
*  it does not have consciousness. It doesn't have emotions. In general, emotions,
*  I see consciousness as being on the same spectrum as emotions. It is a component of the subjective
*  experience that is meant very much to guide behavior generation. It's meant to guide your
*  behavior. In general, human intelligence and animal intelligence has evolved for the purpose
*  of behavior generation, including in a social context. That's why we actually need emotions.
*  That's why we need consciousness. An artificial intelligence system developed in a different
*  context may never need them, may never be conscious, like science.
*  On that point, I would argue it's possible to imagine that there are echoes of consciousness
*  in science when viewed as an organism, that science is consciousness.
*  How would you go about testing this hypothesis? How do you
*  probe the subjective experience of an abstract system like science?
*  The point of probing any subjective experience is impossible. I'm not science,
*  I'm lex. I can't probe another entity. It's no more than bacteria on my skin.
*  You're lex. I can ask you questions about your subjective experience and you can answer me.
*  That's how I know you're conscious. Yes, but that's because we speak the same language.
*  You perhaps, we have to speak the language of science.
*  Honestly, I don't think consciousness, just like emotions of pain and pleasure,
*  is not something that inevitably arises from any sort of sufficiently intelligent information
*  processing. It is a feature of the mind. If you've not implemented it explicitly, it is not there.
*  You think it's an emergent feature of a particular architecture?
*  It's a feature in the same sense. Again, the subjective experience is all about
*  guiding behavior. If the problems you're trying to solve don't really involve
*  an embodied agent, maybe in a social context, generating behavior and pursuing goals like this.
*  If you look at science, that's not really what's happening, even though it is a form of
*  artificial AI, artificial intelligence in the sense that it is solving problems, it is
*  accumulating knowledge, accumulating solutions and so on. If you're not explicitly implementing
*  a subjective experience, implementing certain emotions and implementing consciousness,
*  it's not going to just spontaneously emerge.
*  Yeah. For a system like human-like intelligent system that has consciousness,
*  do you think it needs to have a body?
*  Yes, definitely. It doesn't have to be a physical body,
*  and there's not that much difference between a realistic simulation and the real world.
*  There has to be something you have to preserve kind of thing.
*  Yes, but human-like intelligence can only arise in a human-like context.
*  Intelligence starts.
*  You need other humans in order for you to demonstrate that you have human-like
*  intelligence essentially. So what kind of tests and demonstration would be sufficient for you
*  to demonstrate human-like intelligence? Just out of curiosity, you've talked about,
*  in terms of theorem proving and program synthesis, I think you've written about that there's no good
*  benchmarks for this. That's one of the problems. So let's talk program synthesis. What do you
*  imagine is a good... I think it's related questions for human-like intelligence and for program
*  synthesis. What's a good benchmark for either or both?
*  Right. So you're actually asking two questions, which is one is about quantifying intelligence
*  and comparing the intelligence of an artificial system to the intelligence for human.
*  And the other is about the degree to which this intelligence is human-like.
*  It's actually two different questions. So if you look, you mentioned earlier the Turing test.
*  Well, I actually don't like the Turing test because it's very lazy. It's all about
*  completely bypassing the problem of defining and measuring intelligence and instead delegating
*  to a human judge or a panel of human judges. So it's a total cope out.
*  Right. If you want to measure how human-like an agent is, I think you have to make it interact
*  with other humans. Maybe it's not necessarily a good idea to have these other humans be the judges.
*  Maybe you should just observe behavior and compare it to what a human would actually have done.
*  When it comes to measuring how smart, how clever an agent is and comparing that
*  to the degree of human intelligence. So we're already talking about two things, right?
*  The degree, kind of like the magnitude of an intelligence and its direction, right? Like the
*  norm of a vector and its direction. And the direction is like human likeness and the magnitude,
*  the norm is intelligence. You could call it intelligence, right?
*  So the direction, your sense, the space of directions that are human-like is very narrow.
*  Yeah. So the way you would measure the magnitude of intelligence in a system in a way that also
*  enables you to compare it to that of a human. Well, if you look at different benchmarks for
*  intelligence today, they're all too focused on skill at a given task. That skill at playing chess,
*  skill at playing Go, skill at playing Dota. And I think that's not the right way to go about it
*  because you can always beat a human at one specific task. The reason why our skill at playing Go or
*  at juggling or anything is impressive is because we are expressing this skill within a certain set
*  of constraints. If you remove the constraints, the constraints that we have one lifetime,
*  that we have this body and so on, if you remove the context, if you have unlimited trained data,
*  if you can have access to, for instance, if you look at juggling, if you have no restriction on
*  the hardware, then achieving arbitrary levels of skill is not very interesting and says nothing
*  about the amount of intelligence you've achieved. So if you want to measure intelligence, you need
*  to rigorously define what intelligence is, which in itself, it's a very challenging problem.
*  And do you think that's possible?
*  To define intelligence? Yes, absolutely. I mean, you can provide, many people have provided some
*  definition. I have my own definition. Where does your definition begin if it doesn't end?
*  Well, I think intelligence is essentially the efficiency with which you turn experience into
*  generalizable programs. So what that means is it's the efficiency with which you turn a sampling of
*  experience space into the ability to process a larger chunk of experience space. So measuring
*  skill can be one proxy, across many different tasks, can be one proxy for measure intelligence.
*  But if you want to only measure skill, you should control for two things. You should control for
*  the amount of experience that your system has and the priors that your system has. But if you
*  control, if you look at two agents and you give them the same priors and you give them the same
*  amount of experience, there is one of the agents that is going to learn programs, representation,
*  something, a model that will perform well on the larger chunk of experience space than the other.
*  Yeah. So if you have fixed the experience, which generate better programs,
*  better meaning more generalizable, that's really interesting. That's a very nice clean definition.
*  Oh, by the way, in this definition, it's already very obvious that intelligence has to be
*  specialized because you're talking about experience space and you're talking about segments of
*  experience space. You're talking about priors and you're talking about experience. All of these
*  things define the context in which intelligence emerges. And you can never look at the totality
*  of experience space, right? So intelligence has to be specialized.
*  But it can be sufficiently large, the experience space, even though specialized, there's a certain
*  point when the experience space is large enough to where it might as well be general. It feels
*  general. It looks general. Sure. I mean, it's very relative. Like for instance,
*  many people would say human intelligence is general. In fact, it is quite specialized.
*  You know, we can definitely build systems that start from the same innate priors as what humans
*  have at birth, because we already understand fairly well what sort of priors we have as humans.
*  Like many people have worked on this problem, most notably in the case of human intelligence,
*  Elizabeth Spelka from Harvard. I don't know if you know her. She's worked a lot on what she calls
*  core knowledge. And it is very much about trying to determine and describe what priors we are born
*  with. Like language skills and so on, all that kind of stuff. Exactly. So we have some pretty
*  good understanding of what priors we are born with. So I've actually been working on a benchmark
*  for the past couple of years, you know, on and off. I hope to be able to release it at some point.
*  The idea is to measure the intelligence of systems by capturing for priors, capturing for
*  amount of experience, and by assuming the same priors as what humans are born with so that you
*  can actually compare these scores to human intelligence. And you can actually have humans
*  pass the same test in a way that's fair. And so importantly, such a benchmark should be such that
*  any amount of practicing does not increase your score. So try to picture a game where no matter
*  how much you play this game, that does not change your skill at the game. Can you picture that?
*  As a person who deeply appreciates practice, I cannot actually.
*  There's actually a very simple trick. So in order to come up with a task. So the only thing you can
*  measure is skill at a task. All tasks are going to involve priors. The trick is to know what they are
*  and to describe that. And then you make sure that this is the same set of priors as what human
*  start with. So you create a task that assumes these priors, that exactly documents these priors. So
*  that's the priors are made explicit and there are no other priors involved. And then you generate
*  a certain number of samples in experience space for this task. And this, for one task,
*  assuming that the task is new for the agent passing it, that's one test of this
*  definition of intelligence that we set up. And now you can scale that to many different tasks.
*  Each task should be new to the agent passing it. And also should be human interpretable and
*  understandable so that you can actually have a human pass the same test. And then you can compare
*  the score of your machine and the score of your human. Which could be a lot of, you could even
*  start a task like MNIST just as long as you start with the same set of priors. So the problem with
*  MNIST humans are already trying to recognize digits. But let's say we're considering
*  objects that are not digits, some completely arbitrary patterns. Well, humans already come
*  with visual priors about how to process that. So in order to make the game fair, you would have to
*  isolate these priors and describe them and then express them as computational rules.
*  Having worked a lot with vision science people, that's exceptionally difficult. A lot of progress
*  has been made. There's been a lot of good tests and basically reducing all of human vision into
*  some good priors. We're still probably far away from that perfectly, but as a start
*  for a benchmark, that's an exciting possibility. Yeah. So Elizabeth Spelke actually lists
*  objectness as one of the core knowledge priors. Objectness. Cool. Objectness. Yeah.
*  So we have priors about objectness, like about the visual space, about time, about agents,
*  about goal-oriented behavior. We have many different priors. But what's interesting is that
*  sure, we have this pretty diverse and rich set of priors, but it's also not that diverse.
*  We are not born into this world with a ton of knowledge about the world, with only a small set
*  of core knowledge. Yeah, it's hard. Do you have a sense of how
*  it feels to us humans that that set is not that large, but just even the nature of time
*  that we kind of integrate pretty effectively through all of our perception, all of our reasoning?
*  Maybe how, you know, do you have a sense of how easy it is to encode those priors? Maybe
*  it requires building a universe and then the human brain in order to encode those priors.
*  Or do you have a hope that it can be listed like an axiomatic? I don't think so. So you have to
*  keep in mind that any knowledge about the world that we are born with is something that
*  has to have been encoded into our DNA by evolution at some point. And DNA is a very, very low
*  bandwidth medium. Like it's extremely long and expensive to encode anything into DNA because
*  first of all, you need some sort of evolutionary pressure to guide this writing process. And then
*  the higher level information you're trying to write, the longer it's going to take.
*  And the thing in the environment that you're trying to encode knowledge about has to be stable
*  over this duration. So you can only encode into DNA things that constitute an evolutionary advantage.
*  So this is actually a very small subset of all possible knowledge about the world. You can only
*  encode things that are stable, that are true over very, very long periods of time, typically
*  millions of years. For instance, we might have some visual prior about the shape of snakes,
*  but what makes a face? What's the difference between a face and an orange face? But consider
*  this interesting question. Do we have any innate sense of the visual difference between a male face
*  and a female face? What do you think for human? I mean, I would have to look back into evolution,
*  your history when the gender has emerged, but yeah, I think it's a very interesting question.
*  I mean, the faces of humans are quite different from the faces of great apes.
*  Great apes, right? Yeah. You couldn't tell the face of a female chimpanzee from the face of a
*  male chimpanzee, probably. Yeah. And I don't think there are humans of all that. So we do have innate
*  knowledge of what makes a face, but it's actually impossible for us to have any DNA encoded knowledge
*  of the difference between a female human face and a male human face, because that knowledge,
*  that information came up into the world actually very recently, if you look at the slowness of the
*  process of encoding knowledge into DNA. Yeah. So that's interesting. That's a really powerful
*  argument that DNA is a low bandwidth and it takes a long time to encode. That naturally creates a
*  very efficient encoding. One important consequence of this is that, so yes, we are born into this
*  world with a bunch of knowledge, sometimes a high level knowledge about the world, like the shape,
*  the rough shape of a snake, of the rough shape of face. But importantly, because this knowledge
*  takes so long to write, almost all of this innate knowledge is shared with our cousins,
*  with great apes. So it is not actually this innate knowledge that makes us special.
*  But to throw it right back at you from earlier on in our discussion, that encoding might also include
*  the entirety of the environment of earth. To some extent, so it can include things
*  that are important to survival and production, for which there is some evolutionary pressure,
*  and things that are stable, constant over very, very long time periods. And honestly,
*  it's not that much information. There's also, besides the bandwidth constraint and
*  constraints of the writing process, there's also memory constraints. Like DNA, the part of DNA
*  that deals with the human brain, it's actually fairly small. It's like on the order of megabytes.
*  There's not that much high level knowledge about the world you can encode.
*  That's quite brilliant and hopeful for a benchmark that you're referring to of
*  encoding priors. I actually look forward to it. I'm skeptical whether you can do it in the next
*  couple of years, but hopefully. I've been working on it. So honestly,
*  it's a very simple benchmark and it's not like a big breakthrough or anything. It's more like
*  a fun side project. Right? So is ImageNet. These fun side projects could launch entire
*  groups of efforts towards creating reasoning systems and so on. And I think-
*  Yeah, that's the goal. It's trying to measure strong generalization, to measure the strength
*  of abstraction in our minds and in artificial intelligence agents.
*  And if there's anything true about this science organism, it's individual cells love competition.
*  And benchmarks encourage competition. So that's an exciting possibility. Do you think an AI winter
*  is coming and how do we prevent it? Not really. So an AI winter is something that would
*  occur when there's a big mismatch between how we are selling the capabilities of AI and the
*  actual capabilities of AI. And today, deep learning is creating a lot of value and it will
*  keep creating a lot of value in the sense that these models are applicable to a very wide range
*  of problems that are relevant today. And we are only just getting started with applying algorithms
*  to every problem they could be solving. So deep learning will keep creating a lot of value for
*  the time being. What's concerning, however, is that there's a lot of hype around deep learning
*  and around AI. Lots of people are overselling the capabilities of these systems, not just
*  the capabilities, but also overselling the fact that they might be more or less brain-like,
*  given a kind of a mystical aspect of these technologies, and also overselling the pace
*  of progress. Which, you know, it might look fast in the sense that we have this exponentially
*  increasing number of papers. But again, that's just a simple consequence of the fact that we
*  have ever more people coming into the field. It doesn't mean the progress is actually exponentially
*  fast. Let's say you're trying to raise money for your startup or your research lab. You might want
*  to tell a grandiose story to investors about how deep learning is just like the brain and how it
*  can solve all these incredible problems like self-driving, antibiotics, and so on. And maybe
*  you can tell them that the field is progressing so fast and we are going to have AGI within 15
*  years or even 10 years. And none of this is true. And every time you're saying these things,
*  and an investor or a decision maker believes them, well, this is like the equivalent of taking on
*  credit card debt, but for trust. And maybe this will be what enables you to raise a lot of money,
*  but ultimately you are creating damage. You are damaging the field.
*  That's the concern is that that debt, that's what happens with the other AI winters.
*  The concern is you actually tweeted about this with autonomous vehicles. Almost every single
*  company now have promised that they will have full autonomous vehicles by 2021, 2022.
*  That's a good example of the consequences of overhyping the capabilities of AI and the pace
*  of progress. Because I work especially a lot recently in this area, I have a deep concern
*  what happens when all of these companies after having invested billions have a meeting and say,
*  how much do we actually, first of all, do we have an autonomous vehicle? The answer
*  will definitely be no. And second would be, wait a minute, we've invested one, two, three,
*  four billion dollars into this and we made no profit. And the reaction to that
*  may be going very hard in another direction that might impact even other industries.
*  And that's what we call an AI winter is when there is backlash where no one believes
*  any of these promises anymore because they've turned that to be big lies the first time around.
*  And this will definitely happen to some extent for autonomous vehicles because the public
*  and decision makers have been convinced that around 2015, they've been convinced by these
*  people who are trying to raise money for their startups and so on, that L5 driving was coming
*  in maybe 2016, maybe 2017, maybe 2018. Now in 2019, we're still waiting for it.
*  And so I don't believe we're going to have a full on AI winter because we have these technologies
*  that are producing a tremendous amount of real value. But there is also too much hype. So there
*  will be some backlash, especially there will be backlash. So some startups are trying to sell
*  the dream of AGI. And the fact that AGI is going to create infinite value. Like AGI is like a
*  freelance. If you can develop an AI system that passes a certain threshold of IQ or something,
*  then suddenly you have infinite value. And well, there are actually lots of investors
*  buying into this idea. And they will wait maybe 10, 15 years and nothing will happen.
*  And the next time around, well, maybe there will be a new generation of investors. No one will care.
*  Human memory is fairly short after all. I don't know about you, but because I've spoken about
*  AGI sometimes poetically, I get a lot of emails from people giving me, they're usually like large
*  manifestos of they've, they say to me that they have created an AGI system where they know how
*  to do it. And there's a long write up of how to do it. I get a lot of these emails. They're a little
*  bit feel like it's generated by an AI system actually, but there's usually no, maybe that's
*  recursively self improving AI. It's you have a transformer generating crank papers about the AI.
*  So the question is about, because you've been such a good, you have a good radar for crank
*  papers. How do we know they're not onto something? How do I, so when you start to talk about AGI
*  or anything like the reasoning benchmarks and so on, so something that doesn't have a benchmark,
*  it's really difficult to know. I mean, I talked to Jeff Hawkins, who's really looking at neuroscience
*  approaches to how, and there's some, there's echoes of really interesting ideas in at least
*  Jeff's case, which he's showing. How do you usually think about this? Like preventing yourself from
*  being too narrow minded and elitist about, you know, deep learning. It has to work on these
*  particular benchmarks. Otherwise it's trash. Well, you know, the thing is intelligence
*  does not exist in the abstract. Intelligence has to be applied. So if you don't have a benchmark,
*  if you're not doing improvement on some benchmark, maybe it's a new benchmark, right? Maybe it's not
*  something I've been looking at before, but you do need a problem that you're trying to solve. You're
*  not going to come up with a solution without a problem. So you, general intelligence, I mean,
*  you've clearly highlighted generalization. If you want to claim that you have an intelligence
*  system, it should come with a benchmark. Yes, it should display capabilities of some kind.
*  It should show that it can create some form of value, even if it's a very artificial form of
*  value. And that's also the reason why you don't actually need to care about telling which papers
*  have actually submitted potential and which do not. Because if there is a new technique,
*  it's actually creating value. This is going to be brought to light very quickly because it's
*  actually making a difference. So it's the difference between something that is ineffectual
*  and something that is actually useful. And ultimately usefulness is our guide, not just
*  in this field, but if you look at science in general, maybe there are many, many people over
*  the years that have had some really interesting theories of everything, but they were just
*  completely useless. And you don't actually need to tell the interesting theories from the useless
*  theories. All you need is to see, is this actually having an effect on something else? Is this
*  actually useful? Is this making an impact or not? That's beautifully put. I mean, the same applies
*  to quantum mechanics, to string theory, to the holographic principle. We are doing deep learning
*  because it works. Before it started working, people considered people working on neural
*  networks as cranks very much. No one was working on this anymore. And now it's working, which is
*  what makes it valuable. It's not about being right. It's about being effective. And nevertheless,
*  the individual entities of the scientific mechanism, just like Yoshio Banjo, Yon LeCun,
*  while being called cranks, stuck with it. And so us individual agents, even if everyone's laughing
*  at us, just stick with it. If you believe you have something, you should stick with it.
*  And see it through. That's a beautiful inspirational message to end on.
*  Francois, thank you so much for talking today. That was amazing. Thank you.