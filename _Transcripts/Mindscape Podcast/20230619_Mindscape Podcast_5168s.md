---
Date Generated: June 07, 2024
Transcription Model: whisper medium 20231117
Length: 5168s
Video Keywords: []
Video Views: 23881
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2023/06/19/240-andrew-pontzen-on-simulations-and-the-universe/

It's somewhat amazing that cosmology, the study of the universe as a whole, can make any progress at all. But it has, especially so in recent decades. Partly that's because nature has been kind to us in some ways: the universe is quite a simple place on large scales and at early times. Another reason is a leap forward in the data we have collected, and in the growing use of a powerful tool: computer simulations. I talk with cosmologist Andrew Pontzen on what we know about the universe, and how simulations have helped us figure it out. We also touch on hot topics in cosmology (early galaxies discovered by JWST) as well as philosophical issues (are simulations data or theory?).

Andrew Pontzen received his Ph.D. in astronomy from the University of Cambridge. He is currently Professor of Cosmology at University College London. In addition to his research in cosmology, he frequently writes popular articles and appears in science documentaries. His new book is The Universe in a Box: Simulations and the Quest to Code the Cosmos.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 240 | Andrew Pontzen on Simulations and the Universe
**Mindscape Podcast:** [June 19, 2023](https://www.youtube.com/watch?v=TY84RIDcN1Y)
*  Hello everyone and welcome to the Mindscape podcast. I'm your host, Sean Carroll. We talk about
*  science a lot here at Mindscape. I don't think anyone could avoid getting that impression. But
*  you know, we talk about other things too. I do try to let people in on the details, the real-world
*  details of how science gets done. It's not always straightforward. It's a little bit less, it's
*  different, let's say, than the press release model, right? Like the way that we learn about
*  science is very often because some scientists have done something and then if it's a discovery,
*  experimentally, or like a really cool theory, they will have a press release or there'll be
*  newspaper or internet articles or whatever, or they'll write a book or have a podcast, etc. That's
*  not really how science gets done. Science is much more incremental, it's much more gradual, and
*  there's a lot of tools that people use. So today's subject matter is a little bit different. We're
*  talking about cosmology, but we're talking about specifically the role of computer simulations
*  in cosmology. Our guest is Andrew Ponson, who is a cosmologist at UC London over there in the UK.
*  He has a new book that just came out called The Universe in a Box, Simulations and the Quest to
*  Code the Cosmos. I love the topic because he talks a lot about the Big Bang, cosmology, inflation,
*  dark matter, etc., but the central organizing principle is how we use computer simulations to
*  do this kind of science. That's both crucially important because these days you can't, you know,
*  the theories are so complicated that you can't make very good detailed predictions with a pencil
*  and paper. You really need to use a computer simulation. And because that act, which seems
*  kind of innocent, let's just put it on a computer and simulate it, maybe it's not so innocent after
*  all. I mean, I don't mean not innocent in the sense of guilty, I just mean that maybe you have to think
*  about what exactly it is you're doing, what assumptions you're making, and what you're supposed to learn
*  from this. And that's what we will learn from listening to what Andrew has to say, especially
*  about, you know, you might think, let's put it this way, you might think that how hard can it be?
*  You take the equations, you take some initial conditions for your universe with some matter
*  and some gravity, put it on a computer and solve the equations. How hard can it be? It can be hard.
*  It can be subtle because the map is not the territory, the simulation is not exact. You're
*  going to be making choices along the way about which parts of the universe are important to
*  simulate, which parts you can kind of approximate. And I think that's the thing that Andrew does the
*  best job at it really, driving home. So this is a window into a crucially important part of modern
*  cosmology, but also implicitly a window into how science gets done in a very general sense. So it's
*  a lot of fun to learn about that, think about it. Let's go.
*  Andrew Ponson, welcome to the Mindscape Podcast.
*  Thank you. It's great to be here.
*  We're going to be talking about simulations, right? Putting things on the computer,
*  putting ideas on the computer and watching them go. I can't help but tell a funny story
*  right away because just as we're talking about this, there was a little Twitter kerfuffle because
*  there was a story that came out that people had done a simulation of artificial intelligence on
*  the battlefield. And they said the AI was trained to score points by killing people and there was
*  a human in the loop saying, you know, don't kill that person, don't kill that person, kill this
*  person. And in the simulation, the report said the AI realized that it would score more points by
*  killing its operators, that it would never be told not to kill people anymore. It turns out that was
*  completely not a simulation, at least not a simulation in the sense that we're talking about.
*  It was basically these guys thought it up, which doesn't quite count. So that's an opening. So what
*  counts as a simulation in this sense? Well, I think that's a great question because the
*  book interprets it quite broadly. So, you know, I think at the heart of it, a simulation is trying
*  to make a computer reproduce some kind of phenomenon. Now, the phenomenon might be in physics,
*  so it might be the way that the universe evolves, the way that galaxies grow within it, the way that
*  say black holes collide and make gravitational waves, or the way that exotic substances like
*  dark matter and dark energy sculpt our universe. It might be all of those things, or it might be
*  something really very different. So in the book, I'm arguing actually that we can think of things
*  like artificial intelligence as simulations. Now, they're not literally simulations of the
*  human brain. They're not kind of trying to reproduce the physiology of what's going on inside our brains,
*  apart from anything else, that's just way too complicated to fit on a computer right now. But
*  they're taking kind of loose inspiration from the way that we know that brains do work. And they're
*  taking that loose inspiration and trying to use it to reproduce something a bit like thought.
*  Right. So I think that that is a simulation. And I think one of the things that I really wanted to
*  do with this book is say that when we do a physics simulation, you might imagine, well,
*  that's a much more straightforward thing, right? We know the laws of physics in a way that we don't
*  know the laws of thought. So you might imagine, okay, well, you just take the laws of physics,
*  write down Einstein's equations, you do some clever maths to fit them on a computer, and you hit go,
*  and then you see what happens. But it's not like that at all. Because, I mean, in some ideal world,
*  we might imagine we want to do that. But we just cannot because the complexity of the universe,
*  it's the sheer size of the universe, its extent, but also its complexity in the sense of just the
*  sheer number of elements that are interacting, and the sheer range of different bits of physics
*  that are therefore involved. It means that doesn't fit on a computer. You cannot fit the universe
*  inside a computer. And therefore, even when we're doing physics simulations, there's a ton of
*  approximations and kind of human creativity and leaps of the imagination that go into even fitting
*  these things on a computer in the first place. So what is a simulation? In my mind, it's something
*  that's trying to kind of provide some guidance to the way the world or the universe or thought
*  works. But it's not kind of slavishly following some predetermined set of rules or anything.
*  There's a lot of creativity involved in being able to try and draw out that story.
*  – You did mention that it was on a computer as opposed to the guy who just thought something up
*  and called that a simulation. But we have to relate to the non-astronomers in the audience,
*  the wonderful story of the early galactic dynamic simulation with light bulbs.
*  – Yes, absolutely. So it doesn't have to be on a computer. You're absolutely right. And
*  I tried to kind of trace the origins of where did this idea of simulation come from? I mean,
*  it dates all the way back, in fact, to Ada Lovelace, who, when looking at kind of,
*  but before a computer was ever built, just thinking about the kind of operations a computer
*  could do, she actually came up with the idea of a simulation and the idea that it could try,
*  you know, starting to reproduce phenomena in the natural world. So it goes back at least that far,
*  possibly, I mean, arguably even further than that, but at least that far. And you're right
*  that there's this amazing story of people who tried to do simulations before computers were
*  available, including simulations of merging galaxies. So if you imagine that a galaxy is
*  made up of hundreds of billions of stars, but sometimes two of those galaxies, each with their
*  own hundreds of billions of stars, actually come together in our universe and smash together.
*  And because of the gravity, they don't just kind of pass through each other. The gravity kind of
*  glues them together all into one. So there was this eccentric astronomer who tried to reproduce
*  this in a laboratory before computers were available using light bulbs. So the light bulbs
*  stood in for stars. He didn't have hundreds of billions of them, obviously. That would be
*  impossible. So again, it's like a creative leap. Instead of having hundreds of billions of stars,
*  I'll just have a few light bulbs. I think he had around 70 light bulbs or so.
*  What year are we talking?
*  We are talking in, I think about the 1940s, if I remember correctly. So not that far off the
*  invention of the digital computer, but before it was available, certainly before it was widely
*  available. And so inside this laboratory, you kind of black out all other sources of light,
*  and you just have these shining light bulbs inside the laboratory. And then the kind of
*  masterstroke here is to realize the strength of the light coming from each bulb can be used as a
*  proxy for gravitational attraction. So because the intensity of light from any light source,
*  as you move away, it falls off. Technically, we're talking about the inverse square law here.
*  So it falls off in a very particular way. And it turns out that it falls off in exactly the same
*  way as a gravitational field falls off. So if you measure the strength of the light coming from these
*  shining bulbs, then that's like a proxy for the strength of the gravity. And then you can use that
*  as a kind of shortcut to calculating gravitational forces. And that way, kind of move the bulbs
*  around in your laboratory, measuring the light all the time. And it's an absolutely amazing paper
*  that results from this, showing the merger of two galaxies using this technique. It's something that
*  you could not calculate by hands. If you try to calculate this by hand, you would literally do
*  a lifetime of calculating to get to this answer. Did he learn anything from that experiment that
*  was sort of an interesting discovery? Absolutely. Yeah. I mean, I think it was unclear whether two
*  galaxies would just kind of run past each other or whether they would merge together if you kind of
*  set them on some kind of realistic track, on some realistic collision course. And the way that they
*  interact, the way that, for example, it kind of throws out these things that look like spiral arms.
*  So often if you look at galaxies, and especially if you look at an image of two merging galaxies,
*  you'll find that kind of these big arms kind of thrown out where there's more light along certain
*  directions than others. It showed how those spiral arms could be generated through this process.
*  Now, there are many other ways that you can generate spiral arms as well, but it was an early kind of
*  success from, well, yeah, I mean, you can call it a simulation. Yeah, that is great. I love the story.
*  It is absolutely ingenious, like you said. But okay, let's just hop to the present day. Okay,
*  we've passed the light bulb stage. Nowadays, we're testing the Big Bang model and its
*  scenario for galaxy formation and structure and things like that. So maybe, I know this is an
*  old chestnut, but let's distinguish between the Big Bang model and the Big Bang, the event at the
*  beginning of the universe. Right. I mean, I guess that the Big Bang model is the idea that our
*  universe is expanding, for one thing. That is established beyond any reasonable doubt,
*  that there is just no reasonable way you could argue that the universe isn't expanding. So let's
*  deal with that first. And it used to be hot, right? That's a big part of the Big Bang.
*  Indeed. So if you extrapolate backwards in time, then by the laws of physics, because as you go
*  backwards in time, everything is closer together in the same way that if you squeeze air into a
*  bicycle tire or something, you can feel things getting hot. And so if you imagine going backwards
*  in time, the universe was not just denser, it was also hotter. So this is the Big Bang model,
*  is the idea that the universe started in some very hot, dense state. And we have direct evidence for
*  it being hot as well in the form of the cosmic microwave background radiation, kind of leftover
*  light from that very hot early phase. However, if you go back before that even further, the question
*  is what happened right at the start? If you just keep going backwards in time, the universe is
*  smaller and smaller and smaller. If you just sort of extrapolate that back using Einstein's equations
*  of general relativity, which would seem to be the right way to extrapolate it back, you get to a
*  moment in time where everything was at a point, the kind of infinite density, all the mass in the
*  universe contained in this single point. And that's the kind of classical Big Bang idea, that the
*  universe actually started from a point and then something made it expand outwards and it's been
*  kind of going ever since. That's the Big Bang, the moment that it goes from the point to being an
*  expanding universe. I think, I mean, you'll have your own take on this, but I think most cosmologists
*  these days would not take that as a literal account of what happened at the beginning of our universe
*  too seriously. So in some sense, we've sort of moved beyond believing in the Big Bang,
*  but we still believe in the Big Bang model, the idea that the universe was once very hot and dense
*  and that it started extremely small. Just the idea that it actually started at a point, I think,
*  has been replaced by other more sophisticated ideas about what might have been happening in those very
*  early moments. And we kind of don't need to know because what you, well, for the purposes that you're
*  interested in working within the Big Bang model, you want to understand how galaxies and stars and
*  structure form, right? I mean, what's the basic picture there that we're testing?
*  Yeah. So the key for us is to understand what is it that's built the familiar universe today?
*  So if you look around you, if you look up into the night sky, what do you see?
*  You see individual stars. If you're lucky, you live somewhere where it's dark enough,
*  or you can see the milky band across the sky, which is the Milky Way. If you're really super
*  lucky and you have a pair of binoculars or so on and you know where to look, you can find things
*  like the Andromeda Galaxy, other galaxies beyond our own, containing their own hundreds of billions
*  of stars. So the universe today is quite consisting of lots of individual stars,
*  many of them, perhaps most of them with their own planets, organized in a very particular way
*  into these kind of islands that we call galaxies. Our own is the Milky Way. And then look out far
*  beyond that and you find other galaxies. And if you look out way beyond that and you kind of
*  somehow get an eagle eye view of the universe so that you zoom out so far that even individual
*  galaxies become dots, then everything is organized into something that we call the cosmic web,
*  where the galaxies themselves are not just scattered through space, they line up in some
*  vast, it almost looks like a cobweb-like structure. So what we're really asking when we do simulations
*  is a couple of things. How did that come about? How do our own origins as a human species relate
*  to that? Because there's a kind of surprising link between all of that vastness, mind-boggling
*  vastness, and our own existence here down on rocky planet Earth. And then on top of that,
*  I think we're trying to ask, how does the fundamental constituents of the universe
*  affect what we end up seeing? So that's when we get onto things like the behavior of stars
*  and black holes, and also onto exotic substances that we think have to be out there, things like
*  dark matter and dark energy that we're not seeing directly, but that we think are responsible for
*  sculpting all this. Now to circle all the way back to where we started,
*  how does the Big Bang relate to all of this? Well, if you want to run a simulation of anything,
*  then you need to have what we call initial conditions. And I use the weather as a kind of
*  jumping off point for exactly this reason, that I think you wouldn't expect anybody to be able to
*  produce you a weather forecast unless they already know what the weather's doing today.
*  If there's a storm coming in, then the fact that it's there, it's already there somewhere on planet
*  Earth, you need to know that. And then you can use a simulation to figure out how it's going to move.
*  Well, in cosmology, we're doing something very similar. We need some kind of starting point.
*  How do we think the universe began in order to work out, well, what happens next, and what does
*  it all mean? And so the Big Bang on its own is not a good enough starting point. We need something
*  with more detail. We need something more sophisticated than that. And that takes you
*  off into the realm of quantum mechanics, what was really going on when the universe was that small,
*  and cosmic inflation, and exciting ideas like that. So those are kind of inputs into the whole
*  simulation project. Well, I guess let's get into the details here a little bit. So I get the idea
*  that we're starting with some initial conditions and then letting them go. For forming galaxies,
*  do we really need to talk about quantum fluctuations and inflation? Or can we just say,
*  well, at let's say, the moment of the cosmic microwave background being formed, right,
*  when we see some actual fluctuations in the sky, that gives us enough information to start our
*  initial conditions? Or do we need even more than that? Well, the thing about the cosmic
*  microwave background is it gives us great evidence for the physical theory of something like cosmic
*  inflation. But it doesn't directly tell you what the initial conditions for the universe should be.
*  It's like a projection. So it's like a kind of, we're seeing a frozen representation
*  of what certain parts of the early universe were like. And it's frozen because at some point,
*  the photons can start moving on straight lines, and they're no longer, the universe is not hot
*  enough to have all the electrons around that are scattering them and so on. So at some point,
*  the light from the early universe can start traveling in straight lines. And after that
*  moment, it just keeps traveling until it hits something, which if we're lucky, you know,
*  it might be one of our telescopes. And so we get to see this frozen moment in our universe's history.
*  But it doesn't tell you all there is to know. To go from that to a kind of 3D representation
*  of what do you think the early universe was really like takes quite a lot of physics. So you can't
*  just jump from, oh, here's the picture of the cosmic microwave background. That's what our
*  simulation should start from. You have to use some smart physics to be able to connect that up with
*  a theory that gives you something much more concrete to start your simulation from.
*  And okay, that's that is very helpful. Thank you. So it's a little bit of a, I don't want to say
*  black magic, but there's a little bit of art that comes in here, right? I mean, the whole idea of
*  the these cosmic simulations is sounds like a back and forth between well, we think this is
*  reasonable, let's simulate it, let's test it against the data, let's go back and figure out
*  whether our assumptions are reasonable to start with.
*  Yeah, it absolutely is a kind of, it's dangerously circular in some ways. So I think, you know,
*  on the initial conditions, I don't find that so worrying, precisely because we have such great
*  measurements of the cosmic microwave background. I don't think we're too worried about the initial
*  conditions being completely wrong. There's room for them to be refined. And, you know, you can
*  go and test, oh, well, if my initial conditions are slightly different, and there are reasons why
*  that might happen, for instance, if the flavor of dark matter you have is not the same,
*  dark matter you have is slightly different from what we currently expect, that can change those
*  initial conditions. But the we're talking about details there, you know, those are relatively
*  small details, in terms of the kind of overall story that that simulations paint, there is a much
*  bigger elephant in the room. And the elephant in the room-
*  Well, what's that? You can't just say that, yeah.
*  Yeah, yeah, the elephant in the room is something that we call the subgrid. So it's worth,
*  it's worth just pausing to say what that is. I mean, earlier on, I was saying, there is some
*  creativity involved in fitting all the physics into a computer. And the subgrid, in some sense,
*  is a way of talking about that. And it's called the subgrid, because sometimes, you know, one way
*  you can do a simulation is to divide up the universe or whatever it is you're simulating
*  into a series of cubes, like a 3D grid. But any computer, even if we're working with the world's
*  best supercomputers, we still have a finite number of those cubes that we can fit inside
*  the computer's memory. And then you come to the question, what happens inside one of those cubes?
*  And the simple answer is nothing, because the computer can't go any finer than that. That's
*  the whole point of making the grid in the first place. But if you're happy with that answer,
*  then you're in big trouble. So again, if you go back to the weather, it kind of becomes more
*  tangible. So if you imagine you kind of look up and you look up on a hot, humid day, then
*  you'll start to see kind of very small, but big, big, tall, but small in terms of the kind of
*  overall landscape clouds that's starting to form. They're actually forming through a process called
*  convection. It happens on really quite small scales where there's a kind of updraft of hot,
*  humid air coming up from the ground. It condenses into a cloud up at a large height, and then that
*  cools and starts to come back down again. So that's a process called convection.
*  And it happens on super small scales, way smaller than any weather forecast can actually resolve
*  in its grid. So that's an example of a sub grid process. And if you just ignore that,
*  then you're going to miss the vast majority of thunderstorms. They're just not going to happen.
*  And even worse than that, even if you were happy with missing the thunderstorms,
*  the fact that those clouds are forming has what we call a feedback on the rest of the weather
*  forecast. So if you have a cloud up in the sky, that means the sun's heat is no longer reaching
*  the ground. So the temperatures are going to be different. And once the temperatures are different,
*  that's going to generate different winds. And before you know it, everything you thought you
*  knew about the weather forecast is wrong because you didn't have these kind of small clouds
*  being generated. So what do weather forecasters do? They add them by hand, basically. This is what
*  we call the sub grid. They go in and they say, well, these things have to form, but we can't
*  get them to form using the sort of laws of physics that we started with because they're too small
*  relative to our grid. So we'll just add a rule. We'll make it up. We'll say, if it's a hot, humid
*  day, a certain fraction of our cubes, our grid cells, they're going to start to have clouds in
*  them at a certain rate. And if you're a weather forecaster, okay, that's not too much of a trouble.
*  You can write that down. You can write down a rate at which these clouds are going to form and you
*  can tune it. You have plenty of data at your disposal. You can just go and tweak the knobs
*  until your weather forecasts start being good. You can even kind of calibrate it on old data.
*  You can imagine, go back a week, would we have predicted today's weather better if we'd made some
*  change to our sub grid? So if you're a weather forecaster, I think the idea of the sub grid is
*  quite natural. As a cosmologist, we face similar problems. So a similar problem for us would be,
*  say, the formation of an individual star. That's actually really hard to see on a cosmic scale.
*  We've already mentioned there's hundreds of billions of stars just in one galaxy
*  and then hundreds of billions of galaxies in the observable universe. So the idea that you would
*  ever see an individual star form within a simulation, it's just not going to happen.
*  There's no supercomputer on earth that's powerful enough to do that. But if we ran all our simulations
*  and they had no stars in them, then we'd be in trouble. I mean, we wouldn't be simulating
*  the universe. So we have to go in and force the stars to form. This is the tip of the iceberg,
*  but it's the kind of thing we're talking about. This is the sub grid. You can look at it in two
*  ways. One is to say it's exciting. It's a different way of thinking about physics.
*  The other, which you kind of alluded to a moment ago, is to say this is dangerous,
*  because how do we get this right? Well, the answer is we make it up. We look at the real universe
*  and then we tweak things until our virtual universe starts resembling the real universe.
*  So in the final analysis, what are we really doing? And you'd guess I wouldn't be writing
*  about this if I thought it was actually a pointless exercise. I don't think it is,
*  but it's definitely complicated. It's not a straightforward, oh, we type in some code and
*  it reproduces the universe. No, absolutely not. There's some very subtle things going on there
*  that you need to be really on top of if you want to interpret what people are saying about their
*  simulations. I do think this is a crucially important point. I want to dwell on it, but
*  let's actually back up and set the stage a little bit, because I bet that there are people out there
*  who think that this whole sub grid thing is a very different kind of simulation than they would have
*  guessed you were doing. I mean, maybe the most naive thing following our friend with the light
*  bulbs would be to say, I'm simulating a bunch of points representing individual stars or clusters
*  of stars or things like that. And I'm watching those points move around in my computer simulation.
*  And I think that what you're saying is that's just not at all what we're doing. We're dividing space
*  up into cubes and every cube might contain the equivalent of lots of stars. And we're trying to
*  figure out what the effect of physics in is per cube and how the cubes interact with each other.
*  Yeah, I mean, we're doing something some slightly in between, I suppose, those two extremes that
*  you just described. So we can do simulations with cubes. They're not always with cubes.
*  Sometimes we're using kind of meshes that can distort into different shapes and so on.
*  But thinking about it as cubes is not a bad way to start. That's how we track something like
*  gas through the universe. So there's a lot of gas out there in the universe and we track it
*  in pretty much that way. Then we do have one of these sub grid rules that looks at each individual
*  grid cube, if you like, or whatever it is, whatever we've decomposed the virtual universe into.
*  And it says, is the bit inside here suitable for forming stars? Does it have the right conditions?
*  And the right conditions, by the way, are things like just really dense gas is a good start.
*  And funnily enough, cold gas is also a good start. That can be a bit of a surprise because,
*  of course, stars are hot. But to form a star, you first of all need to get the gas to be really cold,
*  just so that it can collapse down to a small enough scale that it can actually start up at
*  the nuclear fusion processes and so on. So very roughly, if there's a chunk of gas that's cold
*  and dense, then it can start to form stars. What we do then is we kind of create what we sometimes
*  call star particles. And so this is then going a little bit more back to that laboratory setting
*  where you imagine now, OK, I've got a dot as well as the grid. I've also got a dot in my simulation.
*  And that dot is going to be allowed to move around. It's going to follow. It's going to
*  basically follow the trajectory determined by gravitational attraction. And as it moves around,
*  it's going to pass through a bunch of different cubes. And it can affect the gas around it.
*  As it moves around. And one thing to keep in mind, we are not talking about one star here.
*  We are talking about, we imagine a kind of whole collection of stars have formed. And we're kind of
*  following them as representatives almost of the stars in the universe, because, again, we just
*  cannot track the individual stars. So we have a kind of collection of stars moving through our
*  virtual universe. And they're doing things to the gas as they go. If you study stars, you find out
*  that they do all sorts of interesting things in their lives. They spew out gas through what we
*  call stellar winds. They have magnetic fields. They do other interesting things like when they
*  come to the end of their lives, they explode. A lot of them do anyway. And that puts huge amounts
*  of energy back into the galaxy from which the star formed. So we need to capture all of these things
*  and it can get difficult to differentiate in one's mind. What should one think of as kind of
*  the real physics? And what should we think of as stuff that we've made up? But having clarity about
*  that, I think is the key to really understanding what simulations are actually doing.
*  I remember being impressed and surprised the first time I learned that even though there are a lot of
*  stars in a galaxy, individual supernova events when a star really blows up actually are quite
*  important for figuring out the evolution of the galaxy as a whole. That's absolutely right. And
*  I think the realization of how important supernovae are to determining the whole future of a galaxy,
*  this has come about not exclusively, but in large part driven by simulations themselves.
*  Another story of the origins of simulations, which I really like going into in the book,
*  comes from a character called Beatrice Tinsley. She was actually one of the first people to try
*  and simulate a galaxy on a computer. This was in the late 1960s. So by now we are talking about
*  computers more or less as we'd recognize them, but not with the kind of power that we take for
*  granted. These are very, very primitive machines by today's standards, but she was able to do some
*  of the kind of physics we're talking about, but she really stripped the problem back to its bare
*  bones and talked just about the rate at which stars formed inside a single galaxy and trying
*  to understand how is that determined. Some of her later work then started looking at precisely this
*  thing that an individual supernova going off can change the future of a galaxy because it goes off,
*  it pumps a load of energy into the gas that heats up the gas. And when you heat up gas,
*  it can even get expelled from the galaxy. That's one possibility, but certainly it tends to stop
*  it from forming further stars because as I was saying earlier, gas needs to be cold to form stars.
*  So the fate of the galaxy is bound up in the supernova going off. And when she realized this,
*  actually it had a profound effect on all of cosmology because it revealed that you can't
*  think of galaxies as these kind of passive things that just sit there, kind of being boring lights
*  for the universe as a whole, which actually a lot of cosmologists thought about it that way.
*  And one of the things that that changed overnight almost was the idea that the universe as a whole
*  was going to collapse in on itself. And at the end, we've spoken a bit about the beginning of
*  the universe, there was this idea in the late 1960s that the whole universe would re-collapse
*  and you'd have something called the big crunch. Well, that came about from trying to map out how
*  the universe was expanding today. It was using the galaxies to do that as though they were just these
*  kind of inanimate things that just sat there and didn't really have an internal life. The moment
*  that you added this kind of internal life to galaxies, you had to reinterpret all the
*  observations you were taking. And it kind of led to a complete paradigm shift where no longer did
*  the observational evidence say that the universe was going to re-collapse. And that paved the way,
*  of course, for our modern understanding, which is that the universe is probably going to expand
*  forever and do so at an accelerating rate. So, I mean, they couldn't have been more wrong.
*  And it all comes back to how you regard supernovae, which it seems so disconnected,
*  these quite esoteric concerns about how a galaxy evolves changes the fate of the entire universe.
*  And I really love tracing the origin of these ideas.
*  Well, that brings us right to another thing I wanted to get to, which is again, backing up a
*  little bit from where we are now, because when I was a grad student, I think that the idea of using
*  gas dynamics and hydrodynamics and adaptive meshes and things like that, these were all brand new
*  ideas, right? There were still a lot of simulations going on, but they were basically just gravity and
*  dark matter. And so those are still very important. Why don't we talk a little bit about
*  gravity and dark matter? I mean, how did we get from the tiny fluctuations at the CMB era when
*  the microwave background was formed to the first stars and galaxies?
*  Yep, you are absolutely right. What you see in the cosmic microwave background
*  is just small differences from one part of the universe to another.
*  Whereas when we're talking about galaxies and the cosmic web that I mentioned earlier,
*  these are huge, huge differences that if you lived today in a completely
*  randomly chosen part of the universe, your experience would not at all be like our
*  experience. I mean, first of all, you wouldn't be on a planet. So let's just put that to one side.
*  Imagine you've got a spacesuit and you teleport to a completely random part of the universe.
*  Well, when you did that, the density around you is going to be almost nil. And not only that,
*  but you won't be able to see any stars because a typical galaxy will be a very long way away from
*  you. And so if you teleport to a random part of the universe today, it's completely different
*  from the part of the universe we live in. Whereas in those early times, the universe was much the
*  same everywhere. In the cosmic microwave background, the differences we're talking about
*  are what? One part in 100,000, very, very tiny, tiny differences from one place to another.
*  Whereas now we're talking about contrasts of millions, billions easily. These are the
*  kind of contrasts that we're talking about today rather than these very gentle ripples.
*  Now, something has to power that. Something has to build all of that structure. And I think
*  one of the most underappreciated pieces of evidence for dark matter is exactly that
*  structure formation process. So for anybody who hasn't come across it before, dark matter
*  is this extra stuff that we think has to be in the universe that we can't see directly,
*  but that we think is there because of its gravitational effects. And very often when you
*  hear this explained, you'll hear somebody say, it's to do it the way that galaxies rotate or
*  something like that. So if you look at the way a galaxy is rotating, you find that the stars in
*  its outer parts are moving so fast that if you just add up all the gravity from the things you see,
*  so the other stars and the gas and so on, that is not enough gravity to keep it connected to
*  the rest of the galaxy. It's moving so fast, it should just kind of fly off like a car that's
*  just kind of cornered and didn't have enough grip and it just kind of flew off the track and
*  now it's somewhere else. So those stars should be lost. That's the kind of classic evidence people
*  give for dark matter. Now, that's been criticized for being relatively weak. It's a kind of relatively
*  weak argument. You can find ways to get around it. But I think the really compelling evidence for
*  dark matter is when you contrast something like the cosmic microwave background and the universe
*  today, because something had to build all of these structures and that takes a huge amount of force
*  just to move everything far enough to build these kind of structures out of the early universe.
*  And the only way you can really make sense of having that force available to you is if there
*  is a huge amount of extra stuff. In other words, dark matter that is pulling gravitationally,
*  but that otherwise is remarkably elusive, that we can't see it directly. We don't kind of feel it
*  directly, even though it's kind of passing through us here on earth. That line of evidence to my mind
*  when you kind of put all of these things together is the strongest line of evidence for
*  dark matter actually being a real thing. But of course, what we want to do is compare that
*  idea with something like modifying gravity, right? Do you and the people you hang out with
*  doing these simulations take modified gravity seriously as an alternative to dark matter?
*  Well, yeah, I mean, we do. However, we don't work on it ourselves. So most people working
*  in simulations right now are working within the dark matter paradigm. And the reason for that is
*  pretty straightforward. It's been a very predictive paradigm. So what I'm talking about this
*  structure formation process is not something that was used as a kind of starting point,
*  and then we go, oh, what do we need? And then we kind of make up dark matter. It wasn't that way
*  around. So if you look at something like the cosmic microwave background, even the particular
*  ripples you see in the cosmic microwave background, and then the way that those grow, all of those
*  things are predictions from the dark matter paradigm. The dark matter paradigm really grew
*  up in the 1980s, I guess. And during that time, a kind of combination of some theoretical calculations
*  and some early simulations really started to make clear just how powerful it could be. But it started
*  from the dark matter hypothesis, which had been invented. It was motivated by the kind of things
*  like the spin of galaxies and so on. And then it came to the kind of predictions for the cosmic
*  microwave background and predictions for what the structure of the universe looked like.
*  So it is a remarkably predictive paradigm. And to me, that makes it a very attractive thing
*  to work on. I think if you contrast that with modified gravity, modified gravity has not been
*  predictive. It has tried to explain things. It's tried to say, well, instead of having
*  extra material to generate that extra gravity, what if you just change the laws of gravity
*  themselves? And certain observations, it can explain pretty well in that way. But it has never
*  made a prediction that has turned out to be accurate. And for that reason, to my mind,
*  it's not an attractive thing to work on. And I think a lot of simulators feel the same way about
*  it. It doesn't mean it's wrong. I'm always at pains to point this out. We are not saying dark
*  matter is right and modified gravity is wrong. We're saying we have finite resources, we have
*  finite time, we need to choose what to work on. This seems like a better line of inquiry.
*  Until we actually find dark matter in the lab, we can't be sure we're right.
*  But it just seems more promising. Such a responsible scientific attitude that you have.
*  I don't know if you're going to get very far in this world like that, not in the public relations
*  world. But good. I mean, I'm 100% on your side about this. But let me just play one little bit
*  of devil's advocate here. If we had an advocate of mod, of modified Newtonian dynamics, right,
*  Milgram or one of his, the people who think that he's on the right track, I think what they would
*  say is, sure, we don't have a full theory, we don't make all the predictions. But what we do have
*  is an explanation for the particular features and the phenomenology of galaxies, where the dark
*  matter is in galaxies, how the rotation curves look, the implied amount of mass that you get,
*  etc. Does the dark matter traditional paradigm, is it able to explain those features yet? Or is
*  that just something where we say, well, someday it will be, but we're not quite there yet?
*  Yeah. Let me answer in two parts. I think they would make exactly that point. However,
*  if you look at the way that the observations are treated by the modified gravity community,
*  and now perhaps I'm getting into more controversial territory, but I mean, I think the risk is that
*  they tend to focus on particular observations, rather than try to explain the kind of full gamut
*  of observations that we actually have available to us. Now, that's a dangerous game to play.
*  Arguably, you have to play that game sometimes, because you have to focus your work in just the
*  same way that I was talking about a moment ago. But I think that there are many observations that
*  modified gravity really struggles with, as well as some observations that it makes some sense of.
*  That's true even in the galaxies world. Even if you accept that you're going to focus on galaxies,
*  even then, there are a ton of observations which modified gravity really struggles to explain.
*  I think for me, that's an important point. As to does dark matter explain the same set of things
*  that modified gravity can explain, to a first order approximation, yes, it does.
*  It certainly explains, for example, the overall shape of galaxy rotation curves. For instance,
*  this is a big thing. You measure how quickly is a galaxy rotating as a function of radius.
*  Dark matter does a good job of explaining that. However, there is a criticism that in dark matter,
*  this is a kind of emergent phenomenon. The particular way a galaxy rotates is something
*  that emerges from the underlying theory, rather than something that you predict directly from the
*  theory itself. You need to run simulations to be able to make that prediction really
*  with cold dark matter. It's not necessarily quite so clear a priori why cold dark matter produces
*  the kind of rotation curves that it does. I think there is an argument to be had around that.
*  And I think another thing that the modified gravity community might say is, it's also unclear why
*  there's so little scatter on some of these observations. That in modified gravity, every
*  galaxy essentially should behave roughly in the same way with respect to its rotation.
*  Whereas with dark matter, because the amount of dark matter can be different,
*  especially how it is distributed through a galaxy can be different from one galaxy to another.
*  You're left having to explain, well, then why is it that all the galaxies seem to have such
*  similar phenomenology? Why is there not more variation? And I think that's an interesting
*  discussion to have. I think we can explain that. I think it comes back to the kind of feeling
*  feedback things that we were talking about, about the way that we were talking specifically
*  about supernovae. But that's not the only one. There are many feedback relationships where a
*  galaxy, if it has too many stars, for example, then it's going to start having lots of supernovae.
*  That's going to expel gas. And that means it's not going to form as many stars in the future.
*  There are other feedback mechanisms in addition to that relating, for instance, to black holes.
*  We know that there are supermassive black holes at the centre of most, perhaps all,
*  all galaxies. And they also have a feedback relationship with the galaxy and the dark
*  matter around them. So I think the answer probably lies in those feedback relationships.
*  But I think it would be a fair criticism to say that's not fully understood at this point in time.
*  But I would just go back to saying that is within the context of a theory
*  that has been incredibly predictive on a huge range of scales, ranging from the entire universe
*  down to tiny little what we call dwarf galaxies. So to my mind, it's an interesting question,
*  but it's not the kind of thing that convinces me to go and work on modified gravity.
*  It's an audio podcast, so the audience doesn't know. But I've been nodding along for everything
*  you've been saying here. I think that this is very much on the right track. But I should bring up the
*  other worry that has peeked into our consciousness about the whole hot big bang gravitational
*  instability leading to galaxies story, which is observations from the James Webb Space Telescope.
*  I'm contractually obligated to say this because my office at Johns Hopkins is across the street
*  from the Space Telescope Science Institute. So if I can bring up JWST, I have to do it.
*  It's a powerful new telescope that has apparently found very early galaxies,
*  galaxies that are far away and therefore early in the history of the universe,
*  that are very massive, that we would have thought would have taken longer time to assemble.
*  So is this considered a challenge? Is this something that you can account for? Or is
*  this something where you think those observations are probably a little sloppy because it's the
*  early days and hopefully they will go away? Well, I mean, yeah, this is something we could
*  talk about for a whole hour, I think, because this is really exciting, cutting edge stuff.
*  And I think the answer in brief is a combination of all the things you just mentioned. So
*  first thing to say is JWST has just kind of been performing beyond people's wildest dreams. I mean,
*  it's such a fantastic new telescope bringing the cosmos into our own homes, right? The pictures
*  that we're getting to see from it and reaching out much further to see the story of galaxy
*  formation much further than has been possible in the past. So the first thing I wanted to say in
*  response to that is just how exciting it is to be living through this time where the first
*  observations come from JWST. But let's just rewind for a moment. Let's imagine the Hubble
*  Space Telescope launch. Now, I was young when the Hubble Space Telescope launched. I just about
*  remember the excitement around it. I would have been at school. I remember it being on the news
*  because it had the faulty optics, which then got fixed by an astronaut spacewalk. And then it
*  started taking just fantastic pictures. So this would have been what, 93, 94, it's that kind of
*  era. And one of the early pictures it took was something called the Hubble Deep Field.
*  So the plan here was to point Hubble for I think around a week or so at a patch of the sky
*  that was not known to contain anything, just nothing of any interest, which sounds a little
*  crazy, but the idea was build up sensitivity by pointing this incredible new telescope at just one
*  patch of the sky for that kind of very extended period and see what's there. And what was,
*  after that had taken place and it was beamed back and people recreated the picture, we got a kind of
*  iconic picture of a kind of empty space with a whole series of dots and swirls in it. And basically
*  everything that you see in that picture, and you can easily go and see it today, right, you just
*  Google this thing, is everything that you see is a galaxy that's far, far away. And this was an
*  incredible new view at the time of the way what was then thought to be the early universe
*  was evolving. And it was a catastrophe for simulators, a total catastrophe because the
*  kind of predictions that had been made such as they were, were that if you did an exercise like
*  this, it would actually be full of quite bright, large galaxies. That this was despite the fact
*  that people knew about the way that the universe had been building up its galaxies through the
*  gravitational effects of dark matter, all the things that we talked about, you know, the bare
*  bones of that were known at the time, but the simulations were just getting the details wrong
*  and the details of feedback. We keep coming back to it. This sub-grid and the way you
*  calibrate that and get all of those details right about when do stars form, how do they form,
*  do they form clumped together or in kind of spread out. All of these kind of things really matter
*  to be able to go from the bare bones of the scenario you're talking about to the kind of
*  detail of what will you see with a particular telescope. So that leap that took place in the
*  mid-90s, it was on the face of it really catastrophic for the dark matter paradigm because
*  the predictions that had been made were way off. But very quickly people realized what that was
*  telling them. It was telling them that they hadn't been treating the way that stars form correctly.
*  This needed to be revisited and a lot was learned through that process.
*  I suspect what we're seeing with James Webb is a very similar process beginning
*  where it's going to tell us stuff. We are going to learn new stuff about the way galaxies form,
*  but it's very premature to jump to any kind of headline that says this puts the overall
*  story in jeopardy. It throws up interesting challenges, but as things stand, it doesn't
*  put the overall story in jeopardy and probably some combination of improving the simulations
*  and refining the way we treat this data from telescopes, getting better data from JWST and
*  in particular getting more spectra. That's where the light from these galaxies is broken down
*  into its different component colors. So all of these things I think are going to get to a much
*  more measured consensus at some point. Now if the challenges seem insurmountable in a couple of
*  years from now, then we might be having a very different discussion. But when you have a new
*  technology like this, it just takes time to integrate what it's showing us.
*  I think I just say one more thing on this, which is this is obviously treading quite a delicate
*  fine line because on the one hand, hopefully what I'm saying is reasonable. On the other,
*  you might be thinking, well, hang on a second, this isn't how science is supposed to work.
*  You don't get to revise your predictions after you've taken the data because you went, oh,
*  well, come on, it was complicated. So I think we have to be very aware of treading that fine line.
*  There's no getting away from it though. The universe is a complicated, messy place that
*  we cannot fit inside computers. The way to test our understanding is not by building a telescope
*  like JWST that takes us into totally new realms. That pushes forwards our understanding to a new
*  level. And so it's incredibly important. But the way to test our understanding is rather more
*  subtle. And it involves kind of finding, okay, if we're predicting something about how galaxies
*  form, can we find a kind of more direct corollary of that that we can go and test?
*  This is the kind of thing that we try to do. So for example, we think something like our
*  Milky Way galaxy was built out of lots of tiny little chunks that would individually have been
*  very dim, but they have to be out there. And so if we look back into the distant universe,
*  we can start looking for those little chunks of galaxies. Things like that, which are kind of
*  direct corollaries from the picture that we're painting, can be used as tests. Something like
*  this kind of major step into a whole different epoch of the universe's history is much harder
*  to use as a test. And I think you have to expect there will be some tweaking to what we're doing.
*  Let's see where we are, like I say, in a couple of years.
*  Okay. So is it fair to say the short version is these are important results that we should
*  pay close attention to and be open-minded and willing to change our views if necessary, but
*  right now, no reason to really worry about the overall validity of the Big Bang model?
*  Correct. Yeah. Right now, there's nothing that would really throw that into doubt. I think,
*  though, there could be, you know, if some of these things persist and we persist in not being able
*  to explain how such big things came about and so on. So, I mean, it's not that there cannot be
*  anything that would make us start doubting the picture that we're painting, but right now,
*  we're just not there yet. I found a great article online about this issue of the early galaxies
*  by Ivo Lobb. I don't know if I'm pronouncing his name correctly, but he's an astronomer. And
*  his way of putting it is that, you know, the most natural way of thinking about this is it's not
*  necessarily something that these massive galaxies at early times exist but are rare, that what we're
*  missing here is not a major feature of our picture of galaxy formation, but that there's a fast track
*  for the 1%, that if you're really in the right place at the right time, you can make a more
*  massive galaxy than we would have expected. That's absolutely right. I mean, that could be part
*  of the story. So, that then starts to come down to, you know, what data is available so far from
*  something like JWST. And, of course, inevitably, because it's only been up for a short while,
*  it just doesn't have a kind of representative survey of what the universe really looked like
*  at these early times. So, that will also come and that could play a part in explaining what's
*  going on here. I mean, it's super interesting because it could also connect to the origins of
*  supermassive black holes. So, this is the very massive black holes that we find at the centre
*  of modern galaxies. I think one of the big question marks for galaxy formation as a field
*  is where did those supermassive black holes actually come from? Because it's actually very
*  hard to figure out how do you grow black holes quickly enough? If you imagine just creating
*  what we would call a small stellar mass black hole. So, I mean, this is something that would
*  be a few times the mass of our sun. So, it's huge, but small by comparison to these supermassive black
*  holes that are millions or even billions of times the mass of our sun. So, how do you get
*  from one to the other? How do you start from small black holes and get these absolutely huge
*  million or billions of times larger black holes by the present day? I mean, we have ideas, but
*  that's a very hard thing to do. And it may be that all of these stories are kind of bound up together
*  in some way, which is going to make the next 10, 15 years very exciting because we have
*  new gravitational wave facilities on the horizon on that kind of time scale.
*  So, we'll not only be able to see what's happening to galaxies at very early times in our universe,
*  we'll in some sense also be able to feel what's happening to galaxies at very early times in our
*  universe with these very sensitive gravitational wave detectors that will be able to feel the
*  gravitational waves coming from the early population of black holes. So, I think
*  the long term for all of these questions is going to be one of piecing together evidence
*  from many different lines and seeing how we can get it to hang together rather than any single
*  piece of evidence being definitive. I think that maybe there's a question
*  lingering in people's minds here, like, why is it a question how the black holes form? Aren't you
*  simulating what happens? Shouldn't you see them form? And I take it that this goes back to that
*  subgrid problem. It goes exactly back to the subgrid problem. So, if you imagine where does
*  a black hole come from? Well, what we call a stellar mass black hole is formed at the end of
*  the life of a star. So, if we can't actually be sure about how stars form, then we can't actually
*  be sure about how black holes form. And it gets even worse than that actually with black holes,
*  because black holes, the famous thing about them is anything that falls into a black hole stays
*  in a black hole. Okay, well, Hawking radiation is on, but that's a much longer term thing when you
*  start talking about Hawking radiation. So, the main thing about a black hole on the kind of
*  typical time scales we're talking about is anything that goes in stays in.
*  And that means that a black hole can grow. So, it's not just that you form a black hole and it
*  stays that size, it actually grows over time by kind of eating its surroundings. And yet again,
*  we're talking about the subgrid, because you can't actually see an individual black hole in its
*  surroundings. You have to make some informed speculations about how fast could it eat gas
*  from the big cube that it's sitting inside. And not only that, but then that generates energy,
*  that process of eating the gas, what happens to that energy? How does that interact with the
*  gas that might otherwise have been eaten? I mean, maybe the energy from eating one bit of gas can
*  blow away other gas. I mean, it becomes extraordinarily complicated. And all of this has to be handled in
*  some sensible way. But yeah, you can't sort of just zoom in to a simulation and just see this
*  happening. I guess I would be remiss in the modern era if I didn't ask whether there was room here
*  for AI and deep learning models to help us with some of these questions. I mean, people are
*  definitely looking down those lines. The exact way that we use deep learning and AI in astronomy and
*  cosmology is evolving incredibly fast right now. And I think one thing you can imagine doing is
*  you can run a very detailed simulation of how does a black hole eat some gas? Now, if you want
*  to run that detailed simulation using all of the physics that you think is relevant, then you can't
*  simulate the rest of the universe, right? That's part of the problem. But if you want to, you can
*  take your computer time and use it to do that. Now, so a possible thing you could do is subject
*  a black hole to lots of different conditions and then get a deep learning model or something like
*  that to try and predict based on, can be trained on those detailed simulations you run. And then
*  you can try and use that to predict what a black hole does. I mean, in some sense,
*  it's not that different from what we're doing already. That's what would the machine learning
*  learn? Well, it would learn some kind of set of approximations to what a black hole is supposed
*  to do. That's what we're trying to do as humans and then that coding goes into our subgrid.
*  So it's a way that you can perhaps digest more information and bring that into the simulation.
*  And it's definitely something that people are investigating with a lot of energy. But to my
*  mind, the real excitement in AI is somewhere slightly different. First of all, AI to my mind
*  is a simulation. So that's why I end up talking about it in the book. It is a simulation of
*  thought. But what we have right now in the AI landscape is we have things like chat GPT, say,
*  which you can go and ask it a factual question. And if you're lucky, it'll give you a factual
*  answer. Or if you're unlucky, it just makes something up. But it's impressive, but it's
*  kind of got a fairly fixed corpus of knowledge. That's one kind of segment, if you like. And
*  then on another part of the AI landscape, you have the kind of things I was just talking about,
*  where you train models to do quite specific tasks, like predict what should a black hole do within
*  a galaxy or something like that. Now, the question is, how do you start bringing those things together?
*  How do you start getting AIs that not only make predictions, but explain those predictions?
*  And even more than that, they don't just explain them, they link them to the existing body of
*  knowledge. So imagine for a moment, you had a future AI that somehow, it didn't just study
*  your black hole simulations and make predictions that you could use elsewhere. It actually explained
*  what it's learned from those simulations and started talking to you like a physicist. Well,
*  now you'd be somewhere very interesting, possibly somewhere frightening. I mean, maybe we're
*  going to be putting ourselves out of a job, but I think you can go towards that goal
*  right now. You can start making steps towards that goal. And I think that's an incredibly
*  exciting area to be working in. And we're trying to do that with respect to the overall formation
*  of structure in the universe. Because right now, our explanations for how structures form in the
*  universe tend to consist of saying, well, you have the laws of gravity and you have dark matter,
*  and then you program them into a computer and you hit go and here's what you get.
*  And if you could start building on that and actually creating explanations for why,
*  I mean, to go all the way back to your question about why does regularity emerge in galaxies
*  that makes it look like modified gravity? Could we start using AIs to help shed light in that area?
*  I mean, I think maybe we could, but it's difficult because it's having to bring together these rather
*  different takes on AI into a kind of common framework. I'm remembering now, only just now
*  that we're having this conversation, that I was invited to give a talk at an APS meeting back in
*  2006, so ancient history now, on the future of theoretical cosmology. And I remember making
*  somewhat tongue-in-cheek predictions for when computers would start replacing graduate students,
*  postdocs, professors. But I forget, I've lost my track of exactly what those predictions were,
*  so I think I'm safe. Hopefully it was not recorded. But never 100%, I think, but maybe a lot of the
*  dirty work that we do as theoretical physicists will be able to be offloaded to our computer friends.
*  I think that's possible. And I think we have to tread with care here. I mean,
*  it's clear that we are entering dangerous territory with AI as a whole. And it throws up a bunch of
*  ethical and practical dilemmas that we have to look at very carefully as we do this. Even as
*  physicists, it's not like we are trying to develop models that are going to completely change the
*  world, but we are contributing to that overall landscape of AI. And so I think we do have to
*  take a kind of responsible attitude towards this. But yes, I think there is a role to be played.
*  You know, it would be crazy to try and shut ourselves off from this. There is a role to
*  be played where it can augment rather than replace what we're doing. And the more we can get it to
*  actually link what it's doing to a broader landscape of knowledge, I think the more
*  powerful it's going to become in those regards. So I'm kind of excited. I guess like everybody,
*  I'm a little scared too. But I do think there are exciting times ahead. And I'm kind of an optimist.
*  I feel like we can do this. And we can do it in a way that doesn't contribute to the downfall of
*  civilization. That would be good. I think that all things equal, that would be good. Anyway,
*  maybe the place to wrap up is some very big picture philosophical questions about what's
*  going on here. When we talk about simulations, I remember having arguments in graduate school
*  about this. Do you count simulations as part of theory or part of experiment?
*  Right. Well, I mean, I'm on the fence. I think if you look at an individual simulation,
*  you can often locate it in that spectrum. But I think what's so interesting about simulations,
*  in a sense, is that they definitely span that divide. So I can give you a couple of extreme
*  examples, I suppose. So let's imagine that you're working at the Large Hadron Collider, let's say,
*  and you are trying to interpret the data that you're seeing from the Large Hadron Collider.
*  Let's go back in time. Imagine we're trying to pick out the Higgs boson at the Large Hadron
*  Collider. Now, there's a big problem with doing that, which is just that the Large Hadron Collider
*  does not have a Higgs boson detector. You don't have a detector that actually detects the Higgs
*  boson directly. That cannot be built. What you actually detect at the Large Hadron Collider
*  is a bunch of remnants of a Higgs boson after the Higgs boson has kind of come into existence
*  momentarily and then decayed into a bunch of other particles. Those are the things that you
*  actually detect. So you need simulations, actually, to figure out what do we expect to see.
*  If the Higgs boson is there, what do you expect to see in your detectors? It's not a straightforward
*  thing. So those simulations exist, they're run, they are a big part of some people's lives running
*  these kind of simulations. So what is that? Well, I personally think that it's not an experiment.
*  The simulation itself is not an experiment. It's being used to interpret an experiment.
*  So it's a calculation, I guess. It's a calculation of what happens under these
*  circumstances. I wouldn't really call it theory because it's not uncovering anything that we
*  fundamentally didn't know before. So to me, therefore, that's not really theory. It's not
*  really experiment. It's more like a calculation. So some simulations are like that. They're
*  calculations. There's nothing wrong with doing calculations, right? That's at the heart of what
*  we do as physicists. I think it's theory. I think it's just 100% theory. Doing calculations is
*  theory. Yeah. I think experiment is collecting data about the physical world. Of course,
*  when you look at your computer screen, you're collecting data about the physical world in some
*  very thin sense. There's a screen in front of me. I don't care that much if people want to
*  disagree with this, but I think that simulations are just tools for being better theorists,
*  for making predictions on the basis of our theories. Okay. So let me try arguing back against
*  that. So I think, okay, that's arguable for the case of the Higgs boson we just discussed. Do you
*  call it a calculation? Do you call it theory? Okay. Well, it's potato, potato. It's kind of
*  semantics, right? However, I think there is an argument to be made that in certain circumstances,
*  not the one I just described, but in some circumstances, they're experiments. Simulations
*  are experiments. And I guess this is arguing pretty directly against what you just said.
*  Imagine that you haven't discovered the laws of thermodynamics yet. Okay. And now I give you a
*  simulation of a large number of particles. And by the way, I actually do this with undergrad classes.
*  So in a sense, they haven't discovered all of thermodynamics yet. So it's not that counterfactual.
*  So you have a simulation. It models roughly what particles do. Now it doesn't get every aspect of
*  it 100% like reality. Of course it doesn't. It just imagines particles as little bouncy balls
*  bouncing around. But you can discover thermodynamics in these simulations. You can compress the box,
*  the simulation box. You can kind of apply an external force, compress it and see the things
*  speed up. In other words, you're discovering the conservation of energy or you're discovering
*  that the interchange between the external forces and the internal energy. You can do other things.
*  You can discover the way that substances diffuse through a room. You can discover Brownian motion.
*  You can discover all sorts of things inside a simulation. Now, what is the nature of that
*  discovery? That I guess is at the heart of it. But to me, there is not such an obvious fundamental
*  distinction between what you're discovering there, which is like a kind of emergent property of the
*  way things can behave under some circumstances and what you could discover in a laboratory setting.
*  I think the counter argument is, well, hang on, the laboratory, that's real physics, right? But
*  the computer is just doing what you've programmed in. But again, that distinction kind of crumbles
*  in your hands if you really try to make it. Take another example. Say I'm working for an airplane
*  manufacturer. I want to know how is my aircraft wing going to perform? I can make a scale model
*  of it and put it in a wind tunnel. That's an experiment. I'm sure you agree. Or I can make
*  a digital version of it and put it in a virtual environment. Now, why is the latter not an
*  experiment? I mean, it's got some approximations in it, that's for sure. But then so does the wind
*  tunnel. The wind tunnel has approximations. It's perhaps scaled down. It has a particular type of
*  flow. It has walls, which are not going to be there when you fly your actual aircraft.
*  So I've always found that the more you try to examine, the more you try to say simulations
*  cannot be experiments, the more you question, well, if that's true, then what is an experiment
*  if a simulation can't be one of them? I think that the answer is that the experiment tells
*  you something about what nature does, not something about what your theory predicts. Now,
*  if your theory is right, that also happens to tell you something about what nature does.
*  If you do a simulation of little gas molecules, etc. But the point about that simulation of gas
*  molecules is that you might discover the laws of thermodynamics, but then you might go out and look
*  at the world and find that the world doesn't act that way. And you can't do that without collecting
*  real data. Yeah, but I don't know. I mean, experiments are rather like that as well, right?
*  I mean, you have to make some kind of controlled conditions. You make a bunch of assumptions in
*  how you set up the experiment, what you think are the relevant things to control. So experiments
*  are laden with theory at some level. You have to decide what are you doing? What are you controlling?
*  What are you measuring? What do you have to control for? All of these things depend on theory.
*  And then, yeah, you might go out into the real world and find, hey, whatever I based on that
*  experiment doesn't appear to be true. I think, honestly, the same thing is going on in simulations.
*  And I mean, the thermodynamics example, I give it precisely because it isn't right, right? It's not
*  doing quantum field theory to figure out what the particles really do. It's based on a very naive
*  idea about what the micro physics world might look like. And yet, the macro physics that emerges,
*  the laws of thermodynamics that emerge from that are empirically correct. So for emergent phenomena,
*  I feel like simulations, you can regard them as experiments. You have to be aware of the limitations,
*  but then you have to be aware of the limitations of an experiment as well, right? So
*  it's just, it's not obvious to me how you draw that line.
*  Well, that is perfectly fair. That's not obvious. And that's why it's an interesting question. But,
*  okay, final question then. As a simulator of universes, literally, can you imagine a day
*  when you or your successors are going to simulate people in your universes? And that's going to lead
*  us to an obvious next question that I will let you fill in.
*  Right. Yeah. So the short answer is no. I think as a simulator of universes, we have zero motivation
*  to simulate people inside those universes. Just zero. I just cannot imagine why would you want to
*  do that. And maybe we can circle back to that. But just to flesh out, you were saying the next
*  question is obvious. And indeed, yeah. I mean, do we ourselves live inside a simulation? And this
*  is a discussion that's been kind of ongoing for many years now based on a number of people's
*  thinking. But I guess Nick Bostrom, I think was on your podcast some time ago, in fact.
*  And Nick Bostrom kind of distilled this down, I think, to a very neat set of ideas. So
*  he sort of set out a series of postulates, one of them being, we're going to want to continue
*  running simulations that get ever more detailed. And if you follow these postulates, there is a
*  logical conclusion that we ourselves quite possibly live inside a simulated universe.
*  So I have no argument against Nick Bostrom's kind of logic. I think the logic is fine.
*  However, I think where this falls over is, first of all, in assuming, well, Nick Bostrom doesn't
*  assume, but some people when they're describing it do assume that we are going to want to make ever
*  more and more detailed simulations. So I think that assumption is probably incorrect, as I was
*  just saying. So I think once that assumption is swept away, then we no longer have the simulation
*  hypothesis looking as strong. I think there's also a second sort of practical layer to this,
*  that if you wanted to simulate the universe perfectly, then you can count the number of
*  bits or more technically qubits that's required to do that. It's a stupendously large number,
*  it's something like 10 to the 124, I think. That's what's required to simulate the whole universe.
*  How can you do that? Well, it turns out that you would need to use the whole universe to build
*  your computer, because if the whole universe takes 10 to the 124 qubits to describe, then
*  you need to use all of those qubits to describe a universe. So it becomes circular. I mean,
*  you can't do a perfect simulation of the universe from within the universe itself.
*  So then you can say, well, maybe the simulation doesn't have to be perfect and so on, and that
*  leads you down various routes. And you can start arguing about what are we really imagining
*  these future simulators are doing? Why are they making this simulation that seems to be so
*  incredibly detailed and stands up to all of these tests, but where in reality it's a sort of hoax
*  of some sort. And that's where you end up with the simulation hypothesis. It's a basically
*  conspiracy theory territory. And so it's deeply uncomfortable for that reason. But I think,
*  obviously, just because something's uncomfortable doesn't mean it's wrong. But I think, to my mind,
*  the way out of this is to recognize it's not at all obvious that you want to carry on running
*  simulations and ever more detailed simulations. But at least for a little while, you're going to
*  keep wanting to run more detailed simulations than you have right now.
*  Absolutely. Yeah, for a while, you want to add layers of detail. But there's another interesting
*  angle on this, which is as you add more detail, the simulation gets more powerful in certain ways.
*  But in other ways, it gets less powerful. There's a kind of paradox in the heart of this,
*  which is that one of the ways we really learn from simulations is to do countermeasures.
*  We do counterfactual things. So an example would be, let's simulate the universe, but let's stop
*  all the black holes from forming or growing. And let's see what happens. And we can do that exercise.
*  And the answer is you get galaxies that look completely wrong. So it reveals a really deep
*  interplay between the lives of galaxies and the lives of black holes, which is really exciting
*  and connects to the things we were talking about with JWST and future gravitational wave
*  that ability to go in and just switch something off is tied to the fact, the very fact that our
*  simulations are so crude. If the simulation just did everything all by itself, then there wouldn't
*  be like a switch in our code where we could just switch black holes off because they are an
*  inevitable consequence of general relativity. So you wouldn't be able to do that. And so this is an
*  example of what I mean when I say there's a paradox where as you make simulations more powerful,
*  in some sense, they become less powerful at the same time. And that's why I don't personally
*  think you just want to go on adding more and more and more and more detail to simulations.
*  They will get more sophisticated over time, but I think there is some point at which you go,
*  you know what, we're going to do better simulations and cleverer simulations,
*  but they're not going to just have more and more layers of detail.
*  Okay. That's very, actually a very interesting point, but I'm looking forward to what happens
*  next with even better simulations and comparing them with even better data. So Andrew Ponson,
*  thanks so much for being on the Mindscape Podcast.
*  Thank you.
