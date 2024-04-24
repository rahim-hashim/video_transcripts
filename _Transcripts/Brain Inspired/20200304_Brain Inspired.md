---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 7037s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 236
Video Rating: None
---

# BI 062 Stefan Leijnen: Creativity and Constraint
**Brain Inspired:** [March 04, 2020](https://www.youtube.com/watch?v=z-eGFt1MsaM)
*  For thousands of years people looked at knowledge as it's something that's already there.
*  I'm just the one to discover it, like America.
*  And at some point, and it's hard to pinpoint when, but at least this is how we tend to think about it right now,
*  we talk about generation, about creation, about there being something that didn't used to be there.
*  In a more constrained environment, your creativity flourishes.
*  It might even be more easy to be creative if you're extremely constrained.
*  This is Brain Inspired.
*  Hey everyone, this is Paul Middlebrooks.
*  When I was young, I would look up at the clouds and see whatever I wanted.
*  Animals, trains, whatever.
*  As I get older, that happens less and less, and it's frustrating because I value creativity
*  and I worry that as I'm able to see less and less in the clouds, it's a sign that my creativity is evaporating.
*  Creativity is one of those traits that we associate with high intelligence,
*  and it's on the list of attributes that we would want to see in AI to consider a machine truly intelligent, whatever that means.
*  Creativity is also on the list, the very long list, of things that we don't understand all that well.
*  My guest today, Stefan Lenin, started an institute, the Asimov Institute, with the goal of developing artificial creativity,
*  and today we have a long and sometimes winding conversation that covers a lot of topics and ground,
*  but revolves all around creativity and its necessary and inseparable partner, constraint.
*  Stefan's a professor of intelligent data systems at Utrecht University of Applied Sciences in the Netherlands,
*  and he's also part of a lot of different groups.
*  At the Asimov Institute, they do a few things.
*  They take on creative projects and use AI to do so, and most of those projects focus on an AI and human collaboration hybrid.
*  They also, as a service to the general public, strive to explain AI.
*  With that in mind, if you need a speaker for a conference, someone to talk about creativity in AI, for example, you should reach out to Stefan.
*  He regards educating the public as an important service, so he's eager to do that when possible.
*  And there really aren't many people who take public education seriously.
*  Also, I found out Stefan runs the Asimov Institute using his own funds.
*  He's that dedicated and driven.
*  You'll hear us talking about these posters that they sell with well-designed diagrams of the modern zoo of neural networks.
*  It's kind of a reference poster that also happens to be pretty to look at.
*  So funds from the sale of those posters go toward the various costs of upkeep for the Asimov Institute, like web hosting and all that jazz.
*  So I recommend you buy one if you want to support him and have a good-looking poster on your wall.
*  Speaking of support, thanks to Adam, Alexandra, Daniel, Jacob, Robert, Mai, and Jurgis for recently supporting the show on Patreon.
*  Good things are coming your way in the near future, guys.
*  As always, I link to the stuff that we discuss in the show notes at braininspired.co.
*  slash podcast slash sixty two guys look up at those clouds.
*  You see anything? I hope so.
*  I hope your lives and minds are filled with creativity.
*  Thank you for listening. Here's Stefan Leinon.
*  I shall be telling this with a sigh somewhere ages and ages hence two roads diverged in a wood and I I took the one less traveled by.
*  And that has made all the difference.
*  That's from the road not taken, of course, from Robert Frost back in 1916.
*  It is also how you start your dissertation, Stefan.
*  Welcome to the show. Thanks for being here.
*  Thank you, Paul. It is. Yeah.
*  So I have occasionally been called creative very occasionally throughout my life.
*  And when it does happen, I find it to be the highest compliment that I could receive.
*  I know that I'm not alone in this.
*  And, you know, that that may also be creativity was valued in my household growing up.
*  And I wonder just off the bat, do you feel the same way?
*  Do you see it as a as one of the pinnacles of cognition?
*  I would agree with it.
*  I mean, creativity is, of course, an ambiguous term.
*  You once you try to define it, you tend to get into a lot of semantics, which has its good sides and bad sides.
*  But I was reminded of this a couple of weeks ago.
*  It was a quote by Martin Saucisi.
*  And he said, I'll paraphrase here, but more creativity means more personal.
*  So if something is very creative, it tends to be very personal.
*  And so I think if someone compliments you on your creativity, it means you have a, let's say, well-developed personality or you appear to be an individual.
*  And I think this is also why we're so fascinated with respect to this question when we talk about AI and machines, because how do we breathe these machines into life?
*  Well, we know for one that if they're creative, they probably have a personality.
*  So there's I think there's a link between a person and then being creative.
*  I wonder if that has to do with uniqueness, too, and just the personal aspect of it with the uniqueness of the cognitive situation you can get yourself into that is unique to me.
*  And therefore, it's personal or something. I wonder if that has something to do with it.
*  Well, if we think about this robot frost, you know, this mental image of two parts diverge and one less traveled by.
*  If you take the one less traveled by, we typically associate this with creativity, right?
*  There's a path that not that the few others have taken.
*  We also think this might be the hardest part to take.
*  There might be some foliage on the way and we need a knife to go through it.
*  And what I like about the poem is that robot frost, I don't think he ever said this explicitly, but we tend to think about this choice as a positive one.
*  So if we take the road less taken, we get we get this uniqueness.
*  We develop over time.
*  But I think the poem itself is ambiguous.
*  You could also because he's saying I'm telling this with a sigh.
*  So you might also interpret it as a bad choice to to go this way.
*  Yeah, it's a it's a double-edged sword.
*  I would say there's so much to chew on that, you know, nothing worth doing isn't difficult.
*  Nothing worth doing is easy, I suppose, is another to paraphrase.
*  I don't know where that comes from.
*  I'm paraphrasing.
*  But I also I value creativity in others.
*  You know, I would rather all things being equal.
*  I would rather befriend a creative average intelligence person than a super intelligent non creative person.
*  And we'll talk about the relationship between intelligence and creativity here coming up as well.
*  So I don't know.
*  Maybe other people are like that as well.
*  That, you know, creativity is really valued.
*  But for me personally, it's just I value it a lot.
*  So you must value creativity because you started the Asimov Institute.
*  Yes.
*  And this is I don't have the the slogan, you know, the motto, but it's a artificial creativity and constraint.
*  Right.
*  Right. Did you I swear, did you just add the constraint part to that slogan recently?
*  No, it's it's been there.
*  It was I mean, the idea to start this institute came out of my my research and my dissertation had this title.
*  So creativity and constraint in artificial systems.
*  And I think those two like creativity and constraint, putting them together or juxtaposing them, I think it reveals some of the tension that's in creativity.
*  Because there's like I said, it's an ambiguous term.
*  There are especially from a computational point of view, there are very simple, unnew and space of looking at creativity as like a a random process or a guided random process or just something that happens unforeseen things that you don't want to occur.
*  But I think this adding this word constraint already sort of implicitly applies it.
*  There's a paradox to it that in a and I think this is more of an artistic point of view.
*  But in a more constrained environment, your creativity flourishes.
*  It might even be more easy to be creative.
*  If you're extremely constrained, look at the way we write poems, for example, if we if we put on the constraint of adding rhyme to a poem, we almost automatically make the poem itself more creative or put it in the other way.
*  If we don't add rhyme, it becomes very difficult to write a creative poem that we recognize as creative.
*  You can almost even see this in putting a deadline to a goal, right?
*  You know, if you have to get something finished, all of a sudden you become very creative and you finish it.
*  Whereas if it's open ended, you don't you never have to actually put a period on it and you never get as creative as you could be, perhaps.
*  It's a way to focus your your work.
*  I mean, if you paraphrase Douglas Adams, you could say something like I love I love creativity.
*  I love creative act, especially the sound of constraints as they pass by.
*  It's like breaking through those. Right. That's the act of creation.
*  So you need those constraints at some level.
*  Well, that's the act of a particular kind of creativity that we'll get to.
*  But but I want to talk about sort of your background.
*  So, you know, like you just mentioned your dissertation, which was about artificial creativity and constraint.
*  You came to that through your interest in natural creativity and constraint, I would imagine.
*  Take us just briefly. I don't usually do this.
*  Like, you know, tell us about who you are and your background, you know, at the beginning, because every podcast starts with tell us a little bit about yourself.
*  But, you know, you you had you kind of have a an interesting journey, at least from my perspective, because you didn't just stay in academia.
*  You sort of went in and out. You worked.
*  You did some industry stuff.
*  And and now you've you know, you've ended up starting this awesome of Institute.
*  But you're also part of like what maybe 13 or 14 other institutes.
*  I don't know. You're all over the place.
*  So so how did you come to this spot here?
*  So it's I mean, I started out in artificial intelligence.
*  That's that's my background. I mean, if we go a little bit further back, we started out in psychology.
*  And then I learned about this like this is early 2000s.
*  Right. So I wasn't that famous back then.
*  I learned about this thing where you could combine, you know, Lego blocks with with with psychology.
*  So rather than you're studying the brain, you could actually build it and see what it's like.
*  And to me, that felt like something new that we'd never in the past been able to do something like experimental philosophy.
*  So all these these theories that we had about about the mind and about about how brain works and about what knowledge is, we could suddenly build something.
*  We could put people to the test.
*  They put your money where your mouth is. If you think this is your theory, if this works, build it, show it.
*  And I really like this sort of pragmatic stance that was allowed by.
*  So I went into that field, but I got a little bit disappointed here and there during my studies as it sometimes felt like cheap tricks.
*  So a lot of it, I think, and still is in N.A.I. is is making the audience believe that there's something in telling that there's something that there's someone there, someone in this computer.
*  And on the one hand, I wanted to expose this.
*  And I think this is why creativity is such an interesting term, because it's a it's a gateway to a whole set of other human traits like sentience or like normativity and ethics that we we nowadays talk a lot about or or understanding like true understanding of what something means.
*  I think creativity is interesting path towards those terms.
*  So that's that's what triggered me to start moving into the field of creativity.
*  But my journey has been a little bit unusual in part because there wasn't such a field as artificial creativity, or at least I wasn't able to find it.
*  So when I was doing A.I., I think I was doing my graduation projects on the symbol grounding problem, which is essentially about understanding how do you generate meaning in an artificial system?
*  I wanted to continue my P.S.D. and creativity, but I didn't know where to find it.
*  So I got offered a P.S.D. position in Canada, at UBC, at the psychology department.
*  So I moved there. I traveled around a little bit.
*  I went to Boston, Tufts University.
*  And after a couple of years, I was I was happily sort of swimming around in this creativity field.
*  But what I also noticed is that psychologists weren't as prone to to ground their ideas in actual computer science as the A.I. folks are.
*  So I started to miss that. So we could theorize, write interesting papers, but I couldn't put the theories to the test because this translation back into a machine, I was missing that.
*  So during my P.S.D. I switched.
*  I moved back to the Netherlands and I finished it at a machine learning department in Nijmegen, where I was sort of doing it the old fashioned way, building it up from A.I. techniques towards creativity.
*  But by then, my my my topic had already been determined.
*  I was so into this field that I really wanted to continue it.
*  And so that is why I started the Asimov Institute.
*  Basically, it's a refuge to do research on creativity and constraint on the one hand and all these interesting new A.I. techniques really grounded in technology and to figure out, you know, what does this all mean?
*  What what what can we do with these techniques?
*  And also, what do we learn about ourselves?
*  I think that's the second part.
*  What kind of projects do you guys do at the Asimov?
*  Well, we we are happily unbounded by any economic incentives.
*  We have no constraints.
*  We have no constraints in our in our operation in the sense that we are project based.
*  So we work in, let's say, small teams.
*  Typically, that would be an artist and an engineer and maybe a scientist there in a team.
*  And we operate on the basis of our own curiosity and wanting to do a project.
*  I know you guys have done fashion.
*  You've done music.
*  Those are the two main ones that I know.
*  There's a there's a couple.
*  Yeah, well, we did.
*  Those were, let's say we published about those.
*  And I think those were picked up also.
*  So I noticed that I think is really interesting to notice if you do something out of curiosity,
*  people recognize it and people I don't know, they feel your own enthusiasm and that gets transferred really easily.
*  But we did some other projects on like, for instance, audio generation.
*  So can we generate sound effects, 3D model generation for architecture, font generation?
*  So that's that's one part.
*  Another part of the things we do has to do with explaining AI to the general public.
*  So we published a blog post called the Neural Network Zoo, which is a sort of a cheat sheet of different kinds of neural networks.
*  So this is actually how I found you.
*  You were asking me before we started.
*  How did you find me?
*  And it's through the through the neural network zoo.
*  And I must be just be high in Google searches for these things.
*  I'm putting together this course about neural networks and how they relate to brains.
*  That's part of the course.
*  And that's I think it's I don't know, probably the first or second one to pop up.
*  And since then, you've actually talked about it in talks.
*  I don't know if that's why you get invited.
*  But that was my introduction to you.
*  So there you go.
*  Yeah. OK. Good to know.
*  Well, I mean, the post started with a student of mine, Fyodor, who wrote the post, asking me about different types of neural networks just as part of his graduation project.
*  And so we had a couple of discussions and he made notes.
*  And he's a very creative fellow.
*  So he made this nice sort of design language on these neural networks with different colors and sets.
*  Those are the kind of people you need working for you at the SMOF, right?
*  Oh, yeah. Good design. Yeah.
*  Yeah. And the so it wasn't even I mean, it was just a sort of something to play around with ourselves.
*  But as we noticed, we thought maybe this is interesting for other people as well.
*  So we worked on it a bit.
*  We added some text and we put it online.
*  And a week later we saw we had sixty thousand views.
*  So it's a surprise.
*  Yeah. And it's been going on like that.
*  So we get a lot of views on this post and some invited talks.
*  You sell posters now. You can buy a poster of it, right?
*  Yeah, they sell pretty well.
*  Yeah, they do.
*  Yeah, I have one myself.
*  No, I mean, it's so that's even even if we try not to be creative just by making this cheat sheet.
*  Apparently, there's still a creative element because people recognize there's a creativity in this case in design of the poster.
*  So it's actually featured in museum expositions as well.
*  So the Arts Electronica in the Lint last year, they they had these neural network designs from the neural network zoo in their exposition.
*  So I'm waiting for the Christmas sweater version.
*  When is that coming out?
*  Oh, good suggestion.
*  OK, well, it sounds like one of the things that you guys are concerned with at the Asimov anyway is not just autonomous creativity within A.I., but the interaction with human and and what kind of creative output can come from that.
*  Am I accurate in that assessment?
*  Yeah, I mean, we can.
*  The idea of having an autonomous A.I. that is created, of course, it's it's very it's fascinating.
*  It's sci-fi, I think, but it's it's fascinating.
*  But let's say putting this as your goal and then seeing how far you get that that that creates some very interesting open challenges.
*  And one of the things that we found, maybe we can go into one of those projects you mentioned, let's say the fashion project.
*  Sure. One of the things we found is that if you want to use A.I. to generate something artistic, so beyond, let's say, just something new like a shopping list or a recommendation algorithm type of output, but something that we recognize as truly creative, just an algorithm won't do.
*  I am yet to see any output of A.I. that is, let's say un-medaled by any humans that just sort of takes a data set and generates something creative from it.
*  In your judgment, because creativity is a human.
*  Oh, yeah, that's a whole other.
*  Yeah, yeah.
*  Yeah. But not just in my judgment.
*  So in this project, what we did is we worked together with a virtual fashion designer named Amber J. Slaughter.
*  And we wanted to provide a tool that could predict next year's fashion.
*  That was the outset of our project, because then it shows two things, either two things.
*  Either we are able to generate something as creative as a fashion designer, or we show that the fashion industry is as creative as a computer.
*  Both outcomes are interesting by itself and something to publish about.
*  Yeah.
*  So it was also almost like a pamphlet that we wanted to write about the fashion industry.
*  But as we moved along with these predictions, of course, we used, again, a generative adversarial network to produce those outputs.
*  We noticed that the interplay between the tool, the predictive A.I. tool, and Amber's work, it's in this interplay, this hybrid setup, where the tool allows her creativity to diverge and enter new areas of her search space.
*  And then Amber would be able, or better able, to select which samples were more interesting than others.
*  So we have this sort of divergence and selections mechanism going.
*  But it's a composition by both.
*  It's not something that's generated just by Amber or just by the A.I.
*  And this hybrid A.I. is what we found most fascinating about the project.
*  So that's what we developed further.
*  And then the end result was not a statement about the fashion industry so much as it was a new collection for her.
*  And so she's been touring with this collection.
*  And that's also what we published about.
*  And what was her judgment of the types of products, types of directions that the GAN was coming up with?
*  Does she have like 40 balled up pieces of paper on the floor from the printouts or whatever?
*  And this is crap. This is crap.
*  Oh, oh, this is nice.
*  You know, or you know, what was her overall assessment?
*  I mean, it's more or less that's what you get because what you.
*  Not me, man. I make everything perfect the first time.
*  Well, what you get with an A.I.
*  So what we're basically asking the system, you know, it's again, it's advanced statistics, right?
*  We give it a data cloud data points in a multidimensional space.
*  You know, this is the data set.
*  So these are the existing designs that we feed into the system.
*  And then we say, give us new samples.
*  Now, what is new in this case?
*  So how do we define new if we say, give us new samples?
*  Well, that's something that we could actually vary.
*  So we could say, give us samples that look a lot like the existing data points.
*  Or we could say, you know, go wild, diverge a lot.
*  We can do that.
*  But how do we determine the dimension in which it should go or rather how do we make it non-random?
*  I think there's really the problem with artificial creativity, at least in the systems that we have now,
*  is that we can decide for it to create something new and original, but it's random.
*  So how do we add value to it?
*  Because that's the second component of creativity next to this originality component.
*  Well, this is this is Amber's work.
*  This is what Amber's good at.
*  So we have the algorithm generate new stuff, which is sometimes hard to come by if you're an artist or if you're any human being.
*  How do you how do you think of something new?
*  It's really difficult, but I can help you with that.
*  But then if you see the examples, we're pretty good at picking out which ones feel good, like which ones work, especially if you don't have to argue why.
*  You say, hey, I like this.
*  It worked.
*  I'll pick this.
*  I'll feed it into the algorithm again.
*  Now, maybe with a little less divergence, see what comes out of it.
*  And then you get this sort of this hybrid interplay going.
*  And at some point you get something that inspires you, whatever the word inspires me.
*  And based on that, you can have your collection.
*  Wow. It's good stuff.
*  Well, OK, you saw essentially the rise of deep learning.
*  You had a sort of front row seat to it because you had, like you said, been working with these AI systems since early on.
*  And in fact, in your dissertation, you used you created little network agents to study creativity in a society that evolved.
*  But these agents that you use were actually had one hidden layer.
*  They were pretty simple, right?
*  I don't know. I think they had like seven or eight something like that, input units and one out a few output units and then like one hidden layer.
*  And, you know, it's known actually all you need is one hidden layer.
*  But if you know, it can go to infinity and then you can do anything with it.
*  But yours were pretty small and simple.
*  What's your overall? So I did not sort of experience the deep learning explosion because I was recording single neurons, you know, and recording collections of neurons in behaving animals.
*  And so the AI, the neural network world, which has always been there, was kind of off out of my purview.
*  But you have been sort of observing this ever since.
*  What's your take on it? Was it an explosion? Has it been a revolution? Was it amazing?
*  What was it like? What's it been like?
*  Well, it's getting more and more amazing.
*  So it feels like it's this sort of wave that happened in AI.
*  I think it's for me, for my personal, it's been going on for about 10 years now.
*  And if I see around me what I what I see happening, if I see what I like the general public knowledge about AI and about any interest in stuff like deep learning, like 10 years ago, to give you an idea, I wasn't allowed to write papers by my supervisor on neural networks.
*  And because it was just not, you know, nobody did that.
*  It wasn't wouldn't garner interest. Is that why?
*  Yeah, I mean, if you would even even I think I've heard this if you would submit a paper to the MIPS, it's not called Neuros, but so the Neural Information Processing Systems Conference, you shouldn't put the word connectionist or neural network in the title of your paper, because that was out of fashion.
*  That's something that we did in the 80s. And yeah, you did it in the 80s and 90s. You didn't work on that kind of stuff.
*  I mean, and that's 10 years ago.
*  And so it's been a complete shift. Now, interestingly, and I mean, this has been said by others, of course, as well. It hasn't been such a shift in terms of the algorithms themselves. Of course, we've seen new types of architectures pop up, and we have different types of algorithms that run over these, these neural architectures.
*  I mean, the Neural Zoo is one example of this sort of Cambrian explosion of different types of neural network algorithms. But as revolutionary as those systems are, the groundwork for this has been laid in the back in the 80s and the 90s, you know, the work by by Jeffrey Hinton. I mean, he was like one of the godfathers and you can smear to work it's Yeah, I think he's he's often sort of underrepresented in that but he also did a lot of work on this, like developing the LSTM, which is a completely different. So I mean, the really revolutionary work.
*  In terms of, I think AI science has been done way before this revolution started. I think it's more that what happened is the sort of a happy accident with exponential scaling of data, graphic processing units being just very well fitted for neural network matrix computation, the abundance of data and the sort of exponential decrease in cost for storing data.
*  And the internet, which is sort of allowed for all kinds of new business models based on that to sort of flourish. Yeah, so it's it's we were sort of on this crossroads. And I think that's what what what happened and this discussion right now that I find interesting is, are we heading towards a new AI winter or not?
*  That's the we've had about four, I think right now this might be the fifth.
*  By winter, do you do you just mean a funding winter because that's what I have come to understand the winter as being that it's just a matter of funding because people are always people who want to work on AI are always working on on AI in the background, but maybe other people who don't care so much they become bankers during the AI winter or whatever.
*  Yeah, absolutely. Yeah. So the so there's definitely an amount of overhype right now in AI. I mean, we can be clear about this. But but the question is, well, what will happen next? What will stay like that? Will it keep on growing? Or will it sort of move back a bit? I think there's something fundamentally different compared to previous AI winters, which is that a lot of the funding right now isn't coming from the public. It's it's private. It's, you know, commercial enterprises who have an interest in this. I also think that the
*  AI has never been as widespread as it is right now. So I think that's also unique. And I, well, you know, as a Harari as sapiens, like, like, I think in one of the passages on this book, something that really struck me is he points out statistics as a, as a really revolutionary mechanism for humans to better understand the world. And I think what we're seeing right now in deep learning and AI is actually much more part of a,
*  general move towards statistics based on data, putting the human out the loop, generating models that are so complex that we are unable to comprehend them, but they're still functioning. I think that that's more a more accurate description of what is happening than to call it AI and to use terms like intelligence, creativity, and
*  sapiens in this. So in some respects, there's still an AI winter going on, because it's really difficult still to get funding for creativity and sapiens and those kinds of topics. Right. But since we brought up the definition of AI to include anything that has to do with data, we don't we're not noticing it because there's a lot of funding on that.
*  That's kind of taking a step back from, you know, usually the goalposts are just moved right where when you make an AI system, and then all of a sudden it can do something, then you no longer call it AI. I don't remember what the phrase for this is. But so the definition of Google, Google, Google search used to be AI at some point. Yeah, that's right. We don't call AI right now. But yeah, yeah, because it's done. Yeah.
*  Gosh, you know, I have like so many questions for you. And we, you know, we've already 30 minutes in. So
*  Okay.
*  Speaking of the zoo of neural networks, and I'll link to it, of course, in the show notes. So you guys can buy your your zoo of networks posters, these beautiful little schemas of neural networks, these little icons. So you mentioned GANs. Is that like the vast majority of work of your work using GANs? Or are there go to I mean, are you using the whole zoo of neural networks? Or are there some that you are mostly focused on?
*  Well, we in our work, we're interested in generating outputs. Yep. So these these like these tiny neural networks, like you mentioned before, in this multi agent simulation, what this but I only have one layer, which are basically, you know, they're just functions from input to output. They're less interesting for this work, because they're just neural network representations of functions that you could also otherwise describe. So the types of networks that have a sort of an internal dynamic
*  that are recurrent, that rather than going from input to output, also go from output to input, so to speak. So they, they, they, they're much more like actual vision, in that they are an active process. So networks that you could actually sort of sample and ask, I've just showed you 100 different car designs, now generate me a new car, you know, those kind of networks, those are of course, interesting, they're sort of low hanging fruit for creativity research, because you can
*  you can actually show what the network thinks or what it sees. And so there's a couple of them. One of the first networks that had these properties was the deep belief network. Oh, yeah. Because not so much because of its architecture itself, but because of some techniques that allowed you to sample. So a deep
*  belief network, in essence, it's almost like a stack of recurrent networks, going from input data to more abstract representations of this data. And Jeff Hinton has one on the very good YouTube video online, in which he explained this, which you can sort of sample, you can turn them around. So if you start from the most abstract concept, and you sort of trigger those neurons at that level, you can actually show what happens at the input level. So you could almost like,
*  make a projection to its retina. I mean, it's a false metaphor. But this is the idea that you get from it. So you could ask it like, what does the number four look like to you or no, these kind of questions. So I think that was one of the earliest examples of
*  of this sort of generative network. And then you have the the convolutional networks, and particularly the deep convolutional inverse graphics network in which you have two convolutional layers, which you could also use for this. But I think if we make a top three, then the generative adversarial network will be at number one right now because it's such a I mean, it's a it's a it's a great idea. You basically apply the minimax algorithm.
*  To a to training and neural network. So you have them sort of competing against each other sort of minimizing the maximum and maximizing the minimum. And then you Yeah, you it's such a it's such a general approach towards, you know, generating content that you could apply to anything, I think I don't think it's limited. That's what I like about it.
*  generative adversarial networks also, you know, that's gonna go down in history as the story of how they are created in good fellow was out with his friends, you know, having beers one night and kind of came up with the idea and said, I think I can do it. And then he went home and coded it up in that evening. So
*  that's that's great, right? I mean, that's that such a revolutionary technique can be just, you know, someone can think about it, do it. You know, I mean, yeah, I find that very inspiring.
*  Of course, you know, the confluence and part of the creativity, which we're about to talk about is just and constraint is just having the right environment and the right, you know, had we not computers, had we not been in this day and age, you know, with all the data with the computer power, that wouldn't have been possible, you could have had the idea and then gone home and got out your pen and paper and scratched a long night.
*  It's absolutely I mean, timing is a part of it. I mean, Bill Gates didn't have access like early on access to a, you know, a computer system, he wouldn't have found it in Microsoft, or it would have been too late, probably. So I mean, yeah, there's a there's a day and age for these kinds of ideas, I think.
*  Yeah, it really is. Yeah.
*  Okay, creativity. This is why we're really talking today. This is, you know, the holy grail, you know, a lot of people, there's always like the next thing like, well, AI can't do this as soon as AI can do this, we'll consider it real AI and creativity is often the answer to that fill in the blank statement.
*  Okay, I mean, and like you said, there's just so many different definitions. One of my favorite things is you often hear artists and specifically musicians talking about in their process, their creative process, but they don't feel like they're creating anything when they're in the flow state, they feel like they're a vessel and the thing is written.
*  Actually, you do you do hear our writers talk about this too. It's it's already written, the music is already there. It just has to come through them and they have to they have to allow it to come through them, right? So they don't feel like they even have anything to do with it, which people like Tom Petty and Paul Simon have said these sorts of things.
*  In the writing world, it's Steven Pressfield writes about this kind of thing, the muse. So I don't know, you know, there's just this long history of, of people's own introspection of their creative process, which, you know, is completely inaccurate, like you we have terrible accounts of our own introspective process of anything, really.
*  But so okay, there have been a lot of different definitions of creativity, and we'll throw some out there just to kind of get started here. One is creativity is the generation of novel and useful products with a specific context. Margaret Bowden has written a lot about creativity and her definition is the ability to come up with products, ideas or artifacts that are new, surprising and of value. And you already alluded to these three different qualities.
*  Of creativity. So there's a bunch of different definitions of creativity. They're all circling around the same sort of idea. And Margaret Bowden also famously, I don't know if it's famous, but it's well known, talks about three different types of creativity, combinatorial, exploratory and transformational. And I know that, you know, you're well versed in these things, but just to lay them out. So combinatorial creativity is this is the main type that people refer to when they when they refer to creativity. This is when you combine
*  familiar things in unfamiliar ways. And actually, my friend just pointed me to a recent series on it's called creativity is a remix, something like that, where this filmmaker goes through like, you know, a bunch of like Led Zeppelin songs and talks about how they're they're just reusing other people's stuff in in combining it in different ways. I mean, literally copying it and then putting in the different pieces together, things like that. And you know, his take is that all there's nothing new. Every
*  thing is a remix. Everything is combinatorial creativity. exploratory creativity is when you're working within a set of specified rules. But you create new styles, new generate new things within those rules, like an example would be creating a brand new sentence within the rules of grammar and language, right? So that's a type of creativity. And then finally, the most difficult, I suppose, is transformational. That's when you rewrite the rule book, and
*  you're like, okay, so you are playing within the rules. But then maybe you tweak something in particular, and what's what previously seemed impossible, all of a sudden is apparent and possible. All right, did I miss anything? Did that does that kind of cover the three types of creativity?
*  No, quite the opposite. You covered a lot, I think. So maybe we can, we can unfold some of these these terms, like, maybe not one by one. But I think one of the the ways to start would be to look at the sort of the history of creativity, you don't have to go into this for too long. But like, what, where does the term come from? And one of the things that if you if you just study the word is that it's actually a relatively new term. So, you know, the Greeks and the Romans, they had, of course, I'm going to
*  they had conceptions about what creativity was, I don't think they had the word creativity, there's a much later term. But they had conceptions about how something new arises. So one of the earliest references I could find was in Socrates in the Meno dialogues, where he, you know, he has this Socratic conversation about how do you learn something? Do you is it something that you remember from the past? Or otherwise, how did it enter your brain? Like, how did it? Where did it come from?
*  We're just vessels, right? Yeah, it's Yeah, so this is the other if you talk about artists who have and they're talking about the experience of creativity, which is again, something else that we can talk about a creative product. We can talk about a process it is creative. That's that's my personal preference. But we could also talk about the experience of being creative, which might not be the actual thing. But it's a it's if people reported that way, that's how it feels to them. So if you go a little bit, you know, further down the line in history, you have, of course, the
*  Thomas from Queen us. I don't know. domestic Thomas Aquinas, I think. Yeah, so I'm trying to make him into an American. So Tommy Aquinas is what we call him. Yeah. Tommy Aquinas. All right. So he he he I mean, he has this famous argument like the out of nothing can come offing, right? So how does something come about out of nothing?
*  We've come to this point already in the conversation. How do you get something to nothing? Well, I'm doing it chronologically. So yeah, most interesting. So so I just wanted to refer to that because I think this is really something central also in creativity research is what gets you into
*  creativity research. But this is why creativity is a gateway. Once you start asking about those questions, a whole new set of questions open up. And those questions are typically outside of the computational domain. But let's let's let's save that for later. But that's why I think it's interesting. So that's that's Thomas from Aquinas. And then if you go to more recent history, you see a sudden flip in the meaning of creativity. It goes from discovery to invention, if I sort of summarize it. So for 1000s of years, people looked at
*  knowledge as it's something that's already there. I'm just the one to discover it, like America. And at some point, and it's hard to pinpoint when but at least this is how we tend to think about it right now. It's we talk about generation about creation about there being something that didn't use to be there.
*  De novo, de novo, regardless of whether I knew about it or not. It's just it wasn't there. Maybe it's because you know, of our sort of religious, also religious flip that happened that nowadays we are so we have the hubris to actually say that we created something out of nothing or that something new actually arose due to us and maybe 1000 years ago, people wouldn't dream about saying something like that, right? More humble and say, Look, I just stumbled upon this, you know, maybe that's what musicians
*  nowadays also, they're more humble. It's a humble way of saying I'm not that big. I just stumbled. Some are. Yeah. So maybe it's something like that. But that I think this this this flip is important, because it's, it's two perspectives on what creativity can be. And it's, in some ways also goes into this distinction between combinatorial exploratory and
*  inter-formation of creativity, because there you also talk about something new, and either this new was there and we found it, or we actually, you know, did work to create something new. And when you talk about, you know, combinations, that that could be, you know, discovery, that could be something that was already there. And I think the same goes through for exploration. So the way I think about exploration is we have a search space, we have a, you know, computationally, we have a fitness function that is sort of, you know, if we
*  sample the search space, we get an answer of the value of the search space. And then we can use some kind of hill climbing algorithm or whatever, to sort of maximize over the search space. And then we then we found it. But then again, we found it. So it was already there. We just discovered it.
*  We can we can do it in an exhaustive search, essentially.
*  Yes, absolutely. I mean, even the term exploratory creativity already, you know, refers to our lack of knowledge rather than us creating something new. Right. But transformational creativity doesn't act transformation. That's that's
*  something that you you are responsible for. So the way I look at transformational creativity is we have a particular search base, but we're unable to find what we're looking for within the search base. So we need to transform the search base or go into a different search base.
*  And then within it, we can do exploration, creativity and or combinatorial and then we can find it. But there's a paradox there with computers, how do you get a computer to transform its own search base? And I think that question, which is
*  ultimately a Thomas from Aquinas question, but rephrased in computational terms, I think that question is really a driver for research into creativity.
*  All right, maybe we should because that that brings up constraint immediately as well. And I want to get kind of deep in it because I love the idea of constraint. I think it's so much more important than
*  people often conceive of. That's why I like it's, you know, in the title of your dissertation and for the awesome office, it's creativity and constraint. I mean, they go hand in hand. So
*  we'll hold off for just a second because I do want to talk just, you know, a little bit about the neuroscience of creativity.
*  And then about its relation to intelligence and then we'll talk constraint. So there's not a I mean, okay, there's a lot of work done on the neuroscience of creativity. There are not a lot of answers, perhaps. It's kind of a, you know, a big mess. There are models for it.
*  There's like a model called the frontal disinhibition model. And one of the recurring themes in
*  the neuroscience of creativity is that it might, you know, there are these people who have brain damage and it's usually frontal damage or frontotemporal damage.
*  And all of a sudden they weren't creative. They get the brain damage. Either they're getting old and it, you know, atrophies or they get hit upside the head. And all of a sudden they're
*  genius artists. And so anyway, there's kind of been a lot of back and forth on that with lesion studies and also with imaging studies.
*  And it's kind of swirling around this theme that the common thing between all these cases is that there's a disinhibition.
*  So you have these, you know, your frontal regions, a large part of their job is inhibiting the rest of things. And then when and then they can disinhibit something and that allows that other brain area to then go wild, right.
*  So when you get rid of this inhibitory function of the frontal cortex, and it's often related to frontal and temporal cortex and their interaction, when you get rid of that, that inhibition, it disinhibits and allows these
*  other areas often associated with artistic creativity and or other creative processes, they go wild and all of a sudden you're a creative genius. Okay.
*  Now the history of, or sorry, the neuroscience of intelligence, because I mean, we should explore this difference or similarity between intelligence and creativity.
*  So I'll start with the neuroscience here and then we can kind of back off and talk about intelligence and then how they're related.
*  So I maybe the best known neuroscientific theory of intelligence is called the P fit, which is the parietal frontal integration theory.
*  And this basically just states that intelligence is correlated with how efficient information can flow along the frontal and parietal regions of the brain.
*  And I'm going to leave it at that because these are both creativity and intelligence, the neuroscience is just wide open field.
*  We don't know what the fuck we're talking about, really.
*  And people will take, take offense to that.
*  And they should, because we do, you know, there's a lot of great work being done.
*  But like creativity, intelligence has a billion definitions.
*  Howard Gardner, for instance, his version of intelligence, he has started off with, I think, seven different versions.
*  And now it's up to nine or 12, somewhere in that range.
*  But he defines intelligence as a biopsychological potential to process information that can be activated in a cultural setting to solve problems or create products that are of value in a culture.
*  There's this kind of well-known paper by Legg and Hunter in 2007, where they looked at over 70 different definitions from the literature of intelligence.
*  And then so they kind of summarized all these different definitions of intelligence into one, that being that intelligence measures an agent's ability to achieve goals in a wide range of environments.
*  And then I'll mention one more sort of theory of intelligence or definition.
*  Recently, Francois Chollet has written this kind of manifesto on intelligence with a new definition, giving it sort of a more formal and precise definition, which is essentially that intelligence is skill acquisition efficiency.
*  Right. It's it's well, I'll just quote from his paper from his definition.
*  It's the rate at which a learner turns its experience and priors into new skills at valuable tasks that involve uncertainty and adaptation.
*  All right. So, I mean, that was a very long winded.
*  But so, you know, what is the relationship to you between creativity and intelligence?
*  Yeah, well, I mean, in AI, we have a, of course, a well-known definition of intelligence, which is the Turing test.
*  Oh, God.
*  Which is a yeah, I think we're on the same page on this.
*  But so the idea is that you define intelligence not by looking into the processes that happen, but you define it based on the output more or less.
*  Yeah, I'll just summarize it. Right.
*  So you can look at the system from the outside and then say if it's intelligent or not.
*  And, you know, the philosopher John Searle made a good argument against this, which is a Chinese room argument, which is basically saying we can imagine a system that has, at least to our perception,
*  no intelligence whatsoever, but that will produce intelligence outcomes.
*  So I think your response is also telling, when I mentioned the Turing test, in that it's a bit like cheating.
*  So this is the type of cheating I was talking about if I talk about AI.
*  It feels sometimes like we're facing such a difficult problem that we just accept any chance to sort of cheat our way through it.
*  Move forward.
*  To move forward. Because, yeah, this gives you the appearance of moving forward.
*  So as much as I think that Turing test is a value, I mean, it's a valuable contribution to the field.
*  It's a very interesting concept.
*  But I think being stuck with it right now and accepting it as your definition of intelligence, I think it's a weak move because it doesn't tell you anything.
*  It doesn't tell you why something is intelligent or not, or it doesn't tell you what types of intelligence that could be out there.
*  It just tells you it's an evaluative argument.
*  So you can evaluate a system based on it, but it doesn't help you understand how the system works.
*  So this is why I like creativity, because I don't think you could have a Turing test of creativity in the sense that I could easily create a computer program that writes a Shakespeare sonnet.
*  And then I'd ask, is this intelligent?
*  You might say, well, based on the Turing test, this is pretty human-like.
*  So maybe yes.
*  If I say, is it creative?
*  I think you'd have a much harder time judging that because the Turing test for creativity just sounds odd because we know that originality is relative to what's already out there.
*  So you need to have a, it's a relative term.
*  So you need to have a foundation to base this on.
*  So creative compared to what?
*  So I think, and this is also why it's sometimes called the holy grail of human action and also intelligence.
*  Creativity is generally acknowledged as a very hard problem that requires you to go into the system and really understand what is happening in there before you call something creative.
*  How did they do that?
*  Yeah.
*  And so I consider creativity, therefore it's sort of, it's more like a gateway drug to other types of human behavior that are non-computational.
*  So if you accept the premise of creativity, that you need to focus on the process that's going on, and then you go into a computational system and you look at the transistor, then you say, well, that's not really creative.
*  And if we have a simulation of a different type of system, which is non-computational, so we have a computational simulation of something non-computational.
*  We also are having a hard time imagining what that would be like.
*  Like what would the creative system look like, even if we simulate it?
*  So I just want to clarify.
*  So is your sort of attitude that, okay, yes, the Turing test, there's plenty of problems, but you're okay with an operational definition of intelligence if we all agree saying, if it does this output, it's fine.
*  We would give it some input.
*  It gives us, gives an acceptable output and we can measure that and we can call it intelligent or something.
*  And the difference being that for creativity, you actually, the definition of creativity is more about the internal works and internal processing.
*  Is that, am I reading right?
*  I mean, in some respect, you could say artificial intelligence is already solved because I have a computer that I can play chess against.
*  Sure.
*  And it's so if it's in the end, it's all semantics, but I would say, you know, my computer is pretty intelligent in the sense that in a Turing sense, the Turing test.
*  Is it creative?
*  Well, then I have to, you know, I get into this X mean hello argument.
*  Like, well, what did this intelligence come from?
*  Where is it?
*  Is it the data that it used?
*  Is it my input?
*  Is it the programmer?
*  Is it the hardware?
*  Like, where do I pinpoint the creativity or do I pinpoint the production of this intelligence?
*  I don't think an answer is directly necessary there.
*  I think just asking those questions already gets you further than you could get within the computational paradigm or you could get with intelligence because you enter this problem set for which our computational theories or even broader, I think our information theories are
*  shannonian theories.
*  They don't have an answer to this kind of question.
*  So and this is this is what I was referring to earlier with with the I'm plus work.
*  There's no way to have a set of points, data points in space, and then have the algorithm determine which direction is most interesting.
*  You can only do it with more data points, which it pulls towards, but the computer doesn't have any sense of what is interesting or valuable.
*  It can only have something like value if we tell it.
*  So you always need a scoring function, a fitness function or objective function.
*  Without it, a computer doesn't want anything.
*  It doesn't have this sort of driver that we have.
*  So if you take this, you know, if you go along with this definition of creativity, I think you have to acknowledge that there's something about us as biological beings that is not represented in computers.
*  And that opens the sort of the door to a whole range of new questions.
*  Is the intrinsic motivation necessary for creativity?
*  Is the driver like, you know, can you have creativity without implementing?
*  It's a strange question.
*  No, I think I get your question.
*  I think my answer would be no.
*  I think you need a driver or you need purpose.
*  I mean, there's many terms for that.
*  You need something like a concept of value that is not extrinsic.
*  It's not, you know, you're not being told what valuable is.
*  You actually have your own assessment of what value is or what usefulness is or or goals.
*  You need to have some type of goal in order to create something that's creative.
*  This is why some people like I think Brian Cantwell-Smith argue that to really create artificially intelligent systems, they're going to have to have some something at stake that they will no longer be able to run unless they solve the problem.
*  You know, things like that, you know, grounded within within the physical world and where they can get injured, where they can not function well if they don't do something properly.
*  So it's, you know, more and more humanistic sorts of terms.
*  Absolutely. I think there's something to that as well.
*  Are intelligence and creativity orthogonal then?
*  Or does a creative system have to be intelligent?
*  Or does an intelligent system have some creativity?
*  You know, are they completely orthogonal?
*  I think here we get into different meanings of creativity.
*  So if we take, let's say, the big C creativity that's sometimes called so, you know, what artists I would say that's I only know humans who are artists.
*  Well, can you just distinguish between big C and little C just to be really clear?
*  Yeah. So, I mean, big C is that, you know, big C creativity creates the kind of stuff that you hang up in a museum.
*  Little C creativity is, you know, creating your grocery list.
*  Big C like your zoo of networks poster.
*  I would, I will, I'll just be humble here and call it little C.
*  But it's hanging up in a museum.
*  Yeah, you're right.
*  That says you're right.
*  Yeah. So it's, it's the, the type of creativity that we typically associate with art or science or humor, which is also a type of creativity.
*  So it's, it's that.
*  And the little C is, let's say our everyday creativity that we need to just function as normal human beings.
*  So if you talk about the big C creativity, I'd say I only know examples of humans who are artists and all humans I know are intelligent.
*  So they, they sort of, you know, those two definitions always go inside.
*  Doesn't mean that they're the same process, but we don't have any example of something that is truly artistically creative, but not intelligent.
*  I think if we talk about the little C creativity gets more interesting because there you, I mean, I have a cat.
*  I think in some ways you could call him creative.
*  Like sometimes he has these creative ways of, you know, getting me to do things.
*  Yeah.
*  And it's pretty, that's intelligent.
*  It's creative.
*  But, but if you, if you sort of then, you know, unpack this idea of creativity and smaller and smaller C's, you might end up at a point where it's not directly intelligent in the terms of having a fit.
*  But there's, there's this sort of, there's still this sort of purpose driven and this goal.
*  But, but I think this is a biological question.
*  Ultimately, we're not talking about AI anymore.
*  We're talking about biology.
*  Then these fine grain distinctions.
*  It's really hard to say, to draw the line where, where is it just a biological, I'm freaking hungry, Stefan.
*  Yeah.
*  And then, you know,
*  Yeah.
*  And I think the term that's missing, it's another C term is consciousness.
*  And I don't intend to spend the rest of this podcast talking about it, but I mean, this is, it's something that we, we really, we really need to be able to do.
*  This is, it's something that we, we really, we try to overlook as much as we can, but how can you have intelligence or like real intelligence or how can you have real creativity without consciousness?
*  I don't think you can.
*  I think we can do pretty good simulations of it, but I don't think we can.
*  So yeah.
*  And I mean, going into those kinds of definitions, it's even, it's even more difficult.
*  Oh, it's just rough terrain.
*  It really is.
*  I mean, we all end up philosophers, destitute philosophers.
*  The, I was looking up the neuroscience of creativity, which I wasn't well versed with.
*  I ended up reading an article about genius and the idea being that genius is someone is when someone has high intelligence and creativity, and they really dissociated intelligence from creativity where you can have high intelligence, but be a savant and not have creativity so that you're not combining anything new, but you can memorize the phone book, for instance.
*  And that's highly intelligent in some domain, but lacking the creativity.
*  So, you know, I mean, these are all, all these terms are up for grabs.
*  Really?
*  Maybe we should.
*  Oh, did you have, I'm sorry.
*  Were you saying something about the genius?
*  I was, well, I was, I was, I was just mentoring Einstein's definition of genius.
*  I mean, sometimes it's, it's, it's, there's a very small distinction between genius and madness.
*  So I think those type of big C, because that's genius is also big C creativity.
*  There's also a lot of cultural norms involved in that, in what we would call big C creativity or not.
*  And for me, that's, that's, that's too far out there to actually consider.
*  So that's, I, I need to make the questions a little bit smaller than that.
*  That's why I also prefer to think about small C creativity because you want to operationalize the processes that are involved.
*  So, so getting a model of my cat is already difficult enough.
*  You ponder your cat a lot.
*  I can tell.
*  That's awesome.
*  Yeah.
*  So, okay.
*  Constraint.
*  This is the other half really, you know, of, of the Asimov Institute.
*  And, and, you know, I know that you think about this a lot.
*  You either, you worked for or with Terence Deacon.
*  But let's say both.
*  Yeah.
*  Okay.
*  I mean, I, I did my, my master thesis project with him.
*  Yeah.
*  Under him, I should say in Berkeley.
*  And, and since then, we, we, yeah, I've just been fascinated by him.
*  I go to Berkeley as much as I can.
*  I really enjoy being there and then reading his stuff and talking to him.
*  So let's call him a mentor or, yeah.
*  Now, yeah.
*  And they all, this changes over time, of course.
*  Now you can be a collaborator.
*  Um, but he has some fascinating ideas.
*  I, so he wrote this book, Incomplete Nature, which, you know, summarized at length, a lot of ideas that he'd been working on for a long time.
*  About, largely about the real importance of constraint.
*  And I guess Incomplete Nature kind of builds up from, well, nothingness from the concept of zero.
*  And we don't have to recapitulate Incomplete Nature here, but, um, it uses, uh, thermodynamics and dynamics in general.
*  And the concept of how dynamical systems can come together and it's the constraints that allow them to build on each other.
*  And then he kind of uses that to build up to consciousness.
*  Okay.
*  So that's, there's my summary of Incomplete Nature.
*  Um, but, uh, and so I know that you, you've been a fan of his, like you were saying for a long time.
*  And I don't know if you want to start off talking about sort of his work, but I, my question is what is the role of constraint in creativity?
*  I don't know which, which question is, is, is the bigger one of those.
*  Um, well, it's fascinating that constraint is, it's a negative term.
*  And I don't know what I mean by that is it's, it's based on an absence, right?
*  It's the things that don't happen that define what constraint is.
*  So that's, that's one.
*  And what Terry does is he uses this concept of absence to, as you say, build up from more or less mechanical systems, things that we can describe with a pretty accurately with the physics up to, um, cognition.
*  And the, uh, I would say the pivotal move there, or one of the crucial moves he makes is in the domain of biology.
*  And here are a set of questions that I think are still scientifically unanswered yet, but those are crucial to actually move forward in my view, with the field of creativity or artificial intelligence.
*  Or if we want to get a good understanding of what actually this, this goal driven, purposeful behavior like comes from, where does fitness functions come from?
*  How do you, how do we internally score a given situation or a certain creative output or not?
*  We need to have a better understanding of our own, so to speak, architecture.
*  And it's not a computational architecture.
*  It's a biological, physical architecture.
*  Yeah.
*  It's well, it's yeah.
*  So it's physical.
*  It needs to be grounded in physics, but it doesn't mean it's, um, it's like Newtonian or even Boltzmannian.
*  Uh, and so what, what Terry does in incomplete nature is he, he scaffolds this with this term constraint.
*  And, um, he, I love the book because it marries some, some genres.
*  So in one hand, it marries the social sciences to the, um, to the, uh, the physical sciences.
*  So, so, right.
*  So, uh, if you, if you were able to bridge this gap from physics to psychology, you've created a very interesting bridge, but it also creates a bridge between, uh, Western science and Eastern philosophy.
*  Because a lot of the ideas that, you know, that surround absence and constraint are ultimately Daoist.
*  So there's also this gap that is made.
*  So for a, uh, hopelessly romantic scientists like me, this is a fantastic book to read.
*  Oh, I agree that the concepts are just wonderful.
*  I really, I recommend it.
*  I personally couldn't get through the whole thing because the writing is so dense and contained so much, but, and actually you had mentioned to me that there's a, a different book that sort of summarizes, uh, incomplete nature.
*  I think the writing in incomplete nature is dense.
*  It's not a small book, but even then there's, there's many original, um, very deep ideas on almost every page.
*  Yeah.
*  So it takes time to get through and it also takes a couple of rereads to understand some of the ideas that are, uh, that are in there.
*  And, uh, my friend, uh, and, and also, uh, third beacon collaborator, Jeremy Sherman, uh, made a nice effort to write up, uh, and explain some of the ideas that are put forward in incomplete nature in a different book called neither ghost nor machine.
*  Okay.
*  So I would definitely recommend it as a, as a, as it may be as a starter or an explainer or as a sort of companion readers, companion to the incomplete nature.
*  Uh, because, because he also shows how relevant these ideas and how important these ideas are.
*  I think that's it's, it's so it's good to be aware of that as well.
*  So I guess we don't need to go down the constraint in Terry's work as much, uh, I mean, unless it's, it's relevant, but, you know, I guess, but how do you view constraint, uh, within creativity?
*  And I don't know if you want to frame it among the three types of creativity, because, you know, we're all mostly concerned with transformational creativity, creativity, I suppose.
*  Well, we can, we can do a, um, a nice thought exercise to get a grasp of the, of what constraint means for transformational creativity.
*  Sure.
*  I want to, I want to make a disclaimer because I think the type of constraint we're referring to here is not, it's not the type of constraints where that, that, uh, Deacon refers to in incomplete nature.
*  That's a much more unpacked concept of like physical constraint that actually does work.
*  Here we're just talking about constraint as something that constrains to search space, but let's, let's, let's go, let's go into it.
*  So, so thought experiment.
*  So what I'm going to ask you a riddle and I want to also ask you while you're thinking about the solution to the riddle to introspect your own thought process.
*  So it's a two layer riddle, right?
*  So you have to solve it, but you also have to sort of introspect and look inside what's actually going on in your brain.
*  Okay.
*  So here's the riddle.
*  You're in a room and there are three buttons in this room.
*  There's a door.
*  If you enter the door, there's another room and there are three light bulbs.
*  So I'm, I'm, I'm going to ask you which of the buttons, so it's an on and off, you know, flip switches, which of them is connected to which light bulb.
*  And I'll tell you that the light bulbs are all off from the start.
*  And I'll also tell you that once you enter the door, you're not allowed to go back.
*  So you can stay in the first room, play with the switches.
*  You don't see what's going on in the other room.
*  Then you enter the door and close it.
*  Then you look at the light bulbs and then you have to provide me the answer, which light bulb is connected to which switch.
*  Okay.
*  So, uh, and, and you may describe what I was, well, let me try to solve it.
*  First of all, the sad thing is I know I've heard the answer before and now I'm trying to, now I'm trying to recreate the answer in my head.
*  So that's maybe that's cheating.
*  You're just, you're discovering the answer rather than just a vessel.
*  Yeah.
*  So can I, can I shoot the light bulbs from the other room?
*  Tell me the answer.
*  Tell me the answer.
*  Can you, can you, yeah.
*  Let's go back to that question again.
*  So the answer is, uh, I turn on one light bulb, switch, then I turn on a second one, but after like a minute, I turn it off again and I leave the third one off.
*  Yes.
*  That's the heat.
*  The heat, right.
*  Then I go into the other room and I, there's, there's one light bulb that's off, but eat it.
*  And that's how I know the third one.
*  So you can, um, by process of elimination, there'll be a hot bulb and a not hot bulb.
*  And then you can eliminate which one you turned on, which one you turned off and which one you didn't.
*  And then you can map them.
*  Um, so of course the, the natural tendency, and even though I had heard that answer before, uh, I was not a good vessel.
*  So I was picturing and I was trying to think outside the box.
*  Like, what could I do to figure this out?
*  I mean, I just visualized what you spoke.
*  And then I thought about the different combinations of turning lights on and off and then walking through the room and examining the bulbs.
*  And that's about it.
*  And how I, you know, and then, and then there was a problem with me figuring it out.
*  Well, what, what did you discover?
*  So you, so you said that this arena where you look at the sort of the permutations of the switches in the light bulbs.
*  Yeah, I did not, I didn't come to a conclusion.
*  Did you come to the conclusion that you couldn't figure it out by any type of combination of switches?
*  Correct.
*  Yeah.
*  I, I, my conclusion was that it would be inconclusive to stand on one side, flip switches in any order and walk in the room, next room and figure it out by looking, just by looking.
*  Right.
*  Right.
*  So just by, so I think that would constitute a search space for you.
*  So, so, you know, there's a couple of access and dimensions.
*  There's a, some actions that I can do with the, doing the switches.
*  I can go into the other room and I figured out through, I think, exploratory creativity within this search base that there's no satisfying answer there.
*  And what happens next is the interesting part.
*  So how then do you solve the answer?
*  Well, you start exploring different search spaces.
*  And so this is, this is getting into this transformational creativity concept.
*  I would say it's a, it's a metaphor, but still.
*  So I recognize that my original search base doesn't suffice.
*  So what do I do?
*  I go through a process like, hmm, there's a riddle.
*  There's probably an answer.
*  So I probably have to include something else.
*  And then you ask, can I shoot a light bulb from, from, from the other side?
*  I mean, there's, there's tons of things you can imagine that would actually allow you to solve the riddle.
*  You know, maybe you can, you can cheat and open the door.
*  Or you have like a sledgehammer to open the door or you can call a friend and go to the first room or.
*  You have to, you have to understand I'm in the United States.
*  I was born in Texas.
*  So of course I'm thinking guns and shooting.
*  Right.
*  I wouldn't have never come up with that, but I would probably wear clogs or something and then solve it.
*  That's my, yeah.
*  This is how you started your thought process.
*  Yeah.
*  You throw your wooden clog at the.
*  Exactly.
*  Yeah.
*  And then what comes about.
*  So this is really for me, this is a really interesting creative process that starts going on.
*  And two things happen first is diverges.
*  Right.
*  So shooting, calling a friend or whatever, there's all kinds of new sort of options that appear.
*  Yeah.
*  And then there's, this is not always the case, of course, but then there's the option of using the heat of a light bulb to solve the riddle, the riddle.
*  And then it's the second interesting thing that happens.
*  As soon as you hear the answer, you're like, yeah, that's it.
*  So we know that this is a fitting answer somehow.
*  Yeah.
*  Why?
*  Why?
*  Why?
*  Why is this better than shooting?
*  Why?
*  It's something I mean, I don't have any, I think for me, it's something aesthetical, probably.
*  It's something that just connects that fits, but it fits with our broader sense of not only our knowledge, but also our goal driven behavior.
*  There's a purpose in it.
*  There's this like, oh yeah, this is this, we all recognize this is it.
*  So in doing this transformational creative act, we use our feelings, we use our, I would be inclined to say our sentience to actually figure out what the answer to the riddle is compared to other answers.
*  How would you program a computer to do this?
*  There's a paradox because either you give it a search space, it doesn't find the answer and then it's stuck.
*  Or you widen its search space so that it includes the heat of the light bulb.
*  But then you widen the search space.
*  Computer didn't widen its own search space.
*  I'm not arguing that it's completely impossible for computers to do something like that.
*  I'm just saying that in the typical computational paradigm with the programmer and the scoring function, you don't get to this type of creativity.
*  Well, often in the way that, I mean, this is like a really old theory about how creativity works.
*  I cannot conjure it.
*  I'm sure you know it.
*  There's like a four step process, right?
*  Proposed where you basically you work on a problem really hard.
*  You come up, you cannot solve it.
*  You cannot solve it.
*  And then you go on a walk and all of a sudden it just comes to you.
*  Right?
*  So there's this unconscious processing that happens while you're not thinking about it.
*  And of course, computers would never go for a walk.
*  You know, have, let me just back off this problem.
*  The computer says to itself that that would never happen, at least in today's conception of computation.
*  Often the intrinsic, not intrinsic, we intuit the solution, it seems like after this unconscious processing step or series of steps.
*  Right.
*  Yes.
*  And what you mean by unconscious is subconscious, right?
*  Subconscious.
*  Yeah.
*  Yeah.
*  Subconscious.
*  Yeah.
*  And I guess what I failed to mention there is that part of the subconscious processing is letting the constraints fall or reorganizing your search into different constraints.
*  I don't know.
*  Am I onto something there?
*  Right.
*  Right.
*  But I think you are.
*  But first, and this is the first step of this four part process, first you have to build up a set of constraints.
*  So in other words, you have to build up your own search space, your own search space.
*  Yeah.
*  In order to know which of the constraints you can drop.
*  How do I attack the problem?
*  And then you have to reconfigure how you attack the problem once that doesn't work.
*  Yeah.
*  Well, so this is my theory.
*  But if you build your own search space, if you generate your own constraints, those constraints are not imposed on you, but they're intrinsic.
*  And that means that if as soon as you're faced with a problem that is unsolvable within those set of constraints or within that search base, you have an intuition for which constraint you can drop or not.
*  So this gives you a direction in this sort of multi-dimensional problem.
*  So rather than randomly dropping constraints or randomly adding new parts of the search space, we can actually have a sense of where we're going and where we need to head.
*  And so this is where the sort of the shortcut that we use if we program computers, where we imagine a certain constraint to be useful, valuable, and then we impose it into a computer program and it works.
*  But then we leave it alone.
*  The computer doesn't know what the constraints represent.
*  It's us who know it.
*  So it's a tool for us.
*  But as soon as we then want the computer to start dropping constraints or exploring new parts of the search space, design me a good dress, beautiful dress, give me a good music piece.
*  It can only do random.
*  It could or it could diverge away from the samples or towards the samples.
*  There's a statistical way of approaching this, but it doesn't have a evaluative criterion unless we give it to it.
*  But then again, it's us who transform the search space and not the computer itself.
*  So to have a truly autonomously creative system, then you would need to build in a way to for the system to somehow notice its own constraints and the constraints that are relevant to disregard to solve the problem.
*  Right.
*  But I think the the autonomy is the constraint.
*  So once you have a system that generates its own constraint, that's this is what autonomy is about.
*  So.
*  To summarize it, the bad news is that we're a long way away from these types of systems, at least in the computational domain.
*  The good news is, I think if you solve one of these problems, you actually solve many of them.
*  Many of them are referring to the same problem.
*  But it's this this sort of biological step or rather, we need a much better understanding how we as biological systems work and how we scaffold through constraints from pure physics.
*  To psychology.
*  But once we get to that point, I think many of the problems we're facing with artificial intelligence today, even the normative ones, when we talk about ethics and values, the ones that we are right right now out there in the domain, I think they will all actually change.
*  Maybe not be solved, but they will completely change by nature because we're dealing with a completely different type of architecture, a different type of system than the ones that we have now.
*  But.
*  The first step is moving out of the computational paradigm, and that's really difficult because we we are so addicted to thinking about systems as though they are computers or billiard balls Newtonian.
*  So I sometimes you know, this this this this famous metaphor where over time, if you look at history, people have compared their brains to the latest innovation.
*  Right.
*  Yeah.
*  So, you know, in the time of Aristotle, it was the hydraulic press.
*  Yeah.
*  You know, in the I think in the Renaissance, it was the clock like 100 years ago.
*  Our brains were like steam engines, water pumps before that water pumps.
*  There's Yeah, exactly.
*  And then and then there's computers and now and now we have to sometimes you know, I get questions like is the internet conscious?
*  Yeah.
*  And don't get me wrong.
*  I'm not saying it's not.
*  I'm fine with it.
*  I'm fine with this sort of research area.
*  I'm just saying that there's a tendency for us to compare ourselves to our latest innovation and we should be aware of it because it can be a bias in our thinking.
*  What's probably happening is that it's just the most complex thing we know.
*  And our brain is also very complex.
*  And that's why they they seem to align.
*  There's there's a new one that's I think there's one that's that's coming, becoming more and more popular.
*  I'm not sure if you're familiar with Donald Hoffman's take on, you know, our perception of reality is completely different than what reality actually is.
*  And that we're where our perception is this like operating system in as much as like when we see the icons on our computer screens like the trash.
*  It's not an it's not the actual trash.
*  It's just the way that we interface with the computers.
*  Well, that's our perceptual and motor systems with the world.
*  That's the way we interface.
*  And in reality, it's completely different.
*  And I thought, ah, yes, virtual reality goggles are getting popular.
*  And that's the latest technology that it's all none of it's real.
*  You could get lost in virtual reality and like the matrix and things like, you know, things like that.
*  I think, OK, that makes sense that people are thinking that way because now virtual reality and that idea has crept into our thought processes.
*  Right. Right. And you mean same with quantum computing.
*  Yeah, you already have these quantum theories of consciousness.
*  That's been around a while.
*  Yeah. Yeah, you're right.
*  They've been around a while, but I'm sure they'll gain more in popularity as quantum computer computing over the next couple of years will sort of also grow in popularity.
*  Again, interesting field of research definitely needs to be explored.
*  But it's not a given that just because our brains are complex and quantum is complex that they're the same process.
*  I think there's an underlying sort of tendency to sort of assume they might be related just because they're both very complex and we don't understand how to work.
*  Yeah, that's like a halo effect.
*  And then there's also my favorite is explaining one mystery by referring to another complete mystery, which is, you know, I don't know, there's something inherently attractive about that stuff to us as humans.
*  We're all dumb.
*  Yeah, well, I can see why.
*  I mean, with quantum, like we need.
*  So, like I said, I think we need an escape route away from computational thinking.
*  Right. As useful as it is, we need a way out of this computational framework.
*  And of course, this is what quantum provides, because it's is generally accepted also in the hard sciences that it's a completely different way of thinking about mechanical systems, about, you know, it's a different type of computation.
*  But the part that doesn't click with me is if you want to explain consciousness with quantum, how will you ever get there?
*  Because you still have to explain why my cat is conscious, but my TV isn't and they both have quantum particles inside.
*  Right.
*  So we need an explanation of the level at the level of, let's say, our sort of visual objects of range where we could say this is conscious, this is not either that or you're a sort of pan consciousness where you say,
*  everything's conscious.
*  The panpsychist, which I find that so disappointing that people go down that road.
*  I see why it's tempting.
*  The panpsychism.
*  Well, I think it's for lack of a better theory.
*  I think there's tableness in everything.
*  There's a little bit of like table like quality in all matter and throughout the universe.
*  How about that?
*  Well, I mean, it's very hard to contradict your assumption.
*  Of course, I don't know how to start, but I think there is actually a different way out of this computational framework.
*  And this is the constraint story.
*  And I think what the constraints for the story refers to is also a set of familiar terms which have to do with emergence and self-organization.
*  And this route will actually build up in terms of size, right?
*  In terms of skill, it builds up from smaller particles to biological systems.
*  Because if you look at biology, self-organization is much more prevalent than in the sort of dead physical world.
*  So there's something about self-organization that is attractive, is an attractive organizational mechanism that nature employs to actually scaffold and build systems.
*  And then we look at the brain and we find all the necessary components there to actually have this type of self-organization.
*  You know, there's this recurrent, amplified, fast moving particles and electrical signals that sort of are sort of mixing up in our brain.
*  There's definitely a self-organizing emergent quality to our brain, but we're just having a hard time wrapping our heads around it because we don't have the tools and instruments to understand what emergence and self-organization is.
*  But constraint in that respect is super important because our brains are constrained to the space within our skulls and that there are these constraints of the recurrent connections that, you know, so you implement the recurrence, then to build these hierarchical processing structures.
*  So you just can't escape constraint as being just a necessary part of that sort of organization.
*  Are creativity and constraint always tied together or are they, can they be orthogonal?
*  Can you have creativity without constraint?
*  I mean, because if you had no skull and you just had brain, brain, brain, brain, brain, there might, there'd be no end to the process.
*  You wouldn't perhaps loop back and there'd be no self-organizing activity.
*  Now I'm just getting way out there, I realize.
*  Well, I'm tempted to go with this idea that there might be two sides of the same coin.
*  So constraint is about the things that don't happen and creativity is what happens.
*  But already when saying that, I feel like it's very un-nuance.
*  I mean, there's a lot more to those terms than just this sort of, you know, this nice sort of paradoxical way of phrasing it.
*  But if you think about it, self-organization and emergence is also about first off constraint, right?
*  It's about the number of potential states that a system can be in is constrained in self-organization to only a couple of states that you sort of see recurring.
*  Otherwise it's completely random and you would have no organization at all.
*  Right.
*  Right.
*  So it would be uniformly distributed.
*  Yep.
*  But it's because of the randomness, but because there's a sort of a decrease in the randomness, decrease in entropy actually, we see a structure come about in self-organization.
*  And so this is exactly the same thing as what happens with a constraint on the system or sort of intrinsic constraint in the system where there's only a subset of the states that actually happens compared to the number of potential states that you would expect there to be.
*  Maybe I'd be tempted if there's like, if there would be a definition of a smallest C creativity, it might be there.
*  It might be this.
*  So it might be the smallest type of creativity might be the states that occur as opposed to the total to the total number of states that could occur in a system.
*  But it's because of this constraint, only a couple of these states happen.
*  Some minimum reduction in entropy or something.
*  Yeah.
*  Yeah, but that's that's so far removed from these sort of genius Einstein Picasso types of creativity that I think they're completely different terms.
*  Right.
*  If you talk about them.
*  So that's why it's difficult to integrate one definition of creativity.
*  So from the neuroscience side or the biological intelligence side, I'm using neuroscience as usual to just cover all of the biological intelligence facet of things.
*  There are lots of different ways that neuroscientists can study something like creativity in human brains and in minds.
*  But from the AI side, you know, is there anything that you would like to see being researched in the neurosciences that would be relevant or applicable to the study of creativity in artificial systems?
*  Yeah, absolutely.
*  I mean, look at the current revolution in AI right now.
*  I mean, it's mostly powered by neural networks.
*  But when we say neural networks, we're not actually talking about a proper simulation of a neural system in the brain.
*  We're talking about a very loose, loosely based abstraction of a neuron.
*  You know, it started with a perceptron and then you hook those up together.
*  And essentially, the point where we are now is we've diverged quite far away from the let's say our biological inspiration.
*  And we're tinkering with it and we're engineering it in a way that we just, you know, this is how engineering goes.
*  We get good results so that we iterate on those results.
*  But as we move further and further away from the biological inspiration, we also lose track of this inspiration.
*  So I think one way to approach this would be to go back to neuroscience, look at the fruits of that labor and use it as another inspiration to move AI ahead.
*  Because I personally don't believe that AI can move ahead by itself, let's say, without this biological inspiration.
*  I think the brain is so much more complex than even now we understand.
*  Probably, I mean, most people would agree with that, right?
*  But also what neural networks are now, artificial neural networks are so much more basic, I think, than the type of AI that we will have decades from now.
*  So where does this progress come from?
*  If you start with, let's say, current day neural networks, the ones that you could see in the neural network zoo, there's so many directions you can take this.
*  So how do you decide which way to go?
*  I think cognitive neuroscience and neurobiology have a very important role to play in this story, namely, figuring out how these processes work in the brain.
*  What does work, what doesn't work, and then inspiring AI to start engineering those kind of processes.
*  So in a previous podcast, you talked to Wolfgang Maas.
*  I mean, he did research on gases in the brain.
*  Like, I haven't seen a good neural network simulation of this, but this might be a very inspiring idea.
*  Like how do you maybe it's used for like long range communication between neurons, or maybe there's a different kind of sort of spatial function within the clustering of a neural network.
*  There's a reason probably why why nature came up with this idea.
*  So it's up to us to figure out why you do it this way.
*  Well, there are lots of different ways to be inspired, though.
*  I mean, do you think that it necessarily some sort of newer breakthrough needs to come from the biological side of things?
*  Or can it come from physics, for instance?
*  You know, physics is always the go to, right?
*  Physics is the go to.
*  I think I think that's also part of the problem in a way, because, you know, there's there's this gap.
*  I mean, we've talked about it, right?
*  We did this this gap between physical sciences, chemistry, physics, and psychology, sociology, the social sciences.
*  And this this gap can be bridged by biology.
*  And I think when we talk about biology of the brain, we talk about biological neuroscience.
*  So this is actually I think the skill at which you need to look at how you get creativity is actually at the at the skill that cognitive neuroscience also looks.
*  So we can we can take a physics approach.
*  We could we could also look at the quantum level, for example.
*  But I find it very implausible that we'll find a, let's say, unique process that we haven't found before that's responsible for consciousness or emotions.
*  I mean, my my hunch would be that it's probably between the level of the neuron and the collective neural network, some somewhere at some level.
*  And those skills, something happens which makes an unorganized collection of neurons basically dead meat and a particularly organized set of neurons.
*  Alive, conscious and feeling and creative.
*  So what's the difference?
*  I think that question that's that's that's yeah, that's something you'd probably look at if you look at the scale of the cognitive neuroscience does.
*  Asking in just a slightly different way.
*  Do you think that you could come to a satisfying account of artificial creativity without biological research or or biological knowledge from this point forward?
*  Let's say you think you could toy your way to it.
*  I think it would be very unlikely, because even if you engineer something that is created, you still need to understand how it works.
*  And I mean, it's it's perceivable that we would stumble upon this solution or find it one way or another by engineering.
*  We get a machine learning tool that's actually creative and then we sort of trace back our steps.
*  And that helps us understand how the brain works.
*  I mean, it's perceivable that I mean, but it's very unlikely it works this way.
*  Usually work the other way around.
*  We have the example.
*  We know that we are creative.
*  We know we can we can look inside our brains.
*  And then so let's use that as inspiration for the tools that we're building rather than the other way around.
*  It can work that way, but I think it's unlikely it will work that way.
*  I mean, it is the baseline definition of creativity is enmeshed in our own behaviors.
*  Right. That's where we define creativity, essentially.
*  So I guess you can't escape it too much.
*  Yeah, I think another for to give you an example for us.
*  So I think one part of neuroscience that could inspire A.I.
*  would be the lessons that we learn about perception nowadays.
*  So if you look at perception in the computational framework, it's input and outputs.
*  Right. So the idea is light falls onto my retina, which pushes things in motion in my mind.
*  And the output is my arm moving or my head moving or me understanding something.
*  That will be the output. Right.
*  What we learn in neuroscience is that perception is much, much more an active process than the passive process that's described here.
*  That's because if you use a computational model, there's no such thing as a sort of active process in computation.
*  Computation is all feed forward.
*  Whereas in actual perception, it's more like we hallucinate the world around us.
*  And then the world is doing a selection process on our fantasies.
*  And the fantasy that sticks is the one that is selected out by reality.
*  And that's the one that we create.
*  And that's actually creativity. Right.
*  That's something that I came up with a particular image in my mind of what my world looks like.
*  And then the reality selects on that image the things that are actually true and which are not true.
*  Now, using this as inspiration for A.I., I think it already produced fruitful results.
*  So and there's many more examples, I think, like this, which haven't been fleshed out, really.
*  But my guess would be that there is a lot to be gained in A.I. from these types of theories and lessons.
*  Yeah. My understanding is that active vision is becoming more popular in A.I. research.
*  I'm not up to date on it, but I know there's some excitement around it.
*  Yeah, I know you're right.
*  I mean, like attention networks, for example, they use these principles.
*  Yeah.
*  But it's a lot of it is still feed forward based because a lot of neural network, the way we conceive neural networks is still as a
*  like a tiny transistor, a tiny machine that goes from input to output.
*  It's producing these static functions, essentially.
*  Yeah. So of course, you could model the sort of the active process also as a feed forward function,
*  and you could sort of juxtapose that and then you have a sort of superficial representation of what this process is like.
*  But I think in actuality, it's more a dynamical process.
*  It's something that I think actually emergence is the term to study here.
*  I mean, that has been that for me.
*  But that's a very different type of dynamics than the dynamics that you get from neural networks,
*  even if you use attention mechanisms that have become popular in the last couple of years.
*  But OK, so you come home from work and you have the latest edition of Science magazine.
*  I don't know what nature on your delivered to you via drone, of course.
*  And it's on your coffee table waiting for you.
*  Open it up and there's some neuroscientific advancement in research on creativity.
*  What would that what does that look like?
*  Well, what I mean is, is it neuroimaging?
*  Is it EEG?
*  Is it you know, or is it theoretical work that matches with the brain recordings?
*  Will be impressive to you.
*  If I had the answer, I'd probably be in nature.
*  But let me point out what it's not, I think.
*  I think what we need is a is a model is a better model of how the brain actually works.
*  I think it will be a dynamical model.
*  Now, I don't know if you're familiar with the work of Friston, for example.
*  Yeah, he presents this right.
*  He presents this, I think, interesting but still not complete model of how the brain can work,
*  because he presented at the level of information theory.
*  Well, should we just should we just kind of back up and say this is like this is I think
*  you're talking about the free energy principle that he's been working on.
*  Exactly.
*  Yeah, yeah, yeah, yeah.
*  It's called free energy, but it's still coined in information theory terms.
*  Right.
*  And what I mean by that is that creativity is defined as surprise.
*  Well, I mean, it's not about creativity in his case.
*  But if you if you look at this model, if you look at his surprise model,
*  then it comes pretty close to what you could consider as creativity.
*  Which is a mismatch between what you're predicting and what you observe, essentially.
*  Yeah.
*  So it's your expectations and reality and that there's a they form a gradient, more or less.
*  So what you could then say is that if you learn something,
*  it's relative to your previous world model, your worldview.
*  So if you let's say if you learn a little bit, then the step that you made is not very surprising.
*  So you could say it's not very creative.
*  Whereas if it's it has a huge difference with your previous knowledge,
*  then you make a giant leap in knowledge and you have I mean,
*  this is a very unnew and sort of summarized version of it.
*  Right.
*  And you're going to meet him as a similar theory of creativity,
*  which is also sort of surprise based.
*  So it's based on sort of the expected values considering your current mindsets
*  towards your future mindset.
*  But I think this is still too limited.
*  It's going in the right way.
*  I think the type of model, the type of theory is right.
*  If I open up my nature journal and the big theory of creativity is in there,
*  it's probably has this type of almost Hegelian model, like this complete set
*  that explains a lot of things at once, explains the framing problem,
*  explains the creativity, etc.
*  But I think it's not just the information sphere.
*  I think it's actually more you need to go a couple of layers deeper.
*  And I think in order to do so, we need to know more about the brain.
*  So just to relate that to that approach to creativity, though,
*  from the creativity standpoint, if you're somewhat equating
*  surprise or expectation, well, surprise with a potential for creativity,
*  then it's almost as if the more you know, and this jibes fairly decently,
*  actually, in many respects with experience, the more you know,
*  the less creative you can be because there's going to be a smaller mismatch
*  between what you're expecting, the more accurate your expectations are going to be,
*  and the less you're going to be able to learn about the world or be surprised.
*  And therefore, yeah, but this is the paradoxical thing about creativity,
*  because you could say the more you know, the more constrained you are in a way.
*  So even though your leaps might be smaller, you're so constrained that even a small step
*  is very creative because in an extremely constrained environment,
*  it's very difficult to make a creative step.
*  So it's not absolute.
*  And this is also what's wrong, I think, with the Fristons model
*  because it doesn't express this.
*  It just takes a surprise or as a relative term rather than a normative absolute term.
*  He's right about that, but I don't think he's got the nuances right in this second part where
*  creativity is actually you're more creative if you're more constrained.
*  I think a theory that's that would be really mind blowing would be a theory that could actually
*  explain this paradox between creativity and constraint.
*  So, okay, backing out just a little bit, how do you think about constraint and creativity
*  when you're approaching a project that the Asimov is working on?
*  So we, again, we're curiosity driven.
*  So we started project because we're fascinated by a type of art or a type of question or
*  type of technology, neural network, like what can we do with this?
*  So one thing I always try to do is I try to take the creative process of an artist really seriously.
*  I'm not trying to impose my assumptions of what their creative process should look like or assume
*  that all creative processes of all artists are intrinsically the same.
*  They're just trying to be interesting.
*  No, they actually have their own process.
*  There's something that we also find with working with a diverse set of artists
*  that they all have this unique process of getting to where they want to be.
*  So we first have a couple of discussions about how does your process look like?
*  How do you get to new?
*  How do you make new stuff?
*  So do you reach out to them and say, hey, come talk to us?
*  We'd like to work with you.
*  Or how does that work?
*  Sorry to interrupt.
*  It's serendipity so far.
*  I mean, it's just people you meet, you sort of hear talked about.
*  And I mean, they have to be open to this.
*  So they typically have an interest in AI or interest in technology and are not scared of it.
*  And want to explore what the technology can do for them.
*  So that also makes our projects different every time.
*  Because it's like I said, so with the example of the fashion project,
*  we started out making a statement about the fashion industry and ended up creating a tool
*  for computational inspiration for fashion designer.
*  In the case of another project with, you referred to this, with a DJ called DJ Gecko
*  in the music industry, we wanted to explore a thing called style transfer,
*  which is normally used with images, how this could be applied to his music or how
*  we could create new music from it.
*  Oh, I see.
*  So just to make sure everyone's on the same page.
*  So when you say trial style transfer, it's when you take a portrait,
*  like a famous Van Gogh painting, painting, and you apply that, then you
*  enter in a picture of your cat, for instance.
*  And then what the GAN spits out essentially is a your cat,
*  but in the style of a Van Gogh painting.
*  So that's style transfer.
*  Yeah, yeah.
*  So it generates new samples, but the samples are biased in a certain direction.
*  And this direction is determined by the style that you input.
*  And in the visual domain, there's lots of examples of it,
*  but we didn't see too many in the audio domain.
*  So we're interested in the technology, but also in the application, in the arts,
*  and in this case, in music.
*  So what we ended up with was a style transfer.
*  So we more or less extracted the style from Gecko's music using this algorithm
*  and applied it to a number of different songs, like well-known songs.
*  To sort of gecko-fy the songs that he was interested about.
*  The end results were, again, you wouldn't put these things on an album,
*  or if you release them on Spotify, you don't get any hits.
*  But for him, they were very fascinating.
*  I didn't even understand what's so fascinating about it,
*  but he was like, oh, he had something to work with.
*  He saw something there.
*  Hmm.
*  He saw something there, yeah.
*  And so it inspired him, and he used this on his next album,
*  and there are sort of snippets of this in there,
*  but you could hear that it was inspired by the output of the AI.
*  We don't get to split-test our own lives,
*  but I wish you could do a controlled split-test
*  where you have one Gecko who did not observe his own material
*  being processed by an AI system and put out another album,
*  versus one that did, and then to see what the difference is,
*  because it's impossible to know.
*  We only get one take.
*  Yeah, we don't know.
*  I mean, what we can say is that, and this has always been the case,
*  that new technologies open up new doors for artists,
*  and I think this is, again, another technology.
*  Statistics, we use predictions, but very detailed.
*  Deep learning works very well with media,
*  and so it's a good fit with the artist scene
*  to use these tools as enablers for other kinds of content
*  that artists before our time didn't have access to.
*  I don't try to make big claims about the creativity of these systems
*  that's something new in that sense.
*  It's just interesting stuff to experiment with.
*  Yeah.
*  Well, Stefan, I want to open it up to somewhat more general questions here,
*  and some of these actually come from my Patreon supporters.
*  I kind of put it out there that I was going to be speaking with you,
*  and so I got a few questions lobbed at me from them, so we'll see.
*  Okay, good.
*  I want to know how studying creativity over time has altered or shaped
*  the way that you think about creativity.
*  How did you used to feel about it versus how you feel now?
*  Well, it depends on how far you go back.
*  When I was studying computer science, I was probably on the page that
*  creativity is just a random process, and it's like random deviations
*  from what you're actually meant to be doing.
*  Our job is to pick out which one worked well,
*  and that's sort of our job is random, and then we decide whether it would work.
*  Also in the art world, there's just a lot of people talking about art,
*  but there's not much behind it.
*  I was close-minded, you might say, about creativity and about the arts as well.
*  But over time, and I think it happened when I started to notice the boundaries of this mindset,
*  I started to respect the concept of creativity a lot more.
*  Not so much because it's so well-defined and useful, but like I said,
*  acknowledging that there's a whole world of understanding out there
*  that we don't have direct access to, but that's nonetheless valuable and inspiring.
*  Yeah, it's inspiring by itself.
*  In a sense, it sounds like it has actually increased a sense of mystery and awe in you,
*  which there's this weird paradox where people go into research, let's say,
*  to study a particular thing that is interesting to them, let's say consciousness.
*  Then you start studying the brain and you realize, oh God, we have a lot of problems,
*  we don't understand the brain.
*  Then you start studying the particular part of the brain, and then you get down and you
*  don't understand that, and you realize, oh my gosh, we don't understand any of this.
*  You end up studying this very particularly small thing, and the mystery of the big questions
*  kind of goes away as you see, you take layer by layer.
*  But what happens is you then all of a sudden have this new appreciation for all of these
*  different things that you feel like you understand better, quote unquote, but you really understand
*  but you realize that you didn't really understand in the first place.
*  You can see where are the limits of our understanding and what really do we understand
*  and don't we understand, and then it brings that sense of awe and mystery back.
*  Is that kind of what happened?
*  Exactly.
*  One of my ambitions has always been to be at the forefront of knowledge.
*  How do you get there?
*  Well, to get at the front, you need to have good mentors, work in interesting research
*  areas, but also work with interesting researchers.
*  Take your time getting to know the field and also dive deeply into some of their
*  thought processes because people have a reason for being a researcher and believing in their
*  ideas.
*  Even if you don't at first find someone's ideas that interesting, they have a reason
*  for finding it interesting.
*  So try to get into their mind, like what is it about this that's so interesting?
*  If you get into this mode of trying to understand the diverse views and what people are doing,
*  and then I think you get a better feel for the actual problems and the actual
*  discussion, scientific discussion that is going on.
*  Then you start pointing forward.
*  You start looking at the border of knowledge, more or less, and you can slowly prone into
*  the unknown.
*  This is my personal experience of it.
*  Right?
*  Yeah.
*  So there's this famous story of Wittgenstein who also had this transition, you might say,
*  more or less, it's very famous transition, right?
*  Between books.
*  Yeah.
*  Yeah, exactly.
*  So he famously gave a speech at the Biene Kruis, which were a society of, they call
*  themselves, I think, the logical positivists.
*  So they had this almost mathematical idea that from a given set of actions, from facts,
*  very Cartesian way of looking at things, from a particular set of facts, we can just build out
*  theories and have ultimately, if we just put in the effort, have a complete description about
*  everything in this world.
*  And then we sort of almost like a complete science of everything.
*  And Wittgenstein in his speech there, he famously said that they're sort of building
*  an island in an ocean.
*  So they're building out this island of knowledge.
*  And he said, and I'm paraphrasing here, but as much as I enjoy building this island,
*  I even more prefer just swimming in the ocean.
*  And I think this feeling of swimming, it's again, it's a very romantic idea of science
*  and also art, but this feeling of swimming, it's just very enjoyable.
*  And it also, it feeds you, it inspires you.
*  In science, there's a lot of hoops to jump through and a whole lot of stuff you just
*  have to do because you have to do it.
*  But even if it's just dipping your toe into the ocean now and then, I don't know, you
*  get back on the island, inspired again, and you get so many ideas out there.
*  And with the Osloff Institute and with working between art and science, I get to spend a lot
*  of time in the ocean.
*  Yeah.
*  See, but that's part of it.
*  Forging your own path, I think, is really good for that.
*  And when you get to a certain level in academia, you can start forging your own path a lot more.
*  You know, tenure, that would be that level, for instance.
*  But another way to do it is the path that you've taken, which I really admire.
*  I mean, obviously, I quit academia and have, you know, quote unquote, forging my own path here.
*  But I get to dip my toe in new waters every week, which is so wonderful.
*  And it's always rejuvenating to speak with people like you.
*  Yeah, yeah.
*  Thank you.
*  Yeah.
*  It's a sort of an ongoing adventure as well.
*  Because if you would ask me now, like, what would happen to the Osloff Institute?
*  What are our projects?
*  Are we going to do?
*  Where are we headed?
*  I have a very hard time answering that.
*  I have an intuition of where I'd like to go and what's happening right now.
*  But it's hard to plan these things because they're out there in the ocean.
*  So I don't know how to get there.
*  I don't know how to pull it in.
*  Yeah, I go swimming.
*  All right.
*  So here's a question from a Patreon supporter.
*  So I'm paraphrasing here, but they're wondering about the difference between symbolic AI and
*  connectionism AI with respect to creativity.
*  Is there a role for symbol like computation in creativity?
*  Or is it all distributed neural network computation?
*  Do you have a take on this?
*  Well, the difficult marriage between symbolism and connectionism, I mean, it's an older story.
*  I think that's important to recognize.
*  So this is played in the 90s, pretty big.
*  So the symbol grounding problem is a paper by Harnov.
*  He describes it pretty well.
*  They were dealing with these problems and a lot came out of that.
*  So that's also important to recognize.
*  So even though you don't solve this, you still get a lot of interesting theories and open
*  research questions about it.
*  We're right now entering a time where we're dealing with the same types of questions again.
*  And it has to do with some of the shortcomings of the connectionist paradigm.
*  So in the last decade, it was all connectionist.
*  There was no almost no room for symbolic approaches to AI because connectionism just
*  scales very well with data.
*  And as soon as you start meddling with it or you have like a
*  symbolic, the symbolic approach requires more design.
*  Connectionism sort of grows by itself.
*  It's pure machine learning.
*  So it scales much better.
*  But in this scaling that we now have, the complexity of the models that we have is
*  grown so large that we have a very hard time taming them again.
*  And this is the reason why we're talking about ethics so much or we should have regulations on
*  Google and Facebook.
*  There's also a privacy component, but there's also a we don't know what's in those models.
*  We don't know how did we use.
*  We don't know what will happen with self-driving cars if they're completely machine learned on
*  based on data says what like what decisions will they make.
*  So I think in science right now you see a revisiting of this
*  symbol grounding problem.
*  But a major difference is I think is that it's reversed.
*  So what we're coming from in the 90s is a symbolic AI where the connectionist
*  models needed to connect with the symbols.
*  And right now we're dealing with a AI that is dominated by a connectionist approach
*  where we need to express symbolic AI in connectionist terms.
*  If you know me so the burden of the work is on the symbol is back to the symbol.
*  To actually show that they can be represented in connectionist models because
*  not expressing them like this idea of connecting a symbolism symbol AI with connectionist AI.
*  I think it's too simple.
*  It's actually about getting the logic of a symbolic AI and expressing it in a neural
*  network architecture.
*  That's the next challenge for science.
*  This is somewhat related here.
*  Related to creativity then in symbolic processing versus distributed connectionist processing.
*  You're familiar with the frame problem in AI.
*  So someone was asking about how...
*  I'll state the frame problem essentially.
*  How does a cognitive operation that's happening know which parts of representations to operate on
*  and which not to operate on?
*  This goes back to the constraint.
*  How do I know when to stop?
*  What should I not be operating on versus what's relevant for me to be operating on?
*  When am I done?
*  So that's kind of the frame problem.
*  To bring in creativity and analogical reasoning.
*  Analogical reasoning is the idea of taking information from one domain and applying it
*  to another.
*  Roughly this is kind of like combinatorial style of creativity.
*  If you take reasoning from one domain and applying it to another.
*  I guess the question is how does creativity deal with the frame problem?
*  Well the question I think is about...
*  So the frame problem is a problem that starts with a computational approach to intelligence.
*  And then you're looking for creativity to sort of mend the problem.
*  But I think the mending doesn't need to happen after the fact.
*  It needs to be before.
*  So if you start out on the wrong foot in this case.
*  You get the frame problem.
*  You have a very hard time mending it.
*  And I agree with you that the frame problem is just an expression of a whole set of problems
*  including the symbol grounding problem.
*  Which have the same basis.
*  Namely that the computer doesn't understand anything.
*  And we do.
*  And so we can try to have a human in a loop and steer at some level.
*  Or we can try to design as well as we can and make sure that the computer doesn't run
*  into the frame problem.
*  But I think to answer your question how creativity will solve the frame problem.
*  Is once we have a better understanding what a creative architecture looks like.
*  It won't run into the frame problem.
*  Because the frame problem is the absence of creativity.
*  All right.
*  I get a lot of questions from listeners about how to proceed.
*  What to go into.
*  How to start on their career path.
*  If you had one piece of advice.
*  Not that you just have one.
*  But if one springs to mind what would that advice be?
*  If I could give one advice it would be to take yourself seriously.
*  And what I mean by that is actually a couple of things.
*  So it's first off choosing your mentors wisely.
*  I think another part is getting to know yourself.
*  So and that's it's a way to be authentic.
*  And that's also important in science.
*  Because if you just you know go with the latest trends then you'll never be in front of it.
*  It's you're always walking alongside with everybody else.
*  So in order to cut out your own path you really need to know yourself.
*  And because that allows you to decide what your path is.
*  The final aspect of this taking yourself seriously also has to do with AI.
*  And I think it has to do with the acknowledgement that what you feel.
*  Free will.
*  Autonomy or your creativity.
*  Or the idea that you have feelings and consciousness.
*  If you feel those things then don't let anybody tell you that you don't.
*  Or don't let anybody tell you that they have a theory that explains away feelings or consciousness.
*  That shows that it's just an illusion or a simulation running in your brain.
*  If somebody tells you that you need to explain them.
*  Just because their theory doesn't explain those things.
*  It doesn't mean that those things are real.
*  It just means that that theory is inadequate.
*  So and I think that's very important.
*  Because I keep hearing comparisons even by politicians nowadays of people being like computers.
*  Like being mindless drones more or less.
*  And people having consciousness and feelings that's just an illusion.
*  Even worse maybe free will and autonomy just being illusions.
*  And I think that's a very dangerous track to be on.
*  So that's not true.
*  Anybody who tells you that doesn't have a good theory of it is trying to explain it away.
*  We do have free will and autonomy.
*  We just have to figure out what it's like and how it works.
*  And then we can acknowledge it.
*  I love it.
*  So to wrap up.
*  To sum up your advice.
*  You go knock on a famous scientist's door.
*  And when they open it you say, hey man, your stuff is just a theory.
*  And then you close the door again.
*  And so begins the next journey in your life.
*  Yes.
*  Yes.
*  That's great Stefan.
*  I love it.
*  What is something that you used to believe that you now look back on and think, oh that was naive?
*  So many.
*  The most sort of in your face one or at least for me was that I used to believe that you could
*  use a computer to create a mind.
*  And I no longer believe that.
*  It's a fundamental belief that you believe we have to get out of the computational constraints of computers.
*  Absolutely.
*  If we know exactly, let's say how a human body including his brain is built like atom by atom.
*  And then if we make a simulation in a computer of this and we simulate all the physics that's
*  around it, etc.
*  This argument.
*  Then you'd have a artificial intelligence.
*  That used to be the way I thought.
*  You don't understand anything about it, but you have it.
*  You create it.
*  Right.
*  I no longer believe that because I think what you have is a very accurate description of
*  what a human is and what an intelligent is.
*  But that's not the same thing.
*  I can do that on paper.
*  Like I could draw it on paper.
*  It doesn't make the paper itself intelligent.
*  It's just a description.
*  So we need to move beyond computers.
*  Man, that's a great way to end it.
*  You can learn more about Stefan on Twitter at Stefan Linjen or what he actually recommends
*  is that you might want to follow at Asimov Institute to learn more and keep up about
*  all that good stuff.
*  Thank you so much for taking the time and good luck with all your endeavors.
*  You're welcome.
*  Thank you very much.
*  Thank you for the nice talk.
*  Brain Inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to BrainInspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show
*  and prohibit any annoying advertisements like you hear on other shows.
*  To get in touch with me, email Paul at BrainInspired.co.
*  The music you hear is by The New Year.
*  Find them at TheNewYear.net.
*  Thanks for your support.
*  See you next time.
