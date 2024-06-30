---
Date Generated: June 30, 2024
Transcription Model: whisper medium 20231117
Length: 5239s
Video Keywords: []
Video Views: 81
Video Rating: None
Video Description: Show notes: 
https://braininspired.co/podcast/189/

Patreon for full episodes and Discord community: 
https://www.patreon.com/braininspired

Video Series: Open Questions in AI and Neuroscience:
https://braininspired.co/open/

Apple podcasts: 
https://itunes.apple.com/us/podcast/brain-inspired/id1428880766?mt=2
Spotify: 
https://open.spotify.com/show/2UZj8c8Ap5oc2gh2rJxLLe

Music by: The New Year: 
http://www.thenewyear.net/

Joshua Vogelstein runs the Neurodata Lab at Johns Hopkins, which seeks to "Understand and improve animal and machine learning worldwide."
Today our discussion revolves around two main themes, along with my usual random tangents
Jovo, as you'll learn, is theoretically oriented, and enjoys the formalism of mathematics to approach questions that begin with a sense of wonder. So after I learn more about his overall approach, the first topic we discuss is the world's currently largest map of an entire brain... the connectome of an insect, the fruit fly. We talk about his role in this collaborative effort, what the heck a connectome is, why it's useful and what to do with it, and so on.
The second main topic we discuss is his theoretical work on what his team has called prospective learning. Prospective learning differs in a fundamental way from the vast majority of AI these days, which they call retrospective learning. So we discuss what prospective learning is, and how it may improve AI moving forward.
At some point there's a little audio/video sync issues crop up, so we switched to another recording method and fixed it... so just hang tight if you're viewing the podcast... it'l get better soon.

0:00 - Intro
05:25 - Jovo's approach
13:10 - Connectome of a fruit fly
26:39 - What to do with a connectome
37:04 - How important is a connectome?
51:48 - Prospective learning
1:15:20 - Efficiency
1:17:38 - AI doomerism
---

# BI 189 Joshua Vogelstein: Connectomes and Prospective Learning
**Brain Inspired:** [June 29, 2024](https://www.youtube.com/watch?v=V_UkhWeP49w)
*  And I'm betting you it would get us to a place where people could achieve levels of consciousness
*  or mindfulness or meditation that is unheard of currently.
*  The normal kinds of statistical analyses and machine learning tools that one could apply
*  to data, none of the theory applies when you have it as a network.
*  My somewhat obnoxious prediction is that basically everything will be using principles of perspective
*  learning, all the AI, all the modeling of humans and stuff, will all be doing it relatively
*  soon.
*  Hey, I'm Paul.
*  This is Burn Inspired.
*  Do I look sleep deprived?
*  Because I am.
*  And I'm on a little vacation to my former home, Durango, Colorado.
*  But BI must carry on.
*  So here I am.
*  And my guest is Joshua Vogelstein.
*  Jovo, which is what Joshua goes by, runs the NeuroData Lab at Johns Hopkins University,
*  which seeks to understand and improve animal and machine learning worldwide.
*  That's the tagline of this lab.
*  Today our discussion revolves around two main themes, along with my usual random tangents.
*  So Jovo, as you'll learn, is theoretically oriented and enjoys the formalism of mathematics
*  to approach questions that begin with a sense of wonder.
*  So after I learn more about his overall approach, the first topic that we discuss will be the
*  world's currently largest map of an entire brain, the connectome of an insect, the fruit
*  fly.
*  And we talk about his role in that large collaborative project, what the heck a connectome is, why
*  it's useful and what to do with it, and so on.
*  The second main topic that we discuss is his theoretical work on what his team has called
*  prospective learning.
*  Prospective learning differs in a fundamental way from the vast majority of the rest of
*  AI these days, which they call retrospective learning.
*  So we discuss what prospective learning is and how it may improve AI moving forward.
*  At some point, there's little audio video sync issue that crops up.
*  So we had to switch to another recording method and fixed it.
*  So just hang tight.
*  If you're actually viewing the podcast, it'll get better soon.
*  Show notes are at braininspired.co slash podcast slash 189.
*  If you want to experience this full episode and all other full episodes, you can support
*  Brain Inspired on Patreon.
*  Go to braininspired.co to learn how.
*  All right, take two.
*  Here we go.
*  That'll make sense in a second.
*  Jovo, how's the family?
*  How's the kids?
*  How's your shoulder?
*  Just kidding about the shoulder.
*  We didn't get that personal last time.
*  Good to see you again.
*  Thanks.
*  Yeah, I feel great.
*  Family, kids are all great.
*  We had a beautiful weekend with family, events.
*  We're all together and so it's really nice.
*  Where's the cell phone right now?
*  Cell phone is very close now because no kids are home.
*  When they get home, the cell phone will adjourn to the car until they go to sleep.
*  You attach it to a drone?
*  Adjourned.
*  No, I know.
*  Oh, see, my kids are going to walk in the door in a minute now and so I'm going to have
*  to close this door behind me.
*  I was imagining your kids would be home soon as well.
*  No, they're going to martial arts and they'll be home at once.
*  As usual, beautiful setting behind you.
*  I'm jealous of your space.
*  The reason why I said all that at the beginning is because this is take two of our episode.
*  We tried this a few weeks ago.
*  It must have been a few weeks ago, a month ago.
*  Then we had a little post-mortem after and I told you, man, I was really off my game.
*  We went back and forth and mutually agreed to re-record it.
*  This is the first time I'm actually re-recording an episode that I hadn't screwed up the recording
*  on before.
*  So, congratulations.
*  Thank you.
*  Thanks for doing it again with me.
*  It's my pleasure.
*  I thoroughly enjoyed the first one.
*  I look forward to this one too.
*  Do we let on why we are recording?
*  It was basically my scatter brain.
*  Well, I'll just...
*  My part that's taking responsibility for my part, I'd say is I love the concept of a redo.
*  I first started doing redos, I think in middle school recess where we would be playing tag
*  football and someone would say they tagged me and I would say I didn't feel it and then
*  it was unresolved and so we just did a redo.
*  More recently in life, I decided I love that concept and I want to keep it going.
*  I have redos constantly with my kids, with my wife, with myself where I'll say something
*  or do something and I just wasn't thrilled in retrospect with how I did it.
*  So, I'll ask for there to be a redo and I can explain why I want the redo and we do
*  it again.
*  I love the practice and so this is just another manifestation of me doing a redo.
*  Well, what's the phrase?
*  Third time's a charm?
*  I hope we make second time the charm this time, right?
*  I hope each time is charming.
*  Okay, so this time, and I'm not going to refer back to our previous conversation this whole
*  time, but what I thought that we would start with is sort of your overall approach because
*  I don't think, I think I neglected to highlight that last time.
*  One of the things that strikes me at reading, especially this most recent paper that we'll
*  talk about a little bit later is how into mathematics and formalisms and the theory
*  side of things that you are and we'll get into my difficulty in reading your latest
*  paper later, right?
*  But I wonder how you see, so you're interested in neuroscience and artificial intelligence
*  and I wonder how you see yourself navigating between them, among them, in your thinking,
*  in your working, in your excitement and enjoyment.
*  I love that question.
*  I guess the thing that most motivates me any given day is trying to understand us.
*  And by us, I mean something that can be quite general.
*  Sometimes I literally mean just me, what is happening inside of my body and my thinking
*  right now.
*  I don't know the answer in general, but I really like thinking about what is happening
*  inside of us.
*  How are we thinking and how do we get to have these thoughts, these feelings, these emotions,
*  these beliefs?
*  And so in exploring that, what I've come to decide is that the language of mathematics
*  and statistics and more recently data science and artificial intelligence is the language
*  that I think is best equipped today to characterize the kinds of things that we are doing, which
*  as far as I can tell is making a bunch of decisions with a bunch of uncertainty in an
*  environment that we're navigating with a bunch of other agents that seem to be doing
*  approximately the same thing.
*  So then, I mean, your work also, you know, you straddle artificial intelligence.
*  You've done a lot of work in artificial intelligence.
*  You've done a lot of work in neuroscience.
*  But you didn't answer my first question and I asked like seven, which is, you know, how
*  do you see yourself like navigating those two fields in particular?
*  So what I'd like to think that we're doing in our group is pushing artificial intelligence
*  in the direction of being able to more formally and accurately characterize the kinds of things
*  that thinking and learning beings are doing.
*  Okay.
*  One of the things that I wanted to ask you is it seems, and you can correct me, in artificial
*  intelligence and machine learning and in neuroscience that a lot of progress is made by tinkering,
*  right?
*  And kind of making a guess and trying out a new algorithm, seeing how it works and then
*  sort of post-hoc going in and thinking about why it might work.
*  And then, you know, you ratchet it up.
*  And you know, in all of these fields and all the scientific fields, there's this virtuous
*  cycle that we're supposed to do where we start with either experiment or model or theory.
*  And then we just go round and round.
*  And that's how we progress in science.
*  So you know, but you seem like you're a theory slash formalism first approach kind of person.
*  So do you approach problems in general with starting with a theory and trying to build
*  out a theoretical notion?
*  I think I start with wonder.
*  I start with like, how is that happening?
*  Like how did that squirrel figure out where that nut was going to be?
*  Or I don't know if you watched that squirrel ninja warrior course thing online, that little
*  YouTube video, but like how did they figure it out?
*  Or you know-
*  Oh, I did.
*  Yeah, yeah.
*  I know what you're talking about.
*  Or I have a two-year-old son and he'll say something to me like freezing.
*  How did he learn that word freezing?
*  It's not like I gave him a thousand examples of freezing and temperatures and he like somehow
*  over some supervised learning algorithm figured it out.
*  He just today he knows that word.
*  Like how did that happen?
*  How does he know how to jump now?
*  Like I didn't teach him.
*  He just jumps all of a sudden, walks backwards.
*  Like I find all that stuff amazing and awe inspiring.
*  And I just wonder how it happens.
*  So then you don't tinker, right?
*  You go from wondering to a sort of because you have an applied mathematics background
*  partly.
*  And so does your mind just go straight to like how do I formalize this in the mathematical
*  language?
*  Yeah, I'd say it goes from wondering to trying to characterize it somewhat formally.
*  And then the tinkering is like the first time I try to write it down, it's usually nonsense.
*  Like it's not even wrong.
*  It's just like-
*  You mean like write down a formal like mathematical formalisms?
*  Yeah. Yeah.
*  It's not even wrong.
*  It's just nonsense.
*  I mean, it seems right to me at the time.
*  But then I show it to someone else and they're like, like, that's nonsense.
*  So then there's tinkering and trying to figure out the right, I'd say, like conceptual
*  framework to even characterize what's happening.
*  That seems like a different kind of tinkering than, let's say, in an X.
*  Well, let's say in an AI algorithm.
*  Right. So you I think it seems like a different kind of tinkering.
*  Would you agree with that?
*  That, you know, let's add whatever, let's add attention or, you know, let's let's add a
*  convolution and see what happens or something.
*  Yeah, I'd say it's a conceptual tinkering rather than like a numerical experiment tinkering.
*  But it's not that we don't do the other kind.
*  Once we have a claim, the way we like to write our papers is there's some theoretical claim
*  that we have a theorem like this kind of thing will lead to this kind of outcome.
*  Yeah.
*  Then we write an algorithm where we can say this algorithm has the properties that will know it
*  will have whatever or get this property that we care about converges to the right answer or
*  whatever. But then making it work in practice certainly requires a bunch of tinkering.
*  And there's it's not like one directional in the sense of we say some theory thing, we come up
*  with some algorithm thing and then like we'll change the theory based on the results of the
*  algorithms often and vice versa.
*  So we're mutually tinkering on both because it's like there's a right theory or a right algorithm.
*  There's like algorithms and theories go together.
*  It's like here's the algorithm that's the manifestation of this theoretical construct that we
*  desire.
*  So I think that, you know, I don't remember.
*  I can't attribute the quote to anyone in particular.
*  I'm sure it's been attributed to Einstein.
*  But the quote is something about something like, no, it can't be Einstein because I think it's
*  mostly referring to like sort of the experimental tinkering side where advancements are.
*  I don't remember the exact quote either.
*  But the idea is advancements are made by, you know, you do an experiment and then you say, huh,
*  that's funny. You know, something unexpected.
*  Right. And and then and then you go down that avenue.
*  But is that the kind of thing that happens in the theory algorithm theory algorithm back and
*  forth?
*  Oh, yeah. So today I was talking with one of my students and she said to me,
*  the results are bad.
*  And I said, that's great.
*  That means we don't understand something and we're about to learn.
*  And the results, you know, maybe we're bad, maybe not.
*  Like, but we certainly learned a lot in the discussion.
*  And so the whenever I get like a result that's unexpected, it's exciting to me because that
*  means now there's an opportunity to learn something.
*  OK, well, so I'm not sure if tinkering is the right word, but you worked diligently for over 10
*  years figuring out statistics and what you needed to figure out to make the connectome of a
*  larval fruit fly brain, which you claim you're best known for.
*  Do you think you're best you're best known for that?
*  Certainly recently.
*  I mean, one thing that was really cool about that, that one of my say, proudest achievements to
*  date is National Geographic labeled that work as one of the top 10 top seven medical
*  breakthroughs of the year last year.
*  Medical breakthrough.
*  I don't know what their criteria was, and I'm not judging it.
*  I'm just saying I was stoked that it happened.
*  Well, you know, I didn't ask you this before.
*  What is the difference, you know, connectome wise, before we talk about that work a little bit more
*  in depth between a like a larva and an adult brain?
*  Quite a bit. So, you know, larva are basically baby flies and they're pretty small, like, you
*  know, on the order of thousands of neurons versus the adult ones of tens or hundreds of thousands of
*  neurons. And, you know, depending on the species, it can be more or less.
*  And then, like the degree to which the larva can behave and learn is differently.
*  So their cognitive repertoire is more limited.
*  Their connectome, like the set of neurons, the set of connections between the neurons is much
*  smaller. It's also still in development.
*  So the connectome of a seven day larva is different than a six day.
*  For adults, like that's probably true to a certain degree.
*  But after a certain time, like it mostly stops developing and then it's kind of a steady state,
*  people think.
*  So the so the reason why you went after a larva instead of an adult then is because of the level
*  of difficulty, perhaps.
*  We could. Yeah, just we wanted to finish something.
*  That was the thing we could finish.
*  Yeah. Well, I know that I've heard you say and you told me last time that this project began
*  largely because you wanted to figure out whether by how you could tell by looking at a connectome,
*  whether you whether a fruit fly knew calculus or could do calculus.
*  Yeah, that's right. So this was an idea I had in grad school.
*  I think it was, I don't know, 20 years ago, probably at this point, where I started taking a
*  class on statistical pattern recognition.
*  And the deal with almost all the theory and statistical pattern recognition is you start out where
*  you have P features or dimensions and then live in what's called Euclidean space, which means
*  there's really no structure to the different dimensions.
*  Each one is kind of its own independent thing.
*  And statistics and machine learning and data science largely operates on data that kind of follows
*  that model, or at least it's the prevailing model for our data.
*  However, in many real data sets, it's not really a particularly good model.
*  For example, in networks, the variables or the dimensions tend to be the edges and those are
*  between two nodes.
*  And so there's a there's a structural, like logical dependence, not a statistical dependence of like
*  which things happen, which other things, but like a different kind of dependence where this edge
*  happens to demand the existence of this node and this node.
*  I see.
*  And there's no such thing in Euclidean in the normal way that people do statistics and machine
*  learning. And so the implications of that is the normal kinds of statistical analyses and machine
*  learning tools that one could apply to data.
*  None of the theory applies when you have it as a network.
*  And so we spent about a decade tinkering with the theory to like pivot it little by little over to
*  being able to characterize big, complicated networks.
*  But so when you when you started off this project, when you conceived of it, not that you predicted,
*  oh, this is going to take me six weekends to finish and then it takes a little over 10 years.
*  Did you have a sense of how long it might take and relative to how long it ended up taking?
*  Yeah, it was pretty clear from the outset that it was going to take like a decade.
*  It was a lot of work.
*  Like the theory of statistical pattern recognition is all grounded in this one set of assumptions or
*  axioms about the space of the data, which is Euclidean.
*  And we wanted to pivot it to a different and frankly more complicated setting that we thought is
*  more accurate to describe the data.
*  But there's 100 years of work on the first bit and approximately zero work on the second bit.
*  So, you know, less than 100 was a good guess, but sometime for sure.
*  I just realized we didn't define connectome.
*  Can you define connectome for me?
*  Yeah, you know, it's funny.
*  There's a bunch of people publish things and they define connectome in the way that so they can
*  publish and like use the word.
*  But usually what people mean is we're talking about a brain and there's a set of nodes.
*  This could be neurons, but sometimes there are regions of brain and then there's connections among
*  them. And so those could be synapses or tracks if you're talking about regions of brains.
*  And so the connectome is a complete set of nodes that define however you want and edges to find
*  however you want. But it's a complete set at that particular spatial temporal resolution.
*  And you can have functional connectomes as well.
*  Well, people certainly use that word a lot.
*  It's to me, it's very unclear what it really means in the sense of now it kind of depends on there
*  being some statistical model underlying the dynamics of the activity and which model you mean is
*  like a whole nother thing to condition on.
*  So if you just say connectome, you have to define what constitutes a node and what constitutes an
*  edge. And in theory, the edges are measurable.
*  Like you can look into the brain and it's an anatomical thing.
*  Once you go to functional connectome, there's no thing to look at that's an edge.
*  Now it's a quantity that's abstracted and must be estimated from time series data.
*  Yeah. And so I see why one would say it and I've said it and I have a bunch of papers on it, but
*  it's I would kind of prefer the whole world just use correlation matrix instead if that's what they
*  were talking about.
*  OK. So but what we're talking about here with the fly connectome is the fly connectome is the first
*  insect where we have every single neuron much and every single connection between them pretty much.
*  I say pretty much because the imaging like the actual experiment of taking the images is
*  complicated and difficult.
*  The process of stitching all the images together is complicated and difficult.
*  The process of identifying all the cells and their processes and the synapses is again complicated
*  and difficult. And like there's errors in every step.
*  And this is the largest connectome we have.
*  Yeah. This is the largest connectome.
*  Certainly we had at the time maybe someone has completed an adult Drosophila connectome at this point,
*  but we don't have it publicly available if they have done it.
*  Yeah. OK. Because I mean the famous one is the C. elegans connectome, which is like 302 neurons.
*  Depending on whether it's the hermaphrodite or the male.
*  Right. What is the male?
*  Probably smaller.
*  I think it's too more efficient.
*  You mean I did not mean that.
*  No, no. But right.
*  So all right. So now this is publicly publicly available.
*  People can use it to do all sorts of things.
*  One of the things that you've already worked on is looking at bilateral bilateral symmetry and
*  comparing the left and right sides of the brain.
*  So what did you find there?
*  Well, I want to start by telling you why we thought we should even look at that question.
*  OK. You know, it's an interesting thing with with analyzing data is people like to think about the
*  sample size and like how many samples you have.
*  It kind of tells you what you can estimate about the data.
*  So, for example, you have one point, you can kind of guess what the mean is, but you have no idea what
*  the variance is going to be because it's only one point.
*  You have two. Now you can kind of guess the variance, but it's probably not going to be a very good
*  estimate. Now, with the connectome, we have one of them.
*  So, like, we have kind of a mean estimate.
*  It's this one. But like, what else can you really say?
*  And it took us a long time to figure out what can we say where we can really get some confidence about
*  the answer, meaning we could estimate confidence intervals or a p-value or anything like that.
*  Do you just mean what question can you even ask?
*  Yeah, what question can we even ask and have a statistically rigorous answer to?
*  And the answer was, you know, very few questions are actually particularly easily answerable with just
*  one connectome.
*  But it also turns out there's lots of ways to think about a connectome.
*  So you can think about there's one connectome or you can think about there's like thousands of neurons
*  or say tens of thousands or hundreds of thousands of connections.
*  And then you kind of realize there's some flexibility in how you do the modeling.
*  And you can say, for example, maybe the left side is a copy and the right side is a copy.
*  And now we have this internal control because we can look at how similar these two things are to each
*  other. So that's really why we looked at bilateral symmetry, because we had an internal control built
*  into the data.
*  So then, so what did you discover?
*  Well, the first thing we discovered, and this took probably a few years, was that the data was messy.
*  But you already this is this came.
*  It wasn't this published right around the same time as the official publication of the Insect Connectome.
*  Yeah. Yeah. So we really were kind of working on it in parallel.
*  And so when our collaborators, Marta and Albert and Michael, who are all in the UK, they're the ones who
*  really got all the data, did the imaging, lots of image processing and manual labor, you know, really
*  the vast majority of the work in 10 years and getting all the funding to do that.
*  When they first gave us their estimate of the connectome, we looked at it and we're like, no, that's not
*  right. And they're like, what do you mean?
*  And so we'll say things like, well, the brain is a connected network.
*  We know you can go, you can traverse from any neuron in the brain.
*  You can follow a path of connections to get to any other neuron in the brain.
*  And the first network they gave us didn't have that property.
*  There was like a whole big network over here and then a bunch of disconnected ones over here.
*  And so we're like, that's wrong.
*  And they're like, oh, OK.
*  So then they go back and they like figure out all the edges that they missed and they give it to us again.
*  And we're like, nah, still wrong.
*  And they're like, how do you know?
*  Well, and it's like, well, this neuron and this neuron on the left and the right side of the brain are really
*  the same neuron, like they have the same identity, the same, say, developmental history and stuff like that,
*  more or less. They should look very similar to each other.
*  But this one, which you've labeled A on the left, actually looks identical to what you've labeled B on the right
*  and different from what you've labeled A on the right.
*  And they're like, oh, OK. So then they go back and they're like, yeah, you're right.
*  You know, blah, blah, blah. We have to switch this one.
*  Then we have to figure out what's the real identity of this one.
*  And that process, I mean, I'm talking about it kind of lackadaisically, but required
*  years of work because we had to develop the algorithms to be able to check these things on, you know, hundreds or
*  thousands or tens of thousands of edges.
*  And the algorithm had to be efficient enough and we had to be able to interpret the things.
*  And there was a lot of back and forth just till we got to a connectome where like, yeah, we can study this thing.
*  So that I don't want to like just throw a wrench on our conversation already, because I mean, so did that work get
*  easier as big data got bigger and big compute got bigger?
*  I mean, when this started, there was already big data, right.
*  But, you know, I'm not I'm not sure where we are in the exponential curve, right, where we were 10 years ago versus
*  where we are now.
*  What I'd say is my experience is for every applied data set I've ever worked with, the approximately first year of
*  work is me finding flaws in the data that mean like the kind of default analysis that one would do, wouldn't we?
*  And that's been true since for 20 years.
*  It's always been about a year of basically cleaning up the data.
*  Is that because the big data precedes the right big algorithms, big compute or?
*  I think it's just because data are messy and like doesn't matter if it's big or small.
*  Like, you know, even when I was playing with like single cell data, there's like this big spike in the middle of the
*  thing. It's like, why is there a big spike there?
*  It's like, oh, I kicked the table then.
*  And I didn't, you know, mark it down or whatever.
*  It's like, well, now what do we do?
*  Like, do we think of it as two separate sections?
*  We figure out how to do an analysis that's robust to random big spikes.
*  Do we just delete that and call it NANDs?
*  Now we have to adjust our algorithm to be able to deal with NANDs.
*  Like, there's so many options, but it's a process of figuring out like there are anomalies that don't kind of fit in
*  the theoretical assumptions of what the data should look like.
*  We have to change the algorithms and or the data to address them.
*  So then going back to like what what what this connectome is useful for top 10 medical breakthroughs, right?
*  What are some of the things that people are doing with it and what are some of the things that people should be doing
*  with it?
*  Well, I think the connectome, like when we have one connectome for some species, the way I like to think of it is it's a
*  resource.
*  And so similar to the Sloan Digital Sky Survey in Cosmology or the Human Genome Project in Genomics, what it does is it
*  lets people who are interested in understanding, say, circuit mechanisms in the connectome, but other things in the
*  other branches of science, you have some idea that you think might be relevant or real or explain something and you get
*  to go check it in this resource before you go do your experiment.
*  And so think about in Cosmology, before there was sky surveys, you'd have to rent telescope time.
*  It takes about six months.
*  You hope it's not cloudy that night, because if it is, you have to wait another six months.
*  If it's not, now you can look up at the sky and try to get some data on your thing.
*  But once the Sloan Digital Sky Survey existed, the way that we did Cosmology was completely different.
*  Now you check the resource first.
*  If the resource says your hypothesis can't possibly be right because of whatever, you don't ever do that experiment.
*  You don't look in the sky at that time.
*  You keep thinking and come up with a better experimental design that fits within the constraints of what we know is even
*  possible.
*  And so the connectome really is a constraining mechanism.
*  It says, you have some idea about how the circuit works?
*  Well, if it's not in this connectome, it can't be right.
*  Now, obviously there's caveats to that.
*  It could be right in a different fly or whatever.
*  But like in general, it constrains theories so that the experiments that we do are checking for things that could possibly be right.
*  And that's how people are actively using the Drosophila connectome today is investigating all sorts of circuits that they had
*  multiple ideas, competing ideas for what was the explanation.
*  And now they have this thing they can use as a reference and they can make their experimental design more efficient and more precise.
*  So you could potentially think about how some area or some circuit computes flying.
*  Flying, let's say, right.
*  And then and then you would use the model as a resource to potentially design your own model, use the connectome as a resource to
*  potentially design your own model and constrain what your model should look like.
*  You should be able to implement quote unquote flying in a model based on the connectome data.
*  Is that?
*  Yeah, exactly.
*  So right.
*  If you're a model, you thought like this part of the brain connected to this part of the brain in your model and you go to the connectome,
*  you're like, oh, that's not there.
*  OK, that model is wrong.
*  You don't ever have to do the experiment or like collect a whole nother connectome.
*  It's just there's a whole brain regions are not connected in this one fly.
*  It's like unlikely to be the mechanism that explains flight in flies.
*  Right. Right.
*  Is there something that you don't have time to do to do that you would suggest others do that?
*  I mean, you know, I'm asking like a terrible question because maybe you want to tackle the thing that you want to tackle.
*  Right. But is there a question that you think should be being worked on that isn't?
*  Oh, I don't know.
*  Like, I'm most excited about learning.
*  For me, inference, like just being able to guess the right thing, so to speak, basically calculators do that just fine.
*  And it's not interesting to me.
*  Now, I understand explaining behavior is interesting to lots of people.
*  And I'm not saying it's not interesting in general.
*  I'm just saying what I want to discover and learn about is how learning happens rather than how the inference happens after it's learned.
*  And so with respect to the Drosophila, they actually do and can learn a whole bunch of different things.
*  And so what I'm most interested in thinking about is how to understand how Drosophila connectomes change or, say, develop such that they learn some things and not other things.
*  So then you would need a handful of connectomes at larval stage one, a handful of connectomes at larval stage.
*  I don't know how many larval stages there are up to adult.
*  Right. And see how they change.
*  That would be one way of doing it.
*  The way I've been thinking about doing it is if we can train one hemisphere and not the other, then we have an internal control.
*  Or if we can just select a fly that happens to be good at doing something with its left side of its brain and bad with the right side of its brain.
*  So we don't even have to train it.
*  We just find one that through luck or genetics or development or whatever, happens to have this internal control built in where the left side of its connectome gets it and the right side doesn't.
*  But then, I mean, my first thought was like, well, you could just breed and select.
*  Right. But then it's more innate.
*  Then there's the line between innate and learned is blurred.
*  So I guess you'd want to select for flies that you could teach that that don't come with it prepackaged, but that you could teach something to.
*  Yeah. I mean, you know, this word learn is kind of funny.
*  In machine learning, branches of machine learning have done a pretty good job formally describing what learning constitutes.
*  However, I would say in Iris Van Rooge really made this super clear to me in conversations with her that like, that's not what we're doing.
*  Like, that's a formalism that has lots of nice properties and some very similar properties to what we're doing.
*  And it's not it.
*  Yeah. Okay. Yeah, because I was going to ask, like, how many more connectomes are on the way?
*  Oh, probably a lot.
*  I mean, fly, right?
*  Like to, you know, just just sticking in the fly.
*  Well, there's an adult fly, presumably coming very soon.
*  And then, like a lot of the bottleneck in the research is developing the technology to be able to do things at scale.
*  And so we kind of suspect it will be a similar thing like a human genome project.
*  Like, the first one took about a billion dollars in like a decade.
*  But now it's like a thousand dollars in like, I don't know, maybe a week.
*  So we've and it's only been a couple of decades since the first one.
*  So we suspect technology development to follow a similar trajectory.
*  Yeah, that makes sense.
*  So so the connectome includes, I guess, dendrite, all the dendrite, all the dendritic synapses, right?
*  Well, it's kind of one of the like, I'd say, statistical properties.
*  Sorry.
*  It's just like, you when we get a connectome, what we actually measure is an electron microscopy image of the entire 3D brain.
*  So we get everything that one can measure at that resolution that static at that time.
*  One of the things you can derive from that is which neurons connect to which other neurons and say how many connections there are between any pair of neurons.
*  And you can say that's the connectome.
*  But you could also include, say, the volume of each synapse, the location of each synapse, how many neuro vesicular, whatever, anything you want.
*  It's all in there. Right.
*  So there's no one that can stop you from calling that the connectome.
*  And sometimes people do mean all that other stuff.
*  And yeah, whether you need all that other stuff to explain any particular cognitive phenomenon is totally unknown.
*  So a given connectome is frozen in time.
*  And what we know is that the brain, you know, dendritic spines are just turning over all the time.
*  Our brain structure is constantly in flux.
*  Is that built into like those statistical properties built into the connectome or is it is it simply sorry about my ignorance here?
*  Is it is it simply a structure?
*  It is a structure, but what I would say is it's not that obvious how much in flux the anatomy of our brain is once we're adults.
*  And there's certainly a deterioration and we're always losing brain cells and synapses, especially if we're drinking or like getting punched in the head a lot.
*  But other than that, it's really not clear, first of all, how much change there is.
*  So there's there's lots of changing.
*  But whether the actual strength between a pair of neurons changes a lot over time, no one knows because no one measures it in brains because it's real hard.
*  It's certainly possible that the changes are such that homeostatic equilibrium is preserved, meaning that the connection strength between any pair of neurons is static, despite the fact that where the synapses are has changed.
*  But again, that's a thought experiment.
*  And I thought you wouldn't because I was going to ask you, would it matter if people did measure in the brain is constantly in flux in terms of new connections being formed and it's not it doesn't preserve the homeostatic average connective strength between neurons?
*  Right. Would that matter?
*  I was going to ask you that. And I thought, oh, he's not going to like that question.
*  No, I love that question.
*  I don't know. No one knows.
*  Like no one has any clue.
*  Presumably it will matter for certain things and not matter for other things.
*  And like then the fight is, will people be like, it does matter?
*  It doesn't matter. But like matter for what?
*  It matters for like Twitter bickering, I think.
*  Twitter bickering. But I my experience of when I Twitter bicker, I tend to Twitter bicker with people who I really profoundly respect in their knowledge and intellect about this particular topic.
*  Our Twitter bickers are almost always resolved by a phone call.
*  And it's like, well, what did you mean when you said this?
*  And they're like, I meant this.
*  And I'm like, oh, I agree with that.
*  Right. Is Twitter bicker an actual phrase?
*  Because I just said it and it sounds good.
*  But if I start seeing it a lot, I want credit for it.
*  You know, I will duly credit you.
*  If you start using a lot.
*  Yeah. OK.
*  So the last time we talked, we got I won't say heated, but we both got a little I don't know if defensive is the right word or I think I wasn't articulating my points and I wasn't maybe.
*  Understanding your points as well as I should have.
*  And I actually wanted. What's that?
*  Real time Twitter bicker.
*  Is that a thing? That's a thing.
*  I think that's what we did.
*  Oh, that's what we did. I thought you just looked up whether that was a phrase.
*  Yeah. So and what we were talking about is, you know, the difference between necessity and sufficiency.
*  And I was asking if, you know, if if structure is how important it is, which is not it was not a well-formed question.
*  And you made the point, which I agree with, that, of course, like structure is necessary to know.
*  And I referred to Eve Martyr in the past, who has made this point as well, that, you know, structure is necessary to understand function.
*  But it's not sufficient. We both agree with that.
*  And part of the reason I was getting maybe defensive or not heated.
*  I don't know what the word is emotional or something is because I what I what I wanted to ask you is it's because I wasn't articulating.
*  What I wanted to ask you is whether you have received.
*  So, you know, so so therefore, because anatomy is necessary, but not sufficient to understand function, we all agree on that.
*  Have you received like pushback that, oh, this work that you've done, it's just not important.
*  Do you feel that pushback at all?
*  Oh, yeah. So.
*  I just want to say two things.
*  First of all, I would say anatomy is required for certain kinds of explanations of function, but not others.
*  I agree.
*  And Mars levels like at the top level of computation, anatomy is totally relevant.
*  It's neither necessary nor sufficient.
*  It just doesn't show up.
*  But if you want it again, going into the Mars levels, if you want to talk about mechanism, now I think you need anatomy.
*  So I wouldn't say anatomy is always required to explain function.
*  Say for certain levels of explanation, it is required.
*  And in particular, it's required at the mechanistic level of explanation.
*  In terms of pushback, huge pushback.
*  We didn't get into this last time, so I'm glad that we're getting into it.
*  Yeah.
*  So I'll just give like a few concrete things.
*  Like, first of all, there was no real funding mechanism for connectomes.
*  So we did the research just on the back of other funding, but there weren't grants where it's like, yeah, we're going to study connectomes and they're going to NIH or NSF is going to give us money.
*  Really?
*  Did you get rejected funding?
*  Because that would surprise me, actually.
*  There just weren't solicitations for it.
*  Like we kind of did it in like, you know, the ways that you do things to get grants.
*  The other thing is, cosine.
*  So cosine is computational systems neuroscience.
*  It's one of my favorite conferences.
*  I went through years and years.
*  And when I started publishing on connectome, we started submitting abstracts of cosine on connectomes.
*  And we did this for about 10 years and every single year is rejected.
*  And every single year it was rejected.
*  And the reason was, it's really not that interesting or the analysis you did wasn't that interesting.
*  But meanwhile, they were cosine abstracts for work that we had published in Science, Nature, Cell, Nature Methods, PNAS, I don't know, name your other journal, Nature Neuroscience.
*  Every journal you could ever hope to publish anything in.
*  We had published these results.
*  And yet consistently, cosine said, it's not that interesting.
*  And so at some point, like maybe last year, after they rejected our abstract, which was a science paper and not Geo thought was the most one of the top 10 discoveries of the year.
*  I was like, hey, I hear that you're saying it's not that interesting.
*  Lots of people disagree with you.
*  Like, just FYI, lots of people disagree with you.
*  And it's clearly computational and systems neuroscience.
*  So what I said is maybe change the name of the conference to computational systems neuroscience, but not connectomes or whatever you want.
*  Just like you're allowed to not be interested in it.
*  I'm not interested in lots of stuff.
*  I just wanted more transparency in what they really are interested in.
*  And they were really receptive.
*  Like we had a nice conversations about it.
*  So I'm not being critical at all of them.
*  I just like that was a push to the side.
*  So you don't in general feel exasperated by getting a healthy amount of pushback?
*  Because I must feel somewhat exasperating to you.
*  I don't think it'd be as fun if everyone agreed.
*  OK.
*  All right.
*  So, you know, that wasn't as heat.
*  That was a little bit of a shock.
*  All right.
*  So, you know, that wasn't as heated as last time.
*  So that was nice, right?
*  That I didn't perseverate on the structure function.
*  Will we ever find out how important is it on a scale of one to ten?
*  You know, the sorts of ridiculous questions.
*  But is there is there anything else that we didn't cover about this connectome work that you think is important to mention?
*  Well, there's the connections to humans and human consciousness and intelligence and disease that we didn't.
*  Touch on yet.
*  And I do think although so far we only have a fly connectome, I'm interested in their existence of a human connectome.
*  And I do think it will be important for explaining many things about us.
*  I don't know.
*  Important on a scale of one to ten.
*  But pretty important.
*  So consciousness.
*  Yeah.
*  How is that?
*  How is a human connectome going to help us?
*  What's the word?
*  Better understand?
*  Explain?
*  Well, maybe we can start a little bit simpler and talk about how a human connectome could be impactful in supporting, say, medical research.
*  So, for example, let's talk about addiction.
*  There's many experiments we can do in mouse models of addiction where we give mice drugs or whatever and we see that they start exhibiting addictive behaviors.
*  If we could also, say, measure the connectome of a mouse after it's become addicted to something and say a bunch of clones effectively that haven't become addicted to something,
*  we could get deeper insight into the underlying mechanism of addiction at the neuroanatomical level.
*  And that could lead to more effective treatments to help people who are suffering from addictive behaviors to be able to free themselves from those behaviors
*  and live a life that is more conducive to the way they want to be.
*  And so that's like one concrete example of how I think connectome research could have real world implications for dealing with human illness or suffering.
*  But I think, I hope it's really just a start.
*  Insofar as the anatomy is involved in any degree of human suffering, I'd like to think that a deeper understanding of the anatomical underpinnings associated with any element of suffering,
*  we could divide more effective either treatments or better yet like prognostic tools and interventions before people start having these debilitating issues to prevent those outcomes.
*  Oh, like if there is degeneration of a certain area, then you could treat that area with anti-degeneration drugs or something.
*  For example, or something like psychiatric issues, often there's a long window, say of years or a decade leading up to, say, a psychotic break or something like that,
*  where if you could predict a priori, like say 10 years earlier, this person is more susceptible to that kind of thing happening in the future,
*  you could start developing therapeutics, potentially even non-invasive ones, like different kinds of therapies or meditation practices or who knows what,
*  to help pivot their connectome towards a range where they're less likely to suffer from these kinds of disorders.
*  Okay, well, so this connects also then to what you just said about consciousness, because I know that you're interested in connecting neuroscience to spirituality
*  and that you've already looked into the difference between novice meditators and expert meditators and found some differences in their brain activity or structure.
*  Their functional connectomes.
*  Functional connectomes, there you go.
*  There you go. All right. Yeah. So talk a little bit about that.
*  Yeah, so...
*  And how that connects to consciousness. Sorry to interrupt because, I mean, they're related, but they're different.
*  Yeah, so when I'm in a state of presence and mindfulness and, you know, really any cognitive state of mind that I get to,
*  presumably there's a different activity happening in my brain that corresponds to this moment.
*  And so I imagine I like get really frustrated about something and now there's some activity in my brain.
*  Now I somehow am able to calm my nervous system.
*  There's a different set of activities.
*  But if I want to transition my anatomy to be the kind of anatomy such that I tend to not lose presence or I tend to be able to regain presence more quickly,
*  like I don't see why that's not a possible set of scenarios.
*  And arguably, say meditation practice that people do for years or decades, maybe what's happening is they're actually changing their anatomy such that their brain is more easily able to transition to a state of presence or mindfulness from reactivity or something like that.
*  So I don't see any reason a priori that neuroscience research can't be extremely informative about how to essentially train ourselves to be the kinds of people that we would want to be, whatever it is.
*  Maybe you want to be more conscious or mindful.
*  Maybe you want to be more aggressive.
*  Like it could be anything.
*  I'm not making a judgment call on how we want to change our personalities, but often we do have a preference like I'd like to be more like this.
*  And so what's the underlying anatomy that would tend to make it easier to be like this?
*  Two things.
*  One, it's a shame that it takes 10 to 15 years to get to that point.
*  And presumably we get to beat that up a little bit if we had better training, better, etc.
*  But two, is it the case that, let's say, an expert meditator or whatever kind of meditation you're doing,
*  also has a different baseline conscious subjective experience?
*  So if you wanted to be more mindful, is an expert meditator more mindful over coffee than a novice meditator?
*  Does their baseline rate change because of their brain structure change?
*  Would you guess?
*  Or do you know?
*  I certainly do not know.
*  I want to address the earlier thing you said, and I want to relate it back to say like running marathons.
*  So people have been running marathons since like the times of Greeks, right?
*  That's where it started. It's been thousands of years.
*  It was only recently that people even realized that it was possible to run a marathon under three hours.
*  Before that, no one knew whether it was possible.
*  And now people are starting to ask whether it's possible for a human to run a marathon under two hours because people are getting pretty close to that.
*  And the thing that changed wasn't like thousands of years of evolution or genetics.
*  It was better training, better understanding of physiology and better training or maybe just better selection of people and more focused training.
*  But the point is like we can do really amazing things once we understand how to train our bodies into those states.
*  And so it's weird to think about meditation as like a competitive sport, but just for the moment, imagine somehow someone figured out how to make meditation a competitive sport.
*  Like yoga, like modern yoga.
*  I like the way people compete in yoga.
*  I promise you that incentive structure for humans would lead societies to come up with ways of making meditation training extremely fast and extremely efficient.
*  And I'm betting you it would get us to a place where people could achieve levels of consciousness or mindfulness or meditation that is unheard of currently.
*  But do you think if you asked an expert meditator, right?
*  So if you ask like a great writer or comedian or artist, right, they would say that there's no shortcut that you have to put in the work, right?
*  I mean, there's a certain level that you're born with or whatever and start off with and you can train really hard, but there's no like shortcut.
*  What the fuck do they know?
*  I mean, how do they know that they don't have a shortcut?
*  It doesn't mean there is no shortcut.
*  It's just like 99 out of 100 experts would say that.
*  So that's pretty like, well, you know, that's a pretty good sampling.
*  I just bullshitted that number, of course.
*  But it's a logical fallacy.
*  The fact that they don't know that there's a shortcut is not evidence that there's no shortcut.
*  All that means is they don't know of one.
*  And I agree.
*  I also don't know of one.
*  Maybe no one knows of one, but that's not actually evidence that there isn't one.
*  Yeah, I just kind of think it's a beautiful thought that there isn't one.
*  I mean, I think that they're both beautiful thoughts, but there's something appealing about having to put in the hard work that other people aren't willing to put in.
*  I promise you, just like people figured out shortcuts to running marathons faster, it's not like now it's easy to run a marathon.
*  The work won't end just because someone figures out a shortcut.
*  There would always be more levels of depth and consciousness and meditation to achieve.
*  The one in you that's afraid that we'll all achieve enlightenment and somehow that'll be bad, I think can rest assured.
*  I thought enlightenment was the end, though.
*  I thought that was it.
*  I believe that the it is the search and the journey, and I don't think there is a time where we'll get there.
*  Okay, all right.
*  Okay, well, let's move on because we have about a half an hour left, maybe, and I want to kind of take our time a little bit talking about prospective learning.
*  So this is something that you've been working on recently.
*  Is it the second draft?
*  Because it's quite different than the first draft that you sent me of the same thing because it looked like it's a is it a NeurIPS entry or?
*  So we have a white paper that we publish in a conference called COLAAS, which is a Compton Lifelong Learning Agents, I guess what it's called.
*  That was a white paper where we introduced this concept of prospective learning.
*  We didn't have any particularly compelling theoretical results.
*  We had like a couple of nice illustrations of what we were talking about.
*  We now have a preprint that we're circulating to friends where we have the first kind of theoretical results demonstrating, I think relatively clearly, that prospective learning is a coherent concept and it's different from the kinds of learning that we typically talk about in the first draft.
*  OK, yeah, so just so that to be clear, it's pro-spective learning because when I say it, I could probably slur it and it might say perspective.
*  But this is in contrast to retro-spective learning.
*  Did you guys invent the term prospective learning?
*  I don't think so.
*  I mean, people have talked about retrospective and prospective intelligence and cognition.
*  Metacognition as well.
*  Yeah.
*  For at least a decade, presumably longer.
*  I hadn't heard of anyone specifically saying learning, but when they talk about it, they've included the concept of learning.
*  So I wouldn't say that we invented the concept or the phrase.
*  What I would say is we've tried to formalize it in a particular way.
*  But it's a thing that others have said in the past.
*  OK, OK, so this is the previous, the previous concept of prospective learning.
*  The first archive paper that you sent me before was from what's termed the Future Learning Collective.
*  The title of the paper is Prospective Learning Principled Extrapolation to the Future.
*  And I think the manuscript begins with all learning is future oriented.
*  I may be misquoting, but it's something like that.
*  So where did the idea come from and why are there 700 authors on it?
*  And what's the problem that you're trying to solve?
*  So Chava Siegelman was a DARPA program manager several years ago and she created a program called Lifelong Learning Machines
*  where she brought to my attention the fact that machine learning algorithms have this issue,
*  a classical machine learning algorithm have this issue, which is if you train them to perform, say, Task A,
*  and then you train them to perform Task B, they will forget how to perform Task A.
*  And so then if you give them samples from Task A again, they just do poorly.
*  And it's called catastrophic forgetting.
*  It's not just a machine learning problem.
*  People have also noticed this in humans and non-human animals that there's ways of catastrophically interfering
*  with the learning process by introducing a new task that can interfere with the learning process.
*  So it's in general an issue with learning.
*  And in particular, AI was really failing at this kind of problem.
*  And she created this DARPA program to mitigate the issues.
*  We were on that DARPA program and we realized pretty quickly what was happening with the existing approaches
*  to try to mitigate this issue, which is you were trained in machine learning algorithm to perform well on Task A.
*  Then you would do some tricks so that it would learn how to perform well on Task B also without forgetting Task A.
*  And then whichever task you told it it was down, it now had to perform, it would do well on that task.
*  And that was, you know, that was a lot of work from a lot of people and very impressive.
*  However, it's limited in a few ways.
*  And in particular, the way that we've identified one of the limitations is that if there's a way to predict
*  what task is going to happen next, then you don't have this issue.
*  And so imagine instead of being told that you're doing Task A or Task B, it's just switching from Task A to Task B to Task A to Task B.
*  And you don't know.
*  The existing algorithm, some of which can handle the situation, what they do is they retrospectively respond.
*  So after they get a bunch of mistakes on Task B, they realize, oh, this must be Task A and therefore they switch to Task A.
*  So after a switch, they're always at least making one mistake to discover which task you're on and then they can do well.
*  And what we realized is that if the tasks are following some predictable dynamics, which isn't necessarily the case,
*  but if it is the case, then one could predict that the task is going to switch and then not have to,
*  one could then prospectively do well rather than retrospectively react to that there has been a switch.
*  And by dynamics here, the key is that you're simply adding in time into the performance of the algorithms
*  to keep track of time so that they can say, I was in Task A for 10 minutes and then I was in Task B for five,
*  and then I was in Task A for another 10.
*  And so I bet I'm going to be in Task B for another five would be the guess.
*  And if it's if it is that structured kind of series of changes, then it then it behooves.
*  Formally, it behooves the learning algorithm to keep track of that and predict that the task is about to switch.
*  That's right. And not only is it to the advantage of the learning algorithm to make that prediction,
*  we also claim it's what humans and non-human animals do often.
*  And so if you've ever conducted a physiology experiment in animals,
*  what you'll know is people never make the time of things fixed, not never, rarely make the time of trials fixed.
*  There's often like some randomness in that because if it's fixed,
*  the neurons start predicting when they're going to get a reward before they get the reward because we claim the neurons,
*  the organism, everything is prospecting in this way.
*  That machine learning algorithms currently do not do.
*  So then.
*  So was the impetus for this work then thinking about the way organisms work or was it thinking about how AI doesn't work well and how it might work better?
*  Yes.
*  Both of us.
*  Yes.
*  So that's a that's a cheat.
*  You can't cheat like that.
*  Come on.
*  We notice that the AI algorithms were suffering from this way.
*  And because we, a large number of the co-authors on this original paper have done a lot of physiology and behavioral experiments,
*  also notice that humans, animals, neurons often do it differently than it was like a natural thing to put the two things together and be like,
*  OK, what's missing from the AI formalism such that the algorithm aren't doing this thing,
*  that natural intelligence things are doing this thing?
*  So you've mentioned to me and you write about in the paper that maybe the closest thing in AI in terms of keeping track of or using time as a metric is reinforcement learning because you're you're estimating like a discounted,
*  a time discounted reward function.
*  Right.
*  And sometimes and well, you tell me because it seems to me that in this most recent version,
*  anyway, that there are versions.
*  One of the things that perspective learning does is it it predicts into infinity and sometimes it's discounted and sometimes it's not.
*  Do I have that right?
*  Yeah, it can be.
*  I mean, arguably not all problems require a temporal discounting and some of them benefit from it.
*  And sometimes it doesn't make sense without it.
*  So the deal with reinforcement learning is that it's not a time discounted thing.
*  So the deal with reinforcement learning is beautiful theory and very nice numerical experiments in certain settings.
*  For example, video games.
*  You can now use reinforcement learning algorithms to learn how to play video games to basically human level performance with essentially the same amount of training experience as humans.
*  That is a massive accomplishment from a large group of people that have been working on this for now decades.
*  Yeah.
*  However, the algorithm continue to have certain problems.
*  For example, and this is like from a paper recently, if you just like change the colors of the video game, now the algorithm does really poorly or you shift everything over by a few pixels.
*  The algorithms perform very poorly.
*  So those are problems even in the video game level.
*  When you get into the real world, the amount of training data that's required for these algorithms to work is typically so large as to mean that people don't really use reinforcement learning algorithms for the most part in deployment for real world problems.
*  Now, that's not to say that they won't or they couldn't.
*  It's just my understanding.
*  The current say discipline is not what's done.
*  Now, why is that?
*  Well, I don't know why that is, but we have a slightly different approach to dealing with time than the way reinforcement learning does.
*  And there's a few interesting differences.
*  So one is just that our framework doesn't require it doesn't have all the same machinery in particular reinforcement learning.
*  The whole problem is set up that you're making a decision that will impact what happens in the future.
*  There's many problems with times where that's just not the case.
*  Like, for example, you want to build an AI algorithm to detect whether something fell into the pool.
*  You say you have a public pool and you really don't want people falling in at night when there's no lifeguard.
*  However, the camera's performance is going to degrade over time.
*  You know that, because gunk's going to get on the lens and electronics are going to start going bad.
*  And so you really want to be able to have an AI system that's going to be adapting to changes over time,
*  even though the detection algorithm isn't impacting whether people actually go in the pool or not.
*  So that's not a reinforcement learning problem.
*  That is a problem where you really care about encoding time in the algorithm so that you know, say,
*  when you should replace the system or update the data or something like that.
*  So, but in the, let's say, like the video game example that you gave, right, where you move a few pixels
*  and then all of a sudden you can't, the RL algorithm can't perform at all.
*  I mean, there are cases where prospective learning is better suited to be implemented and worse, right?
*  So I just immediately thought, well, what would you need prospective learning for that?
*  Would that be a solution for that?
*  I think it's not clear.
*  What I would say is reinforcement learning kind of evolved out of a perspective on, say,
*  how learning should happen in basically in natural intelligence.
*  And there's really elegant theory, partially observable Markov decision processes is a formal theory
*  underneath most of the theory behind reinforcement learning.
*  And there's lots of algorithms around it.
*  But to a large part, it's distinct from 100 years of kind of a classical learning theory
*  and probably almost correct learning theory that doesn't have time at all.
*  And so one of the implications of this, like I'd say, historical accident of the different evolution
*  of learning algorithms and theories is that reinforcement learning can't easily leverage
*  a lot of the machinery that was built up in the rest of Cisco learning theory
*  because it uses different language and a different problem setting and things like that.
*  So what we tried to do is take the thing that is like the bread and butter, basically how all AI is deployed
*  in the world today, which is underlying probably approximately correct learning theory
*  where you assume there is no time, you just try to learn stuff and see, well, let's see what happens
*  if we include time.
*  And the simplest, most obvious result that we've proved now is that there's many kinds
*  of settings where classical approaches like empirical risk minimization,
*  which we know provably will converge to the best possible answer for classical learning problems,
*  we can prove will fail for problems where you need time.
*  And a simple modification to that, which we call time aware empirical risk minimization, succeeds.
*  And so the point is just if you literally include time as an input,
*  you have whatever images as the input, but also when the images was taken as another feature,
*  you just include it and you include it in a particular way,
*  then you get these really nice results where things can be changing in time and you still perform really well over time.
*  So last time that we talked, I brought up that time is inherently part of transformers, right?
*  Because of what are called positional encodings, which just says this word came at one,
*  this word came at two, this word at three, etc.
*  And you made the distinction that well, that's and I said, well, that's kind of like time, right?
*  And you said, well, it's not basically it's not absolute time.
*  It's relative time.
*  And same thing goes for recurrent neural networks, which keep track of the sequences essentially in their internal dynamics, more or less.
*  So I think I just summarized that OK.
*  But then in this latest paper, you had time to a transformer, which you hadn't told me about before.
*  So so what's going on there?
*  Yeah. So everything you said, I think is exactly right.
*  Positional encoding and transformers converts the relative position of the token or the word in a sentence.
*  If you're using transformers in language modeling to not just a number, but to a matrix actually that represents its time.
*  And that's positional encoding.
*  We changed that in our paper to be able to instead of being the relative position, the absolute time.
*  And we're not the first ones that have changed that other people have done that.
*  There's several papers on autoregressive transformers.
*  And so we're just pointing out that this notion of encoding relative time can be used as encoding exact time.
*  And our real contribution is just that if you do that empirically, then you can learn things where time is changing,
*  where empirical risk minimization such as a transformer that doesn't deal with absolute time,
*  like if it's in images, it was just like a vision transformer and things are changing in time tends to fail.
*  So presumably, I mean, I already mentioned, right.
*  And I think you mentioned that there are situations where prospective learning is optimal and there are situations where it's not necessarily optimal.
*  Are you envisioning like a an overall system that the question is, how do you know?
*  How would a system know when the statistical structure of the task switching right is is predictable enough to then turn on a prospective learning algorithm?
*  Or would you just leave it on all the all the time?
*  I mean, can it be detrimental to a system?
*  If you're implementing prospective learning, when you should be implementing, you know, whatever, I.I.D. type, what is it?
*  Probably approximately correct type learning.
*  Yeah. So for sure, time is another variable, which means if you include time, you've added variance.
*  And so if there's no signal in time, you've simply added variance and no signal.
*  So your signal to noise ratio has gotten worse.
*  So your performance will be worse.
*  I would argue for almost any real world problem, time does matter.
*  Like things are changing in time in the real world.
*  The question really isn't whether time matters, but whether it matters in a way that we can usefully predict it.
*  And so if it's changing in such a chaotic way that it's impossible to learn how it's changing with the amount of data that we get, then including time will not be useful.
*  And that's an empirical question.
*  But it's not a particularly different empirical question than like, should you use a random forest or support vector machine?
*  It's just like empirically, what works better for a particular application?
*  And I think the answer is going to be almost always you'll want to include time because certain things will be changing in a predictable fashion that we can learn.
*  And it's worth it.
*  But that remains to be seen.
*  For you and I, I think I got the grammar right there.
*  Time kind of resets every day, right?
*  Based on sunrise and sunset.
*  So we have like day like her day time.
*  We have time since the beginning of the year, time since we popped out of wombs or or bellies, you know, whatever.
*  Does time need to get reset in these kinds of models or does it go on in the past to infinity as well?
*  Is there a usefulness of having layers or levels of time?
*  Because you use the example of traffic, right?
*  Because you would you would want to know you have a sense of when there's going to be traffic.
*  But you could tell that by the sun.
*  You could tell that often.
*  And that kind of resets every day, right?
*  And if you started every day, then it would be at the same time every day.
*  Yeah.
*  So I want to say a few things.
*  First, I'm pretty sure we all came out of wombs so far.
*  Yeah, I mean, never mind.
*  Yeah, I was picturing a natural child birth type scenario as opposed to a C section.
*  Yes.
*  Cool.
*  And then in terms of traffic, it's a great example because.
*  You have to learn when traffic is relative to sunrise.
*  It's not genetically built into us.
*  And in fact, that will change depending on where you are on Earth.
*  Alaska versus Florida, there are different traffic patterns corresponding to the sun.
*  So you'll have to learn the spatial temporal dependencies of that through just experiencing the world.
*  And if you do, then you'll be better predicting when you'll arrive at a place than if you didn't learn that.
*  So it's a great example of why you should care about time.
*  But so then.
*  Do we need to have like a layered structure of keeping track of time?
*  Right. Because there are certain things that happen seasonally.
*  And I know not to go look for peaches in the winter.
*  Right.
*  Right.
*  Yeah, but you learned that.
*  Yeah, of course. But but that is a that's a different scale, a different scale of time of keeping track of time.
*  Right.
*  Yes. So I make no claim about what the right scale is or how many scales I think in general that makes sense to think about multiple time scales of learning and multiple.
*  In fact, there's an interesting thing here, which is the time scale of learning has to be like matched appropriately in a way.
*  Like if you learn slower than the things are changing.
*  Yeah, right.
*  And you can't ever learn it. So you're you're kind of if you have a learning rate, then your learning rate has to be fast enough that it's faster than the dynamics of the thing.
*  But slow enough such that you actually do learn the things and there's lots more work to explore and how to understand like the kind of optimal learning rate for certain kinds of temporal dynamics.
*  One of the things that you do in the paper is and you've mentioned this a little bit already in our conversation is compare prospective learning to other attempts at at continual learning at learning kind of toward the as things change, continual learning.
*  Lifelong learning, meta learning.
*  So there are these other approaches and going back to the usefulness of mathematical formalism.
*  One of the things I really enjoyed in this latest draft is, you know, there'll be like in bold, there'll be a section entitled comparison to lifelong learning.
*  And then you start with a sentence.
*  If we use the English language, lifelong learning and prospective learning are the same thing.
*  If we use mathematics, they are not.
*  And every I'm paraphrasing, but then every comparison section starts with starts with that.
*  So so that is the usefulness of the formalism.
*  And you and I were speaking in English.
*  So when I ask you a question, I wonder if it not gets under your skin, but if you automatically think, well, it's kind of useless to ask that question in English about time scales or something like that, because what we would need to do is just immediately formalize it and test it in theory.
*  No, I think, you know, English is great.
*  And like, it's how we can we don't want to do.
*  We don't want to you don't want to start communicating and clicks and beeps.
*  Well, I'm open to it.
*  I guess I would say like the formal language also includes spoken.
*  I mean, could be English, but any other language, too.
*  Like, you know, I think people like to pretend like the formal language is a totally separate thing.
*  But if you look at even a statement of a theorem and certainly the proof, there's like a lot of words.
*  It's not just math symbols.
*  And so there's a dance of them together.
*  And I think the formal language can really help refine and make precise the English language or the any other language that we're speaking.
*  And then today we, you and I and other people communicate using spoken language typically sometimes interlaced with some formalisms.
*  But it's really helpful to be able to explain things and understand things at the level in which we communicate.
*  Well, and you and I are also communicating with facial expressions and hand gestures and all that.
*  But that's a separate thing, even less formal.
*  So I want to move on.
*  I want to move on because I want to make sure we talk about a couple of other topics.
*  But where are we?
*  It's still new prospective learning, right?
*  Where are we in the trajectory of when you feel like you will have accomplished a certain level that where you feel like you have not made it, but where it has become useful?
*  And so, yeah, where is it now and where is it going?
*  Well, my somewhat obnoxious prediction is that basically everything will be using principles of prospective learning, all the AI, all the modeling of humans and stuff.
*  Well, it will all be doing it relatively soon.
*  That means the next five to seven years.
*  So if you do that on top of what's being trained these days, that means you're wasting way, way, way more power, right?
*  Well, I actually think a lot of the failures of AI have to do with the fact that not the moral failures or the capitalism failures, but the actual technical failures, like where they don't perform as intended by the designer.
*  Those failures often have to do with the fact that things are changing in time and the people design the system fail to integrate that awareness into the training and the model and stuff.
*  And so the most famous example of this is Google flu trends.
*  Well, I don't know if you remember this, but several years ago, Google announced they have a big new flu trend predictor.
*  And based on what people were searching for, they could predict how much flu there would be in the upcoming days or weeks or months or whatever.
*  And they made a big PR splash about it.
*  And everyone's very excited about it.
*  And then relatively soon afterwards, people realized that if you literally just use the most naive model possible, like you just predict whatever happened last time, it worked better than Google flu trend fit.
*  Wednesday, lose switch or something like that.
*  So it was kind of a big embarrassment for Google in this space.
*  But the reality is that because I would say because they didn't really address the fact that there's time, that was one of their big failure modes.
*  And so obviously predicting what's going to happen in the future is inherently about understanding time and the relationship between what's happening and the time that things happen.
*  So I really do think it will make things more efficient and better.
*  Now, I have fear around who's in charge of AI today and what more efficient AI, the implications of more efficient AI is for, say, the rest of the humans on the planet and the rest of the planet.
*  But I don't think it will lead to more consumption of resources in that in the way I think you're implying.
*  But rather, hopefully it will be more efficient algorithms because you'll be able to predict things in time with less data.
*  Maybe we can kind of mix it in in the last few minutes here because we talked a little bit about your take on AI do more do more ism last time and which is roughly that.
*  Well, what is your take on on AI?
*  So AI do more ism is that we the robots are going to kill us.
*  Yeah, eventually.
*  Right.
*  And we need to worry about it.
*  Yeah.
*  And my take on AI do more ism is that AI is a tool and it's a very powerful tool that means it will harm lots of people and help lots of people.
*  And you don't need to guess about the future.
*  We know today it is currently harming lots of people in various ways.
*  And so we can talk till we're blue in the face about who we expect it to harm in the future and whether it's all of us or just the rich people or just the poor people or whatever.
*  But the reality is it's currently having, I think, relatively profound effects on all of us because it's a powerful tool.
*  And I'm much more interested in the conversation of understanding who it's harming today.
*  And how do we feel about that?
*  What would we like to do in order to change it to make it less harmful for say the billions of people on earth that essentially have no stake in that no ability to change what it's doing but are impacted by it?
*  I mean, so one pushback that you could get on that is that sure, there are problems these days, but the robots taking over and killing all humanity would be like the worst problem because then we'd all be wiped out.
*  I mean, I'm just, you know, but but but I mean, but what you're saying is the relative weight of what we should worry about right now is right now and we should fix what we can fix right now.
*  I think I'm saying something like that.
*  What I'm saying is.
*  It depends who you are.
*  Like the worst thing to happen is it could kill me today.
*  It's killing lots of people today.
*  So it's already catastrophic for all those people that are suffering catastrophically because of it today.
*  The people who talk about A.I.
*  Doomerism are often not the people who are suffering today or people who are worrying about it or like getting funded.
*  You know, there's also lots of people talking about A.I.
*  Doomerism who are getting impacted by it today in many ways.
*  But my point is like the worst thing is very subject specific and like if everyone else dies and I'm alive, you know, it's like.
*  If I die, it's real bad for me.
*  And like I don't need to imagine everyone else also dying.
*  You know, me dying would suck.
*  But you're obnoxious.
*  So it's good for the rest of the world, you know.
*  That's to be determined, I guess, by St. Pete or whoever.
*  Right. Right.
*  So, yeah, when we talked about last time, I mentioned the book Superintelligence by Nick Bostrom and you tried to read the book.
*  You couldn't.
*  I suffered through the whole thing.
*  But I mentioned that in almost every sentence was the word maybe in extrapolating that this may happen.
*  It may happen.
*  And if you put them all together, it's like such a low probability.
*  And you made the point that, yeah, I mean, that these are all probabilities, that everything is a probability in the future.
*  And so why don't we work on what we can work on right now?
*  Yeah, I mean, I guess my perspective on that is everything maybe.
*  I don't know.
*  I'm a huge fan of epistemic humility and generally acknowledging that I literally do not know the right answer ever.
*  I'm with you, man.
*  And so then that comes down to computing probabilities and costs associated with those things.
*  And I don't know the right estimate of the costs or the probabilities.
*  So I'm not saying what one should or should not worry about.
*  My only claim is today it is clear there's lots of harm being caused by people running AI algorithms.
*  And I care.
*  I care about all those people that are suffering.
*  I care about all the non-people that are suffering.
*  And I also care about potential future people.
*  But I don't those people might not exist.
*  Like, for example, there's an asteroid that kills everything in 100 years and AI would have done in 200 years.
*  This doesn't fucking matter if AI would have done it in 200 years.
*  All of that effort was wasted.
*  Well, that asteroid may hit us.
*  Maybe.
*  Like Gaia or the Earth probably will be fine either way, whatever that means.
*  I would like ecosystems to continue because I live in them and my children live in them.
*  But I certainly don't know the right thing to happen.
*  Before I let you go, I wanted to bring up the doomerism just because you had mentioned the people running AI algorithms and efficiency and the problem with that.
*  But to bring it right back to prospective learning, a couple of quick things and I'll let you go.
*  One, do you feel like competition by getting scooped or something for other people who find the value of incorporating time and a prospective forward looking approach?
*  I don't tend to worry about being scooped, but I think I say that from a place of profound privilege.
*  My life is great. If I get scooped, my life will be great.
*  But is there competition surrounding you that you know of or however you feel about it?
*  Yeah, I would say like transformers are kind of on to this idea.
*  One could think of what we're doing, maybe part of what we're doing is trying to formalize some of the ideas that are kind of implicit in transformers and attention and stuff like that.
*  So I would say like maybe almost everyone is kind of working on this problem and we're just trying to formalize it.
*  It would be a great success would be if we can prove when transformers can solve certain kinds of time varying problems and when they can't.
*  And we haven't done that at all yet, but that would be a cool thing.
*  So I kind of think lots of people are working on this one way or the other, and I hope to contribute to that because I like it and it's fun.
*  But yeah, I think it will make progress with or without us.
*  OK, the last thing I wanted to ask about is, you know, I mentioned earlier, do you keep track forever?
*  And then I was thinking there are.
*  As you learn, let's say you're learning musical instruments, right?
*  So sometimes it behooves you if you learn piano, you're probably going to be better at trombone or something.
*  And then and then if you learn a new musical instrument, you're probably going to be even better at that.
*  And I think it's interesting that you're not always having learned piano and trombone, even that they're different tasks.
*  There's overlap, right?
*  There there. I cannot conjure it.
*  Maybe you can.
*  I know that there have been published studies and I know that there are cases where forgetting is a benefit to learning new things.
*  And I'm wondering if you've thought about forgetting in terms of prospective learning and the value that it might be it might bring when appropriate.
*  So forgetting can serve two purposes.
*  One, if you have a finite memory, then you'll want to forget stuff that's not that useful in the future.
*  Otherwise, you'll forget the stuff that is useful in the future and that would sell.
*  That's one purpose.
*  The other is with respect to inference.
*  If you have a large memory bank, it can take time to search it for the right answer.
*  If you forget a bunch of stuff, particular useless stuff or redundant stuff, then you can search it faster and so you can do inference faster.
*  So that's two real unambiguous purposes of forgetting from a computational perspective.
*  I don't know if that answers your question, but that's why forgetting is useful in general.
*  Yeah, OK. In a formalistic way, as usual.
*  Jovo, did we do it? Take two. Do you think we did it this time?
*  I'm happy with it. I also like I'm getting rained on, which I feel pretty excited about.
*  Oh, there's a thunderstorm out in my window as well, but I'm not getting rained on.
*  Well, let's say goodbye real quick. So thanks for doing it again.
*  I'm glad we got to read you and hope you're happy with it.
*  Keep up the good work.
*  Thanks, Mon. I really appreciate your time.
*  I alone produce Brain Inspired.
*  If you value this podcast, consider supporting it through Patreon to access full versions of all the episodes and to join our Discord community.
*  Or if you want to learn more about the intersection of neuroscience and AI, consider signing up for my online course, Neuro AI, the quest to explain intelligence.
*  Go to braininspired.co to learn more.
*  To get in touch with me, email paul at braininspired.co.
*  You're hearing music by the new year.
*  Find them at thenewyear.net.
*  Thank you, thank you for your support. See you next time.
