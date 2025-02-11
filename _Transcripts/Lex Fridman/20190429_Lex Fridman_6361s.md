---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 6361s
Video Keywords: []
Video Views: 77030
Video Rating: None
---

# Oriol Vinyals: DeepMind AlphaStar, StarCraft, and Language | Lex Fridman Podcast #20
**Lex Fridman:** [April 29, 2019](https://www.youtube.com/watch?v=Kedt2or9xlo)
*  The following is a conversation with Ariol Vinales. He's a senior research scientist
*  at Google DeepMind, and before that he was at Google Brain and Berkeley.
*  His research has been cited over 39,000 times. He's truly one of the most brilliant and impactful
*  minds in the field of deep learning. He's behind some of the biggest papers and ideas in AI,
*  including sequence-to-sequence learning, audio generation, image captioning,
*  neural machine translation, and, of course, reinforcement learning. He's a lead researcher
*  of the AlphaStar project, creating an agent that defeated a top professional at the game of Star
*  Craft. This conversation is part of the Artificial Intelligence podcast. If you enjoy it, subscribe on
*  YouTube, iTunes, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D.
*  And now, here's my conversation with Ariol Vinales.
*  You spearheaded the DeepMind team behind AlphaStar that recently beat a top professional player at
*  Star Craft. So you have an incredible wealth of work in deep learning and a bunch of fields,
*  but let's talk about Star Craft first. Let's go back to the very beginning, even before AlphaStar,
*  before DeepMind, before deep learning. First, what came first for you? A love for programming
*  or a love for video games? I think for me, it definitely came first, the drive to play video
*  games. I really liked computers. I didn't really code much, but what I would do is I would just
*  mess with the computer, break it and fix it. That was the level of skills, I guess, that I gained
*  in my very early days, when I was 10 or 11. Then I really got into video games, especially Star
*  Craft, actually, the first version. I spent most of my time just playing pseudo-professionally,
*  as professionally as you could play back in 98 in Europe, which was not a very main scene,
*  what's called nowadays e-sports. Right, of course, in the 90s. So
*  how did you get into Star Craft? What was your favorite race? How did you develop your skill
*  and what was your strategy? All that kind of thing. As a player, I tended to try to play not
*  many games, not to disclose the strategies that I developed. I like to play random, actually,
*  not in competitions, but just to... I think in Star Craft, there's three main races,
*  and I found it very useful to play with all of them. I would choose random many times,
*  even sometimes in tournaments, to gain skill on the three races, because it's not how you play
*  against someone, but also if you understand the race because you played, you also understand what's
*  annoying. Then when you're on the other side, what to do to annoy that person, to try to gain
*  advantages here and there and so on. So I actually played random, although I must say,
*  in terms of favorite race, I really like Zerk. I was probably best at Zerk, and that's probably
*  what I tend to use towards the end of my career before starting university. So let's step back a
*  little bit. Could you try to describe Star Craft to people that may never have played video games,
*  especially the massively online variety like Star Craft?
*  So Star Craft is a real-time strategy game, and the way to think about Star Craft, perhaps,
*  if you understand a bit chess, is that there's a board, which is called map, or like, yeah,
*  the map where people play against each other. There's obviously many ways you can play, but
*  the most interesting one is the one versus one setup, where you just play against someone else,
*  or even the build in AI. Blizzard put a system that can play the game reasonably well, if you
*  don't know how to play. And then in this board, you have again pieces like in chess, but these
*  pieces are not there initially, like they are in chess. You actually need to decide to gather
*  resources to decide which pieces to build. So in a way, you're starting almost with no pieces.
*  You start gathering resources in Star Craft. There's minerals and gas that you can gather,
*  and then you must decide how much do you want to focus, for instance, on gathering more resources
*  or starting to build units or pieces. And then once you have enough pieces or maybe like attack,
*  a good attack composition, then you go and attack the other side of the map.
*  And now the other main difference with chess is that you don't see the other side of the map.
*  So you're not seeing the moves of the enemy. It's what we call partially observable.
*  So as a result, you must not only decide trading of economy versus building your own units,
*  but you also must decide whether you want to scout to gather information.
*  But also by scouting, you might be giving away some information that you might be hiding from
*  the enemy. So there's a lot of complex decision making all in real time. There's also, unlike
*  chess, this is not a turn-based game. You play basically all the time, continuously, and thus,
*  some skill in terms of speed and accuracy of clicking is also very important. And people that
*  train for this really play this game at an amazing skill level. I've seen many times these, and if
*  you can witness this life, it's really, really impressive. So in a way, it's kind of a chess
*  where you don't see the other side of the board. You're building your own pieces, and you also need
*  to gather resources to basically get some money to build other buildings, pieces, technology,
*  and so on. From the perspective of the human player, the difference between that and chess,
*  or maybe that and a game like turn-based strategy like Heroes of Might and Magic,
*  is that there's an anxiety because you have to make these decisions really quickly. And if you
*  are not actually aware of what decisions work, it's a very stressful balance. Everything you
*  describe is actually quite stressful, difficult to balance for an amateur human player. I don't
*  know if it gets easier at the professional level, like if they're fully aware of what they have to
*  do. But at the amateur level, there's this anxiety, oh crap, I'm being attacked, oh crap, I have to
*  build up resources, oh, I have to probably expand. And all these, the real time strategy aspect is
*  really stressful and computation, I'm sure, difficult. We'll get into it. But for me,
*  Battle.net, so StarCraft was released in 98, 20 years ago, which is hard to believe.
*  And Blizzard Battle.net with Diablo in 96 came out. And to me, it might be a narrow perspective,
*  but it changed online gaming and perhaps society forever. But I may have made way too narrow a
*  viewpoint, but from your perspective, can you talk about the history of gaming over the past 20 years?
*  Is this how transformational, how important is this line of games?
*  Right. So I think I kind of was an active gamer whilst this was developing the internet,
*  online gaming. So for me, the way it came was I played other games strategy related, I played
*  a bit of Command and Conquer, and then I played Warcraft 2, which is from Blizzard. But at the
*  time, I didn't know, I didn't understand about what Blizzard was or anything. Warcraft 2 was just a
*  game which was actually very similar to StarCraft in many ways. It's also a real time strategy game
*  where there's orcs and humans, so there's only two races.
*  But it was offline.
*  And it was offline. So I remember a friend of mine came to school and said, oh, there's this new
*  cool game called StarCraft. And I just said, oh, this sounds like just a copy of Warcraft 2.
*  Until I kind of installed it. And at the time, I am from Spain, so we didn't have very good
*  internet. So for us, StarCraft became first kind of an offline experience where you kind of start
*  to play these missions, right? You play against some sort of scripted things to develop the story
*  of the characters in the game. And then later on, I started playing against the built-in AI.
*  And I thought it was impossible to defeat it. Then eventually you defeat one and you can actually
*  play against seven built-in AIs at the same time, which also felt impossible. But actually,
*  it's not that hard to beat seven built-in AIs at once. So once we achieved that, also we discovered
*  we could play, as I said, internet wasn't that great, but we could play with the LAN, right?
*  Basically against each other if we were in the same place, because you could just connect machines
*  with cables, right? So we started playing in LAN mode as a group of friends. And it was really,
*  really much more entertaining than playing against AIs. And later on, as internet was starting to
*  develop and being a bit faster and more reliable, then it's when I started experiencing Battle.net,
*  which is this amazing universe, not only because of the fact that you can play the game against
*  anyone in the world, but you can also get to know more people. You just get exposed to now
*  this vast variety of it's kind of a bit when the chats came about, right? There was a chat system
*  you could play against people, but you could also chat with people not only about Stalker,
*  but about anything. And that became a way of life for kind of two years. And obviously,
*  it exploded in me in that I started to play more seriously going to tournaments and so on and so
*  forth. Do you have a sense on a societal sociological level, what's this whole part of society that many
*  of us are not aware of? And it's a huge part of society, which is gamers. I mean, every time I
*  come across that in YouTube or streaming sites, I mean, this is a huge number of people play games
*  religiously. Do you have a sense of those folks, especially now that you've returned to that realm
*  a little bit on the AI side? Yeah. So in fact, even after Stalker, I actually played World of
*  Warcraft, which is the main sort of online worlds and presence that you get to interact with lots
*  of people. So I played that for a little bit. To me, it was a bit less stressful than Stalker
*  because winning was kind of a given. You just put in this world and you can always complete missions.
*  But I think it was actually the social aspect of, especially StarCraft first and then games like
*  World of Warcraft really shaped me in a very interesting way because what you get to experience
*  is just people you wouldn't usually interact with. So even nowadays, I still have many Facebook
*  friends from the area where I played online and their ways of thinking is even political.
*  They just don't, we don't live in it. We don't interact in the real world, but we were connected
*  by basically fiber. And that way I actually get to understand a bit better that we live in a diverse
*  world. And these were just connections that were made by, because I happened to go in a city,
*  in a virtual city as a priest and I met this warrior and we became friends and then we
*  started playing together. So I think it's transformative and more and more and more
*  people are more aware of it. It's becoming quite mainstream. But back in the day, as you were saying
*  in 2000, 2005 even, it was still a very strange thing to do, especially in Europe. I think there
*  were exceptions like Korea, for instance, it was amazing that everything happened so early in terms
*  of cyber cafes. If you go to Seoul, it's a city that back in the day, Starcraft was kind of,
*  you could be a celebrity by playing Starcraft, but this was like 99, 2000, right? It's not like
*  recently. So yeah, it's quite interesting to look back and yeah, I think it's changing society.
*  The same way, of course, like technology and social networks and so on are also transforming
*  things. And a quick tangent, let me ask, you're also one of the most productive people in your
*  particular chosen passion and path in life and yet you're also appreciate and enjoy video games.
*  Do you think it's possible to enjoy video games in moderation? Someone told me that you could
*  choose two out of three. When I was playing video games, you could choose having a girlfriend,
*  playing video games or studying. And I think for the most part, it was relatively true.
*  These things do take time. Games like Starcraft, if you take the game pretty seriously and you
*  want to study it, then you obviously will dedicate more time to it. And I definitely took gaming and
*  obviously studying very seriously. I love learning science and et cetera. So to me, especially when
*  I started university undergrad, I kind of stepped off Starcraft. I actually fully stopped playing
*  and then World of Warcraft was a bit more casual. You could just connect online. And I mean, it was
*  fun. But as I said, that was not as much time investment as it was for me in Starcraft.
*  OK, so let's get into AlphaStar. You're behind the team. So DeepMind has been working on Starcraft
*  and released a bunch of cool open source agents and so on in the past few years.
*  But AlphaStar really is the moment where the first time you beat a world class player. So what are
*  the parameters of the challenge in the way that AlphaStar took it on? And how did you and David
*  and the rest of the DeepMind team get into it? Consider that you can even beat the best in the
*  world or top players. I think it all started back in 2015. Actually, I'm lying. I think it was 2014
*  when DeepMind was acquired by Google. And I at the time was at Google Brain, which was in California,
*  is still in California. We had this summit where we got together, the two groups. So Google Brain
*  and Google DeepMind got together and we gave a series of talks. And given that they were doing
*  deep reinforcement learning for games, I decided to bring up part of my past,
*  which I had developed at Berkeley, like this thing which we call Berkeley Overmind, which is really
*  just a Starcraft one bot. So I talked about that. And I remember Demis just came to me and said,
*  well, maybe not now. It's perhaps a bit too early, but you should just come to DeepMind and
*  do this again with deep reinforcement learning. And at the time, it sounded very science fiction
*  for several reasons. But then in 2016, when I actually moved to London and joined DeepMind,
*  transferring from Brain, it became apparent that because of the AlphaGo moment and Blizzard reaching
*  out to us to say, wait, do you want the next challenge? And also me being full time at DeepMind,
*  all these came together. And then I went to Irvine in California to the Blizzard headquarters
*  to just chat with them and try to explain how would it all work before you do anything.
*  And the approach has always been about the learning perspective. So in Berkeley, we did
*  a lot of rule-based conditioning. And if you have more than three units, then go attack. And if the
*  other has more units than me, I retreat, and so on and so forth. And of course, the point of deep
*  reinforcement learning, deep learning, machine learning in general is that all these should be
*  learned behavior. So that kind of was the DNA of the project since its inception in 2016, where we
*  just didn't even have an environment to work with. And so that's how it all started really.
*  So if you go back to that conversation with Demis or even in your own head, how far away did you,
*  because we're talking about Atari games, we're talking about Go, which is kind of, if you're
*  honest about it, really far away from StarCraft. Well, now that you've beaten it, maybe you could
*  say it's close, but it seems like StarCraft is way harder than Go, mathematically speaking.
*  So how far away did you think you were? Do you think in 2019 and 18 you could be doing as well
*  as you have? Yeah, when I kind of thought about, okay, I'm going to dedicate a lot of my time and
*  focus on this. And obviously I do a lot of different research in deep learning. So spending
*  time on it, I mean, I really had to kind of think there's going to be something good happening out
*  of this. So really, I thought, well, this sounds impossible. And it probably is impossible to do
*  the full thing, like the full game, where you play one versus one, and it's only a neural
*  network playing and so on. So it really felt like I just didn't even think it was possible.
*  But on the other hand, I could see some stepping stones towards that goal. Clearly, you could
*  define sub problems in StarCraft and sort of dissect it a bit and say, okay, here is a part
*  of the game, here's another part. And also, obviously, the fact, so this was really also
*  critical to me, the fact that we could access human replays, right? So Blizzard was very kind,
*  and in fact, they open source this for the whole community, where you can just go. And it's not
*  every single StarCraft game ever played, but it's a lot of them, you can just go and download.
*  And every day they will, you can just query a data set and say, well, give me all the games
*  that were played today. And given my kind of experience with language and sequences and
*  supervised learning, I thought, well, that's definitely going to be very helpful and something
*  quite unique now, because ever before, we had such a large data set of replays of people playing
*  the game at this scale of such a complex video game, right? So that to me was a precious resource.
*  And as soon as I knew that Blizzard was able to kind of give this to the community,
*  I started to feel positive about something non-trivial happening. But I also thought the
*  full thing, like really no rules, no single line of code that tries to say, well, I mean,
*  if you see this, you need to build a detector. All these, not having any of these specializations
*  seemed really, really, really difficult to me. Intuitively. I do also like that Blizzard was
*  teasing or even trolling you, sort of almost, yeah, pulling you in into this really difficult
*  challenge. Did they have any aware, what's the interest from the perspective of Blizzard,
*  except just curiosity? Yeah, I think Blizzard has really understood and really bring forward
*  this competitiveness of e-sports in games. StarCraft really kind of sparked a lot of
*  something that almost was never seen, especially as I was saying, back in Korea. So they just
*  probably thought, well, this is such a pure one versus one setup that it would be great to see
*  if something that can play Atari or Go and then later on chess could even tackle this kind of
*  complex real-time strategy game. So for them, they wanted to see first, obviously, whether
*  it was possible, if the game they created was in a way solvable to some extent. And I think on
*  the other hand, they also are a pretty modern company that innovates a lot. So just starting
*  to understand AI for them, how to bring AI into games is not AI for games, but games for AI.
*  Both ways, I think, can work. And we obviously at DeepMind use games for AI to drive AI progress,
*  but Blizzard might actually be able to do, and many other companies, to start to understand and
*  do the opposite. So I think that is also something they can get out of this. And they definitely,
*  we have brainstormed a lot about this. But one of the interesting things to me
*  about StarCraft and Diablo and these games that Blizzard has created is the task of balancing
*  classes, for example, sort of making the game fair from the starting point and then let skill
*  determine the outcome. Can you first comment, there's three races, Zerg, Protoss, and Terran.
*  I don't know if I've ever said that out loud. Is that how you pronounce it? Terran?
*  Yeah. Terran.
*  Yeah. Yeah, I don't think I've ever
*  in person interacted with anybody about StarCraft. That's funny. So they seem to be pretty balanced.
*  I wonder if the AI, the work that you're doing with AlphaStar would help balance them even further.
*  Is that something you think about? Is that something that Blizzard is thinking about?
*  Right. So balancing when you add a new unit or a new spell type is obviously possible,
*  given that you can always train or pre-train at scale some agent that might start using that in
*  unintended ways. But I think actually, if you understand how StarCraft has kind of co-evolved
*  with players, in a way, I think it's actually very cool the ways that many of the things and strategies
*  that people came up with. So I think we've seen it over and over in StarCraft that Blizzard comes up
*  with maybe a new unit and then some players get creative and do something kind of unintentional
*  or something that Blizzard designers just simply didn't test or think about. And then after that
*  becomes kind of mainstream in the community, Blizzard patches the game and then they kind of
*  maybe weaken that strategy or make it actually more interesting but a bit more balanced.
*  So this kind of continual talk between players and Blizzard is kind of what has defined them actually
*  in actually most games. In StarCraft but also in World of Warcraft, they would do that. There are
*  several classes and it would be not good that everyone plays absolutely the same race and so on.
*  I think they do care about balancing, of course, and they do a fair amount of testing, but it's
*  also beautiful to also see how players get creative anyways. And whether AI can be more creative at
*  this point, I don't think so. Sometimes something so amazing happens. I remember back in the days
*  like you have these drop ships that could drop the rivers and that was actually not thought about,
*  that you could drop this unit that has this what's called splash damage that would basically
*  eliminate all the enemies workers at once. No one thought that you could actually put them in a
*  really early game, do that kind of damage and then things change in the game. But I don't know,
*  I think it's quite an amazing exploration process from both sides, players and Blizzard alike.
*  Well, it's almost like a reinforcement learning exploration, but the scale of humans that play
*  Blizzard games is almost on the scale of a large scale deep mind RL experiment. I mean,
*  if you look at the numbers, you're talking about I don't know how many games, but hundreds of
*  thousands of games probably a month. Yeah, I mean, so that you could, it's almost the same as running
*  RL agents. What aspect of the problem of Starcraft you think is the hardest? Is it the,
*  like you said, the imperfect information? Is it the fact they have to do long term planning? Is it
*  the real time aspects? We have to do stuff really quickly. Is it the fact that large action space,
*  so you can do so many possible things? Or is it, you know, in the game theoretic sense,
*  there's no Nash equilibrium, or at least you don't know what the optimal strategy is, because
*  there's way too many options. Right. What's, is there something that stands out as just like
*  the hardest, the most annoying thing? So when we sort of looked at the problem and start to define
*  the parameters of it, right? What are the observations? What are the actions? It became
*  very apparent that, you know, the very first barrier that one would hit in Starcraft would be
*  because of the action space being so large and as not being able to search like you could in chess
*  or go, even though the search space is vast. The main problem that we identified was that of
*  exploration, right? So without any sort of human knowledge or human prior, if you think about
*  Starcraft and you know how deep reinforcement learning algorithm works, which is essentially
*  by issuing random actions and hoping that they will get some wins sometimes so they could learn.
*  So if you think of the action space in Starcraft, almost anything you can do in the early game is
*  bad, because any action involves taking workers, which are mining minerals for free. That's
*  something that the game does automatically sends them to mine. And you would immediately just
*  take them out of mining and send them around. So just thinking how is it going to be possible to
*  understand these concepts, but even more like expanding, right? There's these buildings you
*  can place in other locations in the map to gather more resources, but the location of the building
*  is important. And you have to select a worker, send it walking to that location, build the building,
*  wait for the building to be built, and then put extra workers there so they start mining.
*  That feels impossible if you just randomly click to produce that desirable state that then you
*  could hope to learn from, because eventually that may yield to an extra win, right? So for me,
*  the exploration problem and due to the action space and the fact that there's not really turns,
*  there's so many turns because the game essentially ticks at 22 times per second.
*  That's how they discretize time. Obviously, you always have to discretize time. There's
*  no such thing as real time, but it's really a lot of time steps of things that could go wrong.
*  And that definitely felt a priori like the hardest. You mentioned many good ones. I think partial
*  observability, the fact that there is no perfect strategy because of the partial observability.
*  Those are very interesting problems. We start seeing more and more now in terms of as we solve
*  the previous ones, but the core problem to me was exploration and solving it has been basically
*  kind of the focus and how we saw the first breakthroughs. So exploration in a multi
*  hierarchical way. So like 22 times a second exploration has a very different meaning than
*  it does in terms of should I gather resources early or should I wait or so on? So how do you
*  solve the long-term? Let's talk about the internals of AlphaStar. First of all, how do you
*  represent the state of the game as an input? How do you then do the long-term sequence modeling?
*  How do you build a policy? What's the architecture like? AlphaStar has obviously several components,
*  but everything passes through what we call the policy, which is a neural network. That's kind
*  of the beauty of it. There is, I could just now give you a neural network and some weights.
*  And if you fed the right observations and you understood the actions the same way we do,
*  you would have basically the agent playing the game. There's absolutely nothing else needed other
*  than those weights that were trained. Now, the first step is observing the game. And we've
*  experimented with a few alternatives. The one that we currently use mixes both spatial sort of images
*  that you would process from the game, that is the zoomed out version of the map and also a zoomed
*  in version of the camera or the screen as we call it. But also we give to the agent the list of units
*  that it sees, more of as a set of objects that it can operate on. That is not necessarily required
*  to use it. And we have versions of the game that play well without this set vision that is a bit
*  not like how humans perceive the game. But it certainly helps a lot because it's a very natural
*  way to encode the game is by just looking at all the units that they have properties like health,
*  position, type of unit, whether it's my unit or the enemy's. And that's sort of is kind of the
*  summary of the state of the game, that list of units or set of units that you see all the time.
*  But that's pretty close to the way humans see the game. Why do you say it's not,
*  is not, you're saying the exactness of it is not similar to humans?
*  The exactness of it is perhaps not the problem. I guess maybe the problem if you look at it from
*  how actually humans play the game is that they play with a mouse and a keyboard and a screen.
*  And they don't see sort of a structured object with all the units. What they see is what they see on
*  the screen, right? So remember that there's a, sorry to interrupt, there's a plot that you showed
*  with camera based where you do exactly that, right? You move around and that seems to
*  converge to similar performance. Yeah, I think that's what we're kind of experimenting with
*  what's necessary or not, but using the set. So actually if you look at research in computer
*  vision, where it makes a lot of sense to treat images as two dimensional arrays, there's actually
*  a very nice paper from Facebook. I think I forgot who the authors are, but I think it's part of
*  K-Mink's group. And what they do is they take an image, which is this two dimensional signal,
*  and they actually take pixel by pixel and scramble the image as if it was just a list of pixels.
*  Crucially, they encode the position of the pixels with the XY coordinates. And this is just kind of
*  a new architecture, which we incidentally also use in StarCraft called the transformer, which is a
*  very popular paper from last year, which yielded very nice result in machine translation.
*  And if you actually believe in this kind of, oh, it's actually a set of pixels, as long as you encode
*  XY, it's okay. Then you could argue that the list of units that we see is precisely that, because
*  we have each unit as a kind of pixel, if you will, and then their XY coordinates. So in that
*  perspective, without knowing it, we use the same architecture that was shown to work very well on
*  Pascal and ImageNet and so on. So the interesting thing here is putting it in that way, it starts
*  to move it towards the way you usually work with language. So what, and especially with your
*  expertise and work in language, it seems like there's echoes of a lot of the way you would
*  work with natural language in the way you've approached AlphaStar. Right. Does that help with
*  the long-term sequence modeling there somehow? Exactly. So now that we understand what an
*  observation for a given time step is, we need to move on to say, well, there's going to be a
*  sequence of such observations and an agent will need to, given all that it's seen, not only the
*  current time step, but all that it's seen, why? Because there is partial observability. We must
*  remember whether we saw a worker going somewhere, for instance, right? Because then there might be
*  an expansion on the top right of the map. So given that, what you must then think about is,
*  there is the problem of given all the observations, you have to predict the next action.
*  And not only given all the observations, but given all the observations and given all the
*  actions you've taken, predict the next action. And that sounds exactly like machine translation,
*  where, and that's exactly how kind of I saw the problem, especially when you are given supervised
*  data or replaced from humans, because the problem is exactly the same. You're translating essentially
*  a prefix of observations and actions onto what's going to happen next, which is exactly how you
*  would train a model to translate or to generate language as well. You have a certain prefix,
*  you must remember everything that comes in the past because otherwise you might start having
*  non-coherent text. And the same architectures, we're using LSTMs and transformers to operate
*  across time to kind of integrate all that's happened in the past. Those architectures that
*  work so well in translation or language modeling are exactly the same than what the agent is using
*  to issue actions in the game. And the way we train it, moreover, for imitation, which is step one of
*  AlphaStar, is take all the human experience and try to imitate it, much like you try to imitate
*  translators that translated many pairs of sentences from French to English, say,
*  that sort of principle applies exactly the same. It's almost the same code, except that instead of
*  words, you have slightly more complicated objects, which are the observations and the actions are
*  also a bit more complicated than a word. Is there a self-play component then too? So once you run
*  out of imitation? Right. So indeed, you can bootstrap from human replays, but then the agents you get
*  are actually not as good as the humans you imitated. So how do we imitate? Well, we take
*  humans from 3000 MMR and higher. 3000 MMR is just a metric of human skill. And 3000 MMR might be
*  like 50 percent percentile. So it's just kind of average human. So maybe quick pause. MMR is a
*  ranking scale, the matchmaking rating for players. So remember, there's like a master and a grand
*  master. What's 3000? So 3000 is pretty bad. I think it's kind of gold level. It just sounds
*  really good relative to chess, I think. Oh, yeah. The ratings, the best in the world are at 7000.
*  So 3000, it's a bit like Elo indeed. So 3500 just allows us to not filter a lot of the data.
*  So we like to have a lot of data in deep learning, as you probably know. So we take these kind of
*  3500 and above. But then we do a very interesting trick, which is we tell the neural network
*  what level they are imitating. So we say this replay you're going to try to imitate to predict
*  the next action for all the actions that you're going to see is a 4000 MMR replay. This one is a
*  6000 MMR replay. And what's cool about this is then we take this policy that is being trained
*  from human and then we can ask it to play like a 3000 MMR player by setting a bit saying, well,
*  okay, play like a 3000 MMR player or play like a 6000 MMR player. And you actually see how the
*  policy behaves differently. It gets worse economy if you play like a gold level player. It does less
*  actions per minute, which is the number of clicks or number of actions that you will issue in a whole
*  minute. And it's very interesting to see that it kind of imitates the skill level quite well.
*  But if we ask it to play like a 6000 MMR player, we tested, of course, these policies to see how
*  well they do. They actually beat all the built-in AIs that Blizzard put in the game, but they're
*  nowhere near 6000 MMR players. They might be maybe around gold level, platinum, perhaps.
*  So there's still a lot of work to be done for the policy to truly understand what it means to win.
*  So far, we only ask them, okay, here is the screen. And that's what happened on the game
*  until this point. What would the next action be if we ask a pro to now say, oh, you're going to
*  click here or here or there? And the point is experiencing wins and losses is very important
*  to then start to refine. Otherwise, the policy can get loose, can just go off policy as we call it.
*  That's so interesting that you can at least hope eventually to be able to control a policy
*  approximately to be at some MMR level. That's so interesting, especially given that you have
*  ground truth for a lot of these cases. Can I ask you a personal question? What's your MMR?
*  Well, I haven't played Starcraft 2, so I am unranked, which is the kind of lowest league.
*  Okay. So I used to play Starcraft, the first one. But you haven't seriously played Starcraft 2.
*  So the best player we have a deep mind is about 5000 MMR, which is high masters. It's not at
*  grand master level. Grand master level will be the top 200 players in a certain region like Europe
*  or America or Asia. But for me, it would be hard to say. I am very bad at the game. I actually played
*  Alpha Star a bit too late and it beat me. I remember the whole team was, oh, Oriol, you should play.
*  I was, oh, it looks like it's not so good yet. Then I remember I kind of got busy and waited an extra
*  week and I played and it really beat me very badly. How did that feel? Isn't that an amazing
*  feeling? That's amazing. Yeah. I mean, obviously I tried my best and I tried to also impress my
*  because I actually played the first game. So I'm still pretty good at micromanagement.
*  The problem is I just don't understand Starcraft 2. I understand Starcraft.
*  And when I played Starcraft, I probably was consistently like for a couple of years top 32
*  in Europe. So I was decent, but at the time we didn't have this kind of MMR system as well
*  established. So it would be hard to know what it was back then. So what's the difference in
*  interface between Alpha Star and Starcraft and a human player in Starcraft? Is there any
*  significant differences between the way they both see the game? I would say the way they see the
*  game, there's a few things that are just very hard to simulate. The main one perhaps, which
*  is obvious in hindsight is what's called cloaked units, which are invisible units.
*  So in Starcraft, you can make some units that you need to have a particular kind of unit to detect
*  it. So these units are invisible. If you cannot detect them, you cannot target them. So they would
*  just destroy your buildings or kill your workers. But despite the fact you cannot target the unit,
*  there's a shimmer that as a human you observe. I mean, you need to train a little bit. You need
*  to pay attention, but you would see this kind of space-time distortion and you would know, okay,
*  there are... Yeah, there's like a wave thing. Yeah, it's called shimmer. Space-time distortion.
*  That's really like the blizzard term is shimmer. And so this shimmer, professional players actually
*  can see it immediately. They understand it very well, but it's still something that requires
*  certain amount of attention and it's kind of a bit annoying to deal with. Whereas for Alpha Star,
*  in terms of vision, it's very hard for us to simulate sort of, oh, are you looking at this
*  pixel in the screen and so on. So the only thing we can do is there is a unit that's invisible over
*  there. So Alpha Star would know that immediately. Obviously, it still obeys the rules. You cannot
*  attack the unit. You must have a detector and so on. But it's kind of one of the main things that
*  it just doesn't feel there's a very proper way. I mean, you could imagine, oh, you don't have
*  hypers. Maybe you don't know exactly where it is or sometimes you see it, sometimes you don't.
*  But it's just really, really complicated to get it so that everyone would agree, oh, that's the
*  best way to simulate this. It seems like a perception problem. It is a perception problem.
*  So the only problem is people, you ask, oh, what's the difference between how humans perceive the
*  game? I would say they wouldn't be able to tell a shimmer immediately as it appears on the screen.
*  Whereas Alpha Star, in principle, sees it very sharply. It sees that the bit turned from zero
*  to one, meaning there's now a unit there, although you don't know the unit or you know that you
*  cannot attack it and so on. So from a vision standpoint, that probably is the one that
*  is kind of the most obvious one. Then there are things humans cannot do perfectly, even professionals,
*  which is they might miss a detail or they might have not seen a unit. And obviously, as a computer,
*  if there's a corner of the screen that turns green because a unit enters the field of view,
*  that can go into the memory of the agent, the LSTM, and persists there for a while and for
*  however long is relevant. And in terms of action, it seems like the rate of action from Alpha Star
*  is comparative, if not slower than professional players, but it's more precise.
*  So that's really probably the one that is causing us more issues for a couple of reasons. The first
*  one is StarCraft has been an AI environment for quite a few years. In fact, I was participating
*  in the very first competition back in 2010. And there's really not been a very clear set of rules
*  how the actions per minute, the rate of actions that you can issue is. And as a result, these
*  agents or bots that people build in a kind of almost very cool way, they do like 20,000,
*  40,000 actions per minute. Now, to put this in perspective, a very good professional human
*  might do 300 to 800 actions per minute. They might not be as precise. That's why the range is a bit
*  tricky to identify exactly. I mean, 300 actions per minute precisely is probably realistic.
*  800 is probably not, but you see humans doing a lot of actions because they warm up and they kind
*  of select things and spam and so on just so that when they need, they have the accuracy.
*  So we came into this by not having kind of a standard way to say, well, how do we measure
*  whether an agent is at human level or not? On the other hand, we had a huge advantage, which is
*  because we do imitation learning, agents turn out to act like humans in terms of rate of actions,
*  even precisions and imprecisions of actions in the supervised policy. You could see all these.
*  You could see how agents like to spam click to move here. If you played especially Diablo,
*  you wouldn't know what I mean. I mean, you just like spam, oh, I move here, move here, move here.
*  You're doing literally like maybe five actions in two seconds, but these actions are not very
*  meaningful. One would have sufficed. So on the one hand, we start from this imitation policy that
*  is at the ballpark of the actions per minutes of humans because it's actually statistically
*  trying to imitate humans. So we see this very nicely in the curves that we showed in the
*  blog post. Like there's these actions per minute and the distribution looks very human-like.
*  But then, of course, as self-play kicks in, and that's the part we haven't talked too much yet,
*  but of course the agent must play against itself to improve, then there's almost no guarantees
*  that these actions will not become more precise or even the rate of actions is going to increase
*  over time. So what we did, and this is probably kind of the first attempt that we thought was
*  reasonable, is we looked at the distribution of actions for humans for certain windows of time.
*  And just to give a perspective, because I guess I mentioned that some of these agents that are
*  programmatic, let's call them, they do 40,000 actions per minute. Professionals, as I said,
*  do 300 to 800. So what we looked at is we looked at the distribution over professional gamers,
*  and we took reasonably high actions per minute, but we kind of identified certain cutoffs,
*  after which, even if the agent wanted to act, these actions would be dropped.
*  But the problem is this cutoff is probably set a bit too high, and what ends up happening,
*  even though the games and when we ask the professionals and the gamers, by and large,
*  they feel like it's playing human-like. There are some agents that developed
*  maybe slightly too high APMs, which is actions per minute, combined with the precision,
*  which made people sort of start discussing a very interesting issue, which is should we have limited
*  this? Should we just let it lose and see what cool things it can come up with? Right?
*  Interesting.
*  So this is in itself an extremely interesting question, but the same way that modeling the
*  shimmer would be so difficult, modeling absolutely all the details about muscles and precision and
*  tiredness of humans would be quite difficult. So we're really here in kind of innovating in
*  this sense of, okay, what could be maybe the next iteration of putting more rules that makes the
*  agents more human-like in terms of restrictions? So yeah, putting constraints that
*  more constraints. Yeah, that's really interesting. That's really innovative. So one of the constraints
*  you put on yourself or at least focused in is on the Protoss race, as far as I understand.
*  Can you tell me about the different races and how they, so Protoss, Terran and Zerg,
*  how do they compare? How do they interact? Why did you choose Protoss?
*  Right.
*  Yeah, in the dynamics of the game seen from a strategic perspective.
*  So Protoss, so in StarCraft, there are three races. Indeed, in the demonstration, we saw
*  only the Protoss race. So maybe let's start with that one. Protoss is kind of the most technologically
*  advanced race. It has units that are expensive, but powerful, right? So in general, you want to
*  kind of conserve your units as you go attack. So you want to, and then you want to utilize
*  these tactical advantages of very fancy spells and so on and so forth. And at the same time,
*  people say they're a bit easier to play perhaps, right? But that I actually didn't know. I mean,
*  I just talk to now a lot to the players that we work with, TLO and Mana, and they said,
*  oh yeah, Protoss is actually, people think is actually one of the easiest races. So perhaps
*  the easier, that doesn't mean that it's, you know, obviously professional players
*  excel at the three races and there's never like a race that dominates for a very long time anyway.
*  So if you look at the top, I don't know, 100 in the world, is there one race that dominates that
*  list?
*  It would be hard to know because it depends on the regions. I think it's pretty equal in terms of
*  distribution and Blizzard wants it to be equal, right? They wouldn't want one race like Protoss
*  to not be representative in the top place. So definitely like they tried it to be like
*  balanced, right? So then maybe the opposite race of Protoss is Zerg. Zerg is a race where you just
*  kind of expand and take over as many resources as you can. And they have a very high capacity to
*  regenerate their units. So if you have an army, it's not that valuable in terms of losing the
*  whole army is not a big deal as Zerg because you can then rebuild it. And given that you generally
*  accumulate a huge bank of resources, Zergs typically play by applying a lot of pressure,
*  maybe losing their whole army, but then rebuilding it quickly. So although of course every race,
*  I mean, there's never, I mean, they're pretty diverse. I mean, there are some units in Zerg
*  that are technologically advanced and they do some very interesting spells. And there's some
*  units in Protoss that are less valuable and you could lose a lot of them and rebuild them and
*  it wouldn't be a big deal. All right. So maybe I'm missing out. Maybe I'm going to say some dumb
*  stuff, but a summary of strategy. So first there's collection of a lot of resources. That's one
*  option. The other one is expanding. So building other bases. Then the other is obviously attack,
*  building units and attacking with those units. And then I don't know what else there is. Maybe
*  there's the different timing of attacks, like do attack early, attack late. What are the different
*  strategies that emerged that you've learned about? I've read that a bunch of people are super happy
*  that you guys have apparently, that Alpha Star apparently has discovered that it's really good to,
*  what is it, saturate? Oh yeah, the mineral line. Yeah. Yeah. And that's for greedy,
*  amateur players like myself. That's always been a good strategy. You just build up a lot of money
*  and it just feels good to just accumulate and accumulate. So thank you for discovering that
*  validating all of us. But is there other strategies that you discovered interesting,
*  unique to this game? Yeah. So if you look at kind of not being a StarCraft II player, but of course,
*  StarCraft and StarCraft II and real time strategy games in general are very similar.
*  I would classify perhaps the openings of the game. They're very important. And generally,
*  I would say there's two kinds of openings. One that's a standard opening. That's generally
*  how players find sort of a balance between risk and economy and building some units early on so
*  that they could defend, but they're not too exposed basically, but also expanding quite quickly. So
*  this would be kind of a standard opening. And within a standard opening, then what you do
*  choose generally is what technology are you aiming towards? So there's a bit of rock, paper, scissors
*  of you could go for spaceships or you could go for invisible units or you could go for, I don't know,
*  like massive units that attack against certain kinds of units, but they're weak against others.
*  So standard openings themselves have some choices like rock, paper, scissors style. Of course,
*  if you scout and you're good at guessing what the opponent is doing, then you can play as an
*  advantage because if you know you're going to play rock, I mean, I'm going to play paper, obviously.
*  So you can imagine that normal standard games in StarCraft looks like a continuous rock, paper,
*  scissors game where you guess what the distribution of rock, paper, and scissors is from the enemy
*  and reacting accordingly to try to beat it or put the paper out before he kind of changes his
*  mind from rock to scissors and then you would be in a weak position. So sorry to pause on that. I
*  didn't realize this element because I know it's true with poker. I know I looked at Lebron.
*  You're also estimating trying to guess the distribution, trying to better and better
*  estimate the distribution of what the opponent is likely to be doing. Yeah. I mean, as a player,
*  you definitely want to have a belief state over what's up on the other side of the map.
*  And when your belief state becomes inaccurate, when you start having serious doubts whether he's
*  going to play something that you must know, that's when you scout. You want to then gather
*  information, right? Is improving the accuracy of the belief or improving the belief state part of
*  the loss that you're trying to optimize or is it just a side effect? It's implicit, but you could
*  explicitly model it and it would be quite good at probably predicting what's on the other side of
*  the map. But so far it's all implicit. There's no additional reward for predicting the enemy.
*  So there's these standard openings and then there's what people call cheese, which is very
*  interesting. And AlphaStar sometimes really likes this kind of cheese. These cheeses, what they are
*  is kind of an all-in strategy. You're going to do something sneaky. You're going to hide enemies,
*  hide your own buildings close to the enemy base, or you're going to go for hiding your technological
*  buildings so that you do invisible units and the enemy just cannot react to detect it and
*  thus lose the game. And there's quite a few of these cheeses and variants of them. And there
*  is where actually the belief state becomes even more important because if I scout your base and
*  I see no buildings at all, any human player knows something's up. They might know, well,
*  you're hiding something close to my base. Should I build suddenly a lot of units to defend? Should
*  I actually block my ramp with workers so that you cannot come and destroy my base? So all this is
*  happening and defending against cheeses is extremely important. And in the AlphaStar League,
*  many agents actually develop some cheesy strategies. And in the games we saw against TLO and Mana,
*  two out of the ten agents were actually doing these kind of strategies, which are
*  cheesy strategies. And then there's a variant of cheesy strategy, which is called all-in.
*  So an all-in strategy is not perhaps as drastic as, oh, I'm going to build cannons on your base and
*  then bring all my workers and try to just disrupt your base and game over, or GG, as we say in
*  StarCraft. There's these kind of very cool things that you can align precisely at a certain time
*  mark. So for instance, you can generate exactly 10 unit composition that is perfect, like five of
*  this type, five of this other type, and align the upgrade so that at four minutes and a half, let's
*  say, you have these 10 units and the upgrade just finished. And at that point, that army is really
*  scary. And unless the enemy really knows what's going on, if you push, you might then have an
*  advantage because maybe the enemy is doing something more standard. It expanded too much.
*  It developed too much economy and it trade off badly against having defenses and the enemy will
*  lose. But it's called all-in because if you don't win, then you're going to lose. So you see players
*  that do these kind of strategies. If they don't succeed, game is not over. I mean, they still have
*  a base and they still gathering minerals, but they will just GG out of the game because they know,
*  well, game is over. I gambled and I failed. So if we start entering the game theoretic aspects of
*  the game, it's really rich and it's really, that's why it also makes it quite entertaining to watch.
*  Even if I don't play, I still enjoy watching the game. But the agents are trying to do this
*  mostly implicitly. But one element that we improved in self-play is creating the Alpha Star League.
*  And the Alpha Star League is not pure self-play. It's trying to create different personalities of
*  agents so that some of them will become cheesy agents. Some of them might become very economical,
*  very greedy, like getting all the resources, but then being maybe early on, they're going to be
*  weak, but later on they're going to be very strong. And by creating this personality of agents, which
*  sometimes it just happens naturally that you can see kind of an evolution of agents that,
*  given the previous generation, they train against all of them and then they generate kind of the
*  perfect counter to that distribution. But these agents, you must have them in the populations
*  because if you don't have them, you're not covered against these things. You want to create all sorts
*  of the opponents that you will find in the wild so you can be exposed to these cheeses, early
*  aggression, later aggression, more expansions, dropping units in your base from the side,
*  all these things. And pure self-play is getting a bit stuck at finding some subset of these,
*  but not all of these. So the Alpha Star League is a way to kind of do an ensemble of agents
*  that they're all playing in a league much like people play on Battle.net. You play against
*  someone who does a new cool strategy and you immediately, oh my God, I want to try it. I want
*  to play again. And this to me was another critical part of the problem, which was,
*  can we create a Battle.net for agents? And that's kind of what the Alpha Star League really is.
*  Fascinating. And where they stick to their different strategies. Yeah, wow, that's really,
*  really interesting. But that said, you were fortunate enough or just skilled enough to
*  win 5-0. And so how hard is it to win? I mean, that's not the goal. I guess, I don't know what
*  the goal is. The goal should be to win majority, not 5-0. But how hard is it in general to win
*  all matchups and a 1v1? So that's a very interesting question because
*  once you see Alpha Star and superficially you think, well, okay, it won. Let's, if you sum up
*  the games like 10 to 1, it lost the game that it played with the camera interface. You might think,
*  well, that's done. It's superhuman at the game. And that's not really the claim we really can make,
*  actually. The claim is we beat a professional gamer for the first time. StarCraft has really been a
*  thing that has been going on for a few years, but a moment like this had not occurred before yet.
*  But are these agents impossible to beat? Absolutely not. So that's a bit what's
*  the difference is the agents play at Grandmaster level. They definitely understand the game enough
*  to play extremely well. But are they unbeatable? Do they play perfect? No. And actually in StarCraft,
*  because of these sneaky strategies, it's always possible that you might take a huge risk sometimes,
*  but you might get wins out of this. So I think that as a domain, it still has a lot of opportunities,
*  not only because of course we want to learn with less experience. If I learn to play Protoss,
*  I can play Terran and learn it much quicker than Alpha Star can. So there are obvious interesting
*  research challenges as well. But even as the raw performance goes, really the claim here can be we
*  are at pro level or at high Grandmaster level. But obviously the players also did not know what to
*  expect. Their prior distribution was a bit off because they played this kind of new alien brain,
*  as they like to say. And that's what makes it exciting for them. But also I think if you look
*  at the games closely, you see there were weaknesses in some points. Maybe Alpha Star did not scout,
*  or if it had invisible units going against at certain points, it wouldn't have known and it
*  would have been bad. So there's still quite a lot of work to do. But it's really a very exciting
*  moment for us to be seeing, wow, a single neural net on a GPU is actually playing against these guys
*  who are amazing. I mean, you have to see them play in life. They're really, really amazing players.
*  Yeah, I'm sure there must be a guy in Poland somewhere right now training his butt off
*  to make sure that this never happens again with Alpha Star. So that's really exciting
*  in terms of Alpha Star having some holes to exploit, which is great. And then you build on
*  top of each other. And it feels like StarCraft, unlike Go, even if you win, it's still not,
*  it's still not, there's so many different dimensions in which you can explore. So that's
*  really, really interesting. Do you think there's a ceiling to Alpha Star? You've said that it hasn't
*  reached, you know, this is a big, wait, let me actually just pause for a second. How did it feel
*  to come here to this point, to beat a top professional player? Like that night, I mean,
*  you know, Olympic athletes have their gold medal, right? This is your gold medal in a sense.
*  Sure, you're cited a lot, you've published a lot of prestigious papers, whatever, but this is like
*  a win. How did it feel? I mean, it was for me, it was unbelievable. Because first, the win itself,
*  I mean, it was so exciting. I mean, so looking back to those last days of 2018, really, that's
*  when the games were played. I'm sure I look back at that moment, I say, Oh, my God, I want to be
*  like in a project like that. It's like, I already feel the nostalgia of like, yeah, that was huge
*  in terms of the energy and the team effort that went into it. And so in that sense, as soon as it
*  happened, I already knew it was kind of, I was losing it a little bit. So it is almost like sad
*  that it happened and oh my God, like, but on the other hand, it also verifies the approach. But to
*  me also, there's so many challenges and interesting aspects of intelligence that even though we can
*  train a neural network to play at the level of the best humans, there's still so many challenges.
*  So for me, it's also like, well, this is really an amazing achievement. But I already was also
*  thinking about next steps. I mean, as I said, these agents play Protoss versus Protoss, but
*  they should be able to play a different race much quicker, right? So that would be an amazing
*  achievement. Some people call these meta reinforcement learning, meta learning, and so on.
*  So there's so many possibilities after that moment, but the moment itself, it really felt great.
*  We had these bets. So I'm kind of a pessimist in general. So I kind of sent an email to the team.
*  I said, okay, let's against TLO first, right? Like, what's going to be the result? And I really
*  thought we would lose like 5-0, right? We had some calibration made against the 5,000 MMR player.
*  TLO was much stronger than that player, even if he played Protoss, which is his off-race.
*  But yeah, I was not imagining we would win. So for me, that was just kind of a test run or something.
*  And then he was really surprised. And unbelievably, we went to this
*  bar to celebrate. And Dave tells me, well, why don't we invite someone who is a thousand MMR
*  stronger in Protoss, like an actual Protoss player, like that it turned up being Mana, right?
*  And we had some drinks and I said, sure, why not? But then I thought, well, that's really going to
*  be impossible to beat. I mean, because it's so much ahead. A thousand MMR is really like 99%
*  probability that Mana would beat TLO as Protoss versus Protoss, right? So we did that. And to me,
*  the second game was much more important, even though a lot of uncertainty kind of disappeared
*  after we beat TLO. I mean, he is a professional player. So that was kind of, oh, but that's
*  really a very nice achievement. But Mana really was at the top and you could see he played much
*  better. But our agents got much better too. And then after the first game, I said, if we take a
*  single game, at least we can say we beat a game. I mean, even if we don't beat the series, for me,
*  that was a huge relief. And I mean, I remember the hacking dummies and I mean, it was really like
*  this moment for me will resonate forever as a researcher and I mean, as a person. And yeah,
*  it's a really great accomplishment. And it was great also to be there with the team in the room.
*  I don't know if you saw like, so it was really like-
*  I mean, from my perspective, the other interesting thing is just like watching Kasparov,
*  watching Mana was also interesting because he is kind of a loss of words. I mean, whenever you lose,
*  I've done a lot of sports. You sometimes say excuses, you look for reasons, and he couldn't
*  really come up with reasons. So with the off race for Protoss, you could say, well, it felt awkward,
*  it wasn't, but here it was just beaten. And it was beautiful to look at a human being being
*  superseded by an AI system. I mean, it's a beautiful moment for researchers. So yeah,
*  for sure. It was, I mean, probably the highlight of my career so far, because of its uniqueness
*  and coolness. And I don't know, I mean, it's obviously, as you said, you can look at paper
*  citations and so on. But this really is like a testament of the whole machine learning approach.
*  And using games to advance technology. I mean, it really was, everything came together at that
*  moment. That's really the summary. Also on the other side, it's a popularization of AI too,
*  because just like traveling to the moon and so on. I mean, this is where a very large community
*  of people that don't really know AI, they get to really interact with it. Which is very important.
*  I mean, it's extremely important. We must, you know, writing papers helps our peers,
*  researchers to understand what we're doing. But I think AI is becoming mature enough that we must
*  try to explain what it is. And perhaps through games is an obvious way because these games
*  always had built in AI. So it may be everyone experience an AI playing a video game, even if
*  they don't know, because there's always some scripted element. And some people might even
*  call that AI already, right? So what are other applications of the approaches underlying Alpha
*  Star that you see happening? There's a lot of echoes of, you said, transformer of language
*  modeling and so on. Have you already started thinking where the breakthroughs in Alpha Star
*  get expanded to other applications? Right. So I thought about a few things for like,
*  kind of next month, next year. The main thing I'm thinking about actually is what's next
*  as a kind of a grand challenge. Because for me, like we've seen Atari and then there's like the
*  sort of three dimensional worlds that we've seen also like pretty good performance from this Capture
*  the Flag agents that also some people at DeepMind and elsewhere are working on. We've also seen some
*  amazing results on like, for instance, Dota 2, which is also a very complicated game. So for me,
*  like the main thing I'm thinking about is what's next in terms of challenge. So as a researcher,
*  I see sort of two tensions between research and then applications or areas or domains where you
*  apply them. So on the one hand, we've done thanks to the application of StarCraft is very hard.
*  We developed some techniques, some new research that now we could look at elsewhere. Like are there
*  other applications where we can apply these? And the obvious ones, absolutely. You can think of
*  feeding back to sort of the community we took from, which was mostly sequence modeling or natural
*  language processing. So we've developed and extended things from the transformer and we
*  use pointer networks. We combine LSTM and transformers in interesting ways. So that's perhaps
*  the kind of lowest hanging fruit of feeding back to now a different field of machine learning
*  that's not playing video games. Let me go old school and jump to the
*  to Mr. Alan Turing. So the Turing test, you know, it's a natural language test, a conversational test.
*  What's your thought of it as a test for intelligence? Do you think it is a grand
*  challenge that's worthy of undertaking? Maybe if it is, would you reformulate it or phrase it somehow
*  differently? Right. So I really love the Turing test because I also like sequences and language
*  understanding. And in fact, some of the early work we did in machine translation, we tried to
*  apply to kind of a neural chatbot, which obviously would never pass the Turing test because it was
*  very limited. But it is a very fascinating idea that you could really have an AI that would be
*  indistinguishable from humans in terms of asking or conversing with it, right? So I think it's
*  conversing with it, right? So I think the test itself seems very nice and it's kind of well
*  defined actually, like the passing it or not. I think there's quite a few rules that feel like
*  pretty simple and you could really like have, I mean, I think they have these competitions every
*  year. Yeah, so the Leibnir Prize, but I don't know if you've seen, I don't know if you've seen the
*  kind of bots that emerge from that competition. They're not quite as what you would, so it feels
*  like that there's weaknesses with the way Turing formulated it. It needs to be that the definition
*  of a genuine, rich, fulfilling human conversation needs to be something else. Like the Alexa Prize,
*  which I'm not as well familiar with, has tried to define that more, I think by saying you have to
*  continue keeping a conversation for 30 minutes, something like that. So basically forcing the
*  agent not to just fool, but to have an engaging conversation kind of thing. Is that, I mean,
*  have you thought about this problem richly? And if you have in general, how far away are we from,
*  you worked a lot on language understanding, language generation, but the full dialogue,
*  the conversation, just sitting at the bar, having a couple of beers for an hour,
*  that kind of conversation, have you thought about it? Yeah, so I think you touched here on
*  the critical point, which is feasibility, right? So there's a great sort of essay by Hamming,
*  which describes sort of grand challenges of physics. And he argues that, well, okay, for instance,
*  teleportation or time travel are great grand challenges of physics, but there's no attacks.
*  We really don't know or cannot kind of make any progress. So that's why most physicists and so on,
*  they don't work on these in their PhDs and as part of their careers. So I see the Turing test as in
*  in the full Turing test as a bit still too early. Like I am, I think we're, especially with the
*  current trend of deep learning language models, we've seen some amazing examples, I think GPT-2
*  being the most recent one, which is very impressive, but to understand to fully solve passing or fooling
*  a human to think that there's a human on the other side, I think we're quite far. So as a result,
*  I don't see myself and I probably would not recommend people doing a PhD on solving the
*  Turing test because it just feels it's kind of too early or too hard of a problem.
*  Yeah, but that said, you said the exact same thing about StarCraft about a few years ago.
*  Indeed.
*  So to Demis, so you'll probably also be the person who passes the Turing test in three years.
*  I mean, I think that, yeah, so.
*  So we have this on record. This is nice.
*  It's true. It's true. I mean, it's true that progress sometimes is a bit unpredictable.
*  I really wouldn't have not, even six months ago, I would not have predicted the level that we see
*  that these agents can deliver at Grandmaster level. But I have worked on language enough.
*  And basically, my concern is not that something could happen, a breakthrough could happen that
*  would bring us to solving or passing the Turing test, is that I just think the statistical
*  approach to it, like this, it's not going to cut it. So we need a breakthrough, which is great for
*  the community. But given that, I think there's quite more uncertainty. Whereas for StarCraft,
*  I knew what the steps would be to kind of get us there. I think it was clear that using the
*  imitation learning part and then using these battle net for agents were going to be key.
*  And it turned out that this was the case and a little more was needed, but not much more.
*  For Turing test, I just don't know what the plan or execution plan would look like.
*  So that's why I myself working on it as a grand challenge is hard. But there are quite a few
*  sub challenges that are related that you could say, well, I mean, what if you create a great
*  assistant, like Google already has like the Google Assistant? So can we make it better? And can we
*  make it fully neural and so on that I start to believe maybe we're reaching a point where we
*  should attempt these challenges. I like this conversation so much because it echoes very
*  much the StarCraft conversation. It's exactly how you approach StarCraft. Let's break it down into
*  small pieces and solve those and you end up solving the whole game. Great. But that said,
*  you're behind some of the sort of biggest pieces of work in deep learning in the last several years.
*  So you mentioned some limits. What do you think are the current limits of deep learning?
*  And how do we overcome those limits? So if I had to actually use a single word to define
*  the main challenge in deep learning is a challenge that probably has been the challenge for many
*  years and is that of generalization. So what that means is that all that we're doing is fitting
*  functions to data. And when the data we see is not from the same distribution, or even if there are
*  sometimes that it is very close to distribution, but because of the way we train it with limited
*  samples, we then get to this stage where we just don't see generalization as much as we
*  can generalize. And I think adversarial examples are a clear example of this. But
*  if you study machine learning and literature and the reason why SVMs came very popular
*  were because they were dealing and they had some guarantees about generalization, which is
*  unseen data or out of distribution, or even within distribution where you take an image
*  adding a bit of noise, these models fail. So I think really, I don't see a lot of progress
*  on generalization in the strong generalization sense of the word. I think our neural networks,
*  you can always find design examples that will make their outputs arbitrary, which is not good
*  because we humans would never be fooled by these kind of images or manipulation of the image.
*  And if you look at the mathematics, you kind of understand this is a bunch of matrices multiplied
*  together. There's probably numerics and instability that you can just find corner cases. So I think
*  that's really the underlying topic many times we see when even at the grand stage of like
*  Turing tests, generalization, if you start passing the Turing test, should it be in English
*  or should it be in any language? As a human, if you ask something in a different language,
*  you actually will go and do some research and try to translate it and so on. Should the Turing test
*  include that? And it's really a difficult problem and very fascinating and very mysterious actually.
*  Yeah, absolutely. But do you think if you were to try to solve it,
*  can you not grow the size of data intelligently in such a way that the distribution of your
*  training set does include the entirety of the testing set? Is that one path? The other path is
*  totally a new methodology. It's not statistical. So a path that has worked well and it worked well
*  in StarCraft and in machine translation and in languages, scaling up the data and the model.
*  And that's kind of been maybe the only single formula that still delivers today in deep learning.
*  Right? It's that scale, data scale and model scale really do more and more of the things that we
*  thought, oh, there's no way it can generalize to these or there's no way it can generalize to that.
*  But I don't think fundamentally it will be solved with these. And for instance, I'm really liking
*  some style or approach that would not only have neural networks, but it would have programs or
*  some discrete decision making because there is where I feel there's a bit more like, I mean,
*  the example of the best example, I think, for understanding this is I also worked a bit on,
*  oh, like we can learn an algorithm with a neural network. Right? So you give it many examples and
*  it's going to sort the input numbers or something like that. But really, strong generalization
*  is you give me some numbers or you ask me to create an algorithm that sorts numbers and instead
*  of creating a neural net, which will be fragile because it's going to go out of range at some
*  point, you're going to give it numbers that are too large, too small and whatnot. If you just create
*  a piece of code that sorts the numbers, then you can prove that that will generalize to absolutely
*  all the possible inputs you could give. So I think that's the problem comes with some exciting
*  prospects. I mean, scale is a bit more boring, but it really works. And then maybe programs and
*  discrete abstractions are a bit less developed, but clearly I think they're quite exciting in
*  terms of future for the field. Do you draw any insight wisdom from the 80s and expert systems
*  and symbolic systems, symbolic computing? Do you ever go back to those, the reasoning, that kind of
*  logic? Do you think that might make a comeback? You'll have to dust off those books.
*  Yeah, I actually love actually adding more inductive biases. To me, the problem really is
*  what are you trying to solve? If what you're trying to solve is so important that try to solve it no
*  matter what, then absolutely use rules, use domain knowledge, and then use a bit of the magic of
*  machine learning to empower, to make the system as the best system that will detect cancer or
*  detect weather patterns. Or in terms of StarCraft, it also was a very big challenge. So
*  I was definitely happy that if we had to cut a corner here and there, it could have been
*  interesting to do. And in fact, in StarCraft, we start thinking about expert systems because
*  it's a very, you know, you can define, I mean, people actually build StarCraft bots by thinking
*  about those principles, like state machines and rule-based. And then you could think of combining
*  a bit of a rule-based system, but that has also neural networks incorporated to make it generalize
*  a bit better. So absolutely, I mean, we should definitely go back to those ideas and anything
*  that makes the problem simpler. As long as your problem is important, that's okay. And that's
*  research driving a very important problem. And on the other hand, if you want to really focus on the
*  limits of reinforcement learning, then of course, you must try not to look at imitation data or
*  to look for some rules of the domain that would help a lot or even feature engineering, right?
*  So this is a tension that depending on what you do, I think both ways are definitely fine. And
*  I would never not do one or the other if you're, as long as what you're doing is
*  important and needs to be solved, right? Right. So there's a bunch of different ideas that
*  you've developed that I really enjoy. But one is translating from image captioning, translating
*  from image to text. Just another beautiful idea, I think, that resonates throughout your work,
*  actually. So the underlying nature of reality being language always. Yeah, somehow. So what's
*  the connection between images and text, or rather the visual world and the world of language,
*  in your view? Right. So I think a piece of research that's been central to, I would say,
*  even extending into StarCraft is this idea of sequence to sequence learning, which what we
*  really meant by that is that you can now really input anything to a neural network as the input
*  X, and then the neural network will learn a function F that will take X as an input and
*  produce any output Y. And these X and Y don't need to be static or like a feature, like a
*  fixed vector or anything like that. It could be really sequences and now beyond data structures.
*  So that paradigm was tested in a very interesting way when we moved from translating
*  French to English to translating an image to its caption. But the beauty of it is that really,
*  and that's actually how it happened. I changed a line of code in this thing that was doing machine
*  translation, and I came the next day and I saw how it was producing captions that
*  seemed like, oh my God, this is really, really working. And the principle is the same. So I think
*  I don't see text, vision, speech, waveforms as something different.
*  As long as you basically learn a function that will vectorize these into, and then after we
*  vectorize it, we can then use transformers, LSTMs, whatever the flavor of the month of the model is,
*  and then as long as we have enough supervised data, really, this formula will work and will
*  keep working, I believe, to some extent, model of these generalization issues that I mentioned
*  before. But the task there is to vectorize, so to form a representation that's meaningful,
*  I think. And your intuition now, having worked with all this media, is that once you are able
*  to form that representation, you can basically take anything, any sequence. Is there, going back
*  to StarCraft, is there limits on the length? So we didn't really touch on the long term aspect.
*  How did you overcome the whole really long term aspect of things here? Is there some tricks?
*  The main trick, so StarCraft, if you look at absolutely every frame, you might think it's
*  quite a long game. So we would have to multiply 22 times 60 seconds per minute times maybe at
*  least 10 minutes per game on average. So there are quite a few frames, but the trick really was to
*  only observe, in fact, which might be seen as a limitation, but it is also a computational
*  advantage, only observe when you act. And then what the neural network decides is what is the gap
*  going to be until the next action. And if you look at most StarCraft games that we have in the
*  data set that Blizzard provided, it turns out that most games are actually only, I mean, it is
*  still a long sequence, but it's maybe like a thousand to 1500 actions, which if you start
*  looking at LSTMs, large LSTMs, transformers, it's not that difficult, especially if you have supervised
*  learning. If you had to do it with reinforcement learning, the credit assignment problem, what is
*  in this game that made you win? That would be really difficult. But thankfully, because of imitation
*  learning, we didn't kind of have to deal with this directly. Although if we had to, we tried it. And
*  what happened is you just take all your workers and attack with them. And that sort of is kind
*  of obvious in retrospect, because you start trying random actions. One of the actions will be a worker
*  that goes to the enemy base. And because it's self-play, it's not going to know how to defend,
*  because it basically doesn't know almost anything. And eventually what you develop is this,
*  take our workers and attack. Because the credit assignment issue in our route is really, really
*  hard. I do believe we could do better. And that's maybe a research challenge for the future.
*  But yeah, even in StarCraft, the sequences are maybe a thousand, which I believe is within the
*  realm of what transformers can do. Yeah, I guess the difference between StarCraft and Go is
*  in Go and chess, stuff starts happening right away. So there's not... Yeah, it's pretty easy
*  through self-play. Not easy, but through self-play it's possible to develop reasonable strategies
*  quickly as opposed to StarCraft. I mean, in Go, there's only 400 actions. But one action
*  is what people would call the God action. That would be if you had expanded the whole search
*  tree, that's the best action if you did Minimax or whatever algorithm you would do if you had
*  the computational capacity. But in StarCraft, 400 is minuscule. In 400, you couldn't even click
*  on the pixels around a unit. So I think the problem there is in terms of action space size
*  is way harder. And that search is impossible. So there's quite a few challenges indeed that make
*  this kind of a step up in terms of machine learning. For humans, maybe playing StarCraft
*  seems more intuitive because it looks real. I mean, the graphics and everything moves smoothly.
*  Whereas I don't know how to... I mean, Go is a game that I wouldn't really need to study. It
*  feels quite complicated. But for machines, kind of maybe it's the reverse. Yes.
*  Which shows you the gap actually between deep learning and however the heck our brains work.
*  So you developed a lot of really interesting ideas. It's interesting to just ask, what's your
*  process of developing new ideas? Do you like brainstorming with others? Do you like thinking
*  alone? Do you like... like what was it? Ian Goodfellow said he came up with GANs after a few beers.
*  Right. He thinks beers are essential for coming up with new ideas.
*  We had beers to decide to play another game of StarCraft after a week. So
*  it's really similar to that story. Actually, I explained this in a DeepMind retreat and I said,
*  this is the same as the GAN story. I mean, we were in a bar and we decided let's play a game
*  next week and that's what happened. I feel like we're giving the wrong message to young
*  undergrads. Yeah, I know. But in general, do you like brainstorming? Do you like thinking alone,
*  working stuff out? So I think throughout the years also things changed, right? So initially I was
*  very fortunate to be with great minds like Jeff Hinton, Jeff Dean, Ilya Sudskiver. I was really
*  fortunate to join Brain at a very good time. So at that point, ideas, I was just kind of brainstorming
*  with my colleagues and learned a lot. And keep learning is actually something you should never
*  stop doing, right? So learning implies reading papers and also discussing ideas with others.
*  It's very hard at some point to not communicate that being reading a paper from someone or
*  actually discussing, right? So definitely that communication aspect needs to be there,
*  whether it's written or oral. Nowadays, I'm also trying to be a bit more strategic about
*  what research to do. So I was describing a little bit this sort of tension between
*  research for the sake of research, and then you have, on the other hand,
*  applications that can drive the research, right? And honestly, the formula that has worked best for
*  me is just find a hard problem and then try to see how research fits into it, how it doesn't fit into
*  it, and then you must innovate. So I think machine translation drove sequence to sequence. Then maybe
*  learning algorithms that had to, like combinatorial algorithms led to pointer networks.
*  Starcraft led to really scaling up imitation learning and the AlphaStar league. So that's
*  been a formula that I personally like. But the other one is also valid. And I've seen it succeed
*  a lot of the times where you just want to investigate model-based RL as a kind of a research
*  topic. And then you must then start to think, well, how are the tests? How are you going to
*  test these ideas? You need a minimal environment to try things. You need to read a lot of papers
*  and so on. And that's also very fun to do and something I've also done quite a few times,
*  both at Brain, at DeepMind, and obviously as a PhD. So I think besides the ideas and discussions,
*  I think it's important also because you start sort of guiding not only your own goals, but
*  other people's goals to the next breakthrough. So you must really kind of understand this
*  feasibility also as we were discussing before, right? Whether this domain is ready to be tackled
*  or not. And you don't want to be too early. You obviously don't want to be too late. So it's
*  really interesting. This strategic component of research, which I think as a grad student,
*  I just had no idea. I just read papers and discussed ideas. And I think this has been
*  maybe the major change. And I recommend people kind of feed forward to success, how it looks
*  like, and try to backtrack other than just kind of looking at, oh, this looks cool. This looks cool.
*  And then you do a bit of random work, which sometimes you stumble upon some interesting
*  things. But in general, it's also good to plan a bit. Yeah, I like it. Especially like your
*  approach of taking a really hard problem, stepping right in and then being super skeptical about
*  being able to solve the problem. I mean, there's a balance of both, right? There's a silly
*  optimism and a critical sort of skepticism that's good to balance, which is why it's good to have a
*  team of people that balance that. You don't do that on your own. You have both mentors that
*  have seen or you obviously want to chat and discuss whether it's the right time. I mean,
*  Demis came in 2014 and he said, maybe in a bit we'll do StarCraft and maybe he knew.
*  And I'm just following his lead, which is great because he's brilliant, right? So
*  these things are obviously quite important that you want to be surrounded by people who
*  are diverse. They have their knowledge. There's also important to... I mean, I've learned a lot
*  from people who actually have an idea that I might not think it's good, but if I give them
*  the space to try it, I've been proven wrong many, many times as well. So that's great.
*  Your colleagues are more important than yourself, I think.
*  Now, let's real quick talk about another impossible problem. AGI. What do you think it
*  takes to build a system that's human level intelligence? We talked a little bit about
*  the Turing test, StarCraft, all of these have echoes of general intelligence. But if you think
*  about just something that you would sit back and say, wow, this is really something that resembles
*  human level intelligence. What do you think it takes to build that?
*  I find that AGI oftentimes is maybe not very well defined. So what I'm trying to then come up with
*  for myself is what would be a result look like that you would start to believe that you would
*  have agents or neural nets that no longer sort of overfit to a single task, but actually
*  kind of learn the skill of learning, so to speak. And that actually is a field that I am fascinated
*  by, which is the learning to learn or meta learning, which is about no longer learning about a single
*  domain. So you can think about the learning algorithm itself is general. So the same formula
*  we applied for AlphaStar or StarCraft, we can now apply to kind of almost any video game, or you
*  could apply to many other problems and domains. But the algorithm is what's kind of generalizing.
*  But the neural network, those weights are useless even to play another race. I train a network to
*  play very well at Protoss versus Protoss. I need to throw away those weights. If I want to play
*  now Terran versus Terran, I would need to retrain a network from scratch with the same algorithm.
*  That's beautiful, but the network itself will not be useful. So I think if I see an approach
*  that can absorb or start solving new problems without the need to kind of restart the process,
*  I think that to me would be a nice way to define some form of AGI. Again, I don't know,
*  the grandiose, I mean, should Turing test be solved before AGI? I mean, I don't know. I think
*  concretely, I would like to see clearly that meta learning happen, meaning there is an architecture
*  or network that as it sees new problem or new data, it solves it. And to make it kind of a
*  benchmark, it should solve it at the same speed that we do solve new problems. When I define you
*  a new object and you have to recognize it, when you start playing a new game, you played all the
*  Atari games, but now you play a new Atari game, well, you're going to be pretty quickly pretty
*  good at the game. So that's perhaps what's the domain and what's the exact benchmark is a bit
*  difficult. I think as a community, we might need to do some work to define it. But I think this
*  first step, I could see it happen relatively soon. But then the whole what AGI means and so on,
*  I am a bit more confused about what I think people mean different things.
*  There's an emotional psychological level that like even the Turing test passing the Turing test is
*  something that we just pass judgment on as human beings, what it means to be, you know, is a dog
*  in AGI system. Yeah, like what level what does it mean? Right? Yeah, what does it mean? But I like
*  the generalization and maybe as a community would converge towards a group of domains that are
*  sufficiently far away. That would be really damn impressive if also able to generalize some perhaps
*  not as close as Protoss and Zerg was like Wikipedia step. Yeah, it would be a good step. And then
*  really good stuff. But then then like from Starcraft to Wikipedia,
*  yeah, and back. Yeah, that kind of thing. And that that feels also quite hard and far. But
*  I think this as long as you put the benchmark out as we discovered, for instance, with ImageNet,
*  then tremendous progress can be had. So I think maybe there's a lack of benchmark.
*  But I'm sure we'll find one and the community will then work towards that.
*  And then beyond what AGI might mean or would imply, I really am hopeful to see basically
*  machine learning or AI just scaling up and helping people that might not have the resources to hire
*  an assistant or that they might not even know what the weather is like. But, you know, so I think
*  there's in terms of the impact, the positive impact of AI, I think that's maybe what we should
*  also not lose focus, right? The research community building AGI. I mean, that's a real nice goal. But
*  I think the way that DeepMind puts it is and then use it to solve everything else. Right. So
*  I think we should paralyze. Yeah, we shouldn't forget of all the positive things that are
*  actually coming out of AI already and are going to be coming out. Right. But
*  that on that note, let me ask relative to the popular perception. Do you have any worry about
*  the existential threat of artificial intelligence in the near or far future that some people have?
*  I think I'm in the near future. I'm skeptical. So I hope I'm not wrong. I'm not concerned,
*  but I appreciate efforts, ongoing efforts, and even like whole research field on AI safety
*  emerging and in conferences and so on. I think that's great. In the long term, I really hope we
*  just can simply have the benefits outweigh the potential dangers. I am hopeful for that.
*  But also we must remain vigilant to kind of monitor and assess whether the tradeoffs are there. And
*  we have enough also lead time to prevent or to redirect our efforts if need be. Right. So
*  but I'm quite optimistic about the technology and definitely more fearful of other threats
*  in terms of planetary level at this point. But obviously that's the one I kind of have more
*  power on. So clearly I do start thinking more and more about this. And it's kind of it's grown in me
*  actually to start reading more about AI safety, which is a field that so far I have not really
*  contributed to, but maybe there's something to be done there as well. I think it's really important.
*  You know, I talk about this with a few folks, but it's important to ask you and shove it in your
*  head because you're at the leading edge of actually what people are excited about in AI. I mean,
*  the work with AlphaStar, it's arguably at the very cutting edge of the kind of thing that people are
*  afraid of. And so you speaking to that fact and that we're actually quite far away to the kind of
*  thing that people might be afraid of, but it's still worthwhile to think about. And it's also
*  good that you're not as worried and you're also open to think about it. Yeah. I mean,
*  there's two aspects. I mean, me not being worried, but obviously we should prepare for it, right?
*  For things that could go wrong, misuse of the technologies as with any technologies. Right. So
*  I think there's always trade-offs and as a society we've kind of solved this to some extent
*  in the past. So I'm hoping that by having the researchers and the whole community
*  brainstorm and come up with interesting solutions to the new things that will happen in the future,
*  that we can still also push the research to the avenue that I think is kind of the greatest avenue,
*  which is to understand intelligence, right? How are we doing what we're doing? And obviously from
*  a scientific standpoint, that is kind of my personal drive of all the time that I spend doing
*  what I'm doing, really. Where do you see the deep learning as a field heading?
*  Where do you think the next big breakthrough might be? So I think deep learning, I discussed a little
*  of this before, deep learning has to be combined with some form of discretization,
*  program synthesis. I think that's kind of as a research in itself is an interesting topic to
*  expand and start doing more research. And then as kind of what will deep learning enable to do in
*  the future? I don't think that's going to be what's going to happen this year, but also this idea of
*  starting not to throw away all the weights, this idea of learning to learn and really having
*  these agents not having to restart their weights. And you can have an agent that is kind of solving
*  or classifying images on ImageNet, but also generating speech if you ask it to generate
*  some speech. And it should really be kind of almost the same network, but might not be a neural
*  network. It might be a neural network with an optimization algorithm attached to it. But I think
*  this idea of generalization to new task is something that we first must define good benchmarks, but then
*  I think that's going to be exciting and I'm not sure how close we are, but I think if you have a
*  very limited domain, I think we can start doing some progress. And much like how we did a lot of
*  programs in computer vision, we should start thinking, I really like a talk that gave that
*  Leon Butu gave at ICML a few years ago, which is this train test paradigm should be broken.
*  We should stop thinking about a training test, sorry, a training set and a test set. And these
*  are closed things that are untouchable. I think we should go beyond these. And in meta learning,
*  we call these the meta training set and the meta test set, which is really thinking about
*  if I know about ImageNet, why would that network not work on MNIST, which is a much simpler problem?
*  But right now it really doesn't. But it just feels wrong. So I think that's kind of the
*  on the application or the benchmark sites, we probably will see quite a few more interest and
*  progress and hopefully people defining new and exciting challenges really.
*  Do you have any hope or interest in knowledge graphs within this context?
*  So just kind of constructing graphs, so going back to graphs, well neural networks and graphs,
*  but I mean a different kind of knowledge graph, sort of like semantic graphs or there's concepts.
*  Yeah. So I think the idea of graphs is so I've been quite interested in sequences first and then
*  more interesting or different data structures like graphs. And I've studied graph neural networks
*  in the last three years or so. I found these models just very interesting from
*  deep learning sites standpoint. But then why do we want these models and why would we use them?
*  What's the application? What's kind of the killer application of graphs? And perhaps
*  if we could extract a knowledge graph from Wikipedia automatically, that would be interesting
*  because then these graphs have this very interesting structure that also is a bit
*  more compatible with this idea of programs and deep learning kind of working together,
*  jumping neighborhoods and so on. You could imagine defining some primitives to go around graphs.
*  So I think I really like the idea of a knowledge graph. And in fact, when we started,
*  as part of the research we did for StarCraft, I thought, wouldn't it be cool to give the graph of
*  all these buildings that depend on each other and units that have prerequisites of being built by
*  that. And so this is information that the network can learn and extract, but it would have been
*  great to see or to think of really StarCraft as a giant graph that even also as the game evolves,
*  you kind of start taking branches and so on. And we did a bit of research on these, nothing too
*  relevant, but I really like the idea. And it has elements that are, which is something you also
*  work with in terms of visualizing neural networks, as elements of having human interpretable,
*  being able to generate knowledge, representations that are human interpretable that maybe human
*  experts can then tweak or at least understand. So there's a lot of interesting aspect there.
*  And for me personally, I'm just a huge fan of Wikipedia and it's a shame that our neural
*  networks aren't taking advantage of all the structured knowledge that's on the web.
*  What's next for you? What's next for DeepMind? What are you excited about for AlphaStar?
*  Yeah, so I think the obvious next steps would be to apply AlphaStar to other races. I mean,
*  that sort of shows that the algorithm works because we wouldn't want to have created by mistake
*  something in the architecture that happens to work for Protos, but not for other races. So
*  as verification, I think that's an obvious next step that we are working on. And then I would like
*  to see, so agents and players can specialize on different skill sets that allow them to be
*  very good. I think we've seen AlphaStar understanding very well when to take battles
*  and when to not to do that. Also very good at micromanagement and moving the units around and
*  so on. And also very good at producing nonstop and trading of economy with building units.
*  But I have not perhaps seen as much as I would like this idea of the poker idea that you mentioned.
*  I'm not sure StarCraft or AlphaStar rather has developed a very deep understanding of what the
*  opponent is doing and reacting to that and sort of trying to trick the player to do something else.
*  Or that, you know, so this kind of reasoning I would like to see more. So I think purely from
*  a research standpoint, there's perhaps also quite a few things to be done there in the domain of
*  StarCraft. Yeah, in the domain of games, I've seen some interesting work in sort of even auctions,
*  manipulating other players, sort of forming a belief state and just messing with people.
*  Yeah, it's called theory of mind. Theory of mind. Yeah.
*  It's a fascinating theory of mind on StarCraft is kind of they're really made for each other.
*  Yeah. So that would be very exciting to see those techniques applied to StarCraft or perhaps StarCraft
*  driving new techniques, right? As I said, this is always the tension between the two.
*  Well, Oriel, thank you so much for talking today. Awesome. It was great to be here. Thanks.
