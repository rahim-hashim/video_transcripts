---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 8487s
Video Keywords: ['acm turing award', 'agi', 'ai', 'ai podcast', 'algorithms', 'artificial intelligence', 'artificial intelligence podcast', 'computer programming', 'computer science', 'donald knuth', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'literate programming', 'mathematics', 'mit ai', 'open source', 'stanford', 'tex']
Video Views: 225000
Video Rating: None
---

# Donald Knuth: Programming, Algorithms, Hard Problems & the Game of Life | Lex Fridman Podcast #219
**Lex Fridman:** [September 09, 2021](https://www.youtube.com/watch?v=EE1R8FYUJm0)
*  The following is a conversation with Donald Knuth, his second time on this podcast.
*  Don is a legendary computer scientist, touring award winner, father of algorithm analysis,
*  author of the art of computer programming, creator of tech that led to late tech,
*  and one of the kindest and most fascinating human beings I've ever got a chance to talk to.
*  I wrote him a letter a long time ago.
*  He responded.
*  And the rest, as they say, is history.
*  We've interacted many times since then, and every time has been joyful and inspiring.
*  To support this podcast, please check out our sponsors in the description.
*  This is the Lex Friedman podcast, and here is my conversation with Donald Knuth.
*  Your first large-scale program.
*  You wrote it in IBM 650 assembler in the summer of 1957.
*  I wrote it in decimal machine language.
*  I didn't know about assembler until a year later.
*  But the year 1957, and the program was Tic-Tac-Toe.
*  Yeah, I might have learned about assembler later that summer.
*  I probably did.
*  In 1957, hardly anybody had heard of assemblers.
*  You looked at the user manuals.
*  How would you write a program for this machine?
*  It would say, you know, you would say 69, which meant load the distributor,
*  and then you would give the address of the number you wanted to load into the distributor.
*  Yesterday, my friend Doug Spicer at the Computer History Museum sent me a link to something that just went on YouTube.
*  It was the IBM's progress report from 1956, which is very contemporary with 1957.
*  And in 1956, IBM had donated to Stanford University an IBM 650, one of the first ones.
*  When they showed a picture of the assembly line for IBM 650s, and they said, you know,
*  this is number 500 or something coming off the assembly line.
*  And I had never seen so many IBM 650s, except I did in this movie that was on YouTube now.
*  And it showed the picture from Stanford.
*  They said, look, we donated one of these to Stanford, one to MIT, and they mentioned one other college.
*  And in December of 56, they donated to my university, K-STEC.
*  But anyway, they showed a picture then of a class session where a guy was teaching programming.
*  And on the blackboard, it said 69, 8,000.
*  I mean, he was teaching them how to write code for this IBM 650, which was in decimal numbers.
*  So the instructions were 10 decimal digits.
*  You had two digits that said what to do, four digits to say what to do it to,
*  and four more digits to say where to get your next instruction.
*  And there's a manual that describes what each of the numbers mean.
*  And the manual was actually one.
*  If the manual had been well written, I probably never would have gone into computer science,
*  but it was so badly written, I figured that I must have a talent for it because I'm only a freshman
*  and I could write a better manual.
*  And so I started working at the computer center.
*  And wrote some manuals then.
*  But this was the way we did it.
*  And my first program then was June of 1957.
*  The Tic-Tac-Toe.
*  No, that was the second program.
*  The third program.
*  The first program was factoring a number.
*  So you dial a number on the switches.
*  I mean, you sat at this big mainframe and you turn the dials and set a number.
*  And then it would punch out the factors of that number on cards.
*  So that's the input is the number?
*  The input was, yeah, the input was a number, a tendinium number.
*  And the output was its factors.
*  And I wrote that program.
*  I still have a copy of it somewhere.
*  How many lines of code do you remember?
*  Well, yeah, it started out as about 20, but then I kept having me debug it.
*  I discovered debugging, of course, when I wrote my first program.
*  What does debugging look like on a program with just all numbers?
*  Well, you sit there and you, I don't remember how I got it into the machine,
*  but I think there was a way to punch it on card.
*  So each instruction would be one card.
*  Maybe I could get seven instructions on a card, eight instructions, I don't know.
*  But anyway, so I'm sitting there at the console of the machine.
*  I mean, I'm doing this at night when nobody else is around.
*  Of course.
*  And so you have one set of switches where you dial the number I'm inputting,
*  but there's another switch that says, okay, now execute one instruction and show me what you did.
*  Or you could put another four switches and say, stop if you get to that instruction.
*  So I can say, now go until you get there again and watch.
*  So I could watch, it would take that number and it would divide it by two.
*  And if there's no remainder, then okay, two is a factor.
*  So then I work on it.
*  But if not divisible by two, divide by three.
*  Keep trying until you know you're at the end.
*  And you would find a bug if you were just surprised that something weird happened?
*  Well, certainly.
*  I mean, first of all, I might have tried to divide by one instead of two.
*  Off by one error, people make all the time.
*  But maybe I go to the wrong instruction.
*  Maybe I left something in a register that I shouldn't have done.
*  But the first bugs were pretty, you know, I probably on the first night I was able to get the factors of 30,
*  you know, as equal to two, three and five.
*  Okay.
*  So you're sorry to interrupt.
*  You're sitting there late at night.
*  Yeah.
*  So it feels like you spent many years late at night working on a computer.
*  Oh, yeah.
*  So what's that like?
*  So most the world is sleeping and you have to be there at night because that's when you get access to the computer.
*  Between my freshman sophomore year, I didn't need sleep.
*  I used to do all nighters.
*  When I was in high school, I used to do the whole student newspaper every Monday night.
*  You know, I would just stay up all night and it would be done on Tuesday morning.
*  That was because I didn't get ulcers and stuff like that until later.
*  You know, but but but well, the I don't know if you know Rodney Brooks, Rod Brooks, of course.
*  Yeah, he he told he told me a story that he really you're you know, he really looked up to you.
*  He was actually afraid of you.
*  Well, vice versa.
*  But he tells a story when you are working on tech that they screwed up something with a machine.
*  I think this might have been MIT.
*  I don't know.
*  And you were waiting for them to fix the machine so you can get back to work late at night.
*  Oh, that happened all the time.
*  He was really intimidated.
*  He's like Dr. Newth is not happy with this.
*  Oh, that's interesting.
*  But no, the the machine at Stanford AI lab was was down an awful lot because we they had they had many talented programmers changing the operating system every day.
*  So the operating system was getting better every day, but it was also crashing.
*  So so so I wrote almost the entire manual for tech during downtime of that machine.
*  But that's another story.
*  Well, he was saying they it's a hardware problem.
*  They they they tried to fix it.
*  They reinserted something and smoke was everywhere.
*  Oh, wow. He was.
*  Oh, that didn't happen as often as the operating system.
*  But yeah, there was.
*  Anyways, it's a funny story because you're saying there's this tall Don Knuth that I look up to and I see and there was pressure to fix the computer.
*  Well, it's funny.
*  OK, the kind of things we remember that stick in our memory.
*  Well, OK. Yeah.
*  Well, I can tell you a bunch of Rodbroke stories, too.
*  But let's let's let's go back to the 50.
*  So so so I'm debugging this my first program and I I had more bugs in it than number of lines of code.
*  I mean, the number of lines of code kept growing.
*  And let me explain.
*  So I had to punch the answers on cards.
*  All right. So suppose I suppose I'm factoring the number 30, then I got then I got to I got to put two somewhere on the card.
*  I got to put a three somewhere on the card.
*  I got to put a five somewhere on the card.
*  Right. And and you know what?
*  But it was my first program.
*  I probably screwed up and, you know, it fell off the edge of the card or something like that.
*  But but I didn't realize that there are some tend to do numbers that have that have more than eight factors.
*  And the card has only 80 columns.
*  And so I need 10 columns for every factor.
*  So my first program didn't take account for the fact that I would have to punch more than one card.
*  My first program, you know, just line the stuff up in memory and then I punched the card.
*  But but after, you know, by the time I finished, I had to I had to deal with lots of lots of things.
*  Also, I if you if you put a large prime number in there, my program might have sat there for 10 minutes.
*  The 650 was pretty slow.
*  And so it would sit there spinning its wheels and you wouldn't know if it was in a loop or whatever.
*  You said 10 digit is 10 digits.
*  Yeah. So I think the largest is sort of 9999999997 or something like that.
*  That would you know, that would take me a while for that first.
*  Anyway, that was my first program.
*  Well, what was your goal with that program?
*  My goal you were hoping to find a large prime maybe or no.
*  The opposite.
*  No, my goal is to see the lights flashing and understand how this magical machine would be able to do something that took so long by hand.
*  So what was your second program?
*  My second program was was a converted number from from binary to decimal or something like that.
*  It was much simpler.
*  It didn't have that many bugs in it.
*  My third program was Tic Tac Toe.
*  Yeah. And he had some.
*  So the Tic Tac Toe program is interesting on many levels, but one of them is that it had some you can call machine learning in it.
*  That's yeah, that's right.
*  I don't know how long it's going to be before the name of our field has changed from computer science to machine learning.
*  But but anyway, it was my first experience with machine learning.
*  OK, so here we had.
*  Yeah, how does the program?
*  Well, first of all, what is the problem you were solving?
*  What is Tic Tac Toe?
*  What are we talking about?
*  And then what how was it designed?
*  Right. So you got a three by three grid and each each each could be in three states.
*  It can be empty or it can have an X or an O.
*  Yeah. Right. So three to the ninth is a well, what is how big is it?
*  I should know. But it's 80.
*  Eighty one times, 81 times three.
*  So anyway, eight is like two to the third.
*  And so that would be that would be like two to the sixth.
*  And then but that would be 64.
*  Then you have to anyway.
*  I love how you're doing the calculation.
*  So the three lot of anyway, the three comes from the fact that it's either empty.
*  And X or an O. Right.
*  And the 650, what was it was a machine that had only two thousand.
*  Ten digit words go from zero zero zero zero to one nine nine nine, and that's it.
*  And and each word you have a ten digit number.
*  So that's not many bits.
*  I mean, I got to have three in order to have a memory of every position I've seen.
*  I need three to the ninth bits.
*  OK, but it was a decimal machine, too.
*  It didn't have bits, but it did have it did have strange instruction where if you had a ten
*  digit number, but all the digits were either eight or nine, you'd be eight, nine, nine, eight,
*  something like that.
*  That would you can make a test whether it was eight or nine.
*  That was one of the strange things IBM engineers put into the machine.
*  I have no idea why.
*  Well, hardly ever used.
*  But anyway, I needed one digit for every every position I'd seen.
*  Zero meant it was a bad position.
*  Nine minute was good position.
*  I think I started out at five or six.
*  You know, but if you if you win a game, then you then you increase the value of that position
*  for you, but you decrease it for for your opponent.
*  So but I could I had that much total memory for every every possible position was one
*  digit and I had a total of twenty thousand digits, which had to which had to also include
*  my program and all the logic and everything including how to how to ask the user what the
*  moves are and things like this.
*  Okay, so so I think I had to work it out because every every position in tic-tac-toe is equivalent
*  to roughly eight others because you you can rotate the board which gives you a factor
*  four when you can also flip it over and that's another factor too.
*  So I might you know, so I might have needed only three to the ninth over eight positions
*  of you know, plus plus a little bit.
*  So I had but anyway, that was that was a part of the program to squeeze it into this tiny.
*  So you tried to find the inefficient representation that took account for that kind of rotation.
*  I had to otherwise I couldn't do the learning.
*  Wow.
*  So so but but I had three parts to my tic-tac-toe program and I call it brain one brain two
*  and brain three.
*  So brain one just played a see at random.
*  Okay, it's your turn.
*  Okay, you got to put an X somewhere.
*  It has to go in an empty space, but that's that's it.
*  Okay, choose choose one and play it brain two had a canned routine and I think it was
*  it also maybe it had maybe to assume you were the first player or maybe it allowed you to
*  be first.
*  I think you're allowed to be either first or second, but had a canned built-in strategy
*  known to be optimum for tic-tac-toe before I forget by the way, I learned
*  many years later that Charles Babbage had had planned to had thought about programming
*  tic-tac-toe for his for his dream machine that he that he would never be able to finish.
*  Wow.
*  So that was the program he thought about more than a hundred years ago.
*  Yeah, yeah.
*  He had he did that.
*  Okay, and I had but and I had however been influenced by a demonstration at the Museum
*  of Science and Industry in Chicago.
*  It's like it's like Boston's Science Museum.
*  I think Bell Labs had had prepared a special exhibit about telephones and relay technology
*  and they had a tic-tac-toe playing machine as part of that exhibit.
*  So that had been one of my you know, something I'd seen before I was a freshman in college
*  and inspired me to see if I could write a program for it.
*  Okay.
*  So anyway, I had brain one random, you know, knowing nothing brain to knowing everything
*  then brain three was the learning one and I could I could play brain one against brain
*  one brain one against brain two and so on and so you could also play against the user
*  against a live in person.
*  But but but so I started going the learning thing and I said, okay, you know, take two
*  random random people just playing tic-tac-toe knowing nothing and after about I forget the
*  number now, but but it converged after about 600 games to a safe draw.
*  The way my program learned was actually it learned how not to make mistakes because you
*  know how to it didn't try to do anything for winning.
*  Just try to say, you know, losing and not lose.
*  So that was probably because of the way I did I designed the learning thing.
*  I could have, you know, had a different reinforcement function that would that would reward brilliant
*  play.
*  But anyway, it didn't and and and if I if I took a novice against the skilled player,
*  it was able to learn how to play a good game.
*  So there was that and that was really Mike.
*  But after I finished that I felt I understood programming.
*  Was there a did you did a curiosity and interest in learning systems persist for you?
*  So why why did you want brain three to learn?
*  Yeah, I think naturally it's we're talking about Rod Brooks.
*  He was teaching all kinds of very small devices to to learn stuff.
*  If a leaf drops off of a tree, you know, he was saying something.
*  Well, it learns if there's wind or not.
*  But but but I mean he pushed that a little bit too far, but he said he could probably
*  train some little mini bugs to scour out dishes if he had enough financial support.
*  I don't know.
*  Can I can I ask you about that?
*  Because he also mentioned that during those years there was discussion about inspired
*  by touring about computation, you know of what is computation.
*  Yeah.
*  And I never thought about any stuff like that.
*  That was that was way too philosophical.
*  I mean, I was a I was a freshman after all.
*  I mean, I didn't I was pretty much a machine.
*  So it's almost like, yeah, I got you.
*  It's a tinkering mindset, not a philosophical mindset.
*  It was just exciting to me to be able to control something but not but not but not to say,
*  mmm, am I solving a big problem or something like that?
*  Or is this a step for humankind or no, no way?
*  When did you first start thinking about computation in the big sense?
*  You know, like the universal touring machine.
*  Well, I mean, I had to pass and I had to take I had to take classes.
*  Classes on computability when I was a senior.
*  So, you know, we read this book by Martin Davis and yeah, this is cool stuff.
*  But, you know, I learned about it because I know I needed to pass the exams.
*  But I didn't I didn't invent any of that boring stuff.
*  But I had great fun playing with the machine.
*  You know, I I wrote programs because it was fun to write programs and and and get this.
*  I mean, it was like watching miracles happen.
*  You mentioned in in an interview that when reading a program,
*  you can tell when the author of the program changed.
*  Oh, OK.
*  Well, how the heck can you do that?
*  Like what makes a distinct style for a programmer?
*  Do you think you know, there's different Hemingway has a style of writing?
*  This is James Joyce or something.
*  Well, those are pretty yeah, those are pretty easy to imitate.
*  But it's the same with music and whatever you can.
*  I found out during the pandemic, I spent a lot more time playing the piano
*  and I and I found something that I'd had.
*  I had it when I was taking lessons before I was a teenager.
*  And it was Yankee Doodle played in the style of you know,
*  and you had Beethoven and you had Debussy and Chopin and you know,
*  and the last one was Gershwin and and I played over and over again.
*  I thought it was so brilliant.
*  But but it was so easy.
*  But also to appreciate how this this author,
*  Mario somebody or other had had been able to reverse engineer the styles of those
*  composers. So but now particularly to your question, I mean, there would be
*  it was it was pretty obvious in this program.
*  I was reading it was it was a compiler and it had been written by a team at at Carnegie Mellon.
*  And I have no idea which program was responsible for but but you would get to a part
*  where the guy would just not know how to how to move things between registers very efficiently.
*  And so and so everything that could be done in one instruction would take three or
*  something like that. That would be a pretty obvious change in style.
*  But there were but there were also flashes of brilliance where you could do in one instruction.
*  Normally I used to because you knew enough about the way the machine worked that you could
*  that that you could accomplish two goals in one step.
*  So it was mostly the brilliance of the concept more than the semicolons and or the
*  use of short sentences versus long sentences or something like that.
*  So you would see the idea in the code and you see the the different style of thinking
*  Right. It was stylistic.
*  I mean I could identify authors by their by the amount of technical aptitude they had
*  but not by style in the sense of rhythm or something like that.
*  So if you think about Mozart Beethoven Bach if somebody looked at Don Knuth code would they be able to
*  tell that this is a distinct style thinking going on here.
*  What do you think?
*  And what would be the defining characteristic of the style?
*  Well my code now is it is literate programming.
*  So I'm it's a combination of English and C mostly.
*  But but but if you just looked at the C part of it you would also probably notice that I don't
*  you know that I use a lot of global variables that other people don't and I expand things in line more than
*  instead of calling anyway I have different subset of C that I use.
*  Okay but this that's a little bit stylistic.
*  But but with literate programming you alternate between English and and C or whatever.
*  And by the way people listening to this should look up literate programming.
*  It's very interesting concept that you that you proposed and developed over the years.
*  Yeah.
*  Yeah.
*  I'm that's the most significant thing I think to come out of the tech project is that I
*  realized that my programs were to be read by people and not just by computers and that
*  typography could massively enhance that.
*  And and so I mean it they're just wonder if they're going to look it up that they should also look up
*  this book by called Physically Based Rendering by Matt Farr and gosh anyway it got an Academy of
*  Award but it's but but but all the if all the graphic effects you see in movies like you know are
*  accomplished by algorithms in this book.
*  It is the whole book is a literate program.
*  It tells you not only how you do all the shading and and bring images in that you need for
*  animation and textures and so on but it also you can run the code and and and so I find it an extension
*  of the way I of how to teach programming is but by by telling a story as part of the program.
*  So it's it works as a program but it's also readable by humans.
*  Yes and especially by me.
*  Yeah a week later or a year later.
*  That's a good test.
*  If you yourself understand the code easily a week or a year later.
*  Yeah.
*  So it's a what's this place.
*  It's the greatest thing since sliced bread.
*  Programming or literate literate program.
*  Okay.
*  You heard it here first.
*  Okay.
*  You are dodged this question in an interview I listened to.
*  So let me ask you again here.
*  What makes for a beautiful program.
*  What makes for a beautiful program.
*  Yeah.
*  What are the characteristics you see like you just said literate programming.
*  What are the characteristics you see in a program that make you sit back and say that's pretty good.
*  Well the reason I didn't answer is because there are there are dozens and dozens of answers to that because because
*  each you can define beauty the same personally find beauty a different way from hour to hour.
*  I mean it depends on what I and what you're looking for at one level.
*  You it's beautiful just if it works at all another level.
*  It's beautiful if it's if it can be understood easily.
*  It's beautiful if it if it's a literate programming is beautiful.
*  It makes you laugh.
*  I mean yeah I'm actually so I'm with you.
*  I think beauty if it's readable readable.
*  Yeah.
*  Is if you understand what's going on and also understand the elegance of thought behind it and then also as you said wit and humor.
*  I was always I remember having this conversation.
*  I had this conversation on stack overflow.
*  Whether humor is good in comments and I think it is whether humor is good in comments like when you add comments code.
*  Yeah, I always thought a little bit of humor is good.
*  It shows personality.
*  It shows character shows wit and fun and all those kinds of things of the personality of the program.
*  Yeah.
*  Okay, so a couple days ago I received a wonderful present from my former editor at Aspen Wesley.
*  He he's downsizing his house and he found that somebody at the company had had found all the all of their internal files about the art of computer programming from the 1960s and they gave it to him.
*  And then before throwing throwing in the garbage and then so he said oh yeah he he planned to keep it for posterity.
*  But now he realized that posterity is too much for him to handle.
*  So he sent it to me.
*  And so and so I just received this big big stack of letters.
*  Some of which I had written to them but but many of which they had written to early guinea pigs who were telling them whether they should publish or not, you know, and one of the things was in the in the comments to volume one.
*  The major the major reader was was Bob Floyd.
*  Who is my great co-worker in the 60s died early, unfortunately, but but and and he he commented about the humor in it.
*  And so we had we ran it by me, you know, says, you know, keep this joke in or not, you know.
*  They also sent it out to focus group.
*  What do you think about humor in it in a book about computer program?
*  What's the conclusion?
*  And I stated my philosophy is it said, you know, the ideal thing is that it's it's it's something where the reader knows that there's probably a joke or if you only understood it and this is a motivation to understand to think about it a little bit.
*  But anyway, it's a very delicate humor is a bit.
*  I mean, it's it's really each each century invents different kind of humor, too.
*  I mean, different different cultures have different different kinds of humor.
*  Yeah, like we talked about Russia a little bit offline.
*  You know, there's dark humor and when a country goes to something different, that life and stuff like this.
*  You know, and Jack Benny, I mean, Steve Allen wrote this book about humor and it was the most boring book, but he was one of my idols.
*  But but yeah, it's called The Funny Men or something like that.
*  But yeah, OK. So anyway, I think it's important to know that that this is part of life and and it should be fun and not.
*  And so, you know, I wrote this this organ composition, which is based on the Bible, but I didn't refrain from putting little jokes in it.
*  It also in the music.
*  It's hidden in the music. It's it's it's there.
*  Yeah. A little humor is OK.
*  Yeah. I mean, not egregious humor.
*  So in this correspondence, you know, there were there were things I said, yeah, there was a little humor.
*  There were things I said, yeah, I really shouldn't have I really shouldn't have done that.
*  But but other ones, I insisted on and I've got jokes in there that that nobody has figured out yet.
*  In fact, in volume two, I've got a cryptogram, a message in Cypher.
*  And in order to decipher it, you're going to have to have to break an RSA key, which is larger than people know how to break.
*  So, you know, if computers keep getting faster and faster, then it might be 100 years, but somebody will figure out what this message is and they will laugh.
*  I mean, I've got a joke in there.
*  So that one, you really have to work for.
*  I don't know if you've heard about this.
*  Let me explain it. Maybe you'll find it interesting.
*  So OpenAI is a company that does AI work and they have this language model.
*  It's a neural network and can generate language pretty well.
*  But they also have on top of that, develop something called OpenAI Codex.
*  And together with GitHub, they develop a system called OpenAI Copilot.
*  Let me explain what it does.
*  There's echoes of literate programming in it.
*  So what you do is you start writing code and it completes the code for you.
*  So, for example, you start let's go to your factoring program.
*  You start you write in JavaScript and Python in any language that you're trained on.
*  You write the first line and some comments like what this code does and generates the function for you.
*  And it does an incredibly good job.
*  It's not provably right, but it often does a really good job of completing the code for you.
*  I see. But how do you know whether it did a good job or not?
*  You could see a lot of examples where it did a good job.
*  And so it's not a thing that generates code for you.
*  It starts it gives you a so it puts the human in the seat of fixing issues versus writing from scratch.
*  Do you find that kind of idea at all interesting?
*  Every year we're going to be losing more and more control over what machines are doing.
*  And people are saying, well, it seems to like when I was a professor at Caltech in the 60s,
*  we had this guy who talked a good game.
*  He could give inspiring lectures and you'd think, well,
*  thrilling things he was talking about an hour later.
*  You say, well, what did he say?
*  But he really felt that it didn't matter whether computers got the right answer or not.
*  It just matter whether it made you happy or not.
*  If your boss paid for it, then you had a job.
*  You could you could you could take care of your happiness is more important than truth.
*  Exactly. He didn't believe in truth, but he was a philosopher.
*  I like it. And somehow you see we're going that way.
*  I mean, so many more things are taken over by saying, well, this seems to work.
*  And so when there's when when there is competing interest involved,
*  neither side understands why the decision is being made.
*  You know, we realize now that it's that is bad.
*  But but consider what happens five to five or 10 years down the line when things get even more further detached.
*  And each thing is based on something from the previous year.
*  Yeah. So you start to lose the more you automate, the more you start to lose track of some deep human.
*  And exponentially, exponentially.
*  But so that's the dark side.
*  The positive side is the more you automate, the more you let humans do what humans do best.
*  So maybe programming this, you know, maybe humans should focus on a small part of programming that requires that genius.
*  The magic of the human mind and the mess you let the machine generate.
*  Yeah. I mean, that's the that's the positive.
*  But of course, it does come with the darkness of automation.
*  What's better? Correct.
*  I'm never going to try to write a book about that.
*  I'm never going to recommend to any of my students to work for them.
*  So you're on the side of I'm on the side.
*  I'm on the side of happiness.
*  I'm on the side of understanding.
*  And I think these things are really marvelous if they if if what they do is, you know, all of a sudden we have a better medical diagnosis or or you know,
*  it'll help guide some scientific experiment or something like this.
*  You know, so you know, curing diseases or whatever.
*  But but when it when it affects people's lives in a serious way,
*  so if you're writing if you're writing code for oh, yeah, here, this is great.
*  This will make a slaughter. But OK, so.
*  So I see. So you have to be very careful.
*  Like right now, it seems like fun and games.
*  It's useful to write a little JavaScript program that helps you with the website.
*  But like you said, one year passes, two years passes, five years and you forget you start building on top of it.
*  And then all of a sudden you have autonomous weapons systems based.
*  Well, we're all dead. Doesn't matter in that sense.
*  Well, in the end, this whole thing ends anyway.
*  So but it pays.
*  There is a heat death of the universe.
*  Yeah, I predict it.
*  But I'm trying to postpone that for for a little bit.
*  Well, it'd be nice that at the end, as we approach the heat death of the universe,
*  there's still some kind of consciousness there to to to to appreciate it.
*  Hopefully human consciousness.
*  I'll settle for 10 to the 10 to the 10 to the 10th year, some finite number.
*  But but things like this might be the reason we don't pick up any signals from extraterrestrial.
*  They don't want anything to do with us.
*  Oh, because they because they they they invented it, too.
*  So you do have a little bit of worry on the existential threats of A.I. and automation.
*  So like like removing the human from the picture, et cetera.
*  Yeah. People have more more potential to to do harm now than by far than they did a hundred years ago.
*  But are you optimistic about the humans are good at creating destructive things,
*  but also humans are good at solving problems?
*  Yeah, I mean, there's half empty and half full, you know, so.
*  So we have full.
*  I can go. So let me let me put it this way, because because it's the only way I can be optimistic.
*  But think of of of things that have changed because of civilization.
*  You know, they don't occur just in nature.
*  So just just imagine the room we're in, for example.
*  OK, some we've got pencils, we've got books, we've got tables, we've got microphones, clothing, food.
*  All these things were added.
*  Somebody invented them one by one and millions of things that we inherit.
*  OK. And it's inconceivable that that so many millions of billions of things wouldn't have problems.
*  And we get it all right.
*  And each one would have no negative effects and so on.
*  So it's very amazing that it much works as does work.
*  It's it's it's incredibly amazing.
*  And actually, that's the source of my optimism as well, including for artificial intelligence.
*  So we drive over bridges.
*  We we use all kinds of technology.
*  We don't know how it works.
*  And there's millions of brilliant people involved in building a small part of that.
*  And it doesn't go wrong. And it works.
*  And I mean that it works.
*  It doesn't go wrong often enough for us to suffer.
*  And we can identify things that aren't working and try to improve on them in a suboptimal way.
*  Oh, absolutely. But it's but the but the the kind of things that I know how to improve
*  require human beings to be rational.
*  And I'm losing my confidence that human beings are rational.
*  Yeah. Yeah. Now, here you go again with the worst case worst case analysis.
*  They may not be rational, but they're they're they're clever and beautiful in their own kind of way.
*  I tend to think that most people have the desire and the capacity to be good to each other.
*  And love will ultimately win out.
*  Like if they're given the opportunity, that's where they lean.
*  In the art of computer programming, you wrote, The real problem is that programmers have spent far too much time worrying about efficiency in the wrong places and at the wrong times.
*  Premature optimization is the root of all evil in parentheses, or at least most of it in programming.
*  Can you explain this idea? What's the wrong time?
*  What is the wrong place for optimization?
*  So, first of all, the word optimization, I started out writing software and optimization was I was a compiler writer.
*  So optimization meant making the making a better translation so that it would run faster on a machine.
*  So an optimized program is just like, you know, you you run a program and you set the optimization level for the compiler.
*  So that's one word for optimization.
*  And at that time, I happened to be looking in an unabridged dictionary for some reason or other, and I came to word optimizes.
*  So what's the meaning of the word optimized?
*  And it says to view with optimism.
*  And you look in Webster's dictionary of English language in 1960s, that's what optimized me meant.
*  OK. Now, so people started doing cost optimization, all the kinds of things, you know, whole subfields of algorithms and economics and whatever are based on what they call optimization now.
*  But to me, optimization, when I was saying that, was saying changing a program to make it more tuned to the machine.
*  And I found out that when a person writes a program, he or she tends to think that the parts that were hardest to write are going to be hardest for the computer to execute.
*  So maybe I have 10 pages of code, but I had to work a week writing this page.
*  I mentally think that when the computer gets to that page, it's going to slow down.
*  Right. It's because, oh, I don't understand what I'm doing.
*  I better be more careful.
*  Anyway, this is, of course, silly, but it's something that we that we that we don't know when we write a piece of code.
*  We don't know whether the computer is actually going to be executing that code very much.
*  So people had a very poor understanding of what the computer was actually doing.
*  I made one test where we studied a Fortran compiler and it was spending more than 80 percent of its time reading the comments card.
*  But as a programmer, we were really concerned about how fast it could take a complicated expression that had lots of levels of parentheses and convert that into something.
*  But that was just less than one percent of the.
*  So if we optimize that, we didn't know what we were doing.
*  But if we knew that it was spending 80 percent of his time on the comments card, you know, in 10 minutes we could we could make the compiler run more than twice as fast.
*  And you can only do that once you've completed the program and then you empirically study where I had some kind of profiling that I knew what was important.
*  So you don't think this applies generally?
*  I mean, there's something that rings true to this across all of that applied generally, but it was it was only my good luck.
*  I said it, but you know, but I did.
*  But I said it in limited context and I'm glad if it makes people think about stuff because I know.
*  But it applies in another sense, too.
*  That is, sometimes I will do optimization in a way that does help the actual running time, but makes the program impossible to change next week because I've changed my data structure or something that made it less adaptable.
*  So one of the great principles of computer science is it's laziness or whatever you call it, late binding.
*  You know, don't hold off decisions when you can.
*  And, you know, and we understand now quantitatively how valuable that is.
*  What do you mean we understand?
*  People have written thesis about how you can how late binding will improve the I mean, you know, just in time manufacturing or whatever you can make.
*  You can defer a decision instead of doing your advanced planning and say I'm going to allocate 30% to this and 50%.
*  So in all kinds of domains, there's an optimality to laziness in many cases.
*  Decision is not made in advance.
*  So instead you design in order to be flexible to change with the with the way the wind is blowing.
*  Yeah, but so the reason that line resonated with a lot of people is because there's something about the programmers mind that wants that enjoys optimization.
*  So it's a constant struggle to balance laziness and late binding with the desire to optimize the elegance of a well optimized code is something that's compelling to programming.
*  Yeah, it's another concept of beauty.
*  Let me ask you a weird question.
*  So Roger Penrose has talked about computation computers and he proposed that the way the human mind discovers mathematical ideas is something more than a computer that that universal Turing machine cannot do everything that a human mind can do.
*  Now this includes discovering mathematical ideas and it also includes he's written a book about it consciousness.
*  So I don't know if you know Roger, but my my daughter's kids played with his kids in Oxford.
*  Nice. So I'm going to ask you a question.
*  So do you think there is such a limit to the computer?
*  Do you think consciousness is more than a computation?
*  Do you think the human mind the way it thinks is more than a computation?
*  I mean, I can say yes or no, but but but I don't think I have no idea.
*  I mean, I think the human mind is more than a computation.
*  I mean, I can say yes or no, but but but I don't think I have no reason.
*  I mean, so you don't find it useful to have an intuition in one way or the other?
*  Like when you think about algorithms, do you?
*  Isn't it useful to think about the limits?
*  Unanswerable question in my opinion is is no better than anybody else.
*  You think it's unanswerable.
*  So you don't think eventually.
*  Angels condense on the head of a I mean, I don't know.
*  But angels are anyway, there are lots of things that are beyond that we can speculate about.
*  But I don't want somebody to say, oh, yeah, can you said this?
*  And so he's he's he's smart.
*  And so that must be I mean, I say it's something that we'll never know.
*  Interesting. OK, that's a strong statement.
*  I don't I personally think it's something we will know eventually.
*  Like there's no reason to me why the the workings of the human mind are not within the reach of science.
*  That's absolutely possible.
*  And I'm not denying it. Yeah.
*  But right now you don't have a good intuition.
*  I mean, that's also possible.
*  You know that an A.I. you know, created the universe, you know, intelligent design is all has all been done by an A.I.
*  Yes, this is I mean, all these things are.
*  But but but but you're asking me to to pronounce on it.
*  And I don't have any expertise.
*  I know I'm a teacher that passes on knowledge, but I don't but I don't know the fact that I that I vote yes or no on.
*  Well, you do have expertise as a human, not as a not as a teacher or a scholar of computer science.
*  I mean, that's ultimately the realm of where the discussion of human thought.
*  Yeah. Well, I know we're in consciousness.
*  I know where we're coming from.
*  He I'm sure he has no proof.
*  He might even thought he proved it, but no, he doesn't.
*  He doesn't prove it. He is following intuition.
*  But but I mean, you have to ask John McCarthy, John McCarthy, I think we're totally unimpressed by these statements.
*  So you don't think so, even like the touring paper on on the touring tests that, you know, starts by asking, can machines think?
*  Oh, you don't think these kind of touring doesn't like that question?
*  Yeah, I don't consider it important.
*  Let's just put it that way, because it's in the category of things that it would be nice to know.
*  But I think it's beyond knowledge.
*  And so I don't know.
*  I'm more interested in knowing about the Riemann hypothesis or something.
*  So when you say it's an interesting statement beyond knowledge.
*  Yeah, I think what you mean is it's not sufficiently well.
*  It's not even known well enough to be able to formalize it in order to ask a clear question.
*  Yeah. And so that's why it's beyond knowledge.
*  But that doesn't mean it's not eventually going to be formalized.
*  Yeah. Maybe consciousness will be understood some someday.
*  The last time I checked, it was still 200 years away.
*  I haven't been specializing in this by any means.
*  But but I went to lectures about it 20 years ago when I was there was there was a symposium at the American Academy in Cambridge.
*  And it started out by saying essentially everything that's been written about consciousness is is hogwash.
*  I tend to I tend to disagree with that a little bit.
*  So well, it's so consciousness for the longest time still is in the realm of philosophy.
*  So it's just conversations without any basis and understanding.
*  Still, I think once you start creating artificial intelligence systems that interact with humans and they have personality, they have identity, you start flirting with the question of consciousness, not from a philosophical perspective, but from an engineering perspective.
*  And then starts becoming much more like I feel like.
*  Yeah, don't misunderstand me. I certainly don't disagree with that at all.
*  And even at these lectures that we had 20 years ago, there were neurologists pointing out that human beings had actually decided to do something before they were conscious of making that decision.
*  Yeah.
*  I mean, they could tell that, you know, that signals were being sent to their arms before they before they knew that they were thinking like this are true.
*  And my, you know, Les Valiant has an architecture for the brain and more recently, Christos Papadimitriou in the Academy Science Proceedings a year ago with with two other people.
*  But I know Christos very well.
*  And he's got this model of this architecture by which you could create things that correlate well with experiments that are done on consciousness.
*  And he actually has a machine language in which you can write code and test hypotheses.
*  And so it might, you know, we might have a big breakthrough.
*  My personal feeling is that consciousness, the best model I've heard of to explain the miracle of consciousness is that somehow inside of our brains, we're having a continual survival for the fittest competition.
*  And I'm speaking to you, all the possible things I might be wanting to say are all in there.
*  There's like a voting going on.
*  Yeah, right. And one of them is winning. And that's affecting the next sentence and so on.
*  And there was this book, Machine Intelligence or something.
*  On intelligence?
*  On intelligence. Yeah. Bill Atkinson was a total devotee of that book.
*  Well, I like whether it's consciousness or something else, I like the storytelling part that we it feels like for us humans, it feels like there's a concrete story.
*  It's almost like literary programming.
*  I don't know what the programming going on on the inside, but I'm getting a nice story here about what happened.
*  And it feels like I'm in control and I'm getting a nice clear story.
*  But it's also possible there's a competition going on that's really messy.
*  There's a bunch of different competing ideas.
*  And in the end, it just kind of generates a story for you to a consistent story for you to believe.
*  And that makes it all nice.
*  Yeah. And so I prefer to talk about things that I have some expertise and then things which I which I'm only on the sideline.
*  So there's a tricky thing. I don't know if you have any expertise in this.
*  You might be a little bit on the sideline. Be interesting to ask, though.
*  What are your thoughts on cellular automata in the game of life?
*  Have you ever played with those kind of little games?
*  I think the game of life is wonderful and shows all kind of stuff about how things can evolve without the creator understanding anything more than the power of learning in a way.
*  But to me, the most important thing about the game of life is how it focused for me what it meant to have free will or not.
*  Because the game of life is obviously totally deterministic.
*  And I find it hard to believe that anybody who's ever had children cannot believe in free will.
*  On the other hand, this makes it crystal clear.
*  John Conway said he wondered whether it was immoral to shut the computer off after he got into a particularly interesting play of the game of life.
*  Wow. Yeah.
*  Yeah. So there is to me the reason I love the game of life is exactly as you said, a clear illustration that from simple initial conditions with simple rules, you know exactly how the system is operating is deterministic.
*  And yet, if you let yourself if you allow yourself to lose that knowledge a little bit enough to see the bigger organisms that emerge and then all of a sudden they seem conscious.
*  They seem not conscious, but living.
*  If the universe is finite, we're all living in the game of life to slow down.
*  I mean, it's sped up a lot.
*  Do you think technically some of the ideas that you used for analysis of algorithms can be used to analyze the game of life?
*  Can we make sense of it? Or is it too weird?
*  Yeah, I mean, I've got I've got a dozen exercises in volume for practical six that actually work rather well for that purpose.
*  Bill Gospers came up with the with the algorithm that allows that allowed Golly to to run thousands and thousands of times faster.
*  You know, the website called Golly and G-O-L-L-Y just simulates the cellular automata, a game of life.
*  Yeah, you got you got to check it out.
*  Can I ask you about John Conway?
*  Yes. In fact, I'm just reading now the the issue of mathematical intelligence or that came in last last week.
*  It's a whole issue devoted to to, you know, remembrance of him.
*  Did you know him?
*  I slept overnight in his house several times.
*  Yeah, he recently passed away.
*  Yeah, he got he died a year ago.
*  May I think it was of covid.
*  What do you what are some memories of him of his work that stand out for you?
*  Is that on a technical level that any of his work inspire you on a personal level that did he himself inspire you in some way?
*  Absolutely to all of those things.
*  But let's see, when did I first meet him?
*  I guess I first met him at Oxford in 1967 when I was.
*  Wow. OK, that's a long time ago.
*  Yeah. Yeah. You were minus 20 years old or something.
*  I don't know. But but there was a conference where I think I spoken.
*  I was speaking about something that no one has the Knuth Bendix algorithm now, but he but he he gave a famous talk about knots.
*  And and at the end, I didn't know at the time.
*  But but anyway, that talk had now the source of thousands and thousands of papers since then.
*  And it was he was reported on something that he had done in high school.
*  You know, almost 10 years earlier before this conference, but he never published it.
*  And and he climaxed his talk by building some knots.
*  You have these little plastic things that you that you can stick together.
*  It's it's it's something like Lego, but easier.
*  And so he made a whole bunch of knots in front of the audience and so on and then disassembled.
*  So it was a dramatic lecture before he had learned how to give even more dramatic lectures later.
*  So all right. And were you at that lecture?
*  And I was there. Yeah, because I had to. I was at the same conference.
*  For some reason, I was I happened to be in in Calgary at the same day that he was visiting Calgary.
*  And it was the spring of 72. I'm pretty sure.
*  And and we had lunch together and he wrote down during the lunch on a napkin all of the facts about what he called numbers.
*  And and and he covered the napkin with with the theorems about his his idea of numbers.
*  And I thought it was incredibly beautiful.
*  And and later in 1972, my sabbatical year began and I went to Norway.
*  And in December of that year, in the middle of the night, the thought came to me, you know, Conway's theory about numbers would be a great thing to teach students how to invent research and what the joys are of research.
*  And and and so I said and I had also read a book in dialogue by by Alfred Rennie,
*  where kind of a Socratic thing where the two characters were talking to each other about mathematics.
*  And so I and so at the end in the morning, I woke up my wife and said, Jill, I think I want to write a book about Conway's theory.
*  And, you know, you know, I'm supposed to be writing the art of computer programming, doing all this other stuff.
*  But I got but I really want to write this other book.
*  And so we made this plan.
*  But I said, I thought I could write it in a week.
*  And we made the plan then.
*  So in January, I rented a room in a hotel in downtown.
*  We were in sabbatical in Norway.
*  And I rented the hotel in downtown Oslo and did nothing else except write Conway's theory.
*  And I changed the name to surreal numbers that so this book is now published as Surreal Numbers.
*  And and you know, we figured we'd always wondered what would he like to have an affair in a hotel room.
*  So so we figured out that she would visit me twice during the week and things like this.
*  You know, we would try to sneak in.
*  This was hotel was was run by a mission organization.
*  These ladies were probably very strict.
*  But anyway, so so and the wild week in every way.
*  But the thing is, I had lost that I had lost that napkin in which he wrote the theory.
*  But I looked for it, but I couldn't find it.
*  So I tried to recreate from memory what he had told me at that lunch in Calgary.
*  And and as I as I wrote the book, I was going through exactly what I what the characters in the book were supposed to be doing.
*  So I start with the with the two axioms that start out the whole thing.
*  Everything is defined flows from that.
*  But you have to discover why.
*  And and as every mistake that I make as I'm trying to discover it, I my characters make to you know, and and and so it's a long, long story.
*  But I worked through this week and it was it was one of the most intense weeks of my life.
*  And and I I described it in other places.
*  But but but anyway, after six days, I finished it.
*  And on the seventh day, I rested and and I sent to my secretary to type it.
*  It was flowing as I was writing it faster than I could think almost.
*  But but but after I finished it and tried to write a letter to my secretary telling her how to type it, I couldn't write anymore.
*  She gave it everything.
*  The muse had left me completely.
*  Can you explain how that week could have happened?
*  Like, why is that seems like such a magical week of no idea.
*  But anyway, there was some it was almost as if I was channeling.
*  So so so the book was typed.
*  I sent it to Conway and and he said, well, then you got the accident.
*  The one axiom wrong.
*  It is a difference between less than or equal and not greater than.
*  I don't know the opposite of being greater than.
*  Yeah. And less than or equal.
*  But anyway, technically, it can make a difference when you're developing a logical theory.
*  And the way I had chosen was harder to do than John's original.
*  So and we visited him at his house in Cambridge in April.
*  We took a boat actually from Norway over to across the channel and so on and stay with him for some days.
*  And he told he talked we talked about all kinds of things he has.
*  He had puzzles that I'd never heard of before.
*  He had a great way to to solve the game of solitaire.
*  Many of the common interests that we know he had never written up.
*  But anyway, then in the summertime, I took another week off and went to a place in in in the mountains of Norway and rewrote the book using the correct axiom.
*  So that was the most intensive connection with Conway.
*  After that, it started with a napkin.
*  It started with a napkin.
*  But but but we would run into each other.
*  Well, yeah, the next really important.
*  I was giving lectures in Montreal.
*  I was giving a series of of seven lectures about a topic called stable marriages.
*  And and he arrived in Montreal between my sixth and seventh lecture.
*  And and we met at a party.
*  And I started telling him about the topic I was doing.
*  And he sat and thought about it.
*  He came up with a beautiful theory to show that the technical terms, it's that the that the set of all stable marriages forms a lattice.
*  And and there was a simple way to find the greatest lower bounding of two stable fairings and least upper bound of two stable marrying.
*  And so I could use it in my lecture the next day.
*  And he came up with this theorem during the party.
*  And it was a brilliant it's a distributive lesson.
*  I mean, it's it's you know, it added greatly to the theory of stable matching.
*  So you mentioned your wife, Jill, much in stable marriage.
*  Can you tell the story of how you two met?
*  So we celebrated 60 years of what it lists last month.
*  And and we met because I was dating her roommate.
*  This was my sophomore year, her freshman year.
*  I was dating her roommate and I wanted her advice on strategy or something like this.
*  And anyway, I found I enjoyed her advice better than I enjoyed her roommate.
*  You guys are majoring the same thing?
*  No, no, no.
*  Because I read something about working on a computer in grad school on a difficult computer science topic.
*  So so she's an artist and I'm OK.
*  And I'm a geek.
*  And what was she doing with a computer science book?
*  All right. I read it.
*  Was it the manual that she was reading?
*  What was she? I wrote the manual that she had had.
*  She had to take a class in computer science.
*  OK. And and so you're the tutor.
*  No, no. Yeah, no, we know we there were terrible times.
*  You know, trying to learn certain concepts, but I learned art from her.
*  And so we work together, you know, occasionally in design projects.
*  But but every year we write a Christmas card and and we each have to compromise our our own notions of beauty.
*  Yes. When did you fall in love with her?
*  That day that I asked her about her roommate.
*  OK. I mean, no, I OK.
*  So you're I don't mind telling these things, depending on how you for how far you go.
*  But let me promise you.
*  Let me tell you this.
*  I never really enjoyed kissing until I found how she did it.
*  And 60 years.
*  Is there a secret you can you can say in terms of stable marriages, how you stayed together so long?
*  The topic stable marriage, by the way, is not is a technical term.
*  It's a joke, Don.
*  But two different people will have to learn how to compromise and and work together.
*  And you're going to have ups and downs and and crises and so on.
*  And so as long as you don't set your expectation on having 24 hours of bliss,
*  then there's a lot of hope for stability.
*  But if you if if you decide that it's that that there's going to be no frustration.
*  So you're going to have to compromise on your notions of beauty when you write Christmas cards.
*  That's it.
*  You you mentioned that Richard Feynman was someone you looked up to.
*  Yeah.
*  Probably you've met him in Caltech.
*  Well, we knew each other.
*  Yeah, at Caltech for sure.
*  Yeah.
*  You are one of the seminal personalities of computer science.
*  He's one for physics.
*  Have you?
*  Is there specific things you picked up from him by way of inspiration or?
*  So we used to go to each other's lectures and and but but if I saw him sitting in the front row,
*  I would throw me for a loop, actually.
*  And I would I would miss a few a few sentences.
*  What unique story do I have?
*  I mean, I often refer to his his time in Brazil where he essentially said they were teaching all the physics students the wrong way.
*  They were just they were just learning how to pass exams and not learning how to do math.
*  And he said, you know, if you want me to prove it, you know, here I'll turn to any page of this textbook and and I'll tell you what's wrong with this page.
*  And he did so.
*  And the textbook had been written by his host.
*  And and it was a big embarrassing incident.
*  But he had previously asked his host if if he was supposed to tell the truth.
*  But but anyway, it epitomizes the way education goes wrong in all kinds of fields and has to periodically be brought back from from from a process of giving credentials to a process of giving knowledge.
*  That's probably a story that continues to this day in a bunch of places where it's too easy for educational institutions to fall into credentialism versus inspirationalism.
*  I don't know if those are words, but sort of understanding versus just giving a little plaque.
*  And, you know, it's it's pretty much like what we were talking about.
*  If you want the computer to if you want to be able to believe the answer, a computer is sure it's doing that.
*  One of the things Bob Floyd showed me in the 60s, there was a he loved this cartoon.
*  There was a there were two guys standing in front of in those days, a computer was a big thing, you know, and and the first guy says to the other guy, he said,
*  this machine can do in one second what it would take a million people to do in 100 years.
*  And the other guy says, oh, so how do you know it's right?
*  That's a good line.
*  Is there some interesting distinction between physics and math to you?
*  Have you looked at physics much to like speaking of Richard Feynman?
*  So the difference between the physics community, the physics way of thinking, the physics intuition versus the computer science, the theoretical computer science, the mathematical sciences.
*  Do you see that as a gap or are they strongly overlapping?
*  It's quite different.
*  In my opinion, I started as a physics major and I switched into math.
*  And probably the reason was that I could I could get A plus on the physics exam, but I like I never had any idea why I would have been able to come up with the problems that were on those exams.
*  But but in math, I knew, you know, why the teacher set those problems and I thought of other problems that I could set too.
*  And I believe it's quite a different mentality.
*  It has to do with your philosophy of geek, geekdom.
*  No, it's I mean, some of my computer scientists friends are really good at physics and others are not.
*  And I'm you know, I'm really good at algebra, but not at geometry.
*  Talk about different parts of mathematics.
*  You know, it's just it's so different kind of physical.
*  But physicists think of things in terms of waves and I can think of things in terms of waves, but it's like a dog walking on hind legs if I'm thinking about.
*  So you basically you like to see the world in in in discrete ways and then more continuous.
*  Yeah, I'm not sure if Turing would have been a great physicist.
*  I think it was a pretty good chemist.
*  But I don't know. But but but anyway, I see things.
*  I believe that computer science is largely driven by people who have brains who are good at resonating with certain kind of of of concepts and quantum computers.
*  It takes a different kind of brain.
*  Yeah, that's interesting. Yeah.
*  It's well, quantum computers is almost like at the intersection in terms of brain between computer science and physics, because they involves both at least at this at this time.
*  But there is like the physicists I've known they have incredibly powerful intuition.
*  And I mean, statistical mechanics.
*  So I I study statistical mechanics and I mean, random processes are related to algorithms in a lot of a lot of ways.
*  But there's lots of different flavors of flavors of physics, as there are different flavors of mathematics as well.
*  But the thing is that I don't see.
*  Well, actually, when they talk to physicists use completely different language than when they're talking to when they're writing expository papers.
*  And so I didn't understand quantum mechanics at all from reading about it in Scientific American.
*  But when I read how they describe it to each other, talking about eigenvalues and various mathematical terms that that made sense, then it made sense to me.
*  But Hawking said that every formula you put in a book, you lose half of your readers.
*  So he didn't put any formulas in the book. So I couldn't understand his book at all.
*  You could say you understood it, but I really, I really didn't.
*  Well, Feynman also spoke in this way.
*  So Feynman, I think, prided himself on really strong intuition.
*  But at the same time, he was hiding all the really good, the deep computation he was doing.
*  So there was one thing that that I was never able to.
*  I wish I had more time to work out with him, but I guess I could describe it for you.
*  There's there's something that got my name attached to it called Knuth-Arrow notation.
*  But it's a notation for very large numbers.
*  And so I find out that that somebody invented it in in 1830s.
*  It's fairly easy to understand anyway.
*  So you start with x plus x plus x plus x n times.
*  And you can call that x n.
*  So x n is multiplication.
*  Then you take x times x times x times x n times.
*  That gives you exponentiation, x to the nth power.
*  So that's one arrow.
*  So x n with no arrows is multiplication.
*  X arrow n is x to the nth power.
*  Yes. Just to clarify for the.
*  So x times x times x n times is obviously x n.
*  X plus x plus x n times.
*  Oh, yeah. OK. And then x n.
*  No multiplication is x to the n.
*  And then and then here the arrow is when you're doing the same kind of repetitive operation for the exponential.
*  So I put in one arrow and I get x to the nth power.
*  Now I put in two arrows and that makes takes x to the x to the x to the x to the x n times power.
*  So in other words, if it's two double arrow, three, that would be that would be two to the two to the two.
*  So that would be two to the fourth power. That'd be 16. OK.
*  So so so that's the double arrow.
*  And now you can do with triple arrow, of course, and and so on.
*  And and I had this this paper called Well, it's essentially big numbers.
*  You know, you try to impress your friend by saying a number they've never thought of before.
*  And and and I gave a special name for it and designed a font for it that has script K and so on.
*  But but it really is 10, I think, like 10 quadruple arrow three or something like that.
*  And I claim that that number is so mind boggling that you can't comprehend how large it is.
*  But anyway, Feynman, I talked to Feynman about this and he said, oh, let's just let's just use double arrow.
*  But instead of taking integers, let's consider complex numbers.
*  So you know, you have that.
*  I mean, OK, X, X, arrow, arrow two.
*  That means X, X, X, X.
*  But what about X, X, double arrow to two point five?
*  Well, that's not too hard to figure out.
*  That's interpolate between those.
*  But what about X double arrow?
*  I or one plus I or some complex number.
*  And and so he claimed that that that there was no analytic function that would that would that would do the job.
*  But I didn't know how he could claim that that was that wasn't true.
*  And his next question was, did then have a complex number of arrows?
*  Yeah. OK. Wow. OK.
*  OK. So that's that's Feynman. That's five.
*  Yeah. Can you describe what the new Morris Pratt algorithm does and how did you come to develop it?
*  One of the many things that you're known for and has your name attached to it?
*  Yeah. All right. So it should be actually Morris Pratt Knuth.
*  But we decided to use alphabetical order when we published the paper.
*  The problem is something that everybody knows now, if they're if they're using a search engine, you have a large collection of text.
*  And you want to know if if the word Knuth appears anywhere in the text, say, or or some some other word that's less interesting than Knuth.
*  But anyway, that's the most interesting. Morris or something like Morris.
*  Right. We have we have a large piece of text and it's all one long, one dimensional thing.
*  You know, first letter, second letter, et cetera, et cetera, et cetera.
*  And so the question, you'd like to be able to do this quickly.
*  And the obvious way is, let's say we're looking for Morris.
*  OK. So we would we would go through and wait till we get to letter M.
*  Then we look at the next word and sure enough, it's an O and then an R.
*  But then, too bad, the next letter is is E.
*  So we missed we missed out on Morris.
*  And so we go back and start looking for another.
*  So that's the obvious way to do it.
*  All right. And and Jim Morris noticed there was a more clever way to do it.
*  The obvious way would have started.
*  Let's say we found that letter M at character position one thousand
*  was started next at character position one thousand and one.
*  But but he but he said, no, look, we already read the O and the R
*  and we know that they aren't M's. So we can we can start.
*  We don't have to read those over again.
*  So and this gets pretty tricky when when the word isn't Morris,
*  but it's more like abracadabra where you have patterns that are occurring.
*  Like repeating patterns at the beginning, at the middle.
*  Right. Right. So so he worked it out and he put it into the system software at Berkeley,
*  I think it was where he was.
*  He was writing some Berkeley Unix, I think it was some routine
*  that was supposed to find occurrences of patterns in text and and
*  and we didn't explain it.
*  And so he found out that several months later, somebody had had looked at it,
*  didn't look right. So they ripped it out.
*  So he had this this algorithm, but it didn't make it through,
*  you know, because he wasn't understood.
*  Nobody knew about this particularly.
*  Von Pratt also had independently discovered it a year or two later.
*  I forget why.
*  I think Von was studying some technical problem
*  about palindromes or something like that.
*  He wasn't really it.
*  Von wasn't working on on text searching,
*  but he was working on a on an abstract problem that that was related.
*  Well, at that time, Steve Cook was a professor at Berkeley.
*  And it was the greatest mistake that Berkeley CS department made was not to give him tenure.
*  So Steve went to went to Toronto.
*  But but but I knew Steve while he was at Berkeley.
*  And he had come up with a with a very peculiar theorem
*  about a technical concept called a stack automaton.
*  And a stack automaton is a machine that that it can't do everything a Turing machine can do.
*  But it can only look at something on at the top of a stack
*  or it can put more things on the stack or or it can take things off the stack.
*  Like it can't remember a long string of symbols, but it can remember them in reverse order.
*  So if you tell a stack automaton ABCDE, it can it can tell you afterwards.
*  EDCBA, you know, it doesn't have any other memory except except this one thing that it can see.
*  And Steve Cook proved this amazing thing that says if a stack automaton can recognize a language,
*  where the strings of language are length n in any amount of time whatsoever,
*  for the stack automaton, like you zillion steps, a regular computer can recognize that same language in time n log n.
*  So Steve had a way of transforming a computation that goes on and on and on and on
*  and on and on and on in into using different data structures into something that you can do on a regular computer fast.
*  The stack automaton goes slow.
*  But but but but somehow the fact that it can do it at all means that there has to be a fast way.
*  So I thought this was a pretty cool theorem.
*  And so I tried it out on on a problem where I knew a stack automaton could do it,
*  but I couldn't figure out a fast way to do it on a regular computer.
*  I thought I was a pretty good programmer.
*  But but by golly, I couldn't think of any way to recognize this language efficiently.
*  So I went through Steve Cook's construction.
*  I filled my blackboard with all the everything that stack automaton did.
*  You know, I wrote down and then I tried to see patterns in that.
*  And and how did he convert that into a computer program on a regular machine?
*  And finally, I psyched it out.
*  What was what was the thing I was missing so that I could say, oh, yeah, this is what I should do in my program.
*  And now I have a fishing program.
*  And and so I I would never have thought about that if I hadn't had his theorem, which was purely abstract thing.
*  You use this to try to intuit how to use the stack automaton for the string matching problem.
*  Yeah. So so so the problem I I had started with was not the string matching problem.
*  But then I realized that the string matching problem was another thing which would also be could be done by a stack automaton.
*  And so when I looked at what that told me, then I had a nice algorithm for this string matching problem.
*  And it told me exactly what I should remember as I'm as I'm going through the string.
*  And I worked it out. And and I wrote this little paper called Automata Theory Can Be Useful.
*  And the reason was that it was the first I mean, I had been reading all kind of papers about automata theory, but it never taught me.
*  It never improved my programming for everyday problems.
*  It was something that you publish in journals. And you know, it was it was interesting stuff.
*  But it but here was a case where I couldn't figure out how to write the program.
*  I had a theorem from automata theory. Then I knew how to write the program.
*  So this was for me a change in life.
*  I started to say maybe I should learn more about automata.
*  And and and I showed this note to Vaughan Pratt and he said he that's similar to something I was working on.
*  And then and Jim Morris was at Berkeley, too, at the time.
*  Anyway, he he he's had an illustrious career, but I haven't kept track of Jim.
*  But Vaughan is my colleague at Stanford and my student later.
*  But but this is before Vaughan Vaughan was still a graduate student and hadn't come to Stanford yet.
*  So we found out that we'd all been working on the same thing.
*  So it was our algorithm we each discovered independently.
*  But we each of us had discovered a different a different part of the elephant,
*  you know, a different aspect of it.
*  And so we could put our our things together with my job to write the paper.
*  How did the elephant spring to life?
*  Spring to life was because I I had drafted this paper, automata theory.
*  Oh, it can be useful, which was seen by Vaughan and then by Jim and then by Jim.
*  And then then then we combined because maybe they had also been thinking of writing something up about it.
*  About specifically a string match, a string match problem period.
*  Let me ask a ridiculous question.
*  Last time we talked, you told me what the most beautiful algorithm is actually for strongly connected graphs.
*  What is the hardest problem?
*  Puzzle idea in computer science for you personally that you had to work through?
*  Just something that was just the hardest thing that I've ever been involved with.
*  Yeah. OK, well, yeah, that's I don't know how to answer questions like that.
*  But in this case, it's pretty clear.
*  OK, because it's called the birth of the giant component.
*  OK, so now let me explain that, because this is actually gets gets into physics, too.
*  And it gets into something called Bose Einstein statistics.
*  But but but anyway, it's got some interesting stories and it connected with Berkeley again.
*  So start with the idea of a random graph.
*  Now, this is the here we just say we have end points that are totally unconnected and and there's no geometry involved.
*  There's no saying some points are further apart than others.
*  All points are exactly are exactly alike.
*  And let's say we have a graph of a point that's exactly the same as the other point.
*  They're exactly alike. And let's say we have 100 points and we number them from zero zero to nine nine.
*  All right. Now, let's let's take pi the digits of pi.
*  So two at a time. So we had thirty one forty one fifty nine twenty six.
*  We can look go go through pi.
*  And so we take the first two thirty one forty one and let's let's put a connection between point thirty one and point forty one.
*  That's an edge in the graph.
*  So then we take five nine two six and make another edge.
*  And the graph gets bigger, gets more and more connected as we add these things one at a time.
*  We started out with endpoints and we add m edges.
*  OK. Each edge is completely we forgot about it.
*  Edges we had before. We might get an edge twice.
*  We might get an edge from a point to itself.
*  But you know, maybe pi is going to have a run of four digits in there.
*  So we're going to. But anyway, we're evolving a graph at random.
*  And a magical thing happens when the number of edges is like point four nine and maybe n is a million.
*  And I have, you know, four hundred ninety thousand edges.
*  Then it almost all the time it consists of isolated trees.
*  Not even any loops.
*  It's a very small number of edges so far.
*  A little less than half and and.
*  But if I had point five one, it's just a little more than half.
*  So, you know, million points, five hundred and ten thousand edges.
*  Now it probably has a one component that's much bigger than the others.
*  And we call that the giant component.
*  Can you clarify? So is there a name for this kind of random super cool pi random graph?
*  Well, I call it the pie graph.
*  No, no, the pie graph is actually my pie graph is based on on binary representation of pi, not the decimal representation of pi.
*  But but but but anyway, let's suppose I was rolling dice instead.
*  So so so it doesn't doesn't have to be pie.
*  Any source of the point is every step, choose totally at random one of those endpoints, choose totally at random another one of the endpoints.
*  Make that an edge.
*  That's the process.
*  Yeah. So there's there's nothing magical about pi.
*  You know, I was using pi to sort of saying pi is sort of random that nobody knows a pattern.
*  Exactly. Got it.
*  But it's not. Yeah, I could have just as well drawn straws or something.
*  This was a concept invented by Erdos and Rényi and they call it the evolution of random graphs.
*  And if you start out with with a large number and and you and you repeat this process, all of a sudden a big bang happens at one half in.
*  There'll be two points together. Then maybe we'll have have three.
*  And then then they maybe branch out a little bit.
*  But they'll all be separate until we get to one half in and we pass one half in and all of a sudden there's substance to it.
*  There are a lot of the big clump of stuff that's all joined together.
*  So it's almost like a phase transition of some kind.
*  Exactly. It's a phase transition, but it's a double phase transition.
*  It turns out it happens.
*  I mean, there's actually two things going on at once at this phase transition, which is very remarkable about it.
*  OK, so so a lot of the most important algorithms are based on random processes.
*  And so I wanted to I want to understand random processes now.
*  So there are data structures that sort of grow this way.
*  OK, so so so Dick Karp, one of the leading experts on on random randomized algorithms,
*  his students working looking at this at Berkeley.
*  And we heard a rumor that the students had found something interesting happening.
*  The students are generating this are simulating this random evolution of graphs.
*  And they're taking step snapshots that are so often take a look at what the graph is.
*  And the rumor was that every time they looked, there was only one component that had loops in it.
*  Almost always they do a million experience and only three or four times did they ever ever happen to see a loop at this point.
*  No, more than one component with a loop.
*  So they watch until the graph gets completely full, starts out totally empty and gets more and more more and more edges all the time.
*  And so, OK, certainly a loop comes along once.
*  But but now all the loops stay somehow joined to that one.
*  They're they're never there never were two guys with loops.
*  Wow. Interesting.
*  OK. In his experiment.
*  OK. So anyway, this almost always not always.
*  Yeah. But but but with very high probability, this seemed to be true.
*  So so we heard about this rumor at Stanford and we said, if that's true, then must, you know, a lot more must also be true.
*  So there's a whole bunch. There's a whole theory out there waiting to be discovered that we haven't ever thought about.
*  So let's take a look at it.
*  And so we look closer and we find out, no, actually, it's not true.
*  But but in fact, it's almost true, namely, there's a very short interval of time when it's true.
*  And if you don't happen to look at it during that short interval of time, then you miss it.
*  So that, in other words, there'll be a period where there are two or three components have loops.
*  But they join together pretty soon.
*  OK. So if you don't have a real fast shutter speed, you're going to miss you're going to miss that instant.
*  So separate loops don't exist for long.
*  That's that's it. Yeah. You know, I started looking at this to make it quantitative.
*  And the basic problem was to slow down the Big Bang so that I could watch it happening.
*  Yeah, I think I can explain it actually in fairly elementary terms, even even without writing a formula.
*  That's right. Like Hawking would do.
*  And and and so let's let's watch the evolution.
*  And at first, these edges are coming along and they're just making things without loops, which we call trees.
*  OK. So then all of a sudden, a loop first appears.
*  So at that point, I have one component that has a loop.
*  All right. Now, now I say that the complexity of a component is the number of edges minus the number of vertices.
*  So if I have a loop, I have like a loop of length five has five edges and five vertices.
*  Or I could put a tail on that and that would be another edge, another vertex.
*  It's like a zero, one, two complexity kind of thing.
*  So if the if the complexity is zero, we have one one loop I call a cycle or I call a cyclic components.
*  So cyclic component looks like a wheel to which you attach fibers or trees.
*  They go branching, but there's no more loops.
*  There's only one loop and everything else feeds into that loop.
*  OK. And that has complexity zero.
*  But a tree itself has complexity minus one because it has like like like it might have 10 vertices and nine edges to tie the time together.
*  So nine minus 10 is minus one.
*  So so complexity minus one is a tree.
*  It's got to be connected. That's what I mean by a component.
*  It's got to be connected.
*  So if I have 10 things connected, I have to have nine edges.
*  Can you clarify why when complexity goes can go above zero?
*  I'm a little yes. Right.
*  So the complexity plus one is the number of loops.
*  So if complexity is zero, I have one loop.
*  If if complexity is one, that means I have one more edge than I have heard.
*  So I might have like 11 edges and 10 vertices.
*  So it turns we call it a bicycle because it's got two loops and it's got to have two loops in it.
*  Well, why can't it be trees just going off of the loop that I would need more edges than I.
*  All right. Right. OK.
*  So every time I get another loop, I get another excess of edges over vertices.
*  I got you. OK. So in other words, we start out and after I have one loop, I have one component that has a cycle in it.
*  Now, the next step, according to the rumor, would be that at the next step, I would have a bicycle in the evolution of almost all graphs.
*  It would go from cycle to bicycle.
*  But in fact, there's a certain probability it goes from cycle to two different cycles.
*  Right. And I worked out the probability was something like five out of 24.
*  That was pretty high. It was substantial.
*  Yeah. But still, soon they're going to merge together almost.
*  OK. So that's so cool.
*  But then it splits again after you have either either two or one one.
*  The next step is you either have three or you have two one or you have one one one.
*  OK. And so I worked out the probability for those transitions and I worked it out up to up to the first five transitions.
*  And I had these I had these strange numbers, five twenty fours, and I stayed up all night and about three a.m.
*  I had the numbers computed and I looked at them and here were the denominator was something like.
*  Twenty two three zero two three.
*  So the probability was something over two three oh two three.
*  I don't know how you work that out, but I had a formula that I could calculate the probability.
*  Yeah. And I could find the limiting probability as n goes to infinity.
*  And it turned out to be this number.
*  But the denominator was two three.
*  And I looked at the denominator.
*  I said, wait a minute.
*  This number factors because one thousand and one is equal to seven times eleven times thirteen.
*  I had learned that my first computer program.
*  So so so so twenty three oh twenty three is seven times eleven times thirteen times twenty three.
*  That's not a random number.
*  There has to be a reason why those small primes appear in the denominator.
*  But my so all of a sudden that suggested another way of looking at the problem where small prime factors would occur.
*  So what would that be?
*  So that said, oh, yeah.
*  Let me take the logarithm of this formula and and sure enough, it's going to simplify.
*  And it happened.
*  So and I wouldn't have noticed it except for this factorization.
*  OK.
*  So I go to bed and I say, OK, this is this looks like I'm flowing down the big bang.
*  I can figure out what's going on here.
*  And the next day it turned out Bill Gates comes to Stanford to visit.
*  They're trying to sell him on donating money for a new computer science building.
*  And and and I simply gave me an appointment to talk to Bill and I and I wrote down on the blackboard this
*  evolutionary diagram from one to five twenty fours and all this business.
*  Yeah. And I wrote it down.
*  And anyway, at the end of the day, he was discussing people with the with the development office and he said, boy, I was really impressed with what Professor Knuth said about this giant component.
*  And and so, you know, I love this story because it shows that theoretical computer science is really worthwhile.
*  Does Bill have you ever talked to Bill Gates about it since then?
*  Yeah. That's a cool. That's a cool little moment in history.
*  But anyway, he happened to visit on exactly the day after I had I had found this pattern and that allowed me to crack the problem so that I could develop the theory, the theory some more and understand what's happening in the big.
*  But because I could I could now write down explicit formulas for stuff.
*  And so it would work not only the first few steps, but also the study, the whole process.
*  And and I worked further and further and I with two authors, coauthors, and we finally figured out that the probability that the rumor is true.
*  In other words, look at the evolution of of a random graph going from zero zero to complete and say, what's the probability that at every point in time there was only one component with a cycle?
*  We started with this rumor saying there's only one site, there's only one component with a cycle.
*  And so the rumor was that it's 100 percent rumor was that was 100 percent.
*  It turned out the actual numbers is like 87 percent.
*  I should remember the number, but I don't have it with me.
*  But but anyway, but but the but the number it turned out to be like 12 over pi squared or eight over.
*  Anyway, it was a nice it related to pi.
*  Yeah.
*  And we could never have done that with it.
*  So that's the hardest problem I ever solved in my life was to prove that this probability is.
*  It was proven.
*  The probability was proven.
*  Yeah, I was able to prove this that this and this should shed light on a whole bunch of other things about random graphs.
*  That was sort of the major thing we were after.
*  That's super cool.
*  I what was the connection to physics that you mentioned?
*  Well, Bose Einstein statistics is a study of how molecules bond together without geometry, without distance.
*  You created the tech type setting system and released it as open source.
*  Just on that little aspect.
*  Why did you release it as open source?
*  What is your vision for open source?
*  No.
*  OK, well, that the word open source didn't exist at that time.
*  But we but I didn't want proprietary rights over it because I saw how proprietary rights were holding things back in the late 50s.
*  People at IBM developed the language called Fortran.
*  They could have kept it proprietary.
*  They could have said only IBM can use this language.
*  Everybody else has to.
*  But they didn't.
*  They said anybody who can write who can translate Fortran into the into the language of their machines is allowed to make Fortran compilers too.
*  On the other hand, in the typography industry, I had seen a lot of languages that were developed for composing pages.
*  And each manufacturer had his own language for composing pages.
*  And that was holding everything back because people were tied to a particular manufacturer and then a new equipment is invented a year later.
*  But printing machines, they have to expect to amortize the cost over 20, 30 years.
*  So you didn't want that for tech?
*  I didn't need the income.
*  I already I already had a good job.
*  And my books were people were buying enough books that I that that it would bring me plenty of supplemental income for everything my kids needed for education, whatever.
*  So there was no reason for me to try to maximize income any further.
*  Income is sort of a threshold function.
*  If you don't have if you don't have enough, you're starving.
*  But if you get over the threshold, then you start thinking about philanthropy or else you're trying to take it with you.
*  But but anyway, there's a I had my income was over the threshold.
*  So I didn't need to keep it.
*  And so I specifically could see the advantage of of making it open for everybody.
*  Do you think most software should be open?
*  So I think that people should charge for non-trivial software, but not for trivial software.
*  Yeah, you give an example of I think Adobe Photoshop versus GIMP on Linux as Photoshop has value, which so it's definitely worth paying, paying for all this.
*  I mean, I mean, well, they keep adding adding stuff that my wife and I don't care about.
*  But somebody I mean, but I mean, but they have built in a fantastic undo feature, for example, in Photoshop, where you you can go through a sequence of a thousand complicated steps on graphics and it can take you back anywhere in that sequence.
*  Yeah.
*  With really beautiful algorithm.
*  I mean, yeah, it's it's.
*  Oh, that's interesting.
*  I didn't think about what algorithm it must be some kind of efficient representation.
*  Really? Yeah, I know.
*  I mean, there's a lot of really subtle Nobel Prize class creation of intellectual property in in there.
*  And.
*  And with patents, you get a limited time to.
*  I mean, eventually the idea of patents is that you publish so that it's not secret.
*  It's not a trade secret.
*  That said, you you've said that I currently use Ubuntu Linux on a standalone laptop.
*  It has no Internet connection.
*  I occasionally carry flash memory drives between the machine and the Macs that I use for network surfing and graphics, but I trust my family jewels only to Linux.
*  Why do you love Linux?
*  The version of Linux that I use is stable.
*  Actually, I'm going to have to upgrade one of these days, but.
*  To a newer version of Ubuntu.
*  Yeah, I'll stick with Ubuntu, but but right now I'm running something that doesn't support a lot of the new software.
*  The last day I don't remember the number of like 14.
*  Anyway, it's quite and I'm going to get a new computer.
*  I'm getting new solid state memory instead of a hard disk.
*  Well, let me ask you, thinking on the topic of tech.
*  When thinking about beautiful typography, what is your favorite letter, number or symbol?
*  I know, I know ridiculous question, but is there something?
*  Look at the last page.
*  At the very end of the index.
*  What is that?
*  There's a book by Dr. Seuss called On Beyond Zebra, and he gave a name to that.
*  Did you say Dr. Seuss gave a name to that?
*  Dr. Seuss, this is a S-E-U-S-S-E.
*  He wrote children's books in the 50s, 40s and 50s.
*  Wait, are you talking about Cat in the Hat?
*  Cat in the Hat, yeah.
*  That's it.
*  I like how you hit the spot.
*  On Beyond Zebra.
*  Did it get to Soviet Union?
*  No, Dr. Seuss did not come to the Soviet Union.
*  Oh, actually, I think it did a little bit when we were...
*  That was a book, maybe Cat in the Hat or Green Eggs and Ham, I think was used to learn English.
*  Oh, okay.
*  So I think it made it in that way.
*  Okay, I didn't like those as much as Bartholomew Cubbins, but I used to know Bartholomew Cubbins by heart when I was young.
*  So what the heck is this symbol we're looking at?
*  There's so much going on.
*  He has a name for it at the end of his book, On Beyond Zebra.
*  Who made it?
*  He did.
*  He did.
*  So there's... it looks like a bunch of vines.
*  Does that symbol exist in tech?
*  By the way, he made a movie in the early 50s.
*  I don't remember the name of the movie now.
*  You can probably find it easily enough.
*  It features dozens and dozens of pianos all playing together at the same time.
*  But all the scenery is sort of based on the kind of artwork that was in his books and the fantasy based of Seussland.
*  And I saw the movie only once or twice, but it's quite... I'd like to see it again.
*  That's really fascinating that you gave them... they gave them shout out here.
*  Okay.
*  Is there some elegant basic symbol that you're attracted to?
*  Something that gives you pleasure, something you use a lot?
*  Pi?
*  Pi, of course.
*  I try to use Pi as often as I can when I need a random example.
*  Because it doesn't have any known characters.
*  So for instance, I don't have it here to show you, but do you know the game called Masyu?
*  No.
*  It's a great recreation.
*  I mean, Sudoku is easier to understand, but Masyu is more addictive.
*  You have black and white stones like on a go board.
*  And you have to draw a path that goes straight through a white stone and makes the right angle turn at the black stone.
*  And it turns out to be a really nice puzzle because it doesn't involve numbers.
*  It's visual, but it's really pleasant to play with.
*  So I wanted to use it as an example in art of computer programming.
*  And I have I have exercises on how to design cool Masyu puzzles.
*  You can find it on Wikipedia, certainly as an example, M-A-S-Y-U.
*  And so I decided I would take Pi, the actual image of it, and it had pixels.
*  And I would put a stone wherever it belongs in the letter Pi, in the Greek letter Pi.
*  And the problem was, find a way to make some of the stones white, some of the stones black, so that there's a unique solution to the Masyu puzzle.
*  That was a good test case for my algorithm on how to design Masyu puzzles,
*  because I insisted in advance that the stones had to be placed in exactly the positions that make the letter Pi, make a Greek letter.
*  OK, that's cool.
*  And so, you know, and it turned out there was a unique way to do that.
*  And so Pi is a source of examples where I can prove that I'm starting with something that isn't canned.
*  And most recently, I was writing about something called graceful graphs.
*  Graceful graphs is the following.
*  You have a graph that has M edges to it, and you attach numbers to every vertex in the following way.
*  So every time you have an edge between vertices, you take the difference between those numbers.
*  And that difference is got to tell you what edge it is.
*  So one edge, two numbers will be one apart.
*  There'll be another edge where the numbers are two apart.
*  And so it's a great computer problem.
*  Can you find a graceful way to label a graph?
*  So I started with a graph that I use for an organic graph, not a mathematically symmetric graph or anything.
*  I take 49 states of the United States.
*  The edges go from one state to the next state.
*  So, for example, California, be next to Oregon, Nevada, Arizona.
*  And I include District of Columbia.
*  So I have 49.
*  I can't get Alaska and Hawaii in there because they don't touch.
*  You have to be able to drive from one to the other.
*  So is there a graceful labeling of the United States?
*  Each state gets a number.
*  And then if California is number 30 and Oregon is number 11, that edge is going to be number 19.
*  The difference between those.
*  OK, so is there a way to do this for all the states?
*  And so I was thinking of having a contest for people to get it as graceful as they could.
*  But my friend Tom Rukiki actually solved the problem by proving that.
*  I mean, I was able to get it done within seven or something like that.
*  He was able to get a perfect solution.
*  The actual solution or to prove that a solution exists?
*  More precisely, I had figured out a way to put labels on so that all the edges were labeled somewhere between one and 117.
*  But there were some gaps in there because I should really have gone from one to 105 or whatever the number is.
*  So I gave myself too much slack, a lot of slack.
*  He did it without any slack whatsoever.
*  Perfect graceful labeling.
*  And so I call out the contest because the problem's already solved and too easy in a sense because Tom was able to do it in an afternoon.
*  Sorry, he gave the algorithm or for this particular?
*  For the United States.
*  For the United States?
*  This problem is incredibly hard.
*  For the general algorithm?
*  Generally, it's...
*  But it was very lucky that it worked for the United States.
*  Sure.
*  I think.
*  But the theory is still very incomplete.
*  But anyway, then Tom came back a couple of days later and he had been able to not only find a graceful labeling, but the label of Washington was 31.
*  The label of Idaho was 41, following the digits of pi.
*  Going across the topic, the United States, he has the digits of pi perfectly.
*  Did he do it on purpose?
*  He was able to still get a graceful labeling with that extra thing.
*  Wow.
*  Wow.
*  It's a miracle, okay.
*  But I like to use pi in my book, you see.
*  All roads lead to pi, somehow often hidden in the middle of the most difficult problems.
*  Can I ask you about productivity?
*  Productivity.
*  Yeah, you said that, quote, my scheduling principle is to do the thing I hate most on my to-do list.
*  By week's end, I'm very happy.
*  Can you explain this process to a productive life?
*  Oh, I see.
*  Well, but all the time I'm working on what I want, what I don't want to do.
*  But still, I'm glad to have all those unpleasant tasks finished.
*  Yes.
*  Is that something you would advise to others?
*  Well, I, yeah, I don't know how to say it.
*  During the pandemic, I feel my productivity actually went down by half because I have to communicate by writing, which is slow.
*  I have to, I mean, I don't like to send out a bad sentence, so I go through and reread what I've written and edit and fix it.
*  So everything takes a lot longer when I'm communicating by text messages instead of just together with somebody in a room.
*  And it's also slower because the libraries are closed and stuff.
*  But there's another thing about scheduling that I learned from my mother that I should probably tell you.
*  And that is different from what people in robotics field do, which is called planning.
*  So she had this principle that was see something that needs to be done and do it.
*  I would just instead of saying, I'm going to do this first and do this first, just, you know, just do it.
*  Oh, yeah, pick this up.
*  But you're at any one moment, there's a set of tasks that you can do.
*  And you're saying a good heuristic is to do the one you want to do least.
*  Right. The one I haven't got any good reason to.
*  I'll never be able to do any better than I am now.
*  I mean, there are some things that I know if I do something else first, I'll be able to do that one better.
*  But there are some that are going to be harder because, you know, I've forgotten some of the groundwork that went into it or something like that.
*  So I just finished a pretty tough part of the book.
*  And so now I'm doing the parts that are more fun.
*  But the other thing is, as I'm writing the book, of course, I want the reader to think that I'm happy all the time I'm writing the book.
*  You know, it's upbeat. I can have humor.
*  You know, I can say this is cool.
*  Well, this I have to I have to disguise the fact that it was painful in any way to come up.
*  The road to that excitement is painful.
*  Yeah, it's laden with pain.
*  OK, is there you've given some advice to people before, but can you can you give me too too much credit?
*  But anyway, this is my this is my turn to say things that I believe.
*  But what I want to preface it by saying, I also believe that other people do a lot of these things much better than I do.
*  So I can only tell you my side of it.
*  So can I ask you to give advice to young people today, to high school students, to college students,
*  whether they're geeks or the other kind about how to live a life that they can be proud of, how to have a successful career, how to have a successful life?
*  It's always the same as I've said before, I guess, not to do something because because it's trendy.
*  But but it's something that you personally feel that you were called to do rather than somebody else expects you to do.
*  How do you know you're called to do something?
*  If you tried and it works or you or it doesn't work.
*  I mean, you learn about yourself.
*  Life is a binary search.
*  You try something and you find out, oh, yeah, I have a background that helped me with this.
*  Or maybe I'm maybe I could do this if I worked a little bit harder.
*  But you try something else and you say, well, I have really no intuition for this.
*  And it looks like it looks like it doesn't have my name on it.
*  Was there advice along the way that you got about what you should and shouldn't work on?
*  Or do you just try to listen to yourself?
*  Yeah, I probably overreact another way.
*  When something when I see everybody else going somewhere, I probably I probably say, too much competition.
*  But but but but mostly I I played with things that were interesting to me.
*  And then later on, I found, oh, actually, the most important thing I learned was how to be interested in almost anything.
*  I mean, not to be bored. It hurts.
*  It makes me very sad when I when I see kids talking to each other and they say.
*  That was boring. And to me, a person should feel upset if he were help if he had to admit that he wasn't able to find something interesting.
*  Yeah. So, you know, the skill, like saying, I haven't learned how to how to enjoy life.
*  I have to have somebody entertain me instead of.
*  Right. That's really interesting. It is a skill.
*  And I think, Mr. Wallace, I really like the thing he says about this, which is the key to life is to be unborable.
*  And I do really like you saying that it's a skill, because I think that's a really good that's really good advice, which is if you find something boring, that's not.
*  Because it's boring. It's because you haven't developed a skill how to how to find the beauty and how to find the fun in it.
*  That's a really good point.
*  You know, sometimes it's more difficult than others to do this.
*  I mean, during the covid, lots of days when I never saw another human being.
*  But I still find other ways to.
*  It still was a pretty fun time.
*  I came earlier. I came a few minutes early today and I walked around Foster City.
*  I didn't want you know, I didn't know what's going on in Foster City.
*  I saw beautiful, some beautiful flowers at the nursery at Home Depot a few blocks away.
*  Yeah.
*  Life is amazing. It's full of amazing things like this.
*  Yeah, I just sometimes I'll sit there and just stare at a tree.
*  Nature is beautiful.
*  Let me ask you the big ridiculous question.
*  I don't think I asked you last time.
*  So I have to ask this time in case you have a good answer.
*  What is the meaning of life?
*  Our existence here on Earth, the whole thing.
*  Yeah.
*  No, no, you can't.
*  You can't. I will not allow you to to try to escape answering this question.
*  You have to answer definitively because they're surely, surely, Don Knuth.
*  There must be an answer.
*  What is the answer? Is it 42 or?
*  Yes. Well, I don't think it's a numerical.
*  That's the SDS.
*  That was in Zen.
*  OK, but all right.
*  So anyway, it's only for me.
*  But I personally, I think it's a good question.
*  And but I but I personally think of my belief that that God exists, although I have no idea what that means.
*  But I believe that there is some something beyond human capabilities.
*  It might be it might be some AI, but whatever it is.
*  But whatever. But I do believe that that there is something that goes beyond the realm of human understanding.
*  But but that that I can try to learn more about how to resonate with whatever that being would like me to do.
*  So you think you can have occasional glimpses of that being?
*  I strive for that.
*  Not that I ever think I'm going to get close to it.
*  But but it's not it's not for me.
*  It's it's saying what should I do that that being wants me to do?
*  That's that's I'm trying to ask.
*  What that I mean, does that being want me to be talking to Lex Friedman right now?
*  You know, and I said, yes.
*  OK, but thank you.
*  Well, thank you. But what I'm trying to say is I'm not trying to say what of all the strategies I could choose or something, which one?
*  I try to do it not not strategically, but I try to to imagine that I'm following somebody's wishes.
*  Even though you're not smart enough to know what they are.
*  Yeah. But that's the funny little dance.
*  Well, I mean, this AI or whatever is probably is smart enough to help to give me clues.
*  And to make the whole journey from clue to clue a fun one.
*  Yeah. I mean, it's as so many people have said, it's the journey, not the destination.
*  And people live, live through crises, help each other.
*  I think things come up. History repeats itself.
*  You try to say in the world today, is there any government that's working?
*  I read history. I know that things were.
*  They they were they were they were a lot worse in many ways.
*  There's a lot of bad things all the time.
*  And I read about, you know, I look at things and people had good ideas and they were working on great projects.
*  And then I know that it didn't succeed, though, in the end.
*  But but the new insight I've gotten, actually, in that way was I was reading.
*  What book was I reading recently? It was it was by Ken Follett.
*  It was called The Man from St. Petersburg.
*  But it but it was talking about the prequel to World War One.
*  And Winston Churchill, according to this book,
*  sees that that Germany has been spending all its gold reserves building up a huge military.
*  And there's no question that if Germany would attack England, that England would be wiped out.
*  So he wants Russia to help to attack Germany from the other side,
*  because Germany doesn't have enough of an army to be fighting two wars at one.
*  OK, now then there's an anarchist in Russia who sees that wars are something that leaders start, but actually people get killed.
*  And so he wants to stop any alliance between England and Russia,
*  because that would mean that thousands and thousands of people of Russia would be killed that wouldn't be otherwise killed.
*  All right. And so his his life's goal is to assassinate a Russian prince who's visiting England,
*  because that will make will mean the czar will not form the alliance. All right.
*  So we have this question about what should the government do?
*  Should it actually do something that will lead to is war is the war inevitable or is there a way to have peace?
*  And it struck me that if I were in a position of responsibility for people's lives,
*  in most cases, I wouldn't have I wouldn't have any confidence that any of my decisions were good,
*  that these these questions are too hard, probably for any human being, but certainly for me.
*  Well, I think I think coupling the not being sure that the decisions are right.
*  So that that's actually a really good thing, coupled with the fact that you do have to make a decision.
*  And carry the burden of that.
*  And ultimately, I have faith in human beings, in the great leaders to arise and help build a better world.
*  I mean, that's the hope of democracy.
*  Ben, let's hope that we can enhance their abilities with with algorithms.
*  Well put. It's such a huge honor.
*  You've been an inspiration to me and to millions for such a long time.
*  Thank you for spending your really valuable time with me once again.
*  It's a huge honor. I really enjoyed this conversation.
*  Thanks for listening to this conversation with Donald Knuth.
*  To support this podcast, please check out our sponsors in the description.
*  And now let me leave you with some words from Don Knuth himself.
*  Science is what we understand well enough to explain to a computer.
*  Art is everything else we do.
*  Thank you for listening. I hope to see you next time.
