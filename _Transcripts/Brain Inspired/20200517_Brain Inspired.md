---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 6429s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 7806
Video Rating: None
---

# BI 070 Bradley Love: How We Learn Concepts
**Brain Inspired:** [May 17, 2020](https://www.youtube.com/watch?v=qsghTg4XJRg)
*  I think people thought I was crazy when I was doing this because like when you think of brain model, you think it has to have like sort of like a lot of complexity to it.
*  This is really like a simple cognitive model.
*  We used to sit around in graduate school like in the late 90s and with professors and students and talk about the big picture.
*  Everybody thought it would be 200 years before we had any models that could like do object recognition.
*  This is Brain Inspired.
*  Hey everyone, I'm Paul Middlebrooks and today I speak with Bradley Love.
*  Brad's a professor at University College London and a fellow at the Alan Turing Institute.
*  You'll hear he has a lot of interests.
*  One of the things he's worked on for years is a model to understand how we learn and store concepts.
*  You may remember I had Rodrigo Quienquiroga on recently who discovered concept cells in the Human Hippocampus,
*  which respond when someone is presented with a specific concept no matter how that concept is presented.
*  So if that concept is Bradley Love, it could be a picture of him taken from any angle, it could be his written name, and so on.
*  And after today, after you learn about the sustain model that captures how concepts are learned
*  and that maps onto particular brain regions encoding these concepts,
*  your concept neuron for Brad will fire when you think of the sustain model.
*  How meta can you get?
*  So we talk about concepts and his now decades-old model that keeps chugging along.
*  We talk about his cognitive modeling approach to understanding brains and intelligence.
*  And we talk about some of his recent work integrating deep learning models into the study of concepts,
*  plus a few of his other deep learning projects.
*  It's a long episode, but it actually was even longer.
*  This is the first episode for which I saved a segment just for Brain Inspired supporters on Patreon,
*  which I'll start doing more often and posting some extra bonus episodes for Patreon supporters as well.
*  So if it sounds like this episode cuts off a bit abruptly at the end, that's because it's missing the last half hour or so,
*  where we discuss Brad's outlook on AI and some of his wisdom and advice from his own experiences.
*  Eric, Johan, Byung, Rosalind, Howard, and Dennis, or Denny,
*  thank you for your recent support on Patreon, and you can expect that bonus episode very soon.
*  Find show notes at braininspired.co, where you can also learn how to support the show for super cheap.
*  This was a fun episode for me, and I hope that you enjoy.
*  Brad Love.
*  Brad, I have inspired you to actually connect your analog guitar and microphone system board to your digital Mac computer finally,
*  so you're welcome.
*  Thank you. You're the only one that apparently could get me to do this after sitting around a year,
*  so I'm indebted to you before the show even starts.
*  What's our band name going to be?
*  Brainiac's already taken, so I don't know, Brainiac Jr.
*  I think Joseph Ledoux has a band, I think, called the Amygdaloids maybe. I don't know if you've heard them.
*  Yeah, I've heard of them for sure. I've probably heard them too.
*  A couple of times I had the pleasure of making a guest appearance in another cognitive neuroscience band, Pavlov's Dog.
*  Oh, man. That's awesome.
*  I'm definitely not a musical person, but years ago I enjoyed playing in a scrappy lo-fi band as a hobby,
*  but that fell by the wayside, but maybe in lockdown, since you've inspired me to hook this up, I'll dust off the guitar.
*  But you are sitting there with a Fender shirt, t-shirt on.
*  I can see a Fender guitar or at least an electric guitar in the background, so I'm ready, man. I'm ready to go when we're done here.
*  All right. I better keep my day job.
*  Yeah, well, I don't have a day job, so I need something.
*  So, Brad, anyway, welcome to the show. It's good to have you on and thanks for being here.
*  Thanks so much for having me.
*  There's a lot for us to talk about, and I thought we might just start with your kind of philosophical approach to neuroscience and cognitive science.
*  I call everything neuroscience, by the way, so hopefully you can get used to that.
*  So, your philosophical approach and tying it into the whole idea of Mars levels and approaching cognition and neuroscience through different levels.
*  So, I don't know, how would you just describe your philosophical approach to studying intelligence?
*  I don't know if I can ask a broader question than that.
*  Oh, no, sure, sure. I mean, maybe I'll like jump into like the neuroscience approach first, but yeah, I mean,
*  I've always been found working with computational models very helpful just for organizing my ideas.
*  And, you know, they could also surprise you with a actually predict, which is really what you predict, you know, what your theory predicts.
*  So if I kind of found that formalization process helpful, in particular, I found it helpful to work with relatively simple models that I refer to as cognitive models that would be at Mars algorithmic level.
*  So, you know, like really briefly, and I'm sure your listeners know, but like, you know, computational level is the top level.
*  That's sort of the what, like what's the input output function and the algorithmic level is like how, you know, how do you, what steps do you go through, what processes and representations do you use?
*  And of course, below that's the implementation level, which is like the where.
*  But I found working with pretty simple cognitive models helpful to like kind of distilling the basic principles I'm interested in.
*  And I found them to be like a really useful lens on brain data.
*  Like so we've done with like really good collaborators like Tyler Davis and Ali Preston and Mike Mack and others like work using these models to link them to like bold response and fMRI.
*  So it makes it a little bit more theoretical because you kind of take this more like top down view on the data.
*  It could be really useful for capturing like processes that you think are happening through time within a trial or across learning trials.
*  So it's sort of like a middle out approach, I guess, would be the philosophy.
*  It's not really starting from the top or the bottom, but somewhere in the middle as a bridge between like the higher and lower levels.
*  So the idea that there's just there hasn't been enough theory in neuroscience.
*  I don't know. I've been hearing that a lot, maybe over the past 10 years.
*  I'm sure, you know, who knows really when it started becoming more and more vocal.
*  But I feel like just as an observer, I see a ton of focus and focus on and celebration of higher levels within Mars level.
*  So either on the computational level or on the algorithmic level, especially these days, it seems like the algorithmic level, you know, is the right way to approach this.
*  Or at least it's celebrated as such.
*  I mean, do you think that the algorithmic level has gained too much celebratory acceptance?
*  You know, from my perspective, it's like the recent 10 years have been like, oh, poor brains.
*  They often seem completely left out of this this whole endeavor.
*  I mean, I'm not sure if you just look like not so many years ago, like in the 2000s, it was like quite the opposite.
*  Right. Like so that was like in terms of more cognitive science, rational vision theories that are at the computational level were all the rage.
*  So at that level, there actually isn't any notion of mental process or representation.
*  And if you look at cognitive neuroscience, I mean, there was so much like, you know, there's interesting work, but it's like largely like, you know, f m right biology where like, you know, you're just doing these contrasts that aren't linked to any like cognitive model at the algorithmic level.
*  So, I mean, if there's been this like rise in interest in the algorithmic level, you know, it's fairly recent because I mean, definitely then most of neuroscience wasn't model based and most of computational modeling was like Bayesian rational.
*  But it makes sense that, you know, to bring these things together, you know, you know, it's a lot of people would say you want to have like multi level theorizing.
*  So it makes sense that people would get interested in the how of cognition to kind of link things together.
*  So I don't think the brains, you know, you know, being left behind.
*  I mean, I'm certainly interested in using constraints from neural measures to inform the cognitive models.
*  But the cognitive model is really let you see things in the brain data that you couldn't otherwise reveal.
*  So like almost in every study we've published, if we just do a standard contrast or something like, you know, we don't really see much that's interesting.
*  And it's really like the models are helping to reveal these things that aren't like, you know, super obvious because most of what we're interested in are like theoretical things like even like error correction, you know, updating these are like theoretical things.
*  You need a model to characterize or recognition strength or familiarity like you need like they're changed through time both within a trial and across trials.
*  If you're looking at learning studies.
*  So I think the models are really allied with the neuroscience.
*  You've been so you have this sustained model that will eventually talk about here and you've been working on using this model and applying it to brain data as well.
*  And, you know, sort of mapping on its processes to hippocampus and prefrontal cortex.
*  And, you know, we won't go through the whole thing right here.
*  But so you have used your algorithmic level approach to to map on to the implementation level as well.
*  So, I mean, this is something you've been doing for a long time.
*  You know, you just you mentioned the Bayesian approach and you've actually been in the past been critical of the Bayesian brain idea like you were just talking.
*  So the Bayesian brain ideas that brain circuits represent and process and process information as probability distributions.
*  Right. So, you know, it's often used as a normative approach without enough connection to actual brain processing is sort of a rough and dirty summary of in your brain and behavioral sciences article.
*  But so that was a little while ago. Do you think that the Bayesian approach has come down from the strict computational level?
*  And has it gotten better since you suggested it wasn't connected enough with the algorithmic level?
*  You know, I think I don't want to like pat myself on the back.
*  But, yeah, I think I think so. I mean, I think I think it's got more interesting.
*  So like, I think we were a little bit like misconstrued.
*  We were never like anti-Bayesian.
*  And both Matt and I like published papers that take Bayesian approaches and sort of like the sustained successor that's like under petrol review with Kurt Braunlich is like has the same basic principles as the original model.
*  But it's like in like a more Bayesian formalization.
*  Well, I guess what we're really critical of is just leaving behind the other levels of analysis, because really, if you stick to the computational level, you're just leaving behind like so many constraints, like everything about the how of cognition and the neuroscience.
*  I mean, just loads of other things, other endeavors as well.
*  So, you know, there's nothing like wrong with like or even or special with like Bayes rule.
*  So you could have like an algorithmic model, which, you know, is Bayes rule.
*  You could say that's actually like the process people use.
*  That's actually the representation people use.
*  So even those models don't have to stick strictly to the computational level.
*  Yes, that's really what we're critical of.
*  So there's not really any like strong claim that like the brain doesn't keep track of uncertainty or probability distributions or anything like that.
*  It was really like an appeal to like kind of, you know, leave this sort of rational perch and like get down and dirty a little bit with psychology and neuroscience down and dirty with psychology and neuroscience.
*  You might have just written the title for this episode.
*  We'll see.
*  So tied into this idea of levels.
*  So there's Mars famous levels that we've just been talking about.
*  But a maybe complementary approach, I want to say, is the mechanistic account.
*  This is most recently probably.
*  Well, it's been written about by Carl Kraver and William Bechtel.
*  And basically to approach neuroscience and cognition, cognitive science, using a mechanistic approach to really just to summarize it.
*  A mechanism consists of parts of things and those parts operation and their organization together with the constraints that like the environment imposes and what kind of environment it's in.
*  But the idea is that when you break a process down into its mechanism, that the mechanism actually can bridge different levels of of Mars levels.
*  So hierarchically, you can use a mechanism to look at a level above, look at the computational level, for instance, and look at the level below.
*  I mean, do you see merit in the mechanistic approach?
*  And, you know, do you think it's complementary with Mars approach?
*  Yeah, no. Interesting question.
*  Yeah, it seems like the levels of mechanism approach is well suited to neuroscience.
*  I mean, yeah, I mean, if you think of something, yeah, like you said, like, you know, like a car or something, it has components like an engine and brakes and a radio and all those components, of course, can be like decomposed themselves.
*  Right. So you could the engine has a lot of components.
*  But what's I think what's nice about it, maybe for scientists, is that it's just because you're talking about a car at the level of car, like something like higher level.
*  It's not like you say, oh, that's not real because you're describing the engine just in terms of torque and horsepower not going into all its components.
*  So I think, you know, it might taking that sort of like language might like do away with some like conceptual confusions and and science.
*  And it kind of moves people towards away from laws and thinking about systems.
*  I think one thing in terms of whether it's complementary to Mars levels, I think one thing it kind of leaves out is the computational level, because the computational level is not really like a computer.
*  The computational level isn't really concerned with mechanism.
*  It's concerned more with like the problem description, like what's the input output mapping, like literally like what's the function you're trying to solve.
*  So like if we were doing like sorting, it would just be like description of the problem, sort the numbers in order.
*  Whereas the algorithmic level would be like what's you know, what's the algorithm, what series of steps you go through to sort the numbers.
*  So I don't really know if that's like really like present and the levels of mechanism so much.
*  But the way I've read it described is that it is actually separate from sort of the computational or functional in terms of the levels of mechanism nomenclature.
*  It would be called the function. Right. And that function and mechanism actually mutually inform each other.
*  So there is a distinction between if you want to equate function with computational level, there is a distinction in this literature of the mechanistic levels approach between function and mechanism.
*  But that they mutually inform each other.
*  Oh, yeah. No, no, I could I could see that. But like it seems like the computational level.
*  I mean, I think maybe I'm just being like too strict. And of course, like I should go through this more carefully.
*  But, you know, it's like I mean, it's really if you have a computational level account, you really have to like characterize the full range of like possible inputs.
*  And like, I'm not sure, like, you know, people working with mechanisms are thinking about that.
*  This isn't really at all a criticism of it. I mean, there's almost like this sort of kind of like teleological thing to the computational level, like what's the purpose or this.
*  And like, I kind of like taking that perspective sometimes a step back.
*  But, you know, it could be like a creature of the human mind that this level.
*  But I mean, I think it could be a useful perspective to take from time to time.
*  But but yeah, I mean, what I like about the levels of mechanism to that you mentioned is that like you don't really have these sort of monolithic levels like, you know, there's just no end in sight.
*  So you realize there is no bottom to it. So I think it could reduce some chauvinism and levels.
*  And it makes clear, I think, you know, what people are trying to explain in terms of the how much they unpack the mechanisms in terms of the constituent parts.
*  Yeah. Yeah. One way that it's been put to me and this was from John Crackauer, I think a long time ago now.
*  And I don't remember if it was actually on the podcast or I met with him and had a beer and it might have just been over a beer.
*  But he didn't say specifically this with respect to levels of mechanism.
*  But we are talking about Mars level, which he's essentially a proponent of.
*  And he was suggesting that a lot of people make the mistake that you, you know, of applying Mars levels to like size in the brain.
*  Right. So implementation is like neurons.
*  Whereas the algorithmic level we need to think of as bigger circuits and then the computational level is like a functional brain or like the functional.
*  So it's maps onto these like physically larger things.
*  And his point to me was that you can apply Mars levels at at every single different level of physical size.
*  So in that sense, with the levels of mechanism approach, the one way it could be complementary is at every level of mechanism, you can still apply the three sorts of Mars levels of analysis approaches at each level.
*  So I'm not sure if that makes complete sense.
*  Yeah, I mean, like Mars levels, I mean, I find that they're still like helpful in many ways for like understanding one's contribution.
*  But yeah, it makes sense to, you know, try to slice them more or apply them in particular context like you're suggesting, because I mean, you can't just like lump all of neuroscience into like one level.
*  And I mean, Mars levels are really sort of like, you know, borrowed from abstraction hierarchies and computer science and, you know, where the top level there would be like the application, the bottom level would be like below circuits to like physics pretty much.
*  And so there you have like so many like levels you could, you know, traverse along the way, way more than three.
*  And so you see how they're all like how they're all related and how there's like more of a richness and detail as you descend.
*  Yeah, so it makes sense that like, I mean, I think it's just like a good guidance to think about like what your intellectual contribution is.
*  And yeah, so it makes sense that that's not like where you'd want to stop like you're suggesting.
*  You think both reduction and emergence are misguided as as concepts.
*  So, you know, what are your views on emergence and reduction if you had to sort of boil it down?
*  It's funny you ask, like, so I kind of want to have my own little like personal intellectual like Odyssey like writing a recent paper that's like just putting the final touches on it before it hits print.
*  And like a lot of what I believe before writing the paper like change, because I think like a lot of times you're like, oh, emergence, that's cool.
*  It's like, you know, it's like the anthill.
*  It just happens.
*  And it's really it's how things work.
*  It just emerges.
*  You know, we don't things that don't just emerge aren't really interesting mechanisms or models or reduction.
*  Oh, that's really bad.
*  It's just like, you know, you just got to be more open minded.
*  But if you really think about these things like emergence, like how people say it, it doesn't really make a lot of sense.
*  And a lot of what people describe as emergent just really isn't like so if you take things like Sully or Tomada like Conway's Game of Life from the initial conditions, it could generate all these like fascinating patterns.
*  But there's really just simple local rules and being applied that are generating them means obviously being simulated on a computer.
*  And likewise, if you think of flocking behavior with birds again, like each little agent has some simple rules of behavior that apply locally.
*  And so when we say it emerges, we're just really saying we're not that smart and we can't like simulate the whole thing in our head and appreciate it.
*  I mean, it's sort of like saying if I bump my mug of water and it falls off the floor, it's like, oh, the glass broken emerged from me hitting it and it fell.
*  It's like, no, it's like I could appreciate this.
*  And like if we took a space alien, you know, that was like way smarter, it'd be like nothing emerged, you know, in Conway's Game of Life or the flocking behavior.
*  And basically, if you could simulate it on a computer, you're like breaking it down to like the components that are generating whatever the higher level observed behavior.
*  And so it's like the higher level behavior is like completely like reducible to like smaller elements interacting.
*  So like, yeah, I mean, we could use that in like common language, but I think it's like a little slippery and it could lead to like conceptual confusions.
*  I mean, like I had the pleasure as an undergraduate of like briefly studying under a Jaguankin, this like philosopher of mine that introduced this really useful notion of supervenience.
*  There's many varieties of it and they're all formalized like really well.
*  But like the basic idea is like if something supervene to something else, you can't have a change in the higher level thing without some change in the lower level thing.
*  So, you know, you couldn't have like a change in mental state without some change in physical state.
*  And that's pretty common sensical unless you believe in like ghosts or something.
*  But when you start talking about emergence, you're going to have like, you know, mental states like causing mental states and then you like then what's the physical states aren't causing them or you have like overdetermination.
*  Like you have like two causes or you get like downward causation, like all these really weird things if you actually like work through it and think through it or read literature.
*  I'm not expert in and philosophy. It just it just kind of leads to like a little bit of incoherence or at least debate debate, you know, like, whereas if you just kind of stick with it's practically emerging, you know, it's not really emerging.
*  It's like I just it's just like a limit of like human cognition and our ability to analyze data or the quality of the data as opposed to things aren't reducible.
*  I mean, by the same token, like reduction is like sort of like this strange bias scientists have because usually things really I think scientists confuse that things like probably can reduce all the way down to like particles like everything is like at some level physics.
*  I think they confuse that with that is practically possible to do or even desirable because it's not like right now we're like, oh, how do we help small businesses in this economic crisis? Let's talk to a particle physicist, you know, like you would never do that.
*  I think I think a particle physicist would beg to differ because they believe they have a solution to everything. Right.
*  Oh, yeah, of course. We just of course, I guess there's an icing model for it or something. But like I just met like I guess it's the wrong thing because maybe they could actually help but not by like modeling it like quirks and stuff.
*  Right. But yeah, so I think people confuse that. And like so I mean, there's a reason like neuroscience itself is like a higher level discipline, even the lowest level parts of it. Right.
*  And it's not going away. And like economics isn't going away. Like all these fields aren't going away because they're like useful and practically we can't reduce it. It doesn't mean like in principle, like it's not possible or like some super intelligent, you know, agent couldn't reduce it down.
*  But practically speaking, it's just not reducing and like most of neuroscience isn't like formal or understood enough to reduce anyway. So I mean, I just wish we had said we would just kind of focus on what people are trying to explain.
*  Like what's the relevant data where the relevant findings and how good of a job they do like actually explaining that data and then like a lot of these like sort of debates, even discussion of levels, a lot of it just kind of melts away by just being a little bit more clear about those things.
*  My own personal comfort level as a neuroscientist, like I decided at some point, okay, I don't, I feel comfortable not worrying about membrane proteins at synapses and their kinematics. And so I don't need to understand it at that level, even though someone who studies that could say, well, you know, we wouldn't have thoughts if we didn't have membrane proteins at synapses.
*  You know, it's like, that's my favorite thing of any sort of explanatory go to. It's like in any sort of documentary, it's, you know, it's like water. We would not exist without water, you know, and it's always like, oh, my God, it must be the most important thing ever.
*  Water. It's very important. It's true. You know, so particle physics, we would not, you know, of course, you can explain it. You can reduce anything at to a certain level. But your view, so then on emergence is basically emergence is a our way of describing things just at the level that we can understand things and describe things to make sense to us as humans because we cannot simulate every little minute detail.
*  So we have to be comfortable with a certain level of description. And that's sort of what emergence is.
*  Yeah, it could be like so. Yeah, basically, there's sort of like this weak, weak emergence or like a practical emergence or like maybe a philosopher called like epistemic or something like where it's exactly what you said.
*  It does. It's not like saying things don't reduce down to like something lower level, like in principle, it's just saying like, you know, practically, we just can't do it because we're not smart enough. We don't have the right data or the right tools.
*  Yeah, so I think people should be careful. A lot of times it sounds like they're making a stronger claim about like the world or like, you know, the brain or something. And as opposed to a claim about where we are in our science.
*  Okay, so one more thing before we move on here to concepts and switch gears. You don't like the term biological plausibility. I'm not just trying to, you know, bring out all your qualms here. But you don't like that term conceptually. What would you replace it with? Why don't you like it and what would you replace it with?
*  Boy, I really don't like a lot of things. It's like, no, we can talk about lots of things that you like. Yeah.
*  No, I just like more things than I like. You've picked up on that. No, yeah, I think. Yeah. So yeah, recently this recent paper I mentioned like levels of biological plausibility. Yeah, just basically state the reasons why I think it's a completely like vacuous misleading and incoherent concept.
*  I mean, what I guess what are we really studying like stepping back like we're trying to determine what is biologically plausible. So like just asserting it is almost like assuming the answer. But I think worse than that. It's just it's really something in the eye of the beholder.
*  And again, like what I was emphasizing before, one really has to be clear about like what findings and data they're trying to explain. So I give this like example in the paper, like imagine you have this one model, this deep convolutional network and explains activity along the ventral stream like really effectively.
*  And so they're like, hey, we're biologically plausible. We explain the ventral stream activity and these other people are like, no, our models like biologically plausible because we don't use back propagation.
*  And our learning role is consistent with pyramidal like cell activity. And it's like, okay, so are they both biologically plausible is neither. They're both justifying their publication in terms of biological plausibility.
*  What's really going on is like, it's like, they're basically care about different data sources or findings. And they're explaining the data they care about, which is fine. They're basically like, so why don't we just like be a little bit more forthcoming with that and just say we're doing model selection.
*  Model selection is very top down. You select the findings or even the data you care about. And then you could actually select the best model for that data. So basically the two groups in my example are doing like different model selections on different data sets, different aspects of neuroscience.
*  And so like, what is biological plausibility? It's nothing more than explaining the data you care about the best. So it does no work beyond that. So it's just really misleading. And it's been like, abuse their time. I mean, I kind of like resonate to the idea of making things that are biologically plausible.
*  Like who wouldn't? It sounds good. But then I kind of realized reading papers, a lot of papers, not all, some are great, but are just like really junk. And they're like, publish this paper is great because it's biologically plausible and it's better than that model. It's not. I'm like, why? You know, what is biologically plausible about your model? And it's like, sort of face validity almost, you know, like so in the 80s, it'd be like connectionist models were biologically plausible because they had like a lot of little things in them. And the brain had a lot of little things in them. Whereas like production systems,
*  weren't because like, you can't open up the brain and see like a lot of rules or something. But then, you know, like subsequently, like what is like, John Anderson and his colleagues do like they apply like act our production system to explaining bold response, doing mental arithmetic. So now is that model like still not biologically plausible? You know, so I think it's sort of like contrary to multi level theorizing and just like, whatever, just specify the relevant data sources that you're evaluating yourself against.
*  You know, do some model selection and let's just like leave these like that. It's like not a helpful label. I don't think it's a it's a badge that people wear to to elevate, I guess, their research perhaps. But, you know, it's interesting that you you use back propagation.
*  And and maybe this is where like, so there's this big back and forth now in back propagation specifically of whether it's biologically plausible. And maybe you've hit on the point that so on the one hand, the idea of supervised learning and that synapses can can adjust based on some feedback signal, you know, is fine. And in that sense, quote unquote, backpropagation is biologically plausible. But, you know, on the other other hand, we don't have these symmetric models.
*  But, you know, on the other other hand, we don't have these symmetric connections between neurons. So backpropagation as it's done in connectionist, you know, networks is physically impossible because it doesn't exist in brains and therefore is not biologically plausible on that level. But these two things are are somewhat addressing different different levels. Like you said.
*  Yeah, I mean, it could be different levels or even just different aspects of data at the same level. Like, like when you make a model or a theory of something, you don't try to explain everything about the brain or behavior. And so like, it's totally fine to have like a theory of the ventral stream and just be like, well, we're not explaining why the connections aren't symmetrical, you know, but we're explaining like these aspects of the data or findings or because no bottle explains everything about the brain. So yeah, so I just think this like,
*  labels unhelpful because it makes it almost like you are you aren't it's almost like a way to like rule out approaches when no approach explains all the data anyway. So like, if we just do this enough, we could make everything not biologically plausible.
*  Yeah, yeah, I mean, I guess it also depends on how you define, you know, backpropagation in this, in this context. But, you know, there's also a lot of back and forth about what deep learning is. And there are people who practice deep learning that have a definition. And it seems like the definition changes to include more and more things. And people, you know, there's a new finding and people say, well, that's deep learning. You know, there's a new finding in the brain. Oh, that's deep learning. And so, you know, there's a new finding in the brain.
*  And so deep learning deep learning covers that. And all of a sudden, somehow the deep learning definition expands. And so in the end, deep learning wins somehow, you know, so I don't know, back and forth.
*  Oh, no, definitely. I mean, this is like, I mean, I'm not even that well and this has been going on my entire life, you know, like, so it's kind of getting into this. It was like connectionism was like the sort of like Uber theory. But of course, like connectionism isn't a theory, you know, it's like a framework for building
*  theories and models. It's like saying my like, I have a theory, it's called Python, you know, it's like, and then of course, Bayesian models aren't a theory. It's like, again, it's like a really broad framework for building models and theories. And so I mean, deep learning is just the same.
*  I mean, it's not really, I mean, it has some like associated characteristics, but you could build like very different deep learning theories of like the same like phenomenon. So like, it's not really, obviously, it's not really a theory. That's not like being negative. I mean, it's amazing. And you could build amazing theories from it. It's just not a theory. It's like a framework tool, a framework. Yeah.
*  Brad, you really don't like polka music. Why do you not like? No, I'm just kidding. Let's talk about something that you like. So I just I just interviewed Rodrigo Kian Kioroga, who is sort of famous for discovering concept cells. And we talked a little bit about, well, a lot about concept cells and also about lots of other things in this recent book.
*  I really dislike friends. Sorry.
*  Yeah. So just just to sort of recap, though, concepts and concept learning has been your bread and butter for a long time now. And, you know, you've like I said, you had this sustained model that models how we learn concepts, how they're formed and how they map on the brains and lots of other things. But so so I'd love to just talk about concepts and concepts learning. And maybe you can just define what a concept is for people who missed it last time.
*  Sure, sure. I mean, hard to do. So concepts, I mean, you could tie it to generalization, which, of course, every creature that has to make decisions does like, you know, like a dog generalizes, it has a concept of its owner if its owner changes her clothes or haircut, like still the owner. I mean, the way I think about concepts is that it's you know, it's not at any particular place in the processing stream, but it has to be at some, it's some kind of intermediary between
*  perception and action and it has the ability to somewhat decouple from both. And so like what I mean is like, if you think of something like a zebra, if you like remove its stripes, you're changing sort of like your perception of it, but you know, it's still a zebra just because you you know, you painted the thing you have some concept of the zebra that persists. Likewise, if the action you have to take in regards to something changes, like say yesterday, the the price of oil like went to negative 40 US dollars like in the US. So like,
*  there becomes something like, oh, I'm gonna pull this out of the ground and sell it and get rich. And it's like, oh, god, I got to pay someone to take it away. It really changes like how you view it and deal with it. But you're still oil, it's still the same concept of oil. So it's sort of like this nice intermediary that could link perception and action by and decouple them in some ways as like the perceptions and the relevant actions change. So I guess in like, I mean, I guess in terms of like you mentioned sustained in terms of like,
*  clustering models, all these models, again, some like intermediate representation. So in that model, it has clusters that collapse together related experiences. And so you could think of those as the concepts in some sense that like identify sort of the relevant perceptual chunks and link them to responses, naming, for example. So like, it wouldn't confuse concepts with words, you know, you can have many different sort of little conceptual chunks that map on to the same
*  name or the same action.
*  Well, so concepts in general, though, are kind of an abstraction then from, like you said, from sensorial perception and from actions responses related to the perceptions. So in that sense, I don't know, it seems like a very high cognitive human skill, like where where would you place abstraction in the, you know, in the hierarchy of human abilities?
*  I would place it nowhere special. I mean, like, again, like every, every animal that makes decisions has to do this. So like, I mean, yeah, I mean, just like I said, like your dog dogs have concepts, pigeons show peak shift behavior, you know, like, where you kind of generalize the pattern, because I mean, what I'm saying is just like kind of sort of like psychology 101. But like, you know, we never really run across the same exact situation or stimulus twice. So like, I mean, got to have some, some notion. I mean,
*  I don't know. I mean, people could probably link this up with more. I don't think exactly meps on with more like sort of model based learning. I mean, I don't think it's like really special human ability.
*  But so are there are there different just pushing on this a little bit because Rodrigo, you know, is pretty adamant that concepts and like super abstraction sort of lead like you said lead to generalization and and that our level of abstraction or maybe our level of creating concepts divorced from their perceptions and actions and their connection with lots of different areas in our brain, lots of different
*  functions are what give rise to our special human experience, right? So are there different levels of abstraction that still count as concepts, right? So we have maybe different levels of abstractions of concepts.
*  Yeah, no, that's, that's a great question. I mean, certainly, like, I don't want to, like, devalue that people have a reasoning and abstraction abilities, you know, that aren't seen in other species. But I just don't really see them as like, maybe we just got like a couple of the levers and knobs turned exactly right to like, you know, eke a bit more out. But it doesn't seem like there's really like a qualitative like a huge step. I mean, people argue about this forever. And there's there's BBS,
*  papers about this. But if you look at our abstract reasoning abilities, they always have remnants of like more concrete knowledge or processes. And so for example, if you teach people some rule, they could state the rule. But when they apply the rule, it'll be affected by the similarity of the test item to the previous training items. People could do abstract reasoning like deduction, but like how often they make errors as a function of how believable the conclusion is, which has nothing to do with logic.
*  Right. So abstract reasoning, if this then that if that then that it shouldn't matter what the P's and Q's are in the but it does and how well people reason that's why people you know, like Chang and Hulig talk about pragmatic reasoning schemas. I think that's like from way back in the 80s or something.
*  But everything's like this memory retrievals like this. So like, why don't we make really distant analogies, you know, like you have all these great analogies in the history of science, but in practice, like, we always just make analogies from like, the domain we're working in to the same domain and one really next to it because memories guided by like surface features that guide retrieval, right? Like, so that just, that's usually what's relevant. So like, all these things are very, there's very concrete underbelly.
*  To like our abstract symbol processing, it's all highly contextual. And like, so even like when you do some kind of variable binding, if you think of it that way, like, like, if someone says, I love my child, I love chocolate, like love just changed meaning, you know, based on like, what the what took that slot, if you think of it that way.
*  I'm not saying we can't do like symbol processing or abstract reasoning, but it's not actually really that abstract. There's always sort of this underbelly, which suggests it's not completely like, completely abstract in some sense or divorced. Maybe we just have like, you know, we just got like, not like the secret sauce, but just like the settings like a little bit better just to get a little bit farther than like other animals. But it doesn't seem like a night and day thing. And yeah, to me.
*  Yeah, I mean, this is, it's an interesting question, whether adding just a little bit more of something fundamentally changes the nature of what you can do with that thing, right? So you're talking about symbol processing and, and, you know, we have language, and that is a very uniquely human thing. And is there something qualitatively different about the way we process that enables us to have language? The way that I see it? I barely have language, I barely have
*  processing, you know, I don't know how you feel about about it. But it's not like we have opened ourselves up and can explore this eternal new space of processing with symbol processing, for instance. To me, it's very easily conceivable that we are still, like you said, using the same sorts of processes and grounded in that same, you know, evolutionary system, essentially, and not doing that much different, but it's a it's different enough.
*  That there's a different quality.
*  Yeah, no, I mean, that's the way I view it. I'm sure like late some language people get very upset with me. But it's just, you know, it's like another like representational format you could use, or it's like another cue to meaning. A lot of times when people like kind of invoke language, you could actually disrupt their processing. So like in learning studies, you know, you ask people what they're doing, and they convert what they're actually doing into a description, and they start doing their description, which is actually like maladaptive.
*  So I mean, it's not like, I mean, yeah, language could be useful. Obviously, we were using it right now to communicate. I mean, I don't know if it's correct. But like, I think a lot of what drives people, I'm sure there's like special things about our brains. But it's also like, we've built these really like complex environments for ourselves that I think spur our development. And we have these great ways of like, building on the complexity from other other people have figured out and passing it along.
*  So I mean, it's sometimes right, like the convolutional networks, why do they work? Okay, but not perfectly. Now, it's because they have these like, like richer data sets to train on. And, you know, if they had more tasks to do, people are exploring things like self supervised learning, more auxiliary tasks to do with it more ways of interacting, basically ways of just linking things together, making it richer. I think that is a lot of what drives like intelligence is not the device, but like the, the input.
*  And the interaction and the richness of it, you know, it's like, you can't really have like, someone becomes super smart, that gets no interesting input or has no interesting interactions with the world. So I think we discount that we always think about like, the device and not sort of the whole like world it's embedded in and how complex the world is that we've made for ourselves. You know, that's all like, you know, crashing down a little right now. But you know, we build these really, really complex environments, and we have really complex social interactions with
*  each other. And it just builds and builds over generations. And so I mean, that's not the whole story, but that has to be part of the story of why we're different.
*  Okay, so just getting back to concepts, because we could we could talk about our unique human abilities and what is unique and what's not we could talk about that forever. So, but let's take a step back. You know, like I said, I just talked with Rodrigo about concepts. And, you know, he
*  found these concept cells and hippocampus, Jennifer Aniston neurons, as people like to call them. And we'd already know, as you mentioned, you do not like friends. However, these concept cells do exist in the brain, you know, you record the cell and it responds to just invariant representations of, in this case, a person Jennifer Aniston, no matter if you write her name or show her picture, she could be at any different orientation, etc, etc. But what we didn't talk is about how those concept cells come together.
*  How do concepts come to respond that way? In other words, how concepts are learned? And that is something that you've been working on for a long time with your sustained model, which I've already mentioned a few minutes ago. But I wonder if you could just kind of take us through, you know, what the sustained model is and how it addresses how concepts are learned and how they're updated and even stored.
*  Sure, yeah, it'd be my pleasure. I mean, so yeah, this work goes all the way back to the, to the 90s. And the idea was to build a model that could move between two extremes. So on one extreme, you have a prototype representation where you really just have like, one node and memory for like all your declapses all your experiences of a category together. So like you'd have one node and memory for birds. The other extreme model would be the exemplar model, where you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a model of a bird, and you'd have a
*  You would store like a node and memory for each experience. So everything would leave a trace, it would actually be no abstraction in memory. Instead, you do the abstraction at the time of decision by like activating all these traces. So clustering models like navigate those two extremes. And the key to them is like, well, when do you collapse information together and you know, store it, you know, form some kind of abstraction. And the way sustain works, it seems like how people do
*  more and more like over the years, including the level of like brain activity, is that it seems simplicity. So it basically assumes that experiences like collapse together or somewhat, you know, like average together in memory until there's some kind of surprising prediction error that's relevant to the task you're doing, you know, so the example I always use in talks is like, you're learning about birds and mammals, and you see a bat for the first time, and it's small, and it has wings and flies. And
*  so you call it a bird, but that is surprisingly incorrect. So now you make this new node, you know, like centered on that error. So now that could like kind of evolve into its own kind of bat concept or prototype.
*  How does that map on to the idea of a cluster?
*  Yeah, so those these little nodes are the clusters. So the clusters are just, well, they're just representations in your head that are like running averages of the running information. So like, the key is, there's really like two kinds of updates. When you have a new experience, you could either have like, kind of an incremental update, like say you have a cluster for cows in your head, and you see a cow that's 2% bigger than your cow cluster, you know, so you'll just slightly
*  adjust your expectation upwards of how big cows are right. So you just adjust that incrementally adjust that cow cluster, there's no real surprising error there. Whereas if you have some kind of like serious prediction error, like, like we mentioned with like realizing bat is not a bird, then you'll make a whole new node basically memory a whole new cluster. It's really interesting. It's not published yet, but it should be a pre print soon like working with Mike Mack. He actually we actually ran the same
*  study that was like, so crazy. So the backup, we've been using this model for like, like a decade to like interrogate hippocampal and medial prefrontal activity, it's been doing a really good job. And we just keep pushing it farther and farther. So now this thing that we haven't published, it is so ridiculous, like we really are saying like, can we tag behaviorally from the model, like when someone's doing one of these incremental updates, first updates versus like forming a whole new cluster, and memory or recruiting a new cluster, if you want to think of it
*  that way. And it's really just driven by like the order of examples and really like minute things. But surprisingly, like there is like a signature of that in the brain and like Mike Max on a really good job of like relating it to like this monosynaptic versus trisynaptic pathways that I think like Anna Shapiro discussed on one of your previous podcasts, basically like kind of fast learning and slow learning. So like, I don't know, we've done so many other things with this model and like characterizing brain response that I'm excited about. But this is actually
*  just kind of seems ridiculous that like you come up with this cognitive model, like in the 90s, and it does a good job with behavior. And then like in 2005, start thinking about, well, what, what is this computation like kind of relate to in terms of brain systems, thinking about patient studies and animal
*  lesion studies and so on. And then just like kind of coming up with this characterization of the some relatively simple computations in the model and how they might relate to the brain, then like kind of fleshing that out a model based off of mine, it's like it actually works. It's really strange.
*  Yeah, maybe we should talk just how it does seem to map onto the brain. But you know, I should have mentioned that the concept cells were recorded in hippocampus. And, and yeah, this is crafted on the hippocampus. Yeah. Yeah. And one of the and the sustain model with your conceptual learning model maps onto the partly onto the hippocampus as well. So maybe you could spell out the rough and tumble of how the sustain model maps into the brain.
*  Yeah, I mean, first, it's really simple, like so much that I think people thought I was crazy when I was doing this, because like, when you think of brain model, you think it has to have like, sort of, like a lot of complexity to it. This is really like a simple cognitive model. But anyway, this this idea of like, a cluster, just thinking about what is a cluster cluster bundles together related experiences. So if you have a cluster, say to like, encode some surprising event, like encountering
*  a bat, and it's a mammal, it's like binding together in memory, like that it's small, it has wings, it flies, and it has fur. So it has to put all these things together. And to me, it seemed like a lot like the function of say, like, forming like an episodic memory where you have to bind together like all the elements and the context. But of course, like, the hippocampus doesn't work in isolation, like the its connections with medial prefrontal cortex and other areas are crucial.
*  Towards like orienting towards surprising events. And as we propose encoding, like relevant information, so there's a notion of like, kind of attending to the relevant aspects of the situation. That's again, really simple and formalized. I mean, it's it's really, it's really that simple. But just that we just the cluster creation operation should be dependent on the hippocampus. We don't really get into like any sort of long term consolidation hippocampus is like, you know, not the most like, anatomically stable region and
*  usually we end up studying things, you know, not long term over weeks and weeks or something. Right. But if you're looking at a concept learning study, you can you basically can see like what you would expect like the kind of conceptual chunks or clusters that people should learn according to these clustering models according to sustain. You basically see a signature of them in the hippocampus. And you could even see like if you teach people like model ball sort of learning problems using the same stimulus, you could see like,
*  how the items coded differently in the hippocampus, depending on whether people are doing sort of like one task or the other task. And you could also see its linkage functional linkage. Basically, it's just correlation and full response with like,
*  Ventral, medial, prefrontal cortex, particularly early in learning when it has to like the models supposedly figuring out like, what are the relevant aspects of the situation? And so it looks like sort of like kind of this top down attention signal figuring out what's relevant is like that the hippocampus and ventral, medial, prefrontal cortex are cooperating, which is like a lot like the original theory and like, I'd be totally happy to be wrong. And we obviously like are learning a lot of new things. It's kind of like,
*  I don't know, it's kind of surprising. This is like, working out. It's nice. Is the sustained model has it changed at all over the years? Or is it really still in its native, original form? Yeah, I mean, it's, it hasn't changed at all. I mean, the model itself, again, it's ridiculously simple, but like, it just keeps working like even we could even account for like individual differences and like the representations and the attention weights of the model and relate them to like decoding information.
*  And like, bold response. So it's like kind of like crossing individual differences and behavior and brain response. But yeah, the bottles, I mean, all models are really incomplete. And like, I think I mentioned we have this newer model that takes the same principles, like namely, like sort of assuming simplicity and then doing this like surprise based coding. But it's more like a Bayesian framework. But it's not really like your typical Bayesian model, because what it's
*  trying to learn like affects what it samples and like what sort of clusters with knowledge structures it builds, which is really like a critical aspect of sustained that at the time distinguished it from other clustering models like john Anderson's model, because it's kind of got lost. But really, that let in the emphasis of that original psych review paper was that that what you're trying to predict, like what the learner cares about is going to shape what's acquired. So basically, what discrimination one's trying to do is going to determine the internal
*  model they build. So it's not doing like some kind of generic model building based on all the information available. It's very much tailored to the task at hand, which is a little bit goes back to our previous conversation that people really aren't like, so abstract or complete in some sense, you know, it's, it's still a little bit dirty. But yeah, I mean, the model really hasn't changed at all, like not not one bit, we just there is a successor model, but all the principles are there just as more it could account for like, I movements and information.
*  sampling ability. But it's really like the same theory just just like, you know, extended a bit because you know, every model is really incomplete. Yeah, it's, it's, it's, I'm sort of laughing because it reminds me, I did work with Gordon Logan, who came up with the race model of response inhibition, which just basically posits that, you know, your decision of whether to move or not comes down to a race, but
*  between internal processes of whether to move or not. And, you know, and we're like building like neural models, mechanistic accumulator models. And it's like every lab meeting, you know, that we'd have these ideas, and there'd be Gordon just saying, yeah, yeah, the race model already accounts for that. And that was always the answer, you know, because it was so deceptively simple, yet accounted yet still accounts for for so much. So
*  Oh, no, I'm familiar with that work. Yeah, it's kind of kind of beautiful. Yeah, it's like it's Joel and Tom, Paul, Mary, and all those guys pursuing these related things. Yeah. I mean, there's a lot of models like that sort of like the drift diffusion model. Like, I mean, I think like Radcliffe's psych review paper was from the late 70s. And it's sort of like, was was popular in math psychology, but like, you know, kind of sat fallow and then like neuroscience like dusted it off and took took off. But I guess like,
*  yeah, I mean, maybe it's hopeful that even though the brain's really complicated and all its detail to capture like some basic things, you know, there might just be some relatively straightforward, simple operations going on.
*  Yeah, hopefully, it's not all just impossibly complex. Do you think that the formation of a concept so you so like you said, you have, you know, you have your cluster of birds, your concept of birds, which is instantiated by this cluster, and then you see a bat and
*  you know, I don't know, maybe you're told it's not a bird and that's very surprising. And then you have to make a new cluster, a new concept for a bat. Is that the same as the creation of new knowledge? Can we go? Can we go that far?
*  Yeah, I mean, it's sort of carving the environment up like what which aspects are relevant to you. It's almost like a reorganization of how one thinks about things. So yeah, I think you could call that new, new knowledge.
*  Well, but so you just said reorganization, which kind of puts it so that so there's the idea of like, well, okay, then for a bat, you would put it into your mammal, you know, cluster or whatever, or things that are mammals, but also birdlike, right? But, you know, you might not necessarily have that cluster.
*  So you could create a new cluster de novo and, and therefore, you could almost map it, I don't want to say ontologically, but as you know, to the creation of something new de novo knowledge, you know, does that make sense?
*  Yeah, no, I mean, definitely. I think I'm just being like too concrete. It could be like the the creation thing, like sounds like a big deal. But I mean, even right now, like with Robb Muck, we're working on like, a version where basically each clusters like a neuron. So the clusters themselves would have to be like, the units and the model would basically be like at the neuron level. So the cluster is almost like virtual or something.
*  And then creating a cluster is really like changing the receptive properties of these units to like retune them. So, but it's still like, but at a higher level, it is still like creating a cluster. And I think it's really just kind of like partitioning the conceptual space up and showing that like, oh, no, you thought that this whole region of space was all this one thing, but you actually have to put a split in there.
*  And so you are learning something new about that part of conceptual space that something's going on there that you didn't expect, like namely that these are actually strange flying mammals.
*  It still maps into your existing conceptual space at that point. It's not so surprising and so new that it's something that you would otherwise have never been able to think of. I'm not trying to push too much. I just, you know, about the ontological nature of knowledge. But I'm kind of wondering how you conceive of it. So yeah.
*  No, I mean, it's in the existing space of possibilities. It's just that like, it's really like, how do you map that space to like the actions you want to take or your goals to set what you want to do to satisfy your goals. So in this like discussion we're having, it's really the only goal is like to use the English word, bird and mammal correctly. And so I mean, that's what you're building, like knowledge structures, splitting up like the space of possibilities to like correctly achieve that end. And so like, I think you could describe it.
*  Like in sort of, you know, more grandiose language, but I think that's all, you know, like these concepts are all there is to it really.
*  A feature of forming concepts or abstracting things in general is, is that you lose details like that are irrelevant to the concept. Right. So, you know, for a bat, for instance, it wouldn't necessarily matter that the bat was hungry on a Tuesday. Right. And if that's was your one example of the bat and you have 40 different examples of bats now and being hungry on a Tuesday is irrelevant with respect to the concept of a bat.
*  I'm wondering if, well, you've described how episodic and semantic knowledge can blur into each other during that process of losing irrelevant details. Can you just describe that for us?
*  Yeah, it's funny way back when we formalized this like idea. I was like, I thought this would upset people. Basically, it says that like everything like just like you said, everything starts out as an episode. And then it gets interfered with with related experiences if they collapse together in memory and becomes a little bit.
*  There's no magical point, but over time it becomes more semantic in nature. Yeah, Mike Max actually written this up as like, you know, like a focused on this aspect of kind of going from episodes to semantic knowledge. And it's been kind of fleshed fleshed out this idea.
*  But yeah, it's exactly it's exactly that. And like these models do a really good job of like accounting for human recognition ratings. So it's like you're saying, like if things sort of collapse together into the same cluster of memory, you have some knowledge, but you basically have like sort of almost like the histogram of your experiences.
*  You don't have like this, this bat was exactly, you know, this location, this one was at that location. It was this shade of gray versus that shade of gray. It's just sort of like, you know, all averaged together and memory.
*  I mean, but that's, you know, just sort of like our days all blur together and less like, you know, like a person in a gorilla suit burst into the classroom or something. And that'll probably get like, you know, separated off as its own episode because of the surprise.
*  But yeah, so that's, I mean, that's basically it. It's just like, you just basically are doing this like intersection averaging operation on your experiences until like, that sort of collapsing of information together leads to a problem.
*  So you assume everything's simple and can just be like kept together as a running average pretty much. And when that fails, you take note, and then that could become like a new running average in your head. So it's all about like, you're doing some kind of task, you're trying to have some kind of goal.
*  And when the way you're thinking about things isn't working, you take note and that could just keep in mind as an exception or that could kind of turn into something more semantic as time goes on.
*  Can clusters get destroyed?
*  Yeah, it's really good question. It's funny, like way back, like when I was a graduate student making this model, it's looking at
*  And that's funny. It's funny is everything is when way, you know, way back then when it's so interesting how this is a very separate and I'm sorry to interject, but no, no, no. So many people have this experience that like whatever, you know, their careers are their 50 years into their career, but everything was pretty much set.
*  The roadmap was set by something that happened really early on. It's pretty rare that someone late in their career starts a new path. It's all it's like, there's a few crucial years in there and then boom, it's all it's all set for the for the future.
*  So I don't know.
*  Yeah, I think I hit my high point as an undergraduate actually.
*  Yeah, there you go.
*  Yeah, literally my first publication, which gets no credit was exactly like PageRank three years before PageRank. So I should have just like stopped there or something.
*  Wow.
*  It didn't even get it didn't even get the best student paper award at the conference. You know, I don't know what you got to do.
*  You were too early.
*  Yeah, I guess I don't know. But I mean, that's true. But I think I'd be better off if I actually did that. I kind of get into too many things. And then I mean right now, I mean, I don't want to change the conversation.
*  But like right now, I'm trying to kind of we're still working with these models and like the only reason kind of stick with this general theory is because it seems like it's like we're correct.
*  But there's a lot of things that I do and try and things kind of move towards move away. And I mean, I don't know, maybe we can talk what's going on currently, but even moving towards like model based neuroscience was like very different.
*  It was really like I guess my philosophy from model for neuroscience is that you should take like the best cognitive model of the task that explains behavior and kind of use that to work with to kind of figure out what the brain's doing.
*  So like if someone else had a better model of the kind of tasks we were running, well, then I would have just used, you know, their model.
*  So, but I think there is like some truth. But I don't know, I get bored and always want to switch it up anyway.
*  But yeah, I also recently talked to Paul Chisek and he and others like Yuri Buzaki.
*  They they have this push where they say we have it all wrong, that our labels for cognition, our concepts, if you will, are all wrong and actually have been for centuries concepts like attention, decision making, and so on.
*  And then we're going to have to reconceive of and re label what what we're actually studying because because the concepts are wrong, essentially that labels are wrong.
*  Do you think there's any merit to that? And more generally, are we as humans, are we too concept trigger happy?
*  Like can our bias to form concepts? It seems like this is a bias that we have.
*  Like we want to compartmentalize everything and give a label to it. Right.
*  Is that bias to form concepts? If it does the indeed exist, does that lead us astray?
*  You know, when we're in a realm of unknown or, you know, poorly theoretically formed domain like something like studying brains and minds.
*  I like this idea that we might have like the credit all wrong sort of like frameworks for discussing everything.
*  I mean, one reason this might sound cavalier, but like in some sense, these discussions don't really like inform or affect my research because when I use words like concept attention, like I'm very specific.
*  I've got like a formal model and like if someone says that's not attention is OK, just whatever you want to call this weight that follows this rule that explains behavior across 30 studies.
*  Fine. You could call it gobbledygooky whatever like it doesn't.
*  I think so. I don't really know if coming up with like new ontologies of this, like maybe we should just actually be a little bit more specific in what we mean or what we're claiming.
*  It's almost like back to the model selection discussion we had earlier.
*  So I think these are like good things to think about and debate.
*  But I mean, I really I hate to say this because I know everybody doesn't like modeling or like formal descriptions.
*  But unfortunately, I think it's really necessary for dealing with these sort of complex issues.
*  I'm not sure that everyone doesn't like them. I think that they sort of dominate neuroscience these days.
*  All right. Well, about time.
*  That's good. Yeah. Well, that's yeah.
*  It's interesting because, you know, I'm reading having read now about your sustained model.
*  I think, yeah, that's good. You know, this and it's you kind of forget that when you developed sustain and we're approaching things using cognitive models that that was not the rule of the day.
*  It seems more like the rule of the day now. How to approach things.
*  Do you experience that? Do you have that same outlook?
*  Yeah, maybe. Yeah, maybe like my previous comments are just like reflecting like this time period I imprinted on.
*  But yeah, like when I was way back, like in the dark ages, like people in psychology were like, you know, running like two by two studies and doing it.
*  And there wasn't like a lot of mess like type people were like in a real minority and were just like considered like boring and pointless for the most part,
*  even though they're doing a lot of times very interesting and useful work.
*  Now that you say that, I actually kind of I have this recollection in even in graduate school.
*  And I really came in very naive, like my undergrad wasn't related to my graduate school.
*  But I had this recollection of it seemed like everything that we were studying, there is like a model being built for it.
*  And I was like, oh, God, now I have to learn all the modeling stuff, too.
*  And it seemed heavy and hard. And maybe that was when modeling was coming on as such a ubiquitous frame.
*  Yeah, it could be. That's that's really that's really interesting perspective.
*  Yeah. But from the other side, like applying these models, simple models like the ones I work with, they're not like, you know, like all these spiking neurons and like tons of details or like membrane.
*  Like people are just like those models aren't real. That's just like fantasy world.
*  Why would you use this? So it's like basically both sides of psychologists are like, please don't make me like listen to your boring talk about this stuff.
*  I just just show me like like to show me the mirror test or something or I don't know something like it's not biologically plausible.
*  Is that the I don't know if they cared about that.
*  Actually, it's really funny. There is almost like a completely different perspective.
*  There was like a perspective then that's I think it's just sort of died out like as people like retire and stuff that like cognitive psychology was at like a functional level that the brain was completely irrelevant.
*  I mean, it's hard to believe now, but that was like a huge and there was like, you know, popular philosophers at the time like Fodor like pushing it.
*  I mean, there's still like a lot of people that feel that way, but but they're not like part of, you know, this community and it's like ever, you know, decreasing minority.
*  Yeah. So, I mean, it's kind of nice that people appreciate models.
*  I mean, of course, models could clarify. They could also obscure and just having a model.
*  It's only, you know, like you do model based work. It's only as good as the model is.
*  So, you know, if you use the model as a lens on the brain and, you know, that lens is flawed or distorted, then so are all your results.
*  So it's not like a cure all, but it could help incorporate other constraints, like especially if the model is like justified from other studies to, you know, lead to a better result.
*  But it's nice to. Yeah, it's nice that people are coming around to this a bit more.
*  Yeah. All right. Well, I want to ask about the hippocampus and then we'll move on to a little more deep learning work because.
*  It seems like the hippocampus these days is associated with everything.
*  We've just been talking about it in terms of concepts, forming concepts.
*  But, you know, the latest craze in in hippocampal research is its association with navigation.
*  I should say latest. It's not really late. It's been around for a long time.
*  But so, you know, does two questions. Does abstraction, does concepts, do concepts co-opt our navigation system or vice versa?
*  And what does the hippocampus do?
*  That's funny. Yeah. So like, like way, like I got it like way back in like ancient times when I was thinking about like how this clustering while sustained graphed in the mind, I just viewed like it all is the same learning problem, like learning about space.
*  Space is just like another concept to learn. And like, I was really kind of like scared to say that.
*  At one point I crossed paths with Linda Dell and I thought he would like hated. He's like, oh, no, that's that seems OK.
*  And maybe like just over time, getting confidence and like having a good postdoc that wanted to do a deep dive into these issues of like navigation and hippocampus.
*  Like we finally like published something recently on this.
*  But yeah, so I think like obviously people like use space to like organize their thoughts at times like we even in like natural language, you say like I'm feeling up today.
*  I'm feeling down. We understand abstract concepts like time in terms of space, but that's just like using representations of space.
*  That's not like a learning system or a system at all in the brain.
*  So I think there's really just like one general clustering learning system that supports learning concepts and space is just another concept.
*  It's a very in some ways limited concept of how it's like studied like in rodents in the lab.
*  Yeah, so I guess really neither. It's just like there's just sort of like one computation, one learning system, the rule at all.
*  And you change the inputs, you change the task and you get out things that look like Jennifer Aniston or like I don't know, like a rodent enclosure.
*  What about memory? Doesn't the hippocampus do memory?
*  Yeah, I mean, there's there's like, OK, yeah. So the hippocampus is even more than you mentioned.
*  Like, you know, it comes up in like kind of almost like simulation, like imagination, imagination.
*  Yeah, like people call it mental time travel and stuff.
*  But yeah, but I see these clustering studies that we do.
*  I mean, it is, of course, a kind of memory. It's persistent, like over like, you know, our studies only go on like two hours.
*  But in terms of like long term memory, like I said before, we really don't like there's all kinds of ideas of in terms of consolidation involving hippocampus.
*  And I think you've discussed on your podcast, like complementary learning systems and, of course, that's contentious.
*  So there's debates about that. I mostly focus on sort of like the acquisition of knowledge and like don't like wade too deeply.
*  I mean, I find it really interesting and to the consolidation aspects.
*  I mean, I find that reasonable given how again, like how much cell turnover there is in the hippocampus.
*  But yeah, so I kind of view the concept learning as like encompassing memory as well, because it's like again, each cluster starts out as an episodic memory, which hippocampus is implicated in.
*  And it only becomes more semantic when you have a bunch of kind of like similar, almost like redundant experiences that interfere with each other and like sort of wash out the unique aspects of the episode that creates something more semantic.
*  And, you know, I think just like learning a location and space is like a like a place cell does is just that's just a concept of like collapsing together a bunch of related viewpoints and experiences, sites and smells and sounds like the geometry of the room.
*  Like basically just like a lot of inputs that are non surprising and could collapse together into one cluster for that location.
*  So I think all this stuff is like really the same thing.
*  So just to be super nitpicky.
*  So I did have Paul Ciesak on a little while ago, and I really enjoy his it's called a phylogenetic refinement approach.
*  But basically looking through, you know, tracing back our evolutionary history to better explain and better ask better questions about what brain areas are doing and why they're doing it and how they're doing it and stuff.
*  And he didn't really talk about hippocampus and, you know, abstraction and concept learning much.
*  But I was kind of trying to apply his thought process to this and in the whole navigation versus cognitive map versus concepts and abstract conceptual space maps, you know, and thinking about the chicken and egg problem of these things.
*  And I thought so I look back and at the evolutionary development of the hippocampus.
*  I promise I won't take us too far down this road.
*  No, no, no, please.
*  So early on, you know, before the explosion of the cortex, it was it kind of came out of the hypothalamus and which is like a regulatory overall control system, essentially.
*  And and the hippocampus was is kind of related to the explore aspect of the explore exploit trade off and can be associated with this longer term, longer range exploration mechanisms.
*  And I thought, OK, if that's true, like if the hippocampus was sort of developed via built on top of some system that was used for exploring to find food and resources and long range exploration.
*  And I thought, OK, that's related to navigation.
*  And that's kind of related to the cognitive map.
*  And that's not so far from then sort of internalizing these things into abstract concepts.
*  So like a conceptual space for essentially you can think of it as still being used for super long range behavioral purposes.
*  And in that sense is a bit of a navigation, long range exploration way of saying what a concept is.
*  Does that sound ridiculous?
*  I mean, I mean, not even ridiculous.
*  Yeah, I mean, I don't know.
*  Yeah. Evolutionary psychologists have all kinds of descriptions of why we're the way we are too.
*  Yeah, but yeah, I mean, no, no, I thought no, I like these stories.
*  I guess like, yeah, I mean, I think it's valuable to think about, like, you know, where these things came from.
*  But I mean, also, like, where there's all kinds of like, like, I was like, look, a quarter receptors like stress response was it?
*  I can't remember. I remember reading about this stuff like HB axis, like why if you have you get like sometimes memory problems, if you have like people with depression or something, I think this is why.
*  I mean, my reading on this is all out of date.
*  So there's all kinds of like weird things that go on.
*  But I mean, one thing I kind of focus on is just kind of like what kind of computation because you're trying to pull out something more abstract, like more general to like what it's doing.
*  And I totally like I'm on board with that program.
*  So for me, what's more general is that the hippocampus has the ability to like basically bind together like arbitrary elements that are relevant in the situation.
*  Like, like the bad example, you just like why a fur doesn't go with flying and wings.
*  You're just like, boom, you could just do it.
*  You know, like it has this ability to put things together, which would be really useful to like you mentioned if you're exploring a new environment, you have to remember where like you the squirrel hit its, you know, acorns or something.
*  But but yeah, so I mean, it's also like why it would be useful for imagination or mental simulation or, you know, all these sort of functions that are associated with it or episodic memory.
*  I mean, you could like encounter any event and have to remember it's like totally arbitrary.
*  So like, I think that's it.
*  It's it's also like an area that's working, you know, with like, you know, prefrontal cortex to do this where you have to kind of figure out what's relevant and orient.
*  So, yeah, it just seems like it just seems like as ability to like, like learn arbitrary things, almost like build new codes or something.
*  So that would be useful while you're exploring.
*  But I mean, I don't know, I kind of mostly just focus on the kind of computation that does.
*  And it seems like it links together all these different domains that are associated with the hippocampus.
*  Last question about clustering and concept formation.
*  And then we'll move on. I promise.
*  Sure.
*  I thought I mean, I have like a billion more questions about these things.
*  But and I'm sure you've already you thought of these things as you were probably 11 years old.
*  But I thought, you know, maybe is it possible that the development of expertise in a domain is just where, you know, whereas other people might conceive of some, I don't know, let's say piano playing or, you know, whatever expertise domain.
*  There's piano playing and that's kind of like one cluster.
*  Right. But then once you start to really go through your 10,000 hours of practice, is that maybe just a process of forming more clusters where and having a more complex cluster?
*  And having different conceptions, whereas other people kind of would have them as fewer clusters to conceive of the same concept.
*  Yeah, I mean, I think that could be part of the story.
*  Like a lot of even when I was working on this model, originally I was thinking about the expertise literature, like kind of work that like James Snuck and others were doing at the time.
*  And like experts tend to draw.
*  There's all kinds of experts, of course.
*  But like if you take like experts in some perceptual task, like birdwatchers or something, they tend to form like finer gradations and like the concepts, the distinctions they could draw.
*  And so certainly you'd need sort of more partitions, more like clusters and memory to support that.
*  But I think like what really drives a lot of expertise is like kind of changing the space that the clusters themselves would reside in.
*  So like experts seem to have access to like more and more useful features to describe things.
*  So like, you know, for playing chess, you know, like I'm not a chess expert.
*  It's just like board positions, but chess expert could see like, oh, this is like this attacking position or like, you know, like I think this is also we talked about memory.
*  Being very superficial.
*  This is why experts are better in their domain, but not outside their domain is because they have better indexes to their knowledge.
*  So like they when they see something, you know, just like as we become like expert in neuroscience, we have better indexes of people's work.
*  And so we could relate them to each other and retrieve them more relevant work more easily as opposed to rely just on superficial things.
*  So I think the experts change the space.
*  But one nice thing about clustering model is sustained.
*  I think it's actually unusual this way.
*  It's one finding one to go after originally is that when items in a domain become more distinctive as they would be for an expert that has like a richer feature description, a richer space, the benefits of abstraction and the model actually go down.
*  And so there is like a processing advantage to forming more clusters, like you're saying.
*  So it would actually be like adaptive according to the model to like have more clusters when like all the birds look really distinct from each other.
*  Whereas to me, they're just birds because I'm not a bird expert.
*  So I could just class them together.
*  Yeah. Yeah. Yeah. Birds.
*  I don't know. I'm not a bird expert either.
*  I don't understand bird experts.
*  I like them. Yeah, just fine.
*  I know you don't like them because you don't like.
*  I don't know.
*  As long as they don't like friends, it's OK.
*  OK. All right.
*  Let's you know, it's fascinating stuff to me.
*  That's why I keep asking more and more questions.
*  But you've been using deep learning lately.
*  So, you know, there's this deep learning explosion and it's kind of colored everything in cognitive science, neuroscience.
*  And you've been using deep learning a few different ways lately.
*  One thing that you've done is you've connected concept learning to different layers in a convolutional neural network.
*  And the convolutional neural networks that are used to model, as you mentioned earlier, are ventral visual stream, which underlies our ability to recognize objects.
*  So how do you use convolutional neural networks to better understand concept learning and how it connects with the ventral visual stream?
*  Yeah. No, thanks for asking.
*  I mean, I think these these networks are like a complete like game changer for the kind of research I do.
*  So like this like your question is great.
*  I'm going to answer with the step even like further back with all these like clustering models, all these cognitive models do.
*  They rely on the fiction of that the experimenter has to say how people represent things.
*  So you have to say, oh, that's a triangle.
*  That's small. That's red.
*  You know, you have to like read out the features.
*  Whereas like those are that's like a real hard part of the conceptual problem is like, how do you create like a description language?
*  How do you come up with the features?
*  And that's really like in the previous era of machine learning, what made a model good is having good features.
*  Like, you know, we talk about experts having better features.
*  So in some way, like the most interesting problem has been like sidestepped, you know, by necessity, like because you don't know what you can't like pause it like what the representations are.
*  So like deep learning can, you know, like, well, if you just train something on the image that could like pull out like reasonable features itself from the end to end, like optimization.
*  And it's really exciting because it's just not one feature.
*  It's like you just mentioned, there's all kinds of levels of representation of transformations of like the image to the response.
*  And so like, yeah, one thing it did with Olivia Guesta, you know, we're still working on is like looking at animal learning, like pigeon learning.
*  So they could do all these things that people say, oh, that's so abstract.
*  That's so conceptual, you know, like, but there's a lot of cases where like, you know, we kind of infer abilities that maybe aren't there in animals and probably with people too.
*  I mean, probably in developmental studies of children, like we go, oh, look, they have a sense of object permanence or this.
*  I mean, who knows? I mean, yeah, they're well-designed studies, but people read so much into things or like the mirror test, like, oh, like you put a dot on a baby's head and it recognizes.
*  Yeah, it's in dolphins could do it. But then, oh, so can some stupid fish.
*  So maybe that's not a good test anymore.
*  You know, like going on a bit, but like the same thing happens in deep learning, you know, like, oh, look, this could detect cancer.
*  And maybe it just turned out that all the serious cases were sent to like a certain machine that has some artifact in it that like the deep learning model picked up on.
*  So even though it generalizes to the test that the test that has the same sort of confound in it and it doesn't like work well in practice.
*  So anyways, it's a long way around. This is like by modeling concept learning using different levels of representation from the deep learning model.
*  We could ask our people or pigeons relying on like very low level, almost like pixel like information to solve a task or are they doing something more deeper based on sort of features that are a little bit more conceptual and not as like image bound.
*  So that's like one thing we're doing. Yeah. Well, I guess the way that we sort of think about it and you know, the eventual visual stream classically is, you know, light comes in the retina.
*  You're looking at a bat, let's say, you know, and then our visual cortex starts to break it down into all these tiny features and then hierarchically it gets passed to other areas of the brain and they get built up in more and more complex features.
*  And then finally, there's the representation of a bat in our brain. Right. And then and sort of I think the next logical thing to do then is to think, okay, that's the representation that we'll use to form the concept of a bat.
*  Then we'll take that final step. And I guess what your work is showing here is that that's not necessarily how it needs to be done. And that's one of the questions, I suppose.
*  Yeah, I mean, I don't know, maybe like, I think I'm like too much like too much of like a hard ass or something like so I wouldn't think of the end as being like the concept.
*  I mean, maybe it's just like the I mean, of course, you're losing information. Like, what is it the information processing inequality using like information at every stage, you're really just transforming it to get to like the response to the action.
*  But, but yeah, but like what you said, totally right. So like, we could model like what it's just really a question of like, are the are the are the animals using something like more like process or higher level or can you actually just solve this task like in the stupidest way like basically like, like associating responses with like what's coming off your retina and like, maybe for like modeling human learning and animal learning, this would be like a good methodology is to like use tasks where you could apply a lot of different methods.
*  So like, I think the idea of methodology is to like use tasks where you could apply a model to it and like quantify like what kind of information is necessary to solve the task because all these things look so impressive from the outside like oh animals could do this animals could do that but it could be just picking up on some like really superficial property of the images just like how you know, deep learning models look for shortcuts and so you got to go through all these, you know, efforts to like make sure it's just not picking up on texture or something.
*  I think it's the same issue that like it's just not deep learning. I think it's people and animals who are just not that abstract like we were talking earlier, we'll just look for like whatever shortcut to like get to the answer.
*  Yeah, I mean, abstraction is costly. So if there is a better way to do it in a dumb way, you know, that's actually the smart way to do it, I suppose.
*  Yeah, I mean, like also like, how do you we say abstraction, everyone like complains, oh, this is just curve fitting this like, how do you infer like the correct distribution that has anything to do with the training distribution like is like what magic is that either has to be like, building your head or you have to experience it.
*  I mean, I just think we have rich environments and like a lot of extensive interactions, like with fairly rich inputs that like force us to build like somewhat robust representations. But like, I don't know, like, I really hate this like curve fitting complaints. It's like, I don't really know, like what what other what kind of learning is possible here.
*  Is that that? Yeah.
*  Yeah, you either have to build build in like the constraints. I don't know. It's just, there's just no magic.
*  And that's the show. Thanks, everybody for joining us. No, I'm just kidding. We're not going to end up with just no magic. But it's just, it's not so sad. It's just like, oh, where's the wizard?
*  Yeah, I know. That's that that's one thing. Again, just the more you learn, the more magic goes away in your thinking and which is great in some respects, because it's better to understand things. But, you know, once you believe once you realize there is no tooth fairy, it's less magical. And I don't know, there's something less special about that. But it's something even more special about learning how things actually work. So yeah, there's a trade off. But definitely.
*  Yeah, but just to get back on track here. So okay, so yeah, so so you kind of set it up. So what'd you guys do?
*  That work we just actually found that pigeons are pretty much just learning from pixels. So like you're good radiologists still. Yeah, unless you like change some superficial property of the images, then they're I don't know, maybe they I mean, well, it's inconclusive, right? Because we're just we're just their behaviors consistent with like having a like a deep understanding of the images or or just none at all.
*  Just to actually say what you did on the technical front with the deep learning. You basically tested out, you took out different layers from the convolutional neural network and use those different layers to see what the what matched up best with what the pigeons were actually using to do their radiologist work. Right?
*  Yeah, definitely. It's right back to like sort of the model selection story. So basically, you could make a bunch of like, concept learning models that are working on different representations, different input representations. And like you said, you could either work on visual representations that are incredibly low level, like very close to the stimulus, or you could work on ones that are like, you know, very high level in like, through many levels of processing. And it turns out that the
*  lower level ones support the behavior of the pigeons, which look like impressive on the face of it, but it's really maybe not.
*  Okay, so that's that's one way that you're you've been using deep learning. And we're only gonna I mean, you've been doing a lot of different things, actually. But I just want to bring in one more at least. So you've said that your recent work with adding top down attention to a convolutional neural network is basically an attempt to make deep deep learning more human.
*  So what do you mean by that? And how do you implement top down attention in convolutional neural networks? Because there's a lot of talk these days about attention and adding attention to networks and attention is all you need. And yeah, that's there's, and this goes back to what attention is, and that there are about 10,000 different meanings about attention. But but how do you implement top down attention?
*  Sure, sure. Yeah, I mean, you're absolutely right. There's like 10,000 different versions of attention. Actually, I think just like a couple days ago, like a review paper on how attention is used in neuroscience and AI came out from Grace Lindsay's done some work on
*  Yeah, attention and deep learning. But yeah, so for like, if there's any hardcore, like machine learning people listening, like the way we use attention has nothing to do with like the transformer architecture, as you mentioned, we're really kind of talking about a kind of selective attention that picks out what's relevant, given your current goal or expectation. And this goal or expectation is coming from outside, like the deep learning network is coming from outside the ventral stream or the stimulus itself. So like, for example, if you were looking for your
*  keys, you know, it's like you want to like, almost reconfigure your visual system on the fly to prioritize like filters in your visual system that respond to shiny things and small things. Whereas if you're looking for your cat, you know, you would like reconfigure a different way. So that's how we see top down attention is sort of like a layer or multiple layers that are kind of like multiplicatively, like weight the filters. So basically, silence some that are irrelevant that just add noise given the current
*  expectations and like, make others sort of more consequential in the computation, like say there was like a one that was related to how shiny the thing is or something, the texture, if you're looking for your keys. Yeah, so we train up these attention weights for different goals at different intensities and like look at this trade off and we find that we could increase sensitivity in terms measured in terms of D prime. So basically just be better for like moderate levels of attention. But you also get like, rising
*  bias to like, just like people if you're like, you know, if there's those things like, oh, I see faces everywhere, like those funny websites, it's sort of like if you're looking for something, you're more likely to see it. So you see this kind of bias or criterion shift and signal detection terms also happen. So as you turn up attention more and more, you kind of get this like trade off and eventually like things fall apart.
*  The way that you implemented this, though, is correct me if I'm wrong, didn't you? So did you take a fully trained convolutional neural network and then add in a layer, extra layer into the network that then you that was the attention layer that you were just talking about that then you could then train keeping everything else the same? Is that right?
*  Yeah, I mean, I think that's critical because you know, like when you're looking for your keys, your visual systems getting modulated, but it's not like permanently changing that much as a consequence of the task. So yeah, so like we kind of viewed like these pre trained network as sort of like your generic building up all the filters, all the feature detectors, like kind of getting representative experience, almost like you want to hotwire that system on the fly to repurpose it for
*  more specific tasks that are relevant in hand and maybe get into it. But this is like really kind of follows from like some just model based fMRI work we've done. Yeah, so yeah, that's exactly how it works right now. We're like, yeah, we have like a pre print up now and we're working on newer work, we actually like work in a whole like separate attentional network that still relies on a pre trained convolutional neural network to do the object recognition.
*  But as a whole new network that does the top down modulation that could support generalization. So that you know, so if you know how to like look what to look for for like lions and tigers, you probably also know what to look for for a liger, even if you've never done that task before. And we also could like interface it with language. So like, if someone says to you like, look at the blackbird and the tree that will like get transformed into like, basically change the ventral stream to configure for that message coming to you.
*  Yeah, so it's kind of cool. I think it's what people do when we see the same kind of things like in our concept learning studies, if there are fewer aspects of the stimulus that are relevant to the discrimination to like solving the concept learning problem, we actually see like the dimensionality of representations and like the mid level visual system like in lateral occipital cortex are smaller. So we have like this technique for measuring dimensionality of neural representations and this neuro image paper from it with Christiana
*  Altheim from few years ago. Yes, you can see this like kind of task related modulation that is exactly kind of exactly like how we're doing it in the deep learning model like where you kind of just change the dimensionality of the problem and turn silence the irrelevant filters. This isn't spatial attention is like
*  future attention. Right. But yeah, so I think this is what goes on. I mean, I think this is just the goal or the relevancies coming all the way down from like ventral medial prefrontal cortex. It's signals going all the way down to like kind of change these visual representations that are coming on up to the hippocampus and other places. So that's like the rough sort of cartoon conception of what's going on.
*  I'm pretty sure you're cited in Grace Lindsay's recent I haven't read the whole thing yet, but I'm pretty sure that she cites your work in there.
*  Well, it must be a really good review paper then.
*  Yeah, it's excellent. What what are your I mean, so part of your point in this paper is that in machine learning in AI, the focus of attention is basically almost all bottom up.
*  And so, you know, what you're doing here is this top down attention to sort of drive the the system, highlight some weights and get rid of others. Well, what are your thoughts on the state of adding attention in to deep learning?
*  I mean, I think there's no reason like not to so like, I mean, just like with all the caveats that you've mentioned before that there's many different varieties of attention, and we have to be clear about what aspects of attention we're examining.
*  But at least you're like what we're doing, like, I think we have a pretty well worked out like how this kind of selective attention works in like areas that are of interest to us like the prefrontal cortex, the hippocampus and along areas in the ventral stream.
*  I think it's ready to start trying out ideas. It's not like it's not too soon. And if anything, it's like by trying out these ideas and these networks, I think we'll probably get like more insight into like what the brain might be doing. And it might spur, like further understanding onto the neuroscience side. So I think it could be the right point to like kind of get that virtuous cycle that people, you know, like to discuss in terms of neuroscience and AI research.
*  You've said that deep learning is you consider it a game changer. And I mean, is this just something like where it's a candy store for you and you think, oh, I can, you know, you have like 10 different ideas of how you can start using deep networks to interact with your conceptual concept learning systems and so forth.
*  Oh, yeah, I mean, I kind of almost wish I was like born later or something so that I had more years to like play with these things just because like, I mean, just the changes in computing like the
*  I mean, there's the models really aren't like that much different than like the 80s. There's just like a couple insights and good tricks. But like, it's just finally like come together that you could do interesting things. And to me, it's just so exciting that
*  Not to have to work with handcrafted experiment or defined representations. I mean, I don't think people believe what I'm going to say. But like, we used to sit around in graduate school, like in the late 90s and with professors and students and talk about the big picture. And like everybody thought it would be 200 years before we had any models that could like do object recognition like even decently from pixels and like all the research. I wasn't doing any vision science then, but I was doing a lot of research.
*  And so all the researchers saw like all their studies and all the minutiae of refindings is like feeding into like some eventual understanding that would be like so far into the future. I mean, that was so ridiculously wrong. And it's just like, it's very exciting to see that I mean, the same could be said for like even like speech understanding and I mean, face recognition would be like, I'm not even imaginable and like, so like, when people like, don't get excited about this stuff.
*  I think it's just like a really a case of like moving the goalposts or they just, I don't know. I mean, this is what the history of AI to like things like sorting, which I keep mentioned used to be considered like AI. I saw a talk like forever ago by Ray Mooney. It's basically anything that works is no longer AI.
*  There's a name it's called, it's called the AI effect, I believe, to turn the AI effect. But you know, that's interesting that you say that because most people are way short sighted in their estimates of for instance, you know, when will we have AGI, when will we have figured out the brain and it's always 20 to 30 years away. And that that was true 100 years ago. And it's true today. So it's interesting that you had that different perspective on how quickly this seems to have happened.
*  I mean, I don't know, it's really exciting. It kind of goes what we were saying, like, maybe everything isn't really that complicated. I mean, it turns out like, obviously, like, we're not done with vision. And it's these models are like, right, right, have huge hiccups. But I think maybe we really weren't that far off. Like, it's gonna be like going back to our other conversations. Maybe it's about like the complexity of interactions, the richness of the input, you know, it's like the theories weren't really that bad, actually. And it's the stuff kind of works.
*  Even though it's pretty, you know, brain dead. Like, a lot of models, it's Yeah, yeah. So you see, okay, so you use the word, the phrase game changer, and I don't want to harp on that. But, you know, projecting forward, let's say, I don't know, 20 to 30 years, or maybe 200 years, like you were saying before, looking back on this latest, what's called the deep learning revolution, you know, how will history view it? Will we see it as having been an essential leap forward?
*  And toward understanding our own intelligence or toward understanding intelligence in general? Or is it going to, you know, well, I'll leave it open to you. How will history view this time? Yeah, sure. So I mean, I can imagine like, your your guests that are astute would probably like, give the quick history lesson, I'll try to do it really fast, not to be tedious. I mean, people go back to like, Rosenblatt, who was a psychologist, made a perceptron. And like, it was the same thing, you know, it was pretty much like linear regression with batch size,
*  one, and the US Navy, like, I think it was using piled money into it and build like, you know, like a hardware version of it. And it's fine. But like all the newspaper articles, it was the same hype in like the late 50s. It's now like a super intelligent machine. And of course, like, I like, you know, it flamed out because it was just kind of, you know, basically just doing like linear regression. And there's devastating attacks from in skip. But then of course, like, then there's this like, whatever winter and then like,
*  I mean, back propagation was actually discovered much earlier. I mean, it makes sense. It's just like high school mathematics. It's like the chain rule, like big deal. Yeah, it's like a bit like, anyway, it was popularized again in the 80s. And then oh, now we can solve x or a nonlinear problem and something done in the regression and it took off. But then of course, I went away, at least in my opinion, because it was, you know, it's kind of hackish, just like how deep learning is now that in like kernel methods, like support vector machines, even Bayesian methods, like
*  they had a lot of advantages. So then it just kind of went away a lot. But I guess the difference is now like, I mean, this stuff actually like works in a way it doesn't before. And so like, I think how it's viewed, it'll just depend a lot, like how the labels maintain or change, like you said before, like, oh, everything's just like labeled deep learning. So like, maybe we start getting better representations of uncertainty in these models or this. But I mean, unlike before, and like all these other AI Winters, like people, these models actually do like interesting tasks now, and people are making
*  like money off these models, like that's not maybe not of interest to academics. But it's a difference with the like previous waves. So like, yeah, I don't really think it'll bust and like how it's viewed, it's just like, you know, history is like, you know, whoever's writing the history that determines it, but like, I can't see the stuff not leading to the next thing, the next thing, the next thing that makes a huge difference. And of course, like neuroscience is so fad driven, like by the time people start doing
*  really super amazing neuroscience with these models, we probably will have moved on and like under appreciate their work or something and rediscover it later.
*  Yeah, yeah. Oh, that's it's amazing how often that sort of thing happens. But I really appreciate you talking to me for so long. So thanks, Brad.
*  Oh, no, it's great talking with you, Paul. Thank you.
*  Brain inspired is a production of me and you. You can support the show through Patreon for a microscopic two or $4 per month. Go to brain inspired.co and find the red Patreon button there. Your contribution will help sustain and improve the show and prohibit any annoying advertisements like you hear on other shows. To get in touch with me email Paul at brain inspired.co. The music you hear is by the new year.
*  Find them at the new year dot net. Thanks for your support. See you next time.
*  Yeah.
