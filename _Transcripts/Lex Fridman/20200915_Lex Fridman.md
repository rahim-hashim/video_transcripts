---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 15818s
Video Keywords: ['stephen wolfram', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 469595
Video Rating: None
---

# Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe | Lex Fridman Podcast #124
**Lex Fridman:** [September 15, 2020](https://www.youtube.com/watch?v=-t1_ffaFXao)
*  The following is a conversation with Stephen Wolfram, his second time on the podcast.
*  He's a computer scientist, mathematician, theoretical physicist, and the founder and CEO of Wolfram Research,
*  a company behind Mathematica, Wolfram Alpha, Wolfram Language, and the new Wolfram Physics project.
*  He's the author of several books, including A New Kind of Science and the new book, A Project to Find the Fundamental Theory of Physics.
*  This second round of our conversation is primarily focused on this latter endeavor
*  of searching for the physics of our universe in simple rules that do their work on hypographs
*  and eventually generate the infrastructure from which space, time, and all of modern physics can emerge.
*  Quick summary of the sponsors, Simply Safe, Sun Basket, and Masterclass.
*  Please check out these sponsors in the description to get a discount and to support this podcast.
*  As a side note, let me say that to me, the idea that seemingly infinite complexity can arise
*  from very simple rules and initial conditions is one of the most beautiful and important
*  mathematical and philosophical mysteries in science. I find that both cellular automata
*  and the hypograph data structure that Stephen and team are currently working on to be the kind of
*  simple clear mathematical playground within which fundamental ideas about intelligence,
*  consciousness, and the fundamental laws of physics can be further developed in totally new ways.
*  In fact, I think I'll try to make a video or two about the most beautiful aspects of these models
*  in the coming weeks, especially I think trying to describe how fellow curious minds like myself can
*  jump in and explore them either just for fun or potentially for publication of new innovative
*  research in math, computer science, and physics. But honestly, I think the emerging complexity in
*  these type of graphs can capture the imagination of everyone, even if you're someone who never
*  really connected with mathematics. That's my hope at least, to have these conversations that inspire
*  everyone to look up to the skies and into our own minds in awe of our amazing universe.
*  Let me also mention that this is the first time I ever recorded a podcast outdoors as a kind of
*  experiment to see if this is an option in times of COVID. I'm sorry if the audio is not great.
*  I did my best and promise to keep improving and learning as always. If you enjoy this thing,
*  subscribe on YouTube, review it with Fast Stars and Apple Podcasts, follow on Spotify,
*  support on Patreon, or connect with me on Twitter at Lex Friedman. As usual, I'll do a few minutes
*  of ads now and no ads in the middle. I tried to make these interesting, but I do give you timestamps,
*  so you're welcome to skip. But still, please do check out the sponsors by clicking the links in
*  the description. It's the best way to support this podcast. Also, let me say, even though I'm
*  talking way too much, that I did a survey and it seems like over 90% of people either enjoy these
*  ad reads somehow magically, or don't mind them at least. That honestly just warms my heart that
*  people are that supportive. This show is sponsored by SimpliSafe, a home security company. Go to
*  SimpliSafe.com to get a free HD camera. It's simple, no contracts, 15 bucks a month, easy setup.
*  Even I figured it out. I have it set up in my apartment. Of course, I also welcome intruders.
*  One of my favorite movies is Leon or The Professional with Jean Renau, Gary Oldman,
*  and the brilliant young Natalie Portman. If you haven't seen the movie, he's a hitman with a
*  minimalist life that resembles my own. In fact, when I was younger, the idea of being a hitman
*  or targeting evil in a skilled way, which is how I thought about it, really appealed to me.
*  The skill of it, the planning, the craftsmanship. In another life, perhaps, if I didn't love
*  engineering and science so much, I could see myself being something like a Navy SEAL.
*  In general, I love the idea of serving my country, of serving society by contributing my skill in
*  some small way. Anyway, go to SimpliSafe.com slash Lex to get a free HD camera and to support this
*  podcast. They're a new sponsor, and this is a trial run, so you know what to do. This show is
*  also sponsored by Sun Basket, a meal delivery service. Visit sunbasket.com slash Lex and use
*  code Lex to get $30 off your order and to support this podcast. This is the last read of the trial
*  they're doing, so this is the time to get them if you're considering it. And if you do, it'll help
*  ensure that they decide to support this podcast long term. Their meals are healthy and delicious.
*  A nice break from the minimalist meals of meat and vegetables that I usually eat. Maybe on a
*  personal note, one of my favorite things to do is watch people cook, especially people who love
*  cooking, and hang out with people over amazing meals. I still tend to be strict in my diet,
*  no matter what, even in fancy restaurants, but it brings me joy to see friends and family indulge
*  something like a cake that has way too many calories or ice cream or whatever. My mom,
*  in fact, for much of my life made this cake called an anthill on my birthday that brings
*  me a lot of joy and way too many calories. I was thinking of doing a video with my mom
*  as she makes it. I thought it'd be a fun thing to do together. Anyway, go to sunbasket.com slash
*  Lex and use code Lex. Do it now so they sign a long term contract with this podcast. This show
*  is also sponsored by Masterclass. Sign up at masterclass.com slash Lex. 180 bucks a year,
*  you get an all access pass to watch lessons from Chris Hadfield, Neil deGrasse Tyson, Tony Hawk,
*  Carlos Santana, Garret Kasparov, Daniel Nagano, and many more brilliant world experts.
*  Masterclass has been a really special sponsor. They believe in this podcast in a way that gives
*  me strength and motivation to take intellectual risks. I'm thinking of doing a few solo podcasts,
*  episodes on difficult topics, especially in history, like the rise and fall of the Third Reich,
*  or Stalin, Putin, and many other difficult topics that I'm fascinated by. I have a worldview that
*  seeks inspiring positive insights, even and perhaps especially from periods of tragedy and evil
*  that perhaps some folks may find value in if I can only learn to convey the ideas in my mind
*  as clearly as I think them. I think deeply and rigorously and precisely, but to be honest,
*  have trouble speaking in a way that reflects that rigor of thought. So it really doesn't mean a lot
*  the love and support I get as I try to get better at this thing, at this talking thing. Anyway,
*  go to masterclass.com slash Lex to get a discount and to support this podcast.
*  And now finally, here's my conversation with Stephen Wolfram.
*  You said that there are moments in history of physics and maybe mathematical physics or
*  even mathematics where breakthroughs happen and then a flurry of progress follows.
*  So if you look back through the history of physics, what moments stand out to you as
*  important such breakthroughs where a flurry of progress follows?
*  So the big famous one was 1920s, the invention of quantum mechanics,
*  where, you know, in about five or 10 years, lots of stuff got figured out.
*  That's now quantum mechanics. Can you mention the people involved?
*  Yeah, it was kind of the Schrodinger, Heisenberg, you know, Einstein had been a key figure,
*  originally Planck, then Dirac was a little bit later. That was something that happened at that
*  time. That's sort of before my time, right? In my time was in the 1970s. There was this sort of
*  realization that quantum field theory was actually going to be useful in physics.
*  And QCD, quantum chromatodynamics theory of quarks and gluons and so on, was really getting started.
*  And there was again sort of big flurry of things happened then. I happened to be a teenager at that
*  time and happened to be really involved in physics. And so I got to be part of that,
*  which was really cool. Who were the key figures aside from your
*  young selves at that time? You know, who won the Nobel Prize for QCD?
*  Okay, people David Gross, Frank Wilczek, you know, David Politzer, the people who are the sort of the
*  slightly older generation, Dick Feynman, Murray Gell-Mann, people like that, who were Steve
*  Weinberg, Gerhard Hoft, he's younger. He's in the younger group, actually. But these are all
*  characters who were involved. I mean, it's funny because those are all people who are kind of in
*  my time and I know them. And they don't seem like sort of these historical, you know, iconic figures.
*  They seem more like everyday characters, so to speak. And so it's always, you know, when you look
*  at history from long afterwards, it always seems like everything happened instantly.
*  And that's usually not the case. There was usually a long buildup. But usually there's, you know,
*  there's some methodological thing happens. And then there's a whole bunch of low hanging fruit
*  to be picked. And that usually lasts five or 10 years. You know, we see it today with machine
*  learning and, you know, deep learning neural nets and so on, you know, methodological advance,
*  things actually started working in, you know, 2011, 2012 and so on. And, you know, there's been
*  this sort of rapid picking of low hanging fruit, which is probably, you know, some significant
*  fraction of the way, way done, so to speak. Do you think there's a key moment? Like if I had to
*  really introspect, like what was the key moment for the deep learning, quote unquote, revolution?
*  I mean, it's probably the Alex net business. Alex net with image net. So is there something like
*  that with physics where so deep learning neural networks have been around for a long time?
*  Absolutely. In the 1940s. Yeah. There's a bunch of little pieces that came together and then
*  all of a sudden everybody's eyes lit up like, wow, there's something here. Like even just looking at
*  your own work, just your thinking about the universe, that there's simple rules can create
*  complexity. You know, at which point was there a thing where your eyes light up? It's like, wait a
*  minute, there's something here. Is it the very first idea or is it some moment along the line
*  of implementations and experiments? There's a couple of different stages to this. I mean, one is
*  the think about the world computationally, you know, can we use programs instead of equations to
*  make models of the world? That's something that I got interested in in the beginning of the 1980s.
*  You know, I did a bunch of computer experiments. You know, when I first did them, I didn't really,
*  I could see some significance to them, but it took me a few years to really say, wow, there's a big
*  important phenomenon here that lets sort of complex things arise from very simple programs.
*  That kind of happened back in 1984 or so. Then, you know, a bunch of other years go by, then I
*  start actually doing a lot of much more systematic computer experiments and things and find out that
*  the, you know, this phenomenon that I could only have said occurs in one particular case is actually
*  something incredibly general. And then that led me to this thing called principle of computational
*  equivalence. And that was a long story. And then, you know, as part of that process, I was like,
*  okay, you can make simple programs can make models of complicated things. What about the whole
*  universe? That's our sort of ultimate example of a complicated thing. And so I got to thinking,
*  you know, could we use these ideas to study fundamental physics? You know, I happened to
*  know a lot about, you know, traditional fundamental physics. My first, you know, I had a bunch of ideas
*  about how to do this in the early 1990s. I made a bunch of technical progress. I figured out a bunch
*  of things I thought were pretty interesting. You know, I wrote about them back in 2002.
*  With the new kind of science and the cellular automata world and right there's echoes in the
*  cellular automata world with your new Wolfram physics project or we'll get to all that. Allow me to
*  sort of romanticize a little more on the philosophy of science. So Thomas Kuhn, philosopher of science
*  describes that, you know, the progress in science is made with these paradigm shifts. And so to
*  link on the sort of original line of discussion, do you agree with this view that there is
*  revolutions in science that just kind of flip the table? What happens is it's a different way
*  of thinking about things. It's a different methodology for studying things and that opens
*  stuff up. This is this idea of, uh, he's a famous biographer, but I think it's called the innovators,
*  the biographer of Steve Jobs, of Albert Einstein. He also wrote a book. I think it's called the
*  innovators where he discusses, uh, how a lot of, uh, the innovations in the history of computing
*  has been done by groups. There's a complicated group dynamic going on, but there's also a
*  romanticized notion that the individual is at the core of the revolution. Like where does your sense
*  fall is, is, um, ultimately like one person responsible for these revolutions that
*  they create the spark or one or two, whatever, but, or is it just the big mush and mess and chaos of,
*  of people interacting, a personality is interacting. I think it ends up being like many things,
*  there's leadership and there ends up being, it's a lot easier for one person to have a crisp new
*  idea than it is for a big committee to have a crisp new idea. And, um, I think, you know, but I
*  think it can happen that, you know, you have a great idea, but the world isn't ready for you for
*  it. And, um, you know, you can, you can, I mean, this has happened to me plenty, right? It's, you
*  know, you have an idea, it's actually a pretty good idea, but things aren't ready either, either
*  you're not really ready for it or the ambient world isn't ready for it. And it's hard to get
*  the thing to get traction. It's kind of interesting. I mean, when I look at a new kind of science,
*  you're now living inside the history. So you can't tell the story of these decades, but it seems
*  like the new kind of science has not had the revolutionary impact. I would think it, uh, might
*  like, it feels like at some point, of course it might be, but it feels at some point,
*  people will return to that book and say, that was something special here. This was incredible.
*  What happened? Or do you think that's already happened? Oh yeah, it's happened, except that
*  people aren't, you know, the, the sort of the heroism of it may not be there, but the what's
*  happened is for 300 years, people basically said, if you want to make a model of things in the world,
*  mathematical equations are the best place to go. Last 15 years doesn't happen. You know, new models
*  that get made of things most often are made with programs, not with equations. Now, you know,
*  was that sort of going to happen anyway? Was that a consequence of, you know, my particular work and
*  my particular book? It's hard to know for sure. I mean, I am always amazed at the amounts of feedback
*  that I get from people where they say, Oh, by the way, you know, I started doing this whole line of
*  research because I read your book, blah, blah, blah, blah, blah. It's like, well, can you tell
*  that from the academic literature? You know, whether was there a chain of academic references?
*  Probably not. One of the interesting side effects of publishing in the way you did this tome is it
*  serves as an education tool and an inspiration to hundreds of thousands of millions of people.
*  But because it's not a single, it's not a chain of papers with piffy titles. It doesn't create
*  a splash of citations. It's had plenty of citations, but it's, it's, you know, I think that the,
*  people think of it as probably more, you know, conceptual inspiration than, than kind of a,
*  you know, this is a line from here to here to here in our particular field. I think that the,
*  you know, the thing which I am disappointed by, and which will eventually happen is this kind of
*  study of the, the sort of pure computationalism, this kind of study of the abstract behavior of the
*  computational universe. That should be a big thing that lots of people do.
*  You mean in mathematics purely, almost like it's like mathematics, but it isn't mathematics,
*  but it isn't. It isn't. It's a new kind of mathematics is, is it a title of the book?
*  Yeah, right. That's why the book is called that. Right. That's not coincidental.
*  Yeah. It's interesting that I haven't seen really rigorous investigation by thousands of people of
*  this idea. I mean, you look at your competition around rule 30. I mean, that's fascinating. If
*  you can say something, right. Is there some aspect of this thing that could be predicted?
*  That's the fundamental question of science. That's the core. Well, that has been a question of
*  science. I think that's a, that is a, some people's view of what science is about, and it's not clear
*  that's the right view. In fact, as we, as we live through this pandemic full of predictions and so
*  on, it's an interesting moment to be pondering what, what science is actual role in those kinds
*  of things is. Oh, you think it's possible that in science, clean, beautiful, simple prediction
*  may not even be possible in real systems. That's the open question. I don't think it's open. I
*  think that question is answered in the house. No, no, no, no. The answer could be just humans
*  are not smart enough yet. Like we don't have the tools. No, that's, that's the whole point. I mean,
*  that's sort of the big discovery of this principle of computational equivalence of mine.
*  And the, you know, this is something which is kind of a follow on to Gödel's theorem, to Turing's
*  work on the halting problem, all these kinds of things, that there is this fundamental limitation
*  built into science, this idea of computational irreducibility that says that, you know, even
*  though you may know the rules by which something operates, that does not mean that you can readily
*  sort of be smarter than it and jump ahead and figure out what it's going to do. Yes. But do you
*  think there's a hope for pockets of computational reducibility, computational re reducibility,
*  yes, that's so, and then, and then a set of tools and mathematics that help you discover such
*  pockets. That's where we live is in the pockets of reducibility. Right. That's why, you know,
*  and this is one of the things that sort of come out of this physics project and actually something
*  that again, I should have realized many years ago, but didn't is, you know, the, it could very well
*  be that everything about the world is computationally reducible and completely unpredictable. But, you
*  know, in our experience of the world, there is at least some amount of prediction we can make.
*  And that's because we have sort of chosen a slice of probably talk about this in much more detail.
*  But I mean, we've kind of chosen a slice of how to think about the universe in which we can kind
*  of sample a certain amount of computational reducibility. And that's, that's sort of where we,
*  where we exist. And it may not be the whole story of how the universe is, but it is the part of the
*  universe that we care about. And we sort of operate in. And that's, you know, in science,
*  that's been sort of a very special case of that, that is science has chosen to talk a lot about
*  places where there is this computational reducibility that it can find, you know,
*  the motion of the planets can be more or less predicted. You know, the something about the
*  weather is much harder to predict something about, you know, other kinds of things that the,
*  are much harder to predict. And it's, these are, but science has tended to concentrate itself on
*  places where its methods have allowed successful prediction. So you think rule 30, if it could
*  linger on it, because it's just such a beautiful, simple formulation of the essential concept
*  underlying all the things we're talking about. Do you think there's pockets of reducibility
*  inside rule 30? Yes. That is the question of how big are they? What will they allow you to say?
*  And so on. And that's, and figuring out where those pockets are. I mean, in a sense, that's the,
*  that's sort of a, you know, that is an essential thing that one would like to do in science. But
*  it's also the important thing to realize that has not been, you know, is that science, if you just
*  pick an arbitrary thing, you say, what's the answer to this question? That question may not be one
*  that has a computationally reducible answer. That question, if you choose, you know, if you walk
*  along the series of questions and you've got one that's reducible and you get to another one that's
*  nearby and it's reducible, too, if you stick to that kind of stick to the land, so to speak,
*  then you can go down this chain of sort of reducible, answerable things. But if you just say,
*  I'm just pick a question at random, I'm going to have my computer pick a question at random.
*  Most likely, it's going to be reducible. Most likely, it will be reducible. And what we're
*  throwing in the world, so to speak, we, you know, when we engineer things, we tend to engineer
*  things to sort of keep in the zone of reducibility. When we're throwing things by the natural world,
*  for example, not at all certain that we will be kept in this kind of zone of reducibility.
*  Can we talk about this pandemic then? Sure. For a second. So how do we, there's obviously
*  huge amount of economic pain that people are feeling. There's a huge incentive and medical pain,
*  uh, health, just all kind of psychological. There's a huge incentive to figure this out,
*  to walk along the trajectory of reducible, of reducibility. Uh, there's a, there's a lot of
*  disparate data. You know, people understand generally how virus is spread, but it's very
*  complicated because there's a lot of uncertainty. There's a, uh, there could be a lot of variability,
*  like so many, obviously a nearly infinite number of variables that, uh, that represent human
*  interaction. And so you have to figure out in term from the perspective of reducibility,
*  figure out which variables are really important in this kind of, uh, from an epidemiological
*  perspective. So why aren't we, you kind of said that we're clearly failing. Well, I think it's
*  a complicated thing. So, so I mean, you know, when this pandemic started up, you know, I happened to
*  be in the middle of being about to release this whole physics project, but I thought, you know,
*  timing is just a little bit, but, but, um, but, you know, but I thought, you know, I should do
*  the public service thing of, you know, trying to understand what I could about the pandemic. And,
*  you know, we've been curating data about it and all that kind of thing. But, but, you know, so I
*  started looking at the data and started looking at modeling and I decided it's just really hard.
*  You need to know a lot of stuff that we don't know about human interactions. It's actually clear now
*  that there's a lot of stuff we didn't know about viruses, um, and about the way immunity works and
*  so on. And, um, it's, you know, I think what will come out in the end is there's a certain amount of,
*  of what happens that way. You just kind of have to trace each step and see what happens. There's a
*  certain amount of stuff where there's going to be a big narrative about this happened because,
*  you know, of T cell immunity, this cause happened because there's this whole giant sort of field of,
*  of asymptomatic viral stuff out there. You know, there will be a narrative and that narrative,
*  whenever there's a narrative, that's kind of a sign of reducibility. But when you just say,
*  let's from first principles figure out what's going on, then you can potentially be stuck in this kind
*  of mess of irreducibility where you just have to simulate each step. And you can't do that unless
*  you know details about, you know, human interaction networks and so on and so on and so on. The thing
*  that has, has been very sort of frustrating to see is the mismatch between people's expectations
*  about what science can deliver and what science can actually deliver, so to speak. Um, because
*  people have this idea that, you know, it's science, so there must be a definite answer and we must be
*  able to know that answer. And, you know, this is, it is both, uh, uh, you know, the, the, when you've,
*  after you've played around with sort of little programs in the computational universe, you don't
*  have that intuition anymore. You know, it's, it's, I always, I'm always fond of saying, you know, the,
*  the, the, the computational animals are always smarter than you are. That is, you know, you look
*  at one of these things and it's like, it can't possibly do such and such a thing. Then you run it
*  and it's like, wait a minute, it's doing that thing. How does that work? Okay. Now I can go back and
*  understand it. But that's the brave thing about science is that in the chaos of the irreducible
*  universe, we nevertheless persist to find those pockets. That's kind of the whole point.
*  That's like you say that the limits of science, but that, you know, yes, it's highly limited, but
*  there's a hope there. And like, uh, there's so many questions I want to ask here. So one, you said
*  narrative, which is really interesting. So obviously from, uh, at every level of society,
*  you look at Twitter, everybody's constructing narratives about the pandemic, about not just
*  the pandemic, but all the cultural tension that we're going through. So there's narratives,
*  but they're not necessarily connected to the underlying reality of these systems.
*  So our human narratives, I don't even know if they're, I don't like those pockets of reducibility
*  because we're, uh, it's like constructing things that are not actually representative of reality.
*  Well, and thereby not giving us like good solutions to how to predict the system.
*  Look, it gets complicated because, you know, people want to say, explain the pandemic to me,
*  explain what's going to happen in the future. Yes. But also can you explain it? Is there a story
*  to tell what already happened in the past? Yeah. What's going to happen. But I mean,
*  and you know, it's similar to sort of explaining things in AI or in any computational system. It's
*  like, like, you know, explain what happened. Well, it could just be this happened because
*  of this detail and this detail and this detail and a million details. And there isn't a big story
*  to tell. There's no kind of big arc of the story that says, oh, it's because, you know, there's a
*  viral field that has these properties and people start showing symptoms. You know, when, when the
*  seasons change, people will show symptoms and people don't even understand, you know, seasonal
*  variation of flu, for example. It's a, it's a, it's something where, where, you know, that could be a
*  big story or it could be just a zillion little details that mounts up. See, but, okay, let's,
*  let's pretend that this pandemic, like the coronavirus resembles something like the one
*  D rule 30 cellular automata. Okay. So I mean, that's how epidemiologists model virus spread.
*  Indeed. Yes. There's sometimes use cellular automata. Yes. And okay. So you can say it's
*  simplistic, but okay, let's say it is, it's representative of actually what happens.
*  You know, the, the dynamic of you have a graph, it probably is closer to the hyper graph.
*  That's another funny thing. As we were getting ready to release this physics project, we realized
*  that a bunch of things we'd worked out about, about foliations of causal graphs and things
*  were directly relevant to thinking about contact tracing and interactions with cell phones and so
*  on, which is really weird. But like, it just feels like, it feels like we should be able to get some
*  beautiful core insight about the spread of this particular virus on the hyper graph of human
*  civilization. Right. I tried. I didn't, I didn't manage to figure it out. But you're one person.
*  Yeah. But I mean, I think actually it's, it's a funny thing because it turns out the,
*  the main model, you know, this SIR model, I only realized recently was invented by the,
*  the grandfather of a good friend of mine from high school. So that was just a, you know,
*  it's a weird thing. Right. The question is, you know, okay, so you know, you know, on this graph
*  of how humans are connected, you know, something about what happens if this happens and that
*  happens. That graph is made in complicated ways that depends on, on all sorts of issues that,
*  where we don't have the data about how human society works well enough to be able to make
*  that graph. There's actually one of my kids did a study of sort of what happens on different kinds
*  of graphs and how robust are the results. Okay. His basic answer is there are a few general results
*  that you can get that are quite robust, like, you know, a small number of big gatherings is worse
*  than a large number of small gatherings. Okay. That's quite robust. But when you ask more detailed
*  questions, it seemed like it just depends. It depends on details. In other words, it's kind
*  of telling you in that case, you know, the irreducibility matters, so to speak. It's not,
*  there's not going to be this kind of one sort of master theorem that says, and therefore this is
*  how things are going to work. Yeah. But there's a certain kind of, from a graph perspective,
*  the certain kind of dynamic to human interaction. So like large groups and small groups,
*  I think it matters who the groups are. For example, you can imagine large depends how you define
*  large, but you can imagine groups of 30 people as long, like as long as they are, uh,
*  cliques or whatever, like as long as the outgoing degree of that graph is small or something like
*  that, like you can imagine some beautiful underlying rule of human dynamic interaction where
*  I can still be happy, where I can have a conversation with you and a bunch of other people that mean a
*  lot to me in my life and then stay away from the bigger, I don't know, not going to a Miley Cyrus
*  concert or something like that and figuring out mathematically some nice. See, this is an interesting
*  thing. So I mean, in, you know, this is the question of what you're describing is kind of, uh,
*  the problem of, um, the many situations where you would like to get away from computational
*  irreducibility. A classic one in physics is thermodynamics. The, you know, the second law
*  of thermodynamics, the law that says, you know, entropy tends to increase things that, you know,
*  start orderly tend to get more disordered or which is also the thing that says, given that you have
*  a bunch of heat, it's hard heat is, you know, the microscopic motion of molecules. It's hard to turn
*  that heat into systematic mechanical work. It's hard to, you know, just take something being hot
*  and turn that into, oh, the, the, you know, the, all the atoms are going to line up in the bar of
*  metal and the piece of metal is going to shoot in some direction. That's essentially the same problem.
*  How do you go from this, this computationally irreducible mess of things happening and get
*  something you want out of it? It's kind of mining, you know, you're kind of now, you know, actually
*  I've, I've understood in recent years that, that the story of thermodynamics is actually precisely
*  a story of computational irreducibility, but it is a, um, it is already an analogy. You know,
*  you can, you can kind of see that is can you take the, um, you know, what you're asking to do there
*  is you're asking to go from the, um, uh, the kind of, um, the mess of all these complicated human
*  interactions and all this kind of computational processes going on. And you say, I want to achieve
*  this particular thing out of it. I want to kind of extract from the heat of what's happening.
*  I want to kind of extract this useful piece of sort of mechanical work that I find helpful.
*  I mean, do you have a hope for the pandemic? So we'll talk about physics, but for the pandemic,
*  can that be extracted? Do you think? Well, I think the good news is the curves basically,
*  you know, for reasons we don't understand the curves, you know, the, the, the clearly
*  measurable mortality cloves and so on for the Northern hemisphere have gone down.
*  Yeah. But the bad news is that it could be a lot worse for future viruses. And what this pandemic
*  revealed is we're highly unprepared for the discovery of the pockets of reducibility
*  within a pandemic. That's much more dangerous. Well, my guess is the specific risk of, you know,
*  viral pandemics, you know, that the pure virology and, you know, immunology of the thing,
*  this will cause that to advance to the point where this particular risk is probably considerably
*  mitigated. But, you know, it's, you know, does, is, is the structure of modern society robust
*  to all kinds of risks? Well, the answer is clearly no. And, you know, it's, it's surprising to me
*  the extent to which people, you know, as I say, it's, it's a, it's kind of scary, actually,
*  how much people believe in science. That is people say, oh, you know, because the science
*  says this, that and the other will do this and this and this, even though from a sort of common
*  sense point of view, it's a little bit crazy. And the people are not prepared and it doesn't
*  really work in society as it is for people to say, well, actually, we don't really know how the
*  science works. People say, well, tell us what to do. Yeah, because then, yeah, what's the alternative
*  for the masses? It's difficult to sit. It's difficult to meditate on computational reducibility.
*  It's difficult to sit. It's not a good dinner meal while, while knowing that you know nothing
*  about the world. This is a place where, you know, this is, this is what politicians, you know,
*  and political leaders do for a living, so to speak, is you got to make some decision
*  about what to do. And it's some tell some narrative that while amidst the mystery and knowing not much
*  about the past or the future, still telling a narrative that somehow gives people hope that
*  we know what the heck we're doing. Yeah, and get society through the issue. You know, even, even
*  though, you know, the idea that we're just going to, you know, sort of be able to get the definitive
*  answer from science, and it's going to tell us exactly what to do, unfortunately, you know,
*  that it's interesting, because let me point out that if that was possible, if science could always
*  tell us what to do, then in a sense, our, you know, that will be a big downer for our lives.
*  If science could always tell us what the answer is going to be. It's like, well, you know, it's kind
*  of fun to live one's life and just sort of see what happens. If one could always just say, let me,
*  let me check my science. Oh, I know, you know, the result of everything is going to be 42. I don't
*  need to live my life and do what I do. It's just we already know the answer. It's actually good news,
*  in a sense, that there is this phenomenon of computational irreducibility that doesn't allow
*  you to just sort of jump through time and say, this is the answer, so to speak. And that's so that's a
*  good thing. The bad thing is it doesn't allow you to jump through time and know what the answer is.
*  It's scary. Do you think we're going to be okay as a human civilization? You said we don't know.
*  Absolutely. Do you think it's, do you think we'll prosper or destroy ourselves?
*  As a general, in general, I'm an optimist. No, I think that the, you know, it'll be interesting
*  to see, for example, with this, you know, pandemic, I, you know, to me, you know, when you look at,
*  like, organizations, for example, you know, having some kind of perturbation, some kick to the system,
*  usually the end result of that is actually quite good. You know, unless it kills the system,
*  it's actually quite good usually. And I think in this case, you know, people, I mean, my impression,
*  you know, it's a little weird for me, because, you know, I've been a remote tech CEO for 30 years,
*  it doesn't, you know, this is bizarrely, you know, and the fact that, you know, like this coming to
*  see you here is one of the rare moments in human interaction. It's the first time in six months
*  that I've been like, you know, in a building other than my house. Okay. So, so, so, you know,
*  it's, I'm, I'm a kind of ridiculous outlier and these kinds of things. But overall, your sense is
*  when you shake up the system and throw in chaos, that you, you, you, uh, challenge the system,
*  we humans emerge better. Seems to be that way. Who's to know. But I think that, you know, people,
*  you know, my, my sort of vague impression is that people are sort of, you know, oh, what's actually
*  important, you know, what's, uh, what, what is worth caring about and so on. And that seems to be
*  something that perhaps is, is more, you know, emergent in this kind of situation. It's so
*  fascinating that on the individual level, we have our own complex cognition, we have consciousness,
*  we have intelligence, we're trying to figure out little puzzles. And then that somehow creates
*  this graph of collective intelligence. Well, we figure out, and then you throw in these viruses
*  of which there's millions different, you know, this entire taxonomy and the viruses are thrown
*  into the system of collective human intelligence and the little humans figure out what to do about
*  it. We get like, we tweet stuff about information. There's doctors, there's conspiracy theorists,
*  and then we play with different information. I mean, the whole of it is fascinating.
*  I, I am like you also very optimistic, but, uh, there's a fee, just, you said, uh, the
*  computation or reducibility, there's always a fear of the darkness of the uncertainty before,
*  before us. Yeah, I know. Scary. I mean, the thing is if you knew everything, it will be boring.
*  And yeah, it would be, and then, um, uh, and worse than boring, so to speak, it would be,
*  you, it would reveal the pointlessness, so to speak. And in a sense, the, the fact that there
*  is this computational reducibility, it's like, as we live our lives, so to speak, something is being
*  achieved. We're computing what our lives, you know, uh, you know, what happens in our lives.
*  That's funny. So the computation or disability is kind of like, it gives the meaning to life. It is
*  the meaning of life. Computation reducibility is the meaning of life. There you go. It gives
*  it meaning. Yes. I mean, it, it, it's, it's what, it's what causes it to not be something where you
*  can just say, uh, you know, you went through all those steps to live your life, but we already knew
*  what the answer was. Right. Hold on one second. I'm going to use my handy Wolfram Alpha sunburn
*  computation thing. So long as I can get network here. There we go. Oh, actually, you know what?
*  It says sunburn unlikely. This is a QA moment. This is a good moment. Okay. Okay. Well,
*  let me just check what it thinks. I would say why it thinks that it doesn't seem like my intuition.
*  This is one of these cases where we can, the question is, do we do, do we trust the science
*  or do we, um, use common sense? The UV thing is cool. Yeah. Yeah. Well, we'll see. This is a QA
*  moment. As I say, it's, uh, can we trust the product? Yes, we trust the product. So,
*  and then there'll be a data point either way. If, if I'm desperately sunburned, I will send
*  it in a angry feedback because we mentioned the concept so much and a lot of people know it,
*  but can you say what computational reducibility is? Yeah, right. So it's only the question is
*  if you think about things that happen as being computations, you think about the, uh, some process
*  in physics, something that you compute in mathematics, whatever else, it's a computation
*  in the sense it has definite rules. You follow those rules, you, uh, follow them many steps
*  and you get some result. So then the issue is if you look at all these different kinds of computations
*  that can happen, whether they're computations that are happening in the natural world, whether
*  they're happening in our brains, whether they're happening in our mathematics, whatever else,
*  the big question is how do these computations compare is are there dumb computations and smart
*  computations or are they somehow all equivalent? And the thing that I kind of, uh, was sort of
*  surprised to realize from a bunch of experiments that I did in the early nineties, and now we have
*  tons more evidence for it. This thing I call the principle of computational equivalence,
*  which basically says when one of these computations, one of these processes that follows rules doesn't
*  seem like it's doing something obviously simple, then it has reached the sort of equivalent level
*  of sophisticate of computational sophistication of everything. So what does that mean? That means
*  that, you know, you might say, gosh, I'm studying this little tiny, you know, tiny program on my
*  computer. I'm studying this little thing in nature, but I have my brain and my brain is surely much
*  smarter than that thing. I'm going to be able to systematically outrun the computation that it does
*  because I have a more sophisticated computation that I can do. But what the principle of
*  computational equivalence says is that doesn't work. Our brains are doing computations that are
*  exactly equivalent to the kinds of computations that are being done in all these other sorts of
*  systems. And so what consequences does that have? Well, it means that we can't systematically outrun
*  these systems. These systems are computationally irreducible in the sense that there's no sort of
*  shortcut that we can make that jumps to the answer. In a general case. Right, right. But
*  what has happened, you know, what science has become used to doing is using the little sort
*  of pockets of computational reducibility, which by the way are an inevitable consequence of
*  computational irreducibility, that there have to be these pockets scattered around of computational
*  reducibility to be able to find those particular cases where you can jump ahead. I mean, one thing
*  sort of a little bit of a parable type thing that I think is fun to tell you, if you look at
*  ancient Babylon, they were trying to predict three kinds of things. They tried to predict,
*  you know, where the planets would be, what the weather would be like, and who would win or lose
*  a certain battle. And they had no idea which of these things would be more predictable than the
*  other. And, you know, it turns out, you know, where the planets are, is a piece of computational
*  reducibility that, you know, 300 years ago or so we pretty much cracked. I mean, it's been technically
*  difficult to get all the details right, but it's basically, we got that, you know, who's going to
*  win or lose the battle? No, we didn't crack that one. That one, that one, right. Game theorists
*  are trying. And then the weather, how are we kind of halfway on that one? Yeah, I think we're doing
*  okay on that one. You know, long term climate, different story, but the weather, you know, we're
*  much closer on that. But do you think eventually we'll figure out the weather? So do you think
*  eventually most think we'll figure out the local pockets in everything, essentially the local pockets
*  of reducibility? No, I think that it's an interesting question, but I think that the, you know, there is
*  an infinite collection of these local pockets. We'll never run out of local pockets. And by the way,
*  those local pockets are where we build engineering, for example. That's how we, you know, when we, if
*  we want to have a predictable life, so to speak, then, you know, we have to build in these sort of
*  pockets of reducibility. Otherwise, you know, if we were, if we were sort of existing in this kind
*  of irreducible world, we'd never be able to, you know, have definite things to know what's going to
*  happen. You know, I have to say, I think one of the features, you know, when we look at sort of today
*  from the future, so to speak, I suspect one of the things where people will say, I can't believe they
*  didn't see that, is stuff to do with the following kind of thing. So, you know, if we describe, oh,
*  I don't know, something like heat, for instance, we say, oh, you know, the air in here, it's, you
*  know, it's this temperature, this pressure. That's as much as we can say. Otherwise, just a bunch of
*  random molecules bouncing around. People will say, I just can't believe they didn't realize that there
*  was all this detail in how all these molecules were bouncing around, and they could make use of that.
*  And actually, I realized there's a thing I realized last week, actually, was a thing that people say,
*  you know, one of the scenarios for the very long term history of our universe is the so-called heat
*  death of the universe, where basically, everything just becomes thermodynamically boring. Everything's
*  just this big kind of gas and thermal equilibrium. People say, that's a really bad outcome. But
*  actually, it's not a really bad outcome. It's an outcome where there's all this computation going on,
*  and all those individual gas molecules are all bouncing around in very complicated ways,
*  doing this very elaborate computation. It just happens to be a computation that right now,
*  we haven't found ways to understand. We haven't found ways, you know, our brains haven't, you know,
*  and our mathematics and our science and so on, haven't found ways to tell an interesting story
*  about that. It just looks boring to us. You're saying there's a hopeful view of the heat death,
*  quote unquote, of the universe, where there's actual beautiful complexity going on, similar to
*  the kind of complexity we think of that creates rich experience in human life and life on Earth.
*  Yes.
*  So those little molecules interacting complex ways, that could be intelligence in that. There could
*  be-
*  Absolutely. I mean, this is what you learn from this-
*  Wow, that's a hopeful message.
*  Right. I mean, this is what you kind of learn from this principle of computational equivalence.
*  You learn it's both a message of sort of hope and a message of kind of, you know, you're not
*  as special as you think you are, so to speak. I mean, because, you know, we imagine that with
*  sort of all the things we do with human intelligence and all that kind of thing, and all of the stuff
*  we've constructed in science, it's like, we're very special. But actually, it turns out, well,
*  no, we're not. We're just doing computations like things in nature do computations like those gas
*  molecules do computations like the weather does computations. The only thing about the
*  computations that we do that's really special is that we understand what they are, so to speak.
*  In other words, we have a, you know, to us, they're special because kind of they're connected to our
*  purposes, our ways of thinking about things and so on. And that's some, but so-
*  That's very human centric. That's where we're just attached to this kind of thing.
*  So let's talk a little bit of physics. Maybe let's ask the biggest question. What is a theory
*  of everything in general? What does that mean? Yeah. So I mean, the question is, can we kind of
*  reduce what has been physics as a something where we have to sort of pick away and say,
*  do we roughly know how the world works to something where we have a complete formal theory,
*  where we say, if we were to run this program for long enough, we would reproduce everything,
*  you know, down to the fact that we're having this conversation at this moment, etc, etc, etc.
*  Any physical phenomena, any phenomena in this world?
*  Phenomenon in the universe. But the, you know, because of computational irreducibility,
*  it's not, you know, that's not something where you say, okay, you've got the fundamental theory
*  of everything, then, you know, tell me whether, you know, lions are going to eat tigers or
*  something, you know, that's a no, you have to run this thing for, you know, 10 to the 500 steps or
*  something, to know something like that. Okay. So at some moment, potentially, you say, this is a rule,
*  and run this rule enough times, and you will get the whole universe. Right? That's, that's what it
*  means to kind of have a fundamental theory of physics, as far as I'm concerned, is you've got
*  this rule, it's potentially quite simple, we don't know for sure it's simple, but we have various
*  reasons to believe it might be simple. And then you say, okay, I'm showing you this rule, you just
*  run it only 10 to the 500 times, and you'll get everything. In other words, you've kind of reduced
*  the problem of physics to a problem of mathematics, so to speak. It's like, it's as if,
*  you know, you'd like you generate the digits of pi, there's a definite procedure, you just
*  generate them. And it'd be the same thing if you have a fundamental theory of physics of the kind
*  that I'm imagining, you, you know, you get a this rule, and you just run it out, and you get
*  everything that happens in the universe. So a theory of everything is a mathematical
*  framework within which you can explain everything that happens in the universe, it's kind of
*  in a unified way. It's not there's a bunch of disparate modules of
*  does it feel like if you create a rule, and we'll talk about the Wolfram physics model,
*  which is fascinating, but if you if you if you have a simple set of rules with a with a data
*  structure, like a hypergraph, does that feel like a satisfying theory of everything? Because then
*  you really run up against the irreducibility, computational reducibility, right? So that's a
*  really interesting question. So I, I, I, you know, what I thought was going to happen is, I thought,
*  we, you know, I thought we had a pretty good I had a pretty good idea for what the structure of
*  this sort of theory that sort of underneath space and time and so on might be like. And I thought,
*  gosh, you know, in my lifetime, so to speak, we might be able to figure out what happens in
*  the first 10 to the minus 100 seconds of the universe. And that would be cool. But it's pretty
*  far away from anything that we can see today. And it will be hard to test whether that's right,
*  and so on, and so on, and so on. To my huge surprise, although it should have been obvious,
*  and it's embarrassing that it wasn't obvious to me, but, but to my huge surprise, we managed to
*  get unbelievably much further than that. And basically, what happened is that it turns out
*  that even though there's this kind of bed of computational irreducibility, that sort of these
*  all these simple rules run into, there is a there are certain pieces of computational reducibility
*  that quite generically occur for large classes of these rules. And, and this is the really exciting
*  thing, as far as I'm concerned, the the the big pieces of computational reducibility are basically
*  the pillars of 20th century physics. That's the amazing thing that general relativity and
*  quantum field theory, the sort of the pillars of 20th century physics turn out to be precisely
*  the stuff you can say, there's a lot you can't say, there's a lot that's kind of at this
*  irreducible level, where you kind of don't know what's going to happen, you have to run it,
*  you know, you can't run it within our universe, etc, etc, etc, etc. But the thing is, there are
*  things you can say. And the things you can say, turn out to be very beautifully,
*  exactly the structure that was found in 20th century physics, namely,
*  general relativity and quantum mechanics. And general relativity and quantum mechanics
*  are these pockets of reducibility that we think of as that that 20th century physics is
*  essentially pockets of reducibility. And then it's it is incredibly surprising that any kind of model
*  that's generative from simple rules would have would have such pockets.
*  Yeah, well, I think what what's surprising is, we didn't know where those things came from.
*  It's like general relativity, it's a very nice, mathematically elegant theory. Why is it true?
*  You know, quantum mechanics, why is it true? What we realized is that from this, that they are these
*  theories are generic to a huge class of systems that have these particular very unstructured,
*  underlying rules. And that's the that's the thing that is sort of remarkable. And that's the thing
*  to me that's just, it's really beautiful. I mean, it's an interesting thing that's even more beautiful,
*  is that it turns out that, you know, people have been struggling for a long time, you know, how does
*  general relativity theory of gravity relate to quantum mechanics, they seem to have all kinds of
*  incompatibilities. It turns out what we realized is, at some level, they are the same theory.
*  And this is, it's, it's just great, as far as I'm concerned.
*  So maybe like taking a little step back from your perspective, not from the low, not from the
*  beautiful hypergraph, well, from physics model perspective, but from the perspective of 20th
*  century physics, what is general relativity? What is quantum mechanics? How do you think about these
*  two theories from the context of the theory of everything? It's just even definitions.
*  Yeah, yeah, yeah, right. So I mean, you know, a little bit of history of physics, right? So I mean,
*  you know, okay, very, very quick history of this, right? So I mean, you know, physics, you know,
*  in ancient Greek times, people basically said, we can just figure out how the world works. As you know,
*  we're philosophers, we're going to figure out how the world works. You know, some philosophers thought
*  there were atoms, some philosophers thought there were, you know, continuous flows of things,
*  people had different ideas about how the world works. And they tried to just say, we're going to
*  construct this idea of how the world works. They didn't really have sort of notions of doing
*  experiments and so on quite the same way as developed later. So that was sort of an early
*  tradition for thinking about sort of models of the world. Then, by the time of 1600s, time of
*  Galileo, and then Newton, sort of the big idea there was, you know, the title of Newton's book,
*  you know, Principia Mathematica, Mathematical Principles of Natural Philosophy. We can use
*  mathematics to understand natural philosophy, to understand things about the way the world works.
*  And so that then led to this kind of idea that, you know, we can write down a mathematical equation
*  and have that represent how the world works. So Newton's one of his most famous ones is
*  Universal Law of Gravity, Inverse Square Law of Gravity, that allowed him to compute all sorts
*  of features of the planets and so on, although some of them he got wrong and it was took another
*  hundred years for people to actually be able to do the math to the level that was needed. But
*  so that had been the sort of tradition was we write down these mathematical equations. We don't
*  really know where these equations come from. We write them down. Then we figure out, we work out
*  the consequences and we say, yes, that agrees with what we actually observe in astronomy or
*  something like this. So that tradition continued. And then the first of these two sort of great
*  20th century innovations was, well, the history is actually a little bit more complicated, but
*  let's say that there were two quantum mechanics and general relativity. Quantum mechanics,
*  the kind of 1900 was kind of the very early stuff done by Planck that led to the idea of photons,
*  particles of light. But let's take general relativity first. One feature of the story is
*  that special relativity, a thing Einstein invented in 1905, was something which surprisingly was a
*  kind of logically invented theory. It was not a theory where it was something where given these
*  ideas that were sort of axiomatically thought to be true about the world, it followed that such
*  and such a thing would be the case. It was a little bit different from the kind of
*  methodological structure of some existing theories in the more recent times where it's just been,
*  we write down an equation and we find out that it works. So what happened there-
*  So there's some reasoning about the light.
*  The basic idea was the speed of light appears to be constant. Even if you're traveling very fast,
*  you shine a flashlight, the light will come out. Even if you're going at half the speed of light,
*  the light doesn't come out of your flashlight at one and a half times the speed of light.
*  It's still just the speed of light. And to make that work, you have to change your view of how
*  space and time work to be able to account for the fact that when you're going faster, it appears
*  that length is foreshortened and time is dilated and things like this.
*  And that's special relativity.
*  That's special relativity. So then Einstein went on with sort of vaguely similar kinds of thinking.
*  In 1915, he invented general relativity, which is a theory of gravity. And the basic point of
*  general relativity is it's a theory that says when there is mass in space, space is curved.
*  And what does that mean? Usually you think of what's the shortest distance between two points,
*  like ordinarily on a plane in space, it's a straight line. Photons, light goes in straight lines.
*  Well, then the question is, if you have a curved surface, a straight line is no longer straight.
*  On the surface of the Earth, the shortest distance between two points is a great circle.
*  It's a circle. So Einstein's observation was maybe the physical structure of space
*  is such that space is curved. So the shortest distance between two points, the path, the straight
*  line in quotes, won't be straight anymore. And in particular, if a photon is traveling near the sun
*  or something or if a particle is going, something is traveling near the sun, maybe the shortest path
*  will be one that is something which looks curved to us because it seems curved to us because
*  space has been deformed by the presence of mass associated with that massive object.
*  So the idea there is think of the structure of space as being a dynamical changing kind of thing.
*  But then what Einstein did was he wrote down these differential equations that basically
*  represented the curvature of space and its response to the presence of mass and energy.
*  And that ultimately is connected to the force of gravity, which is one of the forces that seems to,
*  based on its strength, operate on a different scale than some of the other forces. So it
*  operates on a scale that's very large. What happens there is just this curvature of space
*  which causes the paths of objects to be deflected. That's what gravity does. It causes the paths of
*  objects to be deflected. And this is an explanation for gravity, so to speak.
*  And the surprise is that from 1915 until today, everything that we've measured about gravity
*  precisely agrees with general relativity. And that it wasn't clear. Black holes were sort of
*  a predict. Well, actually the expansion of the universe was an early potential prediction,
*  although Einstein tried to sort of patch up his equations to make it not cause the universe to
*  expand because it was kind of so obvious the universe wasn't expanding. And it turns out it
*  was expanding and he should have just trusted the equations. And that's a lesson for those of us
*  interested in making fundamental theories of physics is you should trust your theory
*  and not try and patch it because of something that you think might be the case that
*  might turn out not to be the case. Even if the theory says something crazy is happening?
*  Yeah, right. Like the universe is expanding.
*  It took until the 1940s, probably even really until the 1960s, until people understood that
*  black holes were a consequence of general relativity and so on. But the big surprise
*  has been that so far this theory of gravity has perfectly agreed with these collisions of black
*  holes seen by their gravitational waves. It all just works. So that's been kind of one pillar
*  of the story of physics. It's mathematically complicated to work out the consequences of
*  general relativity, but it's not. And some things are kind of squiggly and complicated.
*  People believe energy is conserved. Okay, well, energy conservation doesn't really work in general
*  relativity in the same way as it ordinarily does. And it's all a big mathematical story of how you
*  actually nail down something that is definitive that you can talk about and not specific to the
*  reference frames you're operating in and so on and so on and so on. But fundamentally,
*  general relativity is a straight shot in the sense that you have this theory, you work out
*  its consequences. And that theory is useful in terms of basic science and trying to understand
*  the way black holes work, the way the creation of galaxies work, sort of all these kind of
*  cosmological things. Understanding what happened, like you said, at the Big Bang.
*  Yeah. Like all those kinds of, well, no, not at the Big Bang actually, right? But...
*  Well, features of the expansion of the universe, yes. And there are lots of details where we don't
*  quite know how it's working. Where's the dark matter? Is there dark energy? Et cetera, et cetera,
*  but fundamentally, the testable features of general relativity, it all works very beautifully.
*  And it's, in a sense, it is mathematically sophisticated, but it is not conceptually hard
*  to understand in some sense. Okay, so that's general relativity.
*  And what's its friendly neighbor? Like you said, there's two theories, quantum mechanics.
*  Right. So quantum mechanics, the way that that originated was, one question was, is the world
*  continuous or is it discrete? In ancient Greek times, people had been debating this. People
*  debated it throughout history. Is light made of waves? Is it continuous? Is it discrete? Is it
*  made of particles, corpuscles, whatever? What had become clear in the 1800s is that atoms,
*  that materials are made of discrete atoms. When you take some water, the water is not a continuous
*  fluid, even though it seems like a continuous fluid to us at our scale. But if you say,
*  let's look at it smaller and smaller and smaller and smaller scale, eventually you get down to
*  these molecules and then atoms. It's made of discrete things. The question is sort of how
*  important is this discreteness? Just what's discrete? What's not discrete? Is energy discrete?
*  Is what's discrete? What's not? Does it have mass? Those kinds of questions?
*  Yeah, yeah, right. Well, there's question, for example, is mass discrete is an interesting
*  question, which is now something we can address. But what happened in coming up to the 1920s,
*  there was this kind of mathematical theory developed that could explain certain kinds
*  of discreteness in features of atoms and so on. What developed was this mathematical theory
*  that was the theory of quantum mechanics, theory of wave functions, Schrodinger's equation,
*  things like this. That's a mathematical theory that allows you to calculate lots of features
*  of the microscopic world, lots of things about how atoms work, et cetera, et cetera, et cetera.
*  Now, the calculations all work just great. The question of what does it really mean
*  is a complicated question. Now, I mean, to just explain a little bit historically,
*  the early calculations of things like atoms worked great in the 1920s, 1930s, and so on.
*  There was always a problem in quantum field theory, which is a theory of in quantum mechanics,
*  you're dealing with a certain number of electrons and you fix the number of electrons. You say,
*  I'm dealing with a two-electron thing. In quantum field theory, you allow for particles being
*  created and destroyed so you can emit a photon that didn't exist before. You can absorb a photon,
*  things like that. That's a more complicated, mathematically complicated theory. It had all
*  kinds of mathematical issues and all kinds of infinities that cropped up. It was finally
*  figured out more or less how to get rid of those. But there were only certain ways of doing the
*  calculations and those didn't work for atomic nuclei, among other things. That led to a lot
*  of development up until the 1960s of alternative ideas for how one could understand what was
*  happening in atomic nuclei, et cetera, et cetera, et cetera. End result, in the end, the kind of most
*  quote obvious mathematical structure of quantum field theory seems to work, although it's
*  mathematically difficult to deal with. But you can calculate all kinds of things. You can calculate
*  a dozen decimal places, certain things. You can measure them. It all works. It's all beautiful.
*  Now you say- The underlying fabric is the model of that particular theory is fields. You keep saying
*  fields- Those are quantum fields. Those are different from classical fields. A field is
*  something like you say, like you say, the temperature field in this room. It's like there is
*  a value of temperature at every point around the room. Or you can say the wind field would be the
*  vector direction of the wind at every point. It's continuous. Yes. And that's a classical field.
*  The quantum field is a much more mathematically elaborate kind of thing. And I should explain
*  that one of the pictures of quantum mechanics that's really important is in classical physics,
*  one believes that definite things happen in the world. You pick up a ball, you throw it,
*  the ball goes in a definite trajectory that has certain equations of motion. It goes in a
*  parabola or whatever else. In quantum mechanics, the picture is definite things don't happen.
*  Instead, what happens is this whole structure of many different paths being followed. And we can
*  calculate certain aspects of what happens, certain probabilities of different outcomes and so on.
*  And you say, well, what really happened? What's really going on? What's the underlying story?
*  How do we turn this mathematical theory that we can calculate things with into something that we
*  can really understand and have a narrative about? And that's been really, really hard for quantum
*  mechanics. My friend, Dick Feynman, always used to say, nobody understands quantum mechanics,
*  even though he'd made his whole career out of calculating things about quantum mechanics.
*  But nevertheless, the quantum field theory is very accurate at predicting a lot of the physical
*  phenomena. So it works. Yeah. But there are things about it. When we apply it, the standard model
*  of particle physics, for example, which we apply to calculate all kinds of things, it works really
*  well. And you say, well, it has certain parameters. It has a whole bunch of parameters, actually.
*  You say, why is the, you know, why does the muon particle exist? Why is it 206 times the
*  mass of the electron? We don't know. No idea. But so the standard model of physics is one of the
*  models that's very accurate for describing three, three of the fundamental forces of physics. And
*  it's looking at the world of the very small. Right. And then there's back to the neighbor of
*  of gravity, of general relativity. So, and in the context of a theory of everything,
*  what's traditionally the task of the unification of these theories?
*  And why is it hard? Well, the issue is you try to use the methods of quantum field theory
*  to talk about gravity, and it doesn't work. Just like there are photons of light. So there are
*  gravitons, which are sort of the particles of gravity. And when you try and compute sort of
*  the properties of the particles of gravity, the kind of mathematical tricks that get used
*  in working things out in quantum field theory don't work. And that's, so that's been a sort
*  of fundamental issue. And when you think about black holes, which are a place where sort of the
*  structure of space is, you know, has sort of rapid variation, and you get kind of quantum effects
*  mixed in with effects from general relativity, things get very complicated, and there are
*  apparent paradoxes and things like that. And people have, you know, there have been a bunch
*  of mathematical developments in physics over the last, I don't know, 30 years or so, which have
*  kind of picked away at those kinds of issues and got hints about how things might work.
*  But it hasn't been, you know, the other thing to realize is, as far as physics is concerned,
*  it's just like his general relativity, his quantum field theory, you know, be happy.
*  Yeah. So do you think there's a quantization of gravity, quantum gravity? What do you think of
*  efforts that people have tried to, yeah, what do you think in general of the efforts of the
*  physics community to try to unify these laws? So I think what's, it's interesting. I mean,
*  I would have said something very different before what's happened with our physics project.
*  I mean, you know, the remarkable thing is what we've been able to do is to make from this very
*  simple, structurally simple, underlying set of ideas, we've been able to build this,
*  this, you know, very elaborate structure that's both very abstract and very sort of mathematically
*  rich. And the big surprise, as far as I'm concerned, is that it touches many of the ideas that people
*  have had. So in other words, things like string theory and so on, twister theory, it's like the,
*  you know, we might've thought, I had thought we're out on a prong, we're building something
*  that's computational, it's completely different from what other people have done. But actually,
*  it seems like what we've done is to provide essentially the machine code that, you know,
*  these things are, are various features of domain specific languages, so to speak, that talk about
*  various aspects of this machine code. And I think there's a, this is something that to me is, is,
*  is very exciting because it allows one both for us to provide sort of a new foundation for what's
*  been thought about there, and for the all the work that's been done in those areas to, you know, to
*  give us, you know, more, more momentum to be able to figure out what's going on. Now, you know,
*  people have sort of hoped, oh, we're just going to be able to get, you know, string theory to just
*  answer everything that hasn't worked out. And I think we now kind of can see a little bit about
*  just sort of how far away certain kinds of things are from being able to explain things.
*  Some things, one of the big surprises to me, actually, I literally just got a message about
*  one aspect of this is the, you know, it's turning out to be easier. I mean, this project has been so
*  much easier than I could ever imagine it would be. That is, I thought we would be, you know,
*  just about able to understand the first 10 to the minus 100 seconds of the universe.
*  And, you know, it would be 100 years before we get much further than that. It's just turned out,
*  it actually wasn't that hard. I mean, we're not finished, but, you know,
*  You're seeing echoes of all the disparate theories of physics in this framework.
*  Yes. Yes. I mean, it's a very interesting, you know, sort of history of science like phenomenon. I
*  mean, the best analogy that I can see is what happened with the early days of computability
*  and computation theory. You know, Turing machines were invented in 1936. People sort of understand
*  computation in terms of Turing machines, but actually there had been pre-existing theories
*  of computation, combinators, general recursive functions, lambda calculus, things like this.
*  But people hadn't, those hadn't been concrete enough that people could really wrap their arms
*  around them and understand what was going on. And I think what we're going to see in this case is
*  that a bunch of these mathematical theories, including some very, I mean, one of the things
*  that's really interesting is one of the most abstract things that's come out of sort of
*  mathematics, higher category theory, things about infinity groupoids, things like this, which to me
*  always just seemed like they were floating off into the stratosphere, ionosphere of mathematics,
*  um, turn out to be things which our sort of theory anchors down to something fairly definite
*  and says are super relevant to the way that we can understand how physics works.
*  Give me a second. By the way, I just threw a hat on. You've said that, um,
*  this metaphor analogy that theory of everything is a big mountain and you have a sense that
*  however far we're up the mountain, that the, the Wolfram physics model view
*  of the universe is at least the right mountain. We're the right mountain. Yes. Without question.
*  So I'm, which aspect of it is the right mountain? So for example, I mean, so there's so many aspects
*  to just the way of the Wolfram physics project, the way it approaches the world that's, um,
*  that's clean, crisp, uh, and, uh, unique and powerful. So, you know, there's a,
*  there's discrete nature to it. There's a hyper graph. There's a computational nature. There's
*  a generative aspect. You start from nothing. You generate everything. Which do you think the actual
*  model is actually a really good one? Or do you think this general principle of, from simplicity,
*  generating complexity is the right, like what aspect of the mountain? Yeah, right. I think that
*  the, the kind of the meta idea about using simple computational systems to do things, that's,
*  you know, that's the ultimate big paradigm that is, you know, sort of super important. The details
*  of the particular model are very nice and clean and allow one to actually understand what's going
*  on. They are not unique. And in fact, we know that we know that there's a, uh, there's a large
*  number of different ways to describe essentially the same thing. I mean, I can describe things in
*  terms of hyper graphs. I can describe them in terms of higher category theory. I can describe
*  them in a bunch of different ways. They are in some sense, all the same thing, but our sort of
*  story about what's going on and the kind of, kind of cultural mathematical resonances are a bit
*  different. I think it's, it's, it's perhaps worth sort of saying a little bit about kind of the,
*  the, you know, foundational ideas of, of, uh, of, uh, uh, you know, of these, of these models and
*  things. Great. So can you maybe, uh, can we like rewind? We've talked about it a little bit,
*  but can you say like what the central idea is of the Wolfram physics project? Right. So,
*  so the question is we're interested in finding sort of simple computational rule that describes
*  our whole universe. Can we just pause on that? It's just so beautiful. That's such a beautiful
*  idea that we can generate our universe from a, from a, uh, from a data structure, a simple
*  structure, simple set of rules, and we can generate our entire universe. Yes. That's all
*  inspiring. Right. But, but so, so, you know, the question is how do you actualize that? What might
*  this rule be like? And so one thing you quickly realize is if you're going to pack everything
*  about a universe into this tiny rule, not much that we are familiar with in our universe will
*  be obvious in that rule. So you don't get to fit all these parameters of the universe, all these
*  features of, you know, this is how space works, this is how time works, et cetera, et cetera,
*  et cetera. You don't get to fit that all in. It all has to be sort of packed in to this, this thing,
*  something much smaller, much more basic, much lower level machine code, so to speak than that.
*  And all the stuff that we're familiar with has to kind of emerge from the operation of.
*  So the rule in itself, because of the computational reducibility, is not going to tell you the story.
*  It's not going to give you the answer to, it's not going to let you predict what you're going to have
*  for lunch tomorrow. Right. It's not going to let you predict basically anything about your life,
*  about the universe. Right. But and you're not going to be able to see in that rule, oh, there's the
*  three for the number of dimensions of space and so on. Right. That's not going to be the space time
*  is not going to be obviously. Right. So the question is then what is the universe made of?
*  That's a basic question. And we've had some assumptions about what the universe is made of
*  for the last few thousand years that I think in some cases just turn out not to be right.
*  And, you know, the most important assumption is that space is a continuous thing. That is that
*  you can, if you say, let's pick a point in space, we're going to do geometry, we're going to pick a
*  point, we can pick a point absolutely anywhere in space, precise numbers, we can specify where
*  that point is. In fact, you know, Euclid, who kind of wrote down the original kind of axiomatization
*  of geometry back in 300 BC or so, you know, his very first definition, he says, a point is that
*  which has no part. A point is this, you know, this indivisible, you know, infinitesimal thing.
*  Okay, so we might have said that about material objects, we might have said that about water,
*  for example, we might have said water is a continuous thing that we can just, you know,
*  pick any point we want in some water. But actually, we know it isn't true. We know that water is made
*  of molecules that are discrete. And so the question, one fundamental question is what is space made of?
*  And so one of the things that's sort of a starting point for what I've done is to think of space as
*  a discrete thing, to think of there being sort of atoms of space, just as there are atoms of
*  material things, although very different kinds of atoms. And by the way, I mean, this idea, you know,
*  there were ancient Greek philosophers who had this idea, there were, you know, Einstein actually
*  thought this is probably how things would work out. I mean, he said, you know, repeatedly, he thought
*  that's where it would work out, we don't have the mathematical tools in our time, which was 1940s,
*  1950s, and so on, to explore this. Like the way he thought, you mean that there is something
*  very, very small and discrete, that's underlying space. Yes. And that means that so, you know,
*  the mathematical theory, mathematical theories in physics, assume that space can be described
*  just as a continuous thing, you can just pick coordinates, and the coordinates can have any
*  values. And that's how you define space. Space is just sort of background, sort of
*  theater on which the universe operates. But can we draw a distinction between
*  space as a thing that could be described by three values, coordinates, and how you're,
*  are you using the word space more generally when you say? No, I'm just talking about space,
*  what we experience in the universe. So you think this 3D aspect of it is fundamental?
*  No, I don't think a 3D is fundamental at all, actually. I think that the, but the thing that
*  has been assumed is that space is this continuous thing where you can just describe it by, let's
*  say, three numbers, for instance. But most important thing about that is that you can describe it by
*  precise numbers, because you can pick any point in space, and you can talk about motions, any
*  infinitesimal motion in space. And that's what continuous means. That's what continuous means.
*  That's what, you know, Newton invented calculus to describe these kind of continuous small
*  variations and so on. That was, that's kind of a fundamental idea from Euclid on. That's been a
*  fundamental idea about space. And so- Is that right or wrong? It's not right. It's not right.
*  It's right at the level of our experience most of the time. It's not right at the level of the
*  machine code, so to speak. And so- Machine code. Yeah, of the simulation. That's right. That's right.
*  They're the very lowest level of the fabric of the universe, at least under the Wolfram physics model,
*  is your senses is discrete. Right. So now, what does that mean? So it means, what is space then?
*  So in models, the basic idea is you say, there are these sort of atoms of space,
*  there are these points that represent, you know, represent places in space. But they're just
*  discrete points. And the only thing we know about them is how they're connected to each other.
*  We don't know where they are. They don't have coordinates. We don't get to say this is a
*  position such and such. It's just, here's a big bag of points. Like in our universe, there might
*  be 10 to the 100 of these points. And all we know is this point is connected to this other point. So
*  it's like, you know, all we have is the friend network, so to speak. We don't have, you know,
*  people's, you know, physical addresses. All we have is the friend network of these points.
*  The underlying nature of reality is kind of like a Facebook, we don't know their location,
*  but we have the friends. Yeah, yeah, right. We know which point is connected to which other points.
*  And that's all we know. And so you might say, well, how on earth can you get something which is like
*  our experience of, you know, what seems like continuous space? Well, the answer is, by the
*  time you have 10 to the 100 of these things, those connections can work in such a way that
*  on a large scale, it will seem to be like continuous space in, let's say, three dimensions or
*  some other number of dimensions or 2.6 dimensions or whatever else. Because they're much, much,
*  much, much larger. So like the number of relationships here we're talking about is just
*  a humongous amount. So the kind of thing you're talking about is very, very, very small relative
*  to our experience of daily life. Right. So I mean, you know, we don't know exactly the size, but maybe
*  maybe 10 to the minus, maybe around 10 to the minus 100 meters. So, you know, the size of,
*  to give a comparison, the size of a proton is 10 to the minus 15 meters. And so this is something
*  incredibly tiny compared to that. And the idea that from that would emerge the experience
*  of continuous space is mind blowing. Well, what's your intuition? Why that's possible? Like,
*  first of all, I mean, we'll get into it, but I don't know if we will through the medium of
*  conversation, but the construct of hypografts is just beautiful. Right. Cellulatometer beautiful.
*  We'll talk about it, but this thing about, you know, continuity arising from discrete systems
*  is in today's world is actually not so surprising. I mean, you know, your average computer screen,
*  right? Every computer screen is made of discrete pixels, yet we have the, you know, we have the
*  idea that we're seeing these continuous pictures. I mean, it's, you know, the fact that on a large
*  scale, continuity can arise from lots of discrete elements. This is at some level unsurprising now.
*  Whoa, wait, wait, wait, wait, wait. But the pixels have a very definitive structure of neighbors
*  on a computer screen. Right. There's no concept of spatial, of space inherent in the underlying
*  fabric of reality. Right, right, right. So the point is, but there are cases where there are.
*  So for example, let's just imagine you have a square grid. Okay. And at every point on the grid,
*  you have one of these atoms of space and it's connected to four other four other atoms of space
*  on the, you know, Northeast Southwest corners, right? There you have something where if you zoom
*  out from that, it's like a computer screen. Yeah. So the relationship creates the spatial,
*  like the relationship creates a constraint, which then in an emergent sense creates a like,
*  yeah, like a, uh, basically a spatial coordinate for that thing. Yeah. Right. Even though the
*  individual point doesn't have a space. Even though the individual point doesn't know anything,
*  it just knows what it's, you know, what its neighbors are. They, on a large scale,
*  it can be described by saying, oh, it looks like it's a, you know, this grid is zoomed out grid.
*  You can say, well, you can describe these different points by saying they have certain positions,
*  coordinates, et cetera. Now in the, in the sort of real setup, it's more complicated than that. It
*  isn't just a square grid or something. It's something much more dynamic and complicated,
*  which we'll talk about. But, um, uh, so, you know, first, the first idea, the first key idea is,
*  you know, what's the universe made of? It's made of atoms of space, basically with these
*  connections between them. What kind of connections do they have? Well, so a, the simplest kind of
*  thing you might say is we've got something like a graph where every, uh, every atom of space,
*  uh, where we have these edges that go between out of these connections that go between atoms
*  of space. We're not saying how long these edges are. We're just saying there is a connection from,
*  from this place to the, from this atom to this. Just a quick pause, cause there's a lot of very
*  people that listen to this just to clarify, cause I did a poll actually. What do you think a graph
*  is a long time ago? And it's kind of funny how few people know the term graph, uh, outside of
*  computer science. Let's call it a network. I think that's calling a network is better. So,
*  but every time I like the word graph though, so let's define, let's just say that a graph
*  will use terms, nodes and edges maybe. And it's just, uh, nodes represent some abstract entity.
*  And then the edges represent relationships between those entities. So that's what a graph,
*  so there you go. So that's the basic structure. That is, that is the simplest case of a basic
*  structure. Actually, uh, it tends to be better to think about hyper graphs.
*  So hyper graph is just, instead of saying, uh, there are connections between pairs of things,
*  we say there are connections between any number of things. So there might be ternary edges. So
*  instead of, instead of just having, uh, two points are connected by an edge, you say three points are
*  all associated with a hyper edge, are all connected by a hyper edge. That's just at some level,
*  that's at some level, that's a detail. It's a detail that happens to make the, um, for me,
*  you know, sort of in the history of this project, the realization that you could do things that way
*  broke out of certain kinds of arbitrariness that I felt that there was in the model before I had
*  seen how this worked. I mean, all hyper graph can be mapped to a graph. It's just a convenient
*  representation, mathematical. Right. That's correct. That's correct. But so then, so, okay.
*  So the, the first question, the first idea of these models of ours is space is made of these,
*  you know, connected sort of atoms of space. The next idea is space is all there is. There's nothing
*  except for this space. So in traditional ideas in physics, people have said there's space. It's kind
*  of a background. And then there's matter, all these particles, electrons, all these other things
*  which exist in space. Right. But in this model, one of the key ideas is there's nothing except space.
*  So in other words, everything that has that exists in the universe is a feature of this hyper
*  graph. So how can that possibly be? Well, the way that works is that there are certain structures
*  in this hyper graph where you say that little twisty knotted thing. We don't know exactly how
*  this works yet, but we have sort of idea about how it works mathematically. This sort of twisted
*  knotted thing, that's the core of an electron. This thing over there that has this different
*  form, that's something else. So the different peculiarities of the structure of this graph
*  are the very things that we think of as the particles inside the space, but in fact,
*  it's just a property of the space. Mind blowing, first of all. It's mind blowing,
*  and we'll probably talk in its simplicity and beauty. Yes, I think it's very beautiful.
*  Okay, so that space, and then there's another concept we didn't really kind of mention, but
*  you think it of computation as a transformation. Let's talk about time in a second. On the subject
*  of space, there's this question of kind of what, there's this idea, there is this hyper graph,
*  it represents space and it represents everything that's in space. The features of that hyper graph,
*  you can say certain features in this part we do know, certain features of the hyper graph
*  represent the presence of energy, for example, or the presence of mass or momentum. And we know what
*  the features of the hyper graph that represent those things are, but it's all just the same
*  hyper graph. So one thing you might ask is, if you just look at this hyper graph and you say,
*  we're going to talk about sort of what the hyper graph does, but if you say, how much of what's
*  going on in this hyper graph is things we know and care about, like particles and atoms and electrons
*  and all this kind of thing, and how much is just the background of space? So it turns out, so far
*  in one rough estimate of this, everything that we care about in the universe is only one part in 10
*  to the 120 of what's actually going on. The vast majority of what's happening is purely things that
*  maintain the structure of space. In other words, the things that are the features of space that
*  are the things that we consider notable, like the presence of particles and so on, that's a tiny
*  little piece of froth on the top of all this activity that mostly is just intended to,
*  you know, mostly, I can't say intended, there's no intention here that just maintains the structure
*  of space. Let me load that in. It just makes me feel so good as a human being. To be the froth on
*  the one in the 10 to the 120 or something of well, and also just humbling how in this mathematical
*  framework, how much work needs to be done on the infrastructure. Right. Yes, our universe, right.
*  To maintain the infrastructure of our universe is a lot of work. We are merely writing a little tiny
*  things on top of that infrastructure. But, you know, you were just starting to talk a little
*  bit about what, you know, we talked about, you know, space that represents all the stuff that's
*  in the universe. The question is, what does that stuff do? And for that, we have to start talking
*  about time and what is time and so on. And, you know, one of the basic idea of this model is time
*  is the progression of computation. So in other words, we have a structure of space and there is
*  a rule that says how that structure of space will change. And it's the application, the repeated
*  application of that rule that defines the progress of time. And what does the rule look like in the
*  space of hypergraphs? Right. So what the rule says is something like if you have a little tiny piece
*  of hypergraph that looks like this, then it will be transformed into a piece of hypergraph that looks
*  like this. So that's all it says. It says you pick up these elements of space and you can think of
*  these edges, these hyper edges as being relations between elements in space. You might pick up
*  these two relations between elements in space. And we're not saying where those elements are
*  or what they are, but every time there's a certain arrangement of elements in space,
*  then arrangement in the sense of the way they're connected, then we transform it into some other
*  arrangement. So there's a little tiny pattern and you transform into another little pattern.
*  That's right. And then because of this, I mean, again, it's kind of similar to cellular automata
*  and that like, yes, on paper, the rule looks like super simple. It's like, yeah, okay. Yeah,
*  yeah, right. From this, the universe can be born. But like, once you start applying it,
*  beautiful structure starts being potentially can be created. And what you're doing is you're applying
*  that rule to different parts. Like any time you match it within the hypergraph. Exactly. And then
*  one of the like incredibly beautiful and interesting things to think about is the order in which you
*  apply that rule. Yes. Because that pattern appears all over the place. Right. So this is a big
*  complicated thing, very hard to wrap one's brain around. Okay. So you say the rule is every time
*  you see this little pattern, transform it in this way. But yet, you know, as you look around
*  the space that represents the universe, there may be zillions of places where that little pattern
*  occurs. So what it says is just do this, apply this rule wherever you feel like. And what is
*  extremely non-trivial is, well, okay, so this is happening sort of in computer science terms,
*  sort of asynchronously. You're just doing it wherever you feel like doing it.
*  And the only constraint is that if you're going to apply the rule somewhere, the things to which
*  you apply the rule, the little, you know, elements to which you apply the rule, if they have to be,
*  okay, well, you can think of each application of the rule as being kind of an event that happens
*  in the universe. And these the input to an event has to be ready for the event to occur. That is,
*  if one event occurred, if one transformation occurred, and it produced a particular atom of
*  space, then that atom of space has to already exist before another transformation that's going
*  to apply to that atom of space can occur. So that's like the prerequisite for the event.
*  That's right. That defines a kind of this sort of set of causal relationships between events. It
*  says this event has to have happened before this event. But that is some...
*  But that's not a very limiting constraint.
*  No, it's not. And what's interesting...
*  You still get the zillion, that's a technical term, options.
*  That's correct. But okay, so this is where things get a little bit more elaborate.
*  They're mind-blowing.
*  Right. So what happens is, so the first thing you might say is, you know, let's, well, okay,
*  so this question about the freedom of which event you do when, well, let me sort of state
*  an answer and then explain it. Okay? The validity of special relativity is a consequence of the
*  fact that in some sense, it doesn't matter in what order you do these underlying things,
*  so long as they respect this kind of set of causal relationships.
*  So that's... The part that's in a certain sense is a really important one, but the fact that
*  it sometimes doesn't matter. That's a... I don't know, that's another beautiful thing.
*  So there's this idea of what I call causal invariance.
*  Causal invariance, exactly. That's a really, really powerful idea.
*  Powerful idea, which has actually arisen in different forms many times in the history of
*  mathematics, mathematical logic, even computer science. It has many different names. I mean,
*  our particular version of it is a little bit tighter than other versions, but it's basically
*  the same idea. Here's how to think about that idea. So imagine that... Well, let's talk about
*  it in terms of math for a second. Let's say you're doing algebra and you're told, you know,
*  multiply out this series of polynomials that are multiplied together, okay? You say, well,
*  which order should I do that in? Say, well, do I multiply the third one by the fourth one and then
*  do it by the first one, or do I do the fifth one by the sixth one and then do that? Well, it turns
*  out it doesn't matter. You can multiply them out in any order. You'll always get the same answer.
*  That's a property. If you think about kind of making a kind of network that represents
*  in what order you do things, you'll get different orders for different ways of multiplying things
*  out, but you'll always get the same answer. Same thing if you... Let's say you're sorting. You've
*  got a bunch of A's and B's. They're in some random order, you know, BAA, BBBAA, whatever.
*  And you have a little rule that says every time you see BAA, flip it around to AB. Okay? Eventually,
*  you apply that rule enough times, you'll have sorted the string so that it's all the A's first
*  and then all the B's. Again, there are many different orders in which you can do that,
*  many different sort of places where you can apply that update. In the end, you'll always get the
*  string sorted the same way. I know with sorting a string, it sounds obvious. That's to me a
*  surprising that there is in complicated systems, obviously with a string, but in a hypergraph that
*  the application of the rule, asynchronous rule can lead to the same results sometimes.
*  Yes. Yes. That is not obvious. And it was something that, you know, I sort of discovered
*  that idea for these kinds of systems back in the 1990s. And for various reasons, I was not
*  satisfied by how sort of fragile finding that particular property was. And let me just make
*  another point, which is that it turns out that even if the underlying rule does not have this
*  property of causal invariance, it can turn out that every observation made by observers of the rule
*  they can impose what amounts to causal invariance on the rule. We can explain that. It's a little
*  bit more complicated. I mean, technically that has to do with this idea of completions,
*  which is something that comes up in term rewriting systems, automated theorem proving systems and so
*  on. But let's ignore that for a second. We can come to that later. But- Is it useful to talk
*  about observation? Not yet. Not yet. Okay. So great. So there's some concept of causal invariance
*  as you apply these rules and in asynchronous way, you can think of those transformations as events.
*  So there's this hypergraph that represents space and all of these events happening in the space and
*  the graph grows in interesting, complicated ways. And eventually the froth arises to of what we
*  experience as human existence. So that's some version of the picture, but let's explain a little
*  bit more. Yeah, exactly. What's a little more detail like- Right. Well, so one thing that is
*  sort of surprising in this theory is one of the sort of achievements of 20th century physics was
*  bringing space and time together. That was special relativity. People talk about space-time,
*  this sort of unified thing where space and time kind of are mixed. And there's a nice mathematical
*  formalism in which space and time sort of appear as part of the space-time continuum, the space-time
*  four vectors and things like this. We talk about time as the fourth dimension and all these kinds
*  of things. And it seems like the theory of relativity sort of says space and time are
*  fundamentally the same kind of thing. So one of the things that took a while to understand in this
*  approach of mine is that in my kind of approach, space and time are really not fundamentally the
*  same kind of thing. Space is the extension of this hypergraph. Time is the kind of progress of this
*  inexorable computation of these rules getting applied to the hypergraph. So they seem like very
*  different kinds of things. And so that at first seems like how can that possibly be right? How
*  can that possibly be Lorentz invariant? That's the term for things being following the rules of
*  special relativity. Well, it turns out that when you have causal invariance, that- and let's see,
*  we can- it's worth explaining a little bit how this works. It's a little bit elaborate,
*  but the basic point is that even though space and time sort of come from very different places,
*  it turns out that the rules of sort of space-time that special relativity talks about come out of
*  this model when you're looking at large enough systems. So a way to think about this, you know,
*  in terms of when you're looking at large enough systems, the part of that story is when you look
*  at some fluid like water, for example, there are equations that govern the flow of water.
*  Those equations are things that apply on a large scale. If you look at the individual molecules,
*  they don't know anything about those equations. It's just the sort of the large scale effect of
*  those molecules turns out to follow those equations. And it's the same kind of thing
*  happening in our models. I know this might be a small point, but it might be a very big one.
*  We've been talking about space and time at the lowest level of the model, which is space,
*  the hypergraph, time is the evolution of this hypergraph. But there's also space-time that
*  we think about in general relativity for your special relativity. Like what, how does, how do you
*  go from the lowest source code of space and time as we're talking about to the more traditional
*  terminology of space and time? Yeah, right. So the key thing is this thing we call the causal
*  graph. So the causal graph is the graph of causal relationships between events. So every one of
*  these little updating events, every one of these little transformations of the hypergraph happens
*  somewhere in the hypergraph happens at some stage in the computation. That's an event. That event
*  has a causal relationship to other events in the sense that if another event needs as its input
*  the output from the first event, there will be a causal relationship of the future event will
*  depend on the past event. So you can say it has a causal connection. So you can make this graph
*  of causal relationships between events. That graph of causal relationships, causal invariance,
*  implies that that graph is unique. It doesn't matter. Even though you think, oh, I'm, you know,
*  let's say we were sorting a string, for example. I did that particular transposition of characters
*  at this time. Then I did that one. Then I did this one. Turns out if you look at the network of
*  connections between those updating events, that network is the same. It's the, if you were to,
*  the structure. So in other words, if you were to draw that, if you were to put that network on a
*  picture of where you're doing all the updating, the places where you put the nodes of the network
*  will be different. But the way the nodes are connected will always be the same. So, but the
*  causal graph is a, is, I don't know, it's kind of an observation. It's not enforced. It's just emergent
*  from a set of events. It's a feature of, okay, so what it is, the characteristic, I guess,
*  is the way events happen. Right. It's an event can't happen until its input is ready. Right. And so
*  that creates this network of causal relationships. And that's the causal graph. And the thing,
*  the next thing to realize is, okay, we, when you're going to observe what happens in the universe,
*  you have to sort of make sense of this causal graph. So, and you are an observer who yourself
*  is part of this causal graph. And so that means, so let me give you an example of how that works. So
*  imagine we have a really weird theory of physics of the world where it says this updating process,
*  there's only going to be one update at every moment in time. And there's just going to be like a
*  Turing machine that has a little head that runs around and just is always just updating one thing
*  at a time. So you say, you know, I have a theory of physics and the theory of physics says there's
*  just this one little place where things get updated. You say that's completely crazy because,
*  you know, it's plainly obvious that things are being updated sort of, you know, at the same time.
*  Yeah. But the fact is that the thing is that if I'm, you know, talking to you and you seem
*  to be being updated as I'm being updated, but if there's just this one little head that's running
*  around updating things, I will not know whether you've been updated or not until I'm updated.
*  So in other words, draw this causal graph of the causal relationship between the updatings in you
*  and the updatings in me, it'll still be the same causal graph, whether even though the underlying
*  story of what happens is, oh, there's just this one little thing and it goes and updates in
*  different places in the universe. So is that clear or is that a hypothesis? Is that clear
*  that there's a unique causal graph? If there's causal invariance, there's a unique causal graph.
*  So it's okay to think of what we're talking about as a hypo graph and the operations on it as a kind
*  of Turing machine with a single head, like a single guy running around updating stuff.
*  Is that safe to intuitively think of it this way? Let me think about that for a second. Yes,
*  I think so. I think there's nothing, it doesn't matter. I mean, you can say, okay, there is one,
*  the reason I'm pausing for a second is that I'm wondering, well, when you say running around,
*  depends how far it jumps every time it runs. Yeah, yeah, that's right. But I mean, like,
*  one operation at a time. Yeah, you can think of it as one operation at a time.
*  It's easier for the human brain to think of it that way as opposed to simultaneous.
*  Okay, but the thing is, that's not how we experience the world. What we experience is,
*  we look around, everything seems to be happening at successive moments in time everywhere in space.
*  Yes. And that's partly a feature of our particular construction. I mean, that is,
*  the speed of light is really fast compared to, you know, we look around, you know, I can see maybe
*  100 feet away right now. You know, it's the, my brain does not process very much in the time
*  it takes light to go 100 feet. The brain operates at a scale of hundreds of milliseconds or something
*  like that. I don't know. And speed of light is much faster. Right. You know, light goes, in a
*  billionth of a second, light has gone afoot. So it goes a billion feet every second. There's certain
*  moments through this conversation where I imagine the absurdity of the fact that there's two
*  descendants of apes modeled by a hypergraph that are communicating with each other and experiencing
*  this whole thing as a real time simultaneous update with, I'm taking in photons from you right now,
*  but there's something much, much deeper going on right here. It does have a, it's paralyzing
*  sometimes to just to remember that. Right. No, I mean, you know, but, but so, you know,
*  yes, yes. No, as a small little tangent, I just remembered that we're talking about, I mean, this
*  about the fabric of reality. Right. So we've got this causal graph that represents the sort
*  of causal relationships between all these events in the universe. That causal graph kind of is a
*  representation of space time, but our experience of it requires that we pick reference frames.
*  This is kind of a key idea. Einstein had this idea that what that means is we have to say,
*  what are we going to pick as being the sort of what we define as simultaneous moments in time?
*  So for example, we can say, you know, we, we, how do we set our clocks? You know, if we've got a
*  spacecraft landing on Mars, you know, do we say that, you know, what, what time is it landing at?
*  Was it, you know, even though there's a 20 minute speed of light delay or something, you know,
*  what time do we say it landed at? How do we, how do we set up sort of time coordinates for the world?
*  And that turns out to be that there's kind of this arbitrariness to how we set these reference
*  frames that define sort of what counsel simultaneous and what is the, the essence of special relativity
*  is to think about reference frames going at different speeds and to think about sort of how
*  they assign what counts as space, what counts as time and so on. That's all a bit technical,
*  but the basic bottom line is that the, this causal invariance property that means that it's always
*  the same causal graph independent of how you slice it with these reference frames, you'll always sort
*  of see the same physical processes go on. And that's basically why special relativity works.
*  So there's something like special relativity, like everything around space and time that,
*  that fits this idea of the causal graph. Right. Well, you know, one way to think about it is
*  given that you have a basic structure that just involves updating things in, in these, you know,
*  connected updates and looking at the causal relationships from connected updates, that's
*  enough. When you unravel the consequences of that, that together with the fact that there are lots
*  of these things and that you can take a continuum limits and so on implies special relativity.
*  And so that it's kind of a, not a big deal because it's kind of, it's kind of a, you know,
*  it was completely unobvious when you started off with saying, we've got this graph, it's being
*  updated in time, et cetera, et cetera, et cetera. That just looks like nothing to do with special
*  relativity. And yet you get that. And what, I mean, then the thing, I mean, this was stuff that I
*  figured out back in the 1990s, the, the, the next big thing you get is general relativity.
*  And so in this hypergraph, the, this sort of limiting structure, when you have a very big
*  hypergraph, you can think of as being just like, you know, water seems continuous on a large scale.
*  So this hypergraph seems continuous on a large scale. One question is, you know, how many
*  dimensions of space does it correspond to? So one question you can ask is if you've just got a bunch
*  of points and they're connected together, how do you deduce what effective dimension of space
*  that bundle of points corresponds to? And that's, that's pretty easy to explain. So basically,
*  if you say you've got a point and you look at how many neighbors does that point have, okay,
*  imagine it's on a square grid, then it'll have four neighbors go another level out. How many
*  neighbors do you get then? What you realize is as you go more and more levels out, as you go more
*  and more distance on the graph out, you're, you're capturing something which is essentially a circle
*  in two dimensions. So that, you know, the, the number of the area of a circle is pi r squared.
*  So the, it's the number of points that you get to goes up like the distance you've gone squared.
*  And in general, in d dimensional space, it's r to the power d, it's the, the number of points you get
*  to if you go r steps on the graph grows like the number of steps you go to the power of the dimension.
*  And that's a, that's a way that you can estimate the effective dimension of one of these graphs.
*  So what does that grow to? So how does the dimension grow? There's a, I mean, obviously,
*  the visual aspect of these hyper graphs, they're often visualized in three dimensions,
*  and then there's a certain kind of structure. Like you said, there's the, I mean, a circle,
*  a sphere, there's a planar aspect to it. Right. To this graph, to where it kind of,
*  it almost starts creating a surface, like a complicated surface, but a surface. So how does
*  that connect to effective dimension? Okay, so if you can lay out the graph in such a way that the,
*  that the points in the graph, that, you know, that the points that are neighbors on the graph
*  are neighbors as you lay them out, and you can do that in two dimensions, then it's going to
*  approximate a two dimensional thing. If you can't do that in two dimensions, if everything would
*  have to fold over a lot in two dimensions, then it's not approximating a two dimensional thing.
*  Maybe you can lay it out in three dimensions. Maybe you have to lay it out in five dimensions
*  to have it be the case that it sort of smoothly lays out like that. Well, but okay, so,
*  and I apologize for the different tangent questions, but you know, there's an infinity
*  number of possible rules. So we have to look for rules that, that create the kind of structures
*  that are reminiscent for, that have echoes of the different physics theories in them. So what kind
*  of rules, is there something simple to be said about the kind of rules that you have found
*  beautiful, that you have found powerful? So, so I mean, what, you know, one of the features of
*  computational irreducibility is it's very, you can't say in advance what's going to happen
*  with any particular, you can't say, I'm going to pick these rules from this part of rule space,
*  so to speak, because they're going to be the ones that are going to work. That's, you can make some
*  statements along those lines, but you can't generally say that. Now, you know, the state of
*  what we've been able to do is, you know, different properties of the universe, like dimensionality,
*  you know, integer dimensionality, features of other features of quantum mechanics, things like
*  that. At this point, what we've got is we've got rules that, that any one of those features,
*  we can get a rule that has that feature. So we don't have the sort of the final, here's a rule
*  which has all of these features, we do not have that yet. So if I were to try to summarize the
*  Wolfram physics project, which is, you know, something that's been in your brain for a long
*  time, but really has just exploded in activity, you know, only just months ago. Yes. So it's an
*  evolving thing. And next week, I'll try to publish this conversation as quickly as possible,
*  because by the time it's published, already new things will probably have come out. So,
*  so if I were to summarize it, we've talked about the basics of there's a hypergraph that represents
*  space, there is transformations in the hypergraph that represents time, that progress of time,
*  there's a cause of graph, that's a characteristic of this. And the basic process of science,
*  of, yeah, of science within the Wolfram physics model, is to try different rules and see which
*  properties of physics that we know of known physical theories are appear within the graphs
*  that emerge from that rule. That's what I thought it was going to be. Oh, okay. So what,
*  so what is it? It turns out we can do a lot better than that. It turns out that using kind of
*  mathematical ideas, we can say, and computational ideas, we can make general statements. And those
*  general statements turn out to correspond to things that we know from 20th century physics.
*  In other words, the idea of you just try a bunch of rules and see what they do. That's what I thought
*  we were going to have to do. But in fact, we can say, given causal invariance and computational
*  reducibility, we can derive, and this is where it gets really pretty interesting, we can derive
*  special relativity, we can derive general relativity, we can derive quantum mechanics.
*  And that's where things really start to get exciting, is, you know, it wasn't at all obvious
*  to me that even if we were completely correct, and even if we had, you know, this is the rule,
*  you know, even if we found the rule, to be able to say, yes, it corresponds to things we already know,
*  I did not expect that to be the case. And so for somebody who is a simple mind,
*  and definitely not a physicist, not even close, what does derivation mean in this case?
*  Okay, so, so let me, this is an interesting question. Okay, so there's, so one one thing
*  in the context of computational reducibility. Yeah, yeah, right. Right. So what you have to do,
*  let me get, let me go back to, again, the mundane example of fluids and water and things like that,
*  right? So, so you have a bunch of molecules bouncing around, you can say, just as a piece
*  of mathematics, I happened to do this from cellular automata back in the mid 1980s, you can say,
*  just as a matter of mathematics, you can say, the continuum limit of these little molecules
*  bouncing around is the Navier-Stokes equations. That's just a piece of mathematics. It's not,
*  it doesn't rely on, you have to make certain assumptions that you have to say, there's enough
*  randomness in the way the molecules bounce around that certain statistical averages work, etc., etc.,
*  etc. Okay, it is a very similar derivation to derive, for example, the Einstein equations.
*  Okay, so the way that works, roughly, the Einstein equations are about curvature of space.
*  Curvature of space, I talked about sort of how you can figure out dimension of space. There's a
*  similar kind of way of figuring out if you just sort of say, you know, you're making a larger and
*  larger ball or larger and larger, if you draw a circle on the surface of the earth, for example,
*  you might think the area of a circle is pi r squared, but on the surface of the earth,
*  because it's a sphere, it's not flat, the area of a circle isn't precisely pi r squared. As the
*  circle gets bigger, the area is slightly smaller than you would expect from the formula pi r
*  squared as a little correction term that depends on the ratio of the size of the circle to the
*  radius of the earth. Okay, so it's the same basic thing allows you to measure from one of these
*  hypergraphs, what is its effective curvature. And that's-
*  So the little piece of mathematics that explains special general relativity
*  can map nicely to describe fundamental property of the hypergraphs, the curvature of the hypergraphs.
*  So special relativity is about the relationship of time to space. General relativity is about
*  curvature in this space represented by this hypergraph. So what is the curvature of a
*  hypergraph? Okay, so first I have to explain, what we're explaining is, first thing you have to have
*  is a notion of dimension. You don't get to talk about curvature of things. If you say, oh, it's
*  a curved line, but I don't know what a line is yet. So what is the dimension of a hypergraph then?
*  From where we've talked about effective dimension, but-
*  Right, that's what this is about. What this is about is, you have your hypergraph, it's got a
*  trillion nodes in it. What is it roughly like? Is it roughly like a grid, a two-dimensional grid?
*  Is it roughly like all those nodes are arranged on a line? What's it roughly like? And there's a
*  pretty simple mathematical way to estimate that by just looking at this thing I was describing,
*  the size of a ball that you construct in the hypergraph. You just measure that, you can just
*  compute it on a computer for a given hypergraph, and you can say, oh, this thing is wiggling around,
*  but it roughly corresponds to two or something like that, or roughly corresponds to 2.6 or whatever.
*  So that's how you have a notion of dimension in these hypergraphs. Curvature is something a little
*  bit beyond that. If you look at how the size of this ball increases as you increase its radius,
*  curvature is a correction to the size increase associated with dimension. It's a second-order
*  term in determining the size. Just like the area of a circle is roughly pi r squared, so it goes
*  up like r squared, the 2 is because it's in two dimensions, but when that circle is drawn on a big
*  sphere, the actual formula is pi r squared times one minus r squared over a squared and some
*  coefficient. In other words, there's a correction, and that correction term, that gives you curvature,
*  and that correction term is what makes this hypergraph have the potential to correspond
*  to curved space. Now, the next question is, is that curvature, is the way that curvature works,
*  the way that Einstein's equations for general relativity, is it the way they say it should work?
*  And the answer is yes, and so how does that work? The calculation of the curvature of this hypergraph
*  for some set of rules? No, it doesn't matter what the rules are. So long as they have causal
*  invariance and computational irreducibility, and they lead to finite dimensional space,
*  non-infinite dimensional space, non-dimensional. It can grow infinitely, but it can't be infinite
*  dimensional. So what does infinitely dimensional hypergraph look like? So in a tree, you start from
*  one root of the tree, it doubles, doubles again, doubles again, doubles again, and that means if
*  you ask the question, starting from a given point, how many points do you get to? Remember, like a
*  circle, you get to R squared with a two there. On a tree, you get to, for example, two to the R.
*  It's exponential dimensional, so to speak, or infinite dimensional. Do you have a sense of,
*  in the space of all possible rules, how many lead to infinitely dimensional hypergraphs?
*  No. Is that an important thing to know? Yes, it's an important thing to know. I would love to know
*  the answer to that. But it gets a little bit more complicated because, for example, it's
*  very possible the case that in our physical universe, that the universe started infinite
*  dimensional. And it only, as the, you know, at the Big Bang, it was very likely infinite dimensional.
*  And as the universe sort of expanded and cooled, its dimension gradually went down.
*  And so one of the bizarre possibilities, which actually there are experiments you can do to try
*  and look at this, the universe can have dimension fluctuations. So in other words, we think we live
*  in a three dimensional universe, but actually there may be places where it's actually 3.01
*  dimensional or where it's, you know, 2.99 dimensional. And it may be that in the very
*  early universe, it was actually infinite dimensional. And it's only a late stage
*  phenomenon that we end up getting three dimensional space. But from your perspective of the hypergraph,
*  one of the underlying assumptions kind of implied, but you have a sense, a hope,
*  a set of assumptions that the rules that underlie our universe or the rule that underlies our
*  universe is static. Is that the one of the assumptions you're currently operating under?
*  Yes, but there's a footnote to that which we should get to because it requires a few more steps.
*  Okay. Well, actually then, but let's backtrack to the curvature because we're talking about,
*  as long as it's finite dimensional.
*  Fine dimensional computational irreducibility and causal invariance, then it follows that
*  the large scale structure will follow Einstein's equations. And now let me again qualify that a
*  little bit more. There's a little bit more complexity to it. So Einstein's equations in
*  their simplest form apply to the vacuum, no matter just the vacuum. And they say,
*  in particular, what they say is if you have, so there's this term geodesic, that's a term that
*  means shortest path comes from measuring shortest paths on the earth. So you look at a bunch of,
*  a bundle of geodesics, a bunch of shortest paths. It's like the paths that photons would take
*  between two points. Then the statement of Einstein's equations is basically a statement about
*  a certain, that as you look at a bundle of geodesics, the structure of space has to be such that
*  although the cross-sectional area of this bundle may, although the actual shape of the cross-section
*  may change, the cross-sectional area does not. That's a version, that's the most simple minded
*  version of army nu minus a half of g mu nu equals zero, which is the more mathematical version of
*  Einstein's equations. It's a statement, it's a statement of the thing called the Ricci tensor
*  is equal to zero. That's Einstein's equations for the vacuum. Okay, so we get that as a result of
*  this model, but footnote, big footnote, because all the matter in the universe is the stuff we
*  actually care about. The vacuum is not stuff we care about. So the question is how does matter
*  come into this? For that, you have to understand what energy is in these models. One of the things
*  that we realized last year was that there's a very simple interpretation of energy in these models.
*  Energy is basically, well, intuitively, it's the amount of activity in these hypergraphs
*  and the way that that remains over time. So a little bit more formally, you can think about
*  this causal graph as having these edges that represent causal relationships. You can think
*  about, oh boy, there's one more concept that we didn't get to. The notion of space-like hypersurfaces.
*  So this is not as scary as it sounds. It's a common notion in general relativity. The notion is
*  you are defining what is a possibly, what is, what, where in space-time might be
*  a particular moment in time. So in other words, what is a consistent set of places where you can
*  say this is happening now, so to speak, and you make this series of sort of slices through the
*  space-time, through this causal graph to represent sort of what we consider to be successive moments
*  in time. It's somewhat arbitrary because you can deform that if you're going at a different speed
*  and special relativity. You tip those things. There are different kinds of deformations,
*  but only certain deformations are allowed by the structure of the causal graph. Anyway,
*  be there as it may. The basic point is there is a way of figuring out, you say what is the
*  energy associated with what's going on in this in this hypergraph? And the answer is there is a
*  precise definition of that. And it is the formal way to say it is it's the flux of causal edges
*  through space-like hypersurfaces. The slightly less formal way to say it, it's basically the
*  amount of activity. See, the reason it gets tricky is you might say it's the amount of activity per
*  unit volume in this hypergraph, but you haven't defined what volume is. So it's a little bit that
*  you have to be able to- But this hypersurface gives some more formalism to that. Yeah, yeah.
*  It gives a way to connect that. But intuitively we should think about it as the amount of activity.
*  Right. So the amount of activity that kind of remains in one place in the hypergraph
*  corresponds to energy. The amount of activity that is kind of where an activity here affects
*  an activity somewhere else corresponds to momentum. And so one of the things that's kind of cool
*  is that- I'm trying to think about how to say this intuitively. The mathematics is easy,
*  but the intuitive version I'm not sure. But basically the way that things sort of stay in
*  the same place and have activity is associated with rest mass. And so one of the things that
*  you get to derive is E equals MC squared. That is a consequence of this interpretation of energy
*  in terms of the way the causal graph works, which is the whole thing is sort of a consequence of
*  this whole story about updates in hypergraphs and so on. So can you linger on that a little bit?
*  How do we get E equals MC squared? So where does the mass come from? So-
*  Okay, okay. I mean, is there an intuitive- It's okay. First of all, you're pretty deep in the
*  mathematical explorations of this thing right now. We're in a very- we're in a flux
*  currently. So maybe you haven't even had time to think about intuitive explanations.
*  This one is, look, roughly what's happening, that derivation is actually rather easy.
*  I've been saying we should pay more attention to this derivation because it's such- because
*  people care about this one. But everybody says, it's just easy. It's easy.
*  So there's some concept of energy that can be thought of as the activity, the flux,
*  the level of changes that are occurring based on the transformations within a certain volume,
*  however the heck do you find the volume? Okay. So, and then mass-
*  Well, mass is associated with kind of the energy that does not cause you to- that does not
*  somehow propagate through time. Yeah, I mean, one of the things that was not obvious in the
*  usual formulation of special relativity is that space and time are connected in a certain way,
*  energy and momentum are also connected in a certain way. The fact that the connection of
*  energy to momentum is analogous to the connection to space between space and time is not self-evident
*  in ordinary relativity. It is a consequence of this- of the way this model works. It's an
*  intrinsic consequence of the way this model works. And it's all to do with that- with
*  unraveling that connection that ends up giving you this relationship between energy and- well,
*  it's energy, momentum, mass, they're all connected. And so that's hence the general relativity.
*  You have a sense that it appears to be baked in to the fundamental properties of the way these
*  hypergraphs are evolved. Well, I didn't yet get to- so I got as far as special relativity and
*  equals MC squared. The one last step is in general relativity, the final connection is
*  energy and mass cause curvature in space. And that's something that when you understand this
*  interpretation of energy and you kind of understand the correspondence to curvature and hypergraphs,
*  then you can finally sort of- the big final answer is you derive the full version of Einstein's
*  equations for space, time and matter. And that's- So is that- have you- that last piece with
*  curvature, have- is that- have you arrived there yet? Oh yeah, we're there. Yes. And here's the way
*  that we- here's how we're really, really going to know we've arrived, okay? So we have the
*  mathematical derivation, it's all fine, but you know, mathematical derivations- okay, so one thing
*  that's sort of a- you know, we're taking this limit of what happens when- the limit, you have
*  to look at things which are large compared to the size of an elementary length, small compared to
*  the whole size of the universe, large compared to certain kinds of fluctuations, blah, blah, blah.
*  There's a tower of many, many of these mathematical limits that have to be taken.
*  So if you're a pure mathematician saying, where's the precise proof? It's like, well, there are all
*  these limits, we can, you know, we can try each one of them computationally and we could say,
*  yeah, it really works, but the formal mathematics is really hard to do. I mean, for example, in the
*  case of deriving the equations of fluid dynamics from molecular dynamics, that derivation has never
*  been done. There is no rigorous version of that derivation. So- Because you can't do the limits?
*  Yeah, because you can't do the limits. So the limits allow you to try to describe something
*  general about the system and very, very particular kinds of limits that you need to take with these
*  very- Right, and the limits will definitely work the way we think they work and we can do all kinds
*  of computer experiments- There's just a hard derivation. Yeah, it's just the mathematical
*  structure kind of, you know, ends up running right into computational reducibility and you end up
*  with a bunch of difficulty there. But here's the way that we're getting really confident that we
*  know completely what we're talking about, which is when people study things like black hole mergers
*  using Einstein's equations, what do they actually do? Well, they actually use
*  Mathematica a whole bunch to analyze the equations and so on, but in the end,
*  they do numerical relativity, which means they take these nice mathematical equations and they
*  break them down so that they can run them on a computer and they break them down into something
*  which is actually a discrete approximation to these equations. Then they run them on a computer,
*  they get results, then you look at the gravitational waves and you see if they match.
*  Okay, turns out that our model gives you a direct way to do numerical relativity. So in other words,
*  instead of saying you start from these continuum equations from Einstein, you break them down into
*  these discrete things, you run them on a computer, you say we're doing it the other way around. We're
*  starting from these discrete things that come from our model and we're just running big versions on
*  the computer and what we're saying is this is how things will work. So the way I'm calling this is
*  proof by compilation, so to speak. In other words, you're taking something where we've got
*  this description of a black hole system and what we're doing is we're showing that what we get by
*  just running our model agrees with what you would get by doing the computation from the
*  Einstein equations. As a small tangent or actually a very big tangent, but
*  proof by compilation is a beautiful concept. In a sense, the way of doing physics
*  with this model is by running it or compiling it. Have you thought about,
*  and these things can be very large, is there totally new possibilities of computing
*  hardware and computing software which allows you to perform this kind of compilation?
*  Well, algorithms, software, hardware. So first comment is these models seem to give one a lot
*  of intuition about distributed computing, a lot of different intuition about how to think about
*  parallel computation and that particularly comes from the quantum mechanics side of things which
*  we didn't talk about much yet, but the question of what, given our current computer hardware,
*  how can we most efficiently simulate things? That's actually partly a story of the model
*  itself because the model itself has deep parallelism in it. The ways that we are
*  simulating it, we're just starting to be able to use that deep parallelism to be able to be
*  more efficient in the way that we simulate things. But in fact, the structure of the model itself
*  allows us to think about parallel computation in different ways. And one of my realizations is that
*  it's very hard to get in your brain how you deal with parallel computation and you're always
*  worrying about if multiple things can happen on different computers at different times,
*  oh, what happens if this thing happens before that thing? And we have these race conditions where
*  something can race to get to the answer before another thing and you get all tangled up because
*  you don't know which thing is going to come in first. And usually when you do parallel computing,
*  there's a big obsession to lock things down to the point where you've had locks and mutexes and
*  God knows what else, where you've arranged it so that there can only be one sequence of things
*  that can happen. So you don't have to think about all the different kinds of things that can happen.
*  Well, in these models, physics is throwing us into forcing us to think about all these possible
*  things that can happen. But these models, together with what we know from physics,
*  is giving us new ways to think about all possible things happening,
*  about all these different things happening in parallel. And so I'm guessing-
*  They have built-in protection for some of the parallelism.
*  Well, causal invariance is the built-in protection. Causal invariance is what means
*  that even though things happen in different orders, it doesn't matter in the end.
*  As a person who struggled with concurrent programming in like Java, with all the basic
*  concepts of concurrent programming, if there could be built up a strong mathematical framework for
*  causal invariance, that's so liberating. And that could be not just liberating, but really powerful
*  for massively distributed computation. Absolutely. No, I mean, what's eventual consistency
*  in distributed databases is essentially the causal invariance idea.
*  Yeah. But have you thought about really large simulations?
*  Yeah. I mean, I'm also thinking about, look, the fact is, I've spent much of my life as a
*  language designer, right? So I can't possibly not think about what does this mean for designing
*  languages for parallel computation. In fact, another thing that's one of these, I'm always
*  embarrassed at how long it's taken me to figure stuff out. But back in the 1980s, I worked on
*  trying to make up languages for parallel computation. I thought about doing graph rewriting.
*  I thought about doing these kinds of things, but I couldn't see how to actually make the connections
*  to actually do something useful. I think now physics is kind of showing us how to make those
*  things useful. And so my guess is that in time, we'll be talking about, we do parallel programming,
*  we'll be talking about programming in a certain reference frame. Just as we think about thinking
*  about physics in a certain reference frame, it's a certain coordination of what's going on. We say,
*  we're going to program in this reference frame. Oh, let's change the reference frame to this
*  reference frame. And then our program will seem different and we'll have a different way to think
*  about it. But it's still the same program underneath. So let me ask on this topic,
*  because I put out that I'm talking to you, I got way more questions that I can deal with. But
*  what pops to mind is a question somebody asked on Reddit, I think is, please ask Dr. Wolfram,
*  what are the specs of the computer running the universe? So we're talking about specs of hardware
*  and software for simulations of a large scale thing. What about a scale that is comparative to
*  something that eventually leads to the two of us talking on a balcony?
*  Right, right, right. So actually, I did try to estimate that. And we have to go a couple more
*  stages before we can really get to that answer. Because we're talking about this thing. This is
*  what happens when you build these abstract systems and you're trying to explain the universe.
*  Quite a number of levels deep, so to speak. But the-
*  You mean conceptually or like literally? Because you're talking about small objects and there's
*  10 to the 120 something.
*  Yeah, right. It is conceptually deep. And one of the things that's happening
*  sort of structurally in this project is, there were ideas, there's another layer of ideas,
*  another layer of ideas to get to the different things that correspond to physics. They're just
*  different layers of ideas. And they are, it's actually probably, if anything, getting harder
*  to explain this project, because I'm realizing that the fraction of way through that I am so far
*  and explaining this to you is less than, it might be because we know more now,
*  every week basically we know a little bit more. And like-
*  Those are just layers on the initial fundamental-
*  Yes, but the layers are, you might be asking me, how do we get the difference between fermions and
*  bosons, the difference between particles that can be all in the same state and particles that
*  exclude each other? Okay. Last three days, we've kind of figured that out. Okay. But,
*  it's very interesting. It's very cool. And it's very-
*  And those are some kind of properties at a certain level, layer of abstraction on the
*  hydrography.
*  Yes. But the layers of abstraction are kind of, they're compounding-
*  Stacking up. So it's difficult, but-
*  But the specs nevertheless remain the same.
*  The specs underneath. So I have an estimate. So the question is, what are the units? So we've
*  got these different fundamental constants about the world. So one of them is the speed of light,
*  which is the- So the thing that's always the same in all these different ways of thinking about the
*  universe is the notion of time, because time is computation. And so there's an elementary time,
*  which is sort of the amount of time that we ascribe to elapsing in a single computational step.
*  Okay? So that's the elementary time. So then there's an elementary-
*  That's a parameter or whatever. That's a constant.
*  It's whatever we define it to be, because I mean, we don't-
*  It's all relative, right? It doesn't matter.
*  It doesn't matter what it is, because it could be slow. It's just a number which we use to convert
*  that to seconds, so to speak, because we are experiencing things and we say, this amount of
*  time has elapsed, so to speak.
*  But we're within this thing, so it doesn't-
*  It doesn't matter. But what does matter is the ratio of the spatial distance in this hypograph
*  to this moment of time. Again, that's an arbitrary thing, but we measure that in meters per second,
*  for example, and that ratio is the speed of light. So the ratio of the elementary distance
*  to the elementary time is the speed of light. Okay?
*  Perfect.
*  So there's another- There are two other levels of this. Okay? So there is a thing which we can talk
*  about, which is the maximum entanglement speed, which is a thing that happens at another level
*  in this whole story of how these things get constructed. That's a sort of maximum speed
*  in quantum- In the space of quantum states, just as the speed of light is a maximum speed
*  in physical space, this is a maximum speed in the space of quantum states. There's another level
*  which is associated with what we call rule-iel space, which is another one of these maximum
*  speeds. We'll get to this- So these are limitations on the system that are able to capture the kind
*  of physical universe which we live in, the quantum mechanical- There are inevitable features
*  of having a rule that has only a finite amount of information in the rule. So long as you have a
*  rule that only involves a bounded amount, a limited amount of- Only involving a limited
*  number of elements, limited number of relations, it is inevitable that there are these speed
*  constraints. We knew about the one for speed of light. We didn't know about the one for maximum
*  entanglement speed, which is actually something that is possibly measurable, particularly in
*  black hole systems and things like this. But anyway, this is long story short. You're asking
*  what the processing specs of the universe- Of the sort of computation of the universe.
*  There's a question of even what are the units of some of these measurements. Okay? So the units
*  I'm using are Wolfram language instructions per second, okay? Because you got to have some,
*  you know, what computation are you doing? There's got to be some kind of frame of reference.
*  Because it turns out in the end, there's sort of an arbitrariness in the language that you use to
*  describe the universe. So in those terms, I think it's like 10 to the 500 Wolfram language operations
*  per second, I think. I think it's of that order. So that's the scale of the computation. What about
*  memory? If there's an interesting thing to say about storage and memory? Well, there's a question
*  of how many sort of atoms of space might there be, you know, maybe 10 to the 400. We don't know
*  exactly how to estimate these numbers. I mean, this is based on some, I would say somewhat
*  rickety way of estimating things. You know, when they start to be able to be experiments done,
*  if we're lucky, there will be experiments that can actually nail down some of these numbers.
*  And because of computation reducibility, there's not much hope for very efficient compression,
*  like very efficient representation of this question. Good question. I mean, there's probably
*  certain things, you know, the fact that we can deduce enough. Okay, the question is, how deep
*  does the reducibility go? Right. Okay. And I keep on being surprised. It's a lot deeper than I thought.
*  Okay. And so one of the things is that there's a question of sort of how much of the whole of
*  physics do we have to be able to get in order to explain certain kinds of phenomena? Like, for
*  example, if we want to study quantum interference, do we have to know what an electron is? Turns out
*  I thought we did. Turns out we don't. I thought to know what energy is, we would have to know what
*  electrons were. We don't. So you get a lot of really powerful shortcuts. Right. There's a bunch
*  of sort of bulk information about the world. The thing that I'm excited about last few days, okay,
*  is the idea of fermions versus bosons fundamental idea that I mean, it's the reason we have matter
*  that doesn't just self destruct is because of the exclusion principle. That means that two
*  electrons can never be in the same quantum state. Is it useful for us to maybe first talk about
*  how quantum mechanics quantum mechanics into the Wolfram physics model?
*  Let's go there. So we talked about general relativity. Now, what what have you found?
*  What's the story of quantum mechanics, right within and outside of the Wolfram physics?
*  Right. So I mean, the key idea of quantum mechanics, that sort of the typical interpretation
*  is classical physics says a definite thing happens. Quantum physics says there's this whole
*  set of paths of things that might happen. And we are just observing some overall probability of
*  how those paths work. Okay, so when you think about our hyper graphs, and all these little updates
*  that are going on, there's a very remarkable thing to realize, which is, if you say, well,
*  which particular sequence of updates should you do? Say, well, it's not really defined, you can
*  do any of a whole collection of possible sequences of updates. Okay, that set of possible sequences
*  of updates defines yet another kind of graph that we call a multi way graph. And a multi way graph
*  just is a graph where at every node, there is a choice of several different possible things that
*  could happen. So for example, you go this way, go that way, those are two different edges in the
*  multi way graph. And you're building up the set of possibilities. So actually, like, for example,
*  I just made the one the multi way graph for tic tac toe. Okay, so tic tac toe, you start off with
*  some board that is everything is blank, and then somebody can put down an X somewhere, an O
*  somewhere. And then there are different possibilities. At each stage, there are
*  different possibilities. And so you build up this multi way graph of all those possibilities. Now,
*  notice that even in tic tac toe, you have the feature that there can be something where you have
*  two different things that happen, and then those branches merge, because you end up with the same
*  shape of the same configuration of the board, even though you got there in two different ways.
*  So the thing that's sort of an inevitable feature of our models is that just like quantum mechanics
*  suggests, definite things don't happen. Instead, you get this whole multi way graph of all these
*  possibilities. Okay, so then the question is, so that okay, so that's sort of a picture of what's
*  going on. Now you say, okay, well, quantum mechanics has all these features of, you know,
*  all this mathematical structure and so on. How do you get that mathematical structure? Okay,
*  couple of couple of things to say. So quantum mechanics is actually, in a sense, two different
*  theories glued together. Quantum mechanics is the theory of how quantum amplitudes work that more
*  or less give you the probabilities of things happening. And it's the theory of quantum
*  measurement, which is the theory of how we actually conclude definite things, because the
*  mathematics just gives you these quantum amplitudes, which are more or less probabilities of things
*  happening. But yet, we actually observe definite things in the world. Quantum measurement has
*  always been a bit mysterious. It's always been something where people just say, well, the
*  mathematics says this, but then you do a measurement and the philosophical arguments about what the
*  measurement is. But it's not something where there's a theory of the measurement. Somebody on
*  Reddit also asked, please ask Stephen to tell his story of this, the double split experiment.
*  Okay. Yeah, I can. Does that make sense? Oh, yeah, it makes sense. Absolutely makes sense.
*  Why is this like a good way to discuss? A little bit. Let me explain a couple of things first. So
*  the structure of quantum mechanics is mathematically quite complicated.
*  One of the features, let's see, how to describe this. Okay, so first point is there's this
*  multi-way graph of all these different paths of things that can happen in the world. And the
*  important point is that these, you can have branchings and you can have mergings. Okay,
*  so this property turns out causal invariance is the statement that the number of mergings is equal
*  to the number of branchings. So in other words, every time there's a branch, eventually there will
*  also be a merge. In other words, every time there were two possibilities for what might have happened,
*  eventually those will merge. Beautiful concept, by the way. But yeah.
*  So that idea, okay. So then, so that's one thing. And that's closely related to the
*  objectivity in quantum mechanics. The fact that we believe definite things happen,
*  it's because although there are all these different paths, in some sense, because of causal
*  invariance, they all imply the same thing. I'm cheating a little bit in saying that, but that's
*  roughly the essence of what's going on. Okay. Next thing to think about is you have this multi-way
*  graph. It has all these different possible things that are happening. Now we ask, this multi-way
*  graph is sort of evolving with time. Over time, it's branching, it's merging, it's doing all these
*  things. Okay. The question we can ask is, if we slice it at a particular time, what do we see?
*  And that slice represents, in a sense, something to do with the state of the universe at a particular
*  time. So in other words, we've got this multi-way graph of all these possibilities,
*  and then we're asking, and okay, we take this slice, this slice represents a sense,
*  okay, each of these different paths corresponds to a different quantum possibility for what's happening.
*  Right. When we take the slice, we're saying, what are the set of quantum possibilities that exist at
*  a particular time? And when you say slice, are these, you slice the graph and then there's a
*  bunch of leaves. A bunch of leaves. And those represent the state of things.
*  Right. But then, okay, so the important thing that you are quickly picking up on is that
*  what matters is kind of how these leaves are related to each other. So a good way to tell
*  how leaves are related is just to say, on the step before, did they have a common ancestor?
*  So two leaves might be, they might have just branched from one thing, or they might be far
*  away, you know, way far apart in this graph, where to get to a common ancestor, maybe you have
*  to go all the way back to the beginning of the graph, all the way back to the beginning.
*  So there's some kind of measure of distance. Right. And that, but what you get is by making
*  this slice, we call it branchial space, the space of branches. And in this branchial space,
*  you have a graph that represents the relationships between these quantum states in branchial space.
*  You have this notion of distance in branchial space. Okay, so it's connected to quantum
*  entanglement. Yes, yes. It's basically the distance in branchial space is kind of an
*  entanglement distance. So this is a very nice model. Right. It is very nice. It's very beautiful.
*  I mean, it's so clean. I mean, it's really, you know, and it tells one, okay, so anyway,
*  so then then this this branchial space has the sort of map of the entanglements between quantum
*  states. So in physical space, we have so you know, you can say, take, let's say the causal graph,
*  and we can slice that at a particular time. And then we get this map of how things are laid out
*  in physical space. When we do the same kind of thing, there's a thing called the multiway
*  causal graph, which is the analog of a causal graph for the multiway system, we slice that,
*  we get essentially the relationships between things not in physical space, but in the space
*  of quantum states. It's like which quantum state is similar to which other quantum state. Okay,
*  so now, I think next thing to say is just to mention how quantum measurement works.
*  So quantum measurement has to do with reference frames in branchial space.
*  So okay, so measurement in in physical space, it matters whether how we assign spatial position
*  and how we how we define coordinates in space and time. And that's, that's how we make measurements
*  in ordinary space. So we making a measurement based on us sitting still here, are we traveling
*  at half the speed of light and making measurements that way, these are different reference frames in
*  which we're making our measurements. And the relationship between different events and
*  different points in space and time will be different depending on what reference frame we're in.
*  Okay, so then we have this idea of quantum observation frames, which are the analog of
*  reference frames, but in branchial space. And so what happens is, what we realize is that a quantum
*  measurement is the observer is sort of arbitrarily determining this reference frame. The observer is
*  saying I'm going to understand the world by saying that space and time are coordinated this way,
*  I'm going to understand the world by saying that quantum states and time are
*  coordinated in this way. And essentially what happens is that, you know, the process of quantum
*  measurement is a process of deciding how you slice up this multiway system in these quantum
*  observation frames. So in a sense, the observer, the way the observer enters is by their choice
*  of these quantum observation frames. And what happens is that the observer, because okay,
*  this is again another stack of other concepts, but anyway, because the observer is computationally
*  bounded, there is a limit to the type of quantum observation frames that they can construct.
*  Interesting. Okay, so there's some constraints, some limit on the choice of observation frames.
*  Right. And by the way, I just want to mention that there's a, I mean, it's bizarre, but there's a
*  hierarchy of these things. So in thermodynamics, the fact that we believe entropy increases,
*  we believe things get more disordered, there's a consequence of the fact that we can't track each
*  individual molecule. If we could track every single molecule, we could run every movie in reverse,
*  so to speak, and we would not see that things are getting more disordered. But it's because
*  we are computationally bounded, we can only look at these big blobs of what all these molecules
*  collectively do, that we think that things are, that we describe it in terms of entropy increasing
*  and so on. And it's the same phenomenon, basically, also the consequence of computational irreducibility
*  that causes us to basically be forced to conclude that definite things happen in the world,
*  even though there's this quantum, you know, this set of all these different quantum processes that
*  are going on. So I mean, I'm skipping a little bit, but that's a rough picture.
*  And in the evolution of the Wolfram Physics Project, where do you feel
*  stand on some of the puzzles that are along the way? See, you're skipping along a bunch of stuff.
*  It's amazing how much these things are unraveling. I mean, you know, these things, look, it used to
*  be the case that I would agree with Dick Feynman, nobody understands quantum mechanics, including me.
*  I'm getting to the point where I think I actually understand quantum mechanics. My exercise,
*  okay, is can I explain quantum mechanics for real at the level of kind of middle school
*  type explanation? And I'm getting closer. It's getting there. I'm not quite there. I've tried
*  it a few times. And I realized that there are things where I have to start talking about
*  elaborate mathematical concepts and so on. But I think, and you've got to realize that it's not
*  self-evident that we can explain, you know, at an intuitively graspable level, something which,
*  you know, about the way the universe works, the universe wasn't built for our understanding,
*  so to speak. But I think then, okay, so another important idea is this idea of branchial space,
*  which I mentioned, this sort of space of quantum states. It is, okay, so I mentioned Einstein's
*  equations describing, you know, the effect of mass and energy on trajectories of particles,
*  on geodesics. The curvature of physical space is associated with the presence of energy,
*  according to Einstein's equations. Okay, so it turns out that rather amazingly, the same thing
*  is true in branchial space. So it turns out the presence of energy, or more accurately, Lagrangian
*  density, which is a kind of relativistic invariant version of energy, the presence of that causes
*  essentially deflection of geodesics in this branchial space. Okay, so you might say, so what?
*  Well, turns out that the sort of the best formulation we have of quantum mechanics,
*  the Feynman path integral, is a thing that describes quantum processes in terms of
*  mathematics that can be interpreted as, well, in quantum mechanics, the big thing is you get
*  these quantum amplitudes, which are complex numbers that represent, when you combine them together,
*  represent probabilities of things happening. And so the big story has been how do you derive these
*  quantum amplitudes? And people think these quantum amplitudes, they have a complex number,
*  has, you know, a real part and imaginary part. You can also think of it as a magnitude and a phase.
*  And people have sort of thought these quantum amplitudes have magnitude and phase, and you
*  compute those together. Turns out that magnitude, the magnitude and the phase come from completely
*  different places. The magnitude comes, okay, so what do you, how do you compute things in quantum
*  mechanics? Roughly, I'm telling you, I'm getting there to be able to do this at a middle school
*  level, but I'm not there yet. Roughly what happens is you're asking, does this state in
*  quantum mechanics evolve to this other state in quantum mechanics? And you can think about that
*  like a particle traveling or something traveling through physical space, but instead it's traveling
*  through branchial space. And so what's happening is does this quantum state evolve to this other
*  quantum state? It's like saying, does this object move from this place in space to this other place
*  in space? Okay, now the way that you, that these quantum amplitudes characterize kind of, to what
*  extent the thing will successfully reach some particular point in branchial space, just like
*  in physical space, you could say, oh, it had a certain velocity and it went in this direction.
*  In branchial space, there's a similar kind of concept. Is there a nice way to visualize
*  for me now mentally branchial space? It's just, you have this hypergraph, sorry, you have this
*  multi-way graph. It's this big branching thing, branching and merging thing. But I mean, like
*  moving through that space, I'm just trying to understand what that looks like. You know,
*  that space is probably exponential dimensional, which makes it again, another can of worms and
*  understanding what's going on. That space as in an ordinary space, this hypergraph, the spatial
*  hypergraph limits to something which is like a manifold, like something like three dimensional
*  space. Almost certainly the multi-way graph limits to a Hilbert space, which is something that,
*  I mean, it's just a weird exponential dimensional space. And by the way, you can ask, I mean,
*  there are much weirder things that go on. For example, one of the things I've been interested
*  in is the expansion of the universe in branchial space. So we know the universe is expanding in
*  physical space, but the universe is probably also expanding in branchial space. So that means the
*  number of quantum states of the universe is increasing with time. The diameter of the thing
*  is growing. Right. So that means that the, and by the way, this is related to whether quantum
*  computing can ever work. Why? Okay, so let me explain why. So let's talk about, okay, so first
*  of all, just to finish the thought about quantum amplitudes, the incredibly beautiful thing,
*  but I'm just very excited about this. The Feynman path integral is this formula. It says
*  that the quantum amplitude is e to the i s over h bar, where s is the thing called the action.
*  Okay, so that can be thought of as representing a deflection of the angle of this path in the
*  multi-way graph. So it's a deflection of a geodesic in the multi-way path that is caused by this thing
*  called the action, which is essentially associated with the energy. Okay. And so this is a deflection
*  of a path in branchial space that is described by this path integral, which is the thing that is the
*  mathematical essence of quantum mechanics. Turns out that deflection is the deflection of geodesics
*  in branchial space follows the exact same mathematical setup as the deflection of geodesics
*  in physical space, except the deflection of geodesics and physical space is described with
*  Einstein's equations. The deflection of geodesics in branchial space is defined by the Feynman path
*  integral, and they are the same. In other words, they are mathematically the same. So that means
*  that general relativity is a story of essentially motion in physical space. Quantum mechanics is a
*  story of essentially motion in branchial space and the underlying equation for those two things,
*  although it's presented differently because one's interested in different things in branchial space
*  than physical space, but the underlying equation is the same. So in other words, it's just, you know,
*  these two theories, which are those two sort of pillars of 20th century physics, which have seemed
*  to be off in different directions are actually facets of the exact same theory. And this, I mean,
*  that's exciting to see where that evolves and exciting that that just is there.
*  Right. I mean, to me, you know, look, having spent some part of my early life, you know, working in
*  these, in the context of these theories of 20th century physics, they just, they seem so different
*  and the fact that they're really the same is just really amazing. Actually, you mentioned double
*  slits experiment, okay? So the double slits experiment is an interference phenomenon where
*  you say there are, you know, you can have a photon or an electron, and you say there are these two
*  slits, it could have gone through either one, but there is this interference pattern where it's,
*  there's destructive interference where you might have said in classical physics, oh, well, if there
*  are two slits, then there's a better chance that it gets through one or the other of them. But in
*  quantum mechanics, there's this phenomenon of destructive interference. That means that even
*  though there are two slits, two can lead to nothing, as opposed to two leading to more than,
*  than, for example, one slit. And in what happens in this model, and we've just been understanding
*  this in the last few weeks, actually, is that the what essentially happens is that the, the double
*  slit experiment is a story of the interface between branchial space and physical space.
*  And what's essentially happening is that the destructive interference is the result of
*  the two possible paths associated with photons going through those two slits,
*  winding up at opposite ends of branchial space. And so they don't. And so that's why there's sort
*  of nothing there when you look at it, is because these two different sort of branches couldn't get
*  merged together to produce something that you can measure in physical space. Is there a lot
*  to be understood about branchial space? I guess? Yes. Mathematically speaking. Yes. It's a very
*  beautiful mathematical thing. And it's very, I mean, by the way, this whole theory is just
*  amazingly rich in terms of the mathematics that it says should exist. Okay. So for example, calculus,
*  you know, is a story of infinitesimal change in integer dimensional space, one dimensional,
*  two dimensional, three dimensional space. We need a theory of infinitesimal change in
*  fractional dimensional and dynamic dimensional space. No such theory exists. So there's tools
*  of mathematics that are needed here. Right. And this is the motivation for that, actually. Right.
*  And it's, you know, there are indications and we can do computer experiments and we can see how it's
*  going to come out, but we need to, you know, the actual mathematics doesn't exist. And in branchial
*  space, it's actually even worse. There's even more sort of layers of mathematics that are, you know,
*  we can see how it works roughly by doing computer experiments, but to really understand it, we need
*  more, more sort of mathematical sophistication. Quantum computers. Okay. So the basic idea of
*  quantum computers, the promise of quantum computers is quantum mechanics does things in parallel.
*  And so you can sort of intrinsically do computations in parallel. And somehow that can be much more
*  efficient than just doing them one after another. And, you know, I actually worked on quantum
*  computing a bit with Dick Feynman back in 1981, two, three, that kind of timeframe. And we-
*  Fascinating image. You and Feynman were quantum computers.
*  Well, we tried to work, the big thing we tried to do was invent a randomness chip
*  that would generate randomness at a high speed using quantum mechanics. And the discovery that
*  that wasn't really possible was part of the story of, we never really wrote anything about it. I
*  think maybe he wrote some stuff, but we didn't write stuff about what we figured out about sort
*  of the fact that it really seemed like the measurement process in quantum mechanics was
*  a serious damper on what was possible to do in sort of, you know, the possible advantages of
*  quantum mechanics for computing. But anyway, so the sort of the promise of quantum computing is,
*  let's say you're trying to factor an integer. Well, you can instead of, you know, when you
*  factor an integer, you might say, well, does this factor work? Does this factor work? Does this factor
*  work? In ordinary computing, it seems like we pretty much just have to try all these different
*  factors, you know, kind of one after another. But in quantum mechanics, you might have the idea,
*  oh, you can just sort of have the physics, try all of them in parallel. Okay. And the, you know,
*  and there's this algorithm, Shor's algorithm, which allows you, according to the formalism
*  of quantum mechanics, to do everything in parallel and to do it much faster than you can on a
*  classical computer. Okay. The only little footnote is you have to figure out what the answer is. You
*  have to measure the result. So the quantum mechanics internally has figured out all these
*  different branches, but then you have to pull all these branches together to say, and the classical
*  answer is this. Okay. The standard theory of quantum mechanics does not tell you how to do that.
*  It tells you how the branching works, but doesn't tell you the process of corralling all these things
*  together. And that process, which intuitively you can see is going to be kind of tricky,
*  but our model actually does tell you how that process of pulling things together works.
*  And the answer seems to be, we're not absolutely sure. We've only got to two times three so far,
*  which is kind of in this factorization in quantum computers. But what seems to be the case is that
*  the advantage you get from the parallelization from quantum mechanics is lost from the amount
*  that you have to spend pulling together all those parallel threads to get to a classical answer at
*  the end. Now, that phenomenon is not unrelated to various decoherence phenomena that are seen in
*  practical quantum computers and so on. I should say, as a very practical point, it's like,
*  should people stop bothering to do quantum computing research? No, because what they're
*  really doing is they're trying to use physics to get to a new level of what's possible in computing.
*  And that's a completely valid activity. Whether you can really put, whether you can say, oh,
*  you can solve an NP-complete problem, you can reduce exponential time to polynomial time,
*  you know, we're not sure. And I'm suspecting the answer is no. But that's not relevant to
*  the practical speed ups you can get by using different kinds of technologies, different kinds
*  of physics to do basic computing. So you're saying, I mean, some of the models you're playing with,
*  the indication is that to get all the sheep back together and, you know, to corral everything
*  together to get the actual solution to the algorithm is... You lose all the... You lose
*  all the... By the way, I mean, so again, this question, do we actually know what we're talking
*  about, about quantum computing and so on? So again, we're doing proof by compilation. So we
*  have a quantum computing framework in Wolfram language, which is, you know, a standard quantum
*  computing framework that represents things in terms of the standard, you know, formalism of
*  quantum mechanics. And we have a compiler that simply compiles the representation of quantum gates
*  into multi-way systems. So, and in fact, the message that I got was from somebody who's
*  working on the project who has managed to compile one of the sort of core formalism based on category
*  theory, core quantum formalism into multi-way systems. So this... When you say multi-way system,
*  these multi-way graphs? Yes. So you're compiling... Yeah, okay. That's awesome. And then you can do
*  all kinds of experiments on that multi-way graph. Right. But the point is that what we're saying is
*  the thing, we've got this representation of, let's say, Shaw's algorithm in terms of standard quantum
*  gates, and it's just a pure matter of sort of computation to just say that is equivalent.
*  We will get the same result as running this multi-way system. Can you do complexity analysis
*  on that multi-way system? Well, that's what we've been trying to do. Yes. We're getting there. We
*  haven't done that yet. I mean, there's a pretty good indication of how that's going to work out.
*  And we've done, as I say, our computer experiments, we've unimpressively gotten to about two times
*  three in terms of factorization, which is kind of about how far people have got with physical
*  quantum computers as well. But yes, we will be able to... We definitely will be able to do
*  complexity analysis and we will be able to know. So the one remaining hope for quantum computing,
*  really, really working at this formal level of quantum brand, exponential stuff being done in
*  polynomial time and so on, the one hope, which is very bizarre, is that you can kind of piggyback
*  on the expansion of branchial space. So here's how that might work. So you think energy conservation,
*  standard thing in high school physics, energy is conserved, right? But now you imagine you think
*  about energy in the context of cosmology, in the context of the whole universe. It's a much more
*  complicated story. The expansion of the universe kind of violates energy conservation. And so,
*  for example, if you imagine you've got two galaxies, they're receding from each other very quickly.
*  They've got two big central black holes. You connect a spring between these two central black
*  holes. Not easy to do in practice, but let's imagine you could do it. Now that spring is being
*  pulled apart. It's getting more potential energy in the spring as a result of the expansion of the
*  universe. So in a sense, you are piggybacking on the expansion that exists in the universe
*  and the sort of violation of energy conservation that's associated with that cosmological expansion
*  to essentially get energy. You're essentially building a perpetual motion machine by using
*  the expansion of the universe. And that is a physical version of that. It is conceivable
*  that the same thing could be done in branch-shield space to essentially mine the expansion of the
*  universe in branch-shield space as a way to get sort of quantum computing for free, so to speak,
*  just from the expansion of the universe in branch-shield space. Now, the physical space
*  version is kind of absurd and involves springs between black holes and so on.
*  It's conceivable that the branch-shield space version is not as absurd and that it's actually
*  something you can reach with physical things you can build in labs and so on. We don't know yet.
*  Okay, so like you were saying, the branch-shield space might be expanding and there might be
*  something that could be exploited. Right. In the same kind of way that you can exploit
*  that expansion of the universe in principle in physical space.
*  You just have like a glimmer of hope. Right. I think that the real answer is going to be
*  that for practical purposes, the official brand that says you can do exponential things
*  a polynomial time is probably not going to work. For people curious to kind of learn more. So this
*  is more like, it's not middle school. We're going to go to elementary school for a second.
*  Maybe middle school. Let's go to middle school. So if I were to try to maybe write a pamphlet
*  of like Wolfram Physics Project for Dummies, aka for me, or maybe make a video on the basics,
*  but not just the basics of the physics project, but the basics plus the most beautiful central ideas.
*  How would you go about doing that? Could you help me out a little bit?
*  Yeah. I mean, as a really practical matter, we have this kind of visual summary picture that
*  we made, which I think is a pretty good, when I've tried to explain this to people and it's a pretty
*  good place to start is you got this rule, you apply the rule, you're building up this big
*  hypergraph, you've got all these possibilities, you're kind of thinking about that in terms of
*  quantum mechanics. I mean, that's a decent place to start.
*  So basically, the things we've talked about, which is space represented as a hypergraph,
*  transformation of that space is kind of time.
*  Yes. And then-
*  Structure of that space, the curvature of that space has gravity. That can be explained without
*  going anywhere near quantum mechanics. I would say that's actually easier to explain than special
*  relativity. Oh, so going into general, so going to curvature.
*  Yeah. I mean, special relativity, I think it's a little bit elaborate to explain.
*  Honestly, you only care about it if you know about special relativity, if you know how special
*  relativity is ordinarily derived and so on. So general relativity is easier.
*  Is easier, yes. And then what about quantum? What's the easiest way to reveal-
*  I think the basic point is just this fact that there are all these different branches,
*  that there's this kind of map of how the branches work. And that, I mean, I think actually the recent
*  things that we have about the double-slit experiment are pretty good because you can actually
*  see this, you can see how the double-slit phenomenon arises from just features of these graphs.
*  Now, having said that, there is a little bit of slight of hand there because the true story of
*  the way that double-slit thing works depends on the coordination of branchial space that,
*  for example, in our internal team, there is still a vigorous battle going on about how that works.
*  And what's becoming clear is, I mean, what's becoming clear is that it's mathematically
*  really quite interesting. I mean, that is that there's a, you know, it involves essentially
*  putting space filling curves. You'll basically have a thing which is naturally two-dimensional
*  and you're sort of mapping it into one dimension with a space filling curve. And it's like, why is
*  it this space filling curve and another space filling curve? And that becomes a story about
*  Riemann surfaces and things. And it's quite elaborate. But there's a more, a little bit
*  slight of hand way of doing it where it's, you know, it's surprisingly direct.
*  So a question that might be difficult to answer, but for several levels of people,
*  could you give me advice on how we can learn more specifically? There is people that are completely
*  outside and just curious and are captivated by the beauty of hypergraphs actually. So people
*  that just want to explore, play around with this. A second level is people from, say, people like me
*  who somehow got a PhD in computer science, but are not physicists. And but fundamentally,
*  the work you're doing is of computational nature. So it feels very accessible. So what are, what can
*  a person like that do to learn enough physics or not to be able to, one, explore the beauty of it,
*  and two, the final level of contribute something of a level of even publishable, you know, like
*  strong, interesting ideas at all those layers, complete beginner, ICS person, and the CS person
*  that wants to publish. Right. I mean, I think that, you know, I've written a bunch of stuff.
*  President called Jonathan Gorard, who's been a key person working on this project,
*  has also written a bunch of stuff. And some other people started writing things too.
*  He's a physicist.
*  Physicist. Well, he's, I would say a mathematical physicist. He's pretty mathematically sophisticated.
*  He regularly out-mathematicizes me. Yeah. This strong, yeah, strong mathematical physicist. Yeah,
*  I looked at some of the papers. Right. But so, I mean, you know, I wrote this kind of original
*  announcement blog post about this project, which people seem to have found. I've been really happy,
*  actually, that people who, you know, people seem to have grok-ed key points from that.
*  Much deeper key points. People seem to have grok-ed than I thought they would grok.
*  And that's a kind of a long blog post that explains some of the things we talked about,
*  like the hypograph and the basic rules. And I don't, does it, I forget, it doesn't have any
*  quantum mechanics. Oh, yeah, yeah. It does. It does. But we know a little bit more since that
*  blog post that probably clarifies, but that blog post does a pretty decent job. And, you know,
*  talking about things like, again, somebody didn't mention the fact that the uncertainty principle
*  is a consequence of curvature in branchial space. How much physics should a person know to be able
*  to understand the beauty of this framework and to contribute something novel? Okay. So I think that
*  those are different questions. So, I mean, I think that the why does this work? Why does this make
*  any sense? To really know that, you have to know a fair amount of physics. Okay. And for example,
*  have a decent understanding- When you say why does this work, you're referring to the connection
*  between this model and- General relativity, for example. You have to understand something
*  about general relativity. There's also a side of this where just as the pure mathematical framework
*  is fascinating, if you throw the physics out, right? Then it's quite accessible to, I mean,
*  you know, I wrote this sort of long technical introduction to the project, which seems to have
*  been very accessible to people who are, you know, who understand computation and formal abstract
*  ideas, but are not specialists in physics or other kinds of things. I mean, the thing with the
*  physics part of it is, you know, there's both a way of thinking and a, literally a mathematical
*  formalism. I mean, it's like, you know, to know that we get the Einstein equations, to know we
*  get the energy and momentum tensor, you kind of have to know what the energy and momentum tensor is,
*  and that's physics. I mean, that's kind of graduate level physics, basically. And so that, you know,
*  making that final connection requires some depth of physics knowledge. I mean, that's the unfortunate
*  thing, the difference between machine learning and physics in the 21st century. Is it really out of
*  reach of a year or two worth of study? No, you could get it in a year or two, but you can't get
*  it in a month. Right. I mean- But it doesn't require necessarily like 15 years. No, it does not. And in
*  fact, a lot of what has happened with this project makes a lot of this stuff much more accessible.
*  There are things where it has been quite difficult to explain what's going on, and it requires
*  much more, you know, having the concreteness of being able to do simulations, knowing that this
*  thing that you might have thought was just an analogy is really actually what's going on, makes
*  one feel much more secure about just sort of saying, this is how this works. And I think it will be,
*  you know, the, I'm hoping the textbooks of the future, the physics textbooks of the future,
*  there will be a certain compression. There will be things that used to be very much more elaborate,
*  because for example, even doing continuous mathematics versus this discrete mathematics,
*  you know, to know how things work in continuous mathematics, you have to be talking about stuff
*  and waving your hands about things. Whereas with the discrete version, it's just like, here is a
*  picture. This is how it works. And there's no, oh, did we get the limit right? Did this, you know,
*  this thing that is of, you know, zero, you know, measure zero object, you know, interact with this
*  thing in the right way. You don't have to have that whole discussion. It's just like, here's a
*  picture. You know, this is what it does. And, you know, you can then it takes more effort to say,
*  what does it do in the limit when the picture gets very big? But you can do experiments to build up
*  an intuition, actually. Yes, right. And you can get sort of core intuition for what's going on.
*  Now, in terms of contributing to this, the, you know, I would say that the study of the
*  computational universe and how all these programs work in the computational universe,
*  there's just an unbelievable amount to do there. And it is very close to the surface. That is,
*  you know, high school kids, you can do experiments. It's not, you know, and you can discover things.
*  I mean, you know, we, you can discover stuff about, I don't know, like this thing about expansion of
*  branch-scale space. That's an absolutely accessible thing to look at. Now, you know, the main issue
*  with doing these things is not, there isn't a lot of technical depth difficulty there.
*  The actual doing of the experiments, you know, all the code is all on our website to do all these
*  things. The real thing is sort of the judgment of what's the right experiment to do. How do you
*  interpret what you see? That's the part that, you know, people will do amazing things with.
*  And that's the part that, but it isn't like you have to have done 10 years of study to get to the
*  point where you can do the experiments. You don't see a cool thing. You can do experiments day one,
*  basically. That's the amazing thing about, and you've actually put the tools out there.
*  Yeah. It's beautiful. It's mysterious. There's still, I would say, maybe you can correct me.
*  It feels like there's a huge number of log hanging fruit on the mathematical side, at least not the,
*  not the physics side, perhaps. No, there's, look on the, on the, okay, on the physics side,
*  we are, we're definitely in harvesting mode. You know, of which, which fruit, the low hanging ones
*  or the low hanging. All right. I mean, basically here's the thing. There's a certain list of,
*  you know, here are the effects in quantum mechanics here are the effects in general
*  relativity. It's just like industrial harvesting. It's like, can we get this one, this one, this one,
*  this one, this one. And the thing that's really, you know, interesting and satisfying. And it's
*  like, you know, is one climbing the right mountain? Does one have the right model?
*  The thing that's just amazing is, you know, we keep on like, are we going to get this one?
*  How hard is this one? It's like, oh, you know, it looks really hard. It looks really hard. Oh,
*  actually we can get it. And, and you're, you're continually surprised. I mean, it seems like I've
*  been following your progress. It's kind of exciting. All the in harvesting mode, all the things
*  you're picking up. Right, right. No, I mean, it's, it's the thing that is, I keep on thinking it's
*  going to be more difficult than it is. Now that's a, you know, that's a, who knows what, I mean,
*  the one thing, so the, the, the, the thing that's been a, was a big thing that I think we're, we're
*  pretty close to, I mean, I can give you a little bit of the roadmap. It's sort of interesting to
*  see it's like, what are particles? What are things like electrons? How do they really work?
*  Are you close to get like, what, what's a, are you close to trying to understand like the atom,
*  the electrons, neutrons, protons? Okay. So this is, this is the stack. So the first thing we want
*  understand is the quantization of spin. So particles, they, they kind of spin, they have
*  a certain angular momentum, that angular momentum, even though the masses of particles are all over
*  the place, you know, the electron has a massive 0.511 MAV, the, you know, the proton is 938 MAV,
*  et cetera, et cetera, et cetera. They're all kind of random numbers. The, the spins of all these
*  particles that are either integers or half integers. And that's a fact that was discovered
*  in the 1920s, I guess. The, I think that we are close to understanding why spin is quantized.
*  And that's a, and it appears to be a quite elaborate mathematical story about homotopy
*  groups in twister space and all kinds of things. But bottom line is that seems within reach.
*  And that's, that's a big deal because that's a very core feature of understanding how particles
*  work in quantum mechanics. Another core feature is this difference between particles that obey
*  the exclusion principle and sort of stay apart that leads to the stability of matter and things
*  like that. And particles that love to get together and be in the same state, things like photons
*  that, and that's what leads to phenomena like lasers, where you can get sort of coherently
*  everything in the same state. That difference is the particles of integer spin or bosons like to
*  get together in the same state, the particles of half integer spin of fermions like electrons that
*  they tend to stay apart. And so the question is, can we, can we get that in our models?
*  And oh, just the last few days, I think we made, I mean, I think the story of, I mean, it's, it's,
*  it's one of these things where we're really close. It's, it's, it's connected fermions and bosons.
*  Yeah. So this was what happens is what seems to happen. Okay. It's, you know, subject to revision
*  next, even next few days. But what seems to be the case is that bosons are associated with
*  essentially merging in multi-way graphs and fermions are associated with branching in multi-way graphs.
*  And that essentially the exclusion principle is the fact that in branchial space, things have a
*  certain extent in branchial space that in which things are being sort of forced apart in branchial
*  space. Whereas the case of bosons, they get, they, they come together in branchial space.
*  And the real question is, can we explain the relationship between that and these things
*  called spinners, which are the representation of half integer spin particles that have this
*  weird feature that usually when you go around 360 degree rotation, you get back to where you
*  started from. But for a spinner, you don't get back to where you started from. It takes 720 degrees
*  of rotation to get back to where you started from. And we are just, it feels like we are,
*  we're just incredibly close to actually having that understanding how that works.
*  And it turns out it looks like my current speculation is that it's as simple as the
*  directed hypergraphs versus undirected hypergraphs.
*  Oh, interesting.
*  The relationship between spinners and vectors. So which is just.
*  Ah, it's interesting. Yeah, that'll be interesting if these are all these kind of
*  nice properties of this multi-way graphs of branching and rejoining.
*  Spinners have been very mysterious. And if that's what they turn out to be,
*  there's going to be an easy explanation. Yeah, it's directed versus undirected.
*  It's just, and that's why there's only two different cases.
*  Why are spinners important in quantum mechanics? Can you just give a.
*  Yeah, so spinners are important because they are, they're the representation of electrons,
*  which have half an inch of spin. They are the wave functions of electrons are spinners,
*  just like the wave functions of photons are vectors, the wave functions of electrons are
*  spinners. And they have this property that when you rotate by 360 degrees, they come back to minus
*  one of themselves and take 720 degrees to get back to the original value. And they are a consequence
*  of, and we usually think of rotation in space as being, you know, when you have this notion of
*  rotational invariance and rotational invariance, as we ordinarily experience it, doesn't have the
*  feature. You know, if you go through 360 degrees, you go back to where you started from, but that's
*  not true for electrons. And so that's, that's why understanding how that works is important.
*  Yeah. I've been playing with Mobius strip quite a bit lately, just for fun.
*  Yes. Yes. It has some funk. It has the same kind of funky property.
*  Yes. Right. Exactly. You can have this, the so-called belt trick, which is this way of
*  taking an extended object and you can see properties like spinners with that kind of
*  extended object that- Yeah. It would be very cool if it somehow connects the directive
*  versus undirected. I think that's what it's going to be. I think it's going to be as simple as that,
*  but we'll see. I mean, this is the thing that, you know, this is the big sort of bizarre surprise is
*  that, you know, because, you know, I learned physics as probably, let's say, a fifth generation,
*  in the sense that, you know, if you go back to the 1920s and so on, there were the people who
*  were originating quantum mechanics and so on. Maybe it's a little less than that. Maybe I was
*  like a third generation or something. I don't know, but the people from whom I learned physics
*  were the people who were, you know, who had been students of the students of the people who
*  originated the current understanding of physics. And we're now at, you know, probably the seventh
*  generation of physicists or something from the early days of 20th century physics. And, you know,
*  whenever a field gets that many generations deep, it seems the foundations seem quite inaccessible.
*  And they seem, you know, it seems like you can't possibly understand that we've gone through,
*  you know, seven academic generations. And that's been, you know, that's been this thing that's been
*  difficult to understand for that long. It just can't be that simple. But in a sense, maybe that
*  journey takes you to a simple explanation that was there all along. That's the whole. Right. I mean,
*  the thing for me personally, the thing that's been quite interesting is, you know, I didn't expect
*  this project to work in this way. And I, you know, but I had this sort of weird piece of personal
*  history that I used to be a physicist. And I used to do all this stuff. And I know, you know, the
*  standard canon of physics, I knew it very well. And, you know, but then I've been working on this
*  kind of computational paradigm for basically 40 years. And the fact that, you know, I'm sort of
*  now coming back to, to, you know, trying to apply that in physics, it kind of felt like that journey
*  was necessary. Was this, when did you first try to play with a hypergraph? So I was happy. Yeah. So
*  what I had was, okay, so this is again, you know, one, one always feels dumb after the fact. It's,
*  it's, it's obvious after the fact. But, but so back in the early 1990s, I realized that using graphs
*  as a sort of underlying thing underneath space and time was going to be a useful thing to do.
*  I figured out about multi-way systems. I figured out the things about general relativity, I figured
*  out by the end of the 1990s. But I always felt there was a certain inelegance because I was using
*  these graphs. And there were certain constraints on these graphs that seemed like they were,
*  they were kind of awkward. It was kind of like, you can pick, it's like you couldn't pick any rule.
*  It was like, pick any number, but the number has to be prime. It was kind of like you couldn't,
*  it was kind of an awkward special constraint. I had these trivalent graphs, graphs with just three
*  connections from every node. Okay. So, but, but I discovered a bunch of stuff with that,
*  but I thought it was kind of an elegant. And, you know, the other piece of sort of personal history
*  is obviously I spent my life as a language, computational language designer. And so the
*  story of computational language design is a story of how do you take all these random ideas in the
*  world and kind of grind them down into something that is computationally as simple as possible.
*  And so, you know, I've been very interested in kind of simple computational frameworks for
*  representing things and have, you know, ridiculous amounts of experience in, in trying to do that.
*  And actually all of those trajectories of your life kind of came together. So you make it sound
*  like you could have come up with everything you're working on now decades ago, but in reality.
*  Look, two things slowed me down. I mean, one thing that slowed me down was I couldn't figure
*  out how to make it elegant. And, and that turns out hypergraphs were the key to that. And that I
*  figured out about less than two years ago now. And the other, I mean, I think, so that was,
*  that was sort of a key thing. Well, okay. So the real embarrassment of this project,
*  okay, is that the final structure that we have that is the foundation for this project
*  is basically a, a kind of an idealized version of formalized version of the exact same structure
*  that I've used to build computational languages for more than 40 years. But it took me,
*  but I didn't realize that. And, and, you know, and there yet may be other, so we're focused on
*  physics now, but I mean, that's what the new kind of science is about. Same kind of stuff.
*  And this, in terms of mathematically, um, the beauty of it, so there could be entire other
*  kind of objects that are useful for, like, we're not talking about, you know, machine learning,
*  for example, maybe there's other variants of the hypergraph that are very useful for
*  we'll see whether the multi-way graph or machine learning system is interesting.
*  Okay. Let's leave it at that. That's conversation number three.
*  That's, that's, that's, uh, we're not going to go there right now, but.
*  One of the things you've mentioned is, um, the space of all possible rules that we kind of
*  discussed a little bit, uh, that, you know, there could be, I guess the set of possible rules is
*  infinite. Right. Well, so here's, here's the big sort of one of the conundrums that, that I'm
*  kind of trying to deal with is let's say we think we found the rule for the universe
*  and we say, here it is, you know, write it down. It's a little tiny thing.
*  And then we say, gosh, that's really weird. Why did we get that one?
*  Right. And then we're in this whole situation because let's say it's fairly simple. How did we
*  come up the winners getting one of the simple possible universe rules? Why didn't we get what
*  some incredibly complicated rule? Why do we get one of the simpler ones? And, and that's a thing
*  which, you know, in the history of science, you know, the whole sort of story of Copernicus
*  and so on was, you know, we used to think the earth was the center of the universe,
*  but now we find out it's not. And we're actually just in some, you know, random
*  corner of some random galaxy out in this big universe. There's nothing special about us.
*  So if we get, you know, universe number 317 out of all the infinite number of possibilities,
*  how do we get something that small and simple? Right. So I was very confused by this. And it's
*  like, what are we going to say about this? How are we going to explain this? And I thought it
*  was might be one of these things where you just, you know, you can get it to the threshold and then
*  you find out it's rule number such and such, and you just have no idea why it's like that.
*  Yeah. Okay. So then I realized it's actually more bizarre than that. Okay. So we talked about
*  multi-way graphs. We talked about this idea that you take these underlying transformation rules on
*  these hyper graphs and you apply them wherever the rule can apply. You apply it. And that makes
*  this whole multi-way graph of possibilities. Okay. So let's go a little bit weirder. Let's say that
*  at every place, not only do you apply a particular rule and all possible ways it can apply,
*  but you apply all possible rules in all possible ways they can apply.
*  As you say, that's just crazy. That's way too complicated. You're never going to be able to
*  conclude anything. Okay. However, turns out that there's some kind of an variance. Yeah.
*  Yeah. So what happens is, right. So this thing that you get, there's this kind of rule,
*  little multi-way graph, this multi-way graph that is a branching of rules, as well as a branching
*  of possible applications of rules. This thing has causal invariance. It's an inevitable feature
*  that it shows causal invariance. And that means that you can take different reference frames,
*  different ways of slicing this thing, and they will all in some sense be equivalents. If you
*  make the right translation, they will be equivalents. So, okay. So the basic point here is-
*  If that's true, that would be beautiful.
*  It is true and it is beautiful.
*  So it's not just an intuition. There is some-
*  No, no, no. There's real mathematics behind this. Okay. So here's what it comes out.
*  Yeah. That's amazing.
*  Right. So by the way, I mean, the mathematics that's connected to is the mathematics of higher
*  category theory and groupoids and things like this, which I've always been afraid of, but now
*  I'm finally wrapping my arms around it. But it also relates to computational complexity theory.
*  It's also deeply related to the P versus NP problem and other things like this. Again,
*  it seems completely bizarre that these things are connected, but here's why it's connected.
*  This space of all possible- Okay. So a Turing machine, very simple model of computation.
*  You just got this tape where you write down ones and zeros or something on the tape,
*  and you have this rule that says you change the number, you move the head on the tape, etc.
*  You have a definite rule for doing that. A deterministic Turing machine just does that
*  deterministically. Given the configuration of the tape, it will always do the same thing.
*  A non-deterministic Turing machine can have different choices that it makes at every step.
*  And so, you know, this stuff, you probably teach this stuff.
*  So a non-deterministic Turing machine has this set of branching possibilities,
*  which is in fact one of these multi-way graphs. And in fact, if you say, imagine the extremely
*  non-deterministic Turing machine, the Turing machine that can just do, that takes any possible
*  rule at each step, that is this rule-y-o multi-way graph. The set of possible histories of that
*  extreme non-deterministic Turing machine is a rule-y-o multi-way graph. What term are you using?
*  Rule-y-o?
*  Rule-y-o. It's a weird word. Yeah, it's a weird word.
*  Multi-way graph. Okay. So this, so that...
*  I'm trying to think of the space of rules. So these are basic transformations.
*  So in a Turing machine, it's like it says move left, move, you know, if it's a one,
*  if it's a black square under the head, move left and right a green square. That's a rule.
*  That's a very basic rule, but I'm trying to see the rules on the hypergraphs, how rich of the
*  programs can they be? Or do they all ultimately just map into something simple? Yeah, they're all,
*  I mean, hypergraphs, that's another layer of complexity on this whole thing. You can think
*  about these transformations of hypergraphs, but Turing machines are a little bit simpler.
*  You should think of it Turing machines. Okay.
*  Right. They're a little bit simpler. So if you look at these extreme non-deterministic
*  Turing machines, you're mapping out all the possible non-deterministic paths that the Turing
*  machine can follow. And if you ask the question, can you reach... Okay. So a deterministic Turing
*  machine follows a single path. The non-deterministic Turing machine fills out this whole sort of ball
*  of possibilities. And so then the P versus MP problem ends up being questions about, and we
*  haven't completely figured out all the details of this, but it basically has to do with questions
*  about the growth of that ball relative to what happens with individual paths and so on. So
*  essentially there's a geometrization of the P versus MP problem that comes out of this.
*  That's a sideshow. Okay. The main event here is the statement that you can look at this
*  multi-way graph where the branches correspond not just to different applications of a single rule,
*  but to applications of different rules. Okay. And that then that when you say,
*  I'm going to be an observer embedded in that system, and I'm going to try and make sense of
*  what's going on in the system. And to do that, I essentially am picking a reference frame.
*  And that turns out to be... Well, okay. So the way this comes out essentially is the reference
*  frame you pick is the rule that you infer is what's going on in the universe. Even though
*  all possible rules are being run, although all those possible rules are in a sense giving the
*  same answer because of causal invariance. But what you see could be completely different.
*  If you pick different reference frames, you essentially have a different description language
*  for describing the universe. Okay. So what does this really mean in practice? So imagine there's
*  us. We think about the universe in terms of space and time, and we have various kinds of
*  description models and so on. Now let's imagine the friendly aliens, for example. Right? How do
*  they describe their universe? Well, our description of the universe probably is affected by the fact
*  that we are about the size we are, a meter-ish tall, so to speak. We have brain processing speeds,
*  we're about the speeds we have. We're not the size of planets, for example, where the speed of light
*  really would matter. In our everyday life, the speed of light doesn't really matter.
*  The fact that the speed of light is finite is irrelevant. It could as well be infinite.
*  We wouldn't make any difference. It affects the ping times on the internet. That's about the level
*  of how we notice the speed of light. In our everyday existence, we don't really notice it.
*  So we have a way of describing the universe that's based on our sensory, our senses,
*  our... these days, also on the mathematics we've constructed, and so on. But the realization is
*  that's not the only way to do it. There will be completely utterly incoherent descriptions
*  of the universe, which correspond to different reference frames in this sort of rule-iel space.
*  In the rule-iel space. That's fascinating. So we have some kind of reference frame in
*  this rule-iel space. Right. And from that... That's why we are attributing this rule to the universe.
*  So in other words, when we say, why is it this rule and not another, the answer is just, you know,
*  shine the light back on us, so to speak. It's because of the reference frame that we've picked
*  in our way of understanding what's happening in this sort of space of all possible rules and so on.
*  But also in the space from this reference frame, because of the rule-iel, the invariance,
*  that simple... that the rule on which the universe... with which you can run the universe
*  might as well be simple. Yes. Yes. But okay, so here's another point. So this is again,
*  these are a little bit mind-twisting in some ways, but the... Okay, another thing that's sort of we
*  know from computation is this idea of computation universality. The fact that, given that we have a
*  fact that, given that we have a program that runs on one kind of computer, we can as well,
*  you know, we can convert it to run on any other kind of computer. We can emulate one kind of
*  computer with another. So that might lead you to say, well, you think you have the rule for the
*  universe, but you might as well be running it on a Turing machine, because we know we can emulate
*  any computational rule on any kind of machine. And that's essentially the same thing that's being
*  said here. That is that what we're doing is we're saying these different interpretations of physics
*  correspond to essentially running physics on different underlying, you know, thinking about
*  the physics as running in different... with different underlying rules, as if different underlying
*  computers were running them. And... but because of computation universality, or more accurately,
*  because of this principle of computational equivalence thing of mine, there's... they are...
*  these things are ultimately equivalent. So the only thing that is the ultimate fact about the
*  universe, the ultimate fact that doesn't depend on any of these, you know, we don't have to talk
*  about specific rules, etc., etc., etc. The ultimate fact is the universe is computational,
*  and it is the things that happen in the universe are the kinds of computations that the principle
*  of computational equivalence says should happen. Now, that might sound like you're not really saying
*  anything there, but you are, because you can... you could in principle have a hypercomputer
*  that things that take an ordinary computer an infinite time to do, the hypercomputer can just
*  say, oh, I know the answer. It's this immediately. What this is saying is the universe is not a
*  hypercomputer. It's not simpler than an ordinary Turing machine type computer. It's exactly like
*  an ordinary Turing machine type computer. And so that's the... that's in the end, the sort of net,
*  net conclusion is that's the thing that is the sort of the hard immovable fact about the universe.
*  That's sort of the fundamental principle of the universe is that it is computational and not
*  hypercomputational and not sort of infra computational. It is this level of computational
*  ability. And it's... it kind of has that sort of the core fact. But now, you know, this idea that
*  you can have these different kind of rule-y reference frames, these different description
*  languages for the universe, it makes me... I used to think, okay, imagine the aliens, imagine the
*  extraterrestrial intelligence thing, you know, at least they experienced the same physics.
*  Right. And now I've realized it isn't true. They could have a different rule frame. That's
*  fascinating. They can end up with a description of the universe that is utterly, utterly incoherent
*  with ours. And that's also interesting in terms of how we think about, well, intelligence, the nature
*  of intelligence and so on. You know, I'm fond of the quote, you know, the weather has a mind of its
*  own, because these are, you know, these are sort of computationally that that system is computationally
*  equivalent to the system that is our brains and so on. And what's different is we don't have a way
*  to understand, you know, what the weather is trying to do, so to speak, we have a story about
*  what's happening in our brains, we don't have a sort of connection to what's happening there.
*  So we actually... it's funny, last time we talked, maybe over a year ago, we talked about how
*  it was more based on your work with Arrival. We talked about how would we communicate with
*  alien intelligences. Can you maybe comment on how we might, how the Wolfram Physics Project changed
*  your view, how we might be able to communicate with alien intelligence? Like if they showed up,
*  is it possible that because of our comprehension of the physics of the world might be completely
*  different? We would just not be able to communicate at all. Here's the thing, you know,
*  intelligence is everywhere. The fact this idea that there's this notion of, oh, there's going
*  to be this amazing extraterrestrial intelligence and it's going to be this unique thing, it's just
*  not true. It's the same thing, you know, I think people will realize this about the time when
*  people decide that artificial intelligences are kind of just natural things that are like human
*  intelligences. They'll realize that extraterrestrial intelligences or intelligences
*  associated with physical systems and so on, it's all the same kind of thing.
*  It's ultimately computation.
*  It's all the same, it's all just computation. And the issue is, can you, are you sort of inside it?
*  Are you thinking about it? Do you have sort of a story you're telling yourself about it?
*  And you know, the weather could have a story, it's telling itself about what it's doing.
*  We just, it's utterly incoherent with the stories that we tell ourselves based on how our brains
*  work. I mean, ultimately it must be a question whether we can align. Exactly. Align with the
*  kind of intelligence. Right, right, right. So there's a systematic way of doing it.
*  Right. So the question is in the space of all possible intelligences, what's the,
*  how do you think about the distance between description languages for one intelligence
*  versus another? And needless to say, I have thought about this. And, you know, I don't have
*  a great answer yet, but I think that's a thing where there will be things that can be said.
*  And there'll be things that where you can sort of start to characterize, you know, what is the
*  translation distance between this, you know, version of the universe or this, you know, kind
*  of set of computational rules and this other one. In fact, okay, so this is a, you know, there's
*  this idea of algorithmic information theory. There's this question of sort of what is the,
*  when you have some something, what is the sort of shortest description you can make of it,
*  where that description could be saying run this program to get the thing. Right. So I'm pretty
*  sure that that the that there will be a physicalization of the idea of algorithmic information
*  and that, okay, this is again, a little bit bizarre, but so I mentioned that there's the
*  speed of light, maximum speed of information transmission in physical space. There's a
*  maximum speed of information transmission in branchial space, which is a maximum entanglement
*  speed. There's a maximum speed of information transmission in rule space, which is has to do
*  with a maximum speed of translation between different description languages. And again,
*  I'm not fully wrapped my brain around this one. Yeah, that one just blows my mind to think about
*  that. But that starts getting closer to the, yeah, the, it's kind of the intelligent, right. It's a,
*  and it's also a physicalization of, of algorithmic information. And I think there's probably a
*  connection between, I mean, there's probably a connection between the notion of energy
*  and some of these things, which again, I, I, you know, hadn't seen all this coming. I've always
*  been a little bit resistant to the idea of connecting physical energy to things in, in,
*  in computation theory, but I think that's probably coming. And that's what essentially at the core,
*  what the, the physics project is that you're connecting information theory with physics.
*  Yeah, it's computation and computation. Yeah. Our physical universe. Yeah, right. I mean,
*  the fact that our physical universe is, is right, that we can think of it as a computation and that
*  we can have discussions like, you know, the theory of the physical universe is the same kind
*  of a theory as the P versus MP problem and so on is, is really, you know, I think that's really
*  interesting. And, and the fact that's, well, okay, so this, this kind of brings me to one,
*  one more thing that I have to, in terms of this sort of unification of different ideas,
*  which is meta mathematics. Yeah, let's talk about that. You mentioned that earlier. What the heck is
*  meta mathematics and, okay, so here's, here's what his, okay. So what is mathematics? Mathematics,
*  sort of at a lowest level, one thinks of mathematics as you have certain axioms,
*  you say, you know, you say things like X plus Y is the same as Y plus X. That's an axiom
*  about addition. And then you say, we've got these axioms and we, and from these axioms,
*  we derive all these theorems that fill up the literature of mathematics. The activity of
*  mathematicians is to derive all these theorems. Actually, the axioms of mathematics are very
*  small. You can fit, you know, when I did my new kind of science book, I fit all of the standard
*  axioms of mathematics on basically a page and a half. It's not much stuff. It's like a very
*  simple rule from which all of mathematics arises. The way it works, though, is a little different
*  from the way things work in sort of a computation because in mathematics, what you're interested in
*  is a proof. And the proof says from here, you can use, from this expression, for example,
*  you can use these axioms to get to this other expression. So that proves these two things are
*  equal. Okay. So we can, we can begin to see how this is going to work. What's going to happen is
*  there are paths in metamathematical space. So what happens is each, two different ways to look at
*  it, you can just look at it as mathematical expressions, or you can look at it as mathematical
*  statements, postulates or something. But either way, you think of these things and they are
*  connected by these axioms. So in other words, you have some fact, you, or you have some expression,
*  you apply this axiom, you get some other expression. And in general, given some expression,
*  there may be many possible different expressions you can get. You basically build up a multi-way
*  graph. And a proof is a path through the multi-way graph that goes from one thing to another thing.
*  The path tells you how did you get from one thing to the other thing. It's the,
*  it's the story of how you got from this to that. The theorem is the thing at one end is equal to
*  the thing at the other end. The proof is the path you go down to get from one thing to the other.
*  You mentioned that Gödel's incompleteness theorem is not natural,
*  it fits naturally there. How hard is it? Yeah. So what happens there is that the
*  Gödel's theorem is basically saying that there are paths of infinite length. That is that there's
*  no upper bound. If you know these two things, you say, I'm trying to get from here to here.
*  How long do I have to go? You say, well, I've looked at all the paths of length 10. Somebody says,
*  that's not good enough. That path might be of length a billion. And there's no upper bound on
*  how long that path is. And that's what leads to the incompleteness theorem. So I mean, the thing
*  that is kind of an emerging idea is you can start asking, what's the analog of Einstein's equations
*  in metamathematical space? What's the analog of a black hole in metamathematical space?
*  What's the hope of this whole, yeah, it's fascinating to model all the mathematics in this way.
*  So here's what it is. This is mathematics in bulk. So human mathematicians have made a few
*  million theorems. They published a few million theorems. But imagine the infinite future of
*  mathematics. Apply something to mathematics that mathematics likes to apply to other things. Take
*  a limit. What is the limit of the infinite future of mathematics? What does it look like? What is
*  the continuum limit of mathematics? What is the, as you just fill in more and more and more theorems,
*  what does it look like? What does it do? How does, what kinds of conclusions can you make?
*  So for example, one thing I've just been doing is taking Euclid. So Euclid, very impressive.
*  He had 10 axioms. He derived 465 theorems. Okay. His book, you know, that was the sort of defining
*  book of mathematics for 2000 years. So you can actually map out, and I actually did this
*  20 years ago, but I've done it more seriously now. You can map out the theorem dependency
*  of those 465 theorems. So from the axioms, you grow this graph. It's actually a multi-way graph
*  of how all these theorems get proved from other theorems. And so you can ask questions about,
*  you know, well, you can ask things like, what's the hardest theorem in Euclid? The answer is the
*  hardest theorem is that there are five platonic solids. That turns out to be the hardest theorem
*  in Euclid. That's actually his last theorem in all his books. That's the final...
*  What's the hardness? The distance you have to travel?
*  Yeah. It's 33 steps from the... The longest path in the graph is 33 steps. So that's the...
*  There's a 33-step path you have to follow to go from the axioms, according to Euclid's proofs,
*  to the statement there are five platonic solids. So, okay. So then the question is,
*  what does it mean if you have this map... Okay. So in a sense, this meta-mathematical space
*  is the infrastructural space of all possible theorems that you could prove in mathematics.
*  That's the geometry of meta-mathematics. There's also the geography of mathematics. That is,
*  where did people choose to live in space? And that's what, for example, exploring the sort
*  of empirical meta-mathematics that Euclid is doing. See, you could put each individual human
*  mathematician, you can embed them into that space. I mean, they kind of live...
*  They represent a path. The little path.
*  Things they do. Maybe a set of paths.
*  Right. So like a set of axioms that are chosen...
*  Right. So for example, here's an example of a thing that I realized. So one of the surprising
*  things about... Well, there are two surprising facts about math. One is that it's hard,
*  and the other is that it's doable. Okay? So first question is, why is math hard? You know,
*  you've got these axioms, they're very small. Why can't you just solve every problem in math easily?
*  Yeah, it's just logic. Right. Yeah. Well, logic happens to be
*  a particular special case that does have certain simplicity to it. But general mathematics,
*  even arithmetic, already doesn't have the simplicity that logic has.
*  So why is it hard? Because of computational irreducibility.
*  Right. Because what happens is to know what's true, and this is this whole story about the
*  path you have to follow and how long is the path, and Gödel's theorem is the statement that the
*  path is not a bounded length, but the fact that the path is not always compressible to something
*  tiny is the story of computational irreducibility. So that's why math is hard. Now, the next question
*  is, why is math doable? Because it might be the case that most things you care about don't have
*  finite length paths. Most things you care about might be things where you get lost in the sea
*  of computational irreducibility and worse undecidability, that is, there's just no finite
*  length path that gets you there. You know, why is mathematics doable? You know, Gödel proved his
*  incompleteness theorem in 1931. Most working mathematicians don't really care about it.
*  They just go ahead and do mathematics, even though it could be that the questions they're
*  asking are undecidable. It could have been that Fermat's last theorem is undecidable. It turned
*  out it had a proof. It's a long, complicated proof. The twin prime conjecture might be
*  undecidable. The Riemann hypothesis might be undecidable. These things might be the axioms
*  of mathematics might not be strong enough to reach those statements. It might be the case that
*  depending on what axioms you choose, you can either say that's true or that's not true.
*  . . . And by the way, Fermat's last theorem, it could be a shorter path.
*  . . . Absolutely. Yeah. So the notion of geodesics in
*  metamathematical space is the notion of shortest proofs in metamathematical space.
*  And that's a, you know, human mathematicians do not find shortest paths, nor do automated
*  theorem provers. But the fact, and by the way, the, I mean, this stuff is so bizarrely connected.
*  I mean, if you're into automated theorem proving, there are these so-called critical
*  pair lemmas in automated theorem proving. Those are precisely the branch pairs in our,
*  that in multi-way graphs. Let me just finish on the why mathematics is doable.
*  . . . Oh, yes, the second part. So we know why it's hard. Why is it doable?
*  Right. Why do we not just get lost in undecidability all the time?
*  Yeah. . . . So, and here's
*  another fact is in doing computer experiments and doing experimental mathematics, you do get lost in
*  that way. When you just say, I'm picking a random integer equation, how do I, does it have a solution
*  or not? And you just pick it at random without any human sort of path getting there. Often,
*  it's really, really hard. It's really hard to answer those questions. We just pick them
*  at random from the space of possibilities. But what's, what I think is happening is,
*  and that's a case where you just fell off into this ocean of sort of irreducibility and so on.
*  What's happening is human mathematics is a story of building a path. You started off,
*  you're always building out on this path where you are proving things. You've got this proof
*  trajectory and you're basically, the human mathematics is the sort of the exploration of
*  the world along this proof trajectory, so to speak. You're not just parachuting in
*  from anywhere. You're following Lewis and Clark or whatever. You're actually going,
*  you're doing the path. And the fact that you are constrained to go along that path is the reason
*  you don't end up with luck. Every so often, you'll see a little piece of undecidability and you'll
*  avoid that part of the path. But that's basically the story of why human mathematics has seemed to
*  be doable. It's a story of exploring these paths that are by their nature, they have been constructed
*  to be paths that can be followed, and so you can follow them further.
*  Now, why is this relevant to anything? So, okay, so here's my belief. The fact that human mathematics
*  works that way is, I think there's some sort of connections between the way that observers work
*  in physics and the way that the axiom systems of mathematics are set up to make mathematics
*  be doable in that kind of way. And so, in other words, in particular, I think there is an analog
*  of causal invariance, which I think is, and this is again, it's sort of the upper reaches of
*  mathematics and stuff that, it's a thing, there's this thing called homotopy type theory, which is
*  an abstract, it's come out of category theory, and it's sort of an abstraction of mathematics.
*  Mathematics itself is an abstraction, but it's an abstraction of the abstraction of mathematics.
*  And there is the thing called the univalence axiom, which is a sort of a key axiom in that
*  set of ideas. And I'm pretty sure the univalence axiom is equivalent to causal invariance.
*  What was the term used again? Univalence.
*  Is that something for somebody like me accessible?
*  Um, there's a statement of it that's fairly accessible. I mean, the statement of it is,
*  um, uh, basically it says things which are equivalent can be considered to be identical.
*  In which space?
*  Yeah, it's in higher category.
*  In category theory.
*  Okay, so it's a, but I mean, the thing, just to give a sketch of how that works,
*  so category theory is an attempt to idealize, it's an attempt to sort of have a formal theory
*  of mathematics that is at a sort of higher level than mathematics. It's where, well,
*  you just think about these mathematical objects and these categories of objects and these,
*  these morphisms, these connections between categories. Okay, so it turns out the morphisms
*  and categories, at least weak categories, are very much like the paths in our hypergraphs and things.
*  And it turns out, again, this is, this is where it all gets, gets crazy. I mean, it's, it's the fact
*  that these things are connected is just bizarre. So category theory, uh, the, our causal graphs
*  are like second order category theory. And it turns out you can take the limit of infinite
*  order category theory. So just give roughly the idea. This is a, this is a roughly explainable
*  idea. So a mathematical proof will be a path that says you can get from this thing to this other
*  thing. And here's the path that you get from this thing to this other thing. But in general, there
*  may be many paths, many proofs that get you many different paths that all successfully go from this
*  thing to this other thing. Okay. Now you can define a higher order proof, which is a proof of the
*  equivalence of those proofs. Okay. So you're saying there's a path between those proofs, essentially.
*  Yes. The path between the paths. Yeah. Okay. And so you do that. That's the sort of second
*  order thing that path between the paths is essentially related to our causal graphs.
*  Then, wow. Okay.
*  The infinite limits that infinite limit turns out to be our rule, the multi-way system.
*  Yeah. The rule, the rule, the multi-way system. That's a fascinating thing. I'm both in the
*  physics world and as you're saying, that's, that's so, I'm not sure I've loaded it in completely,
*  but I'm not sure I have either. And it may be one of these things where, where, you know, in another,
*  another five years or something, it's like, it was obvious, but I didn't see it. No, but the thing,
*  which is sort of interesting to me is that there's sort of an upper reach of, of mathematics,
*  of the abstraction of mathematics. This thing, there's this mathematician called Grothendieck,
*  who's generally viewed as being sort of one of the most abstract, sort of creator of the most
*  abstract mathematics of 1970s-ish timeframe. And one of the things that he constructed with this
*  thing, he called the infinity groupoid. And he has the sort of hypothesis about the inevitable
*  appearance of geometry from essentially logic in the structure of this thing. Well, it turns out
*  this rule, the multi-way system is the infinity groupoid. So it's a, it's this limiting object.
*  And this is an, this is an instance of that limiting object. So what to me is, I mean, again,
*  I, I've been always afraid of this kind of mathematics because it seemed incomprehensibly
*  abstract to me. But what's, what's, what I'm sort of excited about with this is that, that we've
*  sort of concretified the way that you can reach this kind of mathematics, which makes it, well,
*  both seem more relevant and also the fact that that, you know, I don't yet know exactly what
*  mileage we're going to get from using the sort of the apparatus that's been built in those areas of
*  mathematics to analyze what we're doing. But the thing that's-
*  So both ways. So using the mathematics to understand what you're doing and
*  what you're doing computationally to understand that mathematics.
*  Right. So, so for example, the, the understanding of metamathematical space,
*  one of the reasons I really want to do that is because I want to understand quantum mechanics
*  better. And, and that, what you see, you know, we live that kind of the multi-way graph of
*  mathematics because we actually know this is a theorem we've heard of. This is another one
*  we've heard of. We can actually say these are actual things in the world that we relate to,
*  which we can't really do as readily for the physics case. And so it's kind of a way to help
*  my intuition. It's also, you know, there are bizarre things like the, what's the analog of
*  Einstein's equations in metamathematical space? What's the analog of a black hole? You know,
*  it turns out it looks like, not completely sure yet, but there's this notion of non-constructive
*  proofs in mathematics. And I think those relate to, well, actually the, the, they're, they relate to
*  things and related to event horizons. So the fact that you can take ideas from physics,
*  like event horizon and map them into the same kind of space, metamathematical, it's, it's really,
*  do you think there'll be, do you think you might stumble upon some breakthrough ideas in theorem
*  proving like for, from the other direction? Yeah, yeah, yeah. No, I mean, what's really nice is
*  that we are using, so this, this absolutely directly maps to theorem proving. So pods and
*  multi-way graphs, that's what a theorem prover is trying to do. But I also mean like, like
*  automated theorem. Yeah, yeah, yeah. That, that's what, right. So the finding of pods, the finding
*  of shortest pods or finding a pods at all is what automated theorem provers do. And actually what,
*  what we've been doing. So we've, you know, we've actually been using automated theorem proving both
*  in the physics project to prove things and using that as a way to understand multi-way graphs. And
*  because what an automated theorem prover is doing is it's trying to find a path through a multi-way
*  graph. And its critical pair lemmas are precisely little stubs of branch pairs going off into
*  branchial space. And that's, I mean, it's really weird. And you know, we have these visualizations
*  in welcome language of our, of, of proof graphs from our automated theorem proving system.
*  And they look reminiscent of. Well, it's just bizarre because we made these up a few years ago
*  and they have these little triangle things and they are, they are, we, we didn't quite get it
*  right. We didn't quite get the analogy perfectly right, but it's very close. You know, just to say
*  in terms of the, how these things are connected. So there's another bizarre connection that I have
*  to mention because, because, which is, which again, we don't fully know, but it's a connection to
*  something else. You might not have thought was in the slightest bit connected, which is distributed
*  blockchain like things. Now you might figure out that that's, you, you would figure out that that's
*  connected because, because it's a story of distributed computing and the issue, you know,
*  with a blockchain, you're saying there's going to be this one ledger that, that globally says this
*  is what happened in the world, but that's a bad deal. If you've got all these different transactions
*  that are happening and you know, this transaction in country, a doesn't have to be reconciled with
*  the transaction in country B, at least not for a while. And that story is just like what happens
*  when I causal graphs that whole reconciliation thing is just like what happens with light cones
*  and that's where the cause of the nurse comes into play. I mean that that's, you know,
*  most of your conversations are about physics, but it's kind of funny that this probably and possibly
*  might have even bigger impact and revolutionary ideas and totally other disciplines. Right.
*  Yeah. Right. So the question is why is that happening? Right. And the reason it's happening
*  I've thought about this obviously, because I like to think about these meta questions of,
*  you know, what's happening is this model that we have is an incredibly minimal model. Yeah. And
*  once you have an incredibly minimal model and this happened with cellular automata as well,
*  cellular automata are an incredibly minimal model. And so it's inevitable that it gets you,
*  it's sort of an upstream thing that gets used in lots of different places. And it's like, you know,
*  the fact that it gets used, you know, cellular automata is sort of a minimal model of, let's say,
*  road traffic flow or something. And they're also a minimal model of something in, you know,
*  chemistry. And they're also a minimal model of something in epidemiology. Right. It's because
*  they're such a simple model that they can apply to all these different things. Similarly, this
*  model that we have of the physics project is another cellular automata or a minimal model of
*  basically of parallel computation where you've defined space and time. These models are minimal
*  models where you have not defined space and time. And they have been very hard to understand in the
*  past. But the, I think the, perhaps the most important breakthrough there is the realization
*  that these are models of physics and therefore that you can use everything that's been developed
*  in physics to get intuition about how things like that work. And that's why you can potentially use
*  ideas from physics to get intuition about how to do parallel computing. And because the underlying
*  model is the same. Yeah. And, but, but we have all of this achievement in physics. I mean, you know,
*  you might say, oh, you've come up with the fundamental theory of physics that throws out
*  what people have done in physics before. Well, it doesn't, but also the real power is to use what's
*  been done before in physics to apply it in these other places. Yes. And this kind of brings up,
*  I know you probably don't particularly love commenting on the work of others, but let me,
*  let me bring up a couple of personalities just cause it's fun. People are curious about it.
*  So there's a Sabine Hassanfelder. I don't know if you're familiar with her. She, she wrote this book
*  that I need to read, but it based, I forget what the title is, but it's beauty leads us astray in
*  physics is a subtitle, something like that, which so much about what we're talking about now, like
*  this simplification is a, to us humans seems to be beautiful. Like there's a certain intuition
*  with physicists, with people that a simple theory, like this reducibility pockets of reducibility is
*  the ultimate goal. And I think what she tries to argue is, uh, no, we just need to come up with
*  theories that are just really good at predicting physical phenomena. It's okay to have a bunch of,
*  uh, disparate theories as opposed to trying to chase this beautiful
*  theory of everything is the ultimate beautiful theory. Uh, a simple one.
*  You know, it's always, it's always your response to that.
*  Well, so what you're quoting is, I don't know the Sabine Hassanfelder's,
*  you know, exactly what she said, but I mean, I'm quoting the title of her book.
*  Okay. Let me, let me, let me respond to what you were describing. It may or may not have
*  anything to do with what, uh, you know, what Sabine Hassanfelder says or thinks.
*  Sorry, Sabine.
*  Right. Sorry for misquoting.
*  But I mean, the question is, you know, does, is beauty a guide to whether something is correct?
*  Which is kind of also the story of Occam's razor. You know, if you've got a bunch of different
*  explanations of things, you know, is the thing that is the simplest explanation likely to be
*  the correct explanation. And there are situations where that's true and there are situations where
*  it isn't true. Sometimes in human systems, it is true because people have kind of, you know,
*  in evolutionary systems, sometimes it's true because it's sort of been kicked to the point
*  where it's minimized. Um, but, uh, you know, in physics does Occam's razor work, you know,
*  is there a simple quotes, beautiful explanation for things, or is it a big mess? Um, you know,
*  we don't intrinsically know, you know, I think that the, I wouldn't, before I worked on the
*  project in recent times, I would have said, we do not know how complicated the rule for the
*  universe will be. And I would have said, you know, the one thing we know, which is a fundamental
*  fact about science, that's the thing that makes science possible is that there is order in the
*  universe. I mean, you know, early theologians would have used that as an argument for the
*  existence of God, because it's like, why is that order in the universe? Why doesn't every single
*  particle in the universe just do its own thing? Um, you know, something must be making there be
*  order in the universe. We, you know, in, in the sort of early theology point of view, that's,
*  you know, the role of God is to do that, so to speak in our, uh, you know, we might say it's
*  the role of a formal theory to do that. And then the question is, but how simple should that theory
*  be? And should that theory be one that, that, you know, where I think the point is if it's simple,
*  it's almost inevitably somewhat beautiful in the sense that because all the stuff that we see has
*  to fit into this little tiny theory and the way it does that has to be, you know, it depends on
*  your notion of beauty. But I mean, for me, the, the sort of the surprising connectivity of it
*  is at least in my aesthetic, that's something that, uh, you know, responds to my aesthetic.
*  But the question is, uh, I mean, you, you, you, you're a fascinating person in the sense that
*  you're at once talking about computational, the fundamental computational reducibility of the
*  universe. And at, and the other hand, trying to come up with a theory of everything, which
*  simply describes the, the, the simple origins of that computational reducibility. I mean,
*  both of those things are kind of, it's paralyzing to think that we can't make any sense of the
*  universe in the general case, but it's hopeful to think like one, we can think of a rule and,
*  uh, that generates this whole complexity. And two, we can find pockets of, uh, reducibility that are
*  powerful for everyday life to do different kinds of predictions. I suppose to be able,
*  wants to find focus on the finding of small pockets of reducibility versus the, uh,
*  theory of everything. You know, it's a funny thing because, because, you know, a bunch of people
*  have started working on this, this, you know, physics project, people who are, you know,
*  physicists basically. Um, and it is really a fascinating sociological phenomenon because
*  what, you know, when I was working on this before in the 1990s, you know, wrote it up,
*  put it, it's a hundred pages of this 1200 page book that I wrote, New Kind of Science is, you
*  know, a hundred pages of that is about physics, right? I, I saw it in that, at that time,
*  not as a pinnacle achievement, but rather as a use case, so to speak. I mean, my main point was
*  this new kind of science and it's like, you can apply it to biology, you can apply it to,
*  you know, other kinds of physics, you can apply it to fundamental physics. It's just,
*  it's just an application, so to speak. It's not the core thing. But, um, but then, you know,
*  one of the things was interesting with that, with that book was, you know, book comes out,
*  lots of people think it's pretty interesting and lots of people start using what it has in different
*  kinds of fields. The one field where there was sort of a, a heavy pitch forking was from my friends,
*  the fundamental physics people, which was, it's like, no, this can't possibly be right. And,
*  you know, it's like, you know, if what you're doing is right, it'll overturn 50 years of what
*  we've been doing. And it's like, no, it won't, was what I was saying. And it's like, um, but, uh,
*  you know, for a while when I started, you know, I was going to go on back in 2002, well, 2004,
*  actually, I was going to go on working on this project and I actually stopped partly because
*  it's like, why am I, you know, this is like, I've been in business a long time, right? I'm,
*  I'm building a product for a target market that doesn't want the product. And it's like,
*  why work? Yeah. Why, why work against the swim against the current or whatever.
*  But you see what's happened, which is sort of interesting is, is that a couple of things
*  happened and it was, it was like, uh, you know, it was like, I, I, I don't want to do this project
*  because I can do so many other things, which I'm really interested in where, you know, people say,
*  great, thanks for those tools, thanks for those ideas, et cetera. Whereas, you know, if you're
*  dealing with kind of a, a, uh, you know, a, a sort of a structure where people are saying, no, no,
*  we don't want this new stuff. We don't need any new stuff. We're really fine with what we're
*  doing. There's like literally like, I don't know, millions of people who are thankful for Wolfram
*  Alpha. Bunch of people wrote to me how thankful they are. They are different crowd than the
*  theoretical physics community, perhaps. Yeah. Well, right. But you know, the theoretical
*  physics community pretty much uniformly uses, uh, well from language and Mathematica, right?
*  And so it's, it's kind of like, like, um, you know, and that, that's, but the thing is,
*  what happens, you know, this is what happens. Mature fields do not, you know, it's like,
*  we're doing what we're doing. We have the methods that we have and where we're just fine here.
*  Now what's happened in the last 18 years or so, I think there's a couple of things have happened.
*  First of all, the, the hope that, you know, string theory or whatever would, would deliver
*  the fundamental theory of physics, that hope has disappeared. That the, another thing that's
*  happened is the, the sort of the interest in computation around physics has been greatly
*  enhanced by the whole quantum information, quantum computing story. People, you know,
*  the idea that there might be something sort of computational, uh, related to physics has somehow,
*  somehow grown. And I think, you know, it's, it's sort of interesting. I mean, right now, if we say,
*  you know, it's like, if you're like, who else is trying to come up with a fundamental theory of
*  physics? It's like there aren't professional, no professional physicists, no professional physicists.
*  What are your, uh, I mean, you've talked with him, but just as a matter of personalities,
*  cause it's a beautiful story. What are your thoughts about Eric Weinstein's work?
*  You know, I think his, his, um, I mean, he did a PhD thesis in mathematical physics at Harvard.
*  Mathematical physicists.
*  And, and, you know, it's, uh, it, it seems like it's kind of, uh, you know, it's, it's in that
*  framework and it's kind of like, I'm not sure how much further it's got than his PhD thesis,
*  which was 20 years ago or something. And I think that, you know, the, the, you know,
*  it's a fairly specific piece of mathematical physics that's quite nice. And, um,
*  what trajectory do you hope it takes? I mean,
*  well, I think in his particular case, I mean, from what I understand, which is not everything
*  at all, but you know, I think I know the rough tradition, at least, of who's operating in is
*  sort of theory of gauge theories, gauge theories, local gauge invariance and so on. Okay. We are
*  very close to understanding how local gauge invariance works in our models and it's very
*  beautiful and it's very, um, and you know, does some of the mathematical structure that he's
*  enthusiastic about fit quite possibly. Yes. So there might be a possibility of trying to
*  understand how those things fit, how gauge theory fits. The question is, you know, so there are a
*  couple of things one might try to get in the world. So for example, it's like, can we get three
*  dimensions of space? We haven't managed to get that yet gauge theory, the standard model of
*  particle physics says that it's SU three cross SU two cross you one, those are the designations of
*  these, um, Lee groups. Um, it doesn't, but, but anyway, so those are, those are sort of
*  representations of symmetries of the theory. And, um, so, you know, it is conceivable that it is
*  generically true. Okay. So all those are subgroups of a group called E eight, which is a weird,
*  exceptionally group. Okay. It is conceivable. I don't know whether that's the case that that
*  will be generic in these models, that it will be generic, that the gauge invariance of the model
*  has this property, just as things like general relativity, which corresponds to think of, uh,
*  general covariance, which is another gauge like invariance. It could conceivably be the case
*  that the kind of local gauge invariance that we see in particle physics is somehow generic. And,
*  and that would be a, you know, the thing that's, that's really cool, I think, you know,
*  sociologically, although this hasn't really hit yet is that all of these different things,
*  all these different things people have been working on in these, in some cases, quite
*  abstruse areas of mathematical physics, an awful lot of them seem to tie into what we're doing.
*  And, you know, it might not be that way. Yeah, absolutely. That's a beautiful thing. I mean,
*  but the reason I said the reason Eric Weinstein is important is to the point that you mentioned
*  before, which is, it's strange that the theory of everything is not at the core of, uh, the passion,
*  the dream, the focus, the funding of the physics community. It's too hard. It's too hard. And people
*  gave up. I mean, basically what happened is ancient Greece, people thought we're nearly there. You
*  know, the world is made of platonic solids. It's, you know, water is a tetrahedron or something.
*  We're almost there. Okay. Long period of time where people were like, no, we don't know how it works.
*  You know, time of Newton, uh, you know, we're almost there. Everything is gravitation,
*  you know, time of Faraday and Maxwell. We're almost there. Everything is fields. Everything is the ether,
*  you know, then the whole time we're making big progress though. Oh yes, absolutely. But the
*  fundamental theory of physics is almost a footnote because it's like, it's the machine code. It's like,
*  we're operating in the high level languages. Um, you know, that's what we really care about.
*  That's what's relevant for our everyday physics. You talked about different centuries and the 21st
*  century will be, uh, everything's computation. Yes. If that takes us all the way, we don't know,
*  but it might take us pretty far. Yes, right. That's right. And I, but I think the point is that
*  it's like, you know, if you're doing biology, you might say, how can you not be really interested
*  in the origin of life and the definition of life? Well, it's irrelevant. You know, you're studying
*  the properties of some virus. It doesn't matter, you know, where, you know, you're operating at
*  some much higher level. And it's the same, what's happening with physics is I was sort of surprised
*  actually, I was sort of mapping out this history of, of people's efforts to understand the
*  fundamental theory of physics. And it's remarkable how little has been done on this question. And
*  it's, you know, because, you know, there've been times when there's been bursts of enthusiasm,
*  we're almost there and then it decays and people just say, oh, it's too hard, but it's not relevant
*  anyway. And I think that the, um, the thing that, um, you know, so, so the question of, of, you know,
*  one question is, why does anybody, why should anybody care? Right? Why should anybody care
*  what the fundamental theory of physics is? I think it's intellectually interesting, but what will be
*  the sort of, what will be the impact of this? What, I mean, this is the key question. What do you think
*  will happen if we figure out the fundamental theory of physics outside of the intellectual
*  curiosity of us? Okay. So here's what, here's my best guess. Okay. So if you look at the history
*  of science, I think a very interesting analogy is Copernicus. Okay. So what did Copernicus do?
*  There'd been this Ptolemaic system for working out the motion of planets. It did pretty well.
*  It used epicycles, et cetera, et cetera, et cetera. It had all this computational
*  ways of working out what planets will be. When we work out where planets are today,
*  we're basically using epicycles, but Copernicus had this different way of formulating things
*  in which he said, you know, and the earth is going around the sun. And that had a consequence. The
*  consequence was you can use this mathematical theory to conclude something, which is absolutely
*  not what we can tell from common sense. Right? So it's like, trust the mathematics, trust the science.
*  Okay. Now fast forward 400 years and, you know, and now we're in this pandemic and it's kind of
*  like, everybody thinks the science will figure out everything. It's like, from the science,
*  we can just figure out what to do. We can figure out everything. That was before Copernicus. Nobody
*  would have thought if the science says something that doesn't agree with our everyday experience,
*  we just have to, you know, compute the science and then figure out what to do. People say that's
*  completely crazy. And so your sense is once we figure out the framework of computation that can
*  basically do any understand the fabric of reality, we'll be able to derive totally counterintuitive
*  things. No, the point I think is the following that right now, you know, I talk about computational
*  irreducibility. People, you know, I was very proud that I managed to get the term computational
*  irreducibility into the congressional record last year. That's right. By the way, that's a whole
*  another topic we're talking about. Different topic. Different day. Different topic. But in any case,
*  you know, but so computational irreducibility is one of these sort of concepts that I think is
*  important in understanding lots of things in the world. But the question is, it's only important
*  if you believe the world is fundamentally computational. Right? And but if you, if you
*  know the fundamental theory of physics and it's fundamentally computational, then you've rooted
*  the whole thing. That is, you know, the world is computational. And while you can discuss whether,
*  you know, it's not the case that people would say, well, you have this whole computational
*  irreducibility, all these features of computation. We don't care about those because after all, the
*  world isn't computational, you might say. But if you know, you know, base, base, base thing,
*  physics is computational, then you know, that that stuff is, you know, that that's kind of
*  the grounding for that stuff, just as in a sense Copernicus was the grounding for the idea that
*  you could figure out something with math and science that was not what you would intuitively
*  think from your senses. So now we've got to this point where, for example, we say, you know, once
*  we have the idea that computation is the foundational thing that explains our whole universe,
*  then we have to say, well, what does it mean for other things? Like, it means there's computational
*  irreducibility. That means science is limited in certain ways. That means this, that means that.
*  But the fact that we have that grounding means that, you know, and I think, for example, for
*  Copernicus, for instance, the implications of his work on the set of mathematics of astronomy
*  were cool, but they involved a very small number of people. The implications of his work for sort
*  of the philosophy of how you think about things were vast and involved, you know, everybody more
*  or less. But do you think so that's actually the way scientists and people see the world around us.
*  So it has a huge impact in that sense. Do you think it might have an impact more directly to
*  engineering derivations from physics, like propulsion systems, our ability to colonize
*  the world? Like, for example, okay, this is like sci-fi, but if you understand
*  the computational nature, say, of the different forces of physics, you know, there's a notion
*  of being able to, you know, warp gravity, things like this. Yeah, can we make warp drive? Warp drive.
*  Yeah. So like, would we be able to, will it, will, you know, will like Elon Musk start paying
*  attention like it's awfully costly to launch these rockets? Do you think we'll be able to,
*  yeah, create warp drive and- Right. You know, I set myself some homework. I agreed to give a talk
*  at some NASA workshop in a few weeks about faster than light travel. So I haven't figured it out yet,
*  but no, but- You got two weeks. Yeah, right. But do you think that kind of understanding of fundamental
*  theory of physics can lead to those engineering breakthroughs? Okay. I think it's far away, but
*  I'm not certain. I mean, you know, this is the thing that I set myself an exercise when gravity
*  waves, gravitational waves were discovered, right? I set myself the exercise of what would black hole
*  technology look like? In other words, right now, you know, black holes are far away there, you know,
*  how on earth can we do things with them? But just imagine that we could get, you know, pet black
*  holes right in our backyard, you know, what kind of technology could we build with them? I got a
*  certain distance, not that far, but I think in, you know, so there are ideas, you know, I have this,
*  one of the weirder ideas is things I'm calling space tunnels, which are higher dimensional pieces
*  of space time, where basically you can, you know, in our three dimensional space, there might be a
*  five dimensional, you know, region, which actually will appear as a white hole at one end and a black
*  hole at the other end, you know, who knows whether they exist. And then the questions, another one,
*  okay, this is another crazy one is the thing that I'm calling a vacuum cleaner. Okay. So, so, so I
*  mentioned that, you know, there's all this activity in the universe, which is maintaining the structure
*  of space. And that leads to a certain energy density effectively in space. And so the question,
*  in fact, dark energy is a story of essentially negative mass produced by the absence of energy
*  you thought would be there, so to speak. And we don't know exactly how it works in our model or
*  the physical universe. But this notion of a vacuum cleaner is a thing where, you know, you have all
*  these things that are maintaining the structure of space, but what if you could clean out some of
*  that stuff that's maintaining the structure of space and make a simpler vacuum somewhere? Yeah.
*  You know, what would that do? A totally different kind of vacuum. Right. And that would lead to
*  negative energy density, which would need to, so gravity is usually a purely attractive force,
*  but negative mass would lead to repulsive gravity and lead to all kinds of weird things. Now, can
*  it be done in our universe? You know, my immediate thought is no. But, you know, the fact is that...
*  Okay, so... Once you understand the fact, because you're saying like at this level of abstraction,
*  can we reach to the lower levels and mess with it? Yes. Once you understand the levels, I think...
*  I know. And I'm, you know, I have to say that this reminds me of people telling one years ago that,
*  you know, you'll never transmit data over a copper wire at more than a thousand, you know,
*  a thousand board or something. Right? And this is why did that not happen? You know, why do we have
*  these much, much faster data transmission? Because we've understood many more of the details of what's
*  actually going on. And it's the same exact story here. And it's the same, you know, I think that
*  this, as I say, I think one of the features of sort of one of the things about our time that will
*  seem incredibly naive in the future is the belief that, you know, things like heat is just random
*  motion of molecules. That it's just throw up your hands. It's just random. We can't say anything
*  about it. That will seem naive. Yeah. At the heat death of the universe, those particles would be
*  laughing at us humans thinking... Yes, right. That life is not beautiful.
*  Humans used to think they're special with their little brains.
*  Well, right. But also, and they used to think that this would just be random and interesting.
*  But that's, but so, so this question about whether you can, you know, mess with the underlying
*  structure and how you find a way to mess with the underlying structure, that's a, you know,
*  I have to say, you know, my immediate thing is, boy, that seems really hard. But then, and, you
*  know, possibly computational irreducibility will bite you. But then there's always some path of
*  computational reducibility. And that path of computational reducibility is the engineering
*  invention that has to be made. Exactly. Those little pockets can have huge engineering impact.
*  Right. And I think that that's right. And I mean, we live in, you know, we make use of so many of
*  those pockets. And the fact is, you know, I, you know, this is, yes, it's a, you know, it's one of
*  these things where, where, you know, I am a person who likes to figure out ideas and so on. And
*  there's sort of tests of my level of imagination, so to speak. And so a couple of places where
*  there's sort of serious humility in terms of my level of imagination. One is this thing about
*  different reference frames for understanding the universe, where like, imagine the physics of the
*  aliens, what will it be like? And I'm like, that's really hard. I don't know, you know, and, and, and,
*  I mean, once you have the framework in place, you can at least reason about the things you don't know.
*  Maybe can't know, or like, it's too hard for, for you to know. But then the, the mathematics can,
*  that's exactly it, allow you to reach beyond where you can reason.
*  Right. So I'm, you know, I'm, I'm, I'm trying to not have, you know, if you think back to Alan
*  Turing, for example, and, you know, when he invented Turing machines, you know, and imagining
*  what computers would end up doing, so to speak. Yeah. You know, and it's very difficult. It's
*  difficult. Right. And it's, it's, and I mean, it's a few reasonable predictions, but most of it he
*  couldn't predict possibly by the time, by 1950, he was making reasonable predictions about something,
*  but not the 30s. Right. Not, not, not in the, not when he first, you know, conceptualized,
*  you know, and he conceptualized universal computing for a very specific mathematical reason that
*  wasn't, wasn't as general, but, but yes, it's a, it's a good sort of exercise in humility to
*  realize that, that it's kind of like, it's, it's really hard to figure these things out.
*  The engineering of, of the universe, if we know how the universe works,
*  how can we engineer it? That's such a beautiful vision. That's such a beautiful, by the way,
*  I have to mention one more thing, which is the ultimate question of, of from physics is, okay,
*  so we have this abstract model of the universe. Why does the universe exist at all? Right. So,
*  you know, we might say there is a formal model that if you run this model, you get the universe,
*  or the model gives you, you know, a model of the universe, right? You, you, you, you run this
*  mathematical thing and the mathematics unfolds in the way that corresponds to the universe.
*  But the question is, why was that actualized? Why does the actual universe actually exist?
*  And so this is, this is another one of these humility and, and is like, can you figure this
*  out? I have a guess, okay, about the answer to that. And my guess is somewhat unsatisfying,
*  but my guess is that it's a little bit similar to Gödel's second incompleteness theorem,
*  which is the statement that from within as an axiomatic theory like Peano arithmetic,
*  you cannot from within that theory prove the consistency of the theory.
*  So my guess is that for entities within the universe, there is no finite determination
*  that can be made of the, the statement. The universe exists is essentially undecidable
*  to any entity that is embedded in the universe. Within the universe. How does that make you feel?
*  Is that, does that put you at peace that it's impossible or is it really ultimately frustrating?
*  Well, I think it just says that it's not a kind of question that, you know, it's there are things
*  that it is reasonable. I mean, there's kinds of, you know, you can talk about hypercomputation as
*  well. You can say, imagine there was a hypercomputer, here's what it would do. So great,
*  it would be lovely to have a hypercomputer, but unfortunately, we can't make it in the universe.
*  Like, it would be lovely to answer this, but unfortunately, we can't do it in the universe.
*  And, you know, this is all we have, so to speak. And I think it's really just a statement. It's
*  sort of, in the end, it'll be a kind of a logical, logically inevitable statement, I think. I think
*  it will be something where it is, as you understand what it means to have, what it means to have a
*  sort of predicate of existence, and what it means to have these kinds of things, it will sort of be
*  inevitable that this has to be the case that from within that universe, you can't establish the
*  reason for its existence, so to speak, you can't prove that it exists, and so on.
*  And nevertheless, because of computational reducibility, the future
*  is ultimately not predictable, full of mystery, and that's what makes life worth living.
*  Right. I mean, right. And, you know, it's funny for me, because as a pure sort of human being
*  doing what I do, it's, you know, I'm, you know, I like, I'm interested in people, I like sort of,
*  you know, the whole human experience, so to speak. And yet, it's a little bit weird when I'm
*  thinking, you know, it's all hypergraphs down there, and it's all just...
*  Hypergraphs all the way down.
*  Right.
*  It's like turtles all the way down.
*  Yeah, yeah, right. And it's kind of, you know, it's, to me, it is a funny thing,
*  because every so often I get this, you know, as I'm thinking about, I think we've really
*  gotten, you know, we've really figured out kind of the essence of how physics works,
*  and I'm like thinking to myself, you know, here's this physical thing, and I'm like,
*  you know, this feels like a very definite thing. How can it be the case that this is just some
*  rule reference frame of, you know, this infinite creature that is so abstract and so on, and I
*  kind of, it is a, it's a funny sort of feeling that, you know, we are, we're sort of, it's like,
*  in the end, it's just sort of, be happy we're just humans type thing. And it's kind of like,
*  but we're making, we make things as, it's not like we're just a tiny speck, we are,
*  in a sense, the, we are more important by virtue of the fact that, in a sense,
*  it's not like there's, there is no ultimate, you know, it's like we're important because,
*  because, you know, we're here, so to speak, and we're not, it's not like there's a thing
*  where we're saying, you know, we are just but one sort of intelligence out of all these other
*  intelligences, and so, you know, ultimately, there'll be the super intelligence, which is
*  all of these put together, and it'll be very different from us. No, it's actually going to
*  be equivalent to us. And the thing that makes us a sort of special is just the details of us,
*  so to speak. It's not something where we can say, oh, there's this other thing, you know, just,
*  you think humans are cool, just wait until you've seen this, you know, it's going to be much more
*  impressive. Well, no, it's all going to be kind of computationally equivalent, and the thing that,
*  you know, it's not going to be, oh, this thing is amazingly much more impressive and amazingly much
*  more meaningful, let's say. No, we're it. I mean, that's the-
*  And the symbolism of this particular moment, so this has been one of the favorite conversations
*  I've ever had, Stephen. It's a huge honor to talk to you, to talk about a topic like this for four
*  plus hours on the fundamental theory of physics, and yet we're just two finite descendants of apes
*  that have to end this conversation because darkness have come upon us.
*  Yes. Right. And we're going to get bitten by mosquitoes and all kinds of terrible things.
*  The symbolism of that, we're talking about the most basic fabric of reality and having to end
*  because of the fact that things end. It's tragic and beautiful, Stephen. Thank you so much. Huge
*  honor. I can't wait to see what you do in the next couple of days and next week, a month.
*  We're all watching with excitement. Thank you so much. Thanks.
*  Thanks for listening to this conversation with Stephen Wolfram, and thank you to our sponsors,
*  Simply Safe, Sun Basket, and Masterclass. Please check out our sponsors in the description to get
*  a discount and to support this podcast. If you enjoy this thing, subscribe on YouTube,
*  review it with five stars on Apple Podcasts, follow on Spotify, support on Patreon,
*  or connect with me on Twitter at Lex Friedman. And now let me leave you with some words from
*  Richard Feynman. Physics isn't the most important thing. Love is. Thank you for listening and hope
*  to see you next time.
