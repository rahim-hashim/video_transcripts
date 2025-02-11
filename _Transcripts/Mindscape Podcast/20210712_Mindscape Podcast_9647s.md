---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 9647s
Video Keywords: ['computation', 'physics']
Video Views: 95597
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/07/12/155-stephen-wolfram-on-computation-hypergraphs-and-fundamental-physics/

It’s not easy, figuring out the fundamental laws of physics. It’s even harder when your chosen methodology is to essentially start from scratch, positing a simple underlying system and a simple set of rules for it, and hope that everything we know about the world somehow pops out. That’s the project being undertaken by Stephen Wolfram and his collaborators, who are working with a kind of discrete system called “hypergraphs.” We talk about what the basic ideas are, why one would choose this particular angle of attack on fundamental physics, and how ideas like quantum mechanics and general relativity might emerge from this simple framework.

Stephen Wolfram received his Ph.D. in physics from Caltech. He is the founder and CEO of Wolfram Research, and the creator of Mathematica, Wolfram|Alpha, and the Wolfram Language. Among his awards are a MacArthur Fellowship. Among his books is A New Kind of Science. He recently launched the Wolfram Physics Project.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

#podcast #ideas #science #philosophy #culture
---

# Mindscape 155 | Stephen Wolfram on Computation, Hypergraphs, and Fundamental Physics
**Mindscape Podcast:** [July 12, 2021](https://www.youtube.com/watch?v=0bMYtEKjHs0)
*  Hello everybody and welcome to the Mindscape Podcast.
*  I'm your host Sean Carroll and this is going to be one of those podcast episodes that people
*  have been clamoring for for a long time.
*  I get a lot of suggestions and a lot of people suggest the same guest over and over again.
*  Sometimes I ignore the people.
*  You know, I love the people but I don't always agree with them.
*  Other times I think, you know what, the people are right and in this case I think that they
*  are.
*  So I invited Stephen Wolfram to be on the podcast.
*  Now Stephen Wolfram was a physics prodigy at a young age, one of the youngest winners
*  of the MacArthur Genius Grant.
*  Started out in particle physics before he moved to think about complexity and cellular
*  automata.
*  Maybe best known right now for inventing the Mathematica programming language and analysis
*  system as well as the underlying Wolfram language that was used to write it and Wolfram
*  Alpha answer engine.
*  I use Mathematica all the time.
*  Many people in my field use Mathematica but he's also still interested in fundamental
*  physics.
*  A few years ago, some years ago, he wrote a big book called A New Kind of Science where
*  he suggested that cellular automata might give a clue as to different ways of thinking
*  about all sorts of science, right?
*  Biology, economics as well as physics.
*  More recently he has launched what is called the Wolfram Physics Project which is simply
*  an effort to start with almost nothing and get the fundamental laws of physics out of
*  them.
*  Now there's a lot to say about this and we don't say everything in this podcast even
*  though it's a long one.
*  I wanted to focus the podcast on giving a sketch for what the main ideas are of the
*  Wolfram Physics Project and how they are not yet fully developed but might be developed
*  going down the line.
*  There were a lot of criticisms and some kudos about how he developed it sort of outside
*  the mainstream of physics research and so forth and then laid on us hundreds of pages
*  of work with he and his collaborators at the same time.
*  It's not the mainstream of theoretical physics.
*  Most physicists who are doing their own thing did not drop everything to work on it but
*  some became interested and they're inviting people to help out.
*  You'll learn a lot in this podcast not about how the research was done or the fact that
*  it was uploaded and shared with the world or whatever.
*  You can draw your own conclusions about that.
*  I care about the substance of the actual ideas and mostly I'm giving Stephen here the opportunity
*  to explain those ideas but there is a family resemblance between what he's trying to do
*  and what I and my collaborators are trying to do in quantum mechanics, stuff like that.
*  So let me very briefly tell you how I see that relationship.
*  What we're trying to do is to start with the simplest, most stripped down version of the
*  best theory we currently understand, namely quantum mechanics, right?
*  To start from almost nothing but quantum mechanics and see how things like space and time and
*  matter and energy emerge from that fundamental description.
*  Stephen Wolfram and his friends are trying to be way more ambitious than that.
*  They're starting with a kind of automata, a kind of discrete system called a hypergraph
*  and generalizations thereof.
*  And basically you have a guess as to what the rules are for how hypergraphs are updated
*  and the point that they're trying to make is that some guesses lead to things that kind
*  of look like the real world.
*  So the hope is that eventually we find specific guesses for what those update rules could
*  be that actually get us the specific real world or very, very close to it.
*  My own attitude is, you know, good luck to them.
*  I'm very much in favor of lots of different approaches to fundamental physics.
*  This is one of them.
*  Great.
*  Let a thousand flowers bloom, et cetera.
*  I actually think that our, my and my collaborators' approach is more promising because it leans
*  heavily on something we already understand quite well, which is quantum mechanics.
*  As I see it, if the Wolfram Physics Project works, they're first going to have to find
*  quantum mechanics in exactly the right way and then find all the features that we have
*  about the real world.
*  So it's kind of a precursor to what I'm trying to do, et cetera.
*  But you know, I might be wrong about that.
*  It could be that this particular way of doing things leads to not just quantum mechanics,
*  but a specific implementation of quantum mechanics that gives us other clues to understand the
*  nature of space and time, et cetera.
*  So as I said, what we're trying to do here in this podcast is help you, the listener,
*  what the ideas are and where they're going.
*  Hopefully we succeed in that.
*  Let me very briefly take an opportunity to, as I occasionally do, remind you that we have
*  resources for the Mindscape podcast.
*  We have a web page, preposterousuniverse.com slash podcast.
*  So every episode has, you know, links to stuff about the authors and other resources and
*  also full transcripts of the complete episode.
*  So you can search every Mindscape episode for the last three years.
*  We're hitting our three year anniversary, roughly speaking.
*  And also we have a Patreon.
*  If you would like to support Mindscape, you can go to patreon.com slash Sean M. Carroll,
*  donate a dollar or two or whatever your local currency is per episode.
*  And you get ad free versions of the podcast, as well as the ability to ask questions in
*  our monthly Ask Me Anything episodes.
*  Mostly it's about gratitude.
*  I'm very happy, very pleased that so many people enjoy Mindscape very much and therefore
*  choose to donate just a little bit.
*  It's the thought that really does count in this case.
*  So with all that, let's go.
*  Stephen Wolf from Welcome to the Mindscape podcast.
*  Hello.
*  So it's been a little over a year, I guess, since you announced your physics project.
*  And I think I finally by no means have become an expert, but at least I know enough about
*  it to ask a whole bunch of ignorant questions to help us all understand it a little bit
*  better. Maybe to start off, is this do you consider this current project to be a
*  continuation of the cellular automata type of stuff you did in your book, A New Kind of
*  Science? Or is it a new branch somehow?
*  Yeah, so I mean, it builds on basically a tower of ideas, technology, intuition and so
*  on that actually I'm sort of amazed we've managed to get to the point we've managed to
*  get to. But all those previous pieces seem to be necessary to get to where we are.
*  And for example, you know, I've studied a lot in New Kind of Science 20 years ago.
*  I studied a lot of cellular automata, which are these very simple programs with, you
*  know, arrays of black and white squares and so on.
*  And from studying those things, I developed both a bunch of intuition about how sort of
*  things work in the computational universe.
*  And I managed to figure out some fairly general principles, which we've been able to get
*  more and more evidence for, which are necessary to kind of launch into figuring out things
*  about physics. Now, when I wrote New Kind of Science, you know, it has 12 chapters.
*  And one of those chapters was called Fundamental Physics, and it had two sections.
*  One was about thermodynamics and one was about kind of the fundamental underlying theory
*  of physics. And for me, at the time, I viewed it as being an incomplete potential
*  application of the general kinds of ideas that I was developing in New Kind of Science.
*  And I had a bunch of specific ideas about thinking about space as a network, thinking
*  about the way time would operate and so on.
*  I was very pleased with the fact that I had managed to get a fair distance in deriving
*  general relativity from that kind of theory of gravity, from that kind of approach.
*  I was not satisfied with where I had got with quantum mechanics and that project.
*  So now restarting that project nearly 20 years later with energetic young physicists
*  and so on. And one kind of initially rather technical new idea that kind of made the
*  model just seem much cleaner to me.
*  It was kind of it's been a new development.
*  And really now I've seen a lot of things that I say to myself, I should have been able to
*  figure that out 25 years ago.
*  Well, that's that. That does not distinguish you from anyone else working on science, right?
*  Yeah, you always look back with that.
*  No, I think I think what's what's so I view it as being what's really neat is that the
*  formalism that we've now got is something which was sort of there were precursors of it in
*  new kind of science. But the full sort of story of it is just emerging now.
*  And it's really neat because it really it gives one sort of a to me, that's sort of this
*  way of understanding things in terms of how simple programs behave, developed a bunch of
*  intuition and new kind of science.
*  Now there's a whole nother level of intuition and results that we're getting that provide
*  in the sort of formalism for this project.
*  And that's so it's it's both applicable to fundamental physics and to a bunch of other
*  things. And I'm pretty excited about that.
*  So let's imagine that first, I'm sure this is not true.
*  But let's imagine that there's going to be a listener who only listens to the first few
*  minutes of this podcast.
*  And we want to let them have a takeaway for what is going on here.
*  I mean, is it accurate?
*  My vague impression to say that the cellular automata had a grid, right?
*  Like you had some checkerboard or something like that and some rules for updating them and
*  some discrete model, which you're going to hope that if you squint and look at very far
*  away, it looks like physics.
*  Whereas here you still have a discrete set of models, but you're not starting with a
*  fixed grid. You're kind of building things up by rules as you go.
*  Right. Yeah, that's right.
*  I mean, I never thought that that cellular automata would be relevant to fundamental
*  physics. I mean, other people were sort of saying cellular automata are going to solve
*  fundamental physics. And I was like, no, please don't say that.
*  That's just not going to work.
*  And cellular automata are very minimal models.
*  Once you have a fixed notion of space and time and they've been extremely fertile models
*  for huge numbers of different kinds of things from road traffic flow to chemical
*  catalysis to leaf growth, all kinds of different things.
*  But they assume a preexisting notion of space and time.
*  And so in thinking about physics, I had realized ages ago that we really need to go
*  underneath the notions of space and time that we're familiar with and see how to build
*  those up from something more fundamental.
*  And so sort of the real starting point of our project is to think about just these
*  that just space is made of something that's not that has not been sort of in the
*  tradition of physics and the traditional mathematics as well.
*  That's not really been a thing that people think about.
*  Space just is is is something in which things are placed at certain positions and so
*  on. And so, you know, in this it's kind of like what people might have thought about a
*  fluid like water.
*  It's just water. It's just flows.
*  It does all these kinds of things.
*  But, you know, 150 years ago, we found out, no, those Greeks were actually right.
*  Some of those Greeks were right.
*  It's made of discrete molecules bouncing around.
*  And with space, we haven't yet sort of made that definitive leap.
*  And one of the sort of starting points of this project is to think space is made of
*  something. What's it made of?
*  It's just made of these disembodied discrete points.
*  And each point is just an abstract element.
*  It doesn't it doesn't have a position.
*  There's nothing. It's just this element.
*  And then what we say is what all we know about those elements is how they're related to
*  other elements, how they're effectively connected to other elements.
*  So it's like you think about all these points in space, all they have is a friend network,
*  so to speak. They don't know where they are.
*  They just know who their friends are, so to speak.
*  And so the first big sort of realization is from something as unstructured as that,
*  by looking at that on a large enough scale, it's kind of like how continuous fluids emerge
*  from lots of discrete molecules underneath bouncing around.
*  There's a there's a notion of a kind of continuous like space that can emerge when you
*  look at that on a large scale.
*  And that's that's kind of the that's that's one starting point.
*  I mean, another important thing to realize is that in our setup, the only thing in the
*  universe is space.
*  And there's no you know, we're not saying space is a background and there are things
*  placed in space.
*  We're saying everything in the universe is just kind of made of space.
*  So what I have in mind is a bunch of dots, right?
*  Nodes that are connected by lines to form some kind of graph.
*  And do I imagine that the line that the dots rather the nodes, are they labeled?
*  Do they come? Are there different kinds of dots or is there just an er dotness that they
*  all share?
*  It's an er dot.
*  OK, that's just all identical.
*  The only thing the only thing about them is they are two dots are either identical or
*  they're not identical.
*  That is, there's a there's a particular dot or there's another dot.
*  And so the only the only thing about them is is kind of their their you know, their
*  identity, so to speak.
*  They don't have they don't have colors.
*  They don't have they don't have positions.
*  They just know I'm this dot and not that other dot.
*  Right. So there's some dots and there's some lines.
*  They make a graph or a hyper graph, I guess.
*  And there's a rule.
*  There is a rule for updating to go from one collection of dots and lines to the next one.
*  And then we just iterate that forever, I suppose.
*  That's right.
*  And the whole universe comes out of that.
*  That's very nice.
*  That that's the idea.
*  So, I mean, you know, there are many pieces to that setup.
*  For example, one thing is all there is is these kind of atoms of space and connections.
*  There's nothing in space.
*  There's nothing. It's not like you then say we've got space.
*  Now let's put a an electron in space.
*  If you want an electron, you have to make it out of space, so to speak.
*  You have to make it from features of that pattern of connections between the atoms of space.
*  So that's kind of the that's that's sort of the the base story of what what is the data structure of the universe?
*  What is the universe sort of made of?
*  And that's the idea.
*  It's made of these discrete elements and relations between those elements, which we can think of as being kind of lines joining them.
*  It's actually convenient.
*  And this was the sort of technical innovation of a couple of years ago to realize that the best way to think about this is in terms of a so-called hyper graph,
*  where we just have elements and relations in a graph.
*  You have you have nodes and you have edges connecting those nodes and each edge connects to nodes in a hyper graph.
*  You can have any number of nodes involved in a hyper edge.
*  And that sounds like it is really a technical detail, but it makes the whole model much, much easier to deal with.
*  Or at least I thought it made it much easier to deal with.
*  In the end, it doesn't make much of a difference.
*  And I could have figured this out 25 years ago.
*  But that's the way these things work.
*  It seemed to make it easier technically to make forward progress.
*  I think you were then talking about sort of what do these atoms of space do?
*  And you're describing kind of the rules that they use to get updated.
*  And yeah, you're right.
*  I mean, the basic idea is you look at the local structure of this graph and you say whenever the local structure of this graph looks like this particular pattern,
*  then it should be updated to be a local piece of graph that looks different.
*  Right. And that's the whole story.
*  Some things are just better at home.
*  You can pause the movie whenever you want.
*  You can have two desserts and no one will judge you.
*  And exercise is one of those things.
*  Peloton delivers a workout experience that you'd never imagine was possible right in your own home.
*  One of the things I especially like about Peloton is the variety of classes driven by different kinds of instructors.
*  If you're the kind of person who needs to be encouraged by your instructor, Robin Arzon is especially good at that.
*  Whereas if you just want to get down to business and get the workout in, Adrian Williams might be the instructor for you.
*  Whatever your mood or overall fitness goal, you can mix and match classes for a total body workout experience.
*  Choose from cardio, strength, yoga, Pilates, outdoor runs, meditation and more.
*  With the Peloton bike, there's nothing like working out from home.
*  Learn more at OnePeloton.com.
*  New members can try Peloton classes free for 30 days at OnePeloton.com slash app.
*  Terms apply.
*  That's O-N-E-P-E-L-O-T-O-N dot com.
*  I like the fact that you just use the word hypergraph because I like to share the jargon with the audience so they can go look it up.
*  Because especially, I mean, I should note, you, I don't want to talk too much about like style and procedure here because there's far too much physics to talk about.
*  But you did announce this project with a website and a call to participate, right?
*  If people want to dig into the details, what is the URL they should be going to?
*  Wolframphysics.org.
*  There you go. And people can find out what the details are and do their own calculations.
*  So that's that's it.
*  Yeah, I mean, the other thing we've done kind of in terms of the public, which has been really a big success, is we've we've live streamed a lot of our internal working meetings.
*  And we've, you know, all the notes from this project are all, you know, posted on the web basically the day after they're made typically.
*  And that's and it's been really interesting because a lot of people who are a lot of professional physicists have gotten involved, but also a lot of people who are, for example, involved in computer kinds of things and understand sometimes more of some of our jargon than the physicists would understand, have also gotten involved.
*  And it's it's really been an interesting process to sort of do science live and in public, so to speak.
*  It's, you know, and I the it's like it, it's a good kind of generator of reality, because, you know, we say some things that are right, we say some things that are wrong, it kind of a a place where you can get to see kind of the process really happen.
*  And there is something that is very different about what you're trying to do in terms of fundamental physics, I would I would argue and then correct me if I'm wrong.
*  Usually, not always, but usually physicists work from the phenomena to try to come up with an explanation, right? Like there are stars in the sky, there are planets moving in certain orbits, what can we do about that? There's an apple falling from a tree.
*  But in some sense, you're just saying, well, here's the simplest possible thing that physics could be. Let's just see if we can guess the right one. Is that more or less accurate?
*  I mean, it is closer to that than the reverse engineering approach. And in fact, when I see people try to sort of understand what we're doing, and sort of say, well, what about doing this and that and the other, the great tendency is to try to reverse engineer.
*  And this was a thing that that I kind of, you know, I, as you know, I used to do sort of mainstream standard physics back in the late 1970s, early 1980s.
*  And, you know, that was what one did in those days. And the thing that was really for me very liberating was when I started studying, well, I got interested in how did complex phenomena occur in the natural world.
*  And the question was, what are the right models to study that? And my initial thought was, let's use all the fancy stuff from physics, all those differential equations and all these kinds of things. I tried doing that total failure.
*  So I said, let's step back and see, you know, is there an alternative approach to modeling that we can use? And I had the very fortunate experience that I had been working as a practical matter on building my first computer language.
*  So forerunner of mathematical morphology language. This is back in 1979, 1980. And what one does when one builds a computer language is one saying, let's take all these computations people might want to do.
*  And let's in a kind of natural science type way, drill down and try and find out what are the primitives from which we can build up all these computations? What are the kind of atoms of computation?
*  And then build up from there. And the thing that's really interesting about that process is you're just making up these atoms of computation. It's not like, you know, it's not really the same kind of, oh, we've also we've got to make sure we get, you know, Einstein's equations here. We've got to do this and this.
*  You're just making it up and you're hoping that it will be in that case useful to people. And so that experience got me into this idea of just figure out the most minimal model and see what it does.
*  And that's what I did with cellular automata. And it worked great in that case. So in a sense with physics, what I was trying to do with this project is find the most structuralist model of structure in the universe.
*  Because that was and and it is not it is by no means self evident that that will work. I mean, that's sort of the ultimate Occam's razor type idea is, you know, just make it, you know, absolutely minimal.
*  Now the thing that's really neat, and maybe we'll talk about this a bunch later, is that now that we have this foundation, we can start to see how a lot of ideas that people have had in mathematical physics.
*  Over the last many decades actually plug into this idea and both inform it and help make those other ideas more more founded and it's it's I think
*  So, so this this notion, which basically, you know, this idea of find the simplest primitives and then see what they do.
*  This is what I get for having spent 40 years being a computational language designer. This is what that's what that's what that involves. And it's different from what people do traditionally in sort of reductionistic science where you say start from the phenomena and then say, how do I get this phenomenon?
*  Right. And I do want to get somewhat different methodology.
*  I do want to definitely get to how we recover all of known physics or at least, you know, move in the direction of recovering all of known physics. But there also seems to be like a couple of deep principles.
*  That you have in mind when you're working on this stuff that maybe it's worth sharing. I mean, one of them is this idea of computational equivalence. Right. I could try to gloss it. But why don't you tell the audience what that means?
*  Yeah, yeah, right. So, you know, you set up some simple program, you run it, you see what it does. You might think if it's a simple program, it will always do simple things.
*  That turns out to not be true. That's sort of the big thing that I discovered in the early 1980s that for several years, I kind of resisted that conclusion and eventually realized that is really the way things are.
*  When you look in the sort of computational universe of possible programs, if you just sort of pick a program at random, even though the program may be very simple, its behavior may be very complicated.
*  Programs that we typically build as humans for some particular known purpose will tend to not have that feature because we want to have them achieve the particular purpose we want them to achieve.
*  Which is one, some purpose that we can describe. And so you avoid this thing that the simple programs producing complicated behavior. That idea of simple programs producing complicated behavior, I think, is sort of the essence of the secret that nature uses to make complicated stuff.
*  And that's why, you know, we look around in nature, we see all this complicated stuff, we say, how could it possibly make all this complicated stuff? That's just the formal fact about what happens in the universe of possible programs.
*  So first thing is the realization simple program doesn't necessarily have to have simple behavior. And then the next question is, okay, so you see this very complicated behavior, how do you characterize it? You could just say, oh, it's very complicated.
*  And in fact, a lot of the people had seen these phenomena for centuries, actually, of fairly simple setups like the digits of pi.
*  Specifying them is quite easy, yet once you've generated the digits, they seem completely random. And people would typically say, oh, it's very complicated. There's not much we can say about that.
*  And they would try to find, you know, like the distribution of prime numbers or something that worked for a long time to try and figure out what regularity can we tease out of this thing that seems quite random.
*  And so what I was interested in was trying to understand how do we characterize this complexity that gets generated. And so the thing that I realized is the way you can think about what's happening is any process of generating some pattern, for example, you can think of as a computation.
*  And then the question is, how sophisticated is that computation? So for example, it might be that computation is just like adding numbers together. It's something very simple. Or that computation is something more sophisticated. And the question is, can you kind of, can you rate the sort of sophistication of computations?
*  And so the big discovery of the 1930s and so on was that you might have thought every different kind of computation you want to do, you'd need a different machine to do it. But then with Turing machines and combinators and a bunch of other ideas, this notion of universal computation arose that says you can just have one piece of hardware and just feed it different programs and it can do different things.
*  And that's been a pretty centrally important idea in the technology of the last 15 years. That's the origin of software, the development of the computer revolution. But for science, the implication there is, well, perhaps these simple programs might actually be, for example, computation universal. They might be able to do essentially any computation you want.
*  So this principle of computational equivalence of mine is basically the idea that when you pick a program, if the program doesn't do something obviously simple, it will be doing a computation that is as sophisticated as the computations that anything can do.
*  So in other words, what that's saying is you might think you start off with an incredibly trivial program and only does trivial computations. As you make the program a little bit more complicated, it would gradually do more and more sophisticated computations. And as you make a really, really, really complicated program, it would do really, really complicated computations.
*  But the somewhat surprising claim of the principle of computational equivalence is that that's not true. Once you get above some very low threshold, you're immediately at the max. You're immediately doing computations that are as sophisticated as anything. And that principle has many implications. And probably the most important immediately for physics is this phenomenon I call computational irreducibility.
*  That's the next one. So go ahead and say that.
*  Right. So I mean, the question there is if you're running a program, can you tell what it will do? One way you can tell what it will do is you just run every step just like the program would run itself. But another thing you can do is say, I'm much smarter than that program. I can jump ahead and it's going to run for a million steps, but I can just jump to the end and say the answer is going to be 42 or something.
*  And so one of the ideas of sort of the exact sciences, the mathematical sciences for a long time has been sort of a sign of doing wonderful things is that you can jump ahead like that. You can readily predict where will the planets be at some time in the future and so on.
*  But so that's what I call computational reducibility, the ability to reduce the computational effort necessary to find the answer to jump ahead. So the claim is actually there are lots of systems that are computationally irreducible in the sense the only way to find out what they'll do is just to run every step or in effect just to observe what the system does.
*  And the reason that happens is because the principle of computational equivalence, because if you think you're the observer, you're the predictor, you are a computational system as well. And the question is, how do you as a computational system compete with the system you're trying to predict?
*  So if it was the case that you could really be smarter than the system you're trying to predict, then yes, you could potentially jump ahead. But what the principle of computational equivalent says is no, actually, that won't be that way. You will be exactly computationally equivalent to the system you're trying to predict.
*  And so the system you're trying to predict, its behavior will seem to you sort of irreducibly complicated. So that's one of its implications.
*  So in some sense, this is saying, you know, both of these principles, the equivalence and the irreducibility, there are computers, as we've known since touring, that are universal computers, they can calculate any function you want to calculate. And what you're saying is in the space of all computers, computations, computations with that capacity are generic in some sense, they're all over the place, they're much easier to find than you might have thought. And there's no way to simplify the typical one into something that you can just leap ahead.
*  Right. I mean, the principle of computational equivalence, one of its predictions, in effect, is that universal computation will be ubiquitous. It actually goes considerably further than that because at a technical level, one of the things that one talks about in universal computation is it is possible to program this system to do whatever computation you want.
*  It's a little bit of a different statement to say, if you are presented with this system, and it is fed, even this very simple program, then it will already do something complicated. So it's a couple of additional steps.
*  But one of the key predictions is computational universality is ubiquitous. And that has many implications. I mean, it has implications in terms of the practicalities of building computers, it has implications in terms of what aspects of physics we can expect to understand, it has implications at a more philosophical level about things like free will and so on, which maybe we'll talk about.
*  Well, and one of the implications is that if we buy into the philosophy of it, it gives us some optimism for this program of starting programming the human sense, not the computer sense, for this project of starting with some very, very simple rules and getting the actual universe out. Right? If all sufficiently complicated computations are at the same level of ability in some sense.
*  Yes, that's true. I mean, one of the things that is sort of a key, I would, you could even say prediction statement of our physics project is what can be done in our universe is just computation and not hyper computation. That is, it's the kind of computation that can be done by a Turing machine.
*  It's not the kind of computation that can be done by a thing that is infinitely more powerful than a Turing machine that you can conceptually imagine, but you can't, you know, the claim is no such thing exists in our universe.
*  And in fact, you can get a bit more technical about it. And the claim of these models is even if it exists, it will be hidden behind the cosmological event horizon from us. We will never be able to observe it.
*  So it's kind of like, well, you can say it exists or you can say it doesn't exist, doesn't really matter, because we'll never be able to interact with it.
*  But so, you know, that's one of the key statements. Yes. And the idea that it's sufficient to have something that is a computational system that we humans can kind of understand how it's constructed, like a Turing machine or like one of these hypergraph rewriting systems, that is a, you know, that's a supposition of this project.
*  And it's a supposition that in a sense is sort of encouraging for us humans that it might be the case that there's something we can kind of hold in our hands that represents everything the universe does, even if the implications of that thing we can hold in our hand are irreducibly complex.
*  And even if we couldn't tell, you know, given that you give us the rules for the universe, if you say, can I make a warp drive? The answer might be, it's really hard to tell.
*  It's an irreducibly complicated thing. It's like, you know, recapitulating the whole history of mathematics and so on to get to the point, you know, can we prove this theorem that there is or isn't a warp drive?
*  So it's, but to me, that's, yes, that's the concept.
*  I'll take all the reasons for optimism I can get. I'm all on board with that. So good. So with those in mind, I mean, let's go back to the physics that you're actually constructing here. We have a hypergraph. We have some rules for updating it.
*  Now, should I read the specific, is it is the idea that there is a specific correct rule for our universe and that rule basically is the fundamental laws of physics?
*  Okay, so this this is where things get a little bit more complicated.
*  Yeah.
*  So I think that it is probably the case that there will be a rule that we'll be able to hold up and say, with this rule, we can reproduce what we observe in physics.
*  Now, footnote, which is really interesting footnote, I think you might say, why did we get this rule and not another rule?
*  You know, it seems very particularly if the rule is simple, that's like, you know, Copernicus was wrong, so to speak.
*  You know, there isn't nothing special about us. We got the simple universe, so to speak, or we got the universe with a simple rule, not the universe with the to us incredibly complicated seeming rule.
*  The thing that is then very surprising is that, and this is, you know, probably have to go a few more steps before we can really, really dig into this properly, is the idea that actually you can think of the universe as running all possible rules.
*  And we as observers of the universe are essentially exist in a particular, in a sense, reference frame in a particular position in rule, real space, as we call it, that essentially gives us a particular sampling of this sort of universal possible universes.
*  And that particular sampling is given our way of parsing what happens in the universe, that is something that we could attribute to a particular underlying rule, but actually we can also think of it as just a slice of this kind of universal possible universes.
*  So it's a little bit more, but I think, you know, operationally, I would hope that we will be able to produce a rule that will have the property that if we work out all its consequences, and we cannot, because remember, one of the very tricky things is we as observers of the universe are embedded in this universe.
*  And so as you change that underlying rule, you not only change the rule for the universe, you also change the rule for us.
*  And so that those two effects in some very, very vague sense cancel each other out so that there is a large class of rules for the universe and rules for us, which all seem the same and which all have the same laws of physics effectively.
*  So to give an analogy, to make this a little bit less bizarre, let's go back to fluid dynamics, for example.
*  And we have laws of fluid dynamics, the Navier-Stokes equations, all these kinds of things, and you might say, how do we derive these? Underneath there are a bunch of molecules bouncing around.
*  Well, there can be water molecules, which have their particular H2O form. There can be air molecules, N2 or whatever it is.
*  These different kinds of molecules bouncing around, all of their physics are quite different. All the details of what happens when those molecules collide are quite different.
*  Yet on a large scale, the laws of fluid dynamics are the same for air and for water. They have some different parameters, but they're basically the same laws.
*  And it's the same kind of thing that I think happens in the derivation of laws of physics. That is, certain aspects of the laws of physics are quite generic.
*  I think general relativity and quantum mechanics are quite generic. And they are things which, if you are an observer, even vaguely like us, they are inevitable that you will observe.
*  And if you want to home in on, well, do we have the fine structure constant with a particular value it has, you probably have to home in on more features of us as observers.
*  Right. I mean, do you think that, do you anticipate that at some step in understanding the relationship between these rules and our universe, there will be an anthropic move of some sort, where you say,
*  there's a lot of things going on, but intelligent observers will only observe this subset of things?
*  Intelligent observers, no. So the question is, what is the right idealization of the human observer?
*  So I'll give you a couple that seem to be enough. So one important one is we're computationally bounded.
*  We don't get to observe. So let's take the gas molecule example again. If you have this gas, it's got a bunch of molecules bouncing around.
*  If you're a sophisticated enough observer, you can see every single molecule, you can work out all the collisions. And in particular, that will allow you, so a big principle of statistical mechanics is second law of thermodynamics,
*  which says typically things get more random as the molecules bounce around in a gas. But if we are not computationally bounded observers, and we can figure out what all these trajectories of all these molecules are,
*  we don't get the second law of thermodynamics. As non-computationally bounded observers, the second law of thermodynamics simply isn't true. And that same idea of a computationally bounded observer is necessary, I think,
*  for us to believe that space has a continuous structure and various other things about the universe. So that's kind of step one.
*  So we're not Laplace's demon.
*  What's that? Sorry?
*  We're not Laplace's demon.
*  That is correct. We're not Laplace. We're not Maxwell's demon. We are thoroughly non-demonic in that sense.
*  Right. We're not finite and bounded.
*  We only have this sort of bounded ability to look at the details of the universe. That's step one.
*  Step two I've understood more recently, actually. And step two is something which I think is sort of the physics essence of consciousness,
*  which is that we have this idea that there is a single thread of experience that we have.
*  It might not be that way. That is, in the universe, and we didn't talk about this in detail yet, but in the universe, all these little updatings are happening all over the universe.
*  But we think that, in a sense, there's sort of microscopic pieces of time happening all over the universe.
*  But we believe we have a single identity through time and that there is a single thread of experience that we have through time.
*  Now, it's by no means self-evident that that would be the way it is, because in our model of physics, everything about the universe is being rewritten 10 to the 100 times or something, or something like this.
*  And so the fact that we have the idea that we are still the same us a second later is non-trivial.
*  And so I think that an observer who has that idea that there's a single thread of time, that is one of the things that you need in order to get the laws of physics that we humans observe.
*  And I think that's a... So there's this idea of we maintain our identity through time, which we might not.
*  And the thing I realized actually even more recently, although I should have realized this earlier, is there's a similar idea for space.
*  It is not self-evident that there is a notion of pure motion.
*  So in other words, you take an object, you move it somewhere else.
*  In our models, I take an object, I move it somewhere else.
*  It's made of different atoms of space by the time it gets to its destination, probably.
*  And so then the question is, how come there's an idea of pure motion?
*  How come a thing can just be moved without changing?
*  Now, obviously, we know in general relativity, you're close to a black hole, funky things can happen to you if you move.
*  Because the structure of space is changing.
*  But this is a very basic fact that most of the time, something moves and it is still the same thing.
*  And so this idea of this single thread of experience in time, this idea that it is possible to have pure motion,
*  and it's possible to maintain your identity as you move around in space,
*  those two attributes seem to be what you need to derive generic laws of physics.
*  That's what you seem to need to derive general relativity and quantum mechanics.
*  Now, if you start asking, why does the electron mass come out to be the actual value it has for us humans,
*  we probably need a little bit more information about us humans to be able to figure that out.
*  That's right.
*  I think. I'm not sure.
*  I mean, for example, one of the things that's a current challenge is the local symmetry groups, local gauge groups.
*  It is looking very likely that it is an inevitable feature of our models that there will be local gauge invariance.
*  And the thing that looks conceivable, I don't know yet, is that the actual gauge group will be determined.
*  So in other words, even though we don't yet know why the universe has three dimensions,
*  we might actually know why the internal symmetry group is maybe a subgroup of E8 or whatever it is
*  before we even know this thing about space.
*  But we don't know, if you ask what's the electron-muon mass ratio, we're still a fair distance away from figuring that out.
*  The classic question.
*  And my expectation would be that there'll be a particular rule that we'll find
*  which will have where a whole bunch of those things will come out.
*  And one of the features, if you believe that the rule is simple,
*  is if you move from one simple rule to another nearby simple rule, everything's going to change
*  because there just aren't very many rules that are that simple.
*  And so instead of having electron-muon mass ratio, it'll be,
*  well, there actually are an infinite number of generations of particles
*  and there are a bizarre number of dimensions of space and all this kind of thing.
*  It'll just be completely different.
*  But that's the current expectation.
*  I think you raised the anthropic principle.
*  And to me, the anthropic principle is sort of a story of lack of imagination, so to speak.
*  Because it's saying the only way that we can have life, intelligence, consciousness,
*  whatever, is the particular way we've seen it.
*  And one of the consequences of this principle of computational equivalence
*  is that actually something like intelligence is ubiquitous.
*  That is, you might have thought to get something as computationally sophisticated
*  as us humans with our brains and all this kind of thing,
*  you need the whole process that's led to us humans.
*  But what the principle of computational equivalence says is that's not true.
*  Even these very simple rules can do it.
*  And that has lots of consequences.
*  If you're worrying about extraterrestrial intelligence, for example,
*  that tells you it's everywhere.
*  It's a question of whether we are sufficiently aligned with that intelligence
*  to be able to recognize it as something that, for example,
*  has purposes that we can understand as human-like purposes.
*  And I think this idea, intelligence requires liquid water,
*  it's almost laughable.
*  I'm on your side when it comes to that.
*  But intelligence might require space-time in some sense.
*  So let's at least try to get that.
*  I mean, is this naive picture that I have in mind where you have the hypergraph,
*  you update, it's a discrete updating.
*  Can I think of the graph at any one update as space
*  and the update itself as time, or is that too simple-minded?
*  Okay, so it gets a little complicated.
*  In fact, the complexity that arises is quantum mechanics, I think.
*  And so it's, in a sense, you try and make it that simple.
*  Okay, so the basic point is the rule says if you have a lump of atoms of space
*  that are connected in this way,
*  transform it into a lump that's connected in this other way.
*  And basically the rule just says that's what you do.
*  It doesn't say where you do it.
*  It's just any time there's a lump that looks like this,
*  you can transform it into a lump that looks like that.
*  And so those transformations can be happening all over this hypergraph.
*  And so it is not at all obvious.
*  That is the only thing that's defined is these can happen.
*  The question of when they happen, what counts as the sort of simultaneity surface,
*  what counts as that moment in time,
*  is something that's really in the eye of the observer.
*  Okay, but the updated graph is supposed to represent space, time, and the things within it,
*  or is it a more subtle map there?
*  No, no. So at any given what's happening is this graph is getting updated.
*  And there are lots of little places where it can get updated.
*  And you can say, okay, I'm going to consider the graph with this collection of updates having been done.
*  I am going to consider that as time t equals zero, let's say.
*  And then another situation you're saying,
*  I'm going to say, now I'm going to say this collection of updates is time t equals one, for example.
*  And each one of those time slices, at each one of those sort of,
*  well, in the language of physics, space-like hyper surfaces,
*  that represents an instantaneous structure of space.
*  But it is somewhat arbitrary what you consider to be this instantaneous sort of structure of space,
*  just as it is in general relativity.
*  Well, sure, right. That's very familiar from general relativity.
*  But I'm just saying, is the collection of the whole shebang space-time and the things within it?
*  No, it's just space. A single hypergraph.
*  The collection of all the updated hypergraphs, that's what I'm asking.
*  Oh, yeah, yeah. Right. The sequence of updates, the hypergraph together with all its updates is supposed to be space-time.
*  And one of the things that is interesting and non-trivial here is,
*  a lot of most traditional views of physics have thought of space and time as being the same kind of thing.
*  In this model, they're really not.
*  Spaced is the extent of the spatial hypergraph.
*  Time is the computational process of updating this hypergraph.
*  So time is the progression of a computation.
*  Space is just, oh, you follow these connections in the hypergraph.
*  And so that makes it not at all obvious that you're going to get things like relativity out of the model
*  because one is breaking apart the traditional connection between space and time.
*  But you say that the whole shebang is space-time.
*  One of the reasons I hesitate a little bit about that is the shebang is made by a computationally irreducible process.
*  So we don't get to, it is a, you know, to say let's just unroll the whole structure of the universe forever.
*  Well, we don't get to do that in the universe.
*  I mean, the universe will do that as the universe does it, but we can't just say this is what's going to happen
*  because there is this phenomenon of computational irreducibility.
*  But I do want to just distinguish between this idea and something that someone like myself would be very fond of,
*  which is some combination of quantum gravity and ever-ready in many worlds
*  where there are different branches of the wave function where the geometry of space-time is just different, perhaps radically different.
*  It sounds like that is not something that is coming out of your hypergraphs.
*  Oh, no, no, that will come out. I was simplifying a bit.
*  So what's happening is at every, you know, these updates, they get, you're just saying
*  whenever you see a piece of hypergraph that looks like this, you can do an update.
*  There are many possible sequences of updates, there are many possible sequencers of these updates that could occur.
*  Each one of those sequencers defines a different path of history, effectively.
*  Now, the non-trivial fact, another additional piece, is this thing we call causal invariance.
*  And so what's happening is if you look at this...
*  Okay, so if you look at this hypergraph and you imagine you roll up the whole universe into a single lump
*  that you can kind of hold in your hand, and then you say that single lump is going to evolve to another whole universe,
*  that process of evolution is not a single thread.
*  That process can branch because the whole universe, if you did two updatings in different orders, for example,
*  you would get different outcomes, you would get different whole universes.
*  And that's very similar to the many-world story.
*  And one difference is that in our models, we're really, you know, taking seriously this idea that there's branching
*  as a result of these different possible orders of updating and so on,
*  and that there's this thing we call the multi-way graph, which is just this description of all these different possible paths of history.
*  But for us, it's very important that the paths of history can branch and they can also merge.
*  And they merge when two outcomes for the universe end up... you apply two different rules,
*  and it so happens that they end up with an identical universe.
*  They end up with a hypergraph that is isomorphic that you can rearrange to be exactly the same hypergraph.
*  And so that branching and merging process is really important because one feature of many of our models,
*  and in fact it seems to be... in the end, it's a ubiquitous feature of all of them,
*  but that's not how it initially looks. Initially it looks like you have to pick it specially, but in the end you don't.
*  It's this thing we call causal invariance.
*  And so essentially what causal invariance says is every time there's a branch, there will be a subsequent merge.
*  So in other words, even though you thought you were going to go in two different branches of history,
*  even though for a while you've got two completely incompatible structures of spacetime, in the end they will merge.
*  In the end they'll be... and that's some... and so that's why, in our models, that's in the end why you get objectivity in quantum mechanics.
*  Well, let me see. So if I'm just a conventional many worlds person, there's perfectly deterministic evolution of the entire wave function.
*  It will branch. And part of the reason why it branches and operationally they never merge
*  is because there's some environment which is huge numbers of degrees of freedom,
*  and the different states in the environment will never exactly line up.
*  So eventually you might imagine them merging back together 10 to the 100 years from now.
*  Is that the kind of thing you have going on, or is your re-merging much more rapid?
*  No, the re-merging is faster than that. But again, it's a little complicated.
*  But the fact that there is divergence and merging is basically...
*  So what in the end happens is that the uncertainty principle is a story of essentially curvature in this basically multi-way graph space.
*  And it's just like in spacetime, one of the classic features is you go around a square,
*  you go around a square with all the right angles and distances, does it close up?
*  If space is curved, it doesn't close up. And what's happening in our models is it's the exact same thing,
*  although the space is more complicated and more like a Hilbert space, that what's happening is the same exact kind of thing
*  is what leads to the uncertainty principle in quantum mechanics. It's that same failure to close up.
*  And now what ends up being the case, and we don't understand this as completely as I would like yet.
*  So just to give some sense of the situation with respect to what we know and what we don't know,
*  so these multi-way graphs... Okay, so first thing to say about multi-way graphs is they represent the sort of branching
*  and merging of paths of history for the universe. So one thing you can do is you can say at any given time,
*  what is the structure of all of those possible branches of history?
*  So just like in space-time, we're going to say let's pick a space like hypersurface.
*  Let's pick a simultaneous moment for all these different parts of space. What does space look like?
*  Or we can do the same kind of thing for this multi-way graph. If we do that, we get this thing which has all these different
*  possible states of the universe. And how are they connected? Well, they're connected in what we call a branchial graph,
*  a graph that represents these different branches. And so one convenient way to construct a branchial graph
*  is to look at the common ancestry of those states. So if two of those states just branched one step before,
*  they're close together in the branchial graph. If they branched many, many, many steps before, they're further apart.
*  And so you can construct, just like from this sort of structure of space-time, you can construct a sort of instantaneous
*  structure of space. So from this multi-way graph, you can construct what we call branchial space.
*  This is the instantaneous representation of the possible branches of quantum history. And in a sense,
*  it's a map of entanglements. Because every one of these branchings, the fact that they had a common ancestor
*  and that they will, is a story of entanglement. That's saying that these two branches of history are not independent.
*  They are connected by the fact that they are entangled. So in a sense, this branchial space is a map of quantum entanglements.
*  And so it's really, I think, incredibly cool because branchial space has many of the same attributes
*  the physical space has. It's more like a Hilbert space. It's a little bit complicated, and we don't fully understand it yet.
*  It's something like a, what is the analog? In space-time, we have this idea of Minkowski space,
*  which has both the usual Euclidean type space for space, and then this notion of time being a separate thing.
*  And exactly how that works for a Hilbert space, the analog of Minkowski space for the Hilbert space of states,
*  we don't understand. It may be something related to Twister space. That's a special case of it.
*  But it's something we don't yet understand. But one thing we do know is, in terms of what we understand,
*  what we don't understand, we do know that our multi-way graphs reproduce an approach to quantum mechanics
*  called categorical quantum mechanics. And we can just show that they are equivalent, basically.
*  And it's known that categorical quantum mechanics is equivalent to standard quantum mechanics that people studied from the 1920s and so on.
*  And not only can we show that they're equivalent, one of the recent things in the last month or two has been
*  we can actually use our models to model quantum circuits. And we can essentially compile a standard quantum circuit into a multi-way graph.
*  And the big excitement of the last few weeks has been, and we can do better circuit optimization in multi-way graphs
*  than you've been able to do in standard quantum circuit formalism. So in other words, we can, if you want to simulate a quantum circuit,
*  it's better to do it through our model than it is to do it through the standard mechanisms of quantum mechanics.
*  But we know the answers have to be the same. So that's what we know for quantum mechanics.
*  We don't yet know fully how that works for quantum field theory. Quantum mechanics, just for other people's benefit,
*  I know you know this very well, but quantum mechanics is a story of what do individual particles do.
*  Quantum field theory is a story of even if you can make particles and the particles are sort of spread out through space,
*  how does that work quantum mechanically? And that's a more difficult thing, which we're just starting to understand.
*  I do want to dig in more specifically to mapping your approach onto the different interpretations of quantum mechanics.
*  But let's just give back up a little bit and keep it simple for the folks who are trying to stay with us here.
*  If I look at the pictures of the graphs, of the hyper graphs that are following the rules, very naively, it looks super duper classical.
*  There's a graph. Something is happening at every point. So could you just explain why you even get something like the double slit experiment
*  where you can get interference, but then if you look at it, you don't get interference. Is that something that pops out of your model?
*  Yes. Yes. I mean, by pop out, there's a little bit of effort to make that pop happen.
*  Sure, of course.
*  Okay. So when you see pictures of these hyper graphs, they are pictures drawn for a particular branch of history,
*  particular branch of quantum mechanical history. That's what we're easily able to visualize.
*  Now, it's been a big project to make what we call local multi-way systems which mix spatial extent with branch-ill extent.
*  That is, mix things which are moving around in space with things which are going to different branches of history.
*  And this has been a big challenge because it's pretty hard for us humans to visualize that stuff.
*  And we've been working on it for the last year, actually. We're getting fairly close to having pretty good visualizations of that.
*  But those are significantly more difficult to understand. But the typical pictures you'll see, our project is full of graphs.
*  So there's many different kinds of graphs that show up. And they're kind of in all the...
*  One of the things that's been a big kind of practical win is that we, at some moment, we kind of did the colors for our model
*  and picked this graph is going to be this color, this graph is going to be this other color.
*  And so as soon as you see one of these things, you can tell that's a causal graph, that's a branch-ill graph or whatever.
*  That's just a... And because all the code for our models is all openly available, people have been just using that code.
*  And so people have been following kind of the color standards, which really help.
*  But so there are probably six different kinds of graphs that show up. The ones that are the most common and colored bullish are the ones
*  that are the hypergraphs that represent the instantaneous structure of space.
*  So there are then these multi-way graphs that represent the kind of the branching and merging of quantum histories.
*  Then there are branch-ill graphs, which are traditionally pink in our world, that represent these slices through the multi-way system.
*  They represent... So in space-time, we are taking a slice through space-time and finding this is what space instantaneously looks like.
*  In the multi-way graph, you take a slice and you're saying this is what the instantaneous map of quantum states looks like.
*  And in fact, what happens is in relativity, we're used to having this idea of reference frames, of how do we label what space and time are?
*  How does an observer decide what counts as space, what counts as time, and so on, if the observer is going at different speeds, you know,
*  you're tipping the reference frame, all those kinds of things. We have exactly the same kind of thing in quantum mechanics.
*  We have what we call quantum observation frames, which are basically the thing that represents...
*  This corresponds to a particular state of the quantum world. And you can think of these in branch-ill space, you can think of these points in branch-ill space,
*  which are histories of the universe, as being different quantum eigenstates. So you can think of them as being different basis elements,
*  so different things from which you would make up a quantum state. And so then what happens is when you have one of these quantum observation frames,
*  you've sliced this multi-way graph, you've got this whole collection of quantum states, and now you ask, for example...
*  So now, okay, this is one other thing I have to explain. In quantum mechanics, the big idea is this notion of quantum amplitudes.
*  That is, you just get to know there's this object, which has complex numbers associated with it and all this kind of thing, that is the quantum amplitude.
*  And so the question is, that quantum amplitude, the complex numbers that are associated with it, one of the things that we've realized is
*  the idea that you can think of a quantum amplitude in terms of complex numbers is confusing. In fact, the right way to think about it is
*  it has a magnitude and it has a phase. And in our models, the magnitude of the quantum amplitude is the result of path counting in the multi-way graph.
*  So in other words, if there are many ways to get to that state in the multi-way graph, the magnitude of the quantum amplitude is determined by the number of ways to get to that point in the multi-way graph.
*  The phase of the quantum amplitude is determined by the position in branchial space. So in other words, the idea is, as you move around in branchial space,
*  you are changing the phase, the coordinates of branchial space are essentially phase coordinates in quantum mechanics.
*  Sorry, you might need to tell me what branchial space is again.
*  Okay, so then we've got this all possible histories of the universe, which correspond to this multi-way graph. They branch, they merge, it's a complicated thing.
*  Now we're saying, and that graph is being formed through time. So now we say, let's take an instantaneous time slice across that graph.
*  It is the quantum analog of a reference frame in relativity. And by the way, those reference frames can get quite wild in quantum mechanics.
*  They're somewhat wilder than the ones you would typically use in general relativity. At least that's our view of how this works.
*  So those reference frames are sort of the choice of the observer. They're not something that is intrinsic to the physics.
*  They're just, oh, we've got this multi-way graph. Now we're going to say, for our purposes, we're going to say this is what the time slice is of that will be like.
*  So this branchial graph is the structure you get by slicing through this multi-way graph. So you're asking the various points in this multi-way graph, how are they arranged?
*  Well, we can say they're arranged nearby if they correspond to something which just had a common ancestor. Just one step back, they had a common ancestor.
*  And other ones, you know, you have to, so basically what happens is the simplest way to make these branchial graphs is you simply join by an edge every pair of nodes that have a common ancestor.
*  And then, so what that means is if there are things that are far apart in the branchial graph, it means their common ancestor was probably many steps in the past.
*  And the idea then is that that, okay, so the claim, which is again mathematically quite non-trivial, is that the coordination of branchial space,
*  that is if you try and assign coordinates, just like in physical space, you'd say there are all these atoms of space and they're just connected in certain ways,
*  but now we say based on those connections, it is, we can say this one has coordinate position blah, blah, blah, and it's next to this other one which has a very similar coordinate position.
*  Okay, so the same, you can do the same kind of thing in branchial space. You can try and coordinate toize branchial space.
*  And the claim is the coordinates of branchial space are the phase of the quantum amplitude.
*  So in other words, what that means, so just to sort of perhaps for people's benefit, maybe we can explain something about, so, you know, I don't know how to, we can try doing, let's see, you probably can do this better than I can, but explain quantum phase.
*  Well, yeah, sorry, the way that I just say it is that, you know, the wave function for a single particle is like a wave. Sometimes it's positive, sometimes it's negative, or plus or minus i, so different contributions can destructively interfere as well as constructively interfere.
*  Right, but the critical idea in a sense is as you have that wave that's going up and down, the phase of the wave is at a particular moment in time, are you up or are you down?
*  Yeah, right.
*  And the phase is kind of the shifting of that wave relative to a particular moment in time. So what we're saying is this branchial space represents kind of where that thing is shifted.
*  A position in branchial space corresponds to a certain shift of that thing. So here's the place where it's actually my favorite result so far in our physics project, which is worth explaining because then we can talk about the double-slot experiment a little bit more easily.
*  Okay, so let's talk about physical space. One of the questions is if you have an object, a particle for example, in physical space, how will it move in physical space? And the standard idea of general relativity and of actually Newtonian physics is it moves according to a shortest path from one point to another.
*  So it's like whatever the shortest path is in space, it'll go along that shortest path. If space is flat, the shortest path will be a straight line. If space is curved, the shortest path might be deformed.
*  And the big idea in Einstein's equations and so on is the deformation of space, the curvature of space is produced by the presence of energy momentum, by the presence of mass in space.
*  So essentially what we're saying is geodesics in space are deflected by the presence of energy. Geodesics shortest paths in space are deflected by the presence of energy. That's kind of a version of what's happening in general relativity.
*  Okay, so now let's look at these multi-way graphs. So the derivation of the Einstein equations and the deflection of geodesics by the presence of energy is something we can do in terms of our rewriting of hypergraphs and a bunch of mathematics associated with that.
*  So it's sort of a mathematical result from that. Now something very analogous to that mathematical result is also true for the multi-way graph. And what then happens is the geodesics essentially in branchial space, the shortest paths in this branchial space, are also deflected by the presence of energy momentum.
*  Okay, so this is where it gets really fun because the sort of good core formulation of quantum mechanics is the Feynman path integral. And the Feynman path integral says you look at all these possible paths of history and you say the phase, the quantum phase associated with the path of history is e to the iS over h bar,
*  where S is this quantity, the action, which is an integral of Lagrangian density, which is essentially the aversion of the amount of energy momentum in a particular region of something.
*  Now in our world that's a particular region of branchial space. Effectively the density of energy momentum in branchial space leads to the deflection of geodesics in branchial space. And so what does that mean? If the position in branchial space is the phase of the quantum amplitude, that means the deflection of a geodesic is a change of phase.
*  And the Feynman path integral is precisely telling you that the presence of energy momentum leads to a change of phase in a quantum amplitude. So what it's saying is, the bigger picture here is that the same mathematics that leads to the Einstein equations in space-time leads to the Feynman path integral in multi-way graphs and branchial space and so on.
*  So in a sense these two fundamental principles of 20th century physics, general relativity and quantum mechanics, in our models are basically the same thing, except that the general relativity is a story of what happens in space-time and quantum mechanics is the story of what happens in what we sometimes call branch-time, the thing you get which is the cross of branchial space together with time.
*  This might be a very unfair question, but I think there's something super simple that I am missing here, which is I just don't see where the negative numbers come in. I hear you saying that there's this position in branchial space as a phase, and I get that if that is true you get the result you want to have.
*  The simplest possible explanation for the negative numbers would make me happy. In other words, the reason why you can interfere as well as add your probabilities.
*  Let me explain. Let's say you're doing a double slit experiment. The photon can go through one slit, it can go through the other slit. Those two possibilities, the question is where do those different possible paths for the photon, where are they in branchial space? In physical space they're going through two slits.
*  The question is where are they in branchial space? If those two possibilities wind up at essentially the same point in branchial space, that is that they end up with the same phase. If those two things wind up at opposite ends of branchial space, those two possible paths of the photon end up in two radically different pieces of branchial space.
*  So what? The issue is how does an observer observe what's going on? This is again, I'm afraid there's another level of concept we have to have here, which is how an observer makes sense of what's going on in the quantum universe.
*  One of the issues is when you are an observer embedded within the universe, you, well we can talk about space time and causal, let's forget space time for a second. In this world of multiray graphs and branching and merging and so on, one of the things that's a little bit brain twisting is you as an observer are also branching.
*  You're part of this multiray graph. So the question of quantum mechanics is how does a branching brain perceive a branching universe? So in other words, your brain is branching just like the universe is branching.
*  And so now what you have to do, and this is where, for example, the idea of a single thread of experience, a single thread of time is important because the whole notion of us as observers is we have at least the fiction that our brain doesn't branch.
*  We have the fiction that definite things happen. And so the question is how do we implement that fiction? And then is our implementation of the fiction consistent with what we actually observe in the world?
*  So the way that we, a convenient way, and this is an idea of Jonathan Gorard, who's one of the people who's been working on this project, is what he calls the completion interpretation of quantum mechanics.
*  And what it has to do with is imagine we've got a branch, but then say, but the observer has to corral those branches together in order to believe that something definite happens.
*  So how is the observer going to do that? What the observer does is to just say, I'm going to imagine that these two branches are equivalent.
*  I'm just going to make a mathematical equivalence between them. And then I'm going to see what consequence does that have for my view of the universe.
*  And so that's the thing. So it might be the case that the view of the universe knitting together these branches would rapidly become incredibly inconsistent.
*  But this causal invariance property implies that eventually these branches will merge. So eventually it's going to be okay.
*  But the question of whether the observer can kind of speed that up and say, no, I'm going to insist it's okay right now, even though it might take a century for these branches from different parts of the universe to merge, it's okay to think of them as merging right now.
*  So that's a consequence mathematically of this causal invariance idea that it's possible to do that.
*  But so in that interpretation, what you're doing is you're essentially making completions that try and corral back together these different branches of history.
*  Okay, so what happens if the two photons wind up at opposite ends of branchial space?
*  Basically what happens is you as an observer have to construct completions that basically complete the whole universe, because you're trying to get from one end of branchial space to another.
*  You're trying to knit everything together. And that means basically that photon, as far as you're concerned, isn't there.
*  So essentially the reason that you're getting destructive interference is that you as an observer simply can't knit it together to say there really is a photon here.
*  It's like the photon has been just smashed into pieces that are scattered all over branchial space.
*  I actually did understand that, even though I wasn't necessarily expecting to.
*  But it seems and maybe this is again an unfair comment, but I'll let you riff on it.
*  It seems like just like we thought we needed interpretations of quantum mechanics in the 1930s that somehow we need interpretations of hypergraphs or growing hypergraphs.
*  I mean, the story you just told, which I'm perfectly willing to grant gets you the double slittics, etc., does seem to involve some metaphysical, interpretational steps along the way.
*  Fair point. I mean, this is a fundamental point.
*  In our models, if we were not roughly the way we are, we would not conclude that the laws of physics are the way they are.
*  So consider the case of the gas molecules again.
*  If we were one of these little demons that's able to compute everything about the gas molecules and do all those things, we wouldn't conclude that thermodynamics and hydrodynamics work the way they do.
*  That's right. We would say, oh, actually, we noticed that these little correlations of molecules here and there and the other, and we'd get a completely different conclusion.
*  So the fact that we derive quantum mechanics is a consequence of the fact that we are roughly the way we are, not in detail with two eyes and all this kind of thing.
*  But in particular, the fact that the branching brain perceiving the branching universe has the idea that definite things happen, that's critical.
*  If we didn't have that notion, and you can think about it in terms of how our brains work.
*  We got all these neurons firing all over our brains.
*  And in a sense, there wouldn't be any real reason to think that there will be a definite thread of experience that we have.
*  It could just be there's all these different things happening all throughout our brain.
*  And this is a fundamental feature of our experience of the world, is that we believe there's a definite thread of time.
*  And so, yes, that is necessary. And I think without that, and it's interesting to think about it, what do the aliens, so to speak, think physics is like?
*  Because, for example, it matters probably that we are roughly the size we are. It matters that we have this notion of single thread of time.
*  I don't think we would recognize the aliens, so to speak, if they didn't have something like a single thread of time.
*  I'm fond of making the comment, the weather has a mind of its own.
*  It's got all this complicated hydrodynamic processes happening in the atmosphere and so on.
*  But yet, we don't have the idea that it has some sort of human-like consciousness, usually at least, depending on our animism, our level of animism.
*  Panpsychism, yeah.
*  Panpsychism, yeah.
*  But would I be then correct to conclude from that, that you think that from this kind of fundamental setup with the hypergraphs and the updates and so forth, we could not get a universe that was fundamentally classical and had observers like ourselves in it?
*  I think our models are very fundamentally quantum mechanical.
*  I think that you can't really get, you know, what you can...
*  Okay, so what you would have to do is say there is only one...
*  Okay, here's a way you can get something that's like a classical universe.
*  And at first it sounds completely crazy, but let's say the universe was built using a Turing machine.
*  So a Turing machine is this model of computation that has, you know, it's tape that has all this data on it and has this head that moves up and down along the tape.
*  And at any moment, it's only doing one thing.
*  It's only at the position of the head that anything changes.
*  And so you could say, imagine a universe where the Turing machine does a definite thing.
*  Let me think about this for a second.
*  Yeah, let me think about this.
*  Is that right?
*  Well, okay, so you can certainly imagine setting it up so that there is only one possible thread of time.
*  Because the Turing machine is an ordinary Turing machine.
*  And for every state it gets into, it has only one possible successful state.
*  And so you might say...
*  And so that would be a kind of degenerate thing of a model like ours that is classical.
*  Yeah, okay, that's fair.
*  But usually what's happening is there are many different places where things can happen.
*  So there are many choices of what can happen, what you do now, what you do next, etc., etc., etc.
*  And I keep on sort of dancing around one issue which we haven't talked about,
*  which is the notion of causal relationships between updating events.
*  So we've got two different updating events.
*  And we could say which one happens before which other one.
*  Well, if one of them, specifically if the output from one of them is used as the input to another one,
*  then it better be the case that the one whose output is being used occurs before the one that needs that output as input.
*  So that defines a certain ordering on certain events have a definite ordering.
*  And in physics terms, those are the time-like separated events.
*  And those are events that are necessarily time-like, separated.
*  So then there are other events that could happen.
*  You could decide that you're going to say these two events happen simultaneously.
*  The spacecraft landed on Mars right as I was eating lunch, so to speak.
*  And those were considered simultaneous events.
*  So one of the issues is given this set of events that are happening, there are certain causal relationships.
*  That is, one event must occur before another event.
*  And you can make another kind of graph, a so-called causal graph, that represents that net of relationships.
*  And just to make things more complicated, in the multi-way graph, there is a multi-way causal graph.
*  Which says there are these events happening.
*  And events can be separated. They can either be time-like.
*  That is, one event must occur before another event.
*  They can be space-like in the sense that they can be at different positions in physical space.
*  Or they can also be branch-like in the sense that they occur on different branches of quantum history.
*  And so all three of those things are possible. Time-like, space-like, branch-like separation.
*  And in fact, the interplay between those things gets pretty interesting when you start talking about things in black holes and ADF CFT and all this kind of stuff.
*  That is how those kinds of things seem to come out, is the relationship between time-like, space-like, branch-like separated events.
*  I mean, you hinted at this a little bit, but maybe to concisely say how you would characterize the solution to the measurement problem of quantum mechanics in your view.
*  I mean, there is a standard list of options with many worlds and hidden variables and dynamical collapses.
*  Are you different than all of those?
*  Probably. I mean, I am not sure because I think that...
*  Let's see. We have a much more microscopic view of what happens in measurement because we are trying to describe the whole universe.
*  We don't get to say, here is my quantum system and then outside of my quantum system is my measurement system.
*  Everything has to be part of the description that we are giving of the universe.
*  And so that is the first big difference.
*  Now, I think it depends what you mean by what the quantum measurement problem is.
*  So one thing that I think is a significant piece of the quantum measurement story is why do people think that definite things happen?
*  And so what essentially is going on is different quantum frames cause people to believe at some moment that different things have happened.
*  But there is some sense in which there is a global consistency to what must happen.
*  So again, in other words, the fact that there are two different outcomes from this measurement is a consequence of the fact that the observer can have defined two different quantum observation frames.
*  And that is what causes those different possible outcomes from the experiment.
*  It sounds like you are closest in spirit to many worlds in the sense that someone who believed in hidden variables or dynamical collapses would say that there just is one outcome for every measurement.
*  You don't need to think very hard about it.
*  Right. No, that is correct.
*  This does not have that idea.
*  This has the idea that the outcome is in a sense based on the frame with which the observer observes it.
*  So in a sense it is kind of like a many worlds thing where which branch did you go on.
*  But the difference is in a sense that in our situation those branches always eventually merge.
*  So in other words, even though you have picked a particular, this observer at this moment has got this outcome, that there will be eventual consistency in how the universe behaves.
*  Now, have we figured all of this out?
*  Not completely.
*  Let me give you an example of where sort of the frontier of what we understand and don't understand.
*  So an obvious question is what does it mean for quantum computing?
*  So in quantum computing there is kind of this notion that has been around since I first studied this stuff around 1981 or so that, gosh, in quantum mechanics there is this, all these different possible paths of history.
*  And I happened to study this with Dick Feynman.
*  So he was very into the multiple paths of history idea because that had been his idea for a way of setting up quantum mechanics.
*  It does make sense.
*  It's like, just think, you know, if you could get this computation to not just go in one, not just do one computation at a time, but follow all these different possible paths of computation, you could in parallel work out all these different results and you'd be able to factor integers fast.
*  We didn't know about that at that time.
*  But those kinds of things.
*  So the idea of quantum computing, you know, the big hope is just use all those paths of history to do a different computation on each path.
*  But the next question is, in the end, we have to observe what the answer was.
*  And so in a sense we've got all these threads of history that have all split apart.
*  They're all doing their different things.
*  We've got to corral all those threads of history back together again to make a definite measurement and say what happened.
*  And so in our models, we can actually ask what is microscopically involved in corralling those threads of history back together.
*  And so in Jonathan's setup of this completion interpretation, we have at least a model of that, which is it involves these completions, these places where you assume that two branches are connected.
*  And by the way, the mathematical underpinning of that, somewhat interesting.
*  The mathematical underpinning comes from the theory of automated theorem proving, which might seem irrelevant, but it isn't.
*  And so the point is when you have, in mathematics, you say there's some axiom system.
*  You say, you know, x plus y is always equal to y plus x.
*  You know, x plus zero is equal to zero. It's equal to x and so on.
*  And then you say, given those rules, can you prove that x, I don't know, some result in algebra?
*  Can you prove that result?
*  And you say, one way to think about that is can I get from one algebraic expression to another algebraic expression just by making this series of moves that correspond to applying particular axioms?
*  So then, if you say, well, I'm starting off from one expression.
*  Now let me apply those axioms in all possible ways and build up this whole graph of possible outcomes.
*  Well, what you build is precisely one of these multi-way graphs.
*  And the space of possible results that you can get starting from one expression, what can you get is a multi-way graph.
*  And so automated theorem proving is the question of, the proof of a theorem is a path that goes from one expression to another expression.
*  So automated theorem proving is about finding that path.
*  And so completions become the formation of lemmas.
*  So in mathematics, you would say, let's make a lemma where we prove that this particular thing is equal to this thing, and that's a piece that we'll use in our big proof.
*  And so these completions are essentially lemmas.
*  They are assumptions about how the universe works that we as observers are making.
*  And so one thing we can then ask for the quantum computing case is, how many such lemmas do we have to produce?
*  How much effort of knitting together the structure of branchial space do we observers have to do in order to conclude the result of the quantum computation?
*  And it seems we're still nailing this down. It's still a little bit messy.
*  But it seems that you can never win with quantum computing.
*  That is, that when you branch out in all these different ways, the effort to corral things back together is at least as great as the gain that you get from things branching apart.
*  Now, to really nail that down, we have to get ever better models of the observer.
*  And that's just not something that traditional models of quantum mechanics, traditional interpretations of quantum mechanics, they are out of that business.
*  So we can't just say, and the observer works like this, external to the quantum system.
*  But we have to be more microscopic and say, no, we're actually going to describe how the observer is working.
*  And so our best model so far is Jonathan's completion interpretation that involves these potential lemmas being produced.
*  There's a traditional understanding in well, there's an understanding in traditional quantum computing that there are some problems for which quantum mechanics certainly gives you a speed up.
*  Are you saying that's not true in your model? Yeah, I think it's not going to be true.
*  That's my guess. I think what's going to happen is, you know, if you take like Shaw's algorithm for factoring, which is primarily a quantum Fourier transform,
*  that Fourier transform is done beautifully quickly because there are all these threads that are running in parallel.
*  The problem is every thread is somewhere in a different place in branchial space, that thread.
*  But us observers, we have to corral all those things back together again in order to tell what actually happened.
*  And that's, you know, so there's a, you know, usually in quantum computing, one just says, and then there's a measurement.
*  Now, in actuality, when you have an actual device, you have all kinds of issues in making that measurement, all kinds of how quickly does it decohere, all these kinds of things.
*  There are all these kinds of very practical experimental, you know, features.
*  And I think people have generally said, given the formalism of quantum mechanics, it, you know, it's like, well, all this quantum stuff happens and then boom, we do a measurement.
*  And the boom we do a measurement is actually pretty difficult in practice with actual experiments.
*  But people have said, but, you know, if we do these experiments well enough, it will become the mathematical idealization that, you know, Voinam and others made about how measurement works.
*  And I don't think that's going to be true.
*  I mean, we're not sure yet, but it seems likely that there will be no way to do to sort of that.
*  If you're honest about how the measurement works, the measurement takes effort.
*  But are you saying that that's going to be a generic result about even conventional quantum mechanics?
*  Or is this specific to your approach?
*  If you could if you could study how measurement works well enough in quantum mechanics.
*  Yes, the problem is in in traditional quantum mechanics, it's like this is all the quantum.
*  These are all the quantum amplitudes.
*  And then the hammer comes down and it's, you know, the born rule or whatever.
*  And that's the end of it.
*  And so you don't you don't get to look inside that measurement process.
*  And when people, you know, I'm I'm probably not, you know, one of the strange things that's happened to me in this physics project is that, you know, I I knew about everything that was going on in physics.
*  Not everything, perhaps, but a lot of things 40 years ago.
*  And then I kind of went to sleep for 40 years and woke up again.
*  And it's remarkable.
*  It's really cool, actually, to see a lot of stuff really didn't change and some stuff advanced.
*  And it's like, you know, I used to know the masses of all these elementary particles.
*  You know, the mass of the lambda is one one one five MEV.
*  And now I look it up again.
*  It's, you know, one one one four point nine six two or something.
*  It's like that's so, you know, there are things like that.
*  And there are also also mathematical ideas and so on.
*  But I'm not sure that I would know everything that people have done and kind of sort of models of quantum measurement.
*  But certainly back when I last knew about it in great detail, people were sort of starting to say.
*  And then we take the small number of quantum degrees of freedom that we're looking at as the quantum system.
*  And we let that sort of spread out in a larger number of quantum degrees of freedom where eventually it will become unambiguous what happened for essentially thermodynamic reasons.
*  Yeah, because it's more or less like what happens in the gas getting randomized.
*  And in fact, this was a thing that Simon and I worked on back when we were we both consultants for a computer company in Boston.
*  And we were I was insisting that we try to do something useful and we try to invent a quantum randomness chip.
*  And so we tried to think about how would you make, you know, in those days, one gigahertz seemed like an impossibly fast rate for this chip.
*  You know, how would you make quantum randomness that one gigahertz.
*  And what we realized is, you know, you have this little quantum effect.
*  But then when you measure that effect, you have to amplify it into a sort of classical number of degrees of freedom.
*  And that process in order for you to have an unambiguous result in order for successive bits that you measure to be uncorrelated, you have to essentially have essentially sort of a thermodynamic phenomenon going on.
*  You have to be you know, it has to randomize.
*  Then that that randomization has to not be correlated with the next thing that happens.
*  And that was that that was to me the first sort of sign that there was going to be a cost to measurement, so to speak.
*  Well, if you if you start a podcast of your own, you can have me on and we can talk about interpretations of quantum mechanics.
*  And that would be fun.
*  But OK, you can teach me all about it.
*  But I mean, I think that that that does help me understand a little bit, because what you're what you're saying is that it's possible that your approach has a different attitude toward, let's just say, the measurement problem of quantum mechanics.
*  So the next obvious question is, do you have a different attitude toward the Schrodinger equation towards a unitary evolution?
*  I mean, the conventional Schrodinger equation is continuous in time and you're not continuous in time.
*  Are you getting the Schrodinger equation as an approximation or is there some sense of which it's exact?
*  Yeah, right. So so it's very similar and we don't know all the details of this yet.
*  But let's talk about the space time case in the space time case.
*  We've got these atoms of space and with connections and so on.
*  And we're looking at things on a large scale.
*  And what should happen is that just like in a fluid where the molecules are bouncing around, but on a large scale we get the fluid equations on a large scale, we should get the Einstein equations.
*  And that's what theoretically theoretically we should get.
*  Now, when I say theoretically, this is, you know, when physicists do mathematics, they're really sloppy.
*  And, you know, there are many, many ways to be taken of, you know, it's these these.
*  There's a certain amount of computational reducibility, which leads to a certain amount of randomness, which leads to certain statistical averages working out in a certain way.
*  When you look at the, you know, the distances have to be large compared to the elementary distance between atoms of space and small compared to the size of the universe.
*  And the curvature has to be small, blah, blah, blah, blah, blah, a whole bunch of conditions.
*  But with all of those conditions and physicists level mathematics, we can derive Einstein's equations.
*  Now, it's worth pointing out that the effort to derive the fluid equations from molecular dynamics has been unsuccessful for 100 years.
*  That is, with a level of, you know, we can derive Einstein's equations with the same level of kind of mathematical rigor that you can derive the fluid equations, which is to say it isn't really mathematically rigorous.
*  But if you take all kinds of limits that that one advantage that we have actually one big advantage that I always forget is that we've done endless simulations.
*  We actually know what limits work and what don't.
*  Right. So it's not like it's just let's hope this works based on some mathematical sort of hope.
*  It's like we ran an experiment with a billion cases and this is what happened.
*  So we can kind of check those assumptions.
*  But OK, so what then happens is what we are saying is that the from this kind of microscopic atoms of space thing, when we do that, when we look at that on a large scale,
*  we reproduce Einstein's equations.
*  So one of the things that we've been doing recently, Jonathan has been much involved in this, has been saying, well, what about practical numerical relativity?
*  So people study, you know, black hole mergers and they do that by taking, you know, the structure of the black holes and they say we have Einstein's equations, which are partial differential equations.
*  And then we will. But in order to make those work on a computer, we have to discretize them because a computer deals digitally with sort of digital elements.
*  And so then you make numerical relativity where you've made some kind of mesh that represents some approximation to space time as, you know, approximating the space time of Einstein's equations.
*  So that's kind of the traditional approach.
*  Now, what we're doing instead is to work upwards from the atoms, so to speak.
*  So we're saying instead of going down from the Einstein equations, just come up from this kind of structure of this this hypergraph and and look at, you know, what is the aggregate behavior of all these atoms of space?
*  The neat thing is that it actually works and it's a practical method for doing numerical relativity.
*  So and in fact, it's looking really promising to as a and what's interesting.
*  So this is now a general relativity, just a side comment for general relativity.
*  So one thing you can ask is so obviously in our simulations, the we have these atoms of space and we simulate on a computer.
*  So I think the extreme kind of amusing version is Jonathan has been doing all these simulations on his laptop just to prove that that's possible, which I think is totally crazy.
*  Yeah. But so he has these simulations of black hole mergers and things done on his laptop using our models.
*  You could do a lot better if you weren't just using a laptop.
*  But anyway, the the the thing that is so it's not obvious that we would be able to get enough approximation to continuum space just kind of on a laptop from our atoms of space rather than having to go, you know, many, many, many orders of magnitude.
*  But it seems that that works.
*  So the next question is in physical space, where might we see evidence of discreteness in space time?
*  So in other words, the in other words, is there a way of making essentially a gravitational microscope that will see into the structure of space time?
*  And so one of the things we've looked at is rapidly rotating black holes right close to the critical, you know, close to J equals M.
*  What happens?
*  And it's pretty neat because in these in these simulations that Jonathan has, what you see is the thing eventually as you go above the critical angular momentum, critical spin rate for the black hole, a piece of space simply separates.
*  So, OK, another thing to explain is in our models of physics, this network doesn't have a built in notion of dimension.
*  So, you know, our experience is space is three dimensional, but this network doesn't have any particular number of dimensions that are built into it.
*  It can be the case that on a large scale, it approximates three dimensional space.
*  But because it doesn't have a fixed number of dimensions, because it isn't microscopically a manifold, so to speak, it can do things like it can change its topology.
*  Things can there can be tears that form in it.
*  There can be holes that form in it and so on.
*  And or more extremely, there can be pieces of the universe that just break off.
*  And so what we see happening for critical, super critical black holes is a piece of the universe just breaks off.
*  And as as the critical angular momentum, what you see is that a piece of the universe is hanging by a thread.
*  And so there are these small number of causal edges that essentially connect one part of the universe to others.
*  And so it's conceivable that we may get some kind of signature, maybe in gravitational radiation of that discreteness, you know, in physics terms, probably shot noise associated with the fact that there is a that there are a small number of causal edges.
*  That are associated with that with that situation.
*  So anyway, that's but that's just the general relativity case in the quantum mechanics case.
*  You're asking about the Schrodinger equation.
*  So the Schrodinger equation has to emerge as a pile of limits from the things that we're doing, because the Schrodinger equation is a non relativistic limit of etc, etc, etc.
*  So the answer is, I think I mean, I'm sorry, just to be just to be super clear.
*  I'm using the generalized version of the Schrodinger equation that would be just as true for quantum field theory and relativity and everything just H psi equals ID by DT psi unitary evolution of function.
*  Right. So so we are from the setup of these multi-way graphs from the interpretation of quantum amplitudes.
*  We are guaranteed unit unit or evolution.
*  100% not as an approximation.
*  That that you think about that for a second.
*  It's a little tricky because you have to define what the initial and final states are.
*  And if you if you say I have the whole multi-way graph of everything, I think you're guaranteed it.
*  But if you say if you say I'm going to make an I'm going to look at a particular region of space time, I think it's not so obvious.
*  I think there is an approximation.
*  That's that's just true.
*  And even in the regular Schrodinger equation, so that I'm perfectly.
*  I think that I think let me think about that for a second.
*  I think that.
*  Let me see.
*  I mean, quantum measurement is not unitary.
*  That's a that's a thing that we that we have to deal with.
*  But a many worlds person says that's just because you're only seeing part of the wave function in exactly the same way that you are right.
*  Right. But I'm a little concerned about the statement that the.
*  See the the statement about the way the Hamiltonian appears there in the in the non relativistic Schrodinger equation is certainly not what we're seeing.
*  So because we have a you know, our thing is sort of relativistic from the get go.
*  And so what I think let me think about this for a second.
*  Well, you could define it in terms of the path integral.
*  I mean, it's any unit evolution from one one wave function to another one quantum.
*  I think between an initial hypersurface and a final hypersurface, I think you inevitably get unit revolution.
*  But you have to define what those hypersurfer says are as you do and you know, as you do when you merge relativity and quantum.
*  General relativity and quantum mechanics.
*  So I think it's I'm I'm I think that's right.
*  I would have to I mean, the part of this.
*  Yeah, I think that that has to be that way.
*  OK. I mean, the part that we've been interested in recently is can we make a practical scheme for doing quantum field theory in the same way that we can make a practical scheme scheme for dealing with Einstein's equations.
*  And so in a sense, you know, one of the things that encourages me in this project is what I might call proof by compilation.
*  That is the fact you say, do you really get Einstein's equations?
*  Well, we can do numerical relativity and it actually works and we can do, you know, black hole mergers and things.
*  So if Einstein's equations are right, then what we're doing is the same.
*  And in quantum mechanics, we've been able to do this compilation of quantum circuits.
*  The next big challenge is to do quantum field theory and to do and to be able to do things like few particle quantum mechanics and those kinds of things.
*  You know, for example, let me give you an example of how things get a little bit complicated.
*  So in quantum mechanics, you know, a very traditional thing is the harmonic oscillator, just kind of the analog of, you know, things bouncing on a spring back and forth.
*  In order to get that in our models, you have to have closed time like curves.
*  So in other words, to get a perfect harmonic oscillator, it's very easy to have a perfect harmonic oscillator if you have closed time like curves.
*  In other words, if the if the history of the universe recapitulate, if the history of the universe repeats itself, that's kind of how you get something like a harmonic oscillator.
*  That's how you get the idealization of a harmonic oscillator.
*  Now, in the real situation in physics, we probably don't believe that there are perfect harmonic oscillators.
*  We can decompose quantum fields into, you know, as let's think of it as a sum of harmonic oscillators.
*  But we're not imagining there's a perfect harmonic oscillator here.
*  But if you say you might say and this is relates to the kind of reverse engineering versus building from the ground up, so to speak.
*  You might say, gosh, how can you think you have a model of quantum mechanics if you can't even have the harmonic oscillator?
*  But well, we can have a harmonic oscillator, but it's a weird idealization, which in our models shows up with with closed time like curves.
*  And so that's you know, that's an example of how things get a little, you know, if you insist on these ideologies, you end up sort of stressing as I think you should.
*  You kind of stress the model. So it's similar to, you know, if you said you say I'm studying molecular dynamics.
*  OK, so then somebody says, well, why can't you get rigid body mechanics?
*  Why can't you get, you know, this thing with a solid object that just moves around and doesn't distort?
*  Well, that's a complicated limit of molecular dynamics that involves, you know, in atomic forces are large compared to the forces on the whole object.
*  Blah, blah, blah. You know, it's it's that's a complicated story.
*  And I think we're seeing some one of the things that's difficult about our model is that it attempts to be a model for everything.
*  So you don't get to say we're going to have this piece we're going to make a model for that piece we're going to idealize away.
*  You have to kind of everything has to come together.
*  And that means that seeing things like how does the harmonic oscillator work?
*  It's a weird idealization. Yeah, that does make sense.
*  If you get exactly unitary evolution, that is to say you get something like the Schrodinger equation.
*  I mean, a many worlds person will say all there is is the Schrodinger equation.
*  You just need to pick the Hamiltonian and someone like me.
*  If I can indulge myself, you know, our project is to start from nothing but a Hamiltonian expressed as a list of energy eigenvalues
*  and show how there is an emergent geometric structure that looks like a graph.
*  You get Einstein's equation and the whole thing.
*  It's similar in spirit in that sense to what you're doing.
*  But so then the question is, if you exactly get unitary evolution,
*  what is the benefit to not just starting with quantum mechanics in the Schrodinger equation versus starting with hyper graphs?
*  Well, because you have a whole structure that you're building.
*  So, I mean, for example, when you say what's the Hamiltonian, you know, that better come out of our model.
*  So, for example, you could ask, which we haven't discussed, what is energy in our model?
*  This is one of the things that surprised me.
*  I thought energy was going to be a very difficult to derive idea that was going to require notions of what particles are and so on and so on.
*  It seems that energy is very simple.
*  It's basically the amount of activity in the hyper graph.
*  And a little bit more formally, it's the flux of causal edges through space like hyper surfaces.
*  And it's concerned. It needs to be said.
*  So, a causal edge is a causal connection between two updating events.
*  And so the question is, if you have a... you have to say it a little bit more carefully,
*  because if you say it's the density of activity, it's what the heck does density mean when we don't have a notion of space yet?
*  So, the more formal thing is energy is the flux of causal edges through space like hyper surfaces.
*  Momentum is the flux of causal edges through time like hyper surfaces.
*  And actually, you now make me wonder, and I don't think I know the answer to this,
*  what is the flux of edges through branch like hyper surfaces?
*  I should know the answer to that, and I don't immediately know.
*  And that's related to...
*  OK, so the point here is, there's a...
*  I think... see, one of the things that's interesting in our models is the relationship between quantum energy and classical energy.
*  Because in our models, it's this notion of... in classical energy, it's the...
*  you know, you've got this single thread of history, you've got this causal graph associated with that thread of history,
*  and you're asking this flux of causal edges.
*  But now you can also have this multi-way causal graph, which not only has space-like separation of events,
*  but also branch-like separation of events.
*  So, events can be separated in branch of space and in physical space.
*  And then the idea is that quantum energy is that activity in this whole multi-way graph.
*  So, it's the amount of activity in the multi-way causal graph.
*  And so then, like the Lagrangian, is this relativistically invariant...
*  This is the... you know, the Lagrangian density is that kind of...
*  you know, relativistically invariant notion of the amount of activity in this multi-way causal graph.
*  And so, for example, one little mystery that this seems to clear up is the thing...
*  if you look at the Planck length, you know, the characteristic length people often talk about
*  for where sort of quantum mechanics and gravity have to kind of come together.
*  In our models, the elementary length is much smaller than the Planck length.
*  And a typical thing is the Planck energy...
*  whereas the Planck length is, you know, 10 to the minus 34 meters or whatever it is,
*  the Planck energy is 10 to the 19 electron volts, if I remember correctly.
*  GEV.
*  What's that?
*  10 to the 19 GEV.
*  GEV, okay. Thank you.
*  Thank you.
*  But it's about the energy in a thunderbolt or something, a lightning strike.
*  It's huge. Not a very small quantum thing.
*  In our models, the elementary energy is also small,
*  because the elementary energy is an individual causal edge in the multi-way causal graph.
*  And the fact that what you observe is this thing...
*  the analog of the Planck energy is something that has been averaged,
*  that has been sort of summed over all possible branches in this multi-way causal graph.
*  Maybe this is a footnote. Forget this footnote.
*  This is just a part of the story.
*  But so you're saying, why do we care about this whole structure that we're building?
*  Why not just put a Hamiltonian in there?
*  And what I'm saying is, for listeners who don't know this,
*  the Hamiltonians and Lagrangians are closely related.
*  I think for you and me, that's pretty obvious.
*  But that may not be obvious.
*  But in some sense, like we said, there's a simple set of rules that you start with.
*  Maybe I can just jump...
*  I'm going to try to guess what you're thinking here,
*  and then you can tell me whether I'm right or wrong.
*  There's an infinite number of Hamiltonians I can write down,
*  but at least for simple ones, there's a finite set of little rules
*  that we can write down for our hypergraphs.
*  So maybe there's a map from the set of rules to Hamiltonians,
*  but it's a very, very few-to-few rather than covering the whole space of possible Hamiltonians.
*  Right. Well, so this is a good question.
*  As you look at simple rewrite rules for hypergraphs, you get some set of Hamiltonians.
*  If you say, oh, I'm going to have a million line program to represent my rules for the hypergraph,
*  you're going to get some other...
*  You can kind of custom engineer whatever Hamiltonian you want, probably.
*  Got it. Okay.
*  So it is not self-evident what kind of Hamiltonians you get from simple update rules we don't entirely know.
*  So, for example, it looks like we get ones that show local gauge invariance.
*  And then we have to ask...
*  And that's a...
*  If you just pick your average Hamiltonian,
*  there's no particular reason for it to have local gauge invariance.
*  But in our models, it probably does.
*  And so that's a good sign.
*  Now, will we get...
*  What other attributes will we like our Hamiltonians for the universe to have?
*  Well, I mean, my approach here is to just say, let's see what we get.
*  For example, okay, so here's one of the complicated things.
*  So the Hamiltonians that you will typically write down in quantum field theory,
*  they are...
*  The things that are in those Hamiltonians, Lagrangians, whatever, are quantum fields.
*  They're quantum fields that represent
*  field operators that correspond to particular particles.
*  So there'll be an electron quantum field, there'll be a photon quantum field, and so on.
*  Now, in our models, we're not yet talking about particles.
*  So those Hamiltonians have to be...
*  What we have is a description of things at a much lower level
*  than a place where you've got actual field operators for particles.
*  So for us, what are the particles?
*  The particles are locally stable kind of deformations in this hypergraph.
*  So, for example, in analogy and fluid mechanics,
*  if you say, what's like a particle in fluid mechanics?
*  Well, a vortex, a whirlpool-like thing in a fluid that is locally stable,
*  and it can move through the fluid and it can interact with other vortices.
*  It's something vaguely similar to that in our hypergraphs,
*  more a kind of topological structure that is some kind of not-yet-very-well-understood feature
*  that is locally stable under the rules.
*  And so when you talk about field operators,
*  those field operators that would occur in your average communal garden particle physics, Lagrangian,
*  those field operators are effective descriptions of these deformations,
*  these topologically stable objects in this hypergraph.
*  The hypergraph is a lower-level description.
*  And so it's not obvious, and it's a very good question, and we don't know.
*  How does the thing that looks like it operates in terms of particles, how does that emerge?
*  What kind of things that look like they're in terms of particles emerge from this lower-level structure?
*  Because in our models, all we have at the beginning is the structure of space.
*  Particles are just features of the structure of space.
*  And so there's an underlying dynamic.
*  I mean, one of the things that's sort of a little shocking in our models
*  is that most of the activity of the universe is associated with the maintenance of the structure of space
*  and has nothing to do with all the particles that we observe in space.
*  So it's a very reasonable question how the Hamiltonians that we're used to in particle physics
*  emerge as effective Hamiltonians from this underlying dynamics, and we don't yet know the answer.
*  Well, you mentioned the particles as something that does come out as these persistent structures.
*  But as you certainly know, quantum field theory, the usual modern physics way of saying things
*  is that fields are somehow more fundamental.
*  When you perturb them and excite them, you get particle-like things.
*  There are circumstances, like the condensation of the Higgs field, where the particle language is not appropriate.
*  Is there a view toward a more field-like ontology coming out of this?
*  Well, I think that, okay, so again, if we say when we talk about particles in particle physics,
*  they are, as you say, sort of what we imagine is, oh, there's a particle.
*  It's not interacting with anything. It's separated from everything else.
*  It has a definite momentum. It is a definite mode of the quantum field.
*  And when it comes close to other particles, then it gets more complicated,
*  and there are other modes of the quantum field that get excited, and eventually some other particle goes out,
*  and you observe it in a particle detector.
*  So for us, we have to think about what do those scattering experiments look like?
*  What is an experiment where you have that separated particle,
*  and this is one of the cases where we are building everything from the ground up,
*  so we don't get to say, oh, it's just a separated particle in the vacuum, so to speak.
*  It's an excitation of some kind embedded in the space that has a lot of activity in it.
*  So for example, when we talk about, so one of the things that I'm wondering is,
*  will there be bizarrely different kinds of stable structures in our hypergraph
*  that aren't like the particles we're used to?
*  So in other words, you mentioned the Higgs field.
*  The Higgs field is a case where we have this condensate,
*  where we have a sort of uniform value of the Higgs field throughout space.
*  And that's a simple case. There are people who know about soliton type solutions to field equations,
*  and there are other kinds of things like that.
*  And one of the possibilities is that in our models,
*  particularly because we have this dimension variation,
*  that there might be bizarrely different stable structures that could exist in the context of our models
*  that don't seem like particles of the ordinary kind, but that one, MENSA, and things like that,
*  might be something bizarrely different.
*  Maybe it's even related to something, you know, maybe it's related to dark matter for all we know.
*  I mean, it's just something that could exist as a sort of stable feature of our universe
*  that goes beyond just the structure of space,
*  but it has a form that we don't yet understand.
*  And I think, I mean, the other thing to realize,
*  so in standard particle physics, we talk about virtual particles.
*  You know, there are always these particle-antiparticle pairs
*  that are sort of popping into existence in the vacuum for a very short time and then annihilating.
*  And one of the features of that, it's always been somewhat mysterious in quantum field theory,
*  because quantum field theory says there's an infinite number of these virtual particles
*  that are occurring all over the universe,
*  and that corresponds to effectively a very high energy density of stuff in the universe.
*  How can that be? How can it not, in Einstein's equations, say, you know,
*  whenever you have energy, you're going to curl up the universe with, you know,
*  gravitational attraction associated with that energy.
*  How can the universe not curl up into a tiny ball because of these vacuum fluctuations of virtual particles?
*  Well, in our models, the sort of limiting case of those virtual particles
*  is these actual rewrite rules in our hypergraph.
*  So, in other words, the sort of the ultimate version of all of those virtual particles
*  is just all these little rewrite rules in the hypergraph,
*  which in our models are exactly what create the structure of space.
*  So, in a sense, that makes it a little less mysterious
*  that, you know, all of this virtual particle stuff doesn't have this terrible effect,
*  this terrible gravitational effect on the universe.
*  Now, you can ask things like, you know, can you imagine how the Higgs mechanism works
*  and all these kinds of things? And yes, I've thought about that.
*  And there's a certain amount you can say. I don't think we can't.
*  I mean, I was very disappointed when the Higgs particle was discovered.
*  I kind of knew it was going to happen.
*  But it was kind of like, it's kind of a hack.
*  And it's disappointing that, you know, it looks so far the Higgs mechanism looks like a hack.
*  And the question is, can we make it look less like a hack?
*  And that will be really neat.
*  So, one little footnote is that you might be interested in work by Tom Banks and Willie Fischler,
*  who have emphasized within the context of more or less conventional quantum gravity
*  the point you just made about the cosmological constant,
*  that we should not think about it as the sum of all these virtual fluctuations.
*  We should think of it as an input, a boundary condition, they call it,
*  that just sets the size of space in some sense.
*  So that's more in line, I think, with the philosophy that you're thinking of.
*  I knew Tom Banks when we were both at the Institute for Advanced Study in probably 1980 or something.
*  I haven't... Great. I'm glad he's doing interesting things.
*  And then the other point was, I mean, I don't want to dwell on all of these,
*  but I presume that if your program pans out,
*  we will want to find solutions to the classic puzzles of particle physics.
*  So not just the cosmological constant problem, but the hierarchy problem,
*  the strong CP problem, baryogenesis.
*  Are these the kinds of things...
*  I'm guessing that I would have heard already if you would solve them,
*  but maybe are they solvable, you think, within the program?
*  You know, eventually they should be.
*  I mean, we can start teasing apart what each of them involves.
*  I mean, you know, the, oh, there are three generations of particles,
*  and, you know, the question is what's generic and what's not.
*  So the surprise for me is that general relativity and quantum mechanics seem to be generic,
*  just as thermodynamics is generic.
*  And the question is, how far does the genericity go?
*  Because I wouldn't have expected...
*  Well, for example, I wouldn't have expected the detailed form of Einstein's equations
*  to be as generic as they seem to be.
*  So, and, you know, it could be...
*  I have this vague suspicion that the structure of the local gauge group might be generic.
*  I might be completely wrong about that.
*  Yeah, well, you can hope.
*  I don't think the three dimensions of space are generic.
*  I don't think the three for the three dimensions of space is generic.
*  Whether the, you know, there are bizarre possibilities,
*  like, you know, maybe the two threes are related, you know,
*  the three generations and the three dimensions of space.
*  Maybe, you know, and I don't know.
*  I mean, that's a... These things are all certainly possible.
*  I think that when it comes to things like...
*  Well, one example is CPT invariance.
*  So that's the question of why is there CPT invariance,
*  and I can explain a little bit about that.
*  We don't know completely.
*  I mean, so in sort of in the stack of things you need in particle physics,
*  a big feature of particle physics is fermions versus bosons.
*  You know, particles like electrons, but a fermion,
*  then have the exclusion principle, don't want to be together,
*  versus photons, which are bosons, and are very happy to be together.
*  And those are distinguished by the spin statistics theorem says,
*  if you are half-entered spin particle, then you will be a fermion,
*  and if you're an integer spin particle, you will be a boson.
*  So, one question is, what are fermions and bosons in our models,
*  and can we derive the spin statistics theorem?
*  And that's an example of a sort of a...
*  You know, one of the achievements of quantum field theory
*  is the derivation of the spin statistics theorem.
*  And so, for us, fermions versus bosons, we have a guess.
*  We're not sure.
*  The guess has to do with...
*  In these multi-way graphs, we suspect that bosons are associated with,
*  in a sense, branchings that merge very quickly,
*  and fermions are associated with branchings that do not merge quickly.
*  And so, that's what leads you, in a sense,
*  the branchings that don't merge quickly wind up with opposite sides of branchial space,
*  things that can't happen effectively, or things that are not observed to happen.
*  And, in fact, at a mathematical level,
*  it is...
*  You actually will then sort of see the fermions are kind of the square root of the bosons,
*  because the fermions are... It just branches.
*  It doesn't do the... It doesn't merge as well,
*  whereas the bosons are both in branches and it merges.
*  And so, now the question is, can we relate that to rotational symmetries
*  that are associated with the spins and so on, and looking promising.
*  Not done yet, but looking promising.
*  So then, if we can do that, then we can derive the spin statistics theorem.
*  And then the next question is, well, CPT invariance, just to explain for people,
*  this is a fundamental symmetry that's believed to exist in quantum field theory,
*  is if you turn particles to antiparticles, you reflect space, and you reverse time,
*  then you'll always get something where the laws of physics work the same way.
*  So, for us, again, it's kind of neat, because it seems like C, charge conjugation,
*  which is particle to antiparticle, is effectively like...
*  It is an inversion in branch-field space, it seems to be.
*  In other words, it's a reflection in branch-field space.
*  Parity is a reflection in physical space,
*  and time reversal is a reflection in time.
*  And so what this is saying is, in the end, that our multi-way causal graph
*  is invariant under a reflection in all three of those directions, so to speak.
*  So, it's at least a very clean formulation of what it means to be CPT invariant.
*  Whether we have not yet shown that we necessarily get CPT invariance,
*  but at least we know what it corresponds to.
*  But that gives some sense.
*  So, when you ask about CP violation, for example, that's still a little ways away,
*  because we don't yet understand CPT invariance.
*  In regular quantum field theory, CPT invariance is tightly connected to Lorentz invariance,
*  the invariance under boosts and so forth.
*  I'm guessing that in a discrete graph model,
*  Lorentz invariance must be, once again, approximate, right?
*  And there'll be at some point, even if it's very, very experimentally inaccessible,
*  where it will break down.
*  Absolutely. There is a maximum boost.
*  You can't get, you know, there's a, in other words,
*  as eventually you start seeing the granularity of space-time.
*  So, you can do, and so, yes, the relationship between,
*  that is, in fact, the derivation path that we're aiming for,
*  is causal invariance in the ordinary causal graph leads to ordinary Lorentz invariance.
*  And the guess is that some kind of, that causal invariance in the multi-way causal graph
*  is associated with the essentially extension of Lorentz invariance that is CPT invariance.
*  So, that's the guess about how it works.
*  Right.
*  We don't know if that's really, and, you know, obviously CPT invariance
*  is a complicated story in general relativity and in non-flat space-time and so on.
*  And no doubt we will run into those issues.
*  There are very good experimental limits on Lorentz violation
*  from different propagation speeds of photons of different wavelengths from gamma ray bursts.
*  They can put limits up to the Planck scale, but as you said, your scale is much tinier,
*  so it might not be anywhere close.
*  Right. I mean, I think the thing that I'm most interested in with respect to those propagation experiments
*  is finding kind of dimension fluctuations in the universe.
*  Because in our models, you know, there's no reason for the dimension to always be three.
*  In fact, one of the things that's a possibility is,
*  so one of the more bizarre possibilities, again, not properly explored,
*  is that the Einstein equations are usually formulated in terms of change,
*  in terms of the change in curvature of space.
*  One possibility is you might be able to say the curvature is always zero,
*  but the dimension changes.
*  And it might be that there is some mathematical equivalence between those
*  for small curvatures, small dimension changes.
*  But, you know, one of the things that we suspect in our models
*  is that the universe started infinite dimensional
*  and only gradually sort of cooled down to be three dimensional.
*  And so that then a lot of the problems about, you know,
*  these horizon problems in the early universe and so on disappear,
*  because when it's infinite dimensional, everything is closely connected.
*  The graph distance between things is small.
*  Now, the suspicion from this is that as it cools down to be three dimensional,
*  there may be dimension fluctuations left over.
*  And so obviously, you know, the question is,
*  would those be visible at the time of recombination?
*  And we see that in the cosmic microwave background.
*  Of course we don't know, but the first question is,
*  what would a dimension fluctuation do to the cosmic microwave background?
*  And then if there was a dimension fluctuation that exists in the current universe,
*  what would it do to the propagation of a photon through that dimension,
*  that region of dimension fluctuation?
*  And this is a piece of, in a sense, classical physics
*  that I keep on meaning to work out,
*  and I keep on hoping somebody else is going to work it out,
*  and it's kind of like I've been collecting this inventory
*  of laws of physics in d dimensions.
*  Well, I think, I mean, I'm just guessing here,
*  so I haven't thought of it myself,
*  but if the effective dimensionality space is not exactly three,
*  Coulomb's law would not be exactly true,
*  and wouldn't that have dramatic effects on QED scattering rates?
*  Well, the question is something like the Thompson cross section, for example.
*  How does that depend on...
*  I am...
*  Well, you're correct that in d-dimensional space...
*  So the way to think about it, I think,
*  photon propagation is using Huygens' principle,
*  where you're saying that every...
*  On this wavefront of a propagating light wave or whatever,
*  every point on that wavefront is a source of a spherical wave
*  that is going to build up the next piece of the wavefront.
*  And if you are in d-dimensional space where d isn't three,
*  those little spherical waves have a different...
*  There's a different density on those spherical waves,
*  so to speak, when you project them into three dimensions.
*  That's at least my thinking about how to do this.
*  Now, the question is...
*  So the question is...
*  So in particle physics, back when I used to do particle physics
*  a long time ago, I was a big enthusiast of this method
*  called dimensional regularization,
*  which is the idea that, you know,
*  while you're doing an integral,
*  if the dimensionality of spacetime is four,
*  the integral diverges horribly.
*  But if we can only say it's four minus epsilon,
*  we can do the integral,
*  and then we take the limit epsilon goes to zero at the end.
*  So I'm sure I've worked out back in the day
*  what the low-energy electron-photon scattering cross-section
*  is in d-dimensions.
*  And that would be a good case to look at.
*  I mean, I think that I will not be surprised
*  if there is some fairly sensitive test
*  of the dimensionality of space.
*  For example, I don't know, and I've been meaning to look it up,
*  what the anomalous magnetic moment
*  of the electron or the muon...
*  You know, it's one minus alpha over 2 pi,
*  but that certainly depends on the dimension of space.
*  I just don't know how.
*  Yeah, there's probably some high-precision particle physics experiment
*  that is sensitive to that.
*  So, okay, I think I only have two questions,
*  but they're both huge questions,
*  so I suspect they're going to take more than two minutes each.
*  But one of them is you referred to this idea
*  that in the early universe
*  maybe we have some bundle of dimensionality
*  or dimensionality is not well-defined,
*  and that sort of comes out in the wash as the evolution happens.
*  So I've thought very much about the arrow of time problem,
*  but I've thought about it in the context of
*  fundamentally reversible directionless laws of physics,
*  which is a little bit different from where you're coming from.
*  So for me, the huge question is,
*  we're evolving toward an equilibrium,
*  empty space situation
*  where all the galaxies are all dissolved around
*  and we have nothing around us but the cosmological horizon,
*  and that's the highest entropy state.
*  But we came from, 14 billion years ago,
*  a very, very, very low entropy state,
*  and in conventional cosmology,
*  there's just no good explanation for that
*  except the papers I've written.
*  And even those are not universally accepted yet,
*  but it sounds like you have a possible,
*  completely different point of view
*  where it's just natural that you start
*  with what we would ex post facto label low entropy.
*  So I think the discussion about entropy is kind of confusing.
*  That's my first statement.
*  I remember having this vigorous argument with Dick Hyman
*  about this very topic,
*  whether the universe was, he made this claim,
*  the universe is a fluctuation.
*  The fact that we are in a state
*  where we're not kind of,
*  where we aren't at sort of the maximally disordered state.
*  And I kept on saying,
*  that's just a completely crazy claim
*  because it's like everything we know is a fluctuation.
*  So I think I would be more eloquent these days
*  than I was back in explaining why that was such a wrong idea.
*  But anyway, the first thing to understand is
*  that people say, oh, eventually the universe will kind of unwind
*  and there'll be nothing interesting in it,
*  there'll be no structure in it,
*  it will all just be in a high entropy state.
*  Okay, my claim is the reason you say that
*  is because you're not an adequate demon.
*  That is, in fact, in the future of the universe,
*  if it turns out that it all just seems like a gas in equilibrium and so on,
*  that you might say that's completely boring,
*  that's all just random, it's the high entropy state.
*  But to another kind of observer, they might say,
*  but look at all those little details about what's happening.
*  This is the most amazing complex structure that you can imagine.
*  I mean, I happen to think if we ask,
*  what will we look back on this time in scientific history
*  and say how could those guys have missed this point?
*  My guess is one of the bigger things will be
*  when people describe something like a gas in thermal equilibrium,
*  they just say it has a certain pressure and temperature.
*  They don't consider any other features of the gas.
*  They don't say, oh, it's got these little microscopic things
*  that we can measure in this way and that way.
*  But my guess is that there are a lot of other features.
*  Now, this question of are they computationally boundedly observable,
*  are they measurable by a computationally bounded observer,
*  I don't know the answer to that really.
*  But the claim I'm making is that when you say it's going to a high entropy state,
*  you're saying, oh, all you're saying is,
*  so I as an observer, the kind of observer I am,
*  can't make anything out of it other than to say it's uniform and random.
*  I think I'm actually saying more than that.
*  I think in this case I'm going to disagree with you
*  because I think that it actually goes to the vacuum quantum state,
*  the Bunch Davis vacuum of decider space.
*  It's a dissipative system because there's a horizon around us
*  and within our horizon all the excitations above the vacuum go away
*  and there's no structure there to be seen by any observer computationally bounded or otherwise.
*  What do you think is in the vacuum?
*  Well, it's a single quantum state, thinking in quantum mechanical terms.
*  It's a unique quantum state, the lowest energy state.
*  So I would claim that's the mistake.
*  It may be interesting to try and take that apart.
*  So in our models, the very fact that there's space there,
*  space is a thing in our models.
*  You have to make space.
*  You don't just get to say, oh, there's this big area of space.
*  Space is made of something.
*  And in our models, space is made of this sort of teaming collection of atoms of space
*  doing all these complicated things.
*  So our vacuum cannot be just the boring, there's nothing there vacuum.
*  Our vacuum has to have a lot of structure in it.
*  Now, if you ask the question, if you say every particle excitation has gone over the horizon,
*  that's what you're basically saying.
*  So let's think about that for a second.
*  What does that mean?
*  In our models, so horizons in our models are visible in essentially breaks in the causal graph.
*  So the causal graph says this is the, you know, causal effects can propagate between these,
*  between these, this event can affect this event, can affect this event.
*  And you make these light cones where one event is having an effect on a whole sort of increasing size
*  cone of other events.
*  So what is an event horizon?
*  An event horizon is, and you literally see this in our models when you run them,
*  and like these black holes, you can literally see the event horizon.
*  And it's a place where the causal edge is, for example, in a black hole, the causal edges go one way.
*  Causal edges go in and they can't come out.
*  And that's, it's very concrete.
*  And so a cosmological event horizon is something where you're separating in the causal graph.
*  You have two different regions of the causal graph, and they are, you simply have no causal edges
*  that go from one side to the other.
*  So what you would be saying is, what you're claiming is every particle excitation has,
*  somehow is in a region of space that is causally disconnected from the region of space that we care about, so to speak.
*  So I think my statement would be, I mean your claim is an interesting one,
*  because basically what you're saying is that all the big particle excitation,
*  all these sort of identifiable topological excitations will be gone and outside of this event horizon.
*  Now what I would be saying is that in order for there to be space inside there, there still has to be stuff going on.
*  Now what this turns into is an argument about is there stuff, is there useful stuff in that region of the universe?
*  And by useful stuff you might say it's this complicated topological structure that represents a photon.
*  But that depends on, and so you say the observer, an observer that you know about right now is observing things like photons,
*  is observing these big complicated topological structures.
*  But in terms of the pure underlying structure of the universe, you could still have all these little atoms of space doing their thing.
*  It's just maybe, maybe it's smoothed out enough conceivably that there aren't any of these sort of identifiable topologically stable structures that still exist there.
*  That's a possible kind of, and then the observer would have to be at the demon level, so to speak,
*  in order to observe that there's anything interesting happening there.
*  And not at a level, if the observer is made of particles, for example, is made of photons,
*  that might be the case that you couldn't get with an observer made of photons,
*  you simply couldn't get information about that more microscopic structure.
*  So I think we should postpone this to either an in-person conversation or me appearing on your podcast,
*  because it does get kind of technical at some point.
*  But I don't want to not give you an opportunity to talk about the beginning of the universe.
*  You talked about the end there.
*  But is there, I'm going to guess that you're going to say that there is a principled reason within this approach to start in what looks something like very roughly the Big Bang.
*  Well, OK, so the question is, in these models, this gets us into another, this is a deep rabbit hole that we're about to enter.
*  But let me say a few things about it, because it's something I've recently been thinking a lot about.
*  So, OK, so in these models, you might imagine that the universe starts as a fairly small hypergraph and gradually expands.
*  And so one of the mistakes I've been trying to not make is kind of a repeat of the Einstein mistake, so to speak.
*  Because in our models, the most natural thing is that this hypergraph just expands dramatically with time.
*  OK, and, you know, I'm not I have a great tendency, and this is kind of a reverse engineering type tendency to say, no, no, no, there's got to be these other rules that reduce the size of the hypergraph so that it doesn't expand insanely.
*  You know, just like Einstein was saying, well, you know, even though the Einstein equations predict the universe should expand, of course, we know it doesn't expand.
*  Except it turns out actually we discovered it does expand.
*  So I'm trying to not repeat that mistake.
*  But, you know, I think that the current expectation would be that just as there's a simple rule, so also there's a simple initial condition.
*  And that is a small hypergraph and which is something that doesn't really even define a dimension, because it's just a tiny little hypergraph.
*  And it starts expanding.
*  And at the beginning, that expansion is like, you know, is something which effect it has high dimension, then it goes down.
*  So one of the things we've been trying to do, which is probably more in your in your day job wheelhouse, so to speak, is we'd really like to know what the analog of the Friedman Robertson Walker model of the universe is for dimension change.
*  So we were pretty sure that there is a an analog for a homogeneous isotropic universe, that there's something just like the usual model, just as it's homogeneous and the universe is homogeneous and isotropic.
*  So what does the scale factor of the universe?
*  What does that?
*  You know, how does that how does that work with time?
*  We're pretty sure there's a directly analogous thing that describes dimension change in the universe.
*  And that will be the effective equations that describe in our models, the very early universe.
*  Yeah, I think there is actually sort of mention a couple of things for your benefit as well as for the audiences.
*  If you want to imagine you have a bunch of dimensions that start small and some of them start expanding, there's a very set of cute models from Brandenburger and Vafa based on string theory.
*  But they have a way why only three dimensions of space would start expanding.
*  It's basically because you can tie your shoes in three dimensions, but not in four dimensions, right?
*  Strings will generically intersect in three dimensions, but not higher numbers of dimensions.
*  So that was there.
*  I wrote that down. I'm going to look that up.
*  That's a fun one.
*  The dual of that, the converse, was actually by me and Lisa Randall and Matt Johnson, where we showed how if you start with higher dimensional decider space, you could actually create a sub universe with fewer macroscopic dimensions by spontaneously compactifying some dimensions.
*  So I think dynamically, given curved space time, you're allowed to go either way.
*  You can have them all small and let some grow or you can have them all big and let some shrink.
*  That's interesting.
*  The question is if it's homogeneous and isotropic, whatever the generalization of that for dimension changes, what I expect is that there's going to be some equation that eventually will have the dimension and the scale factor in it.
*  And it will be only those things.
*  So in the things you were just describing, there's presumably non-homogeneity because you're saying that there are some pieces, some dimensions that grow, some that shrink, and so on.
*  This would be kind of the homogeneous isotropic analog of that.
*  I mean, I think this is, in a sense, this is a quintessential, not particularly easy mathematical physics problem.
*  But it is, in a sense, it's the reason, one reason it's not easy and perhaps interesting to say is that calculus, which is what all of this stuff is based on, is a story of changes with respect to a variable like time.
*  But in our models, and when people do multivariate calculus, they're doing calculus with two variables or three variables, but they never get to do calculus with two and a half variables.
*  That's not a thing.
*  And nobody knows how that works.
*  And so in our models, what we effectively have to do is go below the level of where we talk about variables.
*  And we're actually, in our hypergraphs, you can think about a direction in the hypergraph as being like a variable.
*  So as you move through the hypergraph in a certain direction, that's like a variable.
*  But if the hypergraph is a big mess, it's not obvious what you mean by a direction.
*  If the hypergraph was a nice orderly, like, crystal-like thing, then you'd have a well-defined notion of direction.
*  But in the actual hypergraph, you don't.
*  And that's kind of where you begin.
*  I mean, there needs to be a generalization of calculus made that works in fractional dimensional space on these hypergraphs and so on.
*  And that's kind of the technical difficulty of this.
*  But that's interesting.
*  I'm going to look up that reference.
*  That's very useful.
*  Well, good.
*  And I think this leads actually very naturally into the final big issue I wanted to address, which is locality.
*  And you've talked a lot, I think, even though I never got to sort of specifically ask, I think you've done a good job of explaining how space time arises and Einstein's equation and general relativity.
*  And as you said, three dimensions doesn't seem to magically come out, but maybe we can figure that we get it with the right rules so that that's future work.
*  Good.
*  But locality is an interesting thing.
*  And when I say locality, I just mean the fact that in space, the laws of physics, for the most part, have the property that if you poke the system in one location of space, the effects ripple out locally, right, only to nearest neighbors as you go forward in time.
*  So that's one thing you might want to get out of an approach like yours is that you have this notion of locality.
*  Quantum field theory is based on locality.
*  But in the real world, there's at least two interesting places where we think locality breaks down.
*  One is in quantum measurement with Bell's inequality, right?
*  And the other is potentially in quantum gravity with the holographic principle complementarity, ADS-CFT.
*  So what is your feeling about how you can thread that needle of getting enough locality out of your rules, but also slight deviations from locality when you need them?
*  Okay, my current guess is the following.
*  In space and physical, in these hypergraphs, we are saying there's a certain clump of nodes in the hypergraph that have this structure, they get transformed into one with that structure.
*  That's in a sense local in space in the sense that it involves this local region of nodes in the hypergraph.
*  Now, there's two kinds of locality.
*  One is spatial locality, and the other is branchial locality.
*  In other words, is it?
*  And so my guess is, and the way that things like Bell's inequality, the violation of Bell's inequality, come out is through non-…
*  that branchial space is differently laid out than physical space.
*  Physical space, we know in this hypergraph that it's, you know, we are choosing to a rule that is local with respect to the hypergraph.
*  But the question of what counts as local in this, in branchial space, locality is a different story.
*  Locality is a story there of, well, it's just a different kind of thing because it involves these ancestry and the multi-way graph and so on.
*  So I think that the story there is locality in branchial space is a different issue.
*  And for example, you can ask, what's the analog of a light cone in branchial space?
*  So in physical space, you know, you make a perturbation somewhere, it expands at the speed of light.
*  What happens in branchial space?
*  Well, it also expands at finite speed in our models.
*  And that means there is a maximum entanglement speed in quantum mechanics.
*  And the value of that, we only have one parameter we really need.
*  So if we knew the elementary length or if we knew the elementary time or the elementary energy or if we knew the maximum entanglement speed,
*  any one of those parameters is enough to determine the length scale for our models.
*  But this maximum entanglement speed is saying in branchial space, you have a one vague estimate that we have is the maximum entanglement speed is 10 to the 5 solar masses per second.
*  I don't know if that's correct.
*  That's based on a very hokey calculation that I did, which makes a bunch of assumptions.
*  But it gives you some sense of scale.
*  If that was the right value, we would observe limitations on black hole mergers of big black holes or very rapid mergers that are associated with maximum entanglement speed rather than speed of light.
*  So in a sense, it's a limit of the rate of quantum measurement or the rate of quantum effects.
*  And so one question is, which we were just thinking about recently, is can we actually bound, in other words, in these violation of Bell's inequality experiments where you're looking at propagation of physical space
*  and you're saying it seems to happen instantaneously in physical space.
*  Well, the reason that's happening is because that propagation, so to speak, is actually happening in our models in branchial space, which is a different story than physical space.
*  But if we knew the maximum entanglement speed, we might be able to make bounds on that speed in physical space, which would mean that even though these various Bell's inequality entanglement experiments and so on
*  are much, they seem instantaneous, so to speak, that actually there might be a finite bound.
*  We're not sure about that yet.
*  I think it's probably not exactly the same, but this is certainly spiritually a similar answer to what an Everettian would give to the whole Bell's inequality question.
*  There's not a unique measurement outcome in space.
*  So the rules that Bell was assuming do not necessarily apply.
*  Right. I mean, I think that, so by the way, this maximum entanglement speed has all kinds of consequences.
*  So for example, you can have entanglement horizons. So you can have essentially a horizon in branchial space.
*  And so one of the things we suspect, we don't yet know, is that there's an entanglement horizon outside of the physical event horizon in black holes.
*  And so what that means is so far we can get black holes in our single thread of history, not dealing with multi-way causal graphs.
*  It's just a technically difficult thing to do the analogous calculation for a multi-way graph, but we think we'll be able to do that.
*  And at that point, we will see black holes that have an event horizon in physical space and an event horizon in branchial space.
*  And so the question is, and that is an interesting thing, because if you think about the propagation of information in the history of a black hole,
*  there's a question of can information be trapped between the entanglement horizon and the physical event horizon?
*  And so one of the questions is if you're an observer falling into a black hole, and when you're an observer falling into a black hole to the outside world,
*  time has stopped. And so the question is, what's the analogous thing that happens in the entanglement horizon?
*  And I think what happens is kind of cute. I think what happens is that the observer at the entanglement horizon cannot form a classical thought.
*  Well, sorry, from the observer's point of view, they just fall right through, though, in classical GR.
*  Yes, yes, right. But to a person, correct. So that is, to a person far away from the entanglement horizon,
*  they would conclude that the observer at the entanglement horizon could not form a classical thought.
*  So that means they could never, in the sort of traditional quantum mechanics world, they could never collapse the wave function.
*  And so what would happen is for them, they're observing some virtual particle pair. Did that electron go into the black hole or not?
*  Well, they don't know because they can't form the classical thought to determine whether it went into the black hole or not.
*  And so that's our kind of least qualitative thinking about the sort of black hole information paradox kinds of things in our models.
*  I would suspect that I know, I haven't worked on this, but Jonathan Gorard has worked a bunch on the ER equals EPR story in our models
*  and claims that he is about to produce an actual sort of explicit simulation of an ER equals EPR thing.
*  So that term, which has been, I mean, it's an imminent claim. So it will have to arrive.
*  That's fine. Maybe by the time the episode comes out. But it does remind me of a potential, and I promise this is the last thing, a potential quantitative question.
*  The entropy of a black hole is its horizon area divided by four measured in Planck units, according to Hawking and Bekenstein.
*  Someone like me would interpret that as saying that the black hole is described by a factor of Hilbert space with a dimensionality approximately E to that number.
*  But the Planck length is not fundamental for you. Is there any chance that you would be able to calculate the Bekenstein-Hawking entropy and get the right answer?
*  Yeah, that's an interesting question. So, I mean, in, you know, the notion of what black hole entropy is, what is entropy?
*  Entropy is basically a measure of the number of states, the number of microscopic states of a system consistent with the macroscopic thing that you identify as being the system, so to speak.
*  So this is basically saying, given this thing that we say is a black hole, how many possible microscopic states are consistent with this macroscopic observation that it is a black hole?
*  So I would think that we should be able to compute that. And let me think, how would we... Yeah, I mean, I can imagine how we would compute that.
*  And I think it will... You know, what we have to do... Okay, so in space-time, we can see these event horizons in the causal graph.
*  You can explicitly... I've even studied them a bunch, and you can see all kinds of exotic black holes inside black holes and all kinds of interesting and wild things that can happen.
*  But I started looking at the multi-way version of that. It's just computationally hard, because what's happening is you've got these... You know, it's for the exact reason you've got this big exponential in there.
*  You've got this, you know, all these different threads of history that you have to account for. And as I say, there is an optimization of this that another person working on this project, Max Piskanoff, has been working on for most of the last year, actually,
*  which is the theory of local multi-way systems, which are systems... So the idea is... Okay, so roughly the idea is the following. So you have... When you're looking at this causal graph that represents all these different events,
*  and they're happening through time, and you say, I'm going to take a slice of this causal graph at a particular... What I consider to be a particular moment in time, then I've got a structure of space associated with those causal connections and so on.
*  That is getting us a version of space. When we also have this multi-way graph, there are many different configurations for space.
*  But so there's this notion that I was calling multi-space, which is this thing where every place in space, there's also essentially this stack of multi-way possibilities.
*  And what's difficult is to understand... We can say, okay, there's this multi-way graph and the whole universe is one node in this multi-way graph.
*  Or we can say, we've got one path in the multi-way graph, and now we're going to look at what happens in space.
*  But the thing we're trying to do is to see how do we get a representation that knits those two things together, where we are looking at locality in space and essentially locality in branch-field space, and being able to have those two things combined.
*  If we can successfully do this, I'm pretty sure we can do essentially numerical quantum field theory.
*  And we can do it in the traditional way this is done. It's either Feynman diagrams or it's lattice gauge theory. Lattice gauge theory is an imaginary time, which is kind of not great.
*  And in this setup, we will be able to do it in actual time. And we'll be able to do it.
*  And then the question of whether we see sort of perturbation theory and Feynman diagram is a story of what happens with our topological excitations and so on.
*  That might be a more complicated story.
*  But anyway, that's a...
*  Yeah, I mean, the thing that's really, to me, just tremendously exciting about this whole thing is there's this underlying structure, and we keep on being able to figure out more and more stuff.
*  It's not easy to figure out these things.
*  But it's like nothing is...
*  We're not ending up running into something where we say, oh, my gosh, that's...
*  We just can't explain that. That's just a thing which just is totally orthogonal to what our models are saying.
*  And the other thing that's happening, which I think is that we keep on running into things which say, oh, that's just like causal set theory.
*  Oh, that's just like constructor theory or whatever. Oh, that's just like one of these other theories that's been developed.
*  And what's, to me, both intellectually and sociologically, a terrific thing is that the results that people have developed in these theories, like take causal set theory, for example, there's been kind of a mystery.
*  You're just throwing down events in space time, and you're saying, just look at the relationship between those events in a causal graph.
*  But there's been kind of a mystery. Why are the events thrown down in just such a way that you get Lorentz invariance?
*  Yeah.
*  Well, in our models, we have an algorithmic procedure for generating those events, which immediately gives you Lorentz invariance.
*  But yet, all the mathematics that people have done in causal set theory, which works on arbitrary collections of events in space time, can be applied to our models.
*  And so that's a really neat thing. And the same thing...
*  I mean, we've been in higher category theory is another very elaborate area of mathematics, which is, I mean, our stuff is a concretization, is a concrete instance of higher category theory and all kinds of results that exist in higher category theory that have been extremely abstract.
*  Basically, my test is I can now understand a bunch of these results, which I've never been able to do before.
*  So because they have a concrete instantiation. And one of the things which we are not going to have a chance to talk about here, but the question of which we sort of started to talk about is why this universe and not another one?
*  Why does this universe exist at all? That we seem to be able to have some things to say about.
*  And it turns out that it's all to do with this limit of higher category theory, which turns out to also be this limit of running all possible rules in a multi-way graph.
*  And these are things related to this thing called the infinity groupoid, which was introduced by this chap, Grofendeek, who was a very abstract, abstruse mathematician.
*  And I never thought I would have any reason to care about the infinity groupoid, except that it seems that it is the limit of a bunch of our models.
*  And it seems that it's deeply related to a lot of things about sort of why this universe and why does the universe exist anyway.
*  And just as a teaser of something we're not going to have a chance to talk about.
*  But one of the things that I've been excited about recently is just as we are making this sort of foundational model for physics, I would like to make a foundational model of mathematics.
*  And we're talking about the set of all possible rules for the physical universe. You can also talk about the set of all possible rules in mathematics.
*  And one of my recent conclusions is if we believe that the universe exists, which presumably we do, because that's a notion of existence that we are pretty familiar with,
*  then it necessarily follows that mathematics exists in the same way and that our doing of mathematics is kind of carving out pieces of this kind of structure that is all of mathematics in much the same way that we're kind of carving out pieces of the universe to observe.
*  That's a coming attraction as yet.
*  I mean, what I want to do is to find a bulk theory of mathematics in the same way that we have bulk theories like relativity and quantum mechanics and physics.
*  Well, I can tell you that it was just a couple months ago that we had a podcast episode with Emily Reel, a mathematician from Johns Hopkins, a category theorist, and we talked about the infinity groupoid.
*  Oh, good. Very good. We talked about the infinity groupoid, which tells me both that there's a unity to all of knowledge, but also there's plenty of room to go, which I think that everyone listening to this episode will definitely get that impression.
*  So, Stephen Wolfram, thanks very much for being on the Mindscape Podcast.
*  That was fun. Good stuff.
*  Thank you.
