---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4534s
Video Keywords: ['Science & Medicine', 'Technology', 'Education']
Video Views: 835
Video Rating: None
---

# BI 044 Talia Konkle: Turning Vision On Its Side
**Brain Inspired:** [August 18, 2019](https://www.youtube.com/watch?v=kBKEaJtc8dU)
*  This idea that each region of the brain and each layer of a deep net is representing information in a completely different way.
*  Now that just doesn't turn out to be true.
*  There are a treasure trove of insights in neuroscience and cognitive science that can be assessed with a new lens by being a little bit creative on how you use deep nets.
*  This is Brain Inspired.
*  You ever notice how when you give directions you don't ever use tiny landmarks like follow that road for 40 miles and then take a right when you see the can of soup?
*  Or how if I tell you the story about the time that I got attacked and mangled by an animal that may or may not have been a pet turtle, you picture some kind of creature like a turtle?
*  Or how I'd never ask you to hang onto this mountain for just a second while I pick my teeth with a steak knife or something?
*  Well, Talia Konkel thinks about these things, maybe not these exact things, and she thinks about brains.
*  And it turns out that's a good combination of things to think about.
*  In Talia's case, it means thinking about how our visual stream is organized in terms of what kinds of things are represented as one moves up the classic ventral visual stream hierarchy
*  from low level features like the edges and orientations of Hubel and Wiesel up to the higher level full on objects.
*  She calls it a tripartite organization because she has found that our brains make distinctions between big inanimate things, small inanimate things, and animate things like animals basically.
*  She even invented a tool and a word to name that tool to study these things.
*  So we talk about all that.
*  By the way, I am Paul Middlebrooks and welcome everyone to the show.
*  We also talk about how she's used deep learning networks to study this tripartite organization as well, based off of some of the work of my previous guests like Marcel van Gerven and Dan Yehmans.
*  We talk about how deep learning has actually changed the way that at least some people even teach visual neuroscience, which is an interesting thing I hadn't thought about.
*  Talia will be giving a talk at the upcoming Cognitive Computational Neuroscience Conference in September.
*  So we talk a little bit about the conference.
*  And to remind you, you should check that out at CCneuro.org, where you'll find videos of the talks given during all the previous years of the CCN conference.
*  And soon you'll find a video of her.
*  I will link to the conference and all that we talk about in the show notes at braininspired.co.
*  Stay well, dear listeners.
*  I have appreciated all of the support and the emails I've been getting with questions and suggestions for the show.
*  I make this thing for you and for me.
*  Obviously, it's not for a general audience, but a curious and already rather knowledgeable audience that is you.
*  So I hope it hits you in just the right spot.
*  OK, here's my enjoyable conversation with Talia Konkle, whom you can also find on Twitter at Talia underscore Konkle.
*  Talia, thank you for being on the show and welcome.
*  Thanks for having me.
*  I can tell in my visual stream, you're an animal.
*  So just a little, little foreshadowing there.
*  I couldn't resist.
*  It's true. Critical division success.
*  Consider your visual system working pretty well.
*  Yes, yes.
*  You are an animal who is also a principal investigator as you run your lab.
*  You run your cognitive and neural organization lab at Harvard, where you use behavioral experiments and fMRI imaging and modeling to understand how the things that we represent in our minds physically are mapped in our brains,
*  essentially. Yeah.
*  To ask those questions, you use visual processing, in particular, how we represent objects within the ventral visual processing stream.
*  And maybe another way to say what you do is that you're discovering how our story about the ventral visual stream is wrong.
*  Would that be accurate?
*  Well, we'll just add an updated layer.
*  I think that there's something to the hierarchy, the visual hierarchy, that's sort of the classic story of how information gets routed from our eyes up, you know, through the ventral stream and to higher level representations that help us recognize the world.
*  And I think that's gotten us a really long way.
*  And I think that there's real truth to it as evidenced by all the successes and deep learning that are taking advantage of that kind of architecture.
*  But I think it's just only half the story.
*  And so I think I try and think about what we can learn from the other half, because the cortex is two dimensional.
*  Yeah.
*  The hierarchy is only one axis.
*  So I think about how things are mapping along the other axis and what kind of insights we can get from that.
*  Yeah. And one way to say that, and we'll dive more into this later, I suppose, is that the visual stream research has focused on, let's see, I guess that would be latitude.
*  And haven't looked at the longitude, for instance, or vice versa.
*  So that's an interesting, I wouldn't say short-sightedness, but it's an interesting development.
*  So you mentioned deep learning.
*  And this is a show about sort of the intersection of artificial intelligence and neuroscience.
*  And I have heard you say for a long time, there was like a certain way to teach the introduction to visual neuroscience.
*  And now that deep learning has come into our world, that way to teach it has been altered.
*  Could you could you elaborate on that? How has it been altered?
*  Yeah, sure. I mean, one of the things that you have to do when you teach any a class in cognitive science or cognitive psychology or vision is you have to introduce the problem of vision to people who have maybe never thought about it.
*  And the problem of vision is that you think you just see the world directly.
*  Of course, that those are objects and scenes and people in it.
*  But that's just the mental model and a construct in your head.
*  You don't actually look out at the world.
*  Light comes in to the system and it's constructed to form this rich model that helps us actually act in the world.
*  We don't directly see the world itself.
*  And so that's the problem of vision.
*  And it's hard.
*  It's so easy and effortless, but we couldn't we can't even make machines do it.
*  So that was like the standard story of convincing people.
*  So, you know, young minds coming in to learn about cognitive science, like vision is really interesting problem.
*  It's so hard.
*  We can't even make machines recognize that whole motivation for why it's fun to study vision is completely out the window now.
*  But we have a similar motivation, which is like the problem is so hard that we couldn't make machines do it until five years ago.
*  And now there's a huge, you know, confluence and, you know, all kinds of cross disciplinary insights going back and forth between machine vision and human vision and biological vision to try and understand what's going on.
*  So it's still a very exciting time to be studying vision for different reasons than maybe a few years ago.
*  And you can still you can say, and damn it, it is still hard.
*  And it's still hard that it's easier than it was before.
*  Or at least there's new ways of approaching it.
*  Nice. Yeah.
*  I mean, I had not thought of that.
*  And I heard you mention that.
*  I think you're in a discussion panel or something.
*  And I thought, wow, that's, you know, that's a that's a real big deal to change sort of the paradigm.
*  Yeah.
*  So, yeah.
*  Yeah.
*  Every intro lecture.
*  I know it's exciting.
*  So, hey, you're going to be giving a keynote address here in a month and a half or so in Berlin at the Cognitive Computational Neuroscience Conference.
*  And that conference is about bringing together people from the brain sciences and from the AI sciences, essentially.
*  So you've been in panel discussions about these things and you've had a bunch of abstracts actually.
*  You presented a bunch of abstracts last year at CCN.
*  What is your take on how cognitive science and computational neuroscience and AI can best work together?
*  Hmm.
*  Oh, that's a really good one.
*  I mean, one of the interesting things is that we're still figuring out how and the number of ways and that they can inform each other is still sort of unfolding.
*  I think if I had to like put one principle out there for people interested in this interdisciplinary intersection, it would be to sort of treat all the fields as equal partners in the quest for insight, because it's easy to think of the advances in the other field purely as tools.
*  So I care about the brain and I'm going to use machine learning insights to care about the brain.
*  And so I need someone to help me to just do my models.
*  And that's sort of like, you know, it's not sort of respecting the insight and innovation on the machine learning side.
*  And then it goes the other way, too.
*  Like, I want to make a model perform better.
*  I want some insights from brain science, but I don't actually want to, you know, I just see if you can tell me how to understand my model.
*  But, you know, I'm going to I'm going to build it this way or something like that.
*  So there's there's like room.
*  And honestly, I think if anything, it's more that I mean, is my view, but the neuroscientists may be wanting the machine learning tools and need to get those skills.
*  And I think the most important thing is to actually respect the innovations and insights on both sides and sort of find our way together.
*  So it's a real convergence rather than a sort of usurping or for sort of the tool use without really sort of benefiting from both sides.
*  So that's that's very general advice.
*  But it's an it's an interesting question whether that approach will effectively speed up.
*  Will Harold a more effective research approach?
*  Right. Then so it's either borrowing the tools or diving in and a full fledged respect.
*  Yeah, exactly.
*  And maybe in truth, as it often is in science, like you need all the ways you need the people who use it as tools and you need to be so that's a less less interesting answer.
*  But usually it's true.
*  Like, thank goodness we have people who want to use those tools and people who want to dive across and and that like actually it's the set of all of these approaches together that are important.
*  So so it's not a great answer.
*  But but where where I land is to try and really deeply engage in the other side and try and pull as many cross disciplinary insights as as possible.
*  A respectful animal.
*  You are.
*  I try.
*  What are you going to be talking about?
*  Do you know?
*  I mean, I know it's still, you know, there's plenty of time.
*  We have weeks left to sort that out.
*  I know that the pace of projects is interesting.
*  I never actually quite know what I'm going to talk about till a couple of weeks before.
*  And so I think I have at least two weeks still to start mission critical.
*  Yeah.
*  But yeah, I think there's sort of maybe two broad areas that I'm excited about in terms of directions my research is going and projects to that end that will make it in or some somehow make it into it into the talk.
*  Or maybe one of them will is one of those the the visual stream, the ventral visual stream story that we might talk about today.
*  Yeah, that's right.
*  So one is about like the importance of topography in brain organization and what we might insights we might get into understanding brains by thinking about topography and sort of thinking about how we might add those to deep nets, which don't have a lot of topographic constraints.
*  Right.
*  And then the other is about what's the goal of the ventral visual stream in the first place.
*  And there's been a lot of focus on object recognition and Scott is pretty far.
*  But I think we're starting to move past that and think about what what other goals might give useful feature representations.
*  And so that's we've got some work on that end as well.
*  So it's a choose your own adventure, which would you prefer?
*  Yeah.
*  Is that how you're going to present it at the keynote?
*  Well, I don't know yet.
*  I have two weeks to figure it out.
*  That would certainly be memorable.
*  What would you guys like me to speak about?
*  Just prepare one talk or the other.
*  I don't think I can pull that off yet.
*  What is the most critical open question that's driving you these days in your research?
*  Yeah, those two.
*  Yeah.
*  Well, that's that's yeah.
*  Obviously, right.
*  I mean, yeah, that's where we're going after.
*  Like, what's the real goal of vision?
*  And, you know, what how should we think about moving that forward now?
*  And then and then for me, I've always loved topography and why things are where they are.
*  You know, is that happenstance?
*  Is that arbitrary?
*  Is it informative to the function or the nature of computation?
*  And and I think that those are really deep and hard questions.
*  And to answer them requires, you know, development and thinking about evolution and, you know,
*  computational models of features.
*  And it's just a really rich question to try and get sort of normative style ideas about why the visual system takes the form that it takes.
*  So that's that's what I think is the critical open question that I'm interested in.
*  The evolution route is always fun because there are just so many just so stories that you could tell yourself.
*  And so you have to be really careful.
*  Yeah.
*  But you can make a good story.
*  That's true.
*  I know I actually think that deep nets are kind of an interesting opportunity to start to.
*  Provide different ways of thinking about how things are the way they are.
*  So, you know, there's generally the empiricists who think much of the structure is learned on top of a very general purpose architecture.
*  And the nativists who think, well, the architecture is very specialized to what we do and experience comes in and just sort of fine tunes it.
*  But it's already in there.
*  And, you know, there's many just so stories and models to either end.
*  But I feel like deep nets have really are sort of like an empiricist, you know, new tool to really go, well, what is learnable from what kinds of input and how sparse a feedback signal?
*  And so I think that, yeah, I think that there's room for sort of modeling developments that start to operationalize some of those just so stories to go, well, what if the signal that helps train the network is, you know, something like animate, inanimate rather than a thousand way object categorization?
*  Or, you know, what these kinds of things become operationalizable in a new way?
*  Or what if the network only saw this much, you know, what could it learn with this kind of architecture?
*  So I think those are like new, at least new for neuroscientists coming in these tools and sort of thinking about how we can operationalize some of those stories.
*  So at least to my next question, actually, I mean, it sounds like, you know, so we have to think about, you know,
*  so we have this deep these deep nets, which is like a shiny new tool for neuroscientists, essentially.
*  So the next question is, respectfully, respectfully.
*  Yes, of course.
*  Yes, of course.
*  I don't know, though.
*  Well, I'll leave it for later.
*  Okay.
*  My disrespect.
*  No, we'll get into that.
*  I was just I was thinking about how neuroscience progresses versus how AI progresses.
*  And as a neuroscientist, I feel extremely jealous essentially of how AI progresses because they're fast because they don't need to know how it works.
*  Essentially.
*  Anyway, that's a they're coming around to it.
*  They're starting to know.
*  They're starting to realize they need the tools of cognitive science.
*  It's really exciting.
*  Well, that's true.
*  But but maybe to clarify what I and this really is a tangent.
*  So we won't go far.
*  But but you know, so in neuroscience, progress means understanding like how it works.
*  Right.
*  And in AI, understanding how it works is like nice secondary secondary, but getting it to work, just making some problem solving the problem that you're trying to solve.
*  That is the standard for progress.
*  And and in many cases, and I'm not integrating, you know, the difficulty of it at all.
*  But, you know, that's just a much clearer answer.
*  Yeah.
*  In that sense, it does.
*  You know, that's like, does it beat top performance?
*  Is it state of the art?
*  Check.
*  Moving on.
*  Yeah.
*  Yeah.
*  Yeah.
*  I mean, I've also even seen on Twitter some people in that community expressing remorse over that being the standard and wishing it was a little bit more.
*  Mechanistic.
*  I've heard that sentiment independently a few times.
*  So who knows?
*  There's room for maybe that could be something that we cognitive neuroscientists sort of help, you know, give back.
*  I hope so.
*  Yeah.
*  But so anyway, the question is, what do you think that we need more of to to address what you're seeking to address that the questions that drive you?
*  Do we need more data, better data, better theories, better models, you know, better experience?
*  I know we need all of it, but yeah, we need all of it.
*  But let's see.
*  I think among the top sets, one, I think the idea of doing experiments on models is is something that's maybe not quite made, you know, hit its heyday yet.
*  We do experiments on people or in brain and we get measurements and then.
*  But why not do the same thing with the model?
*  So treat the model as a model system and give it different visual diets and see what kinds of representations it learns or compare what's learned across different architectures.
*  That's just studying the models in and of themselves.
*  And that's like maybe a bit of a contrary thing for a cognitive neuroscientist to stay like that's interesting to me, though, independently of whether it's matches human brains or matches human minds.
*  Just understanding how the models themselves are working and whether they're similar or different and how I think is going to be really important in making the connections.
*  And those are experiments that you can do in a sort of less time and date time limited way, because you just have to run it on your GPU.
*  You don't have to stick someone in the scanner to get those measurements.
*  So I feel like there's more room to do experiments on models just for the sake of understanding the models that in a massive human fMRI datasets.
*  But I think those are underway. Yeah, those are people are working on that.
*  That's right. Yeah. Yeah.
*  Kendrick K does that sort of stuff ahead.
*  That's right. I just saw him give a talk on it.
*  Really, really cool stuff.
*  Yeah, for sure.
*  I'm glad they got him.
*  I'm glad he's doing it because he's doing it well.
*  Right.
*  It's going to be high quality, high reliability data.
*  Yeah, it's going to be really valuable to the community.
*  I mean, in some sense, the deep net approach to the doing experiments on the neural networks is sort of a neuroscientists dream, at least from my perspective, because you attack.
*  Let's say you're for me recording in some area of the brain.
*  But then you still don't know the brain seems like such an unconstrained thing that we don't know about, whereas a neural net, you at least like have it constrained and like you can you kind of have the whole thing there.
*  Yes, there's a lot to learn about it, but it's not a brain like you don't have to consider all the things that you really don't know about it.
*  So, yes, that's right.
*  Right.
*  Exactly.
*  And then I think that is the rub that I think is off putting for some cognitive neuroscientists, which is it's not a brain.
*  It doesn't have like a thalamus.
*  It doesn't have laminar structure in the ground.
*  I mean, there's like any number of architectural motifs that may or may not be super critical for function.
*  And so I think a lot of times the idea of like studying the network and of itself is can be sort of jarring because it clearly isn't like a brain.
*  And so what's the point?
*  But I actually think that reduced complexity is like critical.
*  And as long as you don't get confused, like what I'm studying is how the model does this.
*  And that's interesting for other reasons than direct inference about brains.
*  Then I think you're in the clear.
*  And so exactly those ideas like you can just understand you can probe it to death and figure out what's doing what and what are the information in the weights and how those represented.
*  And yeah, I think it's just you know, we haven't even begun to scratch the surface.
*  We're going to lose you to the A.I. side.
*  I can tell.
*  Well, the sneaky thing is really I still care about how lines and brains are, why they are the way they are.
*  The reason why I want to study machines is because I think they'll give us insights into the human mind and brain.
*  So I do think I keep my my strongest foot planted here.
*  I just think that there's quite a lot to learn from the other side.
*  Yeah, that's why we're here today.
*  So what's I mean, is there something that you want that you're looking to take home from a conference like CCN?
*  Yeah, I think in the same theme, because it's a new convergence.
*  No one even knows how we should or ought combine these like in every every week.
*  There's a new paper where someone's done an interesting thing in a different way.
*  And so and it's impossible to keep up with them all.
*  It's too fast.
*  And so I kind of use the conference as a curation for collecting insightful approaches for how I might start trying compare across, you know,
*  make minds, brains and models.
*  So it's sort of like a sneak, a shortcut to the literature.
*  I think that's great.
*  I mean, a lot of people say they use Twitter like that.
*  But I might push back to that.
*  And I think that's great.
*  But my pushback is that, you know, not everyone's on Twitter, obviously.
*  And then you really are like even siloing yourself even more for those five popular kids on Twitter who keep sharing their papers and generating all the discussion.
*  And I know that's not completely accurate, but I still I still see the danger of like the social media danger in general also applies to science, to Twitter, science Twitter.
*  Was it Twitter science?
*  Yes, science Twitter.
*  Yeah.
*  Yeah.
*  I have to say so about a year ago, we had a lab meeting like how important is science Twitter?
*  Like, do we need to get on this?
*  What's happening?
*  And so we like got accounts and we've been, you know, first you just watch and see what's happening and every time you're brave enough to put something in the stream and see how it's and I have to say, I think it's got more benefits than costs.
*  I think if everyone were on it, it would solve a lot of the problems you mentioned.
*  Like not everyone is on it.
*  I thought it could be a replacement for getting email tables of contents.
*  And it is a bit, but I still I keep abreast of the literature in other ways, not just through Twitter.
*  But, you know, amazing conversations happen like, you know, paper came out in science on dimensionality of object representations and mouse cortex and then the conversation amongst the people who are trying to understand what was going on.
*  I mean, I have access to that in a way that like I would never have had before.
*  So I generally think that the benefits outweigh it.
*  And one other plug, this is for young researchers who might be listening.
*  So also on Twitter, there's this new new, I don't know, trend to when you publish your paper to not just tweet the link, but to do a thread that walks through it.
*  And, you know, I was looking at one and I follow a bunch of CS people because I don't go to those conferences as much as I was watching one.
*  It was on like what compute computer science is the yeah, I follow a bunch of yeah, sorry.
*  Yeah, computer science people, machine learning people.
*  And, you know, I saw one paper and a really, really clear tweet thread on it.
*  Like I was like, not only is the work cool, but the way they talked about it was super clear.
*  And I looked at the guy who was a postdoc over at Stanford, invited him out for a lab.
*  He gave a great talk, gave him a job offer on the spot.
*  So young people, I think it's really important to get out on science Twitter just because the visibility is important and can lead directly to jobs.
*  And outsource your tweets so that someone writes them quite well and clear.
*  Well, no, the idea is to hone the craft.
*  You know, try try and we do this legit, you know, authentic science Twitter.
*  We'll go for that.
*  Yeah. I mean, while we're on Twitter, though, so whenever I get on there, because I use it to promote the show and I don't do a lot of back and forth because mostly I don't care what people are saying on Twitter.
*  But that's probably my fault for not having the right curation.
*  You know, it is a curation.
*  It is, but I don't want to spend months curating the thing and then constantly wonder what I'm missing and what I'm doing right.
*  Because I still feel like no matter what I am giving up, I have a lot to do during the day.
*  I'm sure you do, too.
*  And I am completely giving up my attention to someone else's whim when I go on Twitter.
*  And that really bothers me.
*  So interesting.
*  There is a balance.
*  There is.
*  I mean, I think so.
*  Sorry.
*  Like I said, we had a whole discussion.
*  We have a lot of people on Twitter and how to use it effectively and if it's worthwhile.
*  So I thought a fair amount about this.
*  And I think that like effective curation.
*  So your science Twitter, I like don't follow anyone who's talking about politics.
*  You know, I make sure it's about science and it's a group of people that I like to see what they're posting.
*  And then the other thing is I don't like you have like fear of missing out on opportunity costs.
*  And I understand that.
*  So I just don't use it during those times.
*  I use it when I'm standing in line or when you know, so I've just gotten and I don't expect it to be a complete survey.
*  So when I change my expectations of what it gives me and I use it in times when I wouldn't do anything else.
*  In fact, I'm like, sweet, look, I'm following the literature.
*  Like I'm getting more work done.
*  So I've used it as like a productivity boost.
*  Like when I when I use science Twitter, I'm like, oh, look at look at how how broad a literature I'm able to view while I'm standing in line and waiting for my coffee.
*  I can like learn about science at the same time.
*  So I think that that's a like you have to find your mode and it can definitely be an effective.
*  And so I think that but you know, for where I've landed, I you know, I'm very specific when I use it and when I don't use it like never during the workday.
*  And like usually I just don't really go on it during the work.
*  Yeah. Well, that's smart.
*  I probably should stop trying to keep up with the literature in between paragraphs from reading to my children before bed.
*  Yeah. And then Benny the Bear.
*  What about this causality?
*  Yeah, no, I definitely know exactly what you're talking about.
*  Well, I've read, you know, I've heard Cat in the Hat how many times?
*  Yeah, sure.
*  You can your mouth moves and the sounds come out and you can do other things.
*  I'll delete all this.
*  I'll delete all of this from the show.
*  Yeah, that's right.
*  All right. Well, good luck at your conference talk and it should be a good time.
*  So thank you.
*  Mitchell, Seth, Kyle, Slava, Claudio, guys, guys, thank you for your support on Patreon.
*  I was going to record a little song for you on the guitar and sing to you.
*  But my wife said that that wouldn't exactly be a gift.
*  I could just divorce her.
*  I do like that song.
*  Anyway, thanks, guys.
*  You can support the show by going to braininspired.co and clicking on the red Patreon button there.
*  All right. So let's talk about how you're turning the world of visual neuroscience orthogonal, let's say.
*  Great.
*  So you kind of mentioned this a little bit earlier.
*  People used to think, and I can't remember who, and I don't have the source for this,
*  that our visual perception could be due to us shooting things out of our eyeballs onto the world, onto objects in the world.
*  Yeah, and early view, I actually don't know either. I shouldn't have.
*  I used to know. There's a really good book anyway.
*  But apparently that's also a normal part of development that, you know, when you're younger,
*  you don't know whether light's coming in or whether you're shooting out.
*  I actually asked my daughter this. She's six.
*  And I got actually her answer was not I could not understand what she meant, you know,
*  her perception of what is happening if light is coming in or if she's shooting it out.
*  But so anyway, I'll try on that a little bit more.
*  And it's kind of actually hard and a fun experiment to sort of put your Cartesian hat on it and try to get rid of all your assumptions and think,
*  what would that be like to think, get rid of all your prior knowledge, to think that I'm shooting things out?
*  How would that work? You know, even.
*  I know. It's true. Actually, there's an interesting I saw a paper by Michael Graziano on this where he actually showed evidence
*  that people really do have this internal model that like they are sensing the world like in the same way that you reach out and touch things
*  like your eyes reach out, you know, that that's the, you know, the percept that our internal models of our vision is one of much more of an active reaching force than a than a sensation.
*  Nicholas Humphries talks about this, too, with his like reading.
*  And I've been reading Michael Graziano's like attention schema theory stuff. Yeah. And Nicholas Humphries sold us anyway.
*  So anyway, that's not how it works. But maybe that's our conscious experience.
*  That's how we think it works, which is interesting.
*  We know better. So I'm looking at you, which means that your image is, you know, going hitting the back of my eyeballs, hitting my retina.
*  It gets transformed down nerve signals that shoots down the optic nerve.
*  It makes a pit stop in the part of the thalamus, the lateral geniculate nucleus.
*  And then it gets relayed to our cortex in the backs of our brains and the earliest visual cortex called V1.
*  That's the classic story. Well, that's how light essentially mostly comes in through the eyeballs and gets to our cortex.
*  So maybe I'm going to let you take it now and say, what is the classic story of ventral and dorsal visual streams?
*  Just where are they in the brain and what's their function?
*  Right. OK. So once the visual information hits the cortex, the sort of classic story is that it gets relayed down two pathways, the ventral stream and the dorsal stream.
*  And those have classically been ascribed the functions of recognizing what something is in the ventral stream and where something is in space in the dorsal stream.
*  And along the ventral stream, the classic framework involves a series of hierarchical processing stages.
*  So we think of V1, which transfers information to V2 and V3 and V4 and then into inferior temporal cortex or occipital temporal cortex, depending on if you're in the monkey or the human.
*  And and that it's across those sort of hierarchical information transformations that you go from patterns of light into meaningful representations of objects in the world.
*  That's a classic view. And so in my experience, like the what pathway has really dominated neuroscience.
*  And I guess I my own research had more to do with the where.
*  And so I always wondered why that was the case. Why does what get all of the attention?
*  I mean, I obviously we need to recognize objects, but we also need to know where they are.
*  And I'm not complaining. I'm genuinely curious, like why that was that is the case.
*  And even in deep learning as well. Yeah.
*  You know, I don't have a good answer, but I can just make something up on the spot.
*  Sure. It might be an easier problem to get off the ground because you can get pretty far just looking at like pixel correlations and image statistics.
*  And the question of where and immediately gets into body coordinate frames, hand centered, eye centered, far from the spacer top.
*  Like, it's actually a really complicated problem.
*  And I also think that now that we've gained a lot more information about what measurements from dorsal stream,
*  I think that we might have been off a little bit more in understanding what the dorsal stream does.
*  It does way more than just where is something.
*  In fact, it's got all kinds of object information about what something is.
*  You can decode object category from the dorsal stream almost as well as the ventral stream, not as well, but almost as well.
*  And in some cases, like high abstract things, people have found that you can decode like face identity in the dorsal stream.
*  These are radical things. If you're if you're in a classic view of it's all about spatial information.
*  So I think we made progress on the mental strings are a little closer to like in approximating what its function is.
*  And that problem might be a little easier on a first pass.
*  So that's my guess. They are distinct anatomical pathways.
*  I mean, there is crosstalk, of course. But but, you know, even when you hear someone just say, I study visual processing and it's assumed that there's a ventral stream.
*  Yeah, that's right. Yeah, it's true.
*  I think if you if you think about it, we're like tracing the signal in and understanding the retina and then going to be one.
*  And then we're making our way and we're just sort of like the front edge of sort of tracing the sensory signal and trying to get as far into the brain as we can.
*  And you get a little farther.
*  Visually, like dorsal stream ends up taking less obvious visual characteristics pretty early, whereas ventral stream you get pretty far.
*  Damn it. Everything I did, slowed my career down.
*  Yeah, that turns out it's a trickier beast. But we are making progress on it.
*  I think that we're not too far off from a revised view where I think people are realizing that dorsal stream representations are so much more interesting and multifaceted and multiplexed and abstract.
*  And I think that that, you know, those frameworks are coming forward and the classic view is going to be updated.
*  Well, you're helping that happen, essentially.
*  So yeah, so this classic view, right? You already said it, you know, the ventral stream in the ventral stream and these really early visual areas, you start with these really low level features like little edges and, you know, lines and orientations.
*  And then as you process up among the visual hierarchy, they become mid-level features like smaller shapes and things like that, or not necessarily smaller, but shapes and things like that.
*  Until you get to the peak of the mountain and there you have grandma or there you have the object that you're, my grandma is at the peak.
*  So there you have the object that finally gets encoded and the visual cortex has done its job.
*  And that is one way to look at the map, right? That hierarchy. And you have turned it on its side, which is why I said orthogonal.
*  And I don't know how you want to do. You want to just start talking about how like topography in the brain or you I'm going to let you just take it and talk about the difference.
*  Okay, yeah. So that's right. So if you think of like, we'll just simplify the visual cortex as a two dimensional sheet and what you just described is one axis going from the posterior to the anterior bit of the underside of the brain, where we think that sort of lower level features and then mid-level features and then higher level features.
*  Higher level features are sort of extracted on route to recognition. And that's sort of a one dimensional story, low, middle, high.
*  But what I've been trying to understand is like within the level, what are the major divisions there?
*  Like, so not just sort of what's the level of abstraction, but what's the nature of the tuning? And is there any systematic structure in that?
*  And one thing that we found, I mean, sort of back, back ended into this result, really, but like that story about the hierarchy just doesn't make any predictions about whether some kinds of object information would be represented here in the cortex and other kinds of object information would represent here like animate shapes or inanimate shapes.
*  It just doesn't, it just doesn't have anything to say about that. But we know from brain imaging that the spatial structure of those response preferences is highly consistent.
*  It's consistent across individuals. It's even consistent across species. So, so we, so, and we sort of have, haven't had the, the theories have been sort of absent on that.
*  Why, you know, why is the topography the way it is? And so just in trying to just so the first step was just let's make a map. Like we know object information drives this whole cortex, but like, are there any divisions of objects that drive different parts more than others?
*  And yeah, one of the sort of major findings we have in terms of trying to understand this large scale structure is that the distinction between animals, between big objects that, you know, are useful for supporting your body or navigating around, and then the distinction with small objects and manipulable small things, that that three way division is mapped out across the cortex.
*  So you can see just like a zone of cortex that cares more, responds more to big objects than the other categories, and it runs all the way along the hierarchy. And right next to it is a zone of cortex that responds more to pictures of animals than the other categories, and it runs all the way along the hierarchy.
*  And same with small objects. So there's the systematic structure that's that's orthogonal to the hierarchy. And that's just the data. And I go that's so there's like clear structure in it. And then the interesting thing is trying to understand why. Why? Yeah. What does that tell us about the nature of the tuning?
*  Well, so so you call this the tripartite organization, which is a good name. And and it what you just described makes sense. It's not what you guys expected to find. And it's interesting, because the order of it kind of from, I guess, dorsal to ventral or medial goes anyway, the order of it goes.
*  It's weird. It's a weird order. Yeah, big, big, and then animals in the middle, animals in the middle, and then small things. Yeah, and then animals and then big objects. It's this mirrored tripartite organization. It's super systematic and not at all what we expected. So yeah, so you've done Yeah, so that was like the sort of the major finding that then then you've taken that and run with it. And then a bunch of experiments to see what's going on here.
*  Yeah, weird. I know it turns out that, like, just that that initial finding had a lot of questions like that's a lot of cortex for animals. It's all well doing animals and big objects. No, probably there's different features underneath. And so one of the findings we had was that, well, so this is this idea, we call it content channeling, which is, it's a different way of thinking about how you need to get information from the input to the input.
*  And so you're trying to do meaningful representations of the world. And rather than thinking of trying to extract low and then middle and then high level features, you try and go, well, given these high level distinctions like between animate and big and small objects, what are the what's the systematic structure in the input? What are the covariances that let you get from patterned light up to those? And so the idea is, it's not, you know, big objects tend to be more in your periphery.
*  And recognize more in your peripheral and small objects, you tend to hold them in your hand and they're at the center of gaze. And, you know, if they're out in the periphery, you don't even recognize them anymore because of acuity limits. So there's like already, there's a really early joint between just the the angle that it subtends in your visual field and the size of the object. And that's, that's just a natural covariance that small things tend to have smaller visual angles and big things tend to subtend bigger visual angles.
*  And visual, the visual size of things is something that's mapped in early visual cortex. So there's like the beginnings of a natural way to start to separate small objects and big objects just from a very early signal.
*  So that's an example of a covariance between like a high level property and then a low level input. And so our idea is that what the visual system is trying to do is figure out what covariances there are between the input statistics and the high level statistics and make these channels that run through them and sort of channel information from patterned light into, you know, the useful contentful representations of the world. And so that's what we think is going on, you know, across the world.
*  So that's the hierarchy in this orthogonal way.
*  And it's interesting, you know, the way I described it earlier, you get to the pinnacle, right, of your visual processing and then there you have the object. But of course, it doesn't stop there because we have all of these behaviors that we use objects, our representations of objects for.
*  And part of your story, and I know I'm jumping the gun a little bit here because there's a lot of other stuff to get to, but part of your story is that this content channeling essentially could be used to communicate with broader regions in the cortex that are doing evolutionarily beneficial things essentially or ethologically beneficial things.
*  And that it makes sense along this this channel, let's say for big inanimate objects that it might be.
*  And this is just one example connected more broadly to navigational systems.
*  And this is why these covariant properties along the stream would be useful in this region when they're connected to navigational.
*  So you nailed it entirely. Basically, these divisions, I think, interface with sort of major joints in our behavioral repertoire, manipulating tools, navigating around the world and interacting with other agents.
*  And the idea is by separating those out spatially on the cortex, it makes the wiring problem easier.
*  So other, if you want to get this visual information into other systems, you know, long range networks only have to come in and they can synapse on this part of the object responsive cortex to get to navigation and this other part to get up to sort of reaching regions.
*  And so we're kind of by sort of spatially elaborating these distinctions, it makes the topography or the network wiring much easier to get information out of the visual system into these more a modal or behaviorally relevant networks.
*  I mean, I have so many questions about this.
*  One of the things that you use to do tests to experiment to get at these questions is you use what are called text forms.
*  And this is sort of the study. What's so funny about that?
*  It's funny because we made that word up.
*  And we spent years trying to figure out what to call them. And then we finally landed on text forms.
*  And so when I hear people use the word, it just brings back all the years of pain trying to figure out a snappy name for them.
*  And like, look, there you are saying the word text form, something we made up. So that's good.
*  There you go. Well, so text forms is short for something. So you can tell us that. Or it's a conjunction, essentially.
*  Yeah.
*  So what are they and how do you use them? And what do they fit in the story?
*  Yeah, that's right. So text forms are these stimuli we made by using a smile.
*  She can't help but smile when she says text form.
*  No, it's just a made up word, but I love it.
*  That preserve the texture and course form of the original image.
*  But so hence the word text form.
*  But the critical thing about these stimuli is they're not recognizable.
*  They look like textury blobs. They're interesting, but you don't know what they are.
*  And that makes them a really interesting stimulus to use because they clearly have some of the structure of the visual object that it was generated from.
*  But they're clearly missing features that, for instance, let you recognize it or give you a sense of its 3D form.
*  Like they don't have clear contours.
*  So it's like you can't tell what it is. You don't know what they are.
*  After you show someone what it actually is, can they tell then? I can't.
*  Not very well.
*  We're working on training people so that we can see what happens when you can associate.
*  But anyway, I digress.
*  OK, so these these texture text forms are interesting because they let you see what happens in the visual system, like what regions are even driven by these texture and course form features.
*  And the classic hierarchy theory and certainly what we expected going into this is that maybe we'll drive some of the posterior bits of visual system, but we won't make it all the way up to the anterior bits where high level representations are because these aren't recognizable stimuli.
*  And so how could they possibly drive those high level regions?
*  And then what we found is that they drove the entire visual cortex the same way.
*  So even though you're looking at texturing blobs of things, the texturing blobs that were generated from animals still drive the cortex that represents animate information more than the other ones.
*  These are not the neural correlates of consciousness, for example.
*  Right. Well, there are differences between them.
*  Yeah, like they're a little bit weaker throughout.
*  But the so it's interesting.
*  So there are differences, but it's not like they stop and they don't make it to the anterior bits.
*  So exactly what you make of this, people are debating that where where we've told the story is that I actually think that those anterior bits that we call high level are actually a little bit more mid level and primitive than you might think.
*  And and one of the reasons why this I think this is true is, you know, I think a little bit obvious, which is we can't have a new neuron for every new category.
*  At some point, that's just not a viable coding solution.
*  Like, oh, I learned a new category.
*  I need to grow a new neuron that connects in certain way.
*  Like we need a so usually and I think this is kind of a general rule of organization.
*  I'm going to slight digression here.
*  Like if you go to the grocery store, you know, things we need, we're buying food to make meals, but they're not organized by meals.
*  They're organized by ingredient one level down because to make a meal, you need different ingredients.
*  And sometimes I wish restaurants are organized by meal.
*  But then, you know, you can see the problem is how do you find which meal you want?
*  There's a gazillion meals.
*  So this is like a generally the level you want is not the thing you code for you code one level down.
*  And so what I actually think may be going on in the ventral visual stream, especially in those anterior bits, is there are these little bit more primitive building block features.
*  And then they can be used to make any object but are specifically useful to make the, you know, sets of objects we see in the world most of the time and particularly to emphasize the distinction between animals and big objects and small objects.
*  So their tuning is primitive, but they're organized spatially by these high level distinctions.
*  And so that's kind of a nice property.
*  It means the features themselves are mid level.
*  But, you know, long range regions can go in and listen to part of this cortex and effectively be pretty sure that, you know, there's probably an animal there because those animal like neurons are the ones that are firing.
*  So I think there's a nice way to go from like mid level features to high level content all in one go.
*  It's like the lube of the channel or something.
*  The, you know, allow the early processing to to seep into it and allow the higher level processing to go and grab it.
*  Exactly. So you have like a mid level buffet and high level readout.
*  Yeah.
*  Yeah. So I mean, so you use these text work.
*  I mean, the interesting about one of the interesting things about the way that you use them is you have people sitting in front of a screen and you're showing them these text forms.
*  But of course, on the screen, the text forms are all the same size.
*  But in in real life, you're looking so but you're looking at an object of, say, a blue whale or something, which is well, no, let's not use blue whale because I want to ask you about that later.
*  A barn, a piano, a barn. Yeah, a piano.
*  But, you know, and it's sub 10s, five degrees or something, you know, 10 degrees visual angle.
*  And then you look at, let's say, I don't know, a mouse or something like that.
*  And it's sub 10s, you know, the same amount.
*  So so you're controlling for the actual size.
*  But the processing is still within these channels in the brain.
*  That's right. That's right.
*  There's like this beautiful exchange that happens between early visual cortex and occipital temporal cortex.
*  So in early visual cortex, the dominant spatial organization is by retina toppy.
*  That is visual field maps.
*  So these are even used to define the hierarchy in the first place.
*  V1, V2, V3 are defined because they have separate maps of the world at a large or the visual field at a large scale.
*  And then right past that, things start to change and the responses seem to be organized more by what things look like rather than where they are in the world.
*  Like, so you start to see object centered responses that care more about like curvy things versus boxy things, no matter where it's positioned in the visual field or how big it is in the visual field.
*  So there's this like beautiful transition between cortex organized by space and then cortex organized by shape and and how that magic happens.
*  We don't know yet, but that's that's just in the empirical data.
*  You can just see that that's that there's a switch that happens there.
*  And so we happen to be in the cortex that sort of abstracted away from the retina toppy as the dominant organizing factor.
*  And we start to see responses that are more object centered.
*  So they care about like big objects, systematically different shape structure than small objects.
*  They're boxier. They have larger surfaces. They have more high spatial frequency.
*  There's all this structure that's related to the fact that to be big in the world, you have to have certain shapes withstand gravity.
*  And so I think that's what that's the kind of features that these neurons are and brain regions are picking up on in a way that's abstracted over the sort of initial retinotopic stages.
*  There's so much to do. So cool. Right. So cool.
*  And it opens like so many different, you know, like all good science.
*  You answer one question and it asks multiple more essentially.
*  Yeah.
*  Let's take a little break with a quote of the show.
*  When you see something that is technically sweet, you go ahead and do it and you argue about what to do about it only after you've had your technical success.
*  That is the way it was with the atomic bomb.
*  That would be J. Robert Oppenheimer.
*  So you have shiny new toys and deep learning.
*  And one of the things that you do is test. So let me back up.
*  So I've had Dan Yamans on the show.
*  Cool.
*  I don't think it's Yamans and he with Jim DiCarlo, you know, were responsible for making some of the early deep nets that sort of mimicked the hierarchy of the classical hierarchy of ventral processing where these early layers.
*  So when you teach a one of these deep convolutional neural networks with, you know, various different layers, if you teach it to classify images, when you look at the units and the different layers, they map on pretty well to the ventral visual stream.
*  As far as low level, you know, edges and things and then mid level shapes. I don't know if text forms are in there, you know, and then we've done it.
*  Well, I know. Well, that's that's what so.
*  But so that that classic hierarchical story has been recapitulated in neural networks.
*  And part of what you've done is you've tested your story and tell us what you found.
*  Yeah, I think when we did a couple of things, so we sort of replicate what people find that like deep neural networks do a pretty good job of predicting responses and human ventral visual stream with our stimuli.
*  But then we also could do something fun, which is show the text forms to deep nets and see, you know, what happens.
*  And I actually remember when my postdoc and I were thinking about this, he was like, we I don't even think the text forms are even going to drive.
*  Yeah, well, like, shouldn't we fine tune first?
*  I'm like, no, no, no, no, just show them the deep nets and see what happens.
*  Show them the text forms and see what happens.
*  I don't know. I just knew that the right thing to start with was to see what happens.
*  And and what happens is, you know, well, the deep net thought they were all plastic bags.
*  But the responses at the different layers also did a reasonably good job of matching the responses to text forms.
*  And what's cool is those same responses did a good job matching original recognizable image responses as well.
*  Not as good, but like 80 percent of the way there.
*  And these are these are sort of the mid layers of the convolutional neural network.
*  Yeah. And but that was stretched over a broad region showing that a lot of these different layers actually represented well this mid level sort of form.
*  That's right. So we've been unpacking that.
*  So people have spent a lot of time, again, focusing on the hierarchy.
*  Different layers of a deep net correspond to different layers or sort of regions along the hierarchy in the brain.
*  And that result is real. But it's a way blurrier hierarchy than I think people think.
*  So when you've done it yourself, you see that, well, like, well, layers four, five and six of Alex Net, like they all they all do pretty good across much of this cortex.
*  So it suggests that this idea that each region of the brain and each layer of a deep net is representing information in a completely different way.
*  Now, that just doesn't turn out to be true.
*  And even direct measures on a deep net to understand how similar are the layers to each other also bear this out.
*  Like those mid levels in a deep net are also pretty similar to each other.
*  There are slight changes because it's getting better and better.
*  But, you know, there's a bulk of those layers that have pretty similar kind of responses.
*  So I think I think this also sort of is compatible with the content channeling idea.
*  Like, instead of it really being about isolating separate levels of representation as you go along the hierarchy, it's more about like twiddling and trying to match the covariances to untangle the retinal input and that and align it up with the content divisions at the top.
*  And and sometimes those representations are going to be kind of similar to each other, slightly different, but pretty similar, which means it's going to be more of a blurry gradient, blurry hierarchy.
*  I don't know if that makes sense. But there you go.
*  Yeah. You know, that touches on the topography of that, you know, exists in the brain just because of wiring constraints that things near each other tend to code for the same things.
*  And is it is it the case that deep networks don't have that topography because there's just not a limitation on their wiring?
*  Yeah, this is like one of my current favorite topics, which is what how do we bring?
*  How should we bring topography constraints into deep nets in a way they have some of it?
*  The convolutional part of the deep net is got is has an implicit topography in it.
*  But for instance, you know, the fully connected layers like that's a lot of wires from one neuron to all the other neurons.
*  And, you know, maybe that we should have some constraints on the number of wires or how sparse the connection should be.
*  And so there's a lot of different ways of bringing topography into deep nets.
*  Another one is maybe we should unpack the convolutional assumption a little.
*  That assumes that the features that are learned apply equally everywhere in the visual field.
*  But a lot of the theories about why the cortex comes to have this organization depend on, say, different features in the fovea compared to those in the periphery.
*  And a deep net can't learn those. We might be missing some structure there.
*  So, yeah, exactly how to build topography into deep nets.
*  There's a lot of interesting ways interest if you're interested in a postdoc and doing these things to anyone who's listening.
*  Always, always hiring. Yes.
*  Should I apply? No, that's great.
*  So there are some in the interest of time, I kind of want to wrap up soon about with this push here.
*  But so there's there's the evolutionary question. Right.
*  And I don't maybe maybe you can just tell us what you think it all means, you know, and speculate like what what and why?
*  Yeah, I mean, I think that right now in visual neuroscience,
*  there's like a lot of interest and excitement in trying to figure out why the organization is the way it is.
*  Why does it take these forms? Why do some regions end up where they do systematically and what tuning do they have?
*  And there's sort of two camps, maybe three.
*  The main camps are the people who are on the empiricist side,
*  who think that it's all the structure of the input and a sort of generic architecture
*  and all of this beautiful structure and the separation of different object categories can emerge just from the statistics of natural input.
*  And they are doing things with, you know, there's modeling that can test that.
*  And they're also sort of, you know, raising baby monkeys to see and show that like early experience with new categories can lead to like new regions that are formed,
*  like clearly showing the role of early intensive visual experience in the large scale structure of the cortex.
*  So that's one side. And the other side are the people who think more of that structure is built in.
*  Why is it, you know, tripartite? Well, these are not arbitrary distinctions and navigation, manipulation.
*  So these are critical joints in our behavioral repertoire and network architecture like long range network connections.
*  Yeah, those don't just grow when you're a baby. Those are built in. Those are patterned.
*  So on that side, like the structure of the network might be set up to enforce particular kinds of content divisions that are useful.
*  And so that's the idea of like, are these with these divisions just be learned naturally or are they enforced by particular readout structure?
*  Then now that's a sort of attractable empirical question. And the third camp, this is one that sort of I'm in.
*  And it's I think it's received a little bit less tension. And that's just that maybe the structure of this object selective cortex is emergent itself.
*  It's it's maybe loosely constrained by the input and loosely constrained by the readout,
*  but largely is related to just the similarity structure of things in the world trying to be mapped smoothly on the brain.
*  And so that, again, also leads to testable predictions.
*  Maybe you don't need either of those constraints to kind of see the organization that we're seeing.
*  So I think that, yeah, there's there's pretty exciting computational approaches to sort of getting at, well, how much can you learn from the input?
*  How much do you need to build in and how much can be reflected from sort of a smooth mapping of the shape structure itself?
*  And that's sort of where we're going next.
*  This is also just a broader question of cortex. And, you know, is all cortex the same?
*  You know, obviously, it's not completely structural, structurally the same, but essentially it's the same.
*  A lot of people argue. So it all must be doing the same thing.
*  So that would be, I guess, the empiricist side.
*  Yeah. So, yeah, I kind of think that there's two kinds of cortex.
*  There's the kind that's a little bit more sensory and there's the kind that's a little bit more I want to abstract or a better word like.
*  And you can kind of see this in in the nature of lesions.
*  So if you you get a lesion in the back of the brain, you can't see this part of the visual field or you can't recognize that category of objects.
*  You get a lesion in the anterior temporal lobe or the prefrontal lobe or some of the parietal bits.
*  And it's hard to map what happens like the they don't signal information the same way they participate in a more associative and sort of dynamic representational scheme.
*  Whereas I think the sensory areas are a little bit more fixed and labeled like this neuron once it comes to code for faces like that's what it does.
*  It doesn't code for anything else after that.
*  And so I actually think visual system along the ventral stream, we have this sort of labeled line like what it fires, how it moves, how it moves.
*  It fires highly to it's actually signaling that content is present.
*  And then it just interfaces with the cortex that's now going to make more interesting combinations of those.
*  And that's it. I think that's a different kind of cortex.
*  And, you know, maybe it has different kinds of connectivity motifs.
*  But I don't know the answer to that.
*  But anyway, from from seeing the data and different lesions and the consequences they have, it seems like there's there is a sort of maybe evidence for at least two really different kinds of coding schemes.
*  And how cortex represents information.
*  You just opened a huge box that I want to jump into.
*  But, you know, all I'll say is someone like you, you might I might have thought that you had divided into three.
*  That's all I'm saying instead of two types of coding.
*  Interesting. What's the third?
*  Well, I don't know. That's for you. You have to, you know, maybe.
*  Oh, you mean because of my tripartite?
*  Yeah, you're the you're the.
*  I have to think more about that now.
*  There you go.
*  Good point.
*  Just don't limit yourself to two.
*  That's all right.
*  We do tend to do that.
*  OK, so quickly before we move on, because I want to ask you some broader general kind of questions here.
*  But but back to my beloved dorsal stream.
*  Yes.
*  So, you know, you you took this longitude and added latitude.
*  Let's just for, you know, to be quick, we can say to put the new new scaling in for to complete the map, essentially in the ventral.
*  Yeah, it's the other side of the map.
*  Is there something to be learned in the dorsal stream from this type of approach?
*  Or do you not want to touch that?
*  Oh, it's it's good. I mean, one of the reasons why.
*  So, yes, the short answer is I definitely think there's something to be learned by mapping the cortex.
*  As long as you're in cortex for the maps are stable.
*  Like I'm saying, there seems to be cortex for that's not true.
*  I don't think they may not be as helpful there.
*  But in certain systems like motor cortex and, you know, ventral visual stream, like the maps are stable and so studying them seems useful.
*  I think that one of the reasons why we haven't looked in the dorsal stream too much is because, you know, mostly when you show people pictures of objects and have them do boring tasks like, you know, detect a repeat or a red frame or the fixation change in color, you just don't drive the dorsal stream that much.
*  But then I just recently did some new new work with my student who got a bunch of videos of people performing everyday actions, little short videos.
*  And we tried to span the set of things people do.
*  And we showed Andy Warhol archive or something.
*  How we collected it is another story.
*  We started with verbs, but verbs wasn't ended up not being useful.
*  So then we went to the American Time Use Survey, which was like literally a survey where they called people and asked them what they spend their time on.
*  And anyway, from that, we picked out like common everyday actions.
*  Heaps of work.
*  My graduate student has made a heroic effort.
*  Anyways, we collected all these videos and we scanned people while they're viewing them.
*  And not only do you see like beautiful activations all along the ventral stream, but the dorsal stream, just the whole thing all the way along that intraparietal slant.
*  The focus all the way wrapped around.
*  It's just beautiful activations.
*  And I just had never seen that before.
*  And it made me realize that, you know, to study the dorsal stream, it's going to be, you know, you really have to pay attention to action and people performing actions.
*  And that's a different world than like curvature and, you know, texture and form information.
*  Yeah. And so I think I haven't tried to take on that feature space yet, but I've started to see what makes it go.
*  And it's people doing things in everyday settings and makes it go crazy.
*  And so something there. But then again, so many things drive it that maybe we need completely different theories, you know, that maybe the theories of the ventral stream really don't apply to the dorsal stream in the same way.
*  So, so yeah, so I'm going to say I'm going to just I'm going to keep focusing on the ventral stream for now and we'll we'll get to the dorsal stream next.
*  All right. Well, so you have time for a few big, bigger general questions.
*  Yeah. Yeah. Okay.
*  One just related to what you're just talking about.
*  What is what is something that you see that is just wide open right now for someone, you know, to who wanted to sort of get into this and doesn't want to compete with you, you know, like what in neuroscience and or A.I.
*  Do you feel is just wide open and right for ready for the taking?
*  That's a good I mean, I think there are a treasure trove of insights in neuroscience and cognitive science that can be assessed with a new lens by being a little bit creative on how you use deep nets, comparing deep nets with and without this architectural motif or, you know, like there's insights in mid level vision about what's going on.
*  I think there's a lot of people who have a lot of mid level vision about border ownership selves and some beautiful, beautiful neurophysiology and like, I don't know, there's just like a whole area like can we, you know, they have thoughts about the models.
*  I think like just just treasure trove of neuroscience insights and thinking about clever ways to probe how those work with both human behavior and human neural responses and deep nets.
*  I think there's so many. So I think finding the question or the facet of, you know, visual cognition that you're most interested in and that and sort of exploring how to implement that smartly and how to gain insights using these new modeling tools is a easy one.
*  Yeah, no, that's good.
*  So that is sort of like using the AI almost as a tool then to answer questions about neuroscience.
*  True.
*  No, I'm not knocking it. But my question is, what aspect of neuroscience do you think will have the biggest impact on AI moving forward?
*  Yeah, I don't know if I have a great answer to that.
*  All right.
*  I think AI has so like the advances in artificial intelligence impact so many fields, they make contact with so many fields that like neuroscience can influence a facet of AI, but you know, it's going, it's going to many fields.
*  So yeah, I don't know. Yeah.
*  You can skip that one.
*  No, no, I think I'll leave it in. What is that? What's something you used to believe that you now think is naive?
*  Yeah, I remember. Okay.
*  I remember thinking about how visual experience shapes the cortex and
*  sort of thinking that it was sort of plastic and related to experience.
*  Stop. But what I now realize that that was naive because I didn't appreciate the role of intensive early experience in shaping the large scale topography.
*  And it's really only intensive early experience that's involved in shaping these maps.
*  Late, you can learn new objects just fine as an adult, but they don't give rise to large scale map like changes.
*  You know, they lead to little tweaks in the weights that are you can measure, but they're very subtle.
*  But if you train, you know, you know, kids or baby monkeys to learn new things, you see these huge changes.
*  And so I think it was naive to think that visual experience has an equal impact at any point.
*  And now I appreciate just the how intensive early experience is going to be where the answers lie for why the large scale topography is the way it is.
*  How would you proceed if you had to start over?
*  Interesting. I mean, I'm going to reinterpret that question a little bit to be like, if I were starting now, what would I do?
*  Sure. Well, sure.
*  Which is, I think a lot. And the reason why reinterpreting that is I think I got pretty lucky that in my undergraduate, I took a lot of math and computer science in addition to cognitive science and neuroscience.
*  And like, that paid off.
*  That skill. That's not luck.
*  Well, I mean, they were my interests and I followed them. But now, you know, that that had other interests, too.
*  And, you know, you only can follow some of them.
*  If you have a tendency towards the computational side, I would say start early and and dig deep.
*  And, you know, to the extent that I wish I had done that more, that's mostly where I have regrets.
*  Like, I wish I knew even more. I wish I knew even more of that because being a because it's like the CS computer science fields and neuroscience fields and cognitive science fields have have towers of knowledge.
*  And there's just so much room to string bridges across if you speak their language.
*  And it's a translation problem, if anything else. And the only way it kind of ties back, the only way to be fluent is to get it early so that you speak all the languages.
*  And it's harder to get that later.
*  And if you can immerse yourself now in all of the disciplines, the I think the potential upside is very high.
*  That's basically what Martin Blinjel said as well. So that's good. That's that's that's good.
*  No, yeah, he didn't say it as eloquently. I have to say.
*  Okay, last one. What? No, not against him. He's a very eloquent person.
*  When when we look back at the mystery of consciousness and wonder why we took so long to get it.
*  Ah, I mean, I feel like we have a microcosm of the answer to that right now, because it wasn't I think it's like two days ago or something.
*  We could go there was that problem in computer science about specificity of and and or gates.
*  And it had been like a problem that the who's who of math theoreticians and computer scientists had tried to solve an outstanding problem for 30 years.
*  And then, you know, as of two days ago, it got solved in a two page paper that's so easy and elegant, everyone can understand it.
*  And, you know, the news article I read on it said like, this is going to be taught in every intro introductory class now, because that's how easy it is.
*  It's a paradigm. Yeah. And and so I think that when we finally understand consciousness, I hope it's a little like that, which is it seems like such a hard problem.
*  And people have worked on it for so long. And then when we finally get the answer, it's two pages and we'll not understand why we didn't see it before that.
*  Well, Talia, this has been really fun. I know we are out of time and I can't ask you about using Blue Whales as navigational tools.
*  So that will have to wait until. Yeah. I have to wait until I buy you a beer next time when we actually meet in person or something.
*  Yeah, hopefully it's easy and we'll see. So so I appreciate your time. Have a great conference and and thanks again.
*  Thank you very much for having me.
*  Go to BrainInspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements like you hear on other shows.
*  To get in touch with me, email Paul at BrainInspired.co.
*  The music you hear is by The New Year. Find them at TheNewYear.net.
*  Thanks for your support. See you next time.
*  I don't know why
*  Searching the coffers
*  For empty offers
*  I don't know why
*  You trust the sky
*  You must like your lies from blue eyes
*  You
