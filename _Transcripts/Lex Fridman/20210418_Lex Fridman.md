---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 6977s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'risto miikkulainen']
Video Views: 111340
Video Rating: None
---

# Risto Miikkulainen: Neuroevolution and Evolutionary Computation | Lex Fridman Podcast #177
**Lex Fridman:** [April 18, 2021](https://www.youtube.com/watch?v=CY_LEa9xQtg)
*  The following is a conversation with Risto McEllinan, a computer scientist at University
*  of Texas at Austin and Associate Vice President of Evolutionary Artificial Intelligence at Cognizant.
*  He specializes in evolutionary computation, but also many other topics in artificial intelligence,
*  cognitive science, and neuroscience. Quick mention of our sponsors, Jordan Harbourn,
*  Grammarly, Belcampo, and Indeed. Check them out in the description to support this podcast.
*  As a side note, let me say that nature-inspired algorithms, from ant colony optimization to
*  genetic algorithms to cellular automata to neural networks, have always captivated my imagination,
*  not only for their surprising power in the face of long odds, but because they always opened up
*  doors to new ways of thinking about computation. It does seem that in the long arc of computing
*  history, running toward biology, not running away from it, is what leads to long-term progress.
*  This is the Lex Friedman podcast, and here is my conversation with Risto McEllinan.
*  If we ran the Earth experiment, this fun little experiment we're on,
*  over and over and over and over a million times, and watched the evolution of life as it pans out,
*  how much variation in the outcomes of that evolution do you think we would see?
*  Now, we should say that you are a computer scientist.
*  That's actually not such a bad question for computer scientists, because we are building
*  simulations of these things, and we are simulating evolution. That's a difficult
*  question to answer in biology, but we can build a computational model and run it a million times,
*  and actually answer that question. How much variation do we see when we simulate it?
*  That's a little bit beyond what we can do today, but I think that we will see some regularities.
*  It took evolution also a really long time to get started, and then things accelerated really fast
*  towards the end. But there are things that need to be discovered, and they probably will be
*  over and over again, like manipulation of objects, opposable thumbs, and also some way to communicate,
*  maybe orally, like when you have speech, it might be some other kind of sounds,
*  and decision making, but also vision. Eye has evolved many times, various vision systems have
*  evolved. So we would see those kinds of solutions, I believe, emerge over and over again. They may
*  look a little different, but they get the job done. The really interesting question is would
*  we have primates? Would we have humans? Or something that resembles humans? And would that be
*  an apex of evolution after a while? We don't know where we're going from here, but we certainly
*  see a lot of tool use and building our, constructing our environment. So I think that we will get that.
*  We get some evolution producing some agents that can do that, manipulate the environment and build.
*  What do you think is special about humans? If you were running the simulation and you observe
*  humans emerge, like these tool makers, they start a fire and all that stuff, start running around,
*  building buildings, and then running for president, all those kinds of things.
*  How would you detect that? Because you're really busy as the creator of this evolutionary system,
*  so you don't have much time to observe, detect if any cool stuff came up. How would you detect humans?
*  Well, you are running the simulation, so you also put in visualization and measurement
*  techniques there. So if you are looking for certain things like communication,
*  you'll have detectors to find out whether that's happening, even if it's a lot simulation.
*  And I think that that's what we would do. We know roughly what we want, intelligent agents that
*  communicate, cooperate, manipulate, and we would build detections and visualizations of those
*  processes. Yeah, and there's a lot of, you'd have to run it many times and we have plenty of time to
*  figure out how we detect the interesting things. But also, I think we do have to run it many times
*  because we don't quite know what shape those will take and our detectors may not be perfect for them.
*  Well, that seems really difficult to build the detector of intelligent or intelligent
*  communication. If we take an alien perspective, observing Earth, are you sure that they would be
*  able to detect humans as the special thing? Wouldn't they be already curious about other things?
*  There's way more insects by body mass, I think, than humans by far, and colonies. Obviously,
*  dolphins is the most intelligent creature on Earth. But I think that's what we would do.
*  Obviously, dolphins is the most intelligent creature on Earth. We all know this. So,
*  it could be the dolphins that they detect. It could be the rockets that we seem to be launching.
*  That could be the intelligent creature they detect. It could be some other trees. Trees have
*  been here a long time. I just learned that sharks have been here 400 million years, and that's longer
*  than trees have been here. So, maybe it's the sharks. They go by age. There's a persistent thing.
*  If you survive long enough, especially through the mass extinctions, that could be the thing your
*  detector is detecting. Humans have been here for a very short time, and we're just creating a lot of
*  pollution, but so is other creatures. I don't know. Do you think you would be able to detect
*  humans? How would you go about detecting, in the computational sense, maybe we can leave humans
*  behind? In the computational sense, detect interesting things. Do you basically have to
*  have a strict objective function by which you measure the performance of a system,
*  or can you find curiosities and interesting things? Yeah. Well, I think the first
*  measurement would be to detect how much of an effect you can have in your environment. So,
*  if you look around, we have cities, and that is constructed environments, and that's where
*  a lot of people live. Most people live. So, that would be a good sign of intelligence, that you
*  don't just live in an environment, but you construct it to your liking.
*  Yeah. That's something pretty unique. Certainly, birds build nests, but they don't build quite
*  cities. Termites build mounds and hives and things like that, but the complexity of the human
*  construction cities, I think, would stand out even to an external observer.
*  Of course, that's what a human would say. Yeah. You can certainly say that sharks are really smart
*  because they've been around so long and they haven't destroyed their environment,
*  which humans are about to do, which is not a very smart thing. But we'll get over it, I believe.
*  We can get over it by doing some construction that actually is benign and maybe even enhances
*  the resilience of nature. So, you mentioned the simulation that we run over and over might
*  start slowly. It's a slow start. So, do you think how unlikely, first of all, I don't know if you
*  think about this kind of stuff, but how unlikely is step number zero, which is the springing up,
*  like the origin of life on earth? And second, how unlikely is anything interesting happening beyond
*  that? Sort of like the start that creates all the rich complexity that we see on earth today.
*  Yeah. There are people who are working on exactly that problem from Primordial Soup, how do you
*  actually get self-replicating molecules? And they are very close. With a little bit of help,
*  you can make that happen. Of course, we know what we want so they can set up the conditions
*  and try out conditions that are conducive to that. For evolution to discover that,
*  took a long time. For us to recreate it probably won't take that long. And the next steps from there,
*  I think also with some hand holding, I think we can make that happen.
*  But with evolution, what was really fascinating was eventually the
*  runaway evolution of the brain that created humans and created, well, also other higher animals.
*  That was something that happened really fast. And that's a big question. Is that something
*  replicable? Is that something that can happen? And if it happens, does it go in the same direction?
*  That is a big question to ask. Even in computational terms, I think that it's relatively
*  possible to come up with or create an experiment where we look at the Primordial Soup and the first
*  couple of steps of multicellular organisms even. But to get something as complex as the brain,
*  we don't quite know the conditions for that and how to even get started and whether we can get
*  this kind of runaway evolution happening. From a detector perspective, if we're observing
*  this evolution, what do you think is the brain? What do you think is the, let's say, what is
*  intelligence? In terms of the thing that makes humans special, we seem to be able to reason,
*  we seem to be able to communicate. But the core of that is this something in the broad category
*  we might call intelligence. So if you put your computer scientist hat on,
*  is there favorite ways you like to think about that question of what is intelligence?
*  Well, my goal is to create agents that are intelligent.
*  Not to define what?
*  And that is a way of defining it. And that means that it's some kind of an object or a program
*  that has limited sensory and effective capabilities interacting with the world. And then also a
*  mechanism for making decisions. So with limited abilities like that, can it survive? Survival is
*  the simplest goal, but you could also give it other goals. Can it multiply? Can it solve problems
*  that you give it? And that is quite a bit less than human intelligence. Animals would be intelligent,
*  of course, with that definition. And you might have even some other forms of life. So intelligence
*  is a survival skill, given resources that you have and using your resources so that you will stay around.
*  Do you think death, mortality is fundamental to an agent? So there's a philosopher named Ernest Becker
*  who wrote The Now of Death. And his whole idea, and there's folks, psychologists, cognitive scientists
*  that work on terror management theory. And they think that one of the special things about humans
*  is that we're able to foresee our death. We can realize, not just as animals do, constantly fear,
*  in an instinctual sense, respond to all the dangers that are out there, but understand that
*  this ride ends eventually. And that in itself is the force behind all of the creative efforts of
*  human nature. That's the philosophy. I think that makes sense. A lot of sense. I mean, animals
*  probably don't think of death the same way, but humans know that your time is limited and you want
*  to make it count. And you can make it count in many different ways. But I think that has a lot to do
*  with creativity and the need for humans to do something beyond just surviving. And now going
*  from that simple definition to something that's the next level, I think that that could be the
*  second level of definition that intelligence means something. And you do something that stays
*  behind you. That's more than your existence. You create something that is useful for others,
*  is useful in the future, not just for yourself. And I think that's the nicest definition of
*  intelligence in a next level. And it's also nice because it doesn't require that they are humans or
*  biological. They could be artificial agents of that intelligence. They could achieve those kind
*  of goals. So a particular agent, the ripple effects of their existence on the entirety of the system
*  is significant. So they leave a trace where there's ripple effects. But see, then you go
*  back to the butterfly with the flap of a wing, and then you can trace a lot of nuclear wars and all
*  the conflicts of human history somehow connected to that one butterfly that created all the chaos.
*  So maybe that's a very poetic way to think. That's something we humans in a human-centric way want to
*  hope we have this impact. That is the secondary effect of our intelligence. We've had the long
*  lasting impact on the world, but maybe the entirety of physics in the universe has a very
*  long lasting effect. Sure. But you can also think of it like the wonderful life. What if you're not
*  here? Will somebody else do this? Is it something that you actually contributed because you had
*  something unique to compute? That's a pretty high bar though. Uniqueness. Yeah. So you have to be
*  Mozart or something to actually reach that level. Nobody would have developed that. But other people
*  might have solved this equation if you didn't do it. But also within limited scope. I mean,
*  during your lifetime or next year, you could contribute something that's unique that other
*  people did not see. And then that could change the way things move forward for a while. So I don't
*  think we have to be Mozart to be called intelligence, but we have this local effect that is changing.
*  If you weren't there, that would not have happened. And it's a positive effect. Of course,
*  you want it to be a positive effect. Do you think it's possible to engineer into computational
*  agents a fear of mortality? Does that make any sense? So there's a very trivial thing where
*  you could just code in a parameter, which is how long the life ends, but more of a fear of mortality.
*  Awareness of the way that things end and somehow encoding a complex representation
*  of that fear, which is like maybe as it gets closer, you become more terrified. I mean,
*  there seems to be something really profound about this fear that's not currently encodable
*  in a trivial way into our programs. Well, I think you're referring to the emotion of fear,
*  something because we have cognitively, we know that we have limited lifespan. And most of us cope
*  with it by just, hey, that's what the world is like. And I make the most of it. But sometimes
*  you can have a fear that's not healthy, that paralyzes you, that you can't do anything.
*  And somewhere in between there, not caring at all and getting paralyzed because of fear
*  is a normal response, which is a little bit more than just logic and it's emotion. So now the
*  question is what good are emotions? I mean, they are quite complex and there are multiple
*  dimensions of emotions and they probably do serve a survival function, heightened focus, for instance.
*  And fear of death might be a really good emotion when you are in danger, that you recognize it.
*  Even if it's not logically necessarily easy to derive and you don't have time for that logical
*  deduction, you may be able to recognize the situation is dangerous and this fear kicks in
*  and you all of a sudden perceive the facts that are important for that. And I think that generally
*  is the role of emotions. It allows you to focus what's relevant for your situation. And maybe
*  fear of death plays the same kind of role, but if it consumes you and it's something that you think
*  in normal life when you don't have to, then it's not healthy and then it's not productive.
*  Yeah, but it's fascinating to think how to incorporate emotion into a computational agent.
*  It almost seems like a silly statement to make, but it perhaps seems silly because we have such
*  a poor understanding of the mechanism of emotion, of fear. I think at the core of it
*  is another word that we know nothing about, but say a lot, which is consciousness.
*  Do you ever in your work or maybe on a coffee break, think about what the heck is this thing
*  consciousness and is it at all useful in our thinking about AI systems?
*  Yes, it is an important question. You can build representations and functions,
*  I think, into these agents that act like emotions and consciousness perhaps. So I mentioned
*  emotions being something that allows you to focus and pay attention, filter out what's important.
*  Yeah, you can have that kind of a filter mechanism and it puts you in a different state. Your
*  computation is in a different state. Certain things don't really get through and others
*  heightened. Now, you label that box emotion. I don't know if that means it's an emotion,
*  but it acts very much like we understand what emotions are. We actually did some work like that
*  modeling hyenas who were trying to steal a kill from lions, which happens in Africa. Hyenas are
*  quite intelligent, but not really intelligent. They have this behavior that's
*  more complex than anything else they do. They can band together if there's about 30 of them or so.
*  They can coordinate their effort so that they push the lions away from a kill, even though the lions
*  are so strong that they could kill a hyena by striking with a paw. But when they work together
*  and precisely time this attack, the lions will leave and they get the kill. And probably there
*  are some states like emotions that the hyenas go through. First, they call for reinforcements.
*  They really want that kill, but there's not enough of them, so they vocalize and there's more people,
*  more hyenas that come around. And then they have two emotions. They're very afraid of the lion,
*  so they want to stay away, but they also have a strong affiliation between each other. And then
*  this is the balance of the two emotions. And also, yes, they also want the kill. So it's both repelled
*  and attractive. But then this affiliation eventually is so strong that when they move,
*  they move together. They act as a unit and they can perform that function. So there's an interesting
*  behavior that seems to depend on these emotions strongly and makes it possible coordinate actions.
*  And I think a critical aspect of that, the way you're describing is emotion there is a
*  mechanism of social communication, of social interaction. Maybe humans won't even be
*  that intelligent or most things we think of as intelligent wouldn't be that intelligent without
*  the social component of interaction. Maybe much of our intelligence is essentially an outgrowth
*  of social interaction. And maybe for the creation of intelligent agents, we have to be creating
*  fundamentally social systems. Yes, I strongly believe that's true. And yes, the communication
*  is multifaceted. They vocalize and call for friends, but they also rub against each other
*  and they push and they do all kinds of destors and so on. So they don't act alone. And I don't
*  think people act alone very much either, at least normal most of the time. And social systems are so
*  strong for humans that I think we build everything on top of these kinds of structures. And
*  one interesting theory around that, Bickert's theory for instance for language, but language
*  origins is that where did language come from? And it's a plausible theory that first came
*  social systems, that you have different roles in a society. And then those roles are exchangeable,
*  that I scratch your back, you scratch my back, we can exchange roles. And once you have the brain
*  structures that allow you to understand actions in terms of roles that can be changed, that's the
*  basis for language, for grammar. And now you can start using symbols to refer to objects in the
*  world and you have this flexible structure. So there's a social structure that's fundamental
*  for language to develop. Now again, then you have language, you can refer to things that are not
*  here right now. And that allows you to then build all the good stuff about planning for instance,
*  and building things and so on. So yeah, I think that very strongly humans are social and that
*  gives us ability to structure the world. But also as a society, we can do so much more because
*  one person does not have to do everything. You can have different roles and together achieve a lot
*  more. And that's also something we see in computational simulations today. I mean,
*  we have multi-agent systems that can perform tasks. This fascinating demonstration, Marco
*  Dorico I think it was, these robots, little robots that had to navigate through an environment and
*  there were things that are dangerous, like maybe a big chasm or some kind of groove, a hole,
*  and they could not get across it. But if they grab each other with their gripper,
*  they formed a robot that was much longer than the team and this way they could get across that.
*  So this is a great example of how together we can achieve things we couldn't otherwise,
*  like the hyenas. You know, alone they couldn't, but as a team they could.
*  And I think humans do that all the time. We're really good at that.
*  Yeah. And the way you described the system of hyenas, it almost sounds algorithmic. Like the
*  problem with humans is they're so complex, it's hard to think of them as algorithms. But with
*  hyenas, it's simple enough to where it feels like, at least hopeful that it's possible to create
*  computational systems that mimic that. Yeah. That's exactly why we looked at that.
*  As opposed to humans. Like I said, they are intelligent,
*  but they are not quite as intelligent as say baboons, which would learn a lot and would be
*  much more flexible. Hyenas are relatively rigid in what they can do. And therefore you could look
*  at this behavior like this is a breakthrough in evolution about to happen. That they've discovered
*  something about social structures, communication, about cooperation, and it might then spill over
*  to other things too in thousands of years in the future. Yeah. I think the problem with baboons and
*  humans is probably too much is going on inside the head where we won't be able to measure it if we're
*  observing the system. With hyenas, it's probably easier to observe the actual decision making and
*  the various motivations that are involved. Yeah. They are visible. And we can even quantify
*  possibly their emotional state because they leave droppings behind. And there are chemicals there
*  that can be associated with neurotransmitters. And we can separate what emotions they might have
*  experienced in the last 24 hours. Yeah. What to you is the most beautiful, speaking of hyenas,
*  what to you is the most beautiful nature inspired algorithm in your work that you've come across
*  something maybe earlier on in your work or maybe today? I think it's evolution computation is
*  the most amazing method. So what fascinates me most is that with computers is that you can
*  get more out than you put in. I mean, you can write a piece of code and your machine does what you
*  told it. I mean, this happened to me in my freshman year. It did something very simple and I was just
*  amazed. I was blown away that it would get the number and it would compute the result and I
*  didn't have to do it myself. Very simple. But if you push that a little further, you can have
*  machines that learn and they might learn patterns. And already say deep learning neural networks,
*  they can learn to recognize objects, sounds, patterns that humans have trouble with. And
*  sometimes they do it better than humans. And that's so fascinating. And now if you take that one more
*  step, you get something like evolutionary algorithms that discover things, they create things,
*  they come up with solutions that you did not think of. And that just blows me away. It's so
*  great that we can build systems, algorithms that can be in some sense smarter than we are, that they
*  can discover solutions that we might miss. A lot of times it is because we have as humans,
*  we have certain biases, we expect the solutions to be certain way and you don't put those biases
*  into the algorithm. So they are more free to explore and evolution is just absolutely fantastic
*  explorer. And that's what really is fascinating. Yeah, I think I get made fun of a bit because I
*  currently don't have any kids. But you mentioned programs. I mean, do you have kids? Yeah. So
*  maybe you could speak to this. But there's a magic to the creation of creative process. Like I
*  with spot the Boston Dynamics spot, but really any robot that I've ever worked on,
*  it just feels like the similar kind of joy I imagine I would have as a father,
*  not the same perhaps level, but like the same kind of wonderment, like that exactly this,
*  which is like, you know what you had to do initially to get this thing going.
*  Let's speak on the computer science side, like what the program looks like. But something about
*  it doing more than what the program was written on paper is like, that somehow connects to the
*  magic of this entire universe. Like that's, that's like, I feel like I found God every time I like,
*  it's like, because you've really created something that's living. Yeah. Even if it's a
*  simple program. It has a life of its own, has the intelligence of its own. It's beyond what you
*  actually thought. Yeah. And that is, I think it's exactly spot on. That's exactly what it's about.
*  You created something and has a ability to live its life and do good things. And you just gave
*  it a starting point. So in that sense, I think it's, that may be part of the joy actually.
*  Yeah. But you mentioned creativity in this context, especially in the context of evolutionary
*  computation. So, you know, we don't often think of algorithms as creative. So how do you think
*  about creativity? Yeah. Algorithms absolutely can be creative. They can come up with solutions that
*  you don't think about. I mean, creativity can be defined. A couple of requirements have to,
*  has to be new. It has to be useful and it has to be surprising. And those certainly are true with
*  evolutionary computation discovering solutions. So maybe an example, for instance, we did
*  this collaboration with MIT Media Lab, Caleb Harvest Lab, where they had a hydroponic
*  food computer, they called it, environment that was completely computer controlled,
*  nutrients, water, light, temperature, everything is controlled. Now, what do you do if you can
*  control everything? Farmers know a lot about how to do, how to make plants grow in their own
*  patch of land. But if you can control everything, it's too much. And it turns out that we don't
*  actually know very much about it. So we built a system, evolutionary optimization system,
*  together with a surrogate model of how plants grow and let this system explore recipes on its own.
*  And initially we were focusing on light, how strong, what wavelengths, how long the light was on.
*  And we put some boundaries, which we thought were reasonable, for instance, that there was
*  at least six hours of darkness like night, because that's what we have in the world.
*  And very quickly, the system evolution pushed all the recipes to that limit.
*  We were trying to grow basil and we had initially had some 200, 300 recipes, exploration as well as
*  known recipes, but now we are going beyond that and everything was like pushed at that limit. So
*  we look at it and say, well, we can easily just change it, let's have it your way. And it turns
*  out the system discovered that basil does not need to sleep. 24 hours, lights on and it will
*  thrive. It will be bigger, it will be tastier. And this was a big surprise, not just to us,
*  but also the biologist in the team that anticipated that there are some constraints that are in the
*  world for a reason. It turns out that evolution did not have the same bias and therefore it
*  discovered something that was creative. It was surprising, it was useful and it was new.
*  That's fascinating to think about, like the things we think that are fundamental to living
*  systems on earth today, whether they're actually fundamental or they somehow shape, fit the
*  constraints of the system. And all we have to do is just remove the constraints. Do you ever think
*  about, I don't know how much you know about brain computer interfaces in Neuralink. The idea there
*  is our brains are very limited. And if we just allow, we plug in, we provide a mechanism for
*  a computer to speak with the brain. So you're thereby expanding the computational power of the
*  brain. The possibilities there, sort of from a very high, low philosophical perspective,
*  is limitless. But I wonder how limitless it is. Are the constraints we have, like features that
*  are fundamental to our intelligence? Or is this just like this weird constraint in terms of our
*  brain size and skull and lifespan and senses? It's just the weird little like a quirk of evolution.
*  And if we just open that up, like add much more senses, add much more computational power,
*  the intelligence will expand exponentially. Do you have a sense about constraints
*  the relationship of evolution computation to the constraints of the environment?
*  Well, at first I'd like to comment on that, like changing the inputs to human brain.
*  Yes, that would be great.
*  Flexibility of the brain. I think there's a lot of that. There are experiments that are done in
*  animals like Mikanga Sur, at MIT, switching the auditory and visual information, going to the
*  wrong part of the cortex, and the animal was still able to hear and perceive the visual
*  environment. And there are kids that are born with severe disorders and sometimes they have to remove
*  half of the brain, like one half, and they still grow up. They have the functions migrate to the
*  other parts. There's a lot of flexibility like that. So I think it's quite possible to
*  hook up the brain with different kinds of sensors, for instance, and something that we don't even
*  understand or have today, different kinds of wavelengths or whatever they are. And then the
*  brain can learn to make sense of it. And that I think is this good hope that these prosthetic
*  devices, for instance, work, not because we make them so good and so easy to use, but the brain
*  adapts to them and can learn to take advantage of them. And so in that sense, if there's a trouble,
*  a problem, I think the brain can be used to correct it. Now going beyond what we have today,
*  can you get smarter? That's really much harder to do. Giving the brain more input probably might
*  overwhelm it. It would have to learn to filter it and focus in order to use the information
*  effectively. And augmenting intelligence with some kind of external devices like that
*  might be difficult, I think. But replacing what's lost, I think, is quite possible.
*  Right. So our intuition allows us to sort of imagine that we can replace what's been lost,
*  but expansion beyond what we have. I mean, we are already one of the most, if not the most,
*  intelligent things on this earth, right? So it's hard to imagine if the brain can hold up with an
*  order of magnitude greater set of information thrown at it, if it can reason through that.
*  Part of me, this is the Russian thing, I think, is I tend to think that the limitations is where the
*  superpower is. That immortality and huge increase in bandwidth of information by connecting
*  computers with the brain is not going to produce greater intelligence. It might produce lesser
*  intelligence. So I don't know. There's something about the scarcity being essential to fitness or
*  performance, but that could be just because we're so limited.
*  No, exactly. You make do with what you have. But you don't have to pipe it directly to the brain.
*  We already have devices like phones where we can look up information at any point. And that can
*  make us more productive. You don't have to argue about what happened in that baseball game or
*  whatever it is, because you can look it up right away. And I think in that sense, we can learn to
*  utilize tools. And that's what we have been doing for a long, long time. And the brain is already
*  drinking from the fire hose, like vision. There's way more information in vision than we actually
*  process. So brain is already good at identifying what matters. And we can switch that from vision
*  to some other wavelength or some other kind of modality. But I think that the same
*  processing principles probably still apply. But also indeed this ability to have information more
*  accessible and more relevant, I think can enhance what we do. I mean, kids today at school, they
*  learn about DNA. I mean, things that were discovered just a couple of years ago,
*  it's already common knowledge, and we are building on it. And we don't see a problem where
*  there's too much information that we can absorb and learn. Maybe people become a little bit more
*  narrow in what they know. They are in one field. But this information that we have accumulated,
*  it is passed on, and people are picking up on it. And they are building on it. So it's not like we
*  have reached the point of saturation. We have still this process that allows us to be selective
*  and decide what's interesting, I think still works, even with the more information we have today.
*  Yeah, it's fascinating to think about Wikipedia becoming a sensor. So the firehose of information
*  from Wikipedia, so it's like you integrated directly into the brain the way you're thinking.
*  You're observing the world with all of Wikipedia directly piping into your brain.
*  So when I see a light, I immediately have the history of who invented electricity
*  integrated very quickly into. So just the way you think about the world might be very interesting
*  if you can integrate that kind of information. What are your thoughts, if I could ask,
*  early steps on the Neuralink side? I don't know if you got a chance to see, but
*  there was a monkey playing pong through the brain computer interface. And the dream there is
*  sort of you're already replacing the thumbs essentially that you would use to play a video
*  game. The dream is to be able to increase further the interface by which you interact with the
*  computer. Are you impressed by this? Are you worried about this? What are your thoughts as a human?
*  I think it's wonderful. I think it's great that we could do something like that. There are devices
*  that read your EEG, for instance, and humans can learn to control things using just their thoughts
*  in that sense. And I don't think it's that different. I mean, those signals would go to limbs,
*  they would go to thumbs. Now, the same signals go through a sensor to some computing system.
*  It still probably has to be built on human terms, not to overwhelm them, but utilize what's there
*  and sense the right kind of patterns that are easy to generate. But, oh, that I think is really
*  quite possible and wonderful and could be very much more efficient. So you mentioned surprising
*  being a characteristic of creativity. You already mentioned a few examples, but is there something
*  that jumps out at you as was particularly surprising from the various evolutionary
*  computation systems you've worked on, the solutions that come up along the way, not necessarily the
*  final solutions, but maybe things that would even discarded? Is there something that just jumps
*  to mind? It happens all the time. I mean, evolution is so creative, so good at discovering
*  solutions you don't anticipate. A lot of times they are taking advantage of something that you
*  didn't think was there, like a bug in the software. There's a great paper, the community put it
*  together about surprising anecdotes about evolutionary computation. A lot of them are indeed
*  in some software environment, there was a loophole or a bug and the system utilizes that.
*  By the way, for people who want to read, it's kind of fun to read. It's called the surprising
*  creativity of digital evolution, a collection of anecdotes from the evolutionary computation
*  and artificial life research communities. And there's just a bunch of stories from all the
*  seminal figures in this community. You have a story in there that released to you at least on
*  the tic-tac-toe memory bomb. So can you, I guess, describe that situation if you think that's...
*  Yeah, that's a quite a bit smaller scale than our, basically doesn't need to sleep, surprise. But
*  it was actually done by students in my class, in a neural nets evolution computation class.
*  There was an assignment, it was perhaps the final project where people built
*  game playing AI, it was an AI class. And it was for tic-tac-toe or five in a row in a large board.
*  And this one team evolved a neural network to make these moves. And they set it up,
*  the evolution. They didn't really know what would come out. But it turned out that they
*  did really well. Evolution actually won the tournament. And most of the time when it won,
*  it won because the other teams crashed. And then when we look at it, what was going on
*  was that evolution discovered that if it makes a move that's really, really far away, like
*  millions of squares away, the other teams, the other programs just expanded memory in order to
*  take that into account until they ran out of memory and crashed. And then you win a tournament
*  by crashing all your opponents. I think that's quite a profound example, which probably applies
*  to most games from even a game theoretic perspective, that sometimes to win, you don't
*  have to be better within the rules of the game. You have to come up with ways to break your
*  opponent's brain, if it's a human. Not through violence, but through some hack where the brain
*  just is not... You're basically, how would you put it? You're going outside the constraints of where
*  the brain is able to function. Yeah, expectations of your opponent. I mean, this was even Kasparov
*  pointed out that when Deep Blue was playing against Kasparov, that it was not playing the same way as
*  Kasparov expected. And this has to do with not having the same biases. And that's really one of
*  the strengths of the AI approach. Can you at a high level say, what are the basic mechanisms of
*  evolutionary computation algorithms that use something that could be called an evolutionary
*  approach? Like how does it work? What are the connections to the... What are the echoes of the
*  connection to his biological... A lot of these algorithms really do take motivation from biology,
*  but they are caricatures. You try to essentialize it and take the elements that you believe matter.
*  So in evolutionary computation, it is the creation of variation and then the selection upon that.
*  So the creation of variation, you have to have some mechanism that allow you to create new
*  individuals that are very different from what you already have. That's the creativity part.
*  And then you have to have some way of measuring how well they are doing and using that measure to
*  select who goes to the next generation and you continue. So first you also have to have some
*  kind of digital representation of an individual that can be then modified. So I guess humans
*  in biological systems have DNA and all those kinds of things. You have to have similar kind of
*  encodings in a computer program. Yes. And that is a big question. How do you encode these individuals?
*  So there's a genotype, which is that encoding and then a decoding mechanism gives you the phenotype,
*  which is the actual individual that then performs the task in an environment,
*  can be evaluated how good it is. So even that mapping is a big question. And how do you do it?
*  But typically the representations are either they are strings of numbers or they are some kind of
*  trees. Those are something that we know very well in computer science and we try to do that. But
*  and DNA in some sense is also a sequence and it's a string. So it's not that far from it, but
*  DNA also has many other aspects that we don't take into account necessarily like this folding and
*  interactions that are other than just the sequence itself. And lots of that is not yet captured and
*  we don't know whether they are really crucial. Evolution, biological evolution has produced
*  wonderful things. But if you look at them, it's not necessarily the case that every piece
*  is irreplaceable and essential. There's a lot of baggage because you have to construct it and it
*  has to go through various stages. And we still have appendix and we have tailbones and things
*  like that that are not really that useful. If you try to explain them now, it would make no sense,
*  very hard. But if you think of us as productive evolution, you can see where they came from. They
*  were useful at one point perhaps and no longer are, but they're still there. So that process is
*  complex and your representation should support it. And that is quite difficult if we are limited
*  with strings or trees and then we are pretty much limited what can be constructed. And one thing that
*  we are still missing in evolutionary computation in particular is what we saw in biology, major
*  transitions. So that you go from, for instance, single cell to multi-cell organisms and eventually
*  societies. There are transitions of level of selection and level of what a unit is. And that's
*  something we haven't captured in evolutionary computation yet. Does that require a dramatic
*  expansion of the representation? Is that what that is? Most likely it does, but we don't even
*  understand it in biology very well where it's coming from. So it would be really good to look at
*  major transitions in biology, try to characterize them a little bit more in detail what the processes
*  are. So like a unit, a cell is no longer evaluated alone, it's evaluated as part of a community,
*  organism. Even though it could reproduce, now it can't alone. It has to have this environment.
*  So there's a push to another level, at least the selection. And how do you make that jump to the
*  next level? How do you make the jump? As part of the algorithm. Yeah. So we haven't really seen that
*  in computation yet. And there are certainly attempts to have open-ended evolution, things that
*  could add more complexity and start selecting at a higher level, but it is still not
*  quite the same as going from single to multi to society, for instance, in biology.
*  So there essentially would be, as opposed to having one agent, those agent all of a sudden
*  spontaneously decide to then be together. And then your entire system would then be treating them as
*  one agent. Something like that. Some kind of weird merger. But also, I think you mentioned
*  selection. So basically there's an agent and they don't get to live on if they don't do well. So
*  there's some kind of measure of what doing well is and isn't. And does mutation come into play at
*  all in the process and what the world does it serve? Yeah. So again, back to what the computational
*  mechanisms of evolution computation are. So the way to create variation, you can take multiple
*  individuals, two usually, but you could do more. And you exchange the parts of the representation.
*  You do some kind of recombination. It could be crossover, for instance. In biology, you do have
*  DNA strings that are cut and put together again. We could do something like that. And it seems to
*  be that in biology, the crossover is really the workhorse in biological evolution. In computation,
*  we tend to rely more on mutation. And that is making random changes into parts of the chromosome.
*  You could try to be intelligent and target certain areas of it and make the mutations also
*  follow some principle. Like you collect statistics of performance and correlations
*  and try to make mutations you believe are going to be helpful. That's where evolution
*  computation has moved in the last 20 years. Evolution computation has been around for 50
*  years, but a lot of the recent- Success comes from mutation.
*  Comes from using statistics. It's like the rest of machine learning based on statistics. We use
*  similar tools to guide evolution computation. And in that sense, it has diverged a bit from biological
*  evolution. And that's one of the things I think we could look at again, having a weaker selection,
*  more crossover, large populations, more time, and maybe a different kind of creativity would
*  come out of it. We are very impatient in evolution computation today. We want answers right now,
*  quickly. And if somebody doesn't perform, kill it. And biological evolution doesn't work quite
*  that way. More patient. Yes, much more patient. So I guess we need to add some kind of mating,
*  some kind of dating mechanisms, like marriage maybe in there, into our algorithms to improve
*  the combination mechanism as opposed to mutation doing all of the work. Yeah, and many ways of
*  being successful. Usually in evolution computation, we have one goal, play this game really well
*  and compare to others. But in biology, there are many ways of being successful. You can build
*  niches. You can be stronger, faster, larger, or smarter, or eat this or eat that. So there are
*  many ways to solve the same problem of survival. And that then breeds creativity. And it allows
*  more exploration. And eventually you get solutions that are perhaps more creative.
*  Rather than trying to go from initial population directly or more or less directly to your
*  maximum fitness, which you measure, that's just one metric. So in a broad sense,
*  before we talk about newer evolution, do you see evolutionary computation as more effective than
*  deep learning in a certain context? Machine learning, broadly speaking, maybe even supervised
*  machine learning. I don't know if you want to draw any kind of lines and distinctions and
*  borders where they rub up against each other kind of thing, where one is more effective than the
*  other in the current state of things. Yes, of course, they are very different and they
*  address different kinds of problems. And the deep learning has been really successful in domains
*  where we have a lot of data. And that means not just data about situations, but also what the
*  right answers were. So labeled examples. Or there might be predictions, maybe weather prediction,
*  where the data itself becomes labeled, what happened, what the weather was today and what
*  will be tomorrow. So they are very effective deep learning methods on that kind of tasks.
*  But there are other kinds of tasks where we don't really know what the right answer is.
*  Game playing, for instance, but many robotics tasks and actions in the world, decision making,
*  and actual practical applications like treatments and healthcare or investment in stock market.
*  Many tasks are like that. We don't know and we'll never know what the optimal answers were.
*  And there you need different kinds of approaches. Reinforcement learning is one of those.
*  Reinforcement learning comes from biology as well. Agents learn during their lifetime. They
*  bury and sometimes they get sick and then they don't and get stronger. And then that's how you
*  learn. And evolution is also a mechanism like that by the different time scale because you
*  have a population. Not an individual during its lifetime, but an entire population as a whole can
*  discover what works. And there you can afford individuals that don't work out. Everybody
*  dies and you have a next generation and it will be better than the previous one. So that's the
*  big difference between these methods. They apply to different kinds of problems. And in particular,
*  there's often a comparison that's kind of interesting and important between reinforcement
*  learning and evolutionary computation. And initially reinforcement learning was about
*  individual learning during their lifetime and evolution is more engineering. You don't care
*  about the lifetime. You don't care about all the individuals that are tested. You only care about
*  the final result, the last one, the best candidate that evolution produced. In that sense,
*  they also apply to different kinds of problems. Now that boundary is starting to blur a bit. You
*  can use evolution as an online method and reinforcement learning to create engineering
*  solutions, but that's still roughly the distinction. And from the point of view of what algorithm you
*  want to use, if you have something where there is a cost for every trial, reinforcement learning
*  might be your choice. Now, if you have a domain where you can use a surrogate perhaps, so you
*  don't have much of a cost for trial and you want to have surprises, you want to explore more broadly,
*  then this population-based method is perhaps a better choice because you can try things out
*  that you wouldn't afford when you're doing reinforcement learning. There's very few things
*  as entertaining as watching either evolutionary computation or reinforcement learning, teaching
*  a simulated robot to walk. Maybe there's a higher level question that could be asked here, but
*  do you find this whole space of applications in the robotics interesting for evolutionary computation?
*  Yeah, very much. And indeed, there are fascinating videos of that. And that's actually one of the
*  examples where you can contrast the difference. Between reinforcement learning and evolution.
*  Yes. So if you have a reinforcement learning agent, it tries to be conservative because it
*  wants to walk as long as possible and be stable. But if you have evolutionary computation, it can
*  afford these agents that go haywire. They fall flat on their face and they could take a step and
*  then they jump and then again fall flat. And eventually what comes out of that is something
*  like a falling that's controlled. You take another step and another step and you no longer fall.
*  Instead, you run, you go fast. So that's a way of discovering something that's hard to discover
*  step by step incrementally because you can afford these evolutionists dead ends, although they are
*  not entirely dead ends in the sense that they can serve as stepping stones. When you take two of
*  those, put them together, you get something that works even better. And that is a great example of
*  this kind of discovery. Yeah, learning to walk is fascinating. I talked quite a bit to Ross
*  Stedrick, MIT. There's a community of folks who just roboticists who love the elegance and beauty of
*  movement and of walking by pedo robotics is beautiful, but also exceptionally dangerous
*  in the sense that you're constantly falling essentially if you want to do elegant movement.
*  And the discovery of that is such a good example of that the discovery of a good solution
*  sometimes requires a leap of faith and patience and all those kinds of things.
*  I wonder what other spaces where you have to discover those kinds of things in.
*  Yeah. Another interesting direction is learning for virtual creatures learning to walk. We did a study
*  in simulation obviously that you create those creatures, not just their controller, but also
*  their body. So you have cylinders, you have muscles, you have joints and sensors, and you're
*  creating creatures that look quite different. Some of them have multiple legs, some of them have no
*  legs at all. And then the goal was to get them to move, to walk, to run. And what was interesting is
*  that when you evolve the controller together with the body, you get movements that look natural
*  because they're optimized for that physical setup. And these creatures, you start believing
*  them that they're alive because they walk in a way that you would expect somebody with that kind
*  of a setup to walk. Yeah. There's something subjective also about that, right? I've been
*  thinking a lot about that, especially in the human robot interaction context. I mentioned Spot,
*  the Boston Dynamics robot. There is something about human robot communication. Let's say,
*  let's put it in another context, something about human and dog context, like a living dog,
*  where there's a dance of communication. First of all, the eyes, you both look at the same thing,
*  and the dogs communicate with their eyes as well. If you and a dog want to
*  deal with a particular object, the dog will look at you and then look at the object and look back
*  at you, all those kinds of things. But there's also just the elegance of movement. There's the,
*  of course, the tail and all those kinds of mechanisms of communication. It all seems natural
*  and often joyful. And for robots to communicate that, it's really difficult how to figure that
*  out because it almost seems impossible to hard code in. You can hard code it for demo purpose,
*  something like that, but it's essentially choreographed. If you watch some of the
*  Boston Dynamics videos where they're dancing, all of that is choreographed by human beings.
*  But to learn how to, with your movement, demonstrate a naturalness and elegance,
*  that's fascinating. Of course, in the physical space, that's very difficult to do, to learn
*  the kind of scale that you're referring to. But the hope is that you could do that in simulation
*  and then transfer it into the physical space if you're able to model the robots efficiently,
*  naturally. Yeah. And sometimes I think that it requires a theory of mind on the side of the
*  robot that they understand what you're doing because they themselves are doing something
*  similar. That's a big question too. We talked about intelligence in general and the social
*  aspect of intelligence. And I think that's what is required that we humans understand other humans
*  because we assume that they are similar to us. We have one simulation we did a while ago, Ken
*  Stanley did that. Two robots that were competing, simulation, like I said, they were foraging for
*  food to gain energy. And then when they were really strong, they would bounce into the other
*  robot and win if they were stronger. And we watched evolution discover more and more complex
*  behaviors. They first went to the nearest food and then they started to plot a trajectory so they
*  get more. But then they started to pay attention to what the other robot was doing. And in the end,
*  there was a behavior where one of the robots, the most sophisticated one, sensed where the food
*  pieces were and identified that the other robot was close to two of a very far distance. And there
*  was one more food nearby. So it faked, now I'm using anthropomorphized terms, but it made a move
*  towards those other pieces in order for the other robot to actually go and get them. Because it knew
*  that the last remaining piece of food was close and the other robot would have to travel a long
*  way, lose its energy, and then lose the whole competition. So there was an emergence of
*  something like a theory of mind, knowing what the other robot would do to guide it towards bad
*  behavior in order to win. So we can get things like that happen in simulation as well.
*  But that's a complete natural emergence of a theory of mind. But I feel like if you add a little bit
*  of a place for a theory of mind to emerge easier, then you can go really far. I mean,
*  some of these things with evolution, you add a little bit of design in there, it'll really help.
*  And I tend to think that a very simple theory of mind will go a really long way for cooperation
*  between agents and certainly for human-robot interaction. It doesn't have to be super
*  complicated. I've gotten a chance in the autonomous vehicle space to watch
*  vehicles interact with pedestrians or pedestrians interacting with vehicles in general.
*  I mean, you would think that there's a very complicated theory of mind thing going on,
*  but I have a sense it's not well understood yet, but I have a sense it's pretty dumb.
*  Like it's pretty simple. There's a social contract there between humans, a human driver,
*  and a human crossing the road where the human crossing the road trusts that the human in the
*  car is not going to murder them. And there's something about, again, back to that mortality
*  thing, there's some dance of ethics and morality that's built in. You're mapping your own morality
*  onto the person in the car. And even if they're driving at a speed where you think if they don't
*  stop, they're going to kill you, you trust that if you step in front of them, they're going to hit
*  the brakes. And there's that weird dance that we do that I think is a pretty simple model.
*  But of course, it's very difficult to introspect what it is. And autonomous robots in the human-robot
*  interaction context have to have to build that. Current robots are much less than what you're
*  describing. They're currently just afraid of everything. They're not the kind that fall
*  and discover how to run. They're more like, please don't touch anything. Don't hurt anything.
*  Stay as far away from humans as possible. Treat humans as ballistic objects that you can't,
*  that you do with a large spatial envelope. Make sure you do not collide with. That's how like
*  mentioned Elon Musk thinks about autonomous vehicles. I tend to think autonomous vehicles
*  need to have a beautiful dance between human and machine, where it's not just the collision
*  avoidance problem, but a weird dance. Yeah, I think these systems need to be able to predict
*  what will happen, what the other agent is going to do, and then have a structure of what the goals
*  are and whether those predictions actually meet the goals. And you can go probably pretty far with
*  that relatively simple setup already. But to call it a theory of mind, I don't think you need to.
*  It doesn't matter whether the pedestrian has a mind. It's an object. And we can predict what
*  we will do. And then we can predict what the states will be in the future and whether they
*  are desirable states. Stay away from those that are undesirable and go towards those that are
*  desirable. So it's a relatively simple, functional approach to that. Where do we really need the
*  theory of mind? Maybe when you start interacting and you're trying to get the other agent to do
*  something and jointly so that you can jointly collaboratively achieve something, then it becomes
*  more complex. Well, I mean, even with the pedestrians, you have to have a sense of where
*  their attention, actual attention in terms of their gaze is, but also like, there's this vision
*  science people talk about this all the time. Just because I'm looking at it doesn't mean I'm paying
*  attention to it. So figuring out what is the person looking at? What is the sensory information
*  they've taken in? And the theory of mind piece comes in is what are they actually attending to
*  cognitively? And also what are they thinking about? Like what is the computation they're
*  performing? And you have, you have probably maybe a few options, you know, for the pedestrian
*  crossing. It doesn't have to be, it's like a variable with a few discrete states, but you have
*  to have a good estimation of which of the states that brain is in for the pedestrian case. And the
*  same is for attending with a robot. If you're collaborating to pick up an object, you have to
*  figure out is the human like, like there's a few discrete states that the human could be in and you
*  have to, you have to predict that by observing the human. And that seems like a machine learning
*  problem to figure out what's how the human is, what's the human up to. It's not as simple as
*  sort of planning just because they move their arm means the arm will continue moving in this
*  direction. You have to, you have to really have a model of what they're thinking about and what's
*  motivation behind the movement of the arm. And here we are talking about relatively simple
*  physical actions, but you can take that to higher levels also, like to predict what the people are
*  going to do, you need to know what their goals are. What are they trying to, are they exercising?
*  They're starting to get somewhere. But even, even higher level, I mean, you are predicting what
*  people will do in their career, what their life themes are, do they want to be famous, rich or
*  do good. And that takes a lot more information, but it allows you to then predict their actions,
*  what choices they might make. So how does evolution computation apply to the world of
*  neural networks? Cause I've seen quite a bit of work from you and others on the, in the world of
*  neuro evolution. So maybe first, can you say what is this field? Yeah. Neuro evolution is a
*  combination of neural networks and evolution computation in many different forms, but the
*  early versions were simply using evolution as a way to construct a neural network instead of say,
*  stochastic gradient descent or backpropagation. Because evolution can evolve these parameters,
*  weight values in a neural network, just like any other string of numbers, you can, you can do that.
*  And that's useful because some cases you don't have those targets that you need to backpropagate
*  from. And it might be an agent that's running a maze or a robot playing a game or something.
*  You don't, again, you don't know what the right answer size, you don't have backup, but this way
*  you can still evolve a neural net. And neural networks are really good at these tasks because
*  they, they recognize patterns and they generalize interpolate between known situations. So you want
*  to have a neural network in such a task, even if you don't have a supervised targets. So that's
*  the reason and that's a solution. And also more recently, now when we have all this deep learning
*  literature, it turns out that we can use evolution to optimize many aspects of those designs.
*  The deep learning architectures have become so complex that there's little hope for as little
*  humans to understand their complexity and what actually makes a good design. And now we can use
*  evolution to give that design for you. And it might be mean optimizing hyperparameters, like the depth
*  of layers and so on, or the topology of the network, how many layers, how they're connected,
*  but also other aspects like what activation functions you use, where in the network during
*  the learning process, or what loss function you use, you can generate that, generate that.
*  Even data augmentation, all the different aspects of the design of deep learning experiments could
*  be optimized that way. So that's an interaction between two mechanisms. But there's also,
*  when we get more into cognitive science and the topics that we've been talking about,
*  you could have learning mechanisms at two level timescales. So you do have an evolution that gives
*  you baby neural networks that then learn during their lifetime. And you have this interaction of
*  two timescales. And I think that can potentially be really powerful. Now, in biology, we are not
*  born with all our faculties. We have to learn. We have a developmental period. In humans, it's
*  really long. And most animals have something. And probably the reason is that evolution,
*  the DNA is not detailed enough or plentiful enough to describe them. We can't describe how to set the
*  brain up. But evolution can decide on a starting point and then have a learning algorithm that
*  will construct the final product. And this interaction of intelligent, well, evolution
*  that has produced a good starting point for the specific purpose of learning from it,
*  with the interaction with the environment, that can be a really powerful mechanism for
*  constructing brains and constructing behaviors. I like how you walk back from intelligence. So
*  optimize the starting point maybe. Yeah. Okay. There's a lot of fascinating things to ask here.
*  And this is basically this dance between neural networks and evolution and computation could go
*  into the category of automated machine learning to where you're optimizing whether it's hyperparameters
*  of the topology or hyperparameters taken broadly. But the topology thing is really interesting. I
*  mean, that's not really done that effectively or throughout the history of machine learning has not
*  been done. Usually there's a fixed architecture. Maybe there's a few components you're playing with,
*  but to grow a neural network, essentially the way you grow in their organisms, really fascinating
*  space. How hard is it? Do you think to grow a neural network and maybe what kind of neural
*  networks are more amenable to this kind of idea than others? I've seen quite a bit of work on
*  recurrent neural networks. Is there some architectures that are friendlier than others? And is this just
*  a fun, small scale set of experiments or do you have hope that we can be able to grow
*  powerful neural networks? I think we can. And most of the work up to now is taking
*  architectures that already exist that humans have designed and try to optimize them further.
*  And you can totally do that. A few years ago, we did an experiment. We took a winner of the
*  image captioning competition and the architecture and just broke it into pieces and took the pieces.
*  And that was our search base. See if you can do better. And we indeed could. 15% better
*  performance by just searching around the network design that humans had come up with, or venials
*  and others. But that's starting from a point that humans have produced. But we could
*  do something more general. It doesn't have to be that kind of network.
*  The hard part is just a couple of challenges. One of them is to define the search base. What are
*  your elements and how you put them together? And the space is just really, really big.
*  So you have to somehow constrain it and have some hunch of what will work,
*  because otherwise everything is possible. And another challenge is that in order to evaluate
*  how good your design is, you have to train it. You have to actually try it out. And that's
*  currently very expensive. Deep learning networks may take days to train. Well,
*  imagine having a population of 100 and have to run it for 100 generations. It's not yet quite
*  feasible computationally. It will be, but also there's a large carbon footprint and all that.
*  We are using a lot of computation for doing it. So intelligent methods. And intelligence,
*  we have to do some science in order to figure out what the right representations are
*  and right operators are and how do we evaluate them without having to fully train them. And
*  that is where the current research is. And we're making progress on all those fronts.
*  So yes, there are certain architectures that are more amenable to that approach. But also I think
*  we can create our own architecture and all representations that are even better at that.
*  Do you think it's possible to do like a tiny baby network that grows into something that can do
*  state of the art and like even the simple data set, like MNIST, it just grows into a gigantic
*  monster that's the world's greatest handwriting recognition system?
*  Yeah, there are approaches like that. Esteban Real and Coquille, for instance, have worked on
*  evolving a smaller network and then systematically expanding it to a larger one.
*  Your elements are already there and scaling it up will just give you more power. So again,
*  evolution gives you that starting point. And then there's a mechanism that gives you the final
*  result and a very powerful approach. But you could also simulate the actual growth process.
*  And like I said before, evolving a starting point and then training the network,
*  there's not that much work that's been done on that yet. We need some kind of a simulation
*  environment so there are interactions at will. The supervised environment, it's not as easily
*  usable here. Sorry, the interaction between neural networks?
*  Yeah, the neural networks that you're creating, interacting with the world,
*  and learning from these sequences of interactions, perhaps communication with others.
*  That's awesome.
*  We would like to get there, but just the task of simulating something at that level is very hard.
*  It's very difficult. I love the idea. I mean, one of the powerful things about evolution on Earth is
*  predators and prey emerged. There's bigger fish and smaller fish and it's fascinating to think
*  that you could have neural networks competing against each other, one neural network being able
*  to destroy another one. There's wars of neural networks competing to solve the MNIST problem.
*  And we actually simulated also that prey. And it was interesting what happened there.
*  Padminarajik Pallan did this and K. Holkamp was a zoologist. So we had, again,
*  we had simulated hyenas and simulated zebras. And initially, the hyenas just tried to hunt them. And
*  when they actually stumbled upon the zebra, they ate it and were happy. And then the zebras learned
*  to escape and the hyenas learned to team up. And actually, two of them approached in different
*  directions. And now the zebras, then next step, they generated a behavior where they split in
*  different directions, just like actually gazelles do when they are being hunted. They confuse the
*  predator by going in different directions. That emerged. And then more hyenas joined and kind of
*  circled them. And then when they circled them, they could actually herd the zebras together and
*  eat multiple zebras. So there was like an arms race of predators and prey, and they gradually
*  developed more complex behaviors, some of which we actually do see in nature. And this kind of
*  coevolution, that's competitive coevolution, it's a fascinating topic because there's a promise or
*  possibility that you will discover something new that you don't already know. You didn't build it
*  in. It came from this arms race. It's hard to keep the arms race going. It's hard to have
*  rich enough simulation that supports all of these complex behaviors. But at least for several steps,
*  we've already seen it in this predator prey scenario. Yeah.
*  First of all, it's fascinating to think about this context in terms of evolving architectures.
*  So I've studied Tesla Autopilot for a long time. It's one particular implementation
*  of an AI system that's operating in the real world. I find it fascinating because of the scale at
*  which it's used out in the real world. And I'm not sure if you're familiar with that system much,
*  but you know, Andre Capati leads that team on the machine learning side. And there's a multi-task
*  network, multi-headed network where there's a core, but it's trained on particular tasks.
*  And there's a bunch of different heads that are trained on that. Is there some lessons from
*  evolutionary computation or neuroevolution that could be applied to this kind of multi-headed
*  beast that's operating in the real world? Yes. It's a very good problem for neuroevolution.
*  And the reason is that when you have multiple tasks, they support each other. So let's say you're
*  learning to classify x-ray images to different pathologies. So you have one task is to classify
*  this disease and another one, this disease, another one, this one. And when you're learning
*  from one disease, that forces certain kinds of internal representations and embeddings.
*  And they can serve as a helpful starting point for the other tasks. So you are combining the
*  wisdom of multiple tasks into these representations. And it turns out that you can do better in each of
*  these tasks when you are learning simultaneously other tasks than you would by one task alone.
*  Which is a fascinating idea in itself. Yeah.
*  Yes. And people do that all the time. I mean, you use knowledge of domains that you know
*  in new domains. And certainly neural networks can do that. Where neuroevolution comes in is that
*  what's the best way to combine these tasks? Now there's architectural design that allows you to
*  decide where and how the embeddings, the internal representations are combined and how much you
*  combine them. And there's quite a bit of research on that. And my team, Elliot Mayerson's worked on
*  that in particular. What is a good internal representation that supports multiple tasks?
*  And we're getting to understand how that's constructed and what's in it. So that it is
*  in a space that supports multiple different heads, like you said. And that I think is
*  fundamentally how biological intelligence works as well. You don't build a representation just
*  for one task. You try to build something that's general, not only so that you can do better in
*  one task or multiple tasks, but also future tasks and future challenges. So you learn the structure
*  of the world and that helps you in all kinds of future challenges.
*  And so you're trying to design a representation that will support an arbitrary set of tasks in a
*  particular sort of class of problem. Yeah. And also it turns out, and that's again a surprise
*  that Elliot found, was that those tasks don't have to be very related. You can learn to do
*  better vision by learning language or better language by learning about DNA structure.
*  No, somehow the world... Yeah, it rhymes. The world rhymes, even if it's very disparate fields.
*  I mean, on that small topic, let me ask you, because you've also on the competition,
*  you're a science side, you worked on both language and vision.
*  What's the connection between the two? What's more, maybe there's a bunch of ways to ask this,
*  but what's more difficult to build from an engineering perspective and evolutionary
*  perspective, the human language system or the human vision system or the equivalent of in the
*  AI space, language and vision, or is it the best, is the multitask idea that you're speaking to,
*  that they need to be deeply integrated? Yeah, absolutely the latter. Learning both at the same
*  time, I think is a fascinating direction in the future. So we have datasets where there's visual
*  component as well as verbal descriptions, for instance, and that way you can learn a deeper
*  representation, a more useful representation for both. But it's still an interesting question of
*  which one is easier. Recognizing objects or even understanding sentences, that's relatively
*  possible, but where the challenges are is to understand the world. The visual world, the 3D,
*  what are the objects doing and predicting what will happen, the relationships. That's what makes
*  vision difficult and language, obviously, it's what is being said, what the meaning is.
*  And the meaning doesn't stop at who did what to whom. There are goals and plans and themes,
*  and you eventually have to understand the entire human society and history in order to understand
*  the sentence very much fully. There are plenty of examples of those kinds of short sentences when
*  you bring in all the world knowledge to understand it. And that's the big challenge. Now, we are far
*  from that, but even just bringing in the visual world together with the sentence will give you
*  already a lot deeper understanding of what's happening. And I think that's where we're going
*  very soon. We've had ImageNet for a long time, and now we have all these text collections,
*  but having both together and then learning a semantic understanding of what is happening,
*  I think that will be the next step in the next few years.
*  You're starting to see that with all the work with Transformers, where the AI community is
*  starting to dip their toe into this idea of having language models that are now doing stuff with
*  images, with vision, and then connecting the two. I mean, right now, it's like these little
*  explorations. We're literally dipping the toe in, but maybe at some point we'll just dive into the
*  pool and it'll just be all seen as the same thing. I do still wonder what's more fundamental,
*  whether vision is, whether we don't think about vision correctly. Maybe the fact, because we're
*  humans and we see things as beautiful and so on, and because we have cameras that take in pixels
*  as a 2D image, that we don't sufficiently think about vision as language. Maybe Chomsky is right
*  all along. That language is fundamental to everything, to even cognition, to even
*  consciousness. The base layer is all language, not necessarily English, but some weird abstract
*  representation, linguistic representation. Yeah. Well, earlier we talked about the social
*  structures and that may be what's underlying the language. That's the more fundamental part,
*  and then language has been added on top of that. Language emerges from the social interaction.
*  Yeah, that's a very good guess. We are visual animals. A lot of the brain is dedicated to
*  vision. Also, when we think about various abstract concepts, we usually reduce that to vision
*  and images. We go to a whiteboard, you draw pictures of very abstract concepts. We tend to
*  resort to that quite a bit, and that's a fundamental representation. It's probably
*  possible that it predated language even. Animals, a lot of them don't talk, but they certainly
*  do have vision. Language is an interesting development from mastication, from eating.
*  You develop an organ that actually can produce sound and manipulate them. Maybe that was an
*  accident. Maybe that was something that was available and then allowed us to do the
*  communication. Or maybe it was gestures, sign language could have been the original proto-language.
*  We don't quite know, but the language is more fundamental than the medium in which it's
*  communicated. I think that it comes from those representations.
*  Now, in current world, they are so strongly integrated. It's really hard to say which one
*  is fundamental. You look at the brain structures and even visual cortex, which is supposed to be
*  very much just vision. Well, if you are thinking of semantic concepts, you're thinking of language,
*  visual cortex lights up. It's still useful even for language computations. There are common
*  structures underlying them, so utilize what you need. When you are understanding a scene,
*  you're understanding relationships. Well, that's not so far from understanding relationships
*  between words and concepts. I think that that's how they are integrated.
*  Yeah, and there's dreams. Once we close our eyes, there's still a world in there somehow operating
*  and somehow possibly the visual system somehow integrated into all of it. I tend to enjoy
*  thinking about aliens and thinking about the sad thing to me about extraterrestrial intelligent life
*  that if it was if it visit us here on Earth or if we came on Mars or maybe in another solar system,
*  another galaxy one day, that us humans would not be able to detect it or communicate with it or
*  appreciate. It would be right in front of our nose and we're too self-obsessed to see it. Not
*  self-obsessed, but our tools, our frameworks of thinking would not detect it. As a good movie
*  Arrival and so on where Stephen Wolfram and his son I think were part of developing this alien
*  language of how aliens would communicate with humans. Do you ever think about that kind of stuff
*  where if humans and aliens would be able to communicate with each other, like if we met each
*  other at some okay we could do SETI which is communicating from across a very big distance,
*  but also just us you know if you did a podcast with an alien, do you think we would be able to
*  find a common language and a common methodology of communication? I think from a computational
*  perspective the way to ask that is is you have very fundamentally different creatures, agents that
*  are created. Would they be able to find a common language? Yes, I do think about that. I think a
*  lot of people who are in computing and AI in particular, they got into it because they were
*  fascinated with science fiction and all of these options. I mean Star Trek generated all kinds of
*  devices that we have now. They envisioned it first and it's a great motivator to think about
*  things like that. Again, being a computational scientist and trying to build intelligent agents,
*  what I would like to do is have a simulation where the agents actually evolve communication.
*  Not just communication, we've done that and people have done that many times. They communicate,
*  they signal and so on, but actually develop a language. Language means grammar. It means all
*  these social structures and on top of that grammatical structures. We do it under various
*  conditions and actually try to identify what conditions are necessary for it to come out.
*  Then we can start asking that kind of questions. Are those languages that emerge in those different
*  simulated environments, are they understandable to us? Can we somehow make a translation?
*  We can make it a concrete question. Machine translation of evolved languages.
*  Languages that evolve come up with, can we translate? I have a Google translate for the
*  evolved languages. If we do that enough, we have perhaps an idea what an alien language might be
*  like, the space or where those languages can be. Because we can set up their environment differently.
*  It doesn't need to be gravity. Societies can be different. They may have no predators.
*  Everybody is a predator. All kinds of situations. Then see what the space possibly is, where those
*  languages are and what the difficulties are. That'd be really good actually to do that before the
*  aliens come here. Yes, it's good practice. On the similar connection, you can think of AI systems
*  as aliens. Is there ways to evolve a communication scheme for, there's a field you can call it like
*  explainable AI, for AI systems to be able to communicate? You evolve a bunch of agents,
*  but for some of them to be able to talk to you also. To evolve a way for agents to be able to
*  communicate about their world to us humans. Do you think that there's possible mechanisms for doing
*  that? We can certainly try. If it's an evolution competition system, for instance, you reward
*  those solutions that are actually functional. That communication makes sense. It allows us to
*  together again achieve common goals. I think it's possible. But even from that paper that you
*  mentioned, the anecdotes, it's quite likely also that the agents learn to lie and fake
*  and do all kinds of things like that. We see that in even very low level, like bacterial evolution,
*  there are cheaters. Who's to say that what they say is actually what they think?
*  But that's why I'm saying that there would have to be some common goal so that we can evaluate
*  whether that communication is at least useful. They may be saying things just to make us feel good
*  or get us to do whatever we want, whatever, not turn them off or something.
*  We would have to understand their internal representations much better to really make sure
*  that that translation is political. But it can be useful. I think it's possible to do that.
*  There are examples where visualizations are automatically created so that we can look into
*  the system and the language is not that far from it. It is a way of communicating and
*  logging what you're doing in some interpretable way. I think a fascinating topic to do that.
*  You're making me realize that it's a good scientific question whether lying is an effective
*  mechanism for integrating yourself and succeeding in a social network, in a world that is social.
*  I tend to believe that honesty and love are evolutionary advantages in an environment
*  where there's a network of intelligent agents. But it's also very possible that dishonesty and
*  manipulation and even violence, all those kinds of things might be more beneficial.
*  That's the old open question about good versus evil. I don't know if it's a hopeful,
*  maybe I'm delusional, but it feels like karma is a thing. Long-term, the agents that are just
*  kind to others sometimes for no reason will do better in a society that's not highly constrained
*  on resources. People start getting weird and evil towards each other and bad when the resources are
*  very low relative to the needs of the populace, especially at the basic level like survival shelter,
*  food, all those kinds of things. I tend to believe that once you have those things established, then
*  well, not to believe, I guess I hope that AI systems will be honest.
*  It's scary to think about the Turing test, AI systems that will eventually
*  pass the Turing test will be ones that are exceptionally good at lying. That's a terrifying
*  concept. I don't know. First of all, from somebody who studied language and obviously
*  are not just a world expert in AI, but somebody who dreams about the future of the field, do you
*  hope, do you think there'll be human level or superhuman level intelligences in the future
*  that we eventually build? Well, definitely hope that we can get there. One, I think,
*  important perspective is that we are building AI to help us, that it is a tool like cars or language
*  or communication. AI will help us be more productive and that is always a condition.
*  It's not something that we build and let run and it becomes an entity of its own that doesn't care
*  about us. Now, of course, really far in the future, maybe that might be possible, but not in the
*  foreseeable future when we are building it. Therefore, we are always in a position of limiting
*  what it can or cannot do. Your point about lying is very interesting. Even in these hyena societies,
*  for instance, when a number of these hyenas band together and they take a risk and steal the kill,
*  there are always hyenas that hang back and don't participate in that risky behavior, but they
*  walk in later and join the party after the kill. There are even some that may be ineffective and
*  cause others to have harm. Like I said, even bacteria cheat. We see in biology that there's
*  always some element of opportunity. I think that this is because if you have a society,
*  in order for society to be effective, you have to have this cooperation and you have to have trust.
*  If you have enough of agents who are able to trust each other, you can achieve a lot more.
*  If you have trust, you also have opportunity for cheaters and liars. I don't think that's ever
*  going to go away. There will be hopefully a minority so that they don't get in the way.
*  We studied in these hyena simulations what the proportion needs to be before it's no longer
*  functional. You can point out that you can tolerate a few cheaters and a few liars and the society can
*  still function. That's probably going to happen when we build these systems at Autonomously Learn.
*  The really successful ones are honest because that's the best way of getting things done.
*  There probably are also intelligent agents that find that they can achieve their goals by
*  bending the rules of cheating. There could be a huge benefit to,
*  as opposed to having fixed AI systems, say we build an AGI system and deploying millions of them,
*  that are exactly the same. There might be a huge benefit to introducing from an evolution
*  and computation perspective a lot of variation. Diversity in all its forms is beneficial even if
*  some people are assholes or some robots are assholes. It's beneficial to have that because
*  you can't always, a priori, know what's good, what's bad. That's a fascinating...
*  Absolutely. Diversity is the bread and butter. If you're running an evolution,
*  you see diversity is the one fundamental thing you have to have. Absolutely. Also,
*  it's not always good diversity. It may be something that can be destructive. We had in these hyena
*  simulations, we have hyenas that are suicidal. They just run and get killed, but they form the
*  basis of those who actually are really fast but stop before they get killed and eventually turn
*  into this mob. There might be something useful there if we combine with something else. I think
*  as long as we can tolerate some of that, it may turn into something better. You may change the
*  rules because it's so much more efficient to do something that was actually against the rules
*  before. We've seen society change over time quite a bit along those lines. There were
*  rules in society that we don't believe are fair anymore even though they were considered
*  proper behavior before. Things are changing. I think in that sense, it's a good idea to be
*  able to tolerate some of that cheating because eventually we might turn into something better.
*  I think this is a message to the trolls and the assholes of the internet that you too
*  have a beautiful purpose in this human ecosystem. I appreciate you very much.
*  In moderate quantities.
*  In moderate quantities. There's a whole field of artificial life. I don't know if you're connected
*  to this field if you pay attention. Do you think about this kind of thing? Is there an impressive
*  demonstration to you of artificial life? Do you think of the agents that you work with in
*  evolutionary computation perspective as life? Where do you think this is headed? Is there
*  interesting systems that we'll be creating more and more that make us redefine, maybe rethink
*  about the nature of life? Different levels of definition and goals there. At some level,
*  artificial life can be considered multi-agent systems that build a society that again achieves
*  a goal. It might be robots that go into a building and clean it up or after an earthquake or
*  something. You can think of that as an artificial life problem in some sense. Or you can really
*  think of artificial life as a simulation of life and a tool to understand what life is and how life
*  evolved on earth. Like I said, in artificial life conference, there are branches of that conference
*  of people who really worry about molecular designs and the start of life. Like I said,
*  primordial soup where eventually you get something self-replicating. They're really trying to build
*  that. It's a whole range of topics. I think that artificial life is a great tool to understand
*  life. There are questions like sustainability, species. We're losing species. How bad is it?
*  Is it natural? Is there a tipping point? Where are we going? Like the hyena evolution, we may have
*  understood that there's a pivotal point in their evolution. They discovered cooperation and
*  coordination. Artificial life simulations can identify that and maybe encourage things like that.
*  So, and also, societies can be seen as a form of life itself. I mean, we're not talking about
*  biological evolution. We have evolution of societies. Maybe some of the same phenomena
*  emerge in that domain and having artificial life simulations and understanding could help us
*  build better societies. Yeah. And thinking from a meme perspective from Richard Dawkins,
*  that maybe the organisms, ideas of the organisms, not the humans in these societies,
*  that from, it's almost like reframing what is exactly evolving. Maybe the interesting,
*  the humans aren't the interesting thing as the contents of our minds is the interesting thing.
*  And that's what's multiplying. And that's actually multiplying and evolving in a much faster
*  time scale. And that maybe has more power on the trajectory of life on earth than does biological
*  evolution. Yes.
*  Is the evolution of these ideas. Yes. And it's fascinating, like I said before,
*  that we can keep up somehow biologically. Yeah.
*  We evolve to a point where we can keep up with this meme evolution, literature, internet. We
*  understand DNA and we understand fundamental particles. We didn't start that way a thousand
*  years ago and we haven't evolved biologically very much, but somehow our minds are able to
*  extend. And therefore AI can be seen also as one such step that we created and it's our tool.
*  And it's part of that meme evolution that we created, even if our biological evolution does
*  not progress as fast. And us humans might only be able to understand so much. We're keeping up
*  so far, or we think we're keeping up so far, but we might need AI systems to understand. Maybe like
*  the physics of the universe is operating like a string theory. Maybe it's operating in much higher
*  dimensions. Maybe we're totally, because of our cognitive limitations, are not able to truly
*  internalize the way this world works. And so we're running up against the limitation of our own
*  minds and we have to create these next level organisms like AI systems that would be able to
*  understand much deeper, like really understand what it means to live in a
*  multi-dimensional world that's outside of the four dimensions, the three of space and one of time.
*  Yeah, translation. And generally we can deal with the world even if we don't understand all the
*  details. We can use computers even though most of us don't know all the structure that's underneath
*  or drive a car. I mean, there are many components, especially new cars, that you don't quite fully
*  know, but you have the interface. You have an abstraction of it that allows you to operate it
*  and utilize it. And I think that that's perfectly adequate and we can build on it and AI can play a
*  similar role. I have to ask about beautiful artificial life systems or evolutionary computation
*  systems. Cellular automata to me, I remember it was a game changer for me early on in life when I saw
*  Conway's Game of Life who recently passed away unfortunately.
*  It's beautiful how much complexity can emerge from such simple rules. I just don't,
*  somehow that simplicity is such a powerful illustration and also humbling because it
*  feels like I personally, from my perspective, understand almost nothing about this world
*  because my intuition fails completely how complexity can emerge from such simplicity.
*  My intuition fails, I think, because of the biggest problem I have. Do you find systems like that
*  beautiful? Do you think about cellular automata? Because cellular automata don't really have,
*  and many other artificial life systems don't necessarily have an objective. Maybe that's a
*  wrong way to say it. It's almost like it's just evolving and creating and there's not even a good
*  definition of what it means to create something complex and interesting and surprising. All those
*  words that you said, is there some of those systems that you find beautiful? Yeah, yeah.
*  Similarly, evolution does not have a goal. It is responding to the current situation
*  and survival then creates more complexity and therefore we have something that we perceive
*  as progress, but that's not what evolution is inherently set to do. Yeah, that's really
*  fascinating how a simple set of rules or simple mappings can, from such simple mappings, complexity
*  can emerge. It's a question of emergence and self-organization and the game of life is one
*  of the simplest ones and very visual and therefore it drives home the point that it's possible that
*  non-linear interactions and this kind of complexity can emerge from them.
*  Biology and evolution is along the same lines. We have simple representations. DNA, if you really
*  think of it, it's not that complex. It's a long sequence of them. There are lots of them, but it's
*  a very simple representation and similar with evolutionary computation, whatever string or tree
*  representation we have and the operations. The amount of code that's required to manipulate
*  those is really, really little and of course game of life even less. How complexity emerges
*  from such simple principles, that's absolutely fascinating. The challenge is to be able to
*  control it and guide it and direct it so that it becomes useful. Game of life is fascinating to
*  look at and evolution, all the forms that come out, is fascinating, but can we actually make it
*  useful for us? And efficient because if you actually think about each of the cells in the
*  game of life as a living organism, there's a lot of death that has to happen to create anything
*  interesting. I guess the question is for us humans that are mortal and then life ends quickly,
*  we want to kind of hurry up and make sure we take evolution, the trajectory that is a little bit
*  more efficient than the alternatives. Yeah, and that touches upon something we talked about earlier,
*  that evolution computation is very impatient. We have a goal, we want it right away, whereas
*  its biology has a lot of time and deep time and weak pressure and large populations. One great
*  example of this is the novelty search. So evolution computation where you don't actually specify
*  a fitness goal, something that is the actual thing that you want, but you just reward solutions that
*  are different from what you've seen before, nothing else. And you know what? You actually
*  discover things that are interesting and useful that way. Ken Stamme and Joe Lehmann did this one
*  study where they actually tried to evolve walking behavior on robots. And that's actually what we
*  talked about earlier where your robot actually failed in all kinds of ways and eventually
*  discovered something that was a very efficient walk. And it was because they rewarded things
*  that were different that you were able to discover something. And I think that this is crucial
*  because in order to be really different from what you already have, you have to utilize what is
*  there in a domain to create something really different. So you have encoded the fundamentals
*  of your world and then you make changes to those fundamentals you get further away.
*  So that's probably what's happening in these systems of emergence. Fundamentals are there
*  and when you follow those fundamentals you get into points and some of those are actually
*  interesting and useful. Now even in that robotic walker simulation there was a large set of garbage
*  but among them there were some of these gems. And then those are the ones that somehow you have to
*  outside recognize and make useful. But these kind of productive systems, if you code them the right
*  kind of principles, I think that they encode the structure of the domain. Then you will get to
*  these solutions and discoveries. It feels like that might also be a good way to live life.
*  So let me ask, do you have advice for young people today about how to live life or how to succeed in
*  their career or forget career, just succeed in life from an evolutionary computation perspective?
*  Yes, yes definitely. Explore, diversity, exploration. And I mean individuals take classes in music,
*  history, philosophy, math, engineering, see connections between them, travel, learn a language.
*  All this diversity is fascinating and we have it at our fingertips today. It's possible, you have to
*  make a bit of an effort because it's not easy. But the rewards are wonderful. Yeah there's something
*  interesting about an objective function of new experiences. So try to figure out what is the
*  maximally new experience I could have today. So that novelty, optimizing for novelty for some
*  period of time might be a very interesting way to sort of maximally expand the sets of experiences
*  you had and then ground from that perspective what would be the most fulfilling trajectory
*  through life. Of course the flip side of that is where I come from. Again, maybe Russian, I don't
*  know. But the choice has a detrimental effect I think from at least from my mind where scarcity
*  has an empowering effect. So if I sort of, if I have very little of something and only one of
*  that something I will appreciate it deeply until I came to Texas recently and I've been picking out
*  delicious incredible meat. I've been fasting a lot so I need to do that again. But when you
*  fast for a few days that the first taste of a food is incredible. So the downside of exploration is that
*  somehow maybe you can correct me but somehow you don't get to experience deeply
*  any one of the particular moments. But that could be a psychology thing. That could be just a very
*  human peculiar flaw. Yeah, I didn't mean that you superficially explore. I mean you can
*  explore deeply. Yeah, so you don't have to explore hundred things but maybe a few topics where you
*  can take a deep enough time dive that you gain an understanding. You yourself have to decide at some
*  point that this is deep enough and I've obtained what I can from this topic and now it's time to
*  move on. And that might take years. People sometimes switch careers and they may stay on some
*  career for a decade and switch to another one. You can do it. You're not pretty determined to
*  stay where you are. But in order to achieve something, 10,000 hours makes, you need 10,000
*  hours to become an expert on something. So you don't have to become an expert but to even develop
*  an understanding and gain the experience that you can use later. You probably have to spend,
*  like I said, it's not easy. You've got to spend some effort on it. Now also at some point then
*  when you have this diversity and you have these experiences, this exploration, you may find
*  something that you can't stay away from. Like for us, it was computers, it was AI. I just have to do
*  it. And then it will take decades maybe and you are pursuing it because you figure it out that this
*  is really exciting and you can bring in your experiences. And there's nothing wrong with that
*  either but you asked what's the advice for young people. That's the exploration part. And then
*  beyond that, after that exploration, you actually can focus and build a career. And even there,
*  you can switch multiple times. But I think the diversity exploration is fundamental to having a
*  successful career as is concentration and spending an effort where it matters. But you are in better
*  position to make the choice when you have done your homework. Exploration precedes commitment
*  but both are beautiful. So again, from an evolutionary computation perspective, we'll
*  look at all the agents that had to die in order to come up with different solutions in simulation.
*  What do you think from that individual agent's perspective is the meaning of it all?
*  So for us humans, you're just one agent who's going to be dead, unfortunately, one day too soon.
*  What do you think is the why of why that agent came to be and eventually will be no more? Is
*  there a meaning to it all? Yeah, in evolution, there is meaning. Everything is a potential
*  direction. Everything is a potential stepping stone. Not all of them are going to work out.
*  Some of them are foundations for further improvement. And even those that are perhaps
*  going to die out, where potential energy is potential solutions. In biology, we see a lot
*  of species die off naturally, like the dinosaurs. They have a really good solution for a while,
*  but then it turned out to be not such a good solution in the long term. When there's an
*  environmental change, you have to have diversity. Some other solutions become better. It doesn't
*  mean that that was an attempt. It didn't quite work out or last, but there are still dinosaurs
*  and mountains, at least they're relatives, and they may one day again be useful. Who knows?
*  So from an individual's perspective, you've got to think of a bigger picture.
*  That it is a huge engine that is innovative, and these elements are all part of it,
*  potential innovations on their own and also as raw material, perhaps, or
*  stepping stones for other things that could come after. But it still feels from an individual
*  perspective that I matter a lot, but even if I'm just a little cog in the giant machine,
*  well, is that just a silly human notion in individualistic society? No, should I let go
*  of that? Do you find beauty in being part of the giant machine? Yeah, I think it's meaningful.
*  I think it adds purpose to your life that you are part of something bigger.
*  That said, are you, do you ponder your individual agent's mortality? Do you think about death?
*  Do you fear death? Well, certainly more now than when I was a youngster and did skydiving
*  and paragliding and all these things. You've become wiser.
*  There is a reason for this life arc that younger folks are more fearless in many ways. It's part
*  of the exploration. They are the individuals who think, I wonder what's over those mountains or
*  what if I go really far in that ocean? What would I find? Older folks don't necessarily think that
*  way, but younger do, and it's kind of counterintuitive. Logically, it's like you
*  have a limited amount of time. What can you do with it that matters? You have done your exploration,
*  you committed to a certain direction, and you become an expert perhaps in it. What can I do
*  that matters with the limited resources that I have? That's how I think a lot of people,
*  myself included, start thinking later on in their career.
*  Like you said, leave a bit of a trace and a bit of an impact even after the agent is gone.
*  Yeah, that's the goal.
*  Well, this was a fascinating conversation. I don't think there's a better way to end it.
*  Thank you so much. First of all, I'm very inspired of how vibrant the community at UT Austin
*  is. It's really exciting for me to see it. This whole field seems like profound philosophically,
*  but also the path forward for the artificial intelligence community. Thank you so much for
*  explaining so many cool things to me today and for wasting all of your valuable time with me.
*  It was a pleasure. Thanks, Larry.
*  I appreciate it.
*  Thanks for listening to this conversation with Risto McAleenan. Thank you to The Jordan Harbinger
*  Show, Grammarly, Belcampo, and Indeed. Check them out in the description to support this podcast.
*  Now, let me leave you with some words from Carl Sagan. Extinction is the rule.
*  Survival is the exception. Thank you for listening. I hope to see you next time.
*  Bye.
