---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 6433s
Video Keywords: []
Video Views: 1065382
Video Rating: None
Video Description: 
---

# Bjarne Stroustrup C++  Lex Fridman Podcast #48
**Lex Fridman:** [November 07, 2019](https://www.youtube.com/watch?v=uTxRF5ag27A)
*  The following is a conversation with Bjorn Stjarlström. He's the creator of C++, a programming language that after 40 years is still one of the most popular and powerful languages in the world.
*  Its focus on fast, stable, robust code underlies many of the biggest systems in the world that we have come to rely on as a society.
*  If you're watching this on YouTube, for example, many of the critical back-end components of YouTube are written in C++.
*  Same goes for Google, Facebook, Amazon, Twitter, most Microsoft applications, Adobe applications, most database systems, and most physical systems that operate in the real world like cars, robots, rockets that launch us into space and one day will land us on Mars.
*  C++ also happens to be the language that I use more than any other in my life.
*  I've written several hundred thousand lines of C++ source code.
*  Of course, lines of source code don't mean much, but they do give hints of my personal journey through the world of software.
*  I've enjoyed watching the development of C++ as a programming language, leading up to the big update in the standard in 2011 and those that followed in 14, 17, and toward the new C++ 20 standard, hopefully coming out next year.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube, give it five stars on iTunes, support it on Patreon, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  And now here's my conversation with Bjorn Stroustrup.
*  What was the first program you've ever written?
*  Do you remember?
*  It was my second year in university, first year of computer science, and it was in Alcoa 60.
*  I calculated the shape of a super ellipse and then connected points on the perimeter, creating star patterns.
*  It was with a wet ink on a paper printer.
*  And that was in college, university?
*  Yeah.
*  I learned to program the second year in university.
*  What was the first programming language, if I may ask it this way, that you fell in love with?
*  I think Alcoa 60.
*  And after that, I remember Snowball.
*  I remember Fortran, didn't fall in love with that.
*  I remember Pascal, didn't fall in love with that.
*  It all got in the way of me.
*  And then I discovered Assembler, and that was much more fun.
*  And from there, I went to Microcode.
*  So you were drawn to the, you found the low-level stuff beautiful.
*  I went through a lot of languages, and then I spent significant time in Assembler and Microcode.
*  That was sort of the first really profitable things.
*  And I paid for my masters, actually.
*  And then I discovered Simula, which was absolutely great.
*  Simula?
*  Simula was the extension of Alcoa 60, done primarily for simulation.
*  But basically, they invented object-oriented programming at inheritance and runtime polymorphism while they were doing it.
*  And that was the language that taught me that you could have the sort of the problems of a program grow with the size of the program rather than with the square of the size of the program.
*  That is, you can actually modularize very nicely.
*  And that was a surprise to me.
*  It was also a surprise to me that a stricter type system than Pascal's was helpful, whereas Pascal's type system got in my way all the time.
*  So you need a strong type system to organize your code well, but it has to be extensible and flexible.
*  Let's get into the details a little bit.
*  If you remember, what kind of type system did Pascal have?
*  What type system, typing system did Alcoa 60 have?
*  Basically, Pascal was sort of the simplest language that Niklaus Wirt could define that served the needs of Niklaus Wirt at the time.
*  And it has a sort of a highly moral tone to it.
*  That is, if you can say it in Pascal, it's good.
*  And if you can't, it's not so good.
*  Whereas Simula allowed you basically to build your own type system.
*  So instead of trying to fit yourself into Niklaus Wirt's world, Christen Nygård's language and Ulrich Dahl's language allowed you to build your own.
*  So it's sort of close to the original idea of you build a domain specific language.
*  As a matter of fact, what you build is a set of types and relations among types that allows you to express something that's suitable for an application.
*  So when you say types, the stuff you're saying has echoes of object-oriented programming.
*  Yes, they invented it.
*  Every language that uses the word class for type is a descendant of Simula, directly or indirectly.
*  Christen Nygård and Ulrich Dahl were mathematicians and they didn't think in terms of types,
*  but they understood sets and classes of elements and so they called their types classes.
*  And basically in C++, as in Simula, classes are user-defined type.
*  So can you try the impossible task and give a brief history of programming languages from your perspective?
*  So we started with Algol 60, Simula, Pascal, but that's just the 60s and 70s.
*  I can try.
*  The most sort of interesting and major improvement of programming languages was Fortran, the first Fortran,
*  because before that all code was written for a specific machine and each specific machine had a language,
*  a simple language or a cross-semple or some extension of that idea.
*  But you are writing for a specific machine in the language of that machine.
*  And,
*  Bacchus and his team at IBM built a language that would allow you to write what you really wanted.
*  That is, you could write it in a language that was natural for people.
*  Now these people happen to be engineers and physicists,
*  so the language that came out was somewhat unusual for the rest of the world.
*  But basically they said formula translation because they wanted to have the mathematical formulas translated into the machine.
*  And as a side effect, they got portability because now they are writing in the terms that the humans used and the way humans thought.
*  And then they had a program that translated it into the machine's needs.
*  And that was new and that was great.
*  And it's something to remember.
*  We want to raise the language to the human level, but we don't want to lose the efficiency.
*  So, and that was the first step towards the human.
*  That was the first step.
*  And of course, there were very particular kind of humans.
*  Business people were different, so they got cobalt instead and etc.
*  And Simula came out.
*  No, let's not go to Simula yet.
*  Let's go to Algor.
*  Fortran didn't have at the time the notions of, not a precise notion of type, not a precise notion of scope,
*  not a set of translation phases that was what we have today, lexical, syntax, semantics.
*  It was sort of a bit of a model in the early days, but hey, they had just done the biggest breakthrough in the history of programming, right?
*  So you can't criticize them for not having gotten all the technical details right.
*  So we got Algor.
*  That was very pretty.
*  And most people in commerce and science considered it useless because it was not flexible enough and it wasn't efficient enough and etc.
*  But that was a breakthrough from a technical point of view.
*  Then Simula came along to make that idea more flexible and you could define your own types.
*  And that's where I got very interested.
*  Preston Nygaard, who's the main idea man behind Simula.
*  That was late 60s.
*  This was late 60s.
*  I was a visiting professor in Aarhus.
*  And so I learned object oriented programming by sitting around and well, in theory, discussing with Christen Nygaard.
*  But Preston, once you get started and in full flow, it's very hard to get a word in edgeways.
*  You just listen.
*  So it was great.
*  I learned it from there.
*  Not to romanticize the notion, but it seems like a big leap to think about object oriented programming.
*  It's really a leap of abstraction.
*  Yes.
*  And was that as big and beautiful of a leap as it seems from now in retrospect or was it an obvious one at the time?
*  It was not obvious.
*  And many people have tried to do something like that.
*  And most people didn't come up with something as wonderful as Simula.
*  Lots of people got their PhDs and made their careers out of forgetting about Simula or never knowing it.
*  For me, the key idea was basically I could get my own types.
*  And that's the idea that goes further into C++ where I can get better types and more flexible types and more efficient types.
*  But it's still the fundamental idea.
*  And when I want to write a program, I want to write it with my types that is appropriate to my problem and under the constraints that I'm under with hardware, software, environment, etc.
*  And that's the key idea.
*  People picked up on the class hierarchies and the virtual functions and the inheritance.
*  And that was only part of it.
*  It was an interesting and major part and still a major part in a lot of graphic stuff.
*  But it was not the most fundamental.
*  It was when you wanted to relate one type to another, you don't want them all to be independent.
*  The classical example is that you don't actually want to write a city simulation with vehicles where you say,
*  well, if it's a bicycle, write the code for turning a bicycle to the left.
*  If it's a normal car, turn right the normal car way.
*  If it's a fire engine, turn right the fire engine way.
*  You get these big case statements and bunches of if statements and such.
*  Instead, you tell the base class that that's the vehicle and say turn left the way you want to.
*  And this is actually a real example.
*  They used it to simulate and optimize the emergency services for somewhere in Norway back in the 60s.
*  So this was one of the early examples for why you needed inheritance and you needed a runtime polymorphism
*  because you wanted to handle this set of vehicles in a manageable way.
*  You can't just rewrite your code each time a new kind of vehicle comes along.
*  Yeah, that's a beautiful, powerful idea.
*  And of course, it stretches through your work with C++, as we'll talk about.
*  But I think you structured it nicely.
*  What other breakthroughs came along in the history of programming languages?
*  If we were to tell the history in that way?
*  Obviously, I'm better at telling the part of the history that is the path I'm on as opposed to all the path.
*  Yeah, you skipped the hippie John McCarthy and Lisp, one of my favorite languages.
*  But Lisp is not one of my favorite languages.
*  It's obviously important.
*  It's obviously interesting.
*  Lots of people write code in it and then they rewrite it into C or C++ when they want to go to production.
*  It's in the world I'm at, which are constrained by performance,
*  reliability issues, deployability, cost of hardware.
*  I don't like things to be too dynamic.
*  It is really hard to write a piece of code that's perfectly flexible that you can also deploy on a small computer
*  and that you can also put in, say, a telephone switch in Bogota.
*  What's the chance?
*  If you get an error and you find yourself in the debugger that the telephone switch in Bogota on late Sunday night has a programmer around.
*  The chance is zero.
*  And so a lot of things I think most about can't afford that flexibility.
*  I'm quite aware that maybe 70, 80 percent of all code are not under the kind of constraints I'm interested in.
*  But somebody has to do the job I'm doing because you have to get from these high level flexible languages to the hardware.
*  The stuff that lasts for 10, 20, 30 years is robust, operates under very constrained conditions.
*  Yes, absolutely.
*  That's right.
*  And it's fascinating and beautiful in its own way.
*  It's C++ is one of my favorite languages.
*  And so is Lisp.
*  So I can embody it too for different reasons as a programmer.
*  I understand why Lisp is popular and I can see the beauty of the ideas.
*  And similarly with Smalltalk.
*  It's just not as relevant in my world.
*  And by the way, I distinguish between those and the functional languages where I go to things like ML and Haskell.
*  Different kind of languages.
*  They have a different kind of beauty and they're very interesting.
*  And I actually try to learn from all the languages I encounter to see what is there that would make working on the kind of problems I'm interested in with the kind of constraints that I'm interested in.
*  What can actually be done better?
*  Because we can surely do better than we do today.
*  You've said that it's good for any professional programmer to know at least five languages.
*  Speaking about a variety of languages that you've taken inspiration from and you've listed yours as being at least at the time C++, obviously Java, Python, Ruby and JavaScript.
*  Can you first of all update that list, modify it?
*  You don't have to be constrained to just five, but can you describe what you picked up also from each of these languages?
*  How you see them as inspirations for even your work with C++?
*  This is a very hard question to answer.
*  So about languages, you should know languages.
*  I reckon I knew about 25 or thereabouts when I did C++.
*  It was easier in those days because the languages were smaller and you didn't have to learn a whole programming environment and such to do it.
*  You could learn the language quite easily and it's good to learn so many languages.
*  And I imagine just like with natural language for communication, there's different paradigms that emerge in all of them.
*  Yeah.
*  That there's commonalities and so on.
*  So I picked five out of a hat.
*  You picked five out of a hat.
*  Obviously.
*  The important thing that the number is not one.
*  That's right.
*  It's like I don't like, I mean if you're monoglot, you are likely to think that your own culture is the only one superior to everybody else's.
*  A good learning of a foreign language and a foreign culture is important.
*  It helps you think and be a better person.
*  With programming languages, you become a better programmer, better designer with the second language.
*  Now, once you've got two, the wait of five is not that long.
*  It's the second one that's most important.
*  And then when I had to pick five, I sort of thinking what kinds of languages are there?
*  Well, there's a really low level stuff.
*  It's good.
*  It's actually good to know machine code.
*  Even still?
*  Sorry, even today.
*  The C++ optimizers write better machine code than I do.
*  Yes.
*  But I don't think I could appreciate them if I actually didn't understand machine code and machine architecture.
*  At least in my position, I have to understand a bit of it because you mess up the cache and you're off in performance by a factor of 100.
*  Right?
*  It shouldn't be that if you are interested in either performance or the size of the computer you have to deploy.
*  So I would go as a simpler.
*  I used to mention C, but these days going low level is not actually what gives you the performance.
*  It is to express your ideas so cleanly that you can think about it and the optimizer can understand what you're up to.
*  My favorite way of optimizing these days is throw out the clever bits and see if it still runs fast.
*  And sometimes it runs faster.
*  So I need the abstraction mechanisms or something like C++ to write compact high performance code.
*  There was a beautiful keynote by Jason Turner at the CPPCon a couple of years ago where he decided he was going to program Pong
*  on Motorola 6800, I think it was.
*  And he says, well, this is relevant because it looks like a microcontroller.
*  It has specialized hardware. It has not very much memory and it's relatively slow.
*  And so he shows in real time how he writes Pong, starting with fairly straightforward, low level stuff, improving his subtractions.
*  And what he's doing is writing C++ and it translates into 86Assembler, which you can do with Clang.
*  And you can see it in real time. It's the Compiler Explorer, which you can use on the web.
*  And then he wrote a little program that translated 86Assembler into MotorolaAssembler.
*  And so he types and you can see this thing in real time.
*  Wow. You can see it in real time.
*  And even if you can't read the assembly code, you can just see it.
*  His code gets better. The code, the assembler gets smaller.
*  He increases the abstraction level, uses C++ 11 as it were better.
*  This code gets cleaner. It gets easier to maintain.
*  The code shrinks and it keeps shrinking.
*  And I could not in any reasonable amount of time write that assembler as good as the compiler generated from really quite nice modern C++.
*  And I'll go as far as to say that the thing that looked like C was significantly uglier and smaller when it became and larger when it became machine code.
*  So the abstractions that can be optimized are important.
*  I would love to see that kind of visualization in larger code bases.
*  Yeah. That might be beautiful.
*  But you can't show a larger code base in a one hour talk and have it fit on screen.
*  Right. So that's C and C++.
*  So my two languages would be machine code and C++.
*  And then I think you can learn a lot from the functional languages.
*  So PIC has colloid ML. I don't care which.
*  I think actually you learn the same lessons of expressing especially mathematical notions really clearly and having the type system that's really strict.
*  And then you should probably have a language for sort of quickly churning out something.
*  You could pick JavaScript. You could pick Python.
*  You could pick Ruby.
*  What do you make of JavaScript in general?
*  So you kind of you're talking in the platonic sense about languages, about what they're good at, what their philosophy of design is.
*  But there's also a large user base behind each of these languages and they use it in the way sometimes maybe it wasn't really designed for.
*  That's right.
*  JavaScript is used way beyond probably what it was designed for.
*  Let me say it this way.
*  When you build a tool, you do not know how it's going to be used.
*  You try to improve the tool by looking at how it's being used and when people cut their fingers off and try and stop that from happening.
*  But really you have no control over how something is used.
*  So I'm very happy and proud of some of the things C++ being used at and some of the things I wish people wouldn't do.
*  Bitcoin mining being my favorite example uses as much energy as Switzerland and mostly serves criminals.
*  Yeah.
*  But back to the languages, I actually think that having JavaScript run in the browser was an enabling thing for a lot of things.
*  Yes, you could have done it better, but people were trying to do it better and they were using sort of more principles, language designs, but they just couldn't do it right.
*  And the non-professional programmers that write lots of that code just couldn't understand them.
*  So it did an amazing job for what it was.
*  It's not the prettiest language and I don't think it ever will be the prettiest language, but that's not bigots here.
*  So what was the origin story of C++?
*  You basically gave a few perspectives of your inspiration of object oriented programming.
*  That you had a connection with C and performance efficiency was an important thing you were drawn to.
*  Efficiency and reliability.
*  Reliability.
*  You have to get both.
*  What's reliability?
*  I really want my telephone calls to get through and I want the quality of what I am talking coming out at the other end.
*  The other end might be in London or wherever.
*  So and you don't want the system to be crashing.
*  If you're doing a bank, you mustn't crash.
*  It might be your bank account that is in trouble.
*  There's different constraints like in games.
*  It doesn't matter too much if there's a crash.
*  Nobody dies and nobody gets ruined.
*  But I'm interested in the combination of performance, partly because of sort of speed of things being done.
*  Part of being able to do things that is necessary to have reliability of larger systems.
*  If you spend all your time interpreting a simple function call,
*  you are not going to have enough time to do proper signal processing to get the telephone calls to sound right.
*  Either that or you have to have 10 times as many computers and you can't afford your phone anymore.
*  It's a ridiculous idea in the modern world because we have solved all of those problems.
*  I mean, they keep popping up in different ways because we tackle bigger and bigger problems.
*  Efficiency remains always an important aspect.
*  But you have to think about efficiency, not just as speed, but as an enabler to important things.
*  And one of the things it enables is reliability, is dependability.
*  When I press the pedal, the brake pedal of a car, it is not actually connected directly to anything but a computer.
*  That computer better work.
*  Let's talk about reliability just a little bit.
*  So modern cars have ECUs, millions of lines of code today.
*  So this is certainly especially true of autonomous vehicles where some of the aspects of the control or driver assistance systems that steer the car, that keep it in the lane and so on.
*  So how do you think, you know, I talked to regulators, people in government who are very nervous about testing the safety of these systems of software.
*  Ultimately, software that makes decisions that could lead to fatalities.
*  So how do you how do we test software systems like these?
*  First of all, safety like performance and like security is a systems property.
*  People tend to look at one part of a system at a time and saying something like this is secure.
*  That's all right.
*  I don't need to do that.
*  Yeah, that piece of code is secure.
*  I'll buy your operator.
*  If you want to have reliability, if you want to have performance, if you want to have security, you have to look at the whole system.
*  I did not expect you to say that, but that's very true.
*  Yes, I'm dealing with one part of the system and I want my part to be really good, but I know it's not the whole system.
*  Furthermore, if making an individual part perfect.
*  May actually not be the best way of getting the highest degree of reliability and performance and such.
*  The people say C++ type safe, not type safe.
*  You can break it.
*  Sure, I can break anything that runs on a computer.
*  I may not go through your type system.
*  If I wanted to break into your computer, I'll probably try SQL injection.
*  It's very true.
*  If you think about safety or even reliability at a system level, especially when a human being is involved, it starts becoming hopeless pretty quickly in terms of proving that something is safe to a certain level.
*  Yeah, because there's so many variables.
*  It's so complex.
*  Well, let's get back to something we can talk about and actually make some progress on.
*  Yes.
*  We can look at C++ programs and we can try and make sure they crash less often.
*  The way you do that is largely by simplification.
*  It is not the first step is to simplify the code, have less code, have code that are less likely to go wrong.
*  It's not by runtime testing everything.
*  It is not by big test frameworks that you are using.
*  Yes, we do that also.
*  But the first step is actually to make sure that when you want to express something, you can express it directly in code rather than going through endless loops and convolutions in your head before it gets down the code.
*  That if the way you are thinking about a problem is not in the code, there is a missing piece that's just in your head and the code, you can see what it does, but it cannot see what you thought about it unless you have expressed things directly.
*  When you express things directly, you can maintain it.
*  It's easier to find errors.
*  It's easier to make modifications.
*  It's actually easier to test it and lo and behold, it runs faster.
*  And therefore, you can use a smaller number of computers, which means there's less hardware that could possibly break.
*  So I think the key here is simplification, but it has to be to use the Einstein quote as simple as possible and no simpler.
*  Not simpler.
*  There are other areas with under constraints where you can be simpler than you can be in C++, but in the domain I'm dealing with, that's the simplification I'm after.
*  So how do you inspire or ensure that the Einstein level of simplification is reached?
*  So can you do code review?
*  Can you look at code?
*  Is there, if I gave you the code for the Ford F-150 and said here, is this a mess or is this okay?
*  Is it possible to tell?
*  Is it possible to regulate?
*  An experienced developer can look at code and see if it smells.
*  I mixed metaphors deliberately.
*  Yes.
*  The point is that it is hard to generate something that is really obviously clean and can be appreciated,
*  but you can usually recognize when you haven't reached that point.
*  And so if I have never looked at the F-150 code, so I wouldn't know, but I know what I would be looking for.
*  There I'll be looking for some tricks that correlate with bugs and elsewhere.
*  And I have tried to formulate rules for what good code looks like.
*  And the current version of that is called the C++ core guidelines.
*  One thing people should remember is there's what you can do in a language and what you should do.
*  In a language, you have lots of things that is necessary in some context, but not in others.
*  There's things that exist just because there's 30-year-old code out there and you can't get rid of it.
*  But you can't have rules that say, when you create it, try and follow these rules.
*  This does not create good programs by themselves, but it limits the damage of mistakes.
*  It limits the possibilities of mistakes.
*  And basically, we are trying to say, what is it that a good programmer does at the fairly simple level of where you use the language and how you use it.
*  Now, I can put all the rules for chiseling in Marlboro.
*  It doesn't mean that somebody who follows all of those rules can do a masterpiece by Michelangelo.
*  That is, there's something else to write a good program, just as there's something else to create an important work of art.
*  That is, there's some kind of inspiration, understanding, gift.
*  But we can approach the sort of technical craftsmanship level of it.
*  The famous painters, the famous sculptures was, among other things, superb craftsmen.
*  They could express their ideas using their tools very well.
*  And so these days, I think what I'm doing, what a lot of people are doing,
*  we are still trying to figure out how it is to use our tools very well.
*  For a really good piece of code, you need a spark of inspiration.
*  And you can't, I think, regulate that.
*  You cannot say that I'll take a picture only, I'll buy your picture only if you're at least Van Gogh.
*  There are other things you can regulate, but not the inspiration.
*  I think that's quite beautifully put.
*  It is true that there is, as an experienced programmer, when you see code that's inspired,
*  that's like Michelangelo, you know it when you see it.
*  And the opposite of that is code that is messy, code that smells, you know when you see it.
*  And I'm not sure you can describe it in words, except vaguely through guidelines and so on.
*  It's easier to recognize ugly than to recognize beauty in code.
*  And the reason is that sometimes beauty comes from something that's innovative and unusual.
*  And you have to sometimes think reasonably hard to appreciate that.
*  On the other hand, the messes have things in common.
*  And you can have static checkers and dynamic checkers that find a large number of the most common mistakes.
*  You can catch a lot of sloppiness mechanically.
*  I'm a great fan of static analysis in particular, because you can check for not just the language rules,
*  but for the usage of language rules.
*  And I think we will see much more static analysis in the coming decade.
*  Can you describe what static analysis is?
*  You represent a piece of code so that you can write a program that goes over that representation
*  and look for things that are right and not right.
*  So for instance, you can analyze a program to see if resources are leaked.
*  That's one of my favorite problems.
*  It's not actually all that hard in Modern C++, but you can do it.
*  If you are writing in the C level, you have to have a malloc and a free.
*  And they have to match.
*  If you have them in a single function, you can usually do it very easily.
*  If there's a malloc here, there should be a free there.
*  On the other hand, in between can be showing complete code and then it becomes impossible.
*  If you pass that pointer to the memory out of a function and then want to make sure that the free is done somewhere else,
*  now it gets really difficult.
*  And so for static analysis, you can run through a program and you can try and figure out if there's any leaks.
*  And what you will probably find is that you will find some leaks and you'll find quite a few places where your analysis can't be complete.
*  It might depend on runtime.
*  It might depend on the cleverness of your analyzer.
*  And it might take a long time.
*  Some of these programs run for a long time.
*  But if you combine such analysis with a set of rules, that says how people could use it,
*  you can actually see why the rules are violated.
*  And that stops you from getting into the impossible complexities.
*  You don't want to solve the holding problem.
*  So static analysis is looking at the code without running the code.
*  Yes.
*  And thereby it's almost not a production code, but it's almost like an educational tool of how the language should be used.
*  It guides you like it at its best, right?
*  It would guide you in how you write future code as well and you learn together.
*  Yes.
*  So basically you need a set of rules for how you use the language.
*  Then you need a static analysis that catches your mistakes when you violate the rules
*  or when your code ends up doing things that it shouldn't despite the rules,
*  because there is the language rules.
*  We can go further.
*  And again, it's back to my idea that I would much rather find errors before I start running the code.
*  If nothing else, once the code runs, if it catches an error at runtime,
*  I have to have an error handler.
*  And one of the hardest things to write in code is error handling code, because you know something went wrong.
*  Do you know really exactly what went wrong?
*  Usually not.
*  How can you recover when you don't know what the problem was?
*  You can't be 100% sure what the problem was in many, many cases.
*  And this is part of it.
*  So yes, we need good languages with good type systems.
*  We need rules for how to use them.
*  We need static analysis.
*  And the ultimate for static analysis is of course program proof,
*  but that still doesn't scale to the kind of systems we deploy.
*  Then we start needing testing and the rest of the stuff.
*  So C++ is an object-oriented programming language that creates,
*  especially with its newer versions, as we'll talk about, higher and higher levels of abstraction.
*  So how do you design?
*  Let's even go back to the origin of C++.
*  How do you design something with so much abstraction that's still efficient
*  and is still something that you can manage, do static analysis on,
*  you can have constraints on, they can be reliable, all those things we've talked about.
*  To me, slightly, there's a slight tension between high level abstraction and efficiency.
*  That's a good question.
*  I could probably have a year's course just trying to answer it.
*  Yes, there's a tension between efficiency and abstraction,
*  but you also get the interesting situation that you get the best efficiency out of the best abstraction.
*  And my main tool for efficiency for performance actually is abstraction.
*  So let's go back to how C++ got there.
*  You said it was object-oriented programming language.
*  I actually never said that.
*  It's always quoted, but I never did.
*  I said C++ supports object-oriented programming and other techniques.
*  And that's important because I think that the best solution to most complex,
*  interesting problems require ideas and techniques from things that has been called object-oriented,
*  data abstraction, functional, traditional C-style code, all of the above.
*  And so when I was designing C++, I soon realized I couldn't just add features.
*  If you just add what looks pretty or what people ask for or what you think is good,
*  one by one, you're not going to get a coherent whole.
*  What you need is a set of guidelines that guide your decisions.
*  Should this feature be in or should this feature be out?
*  How should a feature be modified before it can go in and such?
*  And in the book I wrote about that, that's sign and evolution of C++,
*  there's a whole bunch of rules like that.
*  Most of them are not language technical.
*  There are things like don't violate static type system,
*  because I like static type system for the obvious reason that I like things to be reliable on reasonable amounts of hardware.
*  But one of these rules is the zero overhead principle.
*  The what kind of principle?
*  The zero overhead principle.
*  It basically says that if you have an abstraction,
*  it should not cost anything compared to write the equivalent code at a lower level.
*  So if I have, say, a matrix multiply,
*  it should be written in such a way that you could not drop to the C level of abstraction
*  and use arrays and pointers and such and run faster.
*  And so people have written such matrix multiplications
*  and they've actually gotten code that ran faster than Fortran,
*  because once you had the right abstraction, you can eliminate,
*  you can eliminate temporaries and you can do loop fusion and other good stuff like that.
*  That's quite hard to do by hand and in a lower level language.
*  And there's some really nice examples of that.
*  And the key here is that that matrix multiplication,
*  the matrix abstraction allows you to write code that's simple and easy.
*  You can do that in any language.
*  But with C++, it has the features so that you can also have this thing run faster than if you hand coded it.
*  Now, people have given that lecture many times, I and others,
*  and a very common question after the talk where you have demonstrated that you can outperform Fortran for dense matrix multiplication,
*  people come up and say, yeah, but there are C++.
*  If I rewrote your code and see how much faster would it run?
*  The answer is much slower.
*  This happened the first time actually back in the 80s with a friend of mine called Doug McElroy,
*  who demonstrated exactly this effect.
*  And so the principle is you should give programmers the tools so that the abstractions can follow the zero-way principle.
*  Furthermore, when you put in a language feature in C++ or a standard library feature, you try to meet this.
*  It doesn't mean it's absolutely optimal,
*  but it means if you hand code it with the usual facilities in the language in C++ in C,
*  you should not be able to better it.
*  Usually you can do better if you use embedded assembler for machine code for some of the details to utilize part of a computer that the compiler doesn't know about.
*  But you should get to that point before you beat the abstraction.
*  So that's a beautiful ideal to reach for.
*  And we meet it quite often.
*  Quite often.
*  So where's the magic of that coming from?
*  Some of it is the compilation process, so the implementation of C++.
*  Some of it is the design of the feature itself, the guidelines.
*  So I've recently and often talked to Chris Latner, so Klang.
*  What, just out of curiosity, is your relationship in general with the different implementations of C++,
*  as you think about you and committee and other people in C++,
*  think about the design of new features or design of previous features.
*  In trying to reach the ideal of zero overhead,
*  does the magic come from the design, the guidelines, or from the implementations?
*  And, not all.
*  You go for programming technique, programming language features, and implementation techniques.
*  You need all three.
*  And how can you think about all three at the same time?
*  It takes some experience, it takes some practice, and sometimes you get it wrong,
*  but after a while you sort of get it right.
*  I don't write compilers anymore.
*  But Brian Kernighan pointed out that one of the reasons C++ succeeded
*  was some of the craftsmanship I put into the early compilers.
*  And of course I did the language design,
*  and of course I wrote a fair amount of code using this kind of stuff.
*  And I think most of the successes involves progress in all three areas together.
*  A small group of people can do that.
*  Two, three people can work together to do something like that.
*  It's ideal if it's one person that has all the skills necessary,
*  but nobody has all the skills necessary in all the fields where C++ is used.
*  So if you want to approach my ideal in, say, concurrent programming,
*  you need to know about algorithms of concurrent programming,
*  you need to know the trigger of lock-free programming,
*  you need to know something about compiler techniques,
*  and then you have to know some of the application areas where this is,
*  like some forms of graphics or some forms of what we call a web server kind of stuff.
*  And that's very hard to get into a single head, but small groups can do it too.
*  So is there differences in your view, not saying which is better or so on,
*  but difference in the different implementations of C++?
*  Why are there several sort of maybe naive questions for me?
*  GCC, Clang, so on?
*  This is a very reasonable question.
*  When I designed C++,
*  most languages had multiple implementations,
*  because if you run on an IBM, if you run on a Sun, if you run on a Motorola,
*  there was just many, many companies, and they each have their own compilation structure,
*  and their own compilers.
*  It was just fairly common that there was many of them.
*  And I wrote Cfront, assuming that other people would write compilers with C++ if I was successful.
*  And furthermore, I wanted to utilize all the backend infrastructures that were available.
*  I soon realized that my users were using 25 different linkers.
*  I couldn't write my own linker.
*  Yes, I could, but I couldn't write 25 linkers and also get any work done on the language.
*  And so it came from a world where there was many linkers, many optimizers, many compiler frontends,
*  not to start, but many operating systems.
*  The whole world was not an 86 and a Linux box or something, whatever is the standard today.
*  In the old days, they set a set of X.
*  So basically, I assumed there would be lots of compilers.
*  It was not a decision that there should be many compilers.
*  It was just a fact. That's the way the world is.
*  And yes, many compilers emerged.
*  And today, there's at least four frontends, Clang, GCC, Microsoft, and EDG.
*  It is the design group.
*  They supply a lot of the independent organizations and the embedded systems industry.
*  And there's lots and lots of backends.
*  We have to think about how many dozen backends there are.
*  Because different machines have different things, especially in the embedded world,
*  the machines are very different. The architectures are very different.
*  And so having a single implementation was never an option.
*  Now, I also happen to dislike monocultures.
*  Monocultures?
*  They are dangerous.
*  Because whoever owns the monoculture can go stale, and there's no competition,
*  and there's no incentive to innovate.
*  There's a lot of incentive to put barriers in the way of change.
*  Because, hey, we own the world, and it's a very comfortable world for us.
*  And who are you to mess with that?
*  So I really am very happy that there's four frontends for C++.
*  Clang's great, but GCC was great.
*  But then it got somewhat stale.
*  Clang came along, and GCC is much better now.
*  Competition is good.
*  Microsoft is much better now.
*  So at least a low number of frontends puts a lot of pressure on standards compliance
*  and also on performance and error messages and compile time speed,
*  all this good stuff that we want.
*  Do you think, crazy question, there might come along,
*  do you hope there might come along implementation of C++ written,
*  given all its history, written from scratch?
*  So written today from scratch?
*  Well, Clang and the LLVM is more or less written from scratch.
*  But there's been C++ 11, 14, 17, 20.
*  I think sooner or later somebody is going to try again.
*  There's been attempts to write new C++ compilers,
*  and some of them has been used,
*  and some of them has been absorbed into others and such.
*  Yeah, it'll happen.
*  So what are the key features of C++?
*  And let's use that as a way to sort of talk about the evolution of C++, the new feature.
*  So at the highest level, what are the features that were there in the beginning?
*  What features got added?
*  Let's first get a principle or an aim in place.
*  C++ is for people who want to use hardware really well
*  and then manage the complexity of doing that through abstraction.
*  And so the first facility you have is a way of manipulating the machines at a fairly low level.
*  It looks very much like C.
*  It has loops, it has variables, it has pointers like machine addresses.
*  It can access memory directly.
*  It can allocate stuff in the absolute minimum of space needed on the machine.
*  There's a machine-facing part of C++, which is roughly equivalent to C.
*  I said C++ could beat C, and it can.
*  It doesn't mean I dislike C. If I disliked C, I wouldn't have built on it.
*  Furthermore, after Dennis Ritchie, I'm probably the major contributor to modern C.
*  And well, I had lunch with Dennis most days for 16 years, and we never had a harsh word between us.
*  So these C versus C++ fights are for people who don't quite understand what's going on.
*  Then the other part is the abstraction.
*  And there the key is the class, which is a user-defined type.
*  And my idea for the class is that you should be able to build a type that's just like the built-in types
*  in the way you use them, in the way you declare them, in the way you get the memory.
*  And you can do just as well. So in C++ as in C, you should be able to build an abstraction,
*  a class, which we can call capital int, that you can use exactly like an integer and run just as fast as an integer.
*  There's the idea right there. And of course, you probably don't want to use the int itself, but it has happened.
*  People have wanted integers that were range-checked so that you couldn't overflow and such,
*  especially for very safety critical applications like the fuel injection for a marine diesel engine for the largest ships.
*  This is a real example, by the way. This has been done.
*  They built themselves an integer that was just like integer, except that it couldn't overflow.
*  If there was an overflow, you went into the error handling.
*  And then you built more interesting types. You can build a matrix, which you need to do graphics,
*  or you could build a gnome for a video game.
*  And all of these are classes and they appear just like the built-in types in terms of efficiency and so on.
*  So what else is there?
*  And flexibility.
*  So, I don't know, for people who are not familiar with object oriented programming, there's inheritance.
*  There's a hierarchy of classes. You can just like you said, create a generic vehicle that can turn left.
*  So what people found was that you don't actually know. How do I say this?
*  A lot of types are related. That is, the vehicles, all vehicles are related.
*  Bicycles, cars, fire engines, tanks. They have some things in common and some things that differ.
*  And you would like to have the common things common and having the differences specific.
*  And when you didn't want to know about the differences, like just turn left.
*  You don't have to worry about it. That's how you get the traditional object oriented programming coming out of Simula,
*  adopted by Smalltalk and C++ and all the other languages.
*  The other kind of obvious similarity between types comes when you have something like a vector.
*  Fortran gave us the vector called a ray of doubles.
*  But the minute you have a vector of doubles, you want a vector of double precision doubles and for short doubles, for graphics.
*  And why should you not have a vector of integers while you're at it or a vector of vectors and a vector of vectors of chess pieces?
*  Now you have a board. Right?
*  So this is you express the commonality as the idea of a vector and the variations come through parameterization.
*  And so here we get the two fundamental ways of abstracting or of having similarities of types in C++.
*  There's the inheritance and there's a parameterization.
*  There's the object oriented programming and there's the generic programming with the templates for the generic programming.
*  So you've presented it very nicely, but now you have to make all that happen and make it efficient.
*  So generic programming with templates, there's all kinds of magic going on, especially recently that you can help catch up on.
*  But it feels to me like you can do way more than what you just said with templates.
*  You can start doing this kind of meta programming, this kind of.
*  You can do meta programming also. I didn't go there in that explanation.
*  We're trying to be very basics, but go back on to the implementation.
*  Implementation.
*  If you couldn't implement this efficiently, if you couldn't use it so that it became efficient, it has no place in C++ because it will violate the zero.
*  So when I had to get object oriented programming inheritance, I took the idea of virtual functions from Simula.
*  Virtual functions is a similar term. Class is a similar term.
*  If you ever use those words, say thanks to Christian Nygård and Ole Johan Dahl.
*  And I did the simplest implementation I knew of, which was basically a jump table.
*  So you get the virtual function table, the function goes in, does an interaction through a table and get the right function.
*  That's how you pick the right thing there. And I thought that was trivial.
*  It's close to optimal. It's and it was obvious.
*  It turned out the Simula had a more complicated way of doing it and therefore slower.
*  And it turns out that most languages have something that's a little bit more complicated, sometimes more flexible, but you pay for it.
*  And one of the strengths of C++ was that you could actually do this object oriented stuff and your overhead compared to ordinary functions.
*  There's no interactions, sort of in 5, 10, 25 percent.
*  Just the call. It's down there. It's not two.
*  And that means you can afford to use it.
*  Furthermore, in C++ you have the distinction between a virtual function and a non-virtual function.
*  If you don't want any overhead, if you don't need the interaction that gives you the flexibility in object oriented programming, just don't ask for it.
*  So the idea is that you only use virtual functions if you actually need the flexibility.
*  So it's not zero overhead, but zero overhead compared to any other way of achieving the flexibility.
*  Now, or to parameterization.
*  Basically, the compiler looks at the template, say the vector, and it looks at the parameter and then combines the two and generates a piece of code that is exactly as if you've written a vector of that specific type.
*  So that's the minimal overhead.
*  If you have many template parameters, you can actually combine code that the compiler couldn't usually see at the same time and therefore get code that is faster than if you had handwritten the stuff.
*  Unless you are very, very clever.
*  So the thing is, parameterized code, the compiler fills stuff in during the compilation process, not during runtime.
*  That's right. And so furthermore, it gives all the information it's gotten, which is the template, the parameter and the context of use.
*  It combines the three and generates good code.
*  But it can generate.
*  Now, it's a little outside of what I'm even comfortable thinking about, but it can generate a lot of code.
*  Yes.
*  And how do you remember being both amazed at the power of that idea and how ugly the debugging looked?
*  Yes, debugging can be truly horrid.
*  Come back to this because I have a solution.
*  Anyway, the debugging was ugly.
*  The code generated by C++ has always been ugly because there's these inherent optimizations.
*  A modern C++ compiler has frontend, middleend and backend optimizations.
*  Even Cfront back in 83 had frontend and backend optimizations.
*  I actually took the code, generated an internal representation, munched that representation to generate good code.
*  So people say it's not a compiler, it generates C.
*  The reason it generated C was I wanted to use C code generators that are really good at backend optimizations.
*  But I needed frontend optimizations and therefore the C I generated was optimized C.
*  The way a really good handcrafted optimizer human could generate it, and it was not meant for humans.
*  It was the output of a program and it's much worse today.
*  And with templates, it gets much worse still.
*  So it's hard to combine simple debugging with the optimal code.
*  Because the idea is to drag in information from different parts of the code to generate good code, machine code.
*  And that's not readable.
*  So what people often do for debugging is they turn the optimizer off.
*  And so you get code that when something in your source code looks like a function call, it is a function call.
*  When the optimizer is turned on, it may disappear, the function call, it may inline.
*  And so one of the things you can do is you can actually get code that is smaller than the function call
*  because you eliminate the function preamble and return.
*  And there's just the operation there.
*  One of the key things when I did templates was I wanted to make sure that if you have, say, a sort algorithm
*  and you give it a sorting criteria, if that sorting criteria is simply comparing things with less than,
*  the code generated should be the less than, not an indirect function call to a comparison.
*  Comparing to a comparison object, which is what it is in the source code.
*  But we really want down to the single instruction.
*  But anyway, turn off the optimizer and you can debug.
*  The first level of debugging can be done, and I always do, without the optimization on because then I can see what's going on.
*  And there's this idea of concepts that puts some, now I've never even, I don't know if it was ever available in any form,
*  but it puts some constraints on the stuff you can parameterize, essentially.
*  Let me try and explain.
*  So, yes, it wasn't there 10 years ago.
*  We have had versions of it that actually work for the last four or five years.
*  It was a design by Gabby Dos Reis, Drew Sotton and me.
*  We were professors and postdocs in Texas at the time.
*  And the implementation by Andrew Sotton has been available for that time.
*  And it is part of C++20.
*  And there's a standard library that uses it.
*  So this is becoming really very real.
*  It's available in Clang and GCC, GCC for a couple of years.
*  And I believe Microsoft is soon going to do it.
*  We expect all of C++20 to be available in all the major compilers in 20.
*  But this kind of stuff is available now.
*  I'm just saying that because otherwise people might think I was talking about science fiction.
*  And so what I'm going to say is concrete. You can write it today.
*  And there's production uses of it.
*  So the basic idea is that when you have a generic component like a sort function,
*  the sort function will require at least two parameters.
*  One, a data structure with a given type and a comparison criteria.
*  And these things are related.
*  Obviously you can't compare things if you don't know what the type of things you compare.
*  And so you want to be able to say, I'm going to sort something.
*  And it is to be sortable. What does it mean to be sortable?
*  You look it up in the standard. It has to be a sequence with a beginning and an end.
*  There has to be random access to that sequence.
*  And then there has to be the element types has to be comparable.
*  Which means less than operator can operate on.
*  Yes.
*  Less than logical operator can operate.
*  Basically what concepts are, they're compile time predicates.
*  They're predicates you can ask, are you a sequence? Yes. I have beginning and end.
*  Is your element type something that has a less than? Yes. I have a less than.
*  So basically that's the system.
*  And so instead of saying I will take a parameter of any type,
*  it'll say I'll take something that's sortable.
*  And it's well defined.
*  And so you say, okay, you can sort with less than. I don't want less than.
*  I want greater than or something I invent.
*  So you have two parameters, the sortable thing and the comparison criteria.
*  And the comparison criteria will say, well, I can, you can write it saying it should operate on the element type.
*  And it has the comparison operations.
*  So that's simply the fundamental thing. It's compile time predicates.
*  Do you have the properties I need?
*  So it specifies the requirements of the code on the parameters that it gets.
*  It's very similar to types actually.
*  But operating in the space of concepts.
*  Concepts. The word concept was used by Alex Stefanov,
*  who is sort of the father of generic programming in the context of C++.
*  There's other places that use that word.
*  But the way we call it generic programming is Alex's.
*  And he called them concepts because he said they are the sort of the fundamental concepts of an area.
*  So they should be called concepts.
*  And we've had concepts all the time.
*  If you look at the KNR book about C, C has arithmetic types and it has integral types.
*  It says so in the book.
*  And then it lists what they are and they have certain properties.
*  The difference today is that we can actually write a concept that will ask a type, are you an integral type?
*  Do you have the properties necessary to be an integral type?
*  Do you have plus minus divide and such?
*  So maybe the story of concepts, because I thought it might be part of C++11.
*  C, O, X, whatever it was at the time.
*  What was the why didn't it?
*  We'll talk a little bit about this fascinating process of standards,
*  because I think it's really interesting for people.
*  It's interesting for me.
*  But why did it take so long?
*  What shapes did the idea of concepts take?
*  What were the challenges back in 87 or thereabouts?
*  1987.
*  1987 or thereabouts.
*  When I was designing templates, obviously I wanted to express the notion of what is required by a template of its arguments.
*  And so I looked at this and basically for templates, I wanted three properties.
*  I wanted to be very flexible.
*  It had to be able to express things I couldn't imagine,
*  because I know I can't imagine everything and I've been suffering from languages that try to constrain you to only do what the designer thought good.
*  Didn't want to do that.
*  Secondly, it had to run faster, as fast or faster than handwritten code.
*  So basically, if I have a vector of T and I take a vector of char,
*  it should run as fast as you build a vector of char yourself without parameterization.
*  And thirdly, I wanted to be able to express the constraints of the arguments.
*  I had proper type checking of the interfaces.
*  And neither I nor anybody else at the time knew how to get all three.
*  And I thought for C++, I must have the two first.
*  Otherwise, it's not C++.
*  And it bothered me for another couple of decades that I couldn't solve the third one.
*  I mean, I was the one that put function argument type checking into C.
*  I know the value of good interfaces.
*  I didn't invent that idea. It's very common.
*  But I did it.
*  And I wanted to do the same for templates, of course, and I could.
*  So it bothered me.
*  Then we tried again, 2002, 2003.
*  Gabby, Dostreis and I started analyzing the problem, explained possible solutions.
*  There was not a complete design.
*  A group in University of Indiana, an old friend of mine, they started a project at Indiana.
*  And we thought we could get a good system of concepts in another two or three years.
*  That would have made C++ 11 to C++ 06 or 07.
*  Well, it turned out that I think we got a lot of the fundamental ideas wrong.
*  They were too conventional.
*  They didn't quite fit C++, in my opinion.
*  Didn't serve implicit conversions very well.
*  It didn't serve mixed type arithmetic, mixed type computations very well.
*  A lot of stuff came out of the functional community.
*  And that community didn't deal with multiple types in the same way as C++ does.
*  Had more constraints on what you could express and didn't have the draconian performance requirements.
*  And basically, we tried. We tried very hard.
*  We had some successes, but it just in the end wasn't.
*  Didn't compile fast enough, was too hard to use and didn't run fast enough unless you had optimizers that was beyond the state of the art.
*  They still are. So we had to do something else.
*  Basically, it was the idea that a set of parameters has defined a set of operations.
*  And you go through an interaction table just like for virtual functions.
*  And then you try to optimize the interaction away to get performance.
*  And we just couldn't do all of that.
*  But get back to the standardization.
*  We are standardizing C++ under ISO rules, which are very open process.
*  People come in. There's no requirements for education or experience.
*  So you started to develop C++ and there's a whole.
*  What was the first standard established? What is that like?
*  The ISO standard? Is there a committee that you're referring to?
*  There's a group of people. What was that like?
*  How often do you meet? What's the discussion?
*  I'll try and explain that.
*  So sometime in early 1989, two people, one from IBM, one from HP turned up in my office and told me I would like to standardize C++.
*  This was a new idea to me. And I pointed out that it wasn't finished yet.
*  It wasn't ready for formal standardization and such.
*  And they said, no, Bjarn, you haven't gotten it. You really want to do this.
*  Our organizations depend on C++.
*  We cannot depend on something that's owned by another corporation that might be a competitor.
*  Of course, we could rely on you, but you might get run over by a bus.
*  Right. The old bus.
*  We really need to get this out in the open.
*  It has to be standardized under formal rules.
*  And we are going to standardize it under ISO rules.
*  And you really want to be part of it because basically otherwise we'll do it ourselves.
*  And we know you can do it better.
*  So through a combination of arm twisting and flattery, it got started.
*  So in late 89, there was a meeting in D.C. at the actually no, it was not ISO then.
*  It was ANSI, the American National Standard doing.
*  We met there.
*  We were lectured on the rules of how to do an ANSI standard.
*  There was about 25 of us there, which apparently was a new record for that kind of meeting.
*  And some of the old C guys that has been standardized in C was there.
*  So we got some expertise in.
*  So the way this works is that it's an open process.
*  Anybody can sign up if they pay the minimum fee, which is a very expensive fee.
*  The minimum fee, which is about a thousand dollars, though less than a little bit more now.
*  And I think it's $280.
*  It's not going to kill you.
*  And we have three meetings a year.
*  This is fairly standard.
*  We tried two meetings a year for a couple of years.
*  That didn't work too well.
*  So three one week meetings a year.
*  And you meet and you have technical discussions and then you bring proposals forward for votes.
*  The votes are done one person per one vote per organization.
*  So you can't have, say, IBM come in with 10 people and dominate things that's not allowed.
*  And these organizations that extends to the UC plus plus.
*  Yes, all individuals or individuals.
*  I mean, it's a bunch of people in the room deciding the design of a language based on which a lot of the world's systems run.
*  That's right. Well, I think most people would agree it's better than if I decided it or better than if a single organization like agency decides it.
*  I don't know if everyone agrees to that, by the way.
*  Bureaucracies have their critics, too.
*  Yes, they there.
*  Look, standardization is not pleasant.
*  It's it's it's it's horrifying.
*  It's like democracy.
*  But we exactly as Churchill says, democracy is the worst way except for the others.
*  Right. And it's I would say the same with formal standardization.
*  But anyway, so we meet and we we have these votes and that determines what the standard is.
*  Couple of years later, we extended this.
*  So it became worldwide.
*  We have standard organizations that are active in.
*  Currently, 15 to 20 countries and another.
*  15 to 20 are sort of looking and voting based on the rest of the work on it.
*  And we meet three times a year.
*  Next week, I'll be in Cologne, Germany, spending a week doing standardization.
*  And we will vote out the committee draft of C++ 20, which goes to the National Standards Committees for comments and requests for changes and improvements.
*  Then we do that. And there's a second set of votes where hopefully everybody votes in favor.
*  This has happened several times.
*  The first time we finished, we started in the first technical meeting was in 1990.
*  The last was in 98.
*  We voted it out. That was the standard that people used till 11 or a little bit past 11.
*  And it was an international standard.
*  All the countries voted in favor.
*  It took longer with 11. I'll mention why.
*  But all the nations voted in favor.
*  And we work on the basis of consensus.
*  That is, we do not want something that passes 60-40 because then we're getting dialettes and opponents and people complain too much.
*  They all complain too much. But basically, it has no real effect.
*  The standards have been obeyed.
*  They have been working to make it easier to use many compilers, many computers, and all of that kind of stuff.
*  And so the first, it was traditional with ISO standards to take 10 years.
*  We did the first one in eight. Brilliant.
*  And we thought we were going to do the next one in six because now we are good at it.
*  Right. It took 13.
*  Yeah, it was named OX. It was named OX.
*  Hoping that you would at least get it within the single, within the odds, the single digits.
*  I thought we would get, I thought we would get six, seven or eight.
*  The confidence of youth.
*  That's right. Well, the point is that this was sort of like a second system effect.
*  That is, we now knew how to do it.
*  So we were going to do it much better and we got more ambitious.
*  And it took longer.
*  Furthermore, there is this tendency because it's a 10 year cycle or eight, doesn't matter.
*  Just before you're about to ship, somebody has a bright idea.
*  And so we really, really must get that in.
*  We did that successfully with the STL.
*  We got the standard library that gives us all the STL stuff.
*  That basically, I think it saved C++. It was beautiful.
*  And then people tried it with other things and it didn't work so well.
*  They got things in, but it wasn't as dramatic and it took longer and longer and longer.
*  So after C++ 11, which was a huge improvement and what basically what most people are using today,
*  we decided never again.
*  And so how do you avoid those slips?
*  And the answer is that you ship more often so that if you, if you, if you have a slip on a 10 year cycle,
*  by the time you know it's a slip, there's 11 years till you get it.
*  Now with a three year cycle, there is about three, four years till you get it.
*  Like the delay between feature freeze and shipping.
*  So you always get one or two years more.
*  And so we shipped 14 on time.
*  We shipped 17 on time.
*  And we ship, we will ship 20 on time.
*  And that's, it'll happen.
*  And furthermore, this allow, this gives a predictability that allows the implementers,
*  the compiler implementers, the library implementers, to, they have a target and they deliver on it.
*  11 took two years before most compilers were good enough.
*  14, most compilers were actually getting pretty good in 14.
*  And 17, everybody shipped in 17.
*  We are going to have at least almost everybody ship almost everything in 20.
*  And I know this because they're shipping in 19.
*  Predictability is good.
*  Delivery on time is good.
*  And so, yeah.
*  That's great.
*  So that's how it works.
*  There's a lot of features that came in in C++ 11.
*  A lot of features at the birth of C++ that were amazing and ideas with concepts in 2020.
*  What to you is the most, just to you personally, beautiful or just do you sit back and think,
*  wow, that's just nice and clean feature of C++?
*  I have written two papers for the History of Programming Languages Conference,
*  which basically ask me such questions.
*  And I'm writing a third one, which I will deliver at the History of Programming Languages Conference in London next year.
*  So I've been thinking about that.
*  And there is one clear answer.
*  Constructors and destructors.
*  The way a constructor can establish the environment for the use of the type for an object
*  and the destructor that cleans up any messes at the end of it.
*  That is key to C++.
*  That's why we don't have to use garbage collection.
*  That's how we can get predictable performance.
*  That's how you can get the minimal overhead in many, many cases and have really clean types.
*  It's the idea of constructor-destructor pairs.
*  Sometimes it comes out under the name R-A-I-I.
*  Resource acquisition is initialization, which is the idea that you grab resources in the constructor and release them in destructor.
*  It's also the best example of why I shouldn't be in advertising.
*  I get the best idea and I call it resource acquisition is initialization.
*  Not the greatest naming I've ever heard.
*  So it's types, abstraction of types.
*  You said I want to create my own types.
*  Types is an essential part of C++.
*  Making them efficient is the key part.
*  To you, this is almost getting philosophical, but the construction and the destruction,
*  the creation of an instance of a type and the freeing of resources from that instance of a type is what defines the object.
*  It's almost like birth and death is what defines human life.
*  Yeah, that's right. By the way, philosophy is important.
*  You can't do good language design without philosophy because what you are determining is what people can express and how.
*  This is very important.
*  By the way, constructors destructors came into C++ in 1709.
*  In about the second week of my work with what was then called C++ classes, it is a fundamental idea.
*  Next comes the fact that you need to control copying because once you control, as you said, birth and death,
*  you have to control taking copies, which is another way of creating an object.
*  And finally, you have to be able to move things around.
*  So you get the move operations.
*  And that's the set of key operations you can define on a C++ type.
*  And so to you, those things are just a beautiful part of C++ that is at the core of it all.
*  Yes.
*  You mentioned that you hope there will be one unified set of guidelines in the future for how to construct the programming language.
*  So perhaps not one programming language, but a unification of how we build programming languages.
*  If you remember the statements, I have some trouble remembering it, but I know the origin of that idea.
*  So maybe you can talk about sort of C++ has been improving.
*  There's been a lot of programming language.
*  Do you? Where does the arc of history taking us?
*  Do you hope that there is a unification about the languages with which we communicate in the digital space?
*  Well, I think that languages should be designed not by clobbering language features together and doing slightly different versions of somebody else's ideas,
*  but through the creation of a set of principles, rules of thumbs, whatever you call them, I made them for C++.
*  And we're trying to teach people in the standards committee about these rules because a lot of people come in and says, I've got a great idea.
*  Let's put it in the language.
*  And then you have to ask, why does it fit in the language?
*  Why does it fit in this language?
*  It may fit in another language and not here, or it may fit here and not the other language.
*  So you have to work from a set of principles and you have to develop that set of principles.
*  And one example that I sometimes remember is I was sitting down with some of the designers of Common Lisp.
*  And we were talking about languages and language features.
*  And obviously we didn't agree about anything because, well, this was not C++ and vice versa.
*  It's too many parentheses.
*  But suddenly we started making progress.
*  I said, I had this problem and I developed it according to these ideas.
*  And they said, why?
*  We had that problem, different problem, and we develop it with the same kind of principles.
*  And so we worked through large chunks of C++ and large chunks of Common Lisp and figured out we actually had similar sets of principles of how to do it.
*  But the constraints on our designs were very different and the aims for the usage was very different.
*  But there was commonality in the way you reason about language features and the fundamental principles you were trying to do.
*  So do you think that's possible to...
*  So just like there is perhaps a unified theory of physics, of the fundamental forces of physics,
*  I'm sure there is commonalities among the languages, but there's also people involved that help develop these languages.
*  Do you have a hope or an optimism that there will be a unification?
*  If you think about physics and Einstein towards a simplified language, do you think that's possible?
*  Let's remember sort of modern physics, I think, started with Galileo in the 1300s.
*  So they've had 700 years to get going. Modern computing started in about 49.
*  We've got, what's that, 70 years. They have 10 times.
*  And furthermore, they are not as bothered with people using physics the way we are worried about programming is done by humans.
*  So each have problems and constraints the others have, but we are very immature compared to physics.
*  So I would look at sort of the philosophical level and look for fundamental principles, like you don't leak resources, you shouldn't.
*  You don't take errors at runtime that you don't need to. You don't violate some kind of type system.
*  There's many kinds of type systems, but when you have one, you don't break it, etc.
*  There will be quite a few and it will not be the same for all languages.
*  But I think if we step back at some kind of philosophical level, we would be able to agree on sets of principles that applied to sets of problem areas.
*  And within an area of use, like in C++'s case, what used to be called systems programming, the area between the hardware and the fluffier parts of the system, you might very well see a convergence.
*  So these days you see Rust having adopted RAII and sometimes accuses me for having borrowed it 20 years before they discovered it.
*  But we're seeing some kind of convergence here instead of relying on garbage collection all the time.
*  The garbage collection languages are doing things like the dispose patterns and such that imitate some of the construction destruction stuff.
*  And they're trying not to use the garbage collection all the time and things like that.
*  So there's that there's conversion. But I think we have to step back to the philosophical level, agree on principles, and then we'll see some conversions, convergences.
*  And it will be application domain specific.
*  So a crazy question, but I work a lot with machine learning, with deep learning.
*  I'm not sure if you touch that world much, but you could think of programming as a thing that takes some input.
*  Programming is the task of creating a program and a program takes some input and produces some output.
*  So machine learning systems train on data in order to be able to take an input and produce output.
*  But they're messy, fuzzy things, much like we as children grow up.
*  You know, we take some input, make some output, but we're noisy.
*  We mess up a lot. We're definitely not reliable. Biological system are a giant mess.
*  So there's a sense in which machine learning is a kind of way of programming, but just fuzzy.
*  It's very, very, very different than C++ because C++ is like it's just like you said, it's extremely reliable.
*  It's efficient. It's you know, you can you can measure it.
*  You can test in a bunch of different ways with biological systems or machine learning systems.
*  You can't say much except sort of empirically saying that 99.8 percent of the time it seems to work.
*  What do you think about this fuzzy kind of programming?
*  Do you even see it as programming? Is it solely and totally another kind of world?
*  I think it's a different kind of world and it is fuzzy.
*  And in my domain, I don't like fuzziness.
*  That is, people say things like they want everybody to be able to program.
*  But I don't want everybody to program my airplane controls or the car controls.
*  I want that to be done by engineers.
*  I want that to be done with people that are specifically educated and trained for doing building things.
*  And it is not for everybody.
*  Similarly, a language like C++ is not for everybody.
*  It is generated to be a sharp and effective tool for professionals basically.
*  And definitely for people who aim at some kind of precision.
*  You don't have people doing calculations without understanding math.
*  Right? Counting on your fingers is not going to cut it if you want to fly to the moon.
*  And so there are areas where an 84 percent accuracy rate, 16 percent false positive rate is perfectly acceptable
*  and where people will probably get no more than 70.
*  You said 98 percent. What I have seen is more like 84.
*  And by really a lot of blood, sweat and tears, you can get up to 92.5.
*  So this is fine if it is, say, pre-screening stuff before the human look at it.
*  It is not good enough for life-threatening situations.
*  And so there are lots of areas where the falseness is perfectly acceptable and good and better than humans, cheaper than humans.
*  But it is not the kind of engineering stuff I am mostly interested in.
*  I worry a bit about machine learning in the context of cars.
*  You know much more about this than I do.
*  I worry too.
*  But I am sort of an amateur here.
*  I have read some of the papers, but I have not ever done it.
*  And the idea that scares me the most is the one I have heard, and I don't know how common it is,
*  that you have this AI system, machine learning, all of these trained neural nets.
*  And when there is something that is too complicated, they ask the human for help.
*  But the human is reading a book or asleep, and he has 30 seconds or 3 seconds to figure out what the problem was
*  that the AI system could not handle and do the right thing.
*  This is scary.
*  I mean, how do you do the cuddle between the machine and the human?
*  It is very, very difficult.
*  And for the designer of one of the most reliable, efficient, and powerful programming languages, C++,
*  I can understand why that world is actually unappealing.
*  It is for most engineers.
*  To me, it is extremely appealing because we do not know how to get that interaction right.
*  But I think it is possible.
*  But it is very, very hard to do.
*  I think it is possible.
*  But it is very, very hard.
*  It is.
*  And I was stating a problem, not a solution.
*  Yes, that is impossible.
*  I would much rather never rely on the human.
*  If you are driving a nuclear reactor or an autonomous vehicle,
*  it is much better to design systems written in C++ that never ask the human for help.
*  Let's just get one fact in.
*  All of this AI stuff is on top of C++.
*  So that is one reason I have to keep a weather eye out on what is going on in that field.
*  But I will never become an expert in that area.
*  But it is a good example of how you separate different areas of applications,
*  and you have to have different tools, different principles, and they interact.
*  No major system today is written in one language.
*  And there are good reasons for that.
*  When you look back at your life work, what is a moment,
*  what is an event creation that you are really proud of?
*  You say, damn, I did pretty good there.
*  Is it as obvious as the creation of C++?
*  It is obvious.
*  I have spent a lot of time with C++.
*  And there is a combination of a few good ideas,
*  a lot of hard work, and a bit of luck.
*  And I have tried to get away from it a few times,
*  but I get dragged in again, partly because I am most effective in this area,
*  and partly because what I do has much more impact if I do it in the context of C++.
*  I have four and a half million people that pick it up tomorrow if I get something right.
*  If I did it in another field, I would have to start learning,
*  then I have to build it, and then we will see if anybody wants to use it.
*  One of the things that has kept me going for all of these years is,
*  one, the good things that people do with it,
*  and the interesting things they do with it.
*  And also, I get to see a lot of interesting stuff and talk to a lot of interesting people.
*  I mean, if it had just been statements on paper or on a screen,
*  I don't think I could have kept going.
*  But I get to see the telescopes up on Mauna Kea,
*  and I actually went to see how Ford built cars,
*  and I got to JPL and see how they do the Mars rovers.
*  There is so much cool stuff going on,
*  and most of the cool stuff is done by pretty nice people,
*  and sometimes in very nice places, Cambridge, Sofia, Antipolis, Silicon Valley.
*  Yeah, there's more to it than just code, but code is central.
*  On top of the code are the people in very nice places.
*  Well, I think I speak for millions of people, Bjorn,
*  in saying thank you for creating this language
*  that so many systems are built on top of that make a better world.
*  So, thank you, and thank you for talking today.
*  Thanks, and we'll make it even better.
*  Good.
*  Thank you.