---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3436s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 921
Video Rating: None
---

# BI 017 Jeff Hawkins: Location, Location, Location
**Brain Inspired:** [November 07, 2018](https://www.youtube.com/watch?v=FQau3J5QopY)
*  The cortex is actually thousands and thousands of models and all running in parallel and they're voting all the time
*  It's a completely different flip and how you think about it. So do you have it on you?
*  There it is. Okay. So the question is how often does that thing get washed?
*  This is brain inspired
*  Hello good people
*  This is Paul Middlebrooks. Just got back from a little bike ride from a coffee shop here in
*  beautiful, Durango, Colorado. Oh
*  It's so nice here. I hope it's beautiful where you are
*  If you would like to support the show, please go to patreon.com
*  slash brain inspired or go to my website brain inspired co and you can find the red patreon button there
*  It was broken last week. Thank you Matt for informing me, but it should be working now
*  Okay, joke of the show written once again by yours truly. I apologize in advance
*  So a convolutional neural network walks into a bar
*  That's it that's the joke Al Al
*  Thank you little
*  Embodied cognition humor there. Hmm. Yeah
*  All right, I'll keep trying if you have suggestions for the show or jokes
*  Please send them my way to Paul at brain inspired co
*  Alright today. I talk with Jeff Hawkins as you'll hear Jeff describe. He's always been interested in neuroscience and specifically
*  theoretical neuroscience
*  However his career veered to computer industry in the 80s the 1980s that is when he couldn't convince
*  Anyone that theoretical neuroscience was a worthy endeavor
*  while in the realm of the computer industry
*  He founded handspring and palm computing of the famed palm pilot
*  Which for those of you youngins out there was the first widely used handheld computer
*  Otherwise known as a PDA or personal digital assistant
*  fast forward to
*  2002 still without interest from universities to start a theoretical neuroscience program
*  Jeff began his own the Redwood Neuroscience Institute, which has since been subsumed by Berkeley
*  shortly after that he published his excellent and influential book on
*  intelligence and
*  Shortly after that he founded his current company new Menta, which you'll hear us discuss in a moment
*  Today we also discuss his aforementioned book on intelligence
*  Which although it's almost 15 years old now is clearly still relevant and timely and I recommend it to all of you
*  We discussed the role of the theorist in neuroscience. We talked about his new theory
*  Which proposes a fundamental computation?
*  Performed all across our cortex
*  namely that
*  every coracle column in our cortex
*  Models a complete object and you have thousands of models of objects stored across the entirety of our cortex
*  All running in parallel
*  That should make more sense as we discuss it in the show and we talk a little consciousness
*  and how movement is central to cognition and
*  More find the show notes at brain inspired co
*  podcast
*  17 or you can just go to new Menta comm to find all the papers that
*  Lead up to this most recent one that we discuss
*  Okay, enjoy the show
*  Jeff Hawkins, welcome to the podcast and thank you for being here. Thanks for having me Paul
*  So I will have given you a pretty lengthy introduction before we're talking right now
*  But I just want to say here that among the many things that you've done you invented the palm pilot now
*  How long has it been since someone has told you a personal story about using the palm pilot?
*  You'd be surprised how often that happens. It's probably less than a week
*  Okay, well, can I tell you mine just to kick things?
*  Sure, yeah, but it's a totally different part of my life I've completely divorced myself from that but sure go ahead
*  Yeah, well, it's just because you've touched me in many ways, sir
*  So so so my dad actually bought me a palm pilot
*  When I was an undergraduate and I used it for a while and then I kind of put it away
*  and then I I started using it when I went to graduate school because you need to be more organized and
*  So I started using it again
*  I started dating the woman who is now my wife and I brought it over to her apartment and
*  You know, I took her out my pocket
*  I put it on the little bar that separated her kitchen and living room
*  She can she's walking around she walks over and she picks it up and she starts looking at it and she says
*  What is this thing?
*  I was like, it's a it's a palm pilot and I kind of described what it is and and she's looking at it
*  And then and then she her eyes start to kind of screw up and she looks over at me and she said
*  This palm pilot smells like trash and and I look over and she's standing with her foot on the
*  Trash can pedal with the lid wide open and she's smelling her own trash
*  Well, that's an unusual story. I haven't heard one like that before
*  But usually usually people have stories like hey, I really enjoyed it, you know
*  Well, I did actually, you know, one of the funnest things was learning the shortcuts of the handwriting
*  To write the letters. Yeah. Yeah. Yeah the graffiti. That's right
*  Well, you know that that whole part of my life
*  was a sort of interstitial period between being a graduate student in neuroscience and
*  Wanting to become a full-time theoretical neuroscience and when I was a when I was at Berkeley as a graduate student and late eighties
*  I was told I really couldn't do what I wanted to do in neuroscience which was being a theoretician
*  So I ended up going back in the computing industry for what I thought before years
*  Just to sort of make some money and get my bearings and
*  That's when I started palm and the funny thing about that everyone who worked for me for all those years at palm and handspring
*  everybody knew that I really didn't want to be doing that that I wanted to be studying neuroscience and
*  that was sort of the cult there and
*  So that was the plan to get you know
*  Get through that period of my life and come back and be the study brains and that's what happened. That is what happened
*  Yeah, so let's talk about that right so
*  Numenta this is your current company. You've been through a couple iterations the Redwood
*  Institute so Numenta is your current company and it's a private company and the primary goal is to reverse engineer the neocortex
*  And what you guys do from what I understand is you are theoreticians
*  So you study the the data that's collected by experimental neuroscientists
*  You guys study that data you create the theories and create predictions that can then be tested again in in
*  Experimental neuroscience, you know tell me just a little bit more about about it. Yeah, that's quite right
*  although it's funny because in other fields of this physics there there are a lot of
*  theoreticians of
*  theoretical physicists and they're experimentalists in the neuroscience world that's very rare and
*  The in fact when I got into this field it was unheard of you couldn't be a theoretical neuroscientist
*  That's what I was told right you had to work in an experimental lab
*  And I think you did too in your in your past perhaps
*  Yes, I look I'm jealous and I think you've done it the right way because I spent a lot of hours doing experiments
*  Well, I was I was a graduate student at Berkeley and I was looking at these different experimental labs
*  And I said this is not gonna work for me. This is gonna take me years and years and years
*  I'll be in a mess in these experimental techniques and I really want to stick to the high-level theory
*  And the people who are doing the lab work really it's not a luxury. They have typically
*  and so
*  It's unusual but it's that we have a theoretical group, but it shouldn't be unusual other other fields of science to have
*  Theoreticians and and so we play a very traditional role
*  being
*  Theoretical neuroscientists in that we we analyze data. We we work with experimental labs
*  We have a lot of close collaborations, but we don't do the experimental work ourselves
*  That is unusual neuroscience, but it's not unusual than science in general
*  Yeah, so it's it's it's just the way it turned out and and I had to follow the path that made it work for me
*  Yeah
*  So, I mean it's interesting because we're at a time right now in neuroscience where we're starting to be able to collect
*  Larger and larger sets of data. So in a sense, it's really difficult right now to be an experimentalist and a theorist
*  It's getting harder and harder and harder. So yeah that separation
*  I think you're I think you're gonna become a little bit more mainstream and you're helping to
*  Bring that forth as well. So I think you know, I think we are pretty mainstream. We're just rare
*  Yeah, as I said, we have a lot of collaborations and I meet and work with neuroscientists all the time
*  I just I've given dozens and dozens of invited talks at different conferences and neuroscience conferences and so on and
*  So we're well respected
*  It's just that we're just a bit unusual
*  That's good, that's your tagline. Yeah
*  So but who works for you like so what kind of backgrounds do they have? Is it academic backgrounds?
*  experimentalists industry people
*  Well, it's a little bit of a mixture of things. We have an office in Redwood City, California
*  That's Northern, California. We're just a couple miles from Stanford and we have I would say five sort of technical staff
*  Several have PhDs some don't there's a mixture when they come into it no matter they have a mixture of various sorts of
*  Technology machine learning AI and neuroscience. Yeah, when you spend time here, we all become neuroscientists
*  We read neuroscience papers all the time. I train new people who if they don't have the neuroscience they have to learn it
*  So we all become experts in the neuroscience if they do not coming in with that knowledge
*  But so there's like five of us who are sort of the technical staff and we work together as a team and then
*  There's about another five people who sort of do other things. There's marketing and office. We have an office manager and our CEO
*  And so there's various business relationships
*  We maintain things you have to do when you have a business
*  But otherwise it's kind of the size of a small to medium-sized lab exactly
*  It is it's kind of a exactly way is you could think of me as the PI
*  Yeah, although VP research
*  Subhati Ahmad is also he manages everybody so kind of we're partners in that so but you can think of it that way
*  Yeah, it's it's it's a small lab or medium-sized lab a couple episodes ago. I talked with your
*  Your co-founder to leap George. So that was fun. Yeah, so and he's off doing other things now
*  Yeah
*  So I guess the it's probably worth talking for a moment about the underlying technology that you guys have developed and used which is called
*  hierarchical temporal memory
*  Can you give just a broad overview of some of the key properties of HTM?
*  Let's say and maybe in particular the role of sparseness and why it's important. Yeah, I mean that's a big topic
*  We use the term HTM as sort of an umbrella term to refer to our theories about the neocortex
*  And it's an evolving set of theories meaning we're adding to it all the time
*  So when we started using HTM, we had some components in place and now we have many more components in place, right?
*  So it's not a singular thing
*  it's all based on essentially having a theoretical theory of how the neocortex operates and
*  We've made tremendous progress on that and literally in the last year
*  But over the over the last six or seven years, there are numerous things you brought up
*  You brought up some detail you mentioned sparseness and sparse coding
*  That's a core fundamental
*  Principle the brains use is that when you think about a set of neurons and when they want to represent something
*  The way they represent it is some of the neurons are active relatively active and some of them are not some of them are firing
*  Quickly some of them are not we call it a sparse distributed code because if it's sparse because if I say had 10,000 neurons
*  There may only be 2% active at any point in time or about 200
*  And so that's a sparse code
*  But it's distributed because it's not a grandmother cell that you need 200 cells to represent this thing
*  And it turns out that the properties of sparse distributed representations
*  that is you're representing things by having a population of neurons and
*  a subset of them are active the mathematical properties that are very interesting and
*  We've written extensively about this it explains why neurons are typical neurons in the brain have thousands of synapses
*  What those synapses are doing how memories are formed and so on?
*  It's a fairly in-depth topic, but it's it's core to how the brain works the brain
*  this is a it's like if computers work on bytes and words and
*  You know binary words the brains work on sparse distributed
*  Representations and it's sort of the fundamental data type everything we build on top of that
*  Once you know that then you can ask start how you build these circuits and what are they doing and what are the things?
*  They're representing it. That's sort of like a foundation layer and then HTM refers in general
*  We don't even say hierarchical temporal memory much anymore we say HTM
*  But yeah, essentially it just reflects the fact that the brain has a hierarchy of regions
*  The neocortex does and that the way to think about it. It's a memory system
*  It's learning things and it's time-based. You can't really think about the brain acting in a static moment
*  Yeah, it's constantly changing the inputs to your brain are just changing on the order of tens of milliseconds
*  Your eyes are moving all the time. My speech is changing in the order of tens of milliseconds right now
*  So the brain processes time-based data, so it's kind of an umbrella term saying like brains are
*  hierarchically structured they're based on memory they're based on time and
*  That's very generic description and then the details of what really matter. Yeah, okay, so we're gonna
*  We're gonna talk about your most recent paper and it's it's just impossible to really build up to that point
*  You know without spending a couple hours probably so so we're gonna do our best here
*  But I think we can do better than that Paul. Oh, okay. Good. Well, I mean you are I know you're a good teacher
*  So maybe you can help us along here. Let's go back and start about one of the earliest ways that you influenced me
*  Which is your book on intelligence?
*  And I remember reading this on the public buses in Pittsburgh when I was in graduate school
*  I mean, I have very specific memories. I even actually missed my stop one time because I was reading your damn book
*  So
*  Good. Yeah, so like roughly speaking
*  It's kind of built around the work of many people but in particular Vernon Mountcastle
*  Who proposed that the the neocortex is composed of these repeated functional units the cortical column and
*  That across all of our cortex these cortical columns are basically computing the same thing
*  and if we can understand what that thing is that they're computing then we can understand the cortex and
*  What you do is propose that the cortex is making predictions about the world
*  based on comparing what's coming in to the senses and
*  Also comparing that with what's stored in our memory
*  So a prediction is derived from these things and that these predictions drive what we actually
*  Then perceive and and how we go about moving through the world
*  Anything I should we should add to that as that's kind of a bigger overall picture. Yeah, I think I think that's right
*  Would use slightly different language today today people would say and I say too that the brain learns a predictive model of the world
*  Yeah, I don't think I use that particular phrase in the book
*  but that's what I was talking about and so the idea is that you know if for a long time was if people thought of
*  the brain is like an input output processor you put in some century data and you get some action and
*  Many people including myself and when I wrote the book
*  This is the topic of the book was like no, that's not right
*  The way to think about the brain is it learns a model of the world
*  it's a very detailed model the world is there's a incredible number of things you and I have learned in our in our lifetime and
*  That model when you have sensory input comes in it invokes the model and the model makes predictions about what's gonna happen next
*  And those predictions can be at the very low level like what I'm gonna feel when I put my hand on a desk or touch
*  My coffee cup or move my eyes and it could be at a very high level like what's gonna happen if I do this podcast
*  With you would and what might its effects be and so that's the way and I was arguing on intelligence that we need to think
*  About the brain as this sort of memory or predictive this memory based model of the world and how that's a great way of attacking the problem
*  Asking how can you build a model and how can that model make predictions and that's essentially the research paradigm
*  We followed at Nementa is to say how does the neocortex build a model the world how does and that model?
*  How does it make predictions about future events? That's a sort of constraint on the model and says, okay
*  You know we can ask how do neurons make predictions? We actually in our 2016 paper, which was titled them
*  Why neurons have thousands of synapses?
*  We introduced a major new theory about that that there's an internal sort of depolarization state of neurons in the cortex
*  Which represents a predictive state?
*  And so that sort of influence our thinking all along but the simple way if you're new to this is the neuroscience just think about
*  This when you're born you really don't know about anything
*  You don't know about buildings and cars and trees and computers that you don't know about any words
*  You don't know any particular language
*  You don't know about the continents or the countries and so on you have to learn all this stuff and it's stored in your neocortex
*  and you build this model of the world it's in the model is in the stored in your neocortex and
*  Question is how does he how do you learn that model?
*  How is it represented in neurons and then you know?
*  How does it work and that in a nutshell is what I was arguing in on intelligence?
*  That's what we ought to study and that's what we do and our most recent paper the one this was posted a couple weeks ago
*  That really gets at the core of this if we think we figured out the key ingredient here
*  We think we've broken the code on this but that's all been in the same vein
*  So on intelligence was sort of like hey, here's what we should be doing
*  And so here's what I'm gonna do for the next 10 years
*  And and by the way a lot of people had a lot of people love that book
*  Influence quite a few people. Oh, it really did and I really think that it's um, it's a great primer
*  It's it's really engrossing and it's convincing and it's it's really well written and I really think it's a great primer for
*  Just the series of studies that that you've done leading up to the one we're gonna talk about
*  It is I should just mention and complete this if the book is well written
*  I'm gonna give credit to Sandra Blakeslee who is a professional
*  She she is a science writer and she basically helped me make the book readable
*  More readable than I would have so she's a she's listed on the book
*  I just want to point out that that's one of them one of the things I wrote that book
*  I said, you know what?
*  I really want to make this readable and I want it to be a great book and and I think I'm a pretty good writer
*  But I know that I'm not a professional writer and and so I engaged her to help me do that. Anyway, so that's great
*  Yeah, is there anything that if someone reads it today?
*  Is there anything you feel like you got wrong in the book or if you rewrote it? Would there be a major?
*  Directional shift or anything? No, I don't think so. I did read the book again like a year ago
*  Yes, and I wasn't looking forward to it. I was going you know, oh my god. How's it gonna be? You know, and it was pretty good
*  Yeah
*  There's some things I got it wrong in there sure small things
*  But I think in overall the tone and the basic message is still correct. I am writing a new book
*  I've started it. It's sort of a follow-on but but it basically says okay in the last 12 years or whatever
*  It's been we've made a huge amount of progress on this thing. I want to tell people about it
*  We have really cracked a code on this and it's very exciting
*  And it's gonna take me a while to explain it to everybody and we're working on in different ways
*  So I am I want to I want to rewrite the book not to correct anything but just to say hey listen
*  We've made a lot of progress here. Yeah, let me tell you about it. Well, let's talk about it. Let's talk about it now. So
*  So you're here to talk about your most recent work the most recent paper, which really just came out recently
*  Yeah, like a week ago, but it's by way, you know on a preprint server. So we've submitted it for publication
*  I'm sure it'll get published, you know, but we don't know when it actually will get to peer review, but it will yeah
*  It's in bio archive right now and I'll bio archive. Yeah. Yeah, I'll link to it in the show notes
*  But so it's called a framework for intelligence and cortical function based on grid cells in the neocortex
*  And this is just built on layer on layer of your previous work now because this is a podcast
*  I want to keep it as high level as possible, but I know that we need to dig in a little bit and and make the high level
*  Understandable. So let me let me do my best to quickly recap
*  What's led up to this and then and then you can do your thing. Okay. I'm sure okay
*  So you guys really quickly had written five papers on how cortical columns can learn sequences
*  predictive models of the sequences
*  Then you moved on to doing the same sort of thing but with sensorimotor sequences
*  So now we're dealing with locations and movement. So you bring that into the four
*  Then you take another leap you theorize that one way to accomplish this was if the cortex or cortical columns
*  Contains something like a type of cell found in the hippocampus called a grid cell
*  that's known to encode an animal's location in the environment and
*  I should say all these theories in all these theories you map the processes onto specific layers in the cortical columns
*  So you keep it very biologically plausible and now we come to the current work
*  With a thousand brains theory of intelligence and this framework that we'll discuss
*  So maybe you can take a second to expand on
*  That very understated summary of mine and then talk about what's new with what we're I think that was a good summary Paul
*  Let me just try to say in a slightly different way
*  Yeah
*  if you imagine
*  Your brain or your neocortex is in your head and there's several million fibers coming from your sensory organs
*  There's about a million from your eyes and about a million from your body and there's about
*  30,000 from your ears and these patterns are changing all the time as we mentioned earlier they're constantly changing and
*  You just imagine like a flood a changing
*  And the brain has to make sense of this and there's two reasons the reasons these inputs might be changing
*  One is that the world is changing. So right now your listeners could be sitting perfectly still and my voice is
*  Creating this changing stream of data coming into their brain
*  Into your brain. The other reason is that we move that I can imagine if I go to a house and there's nobody in the house
*  I'm learning this house for the first time. Well as I walk around the house and the inputs in my brain are changing
*  But it's because I'm moving I'm picking things up. I'm turning my head
*  So you can think about if we want to build a predictive model of the world
*  We broke it into these two parts. The easier part was what we call sequence memory
*  It's like okay
*  I'm gonna listen to a melody and how do I learn the melody how I'm gonna make predictions about it
*  That's where the world is changing the vast majority of the time the inputs of the brain are changing because we move and that's a
*  Much more difficult problem, but it's a related problem
*  So we tackle the first one the sequence memory
*  then we started thinking about how it is we build this sensory motor as you use the term earlier a sensory motor model of
*  the world and that was much more challenging and
*  it took us a while until we figured out this this sort of trick that we think the brain is doing and
*  That's related to the grid cells that we realize that the that everywhere in the brain everywhere in your new cortex
*  Everywhere throughout the near cortex there are cells that must be representing a location and the location is not
*  It's kind of interesting how they do this, but it's it's a location relative to other things, right?
*  So if I'm looking at a door there are cells in my visual cortex that represent the location of
*  features on the door relative to the door
*  It's like I put some sort of reference frame around the door
*  And then once we realized this is a novel idea as far as we know we don't think anyone else had really realized
*  This was going on in the near cortex
*  Once you realize that this this location segment was pervasive
*  then all kinds of things fell into place and we can say oh my god, we understand how it does this and how it does this and
*  How it does this and then we said how could rain represent locations a very odd thing? How could neurons know?
*  You know where something is relative to something else out in the world out there
*  And that's when we had the idea that let's go look at grid cells
*  Because as you mentioned grid cells are in the in the hippocampal complex
*  They're actually in a part of the brain called the the enter rhino cortex, which is part of the hippocampal complex, right?
*  But it's an older part of the brain. It's small and a human it might be about the size of your pinky and
*  Those cells which have been very well studied as you said they represent location. They represent the location of my body
*  Or anybody's body relative to the room you're in or the environment you're in
*  We said all nature figure this out a long time ago figured out how to represent where you are in the world
*  In India for navigation
*  we said maybe the cortex is using the same thing and maybe those grid cells are also now in the neocortex and
*  We're pretty certain that's the case. And so that was like that's leaves us up there
*  So all of a sudden we have like the brain is just like everyone thought about it
*  But now we have this entire new functionality that's going on everywhere, which is this location processing
*  Something appealing about this idea also is that the brain is not known to reinvent new
*  Structures and things so it builds upon what it has already
*  So it's appealing in that sense that something older evolutionarily would then get
*  Repurposed and maybe changed a little bit but repurposed in the in the neocortex as well
*  Yeah, in fact, in fact these grid cell mechanisms are very complex. They're very kind of clever. Mm-hmm
*  and so my thinking is
*  And this is speculation that these were evolved over many many, you know long before humans and even man
*  Probably before mammals, but maybe certainly early mammals
*  And so we we had to figure out how to get around the world and that was something he had to do from a long
*  Time ago
*  And so there's been under a lot of evolutionary pressure to figure out how to figure out where you are in the world
*  And now what the neocortex does it says? Oh, yeah, look at that. That's a that's a great algorithm
*  I'm gonna use it for something else just like you said
*  In the paper we have a figure and I'll try to paint it for your listeners
*  we show a
*  rat moving around in a room and
*  this is the kind of things that neuroscientists study when they study grid cells and they and the grid cells help the rat make a
*  Map of the room and we're in where things are in the room
*  And so and you do this too
*  So when you walk into your house or your office, you know where things are and you recognize it
*  That's all happening in the grid cells and what we and then we said look the same thing's happening in the neocortex
*  Instead of your body moving around in the room
*  Imagine the finger your finger your finger has a sensory organ. It's a and it's touching things
*  Well, when you touch things with your finger, it's moving around objects
*  It's like it's building a map of an object by touching in different locations
*  And so just like the body moving around in the room your sensory organs whether it's your retina or your finger are moving around
*  Objects and they're learning to make a map of the object in the same way that the end to Rhino cortex learns maps of rooms
*  It's a very analogous situation
*  But of course we can do this for all different parts of my body
*  So I can do it my hands my feet my legs my eyes my ears and so on
*  So the cortex is safely took that algorithm that evolved a long time ago for navigation and mapping of environments
*  Is that I can learn structures of objects in the world and where they are and and and what they look like
*  Very good
*  so
*  so a couple things that in this paper that were already known and have been sort of repurposed and like
*  grid cells like we've just been talking about and
*  A few things that are new and and proposed as theoretical one is that cortical columns learn
*  Complete objects they don't learn features necessarily like each cortical column learns. It's a complete object within it
*  to that that there are grid cells all over the cortex because they are in every cortical column and
*  Three you guys propose the existence of a new type of cell called a displacement cell
*  Yes, that are also in every cortical column and all over the cortex therefore
*  So do you want to just expound on those a little bit? Yeah, sure
*  The order is slightly different first
*  We we said oh there must be grid cells throughout the New York cortex
*  And then once you realize that then you say oh if there are then every column can learn complete models of objects
*  And then when we said oh if they're learning complete model of the objects we deduce there must be this thing called the displacement cell
*  Let me just break it down a little bit. So the grid cells are very well known
*  they're studied that Moses got a Nobel Prize for their for their discovery and
*  Originally thought the proposal that there are grid cells throughout the New York cortex was going to be completely novel
*  But it turns out there's some people who have been observing this
*  I don't think anyone said oh, they're everywhere
*  but people have been seeing evidence for them in certain parts of the New York cortex and
*  We would have predicted that but so this experimental evidence supporting that so what we were saying is it's everywhere
*  That's perhaps the new thing there. Yeah, and then as far as we know no one the displacement cell thing is completely novel
*  It's funny. Some people say well, there's no evidence for that. Well, that's what theoreticians are supposed to do
*  we're supposed to propose things that no one has seen before and
*  So I'm very confident that they're gonna be found and so to me that's some people think of the very speculative
*  I think of just the opposite. This is where this is a bold prediction
*  It is and so it's if someone said oh look we found grid cells everywhere in the neocortex people might say yeah
*  Well other people might have been seeing them. So that's not such a big deal
*  But this is something no one's ever thought about so this will be like, okay
*  you know when we find them that'll be sort of a nice thing, but it's really a
*  We deduced it you can deduce the the presence of these by the I should mention that one of our scientists
*  Marcus Lewis was the guy originally came up with that idea displacement cells
*  We have been working on a particular problem and he came up with that solution, which is very nice
*  it's great that we can propose things that we're pretty confident that exists and
*  and that no one else had thought about before and
*  so when they're discovered or not then that'll either
*  Support the theory or falsify it. I mean if you had to guess right now
*  You like speculation and we like it here on this show. So that's good
*  So what do you what proportion of neurons like within a given cortical column?
*  Do you think are devoted or are these grid cells and displacement cells?
*  Okay
*  Well, let me let me paint a picture for your listeners if you took a square millimeter of cortex of the human your cortex
*  So you have a square millimeter and maybe two and a half millimeters thick that cuts across all the layers
*  There's about a hundred thousand neurons roughly in that square millimeter
*  So that's a lot of neurons and you can break it down somewhere
*  You know, you could say argue there's maybe six layers or ten layers depending on your lookout
*  Let's just say we break into ten layers that means there's ten thousand neurons per each layer of cells a different type of cell types
*  Yeah, these are all rough numbers. Yep. And so I were to say
*  You know how much is dedicated to grid cells? You might say well one of those layers
*  So it might be in a square millimeter cortex
*  There might be several thousand to ten thousand cells that represent the grid cells and there might be similar sort of you know
*  You know several thousand to ten thousand neurons that represent the displacement cells
*  Those are very we're talking very rough numbers. It's not it's not hundreds of thousands. It's not ten
*  Yeah, you know, but that gives you sort of a flavor for and these numbers
*  We're always testing these numbers against both the theory like how many neurons do you need to do these things and also with what's experimental?
*  Empirical evidence about like what do we know about grid cells? What how dense are they in the entorhynic cortex?
*  How many are there and things like that? So we're constantly testing these ideas and those are all those are all copacetic
*  So that gives you a flavor maybe you know, maybe one-tenth of the neurons in the cortex are related specifically to this location stuff
*  Do you propose experiments to people because they're you know, I mean when I retired from neuroscience
*  We were we were able to even at that time which was not long ago
*  But you can get into a layer specific you you kind of know where you are within a layer of a cortex
*  So you could really target these things with electrodes for instance
*  Yeah, so here's how it works we do propose experiments
*  But it's very dependent on whose lab we're talking sure. Yeah. Yeah every every lab has their own experimental techniques. Some are using
*  Probes of tetrodes some are using optical imaging. Some are using fMRI
*  Some have different experimental animals. Some are using humans and so on and so you can't just blankly say
*  Here's an experiment. You have to sit down with the the research team and say what is your lab do?
*  What do you guys and let's come up with an experiment that makes sense for what you guys do
*  And so that's how we go about it. There are many many testable predictions in our work, right?
*  And we have numerous collaborations and numerous conversations all the time with people about how to test these things
*  And of course as you know
*  These experiments are very difficult to do
*  If you want to do even something on a rodent
*  You might spend a year getting ready to do your experiment right a year just getting ready to do it
*  Then another year collecting your data hoping the animals don't all die and you know something but it doesn't happen
*  You know, so it's a multi-year effort. Just you know, it's not something for us to just come drop in one day say hey test this
*  Yeah, it's a you know, you have to be sensitive where they are
*  what we found sometimes is even more successful is that a lot of
*  Experimentalists have data they've collected in the past and we can go back to that
*  Pre-existing data and look for things they didn't know that they had yeah
*  And that's that's quicker because there's no new experiments required. You can say okay
*  we predict we'll find the following things in your data and
*  And that's been a fruitful method for us
*  Well, okay
*  So let's talk just a couple minutes more about the sort of the features or the fallout from the theories, right?
*  so so one of the things is that
*  You propose that every cortical column across the cortex codes for an entire object, right?
*  Yeah in the paper you talk about how objects are made up of sort of sub objects
*  You use the example of a coffee mug has a it's a handle and a cup and sometimes a logo and things like that
*  And so presumably each of these I keep want to say features but sub objects of the object. Yes
*  That's right. It's objects of objects what a more complex object that has more
*  Sub-objects would that require more cortical resources then?
*  Almost the opposite it's first of all, we just have to recognize the world is structured this way
*  I mean the world is structured of things made of things made of things made of things
*  You take you take a car and you can then you identify
*  Dozens of sub components of that car doors and handles and wheels and hubcaps and hoods and so on each of those is sub
*  Components and so the world is structured this way and when we want to learn something new you don't want to learn
*  Everything new again. You basically would say oh, this is like something else
*  It's got these components arranged in this way. And so the brain must do this
*  This is not an option. The brain has to build a model the world
*  It knows what cars are it knows what computers are knows all these things and knows how they work
*  this is all in your head and so the neurons must represent this structure and
*  Not many people think along these lines at least when it comes to neuroscience
*  but so with the questions how do neurons represent this sort of object of objects structure and
*  This is a problem. I identified a long time ago
*  I said, oh my gosh, the neurons have to do this. It seems really hard. It seems really hard to imagine how they do this
*  So we've been thinking about it for a long time and for years and just about a year ago
*  After we started understanding the true nature of grid cells and how they work and the inner workings of grid cells
*  Then we came up with this displacement cell idea
*  Which says oh displacement cells can represent that structure of structure and they can do it very efficiently
*  This is the key of thing about it in the paper
*  I mentioned this but I'll just give you some numbers on it, you know
*  Let's say I want in the paper
*  We talk about a coffee cup and a logo and we say, okay, there's a logo
*  We use the memento logo because we have rights to that but we'll use a brain inspired logo for this. Okay. Okay fine
*  Yeah, great
*  And it's okay. So I've learned a logo
*  I know that and I have this coffee cup and I know that I want to learn a new object
*  Which is the cup with a logo. I don't want to relearn either of those things
*  I just want to somehow say there's a new object to compose the previously learned objects and the
*  Displacement cells through a trick which we won't be able to describe on the air here, right?
*  The displacements do this extremely efficiently. I mean, I'm not I'm not joking here
*  it might be as simple as the activity of 20 neurons or
*  Maybe 50 neurons can represent a new object which is composed of the logo in the coffee cup
*  So it's an extremely efficient methodology for
*  Building complex structures and so it's you say is it need more neurons?
*  Yes, well, we need neurons to represent this but it's far more efficient than if I said, okay
*  Here's a new object. Let's remember every feature at every location for this new object
*  You know if I can build a new composite object using a hundred active neurons
*  You know in a population of this yet several thousand if I can ruin that new structure that efficiently in very in one fell swoop
*  and in essence in one moment of
*  Perception that's an extremely efficient from a learning point of view and a storage point of view and well
*  It's also we're not talking about 20 separate distinct neurons, right? Because these can be overlapping overlapping populations
*  Yeah, exactly. So imagine I'm on a cortical column and I'm and we have these our proposed displacement cells
*  maybe I have 10,000 displacement cells and
*  200 are active at a time. Well, there's there's almost an incredibly almost infinite or bigger than the universe number of ways
*  You can pick 200 cells out of 10,000
*  So we have a very large representational capacity and so even that one column can learn
*  thousands and thousands and thousands of composite objects
*  The numbers are surprising how much capacity there is in these sparse representations
*  And most people just don't think along these lines. Most people think like, you know, a region of the cortex is just
*  Doing some sort of filter and passing information on some place else and we're saying no, these things are incredibly powerful
*  And in the in hindsight we think the brain has to know this stuff. Where is it gonna store it?
*  You know, we kind of think like oh somewhere up in a higher level in the hierarchy some prefrontal lobe thing
*  Well, the prefrontal lobe looks like everything else. So it makes sense that everything is sort of stored everywhere
*  That's a much more copathetic philosophy
*  It's not that it's not that the neo-correct is completely uniform not everything learns everything
*  But everything is able to learn some structure in the world
*  So we know the brain is hierarchical and the common understanding these days is that processing
*  Along the hierarchy goes from sort of simple lower level features like edges line detectors to abstract
*  features like whole objects, etc
*  So how does this framework compare to what's generally accepted about hierarchy in the brain now? Yeah, sure
*  So it's more like that's an incomplete picture. It's not completely wrong, but it's really incomplete
*  So first of all, if you actually look at the wiring of the neocortex, you know
*  The the white matter how regions project to each other. It doesn't look like a regular hierarchy
*  It looks really messy and what you know connections are going all over the place
*  It's like doesn't really fit the description of a nice hierarchy
*  Even the first paper published on this back in 1991 by Thelma and Vanessa
*  They made this famous picture of the monkey's brain how it all the different regions are connected and even back then they said
*  It looks like basically half of all half of all the possible connections in the brain exists, which is incredibly over connected
*  So it's not shouldn't be a surprise when we say that the brain is not strictly hierarchical because it doesn't look that way sure
*  And then the second thing is is when people observe
*  neurons if you go back to in the 60s these two famous neuroscientists who will in diesel and
*  They won a Nobel Prize for they work they work
*  They were basically using anesthetized cats and so the cat was a not awake and they would try to get these cells to be
*  Responded and they say well it looks like these cells respond to these simple features
*  We now know that you have in an awake animal who's actually moving around in the world
*  Yeah, those those cells don't look like that at all. They seem to have very different response properties
*  So this idea that there's these simple feature
*  extractors goes back 50 years and it's based on the
*  On the experimental paradigm of an anesthetized animal and we now know that that's not what it looks like
*  There's a lot of data which does not support the idea that there's this
*  Hierarchical feature extraction thing and people just haven't abandoned it yet and our theory explains all this stuff
*  It explains why these cells behave weirdly we talked about this in some of our papers
*  And so we're introducing this idea that like a single cortical column whether it's in the primary sensory region
*  That's getting input from your eyes or ears or something high level is able to learn complete models of objects
*  And it's a very sophisticated processor
*  They all can't learn the same things like a part of your visual cortex can only learn models based on visual input and only
*  model it can only learn models based on some part of your visual input and then the thousand brains theory which we
*  Labeled this is that you've got thousands of these models if I'm looking at a coffee cup and I'm touching a coffee cup
*  I have tactile models of the coffee cup
*  I have visual models of the coffee cup all these are running in parallel in different cortical columns and they vote and so many of
*  These long-range connections can be understood as them all voting
*  It's like like if you and I were looking at the same object
*  But we neither one of us could be certain what it was and I said, you know, you know Paul
*  I think it might be a coffee cup or it might be a soda can or it might be a
*  Hand-towel computer and you say well, you know, I think it might be
*  Tennis ball or soda can or you know a chair and then we said well, let's vote and then we all guess it's a soda can
*  So it's something like that
*  So it's a very different view instead of like instead of some some this pyramid of information coming up to some
*  One big model of the world the cortex is actually thousands and thousands of models and all running in parallel and they're voting all the time
*  It's a completely different flip and how you think about it
*  And I'm very confident that this is actually what's going on and it doesn't mean that there isn't hierarchy
*  There's still like some models become inputs to other models
*  But it's not like there's feature extraction and you get to one model
*  It's like there's models and models and models all over the place
*  the examples that you give and what we've mostly been talking about art are visual and or
*  Tactical so it's easy to kind of think of how this would work
*  How the framework would encompass these things in a location based coding, right?
*  It's a little more difficult to think about how it might apply to other cognitive abilities like like language and math
*  So how do we conceptualize that sure? Well, let's just start with some physical evidence
*  We get we mentioned Vernon Mountcastle earlier and he said every part of the cortex is doing the same thing and it looks that way
*  The circuitry looks the same way and all the circuitry we've proposed for the for visual and tap in somatosensory
*  Cortex it looks the same everywhere
*  So the evidence would suggest that whatever however these cortical columns are working in vision and touch
*  They're working in language areas and high-level thought so if it just on that pure physical evidence if we said, okay
*  The cortex works on location spaces. Well, then language must work on location spaces, too
*  So we're gonna start with as a walking in assumption now. Let's just take language. For example, it's we don't
*  We don't really we haven't focused on this part, but there's some interesting intriguing ideas
*  Take these displacement cells we propose they represent the relationship of an object to another object
*  And one of the things you can do with them is you can create a recursive or reentrant structures this way
*  Like I could say here's a coffee cup with a logo and the logo has a coffee cup and the coffee cup has a logo
*  it's like a nested structure, right and
*  You think about language much of language is this sort of recursive and reentrant structures
*  You have objects and actions related to other objects and actions and those nested structures in language and so on
*  So there's a hint there that hey, you know this basic idea of representing things
*  In sort of relationship to other things and relationship to other things in a sort of recursive form could form the basis of language
*  Which is very I think it's gonna turn out to be true. There's another there's some studies that have been done
*  Using humans who are doing sort of mental imagery tasks. Yeah, and and
*  These are sort of high-level thinking and thoughts and what they've shown using some clever
*  Imaging techniques fMRI techniques on humans doing these mental tasks
*  Is that there appear to be that when we think about these high-level tasks?
*  We assign objects in location spaces that they can demonstrate this and I won't explain how but it's clever
*  They can show that when we think about structures a mental structure of things in the world
*  We kind of locate them in a framework that's like a physical it's almost like a physical framework, but it's not it's a mental framework
*  That's sort of like a location space. So this is an area that
*  That it's gonna be fascinating to pursue
*  but I I'm very confident that that all have a lot of thought can be understood in this location space using grid cells and
*  And even though it's a we don't have we don't really understand it very well yet
*  It gives us an ability to say look it's gonna be like this
*  So now we have a we have a hook to go into these things and start thinking more about like, okay
*  How is language going to be represented? No one knows right now? No one has any idea how the cortex does language
*  Yeah, and and now I have a framework. It says look, I think it's gonna work under these principles
*  It's gonna work just like this and the columns in them in the view and the parts of the brain that do language are gonna
*  Work on these principles. So let's figure out how language maps onto them. That's exciting. That's a very exciting thing for me
*  I think it's exciting too. It's intuitively appealing as well and and
*  Like a good theory should it really opens up doors to new ways of thought about approaching all different levels of cognitive
*  Capacity that's why we that's why we labeled our paper a framework
*  Yeah
*  For cortical theory or cortical function is because it's very broad and I can't say I have a theory of language
*  I have a theory of this right
*  I have a framework by which you can understand these things and the framework is novel and it's really interesting and
*  Once you get it and people are getting it's like, oh my god, this is incredible. Maybe this could explain everything maybe we'll see
*  Yeah, good. That would be the title of the next book or paper. This explains everything
*  Well, so we didn't touch on on everything that's in the paper so I strongly recommend people look up the paper or just
*  You can just go to the mentor comm and we have all these resources all these resources listed there including a
*  Companion guide to the paper
*  So if you if you're not comfortable reading neuroscience papers, they can be daunting
*  You can read the companion first and sort of explains it in lay terms. So keep up the good work
*  I don't need to tell you that because you are gonna forge ahead no matter what anybody says, which is great
*  So we have just a few more minutes here
*  I'm wondering if I can ask you some sort of broad and speculative and general questions. Yeah, let's go for it
*  Okay one one of the things that you are really well known for is
*  Demonstrating our cortex you bring out a dinner napkin and you say it's yeah, it's about the size of a dinner napkin
*  So do you have it on you? There it is. Okay. So the question is how often does that thing get washed?
*  Well, actually I've had different ones
*  Oh, okay. Sure. Sure. I recently switched to this one because it's kind of like a
*  Gray green color, which is more sort of brain color ish. Oh nice
*  Yeah, it doesn't have the red for the blood in it. It doesn't get washed very often
*  I don't think I've ever washed this but then again, I don't use it that often
*  Well almost it's in your talks a lot, right? I never wipe anything with it. It's like I take it out and I put it away
*  Yeah, that's right. That's right. I suppose I should wash it, but it's not like I've been sitting around the dinner table
*  You know, it's it's kept in my bag or on someplace
*  When you gonna learn how to fold that thing into a
*  Folded yeah. Yeah. Well, it's interesting because you can if you actually took the new cortex out of your head
*  You can't actually iron it flat. It's like a globe. It's you can't you can't take a globe and iron it flat
*  It's you know, it so it's just it's a rough idea
*  It just what it what the great thing about the napkin is that people realize that that thing which is only that big is you
*  Right everything and in there is everything you've ever learned and everything you ever known every experience is in that little sheet
*  It's kind of looking at it. It's like oh my god, that's me
*  Yeah, it's powerful. So actually last
*  Well two episodes ago rather I had Terry Sanofsky on the show and he talked about this being a golden era of
*  Neuroscience that when people look back and this is a guy who's been working on this for a long time
*  Yeah, yeah, because we have lots of data pouring in and we have a lot more
*  computational ability and you know, he works a lot with the deep learning and other
*  AI techniques
*  So with all these all the data coming in we can soon start to really test these
*  frameworks and theories that are being proposed like people like you so do you think that this will be seen as the golden era I
*  Like Terry is a friend of mine. I would I
*  Have a slightly different take on what that is. Mm-hmm
*  We've been collecting lots of data for for a long long time, right?
*  I mean, I mean we have lots of data in the 1970s. We had lots of data in 1980s
*  You know, there's always been more data that has been tons of data that has been unassimilated into theory and
*  We are now collecting it even faster rate
*  But my attitude has been the data itself doesn't isn't gonna give you an answer
*  What we've been lacking is sort of a theoretical framework in which to interpret these things
*  That was true back in the 70s
*  What I read an article by Francis Crick in 1979 that basically launched my career neuroscience
*  And fresh crick said we are lacking a theoretical framework. We don't you know more data is not gonna help
*  So that's what got me going
*  so, you know to me it'll become a golden era in neuroscience if
*  These if these frameworks are correct
*  And for example, like if the work we were doing right now if that turns out to be correct
*  That will begin a golden era neuroscience if we don't have a theoretical framework that understand
*  Then we're just gonna have a be swimming in data and we've been swimming in data for years
*  So to me the the golden era of
*  Neuroscience is when we when we go from being a pre paradigm science
*  And this is in the language of Thomas Kuhn the historian
*  We go from being a pre paradigm science to a post paradigm science
*  Like we just have a whole bunch of data
*  We have no idea what the hell's going on till like now we have now we understand what's happening
*  We can start really attacking this problem in a logical way. We have not been doing that
*  That's not where neuroscience is neuroscience is a lot of data with really almost no theoretical understanding
*  The the only place we've had real success one of the few places we've had real success in the mammalian brain is
*  In the is in the hippocampus and the and the entorhinal cortex because there's some real theories there
*  And we're trying to bring that same sort of level of understanding to the neocortex. Okay, so
*  Rudolfo Lenas, I think is how you pronounce his name and Daniel Walpert
*  They have these ideas that
*  Evolutionarily the way our thought came about is by sort of internalizing
*  movements and how important movement and has been to early, you know since single-celled organisms up
*  evolving through
*  humans, let's say and that virtually all cognition is rooted in movements and this is a little bit related to
*  Your work because you have to move your finger to understand the object to get the the location based framework going on in your cortical
*  Columns, so do you agree with that idea? What's your what's your yeah, I do I do I'm not I'm not
*  Intimately familiar with what they argued so I'm not saying I agree with everything because I really know
*  But at the level you just described I totally agree
*  You cannot understand the brain and you cannot build intelligent machines
*  that have no any sort of embodiment the way you learn the structure of the world is through movement and
*  There's an interesting twist on this in a moment, but let's just follow through on this
*  Everywhere in the near cortex everywhere that we've looked every column has a motor output
*  This is a surprising result. No one you anticipated this many years ago
*  But even primary visual cortex is the nerve the columns air project to the part of the brain that moves the eyes
*  So there's no there's even auditory cortex projects to the part of the brain that orient your head
*  So the idea that you can perceive the world and learn the world without movement is just nonsense
*  You have to move and so we think about the future of AI
*  I think robotics and AI cannot be separated. They're not separate problems. They're one of the same problem
*  Now let's just step back a second and say movement does not have to be physical movement
*  You don't have to what's important is you have to move your senses and experience something to experience another structure in the world
*  So when we sit and do mathematics and we're manipulating equations and structures in our head
*  You know those you can do that completely mentally
*  But I'm still manipulating these structures in my head. I'm trying to visualize them and how they look in different directions
*  That's there's an internal movement command that that is or like you can get like a mathematical operator
*  If I if I multiply or apply a Fourier transform, that's like a movement
*  It's like take this data and act upon it
*  so I think they're right that you cannot separate out movement and sensation and that all
*  Cognition is based on movement and when we interact with the world through our hands and our eyes we have to physically move
*  but internally once you get to high levels of the cortex movements can be more abstract and
*  You don't have to be physical about it, but the same principles apply
*  I know that we have to move on here because we're up against time
*  So I have one more quick question for you. When will we know what we mean when we say consciousness? Oh gosh
*  I try to avoid the word consciousness
*  It's it's just it's just a swamp of I don't know, you know to me I
*  There's a really smart thing that the people who study consciousness that a long time ago
*  They said oh, this is the hard problem how the brain works is the easy problem. Yeah
*  Consciousness is the hard problem. I said well, it was a brilliant marketing move on their part
*  I say to them look understanding how the brain works is a hard problem
*  and there's tens of thousands of neuroscientists around the world working on it all the time and
*  And we've yet to solve that problem mementos working on it
*  We think we've made some significant progress and consciousness to me is like well, it's really even hard to define
*  What do you what is the problem you're trying to describe and it can't they can't describe it very well
*  So to me I wrote about this in non-intelligence. I made an equation
*  I quit I said, you know consciousness can be equivalent to awareness
*  And I said if I if I could turn your brain back to this morning and you you are unaware of everything you did
*  You would claim that you weren't conscious and so I basically I'm arguing that consciousness is very much related to your ability to recall your
*  Experiences if you can't recall your experiences, you'd say you were unconscious
*  You did no recollection of it and it can be as simple as that and and people make it into much more than that
*  So I look I'm gonna just I'll really
*  Bother or piss off some people who study consciousness by saying this. So let's just leave it out of the picture
*  Our focus is on how the brain works how to build machines that work that way that's a great problem and
*  If we solve that problem, we can all go home happy. We don't have to worry about consciousness at the moment
*  Let's just focus on the the real problem. We know we have to solve it's like how does this brain work?
*  This is a great place to end it Jeff
*  Thanks for all your work and guys go to new menta comm to learn more about
*  Jeff and learn and download all the papers that are they're all available to download and read so appreciate your time Jeff
*  I appreciate you interview Paul is great. It's great interview and you have a really nice podcast. So
*  honored
*  You gotta love that confidence the confidence of a theoretical neuroscientist
*  I wish Jeff all the luck and I think that what he is doing is super exciting and
*  I'd love to do that myself
*  Thanks for listening to the show. I hope that you are doing interesting and enjoyable things
*  Speaking of interesting next week. I am speaking with
*  Julie Groyer I believe is how you pronounce it and her amazing coupled spin-twerk
*  Nanooscillators that she's formed into a neural network
*  Super interesting and I'll have to ask her next week if it is enjoyable
*  Yeah, it's gonna be fun
*  See you next time
