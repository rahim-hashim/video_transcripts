---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5477s
Video Keywords: []
Video Views: 4822
Video Rating: None
---

# BI 151 Steve Byrnes: Brain-like AGI Safety
**Brain Inspired:** [October 30, 2022](https://www.youtube.com/watch?v=w7k3o5uIBjs)
*  So what we really want is that we understand what the AGI is thinking in all this full glorious detail.
*  I am hopeful we will get that. I guess I shouldn't say that. I would love it if we got that. I am pessimistic that we will get that.
*  There is a school of thought in neuroscience that says that the human brain is just so enormously complicated that there is just no way, just no way at all that we will possibly have AGI in 100 years or 200 years or 300 years. People will just throw out these numbers. And I really want to push back against that.
*  The question I am interested in is how long would it take to understand the brain well enough to make brain-like AGI?
*  Whereas the question that a lot of other people are asking is how long would it take to understand the brain completely? And these are different questions.
*  Hey everyone, it's Paul. Are you worried about humans building AGI, artificial general intelligence, and that if we do, any number of things could go horribly wrong? If so, Steve Burns shares your worry.
*  Steve is a physicist turned AGI safety expert, I guess I would say. And like a handful of others concerned about how AGI might affect our world, he thinks we should be thinking now about steps to take to ensure that our future AGI-laden world is a safe one, however far away we are from actually building AGI.
*  In Steve's series of blog posts called An Introduction to Brain-Like AGI Safety, he lays out that concern and argues one way to ensure a safe future is to understand how our brains work, including the algorithms that underlie our motivations and ethics to be able to program AGI's the right way to ensure that we don't build AGI sociopaths, for example.
*  So in this episode, we discuss some of the ideas that he elaborates in his writing, and Steve takes a few questions from the gallery of Patreon supporters who joined this live discussion. Links to Steve and his work are at braininspired.co.
*  So I encourage you to go there to learn more. Thanks for listening, as always, and thank you to my Patreon supporters who help make this show possible. All right, here's Steve.
*  Steve Burns, you're one of them physicist turned AGI safety experts. How many of those are there?
*  It does seem to be a common path for whatever reason. Is that right? I was kind of making a joke, but I would assume that AGI safety and alignment people would be from all walks.
*  They are, especially AI these days, but let's see. I used to be able to list five or 10 former physicists, AGI people, off the top of my head. I'm not sure I can do that right now.
*  Okay, well, I'm not going to talk much here, and we're going to get right to your introductory remarks. So you've prepared a few slides for people on YouTube, but you've designed it such that people listening at home should be able to follow along just fine.
*  So what I'm going to do is let you just go ahead and take the floor and talk about what you're doing, what you're concerned about, and how you're going about doing it, and whatever else you want to say.
*  Okay, and then we'll come back and have a discussion about it.
*  All right. Yeah, I made sure that the slides are completely useless for the benefit of the audio listeners.
*  Yeah, thanks for inviting me.
*  I was going to start with a few minutes on what I'm working on and why.
*  So the big question that I'm working on is what happens when people figure out how to put brain-like algorithms on computer chips. So I claim that this is something that's likely to happen sooner or later, so it's well worth thinking about.
*  And when I bring this up to people, they tend to split into two camps based on how they think about that. Either they think about these brain-like algorithms on computer chips as a tool for people to use, or they think of it as like a new species.
*  So let's start with the tool perspective.
*  So this is the perspective that's going to be most familiar to AI people, because if you put brain-like algorithms on computer chips, that is a form of artificial intelligence.
*  And the way that everybody thinks of artificial intelligence these days is it's a tool for humans to use. So if that's your perspective, then the sub problem that I'm working on is accident prevention.
*  So we're concerned about the situation where the algorithms are doing something that nobody wanted them to do, not its programmers, not anybody. For example, being deliberately deceptive.
*  And you can say, why are people going to write code that does something that they don't want it to do? And the answer is this happens all the time.
*  When it's a small problem, we call it a bug. When it's a big problem, we call it a fundamentally flawed software design, but it's certainly a thing.
*  So the technical problem to solve here is if people figure out how to run brain-like algorithms on computer chips, and they want those algorithms to be trying to do X, where X is solar cell research or being honest or whatever the programmers have in mind,
*  then what source code should they write? What training environments should they use? And so on. So this turns out to be an unsolved problem and a surprisingly tricky one.
*  Just to give you a hint of why it's not straightforward, you could consider, for example, humans have an innate sex drive, which you could think of as a mechanism that evolution put in us to make us want to have sex.
*  But it doesn't work reliably. A lot of people have a perfectly functional innate sex drive, but choose to be celibate.
*  Whereas another example, parents are always trying to get their children to be indoctrinated into religion A, but then the children grow up and join religion B, things like that.
*  If you want an AI example instead of a human example, there's long lists of funny ones where the AI algorithms did really ingenious things that the programmer didn't intend and didn't think of and certainly didn't want.
*  One of my favorites is somebody made a reinforcement learning algorithm that would make a robot arm grasp an object.
*  And what ended up happening was the reinforcement learning algorithm learned to place the robotic arm between the object and the camera such that it looked like it was grasping the object when it was not.
*  So you can find lots of examples like that. And again, those all just go to show that solving this problem is not straightforward.
*  And it turns out to be really tricky for pretty deep reasons. And that's a problem that I and others in the field are working on.
*  So, meanwhile, there's probably some people who are really up in arms at this point.
*  Maybe the like neuroscientists and biologists, saying that if we put brain like algorithms on computer chips, we should not think of them as a tool for humans to use we should think of them as a species as a new intelligent species on the planet.
*  And incidentally, species which will probably eventually vastly outnumber humans and think much faster than humans and be more insightful and creative and competent.
*  And they'll be building on each other's knowledge and they'll be inventing tools and technologies to augment their capabilities and making plans and getting things done all the things that that humans and groups and societies of humans can do these algorithms alone or in groups ought
*  to be able to do them too. Right. So the big question is, if we're inviting this new intelligent species onto the planet, how do we make sure that it's a species that we actually want to share the planet with?
*  And how do we make sure that they want to share the planet with us? This raises lots of interesting philosophical questions that we can talk about over drinks.
*  But in addition to all of those, there's a technical question, namely, whatever properties we want this species to have, we need to write source code or come up with training environments to make sure it actually happens.
*  And I think that human sociopaths are an illustrative example here.
*  High functioning sociopaths do in fact exist.
*  Therefore, it is at least possible to put brain like algorithms on computer chips that feel no intrinsic inherent motivation related to compassion and friendship and anything like that.
*  And I would go further and say not only is it possible to make algorithms that have human capacity, human like capacity to make plans and and get things done, but that don't feel compassion and friendship.
*  I would say it's strictly easier to do it that way. I think that compassion and friendship are extra things that we need to put into the source code.
*  And I think that in our current state of knowledge, we wouldn't know how to write the source code that does that. So I say let's try to figure that out in advance.
*  So again, that's a question that I and others in the field are working on. Yeah. So in summary, I claim that sooner or later, it's likely that people will figure out how to run brain like algorithms on computer chips.
*  I claim this is a very big deal, probably the best or worst, certainly the weirdest thing that will have ever happened to humanity.
*  And there's technical work today that we can do to increase the odds that things go well. And that's what I'm working on.
*  Okay, so let's thanks for the little thanks for the presentation, little introductory presentation there. I want to go back, I guess, and ask about your background and where you are now. So you're currently working at Astera.
*  Did I pronounce that correctly?
*  Yes.
*  So, how many people like you are at Astera and then in the AI alignment forum in which you posted the series of blog posts, like how big is that community and how active.
*  Let's see, I think, well, I'm the only full time safety person at Astera.
*  By the way, I just want to make clear that I'm speaking for myself.
*  In the broader community, there are various estimates typically like on the order of 100 people, maybe 200 people who are working full time on sort of artificial general intelligence, safety and alignment type problems in the world, which I think is not enough.
*  But yeah, and of them, I'm certainly on the on the very neuroscience side.
*  Yeah, I was gonna ask you how many people, because, you know, you're the series of blog posts is about brain like AI right and so I'm sort of wondering where you fit within that community if you're on the outside in that you're interested in applying brain knowledge and concepts to, first of all, as a way to build artificial general intelligence
*  and then we'll come to whatever help that means in a moment. But, but where, you know, are you accepted by your peers are you ostracized where do you fit in amongst them.
*  I think my work is being well received I certainly have very frequent discussions with other people, and I get a lot of ideas from from others in the community and I'd like to think that they're getting ideas for me to.
*  Good. Okay, so, should we.
*  Does everyone agree on what a GI is in that community or if there are 200 or so folks. Does that mean that there are 200 definitions or perspective.
*  Right. Let's see so.
*  So the thing that pretty much everybody, or at least most people are like thinking very hard about.
*  There's, there's this notion of transformative AI that would change the world as much as the Industrial Revolution or agriculture.
*  And that's a lot of. So everybody is interested in that.
*  And then there are differences of opinions about what transformative AI would look like.
*  Yeah, and one salient possibility is that transformative AI would look like a goal seeking agents, or I guess I should say more broadly, that it would look like.
*  Yeah, agents that can do the sorts of things that humans can do, like, you know, have ideas and and make plans and execute the plans and if the plans don't work come up with better plans.
*  And if they don't know how to do something they can figure it out. They can invent technology, so on and so forth.
*  There are other visions of transformative AI that don't look like that.
*  And I don't really buy into those visions so I'm not going to do a good job of explaining that perspective. But yeah, I guess you could think of it as that's the scenario that I'm working on and I think that's the likeliest scenario.
*  Okay, so before we move on also I'm just curious how you got into this field like where your concern started did you read rereading books like superintelligence by Nick Bostrom or did you just see the rise of artificial intelligence and start to become concerned.
*  Well, I did read superintelligence by Nick Bostrom. That's a lovely book and there's there's other books too.
*  Yeah, by Stuart Russell and there's a book by Brian Christian.
*  I think I had heard about it on by reading blogs, you know, as one does.
*  And yeah, I had been vaguely interested in it for a very long time without really doing anything about it.
*  But then over time.
*  Yeah, my background is in physics, and I had a job where I was learning machine learning and getting involved in brain computer interface projects.
*  So then at one point, maybe four years ago, I had finished a hobby and I was ready for a new hobby. And I figured my next hobby is going to be AGI safety.
*  And my aspiration in my free time was to learn enough about it that I could leave intelligent comments on other people's blog posts.
*  But I actually did way better than that. And a few years, maybe a couple of years after that, I got a full time job doing it. And now I'm on my second full time job doing it.
*  Nice.
*  Okay, so so the series is called and I'll point to it in the show notes is called intro to brain like AISafety.
*  Do I have that right?
*  AGI safety.
*  AGI safety.
*  Yeah.
*  Yeah. And I kind of want to go through some of them, we're not going to be able to hit everything, obviously, but in the series you kind of go through and start from a neuroscience perspective and talk about what you've learned about brains and how you've applied those to develop what you think would be a system capable, at least the beginnings of a system capable in the future of some sort of artificial general intelligence.
*  And then you go on based on that system to talk about some of the problems with where it could go wrong, how it works, how it could go wrong, what needs to be programmed, what needs to be learned.
*  So maybe in a few minutes we can step through a little bit of those overarching principles because they're interesting.
*  But I'm so naive about this stuff that I didn't know that AGI safety was a thing. And then I didn't know that AGI safety was different than the alignment problem or AGI alignment. Could you just talk a little bit about how those fit together and differ?
*  Yeah, I mean, part of this is just branding.
*  Basically, depending on who I'm talking to, I will describe myself as doing safety or alignment.
*  So what I think about it is the term alignment refers to if you have an AI system that is trying to do something, then is it trying to do the thing that you wanted it to be trying to do?
*  And if so, you call that an aligned system. And if not, then it is misaligned.
*  And I think he means that we're sort of thinking more specifically about catastrophic, about accidents in general and in the context of AGI safety, catastrophic accidents in particular.
*  So you think of the AIs escaping human control and self replicating around the internet and things like that, permanently disempowering humanity, all that kind of stuff.
*  And I think we can talk about why that's less fanciful than it sounds.
*  But anyway, safety and alignment are very closely related because if you want your AI to be not causing harm, the best way is to make an AI that doesn't want to cause harm and vice versa.
*  The way to get safety by and large is through alignment.
*  There's people talk about other possibilities like our AI is going to be safe because we don't connect it to the internet.
*  Our AI is going to be safe because we didn't give it access to the nuclear codes.
*  In the blog series, you mentioned an actual website that describes building the perfect box to prevent the AI from doing it, I guess to make the AI as safe as possible.
*  And there are even design plans for this, which is interesting.
*  Yeah, this is an archive paper by Marcus Hutter and colleagues. They have an appendix with a box that includes laser interlocked and airtight seals and a Faraday cage and so on.
*  I don't know why I find that. I don't know why that's amusing. So I should be upfront here and say these are things that I'm glad that you worry about.
*  But someone like me, when I read Nick Bostrom's Superintelligence, and I know that there are plenty of other sources, one of the things that I noticed is that almost every sentence began with the word if.
*  And then it's if this happens, and then if this happens, and then if this happens.
*  My reading, I struggled to get through the book because it was so chock full of these low probability events, which I don't know how you feel.
*  You just mentioned that they might be less fanciful than I might consider them. Right, but the, but the probability quickly goes to zero, if the probability of each of those if statements is even, you know, half or something like that.
*  That was sort of my reading on it. So I have not been that concerned. The other reason why I don't have.
*  Maybe I'm not as concerned as I should be is because, you know, as you know, we don't, we humans don't have a great track record in predicting the future.
*  And I imagine that the future is not. So thinking about developing a GI in general, and then, you know, the safety issue, if you issues with it.
*  I just have this feeling I mean it's not based on anything I guess it's based on our human track record of being terrible at predicting future events and technologies and so on, that the future is going to look vastly different than we can predict
*  right now. So, maybe, you know, I'm curious about, so my temperature of worry of concern is very low.
*  Where would you put your temperature of concern.
*  Yeah, let's see.
*  So there's a bunch of questions here.
*  Yeah, so the first thing is that there's sort of a lot of paths to reaching the conclusion that a GI is going to be very very important in the future.
*  For example, if you don't think that, you know, Nick Nick Bostrom sends a disproportionate amount of his book talking about one, you know, galaxy brain super intelligent agent, and what would it do.
*  I would also say well what if there is a trillion, somewhat human or human level, as with a trillion robot bodies you know controlling the world.
*  And you know that's a different scenario but it's still a very big deal.
*  And I claim, not a low probability of that, you know, either that or something equally weird.
*  What, let's see, or your other. What else. I think I was just ranting about my disdain for that book, and, and just my doubts about how accurate we can be predicting what the future will look like.
*  Yeah.
*  Right. And then, yeah, so you can say, um, a GI is going to be important in the future but there's nothing that we can do to prepare for it.
*  So why think about it. So that's kind of different from not being concerned that sort of being despondent I guess I'm going to look like a real jerk in what 30 years or however many years it takes right.
*  I don't know how many years and neither does anybody else.
*  We can talk about that more too.
*  I think that the best argument for why we should not feel despondent, like that there is nothing that we can do that's going to be reliably good is first of all, there are very concrete and specific things that I claim that we could be doing right now,
*  that would that seem likely to help. I list a bunch of them in the last blog post of the series, open questions that I'm very eager for more people to work on.
*  Yeah, I want to come back to those actually, maybe we'll get back to that. Yeah.
*  Okay. Yeah, like we can point to particular problems like learning algorithms tend to make models that are large and inscrutable and have lots of unlabeled parameters where lots means millions or billions or trillions.
*  And we can't just look at the activations of those parameters and know what the model is doing and why and what it's thinking. That's a problem. I mean it's obviously a problem already.
*  And it seems like it's likely to be a bigger problem in the future. So we can start working on that problem and have, you know, a reasonable theory that that's going to be helpful in the future.
*  Okay, so this might be, we don't have to perseverate on, you know, the likelihood and all that because that could take us down a long road. But let me, this might be just a good time to ask you a question that a listener sent in who couldn't be here because it's
*  3am in Australia and they're sleeping. But this is sort of about that. And yeah, I don't know if this is the right time to ask it but I'm going to. So this is from Oliver, who says and asks, the core assumption behind AGI safety concerns is the quote,
*  which states, he says that any goal is compatible with any level of intelligence. Thus, the super intelligent paperclip maximizer that example that famous example of the super intelligence that you say, I want to, your goal is to manufacture paper clips and destroys the
*  world, extracting resources in order to do so and destroys us all eventually. Okay, but then Oliver continues, but I find it very difficult to imagine a being that is smart enough to learn everything it needs to about physics, psychology, etc.
*  manipulate and destroy us, yet is not convinced by our best ethical theories that imply that they ought not to do so. So in other words for this kind of scenario to make sense. Do you need to assume that our ethical theories are merely parochial prejudices, lacking any
*  objective truth value.
*  Thanks from Oliver. Did you get all that.
*  Yeah, sometimes the way that I think about this is in the context of reinforcement learning.
*  So if you take alpha go, and you give it a reward function of trying to win it go, then it becomes extraordinarily good at winning it go. If you give it a reward function trying to lose at go then it becomes extraordinarily good at losing it go.
*  So I think that the human brain, likewise has a model based reinforcement learning algorithms right at its core. And I think that the sort of analog of the reward function is what I call innate drives.
*  So there's nothing in the world that says that, you know, eating food when you're hungry is good. It's a thing in your brain.
*  There's nothing in the world that says, you know, for any innate drive.
*  It's a thing in your brain and it makes you think that it's great. And, um, well, oversimplifying a bit.
*  I think that Oliver should spend some time as I have employed by high functioning sociopaths.
*  Not my current boss, but I'm sorry to hear about that, by the way.
*  I've heard that in the blog posts as well.
*  Yeah, I mean, just try to imagine talking of a high functioning sociopath into caring about other people. And if that sounds easier, easy to you, then I suggest that you should actually try.
*  I think that people have a lot of intuitions that are related to things like, you know, justice being good and compassion being good and friendship being good and torture being bad.
*  And I think all of those intuitions are sort of rooted in our human innate drives.
*  When we make future AGI's, we get to put whatever innate drives into them that we want.
*  So it could have an innate drive to maximize stock prices. It could have an innate drive to, you know, whatever crazy thing you can think of.
*  And I think of if you can program it, you can put it in. And I hope that future programmers put in the innate drives for, you know, compassion and friendship and not for maximizing the amount of money in its bank account.
*  But we don't actually know how to write the code for compassion and friendship in a drive right now. And that's one of the things that I would like to figure out.
*  I don't know what compassion really is. You know, some of these concepts are also currently ill-defined or not clearly defined.
*  But again, that's sort of besides the point. But these innate drives that you're talking about are going to be, you claim, at least in your version, in your brain-inspired version of AGI safety, are going to be hard-coded in what you call the steering system or the steering subsystem
*  of what an AGI might look like. So maybe we should sort of jump into what your, what your model, current version of your model entails and the concepts.
*  I'm about to throw a lot of, a lot at you. So I apologize for this because I also want to know why you turned, because I know that you've been learning a lot of neuroscience.
*  So why is the question. And then maybe we can kind of step through the components, you know, really high level overarching ideas and concepts of the components.
*  And then on top of that, a third thing, and I will repeat these, is how did you decide where to stop? Like what was important? What are the important principles to abstract from neuroscience and brains to include, right?
*  There's always that question of how much detail to include.
*  Yeah, sorry. So you said, why study neuroscience? Yeah, what, what, what? Maybe I'm a glutton for punishment.
*  Welcome to the club, sir. Yes.
*  I think that there's the big problem in the field of AGI safety that we're trying to prepare for a thing that doesn't exist yet. People sometimes say, what's the point of even trying? We can't do anything until we have AGI's in front of us that we can experiment on.
*  But we can do contingency planning. And one contingency is that the, well, we know that human brains are able to do all these cool things like go to the moon and invent nuclear weapons.
*  And there's some reason that human brains are able to do that. Some principles of learning and search and planning and perception and so on. And whatever those principles are, presumably future programmers could either, either for future neuroscientists could reverse engineer them.
*  Or future AI programmers could independently come up with the same ideas, just like, you know, TV learning was invented independently by AI researchers before they realized that it was in the brain.
*  From my perspective, I really don't care which of those it is. I care about the destination as opposed to which department is the people who gets the credit at the university.
*  Your bet is that AGI will develop via reverse engineering what we know about the only example that we have of whatever AGI is, what we call AGI, the brain.
*  The brain.
*  I think that it's probable that we'll wind up in the same location, but I don't have any strong opinion about whether we're going to reverse engineer it or reinvent it.
*  I do think that it's in vaguely in the vicinity of lots of different lines of artificial intelligence research, most notably model based reinforcement learning.
*  But I don't think that the way that human brains are able to do the cool things that humans can do is exactly the same as any paper that you could find on archive right now.
*  So the AI people are hard at work. They're publishing more papers. They're coming up with new architectures and learning algorithms.
*  And maybe they will reinvent brain ideas. Maybe some of the people who have been on this podcast and elsewhere will study the principles of learning and whatnot in the brain and come up with the ideas that way.
*  But I do think that whenever I see the brain does thus and such, it seems to be like I often have the reaction. Oh, wow. Well, that is a really good way to do it.
*  So and I have trouble thinking of very different ways to get to the same definition. Sorry, get to the same destination that are wildly different from how the brain does it.
*  But a lot of people disagree with me on that. And I sometimes give the cop out response of maybe this is just one possible route to AGI, but we should be doing contingency planning for every possibility.
*  All right. Well, so you have spent plenty of time looking into neuroscience and used some of the concepts to develop what you see as a feasible model for how an AGI might be built and then go on to say that this is how we could solve or potentially solve or address solving at least the alignment and safety problems.
*  So what are the what are the main components in the model and what do they correspond to in brains?
*  Well, let's see. So I should start with the concept of learning from scratch, which is this jargon term I made up because I couldn't find an appropriate one in the literature.
*  So I'll start with two examples of what learning from scratch is, and then I'll say what they have in common with each other.
*  So the first example is any machine learning algorithm that's initialized from random weights. And the second example is a blank flash drive that you just bought from the store.
*  So maybe all of the bits in it are zero or maybe it's random bits. But what those two things have in common is that you can't do anything useful with them at first.
*  So your machine learning algorithm, your convolutional neural net or whatever is going to output random garbage.
*  But then over time, the weights are updated by gradient descent, and it gradually learns to update to have very useful outputs.
*  And by the same token, you can't get anything useful out of your blank flash drive until you've already written information onto the flash drive.
*  So you could think of these as memory systems in a sort of very broad and abstract sense. I just call them learning from scratch.
*  And in the context of the brain, I'm very interested in modules which are learning from scratch in that sense, that they start from,
*  that they emit random garbage when the organism is very young. And by the time the organism is an adult, they are sending out very useful, ecologically useful outputs that help the organism thrive and reproduce.
*  Do you have children? I was just thinking about thinking of my children as random garbage at the beginning.
*  I do have children. They are emitting lots of very useful outputs.
*  By now. Yeah.
*  By now. Yeah. Even at birth, it's possible that learning from scratch has already been happening in the womb, for example.
*  You don't really need sensory inputs to learn to control your own body. So you can have a reinforcement learning algorithm that can control your own body.
*  And that would be learning from scratch, but it can already start in the womb. And it doesn't really need to be learning from the outside world.
*  Right.
*  So my hypothesis is that 96% of the brain is learning from scratch in that sense, including the whole cortical mantle, the neocortex and hippocampus, the whole striatum, amygdala cerebellum.
*  That's by volume, right? 96% of the brain is learning from scratch.
*  And that's the only way that we can learn from scratch.
*  Yeah.
*  Yeah, probably similar by mass or neuron count. And the big exceptions are the hypothalamus and brainstem, which I think are not learning from scratch in that sense.
*  So I'm very interested in whether that's true or false. It seems to be an under discussed question, in my opinion.
*  I think some people agree and other people disagree. But it's really central to how I think about the brain.
*  So that learning from scratch system is, or that learning from scratch algorithm, I suppose, is contained, you know, lots and lots of different objective functions within what you call the learning subsystem, which consists of, in the brain, consists of the cortex, cerebellum, thalamus, basal ganglia, and so on.
*  And then so that's kind of that's the learning subsystem. And then you have what you think is understudied in neuroscience and you put a call out for more neuroscientists to study the what you call the steering subsystem.
*  So maybe you can describe that as well.
*  Yeah, so that would be the rest of the brain, especially the hypothalamus and brainstem and a few other odds and ends.
*  I think that, yeah, if we go back to the reinforcement learning context, a big thing that, so the reason that I'm calling it the steering subsystem in the series is that one of the very important things that it does is steer the learning algorithms to emit ecologically useful outputs.
*  And a big way that it does that is through the reward function in reinforcement learning. The thing that says that touching a hot stove is bad and eating when you're hungry is good, as opposed to the other way around.
*  So I think that all the innate drives.
*  Well, I think that it's probably somewhat more complicated than just a reward function in the brain.
*  But if we just simplify it to a reward function for the sake of argument, all the innate drives that we have, including things like compassion and friendship and envy, all the social instincts are implemented through this reward function, as far as I can tell.
*  And I'm very interested to know exactly how that works.
*  I think that's a big open question that I wish more people were working on. And I think that that's the kind of work that involves sort of thinking about what the hypothalamus is doing and different parts of the brainstem are doing in the context of reinforcement learning and learning algorithms more generally.
*  But you see these so in the terms of the computer metaphor for the brain, you see these as the hard coded parts of the brain essentially the steering subsystem right so in neuroscience, you would call these innate
*  innate structures of the brain that were born with and have been honed through evolution, right.
*  I mean, obviously, there are lots of genes doing lots of things in the neocortex and the striatum too.
*  I mean you can just look at them you see all the different side of architecture and so on.
*  There's, but I do think that there's a big difference between the two.
*  So in the context of the neocortex, if, if you know this part is a granular and that part is granular, I think of that as sort of an innate neural architecture and innate hyper parameters, which might be different in different parts of the architecture
*  and different in different stages of life and so on.
*  Whereas, so you could think of it as sort of disposition to learn certain types of patterns rather than other types of patterns, but it still has to learn the patterns.
*  And that's a big difference from what I think is happening in the hypothalamus and brainstem, where it's just saying directly what's good and what's bad and what should be done.
*  In some cases, the hypothalamus and brainstem will just do things directly through the motor system without involving the learning algorithms at all.
*  So, you know, if the mouse runs away from incoming bird, it doesn't need to learn to do that because there's sort of specific circuitry in the brainstem that looks for birds and that makes the mouse scamper away when it sees it, as far as I understand.
*  And so, it will override any of the learning subsystems interfering in that case plans, right?
*  Yeah.
*  Well, often and not only that but that's sort of the ground truth that will help the learning systems to do similar things in the future.
*  So, if I imagine that, you know, maybe the amygdala notices that.
*  So, it would be maybe the first time that the mouse sees a bird from overhead.
*  The superior colliculus has its vision processing systems and it can notice that there's a bird and say this is a good time to be scared.
*  This is a good time to scamper away.
*  And so, while the amygdala gets a kind of ground truth signal from that and says this is a good time to be scared.
*  And it can look for sort of arbitrary patterns in what it's thinking and what it's doing, where it's at, not just the amygdala probably other parts of the brain too.
*  And they can learn more sophisticated patterns that can sort of preemptively do things that the brainstem would be thinking is a good idea.
*  So, we have these, the steering subsystem, and the learning subsystem.
*  So how do they communicate and then I want to eventually get to the concept of what you call ersatz interpretability.
*  How do they communicate, and how does that drive the behavior and the learning of the AGI, I'll say.
*  Yeah.
*  This is this is a question that I wish I had a better answer to myself and I'm still trying to learn about it myself for example.
*  Just the other day I was reading about exactly what do neuropeptide receptors do in the striatum as an example of, of something that I'm still a little hazy on the details.
*  So, to be large, if we start from the reinforcement learning perspective, then we would say, the steering subsystem, one of the things that does is send a reward function up to the learning subsystem.
*  And then the learning subsystem can learn a value function and then take good actions that are seem likely to lead to rewards.
*  I think that it's actually more complicated than that, though.
*  If you dig a little deeper into the reinforcement learning literature, you can find examples with multi dimensional value functions, where instead of one reward maybe there's 10 rewards, and you learn a value function for each of the rewards that kind of predicts the
*  different rewards.
*  So, that might be a little bit of a better analogy because, um, if you think about it, I could have some thought or memory, and it does it. It has a valence maybe I think it's a good thought or a bad thought, but it can also have other evocations it can make
*  me feel goosebumps, it can make me get stressed out, you know cortisol.
*  It can make me,
*  I mean, feel envious or whatever. Um, so I think that there's
*  just just like reward can sort of lead to a value function that anticipates the reward, there can also be ground truth goosebumps that leads to anticipation of future goosebumps and ground truth cortisol that leads to anticipation of future cortisol and so on and so forth.
*  Okay, Abby you have your hand raised.
*  So unmute yourself if you want to jump in and ask question.
*  Hi friend. Yeah, I was wondering on the API safety front. I think there's also a group that considers not just you know safety for humanity from the API but also safety for the API itself.
*  And so, kind of a reproductive responsibility for these agents were bringing into existence, and I was wondering what your thoughts were, since you know you're coming from it from a, you know how the brain works perspective.
*  And, you know, there's my perspective where that could increase the chance that there's artificial phenomenology happening here. And, you know, the structures in the AI are mirroring the structures in our brain in ways that we can recognize this you know pain suffering in the
*  What are your thoughts on as someone who's looked into it.
*  On yeah on this approach to a GI through emulating brain systems versus others.
*  Thanks for the question. That's a great question.
*  Yeah, so what do we owe these future API algorithms. Are they going to be conscious or not in a sort of phenomenal logical and morally relevant sense is a question on which I don't claim to be an expert.
*  I think that I have high confidence that it is the least possible to make that that future API systems will be conscious and morally relevant sense. I would go further and think and say that it's likely, but I don't have great confidence on that.
*  If then sort of a separate question is what do we do with that information.
*  I think the immediate place that most people's minds jump to is, they get worried that humans will mistreat the AGI eyes, and I am worried about that too. I think that's certainly a legitimate worry.
*  I'm also worried that the AGI eyes will wind up in charge of everything, and then they'll be mistreating the humans. And I'm worried about the AGI eyes mistreating each other, too.
*  From that perspective, it seems to me that at least one useful thing to do is what I'm trying to do, which is to try to better understand and control the motivations of the AGI.
*  The fact that AGI's are probably likely to be conscious just makes everything sort of more complicated, and I'm not sure exactly what to do about that. I'm not sure that's a great answer, but that's my answer.
*  Oh, you're chilling. No, that's perfect. I think that I was thinking more specifically along the lines of the approach of emulating biological systems versus more disconnected ways of organizing a system towards AGI, where it's like, okay.
*  And your perspective on, hey, should we be going down this path of emulating biological systems, or should we be exploring other paths that don't mimic or emulate or represent natural systems that we give moral consideration to already?
*  And if you think that, hey, you know, emulating biological systems isn't that bad, reasonable, the sort, which I am very open to, or yeah, if we should, there might be merit in going to a more disconnected, unlike biological systems approach to AGI development.
*  Yeah, so let's see. So you touched on a couple issues there. One is, if we have a choice of making conscious AGI's or, you know, not phenomenally conscious AGI's, which one would we pick?
*  And I guess if I had the choice, it seems like the non-phenomenally conscious ones would make things a little less complicated to think about from a moral standpoint. I'm not sure that we will have the choice.
*  And yeah, it might just be something that we have to deal with. I should also clarify that I'm not like, my official position on whether brain-like AGI is better or worse than other paths to AGI, all things considered, is that I don't have an opinion.
*  And I consider that my research is trying to figure out what the answer to that important question is. Yeah.
*  But your models don't, or your proposed model doesn't explicitly build in something to attempt to create consciousness. And, you know, it's lacking a lot of psychological concepts like working memory and attention and things like that, that I presume that you think about and may want to build in eventually.
*  But that's why I'm, you know, part of my question was, how did you decide what to leave in, what to leave out? What were the core principles, right, that were important for when you were building this model?
*  So for example, the idea, the hypothesis of learning from scratch can be true or false. I think it's a meaningful question, whether that's correct or not, independently of all the complexities within the learning algorithms itself.
*  So for example, I think of working memory as sort of a type of output or action, among other things. And we don't have to take a stand on what exactly the space of outputs and actions are.
*  Or I should say that more carefully. I think that, well, it's fine. Anyway, I think that you can make a decision to hold something in working memory in a at least loosely analogous sense to you can make a decision to move your arm.
*  I've tried to focus on the things that seem directly relevant for safety, which tends to be things like, what does it mean for an AGI to be trying to do something? And how can we control what it is that the AGI is trying to do?
*  And if we want the AGI to have sort of pro-social motivations, then how would we go about doing that? So not everything is relevant to that. Protein cascades inside neurons are not relevant to that.
*  The gory details of how the neocortex learns and works are not relevant to that. And yeah, so I tend to be sort of having questions in my mind, and then I try to answer those questions. And sometimes I get the right answer, and sometimes I remain confused.
*  And sometimes I think I have the right answer and then it turns out that I don't. And then I have to go back and edit my old blog posts.
*  Okay, so I'm sorry we're jumping around here, but there are more questions from the chat now. This was related. Both of them are really related, I guess, to what Abik was asking.
*  Donald asks, does the concept of death or a kill switch play into the development? So this goes back to runaway AGI. Well, yeah, runaway, potentially dangerous AGI. Can't we just kill it?
*  Yeah, so I mentioned earlier the difference between safety and alignment. So we don't have a great solution to the alignment problem right now. We don't have any solution to the alignment problem right now. I'm working on it and other people are working on it.
*  But at the moment, we don't have a great solution. And when people hear that, they say, let's try to get safety without alignment. So that means that we don't know for sure how to make sure that the AGI is trying to do the things that we want it to do.
*  We can't really control the AGI's motivations. Maybe the AGI is motivated to do something vaguely related to what we were hoping, or maybe not even that. But the AGI is not going to do anything dangerous because we're locking it in a box and we're not giving it internet access and we're going to turn it off if it tries to do anything funny.
*  So pretty much the consensus of everybody in this field is that that's not a great approach. Maybe it could be used as an extra layer of protection, but it's not a central part of the solution. And there's a lot of things that go wrong.
*  The first thing that goes wrong is that even if you don't let your AGI access the internet, what if the next lab down the street or across the world lets their AGI access the internet? So boxing doesn't work unless everybody does it. The other problem is, what are you going to do with this AGI that might have bad motivations and is in a box?
*  So every output that it sends you might be some useful thing that you wanted it to do, but it could also be part of some dastardly scheme to escape from its box. And how are you going to know? Again, the activations inside this neural net model might be trillions of parameters.
*  And it's just some complicated model. And unless neural network interpretability makes great strides from where it is today, I think our default expectation is that mind reading this AGI is going to be an uphill battle.
*  So yeah, you just have this thing that is in a box and it's kind of useless because you don't trust anything that it's doing. And so you kind of sit around not doing anything and then the next lab releases their AGI from the box.
*  And yeah, even above and beyond that, computer security practices are terrible these days. And we should assume that the box is not going to be leakproof, even if we wanted it to be. So there's a lot of problems with that.
*  I think the better solution, the solution everybody wants is to actually just figure out how to make the AGI have good motivations so that it's trying to do things that we want it to do. And then we don't have to worry about keeping it locked in the box.
*  So would the AGI have control over its own power? I suppose if it was a robot, it would be able to always go plug itself in when its battery got low, etc.
*  Yeah, because we have, well, we won't talk about free will, but we have, I'll just say we have control over our own power, right? And these are what lead to our autonomy and our, you know, drives our motivations and base level inherent drives.
*  But, you know, an AGI, which would presumably require electricity or some source of power, wouldn't have those base inherent motivations unless you hard coded them into what you're calling the steering system, I suppose, right?
*  Well, there's a big problem, which is that, yeah, you might be wondering why I keep talking about the AGI trying to escape the box. Why is the AGI trying to escape the box? If we don't want it to escape the box? The problem is, presumably, we want the AGI to be doing something, designing better solar cells, you know, curing cancer, whatever it is.
*  And the problem is, almost no matter what an agent is trying to do, it can do it better with more resources, and it can do it better if it isn't getting shut down. So let's say we make this AGI that just really wants there to be better solar cells.
*  We have this, you know, mediocre ability to sculpt the motivations of the AGI, and we're able to sort of put some solar cell related motivations into it, but we're not able to fine tune the motivations well enough that it's following human norms and so on and so forth.
*  And yeah, so if the AGI wants to invent better solar cells, the problem is, the best way to invent better solar cells is to convince the humans to let you out of the box and then self replicate around the internet and earn lots of money or steal lots of money and, you know, build lots of labs and do it that way.
*  You can sort of imagine if a bunch of eight year olds have locked you in prison, and you just really, really want to invent better solar cells, what's the first thing you're going to do? Escape prison, and then you can invent the better solar cells.
*  So it's not that the AGI's have this natural yearning to be free, you know, see the blue sky under their heads or whatever. It's that escaping is a good way to accomplish lots of goals.
*  This is called instrumental convergence in the biz, by the way.
*  The biz, yeah.
*  Okay, we have the age old question. So I'm assuming you're just going to solve this and answer it right now, Steve.
*  Hannah asks, how would we know if a brain like AGI is conscious? And I'm wondering how we would know if Hannah is conscious, because that's the, you know, it's a philosophical conundrum, right? So you want to address that?
*  Yeah, I want to reiterate that I'm not an expert on, you know, digital sentience or consciousness. As far as I can tell, from my humble perspective, if the AGI is able to write philosophy papers about consciousness, despite us never telling it anything about
*  consciousness, and they kind of sound like human papers, not only that, but doing it for similar reasons based on similar underlying algorithms going on in its, you know, digital brain as the algorithms that go on in our human brain lead to the same output discussions of
*  consciousness, then I would feel awfully like that's a conscious algorithm. I think that that's necessary. Sorry, I think that that would be sufficient. I don't think that that would be necessary. It's probably, as far as I know, possible to get an AGI that's conscious but doesn't write essays about
*  consciousness. And in that case, I don't really know. I remain somewhat confused on the topic myself.
*  I think we all are, whether we admit it or not. Okay, so Donald commented about his earlier kill switch question, just saying that he was thinking more that part of our motivations for making good choices was our self preservation, right? This inherent drive to stay alive.
*  So that the AI might need similar fear of death to develop good choices. I don't know, are good choices a consequence of fear of death? I make maybe maybe good and bad choices are not sure that they're connected.
*  Um, yeah, I mean, in my mind, it would be good if supposing that we wanted to turn the AI off, that the AI didn't try to trick us into not turning it off. So in that sense, fear of death is exactly the opposite of what we would want in AI to have.
*  All right, what's the climbers name Alex Arnold aren't Arnold who does the free free solo like climbs without ropes and he has no no fear of death. He seems to be he seems to have his morals intact, but I'm not I don't know the guy.
*  Okay, so these are good questions, guys. So keep keep jumping in with the questions. I don't mind jumping around. I hope Steve that this is okay with you.
*  Fine with me.
*  See if we'll lose the audience, either way, perhaps.
*  So, I don't know where we were, you know, we were talking. So we're talking about the model kind of and how you base it on on loosely on the brain and how you conceive of two systems in the brain, communicating with each other.
*  And I don't know if maybe someone Chris is saying that Alex Arnold's amygdala is smaller than average. I'm not sure if that's true. Sorry for the interruption.
*  One of the. I mentioned this before because you put out a call to neuroscientists to start working on the basal parts in the brain that roughly correspond to what you call the steering subsystem, that there's a dearth of research on this because all of neuroscience is
*  focused on the cool part of the brain, the cortex, the seat of consciousness, right, where all the really neat cool stuff happens. But, but you suggest that designing the steering subsystem, which can corresponds to those more innate, hard coded parts of our brains is probably the most
*  powerful way for us to address the safety problem. So, do you want to just comment on that?
*  Yeah, I should be more clear that the
*  The thing that I think we need more work on is specifically people who have a really good understanding of artificial intelligence in general and learning algorithms in particular.
*  I want those people to be, you know, looking carefully at the hypothalamus and the brain stem, not just BTA and SNCC, but the rest of it too. Sort of answering the question of not just how does the reinforcement learning reward prediction error cause the learned models to update, but also what is the reward in the first place?
*  So, if you're looking at the thing that says that touching the hot stove is bad and eating is good, let's try to get more details on that. You know, what is the part of the reward function that's able to solve these tricky problems? Like, for example, if I'm motivated to be kind to my friends and mean to my enemies,
*  that's exactly as the reward function that leads to me feeling those feelings. There's sort of a tricky symbol grounding problem. There isn't an obvious ground truth that you can program into, you know, the hypothalamus or the brain stem to sort of figure out that this is an appropriate moment to feel envy.
*  If I feel envy about, you know, if I think a thought like, oh, I see my friend Rita won a trophy and I didn't, then that thought makes me feel envious. But, you know, the genome doesn't know what a trophy is and it doesn't know who Rita is.
*  Somehow it has to send this negative reward for envy on the basis of what seems like very little ground truth. I think that that's a solvable problem and I'm just very interested in hammering out exactly what the solution is as implemented in the human brain.
*  But the difficulty in that also is that those ground truths can change depending on context, right? So if I see Rita get a trophy in one context, I'll be really envious if I lost to bowling to her and she won the bowling competition, right, or tournament.
*  But then in another context, I might be happy for her because, you know, I've beat her the last three times and she deserves to win every once in a while, right? So it's the exact same scenario. I see Rita win a trophy and my response is different, right?
*  So like, it depends on how we're moving throughout the world and the context of our recent history and our future possibility and how our, whether we're hungry and all of these different signals, right, that are a function of our living continuous time condition in the world.
*  And I'm even losing myself as I'm saying this, but I agree with you in essence that it is a hell of a tricky problem. But so do you think these are neuroscientists that need to work on this who need to appreciate AGI in these issues or these AGI people who need to go into neuroscience perhaps?
*  I'm happy for both to happen. Let's see. Yeah, everything you mentioned about NV being context dependent and so on is absolutely true. I should mention that, you know, NV as we think of it as an adult human is this complicated mix of our innate drives plus a lifetime of experience and culture.
*  So it's not necessarily, so the things that are innate drives aren't going to necessarily have one-to-one correspondence with, you know, English language words for emotions. It might be a different kind of ontology.
*  But, you know, I look forward to the day when we have a theory that sort of explains all those different aspects of all of our different social instincts and where those come from. Yeah, I would love for neuroscientists to be engaged in that project, especially if I can, you know, yeah, the people who are interested in that.
*  The people who are sort of working on the gory details of the neocortex and so on. I would love for them to be spending a little more time thinking about, you know, what is the reward function and not just how does the reward function cause updates?
*  And I am also trying to get the people in AGI safety interested in neuroscience, I think with some success. But there's very few of those people and they're already doing useful things in the other parts of AGI safety. So I'm concerned about parasitizing them for my own pet projects.
*  Sure. So just not to belabor the point and apologies, because I am naive about a lot of the, you know, the concerns. But there's also the question of what is the perfect age to model an AGI after, right? You think children are, what you call them garbage?
*  I'm just kidding. But, but, you know, do we want our AGI to be a 13 year old, a 24 year old? What's that perfect age? And I know, in your blog posts, you think that that perfect age is your age right now, right, which is our, our own biases we each have.
*  But but my point is that those reward functions, you know, change through development also, which is just another dimension of that context specificity.
*  Yeah, I hope that we can make AGI's that don't experience teenage angst. I would be, I'm very optimistic that nobody's, I think that teenage angst is a thing in the genome that's rather specific. And I think that nobody's going to be going out of their way to figure out how that thing works and then put it into AGI's.
*  At least God, I hope not. I think of within lifetime learning in humans as you know, a learning algorithm, and the longer it runs, the more capable the algorithm winds up.
*  I don't know. So the reason I brought that up in my blog post was I wanted to address the question of timelines, for example.
*  If it turns out that we need to run an AGI algorithm for 35 years to make it as, you know, generally intelligent as a 35 year old human, then that means that we're not going to have AGI at least for 35 years, plus however long it takes us to press go on that training.
*  I think that it's unlikely, very unlikely to actually take that long for quite a variety of reasons. I think that the brain speed is very different from AGI speed. We can get into all the differences.
*  So we're going to have to, we're going to take a step back and we were talking about consciousness, a few moments ago. And so Hannah is talking now about pain, right. So if we're building brain like AGI, Hannah is concerned that we're going to begin by building subhuman brain like AGI's with subhuman intelligence who cannot tell us when they're in pain.
*  So presumably if things like consciousness and pain come along for the ride and building these things, again, this is concern directed toward the AIs themselves, I suppose.
*  Yeah, I'm not sure I have much to add to that, but that seems true. I tend to spend most of my time thinking about the sort of later stages when we have AGI's that where there's, you know, trillions of AGI's possibly controlling the world who are using language and so on and so forth.
*  And maybe humans wouldn't be in a position to cause them pain even if they wanted to.
*  But yeah, it's funny that, and a little bit depressing that nobody seems to be thinking too hard about whether reinforcement learning algorithms of today are experiencing pain. My best guess is that they're not, but it's very hard to be highly confident about that kind of thing.
*  So we talked a little bit about explainability and interpretability and what you call airsats interpretability. So, you know, presumably it's important for us to be able to look into the AGI's computations and algorithms and make some sense of them, especially when the
*  When the steering system and the learning system are, you know, interacting and we're trying to interpret what's happening with everything that's inside, so that we can, from the safety perspective, so that we can alter things if we need to, right?
*  So what is airsats interpretability? Maybe you should define airsats too, because I actually knew what it was, but you define it in the blog post. And I know it from airsats coffee from, I think World War II or something.
*  Yeah, that's the I think that's where the term comes from. Airsats means cheap imitation. So what we really want for interpretability for quite a number of reasons is that we understand what the AGI is thinking in all this full glorious detail.
*  I am hopeful
*  that
*  we will get that.
*  I guess I shouldn't say that. I would love it if we got that. I am pessimistic that we will get that.
*  If we could get that it would solve all kinds of problems. You wouldn't have to worry about the AGI deceiving you because you could just check what it's thinking and why it's emitting the words that it's emitting. Is it emitting them for a good reason or for a bad reason?
*  If you had full glorious interpretability and you wanted an AGI that is motivated to be honest, then you could catch it lying a few times with perfect reliability and give it negative rewards and hope that it generalizes from that.
*  If we're just going off of AGI behavior, then there's no way to send a reward signal that is clearly for the AGI lying as opposed to the AGI getting caught lying. We want the AGI to be motivated not to lie, but it's not so good if the AGI is merely motivated to not get caught lying.
*  My little term, ersatz interpretability, is to say that if we don't have full glorious interpretability of this billions or trillions of parameter model corresponding to the neocortex and striatum and so on, it's not like we will know nothing whatsoever about it.
*  We'll get little glimpses of what's going on. So in the context of reinforcement learning, the value function is one example of that. If you look at the value function, you get an idea that whether the AGI thinks that the thought that it's thinking is a good thought or a bad thought.
*  You don't know why, but you know that it's really happy about its current thought or plan.
*  And we can do a little better than that in sort of the same way that the amygdala can learn that something is going to lead to goosebumps.
*  I think the amygdala may be subgenual cingulate cortex or whatever. Some part of the brain is learning that something's going to lead to goosebumps or lead to nausea or lead to crying.
*  You can sort of train up models like that too, that are sort of parallel to a multi-dimensional value function. And then you get a little bit more information.
*  I'm not sure that anything like that is sufficient, but it certainly seems like a step in the right direction.
*  All right, Steve. So I'm aware of the time and I know that we haven't gone through and we've been jumping around and we haven't gone through in any sufficient detail your model and how it relates to brains.
*  But I recommend that people go check out the blog series post. And I think maybe in the last few minutes, maybe we can just go over some of what you see as the most important open problems in AGI safety.
*  And I should say, in the blog post, you spend some time clarifying that you and no one has a solution to the alignment problem itself and or safety more generally.
*  But you sort of hint at some directions and some of the most important problems these days. So maybe you could talk about one or two of the problems that you think are most ripe or most important to be working on.
*  Yeah, the one for neuroscientists
*  that I'm particularly excited about is trying to get a better handle on how the genome puts social instincts into us.
*  And I think this involves trying to understand circuits and probably the hypothalamus and how the circuits interact with learning algorithms in the brain.
*  I think that there are learning algorithms involved, but that it's far from obvious exactly what their ground truth is.
*  I have some sort of speculation in post number 13 of the series, but I don't have an answer. I'm sort of working on it, among other things, but certainly more eyes on that problem would be great.
*  So, yeah, I'm happy for for people to be reading the effects of neuroscience textbooks and stuff like that.
*  But really just sort of trying to connect those ideas to the idea that the neocortex is a learning algorithm, striatum is a learning algorithm.
*  And how do those learning algorithms connect to social instincts? What's the loss function?
*  Those kinds of questions, I think, would be really good, because if we know how the genome makes humans sometimes nice to each other, then maybe we can build off of those ideas when we're trying to brainstorm how to make AGI's be nice to humans and to each other.
*  So that would be that would be my number one for neuroscientists in particular.
*  It's good. You want to add one more and then just a few closing questions for you as well.
*  Let's see, I guess for one thing I'm particularly interested in for AI people in the audience that I think doesn't get enough play.
*  That's why I brought it up is making really big and really good and really human legible world models that are open source.
*  So for example, psych CYC is an example of one that was made laboriously over the course of many decades.
*  Maybe there's a Doug. Is this Doug Lynette? Yeah.
*  Yeah, that one.
*  So that's this. So that one's not open source, regrettably.
*  Maybe there are ways to use machine learning to make open source ones, but the important thing is that they be human legible.
*  And the reason that we care. Well, there's a number of reasons for that.
*  But maybe the simplest one is that if we have this big opaque world model that was learned from scratch.
*  By, you know, fitting sensory data and so on.
*  And we're having trouble making heads or tails of it.
*  It would be helpful if we can try to sort of match up latent variables in this big, opaque world bottle with concepts in a human legible world model.
*  So I want to see, you know, really big and awesome and accurate human legible world models.
*  And that's definitely seems like an attractable problem for machine learning people to be working on.
*  All right, Steve.
*  There are just so many issues that are beyond the scope of our current knowledge or our immediate future knowledge, at least that we can tell.
*  This, you know, you talked about having had a, you know, you're working on a hobby.
*  And it was time for you to get a new hobby. This, have you found your calling? Is this, do you consider this a hobby or?
*  And how long do you think this hobby will last? Because it seems like it could last forever.
*  At least, well, or until AGI happens.
*  Yeah, I have not started a new hobby. This is, I spend, I'm going all out on AGI safety. I think it's really important.
*  And I expect to stop working on it when we get to our post AGI utopia or certain doom, either way.
*  So is there anything that would convince you that AGI safety is not an issue or that AGI is not going to be a thing?
*  Do you see it as inevitable or? Yeah, go ahead.
*  And then, and then we'll, we'll close with now you have to do the prerequisite, the required estimate of when AGI will happen.
*  Oh, fun. Yeah, let's see. I mean, I can imagine things. There are certainly empirical facts that are very relevant to my assessment that AGI safety is important.
*  For example, I have a strong belief that it is feasible to run AGI on, you know, an affordable number of computer chips.
*  Let's say, you know, millions or billions of dollars, but not quadrillions of dollars worth of computer chips.
*  My best guess is low millions based on estimates of how much computation, you know, how many operations per second does the human brain do?
*  How many operations over the course of a human lifetime?
*  It seems very likely to me that once we know more information about how the human brain works,
*  there's not really going to be anything stopping people from putting those algorithms on computer chips in terms of like cost or feasibility.
*  I think it's that we're currently limited by the algorithms. If somehow I were convinced that it's just fundamentally impossible to put these algorithms on, you know, enough silicon that, you know, fits in the world supply of sand, then I would no longer be interested in AGI safety.
*  What if I could convince you that brain processing was not algorithmic fundamentally?
*  So I'm a physicist. I think that the universe, I believe in a, you know, clockwork universe that follows legible laws and that are in principle simulated in physics.
*  So there's a question of, you know, computational tractability or intractability, but I don't think it's fundamentally impossible to simulate a brain on a computer chip.
*  Okay. So what's the number? How many years from now?
*  Yeah, so I don't know, and neither does anybody else. There's a school of thought in neuroscience that says that the human brain is just so enormously complicated that there's just no way, just no way at all that we'll possibly have AGI in 100 years or 200 years or 300 years.
*  People will just throw out these numbers. And I really want to push back against that because I think it's delusionally overconfident. I think that technological forecasting is much harder than that.
*  There are a lot of examples in history where, you know, there was one of the Wright brothers said that they were 50 years away from flight and then they did it two years later.
*  I think there was a New York Times op-ed that said that they were a million years away from flight.
*  There's examples in the opposite direction too. Yeah, technological forecasting is hard. We're not going to have conclusive evidence one way or the other.
*  But we still need to make decisions under uncertainty.
*  We weigh the pros and cons of under preparing versus over preparing. And I find this funny thing where I say, I don't have definitive proof that we're going to have AGI in the next 25 years.
*  And what people hear is there is absolutely no way that we're going to have AGI in the next 25 years, as if the worst possible thing imaginable is preparing for something that doesn't happen.
*  And yeah, that's just not how you make good decisions under uncertainty.
*  Sometimes I like to bring up the analogy that the aliens are coming and the invasion might happen in one year or might happen in 50 years. We don't really know.
*  It depends on the jet stream or whatever.
*  But we're not prepared for them and we don't know how long it'll take to prepare for them and we don't know how much notice we'll get.
*  So it's really obvious to everybody in that scenario that we should start preparing straight away and not twiddle our thumbs and do nothing.
*  And I think that's the right idea here too.
*  But having said all that, I do actually think that if I had to guess that that brain like AGI is something that could well happen in 10 or 20 or 30 years, and not in the hundreds of years like the eminent neuroscientists think.
*  And I have a couple of reasons for that, which I'm happy to spell out.
*  Please, yeah, please.
*  So the first one is that, well, I guess first and foremost, the question I'm interested in is how long would it take to understand the brain well enough to make brain like AGI.
*  Whereas the question that a lot of other people are asking is how long would it take to understand the brain completely.
*  And these are different questions. The first reason that they're different is that understanding a learning algorithm is a lot simpler than understanding a trained model.
*  So for example, in, you know, one machine learning course, you can learn how to make a convolutional neural net.
*  But if you ask the question of how, what are all these 25 million parameters doing and why, in order to distinguish a tree from a car.
*  That's just a really really complicated question.
*  So if you look at the cognitive scientists, they will be doing experiments on adult humans and they say how does the adult human do such and such intelligent task.
*  And that is a trained model question, or at least it's partly a trained model question. It's not a learning algorithm question.
*  So I claim that we'll be able to make brain like AGI long before we have the answers to questions like that.
*  So that's number one. And then the other one is that models are much simpler than their physical instantiations.
*  So again, you know, the person who takes a machine learning course knows how to program a convolutional neural net, knows basically how it works.
*  But if you ask that person, how is it physically instantiated with everything from, you know, semiconductor fabrication and quantum toggling and transistors and CUDA compilers and all that stuff.
*  That's just like decades of work to understand all of that.
*  So by the same token, people studying the brain, you know, you zoom in on any cell and you just find this fractal like unfolding of crazy complexity.
*  And I think that people are going to know how to build brain like AGI long before they unravel all of that complexity.
*  There's an optimistic AI take, and I guess I'll close just by, and I should have mentioned this earlier, one of the things I appreciated reading your blog series and thinking about, you know, people who are working on AGI safety is that someone who's concerned.
*  Someone like you who's concerned about AGI safety, sort of implicit in what you do is also build toward AGI because you're trying to build systems that will be inherently safe or that will mitigate, you know, dangers from the AI.
*  So in essence, you know, you're contributing to the project of building AGI and also at the same time thinking about its safety.
*  So it's just an interesting implicit two things at once wrapped up.
*  So anyway, I just want to say I appreciate that aspect of it.
*  So I think I would kind of push back on that.
*  I think that the right order to do things is to first gain better understanding of whether brain like AGI is what we want to build. And if so, how to build it safely.
*  And then, assuming the answer is yes, and we have a good answer, then, you know, proceed all out in building it.
*  I think that we're still at step one.
*  I try to be conscientious about the things that I publish and don't publish because I don't feel like we're ready for brain like AGI right now.
*  I mean, you know, my individual decisions, I don't have any secret sauce of human intelligence, you know, sitting in my notebooks.
*  It's just a drop in the bucket. But I do like to think of myself as, you know, not trying to build brain like AGI until we're ready for it.
*  All right, Steve, thank you for the thoughtful discussion. Thanks everyone who joined and asked questions.
*  I appreciate it. So I wish you luck in keeping our world safe and, you know, selfishly. So thank you.
*  Thanks for inviting me, Paul. Thanks to everybody on Zoom for coming.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon to access full versions of all the episodes and to join our Discord community.
*  Or if you want to learn more about the intersection of neuroscience and AI, consider signing up for my online course, Neuro AI, The Quest to Explain Intelligence.
*  Go to braininspired.co to learn more. To get in touch with me, email paul at braininspired.co.
*  You're hearing music by the new year. Find them at the new year dot net. Thank you. Thank you for your support. See you next time.
