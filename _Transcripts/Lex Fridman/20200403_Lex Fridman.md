---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6481s
Video Keywords: ['david silver', 'deep rl', 'deepmind', 'google', 'reinforcement learning', 'machine learning', 'deep learning', 'alphazero', 'muzero', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 392098
Video Rating: None
Video Description: David Silver leads the reinforcement learning research group at DeepMind and was lead researcher on AlphaGo, AlphaZero and co-lead on AlphaStar, and MuZero and lot of important work in reinforcement learning.

Support this podcast by signing up with these sponsors:
- MasterClass: https://masterclass.com/lex
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Reinforcement learning (book): https://amzn.to/2Jwp5zG

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
4:09 - First program
11:11 - AlphaGo
21:42 - Rule of the game of Go
25:37 - Reinforcement learning: personal journey
30:15 - What is reinforcement learning?
43:51 - AlphaGo (continued)
53:40 - Supervised learning and self play in AlphaGo
1:06:12 - Lee Sedol retirement from Go play
1:08:57 - Garry Kasparov
1:14:10 - Alpha Zero and self play
1:31:29 - Creativity in AlphaZero
1:35:21 - AlphaZero applications
1:37:59 - Reward functions
1:40:51 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# David Silver AlphaGo, AlphaZero, and Deep Reinforcement Learning  Lex Fridman Podcast #86
**Lex Fridman:** [April 03, 2020](https://www.youtube.com/watch?v=uPUEq8d73JI)
*  The following is a conversation with David Silver,
*  who leads the Reinforcement Learning Research Group
*  at DeepMind and was the lead researcher
*  on AlphaGo, AlphaZero, and co-led the AlphaStar
*  and MuZero efforts and a lot of important work
*  in reinforcement learning in general.
*  I believe AlphaZero is one of the most important
*  accomplishments in the history of artificial intelligence,
*  and David is one of the key humans who brought AlphaZero
*  to life together with a lot of other great researchers
*  at DeepMind.
*  He's humble, kind, and brilliant.
*  We were both jet lagged, but didn't care and made it happen.
*  It was a pleasure and truly an honor to talk with David.
*  This conversation was recorded before the outbreak
*  of the pandemic.
*  For everyone feeling the medical, psychological,
*  and financial burden of this crisis,
*  I'm sending love your way.
*  Stay strong, we're in this together,
*  we'll beat this thing.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube,
*  review it with five stars on Apple Podcasts,
*  support it on Patreon, or simply connect with me on Twitter
*  at Lex Friedman, spelled F-R-I-D-M-A-N.
*  As usual, I'll do a few minutes of ads now
*  and never any ads in the middle
*  that can break the flow of the conversation.
*  I hope that works for you
*  and doesn't hurt the listening experience.
*  Quick summary of the ads, two sponsors,
*  Masterclass and Cash App.
*  Please consider supporting the podcast
*  by signing up to Masterclass at masterclass.com slash Lex
*  and downloading Cash App and using code LexPodcast.
*  This show is presented by Cash App,
*  the number one finance app in the App Store.
*  When you get it, use code LexPodcast.
*  Cash App lets you send money to friends,
*  buy Bitcoin, and invest in the stock market
*  with as little as one dollar.
*  Since Cash App allows you to buy Bitcoin,
*  let me mention that cryptocurrency
*  in the context of the history of money is fascinating.
*  I recommend Ascent of Money
*  as a great book on this history.
*  Debits and credits on ledgers started around 30,000 years ago.
*  The US dollar created over 200 years ago,
*  and Bitcoin, the first decentralized cryptocurrency,
*  released just over 10 years ago.
*  So given that history,
*  cryptocurrency is still very much
*  in its early days of development,
*  but it's still aiming to, and just might,
*  redefine the nature of money.
*  So again, if you get Cash App from the App Store
*  or Google Play and use the code LexPodcast,
*  you get $10, and Cash App will also donate $10 to First,
*  an organization that is helping to advance robotics
*  and STEM education for young people around the world.
*  This show is sponsored by Masterclass.
*  Sign up at masterclass.com slash Lex to get a discount
*  and to support this podcast.
*  In fact, for a limited time now,
*  if you sign up for an All Access Pass for a year,
*  you get to get another All Access Pass
*  to share with a friend.
*  Buy one, get one free.
*  When I first heard about Masterclass,
*  I thought it was too good to be true.
*  For $180 a year, you get an All Access Pass
*  to watch courses from to list some of my favorites.
*  Chris Hadfield on space exploration,
*  Neil deGrasse Tyson on scientific thinking and communication,
*  Will Wright, the creator of SimCity,
*  and Sims on game design,
*  Jane Goodall on conservation,
*  Carlos Santana on guitar,
*  his song Europa could be the most beautiful
*  guitar song ever written,
*  Gary Kasparov on chess, Daniel Nagrano on poker,
*  and many, many more.
*  Chris Hadfield explaining how rockets work
*  and the experience of being launched into space alone
*  is worth the money.
*  For me, the key is to not be overwhelmed
*  by the abundance of choice.
*  Pick three courses you want to complete,
*  watch each of them all the way through.
*  It's not that long, but it's an experience
*  that will stick with you for a long time, I promise.
*  It's easily worth the money.
*  You can watch it on basically any device.
*  Once again, sign up on masterclass.com slash Lex
*  to get a discount and to support this podcast.
*  And now here's my conversation with David Silver.
*  What was the first program you ever written
*  and what programming language?
*  Do you remember?
*  I remember very clearly, yeah.
*  My parents brought home this BBC Model B microcomputer,
*  it was just this fascinating thing to me.
*  I was about seven years old and couldn't resist
*  just playing around with it.
*  So I think first program ever was writing my name out
*  in different colors and getting it to loop and repeat that.
*  And there was something magical about that,
*  which just led to more and more.
*  How did you think about computers back then?
*  Like the magical aspect of it,
*  that you can write a program and there's this thing
*  that you just gave birth to that's able to create
*  sort of visual elements and live on its own.
*  Or did you not think of it in those romantic notions?
*  Was it more like, oh, that's cool.
*  I can solve some puzzles.
*  It was always more than solving puzzles.
*  It was something where there was this
*  limitless possibilities.
*  Once you have a computer in front of you,
*  you can do anything with it.
*  I used to play with Lego with the same feeling.
*  You can make anything you want out of Lego,
*  but even more so with a computer.
*  You're not constrained by the amount of kit you've got.
*  And so I was fascinated by it and started pulling out
*  the user guide and the advanced user guide.
*  And then learning, so I started in basic
*  and then later 6502, my father also became interested
*  in this machine and gave up his career to go back to school
*  and study for a master's degree in artificial intelligence,
*  funnily enough, at Essex University when I was seven.
*  So I was exposed to those things at an early age.
*  He showed me how to program in Prologue
*  and do things like querying your family tree.
*  And those are some of my earliest memories of trying to,
*  trying to figure things out on a computer.
*  Those are the early steps in computer science programming,
*  but when did you first fall in love
*  with artificial intelligence or with the ideas,
*  the dreams of AI?
*  I think it was really when I went to study at university.
*  So I was an undergrad at Cambridge
*  and studying computer science.
*  And I really started to question,
*  what really are the goals?
*  What's the goal?
*  Where do we want to go with computer science?
*  And it seemed to me that the only step
*  of major significance to take was to try
*  and recreate something akin to human intelligence.
*  If we could do that, that would be a major leap forward.
*  And that idea, I certainly wasn't the first to have it,
*  but it nestled within me somewhere and became like a bug.
*  I really wanted to crack that problem.
*  So you thought it was, like you had a notion
*  that this is something that human beings can do,
*  that it is possible to create an intelligent machine?
*  Well, I mean, unless you believe in something metaphysical,
*  then what are our brains doing?
*  Well, at some level,
*  they're information processing systems,
*  which are able to take whatever information is in there,
*  transform it through some form of program
*  and produce some kind of output,
*  which enables that human being to do all the amazing things
*  that they can do in this incredible world.
*  So then do you remember the first time
*  you've written a program that,
*  because you also had an interest in games,
*  do you remember the first time you were in a program
*  that beat you in a game?
*  That more beat you at anything?
*  Sort of achieved super David Silver level performance?
*  So I used to work in the games industry.
*  So for five years, I programmed games for my first job.
*  So it was an amazing opportunity
*  to get involved in a startup company.
*  And so I was involved in building AI at that time.
*  And so for sure, there was a sense of building
*  handcrafted what people used to call AI
*  in the games industry,
*  which I think is not really what we might think of as AI
*  in its fullest sense,
*  but something which is able to take actions
*  and in a way which makes things interesting
*  and challenging for the human player.
*  And at that time I was able to build
*  these handcrafted agents,
*  which in certain limited cases could do things
*  which were able to do better than me,
*  but mostly in these kind of Twitch-like scenarios
*  where they were able to do things faster
*  or because they had some pattern
*  which was able to exploit repeatedly.
*  I think if we're talking about real AI,
*  the first experience for me came after that
*  when I realized that this path I was on
*  wasn't taking me towards,
*  it wasn't dealing with that bug,
*  which I still had inside me
*  to really understand intelligence and try and solve it.
*  That everything people were doing in games
*  was short-term fixes rather than long-term vision.
*  And so I went back to study for my PhD,
*  which was funny enough trying to apply reinforcement learning
*  to the game of Go.
*  And I built my first Go program
*  using reinforcement learning,
*  a system which would by trial and error
*  play against itself and was able to learn
*  which patterns were actually helpful
*  to predict whether it was gonna win or lose the game
*  and then choose the moves that led to the combination
*  of patterns that would mean that you're more likely to win.
*  And that system beat me.
*  And how did that make you feel?
*  Made me feel good.
*  I mean, was there sort of the, yeah,
*  it's a mix of a sort of excitement
*  and was there a tinge of sort of like,
*  almost like a fearful awe?
*  In space, 2001, Space Odyssey,
*  kind of realizing that you've created something that,
*  that is, you know,
*  that's achieved human level intelligence
*  in this one particular little task.
*  And in that case, I suppose neural networks weren't involved.
*  There were no neural networks in those days.
*  This was pre deep learning revolution,
*  but it was a principled self-learning system
*  based on a lot of the principles
*  which people still use in deep reinforcement learning.
*  How did I feel?
*  I think I found it immensely satisfying
*  that a system which was able to learn
*  from first principles for itself
*  was able to reach the point
*  that it was understanding this domain
*  better than I could and able to outwit me.
*  I don't think it was a sense of awe.
*  It was a sense that satisfaction,
*  that something I felt should work had worked.
*  So to me, AlphaGo, and I don't know how else to put it,
*  but to me, AlphaGo and AlphaGo Zero,
*  mastering the game of Go is, again, to me,
*  the most profound and inspiring moment
*  in the history of artificial intelligence.
*  So you're one of the key people behind this achievement,
*  and I'm Russian, so I really felt
*  the first sort of seminal achievement
*  when Deep Blue beat Garry Kasparov in 1987.
*  So as far as I know, the AI community at that point
*  largely saw the game of Go as unbeatable in AI
*  using the state of the art to brute force methods,
*  search methods, even if you consider,
*  at least the way I saw it,
*  even if you consider arbitrary exponential scaling
*  of compute, Go would still not be solvable,
*  hence why it was thought to be impossible.
*  So given that the game of Go was impossible to master,
*  when was the dream for you?
*  You just mentioned your PhD thesis
*  of building the system that plays Go.
*  When was the dream for you that you could actually
*  build a computer program that achieves world class,
*  not necessarily beats the world champion,
*  but achieves that kind of level of playing Go?
*  First of all, thank you, that was very kind words.
*  And funnily enough, I just came from a panel
*  where I was actually in a conversation
*  with Garry Kasparov and Murray Campbell,
*  who was the author of Deep Blue,
*  and it was their first meeting together since the match.
*  So that just occurred yesterday,
*  so I'm literally fresh from that experience.
*  So these are amazing moments when they happen,
*  but where did it all start?
*  Well, for me, it started when I became fascinated
*  in the game of Go.
*  So Go for me, I've grown up playing games,
*  I've always had a fascination in board games,
*  I played chess as a kid, I played Scrabble as a kid.
*  When I was at university, I discovered the game of Go,
*  and to me, it just blew all of those other games
*  out of the water, it was just so deep and profound
*  in its complexity with endless levels to it.
*  What I discovered was that I could devote endless hours
*  to this game, and I knew in my heart of hearts
*  that no matter how many hours I would devote to it,
*  I would never become a grand master,
*  or there was another path, and the other path
*  was to try and understand how you could get
*  some other intelligence to play this game
*  better than I would be able to.
*  And so even in those days, I had this idea that,
*  what if it was possible to build a program
*  that could crack this?
*  And as I started to explore the domain,
*  I discovered that this was really the domain
*  where people felt deeply that if progress could be made
*  in Go, it would really mean a giant leap forward for AI.
*  It was the challenge where all other approaches had failed.
*  This is coming out of the era you mentioned,
*  which was in some sense the golden era
*  for the classical methods of AI, like heuristic search.
*  In the 90s, they all fell one after another,
*  not just chess with deep blue, but checkers,
*  backgammon, Othello.
*  There were numerous cases where systems built
*  on top of heuristic search methods
*  with these high-performance systems
*  had been able to defeat the human world champion
*  in each of those domains.
*  And yet in that same time period,
*  there was a million dollar prize available
*  for the game of Go, for the first system
*  to be a human professional player.
*  And at the end of that time period,
*  at year 2000 when the prize expired,
*  the strongest Go program in the world
*  was defeated by a nine-year-old child
*  when that nine-year-old child was giving nine free moves
*  to the computer at the start of the game
*  to try and even things up.
*  And the computer Go expert beat that same strongest program
*  with 29 handicapped stones, 29 free moves.
*  So that's what the state of affairs was
*  when I became interested in this problem in around 2003
*  when I started working on computer Go.
*  There was nothing, there was just,
*  there was very, very little in the way of progress
*  towards meaningful performance, again,
*  at anything approaching human level.
*  And so people, it wasn't through lack of effort.
*  People have tried many, many things.
*  And so there was a strong sense that something different
*  would be required for Go than had been needed
*  for all of these other domains where AI had been successful.
*  And maybe the single clearest example is that
*  Go, unlike those other domains,
*  had this kind of intuitive property
*  that a Go player would look at a position and say,
*  hey, here's this mess of black and white stones.
*  But from this mess, oh, I can predict
*  that this part of the board has become my territory,
*  this part of the board has become your territory.
*  And I've got this overall sense that I'm gonna win
*  and that this is about the right move to play.
*  And that intuitive sense of judgment,
*  of being able to evaluate what's going on in a position,
*  it was pivotal to humans being able to play this game
*  and something that people had no idea
*  how to put into computers.
*  So this question of how to evaluate a position,
*  how to come up with these intuitive judgments
*  was the key reason why Go was so hard
*  in addition to its enormous search space
*  and the reason why methods which had succeeded so well
*  elsewhere failed in Go.
*  And so people really felt deep down that, you know,
*  in order to crack Go, we would need to get something
*  akin to human intuition.
*  And if we got something akin to human intuition,
*  we'd be able to solve, you know,
*  many, many more problems in AI.
*  So for me, that was the moment where it's like,
*  okay, this is not just about playing the game of Go,
*  this is about something profound.
*  And it was back to that bug,
*  which had been itching me all those years.
*  You know, this is the opportunity to do something meaningful
*  and transformative and I guess a dream was born.
*  That's a really interesting way to put it.
*  So almost this realization that you need to find,
*  formulate Go as a kind of a prediction problem
*  versus a search problem was the intuition.
*  I mean, maybe that's the wrong crude term,
*  but to give it us the ability to kind of
*  intuit things about positional structure of the board.
*  Now, okay, but what about the learning part of it?
*  Did you have a sense that you have to,
*  that learning has to be part of the system?
*  Again, something that hasn't really as far as I think,
*  except with TDGammon and in the 90s with RL a little bit,
*  hasn't been part of those day-to-day art
*  game playing systems.
*  So I strongly felt that learning would be necessary.
*  And that's why my PhD topic back then
*  was trying to apply reinforcement learning
*  to the game of Go.
*  And not just learning of any type,
*  but I felt that the only way to really have a system
*  to progress beyond human levels of performance
*  wouldn't just be to mimic how humans do it,
*  but to understand for themselves.
*  And how else can a machine hope to understand
*  what's going on except through learning?
*  If you're not learning, what else are you doing?
*  Well, you're putting all the knowledge into the system.
*  And that just feels like something which decades of AI
*  have told us is maybe not a dead end,
*  but certainly has a ceiling to the capabilities.
*  It's known as the knowledge acquisition bottleneck
*  that the more you try to put into something,
*  the more brittle the system becomes.
*  And so you just have to have learning.
*  You have to have learning.
*  That's the only way you're going to be able to get
*  a system which has sufficient knowledge in it,
*  millions and millions of pieces of knowledge,
*  billions, trillions of a form that it can actually
*  apply for itself and understand how those billions
*  and trillions of pieces of knowledge can be leveraged
*  in a way which will actually lead it towards its goal
*  without conflict or other issues.
*  Yeah, I mean, if I put myself back in that time,
*  I just wouldn't think like that
*  without a good demonstration of RL.
*  I would think more in the symbolic AI,
*  like not learning, but sort of a simulation
*  of a knowledge base, like a growing knowledge base,
*  but it would still be sort of pattern-based,
*  like basically have little rules that you kind of
*  assemble together into a large knowledge base.
*  Well, in a sense, that was the state of the art back then.
*  So if you look at the Go programs,
*  which had been competing for this prize I mentioned,
*  they were an assembly of different specialized systems,
*  some of which used huge amounts of human knowledge
*  to describe how you should play the opening,
*  how you should, all the different patterns
*  that were required to play well in the game of Go,
*  end game theory, combinatorial game theory,
*  and combined with more principled search-based methods,
*  which were trying to solve for particular sub-parts
*  of the game, like life and death, connecting groups together,
*  all these amazing sub-problems that just emerge
*  in the game of Go, there were different pieces
*  all put together into this collage,
*  which together would try and play against a human.
*  And although not all of the pieces were handcrafted,
*  the overall effect was nevertheless still brittle,
*  and it was hard to make all these pieces work well together.
*  And so really what I was pressing for,
*  and the main innovation of the approach I took,
*  was to go back to first principles and say,
*  well, let's back off that and try and find
*  a principled approach where the system can learn for itself.
*  Just from the outcome, learn for itself.
*  If you try something, did that help or did it not help?
*  And only through that procedure can you arrive
*  at knowledge which is verified,
*  the system has to verify it for itself,
*  not relying on any other third party to say,
*  this is right or this is wrong.
*  And so that principle was already very important
*  in those days, but unfortunately we were missing
*  some important pieces back then.
*  So before we dive into maybe discussing
*  the beauty of reinforcement learning,
*  let's take a step back, we kind of skipped it a bit,
*  but the rules of the game of Go.
*  The elements of it perhaps contrasting to chess
*  that sort of you really enjoy as a human being
*  and also that make it really difficult
*  as a AI machine learning problem.
*  So the game of Go has remarkably simple rules.
*  In fact, so simple that people have speculated
*  that if we were to meet alien life at some point,
*  that we wouldn't be able to communicate with them,
*  but we would be able to play Go with them
*  because they probably have discovered the same rule set.
*  So the game is played on a 19 by 19 grid,
*  and you play on the intersections of the grid
*  and the players take turns.
*  And the aim of the game is very simple,
*  it's to surround as much territory as you can,
*  as many of these intersections with your stones
*  and to surround more than your opponent does.
*  And the only nuance to the game is that
*  if you fully surround your opponent's piece,
*  then you get to capture it and remove it from the board
*  and it counts as your own territory.
*  Now from those very simple rules,
*  immense complexity arises,
*  there's kind of profound strategies
*  in how to surround territory,
*  how to kind of trade off between making solid territory
*  yourself now compared to building up influence
*  that will help you acquire territory later in the game,
*  how to connect groups together,
*  how to keep your own groups alive,
*  which patterns of stones are most useful compared to others.
*  There's just immense knowledge and human Go players
*  have played this game for,
*  it was discovered thousands of years ago
*  and human Go players have built up
*  this immense knowledge base over the years.
*  It's studied very deeply and played by
*  something like 50 million players across the world,
*  mostly in China, Japan and Korea,
*  where it's an important part of the culture,
*  so much so that it's considered one of the four ancient arts
*  that was required by Chinese scholars.
*  So there's a deep history there.
*  But there's interesting quality.
*  So if I compare to chess, chess is in the same way
*  as it is in Chinese culture for Go
*  and chess in Russia is also considered
*  one of the sacred arts.
*  So if we contrast sort of Go with chess,
*  there's interesting qualities about Go.
*  Maybe you can correct me if I'm wrong,
*  but the evaluation of a particular static board
*  is not as reliable.
*  Like you can't, in chess you can kind of assign points
*  to the different units.
*  And it's kind of a pretty good measure
*  of who's winning, who's losing.
*  It's not so clear.
*  Yeah, so in the game of Go,
*  you find yourself in a situation where
*  both players have played the same number of stones,
*  and that actually captures a strong level of play
*  happen very rarely, which means that at any moment in the game
*  you've got the same number of white stones and black stones.
*  And the only thing which differentiates
*  how well you're doing is this intuitive sense of,
*  you know, where are the territories
*  ultimately going to form on this board?
*  And if you look at the complexity of a real Go position,
*  you know, it's mind boggling that kind of question
*  of what will happen in 300 moves from now
*  when you see just a scattering of 20 white
*  and black stones intermingled.
*  And so that challenge is the reason why position evaluation
*  is so hard in Go compared to other games.
*  In addition to that, it has an enormous search space.
*  So there's around 10 to the 170 positions in the game of Go.
*  That's an astronomical number.
*  And that search space is so great
*  that traditional heuristic search methods
*  that were so successful in things like deep blue
*  and chess programs just kind of fall over in Go.
*  So at which point did reinforcement learning
*  enter your life, your research life, your way of thinking?
*  We just talked about learning,
*  but reinforcement learning is a very particular
*  kind of learning.
*  One that's both philosophically sort of profound,
*  but also one that's pretty difficult to get to work
*  as if we look back in the earth, at least the early days.
*  So when did that enter your life
*  and how did that work progress?
*  So I had just finished working in the games industry,
*  this startup company, and I took a year out
*  to discover for myself exactly which path I wanted to take.
*  I knew I wanted to study intelligence,
*  but I wasn't sure what that meant at that stage.
*  I really didn't feel I had the tools
*  to decide on exactly which path I wanted to follow.
*  So during that year, I read a lot.
*  And one of the things I read was Sutton and Bartow,
*  this sort of seminal textbook on
*  an introduction to reinforcement learning.
*  And when I read that textbook,
*  I just had this resonating feeling
*  that this is what I understood intelligence to be.
*  And this was the path that I felt would be necessary
*  to go down to make progress in AI.
*  So I got in touch with Rich Sutton
*  and asked him if he would be interested
*  in supervising me on a PhD thesis in computer go.
*  And he basically said that
*  if he's still alive, he'd be happy to.
*  But unfortunately, he'd been struggling
*  with very serious cancer for some years.
*  And he really wasn't confident at that stage
*  that he'd even be around to see the end of it.
*  But fortunately, that part of the story
*  worked out very happily.
*  And I found myself out there in Alberta.
*  They've got a great games group out there
*  with a history of fantastic work in board games as well,
*  as Rich Sutton, the father of RL.
*  So it was the natural place for me to go in some sense
*  to study this question.
*  And the more I looked into it,
*  the more strongly I felt that this wasn't just the path
*  to progress in computer go,
*  but really, this was the thing I'd been looking for.
*  This was really an opportunity
*  to frame what intelligence means.
*  Like what are the goals of AI
*  in a clear single clear problem definition,
*  such that if we're able to solve
*  that clear single problem definition,
*  in some sense, we've cracked the problem of AI.
*  So to you, reinforcement learning ideas,
*  at least sort of echoes of it,
*  would be at the core of intelligence.
*  It is at the core of intelligence.
*  And if we ever create a human level intelligence system,
*  it would be at the core of that kind of system.
*  Let me say it this way,
*  that I think it's helpful to separate out
*  the problem from the solution.
*  So I see the problem of intelligence,
*  I would say it can be formalized
*  as the reinforcement learning problem.
*  And that that formalization is enough to capture
*  most, if not all of the things
*  that we mean by intelligence,
*  that they can all be brought within this framework
*  and gives us a way to access them
*  in a meaningful way that allows us as scientists
*  to understand intelligence
*  and us as computer scientists to build them.
*  And so in that sense, I feel that it gives us a path,
*  maybe not the only path, but a path towards AI.
*  And so do I think that any system in the future
*  that's solved AI would have to have RL within it?
*  Well, I think if you ask that,
*  you're asking about the solution methods.
*  I would say that if we have such a thing,
*  it would be a solution to the RL problem.
*  Now, what particular methods have been used to get there?
*  Well, we should keep an open mind about the best approaches
*  to actually solve any problem.
*  And the things we have right now for reinforcement learning,
*  maybe I believe they've got a lot of legs,
*  but maybe we're missing some things.
*  Maybe there's gonna be better ideas.
*  I think we should keep, let's remain modest
*  and we're at the early days of this field
*  and there are many amazing discoveries ahead of us.
*  For sure, the specifics,
*  especially of the different kinds of RL approaches currently,
*  there could be other things that fall
*  into the very large umbrella of RL.
*  But if it's okay, can we take a step back
*  and kind of ask the basic question
*  of what is to you reinforcement learning?
*  So reinforcement learning is the study
*  and the science and the problem of intelligence
*  in the form of an agent that interacts with an environment.
*  So the problem you're trying to solve
*  is represented by some environment,
*  like the world in which that agent is situated.
*  And the goal of RL is clear,
*  that the agent gets to take actions.
*  Those actions have some effect on the environment
*  and the environment gives back an observation to the agent
*  saying, this is what you see or sense.
*  And one special thing which it gives back
*  is called the reward signal,
*  how well it's doing in the environment.
*  And the reinforcement learning problem
*  is to simply take actions over time
*  so as to maximize that reward signal.
*  So a couple of basic questions.
*  What types of RL approaches are there?
*  So I don't know if there's a nice brief
*  inwards way to paint a picture of sort of value-based,
*  model-based, policy-based reinforcement learning.
*  Yeah, so now if we think about,
*  okay, so there's this ambitious problem definition of RL.
*  It's really, it's truly ambitious.
*  It's trying to capture and encircle all of the things
*  in which an agent interacts with an environment
*  and say, well, how can we formalize and understand
*  what it means to crack that?
*  Now let's think about the solution method.
*  Well, how do you solve a really hard problem like that?
*  Well, one approach you can take is to decompose
*  that very hard problem into pieces that work together
*  to solve that hard problem.
*  And so you can kind of look at the decomposition
*  that's inside the agent's head, if you like,
*  and ask, well, what form does that decomposition take?
*  And some of the most common pieces that people use
*  when they're kind of putting the solution method together,
*  some of the most common pieces that people use
*  are whether or not that solution has a value function.
*  That means, is it trying to predict,
*  explicitly trying to predict how much reward
*  it will get in the future?
*  Does it have a representation of a policy?
*  That means something which is deciding how to pick actions.
*  Is that decision-making process explicitly represented?
*  And is there a model in the system?
*  Is there something which is explicitly trying to predict
*  what will happen in the environment?
*  And so those three pieces are, to me,
*  some of the most common building blocks.
*  And I understand the different choices in RL
*  as choices of whether or not to use those building blocks
*  when you're trying to decompose the solution.
*  Should I have a value function represented?
*  Should I have a policy represented?
*  Should I have a model represented?
*  And there are combinations of those pieces,
*  and of course, other things that you could add
*  into the picture as well.
*  But those three fundamental choices give rise
*  to some of the branches of RL
*  with which we are very familiar.
*  And so those, as you mentioned there,
*  it's a choice of what's specified or modeled explicitly.
*  And the idea is that all of these
*  are somehow implicitly learned within the system.
*  So it's almost a choice of how you approach a problem.
*  Do you see those as fundamental differences
*  or are these almost like small specifics,
*  like the details of how you solve the problem,
*  but they're not fundamentally different from each other?
*  I think the fundamental idea is maybe at the higher level,
*  the fundamental idea is the first step of the decomposition
*  is really to say, well, how are we really gonna solve
*  any kind of problem where you're trying to figure out
*  how to take actions and just from this stream
*  of observations, you've got some agent situated
*  in its sensory motor stream
*  and getting all these observations in,
*  getting to take these actions, and what should it do?
*  How can you even broach that problem?
*  Maybe the complexity of the world is so great
*  that you can't even imagine how to build a system
*  that would understand how to deal with that.
*  And so the first step of this decomposition is to say,
*  well, you have to learn, the system has to learn for itself.
*  And so note that the reinforcement learning problem
*  doesn't actually stipulate that you have to learn.
*  Like you could maximize your rewards without learning.
*  It would just, wouldn't do a very good job of it.
*  So learning is required because it's the only way
*  to achieve good performance in any sufficiently large
*  and complex environment.
*  So that's the first step.
*  And so that step gives commonality
*  to all of the other pieces.
*  Because now you might ask, well, what should you be learning?
*  What does learning even mean?
*  In this sense, learning might mean, well,
*  you're trying to update the parameters of some system,
*  which is then the thing that actually picks the actions.
*  And those parameters could be representing anything.
*  They could be parameterizing a value function, or a model,
*  or a policy.
*  And so in that sense, there's a lot of commonality
*  in that whatever is being represented there
*  is the thing which is being learned.
*  And it's being learned with the ultimate goal
*  of maximizing rewards.
*  But the way in which you decompose the problem
*  is really what gives the semantics to the whole system.
*  Like are you trying to learn something to predict well,
*  like a value function or a model?
*  Are you learning something to perform well, like a policy?
*  And the form of that objective is kind of giving the semantics
*  to the system.
*  And so it really is, at the next level down,
*  a fundamental choice.
*  And we have to make those fundamental choices as system
*  designers or enable our algorithms
*  to be able to learn how to make those choices for themselves.
*  So then the next step you mentioned,
*  the very first thing you have to deal with
*  is can you even take in this huge stream of observations
*  and do anything with it?
*  So the natural next basic question
*  is what is deep reinforcement learning?
*  And what is this idea of using neural networks
*  to deal with this huge incoming stream?
*  So amongst all the approaches for reinforcement learning,
*  deep reinforcement learning is one family of solution methods
*  that tries to utilize powerful representations that
*  are offered by neural networks to represent
*  any of these different components
*  of the solution of the agent, like whether it's
*  the value function or the model or the policy.
*  The idea of deep learning is to say,
*  well, here's a powerful toolkit that's so powerful
*  that it's universal in the sense that it
*  can represent any function and it can learn any function.
*  And so if we can leverage that universality,
*  that means that whatever we need to represent for our policy
*  or for our value function or for our model,
*  deep learning can do it.
*  So deep learning is one approach that offers us a toolkit that
*  has no ceiling to its performance,
*  that as we start to put more resources into the system,
*  more memory and more computation and more data,
*  more experience, more interactions
*  with the environment, that these are systems that can just
*  get better and better and better at doing whatever the job is
*  they've asked them to do, whatever we've
*  to represent, it can learn a function that does a better
*  and better job of representing that knowledge,
*  whether that knowledge be estimating
*  how well you're going to do in the world, the value function,
*  whether it's going to be choosing what to do
*  in the world, the policy, or whether it's
*  understanding the world itself, what's
*  going to happen next, the model.
*  Nevertheless, the fact that neural networks
*  are able to learn incredibly complex representations that
*  allow you to do the policy, the model, or the value function
*  is, at least to my mind, exceptionally
*  beautiful and surprising.
*  Was it surprising to you?
*  Can you still believe it works as well as it does?
*  Do you have good intuition about why it works at all
*  and works as well as it does?
*  Let me take two parts to that question.
*  I think it's not surprising to me
*  that the idea of reinforcement learning
*  works because in some sense, I feel
*  it's the only thing which can, ultimately.
*  And so I feel we have to address it.
*  And there must be success as possible because we
*  have examples of intelligence.
*  And it must, at some level, be possible to acquire experience
*  and use that experience to do better
*  in a way which is meaningful to environments of the complexity
*  that humans can deal with.
*  It must be.
*  Am I surprised that our current systems can
*  do as well as they can do?
*  I think one of the big surprises for me
*  and a lot of the community is really the fact
*  that deep learning can continue to perform so well despite
*  the fact that these neural networks that they're
*  representing have these incredibly non-linear,
*  bumpy surfaces which, to our low dimensional intuitions,
*  make it feel like, surely you're just going to get stuck
*  and learning will get stuck because you won't be
*  able to make any further progress.
*  And yet, the big surprise is that learning continues.
*  And these, what appear to be local optima,
*  turn out not to be because in high dimensions, when
*  you make really big neural nets, there's always a way out.
*  And there's a way to go even lower.
*  And then you're still not in a local optima
*  because there's some other pathway that will take you out
*  and take you lower still.
*  And so no matter where you are, learning
*  can proceed and do better and better and better without bound.
*  And so that is a surprising and beautiful property
*  of neural nets, which I find elegant and beautiful
*  and somewhat shocking that it turns out to be the case.
*  As you said, which I really like,
*  to our low dimensional intuitions, that's surprising.
*  Yeah.
*  Yeah, we're very tuned to working
*  within a three dimensional environment.
*  And so to start to visualize what a billion dimensional
*  neural network surface that you're trying to optimize over,
*  what that even looks like, is very hard for us.
*  So I think that really, if you try
*  to account for essentially the AI winter where people gave up
*  on neural networks, I think it's really down
*  to that lack of ability to generalize
*  from low dimensions to high dimensions.
*  Because back then, we were in the low dimensional case.
*  People could only build neural nets with 50 nodes in them
*  or something.
*  And to imagine that it might be possible to build
*  a billion dimensional neural net and it might have
*  a completely different qualitatively different property
*  was very hard to anticipate.
*  And I think even now, we're starting
*  to build the theory to support that.
*  And it's incomplete at the moment,
*  but all of the theory seems to be pointing in the direction
*  that indeed, this is an approach which truly is universal,
*  both in its representational capacity, which was known,
*  but also in its learning ability, which is surprising.
*  And it makes one wonder what else we're missing due
*  to our low dimensions intuitions that will seem obvious once
*  it's discovered.
*  I often wonder, when we one day do
*  have AIs which are superhuman in their abilities
*  to understand the world, what will they
*  think of the algorithms that we developed back now?
*  Will it be looking back at these days
*  and thinking that, will we look back and feel
*  that these algorithms were naive first steps,
*  or will they still be the fundamental ideas which
*  are used even in 100,000, 10,000 years?
*  It's hard to know.
*  They'll watch back to this conversation with a smile,
*  maybe a little bit of a laugh.
*  I mean, my sense is I think just like when
*  we used to think that the sun revolved around the Earth,
*  they'll see our systems of today reinforcement learning
*  as too complicated, that the answer was simple all along.
*  There's something, just like you said in the game of Go,
*  I mean, I love the systems of cellular automata,
*  that there's simple rules from which incredible complexity
*  emerges.
*  So it feels like there might be some really simple approaches,
*  just like Rich Sutton says, right?
*  These simple methods with compute over time
*  seem to prove to be the most effective.
*  I 100% agree.
*  I think that if we try to anticipate
*  what will generalize well into the future,
*  I think it's likely to be the case that it's
*  the simple, clear ideas which will have the longest legs
*  and which will carry us furthest into the future.
*  Nevertheless, we're in a situation
*  where we need to make things work today.
*  And sometimes that requires putting together
*  more complex systems where we don't have the full answers yet
*  as to what those minimal ingredients might be.
*  So speaking of which, if we could take a step back to Go,
*  what was MoGo and what was the key idea behind the system?
*  So back during my PhD on Computer Go, around about that time,
*  there was a major new development
*  which actually happened in the context of Computer Go.
*  And it was really a revolution in the way
*  that heuristic search was done.
*  And the idea was essentially that a position
*  could be evaluated or a state in general could be evaluated
*  not by humans saying whether that position is good or not
*  or even humans providing rules as to how you might evaluate it,
*  but instead by allowing the system to randomly play out
*  the game until the end multiple times
*  and taking the average of those outcomes as the prediction
*  of what will happen.
*  So for example, if you're in the game of Go,
*  the intuition is that you take a position
*  and you get the system to kind of play random moves
*  against itself all the way to the end of the game
*  and you see who wins.
*  And if black ends up winning more of those random games
*  than white, well, you say, hey, this
*  is a position that favors white.
*  And if white ends up winning more of those random games
*  than black, then it favors white.
*  So that idea was known as Monte Carlo search
*  and a particular form of Monte Carlo search
*  that became very effective and was developed in computer Go
*  first by Remy Coulomb in 2006 and then taken further
*  by others was something called Monte Carlo tree search, which
*  basically takes that same idea and uses that insight
*  to evaluate every node of a search tree
*  is evaluated by the average of the random play outs
*  from that node onwards.
*  And this idea was very powerful and suddenly
*  led to huge leaps forward in the strength of computer Go
*  playing programs.
*  And among those, the strongest of the Go playing programs
*  in those days was a program called
*  MoGo, which was the first program to actually reach
*  human master level on small boards, 9 by 9 boards.
*  And so this was a program by someone called
*  Sylvain Geli, who's a good colleague of mine,
*  but I worked with him a little bit in those days,
*  part of my PhD thesis.
*  And MoGo was a first step towards the latest successes
*  we saw in computer Go, but it was still
*  missing a key ingredient.
*  MoGo was evaluating purely by random rollouts against itself.
*  And in a way, it's truly remarkable
*  that random play should give you anything at all.
*  Why in this perfectly deterministic game
*  that's very precise and involves these very exact sequences,
*  why is it that randomization is helpful?
*  And so the intuition is that randomization
*  captures something about the nature of the search tree,
*  from a position that you're understanding
*  the nature of the search tree from that node
*  onwards by using randomization.
*  And this was a very powerful idea.
*  And I've seen this in other spaces.
*  Talk to Richard Karp and so on.
*  Randomized algorithms somehow magically
*  are able to do exceptionally well
*  and simplifying the problem somehow.
*  Makes you wonder about the fundamental nature
*  of randomness in our universe.
*  It seems to be a useful thing.
*  So from that moment, can you maybe
*  tell the origin story and the journey of AlphaGo?
*  Yeah.
*  So programs based on Monte Carlo tree search
*  were a first revolution in the sense
*  that they led to suddenly programs that could play the game
*  to any reasonable level.
*  But they plateaued.
*  It seemed that no matter how much effort people put
*  into these techniques, they couldn't exceed the level
*  of amateur, down-level Go players.
*  So strong players, but not anywhere
*  near the level of professionals, never mind the world champion.
*  And so that brings us to the birth of AlphaGo,
*  which happened in the context of a startup company known
*  as DeepMind.
*  I heard of them.
*  Where a project was born.
*  And the project was really a scientific investigation
*  where myself and Ajay Huang and an intern, Chris Madison,
*  were exploring a scientific question.
*  And that scientific question was really,
*  is there another fundamentally different approach
*  to this key question of Go, the key challenge of how can you
*  build that intuition?
*  And how can you just have a system that
*  could look at a position and understand what move to play
*  or how well you're doing in that position?
*  Who's going to win?
*  And so the deep learning revolution had just begun.
*  Systems like ImageNet had suddenly
*  been won by deep learning techniques back in 2012.
*  And following that, it was natural to ask, well,
*  if deep learning is able to scale up so effectively
*  with images to understand them enough to classify them,
*  well, why not go?
*  Why not take the black and white stones of the Go board
*  and build a system which can understand for itself
*  what that means in terms of what move to pick
*  or who's going to win the game, black or white?
*  And so that was our scientific question,
*  which we were probing and trying to understand.
*  And as we started to look at it, we
*  discovered that we could build a system.
*  So in fact, our very first paper on AlphaGo
*  was actually a pure deep learning system, which
*  was trying to answer this question.
*  And we showed that actually a pure deep learning
*  system with no search at all was actually
*  able to reach human Dan level, master level,
*  at the full game of Go, 19 by 19 boards.
*  And so without any search at all,
*  suddenly we had systems which were playing
*  at the level of the best Monte Carlo tree step systems,
*  the ones with randomized rollouts.
*  So first of all, sorry to interrupt,
*  but that's kind of a groundbreaking notion.
*  That's like basically a definitive step away
*  from a couple of decades of essentially
*  search dominating AI.
*  So how did that make you feel?
*  Was it surprising from a scientific perspective
*  in general, how to make you feel?
*  I found this to be profoundly surprising.
*  In fact, it was so surprising that we had a bet back then.
*  And like many good projects, bets are quite motivating.
*  And the bet was whether it was possible for a system
*  based purely on deep learning, no search at all,
*  to beat a Dan level human player.
*  And so we had someone who joined our team,
*  who was a Dan level player, he came in,
*  and we had this first match against him.
*  Which side of the bet were you on, by the way?
*  The loser or the winning side?
*  I tend to be an optimist with the power of deep learning
*  and reinforcement learning.
*  So the system won and we were able to beat
*  this human Dan level player.
*  And for me, that was the moment where it was like,
*  okay, something special is afoot here.
*  We have a system which without search is able to already
*  just look at this position and understand things
*  as well as a strong human player.
*  And from that point onwards, I really felt that
*  reaching the top levels of human play,
*  professional level, world champion level,
*  I felt it was actually an inevitability.
*  And if it was an inevitable outcome,
*  I was rather keen that it would be us that achieved it.
*  So we scaled up.
*  This was something where, you know,
*  so had lots of conversations back then
*  with Demis Asabis, the head of DeepMind,
*  who was extremely excited.
*  And we made the decision to scale up the project,
*  brought more people on board.
*  And so AlphaGo became something where we had a clear goal,
*  which was to try and crack this outstanding challenge of AI
*  to see if we could beat the world's best players.
*  And this led within the space of not so many months
*  to playing against the European champion Fan Hui
*  in a match which became memorable in history
*  as the first time a Go program
*  had ever beaten a professional player.
*  And at that time we had to make a judgment
*  as to when and whether we should go
*  and challenge the world champion.
*  And this was a difficult decision to make.
*  Again, we were basing our predictions on our own progress
*  and had to estimate based on the rapidity
*  of our own progress when we thought we would
*  exceed the level of the human world champion.
*  And we tried to make an estimate and set up a match
*  and that became the AlphaGo versus Lysadol match in 2016.
*  And we should say, spoiler alert,
*  that AlphaGo is able to defeat Lysadol.
*  That's right, yeah.
*  So maybe we could take even a broader view.
*  AlphaGo involves both learning from expert games
*  and as far as I remember, a self-play component
*  to where it learns by playing against itself.
*  But in your sense, what was the role of learning
*  from expert games there?
*  And in terms of your self-evaluation,
*  whether you can take on the world champion,
*  what was the thing that you're trying to do more of,
*  sort of train more on expert games?
*  Or was there's now another,
*  I'm asking so many poorly phrased questions,
*  but did you ever hope or dream that self-play
*  would be the key component at that moment yet?
*  So in the early days of AlphaGo,
*  we used human data to explore the science
*  of what deep learning can achieve.
*  And so when we had our first paper that showed
*  that it was possible to predict the winner of the game,
*  that it was possible to suggest moves,
*  that was done using human data.
*  Oh, solely human data.
*  And so the reason that we did it that way was,
*  at that time we were exploring separately
*  the deep learning aspect
*  from the reinforcement learning aspect.
*  That was the part which was new and unknown to me
*  at that time, was how far could that be stretched?
*  Once we had that, it then became natural
*  to try and use that same representation
*  and see if we could learn for ourselves
*  using that same representation.
*  And so right from the beginning,
*  actually our goal had been to build a system
*  using self-play.
*  And to us, the human data right from the beginning
*  was an expedient step to help us for pragmatic reasons
*  to go faster towards the goals of the project
*  than we might be able to starting solely from self-play.
*  And so in those days, we were very aware
*  that we were choosing to use human data
*  and that might not be the long-term holy grail of AI,
*  but that it was something which was extremely useful to us.
*  It helped us to understand the system.
*  It helped us to build deep learning representations
*  which were clear and simple and easy to use.
*  And so really I would say it served a purpose,
*  not just as part of the algorithm,
*  but something which I continue to use in our research today,
*  which is trying to break down a very hard challenge
*  into pieces which are easier to understand for us
*  as researchers and develop.
*  So if you use a component based on human data,
*  it can help you to understand the system
*  such that then you can build the more principled version
*  later that does it for itself.
*  So as I said, the AlphaGo victory,
*  and I don't think I'm being sort of romanticizing
*  this notion, I think it's one of the greatest moments
*  in the history of AI.
*  So were you cognizant of this magnitude
*  of the accomplishment at the time?
*  I mean, are you cognizant of it even now?
*  Because to me, I feel like it's something that would,
*  we mentioned what the AGI systems of the future
*  will look back.
*  I think they'll look back at the AlphaGo victory as like,
*  holy crap, they figured it out.
*  This is where it started.
*  Well, thank you again.
*  I mean, it's funny, because I guess I've been working on,
*  I've been working on ComputerGo for a long time.
*  So I'd been working at the time of the AlphaGo match
*  on ComputerGo for more than a decade.
*  And throughout that decade,
*  I'd had this dream of what would it be like to,
*  what would it be like really to actually be able to
*  build a system that could play against the world champion?
*  And I imagined that that would be an interesting moment
*  that maybe some people might care about that,
*  and that this might be a nice achievement.
*  But I think when I arrived in Seoul
*  and discovered the legions of journalists
*  that were following us around,
*  and the 100 million people
*  that were watching the match online live,
*  I realized that I'd been off in my estimation
*  of how significant this moment was
*  by several orders of magnitude.
*  And so there was definitely an adjustment process
*  to realize that this was something
*  which the world really cared about,
*  and which was a watershed moment.
*  And I think there was that moment of realization,
*  which was also a little bit scary,
*  because if you go into something thinking it's gonna be
*  maybe of interest,
*  and then discover that 100 million people are watching,
*  it suddenly makes you worry about
*  whether some of the decisions you'd made
*  were really the best ones or the wisest,
*  or were going to lead to the best outcome.
*  And we knew for sure
*  that there were still imperfections in AlphaGo,
*  which were gonna be exposed to the whole world watching.
*  And so, yeah, it was, I think, a great experience,
*  and I feel privileged to have been part of it,
*  privileged to have led that amazing team.
*  I feel privileged to have been in a moment of history,
*  like you say,
*  but also lucky that, in a sense,
*  I was insulated from the knowledge of,
*  I think it would have been harder to focus on the research
*  if the full kind of reality of what was gonna come to pass
*  had been known to me and the team.
*  I think it was, we were in our bubble,
*  and we were working on research,
*  and we were trying to answer the scientific questions,
*  and then bam, the public sees it.
*  And I think it was better that way in retrospect.
*  Were you confident that,
*  I guess, what were the chances that you could get the win?
*  So, just like you said,
*  I'm a little bit more familiar with another accomplishment
*  that we may not even get a chance to talk to.
*  I talked to Oriol Vinales about AlphaStar,
*  which is another incredible accomplishment.
*  But here, with AlphaStar and beating the StarCraft,
*  there was already a track record with AlphaGo
*  and this is the really first time
*  you get to see reinforcement learning
*  face the best human in the world.
*  So what was your confidence like?
*  What was the odds?
*  Well, we actually-
*  Was there a bet?
*  Funnily enough, there was.
*  So just before the match,
*  we weren't betting on anything concrete,
*  but we all held out a hand.
*  Everyone in the team held out a hand
*  at the beginning of the match,
*  and the number of fingers that they had out on that hand
*  was supposed to represent how many games
*  they thought we would win against Lysidol.
*  And there was an amazing spread in the team's predictions,
*  but I have to say I predicted four-one.
*  And the reason was based purely on data.
*  So I'm a scientist first and foremost,
*  and one of the things which we had established
*  was that AlphaGo in around one in five games
*  would develop something which we called a delusion,
*  which was a kind of hole in its knowledge
*  where it wasn't able to fully understand
*  everything about the position,
*  and that hole in its knowledge would persist
*  for tens of moves throughout the game.
*  And we knew two things.
*  We knew that if there were no delusions,
*  that AlphaGo seemed to be playing at a level
*  that was far beyond any human capabilities,
*  but we also knew that if there were delusions,
*  the opposite was true.
*  And in fact, that's what came to pass.
*  We saw all of those outcomes,
*  and Lysidol in one of the games
*  played a really beautiful sequence
*  that AlphaGo just hadn't predicted.
*  And after that, it led it into this situation
*  where it was unable to really understand the position fully
*  and found itself in one of these delusions.
*  So indeed, yeah, four-one was the outcome.
*  So yeah, and can you maybe speak to it a little bit more?
*  What were the five games?
*  Like what happened?
*  Is there interesting things that come to memory
*  in terms of the play of the human or the machine?
*  So I remember all of these games vividly, of course.
*  Moments like these don't come too often
*  in the lifetime of a scientist.
*  And the first game was magical
*  because it was the first time
*  that a computer program had defeated a world champion
*  in this grand challenge of Go.
*  And there was a moment where AlphaGo
*  invaded Lysidol's territory towards the end of the game.
*  And that's quite an audacious thing to do.
*  It's like saying,
*  hey, you thought this was gonna be your territory
*  in the game, but I'm gonna stick a stone
*  right in the middle of it
*  and prove to you that I can break it up.
*  And Lysidol's face just dropped.
*  He wasn't expecting a computer
*  to do something that audacious.
*  The second game became famous for a move known as Move 37.
*  This was a move that was played by AlphaGo
*  that broke all of the conventions of Go,
*  that the Go players were so shocked by this.
*  They thought that maybe the operator had made a mistake.
*  They thought that there was something crazy going on.
*  And it just broke every rule that Go players are taught
*  from a very young age.
*  They're just taught this kind of move called a shoulder hit.
*  You can only play it on the third line or the fourth line.
*  And AlphaGo played it on the fifth line.
*  And it turned out to be a brilliant move
*  and made this beautiful pattern in the middle of the board
*  that ended up winning the game.
*  And so this really was a clear instance
*  where we could say computers exhibited creativity,
*  that this was really a move
*  that was something humans hadn't known about,
*  hadn't anticipated.
*  And computers discovered this idea.
*  They were the ones to say, actually, here's a new idea,
*  something new, not in the domains
*  of human knowledge of the game.
*  And now the humans think this is a reasonable thing to do
*  and it's part of Go knowledge now.
*  The third game, something special happens
*  when you play against a human world champion,
*  which again, I hadn't anticipated before going there,
*  which is, these players are amazing.
*  Lee Sedol was a true champion, 18-time world champion,
*  and had this amazing ability to probe AlphaGo
*  for weaknesses of any kind.
*  And in the third game, he was losing
*  and we felt we were sailing comfortably to victory,
*  but he managed to, from nothing, stir up this fight
*  and build what's called a double co,
*  these kind of repetitive positions.
*  And he knew that historically, no computer Go program
*  had ever been able to deal correctly
*  with double co positions.
*  And he managed to summon one out of nothing.
*  And so for us, this was a real challenge.
*  Like, would AlphaGo be able to deal with this
*  or would it just kind of crumble in the face
*  of this situation?
*  And fortunately, it dealt with it perfectly.
*  The fourth game was amazing in that Lee Sedol
*  appeared to be losing this game.
*  AlphaGo thought it was winning.
*  And then Lee Sedol did something
*  which I think only a true world champion can do,
*  which is he found a brilliant sequence
*  in the middle of the game,
*  a brilliant sequence that led him to really
*  just transform their position.
*  He found just a piece of genius, really.
*  And after that, AlphaGo, its evaluation just tumbled
*  it thought it was winning this game.
*  And all of a sudden it tumbled and said,
*  oh, now I've got no chance.
*  And it started to behave rather oddly at that point.
*  In the final game, for some reason,
*  we as a team were convinced having seen AlphaGo
*  in the previous game, suffer from delusions.
*  We as a team were convinced that it was suffering
*  from another delusion.
*  We were convinced that it was mis-evaluating the position
*  and that something was going terribly wrong.
*  And it was only in the last few moves of the game
*  that we realized that actually,
*  although it had been predicting it was gonna win
*  all the way through, it really was.
*  And so somehow, it just taught us yet again
*  that you have to have faith in your systems.
*  When they exceed your own level of ability
*  and your own judgment, you have to trust in them
*  to know better than you, the designer,
*  once you've bestowed in them the ability
*  to judge better than you can,
*  then trust the system to do so.
*  So just like in the case of Deep Blue beating Garry Kasparov,
*  so Garry was, I think, the first time he's ever lost,
*  actually, to anybody.
*  And I mean, this is a similar situation, at least at all.
*  It's a tragic loss for humans,
*  but a beautiful one, I think.
*  That's kind of, from the tragedy,
*  emerges over time, emerges a kind of inspiring story.
*  But Lisa Dahl recently announced his retirement.
*  I don't know if we can look too deeply into it,
*  but he did say that even if I become number one,
*  there's an entity that cannot be defeated.
*  So what do you think about these words?
*  What do you think about his retirement from the game ago?
*  Well, let me take you back, first of all,
*  to the first part of your comment about Garry Kasparov,
*  because actually, at the panel yesterday,
*  he specifically said that when he first lost to Deep Blue,
*  he viewed it as a failure.
*  He viewed that this had been a failure of his.
*  But later on in his career, he said he'd come to realize
*  that actually it was a success.
*  It was a success for everyone,
*  because this marked a transformational moment for AI.
*  And so even for Garry Kasparov,
*  he came to realize that that moment was pivotal
*  and actually meant something much more
*  than his personal loss in that moment.
*  Lisa Dahl, I think, was much more cognizant of that,
*  even at the time.
*  So in his closing remarks to the match,
*  he really felt very strongly that what had happened
*  in the AlphaGo match was not only meaningful for AI,
*  but for humans as well.
*  And he felt as a Go player that it had opened his horizons
*  and meant that he could start exploring new things.
*  It had brought his joy back for the game of Go,
*  because it had broken all of the conventions and barriers
*  and meant that suddenly anything was possible again.
*  And so I was sad to hear that he'd retired,
*  but he's been a great world champion over many, many years.
*  And I think he'll be remembered for that ever more.
*  He'll be remembered as the last person to beat AlphaGo.
*  I mean, after that, we increased the power of the system
*  and the next version of AlphaGo beats
*  the other strong human players 60 games to nil.
*  So what a great moment for him
*  and something to be remembered for.
*  It's interesting that you spent time at AAAI
*  on a panel with Garry Kasparov.
*  What, I mean, it's almost, I'm just curious to learn
*  the conversations you've had with Garry
*  and the, because he's also now,
*  he's written a book about artificial intelligence.
*  He's thinking about AI.
*  He has kind of a view of it.
*  And he talks about AlphaGo a lot.
*  What's your sense?
*  Arguably, I'm not just being Russian,
*  but I think Garry is the greatest chess player of all time.
*  Probably one of the greatest game players of all time.
*  And you sort of at the center of creating a system
*  that beats one of the greatest players of all time.
*  So what's that conversation like?
*  Is there anything, any interesting digs, any bets,
*  any funny things, any profound things?
*  So Garry Kasparov has an incredible respect for
*  what we did with AlphaGo.
*  And it's an amazing tribute coming from him of all people
*  that he really appreciates and respects what we've done.
*  And I think he feels that the progress
*  which has happened in computer chess,
*  which later after AlphaGo, we built the AlphaZero system,
*  which defeated the world's strongest chess programs.
*  And to Garry Kasparov, that moment in computer chess
*  was more profound than Deep Blue.
*  And the reason he believes it mattered more
*  was because it was done with learning
*  and a system which was able to discover for itself
*  new principles, new ideas,
*  which were able to play the game in a way
*  which he hadn't always known about or anyone.
*  And in fact, one of the things I discovered at this panel
*  was that the current world champion, Magnus Carlsen,
*  apparently recently commented on his improvement
*  in performance and he attributes it to AlphaZero.
*  He's been studying the games of AlphaZero
*  and he's changed his style to play more like AlphaZero.
*  And it's led to him actually increasing his rating
*  to a new peak.
*  Yeah, I guess to me, just like to Garry,
*  the inspiring thing is that,
*  and just like you said with reinforcement learning,
*  reinforcement learning and deep learning,
*  machine learning feels like what intelligence is.
*  And you could attribute it to sort of a bitter viewpoint
*  from Garry's perspective, from us humans perspective,
*  saying that pure search that IBM Deep Blue was doing
*  is not really intelligence,
*  but somehow it didn't feel like it.
*  And so that's the magical,
*  I'm not sure what it is about learning
*  that feels like intelligence, but it does.
*  So I think we should not demean the achievements
*  of what was done in previous areas of AI.
*  I think that Deep Blue was an amazing achievement in itself
*  and that heuristic search of the kind that was used
*  by Deep Blue had some powerful ideas that were in there,
*  but it also missed some things.
*  So the fact that the evaluation function,
*  the way that the chess position was understood
*  was created by humans and not by the machine
*  is a limitation, which means that there's a ceiling
*  on how well it can do, but maybe more importantly,
*  it means that the same idea cannot be applied
*  in other domains where we don't have access
*  to the kind of human grandmasters and that ability
*  to kind of encode exactly their knowledge
*  into an evaluation function.
*  And the reality is that the story of AI is that,
*  most domains turn out to be of the second type
*  where when knowledge is messy,
*  it's hard to extract from experts
*  where it isn't even available.
*  And so we need to solve problems in a different way.
*  And I think AlphaGo is a step towards solving things
*  in a way which puts learning as a first-class citizen
*  and says, systems need to understand for themselves
*  how to understand the world, how to judge the value
*  of any action that they might take within that world
*  and any state they might find themselves in.
*  And in order to do that, we make progress towards AI.
*  Yeah, so one of the nice things about this,
*  about taking a learning approach to the game of Go
*  or game playing is that the things you learn,
*  the things you figure out are actually going to be applicable
*  to other problems that are real-world problems.
*  That's sort of, that's ultimately, I mean,
*  there's two really interesting things about AlphaGo.
*  One is the science of it, just the science of learning,
*  the science of intelligence.
*  And then the other is, well, you're actually learning
*  to figuring out how to build systems
*  that would be potentially applicable in other applications,
*  medical, autonomous vehicles, robotics, all that.
*  I mean, it's just open the door
*  to all kinds of applications.
*  So the next incredible step, right,
*  really the profound step is probably AlphaGo Zero.
*  I mean, it's arguable, I kind of see them all
*  as the same place, but really,
*  and perhaps you were already thinking
*  that AlphaGo Zero is the natural,
*  it was always going to be the next step,
*  but it's removing the reliance on human expert games
*  for pre-training, as you mentioned.
*  So how big of an intellectual leap was this?
*  That self-play could achieve superhuman-level performance
*  on its own.
*  And maybe could you also say, what is self-play?
*  We kind of mentioned it a few times, but.
*  So let me start with self-play.
*  So the idea of self-play is something
*  which is really about systems learning for themselves,
*  but in the situation where there's more than one agent.
*  And so if you're in a game,
*  and a game is played between two players,
*  then self-play is really about understanding that game
*  just by playing games against yourself,
*  rather than against any actual real opponent.
*  And so it's a way to kind of discover strategies
*  without having to actually need to go out
*  and play against any particular human player, for example.
*  The main idea of Alpha Zero was really to try
*  and step back from any of the knowledge
*  that we put into the system and ask the question,
*  is it possible to come up with a single elegant principle
*  by which a system can learn for itself
*  all of the knowledge which it requires
*  to play a game such as Go?
*  Importantly, by taking knowledge out,
*  you not only make the system less brittle
*  in the sense that perhaps the knowledge
*  you were putting in was just getting in the way
*  and maybe stopping the system learning for itself,
*  but also you make it more general.
*  The more knowledge you put in,
*  the harder it is for a system to actually be placed,
*  taken out of the system in which it's kind of been designed
*  and placed in some other system
*  that maybe would need a completely different knowledge base
*  to understand and perform well.
*  And so the real goal here is to strip out
*  all of the knowledge that we put in
*  to the point that we can just plug it
*  into something totally different.
*  And that to me is really, the promise of AI
*  is that we can have systems such as that,
*  which no matter what the goal is,
*  no matter what goal we set to the system,
*  we can come up with, we have an algorithm
*  which can be placed into that world, into that environment,
*  and can succeed in achieving that goal.
*  And then that to me is almost the essence of intelligence
*  if we can achieve that.
*  And so AlphaZero is a step towards that.
*  And it's a step that was taken in the context
*  of two player perfect information games like Go and chess.
*  We also applied it to Japanese chess.
*  So just to clarify, the first step was AlphaGo Zero.
*  The first step was to try and take all of the knowledge
*  out of AlphaGo in such a way that it could play
*  in a fully self-discovered way.
*  Purely from self-play.
*  And to me, the motivation for that was always
*  that we could then plug it into other domains.
*  But we saved that until later.
*  Well, in fact, I mean, just for fun,
*  I could tell you exactly the moment
*  where the idea for AlphaZero occurred to me,
*  because I think there's maybe a lesson there
*  for researchers who are kind of too deeply embedded
*  in their research and working 24 sevens
*  to try and come up with the next idea.
*  Which is, it actually occurred to me on honeymoon.
*  And I was like at my most fully relaxed state,
*  really enjoying myself and just being this,
*  like the algorithm for AlphaZero just appeared.
*  And in its full form.
*  And this was actually before we played against Lisa Doll.
*  But we just didn't, I think we were so busy
*  trying to make sure we could beat the world champion,
*  that it was only later that we had the opportunity
*  to step back and start examining that sort of
*  deeper scientific question of whether
*  this could really work.
*  So, nevertheless, so self-play is probably
*  one of the most sort of profound ideas
*  that it represents, to me at least,
*  artificial intelligence.
*  But the fact that you could use that kind of mechanism
*  to, again, beat world-class players,
*  that's very surprising.
*  So we kind of, to me, it feels like you have to train
*  in a large number of expert games.
*  So was it surprising to you?
*  What was the intuition?
*  Can you sort of think, not necessarily,
*  at that time even now, what's your intuition?
*  Why this thing works so well?
*  Why it's able to learn from scratch?
*  Well, let me first say why we tried it.
*  So we tried it both because I feel that
*  it was the deeper scientific question to be asking
*  to make progress towards AI,
*  and also because, in general, in my research,
*  I don't like to do research on questions
*  for which we already know the likely outcome.
*  I don't see much value in running an experiment
*  where you're 95% confident that you will succeed.
*  And so we could have tried, you know,
*  maybe to take AlphaGo and do something
*  which we knew for sure it would succeed on.
*  But much more interesting to me was to try it
*  on the things which we weren't sure about.
*  And one of the big questions on our minds back then was,
*  you know, could you really do this with self-play alone?
*  How far could that go?
*  Would it be as strong?
*  And honestly, we weren't sure.
*  Yeah, it was 50-50, I think.
*  If you'd asked me, I wasn't confident
*  that it could reach the same level as these systems,
*  but it felt like the right question to ask.
*  And even if it had not achieved the same level,
*  I felt that that was an important direction to be studying.
*  And so then, lo and behold,
*  it actually ended up outperforming
*  the previous version of AlphaGo
*  and indeed was able to beat it by 100 games to zero.
*  So what's the intuition as to why?
*  I think the intuition to me is clear
*  that whenever you have errors in a system,
*  as we did in AlphaGo,
*  AlphaGo suffered from these delusions.
*  Occasionally, it would misunderstand
*  what was going on in a position and mis-evaluate it.
*  How can you remove all of these errors?
*  Errors arise from many sources.
*  For us, they were arising both from, you know,
*  starting from the human data,
*  but also from the nature of the search
*  and the nature of the algorithm itself.
*  But the only way to address them in any complex system
*  is to give the system the ability to correct its own errors.
*  It must be able to correct them.
*  It must be able to learn for itself
*  when it's doing something wrong and correct for it.
*  And so it seemed to me that the way to correct delusions
*  was indeed to have more iterations
*  of reinforcement learning, that, you know,
*  no matter where you start,
*  you should be able to correct those errors
*  until it gets to play that out
*  and understand, oh, well,
*  I thought that I was gonna win in this situation,
*  but then I ended up losing.
*  That suggests that I was mis-evaluating something
*  and there's a hole in my knowledge
*  and now the system can correct for itself
*  and understand how to do better.
*  Now, if you take that same idea
*  and trace it back all the way to the beginning,
*  it should be able to take you from no knowledge,
*  from completely random starting point,
*  all the way to the highest levels of knowledge
*  that you can achieve in a domain.
*  And the principle is the same,
*  that if you bestow a system with the ability
*  to correct its own errors,
*  then it can take you from random
*  to something slightly better than random
*  because it sees the stupid things that the random is doing
*  and it can correct them.
*  And then it can take you from that slightly better system
*  and understand, well, what's that doing wrong?
*  And it takes you onto the next level and the next level.
*  And this progress can go on indefinitely.
*  And indeed, you know, what would have happened
*  if we'd carried on training AlphaGo Zero for longer,
*  we saw no sign of it slowing down its improvements,
*  or at least it was certainly carrying on to improve.
*  And presumably, if you had the computational resources,
*  this could lead to better and better systems
*  that discover more and more.
*  So your intuition is fundamentally
*  there's not a ceiling to this process.
*  One of the surprising things, just like you said,
*  is the process of patching errors.
*  It intuitively makes sense.
*  This is, reinforcement learning
*  should be part of that process.
*  But what is surprising is in the process of patching
*  your own lack of knowledge,
*  you don't open up other patches.
*  You keep sort of, like there's a monotonic decrease
*  of your weaknesses.
*  Well, let me back this up.
*  You know, I think science always should make
*  falsifiable hypotheses.
*  Yes.
*  Let me back up this claim with a falsifiable hypothesis,
*  which is that if someone was to, in the future,
*  take AlphaZero as an algorithm and run it
*  with greater computational resources
*  that we had available today,
*  then I would predict that they would be able
*  to beat the previous system 100 games to zero.
*  And that if they were then to do the same thing
*  a couple of years later,
*  that that would beat that previous system
*  100 games to zero.
*  And that that process would continue indefinitely
*  throughout at least my human lifetime.
*  Presumably the game of Go would set the ceiling.
*  I mean-
*  The game of Go would set the ceiling,
*  but the game of Go has 10 to the 170 states in it.
*  So the ceiling is unreachable by any computational device
*  that can be built out of the, you know,
*  10 to the 80 atoms in the universe.
*  You asked a really good question, which is, you know,
*  do you not open up other errors
*  when you correct your previous ones?
*  And the answer is, yes, you do.
*  And so it's a remarkable fact about this class
*  of two-player game and also true of single agent games,
*  that essentially progress will always lead you to,
*  if you have sufficient representational resource,
*  like imagine you had, could represent every state
*  in a big table of the game,
*  then we know for sure that a progress of self-improvement
*  will lead all the way in the single agent case
*  to the optimal possible behavior.
*  And in the two-player case to the minimax optimal behavior,
*  that is the best way that I can play,
*  knowing that you're playing perfectly against me.
*  And so for those cases, we know that even if you do
*  open up some new error,
*  that in some sense you've made progress.
*  You're progressing towards the best that can be done.
*  So AlphaGo was initially trained on expert games
*  with some self-play.
*  AlphaGo Zero removed the need to be trained on expert games.
*  And then another incredible step for me,
*  because I just love chess,
*  is to generalize that further to be in AlphaZero
*  to be able to play the game of Go,
*  beating AlphaGo Zero in AlphaGo,
*  and then also being able to play the game of chess and others.
*  So what was that step like?
*  What's the interesting aspects there
*  that required to make that happen?
*  I think the remarkable observation,
*  which we saw with AlphaZero,
*  was that actually without modifying the algorithm at all,
*  it was able to play and crack
*  some of AI's greatest previous challenges.
*  In particular, we dropped it into the game of chess.
*  And unlike the previous systems like Deep Blue,
*  which had been worked on for years and years,
*  and we were able to beat
*  the world's strongest computer chess program convincingly
*  using a system that was fully discovered by its own,
*  from scratch with its own principles.
*  And in fact, one of the nice things that we found
*  was that in fact, we also achieved the same result
*  in Japanese chess, a variant of chess
*  where you get to capture pieces
*  and then place them back down on your own side
*  as an extra piece.
*  So a much more complicated variant of chess.
*  And we also beat the world's strongest programs
*  and reached superhuman performance in that game too.
*  And it was the very first time
*  that we'd ever run the system on that particular game
*  was the version that we published
*  in the paper on AlphaZero.
*  It just worked out of the box, literally, no touching it.
*  We didn't have to do anything.
*  And there it was, superhuman performance,
*  no tweaking, no twiddling.
*  And so I think there's something beautiful
*  about that principle that you can take an algorithm
*  and without twiddling anything, it just works.
*  Now, to go beyond AlphaZero, what's required?
*  AlphaZero is just a step.
*  And there's a long way to go beyond that
*  to really crack the deep problems of AI.
*  But one of the important steps is to acknowledge
*  that the world is a really messy place.
*  It's this rich, complex, beautiful,
*  but messy environment that we live in.
*  And no one gives us the rules.
*  Like no one knows the rules of the world.
*  At least maybe we understand that it operates
*  according to Newtonian or quantum mechanics
*  at the micro level or according to relativity
*  at the macro level.
*  But that's not a model that's useful for us as people
*  to operate in it.
*  Somehow the agent needs to understand the world for itself
*  in a way where no one tells it the rules of the game.
*  And yet it can still figure out what to do in that world,
*  deal with this stream of observations coming in,
*  rich sensory input coming in,
*  actions going out in a way that allows it to reason
*  in the way that AlphaGo or AlphaZero can reason
*  in the way that these Go and chess playing programs
*  can reason.
*  But in a way that allows it to take actions
*  in that messy world to achieve its goals.
*  And so this led us to the most recent step
*  in the story of AlphaGo,
*  which was a system called MuZero.
*  And MuZero is a system which learns for itself,
*  even when the rules are not given to it.
*  It actually can be dropped into a system
*  with messy perceptual inputs.
*  We actually tried it in some Atari games,
*  the canonical domains of Atari
*  that have been used for reinforcement learning.
*  And this system learned to build a model
*  of these Atari games that were sufficiently rich
*  and useful enough for it to be able to plan successfully.
*  And in fact, that system not only went on
*  to beat the state of the art in Atari,
*  but the same system without modification
*  was able to reach the same level of superhuman performance
*  in Go, chess and Shogi that we'd seen in AlphaZero,
*  showing that even without the rules,
*  the system can learn for itself just by trial and error,
*  just by playing this game of Go.
*  And no one tells you what the rules are,
*  but you just get to the end and someone says,
*  win or loss.
*  You play this game of chess and someone says win or loss,
*  or you play a game of breakout in Atari
*  and someone just tells you your score at the end.
*  And the system for itself figures out
*  essentially the rules of the system,
*  the dynamics of the world, how the world works.
*  And not in any explicit way, but just implicitly
*  enough understanding for it to be able to plan
*  in that system in order to achieve its goals.
*  And that's the fundamental process
*  that you have to go through when you're facing
*  in any uncertain kind of environment
*  that you would in the real world,
*  is figuring out the sort of the rules,
*  the basic rules of the game.
*  That's right.
*  So I mean, yeah, that allows it to be applicable
*  to basically any domain that could be digitized
*  in the way that it needs to in order to be consumable,
*  sort of in order for the reinforcement learning framework
*  to be able to sense the environment,
*  to be able to act in the environment and so on.
*  The full reinforcement learning problem
*  needs to deal with worlds that are unknown and complex
*  and the agent needs to learn for itself
*  how to deal with that.
*  And so Mu Zero is a step, a further step in that direction.
*  One of the things that inspired the general public
*  and just in conversations I have like with my parents
*  or something with my mom that just loves what was done
*  is kind of at least the notion
*  that there was some display of creativity,
*  some new strategies, new behaviors that were created
*  that again has echoes of intelligence.
*  So is there something that stands up?
*  Do you see it the same way that there's creativity
*  and there's some behaviors, patterns that you saw
*  that Alpha Zero was able to display?
*  That are truly creative?
*  So let me start by saying that I think we should ask
*  what creativity really means.
*  So to me, creativity means discovering something
*  which wasn't known before, something unexpected,
*  something outside of our norms.
*  And so in that sense, the process of reinforcement learning
*  or the self-play approach that was used by Alpha Zero
*  is the essence of creativity.
*  It's really saying at every stage,
*  you're playing according to your current norms
*  and you try something and if it works out, you say,
*  hey, here's something great, I'm gonna start using that.
*  And then that process, it's like a micro discovery
*  that happens millions and millions of times
*  over the course of the algorithm's life
*  where it just discovers some new idea,
*  this pattern's working really well for me,
*  I'm gonna start using that.
*  And now, oh, here's this other thing I can do,
*  I can start to connect these stones together in this way
*  or I can start to sacrifice stones or give up on pieces
*  or play shoulder hits on the fifth line or whatever it is.
*  The system's discovering things like this for itself
*  continually, repeatedly, all the time.
*  And so it should come as no surprise to us then
*  when if you leave these systems going,
*  that they discover things that are not known to humans,
*  to the human norms are considered creative.
*  And we've seen this several times.
*  In fact, in AlphaGo Zero,
*  we saw this beautiful timeline of discovery
*  where what we saw was that there are these opening patterns
*  that humans play called joseki,
*  these are like the patterns that humans learn to play
*  in the corners and they've been developed and refined
*  over literally thousands of years in the game of Go.
*  And what we saw was in the course of the training,
*  AlphaGo Zero, over the course of the 40 days
*  that we trained this system,
*  it starts to discover exactly these patterns
*  that human players play.
*  And over time, we found that all of the joseki
*  that humans played were discovered by the system
*  through this process of self-play
*  and this sort of essential notion of creativity.
*  But what was really interesting was that over time,
*  it then starts to discard some of these
*  in favor of its own joseki that humans didn't know about.
*  And it starts to say,
*  oh, well, you thought that the Knights move
*  pinta joseki was a great idea,
*  but here's something different you can do there,
*  which makes some new variation
*  that humans didn't know about.
*  And actually now the human Go players study the joseki
*  that AlphaGo played and they become the new norms
*  that are used in today's top level Go competitions.
*  That never gets old.
*  Even just the first to me,
*  maybe just makes me feel good as a human being
*  that a self-play mechanism that knows nothing about us humans
*  discovers patterns that we humans do.
*  That's a kind of affirmation that we're doing okay as humans.
*  Yeah.
*  In this domain and other domains, we figured out,
*  it's like the Churchill quote about democracy.
*  It's the, you know, it sucks,
*  but it's the best song we've tried.
*  So in general, taking a step outside of Go
*  and you have like a million accomplishments
*  that have no time to talk about with AlphaStar and so on
*  and the current work, but in general,
*  this self-play mechanism that you've inspired the world with
*  by beating the world champion Go player.
*  Do you see that as,
*  do you see it being applied in other domains?
*  Do you have sort of dreams and hopes that it's applied
*  in both the simulated environments
*  and the constrained environments of games, constrained?
*  I mean, AlphaStar really demonstrates
*  that you can remove a lot of the constraints,
*  but nevertheless, it's in a digital simulated environment.
*  Do you have a hope, a dream that it starts being applied
*  in the robotics environment
*  and maybe even in domains that are safety critical and so on
*  and have a real impact in the real world,
*  like autonomous vehicles, for example,
*  which seems like a very far out dream at this point?
*  So I absolutely do hope and imagine that we will
*  get to the point where ideas just like these are used
*  in all kinds of different domains.
*  In fact, one of the most satisfying things as a researcher
*  is when you start to see other people use your algorithms
*  in unexpected ways.
*  So in the last couple of years, there have been
*  a couple of nature papers where different teams
*  unbeknownst to us took AlphaZero
*  and applied exactly those same algorithms and ideas
*  to real world problems of huge meaning to society.
*  So one of them was the problem of chemical synthesis
*  and they were able to beat the state of the art
*  in finding pathways of how to actually synthesize chemicals,
*  retrochemical synthesis.
*  And the second paper actually just came out
*  a couple of weeks ago in nature showed that
*  in quantum computation, one of the big questions
*  is how to understand the nature of the function
*  in quantum computation and a system based on AlphaZero
*  beat the state of the art by quite some distance there again.
*  So these are just examples and I think that the lesson
*  which we've seen elsewhere in machine learning
*  time and time again is that if you make something general,
*  it will be used in all kinds of ways.
*  You provide a really powerful tool to society
*  and those tools can be used in amazing ways.
*  And so I think we're just at the beginning
*  and for sure I hope that we see all kinds of outcomes.
*  So the other side of the question of reinforcement
*  learning framework is you usually want to specify
*  a reward function and an objective function.
*  What do you think about sort of ideas
*  of intrinsic rewards and when we're not really sure about,
*  if we take human beings as existence proof
*  that we don't seem to be operating
*  according to a single reward,
*  do you think that there's interesting ideas
*  for when you don't know how to truly specify the reward
*  that there's some flexibility for discovering it intrinsically
*  or so on in the context of reinforcement learning?
*  So I think when we think about intelligence,
*  it's really important to be clear
*  about the problem of intelligence.
*  And I think it's clearest to understand that problem
*  in terms of some ultimate goal
*  that we want the system to try and solve for.
*  And after all, if we don't understand the ultimate purpose
*  of the system, do we really even have a clearly defined
*  problem that we're solving at all?
*  Now, within that, as with your example for humans,
*  the system may choose to create its own motivations
*  and sub goals that help the system
*  to achieve its ultimate goal.
*  And that may indeed be a hugely important mechanism
*  to achieve those ultimate goals,
*  but there is still some ultimate goal
*  I think the system needs to be measurable
*  and evaluated against.
*  And even for humans,
*  I mean, humans, we're incredibly flexible.
*  We feel that we can, any goal that we're given,
*  we feel we can master to some degree.
*  But if we think of those goals, really,
*  like the goal of being able to pick up an object
*  or the goal of being able to communicate
*  or influence people to do things in a particular way
*  or whatever those goals are, really, they are,
*  they're sub goals really that we set ourselves.
*  We choose to pick up the object.
*  We choose to communicate.
*  We choose to influence someone else.
*  And we choose those because we think it will lead us
*  to something in later on.
*  We think that that's helpful to us
*  to achieve some ultimate goal.
*  Now, I don't want to speculate whether or not humans
*  as a system necessarily have a singular overall goal
*  of survival or whatever it is,
*  but I think the principle for understanding
*  and implementing intelligence is, has to be
*  if we're trying to understand intelligence
*  or implement our own,
*  there has to be a well-defined problem.
*  Otherwise, if it's not, I think it's like
*  an admission of defeat.
*  That for there to be hope for understanding
*  or implementing intelligence,
*  we have to know what we're doing.
*  We have to know what we're asking the system to do.
*  Otherwise, if you don't have a clearly defined purpose,
*  you're not gonna get a clearly defined answer.
*  The ridiculous big question that has to naturally follow
*  because I have to pin you down on this thing
*  that nevertheless one of the big silly
*  or big real questions before humans is the meaning of life.
*  Is us trying to figure out our own reward function.
*  And you just kind of mentioned that if you want to build
*  intelligent systems and you know what you're doing,
*  you should be at least cognizant to some degree
*  of what the reward function is.
*  So the natural question is,
*  what do you think is the reward function of human life?
*  What is the meaning of life for us humans?
*  The meaning of our existence?
*  I think I'd be speculating beyond my own expertise,
*  but just for fun, let me do that.
*  Yes, please.
*  And say, I think that there are many levels
*  at which you can understand the system
*  and you can understand something as optimizing
*  for a goal at many levels.
*  And so you can understand the,
*  let's start with the universe.
*  What's the purpose?
*  Well, it feels like it's just at one level,
*  just following certain mechanical laws of physics
*  and that that's led to the development of the universe.
*  But at another level, you can view it as actually
*  there's the second law of thermodynamics
*  that says that this is increasing in entropy
*  over time forever.
*  And now there's a view that's been developed
*  by certain people at MIT that this,
*  you can think of this as almost like a goal of the universe,
*  that the purpose of the universe is to maximize entropy.
*  So there are multiple levels
*  at which you can understand a system.
*  The next level down, you might say, well,
*  if the goal is to maximize entropy, well,
*  how can that be done by a particular system?
*  And maybe evolution is something that the universe
*  discovered in order to kind of dissipate energy
*  as efficiently as possible.
*  And by the way, I'm borrowing from Max Tegmark
*  for some of these metaphors, the physicist.
*  But if you can think of evolution as a mechanism
*  for dispersing energy, then evolution,
*  you might say, then becomes a goal,
*  which is if evolution disperses energy
*  by reproducing as efficiently as possible,
*  what's evolution then?
*  Well, it's now got its own goal within that,
*  which is to actually reproduce as effectively as possible.
*  And now how does reproduction,
*  how is that made as effective as possible?
*  Well, you need entities within that
*  that can survive and reproduce as effectively as possible.
*  And so it's natural that in order to achieve
*  that high level goal, those individual organisms
*  discover brains, intelligences,
*  which enable them to support the goals of evolution.
*  And those brains, what do they do?
*  Well, perhaps the early brains,
*  maybe they were controlling things at some direct level.
*  Maybe they were the equivalent of pre-programmed systems,
*  which were directly controlling what was going on
*  and setting certain things in order to achieve
*  these particular goals.
*  But that led to another level of discovery,
*  which was learning systems, parts of the brain
*  which were able to learn for themselves
*  and learn how to program themselves to achieve any goal.
*  And presumably there are parts of the brain
*  where goals are set to parts of that system
*  and provides this very flexible notion of intelligence
*  that we as humans presumably have,
*  which is the ability to kind of,
*  why the reason we feel that we can achieve any goal.
*  So it's a very long-winded answer to say that,
*  I think there are many perspectives
*  and many levels at which intelligence can be understood.
*  And at each of those levels,
*  you can take multiple perspectives.
*  You can view the system as something
*  which is optimizing for a goal,
*  which is understanding it at a level
*  by which we can maybe implement it
*  and understand it as AI researchers or computer scientists,
*  or you can understand it at the level
*  of the mechanistic thing which is going on,
*  that there are these atoms bouncing around in the brain
*  and they lead to the outcome of that system.
*  It's not in contradiction with the fact
*  that it's also a decision-making system
*  that's optimizing for some goal and purpose.
*  I've never heard the description of the meaning of life,
*  structured so beautifully in layers,
*  but you did miss one layer, which is the next step,
*  which you're responsible for,
*  which is creating the artificial intelligence layer
*  on top of that.
*  And I can't wait to see, well, I may not be around,
*  but I can't wait to see what the next layer beyond that.
*  Well, let's just take that argument
*  and pursue it to its natural conclusion.
*  So the next level indeed is for,
*  how can our learning brain achieve its goals
*  most effectively?
*  Well, maybe it does so by us as learning beings,
*  building a system which is able to solve for those goals
*  more effectively than we can.
*  And so when we build a system to play the game of Go,
*  when I said that I wanted to build a system
*  that can play Go better than I can,
*  I've enabled myself to achieve that goal of playing Go
*  better than I could by directly playing it
*  and learning it myself.
*  And so now a new layer has been created,
*  which is systems which are able to achieve goals
*  for themselves.
*  And ultimately there may be layers beyond that
*  where they set sub goals to parts of their own system
*  in order to achieve those and so forth.
*  It's incredible.
*  So the story of intelligence, I think,
*  is a multi-layered one and a multi-perspective one.
*  We live in an incredible universe.
*  Thank you, David.
*  Thank you so much, first of all,
*  for dreaming of using learning to solve Go
*  and building intelligent systems
*  and for actually making it happen
*  and for inspiring millions of people in the process.
*  It's truly an honor.
*  Thank you so much for talking today.
*  Okay, thank you.
*  Thanks for listening to this conversation with David Silver
*  and thank you to our sponsors, Masterclass and Cash App.
*  Please consider supporting the podcast by signing up
*  to Masterclass at masterclass.com slash Lex
*  and downloading Cash App and using code Lexpodcast.
*  If you enjoy this podcast, subscribe on YouTube,
*  review it with five stars on Apple Podcast,
*  support on Patreon, or simply connect with me on Twitter
*  at Lex Friedman.
*  And now let me leave you with some words from David Silver.
*  My personal belief is that we've seen something
*  of a turning point where we're starting to understand
*  that many abilities like intuition and creativity
*  that we've previously thought were in the domain
*  only of the human mind are actually accessible
*  to machine intelligence as well.
*  And I think that's a really exciting moment in history.
*  Thank you for listening and hope to see you next time.