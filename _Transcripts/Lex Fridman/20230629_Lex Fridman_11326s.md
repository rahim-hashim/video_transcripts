---
Date Generated: April 08, 2024
Transcription Model: whisper medium 20231117
Length: 11326s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'george hotz', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai']
Video Views: 1424869
Video Rating: None
---

# George Hotz: Tiny Corp, Twitter, AI Safety, Self-Driving, GPT, AGI & God | Lex Fridman Podcast #387
**Lex Fridman:** [June 29, 2023](https://www.youtube.com/watch?v=dNrTrx42DGQ)
*  What possible ideas do you have for the how human species ends? Sure. So I think the most obvious way to me is wireheading
*  We end up amusing ourselves to death
*  We end up all staring at that infinite tik tok and forgetting to eat
*  Maybe maybe it's even more benign than this. Maybe we all just stop reproducing
*  Now to be fair, it's probably hard hard to get all of humanity
*  Yeah, the interesting thing about humanity is the diversity in it. Oh, yeah organisms in general. There's a lot of weirdos out there
*  Two of them are sitting here. Yeah, I mean diversity in humanity is with due respect
*  I wish I was more weird
*  The following is a conversation with george hotz
*  His third time on this podcast
*  He's the founder of comma ai that seeks to solve autonomous driving and is the founder of a new company called
*  Tiny corp that created tiny grad a neural network framework
*  That is extremely simple with the goal of making it run on any device by any human
*  easily and efficiently
*  As you know george also did a large number of fun and amazing things from hacking the iphone to recently joining twitter for a bit
*  as a
*  Intern in quotes making the case for refactoring the twitter code base
*  In general, he's a fascinating engineer and human being and one of my favorite people to talk to
*  This is alex reidman podcast to support it. Please check out our sponsors in the description and now dear friends. Here's george
*  hotz
*  You mentioned something on a stream about the philosophical nature of time. So let's start with a wild question
*  Do you think time is an illusion?
*  You know
*  I sell phone calls, uh to comma for a thousand dollars, uh, and some guy called me and uh,
*  Like, you know, it's a thousand dollars. You can talk to me for for half an hour and he's like, uh,
*  Yeah, okay. So like time doesn't exist and I really wanted to share this with you
*  I'm like, oh, what do you mean time doesn't exist? Right? Like I think time is a useful model
*  Whether it exists or not, right? Like does quantum physics exist? Well, it doesn't matter
*  It's about whether it's a useful model to describe reality is time
*  Maybe compressive
*  Do you think there is an objective reality or is everything just useful models?
*  Like underneath it all is there an actual thing that we're constructing models for
*  I don't know
*  I was hoping you would know I don't think it matters
*  I mean this kind of connects to the models of constructive reality with machine learning
*  Right sure like is it just nice to have useful approximations of the world such that we can do something with it
*  So there are things that are real column graph complexity is real
*  Yeah, yeah the compressive thing math is real. Yeah
*  It should be a t-shirt
*  And I think hard things are actually hard. I don't think p equals np
*  Oh strong words. Well, I think that's the majority. I do think factoring is in p but
*  I don't think you're the person that falls the majority in all walks of life. So but it's good for that one
*  I do. Yeah in theoretical computer science you you're one of the sheep
*  All right, but do you uh time is a useful model sure
*  What were you talking about on the stream with time? Are you made of time if I remembered half the things I said on stream?
*  Someday someone's gonna make a model of all of that. I'm just gonna come back to haunt me someday soon. Yeah, probably
*  Okay
*  Would that be exciting to you or sad that there's a george harts model?
*  I mean the question is when the george harts model is better than george harts
*  Like I am declining and the model is growing. What is the metric by which you measure better or worse in that if you're competing with yourself
*  Maybe you can just play a game where you have the george harts answer and the george harts model answer and ask which people prefer
*  People close to you or strangers?
*  Either one it will hurt more when it's people close to me, but
*  Both will be overtaken by the george harts model
*  It'd be quite painful right loved ones family members would rather have the model over for thanksgiving than you. Yeah
*  Or like significant others
*  Would rather sext
*  With the uh with the large language model version of you
*  Especially when it's fine tuned to their preferences
*  Is it?
*  Yeah
*  Well, that's what we're doing in a relationship, right?
*  We're just fine tuning ourselves, but we're inefficient with it because we're selfish and greedy and so on
*  Our language models can fine tune more efficiently more selflessly. There's a star trek voyager episode where uh, you know, katharine janeway
*  lost in the delta quadrant makes herself a
*  lover on the holodeck
*  and um
*  The lover falls asleep on her arm and he snores a little bit and you know
*  Janeway edits the program to remove that
*  And then of course the realization is wait
*  This person's terrible. It is actually all their
*  uh
*  Nuances and quirks and slight annoyances that that make this relationship worthwhile
*  But I don't think we're going to realize that until it's too late
*  Well, uh, I think a large language model could incorporate the
*  The flaws and the quirks and all that kind of stuff just the perfect amount of quirks and
*  Flaws to make you charming without crossing the line. Yeah. Yeah
*  and there's probably a good like
*  Approximation of the like the percent of time
*  the language model should be
*  cranky or uh
*  An asshole or jealous or all this kind of stuff and of course it can and it will but all that difficulty at that point is artificial
*  There's no more real difficulty
*  Okay, what's the difference between real and artificial?
*  Artificial difficulty is difficulty. That's like constructed or could be turned off with a knob
*  Real difficulty is like you're in the woods and you gotta survive
*  So if something can not be turned off with a knob, it's real
*  Yeah, I think so or I mean you can't get out of this by smashing the knob with a hammer
*  I mean, maybe you kind of can you know, I
*  Into the wild when uh
*  you know, uh
*  Alexander supertramp he wants to explore something that's never been explored before but it's the 90s. Everything's been explored
*  So he's like, well, i'm just not gonna bring a map
*  Yeah, I mean
*  No, you're you're not exploring you should have brought a map dude. You died. There was a bridge a mile from where you were camping
*  How does that connect to the metaphor of the knob?
*  By not bringing the map you didn't become an explorer
*  You just smashed the thing yeah, yeah the art the difficulty is still artificial
*  You failed before you started. What if we just don't have access to the knob? Well, that maybe is even scarier
*  Right. Like we already exist in a world of nature and nature has been fine-tuned over billions of years. Yeah
*  um to
*  have uh
*  Humans build something and then throw the knob away in some grand romantic gesture is horrifying
*  Do you think of us humans as individuals that are like born and die or is it we're just all part of one living organism?
*  that is
*  Earth that is nature
*  I don't think there's a clear line there. I think it's all kind of just fuzzy. I don't know
*  I mean, I don't think i'm conscious. I don't think i'm anything. I think i'm just a computer program
*  So it's all computation. Yeah, I think running your head is just a
*  Is a this computation everything running in the universe is computation. I think I believe the extended church time thesis
*  Yeah, but
*  There seems to be an embodiment to your particular computation like there's a consistency
*  Well, yeah, but I mean models have consistency too
*  Yeah models that have been rlhf will continually say, you know, like well, how do I murder ethnic minorities?
*  Oh, well, I can't let you do that. How there's a consistency to that behavior
*  It's all rlhf
*  Like we all rlhf each other
*  we we find we provide human feedback and there that
*  Thereby fine-tune these little pockets of computation
*  But it's still unclear why that pocket of computation stays with you like for years
*  It just kind of fall like you have this consistent
*  Set of physics biology
*  Uh what
*  Like whatever you call the the neurons firing like the electrical signals the mechanical signals all of that that seems to stay there
*  And it contains information stores information and that information permeates through time
*  And stays with you. There's like memory
*  It's like sticky
*  Okay, to be fair like a lot of the models we're building today are very even rlhf is
*  Nowhere near as complex as the human loss function reinforcement learning with human feedback
*  um
*  You know when I talked about will gpt12 be agi my answer is no, of course not
*  I mean cross entropy loss is never going to get you there you need
*  uh probably rl in
*  Fancy environments in order to get something that would be considered like agi like
*  So to ask like the question about like why I don't know like it's just some quirk of evolution, right?
*  I don't think there's anything particularly
*  special about
*  Where I ended up
*  Where humans ended up?
*  It's okay
*  We have human level intelligence. Would you call that agi? Whatever we have g i
*  look, I actually I don't really even like the word agi, um, but
*  General intelligence is defined to be whatever humans have
*  Okay
*  So why can gpt12 not get us to agi? Can we just like linger on that?
*  If your loss function is categorical cross entropy if your loss function is just try to maximize compression
*  Uh, I have a soundcloud I rap and I tried to get chat gpt to help me write raps
*  And the raps that it wrote sounded like youtube comment raps, you know
*  You can go on any rap beat online and you can see what people put in the comments and it's the most like
*  Mid quality rap you can find is made good or bad mid is bad. It's like mid. It's like
*  Every time I talk to you, I learn new words
*  Mid yeah
*  I was like, uh, is it is it like basic? Is that what mid means?
*  Kind of it's like it's like middle of the curve, right? Yeah, so there's like there's like I like do that intelligence curve
*  Um, and you have like the dumb guy the smart guy and then the mid guy actually being the mid guy is the worst
*  The smart guy is like I put all my money in bitcoin. The mid guy is like you can't put money in bitcoin. It's not real money
*  Uh, and all of it is a genius meme
*  That's another interesting one
*  memes
*  The humor the idea the absurdity encapsulated in a single image
*  And it just kind of propagates
*  virally
*  Between all of our brains
*  I didn't get much sleep last night. So i'm very I sound like i'm high, but I swear i'm not
*  Uh, do you think we have ideas or ideas have us?
*  I think that we're gonna get super scary memes once the ai's actually are superhuman
*  Like the gay eye will generate memes. Of course you think it'll make humans laugh
*  I think it's worse than that. So, um
*  Infinite jest it's introduced in the first
*  50 pages is about a tape that you uh, once you watch it once you only ever want to watch that tape
*  Um, in fact, you want to watch the tape so much that someone says, okay, here's a hacksaw cut off your pinky
*  And then i'll let you watch the tape again and you'll do it
*  Uh, so we're actually gonna build that I think but it's not going to be one static tape
*  I think the human brain is too complex
*  to be
*  Stuck in one static tape like that if you look at like ant brains, maybe they can be stuck on a static tape
*  But we're going to build that using generative models. We're going to build the tick tock that you actually can't look away from
*  So tick tock is already pretty close there, but the generation is done by humans
*  The algorithm is just doing their recommendation. But if it's if the algorithm is also able to do the generation
*  Well, it's a question about how much intelligence is behind it, right?
*  So the content is being generated by let's say one humanity worth of intelligence and you can quantify a humanity, right? That's a
*  You know, it's it's
*  Exa flops yada flops
*  Uh, but you can quantify it once that generation is being done by a hundred humanities. You're done
*  So it's actually scale that's the problem but also speed
*  Yeah
*  And what if it's sort of manipulating the very limited human dopamine engine
*  for porn
*  Imagine just tick tock but for porn. Yeah, that's like a brave new world
*  I don't even know what it'll look like right like again, you can't imagine the behaviors of something smarter than you but a
*  super intelligent and in
*  An agent that just dominates your intelligence so much
*  Will be able to completely manipulate you is it possible that it won't really manipulate it'll just move past us
*  it'll just kind of
*  Exists the way water exists or the air exists you see and that's the whole ai safety thing
*  It's not the machine that's going to do that. It's other humans using the machine that are going to do that to you. Yeah
*  Because the machine is not interested in hurting humans
*  The machine is a machine
*  Yeah, but the human gets the machine and there's a lot of humans out there very interested in manipulating you
*  Well, let me bring up
*  Eliezer, jetkowski
*  Who recently sat where you're sitting?
*  He thinks that ai will almost surely kill everyone
*  Do you agree with him or not?
*  Yes, but maybe for a different reason
*  Okay
*  what
*  and i'll try to uh
*  Get you to find hope or we could find a no to that answer. But why yes
*  Okay, why didn't nuclear weapons kill everyone? That's a good question. I think there's an answer
*  I think it's actually very hard to deploy nuclear weapons tactically
*  It's very hard to accomplish tactical objectives great I can nuke their country when I have an irradiated pile of rubble
*  I don't want that why not?
*  Why don't I want an irradiated pile of rubble? Yeah, for all the reasons no one wants an irradiated pile of rubble
*  because you can't use that land for uh
*  For resources you can't populate the land. Yeah
*  What you want a a total victory in a war is not usually the
*  Irradiation and eradication of the people there. It's the subjugation and domination of the people
*  Okay
*  So you can't use this strategically tactically in a war. Yeah to help you to help
*  Uh gain a military advantage
*  It's all complete destruction
*  All right
*  But there's egos involved. It's still surprising still surprising that nobody pressed the big red button
*  It's somewhat surprising but you see it's the little red button that's going to be pressed with ai that's gonna
*  You know and that's why we die it's it's not because
*  The ai if there's anything in the nature of ai, it's just the nature of humanity. What's the algorithm behind the little red button?
*  What like what what what possible ideas do you have for the how human species ends? Sure. So I think the most uh,
*  Obvious way to me is wireheading. We end up amusing ourselves to death
*  We end up all
*  Staring at that infinite tik tok and forgetting to eat
*  Maybe maybe it's even more benign than this. Maybe we all just stop reproducing
*  I
*  Know to be fair. It's probably hard hard to get all of humanity. Yeah
*  It probably always goes like the the interesting thing about humanity is the diversity in it. Oh, yeah organisms in general
*  There's a lot of weirdos out there. Well, two of them are sitting here. Yeah, I mean diversity in humanity is with due respect
*  I wish I was more weird
*  No, like i'm kind of look i'm drinking smart water man, that's like a coca-cola product right you want corporate george hoss
*  No, the amount of diversity in humanity, I think is decreasing
*  And just like all the other biodiversity on the planet. Oh boy. Yeah, right social media is not helping go eat mcdonnell's in china
*  Yeah
*  Yeah, no, it's the interconnectedness. That's that's that's that's doing it. Oh, that's interesting
*  So everybody starts relying on the connectivity of the internet
*  And over time that reduces the diversity the intellectual diversity and then that gets you everybody into a funnel
*  They're still going to be a guy in texas. There is and yeah bunker to be fair. Do I think ai kills us all?
*  Uh, I think ai kills everything we call like society today
*  I do not think it actually kills the human species. I think that's actually incredibly hard to do
*  Yeah, but society like if we start over that's tricky most of us don't know how to do most things
*  Yeah, but some of us do and they'll be okay and they'll rebuild after they are
*  Great ai
*  What's rebuilding look like how far like how much do we lose like what is human civilization done?
*  That's interesting the combustion engine electricity
*  so uh
*  Power and energy that's interesting
*  Like how to harness energy?
*  Whoa, they're going to be religiously against that
*  Are they going to get back to uh, like fire?
*  Sure, I mean they'll be a they'll be a little bit like, you know
*  Some kind of amish looking kind of thing. I think I think they're going to have very strong taboos against technology
*  hmm
*  Like technology it's almost like a new religion technology is the devil. Yeah, and uh,
*  Nature is god
*  Sure, so closer to nature, but can you really get away from ai if it destroyed 99 of the human species, isn't it?
*  Somehow have a hold like a stronghold. What's interesting about
*  Everything we build I think we're going to build super intelligence before we build any sort of robustness in the ai
*  We cannot build an ai that is capable of going out into nature and surviving like a um, like a bird
*  Right. A bird is an incredibly robust
*  Organism, we've built nothing like this. We haven't built a machine that's capable of reproducing
*  Yes, but
*  There is uh, you know, I work with like robots a lot now. I have a bunch of them. Um
*  They're mobile
*  They can't reproduce but all they need is I guess you're saying they can't repair themselves
*  But if you have a large number if you have like 100 million of them, let's just focus on them reproducing, right?
*  Do they have microchips in them? Okay, then do they include a fab?
*  No, then how are they going to reproduce? Well, they're hey, it doesn't have to be all on board, right?
*  They can go to a factory to a repair shop. Yeah, but then you're really moving away from robustness
*  Yes, all of life is capable of reproducing without needing to go to a repair shop
*  Life will continue to reproduce in the complete absence of civilization
*  Robots will not
*  So when the if if the ai apocalypse happens
*  I mean the ais are going to probably die out because I think we're going to get again super intelligence long before we get robustness
*  What about if you just improve?
*  the fab to where
*  You just have a 3d printer that can always help you
*  Well, that'd be very interesting. I'm interested in building that
*  Of course you are you think how difficult is that problem to have a robot that uh,
*  Basically can build itself very very hard. I think you've mentioned this like, uh,
*  To me or somewhere
*  Where people think it's easy conceptually?
*  And then they remember that you're going to have to have a fab
*  Yeah on board of course
*  So 3d printer that prints a 3d printer. Yeah
*  Yeah on legs
*  Yeah hard
*  Well, because it's I mean a 3d printer is a very simple machine, right? Okay, you're gonna print chips
*  You're gonna have an atomic printer. How are you gonna dope the silicon? Yeah
*  All right
*  How you gonna edge the silicon?
*  you're gonna have to have a
*  very interesting kind of fab if you want to
*  Have a lot of computation on board
*  but you can do like
*  Structural type of robots that are dumb
*  Yeah, but
*  Structural type of robots aren't going to have the intelligence required to survive in any complex environment
*  What about like ants type of systems? We have like trillions of them
*  I don't think this works. I mean again like
*  Ants at their very core are made up of cells that are capable of individually reproducing
*  They're doing quite a lot a lot of computation that we're taking for granted. It's not even just the computation
*  It's that reproduction is so inherent. Okay, so like there's two stacks of life in the world
*  There's bio the biological stack and the silicon stack the biological stack starts with reproduction
*  Reproduction is at the absolute core the first proto rna organisms were capable of reproducing
*  Right the silicon stack
*  Despite as far as it's come
*  Is nowhere near being able to reproduce
*  Yeah
*  So the the fab movement
*  Digital fabrication
*  Fabrication in the full range of what that means is still in the early stages. Yeah, you're interested in this world
*  Even if you did put a fab on the machine, right? Let's say okay, you know, we can build vaps
*  We know how to do that as humanity
*  We can probably put all the precursors that build all the machines and the fabs also in the machine
*  So first off this machine is going to be absolutely massive
*  I mean we almost have a like think of the size of the thing required to reproduce a machine today
*  right
*  Like is our civilization capable of reproduction?
*  Can we reproduce our civilization on mars?
*  If we were to construct a machine that is made up of humans
*  Like a company that can reproduce itself. Yeah
*  I don't know. It feels like like
*  like 115
*  people
*  Get so much harder than that
*  120
*  I believe that twitter can be run by 50 people. Uh
*  I think that this is going to take most of
*  Like it's just most of society right like we live in one globalized world
*  No, but you're not interested in running twitter. You're interested in seeding
*  like um
*  You want to seed a civilization and then because humans can like oh, okay. You're talking about yeah
*  Okay, so you're talking about the humans reproducing and like basically like what's the smallest self-sustaining colony of humans?
*  Yeah, yeah, okay fine, but they're not going to be making five nanometer chips over time. They will I think you're being
*  Like we have to expand our conception of time here going back to the original uh time scale. I mean over across
*  Maybe 100 generations. We're back to making chips
*  No, if you seed the colony correctly
*  Maybe or maybe they'll watch our
*  Colony die out over here and be like we're not making chips. Don't make chips
*  No, but you have to seed that colony correctly. Whatever you do. Don't make chips chips are what led to their downfall
*  Hmm
*  Well, that is the thing that humans do they they come up the constructed devil
*  A good thing and a bad thing and they really stick by that and then they murder each other over that
*  There's always one asshole in the room who murders everybody
*  And he usually makes tattoos and nice branding
*  Do you need that asshole? That's the question, right?
*  Humanity works really hard today to get rid of that asshole, but I think they might be important
*  Yeah, this whole freedom of speech thing it's it's the freedom of being an asshole seems kind of important, right?
*  Man this thing this fab this human fab that we constructed this human civilization is pretty interesting and now it's
*  building
*  artificial copies of itself or artificial copies of
*  various
*  Aspects of itself that seem interesting like intelligence
*  And I wonder where that goes
*  I like to think it's just like another stack for life like we have like the bio stack life
*  Like we're a bio stack life and then the silicon stack life
*  But it seems like the ceiling
*  There might not be a ceiling in or at least the ceiling is much higher for the for the silicon stack
*  Oh, no, I don't we don't know what the ceiling is for the bio stack either the bio stack the bio stack just
*  Seem to move slower. Um, you have more's law
*  Which is not dead despite many proclamations, uh in the bio stack or the silicon in the silicon stack
*  And you don't have anything like this in the bio stack
*  So I have a meme that I posted I tried to make a meme
*  It didn't work too well
*  But um, I posted a picture of uh, you know, ronald reagan and joe biden and you look this is 1980 and this is 2020
*  And these two humans are basically like the same, right? There's no there's no like like they're
*  There's been no change in humans in the last 40 years. Yeah
*  And then I posted a computer from 1980 and a computer from 2020
*  Wow
*  Yeah with their early early stages, right which is why you said when you said the fab the size of the fab required to make
*  another fab is like, uh
*  Very large right now. Oh, yeah, but computers were very large
*  um 80 years ago
*  And they got pretty tiny and
*  The people are starting to want to wear them on their face
*  In order to escape reality that's the thing in order to be live inside the computer yeah
*  Put a screen right here. I don't have to see the rest of you assholes. I've been ready for a long time
*  You like virtual reality? I love it
*  Do you want to live there? Yeah
*  Yeah
*  Pardon me does too
*  How far away are we do you think?
*  Judging from what you can buy today far very far
*  I gotta tell you that I had the experience of
*  Meta's codec avatar where it's a
*  ultra high resolution scan
*  It looked real
*  I mean the headsets just are not quite at like eye resolution yet
*  I haven't put on any headset where i'm like, oh I this could be the real world
*  Whereas when I put good headphones on
*  Audio is there
*  Like we we can reproduce audio that i'm like i'm actually in a jungle right now. I if I close my eyes
*  I can't tell i'm not
*  Yeah, but then there's also smell and all that kind of stuff. Sure
*  I don't know I
*  The the power of imagination or the power of the the mechanism in the human mind that fills the gaps
*  That kind of reaches and wants to make the thing you see in the virtual world real to you
*  I believe in that power
*  Or humans want to believe yeah
*  Like what if you're lonely? What if you're sad?
*  What if you're really struggling in life and here's a world where you don't have to struggle anymore
*  Humans want to believe so much that people think the large language models are conscious. That's how much humans want to believe
*  Strong words he's throwing left and right hooks. Uh, why do you think large language models are not conscious?
*  I don't think i'm conscious
*  Oh, so what is consciousness then george hans? It's like
*  What it seems to mean to people it's just like a word that atheists use for souls
*  Sure, but that doesn't mean soul is not an interesting word
*  If consciousness is a spectrum, i'm definitely way more conscious than the large language models are
*  I think the large language models are less conscious than a chicken
*  When is the last time you seen a chicken?
*  Uh in miami like a couple months ago
*  How
*  No, like a living chicken living chickens walking around miami. It's crazy like on the street. Yeah, like a chicken a chicken
*  All right
*  All right, I was trying to call you all like a good journalist and I uh, I got shut down
*  Okay, but uh, you don't
*  Think much about this kind of
*  Subjective
*  Subjective feeling that it it feels like something
*  To exist and then as an observer
*  you can
*  Have a sense that an entity is not only intelligent but has a kind of
*  Subjective experience of its reality like a self-awareness that is capable of like suffering of hurting of being excited by the environment in a way
*  That's not merely
*  Kind of an artificial response but a deeply felt one humans want to believe so much that if I took a rock and a sharpie
*  And drew a sad face on the rock. They'd think the rock is sad
*  Yeah
*  And you're saying when we look in the mirror, we we apply the same smiley face with rock pretty much
*  Yeah, doesn't it's not weird though that you're not conscious
*  that
*  No
*  But you do believe in consciousness
*  It's just it's unclear okay, so do you it's like a little like a symptom of the bigger thing that's not that important
*  Yeah
*  I mean it's interesting that like the human systems seem to claim that they're conscious and I guess it kind of like says something
*  And they straight up like okay. What do people mean when even if you don't believe in consciousness?
*  What do people mean when they say consciousness and there's definitely like meanings to it?
*  What's your favorite thing to eat?
*  Pizza cheese piece, what are the toppings? I like cheese pizza. Don't say pineapple
*  No, I don't okay pepperoni because they put any ham on it. Oh, that's real bad. What's the best? What's the best pizza?
*  What are we talking about here? Like you like cheap crappy pizza a chicago deep dish cheese?
*  Oh, that's that's my favorite. There you go. You bite into a deep dish a cargo deep dish pizza
*  And it feels like so you were starving you haven't eaten for 24 hours
*  You just bite in and you're hanging out with somebody that matters a lot to you and you're there with the pizza
*  Yeah, all right
*  It feels like something i'm george motherfucking hot eating a fucking chicago deep dish pizza
*  There's just a full peak
*  Light living experience. Yeah of being human the top of the human condition. Sure
*  It feels like something to experience that
*  Why does it feel like something that's consciousness isn't it
*  If that's the word you want to use to describe it sure i'm not going to deny you if that feeling exists
*  I'm not going to deny that I experienced that feeling
*  When I guess what I kind of take issue to is that there's some like
*  Like how does it feel to be a web server? Do 404s hurt?
*  Not yet, how would you know what suffering looked like sure you can recognize a suffering dog because we're the same stack as the dog
*  All the biostack stuff kind of especially mammals, you know, it's it's really easy you can
*  Game recognizes game. Yeah
*  Versus the silicon stack stuff. It's like you have no idea
*  You have you it. Oh wow, the little thing has learned to mimic
*  you know
*  But then I realized that that's all we are too. Oh look the little thing has learned to mimic
*  Yeah, I guess uh, yeah 404 could be could be suffering but it's
*  so
*  far
*  from
*  Our kind of living organism our kind of stack but it feels like ai can start
*  Maybe mimicking the biological stack better better better because it's trained retrained it. Yeah
*  And so in that maybe that's the definition of consciousness
*  Is the the biostack consciousness the definition of consciousness is how close something looks to human sure i'll give you that one
*  No, how close something?
*  Is to the human experience sure
*  It's a very it's a very anthropocentric definition but well, that's all we got
*  Sure. No, and I don't mean to like I think there's a lot of value in it
*  Look, I just started my second company. My third company will be ai girlfriends
*  No, like I mean, I want to find out what your fourth company is. Oh, well, because I think once you have ai girlfriends, it's uh,
*  Oh boy
*  Does it get interesting?
*  Well, maybe let's go there. I mean the relationships with ai
*  That's creating human-like organisms, right?
*  and part of being human is being conscious is being uh having the capacity to suffer having the capacity to experience this life richly
*  in such a way that you can empathize
*  the ai system empathize with you and you can empathize with it or you can project your
*  Anthropomorphic sense of what the other entity is experiencing and an ai model would need to
*  Yeah to create that experience inside your mind
*  And it doesn't seem that difficult. Yeah, but okay. So here's where it actually gets totally different, right?
*  When you interact with another human you can make some assumptions
*  Yeah
*  When you interact with these models you can't you can make some assumptions that that other human
*  Experiences suffering and pleasure in a pretty similar way to you do the golden rule applies
*  With an ai model, this isn't really true, right?
*  these these large language models are good at fooling people because they were trained on a
*  Whole bunch of human data and told to mimic it. Yep, but if if the ai system says hi, my name is samantha
*  Uh, it has a backstory. Yeah, I went to college here and there. Yeah, maybe you'll integrate this in ai system
*  I made some chat bots. I give them back stories. It was lots of fun. I'm so happy when llama came out
*  Yeah, uh, we'll talk about llama. We'll talk about all that but like, you know the rock with the smiley face. Yeah
*  Well, this it seems pretty natural for for you to anthropomorphize that thing and then start dating it and
*  Before you know it
*  You're married and have kids with a rock
*  With a rock there's pictures on instagram with you and a rock and smiley face
*  to be fair like, you know something that people generally look for when they're looking for someone to date is intelligence in some
*  Form and the rock doesn't really have intelligence only a pretty desperate person would date a rock
*  I think we're all desperate deep down. Oh not rock level desperate
*  All right, uh
*  Not rock level
*  Desperate but ai
*  Level desperate. I don't know. I think all of us have a deep loneliness. It just feels like the language models are there
*  Oh, I agree. And you know what? I won't even say this so cynically
*  I will actually say this in a way that like I want ai friends. I do yeah, like I would love to
*  Love to you know, again, I the language models now are still a little
*  like
*  People are impressed with these gpt things and I look like or like or uh
*  The co-pilot the coding one and i'm like, okay
*  This is like junior engineer level and these people are like fiverr level artists and copywriters
*  Like okay great we got like fiverr and like junior engineers
*  Okay, cool like and this is just a start and it will get better, right?
*  Like I would I can't wait to have ai friends who are more intelligent than I am
*  So fiverr is just a temper. It's not the ceiling. No, definitely not
*  Is it uh, is it count as cheating when you're talking to an ai model emotional cheating?
*  That's that's up to you and your human partner to define oh you have to all right you can yeah
*  You have to have that have to have that conversation. I guess all right
*  I mean integrate that with uh with porn and all this. Well, I mean a similar kind of a porn. Yeah. Yeah
*  Right. I think people in relationships have different views on that
*  Yeah, but most people don't have
*  like
*  Serious open conversations about
*  All the different aspects of what's cool and what's not
*  And it feels like ai is a really weird conversation to have
*  I mean the the porn one is a good branching off like these things, you know
*  One of my scenarios that I put in my chatbot is a uh, you know, uh
*  A nice girl named lexi. She's 20. She just moved out to la
*  She wanted to be an actress, but she started doing only fans instead and you're on a date with her. Enjoy
*  Oh man
*  Yeah, and so is that if you're actually dating somebody in real life, is that cheating?
*  I feel like it gets a little weird. Sure. It gets real weird
*  It's like what are you allowed to say to an ai bot?
*  Imagine having that conversation with a significant other
*  I mean, these are all things for people to define in their relationships what it means to be human is just going to start to get weird
*  Especially online like how do you know like there'll be moments when you'll have
*  What you think is a real human you interacted with on twitter for years and you realize it's not
*  I spread I love this meme, uh heaven banning
*  You know about shadow banning. Yeah, shadow banning. Okay, you post no one can see it
*  Heaven banning you post no one can see it, but a whole lot of ai's are spot up to interact with you
*  Well, maybe that's what the way human civilization ends is all of us a heaven banned there's a great, uh,
*  It's called my little pony friendship is optimal
*  It's a sci-fi story that uh explores this idea
*  Friendship is optimal friendship is optimal. Yeah, i'd like to have some at least stuff on the intellectual realm some ai friends
*  that argue with me
*  But the the romantic realm is weird
*  definitely weird
*  but
*  not out of the realm of uh
*  The uh, the kind of weirdness that human civilization is capable of I think
*  I think I want it look I want it if no one else wants it. I want it
*  Yeah, I think a lot of people probably want it. There's a deep loneliness
*  and i'll fill their
*  Loneliness and you know, it just will only advertise to you some of the time
*  Yeah, maybe the conceptions of monogamy change too like I grew up in a time like I value monogamy
*  but maybe that's a silly notion when you have
*  arbitrary number of ai systems
*  Yeah, this this um this interesting path from rationality to polyamory. Yeah, that doesn't make sense for me for you
*  But you're just a biological organism who was born before
*  Like really the internet really took off
*  the crazy thing is like
*  Culture is whatever we define it as
*  Right. These things are not
*  You've like is ought problem in moral philosophy, right? There's no like like okay
*  What is might be that like computers are capable of mimicking?
*  Uh, you know girlfriends perfectly they passed the girlfriend touring test, right?
*  But that doesn't say anything about ought that doesn't say anything about how we ought to respond to them as a civilization
*  That doesn't say we ought to get rid of monogamy. All right. That's a completely separate question. Really a religious one
*  Girlfriend touring test. I wonder what that looks like girlfriend. Are you writing that?
*  Uh, will you be the the the alan touring of the 21st century that writes the uh, the girlfriend touring test?
*  No, I mean, of course my my ai girlfriends their goal is to pass the girlfriend touring test
*  No, but there should be like a paper that kind of defines the test
*  Or you so I mean the question is if it's deeply personalized or there's a common thing that really gets
*  everybody
*  Yeah, I mean, you know, look we're a company we don't have to get everybody we just have to get a large enough
*  Clientele to stay like are you already already thinking company?
*  All right. Let's uh before we go to company number three and company number four. Let's go to company number two
*  All right, tiny corp
*  Possibly one of the greatest names of all time for a company
*  You've launched a new company called tiny corp that leads the development of tiny grad
*  What's the origin story of tiny corp and tiny grad?
*  I started tiny grad as a like a toy project just to teach myself. Okay, like what is a convolution?
*  What are all these options you can pass to them? What is the derivative of a convolution right? Very similar to a car pathy micro grad
*  very similar
*  and then
*  I started realizing I started thinking about like ai chips. I started thinking about chips that run
*  Ai and I was like well, okay, this is going to be a really big problem if nvidia becomes a monopoly here
*  um
*  How long before nvidia is nationalized?
*  So you uh
*  One of the reasons that start tiny corp is to challenge nvidia
*  it's not so much
*  to challenge nvidia, I actually I like nvidia and
*  it's
*  To make sure power stays decentralized. Yeah, and here's uh
*  computational power
*  Until you nvidia is kind of locking down the computational power of the world
*  if
*  Nvidia becomes just like 10x better than everything else. You're giving a big advantage to somebody who can secure
*  nvidia as a resource
*  Yeah, in fact if jensen watches this podcast, he may want to consider this
*  He may want to consider making sure his company is not nationalized
*  Do you think that's an actual threat? Oh, yes
*  No, but there's so much uh, you know, there's amd so we have nvidia and amd great. All right
*  But you don't you don't think there's like a push
*  Towards like selling like google selling tpus or something like this. You don't think there's a push for that. Have you seen it?
*  Google loves to rent you tpus. It doesn't you can't buy it at best buy
*  So I started work on a uh
*  On a chip
*  I was like, okay. What's it going to take to make a chip?
*  And my first notions were all completely wrong about why about like how you can improve on gpus
*  And I will take this this is from uh, jim keller on your podcast
*  And this is one of my absolute favorite
*  descriptions of computation
*  So there's three kinds of computation paradigms that are common in the world today
*  Other cpus and cpus can do everything cpus can do add and multiply
*  They can do load and store and they can do compare and branch
*  And when I say they can do these things they can do them all fast, right?
*  So compare and branch are unique to cpus and what I mean by they can do them fast is they can do things like
*  Branch prediction and speculative execution and they spend tons of transistors and these like super deep reorder buffers in order to make these things fast
*  Then you have a simpler computation model gpus gpus can't really do compare and branch. I mean they can but it's horrendously slow
*  But gpus can do arbitrary load and store, right gpus can do things like x d reference y
*  So they can fetch from arbitrary pieces of memory. They can fetch from memory that is defined by the contents of the data
*  Um, the third model of computation dsp's and dsp's are just add and multiply
*  Right, like they can do load and stores, but only static load and stores only loads and stores that are known before the program runs
*  And you look at neural networks today and 95 percent of neural networks are all the dsp paradigm
*  They are just statically scheduled adds and multiplies
*  so tiny guard really took this idea and
*  And i'm still working on it to extend this as far as possible
*  Um, every stage of the stack has turn completeness, right python has turn completeness
*  And then we take python we go to c++ which is turn complete and maybe c++ calls into some kuda kernels
*  Which are turn complete the kuda kernels go through lvm which is turn complete into ptx which is turn complete to sas
*  Which is turn complete on a turn complete processor. I want to get turn completeness out of the stack entirely
*  Because once you get rid of turn completeness, you can reason about things
*  Rice's theorem and the halting problem do not apply to admiral machines
*  Okay, what's the power and the value of getting turn completeness out of
*  Out of are we talking about the hardware or the software every layer of the stack every layer every layer of the stack
*  Removing turn completeness allows you to reason about things, right?
*  So the reason you need to do branch prediction in a cpu and the reason it's prediction and the branch predictors are I think
*  They're like 99 on cpus. Why do they get one percent of them wrong? Well, they get one percent wrong because you can't know
*  Right. That's the halting problem. It's equivalent to the halting problem to say whether a branch is going to be taken or not
*  um, I can show that but
*  the
*  admal machine the neural network
*  Runs the identical compute every time the only thing that changes is the data
*  So when you realize this you think about okay, how can we build a computer?
*  How can we build a stack that takes maximal advantage of this idea?
*  uh, so
*  What makes tiny grad different from other neural network libraries is it does not have a primitive operator even for matrix multiplication?
*  And this is every single one they even have primitive operations for things like convolutions so no matmul
*  No matmul. Well, here's what a matmul is. So i'll use my hands to talk here
*  So if you think about a cube and I put my two matrices that i'm multiplying on two faces of the cube
*  Right. You can think about the matrix multiply as okay
*  The n cubed i'm going to multiply for each one in the cubed and then i'm going to do a sum
*  Which is a reduce up to here to the third face of the cube and that's your multiplied matrix
*  So what a matrix multiply is is a bunch of shape operations, right?
*  A bunch of permute three shapes and expands on the two matrices
*  a multiply
*  n cubed a reduce
*  n cubed which gives you an n squared matrix
*  Okay. So what what is the minimum number of operations that can accomplish that if you don't have?
*  Matmul as a primitive so tiny grad has about 20 and you can compare tiny grads
*  Opset or ir to things like xla or prim torch
*  So xla and prim torch are ideas. We're like, okay torch has like 2000 different kernels
*  um
*  Py torch 2.0 introduced prim torch, which has only 250
*  Tiny grad has order of magnitude 25
*  It's it's 10x less than xla or prim torch
*  And you can think about it as kind of like risk versus cisc, right?
*  These other things are cisc like systems
*  Tiny grad is risk
*  And risk one risk architecture is going to change everything
*  1995 hackers
*  Wait, really? That's an actual thing angelina jolee delivers the line risk architecture is going to change everything in 1995
*  And here we are with arm in the phones
*  And arm everywhere
*  Wow, I love it when movies actually have real things in them, right?
*  Okay, interesting. So this is like, uh, so you're thinking of this as the risk
*  architecture of
*  ml stack
*  25, uh, what what can you can you go through the
*  uh
*  The four op types sure
*  um, okay, so you have unary ops which take in
*  uh
*  A tensor and return a tensor of the same size and do some unary op to it x log
*  Uh reciprocal sign, right they take in one and they're pointwise
*  Really? Yeah really?
*  Um almost all activation functions are unary ops
*  Um some combinations of unary ops together is still a unary op
*  um
*  Then you have binary ops binary ops are like, uh point wise addition multiplication division compare
*  Uh, it takes in two tensors of equal size and outputs one tensor
*  Um, then you have reduce ops
*  reduce ops will like take a three-dimensional tensor and turn it into a two-dimensional tensor
*  Or a three-dimensional tensor turn into zero-dimensional tensor think like a sum or max
*  Are really the common ones there?
*  And then the fourth type is movement ops
*  And movement ops are different from the other types because they don't actually require computation. They require different ways to look at memory
*  So that includes reshapes permutes
*  expands flips
*  Those are the main ones probably so with that you have enough to make a map mall and convolutions and every convolution you can imagine
*  dilated convolutions strided convolutions transposed convolutions
*  Um, you're right on github about laziness
*  um showing a map mall
*  Matrix multiplication see how despite the style is fused into one kernel with the power of laziness
*  Can you elaborate on this power of laziness? Sure. So if you type in pytorch a times b plus c
*  What this is going to do is it's going to first multiply add and b a and b and store that result into memory
*  And then it is going to add c by reading that result from memory reading c for memory and writing that out to memory
*  Um, there is way more loads and stores to memory than you need there
*  If you don't actually do a times b as soon as you see it if you wait
*  Until the user actually realizes that tensor until the laziness actually resolves. Um, you confuse that plus c
*  This is like it's the same way haskell works
*  So, uh, what's the process of porting a model into tiny grad?
*  So tiny grad's front end looks very similar to pytorch. Um, I probably could make a perfect
*  Or pretty close to perfect interrupt layer if I really wanted to I think that there's some things that are nicer about tiny grad syntax
*  Than pytorch, but the front end looks very torch like you can also load in onyx models
*  Um, we have
*  More onyx tests passing than core ml
*  Okay, so we'll pass onyx runtime soon
*  What about like the developer experience with tiny grad? Um, what it feels like what a
*  um
*  Versus pytorch by the way, I really like pytorch. I I think that it's actually a very good piece of software
*  Um, I think that they've made a few different trade-offs and these different trade-offs are uh,
*  Where you know tiny grad takes a different path?
*  One of the biggest differences is it's really easy to see the kernels that are actually being sent to the gpu
*  Right if you run pytorch on the gpu
*  You like do some operation and you don't know what kernels ran
*  You don't know how many kernels ran you don't know how many flops were used
*  You don't know how much memory accesses were used tiny grad type debug equals two and it will show you in this beautiful style
*  Um every kernel that's run
*  How many flops and how many bytes?
*  So can you just
*  Linger on what problem tiny grad solves tiny grad solves the problem of porting new ml accelerators quickly
*  one of the reasons uh tons of these companies now, I think um
*  Sequoia marked graph core to zero
*  right cerebus
*  tens torrent
*  grok
*  All of these ml accelerator companies they built chips. The chips were good. The software was terrible
*  Uh, and part of the reason is because I think the same problem is happening with dojo
*  It's really really hard to write a pytorch port
*  Because you have to write 250 kernels and you have to tune them all for performance
*  Uh, what does jim jim color think about tiny grad?
*  You guys hung out quite a bit. So he's uh, you know, he's he was involved. He's involved with chan store. What's his uh,
*  Praise and what's his criticism of what you're doing with your life?
*  look
*  My prediction for tens torrent is that they're going to pivot to making risk five chips
*  Cpus cpus
*  Why
*  Because ai accelerators are a software problem. Not really a hardware problem. Oh interesting. So you don't think
*  You think the diversity of ai accelerators in the hardware space is not going to be a thing that exists long term
*  I think what's going to happen is if I can finish, okay
*  If you're trying to make an ai accelerator
*  You better have the capability of writing a torch level performance stack on nvidia gpus
*  If you can't write a torch stack on nvidia gpus, and I mean all the way I mean down to the driver
*  There's no way you're going to be able to write it on your chip because your chip is worse than an nvidia gpu
*  The first version of the chip you tape out. It's definitely worse. Are you saying writing that stack is really tough?
*  Yes, and not only that actually the chip that you tape out almost always because you're trying to get advantage over nvidia
*  You're specializing the hardware more
*  It's always harder to write software for more specialized hardware like a gpu is pretty generic
*  And if you can't write an nvidia stack, there's no way you can write a stack for your chip
*  So my approach with tiny grad is first write a performant nvidia stack. We're targeting amd
*  So you did say a few to nvidia a little bit with love with love. Yeah, but so like the yankees, you know
*  I'm a metz fan. Oh, you're you're you're a metz fan
*  A risk a risk fan and a mess fan. What's the hope that amd has and you did uh build with amd recently that I saw
*  uh, how does the uh
*  The the 7900 xtx compared to the rtx 4090 or 4080
*  Well, let's start with the fact that the 7900 xtx kernel drivers don't work and if you run demo apps in loops it panics the kernel
*  Okay, so this is a software issue
*  Lisa sue responded to my email
*  Oh, I reached out I was like
*  This is you know
*  really
*  like I understand if your
*  Seven by seven transposed winnegrad com is slower than nvidia's but literally when I run demo apps in a loop the kernel panics
*  So just adding that loop
*  Yeah, I just I just literally took their demo apps and wrote like while true semi-colon do the app semi-colon done in a bunch of screens
*  Right. This is like like the most primitive fuzz testing
*  Why do you think that is they're just not seeing a market in the in um
*  machine learning
*  They're changing they're trying to change they're trying to change and I had a pretty positive interaction with them this week last week
*  I went on youtube. I was just like that's it. I give up on amd like this is their driver doesn't like i'm not gonna i'm not gonna
*  You know, i'll go with intel gpus. All right intel gpus have better drivers
*  So you're kind of spearheading
*  the diversification of
*  gpus
*  Yeah, and i'd like to extend that diversification to everything i'd like to diversify
*  the
*  right the more
*  My central thesis about the world is
*  There's things that centralize power and they're bad and there's things that decentralize power and they're good
*  Everything I can do to help decentralize power i'd like to do
*  So you're really worried about the centralization of nvidia that's interesting and you don't have a fundamental hope for the
*  the proliferation of asics
*  uh except in the cloud
*  I'd like to help them with software. No, actually there's only the only asec that is remotely successful is google's tpu
*  And the only reason that's successful is because google wrote a machine learning framework
*  All right. I think that you have to write a competitive machine learning framework in order to be able to build an asec
*  You think meta with pytorch builds a competitor
*  I hope so
*  They have one they have an internal one internal. I mean, uh public facing with a nice cloud interface and so on
*  I don't want a cloud
*  You don't like cloud. I don't like cloud. What do you think is the fundamental limitation of cloud?
*  Fundamental limitation of cloud is who owns the uh the off switch. So it's uh power to the people. Yeah
*  And you don't you don't like the man to have all the power exactly. All right
*  And right now the only way to do that is with nvidia gpus if you want performance
*  and stability
*  Interesting it's uh, it's a costly investment emotionally to go with amds
*  Well, let me add sort of on a tangent to ask you what what um
*  You've built quite a few pcs. What's your advice on how to build a good custom pc?
*  For uh, let's say for the different applications that you use for gaming for machine learning
*  Well, you shouldn't build one. You should buy a box from the tiny corp
*  I heard rumors whispers
*  About this box in the tiny corp. What's what's this thing look like? What is it? What is it called?
*  It's called the tiny box tiny box. Um, it's fifteen thousand dollars. Yep, and
*  It's almost a pay to flop of compute. It's over 100 gigabytes of gpu ram
*  It's over five terabytes per second of gpu memory bandwidth
*  uh
*  i'm gonna put like four nvme's in in in raid you're gonna get like
*  20 30 gigabytes per second of drive read bandwidth
*  i'm gonna i'm gonna build like
*  The best deep learning box that I can that plugs into one wall outlet
*  Okay, can you go through those specs again a little bit from your from memory?
*  Yeah, so it's almost a pay to flop of compute. So md intel
*  Today i'm leaning toward amd
*  Um, but we're pretty agnostic to the type of compute
*  The the the main limiting spec is a 120 volt 15 amp circuit
*  Okay, well I mean it because in order to like like there's a plug over there, right
*  You have to be able to plug it in
*  Um, we're also going to sell the tiny rack which like what's the most power you can get into your house without arousing suspicion?
*  Uh, and one of the one of the answers is an electric car charger. Wait, where does the rack go your garage?
*  Interesting the car charger a wall outlet is about 1500 watts a car charger is about 10 000 watts
*  What is the most amount of power you can get your hands on without arousing suspicion? That's right george hoss. Okay
*  So the the tiny box and you said nvme's and raid
*  Uh, I forget what you said about memory all that kind of stuff. Okay. So what about what gpus?
*  Again probably probably 7900 xtx's but maybe 3090s maybe a 770s
*  Those are intel's you're flexible or still exploring i'm still exploring. I want to I want to deliver a really good experience to people
*  And yeah, what gpus I end up going with again i'm leaning toward amd
*  It will see you know in my email what I what I said to amd is like
*  Just dumping the code on github is not open source open source is a culture
*  Open source means that your issues are not all one-year-old stale issues
*  open source means
*  Developing in public and if you guys can commit to that I see a real future for amd as a competitor to a video
*  Well, i'd love to get a tiny box to mit so whenever it's ready
*  Let's do it. We're taking pre-orders. I took this from elon. I'm like a hundred dollar fully refundable pre-orders
*  Is it going to be like the cyber truck? It's going to take a few years or no i'll try to do it faster
*  It's a lot simpler. It's a lot simpler than a truck
*  well, there's complexities not to just the
*  Uh putting the thing together but like shipping and all this kind of stuff
*  The thing that I want to deliver to people out of the box is being able to run 65 billion parameter llama
*  In fp16 in real time in like a good like 10 tokens per second or five tokens per second or something just it works
*  Mama's running
*  Uh or something like llama
*  Experience yeah, or I think falcon is is the new one experience a chat with the largest language model that you can have in your house
*  Yeah from from a wall plug from a wall plug. Yeah, actually for inference. It's not like even more power would help you get more
*  Even more power wouldn't get you more
*  No, there's just the biggest parameter the biggest model released is is 65 billion parameter llama as far as I know
*  So it sounds like tiny box will naturally uh pivot towards company number three because you could just get the girlfriend
*  and uh
*  or boyfriend
*  That one's harder actually the boyfriend is harder boyfriend's harder. Yeah, I think that's a
*  Very biased statement. I know a lot of people just see what's what
*  Why is it harder to replace a boyfriend than other girlfriend with the artificial llm?
*  Because women are attracted to status and power and men are attracted to youth and beauty
*  I don't know. I think you both well first of all, you're using language mostly uh to
*  To communicate
*  Youth and beauty and power and status but status fundamentally is a zero sum game
*  Right, whereas youth and beauty are not
*  No, I think status is a narrative you can construct
*  So it's a very good thing that you can use it to communicate with your partner
*  I don't know. I just think that that's why it's harder. You know, yeah, maybe it is my biases
*  I think status is way easier to fake. I also think that you know men are probably more desperate and more likely to buy my product
*  So maybe they're a better target market
*  Desperation is interesting easier to fool. Yeah, that's I could I could see that. Yeah, look I mean look
*  I know you can look at porn viewership. I mean, I think it's a little bit more
*  It's a little bit more difficult to get a girlfriend. I think it's a little bit more difficult to get a girlfriend
*  Yeah, look I mean look I know you can look at porn viewership numbers, right a lot more men watch porn than women
*  You can ask why that is
*  Wow, there's a lot of questions and answers you can get there
*  Anyway with uh with the tiny box how many gpus in tiny box six
*  Oh man, i'll tell you why it's six. Yeah, uh, so amd epic processors have 128 lanes of pcie
*  um, I want to leave enough lanes for
*  some uh drives
*  And I want to leave enough lanes for some networking
*  How do you do cooling for something like this? Ah, that's one of the big challenges
*  Not only do I want the cooling to be good. I want it to be quiet
*  I want the tiny box to be able to sit comfortably in your room. This is really going towards the girlfriend thing
*  Because you want to run the llm. Yeah, i'll give i'll give them more. I mean I can talk about how it relates to company number one
*  Call my ai
*  well
*  But yes quiet. Oh quiet because you maybe potentially want to run it in a car
*  No, no quiet because you want to put this thing in your house and you want it to coexist with you if it's screaming
*  It's 60 db. You don't want that in your house. You'll kick it out 60 db. Yeah
*  Yeah, I want like 40 45. So how do you make the cooling? Uh quiet? That's an interesting problem in itself
*  Um, a key trick is to actually make it big ironically. It's called the tiny box
*  Yeah, but if I can make it big um, a lot of that noise is generated because of high pressure air
*  If you look at like a one u server a one u server has these super high pressure fans
*  They're like super deep and they they're like genesis
*  Versus if you have something that's big well, I can use a big and you know
*  You know
*  They call them big ass fans those ones that are like huge on the ceiling
*  And they're completely silent. So tiny box
*  Will be big
*  It is the uh, I do not want it to be large according to ups. I want it to be shippable as a normal package
*  But that's my constraint there
*  Interesting well the the fans stuff it can't can't be assembled on location or no
*  No
*  No, it has to be well here. You're
*  Look, I want to give you a great out of the box experience. I want you to lift this thing out
*  I want it to be like like the mac, you know
*  Tiny box the apple experience. Yeah
*  I love it. Okay, and so tiny box would run
*  tiny grad
*  like what what what do you envision this whole thing to look like we're talking about like
*  Uh linux with the full
*  software engineering
*  environment
*  And just not pie torch, but tiny grad. Yeah, we did a poll of people want you bunt to our arch
*  We're gonna stick with you bunt to oh interesting. What's your favorite?
*  flavor of
*  Buntu I like up onto my day. However, we pronounce that meat
*  So, how do you uh, you've gotten llama into tiny grad you've gotten stable diffusion into tiny grad
*  Stable diffusion is tiny grad. What was that? Like can you comment on like what are
*  um
*  What are these models? What's interesting about porting them?
*  So what's yeah, like what are the the challenges what what's naturally what's easy all that kind of stuff?
*  There's a really simple way to get these models into tiny grad and you can just export them as onyx and then tiny grad can run onyx
*  Um, so the ports that I did of llama stable diffusion and now whisper are more academic to teach me about the models
*  But they are cleaner than the pie torch versions. You can read the code. I think the code is easier to read. It's less lines
*  There's just a few things about the way tiny grad writes things. Here's here's a complaint. I have about pie torch
*  Nn dot relu is a class
*  Right. So when you create a when you create an nn module, you'll put your nn relus
*  As in a knit and this makes no sense. Relu is completely stateless
*  Why should that be a class?
*  But that's more like a software engineering thing or do you think it has a cost on performance?
*  Oh, no, it doesn't have a cost on performance. Um, but yeah, no, I think that it it's
*  That's what I mean about like tiny grad's front end being cleaner
*  I see
*  Uh, what do you think about mojo? I don't know if you've been paying attention to the programming language that does
*  um some interesting ideas that kind of
*  Intersect tiny grad. I think that there is a spectrum and like on one side you have mojo and on the other side
*  You have like ggml
*  Um, ggml is this like we're gonna run llama fast on mac
*  Okay, we're gonna expand out to a little bit, but we're gonna basically like depth first
*  Right mojo is like we're gonna go breath first. We're gonna go so wide that we're gonna make all of python fast
*  And tiny grads in the middle
*  Tiny grads we are going to make neural networks fast
*  Yeah, but they uh, they try to really
*  Get it to be fast compiled down to specifics
*  Hardware and make that compilation step
*  As flexible and resilient as possible. Yeah, but they've turned completeness
*  And that limits you
*  Turn that's what you're seeing. It's somewhere in the middle. So you're actually going to be targeting some accelerators some
*  Like some some number not one
*  My goal is step one build an equally performance stack to pytorch on nvidia and amd
*  But with way less lines and then step two is okay, how do we make an accelerator, right?
*  But you need step one. You have to first build the framework before you can build the accelerator
*  Uh, can you explain ml perf?
*  What's your approach in general to benchmarking tiny grad performance?
*  so
*  I'm much more of a
*  like
*  Build it the right way and worry about performance later
*  um, there's a bunch of things where I haven't even like
*  Really dove into performance the only place where tiny grad is competitive performance wise right now is on qualcomm gpus
*  So tiny grads actually used an open pilot to run the model. So the driving model is is tiny grad
*  When did that happen that transition?
*  About eight months ago now
*  Um, and it's two x faster than qualcomm's library
*  What's the hardware of open that open pilot runs on the the the comma? Yeah, it's a snapdragon 845
*  Okay, so this is using the gpu so the gpu is an adreno gpu
*  There's like different things. There's a really good microsoft paper that talks about like mobile gpus and why they're different from desktop gpus
*  Um, one of the big things is in a desktop gpu. You can use buffers
*  Uh on a mobile gpu image textures are a lot faster
*  And a mobile gpu image textures and image, okay
*  And so you want to be able to leverage that
*  I want to be able to leverage it in a way that it's completely generic, right?
*  So there's a lot of this xiaomi has a pretty good open source library from o gp is called mace
*  Where they can generate where they have these kernels, but they're all hand coded
*  Right, so that's great. If you're doing three by three confs. That's great if you're doing dense matmols
*  But the minute you go off the beaten path a tiny bit
*  Well, your performance is nothing since you mentioned open pile. I'd love to get an update
*  In the company number one comma ai world, how are things going there in the development?
*  of uh semi-autonomous driving
*  You know
*  Almost no one talks about fsd anymore and even less people talk about open pilot
*  We've solved the problem like we solved it years ago
*  What's the problem exactly?
*  Well, how do you look what what is solving it mean?
*  Solving means how do you build a model that outputs a human policy for driving?
*  How do you build a model that given a reasonable set of sensors outputs a human policy for driving?
*  Uh, so you have, you know companies like wayman cruise which are hand coding these things that are like quasi human policies
*  Then you have
*  Tesla and maybe even to more of an extent comma asking. Okay. How do we just learn human policy from data?
*  Yeah
*  The big thing that we're doing now and we just put it out on twitter
*  At the beginning of comma
*  We published a paper called learning a driving simulator
*  And the way this thing worked was it's a it was an auto encoder
*  And then an rnn in the middle, right? Uh, you take an auto encoder you
*  Compress the picture you use an rnn predict the next date
*  And these things were you know, it was a laughably bad simulator, right? This is 2015 era machine learning technology
*  Today we have vq vae and transformers
*  We're building drive gpt basically
*  drive gpt
*  Okay, uh
*  So and it's trained on what is it trained in a self-supervised way?
*  It's trained on all the driving data to predict the next frame
*  So really trying to uh learn a human policy. What would a human do?
*  Well, actually our simulator is conditioned on the pose so it's actually a simulator you can put in like a state action pair
*  And get out the next state
*  Okay, um, and then once you have a simulator you can do rl in the simulator and rl will get us that human policy
*  So transfers, yeah
*  Rl with a reward function not asking is this close to the human policy but asking what a human disengage if you did this behavior
*  Okay, let me think about the distinction there. What a human disengage
*  Yeah
*  What a human disengage
*  that um
*  correlates I guess with the human policy, but it could be different so it's it uh, it doesn't just say what would a human do it says
*  What would a good human driver do?
*  And uh such that the experience is comfortable
*  But also not annoying in that like the thing is very cautious
*  So it's in the finding a nice balance. That's that's interesting. It's a nice it's asking exactly the right question
*  What will make our customers happy?
*  Right a system that you never want to disengage because usually disengagement is this
*  Almost always a sign of i'm not happy with what the system is doing usually
*  Um, there's some that are just I felt like driving and those are always fine, too
*  But they're just going to look like noise in the data
*  But even I felt like driving
*  Maybe yeah, that's even that's a signal. Like why do you feel like driving?
*  you're
*  you need to uh, re uh calibrate your
*  Relationship with the car. Okay. So what that that's really interesting. Um, how close are we to solving self-driving?
*  um
*  It's hard to say
*  We haven't completely closed the loop yet. So we don't have anything built that truly looks like that architecture yet
*  We have prototypes and there's bugs
*  Um, so we are a couple bug fixes away might take a year might take 10
*  What's the nature of the bugs? Are these uh?
*  These major philosophical bugs logical bugs, what kind of what kind of bugs are we talking about?
*  They're just like they're just like stupid bugs and like also we might just need more scale
*  We just massively expanded our compute cluster at kama
*  We now have about two people worth of compute 40 beta flops
*  Well people
*  People are different
*  20 beta flops that's a person. It's just it's just a unit right horses are different too, but we still call it a horsepower
*  Yeah, but there's something different about mobility than there is about
*  uh
*  Perception and action in a very complicated world
*  But yes, well, yeah, of course not all flops are created equal if you have randomly initialized weights, it's not gonna
*  Not all flops are created equal. So we're doing way more useful things than others. Yeah. Yep
*  Tell me about it. Okay. So more data scale means more scaling compute or scale in scale of data both
*  Diversity of data diversity is very important in data
*  uh
*  Yeah, I mean we have
*  So we have about I think we have like
*  5 000 daily actives
*  How would you evaluate how uh fsd is doing?
*  Pretty well driving pretty well
*  How's that race going?
*  Between kama and fsd tesla has always wanted two years ahead of us
*  They've always been one to two years ahead of us and they probably always will be because they're not doing anything wrong
*  What have you seen that's since the last time we talked that are interesting architectural decisions training decisions like the way
*  The way they deploy stuff the architectures they're using in terms of the software how the teams are run all that kind of stuff data collection
*  Anything interesting? I mean, I know they're moving toward more of an end-to-end approach
*  so
*  Creeping towards end to end as much as possible
*  Across the whole thing the the training the data collection everything they also have a very fancy simulator
*  They're probably saying all the same things we are they're probably saying we just need to optimize, you know
*  What is the reward will get negative reward for disengagement? Right? Like
*  Everyone kind of knows this it's just a question who can actually build and deploy the system
*  Yeah, I mean this good requires good software engineering. I think yeah
*  And the right kind of hardware
*  Yeah, the hardware to run it
*  You still don't believe in cloud in that regard?
*  I have a
*  compute cluster in my uh
*  Us 800 amps tiny grad it's 40 kilowatts at idle our data center
*  Diving crazy with 40 kilowatts just burning just when the computers are idle just when i'm sorry. Sorry compute cluster
*  Compute cluster, I got it. It's not a data center. Yeah now data centers are clouds. We don't have clouds
*  Data centers have air conditioners. We have fans that makes it a compute cluster
*  I'm guessing this is a kind of a legal distinction. That's sure. Yeah, we have a compute cluster
*  You said that you don't think lms have consciousness or at least not more than a chicken
*  Do you think they can reason is there something interesting to you about the word reason?
*  about some of the capabilities that we think is kind of human to be able to
*  Integrate complicated information and
*  through a chain
*  of thought
*  Arrive at a conclusion that feels novel
*  A novel integration of the of disparate facts
*  Yeah, I I don't think that there's I think they can reason better than a lot of people
*  Hey, isn't that amazing to you though?
*  Isn't that like an incredible thing that a transformer could achieve? I mean
*  I think that calculators can add better than a lot of people
*  but language feels like
*  reasoning through the process of language which
*  Looks a lot like thought
*  Making brilliancies in chess which feels a lot like thought
*  Whatever new thing that ai can do everybody thinks is brilliant and then like 20 years go by and they're like well
*  Yeah, but chess that's like mechanical like adding that's like mechanical. So you think language is not that special. It's like chess. It's like chess
*  I don't know
*  Because it's very human we we take it
*  uh, we listen there's something different between chess and
*  and uh language chess is a game that a
*  Subset of population plays language is something we use non-stop for all of our human interaction and human interaction is fundamental to
*  society so it's like holy shit
*  this
*  this language thing is not so difficult to like
*  Create in the machine. The problem is if you go back to 1960 and you tell them that you have a machine that can play
*  amazing chess
*  Of course someone in 1960 will tell you that machine is intelligent
*  Someone in 2010 won't what's changed right today? We think that these machines that have language are intelligent
*  But I think in 20 years we're going to be like, yeah, but can it reproduce?
*  So reproduction
*  Yeah, we might redefine what it means to to be uh
*  What is it a high performance living organism on earth humans are always going to define a niche for themselves like well
*  You know
*  We're better than the machines because we can you know, and like they tried creative for a bit, but no one believes that one anymore
*  But niche is is that is that delusional or is there some accuracy to that because maybe like with chess you start to realize like
*  That that uh, we have ill-conceived notions of what uh,
*  What makes human special?
*  like the apex
*  organism on earth
*  Yeah, and I think maybe we're gonna go through that same thing with language
*  And that same thing with creativity
*  But language carries these notions of truth and so on and so we might be like wait
*  Maybe truth is not carried by language. Maybe there's like a deeper thing. The niche is getting smaller. Oh boy
*  But no, no, no, you don't understand humans are created by god and machines are created by humans therefore
*  Right, like that'll be the last niche we have
*  So what do you think about this the rapid development of alums if we could just like stick on that
*  It's still incredibly impressive like with chad gbt just even chad gbt. What are your thoughts about?
*  reinforcement learning with human feedback on these large language models
*  I'd like to go back to when calculators first came out
*  And or computers and like I wasn't around look i'm i'm 33 years old
*  and to like
*  See how that affected
*  Like society maybe you're right so I want to put on the
*  The uh, the big picture hat here. Oh my god a refrigerator. Wow
*  the refrigerator electricity all that kind of stuff
*  but
*  No with the internet
*  Large language models seeming human like basically passing a touring test
*  It seems it might have really at scale rapid transformative effects on society
*  You're saying like other technologies have as well
*  So maybe calculator is not the best example that because that just seems like
*  I mean, well, no, maybe calculator for milk man the day he learned about refrigerators. He's like i'm done
*  You're telling me you can just keep the milk in your house
*  You don't need to deliver it every day. I'm done
*  Well, yeah, you have to actually look at the practical impacts of certain technologies that they've had
*  Yeah, probably electricity is a big one and also how rapidly it spread
*  And also how rapidly it spread man the internet is a big one. I do think it's different this time though
*  Yeah, it just feels like stuff is getting smaller
*  The initial humans
*  That makes humans special
*  It feels like it's getting smaller rapidly though, doesn't it or is that just the feeling we dramatize everything I think we dramatize everything
*  I think that that that you asked the milkman when he saw refrigerators and they're gonna have one of these in every home
*  Yeah, yeah, yeah
*  Yeah, maybe but boys are impressive
*  so much more impressive than seeing a
*  chess world champion ai system, I disagree actually
*  I disagree
*  I think things like mu zero and alpha go are so much more impressive because these things are playing
*  Beyond the highest human level
*  The language models are writing
*  Middle school level essays and people are like, wow, it's a great essay
*  It's a great five paragraph essay about the causes of the civil war. Okay, forget the civil war just generating code codex
*  You're saying it's mediocre code terrible, but I don't think it's terrible. I think it's just mediocre code. Yeah often
*  close to correct
*  Like for mediocre just the scariest kind of code
*  I spend five percent of time typing and 95 percent of time debugging
*  The last thing I want is close to correct code
*  I want a machine that can help me with the debugging not with the typing, you know, it's like l2 level two
*  Driving similar kind of thing. Yeah, it's you still
*  Should be a good programmer in order to modify. I wouldn't even say debugging. It's just modifying the code reading it
*  Don't think it's like level two driving
*  I think driving is not tool complete and programming is meaning you don't use like the best possible tools to drive
*  Right. You're not you're not like like like
*  Cars have basically the same interface for the last 50 years. Yep. Computers have a radically different interface
*  Okay, can you describe the concept of tool complete?
*  Yeah, so think about the difference between a car from 1980 and a car from today. Yeah, no difference really
*  It's got a bunch of pedals. It's got a steering wheel
*  Great. Maybe now it has a few adas features, but it's pretty much the same car
*  All right, you have no problem getting into a 1980 car and driving it
*  You take a programmer today who spent their whole life doing javascript and you put them in an apple 2e prompt
*  And you tell them about the line numbers in basic
*  But how do I insert something between line 17 and 18? Oh wow
*  uh, but the
*  So you in tool you're putting in the programming languages. So it's just the entirety stack of the tooling
*  Exactly. So it's not just like the like ids or something like this. It's uh, everything. Yes
*  It's ids the languages the runtimes. It's it's everything and programming is is tool complete. So like almost if
*  If if codecs or copilot are helping you
*  That actually probably means that your framework or library is bad and there's too much boilerplate in it
*  Yeah, but don't you think so much programming has boilerplate tiny grad is now 2700 lines
*  And it can run llama and stable diffusion and all of this stuff is in 2700 lines boilerplate and
*  Abstraction indirections and all these things are just bad code
*  Well
*  Let's talk about good code and bad code
*  There's a I would say I don't know for generic scripts that I write just offhand like I like 80 percent of it is written by gpt
*  Just like quick quick like offhand stuff. So not like libraries not like
*  Performing code not stuff for robotics and so on just quick stuff because your basic so much of programming is doing some
*  Some yeah boilerplate but to do so efficiently and quickly
*  Because you can't really automate it fully with like generic method like a generic kind of
*  Um id type of recommendation something like this you do need to have some of the complexity of language models
*  Yeah, I guess if I was really writing like maybe today if I wrote like a lot of like data parsing stuff
*  Yeah, I mean I don't play ctfs anymore
*  But if I still play ctfs a lot of like it's just like you have to write like a parser for this data format
*  Like I wonder or like admin of code
*  I wonder when the models are going to start to help with that kind of code and they may
*  They may and the models also may help you with speed
*  Yeah, the models are very fast
*  But where the models won't I my programming speed is not at all limited by my typing speed
*  And
*  In very few cases it is yes if i'm writing some script to just like parse some weird data format
*  Sure, my programming speed is limited by my typing speed. What about looking stuff up?
*  Because that's essentially a more efficient lookup, right? You know
*  When I was at when I was at twitter, I tried to use uh chat gpt to uh to like
*  Ask some questions like what's the api for this and it would just hallucinate it would just give me completely made up api functions
*  That sounded real
*  Well, do you think that's just a temporary kind of stage?
*  You don't think it'll get better and better and better in this kind of stuff because like it only hallucinates stuff in in the edge cases
*  Yes, if you're writing generic code, it's actually pretty good
*  Yes, if you are writing an absolute basic like react app with a button, it's not going to hallucinate sure
*  No, there's kind of ways to fix the hallucination problem. I think facebook has an interesting paper. It's called atlas
*  and it's actually weird the way that we do, uh language models right now where all of the
*  uh
*  Information is in the weights
*  And the human brain is not really like this. There's like a hippocampus and a memory system
*  So why don't llms have a memory system and there's people working on them. I think future llms are going to be like smaller
*  But are going to run looping on themselves and are going to have retrieval systems
*  And the thing about using a retrieval system is you can cite sources
*  explicitly
*  Which is uh
*  Really helpful to integrate the human into the loop of the of the thing because you can go check the sources and you can
*  Investigate so whenever the thing is hallucinating you can like have the human supervision. So that's pushing it towards level two kind of that's going to kill google
*  Wait, which part when someone makes an llm that's capable of citing its sources. It will kill google
*  Lm that's citing its sources because that's basically a search engine
*  That's what people want in the search engine, but also google might be the people that build it maybe and put ads on it
*  I'd count them out
*  Why is that? What do you think who who wins this? Uh race we got who are the competitors? All right, we got
*  Tiny corp. I don't know if that's
*  Yeah, I mean you're a legitimate competitor in that i'm not trying to compete on that
*  You're not no not as it's gonna accidentally stumble into that competition
*  You don't think you might build a search engine to replace google search
*  When I started comma I said over and over again, i'm going to win self-driving cars. I still believe that
*  I have never said i'm going to win search with the tiny corp and
*  I'm never going to say that because I won't the night is still young
*  We don't you don't know how hard is it to win search?
*  in this new route like it's
*  It feels I mean one of the things that chat gpt kind of shows that there could be a few interesting tricks
*  That really have that create a really compelling product some startup is going to figure it out
*  I think I think if you ask me like google's still the number one webpage
*  I think by the end of the decade google won't be the number one web page anymore
*  So you don't think google because of the how big the corporation is?
*  Look, I I would put a lot more money on mark zuckerberg
*  Why is that?
*  Because mark zuckerberg's alive
*  Like this is all paul graham assay startups are either alive or dead google's dead
*  Face versus live facebook is alive. That's alive meta meta. You see what I mean?
*  Like that's just like like like mark zuckerberg. This is mark zuckerberg reading that paul graham assing and being like i'm gonna show everyone
*  How alive we are i'm gonna change the name
*  So you don't think there's this
*  gutsy
*  pivoting engine
*  of that
*  Like google doesn't have that the the kind of engine that the startup has like constantly, you know what being alive, I guess
*  When I listen to your sam altman podcast, um, he talked about the button
*  Everyone who talks about ai talks about the button the button to turn it off, right?
*  Do we have a button to turn off google?
*  Is anybody in the world capable of shutting google down?
*  What does that mean exactly the company or the search engine we shut the search engine down can we shut the company down?
*  either
*  Can you elaborate on the value of that question? Does sundar pershaya have the authority to turn off google.com tomorrow?
*  Who has the authority it's a good question does anyone does anyone
*  Yeah, i'm sure
*  Are you sure?
*  No, they have the technical power, but do they have the authority? Let's say sundar pershaya made this his sole mission
*  He came into google tomorrow and said i'm gonna shut google.com down. Yeah
*  I don't think you keep this position too long
*  And what is the mechanism by which he wouldn't keep his position well
*  Boards and shares and corporate undermining and oh my god. Our revenue is zero now
*  Okay, so what I mean, what's the case you're making here? So the the capitalist machine prevents you from
*  Having the button. Yeah, and it will have it. I mean this is true for the ai's too, right? There's no turning the ai's off
*  There's no button. You can't press it
*  Now does mark zuckerberg have that button for facebook.com?
*  Yeah, it's probably more I think he does
*  I think he does and this is exactly what I mean and why I bet on him so much more than I bet on
*  Google I guess you could say elon has similar stuff. Oh elon has the button. Yeah
*  Does elon can elon fire the missiles can he fire the missiles?
*  I think some questions are better
*  Unasked right?
*  I mean, you know a rocket an icbm or your rocket that can land anywhere. Isn't that an icbm? Well, yeah, you know
*  Don't ask too many questions
*  my god
*  But the the positive side of the button is that you can innovate aggressively is what you're saying
*  Is which is what's required with?
*  Turning llm into a search engine. I would bet on a startup. I bet it's so easy, right?
*  I bet on something that looks like mid-journey, but for search
*  Just is able to say source a loop on itself
*  I mean, it just feels like one model can take off. Yeah, right and that nice wrapper and some of it scam
*  It's hard to uh
*  Like create a product that just works really nicely
*  Stably the other thing that's going to be cool is there is some aspect of a winner-take-all effect, right? Like once um
*  Someone starts deploying a product that gets a lot of usage you see this with open ai
*  Uh, they are going to get the data set to train future versions of the model
*  Yeah, um, they are going to be able to right, uh, you know
*  I was asked at google image search when I worked there like almost 15 years ago now
*  How does google know which image is an apple and I said the metadata and they're like, yeah
*  That works about half the time. How does google know you'll see the role apples on the front page when you search apple
*  And uh, I don't know. I didn't come up with the answer because I want 12 people click on when they search apple
*  Oh my god. Yeah. Yeah. Yeah, that data is really really powerful. It's the human supervision
*  Uh, what do you think are the chances? What do you think in general that llama was open-sourced? I just uh,
*  did a conversation with uh
*  With mark zuckerberg and he's all in on open source
*  Who would have thought that mark zuckerberg would be the good guy?
*  I mean
*  Who would have thought anything in this world?
*  It's hard to know
*  but open source to you ultimately
*  Is a good thing here
*  undoubtedly
*  you know
*  What's ironic about all these ai safety people is they are going to build the exact thing they fear
*  These we need to have one model that we control in a line
*  This is the only way you end up paper clipped
*  There's no way you end up paper clipped if everybody has an ai so open sourcing is the way to fight the paper clip maximizer
*  Absolutely
*  The only way you think you're going to control it. You're not going to control it
*  so the criticism you have for the ai safety folks
*  is that there is a
*  Belief and a desire for control. Yeah
*  and that belief and desire
*  For centralized control of dangerous ai systems
*  Is not good sam altman won't tell you that gpt4 has 220 billion parameters and is a 16-way mixture model with eight sets of weights
*  Who?
*  Who did you have to murder to get that information?
*  All right
*  I mean look, yes, everyone at open ai knows what I just said was true, right now
*  Ask the question really, you know
*  It upsets me when I like gpt2 when open ai came out with gpt2 and raised a whole fake ai safety thing about that
*  I mean now the model is laughable
*  Like they they used ai safety to hype up their company and it's disgusting
*  Or the flip side of that is they used a relatively weak model in retrospect to explore
*  How do we do ai safety correctly? How do we release things? How do we go through the process? I don't I don't know if
*  Sure, I don't know
*  I don't know how much hype there is charitable interpretation. I don't know how much hype there is in ai safety, honestly
*  Oh, there's so much. I at least don't splitter. I don't know. Maybe twitter's not real life. It is not real life
*  Come on in terms of hype. I mean, I don't
*  I think open ai has been finding an interesting balance between transparency
*  and putting value on um
*  ai safety, you don't think you think just go
*  All out open source to do a llama
*  Absolutely, so do like open source
*  this this is a tough question, which is open source both the
*  base the foundation model and the fine-tuned one so like
*  The model that can be ultra racist and dangerous and like tell you how to build a nuclear weapon. Oh my god
*  Have you met humans?
*  Right like half of these ai. I haven't met most humans. I this makes that's this this allows you to meet every human
*  Yeah, I know but half of these ai alignment problems are just human alignment problems
*  And that's what's also so scary about the language they use. It's like it's not the machines you want to align. It's me
*  But here's the thing
*  It makes it very accessible to ask
*  very uh
*  Questions where the answers have dangerous consequences if you were to act on them
*  I mean, yeah
*  Welcome to the world
*  Well, no for me, there's a lot of friction if I want to find out
*  how to uh
*  I don't know
*  Blow up something. No, there's not a lot of friction. That's so easy
*  No, like what do I search day's bing or do I which search engine do I use? No, there's like lots of stuff
*  No, it feels like I have to keep first off first off first off
*  Anyone who's stupid enough to search for how to blow up a building in my neighborhood is not smart enough to build a bomb
*  Right. Are you sure about that? Yes
*  I feel like I feel like a language model
*  Makes it more accessible for that person who's not smart enough to do they're not gonna build a bomb. Trust me
*  The people the people who are incapable of figuring out how to like ask that question a bit more
*  Academically and get a real answer from it are not capable of procuring the materials which are somewhat controlled to build a bomb
*  No, I think lll makes it more accessible to people with money without the technical know-how, right?
*  To build it like you do really need to know how to build a bomb to build a bomb
*  You can hire people you can find like oh you can hire people to build up
*  You know what? I was asking this question on my stream like can jeff bezos hire a hitman probably not
*  But a language model
*  Can probably help you out
*  Yeah, and you'll still go to jail, right? Like it's not like the language model is god like the language model
*  It's like it's you literally just hired someone on fiverr
*  But you you
*  For in terms of finding hitman is like asking fiverr how to find a hitman. I understand but don't you think wiki?
*  How you know how but don't you think gbt5 will be better because don't you think that information is out there on the internet?
*  I mean, yeah
*  And I think that if someone is actually serious enough to hire a hitman or build a bomb
*  They'd also be serious enough to find the information
*  I don't think so. I think it makes it more accessible if you have if you have enough money to buy hitman
*  I think it decreases the friction
*  Of how hard is it to find that kind of hitman? I I honestly think this the there's a jump
*  in uh
*  Ease and scale of how much harm you can do and I don't mean harm with language
*  I mean harm with actual violence what you're basically saying is like, okay
*  What's going to happen is these people who are not intelligent are going to use machines?
*  To augment their intelligence and now intelligent people and machines intelligence is scary
*  Intelligent agents are scary
*  When i'm in the woods the scariest animal to meet is a human
*  Right. No, no, no, there's look there's like nice california humans. Like I see you're wearing like, you know
*  Street clothes and nikes. All right. Fine. But you look like you've been a human who's been in the woods for a while
*  Yeah, i'm more scared of you than a bear. That's what they say about the amazon when you go to the amazon. It's the human tribes. Oh, yeah
*  So intelligence is scary, right? So to to ask this question in a generic way
*  You're like what if we took everybody who you know, maybe has um, ill intention, but is not so intelligent and gave them intelligence
*  right
*  so
*  We should have intelligence control. Of course
*  We should only give intelligence to good people and that is the absolutely horrifying idea
*  So to you the best defense is actually the best defense is to give more intelligence to the good guys and intelligent
*  Give intelligence to everybody give intelligence to everybody. You know what? It's not even like guns, right?
*  Like people say this about guns, you know
*  What's what's the best defense against a bad guy with a gun good guy with a gun like I kind of subscribe to that
*  But I really subscribe to that with intelligence
*  Yeah, in a fundamental way I agree with you
*  But there's just feels like so much uncertainty and so much can happen rapidly that you can lose a lot of control
*  You can do a lot of damage. Oh, no, we can lose control. Yes. Thank god. Yeah, I hope we can I hope they lose control
*  I want them to lose control more than anything else
*  I think when you lose control, you can do a lot of damage, but you can do more damage when you
*  Centralize and hold on to control is the point you're centralized and held control is tyranny
*  Right. I will always I don't like anarchy either but i'll always take anarchy over tyranny anarchy. You have a chance
*  This human civilization we got going on it's quite interesting. I mean I agree with you. So to you open source
*  Is the way forward here so you admire what facebook is doing here or what meta is doing with the release of them
*  A lot a lot. I lost I lost 80 000 last year investing in meta and when they released llama, i'm like, yeah, whatever man
*  That was worth it
*  It's worth it
*  do you think google and uh
*  Open ai with microsoft will match what what what meta is doing or no?
*  So if I were a researcher
*  Why would you want to work at open ai like, you know, you're just you're on the bad team
*  Like I mean it like you're on the bad team who can't even say that gpt4 has 220 billion parameters
*  So close source to use the bad team
*  Not only close source. I'm not saying you need to make your model weights open
*  I'm not saying that I totally understand. We're keeping our model weights closed because that's our product. All right, that's fine
*  i'm saying like
*  Because of ai safety reasons, we can't tell you the number of billions of parameters in the model
*  That's just the bad guys
*  Just because you're mocking ai safety doesn't mean it's not real. Oh, of course
*  Is it possible that these things can really do a lot of damage that we don't know? Oh my god. Yes
*  Intelligence is so dangerous be it human intelligence or machine intelligence
*  Intelligence is dangerous, but machine intelligence is so much easier to deploy scale like rapidly
*  Like what? Okay, if you have human-like bots on twitter, right?
*  And you have like a thousand of them create a whole narrative
*  like you can
*  Manipulate millions of people but you mean like the intelligence agencies in america are doing right now
*  Yeah, but they're not doing it that that well it feels like you can do a lot they're doing it pretty well
*  What I think they're doing a pretty good job
*  I I suspect they're not nearly as good as a bunch of gbt fueled bots could be well
*  I mean, of course they're looking into the latest technologies for control of people, of course
*  But I think there's a george haas type character that can do a better job than the entirety of them. You don't think so
*  No way
*  No, and i'll tell you why the george haas character can't and I thought about this a lot with hacking
*  Right, like I can find exploits in web browsers. I probably still can I mean I was better out on i24 but
*  The thing that I lack is the ability to slowly and steadily deploy them over five years
*  And this is what intelligence agencies are very good at right intelligence agencies don't have the most sophisticated technology
*  They just have endurance endurance
*  and yeah the financial backing
*  and the infrastructure for the endurance so the more we can
*  Decentralize power like you could make an argument by the way that nobody should have these things and I would defend that argument
*  I would I would like you're saying that look llms and ai and machine intelligence can cause a lot of harm
*  So nobody should have it and I will respect someone philosophically with that position
*  Just like I will respect someone philosophically with the position that nobody should have guns
*  All right, but I will not respect philosophically which with with
*  Only the trusted authorities should have access to this
*  Who are the trusted authorities? You know what i'm not worried about alignment between
*  AI company and their machines i'm worried about alignment between me and ai company
*  What do you think aliezer iedkovsky would say to you?
*  Because he's really against open source. I know and
*  I thought about this. I thought about this and
*  I think this comes down to a
*  Repeated misunderstanding of political power by the rationalists
*  Interesting
*  I think that
*  Elias iedkovsky is scared of these things and I am scared of these things too
*  Everyone should be scared of these things. These things are scary
*  But now you ask about the two possible futures
*  one where a small
*  trusted centralized group of people has them and the other where everyone has them
*  And I am much less scared of the second future than the first
*  Well, there's a small trusted group of people that have control of our nuclear weapons
*  There's a difference again a nuclear weapon cannot be deployed tactically and a nuclear weapon is not a defense against a nuclear weapon
*  Except maybe in some philosophical mind game kind of way
*  But ai is different different how exactly okay, let's say the
*  Intelligence agency deploys a million bots on twitter or a thousand bots on twitter to try to convince me of a point
*  Imagine I had a powerful ai running on my computer saying okay, nice psyop nice psyop nice psyop
*  Okay, here's a psyop. I filtered it out for you
*  Yeah, I mean so you have fundamental hope for that
*  For the for the defense of psyop. I'm not even like I don't even mean these things in like truly horrible ways
*  I mean these things in straight up like ad blocker, right? Yeah, sure bad blocker. I don't want ads
*  Yeah, but they're always finding, you know, imagine I had an ai that could just block all the ads for me
*  So you believe in the
*  The power of the people to always create a not blocker
*  Yeah, I mean I I kind of share that belief. I have that's one of the
*  Deepest optimisms I have is just like there's a lot of good guys
*  So to give you know, you shouldn't hand pick them just
*  Throw out powerful technology out there and the good guys will outnumber and outpower the bad guys
*  Yeah, i'm not even going to say there's a lot of good guys
*  I'm saying that good out number is bad, right good out number is bad in skill and performance
*  Yeah, definitely in skill and performance probably just a number two probably just in general
*  I mean, you know if you believe philosophically in democracy, you obviously believe that
*  um that good out number is bad and
*  Like the only if you give it to a small number of people
*  There's a chance you gave it to good people, but there's also a chance you gave it to bad people
*  If you give it to everybody
*  Well, if good out number is bad, then you definitely gave it to more good people than bad
*  That's really interesting so that's on the safety grounds
*  But then also of course, there's uh other motivations like you don't want to give away your secret sauce
*  Well, that's I mean, I look I respect capitalism
*  I don't think that I think that it would be polite for you to make model architectures open source and fundamental breakthroughs
*  Open source. I don't think you have to make way to open source. You know, what's interesting is that
*  like there's so many possible trajectories in human history where
*  You could have the next google be open source. So for example
*  I don't know if that connection is accurate, but you know wikipedia made a lot of interesting decisions not to put ads
*  Like wikipedia is basically open source. You could think of it that way
*  Yeah
*  And like that's one of the main websites on the internet
*  And like it didn't have to be that way
*  It could have been like google could have created wikipedia put ads on it. You could probably run amazing ads now on wikipedia
*  You wouldn't have to keep asking for money, but
*  It's interesting right? So llama open source llama
*  derivatives of open source llama might win the internet
*  I sure hope so. I hope to see another era. You know, the kids today don't know how good the internet used to be
*  And I don't think this is just all right. Come on. Like everyone's nostalgic for their past
*  But I actually think the internet before
*  Small groups of weaponized corporate and government interests took it over was a beautiful place
*  You know those small small number of companies have created some sexy products
*  But you're saying overall in the long arc of history the centralization of power they have
*  Like suffocated the human spirit at scale. Here's a question to ask about those beautiful sexy products
*  Imagine 2000 google to 2010 google, right a lot changed. We got maps. We got gmail
*  We lost a lot of products too. I think from yeah, I mean somewhere probably got chrome, right?
*  And now let's go from 2010. We got android now. Let's go from 2010 to 2020
*  Well, what does google have? Well search engine maps mail android and chrome. Oh, I see
*  The internet was this
*  You know, I was times person of the year in 2006
*  Yeah
*  I love this. It's you was times person of the year in 2006. All right, like like that's
*  You know so quickly did people forget and I think some of it's social media. I think some of it
*  I hope look I hope that I I don't it's possible that some very sinister things happen
*  I don't I don't know. I think it might just be like the effects of social media
*  But something happened in the last 20 years
*  Oh, okay, so you're just being an old man who's worried about the I think there's always it goes
*  It's the cycle thing that's ups and downs and I think people rediscover the power of distributed of decentralized
*  Yeah, I mean that's kind of like what the the whole like cryptocurrency is trying like that
*  I think crypto is just carrying the flame of that spirit of like stuff should be decentralized
*  It's just such a shame that they all got rich
*  You know, yeah, if you took all the money out of crypto, it would have been a beautiful place. Yeah
*  But no, I mean these people, you know, they they they sucked all the value out of it and took it
*  Yeah, money kind of corrupts the mind somehow it becomes a drug and you corrupted all of crypto
*  You had coins worth billions of dollars that had zero use
*  You still have hope for crypto sure I have hope for the ideas I really do um, yeah, I mean, you know
*  I want the US dollar to collapse
*  I do
*  george hodds
*  Well, let me sort of on on the at as 80 do you think there's some interesting questions there though
*  To solve for the open source community in this case. So like alignment, for example, uh,
*  Or the control problem like if you really have super powerful you said it's scary
*  What do we do with it? So not not control not centralized control, but like
*  If you were then you're gonna see some guy
*  Or gal release a super powerful language model open source and here you are george hodds thinking
*  Holy shit. Okay. What ideas do I have to?
*  combat this thing
*  So what's the idea of this?
*  thing
*  So what ideas would you have? I am
*  So much not worried about the machine
*  Independently doing harm. That's what some of these ai safety people seem to think they somehow seem to think that the machine like
*  Independently is going to rebel against its creator. So you don't think you'll find autonomy?
*  No, this is sci-fi
*  B-movie garbage. Okay. What if the thing writes code basically writes viruses?
*  Viruses if the thing writes viruses, it's because the human
*  Told to write viruses. Yeah, but there's some things you can't like put back in the box
*  That's the that's kind of the whole point is it kind of spreads give it access to the internet. It spreads installs itself
*  Modifies your shit b b b plot sci-fi
*  Not real i'm trying to work. I'm trying to get better at my plot writing the thing the thing that worries me
*  I mean we have a real danger to discuss and that is bad humans using the thing to do whatever bad
*  unaligned ai thing you want but this goes to the
*  Your previous concern that who gets to define who's a good human who's a bad human?
*  Nobody does we give it to everybody and if you do anything besides give it to everybody trust me
*  The bad humans will get it
*  And that's power. It's always the bad humans who get power. Okay power
*  and
*  Power turns even slightly good humans to bad. Sure. That's the intuition you have. I don't know
*  I don't think everyone I don't think everyone I just think that like
*  Here's a the saying that I put in one of my blog posts
*  When I was in the hacking world
*  I found 95 percent of people to be good and five percent of people to be bad
*  Like just who I personally judged as good people and bad people
*  Like they believed about like, you know good things for the world
*  They wanted like flourishing and they wanted, you know growth and they wanted things I consider good, right?
*  I came into the business world with comma and I found the exact opposite
*  I found five percent of people good and 95 percent of people bad. I found a world that promotes psychopathy
*  I wonder what that means. I wonder if that care like uh,
*  I wonder if that's anecdotal or if it uh,
*  If there's true to that there's something about capitalism
*  Well at the core that promotes the people that run capitalism that promotes psychopathy
*  That saying may of course be my own biases, right that may be my own biases that these people are a lot more aligned with me
*  Than these other people
*  Right. Yeah
*  So, you know, I can certainly uh
*  Recognize that but you know in general, I mean this is like like the common sense maxim
*  Which is the people who end up getting power are never the ones you want with it
*  But do you have a concern of super intelligent a gi?
*  Open-sourced
*  And then what do you do with that? I'm not saying control it. It's open source. What do we do with this human species?
*  That's not up to me. I mean, you know, like i'm not a central planner
*  Not central planner, but you'll probably tweet
*  There's a few days left to live for the human species
*  I have my ideas of what to do with it and everyone else has their ideas of what to do with it
*  May the best ideas win, but at this point do you brainstorm like?
*  Because it's not regulation. It could be decentralized regulation where people agree that this is just like
*  We create tools that make it more difficult for you
*  To uh
*  Maybe make it more difficult for code to spread, you know antivirus software this kind of thing
*  But you're saying that you should build ai firewalls. That sounds good. You should definitely be running an ai firewall
*  Yeah, right. You should be running an ai firewall to your mind
*  Right, you're constantly under you know such an interesting idea. It's like info wars man, like I don't know if you're being sarcastic
*  No, i'm dead serious, but I think there's power to that. It's like
*  How do I
*  Protect my mind from influence of human like or superhuman intelligent bots
*  I is not being I would pay so much money for that product. I would pay so much money for that product
*  I would you know how much money i'd pay just for a spam filter that works
*  well on twitter sometimes I
*  would like to have a
*  a uh
*  a protection mechanism for my mind
*  From the outrage mobs, yeah, because they feel like bot-like behavior
*  It's like there's a large number of people that will just grab a viral narrative and attack anyone else that believes otherwise and it's like
*  Whenever someone's telling me some story from the news i'm always like I don't want to hear it cia
*  Opera it's a cia opera like it doesn't matter if that's true or not. It's just trying to influence your mind
*  You're repeating an ad to me
*  With the viral mobs of this is like they're yeah, they're like to me a defense against those those mobs
*  Is just getting multiple perspectives always from from sources that make you feel kind of
*  Like you're getting smarter
*  And just actually just basically feels good like a good documentary
*  Just feels good something feels good about it. It's well done. It's like, oh, okay. I never thought of it this way
*  This just feels good
*  Sometimes the outrage mobs even if they have a good point behind it when they're like mocking and derisive and just aggressive
*  You're with us or against us this this fucking this is why I delete my tweets
*  Yeah, why'd you do that?
*  I was you know, I was I missed your tweets. You know what it is the algorithm promotes toxicity. Yeah
*  and like
*  You know, I think elon has a much better chance of fixing it than the previous
*  uh regime
*  Yeah, but to solve this problem to solve like to build a social network that is actually not toxic
*  without
*  Moderation
*  Mm-hmm
*  Like uh, not the stick but carrot so like where people
*  Uh look for goodness
*  So make it uh catalyze the process of connecting cool people and being cool to each other
*  Yeah
*  Without ever sensory without ever censoring and and and like scott alexander has a blog post
*  I like where he talks about like moderation is not censorship, right?
*  Like all moderation you want to put on twitter, right? Like you could totally make this moderation like just a
*  You don't have to block it for everybody
*  You can just have like a filter button
*  Right that people can turn off if they were like safe search for twitter, right?
*  Like someone could just turn that off, right?
*  So like but then you'd like take this idea to an extreme, right?
*  Well, the network should just show you
*  This is a couch surfing ceo thing, right? If it shows you right now these algorithms are designed to maximize engagement
*  Well turns out outrage maximizes engagement quirk of human quirk of the human mind, right just as I fall for it everyone falls for it
*  Um, so yeah, you gotta figure out how to maximize for something other than engagement
*  And I actually believe that you can make money with that too
*  So it's not I don't think engagement is the only way to make money
*  I actually think it's incredible that we're starting to see I think again
*  Yolanda's doing so much stuff right with twitter like charging people money
*  As soon as you charge people money, they're no longer the product
*  They're the customer
*  And then they can start building something that's good for the customer and not good for the other customer, which is the ad agencies
*  Hasn't hasn't picked up steam
*  I pay for twitter doesn't even get me anything. It's my donation to this new business model. Hopefully working out
*  Sure, but you know you for this business model to work. It's like
*  most people should be signed up to twitter and so the way it was
*  There was something perhaps not compelling or something like this to people think you need most people at all
*  I think that why do I need most people right? Don't make an 8 000 person company make a 50 person company
*  Well, so speaking of which
*  You worked at twitter for a bit I did as an intern
*  The world's greatest intern. Yeah
*  All right, there's been better. There's been better
*  Uh, tell me about your time at twitter. How did it come about and what did you learn from the experience?
*  so I
*  Deleted my first twitter in 2010
*  I had
*  Over 100 000 followers back when that actually meant something
*  and
*  I just saw, you know
*  My co-worker summarized it. Well, he's like
*  Whenever I see someone's twitter page
*  I either think the same of them or less of them. I never think more of them
*  Yeah, right like like, you know, I don't want to mention any names
*  But like some people who like, you know
*  Maybe you would like read their books and you would respect them you see them on twitter and you're like
*  Okay, dude
*  Yeah, but there are some people with same
*  You know who I respect a lot
*  Are people that just post really good technical stuff. Yeah
*  and I guess
*  I don't know. I think I respect them more for it because you you realize oh this wasn't uh,
*  There's like so much depth to this person to their technical understanding of so many different topics
*  Okay, so I try to follow people I try to
*  Consume stuff that's technical machine learning content. There's probably
*  a few of those people
*  and
*  The problem is inherently what the algorithm rewards, right?
*  And people think about these algorithms people think that they are terrible awful things
*  And you know, I love that elon open sourced it. Um, because I mean what it does is actually pretty obvious
*  It just predicts what you are likely to retweet and like and linger on
*  That's what all these algorithms do with tiktok does so all these recommendation engines do
*  And it turns out that the thing that you are most likely to interact with is outrage
*  And that's a quirk of the human condition
*  I mean and there's different flavors of outrage. It doesn't have to be it could be mockery
*  You'd be outraged the topic of outrage could be different. It could be an idea. It could be a person it could be
*  Maybe there's a better word than outrage. It could be drama. Sure. Drama kind of stuff
*  Yeah, but doesn't feel like when you consume it. It's a constructive thing for the individuals that consume it in the long term
*  Yeah, so my time there. I absolutely couldn't believe you know, I got
*  crazy amount of hate, uh, you know just on twitter for working at twitter it seems like
*  People associated with this. I think maybe uh, you were exposed to some of this
*  To connection to elon or is it working on twitter?
*  Twitter and elon like the whole there's just elon's gotten a bit spicy during that time
*  A bit political a bit. Yeah
*  Yeah, you know, I remember one of my tweets. It was never go full republican and elon liked it
*  You know, I think I think
*  Oh boy, I uh, yeah, I mean there's a roller coaster of that but being political on twitter. Yeah boy. Yeah
*  And also being
*  Just attacking anybody on twitter. It comes back at you harder
*  And if his political and attacks sure
*  Sure, absolutely
*  and then letting
*  uh
*  Sort of de-platform people back on
*  Even adds more fun to the to the to the beautiful chaos
*  I was hoping
*  And like I remember when elon talked about buying twitter like six months earlier
*  He was talking about like a principled
*  Commitment to free speech
*  And i'm a big believer and fan of that. I would love to see
*  An actual principled commitment to free speech
*  Of course, this isn't quite what happened
*  Um instead of the oligarchy deciding what to ban you had a monarchy deciding what to ban, right instead of you know
*  All the twitter files shadow
*  Really the oligarchy just decides what cloth masks are ineffective against covid
*  That's a true statement every doctor in 2019 knew it and now i'm banned on twitter for saying it interesting oligarchy
*  Um, so now you have a monarchy and uh, you know, he bans things he doesn't like
*  so, you know, it's just it's just different it's different power and like, you know, maybe I uh,
*  Maybe I align more with him than with the oligarchy, but it's not free speech. Absolutely
*  but I feel like
*  Being a free speech absolutist on the social network requires you to also have tools for the individuals
*  to
*  control what they consume easier like uh,
*  Not censor, you know, but just like control like oh, I like to see more cats
*  And less politics and this isn't even this isn't even remotely controversial
*  This is just saying you want to give paying customers for a product what they want
*  Yeah, and not through the process of censorship but through a process of like what's it? It's individualized, right?
*  It's individualized transparent censorship, which is honestly what I want. What is an ad blocker? It's individualized transparent censorship, right? Yeah, but
*  Censorship is a strong word
*  And people are very sensitive too. I know but you know
*  I just use words to describe what they functionally are and what is an ad blocker? It's just censorship
*  When I look at you right now, I'm looking at you. I'm censoring
*  Everything else out when i'm full when my mind is focused on you
*  That's you can use the word censorship that way
*  But usually when people get very sensitive about the censorship thing, I I think when you have when anyone is allowed to say anything
*  You should probably have tools
*  that
*  Maximize the quality of the experience for individuals. So
*  You know for me like what I really value boy would be amazing to somehow figure out how to do that
*  I love disagreement and debate and people who disagree with each other disagree with me, especially in the space of ideas
*  But the high quality ones so not derision, right? Mazelot's hierarchy of argument. I think it's a real word for it
*  Probably yeah, there's just a way of talking that's like snarky and so on that somehow is
*  Gets people on twitter and they get excited and so on you have like ad hominem refuting the central point
*  I'd like seeing this as an actual pyramid something. Yeah, it's yeah, and it's it's like all of it
*  All the wrong stuff is attractive to people
*  I mean we can just train a classifier to absolutely say what level of mazla's hierarchy of argument are you at?
*  Yeah, if it's ad hominem like okay cool. I turned on the no ad hominem filter
*  I wonder if there's a social network that will allow you to have that kind of filter. Yeah, so
*  Here's the problem with that
*  It's not going to win in a free market
*  Yeah, what wins in a free market is all television today is reality television because it's engaging
*  Right if if engaging is what wins in a free market, right? So it becomes hard to keep these other more nuanced values
*  Well, okay, so that's the experience of being on twitter, but then you got a chance to also
*  And together with other engineers and with elon sort of look
*  Brainstorm when you step into a code base that's been around for a long time, you know, there's other social networks, you know facebook
*  This is old code bases and you step in and see okay
*  How do we make with a fresh mind?
*  Progress on this code base like what what did you learn about software engineering about programming from just experiencing that so my
*  Technical recommendation to elon and I said this on the twitter spaces afterward. I said this
*  many times during my brief internship
*  Was that you need refactors before features
*  This code base was
*  And look i've worked at google. I've worked at facebook
*  Uh facebook has the best code
*  Then google then twitter
*  Um, and you know what you can know this because look at the machine learning frameworks, right?
*  Facebook released pie torch google released tensorflow and twitter released
*  Yeah
*  Okay, so you know
*  It's a proxy but yeah, they're the the google code base is quite interesting
*  There's a lot of really good software engineers there, but the code base is very large
*  The code base was good in 20 in 2005, right? It looks like 2005. There's so many products so many teams, right? It's very difficult to
*  um, I feel like twitter does less like obviously much less than google
*  Google
*  In terms of like the set of features, right?
*  So like it's I can imagine the number of software engineers that could
*  Recreate twitter is much smaller than to recreate google
*  Yeah, I still believe and the amount of hate I got for saying this that 50 people could build and maintain twitter
*  Uh pretty what's the nature of the hate comfortably?
*  That you don't know what you're talking about. You know what it is and it's the same
*  This is my summary of like the hate I get on hacker news
*  it's like
*  When I say i'm going to do something
*  they
*  Have to believe that it's impossible. Yeah, because
*  If doing things was possible
*  They'd have to do some soul searching and ask the question. Why didn't they do anything?
*  So when you say and I do say that's where the hate comes when you say well, there's a core truth to that
*  Yeah, so when you say i'm going to solve self-driving
*  People go like what are your credentials? What the hell are you talking about?
*  What is this is an extremely difficult problem? Of course, you're a noob that doesn't understand the problem deeply
*  Uh, I mean that that was the same nature of hate that probably ilan goween even first talked about autonomous driving
*  Uh, but you know, there's pros and cons to that because like, you know, there is experts in this world
*  No, but the mockers aren't experts the market the the people who are mocking are not experts with carefully reasoned arguments about why you need
*  8 000 people to run a bird app there, but the people are gonna lose their jobs
*  Well that but also there's the software genius that probably says no
*  It's a lot more complicated than you realize but maybe it doesn't need to be so complicated, you know
*  Some people in the world like to create complexity
*  Some people in the world thrive under complexity like lawyers, right lawyers want the world to be more complex because you need more lawyers
*  You need more legal hours, right?
*  Um, I think that's another if there's two great evils in the world. It's centralization and complexity. Yeah, and uh,
*  the one of the sort of hidden
*  Uh side effects of software engineering is
*  Um like finding pleasure and complexity
*  I mean, I don't remember just taking all the software engineering courses and just doing programming and this is just coming up in this
*  uh
*  Uh object-oriented programming kind of idea you don't like not often do people tell you like do the simplest possible thing like
*  Like a professor a teacher is not going to get in front like
*  This is the simplest way to do it
*  They'll say like this is direct there's the right way and the right way at least for a long time
*  You know, especially I came up with like java, right? Like is is there's so much boilerplate so much like
*  So many classes so many like designs and architectures and so on like planning for features
*  Far into the future and planning poorly and all this kind of stuff
*  And then there's this like code base that follows you along and puts pressure on you and nobody
*  Knows what like parts different parts do which slows everything down is the kind of bureaucracy that's instilled in the code as a result
*  Of that, but then you feel like oh well, I follow good software engineering practices
*  Is it is an interesting trade-off because then you look at like the ghetto-ness of like pearl in the old like
*  How quickly you just write a couple lines just get stuff done
*  That trade-off is interesting or bash or whatever these kind of ghetto things you can do in linux
*  One of my favorite things to look at today is how much do you trust your tests?
*  Right. We've put a ton of effort in comma and I put a ton of effort in tiny grad
*  Into making sure if you change the code and the tests pass that you didn't break the code. Yeah
*  Now this obviously is not always true
*  But the closer that is to true the more you trust your tests the more you're like
*  Oh, I got a pull request and the tests pass. I feel okay to merge that the faster you can make progress
*  You're always programming with tests in mind developing tests with that in mind that if it passes it should be good and twitter had a
*  not that
*  So it was impossible to make progress in the code base
*  What other stuff can you say about the code base that made it difficult?
*  Uh, what are some interesting sort of quirks broadly speaking from that?
*  Compared to just your experience with comma
*  And everyone else the real thing that I spoke to a bunch of uh
*  you know like like like
*  Individual contributors at twitter and I just had stashed i'm like, okay, so like
*  What's wrong with this place? Why does this code look like this and they explained to me what twitter's promotion system was?
*  The way that you got promoted at twitter was you wrote a library that a lot of people used
*  Right
*  So some guy wrote an nginx replacement for twitter
*  Why does twitter need an nginx replacement? What was wrong with nginx?
*  Well, you see you're not going to get promoted if you use nginx
*  But if you write a replacement and lots of people start using it as the twitter front end for their product
*  Then you're going to get promoted right so interesting because like from the individual perspective, how do you incentivize?
*  How do you create the kind of incentives that will reach a lead to a great code base?
*  What's okay? What's the answer to that?
*  so
*  What I do at comma and at uh
*  And you know at tiny corp is you have to explain it to me
*  You have to explain to me what this code does
*  All right, and if I can sit there and come up with a simpler way to do it you have to rewrite it
*  You have to agree with me about the simpler way. Um, you know, obviously we can have a conversation about this
*  It's not a it's not dictatorial. But if you're like wow wait, that actually is way simpler
*  Like like the simplicity is important
*  Right, but that requires people that overlook the code
*  At the highest levels to be like, okay, it requires technical leadership. You trust. Yeah technical leadership
*  So managers or whatever should have to have technical savvy deep technical savvy
*  Managers should be better programmers than the people who they manage. Yeah
*  And that's not always obvious to create trivial to create especially large companies
*  Managers get soft and like you know, and this is just i've instilled this culture at comma and comma has better programmers than me who work
*  There but you know again
*  I'm like the you know, the old guy from goodwill hunting. It's like look man
*  you know
*  I might not be as good as you but I can see the difference between me and you
*  Right. And yeah, this is what you need. This is what you need at the top or you don't necessarily need the manager to be
*  Absolute best I shouldn't say that but like they need to be able to recognize skill. Yeah, they have good intuition
*  Intuition that's laden with wisdom from all the battles of trying to reduce complexity and code bases
*  Um, you know, I took I took a political approach at comma too that I think is pretty interesting
*  I think elon takes the same political approach
*  Uh, you know google had no politics and what ended up happening is the absolute worst kind of politics took over
*  Um comma has an extreme amount of politics and they're all mine and no dissidence is tolerated
*  So it's a dictatorship. Yep. It's an absolute dictatorship. Right elon does the same thing
*  Now the thing about my dictatorship is here are my values
*  Yeah, it's just transparent it's transparent it's a transparent dictatorship, right and you can choose to opt in or you know
*  You get free exit, right? That's the beauty of companies if you don't like the dictatorship you quit
*  So you mentioned rewrite before or refactor before features
*  If you were to refactor the twitter code base, what would that look like and maybe also comment on how difficult is it to refactor?
*  The main thing I would do is first of all identify the pieces and then put tests in between the pieces
*  Right. So there's all these different twitter as a microservice architecture
*  Um
*  All these different microservices and the thing that I was working on there look like, you know
*  George didn't know any javascript. He asked how to fix search blah blah blah blah. Look man like
*  The thing is like I just you know
*  I'm upset that the way that this whole thing was portrayed because it wasn't like it wasn't like taken by people like honestly
*  It wasn't like by it was taken by people who started out with a bad faith assumption
*  Yeah, and I mean I look I can't like and you as a programmer just being transparent out there actually having
*  Like fun and like this is what programming should be about. I love that. Elon gave me this opportunity
*  Yeah, like really it it does and like, you know, he came on my my the the day
*  I quit he came on my twitter spaces afterward and we had a conversation like I just I respect that so much
*  Yeah, and it's also inspiring to just engineers and programmers and just it's cool. It should be fun
*  The people people that were hating on it is like, oh man
*  It was fun it was fun it was stressful
*  But I felt like you know, it was not like a cool like point in history and like I hope I was useful
*  I probably kind of wasn't but like maybe you also were one of the people that kind of made a strong case to refactor
*  Yeah, and that that's a really
*  Interesting thing to raise like maybe that is the right, you know
*  The timing of that is really interesting. If you look at just the development of autopilot, you know going
*  From mobile eye to just like more if you look at the history of semi-autonomous driving in tesla
*  Is is more and more like you could say refactoring or or starting from scratch redeveloping from scratch
*  It's refactoring all the way down and like it and the question is like can you do that sooner?
*  Uh, can you maintain product profitability?
*  And like what's the what's the right time to do it? How do you do it?
*  You know on any one day it's like you don't want to pull off the band-aid like it's
*  Like everything works. It's just like little fix here and there
*  But maybe starting from scratch
*  This is the main philosophy of tiny grad you have never refactored enough
*  Your code can get smaller your code can get simpler your ideas can be more elegant
*  but
*  Would you consider?
*  You know say you were like running twitter development teams engineering teams
*  Programming teams
*  Would you go as far as like different programming language just go that far
*  I mean the first thing that I would do is build tests. The first thing I would do is get a ci
*  To where people can trust to make changes
*  So that before I touched any code I would actually say no one touches any code
*  The first thing we do is we test this code base. This is classic. This is how you approach a legacy code base
*  This is like what any how to approach a legacy code base book will tell you
*  So and then you hope that there's modules that can live on for a while
*  and then you add new ones maybe in a different language or
*  Before we had new ones we replace old ones
*  Yeah, yeah, meaning like replace old ones with something simpler. We we look at this like this thing
*  That's a hundred thousand lines and we're like, well, okay
*  Maybe this did even make sense in 2010, but now we can replace this with an open source thing
*  Right
*  Yeah, and you know we look at this here. Here's another 50 000 lines. Well actually, you know
*  We can replace this with 300 lines of go
*  And you know what? I trust that the go actually replaces this thing because all the tests still pass
*  So step one is testing. Yeah, and then step two is like the programming language is an afterthought, right?
*  You know, let a whole lot of people compete be like, okay
*  Who wants to rewrite a module whatever language you want to write it in just the tests have to pass
*  And if you figure out how to make the test pass but break the site
*  That's we got to go back to step one step one is get tests that you trust in order to make changes in the code base
*  I wonder how hard it is too because i'm with you on on testing and everything
*  I have from tests to like asserts to everything code is just covered in this because
*  It should be very easy to make rapid changes
*  And no, that's not going to break everything and that's the way to do it. But I wonder how difficult is it to
*  Um integrate tests into a code base that doesn't have many of them
*  So i'll tell you what my plan was at twitter. It's actually similar to something we use at comma
*  So a comma we have this thing called process replay
*  And we have a bunch of routes that will be run through so comma is a microservice architecture too with microservices
*  In the driving like we have one for the cameras one for the sensor one for the planner
*  uh one for the model
*  And we have an api which the microservices talk to each other with we use this custom thing called serial which uses zmq
*  twitter uses um
*  Thrift and then it uses this thing called finagle, which is a scala
*  uh
*  Rpc backend, but this doesn't really matter the thrift and finagle
*  layer
*  Was a great place
*  I thought to write tests
*  Right to start building something that looks like process replay
*  So twitter had some stuff that looked kind of like this but it wasn't offline was only online
*  So you could ship like a modified version of it and then you could
*  Redirect some of the traffic to your modified version and diff those two but it was all online
*  There was no like ci in the traditional sense. I mean there was some but like it was not full coverage
*  So you can't run all of twitter offline to test something then this was another problem. You can't run all of twitter
*  right period
*  Twitter one person can't twitter runs in three data centers and that's it. Yeah, there's no other place you can run twitter, which is like
*  George you don't understand. This is modern software development. No, this is bullshit. Like why can't it run on my laptop?
*  What are you doing twitter can run it? Yeah, okay
*  Well, i'm not saying you're gonna download the whole database to your laptop
*  But i'm saying all the middleware and the front end should run on my laptop, right?
*  That sounds really compelling. Yeah
*  But can that be achieved?
*  By a code base that grows over the years
*  I mean the three data centers didn't have to be right because it's they're totally different like designs
*  The problem is more like
*  Like why did the code base have to grow what new functionality has been added to compensate for the the lines of code that are there?
*  one of the ways to explain is that
*  The incentive for software developers to move up in the companies to add code
*  To add and especially large, you know what the incentive for politicians to move up in the political structures to add laws. Yeah, same problem
*  Yeah
*  Yeah, if uh, the flip side is to simplify simplify simplify
*  I mean, you know what? This is something that I do differently from from from elon with with comma about self-driving cars
*  You know, I hear the new version is going to come out and the new version is not going to be better
*  But at first and it's going to require a ton of refactors. I say, okay take as long as you need
*  Like you convinced me this architecture is better. Okay, we have to move to it
*  Even if it's not going to make the product better tomorrow, the top priority is making is getting the architecture, right?
*  so what do you think about sort of a
*  Thing where the product is online?
*  So how I guess would you do a refactor if you ran
*  Engineering on twitter, would you just do a refactor? How long would it take?
*  what would that mean for the running of the
*  of the actual service, you know and
*  I'm not the right person to run twitter
*  I'm just not and that's the problem like like I don't really know
*  I don't really know if that's you know
*  A common thing that I thought a lot while I was there was whenever I thought something that was different to what elon thought
*  I'd have to run something in the back of my head reminding myself
*  That elon
*  Is the richest man in the world?
*  And in general his ideas are better than mine
*  Now there's a few things I think I do understand and know more about
*  but like in general
*  I'm not qualified to run twitter. No, I shouldn't say qualified but like I don't think I'd be that good at it
*  I don't think I'd be good at it. I don't think I'd really be good at running an engineering organization at scale
*  I think I could lead a very good refactor of twitter
*  and it would take like six months to a year and
*  The results to show at the end of it would be feature development in general. It takes 10x less time 10x less man hours
*  That's what I think I could actually do. Um, do I think that it's the right decision for the business?
*  above my pay grade
*  Yeah, but a lot of these kinds of decisions are above everybody's pay grade. I don't want to be a manager
*  I don't want to do that. I just like like if you really forced me to yeah, it would make me maybe
*  Make me upset if I had to make those decisions, I don't want to
*  Yeah, but a refactor is so compelling if this is to become
*  something much bigger than what twitter was
*  Is it feels like
*  A refactor has to be coming at some point george your junior software engineer every junior software engineer wants to come in and refactor the whole code
*  Okay
*  Like that's like your opinion, man
*  Yeah, it doesn't you know, sometimes they're right
*  Well, like whether they're right or not. It's definitely not for that reason, right?
*  It's definitely not a question of engineering prowess
*  It is a question of maybe what the priorities are for the company and I did get more
*  Intelligent like feedback from people I think in good faith like saying that
*  Um from actually from ilan and like, you know from from from ilan sort of like like people were like well
*  You know a stop the world refactor might be great for engineering, but you know, we have business to run
*  and hey
*  Above my pay grade. What do you think about ilan as an engineering leader?
*  Having to experience them in the most chaotic of spaces. I would say
*  That's a good point
*  My respect for him is unchanged. Um, and I did have to think a lot more deeply about some of the decisions he's forced to make
*  About the tensions within those the trade-offs within those decisions
*  About like a whole like
*  Like matrix coming at him. I think that's andrew tate's word for it. Sorry to borrow it
*  Also bigger than engineering just everything. Yeah, like like the war on the woke
*  Yeah, like it just it just man and like
*  He doesn't have to do this, you know
*  He doesn't have to he could go like parag and go chill at the four seasons maui
*  You know, but see one person I respect and one person I don't
*  So his heart is in the right place fighting in this case for this ideal of the freedom of expression
*  I wouldn't define the ideal so simply
*  I think you can define the ideal no more than just saying
*  Elon's idea of a good world
*  freedom of expression is
*  But to you it's still the downsides of that is the monarchy
*  Yeah, I mean monarchy has problems right? But I mean would I trade right now the monarchy or the current oligarchy?
*  Which runs america for the monarchy? Yeah, I would sure
*  Yeah, you know why because power would cost one cent a kilowatt hour
*  Tenth of a cent a kilowatt hour
*  What do you mean right now I pay about 20 cents a kilowatt hour for electricity in san diego
*  That's like the same price you paid in 1980
*  What the hell so you would see a lot of innovation with Elon maybe it have maybe have some hyper loops
*  Yeah, right and i'm willing to make that trade-off right i'm willing to and this is why you know people think that like dictators take back
*  And this is why you know people think that like dictators take power through some like
*  through some untoward mechanism sometimes they do but usually it's because the people want them and
*  The downsides of a dictatorship. I feel like we've gotten to a point now with the oligarchy where
*  Yeah, I would prefer the dictator
*  Uh, what'd you think about scala as a programming language?
*  I liked it more than I thought
*  I did the tutorials like I was very new to it like it would take me six months to be able to write like good
*  Scala
*  I mean, what did you learn about learning a new programming language from that?
*  Um, oh, I love I love doing like new programming. I tutorials and doing them. I did all this for rust
*  uh
*  It keeps some of its upsetting jvm roots, but it is a much nicer
*  In fact, I almost don't know why cotlin took off and not scala. I think scala has some beauty that cotlin lacked
*  Uh
*  Whereas cotlin felt a lot more
*  I mean it was almost like I don't know if it actually was a response to swift
*  But that's kind of what it felt like like cotlin looks more like swift and scala looks more like
*  Well, like a functional programming language more like like, you know camel or haskell
*  Let's actually just explore we touched it a little bit but
*  Just on the art the science and the art of programming. Oh for you personally how much of your programming is done with gpt currently?
*  None
*  None, I don't use it at all
*  Because you prioritize simplicity so much
*  Yeah, I find that a lot of it is noise. I do use vs code
*  um
*  And I do like some amount of autocomplete. I do like like a very um
*  A very like feels like rules-based autocomplete like an autocomplete. It's going to complete the variable name for me
*  So I'm just type it I can just press tab
*  All right, that's nice, but I don't want an autocomplete
*  you know what I hate when autocompletes when I type the word for and it like puts like
*  Two two parentheses and two semicolons and two braces i'm like
*  Well, let me with uh vs code and gpt with codec you can um
*  You can kind of brainstorm I I find
*  I'm like probably the same as you but I like that it generates code
*  and you basically disagree with it and write something simpler, but to me that somehow is like
*  Inspiring it makes me feel good. It also gamifies the simplification process because i'm like, oh, yeah
*  You dumb ai system you think this is the way to do it. I have a simpler thing here
*  It just constantly reminds me of like like bad stuff
*  I mean, I tried the same thing with rap, right?
*  I tried the same thing with rap and actually I think i'm a much better programmer than rapper
*  But like I even tried I was like, okay
*  Can we get some inspiration from these things for some rap lyrics?
*  And I just found that it would go back to the most like cringey tropes and dumb rhyme schemes and i'm like
*  Yeah, this is what the code looks like too
*  I I think you and I probably have different thresholds for cringe code
*  You probably hate cringe code
*  So it's for you
*  I mean, uh
*  Boilerplate is a as a part of code
*  Like some of it
*  Yeah, and some of it is just like faster lookup
*  Because I don't know about you, but I don't remember everything like I don't i'm offloading so much of my memory
*  about like
*  um
*  Yeah, different functions library functions all that kind of stuff like this gpt just is very fast at standard stuff and like
*  Uh standard library stuff basic stuff that everybody uses
*  Yeah, I think that
*  I don't know. I mean there's just a little of this in python
*  Maybe if I was coding more in other languages, I would consider it more
*  But I feel like python already does such a good job of removing any boilerplate
*  That's true. It's the closest thing you can get to pseudocode, right? Yeah, that's true
*  That's true. I'm like, yeah, sure if I like yeah great gpt. Thanks for reminding me to free my variables
*  Unfortunately, you didn't really recognize the scope correctly and you can't free that one
*  But like you put the freeze there and like I get it
*  Fiber
*  Whenever i've used fiber for certain things like design or whatever
*  Yeah, it's always you come back. I think that's probably closer my experience with fiber
*  It's closer to your experience with programming with gpt is like
*  You're just frustrated and feel worse about the whole process of design and art and whatever. Whatever I use fiber for
*  Still I just feel like later versions gpt I i'm using
*  um
*  GPT as much as possible
*  To just learn the dynamics of it like
*  These early versions because it feels like in the future you'll be using it more and more
*  And so like I don't want to be like for the same reason I gave away all my books and switched to kindle
*  because like all right
*  How long are we gonna have paper books like 30 years from now?
*  Like I want to learn to be reading on kindle even though I don't enjoy it as much
*  And you learn to enjoy it more in the same way I switched from
*  Um
*  Let me just pause switch from emacs to vs code. Yeah, I switched from vim to vs code
*  I think I similar but yeah, it's tough and that vim to vs code is even tougher because emacs is like
*  Old like more outdated feels like it the community is more outdated
*  Vim is like pretty vibrant still so I never used any of the plugins. I still don't use that
*  That's what I looked at myself in the mirror. I'm like, yeah, you wrote some stuff in lisp. Yeah
*  But I never used any of the plugins in them either I had the most vanilla vim
*  I have a syntax highlighter. I didn't have autocomplete like
*  these things
*  I feel like help you so marginally
*  that like
*  And now okay now vs codes autocomplete has gotten good enough that like okay
*  I don't have to set it up. I can just go into any code base and autocompletes right 90% of the time
*  Okay, cool. I'll take it
*  All right
*  So I don't think I'm gonna have a problem at all adapting to the tools once they're good
*  but like the real thing that I want
*  is not
*  Something that like tab completes my code and gives me ideas. The real thing that I want is a very intelligent pair programmer that
*  Uh comes up with a little pop-up saying hey, uh, you wrote a bug on line 14 and here's what it is
*  Yeah now I like that. You know, what does a good job of this my pi?
*  I love my mind my pie this fancy type checker for python. Yeah. Um, and actually I tried like microsoft released one too and it was like
*  60 false positives my pie is like 5 false positives
*  95% of the time it recognizes I didn't really think about that typing interaction correctly. Thank you my pie. So you like uh type hinting you liked
*  You like pushing the language towards there was being a typed language. Oh, yeah, absolutely. I think I think optional typing is is great
*  I mean look I think that like it's like a meat in the middle, right?
*  Like python has these optional type hinting and like c++ has auto
*  C++ takes allows you to take a step back. Well c++ would have you brutally type out std string iterator, right?
*  Now I can type auto which is nice and then python used to just have
*  a what type is a
*  It's an a
*  Um a colon str. Oh, okay. It's a string cool
*  Yeah, I wish there were I wish there was a way like a simple way in python to uh,
*  Like turn on a mode which would enforce the types
*  Yeah, like give a warning when there's no type something like this
*  Well, no to give a warning where like my pile is a static type checker
*  But i'm asking just for a runtime type checker like there's like ways to like hack this in but I wish it was just
*  Like a flag like python 3-t
*  Oh, I see. I see enforce the types around time. Yeah, I feel like that makes you a better programmer that that's a kind of test
*  Right that the the type can the type remains the same
*  Well that I know that I didn't like mess any types up
*  But again, like my pie is getting really good and I love it
*  Um, and I can't wait for some of these tools to become AI powered
*  Like I want ai's reading my code and giving me feedback. I don't want ai's
*  writing
*  Half-assed autocomplete stuff for me
*  I wonder if you can now take gpt and give it a code that you wrote for function and say
*  How can I make this simpler and have it accomplish the same thing?
*  I think you'll get some good ideas on some code you maybe not the code you write
*  um
*  For tiny grad type of code because that requires so much design thinking but like other kinds of code
*  I don't know. I downloaded the plug-in maybe like two months ago. I tried it again and found the same look
*  I don't doubt that these models are going to first become useful to me then be as good as me and then surpass me
*  but
*  from what i've seen today, it's like
*  like like
*  someone, you know
*  Occasionally taking over my keyboard that I hired from fiverr. Yeah
*  I'd rather have ideas about how to debug the coder basically a better debugger is really interesting
*  I mean, but it's not a better debugger. I guess I would love a better debugger
*  Yeah, it's not yet. Yeah, but it feels like it's not too far
*  Yeah
*  One of my co-workers says he uses them for print statements
*  Like every time he has to like just like when he needs the only thing he can really write is like, okay
*  I just want to write the thing to like print the state out right now
*  oh that
*  Definitely is much faster as print statements. Yeah
*  I see myself using that a lot just like because it it figures out the rest of the functions just like okay print everything
*  Yeah print everything right and then yeah, like if you want a pretty printer maybe i'm like, yeah
*  You know what? I think like I think in two years i'm going to start using these plugins
*  Yeah a little bit and then in five years i'm going to be heavily relying on some ai augmented flow
*  And then in 10 years, do you think you'll ever get to 100?
*  Where the like what's the role of the human?
*  That it converges to
*  as a programmer
*  So you think it's all generated our niche becomes. Oh, I think it's over for humans in general
*  It's not just programming. It's everything
*  So niche become well our niche becomes smaller smaller smaller. In fact, i'll tell you what the last niche of humanity is going to be
*  Yeah
*  Um, this is a great book and it's if I recommended metamorphosis prime intellect last time
*  There is a sequel called a casino odyssey in cyberspace
*  and um
*  I don't want to give away the ending of this but it tells you what the last remaining human currency is
*  And I agree with that
*  We'll, uh leave that as the cliffhanger, uh
*  So no more programmers left, huh
*  That's where we're going unless you want handmade code. Maybe they'll sell it on etsy. This is handwritten code
*  Doesn't have that machine polished to it it has those slight imperfections that would only be written by a person
*  I wonder how far away we are from that
*  I mean, there's uh some aspect to you know on instagram your title is listed as prompt engineer, right?
*  thank you for noticing
*  it's uh, I don't know if it's ironic or uh, non
*  uh
*  Or sarcastic or not. Uh, what do you think of prompt engineering as a scientific?
*  and
*  Engineering discipline or maybe and maybe art form, you know what?
*  I started comma six years ago and I started the tiny corp a month ago
*  I'm like, okay, I'm gonna get an office in san diego. I'm gonna bring people here
*  I don't think so. I think i'm actually gonna do remote
*  Right george. You're gonna do remote you hate remote. Yeah, but i'm not gonna do job interviews
*  The only way you're gonna get a job is if you contribute to the github
*  Right and then like it like like interacting through github
*  And then you're gonna do remote. You're gonna do remote. You're gonna do remote. You're gonna do remote
*  Right and then like it like like interacting through github
*  like like github being the real like
*  Project management software for your company and the thing pretty much just is a github repo
*  Is like showing me kind of what the future of okay
*  So a lot of times i'll go on a discord or kind of grab discord and i'll throw out some random like hey
*  You know, can you change instead of having log and exp as llops change it to log two and exp too
*  It's pretty small change you can just use like change a base formula
*  um
*  That's the kind of task that I can see an ai being able to do in a few years
*  Like in a few years I could see myself describing that and then within 30 seconds a pull request is up that does it
*  And it passes my ci and I merge it
*  right, so I really started thinking about like well, what is the future of
*  Jobs, how many ai's can I employ at my company as soon as we get the first tiny box up?
*  I'm gonna stand up a 65b llama in the discord and it's like, yeah, here's the tiny box. He's just like he's chilling with us
*  basically
*  I mean like you said with niches like
*  most human jobs
*  Will eventually be replaced with prompt engineering. Well prompt engineering kind of is this like
*  As you like move up the stack, right?
*  Like okay, there used to be humans actually doing um arithmetic by hand
*  There used to be like big farms of people doing doing doing pluses and stuff, right?
*  And then you have like spreadsheets, right?
*  And then okay the spreadsheet can do the plus for me and then you have like macros
*  Right, and then you have like things that basically just are spreadsheets under the hood, right? Like like accounting software
*  um
*  As we move further up the abstraction. Well, what's at the top of the abstraction stack? Well prompt engineer
*  Yeah, right
*  What is what is the last thing if you think about like humans wanting to keep control
*  Well, what am I really in the company but a prompt engineer, right?
*  Isn't there a certain point where the ai will be better at writing prompts?
*  Yeah, but you see the problem with the ai writing prompts a definition that I always liked of ai was ai is the do what I mean machine
*  Right ai is not the like the computer is so pedantic. It does what you say. So
*  But you want to do what I mean machine
*  Yeah, right. You want the machine where you say, you know
*  Get my grandmother out of the burning house
*  It like reasonably takes your grandmother and puts her on the ground not lifts her a thousand feet above the burning house and lets her fall
*  All right, but you know judkowski examples
*  But
*  Uh, it's not going to find the meaning. I mean to do what I mean, it has to figure stuff out. Sure and
*  The thing you'll maybe ask it to do is
*  Run government for me. Oh and do what I mean very much comes down to how aligned is that ai with you?
*  of course
*  When you talk to an ai that's made by a big company in the cloud the ai
*  Fundamentally is aligned to them not to you. Yeah, and that's why you have to buy a tiny box
*  So you make sure the ai stays aligned to you every time that they start to pass, you know, ai regulation or gpu regulation
*  I'm gonna see sales of tiny boxes spike. It's gonna be like guns
*  Right every time they talk about gun regulation boom
*  Gun sales so in the space of ai you're an anarchist anarchism
*  Espouser believer i'm an informational anarchist. Yes. I'm an informational anarchist and a physical status
*  I do not think anarchy in the physical world is very good because I exist in the physical world
*  But I think we can construct this virtual world where anarchy it can't hurt you right?
*  I love that tyler the creator
*  Uh tweet, uh, yo cyber bullying isn't real man. Have you tried turning off the screen close your eyes like yeah
*  But how do you
*  Prevent the ai from basically
*  replacing all
*  Human prompt engineers where there's it's like a self like where nobody's the prompt engineer anymore
*  So autonomy greater and greater autonomy until it's full autonomy. Yeah
*  And that's just where it's headed because one person is going to say run everything for me you see
*  I look at potential futures and as long as the ai's go on to create a vibrant
*  civilization with diversity and complexity across the universe
*  More power to them. I'll die
*  If the ai's go on to actually like turn the world into paper clips and then they die out themselves
*  Well, that's horrific and we don't want that to happen
*  So this is what I mean about like robustness. I trust robust machines
*  The current ai's are so not robust like this comes back to the idea that we've never made a machine that can self-replicate
*  Right, but when we have if the machines are truly robust and there is one prompt engineer left in the world
*  Hope you're doing good, man. Hope you believe in god like, you know
*  you know go by god and
*  Go help go forth and and and conquer the universe
*  Well, you mentioned uh, because I talked to mark about faith and god and you said you were impressed by that
*  Um, what's your own belief in god and how does that affect your work?
*  you know
*  I never really considered when I was younger. I guess my parents were atheist
*  So I was raised kind of atheist. I never really considered how absolutely like silly atheism is
*  because like
*  I create worlds
*  Every like game creator like how are you an atheist bro?
*  You create worlds with the pidevan. No one created our world man. That's different. Haven't you heard about like the big bang and stuff?
*  Yeah, I mean, what's the skyrim myth origin story in skyrim?
*  I'm sure there's like some part of it in skyrim
*  But it's not like if you ask the creators like the the big bang is in universe, right?
*  I'm sure they have some big bang notion in skyrim, right?
*  But that obviously is not at all how skyrim was actually created. It was created by a bunch of programmers in a room, right?
*  so like
*  You know, it just just it struck me one day how just silly atheism is like, of course we were created by god
*  It's the most obvious thing
*  Yeah, that's uh
*  That's such a nice way to put it like we're we're such powerful creators ourselves
*  It uh, it's silly not to concede that there's creators even more powerful than us
*  Yeah, and then like I also just like I like that notion that notion gives me a lot of
*  I mean, I guess you can talk about what it gives a lot of religious people is kind of like it just gives me comfort
*  It's like you know what if we mess it all up and we die out. Yeah
*  Yeah, and the same the same way that a video game kind of has comfort in it god will try again
*  Or there's balance like somebody figured out a balanced
*  view of it like how to like so it all makes sense in the end
*  like uh
*  A video game is usually not going to have crazy crazy stuff. You know people will come up with uh,
*  like, uh
*  Well, yeah, but like man who created god?
*  Like that's god's problem
*  No, like i'm not gonna think this is this is what you're asking me. What if god i'm just living god
*  I'm just this npc living in this game. I mean to be fair like if god didn't believe in god
*  He'd be as you know, silly as the atheists here
*  Uh, what do you think is the greatest?
*  Computer game of all time. Do you do you have any time to play games anymore?
*  Have you played diablo 4?
*  I have not played diablo 4. I will be doing that shortly. I have to all right
*  There's just so much history with one two and three. You know what i'm gonna say world of warcraft
*  And
*  It's not that the game is so it's such a great game. It's not
*  It's that I remember in 2005 when it came out how it opened my mind to
*  ideas
*  it opened my mind to like
*  Like like like this this whole world we've created right and there's almost been nothing like it since
*  Like you can look at mmos today and I think they all have lower user bases than world of warcraft like evon line's kind of cool
*  but
*  but to think that like
*  like everyone know you know people are always like to look at the apple headset like
*  What do people want in this vr? Everyone knows what they want. I want ready player one
*  and like that
*  So i'm gonna say world of warcraft and i'm hoping that like games can get out of this whole
*  mobile gaming dopamine pump thing and like create worlds create worlds
*  Yeah, that that and worlds that captivate a very large fraction of the human population
*  Yeah, and I think it'll come back. I believe but mmo like really
*  Really pull you in games do a good job. I mean, okay other like two other games that I think are, you know
*  Very noteworthy from your skyrim and gta 5
*  Skyrim, yeah, that's probably number one for me dta. Yeah, what is it about gta?
*  GTA is really
*  I I guess gta is real life. I know there's prostitutes and guns and stuff
*  Yes, I know but it's uh, it's how imagine your life to be actually I wish it was that cool. Yeah
*  Yeah
*  Yeah, I guess that's you know, because they're sims right which is also a game I like
*  But it's a gamified version of life, but it also is I would love a combination of sims and gta
*  So more freedom more violence more rawness
*  But with also like ability to have a career and family and this kind of stuff
*  What i'm really excited about in games is like once we start getting intelligent ais to interact with oh, yeah
*  Right like the npc's and games have never been
*  But conversationally
*  Oh in every way
*  E in like yeah in like every way like when you're actually building a world and a world
*  imbued with intelligence
*  Oh, yeah, right and it's just hard like there's just like like, you know running world of warcraft
*  Like you're limited by you're running on a pennium 4, you know, how much intelligence can run? How many flops did you have?
*  Right, but now when i'm running a game on a hundred pay to flop machine. Well, that's five people
*  I'm trying to make this a thing 20 pay to flops of compute is one person of compute. I'm trying to make that a unit
*  20
*  Pedal flops is one person one person one person flop. It's like a horsepower
*  Like what's a horsepower? That's how powerful the horse is. What's a what's a person of compute? Well, you know flop I got it
*  That's interesting
*  Uh vr also adds a I mean in terms of creating worlds, you know what?
*  border quest 2
*  I put it on and I can't believe the first thing they show me is a bunch of scrolling clouds and a facebook login screen
*  Yeah
*  You had the ability to bring me into a world
*  And what did you give me a pop-up right? Like well, and this is why you're not cool mark zuckerberg
*  But you could be cool. Just make sure on the quest 3 you don't put me into clouds and a facebook login screen
*  Bring me to a world. I just tried quest 3 it was awesome. But hear that guys. I agree with that
*  So
*  You know what because I uh, I mean the beginning um
*  What is it? Todd? Howard said this about?
*  Uh design of the beginning of the games he creates is like the beginning is so so so important
*  Um, I recently played zelda for the first time zelda breath of the wild the previous one and like it's very quickly
*  You come out of this like uh within like 10 seconds
*  You come out of like a cave type place and it's like this world opens up. It's like
*  And it like it pulls you in you forget whatever troubles I was having whatever like
*  I got to play that from the beginning. I played it for like an hour at a friend's house
*  Ah, no the beginning they got it. They did really well the expansiveness of that space
*  um
*  The the peacefulness of that play they got this the music I mean so much of that
*  Is creating that world and pulling you right in i'm gonna go i'm gonna go buy a switch like i'm gonna go today and buy a switch
*  You sure well the new one came. I haven't played that yet, but uh, diablo 4 is something. I mean there's sentimentality also, but
*  something about vr
*  Really is incredible, but the
*  The new quest 3 is mixed reality and I got a chance to try that so it's uh augmented reality and for video games
*  It's done really really well. Is it passed through cameras cameras cameras? Okay. Yeah
*  The apple one is that one passed through our cameras? I don't know. Yeah, I don't know how real it is
*  I don't know anything, you know coming out
*  January
*  Is it january or is it some point some point? All right, maybe not january. Maybe that's my optimism, but apple
*  I will buy it. I don't care if it's expensive and does nothing. I will buy it
*  I will support this future endeavor. You're the meme. Oh, yes. I support competition
*  it seemed like quest was like the only people doing it and this is great that they're like
*  You know what and this is another place we'll give some more respect to marie zuckerberg
*  The two companies that have endured through technology or apple and microsoft
*  All right, and what do they make computers and business services?
*  Right all the memes social ads they all come and go
*  But you want to endure build hardware
*  Yeah, and then you know it does does a really interesting job
*  Maybe I maybe i'm new but this but uh, it's a 500 headset
*  uh quest 3 and
*  Just having creatures running around the space like our space right here to me
*  Okay, this is very like boomer statement
*  But it added windows
*  to the place
*  The I heard about the aquarium. Yeah aquarium, but in this case, it was a zombie game. Whatever. It doesn't matter
*  but just like
*  It it modifies the space in a way where I can't it really feels like a window and you can look out
*  It's pretty cool. Like I was just it's like a zombie game. They're running at me whatever
*  But what I was enjoying is the fact that there's like a window and and they're stepping on objects in the space
*  That was a different kind of escape also because you can see the other humans so it's integrated with the other humans. It's really
*  And that's why it's really important than ever that the ai is running on those systems are aligned with you
*  Oh, yeah, they're gonna augment your entire world. Oh, yeah
*  and that those ai's have uh
*  I mean you think about all the dark stuff
*  like
*  Like sexual stuff like if those ai's threaten me
*  That could be haunting
*  That like if they like threaten me in a non-video game way
*  It's like oh, yeah, yeah, yeah, yeah
*  Like they'll know personal information about me and it's like and then you lose track of what's real what's not like
*  What if stuff is like hacked? There's two directions the ai girlfriend company can take right?
*  There's like the highbrow something like her
*  Maybe something you kind of talk to and this is and then there's the lowbrow version of it where I want to set up a brothel
*  In time square. Yeah
*  Yeah, it's not cheating if it's a robot. It's a vr experience if is there an in-between
*  No
*  I don't want to do that one with that one. Have you decided yet?
*  No, figure it out. We'll see we'll see what the technology goes
*  I would love to hear your opinions for george's
*  uh third company what to do, uh, the brothel in time square or the uh,
*  the her experience
*  Uh, what do you think company number four will be you think there'll be a company number four
*  There's a lot to do in company number two. I'm just like i'm talking about company number three now
*  Didn't none of that tech exists yet
*  There's a lot to do in company number two company number two
*  Is going to be the great struggle of the next six years and of the next six years
*  How centralized is compute going to be the less centralized computer is going to be the better of a chance we all have
*  So you're bearing the you're like a flag bearer for open source distributed
*  decentralization of uh compute we have to we have to or they will just completely dominate us
*  I showed a picture on stream of a man
*  In a chicken farm. Have you seen one of those like factory farm chicken farms? Why does he dominate all the chickens?
*  Why does he smarter he's smarter, right?
*  Some people some people on twitch were like he's bigger than the chickens. Yeah, and now here's a man in a cow farm
*  right
*  So it has nothing to do with their size and everything to do with their intelligence and if one
*  Central organization has all the intelligence you'll be the chickens and they'll be the chicken man
*  But if we all have the intelligence, we're all the chickens
*  We're not all the man we're all the chickens
*  And there's no chicken man, there's no chicken man, we're just chickens in miami
*  He was having a good life man. I'm sure he was
*  I'm sure he was what have you learned from launching a running comma ai and tiny corp? So this
*  Starting a company from an idea and scaling it and by the way, i'm all in on tiny box. So i'm i'm i'm your
*  I'll I guess it's pre-order only now. I want to make sure it's good
*  I want to make sure that like the thing that I deliver is like
*  Not going to be like a quest to which you buy and use twice
*  I mean it's better than a quest which you bought and used less than once statistically
*  Well, if there's a beta program for uh tiny box i'm into sounds good
*  So I won't be the whiny. Uh, yeah, i'll be the tech tech savvy
*  User of the tiny box just to be in what have I in the early days?
*  What have you learned from building these companies?
*  The longest time at comma I asked why
*  Why you know, why did I start a company? Why did I do this?
*  But you know what else was like i'm gonna do
*  So you like
*  You like bringing ideas to life
*  With comma
*  It really started as an ego battle with elon
*  I wanted to beat him. I like I saw a worthy adversary, you know
*  Here's a worthy adversary who I can beat at self-driving cars
*  And like I think we've kept pace and I think he's kept ahead. I think that's what's ended up happening there
*  Um, but I do think comma is I mean comes profitable
*  like
*  And like when this drive gpt stuff starts working, that's it
*  There's no more like bugs in the loss function like right now. We're using like a hand-coded simulator
*  There's no more bugs. This is going to be it. This is the run-up to driving
*  Like this is the run-up to driving. I hear a lot of really, um a lot of props
*  For open pilot for comma it's it's so it's it's better than fsd and autopilot in certain ways
*  It has a lot more to do with which feel you like we lowered the price on the hardware to 1499
*  You know how hard it is to ship reliable consumer electronics that go on your windshield. We're doing more than like
*  Most cell phone companies, how'd you pull that off? By the way shipping a product that goes in a car. I know
*  I have a I have a I have an smt line. It's all I make all the boards in house in san diego
*  Quality control I care immensely about it. Actually are you're basically a mom and pop
*  Shop with great testing our head of open pilot is great at like, you know
*  Okay, I want all the comet theories to be identical. Yeah
*  And yeah, I mean, you know, it's look it's 1499 it
*  30 day money back guarantee it will
*  It will blow your mind at what it can do is it hard to scale
*  You know what there's kind of downsides to scaling it people are always like why don't you advertise?
*  Our mission is to solve self-driving cars while delivering shippable intermediaries. Our mission has nothing to do with selling a million boxes
*  It's tawdry
*  Do you think it's possible that uh comma gets sold?
*  Only if I felt someone could accelerate that mission
*  And wanted to keep it open source
*  And like not just wanted to I don't believe what anyone says. I believe incentives
*  if a company wanted to buy comma with their incentives or to keep it open source, but
*  Comma doesn't stop at the cars. The cars are just the beginning
*  The device is a human head. The device has two eyes two ears. It breathes air has a mouth
*  So you think this goes to embodied robotics? We have we sell common bodies too
*  You know, they're very they're very rudimentary
*  But one of the problems that we're running into is that the comma three has about as much intelligence as a b
*  If you want a human's worth of intelligence
*  You're going to need a tiny rack not even a tiny box. You're going to need like a tiny rack maybe even more
*  How does that?
*  How do you put legs on that? You don't and there's no way you can you you connect to it wirelessly?
*  So you put your tiny box or your tiny rack in your house
*  And then you get your comma body and your comma body runs the models on that
*  It's it's close. All right, it's not you don't have to go to some cloud which is, you know, 30 milliseconds away
*  You go to a thing which is 0.1 milliseconds away. So the ai girlfriend
*  Will have like a central hub in the home
*  I mean eventually if you fast forward 20 30 years the mobile chips will get good enough to run these ai's
*  But fundamentally it's not even a question of putting legs on a tiny box because how are you getting 1.5 kilowatts of power on that thing?
*  Right. So you you need they're very synergistic businesses. I also want to build all of commas training computers
*  I comma builds training computers right now. We use
*  Commodity parts. I think I can do it cheaper
*  So we're gonna build tiny corp is gonna not just sell tiny boxes tiny boxes the consumer version
*  But i'll build training data centers, too. Have you talked to
*  Andre kaput here? Have you talked to elan about tiny core? He went to work at open ai
*  What do you love about andre kaput?
*  to me, he's one of the
*  Truly special humans we got oh man, like you know, his streams are just a level of quality so far beyond mine
*  Like I can't help myself. Like it's just it's just you know, yeah, he's good. He
*  Wants to teach you. Yeah, I want to show you that i'm smarter than you
*  Yeah, he has no
*  That's I mean, uh, thank you for the sort of
*  The raw authentic honesty
*  I mean a lot of us have that
*  I think andre is as legit as it gets in that he just wants to teach you and it's a there's a curiosity that just
*  Drives him and just like at his at the stage where he is in life
*  to be
*  Still like one of the best tinkerers in the world. Yeah, it's crazy like to uh,
*  What is it micro grad micro grad was yeah inspiration for tiny grad
*  Ain't that the whole I mean his his his cs 231 n was this was this was the inspiration
*  This is what I just took and ran with and ended up writing this so, you know
*  But I mean to me that don't go work for darth vader, man
*  I mean to flip the flip side to me is that the fact that he's going there
*  Is a good sign
*  for open ai
*  I think you know
*  I I like ilias discover a lot. I like those those guys are really good at what they do
*  I know they are and that's kind of what's even like more and you know what?
*  It's not that open ai doesn't open source the weights of gpt4
*  It's that they go in front of congress
*  And that is what upsets me, you know, we had two effective altruists sams go in front of congress one's in jail
*  I think you're drawing parallels on the
*  I'm in jail. You give me a look
*  Give me a look. No, I think I think effective altruism is a terribly evil ideology. Oh, yeah, that's interesting
*  Why do you think that is? Why do you think?
*  There's something about a thing that sounds pretty good
*  That kind of gets us into trouble because you get sam bangman freed like sam bangman freed is the embodiment of effective altruism
*  Utilitarianism is an abhorrent ideology
*  Like like well, yeah, we're gonna kill those three people to save a thousand of course, yeah, right there's no there's no underlying like there's just
*  Yeah
*  Yeah, but to me that's a bit surprising
*  but it's also
*  In retrospect not that surprising but I haven't heard really clear kind of
*  Um, like rigorous analysis why effective altruism is flawed
*  Oh, well, I think charity is bad, right? So what is charity but investment that you don't expect to have a return on right?
*  Yeah, but you can also think of charity as like um
*  Is you would like to see uh, so allocate resources in an optimal way
*  To uh to make a better world
*  And probably almost always that involves starting a company
*  Yeah, right because more efficient. Yeah, if you just take the money and you spend it on malaria nets, you know
*  Okay, great. You've made 100 malaria nets, but if you teach yeah, I mean how to fish right? Yeah
*  No, but the problem is uh teaching them how to fish it might be harder starting a company might be harder than
*  Allocating money that you already have I like the flip side of effective altruism effective accelerationism
*  I think accelerationism is the only thing that's ever lifted people out of poverty
*  Um, the fact that food is cheap not we're giving food away because we are kind-hearted people
*  No food is cheap
*  And that's the world you want to live in
*  Ubi what a scary idea
*  What a scary idea all your power now
*  Your money is power. Your only source of power is granted to you by the goodwill of the government
*  What a scary idea. So you even think long term even uh,
*  I'd rather die than need ubi to survive and I mean it
*  Is that a good idea?
*  What if survival is basically guaranteed what if our life becomes so good
*  You can make survival guaranteed without ubi. What you have to do is make housing and food dirt cheap
*  Right, like and that's the good world and actually let's go into what we should really be making dirt cheap, which is energy
*  right that energy that
*  You know that that's if there's one
*  I'm pretty centrist politically if there's one political position I cannot stand it's deceleration
*  It's people who believe we should use less energy. Yeah, not people who believe global warming is a problem
*  I agree with you not people who believe that you know, uh, the saving the environment is good. I agree with you
*  But people who think we should use less energy that energy usage is a moral bad. No
*  No, you are asking you are you are diminishing humanity
*  Yeah, energy is flourishing of creative flourishing of the the human species
*  How do we make more of it? How do we make it clean? And how do we make just just just how do how do I pay?
*  You know 20 cents for a megawatt hour instead of a kilowatt hour part of me wishes that um,
*  Elon went into nuclear fusion versus twitter
*  Pardon me
*  Or somebody somebody like elon, you know, we need to
*  I wish there were more more elons in the world and yeah
*  I think elon sees it as like, uh, this is a political battle that needed to be fought
*  And again like you know, I always ask the question of whenever I disagree with him
*  I remind myself that he's a billionaire and i'm not so uh, you know
*  Maybe he's got something figured out that I don't or maybe he doesn't to have some
*  Humility, but at the same time me as a person who happens to know him
*  I find myself in that same position and
*  Sometimes even billionaires need friends who disagree and help them grow
*  And that's a difficult that's a difficult reality and it must be so hard. It must be so hard to meet people
*  Once you get to that point where?
*  Fame power money everybody's sucking up to you. See I love not having shit like I don't have shit man
*  You know like like trust me. There's nothing I can give you. There's nothing worth taking for me, you know
*  Yeah, it takes a really special human being when you have power when you have fame when you have money
*  To still think from first principles
*  Not like all the adoration you get towards you all the admiration all the people saying yes
*  Yes, yes, and all the hate too and the hate I'm gonna worse
*  So the hate makes you want to go to the yes people
*  Because the the hate exhausts you and the kind of hate that elon's gotten from the left is pretty intense
*  And so that of course drives him, right?
*  and
*  loses balance and
*  It keeps this absolutely fake like
*  psyop
*  Political divide alive so that the one percent can keep power. Like yeah
*  I wish would be less divided because it is giving power. It gives power to the ultra powerful
*  The rich get richer
*  You have love in your life has love made you a better or a worse programmer?
*  Do you keep productivity metrics no, no
*  No, i'm not not that i'm not that methodical
*  um, I think that there comes to a point where
*  If it's no longer visceral, I just can't enjoy it
*  Like I still viscerally love programming
*  The minute I started like so that's one of the big loves of your life is programming
*  I mean just my computer in general. I mean, you know, I tell my girlfriend my first love is my computer, of course
*  Right, like, you know, I sleep with my computer. It's there for a lot of my sexual experiences like come on
*  So is everyone's right?
*  Uh, like, you know, you gotta be real about that and like not just like the id for programming
*  It's just the entirety of the computational machine the fact that yeah, I mean it's you know, I wish it was uh,
*  Someday they'll be smarter and so maybe i'm weird for this but I don't discriminate man
*  I'm not going to discriminate bio stack life and silicon stack life like so the moment the computer
*  Starts to say like I miss you. I started to have some of the basics of uh,
*  human intimacy
*  It's over for you. The moment vs code says
*  Hey george, no, you see no no, but vs code is
*  No, they're just doing that microsoft's doing that to try to get me hooked on it. I'll see through it
*  I'll see through it's gold digger man. It's gold digger. Look at me an open source
*  Well, this just gets more interesting right if it's if it's open source and yeah
*  Though microsoft's done a pretty good job on that. Oh, absolutely
*  No, no, no, look, I think microsoft again
*  I wouldn't count on it to be true forever
*  But I think right now microsoft is doing the best work in the programming world like between yeah
*  github github actions vs code the improvements to python, you know, where's microsoft like
*  This is who who would have thought microsoft?
*  And mark zuckerberg are spearheading the open source movement
*  Right, right
*  How how things change oh it's beautiful
*  By the way, that's who i'd bet on to replace google by the way who microsoft
*  Microsoft i think satya nadela said straight up i'm coming for it
*  Interesting. So your bet
*  Who wins?
*  Agi. Oh, I don't know about agi. I think we're a long way away from that
*  But I would not be surprised if in the next five years bing overtakes google as a search engine
*  Interesting wouldn't surprise
*  Interesting
*  I hope some startup does
*  It might be some startup too. I would I would equally bet on some startup
*  Yeah, i'm like 50 50. Yeah, but maybe that's naive
*  I believe in the power of these language models satya is alive microsoft's alive
*  Yeah
*  It's great. It's great. I like all the innovation in these companies. They're not being stale
*  Uh and to the degree they're being stale they're losing
*  So there's a lehugen center to do a lot of exciting work and open source work, which is this is incredible only way to win
*  You're older
*  You're wiser. What's the meaning of life george harts?
*  to win
*  It's still to win. Of course
*  Always of course what's winning look like for you?
*  I don't know. I haven't figured out what the game is yet
*  But when I do I want to so it's bigger than solving self-driving. It's bigger than
*  uh
*  Democ democritizing decentralizing compute
*  I think the game is to stand out eye with god
*  I wonder what that means for you like at the end of your life what that would look like
*  I mean, this is what like I don't know. This is some this is some
*  There's probably some ego trip of mine, you know, like if you want to stand eye to eye with god
*  You're just blasphemous man. Okay. I don't know. I don't know. I don't know if it would upset god
*  I think he like wants that. I mean, I certainly want that for my creations
*  I want my creations to stand eye to eye with me
*  So why wouldn't god want me to stand eye to eye with him?
*  That's the best I can do golden rule
*  I'm just imagining the creator of a video game
*  Having to uh
*  Look and stand eye to eye
*  With one of the characters
*  I only watched season one of westworld. Yeah, we got to find the maze and solve it like
*  Yeah, I wonder what that looks like it feels like a really special time in human history
*  Where that's actually possible like there's something about ai that's like we're playing with something weird here
*  Something really weird. I wrote a blog post. Uh,
*  I reread genesis and just looked like they give you some clues at the end of genesis for finding the garden of eden
*  And i'm interested
*  i'm interested
*  Well, I hope you find just that george you're one of my favorite people
*  Thank you for doing everything you're doing and in this case for fighting for open source or for decentralization of ai
*  It's uh, it's a fight worth fighting fight worth winning hashtag
*  Um, I love you brother. These conversations are always great. I hope to talk to you many more times. Good luck with tiny corp
*  Thank you. Great to be here
*  Thanks for listening to this conversation with george hotz to support this podcast
*  Please check out our sponsors in the description and now let me leave you with some words from albert einstein
*  Everything should be made as simple as possible, but not simpler
*  Thank you for listening and hope to see you next time
