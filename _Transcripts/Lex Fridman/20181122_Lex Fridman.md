---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 5204s
Video Keywords: []
Video Views: 287124
Video Rating: None
---

# Guido van Rossum: Python | Lex Fridman Podcast #6
**Lex Fridman:** [November 22, 2018](https://www.youtube.com/watch?v=ghwaIiE3Nd8)
*  The following is a conversation with Gwidovan Rasam, creator of Python,
*  one of the most popular programming languages in the world, used in almost any application
*  that involves computers, from web backend development to psychology, neuroscience,
*  computer vision, robotics, deep learning, natural language processing, and almost any subfield of AI.
*  This conversation is part of MIT course on artificial general intelligence
*  and the artificial intelligence podcast. If you enjoy it, subscribe on YouTube, iTunes,
*  or your podcast provider of choice, or simply connect with me on Twitter at Lex Friedman,
*  spelled F-R-I-D. And now here's my conversation with Gwidovan Rasam.
*  You were born in the Netherlands in 1956. Your parents and the world around you was
*  deeply impacted by World War II, as was my family from the Soviet Union. So with that context,
*  what is your view of human nature? Are some humans inherently good and some inherently evil,
*  or do we all have both good and evil within us?
*  Gwidovan Rasam Ouch, I did not expect such a deep one. I guess we all have good and evil
*  potential in us. And a lot of it depends on circumstances and context.
*  Peter T. Leeson Out of that world, at least on the Soviet Union side in Europe,
*  sort of out of suffering, out of challenge, out of that kind of set of traumatic events,
*  often emerges beautiful art, music, literature. In an interview I read or heard you said you
*  enjoyed Dutch literature when you were a child. Can you tell me about the books that had an
*  influence on you in your childhood? Gwidovan Rasam
*  Well, as a teenager, my favorite Dutch author was a guy named Willem Frederik Hermans,
*  whose writing, certainly his early novels, were all about sort of
*  ambiguous things that happened during World War II. I think he was a young adult during that time,
*  and he wrote about it a lot. And very interesting, very good books, I thought, I think.
*  Peter T. Leeson In a nonfiction way?
*  Gwidovan Rasam No, it was all fiction, but it was very much set in the ambiguous world of resistance
*  against the Germans, where often you couldn't tell whether someone was truly in the resistance
*  or really a spy for the Germans. And some of the characters in his novels sort of cross that line,
*  and you never really find out what exactly happened. Peter T. Leeson
*  And in his novels, there's always a good guy and a bad guy. Is the nature of good and evil, is it
*  clear there's a hero? Gwidovan Rasam
*  No, his heroes are often more, his main characters are often anti-heroes. And so they're not very
*  heroic. They're often, they fail at some level to accomplish their lofty goals.
*  Peter T. Leeson And looking at the trajectory through the
*  rest of your life, has literature, Dutch or English or translation had an impact?
*  Outside the technical world that you existed in?
*  Gwidovan Rasam I still read novels. I don't think that it
*  impacts me that much directly. Peter T. Leeson
*  Doesn't impact your work. It's just, it's a... Gwidovan Rasam
*  It's a separate world. My work is highly technical and sort of the world of art and
*  literature doesn't really directly have any bearing on it.
*  Peter T. Leeson You don't think there's a creative element
*  to the design? You know, some would say art, design of a language is art.
*  Gwidovan Rasam I'm not disagreeing with that. I'm just
*  saying that sort of I don't feel direct influences from more traditional art on my own creativity.
*  Peter T. Leeson Right. Of course, you don't feel doesn't
*  mean it's not somehow deeply there in your subconscious. Who knows?
*  Peter T. Leeson Yeah.
*  Peter T. Leeson So let's go back to your early teens. Your
*  hobbies were building electronic circuits, building mechanical models. What, if you can just
*  put yourself back in the mind of that young Gwido, 12, 13, 14, was that grounded in a desire to
*  create a system? So to create something? Or was it more just tinkering, just the joy of puzzle
*  solving? Gwidovan Rasam
*  I think it was more the latter, actually. I maybe towards the end of my high school
*  period, I felt confident enough that that I designed my own circuits that were sort of
*  interesting, somewhat. But a lot of that time, I literally just took a model kit and follow the
*  instructions, putting the things together. I mean, that I think the first few years that I built
*  electronics kits, I really did not have enough understanding of sort of electronics to really
*  understand what I was doing. I mean, I could debug it and I could sort of follow the instructions
*  very carefully, which has always stayed with me. But I had a very naive model of like how a
*  transistor works. And I don't think that in those days, I had any understanding of coils and
*  capacitors, which actually sort of was a major problem when I started to build more complex
*  digital circuits, because I was unaware of the sort of the analog part of how they actually work.
*  And I would have things that the scheme, the schematic looked, everything looked fine, and
*  it didn't work. And what I didn't realize was that there was some megahertz level
*  oscillation that was throwing the circuit off because I had a sort of two wires were too close,
*  or the switches were were kind of poorly built. But through that time,
*  I think it's really interesting and instructive to think about because as echoes of it are in this
*  time now. So in the 1970s, the personal computer was being born. So did you sense in tinkering with
*  these circuits? Did you sense the encroaching revolution in personal computing? So if at that
*  point, you're such we'll sit you down and ask you to predict the 80s and the 90s. Do you think you
*  would be able to do so successfully to unroll this the process that's? No, I had no clue. I
*  remember I think in the summer after my senior year, or maybe it was the summer after my junior
*  year. Well, at some point, I think when I was 18, I went on a trip to the Math Olympiad in
*  Eastern Europe. And there was like I was part of the Dutch team. And there were other nerdy kids
*  that sort of had different experiences. And one of them told me about this amazing thing called a
*  computer. And I had never heard that word. My own explorations in electronics were sort of about
*  very simple digital circuits. And I, I had sort of I had the idea that I somewhat understood how
*  a digital calculator worked. And so there is maybe some echoes of computers there, but I didn't
*  didn't I never made that connection. I didn't know that when my parents were paying for
*  magazine subscriptions using punched cards that there was something called a computer that was
*  involved that read those cards and transferred the money between accounts. I was actually also
*  not really interested in those things. It was only when I went to university to study math
*  that I found out that they had a computer and students were allowed to use it. And there was
*  you're supposed to talk to that computer by programming it. What did that feel like?
*  Yeah, that was the only thing you could do with it. That the computer wasn't really
*  connected to the real world. The only thing you could do was sort of you typed your program on
*  a bunch of punched cards. You gave the punched cards to the operator. And an hour later,
*  the operator gave you back your printout. And so all you could do was write a program that
*  did something very abstract. And I don't even remember what my first forays into programming
*  were, but they were sort of doing simple math exercises and just to learn how a programming
*  language worked. Did you sense, okay, first year of college, you see this computer, you're
*  you're able to have a program and it generates some output. Did you start seeing the possibility
*  of this? Or was it a continuation of the tinkering with circuits? Did you start to imagine that one,
*  the personal computer, but did you see it as something that is a tool to get tools like a
*  word processing tool, maybe maybe for gaming or something? Or did you start to imagine that it
*  could be, you know, going to the world of robotics, like you, you know, the Frankenstein picture that
*  you could create an artificial being, there's like another entity in front of you. You did not see
*  I don't think I really saw it that way. I was really more interested in the tinkering. It's
*  maybe not as sort of a complete coincidence that I ended up sort of creating a programming language,
*  which is a tool for other programmers. I've always been very focused on the sort of activity of
*  programming itself and not so much what happens with with the program you write. I do remember,
*  and I don't remember, maybe in my second or third year, probably my second actually,
*  someone pointed out to me that there was this thing called Conway's game of life.
*  You're probably familiar with it. I think in the 70s, I think, is yeah, he came up with it.
*  So there was a scientific American column by someone who did a monthly column about
*  mathematical diversions. I'm also blanking out on the guy's name. It was very famous at the time,
*  and I think up to the 90s or so. And one of his columns was about Conway's game of life.
*  And he had some illustrations and he wrote down all the rules. And sort of there was the suggestion
*  that this was philosophically interesting that that was why Conway had called it that.
*  And all I had was like the two pages photocopy of that article. I don't even remember where I got it,
*  but it spoke to me and I remember implementing a version of that game
*  for the batch computer we were using where I had a whole Pascal program that sort of read
*  an initial situation from input and read some numbers that said do so many generations and
*  print every so many generations and then out would come pages and pages of sort of things.
*  Patterns of different kinds. Yeah.
*  Yeah. And I remember much later, I've done a similar thing using Python, but I'd sort of
*  that original version I wrote at the time I found interesting because I combined it with
*  some trick I had learned during my electronics hobbyist times. I essentially first on paper,
*  I designed a simple circuit built out of logic gates that took nine bits of input, which is the
*  sort of the cell and its neighbors and produced a new value for that cell.
*  And it's like a combination of a half adder and some other clipping. No, it's actually a full
*  adder. And so I had worked that out and then I translated that into a series of boolean operations
*  on Pascal integers where you could use the integers as bitwise values.
*  And so I could basically generate 60 bits of a generation in like
*  eight instructions or so. Nice.
*  So I was proud of that. It's funny that you mentioned, so for people who don't know Conway's
*  Game of Life, it's a cellular automata where there's single compute units that kind of look at
*  their neighbors and figure out what they look like in the next generation based on the state
*  of their neighbors. And this is a deeply distributed system in concept at least.
*  And then there's simple rules that all of them follow. And somehow out of this simple rule,
*  when you step back and look at what occurs, it's beautiful. There's an emergent complexity,
*  even though the underlying rules are simple, there's an emerging complexity.
*  Now the funny thing is you've implemented this and the thing you're commenting on is you're proud of
*  a hack you did to make it run efficiently. When you're not commenting on, like this is a beautiful
*  implementation, you're not commenting on the fact that there's an emergent complexity,
*  that you've coded a simple program and when you step back and you print out the following
*  generation after generation, that's stuff that you may have not predicted would happen is happening.
*  And is that magic? I mean, that's the magic that all of us feel when we program. When you create
*  a program and then you run it, whether it's Hello World or it shows something on screen,
*  if there's a graphical component, are you seeing the magic in the mechanism of creating that?
*  I think I went back and forth. As a student, we had an incredibly small budget
*  of computer time that we could use. It was actually measured. I once got in trouble with
*  one of my professors because I had overspent the department's budget. It's a different story.
*  I actually wanted the efficient implementation because I also wanted to explore
*  what would happen with a larger number of generations and a larger size of the board.
*  And so once the implementation was flawless, I would feed it different patterns. And then I
*  think maybe there was a follow-up article where there were patterns that were like gliders,
*  patterns that repeated themselves after a number of generations but translated one or two positions
*  to the right or up or something like that. And there were, I remember things like glider guns.
*  Well, you can Google Conway's Game of Life. People still go aw and ooh over it.
*  For a reason, because it's not really well understood why. I mean, this is what Stephen
*  Wolfram is obsessed about. We don't have the mathematical tools to describe the kind of
*  complexity that emerges in these kinds of systems. The only way you can do is to run it.
*  I'm not convinced that it's sort of a problem that lends itself to classic mathematical analysis.
*  So one theory of how you create an artificial intelligence or an artificial being is you kind
*  of have to, same with the Game of Life, you kind of have to create a universe and let it run.
*  That creating it from scratch in a design way, in coding up a Python program that creates
*  a fully intelligent system may be quite challenging that you might need to create
*  a universe just like the Game of Life is. Well, you might have to experiment with a lot of
*  different universes before there is a set of rules that doesn't essentially always just end up
*  repeating itself in a trivial way. Yeah. And Stephen Wolfram works with these simple rules,
*  says that it's kind of surprising how quickly you find rules that create interesting things.
*  You shouldn't be able to, but somehow you do. And so maybe our universe is laden with
*  rules that will create interesting things that might not look like humans, but
*  emergent phenomena that's interesting may not be as difficult to create as we think.
*  But let me sort of ask, at that time, some of the world, at least in popular press,
*  was kind of captivated, perhaps at least in America, by the idea of artificial intelligence,
*  that these computers would be able to think pretty soon. And did that touch you at all? Did that
*  in science fiction or in reality in any way? I didn't really start reading science fiction until
*  much, much later. I think as a teenager, I read maybe one bundle of science fiction stories.
*  Was it in the background somewhere, like in your thoughts? That sort of the
*  using computers to build something intelligent always fell to me because I had, I felt I had so
*  much understanding of what actually goes on inside a computer. I knew how many bits of memory it had
*  and how difficult it was to program and sort of, I didn't believe at all that you could just build
*  something intelligent out of that, that would really sort of satisfy my definition of intelligence.
*  I think the most influential thing that I read in my early 20s was Gödel Escherbach.
*  That was about consciousness and that was a big eye-opener in some sense.
*  In what sense? So on your own brain, did you at the time or do you now see your own brain as a
*  computer? Or is there a total separation of the way? So yeah, you're very pragmatically, practically
*  know the limits of memory, the limits of this sequential computing or weakly paralyzed computing
*  and you just know what we have now and it's hard to see what's going on in the brain.
*  We have now and it's hard to see how it creates but it's also easy to see. It was in the 40s, 50s,
*  60s and now at least similarities between the brain and our computers. Oh yeah, I mean I
*  totally believe that brains are computers in some sense. I mean the rules they use to play by are
*  pretty different from the rules we can sort of implement in our current hardware but I don't
*  believe in like a separate thing that infuses us with intelligence or consciousness or any of that.
*  There's no soul. I've been an atheist probably from when I was 10 years old just by thinking
*  a bit about math and the universe and well my parents were atheists. Now I know that you could
*  be an atheist and still believe that there is something sort of about intelligence or consciousness
*  that cannot possibly emerge from a fixed set of rules. I am not in that camp. I totally see that
*  sort of given how many millions of years evolution took its time.
*  DNA is a particular machine that encodes information and an unlimited amount of information
*  in chemical form and has figured out a way to replicate itself. I thought that that was maybe
*  it's 300 million years ago but I thought it was closer to half a half a billion years ago that that
*  sort of originated and it hasn't really changed that the sort of the structure of DNA hasn't
*  changed ever since. That is like our binary code that we have in hardware. I mean the basic programming
*  language hasn't changed but maybe the programming itself obviously did sort of it happened to be a
*  set of rules that was good enough to sort of develop endless variability and sort of the
*  the idea of self-replicating molecules competing with each other for resources and one type
*  eventually sort of always taking over that happened before there were any fossils. So we don't know
*  how that exactly happened but I believe it's clear that that did happen. Can you comment on
*  consciousness and how you see it because I think we'll talk about programming quite a bit. We'll
*  talk about intelligence connecting to programming fundamentally but consciousness is this whole
*  other thing. Do you think about it often as a developer of a programming language and
*  and as a human? Those are pretty sort of separate topics.
*  My line of work working with programming does not involve anything that goes in the direction of
*  developing intelligence or consciousness but sort of privately as an avid reader of popular science
*  writing I have some thoughts which is mostly that I don't actually believe that consciousness
*  is an all or nothing thing. I have a feeling that and I forget what I read that influenced this but
*  I feel that if you look at a cat or a dog or a mouse they have some form of intelligence.
*  If you look at a fish it has some form of intelligence and
*  that evolution just took a long time but I feel that the sort of evolution of
*  more and more intelligence that led to sort of the human form of intelligence followed the evolution
*  of the senses especially the visual sense. I mean there is an enormous amount of processing
*  that's needed to interpret a scene and humans are still better at that than computers are.
*  I have a feeling that there is a sort of
*  the reason that mammals in particular developed the levels of consciousness that they have and
*  that eventually going from intelligence to self-awareness and consciousness has to do with
*  sort of being a robot that has very highly developed senses. There is a lot of rich
*  sensory information coming in so that's a really interesting thought that whatever that basic
*  mechanism of DNA, whatever that basic building blocks of programming is if you just add more
*  abilities, more high resolution sensors, more sensors, you just keep stacking those things on
*  top that this basic programming in trying to survive develops very interesting things
*  that start to us humans to appear like intelligence and consciousness.
*  As far as robots go I think that the self-driving cars have the sort of
*  the greatest opportunity of developing something like that because
*  when I drive myself I don't just pay attention to the rules of the road.
*  I also look around and I get clues from that oh this is a shopping district.
*  Oh here's an old lady crossing the street. Oh here is someone carrying
*  a pile of mail. There's a mailbox. I bet you they're gonna cross the street to reach that
*  mailbox and I slow down and I don't even think about that. And so there is so much
*  where you turn your observations into an understanding of what other consciousnesses
*  are going to do or what other systems in the world are going to be. Oh that tree is gonna fall.
*  I see much more of I expect somehow that if anything is going to become conscious it's going
*  to be the self-driving car and not the network of a bazillion computers in a Google or Amazon data
*  center that are all networked together to do whatever they do.
*  So in that sense so you actually highlight because that's what I work in Thomas Veekel is you
*  highlight the big gap between what we currently can't do and what we truly need to be able to do
*  to solve the problem. Under that formulation then consciousness and intelligence is something that
*  basically a system should have in order to interact with the system. So that's the
*  basically a system should have in order to interact with us humans
*  as opposed to some kind of abstract notion of consciousness. Consciousness is something that
*  you need to have to be able to empathize, to be able to fear, understand what the fear of death is.
*  All these aspects that are important for interacting with pedestrians you need to be able to
*  do basic computation based on our human desires and flaws.
*  Yeah if you look at the dog the dog clearly knows I mean I'm not the dog owner but I have friends
*  who have dogs the dogs clearly know what the humans around them are going to do or at least they have
*  a model of what those humans are going to do and they learn. Some dogs know when you're going out
*  and they want to go out with you they're sad when you leave them alone they cry.
*  They're afraid because they were mistreated when they were younger.
*  We don't assign sort of consciousness to dogs or at least not not all that much but I also don't
*  think they have none of that. So I think it's consciousness and intelligence are not
*  all or nothing. The spectrum it's really interesting but in returning to
*  programming languages and the way we think about building these kinds of things,
*  about building intelligence, building consciousness, building artificial beings.
*  So I think one of the exciting ideas came in the 17th century and with Leibniz, Hobbes,
*  Descartes where there's this feeling that you can convert all thought all reasoning all the thing
*  that we find very special in our brains you can convert all of that into logic. You can formalize
*  it, form a reasoning and then once you formalize everything all of knowledge then you can just
*  calculate and that's what we're doing with our brains is we're calculating. So there's this whole
*  idea that we that this is possible. But they weren't aware of the concept of pattern matching
*  in the sense that we are aware of it now. They sort of thought you they had discovered incredible
*  bits of mathematics like Newton's calculus and their sort of idealism, their sort of
*  extension of what they could do with logic and math sort of went along those lines and they thought
*  there's like yeah logic there's like a bunch of rules and a bunch of input
*  they didn't realize that how you recognize a face is not just a bunch of rules but is a
*  shit ton of data plus a circuit that that sort of interprets the visual clues and the context
*  and everything else and somehow can massively parallel pattern match against stored rules.
*  I mean if I see you tomorrow here in front of the Dropbox office I might recognize you.
*  Even if I'm wearing a different shirt. Yeah but if I see you tomorrow in a coffee shop in Belmont
*  I might have no idea that it was you or on the beach or whatever. I make those kind of mistakes
*  myself all the time. I see someone that I only know as like oh this person is a colleague of my wife's
*  and then I see them at the movies and I don't recognize them. But do you see those you call
*  it pattern matching do you see that rules is unable to encode that to you everything you see
*  all the piece of information you look around this room I'm wearing a black shirt I have a certain
*  height I'm a human all these you can there's probably tens of thousands of facts you pick up
*  moment by moment about this scene you take them for granted and you accumulate
*  aggregate them together to understand the scene you don't think all of that could be encoded to
*  where at the end of the day you can just put it all on the table and calculate oh I don't know
*  what that means I mean yes in the sense that there is no there there is no actual magic there but
*  there are enough layers of abstraction from sort of from the facts as they enter my eyes and my
*  ears to the understanding of the scene that that's I don't think that that AI has really covered
*  enough of of of that distance it's like if you take a human body and you realize it's built out
*  of atoms well that that is a uselessly reductionist view right the body is built out of organs the
*  organs are built out of cells the cells are built out of proteins the proteins are built out of
*  amino acids the amino acids are built out of atoms and then you get to quantum mechanics
*  so that's a very pragmatic view I mean obviously as an engineer I agree with that kind of view but
*  you also have to consider the Sam Harris view of well intelligence is just information processing
*  that you just like you said you take in sensory information you do some stuff with it and
*  you come up with actions that are intelligent that makes it sound so easy I don't know who Sam Harris
*  is oh uh well it's philosopher so like this is how philosophers often think right and essentially
*  that's what the cart was is wait a minute if there is like you said no magic so he basically
*  says it doesn't appear like there's any magic but we know so little about it that it might as well
*  be magic so just because we know that we're made of atoms just because we know we're made of organs
*  the fact that we know very little how to get from the atoms to organs in a way that's recreatable
*  means it that you shouldn't get too excited just yet about the fact that you figured out that we're
*  made of atoms right and and and the same about taking facts as our our sensory organs take them
*  in and turning that into reasons and actions that sort of there are a lot of abstractions that we
*  haven't quite figured out how to how to deal with those I mean I
*  sometimes I don't know if I can go on a tangent or not please uh drag you back in sure so if I
*  take a simple program that parses uh say say I have a compiler it parses a program
*  in a sense the input routine of that compiler of that parser is a sense a sensing organ and it
*  builds up a mighty complicated internal representation of the program it just saw it doesn't just
*  have a linear sequence of bytes representing the text of the program anymore it has an abstract
*  syntax tree and I don't know how many of your viewers or listeners are familiar with compiler
*  technology but there is fewer and fewer these days right uh that's also true probably
*  people want to take a shortcut but there's sort of this abstraction is a data structure that the
*  compiler then uses to produce outputs that is relevant like a translation of the program to
*  machine code that can be executed by by hardware and then that data structure gets thrown away
*  when a fish or a fly sees sort of gets visual impulses I'm sure it also builds up some data
*  structure and for the fly that may be very minimal a fly may may have only a few I mean
*  in the case of a fly's brain I could imagine that there are few enough layers of abstraction that
*  it's not much more than when it's darker here than it is here well it can sense motion because a fly
*  sort of responds when you move your arm towards it so clearly its visual processing is intelligent
*  or well not intelligent but it has an abstraction for motion and we still have similar things in in
*  in but much more complicated in our brains I mean otherwise you couldn't drive a car if you
*  if you couldn't sort if you didn't have an incredibly good abstraction for motion
*  yeah in some sense the same abstraction for motion is probably one of the primary
*  sources of our of information for us we just know what to do I think we know what to do with that
*  we've built up other abstractions on top we build much more complicated data structures based on
*  that and we build more persistent data structures sort of after some processing some information
*  sort of gets stored in our memory pretty much permanently and is available on recall I mean
*  there are some things that you sort of you're conscious that you're remembering it like you
*  give me your phone number I well at my age I have to write it down but I could imagine I could
*  remember those seven numbers or ten digits and reproduce them in a while if I sort of repeat them
*  to myself a few times so that's a fairly conscious form of memorization on the other hand
*  how do I recognize your face I have no idea my brain has a whole bunch of specialized hardware
*  that knows how to recognize faces I don't know how much of that is sort of clear to me but I
*  coded in our DNA and how much of that is trained over and over between the ages of zero and three
*  but somehow our brains know how to do lots of things like that that are useful in our
*  interactions with other humans without really being conscious of how it's done anymore
*  right so our actual day-to-day lives we're operating at the very highest level of abstraction
*  we're just not even conscious of all the little details underlying it there's compilers on top
*  of it's like turtles on top of turtles or turtles all the way down it's compilers all the way down
*  but that's essentially you say that there's no magic that's what I what I was trying to get at
*  I think is with Descartes started this whole train of saying that there's no magic I mean there's
*  others before well didn't the cart also have the notion though that the soul and the body were
*  were fundamentally separate yeah I think he had to write in God in there for political reasons so I
*  don't actually I'm not a historian but there's notions in there that all of reasoning all of
*  human thought can be formalized I think that continued in the 20th century with with the
*  Russell and with with Gaido's incompleteness theorem this debate of what what what are the
*  limits of the things that could be formalized that's where the touring machine came along
*  and this exciting idea I mean underlying a lot of computing that you can do quite a lot with a
*  computer you can you can encode a lot of the stuff we're talking about in terms of recognizing faces
*  and so on theoretically in an algorithm they can then run on a computer and in that context I'd
*  like to ask programming in a philosophical way what so what it what does it mean to program a
*  computer so you said you write a python program or a compiled a c++ program that compiles to some
*  bytecode it's forming layers you're you're you're programming a layer of abstraction that's higher
*  how do you see programming in that context can it keep getting higher and higher levels of abstraction
*  I think in some at some point the higher level of levels of abstraction will not be called
*  programming and they will not resemble what we we call programming at the moment there will not
*  be source code I mean there will still be source code sort of at a lower level of the machine just
*  like they're still molecules and electrons and and sort of proteins in our brains but
*  and and so they're still programming and and and system administration and who knows what keeping
*  to keep the machine running but what the machine does is is a different level of abstraction in a
*  sense and as far as I understand the way that for last decade or more people have made progress with
*  things like facial recognition or the self-driving cars is all by endless endless amounts of training
*  data where at least as as a lay person and I feel myself totally as a lay person in that field
*  it looks like the researchers who publish the results don't necessarily know exactly how
*  how their algorithms work and I often get upset when I sort of read a sort of a fluff piece
*  about Facebook in the newspaper or social networks and they say well algorithms and that's like a
*  totally different interpretation of the word algorithm yeah because for me the way I was
*  trained or what I learned when I was eight or ten years old an algorithm is a set of rules that you
*  completely understand they can be mathematically analyzed and and and you can prove things you can
*  like prove that eris dostany sieve produces all prime numbers and only prime numbers
*  yeah so uh I don't know if you know who Andre Capati is I'm afraid not um so he's a
*  head of AI at Tesla now but he was at Stanford before and he has this cheeky way of calling
*  this concept software 2.0 so let me disentangle that for a second so so kind of what you're
*  referring to is the traditional traditional the algorithm the concept of an algorithm something
*  that's there it's clear you can read it you understand it you can prove it's functioning
*  it's kind of software 1.0 and what software 2.0 is is exactly what you describe which is
*  you have neural networks which is a type of machine learning that you feed a bunch of data
*  and that neural network learns to do a function all you specify is the inputs and the outputs you want
*  and you can't look inside you can't analyze it all you can do is train this function to
*  map the inputs to the outputs by giving a lot of data in that sense programming becomes getting a
*  lot of cleaning getting a lot of data that's what programming is uh in this well there would
*  be programming 2.0 2.0 to programming 2.0 and I wouldn't call that programming it's just a
*  different activity just like building organs out of cells is not called chemistry well so let's
*  just uh let's just step back and think sort of more generally of course but you know it's like uh
*  uh as a parent teaching teaching your kids things can be called programming in that same sense that
*  that's how program is being used you're providing them data examples uh use cases so imagine writing
*  a function not by uh not with for loops and uh clearly readable text but more saying well here's
*  a lot of examples of what this function should take and here's a lot of examples of when it takes
*  those functions it should do this and then figure out the rest so that's this 2.0 concept and the
*  question I have for you is like it's a very fuzzy way this is the reality of a lot of these pattern
*  recognition systems and so on it's a fuzzy way of quote unquote programming what do you think about
*  this kind of world uh should be called something totally different than programming it's like if
*  you're a software engineer does that mean you're you're designing systems that are very can be
*  systematically tested evaluated they have a very specific specification and then this other fuzzy
*  software 2.0 world machine learning world that's that's something else totally or is there some
*  intermixing that's possible well the question is probably only being asked because we we don't
*  quite know what that software 2.0 actually is and it sort of I think there is a truism that
*  every task that ai has has tackled in the past at some point we realized how it was done and then
*  it was no longer considered part of artificial intelligence because it was no longer necessary
*  to to use that term it was just oh now we know how to do this and a new field of science or
*  engineering has been developed and i don't know if sort of every form of learning or
*  sort of controlling computer systems should always be called programming so i don't know maybe i'm
*  focused too much on the terminology i but i expect that
*  that there just will be different concepts where people with sort of different education and a
*  different model of what they're trying to do will will develop those concepts yeah and i guess if
*  you could comment on another way to put this concept is i think i think the kind of functions
*  that neural networks provide is things as opposed to being able to upfront prove that this should
*  work for all cases you throw at it all you're able it's the worst case analysis versus average case
*  all you're able to say is it's it seems on everything we've tested to work 99.9 percent
*  of the time but we can't guarantee it and it it fails in unexpected ways we can even give you
*  examples of how it fails in unexpected ways but it's like really good most of the time yeah but
*  there's no room for that in current ways we think about programming uh programming 1.2
*  is actually sort of getting to that point too where the sort of the ideal of a bug free program
*  has been abandoned long ago by most software developers we only care about bugs that manifest
*  themselves often enough to be annoying and we're willing to take the occasional crash or outage or
*  incorrect result for granted because we can't possibly we we don't have enough programmers to
*  make all the code bug free and it would be an incredibly tedious business and if you try to
*  throw formal methods at it it gets it becomes even more tedious so every once in a while the
*  user clicks on a link in and somehow they get an error and the average user doesn't panic they
*  just click again and see if it works better the second time which often magically it does
*  or they go up and they try some other way of performing their tasks so that's sort of an
*  end-to-end recovery mechanism and inside systems there is all sorts of retries and timeouts and
*  fallbacks and I imagine that that sort of biological systems are even more full of that
*  because otherwise they wouldn't survive. Do you think programming should be taught and thought of
*  as exactly what you just said before I come from is kind of you're you're always denying that fact
*  always? In sort of basic programming education
*  the sort of the programs you're you're having students write are so small and simple
*  that if there is a bug you can always find it and fix it because the sort of programming as it's
*  being taught in some even elementary middle schools in high school introduction to programming
*  classes in college typically it's programming in the small very few classes sort of actually teach
*  software engineering building large systems I mean every summer here at Dropbox we have a large
*  number of interns every tech company on the west coast has the same thing these interns are always
*  amazed because this is the first time in their life that they see what goes on in a really large
*  software development environment and everything they've learned in college was almost always about
*  a much smaller scale and somehow that difference in scale makes a qualitative difference in how you
*  how you do things and how you think about it. If you then take a few steps back into decades of 70s
*  and 80s when you're first thinking about Python or just that world of programming languages
*  did you ever think that there would be systems as large as underlying Google, Facebook and Dropbox?
*  Did you when you were thinking about Python? I was actually always caught by surprise by
*  sort of this yeah pretty much every stage of computing. So maybe just because you've spoken
*  in other interviews but I think the evolution of programming languages are fascinating and it's
*  especially because it leads from my perspective towards greater and greater degrees of intelligence.
*  I learned the first programming language I played with in Russia was with the turtle logo.
*  If you look I just have a list of programming languages all of which I've played with a little
*  bit and they're all beautiful in different ways from Fortran, Cobol, Lisp, Algol 60,
*  Basic, Logo again, C, as a few the object oriented came along in the 60s, Simula, Pascal, Small Talk,
*  all of that leads. They're all the classics. The classics yeah the classic hits right. Scheme
*  built that's built on top of Lisp, on the database side SQL, C++ and all that leads up to Python,
*  Pascal too and that's before Python, Matlab, these kind of different communities, different languages.
*  So can you talk about that world? I know that sort of Python came out of ABC which I actually
*  never knew that language. I just having researched this conversation went back to you see and it
*  looks remarkably it has a lot of annoying qualities but underneath those like all caps and so on
*  but underneath that there's elements of Python that are quite they're already there. That's where
*  I got all the good stuff. All the good stuff so but in that world you're swimming these programming
*  languages were you focused on just the good stuff in your specific circle or did you have a sense
*  of what what is everyone chasing? You said that every programming language is built to scratch an itch.
*  Were you aware of all the itches in the community and if not or if yes I mean what itch were you
*  trying to scratch with Python? Well I'm glad I wasn't aware of all the itches because I would
*  probably not have been able to do anything. I mean if you're trying to solve every problem at once
*  I mean if you're trying to solve every problem at once
*  you solve nothing. Well yeah it's it's too overwhelming and so I had a very
*  very focused problem. I wanted a programming language that sat somewhere in between shell
*  scripting and C and now arguably there is like one is higher level one is lower level
*  and Python is sort of a language of an intermediate level although it's still
*  pretty much at the high level and I was I was thinking about much more about
*  I want a tool that I can use to be more productive as a programmer in a very specific environment
*  and I also had given myself a time budget for the development of the tool and that was sort of
*  about three months for both the design like thinking through what are all the features
*  of the language syntactically and semantically and how do I implement the whole pipeline from
*  parsing the source code to executing it. So I think both with the timeline and the goals
*  it seems like productivity was at the core of it as a goal so like for me in the 90s and the
*  first decade of the 21st century I was always doing machine learning AI programming for my research
*  was always in C++ and then and then the other people who are a little more mechanical engineering
*  electrical engineering are are MATLAB-y they're a little bit more MATLAB focused those are the
*  world and maybe a little bit Java too but people who are more interested in emphasizing the object
*  oriented nature of things so but then in the last 10 years or so especially with the oncoming of
*  neural networks in these packages that are built on Python to interface with with neural networks
*  I switched to Python and it's just I've noticed a significant boost that I can't exactly because
*  I don't think about it but I can't exactly put into words why I'm just accept much much more
*  productive just being able to get the job done much much faster so how do you think whatever
*  that qualitative difference is I don't know if it's quantitative it could be just a feeling
*  I don't know if I'm actually more productive but how do you think about they are
*  yeah well that's right I think there's elements let me just speak to one aspect I think those
*  effecting my productivity is C++ was I really enjoyed creating performant code and creating
*  a beautiful structure where everything that you know this kind of going into this especially with
*  the newer and newer standards of templated programming of just really creating this beautiful
*  beautiful formal structure that I found myself spending most of my time doing that as opposed
*  to getting it parsing a file and extracting a few keywords or whatever the task I was trying to do
*  so what is it about Python how do you think of productivity in general as you were designing it
*  now sort of through the decades last three decades what do you think it means to be a productive
*  programmer and how did you try to design it into the language there are different tasks
*  and as a programmer it's it's useful to have different tools available that sort of are
*  suitable for different tasks so I still write C code I still write shell code but I write most
*  of my my things in Python why do I still use those other languages because sometimes the task just
*  demands it and well I would say most of the time the task actually demands a certain language
*  because the task is not write a program that solves problem x from scratch but it's more like
*  fix a bug in existing program x or add a small feature to an existing large program
*  but even if if you sort of if you're not constrained in your choice of language by context like that
*  uh there is still the fact that if you write it in a certain language then you sort of
*  you you have this balance between how long does it time to does it take you to write the code
*  write the code and how long does the code run and when you're in sort of
*  in the phase of exploring solutions you often spend much more time writing the code than
*  running it because every time you've sort of you've run it you see that the output is not
*  quite what you wanted and you spend some more time coding and a language like Python just
*  makes that iteration much faster because there are fewer details there is a large library
*  sort of there are fewer details that that you have to get right before your program compiles and runs
*  uh there are libraries that do all sorts of stuff for you so you can sort of very quickly
*  take a bunch of existing components put them together and get your prototype application
*  running just like when i was building electronics i was using a breadboard most of the time
*  so i i had this like sprawled out circuit that if you shook it it would stop working because it was
*  not put together very well but it functioned and all i wanted was to see that it worked and then
*  move on to the next next schematic or design or add something to it once you've sort of figured out
*  oh this is the perfect design for my radio or light sensor or whatever then you can say okay
*  how do we design a pcb for this how do we solder the components in a small space how do we make it
*  so that it is robust against uh say voltage fluctuations uh or mechanical uh disruption
*  i mean i know nothing about that when it comes to designing electronics but i know a lot about that
*  when it comes to to writing code so the initial initial steps are uh efficient fast and there's
*  not much stuff that gets in the way but you're kind of describing um from uh like darwin described
*  the evolution of species right you're you're observing of what is about true about python now
*  if you take a step back if the art of if the act of creating languages is art and you had three
*  months to do it initial steps so you just specified a bunch of goals sort of things that you observe
*  about python perhaps you had those goals but how do you create the rules the syntactic structure
*  the the features that result in those so i have in the beginning and i have follow-up questions
*  about through the evolution of python too but in the very beginning when you're sitting there
*  creating uh the the lexical analyze or whatever evolution was still a big part of it because
*  i i sort of i said to myself i don't want to have to design everything from scratch i'm going to
*  borrow features from other languages that i like oh interesting so you basically exactly you first
*  observe what you like yeah and so that's why if you're 17 years old and you want to sort of create
*  a programming language you're not going to be very successful at it because you have no experience
*  with other languages whereas i was in my let's say mid-30s uh i had written parsers before so i had
*  worked on the implementation of abc i had spent years debating the design of abc with its authors
*  it's that with its designers i had nothing to do with the design it was designed fully as it was
*  ended up being implemented when i joined the team but so you borrow ideas and concepts and very
*  concrete sort of local rules from different languages like the indentation and certain
*  other syntactic features from abc but i chose to borrow string literals and how numbers work from c
*  and various other things so and then if you take that further so yet you've had this funny sounding
*  but i think surprisingly accurate and at least practical uh title of benevolent dictator for life
*  for quite you know for the last three decades or whatever or no not the actual title but functionally
*  speaking uh so you had to make decisions design decisions
*  can you maybe uh let's take python 2 so python releasing python 3 as an example
*  it's not backward compatible to python 2 in in ways that a lot of people know so what was that
*  deliberation discussion decision like yeah what was the psychology of that experience
*  do you regret any aspects of how that experience undergone uh that well yeah so it was a group
*  process really it at that point even though i was bdfl in nine in name and and certainly everybody
*  everybody sort of respected my my position as the creator and and the current sort of owner of the
*  language design i was looking at everyone else for feedback sort of python 3.0 in some sense was
*  sparked by other people in the community uh pointing out oh well there are a few issues that
*  sort of bite users over and over can we do something about that and for python 3 we took a
*  number of those python wards as they were called at the time and we said can we try to sort of make
*  small changes to the language that address those wards and we had sort of in the past we had always
*  taken backwards compatibility very seriously and so many python wards in earlier versions had already
*  been resolved because they could be resolved while maintaining backwards compatibility or sort of
*  using a very gradual path of evolution of the language in a certain area and so we were stuck
*  with a number of wards that were widely recognized as problems not like roadblocks but nevertheless
*  sort of things that some people trip over and you know that that's always the same thing that
*  people trip over when they trip and we could not think of a backwards compatible way of
*  resolving those issues but it's still an option to not resolve the issues and so yes for for a long
*  time we had sort of resigned ourselves to well okay the language is not going to be perfect in
*  this way and that way and that way and we sort of certain of these I mean there are still plenty
*  of things where you can say well that's that particular detail is better in java or in r or in
*  visual basic or whatever and we're okay with that because well we can't easily change it
*  uh it's not too bad we can do a little bit with user education or we can have a static analyzer
*  or warnings in in the parser or something but there were things where we thought well these are
*  really problems that are not going away they are getting worse in the future
*  we should do something about it do something but ultimately there is a decision to be made right
*  yes so was that the toughest decision in the history of python you had to make
*  as the benevolent dictator for life or if not what are there maybe even on the smaller scale what was
*  the decision where you were really torn up about well the toughest decision was probably to resign
*  all right let's go there hold on a second then let me just because in the interest of time too
*  because i have a few cool questions for you i mean let's touch a really important one because
*  it was quite dramatic and beautiful in certain kinds of ways uh in july this year three months
*  ago you wrote now that pep 572 is done i don't ever want to have to fight so hard for a pep
*  and find that so many people despise my decisions i would like to remove myself entirely from the
*  decision process i'll still be there for a while as an ordinary core developer and i'll still be
*  available to mentor people possibly more available but i'm basically giving myself a permanent
*  vacation from being bdfl benevolent dictator for life and you all will be on your own
*  first of all just this it's uh it's almost shakespeareian i'm not going to appoint a
*  successor so what are you all going to do create a democracy anarchy a dictatorship a federation
*  so that was a very dramatic and beautiful
*  a set of statements it's almost it's open-ended nature called the community to create a future
*  for python it's just kind of a beautiful aspect to it wow so what and and dramatic you know
*  what was making that decision like what was on your heart on your mind stepping back now a few
*  months later we could take me to your mind i'm glad you like the writing because
*  it was actually written pretty quickly it was literally something like
*  after months and months of going around in circles i had finally approved pep 572
*  which i i had a big hand in its design although i didn't initiate it originally i sort of gave
*  it a bunch of nudges in a direction that would be better for the language so so sorry just to ask
*  is async i o is no that's the one or no no pep 572 was actually a small feature which is assignment
*  expressions oh assignment expressions okay that had been thought there was just a lot of debate
*  where a lot of people claimed that they knew what was pythonik and what was not pythonik and they
*  knew that this was going to destroy the language this was like a violation of python's most
*  fundamental design philosophy and i thought that was all bullshit because i was in favor of it and
*  i would think i know something about python's design philosophy so i was
*  really tired and also stressed of that thing and literally after sort of announcing i was going to
*  accept it a certain wednesday evening i had finally sent the email it's accepted now let's just go
*  implement it so i went to bed feeling really relieved that's behind me and i wake up thursday
*  morning 7 a.m and i think well that was the last one that's going to be such such a terrible
*  debate and that's going to be so that's the last time that i let myself be so stressed out about
*  a pep decision i should just resign i've been sort of thinking about retirement for half a decade
*  i've been joking and sort of mentioning retirement sort of telling the community
*  some point in the future i'm going to retire don't take that fl part of my title too literally
*  and i thought okay this is it i'm done i had the day off i wanted to have a good time with my wife
*  we were going to a little beach town nearby and in i think maybe 15 20 minutes i wrote that thing
*  that you just called shakespearian and the funny thing is i guess so much crap for calling you
*  shakespearian i didn't even i didn't even realize what a monumental decision it was
*  because five minutes later i read that sent a link to my message back on twitter
*  where people were already discussing on twitter guido resigned as the bdfl
*  and i had i had posted it on an internal forum that i thought was only read by core developers
*  so i thought i would at least have one day before the news would sort of get out
*  the on your own aspects i had also an element of quite it was quite a powerful element
*  of the uncertainty that lies ahead but can you also just briefly talk about you know like for
*  example i play guitar as a hobby for fun and whenever i play people are super positive
*  it's super friendly they're like this is awesome this is great but sometimes i enter as an outside
*  observer i enter the programming community and there seems to some sometimes be camps on whatever
*  the topic and and the two camps the two or plus camps are often pretty harsh at criticizing the
*  opposing camps as an onlooker i may be totally wrong on this yeah holy wars are are sort of a
*  favorite activity in the programming community and what is the psychology behind that is is that
*  okay for a healthy community to have is that is that a productive force ultimately for the
*  evolution of a language well if everybody is betting each other on the back and never telling
*  the truth yes uh it would not be a good thing i think there is a middle ground where sort of
*  being nasty to each other is not okay but there there is is is a middle ground where there is
*  healthy ongoing criticism and feedback that is very productive and you you mean at at every level
*  you see that i mean someone proposes to fix a very small issue in a code base uh chances are
*  that some reviewer will sort of respond by saying well actually you can do it better the other way
*  right uh when it comes to deciding on the future of the python core developer community
*  we now have i think five or six competing proposals for a constitution
*  so that future do you have a fear of that future do you have a hope for that future
*  i'm very confident about that future it by and large i think that the debate has been very healthy
*  and productive uh and i actually when when i wrote that resignation email i knew that that python was
*  in a very good spot and that the python core development community the group of 50 or 100
*  people who sort of write or review most of the code that goes into python those people
*  get along very well most of the time uh a large number of different areas of expertise are
*  represented uh different levels of experience in the python core dev community different levels
*  of experience completely outside it in software development in general large systems small systems
*  embedded systems so i i felt okay resigning because i knew that that the community can
*  really take care of itself and out of a grab bag of future future developments let me ask if you
*  can comment maybe on all very quickly concurrent programming parallel computing async i-o
*  these are things that people have uh expressed hope complained about whatever have discussed on
*  on reddit async i-o so the parallelization in general uh packaging i was totally clueless on
*  this i just use pip to install stuff but apparently there's pip nv poetry there's these dependency
*  packaging systems that manage dependencies and so on they're emerging and there's a lot of confusion
*  about what's what's the right thing to use then also uh functional programming the the ever you
*  know uh the the uh are we going to get more functional programming or not this kind of
*  this kind of idea and of course the uh the the gil is a the connected to the parallelization i
*  suppose the global interpreter lock problem can you just comment on whichever you want to comment
*  on well let's take the gil and parallelization and async i-o as one one topic i'm not that hopeful
*  that python will develop into a sort of high concurrency high parallelism language
*  that's sort of the the way the language is designed the way most users use the language
*  the way the language is implemented all make that a pretty unlikely future so you you think it
*  might not even need to really the way people use it it it might not be something that should be a
*  of great concern i think i think async i-o is a special case because it sort of allows overlapping
*  i-o and only i-o and that is is a sort of best practice of supporting very high throughput i-o
*  many connections uh per second uh i'm not worried about that i think async i-o will evolve there are
*  a couple of competing packages we have some very smart people who are sort of pushing us in sort of
*  to make async i-o better parallel computing i think that python is not the language for that
*  there are there are ways to work around it but you sort of you can't expect to write
*  an algorithm in python and have a compiler automatically paralyze that what you can do
*  is use a package like numpy and there are a bunch of other very powerful packages that sort of
*  use all the cpus available because you tell the package here's the data here's the abstract
*  operation to apply over it go at it and then then we're back in the c++ world but the
*  those packages are themselves implemented usually in c++ that's right that's that's where tensorflow
*  and all these packages come in where they parallelize across gpus for example they take care of that
*  for you so in terms of packaging uh can you comment on the packaging and yeah my packaging has always
*  been my least favorite topic it's it's it's a really tough problem because uh the os and the
*  the os and the platform want to own packaging uh but their packaging solution is not specific
*  to a language like if you take linux there are two competing packaging solutions for linux
*  or for unix in uh in general and but they all work across all languages
*  and several languages like node javascript uh and ruby and python all have their own packaging
*  solutions that only work within the ecosystem of that language well what should you use
*  that is a tough problem my own own approach is i use the system packaging system to install python
*  and i use the python packaging system then to install third-party python packages that's what
*  most people do 10 years ago python packaging was really a terrible situation nowadays pip is the
*  future there is there is a separate ecosystem for a numerical and scientific python python based on
*  anaconda those two can live together i don't think there is a need for more than that great
*  so that's that's packaging that's well at least for me that's that's where i've been extremely
*  happy i didn't i didn't even know this was an issue until it was brought up well in the interest of
*  time let me sort of skip through a million other questions i have so i watched the five hour five
*  five and a half hour oral history uh that you've done with the computer history museum and the nice
*  thing about it it gave this because of the linear progression of the interview it gave this feeling
*  of a life you know a life well lived with interesting things in it um sort of a pretty i
*  would say a good spend of of this little existence we have on earth so outside of your family uh
*  looking back what about this journey are you really proud of
*  are there moments that stand out accomplishments ideas is it the creation of python itself that
*  stands out as a thing that you look back and say damn i did pretty good there
*  well i would say that python is definitely the best thing i've ever done
*  definitely the best thing i've ever done and i i wouldn't sort of say just the creation of python
*  but the way i sort of raised python like a baby i didn't just conceive a child but i raised a child
*  and now i'm setting the child free in the world and i've set up the child to to sort of be able
*  to take care of himself and i'm i'm very proud of that and as the announcer of monty python's
*  flying circus used to say and now for something completely different do you have a favorite
*  monty python moment or a moment in hitchhiker's guide or any other literature show movie that
*  cracks you up when you think about it oh you can always play me the parrots the dead parrot sketch
*  oh that's brilliant yeah that's my favorite as well pushing up the daisies
*  okay grita thank you so much for talking with me today
*  lex it's been a great conversation
*  you
