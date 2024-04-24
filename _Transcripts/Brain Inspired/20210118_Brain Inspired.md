---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5130s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 41442
Video Rating: None
---

# BI 095 Chris Summerfield and Sam Gershman: Neuro for AI?
**Brain Inspired:** [January 18, 2021](https://www.youtube.com/watch?v=OBMsP7VNU9Q)
*  It took a while for me to come to the appreciation, and this is partly thanks to Chris, of the
*  importance of computation in the way that we think about all aspects of the brain.
*  You know, we talk a lot about diversity in our field, and you know, I think that there's
*  a type of diversity which sometimes gets less attention, which is intellectual diversity.
*  And I just think that the diversity of viewpoints which neuroscientists bring into machine learning,
*  is like a kind of intellectual stirring of the pot. That in and of itself carries enormous intrinsic value.
*  There's no common ground for everyone to agree on what constitutes artificial general intelligence, for example.
*  And I think for cognitive scientists, in some ways it's a little bit easier because what we want to do is not necessarily
*  define an all-encompassing notion of intelligence, but try to isolate some aspects of human intelligence that we think are important.
*  Without claiming that those constitute the entirety of intelligence, and then try to build machines that match those abilities.
*  What we're doing in cognitive science, in computational neuroscience, is basically to try to come up with good new ideas
*  that might be seeds, that might be planted and might scale. Not all of them are going to scale, right?
*  But they're just interesting principles about how information processing systems work, that give us the nugget of an insight
*  that might one day be translated into something bigger and more powerful.
*  This is Brain Inspired.
*  Artificial intelligence continues to contribute to neuroscience, but does neuroscience have anything really to offer AI moving forward?
*  That's the main topic this episode. Hi everyone, I'm Paul. Today I bring you Chris Summerfield and Sam Gershman,
*  who've known each other a long time, and they have slightly different but overlapping answers and viewpoints regarding that question.
*  Chris runs his Human Information Processing Lab at the University of Oxford, where they focus on the computational underpinnings
*  of how we learn and make decisions about what we're perceiving and what actions to take.
*  And he also works at DeepMind. And this is the second time Sam has been on. He was on episode 28 back in the day.
*  He runs his Computational Cognitive Neuroscience Lab at Harvard, where they focus on the computational underpinnings
*  of how we learn and represent our environments.
*  So we have a wide-ranging discussion today that begins with and circles around the relationship between neuroscience and AI
*  and how neuroscience has or hasn't and will or won't influence the AI world.
*  And along the way we dip into topics like the merits of prediction versus understanding,
*  the centrality of humans in specifying the problems that we want AI to solve and what that means for the kind of AI that we are building,
*  how artificial general intelligence and or human-level AI fits into that story, and plenty more.
*  There's also a guest question today from Andrew Sacks, who's been on the podcast before, where we discussed some deep learning theory issues.
*  He's also one of the co-authors with Chris on a recent opinion piece titled, If Deep Learning is the Answer, What is the Question?
*  Which of course I link to in the show notes with the other stuff at braininspired.co.
*  Just a reminder, if you support the show on Patreon, I've started a Discord community that's slowly becoming more active and engaged
*  and will likely lead to some live online gatherings in the future.
*  So check my Patreon posts for how to join that.
*  And if you don't support the show on Patreon but want to for a few dollars a month, go to the Brain Inspired website and find the red Patreon button there.
*  So I've made a few levels of support now with different bells and whistles within each level.
*  I trust you'll enjoy Chris and Sam today. The discussion centers on what this podcast is all about. Enjoy.
*  So Chris, I was reconnecting with Sam a little while ago and I had I re-invited him back on the show because he's been on the podcast before.
*  And I offered to have him invite someone and pick a topic of his choosing and maybe invite someone to dialogue.
*  And I suggested he invite someone intellectually inferior.
*  And like right before I even finished the sentence, he said, Chris Summerfield.
*  So anyway, thanks for coming on.
*  That's prophetic on your part.
*  So you guys knew each other at Columbia in the mid or early 2000s, correct?
*  That's right.
*  That's correct.
*  How did you guys know each other? And what I really want to know is, you know, what was going on at that point in your minds and in your perspectives and outlooks and how those have changed since then?
*  Well, I mean, I remember sitting wedged between two graduate students desks.
*  One was Chris and one was Emily Stern.
*  And they had put a little plank of wood connecting the two desks where I could place my computer there.
*  And then I would just I would be trying to work.
*  But really, I was mostly listening to them banter with each other.
*  You were an undergraduate, right?
*  I was an undergraduate. That's right.
*  So I was just completely swept away by the experience of graduate school.
*  I thought that seemed to be the most fun thing that you could be doing with your time.
*  It actually was kind of catastrophic for my undergraduate career because I completely lost interest in classes and wanted to just come to the lab all the time.
*  I remember the time well.
*  Yeah. So the banter with Emily goes on to this day.
*  But I mean, I think it was an interesting time also to be a graduate student as well, because it was sort of like it's kind of like the wild.
*  It was like the Wild West of neuroimaging at the time.
*  So 2000 and must have been 2003, 2004.
*  And I think the field was still at a stage where you could sort of take any task off the shelf and put someone in the scanner and like, you know,
*  whatever you found was a result of some interest, at least to that community.
*  And, you know, you asked about how things have changed.
*  I mean, it's interesting, you know, both, I think probably the way what Sam and I both find interesting in our work right now is probably just as different as it could possibly be to what the field where the field was at at that time.
*  In the sense that, you know, at that time, there was very little focus on on mechanism and there was there was very little concern given to how whatever you measured at the neural level might actually tap into, you know, what was going on, the underlying mechanics.
*  And I think it's very different now.
*  How have your interests changed?
*  So, Chris, you said that the interests of the field were different than than your interests now.
*  How have your interests, you know, what were your what was your big question back then and how has it changed?
*  Well, I was I was working.
*  I mean, the lab where Sam and I were both working was it was Jennifer Mangels lab.
*  It was a memory research lab, cognitive neuroscience memory lab.
*  And after having done my PhD there, I think that, you know, I was kind of disenchanted with the idea that the end point of science was kind of to identify these sort of data features and just to write stories about the existence of these data features as a scientific result.
*  And I wanted to I wanted to do something that made much tighter links to, you know, how the system worked.
*  And at the time, I felt like the only way that I could do that was to go and work in what was then kind of the most, you know, I guess like the the domain that has the sort of simplest mapping from stimulus to theory or or I guess experiment to theory, which was to work in psychophysics or perceptual decision making as it became known around that time.
*  And, you know, it's interesting that that move in that in making that move, I kind of shed, you know, all of this sort of stuff about cognition and and memory and so on.
*  But I think that the field has the field has has in a way it's sort of come full circle.
*  And I think that what's going on now is that there is a lot more traction computationally on those those more topics of of of cognitive interest.
*  I mean, that's not to say that we didn't have good cognitive theories around the time, but I think those theories are now much more joined up with with neuroscience.
*  And so for me personally, you know, it feels like coming back to cognition as a really important domain of study.
*  And all the things that we thought were just simple psychophysics turn out to be impinged upon by various cognitive processes like beliefs and memory and so on.
*  And Sam, so how was your perspective changed?
*  I mean, you had already been I was just looking back at your neuro tree for you, Sam, and if you know, for both you.
*  But but man, you were a research assistant in like three different labs as an undergrad.
*  It looks like as an undergrad. I mean, you have this you've had a lot of variation in your upbringing in your trajectory, I suppose.
*  It seems like you've always been interested in in all of this stuff.
*  But did you have this kind of wild eyed view? How is your perspective and interests and outlook changed?
*  Well, I think like many people as an undergrad, I just didn't really know enough or understand enough to know what was connected to what or what was not connected to what.
*  And so everything sort of seemed interesting and connected.
*  But I mean, it is I was really just kind of confused and bouncing around and following my nose towards whatever was interesting.
*  So I had started off doing stuff on on memory, but I got interested at some point in emotion and later in decision making and reinforcement learning.
*  After I left Columbia, I went and worked at NYU for a while in Nathaniel Dawes lab.
*  But I think my my perspective has changed a lot in the sense that I didn't really have much of a perspective when I was an undergrad.
*  I was just trying to do things that seemed interesting to me.
*  And I think it was it took a while for me to come to the appreciation.
*  And this is partly thanks to Chris of the importance of computation in the way that we think about all aspects of the brain.
*  I guess I don't know if this is true, Chris, that at the time that I met you, I think you are undergoing a similar kind of conversion experience.
*  And so that is so like but the problem was that at Columbia at that time, there weren't really people doing this kind of this kind of thing.
*  I mean, there were there were computational neuroscientists at the medical school, as there still are.
*  But in the psychology department, which is where we were, there wasn't a lot of that.
*  And so I was just kind of picking things up as I went along.
*  That's that's absolutely right. So Columbia was in a way I mean, it was a it was a wonderful place to be a graduate student.
*  But in a way, it was also a slightly strange place because I think there's a policy particularly of maintaining incredible diversity in the research interests and approaches of the faculty there,
*  meaning that you have lots and lots of different topics being addressed, but you don't have a critical mass in any one topic.
*  And there certainly wasn't a critical mass in cognition or in cognitive and computational neuroscience, which is, I guess, you know, sort of where both our work has ended up.
*  Chris, I mean, we won't perseverate on this for too much longer.
*  But Sam mentioned that there was his experience was one at least partially of a sort of mentor mentee relationship.
*  And I remember being a graduate student and interacting with undergrads, even being a postdoc and interacting with graduate students.
*  And I always knew in the back of my head that that's what the relationship was mentor mentee, but it didn't feel that way.
*  Did it did it feel that way? Were you mentoring Sam? Did you were you conscious of that?
*  Are you kidding? It was almost the opposite way around, I think. And it's remained that ever since.
*  No, I mean, I actually think to this day, I I continue to feel how important it is to nurture undergrads because I just benefited so much from just
*  I don't even know if nurturing is the right word. It's just being able to hang out around graduate students and sponge up what they're doing, even though they're only just marginally less confused than I was.
*  But I didn't realize it at the time.
*  Marginally less confused, but but slightly more than marginally more miserable sometimes.
*  Well, that was the other thing that I found jarring was I remember going to dinner at one point to a graduate student's house when I was still an undergrad.
*  And all the grad students were really griping about their lives and their careers.
*  And I just couldn't understand it because it just seemed so glamorous to be a graduate student from where I was sitting, which is like I couldn't go to a class without falling asleep.
*  And I just I just wanted to be where the action was.
*  But now now I understand a little better the difficulties of being a grad student.
*  All right, guys. Very good. Well, so the the I guess the main topic that we can just dance around here that Sam mentioned that maybe you guys had different perspectives on how valuable neuroscience is to A.I.
*  And, you know, the overarching picture, I suppose, and you can correct me if I'm wrong, is that Sam thinks that neuroscience hasn't contributed much to A.I.
*  and or doesn't have as much to contribute to A.I. as A.I. has to contribute to neuroscience.
*  And he believes, Chris, that you believe the opposite as you've written about plenty as and spoken about.
*  And I know it's more subtle than that. But so I'm not sure what the best way into this discussion is.
*  Whether you each want to just make a case using an example from your own recent work or I have some suggested topics that can lead us into this discussion.
*  Well, can I just clarify? I don't.
*  It's not that I think that neuroscience can't contribute anything to A.I.
*  I certainly would very much welcome that. I just think that it's been a little bit oversold.
*  I think that the examples that people use as evidence for that kind of claim are a little bit thin.
*  That's my perspective.
*  So, I mean, there's a number of different clarifications, which I think it would be important to make before we start the discussion.
*  So the first one is about forward looking versus backward looking.
*  Right. So, you know, obviously neuroscience, cognitive science and A.I.
*  research have kind of grown up together.
*  And so, you know, the in the past, there obviously has been considerable mutual cross fertilization.
*  But whether you would want to characterize that as like, you know, ideas in A.I.
*  sort of being imported wholesale from neuroscience or not, I mean, you could certainly tell that story, right?
*  You know, you could say, oh, look, you know, we suddenly realized that a good way to do computation is to have like, you know,
*  sheets of neurons that integrate information and transduce it nonlinearly.
*  Like, wow, that's because that's what the brain does.
*  But, you know, of course, it's not as simple as that.
*  Or you could make equivalent stories for reinforcement learning or for even for memory processes.
*  If you think of, you know, the way that LSTMs do gating, right, it looks an awful lot like our contemporary theories of,
*  you know, activity, silent states and fast synaptic plasticity and prefrontal cortex.
*  So you can make those stories. But I think that's kind of not the most interesting way to tackle the question.
*  And maybe if I could just. Forward looking. Yeah, go on.
*  I'm sorry, because I didn't. It might be useful to ground this a little bit in the question.
*  If if I am a computer scientist trying to build A.I., what should I spend my time doing?
*  Should I spend my time basically trying to build engineering artifacts and fiddling with them until they do something useful?
*  Or is it good for me to spend at least part of my time learning about biology and maybe even doing biology in the effort?
*  It's part of an effort to uncover the mechanisms that allow the brain to do intelligent things.
*  And and and so I do get plenty of people into my coming into my office.
*  I'm sure Chris does, too, that people from computer science and other engineering disciplines
*  who want to learn about the brain precisely for this reason, because they think that by learning about the brain,
*  they can uncover some secrets that they can put into their algorithms.
*  And I think that that's the part that I'm kind of skeptical about.
*  I think that certainly the idea that you could find parallels and cross currents between neuroscience and that that's that that's been hugely useful.
*  Even if we don't worry about like the whole intellectual history of who influenced who,
*  it's just I think it's a it's a matter of like what do you hope to get out of biology as an engineer?
*  Can I just ask a clarification question about what you mean by biology?
*  Because, you know, for instance, you know, in your in your paper, building machines that learn and think like humans,
*  you talk about a lot of cognitive aspects that could be could be an aid to to building A.I.,
*  things like intrinsic physics, intrinsic psychology, causality, compositionality.
*  But these are more cognitive science type psychology level type things.
*  So when you say biology, do you just do you mean the the the I mean actual biology or because we're talking about neuroscience here,
*  not about psychology. Yeah.
*  OK. Yeah. See, I guess my definition of neuroscience is just really broad because if you narrow the neuroscience down to because I believe that when you're doing
*  when you're using like deep learning models to understand the brain, you're doing neuroscience and you're comparing it to brain activity.
*  That is neuroscience. But that's not what we're talking about, right?
*  We're talking about using neuroscience to build better A.I. Right.
*  So I think we were all in agreement that A.I. has had a lot of lot has contributed and will continue to contribute much to our understanding of the brain.
*  It's sort of the other direction, which I'm more skeptical about.
*  Does it matter? Do you think that neuroscience is still quite young and from my perspective still has a long way to go in learning actually what the brain is doing?
*  But this is this is exactly the issue that I'm concerned about, which is that how what is the process by which we understand what the brain is doing?
*  The reason why I move towards computational theories is because the computational theories provide a way of not just interpreting, but also just describing the mechanisms that we observe in the brain.
*  So the point is that we can't actually discover how the brain works unless we go in with some computational theory to interpret what we're measuring.
*  There's not there's not a kind of naive empiricist pathway by which we can just look at the data and from that extract computational mechanism.
*  Do you think people believe that there is?
*  I do. I mean, I think that many neuroscientists approach the data gathering enterprise in that way that will measure a bunch of things and then see what comes out or apply kind of sophisticated statistical algorithms to extract structure from their data and then try to interpret it.
*  But that's not necessarily the sort of that's not necessarily the sort of knowledge that people are going to want to buy into in machine learning in order to try to build better models.
*  Right. Is it? I mean, it's true that people do that.
*  Sorry, which kind of knowledge?
*  Well, I mean, you know, this what you described is this sort of, you know, there are these sort of Baconian neuroscientists out there who are just into sort of, you know, massive data collection exercises.
*  And of course, you know, there is an excitement around, you know, big data in neuroscience, rightly, I think.
*  But when you talk about, you know, neuroscience influencing AI research, I don't think that's what most readily springs to mind.
*  I think when we think about neuroscience influencing AI research, we think about constraints on architectures that come from our knowledge of memory systems.
*  We think about, you know, kind of the sorts of processes which underlie attentional selection or task level control or even language.
*  And we think about these clearly.
*  These are not ideas from neuroscience, qua neuroscience.
*  Right. These are ideas which span psychology, cognitive science and neuroscience.
*  But I think I think there is there is a there is an argument that these things are useful for building stronger AI.
*  But I think it really depends upon what you want your AI to do.
*  Right. I mean, what do you want to do is is protein folding.
*  I shouldn't think you need any of these things.
*  Yeah, I think when we talk about AI, we're talking about doing the kinds of things that the brain does.
*  Right. Human flexible human intelligence.
*  Right. That's just that's not all of AI.
*  But that's I think that's the kind of AI that is in question here.
*  And I think just in response to what you just said, Chris, it seems to me that there's that we have two horns of a dilemma.
*  One is one path you can go is collect data in this sort of Baconian big data mode.
*  But until it's interpreted through the right theoretical lens, it may not be particularly useful from an engineering perspective.
*  Or you can go in with a more theory driven approach.
*  But to do that, you need to have already a computational theory in your grasp.
*  And the problem is that if you already have that computational theory, right, then again, from the engineering perspective, you could just build that computational theory into your algorithms.
*  Right. You don't need if you already have a computational theory, why do you need to go look at the biology?
*  Yeah, I mean, I don't disagree with that at all.
*  I mean, to my mind, neuroscience has many things to offer AI, but they're not primarily theories of how the brain works.
*  I think they're they're primarily tools and approaches which are mature in psychology and neuroscience and which are either overlooked or immature in machine learning and AI research.
*  So one is just like a good sense of how to define the question, right, to have to define a research question.
*  So one thing psychologists are really good at is they're really good at framing a research question and desiring and designing environments.
*  You know what we call, you know, experiments in machine learning terms is just an environment defining environments that are there to kind of explore that research question and try to work out how an agent is solving a particular class of problem.
*  And that's an enormously useful tool for doing machine learning research, because if you want your engineering approaches to scale and generalise, you need to understand how they work.
*  And what machine learning and AI researchers historically do very badly is to take the trouble to sit down and try and work out how their algorithms are solving the problems that they're solving.
*  And, you know, there's there's not to say that nobody does that, but there's an excessive focus on whether it works relative to how it works.
*  And I think what neuroscientists can provide are tools and approaches that can can mediate that.
*  I also just think that sociologically, you know, maybe this is trite point, but, you know, we talk a lot about diversity in our field.
*  And, you know, I think that there's a type of diversity, which sometimes perhaps reasonably, but it gets less attention, which is intellectual diversity.
*  And I just think that the diversity of viewpoints which neuroscientists bring into machine learning is sort of, you know, it's like a kind of intellectual stirring of the pot.
*  And, you know, I think that that in and of itself carries enormous intrinsic value.
*  And I think that it's exactly the same is true in the reverse direction.
*  Right. And maybe I don't know if we'll get on to talking about how neuroscience is being has been and is being shaped by, you know, what's gone on in AI research in the last sort of eight to ten years.
*  But in both directions, that sort of, you know, mixing it up that's come from the crossover between the fields, I think is really, really valuable.
*  Yeah, I think what you're saying, Chris, resonates with me a lot.
*  The thing that just to maybe give my own reiteration of what you're saying, the thing that neuroscience and cognitive science have contributed most, I think, to AI research is a different kind of workflow pattern.
*  Because if you think about if you think about the way in which computer scientists go about improving their their artifacts, they you have to you have to establish some benchmarks and then show that you can achieve state of the art performance on those benchmarks.
*  And then there's this kind of arms race to get better and better performance.
*  But at some point, people say, well, we need different benchmarks like this benchmark is not capturing something important.
*  And usually the points at which that happens is when people realize.
*  And it's sort of when when the computer scientists kind of step outside their paradigm and look beyond to the things that people do often that that people can do and their systems can't do or fail in weird ways.
*  Right. So examples of this are like adversarial examples for computer vision systems, for example.
*  And I think that what cognitive scientists and neuroscientists have to offer is that essentially they have a whole collection of the they have a collection of different ways of teasing apart these different kinds of or let me put it a different way.
*  So they I think that they have a methodology for looking for constructing the kinds of tests that would reveal mechanism.
*  Right. That's what Chris was saying before.
*  And that that is often of less interest to engineers who are trying to achieve state of the art performance because you don't necessarily need to understand why some things work.
*  Something works as long as it works. Right.
*  It's sort of like keeping things, keeping people honest, right.
*  Keeping computer scientists honest about what is the what are the important things to capture.
*  Yeah. But also, I mean, if you think about even beyond beyond thinking about, yeah, this keeping honest or whatever, if you think about the the way in which cognitive scientists and neuroscientists have have also helped define the problem, right, define the set.
*  If we're talking about like, you know, kind of AI research of the kind of, you know, what people call the search for general intelligence, then, you know, even just defining what that means is something which I think within machine learning and AI research, there's not enough attention given to.
*  And I think in cognitive science is something that people have thought much more deeply about, you know, posing the simple question of like, if you if you wanted to to develop like success criteria for building the sorts of intelligence, like if we're talking about human level machine intelligence, what would those success criteria look like?
*  I think that, you know, that's the sort of question that you're going to find richer and more varied answers in cognitive science, maybe not necessarily neuroscience, but in cognitive science than you would in contemporary machine learning research, I think.
*  That was going to be one of my questions to you because so cognitive science has what originally six branches, anthropology is even one of them that is supposed to be included in what cognitive science is.
*  But philosophy is one of them. And I'm wondering if if we get the definitions wrong, if we get the questions wrong, is that going to hinder the ability to create something like AGI? I'm not sure if that's what you're getting at, Chris, about formulating the questions correctly.
*  And if that's what you mean, is the philosophical part of cognitive science or or something else?
*  I don't even know if it needs to be a philosophical part, right? Formulating a research question is an intrinsic part of the scientific endeavor, right?
*  You know, you think thinking about, you know, what does it mean for an agent to, you know, kind of display some some strong forms of generalization or to display metacognition or to, you know, display curiosity?
*  How do you operationalize those and how do you measure them? That doesn't seem to me like a philosophical question. That seems to me like a scientific question. That's the sort of thing that cognitive scientists do well.
*  So, yeah, I think operationalization is a scientific thing. So but so there's no risk you think of if we, you know, something like metacognition, right, which I quote unquote studied and thought I knew what it meant until I studied it and realized I didn't know what it meant.
*  You know, a lot of assumptions I had about what it meant. So we operationalized it and then measured things. But I still don't know what metacognition is, even though we operationalized it, we gave it a definition, measured it and said whether the monkeys were being metacognitive, for instance.
*  But I still really don't understand what metacognition is. And I don't know if that matters.
*  So can I give a different example, which might be useful reference point for discussion? You sometimes see computer scientists saying that a particular task was solved. So for example, at some point, I think people started declaring Atari to be solved.
*  Well, one operationalization of success in those games is can you achieve human or superhuman level performance with enough training? And then by that criterion, you could say that Atari has been solved.
*  But if you look at it from the perspective of achieving human level sample complexity, like can you get to the asymptotic performance as quickly as humans can? Or can you generalize to other variants of the games as quickly as humans can?
*  And then arguably, Atari hasn't been solved yet. So depending on your operationalization, you're going to have different criteria for success.
*  And to me, I think the important thing is that there's nothing within the framework of machine learning that tells you how to operationalize the constructs of intelligence.
*  And I think that's why there's been so much back and forth about this, because there's no common ground for everyone to agree on what constitutes artificial general intelligence, for example.
*  And I think for cognitive scientists, maybe it's a different kind of, in some ways, it's a little bit easier because what we want to do is not necessarily define an all encompassing notion of intelligence, but try to isolate some aspects of human intelligence that we think are important.
*  Without claiming that those constitute the entirety of intelligence and then try to build machines that match those abilities. And that the hope is that by studying those empirically, we can learn something about how they work in the brain and that can be ported into AI.
*  I was waiting to see if you had comment on that, Chris. I mean, go ahead if you do.
*  I don't know if I really do have a comment. I mean, I completely agree. You know, the operationalization question, we can operationalize in terms of some sort of external benchmark like Atari, right?
*  So nobody in the contemporary AI community invented Atari, just as they didn't invent Go. So it provides an external benchmark.
*  But of course, you know, there's a kind of, you know, there's a kind of good heart's law problem with these external benchmarks, right?
*  Which is that, you know, people optimize for the benchmark and they don't optimize for the general functions which underlie good performance on the benchmark, right?
*  And, you know, the trouble is that then you're into, if you say, okay, well, let's dispense with the external benchmarks, then you're into the much more slippery world where you're both making up the tests that you use to evaluate your agents and you're training the agents that are going to try and pass those tests.
*  Right. And that's obviously a much more, you know, it's a much more difficult situation to come up with good validations of your performance because obviously you don't know whether those two process, the process of building the test and the process of training the agent are actually sort of mutually interacting in some way, which means that, you know, you're just satisfying your own demand characteristics.
*  I think this is a real challenge for AI research.
*  I think it's also a challenge for neuroscience research, honestly.
*  I think that we see a similar phenomenon where, for example, now one approach to understanding what the ventral visual stream does is to train systems for image classification.
*  So that typically is some kind of deep convolutional neural network and then try to quantitatively match the activity in the layers of the artificial network to the activity in the layers of in the different regions of the ventral visual stream.
*  And then the game becomes how do we get those numbers, the numbers quantifying the match to be as high as possible.
*  And my worry about that is that in operationalizing success in that way, you're ignoring a lot about other aspects of vision that might not be captured by these kinds of systems.
*  So when I talk to students about this, I often give them examples of all sorts of phenomena from visual cognition, which it's not obvious or not only is it not obvious that the systems can do it, but nobody is actually trying to ascertain whether those systems do it or few people are because the way in which the success criteria are set up are not designed to assess that.
*  That's not part of the assessment.
*  So I agree with that like 100%.
*  So I've written about this as well.
*  And I mean, I think that there is a real worry that what I see as being the central project of computational neuroscience, which is essentially to try to understand computation is sort of being sort of slightly gleefully dispensed with in the irrational exuberance around machine learning methods.
*  And there's a sort of sense of, well, actually, we don't have to grapple with the hard problems because we can just train neural networks and we can just find some linear mapping that kind of that links whatever our neural markers are with our neural network.
*  And that's kind of that is the story.
*  And, you know, you've you've had guests on your podcast, I think, who advocate for this.
*  And it seems to me that there's a there's a sort of a corollary of that viewpoint, which is that, you know, actually, there isn't anything really very interesting to be studied in the first place.
*  And I disagree with that.
*  And I suspect Sam does, too.
*  Yeah, but I guess I think we shouldn't summarily dismiss the kind of radical challenge to scientific understanding that's posed by these kinds of approaches, which I think I think I think we should we should address.
*  And I'll come back to why I think it doesn't quite work.
*  But I was very struck actually once talking to a geologist who told me that he felt that the general multiple generations of geophysicists were ruined by their classical education because the textbooks have various kinds of mathematical models and principles.
*  But if you actually try to use those to, for example, predict earthquakes, they just completely fail.
*  And he was impressed.
*  And I think it was a kind of earth shattering moment for him when he realized that he could train neural networks to predict earthquakes far better than all the classical theory could.
*  And to him, the way that he interpreted that was that we shouldn't be wasting time with the classical theory.
*  We should refashion science as a kind of predictive enterprise, because what good are all these scientific theories if they can't predict some of the critical things that we want to use them to predict?
*  And so it's a kind of it, a limited approach to the scientific enterprise where we're going to get rid of our conventional notions of understanding and replace them with generic prediction.
*  And I think there's a school of thought within neuroscience that that is a viable approach.
*  To me, the problem with this is not so much about prediction per se.
*  I think we should strive to build models that make good predictions, quantitatively accurate predictions.
*  The problem is, how do you know if you're successful?
*  Because you have to say this is the signal that I want to predict.
*  And then you can only declare victory once you've stipulated that these are the phenomena that I'm trying to predict.
*  And I had this conversation with Jim DiCarlo at some point recently where I was asking him, so you've set up the task that you want to predict as much variance as you can of, let's say, inferior temporal cortex activity.
*  Now you're using population recordings, but what if you can measure other stuff, right?
*  Like all the ion channel activations in all the neurons, right?
*  All the extracellular contents and so on, all the intracellular contents.
*  And he said, yes, I want to build models that can predict all of that stuff.
*  So the only limiting factor there is our ability to measure stuff.
*  And the more we can measure that, that automatically gets encompassed within the scope of the modeling exercise.
*  And that struck me as actually kind of surprising that he said that because it seemed to me that if your goal is to understand how a system can, for example, perform image classification, you might actually be doing, or object recognition.
*  You might be doing yourself a disservice because you could gain points in your score by basically just being able to capture the kinetics of ion channels without actually improving your ability to predict the aspects of the activation that are actually relevant for doing object recognition.
*  In other words, like if the scope of your scientific theory is completely unbounded, then you can score in ways that are kind of unrelated to the thing that you're actually trying to do in the first place.
*  Yeah. So I think there's two. I would agree with that and I would sort of nuance it in two ways, right?
*  So what are our critiques of a pure, you know, this kind of pure eliminative version of science in which all we try to do is come up with a great predictive model?
*  Well, I mean, number one is that, you know, there may be future occasions in which you wish to explain particular parts of the variance in your data, which are poorly captured by your predictive model, right?
*  So your predictive model, if you're just optimizing for a single variable, right, it may well be the case that that variable is not actually very interesting.
*  And the way that your model succeeds is by capturing all the boring stuff.
*  And the link to the specific case that we're considering, which is, you know, kind of trying to explain variance in population activity in IT is that, you know, if you compare the amount of variance that is explained by deep supervised networks that are trained versus untrained, it's actually a relatively modest improvement that you get by just training the network.
*  And what that means is that essentially most of your variance is being explained by what's present in the stimuli in the first place, right?
*  It's nothing to do with the network per se.
*  So you can build good predictive models that aren't actually all that useful in the long run.
*  And the second point, I think, is more critical.
*  And it's like, why do we want forms of understanding which are not just blind prediction?
*  And for me, that's because the translational opportunities which are presented by science are not just those that come with, you know, having fantastic predictive models.
*  I mean, protein folding is a fantastic predictive model.
*  And you can think, OK, in that particular case, all I need is a black box that's going to tell me exactly how this protein folds.
*  And then I can, you know, give malaria or whatever is going to be done with it.
*  But there are manifold other cases in which we need also to have understanding for understanding sake.
*  And that's because the decisions which are consequent to those predictions bear upon aspects of our society, which are, you know, kind of have have have moral resonance or have consequences.
*  So in other words, I'm talking about interpretability and, you know, we want to be able to understand how systems work because it's only when we understand how systems work and can explain them that we can make appropriate judgments.
*  So in this context, it might be a health context.
*  So we need to understand how things work so we can make decisions that have consequences for for patient care and not just for, you know, kind of for diagnosis and prognosis, for example.
*  That's also assuming that humans are the right judges.
*  Right. So why not just replace the human judgment with another black box predictive system that would if it's so good at what it's doing, why rely on humans to to be the arbiter?
*  Go ahead.
*  But I mean, we're talking about in any design system, you're designing it to do something that you want it to do.
*  Right. And part of the problem is that we don't know exactly how to specify the design in the sense that like, you know, the kind of common examples are like, I want to build a robot that says make as much money as you can.
*  Right. But then the robot goes and sells your dog.
*  Right. Now, you didn't know it's doing what you told it to do.
*  Right. But there's something that you didn't tell you didn't want it to do.
*  And because you didn't specify it in that way, then something bad happened.
*  And it's very easy to go off the rails in that way.
*  Right. Like if you tell the system, you know, cure malaria, what happens if it kills many thousands of people in the process and but still ultimately cures malaria?
*  So we can't it's inescapable, right, that there's a human in the loop for these for like socially meaningful.
*  Circling back to our earlier conversation, so I completely agree with that.
*  And, you know, for me, in actual fact, you know, we talked about we framed this discussion around a distinction between, you know, general versus narrow AI.
*  And I actually see that distinction as being inextricably linked to precisely what Sam just highlighted.
*  So for me, any sort of generally intelligent system has to be a system which is able to forge its own priorities independent of a human who, you know, kind of specifies them directly, right?
*  It's a system that is able to work out what it should do in the context of, you know, in the open ended context of the data that it receives, rather than satisfying an objective like, you know, kind of, you know, fault proteins are when it go.
*  Chris, how far do you how far do you take that?
*  So if we think about actual humans, we spend a lot of time raising kids and kind of programming them to have the same value, not just the same values, but also the same sort of methods for for achieving their goals.
*  And that's part of us.
*  Inculcating the design specifications for living in human society.
*  And I would expect the same would be true of a robot, right?
*  Like when you say they should be able to operate independently, I don't think you mean completely independently because they still have to kind of interact with human society in various ways.
*  I just interject and say that despite our best efforts to program our children, it doesn't work.
*  Right. So because of, you know, things like and Chris has written about, I was going to ask about intrinsic motivation and having something at stake and, you know, the reward paradox, et cetera.
*  And how much that has to bear on on this sort of question of of the general AI aspect and having something at stake and having your own issues and and something to well intrinsic intrinsic motivation, I suppose would be the question.
*  But but Sam, you're fooling yourself if you think you're probate programming your children well.
*  I didn't say I'm programming them well, but I said that I think that we're underestimating how much we program our kids and like they couldn't function in human society if all they did was hoard resources for themselves and kill anyone who got in their way.
*  Right. And they learn because your kids are not teenagers yet.
*  You know, they they they learn skills that allow them to cooperate and collaborate with other people.
*  So I mean, I agree. And I mean, you know, if you ask me, I mean, we we haven't got to this point in the discussion.
*  But, you know, my my view is that I don't think that we will be able to build general intelligence in any recognizable form.
*  And I think that actually as a project, I actually don't see that as necessarily something which is going to be, you know, the most advantageous goal for humanity.
*  I mean, I I think, you know, first of all, we have a lot of humans and, you know, we probably don't want to build any more or we don't need to build any more.
*  And secondly, I think, you know, but more more seriously, I think that so much of what we think of as human intelligence comes wrapped up with our our social nature, with our culture, with the things we learn from others, from our parents, from society, with the values that we have.
*  And I think those values, we acquire them by virtue of being human ourselves.
*  And I think it would be very difficult, if not impossible for an agent, which is not a human, which does not have human status in society, which does not have a human body, a human abilities, which is not constrained in the same way that a human is, you know, you know, I can't like, you know, make a copy of my brain, right.
*  But an AI system, you could. So a system that is not constrained in those ways, I don't see how it could ever have the same sort of intelligence that that we do.
*  That doesn't mean that we wouldn't be able to build very powerful systems.
*  But I think the goal of sort of seeking to emulate a human is a little bit naive, perhaps.
*  This obviously intersects with questions of value alignment.
*  Right. So, I mean, you're saying that we may not value it as a species anyway, that we would derive more value from a bunch of narrow AI than a human like general AI. Am I reading you correctly?
*  I mean, it's something in between, right? Sorry, Chris, you should answer the question.
*  Yeah, I mean, I'm not saying that we shouldn't try to build stronger AI than we have right now.
*  And, you know, I share completely all the, you know, the things that Sam has highlighted, right, you know, which is that, you know, the machine learning solutions that we have right now tend to be, they're not very robust and, you know, they're limited in their applicability and so on.
*  I think we can do better.
*  But I think that, you know, kind of a sort of naive imagining of the end point of this research as being something which is, you know, sort of walks and talks a little bit like us, except kind of better, is misguided at best and, you know, dangerous at worst.
*  I think if you look at how AI is portrayed in science fiction movies and literature, that's the kind of thing that I think most people have in mind when they talk about AGI, right?
*  It's something it's like very capable assistance for humans, right?
*  And I think what people sometimes forget is that there's a big difference between very capable assistance for humans and humans.
*  Because we don't necessarily want AI systems that have all the same values as us because those systems are going to expect the same privileges as us.
*  They're going to expect the same to be able to live the same lives as us, right?
*  And we don't want to be in the business of like enslaving other humans, right?
*  So the minute that they really achieve that kind of humanity, then that's going to be the point at which the artificial assistant era is kind of over, right?
*  Unless you're willing to start a new era of slave machine slavery.
*  So I think that our goals should be to create good, strong AI systems that can help us do things that we care about and not worry too much about perfectly emulating the human brain.
*  Right. So to bring some of these trends, I mean, the conversation's sort of gone in two different directions, but to bring these trends together, I mean, I guess for me, what links these two topics is that in science, we need understanding for understanding's sake.
*  And for me, at least, you know, having great predictive models is not the sole objective of science.
*  And, you know, when we're thinking about AI, understanding additionally furnishes us with an opportunity to not only build powerful systems, but to understand how those systems achieve the goals that they are set.
*  And thus to have, you know, to be able to exert more control over them, to behave in ways that we find to be acceptable, right?
*  The value alignment problem, you know, bypassing some of the potential externalities, which will inevitably ensue from just sort of rampant, you know, kind of optimization of powerful agents.
*  Okay, guys, so I'm going to throw a wrench in this real quick, because just for the in the interest of time.
*  So we were going to talk and we may still talk about and frame some of these questions about how neuroscience can inform AI and how AI has and can inform neuroscience.
*  We were going to discuss Chris's recent paper, If Deep Learning is the Answer, What's the Question?
*  One of the co-authors on that paper is Andrew Sachs, and I enlisted him to ask a question.
*  I'll just play the question and I'm sorry if it's kind of an orthogonal perhaps, but I'm sure we can bring it all back together.
*  So here's the question. And Sam, this is you know, you can take this for you as well.
*  Hi, Chris. It was an absolute pleasure writing this paper with you.
*  And I feel like we see eye to eye on so many things that, yeah, it's just always wonderful to collaborate with someone who you feel like each person really gets where the other is coming from.
*  That sort of makes it hard for me to ask an intriguing question.
*  But here's my attempt in rereading this paper, we defend the idea that it's worth trying to understand these models.
*  And yet I was reflecting on DeepMind's accomplishments.
*  And one of the features they seem to prize quite greatly in their systems is that their systems teach them something that the designers didn't know.
*  In AlphaGo, it discovered new moves in Go that were considered beautiful and certainly beyond anything the designers knew.
*  And in AlphaFold, we've learned something that there's no question no human has access to.
*  And my question to you is, have we underappreciated the value of that type of scientific discovery?
*  Are those opportunities waiting for us in neuroscience where one of these complex models delivers fundamentally creative new knowledge that humans can then go back and reinterpret?
*  OK, so it wasn't quite orthogonal, it turns out. But there you go. Thanks, Andrew, for the question.
*  I mean, the question seems very related to the discussion that we were just having.
*  Yep.
*  So I guess my answer would be the same. So, you know, if we focus on AlphaGo, I mean, it's kind of interesting.
*  It's certainly true that, you know, in a way the system is endowed with knowledge which we do not have in the sense that it can beat any of us convincingly at that game.
*  But to what extent that actually feeds back and provides us with new knowledge, I think it's kind of debatable, right?
*  I mean, when AlphaGo came out, I remember having a discussion with colleagues at DeepMind about what would constitute an explanation from AlphaGo of a particular move that it made.
*  And I think I should probably credit Neil Rabinovitz with this insight.
*  And he said that, you know, well, on the one hand, you can think of sort of two extremes of explanation which AlphaGo might give for one of its moves.
*  So on the one hand, it might say, well, you know, I made this move because, you know, parameter one was set to this value.
*  Parameter two was set to this value.
*  Parameter three all the way up to, you know, however many million of parameters it had.
*  And that would be one answer which would be basically useless to us.
*  Alternatively, you know, it could say, if you asked it why it made that move, it could say, well, because I wanted to win.
*  And that answer would also be useless to us.
*  And I think that it's actually a really non-trivial problem to back out what might constitute genuine interpretable knowledge even from these powerful systems.
*  I mean, the case of AlphaFold is a bit different because with the blind prediction, we don't understand necessarily how exactly AlphaFold is making those predictions.
*  But because we know it does so accurately, we can accurately we can go on and do incredible things.
*  And that's really, really amazing.
*  But I'm not actually sure that I agree with the central premise that we get that kind of interpretable knowledge for free out of these powerful agents.
*  Yeah, just to echo what Chris is saying.
*  I actually think that there's there's two ways to interpret what Andrew is saying here.
*  One is a kind of less radical interpretation, which is essentially that these kinds of systems are tools for discovering things in a similar way that, let's say, a telescope was a tool for Galileo being able to see things that he couldn't see with his naked eye.
*  Right. So there were sort of cognitive and perceptual limitations that, you know, in, let's say, the combinatorial space of go or protein folding,
*  we just can't evaluate all the different possibilities. So if we have a really powerful tool for efficiently searching the combinatorial space, then we can discover things that when presented to us, we can, using our own brains, interpret the meaning of those discoveries.
*  Right. So it's discovery in the sense that in the sense of a kind of measurement tool or prosthetic rather than a more radical notion of discovery,
*  which is that the machine itself teaches us how to understand what it's doing.
*  Right. And I think that's what Chris is talking about here.
*  And I think this is this is goes back actually, Paul, to what you're saying about metacognition and what it means, because if you take something like AlphaGo, AlphaGo is trained to win go.
*  Right. It's not trained to explain go to people.
*  Right. Now you could try to build machines that do that. Right. And I think that raises the question, why would you want to do that?
*  And for me, the reason why you'd want it to do want to do that. And this is essentially the problem of building interpretable systems is that the systems when we design narrow specifications for what we want our systems to do,
*  that's useful and kind of convenient because we know how to do that. Right. We know how to tell a computer system how to play go. Right.
*  That doesn't mean it's easy to build a system that actually wins go. But it's easy to define the goal of the system.
*  But when we say that we want a system to generalize in a flexible way, it's actually not at all clear what we mean by generalized flexibly, because we don't we haven't defined the scope of flexible generalization.
*  In other words, we don't know what is the set of things that we want to generalize over.
*  And you can see this in a lot of discussion about invariance in a ad. Right. So a lot of groups are interested in building invariance into their systems.
*  And everyone kind of agrees on intuitive examples, like if you have a representation of an object, then it should be invariant to certain kinds of transformations, like if you move it around or make it bigger or smaller.
*  But in essence, all of them, all of the definitions of invariant, all the specific definitions of invariance require some human to say this is what I want my system to be invariant to.
*  There's no way for the system to autonomously come up with what invariance is it wants or except well, I should qualify that by saying that there are people trying to build systems that can discover invariance is in that I think that's an extremely interesting work line of research.
*  But it raises the kind of puzzle, which is that how do you know whether it's learning the right kind of invariance is without humans being able to inspect the invariance as it learns to say, yes, that's a good invariance and no, that's a bad invariance.
*  And that's why we need interpretability, because we need to we need to we need to be able to verify that our system is doing the thing that we want.
*  I'm so glad you raised this issue. So this is something that I, you know, I feel very strongly about. And I think that it's something that is often, you know, deeply overlooked.
*  You know, I was just reading papers today in which, you know, the kind of in the introduction section, we've already these papers, there's kind of like, you know, it starts off by saying humans are great at generalizing.
*  And like we were building machine learning systems, but they don't do transfer learning or, you know, out of distribution inference, nearly as well as humans and like, well, how can we fix that? Right.
*  But of course, you know, there's a there's a there's a sort of hidden anthropocentrism in that statement, right, which is the assumption that the way that humans generalize is like the correct way to do it.
*  And so, you know, there's a well known example, which Gary Marcus is fond of illustrating using to illustrate failures of generalization, which is where you have a network which should in theory learn an identity mapping between, you know, kind of binary and from binary inputs to binary outputs.
*  And, you know, you can show that if you try to do that in a few sample way, then it fails on that that problem.
*  And I think what's not often discussed is the fact that implicit in that claim is the idea that the identity function is like the right thing to do.
*  So fundamentally, when you want to talk about good generalization, you're making an you're making an ontological claim.
*  You're making a claim about how the world is and thus what the generalization conditions which we want should be.
*  And the thing is that, you know, going back to what we were just discussing, how the world is, is always seen through the lens of our values as humans, right?
*  The world is as it is to us because of our human nature and because of our, you know, our shared beliefs and our shared customs and our shared values across society.
*  And I think that you can't escape from that.
*  And I think that that human element, because machine learning is born of statistics and computer science and these disciplines, which have sort of elided the human aspect,
*  there's a failure to recognize that fundamentally actually these deep research questions are fundamentally questions about the world and specifically about the human world.
*  Do you think that so for me personally, just viewing it, I feel like one of the things that machine learning and AI has taught us is just how poor we are at doing things and how limited our abilities are.
*  And really how, you know, like you just said in introductory papers, we're the most general thing ever.
*  But really, we're not very good at generalizing ourselves.
*  And we have all these constraints and limitations.
*  And I feel like AI has actually highlighted that.
*  And I'm wondering if you guys feel the same.
*  So AI has taught us about us in that respect.
*  It's a hard question.
*  Sam, do you?
*  I want to know what you want to get.
*  I want to know what you're going to say before I try to answer the question.
*  Well, it's a hard question in part because I could agree with it, depending or not, depending on what exactly you mean.
*  I mean, there's certainly lots of ways in which we generalize very effectively that we don't know how to build AI systems to generalize in that way.
*  But I mean, I mean, what kind of failures are you thinking of?
*  Oh, I don't have a specific example in mind, unfortunately.
*  But I just think in a in a general sense, you know, so AI can do very specific things very well using a very particular network, you know, deep learning network, for instance.
*  And we may be extremely bad at doing that.
*  And that's a very that's a specialized example.
*  And that's you know, we transfer learn much better than AI does, for instance.
*  But I think it has pointed out that we're not so good at a lot of things that we think we're good at.
*  I think was my main my main point.
*  Right. But I think I think I understand what you're saying.
*  Like we could say we think we're really good at playing Go.
*  But actually, we're not that good at it because you can build machines that do way better at us.
*  And we thought we were good because we're such generalized abstract thinkers, for instance.
*  And that's not the way to play Go, for instance, unless that's what the deep learning network is doing.
*  Well, I'm not sure about that claim.
*  I don't know if anyone has claimed that the reason we're good at Go is because we're such generalists.
*  I think actually to be really good at Go, you have to be single mindedly obsessed.
*  I mean, I think that's true of any kind of expertise in a particular domain.
*  But not if you listen. And I only know this for chess.
*  Not if you listen to the experts at chess, they're at least not aware of playing out all the scenarios.
*  Right. They're only aware of the heuristics of the board and the way the board is set up.
*  And they don't think six moves ahead.
*  They think I've been here before and this is what needs to happen because I can kind of see it.
*  Right. But I'm not I'm not making a claim about the specific mechanisms by which experts achieve success at these games.
*  I'm just saying that if you believe some of the theories about chess expertise, I don't know about Go expertise, but I could imagine that it's similar.
*  For example, Herb Simon did quite a bit of research on chess expertise.
*  And the claim was that they are building up this massive data.
*  Grandmasters, for example, are building up this massive database of patterns that they can refer to and determine their moves.
*  I almost feel like it's the opposite. You could make the opposite claim, right?
*  Which is that machine learning has sort of swallowed in a kind of unexamined fashion the notion that humans are really, really good at generalizing.
*  Because, you know, the sorts of behaviors, I guess, that we would like our agents to be able to to engage in, maybe there are things like, you know,
*  we want them to be able to solve complex math problems or we want them to be able to do science or we want them to be able to do means end reasoning to solve climate change or this kind of things.
*  And we recognize that these things are really hard and these are things that humans are actively engaged at and given enough time and resources might be able to do.
*  But I think that the real problem with that statement is, and this is, you know, obviously relates to things that Sam has said before, but it's some and others have said before.
*  But the real problem with the statement is that it overlooks the extent to which that ability to reason abstractly is is like heavily grounded in the training that we have and the sharing of information that we have.
*  You know, of course, I can do multiplication. I'm not very good at maths, by the way, but, you know, I can probably compute simple polynomials.
*  But like, you know, I can only do that because someone taught me how to do it.
*  Right. And we forget, I think, you know, that when we are trying to train agents, we forget that our ability to to solve complex problems and to reason abstractly,
*  that we forget about the extent to which that comes only through, you know, a really, really careful nurturing of our understanding in an educational or a curriculum setting and through the sharing of with other people.
*  And, you know, I think in a way there's a sort of naive motivation in a lot of papers in machine learning that focus on transfer learning, which is like, oh, you know, humans, you know,
*  it's like as if you take, you know, baby Jim and sort of just give him a lot of data and then, you know, because because there's something magical in his brain, then suddenly, you know, he can like understand quantum physics.
*  And it's I think by trial and error. And I think it's just not like that.
*  Yeah, I mean, this is if you look in the kind of psychology literature and the studies of analogical reasoning, which I think are maybe paradigmatic of what we'd like a ISIS to do in terms of flexible generalization.
*  Actually, humans are quite frequently quite dismal at that. And you have to do a lot of cajoling to get people to recognize analogies, at least in certain circumstances.
*  So I think part and part of that, as Chris is saying, is that in order to recognize analogies, you need a lot of content knowledge in the different domains in order to be able to map between them.
*  That's kind of the logic of cognitive theories about analogical reasoning, like structure mapping, where you need to start off with the right sort of primitives and relations in the two domains.
*  And then you can and then you can map between them unless you have that you can't achieve that mapping.
*  Yeah. So I think, you know, one one of the mistakes that people make in in contemporary research is to is to is to say failure to treat the kinds of computation that underlies sensory motor behaviors, and the kinds of computation that underlie, you know,
*  cognitive behaviors, reasoning and and and inference, a failure to treat those differentially.
*  And I think those are fundamentally different sorts of problems. And I think they're solved in fundamentally different ways in the human brain.
*  I think that, you know, if you look at sensory motor behaviors, you know, it takes years or months, years for us to learn to to walk and to recognize objects, for example, right, requires a lot of data.
*  And, you know, it's a highly complex, nonlinear problem at the end of which we have, you know, reasonably useful representations, both of objects and of motor patterns, right.
*  But that takes a long time to learn. And I think that, you know, when we look at human cognitive behavior, there's an assumption that the same thing sort of happens, right, that we just use, you know, big, complex functional approximation to acquire knowledge about, you know, I don't know, you know,
*  how to do legal jurisprudence or how to diagnose illnesses or, you know, how to, I don't know, understand the pancreas.
*  And I just think that that those types of understanding those kinds that rely on structured knowledge are not acquired in the same way that sensory motor behaviors are acquired.
*  They're quite in fundamentally different ways. And it's not just through lots of training and lots of feedback, whether that's reinforcement or supervised.
*  It's it's a fundamentally different process that has much more to do with sort of assembling little packets of knowledge into composite holes, bootstrapping off, you know, existing fragmentary understanding to try to gradually build up the sorts of knowledge bases that allow us to function effectively.
*  I think computationally, it's a completely, completely different process. And I think that's, you know, in thinking about, you know, the nature of reasoning and thinking about how we solve these types of problems, I think it's really, really important to separate those two domains.
*  So, Sam, the last time you're on the podcast, you recommended the book, What is Thought by Eric Baum. And in that I started reading it.
*  The way he thinks of the mind, which is what we all kind of want to understand, or that's an assumption on my part, what I want to understand the way he thinks of a mind is as a collection of, well, the mind is a program.
*  And not only is it a program, it's a collection, like all programs are, of subroutines, of subfunctions.
*  And he posits, you know, that most of the great stuff that we do, of course, is unconscious. And these are all like the tiny subroutines working in the background.
*  And I'm hoping that this is related to what Chris was just talking about, and that what the end result of all these subroutines working together somehow, all these modules working together is what results in mind and what we think of as mind.
*  But like, analogical reasoning, for instance, you know, and the awareness of coming up with analogy is just kind of this end result of all these subroutines working in a massive interaction.
*  And that, you know, we need to understand how the subroutines or algorithms are combining and being reused for various different cognitive functions.
*  And that's the way to go about understanding how our higher cognitive functions and our minds come about.
*  And Chris has noted in talks, you know, and especially with in AI, you know, modules like attention being added, you know, memory, external memory, those sorts of modules being added.
*  Chris has noted that one thing he thinks is important moving forward in AI is to figure out how to make all these little modules work together and function together.
*  And that might be key to developing some of these higher cognitive functions that are more human like, right, or more powerful anyway.
*  So I want to throw that out there, first of all, but I also wanted to ask if that is a place that is ripe for neuroscience, cognitive science to inform AI or if that's a place where AI is just going to engineer it.
*  And if you still if you agree with that, Eric Baum, if you still recommend that book and if you agree with that conception of mind as well, Sam.
*  Yeah, well, I think just harkening back to the thing that Chris said last about these sort of two completely different computational processes for acquiring different kinds of information on the one hand, sensory motor learning that might rely on some kind of dense function approximation,
*  whereas higher cognition is something more modular and maybe hierarchical.
*  I don't know if Chris, I'm paraphrasing you correctly, but I mean, it's maybe maybe it's a little bit too extreme to say that it's completely different learning mechanism like, you know, who knows, maybe both of them rely on back prop.
*  But but I do agree that the basis of higher cognition has to do with putting together simple building blocks into more complex functions.
*  I think that that is undoubtedly true.
*  And if you want to learn those abilities, you have to have strong inductive biases that promote discovery of this kind of modularity and hierarchical composition and so on.
*  Right. And those kinds of inductive biases might be fundamentally different than the kinds of inductive biases you need to learn a dense, let's say, feed forward mapping from sensory to motor programs.
*  But in terms of your question, Paul, about whether we can benefit from studying the brain, I guess it just all depends on what exactly one means by that.
*  Because, you know, there's just tons of data on things like attention and memory.
*  Right. But only some of that data is actually going to be useful from an engineering perspective.
*  And we just I don't feel like neuroscientists have made a sufficiently precise case about which aspects of the brain and mind are actually useful for engineering.
*  So I think that's a that's a I would guess a reason to have more dialogue at the level of here are these particular things that people do, not just in general, like complementary learning systems in some very general sense, but actually like here's how we think computationally.
*  And so another way of saying that is computational cognitive neuroscientists are building models all the time of things like attention and memory.
*  But I think from the perspective of the engineers, these models are not particularly useful because they're not scalable.
*  And they and they're designed to explain some very specific phenomena as opposed to being some kind of general purpose to actually understand what's going on in the brain.
*  And so there's a kind of disconnect in the in the methodologies.
*  So and I gather that I think I think at least people at DeepMind, for example, are interested in probing this more like, can we take the computational ideas from computational cognitive neuroscience and sort of upgrade them so that they can work with the data?
*  Yeah, I mean, I think I think that's absolutely right.
*  I mean, I, I completely agree that, you know, there's that there is a major barrier in translating any of these ideas, whether it's ideas about composition or
*  whether it's ideas about
*  memory systems or attention or whatever, a major barrier in translating from neuroscience to to AI.
*  And that is, you know, one barrier, as I mentioned, is just scale.
*  Right. So we tend to build toy models in neuroscience and everything, you know, in machine learning, it's not whether it works.
*  The matter is, it's whether it scales. Right.
*  Or at least, you know, that's that's at least as important.
*  The second issue is that in neuroscience, we tend to focus, you know, we tend to be narrowly focused.
*  So most people, I mean, I think, you know, Sam's group is really an exception because of the breadth of topics which are studied in his in his lab.
*  But most groups focus on either one brain area or one method or, you know, one process.
*  And they sort of drill down into that and try to understand it.
*  And, you know, of course, that's fine if you just want to model some data, you know, from hippocampal neurons.
*  But it's not fine if you want the whole system to work.
*  And then the last gap is that our models tend to be pretty handcrafted, of course, in neuroscience.
*  And so, you know, handcrafted models have relatively limited utility in contemporary machine learning.
*  So all those are serious impediments to, you know, all those mean that you can't just take sort of ideas from neuroscience off the shelf and translate them into viable machine learning methods.
*  But I think, you know, I'm sure Sam would agree that the whole point of what we're doing in in cognitive science and computational neuroscience is basically to try to come up with like good new ideas that might be seeds,
*  that might be planted and might scale.
*  Not all of them are going to scale, right?
*  But they're just interesting principles about how information processing systems work that give us the nugget of an insight that might one day be translated into something bigger and more powerful.
*  I'm reminded of when my kids were little and you get all this parenting advice.
*  And I remember my parents had particularly strong feelings about various things.
*  And I asked them, did you did you do the same thing for my brother?
*  And they said, sure. And I said, did it work?
*  And they said, no, of course not. He's totally different.
*  He said, so why do you think it would work for my kids?
*  And my wife had the sage wisdom to point out that like we shouldn't be thinking about parenting advice as sort of ironclad rules about how things should be done, but just ideas to be tried.
*  So maybe cognitive neuroscience is kind of like the naggy parent for AI, giving various kinds of rules about how the brain works.
*  But it's up to the engineers to kind of figure out and to use those suggestions and to figure out what's actually useful.
*  See, I just interviewed Alison Gopnik, who has written a whole book about how parenting is a recent word.
*  And to be a parent is different than parenting.
*  And we shouldn't parent or we shouldn't. Yeah, we shouldn't parent.
*  It's not a real verb, but we've only taken it on recently in society as a verb because it doesn't work.
*  So I guess what you're saying is cognitive science doesn't work for AI.
*  No, no, I mean, I just think I think I like Chris's perspective because I think it's more pragmatic.
*  It's saying like we shouldn't we shouldn't hope that cognitive science and neuroscience are going to give us completely like fully functional computational principles for artificial intelligence.
*  What they're going to give us are seeds for the construction of engineering systems because it's just any any realistically any system that's going to work in the real world is going to require all sorts of
*  extra stuff that we're not going to get from these kinds of stylized models that we typically use in cognitive science and neuroscience.
*  So in philosophy of mind, so there's always there's been this age old question of whether mental states are causal.
*  Right. So limited to Vizem says that they aren't that eventually we will, you know, the functional states of the at the implementation level essentially
*  will will learn enough about them that mental states will figure out are eventually not causal.
*  Do you think that AI will settle that debate, you know, building these networks and and we'll be able to use, you know, build AI that's explainable enough to us that we can understand enough that that it will settle the debate of whether
*  mental states, quote unquote, are causal or whether it's just all network properties or will that become a moot question?
*  I think the answer to the question is no.
*  I don't think anything will ever settle any philosophical debates.
*  I think the point of those philosophical debates is not to be settled.
*  It is to they are they are tools for the exploration of reason itself and the entrainment of cognitive processes that surround rhetoric and debate and and their ways of thinking about problems.
*  I don't think that. Yeah, I don't I don't think the point of that debate is to be settled.
*  Maybe I'm an outlier. Maybe philosophers who are listening will just want to shoot me at this point.
*  Yeah. Last, last question. Just just where where did we end up here?
*  So how so how useful is neuroscience for AI?
*  How you know and vice versa.
*  But most of the first question, because that's the question that I think is mostly assumed is that nurse these days is that neuroscience is not very useful for AI.
*  So I don't know. Where did we come to?
*  I have about a thousand more questions, as you guys know, but we'll end up with this one.
*  Did we settle anything?
*  I mean, I'm still totally open to us discovering things from neuroscience that will be useful for AI.
*  I just think that we have to keep in mind that in order to be able to recognize some discovery as being useful in the first place, you need to be able to computationally implement it right.
*  And you need to be able to recognize the computations in the first place.
*  It's sort of like if I just stumbled upon a Turing machine on the sidewalk and I didn't know anything about Turing machines, would I be able to, you know, understand a Turing machine just from from like handling this artifact?
*  Like maybe that's possible in principle, but it would be extremely challenging.
*  And so I think the same is true for neuroscience, maybe even more true that we have to just start with it.
*  We have to go into it with computational principles in order to be able to recognize anything in the first place.
*  And so the process of translating from neuroscience to AI is more a process of kind of, as I said,
*  upgrading the discoveries from neuroscience and the models from neuroscience as opposed to like this sort of naively empiricist mode of discovery where we find some biological phenomenon and plug it into our models.
*  And all of a sudden, our models are going to be much more powerful.
*  Chris, I have one question for you. I hear the baby crying.
*  From the deep learning is the answer paper.
*  So one of the things that you guys write about is, you know, using idealistic, reduced, deep, deep models so that we can conceptually understand what's going on.
*  And this goes back to understanding.
*  And I'm wondering if do you think our conceptual insight will ever catch up to the complexity of what we can build and use?
*  Will that complexity forever be a couple steps ahead while we're trying to look at that huge model, reduce it into an answerable question for our understanding?
*  And that's how we advance our understanding.
*  Well, I guess the messy real world is always ahead of our idealizations of it, right?
*  That's just a general principle.
*  But I mean, those idealizations, I mean, hopefully they're useful for lots of things.
*  One of the reasons why I think it's a great time to be a cognitive scientist or neuroscientist is precisely because there is this reawakened interest in models that kind of learn by themselves.
*  Right. So it means that the dynamics of learning, the ways in which we learn, the ways we can accelerate learning, the structure in our learning, like all of these are viable questions in a way that they were not when the state spaces of our models were entirely populated by hand.
*  And that's the opportunity that my lab has tried to seize and to study at small scale, but to study for its own sake.
*  Right. I mean, these questions clearly may have resonance one day, probably not in my hands, probably in Sam's hands, but may have resonance for AI one day.
*  But for me, really, the goal is just to understand the principles of learning, use these tools, these networks as tools for understanding principles of learning per se as a research topic.
*  Thank you, Sam. Thank you, Chris. We'll see how this turned out, but I really appreciate your time and just the open sort of dialogue here.
*  Thank you. It was fun.
*  It was lots of fun. Thank you, Paul. Sam, really nice to see you.
*  Yeah, we'll catch up soon.
*  All right. Take care.
*  Brain Inspired is a production of me and you. I don't do advertisements. You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes, plus bonus episodes that focus more on the cultural side but still have science.
*  Go to BrainInspired.co and find the red Patreon button there. To get in touch with me, email Paul at BrainInspired.co. The music you hear is by The New Year. Find them at TheNewYear.net. Thank you for your support. See you next time.
*  Bye.
