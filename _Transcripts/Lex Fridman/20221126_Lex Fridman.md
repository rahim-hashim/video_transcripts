---
Date Generated: April 09, 2024
Transcription Model: whisper medium 20231117
Length: 11751s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'asyncio', 'coding', 'gil', 'guido van rossum', 'ide', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'mypy', 'parallelism', 'programming', 'python 3']
Video Views: 1249941
Video Rating: None
---

# Guido van Rossum: Python and the Future of Programming | Lex Fridman Podcast #341
**Lex Fridman:** [November 26, 2022](https://www.youtube.com/watch?v=-DVyjdw4t9I)
*  Can you imagine possible features that Python 4.0 might have that would necessitate the creation of the new 4.0,
*  given the amount of pain and joy, suffering and triumph that was involved in the move between version two and version three.
*  The following is a conversation with Guido Van Rossum, his second time on this podcast.
*  He is the creator of the Python programming language and is Python's Emeritus BDFL, benevolent dictator for life.
*  This is the Lex Friedman podcast.
*  To support it, please check out our sponsors in the description.
*  And now, dear friends, here's Guido Van Rossum.
*  Python 3.11 is coming out very soon.
*  In it, CPython claimed to be 10 to 60% faster.
*  How did you pull that off?
*  And what's CPython?
*  CPython is the last Python implementation standing, also the first one that was ever created.
*  The original Python implementation that I started over 30 years ago.
*  So what does it mean that Python, the programming language, is implemented in another programming language called C?
*  What kind of audience do you have in mind here?
*  People who know programming?
*  No, there's somebody on a boat that's into fishing and have never heard about programming, but also some world-class programmers.
*  So you're going to have to speak to both.
*  Imagine a boat with two people.
*  One of them has not heard about programming and is really into fishing.
*  And the other one is like an incredible Silicon Valley programmer that's programmed in everything.
*  C, C++, Python, Rust, Java, and knows the entire history of programming languages.
*  So you're going to have to speak to both.
*  I imagine that boat in the middle of the ocean.
*  Yes.
*  I'm going to please the guy who knows how to fish first.
*  Yes, please.
*  He seems like the most useful in the middle of the ocean.
*  You got to make him happy.
*  I'm sure he has a cell phone.
*  So he's probably very suspicious about what goes on in that cell phone, but he must have heard that inside a cell phone is a tiny computer.
*  And a programming language is computer code that tells the computer what to do.
*  It's a very low level language.
*  It's zeros and ones, and then there's assembly.
*  And then...
*  Oh yeah, we don't talk about these really low levels because those just confuse people.
*  I mean, when we're talking about human language, we're not usually talking about vocal tracts and how you position your tongue.
*  I was talking yesterday about how when you have a Chinese person and they speak English, this is a bit of a stereotype they often don't know.
*  They can't seem to make the difference well between an L and an R.
*  And I have a theory about that, and I've never checked this with linguists, that it probably has to do with the fact that in Chinese there is not really a difference.
*  And it could be that there are regional variations in how native Chinese speakers pronounce that one sound that sounds like L to some of them, like R to others.
*  So it's both the sounds you produce with your mouth throughout the history of your life and what you're used to listening to.
*  I mean, every language has that.
*  Russian has the Slavic languages have sounds like the letters like Americans or English speakers don't seem to know the sound.
*  They seem uncomfortable with that sound.
*  Yeah.
*  Oh, yes.
*  Okay.
*  So we're not going to the shapes of tongues and the sounds that the mouth can make.
*  Fine.
*  And similarly, we're not going into the ones and zeros or machine language.
*  I would say a programming language is a list of instructions like a cookbook recipe that sort of tells you how to do a certain thing.
*  Like make a sandwich.
*  Well, acquire a loaf of bread, cut it in slices.
*  Take two slices, put mustard on one, put the jelly on the other or something, then add the meat, then add the cheese.
*  I've heard that science teachers can actually do great stuff with recipes like that and trying to interpret their students' instructions incorrectly until the students are completely unambiguous about it.
*  With language, see, that's the difference between natural languages and programming languages.
*  I think ambiguity is a feature, not a bug in human spoken languages.
*  Like that's the dance of communication between humans.
*  Well, for lawyers, ambiguity certainly is a feature.
*  For plenty of other cases, the ambiguity is not much of a feature, but we work around it, of course.
*  What's more important is context.
*  So with context, the precision of the statement becomes more and more concrete.
*  Right.
*  But, you know, when you say, I love you to a person that matters a lot to you, the person doesn't try to compile that statement and return an error saying, please define love.
*  Right.
*  No, but I imagine that my wife and my son interpret it very differently.
*  Yes.
*  Even though it's the same three words.
*  But imprecisely still.
*  For sure.
*  Lawyers have a lot of follow up questions for you.
*  Nevertheless, the context is already different in that case.
*  Yes, fair enough.
*  So that's a programming language is ability to unambiguously state a recipe.
*  Actually, let's go back.
*  Let's go to Pepe.
*  You go through and Pepe, the style guy for Python code, some ideas of what this language should look like, feel like, read like.
*  And the big idea there is that code readability counts.
*  What does that mean to you?
*  And how do we achieve it?
*  So this recipe should be readable.
*  That's a thing between programmers.
*  Because on the one hand, we always explain the concept of programming language as computers need instructions and computers are very dumb and they need very precise instructions because they don't have much context.
*  In fact, they have lots of context, but their context is very different.
*  But what we've seen emerge during the development of software, starting in the probably in the late forties, is that software is a very social activity.
*  A software developer is not a mad scientist who sits alone in his lab writing brilliant code.
*  A software is developed by teams of people.
*  Even the mad scientist sitting alone in his lab can type fast enough to produce enough code so that by the time he's done with his coding, he still remembers what the first few lines he wrote mean.
*  So even the mad scientist coding alone in his lab would be sort of wise to adopt conventions on how to format the instructions that he gives to the computer.
*  So that the thing is, there is a difference between a cookbook recipe and a computer program.
*  The cookbook recipe, the author of the cookbook writes it once and then it's printed in 100,000 copies and then lots of people in their kitchens try to recreate that recipe, that particular pie or dish from the recipe.
*  And so there the goal of the cookbook author is to make it clear to the human reader of the recipe, the human amateur chef in most cases.
*  When you're writing a computer program, you have two audiences at once.
*  It needs to tell the computer what to do.
*  But it also is useful if that program is readable by other programmers, because computer software, unlike the typical recipe for a cherry pie, is so complex.
*  That you don't get all of it right at once.
*  You end up with the activity of debugging and you end up with the activity of...
*  So debugging is trying to figure out why your code doesn't run the way you thought it should run.
*  That means broadly, it could be stupid little errors or it could be big logical errors.
*  It could be anything.
*  Spiritual.
*  Yeah, it could be anything from a typo to a wrong choice of algorithm to building something that does what you tell it to do, but that's not useful.
*  Yeah, it seems to work really well 99% of the time, but does weird things 1% of the time on some edge cases.
*  That's pretty much all software nowadays.
*  All good software, right?
*  Well, yeah, for bad software.
*  That 99% goes down a lot.
*  But it's not just about the complexity of the program.
*  Like you said, it is a social endeavor in that you're constantly improving that recipe for the cherry pie.
*  But you're in a group of people improving that recipe.
*  Or the mad scientist is improving the recipe that he created a year ago and making it better.
*  Or adding adding something he decides that he wants.
*  I don't know, he wants some decoration on his pie or icing or.
*  So there's broad philosophical things in their specific advice on style.
*  So first of all, the thing that people first experience when they look at Python.
*  There is a it is very readable, but there's also like a spatial structure to it.
*  Can you explain the indentation style of Python and what is the magic to it?
*  Spaces are important for readability of any kind of text.
*  If you take a cookbook recipe and you remove all the sort of.
*  All the bullets and other markup and you just crunch all the text together,
*  maybe you leave the spaces between the words, but that's all you leave.
*  When you're in the kitchen trying to figure out, oh, what are the ingredients and what are the steps?
*  And where does this step end and the next step begin?
*  You're going to have a hard time if it's if it's just one solid block of text.
*  On the other hand, what what a typical cookbook does if the paper is not too expensive,
*  each recipe starts on its own page.
*  Maybe there is a picture next to it.
*  The list of ingredients comes first.
*  There's a standard notation.
*  There's there's shortcuts so that you don't have to sort of write two sentences on how you have to cut the onion,
*  because there are only three ways that people ever cut onions in a kitchen, small, medium and in slices or something like that.
*  Right. None of my examples make any sense to real cooks, of course.
*  Yeah, we're talking to programmers with the metaphor of cooking.
*  I love it. But there is a strictness to the spacing that Python defines.
*  So there's some. Looser things, some stricter things, but the four spaces for the for the indentation is really interesting.
*  It it really it really defines what language looks and feels like.
*  Because indentation sort of taking a block of text and then having inside that block of text,
*  a smaller block of text that is indented further as sort of a group.
*  It's it's it's like you have a bulleted list in a complex business document and inside some of the bullets are other bulleted lists.
*  You will indent those too. If each bulleted list is indented several inches,
*  then at two levels deep, there's no no space left on the page to put any of the words of the text.
*  You can't indent too far. On the other hand, if you don't indent at all,
*  you can tell whether something is a top level bullet or a second level bullet or a third level bullet.
*  So you have to have some compromise and based on ancient conventions and sort of the typical width of a computer screen in the 80s
*  and all sorts of things, sort of. We we came up with sort of four spaces as a compromise.
*  I mean, there are groups, there are large groups of people who code with two spaces per indent level.
*  For example, the Google Style Guide, all the Google Python code,
*  and I think also all the Google C++ code is indented with only two spaces per block.
*  If you're not used to that, it's harder to at a glance understand the code because the sort of the high level structure is determined by the indentation.
*  On the other hand, there are other programming languages where the indentation is eight spaces or a whole tap stop in sort of classic Unix.
*  And to me, that looks weird because you sort of after three indent levels, you've got no room left.
*  Well, there is some languages where the indentation is a recommendation, the stylistic one, the code compiles even without any indentation.
*  And then Python really indentation is a fundamental part of the language, right?
*  It doesn't have to be four spaces, so you can code Python with two spaces per block or four or six spaces or twelve if you really want to go wild.
*  But sort of everything that belongs to the same block needs to be indented the same way.
*  In practice, in most other languages, people recommend doing that anyway.
*  If you look at C or Rust or C++, all those languages, Java, don't have a requirement of indentation.
*  But except in extreme cases, they're just as anal about having their code properly indented.
*  So any IDE that the syntax highlighting that works with Java or C++, they will yell at you aggressively if you don't do proper indentation.
*  They'd suggest the proper indentation for you.
*  Like in C, you type a few words and then you type a curly brace, which is their notion of sort of begin an indented block.
*  Then you hit return and then it automatically indents four or eight spaces, depending on your style preferences or how your editor is configured.
*  Was there a possible universe in which you considered having braces in Python?
*  Absolutely, yeah.
*  What was the 60, 40, 70, 30 in your head?
*  What was the trade off?
*  For a long time, I was actually convinced that the indentation was just better.
*  Without context, I would still claim that indentation is better.
*  It reduces clutter.
*  However, as I started to say earlier, context is almost everything.
*  And in the context of coding, most programmers are familiar with multiple languages, even if they're only good at one or two.
*  And apart from Python and maybe Fortran, I don't know how that's written these days anymore, but all the other languages,
*  JavaScript, TypeScript, Perl are all using curly braces to sort of indicate blocks.
*  And so Python is the odd one out.
*  So it's a radical idea.
*  Do you still, as a radical renegade revolutionary, do you still stand behind this idea of indentation versus braces?
*  Like, what can you dig into a little bit more?
*  Why you still stand behind indentation?
*  Because context is not the whole story.
*  History, in a sense, provides more context.
*  So for Python, there is no chance that we can switch.
*  Python is using curly braces for something else, dictionaries mostly.
*  We would get in trouble if we wanted to switch.
*  Just like you couldn't redefine C to use indentation, even if you agree that indentation sort of in a greenfield environment would be better,
*  you can't change that kind of thing in a language.
*  It's hard enough to reach agreement over much more minor details.
*  I mean, in the past in Python, we did have a big debate about teps versus spaces and four spaces versus fewer or more.
*  And we sort of came up with a recommended standard and sort of options for people who want to be different.
*  But yes, I guess the thought experiment I'd like you to consider is if you could travel back through time when the compatibility is not an issue.
*  And you started Python all over again.
*  Can you make the case for indentation still?
*  Well, it frees up a pair of matched brackets of which there are never enough in the world for other purposes.
*  Really makes the language slightly.
*  Sort of easier to grasp for people who don't already know another programming language.
*  Because the sort of one of the things and I mostly got this from my mentors who.
*  Taught me programming language design in the earlier 80s when you're teaching programming.
*  For for the total newbie who has not.
*  Coded before it, not in any other language.
*  A whole bunch of concepts in programming are very alien or.
*  Sort of. New and and maybe very interesting, but also distracting and confusing, and there are many different things you have to learn.
*  You have to sort of. In a typical 13 week programming course, you have to.
*  If it's like really. Learning to program from scratch, you have to cover algorithms, you have to cover data structures, you have to cover syntax,
*  you have to cover variables, loops, functions, recursion, classes.
*  Expressions operators. There are so many concepts if you sort of.
*  If you can spend a little less time. Having to worry about the syntax that the classic example was often.
*  Oh, the compiler complains every time I put a semi column in the wrong place or I forget to put a semi column.
*  Python doesn't have semi columns in that sense, so you can't forget them and you are also not.
*  Sort of misled into putting them where they don't belong because you don't learn about them in the first place.
*  The flip side of that is forcing the strictness onto the beginning programmer to teach them that programming is.
*  Values attention to details you don't get to just write the way you write in English, any of other details that they pay attention to.
*  I think they'll they'll still get the message about paying attention to detail.
*  The interesting design choice, so I still program quite a bit in PHP and I'm sure there's other languages like this, but the dollar sign before a variable.
*  That was always an annoying thing for me.
*  It didn't quite fit into my understanding of why this is good for a programming language.
*  I'm not sure if you ever thought about that one.
*  That is a historical thing.
*  There is a whole lineage of programming languages.
*  PHP is one pearl was one on the union shell.
*  Is one of the oldest or all the different shells.
*  The dollar was invented for that purpose because the very earliest shells had a notion of scripting, but they did not have a notion of parameterizing the scripting.
*  And so a script is just a few lines of text where each line of text is a command that is read by a very primitive command processor that then sort of takes the first word on the line as the name of a program and passes all the rest.
*  Of the line as text into the program for the program to figure out what to do with as arguments.
*  And so by the time scripting was slightly more mature than the very first script.
*  There was a convention that just like the first word of line is the name of the program, the following words.
*  Could be names of files input dot text output dot html things like that.
*  The next thing that happens is oh it would actually be really nice if we could have variables and especially parameters for scripts parameters are usually what starts this process.
*  But now you have a problem because you can't just.
*  Say the parameters are x y and z and so now we call say let's say access the input file and why is the output file and let's forget about z for now.
*  I have my program and I write program x y well that already has a meaning because that presumably means x itself is the file.
*  It's a file name it's not a variable name.
*  And so the inventors of of things like the unique shell and I'm sure job command language in at IBM before that.
*  How to use something that made it clear to the script processor.
*  Here is an x that is not actually the name of a file which you just pass through to the.
*  To the program you're running here is an x that is the name of a variable and when you're writing a script processor you try to keep it as simple as possible.
*  Because at that as certainly in the 50s and 60s.
*  The thing that interprets the script was itself a very had to be a very small program because it had to fit in a very small part of memory and so saying oh.
*  Just look at each character and if you see a dollar sign you jump to another section of the code and then you gobble up characters are say until the next space or something and you say that's the variable name.
*  And so it was was sort of.
*  Invented as.
*  A clever way to make parsing of things that contain both contain both variable and fixed parts very easy in a very simple script processor it also helps even then it also helps the human author and the human reader of the.
*  The script.
*  To quickly see oh 20 lines down in the script I see a reference to xyz oh it has a dollar in front of it so now we know that xyz must be one of the parameters of the script was this fascinating several things to say which is.
*  The left over some the simple script processor languages are now in code bases like behind facebook or behind most of the back and I think php's probably still runs most of the back end of the internet oh yeah yeah I think there's a lot of it in wikipedia too for example.
*  It's funny that those decisions are not funny it's fascinating that those decisions permeate through time just like biological systems right.
*  I mean that the sort of the inner workings of dna.
*  Have been stable for well I don't know how long it was like 300 million years half a billion years.
*  And there there are all sorts of weird quirks there that don't make a lot of sense if you were to design a system like self replicating molecules from scratch.
*  What that system has a lot of interesting resilience has redundancy that results.
*  I can messes up an interesting ways that still is resilient when you look at the system level of the organism code doesn't necessarily have that program computer programming code.
*  You'd be surprised how much resilience modern code has.
*  I mean if you if you look at the number of bugs per line of code.
*  Even in in very well tested.
*  Code that in practice works just fine there actually lots of things that don't work fine.
*  And there are error correcting or self correcting mechanisms at many levels.
*  Including probably the user of the code well in the end the user who sort of is told well you gotta reboot your your pc is part of that system and a slightly.
*  Last drastic thing is reload page which we all know how to do without thinking about it when something weird happens you try to reload a few times before you say oh there's something really weird.
*  Or try to click the button again if the first time didn't work well yeah that we should all have learned not to do that because that's probably just gonna turn the light back off.
*  Yeah true to do it three times that's the that's the right lesson so.
*  And I wonder how many people actually like the dollar sign like you said it is documentation so to me it's whatever the opposite of syntactic sugars syntactic poison.
*  To me it is such a pain in the ass that after typing a dollar sign also super error prone.
*  So it's not self documenting it's it's like a bug generating thing it is a kind of documentation that's the pro and the con is it's a source of a lot of bugs but actually I have to ask you.
*  This is really interesting idea of bugs per line of code.
*  If you look at all the computer systems out there from the code that runs nuclear weapons to the code that runs all the amazing companies that you've been involved with and not go that runs twitter and facebook and dropbox and google and microsoft windows and so on.
*  And we like laid out.
*  Wouldn't that be a cool like table bugs per line of code and what would let's put like actual companies aside do you think we'd be surprised by the number we see there for all these companies.
*  That depends on whether you've ever read about research that's been done in this area before and.
*  And.
*  I don't know that the last time I saw some research like that there was probably in the nineties and the research might have been done in the eighties but the conclusion was across a wide range of different software different languages.
*  Different companies different development styles.
*  The number of bugs is always I think it's in the order of about one bug per thousand lines in sort of mature software that that is considered.
*  Interest as good as it gets can give you some facts here there's a lot of papers so you said mature software right so here's a.
*  A report from a programming analytics company.
*  Now this is from a developer perspective let me just say what it says this is very weird and surprising on average a developer creates 70 bugs per 1000 lines of code.
*  15 bugs per 1000 lines of code find their way to the customers.
*  This is in software they've always I was wrong by an order of magnitude there fixing a bug takes 30 times longer than writing a line of code that I can believe yeah 75% of a developers time is spent on debugging.
*  That's for an average developer date they analyze this 15 argue.
*  1500 hours a year in the US alone 113 billion dollars to spend annually on identifying and fixing bugs.
*  And I imagine this is marketing literature for someone who claims to have a golden bullet or silver bullet that makes all that investment in fixing bugs go away but that that is usually not going to that's not gonna happen.
*  What there are I mean they're referencing a lot of stuff of course but it is a page.
*  That is you know there's a contact us button at the bottom presumably if you just spend a little bit less than a hundred billion dollars were willing to solve the problem for you.
*  Right and there's also a report on stack exchanges that go on the exact same topic but when I open it up at the moment the page says stack or flows currently offline for maintenance.
*  Oh that is ironic yes by the way their error page is awesome anyway.
*  I mean can you believe that number of bugs oh absolutely is that scary the 70 bucks per 1000 lines of code so even 10 bucks per 1000 lines well that's about one bug after every 15 lines and that's when you're first typing it in.
*  I'm a developer but like how many bugs are going to be found.
*  If you're if you're typing well the development process is extremely iterative typically you don't make a plan for what software you're going to release a year from now.
*  And work out all the details because actually all the details themselves consist.
*  They sort of compose a program.
*  And that's that.
*  Being a program all your plans will have bugs in them too and inaccuracies.
*  But what what you actually do is.
*  You do a bunch of typing and I'm actually really I'm a really bad typist that just I've never learned to type with 10 fingers.
*  I need to use.
*  Well I use all 10 of them but not very well but I never I never took a typing class and I never sort of corrected that so the first time I I seriously learned.
*  I had to learn the layout of a of a qwerty keyboard was actually in college in my first programming classes where we used punch cards.
*  And so with my two fingers I sort of packed out my code.
*  What anyone give you a little coding demonstration they'll have to produce like four lines of code.
*  And now see how many times they use the backspace key yeah because they made a mistake and and and some people especially when when someone else is looking.
*  Will will backspace over 2030 40 characters to fix a typo earlier in the line if you're.
*  If you're slightly more experience of course you use your arrow buttons to go or your mouse to but the mouse is usually slower than than the arrows.
*  But a lot of people when they type a 20 character word which is unusual and they realized they made a made a mistake.
*  The backspace over the whole thing and then we type it and sometimes it takes 34 times to get it right so.
*  I don't know what your definition of bug is arguably miss typing a word and then correcting it immediately is not a bug on the other hand you you already.
*  Do sort of lose time and every once in a while there's sort of a typo that you don't get.
*  And now you've you've you've typed like 10 lines of code.
*  And somewhere in the middle of it you don't know where yet is a typo or maybe a think oh where you you forgot that you had to initialize a variable or something.
*  But those are two different things and I would say yes you have to actually run the code to discover that typo but forgetting to initialize a variable is a fundamentally different.
*  Thing because that thing can go on discovered that depends on the language in python it will not write in sort of modern compilers are usually pretty good at catching that even even foresee so for that specific thing but actually deeper.
*  It might there might be another variable that his initialize but logically speaking the one you meant related yep domain.
*  It's like name the same but it's a different thing and you forgot to initialize whatever some counter or some some basic variable they're using I can tell that you've coded yes.
*  Which has the backspace under the thumb and one of the biggest reasons I use that keyboard is because you realize in order to use the backspace unusual keyboard you have to stretch your pinky out.
*  Which has the backspace under the thumb and one of the biggest reasons I use that keyboard is because you realize in order to use the backspace unusual keyboard you have to stretch your pinky out.
*  Like the foremost normal keyboards the backspace is under the pinky so I don't know if people realize the pain they go through in their life.
*  Because of the backspace keeping so far away so with the kinesis is right under the thumbs you don't have to actually move your hands the backspace in the what what do you do if you're ever not with your own keyboard and you have to use someone else's pc keyboard that has.
*  A standard layout so first of all it turns out that you can actually go your whole life always having the keyboard.
*  But you so this well except for that that little tablet that you're using sort of note taking right now right yeah so it's very inefficient note taking but I'm not I'm just looking stuff up.
*  But in most cases I would be actually using the keyboard here right now I just don't anticipate you have to calculate how much typing do you anticipate.
*  I anticipate quite a bit then I'll just I have a keyboard people with me and same same with the I mean the embarrassing.
*  I've accepted being the weirdo that I am but you know when I go on an airplane and I anticipate to do programming or a lot of typing.
*  I will have a laptop that will pull out a kinesis keyboard in addition to the laptop and it's just quite yet you have to accept who you are.
*  But also it's a you know for a lot of people for me certainly there's a comfort space where there's a certain kind of setups that are maximize productivity and.
*  It's like some people have a warm blanket that they like when they watch a movie I like the kinesis keyboard takes me to a place of focus and I still mostly.
*  I am trying to make sure I use the state of the art ideas for everything but my comfort place just like the kinesis keyboard is still e max.
*  So I still use I still I mean that's one of some of the debates I have with myself about everything from a technology perspective.
*  Is how much to hold on to the tools you're comfortable with versus how much to invest in using modern tools and the signal that the communities provide you with.
*  Is the noisy one because a lot of people year to year get excited about new tools and you have to make a prediction are these tools defining a new generation of something that will transform programming or is this just a fad that will pass.
*  Certainly with javascript frameworks and front and the back end of the web there's a lot of different styles that came and went.
*  I remember learning.
*  What was it called action script I remember for flash.
*  I'm learning how to program and flash learning how to design to graphic animation all that kind of stuff flash same with java applets remember creating quite a lot of java applets thinking that this potentially defines the future of the web.
*  I did not well you know in most cases like that the particular technology eventually gets replaced.
*  But many of the concepts that the technology introduced or made accessible first.
*  I preserved of course because yeah we're not using java applets anymore but the notion of reactive web pages.
*  That sort of contain little bits of code that respond directly to.
*  Something you do like pressing a button or a link or hovering even.
*  I have certainly not gone away and that those animations that were made painfully.
*  Complicated with flash i mean flash was an innovation when it first came up and when it was replaced by javascript equivalence stuff.
*  It was a somewhat better way to do animations but those animations are still there not all of them but but sort of.
*  Again there is an evolution and often so often with technology.
*  The sort of the technology that was eventually thrown away or replaced was still essential to to sort of get started there wouldn't be jet planes without propeller planes.
*  I got you but from a user perspective yes from the feature set yes but I from a programmer perspective it feels like.
*  All the time I spent with action script all the time I spent with java on the applet side for the good development I well no java I have to push back that that was useful.
*  That because it transfers but the flash doesn't transfer so some things you learn invest time and what yeah what what you learned this kit the skill you picked up learning action script.
*  What sort of it was perhaps a super valuable skill at the time you picked it up if you if you learned action script early enough.
*  But that skill is no longer in demand with us the calculation you have to make when you're learning new things like today people start learning programming today i'm trying to see what are the new languages to try what are the new systems to try that what are the new ideas to try to keep keep improving.
*  That's that's why we start when we're young right when we're not but that seems very true to me that that when you're young you have your whole life ahead of you and you're.
*  You're allowed to make mistakes in fact you should you should feel encouraged to to do a bit of stupid stuff yeah try not to get yourself killed or seriously maimed but try stuff that.
*  Deviate from from what everybody else is doing.
*  And like nine out of ten times you'll just learn why everybody else is not doing that everybody else doing it some other way and one out of ten times you sort of.
*  You discover something that's better or that's that somehow works I mean there are all sorts of crazy things that were invented.
*  By accident by people trying trying stuff together that's great advice to try random stuff make a lot of mistakes once you're married with kids you're probably going to be a little more risk averse because now there's more at stake and you've already hopefully had some time where you were experimenting with crazy shit.
*  I like how marriage and kids solidifies your choice of programming language how does that the Robert Frost poem with the the road less taken.
*  Which I think is misinterpreted by most people but anyway I feel like the choices you make early on especially if you go all in they're going to define the rest of your life's trajectory in a way that.
*  Like you basically are picking a camp so.
*  You know there's if you invest a lot in php if you invest a lot in dot net if you invest a lot in javascript.
*  You're going to stick there.
*  You that's that's your life journey it's very hard to only as far as that technology remains relevant yes yes I mean if if at age 16 you learn coding in C.
*  And by the time you're 26 C is like a dead language.
*  Then there's still time to switch there's probably some kind of survivor bias or whatever it's called in in sort of your observation that that you pick a camp because there are many different camps to pick and if you pick dot net then.
*  Then you can coast for the rest of your life because that's the technology is now so ubiquitous of course that it's even if it's if it's bound to die it's going to take a very long time well for me personally.
*  I had a very difficult and in my own head brave leap that I had to take relevant to our discussion which is most of my life I programmed the scene C++ and so.
*  I having that hammer everything look like a nail so I would literally even do scripting in C++.
*  I don't create programs I do script like things and when I first came to Google and before then it became already before tensile for before all of that there was a growing realization that C++ is not the right tool for machine learning.
*  We can talk about why that is it's unclear why that is a lot of things has to do with community and culture and how to emerges and stuff like that but.
*  For me to decide to take the leap to python like all out basically switch completely from C++ except for.
*  Highly performant robotics applications are still.
*  There's still a culture of C++ in the space of robotics.
*  That was a big leap.
*  Like I had to you know like like people have like existential crises or midlife crisis whatever it to realize almost like walking away from a person you love.
*  Because I was sure that C++ would have to be a lifelong companion for a lot of problems I would want to solve C++ would be there and it was a question to say well.
*  That might not be the case because people still one of the most popular languages in the world one of the most used one of the most dependent on it's also still evolving quite a bit I mean.
*  That that is not a sort of a fossilizing community yes they are doing great innovative work actually a lot but yet that sort of their innovations are hard to follow if you're not already a hard core C++ user.
*  What this was the thing it pulls you in it's a rabbit hole I was a hardcore the all metaprogramming template programming like I would start using the modern C++ as it developed.
*  Right now just the not not just the shared pointer in the garbage collection that makes it easier for you to work with some of the flaws.
*  But the detail like the metaprogramming the the crazy stuff that's that's coming out there but then you have to just empirically look and step back and say what language am I more productive in.
*  Sorry to say what language do I enjoy my life with more and readability and able to think through and all that kind of stuff that those questions are harder to ask when you already have.
*  A loved one which in my case a C++ and then there's Python like that meme was the grass is greener on the other side am I just infatuated with a new fad new cool thing.
*  Or is this actually going to make my life better and I think a lot of people face that kind of decision it was a difficult decision for me.
*  When I made it at this time it's an obvious switch if you're into machine learning but that time it wasn't quite yet so obvious it was a risk and you know you have the same kind of stuff with them.
*  I still because of my connection WordPress.
*  I still do a lot of back ended programming in PHP.
*  And the question is you know no J.S. Python do you switch to do you switch back into any of those.
*  Programming is it there's the case for no J.S. for me well more more more of the front end it runs in JavaScript.
*  And fascinating cool stuff is that is JavaScript maybe use the same programming language for the back end as well.
*  The case for Python for the back end is well you're doing so much programming outside of the web in Python so maybe use Python for the back end and then the case for PHP well most of the web still runs in PHP.
*  You have a lot of experience with PHP.
*  Why fix something that's not broken those are my personal struggles but I think they reflect the struggles of a lot of people with different programming languages with different problems are trying to solve it's a weird one.
*  And there's not a single answer right because depending on how much time you have to learn new stuff where you are in your life what what you're currently working on who you want to work with what communities you like.
*  There's not one right choice maybe if you if you sort of.
*  If you can look back 20 years you can say well that whole detour through action script was a waste of time but.
*  Nobody could know that so you can you can beat yourself up over that.
*  You just need to accept that not every choice you make is going to be perfect maybe sort of keep plan B in the back of your mind.
*  But don't don't overthink it don't don't try to sort of don't.
*  Don't don't try to sort of don't.
*  Don't create a spreadsheet with like we're trying to estimate well if I learn this language I expect to make X million dollars in a lifetime and if I learned that language I expect to make Y million dollars in a lifetime and which which is higher and what which has more risk and where's the chance that it's like picking picking a stock.
*  Kind of kind of but.
*  I think with stocks you can do diversifying your investment is good with productivity in life.
*  Boy that spreadsheet is possible to construct.
*  Like if you actually carefully analyze what your interests in life are where you think you can maximally impact the world.
*  There really is better and worse choices for programming language they're not just about the syntax but about the community about where you predict the communities headed.
*  What's large systems are programmed in that but can you create that spreadsheet because that's sort of you're mentioning a whole bunch of inputs that go into that spreadsheet where you have to estimate things that are very hard to measure and even harder I mean they're they're hard to measure.
*  Retroactively and they're even harder to predict like what is the better community well better is is one of those.
*  Incredibly difficult words what's better for you is not better for someone else but we're not doing a public speech about what's better we're doing a personal spiritual journey I can determine a circle of friends.
*  Circle circle one and circle two and I can have a bunch of parties with one and bunch of parties with two and then write down or take a mental note of what made me happier right and that you know you have.
*  If you're a machine learning person you want to say OK I want to build a large company that does that is grounded in machine learning but also has a sexy interface that has a large impact in the world what languages do I use.
*  You look at what Facebook is using you look what Twitter is using then you look at performant more newer languages like rust or you look at languages that have taken that most the community uses in machine learning space that's python.
*  You can like think through you can hang out and think through it and it's always a invest and the the level of activity of the community is also really interesting like you said c++ and python a super active.
*  In terms of the development of the language itself but do you think that you can make.
*  Objective choices there no no no but there's a gut you build up like don't you don't you believe in that gut feeling everything is very subjective and yes you most certainly can have a gut feeling and your gut can also be wrong that's why there are billions of people because they're not all right.
*  I mean clearly there are more people living in the Bay area who have plans to sort of create a Google sized company then there's room in the world for Google sized companies and they're gonna have to duke it out in the market.
*  The space and there's many more choices than just the programming language speaking of which let's go back to the boat with the with the fisherman who's tuned out long ago.
*  The programmer let's jump around and go back to see python that we tried to define as the reference implementation and one of the big things that's coming out in three dot eleven was the right way to we tend to say three dot eleven because it really was like.
*  We went three dot eight three dot nine three dot ten three dot eleven and are planning to go up to three dot ninety nine.
*  Nine nine what happens after ninety nine probably just three dot one hundred one five make it there okay and go all the way to four twenty I got it forever python v3 we'll talk about four but more for fun.
*  So three dot eleven is coming out one of the big sexy things in it is it'll be much faster so how did you beyond hiring a great team or working with a great team make it faster what are some ideas that me makes it faster.
*  It has to do with simplicity of software versus performance and so even though see is known to be a low level language which is great for writing sort of a high performance language interpreter.
*  When I originally started python or see python I didn't expect there would be.
*  Great success and fame in my future.
*  So I.
*  I try to get something working and useful.
*  In about three months and so I sort of I cut corners.
*  I borrowed ideas left and right when it comes to language design as well as implementation.
*  I also wrote much of the code as simple as it could be.
*  And.
*  There are there are like there are many things that you can code more efficiently by adding more code.
*  It's a bit of a sort of a time space trade off.
*  Where you can compute a certain thing from a small number of inputs.
*  And every time you get presented with new input.
*  I you do the whole computation from the top.
*  That can be simple looking code it's easy to understand it's easy to reason about that you can you can tell quickly that it's correct in at least in the sort of mathematical sense of correct.
*  Because it's implemented in see maybe it performs relatively well.
*  But overtime as sort of.
*  As the requirements for that code and the need for performance go up.
*  You might be able to rewrite that same algorithm using more memory maybe remember previous results.
*  So you don't have to recompute everything from scratch like the classic example is computing prime numbers.
*  Like.
*  Is 10 a prime number.
*  Well you sort of is it divisible by 2 is it divisible by 3 is it divisible by 4 and we go all the way to is a divisible by 9.
*  And it is not well actually 10 is divisible by 2 so that we stop but say 11 is divisible by 10 the answer is 9 is no 10 times in a row so now we know 11 is a prime number.
*  On the other hand if we already know that 235 and 7 are prime numbers and you know a little bit about the mathematics of.
*  How prime numbers work you know that if you have a rough estimate for the square root of 11 you don't actually have to check is it divisible by 4 or is it divisible by 5 you all you have to check in the case of 11 is is divisible by 2 is it divisible by 3.
*  Because take 12.
*  If it's divisible by 4 or 12 divided by 4 is 3 so you you should have come across the question is it divisible by 3 first.
*  So if you know basically nothing about prime numbers except the definition maybe you go for X from 2.
*  Through n minus 1 is n divisible by X and then at the end if you got all nose for every single one of those questions.
*  You know oh it must be a prime number well the first thing is you can stop it rating when you find a yes answer and the second is you can also stop iterating when you had have reached.
*  The square root of n because you know that if it has a divisor larger than than the square root and also have a divisor smaller than the square root.
*  Then you say oh except for 2 we don't need to bother with checking for even numbers because all even numbers are divisible by 2 so if it's divisible by 4.
*  We would already have come across the question is it divisible by 2 and so now you go special case check is it divisible by 2 and then you just check 35711.
*  And so now you you sort of reduced your search space by 50% again by by skipping all the even numbers are kept for 2.
*  If you think a bit more about it or you just.
*  Read in your book about the history of math one of the first algorithms ever written down all you have to do is check is it divisible by any of the previous prime numbers that are smaller than the square root.
*  And before you get to a better algorithm than that.
*  You have to have several PhDs in in discrete math so that's as much as I know.
*  So of course that same story applies to a lot of other algorithms string matching is a good example of how to come up with an efficient algorithm and sometimes yeah.
*  The more efficient algorithm is not so much more complex than the inefficient one but that's an art and it's not.
*  Always the case in the general cases the more perform at the algorithm the more complex is going to be there's a there's a kind of trade off.
*  The simpler algorithms are also the ones that people invent first because when you're looking for a solution.
*  You look at the simplest way to get there first and so if there is a simple solution.
*  Even if it's not the best solution not the fastest or the memory most memory efficient or whatever.
*  A simple solution and simple is is fairly subjective but mathematicians have also thought about sort of what is a good definition for simple in the case of algorithms.
*  But the simpler the simpler solutions tend to be easier to follow for other programmers who haven't made a study of a particular field and when I when I started with python I.
*  I was a good programmer in general I knew sort of basic data structures and knew the sea language pretty well but there were many areas where I was.
*  Only somewhat familiar with the state of the art.
*  And so I picked in many cases the simplest way I could solve a particular sub problem because when you when you're designing and implementing a language you have to like.
*  You have many hundreds of little problems to solve and you have to have solutions for every one of them before you can can sort of say I've invented a programming language.
*  First of all so see python what kind of things does it do to an interpreter it takes in this readable language that we talked about this python.
*  What is this supposed to do the interpreter basically it's it's sort of a recipe for understanding recipes.
*  So instead of a recipe that says bake me a cake we have a recipe for well given the text of a program.
*  How do we run that program and and that is sort of the recipe for building a computer the recipe for the Baker and the chef yeah what are the algorithmically tricky things that.
*  Happy to be low hanging fruit that could be improved on maybe throughout the history of python but also now how is it possible that three dot eleven in year twenty twenty two it's possible to get such a big performance improvement.
*  We focused.
*  On a few areas where we we still felt there was low hanging fruit.
*  The biggest one is actually the interpreter itself and this has to do with details of how python is defined so I didn't know if the fisherman is going to follow this story here he already jumped off the boat he's he's he's this.
*  I'm bored yeah stupid python is actually even though it's always called an interpreted language it's there's also a compiler in there it just doesn't compile to machine code it compiles to.
*  By code which is sort of code for an imaginary computer that is called the python interpreter so it's compiling code that is more easily digestible by the interpreter or is digestible at all it is the code that is digested by the interpreter
*  that's the compiler we tweaked very minor bits of the compiler almost all the work was done in the interpreter because.
*  When you have a program you compile at once and then you run the code a whole bunch of times or maybe there's one function in the in the code that gets run many times.
*  Now I know that that sort of people who who know this field are expecting me to at some point say we built a just-in-time compiler actually we didn't we just made the interpreter a little more efficient.
*  What's a just-in-time compiler that is a thing from the Java world although it's now applied to almost all.
*  Programming language is especially interpreted once so you see the components that part are not like a just-in-time compiler but is a compiler that creates by code that is then.
*  Fed to the interpreter and the compiler.
*  What is there something interesting to say about the compiler it's interesting that you haven't changed that tweet that at all or much we changed some parts of the byte code.
*  But not very much and so we only had to change the parts of the compiler where we decided that the breakdown of a python program in byte code instructions had to be slightly different.
*  But.
*  That did that didn't gain us the performance improvements that performance improvements were like making the interpreter faster in part by sort of.
*  Removing the fat from some internal data structures used by the interpreter but.
*  The key idea is an adaptive specializing interpreter.
*  Let's go what is adaptive about it what is specialized about it well let me first talk about the specializing part because that adaptive part is the sort of.
*  The second order effect but they're both important so byte code is a bunch of machine instructions but it's an imaginary machine but the machine can do things like call a function.
*  Add two numbers print a value.
*  Those are sort of typical instructions in python.
*  I and if we take the example of adding two numbers.
*  Actually in python the language there's no such thing as adding two numbers there's just an the compiler.
*  Doesn't know that you're adding two numbers you might as well be adding two strings or two lists.
*  Or two instances of some user defined class that happened to implement this operator called add.
*  That's a very interesting and fairly powerful mathematical concept it's mostly a user interface trick because it means that.
*  A certain category of functions.
*  Can be written using a symbols single symbol the plus sign and sort of a bunch of other functions can be written using another single symbol the multiply sign.
*  So if we take addition the way traditionally in python the add byte code was executed is.
*  Pointers pointers and more pointers.
*  So first we we we have two objects an object is basically a pointer to a bunch of memory that contains more pointers pointers all the way down.
*  Well not quite but there there are a lot of them so to simplify a bit we look up in one of the objects.
*  What is the type of that object and does that object type define an add operation.
*  And so you can imagine that there is a sort of a type integer that knows how to add itself to another integer.
*  And there is a type floating point number that knows how to add itself to another floating point number.
*  And the integers of floating point numbers are sort of important i think mostly historically because in the first computers.
*  Use the sort of the same bit pattern when interpreted as a floating point number had a very different value than when interpreted as an integer.
*  Can I ask a dumb question here please do given the basics of intent float and add who carries the knowledge of how to add two integers is it the integer.
*  It's the type integer versus it's the type integer and the type float what about the operator is the operator.
*  Just exist as a platonic form possessed by the integer the operator is more like.
*  It's an index in a list of functions that the integer type defines and so the integer type.
*  Is really a collection of functions and there is an add function and there's a multiply function and there are like 30 other functions for other operations this power function, for example.
*  And you can imagine that in in memory there is a distinct slot for the add operations let's say the add operation is the first operation of a type and the multiply is the second operation of a type.
*  So now we take the integer type and we take the floating point type.
*  In both cases the add operation is the first slot and multiply is the second slot but.
*  Each slot contains a function and the functions are different because the the add to integers function interprets the bit patterns as integers the add to float.
*  Function interprets that the same bit pattern as as a floating point number and then there is the string data type which again interprets the the bit pattern as.
*  The address of a of a sequence of characters there are lots of lies in that story but that's that's sort of a basic idea.
*  I could tell the fact the fake news and the fabrication going on here at the table but where's the optimization is it on the operators is that different.
*  So the integer optimization is the observation that.
*  In a particular line of code.
*  In a particular line of code.
*  So now you you write your little python program and you write a function and that function sort of takes a bunch of inputs and at some point it adds two of the inputs together.
*  Now i bet you even if you call your function a thousand times that all those calls are likely all going to be about integers because maybe your program is all about integers or maybe.
*  On that particular line of code where that there's that plus operator.
*  Every time the program hits that line the variables a and b that be are being added together happen to be strings.
*  And so what we do is instead of having this single byte code that says here's an ad operation and the implementation of add is fully generic it looks at the object from the object it looks at the type.
*  Then it takes the type and it looks at looks up the function pointer then it calls the function now the function has to be has to look at the other argument and has to double check that the other argument has the right type.
*  And then there's a bunch of air checking before it can actually just go ahead and add the two bit patterns in the right way what we do is.
*  Every time we execute an add instruction like that.
*  We we keep a little note of.
*  In the end after after we hit the code that that did the addition for a particular type what type was it.
*  What type was it.
*  And then after a few times through that code if it's this if it's the same type all the time.
*  I we say oh so this ad operation even though it's the generic ad operation it might as well be the ad integer operation.
*  Add integer operation is much more efficient because it just says assume that a and b are integers do the addition operation do it right there in line and produce the result.
*  And the big lie here is that in python even if you have great evidence that in the past it was always two integers that you were adding.
*  At some point in the future that same line of code could still be hit with two floating points or two strings or maybe a string and an integer.
*  That's not a great lie that's just the fact of life.
*  I didn't account for what what should happen in that case in in the way I told the story there is some accounting for and and so what do we actually have to do is when we have the add integer operation.
*  We still have to check are the two arguments in fact integers we applied some tricks to make those checks efficient and we know statistically that the outcome is almost always yes they were they are both integers.
*  Add and so we quickly make that check and then we proceed with the sort of add integer operation and then there is a fallback mechanism where we say.
*  Oops one of them wasn't an integer now we're going to pretend that there was just the fully generic ad operation we wasted a few cycles believing it was.
*  What was going to be two integers and then we had to back up but we didn't waste that much time and statistically most of the time.
*  Basically we were sort of hoping that most of the time we guess right because if we if it turns out that we guessed wrong too often.
*  Or we didn't have a good guess at all things might actually end up running a little slower so someone with aren't with this knowledge.
*  And a copy of the implementation someone could easily construct a counter example where they say oh I have a program and now it runs five times as slow in python 311 than it did in python 310.
*  But that's a very unrealistic program that's that's just like an extreme fluke.
*  It's a fun reverse engineering task though so there's a.
*  People like fun yes so there's some presumably heuristic of what defines the momentum.
*  Of saying you know you seem to be working adding two integers not to generic types so how do you figure out that heuristic.
*  I think that the heuristic is actually we assume that the weather tomorrow is going to be the same as the weather today.
*  Do you need two days of the weather no.
*  That is already so much better than than than guessing randomly that so how do you find this idea.
*  Hey I wonder if instead of adding to generic types we start assuming that the weather tomorrow the same as the weather today where do you find the idea for that because that ultimately.
*  For you to do that you have to kind of understand how people are using the language right python is not the first language to do a thing like this this is a fairly well known trick especially from.
*  Other interpreted languages that had reason to be sped up we occasionally look at papers about hhvm which is for facebook's.
*  Efficient compiler for php there are tricks known from the jvm and sometimes it just comes from academia.
*  The trick here is that the type itself doesn't the variable doesn't know what type it is.
*  So this is not a statically typed language where you can you can get that sort of have a shortcut to saying it's in this is a trick that is especially important for.
*  For interpreted languages with dynamic typing because if if the compiler could read in the source these x and y that were adding our integers the compiler can just insert the single add machine code that.
*  Hardware machine instruction that exists on every cpu and did over floats.
*  The types of your variables you you don't even declare the existence of your variables they just spring into existence when you first assigned them.
*  Which is really cool and sort of helps those beginners because there is less bookkeeping they have to learn how to do before they can start playing around with code.
*  Because there is less bookkeeping they have to learn how to do before they can start playing around with code but it makes the interpretation of the code less efficient and so we're sort of.
*  Trying to.
*  To make the interpretation more efficient without losing the the super dynamic nature of the language that's always the challenge.
*  3.5 got the pep for the four type hints what is type hinting and.
*  Is it used by the interpreter the hints or is it just in tactic sugar so the type hints is an optional mechanism that people can use and it's especially popular with sort of.
*  Larger companies that have very large code bases written in python do you think of it is almost like documentation saying these two variables are this time more than documentation i mean so it.
*  It is a sub language of python where where you can express the types of variables so here's a variable and it's an integer.
*  And here's an argument to this function and it's a string and here is a function that returns a list of strings but that's not checked when you run the but.
*  Exactly there there is a separate piece of software called a static type checker that reads all your source code without executing it and things long and hard about.
*  What it looks from just reading the code that code might be doing and double checks if that makes sense if you take the types as annotated into account.
*  So this is something you're supposed to run as you develop it's like a linter yeah that's definitely a development tool but the type annotations currently are not used for.
*  Speeding up the interpreter and there are a number of reasons many people don't use them even when they do use them.
*  They sometimes contain lies where the static type checker says everything's fine.
*  I cannot prove that this integer is ever not an integer but at runtime somehow someone manages to violate that assumption.
*  And the interpreter.
*  Ends up doing just fine if we started enforcing type annotations in python many python programs would no longer work.
*  And some python programs wouldn't even be possible because they're too dynamic.
*  So we made we made a choice of not using the annotations there there is a possible future where eventually.
*  345 releases in the future we could start using those annotations to sort of.
*  Provide hints because we can we can still say well the source code leads us to believe that these X and Y are both integers and so we can generate an add an add integer instruction.
*  But we can still have a fallback that says oh if the if somehow the code coded runtime provided something else maybe it provided two decimal numbers.
*  We can still use that generic add operation as a fallback but we're not there is there currently a mechanism or do you see something like that we can almost add like an assert.
*  Inside a function that says please check that my type hints are actually mapping to reality sort of like insert manual static typing there are third party libraries that.
*  Are in that business it's possible to do that kind of thing it's possible to for a third party library to take a hint.
*  And enforce it.
*  What we actually do is and this I think this is a fairly unique feature in python the type hints can be introspective at runtime so while the program is running.
*  They mean python is a very introspectable language you can look at the variable and ask yourself what is the type of this.
*  This variable and if that baby that variable happens to refer to a function you can ask what are the arguments to the function.
*  And nowadays you can also ask what are the type annotations for the function so the type annotations are there inside the variable as it's at runtime.
*  They're mostly associated with the function object not with each individual variable but you can sort of map from from the arguments to the variables and that's what a third party library can exactly and the problem with that is that all that extra runtime type checking.
*  Is going to slow your code down instead of speed it up I think the reference this.
*  Sales pitchy blog post that says 75% of developers time is spent on debugging I would say that in some cases that might be okay it might be okay to pay the cost of performance for the catching of the types the type errors.
*  And in most cases doing it.
*  Statically before you ship your code to production is more efficient than doing it at runtime piecemeal.
*  Can you tell me about.
*  NYP Y my project what is it what's the mission and in general what is the future of a static typing in python.
*  What's up my pie was started by a finish developer you call let us know.
*  So many cool things out of Finland I gotta say just that part of the world I guess people have nothing better to do in those long cold winters.
*  I don't know I think you can live in England when he invented that stuff actually but.
*  My pie is the original static type checker for python and the type annotations that were introduced with pet for 84.
*  Where sort of developed together with the static type checker and in fact you can had first invented a different syntax that wasn't quite compatible with python.
*  And you can I sort of met at the python conference in I think in 2013.
*  And we we sort of came up with a compromise syntax.
*  That would not require any changes to python and that would let my pie sort of be an add on static type checker for python.
*  Just out of curiosity was like double colon or something what was he proposing that would break python.
*  I think he was using angular brackets for types like in c++ or Java generics.
*  Yeah you can't use angular brackets in python it would be too tricky.
*  For well we that the key thing is that we already had a syntax for annotations we just didn't know what to use them for yet.
*  So type annotations were just the sort of most logical thing to to use that existing dummy syntax for.
*  So there was no there was no syntax for defining generics directly syntactically in the language my pie literally meant my version of python where my it refers to you.
*  He had a parser that translated my pie into python by like doing the type checks and then removing the annotations and all the angular brackets from the positions where where he was using them.
*  But a pre processor model doesn't work very well with the typical workflow of python development projects.
*  That's funny I mean that could have been another major split if it became successful like if you watch typescript versus javascript.
*  Is it like a split in the community over types right that seems to be stabilizing now.
*  It's not necessarily a split there are certainly plenty of people who don't use typescript but.
*  Just use the original javascript notation just like there are many people in the python world who don't use type annotations and don't use static type checkers.
*  Now I know but there is a bit of a split between typescript and javas old school javascript yes whatever.
*  Well in the javascript world transpilers are sort of the standard way of working anyway which is why typescript being a transpiler itself is not a big deal.
*  And transpilers for people who don't know it's exactly the thing you said with mypies it's the code I guess you call pre processing code that translates from one language to the other and that's part of the culture part of the workflow of the javascript community.
*  That's right at the same time an interesting development in the javascript slash typescript world at the moment is that.
*  There is a proposal under consideration it's only a stage one proposal that proposes to add a feature to javascript where just like python it will ignore certain syntax.
*  When running the javascript code and what it ignores is more or less a superset of the typescript annotation syntax.
*  It's just so that would mean that eventually if you wanted to you could take typescript.
*  And you could shove it directly into javascript interpreter without translation.
*  The interesting thing in the javascript world at least the web browser world.
*  The web browsers have changed how they deploy and they they sort of update their javascript engines.
*  Much more quickly than they used to in the early days and so there's much less of a need for.
*  Translation in javascript itself because most browsers just support the most recent version of a script.
*  Just an attention of attention do you see if you recommend somebody use a thing would you recommend typescript to javascript.
*  I would recommend typescript just because of the strictness of the typing it's.
*  An enormously helpful extra tool that helps you sort of.
*  Keep your head straight about what your code is actually doing.
*  I mean it's it's it it helps with editing your code it helps with ensuring that your code.
*  Is not too incorrect.
*  And it's actually.
*  Quite compatible with javascript nevermind this syntactic sort of hack that is still years in the future.
*  But any library that is written in pure javascript can still be used from typescript programs.
*  And also the other way around you can write a library in typescript.
*  And then export it in a form that is totally consumable by javascript.
*  That sort of compatibility is is sort of the key to this to the success of typescript.
*  Yeah just to look at is almost like a biological system that's evolving it's fascinating to see javascript of all the way it does.
*  Well maybe we should consider that biological systems are just engineering systems to write yes.
*  Very advanced with with more history but it's almost like the most visceral in the javascript world because there's just so much code written in javascript.
*  That for its history was messy if you talk about bugs per line of code i just feel like javascript.
*  It's the cake or whatever the terminology is it beats python by a lot in terms of number of bugs meaning like way more bugs in javascript.
*  And then and then the obviously the browsers are developing just there's so much active development it feels a lot more like evolution.
*  Where a bunch of stuff is born and dies and there's experimentation and debates versus python is more.
*  All that stuff is happening but there's just a longer history of stable working giant software systems written in python versus javascript is just a giant beautiful i would say mess of code it's very different culture and.
*  To some extent differences in culture are random but to some extent they the differences have to do with the environment.
*  And the fact that javascript is primarily.
*  The language for developing web applications especially the client side and the fact that it's basically the only language for developing web applications.
*  Makes that community sort of just have a different nature than the community of other languages.
*  Plus the graphical component and the fact that they're deploying it on all kinds of shapes of screens and devices and all that kind of stuff is just creates a beautiful chaos anyway back to my pie.
*  So what okay you met you talked about a syntax that could work where does it currently stand what's the future static typing in python.
*  It is still controversial but it is much more accepted than when my pie and pep for 84 were were young.
*  What's the connection between pep 44 type hints and my pie my pie.
*  What's the original static type checkers so it might by quickly evolved from you guys own variant of python to a static type checker for python and sort of that for 84 that that was it like.
*  A very productive year where like many hundreds of messages were exchanged debating the merits of every aspect of of that pep.
*  And so my pie is a static type checker for python it is itself written in python most additional static typing features that we introduced in the time since three six.
*  I were also prototyped through my pie.
*  My pie being an open source project with a very small number of maintainers.
*  What's successful enough that people said this static type checking stuff for python is actually worth an investment for our company.
*  What's somehow date shows not to support.
*  Making my pie faster say or adding new features to my pie but both google and facebook and later microsoft.
*  Develop their own static type checker i think facebook was one of the first day decided that they wanted to use the same technology that they had successfully used for hhvm.
*  Because they they sort of they had a bunch of compiler writers and sort of static type checking experts who had written the hhvm compiler and it was big success within the company and they had done it in a certain way sort of.
*  They wrote a big highly parallel application in an obscure language named oh camel which is apparently mostly very good for writing state type checkers.
*  Interesting i have a lot of questions about how to write a static type checker that's very confusing facebook wrote their version and they worked on it in secret for about a year and then they came clean and went open source.
*  Google in the meantime was developing something called pie type which was mostly.
*  Interesting because it as you may have heard they have one gigantic mono repo.
*  So all the code is checked into a single repository facebook has a different approach of facebook developed pyre which which was written in camel which worked well with facebook's development workflow.
*  Google developed something they called by type which was actually itself written in python.
*  And it was meant to sort of fit well in their static type checking needs in google's gigantic mono repo so google has the one giant got it so.
*  The just to clarify this static type checker.
*  Philosophically is the thing that's supposed to exist outside of the language itself and it's just a workflow like a debugger for the program linter for people who don't know a linter maybe you can correct me.
*  But it is a thing that runs to the code continuously pre processing to find issues based on style.
*  Documentation i mean there's all kinds of linters right it can check that what usual things does a linter do maybe check that you have an too many characters in a single line.
*  Linters often do static analysis where they try to point out things that are likely mistakes but not incorrect according to the language specification like maybe you have a variable that you never use.
*  For the compiler that is valid you might.
*  Sort of you might be planning to use it in future version of the of the code and the compiler might just optimize it out but the compiler is not gonna tell you hey you never using this variable.
*  Linter will tell you that variable is not used maybe.
*  There's a typo somewhere else we are you meant to use it but you accidentally use something else or there are a number of sort of common scenarios and a linter is often.
*  A big collection of little heuristics where by looking at the combination of how your code is laid out maybe how it's indented maybe did comment structure.
*  But also just.
*  Things like definition of names use of names it'll tell you likely things that are wrong and in some cases linters are are really style checkers.
*  For python there are a number of linters that check things like do you use the the pep eight.
*  Recommended naming scheme for your functions and classes and variables because like classes start with an uppercase and the rest starts with a lower case and.
*  There's like differences there and so the linter can tell you hey you have a class that whose first letter is not.
*  An uppercase letter and that's just I just find it annoying if I wanted that to be uppercase letter I would have typed an uppercase letter but other people find it very comforting that if the linter.
*  Is no longer complaining about their code that they have followed all the style rules.
*  Maybe it's a fast way for a new developer joining a team to learn the style rules right yeah there's definitely that but the best use of a linter is probably.
*  Not so much to to sort of and force team uniformity but to actually help developers.
*  Catch bugs that the compilers for whatever reason don't catch and there's lots of that in python and so but a static type checker.
*  Focus is on a particular aspect of the linting which.
*  I mean it might buy doesn't care how you name your classes and variables.
*  I but it is meticulous about when you say that it was an integer here and you're passing a string there it will tell you hey that strings not an integer so something's wrong either.
*  Either you were incorrect when you said it was an integer or you're incorrect when you're passing into string if this is a race of static type checkers is somebody winning.
*  You said it's interesting that the companies didn't choose to invest in this centralized development.
*  Of my pie is is there a future for my pie what do you see as the one of the companies went out and everybody uses like.
*  Pi type whatever Google's is called well Microsoft is hoping that Microsoft's horse in that race called pie right is going to win.
*  I write write like R I G H T correct yeah my my all my word processors tend to type of correct that as pie right the name of the I don't know what it is.
*  Some kind of semi precious metal oh right.
*  I love it okay so okay that's the Microsoft hope but it okay so let me ask the question a different way is there going to be ever a future where's the static type checker gets integrated into the language.
*  Nobody is currently excited about.
*  Doing any work towards that that doesn't mean that five or ten years from now the situation isn't.
*  Different at the moment.
*  All the static type checkers.
*  I still evolve at a much higher speed than python and its annotation syntax evolve.
*  You get a new release of python once a year those are the only times that you can introduce new annotation syntax.
*  And there's there always people who invent new new annotation syntax that they're trying to push.
*  And worse once we've all agreed that we are going to put some new syntax in we can never take it back.
*  At least a sort of deprecating an existing feature takes many releases because you have to assume that people started using it as soon as we announced it.
*  And then you can't take it away from them right away you have to start telling them well this will go away but we're not gonna commit tell you that it's an error yet and then later it's gonna be a warning and then eventually three releases in the future maybe we remove it.
*  On the other hand the typical static type checker.
*  Still has a release like.
*  Every month every two months certainly many times a year.
*  Some type checkers also include a bunch of experimental ideas that aren't official standard python syntax yet.
*  The static type checkers also just get better at discovering things that that sort of are unspecified by the language but that sort of could make sense and so each static type checker actually has it sort of strong and weak points.
*  So it's cool it's like a laboratory of experiments yeah Microsoft Google and all and you get to see.
*  But that said you said there's not interest I think there is a lot of interest in type hinting right.
*  In the pep four eighty four actually like how many people use that do you have a sense how many people use because it's optional it's not like you can't use it.
*  But that said you said there's not interest I think there is a lot of interest in type hinting right.
*  In the pep four eighty four actually like how many people use that do you have a sense how many people use because it's optional it's a sugar.
*  I can't put a number on it but from the number of packages that do interesting things with it at runtime and the fact that there are like.
*  Now feel for very mature type checkers.
*  That each have their their segment of the market and on then there is a pie charm which has a sort of more heuristic based type checker that also supports the same syntax.
*  My assumption is that.
*  Many many people developing python software professionally.
*  For some kind of production situation are using a static type checker especially any anybody who has a continuous integration cycle probably has.
*  One of the steps in in their their testing routine that that happens for basically every every commit.
*  Is run a static type checker and in most in most cases that will be my pie.
*  So I think it's pretty popular topic.
*  According to this web page twenty to thirty percent of python three code bases are using type hints.
*  Wonder how they measured that that they just scan all of github.
*  Yeah that's what it looks like yeah they did a quick sent not all of but like a random sampling.
*  So you mentioned pie charm let me ask you the the big subjective question.
*  What's the best idea for python and you're extremely by us now that year with microsoft.
*  Is it pie charm vs code vim or emacs historically I actually started out with using thin but when it was still called vi.
*  For very long time I think from the early eighties to.
*  I'd say two years ago I was emacs user nice between I'd say twenty thirteen and twenty eighteen.
*  I dabbled with pie charm mostly because it had had a couple of features I mean.
*  Pie charm is like driving an eighteen wheeler truck whereas emacs is more.
*  Like driving your comfortable toyota car that's that's the best solution.
*  Driving your comfortable toyota car that's that's that you've had for a hundred thousand miles and you know what every little rattle of the car means.
*  I was very comfortable in emacs but there were certain things it couldn't do it wasn't very good at that sort of at least the way I had configured it.
*  I didn't have very good tooling in emacs for finding the definition of a function.
*  Got it when I was at dropbox exploring a five million line python code base.
*  I just grabbing all that code for where there where is there a class foobar well turns out that if you grab all five million lines of code there are many classes with the same name.
*  And so pie charm sort of once once you fired it up and once it's indexed your repository was very helpful but the soonest I had to edit code I would.
*  Jump back to emacs and do all my editing there because I could type much faster and switch between files when I when I knew which file I wanted much much quicker and I never really got used to the whole pie charm user interface.
*  Yeah I feel torn in that same kind of way because I've used pie charm off and on exactly in that same way and I feel like I'm just being an old grumpy man.
*  For not learning how to quickly switch between files and all that kind of stuff I feel like that has to do with shortcuts has to do with.
*  I mean you just have to get accustomed just like with touch typing yeah you have to just want to to learn that I mean if you don't need it much you don't need touch typing either.
*  You can type with two fingers just fine in the short term but in the long term your life will become better psychologically and productivity wise if you learn how to type with ten fingers.
*  If you do a lot of keyboard input before everyone emails and stuff right like you look at the next twenty thirty years of your life you have to anticipate where technology is going.
*  Do you want to invest in handwriting notes probably not more and more people are doing typing versus handwriting notes so you can anticipate that.
*  There's no reason to actually practice handwriting there's more reason to practice typing.
*  You can actually estimate back to the spreadsheet the number of paragraphs sentences or words you write for the rest of your life.
*  You probably go again with the spreadsheet of my life.
*  All of that is not actual like converted to a spreadsheet but the gut feeling like I have the same kind of gut feeling about books I've almost exclusively switched to Kindle now for ebook readers.
*  Even though I still love and probably always will the smell the feel of a physical book and.
*  You the reason I switched to Kindle is like all right well this is really paving the future is going to be digital in terms of consuming.
*  Books and content of that nature so you should get you know you should let your brain get accustomed to that experience.
*  And that same way it feels like pie charm or VS code I think by charm is is the most sophisticated feature full.
*  Python ID it feels like I should probably at some point very soon switch entire like i'm not allowed to use anything else for python.
*  Then this ID or VS code it doesn't matter but walk away from e max for this particular application so I think i'm limiting myself in the same way that using two fingers for typing is limiting myself.
*  This is a therapy session this is not.
*  But i'm sure a lot of people are thinking is what I thought you.
*  I think that that sort of everybody has to decide for themselves which one they want to to invest more time in.
*  I actually.
*  Ended up giving VS code a very tentative try when I started out at Microsoft and really liking it.
*  And it sort of it took me a while before I realized why that was but and I think that actually the founders of VS code may not necessarily agree with me on this but to me VS code is in a sense the spiritual successor of e max.
*  Because as you probably know as an old e max hack.
*  The key part of e max is that it's mostly written in in lisp.
*  And that's that's sort of new features of of e max usually update all the list packages and add new list packages and oh yeah there's also.
*  Some very obscure thing improved in the part that's not in lisp but that's usually not why you would upgrade to a new version of e max.
*  There's a core implementation that that sort of can read a file and it can put bits on the screen and it can sort of manage memory and buffers and then what makes it.
*  An editor full of features is all the list packages and of course the design of how the list packages interact with each other and with that that sort of that base layer.
*  Of the core immutable engine but almost everything in that core engine in e max case can still be overridden or replaced and so.
*  VS code has a similar architecture where there is like.
*  A base engine that you have no control over I mean it's open source but nobody except the people who work on that part.
*  Change is it much and it has a sort of a package manager and a whole series of interfaces for packages and an additional series of conventions for how packages should interact with the lower layers and with each other.
*  And powerful primitive operations that let you.
*  Move the cursor around or select pieces of text or delete pieces of text or interact with the keyboard and the mouse and whatever peripherals you have.
*  And and so the sort of the the extreme extensibility and the package ecosystem that you that you see in VS code is a is a mirror of very similar architectural features in e max.
*  What is it a serious try because as far as sort of the hype and the excitement in the general programming community VS code seems to dominate the interesting thing about.
*  I'll pie charm and what is it php store which of these jet brains specific IDs that are designed for one programming language it's interesting to.
*  What an ID specialized right there usually actually just specializations of intelligent because underneath it's all the same.
*  Editing engine with different veneer on top.
*  Where in VS code many things you do require loading third party extensions.
*  In pie charm it is possible to have third party extensions but it is it is a struggle to create one.
*  Yes we are part of the culture all that kind of stuff yeah we that I remember that might have been five years ago or so we were trying to get some better my pie integration into pie charm.
*  Is my pie is sort of python tooling and pie charm.
*  Had had its own type checking heuristic thing that we wanted to replace with something based on my pie because that was what we were using in the company and it's for the for the guy who was writing that.
*  Pie charm extension it was really a struggle to to sort of find documentation and get the development workflow going and debug his code and all that so that was was not a pleasant experience.
*  Let me talk to you about parallelism in your post titled reasoning about a sink ios summer for.
*  You talk about a fast food restaurant silicon valley that has only one table is this a real thing I just wanted to ask you about that is that just like a metaphor you're using or is that an actual restaurant in silicon valley it was it was a metaphor of course.
*  I can imagine such a restaurant so for people who don't then read the thing you should you should but it was a.
*  Idea of a restaurant where is only one table and you show up one at a time and they are prepared and actually looked it up and there is restaurants like this throughout the world.
*  It seems like a fascinating idea you stand in line you show up there's one table.
*  They are they ask all kinds of questions that could just for you that's fascinating it sounds like you'd find places like that in tokyo.
*  It sounds like a very japanese thing or in the bay area there are pop places that probably more or less work like that i've never eaten at such a place the fascinating thing is you propose is a fast food this is all for burger it was one of my rare.
*  Sort of more literary or poetic moments where i thought i'll just open with a crazy example to catch your attention and the rest is very dry stuff about locks and semaphores and how a semaphore is a generalization of a lock.
*  What was very poetic and well delivered and actually made me wonder if it's real or not because you don't make that explicit and it feels like it could be true and in fact i wouldn't be surprised if somebody like listens to this and knows exactly a restaurant like this in silicon valley anyway can we step back and.
*  Can you just talk about parallelism concurrency threading asynchronous all these different terms what is it sort of a high philosophical level the the fisherman is back in the boat.
*  Well the idea is if the fisherman has two fishing rods.
*  Since fishing is mostly a matter of waiting for fish to nibble what depends on how you do it actually but if you had to if if you're doing the style of fishing where you sort of you you throw it out and then.
*  You let it sit for a while until maybe you see a nibble one fisherman can easily run two or three or four.
*  Fishing rods and so as long as you can afford the equipment you can catch four times as many fish by a small investment in for fishing rods and so get since your time.
*  You sort of say you have all saturday to go fishing if you can catch four times as much fish you have a much higher productivity and that's actually i think how deep sea fishing is done you could just have a rod and you put in the whole thing you can have many rods.
*  What is there an interesting difference between parallelism and concurrency and asynchronous is there one a subset of the other to you like how do you think about these terms in the computer world there is a big difference when people are talking about parallelism like a parallel computer.
*  That's usually really several complete cpus that are sort of tied together and share something like memory or an iobus.
*  Concurrency can be a much more abstract concept.
*  Where.
*  You have the illusion that things happen.
*  Simultaneously but what the computer actually does is it spends a little time running some this program for a while and then it spend some time running that program for a while and then spending some time for the third program for a while.
*  Parallelism is the reality and concurrency is part reality part of the yeah parallelism typically implies that there is multiple copies of the hardware.
*  You write that implementing synchronization primitives is hard in that blog post and you talk about locks and semaphores why is it hard to implement synchronization primitives.
*  Because at the conscious level our brains are not trained to to sort of keep track of multiple things at the same time like obviously you can walk and chew gum at the same time.
*  Because they're both activities that require only a little bit of your conscious activity but try balancing your checkbook and watching a murder mystery on tv.
*  You'll mix up the digits or you'll miss an essential clue on in the tv show.
*  So why does it matter that the programmer the human.
*  Is is bad as the programmer is at least with the current state of the art is responsible for writing the code correctly and it's hard enough to keep track of a recipe that you just.
*  Execute one step at a time chop the carrots then peel the potatoes mix the icing.
*  You need your whole brain when you're when you're reading a piece of code what what is going on okay we're we're we're loading.
*  The number of mermaids in variable a and the number of more men in variable B and now we take the average or whatever.
*  I like we're just jumping from metaphor to metaphor I like it you have to keep in your head what is in a what is in B what is in C hopefully have better names.
*  And that is challenging enough if you have two different pieces of code that are are sort of being executed.
*  Simultaneously whether is using the parallel or the concurrent approach if like.
*  A is the number of fishermen and B is the number of programmers but in another part of the code is the number of mermaids and B is the number of merman.
*  And somehow that's the same variable if you do it sequentially if first you do your mermaid more people computation and then you do your people in the boat computation.
*  Doesn't matter that the variables are called a and B and that is literally the same variable because you you're done with one use of that variable but when you mix them together suddenly.
*  The number of more people replaces the number of fishermen and your computation goes dramatically wrong and there's all kinds of ordering.
*  Of operations that could result in the assignment of those variables and so you have to anticipate all possible orderings and you think you're smart and you'll put a lock around it.
*  And in practice in terms of bugs per line of per thousand lines of code.
*  This is an area where everything is worse so a lock is a mechanism by which you forbid only one.
*  Chef can access the oven at a time something like that and then semaphores allow you to do what multiple ovens that's not a bad idea because if you're sort of.
*  If you're preparing if you're baking cakes and you have multiple people all baking cakes but there's only one oven then maybe you can tell that the oven is in use but maybe it's preheating and so you have to maybe maybe you make a sign that says oven in use.
*  And you flip the sign over and it says often is free when you're done baking your cake.
*  That's a lock that sort of and and what do you do when you have two ovens or maybe you have 10 ovens.
*  You can put a separate sign on each oven or maybe you can sort of someone who comes in wants to see at a glance and maybe there's an electronic sign that says there are still five ovens available.
*  Or maybe there are already three people waiting for an oven so you can.
*  If you see an oven that's not in use it's already reserved for someone else who got in line first and that's sort of what it what what the restaurant metaphor was trying to explain.
*  Yeah so you're now tasks you sitting as a designer python with a team of brilliant core developers and have to try to figure out to what degree can any of these ideas be integrated and not so maybe this is a good time to ask what is a sync i.
*  And how has it evolved since python 3.4.
*  Wow yeah so we had this really old library for for doing things.
*  Concurrently especially things that had to do with i.o. and networking i.o. was especially a sort of a popular topic.
*  And.
*  In the python standard library we had a brief period where there was lots of development and i think was late nineties maybe early two thousands and like.
*  Two little modules were added that were the state of the art of doing a synchronous i.o. or sort of non blocking a i.o. which means that you can keep multiple network connections open and sort of service them all in parallel like a typical web server does.
*  So i.o. is input and output you're writing either to the network or yes from a network connection or reading and writing to a hard drive storage also possible and you can do.
*  The ideas you can do to multiple while also doing computation.
*  Running some code that does some fancy stuff yeah like when you're writing a web server when a request comes in a user the sort of needs to see a particular web page.
*  I have to find that page maybe in the database and format it properly and send it back to the client and.
*  There's a lot of waiting waiting for the database waiting for the network and so you can handle hundreds of thousands or millions of requests.
*  Concurrently online machine anyway waste of doing that in python were kind of stagnated and.
*  I forget it might have been around 2012 2014.
*  When someone for the umpteenth time actually said these async chat and async core modules that you have in a standard library are not quite enough to solve my particular problem.
*  Can we add one tiny little feature and everybody said no that stuff is not to but you're not supposed to use that stuff right your own using.
*  Third party library and then everybody started a debate about what the right third party library was and somehow I I felt that there was actually a queue for well maybe we need a better state of the art.
*  Module in the standard library for for multiplexing input output from different sources you could say that it's spiraled out of control a little bit it was at the time it was the largest python enhancement proposal that was ever proposed.
*  Can you were deeply involved with that at the time I was very much involved with that I was like the lead architect.
*  I ended up talking to people who had already developed serious third party libraries that did similar things and sort of taking ideas from them and.
*  Getting their feedback on my design and eventually we put it in the standard library and after a few years I got distracted I think the thing the big thing that distracted me was actually type annotations.
*  Other people kept it alive and kicking and it's been quite successful actually.
*  In the world of python web clients so initially what are some of the design challenges there in that debate for the pep and what are some things that got rejected what are some things that got accepted to stand out to you.
*  There are a couple of different ways you can handle parallel I oh and this happens sort of at an architectural level in operating systems as well like windows prefers to do it one way and unix prefers to do it the other way.
*  You sort of.
*  You have an object that represents a network endpoint say connection with web browser that your client.
*  And say you're you're you're waiting for an incoming request to fundamental approaches are.
*  Okay i'm waiting for an incoming request i'm doing something else come wake me up or a course sort of come tell me when something interesting happened like a packet came in on that network connection.
*  And the other paradigm is.
*  Where on a team of a whole bunch of people with maybe a little mind and we can only manage one web connection at a time so.
*  I'm just sitting.
*  Looking at this this web connection and i'm just blocked until something comes in and then.
*  i'm already waiting for it.
*  I get I get the data I process the data and then I go back to the top and say no sort of i'm waiting for the next packet.
*  Those are about the two paradigms one is a paradigm where there is sort of notionally a thread of control whether it's an actual operating system thread or more an abstraction in async i we call them tasks.
*  But a task in a sink i or a thread in other contexts is devoted to one thing and it has logic.
*  For all the stages like when it's a web request like.
*  First wait wait for the first line of the web request parsed it because then you know if it's a get or post or a put or whatever or an error.
*  Then wait until you have a bunch of lines until there's a blank line then parse that as headers and then interpret that and then wait for the rest of the.
*  Data to come in if there is any more that you request expect that sort of standard web stuff.
*  And the other thing is and there's always endless debate about which approach is more efficient and which approach is more error prone.
*  Where i just have a whole bunch of stacks in front of me and whenever.
*  A packet comes in i sort of look at the number of the pack that there's some number on the packet and i say oh that packet goes on this pile.
*  And then i can do a little bit and then sort of that pile provides my context.
*  And as soon as i'm done with with the processing i sort of.
*  I can't forget everything about what's going on because the next packet will come in from some random other client and it's that pile or this pile.
*  And every time a pile is maybe empty or full or whatever the criteria is i can toss it away or use it for a new space but.
*  Several traditional third party libraries for asynchronous i.o. processing in python shows the model of a callback.
*  And that's that's the idea where you have a bunch of different stacks of paper in front of you and every time someone gives you a piece gives you a new sheet you decide which stack it belongs to.
*  And that leads to a certain style of spaghetti code that i find sort of aesthetically.
*  Not pleasing and i i was sort of never very successful and i had heard many stories about people who are also.
*  Sort of complaining about that style of coding.
*  It was very prevalent in javascript at the time at least because it was like how did javascript event loop.
*  Basically works and so i thought well the task based model where each task has a bunch of logic.
*  We had mechanisms in the python language that we could easily reuse for for that and i thought i want to build a whole library for asynchronous networking i.o.
*  And all the other things that need may need to be done asynchronously.
*  Based on that paradigm and so i just chose a paradigm and try to see how far i could get with that and it turns out that it's pretty good paradigm.
*  The people enjoy that kind of paradigm programming for asynchronous i.o. relative to callbacks.
*  Okay beautiful so how does that all interplay with the infamous guild the goal the global interpreter lock.
*  Maybe can you say what the gil is and how does it dance beautifully with a sink i.o.
*  The global interpreter lock.
*  Solves the problem that python originally was not written with either asynchronous or or parallelism in mind at all there was no concurrency in the language there was no parallelism there were no threads.
*  Only a small number of years into python's initial development.
*  All the new cool operating systems like son of us and silicon graphics iris and then eventually posix and windows all came with threading libraries.
*  That lets you do multiple things in parallel and there is a certain certain sort of principle which is the operating system handles the threads for you.
*  And the program can pretend that there are as many cpus as as there are threads in the program.
*  And those cpus were completely independently.
*  And if you don't have enough cpus the operating system sort of simulates those extra cpus on the other hand if you have enough cpus.
*  You can get a lot of work done by deploying those multiple cpus but python wasn't written to to do that.
*  And so.
*  As libraries for for multi threading were added to see but every operating system vendor was adding their own version of that.
*  We thought and maybe we were wrong but at the time we thought well we quickly want to be able to support these multiple threads.
*  Because they seemed at the time in the early nineties when they were new at least to me.
*  They seemed a cool interesting programming paradigm and one of the things that that python at least at the time felt was nice about the language was that we could give a.
*  Safe version of all kinds of cool new operating system toys to the python programmer like i remember.
*  One or two years before threading I had spent some time adding networking sockets.
*  To python and they were very literal translation of the networking sockets that were in the bsd operating system so unix bsd.
*  But the nice thing was if you're using sockets from python then all the things you can do wrong with sockets in c would automatically give you a clear error message instead of just ending up with a malfunctioning hanging program.
*  And so we thought well we'll do the same thing with threading but we didn't really want to rewrite the interpreter.
*  Interpreter to be thread safe because that that was was like.
*  That would be a very complex refactoring of all the interpreter code and all the runtime code because all the objects were written with the assumption that there's only one thread.
*  And so we said okay well we'll take our losses will provide something that looks like threads and as long as you only have a single cpu on your computer which most computers at the time did.
*  It feels just like threats because.
*  The whole idea of of multiple threads in the os was that even if your computer only had one cpu you could still fire up at many threads as you wanted well within reason maybe ten or twelve not five thousand.
*  And so we thought we had conquered the.
*  The abstraction of threads pretty well because multi core cpus were were not in in most python programmers hands anyway and then of course a couple of more iterations of morse law and computers getting faster and at some point.
*  The chip designers decided that they couldn't make the cpus faster but they could still make them smaller and so they could put multiple cpus on one chip and suddenly there was all this pressure about do things in parallel and that's where the solution we had in python didn't work.
*  And that's that's sort of the moment that the gil became became infamous because the gil the gil was the solution we use to sort of.
*  Take this single interpreter and share it between all the different operating system threats that you could create and so as long as the hardware physically only had one cpu that was all fine.
*  And then as hardware vendors were suddenly telling us all oh you got to paralyze everything's got to be paralyzed people started saying oh but we can use multiple threads in python and then they discovered oh but actually all threats run on a single single core.
*  Is there a way is there ideas in the future to remove the global interpreter log gil like maybe multiple sub interpreters some tricky.
*  Interpreters on top of interpreters kind of thing yeah there there are a couple of possible futures there the.
*  The most likely future is that will get multiple sub interpreters which each run a completely independent python program nice but there there's still some benefit of.
*  Off sort of faster communication between those programs but it's also managing for you this running a multiple python programs.
*  Yeah it's hidden from you right the it's it's hidden from you but you have to spend more time communicating between those programs because the sort of.
*  The attractive thing about the multi threaded model is that the threats can share objects at the same time that's also the downfall of the multi threaded programming model.
*  Because when you do share objects you weren't and you didn't necessarily intend to share them or there were aspects of those objects that that were not reusable you get all kinds of concurrency bugs and so.
*  The reason i wrote that little blog post about semaphores was that concurrency bugs are just harder.
*  It would be nice if python had no global interpreter lock and it had so called free threading.
*  What it would also cause a lot more software bugs.
*  The interesting thing is that there is still a possible future where we are actually going to or where we could experiment at least with that.
*  Because there is a guy working for facebook who has developed a fork of CPython.
*  That he called the no gill interpreter where he removed the gill and made a whole bunch of optimizations so that the single threaded case doesn't run too much slower.
*  And multi threaded case will actually use all the cores that you have.
*  And so that's that would be an interesting possibility.
*  If we would be willing as python core developers to actually.
*  Maintain that code indefinitely and if we're willing to put up with the additional complexity of the interpreter and the additional sort of overhead for the single threaded case and i'm personally not convinced that.
*  There are enough people.
*  I'm needing the speed of multiple threads with their python programs.
*  That it's worth to sort of take that performance hit and that complexity hit.
*  I feel that the gill actually is pretty nice goldilocks point between no threads and all threads all the time but not everybody agrees on that so that is definitely a possible future the sub interpreters look like a fairly safe bet for 312 so.
*  Say a year from now.
*  Here so the goal is to do a new version every year for python let me ask you perhaps a fun question but there's a philosophy to to will there ever be a python 4.0 now before you say it's currently a joke and probably not we're going to go to 3.99 or 3.99999.
*  Can you imagine possible features.
*  That python 4.0 might have that would necessitate the creation of the new 4.0 given the amount of pain and joy suffering and triumph that was involved in the move between version two and version three.
*  Yeah well we're we.
*  As a community and as a core development team we have a large amount of painful memories about the python three transition.
*  Which is one reason that sort of everybody is happy that we decided there's not going to be a 4.0 at least not anytime soon and if there is going to be one that will sort of plan the transition very differently.
*  Because clearly we underestimated the pain the transition caused for our users in the python three case and.
*  Had we known we could have sort of designed python three somewhat differently without making it any worse.
*  We just thought that we had a good plan but we we we underestimated where what what sort of the users were capable of when it comes to that kind of transition by the way I think we talked.
*  I think we talked.
*  Way before a year and a half before the python to officially end of life end of life.
*  What was that what was your memory of the end of life did you shed a tear on January 1st 2020 did was there.
*  We were standing alone or team had basically moved on years before it was it was purely it was a little symbolic moment.
*  Add to signal to the remaining users that.
*  There was no longer going to be any new releases or support for python two seven.
*  Did you share a single tear while looking out over the horizon.
*  I'm not not a very poetic person and I don't shed tears like that but no.
*  We actually had planned a party but the party was planned for the python called the US python conference that year which would never happened of course because of the pandemic.
*  Oh is it like a march 20 yeah the conference was going to be I think late April that year.
*  So that that was a very difficult decision to cancel it but.
*  They did anyway if we're going to have a python for we're going to have to have both a different reason for for having that and a different process for managing the transition can you imagine a possible process.
*  That so I think you're implying that if there is a 4.0 in some ways it would break back compatibility.
*  Well so.
*  Here is here is a concrete thought i've had and i'm not unique but not everyone agrees with this so this is definitely a personal opinion.
*  If we were to try something like that no guilt python.
*  My expectation is that.
*  It would feel just different enough.
*  At least for the the part of the python ecosystem that is heavily based on see extensions and that is like the entire machine learning data science scientific python.
*  The entire machine learning data science scientific python world is all based on see extensions for python and so.
*  Those people would likely feel the pain the most because they.
*  Even if we don't change anything about the syntax of the language and the semantics of the language when you're writing python code week we could even say suppose that after python say 3 19 instead of 3 20 will have 4.0.
*  Suppose that's the time when we flip the switch to 4.0 will will not have a gill imagine it was like that.
*  So.
*  I would probably say.
*  That particular year the release that we name 4.0 will be syntactically it will not have any new syntactical features no new modules in the standard library no new built in functions.
*  Everything will be at the python level will be purely compatible with python 3.19 however.
*  Extension modules will have to make a change they will have to be recompiled they will not have the same binary interface.
*  I the semantics and and api is for for some.
*  Things that are frequently accessed by see extensions will be different and so for a pure python user.
*  4.0 would be a breeze except that there are very few pure python users left because everybody who is using python for something significant is using third party extensions there are like i don't know.
*  Several hundreds of thousands of third party extensions on the pipey i service.
*  I'm not saying they're all they're all good but there is a large list of extensions that would have to do work and some of those extensions are currently already low on maintainers.
*  And they're struggling to where keep afloat so there you can give a huge heads up to them if you go to 4.0 to really keep developing it yeah we probably have to do something like.
*  Several years before who knows maybe five years earlier like three to fifteen we would have to say and i'm just making that specific numbers up but we at some point we have to say.
*  The no gill python could be an option it might be a compile time option.
*  If you want to use no gill python you have to recompile python from source for your platform using your tool set.
*  All you have to do is change one configuration variable and then you just run make.
*  Configure and make it will build it for you but now you also have to use the no gill compatible versions of all extension modules you want to use.
*  And so as long as many extension modules don't have fully functional.
*  Sort of variants that work in the no gill world that's not a very practical thing for python users but it would allow extension developers.
*  To test the waters see what they need to syntactically to be able to compile at all maybe they're using.
*  Functions that are defined by the python three run time that won't be in the python four run time those functions will not work they'll have to find an alternative.
*  But they can experiment with that and sort of write test applications and that would be a way to transition and that that could be a series of releases where that.
*  Python four is more and more imminent we.
*  Have supported more and more third party extension modules to have solid support that works for no gill python for that new API.
*  And then sort of python python four dot oh is like the official moment that the mayor comes out and cuts the ribbon and now python now the sort of no gill mode is the default and maybe the only mode there is.
*  The internet wants to know from reddit.
*  It's a it's a small and fun question there's many fun questions but.
*  Out of the pipeline packages pipeline packages do you have a do you have ones you like do you in your opinion or there must have pipeline libraries or ones you use all the time constantly oh my that.
*  I should really have a standard answer for that question but like a positive standard answer but my current standard answer is that i'm not a big user of third party packages when i write python code i'm usually developing some tooling around building python itself.
*  And the last thing we want is dependencies on third party packages so I tend to just use the standard library and that's where your focus is that's where your mind is.
*  But do you do you keep an eye on what's out there to understand where the standard library could be moving should be moving it's a good kind of landscape of what's missing from the sale library well usually when something's missing from the standard library now we have.
*  Nowadays.
*  It is a relatively new idea and there is a third party implementation or maybe possibly multiple third party implementations but.
*  They evolve at a much higher rate than they could when they're in the standard library so they it would be a big reduction in in activity to.
*  Incorporate things like that in the standard library so I I like that there is a lively package ecosystem and that sort of recent trends in the standard library are actually that we're doing the occasional spring cleaning where we're just.
*  We're we're.
*  Choosing some modules that have not had a lot of change in a long time and that maybe.
*  Would be better off not existing at all at this point because there might be a better third party.
*  There might be a better third party alternative anyway and we're we're sort of slowly removing those that often those are things that I sort of I spiked somewhere in 1992 or 1993.
*  If you look look through the commit history it's very sad like.
*  All cosmetic changes like changes in the indentation style or the name of this other standard library module got changed or nothing nothing of any substance the API is identical to what it was 20 years ago.
*  So speaking of packages they have a.
*  A lot of impact on a lot of people's lives does it make sense to you why python has become the primary the dominant language for the machine learning community so packages like.
*  So packages like pi torch tensor flow second learn and even like the lower level stuff like non pi side pi pandas matplotlib with the visualization can you like does it make sense to you why it.
*  Uh permeated the entire data science machine learning a community well it's part of it is an effect that's as simple as we're all driving on the right side of the road right.
*  Uh it's compatibility yeah it's it's and and and part of it is.
*  Uh.
*  Not not quite as as as fundamental as driving on the right side of the road which you have to do for for safety reasons we have to agree on something.
*  I think they could have picked javascript or pearl there was there was a time in the early 2000's that it really looked like pearl what was going to dominate like biosciences.
*  Because dna search was all based on regular expressions and pearl has the fastest and most comprehensive regular expression engine still does.
*  I spent quite a long time with pearl thousand other letting go.
*  Letting go of this kind of data processing system the reasons why python.
*  Became the lingua franca of scientific code and and.
*  Machine learning learning in particular and data science.
*  It really had a lot to do with.
*  Anything was better than see your c++ recently a guy who worked at lauren's livermore national laboratories in the the sort of computing division.
*  Wrote me his his memoirs and and he had his his own view of how he helped something he called computational steering into existence.
*  And this was the idea that you you take libraries that in in his days were written in fortran that that solved universal mathematical problems.
*  And those libraries still work but the scientists that use the libraries use them to solve continuously different.
*  Specific applications and answer different questions and so those poor scientists were.
*  Where were required to to use say fortran because fortran was the library the language that the library was written in.
*  And then the scientist would have to write an application that sort of uses the library to solve a particular equation or set off of answer a set of questions and the safer same for c++.
*  Because there is there is interoperability so the dusty decks are written either in c++ or fortran.
*  And so poor was one of the people who.
*  I think in the mid nineties saw that that you needed a higher level language for the scientists.
*  To to sort of tie together the fundamental mathematical algorithms of linear algebra and and other stuff.
*  And so.
*  Gradually some library started appearing that did very fundamental stuff with arrays of numbers in python.
*  I mean when I first created python I was not expecting it to be used for arrays of numbers much I thought that was like an outdated data type.
*  And everything was like objects and strings and like python was good and fast at string manipulation and objects obviously but arrays of numbers were not very efficient and the multi dimensional arrays didn't even exist in the language at all.
*  But there were people who realized that python had extensibility.
*  That was flexible enough that they could write third party packages that did support large arrays of numbers and operations on them very efficiently.
*  And somehow they got a foothold through sort of different parts of the scientific community I remember that the Hubble space telescope people in Baltimore were somehow big python fans in the late nineties.
*  And at various points small improvements were made and more people got in touch with using python to derive these libraries.
*  Of interesting algorithms and like once once you have a bunch of scientists who are working on similar problems say they're all working on stuff that.
*  Data that comes in from the Hubble space telescope but they're looking at different things some some are looking at stars in this galaxy other are looking at galaxies the math is completely different but the underlying libraries are still the same.
*  And so they exchange code they say well I wrote this python program or I wrote a python library to solve this class of problems.
*  And the other guys either say oh I can use that library to or if you make a few changes I can use that library to why right why start from scratch in pearl or javascript where there's not that infrastructure.
*  For arrays of numbers yet where is in python you have it and so more and more scientists at different places doing different different work.
*  Discovered python and then then people who had an idea for an important new fundamental library decided oh python is is actually already known to our users so.
*  Let's use python as the user interface I think that's how tensor I imagine at least that's how tensor flow ended up with python as the user interface interface right but with tensor flow.
*  There's a deeper history of what the communities it's not just like what packages and needs it's like what the community leans on for programming language because tensor flow.
*  Had a prior library that was internal to google but there's also competing machine learning frameworks like the anno cafe they were in python there was some scholars.
*  Some other languages but python was really dominating it and it's interesting because there's other languages from the engineering space like matlab.
*  That a lot of people used but different design choices by the company by the core developers led to it not spreading and one of the choices of my lab.
*  By math works is to not make it open source right or not you know having people pay it was a very expensive product and so universities especially disliked it because it was a price per seat I remember hearing.
*  Yeah but I think that's not why it failed or I failed to spread I think universities didn't like it but they would still pay for it.
*  The thing is it didn't feed into that github open source packages culture so like and that's somehow a precondition for.
*  Open source packages culture so like and that's somehow a precondition for for viral spreading the hacker culture like the tinkerer culture.
*  With python it feels like you can build a package from scratch to solve a particular problem and get excited about sharing that package with others and that creates an excitement about a language I tend to like python's approach to open source in particular because it's sort of.
*  It's almost egalitarian.
*  There's there's little hierarchy there's there's obviously some because the like you need to decide where you drive on the left or the right side of the road sometimes.
*  But there is a lot of access for people with little power you don't have to work for a big tech company to make a difference in the python world.
*  We have affordable events that really care about community and support people and sort of the community is.
*  Is like a big deal at our conferences and in in the psf when the psf funds events it's always about.
*  Growing the community the psf funds very little development.
*  They that they do some but most of the develop most of the money that the psf forks out.
*  Is to community fostering things.
*  So speaking of egalitarian last time we talked four years ago it was just after you step down from your role as the benevolent dictator for life be dfl looking back what are your insights and lessons.
*  You learn from that experience about python developer community about human nature about human civilization.
*  Life itself oh my.
*  I probably held on to the position too long.
*  I remember being just extremely stressed for a long time.
*  And it wasn't very clear to me what was leading what was causing the stress.
*  And looking back.
*  Add.
*  I should have sort of relinquished my central role as be dfl sooner.
*  What were the pros and cons of the be dfl role like what were the you not relinquishing it what what are the benefits of that for the community and what are the drawbacks.
*  Well the benefits for the community would be things like.
*  I.
*  Clarity of vision and sort of.
*  A clear direction because I.
*  I had certain ideas in in mind when I created python and well I sort of let myself be influenced by many other ideas as python evolved and became.
*  More successful and more complex and more used I also stuck to certain principles and it's still hard to say what are python score principles.
*  But the fact that I was playing that role and sort of always very active grew the community in a certain way.
*  It modeled to the community how to think about.
*  How to how to solve a certain problem well.
*  That was a source of stress but it was also beneficial it was a source of stress for me personally but it was beneficial for the community because people people sort of.
*  Over time had learned how I was thinking and could predict.
*  But how how I would would decide about a particular issue and not always perfectly of course but there was like.
*  There wasn't a lot of jerking around like this year we're all but this year the democrats are in power and we're doing these kind of things and now the republicans are in power and they roll all that back into those kind of things.
*  There is a clear fairly straight path ahead and so fortunately the successor structure with the steering council has sort of found a similar way of.
*  Of leading the community in a fairly steady direction without stagnating and for me personally it's more fun because there are there are things I can just ignore.
*  Yeah oh yeah there's a bug in multi processing let someone else decide whether that's important to solve or not.
*  I'll stick to typing in the async IO and the faster interpreter.
*  Yeah it allows you to focus a little bit more yeah.
*  What are interesting differences in culture if you can comment on between Google Dropbox and Microsoft from a python programming perspective all places you've been to the positive.
*  Is there a difference or is it just about people and there's great people everywhere or is there a culture differences.
*  Dropbox is much smaller than the other two in your list yeah so that's.
*  That is a big difference the set of products they provide is more narrower so they're more focused.
*  And yeah and and Dropbox sort of at least during the time I was there had the tendency of sort of.
*  Making a big plan putting the whole company behind that plan for a year and then evaluate and then suddenly find that.
*  Everything was wrong about the plan and then they had to do something completely different.
*  The annual engineering reorg was was sort of an unpleasant tradition that dropbox because like there's a new VP of engineering and so now all the directors are being reshuffled and this guy was in charge of of.
*  Infrastructure one year and the next year he was made in charge of I don't know product development.
*  It's fascinating cuz like you don't think about these companies internally but I you know Dropbox to me from the very beginning was one of my favorite services there's certain like programs and online services that.
*  Make me happy make me more efficient and all that kind of stuff but one of the powers of those kinds of services they disappear that you're not supposed to think about how it all works but it's incredible to me that you can sink stuff effortlessly.
*  Across so many machines so quickly and like don't have to worry about conflicts they they they take care of the you know as a person that comes from version repositories and all that kind of stuff or merge is super difficult and.
*  Just keeping different versions of different files is very tricky the fact that they could take care of that I just I don't know the the engineer behind the scenes must be super difficult both on the computer infrastructure and the software.
*  A lot of internal sort of hand wringing about things like that but the the product itself always worked very smoothly yeah.
*  What does probably a lot of lessons to that you can have a lot of terminal inside and the engineering side but if the product is good the product is good and don't maybe don't mess with that either to you know when it's good.
*  Keep it's like with Google focus on the search and ads.
*  Right like the money will come and make sure that's done extremely well and don't forget what you do extremely well in what ways do you provide value and happiness to the world make sure you do that well.
*  Is there something else to say about Google and Microsoft Microsoft has had a very fascinating shift recently with the new CEO what do you know recent CEO with purchasing GitHub.
*  Embracing open source culture embracing the developer culture is pretty interesting to see that's like why I joined Microsoft.
*  I mean after after retiring and thinking that I would stay retired for the rest of my life which of course was a ridiculous thought but I was I was.
*  I was done working for a bit and then the pandemic made me realize that work work and also provided a source of fulfillment.
*  Keep you keep you out of trouble.
*  Microsoft is very interesting company because it has this incredible very long and varied history and this amazing catalog of products that many of which also date way back I mean.
*  I've been been talking to a bunch of Excel people lately and Excel is like 35 years old and they can still read spreadsheets that that they might find on old floppy drive.
*  Yeah.
*  Yeah there's man there's so many incredible tools through the years.
*  Excel one of the great shames of my life.
*  Is that I've never learned how to use Excel well I mean it just always felt like so many features are there it's similar with ideas like pie charm.
*  It feels like I converge quickly to the dumbest way to use a thing to get the job done when clearly there's so much more power your fingertips.
*  But there's I do think there's probably expert users of Excel.
*  Oh Excel is a cash cow actually.
*  Oh it actually brings in money.
*  Oh yeah a lot of the engineering sort of if you look deep inside Excel there's some very good engineering very very impressive stuff.
*  Okay now I need to definitely learn.
*  I had issues because I'm a keyboard person so I had issues coming up with shortcuts and Microsoft sometimes it's changed over the years but sometimes they kind of want to make things easier for you on the surface and therefore make it harder for like.
*  People that like to have shortcuts and all that kind of stuff to optimize their workflow.
*  Now Excel is probably people are probably yelling at me it's like no Excel probably has a lot of ways to optimize work.
*  In fact I keep discovering that there are many features in Excel that only exists at keyboard shortcuts.
*  Yeah that's the sense I have and now like I'm a bad keyboard user.
*  Only exists at keyboard shortcuts.
*  Yeah that's the sense I have and now like I'm embarrassed that it's just you just have to know what they are yeah that's that's like there's no logic or.
*  Or reason to the assignment of the keyboard shortcuts because they they go back even longer than 35 years.
*  Can you maybe comment about such an Adela and how hard it is for CEO to sort of pivot company towards open source or developer culture is there something you could see about like how what's the role of leadership in such a.
*  Pivot and definition of a new vision I've never met him but I hear.
*  He's just a really sharp.
*  Thinker.
*  But he also has an incredible business sense he took the organization that had very solid pieces but that was also struggling.
*  With all sorts of shameful things especially the Steve Ballmer time.
*  I imagine in part through his personal charm and thinking and of course that the great trust that that the rest of the leadership has in him he managed to to really turn the company around and sort of.
*  Change it from from openly hostile to open source to to actively embracing open source.
*  And that doesn't mean that suddenly excel is going to go open source but that means that there's room for a product like VS code which is open source.
*  Yeah it's fascinating and it gives me faith that large companies with good leadership can grow can expand can change and pivot and so on develop because it gets harder and harder as the company gets large.
*  You wrote a blog post in response to a person looking for advice about whether with the CS degree to choose a nine to five job or to become an entrepreneur.
*  Finishing question if you just think from first principles right now somebody has took a few years in programming is loved software engineering in some sense creating Python is an entrepreneurial endeavor.
*  That's a choice that a lot of people that are good programmers have to make do I work for a big company or do I create something new.
*  Or you can work for a big company and create something new there.
*  Inside the yeah I mean big companies have individuals who create new stuff that eventually grows big all the time.
*  And if you're the person that creates a new thing it grows big you'll have a chance to move up quickly in the company to run that thing.
*  If that's your aspiration but what what can also happen is that someone is brilliant engineer and sort of builds a great first version of a product.
*  And has no aspirations to then become a manager and grow the team from five people to twenty people to a hundred people to a thousand people and.
*  Be in charge of hiring and meetings and they move on to inventing another crazy thing inside the same company or sometimes they.
*  They found a startup or they moved to a different great larger small company there's all sorts of models.
*  And sometimes people sort of do have this whole trajectory from engineer buckling down writing code.
*  Not nine to five but more like noon till midnight seven days a week.
*  And coming up with a product and sort of.
*  Staying in charge I mean if you take drew Houston drop boxes founder he is still the CEO.
*  And at least when when I was there he had not checked out or anything he was he was good CEO.
*  But he had started out as the technical inventor or co inventor and so he was someone who.
*  I don't know if he always aspired that I think when when he was sixteen he already started a company so maybe maybe he did but he sort of.
*  It turned out that that he had he did have the personal sort of skill set needed to to grow and stay on top and other people sort of.
*  A brilliant engineers and horrible at management I count myself at least in the second category so your your your first love and still your love is to be the quote unquote individual contributor to the program.
*  Do you have advice for a programming beginner on how to learn python the right way.
*  Find something you actually want to do with it if you say I want to learn skill X.
*  That's not enough motivation you need to pick something.
*  And it can be it can be a crazy problem you want to solve it can be completely unrealistic.
*  But something that that challenges you in into actually learning.
*  Coding in in some language.
*  And there's so many projects out there you can look for like that that doesn't have to be some big ambitious thing it could be writing a small bot if you're into social media you can write a reddit bot or twitter bot or or some aspect of automating some as something that you do every single day processing files all that kind of stuff nowadays you can take machine learning components and and sort of.
*  Plug those things together so cool stuff with them so that's actually a really good example so if you're interested in machine learning the state of machine learning is such that like a tutorial that takes an hour.
*  Can get you to start using pre trained models to do something super cool and that's a good way to learn python cause you learn just enough to run this model and that's like a sneaky way to get get in there to figure out how to import stuff how to.
*  Write basic i o how to run functions and i'm not sure if it's the best way to learn the basics and python but could be nice to just get fall in love first and then figure out the basics right.
*  Yeah you can't expect to learn python from a one hour video blanking out on the name of someone who.
*  Who wrote a very funny blog post where he said i see all these ads for things like learn python in ten days or so and he said the goal should be learn python in ten years.
*  That's hilarious but i completely disagree with that i think the criticism behind that is that.
*  The the place is just like the blog post from earlier the places that tell you learn python five minutes or ten minutes they're actually usually really bad tutorials so the thing is i do believe that you can learn a thing.
*  In an hour to get some interesting quick like to it hooks you i mean this but it just takes a tremendous amount of skill to be that kind of educator.
*  Richard Feynman was able to condense a lot of ideas and physics in a very short amount of time but that takes a deep deep understanding and so yes of course the actual i think the ten the ten years is about the experience the pain along the way and there's something.
*  Well you have to practice you can memorize the syntax.
*  But well i couldn't but maybe maybe someone else can but that doesn't make you a coder.
*  Yeah actually coding has changed in fascinating ways because so much of coding is copying pasting from stack overflow and then adjusting.
*  Which is another way of coding and i don't want to talk down to that kind of style coding because it's kind of a nicely efficient but you know where that is going.
*  Code generation no seriously get a copilot copilot i use it every day and it really yeah it writes.
*  A lot of code for me and usually it's slightly wrong but it's still saves me typing because all i have to do is like change one word in a line of text that otherwise it it generated perfectly and like.
*  How many times are you looking for like oh what was i doing this morning i was looking for and begin marker and i look at was looking for an end marker and so begin is.
*  Blah blah blah search for begin this is the begin token and then the next line i type E.
*  And it it completes the whole line with and instead of begin that's a very simple example sometimes it it sort of if i name my function right it writes a five or ten line function.
*  And you know python enough to very quickly then detect the issues you so it's it becomes a really good dance partner then it doesn't save me a lot of thinking but since i'm a poor typist i'm very much appreciative of.
*  All the all the typing it does for me much better actually than the previous generation of suggestions that are also still built in vs code.
*  I wear when you hit like a dot it it tries to guess what the type is of the variable to the left of the dot and then it gives you a list of pop down menu of what the attributes of that object are but copilot is much much smoother than that was fascinating to hear.
*  That you use get help copilot do you think do you worry about the future that the automatic code generation.
*  Increasing amount of that kind of capability are programmers jobs threatened or is there still a significant role for you are programmers jobs threatened by the existence of stack overflow.
*  I don't think so it helps you take care of the boring stuff and.
*  You shouldn't try to use it to do something that you have no way of understanding what you're doing yet.
*  A tool like that is always best when the question you're asking is please remind me of how i do this which i.
*  I could do i could look up how to do it but.
*  Right now i forgotten whether the method is called foo or bar or how you what the shape of the API is does it use a builder object or a constructor or a factory or.
*  Something else and what are the parameters it serves that role it's like a great assistant.
*  The creative work of sort of deciding what you want what you want to go to do is totally yours.
*  What do you think is the future of python in the next 1020 50 years hundred years look forward everything about your imagine a future.
*  Human civilization for living inside the metaverse.
*  On mars human robots everywhere what part does python play in that.
*  It'll eventually become sort of a legacy language that plays an important role but that's that most people have never heard of and don't need to know about just like all kinds of.
*  Basic structures in in biology like mitochondria.
*  So it permeates all of life all of digital life but people just build on top of it and they only know the stuff that's on top of it yeah.
*  You guys you build layers of abstractions i mean most programmers nowadays rarely need to do binary arithmetic right.
*  Yep or even think about it or even learn about it or they can go quite far without knowing i started.
*  Building little digital circuits out of nand gates that i built myself with transistors and resistors so i'd sort of i feel very blessed that's.
*  With with that start when i was a teenager.
*  I i learned some of the basic at least concepts that that go into building a computer and i'd sort of every part.
*  I have some understanding what.
*  What it's for and why it's there and how it works and i can't forget about all that most of the time but i sort of.
*  I enjoy knowing oh if you go deeper you at some point you get to where nand gates and have adders and shift registers and.
*  When it comes to the point of how do you how do you actually make a chip out of silicon i have no idea that's just magic to me.
*  But you enjoy knowing that you can walk a while towards the lower and lower layers but you don't need to it's nice the other day as a sort of.
*  Mental exercise i was trying to figure out if i could build a.
*  Flip flop circuits out of relays who is just sort of.
*  Trying to remember how does it really really work yeah there's like this electromagnetic force that pulls a switch open or shut.
*  I can you can have have like you can open one switch in another shot another and.
*  I can have multiple contacts that go at once and how many relays do i really need to sort of represent one bit of information can the relay just feed on itself there was i don't think i got to the final solution but it was fun that i.
*  I could still do a little bit of problem solving and thinking at that level.
*  And it's cool how we build on top of each other so there's people that are just you stood on the shoulders of giants and there's others will stand on your shoulders and it's a giant beautiful higher yeah I feel I sort of cover cover this middle layer of the technology stack where.
*  I sort of Peters out below the.
*  The level of of of nan gates and at the top I sort of I lose track when it gets to machine learning.
*  And then eventually the machine learning will build higher and higher layers that will help us understand the lowest layer of the physics and thereby the universe figures out how.
*  It itself works maybe maybe not yeah i did i mean it's it's possible i mean if you think of human consciousness if that's even the right concept.
*  It's it's interesting that that's sort of we have this super parallel brain that does all these incredible parallel operations like image recognition.
*  I recognize your face.
*  Does you huge amount of processing that goes on in parallel there's lots of nerves between my eyes and my brain.
*  And the brain does a whole bunch of stuff all at once because actually really slow circuits but there are many of them that all work together.
*  On the other hand when i'm speaking everything is completely sequential.
*  I have to sort of string words together one at a time and when i'm thinking about stuff when i'm understanding the world.
*  I'm also thinking of everything like one step at a time.
*  And so we've we've sort of we've got all this this incredible.
*  Parallel circuitry in our brains and eventually we use that to simulate a single threaded much much higher level interpreter.
*  It's exactly i mean that's the illusion of it that's the illusion of it for us that is a single sequential.
*  Set of thoughts and all of that came from a single cell to the process of embryo genesis of DNA is the code.
*  DNA holds the entirety of the code the information and how to use that information to build up an organism the entire like.
*  The arms the legs the brain so you don't buy a computer you buy like a you buy a seed diagram and then you plant the computer and it builds itself in almost the same way.
*  And then does the computation and then is eventually dies it gets stale but gives birth to young computers.
*  More and more and gives them lessons but they figure stuff out on their own and over time it goes on that way and those computers when they go to college tried to figure out how to program and they built their own little computers.
*  They're increasingly more intelligent increasingly higher and higher levels of abstractions is it interesting that that you sort of you see the same thing appearing at different levels though because you have like.
*  Cells that that create new cells.
*  And eventually that builds a whole organism but then the animal or the plant or the human has its own mechanism of replication.
*  That that is is sort of connected in a very complicated way to the mechanism of replication of the cells and then if you if you look inside the cell if you see how DNA and proteins are.
*  Are connected then there is yet another completely different mechanism whereby proteins are mass produced.
*  Using enzymes and and and a little bit of code from from DNA and of course viruses break into it at that level.
*  And while the mechanisms might be different it seems like the nature of the mechanism is the same and it cares across natural languages and programming languages humans.
*  Maybe even human civilizations or intelligence civilizations and then all the way down to the single cell organ.
*  It is fascinating to see what abstraction levels are built on top of individual humans and how you have like whole societies.
*  That that sort of have a similar self preservation.
*  I don't know what it is instinct nature abstraction as the individuals have and the cells have and then they self replicate and breed in different ways.
*  It's hard for us humans to introspect it because we were very focused on our particular layer of abstraction but from an alien perspective looking on earth they'll they'll probably see the higher level organism of human civilization.
*  As part of this bigger organism of life on earth itself in fact that could be an organism just alone just life life life on earth.
*  This is been a wild both philosophical and technical conversation with your your an amazing human being your.
*  You were gracious enough to talk to me when I was first students podcast when the earliest first people have talked to somebody I admired for a long time is just a huge honor that you did it at that time you do it again you're awesome.
*  Thanks for listening to this conversation with Guido been awesome to support this podcast please check out our sponsors in the description and now let me leave you some words from Oscar wild experience is the name that everyone gives to their mistakes Thank you for listening and hope to see you next time.
