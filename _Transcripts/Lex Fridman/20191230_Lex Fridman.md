---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6356s
Video Keywords: []
Video Views: 407339
Video Rating: None
Video Description: 
---

# Donald Knuth Algorithms, Complexity, and The Art of Computer Programming  Lex Fridman Podcast #62
**Lex Fridman:** [December 30, 2019](https://www.youtube.com/watch?v=2BdBfsXbST8)
*  The following is a conversation with Donald Knuth, one of the greatest and most impactful
*  computer scientists and mathematicians ever. He's the recipient of the 1974 Touring Award,
*  considered the Nobel Prize of Computing. He's the author of the multi-volume work,
*  the magnum opus, The Art of Computer Programming. He made several key contributions to the rigorous
*  analysis of computational complexity of algorithms, including the popularization
*  of asymptotic notation that we all affectionately know as the Big O notation. He also created the
*  tech typesetting system, which most computer scientists, physicists, mathematicians,
*  and scientists and engineers in general use to write technical papers and make them look
*  beautiful. I can imagine no better guest to end 2019 with than Don, one of the kindest,
*  most brilliant people in our field. This podcast was recorded many months ago. It's one I avoided
*  because perhaps counterintuitively, the conversation meant so much to me. If you can believe it,
*  I knew even less about recording back then, so the camera angle is a bit off. I hope that's
*  okay with you. The office space was a big cram for filming, but it was a magical space where Don does
*  most of his work. It meant a lot to me that he would welcome me into his home. It was quite a
*  journey to get there. As many people know, he doesn't check email, so I had to get creative.
*  The effort was worth it. I've been doing this podcast on the side for just over a year.
*  Sometimes I had to sacrifice a bit of sleep, but always happy to do it and to be part of an amazing
*  community of curious minds. Thank you for your kind words of support and for the interesting
*  discussions, and I look forward to many more of those in 2020. This is the Artificial Intelligence
*  Podcast. If you enjoy it, subscribe on YouTube, give it five stars on Apple Podcasts, follow on
*  Spotify, support on Patreon, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  I recently started doing ads at the end of the introduction. I'll do one or two minutes
*  after introducing the episode and never any ads in the middle that break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience. I provide timestamps for
*  the start of the conversation that you can skip to, but it helps if you listen to the ad and
*  support this podcast by trying out the product or service being advertised. This show is presented
*  by Cash App, the number one finance app in the App Store. I personally use Cash App to send money
*  to friends, but you can also use it to buy, sell, and deposit Bitcoin in just seconds. Cash App also
*  has a new investing feature. You can buy fractions of a stock, say $1 worth, no matter what the stock
*  price is. Broker services are provided by Cash App Investing, a subsidiary of Square, and a member
*  of the SIPC. I'm excited to be working with Cash App to support one of my favorite organizations
*  called FIRST, best known for their FIRST Robotics and LEGO competitions. They educate and inspire
*  hundreds of thousands of students in over 110 countries and have a perfect rating on Charity
*  Navigator, which means that donated money is used to maximum effectiveness. When you get Cash App
*  from the App Store or Google Play and use code LEXPODCAST, you'll get $10, and Cash App will also
*  donate $10 to FIRST, which again is an organization that I've personally seen inspire girls and boys
*  to dream of engineering a better world. And now here's my conversation with Donald Knuth.
*  In 1957 at Casetech, you were once allowed to spend several evenings with an IBM 650 computer,
*  as you've talked about in the past, and you fell in love with computing then.
*  Can you take me back to that moment with the IBM 650? What was it that grabbed you about that computer?
*  So the IBM 650 was this machine that, well, it didn't fill a room, but it was big and noisy.
*  But when I first saw it, it was through a window and there were just a lot of lights flashing on it.
*  And I was a freshman. I had a job with the statistics group and I was supposed to punch
*  cards for data and then sort them on another machine. But then they got this new computer,
*  came in and it had interesting lights. Okay, so well, but I had a key to the building so I could
*  get in and look at it and got a manual for it. And my first experience was based on the fact that
*  I could punch cards, basically, which is a big thing for the deal. But the IBM 650 was big in
*  size but incredibly small in power in memory. It had 2,000 words of memory and a word of memory was
*  10 decimal digits plus a sign. And it would do, to add two numbers together, you could probably
*  expect that would take, I'll say three milliseconds. So-
*  It's pretty fast. The memory is the constraint. The memory is the problem.
*  That was why it took three milliseconds because it took five milliseconds for the drum to go around.
*  And you had to wait, I don't know, five cycle times. If you have an instruction,
*  one position on the drum, then it would be ready to read the data for the instruction.
*  And you'd go three notches. The drum is 50 cycles around and you go three cycles
*  and you can get the data and then you can go another three cycles and get to your next
*  instruction if the instruction is there. Otherwise, you spin until you get to the right place.
*  And we had no random access memory whatsoever until my senior year. In senior year, we got 50
*  words of random access memory, which were priceless. And we would move stuff up to the
*  random access memory in 60 word chunks and then we would start again. So it was
*  subroutine when to go up there and- Could you have predicted the future
*  60 years later of computing from then? No. In fact, the hardest question I was ever asked was
*  what could I have predicted? In other words, the interviewer asked me, she said,
*  what about computing has surprised you? And immediately I rattled off a couple dozen things
*  and then she said, okay, so what didn't surprise? And I tried for five minutes to think of something
*  that I would have predicted and I couldn't. But let me say that this machine, I didn't know,
*  there wasn't much else in the world at that time. The 650 was the first
*  machine that there were more than a thousand of ever. Before that, each machine there might be
*  a half a dozen examples, maybe a couple dozen. The first mass market, mass produced.
*  The first one, yeah, done in quantity. And IBM didn't sell them, they rented them, but they
*  rented them to universities at great, you know, had a great deal. And so that's why
*  a lot of students learned about computers at that time.
*  So you refer to people, including yourself, who gravitate toward a kind of computational
*  thinking as geeks. At least I've heard you use that terminology.
*  It's true that I think there's something that happened to me as I was growing up that made my
*  brain structure in a certain way that resonates with computers.
*  So there's this space of people, it's 2% of the population you empirically estimate.
*  That's been fairly constant over most of my career, however,
*  it might be different now because kids have different experiences when they're young.
*  So what does the world look like to a geek? What is this aspect of thinking that is unique to...
*  That makes a geek.
*  This is a very important question. In the 50s, IBM noticed that there were geeks and non-geeks,
*  and so they tried to hire geeks. And they put out Asperger's papers saying,
*  if you play chess, come to Madison Avenue for an interview or something like this.
*  They were trying for some things. So what is it that I find easy and other people
*  tend to find harder? And I think there's two main things. One is this ability to jump levels of
*  abstraction. So you see something in the large and you see something in the small,
*  and you pass between those unconsciously. So you know that in order to solve some big problem,
*  what you need to do is add one to a certain register and that gets you to another step.
*  And below the... I don't go down to the electron level, but I knew what those middle
*  seconds were, what the drum was like. On the 650, I knew how I was going to factor a number or
*  find a root of an equation or something because of what I was doing. And as I'm debugging,
*  I'm going through, did I make a key punch error? Did I write the wrong instruction? Do I have the
*  wrong thing in a register? And each level is different. And this idea of being able to
*  see something at lots of levels and fluently go between them seems to me to be much more pronounced
*  in the people that resonate with computers. So in my books, I also don't stick just to the high
*  level, but I mix low level stuff with high level. And this means that some people think
*  that I should write better books. And that's probably true. But other people say,
*  if you think like that, then that's the way to train yourself, like keep mixing the levels and
*  learn more and more how to jump between. So that's the one thing. The other thing is
*  that it's more of a talent to be able to deal with non-uniformity where there's case one,
*  case two, case three, instead of having one or two rules that govern everything.
*  So it doesn't bother me if I need, like an algorithm has 10 steps to it. Each step does
*  something else that doesn't bother me. But a lot of pure mathematics is based on one or two rules,
*  which are universal. And so this means that people like me sometimes work with systems that are more
*  complicated than necessary because it doesn't bother us that we didn't figure out the simple
*  rule. And you mentioned that while Jacobi, Boole, Abel, and all the mathematicians in the 19th
*  century may have had symptoms of geek, the first 100% legit geek was Turing, Alan Turing.
*  I think he had a lot more of this quality than anybody, just from reading the kind of stuff he
*  did. So what influence has Turing had on you in your way of thinking?
*  Well, okay. So I didn't know that aspect of him until after I graduated some years. As undergrad,
*  we had a class that talked about computability theory and Turing machines. And it was all,
*  it sounded like a very specific kind of purely theoretical approach to stuff. So when, how old
*  was he when I learned that he had a design machine and that he wrote a wonderful manual for
*  for Manchester machines. And he invented all, you know, subroutines. And he was a real hacker
*  that he got his hands dirty. I thought for many years that he had only done purely formal work.
*  As I started reading his own publications, I could, you know, I could feel this kinship.
*  And, and of course he had a lot of peculiarities. Like he wrote numbers backwards because,
*  I mean, left to right instead of right to left, because that's the,
*  that's, it was easier for computers to process them that way.
*  What do you mean left to right?
*  He would write pi as, you know, 9514.3. I mean, okay.
*  Right. Got it.
*  401.3 on the blackboard. I mean, when he, he, he, he had trained himself to,
*  to do that because the computers he was working with worked that way inside.
*  Trained himself to think like a computer. Well, there you go. That's, that's geek thinking.
*  Yeah.
*  You've practiced some of the most elegant formalism in computer science.
*  And yet you're the creator of a concept like literate programming,
*  which seems to move closer to natural language type of description of programming.
*  Yeah, absolutely.
*  So how do you see those two as conflicting as the formalism of theory and the idea of
*  literate programming?
*  So there, there we are in a non-uniform system where I don't, where I don't think one,
*  one size fits all and I'm not sure how to put it.
*  I don't think all truth lies in one, in one kind of expertise. And so somehow in a way you'd say
*  my life is a convex combination of English and mathematics.
*  And you're okay with that.
*  And not only that, I think I wish, you know, I want my kids to be that way. I want et cetera,
*  you know, use left brain, right brain at the same time. You got a lot more done. That's,
*  that was part of the, part of the bargain.
*  And I've heard that you didn't really read for pleasure until into your thirties.
*  Literature.
*  That's true. You know more about me than I do, but I'll try to be consistent with what you read.
*  Yeah, no, just believe me. I just go with whatever story I tell you. It'll be easier that way.
*  The conversation.
*  Right. Yeah, no, that's true.
*  So I've heard mention of Philip Roth's American Pastoral, which I love as a book.
*  I don't know if it was, it was mentioned as something I think that was meaningful to you as
*  well. In either case, what literary books had a lasting impact on you? What literature?
*  Okay, good, good question. So I, so I, I met Roth.
*  Oh, really?
*  Well, we both got doctors from Harvard on the same day. So, so we were, yeah, we had lunch together
*  and stuff like that. And, but he knew that, you know, computer books would never sell. Well,
*  all right. So you say you, you, you, you were a teenager when you left Russia. So
*  I have to say that Tolstoy was one of the big influences on me. I especially like Anna Karnina,
*  not because of, of particular of the plot of the story where, but because
*  there's this character who, you know, the philosophical discussions, it's all, it's a,
*  it's a whole way of life is worked out there among the characters. And so, and so that I thought was,
*  was especially beautiful. On the other hand, Dostoevsky, I, I didn't like it all because I,
*  I felt that he, his genius was mostly because he kept forgetting what he,
*  what he had started out to do and he was just sloppy. I, I didn't think that, that, that,
*  that he polished his stuff at all. And I tend to admire somebody who,
*  who dots the I's and crosses the T's.
*  So the music of the prose is what you admire more than?
*  I certainly do admire the music of the language, which I couldn't appreciate
*  in the Russian original, but, but I can in Victor Hugo, you know, because close,
*  French is much, is closer. But Tolstoy, I like the same reason I like Herman Wouk as a,
*  as a novelist. I think, like his book, Marjorie Morningstar has a similar
*  character in Hugo who developed his own personal philosophy and expo and it goes in.
*  Was consistent.
*  Yeah, right. And it's worth, worth pondering. So, yeah.
*  So you don't like Nietzsche and, uh.
*  Like what?
*  You don't like Friedrich Nietzsche or.
*  Nietzsche, yeah, no, no, yeah, this has never, I keep seeing quotations from Nietzsche and,
*  and he never tempted me to read any further.
*  Well, he's full of contradictions, so you will certainly not appreciate him.
*  But Schiller, you know, I'm trying to get, get across what I appreciate in literature.
*  And part of it is the, is, is as you say, the music of the language, of the way it flows
*  and take Raymond Chandler versus Dashiell Hammett. Dashiell Hammett's sentences are awful
*  and Raymond Chandler's are beautiful. They just flow. So I, I don't, uh, I don't read
*  literature because it's supposed to be good for me or because somebody said it's great. But,
*  but I find things that I like. I mean, uh, you mentioned you were dressed like James Bond. So I,
*  I love Ian Fleming. I think he's got, he had a really great gift for, if he has a golf game
*  or a game of bridge or something, and this comes into his story, it'll, it'll be the most exciting
*  golf game or, or, or, you know, the absolute best possible hands of bridge that, that exists. And,
*  and, and he, he exploits it and tells it beautifully. So.
*  So in connecting some things here, looking at literate programming and being able to
*  it convey, uh, encode algorithms to a computer in a way that mimics how humans speak,
*  uh, how, what do you, what do you think about natural language in general and the messiness
*  of our human world about trying to express difficult things? So the idea of literate
*  programming is to, is really to try to, uh, understand something better by seeing it from
*  at least two perspectives, the formal and the informal. If we're trying to understand a
*  complicated thing, if we can look at it in different ways. And so this is in fact,
*  the key to technical writing, uh, a good technical writer, trying not to be obvious about it, but
*  says everything twice, uh, formally and informally, or maybe three times, but you try to give, uh,
*  the, uh, the reader, um, a way to, to put the concept into his own brain or her own brain.
*  Is that better for the writer or the reader or both?
*  Well, the writer just tries to understand the reader. That's the goal of a writer is to,
*  to have a good mental image of the reader and to say what the reader expects next and to,
*  to impress the reader with what has impressed the writer
*  why something is interesting. So, so when you have a computer program, we try to,
*  instead of looking at it as something that we're just trying to give an instruction to the
*  computer. What we really want to be is giving, giving insight to the person who's, uh, uh,
*  going to be maintaining this program or, or to the programmer himself when he's debugging it
*  as to why this stuff is being done. And so all the techniques of exposition that a teacher uses or
*  book writer uses make you better programmer if your, if your program is going to be,
*  uh, not just a one shot deal.
*  So how difficult is that? Do you see hope for the combination of informal and formal
*  for the programming task?
*  Yeah, I, I'm the wrong person to ask, I guess, because I'm a geek, but, but I think for a geek,
*  it's easy. I know, I don't know, not some people have difficulty writing and that might be because
*  there's something in their brain structure that makes it hard for them to write or, uh,
*  or it might be something just that they haven't had enough practice. I'm not the right one to,
*  to judge, but I don't think you can teach any person any particular skill. I do think that,
*  that writing is, is half of my life. And so I put it together in the program. Even when,
*  right? Even when I'm writing a one shot program, I, I write it in a literate way,
*  because I get it right faster that way.
*  Now, does it get compiled automatically?
*  Or so I guess on the technical side, my question was how difficult is it design a system where
*  much of the programming is done informally?
*  Informally?
*  Yeah, informally.
*  I think, uh, whatever works to make it understandable is good. Uh, but then you have to
*  also understand how informal it is. You have to know the limitations you have to, you, you,
*  so by putting the formal and informal together, this, this is where,
*  this is where it gets locked into your, into your brain. You can, you can say informally,
*  uh, well, I'm working on a problem right now, so.
*  Let's go there. Can you give me an example of, um, of connecting the informal and the formal?
*  Well, it's a little too complicated an example. There's a puzzle that's self-referential. It's
*  called a Japanese arrow puzzle and, uh, and, and you're given a bunch of boxes. Each one points
*  north, east, south or west. And at the end, you're supposed to fill in each box with the number of
*  distinct numbers that it points to. So if I put a three in a box, that means that, and it's pointing
*  to five other boxes, that means that there's going to be three different numbers in those five boxes.
*  And, uh, and those boxes are pointing, one might be pointing to me, one might be pointing the other,
*  the other way. But anyway, I, I'm supposed to find a set of numbers that obeys this complicated
*  condition that each number counts how many distinct numbers, uh, it points to. Well, um,
*  and, uh, so a guy sent me his solution to this problem where he, where he, um,
*  uh, uh, uh, uh, presents formal statements that, that, that say either this is true or this is true
*  or this is true. And, and, and so I try to render that formal statement informally. And I try to say,
*  I contain a three and, and, uh, the guys I'm pointing to, uh, contain the numbers one, two and
*  six. So by putting it informally, and also I convert it into a, into a dialogue statement, uh,
*  uh, that helps me understand the logical statement that he's written down as a string of numbers
*  in terms of some abstract variables that he had. That's really interesting. So maybe an extension
*  of that. There has been a resurgence in computer science and machine learning and, uh, neural
*  networks. So using data to construct algorithms. So it's another way to construct algorithms really.
*  Yes. If you can think of it that way. Uh, uh, so as opposed to natural language to construct
*  algorithms, use data to construct algorithms. So what, uh, what's your view of this branch of
*  computer science, uh, where data is almost more important than the, uh, mechanism of the algorithm?
*  It seems to be, um, suited to a certain kind of non-geek, uh, and which is probably why it's,
*  it's, uh, it's taken off. It has its own community that that really, that really resonates with that.
*  But, um, it's hard to, you know, to trust something like that because nobody, even the people who,
*  who work with it, that they have no idea what has, what has been learned.
*  That's a really interesting thought that it's, uh, it makes algorithms more accessible to a different
*  community, a different type of brain. Yep. And that's really interesting because, uh,
*  just like literate programming, perhaps could make programming more accessible to a certain kind of
*  brain. There are people who think it's just a matter of education, uh, and anybody can learn
*  to be a great programmer. Anybody can learn to be a great, uh, uh, uh, skier. Um, uh, you know, I, I,
*  I wish that were true, but I, but I know that there's a lot of things that I've tried to do.
*  And I, and I was well motivated and I, and I kept trying to build myself up and I never got past a
*  certain level. Uh, I can't view, for example, I can't view, uh, uh, three, three dimensional
*  objects in my, in my head. I have to, I have to make a model and look at it and study it from all
*  points of view. And then I start to get some idea of, but other people are good at four dimensions.
*  Physicists. Yeah. So let's go to, uh, the art of computer programming in 1962, you set the table
*  of contents for this, uh, magnum opus, right? It was supposed to be a single book with 12 chapters.
*  Now today, what is it? 57 years later, you're in the middle of volume four of seven.
*  And in the middle of volume four B is four B or precisely can ask you for an impossible task,
*  which is try to summarize the book so far, maybe by giving a little examples. So from the sorting
*  and the search and the combinatorial algorithms, if you were to give a summary,
*  a quick elevator summary, but depending how many floors there are in the building. Yeah.
*  The first volume called fundamental algorithms talks about something that you can't, the stuff
*  you can't do without. Uh, you have to, you have to know the basic concepts of what is a program,
*  what is it, what is the algorithm and, uh, and, and it also talks about a low level machine. So
*  you can have some, some kind of an idea what's going on. And it has basic concepts of input,
*  output and, uh, subroutines induction, induction, right? Mathematical preliminary. So, so the thing
*  that makes my book different from a lot of others is that all that I try to not only present the
*  algorithm, but I try to analyze them and which means quantitatively, I say not only does it work,
*  but it works this fast. Okay. And so I need math for them. And then there's the standard way to
*  structure data inside and represent information in the computer. So that's all volume one of
*  volume two talks. It's called semi-numerical algorithms. And here we're, here we're,
*  we're writing programs, but we're also dealing with numbers. Algorithms deal with, with, with
*  any kinds of objects, but, but specific when there's objects are numbers, well, then, then we have
*  certain special paradigms that, that apply to things that have evolved numbers. And so there's,
*  there's, there's, there's arithmetic on numbers and, and there's matrices full of numbers. There's
*  random numbers and there's power series full of numbers. There's different algebraic concepts
*  that have numbers in structured ways. And arithmetic in the way a computer would think about arithmetic.
*  So floating point, floating point arithmetic, high precision arithmetic, not only addition,
*  subtraction, multiplication, but also comparison of numbers. So then check, then volume three talks
*  about sorting and search. I like that one. Sort and search. Sorting and search. I love sorting.
*  Right. So, so here, you know, we're not dealing necessarily with numbers because you sort letters
*  and other objects and searching we're doing all the time with Google nowadays, but I mean,
*  we have to find stuff. So again, algorithms that, that underlie all kinds of applications.
*  None of these volumes is about a particular application, but the applications are examples
*  of why people want to know about sorting, why people want to know about random numbers.
*  So then volume four goes into combinatorial algorithm. This is where we have
*  zillions of things to deal with. And we, and here we keep finding cases where one good idea can,
*  can make something go more than a million times faster. And, and, and we're dealing with problems
*  that are probably never going to be solved efficiently, but that doesn't mean we give up
*  on them. And, and, and we have this chance to have good ideas and go much, much faster on them. So,
*  that's combinatorial algorithms. And those are the ones that are, I mean, you say sorting is
*  most fun for you. Well, it's true, it's fun, but combinatorial algorithms are the ones that I always,
*  that I always enjoyed the most because that's when my skill at programming had the most payoff.
*  And the different, the difference between an obvious algorithm that you think of first thing
*  and a, you know, and a good, and an interesting subtle algorithm that not so obvious, but, but
*  run circles around the other one. That's, that's where computer science really comes,
*  comes in. And a lot of these combinatorial methods were found first in applications
*  to artificial intelligence or cryptography. And in my case, I, I just liked them and it was
*  associated more with puzzles. Do you like them most in the domain of graphs and graph theory?
*  Graphs are great because they're, they're, they're terrific models of so many things in the real world
*  and you throw numbers on a graph, you've got a network and so there you, there you have many more
*  things. So, but combinatorial in general is any arrangement of objects that, that has some kind of
*  higher structure, non-random structure. And it's okay. Is it possible to put something together
*  satisfying all these conditions? Like I mentioned arrows a minute ago, you know, is there a way to,
*  to put these numbers on a bunch of boxes that are pointing to each other? Is that going to be
*  possible at all? That's volume four. That's volume four. What does the future hold?
*  Volume 4A was part one. And, and what happened was in 1962, when I started writing down a table of
*  contents, it wasn't going to be a book about computer programming in general. It was going
*  to be a book about how to write compilers. And I was asked to write a book explaining how to,
*  how to write a compiler. And at that time there were only a few dozen people in the world who
*  had written compilers and I happened to be one of them. So, and I also had some experience writing
*  for like the campus newspaper and things like that. So, so I said, okay, great. I'm the only
*  person I know who, who's written a compiler, but hasn't invented any new techniques for writing
*  compilers. And all the other people I knew had super ideas, but I couldn't see that they would
*  be able to write a book that wouldn't, that would describe anybody else's ideas with their own.
*  So I could be the, I could be the journalist and I could explain what all these cool ideas about
*  compiler writing were. And, and then I, I started putting down, well, yeah, let me, you need
*  have a chapter about data structures. You need to have some introductory material.
*  You want to talk about searching because a compiler writer has to, has to look up the
*  variables in a symbol table and find out, you know, which, which, when you, when you write the
*  name of the variable in one place, it's supposed to be the same as the one you put somewhere else.
*  So you need all these basic techniques and I, and I, you know, kind of know some arithmetic and stuff.
*  So I, so I threw in these chapters and I threw in a chapter on combinatorics because that was what
*  I really enjoyed programming the most, but there weren't many algorithms known about combinatorial
*  methods in 1962. So that was a kind of a short chapter, but it was sort of thrown in just for fun.
*  And chapter 12 was going to be actual compilers, applying all the stuff in chapters 1 to 11
*  to make compilers. Well, okay. So that was my table of contents from 1962. And during the 70s,
*  the whole field of combinatorics went through a huge explosion. People talk about combinatorial
*  explosion and they usually mean by that, that the number of cases goes up, you know, you change
*  end to end plus one and all of a sudden you, your problem has gotten more than 10 times harder. But
*  there was an explosion of ideas about combinatorics in the 70s to the point that it, like, take 1975,
*  I bet you more than half of all the journals of computer science were about combinatorial methods.
*  What kind of problems were occupying people's minds? What kind of problems in combinatorics?
*  Was it set up to satisfy ability graph theory? Yeah. Graph theory was quite dominant. I mean,
*  but all of the NP hard problems that you have, like Hamiltonian path or
*  Fowler-Salesman. Going beyond graphs, you had operation research whenever there was a small
*  class of problems that had efficient solutions and they were usually associated with Matroid
*  theory, special mathematical construction. But once we went to things that involve three things
*  at a time instead of two, all of a sudden things got harder. So we had satisfiability problems where
*  if you have clauses, every clause has two logical elements in it, then we can satisfy it
*  linear time. We can test for satisfiability in linear time, but if you allow yourself three
*  variables in a clause, then nobody knows how to do it. So these articles were about trying to
*  find better ways to solve cryptography problems and graph theory problems. We have lots of data,
*  but we didn't know how to find the best subsets of the data. With sorting,
*  we could get the answer. It didn't take long. So how did it continue to change from the 70s to today?
*  Yeah. So now there may be half a dozen conferences whose topic is combinatorics,
*  a different kind, but fortunately I don't have to rewrite my book every month like I had to in the
*  70s. But still there's a huge amount of work being done and people getting better ideas on
*  these problems that don't seem to have really efficient solutions, but we still get to do a
*  lot more with them. And so this book that I'm finishing now is, I've got a whole bunch of brand
*  new methods that as far as I know, there's no other book that covers this particular approach.
*  So I'm trying to do my best of exploring the tip of the iceberg and I try out lots of things and
*  keep rewriting as I find better methods. So what's your writing process like? What's
*  your thinking and writing process like every day? What's your routine even?
*  I guess it's actually the best question because I spend seven days a week doing it.
*  You're the most prepared to answer it.
*  Yeah. But okay. So the chair I'm sitting in is where I do...
*  It's where the magic happens.
*  Well, reading and writing. The chair is usually sitting over there where I have some reference
*  book, but I found this chair which was designed by a Swedish guy anyway. It turns out this is the
*  only chair I can really sit in for hours and hours and not know that I'm in a chair. But then I have
*  the standup desk right next to us and so after I write something with pencil and eraser, I get up
*  and I type it and revise and rewrite standing up.
*  The kernel of the idea is first put on paper.
*  Yeah.
*  That's where...
*  Right. And I'll write maybe five programs a week, of course, literate programming.
*  And these are... Before I describe something in my book, I always program it to see how it's
*  working and I try it a lot. So for example, I learned at the end of January, I learned of a
*  breakthrough by four Japanese people who had extended one of my methods in a new direction.
*  And so I spent the next five days writing a program to implement what they did. But they had only
*  generalized part of what I had done, so then I had to see if I could generalize more parts of it.
*  And then I had to take their approach and I had to try it out on a couple of dozen of the other
*  problems I had already worked out with my old methods. And so that took another couple of
*  weeks. And then I started to see the light and I started writing the final draft and then I would
*  type it up, involve some new mathematical questions. And so I wrote to my friends who
*  might be good at solving those problems and they solved some of them. And so I put that in as
*  exercises. And so a month later, I had absorbed one new idea that I learned and I'm glad I heard
*  about it in time, otherwise I wouldn't put my book out before I'd heard about the idea.
*  On the other hand, this book was supposed to come in at 300 pages and I'm up to 350 now.
*  That added 10 pages to the book. But if I learn about another one, my publisher is going to shoot
*  me. Well, so in that process, in that one month process, are some days harder than others?
*  Are some days harder than others? Well, yeah, my work is fun, but I also work hard and every big
*  job has parts that are a lot more fun than others. And so many days I'll say, why do I have to have
*  such high standards? Why couldn't I just be sloppy and not try this out and just report the answer?
*  But I know that people are counting me to do this and so, okay, so okay, Don, I'll grit my teeth and
*  do it. And then the joy comes out when I see that actually I'm getting good results. And I get,
*  and I even more when I see that somebody has actually read and understood what I wrote and
*  told me how to make it even better. I did want to mention something about the method. So I got this
*  tablet here where I do the first writing of concepts. Okay. So, so, and what language is that?
*  And right, so here, take a look at it, but you know, here,
*  random say, explain how to draw such skewed pixel diagrams. Okay. So I got this paper
*  about 40 years ago when I was visiting my sister in Canada and they make tablets of paper with
*  this nice large size and just the right very small space between lines. Yeah. Maybe I'll also just
*  show it. Yeah. Yeah. Wow. You know, I've got these manuscripts going back to the sixties
*  and, and those are when I get my ideas on paper. Okay. But I'm a good typist. In fact,
*  I went to typing school when I was, when I was in high school and so I can type faster than I think.
*  So then when I do the editing and stand up and type, then I, then I revise this and it comes out
*  a lot different than what, you know, for style and rhythm and things like that come out at the,
*  at the typing state. And you type in tech. And I type in tech. And can you, can you think in tech?
*  No. So to a certain extent I have, I have only a small number of, of idioms that I use, like,
*  you know, I'm beginning with theorem, I do something for displayed equation, I do something
*  and so on. But I, but I, I have to see it. And in the way that it's on paper here. Yeah. Right.
*  So for example, Turing wrote what the other direction you don't write macros. You don't
*  think in macros. Not particularly, but when I need a macro, I'll go ahead and do it. But the thing is
*  I also write to fit. I mean, I'll, I'll change something if I can, if I can save a line.
*  I'll, you know, it's like Haiku. I'll figure out a way to rewrite the sentence so that it'll look
*  better on the page. And I shouldn't be wasting my time on that, but, but I can't resist because I
*  know it's only another 3% of the time or something like that. And it could also be argued that that
*  is what life is about. Ah, yes. In fact, that's true. Like, like I worked in the garden one day
*  a week and that's, that's kind of a description of my life is getting rid of weeds, you know,
*  removing bugs for programs. And so, you know, a lot of writers talk about, you know, basically
*  suffering the writing processes, having, you know, it's extremely difficult. And I think of
*  programming, especially the, or technical writing that you're doing can be like that.
*  Do you find yourself methodologically, how do you every day sit down to do the work?
*  Is it a challenge? You kind of say it's, you know, it's fun,
*  but it'd be interesting to hear if there are non-fun parts that you really struggle with.
*  Yeah. So the fun comes when I'm able to put together ideas of two people who didn't
*  know about each other. And so I might be the first person that saw both of their ideas. And so then,
*  then I get to make the synthesis and that gives me a chance to be creative. But the dredge work is
*  where I, I've got to chase everything down to its root. This leads me into really interesting
*  stuff. I mean, I learn about Sanskrit and I, and, you know, I try to give credit to all the authors.
*  And so I write, so I write to people who know the people, authors, if they're dead or I communicate
*  this way. And I got to get the math right. And I got to tackle all my programs, try to find holes
*  in them. And I rewrite the programs over after I get a better idea. Is there ever dead ends?
*  Dead ends. Oh yeah. I throw stuff out. Yeah. One of the things that I spend a lot of time preparing,
*  a major example based on the game of baseball. And I know a lot of people who, for whom baseball
*  is the most important thing in the world, you know, but I also know a lot of people
*  from cricket is the most important in the world or soccer or something, you know. And,
*  and I realized that if I had a big example, I mean, it was going to have a fold out illustration
*  and everything. I was saying, well, what, what am I really teaching about algorithms here where I had
*  this, this, this baseball example? And if I was a person who, who, who knew only cricket,
*  what would they think about this? And so, so I've ripped the whole thing out, but I, you know, I had,
*  I had something that would have really appealed to people who grew up with baseball as, as, as,
*  as a major theme in their life. Which is a lot of people, but, but just, yeah. So I still a minority.
*  Small minority. I took out bowling too. Even a smaller minority.
*  What's the art in the art of programming? Why, why is there of the few words in the title,
*  why is art one of them? Yeah. Well, that's, that's what I wrote my Turing lecture about. And
*  so when people talk about art, it really, I mean, what the word means is
*  something that's not in nature. So when you have artificial intelligence, the art comes from the
*  same route saying that this is something that was created by, by human beings. And then it's gotten
*  a further meaning often of fine art, which has this beauty to the, to the mix. And so as you know,
*  we have things that are artistically done and, and this means not only done by humans, but also
*  done in a way that's elegant and brings joy and, and has, has, I guess, Tolstoy versus Dostoevsky.
*  Right. But anyway, it, it's that part that, that says that it's done well as well as not only
*  different from nature. In general, then art is what human beings are specifically good at. And when
*  they say artificial intelligence, well, they're trying to mimic human beings. But there's an
*  element of fine art and beauty. You are one. That's what I, that's what I try to also say that you
*  can write a program and make a work of art. So now in terms of surprising, you know, what ideas in,
*  in writing from sort and search to the combinatorial algorithms, what ideas have you come across
*  that were particularly surprising to you that's that changed the way you see a space of problems?
*  I get a surprise every time I have a bug in my program, obviously, but that isn't really what
*  you're looking for. More transformational than surprising. For example, in volume four A,
*  I was especially surprised when I learned about data structure called BDD, Boolean Decision Diagram,
*  because I sort of had the feeling that as an old timer, and you know, I've been programming
*  since the 50s, and BDDs weren't invented until 1986. And here comes a brand new idea that
*  revolutionizes the way to represent a Boolean function. And Boolean functions are so basic to
*  all kinds of things in, I mean, logic is underlies everything we can describe, all of what we know
*  in terms of logic somehow, and propositional logic. I thought that was cut and dried and
*  everything was known. But here comes Randy Bryant and discovers that BDDs are incredibly powerful.
*  Then, so that means I have a whole new section to the book that I never would have thought of
*  until 1986, not even until 1990s, when people started to use it for, you know, a billion
*  dollars of applications. And it was the standard way to design computers for a long time until
*  SAT solvers came along in the year 2000. So that's another great big surprise.
*  So a lot of these things have totally changed the structure of my book.
*  And the middle third of volume 4B is about SAT solvers, and that's
*  300 plus pages, which is all about material, mostly about material that was discovered in
*  this century. And I had to start from scratch and meet all the people in the field and write.
*  I have 15 different SAT solvers that I wrote while preparing that.
*  Seven of them are described in the book, others were from my own experience.
*  So newly invented data structures or ways to represent?
*  A whole new class of algorithm.
*  A whole new class of algorithm.
*  Yeah. And the interesting thing about the BDDs was that the theoreticians started looking at it and
*  and started to describe all the things you couldn't do with BDDs. And so they were getting
*  a bad name because, you know, okay, they were useful, but they didn't solve every problem.
*  I'm sure that the theoreticians are in the next 10 years are going to show why machine learning
*  doesn't solve everything. But I'm not only worried about the worst case, I get a huge delight when I
*  can actually solve a problem that I couldn't solve before. Even though I can't solve the problem that
*  it suggests as a further problem, I know that I'm way better than I was before. And so I found out
*  that BDDs could do all kinds of miraculous things. And so I had to spend quite a few years
*  learning about that territory.
*  So in general, what brings you more pleasure? Proving or showing a worst case analysis of an algorithm
*  or showing a good average case or just showing a good case that, you know, something good
*  pragmatically can be done with this algorithm?
*  Yeah, I like a good case that that is maybe only a million times faster than I was able to do before.
*  But I'm not worried about the fact that it's still that it's still going to take too long if I double
*  the size of the problem.
*  So that said, you popularized the asymptotic notation for describing running time. Obviously,
*  in the analysis of algorithms, worst case is such an important part. Do you see any aspects of that
*  kind of analysis as lacking? And notation too?
*  Well, the main purpose, we should have notations that help us for the problems we want to solve.
*  And so they match our intuitions. And people who worked in number theory had used asymptotic
*  notation in a certain way, but it was only known to a small group of people. And I realized that,
*  in fact, it was very useful to be able to have a notation for something that we don't know exactly
*  what it is, but we only know partial about it and so on. So for example, instead of big O notation,
*  let's just take a much simpler notation where I'd say zero or one or zero one or two.
*  And suppose that when I had been in high school, we would be allowed to put in the middle of our
*  formula, x plus zero one or two equals y. And then we would learn how to multiply two such
*  expressions together and deal with them. Well, the same thing, big O notation says,
*  here's something that's, I'm not sure what it is, but I know it's not too big.
*  I know it's not bigger than some constant times n squared or something like that.
*  Right.
*  So I write big O of n squared. Now I learn how to add big O of n squared to big O of n cubed. And I
*  know how to add big O of n squared to plus one and square that and how to take logarithms,
*  exponentials, we have big O's in the middle of them. And that turned out to be hugely valuable
*  in all of the work that I was trying to do as I'm trying to figure out how good an algorithm is.
*  So have there been algorithms in your journey that perform very differently in practice than
*  they do in theory? Well, the worst case of a combinatorial algorithm,
*  is almost always horrible. But we have SAT solvers that are solving, where one of the
*  last exercises in that part of my book was to figure out a problem that has 100 variables
*  that's difficult for a SAT solver. But you would think that a problem with 100 billion variables
*  requires you to do two to the 100th operations because that's the number of possibilities when
*  you have 100 billion variables in two to the 100th. Two to the 100th is way bigger than
*  than we can handle. 10 to the 17th is a lot.
*  You've mentioned over the past few years that you believe p may be equal to np, but that is not
*  really... If somebody does prove that p equals np, it will not directly lead to an actual algorithm
*  to solve difficult problems. Can you explain your intuition here? Has it been changed?
*  And in general, on the difference between easy and difficult problems of p and np and so on?
*  Yeah. So the popular idea is if an algorithm exists, then somebody will find it.
*  And it's just a matter of writing it down. But many more algorithms exist than anybody can
*  understand or ever make use of. Or discover, yeah.
*  Because they're just way beyond human comprehension. The total number of algorithms is
*  is more than mind boggling. So we have situations now where we know that algorithms exist,
*  but we don't know the foggiest idea what the algorithms are. There are simple examples based
*  on game playing where you say, well, there must be an algorithm that exists to win in the game of
*  hex because for the first player to win in the game of hex because hex is always either a win
*  for the first player or the second player. What's the game of hex?
*  There's a game of hex which is based on putting pebbles onto a hexagonal board. And the white
*  player tries to get a white path from left to right and the black player tries to get a black
*  path from bottom to top. And how does capture occur?
*  And there's no capture. You just put pebbles down one at a time. But there's no draws because
*  after all the white and black are played, there's either going to be a white path across from each
*  to west or a black path from bottom to top. So there's always, you know, it's the perfect
*  information game and people take turns like a tic-tac-toe. And the hex board can be
*  different sizes, but there's no possibility of a draw and players move one at a time.
*  And so it's got to be either a first player win or a second player win. Mathematically,
*  you follow out all the trees and either there's always a win for the first player, second player.
*  Okay. And it's finite. The game is finite. So there's an algorithm that will decide,
*  you can show it has to be one or the other because the second player could mimic the first player
*  with kind of a pairing strategy. And so you can show that it has to be one way or the other.
*  But we don't know any algorithm anyway. There are cases where you can prove the existence of
*  a solution, but nobody knows anyway how to find it. But more like the algorithm question,
*  there's a very powerful theorem in graph theory by Robinson and Seymour that says that every
*  class of graphs that is closed undertaking miners has a polynomial time algorithm to determine
*  whether it's in this class or not. Now, a class of graphs, for example, planar graphs, these are
*  graphs that you can draw in a plane without crossing lines. And the planar graph is taking
*  a graph. Taking miners means that you can shrink an edge into a point or you can delete an edge.
*  And so you start with a planar graph, shrink any edge to a point is still planar.
*  Deleting an edge is still planar. Okay. Now, but there are millions of different
*  ways to describe a family of graphs that still remains the same undertaking miners.
*  And Robertson and Seymour proved that any such family of graphs, there's a finite number of
*  minimum graphs that are obstructions. So that if it's not in the family, then it has to contain
*  it. Then there has to be a way to shrink it down until you get one of these bad minimum graphs
*  that's not in the family. In the case of a planar graph, the minimum graph is a five-pointed star
*  where everything pointed to another and the minimum graph consisting of trying to connect
*  three utilities to three houses without crossing lines. And so there are two bad graphs that are
*  not planar. And every non-planar graph contains one of these two bad graphs by shrinking and
*  removing edges. Sorry, can you say that again? So he proved that there's a finite number of
*  these bad graphs. There's always a finite number. So somebody says, here's a family-
*  It's hard to believe.
*  And they put in a sequence of 20 papers. I mean, it's deep work, but it's-
*  Because that's for any arbitrary class.
*  Any arbitrary class that's closed under taking minors.
*  Maybe I'm not understanding because it seems like a lot of them are closed under taking minors.
*  Almost all the important classes of graphs are. There are tons of such graphs, but also
*  hundreds of them that arise in applications. I have a book over here called
*  The Classes of Graphs. And it's amazing how many different classes of graphs that people
*  have looked at.
*  So why do you bring up this theorem or this proof?
*  Now, there are lots of algorithms that are known for special class of graphs. For example,
*  if I have a quarter graph, then I can color it efficiently. If I have some kind of graphs,
*  it'll make a great network. So you'd like to test it. Somebody gives you graphs,
*  oh, is it in this family of graphs? If so, then I can go to the library and find an algorithm
*  that's going to solve my problem on that graph.
*  We want to have a graph that says-
*  An algorithm that says,
*  give me a graph, I'll tell you whether it's in this family or not.
*  All I have to do is test whether or not- Does this given graph have a minor? That's one of
*  the bad ones. A minor is everything you can get by shrinking and removing it.
*  Given any minor, there's a polynomial time algorithm saying,
*  I can tell whether this is a minor of you. There's a finite number of bad cases.
*  Does it have this bad case? polynomial time, I got the answer. Does it have this bad case?
*  polynomial time, I got the answer. Total polynomial time. I've solved the problem. However,
*  all we know is that the number of minors is finite. We might only know one or two of those
*  minors, but we don't know if we've got 20 of them. We don't know if there might be 21, 25.
*  All we know is that it's finite. Here we have a polynomial time algorithm that we don't know.
*  That's a really great example of what you worry about or why you think P equals NP won't be useful,
*  but still, why do you hold the intuition that P equals NP?
*  Because you have to rule out so many possible algorithms as being not working.
*  You can take the graph and you can represent it in terms of certain prime numbers, and then you
*  can multiply those together, and then you can take the bitwise and construct some certain
*  constant in polynomial time. That's a perfectly valid algorithm. There are so many algorithms of
*  that kind. A lot of times we see random, you take data and we get coincidences that some
*  fairly random-looking number actually is useful because it happens to solve a problem just because
*  there are so many hairs on your head. It seems unlikely that two people are going to have the
*  same number of hairs on their head. You can count how many people there are and how many hairs on
*  their head. There must be people walking around in the country that have the same number of hairs
*  on their head. That's a coincidence that you might say also this particular combination of operations
*  just happens to prove that a graph has a Hamiltonian path. I see lots of cases where
*  unexpected things happen when you have enough possibilities.
*  Because the space of possibilities is so huge, your intuition just says it's not.
*  You have to rule them all out. That's the reason for my intuition. It's by no means a proof.
*  I mean, some people say, well, P can't equal NP because you've had all these smart people.
*  The smartest designers have been racking their brains for years and years,
*  and there's million-dollar prizes out there. Nobody has thought of the algorithm, so there must
*  be no such algorithm. On the other hand, I can use exactly the same logic and I can say, well,
*  P must be equal to NP because there are so many smart people out here who have been trying to
*  prove it unequal to NP, and they've all failed. This kind of reminds me of the discussion about
*  the search for aliens. They've been trying to look for them, and we haven't found them yet,
*  therefore they don't exist. But you can show that there's so many planets out there that they very
*  possibly could exist. Then there's also the possibility that they exist, but they all
*  discovered machine learning or something and then blew each other up.
*  On that small, quick tangent, let me ask, do you think there's intelligent life out there in the
*  universe? I have no idea. Do you hope so? Do you think about it? I don't spend my time thinking
*  about things that I could never know, really. And yet you do enjoy the fact that there are as
*  many things you don't know. You do enjoy the mystery of things. I enjoy the fact that I have
*  limits, yeah, but I don't take time to answer unsolvable questions. Got it.
*  Well, because you've taken on some tough questions that may seem unsolvable. You have taken on some
*  tough questions that may seem unsolvable. It gives me a thrill when I can get
*  further than I ever thought I could. But much like with religion, these...
*  I'm glad that there's no proof that God exists or not. I mean, I think...
*  It would spoil the mystery.
*  It would be too dull, yeah.
*  So to quickly talk about the other art of artificial intelligence,
*  what's your view? Artificial intelligence community has developed as part of computer
*  science and in parallel with computer science since the 60s. What's your view of the AI community
*  from the 60s to now? So all the way through it was the people who were inspired by trying to
*  mimic intelligence or to do things that were somehow the greatest achievements of intelligence
*  that had been inspiration to people who have pushed the envelope of computer science
*  maybe more than any other group of people. So all the way through it's been a great source of
*  of good problems to sink teeth into and getting partial answers and then more and more
*  successful answers over the years. So this has been the inspiration for lots of the great
*  discoveries of computer science. Are you yourself captivated by the possibility of creating
*  of algorithms having echoes of intelligence in them?
*  Not as much as most of the people in the field, I guess I would say, but that's not to say that
*  they're wrong or that it's just you asked about my own personal preferences. But the thing that I
*  worry about is when people start believing that they've actually succeeded.
*  Because it seems to me that there's a huge gap between really understanding something
*  and being able to pretend to understand something and give the illusion of understanding something.
*  Do you think it's possible to create without understanding?
*  Yeah. I do that all the time too. I mean that's why I use random numbers.
*  But there's still this great gap. I don't assert that it's impossible, but I don't see anything
*  coming any closer to really the kind of stuff that I would consider intelligence.
*  You've mentioned something that on that line of thinking, which I very much agree with. So the
*  art of computer programming as the book is focused on single processor algorithms
*  and for the most part. You mentioned...
*  That's only because I set the table of contents in 1962. You have to remember.
*  For sure. There's no...
*  I'm glad I didn't wait until 1965.
*  One book, maybe we'll touch on the Bible, but one book can't always cover the entirety of everything.
*  So I'm glad the table of contents for the art of computer programming is what it is.
*  But you did mention that you thought that an understanding of the way ant colonies are able
*  to perform incredibly organized tasks might well be the key to understanding human cognition. So
*  these fundamentally distributed systems. So what do you think is the difference between the way
*  Don Knuth would sort a list and an ant colony would sort a list or perform an algorithm?
*  Sorting a list isn't the same as cognition though, but I know what you're getting at.
*  Well, the advantage of ant colony, at least we can see what they're doing. We know which
*  ant has talked to which other ant and it's much harder with brains to know to what extent
*  of neurons are passing signal. So I'm just saying that ant colony might be,
*  if they have the secret of cognition, think of an ant colony as a cognitive single being rather
*  than as a colony of lots of different ants. I mean, just like the cells of our brain and
*  the microbiome and all that is interacting entities, but somehow I consider myself to be
*  a single person. Well, you know, an ant colony, you can say might be cognitive somehow.
*  It's some sort of abstraction.
*  Yeah. I mean, you know, okay, I smash a certain ant and the organism thinks,
*  that stung, what was that? But if we're going to crack the secret of cognition, it might be that
*  we could do so by psyching out how ants do it because we have a better chance to measure
*  communicating by pheromones and by touching each other and sight, but not by much more subtle
*  phenomenon like electric currents going through. But even a simpler version of that, what are your
*  thoughts of maybe Conway's game of life? Okay. So Conway's game of life is able to simulate any
*  computable process and any deterministic process is like how you went there. I mean,
*  that's not its most powerful thing. I would say, I mean,
*  I mean, it can simulate it, but the magic is that the individual units are distributed.
*  Yes.
*  And extremely simple.
*  Yes. We understand exactly what the primitives are.
*  The primitives, just like with the ant colony, even simpler though.
*  But if we, but still it doesn't say that I understand, I understand life. I mean, I understand,
*  but it gives me a better insight into what does it mean to have a deterministic universe?
*  What does it mean to have free choice, for example?
*  Do you think God plays dice?
*  Yes. I don't see any reason why God should be forbidden from using the most efficient
*  ways to, I mean, we know that dice are extremely important in inefficient algorithms. There are
*  things that couldn't be done well without randomness. And so I don't see any reason why
*  God should be prohibited from-
*  When the algorithm requires it, you don't see why the physics should constrain it.
*  So in 2001, you gave a series of lectures at MIT about religion and science.
*  No, that was 1999.
*  But you published-
*  The book came out in 2001.
*  So in 1999, you spent a little bit of time in Boston enough to give those lectures.
*  Yeah.
*  And I read the 2001 version, most of it. It's quite fascinating to read. I recommend people,
*  it's transcription of your lectures. So what did you learn about how ideas get started and grow from
*  studying the history of the Bible? So you've rigorously studied a very particular part of the
*  Bible. What did you learn from this process about the way us human beings as a society
*  develop and grow ideas, share ideas, and identify with those ideas?
*  Share ideas and identify with those ideas.
*  Yeah. Well, it's hard to summarize that. I wouldn't say that I learned a great deal of
*  really definite things where I could make conclusions, but I learned more about what I don't know.
*  You have a complex subject, which is really beyond human understanding. So we give up on saying,
*  I'm never going to get to the end of the road and I'm never going to understand it. But you say,
*  but maybe it might be good for me to get closer and closer and learn more and more about something.
*  How can I do that efficiently? And the answer is, well, use randomness.
*  And so try a random subset that is within my grasp and study that in detail instead of just
*  studying parts that somebody tells me to study or instead of studying nothing because it's too hard.
*  So I decided for my own amusement once that I would take a subset of the verses of the Bible
*  and I would try to find out what the best thinkers have said about that small subset.
*  And I had about, let's say, 60 verses out of 3,000, I think it's one out of 500 or something like
*  this. And so then I went to the libraries, which are well-indexed. I spent, for example,
*  at Boston Public Library, I would go once a week for a year. And I went to have a dozen times to
*  hand over Harvard Library to look at this book that weren't in the Boston Public.
*  Where scholars had looked at and you can go down the shelves and you can look in the index and say,
*  oh, is this verse mentioned anywhere in this book? If so, look at page 105. So in other words,
*  I could learn not only about the Bible, but about the secondary literature about the Bible,
*  the things that scholars have written about it. And so that gave me a way to
*  zoom in on parts of the thing so that I could get more insight. And so I look at it as a way of
*  giving me some firm pegs, which I could hang pieces of information, but not as
*  things where I would say, and therefore this is true.
*  In this random approach of sampling the Bible, what did you learn about the most, you know,
*  central, one of the biggest accumulation of ideas in our…
*  It seemed to me that the main thrust was not the one that most people think of as saying, you know,
*  oh, don't have sex or something like this. But the main thrust was to try to figure out
*  how to live in harmony with God's wishes. I'm assuming that God exists and as I say, I'm glad
*  that there's no way to prove this because I would run through the proof once and then I'd forget it
*  and I would never speculate about spiritual things and mysteries otherwise and I think my life would
*  be very incomplete. So I'm assuming that God exists, but a lot of the people say God doesn't
*  exist, but that's still important to them. And so in a way that might still be whether God is there
*  or not in some sense, God is important to them. One of the verses I studied, you can interpret it
*  as saying, it's much better to be an atheist than not to care at all.
*  So I would say it's similar to the P equals NP discussion. You mentioned a mental exercise
*  that I'd love it if you could partake in yourself, a mental exercise of being God.
*  If you were God, Don Knuth, how would you present yourself to the people of Earth?
*  You mentioned your love of literature and there's this book that really I can recommend to you.
*  The title I think is Blasphemy. It talks about God revealing himself through a computer in
*  in Los Alamos. It's the only book that I've ever read where
*  the punchline was really the very last word of the book and explained the whole idea of the book.
*  And so I don't want to give that away, but it's really very much about this question that you
*  raised. But suppose God said, okay, my previous means of communication with the world
*  are not the best for the 21st century, so what should I do now? And it's conceivable
*  that God would choose the way that's described in this book.
*  Another way to look at this exercise is looking at the human mind,
*  looking at the human spirit, the human life in a systematic way.
*  I think it mostly you want to learn humility. You want to realize that once we solve one problem,
*  that doesn't mean that all of a sudden other problems are going to drop out. And we have to
*  realize that there are things beyond our ability. I see hubris all around.
*  Yeah, well said. If you were to run program analysis on your own life,
*  how did you do in terms of correctness, running time, resource use, asymptotically speaking,
*  Okay, yeah, well, I would say that question has not been asked me before.
*  I started out with library subroutines and learning how to be an automaton that was obedient.
*  And I had the great advantage that I didn't have anybody to blame for my failures. If I started
*  getting not understanding something, I knew that I should stop playing ping pong. And it was my
*  fault that I was I wasn't studying hard enough or something rather than that somebody was
*  discriminating against me in some way. And I don't know how to avoid the existence of biases
*  in the world. But I know that that's an extra burden that I didn't have to suffer from.
*  And then I found from parents, I learned the idea of service to other people as being more
*  important than what I get out of stuff myself. I know that I need to be happy enough in order
*  to be able to be of service. But I came to a philosophy for finally that I phrase as
*  point eight is enough. There was a TV show once called eight is enough, which was about
*  you know, somebody had eight kids. But I say point eight is enough, which means
*  if I can have a way of rating happiness, I think it's good design that
*  to have an organism that's happy about 80% of the time. And if it was 100% of the time,
*  it would be like everybody's on drugs and never and everything collapses, nothing works,
*  because everybody's just too happy. Do you think you've achieved that point eight optimal?
*  There are times when I when I'm down and I, you know, and I mean, I know that I'm chemically
*  that I know that I've actually been programmed to be to be depressed a certain amount of time.
*  And if that gets out of kilter, and I'm more depressed than you know, sometimes I,
*  I find myself trying to think now, who should I be mad at today? There must be a reason why I'm
*  but I but then I realized, you know, it's just my it's just my chemistry telling me that I'm
*  supposed to be mad at somebody. And so I try to say, Okay, go to sleep and get better. But,
*  but if I'm, but if I'm not 100% happy, that doesn't mean that I should find somebody that
*  screaming and and and try to silence them. But I but I'm saying, you know, okay, I'm not 100%
*  happy. But but I'm happy enough to be to be a part of a sustainable situation. So, so that's
*  kind of the the numerical analysis I do. You've converged towards the optimal, which human life
*  is a point eight. Yeah, I hope it's okay to talk about, as you talked about previously, in 2006,
*  you were diagnosed with prostate cancer. Has that encounter with mortality changed you in some way
*  or the way you see the world? Yeah, it did. The first encounter with mortality was my when my
*  dad died, and I, I went through a month when I sort of came to
*  be comfortable with the fact that I was going to die someday. And during that month, I don't know,
*  I, I felt okay, but I couldn't sing. And, you know, and I, and I couldn't do original
*  research either. I can, I sort of remember, after three or four weeks, the first time I started
*  having a technical thought that made sense and was maybe slightly creative, I could sort of feel
*  that out that that something was starting to move again. But that was, you know, so I felt very empty
*  for until I came to grips with the I learned that this is sort of a standard grief process that
*  people go through. Okay, so then now I'm at a point in my life, even more so than in 2006,
*  where, where all of my goals have been fulfilled, except for finishing the art of computer programming.
*  I, I had one major unfulfilled goal, I'd wanted all my life to write a piece of
*  a piece of music that, and I had an idea for, for a certain kind of music that I thought
*  ought to be written, at least somebody ought to try to do it. And I, and I felt that it was
*  that it wasn't going to be easy, but I wanted to, I wanted it to be proof of concept, I wanted to
*  know if it was going to work or not. And so I spent a lot of time. And finally, I finished that
*  piece. And we had the, we had the world premiere last year on my 80th birthday, and we had another
*  premiere in Canada, and there's talk of concerts in Europe and various things. So that, but that's
*  done. It's part of the world's music now. And it's either good or bad. But I did what I was hoping to
*  do. So the only thing that I, that I have on my agenda is to, is to try to do as well as I can
*  with the art of computer programming until I go see now. Do you think there's a element of 0.8
*  that might apply there? 0.8? Yeah. Well, I look at it more that I got actually to 1.0
*  with when that concert was over with. I mean, I, you know, I, so in 2006, I was at 0.8.
*  So when I was diagnosed with prostate cancer, then I said, okay, well, maybe this is, you know,
*  I've had all kinds of good luck all my life, and there's no, I have nothing to complain about.
*  So I might die now. And we'll see what happens. And so, so it's quite seriously, I went and I
*  didn't, I had no expectation that I deserved better. I didn't make any plans for the future.
*  I had my surgery, I came out of the surgery, and, and spent some time learning how to walk
*  again and so on. It was painful for a while. But I got home and I realized I hadn't really
*  thought about what to do next. I hadn't, I hadn't any expectation. You know, I said, okay,
*  hey, I'm still alive. Okay, now I can write some more books. But I didn't come with the attitude
*  that, you know, this was, this was terribly unfair. And, and I just said, okay, I was accepting
*  whatever turned out, you know, I got, I got more than my share already. So why should I?
*  And I didn't, and I really, when I got home, I realized that I had really not thought about the
*  next step, what I would do after I would, after I would be able to work again, I had sort of
*  thought of it as if, as this might, you know, I was comfortable with, with the fact that it was at
*  the end. But I was hoping that I would still, you know, be able to
*  learn about satisfiability and, and also someday even write music. I didn't start,
*  I didn't start seriously on the music project until 2012.
*  So I'm going to be in huge trouble if I don't talk to you about this.
*  In the 70s, you've created the tech typesetting system together with Metafont language for font
*  description and computer modern family of typefaces. That has basically defined the
*  methodology and the aesthetic of the countless research fields, right? Math, physics,
*  well, beyond computer science, so on. Okay. Well, first of all, thank you.
*  I think I speak for a lot of people in saying that, but a question in terms of beauty,
*  there's a beauty to typography that you've created and yet beauty is hard to quantify.
*  Right. How does one create beautiful letters and beautiful equations? Like what, what, what?
*  So, and perhaps there's no words to be describing,
*  to be describing the process, but.
*  So the great Harvard mathematician, George D. Bergoff, wrote a book in the 30s called
*  Aesthetic Measure, where he, where he would have pictures of vases and underneath would be a number.
*  And this was how beautiful the vase was. And he had a formula for this. And, and he actually,
*  also wrote about music. And so he could, he, he, he could, you know, so I thought maybe I would,
*  part of my musical composition, I would try to program his algorithms and, and, you know,
*  so that I would, I would write something that had the highest number by his score. Well, it wasn't
*  quite rigorous enough for, for a computer to, to do, but anyway, people have tried to,
*  to put numerical value on beauty. But, and, and he, he did probably the most serious attempt. And,
*  and George Gershwin's teacher also wrote two volumes where he talked about his method of,
*  of composing music. But you're talking about another kind of beauty and beauty in letters and
*  elegance and whatever that curvature is.
*  Right. So, so, and so that's, and yeah, I, the beholder, as they say, but
*  striving for excellence in whatever definition you want to give to beauty, then you try to
*  get as close to that as you can somehow with it.
*  I guess, I guess I'm trying to ask, and there may not be a good answer.
*  What loose definitions were you operating under with the community of people that you're working
*  on? Oh, the loose definition, I wanted, I wanted it to appeal to me, to me.
*  You personally. Yeah.
*  That's a good start. Yeah. No, and it failed that test when I got,
*  volume two came out with this, with the new printing and I was expecting it to be the
*  happiest day of my life. And, and I, I felt like a burning, like how angry I was that I opened the
*  book and it was in the same beige covers and, and, but, but it didn't look right on the page.
*  The number two was particularly ugly. I couldn't stand any page that had a two in his page number.
*  And I was expecting that it was, you know, I spent all this time making measurements and I,
*  and I had looked at stuff in different ways and I had, I had great technology, but,
*  but it didn't, you know, but I, but I wasn't done. I had, I had to retune the whole thing
*  after 1961. Has it ever made you happy finally?
*  Oh, oh yes. Or is it a point eight?
*  Oh, no, and so many books have come out that would never have been written without this.
*  I just, it just, it's just, it's a joy, but I can, but now I, I mean, all these pages that are sitting
*  up there, I, I, I don't have a, if I didn't like them, I would change them. That's my,
*  nobody else has this ability. They have to stick with what I gave them.
*  Yeah. So in terms of the other side of it, there's the typography. So the look of the,
*  of the type and the curves and the lines. What about the spacing?
*  What about the?
*  The spacing between the white space.
*  It seems like you could be a little bit more systematic about the layout or
*  technical.
*  Oh yeah. You can always go further. I, I, I, I didn't, I didn't stop at point eight. I stopped
*  at about 0.98. It seems like you're not following your own rule for happiness or is.
*  No, no, no. I, there's okay. The question is this, what is the Japanese word? Wabi-sabi or
*  something where, where the most beautiful works of art are those that have flaws because then the
*  person who, who perceives them as their own appreciation and that gives the viewer more
*  satisfaction or so on. But, but I, but no, no, with typography, I wanted it to look as good as I
*  could in the vast majority of cases. And then when it doesn't, then I, I say, okay, that's 2% more
*  work for the, for the author. But, but I didn't want to, I, I didn't want to say that my job was
*  to get 200% with and take all the work away from the author. That's what I meant by that.
*  So if you were to venture a guess, how much of the nature of reality
*  do you think we humans understand? So you mentioned you appreciate mystery.
*  How much of the world about us is shrouded in mystery? Are we, are we, if you were to put a
*  number on it, what, what percent of it all do we understand? Are we totally-
*  How many leading zeros do you point 0.00? I don't know. No, I think it's infinitesimal.
*  How do we think about that? And what do we do about that? Do we continue one step at a time?
*  Yeah, we muddle through. I mean, we do our best. We realize that nobody's perfect. And we,
*  and we try to keep advancing, but we don't spend time saying, we're not there. We're not all the
*  way to the end. Some mathematicians that, that would be in the office next to me when I was
*  in the math department, they would never think about anything smaller than countable infinity.
*  And I never, you know, we intersected that countable infinity because I rarely got up
*  to countable infinity. I was always talking about finite stuff. But even limiting to finite stuff,
*  which is, which is, which the universe might be, there's no way to really know whether the
*  universe is, isn't, isn't just made out of capital N, whatever units you want to call them, quarks
*  or whatever, where capital N is some finite number. All of the numbers that are comprehensible
*  are still way smaller than most, almost all finite numbers. I got this one paper
*  called supernatural numbers, where I, what, what, I guess you probably ran into something
*  called Knuth arrow notation. Did you ever run into that where, or anyway, so you take the number,
*  I think it's like, I, and I called it super K, I named it after myself, but it's, it's,
*  but in arrow notation is something like 10 and then four arrows and a three or something like that.
*  Okay. Now the arrow notation, if you have, if you have no arrows, that means multiplication,
*  X, Y means X times X times X times X, Y times. If you have one arrow, that means exponentiation.
*  So X one arrow, Y means X to the X to the X to the X to the X, Y times. So I found out by the way that
*  this notation was invented by a guy in 1830 and, and he was, he was a, a,
*  one of the English nobility who, who spent his time thinking about stuff like this.
*  And, and it was exactly the same concept that I, that I, that I used arrows and he used a slightly
*  different notation. But anyway, this, and then this Ackerman's function is, is based on the same kind
*  of ideas, but Ackerman was 1920s. But anyway, you've got this number 10 quadruple arrow three. So,
*  so that's, that says, well, we take, you know, we take 10 to the 10 to the 10 to the 10 to the 10th
*  and how many times do we do that? Oh, 10 double arrow two times or something. I mean, how tall is
*  that stack? But, but, but then we do that again, because that was only 10 triple or quadruple or
*  two. We take quadruple arrow three. It gets way beyond comprehension. Okay. And, and, and so,
*  but it's so small compared to what finite numbers really are, because I want to using four arrows and,
*  you know, a 10 and a three, I mean, let's have that, let's have that many number arrows. I mean,
*  the boundary between infinite and finite is incomprehensible for us humans anyway.
*  Infinity is a good, is a useful way for us to think about extremely large, extremely large things.
*  And, and, and, and we can, we can manipulate it, but, but we can never know that the universe is
*  actually anywhere near that. So, it just, so I realize how little we know. But, but, but we,
*  we found an awful lot of, of, of things that are too hard for any one person to know even with,
*  even in our small universe. Yeah. And we did pretty good. So, when you go up to heaven and meet God
*  and get to ask one question that would get answered, what question would you ask?
*  What kind of browser do you have up here?
*  No, I actually, I don't think it's meaningful to ask this question, but,
*  but I certainly hope we had good internet.
*  Okay. On that note, that's, that's a, that's beautiful actually. Don, thank you so much.
*  It was a huge honor to talk to you. I really appreciate it.
*  Well, thanks for the gamut of questions.
*  Yeah, it was fun.
*  Thanks for listening to this conversation with Donald Knuth. And thank you to our presenting
*  sponsor, Cash App. Download it, use Code Lex podcast, you'll get $10 and $10 will go to first,
*  a STEM education nonprofit that inspires hundreds of thousands of young minds to learn
*  and to dream of engineering our future. If you enjoy this podcast, subscribe on YouTube,
*  give it five stars on Apple podcasts, support on Patreon, or connect with me on Twitter.
*  And now let me leave you with some words of wisdom from Donald Knuth.
*  We should continually be striving to transform every art into a science.
*  And in the process, we advance the art. Thank you for listening and hope to see you next time.
