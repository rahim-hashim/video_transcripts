---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5179s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 27456
Video Rating: None
---

# BI 055 Thomas Naselaris: Seeing Versus Imagining
**Brain Inspired:** [December 09, 2019](https://www.youtube.com/watch?v=g8nFNPDfa6M)
*  You can look at a picture, you can imagine a picture, you can attend a picture, you can
*  detect a picture.
*  The same cortical machinery is being used in every one of these cases.
*  So this is an example, I think, where developments in AI have been essential.
*  There's something wonderfully satisfying about mastering a hard thing that you know can be
*  And doing it super well.
*  And it's tempting to trade that in for the uncertainty that you live with all the time
*  when you're trying to figure out your little slice of the question, how does the brain
*  work?
*  This is Brain Inspired.
*  Is there a difference between seeing a tree and imagining a tree?
*  If so, what is that difference?
*  And what does it say about how our brains process and or imagine images in our heads?
*  Today my guest is Thomas Nassalaris, who knows a bit about that.
*  Thomas runs his lab at Medical University of South Carolina, where if you go, he may put
*  you in an fMRI scanner and show you a famous painting, then later tell you to just imagine
*  that painting.
*  And when you're all done, he'll use encoding and decoding models to predict how your brain
*  responded and what information was in your brain.
*  We talk about all of that, as well as how far along we've come with fMRI in general
*  and how much farther there is still to go.
*  Thomas is a co-founder, along with Kendrick Kay, of the Cognitive Computational Neuroscience
*  Conference, where folks studying biological intelligence and artificial intelligence come
*  together to share ideas and good times.
*  So with regard to the CCN Conference and otherwise, we talk about the current state and outlook
*  for how the AI and neuroscience worlds are and are not interfacing well.
*  And Thomas also describes this huge fMRI dataset that he and Kendrick Kay have collected, from
*  which they're starting to be able to infer entire visual system network models.
*  You can visit his lab website to learn more.
*  That is at Nassalarislab.net or go to the show notes at braininspired.co.
*  Carson, Alexander, Chad, Thomas, Jeff, and Lisa, thank you guys for your support on Patreon.
*  I will be sending videos from the Brain Inspired course your way in the coming weeks.
*  If you're a new listener, you can learn more about that at braininspired.co.
*  The mountain in my backyard just opened for ski season, so I am strapping on my snowboard
*  and heading there soon.
*  Somewhere deep in my visual cortex, months ago, I clamped a representation of that snowy
*  mountain and it's been blurrily infiltrating my early visual cortex ever since.
*  But now I get to pass it through my retinas as well.
*  I hope that'll make more sense to you after you enjoy Thomas Nassalaris.
*  Thomas, thanks for being here and welcome.
*  Thanks for having me.
*  It's fun to be here.
*  What in God's name made you quit the glorious gold standard world of monkey neurophysiology
*  and go into human fMRI and were you ridiculed for doing so?
*  That's a good opening question.
*  A lot of reasons.
*  I think some of them were circumstantial.
*  I ended up in a lab that was just getting started developing a really interesting and
*  intriguing approach to fMRI.
*  I had the opportunity to work with people in that lab.
*  This is a very gallant lab at UC Berkeley.
*  People being like Kendra Kaye is still a good friend and collaborator.
*  So that was circumstantial.
*  If that hadn't been going on in the lab at the time that I got there, I probably would
*  not have made the transition.
*  But why did this set of circumstances, why were they compelling and interesting?
*  I came from, as a graduate student, I came from the lab of Georgopoulos, who was studying
*  population activity.
*  The idea was to record as many neurons as you could and build models that helped you
*  understand how whole populations of neurons were coordinating, in this case, our movement.
*  Very simple behavior.
*  I thought it would be interesting to try to take this population approach to vision.
*  My initial idea going to Jack's lab is that we were going to record for many neurons in
*  a visual system and try to build transforms between stimulus and brain activity.
*  Oh, wow.
*  Going from stimulus to brain activity is what's called an encoding model.
*  One of the things I was particularly interested in was reversing the transform.
*  Taking population activity and constructing a picture from that.
*  It seemed like an interesting and cool thing to do at the time.
*  It still does to some extent.
*  To get that to work, you need lots of neurons.
*  While I was busy setting up the techniques that we would need to move from the single
*  cell recording paradigm that was going on in the lab at the time to multi-neuron paradigm,
*  Kendrick came by one day and said, hey, I don't know what he actually said.
*  I'll just confabulate.
*  Something like, hey, let's just do this with f of r i.
*  We have the whole brain, every part of the visual system.
*  You'll work for two years to get 500 neurons and I can give you 5,000 voxels tomorrow.
*  It's data.
*  Yeah, right.
*  The question was, were the models that we were intending to build the encoding and decoding
*  models that would map stimuli to and from, in scare quotes, real brain activity?
*  Would they work when the activity in question was this weird aggregate signal coming out
*  of a voxel that took a million neurons, probably averaged them in some way, and then ran them
*  through this nonlinear plumbing operation?
*  It's just totally unclear that any of the insights we gained for decades of CAD and
*  monkey physiology would apply.
*  Now it seems naive to be surprised by the fact, but they did.
*  Very quickly, it became apparent to me that nothing, no analysis that I threw, I was even
*  considering throwing at neurons, would fail when I threw the net voxels.
*  Now I have the entire human brain, multiple processing levels, many quasi-independent
*  units, and a connection to the computational work, or a contiguity with the computational
*  work that I wanted to do and that had been ongoing in physiology.
*  Now add to that the fact that humans are just, they're just a lot more pleasant to work with
*  than what I was working with before.
*  They don't...
*  Yes.
*  Most.
*  Most.
*  Most of them are.
*  I mean, there's no comparison.
*  What I wanted to do was play with data, and I was willing, and I had built up a skill
*  set, a surgical and veterinary skill set over the years in order to give me access to the
*  data I wanted to play with.
*  And all of a sudden I like...
*  Dropped that.
*  I was surprising.
*  Yeah.
*  So I didn't drop it like immediately.
*  I, you know, I kept, I remained part of the physiology project until the end in terms
*  of Jack Galman's lab.
*  I mean, I think I was, I implanted one of the last Utah arrays that they used.
*  I think maybe they can correct you.
*  The whole surgical suite of skills that you learn is, that's interesting because it's
*  basically useless now, but if I'm in a room, I've had this thought occasionally just kind
*  of pops up if I'm reminiscing.
*  Like if someone fell and, you know, their skull busted or opened or something, I am
*  most likely the best person to attend to them in that situation, you know, which is a crazy
*  thought.
*  Yeah, you could probably do, you know, slightly less harm than good, I think.
*  Yeah, less harm.
*  Yeah.
*  But no one, did anyone tell you, hey, you're going down the wrong path here.
*  You need to stick with monkey neurophysiology?
*  No.
*  I mean, I bet, you know, I, the Gal Lab was, was at least at the time kind of insular.
*  We are all sort of feverishly working on our own little thing.
*  Yeah.
*  And, you know, I was getting positive reinforcement from within the lab and things started working
*  well really quickly, you know, and we were getting positive feedback in the form of publications.
*  So it didn't, no, no one said, what the hell are you doing?
*  You know, in retrospect, there's a problem with making that transition just in the sense
*  that, you know, while people who started doing fMRI as grad students and continued to do
*  it through their careers, you know, where they were learning the kind of art, the arcana
*  that goes with any imaging modality, I was learning a completely different set of, you
*  know, voodoo magic spells.
*  And so that, you know, I didn't, I didn't really appreciate the extent to which there
*  would be a kind of learning curve.
*  When I started my own lab, I was like, I'm an fMRI researcher now and I have to build
*  this infrastructure in my own lab.
*  Oh, yeah.
*  That was, yeah, that actually took some doing.
*  But that, you know, that's whatever.
*  Anytime you try something new, you have to deal with that.
*  So it's fine.
*  I have an EEG friend who just, you know, a couple of years ago started his own EEG lab
*  and it seems like that took much less, it was a much faster learning curve.
*  I mean, he had done it in the past, so he knew what into what went into making a rig
*  and everything. But it's a it's a less of a beast, I think.
*  I mean, it has its own issues as well.
*  So, yeah, I mean, every measurement modality is its own specialized craft.
*  Well, and starting a monkey lab as well is I was always worried about that.
*  Like, oh, my God, that's it takes so much to just in administrative issues alone.
*  Absolutely. Yeah.
*  The whole administrative aspect of it.
*  And so it's, you know, it's heroic work.
*  And so I am convinced that FMRI is essential.
*  It's an essential tool.
*  So, you know, I described to you sort of why the transition, why I was able to make
*  it or how I rationalize the transition at the time.
*  I still think there are good reasons.
*  But my appreciation for FMRI has grown immensely because, you know, when I started
*  my own lab, I started studying things that really only humans can do or that.
*  Well, that's too strong a statement that is very, very difficult to study in nonhumans.
*  That's mental imagery.
*  You know, it's a relatively easy experiment, you know, or at least set of instructions
*  to tell a subject, close your eyes or whatever, stare at a blank screen
*  and imagine a unicorn.
*  And you could develop some kind of animal model of that, I'm sure.
*  Probably people are working on it.
*  But, you know, one of the defining aspects of mental imagery is the subjective,
*  phenomenal component that subjects can communicate and confirm took place.
*  They can say, yes, I did what you asked me.
*  In fact, you can be the subject in your own FMRI experiment and confirm to yourself
*  that you imagined the things you were supposed to imagine.
*  So that I mean, that's that's a really, I think, important thing.
*  And mental imagery is it's just one of the phenomenon
*  that are so much easier to access or maybe only, you know,
*  it's only possible access if you're working with humans.
*  I mean, language is the other obvious, obvious phenomenon.
*  But, you know, I mean, the kind of cognitive flexibility that humans show,
*  you know, I mean, you can just kind of give someone a set of instructions,
*  a set of visual puzzles and just tell them to solve it, you know, and they just will.
*  So being able to access the processing that takes place
*  when uniquely or, let's say, strongly human
*  cognition is going on, I think it's essential.
*  And I think FMRI is unparalleled.
*  And it's in the access it gives you to that.
*  Well, you just ran through multiple topics that I want to
*  that we'll dive a little deeper into here.
*  OK, I want to back up and kind of ease our ways in our way into it.
*  One of the things I was going to ask you, speaking of head injuries,
*  is were you a skater growing up?
*  But now I know you have skateboards on your wall behind you as we're speaking,
*  like frames. Yeah, I remain a skater.
*  I am. There's a skate park
*  about five minutes from my house here in Charleston.
*  Wow. Lovely, two lovely bowls and a snake run in a street course.
*  Were you a punk kid? No, no.
*  I think I was.
*  I didn't really embrace skating culture.
*  Oh, I mean, I had no problem with it.
*  But the kind of.
*  Yeah, I kind of punk aspect of it, I never really got into.
*  I think I like to geek out on the technical aspects of skating when I was young.
*  Gotcha. Now that I'm old and I'm slow, I like.
*  Just carving bowls, dropping in and just doing like
*  there's such a division at the skate park between
*  dudes who, you know, like the 45 year old dad
*  and these, you know, seven to 16 year old kids.
*  You're not trying to keep up with the lingo?
*  No, no, that would be absurd.
*  I mean, you know, draw the line somewhere for God's sake.
*  Yeah, yeah, I don't even try.
*  You know, I just kind of keep by the sense and watch and admire these kids.
*  Insane, beautiful, insane acrobatics that they pull off feet away from me.
*  It's too bad you can't skateboard in an fMRI rig.
*  That would be a challenge to break down and study.
*  Yeah. Well, imagination, I suppose, imagery, skateboarding.
*  Yeah, you could.
*  OK, so Thomas, I get I get listener emails asking for advice here.
*  And in one.
*  The emailer was seeking advice on how to achieve this very particular state
*  in terms of their career, like the trajectory, they had a very particular
*  trajectory in mind that they would end up studying this very particular thing
*  in this very particular way, using these very particular methods.
*  And part of my advice was to not worry too much about the destination,
*  because the minute you learn something,
*  you discover how little you know and your path and your goals change.
*  And that happens about once every two weeks or so until you die.
*  I also advised to eat healthy and try not to die.
*  But so good.
*  Was that was that good advice or bad advice?
*  I think that's perfect advice.
*  I would add, though, you say you said that something that happens every two weeks,
*  I would say that happening two weeks, a new and exciting
*  this confusion that pulls you in multiple directions
*  and makes you uncertain about which way you're supposed to go.
*  That happens every two weeks if you're doing your job, you know, if you're
*  constantly pushing and challenging yourself and casting yourself
*  into, you know, new questions, new terrains.
*  That's the excitement, the exhilaration and the exhaustion.
*  The exhaustion. So in some sense, it's a well, not a punishment,
*  but it's a punishment and a reward for doing your job well, I suppose.
*  Yeah. You know, I spent I spent a lot of time in the past
*  thinking and talking to other people about what the right metaphor is for science.
*  You know, and because sometimes it's kind of like it is like you describe as hard
*  that you feel like you're ascending to some new vista.
*  And, you know, I have this with like an infinite horizon
*  and all will be revealed to you.
*  Yes. Make it up another few feet.
*  It's a false summit. Right.
*  It is. And you keep climbing and climbing, but you do get higher and higher views.
*  It feels like that sometimes.
*  I think other times it feels like you are toiling to like
*  dig a grave for your best ideas, you know, like where your best ideas will be buried.
*  That's the thing. It's like you're working so hard.
*  And the harder you work, it's like the bigger shovel full of dirt
*  that you're scooping out for the the faster you dig.
*  You're digging your grave. So that's a real conundrum.
*  Yeah. Yeah. I think lots of metaphors fly.
*  Well, thanks for talking with me today, Thomas.
*  It's been a great conversation.
*  And let's not end on that, I suppose.
*  OK, no, no, that's a little grim.
*  Is there is there some advice that that sticks out in your in your head
*  that anyone has given you that you might consider the worst advice
*  you've ever gotten in terms of science?
*  Oh, no.
*  I think to the credit of many of the mentors I've met along the way.
*  Many of them sort of delivered not to me individually,
*  but to sort of my cohort, these these prognosis
*  about like what our likely fate was in science.
*  You know, and we had one of these, you know, classic
*  talks in my first week of grad school
*  where this this professor, very successful,
*  you know, and just kind of hard edged kind of dude.
*  It was like 80 percent of you will not have the job
*  that you think you're going to get.
*  Yeah. Right.
*  So had I interpret that as advice to do something else,
*  it would have been bad advice.
*  But I don't I don't think he was delivering it like that.
*  He was just saying these are the stats.
*  Yeah. He wasn't saying go away.
*  No, no. So, yeah.
*  I honestly I can't think of.
*  I can't think of any advice I've received has had much impact
*  one way or the other, to be honest.
*  I mean, just because again, there is so much uncertainty in science.
*  Yeah. You never really know if the thing you're working on is going to yield.
*  It's going to yield what you hope it will.
*  Or if it's going to lead to just another problem or a dead end.
*  And you can ask people, you know, is this the right thing?
*  Am I doing the right thing?
*  And there's so much noise in the feedback.
*  So much. Yeah.
*  It's like the review process.
*  So not nothing really stands out as particularly.
*  How important is it to sort of stay the course in what you're doing
*  as you're twirling away at something and you don't know if it's going to work out?
*  And it seems like it might not.
*  And but you have this gut intuition.
*  You know, what what's the right amount of intuition to stick with
*  versus the amount of clarity received from facts?
*  Yeah. We'll move on soon.
*  No, no, I feel like if someone had kind of said what you just said
*  in an assertive way to me, that would have counted as good advice.
*  So allow me to offer advice.
*  And that is, you know, perseverance is essential.
*  And any scientist will tell you this.
*  You know, most breakthroughs come long after you kind of are
*  the original excitement of the idea that motivated you to get into a project.
*  It's kind of decayed into and it's transformed itself
*  through a variety of different emotions, you know,
*  dread and determination and then re-excitement and then redread.
*  Failure acceptance.
*  Yeah, right. So you have to you have to commit to multiple cycles
*  of attempt and failure, false discoveries and things like that.
*  And so you kind of ground out and something that you're convinced is
*  probably pretty true.
*  And just pushing through, keep, you know, continuing to push,
*  especially if you if your own personal velocity is slow.
*  I mean, which I think is fair to say about me.
*  It takes me a long time to bring projects to completion usually.
*  So I mean, I think it's particularly important to keep going.
*  Well, that is another frustrating thing.
*  I mean, I know we're talking a lot of culture here, but you have this idea
*  and you can sort of immediately see the project and how it's going to turn out,
*  how to set it up, how to implement it.
*  But you don't realize the end of what you're seeing is actually 20, 30 years in the future.
*  Yeah, and it's resemblance.
*  You know, this this mental image you have of this thing that the project is going to be.
*  It often is really poor approximation to what you end up with.
*  Yeah, but so my wife is a clothing designer and we, you know,
*  we talk a lot about the creative process.
*  I think it's really the same in science as it is.
*  I believe you.
*  Yeah.
*  And in the arts, you you kind of get this idea about the way things could be.
*  And so you're creating, you know, you're creating a narrative or maybe a picture.
*  And then you go and the process of checking if that's true is very similar to the process
*  of putting an idea on paper or into words, I think, for an artist or a writer.
*  Like the immediate feedback you get is, you know, it always causes you to refine the initial idea.
*  It makes one hesitate to proceed because, you know, as soon as I do something that's worth
*  doing, that's any sort of progress.
*  Oh, the feedback is going to be rough.
*  Yeah.
*  The resistance is hard.
*  To make an idea, you know, the idea is another metaphor, you know, science, science as
*  parenthood or at least midwifery, right?
*  Yeah.
*  Oh, you're bringing an idea out into the world.
*  It is that once the most precious and most vulnerable thing in the, you know,
*  a new idea, it's like a baby, there's nothing more precious, nothing more vulnerable.
*  And it's immediately going to get exposed to all kinds of abuse.
*  And the world is not going to accommodate it.
*  I mean, the world does not accommodate your theories in the way that you want it to ever,
*  you know?
*  And so that's another helpful way of thinking about scientific processing.
*  Don't have kids, guys.
*  Don't have kids.
*  So you ran the show at Cognitive Computational Neuroscience Conference this year.
*  Your friend and collaborator, Kendrick Kay, with whom you conceived this idea
*  and decided to execute and have executed well.
*  So I know Kendrick is kind of lazy, I guess, right?
*  Because, you know, he didn't even attend this year.
*  No, that's not a word I use to describe him.
*  I think he may be oversubscribed.
*  I mean, he's got a lot of projects.
*  I'm one of his many collaborators.
*  He's doing lots of things at any one time.
*  Yeah, so I think that, you know, he and I have multiple projects together.
*  And we sort of trade, you know, we can kind of have a sort of an economy
*  where it's like, I'll work on this and you work on that.
*  So I totally understood his choice this year.
*  It was my first time having currywurst in Berlin this year,
*  which I thought was OK.
*  Currywurst is OK.
*  Achieving our mission, you know, cultural exposure.
*  I took that home.
*  And the other thing I took home, besides things from the conference, of course,
*  but culturally, the other thing I took home was, good God, they smoke a lot there.
*  I couldn't believe it.
*  Yeah, it's almost like, you know, the effects of smoking are just like this cultural thing.
*  If you smoke in the right culture, you won't get cancer.
*  It must be.
*  Have you recovered?
*  You did a great job.
*  It was really impressive to see you keep your head on straight
*  and organize the whole thing and just keep it running.
*  So have you recovered from the experience yet?
*  Yeah. Yeah, I think so.
*  I think I'm like everyone else.
*  Like what you really want to be doing is just being in your lab,
*  working on your projects and ideas, stuff like that.
*  So when I got back from CC and I immediately just kind of put it out of my mind
*  and started working on stuff that I was excited about,
*  because, of course, I got all kinds of ideas and inspiration from the conference itself.
*  And now I think just so it's been about a month or two.
*  And now I'm kind of getting back to organizing 2020
*  and, you know, grant reviews and submissions and papers, you know, the whole.
*  Yep. The whole rigmarole.
*  I'm out. See, I'm out of it.
*  I have to doubt.
*  Yeah, you're kind of.
*  It's just the good stuff.
*  So focusing on that.
*  So the kind of the point of CCN is to bring together these diverse fields,
*  neuroscience, computational neuroscience,
*  artificial intelligence, cognitive science.
*  And as you gain more experience,
*  what do you see as the ongoing challenges to bring these fields together?
*  Are there things that you've learned throughout,
*  you know, kind of each conference, each iteration like, oh,
*  do you see a pattern of ongoing challenges?
*  So, I mean, some of the challenges are very generic and the things I've learned.
*  Some of the things I've learned are very generic,
*  just about human behavior and coordinating lots of humans around it.
*  But that's not your question.
*  So, yeah, there's lots of things.
*  So the cultural there are cultural differences between the different disciplines
*  that affect, for example, expectations around publishing.
*  AI is as a field, you know, people build their reputations to a large extent,
*  publishing and conference proceedings.
*  And those are in some sense not considered a real thing in biology and neuroscience.
*  Fast and loose kind of considering.
*  Right.
*  Right.
*  It's a weird thing.
*  So that the conference, the submissions to a conference are much more rigorous
*  for engineers and AI people than they are for many neuroscientists,
*  where you might just submit an abstract and it's sort of some quality controls applied.
*  But then the paper process, you know, getting a paper through view
*  is extremely rigorous in biology.
*  Yeah.
*  It can take a year from the time you submit a paper,
*  which is for a conference proceeding unheard of.
*  So there's that kind of stuff.
*  But I mean, obviously, though, the conceptual issues
*  are perhaps deeper, at least more interesting.
*  So one of the things that's come up and
*  there's a sort of asymmetry between neuroscience and AI right now.
*  There is, I think, not everyone feels this way,
*  but there is a sense in which AI is making a lot of progress
*  by sort of operationalizing concepts that are loosely sort of related or borrowed maybe.
*  Well, they use the same term.
*  Psychology.
*  Yeah, they at least use the same language
*  and they use some of the concepts that are in neuroscience.
*  But it seems like the cycle between AI and neuroscience felt tighter in the past.
*  Whereas now, the things that can be done in terms of building really impressive systems
*  that can accomplish tasks that many neuroscientists wouldn't think to study
*  in the laboratory.
*  They're so complex.
*  And I think it's actually at the level of tasks that there's a real...
*  Like what?
*  Do you have an example?
*  A real distance.
*  Like driving a car.
*  Or just like captioning an image.
*  I mean, just having someone look at 100 images and write out a caption.
*  And just scan the brain while they're doing that.
*  Okay, now go.
*  Tell me what happened.
*  And neuroscience tend not to do experiments like that.
*  It's such a more straightforward...
*  It's application-based more than understanding-based, it seems.
*  Right.
*  So there's another, I think, shock or surprise to me that a relatively small set of tools
*  in this kind of deep learning age can be utilized to solve tasks that I would have thought would
*  require much more sophisticated ideas and machinery to carry out.
*  That you could argue about the extent to which AI people are really solving really hard tasks.
*  I mean, captioning is a good example.
*  I don't know.
*  I have to be careful.
*  You have to be careful whenever you say what AI can and can't do.
*  It's next week's crop of papers.
*  Last week.
*  Last week.
*  Yeah.
*  You said...
*  But last I checked in, the kind of rich, interpretive interaction that human beings
*  can have with a painting, for example.
*  There's nothing like that in AI.
*  Right?
*  But the caption might come out the same.
*  What do you mean the same?
*  Well, if I'm looking at the Mona Lisa, what an AI caption
*  underneath a picture of the Mona Lisa might say, whatever my internal milieu of my experience
*  looking at the Mona Lisa, the caption, the text might come out the same as an AI's would.
*  Right?
*  It could.
*  It could.
*  But as a neuroscientist, I'm very happy to just immediately move the goal posts.
*  We move them weekly, apparently.
*  Yes.
*  Okay.
*  Give me an AI system that can tell you, is her smile menacing or altruistic?
*  What is she smiling about?
*  When you finish that sentence, you hear boop, boop, boop, boop, boop.
*  And then they come back a week later with something that can do that.
*  Right?
*  You put your finger on the disorienting pace of AI research relative to neuroscience research.
*  I mean, one of the things I was doing for a while, and I still am to some extent,
*  is taking AI systems and kind of opening them up and they give you a bunch of space and variables.
*  And you can regress them onto the brain.
*  The whole craft of regressing big complicated models, the guts of big complicated models,
*  onto lots and lots of different parts of brain.
*  That in and of itself is a piece of work that you can put a lot of work into.
*  But the interesting part is the model, the one that supplies predictors.
*  And that project right now, or that way of approaching or kind of linking AI and neuroscience,
*  I think is really hard to do simply because the space of models that could be compared
*  is overwhelming. It outstrips what anyone can do in a laboratory.
*  Yeah.
*  And the complexity of the models and yeah, the rate at which they're being developed.
*  So I almost see...
*  I'm still thinking this through. I'm still processing. I mean,
*  it's because I think right now it's anyone's guess what the relationship of neuroscience
*  and AI is going to be.
*  See, that's your problem. You're a processor. You're a slow neuroscientist. You need to go
*  in the AI, the fast cycle route, man.
*  Yeah, I don't know how that's doable.
*  Stop thinking about it and just do it, damn it.
*  Yeah, sure. That's good advice. There you go.
*  Yeah, so I guess this kind of confusion, these asymmetries between AI and neuroscience
*  in terms of their pace, this kind of quandary that neuroscientists are in,
*  what do we do with all this computation that's been going on and that seems to be solving hard
*  problems, hard tasks? We would love to have an explanation for how the brain does any one of the
*  tasks that a lot of these AI systems are solving.
*  So I just think the uncertainty around those questions is motivation itself for the conference.
*  You could take the stance that if you're doing AI right now, right now is a good time to just do it.
*  And not necessarily worry about whether some new operation I've coded up is
*  taking place in the basal ganglia or is it prefrontal cortex.
*  But my hunch, my prediction is that the kind of techniques that are driving progress right now
*  will plateau, as they always do. The goalposts for explaining human behavior, creativity,
*  intelligence will remain, seem just as distant as they've always seemed.
*  And the intuitions and insights that neuroscientists produce on their yearly instead of weekly basis
*  or rate will be essential. That's my operating assumption.
*  Well, you have to have that assumption to stay in your field, keep doing what you're doing, right?
*  You do.
*  Yeah. For the conference in particular, are there, and in this past one, for instance,
*  were there topics that you thought were underrepresented or missing or what are
*  areas with just from your vantage point with maybe the most opportunity
*  for someone to enter the field and make viable progress, advance the field?
*  Okay, so I mean, one thing that was missing and this is something we can work on
*  is I think motor control and its interface with robotics.
*  That's interesting that that's missing. You wouldn't expect it.
*  Yeah, well, I mean, it's something I personally would like to learn a lot more about,
*  especially, I mean, just again, personally, you know, I started out
*  doing motor control and thinking a lot about that. Yeah, so I would love to see more of that work
*  represented at CCN. But it's not like there's, yeah, a place to jump in.
*  And make progress. Is that what you said?
*  Yeah, well, that would be a place. But the motor push is interesting because I think that that
*  is a wave that I thought that it was sort of on the upswing. I know perception, of course,
*  has been there and it continues to be massively represented in the literature and in people's
*  labs. But motor function as an important cognitive function is on the rise, I feel,
*  as a thing that brains fundamentally do. That's a strange thing to say, like what brains are
*  computationally for. The answer movement seems to be on the rise.
*  Yes, that idea, I feel like I'm running into it more often. And it's, I mean, intuitively,
*  it's really appealing. All the sensory processing sort of has to be set up in a way that makes
*  the coordination of movement efficient and meaningful. What I don't know right now is
*  the extent to which techniques that are being used to solve computer vision problems,
*  which is the branch of AI I'm most familiar with right now, how they're faring in terms of
*  solving control problems. I don't know the answer to that. It's something I've been meaning to
*  learn more about. It seems essential. That's the one thing that you don't know about right now.
*  I like that. My words, not yours. So just a couple more questions about this sort of stuff. And then
*  I want to get into what you do and your approach in doing it. What do you think, if you had to
*  choose, if all your skills were gone, what would be the one skill that you would try to tackle
*  going into this broad sort of neuroscience AI field? All my skills are gone. Or you mean like
*  if I was starting over? Yeah, you're a skater, you're on the half pipe, and you're like,
*  hey, I think I want to get into neuro AI. But I don't know, like, what should I learn first? And
*  you know, what's the most important thing for me to know? Math. Math. There it is.
*  Get a math major. I think it's the most all purpose. I mean, it gives you a technical skill,
*  and it's an intellectual workout. But that's funny. I mean, so because I started off as an
*  undergrad, just kind of humanities, your math and philosophy, right? Yeah, but I started off
*  just taking literature classes and worthless. Priceless, I would say. Priceless. Yeah. All
*  right. And at some point, realize that most of the things I was interested in philosophy, you could
*  actually you're kind of lucky enough to be born in an age where you can attack them scientifically,
*  or address them scientifically. And I realized this passion, this interest, this opportunity
*  rather late. I was like a junior. Undergraduate? Yeah, yeah. I had spent, you know, three years just
*  doing soft science at best. Tolstoy or Dostoevsky? Back then it was Dostoevsky,
*  now it's Tolstoy. Me too. What the hell happens to us as we age? All right, that's a different
*  question. But that is, you know, I mean, well, okay, so what do you think is like the least? So
*  math is the most important. So what do you think is something that you consider a waste of your time
*  looking back? You think that the literature was priceless, right? So what's least important? Or
*  what was a waste of your time? You think? Nothing. I mean, I've gone down a lot of dead ends,
*  obviously, like most people have. But you know, I've always learned from them. I guess I could say
*  it would have been, it might have been better for me to have started studying science a little bit
*  earlier. But I don't consider, you know, the seminar on Ulysses like a waste of time.
*  Really? Ulysses? Not a waste of time? A highlight. No. All right. I can't do fiction anymore, man.
*  It's rough. I don't know what's happened. So, Thomas, all right, let's talk about some science.
*  Here's my abridged historical account of attitudes towards fMRI in neuroscience. This is roughly
*  chronological. Yeah. Ah, it's great. Ah, it sucks. Oh, hey, it's great. Ah, it sucks. And then maybe
*  back and forth a few more times. So I don't know if that's accurate to you. But when fMRI was
*  introduced from my understanding of the history, it actually took a few years for people to figure
*  out how to use it properly, how to use it well for experiments. And maybe the first, one of the first
*  useful ways of doing this that came along was the subtraction method, where you subtract the
*  activation while someone is looking at a tree, for instance, from the background activation when
*  someone's not looking at the tree, right? And then there have been multiple advances along the way,
*  which I'll just skip over, and then comes along this new shiny object, which is multi-voxel pattern
*  analysis. And in fact, when I started my postdoc, there was one of the selling points to me was like,
*  oh, here, I don't know if I should name the name, but it's Frank Tong was like down the hallway.
*  He was like, oh, he does multi-voxel pattern analysis. And that was like a selling point. Oh,
*  that's the new way to go. What is that? What is multi-voxel pattern analysis? And what's good
*  about it? Well, I just, I just want to say that that I, my, my general feeling about fMRI, given
*  this, you know, this cycle of enthusiasm, is that we, we still, as a community, are not doing justice
*  to the quality of the data. Oh, I see. The entire brain, and given the amount of coverage,
*  that the resolution is actually excellent, you know, pretty reasonably well resolved, given the
*  fact that you're seeing the entire brain in depth. Yeah. Shouldn't we have it all figured out by now?
*  I mean, it holds out the opportunity of figuring out a lot more than we have. And I think that we,
*  we're still trying to figure out how to analyze this insanely rich data, right? So,
*  fMRI started out as big data. And the techniques and the ideas to analyze it, just what they weren't
*  there. And people did, I think, brilliant things, simplifying the data down to, in a way that allowed
*  them to make incredibly important discoveries in the, kind of the brain mapping era, you know,
*  the kind of what, what does what, or what might do what era. I remember, I had like a tiny bit
*  of training. I did a rotation in graduate school, and it was an fMRI lab. And I remember literally,
*  in Excel, like, circle, like an ROI, a region of interest, adjusting a circle on a picture of a
*  brain, and then like using the data, like counting the data in the circle. I was like, well, this is
*  crazy, but it's a simplification. It is. And, you know, and you choices were made. And you're right,
*  I mean, as a field, I shouldn't say we, because I came to it rather late. People have been constantly
*  refining their approach. Okay, so, so you kind of go up through the kind of subtraction era and into
*  the MVP era. And what is MVP? It's a way of trying to extract information from patterns of
*  brain activity patterns. I mean, the best way I can think about it, or to kind of summarize it,
*  is take any number of n voxels, and you can think of it as a vector. And up until MVP,
*  people were just analyzing the length of the vector. They didn't really think about what
*  direction it was pointing in. And MVP gives you a set of tools for deciding if two vectors are
*  pointing in a different direction, a significantly different direction. Right? So that's, that's a
*  simple right. So if the two vectors correspond to seeing a face, seeing a place, or to thinking
*  about something versus seeing something, you can start gaining a lot of information instead of,
*  you know, what does what, you can start saying which states are discriminable from other states.
*  That's a much more detailed query that you can make if just by taking into consideration the
*  orientation. So you can decode a lot more. You can, I mean, it allows you to do decoding,
*  right? Because, I mean, you can divide the space of brain states, you can put them into two buckets,
*  and you can say, all right, now I've measured a brain state, is it in bucket one or bucket two?
*  And then, yeah, you have a decoder. I think, right, so the thing that miss it that,
*  that is missing, which is kind of obvious, now I hope that, all right, so you have two vectors,
*  and they're pointing in a different direction. Why? What do they actually represent? And to
*  answer that question, you have to build a model, a model that transforms, in my case,
*  in the case of vision, stimuli into this vector. And that transformation, understanding and building,
*  designing that transformation takes a lot of work. And that's kind of where, I think that's where the
*  field is right now. So one could say that one of the things that MVPA is missing in that sense is
*  representation. Yeah. So the term representation can be thorny, right? It's been referred to as a
*  filler term, for instance, and that it gets used, like when we don't understand how something works,
*  we can just say that something in the environment is simply represented by the neural activity.
*  And in the case of like MVPA, that would be like the pattern of voxel activity. And then there's
*  an exhausting philosophical thread, speaking of philosophy, as philosophical threads tend to be
*  exhausting, that on what would even count as representation, and you can go down that hole
*  and never come out the other end, of course. Yes. So representation plays a central role in your
*  approach to brain processing with these models. How should we understand representation in the
*  way that you use it? Yeah, I think it's a fine word. I think, I mean, it can be used meaningfully,
*  I think. So when I use it, I typically mean something very specific, that there is an
*  encoding model. So it's defined by the fact that of there being an encoding model?
*  Yes. Gotcha. That is what I mean. So when I use the word representation, I mean,
*  I'm referring to what is being encoded in brain activity. And there are tests for determining
*  what is being encoded, or at least for adjudicating between different hypotheses about what is being
*  encoded. And you can argue about what the best way to test or to adjudicate is. I think there's
*  plenty of reasonable ways to do it right now. But the idea is that what you want to know, so again,
*  this is very vision specific, is brain activity has a nonlinear relationship with stimuli,
*  visual stimuli. And how do you conceive of that nonlinear relationship? The approach I've been
*  taking is, and many others, is you think of the stimulus in its rawest form, a pixel-like
*  representation of the stimulus being transformed for a nonlinear operation into a feature space,
*  and defining that feature space, its function, its properties, whether or not it's efficient or
*  optimal. It's a really interesting set of questions where my mind is sort of parked and has been for
*  a long time. And then the whole process of building and coding models is really an exercise
*  and testing whether this feature space that you defined is going to predict variation in brain
*  activity in the parts of the brain that you find interesting. But it's in defining the features and
*  in the representation that I think the real interest lies for me. It also is a gateway into,
*  I think, questions not just about representation, but about processing, which is another vague,
*  another word that sort of means everything and nothing simultaneously.
*  Processing has sort of taken over in my mind as the important thing.
*  So my working definition of it, I agree, it is the important thing, my working definition of it right
*  now is you want a model that's flexible enough to be queried in multiple ways that can tell you
*  about multiple, let's say, operating modes of the system or the subject. So again, I'll just
*  refer to my own work because these are the examples I'm most familiar with.
*  You can look at a picture, you can imagine a picture, you can attend a picture, you can
*  detect a picture. The same cortical machinery is being used in every one of these cases.
*  The tasks I've just referred to have very different criteria for success, but the machinery that
*  accomplishes them, we know is the same. You're getting engagement of visual cortex broadly
*  construed with every single one of those things. So defining an architecture that can predict
*  brain activity states in these different operating modes, right? Either by reconfiguring, you know,
*  and not by just sort of pulling one model out and putting another model in. But one, a model or
*  a way of relating brain activity to cognitive state and to stimuli that, you know, by reconfiguring
*  its inputs or adjusting some smallish set of knobs, right? We can explain how the brain
*  transitions from these very different tasks. That's what processing means to me. And I think
*  that's where I'm trying to head. And I think that's where the field needs to end, in my opinion.
*  Yeah. So, okay. Well, maybe in a really broad sense, let's just go through,
*  I mean, do you call it voxel-wise modeling these days?
*  Oh, yeah. Yeah. I mean, voxel-wise is helpful to people working in fMRI because it distinguishes
*  the approach from NDPA or ROI-centric. But it could just as easily be cell-wise.
*  You know, I started off talking about how the same computational model applies to very different
*  measurement modalities. So, models that we're trying to predict single neuron spiking activity
*  transported just effortlessly to bold activity in voxels. And now I have two photon
*  activity that a colleague has given me, or two photon images. And I can just sort of apply the
*  same model to predicting single change in individual pixels. So, these are small pieces of cell.
*  And they work. Once you get it into a feature space?
*  Yes. Right. So, okay. Well, the basic thing is you take an image, let's say, or some stimulus,
*  like an image. And then you build an encoding model to take that stimulus and transform it into a
*  predicted brain activity for whatever kind of signal that you're measuring. And then you can
*  actually decode from, build a decoding model based on the encoding model and the activity,
*  and decode out the stimulus from the brain activity at that point. And so, you have a kind
*  of a full circle system. Yeah. Yeah. So, there's, right. So, if all you want to do is decode,
*  you can skip the encoding step if you want to. But there are advantages, scientific and technical,
*  to building an encoding model first. Well, it's explanatory, right?
*  Yes. Okay. If you want to explain brain activity, you need an encoding model. Right. So, I mean,
*  here's an example that I discuss a lot, sort of just a thought experiment. There's basically
*  an infinite number of things you can read out from a brain area. And some of them are really trivial.
*  Right. So, I could give me any, you know, 50 voxels from any brain area, and I can read out
*  really dumb things, like whether or not there's an image on the screen, just like luminance or
*  contrast. It counts for a huge amount of variance. Right. That's true. So, I can decode that with 100%
*  accuracy from some mysterious visual cortical area deep in the ventral stream. You don't need
*  AI to do that. Right. But it obviously doesn't mean that that's what this interesting ventral
*  stream area does. It's just, you know, I mean- We learn the light must be on, guys. That's what we
*  learn. Right. So, you can really get, you have to be careful with what you infer from decoding success.
*  An encoding model, on the other hand, would reveal if you build an encoding model in which contrast
*  is your only predictor and you're deep in the visual cortex, it's going to, it is going to
*  account for a lot of the variance, but not the variance that makes it interestingly different from
*  previous or the next visual area. The one that we're actually interested in, the one that
*  discriminates certain kinds of objects from another. So, encoding models let you know how far you have
*  to go before you can claim. Well, they define victory and they give you a measure of how far
*  you have to go to be able to claim it. Now, that measures prediction accuracy and there is a
*  difference, I think, between accurate prediction and understanding. Another philosophical, you know,
*  issue, an important one, but encoding models have that very strong and particular advantage
*  of letting you know where you stand. So, let's maybe talk about, I'm using
*  an example from your work. So, one area of study that you pursue is mental imagery,
*  which you've already talked about, which is another, yet another fun philosophical deep dive that
*  one may never recover from. Well, I mean, the cool thing is that I really do think that progress
*  can and is being made on mental imagery, which is this thousands of year old question.
*  Philosophical question and science is helping make progress, yeah.
*  Really, yeah, which is really gratifying. As I mentioned earlier, that is the exact reason I
*  got into science, is to pursue this kind of philosophical question. So, you can make a lot
*  of progress using techniques that have been built to study visual responses. So, the thing we've
*  been working on for a while is imagery and coding models. So, these are models that relate brain
*  activity during imagery to stimuli that you've asked subjects to imagine.
*  So, you see a Van Gogh painting and then later you're asked to imagine the Van Gogh painting
*  or something. Yes. So, what features of that stimulus that's being imagined now, not seen,
*  are encoded in brain activity? How is that code different from the code you would get if you were
*  seeing it? So, questions about, you know, are mental images really images, you know, these old
*  philosophical questions. Yeah. They sort of evaporate. They're just sort of like fog that blows
*  away and you pose these concrete questions. Here is brain activity, measurable brain activity,
*  and I can build a transform between stimulus and brain activity. And I can do it when people have
*  sat there looking for hours at an empty screen and just a mostly empty screen looking at tiny
*  little cues that says, imagine this, now imagine that, now imagine that. I can build maps between
*  unseen stimuli and brain activity that are extraordinarily, in my opinion, I think they're
*  really remarkably accurate in terms of their prediction power. You can predict what people are,
*  you know, how people's brains are going to respond when they're imagining, you know,
*  hundreds of mental images. You know, then there's concrete questions you can ask. They're
*  not philosophical. What is the peak of the tuning curve for imagined versus seen spatial frequencies?
*  What is the region of imagined versus seen space that most excites of oxal? How large is that
*  region? Does it move between imagery and vision? These are really direct questions that you can
*  answer. So you can kind of take and make these measurements. Well, I'm saying you can because
*  we've done it. It was a question whether or not you can apply these methods, to me at least,
*  whether or not you could apply these methods and have them tell you anything meaningful. By these
*  methods, I mean, you know, visual encoding model methods to mental imagery. There's then a challenge
*  and you do see very, very real differences, it seems, between how seen and mental images
*  are represented. Perhaps not surprisingly, mental images, the code for mental imagery is less
*  specific. And I think that that accords very well with, you know, our most people's experience of
*  mental imagery. And intuition, yeah. And intuition, but to be able to measure it in terms of receptive
*  field size and spatial frequency tuning function is very satisfying. I mean, it really removes the
*  debate from, you know, the kind of discussion about mental imagery out of the realm of philosophy and
*  kind of internal thought experiments. And then you have the challenge of explaining what kind of
*  computational framework or what kind of network architecture will produce these different codes,
*  these distinct brain activity codes. I suppose this is where your sort of theory of, you know,
*  mental imagery comes in. It has to do with predictive coding. Do you want to talk about it?
*  Yeah, I would love to. So this is an example, I think, where developments in AI have been
*  essential. Right? So there's a theory of generative modeling. It's been around for a while. It actually
*  predates deep learning by many years. But it provides such an obvious and tantalizing
*  framework for thinking about mental imagery. Because one of the things that distinguishes
*  generative models is the ability to synthesize images. And it's something, so if you think,
*  if you conceive of a generative model as being implemented in a network, it will be a network
*  that has connections that map not just from stimulus to internal state, but from internal
*  state to stimulus. And you can clamp internal states and propagate activity back toward the
*  sensory layer and get a picture. So what does that mean to clamp an internal state?
*  Clamping. So formally, in our model, clamping is conditional inference. So the theory, and this is
*  not my theory, this is a theory that others have worked out and explored for many years prior to me,
*  my work on mental imagery, is that the visual system somehow represents a distribution,
*  a probability distribution over representations of things in the world. This distribution can
*  tell you how likely it is for certain sets of states to co-occur. Right? Sky and blue,
*  beach and sand, whatever level of representation you might be interested in. Now, in that context,
*  vision is cast as posterior inference. So you want to derive a distribution over a set of visual
*  features given the stimulus. The stimulus is taken as a given. And it kind of makes sense
*  that there are no feedback projections to the retina that can kind of, by which you can cortically
*  control retinal activity. So in some sense, it is taken as a given. Now, you can extend that notion.
*  What we've done is just kind of extend that idea to account for mental imagery. So we make the
*  assumption that the kind of clamping that takes place in the retina can happen internally. Right?
*  And this is a representation level assumption. I don't have a theory about how this happens
*  physiologically. Yeah. But the idea is, you know, so you can sort of treat as certain
*  an internal representation, like a dog is out there. Right? And then you can run,
*  and then you can run inference again. Right? So you can infer what are the most likely set
*  of features given whatever the retina is showing me right now. And this internal representation,
*  this clamped state, we're treating as knowledge. We're treating as certain.
*  As the stimulus. Yeah. You're effectively treating it. You're kind of elevating it,
*  giving it the status of a retinal stimulus. Very intuitive. Right? All this, you know,
*  this probabilistic stuff that gives you a framework for making that intuitive idea
*  formal and then producing predictions about, right? So now, so if you equate, or you, let's say,
*  you analogize the, these internal states that the generative model describes with brain activity,
*  you can easily, I mean, in a fairly straightforward way, get a prediction of what is going to happen
*  in the brain when this high level state is, or is not plant. And then you can also play games
*  where you can kind of manipulate the coherence between what is being seen at the retina and
*  what is being clamped internally. So mental imagery in our model, mental imagery is what
*  happens when the retina becomes uninformative. So it remains fixed and it's simplest if you just
*  treat it as a blank screen while the clamp states vary. So you're varying your mental image,
*  but the screen is staying fixed. So all pixel values have the same value or it's like
*  a field of noise or something? Right now, so that I think the important thing is that the stimulus
*  remain fixed while the mental image is very. So it's uninformative either way. Sorry, it's a
*  technical. Yeah, yeah, yeah. But mathematically and experimentally, your life is made easier
*  if you just treat them as being turned off. I see. Yeah. There's a bias term that you don't
*  have to carry around anymore. Which makes sense. Yeah, yeah. Right. So then the question is,
*  what happens when you're driving the brain from above instead of below? I mean, that's the
*  simplest way to put it. And I mean, there's some really basic properties of vision coming into play.
*  So one of the things we know develops in the feature spaces that the visual cortex represents
*  across this hierarchy is invariance. In order for some cluster of cells to be able to identify an
*  object, whatever and however it's presented, it has to be invariant to a lot of its details.
*  Mm-hmm. So if that now is your source, if that neuron is kind of your source,
*  those cluster of neurons are your source of input for this imagery process, okay? And you tell a
*  subject, imagine a cat over here, imagine a cat over there, imagine a cat that's gray and it's blue.
*  Those neurons might not, their activity might not very much. So that lack of specificity is somehow,
*  I mean, it makes sense that you might expect it is going to be sort of propagated back down
*  the visual cortex and homogenize the activity, right? And you're going to get a loss of specificity
*  and it's going to make lower level visual areas look, during imagery, look a lot like higher level
*  visual areas do during vision. So these are all intuitive. You can implement them using the kind
*  of the framework of generative modeling. You get specific predictions and it's, it pans out,
*  I mean, at least in our experience, right? You see in terms of the features, the selectivity that
*  we've looked at, which is very simple, just spatial frequency tuning during scene for scene
*  and imagined features and scene and imagined receptive fields. You know, V1 imagery, receptive
*  fields and spatial frequency to the clutches look a lot more like, like they do during vision in
*  higher level brain areas. Without the sort of bottom up stimulus driving activity. Yes.
*  So is mental imagery then, back to the predictive coding aspect of it, is it a form of predictive
*  coding? Is it separate? Yeah. What I am saying and thinking is it's inference.
*  Yeah. So vision is inference. Mental imagery is inference. In a formal sense, the only thing
*  different is the conditioning set. During vision, you condition on stimuli. During mental imagery,
*  you condition on stimulus in some clamped internal state. In both cases, you know, if you want to
*  conceive of inference as being implemented by a network with feed forward and feedback connections,
*  this, you know, the activity is flowing along those same connections being integrated
*  at every point by the same rules. Now that's where you start, maybe you want to start thinking about
*  predictive coding, predictive coding. My understanding of it, at least is it's a way of implementing
*  inference in a network. If you go back and look at the Rowan Ballard paper that to my knowledge,
*  introduced at least the term and really it's very influential, I think, in terms of getting
*  people to think about predictive coding. You know, it's formulated as the same kind of model that
*  we're using right now to make our predictions about mental imagery. It's a latent Gaussian model. It's
*  a stack of Gaussian variables. Now how you run inference with that generative model, I think,
*  determines whether or not you have predictive coding on your hands.
*  Okay, so the way they did it is to take gradients with respect to state.
*  So they kind of cast this, the inference problem is one of finding equilibrium in a dynamical system.
*  That's, I think, it's a perfectly valid and fruitful and formative way to think about it.
*  The something that's associated with predictive coding is a very kind of specific assumption about
*  propagation of prediction errors, prediction errors being propagated forward, predictions
*  being propagated back. You can set up a neural network that implements things in that way,
*  that implements inference in that way. I don't think it's essential though, so I would see that
*  inference, probabilistic inference, as an umbrella and predictive coding as particularly intuitive
*  kind of point underneath that umbrella of operations. So is this like a, I mean, is this a
*  principle, this imagery type inference, is this a principle that extends to all cognition or just
*  perception? We're pursuing that idea. Okay, so what we presented at CCN last just a few months ago
*  was some modeling work suggesting that you can account for a number of phenomena you see in the
*  attention literature using the same idea, the idea of clamping and inference, conditional inference.
*  So in this approach, what distinguishes imagery from attention is that during attention, you
*  actually turn the stimulus back on and then you get this rich set of, and the stimulus does vary
*  and the clamp state can vary as well, and you get this rich set of interactions that can drive
*  spatial frequency tuning functions and receptive fields all over the place. You can see really
*  dramatic changes in the way that the intermediate areas are representing stimuli depending on how
*  you kind of tune the representation in the clamp layer and its relationship to the stimulus.
*  So I think there's some generality there and that actually segues nicely into the
*  the natural scenes project. For my grand designs, so if any of this stuff is true,
*  it should be able to scale, or whatever is true about it should be able to scale.
*  So what does that mean? So that means that, so in order to account for mental imagery,
*  I'm making really pretty strong assumptions about what the visual cortex can do.
*  You know, I'm ascribing operations to it to account for mental imagery and if any of that is true,
*  then I should be able to, it should give me a more accurate predictive model of brain activity
*  in any state, including just kind of passive vision.
*  So my idea is, or my aspiration rather, is to enter a stage where we can test hypotheses about
*  network architecture, and again I'm not taking credit for this idea, a lot of other people
*  thinking along these lines, by inferring network architectures directly from brain activity.
*  So to do this, you decided to spend seven years collecting a ton of brain activity.
*  Not seven years, fortunately. Kendrick is among his many, many complimentary things I could say
*  about him. He's lightning fast and the really talented postdoc, Emily Allen, and grad student,
*  Yihong Wu. They have put together a data acquisition effort that is truly heroic.
*  We talked about it a little bit when he was on.
*  I think he was just getting started when you guys talked.
*  He was already, it seemed a little overwhelmed, but yeah.
*  They did it. So we just completed acquisition on the core part of the experiment.
*  Congrats.
*  Yeah, just a few weeks ago. What they were able to do is, so the kind of, the stats are,
*  it's eight subjects, 10,000 images seen by each subject three times each.
*  These are naturalistic images, like the one that's on your website.
*  Yeah, they're photographs. They're pulled from a computer vision, from a database of images
*  that the computer vision people put together. It's called Coco.
*  The reason we chose it is because it's richly annotated. It also kind of narrows the visual
*  world a little bit to hopefully make things a little bit more manageable. So there are certain
*  kinds of objects that show up over and over again in a variety of different locations. So it allows
*  you to explore, hopefully, we're hoping issues of object recognition and invariance at the sacrifice
*  of a little bit of breadth. Some kinds of objects only show up once in this massive
*  barrage of stimulation. There are cognitive tasks associated with it, but the idea is now you can
*  take a bunch of data, enough data that you can kind of put it into the machine learning pipeline
*  and start trying to test hypotheses about, this is what I'm interested in, about how the whole
*  system, the whole visual system and all of its parts relate to one another and cast those hypotheses
*  as I think the most likely candidate right now is a kind of neural network. And the space of
*  architectures and nonlinearities you could explore is vast, but I think we have the data to do it now.
*  So you're going to be using your encoding model's approach throughout all the layers of the visual
*  system? That's what we're doing right now. So now though you have enough data where you can do
*  two things at once. You can learn the feature map. So you can learn the nonlinear map from stimulus
*  to feature space. You can learn multiple sets of features that are compatible for different brain
*  areas and simultaneously learn the coupling, which is the encoding model between those features
*  and brain activity. And you can do it all at once. And it's working. Yeah, I mean, it's great. Yeah,
*  beautifully accurate predictions. What we learn from all of this is, you know, that's just a
*  starting point. That's like, it's just kind of showing we can do the thing with the data that we
*  hoped we could do once we had it. Now we're starting to dig in and consider interestingly
*  different approaches to predicting brain activity, where the difference lies in network architecture.
*  At least that's what we're focusing on right now. So at the very beginning,
*  toward the very beginning, we talked about how when you have this idea and then you can kind of
*  just immediately see the future, the consequences where it's headed, like the endpoint,
*  where is that? What is that endpoint and how many years? I mean, I know another feature of this is
*  it always changes as you make progress. Of course. Yeah. Yeah. Yeah. So I'll give you
*  my vision for this sort of far enough ahead that it's not, you know, just sort of blurred,
*  blurred out into just pure visual thinking. From your mental imagery, your early visual
*  cortices right now have a very blurry image. Yeah. So, you know, as I briefly mentioned,
*  there are cognitive tasks associated with this acquisition. So it's not just passive
*  observation of the stimuli. It's actually a really demanding long-term memory task because people,
*  the subjects had to indicate for every single image that they saw if they'd ever seen it before.
*  And some of them hadn't been seen in, wait, I just paused because subjects can't know this.
*  But we're done with collections. So I'm going to move on. Okay. So, you know, some of the images
*  subjects have not seen for a year. Whoa. Yeah. And they're better at it than you might have expected.
*  There's, you know, months long above chance memory going on. So right there,
*  you know, hunting for signals, memory signals, understanding how they're integrated
*  into the visual processing and then right out into this finger, this button push.
*  To me, a model, right? So the models that we're using to predict visual brain activity right now,
*  many of them are not, they don't handle this kind of processing. This kind of memory-based
*  recognition processing that's occurring in parallel with all the other visual operations
*  like object recognition that go on when you just show someone a natural scene. I think a
*  realistic intermediate term goal is an architecture that explains both the seeing and the remembering
*  at the same time. That's a really exciting possibility. I think that
*  going after that, that goal will push the field in interesting directions.
*  Maybe with that, if you have just a couple more minutes, I could ask you some, again,
*  real broad questions. Yeah. So this, by the way, this is really exciting work and I really
*  appreciate you explaining a lot of it to me and my audience here. So, yeah, it's fun. So,
*  does AI need neuroscience? Yeah. Yeah. I mean, I said that earlier. It's definitely,
*  you know, a lot of people, myself included, think of neuroscience and AI as, you know,
*  they're in this kind of virtuous cycle where the neuroscientists reveal principles of brain
*  function that are operationalized by AI. They show how these ideas can be refined and scaled,
*  which we then bring back to the brain and test them against behavior and brain activity.
*  It's possible, right, like the, you know, if you think that the loop is going to kind of take us
*  the amount of time before AI kind of loops back around to needing AI,
*  it feels like it's going on a little bit longer. To needing neuroscience. Yeah. Sorry. I'm sorry.
*  Yeah. AI needing neuroscience, right? So I don't know when it's going to boomerang back.
*  And this is obviously a simplistic model because there's cyclical work happening in multiple
*  labs right now as we speak. And, you know, I'm sure the next person you interview will give you a
*  nice example of that. Yeah. But there is a sense, my sense is that the AI is going to go a long
*  distance before it runs into the kind of dead end that they need neuroscientists to rescue them from.
*  The plateau that you mentioned before, you mean? Or because a lot of people think that the plateau
*  is coming sooner rather than later with like the limits of deep learning are nigh. Yeah, I guess.
*  Yeah. I mean, my, but whatever, everything is always 10 years away. I don't know.
*  Yeah, that's true. Maybe sooner than that. But I mean, AI is having a moment. Yes,
*  AI needs neuroscience. I think to paraphrase something David Susselow said at CCN,
*  AI is killing it right now. That's just a fact. So that's something we should celebrate.
*  But he said it in the spirit of yes, AI is killing it. Get over it and keep moving forward because
*  it'll what you're doing is important. I agree. I agree with that. I absolutely agree with that.
*  And the worst thing in the world would be for neuroscientists is to sort of sit back and
*  read popular science accounts of how these AI systems are working. I just, I feel like we just,
*  we're focusing on kind of targeted questions. Yeah. Right. But we have in our hands
*  the end point, right? We're daily interrogating the thing that AI is trying to build toward. And
*  that will never not be relevant. I mean, not only from a conceptual intellectual point of view,
*  but also obviously from a mental health point of view, right? It doesn't matter. You know,
*  you could have, you can have an AI system that drives your car for you.
*  Questions still going to remain. You know, someone has just gone through trauma. They can't
*  cope with their normal life. What do we do? Yeah. You can never get too far away from the brain,
*  away from people. If those kinds of questions are driving you and they have to be driving you.
*  One of the worries though, and I faced this in my own little career and I saw it a lot too,
*  is that you go in with this sort of big question, right? You're going to figure out consciousness
*  or whatever. And then you realize you don't know. And then you start studying a smaller piece of it,
*  but then you start getting like, oh, okay. Into the sort of learning the technical sides of things.
*  And that becomes interesting to you. And three steps further down the road. And all of a sudden,
*  you're just a technician working on the nuances of electrode impedance, right? And it's like the
*  most fascinating thing. So I can see this being a problem with neuroscientists becoming interested
*  in AI. And then the AI itself is the thing that becomes interesting because it's easy to make
*  progress on. So how does that happen? That's happening to grad students nonstop. And, you know,
*  at dinners, at conferences with other neuroscientists who are running labs and graduate
*  programs, it's kind of, it's being noticed that that transition from, you know, the kind of
*  enthusiasm that inspires people to understand, to want to study neuroscience to begin with,
*  to kind of full scale conversion into, you know, enthusiasm for the technical side of AI. It's fun.
*  I mean, it's, you know, building systems and AI has developed a set of building blocks and you can,
*  it's like the exact fun you get with Tinker Toys or Legos. You can snap them together to make really
*  cool new things and they kind of work. They tend to work.
*  Except first you got to get your server up and running and get some of those.
*  Some people get into that too.
*  That's true. That's another, that's all these waypoints where people get.
*  I can think, I am thinking of really talented neuroscientists who got really into parallelizing
*  computation and made that job.
*  It's so tempting. And, and, but then I always have in the back of my head,
*  keep your eyes on the larger picture. And I don't know why I feel that push to,
*  to try to keep it broad because I think people are very happy when they go down that technical road.
*  Yeah. I think you can make it sound a little better. At least in my mind,
*  I make it sound a little better and think of it as craft. Right? So again, the analogy,
*  the creative work to art becomes really relevant here because the same thing happens in art.
*  There's what you're trying to communicate and there's the, your mastery of the medium.
*  And that master, there's satisfaction in mastery.
*  There really is. There's satisfaction in craft and become, you know, and the way,
*  the way we passed on knowledge of craft to each other is very old school. It's very like artisanal
*  and there's something wonderfully satisfying about mastering a hard thing that you know can be done
*  and doing it super well. And it's, it's tempting to trade that in for the uncertainty that you
*  live with all the time when you're trying to figure out your little slice of the question,
*  how does the brain work?
*  So mastering uncertainty is a goal that you seem to have,
*  you seem to have accomplished. And if you're, I am addicted to the creative cycle of science
*  so that the being plunged into uncertainty and the feelings of insecurity and feeling overwhelmed
*  and futility that come. But as we said, you know, you, you, you, you take your beautiful new idea
*  and you test it against an experiment or even just write it down in a grant.
*  To me, that is part of the engine that keeps me going. Like I, it's, it's very addictive to me.
*  All right, Thomas. Well, I know that your engine has been running here for a while with me.
*  I really appreciate it. So I mean, there's a lot more as always that we could have gotten to.
*  And maybe next time people want to learn more, they can go to nazolara's lab.net. And of course,
*  I'll link to all this stuff in the show notes and there are specific papers that we sort of
*  glossed over, but good luck, man. I really appreciate your time. Thanks. It's been really
*  fun talking to you. This is cool. Brain inspired is a production of me and you. You can support the
*  show through Patreon for a microscopic two or $4 per month. Go to braininspired.co and find the
*  red Patreon button there. Your contribution will help sustain and improve the show and prohibit
*  any annoying advertisements like you hear on other shows. To get in touch with me, email paul
*  at braininspired.co. The music you hear is by the new year. Find them at the new year.net.
*  Thanks for your support. See you next time.
